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
  tax-deeds.yml          twice-weekly Texas tax deed screener (separate module)
.claude/skills/
  daily-research/        Phase 1 prompt contract
  daily-synthesis/       Phase 2 prompt contract
  daily-redteam/         Phase 2c adversarial review
config/
  strategy.md            horizon, sizing, conviction, ranking rules
  universe.md            Robinhood venue constraints
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
  report_schema.json     the contract between synthesis and publishing
  tax_deeds.py           tax deed gates, redemption law, economics, tiering
  tax_deed_sources.py    county list / CAD / lien adapters, robots + rate limit
  tax_deed_screen.py     the tax deed run: ingest, screen, publish
reports/<date>/
  prior_context.md       what was recommended before and how it went
  candidates.jsonl       captured candidates — the research deliverable
  notes.md               raw research log (checkpointed)
  report.json            final structured output
state/
  open_positions.json    picks still being tracked for performance
data/tax_deeds/
  <date>.json            tax deed run snapshot, every listing including rejects
  manual/                drop-box for counties that publish only a PDF
reports/tax_deeds/<sale>/
  <county>_<account>.md  due-diligence packet per Tier A/B candidate
```

## Tuning it

Two files change behavior with no code edits, and both are read fresh on every
run:

- **`config/strategy.md`** — how many ideas, the reward-to-risk floors per
  horizon, position size caps, the conviction rubric, and how the research
  budget is divided.
- **`config/universe.md`** — what is tradeable and what is excluded.

## Disclaimer

This software generates automated speculation from public data. It is not
investment advice, it is not produced by a registered advisor, and it carries no
warranty of accuracy. Model output can be confidently wrong, prices in the
report may be stale by the time you read it, and past performance in the
tracker tab does not predict future results. Trading stocks, crypto, futures,
and event contracts can lose you money, and futures in particular are leveraged
and can lose more than you deposit. You alone are responsible for every trade
you place.
