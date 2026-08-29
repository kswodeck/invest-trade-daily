#!/usr/bin/env python3
"""Tests for classifying a report as missing, stub, or published.

The published/stub boundary decides whether a morning gets retried, so the
cases here are drawn from real report.json files rather than invented shapes.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from report_state import MISSING, PUBLISHED, STUB, classify, classify_text  # noqa: E402

# reports/2026-08-28/report.json exactly as it was published to the Sheet.
SYNTHESIS_SKELETON = {
    "date": "2026-08-28",
    "generated_at_et": "2026-08-28T12:21:28-04:00",
    "truncated": True,
    "data_quality_notes": "Synthesis in progress.",
    "market_context": {"summary": "Synthesis in progress.", "regime": "unknown"},
    "recommendations": [],
}


class Classify(unittest.TestCase):
    def test_the_2026_08_28_skeleton_is_a_stub(self):
        self.assertEqual(classify(SYNTHESIS_SKELETON), STUB)

    def test_ensure_report_stub_is_recognised_by_its_own_marker(self):
        # Carries the flag even though a stub may gain a watchlist later.
        stub = dict(SYNTHESIS_SKELETON, pipeline_failure=True, watchlist=[{"symbol": "SPY"}])
        self.assertEqual(classify(stub), STUB)

    def test_a_report_with_recommendations_is_published(self):
        report = dict(SYNTHESIS_SKELETON, recommendations=[{"symbol": "NVDA"}])
        self.assertEqual(classify(report), PUBLISHED)

    def test_watchlist_only_still_counts_as_published(self):
        # A thin day that honestly found nothing to trade but something to watch
        # is a real result, not a failure — don't re-run it.
        report = dict(SYNTHESIS_SKELETON, watchlist=[{"symbol": "SPY"}])
        self.assertEqual(classify(report), PUBLISHED)

    def test_nothing_at_all_is_a_stub(self):
        self.assertEqual(classify({"recommendations": [], "watchlist": []}), STUB)

    def test_absent_report_is_missing(self):
        self.assertEqual(classify(None), MISSING)


class ClassifyText(unittest.TestCase):
    """Whatever the caller pipes in, the answer has to be actionable."""

    def test_absent_is_missing_but_empty_is_a_stub(self):
        self.assertEqual(classify_text(None), MISSING)
        self.assertEqual(classify_text(""), STUB)
        self.assertEqual(classify_text("   \n"), STUB)

    def test_unparseable_is_a_stub_not_missing(self):
        # Something wrote it; it still needs replacing before publish reads it.
        self.assertEqual(classify_text("{not json"), STUB)
        self.assertEqual(classify_text("[1, 2, 3]"), STUB)

    def test_round_trips_real_json(self):
        import json

        self.assertEqual(classify_text(json.dumps(SYNTHESIS_SKELETON)), STUB)


if __name__ == "__main__":
    unittest.main()
