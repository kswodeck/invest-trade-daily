"""End to end, with the network replaced by fixtures.

The required deliverable here is the dry run: a mode that produces every result
and touches no Sheet. It matters beyond convenience — this pipeline writes to a
spreadsheet the daily report also writes to, and a screening run that half
worked must never be the thing that rewrites the tab.
"""

from __future__ import annotations

import io
import contextlib
import json
import shutil
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "tax_deeds"
sys.path.insert(0, str(REPO / "scripts"))

import tax_deeds as td  # noqa: E402
import tax_deed_sources as tds  # noqa: E402
import tax_deed_screen as screen  # noqa: E402

SALE = "2026-10-06"


class FixtureSources:
    """Stands in for `tax_deed_sources`, reading the archived shapes instead.

    Deliberately the same three entry points the real module exposes, so the
    orchestration under test is the orchestration that ships.
    """

    FILES = {"Dallas": "dallas_realauction.html", "Tarrant": "tarrant_lgbs.html",
             "Johnson": "johnson_constable.html", "Ellis": "ellis_manual.csv"}

    def __init__(self, check_results: dict | None = None, broken: str | None = None):
        self.check_results = check_results or {}
        self.broken = broken
        self.verified = False

    def verify(self, cfg):
        self.verified = True
        return [{"kind": "county list", "id": name, "url": "fixture", "ok": True,
                 "detail": "fixture"} for name in self.FILES]

    def county_listings(self, county, cfg, sale_date=None):
        name = county["name"]
        source = county["sources"][0]
        if name == self.broken or name not in self.FILES:
            return [], [{"id": source["id"], "county": name, "ok": False,
                         "url": source["url"], "rows": 0,
                         "detail": "the page no longer contains its structural markers"}]
        text = (FIXTURES / self.FILES[name]).read_text()
        manual = self.FILES[name].endswith(".csv")
        if manual:
            rows, _ = tds.rows_from_csv(text, source["column_map"])
        else:
            rows, _ = tds.rows_from_tables(tds.collect_tables(text), source["column_map"])
        listings = []
        for raw in rows:
            if source.get("county_filter") and not manual:
                blob = " ".join(str(v) for v in raw.values()).lower()
                if source["county_filter"].lower() not in blob:
                    continue
            listings.append(tds.normalize_listing(raw, name, source, cfg))
        return listings, [{"id": source["id"], "county": name, "ok": True,
                           "url": source["url"], "rows": len(listings),
                           "detail": "fixture"}]

    def cad_record(self, cad_key, account, cfg):
        if not account:
            return None
        html = (FIXTURES / ("dcad_account.html" if cad_key == "DCAD" else "tad_account.html"))
        record = tds.parse_cad_record(html.read_text())
        # The fixture pages are one property each; re-key them onto whichever
        # account is being enriched so every listing gets a plausible match.
        record.update({"account": account, "cad": cad_key,
                       "cad_url": f"https://example.invalid/{cad_key}/{account}"})
        if cad_key != "DCAD":
            record["exemptions"] = []
            record.pop("homestead", None)
        return record

    def run_checks(self, listing, cad, cfg):
        out = []
        for name in list(td.LIEN_CHECKS) + ["flood_zone", "road_frontage", "lot_size"]:
            result = self.check_results.get(name, td.CLEAN)
            out.append(td.check_record(name, result, "fixture", f"{name} {result}"))
        return out


class DryRun(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self._saved = (td.SNAPSHOT_DIR, td.PACKET_DIR)
        td.SNAPSHOT_DIR = self.tmp / "data"
        td.PACKET_DIR = self.tmp / "reports"
        self._publish = screen.publish
        screen.publish = self._must_not_publish

    def tearDown(self):
        td.SNAPSHOT_DIR, td.PACKET_DIR = self._saved
        screen.publish = self._publish
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _must_not_publish(self, *args, **kwargs):
        self.fail("a dry run reached the Google Sheet")

    def run_screen(self, *extra, check_results=None, broken=None):
        sources = FixtureSources(check_results, broken)
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            code = screen.main(["--dry-run", "--no-verify", "--sale-date", SALE, *extra],
                               sources=sources)
        return code, out.getvalue(), sources

    def test_a_dry_run_prints_the_tab_and_writes_no_sheet(self):
        code, output, _ = self.run_screen()
        self.assertEqual(code, 0)
        self.assertIn("DRY RUN", output)
        self.assertIn("Sheet not touched.", output)
        self.assertIn("NOT A TITLE SEARCH", output)

    def test_it_archives_the_run_snapshot(self):
        self.run_screen()
        snapshots = list((self.tmp / "data").glob("*.json"))
        self.assertEqual(len(snapshots), 1)
        payload = json.loads(snapshots[0].read_text())
        self.assertEqual(payload["sale_date"], SALE)
        self.assertIn("NOT A TITLE SEARCH", payload["disclaimer"])
        self.assertGreater(payload["totals"]["listings"], 0)
        self.assertEqual(payload["counties"], ["Dallas", "Tarrant", "Johnson", "Ellis"])

    def test_the_snapshot_records_the_thresholds_the_run_actually_used(self):
        self.run_screen()
        payload = json.loads(next((self.tmp / "data").glob("*.json")).read_text())
        self.assertEqual(payload["thresholds"]["MAX_OPENING_BID"], 20000)
        self.assertEqual(payload["thresholds"]["QUIET_TITLE_BUDGET"], 3500)
        self.assertEqual(payload["thresholds"]["HOLDING_MONTHS"], 7)

    def test_packets_are_written_for_tier_a_and_b_only(self):
        self.run_screen()
        packets = sorted((self.tmp / "reports" / SALE).glob("*.md"))
        self.assertTrue(packets)
        payload = json.loads(next((self.tmp / "data").glob("*.json")).read_text())
        expected = sum(1 for r in payload["results"] if r["tier"] in ("A", "B"))
        self.assertEqual(len(packets), expected)
        for packet in packets:
            text = packet.read_text()
            self.assertIn("NOT A TITLE SEARCH", text)
            self.assertIn("- [ ] Title search ordered", text)

    def test_the_dallas_homestead_fixture_is_rejected_not_shortlisted(self):
        """DCAD's fixture carries a Residence Homestead exemption.

        The cancelled row is rejected before enrichment ever runs — there is no
        point paying three requests for a listing already off the sale — so it
        is rejected on its status alone and never sees a CAD record.
        """
        self.run_screen("--county", "Dallas")
        payload = json.loads(next((self.tmp / "data").glob("*.json")).read_text())
        self.assertTrue(payload["results"])
        self.assertEqual(payload["totals"]["candidates"], 0)
        reasons = {r["listing"]["cause_number"]: {x["code"] for x in r["rejections"]}
                   for r in payload["results"]}
        self.assertTrue(all(reasons.values()), "every Dallas row must be rejected")
        self.assertEqual(reasons["TX-19-02277"], {"withdrawn"})
        self.assertTrue(any("homestead" in codes for codes in reasons.values()))

    def test_a_listing_rejected_on_the_cheap_gates_is_never_enriched(self):
        """Enrichment is three requests a property; a withdrawn one earns none."""
        sources = FixtureSources()
        looked_up = []
        original = sources.cad_record
        sources.cad_record = lambda key, acct, cfg: (looked_up.append(acct)
                                                     or original(key, acct, cfg))
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            screen.main(["--dry-run", "--no-verify", "--sale-date", SALE,
                         "--county", "Dallas"], sources=sources)
        self.assertNotIn("00000444444444000", looked_up,
                         "the cancelled listing must not cost a CAD lookup")

    def test_a_federal_tax_lien_hit_empties_the_shortlist(self):
        _, output, _ = self.run_screen(check_results={"federal_tax_lien": td.HIT})
        payload = json.loads(next((self.tmp / "data").glob("*.json")).read_text())
        self.assertEqual(payload["totals"]["candidates"], 0)
        self.assertIn("federal_tax_lien", output)

    def test_unavailable_lien_checks_leave_candidates_but_strip_their_rank(self):
        self.run_screen(check_results={"federal_tax_lien": td.UNAVAILABLE})
        payload = json.loads(next((self.tmp / "data").glob("*.json")).read_text())
        candidates = [r for r in payload["results"] if r["status"] == "candidate"]
        self.assertTrue(candidates)
        for result in candidates:
            self.assertEqual(result["tier"], "C")
            self.assertIn("federal_tax_lien", result["checks_unavailable"])

    def test_all_four_counties_appear_even_when_one_has_no_candidates(self):
        code, output, _ = self.run_screen()
        self.assertEqual(code, 0)
        for name in ("DALLAS", "TARRANT", "JOHNSON", "ELLIS"):
            self.assertIn(f"{name} COUNTY", output.upper())

    def test_a_broken_source_exits_non_zero_and_names_the_url(self):
        """County sites change format without notice; a silent empty tab reads
        exactly like `no sales this month`, which is the dangerous failure."""
        code, output, _ = self.run_screen(broken="Johnson")
        self.assertEqual(code, 1)
        self.assertIn("Sources that failed", output)
        self.assertIn("johnsoncountytx.org", output)

    def test_the_summary_reports_the_34015_blocker(self):
        _, output, _ = self.run_screen()
        self.assertIn("§34.015", output)
        self.assertIn("written statement", output.lower())

    def test_no_files_skips_both_file_outputs(self):
        self.run_screen("--no-files")
        self.assertFalse((self.tmp / "data").exists())
        self.assertFalse((self.tmp / "reports").exists())

    def test_verification_runs_before_ingest_unless_switched_off(self):
        sources = FixtureSources()
        with contextlib.redirect_stdout(io.StringIO()), \
             contextlib.redirect_stderr(io.StringIO()):
            screen.main(["--dry-run", "--sale-date", SALE], sources=sources)
        self.assertTrue(sources.verified)


class CheckFailuresAreNeverClean(unittest.TestCase):
    def test_a_raising_check_adapter_becomes_unavailable_not_absent(self):
        class Exploding(FixtureSources):
            def run_checks(self, listing, cad, cfg):
                raise RuntimeError("clerk portal timed out")

        cfg = td.load_config()
        with contextlib.redirect_stderr(io.StringIO()):
            results, _ = screen.collect(cfg, date(2026, 9, 3), SALE, ["Tarrant"],
                                        Exploding())
        self.assertTrue(results)
        for result in results:
            for name in td.LIEN_CHECKS:
                self.assertIn(name, result["checks_unavailable"])
            self.assertNotEqual(result["tier"], "A")


if __name__ == "__main__":
    unittest.main()


class PacketTierSwitch(unittest.TestCase):
    """The realistic production case: every candidate is Tier C."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self._saved = (td.SNAPSHOT_DIR, td.PACKET_DIR)
        td.SNAPSHOT_DIR, td.PACKET_DIR = self.tmp / "data", self.tmp / "reports"
        self._publish, screen.publish = screen.publish, self._fail

    def tearDown(self):
        td.SNAPSHOT_DIR, td.PACKET_DIR = self._saved
        screen.publish = self._publish
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _fail(self, *a, **k):
        self.fail("a dry run reached the Google Sheet")

    def _run(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            screen.main(["--dry-run", "--no-verify", "--sale-date", SALE],
                        sources=FixtureSources({"federal_tax_lien": td.UNAVAILABLE}))
        return out.getvalue()

    def test_all_tier_c_writes_no_packets_and_says_why(self):
        output = self._run()
        self.assertFalse(list((self.tmp / "reports").rglob("*.md")))
        self.assertIn("PACKET_TIERS=A,B,C", output)

    def test_widening_the_knob_writes_one_per_candidate(self):
        import os
        os.environ["PACKET_TIERS"] = "A,B,C"
        try:
            self._run()
        finally:
            del os.environ["PACKET_TIERS"]
        packets = list((self.tmp / "reports").rglob("*.md"))
        payload = json.loads(next((self.tmp / "data").glob("*.json")).read_text())
        self.assertTrue(packets)
        self.assertEqual(len(packets), payload["totals"]["candidates"])
        for packet in packets:
            self.assertIn("federal tax lien | **unavailable — not screened**",
                          packet.read_text())



class EveryListFailed(unittest.TestCase):
    """The first live run hit this and left nothing behind but the job log.

    Exiting before the snapshot was written meant the only record of which URL
    broke, and why, scrolled past in raw CI output. The Sheet must still go
    untouched — an empty `Tax Deeds` tab reads like "no sales this month",
    which is the one failure that would cost a sale date — but the diagnosis
    has to survive on disk.
    """

    class AllBroken(FixtureSources):
        def verify(self, cfg):
            self.verified = True
            return [{"kind": "county list", "id": "dallas_auction",
                     "url": "https://dallas.example.invalid/", "ok": False,
                     "detail": "HTTP 403: the host refused this User-Agent"},
                    {"kind": "county list", "id": "tarrant_auction",
                     "url": "https://agg.example.invalid/", "ok": False,
                     "detail": "the page contains no HTML table at all"}]

        def county_listings(self, county, cfg, sale_date=None):
            raise AssertionError("nothing should be ingested when every list failed")

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self._saved = (td.SNAPSHOT_DIR, td.PACKET_DIR)
        td.SNAPSHOT_DIR, td.PACKET_DIR = self.tmp / "data", self.tmp / "reports"
        self._publish = screen.publish
        screen.publish = self._fail

    def tearDown(self):
        td.SNAPSHOT_DIR, td.PACKET_DIR = self._saved
        screen.publish = self._publish
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _fail(self, *a, **k):
        self.fail("the Sheet was written despite every source failing")

    def _run(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = screen.main(["--sale-date", SALE], sources=self.AllBroken())
        return code, out.getvalue() + err.getvalue()

    def test_it_exits_2_not_1_so_the_workflow_can_tell_them_apart(self):
        code, _ = self._run()
        self.assertEqual(code, 2)

    def test_the_snapshot_still_records_every_source_and_its_error(self):
        self._run()
        payload = json.loads(next((self.tmp / "data").glob("*.json")).read_text())
        failed = {s["id"]: s["detail"] for s in payload["sources"] if not s["ok"]}
        self.assertEqual(set(failed), {"dallas_auction", "tarrant_auction"})
        self.assertIn("403", failed["dallas_auction"])
        self.assertEqual(payload["totals"]["listings"], 0)

    def test_the_output_names_the_urls_and_says_the_sheet_was_spared(self):
        _, output = self._run()
        self.assertIn("https://dallas.example.invalid/", output)
        self.assertIn("no sales this month", output)
        self.assertIn("Sources that failed", output)

