#!/usr/bin/env python3
"""Find out why an appraisal district lookup misses, one account at a time.

    python scripts/tax_deed_cad_probe.py                      # every district, 3 accounts each
    python scripts/tax_deed_cad_probe.py --district DCAD
    python scripts/tax_deed_cad_probe.py --district TAD --account 00069590
    python scripts/tax_deed_cad_probe.py --json reports/tax_deeds/cad_probe.json

The CAD lookup has never matched a property — 0 of 370, 1,185, 1,207 and 1,209
listings across every live run there has been — and the run summary can only
say which of `cad_record`'s exits was taken:

    DCAD — page rendered but carried no appraised value ×21;
           the district's own search returned no detail link ×12

That is not enough to fix anything. "Carried no appraised value" is true of a
page whose value is rendered by JavaScript, a page whose labels are worded
differently from `CAD_FIELDS`, and a page that says "account not found" — three
unrelated problems with three unrelated fixes, and guessing between them is how
the config accumulated URL patterns that were never right.

So this asks the question the screener cannot: it fetches the same URLs the
screener fetches, and then reports **what was in the response**. Chiefly one
distinction, because it decides everything downstream:

  * money in the HTML, none of it parsed  -> a label-wording problem, and the
    labels that *are* on the page are printed so `field_map` can be fixed.
  * no money in the HTML at all           -> the page renders client-side, and
    the fix is the endpoint it calls for itself, the same shape of fix
    `rows_from_json` already is for county lists.

It is read-only and deliberately small. It writes no cache entry, records no
miss against the district's give-up counter, and touches neither the snapshot
nor the Sheet — running it can change no screening result. Accounts come from
the newest snapshot, so they are accounts a real run really did try.

Manners are the module's: robots.txt is honoured, one request per second per
host, and `TAX_DEED_CONTACT_EMAIL` is required, same as everywhere else.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import tax_deeds as td  # noqa: E402
import tax_deed_sources as src  # noqa: E402

DEFAULT_ACCOUNTS = 3

# Enough to tell "this page has numbers on it" from "this page is a shell", and
# no more. A CAD detail page states a value in dollars; a JavaScript shell
# states none because the value has not arrived yet.
_MONEY = re.compile(r"\$\s?\d[\d,]{2,}|\b\d{1,3}(?:,\d{3})+(?:\.\d\d)?\b")

# A page that loaded and told us there is no such account is a *correct*
# answer, and must never be filed as a parser failure — that conflation is
# what put three different problems under one summary line.
_NOT_FOUND = re.compile(
    r"no\s+(?:record|result|match|propert|account)|not\s+found|0\s+result|"
    r"no\s+data\s+(?:found|available)|invalid\s+account", re.I)


# --------------------------------------------------------------------------
# verdicts
# --------------------------------------------------------------------------

ROBOTS = "robots_disallowed"
UNREACHABLE = "host_unreachable"
NOT_FOUND = "account_not_found"
JAVASCRIPT = "page_renders_client_side"
WORDING = "label_wording"
MARKERS = "markers_absent"
MATCHED = "matched"

# Ordered worst-to-best, so a district's verdict is the best outcome any of its
# attempts reached rather than whichever happened to run last.
VERDICT_ORDER = [ROBOTS, UNREACHABLE, MARKERS, NOT_FOUND, JAVASCRIPT, WORDING, MATCHED]

FIXES = {
    ROBOTS: "The district disallows this path. That is policy, it is honoured, "
            "and there is no config that changes it — the same line the clerk "
            "portals sit behind.",
    UNREACHABLE: "Nothing was served. Resolve the host before configuring it: "
                 "three hostnames in this config once pointed nowhere and "
                 "reported a transient-looking network error every run.",
    MARKERS: "The page loaded but carries none of the district's "
             "`required_markers`, so the screener discards it before parsing. "
             "Either the markers are stale or the URL pattern reaches the "
             "wrong page.",
    NOT_FOUND: "The district answered, and its answer is that it has no such "
               "account. That is a working lookup against a spelling it does "
               "not index — try `account_variants`, or the county list's "
               "account numbers are from a different system than the roll.",
    JAVASCRIPT: "No money anywhere in the HTML: the page renders its values "
                "client-side, so no `field_map` wording can ever match. Fix is "
                "the endpoint the page calls for itself — the same shape of fix "
                "`rows_from_json` is for county lists. Candidate URLs, and any "
                "embedded JSON carrying a value, are listed per attempt below.",
    WORDING: "The value is in the HTML and `parse_cad_record` did not take it. "
             "This is a `field_map` fix and nothing more: the money-bearing "
             "labels actually on the page are listed per attempt below. Add "
             "them to the district's `field_map` in config/tax_deeds.json.",
    MATCHED: "The lookup works. Nothing to fix here.",
}


def best(verdicts: list[str]) -> str:
    """The furthest any attempt got. Absent evidence, the host is unreachable."""
    ranked = [v for v in VERDICT_ORDER if v in verdicts]
    return ranked[-1] if ranked else UNREACHABLE


# --------------------------------------------------------------------------
# one fetch, fully described
# --------------------------------------------------------------------------

def money_labels(html: str, limit: int = 12) -> list[str]:
    """The `label: value` pairs on this page whose value looks like money.

    This is the whole point of the probe in the label-wording case: it is the
    list of wordings to paste into `field_map`, taken from the page rather than
    guessed at.
    """
    out: list[str] = []
    for label, value in src.label_values(html):
        if not _MONEY.search(value or ""):
            continue
        entry = f"{label.strip()[:60]} = {value.strip()[:30]}"
        if entry not in out:
            out.append(entry)
        if len(out) >= limit:
            break
    return out


def json_with_values(html: str, limit: int = 6) -> list[str]:
    """Keys in the page's own embedded JSON that look like a value.

    When a page renders client-side it often still ships its data inline, which
    is what `discover_json_records` already exploits for county lists. If that
    is the case here, the fix is a config change rather than a parser.
    """
    wanted = re.compile(r"value|apprais|market|assess|land|improve", re.I)
    found: list[str] = []

    def walk(node: Any, path: str = "", depth: int = 0) -> None:
        if len(found) >= limit or depth > 6:
            return
        if isinstance(node, dict):
            for key, value in node.items():
                walk(value, f"{path}.{key}" if path else str(key), depth + 1)
        elif isinstance(node, list):
            for value in node[:20]:
                walk(value, path, depth + 1)
        elif path and wanted.search(path) and str(node).strip():
            entry = f"{path} = {str(node)[:30]}"
            if entry not in found:
                found.append(entry)

    for payload in src.embedded_json(html):
        walk(payload)
    return found


def probe_url(url: str, district: dict, cfg: dict) -> dict:
    """Fetch one URL and say everything the screener's exits leave out."""
    attempt: dict[str, Any] = {"url": url}
    try:
        html = src.fetch(url, cfg)
    except src.RobotsDisallowed as exc:
        return {**attempt, "verdict": ROBOTS, "detail": exc.detail}
    except src.SourceError as exc:
        return {**attempt, "verdict": UNREACHABLE, "detail": exc.detail}

    attempt["bytes"] = len(html)
    markers = [m.lower() for m in district.get("required_markers") or []]
    present = [m for m in markers if m in html.lower()]
    attempt["markers_present"] = present
    attempt["markers_absent"] = [m for m in markers if m not in present]

    record = src.parse_cad_record(html, district.get("field_map"))
    attempt["parsed"] = {k: v for k, v in record.items() if v not in (None, "", [])}

    if record.get("appraised_value"):
        attempt["verdict"] = MATCHED
        return attempt

    # Order matters. A page missing its markers was never going to be parsed,
    # so say that rather than diagnosing the parse that never happened.
    if markers and not present:
        attempt["verdict"] = MARKERS
        return attempt

    labels = money_labels(html)
    attempt["money_labels"] = labels
    attempt["money_in_html"] = bool(_MONEY.search(html))

    if labels or attempt["money_in_html"]:
        # A "no such account" page can still carry money in a footer or a
        # sidebar, so check what the page says before blaming the field map.
        attempt["verdict"] = NOT_FOUND if _NOT_FOUND.search(html) and not labels else WORDING
        return attempt

    attempt["verdict"] = NOT_FOUND if _NOT_FOUND.search(html) else JAVASCRIPT
    if attempt["verdict"] == JAVASCRIPT:
        attempt["embedded_json"] = json_with_values(html)
        attempt["api_candidates"] = src.candidate_api_urls(html, url)[:5]
    return attempt


def probe_search(cad_key: str, district: dict, account: str, cfg: dict) -> dict:
    """The district's own search box, and what it gave back.

    `cad_search` returns a link or None, and None covers "the search refused",
    "it answered with no results" and "it answered with links we rejected".
    This reports which, because only the third is a code fix.
    """
    search = district.get("search_url")
    if not search:
        return {"searched": False, "why": "no search_url configured"}

    out: dict[str, Any] = {"searched": True, "url": search, "params_tried": []}
    for param in src.CAD_SEARCH_PARAMS:
        entry: dict[str, Any] = {"param": param}
        try:
            html = src.fetch(search, cfg, params={param: account})
        except src.SourceError as exc:
            entry["error"] = exc.detail[:120]
            out["params_tried"].append(entry)
            continue

        hrefs = [urllib.parse.urljoin(search, h) for h in src._DETAIL_HREF.findall(html)]
        detail = [h for h in hrefs if src._DETAIL_PATH.search(h)]
        same_host = [h for h in detail
                     if urllib.parse.urlsplit(h).netloc == urllib.parse.urlsplit(search).netloc]
        tail = td.normalize_account(account)[-6:]
        # The account-tail rule is what `cad_search` rejects links on, so
        # report it separately: links that look right but fail this one test
        # are a different problem from a search that returned nothing.
        matching = [h for h in same_host if tail and tail in td.normalize_account(h)]
        entry.update({"bytes": len(html), "detail_links": len(detail),
                      "same_host": len(same_host), "account_in_link": len(matching),
                      "sample": (matching or same_host or detail)[:3]})
        out["params_tried"].append(entry)
        if matching:
            out["followed"] = matching[0]
            out["detail"] = probe_url(matching[0], district, cfg)
            break
    return out


# --------------------------------------------------------------------------
# accounts to probe
# --------------------------------------------------------------------------

def sample_accounts(county: str, limit: int) -> list[str]:
    """Real accounts a real run tried, newest snapshot first.

    Made-up account numbers would prove nothing: half the plausible failures
    are about which spelling the roll indexes, and only the county's own
    listings carry that.
    """
    snapshots = sorted(td.SNAPSHOT_DIR.glob("*.json"), reverse=True)
    for path in snapshots:
        try:
            results = json.loads(path.read_text()).get("results") or []
        except (json.JSONDecodeError, OSError):
            continue
        seen: list[str] = []
        for result in results:
            listing = result.get("listing") or {}
            if listing.get("county") != county:
                continue
            account = str(listing.get("account") or "").strip()
            if account and account not in seen:
                seen.append(account)
            if len(seen) >= limit:
                return seen
        if seen:
            return seen
    return []


def probe_district(cad_key: str, county: str, cfg: dict, accounts: list[str]) -> dict:
    district = (cfg.get("appraisal_districts") or {}).get(cad_key) or {}
    out: dict[str, Any] = {"district": cad_key, "county": county,
                           "name": district.get("name", cad_key),
                           "configured": bool(district), "accounts": []}
    if not district:
        out["verdict"] = UNREACHABLE
        out["note"] = f"no appraisal_districts entry named {cad_key!r}"
        return out
    if not accounts:
        out["verdict"] = UNREACHABLE
        out["note"] = ("no accounts for this county in any snapshot — run the "
                       "screener once, or pass --account")
        return out

    patterns = [p for p in [district.get("account_url"),
                            *(district.get("account_url_fallbacks") or [])] if p]
    verdicts: list[str] = []

    for account in accounts:
        entry: dict[str, Any] = {"account": account, "attempts": []}
        for pattern in patterns:
            for variant in src.account_variants(account):
                url = pattern.replace("{account}", urllib.parse.quote(str(variant)))
                attempt = probe_url(url, district, cfg)
                attempt["variant"] = variant
                entry["attempts"].append(attempt)
                verdicts.append(attempt["verdict"])
                if attempt["verdict"] == MATCHED:
                    break
            if entry["attempts"] and entry["attempts"][-1]["verdict"] == MATCHED:
                break

        if not any(a["verdict"] == MATCHED for a in entry["attempts"]):
            entry["search"] = probe_search(cad_key, district, account, cfg)
            if (found := entry["search"].get("detail")):
                verdicts.append(found["verdict"])
        out["accounts"].append(entry)

    out["verdict"] = best(verdicts)
    return out


# --------------------------------------------------------------------------
# report
# --------------------------------------------------------------------------

def render(report: list[dict]) -> list[str]:
    out = ["## Appraisal district probe", "",
           "What each district actually served, for accounts taken from the newest "
           "snapshot. Read-only: no cache written, no miss recorded, no snapshot or "
           "Sheet touched.", "",
           "| District | County | Verdict |", "| --- | --- | --- |"]
    for entry in report:
        out.append(f"| `{entry['district']}` | {entry['county']} | **{entry['verdict']}** |")

    for entry in report:
        out += ["", f"### {entry['name']} (`{entry['district']}`) — {entry['verdict']}", "",
                FIXES.get(entry["verdict"], "")]
        if entry.get("note"):
            out += ["", f"> {entry['note']}"]

        for account in entry.get("accounts", []):
            out += ["", f"**Account `{account['account']}`**", ""]
            for attempt in account["attempts"]:
                line = f"- `{attempt['verdict']}` — {attempt['url']}"
                if attempt.get("bytes") is not None:
                    line += f" ({attempt['bytes']:,} bytes)"
                if attempt.get("detail"):
                    line += f"\n  - {attempt['detail'][:160]}"
                if attempt.get("markers_absent"):
                    line += f"\n  - markers absent: {attempt['markers_absent']}"
                if attempt.get("parsed"):
                    line += f"\n  - parsed: {json.dumps(attempt['parsed'])[:200]}"
                for label in attempt.get("money_labels") or []:
                    line += f"\n  - money label on the page: `{label}`"
                for key in attempt.get("embedded_json") or []:
                    line += f"\n  - embedded JSON: `{key}`"
                for url in attempt.get("api_candidates") or []:
                    line += f"\n  - endpoint the page calls: {url}"
                out.append(line)

            search = account.get("search")
            if not search:
                continue
            if not search.get("searched"):
                out.append(f"- search: {search.get('why')}")
                continue
            out.append(f"- search: {search['url']}")
            for tried in search.get("params_tried", []):
                if tried.get("error"):
                    out.append(f"  - `{tried['param']}` — {tried['error']}")
                    continue
                out.append(f"  - `{tried['param']}` — {tried['bytes']:,} bytes, "
                           f"{tried['detail_links']} detail link(s), "
                           f"{tried['same_host']} on this host, "
                           f"{tried['account_in_link']} naming the account")
                for sample in tried.get("sample", []):
                    out.append(f"    - {sample}")
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--district", action="append",
                    help="limit to this CAD key (DCAD/TAD/JohnsonCAD/EllisCAD); repeatable")
    ap.add_argument("--account", action="append",
                    help="probe this account instead of sampling; repeatable")
    ap.add_argument("--accounts", type=int, default=DEFAULT_ACCOUNTS,
                    help=f"accounts to sample per district (default {DEFAULT_ACCOUNTS})")
    ap.add_argument("--json", type=Path, help="also write the full findings here")
    ap.add_argument("--config", type=Path, help="alternate config/tax_deeds.json")
    args = ap.parse_args(argv)

    cfg = td.load_config(args.config)
    wanted = {d.lower() for d in args.district} if args.district else None

    report: list[dict] = []
    for county in td.counties(cfg):
        cad_key = county.get("cad") or ""
        if wanted and cad_key.lower() not in wanted:
            continue
        accounts = args.account or sample_accounts(county["name"], max(1, args.accounts))
        report.append(probe_district(cad_key, county["name"], cfg, accounts))

    if not report:
        print("No district matched. Configured: "
              + ", ".join(sorted((cfg.get("appraisal_districts") or {}))), file=sys.stderr)
        return 2

    lines = render(report)
    print("\n".join(lines))
    if (step_summary := os.environ.get("GITHUB_STEP_SUMMARY")):
        with open(step_summary, "a", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + "\n")
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
        print(f"\nFull findings -> {args.json}", file=sys.stderr)

    # A probe reports; it does not pass or fail. The one exception is a probe
    # that could not ask anything at all, which is a broken probe rather than a
    # finding about any district.
    reached = [e for e in report if e["verdict"] != UNREACHABLE or e.get("accounts")]
    return 0 if reached else 2


if __name__ == "__main__":
    raise SystemExit(main())
