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
   ├─ Phase 2 — SYNTHESIS  (Opus, ~12 min, always runs)
   │    Reads whatever notes exist and emits strict-schema report.json.
   │
   ├─ Phase 3 — PUBLISH
   │    Grades yesterday's open picks, then writes:
   │      • "Today" tab      — this morning's ranked ideas
   │      • "<date>" tab     — dated archive of the same
   │      • "Performance"    — running scorecard of every past call
   │
   └─ Phase 4 — COMMIT
        reports/<date>/ lands in git as the durable audit trail.
```

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

Horizons: **intraday** and **swing** (days to weeks). See
[`config/strategy.md`](config/strategy.md) and
[`config/universe.md`](config/universe.md) to tune this.

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
  keepalive.yml          stops GitHub disabling the cron after 60 idle days
  data-sources-check.yml manual probe of every data source and the Sheet
.claude/skills/
  daily-research/        Phase 1 prompt contract
  daily-synthesis/       Phase 2 prompt contract
config/
  strategy.md            horizon, sizing, conviction, ranking rules
  universe.md            Robinhood venue constraints
scripts/
  market_data.py         keyless-first data CLI Claude calls during research
  add_candidate.py       validates and captures a candidate during research
  build_context.py       prior picks and outcomes, so research has memory
  ensure_report.py       guarantees a publishable report.json exists
  publish_sheets.py      Sheets writer + performance grader
  step_summary.py        the Actions run summary
  check_sources.py       probes every data source and capability
  check_sheets.py        write/read/delete test against the Sheet
  report_schema.json     the contract between synthesis and publishing
reports/<date>/
  prior_context.md       what was recommended before and how it went
  candidates.jsonl       captured candidates — the research deliverable
  notes.md               raw research log (checkpointed)
  report.json            final structured output
state/
  open_positions.json    picks still being tracked for performance
```

## Tuning it

Two files change behavior with no code edits, and both are read fresh on every
run:

- **`config/strategy.md`** — how many ideas, the swing/intraday split, minimum
  reward-to-risk, position size caps, the conviction rubric, and how the
  research budget is divided.
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
