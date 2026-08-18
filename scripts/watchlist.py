#!/usr/bin/env python3
"""Build a tap-to-open watchlist of high-conviction ideas.

    python scripts/watchlist.py 2026-08-17 --days 14

Robinhood has no watchlist API — their only official public API is for crypto
trading, and their terms do not permit third-party applications to act on an
account. So rather than automating the write, this produces the next best
thing: a deduplicated list of conviction 4+ ideas where each row is a link that
opens the Robinhood app straight to that instrument. From there it is one tap
to "Add to List".

Ideas persist for `--days` after they were last recommended, so a name does not
vanish from the list because today's research happened to look elsewhere.

Importable: `collect(today, days)` and `render_rows(entries)`.
"""

from __future__ import annotations

import argparse
import json
from datetime import date, timedelta
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
STATE_PATH = REPO / "state" / "open_positions.json"

MIN_CONVICTION = 4

# Deep links open the mobile app directly to the instrument. Equities are the
# stable case; crypto follows the same pattern. Futures and event contracts have
# no public per-instrument URL, so those rows carry no link rather than a broken
# one.
def deep_link(idea: dict) -> str:
    symbol = (idea.get("symbol") or "").upper().lstrip("/")
    cls = idea.get("asset_class")
    if cls in ("stock", "etf"):
        return f"https://robinhood.com/stocks/{symbol}"
    if cls == "crypto":
        return f"https://robinhood.com/crypto/{symbol}"
    return ""


def load_positions() -> set[str]:
    if not STATE_PATH.exists():
        return set()
    try:
        rows = json.loads(STATE_PATH.read_text() or "[]")
    except json.JSONDecodeError:
        return set()
    return {r.get("symbol") for r in rows if r.get("status") == "open"}


def collect(today: date, days: int = 14, min_conviction: int = MIN_CONVICTION) -> list[dict]:
    """Every conviction 4+ idea from the last `days` reports, newest wins."""
    entries: dict[str, dict] = {}

    for offset in range(days, -1, -1):  # oldest first so newer entries overwrite
        day = today - timedelta(days=offset)
        path = REPO / "reports" / day.isoformat() / "report.json"
        if not path.exists():
            continue
        try:
            report = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue

        for idea in report.get("recommendations", []):
            if (idea.get("conviction") or 0) < min_conviction:
                continue
            symbol = idea.get("symbol")
            if not symbol:
                continue
            prior = entries.get(symbol)
            entries[symbol] = {
                "symbol": symbol,
                "instrument": idea.get("instrument", ""),
                "asset_class": idea.get("asset_class", ""),
                "venue": idea.get("venue", ""),
                "direction": idea.get("direction", ""),
                "horizon": idea.get("horizon", ""),
                "conviction": idea.get("conviction"),
                "entry": (idea.get("entry") or {}).get("ideal"),
                "target": (idea.get("exit") or {}).get("target"),
                "last_price": idea.get("last_price"),
                "distance_to_entry_pct": idea.get("distance_to_entry_pct"),
                "catalyst": (idea.get("catalyst") or {}).get("event", ""),
                "catalyst_when": (idea.get("catalyst") or {}).get("datetime_et") or "",
                "waiting": bool((idea.get("catalyst") or {}).get("wait")),
                "last_seen": day.isoformat(),
                "first_seen": (prior or {}).get("first_seen", day.isoformat()),
                "times_recommended": ((prior or {}).get("times_recommended", 0)) + 1,
                "link": deep_link(idea),
            }

    open_symbols = load_positions()
    for entry in entries.values():
        entry["already_open"] = entry["symbol"] in open_symbols

    return sorted(
        entries.values(),
        key=lambda e: (-(e["conviction"] or 0), e["last_seen"]),
        reverse=False,
    )


HEADERS = [
    "Open in Robinhood", "Symbol", "Instrument", "Class", "Side", "Horizon",
    "Conv", "Entry", "Last", "Dist to Entry", "Catalyst", "When (ET)",
    "Status", "First seen", "Times", "Last seen",
]


def render_rows(entries: list[dict], today: date, min_conviction: int = MIN_CONVICTION) -> list[list[Any]]:
    rows: list[list[Any]] = [
        [f"WATCHLIST — conviction {min_conviction}+ · {len(entries)} instruments · as of {today.isoformat()}"],
        ["Tap a link to open the instrument in Robinhood, then use Add to List. "
         "Robinhood has no watchlist API, so this is the fastest safe path."],
        ["Names persist here for two weeks after they were last recommended, so a "
         "good idea does not disappear because today's research looked elsewhere."],
        [""],
        HEADERS,
    ]

    for e in entries:
        # HYPERLINK renders as a tappable label; needs USER_ENTERED on write.
        link = f'=HYPERLINK("{e["link"]}","▶ {e["symbol"]}")' if e["link"] else "—"
        status = "● holding" if e.get("already_open") else ("⏸ waiting" if e["waiting"] else "▶ actionable")
        dist = e.get("distance_to_entry_pct")
        rows.append([
            link,
            e["symbol"],
            e["instrument"],
            (e["asset_class"] or "").upper(),
            (e["direction"] or "").upper(),
            e["horizon"],
            e["conviction"],
            e["entry"] if e["entry"] is not None else "",
            e["last_price"] if e["last_price"] is not None else "",
            f"{dist:+.2f}%" if dist is not None else "",
            e["catalyst"][:70],
            e["catalyst_when"],
            status,
            e["first_seen"],
            e["times_recommended"],
            e["last_seen"],
        ])

    if not entries:
        rows.append([f"No conviction {min_conviction}+ ideas in the window."])
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("date", nargs="?", help="as-of date, YYYY-MM-DD; defaults to today")
    ap.add_argument("--days", type=int, default=14, help="how far back to carry ideas forward")
    ap.add_argument("--min-conviction", type=int, default=MIN_CONVICTION)
    args = ap.parse_args(argv)

    today = date.fromisoformat(args.date) if args.date else date.today()
    entries = collect(today, args.days, args.min_conviction)
    for row in render_rows(entries, today, args.min_conviction):
        print(" | ".join(str(c) for c in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
