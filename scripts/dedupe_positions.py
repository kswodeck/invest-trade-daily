#!/usr/bin/env python3
"""Collapse re-pitched ideas in state/open_positions.json into single positions.

    python scripts/dedupe_positions.py --dry-run
    python scripts/dedupe_positions.py

The tracker used to open a new row every time an idea was published, so a
thesis carried for a fortnight became a fortnight of rows: DHT appeared six
times, XLE five, and the first 57 rows were 24 distinct calls. Every figure
that averaged over rows counted the re-pitched losers repeatedly.

`publish_sheets.merge_report` stops it happening again. This is the one-off
repair of what is already stored, applying the same rule backwards:

    One live position per (symbol, direction). A republish while that position
    is still live is an amendment to it. A republish after it has closed is a
    genuinely new trade and keeps its own row — a name worth trading three
    times still shows up three times.

Merged rows are cleared of their grades and re-graded on the next publish,
because the outcome recorded against a row was computed against the levels it
held at the time. KRE's surviving row was stopped at 74.20 on 2026-08-25; with
the stop it was actually carrying by 2026-08-18 it was out on the 19th. The
levels changed, so the answer does too, and only a walk over the bars with
`amendments` in hand can say what it is.

Idempotent: with no duplicate live rows left, a second run changes nothing.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
STATE_PATH = REPO / "state" / "open_positions.json"
sys.path.insert(0, str(REPO / "scripts"))

# Written by grading, meaningless once the levels behind them have moved.
DERIVED = ("status", "filled_date", "fill_price", "closed", "exit_price",
           "pct_vs_entry", "days_open", "days_since_published")

# Fields describing today's view of the idea rather than the position's
# history, so the most recent publication wins.
CURRENT_VIEW = ("conviction", "position_size_pct", "horizon", "instrument",
                "venue", "unit", "asset_class", "last_price", "last_price_asof")


def _live_on(pos: dict, when: str) -> bool:
    """Was this position still open or awaiting entry on the given date?"""
    closed = pos.get("closed")
    return closed is None or closed >= when


def _level_record(pos: dict) -> dict[str, Any]:
    return {
        "date": pos.get("opened"),
        "entry": pos.get("entry"),
        "target": pos.get("target"),
        "stop": pos.get("stop"),
        "reference_price": pos.get("reference_price"),
    }


def group_runs(rows: list[dict]) -> list[list[dict]]:
    """Split one symbol/direction's rows into consecutive live positions."""
    runs: list[list[dict]] = []
    for row in sorted(rows, key=lambda p: p.get("opened") or ""):
        if runs and _live_on(runs[-1][0], row.get("opened") or ""):
            runs[-1].append(row)
        else:
            runs.append([row])
    return runs


def collapse(run: list[dict]) -> tuple[dict, bool]:
    """One run of rows into one position. Returns (position, was_merged)."""
    head = json.loads(json.dumps(run[0]))  # copy; the input stays readable
    if len(run) == 1:
        return head, False

    history = [_level_record(run[0])]
    for row in run[1:]:
        record = _level_record(row)
        previous = history[-1]
        if all(record[field] == previous[field]
               for field in ("entry", "target", "stop")):
            continue  # republished unchanged — the report repeating itself
        history.append(record)

    latest = run[-1]
    for field in CURRENT_VIEW:
        if latest.get(field) is not None:
            head[field] = latest[field]
    for field in ("entry", "target", "stop", "reference_price"):
        head[field] = history[-1][field]

    # A run republished at unchanged levels is one position with no revisions
    # to record — EEM went out three mornings at the same 65.60. Storing a
    # one-entry history would make it look revised on the Sheet.
    if len(history) > 1:
        head["amendments"] = history
        head["last_amended"] = history[-1]["date"]
    else:
        head.pop("amendments", None)
        head.pop("last_amended", None)
    head["last_seen"] = latest.get("opened")
    for field in DERIVED:
        head.pop(field, None)
    head["status"] = "pending"
    return head, True


def dedupe(positions: list[dict]) -> tuple[list[dict], list[str]]:
    by_thesis: dict[tuple, list[dict]] = defaultdict(list)
    for pos in positions:
        by_thesis[(pos.get("symbol"), pos.get("direction"))].append(pos)

    out: list[dict] = []
    notes: list[str] = []
    for (symbol, direction), rows in by_thesis.items():
        runs = group_runs(rows)
        for run in runs:
            position, merged = collapse(run)
            out.append(position)
            if merged:
                revisions = len(position.get("amendments") or [])
                changes = (f"{revisions - 1} level revision(s)" if revisions > 1
                           else "republished at unchanged levels")
                notes.append(
                    f"{symbol} {direction}: {len(run)} rows -> 1 position opened "
                    f"{run[0].get('opened')}, last pitched {position['last_seen']} "
                    f"— {changes}")
        if len(runs) > 1:
            notes.append(f"{symbol} {direction}: kept as {len(runs)} separate "
                         "positions — each opened after the previous one closed")
    out.sort(key=lambda p: (p.get("opened") or "", p.get("symbol") or ""))
    return out, notes


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would change without writing state")
    ap.add_argument("--state", type=Path, default=STATE_PATH)
    args = ap.parse_args(argv)

    positions = json.loads(args.state.read_text() or "[]")
    deduped, notes = dedupe(positions)

    for note in notes:
        print(f"  {note}")
    merged = len(positions) - len(deduped)
    print(f"\n{len(positions)} rows -> {len(deduped)} positions "
          f"({merged} folded in as amendments)")

    if merged:
        print("Merged positions were cleared of their grades; the next publish "
              "re-grades them from daily bars against the levels each day held.")
    if args.dry_run:
        print("\nDry run — state not written.")
        return 0
    args.state.write_text(json.dumps(deduped, indent=2) + "\n")
    print(f"\nWrote {args.state}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
