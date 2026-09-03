# invest-trade-daily

An automated daily trade-idea report. Every morning at **6:00 AM ET**, a GitHub
Actions workflow runs Claude Opus in deep-research mode against news, price
action, filings, and macro data, then publishes ranked, actionable trade ideas
to a Google Sheet.

> **Not financial advice.** This repository produces algorithmically generated
> research for personal use. Every idea it emits is a hypothesis, not a
> recommendation. See [Disclaimer](#disclaimer).

## How it works

```
06:00 ET (cron, DST-aware)
   │
   ├─ Phase 0 — CONTEXT
   │    Summarizes open positions, hit rate by category, and recently
   │    repeated symbols so the research phase has memory.
   │
   ├─ Phase 1 — RESEARCH  (Opus, hard 60 min cap)
   │    Scans news, filings, macro, price action, event markets.
   │    Appends every finding to reports/<date>/notes.md as it goes,
   │    so a mid-thought timeout still leaves usable material.
   │
   ├─ Phase 2 — SYNTHESIS  (Opus, ~15 min, always runs)
   │    Reads whatever candidates exist and emits strict-schema report.json.
   │
   ├─ Phase 2b — VALIDATE  (code, not a model)
   │    Recomputes R:R, checks direction consistency, compares entries to
   │    live prices, verifies earnings dates against the real calendar,
   │    sizes targets and stops in ATR, measures expectancy against the
   │    random-walk baseline, checks conviction against the evidence
   │    listed for it, and resolves every cited URL.
   │
   ├─ Phase 2c — RED TEAM  (Opus, ~12 min)
   │    A separate pass whose only job is to attack the ideas and kill
   │    the weak ones, starting from the validation flags.
   │
   ├─ Phase 2d — ENFORCE
   │    Anything still failing a hard check moves to the watchlist with
   │    its reason attached, rather than publishing as a live idea.
   │
   ├─ Phase 3 — PUBLISH
   │    Computes portfolio exposure, grades yesterday's open picks,
   │    then writes:
   │      • "Today" tab      — this morning's ranked ideas
   │      • "<date>" tab     — dated archive of the same
   │      • "Performance"    — running scorecard of every past call
   │
   ├─ Phase 4 — COMMIT
   │    reports/<date>/ lands in git as the durable audit trail.
   │
   └─ 09:35 & 12:30 ET — REFRESH PRICES  (separate workflow)
        Re-quotes every idea and updates the Sheet's Last price,
        As-of stamp and Dist-to-Entry. Prices only — the morning's
        entries, targets, stops and theses are never touched.
```

### Why prices are refreshed separately

The report is researched at 6am ET, three and a half hours before the US open.
**No data provider changes that** — at 6am the freshest honest equity price is
the previous close, and a report generated on a Sunday will legitimately carry
Friday's 4pm prices. Every quote therefore records its `as of` timestamp and the
session it was taken in, so a *closed market* is never mistaken for *stale data*.

The refresh runs are what make the sheet current at the moment you would place
an order.

The 60-minute cap is enforced by GitHub at the step level, not by asking Claude
to watch a clock. When the research step is killed, `continue-on-error` lets the
job proceed to synthesis anyway — so **the report always ships**, it just ships
with less research behind it. The `truncated` flag in `report.json` records
whether that happened.

### When it breaks

If synthesis produces nothing usable, `ensure_report.py` publishes a stub that
says the pipeline failed — explicitly, so a blank sheet is never mistaken for
"no good trades today" — and then **fails the workflow on purpose**. GitHub only
emails you about red runs, so a green run publishing zero ideas would be the one
morning you'd hear nothing about. The Sheet write and the commit both happen
before that failure, so you keep the record either way.

## Odd-lot tender screener

A second, independent daily job. It has nothing to do with the trade-idea
pipeline above — no model runs, no research phase, no conviction score — and it
publishes to its own single tab on the same Sheet.

```
05:37 ET  ── 30 minutes ahead of the daily report ──┐
18:30 ET  ── after EDGAR's 17:30 filing cutoff ─────┤
                                                    │
   ├─ DISCOVER   EDGAR full-text search over a trailing 75 days:
   │             six phrasings across eight Schedule TO forms,
   │             paginated. Hits are grouped into filings by
   │             accession, keeping every matching exhibit.
   │
   ├─ RE-SCORE   Every open offer, not just the new ones. Prices
   │             move; an offer rejected on Monday for a 0.9%
   │             spread is a different trade on Thursday.
   │
   ├─ GATE 1-4   Read the filing's exhibits, run the economics,
   │             flag the risks, assign a tier. Every rejection
   │             keeps its reason, and the report tallies them.
   │
   ├─ PUBLISH    The "Odd Lot" tab, overwritten in place. Expired
   │             offers leave it.
   │
   └─ COMMIT     state/odd_lot_universe.json and
                 reports/<date>/odd_lot.md are the history.
```

### What an odd-lot tender is

Some issuer tender offers give preferential treatment to small holders: if you
own **fewer than 100 shares**, your shares are accepted for payment **before**
any proration of everyone else's. When an offer is oversubscribed, a 1,000-share
holder might get 300 shares taken; a 99-share holder gets all 99. The trade is
to buy 99 shares below the offer price, tender them, and collect the spread
without standing in the proration queue.

The rules are terms of each offer, not a market convention, and every one of
them has bitten somebody:

- **Fewer than 100 shares**, owned beneficially or of record. 100 is not an odd
  lot; 99 is.
- **You must tender every share you own.** A partial tender forfeits the
  preference entirely.
- **Ownership aggregates across all accounts by SSN.** You cannot split 150
  shares across two brokers and claim two odd lots.
- **The issuer can remove the preference mid-offer.** Frontera Energy did
  exactly that by amendment in September 2024. This is why `SC TO-I/A`
  amendments are read rather than skipped, and why an amendment that removes it
  is a hard rejection.
- **The preference can be conditioned.** An ITEX `SC TO-I` voided it if the
  purchase would leave the stock held of record by fewer than 300 persons — a
  preference that evaporates precisely when it is used. Also a hard rejection.
- **In a Dutch auction, shares are accepted at or below the final price.** The
  low end of the range is the only price a tender is guaranteed to clear at, so
  the low end is what the spread is computed from.

**This is research output. It places no orders and talks to no broker.**

### Finding the offers in the first place

A tender offer is a Schedule TO whose substance lives in its exhibits — the
Offer to Purchase, the Letter of Transmittal, the Notice of Guaranteed Delivery,
the letters to brokers, the summary advertisement. Every one of them says "odd
lot", so full-text search returns them all, as separate hits sharing one
accession number.

**The filing is read, not one of its exhibits.** Keeping a single hit per
accession means judging the offer on whichever document the search happened to
rank first, and when that is the Letter of Transmittal — an Odd Lots checkbox
and nothing else — the filing is rejected for "no acceptance-before-proration
language" while the Offer to Purchase sits beside it saying exactly that. That
is why the first live run rejected all four of its filings. Exhibits are now
read in turn until one carries the complete terms, and the entry records which
one supplied them.

Three other things bound what discovery can see, all of them in
`config/odd_lot.json`:

- **`lookback_days`, 75.** A tender offer runs 20–40 business days. A window
  shorter than one offer's lifetime can only see what was filed since the last
  successful run, so a few quiet days lose everything filed in them permanently.
  Seventy-five days makes discovery self-healing: an offer missed on Monday is
  found on Friday, still open.
- **Pagination.** The endpoint returns ten hits per page. Reading only the
  first capped discovery at ten *documents* per query — and a single filing can
  account for five of them.
- **Date slices, and per-query isolation.** The window is queried in 25-day
  slices, and a query that fails costs that slice rather than the pass. EFTS
  returns 500s: one on a 75-day `SC TO-T` query took down all forty-eight
  queries of the first wide run. A 5xx is retried (unlike a 403 or 429, where
  retrying is what extends the block); discovery only gives up when *every*
  query failed, which is the difference between "EDGAR is having a moment" and
  "the endpoint is gone". Partial failures are named in the report, because a
  thinner sweep should not read like a quiet day.
- **Three phrasings, eight forms.** `"odd lot"`, `"odd lots"` and `"odd-lot"`,
  across `SC TO-I`, `SC TO-T`, `SC 13E4F`, `SC 13E3` and each one's `/A`. One
  query per pair rather than one big OR, because EFTS scores and truncates per
  query and a busy form would crowd out a quiet one. Phrases like
  `"odd lot holder"` are deliberately *not* listed: a phrase search for
  `"odd lot"` already matches every document containing them, so they doubled
  the query count and found nothing new.

A filing whose filer has no ticker on file — common, since tender offers are
often filed by a parent or an acquirer — is resolved through the SEC's own
`company_tickers.json`, cached daily. Gate 2 rejects an offer it cannot price,
and three of the first live run's four filings arrived without a ticker.

### Where the universe went

Every report ends with a funnel: how many queries ran over what window, how many
document hits and distinct filings came back, and a tally of which gate turned
each rejected offer away. **A screener that finds nothing looks exactly like one
that is broken**, and this is the only thing that tells them apart — the first
live run rejected its entire universe at Gate 1 and read as a quiet day.

The tally is keyed on the rejection messages themselves, and anything it cannot
classify is counted and flagged rather than dropped, so a reworded gate shows up
as drift instead of silently vanishing from the funnel.

### The gates, and why each threshold is where it is

Everything below lives in [`config/odd_lot.json`](config/odd_lot.json). Nothing
in the code carries a default that overrides it.

**Gate 1 — the document.** Any failure rejects, with the reason recorded.

| Check | Why |
| --- | --- |
| Both a "fewer than 100 shares" threshold **and** acceptance-before-proration language, in the same passage | Either half alone is a different document. A threshold with no promise is an offer that merely *defines* an odd lot; proration language with no threshold is the ordinary pro-rata sentence in every oversubscribed tender. |
| Cash offer, not an exchange offer | An exchange offer pays in stock. There is no spread to capture, only a ratio. Reported as three answers — cash, exchange, or *unstated* — because "pays in stock" and "we could not find what it pays" are different findings and were being reported as the first. |
| Common equity, not debt or preferred | Debt tenders use the identical odd-lot phrasing for *notes*. 99 notes is a $99,000 position, not a $1,000 one. Closed-end funds and BDCs — a large share of the `SC TO-I` population — call their equity *shares of beneficial interest*, and count. |
| Currently open, not expired or terminated | Decided from the expiration date read out of the document. |
| No amendment removing the preference | The Frontera pattern. |
| No record-holder condition on the preference | The ITEX pattern. Read inside the odd-lot passage only — a standalone "fewer than 300 holders of record" is deregistration boilerplate that nearly every small-cap tender carries. |
| Not restricted to accredited investors, QIBs, or non-US persons | You cannot tender into an offer you are not eligible for. |

**Gate 2 — the economics.** Any failure rejects.

| Threshold | Default | Why this number |
| --- | --- | --- |
| `min_spread_pct` | 1.5% | Below this the spread is inside execution noise: the bid-ask on a thin small cap, plus the commission-free but not price-free reality of a market order, eats it. |
| `max_capital` | $5,000 | 99 shares of a $50 stock is $4,950. The cap is what keeps this a small mechanical trade rather than a concentrated position in a company you have not researched. |
| `min_days_to_expiry` | 4 days | Broker tender deadlines run **ahead** of the offer's own deadline, often by a full business day, and the instruction has to be entered and processed. Four days is the smallest window in which the trade is actually placeable. |
| `min_avg_volume_30d` | 50,000 shares | Exit liquidity. If the offer is amended, terminated, or you miss the tender deadline, you own 99 shares outright and need somewhere to sell them. |
| `min_market_price` | $1.00 | A hard floor with no exceptions. Sub-dollar stocks carry delisting mechanics and spreads measured in percent, and a 3% spread on a $0.40 stock is one tick. |

**Gate 3 — risk flags.** These never reject. They cost the offer its tier and
are printed alongside it:

financing condition · minimum-tender condition · litigation or regulatory
condition · **market price above offer price** · foreign private issuer
(withholding-tax complexity) · going-concern language.

*Market price above offer price* earns its prominence: it means the market
disagrees with the offer outright — expecting a raised bid, or pricing in a
contested deal — and the spread it produces is negative.

Flags are checked for negation. "The Offer is **not** conditioned on the receipt
of financing" is the sentence a clean offer uses to say it has no financing
condition, and reading it as one would cost that offer its Tier A on the
strength of a promise that it has none.

**Gate 4 — tiering.**

- **Tier A** — spread ≥3%, ≥7 days to expiry, zero flags.
- **Tier B** — spread ≥1.5%, with at most one minor flag. A tighter timeline
  and a thinner spread both live here, in any combination.
- **Tier C** — a material flag, or more than one flag of any kind.
  Informational, printed so the day's work is visible, not traded.
  `market_price_above_offer` and `going_concern` are never minor and send an
  offer to C on their own, however good the numbers look.

The spread is a **qualifier for Tier B, not a discriminator within it**. Any
spread clearing the Gate 2 floor is a Tier B spread — a 1.8% spread is a smaller
version of the same trade, not evidence against it, and it does not stack with a
flag to force a demotion. What separates B from C is whether something is wrong
with the offer, which is what the flags are for.

### How you hear about a hit

Most days the screener finds nothing, so nobody opens the tab. A Tier A or B
offer has a deadline attached, so it comes and finds you instead: the run opens
a **GitHub issue**, which reaches you by email and mobile push through
notification machinery you already have configured, with no new secrets and no
third-party service.

The issue is written to be decidable from the notification itself — tier,
ticker, spread and expiry in the title; every number the gates used, the quoted
odd-lot paragraph, a link to the filing, and the four ways to forfeit the
preference in the body. It closes itself when the offer expires or stops
clearing the gates.

**It speaks once per offer per tier.** The screener re-scores its whole universe
twice a day, so an alert keyed on the offer alone would fire twice a day for as
long as the offer stayed open — and an alert that arrives every day is one you
stop reading, which costs more than the alert was ever worth. A new qualifying
offer speaks once. An upgrade from B to A speaks again, because that is news. A
decay from A to B stays quiet, because you already know. The
`(accession, tier)` pair it remembers is committed with the universe, so it
survives the runner.

**Deliberately not a failed build.** Failing the workflow is how this repo
alarms — GitHub emails the owner on a red scheduled run, and both `Report
Watchdog` and the daily report's stub check depend on that. But those are
failures, and a tender offer is good news. Overloading red to mean "something
good happened" would make the colour meaningless in the one repo where it is
load-bearing, and you could no longer tell a broken screener from a productive
one at a glance. Red stays reserved for breakage: a discovery outage, or a
screen that died.

Tune it in `config/odd_lot.json` under `notify` — `min_tier` (default `"B"`;
set `"A"` for hits only), the issue `labels`, and `close_when_gone`.

### Most days there are no Tier A results

That is the correct output, and the report says so in those words. An odd-lot
tender with a 3%+ spread and a clean condition set is genuinely rare. **The
thresholds are not lowered, the date window is not widened, and Tier C is not
promoted, to produce content.** An empty report is a valid report; a full one
produced by moving a threshold is worse than nothing, because it looks the same.

The `Rejected` section exists for the same reason. Seeing what was filtered and
why is the only way to know whether a threshold is doing its job or throwing
away the entire universe.

### SEC fair access

EDGAR is free and keyless, and the obligations that come with it are enforced in
one place, [`scripts/odd_lot.py`](scripts/odd_lot.py)'s `SecClient`:

- **A contact User-Agent on every request**, `<Tool name> <contact email>`. The
  `SEC_USER_AGENT` secret overrides the placeholder in config. A missing or
  generic User-Agent (`Mozilla/5.0`, `python-requests/2.28`) returns 403 and
  blocks the IP for about ten minutes — and on a shared GitHub runner, that is
  somebody else's outage too. `check_user_agent` refuses to start without one.
- **8 requests/second**, under the SEC's 10, held by a sliding-window limiter
  with a 0.12s spacing floor. The limit is per IP and aggregated across
  machines, so the headroom is not politeness theatre.
- **60-second backoff on 403 or 429, and no retry.** Retrying extends the block.
- **CIKs zero-padded to 10 digits.** An unpadded CIK 404s, which reads as "this
  company has no filings" rather than as an error.
- **Documents cached and never re-fetched.** An offer document cannot change; an
  amendment arrives as a new filing with its own accession.

The EFTS full-text search endpoint is undocumented and the SEC reserves the
right to change it, so it sits behind an adapter that **raises** on an
unexpected response shape rather than returning zero hits. A silent zero would
be indistinguishable from a quiet week, which is the normal result.

### Running it by hand

```bash
python scripts/odd_lot.py run --dry-run     # screen and print, write nothing
python scripts/odd_lot.py universe          # what is currently tracked
python scripts/odd_lot.py rescore           # re-price without re-discovering
python scripts/publish_odd_lot.py --dry-run # render the tab without writing it
python tests/test_odd_lot_pipeline.py --demo  # a full run, offline, on fixtures
```

Actions → **Odd-Lot Tender Screener** → *Run workflow* does the same on a runner.

## Scope

Only instruments you can actually trade in Robinhood are recommended:

| Asset class       | Venue                        | Direction vocabulary |
| ----------------- | ---------------------------- | -------------------- |
| Stocks & ETFs     | Robinhood                    | buy / sell-short     |
| Crypto            | Robinhood Crypto             | buy / sell           |
| Futures           | Robinhood Derivatives        | long / short         |
| Event contracts   | Robinhood Prediction Markets | yes / no             |

Three horizons, all treated as first-class: **intraday** (same session),
**swing** (days to weeks), and **long_term** (months to years, buy and hold).

**There are no quotas and no target count.** The report surfaces every idea
that clears the bar, up to 50, and the mix falls where it falls. Forcing variety
would mean dropping a good idea to make room for a worse one.

Conviction runs 2–5, and **2 is published** — that is where asymmetric,
small-cap and early-thesis ideas live. They are marked speculative and sized as
lottery tickets (1% max), which is what makes them safe to carry.

**Small and micro caps are in scope**, subject to a liquidity floor of $500K
average daily dollar volume, because a position you cannot exit is worth nothing.

**Futures are preferred over spot** when the same underlying trades as a
Robinhood contract. This is not stylistic — Robinhood Crypto cannot short, so a
bearish crypto `sell` cannot profit if the thesis is right, while a short `/MBT`
can. Validation fails that case outright.

See [`config/strategy.md`](config/strategy.md) and
[`config/universe.md`](config/universe.md) to tune this.

## Texas tax deed screener

A separate, twice-weekly module sharing this repo's Sheets credentials and
nothing else. Texas tax sales are the first Tuesday of each month and counties
publish their lists at least 21 days ahead; `Tax Deed Screener` ingests those
lists for **Dallas, Tarrant, Johnson and Ellis**, applies disqualifying filters,
and writes a shortlist to its own `Tax Deeds` tab plus a due-diligence packet per
surviving property. It never touches the trade report's tabs.

**It does not certify title and it cannot.** County clerk lien records are not
reliably machine-readable. Every row is a candidate requiring a professional
title search before any bid, and the checks that could not run are a column of
their own next to the ones that did — a blank Flags cell means the checks that
ran found nothing, never that the property is clear.

Two things surprise people, and both are the tool working rather than failing:
everything grades **Tier C** while the county clerk portals stay unscrapeable,
because an unscreened federal tax lien is a material flag; and **occupancy is
flagged unknown on every row**, because it cannot be determined remotely and is
never inferred.

Every county URL lives in [`config/tax_deeds.json`](config/tax_deeds.json) and
ships **unverified** — run `python scripts/tax_deed_sources.py verify` before the
first real run and expect to fix URLs and column names. County sites change
format without notice; the fix is always config, never the parser. Full
documentation: **[`config/tax_deeds.md`](config/tax_deeds.md)**.

```bash
python scripts/tax_deed_sources.py verify     # fetch every source, check structure
python scripts/tax_deed_screen.py --dry-run   # full run, Sheet untouched
python scripts/tax_deeds.py statement         # §34.015 written statement status
```

## Setup

The workflow cannot run until you provision four secrets and a Google Sheet.
Full walkthrough: **[docs/SETUP.md](docs/SETUP.md)**.

Quick version:

| Secret                      | Required | What it is                                      |
| --------------------------- | -------- | ----------------------------------------------- |
| `CLAUDE_CODE_OAUTH_TOKEN`   | yes      | `claude setup-token` — bills your Claude plan    |
| `GCP_SERVICE_ACCOUNT_JSON`  | yes      | Service account key, whole JSON file             |
| `GOOGLE_SHEET_ID`           | yes      | The `/d/<THIS>/edit` part of your Sheet URL      |
| `SEC_USER_AGENT`            | yes      | `Your Name your@email.com` — SEC requires it     |
| `FRED_API_KEY`              | no       | Free. Unlocks macro series                       |
| `FINNHUB_API_KEY`           | no       | Free tier. Better quotes, earnings calendar      |
| `TWELVEDATA_API_KEY`        | no       | Free tier. Backup daily OHLCV                    |
| `ALPHAVANTAGE_API_KEY`      | no       | Free tier. Last-resort OHLCV                     |
| `TAX_DEED_CONTACT_EMAIL`    | no       | Required only by the tax deed screener           |

Everything degrades gracefully: with zero optional keys the pipeline still runs
on Nasdaq, CoinGecko, SEC EDGAR, Kalshi, and Claude's own web search.

Source choice is driven by what actually works from a GitHub Actions runner,
which is a datacenter IP that many finance APIs treat differently from a
browser:

- **Quotes** come from Finnhub, **daily history** from Nasdaq — both work.
- **Yahoo** rate limits runners with `429` and **Stooq** returns `404` to them.
  Both are kept in the chain because they cost nothing to try and do sometimes
  succeed, but neither can be relied on.
- Twelve Data and Alpha Vantage sit behind those as keyed insurance.

## Running it manually

Actions → **Daily Trade Report** → *Run workflow*. Inputs let you shorten the
research budget or skip the Sheets write:

```
research_minutes: 15      # quick smoke test
dry_run: true             # writes reports/ but not the Sheet
```

## Layout

```
.github/workflows/
  daily-report.yml       the scheduled pipeline
  refresh-prices.yml     re-quotes today's ideas after the open and at midday
  weekly-digest.yml      Sunday scorecard: hit rate by conviction and horizon
  keepalive.yml          stops GitHub disabling the cron after 60 idle days
  data-sources-check.yml manual probe of every data source and the Sheet
  odd-lot-screener.yml   twice-daily odd-lot tender screen, 05:37 and 18:30 ET
  tax-deeds.yml          twice-weekly Texas tax deed screener (separate module)
.claude/skills/
  daily-research/        Phase 1 prompt contract
  daily-synthesis/       Phase 2 prompt contract
  daily-redteam/         Phase 2c adversarial review
config/
  strategy.md            horizon, sizing, conviction, ranking rules
  universe.md            Robinhood venue constraints
  odd_lot.json           SEC contact, capital cap, and every screener threshold
  tax_deeds.json         county sources, gates and the §34.015 statement
  tax_deeds.md           how the tax deed screener is configured
scripts/
  market_data.py         keyless-first data CLI Claude calls during research
  add_candidate.py       validates and captures a candidate during research
  validate_report.py     recomputes and checks every number before publishing
  exposure.py            portfolio-level net/gross and concentration warnings
  refresh_prices.py      post-open re-quote and distance-to-entry
  weekly_digest.py       weekly scorecard and conviction calibration
  build_context.py       prior picks and outcomes, so research has memory
  ensure_report.py       guarantees a publishable report.json exists
  publish_sheets.py      Sheets writer + performance grader
  dedupe_positions.py    one-off: collapse re-pitched ideas into one position
  step_summary.py        the Actions run summary
  check_sources.py       probes every data source and capability
  check_sheets.py        write/read/delete test against the Sheet
  odd_lot.py             odd-lot tender screener: EDGAR, gates, universe, report
  publish_odd_lot.py     the single "Odd Lot" tab, overwritten each run
  notify_odd_lot.py      opens a GitHub issue when a Tier A or B offer appears
  report_schema.json     the contract between synthesis and publishing
  tax_deeds.py           tax deed gates, redemption law, economics, tiering
  tax_deed_sources.py    county list / CAD / lien adapters, robots + rate limit
  tax_deed_screen.py     the tax deed run: ingest, screen, publish
reports/<date>/
  prior_context.md       what was recommended before and how it went
  candidates.jsonl       captured candidates — the research deliverable
  notes.md               raw research log (checkpointed)
  report.json            final structured output
  odd_lot.md             that day's odd-lot screen, tiers and rejections
state/
  open_positions.json    picks still being tracked for performance
  odd_lot_universe.json  open tender offers and the archive of closed ones
data/tax_deeds/
  <date>.json            tax deed run snapshot, every listing including rejects
  manual/                drop-box for counties that publish only a PDF
reports/tax_deeds/<sale>/
  <county>_<account>.md  due-diligence packet per Tier A/B candidate
tests/fixtures/odd_lot/
  *.html                 constructed language patterns for the parser
  real/                  actual filings, fetched on demand — see its README
```

## Tuning it

Three files change behavior with no code edits, and all are read fresh on every
run:

- **`config/strategy.md`** — how many ideas, the reward-to-risk floors per
  horizon, position size caps, the conviction rubric, and how the research
  budget is divided.
- **`config/universe.md`** — what is tradeable and what is excluded.
- **`config/odd_lot.json`** — the screener's SEC contact string, capital cap,
  spread and liquidity floors, tier boundaries, and schedule windows. Each one
  is explained in [the section above](#the-gates-and-why-each-threshold-is-where-it-is).

## Disclaimer

This software generates automated speculation from public data. It is not
investment advice, it is not produced by a registered advisor, and it carries no
warranty of accuracy. Model output can be confidently wrong, prices in the
report may be stale by the time you read it, and past performance in the
tracker tab does not predict future results. Trading stocks, crypto, futures,
and event contracts can lose you money, and futures in particular are leveraged
and can lose more than you deposit. You alone are responsible for every trade
you place.
