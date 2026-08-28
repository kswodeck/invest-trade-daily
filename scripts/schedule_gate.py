#!/usr/bin/env python3
"""Decide whether a scheduled invocation is today's daily-report run.

GitHub cron is UTC-only and has no DST awareness, so a 6am ET job must declare
one arm for EDT and one for EST. Both arms fire every day of the year — the
gate is what drops the one that is not 6am ET today.

Two independent questions, answered separately, because conflating them is what
broke:

1. **Is it still early enough?** Decided from the wall clock in New York, never
   from which cron fired. In EDT the 11:00 UTC "EST arm" lands at 7am ET, which
   is a perfectly good hour — so the hour check alone cannot tell the arms
   apart, and must not try.

2. **Has today's report already been published?** Decided from the branch tip,
   never from the checked-out tree. A scheduled run is pinned to the SHA that
   existed when GitHub created it, so its checkout cannot contain a commit an
   earlier arm pushed minutes ago. The caller resolves this and passes the
   answer in as --have-report.

Answering (2) against the live branch is what actually stops the duplicate run;
the hour window only decides whether a late delivery is still worth honouring.

    python scripts/schedule_gate.py --event-name schedule \
        --cron "0 11 * * *" --have-report false --window 6-11

Prints a JSON decision to stdout and, when GITHUB_OUTPUT is set, appends
`proceed`, `date` and `late` for the workflow to branch on. Always exits 0 —
"do not run" is a decision, not a failure.
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")


@dataclass(frozen=True)
class Decision:
    proceed: bool
    date: str
    reason: str
    late: bool = False


def cron_local_hour(cron: str, now_et: datetime) -> int | None:
    """The New York hour a UTC cron expression lands on, on now_et's date.

    Returns None for anything but a plain numeric hour field — the arms this
    repo declares are all of the form "M H * * *", and a stepped or listed hour
    has no single answer worth guessing at.
    """
    fields = cron.split()
    if len(fields) != 5:
        return None
    minute, hour = fields[0], fields[1]
    if not (hour.isdigit() and minute.isdigit()):
        return None
    fired = datetime(
        now_et.year, now_et.month, now_et.day, int(hour), int(minute), tzinfo=UTC
    )
    # A UTC morning hour maps to the same calendar day in ET only after the
    # offset is applied; anchor on now_et's ET date and step back if it wrapped.
    local = fired.astimezone(ET)
    if local.date() > now_et.date():
        local = (fired - timedelta(days=1)).astimezone(ET)
    return local.hour


def decide(
    now_et: datetime,
    event_name: str,
    have_report: bool,
    window_start: int,
    window_end: int,
) -> Decision:
    """Whether this invocation should run the pipeline.

    window_start/window_end are ET hours, half-open: [start, end). The window is
    wide because GitHub's scheduler is best-effort and routinely delivers this
    repo's crons late — but not unbounded, because a report framed as the 6am
    pre-open view is a lie if it is researched and published in the afternoon.
    """
    date = now_et.date().isoformat()

    if event_name != "schedule":
        # A human (or the watchdog) asked for this explicitly. Honour it — the
        # duplicate guard exists to stop the scheduler, not the operator.
        return Decision(True, date, f"{event_name} — proceeding on request")

    if have_report:
        return Decision(False, date, f"reports/{date}/report.json is already on the branch")

    if now_et.hour < window_start:
        return Decision(
            False,
            date,
            f"{now_et:%H:%M} ET is before the {window_start:02d}:00 window — "
            "this is the other DST arm",
        )

    if now_et.hour >= window_end:
        return Decision(
            False,
            date,
            f"{now_et:%H:%M} ET is past the {window_end:02d}:00 cutoff — GitHub "
            "delivered this cron too late for a pre-open report",
            late=True,
        )

    return Decision(True, date, f"{now_et:%H:%M} ET, no report yet — proceeding")


def _window(raw: str) -> tuple[int, int]:
    start, _, end = raw.partition("-")
    return int(start), int(end)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--event-name", required=True, help="github.event_name")
    ap.add_argument("--cron", default="", help="github.event.schedule, for the log")
    ap.add_argument(
        "--have-report",
        required=True,
        help="true if reports/<today>/report.json exists on the branch tip",
    )
    ap.add_argument(
        "--window",
        default="6-11",
        help="ET hours [start-end) in which a scheduled run may proceed",
    )
    args = ap.parse_args()

    start, end = _window(args.window)
    now_et = datetime.now(ET)
    decision = decide(
        now_et=now_et,
        event_name=args.event_name,
        have_report=args.have_report.strip().lower() == "true",
        window_start=start,
        window_end=end,
    )

    print(f"Now: {now_et:%a %Y-%m-%d %H:%M:%S %Z} (hour {now_et.hour})")
    if args.cron:
        local = cron_local_hour(args.cron, now_et)
        where = f"{local:02d}:00 ET today" if local is not None else "an unparsed hour"
        print(f"Fired by cron {args.cron!r}, which is {where}.")
    print(f"{'PROCEED' if decision.proceed else 'SKIP'}: {decision.reason}")

    if decision.late:
        print(
            "::warning::Scheduled delivery arrived outside the report window. "
            "No report was produced from this invocation."
        )

    print(json.dumps(asdict(decision)))

    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as fh:
            fh.write(f"proceed={str(decision.proceed).lower()}\n")
            fh.write(f"date={decision.date}\n")
            fh.write(f"late={str(decision.late).lower()}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
