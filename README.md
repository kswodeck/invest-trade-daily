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
| `ALPHAVANTAGE_API_KEY`      | no       | Free tier. Fallback quotes and fundamentals      |

Everything degrades gracefully: with zero optional keys the pipeline still runs
on Stooq, CoinGecko, SEC EDGAR, Kalshi, and Claude's own web search.

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
  daily-report.yml     the scheduled pipeline
  keepalive.yml        stops GitHub disabling the cron after 60 idle days
.claude/skills/
  daily-research/      Phase 1 prompt contract
  daily-synthesis/     Phase 2 prompt contract
config/
  strategy.md          horizon, sizing, conviction, ranking rules
  universe.md          Robinhood venue constraints
scripts/
  market_data.py       keyless-first data CLI Claude calls during research
  publish_sheets.py    Sheets writer + performance grader
  report_schema.json   the contract between synthesis and publishing
reports/<date>/
  notes.md             raw research log (checkpointed)
  report.json          final structured output
state/
  open_positions.json  picks still being tracked for performance
```

## Disclaimer

This software generates automated speculation from public data. It is not
investment advice, it is not produced by a registered advisor, and it carries no
warranty of accuracy. Model output can be confidently wrong, prices in the
report may be stale by the time you read it, and past performance in the
tracker tab does not predict future results. Trading stocks, crypto, futures,
and event contracts can lose you money, and futures in particular are leveraged
and can lose more than you deposit. You alone are responsible for every trade
you place.
