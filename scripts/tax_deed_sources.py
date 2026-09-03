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
_robots: dict[str, Any] = {}


def user_agent(cfg: dict) -> str:
    """A descriptive UA with a contact email, or a refusal to fetch at all.

    County IT desks block anonymous crawlers and they are right to. If nobody
    can email us to say stop, we do not get to fetch.
    """
    contact = (os.environ.get("TAX_DEED_CONTACT_EMAIL") or cfg.get("contact_email") or "").strip()
    if not contact:
        raise SystemExit(
            "No contact email configured. Set TAX_DEED_CONTACT_EMAIL, or "
            "`contact_email` in config/tax_deeds.json. The screener will not "
            "make anonymous requests to county servers.")
    template = cfg.get("user_agent") or "invest-trade-daily-taxdeeds/1.0 ({contact})"
    return template.replace("{contact}", contact)


def session(cfg: dict):
    global _session
    if _session is None:
        import requests  # lazy: keeps this module importable on a bare runner
        _session = requests.Session()
        _session.headers.update({"User-Agent": user_agent(cfg),
                                 "Accept": "text/html,application/json;q=0.9,*/*;q=0.8"})
    return _session


def _throttle(url: str, cfg: dict) -> None:
    interval = float(cfg.get("request_interval_seconds") or 1.0)
    host = urllib.parse.urlsplit(url).netloc
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
        try:
            _throttle(root, cfg)
            resp = session(cfg).get(f"{root}/robots.txt", timeout=TIMEOUT)
            if resp.status_code >= 500:
                _robots[root] = None
            else:
                parser.parse(resp.text.splitlines() if resp.status_code < 400 else [])
                _robots[root] = parser
        except Exception as exc:  # noqa: BLE001
            _robots[root] = None
            _robots[f"{root}!why"] = f"{type(exc).__name__}: {exc}"

    parser = _robots.get(root)
    if parser is None:
        why = _robots.get(f"{root}!why", "robots.txt returned a server error")
        return False, f"could not read {root}/robots.txt ({why}) — not fetching"
    agent = user_agent(cfg).split("/")[0]
    if parser.can_fetch(agent, url) or parser.can_fetch("*", url):
        return True, "allowed by robots.txt"
    return False, f"{root}/robots.txt disallows this path for {agent}"


def fetch(url: str, cfg: dict, *, params: dict | None = None) -> str:
    """One polite GET. Raises SourceError with the URL on any failure."""
    allowed, why = robots_allows(url, cfg)
    if not allowed:
        raise RobotsDisallowed(url, why)
    _throttle(url, cfg)
    try:
        resp = session(cfg).get(url, params=params, timeout=TIMEOUT)
        resp.raise_for_status()
    except SourceError:
        raise
    except Exception as exc:  # noqa: BLE001
        raise SourceError(url, f"{type(exc).__name__}: {exc}") from exc
    return resp.text


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
        return [], {"reason": "no table with a header row and at least one data row",
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
    elif fmt == "html_table":
        rows, diag = rows_from_tables(collect_tables(text), column_map)
    else:
        raise SourceError(url, f"unknown source format {fmt!r} for '{source['id']}'")

    if not rows:
        raise StructureChanged(url, (
            f"could not read a sale list from this page: {diag.get('reason')}. "
            f"Headers seen: {diag.get('headers_seen') or diag.get('header_matched')}. "
            f"Update `column_map` for source '{source['id']}' in config/tax_deeds.json."))
    diag["source"] = url
    return rows, diag


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
        parsed = []
        for raw in rows:
            listing = normalize_listing(raw, county["name"], source, cfg)
            # A cross-county aggregator returns every county it covers; keep ours.
            if filter_name:
                blob = " ".join(str(v) for v in raw.values()).lower()
                if filter_name.lower() not in blob and county["name"].lower() not in blob:
                    continue
            if sale_date and listing["sale_date"] and listing["sale_date"] != sale_date:
                continue
            parsed.append(listing)

        listings.extend(parsed)
        entry.update(ok=True, rows=len(parsed),
                     detail=f"{diag.get('source')} · matched {diag.get('mapped')}")
        report.append(entry)
    return listings, report


# --------------------------------------------------------------------------
# CAD enrichment, cached by account number
# --------------------------------------------------------------------------

def _cache_path(cad_key: str, account: str) -> Path:
    return CACHE_DIR / "cad" / f"{cad_key}_{td.normalize_account(account) or 'unknown'}.json"


def cad_record(cad_key: str, account: str, cfg: dict, *, use_cache: bool = True) -> dict | None:
    """The appraisal district record for one account, or None when unmatched."""
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

    url = district["account_url"].replace("{account}", urllib.parse.quote(str(account)))
    try:
        html = fetch(url, cfg)
    except SourceError:
        return None

    markers = [m.lower() for m in district.get("required_markers") or []]
    if markers and not any(m in html.lower() for m in markers):
        raise StructureChanged(url, (
            f"the {cad_key} account page no longer contains any of {markers!r}. "
            f"Update `required_markers` / `account_url` for {cad_key}."))

    record = parse_cad_record(html, district.get("field_map"))
    if not record.get("appraised_value"):
        return None  # a page that renders but carries no value is not a match

    record.update({"account": str(account), "account_key": td.normalize_account(account),
                   "cad": cad_key, "cad_url": url, "source": district.get("name", cad_key),
                   "fetched_at": td.now_iso()})
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    return record


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


def flood_check(listing: dict, cad: dict | None, cfg: dict) -> dict:
    """FEMA National Flood Hazard Layer at the parcel's geocoded point."""
    spec = cfg.get("flood") or {}
    url = spec.get("url", "")
    address = listing.get("address") or (cad or {}).get("situs") or ""
    if not url:
        return td.check_record("flood_zone", td.UNAVAILABLE, "not configured",
                               "no FEMA NFHL endpoint configured")
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
                               f"Zone {'/'.join(sorted(set(high_risk)))} at {lat:.5f},{lon:.5f}")
    if not zones:
        return td.check_record("flood_zone", td.UNAVAILABLE, url,
                               "the NFHL returned no polygon at this point — the panel may "
                               "be unmapped; check the FEMA map service by hand")
    return td.check_record("flood_zone", td.CLEAN, url,
                           f"Zone {'/'.join(sorted(set(zones)))} at {lat:.5f},{lon:.5f}")


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
                entry.update(ok=True, detail=f"{len(rows)} row(s); mapped {diag.get('mapped')}")
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
            entry = {"kind": f"lien: {name}", "id": f"{name}/{county_name}", "url": url}
            try:
                fetch(url, cfg)
                entry.update(ok=True, detail="reachable" + (
                    "" if spec.get("query_url") else
                    " — but no query_url configured, so this check reports unavailable"))
            except SourceError as exc:
                entry.update(ok=False, detail=exc.detail)
            out.append(entry)

    for key in ("flood", "environmental", "geocoder"):
        spec = cfg.get(key) or {}
        url = spec.get("url", "")
        if not url:
            continue
        probe = url.replace("{zip}", "75202")
        entry = {"kind": key, "id": key, "url": probe}
        try:
            fetch(probe, cfg, params={"f": "json"} if key == "flood" else None)
            entry.update(ok=True, detail="reachable")
        except SourceError as exc:
            entry.update(ok=False, detail=exc.detail)
        out.append(entry)
    return out


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
