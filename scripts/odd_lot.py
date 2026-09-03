#!/usr/bin/env python3
"""Odd-lot tender offer screener — discovery, daily re-scoring, and the report.

    python scripts/odd_lot.py discover                 # EFTS -> universe
    python scripts/odd_lot.py rescore                  # re-price the whole universe
    python scripts/odd_lot.py run --dry-run            # both, then print, write nothing
    python scripts/odd_lot.py report 2026-09-03        # render reports/<date>/odd_lot.md
    python scripts/odd_lot.py universe                 # dump what is being tracked
    python scripts/odd_lot.py slot --event-name schedule

Some issuer tender offers accept the shares of holders who own **fewer than
100 shares** ahead of any proration of everyone else's. Buy 99 shares below the
offer price, tender all of them, get taken out at the offer price without being
prorated. The edge is small, entirely mechanical, and evaporates the moment a
detail is wrong — which is why every gate below is a rejection with a reason
attached rather than a score.

The rules, from the filings themselves:

* The threshold is *fewer than* 100 shares, owned beneficially or of record.
* The holder must tender **all** shares owned. A partial tender forfeits it.
* Ownership aggregates across every account by SSN. It cannot be split across
  brokers, accounts, or certificates to manufacture two odd lots.
* An issuer can **remove** the preference mid-offer by amendment (Frontera
  Energy did exactly that in September 2024), so an `SC TO-I/A` has to be read,
  not skipped.
* The preference can be **conditioned** — voided if the purchase would leave
  the stock held of record by fewer than some number of persons (ITEX's
  `SC TO-I` used 300). A conditioned preference is not a preference.
* In a Dutch auction, shares are accepted at prices **at or below** the final
  purchase price, so the low end of the range is the only price you can count
  on receiving.

This module is research output. It places no orders and talks to no broker.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
from collections import deque
from dataclasses import asdict, dataclass, field, fields
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Iterable
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO / "config" / "odd_lot.json"
UNIVERSE_PATH = REPO / "state" / "odd_lot_universe.json"
CACHE_DIR = REPO / "state" / "odd_lot_cache"

sys.path.insert(0, str(REPO / "scripts"))

ET = ZoneInfo("America/New_York")

# A User-Agent the SEC treats as a scraper. Sending one of these earns a 403 and
# a ~10 minute block of the whole IP, which on a shared runner is not only our
# problem — so it is a hard failure at startup, not a runtime surprise.
GENERIC_USER_AGENTS = re.compile(
    r"^\s*(?:mozilla/|python-requests|curl/|wget|okhttp|java/|go-http|libwww)", re.I
)


# --------------------------------------------------------------------------
# config
# --------------------------------------------------------------------------

_config_cache: dict[str, Any] | None = None


def load_config(path: Path | None = None) -> dict[str, Any]:
    """The whole config file, with the SEC_USER_AGENT secret layered on top.

    The env var wins over the file because the file is committed: its contact
    address is a placeholder, and the secret is the address the SEC would
    actually reach a human at.
    """
    global _config_cache
    if path is None and _config_cache is not None:
        return _config_cache
    cfg = json.loads((path or CONFIG_PATH).read_text())
    env_ua = os.environ.get("SEC_USER_AGENT", "").strip()
    if env_ua:
        cfg["sec"]["user_agent"] = env_ua
    if path is None:
        _config_cache = cfg
    return cfg


def check_user_agent(ua: str) -> None:
    """Fail loudly on a User-Agent the SEC will block, before any request goes out."""
    ua = (ua or "").strip()
    if not ua:
        raise SystemExit(
            "No SEC User-Agent. Set the SEC_USER_AGENT secret or config/odd_lot.json "
            "sec.user_agent to '<Tool name> <contact email>'. The SEC returns 403 "
            "without one."
        )
    if GENERIC_USER_AGENTS.match(ua):
        raise SystemExit(
            f"SEC User-Agent {ua!r} looks like a generic client string. The SEC "
            f"returns 403 and blocks the IP for ~10 minutes. Use "
            f"'<Tool name> <contact email>'."
        )
    if "@" not in ua:
        raise SystemExit(
            f"SEC User-Agent {ua!r} carries no contact email. SEC fair-access "
            f"policy requires one."
        )


# --------------------------------------------------------------------------
# rate limiting
# --------------------------------------------------------------------------

class RateLimiter:
    """Sliding-window limiter. The SEC's ceiling is 10 req/s per IP; we sit at 8.

    Two independent brakes, because either one alone lets a burst through:

    * a **window**, holding the timestamps of the last `max_per_second` requests
      — when the oldest is under a second old, sleep until it ages out. This is
      what stops ten calls landing inside the same second.
    * a **spacing** floor of 0.12s between consecutive calls, which keeps the
      steady-state cadence under the ceiling even when the window has room.

    The limit is per IP and aggregated across machines, so two runners sharing
    an egress address share this budget. 8 leaves the headroom for that.
    """

    # Every sleep overshoots its boundary by a microsecond. Sleeping to exactly
    # the boundary can land a float hair short of it, and the remaining sleep is
    # then smaller than the clock's own resolution — so the wait never
    # completes and the limiter spins instead of sending. Overshooting costs a
    # microsecond a request and cannot fail to make progress.
    EPSILON = 1e-6

    def __init__(self, max_per_second: int = 8, min_interval: float = 0.12,
                 clock=time.monotonic, sleeper=time.sleep) -> None:
        self.max_per_second = max_per_second
        self.min_interval = min_interval
        self._clock = clock
        self._sleep = sleeper
        self._calls: deque[float] = deque()
        self._last: float | None = None

    def acquire(self) -> None:
        """Block until another request may be sent, then record it."""
        while True:
            now = self._clock()

            if self._last is not None:
                gap = self.min_interval - (now - self._last)
                if gap > 0:
                    self._sleep(gap + self.EPSILON)
                    continue

            while self._calls and now - self._calls[0] >= 1.0:
                self._calls.popleft()

            if len(self._calls) < self.max_per_second:
                self._calls.append(now)
                self._last = now
                return

            self._sleep(max(1.0 - (now - self._calls[0]), 0.0) + self.EPSILON)


# --------------------------------------------------------------------------
# SEC client
# --------------------------------------------------------------------------

class SecBlocked(RuntimeError):
    """A 403 or 429 from the SEC. Retrying now extends the block, so we do not."""


class EftsSchemaError(RuntimeError):
    """The full-text search response did not have the shape we parse.

    EFTS is undocumented and the SEC reserves the right to change it. A silent
    zero-hit day would look exactly like a quiet week for tender offers, so the
    adapter raises instead of returning nothing.
    """


class SecClient:
    """Every SEC request in this module goes through here.

    Carries the fair-access obligations in one place: the contact User-Agent,
    the rate limiter, the block backoff, and the on-disk cache. A document
    already in the cache is never fetched twice.
    """

    def __init__(self, config: dict[str, Any] | None = None,
                 cache_dir: Path | None = None, limiter: RateLimiter | None = None) -> None:
        cfg = (config or load_config())["sec"]
        self.cfg = cfg
        self.user_agent = cfg["user_agent"]
        check_user_agent(self.user_agent)
        self.cache_dir = cache_dir if cache_dir is not None else CACHE_DIR
        self.limiter = limiter or RateLimiter(
            max_per_second=cfg["max_requests_per_second"],
            min_interval=cfg["min_seconds_between_requests"],
        )
        self._session = None
        self.fetched = 0
        self.cache_hits = 0

    def _requests_session(self):
        # Imported here rather than at module scope so the parsing and scoring
        # logic below stays importable on a runner with nothing pip-installed —
        # see tests/test_no_hard_dependencies.py.
        if self._session is None:
            import requests

            self._session = requests.Session()
            self._session.headers.update({
                "User-Agent": self.user_agent,
                "Accept-Encoding": "gzip, deflate",
            })
        return self._session

    def _cache_path(self, key: str) -> Path:
        safe = re.sub(r"[^A-Za-z0-9._-]", "_", key)[:180]
        return self.cache_dir / safe

    def get(self, url: str, *, params: dict | None = None, cache_key: str | None = None) -> str:
        """Fetch a URL as text, from the cache when we already have it.

        `cache_key` is required for anything worth caching; a request without
        one is always live (the EFTS query, whose answer changes by the minute).
        """
        if cache_key:
            path = self._cache_path(cache_key)
            if path.exists():
                self.cache_hits += 1
                return path.read_text(encoding="utf-8", errors="replace")

        self.limiter.acquire()
        session = self._requests_session()
        resp = session.get(url, params=params, timeout=self.cfg["timeout_seconds"])
        self.fetched += 1

        if resp.status_code in (403, 429):
            wait = self.cfg["block_backoff_seconds"]
            # Deliberately no retry loop. A 403 means the IP is already blocked
            # for ~10 minutes and every further request restarts that clock.
            time.sleep(wait)
            raise SecBlocked(
                f"HTTP {resp.status_code} from {url}. Backed off {wait}s. "
                f"The SEC blocks the IP for ~10 minutes; do not retry immediately."
            )
        resp.raise_for_status()

        if cache_key:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            self._cache_path(cache_key).write_text(resp.text, encoding="utf-8")
        return resp.text

    def get_json(self, url: str, *, params: dict | None = None,
                 cache_key: str | None = None) -> Any:
        return json.loads(self.get(url, params=params, cache_key=cache_key))


_ticker_by_cik: dict[str, str] | None = None


def ticker_for_cik(cik: str, client: SecClient) -> str:
    """The ticker for a CIK, from the SEC's own company list.

    EFTS renders a filer as `ACME CORP (ACME) (CIK 0000123456)`, but only when
    it has a ticker on file for the entity that filed — and a tender offer is
    frequently filed under a holding company or an acquirer that has none. In
    the first live run three of four filings arrived without one, and Gate 2
    rejects an offer it cannot price, so each was dropped before any of its
    terms were considered.

    The map is a single 1MB fetch, cached for the day like every other
    document.
    """
    global _ticker_by_cik
    if _ticker_by_cik is None:
        try:
            data = client.get_json(
                client.cfg["tickers_url"],
                cache_key=f"company_tickers_{date.today().isoformat()}.json")
        except Exception:  # noqa: BLE001 - a missing map is not a failed run
            _ticker_by_cik = {}
        else:
            rows = data.values() if isinstance(data, dict) else data
            _ticker_by_cik = {}
            for row in rows:
                try:
                    _ticker_by_cik.setdefault(pad_cik(row["cik_str"]),
                                              str(row["ticker"]).upper())
                except (KeyError, TypeError, ValueError):
                    continue
    return _ticker_by_cik.get(pad_cik(cik), "")


def pad_cik(cik: Any) -> str:
    """Zero-pad a CIK to the 10 digits data.sec.gov requires. Unpadded 404s."""
    digits = re.sub(r"\D", "", str(cik))
    if not digits:
        raise ValueError(f"not a CIK: {cik!r}")
    return digits.zfill(10)


# --------------------------------------------------------------------------
# EDGAR full-text search adapter
# --------------------------------------------------------------------------

def _efts_highlights(raw: dict[str, Any]) -> list[str]:
    """Snippet text, from whichever key this EFTS build puts it under.

    Decorative — the paragraph quoted in the report comes from the fetched
    document, never from a snippet — so a missing or moved highlight block is
    not worth failing over the way a missing `hits` block is.
    """
    for container, key in ((raw.get("highlight"), "_source"),
                           (raw.get("_source"), "_highlight")):
        if isinstance(container, dict) and isinstance(container.get(key), list):
            return [_clean_text(h) for h in container[key][:3]]
    return []


def _efts_hit(raw: dict[str, Any]) -> dict[str, Any]:
    """One EFTS hit, flattened. Raises EftsSchemaError on an unexpected shape.

    The `_id` is `<accession>:<primary document filename>`, which is the only
    place the response names the document itself — everything else in the hit
    is metadata about the filing.
    """
    if not isinstance(raw, dict) or not isinstance(raw.get("_source"), dict) or "_id" not in raw:
        raise EftsSchemaError(f"hit has no _source/_id: {str(raw)[:200]}")
    src = raw["_source"]
    accession_raw, _, document = str(raw["_id"]).partition(":")
    ciks = src.get("ciks") or []
    if not ciks:
        raise EftsSchemaError(f"hit {raw['_id']} carries no ciks: {str(src)[:200]}")
    names = src.get("display_names") or []
    forms = src.get("root_forms") or []

    accession = _normalize_accession(accession_raw or src.get("adsh", ""))
    cik = pad_cik(ciks[0])
    return {
        "accession": accession,
        "cik": cik,
        "company": _company_from_display_name(names[0] if names else ""),
        "ticker": _ticker_from_display_name(names[0] if names else ""),
        # `file_type` is the *document's* type — EX-99.(A)(1)(III) and friends —
        # not the filing's form. The first live run reported every hit as an
        # exhibit because this preferred it. `root_forms` carries the form.
        "form": (forms[0] if forms else "") or src.get("form") or src.get("file_type") or "",
        "document_type": src.get("file_type") or "",
        "filed": src.get("file_date") or "",
        "document": document,
        "url": document_url(cik, accession, document),
        "index_url": filing_index_url(cik, accession),
        "highlights": _efts_highlights(raw),
    }


def _normalize_accession(raw: str) -> str:
    """`0001234567-24-000123`, dashes and all, from whatever EFTS returned."""
    digits = re.sub(r"\D", "", raw)
    if len(digits) != 18:
        return raw.strip()
    return f"{digits[:10]}-{digits[10:12]}-{digits[12:]}"


def _ticker_from_display_name(name: str) -> str:
    """EFTS renders names as `ACME CORP (ACME)  (CIK 0000123456)`."""
    tickers = re.findall(r"\(([A-Z][A-Z0-9.\-]{0,6})\)", name or "")
    for candidate in tickers:
        if not candidate.startswith("CIK"):
            return candidate
    return ""


def _company_from_display_name(name: str) -> str:
    """`ACME CORP (ACME) (CIK 0000123456)` -> `ACME CORP`."""
    return re.sub(r"\s*\([^)]*\)\s*", " ", name or "").strip() or (name or "").strip()


def document_url(cik: str, accession: str, document: str) -> str:
    base = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession.replace('-', '')}"
    return f"{base}/{document}" if document else base


def filing_index_url(cik: str, accession: str) -> str:
    return (f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
            f"{accession.replace('-', '')}/{accession}-index.htm")


def parse_efts_response(payload: Any) -> list[dict[str, Any]]:
    """Flatten an EFTS response, or say loudly that its schema moved.

    Zero hits is a legitimate answer — most days nobody files an odd-lot tender.
    A *missing* `hits` block is not, and must never be mistaken for one.
    """
    if not isinstance(payload, dict):
        raise EftsSchemaError(f"EFTS returned {type(payload).__name__}, not an object")
    hits = payload.get("hits")
    if not isinstance(hits, dict) or "hits" not in hits:
        raise EftsSchemaError(
            "EFTS response has no hits.hits — the undocumented endpoint has "
            f"probably changed. Keys seen: {sorted(payload)[:10]}"
        )
    rows = hits["hits"]
    if not isinstance(rows, list):
        raise EftsSchemaError(f"EFTS hits.hits is {type(rows).__name__}, not a list")
    return [_efts_hit(row) for row in rows]


# A tender offer is filed as a Schedule TO with the substance in its exhibits:
# the Offer to Purchase, the Letter of Transmittal, the Notice of Guaranteed
# Delivery, the letters to brokers, the summary advertisement. Every one of
# them says "odd lot", so full-text search returns them all — as separate hits
# sharing one accession number.
#
# Keeping one of those and discarding the rest, which is what this did, means
# the filing is judged on whichever exhibit the search happened to rank first.
# When that is the Letter of Transmittal — which has an Odd Lots checkbox and
# nothing else — the offer is rejected for "no acceptance-before-proration
# language" while the Offer to Purchase sitting beside it says exactly that.
# That is the reason the first live run rejected all four of its filings.

def _merge_hit(filings: dict[str, dict[str, Any]], hit: dict[str, Any],
               found_by: str, max_documents: int) -> None:
    """Fold one EFTS hit into its filing, keeping the document as a candidate."""
    filing = filings.get(hit["accession"])
    if filing is None:
        filing = {k: v for k, v in hit.items() if k not in ("document", "document_type")}
        filing["documents"] = []
        filing["found_by"] = found_by
        filings[hit["accession"]] = filing

    if not hit.get("document"):
        return
    if any(d["name"] == hit["document"] for d in filing["documents"]):
        return
    if len(filing["documents"]) >= max_documents:
        return
    filing["documents"].append({
        "name": hit["document"],
        "type": hit.get("document_type") or "",
        "url": hit["url"],
    })


def _efts_page(client: SecClient, config: dict[str, Any], *, term: str, form: str,
               start: str, end: str, offset: int) -> tuple[list[dict[str, Any]], int]:
    """One page of results, and the total the search says it has."""
    params = {"q": term, "forms": form, "dateRange": "custom",
              "startdt": start, "enddt": end}
    if offset:
        params["from"] = offset
    payload = client.get_json(config["sec"]["efts_url"], params=params)
    hits = parse_efts_response(payload)
    total = 0
    try:
        total = int(payload["hits"]["total"]["value"])
    except (KeyError, TypeError, ValueError):
        total = len(hits) + offset  # no total reported; stop when a page runs short
    return hits, total


def search_filings(client: SecClient, config: dict[str, Any], *,
                   today: date | None = None,
                   stats: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    """Every odd-lot-mentioning tender filing in the window, one entry per filing.

    One query per (term, form) pair rather than one big OR: EFTS scores and
    truncates per query, so a busy form would otherwise crowd a quiet one out
    of the results entirely.

    Paginated, because the endpoint returns ten hits per page. Reading only the
    first page silently caps discovery at ten documents per query — and since a
    single filing can account for five of them, that is a handful of filings.
    """
    disc = config["discovery"]
    today = today or datetime.now(ET).date()
    start = (today - timedelta(days=disc["lookback_days"])).isoformat()
    end = today.isoformat()
    cap = disc["max_hits_per_query"]
    max_documents = disc.get("max_documents_per_filing", 8)

    filings: dict[str, dict[str, Any]] = {}
    queries = raw_hits = 0

    for term in disc["query_terms"]:
        for form in disc["forms"]:
            offset = 0
            while offset < cap:
                hits, total = _efts_page(client, config, term=term, form=form,
                                         start=start, end=end, offset=offset)
                queries += 1
                raw_hits += len(hits)
                for hit in hits:
                    _merge_hit(filings, hit, f"{term} / {form}", max_documents)
                offset += len(hits)
                if not hits or offset >= total:
                    break

    if stats is not None:
        stats.update({"queries": queries, "raw_hits": raw_hits,
                      "filings": len(filings),
                      "documents": sum(len(f["documents"]) for f in filings.values()),
                      "window": f"{start}..{end}"})

    return sorted(filings.values(), key=lambda f: (f["filed"], f["accession"]), reverse=True)


# --------------------------------------------------------------------------
# document text
# --------------------------------------------------------------------------

_TAG_BREAKS = re.compile(r"</(?:p|div|tr|table|li|h[1-6])>|<br\s*/?>|<p[ >]|<div[ >]", re.I)
_TAGS = re.compile(r"<[^>]+>")
_SCRIPTS = re.compile(r"<(script|style)\b.*?</\1>", re.I | re.S)


def html_to_text(raw: str) -> str:
    """Filing HTML to paragraph-preserving plain text.

    Paragraph structure is load-bearing here, not cosmetic: the odd-lot
    preference has to be *quoted* into the report so a human can verify it in
    seconds, and a quote is only checkable if it is the paragraph the filing
    actually contains.
    """
    text = _SCRIPTS.sub(" ", raw)
    text = _TAG_BREAKS.sub("\n", text)
    text = _TAGS.sub(" ", text)
    text = html.unescape(text)
    text = text.replace("\xa0", " ").replace("​", "")
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r" ?\n ?", "\n", text)
    return re.sub(r"\n{2,}", "\n\n", text).strip()


def paragraphs(text: str) -> list[str]:
    """Non-trivial paragraphs. Single newlines inside one are folded to spaces."""
    out = []
    for block in re.split(r"\n\s*\n", text):
        joined = " ".join(block.split())
        if len(joined) > 30:
            out.append(joined)
    return out


def _clean_text(value: Any) -> str:
    return " ".join(html_to_text(str(value)).split())


def _normalize_for_match(text: str) -> str:
    """Quote and dash variants folded, so a regex does not miss on typography."""
    return (text.replace("’", "'").replace("‘", "'")
                .replace("“", '"').replace("”", '"')
                .replace("–", "-").replace("—", "-"))


# --------------------------------------------------------------------------
# offer-document patterns
# --------------------------------------------------------------------------
#
# Every pattern below is anchored on language that appears in the filings
# themselves rather than on a paraphrase of it. Two properties matter more than
# breadth: a pattern must not fire on the boilerplate every tender offer
# carries, and a near-miss must fail closed. A missed opportunity costs nothing;
# a false positive puts real money into a trade whose premise is wrong.

# "fewer than 100 shares", "less than one hundred (100) Shares",
# "fewer than 100 of our common shares". Bounded so it cannot leap a sentence.
ODD_LOT_THRESHOLD = re.compile(
    r"(?:fewer|less)\s+than\s+(?:one\s+hundred|100)\b[^.;:]{0,90}?\bshares?\b", re.I)

# The promise that makes the trade: accepted before, or exempt from, proration.
PRORATION_PREFERENCE = re.compile(
    r"(?:accept\w*|purchas\w*|tak\w*|paid|pay\w*)\b[^.;]{0,140}?"
    r"(?:before|prior\s+to|ahead\s+of|in\s+advance\s+of)\s+(?:any\s+)?"
    r"(?:pro\s?ration|prorat\w+|pro\s+rata)"
    r"|(?:not\s+(?:be\s+)?subject\s+to|without\s+(?:any\s+)?|exempt\s+from)\s+"
    r"(?:pro\s?ration|prorat\w+|pro\s+rata)"
    r"|(?:pro\s?ration|prorat\w+|pro\s+rata)[^.;]{0,80}?\b(?:will|shall|does)\s+not\s+apply",
    re.I)

ODD_LOT_MARKER = re.compile(r"\bodd\s+lots?\b|\bodd[- ]lot\s+holders?\b", re.I)

# Whether a document is an amendment is read from the document itself. Neither
# EFTS field reliably carries the "/A": file_type names the exhibit, and
# root_forms is the *root* form, which is "SC TO-I" for an SC TO-I/A. Since
# that flag is what arms the Frontera check below, deriving it from a form
# string would leave the check silently disarmed in production.
AMENDMENT_MARKER = re.compile(
    r"\bamendment\s+no\.?\s*\d+\b|\bamends\s+and\s+supplements\b"
    r"|\bamendment\s+to\s+(?:the\s+)?(?:schedule\s+to|offer\s+to\s+purchase)\b"
    r"|\bthis\s+amendment\s+amends\b", re.I)

# An SC TO-I/A taking the preference away — the Frontera Energy pattern.
PREFERENCE_REMOVED = re.compile(
    r"(?:odd\s+lots?|odd[- ]lot\s+(?:priority|preference|provision)\w*)[^.]{0,220}?"
    r"\b(?:is|are|will\s+be|has\s+been|have\s+been|shall\s+be)\s+(?:hereby\s+)?"
    r"(?:deleted|eliminated|removed|withdrawn|terminated|revoked|amended\s+to\s+"
    r"(?:delete|eliminate|remove))"
    r"|\b(?:delet\w+|eliminat\w+|remov\w+|withdraw\w+|terminat\w+)\b[^.]{0,140}?"
    r"\bodd\s+lots?\b"
    r"|\bodd\s+lots?\b[^.]{0,160}?\bwill\s+no\s+longer\s+be\b",
    re.I)

# The preference voided if the purchase would drop the record-holder count
# below a floor — the ITEX SC TO-I pattern. Only counts inside the odd-lot
# passage: a standalone "fewer than 300 holders of record" is deregistration
# boilerplate that nearly every small-cap tender document carries.
#
# The captured number must be followed by a word meaning *people*. An earlier
# version anchored on "of record" appearing anywhere nearby and then took the
# next number, which matched the odd-lot definition itself — "a holder of
# record of fewer than 100 Shares" — and rejected the four commonest ways of
# writing the preference as if they were the condition that voids it. The
# first live run rejected its entire universe that way.
RECORD_HOLDER_CONDITION = re.compile(
    r"(?:fewer|less)\s+than\s+(\d{2,5})\s+(?:record\s+)?"
    r"(?:persons|holders|shareholders|stockholders|beneficial\s+owners)\b"
    r"|(?:below|under|beneath)\s+(\d{2,5})\s+(?:record\s+)?"
    r"(?:persons|holders|shareholders|stockholders|beneficial\s+owners)\b",
    re.I)

# Narrow on purpose. Every tender offer carries jurisdictional boilerplate
# ("not being made in any jurisdiction where..."), and treating that as a
# restriction would reject the entire universe.
RESTRICTED_OFFER = re.compile(
    r"(?:only|solely|exclusively)\s+to\s+(?:persons\s+(?:who\s+are\s+)?)?"
    r"(?:accredited\s+investors|qualified\s+institutional\s+buyers|QIBs)"
    r"|\b(?:accredited\s+investors|qualified\s+institutional\s+buyers|QIBs)\s+only\b"
    r"|(?:is|are)\s+not\s+being\s+made\s+to\s+(?:any\s+)?(?:holders|persons|shareholders|"
    r"stockholders)\s+(?:resident\s+)?in\s+the\s+United\s+States",
    re.I)

EXCHANGE_OFFER = re.compile(
    r"\boffer\s+to\s+exchange\b|\bexchange\s+offer\b"
    r"|in\s+exchange\s+for\s+(?:newly\s+issued\s+|shares|units|notes|ordinary)", re.I)

CASH_OFFER = re.compile(
    r"\boffer\s+to\s+purchase\s+for\s+cash\b|\bnet\s+to\s+the\s+seller\s+in\s+cash\b"
    r"|\bpurchase\s+price[^.]{0,60}?\bin\s+cash\b|\bfor\s+cash\b", re.I)

# Whichever subject marker appears first in the cover pages is the security
# being tendered for; the rest are capitalization the document mentions later.
COMMON_EQUITY_SUBJECT = re.compile(
    r"\bcommon\s+(?:stock|shares)\b|\bordinary\s+shares\b|\bcommon\s+units\b", re.I)
DEBT_OR_PREFERRED_SUBJECT = re.compile(
    r"\b\d+(?:[.\d]*)?\s*%\s+(?:senior\s+|subordinated\s+|convertible\s+|secured\s+)*"
    r"(?:notes?|bonds?|debentures?)\b|\bdebentures?\b"
    r"|\bpreferred\s+(?:stock|shares|units)\b|\bdepositary\s+shares\b", re.I)

TERMINATED = re.compile(
    r"\bthe\s+offer\s+(?:has\s+been|was|is\s+hereby)\s+(?:terminated|withdrawn|cancell?ed)\b"
    r"|\bhereby\s+terminates\s+the\s+offer\b", re.I)

# "not greater than $12.00 nor less than $10.50" and its mirror image. Order is
# not assumed: min()/max() decide which end is which.
DUTCH_RANGE = re.compile(
    r"(?:not\s+(?:greater|more|higher)\s+than|at\s+or\s+below|up\s+to)\s+\$\s?([\d,]+\.\d{2})"
    r"[^.]{0,80}?(?:nor|and\s+not|or)\s+(?:not\s+)?less\s+than\s+\$\s?([\d,]+\.\d{2})"
    r"|(?:not\s+less\s+than)\s+\$\s?([\d,]+\.\d{2})[^.]{0,80}?"
    r"(?:nor|and\s+not|or)\s+(?:more|greater|higher)\s+than\s+\$\s?([\d,]+\.\d{2})"
    r"|price\s+range\s+of\s+\$\s?([\d,]+\.\d{2})\s*(?:to|-|through)\s*\$\s?([\d,]+\.\d{2})",
    re.I)

FIXED_PRICE = re.compile(
    r"\$\s?([\d,]+\.\d{2})\s+(?:net\s+)?(?:in\s+cash\s+)?per\s+(?:share|Share|unit)"
    r"|(?:purchase\s+price|price)\s+of\s+\$\s?([\d,]+\.\d{2})\s+per\s+(?:share|Share|unit)"
    r"|\$\s?([\d,]+\.\d{2})\s+per\s+(?:share|Share|unit),?\s+net\s+to\s+the\s+seller",
    re.I)

_MONTH = (r"January|February|March|April|May|June|July|August|September|October|"
          r"November|December")

# [\s\S] rather than [^.]: the sentence that carries the date almost always
# reads "will expire at 5:00 p.m., New York City time, on October 15, 2026",
# and a class excluding "." stops dead on the abbreviation. Bounded and lazy
# instead, so it takes the first date after the keyword and cannot wander into
# the next paragraph.
EXPIRATION_DATE = re.compile(
    rf"expir\w+[\s\S]{{0,140}}?\b({_MONTH})\s+(\d{{1,2}}),\s*(\d{{4}})"
    rf"|\bExpiration\s+(?:Date|Time)\b[\s\S]{{0,160}}?\b({_MONTH})\s+(\d{{1,2}}),\s*(\d{{4}})",
    re.I)

WITHDRAWAL_DATE = re.compile(
    rf"withdraw\w+[\s\S]{{0,160}}?\b({_MONTH})\s+(\d{{1,2}}),\s*(\d{{4}})", re.I)

# An extension amendment states two dates in one sentence — "previously
# scheduled to expire on October 1, has been extended and will now expire on
# October 16" — and the first one is dead. Which of the two is picked decides
# whether a live offer is dropped or a closed one is published as open.
SUPERSEDED_DATE = re.compile(
    r"\b(?:previously|originally|initially|heretofore|prior\s+to\s+(?:its|the)\s+extension)\b",
    re.I)
EXTENSION_MARKER = re.compile(
    r"\b(?:has\s+been|have\s+been|is\s+hereby|are\s+hereby|was|were)\s+extended\b"
    r"|\bwill\s+now\s+expire\b|\bas\s+(?:so\s+)?extended\b"
    r"|\bextend(?:ed|s)\s+the\s+(?:Offer|Expiration)\b", re.I)

MAX_SHARES_SOUGHT = re.compile(
    r"up\s+to\s+([\d,]{4,})\s+(?:of\s+its\s+|of\s+our\s+)?(?:issued\s+and\s+outstanding\s+)?"
    r"(?:shares|Shares|common\s+shares)", re.I)

# A negator in the same sentence, immediately before a condition. "The Offer is
# **not** conditioned on the receipt of financing" is a sentence every clean
# tender document contains, and reading it as a financing condition would cost
# the offer its Tier A on the strength of a promise that it has no such
# condition.
NEGATOR = re.compile(r"\b(?:not|no|without|free\s+of|absence\s+of)\b", re.I)

# Gate 3 — scored down and surfaced, never rejected on.
RISK_PATTERNS: dict[str, re.Pattern[str]] = {
    "financing_condition": re.compile(
        r"\bfinancing\s+condition\b|conditioned\s+(?:up)?on[^.]{0,120}?\b(?:obtaining|receipt\s+of)"
        r"[^.]{0,60}?\bfinancing\b|subject\s+to[^.]{0,80}?\bfinancing\b", re.I),
    "minimum_tender_condition": re.compile(
        r"\bminimum\s+(?:tender|condition)\b|conditioned\s+(?:up)?on[^.]{0,140}?"
        r"\bat\s+least\s+[\d,]+\s+shares\s+(?:being\s+)?(?:validly\s+)?tendered", re.I),
    "litigation_or_regulatory_condition": re.compile(
        r"\b(?:antitrust|HSR|Hart-Scott-Rodino|regulatory\s+approval|CFIUS)\b"
        r"|conditioned\s+(?:up)?on[^.]{0,120}?\b(?:approval|litigation|injunction)\b", re.I),
    "foreign_private_issuer": re.compile(
        r"\bforeign\s+private\s+issuer\b|\bwithholding\s+tax\b[^.]{0,80}?\bnon-?U\.?S\.?"
        r"|\bCanada\s+Revenue\s+Agency\b", re.I),
    "going_concern": re.compile(
        r"\bgoing\s+concern\b|substantial\s+doubt\s+about[^.]{0,60}?\bcontinue\s+as\s+a\s+going", re.I),
}


# --------------------------------------------------------------------------
# parsing an offer document
# --------------------------------------------------------------------------

# The cover pages carry the title, the subject security, and the price. Reading
# the whole document for those invites the capitalization table and the tax
# discussion into the answer.
COVER_CHARS = 8000


@dataclass
class OfferTerms:
    """Everything Gate 1 and Gate 2 need, extracted from one offer document."""

    odd_lot_paragraph: str | None = None
    has_threshold: bool = False
    has_proration_preference: bool = False
    is_cash_offer: bool = False
    is_common_equity: bool = False
    subject_security: str | None = None
    offer_price: float | None = None
    dutch_range: tuple[float, float] | None = None
    price_basis: str | None = None          # "fixed" | "dutch_low_end"
    expiration_date: str | None = None
    withdrawal_deadline: str | None = None
    withdrawal_basis: str | None = None     # "explicit" | "expiration_date"
    max_shares_sought: int | None = None
    preference_removed: bool = False
    record_holder_condition: int | None = None
    restricted_offer: bool = False
    terminated: bool = False
    risk_flags: list[str] = field(default_factory=list)


def terms_from_stored(stored: dict[str, Any], paragraph: str | None = None) -> OfferTerms:
    """Rebuild an OfferTerms from a universe entry written by an earlier run.

    Unknown keys are dropped rather than raising. The universe is committed to
    the repo and outlives any one version of this module, so a field renamed
    here must not turn every stored entry into a crash on the next run.
    """
    known = {f.name for f in fields(OfferTerms)}
    return OfferTerms(odd_lot_paragraph=paragraph,
                      **{k: v for k, v in stored.items()
                         if k in known and k != "odd_lot_paragraph"})


def find_odd_lot_passage(text: str) -> tuple[str | None, bool, bool]:
    """The paragraph carrying the odd-lot preference, and which halves it has.

    Both halves must land in the same passage. Requiring only the threshold
    would pass a document that merely defines an Odd Lot and then prorates
    everyone equally; requiring only the proration language would pass the
    ordinary "shares will be purchased on a pro rata basis" sentence that every
    oversubscribed tender offer contains.

    Adjacent paragraphs are tried as a pair because the summary term sheet often
    breaks the definition and the promise across a paragraph boundary, and a
    two-paragraph quote is still something a human can check in seconds.
    """
    blocks = paragraphs(text)
    best: tuple[str | None, bool, bool] = (None, False, False)

    for window in (1, 2):
        for i in range(len(blocks) - window + 1):
            passage = " ".join(blocks[i:i + window])
            probe = _normalize_for_match(passage)
            if not ODD_LOT_MARKER.search(probe) and not ODD_LOT_THRESHOLD.search(probe):
                continue
            threshold = bool(ODD_LOT_THRESHOLD.search(probe))
            preference = bool(PRORATION_PREFERENCE.search(probe))
            if threshold and preference:
                return passage, True, True
            # Remember the closest near-miss so a rejection can say which half
            # was missing rather than only that the document did not qualify.
            if (threshold or preference) and not any(best[1:]):
                best = (passage, threshold, preference)
            elif threshold and not best[1]:
                best = (passage, threshold, preference)
    return best


def _money(*groups: str | None) -> float | None:
    for g in groups:
        if g:
            return float(g.replace(",", ""))
    return None


def parse_prices(text: str) -> tuple[float | None, tuple[float, float] | None, str | None]:
    """(offer_price, dutch_range, basis).

    In a Dutch auction the issuer picks the final price and accepts every share
    tendered *at or below* it, so the low end is the only number a tender is
    guaranteed to clear at. Taking the midpoint would price the trade off a
    figure the seller never promised.
    """
    probe = _normalize_for_match(text)
    dutch = DUTCH_RANGE.search(probe)
    if dutch:
        values = [float(g.replace(",", "")) for g in dutch.groups() if g]
        if len(values) >= 2:
            low, high = min(values), max(values)
            return low, (low, high), "dutch_low_end"

    fixed = FIXED_PRICE.search(probe)
    if fixed:
        return _money(*fixed.groups()), None, "fixed"
    return None, None, None


def _parse_us_date(month: str, day: str, year: str) -> str | None:
    try:
        return datetime.strptime(f"{month} {day} {year}", "%B %d %Y").date().isoformat()
    except ValueError:
        return None


def _expiration_candidates(probe: str) -> list[tuple[str, bool]]:
    """Every readable expiration date, paired with "this one is an extension"."""
    found = []
    for match in EXPIRATION_DATE.finditer(probe):
        groups = [g for g in match.groups() if g]
        if len(groups) < 3:
            continue
        iso = _parse_us_date(groups[0], groups[1], groups[2])
        if not iso:
            continue
        context = probe[max(0, match.start() - 140):match.end()]
        if SUPERSEDED_DATE.search(probe[max(0, match.start() - 100):match.start()]):
            continue
        found.append((iso, bool(EXTENSION_MARKER.search(context))))
    return found


def parse_dates(text: str) -> tuple[str | None, str | None, str]:
    """(expiration, withdrawal_deadline, withdrawal_basis).

    When a document states more than one expiration, an **extension** wins and
    otherwise the **earliest** does. The asymmetry is deliberate: reading an
    expiry earlier than the truth drops a live offer, which costs a missed
    trade, while reading one later than the truth publishes a closed offer as
    open, which costs money. Only an explicit extension is allowed to push the
    date out.

    Withdrawal rights normally run to the expiration date and the document says
    so in prose rather than with a second date. When no explicit date is found
    the expiration is used, and the basis records that it was inferred — the
    report prints the distinction rather than presenting a guess as a fact.
    """
    probe = _normalize_for_match(text)
    candidates = _expiration_candidates(probe)
    extended = [iso for iso, is_extension in candidates if is_extension]
    if extended:
        expiration = max(extended)
    elif candidates:
        expiration = min(iso for iso, _ in candidates)
    else:
        expiration = None

    withdrawal, basis = None, "expiration_date"
    wmatch = WITHDRAWAL_DATE.search(probe)
    if wmatch:
        groups = [g for g in wmatch.groups() if g]
        if len(groups) >= 3:
            candidate = _parse_us_date(groups[0], groups[1], groups[2])
            if candidate and candidate != expiration:
                withdrawal, basis = candidate, "explicit"
    return expiration, (withdrawal or expiration), basis


def classify_subject_security(cover: str) -> tuple[bool, str | None]:
    """Whether the security being tendered for is common equity, and what it is.

    Decided by whichever marker appears **first** in the cover pages. A common
    stock tender by a company with preferred outstanding will mention preferred
    somewhere; it will not mention it in the title.
    """
    probe = _normalize_for_match(cover)
    common = COMMON_EQUITY_SUBJECT.search(probe)
    other = DEBT_OR_PREFERRED_SUBJECT.search(probe)
    if common and (not other or common.start() < other.start()):
        return True, common.group(0)
    if other:
        return False, other.group(0)
    return False, None


def _negated(probe: str, start: int, lookback: int = 70) -> bool:
    """Is there a negator between the start of this sentence and `start`?

    Scoped to the sentence: the window is cut at the last period before the
    match, so "...prior to the Expiration Date. The Offer is conditioned upon"
    does not inherit a "not" from the sentence before it.
    """
    window = probe[max(0, start - lookback):start]
    window = window[window.rfind(".") + 1:]
    return bool(NEGATOR.search(window))


def detect_risk_flags(probe: str) -> list[str]:
    """Gate 3 flags present in the document, negated mentions excluded."""
    found = []
    for name, pattern in RISK_PATTERNS.items():
        for match in pattern.finditer(probe):
            if not _negated(probe, match.start()):
                found.append(name)
                break
    return sorted(found)


def parse_offer_document(raw: str, *, is_amendment: bool | None = None) -> OfferTerms:
    """Everything the gates need from one offer-to-purchase document.

    `is_amendment` overrides the reading; left as None it is read from the
    document, which is the only source that cannot be wrong about it.
    """
    text = html_to_text(raw)
    probe = _normalize_for_match(text)
    cover = text[:COVER_CHARS]

    passage, threshold, preference = find_odd_lot_passage(text)
    price, dutch, basis = parse_prices(text)
    expiration, withdrawal, wbasis = parse_dates(text)
    is_common, subject = classify_subject_security(cover)

    amendment = (bool(AMENDMENT_MARKER.search(_normalize_for_match(cover)))
                 if is_amendment is None else is_amendment)

    cash_hits = len(CASH_OFFER.findall(_normalize_for_match(cover)))
    exchange_hits = len(EXCHANGE_OFFER.findall(_normalize_for_match(cover)))

    # The record-holder condition only voids the preference when it is attached
    # to it. Read inside the odd-lot passage, not the whole document.
    record_floor = None
    if passage:
        cond = RECORD_HOLDER_CONDITION.search(_normalize_for_match(passage))
        if cond:
            record_floor = int(next(g for g in cond.groups() if g))

    shares_match = MAX_SHARES_SOUGHT.search(probe)
    max_shares = None
    if shares_match:
        digits = shares_match.group(1).replace(",", "")
        max_shares = int(digits) if digits.isdigit() else None

    return OfferTerms(
        odd_lot_paragraph=passage,
        has_threshold=threshold,
        has_proration_preference=preference,
        is_cash_offer=cash_hits > 0 and cash_hits >= exchange_hits,
        is_common_equity=is_common,
        subject_security=subject,
        offer_price=price,
        dutch_range=dutch,
        price_basis=basis,
        expiration_date=expiration,
        withdrawal_deadline=withdrawal,
        withdrawal_basis=wbasis,
        max_shares_sought=max_shares,
        preference_removed=bool(amendment and PREFERENCE_REMOVED.search(probe)),
        record_holder_condition=record_floor,
        restricted_offer=bool(RESTRICTED_OFFER.search(probe)),
        terminated=bool(TERMINATED.search(probe)),
        risk_flags=detect_risk_flags(probe),
    )


# --------------------------------------------------------------------------
# gates
# --------------------------------------------------------------------------

@dataclass
class GateResult:
    """A pass/reject decision plus every reason it could be argued with.

    `rejections` is the deliverable of a rejecting gate. A screener that only
    emits what survived cannot be tuned — you never learn that the threshold
    you set is throwing away the whole universe.
    """

    passed: bool
    rejections: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def reject(self, reason: str) -> "GateResult":
        self.passed = False
        self.rejections.append(reason)
        return self


def gate_document(terms: OfferTerms, *, form: str, today: date) -> GateResult:
    """GATE 1 — is this actually a live, cash, common-equity odd-lot offer?

    Any failure rejects. The gate is deliberately unforgiving: everything it
    checks is a fact stated in the document, so a document that does not state
    it plainly is a document we have not understood, and an odd-lot trade
    entered on a misunderstanding has no edge left in it to absorb the error.
    """
    result = GateResult(passed=True)

    if not terms.has_threshold:
        result.reject("no 'fewer than 100 shares' odd-lot threshold in the document")
    if not terms.has_proration_preference:
        result.reject("odd lots mentioned but no acceptance-before-proration language")

    if terms.preference_removed:
        result.reject("amendment removes the odd-lot preference (Frontera pattern)")
    if terms.record_holder_condition is not None:
        result.reject(
            f"odd-lot preference conditioned on keeping at least "
            f"{terms.record_holder_condition} holders of record (ITEX pattern)")
    if terms.restricted_offer:
        result.reject("offer restricted to accredited investors, QIBs, or non-US persons")

    if not terms.is_cash_offer:
        result.reject("not a cash offer — reads as an exchange offer for other securities")
    if not terms.is_common_equity:
        subject = terms.subject_security or "unidentified security"
        result.reject(f"subject security is not common equity ({subject})")

    if terms.terminated:
        result.reject("the offer has been terminated or withdrawn")
    if terms.expiration_date is None:
        result.reject("no expiration date could be read from the document")
    elif date.fromisoformat(terms.expiration_date) < today:
        result.reject(f"offer expired {terms.expiration_date}")

    if form.upper().endswith("/A") and not terms.preference_removed:
        result.warnings.append(
            "amendment — terms below are this amendment's, read it against the original")
    return result


def economics(offer_price: float, market_price: float, expiration: str, *,
              today: date, shares: int = 99) -> dict[str, Any]:
    """The arithmetic, and only the arithmetic. No opinion, no thresholds."""
    spread_pct = (offer_price - market_price) / market_price
    days = (date.fromisoformat(expiration) - today).days
    return {
        "market_price": round(market_price, 4),
        "offer_price": round(offer_price, 4),
        "spread_pct": round(spread_pct, 6),
        "capital": round(shares * market_price, 2),
        "days_to_expiry": days,
        # Annualising a sub-4-day holding period produces a number in the
        # hundreds of percent. It is a comparison aid between offers, not a
        # return anyone collects — Gate 2's day floor is what keeps it sane.
        "annualized": round(spread_pct * (365 / days), 6) if days > 0 else None,
        "gross_profit": round(shares * (offer_price - market_price), 2),
    }


def gate_economics(econ: dict[str, Any], avg_volume: float | None,
                   config: dict[str, Any]) -> GateResult:
    """GATE 2 — is the spread worth the capital, the wait, and the exit risk?"""
    cfg = config["economics"]
    result = GateResult(passed=True)

    if econ["spread_pct"] < cfg["min_spread_pct"]:
        result.reject(
            f"spread {econ['spread_pct'] * 100:.2f}% below the "
            f"{cfg['min_spread_pct'] * 100:.1f}% floor")
    if econ["capital"] > cfg["max_capital"]:
        result.reject(
            f"99 shares costs ${econ['capital']:,.0f}, over the "
            f"${cfg['max_capital']:,.0f} cap")
    if econ["days_to_expiry"] < cfg["min_days_to_expiry"]:
        result.reject(
            f"{econ['days_to_expiry']} days to expiry, under the "
            f"{cfg['min_days_to_expiry']}-day floor (broker cutoffs precede the "
            f"offer deadline)")
    if econ["market_price"] < cfg["min_market_price"]:
        result.reject(
            f"${econ['market_price']:.2f} is below the ${cfg['min_market_price']:.2f} "
            f"sub-dollar floor")
    if avg_volume is None:
        result.reject("no 30-day volume available — exit liquidity unknown")
    elif avg_volume < cfg["min_avg_volume_30d"]:
        result.reject(
            f"30-day average volume {avg_volume:,.0f} under the "
            f"{cfg['min_avg_volume_30d']:,.0f}-share exit-liquidity floor")
    return result


def gate_risk(terms: OfferTerms, econ: dict[str, Any]) -> list[str]:
    """GATE 3 — flags. Never rejects; they cost the offer its tier instead.

    "Market price above offer price" earns its place at the top of the list.
    It means the market disagrees with the offer — expecting a raised bid, or
    pricing in a fight — and the arithmetic spread it produces is negative, so
    it is the one flag that is also a statement about the trade itself.
    """
    flags = list(terms.risk_flags)
    if econ["market_price"] > econ["offer_price"]:
        flags.insert(0, "market_price_above_offer")
    return flags


def tier_for(econ: dict[str, Any], flags: list[str], config: dict[str, Any]) -> str:
    """GATE 4 — A, B, or C.

    Tier A is the clean case: a wide spread, room on the calendar, and nothing
    flagged. Tier C is what the flags decide — a material flag, or more than
    one flag of any kind. Tier B is everything else that cleared the gates: a
    thinner spread, a tighter timeline, or a single minor flag, in any
    combination.

    The spread is a **qualifier for B, not a discriminator within it**. Any
    spread at or above the Gate 2 floor is a Tier B spread; a 1.8% spread is
    not evidence against an offer, it is just a smaller version of the same
    trade. What separates B from C is whether something is wrong with the
    offer, and that is what the flags are for.

    Two flags are never minor. `market_price_above_offer` means the market
    disagrees with the offer outright, and `going_concern` means the
    counterparty for your $1,000 may not be there to settle it. Either one
    sends the offer to C on its own.
    """
    tiers = config["tiers"]
    a, b = tiers["tier_a"], tiers["tier_b"]
    material = set(tiers.get("material_flags", []))

    # Asked first: a material flag beats a wide spread and a long calendar.
    if (material & set(flags)) or len(flags) > b["max_risk_flags"]:
        return "C"
    if (econ["spread_pct"] >= a["min_spread_pct"]
            and econ["days_to_expiry"] >= a["min_days_to_expiry"]
            and len(flags) <= a["max_risk_flags"]):
        return "A"
    # Normally unreachable — Gate 2 rejects anything under its own floor — but
    # the two floors are separate config entries and can be set apart.
    return "B" if econ["spread_pct"] >= b["min_spread_pct"] else "C"


# Which gate is doing the rejecting. A screener that finds nothing looks
# identical to one that is broken, and the difference is entirely in where the
# universe is being lost — the first live run rejected everything at Gate 1 and
# read as a quiet day. Keyed by the leading words of each rejection so the
# tally follows the messages rather than a parallel list of codes that drifts.
REJECTION_KINDS = {
    "no odd-lot language": ("no 'fewer than 100", "odd lots mentioned but no"),
    "no readable document": ("the filing carried no readable",),
    "preference removed or conditioned": ("amendment removes", "conditioned on keeping"),
    "not a cash common-equity offer": ("not a cash offer", "not common equity",
                                       "restricted to accredited"),
    "expired or terminated": ("offer expired", "terminated or withdrawn",
                              "no expiration date"),
    "no ticker": ("no ticker for CIK",),
    "no price": ("no live price", "no offer price"),
    "spread too thin": ("spread ",),
    "capital over the cap": ("99 shares costs",),
    "too close to expiry": ("days to expiry",),
    "illiquid": ("exit-liquidity floor", "exit liquidity unknown"),
    "sub-dollar": ("sub-dollar floor",),
    "SEC blocked the fetch": ("SEC blocked",),
    "fetch failed": ("could not fetch",),
}


def rejection_tally(universe: dict[str, Any]) -> dict[str, Any]:
    """How many offers each gate turned away, and the leftovers it could not
    classify — an unclassified rejection means a message changed and this
    tally quietly stopped describing the funnel."""
    counts: dict[str, int] = {}
    unclassified = 0
    for entry in universe["open"]:
        for reason in entry.get("rejections") or []:
            for label, prefixes in REJECTION_KINDS.items():
                if any(p in reason for p in prefixes):
                    counts[label] = counts.get(label, 0) + 1
                    break
            else:
                unclassified += 1
    return {"rejected_by": dict(sorted(counts.items(), key=lambda kv: -kv[1])),
            "unclassified_rejections": unclassified}


# --------------------------------------------------------------------------
# the universe
# --------------------------------------------------------------------------
#
# Committed to the repo so the history survives the runner. Two halves:
# `open` is every offer still worth re-scoring each day, `archive` is what
# happened to the ones that closed. Discovery appends; re-scoring rewrites the
# economics on all of them, because prices move and an offer rejected on
# Tuesday's spread can clear the floor on Thursday's.

EMPTY_UNIVERSE = {"updated_at": None, "last_run_at": None, "open": [], "archive": []}


def load_universe(path: Path | None = None) -> dict[str, Any]:
    path = path or UNIVERSE_PATH
    if not path.exists():
        return json.loads(json.dumps(EMPTY_UNIVERSE))
    data = json.loads(path.read_text())
    for key in ("open", "archive"):
        data.setdefault(key, [])
    return data


def save_universe(universe: dict[str, Any], path: Path | None = None) -> None:
    path = path or UNIVERSE_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    universe["updated_at"] = datetime.now(ET).isoformat(timespec="seconds")
    path.write_text(json.dumps(universe, indent=2, sort_keys=False) + "\n")


def add_discoveries(universe: dict[str, Any], hits: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Append hits not already known, by accession number. Returns the new ones.

    Accession is the right key: an amendment carries its own, so an `SC TO-I/A`
    that changes the terms enters as its own entry rather than silently
    overwriting the original offer's reading.
    """
    known = {e["accession"] for e in universe["open"]} | {e["accession"] for e in universe["archive"]}
    added = []
    for hit in hits:
        if hit["accession"] in known:
            continue
        entry = dict(hit)
        entry.update({
            "first_seen": datetime.now(ET).date().isoformat(),
            "status": "new",
            "tier": None,
            "rejections": [],
            "risk_flags": [],
        })
        universe["open"].append(entry)
        known.add(hit["accession"])
        added.append(entry)
    return added


def archive_expired(universe: dict[str, Any], today: date,
                    stale_after_days: int | None = None) -> list[dict[str, Any]]:
    """Move finished offers out of `open`, with the outcome kept.

    An entry whose expiration never parsed is **not** treated as expired:
    "we could not read the date" is not "it has closed", and quietly archiving
    the first as the second would hide a parser failure behind a plausible
    outcome. It is retired only once it is old enough that no tender offer
    could still be open, and the outcome says which of the two happened —
    otherwise the universe grows without bound on exactly the entries the
    parser handles worst.
    """
    still_open, moved = [], []
    for entry in universe["open"]:
        expiry = entry.get("expiration_date")
        age = _days_since(entry.get("first_seen"), today)

        if expiry and date.fromisoformat(expiry) < today:
            entry["outcome"] = (
                f"expired {expiry} as tier {entry['tier']}"
                if entry.get("tier") else f"expired {expiry}, never cleared the gates")
        elif (not expiry and stale_after_days is not None
              and age is not None and age >= stale_after_days):
            entry["outcome"] = (
                f"aged out after {age} days — no expiration date could ever be read "
                f"from the document")
        else:
            still_open.append(entry)
            continue

        entry["status"] = "expired"
        entry["archived_on"] = today.isoformat()
        moved.append(entry)
        universe["archive"].append(entry)

    universe["open"] = still_open
    return moved


def _days_since(stamp: str | None, today: date) -> int | None:
    try:
        return (today - date.fromisoformat(str(stamp))).days
    except (TypeError, ValueError):
        return None


# --------------------------------------------------------------------------
# scoring one entry
# --------------------------------------------------------------------------

def _market_data():
    """Imported lazily: this module's logic must load without the HTTP stack."""
    import market_data

    return market_data


def fetch_quote(symbol: str, md: Any) -> tuple[float | None, str | None, str | None]:
    """(price, asof, source) from whatever quote source answers first."""
    try:
        q = md.quote(symbol)
    except Exception as exc:  # noqa: BLE001 - a dead quote source is not a crash
        return None, None, f"{type(exc).__name__}: {exc}"
    if not q.get("ok"):
        return None, None, "no quote source answered"
    return q.get("price"), q.get("asof"), q.get("source")


def fetch_liquidity(symbol: str, md: Any) -> float | None:
    """30-day average share volume, or None when no source could supply it."""
    try:
        hist = md.history(symbol, days=45)
    except Exception:  # noqa: BLE001
        return None
    return hist.get("avg_volume_30d") if hist.get("ok") else None


def terms_completeness(terms: OfferTerms) -> tuple[int, int, int, int]:
    """How usable a reading of one document is, for picking between exhibits.

    Ordered so that the preference language dominates: a document that states
    the odd-lot terms is the Offer to Purchase, and a document that merely
    mentions odd lots is the Letter of Transmittal standing next to it. Price
    and expiry break ties between two documents that both carry the language.
    """
    return (
        int(terms.has_threshold and terms.has_proration_preference),
        int(terms.offer_price is not None),
        int(terms.expiration_date is not None),
        int(terms.odd_lot_paragraph is not None),
    )


def candidate_documents(entry: dict[str, Any]) -> list[dict[str, Any]]:
    """Every exhibit worth reading for this filing, best guess first.

    The order is only a cost optimisation — every document is read either way
    until one carries the full odd-lot terms. Guessing from the exhibit label
    alone is not safe: issuers letter their exhibits inconsistently, and the
    (a)(1) block that usually holds the Offer to Purchase sometimes holds the
    transmittal letter instead.
    """
    documents = entry.get("documents")
    if not documents:
        # An entry stored before filings carried a document list.
        return ([{"name": entry.get("document") or "", "type": "",
                  "url": entry.get("url") or ""}] if entry.get("url") else [])

    def rank(doc: dict[str, Any]) -> tuple[int, str]:
        label = f"{doc.get('type', '')} {doc.get('name', '')}".lower()
        if "transmittal" in label or "guaranteed" in label:
            return (2, label)          # never the offer document
        if "offer" in label or "(a)(1)(i)" in label or "otp" in label:
            return (0, label)          # usually is
        return (1, label)

    return sorted(documents, key=rank)


def read_offer_documents(entry: dict[str, Any], client: SecClient,
                         ) -> tuple[OfferTerms | None, dict[str, Any] | None, list[str]]:
    """Read the filing's exhibits, return the best reading and which gave it.

    Stops early on a document carrying the complete terms. Anything less keeps
    looking, because a filing is only as good as its best exhibit and the first
    one back is frequently the wrong one.
    """
    best: tuple[tuple[int, ...], OfferTerms, dict[str, Any]] | None = None
    read: list[str] = []

    for doc in candidate_documents(entry):
        if not doc.get("url"):
            continue
        raw = client.get(doc["url"], cache_key=f"{entry['accession']}_{doc['name']}")
        read.append(doc["name"])
        terms = parse_offer_document(raw)
        score = terms_completeness(terms)
        if best is None or score > best[0]:
            best = (score, terms, doc)
        if score[0] and score[1] and score[2]:
            break

    if best is None:
        return None, None, read
    return best[1], best[2], read


def score_entry(entry: dict[str, Any], *, client: SecClient | None, md: Any,
                config: dict[str, Any], today: date) -> dict[str, Any]:
    """Run one universe entry through all four gates and write the result back.

    Every field this sets is recomputed from the document and a live quote on
    every run. Nothing is carried forward from yesterday's reading except the
    identifiers — a stale spread is worse than no spread, because it looks
    exactly like a fresh one.
    """
    entry["last_scored"] = today.isoformat()
    entry["rejections"] = []
    entry["warnings"] = []
    entry["risk_flags"] = []
    entry["tier"] = None

    # --- Gate 1: the document -------------------------------------------
    if client is not None:
        try:
            terms, document, read = read_offer_documents(entry, client)
        except SecBlocked as exc:
            entry["status"] = "deferred"
            entry["rejections"] = [f"SEC blocked the fetch: {exc}"]
            return entry
        except Exception as exc:  # noqa: BLE001
            entry["status"] = "rejected"
            entry["rejections"] = [f"could not fetch the offer document: "
                                   f"{type(exc).__name__}: {exc}"]
            return entry
        entry["documents_read"] = read
        if terms is None:
            entry["status"] = "rejected"
            entry["rejections"] = ["the filing carried no readable document"]
            return entry
        # Which exhibit actually supplied the terms, so a rejection can be
        # checked against the document it was read from.
        entry["document"] = (document or {}).get("name") or entry.get("document")
        entry["url"] = (document or {}).get("url") or entry.get("url")
        entry["terms"] = {k: v for k, v in asdict(terms).items() if k != "odd_lot_paragraph"}
        entry["odd_lot_paragraph"] = terms.odd_lot_paragraph
        entry["offer_price"] = terms.offer_price
        entry["dutch_range"] = list(terms.dutch_range) if terms.dutch_range else None
        entry["price_basis"] = terms.price_basis
        entry["expiration_date"] = terms.expiration_date
        entry["withdrawal_deadline"] = terms.withdrawal_deadline
        entry["withdrawal_basis"] = terms.withdrawal_basis
        entry["max_shares_sought"] = terms.max_shares_sought
    else:
        # Re-scoring without a client re-uses the stored reading of the
        # document, which is immutable — an amendment arrives as a new filing
        # with its own accession, never as an edit to this one.
        stored = entry.get("terms")
        if not stored:
            entry["status"] = "rejected"
            entry["rejections"] = ["no stored reading of the document, and EDGAR was "
                                   "not consulted"]
            return entry
        terms = terms_from_stored(stored, entry.get("odd_lot_paragraph"))

    gate1 = gate_document(terms, form=entry["form"], today=today)
    entry["warnings"] = gate1.warnings
    if not gate1.passed:
        entry["status"] = "rejected"
        entry["rejections"] = gate1.rejections
        return entry

    # --- Gate 2: the economics ------------------------------------------
    symbol = entry.get("ticker") or ""
    if not symbol and client is not None:
        # EFTS only names a ticker when the *filer* has one on file, and a
        # tender offer is often filed by a parent or an acquirer that does not.
        symbol = ticker_for_cik(entry["cik"], client)
        if symbol:
            entry["ticker"] = symbol
            entry["ticker_source"] = "sec_company_tickers"
    if not symbol:
        entry["status"] = "rejected"
        entry["rejections"] = [
            f"no ticker for CIK {entry.get('cik')} in the filing or the SEC "
            f"company list — cannot price the trade"]
        return entry

    price, asof, source = fetch_quote(symbol, md)
    entry["market_price"] = price
    entry["price_asof"] = asof
    entry["price_source"] = source
    if price is None:
        entry["status"] = "rejected"
        entry["rejections"] = [f"no live price for {symbol} ({source})"]
        return entry
    if terms.offer_price is None:
        entry["status"] = "rejected"
        entry["rejections"] = ["no offer price could be read from the document"]
        return entry

    econ = economics(terms.offer_price, price, terms.expiration_date,
                     today=today, shares=config["economics"]["shares_tendered"])
    entry.update(econ)

    volume = fetch_liquidity(symbol, md)
    entry["avg_volume_30d"] = volume

    flags = gate_risk(terms, econ)
    entry["risk_flags"] = flags

    gate2 = gate_economics(econ, volume, config)
    if not gate2.passed:
        entry["status"] = "rejected"
        entry["rejections"] = gate2.rejections
        return entry

    entry["status"] = "candidate"
    entry["tier"] = tier_for(econ, flags, config)
    return entry


# --------------------------------------------------------------------------
# who to tell, and when
# --------------------------------------------------------------------------
#
# The whole point of the screener is that most days it finds nothing, which
# means nobody will read a report that says so. A Tier A or B offer has a
# deadline attached and is the one day the tab is worth opening — so it has to
# come and find you.
#
# Everything here is a pure decision over the universe. It knows nothing about
# GitHub, email, or any other channel; `scripts/notify_odd_lot.py` carries it.

TIER_RANK = {"A": 3, "B": 2, "C": 1}


def _tier_at_least(tier: str | None, floor: str) -> bool:
    return TIER_RANK.get(tier or "", 0) >= TIER_RANK.get(floor, 99)


def notifications_due(universe: dict[str, Any], config: dict[str, Any]) -> list[dict[str, Any]]:
    """Qualifying offers nobody has been told about yet.

    Deduplicated on `(accession, tier)`, which is the rule that makes this
    liveable. The screener re-scores the whole universe twice a day, so keying
    on the accession alone would be two emails a day for as long as an offer
    stays open — and an alert that arrives every day is one you stop reading,
    which costs more than the alert was ever worth.

    A tier that *improves* re-notifies, because "the B I mentioned is now an A"
    is news. A tier that decays does not: you already know about the offer, and
    the tab and the report carry the current state.
    """
    floor = config["notify"]["min_tier"]
    due = []
    for entry in universe["open"]:
        if entry.get("status") != "candidate" or not _tier_at_least(entry.get("tier"), floor):
            continue
        told = entry.get("notified") or {}
        if TIER_RANK.get(entry["tier"], 0) > TIER_RANK.get(told.get("tier", ""), 0):
            due.append(entry)
    return due


def record_notified(entry: dict[str, Any], *, issue: int | None = None,
                    now: datetime | None = None) -> dict[str, Any]:
    """Mark an entry as announced at its current tier."""
    entry["notified"] = {
        "tier": entry.get("tier"),
        "at": (now or datetime.now(ET)).isoformat(timespec="seconds"),
        "issue": issue,
    }
    return entry


def notifications_to_close(universe: dict[str, Any], config: dict[str, Any]) -> list[dict[str, Any]]:
    """Announced offers that have since expired or stopped qualifying.

    Closing is the quiet half of the lifecycle: it takes the offer off the open
    list without sending anything, so the record of what was announced stays
    honest without a second alert saying an opportunity went away.
    """
    if not config["notify"].get("close_when_gone", True):
        return []
    floor = config["notify"]["min_tier"]
    gone = []
    for entry in universe["archive"]:
        told = entry.get("notified") or {}
        if told.get("issue") and not told.get("closed"):
            gone.append(entry)
    for entry in universe["open"]:
        told = entry.get("notified") or {}
        if not told.get("issue") or told.get("closed"):
            continue
        if entry.get("status") != "candidate" or not _tier_at_least(entry.get("tier"), floor):
            gone.append(entry)
    return gone


# --------------------------------------------------------------------------
# the report
# --------------------------------------------------------------------------

TIER_HEADINGS = {
    "A": "Tier A — spread ≥3%, ≥7 days, no flags",
    "B": "Tier B — spread ≥1.5%, with a tighter timeline or one minor flag",
    "C": "Tier C — a material flag, or more than one (informational only)",
}

DISCLAIMER = (
    "Automated research, not investment advice. Odd-lot preferences are a term of "
    "each offer and can be amended or removed by the issuer at any time. Verify the "
    "quoted paragraph in the linked filing before tendering anything."
)


def _pct(value: float | None) -> str:
    return "—" if value is None else f"{value * 100:+.2f}%"


def _flag_list(flags: list[str]) -> str:
    return ", ".join(f.replace("_", " ") for f in flags) if flags else "none"


def _usd(value: Any) -> str:
    return "—" if value is None else f"${value:,.2f}"


def _count(value: Any) -> str:
    return "—" if value is None else f"{value:,}"


def render_entry(entry: dict[str, Any]) -> list[str]:
    """One opportunity, with everything needed to check it by hand in seconds."""
    ticker = entry.get("ticker") or "?"

    if entry.get("dutch_range"):
        low, high = entry["dutch_range"]
        price_line = (f"{_usd(entry.get('offer_price'))} "
                      f"(Dutch range {_usd(low)}–{_usd(high)}, low end used)")
    else:
        price_line = _usd(entry.get("offer_price"))

    withdrawal = entry.get("withdrawal_deadline") or "—"
    if withdrawal != "—" and entry.get("withdrawal_basis") == "expiration_date":
        withdrawal += " (no separate date stated; withdrawal runs to expiration)"

    document = entry.get("document") or "filing index"
    rows = [
        ("Form", f"{entry.get('form', '')} filed {entry.get('filed', '')}"),
        ("Offer document", f"[{document}]({entry.get('url', '')})"),
        ("Filing index", f"[{entry['accession']}]({entry.get('index_url', '')})"),
        ("Offer price", price_line),
        ("Current price", f"{_usd(entry.get('market_price'))} "
                          f"({entry.get('price_source') or 'no source'}, "
                          f"as of {entry.get('price_asof') or '—'})"),
        ("Spread", _pct(entry.get("spread_pct"))),
        ("Annualized", _pct(entry.get("annualized"))),
        ("Capital for 99 shares", _usd(entry.get("capital"))),
        ("Gross profit on 99 shares", _usd(entry.get("gross_profit"))),
        ("Expiration", f"{entry.get('expiration_date') or '—'} "
                       f"({entry.get('days_to_expiry', '—')} days)"),
        ("Withdrawal deadline", withdrawal),
        ("30-day avg volume", _count(entry.get("avg_volume_30d"))),
        ("Max shares sought", _count(entry.get("max_shares_sought"))),
        ("Risk flags", _flag_list(entry.get("risk_flags") or [])),
    ]

    lines = [f"### {ticker} — {entry.get('company', '')}", "",
             "| | |", "| --- | --- |"]
    lines += [f"| {label} | {value} |" for label, value in rows]
    lines.append("")

    for warning in entry.get("warnings") or []:
        lines += [f"> ⚠ {warning}", ""]

    # The quoted paragraph is the point of the whole report: it is what lets a
    # human confirm the preference exists, and on what terms, without reading
    # a 90-page offer to purchase.
    if entry.get("odd_lot_paragraph"):
        lines += ["**Odd-lot language, quoted from the filing:**", "",
                  "> " + " ".join(entry["odd_lot_paragraph"].split()), ""]
    return lines


def render_report(universe: dict[str, Any], report_date: date,
                  config: dict[str, Any], *, slot: str = "") -> str:
    """The dated markdown report. Zero Tier A results is the normal outcome."""
    live = [e for e in universe["open"] if e.get("status") == "candidate"]
    rejected = [e for e in universe["open"] if e.get("status") == "rejected"]
    deferred = [e for e in universe["open"] if e.get("status") == "deferred"]
    by_tier = {t: [e for e in live if e.get("tier") == t] for t in ("A", "B", "C")}
    econ = config["economics"]

    stamp = datetime.now(ET).strftime("%Y-%m-%d %H:%M ET")
    out = [
        f"# Odd-lot tender screener — {report_date.isoformat()}",
        "",
        f"Run {stamp}{f' ({slot} slot)' if slot else ''}. "
        f"{len(universe['open'])} offers tracked, {len(live)} clear every gate: "
        f"{len(by_tier['A'])} Tier A, {len(by_tier['B'])} Tier B, {len(by_tier['C'])} Tier C.",
        "",
    ]

    if not by_tier["A"]:
        out += [
            "**No Tier A opportunities today.** That is the ordinary result — an "
            "odd-lot tender with a 3%+ spread and a clean condition set is rare, and "
            "the thresholds below are not moved to produce one.",
            "",
        ]

    for tier in ("A", "B", "C"):
        entries = sorted(by_tier[tier], key=lambda e: -(e.get("spread_pct") or 0))
        out += [f"## {TIER_HEADINGS[tier]}", ""]
        if not entries:
            out += ["_None._", ""]
            continue
        for entry in entries:
            out += render_entry(entry)

    out += ["## Rejected", ""]
    if not rejected:
        out += ["_Nothing was rejected this run._", ""]
    else:
        out += ["| Ticker | Form | Filed | Reason |", "| --- | --- | --- | --- |"]
        for entry in sorted(rejected, key=lambda e: e.get("filed", ""), reverse=True):
            reason = "; ".join(entry.get("rejections") or ["unstated"])
            out.append(f"| {entry.get('ticker') or '—'} | {entry.get('form', '')} "
                       f"| {entry.get('filed', '')} | {reason} |")
        out.append("")

    if deferred:
        out += ["## Deferred — not read this run", "",
                "| Ticker | Accession | Why |", "| --- | --- | --- |"]
        for entry in deferred:
            out.append(f"| {entry.get('ticker') or '—'} | {entry['accession']} "
                       f"| {'; '.join(entry.get('rejections') or [])} |")
        out.append("")

    newly_archived = [e for e in universe["archive"]
                      if e.get("archived_on") == report_date.isoformat()]
    if newly_archived:
        out += ["## Expired today", ""]
        for entry in newly_archived:
            out.append(f"- {entry.get('ticker') or '—'} {entry.get('company', '')} — "
                       f"{entry.get('outcome', '')}")
        out.append("")

    funnel = universe.get("funnel") or {}
    if funnel:
        out += [
            "## Where the universe went",
            "",
            "A screener that finds nothing reads exactly like one that is broken. "
            "This is the difference.",
            "",
            f"- **{funnel.get('queries', 0)}** full-text queries over "
            f"`{funnel.get('window', '?')}` returned **{funnel.get('raw_hits', 0)}** "
            f"document hit(s) across **{funnel.get('filings', 0)}** filing(s) "
            f"(**{funnel.get('documents', 0)}** exhibits kept as candidates)",
            f"- **{len(universe['open'])}** offers open, "
            f"**{len(universe['archive'])}** archived",
            "",
        ]
        rejected_by = funnel.get("rejected_by") or {}
        if rejected_by:
            out += ["| Turned away for | Count |", "| --- | --- |"]
            out += [f"| {label} | {count} |" for label, count in rejected_by.items()]
            out.append("")
        if funnel.get("unclassified_rejections"):
            out += [f"> ⚠ {funnel['unclassified_rejections']} rejection(s) did not "
                    f"match any known reason — `REJECTION_KINDS` has drifted from "
                    f"the gates.", ""]

    out += [
        "## Thresholds in force",
        "",
        f"- Minimum spread **{econ['min_spread_pct'] * 100:.1f}%**, "
        f"maximum capital **${econ['max_capital']:,}** for "
        f"{econ['shares_tendered']} shares",
        f"- Minimum **{econ['min_days_to_expiry']} days** to expiry, minimum "
        f"**{econ['min_avg_volume_30d']:,}** shares 30-day average volume",
        f"- Hard price floor **${econ['min_market_price']:.2f}** per share",
        "",
        "Every threshold and its rationale is in the README's odd-lot section. "
        "Changing one to produce content is how a screener stops being one.",
        "",
        "---",
        "",
        f"_{DISCLAIMER}_",
        "",
    ]
    return "\n".join(out)


# --------------------------------------------------------------------------
# which slot is this?
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class SlotDecision:
    proceed: bool
    slot: str
    date: str
    reason: str


def _window(raw: str) -> tuple[int, int]:
    start, _, end = raw.partition("-")
    return int(start), int(end)


def slot_for(now_et: datetime, config: dict[str, Any], *, event_name: str = "schedule",
             last_run_at: str | None = None, force: bool = False) -> SlotDecision:
    """Which of the two daily slots this invocation is, if either.

    Both slots are declared as two UTC crons apiece because GitHub cron has no
    DST awareness, so on any given day one arm of each pair lands an hour off.
    The window cannot separate the arms — that is the mistake the daily report
    made for two weeks — so it does not try. The window only asks whether this
    is roughly the right part of the day; `last_run_at` is what actually stops
    the second arm doing the work again an hour later.
    """
    sched = config["schedule"]
    today = now_et.date().isoformat()
    hour = now_et.hour

    pre_start, pre_end = _window(sched["premarket_window_et"])
    eve_start, eve_end = _window(sched["evening_window_et"])
    if pre_start <= hour < pre_end:
        slot = "premarket"
    elif eve_start <= hour < eve_end:
        slot = "evening"
    else:
        slot = ""

    if event_name != "schedule" and not force:
        return SlotDecision(True, slot or "manual", today,
                            f"{event_name} — proceeding on request")
    if force:
        return SlotDecision(True, slot or "manual", today, "forced")
    if not slot:
        return SlotDecision(
            False, "", today,
            f"{now_et:%H:%M} ET is in neither the {sched['premarket_window_et']} "
            f"nor the {sched['evening_window_et']} ET window")

    minutes = _minutes_since(last_run_at, now_et)
    if minutes is not None and minutes < sched["min_minutes_between_runs"]:
        return SlotDecision(
            False, slot, today,
            f"the universe was re-scored {minutes:.0f} minutes ago — this is the "
            f"other DST arm of the {slot} slot")
    return SlotDecision(True, slot, today, f"{now_et:%H:%M} ET, {slot} slot")


def _minutes_since(stamp: str | None, now: datetime) -> float | None:
    if not stamp:
        return None
    try:
        then = datetime.fromisoformat(stamp)
    except ValueError:
        return None
    if then.tzinfo is None:
        then = then.replace(tzinfo=ET)
    return (now - then).total_seconds() / 60


# --------------------------------------------------------------------------
# pipeline
# --------------------------------------------------------------------------

def run_screen(*, config: dict[str, Any], today: date, discover: bool = True,
               skip_edgar: bool = False, universe_path: Path | None = None,
               client: Any = None, md: Any = None) -> dict[str, Any]:
    """Discovery, then re-score every open offer. Returns the universe.

    Phase 2 re-scores the **whole** universe rather than only what discovery
    just found. An offer rejected on Monday for a 0.9% spread is a different
    trade on Thursday if the stock has drifted down 2%, and an offer that only
    ever gets scored on the day it was filed would never be seen again.

    `client` and `md` are injectable so the pipeline can be driven end to end
    without the network; left alone they are the real ones.
    """
    universe = load_universe(universe_path)
    if client is None and not skip_edgar:
        client = SecClient(config)
    if md is None:
        md = _market_data()

    universe["discovery_error"] = None
    funnel: dict[str, Any] = {}
    if discover and client is not None:
        # A schema change is not caught here. EFTS is undocumented and the SEC
        # can move it; if it has, the screener is blind and every later day
        # would report a quiet week for tender offers. That has to be loud.
        try:
            hits = search_filings(client, config, today=today, stats=funnel)
        except EftsSchemaError:
            raise
        except Exception as exc:  # noqa: BLE001 - a dead network is not a crash
            universe["discovery_error"] = f"{type(exc).__name__}: {exc}"
            print(f"::error title=Odd-lot discovery failed::{type(exc).__name__}: {exc}")
            print("Discovery failed — re-scoring the existing universe anyway. "
                  "Yesterday's offers still expire and still move on price.")
        else:
            print(f"Discovery: {funnel.get('queries', 0)} queries over "
                  f"{funnel.get('window', '?')} returned {funnel.get('raw_hits', 0)} "
                  f"document hit(s) across {len(hits)} filing(s); "
                  f"{len(add_discoveries(universe, hits))} new.")

    # Archived twice, on either side of scoring, and both passes earn their
    # keep. The first uses the expiration read on a previous run and saves
    # fetching a document for an offer that is already over. The second catches
    # the expirations only read just now: without it a newly discovered expired
    # offer would sit in `open` as a rejection until tomorrow, and the report
    # would carry a dead offer in its rejected table rather than its archive.
    stale_after = config["discovery"]["stale_after_days"]
    archived = archive_expired(universe, today, stale_after)

    for entry in universe["open"]:
        score_entry(entry, client=client, md=md, config=config, today=today)
    archived += archive_expired(universe, today, stale_after)
    if archived:
        print(f"Archived {len(archived)} expired offer(s).")

    tiers = [e.get("tier") for e in universe["open"] if e.get("status") == "candidate"]
    print(f"Scored {len(universe['open'])} open offer(s): "
          f"{tiers.count('A')} Tier A, {tiers.count('B')} Tier B, {tiers.count('C')} Tier C, "
          f"{sum(1 for e in universe['open'] if e.get('status') == 'rejected')} rejected.")

    funnel.update(rejection_tally(universe))
    universe["funnel"] = funnel
    if client is not None:
        print(f"SEC requests: {client.fetched} fetched, {client.cache_hits} served from cache.")
    universe["last_run_at"] = datetime.now(ET).isoformat(timespec="seconds")
    return universe


def print_universe(universe: dict[str, Any]) -> None:
    """The dry-run view: one line per tracked offer, with the verdict."""
    print(f"\nUniverse: {len(universe['open'])} open, {len(universe['archive'])} archived. "
          f"Last run {universe.get('last_run_at') or 'never'}.")
    if not universe["open"]:
        print("  (nothing tracked)")
        return
    print(f"\n  {'TICKER':<8} {'FORM':<10} {'FILED':<11} {'TIER':<5} {'SPREAD':>8} "
          f"{'DAYS':>5}  STATUS / REASON")
    print("  " + "-" * 96)
    for entry in sorted(universe["open"], key=lambda e: e.get("filed", ""), reverse=True):
        spread = entry.get("spread_pct")
        reason = (entry.get("rejections") or [entry.get("status", "")])[0]
        print(f"  {(entry.get('ticker') or '—'):<8} {entry.get('form', ''):<10} "
              f"{entry.get('filed', ''):<11} {(entry.get('tier') or '—'):<5} "
              f"{(f'{spread * 100:+.2f}%' if spread is not None else '—'):>8} "
              f"{str(entry.get('days_to_expiry', '—')):>5}  {reason[:52]}")


def write_report(universe: dict[str, Any], report_date: date, config: dict[str, Any],
                 *, slot: str = "") -> Path:
    path = REPO / "reports" / report_date.isoformat() / "odd_lot.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_report(universe, report_date, config, slot=slot))
    return path


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def _emit_github_output(**values: Any) -> None:
    out = os.environ.get("GITHUB_OUTPUT")
    if not out:
        return
    with open(out, "a", encoding="utf-8") as fh:
        for key, value in values.items():
            fh.write(f"{key}={value}\n")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    for name, help_text in (("discover", "query EFTS and append new filings to the universe"),
                            ("rescore", "re-price every open offer, no discovery"),
                            ("run", "discover, then re-score, then write the report")):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("--date", type=date.fromisoformat, default=None,
                       help="report date (default: today in ET)")
        p.add_argument("--dry-run", action="store_true",
                       help="print what would happen; write no universe and no report")
        p.add_argument("--skip-edgar", action="store_true",
                       help="re-score from the stored document readings and live "
                            "quotes, without calling EDGAR at all")
        p.add_argument("--slot", default="", help="premarket or evening, for the report header")

    p = sub.add_parser("report", help="re-render the report from the stored universe")
    p.add_argument("date", nargs="?", type=date.fromisoformat, default=None)

    sub.add_parser("universe", help="print the tracked universe")

    p = sub.add_parser("slot", help="decide whether this invocation is a scheduled slot")
    p.add_argument("--event-name", default="schedule")
    p.add_argument("--force", action="store_true")

    args = ap.parse_args(argv)
    config = load_config()

    if args.cmd == "slot":
        universe = load_universe()
        decision = slot_for(datetime.now(ET), config, event_name=args.event_name,
                            last_run_at=universe.get("last_run_at"), force=args.force)
        print(f"{'PROCEED' if decision.proceed else 'SKIP'}: {decision.reason}")
        print(json.dumps(asdict(decision)))
        _emit_github_output(proceed=str(decision.proceed).lower(), slot=decision.slot,
                            date=decision.date)
        return 0

    if args.cmd == "universe":
        print_universe(load_universe())
        return 0

    if args.cmd == "report":
        report_date = args.date or datetime.now(ET).date()
        path = write_report(load_universe(), report_date, config)
        print(f"Wrote {path.relative_to(REPO)}")
        return 0

    today = args.date or datetime.now(ET).date()
    universe = run_screen(config=config, today=today,
                          discover=args.cmd in ("discover", "run"),
                          skip_edgar=args.skip_edgar)
    print_universe(universe)

    if args.dry_run:
        print("\nDry run — universe and report not written.")
        return 1 if universe.get("discovery_error") else 0

    save_universe(universe)
    print(f"\nWrote {UNIVERSE_PATH.relative_to(REPO)}")
    if args.cmd == "run":
        path = write_report(universe, today, config, slot=args.slot)
        print(f"Wrote {path.relative_to(REPO)}")

    # Deliberately red. A discovery outage means today's filings were never
    # seen, and a green run publishing yesterday's universe would look exactly
    # like a quiet day — which is the normal, correct output most mornings.
    return 1 if universe.get("discovery_error") else 0


if __name__ == "__main__":
    raise SystemExit(main())
