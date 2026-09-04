#!/usr/bin/env python3
"""Fetch and parse the county tax sale lists, CAD records, and lien sources.

    python scripts/tax_deed_sources.py verify              # every source, structure checked
    python scripts/tax_deed_sources.py listings Dallas     # what one county publishes
    python scripts/tax_deed_sources.py cad DCAD 00000123456789000

Every URL comes from `config/tax_deeds.json`; nothing here hardcodes one. County
sites change format without notice, so `verify` fetches each source and asserts
the structural markers the config declares, and fails loudly *with the actual
URL* when they are gone. A screening run verifies before it ingests.

Manners, per the module's own non-goals:

  * robots.txt is honoured. A disallowed path is not fetched, at all, and the
    check that needed it reports `unavailable`.
  * One request per second per host, globally, no exceptions.
  * The User-Agent names the project and carries a contact email. Without an
    email configured this module refuses to make a request rather than fetch
    anonymously.

`requests` is imported lazily so the parsers below are testable on a runner
with nothing pip-installed — which is what `tests/` actually runs on.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.robotparser
from datetime import date, datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import tax_deeds as td  # noqa: E402

CACHE_DIR = REPO / "data" / "tax_deeds" / "cache"
MANUAL_DIR = REPO / "data" / "tax_deeds" / "manual"
CAD_CACHE_DAYS = 30
TIMEOUT = 30


class SourceError(Exception):
    """A source could not be used. Always carries the URL that failed."""

    def __init__(self, url: str, detail: str):
        self.url, self.detail = url, detail
        super().__init__(f"{detail} ({url})")


class RobotsDisallowed(SourceError):
    pass


class StructureChanged(SourceError):
    pass


# --------------------------------------------------------------------------
# HTTP: identity, robots, rate limit
# --------------------------------------------------------------------------

_session: Any = None
_last_request: dict[str, float] = {}

# Per-host interval, raised when a host says it is being asked too often. Tarrant
# CAD answered 429 to 365 straight lookups at the global one-per-second: the
# right response to "too fast" is to slow down for that host, not to keep the
# same pace and record 365 identical failures.
_host_interval: dict[str, float] = {}
MAX_HOST_INTERVAL = 8.0
RATE_LIMIT_RETRIES = 2
_robots: dict[str, Any] = {}

# Sentinel: robots.txt gave no answer at all, as distinct from answering
# "server error" (None), which stays a refusal.
ALLOW_UNKNOWN = object()


# Two hosts refused the plain UA outright on the first live run, and a 403 is
# not a policy statement — robots.txt is, and it is honoured absolutely and
# separately below. What a UA filter usually catches is an unfamiliar token, so
# the fallback wears the "Mozilla/5.0 (compatible; ...)" form that well-behaved
# crawlers have used for decades: it still names this project and still carries
# an address to complain to. That is a different thing from impersonating a
# browser, and the line is that every UA here identifies itself truthfully.
DEFAULT_AGENTS = [
    "invest-trade-daily-taxdeeds/1.0 (+https://github.com/kswodeck/invest-trade-daily; {contact})",
    "Mozilla/5.0 (compatible; invest-trade-daily-taxdeeds/1.0; +mailto:{contact})",
]


def contact_email(cfg: dict) -> str:
    contact = (os.environ.get("TAX_DEED_CONTACT_EMAIL")
               or cfg.get("contact_email") or "").strip()
    if not contact:
        raise SystemExit(
            "No contact email configured. Set TAX_DEED_CONTACT_EMAIL, or "
            "`contact_email` in config/tax_deeds.json. The screener will not "
            "make anonymous requests to county servers.")
    return contact


def user_agents(cfg: dict) -> list[str]:
    """Every UA this run may send, most specific first."""
    contact = contact_email(cfg)
    configured = [cfg.get("user_agent")] + list(cfg.get("user_agent_fallbacks") or [])
    templates = [t for t in configured if t] or DEFAULT_AGENTS
    if len(templates) == 1:
        templates = templates + DEFAULT_AGENTS[1:]
    seen, out = set(), []
    for template in templates:
        agent = template.replace("{contact}", contact)
        if agent not in seen:
            seen.add(agent)
            out.append(agent)
    return out


def user_agent(cfg: dict) -> str:
    """The identity this screener claims. Used for robots.txt, always."""
    return user_agents(cfg)[0]


def session(cfg: dict):
    global _session
    if _session is None:
        import requests  # lazy: keeps this module importable on a bare runner
        _session = requests.Session()
        # A request missing the headers every real client sends is itself a bot
        # signal, and some county WAFs refuse on that alone. Nothing here is
        # untrue about us — the User-Agent still says exactly who we are.
        _session.headers.update({
            "User-Agent": user_agent(cfg),
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
        })
    return _session


def _throttle(url: str, cfg: dict) -> None:
    host = urllib.parse.urlsplit(url).netloc
    base = float(cfg.get("request_interval_seconds") or 1.0)
    configured = (cfg.get("host_interval_seconds") or {}).get(host)
    interval = max(base, float(configured or 0), _host_interval.get(host, 0.0))
    elapsed = time.monotonic() - _last_request.get(host, 0.0)
    if elapsed < interval:
        time.sleep(interval - elapsed)
    _last_request[host] = time.monotonic()


def robots_allows(url: str, cfg: dict) -> tuple[bool, str]:
    """Ask robots.txt. A missing file allows; an unreadable one does not.

    The RFC and every crawler treat 4xx as "no rules, go ahead". A 5xx or a
    connection failure is different: the rules exist and we could not read
    them, so the conservative answer is no.
    """
    if not cfg.get("respect_robots_txt", True):
        return True, "robots.txt checking disabled in config"
    parts = urllib.parse.urlsplit(url)
    root = f"{parts.scheme}://{parts.netloc}"
    if root not in _robots:
        parser = urllib.robotparser.RobotFileParser()
        parser.set_url(f"{root}/robots.txt")
        error: Exception | None = None
        for attempt in range(2):
            try:
                _throttle(root, cfg)
                resp = session(cfg).get(f"{root}/robots.txt", timeout=TIMEOUT)
            except Exception as exc:  # noqa: BLE001
                error = exc
                continue
            error = None
            if resp.status_code >= 500:
                # The server is speaking, and what it says is "I am broken".
                # Be conservative: no rules could be read, so do not crawl.
                _robots[root] = None
                _robots[f"{root}!why"] = f"robots.txt returned HTTP {resp.status_code}"
            else:
                # 4xx means there are no rules, which is permission.
                parser.parse(resp.text.splitlines() if resp.status_code < 400 else [])
                _robots[root] = parser
            break
        if error is not None:
            # A connection reset or timeout is not a statement of policy — it
            # is no signal at all, and treating silence as prohibition
            # permanently disabled two sources that plainly permit access
            # (hazards.fema.gov among them). Retried once above; allow, and
            # say so, rather than let a flaky hop become a standing ban.
            _robots[root] = ALLOW_UNKNOWN
            _robots[f"{root}!why"] = f"{type(error).__name__}: {error}"

    parser = _robots.get(root)
    if parser is ALLOW_UNKNOWN:
        return True, (f"{root}/robots.txt was unreachable twice "
                      f"({_robots.get(f'{root}!why')}) — a network failure states no policy, "
                      f"so this is treated as no rules rather than as a prohibition")
    if parser is None:
        why = _robots.get(f"{root}!why", "robots.txt returned a server error")
        return False, f"could not read {root}/robots.txt ({why}) — not fetching"
    # Always our own name, never whichever UA string a refusal made us fall
    # back to — robots rules apply to who we are, not to what we sent.
    agent = user_agent(cfg).split("/")[0]
    if parser.can_fetch(agent, url) or parser.can_fetch("*", url):
        return True, "allowed by robots.txt"
    return False, f"{root}/robots.txt disallows this path for {agent}"


# What an HTTP status actually means for a county source, because the fix
# differs and the first live run made that concrete: five sources failed with
# three unrelated causes and one message telling the operator to edit
# `column_map` for all of them.
def _explain_status(code: int, url: str) -> str:
    if code in (401, 403):
        return (f"HTTP {code}: the host refused this User-Agent. Not a format change — the "
                f"page may be fine in a browser. Some county vendors block non-browser "
                f"clients outright; check whether the list is published somewhere else, or "
                f"export it by hand. Do not spoof a browser to get around this.")
    if code == 404:
        return (f"HTTP {code}: this URL does not exist. It moved or was never right — find "
                f"the current one and update it in config/tax_deeds.json.")
    if code == 400:
        return (f"HTTP {code}: the host rejected the request itself, usually a missing or "
                f"wrong query parameter rather than a wrong URL.")
    if code == 429:
        return f"HTTP {code}: rate limited. Raise `request_interval_seconds` in the config."
    if code >= 500:
        return f"HTTP {code}: the host is broken right now. Nothing to fix here; try later."
    return f"HTTP {code} from {url}"


def fetch(url: str, cfg: dict, *, params: dict | None = None) -> str:
    """One polite GET, retried through the UA list on a refusal.

    robots.txt is checked once, against this screener's own identity, and a
    disallow ends it — the retry below never re-asks and never re-decides. It
    exists only for hosts that answer 401/403 to an unfamiliar User-Agent while
    publishing no rule against us at all.
    """
    allowed, why = robots_allows(url, cfg)
    if not allowed:
        raise RobotsDisallowed(url, why)

    agents = user_agents(cfg)
    host = urllib.parse.urlsplit(url).netloc
    last: Exception | None = None
    backoffs = 0
    index = -1
    while True:
        index = min(index + 1, len(agents) - 1)
        agent = agents[index]
        _throttle(url, cfg)
        try:
            resp = session(cfg).get(url, params=params, timeout=TIMEOUT,
                                    headers={"User-Agent": agent})
        except SourceError:
            raise
        except Exception as exc:  # noqa: BLE001
            last = SourceError(url, f"{type(exc).__name__}: {exc}")
            break
        if resp.status_code in (401, 403) and index + 1 < len(agents):
            continue
        if resp.status_code == 429:
            # Back off for this host and try again rather than burning the rest
            # of the run recording the same refusal once per property.
            current = max(_host_interval.get(host, 0.0),
                          float(cfg.get("request_interval_seconds") or 1.0))
            _host_interval[host] = min(current * 2, MAX_HOST_INTERVAL)
            if backoffs < RATE_LIMIT_RETRIES:
                backoffs += 1
                time.sleep(_host_interval[host])
                continue
        if resp.status_code >= 400:
            detail = _explain_status(resp.status_code, url)
            if resp.status_code in (401, 403):
                detail += (f" All {len(agents)} configured User-Agents were refused, so this "
                           f"is the host's filter and not a format change.")
            if resp.status_code == 429:
                detail += (f" Backed off to {_host_interval.get(host, 0):.0f}s for this host "
                           f"and retried {backoffs} time(s); pin it with "
                           f"`host_interval_seconds` in config/tax_deeds.json.")
            raise SourceError(url, detail)
        return resp.text
    raise last or SourceError(url, "no User-Agent was accepted")


def fetch_json(url: str, cfg: dict, *, params: dict | None = None) -> Any:
    text = fetch(url, cfg, params=params)
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise StructureChanged(url, f"expected JSON, got {text[:80]!r}") from exc


# --------------------------------------------------------------------------
# HTML parsing — stdlib only, so the parser tests run on a bare runner
# --------------------------------------------------------------------------

class _TableCollector(HTMLParser):
    """Every <table> on the page as rows of {text, href} cells.

    County pages nest the real sale list inside one or more layout tables, so
    each open table gets its own frame holding its own in-progress row and
    cell. A single shared `_row` was enough to make the inner table's first
    `<tr>` discard the outer cell that contained it, which loses whichever
    table happens to be wrapped.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tables: list[list[list[dict]]] = []
        self._frames: list[dict] = []

    @property
    def _frame(self) -> dict | None:
        return self._frames[-1] if self._frames else None

    def handle_starttag(self, tag, attrs):
        frame = self._frame
        if tag == "table":
            self._frames.append({"rows": [], "row": None, "cell": None})
        elif frame is None:
            return
        elif tag == "tr":
            frame["row"] = []
        elif tag in ("td", "th"):
            if frame["row"] is None:
                frame["row"] = []
            frame["cell"] = {"text": [], "href": ""}
        elif tag == "a" and frame["cell"] is not None and not frame["cell"]["href"]:
            frame["cell"]["href"] = dict(attrs).get("href", "") or ""
        elif tag in ("br", "p", "div") and frame["cell"] is not None:
            frame["cell"]["text"].append(" ")

    def handle_endtag(self, tag):
        frame = self._frame
        if frame is None:
            return
        if tag in ("td", "th") and frame["cell"] is not None:
            text = re.sub(r"\s+", " ", "".join(frame["cell"]["text"])).strip()
            frame["row"] = frame["row"] if frame["row"] is not None else []
            frame["row"].append({"text": text, "href": frame["cell"]["href"]})
            frame["cell"] = None
        elif tag == "tr":
            if frame["row"]:
                frame["rows"].append(frame["row"])
            frame["row"] = None
        elif tag == "table":
            self.tables.append(self._frames.pop()["rows"])

    def handle_data(self, data):
        frame = self._frame
        if frame is not None and frame["cell"] is not None:
            frame["cell"]["text"].append(data)

    def close(self):
        super().close()
        while self._frames:  # unclosed <table>, common enough on county pages
            frame = self._frames.pop()
            if frame["row"]:
                frame["rows"].append(frame["row"])
            self.tables.append(frame["rows"])


def collect_tables(html: str) -> list[list[list[dict]]]:
    parser = _TableCollector()
    parser.feed(html)
    parser.close()
    return parser.tables


def _norm(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", re.sub(r"\s+", " ", str(text or "").lower())).strip()


def map_columns(header: list[str], column_map: dict[str, list[str]]) -> dict[str, int]:
    """Canonical field -> column index, by the substring patterns in config.

    Fields are resolved in config order, which is therefore precedence order:
    `minimum_opening_bid` lists "minimum bid" before "judgment" because a
    judgment amount is only a last-resort stand-in for an opening bid.
    """
    normalized = [_norm(h) for h in header]
    mapping: dict[str, int] = {}
    used: set[int] = set()
    for field, patterns in column_map.items():
        for pattern in patterns:
            needle = _norm(pattern)
            for index, text in enumerate(normalized):
                if index in used or not text or needle not in text:
                    continue
                mapping[field] = index
                used.add(index)
                break
            if field in mapping:
                break
    return mapping


# A list we cannot price or identify is not a list we can screen.
REQUIRED_FIELDS = ("minimum_opening_bid",)
IDENTIFYING_FIELDS = ("account", "cause_number")


def rows_from_tables(tables: list[list[list[dict]]], column_map: dict[str, list[str]]
                     ) -> tuple[list[dict], dict]:
    """Pick the table that looks like the sale list and read its rows.

    Returns the parsed rows and a diagnostic describing what was found, which
    is what the caller puts in the error when the structure has changed.
    """
    best: tuple[int, list[list[dict]], dict[str, int], list[str]] | None = None
    seen_headers: list[list[str]] = []

    for table in tables:
        if len(table) < 2:
            continue
        header = [c["text"] for c in table[0]]
        seen_headers.append(header)
        mapping = map_columns(header, column_map)
        score = len(mapping)
        if score and (best is None or score > best[0]):
            best = (score, table, mapping, header)

    if best is None:
        # Two very different failures, and the first live run conflated them:
        # a page with no <table> at all is almost always a JavaScript app that
        # renders its list client-side, and no amount of `column_map` editing
        # will ever parse it. A page with tables but none that map is the
        # ordinary format change.
        total = sum(len(t) for t in tables)
        if not tables or total == 0:
            return [], {"reason": "the page contains no HTML table at all",
                        "no_tables": True, "headers_seen": []}
        return [], {"reason": "tables are present but none has a header row and a data row",
                    "headers_seen": seen_headers}

    _, table, mapping, header = best
    missing = [f for f in REQUIRED_FIELDS if f not in mapping]
    if not any(f in mapping for f in IDENTIFYING_FIELDS):
        missing.append("account or cause_number")
    if missing:
        return [], {"reason": f"the best-matching table is missing {', '.join(missing)}",
                    "header_matched": header, "mapped": sorted(mapping),
                    "headers_seen": seen_headers}

    rows: list[dict] = []
    for raw in table[1:]:
        if len(raw) < 2 or all(not c["text"] for c in raw):
            continue
        record: dict[str, Any] = {}
        for field, index in mapping.items():
            if index < len(raw):
                record[field] = raw[index]["text"]
        href = next((c["href"] for c in raw if c["href"]), "")
        if href:
            record["_href"] = href
        rows.append(record)
    return rows, {"header_matched": header, "mapped": sorted(mapping), "rows": len(rows)}


def _dig(payload: Any, path: str) -> Any:
    """Walk a dotted path into decoded JSON. `data.results` or `` for the root."""
    for part in [p for p in str(path or "").split(".") if p]:
        if isinstance(payload, dict):
            payload = payload.get(part)
        elif isinstance(payload, list) and part.isdigit():
            payload = payload[int(part)] if int(part) < len(payload) else None
        else:
            return None
    return payload


def rows_from_json(text: str, source: dict) -> tuple[list[dict], dict]:
    """A JSON list endpoint, mapped by `field_map` rather than header text.

    This exists because three of the four counties publish through a single
    JavaScript app that renders its table client-side — there is no HTML table
    to parse, only the endpoint the page itself calls. Once that endpoint is
    known, wiring it up stays a config change: `records_path` says where the
    array lives and `field_map` maps canonical field -> dotted key.
    """
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        return [], {"reason": f"the response is not JSON ({exc})"}

    records = _dig(payload, source.get("records_path", ""))
    if isinstance(records, dict):
        records = [records]
    if not isinstance(records, list):
        keys = sorted(payload)[:12] if isinstance(payload, dict) else type(payload).__name__
        return [], {"reason": f"no array of records at records_path "
                              f"{source.get('records_path', '')!r}; top level holds {keys}"}

    field_map = source.get("field_map") or {}
    if not field_map:
        sample = sorted((records[0] or {}).keys())[:20] if records else []
        return [], {"reason": f"no `field_map` configured for this JSON source; the first "
                              f"record's keys are {sample}"}

    rows = []
    for record in records:
        if not isinstance(record, dict):
            continue
        row = {}
        for field, key in field_map.items():
            value = _dig(record, key)
            if value not in (None, ""):
                row[field] = value
        if row:
            rows.append(row)
    return rows, {"mapped": sorted(field_map), "rows": len(rows)}


# --------------------------------------------------------------------------
# discovery: the list is in the page, just not in a <table>
# --------------------------------------------------------------------------
#
# Three of the four counties publish through one JavaScript app, and a table
# parser can never read it. But a client-rendered page still has to get its data
# from somewhere, and in practice it is sitting right there in the HTML — in a
# __NEXT_DATA__ blob, a hydration assignment, or a JSON-LD block. So rather than
# asking an operator to open dev tools and hand-write a field map, look for it.
#
# The mapping is inferred from the same `column_map` the table parser uses: a
# JSON key named `minimumBid` matches the "minimum bid" pattern once both are
# normalized, so a county's existing config keeps working unchanged.

_SCRIPT = re.compile(r"<script\b([^>]*)>(.*?)</script\s*>", re.I | re.S)
_ASSIGNED = re.compile(r"=\s*(\{.*\}|\[.*\])\s*;?\s*$", re.S)


def _balanced(text: str, start: int) -> str | None:
    """The JSON value beginning at `start`, by brace/bracket matching."""
    opener = text[start]
    closer = {"{": "}", "[": "]"}.get(opener)
    if not closer:
        return None
    depth, in_string, escaped = 0, False, False
    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == opener:
            depth += 1
        elif char == closer:
            depth -= 1
            if depth == 0:
                return text[start:index + 1]
    return None


def embedded_json(html: str) -> list[Any]:
    """Every JSON value the page carries inline, decoded."""
    out: list[Any] = []
    for attrs, body in _SCRIPT.findall(html or ""):
        body = body.strip()
        if not body:
            continue
        candidates: list[str] = []
        if "json" in attrs.lower() or body[:1] in "{[":
            candidates.append(body)
        match = _ASSIGNED.search(body)
        if match:
            candidates.append(match.group(1))
        for index, char in enumerate(body):
            if char in "{[" and len(candidates) < 6:
                chunk = _balanced(body, index)
                if chunk and len(chunk) > 200:
                    candidates.append(chunk)
                break
        for chunk in candidates:
            try:
                out.append(json.loads(chunk))
            except (json.JSONDecodeError, RecursionError):
                continue
    return out


def _record_arrays(payload: Any, path: str = "", depth: int = 0):
    """Every array-of-objects in a decoded payload, with its dotted path."""
    if depth > 8:
        return
    if isinstance(payload, list):
        dicts = [item for item in payload if isinstance(item, dict)]
        if len(dicts) >= 1 and len(dicts) >= len(payload) / 2:
            yield path, dicts
        for index, item in enumerate(payload[:50]):
            yield from _record_arrays(item, f"{path}.{index}".lstrip("."), depth + 1)
    elif isinstance(payload, dict):
        for key, value in payload.items():
            yield from _record_arrays(value, f"{path}.{key}".lstrip("."), depth + 1)


def _flatten_keys(record: dict, prefix: str = "", depth: int = 0) -> dict[str, str]:
    """Leaf key -> dotted path, so `addr.line1` is mappable as one field."""
    out: dict[str, str] = {}
    for key, value in record.items():
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict) and depth < 2:
            out.update(_flatten_keys(value, path, depth + 1))
        elif not isinstance(value, (dict, list)):
            out[path] = path
    return out


# JSON keys are camelCase and dotted where table headers are spaced words, and
# `_norm` alone leaves "minimumBid" as "minimumbid", which the pattern "minimum
# bid" can never match. Split the humps and the separators first, and match on
# the whole dotted path so a nested `address.line1` still reads as an address.
_HUMPS = re.compile(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")


def _key_words(path: str) -> str:
    return _norm(_HUMPS.sub(" ", str(path or "")).replace(".", " ").replace("_", " "))


def _flatten_values(payload: Any, depth: int = 0) -> list[Any]:
    """Every scalar in a record, however nested."""
    if depth > 3:
        return []
    if isinstance(payload, dict):
        return [v for value in payload.values() for v in _flatten_values(value, depth + 1)]
    if isinstance(payload, list):
        return [v for item in payload[:20] for v in _flatten_values(item, depth + 1)]
    return [] if payload is None else [payload]


def infer_field_map(keys: Iterable[str], column_map: dict[str, list[str]]) -> dict[str, str]:
    """Canonical field -> JSON key, using the source's own header patterns.

    `minimumBid`, `minimum_bid` and `Minimum Bid` all reduce to the same words,
    which is why a config written for an HTML table transfers to the JSON behind
    it with no new configuration at all.
    """
    paths = list(keys)
    mapping = map_columns([_key_words(path) for path in paths], column_map)
    return {field: paths[index] for field, index in mapping.items()}


def best_record_array(payloads: Iterable[Any], column_map: dict[str, list[str]]
                      ) -> tuple[list[dict], dict]:
    """The array in these payloads that most looks like a sale list.

    Qualifying means carrying an opening bid and something to identify a
    property by — the same bar `rows_from_tables` applies, so a discovered list
    is never worse-specified than a parsed one, and navigation menus and config
    blobs cannot pass it.
    """
    best: tuple[int, list[dict], dict[str, str], str] | None = None
    seen_paths: list[str] = []

    for payload in payloads:
        for path, records in _record_arrays(payload):
            field_map = infer_field_map(_flatten_keys(records[0]), column_map)
            if not any(f in field_map for f in IDENTIFYING_FIELDS):
                continue
            if not all(f in field_map for f in REQUIRED_FIELDS):
                continue
            seen_paths.append(path)
            score = len(field_map) * 100 + min(len(records), 99)
            if best is None or score > best[0]:
                best = (score, records, field_map, path)

    if best is None:
        return [], {"reason": "no JSON array looked like a sale list",
                    "candidates": seen_paths[:5]}

    _, records, field_map, path = best
    rows = []
    for record in records:
        row = {field: _dig(record, key) for field, key in field_map.items()}
        row = {k: v for k, v in row.items() if v not in (None, "")}
        if row:
            # Everything the record held, mapped or not. A cross-county
            # aggregator names the county in a field nothing maps to, and
            # filtering on the mapped values alone silently dropped every row
            # of three working sources.
            row["_blob"] = " ".join(
                str(v) for v in _flatten_values(record)).lower()
            rows.append(row)
    return rows, {"mapped": sorted(field_map), "rows": len(rows),
                  "discovered_path": path, "discovered_field_map": field_map,
                  "candidates": seen_paths[:5]}


def _matches_county(rows: list[dict], source: dict) -> bool:
    """Does this batch actually contain the county the source is scoped to?

    No filter configured means any row is ours. An empty batch is not.
    """
    wanted = source.get("county_filter")
    if not wanted:
        return bool(rows)
    needle = wanted.lower()
    return any(needle in " ".join(str(v) for v in row.values()).lower() for row in rows)


def discover_json_records(html: str, source: dict) -> tuple[list[dict], dict]:
    """Find the sale list inside the JSON a client-rendered page ships with."""
    rows, diag = best_record_array(embedded_json(html), source.get("column_map") or {})
    if not rows:
        diag["reason"] = "no embedded JSON array looked like a sale list"
    return rows, diag


# --------------------------------------------------------------------------
# discovery, part two: the page fetches its list rather than shipping it
# --------------------------------------------------------------------------
#
# taxsales.lgbs.com carries no table AND no embedded records — it calls an API
# after load. The endpoint is not a secret: it is written in the page's own
# scripts. So collect the API-shaped URLs the page references, GET the
# plausible ones, and score whatever comes back the same way. This is the
# difference between "find the endpoint yourself in dev tools" and the tool
# doing it, which is the whole point of the exercise.
#
# Bounded on purpose: only URLs the page itself names, only the same host, and
# only MAX_API_PROBES of them, at the same one-per-second everything else obeys.
# It never guesses at paths the site did not mention.

_API_REF = re.compile(r"""["'`](?P<url>(?:https?://[^"'`\s]+|/)[^"'`\s]*"""
                      r"""(?:api|rest|search|sales|properties|listings)[^"'`\s]*)["'`]""",
                      re.I)
_SCRIPT_SRC = re.compile(r"""<script[^>]+src\s*=\s*["']([^"']+)["']""", re.I)
MAX_API_PROBES = 8
MAX_BUNDLES = 3

# A first page is not a sale list. These APIs page at 10-50 records and hand
# back the next URL; the first live success returned exactly 10 rows per county,
# which is a page size, not a month's docket. Bounded so a runaway `next` chain
# cannot spin forever.
MAX_PAGES = 40
MAX_ROWS = 5000
_NEXT_KEYS = ("next", "next_page", "nextPage", "next_url", "nextUrl")


def _next_url(payload: Any, current: str) -> str | None:
    """The following page, for the paging shapes these APIs actually use."""
    if not isinstance(payload, dict):
        return None
    for key in _NEXT_KEYS:
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return urllib.parse.urljoin(current, value)
    links = payload.get("links")
    if isinstance(links, dict):
        for key in _NEXT_KEYS:
            value = links.get(key)
            if isinstance(value, str) and value.strip():
                return urllib.parse.urljoin(current, value)
    return None


# These endpoints serve every county their firm covers. Paging the whole state
# at one request per second is not a plan — the first live success walked 40
# pages, 400 rows, and none of them were ours. So ask the API to filter, using
# the field name the API itself uses as the query key. `query_params` in config
# pins it once it is known, and skips the probing entirely.
COUNTY_PARAM_GUESSES = ("county", "county_name", "county__name", "search", "q")
MAX_NARROW_PROBES = 10


def _narrow_to_county(url: str, payload: Any, rows: list[dict], diag: dict,
                      source: dict, cfg: dict):
    """Re-request the endpoint filtered to this county, if that is possible."""
    column_map = source.get("column_map") or {}
    wanted = source.get("county_filter")
    pinned = source.get("query_params") or {}

    def request(params: dict):
        query = urllib.parse.urlencode(params)
        joiner = "&" if urllib.parse.urlsplit(url).query else "?"
        target = f"{url}{joiner}{query}"
        try:
            body = fetch(target, cfg)
            fresh = json.loads(body)
        except (SourceError, json.JSONDecodeError):
            return None
        found, found_diag = best_record_array([fresh], column_map)
        return (target, fresh, found, found_diag) if found else None

    if pinned:
        result = request(pinned)
        return (*result, pinned) if result else (url, payload, rows, diag, {})

    if not wanted:
        return url, payload, rows, diag, {}

    # Already ours? Then the endpoint is county-scoped and needs no narrowing.
    if any(wanted.lower() in str(row.get("county", "")).lower() for row in rows):
        return url, payload, rows, diag, {}

    key = (diag.get("discovered_field_map") or {}).get("county")
    observed = [str(row["county"]) for row in rows if row.get("county")]
    values = county_value_variants(wanted, observed)
    params = [p for p in dict.fromkeys([key, *COUNTY_PARAM_GUESSES]) if p]

    # Bounded: every value against the API's own field name, then the best
    # value against the guesses. Fully crossing the two would be 25 requests at
    # one per second for a filter that usually works on the first try.
    attempts = [(params[0], value) for value in values]
    attempts += [(param, values[0]) for param in params[1:]]

    for param, value in attempts[:MAX_NARROW_PROBES]:
        result = request({param: value})
        if not result:
            continue
        target, fresh, found, found_diag = result
        matched = sum(1 for row in found if wanted.lower() in str(row.get("county", "")).lower())
        # Accept only if the parameter actually did something. An API that
        # ignores an unknown query key returns the unfiltered list, and taking
        # that would look like success while changing nothing.
        if matched and matched >= len(found) * 0.9:
            found_diag["narrowed_by"] = f"{param}={value}"
            return target, fresh, found, found_diag, {param: value}
    diag["narrowing_failed"] = [f"{p}={v}" for p, v in attempts[:MAX_NARROW_PROBES]]
    return url, payload, rows, diag, {}


def county_value_variants(wanted: str, observed: Iterable[str]) -> list[str]:
    """How this API spells a county name, learned from what it just sent.

    The live feed returns `GALVESTON COUNTY` and `PHILADELPHIA COUNTY` — it is
    nationwide, and it stores the name uppercased with a suffix. Querying it for
    `Tarrant` finds nothing. Rather than hardcode that shape, read it off the
    records: whatever form the data is in is the form the filter wants.
    """
    variants: list[str] = []
    for sample in list(observed)[:20]:
        text = str(sample).strip()
        if not text:
            continue
        suffix = ""
        match = re.search(r"\s+(COUNTY|County|county|PARISH|Parish)$", text)
        if match:
            suffix = match.group(0)
        body = text[:len(text) - len(suffix)] if suffix else text
        if body.isupper():
            candidate = f"{wanted.upper()}{suffix.upper() if suffix else ''}"
        elif body.islower():
            candidate = f"{wanted.lower()}{suffix.lower() if suffix else ''}"
        else:
            candidate = f"{wanted}{suffix}"
        if candidate not in variants:
            variants.append(candidate)

    for candidate in (wanted, f"{wanted} County", wanted.upper(), f"{wanted.upper()} COUNTY"):
        if candidate not in variants:
            variants.append(candidate)
    return variants


def follow_pages(payload: Any, rows: list[dict], source: dict, cfg: dict,
                 url: str) -> tuple[int, list[dict]]:
    """Walk `next` until the list runs out. Returns (pages read, all rows)."""
    column_map = source.get("column_map") or {}
    seen_urls = {url}
    # One property is one row however many times paging hands it back. A `next`
    # that points at a page already read terminates the walk, but a URL that
    # merely spells the same page differently (`?page=1` versus no parameter)
    # does not — and a list that shifts between requests can repeat a record
    # with no loop at all. So dedupe on the property, not on the URL.
    seen_rows = {_row_key(row) for row in rows}
    pages = 1
    current = _next_url(payload, url)
    while current and current not in seen_urls and pages < MAX_PAGES and len(rows) < MAX_ROWS:
        seen_urls.add(current)
        try:
            body = fetch(current, cfg)
            page = json.loads(body)
        except (SourceError, json.JSONDecodeError):
            break
        more, _ = best_record_array([page], column_map)
        fresh = [row for row in more if _row_key(row) not in seen_rows]
        if not fresh:
            break
        seen_rows.update(_row_key(row) for row in fresh)
        rows.extend(fresh)
        pages += 1
        current = _next_url(page, current)
    return pages, rows


def _row_key(row: dict) -> str:
    """What makes this row one property, for deduplication across pages."""
    account = td.normalize_account(row.get("account"))
    cause = re.sub(r"[^0-9A-Za-z]", "", str(row.get("cause_number") or "")).upper()
    return f"{account}|{cause}" if (account or cause) else str(row.get("_blob") or row)


def candidate_api_urls(html: str, base_url: str) -> list[str]:
    """API-shaped URLs the page names, most promising first, same host only."""
    host = urllib.parse.urlsplit(base_url).netloc
    found: list[str] = []
    for match in _API_REF.finditer(html or ""):
        raw = match.group("url")
        if raw.startswith("//"):
            raw = "https:" + raw
        absolute = urllib.parse.urljoin(base_url, raw)
        parts = urllib.parse.urlsplit(absolute)
        if parts.scheme not in ("http", "https") or parts.netloc != host:
            continue
        if re.search(r"\.(?:js|css|png|jpe?g|svg|gif|woff2?|ico|map)$", parts.path, re.I):
            continue
        if absolute not in found:
            found.append(absolute)

    return sorted(found, key=_api_rank)


def _api_rank(url: str) -> tuple:
    """Most-likely-to-be-the-list first, so the probe budget is not wasted.

    Scored on the path and query only. Matching the whole URL let the host name
    decide it: every candidate on `taxsales.lgbs.com` contains "sales", so they
    all tied and the bare `/api/` won on length — spending two probes before
    reaching `/api/property_sales/`.
    """
    parts = urllib.parse.urlsplit(url.lower())
    path = f"{parts.path}?{parts.query}"
    return (0 if re.search(r"sale|propert|listing", path) else 1,
            0 if "/api/" in path else 1,
            len(path))


def discover_api_records(html: str, source: dict, cfg: dict, url: str
                         ) -> tuple[list[dict], dict]:
    """Follow the page's own API references until one returns the sale list."""
    column_map = source.get("column_map") or {}
    tried: list[str] = []

    bundles = []
    for src in _SCRIPT_SRC.findall(html or "")[:20]:
        absolute = urllib.parse.urljoin(url, src)
        if urllib.parse.urlsplit(absolute).netloc == urllib.parse.urlsplit(url).netloc:
            bundles.append(absolute)

    texts = [html]
    for bundle in bundles[:MAX_BUNDLES]:
        try:
            texts.append(fetch(bundle, cfg))
        except SourceError:
            continue

    # Rank across every source of references at once. Sorting each file
    # separately put the page's bare `/api/` ahead of the bundle's
    # `/api/property_sales/`, spending probes on the least likely candidate.
    seen: list[str] = []
    for text in texts:
        for candidate in candidate_api_urls(text, url):
            if candidate not in seen:
                seen.append(candidate)
    candidates = sorted(seen, key=_api_rank)

    for candidate in candidates[:MAX_API_PROBES]:
        tried.append(candidate)
        try:
            body = fetch(candidate, cfg)
        except SourceError:
            continue
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            continue
        rows, diag = best_record_array([payload], column_map)
        if rows:
            endpoint, payload, rows, diag, params = _narrow_to_county(
                candidate, payload, rows, diag, source, cfg)
            pages, rows = follow_pages(payload, rows, source, cfg, endpoint)
            diag.update(api_endpoint=endpoint, probed=tried, pages=pages,
                        rows=len(rows), query_params=params)
            return rows, diag

    return [], {"reason": f"followed {len(tried)} API reference(s) the page names and none "
                          f"returned a sale list", "probed": tried}


def rows_from_csv(text: str, column_map: dict[str, list[str]]) -> tuple[list[dict], dict]:
    reader = list(csv.reader(io.StringIO(text)))
    if len(reader) < 2:
        return [], {"reason": "fewer than two CSV rows"}
    header = reader[0]
    mapping = map_columns(header, column_map)
    missing = [f for f in REQUIRED_FIELDS if f not in mapping]
    if not any(f in mapping for f in IDENTIFYING_FIELDS):
        missing.append("account or cause_number")
    if missing:
        return [], {"reason": f"CSV is missing {', '.join(missing)}",
                    "header_matched": header, "mapped": sorted(mapping)}
    rows = []
    for raw in reader[1:]:
        if not any(cell.strip() for cell in raw):
            continue
        rows.append({field: raw[i] for field, i in mapping.items() if i < len(raw)})
    return rows, {"header_matched": header, "mapped": sorted(mapping), "rows": len(rows)}


# --------------------------------------------------------------------------
# label/value parsing, for CAD detail pages
# --------------------------------------------------------------------------

class _TextCollector(HTMLParser):
    """Visible text, with table cells kept as separate runs."""

    SKIP = {"script", "style", "noscript"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.runs: list[str] = []
        self._skip = 0
        self._buf: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip += 1
        elif tag in ("td", "th", "tr", "br", "p", "div", "li", "span", "dt", "dd"):
            self._flush()

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip:
            self._skip -= 1
        elif tag in ("td", "th", "tr", "p", "div", "li", "dt", "dd"):
            self._flush()

    def handle_data(self, data):
        if not self._skip:
            self._buf.append(data)

    def _flush(self):
        text = re.sub(r"\s+", " ", "".join(self._buf)).strip()
        if text:
            self.runs.append(text)
        self._buf = []

    def close(self):
        super().close()
        self._flush()


def text_runs(html: str) -> list[str]:
    parser = _TextCollector()
    parser.feed(html)
    parser.close()
    return parser.runs


def label_values(html: str) -> list[tuple[str, str]]:
    """(label, value) pairs from a CAD detail page.

    Two shapes cover every district here: adjacent table cells, and a single
    run reading `Label: value`. Both are collected; the field map below takes
    the first that matches.
    """
    runs = text_runs(html)
    pairs: list[tuple[str, str]] = []
    for index, run in enumerate(runs):
        if ":" in run:
            label, _, value = run.partition(":")
            if label.strip() and value.strip():
                pairs.append((label.strip(), value.strip()))
        if index + 1 < len(runs):
            pairs.append((run, runs[index + 1]))
    return pairs


# Structural, not locational, so it lives in code — but a district may override
# it with a `field_map` key in config when its page uses different wording.
CAD_FIELDS: dict[str, list[str]] = {
    "appraised_value": ["total appraised value", "appraised value", "total market value",
                        "total value", "market value"],
    "land_value": ["land value", "land market", "land appraised"],
    "improvement_value": ["improvement value", "improvement market", "building value",
                          "impr value"],
    "year_built": ["year built", "yr built", "effective year built"],
    "sqft": ["living area", "building area", "total living", "main area", "square feet",
             "sq ft"],
    "lot_sqft": ["land sqft", "land square feet", "lot size", "land area"],
    "acres": ["acres", "acreage"],
    "legal_description": ["legal description", "legal"],
    "subdivision": ["subdivision", "addition", "neighborhood"],
    "situs": ["situs", "property address", "location address", "site address"],
    "exemptions": ["exemption"],
    "land_use_code": ["land use code", "state code", "sptb", "property class code",
                      "use code", "division code"],
    "land_use_description": ["land use", "property type", "improvement type",
                             "class description", "property use"],
    "owner_name": ["owner name", "owner"],
    "zip": ["zip", "postal code"],
    "frontage": ["frontage", "front feet", "road frontage"],
}

MONEY_FIELDS = {"appraised_value", "land_value", "improvement_value"}
INT_FIELDS = {"year_built", "sqft", "lot_sqft"}
FLOAT_FIELDS = {"acres", "frontage"}


# How much wording a label may carry around the pattern before it stops being
# that label. "Total Appraised Value" is still the appraised value; "HYDE
# JACKSON ADDITION BLOCK 7 LOT 15" is not the subdivision, it is a legal
# description that happens to contain the word "addition" — and pairing it with
# the next run put the literal string "Neighborhood" in the subdivision field.
LABEL_SLACK = 12


def _label_matches(label: str, needle: str) -> bool:
    normalized = _norm(label)
    return bool(needle) and needle in normalized and len(normalized) <= len(needle) + LABEL_SLACK


def parse_cad_record(html: str, field_map: dict[str, list[str]] | None = None) -> dict:
    """Canonical CAD fields from a district detail page.

    Fields resolve in `field_map` order and consume the pair they matched, so
    `land_use_code` takes "Land Use Code: A11" and `land_use_description` has
    to go find "Property Type" instead of reporting the code twice.
    """
    field_map = field_map or CAD_FIELDS
    pairs = label_values(html)
    used: set[int] = set()
    record: dict[str, Any] = {}

    for field, patterns in field_map.items():
        for pattern in patterns:
            needle = _norm(pattern)
            for index, (label, value) in enumerate(pairs):
                if index in used or not value.strip() or not _label_matches(label, needle):
                    continue
                if field in MONEY_FIELDS:
                    parsed = td.parse_money(value)
                elif field in INT_FIELDS:
                    digits = re.sub(r"[^0-9]", "", value)
                    parsed = int(digits) if digits else None
                elif field in FLOAT_FIELDS:
                    parsed = td.parse_money(value)
                else:
                    parsed = value.strip()
                if parsed not in (None, ""):
                    record[field] = parsed
                    used.add(index)
                    break
            if field in record:
                break

    exemptions = [v for label, v in pairs
                  if _label_matches(label, "exempt") and v.strip()]
    record["exemptions"] = sorted({
        part.strip() for value in exemptions
        for part in re.split(r"[,;/]| and ", value) if part.strip()
        and _norm(part) not in ("none", "n a", "no", "0")
    })

    haystack = _norm(" ".join(f"{a} {b}" for a, b in pairs))
    if re.search(r"\bhomestead\b", haystack) and not re.search(
            r"homestead\s*(?:exemption)?\s*[:\-]?\s*(?:no|none|0|false)\b", haystack):
        record["homestead"] = True
    return record


# --------------------------------------------------------------------------
# county sale lists
# --------------------------------------------------------------------------

def manual_path(source_id: str) -> Path:
    return MANUAL_DIR / f"{source_id}.csv"


def load_source(source: dict, cfg: dict) -> tuple[list[dict], dict]:
    """Rows from one configured source, live or from a manual CSV drop.

    The manual path exists because several Texas constable sales publish only
    a PDF, and this repo does not carry a PDF dependency. Rather than pretend
    to parse one, the source reports what it needs and reads
    `data/tax_deeds/manual/<source_id>.csv` if an operator exported it by hand.
    """
    url = source.get("url", "")
    column_map = source.get("column_map") or {}
    override = manual_path(source["id"])

    if override.exists():
        rows, diag = rows_from_csv(override.read_text(), column_map)
        diag["source"] = f"manual CSV {override.relative_to(REPO)}"
        # An operator exported this county's list by hand, so the aggregator
        # filter below must not run over it — a hand-exported Ellis list has no
        # reason to carry the word "Ellis" in any column, and filtering on one
        # silently drops every row.
        diag["manual"] = True
        if not rows:
            raise StructureChanged(str(override), f"manual CSV unusable: {diag.get('reason')}")
        return rows, diag

    fmt = source.get("format", "html_table")
    if fmt == "pdf":
        raise SourceError(url, (
            "this source publishes a PDF and the repo carries no PDF dependency. "
            f"Export it to CSV and drop it at {override.relative_to(REPO)} — the "
            f"column headers are matched by the source's column_map."))

    # A county that moves its list usually keeps publishing it somewhere; try
    # every known location before calling the source broken.
    attempts: list[str] = [u for u in [url, *(source.get("fallback_urls") or [])] if u]
    errors: list[str] = []
    for candidate in attempts:
        try:
            rows, diag = _read_source(candidate, source, fmt, column_map, cfg)
        except SourceError as exc:
            errors.append(f"{candidate} — {exc.detail}")
            continue
        diag["source"] = candidate
        if candidate != url:
            diag["via_fallback"] = candidate
        return rows, diag

    detail = errors[0] if len(errors) == 1 else (
        f"all {len(attempts)} configured locations failed:\n      "
        + "\n      ".join(errors))
    raise StructureChanged(url, detail)


def _read_source(url: str, source: dict, fmt: str, column_map: dict, cfg: dict
                 ) -> tuple[list[dict], dict]:
    text = fetch(url, cfg)

    markers = [m.lower() for m in source.get("required_markers") or []]
    low = text.lower()
    absent = [m for m in markers if m not in low]
    if absent:
        raise StructureChanged(url, (
            f"the page no longer contains {absent!r}, which config/tax_deeds.json "
            f"declares as its structural markers. The county changed the page; "
            f"update `required_markers` and `column_map` for source '{source['id']}'."))

    if fmt == "csv":
        rows, diag = rows_from_csv(text, column_map)
    elif fmt == "json":
        rows, diag = rows_from_json(text, source)
    elif fmt == "html_table":
        rows, diag = rows_from_tables(collect_tables(text), column_map)
        if not rows:
            # The page rendered its list client-side. Rather than fail with
            # advice to go read dev tools, look for the data the page shipped
            # with itself — see discover_json_records.
            found, found_diag = discover_json_records(text, source)
            found_diag["route"] = "embedded" if found else None

            # Rows are not the same thing as *our* rows. The embedded payload on
            # this vendor's page is the first chunk of a nationwide feed, so
            # discovery succeeded with 400 records and none of them were this
            # county's — and because it succeeded, the API route never ran, and
            # with it neither did the server-side narrowing that is the only way
            # to reach the rest of the feed. So "found, but none ours" has to
            # fall through exactly like "found nothing".
            if source.get("probe_api", True) and not _matches_county(found, source):
                api_rows, api_diag = discover_api_records(text, source, cfg, url)
                if api_rows and (_matches_county(api_rows, source) or not found):
                    api_diag["route"] = "api"
                    found, found_diag = api_rows, api_diag

            if found:
                found_diag["auto_discovered"] = True
                return found, found_diag
            diag["discovery"] = found_diag.get("reason")
    else:
        raise SourceError(url, f"unknown source format {fmt!r} for '{source['id']}'")

    if not rows:
        raise StructureChanged(url, _unparseable(source, diag))
    return rows, diag


def _unparseable(source: dict, diag: dict) -> str:
    """Why the page did not parse, and the fix that actually applies to it."""
    url, sid = source.get("url", ""), source["id"]
    if diag.get("no_tables"):
        return (
            f"this page contains no HTML table at all, so there is nothing for a table "
            f"parser to read and no `column_map` edit can fix it — the list is rendered by "
            f"JavaScript. Automatic discovery of the JSON the page ships with itself was "
            f"tried and found nothing ({diag.get('discovery', 'no candidates')}). Two ways "
            f"forward: open the page with the network tab, find the endpoint it calls, and "
            f"add it as a `\"format\": \"json\"` source (or as a `fallback_urls` entry) "
            f"for '{sid}'; or export the list by hand to "
            f"{manual_path(sid).relative_to(REPO)}.")
    discovery = f" Automatic JSON discovery also found nothing ({diag['discovery']})." \
        if diag.get("discovery") else ""
    return (
        f"could not read a sale list from this page: {diag.get('reason')}. "
        f"Headers seen: {diag.get('headers_seen') or diag.get('header_matched')}."
        f"{discovery} Update `column_map` for source '{sid}' in config/tax_deeds.json, "
        f"or export the list to {manual_path(sid).relative_to(REPO)}.")


def normalize_listing(raw: dict, county: str, source: dict, cfg: dict) -> dict:
    """One county row in the shape every gate downstream expects."""
    url = source.get("url", "")
    href = raw.get("_href") or ""
    if href and not href.startswith("http"):
        href = urllib.parse.urljoin(url, href)
    return {
        "county": county,
        "source_id": source["id"],
        "sale_type": source.get("sale_type", "auction"),
        "cause_number": (raw.get("cause_number") or "").strip(),
        "account": (raw.get("account") or "").strip(),
        "account_key": td.normalize_account(raw.get("account")),
        "address": (raw.get("address") or "").strip(),
        "legal_description": (raw.get("legal_description") or "").strip(),
        "property_type": (raw.get("property_type") or "").strip(),
        "owner_name": (raw.get("owner_name") or "").strip(),
        "minimum_opening_bid": td.parse_money(raw.get("minimum_opening_bid")),
        "adjudged_value": td.parse_money(raw.get("adjudged_value")),
        "sale_date": td.parse_date(raw.get("sale_date")),
        "status": (raw.get("status") or "").strip(),
        "precinct": (raw.get("precinct") or "").strip(),
        "listing_url": href or url,
        "fetched_at": td.now_iso(),
    }


def county_listings(county: dict, cfg: dict, sale_date: str | None = None
                    ) -> tuple[list[dict], list[dict]]:
    """Every listing this county publishes, plus a per-source report."""
    listings: list[dict] = []
    report: list[dict] = []

    for source in county.get("sources", []):
        entry = {"id": source["id"], "county": county["name"], "url": source.get("url", ""),
                 "sale_type": source.get("sale_type"), "ok": False, "rows": 0, "detail": ""}
        try:
            rows, diag = load_source(source, cfg)
        except SourceError as exc:
            entry["detail"] = exc.detail
            report.append(entry)
            continue

        filter_name = None if diag.get("manual") else source.get("county_filter")
        parsed: list[dict] = []
        dropped_county = dropped_date = 0
        dates_seen: set[str] = set()
        counties_seen: dict[str, int] = {}

        for raw in rows:
            listing = normalize_listing(raw, county["name"], source, cfg)
            # A cross-county aggregator returns every county it covers; keep
            # ours. Prefer an explicit county field, fall back to everything the
            # record held — mapped or not.
            if filter_name:
                if raw.get("county"):
                    counties_seen[str(raw["county"])[:40]] = \
                        counties_seen.get(str(raw["county"])[:40], 0) + 1
                # Both, not either: the mapped `county` field can hold a numeric
                # id rather than a name, and then the name is only findable in
                # the rest of the record.
                blob = " ".join(str(v) for v in (
                    raw.get("county"), raw.get("_blob"),
                    *(v for k, v in raw.items() if k != "_blob"))).lower()
                if filter_name.lower() not in blob and county["name"].lower() not in blob:
                    dropped_county += 1
                    continue
            if listing["sale_date"]:
                dates_seen.add(listing["sale_date"])
            if sale_date and listing["sale_date"] and listing["sale_date"] != sale_date:
                dropped_date += 1
                continue
            parsed.append(listing)

        listings.extend(parsed)
        # Say where the rows went. "Fetched 10, kept 0" was invisible before,
        # and it read exactly like a source that returned nothing at all.
        detail = (f"{diag.get('source')} · fetched {len(rows)}, kept {len(parsed)}"
                  f" · matched {diag.get('mapped')}")
        if diag.get("pages", 1) > 1:
            detail += f" · {diag['pages']} page(s)"
        if dropped_county:
            # Name what did come back. "400 not in Tarrant" leaves you unable to
            # tell a statewide feed from a county field holding a numeric id.
            top = sorted(counties_seen.items(), key=lambda kv: -kv[1])[:6]
            detail += (f" · {dropped_county} not in {filter_name}"
                       + (f" (saw {top})" if top else " (no county field in the records)"))
            if diag.get("narrowing_failed"):
                detail += (f" · could not narrow server-side, tried "
                           f"{diag['narrowing_failed']} — set `query_params` on this source "
                           f"to the key and value this API actually wants")
        if dropped_date:
            detail += (f" · {dropped_date} for another sale date "
                       f"(saw {sorted(dates_seen)[:6]}, wanted {sale_date})")
        entry.update(ok=True, rows=len(parsed), fetched=len(rows),
                     dropped_county=dropped_county, dropped_date=dropped_date,
                     sale_dates_seen=sorted(dates_seen)[:12], detail=detail)
        report.append(entry)
    return listings, report


# --------------------------------------------------------------------------
# CAD enrichment, cached by account number
# --------------------------------------------------------------------------

def _cache_path(cad_key: str, account: str) -> Path:
    return CACHE_DIR / "cad" / f"{cad_key}_{td.normalize_account(account) or 'unknown'}.json"


# Why a CAD lookup failed, kept per district for the run report. A silent None
# gave 664 identical `no_cad_match` rejections across two districts that turned
# out to have entirely different problems — Dallas was being throttled after
# ~94 requests, while Tarrant and Ellis matched nothing at all.
cad_failures: dict[str, dict[str, int]] = {}


def _note_cad_failure(cad_key: str, reason: str) -> None:
    cad_failures.setdefault(cad_key, {})
    cad_failures[cad_key][reason] = cad_failures[cad_key].get(reason, 0) + 1


def account_variants(account: str) -> list[str]:
    """The spellings a district might index this account under.

    Sale lists and appraisal rolls disagree about punctuation and leading
    zeros — `126-0002-0009` on a constable list is `12600020009` in the roll —
    so try the obvious re-spellings before concluding there is no such parcel.
    """
    raw = str(account or "").strip()
    if not raw:
        return []
    out = [raw]
    for candidate in (td.normalize_account(raw), raw.replace("-", ""),
                      raw.replace(" ", ""), raw.lstrip("0"),
                      td.normalize_account(raw).lstrip("0")):
        if candidate and candidate not in out:
            out.append(candidate)
    return out


def cad_record(cad_key: str, account: str, cfg: dict, *, use_cache: bool = True) -> dict | None:
    """The appraisal district record for one account, or None when unmatched.

    Tries each configured URL pattern against each plausible spelling of the
    account, stopping at the first page that yields an appraised value.
    """
    district = (cfg.get("appraisal_districts") or {}).get(cad_key)
    if not district or not account:
        return None

    path = _cache_path(cad_key, account)
    if use_cache and path.exists():
        try:
            cached = json.loads(path.read_text())
            fetched = datetime.fromisoformat(cached["fetched_at"])
            if datetime.now(fetched.tzinfo) - fetched < timedelta(days=CAD_CACHE_DAYS):
                return cached
        except (json.JSONDecodeError, KeyError, ValueError):
            pass

    patterns = [p for p in [district.get("account_url"),
                            *(district.get("account_url_fallbacks") or [])] if p]
    markers = [m.lower() for m in district.get("required_markers") or []]
    variants = account_variants(account)
    unreachable = False

    for pattern in patterns:
        for variant in variants:
            url = pattern.replace("{account}", urllib.parse.quote(str(variant)))
            try:
                html = fetch(url, cfg)
            except SourceError as exc:
                unreachable = True
                _note_cad_failure(cad_key, exc.detail[:80])
                continue
            if markers and not any(m in html.lower() for m in markers):
                _note_cad_failure(cad_key, f"page missing markers {markers!r}")
                continue
            record = parse_cad_record(html, district.get("field_map"))
            if not record.get("appraised_value"):
                # A page that renders but carries no value is a miss, not a
                # match — usually "account not found" served as a 200.
                _note_cad_failure(cad_key, "page rendered but carried no appraised value")
                continue

            record.update({"account": str(account), "account_key": td.normalize_account(account),
                           "cad": cad_key, "cad_url": url,
                           "source": district.get("name", cad_key),
                           "matched_as": variant, "fetched_at": td.now_iso()})
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
            return record

        if unreachable:
            # The district is refusing us, not missing this parcel. Trying more
            # spellings is just more requests at a host already saying no.
            break
    return None


# --------------------------------------------------------------------------
# Gate 2 checks
# --------------------------------------------------------------------------

def clerk_check(name: str, spec: dict, listing: dict, cfg: dict) -> dict:
    """Search county clerk records for one lien class against the owner name.

    These portals are session-gated and JavaScript-driven; none of the four
    counties publishes a keyless query endpoint. That is the honest answer this
    returns, and it is why the packet exists. Configure `query_url` on the
    source (a template taking {query} and {county}) the day one appears and
    this starts returning real results instead.
    """
    county = listing.get("county", "")
    base = (spec.get("urls") or {}).get(county) or (spec.get("urls") or {}).get("_all") or ""
    owner = listing.get("owner_name") or ""
    terms = spec.get("query_terms") or []

    if not base:
        return td.check_record(name, td.UNAVAILABLE, "not configured",
                               f"no clerk source configured for {county}")
    if not owner:
        return td.check_record(name, td.UNAVAILABLE, base,
                               "the county list published no owner name to search against")

    query_url = spec.get("query_url")
    if not query_url:
        return td.check_record(name, td.UNAVAILABLE, base, (
            "county clerk records are not machine-readable here — the portal needs an "
            "interactive session and publishes no keyless query endpoint. Search it by "
            "hand for the owner name before bidding."))

    url = (query_url.replace("{county}", urllib.parse.quote(county))
                    .replace("{query}", urllib.parse.quote(owner)))
    try:
        text = fetch(url, cfg)
    except SourceError as exc:
        return td.check_record(name, td.UNAVAILABLE, url, exc.detail)

    low = text.lower()
    hits = [term for term in terms if term.lower() in low]
    if hits:
        return td.check_record(name, td.HIT, url,
                               f"{', '.join(hits)} against owner {owner!r}")
    return td.check_record(name, td.CLEAN, url,
                           f"no {name.replace('_', ' ')} instrument matched owner {owner!r} "
                           f"in this index — an index search, not a title search")


def pace_check(spec: dict, listing: dict, cfg: dict) -> dict:
    """Texas PACE Authority project registry. Super-priority, so a hit rejects."""
    url = (spec.get("urls") or {}).get(listing.get("county")) or \
          (spec.get("urls") or {}).get("_all") or ""
    address = listing.get("address") or ""
    if not url:
        return td.check_record("pace_lien", td.UNAVAILABLE, "not configured",
                               "no PACE registry configured")
    if not address:
        return td.check_record("pace_lien", td.UNAVAILABLE, url,
                               "no address on the listing to match against the registry")
    try:
        text = fetch(url, cfg)
    except SourceError as exc:
        return td.check_record("pace_lien", td.UNAVAILABLE, url, exc.detail)

    street = _norm(address).split()
    needle = " ".join(street[:3]) if len(street) >= 3 else _norm(address)
    if needle and needle in _norm(text):
        return td.check_record("pace_lien", td.HIT, url,
                               f"address {address!r} appears in the PACE project registry")
    return td.check_record("pace_lien", td.CLEAN, url, (
        "not in the Texas PACE Authority published project registry — that registry only, "
        "not a county clerk lien search"))


def environmental_check(listing: dict, cad: dict | None, cfg: dict) -> dict:
    """Land-use and nearby-facility screen. A proximity flag, not a Phase I."""
    spec = cfg.get("environmental") or {}
    cad = cad or {}
    blob = " ".join(str(x or "") for x in (
        listing.get("property_type"), listing.get("legal_description"),
        cad.get("land_use_description"), cad.get("land_use_code"), cad.get("subdivision")))
    keywords = [k for k in spec.get("suspect_use_keywords", []) if k.lower() in blob.lower()]
    codes = [c for c in spec.get("suspect_land_use_codes", [])
             if _norm(c) and _norm(c) == _norm(cad.get("land_use_code", ""))]
    if keywords or codes:
        return td.check_record("environmental", td.HIT, "CAD land use", (
            f"land use suggests {', '.join(keywords + codes)} — gas station, dry cleaner, "
            f"auto repair or industrial history carries environmental lien risk"))

    zip_code = re.sub(r"[^0-9]", "", str(cad.get("zip") or ""))[:5]
    if not zip_code:
        match = re.search(r"\b(\d{5})(?:-\d{4})?\b", listing.get("address") or "")
        zip_code = match.group(1) if match else ""
    url = spec.get("url", "")
    if not url or not zip_code:
        return td.check_record("environmental", td.UNAVAILABLE, url or "not configured", (
            "CAD land use showed nothing and no ZIP was available for the facility "
            "screen; TCEQ has no keyless per-parcel endpoint — "
            f"{spec.get('manual_reference_url', '')}"))
    try:
        payload = fetch_json(url.replace("{zip}", zip_code), cfg)
    except SourceError as exc:
        return td.check_record("environmental", td.UNAVAILABLE, url, exc.detail)

    records = payload if isinstance(payload, list) else payload.get("Results") or []
    names = " ".join(str(r.get("PRIMARY_NAME", "")) for r in records if isinstance(r, dict))
    near = [k for k in spec.get("suspect_use_keywords", []) if k.lower() in names.lower()]
    if near:
        return td.check_record("environmental", td.HIT, url, (
            f"regulated facilities in ZIP {zip_code} matching {', '.join(sorted(set(near)))} — "
            f"ZIP-level proximity only; confirm the parcel and its neighbours on the ground"))
    return td.check_record("environmental", td.CLEAN, url, (
        f"CAD land use is not a suspect class and no matching regulated facility in ZIP "
        f"{zip_code} — a screen, not a Phase I assessment"))


# --------------------------------------------------------------------------
# Gate 3 checks
# --------------------------------------------------------------------------

def geocode(address: str, cfg: dict) -> tuple[float, float] | None:
    spec = cfg.get("geocoder") or {}
    url = spec.get("url")
    if not url or not address:
        return None
    try:
        payload = fetch_json(url, cfg, params={
            "address": address, "benchmark": spec.get("benchmark", "Public_AR_Current"),
            "format": "json"})
    except SourceError:
        return None
    matches = (((payload or {}).get("result") or {}).get("addressMatches") or [])
    if not matches:
        return None
    coords = matches[0].get("coordinates") or {}
    if coords.get("x") is None or coords.get("y") is None:
        return None
    return float(coords["x"]), float(coords["y"])


_flood_layer_cache: dict[str, str] = {}

# The layer index inside the NFHL MapServer is not stable across service
# revisions, and 28 was wrong on the first live run. An operator cannot guess
# the right one, so resolve it by name instead: ask the service what it
# publishes and take the flood-hazard-zone layer. Resolved once per run.
FLOOD_LAYER_NAMES = re.compile(r"flood\s*hazard\s*zone|flood\s*hazard\s*area|^s?_?fld_haz",
                               re.I)


def resolve_flood_url(spec: dict, cfg: dict) -> tuple[str, str]:
    """(url, note). Falls back to the configured URL when nothing better shows."""
    configured = spec.get("url", "")
    if not configured or not spec.get("autodetect_layer", True):
        return configured, ""
    if configured in _flood_layer_cache:
        resolved = _flood_layer_cache[configured]
        return resolved, ("" if resolved == configured else
                          f"auto-resolved the NFHL layer to {resolved}")

    payload = None
    for base in [configured, *(spec.get("url_fallbacks") or [])]:
        root = re.sub(r"/\d+/query/?$", "", base)
        if root == base:
            continue
        try:
            payload = fetch_json(root, cfg, params={"f": "json"})
        except SourceError:
            continue
        configured = base
        break
    if payload is None:
        _flood_layer_cache[spec.get("url", "")] = spec.get("url", "")
        return spec.get("url", ""), ""

    named = [(l.get("id"), str(l.get("name") or ""))
             for l in (payload.get("layers") or []) if l.get("id") is not None]
    match = next((i for i, name in named if FLOOD_LAYER_NAMES.search(name)), None)
    if match is None:
        match = next((i for i, name in named if re.search(r"flood", name, re.I)), None)
    resolved = f"{root}/{match}/query" if match is not None else configured
    _flood_layer_cache[configured] = resolved
    return resolved, ("" if resolved == configured else
                      f"auto-resolved the NFHL layer to id {match} "
                      f"({dict(named).get(match)})")


def flood_check(listing: dict, cad: dict | None, cfg: dict) -> dict:
    """FEMA National Flood Hazard Layer at the parcel's geocoded point."""
    spec = cfg.get("flood") or {}
    url, layer_note = resolve_flood_url(spec, cfg)
    address = listing.get("address") or (cad or {}).get("situs") or ""
    if not url:
        return td.check_record("flood_zone", td.UNAVAILABLE, "not configured",
                               "no FEMA NFHL endpoint configured")
    suffix = f" ({layer_note})" if layer_note else ""
    point = geocode(address, cfg)
    if point is None:
        return td.check_record("flood_zone", td.UNAVAILABLE, url,
                               f"could not geocode {address!r} to a point for the NFHL query")

    lon, lat = point
    try:
        payload = fetch_json(url, cfg, params={
            "geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint",
            "inSR": "4326", "spatialRel": "esriSpatialRelIntersects",
            "outFields": "FLD_ZONE,ZONE_SUBTY", "returnGeometry": "false", "f": "json"})
    except SourceError as exc:
        return td.check_record("flood_zone", td.UNAVAILABLE, url, exc.detail)

    zones = [str((f.get("attributes") or {}).get("FLD_ZONE") or "").upper()
             for f in (payload.get("features") or [])]
    high_risk = [z for z in zones if z in {s.upper() for s in spec.get("high_risk_zones", [])}]
    if high_risk:
        return td.check_record("flood_zone", td.HIT, url,
                               f"Zone {'/'.join(sorted(set(high_risk)))} at "
                               f"{lat:.5f},{lon:.5f}{suffix}")
    if not zones:
        return td.check_record("flood_zone", td.UNAVAILABLE, url,
                               "the NFHL returned no polygon at this point — the panel may "
                               "be unmapped; check the FEMA map service by hand")
    return td.check_record("flood_zone", td.CLEAN, url,
                           f"Zone {'/'.join(sorted(set(zones)))} at "
                           f"{lat:.5f},{lon:.5f}{suffix}")


def frontage_check(cad: dict | None) -> dict:
    """Road frontage, when the CAD record happens to publish it.

    None of the four districts exposes parcel geometry without their GIS
    portal, so this is usually unavailable — recorded as such, and shown in the
    sheet's Checks Unavailable column rather than inferred away.
    """
    cad = cad or {}
    frontage = cad.get("frontage")
    if frontage is None:
        return td.check_record("road_frontage", td.UNAVAILABLE, cad.get("cad_url", "CAD record"),
                               "the CAD record publishes no frontage; parcel geometry needs "
                               "the district GIS portal")
    if float(frontage) <= 0:
        return td.check_record("road_frontage", td.HIT, cad.get("cad_url", "CAD record"),
                               "frontage is zero on the CAD record — possibly landlocked")
    return td.check_record("road_frontage", td.CLEAN, cad.get("cad_url", "CAD record"),
                           f"{frontage:g} ft of frontage on the CAD record")


def lot_size_check(listing: dict, cad: dict | None, cfg: dict) -> dict:
    """Lot size against the municipality of record's minimum."""
    cad = cad or {}
    minimums = {k.upper(): v for k, v in (cfg.get("municipal_minimum_lot_sqft") or {}).items()
                if isinstance(v, (int, float))}
    address = (listing.get("address") or cad.get("situs") or "").upper()
    city = next((name for name in minimums if name and name in address), None)

    lot = cad.get("lot_sqft")
    if lot is None and cad.get("acres"):
        lot = float(cad["acres"]) * 43560
    if lot is None:
        return td.check_record("lot_size", td.UNAVAILABLE, cad.get("cad_url", "CAD record"),
                               "the CAD record publishes no lot size or acreage")
    if city is None:
        return td.check_record("lot_size", td.UNAVAILABLE, "config",
                               f"no municipal minimum configured for {address[:60]!r}; add the "
                               f"city to municipal_minimum_lot_sqft")
    if lot < minimums[city]:
        return td.check_record("lot_size", td.HIT, "config",
                               f"{lot:,.0f} sqft is below {city}'s {minimums[city]:,.0f} sqft "
                               f"minimum — likely unbuildable")
    return td.check_record("lot_size", td.CLEAN, "config",
                           f"{lot:,.0f} sqft clears {city}'s {minimums[city]:,.0f} sqft minimum")


def run_checks(listing: dict, cad: dict | None, cfg: dict) -> list[dict]:
    """Every check available, each recording checked_at, source and result."""
    liens = cfg.get("lien_sources") or {}
    checks: list[dict] = []

    for name in ("federal_tax_lien", "hoa_assessment", "municipal_lien"):
        spec = liens.get(name)
        if spec:
            checks.append(clerk_check(name, spec, listing, cfg))
        else:
            checks.append(td.check_record(name, td.UNAVAILABLE, "not configured",
                                          f"no {name} source in config/tax_deeds.json"))

    pace = liens.get("pace_lien")
    checks.append(pace_check(pace, listing, cfg) if pace else td.check_record(
        "pace_lien", td.UNAVAILABLE, "not configured", "no PACE source configured"))

    checks.append(environmental_check(listing, cad, cfg))
    checks.append(flood_check(listing, cad, cfg))
    checks.append(frontage_check(cad))
    checks.append(lot_size_check(listing, cad, cfg))
    return checks


# --------------------------------------------------------------------------
# verification
# --------------------------------------------------------------------------

def verify(cfg: dict) -> list[dict]:
    """Fetch every configured source and check it still looks like itself."""
    out: list[dict] = []

    for county in td.counties(cfg):
        for source in county.get("sources", []):
            entry = {"kind": "county list", "id": source["id"], "url": source.get("url", "")}
            try:
                rows, diag = load_source(source, cfg)
                detail = f"{len(rows)} row(s); mapped {diag.get('mapped')}"
                if diag.get("via_fallback"):
                    detail += f"; via fallback {diag['via_fallback']}"
                if diag.get("auto_discovered"):
                    # Worth surfacing loudly: the page had no table and the list
                    # was recovered from the JSON it ships with. Print what to
                    # pin so a working run stops depending on a heuristic.
                    detail += (f"; AUTO-DISCOVERED from embedded JSON at "
                               f"{diag.get('discovered_path')} — pin it with "
                               f"{json.dumps({'format': 'json', 'records_path': diag.get('discovered_path'), 'field_map': diag.get('discovered_field_map')})}")
                entry.update(ok=True, detail=detail)
            except SourceError as exc:
                entry.update(ok=False, detail=exc.detail)
            out.append(entry)

    for key, district in (cfg.get("appraisal_districts") or {}).items():
        url = district.get("search_url") or district.get("account_url", "")
        entry = {"kind": "appraisal district", "id": key, "url": url}
        try:
            html = fetch(url, cfg)
            markers = [m.lower() for m in district.get("required_markers") or []]
            absent = [m for m in markers if m not in html.lower()]
            entry.update(ok=not absent,
                         detail="reachable, markers present" if not absent
                         else f"missing markers {absent!r} — update required_markers/account_url")
        except SourceError as exc:
            entry.update(ok=False, detail=exc.detail)
        out.append(entry)

    for name, spec in (cfg.get("lien_sources") or {}).items():
        if not isinstance(spec, dict) or not spec.get("urls"):
            continue
        for county_name, url in spec["urls"].items():
            entry = {"kind": f"lien: {name}", "id": f"{name}/{county_name}", "url": url or ""}
            if not url:
                # A deliberate null: the URL that was here turned out not to
                # exist. Reported as unconfigured rather than as a failure,
                # because there is nothing broken to fix — something has to be
                # found. The check itself already reports `unavailable`, which
                # is a flag, so this cannot be mistaken for a clean screen.
                entry.update(ok=True, detail=(
                    "no source configured — this check reports unavailable, which is a flag. "
                    + str(spec.get("_ellis") or spec.get("_verified") or "")[:200]))
                out.append(entry)
                continue
            try:
                fetch(url, cfg)
                entry.update(ok=True, detail="reachable" + (
                    "" if spec.get("query_url") else
                    " — but no query_url configured, so this check reports unavailable"))
            except SourceError as exc:
                entry.update(ok=False, detail=exc.detail)
            out.append(entry)

    out.extend(_verify_enrichment(cfg))
    return out


# A probe has to exercise the call the screener actually makes. The first live
# run failed the Census geocoder and the FEMA layer for reasons that were
# entirely this function's fault: it fetched both bare, and an endpoint that
# requires query parameters answers a bare GET with 400 or 404. A verifier that
# invents its own failures is worse than no verifier, because it buries the real
# ones in noise.
PROBE_ADDRESS = "500 Elm St, Dallas, TX 75202"
PROBE_POINT = (-96.7970, 32.7767)   # lon, lat — Dallas County courthouse block


def _verify_enrichment(cfg: dict) -> list[dict]:
    out: list[dict] = []

    spec = cfg.get("geocoder") or {}
    if spec.get("url"):
        entry = {"kind": "geocoder", "id": "geocoder", "url": spec["url"]}
        try:
            payload = fetch_json(spec["url"], cfg, params={
                "address": PROBE_ADDRESS,
                "benchmark": spec.get("benchmark", "Public_AR_Current"), "format": "json"})
            matches = ((payload.get("result") or {}).get("addressMatches") or [])
            entry.update(ok=bool(matches),
                         detail=f"geocoded the probe address to "
                                f"{(matches[0].get('coordinates') or {})}" if matches
                         else "reachable, but it geocoded nothing for a known-good address "
                              "— the benchmark may be wrong")
        except SourceError as exc:
            entry.update(ok=False, detail=exc.detail)
        out.append(entry)

    spec = cfg.get("flood") or {}
    if spec.get("url"):
        out.append(_verify_flood(spec, cfg))

    spec = cfg.get("environmental") or {}
    if spec.get("url"):
        url = spec["url"].replace("{zip}", "75202")
        entry = {"kind": "environmental", "id": "environmental", "url": url}
        try:
            payload = fetch_json(url, cfg)
            count = len(payload if isinstance(payload, list)
                        else payload.get("Results") or [])
            entry.update(ok=True, detail=f"reachable, {count} facility record(s) for the "
                                         f"probe ZIP")
        except SourceError as exc:
            entry.update(ok=False, detail=exc.detail)
        out.append(entry)
    return out


def _verify_flood(spec: dict, cfg: dict) -> dict:
    """Probe the NFHL with a real point, and name the layers when it 404s.

    A wrong layer index is the likely reason this fails, and the operator
    cannot guess the right one — so when the query path is missing, ask the
    MapServer for its own layer list and print the candidates.
    """
    url, layer_note = resolve_flood_url(spec, cfg)
    entry = {"kind": "flood", "id": "flood", "url": url}
    lon, lat = PROBE_POINT
    try:
        payload = fetch_json(url, cfg, params={
            "geometry": f"{lon},{lat}", "geometryType": "esriGeometryPoint", "inSR": "4326",
            "spatialRel": "esriSpatialRelIntersects", "outFields": "FLD_ZONE",
            "returnGeometry": "false", "f": "json"})
    except SourceError as exc:
        entry.update(ok=False, detail=f"{exc.detail} {_flood_layer_hint(url, cfg)}".strip())
        return entry

    if isinstance(payload, dict) and payload.get("error"):
        message = (payload["error"] or {}).get("message", "unknown ArcGIS error")
        entry.update(ok=False,
                     detail=f"the service answered with an error: {message}. "
                            f"{_flood_layer_hint(url, cfg)}".strip())
        return entry
    fields = [f.get("name") for f in (payload.get("fields") or [])]
    entry.update(ok="FLD_ZONE" in fields or bool(payload.get("features")) or fields == [],
                 detail=f"queried the probe point; "
                        f"{len(payload.get('features') or [])} zone polygon(s), "
                        f"fields {fields[:6]}. {layer_note}".strip())
    return entry


def _flood_layer_hint(url: str, cfg: dict) -> str:
    """Ask the MapServer which layers it has, so a wrong index is fixable."""
    root = re.sub(r"/\d+/query/?$", "", url)
    if root == url:
        return ""
    try:
        payload = fetch_json(root, cfg, params={"f": "json"})
    except SourceError as exc:
        return f"(could not list the service's layers either: {exc.detail})"
    layers = [(l.get("id"), l.get("name")) for l in (payload.get("layers") or [])]
    flood = [f"{i}={n}" for i, n in layers if n and re.search(r"flood|hazard|zone", n, re.I)]
    if flood:
        return (f"The service does publish layers that look right — set the index in "
                f"`flood.url` to one of: {', '.join(flood)}.")
    return f"The service lists {len(layers)} layer(s): {layers[:12]}"


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("verify")
    listings = sub.add_parser("listings")
    listings.add_argument("county")
    cad = sub.add_parser("cad")
    cad.add_argument("district")
    cad.add_argument("account")
    args = ap.parse_args(argv)

    cfg = td.load_config()

    if args.command == "verify":
        rows = verify(cfg)
        print("| Source | Kind | Status | Detail |")
        print("| --- | --- | --- | --- |")
        for row in rows:
            print(f"| `{row['id']}` | {row['kind']} | {'✅' if row['ok'] else '🔴'} "
                  f"| {row['detail'][:220]} |")
        broken = [r for r in rows if not r["ok"]]
        print(f"\n**{len(rows) - len(broken)} of {len(rows)} sources verified.**")
        for row in broken:
            print(f"\n🔴 `{row['id']}` — {row['url']}\n    {row['detail']}")
        return 1 if broken else 0

    if args.command == "listings":
        county = next((c for c in td.counties(cfg) if c["name"].lower() == args.county.lower()),
                      None)
        if not county:
            raise SystemExit(f"{args.county} is not configured")
        rows, report = county_listings(county, cfg)
        print(json.dumps({"listings": rows, "sources": report}, indent=2))
        return 0

    record = cad_record(args.district, args.account, cfg)
    print(json.dumps(record, indent=2) if record else "no CAD match")
    return 0 if record else 1


if __name__ == "__main__":
    raise SystemExit(main())
