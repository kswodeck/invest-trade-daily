"""The gates that decide whether a tax deed listing reaches the shortlist.

The load-bearing ones are the four the task spec calls out, and each is here
because getting it wrong costs real money rather than a red test: a federal tax
lien that survives the sale, a lien check that could not run being read as a
clean one, a homestead's two-year redemption, and the arithmetic underneath
both exit routes.
"""

from __future__ import annotations

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
        self.assertEqual(len(td.HEADERS), 22)
        self.assertEqual(td.HEADERS[td.COL_TIER], "Tier")
        self.assertIn("Value Source", td.HEADERS)

    def test_counties_are_blocked_in_dallas_tarrant_johnson_ellis_order(self):
        banners = [self.values[row][0] for row in self.spec["county_rows"]]
        self.assertEqual([b.split()[0] for b in banners],
                         ["DALLAS", "TARRANT", "JOHNSON", "ELLIS"])

    def test_a_county_with_nothing_says_so_rather_than_being_omitted(self):
        text = "\n".join(str(row[0]) for row in self.values if row)
        self.assertIn("ELLIS COUNTY — 0 candidate(s)", text)
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

