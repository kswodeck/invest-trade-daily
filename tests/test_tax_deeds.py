"""The gates that decide whether a tax deed listing reaches the shortlist.

The load-bearing ones are the four the task spec calls out, and each is here
because getting it wrong costs real money rather than a red test: a federal tax
lien that survives the sale, a lien check that could not run being read as a
clean one, a homestead's two-year redemption, and the arithmetic underneath
both exit routes.
"""

from __future__ import annotations

import json
import sys
import unittest
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import tax_deeds as td  # noqa: E402

TODAY = date(2026, 9, 3)
SALE = "2026-10-06"

CHECK_NAMES = list(td.LIEN_CHECKS) + ["flood_zone", "road_frontage", "lot_size"]


def cfg() -> dict:
    return td.load_config()


def listing(**overrides) -> dict:
    base = {
        "county": "Dallas", "sale_type": "auction", "cause_number": "TX-22-01188",
        "account": "00000123456789000", "account_key": "00000123456789000",
        "address": "1417 S HARWOOD ST, DALLAS, TX 75215",
        "legal_description": "CITY VIEW ADDN BLK 1/1234 LT 7",
        "property_type": "Residential Single Family", "owner_name": "SMITH, JOHN A",
        "minimum_opening_bid": 8450.0, "adjudged_value": 74300.0,
        "sale_date": SALE, "status": "Active",
        "listing_url": "https://example.invalid/dallas/1",
    }
    base.update(overrides)
    return base


def cad(**overrides) -> dict:
    base = {
        "account": "00000123456789000", "appraised_value": 74300.0,
        "land_value": 22000.0, "improvement_value": 52300.0,
        "year_built": 1948, "sqft": 1024, "lot_sqft": 6250,
        "legal_description": "CITY VIEW ADDN BLK 1/1234 LT 7",
        "subdivision": "CITY VIEW ADDITION", "land_use_code": "A11",
        "land_use_description": "Residential Single Family", "exemptions": [],
        "situs": "1417 S HARWOOD ST DALLAS, TX 75215",
        "cad_url": "https://example.invalid/dcad/1", "cad": "DCAD",
    }
    base.update(overrides)
    return base


def checks(**results) -> list[dict]:
    """Every check clean unless named otherwise: `checks(federal_tax_lien='hit')`."""
    out = []
    for name in CHECK_NAMES:
        result = results.get(name, td.CLEAN)
        out.append(td.check_record(name, result, "test fixture", f"{name} {result}"))
    return out


def codes(items: list[dict]) -> set[str]:
    return {item["code"] for item in items}


class Gate1HardDisqualifiers(unittest.TestCase):
    def test_a_clean_low_bid_listing_survives(self):
        result = td.screen(listing(), cad(), checks(), cfg(), TODAY)
        self.assertEqual(result["status"], "candidate")
        self.assertEqual(result["rejections"], [])
        self.assertEqual(result["tier"], "A")

    def test_a_homestead_exemption_rejects(self):
        """§34.21(a): two years to redeem. You cannot sell, re-tenant or remodel."""
        result = td.screen(listing(), cad(exemptions=["Residence Homestead", "OV65"]),
                           checks(), cfg(), TODAY)
        self.assertEqual(result["status"], "rejected")
        self.assertIn("homestead", codes(result["rejections"]))
        self.assertIsNone(result["tier"])

    def test_the_homestead_flag_on_the_cad_record_rejects_too(self):
        result = td.screen(listing(), cad(homestead=True), checks(), cfg(), TODAY)
        self.assertIn("homestead", codes(result["rejections"]))

    def test_an_agricultural_exemption_rejects(self):
        result = td.screen(listing(), cad(exemptions=["1-D-1 Open Space"]),
                           checks(), cfg(), TODAY)
        self.assertIn("agricultural", codes(result["rejections"]))

    def test_a_mineral_only_interest_rejects(self):
        result = td.screen(
            listing(legal_description="MINERAL INTEREST ONLY, OIL AND GAS, ABST 1234"),
            cad(land_value=0, improvement_value=0), checks(), cfg(), TODAY)
        self.assertIn("mineral_only", codes(result["rejections"]))

    def test_a_severed_mineral_note_on_a_real_parcel_does_not_reject(self):
        """A house whose legal mentions a severed mineral estate is still a house."""
        result = td.screen(
            listing(legal_description="CITY VIEW ADDN LT 7, MINERAL ESTATE SEVERED"),
            cad(), checks(), cfg(), TODAY)
        self.assertNotIn("mineral_only", codes(result["rejections"]))

    def test_a_mobile_home_without_land_rejects(self):
        result = td.screen(listing(legal_description="MOBILE HOME ONLY - NO LAND"),
                           cad(land_value=0), checks(), cfg(), TODAY)
        self.assertIn("mobile_home_without_land", codes(result["rejections"]))

    def test_an_opening_bid_over_the_cap_rejects(self):
        result = td.screen(listing(minimum_opening_bid=31200.0),
                           cad(appraised_value=188000.0), checks(), cfg(), TODAY)
        self.assertIn("opening_bid_over_cap", codes(result["rejections"]))

    def test_bid_to_value_over_the_cap_rejects(self):
        result = td.screen(listing(minimum_opening_bid=14900.0),
                           cad(appraised_value=19000.0), checks(), cfg(), TODAY)
        self.assertIn("bid_to_value_over_cap", codes(result["rejections"]))

    def test_no_cad_match_flags_rather_than_hiding_the_property(self):
        """An unreachable appraisal district says nothing about the property."""
        result = td.screen(listing(adjudged_value=None), None, checks(), cfg(), TODAY)
        self.assertEqual(result["status"], "candidate")
        self.assertIn("no_cad_match", codes(result["flags"]))
        self.assertEqual(result["tier"], "C")
        self.assertIsNone(result["economics"])

    def test_the_countys_adjudged_value_prices_it_when_the_cad_cannot(self):
        """Tarrant rate-limited 365 lookups and Ellis reset the connection.

        The sale list often carries the adjudged value — the figure the court
        set in the tax suit — which is a real published number, so a dead
        appraisal district no longer means an unpriceable property.
        """
        result = td.screen(listing(adjudged_value=74300.0), None, checks(), cfg(), TODAY)
        self.assertEqual(result["status"], "candidate")
        self.assertEqual(result["economics"]["value_source"], "adjudged")
        self.assertAlmostEqual(result["economics"]["bid_to_value"], 8450 / 74300, places=4)
        detail = next(f["detail"] for f in result["flags"] if f["code"] == "no_cad_match")
        # Honest about provenance: the county published it; what basis it used
        # is the bidder's to confirm.
        self.assertIn("published on the county sale list", detail)
        self.assertIn("confirm its basis and its age", detail)
        self.assertIn("none ran", detail)

    def test_the_cad_is_preferred_over_the_adjudged_value_when_both_exist(self):
        result = td.screen(listing(adjudged_value=999999.0), cad(), checks(), cfg(), TODAY)
        self.assertEqual(result["economics"]["value_source"], "cad")
        self.assertEqual(result["economics"]["cad_value"], 74300.0)

    def test_an_adjudged_value_still_enforces_the_bid_to_value_cap(self):
        """Pricing on the fallback must not become a way around the gate."""
        result = td.screen(listing(minimum_opening_bid=9000.0, adjudged_value=10000.0),
                           None, checks(), cfg(), TODAY)
        self.assertEqual(result["status"], "rejected")
        self.assertIn("bid_to_value_over_cap", codes(result["rejections"]))

    def test_a_struck_off_listing_needs_no_sale_date(self):
        """There is no auction, so there is no date. That is the category."""
        result = td.screen(listing(sale_type="struck_off", sale_date=None), cad(),
                           checks(), cfg(), TODAY)
        self.assertEqual(result["status"], "candidate")
        self.assertNotIn("no_sale_date", codes(result["flags"]))
        self.assertEqual(result["tier"], "A")

    def test_an_auction_listing_with_no_date_flags_but_survives(self):
        result = td.screen(listing(sale_date=None), cad(), checks(), cfg(), TODAY)
        self.assertEqual(result["status"], "candidate")
        self.assertIn("no_sale_date", codes(result["flags"]))

    def test_a_passed_sale_date_rejects(self):
        result = td.screen(listing(sale_date="2026-08-04"), cad(), checks(), cfg(), TODAY)
        self.assertIn("sale_date_passed", codes(result["rejections"]))

    def test_a_withdrawn_listing_rejects(self):
        result = td.screen(listing(status="Cancelled - Taxes Paid"), cad(),
                           checks(), cfg(), TODAY)
        self.assertIn("withdrawn", codes(result["rejections"]))

    def test_a_missing_opening_bid_flags_rather_than_rejects(self):
        """Not knowing the bid is not a finding about the property."""
        result = td.screen(listing(minimum_opening_bid=None), cad(), checks(), cfg(), TODAY)
        self.assertEqual(result["status"], "candidate")
        self.assertIn("no_opening_bid", codes(result["flags"]))
        self.assertEqual(result["tier"], "C")
        self.assertIsNone(result["economics"])


class Gate2LienScreening(unittest.TestCase):
    def test_a_federal_tax_lien_hit_rejects(self):
        """The IRS keeps a 120-day right of redemption. Not a risk worth pricing."""
        result = td.screen(listing(), cad(), checks(federal_tax_lien=td.HIT),
                           cfg(), TODAY)
        self.assertEqual(result["status"], "rejected")
        self.assertIn("federal_tax_lien", codes(result["rejections"]))
        detail = next(r["detail"] for r in result["rejections"]
                      if r["code"] == "federal_tax_lien")
        self.assertIn("7425(d)", detail)
        self.assertIn("120", detail)

    def test_a_pace_lien_hit_rejects(self):
        result = td.screen(listing(), cad(), checks(pace_lien=td.HIT), cfg(), TODAY)
        self.assertIn("pace_lien", codes(result["rejections"]))

    def test_an_hoa_hit_flags_but_does_not_reject(self):
        result = td.screen(listing(), cad(), checks(hoa_assessment=td.HIT), cfg(), TODAY)
        self.assertEqual(result["status"], "candidate")
        self.assertIn("hoa_assessment", codes(result["flags"]))

    def test_an_unavailable_lien_check_does_not_pass_as_clean(self):
        """The whole point. `couldn't check` is unknown, never clean."""
        result = td.screen(listing(), cad(), checks(federal_tax_lien=td.UNAVAILABLE),
                           cfg(), TODAY)
        self.assertIn("federal_tax_lien_unchecked", codes(result["flags"]))
        flag = next(f for f in result["flags"] if f["code"] == "federal_tax_lien_unchecked")
        self.assertEqual(flag["severity"], td.MATERIAL)
        self.assertIn("Unknown, not clean", flag["detail"])
        self.assertIn("federal_tax_lien", result["checks_unavailable"])
        self.assertNotIn("federal_tax_lien", result["checks_run"])
        # And it must cost the listing its rank, or the flag would be decorative.
        self.assertEqual(result["tier"], "C")

    def test_a_check_that_never_ran_at_all_is_treated_as_unavailable(self):
        """An absent check and a failed check look identical to the property."""
        partial = [c for c in checks() if c["check"] != "pace_lien"]
        result = td.screen(listing(), cad(), partial, cfg(), TODAY)
        self.assertIn("pace_lien_unchecked", codes(result["flags"]))
        self.assertIn("pace_lien", result["checks_unavailable"])
        self.assertEqual(result["tier"], "C")

    def test_no_checks_at_all_is_the_worst_case_not_the_best(self):
        result = td.screen(listing(), cad(), [], cfg(), TODAY)
        self.assertEqual(result["status"], "candidate")
        self.assertEqual(result["tier"], "C")
        for name in td.LIEN_CHECKS:
            self.assertIn(f"{name}_unchecked", codes(result["flags"]))

    def test_a_bogus_check_result_raises_rather_than_rendering_as_a_blank(self):
        with self.assertRaises(ValueError):
            td.check_record("federal_tax_lien", "probably fine", "somewhere")


class Gate3Physical(unittest.TestCase):
    def test_an_unchecked_flood_zone_is_still_a_flag(self):
        result = td.screen(listing(), cad(), checks(flood_zone=td.UNAVAILABLE),
                           cfg(), TODAY)
        self.assertIn("flood_zone_unchecked", codes(result["flags"]))
        self.assertEqual(result["minor_flags"], 1)

    def test_a_flood_zone_hit_is_a_material_flag_not_a_rejection(self):
        """It is priceable — insurance, a lower bid — where a homestead is not."""
        result = td.screen(listing(), cad(), checks(flood_zone=td.HIT), cfg(), TODAY)
        self.assertEqual(result["status"], "candidate")
        self.assertIn("flood_zone", codes(result["flags"]))
        self.assertEqual(result["tier"], "C")

    def test_flood_can_still_be_made_a_rejection_by_config(self):
        config = cfg()
        config["thresholds"]["REJECT_FLOOD_ZONE"] = True
        result = td.screen(listing(), cad(), checks(flood_zone=td.HIT), config, TODAY)
        self.assertIn("flood_zone", codes(result["rejections"]))

    def test_zero_frontage_flags_as_possibly_landlocked(self):
        result = td.screen(listing(), cad(), checks(road_frontage=td.HIT), cfg(), TODAY)
        self.assertIn("landlocked", codes(result["flags"]))

    def test_a_low_improvement_value_on_a_structure_flags_as_a_teardown(self):
        result = td.screen(listing(), cad(improvement_value=2500.0), checks(),
                           cfg(), TODAY)
        self.assertIn("likely_teardown", codes(result["flags"]))
        # One minor flag no longer costs Tier A — see TIER_A_MAX_MINOR_FLAGS.
        self.assertEqual(result["tier"], "A")

    def test_occupancy_is_always_unknown_and_never_inferred(self):
        result = td.screen(listing(), cad(), checks(), cfg(), TODAY)
        self.assertIn("occupancy_unknown", codes(result["flags"]))

    def test_the_occupancy_flag_does_not_make_tier_a_unreachable(self):
        """It is on every row, so it cannot rank rows. That is why it is UNIVERSAL."""
        result = td.screen(listing(), cad(), checks(), cfg(), TODAY)
        self.assertEqual(result["tier"], "A")
        self.assertEqual(result["material_flags"], 0)
        self.assertEqual(result["minor_flags"], 0)


class Gate4Economics(unittest.TestCase):
    def setUp(self):
        self.result = td.screen(listing(), cad(), checks(), cfg(), TODAY)
        self.econ = self.result["economics"]

    def test_bid_to_value_and_max_bid(self):
        self.assertAlmostEqual(self.econ["bid_to_value"], 8450 / 74300, places=4)
        self.assertAlmostEqual(self.econ["max_bid"],
                               74300 * td.threshold(cfg(), "MAX_BID_TO_VALUE"),
                               places=2)

    def test_the_redemption_payout_is_the_bid_plus_the_statutory_25_percent(self):
        self.assertAlmostEqual(self.econ["redemption_payout"], 8450 * 1.25, places=2)
        self.assertEqual(self.econ["redemption_period"], "180d")

    def test_total_cost_is_bid_plus_quiet_title_plus_holding_plus_post_judgment(self):
        parts = (self.econ["opening_bid"] + self.econ["quiet_title_budget"]
                 + self.econ["holding_costs"] + self.econ["post_judgment_taxes_estimate"])
        self.assertAlmostEqual(self.econ["est_total_cost"], parts, places=2)

    def test_the_redemption_capital_is_the_bid_plus_unreimbursed_carry_only(self):
        """No quiet title on a redeemable property, and taxes wash under §34.21(b).

        Counting the taxes as a cost with no matching reimbursement is what
        made a 17% redemption read as a headline -8% loss.
        """
        self.assertAlmostEqual(
            self.econ["redemption_capital"],
            self.econ["opening_bid"] + self.econ["redemption_carry"], places=2)
        self.assertNotIn(self.econ["quiet_title_budget"],
                         (self.econ["redemption_capital"],))
        self.assertLess(self.econ["redemption_carry"], self.econ["holding_costs"])

    def test_a_cheap_non_homestead_redemption_pays_rather_than_loses(self):
        self.assertGreater(self.econ["redemption_net_profit"], 0)
        self.assertGreater(self.econ["redemption_annualized_pct"],
                           self.econ["redemption_return_pct"])

    def test_both_outcomes_are_reported(self):
        self.assertIn("redemption_annualized_pct", self.econ)
        self.assertIn("ownership_equity", self.econ)
        self.assertAlmostEqual(self.econ["ownership_equity"],
                               self.econ["cad_value"] - self.econ["est_total_cost"], places=2)

    def test_a_two_year_redemption_prices_both_penalty_years(self):
        terms = td.redemption_terms(listing(), cad(exemptions=["Residence Homestead"]))
        econ = td.gate4_economics(listing(), cad(exemptions=["Residence Homestead"]),
                                  cfg(), terms)
        self.assertEqual(econ["redemption_period"], "2yr")
        self.assertAlmostEqual(econ["redemption_payout"], 8450 * 1.25, places=2)
        self.assertAlmostEqual(econ["redemption_payout_year_two"], 8450 * 1.50, places=2)

    def test_nothing_is_priced_without_any_value_at_all(self):
        self.assertIsNone(td.gate4_economics(listing(adjudged_value=None),
                                             cad(appraised_value=None), cfg()))

    def test_the_value_source_is_always_recorded(self):
        self.assertEqual(self.econ["value_source"], "cad")


class Gate5Tiering(unittest.TestCase):
    def test_tier_a_needs_zero_flags_and_a_bid_under_35_percent(self):
        self.assertEqual(td.screen(listing(), cad(), checks(), cfg(), TODAY)["tier"], "A")

    def test_a_cheap_listing_with_one_minor_flag_still_reaches_tier_a(self):
        result = td.screen(listing(), cad(), checks(hoa_assessment=td.HIT), cfg(), TODAY)
        self.assertEqual(result["minor_flags"], 1)
        self.assertEqual(result["tier"], "A")

    def test_two_minor_flags_drop_a_cheap_listing_to_tier_b(self):
        result = td.screen(listing(), cad(),
                           checks(hoa_assessment=td.HIT, flood_zone=td.UNAVAILABLE),
                           cfg(), TODAY)
        self.assertEqual(result["minor_flags"], 2)
        self.assertEqual(result["tier"], "B")

    def test_a_bid_between_35_and_60_percent_is_tier_b_even_with_no_flags(self):
        result = td.screen(listing(minimum_opening_bid=8450.0),
                           cad(appraised_value=20000.0), checks(), cfg(), TODAY)
        self.assertEqual(result["tier"], "B")

    def test_a_material_flag_drops_it_to_tier_c(self):
        result = td.screen(listing(), cad(), checks(municipal_lien=td.HIT), cfg(), TODAY)
        self.assertEqual(result["tier"], "C")

    def test_more_than_two_minor_flags_drop_it_to_tier_c(self):
        result = td.screen(listing(improvement_value=2500.0), cad(improvement_value=2500.0),
                           checks(hoa_assessment=td.HIT, flood_zone=td.UNAVAILABLE),
                           cfg(), TODAY)
        self.assertEqual(result["minor_flags"], 3)
        self.assertEqual(result["tier"], "C")

    def test_rejected_listings_carry_no_tier(self):
        rejected = td.screen(listing(), cad(exemptions=["Residence Homestead"]),
                             checks(), cfg(), TODAY)
        self.assertEqual(rejected["status"], "rejected")
        self.assertIsNone(rejected["tier"])


class WrittenStatement34015(unittest.TestCase):
    def config_with(self, expires):
        config = cfg()
        config["bidder_statement"]["counties"]["Dallas"] = {"expires": expires}
        return config

    def test_a_missing_statement_is_a_blocker(self):
        status = td.statement_status(self.config_with(None), "Dallas", TODAY)
        self.assertEqual(status["state"], "missing")
        self.assertIn("may not deliver a deed", status["message"])

    def test_it_warns_at_thirty_days_out(self):
        status = td.statement_status(self.config_with("2026-09-25"), "Dallas", TODAY)
        self.assertEqual(status["state"], "expiring")
        self.assertEqual(status["days_left"], 22)
        self.assertIn("21 working days", status["message"])

    def test_thirty_one_days_out_is_still_current(self):
        status = td.statement_status(self.config_with("2026-10-04"), "Dallas", TODAY)
        self.assertEqual(status["state"], "current")

    def test_an_expired_statement_says_so(self):
        status = td.statement_status(self.config_with("2026-08-01"), "Dallas", TODAY)
        self.assertEqual(status["state"], "expired")
        self.assertLess(status["days_left"], 0)


class SheetOutput(unittest.TestCase):
    def setUp(self):
        self.config = cfg()
        self.results = [
            td.screen(listing(), cad(), checks(), self.config, TODAY),
            td.screen(listing(county="Tarrant", account="02345678",
                              minimum_opening_bid=7800.0,
                              address="1109 E ANNIE ST, FORT WORTH, TX 76104"),
                      cad(account="02345678", appraised_value=63000.0),
                      checks(hoa_assessment=td.HIT), self.config, TODAY),
            td.screen(listing(county="Tarrant", account="07654321",
                              minimum_opening_bid=4250.0),
                      cad(account="07654321", appraised_value=38400.0),
                      checks(), self.config, TODAY),
            td.screen(listing(county="Johnson", status="Cancelled"), cad(),
                      checks(), self.config, TODAY),
        ]
        self.statements = td.statement_report(
            self.config, [c["name"] for c in td.counties(self.config)], TODAY)
        self.values, self.spec = td.sheet_rows(
            self.results, self.config, TODAY, SALE, self.statements)

    def test_the_disclaimer_is_row_one(self):
        self.assertEqual(self.values[0][0], td.DISCLAIMER)
        self.assertIn("NOT A TITLE SEARCH", self.values[0][0])

    def test_the_header_lands_on_the_frozen_row(self):
        self.assertEqual(self.values[td.HEADER_ROW - 1], td.HEADERS)
        self.assertEqual(len(td.HEADERS), 23)
        self.assertEqual(td.HEADERS[td.COL_TIER], "Tier")
        self.assertIn("Value Source", td.HEADERS)

    def test_counties_are_blocked_in_dallas_tarrant_johnson_ellis_order(self):
        banners = [self.values[row][0] for row in self.spec["county_rows"]]
        self.assertEqual([b.split()[0] for b in banners],
                         ["DALLAS", "TARRANT", "JOHNSON", "ELLIS"])

    def test_a_county_with_nothing_says_so_rather_than_being_omitted(self):
        text = "\n".join(str(row[0]) for row in self.values if row)
        self.assertIn("ELLIS COUNTY — 0 on the 2026-10-06 docket · 0 candidate(s)",
                      text)
        self.assertIn("no listing survived the gates", text)

    def test_rows_sort_by_tier_then_bid_to_value(self):
        rows = [self.values[row] for row, _ in self.spec["data_rows"]
                if self.values[row][0] == "Tarrant"]
        ratios = [float(r[td.HEADERS.index("Bid/Value")]) for r in rows]
        self.assertEqual(ratios, sorted(ratios))

    def test_rejected_listings_never_reach_the_sheet(self):
        accounts = [self.values[row][4] for row, _ in self.spec["data_rows"]]
        self.assertEqual(len(accounts), 3)

    def test_every_row_shows_which_checks_ran_and_which_did_not(self):
        run = td.HEADERS.index("Checks Run")
        unavailable = td.HEADERS.index("Checks Unavailable")
        for row, _ in self.spec["data_rows"]:
            self.assertTrue(self.values[row][run])
            self.assertTrue(self.values[row][unavailable])

    def test_the_statement_line_surfaces_the_blocker(self):
        self.assertIn("§34.015", self.values[2][0])
        self.assertIn("MISSING", self.values[2][0])


class PacketOutput(unittest.TestCase):
    def setUp(self):
        self.config = cfg()
        self.result = td.screen(listing(), cad(), checks(federal_tax_lien=td.UNAVAILABLE),
                                self.config, TODAY)
        self.statement = td.statement_status(self.config, "Dallas", TODAY)
        self.text = td.packet_markdown(self.result, self.config, self.statement)

    def test_it_opens_with_the_disclaimer(self):
        self.assertIn(td.DISCLAIMER, self.text)

    def test_it_carries_the_whole_manual_checklist(self):
        for item in td.CHECKLIST:
            self.assertIn(f"- [ ] {item}", self.text)

    def test_every_check_is_listed_with_its_result_and_timestamp(self):
        for check in self.result["checks"]:
            self.assertIn(check["checked_at"], self.text)
        self.assertIn("unavailable — not screened", self.text)

    def test_it_states_the_redemption_period_and_its_basis(self):
        self.assertIn("§34.21", self.text)
        self.assertIn("180 days", self.text)
        self.assertIn("§34.21(h)", self.text)
        self.assertIn("does not come back clean", self.text)

    def test_it_states_the_bidder_eligibility_rules(self):
        self.assertIn("§34.015", self.text)
        self.assertIn("50-307", self.text)
        self.assertIn("Class B misdemeanor", self.text)
        self.assertIn("21 working days", self.text)

    def test_the_packet_path_is_sale_date_county_account(self):
        path = td.packet_path(self.result)
        self.assertEqual(path.parent.name, SALE)
        self.assertEqual(path.name, "dallas_00000123456789000.md")

    def test_no_output_claims_clear_title(self):
        """The one thing this tool must never say, in any of its own words."""
        statements = td.statement_report(self.config, ["Dallas"], TODAY)
        values, _ = td.sheet_rows([self.result], self.config, TODAY, SALE, statements)
        blob = (self.text + "\n" + "\n".join(str(c) for row in values for c in row)).lower()
        for phrase in ("clear title", "free and clear", "title is clear", "clean title",
                       "marketable title", "title guaranteed", "insurable title"):
            self.assertNotIn(phrase, blob, f"output claimed {phrase!r}")


class Helpers(unittest.TestCase):
    def test_first_tuesday_is_the_texas_sale_day(self):
        self.assertEqual(td.first_tuesday(2026, 10), date(2026, 10, 6))
        self.assertEqual(td.first_tuesday(2026, 12), date(2026, 12, 1))

    def test_the_next_sale_rolls_into_next_month_once_this_one_has_passed(self):
        self.assertEqual(td.next_sale_date(date(2026, 9, 3)), date(2026, 10, 6))
        self.assertEqual(td.next_sale_date(date(2026, 10, 6)), date(2026, 10, 6))
        self.assertEqual(td.next_sale_date(date(2026, 12, 2)), date(2027, 1, 5))

    def test_no_figure_published_is_none_and_never_zero(self):
        for blank in ("", "  ", "N/A", "TBD", "-", None):
            self.assertIsNone(td.parse_money(blank))
        self.assertEqual(td.parse_money("$8,450.00"), 8450.0)

    def test_thresholds_read_from_the_environment_first(self):
        import os
        config = cfg()
        self.assertEqual(td.threshold(config, "MAX_OPENING_BID"), 20000)
        os.environ["MAX_OPENING_BID"] = "5000"
        try:
            self.assertEqual(td.threshold(config, "MAX_OPENING_BID"), 5000.0)
        finally:
            del os.environ["MAX_OPENING_BID"]


if __name__ == "__main__":
    unittest.main()


class PacketTiers(unittest.TestCase):
    """Which candidates get a packet, and the escape hatch when none do."""

    def test_the_default_covers_every_tier(self):
        """A,B wrote nothing at all while the clerk portals stay unscreenable.

        A default that produces no output is not conservative, it is broken.
        """
        self.assertEqual(td.packet_tiers(cfg()), {"A", "B", "C"})

    def test_it_can_be_narrowed_once_a_clerk_source_is_configured(self):
        config = cfg()
        config["thresholds"]["PACKET_TIERS"] = "A,B"
        self.assertEqual(td.packet_tiers(config), {"A", "B"})

    def test_the_environment_wins(self):
        import os
        os.environ["PACKET_TIERS"] = "a, c"
        try:
            self.assertEqual(td.packet_tiers(cfg()), {"A", "C"})
        finally:
            del os.environ["PACKET_TIERS"]



class WalkAwayBid(unittest.TestCase):
    """Every other figure prices the auction *floor*, which nobody pays.

    The number a bidder actually needs is where to stop, and the checklist has
    asked for it since the first commit while nothing computed it.
    """

    def setUp(self):
        self.econ = td.gate4_economics(listing(), cad(), cfg())

    def test_the_walk_away_is_the_lower_of_the_two_ceilings(self):
        self.assertEqual(self.econ["walk_away_bid"],
                         min(self.econ["policy_cap_bid"],
                             self.econ["equity_breakeven_bid"]))

    def test_it_says_which_ceiling_is_binding(self):
        self.assertIn(self.econ["walk_away_basis"], (
            "policy cap (MAX_BID_TO_VALUE)",
            "equity break-even — above this you paid more than the property is worth"))

    def test_equity_is_zero_at_the_equity_break_even(self):
        at = td.gate4_economics(
            listing(minimum_opening_bid=self.econ["equity_breakeven_bid"]), cad(), cfg())
        self.assertAlmostEqual(at["ownership_equity"], 0.0, places=2)

    def test_headroom_is_how_far_the_bidding_can_run(self):
        self.assertAlmostEqual(self.econ["bid_headroom"],
                               self.econ["walk_away_bid"] - self.econ["opening_bid"], places=2)

    def test_a_cheap_property_redeems_at_a_loss(self):
        """The premium is a percentage; the carry it must cover is not.

        Five of one live run's 157 priced listings sat under this floor, and the
        bid-to-value ranking puts exactly those at the top.
        """
        econ = td.gate4_economics(listing(minimum_opening_bid=726.0), cad(), cfg())
        self.assertLess(econ["redemption_net_profit"], 0)
        self.assertGreater(econ["min_profitable_bid"], 726.0)

    def test_the_floor_is_where_the_premium_exactly_covers_the_carry(self):
        floor = self.econ["min_profitable_bid"]
        at = td.gate4_economics(listing(minimum_opening_bid=floor), cad(), cfg())
        self.assertAlmostEqual(at["redemption_net_profit"], 0.0, places=2)

    def test_a_bid_below_the_floor_is_flagged_not_silently_ranked_best(self):
        result = td.screen(listing(minimum_opening_bid=726.0), cad(), checks(), cfg(), TODAY)
        self.assertIn("redemption_loses_at_this_bid", codes(result["flags"]))
        detail = next(f["detail"] for f in result["flags"]
                      if f["code"] == "redemption_loses_at_this_bid")
        self.assertIn("Fine if you keep it", detail)

    def test_an_opening_bid_past_the_walk_away_is_a_material_flag(self):
        """A cheap property passes the ratio cap and still has no room in it.

        $4,000 on a $6,000 house is 0.67 bid-to-value, well inside the 0.75
        cap Gate 1 enforces — but the quiet title budget alone is $3,500, so
        the equity break-even sits at $1,757 and the ratio never sees it.
        """
        result = td.screen(listing(minimum_opening_bid=4000.0),
                           cad(appraised_value=6000.0), checks(), cfg(), TODAY)
        self.assertNotIn("bid_to_value_over_cap", codes(result["rejections"]))
        self.assertIn("opening_bid_past_walk_away", codes(result["flags"]))
        self.assertEqual(result["tier"], "C")

    def test_the_ratio_cap_alone_would_have_passed_that_bid(self):
        econ = td.gate4_economics(
            listing(minimum_opening_bid=4000.0), cad(appraised_value=6000.0), cfg())
        self.assertLess(econ["bid_to_value"],
                        td.threshold(cfg(), "MAX_BID_TO_VALUE"))
        self.assertLess(econ["walk_away_bid"], econ["opening_bid"])
        self.assertEqual(econ["walk_away_basis"],
                         "equity break-even — above this you paid more than "
                         "the property is worth")


class BusinessDays(unittest.TestCase):
    def test_weekends_do_not_count(self):
        # Fri 2026-09-04 -> Mon 2026-09-07 is one working day.
        self.assertEqual(td.business_days_between(date(2026, 9, 4), date(2026, 9, 7)), 1)

    def test_counting_backwards_skips_weekends_too(self):
        self.assertEqual(td.subtract_business_days(date(2026, 9, 7), 1), date(2026, 9, 4))

    def test_a_past_date_is_zero_not_negative(self):
        self.assertEqual(td.business_days_between(date(2026, 9, 7), date(2026, 9, 4)), 0)


class StatementAgainstTheSaleDate(unittest.TestCase):
    """Expiry alone misses the two ways this actually catches people out."""

    def config_with(self, expires):
        config = cfg()
        config["bidder_statement"]["counties"]["Dallas"] = {"expires": expires}
        return config

    def test_no_statement_and_too_little_time_means_you_cannot_bid(self):
        status = td.statement_status(self.config_with(None), "Dallas",
                                     date(2026, 9, 5), "2026-09-15")
        self.assertEqual(status["state"], "too_late")
        self.assertIn("cannot bid at this sale", status["message"])
        self.assertIn("next first Tuesday", status["message"])

    def test_no_statement_but_time_enough_says_apply_today(self):
        status = td.statement_status(self.config_with(None), "Dallas",
                                     date(2026, 9, 5), "2026-12-01")
        self.assertEqual(status["state"], "missing")
        self.assertIn("apply today", status["message"])

    def test_a_statement_expiring_before_sale_day_is_worthless(self):
        """Current today, useless on the day it is needed."""
        status = td.statement_status(self.config_with("2026-09-20"), "Dallas",
                                     date(2026, 9, 5), "2026-10-06")
        self.assertEqual(status["state"], "expires_before_sale")
        self.assertIn("worthless on sale day", status["message"])

    def test_a_statement_good_past_sale_day_is_current(self):
        status = td.statement_status(self.config_with("2027-01-01"), "Dallas",
                                     date(2026, 9, 5), "2026-10-06")
        self.assertEqual(status["state"], "current")

    def test_without_a_sale_date_nothing_changes(self):
        status = td.statement_status(self.config_with(None), "Dallas", date(2026, 9, 5))
        self.assertEqual(status["state"], "missing")
        self.assertNotIn("sale_date", status)


class DeadlineCalendar(unittest.TestCase):
    def test_the_prose_becomes_dates(self):
        due = td.deadlines(cfg(), "Dallas", "2026-10-06", date(2026, 9, 5))
        self.assertTrue(due)
        for item in due:
            self.assertRegex(item["due"], r"^\d{4}-\d{2}-\d{2}$")
            self.assertLess(item["due"], "2026-10-06")

    def test_they_are_ordered_earliest_first(self):
        due = td.deadlines(cfg(), "Dallas", "2026-10-06", date(2026, 9, 5))
        self.assertEqual([d["due"] for d in due], sorted(d["due"] for d in due))

    def test_a_passed_deadline_is_marked_missed(self):
        due = td.deadlines(cfg(), "Dallas", "2026-10-06", date(2026, 10, 1))
        self.assertTrue(any(d["missed"] for d in due))

    def test_no_sale_date_means_no_deadlines(self):
        self.assertEqual(td.deadlines(cfg(), "Dallas", None, date(2026, 9, 5)), [])


class RepeatOfferings(unittest.TestCase):
    """A property on the list three months running did not sell three times."""

    def setUp(self):
        import tempfile, shutil
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def _snapshot(self, day, bid):
        (self.tmp / f"{day}.json").write_text(json.dumps({"results": [
            {"listing": {"county": "Dallas", "account": "00000123456789000",
                         "minimum_opening_bid": bid}}]}))

    def test_it_counts_prior_offerings(self):
        for day, bid in (("2026-07-07", 12000), ("2026-08-04", 10000)):
            self._snapshot(day, bid)
        history = td.offer_history(date(2026, 9, 1), self.tmp)
        entry = history["dallas|acct|00000123456789000"]
        self.assertEqual(entry["times_offered"], 2)
        self.assertEqual(entry["first_seen"], "2026-07-07")

    def test_todays_own_snapshot_is_not_prior_history(self):
        self._snapshot("2026-09-01", 12000)
        self.assertEqual(td.offer_history(date(2026, 9, 1), self.tmp), {})

    def test_two_or_more_prior_offerings_flag(self):
        for day, bid in (("2026-07-07", 12000), ("2026-08-04", 10000)):
            self._snapshot(day, bid)
        result = td.screen(listing(), cad(), checks(), cfg(), TODAY)
        td.annotate_history(result, td.offer_history(date(2026, 9, 1), self.tmp), cfg())
        self.assertIn("offered_repeatedly", codes(result["flags"]))
        detail = next(f["detail"] for f in result["flags"] if f["code"] == "offered_repeatedly")
        self.assertIn("did not sell", detail)
        self.assertIn("$12,000", detail)

    def test_a_single_prior_offering_is_context_not_a_flag(self):
        self._snapshot("2026-08-04", 10000)
        result = td.screen(listing(), cad(), checks(), cfg(), TODAY)
        td.annotate_history(result, td.offer_history(date(2026, 9, 1), self.tmp), cfg())
        self.assertNotIn("offered_repeatedly", codes(result["flags"]))
        self.assertEqual(result["history"]["times_offered"], 1)

    def test_a_property_never_seen_before_gets_no_history(self):
        result = td.screen(listing(), cad(), checks(), cfg(), TODAY)
        td.annotate_history(result, {}, cfg())
        self.assertNotIn("history", result)

    def test_a_corrupt_snapshot_does_not_take_the_run_down(self):
        (self.tmp / "2026-07-07.json").write_text("{ not json")
        self.assertEqual(td.offer_history(date(2026, 9, 1), self.tmp), {})

    def test_a_listing_with_no_account_falls_back_to_the_cause_number(self):
        """The unmatched listings are exactly the ones that lack an account."""
        key = td.offer_key({"county": "Dallas", "cause_number": "TX-22-01188"})
        self.assertEqual(key, "dallas|cause|TX2201188")

    def test_and_to_the_address_when_there_is_no_cause_number_either(self):
        key = td.offer_key({"county": "Dallas", "address": "1417 S Harwood St"})
        self.assertEqual(key, "dallas|addr|1417sharwoodst")

    def test_the_same_address_in_two_counties_is_two_properties(self):
        self.assertNotEqual(td.offer_key({"county": "Dallas", "address": "1 Main"}),
                            td.offer_key({"county": "Ellis", "address": "1 Main"}))

    def test_a_listing_with_nothing_to_match_on_is_not_matched(self):
        self.assertEqual(td.offer_key({"county": "Dallas"}), "")

    def test_the_added_flag_re_tiers_the_row(self):
        """The flag arrives after screening, so the tier has to be recomputed.

        Otherwise the row reads Tier A beside the flags that disqualify it.
        """
        for day in ("2026-07-07", "2026-08-04"):
            self._snapshot(day, 10000)
        result = td.screen(listing(), cad(), checks(), cfg(), TODAY)
        before = result["tier"]
        td.annotate_history(result, td.offer_history(date(2026, 9, 1), self.tmp), cfg())
        self.assertEqual(result["minor_flags"], td.count_flags(result["flags"])[1])
        self.assertEqual(result["tier"],
                         td.gate5_tier(result["flags"], result["economics"],
                                       result["cad"], cfg()))
        self.assertIn(before, ("A", "B", "C"))

    def test_a_rejected_row_keeps_its_null_tier(self):
        for day in ("2026-07-07", "2026-08-04"):
            self._snapshot(day, 10000)
        result = td.screen(listing(status="Withdrawn"), cad(), checks(), cfg(), TODAY)
        td.annotate_history(result, td.offer_history(date(2026, 9, 1), self.tmp), cfg())
        self.assertIsNone(result["tier"])



class TheDocketAxis(unittest.TestCase):
    """Which sale a row belongs to is not a measure of the property.

    The first live run published 328 candidates under a "sale 2026-10-06"
    banner. 18 of them were on that docket. The other 310 carried the feed's
    own `Available for Future Sale`, which is not a defect, not an unknown, and
    not a reason to rank them lower — only a reason not to let them look like
    tomorrow's shortlist.
    """

    def result(self, sale_date=None, status="Active", screening_for=SALE, **extra):
        return td.screen(listing(sale_date=sale_date, status=status, **extra),
                         cad(), checks(), cfg(), TODAY, screening_for)

    def test_a_listing_set_for_this_sale_is_on_the_docket(self):
        docket = self.result(sale_date=SALE, status="Scheduled for Auction")["docket"]
        self.assertEqual(docket["state"], td.ON_DOCKET)
        self.assertTrue(docket["on_docket"])
        self.assertEqual(docket["label"], "yes")

    def test_the_feeds_own_words_are_read_not_treated_as_silence(self):
        for phrasing in ("Available for Future Sale", "Not Yet Scheduled",
                         "PENDING", "To Be Rescheduled"):
            with self.subTest(phrasing):
                docket = self.result(status=phrasing)["docket"]
                self.assertEqual(docket["state"], td.NOT_SCHEDULED)
                self.assertFalse(docket["on_docket"])

    def test_a_listing_for_a_different_sale_says_which(self):
        docket = self.result(sale_date="2026-11-03")["docket"]
        self.assertEqual(docket["state"], td.OTHER_SALE)
        self.assertEqual(docket["label"], "sale 2026-11-03")
        self.assertIn("2026-11-03", docket["detail"])

    def test_a_struck_off_listing_has_no_docket_to_be_on(self):
        docket = self.result(sale_type="struck_off")["docket"]
        self.assertEqual(docket["state"], td.OVER_THE_COUNTER)
        self.assertIn("any time", docket["detail"])

    def test_silence_with_no_explanation_stays_an_unknown(self):
        result = self.result(status="Active")
        self.assertEqual(result["docket"]["state"], td.DATE_UNKNOWN)
        self.assertIn("no_sale_date", codes(result["flags"]))

    def test_but_a_status_that_explains_the_silence_is_not_an_unknown(self):
        """`Available for Future Sale` answers the question the flag asks."""
        result = self.result(status="Available for Future Sale")
        self.assertNotIn("no_sale_date", codes(result["flags"]))

    def test_being_off_the_docket_is_never_a_flag(self):
        """It would rank rows, and it says nothing about the property.

        It would also drive 94% of a run into Tier C, which is the mistake
        `occupancy_unknown` carries severity `universal` to avoid.
        """
        off = self.result(status="Available for Future Sale")
        on = self.result(sale_date=SALE, status="Scheduled for Auction")
        self.assertEqual(codes(off["flags"]), codes(on["flags"]))
        self.assertEqual(off["tier"], on["tier"])

    def test_nor_a_rejection(self):
        self.assertEqual(self.result(status="Available for Future Sale")["status"],
                         "candidate")

    def test_screening_without_a_sale_date_does_not_invent_one(self):
        """Any published date is 'the' date when nothing was asked for."""
        docket = td.screen(listing(sale_date="2026-11-03"), cad(), checks(),
                           cfg(), TODAY)["docket"]
        self.assertEqual(docket["state"], td.ON_DOCKET)


class DocketOrdering(unittest.TestCase):
    def rows(self, *specs):
        out = []
        for sale_date, status in specs:
            out.append(td.screen(listing(sale_date=sale_date, status=status),
                                 cad(), checks(), cfg(), TODAY, SALE))
        return out

    def test_what_you_can_bid_on_sorts_first(self):
        rows = self.rows((None, "Available for Future Sale"),
                         ("2026-11-03", "Active"),
                         (SALE, "Scheduled for Auction"))
        rows.sort(key=lambda r: td.sort_key(r, td.county_order(cfg())))
        self.assertEqual([r["docket"]["state"] for r in rows],
                         [td.ON_DOCKET, td.NOT_SCHEDULED, td.OTHER_SALE])

    def test_the_docket_outranks_the_tier(self):
        """A Tier A property six weeks out is not tomorrow morning's problem."""
        later = td.screen(listing(sale_date="2026-11-03", minimum_opening_bid=1000.0),
                          cad(), checks(), cfg(), TODAY, SALE)
        now = td.screen(listing(sale_date=SALE, minimum_opening_bid=19000.0),
                        cad(), checks(), cfg(), TODAY, SALE)
        order = td.county_order(cfg())
        self.assertLess(td.sort_key(now, order), td.sort_key(later, order))


class DocketInTheOutputs(unittest.TestCase):
    def setUp(self):
        self.statements = td.statement_report(cfg(), ["Dallas"], TODAY, SALE)
        self.on = td.screen(listing(sale_date=SALE, status="Scheduled for Auction"),
                            cad(), checks(), cfg(), TODAY, SALE)
        self.off = td.screen(
            listing(sale_date=None, status="Available for Future Sale", account="99"),
            cad(), checks(), cfg(), TODAY, SALE)

    def test_the_sheet_has_a_column_for_it(self):
        self.assertIn("On This Docket", td.HEADERS)
        row = td._sheet_row(self.on)
        self.assertEqual(row[td.HEADERS.index("On This Docket")], "yes")
        self.assertEqual(td._sheet_row(self.off)[td.HEADERS.index("On This Docket")],
                         "not scheduled")

    def test_the_banner_gives_both_numbers(self):
        values, _ = td.sheet_rows([self.on, self.off], cfg(), TODAY, SALE, self.statements)
        self.assertIn("1 on this docket of 2 candidates", values[1][0])

    def test_a_packet_for_an_unscheduled_property_does_not_say_sale_none(self):
        text = td.packet_markdown(self.off, cfg(), self.statements[0])
        self.assertNotIn("Sale None", text)
        self.assertIn("Not scheduled for any sale yet", text)

    def test_and_carries_no_deadline_table_it_cannot_honour(self):
        text = td.packet_markdown(self.off, cfg(), self.statements[0])
        self.assertNotIn("Deadlines before this sale", text)

    def test_while_a_docketed_one_does(self):
        text = td.packet_markdown(self.on, cfg(), self.statements[0])
        self.assertIn(f"**Sale {SALE}**", text)
        self.assertIn("Deadlines before this sale", text)

    def test_an_unscheduled_packet_is_filed_away_from_the_sale(self):
        self.assertEqual(td.packet_path(self.off).parent.name, "undated")
        self.assertEqual(td.packet_path(self.on).parent.name, SALE)
