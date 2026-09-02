"""Performance tracker: grading, and the figures the Sheet actually shows.

The scorecard is spreadsheet formulas, so these tests render the detail table
the way `publish_sheets` renders it and then evaluate those formulas against it
with `tests/sheet_formula.py`. That is deliberate: every accounting bug this
suite was written for rendered perfectly and simply reported a wrong number.
"""

from __future__ import annotations

import sys
import unittest
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
sys.path.insert(0, str(REPO / "tests"))

import publish_sheets as ps  # noqa: E402
from sheet_formula import Sheet  # noqa: E402


def position(**overrides) -> dict:
    base = {
        "opened": "2026-08-20", "instrument": "Test Co", "symbol": "TST",
        "asset_class": "stock", "venue": "Robinhood Stocks", "direction": "buy",
        "horizon": "swing", "unit": "usd", "entry": 100.0, "target": 120.0,
        "stop": 94.0, "conviction": 3, "status": ps.PENDING,
        "days_open": 0, "days_since_published": 0, "reference_price": 104.0,
    }
    base.update(overrides)
    return base


# One book with a known answer to every figure on the tab. Nine graded rows —
# 1 target, 2 stopped, 2 open, 3 pending, 1 never filled — plus two rows the
# scorecard must ignore entirely.
BOOK = [
    position(symbol="WIN", status=ps.TARGET_HIT, filled_date="2026-08-21",
             fill_price=100.0, closed="2026-08-28", exit_price=120.0,
             pct_vs_entry=10.0, days_open=7),
    position(symbol="LOSE1", status=ps.STOPPED, filled_date="2026-08-21",
             fill_price=100.0, closed="2026-08-25", exit_price=97.0,
             pct_vs_entry=-3.0, days_open=4),
    position(symbol="LOSE2", status=ps.STOPPED, filled_date="2026-08-21",
             fill_price=100.0, closed="2026-08-24", exit_price=95.0,
             pct_vs_entry=-5.0, days_open=3, horizon="long_term"),
    position(symbol="OPEN1", status=ps.OPEN, filled_date="2026-08-22",
             fill_price=100.0, pct_vs_entry=4.0, days_open=9),
    position(symbol="OPEN2", status=ps.OPEN, filled_date="2026-08-22",
             fill_price=100.0, pct_vs_entry=-2.0, days_open=9, asset_class="etf"),
    position(symbol="WAIT1"),
    position(symbol="WAIT2", entry=110.0),           # above the market: a breakout
    position(symbol="WAIT3", reference_price=None),  # no reference: unknown style
    position(symbol="MISSED", status=ps.NOT_FILLED, closed="2026-08-30"),
    # Ungraded: no quote source, and a contract-month basis error respectively.
    position(symbol="KXEVENT", asset_class="event", unit="cents"),
    position(symbol="/MESU6", asset_class="futures", status=ps.OPEN,
             filled_date="2026-08-21", fill_price=100.0, pct_vs_entry=50.0,
             days_open=12),
]

FIRST_ROW = 30  # arbitrary, to catch a formula that assumes the table starts at 1


class ScorecardFigures(unittest.TestCase):
    """Evaluate the emitted formulas against the emitted rows."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.block, cls.formats = ps.cumulative_rows(BOOK, FIRST_ROW)
        cls.sheet = Sheet([ps.perf_row(p) for p in BOOK], FIRST_ROW)
        cls.labelled = {}
        for row in cls.block:
            if row and isinstance(row[0], str) and len(row) > 1:
                cls.labelled[row[0]] = row

    def value(self, label: str, column: int = 1):
        self.assertIn(label, self.labelled, f"no scorecard row labelled {label!r}")
        return self.sheet.evaluate(self.labelled[label][column])

    def find(self, prefix: str) -> list:
        for label, row in self.labelled.items():
            if label.startswith(prefix):
                return row
        self.fail(f"no scorecard row starting {prefix!r}")

    # -- the headline figures ---------------------------------------------

    def test_average_per_idea_is_realized_over_closed_trades(self):
        # (+10 - 3 - 5) / 3 closed. The futures +50 must not appear.
        self.assertAlmostEqual(self.value("Average per idea — the equal-weight return"),
                               2.0 / 3, places=6)

    def test_average_per_idea_unrealized_covers_open_positions_only(self):
        row = self.find("Average per idea")
        self.assertAlmostEqual(self.sheet.evaluate(row[2]), 1.0, places=6)

    def test_average_per_idea_combined_divides_by_marked_rows(self):
        # (10 - 3 - 5 + 4 - 2) / 5 rows carrying a mark.
        row = self.find("Average per idea")
        self.assertAlmostEqual(self.sheet.evaluate(row[3]), 0.8, places=6)

    def test_closed_counts_exclude_pending_and_never_filled(self):
        """The bug this whole file exists for: pending rows counted as closed."""
        row = self.find("Closed: target / stopped / expired")
        target, stopped, expired = (self.sheet.evaluate(cell) for cell in row[1:4])
        self.assertEqual((target, stopped, expired), (1.0, 2.0, 0.0))

    def test_hit_rate_is_targets_over_closed(self):
        self.assertAlmostEqual(self.value("Hit rate (closed that reached target)"),
                               1 / 3, places=6)

    def test_fill_rate_counts_only_setups_that_became_positions(self):
        # 2 open + 3 closed of 9 graded setups.
        self.assertAlmostEqual(self.value("Fill rate (setups that reached their entry)"),
                               5 / 9, places=6)

    def test_average_days_held_ignores_setups_that_never_filled(self):
        # (7 + 4 + 3 + 9 + 9) / 5 — not diluted by four unfilled rows.
        self.assertAlmostEqual(self.value("Average days held (filled positions only)"),
                               32 / 5, places=6)

    def test_best_and_worst_exclude_ungraded_rows(self):
        row = self.find("Best / worst")
        self.assertEqual(self.sheet.evaluate(row[1]), 10.0)  # not the futures +50
        self.assertEqual(self.sheet.evaluate(row[2]), -5.0)

    def test_open_positions_up_and_down(self):
        row = self.find("Open positions up / down")
        self.assertEqual(self.sheet.evaluate(row[1]), 1.0)
        self.assertEqual(self.sheet.evaluate(row[2]), 1.0)

    def test_header_line_counts_every_bucket(self):
        rendered = self.sheet.evaluate(self.block[2][0])
        for fragment in ("Graded setups: 9", "filled and open: 2", "closed: 3",
                         "awaiting entry: 3", "never filled: 1",
                         "ungraded (event / futures): 2"):
            self.assertIn(fragment, rendered)

    # -- fill quality ------------------------------------------------------

    def test_fill_quality_splits_by_entry_style(self):
        pullback = self.find("pullback")
        self.assertEqual(self.sheet.evaluate(pullback[1]), 7.0)   # setups
        self.assertEqual(self.sheet.evaluate(pullback[2]), 5.0)   # filled
        breakout = self.find("breakout")
        self.assertEqual(self.sheet.evaluate(breakout[1]), 1.0)
        self.assertEqual(self.sheet.evaluate(breakout[2]), 0.0)

    # -- breakdowns --------------------------------------------------------

    def test_breakdown_closed_column_matches_the_top_block(self):
        """Every by-X table derived closed as `ideas - open`, counting pending."""
        swing = self.find("swing")
        self.assertEqual(self.sheet.evaluate(swing[1]), 8.0)  # graded swing ideas
        self.assertEqual(self.sheet.evaluate(swing[2]), 2.0)  # WIN and LOSE1 only

    def test_breakdown_average_realized_divides_by_real_closed_count(self):
        swing = self.find("swing")
        self.assertAlmostEqual(self.sheet.evaluate(swing[4]), 3.5, places=6)  # (10-3)/2

    def test_breakdown_excludes_ungraded_asset_classes(self):
        self.assertNotIn("FUTURES", self.labelled)
        self.assertNotIn("EVENT", self.labelled)

    def test_headline_offset_points_at_the_average_row(self):
        self.assertTrue(self.block[ps.HEADLINE_OFFSET][0].startswith("Average per idea"))

    def test_every_formatted_cell_exists_and_holds_a_formula(self):
        for offset, column, _kind in self.formats:
            row = self.block[offset]
            self.assertGreater(len(row), column, f"row {offset} has no column {column}")
            self.assertTrue(str(row[column]).startswith("="),
                            f"row {offset} column {column} is not a formula")


class Grading(unittest.TestCase):
    def test_open_without_a_fill_is_demoted_to_pending(self):
        """11 legacy rows sat `open` with no fill, inflating every open figure."""
        stale = position(symbol="LEGACY", status=ps.OPEN, asset_class="event")
        graded = ps.grade_position(dict(stale), date(2026, 9, 2))
        self.assertEqual(graded["status"], ps.PENDING)

    def test_a_real_fill_keeps_its_open_status(self):
        live = position(symbol="REAL", status=ps.OPEN, asset_class="event",
                        filled_date="2026-08-21", fill_price=100.0)
        graded = ps.grade_position(dict(live), date(2026, 9, 2))
        self.assertEqual(graded["status"], ps.OPEN)

    def test_a_closed_position_is_never_regraded(self):
        closed = position(symbol="DONE", status=ps.STOPPED, closed="2026-08-25",
                          exit_price=94.0, pct_vs_entry=-6.0)
        self.assertEqual(ps.grade_position(dict(closed), date(2026, 9, 2)),
                         closed)


class EntryStyle(unittest.TestCase):
    def test_long_below_the_market_is_a_pullback(self):
        self.assertEqual(ps.entry_style(position(entry=100.0, reference_price=104.0)),
                         "pullback")

    def test_long_above_the_market_is_a_breakout(self):
        self.assertEqual(ps.entry_style(position(entry=110.0, reference_price=104.0)),
                         "breakout")

    def test_short_above_the_market_is_a_pullback(self):
        """Selling into a bounce is the same adverse selection, mirrored."""
        self.assertEqual(
            ps.entry_style(position(direction="sell_short", entry=110.0,
                                    reference_price=104.0)),
            "pullback")

    def test_short_below_the_market_is_a_breakout(self):
        self.assertEqual(
            ps.entry_style(position(direction="sell_short", entry=100.0,
                                    reference_price=104.0)),
            "breakout")

    def test_missing_reference_price_is_unknown(self):
        self.assertEqual(ps.entry_style(position(reference_price=None)), "unknown")


class GradeableClasses(unittest.TestCase):
    def test_event_and_futures_are_not_graded(self):
        self.assertFalse(ps.is_graded(position(asset_class="event")))
        self.assertFalse(ps.is_graded(position(asset_class="futures")))

    def test_equities_etfs_and_crypto_are_graded(self):
        for asset_class in ("stock", "etf", "crypto"):
            self.assertTrue(ps.is_graded(position(asset_class=asset_class)))


class CompoundedReturn(unittest.TestCase):
    def test_compounds_closed_trades_in_close_order(self):
        # LOSE2 closed 08-24, LOSE1 08-25, WIN 08-28 — and float multiplication
        # is not associative, so the order is part of the answer, not a detail.
        expected = round((0.95 * 0.97 * 1.10 - 1) * 100, 2)
        self.assertEqual(ps.compounded_return(BOOK), expected)

    def test_a_full_loss_and_a_double_do_not_cancel(self):
        """Averaging says flat; compounding says you have half your money."""
        book = [
            position(symbol="DOUBLE", status=ps.TARGET_HIT, filled_date="2026-08-01",
                     closed="2026-08-10", pct_vs_entry=100.0),
            position(symbol="HALVED", status=ps.STOPPED, filled_date="2026-08-01",
                     closed="2026-08-11", pct_vs_entry=-50.0),
        ]
        self.assertEqual(ps.compounded_return(book), 0.0)

    def test_ignores_open_pending_and_ungraded_rows(self):
        only_open = [p for p in BOOK if p["status"] in (ps.OPEN, ps.PENDING)]
        self.assertIsNone(ps.compounded_return(only_open))

    def test_is_not_a_sum_of_percentages(self):
        """The figure this replaced added percentages together and called it a return."""
        closed = [p for p in BOOK if p["status"] in ps.CLOSED_STATUSES and ps.is_graded(p)]
        naive_sum = sum(p["pct_vs_entry"] for p in closed)
        self.assertNotAlmostEqual(ps.compounded_return(BOOK), naive_sum, places=2)


class Scorecard(unittest.TestCase):
    def test_reports_distinct_theses_alongside_row_count(self):
        line = ps.summarize(BOOK)[0]
        self.assertIn("9 graded rows from 9 distinct theses", line)

    def test_repeated_theses_collapse_in_the_thesis_count(self):
        repeated = BOOK + [position(symbol="WIN", opened="2026-08-27"),
                           position(symbol="WIN", opened="2026-08-28")]
        self.assertIn("11 graded rows from 9 distinct theses", ps.summarize(repeated)[0])


if __name__ == "__main__":
    unittest.main()
