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

    def test_the_cap_rejects_just_over_and_keeps_just_under(self):
        """Whatever the cap is set to, it has to bite exactly at it."""
        cap = td.threshold(cfg(), "MAX_OPENING_BID")
        over = td.screen(listing(minimum_opening_bid=cap + 1),
                         cad(appraised_value=cap * 20), checks(), cfg(), TODAY)
        self.assertIn("opening_bid_over_cap", codes(over["rejections"]))
        under = td.screen(listing(minimum_opening_bid=cap),
                          cad(appraised_value=cap * 20), checks(), cfg(), TODAY)
        self.assertNotIn("opening_bid_over_cap", codes(under["rejections"]))

    def test_but_it_never_touches_a_listing_with_no_published_bid(self):
        """The cap is a finding about a number. No number is not a finding.

        183 of the 2026-09-11 run's 252 tab rows published no bid at all, so
        the cap says nothing about them either way — they carry
        `no_opening_bid`, which flags and ranks them down. Rejecting them for
        an unknown is the mistake that hid 544 real candidates on the first
        live run.
        """
        result = td.screen(listing(minimum_opening_bid=None), cad(), checks(),
                           cfg(), TODAY)
        self.assertNotIn("opening_bid_over_cap", codes(result["rejections"]))
        self.assertIn("no_opening_bid", codes(result["flags"]))

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
        self.assertEqual(td.HEADERS[td.COL_TIER], "Tier")
        self.assertIn("Value Source", td.HEADERS)

    def test_every_data_row_has_a_cell_per_header(self):
        """The property a column count was standing in for.

        A literal 23 here had to be edited every time a column was added, which
        tested the edit rather than the grid. What matters is that no row is
        short: a data row with fewer cells than headers silently shifts every
        value after the gap into the wrong column.
        """
        self.assertTrue(self.spec["data_rows"], "no data rows to check")
        for index, _ in self.spec["data_rows"]:
            self.assertEqual(len(self.values[index]), len(td.HEADERS),
                             f"row {index} does not line up with the header")

    def test_city_sits_beside_county_because_it_is_read_with_it(self):
        self.assertEqual(td.HEADERS.index("City"), td.HEADERS.index("County") + 1)

    def test_counties_are_blocked_in_dallas_tarrant_johnson_ellis_order(self):
        banners = [self.values[row][0] for row in self.spec["county_rows"]]
        self.assertEqual([b.split()[0] for b in banners],
                         ["DALLAS", "TARRANT", "JOHNSON", "ELLIS"])

    def test_a_county_with_nothing_says_so_rather_than_being_omitted(self):
        text = "\n".join(str(row[0]) for row in self.values if row)
        self.assertIn("ELLIS COUNTY — 0 on the 2026-10-06 docket · 0 shown", text)
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
        configured = (config.get("thresholds") or {})["MAX_OPENING_BID"]
        self.assertEqual(td.threshold(config, "MAX_OPENING_BID"), configured)
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
        self.assertIn("1 on this docket of 1 shown", values[1][0])
        self.assertIn("1 not-yet-scheduled candidate(s) held off", values[1][0])

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


class CommercialAndIndustrialAreRejectedWhenTheUseWasRead(unittest.TestCase):
    """The gate's own rule, applied to one more field.

    A use that was read and is commercial disqualifies. A use nothing published
    is an unknown, and an unknown has never rejected anything in this module —
    that is the rule that stopped 544 real candidates being thrown away on the
    first live run, and it applies here whether or not it makes the filter look
    busy today.
    """

    def screened(self, cad_over=None, **listing_over):
        return td.screen(listing(**listing_over), cad(**(cad_over or {})), checks(),
                         cfg(), TODAY)

    def test_an_sptb_commercial_category_rejects(self):
        result = self.screened({"land_use_code": "F1"})
        self.assertIn("commercial_or_industrial", codes(result["rejections"]))

    def test_so_does_industrial(self):
        self.assertIn("commercial_or_industrial",
                      codes(self.screened({"land_use_code": "F2"})["rejections"]))

    def test_and_personal_commercial_and_industrial_and_utilities(self):
        for code in ("L1", "L2", "J3", "J"):
            with self.subTest(code=code):
                result = self.screened({"land_use_code": code})
                self.assertIn("commercial_or_industrial", codes(result["rejections"]))

    def test_single_family_is_kept(self):
        result = self.screened({"land_use_code": "A"})
        self.assertNotIn("commercial_or_industrial", codes(result["rejections"]))
        self.assertNotIn("property_use_unknown", codes(result["flags"]))

    def test_and_so_are_the_other_residential_and_land_categories(self):
        for code in ("A1", "B", "C1", "D1", "E", "M1", "O"):
            with self.subTest(code=code):
                result = self.screened({"land_use_code": code})
                self.assertNotIn("commercial_or_industrial", codes(result["rejections"]),
                                 f"{code} is residential or land, not commercial")

    def test_a_use_description_rejects_when_there_is_no_code(self):
        result = self.screened({"land_use_code": None,
                                "land_use_description": "Warehouse / Light Industrial"})
        self.assertIn("commercial_or_industrial", codes(result["rejections"]))

    def test_the_county_lists_own_property_type_is_enough(self):
        result = self.screened({"land_use_code": None, "land_use_description": None},
                               property_type="COMMERCIAL - RETAIL STRIP")
        self.assertIn("commercial_or_industrial", codes(result["rejections"]))

    def test_a_residential_property_type_is_a_determination_not_an_unknown(self):
        result = self.screened({"land_use_code": None, "land_use_description": None},
                               property_type="Single Family Residence")
        self.assertNotIn("property_use_unknown", codes(result["flags"]))

    def test_nothing_readable_flags_and_never_rejects(self):
        """The common case today, and the one that must not turn into a reject."""
        result = self.screened({"land_use_code": None, "land_use_description": None},
                               property_type="")
        self.assertNotIn("commercial_or_industrial", codes(result["rejections"]))
        self.assertIn("property_use_unknown", codes(result["flags"]))
        self.assertEqual(result["status"], "candidate")

    def test_and_the_unknown_costs_the_property_its_rank(self):
        """Material, so it can never read as a clean screen."""
        result = self.screened({"land_use_code": None, "land_use_description": None},
                               property_type="")
        entry = next(f for f in result["flags"] if f["code"] == "property_use_unknown")
        self.assertEqual(entry["severity"], td.MATERIAL)

    def test_the_street_address_is_never_evidence(self):
        """It reads commercial to a person. This module does not infer."""
        result = self.screened({"land_use_code": None, "land_use_description": None},
                               property_type="", address="11970 N CENTRAL EXPY")
        self.assertNotIn("commercial_or_industrial", codes(result["rejections"]))

    def test_nor_is_a_subdivision_platted_as_industrial(self):
        """A house on a lot inside INDUSTRIAL ADDITION is a house."""
        result = self.screened(
            {"land_use_code": "A", "land_use_description": None},
            legal_description="INDUSTRIAL ADDITION BLOCK 4 LOT 7")
        self.assertNotIn("commercial_or_industrial", codes(result["rejections"]))

    def test_the_rejection_names_the_field_that_said_so(self):
        result = self.screened({"land_use_code": "F1"})
        detail = next(r for r in result["rejections"]
                      if r["code"] == "commercial_or_industrial")["detail"]
        self.assertIn("F1", detail)
        self.assertIn("CAD", detail)

    def test_it_runs_when_no_appraisal_district_record_matched(self):
        """Placed after the `if not cad` block, this never ran at all.

        That block returns in both branches, and no row in the 2026-09-11 run
        has a CAD record — so the filter read as working, rejected nothing, and
        flagged nothing either. It does not need a CAD: the county list's own
        property type answers it when the feed publishes one.
        """
        result = td.screen(listing(property_type="COMMERCIAL WAREHOUSE"), None,
                           checks(), cfg(), TODAY)
        self.assertIn("commercial_or_industrial", codes(result["rejections"]))

    def test_and_flags_the_unknown_when_no_record_matched_either(self):
        result = td.screen(listing(property_type=""), None, checks(), cfg(), TODAY)
        self.assertIn("property_use_unknown", codes(result["flags"]))

    def test_the_whole_of_a_real_run_gets_the_flag_rather_than_none_of_it(self):
        """The shape of the bug, at run scale: 224 rows or 0, never in between.

        Every row of that run lacks a CAD record and a property type, so the
        honest output is the flag on all of them. Zero was the symptom.
        """
        # The fixture publishes a property type; that run's rows do not.
        rows = [td.screen(listing(account=str(n), property_type=""), None,
                          checks(), cfg(), TODAY)
                for n in range(5)]
        flagged = sum(1 for r in rows
                      if any(f["code"] == "property_use_unknown" for f in r["flags"]))
        self.assertEqual(flagged, len(rows))

    def test_it_can_be_turned_off_into_a_flag_without_becoming_silent(self):
        config = dict(cfg(), thresholds=dict(cfg().get("thresholds") or {},
                                             REJECT_COMMERCIAL_USE=False))
        result = td.screen(listing(), cad(land_use_code="F1"), checks(), config, TODAY)
        self.assertNotIn("commercial_or_industrial", codes(result["rejections"]))
        entry = next(f for f in result["flags"] if f["code"] == "commercial_or_industrial")
        self.assertEqual(entry["severity"], td.MATERIAL)


class TheRadiusRejectsWhatWasMeasuredAndFlagsWhatWasNot(unittest.TestCase):
    """MAX_MILES_FROM_BASE: 35 straight-line miles from Mansfield (40 until 2026-10-03).

    A distance that was measured and is past the line rejects, like a bid over
    the cap. One that could not be measured flags, because an unknown has never
    rejected anything here — and a city that cannot be where the property is
    (a mailing city, a geocoder match in another Texas town) is reported as
    unknown rather than as far away, because rejecting on it would be a finding
    the run never made.
    """

    def screened(self, **over):
        return td.screen(listing(**over), cad(), checks(), cfg(), TODAY)

    def test_the_base_is_mansfields_own_center(self):
        label, lat, lon = td.home_base(cfg())
        self.assertEqual(label, "Mansfield, TX")
        self.assertAlmostEqual(lat, 32.563, places=2)
        self.assertAlmostEqual(lon, -97.142, places=2)

    def test_the_great_circle_is_right_on_a_known_pair(self):
        """Dallas to Fort Worth city centers: about 30 miles, by any atlas."""
        dallas = td.find_place("Dallas")
        fort_worth = td.find_place("Fort Worth")
        miles = td.haversine_miles(dallas[1:3], fort_worth[1:3])
        self.assertGreater(miles, 28)
        self.assertLess(miles, 32)

    def test_a_city_past_the_line_is_rejected_with_its_distance(self):
        result = self.screened(city="Rowlett", county="Dallas")
        rejection = next(r for r in result["rejections"] if r["code"] == "outside_radius")
        self.assertIn("Rowlett", rejection["detail"])
        self.assertIn("41.0", rejection["detail"])
        self.assertIn("MAX_MILES_FROM_BASE", rejection["detail"])

    def test_each_city_lands_on_the_side_of_the_line_its_distance_says(self):
        """Judged against the configured radius, never a remembered one.

        This used to list Garland and Seagoville as "inside", which was true at
        40 miles and false the day the line moved to 35 — a test of the old
        setting rather than of the gate. Now every city is measured and must be
        kept exactly when it is within the line and rejected exactly when not.
        """
        radius = float(td.threshold(cfg(), "MAX_MILES_FROM_BASE"))
        cities = [("Mansfield", "Tarrant"), ("Fort Worth", "Tarrant"), ("Dallas", "Dallas"),
                  ("Mesquite", "Dallas"), ("Seagoville", "Dallas"), ("Richardson", "Dallas"),
                  ("Garland", "Dallas"), ("Rowlett", "Dallas"), ("Sachse", "Dallas")]
        sides = set()
        for city, county in cities:
            with self.subTest(city=city):
                miles = td.locate({"city": city, "county": county}, cfg())["miles"]
                result = self.screened(city=city, county=county)
                rejected = "outside_radius" in codes(result["rejections"])
                self.assertEqual(rejected, miles > radius,
                                 f"{city} at {miles} mi against a {radius:g}-mile line")
                self.assertNotIn("distance_unknown", codes(result["flags"]))
                sides.add(rejected)
        self.assertEqual(sides, {True, False},
                         "the sample no longer straddles the line, so it tests one side only")

    def test_the_configured_radius_is_35_miles(self):
        """The requested setting, pinned once, in one place, on purpose."""
        self.assertEqual(float(td.threshold(cfg(), "MAX_MILES_FROM_BASE")), 35.0)
        self.assertEqual(float(td.DEFAULT_THRESHOLDS["MAX_MILES_FROM_BASE"]), 35.0,
                         "the built-in default and the config should not disagree")

    def test_the_line_is_inclusive_at_exactly_the_radius(self):
        config = cfg()
        rowlett = td.locate({"city": "Rowlett", "county": "Dallas"}, config)["miles"]
        at_line = dict(config, thresholds=dict(config["thresholds"],
                                               MAX_MILES_FROM_BASE=rowlett))
        result = td.screen(listing(city="Rowlett", county="Dallas"), cad(), checks(),
                           at_line, TODAY)
        self.assertNotIn("outside_radius", codes(result["rejections"]))

    def test_moving_the_line_moves_the_answer(self):
        config = cfg()
        wider = dict(config, thresholds=dict(config["thresholds"], MAX_MILES_FROM_BASE=45))
        result = td.screen(listing(city="Rowlett", county="Dallas"), cad(), checks(),
                           wider, TODAY)
        self.assertNotIn("outside_radius", codes(result["rejections"]))

    def test_zero_turns_the_radius_off_entirely(self):
        config = cfg()
        off = dict(config, thresholds=dict(config["thresholds"], MAX_MILES_FROM_BASE=0))
        result = td.screen(listing(city="Rowlett", county="Dallas"), cad(), checks(),
                           off, TODAY)
        self.assertNotIn("outside_radius", codes(result["rejections"]))
        self.assertNotIn("distance_unknown", codes(result["flags"]))
        self.assertIsNone(td.home_base(off))

    def test_a_feed_truncated_at_16_characters_still_resolves(self):
        """Tarrant's list cuts every city at 16 characters."""
        where = td.locate({"city": "North Richland H", "county": "Tarrant"}, cfg())
        self.assertEqual(where["place"], "North Richland Hills")
        self.assertIsNotNone(where["miles"])

    def test_but_a_short_prefix_is_a_guess_and_is_not_taken(self):
        self.assertIsNone(td.find_place("Lake"))
        self.assertIsNone(td.find_place("North"))

    def test_spelling_differences_of_case_resolve(self):
        self.assertEqual(td.find_place("Desoto")[0], "DeSoto")

    def test_no_city_flags_and_never_rejects(self):
        result = self.screened(city="", address="1 NOWHERE RD", county="Dallas")
        self.assertNotIn("outside_radius", codes(result["rejections"]))
        entry = next(f for f in result["flags"] if f["code"] == "distance_unknown")
        self.assertEqual(entry["severity"], td.MATERIAL)

    def test_a_town_too_small_for_the_table_flags_and_never_rejects(self):
        result = self.screened(city="Westworth Villag", address="1 X ST", county="Tarrant")
        self.assertEqual(result["status"], "candidate")
        self.assertIn("distance_unknown", codes(result["flags"]))

    def test_a_city_that_cannot_be_in_this_county_is_unknown_not_far(self):
        """Houston on a Dallas County listing is a wrong city, not a far lot.

        Rejecting it at 225 miles would turn a data error into a finding.
        """
        result = self.screened(city="Houston", address="1 X ST", county="Dallas")
        self.assertNotIn("outside_radius", codes(result["rejections"]))
        detail = next(f for f in result["flags"] if f["code"] == "distance_unknown")["detail"]
        self.assertIn("seat", detail)

    def test_a_city_straddling_the_county_line_is_believed(self):
        """Grand Prairie is listed by Tarrant though GeoNames files it in Dallas."""
        where = td.locate({"city": "Grand Prairie", "county": "Tarrant"}, cfg())
        self.assertIsNotNone(where["miles"])

    def test_a_geocoded_parcel_point_beats_its_citys_center(self):
        """Dallas's center is inside; its far north-east corner is not."""
        far_ne_dallas = (32.95, -96.55)
        where = td.locate({"city": "Dallas", "county": "Dallas",
                           "lat": far_ne_dallas[0], "lon": far_ne_dallas[1]}, cfg())
        self.assertGreater(where["miles"], 40)
        self.assertIn("parcel", where["basis"])

    def test_but_a_geocoded_point_in_the_wrong_place_is_not_used(self):
        """A Wayne Street matched in Houston must not measure a Dallas lot."""
        houston = td.find_place("Houston")
        where = td.locate({"city": "Dallas", "county": "Dallas",
                           "lat": houston[1], "lon": houston[2]}, cfg())
        self.assertEqual(where["place"], "Dallas")
        self.assertLess(where["miles"], 40)

    def test_the_check_runs_with_no_appraisal_district_record(self):
        """The commercial filter shipped after an early return once. Not twice."""
        result = td.screen(listing(city="Rowlett", county="Dallas"), None, checks(),
                           cfg(), TODAY)
        self.assertIn("outside_radius", codes(result["rejections"]))

    def test_the_sheet_shows_the_miles_and_the_full_city_name(self):
        statements = td.statement_report(cfg(), ["Tarrant"], TODAY, SALE)
        row = td.screen(listing(city="North Richland H", county="Tarrant"), cad(),
                        checks(), cfg(), TODAY, SALE)
        values, spec = td.sheet_rows([row], cfg(), TODAY, SALE, statements)
        index, _ = spec["data_rows"][0]
        self.assertEqual(values[index][td.HEADERS.index("City")], "North Richland Hills")
        self.assertIsInstance(values[index][td.HEADERS.index("Miles")], float)

    def test_an_unresolvable_base_refuses_to_run_rather_than_skip_the_filter(self):
        config = dict(cfg(), home_base={"place": "Nowhereville", "lat": None, "lon": None})
        with self.assertRaises(SystemExit):
            td.home_base(config)


class PreferredCitiesAreHighlightedAndTrumpTheRadius(unittest.TestCase):
    """Nineteen named cities, highlighted light green and never cut by distance.

    They trump the radius and nothing else. Every other gate — the bid cap,
    the commercial filter, homestead — still applies, because the request was
    about distance and a preference for a town is not a reason to buy a
    warehouse in it.
    """

    def with_radius(self, miles, extra=None):
        config = cfg()
        config = dict(config, thresholds=dict(config["thresholds"], MAX_MILES_FROM_BASE=miles))
        if extra is not None:
            config = dict(config, preferred_cities=dict(config["preferred_cities"],
                                                        cities=extra))
        return config

    def test_the_configured_list_is_the_one_asked_for(self):
        names = td.preferred_cities(cfg())
        self.assertEqual(len(names), 19)
        for city in ("Mansfield", "Irving", "Carrollton", "Rendon", "Venus"):
            self.assertIn(city, names)

    def test_waxahachie_is_spelled_so_it_can_match(self):
        """The request read "Waxahatchie", which no row would ever say."""
        self.assertIn("Waxahachie", td.preferred_cities(cfg()))
        self.assertNotIn("Waxahatchie", td.preferred_cities(cfg()))
        self.assertIsNotNone(td.find_place("Waxahachie"))

    def test_every_configured_city_is_one_the_place_table_knows(self):
        """A typo here would silently highlight nothing, forever."""
        for city in td.preferred_cities(cfg()):
            with self.subTest(city=city):
                self.assertIsNotNone(td.find_place(city), city)

    def test_a_row_in_a_preferred_city_is_recognised(self):
        self.assertEqual(td.preferred_city({"city": "Arlington", "county": "Tarrant"}, cfg()),
                         "Arlington")

    def test_case_does_not_matter(self):
        self.assertEqual(td.preferred_city({"city": "GRAND PRAIRIE", "county": "Dallas"},
                                           cfg()), "Grand Prairie")

    def test_a_name_truncated_by_the_feed_still_counts(self):
        self.assertEqual(td.preferred_city({"city": "North Richland H", "county": "Tarrant"},
                                           cfg()), "North Richland Hills")

    def test_matching_is_exact_never_a_substring(self):
        only_richland = self.with_radius(35, extra=["Richland Hills"])
        self.assertIsNone(td.preferred_city({"city": "North Richland Hills",
                                             "county": "Tarrant"}, only_richland))
        self.assertIsNone(td.preferred_city({"city": "Dallas", "county": "Dallas"}, cfg()))

    def test_a_preferred_city_past_the_line_is_kept(self):
        tight = self.with_radius(5)
        irving = td.screen(listing(city="Irving", county="Dallas"), cad(), checks(),
                           tight, TODAY)
        dallas = td.screen(listing(city="Dallas", county="Dallas"), cad(), checks(),
                           tight, TODAY)
        self.assertNotIn("outside_radius", codes(irving["rejections"]))
        self.assertIn("outside_radius", codes(dallas["rejections"]),
                      "the same radius still cuts a city that is not preferred")

    def test_and_is_never_flagged_as_unmeasured(self):
        """The question the radius asks has been answered by the user."""
        config = self.with_radius(35, extra=["Westworth Village"])
        result = td.screen(listing(city="Westworth Village", county="Tarrant"), cad(),
                           checks(), config, TODAY)
        self.assertNotIn("distance_unknown", codes(result["flags"]))

    def test_it_trumps_the_radius_and_nothing_else(self):
        result = td.screen(listing(city="Mansfield", county="Tarrant",
                                   minimum_opening_bid=50000.0),
                           cad(), checks(), cfg(), TODAY)
        self.assertIn("opening_bid_over_cap", codes(result["rejections"]))
        result = td.screen(listing(city="Mansfield", county="Tarrant"),
                           cad(land_use_code="F1"), checks(), cfg(), TODAY)
        self.assertIn("commercial_or_industrial", codes(result["rejections"]))

    def test_the_sheet_writes_the_configured_name_the_highlight_rule_matches(self):
        statements = td.statement_report(cfg(), ["Tarrant"], TODAY, SALE)
        row = td.screen(listing(city="North Richland H", county="Tarrant"), cad(),
                        checks(), cfg(), TODAY, SALE)
        values, spec = td.sheet_rows([row], cfg(), TODAY, SALE, statements)
        index, _ = spec["data_rows"][0]
        self.assertEqual(values[index][td.HEADERS.index("City")], "North Richland Hills")
        self.assertIn("North Richland Hills", spec["preferred"]["cities"])
        self.assertEqual(spec["preferred"]["column"], td.HEADERS.index("City"))
        self.assertIn("light green", values[1][0], "the banner says what the green means")

    def test_the_highlight_is_light_green_and_not_tier_as_green(self):
        color = td.highlight_color(cfg())
        self.assertEqual(color, {"red": 0.714, "green": 0.843, "blue": 0.659})
        tier_a = {"red": 0.85, "green": 0.94, "blue": 0.86}
        self.assertGreater(sum(abs(color[k] - tier_a[k]) for k in color), 0.25,
                           "close enough to Tier A's tint to be mistaken for it")

    def test_a_malformed_color_refuses_rather_than_painting_garbage(self):
        bad = dict(cfg(), preferred_cities={"cities": ["Mansfield"], "highlight": "green"})
        with self.assertRaises(SystemExit):
            td.highlight_color(bad)


class TheCityComesFromTheBestSourceThatHasIt(unittest.TestCase):
    """Three sources, not equally good, so the row records which answered.

    And a blank means **not determined**, never "no city": plenty of this
    inventory is unincorporated county land where the answer is legitimately
    not a city name. Nothing here fills it in from the county.
    """

    def test_the_county_list_wins_when_it_publishes_one(self):
        self.assertEqual(td.city_of({"city": "Grand Prairie"},
                                    {"situs": "1 MAIN ST, DALLAS, TX 75201"},
                                    {"city": "Irving"}),
                         ("Grand Prairie", "county list"))

    def test_the_cad_situs_is_next(self):
        city, source = td.city_of({}, {"situs": "1234 MAIN ST, DUNCANVILLE, TX 75116"},
                                  {"city": "Irving"})
        self.assertEqual((city, source), ("Duncanville", "CAD situs"))

    def test_the_geocoder_is_last_because_it_is_a_guess(self):
        self.assertEqual(td.city_of({}, None, {"city": "Irving"}), ("Irving", "geocoder"))

    def test_nothing_is_blank_and_never_the_county_name(self):
        city, source = td.city_of({"county": "Dallas"}, None, None)
        self.assertEqual(city, "")
        self.assertEqual(source, "")

    def test_an_all_caps_city_is_title_cased_for_reading(self):
        self.assertEqual(td.city_of({"city": "MESQUITE"}, None)[0], "Mesquite")

    def test_a_mixed_case_city_is_left_exactly_as_published(self):
        self.assertEqual(td.city_of({"city": "DeSoto"}, None)[0], "DeSoto")

    def test_a_situs_with_no_city_field_is_not_mined_for_one(self):
        self.assertEqual(td.city_of({}, {"situs": "1234 MAIN ST"}), ("", ""))

    def test_nor_is_a_situs_whose_city_slot_is_a_number(self):
        """A trailing ZIP shifted into the city slot is not a city."""
        self.assertEqual(td.city_of({}, {"situs": "1234 MAIN ST, 75201, TX"}), ("", ""))

    def test_the_sheet_carries_it_and_the_source_does_not_leak_into_the_cell(self):
        statements = td.statement_report(cfg(), ["Dallas"], TODAY, SALE)
        row = td.screen(listing(city="Mesquite"), cad(), checks(), cfg(), TODAY, SALE)
        row["listing"]["city_source"] = "county list"
        values, spec = td.sheet_rows([row], cfg(), TODAY, SALE, statements)
        index, _ = spec["data_rows"][0]
        self.assertEqual(values[index][td.HEADERS.index("City")], "Mesquite")


class TheTabCarriesWhatCanBeActedOn(unittest.TestCase):
    """565 of one run's 820 candidates were inventory with no auction at all.

    Scrolling past them to reach the 20 you can bid on is how a working tool
    stops being used. `SHEET_DOCKETS` keeps them off the tab — and off the tab
    only: they are still screened, still tiered, still counted, still in the
    snapshot that `offer_history` reads.
    """

    def setUp(self):
        self.statements = td.statement_report(cfg(), ["Dallas"], TODAY, SALE)

    def row(self, **over):
        return td.screen(listing(**over), cad(), checks(), cfg(), TODAY, SALE)

    def tab(self, results, dockets=None):
        config = cfg()
        if dockets is not None:
            config = dict(config, thresholds=dict(config.get("thresholds") or {},
                                                  SHEET_DOCKETS=dockets))
        return td.sheet_rows(results, config, TODAY, SALE, self.statements)

    def test_an_unscheduled_auction_listing_is_not_published(self):
        off = self.row(sale_date=None, status="Available for Future Sale")
        _, spec = self.tab([off])
        self.assertEqual(spec["data_rows"], [])

    def test_a_struck_off_listing_is_published_despite_having_no_sale_date(self):
        """The reason this reads the docket state and not the sale date.

        Struck-off property has no auction and never will — it is bought from
        the county across the counter, today. A "has a date" filter would have
        deleted all 235 of them from a live run.
        """
        otc = self.row(sale_date=None, sale_type="struck_off")
        self.assertEqual(otc["docket"]["state"], td.OVER_THE_COUNTER)
        _, spec = self.tab([otc])
        self.assertEqual(len(spec["data_rows"]), 1)

    def test_an_on_docket_listing_is_published(self):
        _, spec = self.tab([self.row(sale_date=SALE)])
        self.assertEqual(len(spec["data_rows"]), 1)

    def test_a_listing_for_another_sale_is_published(self):
        _, spec = self.tab([self.row(sale_date="2026-11-03")])
        self.assertEqual(len(spec["data_rows"]), 1)

    def test_an_unreadable_date_is_published_because_it_may_be_this_docket(self):
        """No date *and no reason given* might be a date we failed to read.

        Hiding a row that could be biddable is the failure this module exists
        to avoid, so the benefit of the doubt goes to showing it.
        """
        unknown = self.row(sale_date=None, status="Active")
        self.assertEqual(unknown["docket"]["state"], td.DATE_UNKNOWN)
        _, spec = self.tab([unknown])
        self.assertEqual(len(spec["data_rows"]), 1)

    def test_the_held_back_rows_are_not_rejected(self):
        off = self.row(sale_date=None, status="Available for Future Sale")
        self.tab([off])
        self.assertEqual(off["status"], "candidate")
        self.assertEqual(off["rejections"], [])
        self.assertIsNotNone(off["tier"])

    def test_and_the_tab_says_how_many_it_held_back(self):
        """A tab quietly showing fewer rows than the run found is its own lie."""
        rows, _ = self.tab([self.row(sale_date=SALE),
                            self.row(sale_date=None, account="9",
                                     status="Available for Future Sale")])
        self.assertIn("1 not-yet-scheduled candidate(s) held off this tab", rows[1][0])
        self.assertIn("SHEET_DOCKETS", rows[1][0])
        self.assertIn("in the snapshot", rows[1][0])

    def test_the_county_header_counts_match_the_rows_under_it(self):
        rows, spec = self.tab([self.row(sale_date=SALE),
                               self.row(sale_date=None, account="9",
                                        status="Available for Future Sale")])
        header = rows[spec["county_rows"][0]][0]
        self.assertIn("1 shown of 2 listed", header)
        self.assertIn("1 not yet scheduled, held off this tab", header)

    def test_it_is_configurable_back_to_everything(self):
        off = self.row(sale_date=None, status="Available for Future Sale")
        _, spec = self.tab([off], dockets="on_docket,over_the_counter,other_sale,"
                                          "date_unknown,not_scheduled")
        self.assertEqual(len(spec["data_rows"]), 1)

    def test_the_snapshot_still_records_every_candidate(self):
        """`offer_history` reads snapshots — a row off the tab must still be in it."""
        off = self.row(sale_date=None, status="Available for Future Sale")
        on = self.row(sale_date=SALE, account="9")
        payload = td.snapshot([off, on], cfg(), TODAY, SALE, self.statements, [])
        self.assertEqual(len(payload["results"]), 2)

    def note(self, results, **kw):
        rows, spec = self.tab(results, **kw)
        return " ".join(str(rows[i][0]) for i in spec["note_rows"])

    def test_an_emptied_county_is_not_reported_as_having_failed_the_gates(self):
        """The distinction the whole module turns on, in the one place it shows.

        A county block goes empty for three different reasons and they must not
        share a sentence. A held-back row passed every gate; saying it did not
        is a finding the run never made.
        """
        off = self.row(sale_date=None, status="Available for Future Sale")
        note = self.note([off])
        self.assertIn("none of them on a docket", note)
        self.assertIn("still screened and in the snapshot", note)
        self.assertNotIn("no listing survived the gates", note)

    def test_a_county_whose_listings_were_all_rejected_still_says_so(self):
        rejected = td.screen(listing(sale_date=SALE), cad(homestead=True), checks(),
                             cfg(), TODAY, SALE)
        self.assertEqual(rejected["status"], "rejected")
        self.assertIn("no listing survived the gates", self.note([rejected]))

    def test_a_county_that_published_nothing_says_that_instead(self):
        self.assertIn("no listing published", self.note([]))
