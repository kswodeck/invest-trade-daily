#!/usr/bin/env python3
"""Tests for who gets told about an odd-lot offer, and how often.

    python -m unittest tests.test_odd_lot_notify -v

The dedupe rule is the whole design. The screener re-scores its entire universe
twice a day, so an alert keyed on the offer alone would fire twice a day for as
long as the offer stayed open — and an alert that arrives every day is one you
stop reading, which costs more than the alert was ever worth. Keyed on
`(accession, tier)` instead: a new qualifying offer speaks once, an upgrade
speaks again because that is news, and nothing else speaks at all.
"""

from __future__ import annotations

import json
import sys
import unittest
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import notify_odd_lot as notify  # noqa: E402
from odd_lot import (  # noqa: E402
    notifications_due, notifications_to_close, record_notified,
)

ET = ZoneInfo("America/New_York")
CONFIG = json.loads((REPO / "config" / "odd_lot.json").read_text())
NOW = datetime(2026, 9, 3, 5, 37, tzinfo=ET)


def offer(tier: str | None, *, accession: str = "0001-26-000001",
          status: str = "candidate", **kwargs) -> dict:
    return {
        "accession": accession, "cik": "0000320193", "company": "Acme Corp",
        "ticker": "ACME", "form": "SC TO-I", "filed": "2026-09-01",
        "document": "offer.htm", "url": "https://example.invalid/offer.htm",
        "index_url": "https://example.invalid/index.htm",
        "status": status, "tier": tier, "rejections": [], "risk_flags": [],
        "warnings": [], "offer_price": 10.0, "market_price": 9.5,
        "spread_pct": 0.0526, "annualized": 0.64, "capital": 940.5,
        "gross_profit": 49.5, "expiration_date": "2026-10-03",
        "days_to_expiry": 30, "withdrawal_deadline": "2026-10-03",
        "withdrawal_basis": "expiration_date", "avg_volume_30d": 500_000,
        "odd_lot_paragraph": "Holders of fewer than 100 Shares who tender all of "
                             "them will be accepted before proration.",
        "last_scored": "2026-09-03", **kwargs,
    }


def universe(*entries: dict, archive: list[dict] | None = None) -> dict:
    return {"open": list(entries), "archive": list(archive or [])}


class WhoGetsAnnounced(unittest.TestCase):
    def due(self, *entries: dict, **kwargs) -> list[str]:
        return [e["ticker"] for e in notifications_due(universe(*entries, **kwargs), CONFIG)]

    def test_tier_a_and_b_are_announced(self):
        self.assertEqual(self.due(offer("A")), ["ACME"])
        self.assertEqual(self.due(offer("B")), ["ACME"])

    def test_tier_c_is_not_announced(self):
        """C is informational by definition — it carries a material flag."""
        self.assertEqual(self.due(offer("C")), [])

    def test_a_rejected_offer_is_never_announced(self):
        self.assertEqual(self.due(offer("A", status="rejected")), [])
        self.assertEqual(self.due(offer(None, status="rejected")), [])

    def test_a_deferred_offer_is_not_announced(self):
        """The SEC blocked the fetch; we do not know what the offer says."""
        self.assertEqual(self.due(offer(None, status="deferred")), [])


class ItOnlySpeaksOnce(unittest.TestCase):
    def test_an_announced_offer_is_not_announced_again(self):
        entry = record_notified(offer("A"), issue=7, now=NOW)
        self.assertEqual(notifications_due(universe(entry), CONFIG), [])

    def test_re_scoring_twice_a_day_does_not_re_announce(self):
        """The failure mode this rule exists for."""
        entry = offer("B")
        for run in range(6):  # three days, two slots each
            due = notifications_due(universe(entry), CONFIG)
            if due:
                record_notified(due[0], issue=7, now=NOW)
            with self.subTest(run=run):
                self.assertEqual(len(due), 1 if run == 0 else 0)

    def test_an_upgrade_from_b_to_a_speaks_again(self):
        """"the B I mentioned is now an A" is news."""
        entry = record_notified(offer("B"), issue=7, now=NOW)
        entry["tier"] = "A"
        self.assertEqual([e["ticker"] for e in notifications_due(universe(entry), CONFIG)],
                         ["ACME"])

    def test_a_downgrade_from_a_to_b_stays_quiet(self):
        """You already know about the offer; the tab carries the current state."""
        entry = record_notified(offer("A"), issue=7, now=NOW)
        entry["tier"] = "B"
        self.assertEqual(notifications_due(universe(entry), CONFIG), [])

    def test_a_rejected_offer_that_becomes_a_candidate_is_announced(self):
        """Prices move — this is the case re-scoring the whole universe is for."""
        entry = offer(None, status="rejected", rejections=["spread 0.9% below floor"])
        self.assertEqual(notifications_due(universe(entry), CONFIG), [])
        entry.update({"status": "candidate", "tier": "A", "rejections": []})
        self.assertEqual(len(notifications_due(universe(entry), CONFIG)), 1)


class ClosingTheLoop(unittest.TestCase):
    def test_an_expired_announced_offer_is_closed(self):
        entry = record_notified(offer("A", status="expired"), issue=7, now=NOW)
        closing = notifications_to_close(universe(archive=[entry]), CONFIG)
        self.assertEqual(len(closing), 1)
        self.assertIn("expired", notify.closing_comment(closing[0]))

    def test_an_offer_that_stops_qualifying_is_closed_with_the_reason(self):
        entry = record_notified(offer("A"), issue=7, now=NOW)
        entry.update({"status": "rejected", "tier": None,
                      "rejections": ["3 days to expiry, under the 4-day floor"]})
        closing = notifications_to_close(universe(entry), CONFIG)
        self.assertEqual(len(closing), 1)
        self.assertIn("under the 4-day floor", notify.closing_comment(closing[0]))

    def test_a_still_qualifying_offer_is_left_open(self):
        entry = record_notified(offer("A"), issue=7, now=NOW)
        self.assertEqual(notifications_to_close(universe(entry), CONFIG), [])

    def test_an_issue_is_only_closed_once(self):
        entry = record_notified(offer("A", status="expired"), issue=7, now=NOW)
        entry["notified"]["closed"] = NOW.isoformat()
        self.assertEqual(notifications_to_close(universe(archive=[entry]), CONFIG), [])

    def test_an_offer_that_was_never_announced_needs_no_closing(self):
        entry = offer("C", status="expired")
        self.assertEqual(notifications_to_close(universe(archive=[entry]), CONFIG), [])


class TheNotificationItself(unittest.TestCase):
    """It has to be decidable from the notification, on a phone, in ten seconds."""

    def setUp(self):
        self.entry = offer("A")
        self.title = notify.issue_title(self.entry)
        self.body = notify.issue_body(self.entry, CONFIG)

    def test_the_title_leads_with_the_decision(self):
        self.assertTrue(self.title.startswith("[Tier A] ACME"))
        self.assertIn("+5.26%", self.title)
        self.assertIn("2026-10-03", self.title)

    def test_the_body_carries_every_number_the_gates_used(self):
        for fragment in ("$10.00", "$9.50", "+5.26%", "$940.50", "$49.50",
                         "2026-10-03", "30 days", "500,000"):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, self.body)

    def test_the_body_quotes_the_filing_and_links_it(self):
        self.assertIn("before proration", self.body)
        self.assertIn("https://example.invalid/offer.htm", self.body)

    def test_the_body_states_the_rules_that_forfeit_the_preference(self):
        """The three ways to lose the preference after buying the shares."""
        self.assertIn("fewer than 100", self.body)
        self.assertIn("Tender **every** share", self.body)
        self.assertIn("aggregates across all accounts", self.body)
        self.assertIn("broker's tender deadline runs **ahead**", self.body)

    def test_the_body_is_not_mistakable_for_advice(self):
        self.assertIn("not investment advice", self.body)

    def test_a_dutch_range_shows_both_ends_and_which_was_used(self):
        entry = offer("A", dutch_range=[8.2, 9.4], offer_price=8.2)
        self.assertIn("low end used", notify.issue_body(entry, CONFIG))

    def test_an_amendment_warning_precedes_the_table_it_refers_to(self):
        """gate_document phrases its warning as "terms below"."""
        entry = offer("A", warnings=["amendment — terms below are this amendment's"])
        body = notify.issue_body(entry, CONFIG)
        self.assertIn("[!WARNING]", body)
        self.assertLess(body.index("[!WARNING]"), body.index("| Offer price |"))


class MissingCredentialsNeverBreakTheRun(unittest.TestCase):
    """The universe, the report and the tab are all written before this runs."""

    def test_it_exits_zero_without_a_token(self):
        import contextlib
        import io
        import os

        saved = {k: os.environ.pop(k, None) for k in ("GITHUB_TOKEN", "GITHUB_REPOSITORY")}
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(notify.main(["--dry-run"]), 0)
        finally:
            for key, value in saved.items():
                if value is not None:
                    os.environ[key] = value


if __name__ == "__main__":
    unittest.main()
