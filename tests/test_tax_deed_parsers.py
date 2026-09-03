"""Parsers for the four county list formats, against archived-shape fixtures.

See `tests/fixtures/tax_deeds/README.md` for what these fixtures are and — more
importantly — what they are not. They pin the parsers against the shapes the
counties publish. They cannot tell you the live page still looks like this;
`scripts/tax_deed_sources.py verify` is what does that, and the tests at the
bottom cover it failing loudly rather than quietly returning nothing.
"""

from __future__ import annotations

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

    def test_a_page_with_no_table_at_all_reports_why(self):
        rows, diag = tds.rows_from_tables(tds.collect_tables("<p>Sale postponed.</p>"),
                                          source_for("Dallas")["column_map"])
        self.assertEqual(rows, [])
        self.assertIn("no table", diag["reason"])

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
