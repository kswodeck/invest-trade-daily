# Odd-lot parser fixtures

Two kinds of fixture live here, and the difference matters.

## `*.html` — language patterns

Constructed documents, each built around one clause pattern the parser has to
get right: a fixed-price offer, a Dutch auction, the Frontera-style amendment
that removes the preference, the ITEX-style record-holder condition, an
exchange offer, a debt tender, an expired offer, an offer whose auditor doubts
it survives to settle, and the near-misses that must *not* pass (odd lots
defined but never given priority; a pro-rata sentence with no odd-lot
threshold).

**They are not transcripts of any filing.** Nothing here is quoted from an
issuer document, and nothing in them should be cited as if it were. They are
test inputs written to exercise the regexes, in the register real offer
documents use.

## `real/` — actual archived filings

Empty in the repository, and populated on demand:

```bash
python tests/fetch_odd_lot_fixtures.py            # trailing 120 days
python tests/fetch_odd_lot_fixtures.py --days 365 --limit 8
```

That script queries EDGAR full-text search for real `SC TO-I` filings
containing odd-lot language, saves the primary offer documents here, and writes
`manifest.json` recording each one's accession number, company, form, filing
date and URL — so every fixture traces back to the document it came from.

`tests/test_odd_lot_parser.py` runs the same assertions over every file it
finds in `real/`, and skips that class with the command above when the
directory is empty. It is skipped rather than failed because
`.github/workflows/tests.yml` runs on a bare runner with no network by design.

Fixtures were not committed by the change that added this module: the session
that wrote it had no route to `sec.gov`, and inventing a document to stand in
for a filing is exactly the failure mode the screener exists to avoid.
