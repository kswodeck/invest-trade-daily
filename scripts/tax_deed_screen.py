#!/usr/bin/env python3
"""Screen the Texas tax deed sales and publish the shortlist.

    python scripts/tax_deed_screen.py                       # next first-Tuesday sale
    python scripts/tax_deed_screen.py --dry-run             # print everything, touch no Sheet
    python scripts/tax_deed_screen.py --sale-date 2026-10-06 --county Dallas
    python scripts/tax_deed_screen.py --no-verify           # skip the source structure check

Three outputs, in this order, because each is worth having even if the next
step fails:

  data/tax_deeds/<screened>.json          the run's full snapshot, every listing
  reports/tax_deeds/<sale>/<county>_<acct>.md   a packet per Tier A/B candidate
  Google Sheet tab `Tax Deeds`            rewritten in full, existing tabs untouched

THIS TOOL DOES NOT CERTIFY TITLE. Every row it emits is a candidate requiring a
professional title search before a bid. See `scripts/tax_deeds.py`.

Credentials are the daily report's: GCP_SERVICE_ACCOUNT_JSON and GOOGLE_SHEET_ID.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import tax_deeds as td  # noqa: E402

ET = ZoneInfo("America/New_York")
TAB_TITLE = "Tax Deeds"

# Tier colors, reused from the daily report's palette so the workbook reads as
# one document. Sheets colors are 0..1 floats.
TIER_BG = {
    "A": {"red": 0.85, "green": 0.94, "blue": 0.86},
    "B": {"red": 1.0, "green": 0.95, "blue": 0.80},
    "C": {"red": 0.95, "green": 0.95, "blue": 0.96},
}
HEADER_BG = {"red": 0.16, "green": 0.19, "blue": 0.27}
BANNER_BG = {"red": 0.90, "green": 0.91, "blue": 0.94}
WARN_BG = {"red": 0.98, "green": 0.87, "blue": 0.87}
INK = {"red": 0.13, "green": 0.13, "blue": 0.15}
WHITE = {"red": 1.0, "green": 1.0, "blue": 1.0}


def rel(path: Path) -> str:
    """Repo-relative when it is under the repo, absolute otherwise.

    The output directories are module constants the tests redirect to a temp
    dir, and `relative_to` raises rather than falling back on a path outside
    the repo — which turned a passing dry run into a crash on the print.
    """
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return str(path)


def col_letter(index: int) -> str:
    letter = ""
    while True:
        letter = chr(ord("A") + index % 26) + letter
        index = index // 26 - 1
        if index < 0:
            return letter


# --------------------------------------------------------------------------
# collection
# --------------------------------------------------------------------------

def collect(cfg: dict, today: date, sale_date: str, only: list[str] | None = None,
            sources: Any = None) -> tuple[list[dict], list[dict]]:
    """Fetch, enrich, check and screen every listing. Returns (results, sources).

    `sources` is injected so the pipeline can be exercised end to end without a
    network — which is how the dry-run test runs.
    """
    if sources is None:
        import tax_deed_sources as sources  # lazy: needs requests

    results: list[dict] = []
    report: list[dict] = []

    for county in td.counties(cfg):
        if only and county["name"].lower() not in {o.lower() for o in only}:
            continue
        try:
            listings, source_report = sources.county_listings(county, cfg, sale_date)
        except Exception as exc:  # noqa: BLE001 - one dead county must not kill the run
            report.append({"id": county["name"], "county": county["name"], "ok": False,
                           "url": "", "rows": 0, "detail": f"{type(exc).__name__}: {exc}"})
            continue
        report.extend(source_report)

        # Enrich only what could still be bought. Every listing used to get a
        # CAD lookup plus a geocode plus a flood query — three requests each,
        # at one per second — so 758 listings meant well over half an hour of
        # traffic, and the appraisal district stopped answering after about 94
        # of them. A listing already rejected on its bid, its status or a
        # passed sale date cannot be rescued by anything enrichment would find.
        cheap = [(l, td.gate1_hard_disqualifiers(l, None, cfg, today)[0]) for l in listings]
        priced = [(l, r) for l, r in cheap if not r]
        priced.sort(key=lambda pair: pair[0].get("minimum_opening_bid") or float("inf"))
        budget = int(td.threshold(cfg, "MAX_ENRICHMENTS"))
        enrich = {id(l) for l, _ in priced[:budget]}
        skipped = max(0, len(priced) - budget)

        for listing in listings:
            cad = None
            checks: list[dict] = []
            if id(listing) in enrich:
                try:
                    cad = sources.cad_record(county.get("cad", ""),
                                             listing.get("account", ""), cfg)
                except Exception as exc:  # noqa: BLE001
                    print(f"  CAD lookup failed for {listing.get('account')}: {exc}",
                          file=sys.stderr)
                try:
                    checks = sources.run_checks(listing, cad, cfg)
                except Exception as exc:  # noqa: BLE001 - an exception is not a clean check
                    print(f"  checks failed for {listing.get('account')}: {exc}",
                          file=sys.stderr)
                    checks = [td.check_record(name, td.UNAVAILABLE, "check raised",
                                              f"{type(exc).__name__}: {exc}")
                              for name in td.LIEN_CHECKS]
            results.append(td.screen(listing, cad, checks, cfg, today))

        if skipped:
            print(f"  {county['name']}: enriched the {budget} cheapest of {len(priced)} "
                  f"priceable listings; {skipped} were left unenriched (MAX_ENRICHMENTS)",
                  file=sys.stderr)
        for entry in source_report:
            entry["enriched"] = min(len(priced), budget)
            entry["not_enriched"] = skipped

    order = td.county_order(cfg)
    # Prior offerings, from the snapshots already on disk. Nothing is fetched.
    history = td.offer_history(today)
    for result in results:
        td.annotate_history(result, history, cfg)

    results.sort(key=lambda r: td.sort_key(r, order))
    return results, report


# --------------------------------------------------------------------------
# file outputs
# --------------------------------------------------------------------------

def write_snapshot(results: list[dict], cfg: dict, today: date, sale_date: str,
                   statements: list[dict], source_report: list[dict]) -> Path:
    path = td.snapshot_path(today)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = td.snapshot(results, cfg, today, sale_date, statements, source_report)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    return path


def write_packets(results: list[dict], cfg: dict, statements: list[dict]) -> list[Path]:
    """One packet per candidate in PACKET_TIERS — Tier A and B by default."""
    written: list[Path] = []
    tiers = td.packet_tiers(cfg)
    by_county = {s["county"]: s for s in statements}
    for result in results:
        if result.get("tier") not in tiers:
            continue
        county = result["listing"].get("county", "")
        statement = by_county.get(county) or {"message": "no §34.015 status computed"}
        path = td.packet_path(result)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(td.packet_markdown(result, cfg, statement))
        written.append(path)
    return written


# --------------------------------------------------------------------------
# the Google Sheet
# --------------------------------------------------------------------------

def style_tab(ws, values: list[list[Any]], spec: dict, n_cols: int) -> None:
    """Disclaimer banner, frozen header, county blocks, tier conditional formats.

    Conditional format rules rather than painted cells, because the tab is
    rewritten every run and a rule keyed on the Tier column keeps working when
    the rows move. Existing rules are deleted first: gspread's `clear()` leaves
    them behind, so re-adding without deleting stacks a duplicate set every run.
    """
    sid = ws.id
    n_rows = len(values)
    tier_col = col_letter(td.COL_TIER)
    first_data = td.HEADER_ROW + 1  # 1-based sheet row of the first body row

    reqs: list[dict] = []

    # Drop this tab's existing conditional formats, newest index first.
    try:
        meta = ws.spreadsheet.fetch_sheet_metadata()
        existing = next((s.get("conditionalFormats") or []
                         for s in meta.get("sheets", [])
                         if (s.get("properties") or {}).get("sheetId") == sid), [])
        for index in range(len(existing) - 1, -1, -1):
            reqs.append({"deleteConditionalFormatRule": {"sheetId": sid, "index": index}})
    except Exception as exc:  # noqa: BLE001 - styling never blocks the content
        print(f"  note: could not enumerate existing conditional formats: {exc}",
              file=sys.stderr)

    reqs += [
        {"unmergeCells": {"range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": 4,
                                    "startColumnIndex": 0, "endColumnIndex": n_cols}}},
        {"mergeCells": {  # the disclaimer, across the full width
            "range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": 1,
                      "startColumnIndex": 0, "endColumnIndex": n_cols},
            "mergeType": "MERGE_ALL"}},
        {"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": 1},
            "cell": {"userEnteredFormat": {
                "backgroundColor": WARN_BG,
                "wrapStrategy": "WRAP",
                "verticalAlignment": "MIDDLE",
                "textFormat": {"bold": True, "fontSize": 10, "foregroundColor": INK}}},
            "fields": "userEnteredFormat(backgroundColor,wrapStrategy,verticalAlignment,textFormat)"}},
        {"updateDimensionProperties": {  # room for the disclaimer to wrap
            "range": {"sheetId": sid, "dimension": "ROWS", "startIndex": 0, "endIndex": 1},
            "properties": {"pixelSize": 96}, "fields": "pixelSize"}},
        {"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": 1, "endRowIndex": 3},
            "cell": {"userEnteredFormat": {"textFormat": {"bold": True, "fontSize": 11,
                                                          "foregroundColor": INK}}},
            "fields": "userEnteredFormat.textFormat"}},
        {"repeatCell": {  # header band
            "range": {"sheetId": sid, "startRowIndex": td.HEADER_ROW - 1,
                      "endRowIndex": td.HEADER_ROW, "startColumnIndex": 0,
                      "endColumnIndex": n_cols},
            "cell": {"userEnteredFormat": {
                "backgroundColor": HEADER_BG,
                "textFormat": {"bold": True, "foregroundColor": WHITE, "fontSize": 10},
                "verticalAlignment": "MIDDLE", "horizontalAlignment": "CENTER",
                "wrapStrategy": "WRAP"}},
            "fields": "userEnteredFormat(backgroundColor,textFormat,verticalAlignment,horizontalAlignment,wrapStrategy)"}},
        {"updateSheetProperties": {
            "properties": {"sheetId": sid,
                           "gridProperties": {"frozenRowCount": td.HEADER_ROW}},
            "fields": "gridProperties.frozenRowCount"}},
        {"repeatCell": {  # wrap the long prose columns
            "range": {"sheetId": sid, "startRowIndex": td.HEADER_ROW, "endRowIndex": n_rows,
                      "startColumnIndex": td.COL_LEGAL, "endColumnIndex": td.COL_FLAGS + 3},
            "cell": {"userEnteredFormat": {"wrapStrategy": "WRAP",
                                           "verticalAlignment": "TOP"}},
            "fields": "userEnteredFormat(wrapStrategy,verticalAlignment)"}},
        {"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "COLUMNS",
                      "startIndex": td.COL_LEGAL, "endIndex": td.COL_LEGAL + 1},
            "properties": {"pixelSize": 260}, "fields": "pixelSize"}},
        {"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "COLUMNS",
                      "startIndex": td.COL_FLAGS, "endIndex": td.COL_FLAGS + 3},
            "properties": {"pixelSize": 240}, "fields": "pixelSize"}},
    ]

    for row in spec.get("county_rows", []):
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": row, "endRowIndex": row + 1,
                      "startColumnIndex": 0, "endColumnIndex": n_cols},
            "cell": {"userEnteredFormat": {
                "backgroundColor": BANNER_BG,
                "textFormat": {"bold": True, "fontSize": 11, "foregroundColor": INK}}},
            "fields": "userEnteredFormat(backgroundColor,textFormat)"}})

    # Tier tinting, as rules on the Tier column so they survive the rows moving.
    body = {"sheetId": sid, "startRowIndex": td.HEADER_ROW, "endRowIndex": max(n_rows, first_data),
            "startColumnIndex": 0, "endColumnIndex": n_cols}
    for index, tier in enumerate(("A", "B", "C")):
        reqs.append({"addConditionalFormatRule": {
            "index": index,
            "rule": {"ranges": [body], "booleanRule": {
                "condition": {"type": "CUSTOM_FORMULA", "values": [
                    {"userEnteredValue": f'=${tier_col}{first_data}="{tier}"'}]},
                "format": {"backgroundColor": TIER_BG[tier]}}}}})

    ws.spreadsheet.batch_update({"requests": reqs})


def publish(values: list[list[Any]], spec: dict) -> str:
    """Write the `Tax Deeds` tab. Creates it; never touches another tab."""
    import publish_sheets as ps

    n_cols = max(len(row) for row in values)
    spreadsheet, client_email = ps.open_spreadsheet()
    print(f"Opened spreadsheet as {client_email}")

    ws = ps.with_retry(
        lambda: ps.get_or_create(spreadsheet, TAB_TITLE, len(values) + 20, n_cols + 2),
        f"creating/clearing '{TAB_TITLE}'")
    padded = [row + [""] * (n_cols - len(row)) for row in values]
    ps.with_retry(lambda: ws.update(padded, "A1", value_input_option="RAW"),
                  f"writing '{TAB_TITLE}'")
    try:
        style_tab(ws, values, spec, n_cols)
    except Exception as exc:  # noqa: BLE001 - the rows matter more than the colors
        print(f"  warning: formatting '{TAB_TITLE}' failed: {exc}", file=sys.stderr)
    return f"https://docs.google.com/spreadsheets/d/{spreadsheet.id}/edit#gid={ws.id}"


# --------------------------------------------------------------------------
# reporting
# --------------------------------------------------------------------------

STATEMENT_MARKS = {
    "current": "✅", "expiring": "⚠️", "expired": "🔴", "missing": "🔴",
    "unreadable": "🔴", "expires_before_sale": "🔴", "too_late": "⛔",
}


def summarize(cfg: dict, results: list[dict], statements: list[dict],
              source_report: list[dict], sale_date: str,
              today: date | None = None) -> list[str]:
    candidates = [r for r in results if r["status"] == "candidate"]
    tiers = {t: sum(1 for r in candidates if r["tier"] == t) for t in ("A", "B", "C")}
    out = [
        f"## Texas Tax Deeds — sale {sale_date}", "",
        f"> {td.DISCLAIMER}", "",
        f"{len(results)} listing(s) ingested · {len(candidates)} candidate(s) · "
        f"Tier A {tiers['A']} / B {tiers['B']} / C {tiers['C']}", "",
        "| County | Listed | Candidates | A | B | C |", "| --- | --- | --- | --- | --- | --- |",
    ]
    # Every configured county, in report order, whether or not it produced
    # anything. A county missing from this table reads as "nothing for sale",
    # which is indistinguishable from "its source broke and nobody noticed".
    for name in [c["name"] for c in td.counties(cfg)]:
        block = [r for r in candidates if r["listing"]["county"] == name]
        out.append(f"| {name} | {sum(1 for r in results if r['listing']['county'] == name)} "
                   f"| {len(block)} "
                   f"| {sum(1 for r in block if r['tier'] == 'A')} "
                   f"| {sum(1 for r in block if r['tier'] == 'B')} "
                   f"| {sum(1 for r in block if r['tier'] == 'C')} |")

    out += ["", "### §34.015 written statement", ""]
    for status in statements:
        out.append(f"- {STATEMENT_MARKS.get(status['state'], '🔴')} {status['message']}")

    # The run's own date, not the wall clock — a --today run must not read
    # half its dates from one calendar and half from another.
    asof = today or date.today()
    upcoming = [d for county in {s["county"] for s in statements}
                for d in td.deadlines(cfg, county, sale_date, asof)]
    if upcoming:
        out += ["", "### Deadlines before this sale", "",
                "Weekdays only, so each is the latest date that could possibly work.", "",
                "| Due | County | What | Status |", "| --- | --- | --- | --- |"]
        for item in sorted(upcoming, key=lambda d: d["due"]):
            out.append(f"| {item['due']} | {item['county']} | {item['what']} "
                       f"| {'**MISSED**' if item['missed'] else 'ahead'} |")

    reasons: dict[str, int] = {}
    for result in results:
        for rejection in result["rejections"]:
            reasons[rejection["code"]] = reasons.get(rejection["code"], 0) + 1
    if reasons:
        out += ["", "### Rejections", ""]
        out += [f"- `{code}` × {count}" for code, count in
                sorted(reasons.items(), key=lambda kv: -kv[1])]

    try:
        import tax_deed_sources as _sources
        failures = _sources.cad_failures
    except Exception:  # noqa: BLE001
        _sources, failures = None, {}
    if failures:
        out += ["", "### Appraisal district lookups that failed", "",
                "A property with no CAD record is flagged, not rejected — but it cannot be "
                "valued, so it cannot rank. These are the reasons, per district.", ""]
        abandoned = getattr(_sources, "cad_abandoned", {}) if failures else {}
        for district, reasons in sorted(failures.items()):
            top = sorted(reasons.items(), key=lambda kv: -kv[1])[:3]
            line = f"- **{district}** — " + "; ".join(f"{r} ×{n}" for r, n in top)
            if district in abandoned:
                line += f"\n  - **Stopped trying this district**: {abandoned[district]}"
            out.append(line)

    broken = [s for s in source_report if not s.get("ok")]
    if broken:
        out += ["", "### Sources that failed", "",
                "County sites change format without notice. Each line names the URL to fix.", ""]
        out += [f"- 🔴 `{s['id']}` — {s.get('url')}\n  {s.get('detail')}" for s in broken]
    return out


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None, sources: Any = None) -> int:
    """`sources` is injected by the dry-run test so the whole pipeline can be
    exercised without a network; production leaves it None."""
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sale-date", help="YYYY-MM-DD; defaults to the next first Tuesday")
    ap.add_argument("--county", action="append", help="limit to these counties; repeatable")
    ap.add_argument("--dry-run", action="store_true",
                    help="print everything and write the files, but do not touch the Sheet")
    ap.add_argument("--no-files", action="store_true", help="skip the snapshot and packets")
    ap.add_argument("--no-verify", action="store_true",
                    help="skip the source structure check before ingesting")
    ap.add_argument("--config", type=Path, help="alternate config/tax_deeds.json")
    args = ap.parse_args(argv)

    cfg = td.load_config(args.config)
    today = datetime.now(ET).date()
    sale_date = args.sale_date or td.next_sale_date(today).isoformat()
    names = [c["name"] for c in td.counties(cfg)
             if not args.county or c["name"].lower() in {o.lower() for o in args.county}]
    statements = td.statement_report(cfg, names, today, sale_date)

    print(td.DISCLAIMER)
    print(f"\nScreening {', '.join(names)} for the {sale_date} sale (today {today}).\n")

    verification: list[dict] = []
    every_list_failed = False
    if not args.no_verify:
        if sources is None:
            import tax_deed_sources as sources
        verification = sources.verify(cfg)
        for entry in verification:
            if not entry["ok"]:
                print(f"🔴 {entry['id']} — {entry['url']}\n    {entry['detail']}",
                      file=sys.stderr)
        lists = [e for e in verification if e["kind"] == "county list"]
        every_list_failed = bool(lists) and not any(e["ok"] for e in lists)

    # When every county list is unreadable there is nothing to screen — but
    # raising here is what made the first live run useless: it exited before
    # writing the snapshot or the step summary, so the only record of *which*
    # URL broke and why was in the raw job log. Carry on with an empty result
    # set, leave the full diagnosis on disk and in the summary, and return
    # non-zero at the end. The Sheet is still not touched, which is the part
    # that actually mattered.
    results: list[dict] = []
    source_report: list[dict] = []
    if not every_list_failed:
        results, source_report = collect(cfg, today, sale_date, args.county, sources)
    source_report = verification + source_report

    for status in statements:
        # Same marks as the summary. A `too_late` county is not a warning that
        # ranks with an expiring statement — its whole sale is off the table.
        if status["state"] != "current":
            mark = STATEMENT_MARKS.get(status["state"], "🔴")
            print(f"{mark}  {status['message']}", file=sys.stderr)

    values, spec = td.sheet_rows(results, cfg, today, sale_date, statements)

    if not args.no_files:
        path = write_snapshot(results, cfg, today, sale_date, statements, source_report)
        print(f"Snapshot -> {rel(path)}")
        packets = write_packets(results, cfg, statements)
        tiers = "/".join(sorted(td.packet_tiers(cfg)))
        print(f"Packets  -> {len(packets)} Tier {tiers} due-diligence file(s) under "
              f"{rel(td.PACKET_DIR / sale_date)}/")
        if not packets and any(r["status"] == "candidate" for r in results):
            print(f"  note: every candidate fell outside Tier {tiers}. While the county "
                  f"clerk adapters report unavailable, an unscreened federal tax lien is a "
                  f"material flag and nothing reaches Tier A or B. Set PACKET_TIERS=A,B,C "
                  f"to write a packet per candidate and read the flags yourself.")

    summary = summarize(cfg, results, statements, source_report, sale_date, today)
    print("\n".join(summary))
    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as handle:
            handle.write("\n".join(summary) + "\n")

    if every_list_failed:
        print("\n".join([
            "", "🔴 Every county sale list failed verification.", "",
            "Nothing was screened and the Sheet was not touched — an empty `Tax Deeds` tab",
            "reads exactly like 'no sales this month', which is the one failure that would",
            "cost you a sale date. The snapshot above records every source and its error.",
            "", "Fix config/tax_deeds.json, then re-run "
            "`python scripts/tax_deed_sources.py verify`.",
        ]), file=sys.stderr)
        return 2

    if args.dry_run:
        print(f"\n--- DRY RUN: '{TAB_TITLE}' tab, {len(values)} rows ---")
        for row in values[:40]:
            print("  " + " | ".join(str(cell)[:26] for cell in row))
        if len(values) > 40:
            print(f"  ... {len(values) - 40} more row(s)")
        print("\nSheet not touched.")
    else:
        print(f"\n{publish(values, spec)}")

    broken = [s for s in source_report if not s.get("ok")]
    if broken:
        print(f"\n{len(broken)} source(s) failed — see the URLs above.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    # An uncaught exception exits 1, which is exactly the code that means "a
    # source failed verification" — so a crash inside the screener read as a
    # bad county URL, and a real UnboundLocalError shipped looking like one.
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception:  # noqa: BLE001
        import traceback
        traceback.print_exc()
        print("::error::tax_deed_screen.py crashed — this is a bug in the screener, "
              "not a county source.", file=sys.stderr)
        raise SystemExit(3)
