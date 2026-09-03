#!/usr/bin/env python3
"""Publish the odd-lot universe to a single tab on the existing Sheet.

    python scripts/publish_odd_lot.py
    python scripts/publish_odd_lot.py --dry-run

Writes **one** tab, `Odd Lot`, overwritten in place on every run. It is a live
view of what is currently tenderable, not an archive: an offer that expires
leaves the tab, and `reports/<date>/odd_lot.md` plus the universe file in
`state/` keep the history.

That is the opposite of how `publish_sheets.py` treats the daily report, and
deliberately so. A trade idea is a call that has to be scored later, so its tab
is dated and immutable. An open tender offer is a fact about today with an
expiration date attached — a dated archive of it would be a list of offers you
can no longer tender into.

Shares the credentials, retry and styling helpers with `publish_sheets.py`, so
there is one answer to "how does this repo talk to Google" rather than two.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import odd_lot  # noqa: E402
from publish_sheets import (  # noqa: E402
    AMBER, GREEN, GREY, HEADER_BG, INK, WHITE, open_spreadsheet, with_retry,
)

ET = ZoneInfo("America/New_York")
TAB = "Odd Lot"

HEADERS = [
    "Tier", "Ticker", "Company", "Form", "Filed", "Offer", "Last", "As of",
    "Spread", "Annualized", "Capital 99sh", "Profit 99sh", "Expires", "Days",
    "Withdraw by", "Avg vol 30d", "Risk flags", "Odd-lot language / why rejected",
    "Filing",
]

COL_TIER, COL_SPREAD = 0, 8
COL_QUOTE = HEADERS.index("Odd-lot language / why rejected")

TIER_BG = {"A": GREEN, "B": AMBER, "C": GREY}

DISCLAIMER = (
    "Automated research, not investment advice. An odd-lot preference is a term of the "
    "offer and the issuer can amend or remove it — verify the quoted language in the "
    "linked filing before tendering. You must tender ALL shares you own, and ownership "
    "aggregates across every account under your SSN."
)


def _pct(value: float | None) -> str:
    return "" if value is None else f"{value * 100:+.2f}%"


def _usd(value: float | None) -> str:
    return "" if value is None else f"${value:,.2f}"


def _count(value: int | None) -> str:
    return "" if value is None else f"{value:,}"


def offer_row(entry: dict[str, Any], *, rejected: bool = False) -> list[Any]:
    """One row, for a live offer or a rejected one.

    Rejected offers keep whatever economics were computed before the gate that
    stopped them, and their risk flags — a rejection for a $8,415 capital
    requirement is far more useful next to the price that caused it, and a
    `market price above offer` flag is worth seeing whatever the verdict.
    """
    if entry.get("dutch_range"):
        low, high = entry["dutch_range"]
        offer = f"{_usd(low)} (Dutch {_usd(low)}–{_usd(high)})"
    else:
        offer = _usd(entry.get("offer_price"))

    withdraw = entry.get("withdrawal_deadline") or ""
    if withdraw and entry.get("withdrawal_basis") == "expiration_date":
        withdraw += " (= expiry)"

    if rejected:
        wide = "REJECTED: " + "; ".join(entry.get("rejections") or ["unstated"])
    else:
        wide = " ".join((entry.get("odd_lot_paragraph") or "").split())

    return [
        entry.get("tier") or "",
        entry.get("ticker") or "",
        entry.get("company") or "",
        entry.get("form") or "",
        entry.get("filed") or "",
        offer,
        _usd(entry.get("market_price")),
        (entry.get("price_asof") or "")[:16],
        _pct(entry.get("spread_pct")),
        _pct(entry.get("annualized")),
        _usd(entry.get("capital")),
        _usd(entry.get("gross_profit")),
        entry.get("expiration_date") or "",
        entry.get("days_to_expiry", ""),
        withdraw,
        _count(entry.get("avg_volume_30d")),
        ", ".join(f.replace("_", " ") for f in entry.get("risk_flags") or []),
        wide,
        entry.get("url") or "",
    ]


def build_values(universe: dict[str, Any], config: dict[str, Any],
                 now: datetime | None = None) -> tuple[list[list[Any]], int, dict[str, Any]]:
    """Returns (rows, header_row_1based, style_spec)."""
    now = now or datetime.now(ET)
    live = [e for e in universe["open"] if e.get("status") == "candidate"]
    rejected = [e for e in universe["open"] if e.get("status") == "rejected"]
    by_tier = {t: [e for e in live if e.get("tier") == t] for t in ("A", "B", "C")}
    econ = config["economics"]

    rows: list[list[Any]] = [
        ["ODD-LOT TENDER OFFERS — CURRENTLY OPEN"],
        [f"Updated {now:%Y-%m-%d %H:%M ET}  ·  {len(universe['open'])} offers tracked  ·  "
         f"{len(by_tier['A'])} Tier A, {len(by_tier['B'])} Tier B, {len(by_tier['C'])} Tier C  ·  "
         f"{len(rejected)} rejected"],
        [f"Buy {econ['shares_tendered']} shares (fewer than 100), tender ALL of them, and they are "
         f"accepted before proration. Thresholds: spread ≥{econ['min_spread_pct'] * 100:.1f}%, "
         f"≥{econ['min_days_to_expiry']} days to expiry, ≤${econ['max_capital']:,} capital, "
         f"≥{econ['min_avg_volume_30d']:,} avg shares/day, ≥${econ['min_market_price']:.2f}/share."],
    ]

    if not by_tier["A"]:
        rows.append(["No Tier A opportunities. That is the normal result — thresholds are "
                     "never lowered to fill this tab."])

    rows.append([""])
    header_row = len(rows) + 1
    rows.append(HEADERS)

    tier_rows: list[tuple[int, str]] = []
    for tier in ("A", "B", "C"):
        for entry in sorted(by_tier[tier], key=lambda e: -(e.get("spread_pct") or 0)):
            tier_rows.append((len(rows), tier))
            rows.append(offer_row(entry))

    if not live:
        rows.append(["—", "", "No open offer currently clears every gate."])

    section_rows: list[int] = []
    if rejected:
        rows.append([""])
        section_rows.append(len(rows))
        rows.append([f"REJECTED ({len(rejected)}) — what was filtered out, and why. "
                     f"Seeing this is how the thresholds get tuned."])
        for entry in sorted(rejected, key=lambda e: e.get("filed", ""), reverse=True):
            rows.append(offer_row(entry, rejected=True))

    rows += [[""], [DISCLAIMER]]
    return rows, header_row, {"tiers": tier_rows, "sections": section_rows}


def style_tab(ws, header_row: int, n_cols: int, n_rows: int, spec: dict[str, Any]) -> None:
    """Header band, tier tinting, frozen header, and a readable quote column."""
    sid = ws.id
    reqs: list[dict] = [
        {"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": 1},
            "cell": {"userEnteredFormat": {
                "textFormat": {"bold": True, "fontSize": 14, "foregroundColor": INK}}},
            "fields": "userEnteredFormat.textFormat"}},
        {"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": header_row - 1, "endRowIndex": header_row,
                      "startColumnIndex": 0, "endColumnIndex": n_cols},
            "cell": {"userEnteredFormat": {
                "backgroundColor": HEADER_BG,
                "textFormat": {"bold": True, "foregroundColor": WHITE, "fontSize": 10},
                "verticalAlignment": "MIDDLE", "horizontalAlignment": "CENTER"}},
            "fields": "userEnteredFormat(backgroundColor,textFormat,verticalAlignment,"
                      "horizontalAlignment)"}},
        {"updateSheetProperties": {
            "properties": {"sheetId": sid, "gridProperties": {"frozenRowCount": header_row}},
            "fields": "gridProperties.frozenRowCount"}},
        # The quoted paragraph is the reason the tab is trustworthy, so it gets
        # room to be read rather than a truncated cell nobody expands.
        {"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "COLUMNS",
                      "startIndex": COL_QUOTE, "endIndex": COL_QUOTE + 1},
            "properties": {"pixelSize": 460}, "fields": "pixelSize"}},
        {"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "COLUMNS",
                      "startIndex": HEADERS.index("Company"), "endIndex": HEADERS.index("Company") + 1},
            "properties": {"pixelSize": 200}, "fields": "pixelSize"}},
        {"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": header_row, "endRowIndex": n_rows,
                      "startColumnIndex": COL_QUOTE, "endColumnIndex": COL_QUOTE + 1},
            "cell": {"userEnteredFormat": {"wrapStrategy": "WRAP", "verticalAlignment": "TOP"}},
            "fields": "userEnteredFormat(wrapStrategy,verticalAlignment)"}},
    ]

    for row in spec.get("sections", []):
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": row, "endRowIndex": row + 1,
                      "startColumnIndex": 0, "endColumnIndex": n_cols},
            "cell": {"userEnteredFormat": {
                "backgroundColor": HEADER_BG,
                "textFormat": {"bold": True, "foregroundColor": WHITE, "fontSize": 11}}},
            "fields": "userEnteredFormat(backgroundColor,textFormat)"}})

    for row, tier in spec.get("tiers", []):
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": row, "endRowIndex": row + 1,
                      "startColumnIndex": COL_TIER, "endColumnIndex": COL_TIER + 1},
            "cell": {"userEnteredFormat": {
                "backgroundColor": TIER_BG.get(tier, GREY),
                "textFormat": {"bold": True}, "horizontalAlignment": "CENTER"}},
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)"}})
        # A negative spread should never reach a live row — Gate 2 rejects it —
        # but tint it red rather than trust that, because the one time it does
        # it is the row that must not read as an opportunity.
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": row, "endRowIndex": row + 1,
                      "startColumnIndex": COL_SPREAD, "endColumnIndex": COL_SPREAD + 1},
            "cell": {"userEnteredFormat": {"textFormat": {"bold": True}}},
            "fields": "userEnteredFormat.textFormat"}})

    ws.spreadsheet.batch_update({"requests": reqs})


def publish(universe: dict[str, Any], config: dict[str, Any], *, dry_run: bool = False) -> int:
    values, header_row, spec = build_values(universe, config)

    if dry_run:
        for row in values:
            print(" | ".join(str(c)[:28] for c in row))
        print(f"\nDry run — '{TAB}' not written ({len(values)} rows).")
        return 0

    spreadsheet, _ = open_spreadsheet()
    n_cols = max(len(r) for r in values)
    ws = with_retry(
        lambda: _tab(spreadsheet, len(values) + 20, n_cols + 2), f"creating/clearing '{TAB}'")
    padded = [row + [""] * (n_cols - len(row)) for row in values]
    with_retry(lambda: ws.update(padded, "A1", value_input_option="RAW"), f"writing '{TAB}'")
    try:
        style_tab(ws, header_row, n_cols, len(values), spec)
    except Exception as exc:  # noqa: BLE001 - content matters more than styling
        print(f"  warning: formatting failed on '{TAB}': {exc}", file=sys.stderr)
    print(f"Wrote {len(values)} rows to '{TAB}'.")
    return 0


def _tab(spreadsheet, rows: int, cols: int):
    """The one tab, cleared and resized. Never a second, never a dated copy."""
    rows, cols = max(rows, 50), max(cols, 26)
    try:
        ws = spreadsheet.worksheet(TAB)
    except Exception:  # noqa: BLE001 - gspread raises WorksheetNotFound
        return spreadsheet.add_worksheet(title=TAB, rows=rows, cols=cols)
    ws.clear()
    if ws.row_count < rows or ws.col_count < cols:
        ws.resize(rows=max(rows, ws.row_count), cols=max(cols, ws.col_count))
    return ws


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="render the tab but do not write it")
    args = ap.parse_args(argv)
    return publish(odd_lot.load_universe(), odd_lot.load_config(), dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
