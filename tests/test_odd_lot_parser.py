#!/usr/bin/env python3
"""Tests for the odd-lot offer-document parser and Gate 1.

    python -m unittest discover -s tests -v

Gate 1 is the only thing standing between a headline number and a trade whose
premise is wrong, and every case below is a way the premise can be wrong while
the document still looks right at a glance: the preference removed by a later
amendment, the preference conditioned on a record-holder floor, an exchange
offer that pays in stock, a debt tender that happens to use the same phrase.

Two fixture sets, and they are not interchangeable —
see tests/fixtures/odd_lot/README.md. The `*.html` files are constructed
patterns; `real/` holds actual archived filings and is populated on demand by
`tests/fetch_odd_lot_fixtures.py`.
"""

from __future__ import annotations

import json
import sys
import unittest
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from odd_lot import (  # noqa: E402
    RECORD_HOLDER_CONDITION, OfferTerms, classify_subject_security, detect_risk_flags,
    find_odd_lot_passage, gate_document, html_to_text, parse_dates,
    parse_offer_document, parse_prices, _normalize_for_match,
)

FIXTURES = REPO / "tests" / "fixtures" / "odd_lot"
REAL = FIXTURES / "real"
TODAY = date(2026, 9, 3)


def fixture(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


def parse(name: str, *, amendment: bool = False) -> OfferTerms:
    return parse_offer_document(fixture(name), is_amendment=amendment)


class QualifyingOffers(unittest.TestCase):
    """Both halves of the preference present, in the same passage."""

    def test_fixed_price_offer_qualifies(self):
        terms = parse("fixed_price_with_preference.html")
        self.assertTrue(terms.has_threshold)
        self.assertTrue(terms.has_proration_preference)
        self.assertTrue(terms.is_cash_offer)
        self.assertTrue(terms.is_common_equity)
        self.assertEqual(terms.offer_price, 18.75)
        self.assertEqual(terms.price_basis, "fixed")
        self.assertEqual(terms.expiration_date, "2026-11-12")
        self.assertTrue(gate_document(terms, form="SC TO-I", today=TODAY).passed)

    def test_the_quoted_paragraph_is_the_odd_lot_paragraph(self):
        """The report's whole claim to being checkable rests on this quote."""
        terms = parse("fixed_price_with_preference.html")
        self.assertIsNotNone(terms.odd_lot_paragraph)
        quote = terms.odd_lot_paragraph
        self.assertIn("fewer than 100 Shares", quote)
        self.assertIn("before proration", quote)
        # And it is a passage from the document, not a reconstruction of one.
        self.assertIn(" ".join(quote.split()),
                      " ".join(html_to_text(fixture("fixed_price_with_preference.html")).split()))

    def test_dutch_auction_takes_the_low_end(self):
        """At or below the final price: the low end is the only guaranteed fill."""
        terms = parse("dutch_auction_with_preference.html")
        self.assertEqual(terms.dutch_range, (8.20, 9.40))
        self.assertEqual(terms.offer_price, 8.20)
        self.assertEqual(terms.price_basis, "dutch_low_end")
        self.assertTrue(gate_document(terms, form="SC TO-I", today=TODAY).passed)

    def test_an_amendment_that_only_extends_still_qualifies(self):
        terms = parse("amendment_extends_only.html", amendment=True)
        self.assertFalse(terms.preference_removed)
        result = gate_document(terms, form="SC TO-I/A", today=TODAY)
        self.assertTrue(result.passed)
        self.assertTrue(any("amendment" in w for w in result.warnings),
                        "an amendment must be flagged for reading against the original")
        self.assertEqual(terms.expiration_date, "2026-10-16")


class Rejections(unittest.TestCase):
    """Every one of these looks like an opportunity until the document is read."""

    def reasons(self, terms: OfferTerms, form: str = "SC TO-I") -> str:
        return " | ".join(gate_document(terms, form=form, today=TODAY).rejections)

    def test_amendment_removing_the_preference_is_rejected(self):
        """The Frontera Energy pattern: the preference withdrawn mid-offer.

        The offer is still live, still cash, still common stock, and still
        mentions odd lots throughout — everything except the one term that
        made it a trade. An amendment that is skipped rather than read is a
        position entered on terms that no longer exist.
        """
        terms = parse("amendment_removes_preference.html", amendment=True)
        self.assertTrue(terms.preference_removed)
        result = gate_document(terms, form="SC TO-I/A", today=TODAY)
        self.assertFalse(result.passed)
        self.assertTrue(any("removes the odd-lot preference" in r for r in result.rejections),
                        f"expected a preference-removal rejection, got {result.rejections}")

    def test_a_removal_is_only_read_out_of_an_amendment(self):
        """`preference_removed` is scoped to amendments on purpose.

        An original offer describing what it does *not* do must not be read as
        removing anything, and only an amendment can remove a term.
        """
        terms = parse("amendment_removes_preference.html", amendment=False)
        self.assertFalse(terms.preference_removed)

    def test_record_holder_condition_is_rejected(self):
        """The ITEX pattern: a preference that evaporates when it is used."""
        terms = parse("record_holder_condition.html")
        self.assertEqual(terms.record_holder_condition, 300)
        self.assertIn("300 holders of record", self.reasons(terms))

    def test_exchange_offer_is_rejected(self):
        terms = parse("exchange_offer.html")
        self.assertFalse(terms.is_cash_offer)
        self.assertIn("not a cash offer", self.reasons(terms))

    def test_debt_tender_is_rejected(self):
        """Same odd-lot phrasing, different security. 99 notes is not 99 shares."""
        terms = parse("debt_tender.html")
        self.assertFalse(terms.is_common_equity)
        self.assertIn("not common equity", self.reasons(terms))

    def test_offer_without_a_preference_is_rejected(self):
        """Odd lots named, proration described, and no priority given.

        The near-miss that a threshold-only or proration-only test would pass.
        """
        terms = parse("no_preference_only_proration.html")
        self.assertFalse(terms.has_proration_preference)
        self.assertIn("no acceptance-before-proration language", self.reasons(terms))

    def test_expired_offer_is_rejected(self):
        terms = parse("expired_offer.html")
        self.assertEqual(terms.expiration_date, "2025-02-14")
        self.assertIn("expired 2025-02-14", self.reasons(terms))

    def test_offer_restricted_to_qibs_is_rejected(self):
        terms = parse("restricted_to_qibs.html")
        self.assertTrue(terms.restricted_offer)
        self.assertIn("restricted to accredited investors", self.reasons(terms))


class TheFirstLiveRun(unittest.TestCase):
    """The two defects the 2026-09-03 premarket run surfaced.

    Both were invisible to the constructed fixtures because both live in the
    seam between EDGAR's response and the parser — the place a fixture written
    from the same assumptions as the code cannot reach.
    """

    def test_a_record_holder_floor_counts_people_not_shares(self):
        """"a holder of record of fewer than 100 Shares" is the preference
        itself, not the condition that voids it.

        The first live run rejected all four of its filings, two of them as the
        ITEX pattern with a floor of "100" — which is the odd-lot threshold. The
        capture must be followed by a word meaning people, or the screener
        rejects the commonest ways of writing the thing it looks for.
        """
        for text in (
            "If you are a holder of record of fewer than 100 Shares and you tender all",
            "Shares held of record by a shareholder who owns fewer than 100 Shares",
            "Any record holder who owns fewer than 100 Shares and tenders all of them",
            "Persons of record owning fewer than 100 shares may tender all such shares",
        ):
            with self.subTest(text=text[:48]):
                self.assertIsNone(
                    RECORD_HOLDER_CONDITION.search(_normalize_for_match(text)),
                    "the odd-lot definition was read as a record-holder floor")

    def test_a_genuine_record_holder_floor_is_still_caught(self):
        """The fix must not buy its precision by going blind."""
        for text, expected in (
            ("would result in the Shares being held of record by fewer than 300 persons", "300"),
            ("if it would reduce the number of holders of record below 300 holders", "300"),
            ("voided if fewer than 500 shareholders of record would remain", "500"),
        ):
            with self.subTest(text=text[:48]):
                match = RECORD_HOLDER_CONDITION.search(_normalize_for_match(text))
                self.assertIsNotNone(match, "a real ITEX-pattern condition was missed")
                self.assertEqual(next(g for g in match.groups() if g), expected)

    def test_an_amendment_is_recognised_from_the_document_not_the_form_string(self):
        """What arms the Frontera check must not depend on EFTS's form field.

        `file_type` is the exhibit type (EX-99.(A)(1)(III)) and `root_forms` is
        the *root* form, "SC TO-I" even for an SC TO-I/A. Deriving the flag
        from either leaves the check disarmed in production while every test
        that passes the flag by hand still passes.
        """
        terms = parse_offer_document(fixture("amendment_removes_preference.html"))
        self.assertTrue(terms.preference_removed)
        self.assertFalse(gate_document(terms, form="SC TO-I", today=TODAY).passed,
                         "rejected on the document, whatever the form string says")

    def test_an_original_offer_is_never_read_as_an_amendment(self):
        for name in ("fixed_price_with_preference.html",
                     "dutch_auction_with_preference.html",
                     "going_concern_offer.html"):
            with self.subTest(fixture=name):
                self.assertFalse(parse_offer_document(fixture(name)).preference_removed)


class PassageDetection(unittest.TestCase):
    def test_both_halves_must_be_in_the_same_passage(self):
        split = ("Holders who own fewer than 100 shares are Odd Lot Holders.\n\n"
                 "Some entirely unrelated paragraph about the tax consequences of "
                 "participating in the offer, long enough to be kept by the "
                 "paragraph filter and to separate the two halves.\n\n"
                 "A third paragraph, also unrelated, describing the mechanics of "
                 "the letter of transmittal and where to send it.\n\n"
                 "Shares will be accepted for payment before proration.")
        _, threshold, preference = find_odd_lot_passage(split)
        self.assertTrue(threshold)
        self.assertFalse(preference,
                         "halves three paragraphs apart must not be read as one preference")

    def test_adjacent_paragraphs_are_read_together(self):
        adjacent = ("If you own, beneficially or of record, fewer than 100 Shares in "
                    "the aggregate, you are an Odd Lot Holder for purposes of the Offer.\n\n"
                    "Shares tendered by Odd Lot Holders who tender all Shares owned will "
                    "be accepted for payment before proration of other tendered Shares.")
        passage, threshold, preference = find_odd_lot_passage(adjacent)
        self.assertTrue(threshold and preference)
        self.assertIn("fewer than 100 Shares", passage)
        self.assertIn("before proration", passage)


class RiskFlags(unittest.TestCase):
    """Gate 3 never rejects, but a wrong flag still costs an offer its tier."""

    def test_minimum_tender_condition_is_flagged(self):
        terms = parse("dutch_auction_with_preference.html")
        self.assertIn("minimum_tender_condition", terms.risk_flags)

    def test_a_negated_condition_is_not_a_flag(self):
        """"The Offer is not conditioned upon the receipt of financing."

        The sentence a clean offer uses to say it has no financing condition.
        Reading it as one would cost that offer its Tier A on the strength of
        a promise that it has no such condition.
        """
        terms = parse("fixed_price_with_preference.html")
        self.assertNotIn("financing_condition", terms.risk_flags)
        self.assertNotIn("minimum_tender_condition", terms.risk_flags)

    def test_an_unnegated_financing_condition_is_flagged(self):
        probe = _normalize_for_match(
            "The Offer is conditioned upon our receipt of financing on terms "
            "satisfactory to us.")
        self.assertIn("financing_condition", detect_risk_flags(probe))

    def test_a_negator_does_not_leak_across_a_sentence(self):
        probe = _normalize_for_match(
            "Shares may not be withdrawn after the Expiration Date. The Offer is "
            "conditioned upon our receipt of financing.")
        self.assertIn("financing_condition", detect_risk_flags(probe))


class SubjectSecurity(unittest.TestCase):
    def test_first_marker_in_the_cover_pages_wins(self):
        """A common-stock tender by a company that also has preferred outstanding."""
        cover = ("Offer to Purchase for Cash Up to 500,000 Shares of Common Stock. "
                 "The Company also has Series A Preferred Stock outstanding, which "
                 "is not subject to this Offer.")
        is_common, subject = classify_subject_security(cover)
        self.assertTrue(is_common)
        self.assertIn("Common Stock", subject)

    def test_a_preferred_tender_is_not_common_equity(self):
        cover = ("Offer to Purchase for Cash Any and All of its outstanding Series B "
                 "Preferred Stock. The Company's common stock is listed on Nasdaq.")
        is_common, subject = classify_subject_security(cover)
        self.assertFalse(is_common)


class DateParsing(unittest.TestCase):
    def test_the_time_of_day_does_not_stop_the_date(self):
        """"5:00 p.m." is full of periods, and a [^.] window died on them."""
        expiration, _, _ = parse_dates(
            "The Offer will expire at 5:00 p.m., New York City time, on "
            "October 15, 2026, unless extended.")
        self.assertEqual(expiration, "2026-10-15")

    def test_withdrawal_defaults_to_expiration_and_says_so(self):
        _, withdrawal, basis = parse_dates(
            "The Offer will expire at 5:00 p.m. on October 15, 2026. Shares may be "
            "withdrawn at any time prior to the Expiration Date.")
        self.assertEqual(withdrawal, "2026-10-15")
        self.assertEqual(basis, "expiration_date",
                         "an inferred deadline must be labelled as inferred")

    def test_an_extension_wins_over_the_date_it_superseded(self):
        """"previously scheduled to expire on X ... will now expire on Y".

        Taking the first date in that sentence reads a live, extended offer as
        one that expired two weeks ago.
        """
        expiration, _, _ = parse_dates(
            "The Offer, previously scheduled to expire at 5:00 p.m., New York City "
            "time, on October 1, 2026, has been extended and will now expire at "
            "5:00 p.m., New York City time, on October 16, 2026.")
        self.assertEqual(expiration, "2026-10-16")

    def test_without_an_extension_the_earliest_date_wins(self):
        """Failing closed: an early read drops a live offer, a late read
        publishes a dead one as tradeable."""
        expiration, _, _ = parse_dates(
            "The Offer will expire on October 9, 2026. Payment for Shares accepted "
            "following the Expiration Date will be made on or about "
            "November 20, 2026.")
        self.assertEqual(expiration, "2026-10-09")

    def test_an_unreadable_expiration_is_none_not_a_guess(self):
        expiration, _, _ = parse_dates("The Offer will expire in due course.")
        self.assertIsNone(expiration)


class PriceParsing(unittest.TestCase):
    def test_dutch_range_is_order_independent(self):
        for text in ("at a price not greater than $12.50 nor less than $10.75 per share",
                     "at a price not less than $10.75 nor greater than $12.50 per share"):
            with self.subTest(text=text):
                price, rng, basis = parse_prices(text)
                self.assertEqual(rng, (10.75, 12.50))
                self.assertEqual(price, 10.75)
                self.assertEqual(basis, "dutch_low_end")

    def test_fixed_price_variants(self):
        for text, expected in (
            ("$18.75 net per share in cash", 18.75),
            ("at a purchase price of $22.00 per share", 22.00),
            ("$4.25 per Share, net to the seller in cash", 4.25),
        ):
            with self.subTest(text=text):
                self.assertEqual(parse_prices(text)[0], expected)


class RealArchivedFilings(unittest.TestCase):
    """The same assertions, against filings EDGAR actually served.

    Skipped rather than failed when the directory is empty: tests.yml runs on a
    bare runner with no network by design, and the pattern fixtures cover the
    logic. Populate with `python tests/fetch_odd_lot_fixtures.py`.
    """

    @classmethod
    def setUpClass(cls):
        cls.manifest = []
        path = REAL / "manifest.json"
        if path.exists():
            cls.manifest = json.loads(path.read_text())
        if not cls.manifest:
            raise unittest.SkipTest(
                "no real filings fixtured — run `python tests/fetch_odd_lot_fixtures.py` "
                "(needs SEC_USER_AGENT and a route to sec.gov)")

    def test_at_least_three_real_filings_are_fixtured(self):
        self.assertGreaterEqual(
            len(self.manifest), 3,
            "fixture at least three real filings: "
            "`python tests/fetch_odd_lot_fixtures.py --days 365 --limit 5`")

    def test_every_real_filing_parses_to_a_qualifying_offer(self):
        for row in self.manifest:
            with self.subTest(accession=row["accession"], company=row["company"]):
                raw = (REAL / row["file"]).read_text(encoding="utf-8")
                terms = parse_offer_document(
                    raw, is_amendment=row["form"].upper().endswith("/A"))
                self.assertTrue(terms.has_threshold,
                                f"no 'fewer than 100 shares' threshold in {row['url']}")
                self.assertTrue(terms.has_proration_preference,
                                f"no before-proration language in {row['url']}")
                self.assertIsNotNone(terms.odd_lot_paragraph)
                self.assertIsNotNone(terms.expiration_date,
                                     f"no expiration date read from {row['url']}")
                self.assertIsNotNone(terms.offer_price,
                                     f"no offer price read from {row['url']}")


if __name__ == "__main__":
    unittest.main()
