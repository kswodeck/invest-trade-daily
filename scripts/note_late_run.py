#!/usr/bin/env python3
"""Say so in the report when the research did not happen at 6am.

The report is written and read as the pre-open view: prices are the prior
close, entries are levels to work when the session opens, and the whole frame
assumes the reader sees it before 9:30. Widening the schedule window to 6-11 ET
was the right call — GitHub delivers this repo's crons hours late and a late
report beats none — but it quietly made that frame a lie on any late morning.
2026-08-29 and 2026-08-30 were both researched around 10:45 ET and published
just before noon, described exactly like the 6am ones.

So stamp the report with when it actually ran. A reader can discount a
10:45 report on its own terms; they cannot discount one that does not admit
what it is.

    python scripts/note_late_run.py reports/2026-08-30/report.json \\
        --started-et 2026-08-30T10:42:00-04:00

The note is prepended to data_quality_notes — the schema allows no new
top-level keys, and this is exactly what that field is for. Runs that started
in the pre-open slot are left untouched, and the stamp is idempotent, so a
re-run does not stack notes. Exits 0 whether or not it wrote anything.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, time
from pathlib import Path
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")

# The slot the report is written for. Anything materially past it is worth
# saying out loud; 07:30 leaves room for the ordinary half-hour of scheduler
# slippage that has always been present without narrating it every day.
PRE_OPEN_DEADLINE = time(7, 30)
REGULAR_OPEN = time(9, 30)
REGULAR_CLOSE = time(16, 0)

MARKER = "RESEARCHED LATE:"


def session_at(when_et: datetime) -> str:
    """Plain-language session, matching market_data.market_session()'s split."""
    if when_et.weekday() >= 5:
        return "with the market closed for the weekend"
    t = when_et.time()
    if t < REGULAR_OPEN:
        return "before the open"
    if t < REGULAR_CLOSE:
        return "during the regular session"
    return "after the close"


def note_for(started_et: datetime) -> str | None:
    """The sentence to prepend, or None when the run was timely."""
    if started_et.time() <= PRE_OPEN_DEADLINE:
        return None
    where = session_at(started_et)
    caveat = (
        "Prices and levels here reflect a market already trading, not the "
        "pre-open view this report is normally written as"
        if where == "during the regular session"
        else "This is later than the 6am pre-open slot the report is written for"
    )
    return (
        f"{MARKER} the research phase started at {started_et:%H:%M} ET, {where}. "
        f"{caveat}. GitHub delivered the scheduled trigger late."
    )


def stamp(report: dict, started_et: datetime) -> bool:
    """Prepend the note in place. True when the report was changed."""
    note = note_for(started_et)
    if note is None:
        return False
    existing = str(report.get("data_quality_notes") or "").strip()
    if existing.startswith(MARKER):
        return False  # already stamped; never stack
    report["data_quality_notes"] = f"{note} {existing}".strip()
    return True


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("report", type=Path, help="path to report.json")
    ap.add_argument(
        "--started-et",
        required=True,
        help="ISO timestamp of when the run started, e.g. 2026-08-30T10:42:00-04:00",
    )
    args = ap.parse_args(argv)

    try:
        started = datetime.fromisoformat(args.started_et)
    except ValueError:
        print(f"Unparseable --started-et {args.started_et!r}; not stamping.", file=sys.stderr)
        return 0
    started = started.astimezone(ET) if started.tzinfo else started.replace(tzinfo=ET)

    if not args.report.exists():
        print(f"No report at {args.report} — nothing to stamp.")
        return 0
    try:
        report = json.loads(args.report.read_text())
    except json.JSONDecodeError as exc:
        # ensure_report.py owns replacing a broken report; don't fight it.
        print(f"{args.report} is not valid JSON ({exc}); not stamping.", file=sys.stderr)
        return 0

    if stamp(report, started):
        args.report.write_text(json.dumps(report, indent=2) + "\n")
        print(f"Stamped: started {started:%H:%M} ET, {session_at(started)}.")
    else:
        print(f"Started {started:%H:%M} ET — timely, or already stamped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
