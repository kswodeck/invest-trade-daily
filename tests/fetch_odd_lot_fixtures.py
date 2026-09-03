#!/usr/bin/env python3
"""Download real archived odd-lot tender filings into tests/fixtures/odd_lot/real/.

    python tests/fetch_odd_lot_fixtures.py
    python tests/fetch_odd_lot_fixtures.py --days 365 --limit 8 --forms "SC TO-I" "SC TO-I/A"

`tests/test_odd_lot_parser.py` asserts against every document this leaves
behind, and skips that class when the directory is empty — `tests.yml` runs on
a bare runner with no network, and the parser's logic is covered by the pattern
fixtures either way.

Nothing here is hardcoded to a particular accession number. The filings are
found by the same EFTS query the screener runs, so a fixture set is whatever
the SEC actually held in the window rather than a list transcribed from memory,
and `manifest.json` records where each one came from.

Needs `SEC_USER_AGENT` set, or `sec.user_agent` in config/odd_lot.json, and a
network route to sec.gov.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import odd_lot  # noqa: E402

FIXTURES = REPO / "tests" / "fixtures" / "odd_lot" / "real"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=120, help="how far back to search")
    ap.add_argument("--limit", type=int, default=5, help="how many documents to keep")
    ap.add_argument("--forms", nargs="+", default=None, help="override the form list")
    args = ap.parse_args(argv)

    config = odd_lot.load_config()
    config["discovery"]["lookback_days"] = args.days
    if args.forms:
        config["discovery"]["forms"] = args.forms

    client = odd_lot.SecClient(config)
    hits = odd_lot.search_filings(client, config, today=date.today())
    print(f"EFTS returned {len(hits)} filing(s) over the trailing {args.days} days.")

    FIXTURES.mkdir(parents=True, exist_ok=True)
    manifest, kept = [], 0
    for hit in hits:
        if kept >= args.limit:
            break
        try:
            terms, document, _ = odd_lot.read_offer_documents(hit, client)
        except Exception as exc:  # noqa: BLE001 - one bad filing is not fatal
            print(f"  skip {hit['accession']}: {type(exc).__name__}: {exc}")
            continue

        # Only keep documents that actually carry the language under test. A
        # filing's other exhibits match "odd lot" without stating the terms.
        if terms is None or not (terms.has_threshold and terms.has_proration_preference):
            print(f"  skip {hit['accession']}: no exhibit carried the odd-lot preference")
            continue

        raw = client.get(document["url"],
                         cache_key=f"{hit['accession']}_{document['name']}")
        name = f"{hit['accession'].replace('-', '')}_{hit['form'].replace('/', '')}.html"
        (FIXTURES / name).write_text(raw, encoding="utf-8")
        manifest.append({
            "file": name,
            "accession": hit["accession"],
            "cik": hit["cik"],
            "company": hit["company"],
            "ticker": hit["ticker"],
            "form": hit["form"],
            "filed": hit["filed"],
            "url": document["url"],
            "document": document["name"],
            "expiration_date": terms.expiration_date,
            "offer_price": terms.offer_price,
            "fetched_on": date.today().isoformat(),
        })
        kept += 1
        print(f"  kept {name} — {hit['company']} {hit['form']} {hit['filed']}")

    (FIXTURES / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"\nWrote {kept} fixture(s) and manifest.json to "
          f"{FIXTURES.relative_to(REPO)}.")
    if not kept:
        print("No filing in the window carried odd-lot language in its primary "
              "document. Widen --days and try again.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
