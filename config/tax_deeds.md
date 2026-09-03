# Texas tax deed screener — configuration

Twice-weekly module, separate from the daily trade report. It ingests the tax
sale lists Dallas, Tarrant, Johnson and Ellis counties publish, applies
disqualifying filters, and produces a shortlist with a due-diligence packet per
surviving property.

## It does not certify title, and it cannot

County clerk lien records are not reliably machine-readable. Every output row is
a **candidate** requiring a professional title search before any bid. That
sentence is in row 1 of the sheet, at the top of every packet, in the run
summary, and in the snapshot JSON. `tests/test_tax_deeds.py` fails the build if
any generated output claims clear, clean, marketable or insurable title.

The corollary matters more than the disclaimer: **a blank Flags column means the
checks that ran found nothing, never that the property is clear.** Which checks
actually ran is a column of its own, next to the ones that did not.

## Files

| Path | What it is |
| --- | --- |
| `config/tax_deeds.json` | every URL, threshold and the §34.015 statement |
| `scripts/tax_deeds.py` | gates, redemption law, economics, tiering, rendering |
| `scripts/tax_deed_sources.py` | fetching, robots, rate limit, parsers, verification |
| `scripts/tax_deed_screen.py` | the run: ingest → enrich → screen → publish |
| `data/tax_deeds/<date>.json` | the run snapshot, every listing including rejects |
| `data/tax_deeds/manual/<source>.csv` | operator drop-box for PDF-only counties |
| `reports/tax_deeds/<sale>/<county>_<acct>.md` | packet per Tier A/B candidate |
| Google Sheet tab `Tax Deeds` | the shortlist, rewritten in full each run |

## Running it

```bash
python scripts/tax_deed_sources.py verify        # fetch every source, check structure
python scripts/tax_deed_screen.py --dry-run      # full run, Sheet untouched
python scripts/tax_deed_screen.py --sale-date 2026-10-06 --county Dallas
python scripts/tax_deeds.py thresholds           # what the gates are set to
python scripts/tax_deeds.py statement            # §34.015 status per county
```

Credentials are the daily report's: `GCP_SERVICE_ACCOUNT_JSON` and
`GOOGLE_SHEET_ID`. It creates its own tab and never writes to an existing one.
`TAX_DEED_CONTACT_EMAIL` is additionally required — see Manners below.

## Thresholds

Resolved **environment → config file → built-in default**, so a workflow can
widen a gate for one run without a commit.

| Knob | Default | What it does |
| --- | --- | --- |
| `MAX_OPENING_BID` | 20000 | Gate 1 rejects a larger minimum bid |
| `MAX_BID_TO_VALUE` | 0.60 | Gate 1 rejects above it; also the recommended max bid |
| `TIER_A_BID_TO_VALUE` | 0.35 | Tier A ceiling |
| `QUIET_TITLE_BUDGET` | 3500 | in the ownership case only |
| `HOLDING_MONTHS` | 7 | 180-day redemption plus a month |
| `REJECT_FLOOD_ZONE` | true | false demotes a flood hit to a material flag |
| `EFFECTIVE_TAX_RATE` | 0.023 | DFW ad valorem, for holding and post-judgment taxes |
| `MONTHLY_CARRY` | 75 | insurance and utilities on a vacant parcel |
| `POST_JUDGMENT_YEARS` | 1.0 | years of taxes assumed accrued since judgment |
| `TEARDOWN_IMPROVEMENT_VALUE` | 5000 | below it, a parcel with a structure is flagged |
| `STATEMENT_WARN_DAYS` | 30 | §34.015 expiry warning |
| `TIER_B_MAX_MINOR_FLAGS` | 2 | more than this drops to Tier C |
| `PACKET_TIERS` | `A,B` | which tiers get a due-diligence packet |

## §34.015 — fill this in

`bidder_statement.counties.<County>.expires` is the expiry of the written
statement *you hold* from that county's assessor-collector. Null means you hold
none, and the report says so on the sheet, in the summary and in every packet.

This is the one blocker that is entirely yours to fix and entirely invisible
until the deed does not arrive: without an unexpired statement the officer **may
not deliver a deed**, so a winning bid buys nothing. Notarized Form 50-307,
`comptroller.texas.gov/forms/50-307.pdf`. Processing runs to a minimum of 21
working days in some counties, which is why the warning fires at 30 days.

An individual may not bid or purchase in the name of another individual
(§34.011). Knowing violation is a Class B misdemeanor.

## Sources

Every URL is here; none is in the logic, and `test_no_url_is_hardcoded_in_the_
screening_logic` keeps it that way. Each source declares:

- `format` — `html_table`, `csv`, or `pdf`
- `required_markers` — strings that must still be on the page
- `column_map` — canonical field → header patterns, **in precedence order**
  (`minimum_opening_bid` lists "minimum bid" before "judgment" because a
  judgment amount is only a last-resort stand-in for an opening bid)
- `county_filter` — for aggregators that carry several counties on one page
- `sale_type` — `auction` or `struck_off`

**Every source ships marked `"status": "unverified"`.** They were assembled from
the county and law-firm pages that publish these lists, not confirmed against a
live fetch — the environment this was built in cannot reach county hosts. Run
`python scripts/tax_deed_sources.py verify` before the first real run and expect
to fix URLs and column names. That is the intended workflow, not a defect: county
sites change format without notice, and the fix is always config, never the
parser.

Verification fetches each source and fails **with the URL** when its markers or
columns are gone. A screening run verifies first, and exits non-zero if any
source broke — because a silently empty tab reads exactly like "no sales this
month", which is the dangerous failure.

### What the first live run established (2026-09-03)

Verification did its job and named five broken county sources. None of them was
a parser bug, and the causes were three different things:

| Source | Result | What it means |
| --- | --- | --- |
| `dallas_auction` | HTTP 403 | the host refuses a non-browser User-Agent |
| `johnson_auction` | HTTP 403 | same |
| `dallas_struck_off`, `tarrant_auction`, `ellis_auction` | 200, no HTML table | `taxsales.lgbs.com` is a JavaScript app |
| `ellis.tx.publicsearch.us` | DNS NXDOMAIN | Ellis is not on that platform; the URL was invented |
| PACE registry | HTTP 404 | the completed-projects path is wrong |
| FEMA NFHL layer 28 | HTTP 404 | wrong layer index |
| Census geocoder | HTTP 400 | **verify's own bug** — it probed with no address |

Three lessons are now enforced in code rather than left as folklore.

**A 403 is not a format change.** The page may be perfectly fine in a browser;
the host simply refuses non-browser clients. `_explain_status` says so, and says
explicitly not to spoof a browser to get around it — that is the same line the
robots.txt rule draws. The ways forward are a different published location for
the list, or the manual CSV drop.

**A page with no HTML table cannot be fixed with `column_map`.** It is a
JavaScript app that renders the list client-side, and no header pattern will
ever match because there are no headers in the HTML. Open the page with the
network tab, find the JSON endpoint it calls for itself, and set
`"format": "json"` with `records_path` and `field_map` on that source. That is a
config change, which is the point. `rows_from_json` walks dotted paths, so
`addr.line1` works.

**A dead URL is worse than a null.** `ellis.tx.publicsearch.us` was a plausible
guess that does not resolve, and it reported as a network error every run —
noise that looks transient and is not. Those URLs are now `null`, which reports
"no source configured" and leaves the check `unavailable`, which is a flag. A
null never becomes a clean screen; `test_an_unconfigured_source_still_costs_the_
property_its_tier` holds that line.

The three CADs that matter — DCAD, TAD, Johnson CAD — verified clean, which is
the part of the pipeline that values a property.

### What it now works around by itself

Four of the five live failures are handled without anyone editing config. They
are ordered attempts, not guesses: each only runs after the plain path failed.

**A refused User-Agent.** Two counties answered 403 to the plain UA. robots.txt
is a policy statement and is still honoured absolutely — checked once, against
this screener's own name, and a disallow ends it. A 403 on a UA string is a
filter, not a policy, so a refusal is retried with
`Mozilla/5.0 (compatible; invest-trade-daily-taxdeeds/1.0; +mailto:you@example)`
— the form well-behaved crawlers have used for decades. **Every UA in the list
names this project and carries an address to complain to**; that is the line,
and a UA that impersonates a browser without identifying itself does not go in
`user_agent_fallbacks`.

**A JavaScript-rendered list.** `taxsales.lgbs.com` serves three counties and
has no HTML table at any URL. But a client-rendered page still ships with its
data — a `__NEXT_DATA__` blob, a hydration assignment, a JSON-LD block — so when
the table parser finds nothing, `discover_json_records` decodes every inline
JSON value, walks it for arrays of objects, and scores each against the source's
**existing `column_map`**. `minimumBid` and `"minimum bid"` reduce to the same
words once the camel humps are split, so no new configuration is needed; nested
keys map too, which is how `address.line1` becomes the address. An array only
qualifies if it carries an opening bid and something to identify a property by
— the same bar the table parser applies, so a discovered list is never
worse-specified than a parsed one. Navigation menus and config blobs fail it.

When discovery works, `verify` says so and prints the exact
`{"format": "json", "records_path": ..., "field_map": ...}` to paste in. Pin it
when you see it: a heuristic that works today should become configuration.

**A list the page fetches rather than ships.** `taxsales.lgbs.com` has no table
*and* no records in its HTML — it calls an API after load. That endpoint is not
a secret: it is written in the page's own scripts. So when embedded discovery
finds nothing, `discover_api_records` collects the API-shaped URLs the page and
its same-origin bundles reference, GETs the most likely ones, and scores the
replies the same way. Bounded on purpose — only URLs the site itself names, only
its own host, at most `MAX_API_PROBES` of them, at the same one request per
second — and it never guesses at paths the site did not mention. Set
`"probe_api": false` on a source to switch it off.

**A statewide feed.** These endpoints serve every county the firm covers, and
paging the whole state at one request per second is not a plan — the first
success walked 40 pages, fetched 400 rows and kept none of them. So when the
first page holds none of this county's rows, `_narrow_to_county` re-requests it
filtered, using the field name the API itself uses as the query key before
falling back to a short list of guesses. A parameter the API *ignores* returns
the unfiltered list, which would look like success while changing nothing, so a
narrowing is only accepted when nearly every row that comes back is actually
this county's. Pin it with `query_params` on the source once you see which key
worked, and the probing is skipped.

The value it queries with is learned, not guessed. The live feed turned out to
be **nationwide** — Galveston, Maverick, and Philadelphia County among the first
400 rows — and it stores names as `TARRANT COUNTY`, uppercase with a suffix. A
query for `Tarrant` finds nothing. So `county_value_variants` reads the shape off
the records the API just returned and asks in that shape first, falling back to
the usual spellings. Hardcoding "uppercase plus COUNTY" would have been a guess
about one vendor; reading it is not.

**A moved list.** Every source takes `fallback_urls`, tried in order after the
primary fails. They are strictly additive — never fetched when the primary
works — and `verify` reports which one got used.

**A re-indexed FEMA layer.** Layer 28 was wrong, and an operator cannot guess
the right index. With `flood.autodetect_layer` on, the screener asks the
MapServer for its layer list and takes the flood-hazard-zone layer by name,
resolved once per run and cached.

**An unreachable robots.txt.** `hazards.fema.gov` and `esearch.elliscad.com`
reset the connection on `/robots.txt`, and the original rule — anything
unreadable means do not fetch — turned that into a standing ban on two sources
that plainly permit access. A connection reset is not a statement of policy; it
is no signal at all. So a network-level failure is retried once and then treated
as "no rules", with the reason recorded. An HTTP 5xx still refuses, because
there the server is speaking and what it says is that it is broken.

What is **not** worked around, because it should not be: the four
`publicsearch.us` clerk portals disallow crawling in robots.txt. Those checks
stay `unavailable`, which is a material flag, which means Tier C. Setting
`respect_robots_txt: false` to get around that is not a supported fix.

### Exit codes

| Code | Meaning |
| --- | --- |
| 0 | clean run |
| 1 | published, but at least one source failed verification |
| 2 | every county list failed — nothing screened, Sheet untouched |
| other | the screener crashed; that is a bug |

1 and 2 are outcomes, not crashes, and both still write the snapshot and the
step summary before returning. The first live failure exited before writing
anything, so the only record of which URL broke was raw CI log — that is fixed,
and the workflow commits the snapshot on those codes precisely so the diagnosis
survives the run.

### Struck-off lists

Properties that did not sell at auction, purchasable over the counter at the
original minimum bid with no auction to attend. Captured as `sale_type:
struck_off` and shown in the Sale Type column. Dallas has one configured; add
the others as you find where each county publishes them.

### PDF-only counties

Several constable offices publish only a PDF and this repo carries no PDF
dependency. Rather than pretend to parse one, such a source errors with the path
to drop a hand-exported CSV: `data/tax_deeds/manual/<source_id>.csv`, matched by
the same `column_map`. A manual file, when present, wins over the live fetch.

## Manners

Non-negotiable, and enforced in code:

- **robots.txt is honoured.** A disallowed path is not fetched at all, and the
  check that needed it reports `unavailable`. A missing robots.txt allows; one
  that returns a server error does not, because the rules exist and we could not
  read them.
- **One request per second per host**, globally.
- **The User-Agent names the project and carries a contact email.** Without
  `TAX_DEED_CONTACT_EMAIL` (or `contact_email` here) the module refuses to make
  a request rather than fetch anonymously.

## The gates

**Gate 1 — hard disqualifiers, rejected with the reason logged.** Opening bid
over the cap; homestead or agricultural exemption on the CAD record; mineral-only
interest; mobile home without the land; sale date passed or listing withdrawn; no
CAD match; bid-to-value over the cap. The exemption classes go because §34.21(a)
gives them a two-year redemption, and you cannot sell, re-tenant or remodel
through it.

**Gate 2 — liens.** A property passes only if every check returned clean, **or
returned unavailable and left a flag behind.** Federal tax lien or PACE hit
rejects outright. HOA hits flag. A check that never ran is treated identically to
one that failed, because the two are indistinguishable from the property's point
of view.

**Gate 3 — physical.** FEMA flood zone; road frontage; municipal minimum lot
size; teardown-level improvement value. Occupancy is flagged unknown on every
row and never inferred — see below.

**Gate 4 — economics.** Both outcomes, because both are acceptable: redeemed
pays 25% of the bid over ≤180 days; not redeemed leaves you the equity against
CAD value net of estimated costs.

The two are costed differently on purpose. You do not buy a quiet title action on
a property that is still redeemable, so the redemption case excludes that budget.
And §34.21(b) makes the former owner reimburse the deed recording fee and the
taxes, penalties, interest and costs you paid — so those wash, and are excluded
from **both** sides of the redemption case. Counting them as a cost with no
matching reimbursement is what turned a 17% redemption into a headline -8% loss.
What is left is the carry the statute does not repay: insurance and utilities
over `HOLDING_MONTHS`.

It is still conservative. §34.21(a) computes the 25% premium on the *aggregate
total* — the bid plus the recording fee plus the taxes reimbursed — where this
takes it on the bid alone, as the spec does.

**Gate 5 — tiering.** A: no flags, bid-to-value < 0.35. B: no material flags, one
or two minor, bid-to-value < 0.60. C: passes the hard gates but carries material
flags — informational only.

## Two consequences worth knowing before you go debugging

**Everything grading Tier C is the tool working.** Unavailable federal-tax-lien
and PACE checks are *material* flags, and material flags mean Tier C. The clerk
portals are session-gated and publish no keyless query endpoint, so unless you
configure a `query_url` that actually works, every property carries two material
flags and nothing is ever Tier A or B. That is the screener reporting it screened
none of the disqualifiers — not a bug, and not something to soften by
downgrading the severity.

The consequence is that the default `PACKET_TIERS=A,B` writes no packets at all
in that state, and the run says so rather than leaving you to notice an empty
directory. Set `PACKET_TIERS=A,B,C` to get one per candidate and read the flag
list yourself — that is the honest way to work an unscreened shortlist, and it
does not require pretending a property cleared a check that never ran.

**Occupancy is flagged on every single row.** It cannot be determined remotely
and is never inferred. Because it is on every row it cannot rank rows, so it
carries severity `universal` and the tiering ignores it — otherwise Tier A would
be unreachable and the tiers would mean nothing. It still shows in the Flags
column and still puts the drive-by on every checklist. Do not remove it to tidy
up a report; it is the reason the drive-by is there.

## Redemption, in one place

| Property | Period | Premium |
| --- | --- | --- |
| Homestead, agricultural, mineral | 2 years | 25% year one, 50% year two |
| Everything else | 180 days | 25% |

The former owner may not occupy, possess, or receive rents during redemption
(§34.21(h)); the purchaser may evict, subject to servicemember protections and
bona fide leases. **Redemption reconstitutes junior liens the sale had otherwise
eliminated — a redeemed property does not come back clean.** And where a federal
tax lien was of record, IRC §7425(d) / 28 U.S.C. §2410 give the IRS 120 days from
the sale to redeem, or the state period, whichever is longer. That right survives
the sale, which is why a federal tax lien hit rejects rather than prices.

## Non-goals

No bidding, no auction account automation, no payment handling. Nothing in the
code, comments or output may claim clear title.

Logic changes here need a test in `tests/` — run with
`python -m unittest discover -s tests`.
