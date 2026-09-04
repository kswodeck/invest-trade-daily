"""Parsers for the four county list formats, against archived-shape fixtures.

See `tests/fixtures/tax_deeds/README.md` for what these fixtures are and — more
importantly — what they are not. They pin the parsers against the shapes the
counties publish. They cannot tell you the live page still looks like this;
`scripts/tax_deed_sources.py verify` is what does that, and the tests at the
bottom cover it failing loudly rather than quietly returning nothing.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "tax_deeds"
sys.path.insert(0, str(REPO / "scripts"))

import tax_deeds as td  # noqa: E402
import tax_deed_sources as tds  # noqa: E402


def fixture(name: str) -> str:
    return (FIXTURES / name).read_text()


def source_for(county_name: str, index: int = 0) -> dict:
    cfg = td.load_config()
    county = next(c for c in td.counties(cfg) if c["name"] == county_name)
    return county["sources"][index]


def parse_html(county_name: str, name: str, index: int = 0):
    source = source_for(county_name, index)
    return tds.rows_from_tables(fixture_tables(name), source["column_map"])


def fixture_tables(name: str):
    return tds.collect_tables(fixture(name))


class DallasRealAuction(unittest.TestCase):
    """Online RealAuction portal: an `Opening Bid` column and a status column."""

    def setUp(self):
        self.rows, self.diag = parse_html("Dallas", "dallas_realauction.html")

    def test_every_listing_is_read(self):
        self.assertEqual(len(self.rows), 5)

    def test_the_columns_that_matter_are_mapped(self):
        for field in ("account", "cause_number", "minimum_opening_bid", "sale_date",
                      "owner_name", "status"):
            self.assertIn(field, self.diag["mapped"])

    def test_a_row_normalizes_into_the_shape_the_gates_expect(self):
        listing = tds.normalize_listing(self.rows[0], "Dallas",
                                        source_for("Dallas"), td.load_config())
        self.assertEqual(listing["account"], "00000123456789000")
        self.assertEqual(listing["cause_number"], "TX-22-01188")
        self.assertEqual(listing["minimum_opening_bid"], 8450.0)
        self.assertEqual(listing["sale_date"], "2026-10-06")
        self.assertEqual(listing["sale_type"], "auction")
        self.assertEqual(listing["county"], "Dallas")

    def test_the_detail_link_becomes_an_absolute_listing_url(self):
        listing = tds.normalize_listing(self.rows[0], "Dallas",
                                        source_for("Dallas"), td.load_config())
        self.assertTrue(listing["listing_url"].startswith("http"))
        self.assertIn("00000123456789000", listing["listing_url"])

    def test_a_cancelled_row_keeps_its_status_so_gate_1_can_reject_it(self):
        cancelled = [r for r in self.rows if "Cancelled" in r.get("status", "")]
        self.assertEqual(len(cancelled), 1)
        listing = tds.normalize_listing(cancelled[0], "Dallas",
                                        source_for("Dallas"), td.load_config())
        result = td.screen(listing, None, [], td.load_config(), date(2026, 9, 3))
        self.assertIn("withdrawn", {r["code"] for r in result["rejections"]})


class TarrantAggregator(unittest.TestCase):
    """One page carries several counties; only ours may come through."""

    def setUp(self):
        self.cfg = td.load_config()
        self.source = source_for("Tarrant")
        self.rows, self.diag = parse_html("Tarrant", "tarrant_lgbs.html")

    def test_the_aggregate_table_parses_in_full(self):
        self.assertEqual(len(self.rows), 4)

    def test_the_county_filter_keeps_only_tarrant(self):
        kept = []
        for raw in self.rows:
            blob = " ".join(str(v) for v in raw.values()).lower()
            if self.source["county_filter"].lower() in blob:
                kept.append(raw)
        self.assertEqual(len(kept), 2)
        self.assertTrue(all("FORT WORTH" in r["address"] for r in kept))

    def test_money_and_dates_normalize(self):
        listing = tds.normalize_listing(self.rows[0], "Tarrant", self.source, self.cfg)
        self.assertEqual(listing["minimum_opening_bid"], 7800.0)
        self.assertEqual(listing["adjudged_value"], 63000.0)
        self.assertEqual(listing["sale_date"], "2026-10-06")


class JohnsonConstable(unittest.TestCase):
    """The real table is nested two layout tables deep, and dates are long-form."""

    def setUp(self):
        self.rows, self.diag = parse_html("Johnson", "johnson_constable.html")

    def test_the_nested_table_is_found_not_the_layout_wrappers(self):
        self.assertEqual(len(fixture_tables("johnson_constable.html")), 3)
        self.assertEqual(len(self.rows), 2)

    def test_a_long_form_date_parses(self):
        listing = tds.normalize_listing(self.rows[0], "Johnson",
                                        source_for("Johnson"), td.load_config())
        self.assertEqual(listing["sale_date"], "2026-10-06")
        self.assertEqual(listing["minimum_opening_bid"], 3900.0)

    def test_a_br_inside_a_cell_becomes_a_space_not_a_run_on(self):
        self.assertIn("WESTHILL ADDITION, CLEBURNE 1802 W HENDERSON",
                      self.rows[0]["legal_description"])


class EllisManualCsv(unittest.TestCase):
    """The escape hatch for a county that publishes only a PDF."""

    def setUp(self):
        self.source = source_for("Ellis")
        self.rows, self.diag = tds.rows_from_csv(fixture("ellis_manual.csv"),
                                                 self.source["column_map"])

    def test_the_csv_parses(self):
        self.assertEqual(len(self.rows), 3)
        self.assertIn("minimum_opening_bid", self.diag["mapped"])

    def test_quoted_commas_survive(self):
        listing = tds.normalize_listing(self.rows[0], "Ellis", self.source,
                                        td.load_config())
        self.assertEqual(listing["address"], "604 W MARVIN AVE, WAXAHACHIE, TX 75165")
        self.assertEqual(listing["minimum_opening_bid"], 5600.0)

    def test_a_mobile_home_only_row_is_rejected_downstream(self):
        row = next(r for r in self.rows if "MOBILE HOME" in r["legal_description"])
        listing = tds.normalize_listing(row, "Ellis", self.source, td.load_config())
        result = td.screen(listing, {"appraised_value": 8400.0, "land_value": 0,
                                     "exemptions": []},
                           [], td.load_config(), date(2026, 9, 3))
        self.assertIn("mobile_home_without_land", {r["code"] for r in result["rejections"]})


class AppraisalDistrictRecords(unittest.TestCase):
    def test_dcad_label_value_pairs_parse(self):
        record = tds.parse_cad_record(fixture("dcad_account.html"))
        self.assertEqual(record["appraised_value"], 74300.0)
        self.assertEqual(record["land_value"], 22000.0)
        self.assertEqual(record["improvement_value"], 52300.0)
        self.assertEqual(record["year_built"], 1948)
        self.assertEqual(record["sqft"], 1024)
        self.assertEqual(record["lot_sqft"], 6250)
        self.assertEqual(record["legal_description"], "CITY VIEW ADDN BLK 1/1234 LT 7")
        self.assertEqual(record["land_use_code"], "A11")

    def test_a_homestead_exemption_is_detected(self):
        record = tds.parse_cad_record(fixture("dcad_account.html"))
        self.assertIn("Residence Homestead", record["exemptions"])
        self.assertTrue(td.is_homestead(record))

    def test_tad_uses_different_wording_and_still_parses(self):
        record = tds.parse_cad_record(fixture("tad_account.html"))
        self.assertEqual(record["appraised_value"], 63000.0)
        self.assertEqual(record["sqft"], 968)
        self.assertEqual(record["subdivision"], "HYDE JACKSON")

    def test_none_is_not_an_exemption(self):
        record = tds.parse_cad_record(fixture("tad_account.html"))
        self.assertEqual(record["exemptions"], [])
        self.assertIsNone(td.is_homestead(record))

    def test_the_land_use_description_is_not_just_the_code_again(self):
        """`Land Use Code` matched both fields until each consumed its own pair."""
        record = tds.parse_cad_record(fixture("dcad_account.html"))
        self.assertEqual(record["land_use_description"], "Residential Single Family")

    def test_a_legal_description_containing_addition_is_not_the_subdivision(self):
        record = tds.parse_cad_record(fixture("tad_account.html"))
        self.assertNotEqual(record["subdivision"], "Neighborhood")


class StructureChangesFailLoudly(unittest.TestCase):
    """A county reformatting its page must be an error naming the URL."""

    def test_a_renamed_bid_column_is_not_silently_dropped(self):
        html = fixture("dallas_realauction.html").replace("Opening Bid", "Starting Amount")
        rows, diag = tds.rows_from_tables(tds.collect_tables(html),
                                          source_for("Dallas")["column_map"])
        self.assertEqual(rows, [])
        self.assertIn("minimum_opening_bid", diag["reason"])

    def test_a_page_with_no_table_at_all_is_diagnosed_as_a_javascript_page(self):
        """Three of four counties publish through a React app, and the first
        live run told the operator to edit `column_map` for all of them."""
        rows, diag = tds.rows_from_tables(tds.collect_tables("<div id=root></div>"),
                                          source_for("Dallas")["column_map"])
        self.assertEqual(rows, [])
        self.assertTrue(diag["no_tables"])

        advice = tds._unparseable(source_for("Dallas"), diag)
        self.assertIn("no HTML table at all", advice)
        self.assertIn("rendered by JavaScript", advice)
        self.assertIn("discovery of the JSON", advice)
        self.assertNotIn("Update `column_map`", advice)

    def test_tables_that_are_present_but_unmapped_still_point_at_column_map(self):
        html = fixture("dallas_realauction.html").replace("Opening Bid", "Starting Amount")
        _, diag = tds.rows_from_tables(tds.collect_tables(html),
                                       source_for("Dallas")["column_map"])
        advice = tds._unparseable(source_for("Dallas"), diag)
        self.assertIn("column_map", advice)
        self.assertNotIn("JavaScript", advice)

    def test_load_source_raises_with_the_url_when_the_markers_are_gone(self):
        source = dict(source_for("Dallas"), id="test_marker_drift",
                      required_markers=["a marker that will never be on the page"])
        calls = {}

        def fake_fetch(url, cfg, **kwargs):
            calls["url"] = url
            return "<html><body>Nothing to see.</body></html>"

        original, tds.fetch = tds.fetch, fake_fetch
        try:
            with self.assertRaises(tds.StructureChanged) as caught:
                tds.load_source(source, td.load_config())
        finally:
            tds.fetch = original
        self.assertEqual(caught.exception.url, source["url"])
        self.assertIn(source["url"], str(caught.exception))
        self.assertIn("required_markers", caught.exception.detail)

    def test_load_source_raises_when_the_columns_no_longer_map(self):
        source = dict(source_for("Dallas"), id="test_column_drift")
        html = fixture("dallas_realauction.html").replace("Opening Bid", "Starting Amount")

        original, tds.fetch = tds.fetch, lambda url, cfg, **kw: html
        try:
            with self.assertRaises(tds.StructureChanged) as caught:
                tds.load_source(source, td.load_config())
        finally:
            tds.fetch = original
        self.assertIn(source["url"], str(caught.exception))
        self.assertIn("column_map", caught.exception.detail)

    def test_a_pdf_only_source_names_the_manual_path_instead_of_pretending(self):
        source = dict(source_for("Ellis"), id="test_pdf_source", format="pdf")
        with self.assertRaises(tds.SourceError) as caught:
            tds.load_source(source, td.load_config())
        self.assertIn("data/tax_deeds/manual/test_pdf_source.csv",
                      str(caught.exception).replace("\\", "/"))


class Manners(unittest.TestCase):
    def test_no_contact_email_means_no_requests(self):
        cfg = td.load_config()
        cfg["contact_email"] = ""
        import os
        saved = os.environ.pop("TAX_DEED_CONTACT_EMAIL", None)
        try:
            with self.assertRaises(SystemExit) as caught:
                tds.user_agent(cfg)
            self.assertIn("anonymous requests", str(caught.exception))
        finally:
            if saved is not None:
                os.environ["TAX_DEED_CONTACT_EMAIL"] = saved

    def test_the_user_agent_carries_the_project_and_the_contact(self):
        cfg = td.load_config()
        cfg["contact_email"] = "someone@example.com"
        agent = tds.user_agent(cfg)
        self.assertIn("invest-trade-daily", agent)
        self.assertIn("someone@example.com", agent)
        self.assertNotIn("{contact}", agent)

    def test_the_configured_rate_limit_is_at_most_one_request_per_second(self):
        interval = float(td.load_config().get("request_interval_seconds"))
        self.assertGreaterEqual(interval, 1.0)


class ConfigurationIntegrity(unittest.TestCase):
    """The shipped config is what production reads; a typo in it is a bug."""

    def setUp(self):
        self.cfg = td.load_config()

    def test_all_four_counties_are_configured_in_report_order(self):
        self.assertEqual([c["name"] for c in td.counties(self.cfg)],
                         ["Dallas", "Tarrant", "Johnson", "Ellis"])

    def test_every_county_has_a_source_and_a_configured_appraisal_district(self):
        districts = self.cfg["appraisal_districts"]
        for county in td.counties(self.cfg):
            self.assertTrue(county["sources"], f"{county['name']} has no source")
            self.assertIn(county["cad"], districts)
            for source in county["sources"]:
                self.assertTrue(source.get("url"))
                self.assertTrue(source.get("column_map"))
                self.assertIn(source.get("sale_type"), ("auction", "struck_off"))

    def test_struck_off_lists_are_captured_separately(self):
        kinds = {s.get("sale_type") for c in td.counties(self.cfg) for s in c["sources"]}
        self.assertIn("struck_off", kinds)

    def test_no_url_is_hardcoded_in_the_screening_logic(self):
        """Every URL lives in config. The code may only name the config file."""
        for name in ("tax_deeds.py", "tax_deed_screen.py"):
            source = (REPO / "scripts" / name).read_text()
            for line in source.splitlines():
                if "http" not in line:
                    continue
                self.assertTrue(
                    "comptroller.texas.gov/forms/50-307" in line
                    or "docs.google.com/spreadsheets" in line
                    or line.lstrip().startswith(("#", '"', "'", "*"))
                    or '"""' in line,
                    f"{name} hardcodes a URL outside config: {line.strip()!r}")

    def test_every_threshold_the_gates_read_has_a_default(self):
        for name in self.cfg["thresholds"]:
            if name.startswith("_"):
                continue
            self.assertIn(name, td.DEFAULT_THRESHOLDS)

    def test_the_written_statement_block_covers_every_county(self):
        configured = self.cfg["bidder_statement"]["counties"]
        for county in td.counties(self.cfg):
            self.assertIn(county["name"], configured)
        self.assertIn("50-307", self.cfg["bidder_statement"]["form_url"])


if __name__ == "__main__":
    unittest.main()


class JsonSourceFormat(unittest.TestCase):
    """For the counties that publish through a JavaScript app.

    taxsales.lgbs.com serves three of the four counties and renders its list
    client-side, so there is no HTML table at any URL. The list is reachable
    only as the JSON the page fetches for itself — and wiring that up has to
    stay a config change, not a parser change.
    """

    PAYLOAD = json.dumps({"data": {"results": [
        {"acct": "02345678", "cause": "348-612345-21",
         "addr": {"line1": "1109 E ANNIE ST, FORT WORTH, TX 76104"},
         "minBid": "$7,800.00", "saleDate": "10/06/2026", "county": "Tarrant"},
        {"acct": "07654321", "cause": "236-598877-19",
         "addr": {"line1": "4412 AVENUE N, FORT WORTH, TX 76105"},
         "minBid": "$4,250.00", "saleDate": "10/06/2026", "county": "Tarrant"},
    ]}})

    SOURCE = {
        "id": "tarrant_json", "sale_type": "auction", "format": "json",
        "url": "https://agg.example.invalid/api/sales",
        "records_path": "data.results",
        "field_map": {"account": "acct", "cause_number": "cause",
                      "address": "addr.line1", "minimum_opening_bid": "minBid",
                      "sale_date": "saleDate"},
    }

    def test_records_are_read_through_a_dotted_path(self):
        rows, diag = tds.rows_from_json(self.PAYLOAD, self.SOURCE)
        self.assertEqual(len(rows), 2)
        self.assertEqual(diag["rows"], 2)

    def test_nested_keys_resolve(self):
        rows, _ = tds.rows_from_json(self.PAYLOAD, self.SOURCE)
        self.assertEqual(rows[0]["address"], "1109 E ANNIE ST, FORT WORTH, TX 76104")

    def test_it_normalizes_into_the_same_shape_the_gates_expect(self):
        rows, _ = tds.rows_from_json(self.PAYLOAD, self.SOURCE)
        listing = tds.normalize_listing(rows[0], "Tarrant", self.SOURCE, td.load_config())
        self.assertEqual(listing["minimum_opening_bid"], 7800.0)
        self.assertEqual(listing["sale_date"], "2026-10-06")
        self.assertEqual(listing["account"], "02345678")

    def test_a_wrong_records_path_names_what_the_payload_actually_holds(self):
        rows, diag = tds.rows_from_json(self.PAYLOAD, dict(self.SOURCE, records_path="items"))
        self.assertEqual(rows, [])
        self.assertIn("data", diag["reason"])

    def test_a_missing_field_map_prints_the_keys_to_map(self):
        source = dict(self.SOURCE)
        del source["field_map"]
        rows, diag = tds.rows_from_json(self.PAYLOAD, source)
        self.assertEqual(rows, [])
        self.assertIn("acct", diag["reason"])

    def test_html_served_where_json_was_expected_says_so(self):
        rows, diag = tds.rows_from_json("<html>login</html>", self.SOURCE)
        self.assertEqual(rows, [])
        self.assertIn("not JSON", diag["reason"])


class StatusCodesGetTheRightAdvice(unittest.TestCase):
    """Five sources failed the first live run for three unrelated reasons, and
    every one of them was reported as `update column_map`."""

    def test_a_403_is_named_as_a_refused_user_agent_not_a_format_change(self):
        detail = tds._explain_status(403, "https://example.invalid/")
        self.assertIn("refused this User-Agent", detail)
        self.assertIn("Do not spoof a browser", detail)

    def test_a_404_says_the_url_is_wrong(self):
        self.assertIn("does not exist", tds._explain_status(404, "https://example.invalid/"))

    def test_a_429_points_at_the_rate_limit_knob(self):
        self.assertIn("request_interval_seconds", tds._explain_status(429, "u"))

    def test_a_5xx_is_not_the_operators_problem(self):
        self.assertIn("Nothing to fix here", tds._explain_status(503, "u"))


class DeliberatelyUnconfiguredSources(unittest.TestCase):
    """A URL proven not to exist is nulled, not left in place to fail nightly."""

    def setUp(self):
        self.cfg = td.load_config()
        for name in ("federal_tax_lien", "hoa_assessment", "municipal_lien", "pace_lien"):
            self.cfg["lien_sources"][name]["urls"] = {}
        self.listing = {"county": "Ellis", "owner_name": "BLUE, PAT",
                        "address": "604 W MARVIN AVE, WAXAHACHIE, TX 75165"}

    def test_a_null_clerk_url_reports_unavailable_and_never_clean(self):
        for name in ("federal_tax_lien", "hoa_assessment", "municipal_lien"):
            with self.subTest(check=name):
                check = tds.clerk_check(name, self.cfg["lien_sources"][name],
                                        self.listing, self.cfg)
                self.assertEqual(check["result"], tds.td.UNAVAILABLE)

    def test_a_null_pace_url_reports_unavailable(self):
        check = tds.pace_check(self.cfg["lien_sources"]["pace_lien"], self.listing, self.cfg)
        self.assertEqual(check["result"], tds.td.UNAVAILABLE)

    def test_an_unconfigured_source_still_costs_the_property_its_tier(self):
        """Nulling a URL must not become a quiet way to stop flagging."""
        from datetime import date as _date
        checks = [tds.clerk_check(n, self.cfg["lien_sources"][n], self.listing, self.cfg)
                  for n in ("federal_tax_lien", "hoa_assessment", "municipal_lien")]
        checks.append(tds.pace_check(self.cfg["lien_sources"]["pace_lien"],
                                     self.listing, self.cfg))
        result = td.screen(
            {"county": "Ellis", "minimum_opening_bid": 5600.0, "sale_date": "2026-10-06",
             "status": "Active", "account": "170000012345"},
            {"appraised_value": 52000.0, "exemptions": []},
            checks, self.cfg, _date(2026, 9, 3))
        self.assertEqual(result["tier"], "C")
        self.assertIn("federal_tax_lien_unchecked", {f["code"] for f in result["flags"]})



class DiscoversTheListInsideAJavaScriptPage(unittest.TestCase):
    """The automated way out of the LGBS problem.

    A client-rendered page still has to get its data from somewhere, and in
    practice it ships with it — a __NEXT_DATA__ blob, a hydration assignment, a
    JSON-LD block. So instead of asking someone to open dev tools and hand-write
    a field map, find it, and map it with the `column_map` the source already
    has: `minimumBid` and "minimum bid" normalize to the same thing.
    """

    def setUp(self):
        self.source = source_for("Tarrant")
        self.html = fixture("lgbs_spa.html")

    def test_the_page_really_has_no_table_to_parse(self):
        rows, diag = tds.rows_from_tables(tds.collect_tables(self.html),
                                          self.source["column_map"])
        self.assertEqual(rows, [])
        self.assertTrue(diag["no_tables"])

    def test_the_list_is_found_anyway(self):
        rows, diag = tds.discover_json_records(self.html, self.source)
        self.assertEqual(len(rows), 3)
        self.assertIn("results", diag["discovered_path"])

    def test_the_field_map_is_inferred_from_the_existing_column_map(self):
        _, diag = tds.discover_json_records(self.html, self.source)
        mapped = diag["discovered_field_map"]
        self.assertEqual(mapped["minimum_opening_bid"], "minimumBid")
        self.assertEqual(mapped["account"], "accountNumber")
        self.assertEqual(mapped["cause_number"], "causeNumber")

    def test_a_nested_address_object_is_reachable(self):
        _, diag = tds.discover_json_records(self.html, self.source)
        self.assertEqual(diag["discovered_field_map"]["address"], "address.line1")

    def test_discovered_rows_normalize_like_any_other(self):
        rows, _ = tds.discover_json_records(self.html, self.source)
        listing = tds.normalize_listing(rows[0], "Tarrant", self.source, td.load_config())
        self.assertEqual(listing["minimum_opening_bid"], 7800.0)
        self.assertEqual(listing["sale_date"], "2026-10-06")
        self.assertEqual(listing["account"], "02345678")

    def test_navigation_and_config_blobs_are_not_mistaken_for_a_sale_list(self):
        """The page carries three JSON arrays; only one is the list."""
        _, diag = tds.discover_json_records(self.html, self.source)
        self.assertNotIn("navigation", diag["discovered_path"])

    def test_load_source_falls_through_to_discovery_without_config_changes(self):
        source = dict(self.source, id="test_spa", required_markers=[])
        original, tds.fetch = tds.fetch, lambda url, cfg, **kw: self.html
        try:
            rows, diag = tds.load_source(source, td.load_config())
        finally:
            tds.fetch = original
        self.assertEqual(len(rows), 3)
        self.assertTrue(diag["auto_discovered"])


class FallbackUrls(unittest.TestCase):
    """A county that moves its list usually still publishes it somewhere."""

    def test_the_second_location_is_tried_when_the_first_refuses(self):
        source = dict(source_for("Dallas"), id="test_fallback", required_markers=[],
                      fallback_urls=["https://backup.example.invalid/list"])
        html = fixture("dallas_realauction.html")
        seen = []

        def fake_fetch(url, cfg, **kw):
            seen.append(url)
            if url == source["url"]:
                raise tds.SourceError(url, "HTTP 403: the host refused this User-Agent")
            return html

        original, tds.fetch = tds.fetch, fake_fetch
        try:
            rows, diag = tds.load_source(source, td.load_config())
        finally:
            tds.fetch = original
        self.assertEqual(len(seen), 2)
        self.assertEqual(len(rows), 5)
        self.assertEqual(diag["via_fallback"], "https://backup.example.invalid/list")

    def test_every_location_failing_reports_all_of_them(self):
        source = dict(source_for("Dallas"), id="test_all_fail",
                      fallback_urls=["https://backup.example.invalid/list"])

        def fake_fetch(url, cfg, **kw):
            raise tds.SourceError(url, "HTTP 404: this URL does not exist")

        original, tds.fetch = tds.fetch, fake_fetch
        try:
            with self.assertRaises(tds.StructureChanged) as caught:
                tds.load_source(source, td.load_config())
        finally:
            tds.fetch = original
        self.assertIn("2 configured locations failed", caught.exception.detail)
        self.assertIn("backup.example.invalid", caught.exception.detail)


class UserAgentFallback(unittest.TestCase):
    """robots.txt is policy and is absolute; a 403 on a UA string is a filter."""

    def setUp(self):
        self.cfg = td.load_config()
        self.cfg["contact_email"] = "someone@example.com"

    def test_every_user_agent_identifies_the_project_and_a_contact(self):
        agents = tds.user_agents(self.cfg)
        self.assertGreaterEqual(len(agents), 2)
        for agent in agents:
            self.assertIn("invest-trade-daily-taxdeeds", agent)
            self.assertIn("someone@example.com", agent)
            self.assertNotIn("{contact}", agent)

    def test_the_robots_identity_is_our_own_name_not_the_fallback(self):
        """A fallback that says Mozilla must not become how we read robots."""
        self.assertTrue(tds.user_agent(self.cfg).startswith("invest-trade-daily-taxdeeds"))

    def test_still_no_contact_still_no_requests(self):
        import os
        cfg = dict(self.cfg, contact_email="")
        saved = os.environ.pop("TAX_DEED_CONTACT_EMAIL", None)
        try:
            with self.assertRaises(SystemExit):
                tds.user_agents(cfg)
        finally:
            if saved is not None:
                os.environ["TAX_DEED_CONTACT_EMAIL"] = saved



class FloodLayerSelfHeals(unittest.TestCase):
    """A wrong layer index is not something an operator can guess."""

    def setUp(self):
        self.cfg = td.load_config()
        tds._flood_layer_cache.clear()
        self._fetch_json = tds.fetch_json

    def tearDown(self):
        tds.fetch_json = self._fetch_json
        tds._flood_layer_cache.clear()

    def _serve(self, layers):
        tds.fetch_json = lambda url, cfg, **kw: {"layers": layers}

    def test_a_reindexed_service_is_followed_by_name(self):
        self._serve([{"id": 14, "name": "Political Jurisdictions"},
                     {"id": 31, "name": "Flood Hazard Zones"}])
        url, note = tds.resolve_flood_url(self.cfg["flood"], self.cfg)
        self.assertTrue(url.endswith("/31/query"))
        self.assertIn("auto-resolved", note)

    def test_a_correct_index_is_left_alone_and_says_nothing(self):
        self._serve([{"id": 28, "name": "Flood Hazard Zones"}])
        url, note = tds.resolve_flood_url(self.cfg["flood"], self.cfg)
        self.assertEqual(url, self.cfg["flood"]["url"])
        self.assertEqual(note, "")

    def test_it_is_resolved_once_per_run_not_once_per_property(self):
        calls = []

        def counting(url, cfg, **kw):
            calls.append(url)
            return {"layers": [{"id": 31, "name": "Flood Hazard Zones"}]}

        tds.fetch_json = counting
        for _ in range(5):
            tds.resolve_flood_url(self.cfg["flood"], self.cfg)
        self.assertEqual(len(calls), 1)

    def test_an_unreachable_service_falls_back_to_the_configured_url(self):
        def boom(url, cfg, **kw):
            raise tds.SourceError(url, "unreachable")

        tds.fetch_json = boom
        url, note = tds.resolve_flood_url(self.cfg["flood"], self.cfg)
        self.assertEqual(url, self.cfg["flood"]["url"])

    def test_autodetect_can_be_switched_off(self):
        self._serve([{"id": 31, "name": "Flood Hazard Zones"}])
        spec = dict(self.cfg["flood"], autodetect_layer=False)
        url, _ = tds.resolve_flood_url(spec, self.cfg)
        self.assertEqual(url, spec["url"])


class EveryCountyHasSomewhereElseToLook(unittest.TestCase):
    def test_the_sources_that_failed_live_now_carry_fallbacks(self):
        cfg = td.load_config()
        by_id = {s["id"]: s for c in td.counties(cfg) for s in c["sources"]}
        for sid in ("dallas_auction", "johnson_auction", "tarrant_auction",
                    "ellis_auction", "dallas_struck_off"):
            with self.subTest(source=sid):
                self.assertTrue(by_id[sid].get("fallback_urls"))



class FollowsThePagesOwnApiReferences(unittest.TestCase):
    """The LGBS case: no table, and no records in the HTML either.

    The page fetches its list after load, and the endpoint is not a secret — it
    is written in the page's own scripts. Reading those is the difference
    between "go find it in dev tools" and the tool finding it, which is the
    whole point.
    """

    API = json.dumps({"count": 2, "results": [
        {"causeNumber": "348-612345-21", "accountNumber": "02345678",
         "minimumBid": "$7,800.00", "saleDate": "10/06/2026", "county": "Tarrant",
         "address": {"line1": "1109 E ANNIE ST"},
         "legalDescription": "HYDE JACKSON BLOCK 7 LOT 15", "style": "TARRANT VS WHITE"},
        {"causeNumber": "236-598877-19", "accountNumber": "07654321",
         "minimumBid": "$4,250.00", "saleDate": "10/06/2026", "county": "Tarrant",
         "address": {"line1": "4412 AVENUE N"},
         "legalDescription": "POLYTECHNIC HEIGHTS BLOCK 22 LOT 3", "style": "TARRANT VS GREY"}]})

    def setUp(self):
        self.cfg = td.load_config()
        self.source = dict(source_for("Tarrant"), id="probe_test", required_markers=[])
        self.shell = fixture("lgbs_api_shell.html")
        self.bundle = fixture("lgbs_bundle.js")
        self.served = []
        self._fetch = tds.fetch
        tds.fetch = self._fake

    def tearDown(self):
        tds.fetch = self._fetch

    def _fake(self, url, cfg, **kw):
        self.served.append(url)
        if url.endswith("main.4f2a1c.js"):
            return self.bundle
        if "/api/property_sales/" in url and "detail" not in url:
            return self.API
        if url.rstrip("/") == self.source["url"].rstrip("/"):
            return self.shell
        raise tds.SourceError(url, "HTTP 404: this URL does not exist")

    def test_the_list_is_found_without_any_config_change(self):
        rows, diag = tds.load_source(self.source, self.cfg)
        self.assertEqual(len(rows), 2)
        self.assertTrue(diag["auto_discovered"])
        self.assertEqual(diag["api_endpoint"],
                         "https://taxsales.lgbs.com/api/property_sales/")

    def test_a_reference_only_present_in_a_js_bundle_is_followed(self):
        tds.load_source(self.source, self.cfg)
        self.assertIn("https://taxsales.lgbs.com/static/js/main.4f2a1c.js", self.served)

    def test_the_likeliest_endpoint_is_probed_first(self):
        """A bare /api/ used to be tried ahead of /api/property_sales/."""
        tds.load_source(self.source, self.cfg)
        probes = [u for u in self.served if "/api/" in u]
        self.assertTrue(probes[0].endswith("/api/property_sales/"), probes)

    def test_discovered_rows_normalize_like_any_other(self):
        rows, _ = tds.load_source(self.source, self.cfg)
        listing = tds.normalize_listing(rows[0], "Tarrant", self.source, self.cfg)
        self.assertEqual(listing["minimum_opening_bid"], 7800.0)
        self.assertEqual(listing["sale_date"], "2026-10-06")

    def test_only_same_host_urls_are_probed(self):
        """A third-party analytics script is referenced and must be left alone."""
        tds.load_source(self.source, self.cfg)
        self.assertFalse([u for u in self.served if "othersite.example" in u])

    def test_assets_are_never_probed(self):
        tds.load_source(self.source, self.cfg)
        self.assertFalse([u for u in self.served if u.endswith((".png", ".svg"))])

    def test_the_probe_budget_is_bounded(self):
        self.assertLessEqual(tds.MAX_API_PROBES, 8)
        self.assertLessEqual(tds.MAX_BUNDLES, 3)

    def test_probing_can_be_switched_off_per_source(self):
        source = dict(self.source, probe_api=False)
        with self.assertRaises(tds.StructureChanged):
            tds.load_source(source, self.cfg)
        self.assertFalse([u for u in self.served if "/api/" in u])


class RobotsUnreachableIsNotAProhibition(unittest.TestCase):
    """A connection reset states no policy; an HTTP 5xx does."""

    def setUp(self):
        tds._robots.clear()
        self._session = tds.session
        self.cfg = td.load_config()
        self.cfg["contact_email"] = "someone@example.com"

    def tearDown(self):
        tds.session = self._session
        tds._robots.clear()

    def _serve(self, behaviour):
        class FakeSession:
            def get(self, url, **kw):
                return behaviour(url)
        tds.session = lambda cfg: FakeSession()

    def test_a_connection_reset_allows_after_a_retry(self):
        """hazards.fema.gov reset on robots.txt and was banned for it."""
        calls = []

        def reset(url):
            calls.append(url)
            raise ConnectionError("Connection aborted. ConnectionResetError(104)")

        self._serve(reset)
        allowed, why = tds.robots_allows("https://hazards.fema.gov/x/query", self.cfg)
        self.assertTrue(allowed)
        self.assertIn("states no policy", why)
        self.assertEqual(len(calls), 2, "it must retry once before deciding")

    def test_a_server_error_still_refuses(self):
        class Resp:
            status_code, text = 503, ""
        self._serve(lambda url: Resp())
        allowed, why = tds.robots_allows("https://example.invalid/x", self.cfg)
        self.assertFalse(allowed)
        self.assertIn("not fetching", why)

    def test_a_404_means_no_rules_which_is_permission(self):
        class Resp:
            status_code, text = 404, ""
        self._serve(lambda url: Resp())
        allowed, _ = tds.robots_allows("https://example.invalid/x", self.cfg)
        self.assertTrue(allowed)

    def test_a_real_disallow_is_still_obeyed(self):
        class Resp:
            status_code = 200
            text = "User-agent: *\nDisallow: /"
        self._serve(lambda url: Resp())
        allowed, why = tds.robots_allows("https://example.invalid/x", self.cfg)
        self.assertFalse(allowed)
        self.assertIn("disallows", why)



class PagingAndFilteringAreVisible(unittest.TestCase):
    """Three sources fetched 10 rows each and kept none, and said nothing.

    Two bugs behind one silence: the aggregator names the county in a field
    nothing mapped, so filtering on the mapped values dropped every row; and 10
    was the API's page size rather than the month's docket.
    """

    FIELDS = {"cause_nbr": "C-{a}", "account_nbr": "{a}", "prop_address_one": "{a} MAIN ST",
              "minimum_bid": "$7,800.00", "status": "Active", "precinct": "1"}

    def _record(self, county, account, sale_date="2026-10-06"):
        record = {k: v.format(a=account) for k, v in self.FIELDS.items()}
        record.update(county=county, sale_date=sale_date)
        return record

    def setUp(self):
        self.cfg = td.load_config()
        self.county = next(c for c in td.counties(self.cfg) if c["name"] == "Tarrant")
        self.county["sources"][0] = dict(self.county["sources"][0], required_markers=[])
        self.pages = {
            1: {"count": 5, "next": "/api/property_sales/?page=2",
                "results": [self._record("Tarrant", "111"), self._record("Dallas", "222")]},
            2: {"count": 5, "next": "/api/property_sales/?page=3",
                "results": [self._record("Tarrant", "333"), self._record("Ellis", "444")]},
            3: {"count": 5, "next": None,
                "results": [self._record("Tarrant", "555", "2026-11-03")]},
        }
        self.shell = ('<html><body><div id=root></div>'
                      '<script>var A="/api/property_sales/";</script></body></html>')
        self._fetch = tds.fetch
        tds.fetch = self._fake

    def tearDown(self):
        tds.fetch = self._fetch

    def _fake(self, url, cfg, **kw):
        if "/api/property_sales/" in url:
            found = re.search(r"page=(\d+)", url)
            return json.dumps(self.pages[int(found.group(1)) if found else 1])
        return self.shell

    def test_every_page_is_followed_not_just_the_first(self):
        listings, report = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertIn("3 page(s)", report[0]["detail"])

    def test_the_county_filter_reads_a_field_nothing_mapped(self):
        listings, report = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertEqual([l["account"] for l in listings], ["111", "333"])
        self.assertEqual(report[0]["dropped_county"], 2)

    def test_rows_for_another_sale_date_are_dropped_and_counted(self):
        _, report = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertEqual(report[0]["dropped_date"], 1)
        self.assertIn("2026-11-03", report[0]["sale_dates_seen"])

    def test_the_report_says_where_every_row_went(self):
        """`fetched 10, kept 0` read exactly like a source returning nothing."""
        _, report = tds.county_listings(self.county, self.cfg, "2026-10-06")
        detail = report[0]["detail"]
        self.assertIn("fetched 5, kept 2", detail)
        self.assertIn("not in Tarrant", detail)
        self.assertIn("another sale date", detail)

    def test_paging_is_bounded(self):
        self.assertLessEqual(tds.MAX_PAGES, 40)
        self.assertLessEqual(tds.MAX_ROWS, 5000)

    def test_a_next_that_loops_back_terminates(self):
        self.pages[3]["next"] = "/api/property_sales/?page=1"
        listings, report = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertEqual(len(listings), 2)



class AsksTheApiToFilterRatherThanPagingTheState(unittest.TestCase):
    """These endpoints serve every county their firm covers.

    The first live success walked 40 pages, fetched 400 rows and kept none of
    them — paging a statewide feed at one request per second is not a plan. So
    ask the API to narrow, using the field name the API itself uses as the key.
    """

    def _rec(self, i, county):
        return {"cause_nbr": f"C{i}", "account_nbr": str(i), "prop_address_one": f"{i} MAIN",
                "minimum_bid": "$7,800.00", "sale_date": "2026-10-06",
                "status": "Active", "county": county}

    def setUp(self):
        self.cfg = td.load_config()
        self.county = next(c for c in td.counties(self.cfg) if c["name"] == "Tarrant")
        self.county["sources"][0] = dict(self.county["sources"][0], required_markers=[])
        self.statewide = [self._rec(i, "Anderson") for i in range(10)]
        self.ours = [self._rec(100 + i, "Tarrant") for i in range(3)]
        self.honoured = "county"
        self.served = []
        self._fetch = tds.fetch
        tds.fetch = self._fake

    def tearDown(self):
        tds.fetch = self._fetch

    def _fake(self, url, cfg, **kw):
        self.served.append(url)
        if "/api/property_sales/" in url:
            found = re.search(r"[?&](county|county_name|county__name|search|q)=([A-Za-z]+)", url)
            if found and found.group(1) == self.honoured and found.group(2) == "Tarrant":
                return json.dumps({"count": 3, "next": None, "results": self.ours})
            # An API that does not know a query key ignores it and returns
            # everything — which must not read as a successful narrowing.
            return json.dumps({"count": 10, "next": None, "results": self.statewide})
        return '<html><script>var A="/api/property_sales/";</script></html>'

    def test_it_re_requests_narrowed_and_keeps_the_result(self):
        listings, report = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertEqual([l["account"] for l in listings], ["100", "101", "102"])
        self.assertIn("fetched 3, kept 3", report[0]["detail"])

    def test_a_parameter_the_api_ignores_is_not_taken_for_success(self):
        self.honoured = "nothing-matches-this"
        listings, report = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertEqual(listings, [])
        self.assertIn("not in Tarrant", report[0]["detail"])

    def test_an_already_county_scoped_endpoint_is_left_alone(self):
        self.statewide = self.ours
        tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertFalse([u for u in self.served if "county=" in u],
                         "no narrowing should be attempted when page one is already ours")

    def test_a_pinned_query_param_skips_the_probing(self):
        self.county["sources"][0] = dict(self.county["sources"][0],
                                         query_params={"county": "Tarrant"})
        listings, _ = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertEqual(len(listings), 3)
        probes = [u for u in self.served if "=" in u.split("/api/")[-1]]
        self.assertEqual(len(probes), 1, probes)

    def test_the_report_names_the_counties_that_did_come_back(self):
        """`400 not in Tarrant` cannot tell a statewide feed from a numeric id."""
        self.honoured = "nothing-matches-this"
        _, report = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertIn("Anderson", report[0]["detail"])

    def test_a_county_field_holding_an_id_still_matches_on_the_rest_of_the_record(self):
        self.honoured = "nothing-matches-this"
        self.statewide = [dict(self._rec(1, "057"), prop_address_one="1 MAIN ST, TARRANT")]
        listings, _ = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertEqual(len(listings), 1)



class LearnsHowTheApiSpellsACountyName(unittest.TestCase):
    """The live feed is nationwide and stores `GALVESTON COUNTY`.

    Querying it for `Tarrant` finds nothing, and hardcoding "uppercase plus
    COUNTY" would be a guess about one vendor. The records themselves say what
    shape the data is in, and that is the shape the filter wants.
    """

    def test_it_copies_the_case_and_suffix_it_was_shown(self):
        self.assertEqual(
            tds.county_value_variants("Tarrant", ["GALVESTON COUNTY", "MAVERICK COUNTY"])[0],
            "TARRANT COUNTY")

    def test_title_case_is_followed_too(self):
        self.assertEqual(tds.county_value_variants("Tarrant", ["Galveston County"])[0],
                         "Tarrant County")

    def test_a_bare_name_stays_bare(self):
        self.assertEqual(tds.county_value_variants("Tarrant", ["Galveston"])[0], "Tarrant")

    def test_the_usual_shapes_are_still_tried_when_nothing_was_observed(self):
        variants = tds.county_value_variants("Tarrant", [])
        self.assertIn("Tarrant", variants)
        self.assertIn("TARRANT COUNTY", variants)

    def test_probing_is_bounded(self):
        self.assertLessEqual(tds.MAX_NARROW_PROBES, 10)


class NationwideFeedIsNarrowedByTheLearnedValue(unittest.TestCase):
    def _rec(self, i, county):
        return {"cause_nbr": f"C{i}", "account_nbr": str(i), "prop_address_one": f"{i} MAIN",
                "minimum_bid": "$7,800.00", "sale_date": "2026-10-06",
                "status": "Active", "county": county}

    def setUp(self):
        self.cfg = td.load_config()
        self.county = next(c for c in td.counties(self.cfg) if c["name"] == "Tarrant")
        self.county["sources"][0] = dict(self.county["sources"][0], required_markers=[])
        self.elsewhere = [self._rec(i, "GALVESTON COUNTY") for i in range(10)]
        self.ours = [self._rec(100 + i, "TARRANT COUNTY") for i in range(3)]
        self.served = []
        self._fetch = tds.fetch
        tds.fetch = self._fake

    def tearDown(self):
        tds.fetch = self._fetch

    def _fake(self, url, cfg, **kw):
        self.served.append(url)
        if "/api/property_sales/" in url:
            # Only the value the data is actually stored in matches.
            if "county=TARRANT+COUNTY" in url or "county=TARRANT%20COUNTY" in url:
                return json.dumps({"count": 3, "next": None, "results": self.ours})
            return json.dumps({"count": 10, "next": None, "results": self.elsewhere})
        return '<html><script>var A="/api/property_sales/";</script></html>'

    def test_the_learned_spelling_is_what_finds_the_rows(self):
        listings, report = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertEqual([l["account"] for l in listings], ["100", "101", "102"])

    def test_it_is_the_first_thing_tried(self):
        tds.county_listings(self.county, self.cfg, "2026-10-06")
        narrowed = [u for u in self.served if "county=" in u]
        self.assertTrue(narrowed[0].endswith("county=TARRANT+COUNTY"), narrowed[:3])

    def test_a_failure_to_narrow_says_what_it_tried_and_what_to_pin(self):
        self.ours = []
        _, report = tds.county_listings(self.county, self.cfg, "2026-10-06")
        detail = report[0]["detail"]
        self.assertIn("could not narrow server-side", detail)
        self.assertIn("query_params", detail)
        self.assertIn("GALVESTON COUNTY", detail)



class FoundRowsAreNotTheSameThingAsOurRows(unittest.TestCase):
    """The bug that survived four rounds of fixes.

    The vendor page embeds the first chunk of a *nationwide* feed. Embedded
    discovery therefore succeeded with 400 records, none of them this county's —
    and because it succeeded, the API route never ran, and with it neither did
    the server-side narrowing that is the only way to reach the rest of the
    feed. "Found, but none ours" has to fall through exactly like "found
    nothing".
    """

    def _rec(self, i, county):
        return {"cause_nbr": f"C{i}", "account_nbr": str(i), "prop_address_one": f"{i} MAIN",
                "minimum_bid": "$7,800.00", "sale_date": "2026-10-06",
                "status": "Active", "county": county}

    def setUp(self):
        self.cfg = td.load_config()
        self.county = next(c for c in td.counties(self.cfg) if c["name"] == "Tarrant")
        self.county["sources"][0] = dict(self.county["sources"][0], required_markers=[])
        self.embedded = [self._rec(i, "GALVESTON COUNTY") for i in range(10)]
        self.ours = [self._rec(100 + i, "TARRANT COUNTY") for i in range(3)]
        self.served = []
        self._fetch = tds.fetch
        tds.fetch = self._fake

    def tearDown(self):
        tds.fetch = self._fetch

    def _page(self):
        return ('<html><body><div id=root></div>'
                '<script id="__NEXT_DATA__" type="application/json">'
                + json.dumps({"count": 9999, "next": None, "results": self.embedded})
                + '</script><script>var A="/api/property_sales/";</script></body></html>')

    def _fake(self, url, cfg, **kw):
        self.served.append(url)
        if "/api/property_sales/" in url:
            if "county=TARRANT+COUNTY" in url or "county=TARRANT%20COUNTY" in url:
                return json.dumps({"count": 3, "next": None, "results": self.ours})
            return json.dumps({"count": 9999, "next": None, "results": self.embedded})
        return self._page()

    def test_embedded_rows_that_are_not_ours_do_not_end_the_search(self):
        listings, _ = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertEqual([l["account"] for l in listings], ["100", "101", "102"])

    def test_the_api_route_runs_and_narrows(self):
        tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertTrue([u for u in self.served if "county=TARRANT" in u.replace("%20", "+")])

    def test_embedded_rows_that_are_ours_are_kept_without_touching_the_api(self):
        self.embedded = self.ours
        listings, _ = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertEqual(len(listings), 3)
        self.assertFalse([u for u in self.served if "/api/" in u],
                         "no API probing when the page already gave us our rows")

    def test_a_source_with_no_county_filter_keeps_whatever_it_finds(self):
        source = dict(self.county["sources"][0])
        source.pop("county_filter", None)
        self.county["sources"][0] = source
        listings, _ = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertEqual(len(listings), 10)
        self.assertFalse([u for u in self.served if "/api/" in u])

    def test_the_embedded_rows_are_kept_when_the_api_finds_nothing_better(self):
        """Falling through must not lose what discovery already had."""
        self.ours = []
        source = dict(self.county["sources"][0])
        source.pop("county_filter", None)
        self.county["sources"][0] = source
        listings, _ = tds.county_listings(self.county, self.cfg, "2026-10-06")
        self.assertEqual(len(listings), 10)

    def test_matches_county_is_honest_about_an_empty_batch(self):
        self.assertFalse(tds._matches_county([], {"county_filter": "Tarrant"}))
        self.assertFalse(tds._matches_county([], {}))



class AppraisalDistrictLookupsTryHarderAndSayWhy(unittest.TestCase):
    """664 identical `no_cad_match` rejections hid two different problems.

    Dallas matched 94 accounts and then stopped — throttling. Tarrant and Ellis
    matched none at all — the URL pattern is wrong. One silent `None` for both.
    """

    def setUp(self):
        self.cfg = td.load_config()
        tds.cad_failures.clear()
        self._fetch = tds.fetch
        self.served = []

    def tearDown(self):
        tds.fetch = self._fetch
        tds.cad_failures.clear()

    def test_account_spellings_are_tried(self):
        """A constable list writes 126-0002-0009; the roll writes 12600020009."""
        self.assertIn("12600020009", tds.account_variants("126-0002-0009"))
        self.assertIn("139750000000", tds.account_variants("00000139750000000"))

    def test_a_second_url_pattern_is_tried_when_the_first_misses(self):
        good = fixture("tad_account.html")

        def fake(url, cfg, **kw):
            self.served.append(url)
            if "property-detail" in url:
                return good
            return "<html><body>Tarrant Appraisal District — account not found</body></html>"

        tds.fetch = fake
        record = tds.cad_record("TAD", "02345678", self.cfg, use_cache=False)
        self.assertIsNotNone(record)
        self.assertEqual(record["appraised_value"], 63000.0)
        self.assertIn("property-detail", record["cad_url"])

    def test_a_page_that_renders_but_carries_no_value_is_a_miss_not_a_match(self):
        tds.fetch = lambda url, cfg, **kw: (
            "<html><body>Tarrant Appraisal District</body></html>")
        self.assertIsNone(tds.cad_record("TAD", "02345678", self.cfg, use_cache=False))
        reasons = tds.cad_failures.get("TAD", {})
        self.assertTrue(any("no appraised value" in r for r in reasons))

    def test_a_refusing_district_is_not_hammered_with_more_spellings(self):
        """Trying more account numbers at a host already saying no is just more
        requests at a host already saying no."""
        def refuse(url, cfg, **kw):
            self.served.append(url)
            raise tds.SourceError(url, "HTTP 403: the host refused this User-Agent")

        tds.fetch = refuse
        self.assertIsNone(tds.cad_record("DCAD", "00000139750000000", self.cfg,
                                         use_cache=False))
        self.assertLessEqual(len(self.served), len(tds.account_variants("00000139750000000")))

    def test_the_reason_is_recorded_per_district(self):
        tds.fetch = lambda url, cfg, **kw: (_ for _ in ()).throw(
            tds.SourceError(url, "HTTP 429: rate limited"))
        tds.cad_record("DCAD", "1", self.cfg, use_cache=False)
        tds.cad_record("TAD", "2", self.cfg, use_cache=False)
        self.assertIn("DCAD", tds.cad_failures)
        self.assertIn("TAD", tds.cad_failures)

    def test_every_district_has_a_fallback_pattern_configured(self):
        for key, district in self.cfg["appraisal_districts"].items():
            with self.subTest(district=key):
                self.assertTrue(district.get("account_url"))



class BacksOffWhenAHostSaysTooFast(unittest.TestCase):
    """Tarrant CAD answered 429 to 365 straight lookups at one per second.

    The right response to "too fast" is to slow down for that host, not to keep
    the same pace and record 365 identical failures.
    """

    class Resp:
        def __init__(self, code, text=""):
            self.status_code, self.text = code, text

    def setUp(self):
        self.cfg = td.load_config()
        self.cfg["contact_email"] = "someone@example.com"
        self.cfg["request_interval_seconds"] = 0  # keep the test instant
        tds._robots.clear()
        tds._host_interval.clear()
        self._session, self._sleep = tds.session, tds.time.sleep
        tds.time.sleep = lambda *_: None
        tds._robots["https://slow.example.invalid"] = tds.ALLOW_UNKNOWN

    def tearDown(self):
        tds.session, tds.time.sleep = self._session, self._sleep
        tds._robots.clear()
        tds._host_interval.clear()

    def _serve(self, codes):
        self.calls = []
        queue = list(codes)

        class FakeSession:
            def get(inner, url, **kw):
                self.calls.append(url)
                return BacksOffWhenAHostSaysTooFast.Resp(
                    queue.pop(0) if queue else 200, "ok")

        tds.session = lambda cfg: FakeSession()

    def test_a_429_is_retried_after_slowing_down(self):
        self._serve([429, 200])
        self.assertEqual(tds.fetch("https://slow.example.invalid/x", self.cfg), "ok")
        self.assertEqual(len(self.calls), 2)
        self.assertGreater(tds._host_interval["slow.example.invalid"], 0)

    def test_the_slower_interval_persists_for_the_rest_of_the_run(self):
        self._serve([429, 429, 200])
        tds.fetch("https://slow.example.invalid/x", self.cfg)
        first = tds._host_interval["slow.example.invalid"]
        self.assertGreaterEqual(first, 2)

    def test_it_gives_up_rather_than_retrying_forever(self):
        self._serve([429] * 20)
        with self.assertRaises(tds.SourceError) as caught:
            tds.fetch("https://slow.example.invalid/x", self.cfg)
        self.assertLessEqual(len(self.calls), tds.RATE_LIMIT_RETRIES + 2)
        self.assertIn("host_interval_seconds", caught.exception.detail)

    def test_the_backoff_is_bounded(self):
        self.assertLessEqual(tds.MAX_HOST_INTERVAL, 8.0)

    def test_a_host_can_be_pinned_slower_in_config(self):
        self.assertIn("www.tad.org", td.load_config()["host_interval_seconds"])

    def test_a_403_still_walks_the_user_agents_and_then_stops(self):
        self._serve([403, 403])
        with self.assertRaises(tds.SourceError) as caught:
            tds.fetch("https://slow.example.invalid/x", self.cfg)
        self.assertEqual(len(self.calls), len(tds.user_agents(self.cfg)))
        self.assertIn("User-Agents were refused", caught.exception.detail)



class GivesUpOnADistrictThatNeverAnswers(unittest.TestCase):
    """Nine search probes per property against a district that cannot be
    searched is nearly two hours for one county, against a 45-minute job."""

    def setUp(self):
        self.cfg = td.load_config()
        tds.cad_failures.clear()
        tds.cad_abandoned.clear()
        tds._cad_misses.clear()
        tds._cad_search_param.clear()
        self._fetch = tds.fetch
        self.calls = []

    def tearDown(self):
        tds.fetch = self._fetch
        tds.cad_failures.clear()
        tds.cad_abandoned.clear()
        tds._cad_misses.clear()

    def _always_fail(self, url, cfg, **kw):
        self.calls.append(url)
        raise tds.SourceError(url, "HTTP 404: this URL does not exist")

    def test_it_stops_after_a_bounded_number_of_consecutive_misses(self):
        tds.fetch = self._always_fail
        for i in range(40):
            tds.cad_record("TAD", f"{i:08d}", self.cfg, use_cache=False)
        self.assertIn("TAD", tds.cad_abandoned)
        self.assertLess(len(self.calls), 40, "it kept asking a district that never answers")

    def test_giving_up_is_reported_with_the_reason(self):
        tds.fetch = self._always_fail
        for i in range(20):
            tds.cad_record("TAD", f"{i:08d}", self.cfg, use_cache=False)
        self.assertIn("gave up after", tds.cad_abandoned["TAD"])
        self.assertIn("404", tds.cad_abandoned["TAD"])

    def test_one_district_giving_up_does_not_stop_another(self):
        tds.fetch = self._always_fail
        for i in range(20):
            tds.cad_record("TAD", f"{i:08d}", self.cfg, use_cache=False)
        self.assertNotIn("DCAD", tds.cad_abandoned)
        self.assertIsNone(tds.cad_record("DCAD", "1", self.cfg, use_cache=False))

    def test_a_success_resets_the_counter(self):
        good = fixture("tad_account.html")
        state = {"n": 0}

        def sometimes(url, cfg, **kw):
            state["n"] += 1
            if state["n"] % 3 == 0:
                return good
            raise tds.SourceError(url, "HTTP 404: this URL does not exist")

        tds.fetch = sometimes
        for i in range(30):
            tds.cad_record("TAD", f"{i:08d}", self.cfg, use_cache=False)
        self.assertNotIn("TAD", tds.cad_abandoned,
                         "a district that answers sometimes must not be abandoned")

    def test_the_bound_is_small_enough_to_matter(self):
        self.assertLessEqual(tds.CAD_GIVE_UP_AFTER, 20)



class MapsThePlainValueFieldTheFeedActuallyPublishes(unittest.TestCase):
    """The unmapped-key diagnostic earned its place on its first live run.

    The feed carries a field called exactly `value`, and every value pattern
    required the word adjudged, appraised or assessed — so 363 listings went
    unpriced next to a number the county had published for each of them.
    """

    def setUp(self):
        self.cfg = td.load_config()
        self.source = source_for("Tarrant")
        # The real key list, from the live run's unmapped-fields report.
        self.keys = ["cause_nbr", "account_nbr", "prop_address_one", "minimum_bid",
                     "sale_date", "status", "county", "precinct", "value", "sale_nbr",
                     "uid", "prop_city", "prop_zipcode", "google_view", "has_photo"]

    def test_the_bare_value_field_is_mapped(self):
        mapped = tds.infer_field_map(self.keys, self.source["column_map"])
        self.assertEqual(mapped.get("adjudged_value"), "value")

    def test_it_does_not_steal_the_minimum_bid(self):
        mapped = tds.infer_field_map(self.keys, self.source["column_map"])
        self.assertEqual(mapped.get("minimum_opening_bid"), "minimum_bid")

    def test_a_more_specific_name_still_wins(self):
        mapped = tds.infer_field_map(["adjudged_value", "value", "minimum_bid", "account_nbr"],
                                     self.source["column_map"])
        self.assertEqual(mapped.get("adjudged_value"), "adjudged_value")

    def test_a_listing_carrying_it_is_priced_without_any_cad(self):
        from datetime import date as _date
        row = {"account_nbr": "02345678", "cause_nbr": "C-1", "minimum_bid": "$7,800.00",
               "value": "$63,000.00", "sale_date": "2026-10-06", "status": "Active",
               "county": "TARRANT COUNTY", "prop_address_one": "1109 E ANNIE ST"}
        mapped = tds.infer_field_map(list(row), self.source["column_map"])
        listing = tds.normalize_listing({f: row[k] for f, k in mapped.items()},
                                        "Tarrant", self.source, self.cfg)
        self.assertEqual(listing["adjudged_value"], 63000.0)
        result = td.screen(listing, None, [], self.cfg, _date(2026, 9, 4))
        self.assertEqual(result["economics"]["value_source"], "adjudged")
        self.assertAlmostEqual(result["economics"]["bid_to_value"], 7800 / 63000, places=4)



class MarkersAndFiltersBelongToAUrlNotASource(unittest.TestCase):
    """The bug that cost Johnson County every single run.

    Its fallback is the same nationwide feed that already works for three other
    counties, and it was rejected for not containing the word "constable" — a
    marker written for the county's own page — then would have returned the
    whole country for want of a filter.
    """

    def setUp(self):
        self.cfg = td.load_config()
        self.served = []
        self._fetch = tds.fetch

    def tearDown(self):
        tds.fetch = self._fetch

    def _source(self, **over):
        base = {"id": "t", "sale_type": "auction", "format": "html_table",
                "url": "https://county.example.invalid/constable-sale",
                "required_markers": ["constable"],
                "column_map": source_for("Tarrant")["column_map"]}
        base.update(over)
        return base

    def test_a_string_fallback_inherits_no_markers(self):
        html = fixture("dallas_realauction.html")   # contains no "constable"

        def fake(url, cfg, **kw):
            self.served.append(url)
            if "county.example" in url:
                raise tds.SourceError(url, "HTTP 403: the host refused this User-Agent")
            return html

        tds.fetch = fake
        rows, diag = tds.load_source(
            self._source(fallback_urls=["https://aggregate.example.invalid/"]), self.cfg)
        self.assertEqual(len(rows), 5)
        self.assertEqual(diag["via_fallback"], "https://aggregate.example.invalid/")

    def test_an_object_fallback_carries_its_own_filter(self):
        html = fixture("tarrant_lgbs.html")         # Tarrant, Dallas and Ellis rows

        def fake(url, cfg, **kw):
            if "county.example" in url:
                raise tds.SourceError(url, "HTTP 403: the host refused this User-Agent")
            return html

        tds.fetch = fake
        county = {"name": "Johnson", "cad": "JohnsonCAD", "sources": [self._source(
            fallback_urls=[{"url": "https://aggregate.example.invalid/",
                            "required_markers": [], "county_filter": "Ellis"}])]}
        listings, report = tds.county_listings(county, self.cfg)
        # The filter came from the URL that answered, not from the source.
        self.assertEqual(len(listings), 1)
        self.assertIn("WAXAHACHIE", listings[0]["address"])

    def test_the_primary_url_still_gets_its_own_markers(self):
        tds.fetch = lambda url, cfg, **kw: "<html>nothing here</html>"
        with self.assertRaises(tds.StructureChanged) as caught:
            tds.load_source(self._source(fallback_urls=[]), self.cfg)
        self.assertIn("constable", caught.exception.detail)

    def test_johnson_now_reaches_the_aggregate_that_works_for_everyone_else(self):
        source = next(s for c in td.counties(self.cfg) if c["name"] == "Johnson"
                      for s in c["sources"])
        lgbs = [f for f in source["fallback_urls"] if isinstance(f, dict)]
        self.assertTrue(lgbs, "Johnson needs an object fallback for the aggregate")
        self.assertEqual(lgbs[0]["county_filter"], "Johnson")
        self.assertEqual(lgbs[0]["required_markers"], [])


class ClerkRecordsMayLiveOnMoreThanOneHost(unittest.TestCase):
    """A robots disallow is that host's policy and ends the matter there.

    It is not the county's policy, though, and counties publish the same
    official records index on more than one system — so a second host is a
    different source, not a way around the first one's rules.
    """

    def setUp(self):
        self.cfg = td.load_config()
        self.listing = {"county": "Dallas", "owner_name": "SMITH, JOHN",
                        "address": "1417 S HARWOOD ST"}
        self._fetch = tds.fetch

    def tearDown(self):
        tds.fetch = self._fetch

    def test_every_county_has_more_than_one_candidate_host(self):
        spec = self.cfg["lien_sources"]["federal_tax_lien"]
        for county in ("Dallas", "Tarrant", "Johnson", "Ellis"):
            with self.subTest(county=county):
                self.assertGreaterEqual(len(tds.clerk_candidates(spec, county)), 2)

    def test_a_disallowed_host_is_skipped_and_the_next_is_tried(self):
        spec = dict(self.cfg["lien_sources"]["federal_tax_lien"],
                    query_url="{base}/search?q={query}", query_terms=["FEDERAL TAX LIEN"])
        seen = []

        def fake(url, cfg, **kw):
            seen.append(url)
            if "publicsearch.us" in url:
                raise tds.RobotsDisallowed(url, "robots.txt disallows this path")
            return "<html>no results</html>"

        tds.fetch = fake
        check = tds.clerk_check("federal_tax_lien", spec, self.listing, self.cfg)
        self.assertEqual(check["result"], tds.td.CLEAN)
        self.assertNotIn("publicsearch.us", check["source"])
        self.assertGreaterEqual(len(seen), 2)

    def test_every_host_refusing_is_unavailable_and_never_clean(self):
        spec = dict(self.cfg["lien_sources"]["federal_tax_lien"],
                    query_url="{base}/search?q={query}")

        def refuse(url, cfg, **kw):
            raise tds.RobotsDisallowed(url, "robots.txt disallows this path")

        tds.fetch = refuse
        check = tds.clerk_check("federal_tax_lien", spec, self.listing, self.cfg)
        self.assertEqual(check["result"], tds.td.UNAVAILABLE)
        self.assertIn("robots.txt", check["detail"])

    def test_without_a_query_url_it_is_still_unavailable(self):
        check = tds.clerk_check("federal_tax_lien",
                                self.cfg["lien_sources"]["federal_tax_lien"],
                                self.listing, self.cfg)
        self.assertEqual(check["result"], tds.td.UNAVAILABLE)
        self.assertIn("query_url", check["detail"])


class PacketsAreWrittenForEveryCandidateByDefault(unittest.TestCase):
    def test_the_default_covers_tier_c(self):
        self.assertEqual(td.packet_tiers(td.load_config()), {"A", "B", "C"})

