#!/usr/bin/env python3
"""Tests for the catch-up's dispatch bound.

Every workflow in the repo can call the catch-up, so the tally is the only
thing standing between a failing pipeline and a morning of dispatch loops.
"""

from __future__ import annotations

import sys
import unittest
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from report_runs import tally  # noqa: E402

ET = ZoneInfo("America/New_York")
NOW = datetime(2026, 8, 28, 9, 0, tzinfo=ET)


def run(status: str, created: str) -> dict:
    return {"status": status, "createdAt": created}


class Tally(unittest.TestCase):
    def test_counts_busy_and_todays_runs(self):
        runs = [
            run("completed", "2026-08-28T15:53:36Z"),   # 11:53 ET today
            run("in_progress", "2026-08-28T13:10:00Z"),  # 09:10 ET today
            run("completed", "2026-08-27T20:10:54Z"),   # yesterday ET
        ]
        self.assertEqual(tally(runs, NOW), (1, 2))

    def test_late_utc_runs_belong_to_the_previous_et_day(self):
        # 01:00 UTC on the 29th is 21:00 ET on the 28th — still today's attempt.
        self.assertEqual(tally([run("completed", "2026-08-29T01:00:00Z")], NOW), (0, 1))
        # 05:00 UTC on the 29th is 01:00 ET on the 29th — no longer today's.
        self.assertEqual(tally([run("completed", "2026-08-29T05:00:00Z")], NOW), (0, 0))

    def test_every_pending_status_counts_as_busy(self):
        for status in ("queued", "in_progress", "requested", "waiting", "pending"):
            with self.subTest(status=status):
                busy, _ = tally([run(status, "2026-08-28T13:00:00Z")], NOW)
                self.assertEqual(busy, 1)

    def test_malformed_entries_are_skipped_not_fatal(self):
        runs = [
            "not a dict",
            {"status": "completed"},                       # no createdAt
            run("completed", "whenever"),                  # unparseable
            run("completed", "2026-08-28T13:00:00Z"),      # the only real one
        ]
        self.assertEqual(tally(runs, NOW), (0, 1))

    def test_no_runs_at_all(self):
        self.assertEqual(tally([], NOW), (0, 0))


if __name__ == "__main__":
    unittest.main()
