"""The probe's job is to tell three failures apart. So test that it does.

The run summary already reports *which exit* `cad_record` took. What it cannot
say is why, and "page rendered but carried no appraised value" is true of a
JavaScript shell, of a page whose labels are worded differently, and of a page
saying the account does not exist. Those have three unrelated fixes, and a
probe that confuses them is worse than no probe — it would send someone to edit
`field_map` for a page that has no labels at all.

No network here. Every test feeds HTML straight to the classifier.
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import tax_deeds as td  # noqa: E402
import tax_deed_sources as src  # noqa: E402
import tax_deed_cad_probe as probe  # noqa: E402


DISTRICT = {"name": "Test CAD", "required_markers": ["testcad"],
            "account_url": "https://cad.example/acct/{account}",
            "search_url": "https://cad.example/search"}


def page(body: str, marker: str = "TestCAD") -> str:
    return f"<html><body><h1>{marker}</h1>{body}</body></html>"


class Fetches:
    """Stands in for `src.fetch`, keyed by URL."""

    def __init__(self, pages: dict, errors: dict | None = None):
        self.pages, self.errors = pages, errors or {}
        self.asked: list[str] = []

    def __call__(self, url, cfg, *, params=None):
        full = url + ("?" + "&".join(f"{k}={v}" for k, v in (params or {}).items())
                      if params else "")
        self.asked.append(full)
        for pattern, exc in self.errors.items():
            if pattern in url:
                raise exc
        for pattern, html in self.pages.items():
            if pattern in url:
                return html
        raise src.SourceError(url, "HTTP 404")


class ItTellsTheThreeFailuresApart(unittest.TestCase):

    def setUp(self):
        self.real = src.fetch
        self.addCleanup(lambda: setattr(src, "fetch", self.real))

    def probe(self, html=None, *, errors=None, district=None):
        src.fetch = Fetches({"cad.example": html} if html is not None else {}, errors)
        return probe.probe_url("https://cad.example/acct/1", district or DISTRICT, {})

    def test_a_page_carrying_a_value_is_a_match(self):
        result = self.probe(page("<td>Total Appraised Value</td><td>$41,250</td>"))
        self.assertEqual(result["verdict"], probe.MATCHED)
        self.assertEqual(result["parsed"]["appraised_value"], 41250.0)

    def test_money_on_the_page_that_did_not_parse_is_a_wording_problem(self):
        """The fix is `field_map`, and the probe has to hand over the wording."""
        result = self.probe(page("<td>Certified Roll Total</td><td>$41,250</td>"))
        self.assertEqual(result["verdict"], probe.WORDING)
        self.assertTrue(any("Certified Roll Total" in m for m in result["money_labels"]),
                        f"the wording to add was not reported: {result['money_labels']}")

    def test_no_money_anywhere_is_a_client_side_page(self):
        """No `field_map` wording can ever match a page with no values in it."""
        result = self.probe(page('<div id="root"></div>'))
        self.assertEqual(result["verdict"], probe.JAVASCRIPT)
        self.assertNotIn("money_labels", {k: v for k, v in result.items() if v})

    def test_and_it_reports_the_data_such_a_page_ships_with_itself(self):
        html = page('<div id="root"></div><script>window.__D={"appraisedValue":41250};</script>')
        result = self.probe(html)
        self.assertEqual(result["verdict"], probe.JAVASCRIPT)
        self.assertTrue(any("41250" in e for e in result["embedded_json"]),
                        f"the inline value was not surfaced: {result['embedded_json']}")

    def test_a_district_saying_it_has_no_such_account_is_not_a_parser_failure(self):
        result = self.probe(page("<p>No records found for that account.</p>"))
        self.assertEqual(result["verdict"], probe.NOT_FOUND)

    def test_a_page_without_the_markers_is_reported_as_that_and_not_diagnosed(self):
        """It was discarded before parsing, so a parse verdict would be a guess."""
        result = self.probe("<html><body>Totally different site $9,999</body></html>")
        self.assertEqual(result["verdict"], probe.MARKERS)
        self.assertEqual(result["markers_absent"], ["testcad"])

    def test_a_robots_disallow_is_never_called_a_parser_problem(self):
        result = self.probe(errors={"cad.example": src.RobotsDisallowed(
            "https://cad.example/acct/1", "robots.txt disallows this path")})
        self.assertEqual(result["verdict"], probe.ROBOTS)

    def test_an_unreachable_host_is_its_own_answer(self):
        result = self.probe(errors={"cad.example": src.SourceError(
            "https://cad.example/acct/1", "Name or service not known")})
        self.assertEqual(result["verdict"], probe.UNREACHABLE)
        self.assertIn("Name or service", result["detail"])

    def test_every_verdict_carries_advice_that_names_the_fix(self):
        """A verdict with no advice sends the reader back to the raw log."""
        for verdict in probe.VERDICT_ORDER:
            self.assertIn(verdict, probe.FIXES)
            self.assertGreater(len(probe.FIXES[verdict]), 20, verdict)


class TheDistrictVerdictIsTheFurthestAnyAttemptGot(unittest.TestCase):
    """One spelling missing is not the district's verdict.

    `account_variants` tries several, and `account_url_fallbacks` several more.
    Reporting whichever ran last would make a working district look broken on
    the strength of a 404 for a spelling nobody expected to work.
    """

    def test_a_match_anywhere_wins(self):
        self.assertEqual(probe.best([probe.UNREACHABLE, probe.MATCHED,
                                     probe.JAVASCRIPT]), probe.MATCHED)

    def test_wording_beats_javascript_because_it_is_the_cheaper_fix(self):
        self.assertEqual(probe.best([probe.JAVASCRIPT, probe.WORDING]), probe.WORDING)

    def test_a_real_answer_beats_a_refusal(self):
        self.assertEqual(probe.best([probe.ROBOTS, probe.NOT_FOUND]), probe.NOT_FOUND)

    def test_no_evidence_at_all_is_unreachable_rather_than_anything_hopeful(self):
        self.assertEqual(probe.best([]), probe.UNREACHABLE)


class ItAsksAboutRealAccounts(unittest.TestCase):
    """Invented account numbers would prove nothing.

    Half the plausible failures are about which spelling the roll indexes, and
    only the county's own listings carry that.
    """

    def setUp(self):
        import shutil, tempfile
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.saved = td.SNAPSHOT_DIR
        td.SNAPSHOT_DIR = self.tmp
        self.addCleanup(lambda: setattr(td, "SNAPSHOT_DIR", self.saved))

    def write(self, name: str, accounts: list[tuple[str, str]]):
        (self.tmp / name).write_text(json.dumps({"results": [
            {"listing": {"county": county, "account": account}}
            for county, account in accounts]}))

    def test_it_takes_accounts_from_the_newest_snapshot(self):
        self.write("2026-09-01.json", [("Dallas", "old-1")])
        self.write("2026-09-11.json", [("Dallas", "new-1"), ("Dallas", "new-2")])
        self.assertEqual(probe.sample_accounts("Dallas", 2), ["new-1", "new-2"])

    def test_it_only_takes_that_county(self):
        self.write("2026-09-11.json", [("Tarrant", "t-1"), ("Dallas", "d-1")])
        self.assertEqual(probe.sample_accounts("Dallas", 5), ["d-1"])

    def test_it_falls_back_to_an_older_snapshot_rather_than_giving_up(self):
        self.write("2026-09-01.json", [("Ellis", "e-1")])
        self.write("2026-09-11.json", [("Dallas", "d-1")])
        self.assertEqual(probe.sample_accounts("Ellis", 2), ["e-1"])

    def test_it_skips_an_unreadable_snapshot_instead_of_raising(self):
        (self.tmp / "2026-09-12.json").write_text("{not json")
        self.write("2026-09-11.json", [("Dallas", "d-1")])
        self.assertEqual(probe.sample_accounts("Dallas", 1), ["d-1"])

    def test_no_snapshot_is_reported_rather_than_probed_with_a_guess(self):
        self.assertEqual(probe.sample_accounts("Dallas", 3), [])
        out = probe.probe_district("DCAD", "Dallas",
                                   {"appraisal_districts": {"DCAD": DISTRICT}}, [])
        self.assertEqual(out["verdict"], probe.UNREACHABLE)
        self.assertIn("no accounts", out["note"])


class ItChangesNothing(unittest.TestCase):
    """A diagnostic that alters a screening result is not a diagnostic.

    The probe fetches the same URLs the screener does, so the risk is real: a
    cache entry written here would be served to the next run, and a miss
    recorded here would count toward `CAD_GIVE_UP_AFTER` and retire a district
    that nobody had screened yet.
    """

    def setUp(self):
        self.real = src.fetch
        self.addCleanup(lambda: setattr(src, "fetch", self.real))
        src.fetch = Fetches({"cad.example": page("<td>Appraised Value</td><td>$1,000</td>")})

    def test_it_writes_no_cache_entry(self):
        before = set(src.CACHE_DIR.rglob("*")) if src.CACHE_DIR.exists() else set()
        probe.probe_url("https://cad.example/acct/1", DISTRICT, {})
        after = set(src.CACHE_DIR.rglob("*")) if src.CACHE_DIR.exists() else set()
        self.assertEqual(before, after)

    def test_it_records_no_miss_against_the_give_up_counter(self):
        src.fetch = Fetches({"cad.example": page("<div id=root></div>")})
        before = dict(src._cad_misses)
        for _ in range(src.CAD_GIVE_UP_AFTER + 2):
            probe.probe_url("https://cad.example/acct/1", DISTRICT, {})
        self.assertEqual(dict(src._cad_misses), before)
        self.assertNotIn("DCAD", src.cad_abandoned)


class TheReportNamesTheFixRatherThanTheSymptom(unittest.TestCase):

    def test_it_prints_the_verdict_and_what_to_do_about_it(self):
        text = "\n".join(probe.render([{
            "district": "DCAD", "county": "Dallas", "name": "Dallas CAD",
            "verdict": probe.WORDING, "accounts": [{
                "account": "123", "attempts": [{
                    "url": "https://cad.example/acct/123", "verdict": probe.WORDING,
                    "bytes": 4096, "money_labels": ["Certified Roll Total = $41,250"],
                    "parsed": {"owner_name": "SMITH J"}}]}]}]))
        self.assertIn("DCAD", text)
        self.assertIn(probe.WORDING, text)
        self.assertIn("field_map", text)
        self.assertIn("Certified Roll Total", text)
        self.assertIn("https://cad.example/acct/123", text)

    def test_a_district_with_nothing_to_report_still_appears(self):
        """A district missing from the table reads as one that passed."""
        text = "\n".join(probe.render([{"district": "TAD", "county": "Tarrant",
                                        "name": "Tarrant AD", "verdict": probe.UNREACHABLE,
                                        "note": "no accounts", "accounts": []}]))
        self.assertIn("TAD", text)
        self.assertIn("no accounts", text)


if __name__ == "__main__":
    unittest.main()
