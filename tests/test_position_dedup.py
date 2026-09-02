"""One live position per idea, and what happens when it is re-pitched.

The tracker opened a fresh row every time an idea was published, so a thesis
carried for a fortnight became a fortnight of rows and every average counted
the same losing call repeatedly. These cover the rule that replaced it:

    One live position per (symbol, direction). Republished while live, it is an
    amendment. Republished after it closed, it is a new trade with its own row.

The subtle half is grading. Amended levels take effect from the day they were
published, so a stop moved on the 20th governs the 20th onward — grading the
whole history against the final stop would rewrite the sessions before it.
"""

from __future__ import annotations

import sys
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import dedupe_positions as dd  # noqa: E402
import publish_sheets as ps  # noqa: E402


def position(**overrides) -> dict:
    base = {
        "opened": "2026-08-20", "instrument": "Test Co", "symbol": "TST",
        "asset_class": "stock", "venue": "Robinhood Stocks", "direction": "buy",
        "horizon": "swing", "unit": "usd", "entry": 100.0, "target": 120.0,
        "stop": 90.0, "conviction": 3, "status": ps.PENDING,
        "reference_price": 104.0, "days_open": 0, "days_since_published": 0,
    }
    base.update(overrides)
    return base


def report(date_: str, *ideas: dict) -> dict:
    return {"date": date_, "recommendations": list(ideas)}


def recommendation(**overrides) -> dict:
    base = {
        "symbol": "TST", "instrument": "Test Co", "asset_class": "stock",
        "venue": "Robinhood Stocks", "direction": "buy", "horizon": "swing",
        "conviction": 3, "entry": {"ideal": 100.0}, "exit": {"target": 120.0},
        "stop": 90.0, "last_price": 104.0, "catalyst": {"event": "x", "action": "y"},
    }
    base.update(overrides)
    return base


def bars(*rows: tuple[str, float, float]) -> dict:
    """(date, low, high) triples as a market_data.history payload."""
    return {"ok": True, "recent": [
        {"date": d, "o": (l + h) / 2, "h": h, "l": l, "c": (l + h) / 2, "v": 1e6}
        for d, l, h in rows]}


class MergingTodaysReport(unittest.TestCase):
    def test_a_new_idea_opens_a_position(self):
        positions: list[dict] = []
        opened, amended = ps.merge_report(positions, report("2026-08-20", recommendation()))
        self.assertEqual((opened, amended), (1, 0))
        self.assertEqual(len(positions), 1)

    def test_re_pitching_a_live_idea_amends_it_rather_than_opening_a_second(self):
        positions = [position()]
        opened, amended = ps.merge_report(
            positions, report("2026-08-24", recommendation(stop=88.0)))
        self.assertEqual((opened, amended), (0, 1))
        self.assertEqual(len(positions), 1)
        self.assertEqual(positions[0]["stop"], 88.0)
        self.assertEqual(positions[0]["opened"], "2026-08-20")  # identity is the first day

    def test_re_pitching_at_unchanged_levels_records_nothing(self):
        """EEM went out three mornings at the same 65.60. That is one idea."""
        positions = [position()]
        opened, amended = ps.merge_report(positions, report("2026-08-24", recommendation()))
        self.assertEqual((opened, amended), (0, 0))
        self.assertNotIn("amendments", positions[0])
        self.assertEqual(positions[0]["last_seen"], "2026-08-24")

    def test_the_same_idea_after_a_close_is_a_new_trade(self):
        """A name worth trading twice is counted twice."""
        positions = [position(status=ps.STOPPED, closed="2026-08-25",
                              filled_date="2026-08-21", pct_vs_entry=-10.0)]
        opened, amended = ps.merge_report(
            positions, report("2026-08-27", recommendation(entry={"ideal": 92.0})))
        self.assertEqual((opened, amended), (1, 0))
        self.assertEqual(len(positions), 2)
        self.assertEqual(positions[1]["opened"], "2026-08-27")
        self.assertEqual(positions[0]["pct_vs_entry"], -10.0)  # the first trade stands

    def test_the_other_side_of_the_same_symbol_is_its_own_position(self):
        positions = [position()]
        ps.merge_report(positions, report("2026-08-24", recommendation(direction="sell_short")))
        self.assertEqual(len(positions), 2)

    def test_an_idea_waiting_for_its_catalyst_is_not_tracked_at_all(self):
        positions: list[dict] = []
        waiting = recommendation(catalyst={"event": "CPI", "action": "wait", "wait": True})
        self.assertEqual(ps.merge_report(positions, report("2026-08-20", waiting)), (0, 0))
        self.assertEqual(positions, [])

    def test_publishing_twice_in_one_day_does_not_double_count(self):
        positions: list[dict] = []
        today = report("2026-08-20", recommendation())
        ps.merge_report(positions, today)
        opened, amended = ps.merge_report(positions, today)
        self.assertEqual((opened, amended), (0, 0))
        self.assertEqual(len(positions), 1)


class Amending(unittest.TestCase):
    def test_an_unfilled_setup_can_have_every_level_revised(self):
        pos = position()
        ps.apply_amendment(pos, {"entry": 97.0, "target": 118.0, "stop": 88.0,
                                 "reference_price": 99.0}, "2026-08-24")
        self.assertEqual((pos["entry"], pos["target"], pos["stop"]), (97.0, 118.0, 88.0))

    def test_a_filled_position_keeps_the_entry_it_was_filled_at(self):
        """You bought at a price. Revising it would rewrite the fill."""
        pos = position(status=ps.OPEN, filled_date="2026-08-21", fill_price=100.0)
        ps.apply_amendment(pos, {"entry": 97.0, "target": 125.0, "stop": 95.0}, "2026-08-24")
        self.assertEqual(pos["entry"], 100.0)
        self.assertEqual(pos["stop"], 95.0)
        self.assertEqual(pos["fill_price"], 100.0)

    def test_the_history_keeps_every_revision_with_its_date(self):
        pos = position()
        ps.apply_amendment(pos, {"entry": 100.0, "target": 120.0, "stop": 94.0}, "2026-08-22")
        ps.apply_amendment(pos, {"entry": 100.0, "target": 120.0, "stop": 96.0}, "2026-08-24")
        self.assertEqual([a["date"] for a in pos["amendments"]],
                         ["2026-08-20", "2026-08-22", "2026-08-24"])
        self.assertEqual(pos["last_amended"], "2026-08-24")

    def test_conviction_and_size_follow_the_most_recent_view(self):
        pos = position(conviction=2)
        ps.apply_amendment(pos, {"entry": 100.0, "target": 120.0, "stop": 88.0,
                                 "conviction": 4, "position_size_pct": 3.0}, "2026-08-24")
        self.assertEqual(pos["conviction"], 4)
        self.assertEqual(pos["position_size_pct"], 3.0)


class LevelsInForce(unittest.TestCase):
    AMENDED = position(amendments=[
        {"date": "2026-08-20", "entry": 100.0, "target": 120.0, "stop": 90.0},
        {"date": "2026-08-24", "entry": 100.0, "target": 120.0, "stop": 96.0},
    ], stop=96.0)

    def test_before_the_revision_the_original_stop_stands(self):
        self.assertEqual(ps.levels_in_force(self.AMENDED, "2026-08-22")[2], 90.0)

    def test_on_the_day_of_the_revision_the_new_stop_applies(self):
        self.assertEqual(ps.levels_in_force(self.AMENDED, "2026-08-24")[2], 96.0)

    def test_after_the_revision_the_new_stop_stands(self):
        self.assertEqual(ps.levels_in_force(self.AMENDED, "2026-09-01")[2], 96.0)

    def test_a_position_never_amended_uses_its_flat_levels(self):
        self.assertEqual(ps.levels_in_force(position(), "2026-08-25"),
                         (100.0, 120.0, 90.0, 104.0))

    def test_a_date_before_the_first_record_falls_back_to_the_opening_levels(self):
        self.assertEqual(ps.levels_in_force(self.AMENDED, "2026-08-01")[2], 90.0)


class GradingAgainstAmendedLevels(unittest.TestCase):
    """The reason amendments are dated rather than overwritten."""

    def grade(self, pos: dict, history: dict, today: date) -> dict:
        with mock.patch.dict(sys.modules):
            fake = mock.MagicMock()
            fake.history.return_value = history
            fake.quote.return_value = {"ok": False}
            fake.crypto.return_value = {"ok": False}
            sys.modules["market_data"] = fake
            return ps.grade_position(dict(pos), today)

    def test_a_stop_moved_up_does_not_stop_the_trade_out_retroactively(self):
        """The 21st traded to 95. The stop only reached 96 on the 24th."""
        pos = position(amendments=[
            {"date": "2026-08-20", "entry": 100.0, "target": 120.0, "stop": 90.0,
             "reference_price": 104.0},
            {"date": "2026-08-24", "entry": 100.0, "target": 120.0, "stop": 96.0,
             "reference_price": 104.0},
        ], stop=96.0)
        history = bars(("2026-08-20", 101.0, 105.0),   # no fill yet
                       ("2026-08-21", 95.0, 102.0),    # fills at 100, low 95
                       ("2026-08-22", 97.0, 101.0),    # under the later stop, not the current one
                       ("2026-08-25", 94.0, 99.0))     # now 96 is in force — stopped
        graded = self.grade(pos, history, date(2026, 8, 26))
        self.assertEqual(graded["filled_date"], "2026-08-21")
        self.assertEqual(graded["status"], ps.STOPPED)
        self.assertEqual(graded["closed"], "2026-08-25")
        self.assertEqual(graded["exit_price"], 96.0)

    def test_the_original_stop_still_governs_the_days_it_was_in_force(self):
        pos = position(amendments=[
            {"date": "2026-08-20", "entry": 100.0, "target": 120.0, "stop": 90.0,
             "reference_price": 104.0},
            {"date": "2026-08-24", "entry": 100.0, "target": 120.0, "stop": 96.0,
             "reference_price": 104.0},
        ], stop=96.0)
        history = bars(("2026-08-21", 95.0, 102.0),
                       ("2026-08-22", 89.0, 96.0))     # through 90 while 90 was the stop
        graded = self.grade(pos, history, date(2026, 8, 23))
        self.assertEqual(graded["status"], ps.STOPPED)
        self.assertEqual(graded["closed"], "2026-08-22")
        self.assertEqual(graded["exit_price"], 90.0)

    def test_an_entry_revised_before_the_fill_is_the_one_that_fills(self):
        pos = position(entry=97.0, amendments=[
            {"date": "2026-08-20", "entry": 100.0, "target": 120.0, "stop": 90.0,
             "reference_price": 104.0},
            {"date": "2026-08-22", "entry": 97.0, "target": 120.0, "stop": 90.0,
             "reference_price": 104.0},
        ])
        history = bars(("2026-08-20", 101.0, 105.0),
                       ("2026-08-23", 96.5, 99.0))
        graded = self.grade(pos, history, date(2026, 8, 24))
        self.assertEqual(graded["filled_date"], "2026-08-23")
        self.assertEqual(graded["fill_price"], 97.0)

    def test_an_actively_re_pitched_idea_is_not_timed_out_on_its_first_appearance(self):
        """XLE was still being published on day 18 of a 45-day clock."""
        pos = position(opened="2026-06-01", last_seen="2026-09-01",
                       amendments=[
                           {"date": "2026-06-01", "entry": 100.0, "target": 120.0, "stop": 90.0},
                           {"date": "2026-09-01", "entry": 99.0, "target": 120.0, "stop": 90.0},
                       ], entry=99.0)
        graded = self.grade(pos, {"ok": False}, date(2026, 9, 2))
        self.assertEqual(graded["status"], ps.PENDING)

    def test_an_idea_nobody_has_pitched_in_months_still_times_out(self):
        pos = position(opened="2026-06-01", last_seen="2026-06-01")
        graded = self.grade(pos, {"ok": False}, date(2026, 9, 2))
        self.assertEqual(graded["status"], ps.NOT_FILLED)


class MigratingStoredHistory(unittest.TestCase):
    def test_a_run_of_re_pitches_collapses_to_one_position(self):
        rows = [position(opened="2026-08-15", stop=94.0),
                position(opened="2026-08-17", stop=95.4),
                position(opened="2026-08-18", stop=95.2)]
        out, _ = dd.dedupe(rows)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]["opened"], "2026-08-15")
        self.assertEqual(out[0]["stop"], 95.2)
        self.assertEqual([a["stop"] for a in out[0]["amendments"]], [94.0, 95.4, 95.2])

    def test_a_re_pitch_after_a_close_stays_a_separate_position(self):
        rows = [position(opened="2026-08-15", status=ps.STOPPED, closed="2026-08-20"),
                position(opened="2026-08-25")]
        out, _ = dd.dedupe(rows)
        self.assertEqual(len(out), 2)
        self.assertEqual(out[0]["status"], ps.STOPPED)  # the closed trade is untouched

    def test_merged_positions_drop_their_grades_for_regrading(self):
        """The recorded outcome was computed against levels that later moved."""
        rows = [position(opened="2026-08-15", status=ps.STOPPED, closed="2026-08-25",
                         filled_date="2026-08-18", pct_vs_entry=-3.39, stop=94.0),
                position(opened="2026-08-18", stop=95.2)]
        out, _ = dd.dedupe(rows)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]["status"], ps.PENDING)
        for field in ("filled_date", "closed", "pct_vs_entry", "exit_price"):
            self.assertNotIn(field, out[0])

    def test_unchanged_re_pitches_leave_no_revision_history(self):
        rows = [position(opened="2026-08-21"), position(opened="2026-08-22"),
                position(opened="2026-08-23")]
        out, _ = dd.dedupe(rows)
        self.assertEqual(len(out), 1)
        self.assertNotIn("amendments", out[0])
        self.assertEqual(out[0]["last_seen"], "2026-08-23")

    def test_the_two_sides_of_a_symbol_never_merge(self):
        rows = [position(direction="buy"), position(direction="sell_short")]
        self.assertEqual(len(dd.dedupe(rows)[0]), 2)

    def test_running_it_twice_changes_nothing(self):
        rows = [position(opened="2026-08-15", stop=94.0),
                position(opened="2026-08-18", stop=95.2)]
        once, _ = dd.dedupe(rows)
        twice, _ = dd.dedupe(once)
        self.assertEqual(once, twice)


if __name__ == "__main__":
    unittest.main()
