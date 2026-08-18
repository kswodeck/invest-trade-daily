#!/usr/bin/env python3
"""Re-quote today's published ideas and update the Sheet.

    python scripts/refresh_prices.py reports/2026-08-17/report.json
    python scripts/refresh_prices.py reports/2026-08-17/report.json --dry-run

The report is researched at 6am ET, three and a half hours before the US open.
No data provider fixes that: at 6am the freshest honest equity price is the
previous close. This runs after the open instead, so the sheet shows what things
actually cost at the moment you would place an order, and how far each idea sits
from its entry right now.

It touches prices only. Entries, targets, stops and theses are the morning's
analysis and are left exactly as they were.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

ET = ZoneInfo("America/New_York")

# Two scheduled refreshes plus DST double-arms means the same run can fire
# twice. Anything refreshed this recently is already current.
MIN_MINUTES_BETWEEN = 90


def refresh_one(idea: dict, md: Any) -> tuple[bool, str]:
    """Update one idea's price in place. Returns (changed, note)."""
    symbol = idea.get("symbol", "")
    cls = idea.get("asset_class")
    if not symbol or cls == "event":
        return False, "no free quote source"

    try:
        if cls == "crypto":
            res = md.crypto([idea.get("coingecko_id") or symbol.lower()])
            prices = list(res.get("prices", {}).values()) if res.get("ok") else []
            price = prices[0]["price"] if prices else None
            asof, source = datetime.now(ET).isoformat(timespec="seconds"), "coingecko"
        else:
            q = md.quote(symbol)
            if not q.get("ok"):
                return False, "quote failed"
            price, asof, source = q.get("price"), q.get("asof"), q.get("source")
    except Exception as exc:  # noqa: BLE001 - a refresh must never break the sheet
        return False, f"{type(exc).__name__}"

    if price is None:
        return False, "no price"

    before = idea.get("last_price")
    idea["last_price"] = price
    idea["last_price_asof"] = asof
    idea["price_source"] = source

    entry = (idea.get("entry") or {}).get("ideal")
    if entry:
        idea["distance_to_entry_pct"] = round((price - entry) / entry * 100, 2)

    moved = f"{before} → {price}" if before is not None else str(price)
    return True, moved


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("report", type=Path)
    ap.add_argument("--dry-run", action="store_true", help="update the file but not the Sheet")
    ap.add_argument("--force", action="store_true", help="refresh even if recently refreshed")
    args = ap.parse_args(argv)

    if not args.report.exists():
        print(f"No report at {args.report} — nothing to refresh.")
        return 0

    report = json.loads(args.report.read_text())
    ideas = report.get("recommendations", [])
    if not ideas:
        print("Report has no recommendations — nothing to refresh.")
        return 0

    last = report.get("last_refreshed_et")
    if last and not args.force:
        try:
            age = (datetime.now(ET) - datetime.fromisoformat(last)).total_seconds() / 60
            if age < MIN_MINUTES_BETWEEN:
                print(f"Refreshed {age:.0f} min ago (< {MIN_MINUTES_BETWEEN}); skipping. Use --force to override.")
                return 0
        except ValueError:
            pass

    import market_data as md

    session = md.market_session()
    print(f"Refreshing {len(ideas)} ideas — US equity session: {session}")

    changed = 0
    for idea in sorted(ideas, key=lambda i: i.get("rank", 99)):
        ok, note = refresh_one(idea, md)
        changed += ok
        dist = idea.get("distance_to_entry_pct")
        dist_s = f"{dist:+.2f}% from entry" if dist is not None else ""
        print(f"  {idea.get('symbol', ''):<10} {'✓' if ok else '–'} {note:<24} {dist_s}")

    report["last_refreshed_et"] = datetime.now(ET).isoformat(timespec="seconds")
    report["last_refresh_session"] = session
    args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(f"\nUpdated {changed} of {len(ideas)} prices in {args.report.name}")

    if args.dry_run:
        print("Dry run — Sheet not touched.")
        return 0

    try:
        import publish_sheets as ps
        spreadsheet, _ = ps.open_spreadsheet()
        values, header_row, spec = ps.build_today_values(report)
        ps.write_tab(spreadsheet, "Today", values, header_row, spec)
        ps.write_tab(spreadsheet, report["date"], values, header_row, spec)
        print("Rewrote the 'Today' and dated tabs with fresh prices.")
    except SystemExit as exc:
        print(f"Sheet update skipped: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
