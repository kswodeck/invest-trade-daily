#!/usr/bin/env python3
"""Tests for the daily-report schedule gate.

    python -m unittest discover -s tests -v

The cases below are the ones the old shell gate got wrong: a 7am ET arm that
sailed through an hour check meant to reject it, and a cron delivered ten hours
late that was thrown away as "the other DST arm".
"""

from __future__ import annotations

import sys
import unittest
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from schedule_gate import cron_local_hour, decide  # noqa: E402

ET = ZoneInfo("America/New_York")

EDT_ARM = "0 10 * * *"  # 06:00 ET while EDT is in force
EST_ARM = "0 11 * * *"  # 06:00 ET while EST is in force


def et(month: int, day: int, hour: int, minute: int = 0) -> datetime:
    return datetime(2026, month, day, hour, minute, tzinfo=ET)


def gate(now, *, event="schedule", state="missing", window=(6, 11)):
    return decide(now, event, state, window[0], window[1])


class CronToLocalHour(unittest.TestCase):
    """Both arms fire every day; only one of them is 6am ET."""

    def test_summer(self):
        summer = et(8, 28, 7)
        self.assertEqual(cron_local_hour(EDT_ARM, summer), 6)
        self.assertEqual(cron_local_hour(EST_ARM, summer), 7)

    def test_winter(self):
        winter = et(1, 15, 7)
        self.assertEqual(cron_local_hour(EDT_ARM, winter), 5)
        self.assertEqual(cron_local_hour(EST_ARM, winter), 6)

    def test_unparseable_hour_is_not_guessed(self):
        self.assertIsNone(cron_local_hour("0 */4 * * *", et(8, 28, 7)))
        self.assertIsNone(cron_local_hour("nonsense", et(8, 28, 7)))


class SummerArms(unittest.TestCase):
    """EDT: the arms land at 6am and 7am ET, both inside any sane hour window.

    The hour check cannot separate them — only the published-report check can,
    and only if it reads the branch tip rather than the pinned checkout.
    """

    def test_six_am_arm_runs(self):
        self.assertTrue(gate(et(8, 28, 6, 2)).proceed)

    def test_seven_am_arm_is_stopped_by_the_published_report(self):
        d = gate(et(8, 28, 7, 5), state="published")
        self.assertFalse(d.proceed)
        self.assertIn("already on the branch", d.reason)

    def test_seven_am_arm_retries_when_the_six_am_arm_produced_nothing(self):
        self.assertTrue(gate(et(8, 28, 7, 5)).proceed)


class WinterArms(unittest.TestCase):
    def test_edt_arm_is_too_early_in_winter(self):
        d = gate(et(1, 15, 5, 1))
        self.assertFalse(d.proceed)
        self.assertIn("other DST arm", d.reason)

    def test_est_arm_runs(self):
        self.assertTrue(gate(et(1, 15, 6, 1)).proceed)


class LateDelivery(unittest.TestCase):
    """GitHub's scheduler is best-effort; these are the observed delays."""

    def test_typical_half_hour_delay_still_runs(self):
        self.assertTrue(gate(et(8, 26, 6, 36)).proceed)

    def test_delay_the_old_two_hour_window_would_have_dropped(self):
        # 2026-08-26 style creep, pushed past 08:00. The old gate rejected this.
        self.assertTrue(gate(et(8, 26, 10, 15)).proceed)

    def test_ten_hour_delay_is_refused_and_flagged(self):
        # 2026-08-27: both arms were delivered at ~16:10 ET.
        d = gate(et(8, 27, 16, 11))
        self.assertFalse(d.proceed)
        self.assertTrue(d.late)
        self.assertIn("too late", d.reason)

    def test_cutoff_is_half_open(self):
        self.assertTrue(gate(et(8, 28, 10, 59)).proceed)
        self.assertFalse(gate(et(8, 28, 11, 0)).proceed)


class StubReports(unittest.TestCase):
    """A skeleton left by a dying synthesis is not today's work.

    2026-08-28 shipped {"data_quality_notes": "Synthesis in progress.",
    "recommendations": []} to the Sheet, and because the file existed every
    later check treated the day as done.
    """

    def test_stub_is_retried_while_the_window_is_open(self):
        d = gate(et(8, 28, 7, 5), state="stub")
        self.assertTrue(d.proceed)
        self.assertIn("only a stub", d.reason)

    def test_stub_past_the_cutoff_alarms_rather_than_running(self):
        d = gate(et(8, 28, 12, 30), state="stub")
        self.assertFalse(d.proceed)
        self.assertTrue(d.late)
        self.assertIn("nothing usable", d.reason)

    def test_missing_past_the_cutoff_says_so_differently(self):
        d = gate(et(8, 28, 12, 30), state="missing")
        self.assertTrue(d.late)
        self.assertIn("no report was published", d.reason)

    def test_a_stub_before_the_window_is_still_the_wrong_arm(self):
        self.assertFalse(gate(et(1, 15, 5, 1), state="stub").proceed)


class ManualRuns(unittest.TestCase):
    """The duplicate guard exists to stop the scheduler, not the operator."""

    def test_dispatch_runs_outside_the_window(self):
        self.assertTrue(gate(et(8, 27, 16, 30), event="workflow_dispatch").proceed)

    def test_dispatch_runs_even_when_a_report_exists(self):
        d = gate(et(8, 27, 16, 30), event="workflow_dispatch", state="published")
        self.assertTrue(d.proceed)

    def test_date_is_the_et_date(self):
        # 20:30 UTC on the 27th is still the 27th in ET; 01:00 UTC is not.
        self.assertEqual(gate(et(8, 27, 16, 30)).date, "2026-08-27")


if __name__ == "__main__":
    unittest.main()
