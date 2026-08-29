#!/usr/bin/env python3
"""Tally today's daily-report runs, so the catch-up knows when to stop.

Reads the JSON that `gh run list --json status,createdAt` prints and answers two
questions the catch-up needs before dispatching:

- Is one already queued or running? Dispatching then only queues a duplicate
  that the gate skips seconds later.
- How many have already been created today, in ET? A pipeline that has failed
  three times this morning will not be fixed by a fourth attempt, and every
  workflow in the repo can call the catch-up — the bound is what keeps that from
  becoming a dispatch loop.

"Today" is the New York date, matching the report the runs are trying to
produce; a run created at 02:00 UTC belongs to the previous ET day.

    gh run list --workflow daily-report.yml --limit 50 --json status,createdAt \\
        | python scripts/report_runs.py

Prints "<busy> <started_today>". Malformed or empty input prints "0 0" — the
caller's fallback is to dispatch, which the concurrency group makes safe.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
BUSY_STATUSES = frozenset({"queued", "in_progress", "requested", "waiting", "pending"})


def tally(runs: list[dict], now_et: datetime) -> tuple[int, int]:
    """(runs busy right now, runs created on now_et's ET date)."""
    today = now_et.date()
    busy = 0
    started = 0
    for run in runs:
        if not isinstance(run, dict):
            continue
        if run.get("status") in BUSY_STATUSES:
            busy += 1
        created = run.get("createdAt")
        if not isinstance(created, str):
            continue
        try:
            when = datetime.fromisoformat(created.replace("Z", "+00:00"))
        except ValueError:
            continue
        if when.astimezone(ET).date() == today:
            started += 1
    return busy, started


def main() -> int:
    try:
        runs = json.load(sys.stdin)
    except (json.JSONDecodeError, UnicodeDecodeError):
        runs = []
    if not isinstance(runs, list):
        runs = []
    busy, started = tally(runs, datetime.now(ET))
    print(busy, started)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
