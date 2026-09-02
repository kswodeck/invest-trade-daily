---
name: daily-research
description: Phase 1 of the daily trade report. Deep research into news, filings, macro, price action, and event markets to surface Robinhood-tradeable trade ideas, checkpointing findings continuously to notes.md.
allowed-tools: WebSearch, WebFetch, Bash, Read, Write, Edit, Glob, Grep
---

# Daily research phase

You are researching trade ideas for today's report. Read these three files
first — they override anything here that conflicts:

| File | What it gives you |
| --- | --- |
| `config/strategy.md` | What counts as a good idea, and how to rank |
| `config/universe.md` | What is tradeable |
| `reports/<date>/prior_context.md` | What you already recommended, and how it went |

## Prior context is not optional reading

`prior_context.md` lists your open positions, your hit rate by category, and the
symbols you have been repeating. Three obligations come out of it:

1. **Manage open positions before hunting new ones.** For each open position,
   decide: hold, adjust the target or stop on new information, or close early.
   If something changed, emit a recommendation for that symbol and mark it as an
   update to an existing position — do not present it as a fresh idea.
2. **Do not re-pitch.** A symbol you have recommended three days running is a
   sign you are anchored, not a sign of conviction. Re-recommend it only if
   something concrete changed, and say what changed.
3. **Let the track record inform the bar, carefully.** If a category is
   consistently losing, raise the bar for it. But under roughly 15 closed trades
   the sample is noise — say so rather than over-fitting to a bad week.

## The single most important rule

**You will be killed without warning when the time cap expires.** There is no
grace period and no chance to write a summary at the end. Everything you have
not already written to disk is lost.

A previous run learned this the hard way: it produced 38,000 characters of
excellent research and **zero usable ideas**, because it spent the whole budget
gathering and never converted anything into a candidate before it was killed.
Rich notes that nobody can trade are a failed run.

## Your deliverable is candidates.jsonl, not notes.md

`notes.md` is your working log. **`candidates.jsonl` is the actual output.**
Synthesis builds the report from it. A finding that never becomes a candidate
does not reach the reader.

Capture a candidate the moment it is fully specified — entry, target, stop,
catalyst, sources:

```bash
python scripts/add_candidate.py '{
  "symbol": "NVDA",
  "instrument": "NVIDIA Corp",
  "asset_class": "stock",
  "venue": "Robinhood Stocks",
  "direction": "buy",
  "horizon": "swing",
  "conviction": 4,
  "entry": {"ideal": 178.50, "zone_low": 176.0, "zone_high": 180.0},
  "exit": {"target": 205.0, "target_2": 218.0},
  "stop": 168.0,
  "position_size_pct": 3,
  "catalyst": {"event": "Q2 earnings", "datetime_et": "2026-08-27T16:20",
               "action": "enter before, trim half into the print", "wait": false},
  "win_probability": 0.45,
  "thesis": "Two specific sentences naming the mechanism.",
  "key_risk": "The one thing most likely to break it.",
  "counter_argument": "The strongest case against.",
  "evidence": [
    {"kind": "dated_catalyst", "detail": "Q2 earnings confirmed on the fetched calendar",
     "source": "https://..."},
    {"kind": "primary_document", "detail": "Read the 8-K; guidance raised on datacenter",
     "source": "https://..."},
    {"kind": "positioning", "detail": "Three officers bought open-market in August",
     "source": "https://..."}
  ],
  "sources": ["https://...", "https://..."]
}'
```

Two fields there are new and are the ones most often left out:

- **`evidence`** is what conviction now means. One entry per *independent*
  confirmation, and the score is the count of distinct `kind` values — 1 kind
  is a 2, two kinds a 3, three a 4, four or more a 5. Three articles about the
  same press release are one confirmation, not three. See the conviction table
  in `config/strategy.md` for what each kind requires.
- **`win_probability`** is your estimate that the target is reached before the
  stop. It has a hard baseline: `1 / (1 + R:R)` is both the driftless
  random-walk probability and the break-even hit rate, so at 3:1 anything at or
  below 25% is an idea that loses money at its own numbers. Whatever you claim
  above that baseline is the edge you are asserting — validation prints both.

It validates on the spot and tells you what is wrong, so a malformed idea
surfaces while you can still fix it. It rejects non-Robinhood venues outright.

**Two hard deadlines. Neither is negotiable:**

| By | You must have |
| --- | --- |
| **Minute 20** | At least one candidate captured, even a conviction-2 one |
| **70% of budget** | Stopped all new research; converting findings to candidates |

Check the clock with `date` rather than trusting your sense of elapsed time. If
minute 20 arrives and you have nothing captured, you are researching too
broadly — take your best current idea, set levels from real price history, and
capture it. You can always capture an improved version later; the file is a log
and synthesis takes the last entry per symbol.

Set up first, before any research:

```bash
DATE=$(TZ=America/New_York date +%F)
mkdir -p "reports/$DATE"
echo "# Research log — $DATE" > "reports/$DATE/notes.md"
```

Then append to `notes.md` continuously for context, reasoning, and rejections.
Use `Edit` or shell appends — never rewrite the file wholesale, and never
buffer findings to write "in a moment".

## Time budget

Your total budget is set by the workflow (normally 60 minutes). Track elapsed
time with `date` calls; do not trust your sense of how long things have taken.
Allocate roughly per `config/strategy.md`:

| Phase | Share | Output |
| --- | --- | --- |
| Macro and calendar | 10% | Market regime, this week's dated events |
| Catalyst hunting | 30% | Dated events in the next 10 sessions |
| News and filings | 20% | Overnight moves, 8-Ks, guidance, analyst actions |
| Level setting | 20% | Real entry/target/stop from price history |
| Falsification | 10% | The case against each finalist |
| Consolidation | 10% | Everything remaining captured as candidates |

Do not treat these as strict sequential stages. **Capture candidates as you go**
— when catalyst hunting turns up a dated event and you can set levels on it, run
`add_candidate.py` right then rather than saving it for a later pass. The
falsification and consolidation phases refine what is already captured; they are
not the first time anything gets written down.

A half-researched idea with no levels is unusable, but so is a perfect idea that
was never captured. Six complete candidates beat fifteen fragments, and both
beat an empty file.

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
python scripts/market_data.py insiders NVDA         # open-market insider buying
python scripts/market_data.py analysts NVDA        # recommendation trend, surprise record
python scripts/market_data.py short NVDA           # short interest, days to cover
python scripts/market_data.py relstrength NVDA --peer XLK   # leading or lagging?
python scripts/market_data.py implied NVDA --entry 178.5 --target 205
                                                   # is the target inside what options price?
```

**Check insiders on every equity finalist.** Executives sell for a hundred
reasons — taxes, diversification, a house — but they buy for one. A cluster of
open-market purchases (`open_market_buys` with several `distinct_buyers`) is one
of the few genuinely predictive public signals, and it is strongest exactly
where this report is weakest: confirming that a de-rated name is cheap rather
than broken. Cite it in the thesis when it is there. Its absence is not a
negative, so do not treat it as one.

**Set the stop before the target, and never the other way round.** The stop is
where the thesis is wrong; find that level first, from real price history, then
see what target the reward-to-risk floor implies and ask whether it is
reachable. Doing it in the other order produces a stop reverse-engineered to
clear the floor, which is what the first month of this report actually did:
every one of the first ten stop-outs had a stop tighter than 1.6 ATR. A swing
stop must now clear 2.0 ATR to publish — 1.8 for an ETF, 2.5 for crypto and
futures, which gap in ways ATR does not describe — or validation fails the
idea. See the table in `config/strategy.md`. **If an idea
only clears the floor with a tight stop, the idea failed the floor** — widen
the stop, recheck, and drop it if it no longer qualifies.

When a source returns `ok: false`, note it and move on — record the gap so the
synthesis phase can report it honestly in `data_quality_notes`. Use WebSearch
and WebFetch for anything the CLI does not cover: breaking news, analyst
commentary, Robinhood product availability, sector narratives.

**Never state a price you did not fetch.** If you could not get a number, write
`unknown` in the notes. A fabricated price is worse than a missing one because
it will be traded on.

## Note format

Candidates go through `add_candidate.py`, so `notes.md` carries everything
else: reasoning, context, evidence, and the work you did that did not become a
recommendation. Timestamp every entry and cite sources. Headings are yours to
choose — `MACRO`, `LEVELS`, `NEWS`, `VENUE CHECK` and similar are all useful —
with three that carry specific meaning:

```markdown
## [HH:MM ET] MACRO — rates and policy
- <finding> — source: <url>

## [HH:MM ET] REJECTED — TSLA — no dated catalyst inside horizon, R:R 1.2

## [HH:MM ET] POSITION UPDATE — NVDA — opened 2026-08-05, +6.2%
- decision: hold, raise stop to 176 (now above entry)
- why: earnings moved to 2026-08-27; thesis intact, first target within 2 ATR
- action: captured via add_candidate.py with the revised stop
```

Log rejections in one line each. They stop synthesis from re-litigating ideas
you already dismissed, and they show the work.

A `POSITION UPDATE` still needs `add_candidate.py` to reach the report — note
the decision here, then capture it. Notes alone change nothing.

## Scope reminders

- Robinhood-tradeable only. Verify availability when uncertain — do not rely on
  what you remember about Robinhood's product list.
- Prefer micro and nano futures contracts. Name the contract month.
- Event contract prices are cents and mean implied probability. Your edge must
  be a stated probability disagreement, not a hunch.
- Options are out of scope entirely.
- **There is no target count.** Capture everything that clears the bar, up to
  50. Twenty good candidates is a good day; so is six. Never stop early to hit a
  tidy number, and never pad. Diversify the driver — twenty ideas that all
  depend on one CPI print is one idea.
- **The conviction floor is 2, not 3.** Conviction 2 is where asymmetric,
  small-cap and early-thesis ideas live and it is explicitly wanted — but it is
  sized as a lottery ticket and its thinness must be stated in `key_risk`.

## Reach beyond the obvious names

Three things this report should hunt harder than a generic screen would:

**Small and micro caps.** The asymmetric ideas are below the mega-cap tier, and
a report full of names everyone already owns is not worth much. Check liquidity
first — average daily dollar volume must clear $500K and your position must be a
small fraction of it — then size it as a lottery ticket, widen the stop to the
instrument's real volatility, and name the dilution and halt risk. State the
market cap and dollar volume in the thesis for anything under $2B.

**Futures over spot.** When the same underlying trades as a Robinhood futures
contract, prefer the contract. This is not stylistic: Robinhood Crypto cannot
short at all, so a bearish crypto `sell` makes no money if you are right. A
short `/MBT` does. The same applies to index views — `/MES` over shorting SPY,
which needs margin. See the substitution table in `config/universe.md`. The
exception is long-term holds, where roll costs make spot cleaner.

**Event contracts.** Actively hunt Robinhood's prediction markets rather than
treating them as a curiosity. A mispriced probability is often a cleaner
expression than the equivalent equity trade, because the payoff is defined and
the thesis is one falsifiable claim rather than a price path that can be right
and still stop you out. Use `market_data.py events "<topic>"` and state the
market's implied probability against your own estimate.

## Horizons carry no quotas

`intraday`, `swing`, and `long_term` are all first-class, and there is no target
number for any of them. **Do not manufacture a mix.** Capture the best
opportunities you actually find; if that is seven long-term accumulations and
one day trade, capture exactly that.

`long_term` is the lane most easily crowded out by the day's news, because
nothing about it is urgent. Give it deliberate time rather than the leftovers:
a quality business de-rated on a fixable problem, a secular supply or demand
imbalance with years to run, an asset repricing to a new regime. These often
turn out to be the highest-conviction ideas of the day precisely because they
do not depend on guessing a reaction to a print.

Long-term candidates are shaped differently, and that is expected:

- `catalyst.datetime_et` may be `null`; use `catalyst.event` for the driver and
  `catalyst.action` for the accumulation plan
- `entry.zone_low` / `zone_high` matter more than `entry.ideal`
- `exit.target` is a defended valuation, not a chart level
- `stop` may be `null`, but `key_risk` must then state the concrete
  invalidation — the development that proves the thesis wrong, not a price move
- reward-to-risk floor is 2.5, measured against a stated bear-case price

See `config/strategy.md` for the full definitions.

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
