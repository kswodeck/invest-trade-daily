#!/usr/bin/env python3
"""Tests for the odd-lot rate limiter, economics, gates, universe and slots.

    python -m unittest discover -s tests -v

The rate-limiter tests are the ones that matter to somebody other than us. The
SEC's 10 requests/second is per IP and aggregated across machines, and the
penalty for exceeding it is a ~10 minute block of the whole address — which on
a shared GitHub runner is somebody else's outage too. So the limiter is tested
on a fake clock, where a burst either provably cannot happen or provably can.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import date, datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import odd_lot  # noqa: E402
from odd_lot import (  # noqa: E402
    EftsSchemaError, OfferTerms, RateLimiter, add_discoveries, archive_expired,
    check_user_agent, economics, gate_economics, gate_risk, load_universe, pad_cik,
    parse_efts_response, save_universe, slot_for, terms_from_stored, tier_for,
)

ET = ZoneInfo("America/New_York")
TODAY = date(2026, 9, 3)
CONFIG = json.loads((REPO / "config" / "odd_lot.json").read_text())


class FakeClock:
    """A monotonic clock that only advances when something sleeps on it."""

    def __init__(self) -> None:
        self.now = 0.0
        self.sleeps: list[float] = []

    def time(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        # A negative or zero sleep would spin forever against a fake clock, and
        # would be a bug against a real one too.
        self.sleeps.append(seconds)
        self.now += max(seconds, 0.0)


class RateLimiterHoldsTheCeiling(unittest.TestCase):
    def limiter(self, **kwargs) -> tuple[RateLimiter, FakeClock]:
        clock = FakeClock()
        return RateLimiter(clock=clock.time, sleeper=clock.sleep, **kwargs), clock

    def test_no_one_second_window_ever_holds_more_than_eight_requests(self):
        limiter, clock = self.limiter(max_per_second=8, min_interval=0.12)
        stamps = []
        for _ in range(60):
            limiter.acquire()
            stamps.append(clock.now)

        for i, start in enumerate(stamps):
            in_window = sum(1 for t in stamps[i:] if t - start < 1.0)
            self.assertLessEqual(
                in_window, 8,
                f"{in_window} requests inside the second starting at {start:.3f}s")

    def test_the_spacing_floor_is_honoured_between_consecutive_calls(self):
        limiter, clock = self.limiter(max_per_second=8, min_interval=0.12)
        stamps = []
        for _ in range(25):
            limiter.acquire()
            stamps.append(clock.now)
        gaps = [b - a for a, b in zip(stamps, stamps[1:])]
        self.assertTrue(all(gap >= 0.12 - 1e-9 for gap in gaps),
                        f"minimum gap was {min(gaps):.4f}s, floor is 0.12s")

    def test_sustained_rate_stays_under_the_sec_ceiling(self):
        limiter, clock = self.limiter(max_per_second=8, min_interval=0.12)
        for _ in range(100):
            limiter.acquire()
        # 100 requests at a 0.12s floor cannot finish sooner than 11.88s.
        self.assertGreaterEqual(clock.now, 99 * 0.12 - 1e-9)
        self.assertLessEqual(100 / max(clock.now, 1e-9), 10.0,
                             "sustained rate exceeded the SEC's 10 req/s ceiling")

    def test_a_long_run_terminates_rather_than_spinning_on_a_float_boundary(self):
        """Sleeping to exactly the window boundary can land a hair short of it,
        and the remaining sleep is then below the clock's own resolution — the
        limiter spins forever instead of sending. Every wait overshoots by a
        microsecond for this reason, so a long run has to finish."""
        limiter, clock = self.limiter(max_per_second=8, min_interval=0.12)
        for _ in range(400):
            limiter.acquire()
        self.assertGreater(clock.now, 0)
        self.assertTrue(all(s > 0 for s in clock.sleeps),
                        "a zero-length sleep cannot advance a clock")

    def test_the_test_harness_can_actually_catch_a_burst(self):
        """A limiter that cannot fail proves nothing — check the harness bites."""
        limiter, clock = self.limiter(max_per_second=50, min_interval=0.0)
        stamps = []
        for _ in range(20):
            limiter.acquire()
            stamps.append(clock.now)
        in_first_second = sum(1 for t in stamps if t - stamps[0] < 1.0)
        self.assertGreater(in_first_second, 8)

    def test_an_idle_gap_lets_the_window_drain(self):
        limiter, clock = self.limiter(max_per_second=8, min_interval=0.12)
        for _ in range(8):
            limiter.acquire()
        clock.now += 5.0
        before = len(clock.sleeps)
        limiter.acquire()
        self.assertEqual(len(clock.sleeps), before,
                         "a request after an idle gap should not have to wait")


class UserAgentIsChecked(unittest.TestCase):
    def test_a_contact_user_agent_passes(self):
        check_user_agent("InvestingResearch kris@example.com")

    def test_generic_and_empty_user_agents_are_refused(self):
        for bad in ("", "   ", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
                    "python-requests/2.28.1", "curl/8.4.0"):
            with self.subTest(ua=bad):
                with self.assertRaises(SystemExit):
                    check_user_agent(bad)

    def test_a_user_agent_without_a_contact_address_is_refused(self):
        with self.assertRaises(SystemExit):
            check_user_agent("InvestingResearch")


class CikPadding(unittest.TestCase):
    def test_ciks_are_padded_to_ten_digits(self):
        """data.sec.gov 404s on an unpadded CIK, which reads as "no filings"."""
        self.assertEqual(pad_cik(320193), "0000320193")
        self.assertEqual(pad_cik("320193"), "0000320193")
        self.assertEqual(pad_cik("CIK0000320193"), "0000320193")
        self.assertEqual(pad_cik("0000320193"), "0000320193")


class EftsAdapterFailsLoudly(unittest.TestCase):
    """A schema change must not look like a quiet week for tender offers."""

    def test_zero_hits_is_a_valid_answer(self):
        self.assertEqual(parse_efts_response({"hits": {"hits": []}}), [])

    def test_a_missing_hits_block_raises(self):
        for payload in ({}, {"results": []}, {"hits": {}}, [], "nope"):
            with self.subTest(payload=payload):
                with self.assertRaises(EftsSchemaError):
                    parse_efts_response(payload)

    def test_a_hit_without_ciks_raises(self):
        with self.assertRaises(EftsSchemaError):
            parse_efts_response({"hits": {"hits": [
                {"_id": "0001104659-26-000123:doc.htm", "_source": {"ciks": []}}]}})

    def test_the_form_is_the_filing_form_not_the_exhibit_type(self):
        """EFTS `file_type` names the *document* — EX-99.(A)(1)(III) — and the
        first live run reported every hit as an exhibit because this preferred
        it over `root_forms`."""
        hit = parse_efts_response({"hits": {"hits": [{
            "_id": "0001104659-26-000123:ex99a1iii.htm",
            "_source": {"ciks": ["0000320193"], "display_names": ["ACME (ACME)"],
                        "file_type": "EX-99.(A)(1)(III)", "root_forms": ["SC TO-I"],
                        "file_date": "2026-09-01"}}]}})[0]
        self.assertEqual(hit["form"], "SC TO-I")
        self.assertEqual(hit["document_type"], "EX-99.(A)(1)(III)")

    def test_a_well_formed_hit_is_flattened(self):
        hits = parse_efts_response({"hits": {"hits": [{
            "_id": "0001104659-26-000123:tm26123d1_sctoi.htm",
            "_source": {
                "ciks": ["0000320193"],
                "display_names": ["MERIDIAN INDUSTRIAL HOLDINGS INC  (MIH)  (CIK 0000320193)"],
                "file_type": "SC TO-I",
                "file_date": "2026-09-01",
                "root_forms": ["SC TO-I"],
            },
            "highlight": {"_source": ["holders of <em>odd lots</em> will be accepted"]},
        }]}})
        self.assertEqual(len(hits), 1)
        hit = hits[0]
        self.assertEqual(hit["accession"], "0001104659-26-000123")
        self.assertEqual(hit["cik"], "0000320193")
        self.assertEqual(hit["ticker"], "MIH")
        self.assertEqual(hit["company"], "MERIDIAN INDUSTRIAL HOLDINGS INC")
        self.assertEqual(hit["form"], "SC TO-I")
        self.assertTrue(hit["url"].endswith("/000110465926000123/tm26123d1_sctoi.htm"))
        self.assertEqual(hit["highlights"], ["holders of odd lots will be accepted"])


class Economics(unittest.TestCase):
    def test_the_arithmetic(self):
        econ = economics(10.00, 9.50, "2026-10-03", today=TODAY, shares=99)
        self.assertAlmostEqual(econ["spread_pct"], 0.0526316, places=6)
        self.assertEqual(econ["capital"], 940.50)
        self.assertEqual(econ["days_to_expiry"], 30)
        self.assertAlmostEqual(econ["annualized"], 0.0526316 * (365 / 30), places=5)
        self.assertEqual(econ["gross_profit"], 49.50)

    def test_an_offer_below_the_market_is_a_negative_spread_not_an_error(self):
        econ = economics(9.00, 10.00, "2026-10-03", today=TODAY)
        self.assertLess(econ["spread_pct"], 0)
        self.assertIn("market_price_above_offer", gate_risk(OfferTerms(), econ))

    def test_same_day_expiry_does_not_divide_by_zero(self):
        econ = economics(10.00, 9.50, TODAY.isoformat(), today=TODAY)
        self.assertEqual(econ["days_to_expiry"], 0)
        self.assertIsNone(econ["annualized"])


class GateTwo(unittest.TestCase):
    def reasons(self, econ, volume=500_000) -> str:
        return " | ".join(gate_economics(econ, volume, CONFIG).rejections)

    def clean(self) -> dict:
        return economics(10.00, 9.50, "2026-10-03", today=TODAY)

    def test_a_clean_offer_passes(self):
        self.assertTrue(gate_economics(self.clean(), 500_000, CONFIG).passed)

    def test_a_thin_spread_is_rejected(self):
        econ = economics(10.00, 9.90, "2026-10-03", today=TODAY)
        self.assertIn("below the 1.5% floor", self.reasons(econ))

    def test_capital_over_the_cap_is_rejected(self):
        """99 shares of a $60 stock is $5,940 — over the $5,000 cap."""
        econ = economics(63.00, 60.00, "2026-10-03", today=TODAY)
        self.assertIn("over the $5,000 cap", self.reasons(econ))

    def test_a_short_timeline_is_rejected(self):
        """Broker tender cutoffs land a day or more before the offer deadline."""
        econ = economics(10.00, 9.50, "2026-09-05", today=TODAY)
        self.assertIn("under the 4-day floor", self.reasons(econ))

    def test_a_sub_dollar_stock_is_rejected_with_no_exception(self):
        econ = economics(1.20, 0.95, "2026-10-03", today=TODAY)
        self.assertIn("sub-dollar floor", self.reasons(econ))

    def test_thin_volume_is_rejected(self):
        self.assertIn("exit-liquidity floor", self.reasons(self.clean(), volume=12_000))

    def test_unknown_volume_is_rejected_rather_than_assumed(self):
        self.assertIn("exit liquidity unknown", self.reasons(self.clean(), volume=None))


class Tiering(unittest.TestCase):
    """B is decided by the flags, not by how thin the spread is.

    A spread at or above the Gate 2 floor is a Tier B spread, full stop — a
    1.8% spread is a smaller version of the same trade, not evidence against
    it. What separates B from C is whether something is wrong with the offer.
    """

    def tier(self, spread_pct: float, days: int, flags: list[str]) -> str:
        econ = {"spread_pct": spread_pct, "days_to_expiry": days}
        return tier_for(econ, flags, CONFIG)

    def test_tier_a_needs_all_three(self):
        self.assertEqual(self.tier(0.04, 21, []), "A")

    def test_a_thinner_spread_alone_is_tier_b(self):
        self.assertEqual(self.tier(0.02, 21, []), "B")

    def test_a_tight_timeline_alone_is_tier_b(self):
        self.assertEqual(self.tier(0.04, 5, []), "B")

    def test_one_minor_flag_alone_is_tier_b(self):
        self.assertEqual(self.tier(0.04, 21, ["minimum_tender_condition"]), "B")

    def test_a_thin_spread_with_one_minor_flag_is_still_tier_b(self):
        """The spread does not stack with a flag to make a demotion.

        This is the case the "1.5-3%" reading got wrong: it counted a thin
        spread as a shortfall, so a 1.8% spread plus one minor flag became two
        shortfalls and fell to C. A 1.8% spread with a minimum-tender condition
        is a Tier B trade — one thing to check, at a smaller size.
        """
        self.assertEqual(self.tier(0.018, 21, ["minimum_tender_condition"]), "B")

    def test_a_thin_spread_and_a_tight_timeline_is_still_tier_b(self):
        self.assertEqual(self.tier(0.016, 5, []), "B")

    def test_everything_soft_at_once_is_still_tier_b(self):
        self.assertEqual(self.tier(0.016, 4, ["minimum_tender_condition"]), "B")

    def test_two_flags_is_tier_c(self):
        """One thing to check is a Tier B trade; two is a different offer."""
        self.assertEqual(
            self.tier(0.08, 60, ["minimum_tender_condition", "financing_condition"]), "C")

    def test_a_material_flag_alone_is_tier_c(self):
        """A going concern is never a minor flag: it is the counterparty. And
        neither beats a wide spread on a long calendar."""
        self.assertEqual(self.tier(0.06, 30, ["going_concern"]), "C")
        self.assertEqual(self.tier(0.06, 30, ["market_price_above_offer"]), "C")

    def test_the_tier_b_spread_floor_is_a_floor_not_a_band(self):
        """Its upper end is Tier A's requirement, not a ceiling on B."""
        self.assertEqual(CONFIG["tiers"]["tier_b"]["min_spread_pct"],
                         CONFIG["economics"]["min_spread_pct"],
                         "Tier B's spread floor is the gate's floor — anything "
                         "published is a Tier B spread")
        self.assertNotIn("max_spread_pct", CONFIG["tiers"]["tier_b"])

    def test_a_spread_under_the_floor_cannot_be_tiered(self):
        """Unreachable through Gate 2, but the two floors are separate config
        entries and can be set apart."""
        self.assertEqual(self.tier(0.004, 30, []), "C")


class Universe(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "universe.json"
        self.addCleanup(self.tmp.cleanup)

    def hit(self, accession: str, **kwargs) -> dict:
        return {"accession": accession, "cik": "0000320193", "company": "ACME",
                "ticker": "ACME", "form": "SC TO-I", "filed": "2026-09-01",
                "document": "doc.htm", "url": "https://example.invalid/doc.htm",
                "index_url": "https://example.invalid/index.htm", "highlights": [],
                **kwargs}

    def test_deduplication_is_by_accession(self):
        universe = load_universe(self.path)
        add_discoveries(universe, [self.hit("0001-26-000001")])
        added = add_discoveries(universe, [self.hit("0001-26-000001"),
                                           self.hit("0001-26-000002")])
        self.assertEqual([e["accession"] for e in added], ["0001-26-000002"])
        self.assertEqual(len(universe["open"]), 2)

    def test_an_amendment_enters_as_its_own_entry(self):
        """An SC TO-I/A carries its own accession and its own reading of the
        terms; collapsing it into the original would hide the amendment."""
        universe = load_universe(self.path)
        add_discoveries(universe, [self.hit("0001-26-000001")])
        add_discoveries(universe, [self.hit("0001-26-000009", form="SC TO-I/A")])
        self.assertEqual(len(universe["open"]), 2)

    def test_an_archived_accession_is_not_rediscovered(self):
        universe = load_universe(self.path)
        add_discoveries(universe, [self.hit("0001-26-000001", )])
        universe["open"][0]["expiration_date"] = "2026-08-01"
        archive_expired(universe, TODAY)
        self.assertEqual(len(universe["open"]), 0)
        self.assertEqual(add_discoveries(universe, [self.hit("0001-26-000001")]), [])

    def test_expiry_archives_with_the_outcome_kept(self):
        universe = load_universe(self.path)
        add_discoveries(universe, [self.hit("0001-26-000001")])
        universe["open"][0].update({"expiration_date": "2026-09-02", "tier": "B"})
        moved = archive_expired(universe, TODAY)
        self.assertEqual(len(moved), 1)
        self.assertEqual(universe["archive"][0]["status"], "expired")
        self.assertIn("tier B", universe["archive"][0]["outcome"])

    def test_an_unreadable_expiration_is_not_archived_as_expired(self):
        """"we could not read the date" is not "it has expired" — archiving it
        as one hides a parser failure behind a plausible outcome."""
        universe = load_universe(self.path)
        add_discoveries(universe, [self.hit("0001-26-000001")])
        universe["open"][0]["expiration_date"] = None
        self.assertEqual(archive_expired(universe, TODAY), [])
        self.assertEqual(len(universe["open"]), 1)

    def test_an_entry_with_no_readable_expiration_ages_out_eventually(self):
        """It must not be archived as "expired" — that would hide a parser
        failure — but it cannot sit in `open` forever either."""
        universe = load_universe(self.path)
        add_discoveries(universe, [self.hit("0001-26-000001")])
        entry = universe["open"][0]
        entry.update({"expiration_date": None, "first_seen": "2026-01-01"})

        self.assertEqual(archive_expired(universe, TODAY, stale_after_days=None), [])
        self.assertEqual(archive_expired(universe, TODAY, stale_after_days=400), [])

        moved = archive_expired(universe, TODAY, stale_after_days=120)
        self.assertEqual(len(moved), 1)
        self.assertIn("no expiration date could ever be read", moved[0]["outcome"])

    def test_a_universe_round_trips_through_disk(self):
        universe = load_universe(self.path)
        add_discoveries(universe, [self.hit("0001-26-000001")])
        universe["last_run_at"] = "2026-09-03T05:37:00-04:00"
        save_universe(universe, self.path)
        reloaded = load_universe(self.path)
        self.assertEqual(len(reloaded["open"]), 1)
        self.assertEqual(reloaded["last_run_at"], "2026-09-03T05:37:00-04:00")
        self.assertIsNotNone(reloaded["updated_at"])


class StoredTermsSurviveSchemaDrift(unittest.TestCase):
    """The universe is committed and outlives any one version of this module."""

    def test_unknown_stored_fields_are_dropped_rather_than_raising(self):
        terms = terms_from_stored(
            {"has_threshold": True, "offer_price": 12.5,
             "a_field_this_version_no_longer_has": "whatever"},
            paragraph="quoted text")
        self.assertTrue(terms.has_threshold)
        self.assertEqual(terms.offer_price, 12.5)
        self.assertEqual(terms.odd_lot_paragraph, "quoted text")

    def test_missing_stored_fields_fall_back_to_the_dataclass_defaults(self):
        terms = terms_from_stored({"has_threshold": True})
        self.assertFalse(terms.has_proration_preference)
        self.assertEqual(terms.risk_flags, [])


class Slots(unittest.TestCase):
    """Both DST arms of each slot fire every day; only one should do the work."""

    def et(self, hour: int, minute: int = 37, day: int = 3) -> datetime:
        return datetime(2026, 9, day, hour, minute, tzinfo=ET)

    def decide(self, now, **kwargs):
        return slot_for(now, CONFIG, **kwargs)

    def test_the_premarket_slot_runs(self):
        decision = self.decide(self.et(5))
        self.assertTrue(decision.proceed)
        self.assertEqual(decision.slot, "premarket")

    def test_the_evening_slot_runs(self):
        decision = self.decide(self.et(18, 30))
        self.assertTrue(decision.proceed)
        self.assertEqual(decision.slot, "evening")

    def test_the_middle_of_the_session_is_neither_slot(self):
        self.assertFalse(self.decide(self.et(14)).proceed)

    def test_the_second_dst_arm_is_dropped_by_the_recent_run_not_the_hour(self):
        """In EDT the two premarket arms land at 5:37 and 6:37 ET. Both are
        inside any sane window, so the window cannot separate them — the same
        mistake the daily report's gate made for two weeks."""
        first = self.et(5)
        self.assertTrue(self.decide(first).proceed)
        second = self.decide(self.et(6), last_run_at=first.isoformat())
        self.assertFalse(second.proceed)
        self.assertIn("other DST arm", second.reason)

    def test_the_evening_arm_is_not_blocked_by_the_morning_run(self):
        morning = self.et(5).isoformat()
        decision = self.decide(self.et(18, 30), last_run_at=morning)
        self.assertTrue(decision.proceed, decision.reason)

    def test_each_cron_arm_lands_where_it_is_meant_to(self):
        """The four declared crons, resolved to ET in both DST regimes.

        Each slot declares two UTC arms because GitHub cron has no DST
        awareness. In each regime exactly one arm of each pair should be in
        window; the other is either out of window or stopped by the
        recent-run guard. Getting this wrong is silent — the run simply
        happens at the wrong hour, or twice.
        """
        cases = [
            # (UTC cron hour+minute, ET month/day, expected ET hour, expected slot)
            ((9, 37), (7, 15), 5, "premarket"),    # EDT: 09:37Z -> 05:37 ET
            ((10, 37), (7, 15), 6, "premarket"),   # EDT: the EST arm, an hour late
            ((9, 37), (1, 15), 4, ""),             # EST: 09:37Z -> 04:37 ET, too early
            ((10, 37), (1, 15), 5, "premarket"),   # EST: 10:37Z -> 05:37 ET
            ((22, 30), (7, 15), 18, "evening"),    # EDT: 22:30Z -> 18:30 ET
            ((23, 30), (7, 15), 19, "evening"),    # EDT: the EST arm, an hour late
            ((22, 30), (1, 15), 17, ""),           # EST: 22:30Z -> 17:30 ET, too early
            ((23, 30), (1, 15), 18, "evening"),    # EST: 23:30Z -> 18:30 ET
        ]
        for (utc_h, utc_m), (month, day), expected_hour, expected_slot in cases:
            fired = datetime(2026, month, day, utc_h, utc_m, tzinfo=timezone.utc)
            local = fired.astimezone(ET)
            with self.subTest(cron=f"{utc_m} {utc_h} * * *", et=f"{local:%m-%d %H:%M}"):
                self.assertEqual(local.hour, expected_hour)
                decision = self.decide(local)
                self.assertEqual(decision.slot, expected_slot)
                self.assertEqual(decision.proceed, bool(expected_slot))

    def test_the_evening_arm_does_not_fire_before_the_edgar_deadline(self):
        """EDGAR's cutoff is 17:30 ET, so an evening run at 17:30 has nothing
        new to find. The window starts at 18:00 for that reason."""
        self.assertFalse(self.decide(self.et(17, 30)).proceed)
        self.assertTrue(self.decide(self.et(18, 30)).proceed)

    def test_a_manual_dispatch_is_honoured_at_any_hour(self):
        decision = self.decide(self.et(14), event_name="workflow_dispatch")
        self.assertTrue(decision.proceed)

    def test_force_overrides_the_recent_run_guard(self):
        recent = self.et(5, 30).isoformat()
        self.assertTrue(self.decide(self.et(6), last_run_at=recent, force=True).proceed)

    def test_an_unparseable_last_run_does_not_block_the_slot(self):
        self.assertTrue(self.decide(self.et(5), last_run_at="not a timestamp").proceed)


class ConfigIsTheOnlySourceOfThresholds(unittest.TestCase):
    def test_every_threshold_the_gates_read_is_present(self):
        for key in ("shares_tendered", "min_spread_pct", "max_capital",
                    "min_days_to_expiry", "min_avg_volume_30d", "min_market_price"):
            self.assertIn(key, CONFIG["economics"])
        self.assertEqual(CONFIG["economics"]["shares_tendered"], 99,
                         "99 is the whole trade: fewer than 100, tendered in full")
        self.assertIn("material_flags", CONFIG["tiers"])

    def test_the_sec_user_agent_env_var_overrides_the_committed_placeholder(self):
        import os

        original = os.environ.get("SEC_USER_AGENT")
        os.environ["SEC_USER_AGENT"] = "TestTool test@example.com"
        try:
            cfg = odd_lot.load_config(REPO / "config" / "odd_lot.json")
            self.assertEqual(cfg["sec"]["user_agent"], "TestTool test@example.com")
        finally:
            if original is None:
                os.environ.pop("SEC_USER_AGENT", None)
            else:
                os.environ["SEC_USER_AGENT"] = original


class TheScreenerAlarmCannotGoQuiet(unittest.TestCase):
    """A screen that fails must turn the run red.

    Structural assertions on the workflow rather than on Python, because both
    bugs lived in the YAML: the step piped into `tee`, so it reported tee's
    exit code and every failure read as success; and the alarm looked only at
    `discovery_error` in the universe file, which a crash never gets far enough
    to write. Together they meant an EFTS schema change — the thing the adapter
    raises loudly for — would have produced a green run, an empty tab, and no
    email. Text matching, because tests.yml runs stdlib-only with no yaml.
    """

    WORKFLOW = (REPO / ".github" / "workflows" / "odd-lot-screener.yml").read_text()

    def test_the_screen_step_does_not_swallow_its_exit_code_through_tee(self):
        self.assertIn("set -o pipefail", self.WORKFLOW)

    def test_the_alarm_reads_the_step_outcome_and_not_only_the_universe_file(self):
        self.assertIn("steps.screen.outcome", self.WORKFLOW)
        self.assertIn("SCREEN_OUTCOME", self.WORKFLOW)

    def test_the_screen_step_still_lets_publish_and_commit_run(self):
        """A discovery outage should still re-price and still publish — a
        stale-but-labelled tab beats no tab."""
        self.assertIn("continue-on-error: true", self.WORKFLOW)


if __name__ == "__main__":
    unittest.main()
