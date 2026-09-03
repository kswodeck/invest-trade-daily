#!/usr/bin/env python3
"""End-to-end run of the odd-lot pipeline, offline.

    python -m unittest tests.test_odd_lot_pipeline -v
    python tests/test_odd_lot_pipeline.py --demo    # print the run and the report

Drives `run_screen` from discovery through Gate 4 to the rendered markdown,
with the SEC client and the quote source replaced by stubs reading the pattern
fixtures. Everything between them is the production code path.

The `--demo` flag prints what a run looks like — the dry-run walkthrough, on a
machine with no route to sec.gov.
"""

from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import odd_lot  # noqa: E402
import publish_odd_lot  # noqa: E402

FIXTURES = REPO / "tests" / "fixtures" / "odd_lot"
CONFIG = json.loads((REPO / "config" / "odd_lot.json").read_text())
TODAY = date(2026, 9, 3)

# (fixture, ticker, form, market price, 30-day average volume)
CATALOG = [
    ("fixed_price_with_preference.html", "MIH", "SC TO-I", 17.80, 620_000),
    ("dutch_auction_with_preference.html", "CLDR", "SC TO-I", 8.05, 310_000),
    ("amendment_removes_preference.html", "NBEL", "SC TO-I/A", 5.85, 900_000),
    ("record_holder_condition.html", "PDMX", "SC TO-I", 4.05, 140_000),
    ("exchange_offer.html", "LKSP", "SC TO-T", 21.00, 480_000),
    ("debt_tender.html", "AMPL", "SC TO-I", 14.00, 260_000),
    ("no_preference_only_proration.html", "HWMC", "SC TO-I", 21.10, 350_000),
    ("expired_offer.html", "GFRD", "SC TO-I", 15.10, 200_000),
    ("restricted_to_qibs.html", "STLP", "SC TO-I", 29.90, 175_000),
    ("amendment_extends_only.html", "WTMB", "SC TO-I/A", 26.95, 410_000),
    # Clears Gate 1 but 99 shares costs $8,415 — over the $5,000 cap.
    ("fixed_price_with_preference.html", "EXPN", "SC TO-I", 85.00, 700_000),
]


class StubMarketData:
    """`quote` and `history` with the shape market_data actually returns."""

    def __init__(self, prices: dict[str, float], volumes: dict[str, int]) -> None:
        self.prices, self.volumes = prices, volumes

    def quote(self, symbol: str) -> dict:
        price = self.prices.get(symbol.upper())
        if price is None:
            return {"ok": False, "symbol": symbol}
        return {"ok": True, "symbol": symbol.upper(), "price": price,
                "asof": "2026-09-02T16:00:00-04:00", "source": "stub",
                "session": "closed"}

    def history(self, symbol: str, days: int = 120) -> dict:
        volume = self.volumes.get(symbol.upper())
        if volume is None:
            return {"ok": False, "symbol": symbol}
        return {"ok": True, "symbol": symbol.upper(), "avg_volume_30d": volume}


class StubDiscovery:
    """A SecClient whose EFTS query returns the catalog as EFTS-shaped hits."""

    def __init__(self) -> None:
        self.fetched = 0
        self.cache_hits = 0
        self.by_accession: dict[str, str] = {}
        self.hits: list[dict] = []
        for i, (fixture, ticker, form, _, _) in enumerate(CATALOG, start=1):
            accession = f"0001104659-26-{i:06d}"
            self.by_accession[accession] = (FIXTURES / fixture).read_text()
            self.hits.append({
                "accession": accession, "cik": "0000320193",
                "company": f"{ticker} Corp", "ticker": ticker, "form": form,
                "filed": "2026-09-01", "document": fixture,
                "url": f"https://www.sec.gov/Archives/{fixture}",
                "index_url": "https://www.sec.gov/Archives/index.htm",
                "highlights": [],
            })

    def get_json(self, url: str, *, params=None, cache_key=None):
        """One EFTS page, in the shape parse_efts_response expects."""
        return {"hits": {"hits": [
            {"_id": f"{h['accession']}:{h['document']}",
             "_source": {"ciks": [h["cik"]],
                         "display_names": [f"{h['company']}  ({h['ticker']})"],
                         "file_type": h["form"], "file_date": h["filed"]}}
            for h in self.hits]}}

    def get(self, url: str, *, params=None, cache_key: str | None = None) -> str:
        self.fetched += 1
        return self.by_accession[(cache_key or "").split("_")[0]]


class StubMarketData:
    """`quote` and `history` with the shape market_data actually returns."""

    def __init__(self, prices: dict[str, float], volumes: dict[str, int]) -> None:
        self.prices, self.volumes = prices, volumes

    def quote(self, symbol: str) -> dict:
        price = self.prices.get(symbol.upper())
        if price is None:
            return {"ok": False, "symbol": symbol}
        return {"ok": True, "symbol": symbol.upper(), "price": price,
                "asof": "2026-09-02T16:00:00-04:00", "source": "stub",
                "session": "closed"}

    def history(self, symbol: str, days: int = 120) -> dict:
        volume = self.volumes.get(symbol.upper())
        if volume is None:
            return {"ok": False, "symbol": symbol}
        return {"ok": True, "symbol": symbol.upper(), "avg_volume_30d": volume}


def build_run(tmp: Path) -> tuple[dict, StubDiscovery]:
    """A full `run_screen`, with the network replaced at its two edges.

    Discovery, deduplication, archiving, all four gates, tiering and the
    universe write are the production code path — only EDGAR and the quote
    source are stubs.
    """
    client = StubDiscovery()
    md = StubMarketData({t: p for _, t, _, p, _ in CATALOG},
                        {t: v for _, t, _, _, v in CATALOG})
    # run_screen narrates its progress, which is what you want from a workflow
    # step and noise in a test run.
    with contextlib.redirect_stdout(io.StringIO()):
        universe = odd_lot.run_screen(config=CONFIG, today=TODAY, discover=True,
                                      universe_path=tmp / "universe.json",
                                      client=client, md=md)
    return universe, client


class PipelineEndToEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.universe, cls.client = build_run(Path(cls.tmp.name))
        cls.by_ticker = {e["ticker"]: e for e in cls.universe["open"]}

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_the_two_clean_offers_are_the_only_candidates(self):
        candidates = sorted(e["ticker"] for e in self.universe["open"]
                            if e["status"] == "candidate")
        self.assertEqual(candidates, ["CLDR", "MIH", "WTMB"])

    def test_every_rejection_carries_a_reason(self):
        for entry in self.universe["open"]:
            if entry["status"] == "rejected":
                with self.subTest(ticker=entry["ticker"]):
                    self.assertTrue(entry["rejections"],
                                    "a rejection with no reason cannot be tuned")

    def test_an_offer_that_expired_before_it_was_ever_scored_is_archived(self):
        """Archiving runs on both sides of scoring, and this is why the second
        pass exists: on the day it is discovered, an already-expired offer has
        no stored expiration for the first pass to act on."""
        self.assertNotIn("GFRD", set(self.by_ticker))
        self.assertEqual([e["ticker"] for e in self.universe["archive"]], ["GFRD"])

    def test_the_capital_cap_rejects_an_otherwise_clean_offer(self):
        entry = self.by_ticker["EXPN"]
        self.assertEqual(entry["status"], "rejected")
        self.assertIn("over the $5,000 cap", " ".join(entry["rejections"]))

    def test_the_dutch_auction_is_priced_off_the_low_end(self):
        entry = self.by_ticker["CLDR"]
        self.assertEqual(entry["offer_price"], 8.20)
        self.assertAlmostEqual(entry["spread_pct"], (8.20 - 8.05) / 8.05, places=6)

    def test_two_shortfalls_together_are_tier_c(self):
        """CLDR is a 1.86% spread *and* a minimum-tender condition. Either alone
        would be Tier B; together they are two shortfalls, which is C."""
        entry = self.by_ticker["CLDR"]
        self.assertEqual(entry["risk_flags"], ["minimum_tender_condition"])
        self.assertLess(entry["spread_pct"], 0.03)
        self.assertEqual(entry["tier"], "C")

    def test_a_single_shortfall_is_tier_b(self):
        """WTMB clears every gate and misses Tier A only on spread."""
        entry = self.by_ticker["WTMB"]
        self.assertEqual(entry["risk_flags"], [])
        self.assertGreaterEqual(entry["days_to_expiry"], 7)
        self.assertLess(entry["spread_pct"], 0.03)
        self.assertEqual(entry["tier"], "B")

    def test_the_clean_fixed_price_offer_reaches_tier_a(self):
        entry = self.by_ticker["MIH"]
        self.assertEqual(entry["tier"], "A")
        self.assertEqual(entry["risk_flags"], [])
        self.assertEqual(entry["capital"], round(99 * 17.80, 2))

    def test_each_document_is_fetched_exactly_once(self):
        """Once per discovered filing, archived ones included — the offer that
        turned out to be expired still had to be read to find that out."""
        tracked = len(self.universe["open"]) + len(self.universe["archive"])
        self.assertEqual(self.client.fetched, tracked)
        self.assertEqual(tracked, len(CATALOG))

    def test_re_scoring_offline_needs_no_second_fetch(self):
        """Prices move daily; the document does not. An amendment arrives as a
        new filing with its own accession, never as an edit to this one."""
        before = self.client.fetched
        md = StubMarketData({e["ticker"]: 1.05 for e in self.universe["open"]},
                            {e["ticker"]: 999_999 for e in self.universe["open"]})
        for entry in list(self.universe["open"]):
            odd_lot.score_entry(dict(entry), client=None, md=md,
                                config=CONFIG, today=TODAY)
        self.assertEqual(self.client.fetched, before)


class RenderedReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        universe, _ = build_run(Path(cls.tmp.name))
        cls.report = odd_lot.render_report(universe, TODAY, CONFIG, slot="premarket")

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_the_report_quotes_the_odd_lot_paragraph(self):
        self.assertIn("Odd-lot language, quoted from the filing", self.report)
        self.assertIn("before proration", self.report)

    def test_the_report_lists_rejections_with_reasons(self):
        self.assertIn("## Rejected", self.report)
        self.assertIn("removes the odd-lot preference", self.report)
        self.assertIn("300 holders of record", self.report)

    def test_the_report_links_the_offer_document(self):
        self.assertIn("https://www.sec.gov/Archives/", self.report)

    def test_the_report_states_the_thresholds_it_applied(self):
        self.assertIn("Minimum spread **1.5%**", self.report)
        self.assertIn("$5,000", self.report)

    def test_an_empty_universe_says_so_plainly(self):
        """Zero Tier A is the normal result and must read as a finding, not as
        a blank page that could equally mean the run failed."""
        empty = odd_lot.render_report(dict(odd_lot.EMPTY_UNIVERSE), TODAY, CONFIG)
        self.assertIn("No Tier A opportunities today", empty)
        self.assertIn("_None._", empty)


class OddLotTab(unittest.TestCase):
    """The single Sheet tab: one live view, overwritten in place each run."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        universe, _ = build_run(Path(cls.tmp.name))
        cls.values, cls.header_row, cls.spec = publish_odd_lot.build_values(
            universe, CONFIG)
        cls.header = cls.values[cls.header_row - 1]
        cls.rows = [r for r in cls.values[cls.header_row:]
                    if len(r) == len(publish_odd_lot.HEADERS)]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def col(self, row: list, name: str):
        return row[publish_odd_lot.HEADERS.index(name)]

    def test_the_header_row_is_where_the_style_spec_says_it_is(self):
        self.assertEqual(self.header, publish_odd_lot.HEADERS)

    def test_live_offers_come_first_and_in_tier_order(self):
        tiers = [self.col(r, "Tier") for r in self.rows if self.col(r, "Tier")]
        self.assertEqual(tiers, ["A", "B", "C"])
        self.assertEqual([t for _, t in self.spec["tiers"]], ["A", "B", "C"])

    def test_a_rejected_row_keeps_the_economics_that_rejected_it(self):
        """A $8,415 capital rejection is only useful next to the price that
        caused it."""
        row = next(r for r in self.rows if self.col(r, "Ticker") == "EXPN")
        self.assertEqual(self.col(row, "Tier"), "")
        self.assertIn("REJECTED:", self.col(row, "Odd-lot language / why rejected"))
        self.assertIn("over the $5,000 cap",
                      self.col(row, "Odd-lot language / why rejected"))
        self.assertEqual(self.col(row, "Capital 99sh"), "$8,415.00")

    def test_market_price_above_offer_is_flagged_even_on_a_rejected_row(self):
        """The spec calls for flagging it prominently: it means the market
        disagrees with the offer, not merely that the spread is thin."""
        row = next(r for r in self.rows if self.col(r, "Ticker") == "EXPN")
        self.assertIn("market price above offer", self.col(row, "Risk flags"))

    def test_the_dutch_range_is_shown_next_to_the_price_it_resolves_to(self):
        row = next(r for r in self.rows if self.col(r, "Ticker") == "CLDR")
        self.assertEqual(self.col(row, "Offer"), "$8.20 (Dutch $8.20–$9.40)")

    def test_expired_offers_are_not_on_the_tab(self):
        """The tab is what is tenderable now; the report and the universe keep
        the history."""
        self.assertNotIn("GFRD", [self.col(r, "Ticker") for r in self.rows])

    def test_an_empty_universe_still_renders_a_usable_tab(self):
        values, header_row, _ = publish_odd_lot.build_values(
            dict(odd_lot.EMPTY_UNIVERSE), CONFIG)
        flat = " ".join(str(c) for row in values for c in row)
        self.assertIn("No Tier A opportunities", flat)
        self.assertIn("No open offer currently clears every gate", flat)
        self.assertEqual(values[header_row - 1], publish_odd_lot.HEADERS)

    def test_the_thresholds_are_printed_on_the_tab_itself(self):
        """So a number on this tab can be argued with without opening the repo."""
        flat = " ".join(str(c) for row in self.values[:5] for c in row)
        self.assertIn("fewer than 100", flat)
        self.assertIn("tender ALL", flat)
        self.assertIn("$5,000", flat)


def demo() -> int:
    """Print a full dry run and the report it produces."""
    with tempfile.TemporaryDirectory() as tmp:
        universe, client = build_run(Path(tmp))
        tiers = [e.get("tier") for e in universe["open"] if e["status"] == "candidate"]
        print(f"Scored {len(universe['open'])} open offer(s): {tiers.count('A')} Tier A, "
              f"{tiers.count('B')} Tier B, {tiers.count('C')} Tier C, "
              f"{sum(1 for e in universe['open'] if e['status'] == 'rejected')} rejected.")
        print(f"SEC requests: {client.fetched} fetched, {client.cache_hits} from cache.")
        odd_lot.print_universe(universe)
        print("\n" + "=" * 78 + "\n")
        print(odd_lot.render_report(universe, TODAY, CONFIG, slot="premarket"))
    return 0


if __name__ == "__main__":
    if "--demo" in sys.argv:
        raise SystemExit(demo())
    unittest.main()
