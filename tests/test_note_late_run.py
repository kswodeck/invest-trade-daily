#!/usr/bin/env python3
"""Tests for stamping a late report with when it was actually researched.

The 6-11 ET window exists so a late delivery still produces a report. The cost
is that the report can be researched mid-session while reading like the 6am
pre-open view — these cases are the ones that must not go out unlabelled.
"""

from __future__ import annotations

import sys
import unittest
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from note_late_run import MARKER, note_for, session_at, stamp  # noqa: E402

ET = ZoneInfo("America/New_York")


def at(day: int, hour: int, minute: int = 0) -> datetime:
    return datetime(2026, 8, day, hour, minute, tzinfo=ET)


class WhenToStamp(unittest.TestCase):
    def test_the_six_am_slot_is_not_stamped(self):
        self.assertIsNone(note_for(at(31, 6, 2)))

    def test_ordinary_scheduler_slippage_is_not_narrated(self):
        # 25-38 minutes late was the norm for two weeks; saying so daily is noise.
        self.assertIsNone(note_for(at(31, 6, 38)))
        self.assertIsNone(note_for(at(31, 7, 30)))

    def test_just_past_the_deadline_is_stamped(self):
        note = note_for(at(31, 7, 31))
        self.assertIsNotNone(note)
        self.assertIn("before the open", note)

    def test_a_weekday_run_at_the_observed_delay_is_stamped_mid_session(self):
        # Mon 2026-08-31 at the 4h42m delay seen on the 29th and 30th.
        note = note_for(at(31, 10, 42))
        self.assertIn("10:42 ET", note)
        self.assertIn("during the regular session", note)
        self.assertIn("market already trading", note)

    def test_the_real_2026_08_30_run_was_a_sunday_and_says_so(self):
        # Delivered 14:42Z = 10:42 ET, published just before noon — but on a
        # Sunday, so "mid-session" would be wrong and the weekend wording wins.
        note = note_for(at(30, 10, 42))
        self.assertIn("10:42 ET", note)
        self.assertIn("weekend", note)
        self.assertIn("later than the 6am pre-open slot", note)


class Sessions(unittest.TestCase):
    def test_boundaries(self):
        self.assertEqual(session_at(at(31, 9, 29)), "before the open")
        self.assertEqual(session_at(at(31, 9, 30)), "during the regular session")
        self.assertEqual(session_at(at(31, 15, 59)), "during the regular session")
        self.assertEqual(session_at(at(31, 16, 0)), "after the close")

    def test_weekend_runs_say_so(self):
        # 2026-08-29 and 30 were a Saturday and Sunday; the report still runs.
        self.assertIn("weekend", session_at(at(29, 10, 56)))


class Stamping(unittest.TestCase):
    def test_prepends_and_keeps_the_existing_notes(self):
        report = {"data_quality_notes": "Two sources were unreachable."}
        self.assertTrue(stamp(report, at(31, 10, 42)))
        notes = report["data_quality_notes"]
        self.assertTrue(notes.startswith(MARKER))
        self.assertIn("Two sources were unreachable.", notes)

    def test_is_idempotent(self):
        report = {"data_quality_notes": "x"}
        self.assertTrue(stamp(report, at(31, 10, 42)))
        once = report["data_quality_notes"]
        self.assertFalse(stamp(report, at(31, 10, 42)))
        self.assertEqual(report["data_quality_notes"], once)

    def test_timely_run_leaves_the_report_untouched(self):
        report = {"data_quality_notes": "x"}
        self.assertFalse(stamp(report, at(31, 6, 5)))
        self.assertEqual(report["data_quality_notes"], "x")

    def test_handles_a_report_with_no_notes_field(self):
        report = {}
        self.assertTrue(stamp(report, at(31, 10, 42)))
        self.assertTrue(report["data_quality_notes"].startswith(MARKER))


if __name__ == "__main__":
    unittest.main()
