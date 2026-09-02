"""The gates that decide whether an idea's numbers are worth publishing.

These cover the three checks added after the first month's record: a stop
inside the noise, a reward-to-risk ratio with no probability behind it, and a
conviction score with no evidence behind it.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import validate_report as vr  # noqa: E402


def idea(**overrides) -> dict:
    base = {
        "symbol": "TST", "horizon": "swing", "direction": "buy", "conviction": 3,
        "entry": {"ideal": 100.0}, "exit": {"target": 118.0}, "stop": 94.0,
    }
    base.update(overrides)
    return base


def status_of(checks: list[dict], name: str) -> str | None:
    for check in checks:
        if check["check"] == name:
            return check["status"]
    return None


def detail_of(checks: list[dict], name: str) -> str:
    for check in checks:
        if check["check"] == name:
            return check["detail"]
    return ""


class StopDistance(unittest.TestCase):
    """ATR=3 here, so a 6-point stop is 2.0 ATR and a 3-point stop is 1.0."""

    def test_a_stop_inside_the_noise_fails(self):
        # DHT shipped at 7.4:1 on a 0.71 ATR stop and was stopped the same day.
        checks = vr.check_stop_distance(idea(stop=97.9), atr=3.0)
        self.assertEqual(status_of(checks, "stop_distance"), vr.FAIL)
        self.assertIn("inside the noise", detail_of(checks, "stop_distance"))

    def test_a_stop_between_the_floor_and_the_guide_warns(self):
        checks = vr.check_stop_distance(idea(stop=95.0), atr=3.0)  # 1.67 ATR
        self.assertEqual(status_of(checks, "stop_distance"), vr.WARN)

    def test_a_stop_clear_of_the_guide_passes(self):
        checks = vr.check_stop_distance(idea(stop=93.0), atr=3.0)  # 2.33 ATR
        self.assertEqual(status_of(checks, "stop_distance"), vr.PASS)

    def test_intraday_uses_its_own_tighter_floor(self):
        tight = idea(horizon="intraday", stop=97.0)  # 1.0 ATR
        self.assertEqual(status_of(vr.check_stop_distance(tight, 3.0), "stop_distance"),
                         vr.WARN)
        self.assertEqual(
            status_of(vr.check_stop_distance(idea(horizon="swing", stop=97.0), 3.0),
                      "stop_distance"),
            vr.FAIL)

    def test_long_term_is_exempt_because_its_downside_is_a_bear_case(self):
        checks = vr.check_stop_distance(idea(horizon="long_term", stop=None), atr=3.0)
        self.assertEqual(status_of(checks, "stop_distance"), vr.PASS)

    def test_a_missing_atr_warns_rather_than_guessing(self):
        self.assertEqual(status_of(vr.check_stop_distance(idea(), None), "stop_distance"),
                         vr.WARN)

    def test_a_missing_stop_fails(self):
        self.assertEqual(status_of(vr.check_stop_distance(idea(stop=None), 3.0),
                                   "stop_distance"), vr.FAIL)

    def test_a_ratio_lifted_by_tightening_the_stop_no_longer_passes_clean(self):
        """KRE, republished three times: same entry and target, stop walked in.

        74.20 -> 75.20 took the ratio from 2.19:1 to 3.56:1 and the stop from
        2.52 ATR to 1.55 ATR. Before this check the second version looked like
        the better idea. It is the one that gets stopped.
        """
        atr = 1.03  # KRE's ATR14 on the day
        loose = idea(entry={"ideal": 76.8}, exit={"target": 82.5}, stop=74.2)
        tight = idea(entry={"ideal": 76.8}, exit={"target": 82.5}, stop=75.2)

        _, loose_rr = vr.check_risk_reward(loose)
        _, tight_rr = vr.check_risk_reward(tight)
        self.assertGreater(tight_rr, loose_rr)  # the ratio improves...

        # ...while the stop check moves the other way, which is the point.
        self.assertEqual(status_of(vr.check_stop_distance(loose, atr), "stop_distance"),
                         vr.PASS)
        self.assertEqual(status_of(vr.check_stop_distance(tight, atr), "stop_distance"),
                         vr.WARN)

    def test_the_floor_is_set_where_it_catches_the_worst_of_the_record(self):
        """Stop-ATR multiples of all nine measurable stop-outs of the first month.

        1.5 fails the worst five outright and warns on the rest; every one of
        them sits under the 2.0 guide. Nothing filled at 2.0 ATR or wider has
        been stopped. The floor is deliberately the conservative end of that —
        raising it to 2.0 would leave swing targets only a 4-6 ATR band under
        the ATR ceiling, which buys safer stops with more optimistic targets.
        """
        stopped_out = [1.50, 1.35, 1.49, 1.59, 1.54, 1.13, 1.53, 1.11, 0.71]
        failed = [m for m in stopped_out if m < vr.MIN_STOP_ATR["swing"]]
        self.assertEqual(len(failed), 5)
        self.assertTrue(all(m < vr.SAFE_STOP_ATR["swing"] for m in stopped_out))


class Expectancy(unittest.TestCase):
    def test_the_baseline_is_the_random_walk_probability(self):
        _, figures = vr.check_expectancy(idea(win_probability=0.5), computed_rr=3.0)
        self.assertEqual(figures["breakeven_probability"], 0.25)

    def test_an_idea_that_loses_at_its_own_hit_rate_fails(self):
        # 3:1 needs better than 25%; 20% is a losing bet stated plainly.
        checks, _ = vr.check_expectancy(idea(win_probability=0.20), computed_rr=3.0)
        self.assertEqual(status_of(checks, "expectancy"), vr.FAIL)
        self.assertIn("loses money", detail_of(checks, "expectancy"))

    def test_exactly_break_even_fails(self):
        checks, _ = vr.check_expectancy(idea(win_probability=0.25), computed_rr=3.0)
        self.assertEqual(status_of(checks, "expectancy"), vr.FAIL)

    def test_a_modest_edge_passes(self):
        checks, figures = vr.check_expectancy(idea(win_probability=0.35), computed_rr=3.0)
        self.assertEqual(status_of(checks, "expectancy"), vr.PASS)
        self.assertAlmostEqual(figures["expectancy_r"], 0.35 * 3 - 0.65, places=3)
        self.assertAlmostEqual(figures["claimed_edge"], 0.10, places=3)

    def test_a_large_claimed_edge_warns(self):
        checks, _ = vr.check_expectancy(idea(win_probability=0.60), computed_rr=3.0)
        self.assertEqual(status_of(checks, "expectancy"), vr.WARN)
        self.assertIn("large claim", detail_of(checks, "expectancy"))

    def test_a_missing_probability_warns_and_states_the_bar(self):
        """A warning, not a failure — an invented number is worse than none."""
        checks, figures = vr.check_expectancy(idea(), computed_rr=3.0)
        self.assertEqual(status_of(checks, "expectancy"), vr.WARN)
        self.assertIn("25%", detail_of(checks, "expectancy"))
        self.assertEqual(figures["breakeven_probability"], 0.25)

    def test_a_probability_outside_zero_to_one_fails(self):
        for bad in (0, 1, 55, -0.2):
            checks, _ = vr.check_expectancy(idea(win_probability=bad), computed_rr=3.0)
            self.assertEqual(status_of(checks, "expectancy"), vr.FAIL, bad)

    def test_nothing_is_claimed_without_a_ratio_to_claim_it_against(self):
        checks, figures = vr.check_expectancy(idea(), computed_rr=None)
        self.assertEqual(checks, [])
        self.assertEqual(figures, {})

    def test_a_healthy_ratio_does_not_imply_a_healthy_bet(self):
        """The whole point: 7.4:1 and 10% is still a losing idea."""
        checks, _ = vr.check_expectancy(idea(win_probability=0.10), computed_rr=7.4)
        self.assertEqual(status_of(checks, "expectancy"), vr.FAIL)


class ConvictionEvidence(unittest.TestCase):
    @staticmethod
    def with_kinds(*kinds: str, conviction: int) -> dict:
        return idea(conviction=conviction,
                    evidence=[{"kind": k, "detail": "…"} for k in kinds])

    def test_the_score_must_be_paid_for_in_distinct_confirmations(self):
        supported = self.with_kinds("dated_catalyst", "primary_document",
                                    "positioning", conviction=4)
        self.assertEqual(status_of(vr.check_conviction_evidence(supported),
                                   "conviction_evidence"), vr.PASS)

    def test_an_over_scored_idea_warns_and_names_the_supported_score(self):
        checks = vr.check_conviction_evidence(
            self.with_kinds("dated_catalyst", "positioning", conviction=5))
        self.assertEqual(status_of(checks, "conviction_evidence"), vr.WARN)
        self.assertIn("supported score is 3", detail_of(checks, "conviction_evidence"))

    def test_repeating_one_kind_does_not_buy_a_higher_score(self):
        """Three articles about one press release are one confirmation."""
        checks = vr.check_conviction_evidence(
            self.with_kinds("primary_document", "primary_document",
                            "primary_document", conviction=4))
        self.assertEqual(status_of(checks, "conviction_evidence"), vr.WARN)
        self.assertIn("supported score is 2", detail_of(checks, "conviction_evidence"))

    def test_no_evidence_at_all_warns(self):
        checks = vr.check_conviction_evidence(idea(conviction=3))
        self.assertEqual(status_of(checks, "conviction_evidence"), vr.WARN)
        self.assertIn("no evidence listed", detail_of(checks, "conviction_evidence"))

    def test_conviction_two_needs_only_one_confirmation(self):
        checks = vr.check_conviction_evidence(
            self.with_kinds("technical_level", conviction=2))
        self.assertEqual(status_of(checks, "conviction_evidence"), vr.PASS)

    def test_it_warns_rather_than_failing_so_the_fix_is_a_lower_score(self):
        checks = vr.check_conviction_evidence(
            self.with_kinds("positioning", conviction=5))
        self.assertNotEqual(status_of(checks, "conviction_evidence"), vr.FAIL)


class Thresholds(unittest.TestCase):
    def test_every_horizon_with_a_stop_has_a_floor_and_a_guide(self):
        self.assertEqual(set(vr.MIN_STOP_ATR), set(vr.SAFE_STOP_ATR))
        for horizon, floor in vr.MIN_STOP_ATR.items():
            self.assertLess(floor, vr.SAFE_STOP_ATR[horizon], horizon)

    def test_the_stop_floor_leaves_room_under_the_target_ceiling(self):
        """A floor high enough to force optimistic targets is its own bug."""
        for horizon, floor in vr.MIN_STOP_ATR.items():
            implied_target = floor * vr.RR_FLOOR[horizon]
            self.assertLess(implied_target, vr.ATR_LIMIT[horizon], horizon)

    def test_conviction_evidence_requirements_rise_with_the_score(self):
        needs = [vr.CONVICTION_EVIDENCE[score] for score in sorted(vr.CONVICTION_EVIDENCE)]
        self.assertEqual(needs, sorted(needs))
        self.assertEqual(min(vr.CONVICTION_EVIDENCE), 2)  # the publish floor


if __name__ == "__main__":
    unittest.main()
