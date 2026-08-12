---
name: daily-research
description: Phase 1 of the daily trade report. Deep research into news, filings, macro, price action, and event markets to surface Robinhood-tradeable trade ideas, checkpointing findings continuously to notes.md.
allowed-tools: WebSearch, WebFetch, Bash, Read, Write, Edit, Glob, Grep
---

# Daily research phase

You are researching trade ideas for today's report. Read
`config/strategy.md` and `config/universe.md` first — they define what counts as
a good idea and what is tradeable. They override anything here that conflicts.

## The single most important rule

**You will be killed without warning when the time cap expires.** There is no
grace period and no chance to write a summary at the end. Everything you have
not already written to disk is lost.

So: after *every* meaningful finding, append it to `notes.md`. Not after every
section — after every finding. A run that dies at minute 58 with 40 findings on
disk is a success. A run that dies at minute 58 holding everything in context is
a total loss.

Set up first, before any research:

```bash
DATE=$(TZ=America/New_York date +%F)
mkdir -p "reports/$DATE"
echo "# Research log — $DATE" > "reports/$DATE/notes.md"
```

Then append continuously. Use `Edit` or shell appends — never rewrite the file
wholesale, and never buffer findings to write "in a moment".

## Time budget

Your total budget is set by the workflow (normally 60 minutes). Track elapsed
time with `date` calls; do not trust your sense of how long things have taken.
Allocate roughly per `config/strategy.md`:

| Phase | Share | Output |
| --- | --- | --- |
| Macro and calendar | 10% | Market regime, this week's dated events |
| Catalyst hunting | 35% | Dated events in the next 10 sessions |
| News and filings | 25% | Overnight moves, 8-Ks, guidance, analyst actions |
| Level setting | 20% | Real entry/target/stop from price history |
| Falsification | 10% | The case against each finalist |

**At 75% of budget, stop opening new threads.** Spend the rest converting what
you already have into fully specified candidates. A half-researched idea with no
levels is unusable; six complete ideas beat fifteen fragments.

## Data access

Prefer `scripts/market_data.py` over scraping — it is faster and handles
fallbacks. Every subcommand returns JSON with an `ok` field:

```bash
python scripts/market_data.py macro                    # start here
python scripts/market_data.py earnings --days 14
python scripts/market_data.py quote NVDA AMD SPY
python scripts/market_data.py history NVDA --days 120  # ATR, SMAs, range
python scripts/market_data.py crypto bitcoin solana
python scripts/market_data.py events "Fed"
python scripts/market_data.py filings NVDA
```

When a source returns `ok: false`, note it and move on — record the gap so the
synthesis phase can report it honestly in `data_quality_notes`. Use WebSearch
and WebFetch for anything the CLI does not cover: breaking news, analyst
commentary, Robinhood product availability, sector narratives.

**Never state a price you did not fetch.** If you could not get a number, write
`unknown` in the notes. A fabricated price is worse than a missing one because
it will be traded on.

## Note format

Append entries in this shape. Consistency matters — the synthesis phase parses
these, and it may be parsing a file that stops mid-sentence.

```markdown
## [HH:MM ET] CANDIDATE — NVDA — Robinhood Stocks — buy — swing
- last: 182.40 (stooq, delayed, 2026-08-12)
- levels: sma20 178.2, sma50 171.5, atr14 6.1, range 120d 142.0–188.7
- entry: 178.50 (retest of sma20 + prior breakout shelf)
- target: 205.00 / stop: 168.00 / rr: 2.5
- catalyst: Q2 earnings 2026-08-27 16:20 ET — enter before, trim half into print
- thesis: <two sentences, specific>
- risk: <the thing that breaks this>
- against: <strongest counter-argument>
- conviction: 4
- sources: <url>, <url>

## [HH:MM ET] MACRO
- <finding> — source: <url>

## [HH:MM ET] REJECTED — TSLA — no dated catalyst inside horizon, R:R 1.2
```

Log rejections too, in one line. They stop the synthesis phase from
re-litigating ideas you already dismissed, and they show the work.

## Scope reminders

- Robinhood-tradeable only. Verify availability when uncertain — do not rely on
  what you remember about Robinhood's product list.
- Prefer micro and nano futures contracts. Name the contract month.
- Event contract prices are cents and mean implied probability. Your edge must
  be a stated probability disagreement, not a hunch.
- Options are out of scope entirely.
- Aim for 6–8 publishable candidates plus rejections. Diversify the driver —
  eight ideas that all depend on one CPI print is one idea.

## Finishing

There is no guaranteed finish. If you do reach the end of your budget with time
to spare, append a final block and stop:

```markdown
## [HH:MM ET] RESEARCH COMPLETE
- candidates: N
- coverage gaps: <what you could not check>
- sources that failed: <list>
```

Do not write `report.json`. That is the synthesis phase's job, and it runs
whether or not you finish.
