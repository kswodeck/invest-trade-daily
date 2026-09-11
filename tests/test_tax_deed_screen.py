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

    def test_all_tier_c_still_gets_a_packet_each_by_default(self):
        """The whole point of the default change: an unscreened shortlist is
        worked by reading the flag list, and that needs the packet."""
        self._run()
        payload = json.loads(next((self.tmp / "data").glob("*.json")).read_text())
        packets = list((self.tmp / "reports").rglob("*.md"))
        self.assertTrue(packets)
        self.assertEqual(len(packets), payload["totals"]["candidates"])

    def test_narrowing_the_knob_to_a_and_b_writes_none_and_says_why(self):
        import os
        os.environ["PACKET_TIERS"] = "A,B"
        try:
            output = self._run()
        finally:
            del os.environ["PACKET_TIERS"]
        self.assertFalse(list((self.tmp / "reports").rglob("*.md")))
        self.assertIn("PACKET_TIERS=A,B,C", output)

    def test_every_packet_carries_the_flags_that_held_it_at_tier_c(self):
        self._run()
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



class ARobotsDisallowIsPolicyNotBreakage(unittest.TestCase):
    """The four clerk portals disallow crawling and always will.

    Counting that as a source failure returned exit code 1 on every run —
    including the run that screened 370 listings and published 328 candidates.
    A workflow that is red whether or not anything is wrong tells you nothing,
    and the first thing you learn from it is to stop looking.
    """

    def summary(self, report):
        cfg = td.load_config()
        statements = td.statement_report(cfg, ["Dallas"], date(2026, 9, 7), SALE)
        return "\n".join(screen.summarize(cfg, [], statements, report, SALE,
                                          date(2026, 9, 7)))

    def policy_entry(self, **over):
        entry = {"kind": "lien: federal_tax_lien", "id": "federal_tax_lien/Dallas",
                 "url": "https://dallas.tx.publicsearch.us/", "ok": True, "policy": True,
                 "detail": "not permitted by robots.txt on all 2 host(s) — this check "
                           "reports unavailable, which is a flag, on every row."}
        entry.update(over)
        return entry

    def test_it_is_not_listed_among_the_failures(self):
        text = self.summary([self.policy_entry()])
        self.assertNotIn("Sources that failed", text)

    def test_but_it_is_listed(self):
        """Silence would read as 'the lien check ran and found nothing'."""
        text = self.summary([self.policy_entry()])
        self.assertIn("Checks not permitted", text)
        self.assertIn("federal_tax_lien/Dallas", text)

    def test_and_says_the_rows_carry_a_flag_for_it(self):
        text = self.summary([self.policy_entry()])
        self.assertIn("unavailable", text)
        self.assertIn("Tier A", text)

    def test_and_says_disabling_robots_is_not_the_fix(self):
        text = self.summary([self.policy_entry()])
        self.assertIn("respect_robots_txt", text)

    def test_a_real_failure_alongside_it_still_gets_its_own_section(self):
        broken = {"kind": "county list", "id": "dallas_auction", "ok": False,
                  "url": "https://dallas.example.invalid/", "detail": "HTTP 404"}
        text = self.summary([self.policy_entry(), broken])
        self.assertIn("Sources that failed", text)
        self.assertIn("dallas_auction", text)
        self.assertIn("Checks not permitted", text)

    def test_the_exit_code_ignores_policy_entries(self):
        report = [self.policy_entry(), {"id": "ok_one", "ok": True}]
        self.assertEqual([s for s in report if not s.get("ok")], [])


class ARunThatRunsOutOfTimeStillLeavesARecord(unittest.TestCase):
    """A job killed by the workflow's timeout runs no further steps.

    So the snapshot is never committed and the step summary is never written —
    exactly the failure this module goes out of its way to prevent for exit
    codes 1 and 2, where the record of what broke has to survive the failure.
    On 2026-09-07 a run was cancelled at 45m21s and left nothing behind at all.

    Enrichment is the only unbounded part, so it is what gets cut. Everything
    already fetched is still screened, ranked and written.
    """

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def run_with(self, *extra):
        sources = FixtureSources(None, None)
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = screen.main(["--dry-run", "--no-verify", "--no-files",
                                "--sale-date", SALE, *extra], sources=sources)
        return code, out.getvalue(), err.getvalue()

    def test_the_run_still_succeeds_and_still_reports(self):
        code, out, _ = self.run_with("--deadline-minutes", "0.0000001")
        self.assertEqual(code, 0)
        self.assertIn("DRY RUN", out)

    def test_it_says_it_ran_out_of_time(self):
        """Silence here would read as 'the appraisal district had nothing'."""
        _, _, err = self.run_with("--deadline-minutes", "0.0000001")
        self.assertIn("out of time", err)

    def test_the_summary_says_the_rows_were_never_looked_up(self):
        _, out, _ = self.run_with("--deadline-minutes", "0.0000001")
        self.assertIn("ran out of time", out)
        self.assertIn("never looked up", out)

    def test_zero_disables_it(self):
        _, out, err = self.run_with("--deadline-minutes", "0")
        self.assertNotIn("out of time", err)
        self.assertNotIn("ran out of time", out)

    def test_a_generous_deadline_does_not_fire(self):
        _, out, err = self.run_with("--deadline-minutes", "60")
        self.assertNotIn("out of time", err)
        self.assertNotIn("ran out of time", out)

    def test_the_default_stays_inside_the_workflow_timeout(self):
        """45 minutes is the job cap. The screener's own clock must beat it."""
        self.assertLess(screen.DEFAULT_DEADLINE_MINUTES, 45)
        self.assertGreater(screen.DEFAULT_DEADLINE_MINUTES, 20)

    def test_the_deadline_helper_returns_none_when_disabled(self):
        self.assertIsNone(screen.enrichment_deadline(0))
        self.assertIsNone(screen.enrichment_deadline(None))
        self.assertIsNotNone(screen.enrichment_deadline(5))


class APacketGateWithholdsAFileNotAProperty(unittest.TestCase):
    """One run wrote 572 packets, 541 for properties with no auction assigned.

    That is several hundred files a run, twice a week, for rows that are not on
    the sale being screened. The gate is `PACKET_DOCKETS`, and it is bounded to
    exactly one thing: whether a markdown checklist is written to disk.

    Having no sale date is never a reason to reject, rank down, or drop a row —
    and the default proves it, because `over_the_counter` has no sale date and
    is *kept*: struck-off property is buyable from the county today, which makes
    it the most actionable category there is. Keying this on "has a date" would
    have cut precisely the rows a buyer can act on soonest.
    """

    def setUp(self):
        # The listing/cad/checks fixtures live with the gate tests they were
        # written for; reusing them keeps one definition of "a normal listing".
        from test_tax_deeds import TODAY, cad, checks, codes, listing
        self.fixtures = (TODAY, listing, cad, checks, codes)
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        # Both directories, like every other class here. Patching only
        # PACKET_DIR let the two `screen.main` tests below write a fixture
        # snapshot straight into the repo's `data/tax_deeds/`, where a later
        # `git add -A` committed 12 fixture rows over a 1,185-listing run
        # record. Snapshots are the run history `offer_history` reads.
        self._saved = (td.SNAPSHOT_DIR, td.PACKET_DIR)
        td.SNAPSHOT_DIR, td.PACKET_DIR = self.tmp / "data", self.tmp / "reports"
        self.addCleanup(lambda: setattr(td, "SNAPSHOT_DIR", self._saved[0]))
        self.addCleanup(lambda: setattr(td, "PACKET_DIR", self._saved[1]))
        self.cfg = td.load_config()
        self.statements = td.statement_report(self.cfg, ["Dallas"], TODAY, SALE)

    def screened(self, **listing_over):
        today, listing, cad, checks, _ = self.fixtures
        return td.screen(listing(**listing_over), cad(), checks(), self.cfg, today, SALE)

    def flag_codes(self, result):
        return self.fixtures[4](result["flags"])

    def write(self, results, dockets=None):
        cfg = self.cfg
        if dockets is not None:
            cfg = dict(cfg, thresholds=dict(cfg.get("thresholds") or {},
                                            PACKET_DOCKETS=dockets))
        return screen.write_packets(results, cfg, self.statements)

    def test_an_on_docket_property_gets_a_packet(self):
        written, _ = self.write([self.screened(sale_date=SALE)])
        self.assertEqual(len(written), 1)

    def test_a_struck_off_property_gets_one_too_despite_having_no_sale_date(self):
        """The case that makes 'no date' the wrong thing to gate on."""
        result = self.screened(sale_date=None, sale_type="struck_off")
        self.assertEqual(result["docket"]["state"], td.OVER_THE_COUNTER)
        written, withheld = self.write([result])
        self.assertEqual(len(written), 1)
        self.assertEqual(withheld, {})

    def test_an_unscheduled_property_gets_no_file(self):
        written, withheld = self.write(
            [self.screened(sale_date=None, status="Available for Future Sale")])
        self.assertEqual(written, [])
        self.assertEqual(withheld, {td.NOT_SCHEDULED: 1})

    def test_but_it_is_still_a_candidate(self):
        """The whole point. Withholding a file is not a verdict."""
        result = self.screened(sale_date=None, status="Available for Future Sale")
        self.write([result])
        self.assertEqual(result["status"], "candidate")
        self.assertEqual(result["rejections"], [])
        self.assertIsNotNone(result["tier"])

    def test_the_packet_gate_is_not_what_keeps_it_off_the_sheet(self):
        """Whether a row is published is `SHEET_DOCKETS`, decided separately.

        Withholding the packet must not also withhold the row; the two gates
        are configured apart so each can be reasoned about on its own.
        """
        off = self.screened(sale_date=None, status="Available for Future Sale")
        on = self.screened(sale_date=SALE, account="22")
        self.write([off, on])          # packets: `off` gets none
        cfg = dict(self.cfg, thresholds=dict(
            self.cfg.get("thresholds") or {},
            SHEET_DOCKETS="on_docket,over_the_counter,other_sale,"
                          "date_unknown,not_scheduled"))
        _, spec = td.sheet_rows([off, on], cfg, self.fixtures[0], SALE, self.statements)
        self.assertEqual(len(spec["data_rows"]), 2)

    def test_and_the_gate_adds_no_flag_of_its_own(self):
        before = self.screened(sale_date=None, status="Available for Future Sale")
        codes_before = self.flag_codes(before)
        self.write([before])
        self.assertEqual(self.flag_codes(before), codes_before)

    def test_the_withheld_count_is_reported_rather_than_silent(self):
        _, withheld = self.write(
            [self.screened(sale_date=None, status="Available for Future Sale"),
             self.screened(sale_date=None, status="Pending", account="23")])
        self.assertEqual(sum(withheld.values()), 2)

    def test_it_is_configurable_back_to_everything(self):
        result = self.screened(sale_date=None, status="Available for Future Sale")
        written, withheld = self.write(
            [result], dockets="on_docket,over_the_counter,other_sale,"
                              "not_scheduled,date_unknown")
        self.assertEqual(len(written), 1)
        self.assertEqual(withheld, {})

    def test_the_tier_gate_still_applies_independently(self):
        # The fixture screens to Tier A, so exclude A to make the tier miss.
        cfg = dict(self.cfg, thresholds=dict(self.cfg.get("thresholds") or {},
                                             PACKET_TIERS="B,C"))
        result = self.screened(sale_date=SALE)
        self.assertEqual(result["tier"], "A")
        written, withheld = screen.write_packets([result], cfg, self.statements)
        self.assertEqual(written, [])
        self.assertEqual(withheld, {}, "a tier miss is not a docket withholding")

    def test_a_whole_run_says_out_loud_what_it_withheld(self):
        """Unit counts are not enough — the operator reads the console."""
        class Unscheduled(FixtureSources):
            def county_listings(self, county, cfg, sale_date):
                rows, report = super().county_listings(county, cfg, sale_date)
                for row in rows:
                    row["sale_date"] = None
                    row["status"] = "Available for Future Sale"
                return rows, report

        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            screen.main(["--dry-run", "--no-verify", "--sale-date", SALE],
                        sources=Unscheduled(None, None))
        text = out.getvalue()
        self.assertIn("no packet for", text)
        self.assertIn("still screened", text)
        self.assertIn("withholds a file, not a property", text)
        self.assertIn("PACKET_DOCKETS", text)
        # A test that screens for real must not write into the repo. This one
        # did, once, and a `git add -A` committed fixture rows over a live run.
        self.assertTrue(list((self.tmp / "data").glob("*.json")),
                        "the snapshot did not land in the temp directory")
        self.assertNotEqual(td.SNAPSHOT_DIR, self._saved[0],
                            "the real snapshot directory was still in play")

    def test_and_the_sheet_never_calls_a_held_back_row_a_rejected_one(self):
        """The sentence above has to be true, not just printed.

        A county whose every candidate is held off the tab used to print "no
        listing survived the gates for this county", which is a finding the run
        did not make — those rows passed every gate. The test only passed
        because the dry run truncated cells to 26 characters and the sentence
        was never visible, so the dry run prints notes in full now too.
        """
        class Unscheduled(FixtureSources):
            def county_listings(self, county, cfg, sale_date):
                rows, report = super().county_listings(county, cfg, sale_date)
                for row in rows:
                    row["sale_date"] = None
                    row["status"] = "Available for Future Sale"
                return rows, report

        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            code = screen.main(["--dry-run", "--no-verify", "--sale-date", SALE],
                               sources=Unscheduled(None, None))
        text = out.getvalue()
        self.assertEqual(code, 0)
        self.assertIn("DRY RUN", text)

        # The fixture gives both cases, which is what makes this a test of the
        # distinction rather than of one wording. Dallas's five listings are
        # all rejected outright; Tarrant's two pass every gate and are held
        # back only for having no docket.
        tarrant = text.split("TARRANT COUNTY")[-1].split("JOHNSON COUNTY")[0]
        self.assertNotIn("no listing survived the gates", tarrant)
        self.assertIn("none of them on a docket", tarrant)
        self.assertIn("still screened and in the snapshot", tarrant)
        dallas = text.split("DALLAS COUNTY")[-1].split("TARRANT COUNTY")[0]
        self.assertIn("no listing survived the gates", dallas)

        # And the run's own record keeps every held-back row.
        snapshot = json.loads(sorted((self.tmp / "data").glob("*.json"))[0].read_text())
        kept = [r for r in snapshot["results"] if r["status"] == "candidate"]
        self.assertTrue(kept, "held-back candidates vanished from the snapshot")
        self.assertTrue(all(r["docket"]["state"] == td.NOT_SCHEDULED for r in kept))

    def test_the_step_summary_accounts_for_the_rows_the_tab_does_not_show(self):
        """A reader comparing the summary's count to the tab's needs the reason.

        The summary counts the run; the tab carries a subset. Two numbers that
        differ with nothing to explain the gap is how a tool earns distrust.
        """
        off = self.screened(sale_date=None, status="Available for Future Sale")
        on = self.screened(sale_date=SALE, account="31")
        text = "\n".join(screen.summarize(
            self.cfg, [off, on], self.statements, [], SALE, self.fixtures[0]))
        self.assertIn("held off the `Tax Deeds` tab", text)
        self.assertIn("1 not scheduled", text)
        self.assertIn("Nothing is rejected", text)
        self.assertIn("SHEET_DOCKETS", text)

    def test_and_says_nothing_when_the_tab_shows_everything(self):
        on = self.screened(sale_date=SALE)
        text = "\n".join(screen.summarize(
            self.cfg, [on], self.statements, [], SALE, self.fixtures[0]))
        self.assertNotIn("held off the", text)

    def test_the_default_keeps_every_state_that_has_somewhere_to_be(self):
        keep = td.packet_dockets(self.cfg)
        self.assertIn(td.ON_DOCKET, keep)
        self.assertIn(td.OVER_THE_COUNTER, keep)
        self.assertIn(td.OTHER_SALE, keep)
        self.assertNotIn(td.NOT_SCHEDULED, keep)
