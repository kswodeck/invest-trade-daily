# invest-trade-daily — working notes for Claude

This repo generates a daily, actionable trade-idea report and publishes it to a
Google Sheet. Two Claude phases run in sequence inside one GitHub Actions job.

## Non-negotiables

1. **Robinhood-tradeable only.** If it can't be traded in a Robinhood account,
   it does not go in the report. See `config/universe.md`. When unsure whether
   an instrument is offered, verify at runtime — do not guess from memory.
2. **Never fabricate a number.** Every price, date, and figure must trace to a
   fetched source. If you could not get a live price, write `null` and say so
   in `data_quality_notes` rather than estimating.
3. **Every claim carries a source URL.** No source, no recommendation.
4. **Checkpoint constantly during research.** The research phase is killed at a
   hard wall clock limit with no warning. Append to `reports/<date>/notes.md`
   after *every* finding, not at the end. Unwritten research is lost research.
5. **Capture candidates as you find them**, via
   `python scripts/add_candidate.py '<json>'`. `candidates.jsonl` is what
   synthesis builds the report from; `notes.md` is context. A run that gathers
   brilliantly and captures nothing produces nothing — this has already
   happened once.
6. **Never commit secrets.** Credentials arrive as environment variables only.

## Phase contract

| Phase | Runs | Writes | Reads |
| ----- | ---- | ------ | ----- |
| 0 Context | `scripts/build_context.py` | `reports/<date>/prior_context.md` | `state/`, past reports |
| 1 Research | `/daily-research` | `candidates.jsonl` (the deliverable), `notes.md` (context) | web, `market_data.py`, prior context |
| 2 Synthesis | `/daily-synthesis` | `reports/<date>/report.json` | the above |
| 2a Guarantee | `scripts/ensure_report.py` | a stub `report.json` if it is missing, invalid, or empty | `report.json`, `notes.md` |
| 2b Validate | `scripts/validate_report.py` | a `validation` block per idea | live prices, ATR, earnings calendar |
| 2c Red team | `/daily-redteam` | edits `report.json` | validation flags, sources |
| 2d Enforce | `scripts/validate_report.py --enforce` | demotes failures to the watchlist | `report.json` |
| 3 Publish | `scripts/publish_sheets.py` | Google Sheet, `state/open_positions.json` | `report.json` |
| 4 Refresh | `scripts/refresh_prices.py` | fresh `last_price`, `distance_to_entry_pct` | live quotes |

## How the Performance tab counts

Everything above the detail table is a live spreadsheet formula, so the rules
live in `cumulative_rows` rather than in a stored number. Four of them are
load-bearing, each because getting it wrong was shipped once:

- **Closed means closed.** The breakdown tables derived it as `ideas - open`,
  which counted every setup still waiting for its entry as a closed trade — 10
  closed trades read as 32, and every by-horizon and by-conviction average with
  them. It is now a sum of the target, stopped and expired counts.
- **Open means filled.** A row is a position only once a bar traded at its
  entry. Eleven rows written before fills were tracked sat `open` with no
  `filled_date`, and nothing demoted them, so the fill rate read 61% against a
  true 42%. `grade_position` now sends any such row back to pending.
- **Averages, never sums.** A sum of percentages grows with how many ideas were
  published rather than with how they did, and the tab used to headline one.
  The equal-weight average per idea is the portfolio figure; `compounded_return`
  is the other honest one, closed trades taken in sequence.
- **Only graded rows count.** Event contracts have no free quote source and
  futures are marked against the continuous front-month rather than the
  recommended contract, so both are flagged `no` in the Graded column and
  excluded from every figure above the table.
- **One row is one position, not one publication.** A thesis re-pitched while
  its position is still live amends that position; it does not open a second
  one. DHT was published six mornings and XLE five, and the first 57 rows were
  24 distinct calls, every re-pitched loser counted again in each average.
  `merge_report` enforces one live position per `(symbol, direction)`.

**Re-trading the same name is not deduplication.** Once a position closes —
target, stop, expiry, or never filled — the same idea published again opens its
own row, because it is a genuinely separate trade. A symbol worth trading three
times shows up three times; only concurrent duplicates of one live idea merge.

Amendments are dated, not overwritten. `levels_in_force` returns the entry,
target and stop standing on a given day, and grading reads them per bar, so a
stop moved on the 20th governs the 20th onward. Grading a whole history against
the final stop would be the same rewriting-of-the-past that made the tracker
worth distrusting. A filled position can have its exits amended but never its
entry: it was bought at a price. `scripts/dedupe_positions.py` applied this
rule backwards over the stored history, once.

Prices carry `as of` and the market session they were taken in. At 6am ET the
freshest honest equity price is the previous close — that is a closed market,
not stale data, and the two must never be conflated. `market_data.market_session()`
and `age_minutes()` are how you tell them apart.

Phases 2b–2d exist because the model is strong at research and undisciplined
about its own arithmetic. A live report once shipped eight reward-to-risk ratios
clustered at 2.04–2.33 against a 2.0 floor: targets nudged until they passed.
**Every number in `validation` is recomputed from source — never trust a figure
the model wrote about its own idea.**

The same floor was then cleared from the other side. A ratio improves just as
well by moving the stop closer, and that is free: KRE was republished three
times at an unchanged entry with the stop walked in, lifting 2.19:1 to 4.07:1
while making the trade strictly worse, and ideas shipped at 29:1 on a 0.19 ATR
stop. All ten of the first month's stop-outs had a stop tighter than 1.6 ATR.
So `check_stop_distance` now puts a floor under the stop in ATRs — 2.0 for a
swing, scaled by asset class because a basket cannot gap on one company's news
and crypto trades through the weekend — and
`check_expectancy` asks the question the ratio never answered — 3:1 at a 20%
hit rate loses money. Its baseline is not a preference: for a driftless random
walk the chance of touching the target before the stop is exactly `1/(1+R:R)`,
which is also the break-even hit rate, so every idea is implicitly claiming to
beat it and `win_probability` is where it says by how much.

Conviction is a count of the confirmations listed in `evidence`, not a feeling.
It had collapsed to a default — 39 of the first 57 ideas scored 3 — which made
the by-conviction table unreadable. `check_conviction_evidence` names the score
the evidence supports; the red team lowers it.

Phase 2 must produce a schema-valid `report.json` **even if `notes.md` is
short, truncated, or nearly empty**. A thin report that says so honestly is the
correct output; a fabricated full report is a failure.

## Scheduling

GitHub cron is UTC-only, so 6am ET is declared as two arms (`0 10` and `0 11`
UTC) and both fire every day of the year. `scripts/schedule_gate.py` decides
which one works, on two separate questions:

- **Is it still early enough?** From the wall clock in New York, never from
  which cron fired — in EDT the "EST arm" lands at a perfectly reasonable 7am,
  so the hour alone cannot tell the arms apart. The window is `6-11` ET.
- **Is today's report already published?** From the branch tip, never from the
  checked-out tree. A scheduled run is pinned to the SHA it was created at, so
  its checkout cannot contain a commit the earlier arm pushed minutes ago.

"Published" is a three-way answer from `scripts/report_state.py`, not a file
existence test. A report holding neither a recommendation nor a watchlist entry
is a **stub**: it concluded nothing, so it is retried while the window is open
and alarmed on once the window shuts. `2026-08-28` is why — synthesis was killed
mid-write, left a schema-valid `{"data_quality_notes": "Synthesis in progress.",
"recommendations": []}`, and every later check saw a file and called the day
done. `ensure_report.py` uses the same rule, so a skeleton like that is replaced
by the honest no-signal stub instead of reaching the Sheet.

Recovery is `.github/actions/report-catch-up`, which any workflow can call: it
dispatches the report when the branch has nothing usable and the window is still
open. `Report Watchdog` and `Refresh Prices` both call it, on the theory that
whichever workflow GitHub does manage to deliver can rescue the morning.
`scripts/report_runs.py` bounds it — three attempts a day, and never while one
is already running.

Consequences worth knowing before you go debugging:

- A second run per day that finishes in ~10 seconds is the gate working.
- GitHub's scheduler is best-effort and has delivered this repo's crons ten
  hours late, watchdog slots included. A day with no `reports/<date>/` is a real
  outcome, not necessarily a bug — but it should always be a red `Report
  Watchdog` run, never silence.
- Never widen the window so far that an afternoon run publishes a report framed
  as the 6am pre-open view.
- Nothing here can fix delivery itself, and everything above is damage control:
  it turns "no report" into "a late report that admits it is late". Since
  2026-08-27 delivery has run 4-11 hours late daily. A 6am report requires an
  external caller hitting `repository_dispatch` — see `docs/scheduling.md`.
- A run that starts materially after the pre-open slot is stamped by
  `scripts/note_late_run.py`, so a report researched mid-session says so instead
  of reading like the 6am view. Never remove that stamp to tidy up a report.

Logic changes here need a test in `tests/` — run with
`python -m unittest discover -s tests`.

## Texas tax deed screener

A separate twice-weekly module — Dallas, Tarrant, Johnson, Ellis. It shares the
daily report's Sheets credentials and nothing else: its own `Tax Deeds` tab, its
own workflow, its own config. Do not write it into the report pipeline.

**It does not certify title and it cannot.** County clerk lien records are not
reliably machine-readable. Every row is a candidate requiring a professional
title search before a bid, and no code, comment or output may imply otherwise —
`test_no_output_claims_clear_title` fails the build over the phrase. The
corollary is the one people get wrong: a blank Flags cell means the checks that
*ran* found nothing, never that the property is clear, which is why "Checks Run"
and "Checks Unavailable" are columns of their own.

Four rules are load-bearing:

- **Unavailable is never clean, and never a rejection either.** A check that
  could not run leaves a flag behind, and a check that never ran at all is
  treated identically to one that failed — the two are indistinguishable from
  the property's point of view. But an unknown is not a finding, so it costs the
  property its rank and never hides it. Gate 1 splits on exactly this: a
  rejection is something that was *read* and disqualifies (bid over cap,
  homestead, withdrawn, bid-to-value over cap); an unknown flags (no bid
  published, no CAD match, no appraised value, an auction listing with no date).
  The first live run is why — 718 of 758 listings were rejected for having no
  sale date, and they were struck-off properties, which have no sale date
  because there is no auction. Another 664 went for an unreachable appraisal
  district. Between them they hid all 544 real candidates.
- **So everything grading Tier C is the tool working.** Unscreened federal tax
  lien and PACE checks are *material* flags and material means Tier C. The clerk
  portals are session-gated and publish no keyless query endpoint, so until a
  working `query_url` is configured nothing will ever be Tier A. That is the
  screener reporting it screened none of the disqualifiers. Do not soften it by
  downgrading the severity.
- **Occupancy is flagged unknown on every row, always, and never inferred.**
  Because it is on every row it cannot rank rows, so it carries severity
  `universal` and the tiering ignores it — otherwise Tier A would be unreachable
  and the tiers would mean nothing. It still shows in Flags and still puts the
  drive-by on every checklist. Never remove it to tidy up a report.
- **Redemption and ownership are costed differently on purpose**, and getting it
  wrong made a good trade read as a loss. You do not buy a quiet title action on
  a property that is still redeemable, so the redemption case excludes that
  budget; and §34.21(b) makes the former owner reimburse the recording fee and
  the taxes, penalties, interest and costs the purchaser paid, so those wash and
  are excluded from *both* sides. Counting them as a cost with no matching
  reimbursement turned a 17% redemption into a headline -8%. What remains is the
  carry the statute does not repay — insurance and utilities on a vacant parcel.
  It is still conservative: §34.21(a) takes the 25% premium on the aggregate
  total, where `gate4_economics` takes it on the bid alone.

- **A ratio is not a ceiling, and the bid published is only the opening one.**
  `bid_ceilings` prices where the bidding has to stop: the equity break-even and
  the `MAX_BID_TO_VALUE` policy cap, whichever binds first. They are not the same
  number, which is why both exist — `QUIET_TITLE_BUDGET` is fixed at $3,500
  regardless of value, so on a cheap parcel it eats the whole spread while the
  ratio still reads fine. $4,000 on a $6,000 house is 0.67 bid-to-value, inside
  the 0.75 cap, against a $1,757 break-even; `opening_bid_past_walk_away` is
  material for exactly that. And below `min_profitable_bid` — unreimbursed carry
  divided by the premium, about $2,100 — a *redemption* loses money, because the
  premium is a percentage and the carry it must cover is not. Five of one live
  run's 157 priced listings sat under that floor, and the bid-to-value sort puts
  precisely those on top: the one case where the tool's own ranking points at its
  worst outcome, so it is flagged rather than derived.

- **§34.015 is checked against the sale date, not against today.** Two states the
  expiry alone cannot see: `too_late` (you hold no statement and the sale is
  nearer than the 21 working days one takes to issue — you cannot bid at this
  sale, and "renew soon" would be the wrong sentence), and `expires_before_sale`
  (current the morning you read the report, worthless the morning you bid).
  Everything with a lead time — statement, registration, deposit — is counted
  backwards in *working* days by `deadlines()`, because that is how the counties
  count and a weekend quietly eats two days of a five-day window.

- **Which sale a row is for is an axis, not a flag.** The report is headed with
  one sale date and its rows are not all on it: the first live run published 328
  candidates under "sale 2026-10-06", 18 of which were on that docket. The rest
  carried the feed's own `Available for Future Sale` — real inventory with no
  auction assigned, nothing wrong with them, answering a different question than
  the header asked. `docket_status` gives five states and the sheet a column,
  because a flag would rank rows against each other and being off the docket
  says nothing about whether a property is a good buy — it would also put 94% of
  a run in Tier C and make the tiers meaningless, the trap `occupancy_unknown`
  is `universal` to avoid. On-docket rows sort *above* the tier: a Tier A
  property six weeks out is not a better use of tomorrow morning than a Tier B
  one on tomorrow's docket. Banner and summary give both counts, and the
  deadline table only covers counties with something on this docket — telling
  someone to stage a deposit for a sale they have no property in is the
  conflation the column exists to end. `no_sale_date` narrowed to match: a
  status that *explains* the silence is a determination, so the flag is now only
  for no date and no reason given, which removed 336 false unknowns from that
  run.

- **Repeat offerings come from the snapshots, not the network.** A property
  matched across `data/tax_deeds/<date>.json` by account, else cause number, else
  county and address, and offered at two or more prior sales, is flagged
  `offered_repeatedly` (minor). It does not disqualify — plenty go unsold because
  nobody was in the room — but it is the cheapest signal available that the room
  saw something, and it belongs on the row rather than in the reader's memory.

Statute the gates encode, in one place: homestead, agricultural and mineral
property redeem for two years (25% year one, 50% year two) and are rejected at
Gate 1 for exactly that reason; everything else is 180 days at 25%. Redemption
reconstitutes junior liens the sale had eliminated, so a redeemed property does
not come back clean. A federal tax lien rejects rather than prices because IRC
§7425(d) gives the IRS 120 days from the sale to redeem, and that right survives.
Without an unexpired §34.015 written statement the officer may not deliver a
deed, so a winning bid buys nothing — the report surfaces the holder's expiry
from config and warns at 30 days, because renewal runs to 21 working days.

Every URL is in `config/tax_deeds.json`, never in logic.
`scripts/tax_deed_sources.py verify` fetches each one and fails **with the URL**
when its markers or columns are gone; a screening run verifies first. When a
county reformats, fix the config — never the parser. A county publishing only a
PDF gets a hand-exported CSV in `data/tax_deeds/manual/`, not a PDF dependency.

The first live run (2026-09-03) failed five county sources, and the three
lessons are now in code rather than folklore — see `config/tax_deeds.md`:

- **A 403 is not a format change.** The host is refusing a non-browser
  User-Agent; the page may be fine in a browser. `_explain_status` says so, and
  says not to spoof one — that is the same line the robots.txt rule draws.
- **A page with no HTML table cannot be fixed with `column_map`.** It is a
  JavaScript app, and telling the operator to edit header patterns for a source
  that has no headers is worse than saying nothing. `rows_from_json` exists so
  the fix — point at the endpoint the page calls for itself — stays a config
  change.
- **A dead URL is worse than a null.** A plausible guess that does not resolve
  reports a network error every run, which reads as transient and is not. Nulled
  sources report "not configured" and leave the check `unavailable`, which is a
  flag. A null never becomes a clean screen.

Four of those five failures are now worked around automatically, each as an
ordered fallback that only runs after the plain path failed: a 403 is retried
with a `Mozilla/5.0 (compatible; invest-trade-daily-taxdeeds/1.0; +mailto:...)`
UA, because a UA filter is not a policy — every UA in the list still names the
project and carries a contact, and robots.txt is checked separately, once,
against our own name, where a disallow ends it. A page with no table falls
through to `discover_json_records`, which decodes the JSON the page ships with
itself and infers the field map from the source's existing `column_map` (camel
humps split, so `minimumBid` matches "minimum bid"); an array qualifies only if
it carries an opening bid and an identifier, the same bar the table parser
applies. Sources take `fallback_urls`. And `resolve_flood_url` follows the NFHL
layer by name so a re-indexed service self-heals. What is deliberately *not*
worked around is robots.txt: the clerk portals disallow crawling, those checks
stay unavailable, and `respect_robots_txt: false` is not a supported fix.

Two blockers had feasible workarounds and one did not. Markers and the county
filter belong to a URL, not to a source — conflating them cost Johnson every run,
because its fallback is the aggregate that already works for three other
counties and it was rejected for lacking the word "constable". A `fallback_urls`
entry may be an object carrying its own `required_markers` and `county_filter`.
And each lien source takes a list of official-records hosts per county, tried in
order and robots-checked individually: a disallow is that host's policy and ends
the matter there, but it is not the county's, and a county publishes the same
index on more than one system. `PACKET_TIERS` defaults to `A,B,C` because `A,B`
wrote no packets at all while every property carries an unscreened lien check —
a default that produces nothing is broken, not conservative.

Exit codes carry meaning: 0 clean, 1 published with a broken source, 2 every
county list failed so nothing was screened and the Sheet was left alone,
anything else a crash. 1 and 2 both write the snapshot and the step summary
before returning — the first live failure exited before writing anything, so the
only record of which URL broke was raw CI log. A verifier whose own probe is
wrong is worse than none, which is why `_verify_enrichment` exercises the call
the screener actually makes: probing the Census geocoder with no address got it
a 400 and reported a working source as broken.

Manners are enforced in code, not documented as intentions: robots.txt is
honoured (unreadable means do not fetch), one request per second per host, and
without `TAX_DEED_CONTACT_EMAIL` the module refuses to fetch rather than go
anonymous.

The tab is rewritten in full every run — stale listings are dangerous, since a
property pulled on Friday is still a live-looking row on Monday. Each run's
snapshot goes to `data/tax_deeds/<date>.json` including the rejects and the
reason for each.

Logic changes here need a test in `tests/` — the same suite as everything else.

## Data access

Use `scripts/market_data.py` before reaching for raw web scraping — it is
faster, more reliable, and already handles fallbacks:

```bash
python scripts/market_data.py quote NVDA SPY          # equities/ETFs
python scripts/market_data.py crypto bitcoin ethereum # crypto
python scripts/market_data.py history NVDA --days 90  # OHLCV
python scripts/market_data.py macro                   # rates, VIX, DXY, FRED
python scripts/market_data.py events "CPI"            # Kalshi event contracts
python scripts/market_data.py filings NVDA            # recent SEC filings
python scripts/market_data.py earnings --days 14      # upcoming earnings
```

Every subcommand prints JSON to stdout and never raises on a failed source — it
returns `{"ok": false, "error": ...}` for that source and moves on. Check `ok`.

## Style

- Python: standard library first, `requests` for HTTP, no heavy frameworks.
  Type-hint public functions. Keep scripts runnable standalone.
- Markdown research notes: terse, factual, timestamped. Bullets over prose.
- Never rewrite history in `reports/` — past reports are the performance record.
