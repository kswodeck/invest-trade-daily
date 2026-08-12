# Strategy configuration

Everything here is a tunable knob. Edit this file to change what the daily
report looks for and how it ranks. The research and synthesis phases both read
it, so a change here takes effect on the next run with no code change.

## Output shape

| Setting | Value |
| --- | --- |
| Total recommendations | **6–8** |
| Swing ideas (days to weeks) | 4–5 |
| Intraday ideas (same session) | 2–3 |
| Watchlist (not yet actionable) | up to 5 |
| Minimum conviction to publish | 3 of 5 |

If a genuinely good idea count comes up short, **publish fewer**. Padding the
list with filler to hit 8 is worse than shipping 4 strong ideas and saying the
tape was thin. Record that judgement in `data_quality_notes`.

## Horizon definitions

**Intraday** — entered and exited within the same US session. Levels must be
precise and are expected to be live only for the first few hours after the
open. Requires a specific intraday catalyst: an earnings reaction, an economic
print at 8:30 ET, a gap to fill, an overnight futures move. Not a general lean.

**Swing** — held days to weeks. Entry may be a zone rather than a single price.
Thesis must survive an overnight gap, so a swing idea whose entire edge is one
scheduled event needs the event risk called out explicitly.

## Risk parameters

- **Minimum reward-to-risk: 2.0** on swing, **1.5** on intraday. Compute from
  entry, target, and stop. An idea that cannot clear this does not publish.
- **Every idea carries a stop.** Futures and short equity: mandatory, no
  exceptions. Long equity, crypto, and event contracts: a stop or an explicit
  invalidation condition in prose.
- **Position sizing** is expressed as a percentage of trading capital, not a
  dollar amount: `1%` (speculative), `2-3%` (standard), `5%` (high conviction).
  Never suggest more than 5% in a single idea, or more than 2% in a futures
  contract.
- **Correlation cap.** No more than 3 ideas whose outcome depends on the same
  driver — the same sector, the same macro print, the same rate path. Eight
  ideas that are all one bet on semis is one idea with extra steps.

## Conviction scale

| Score | Meaning |
| --- | --- |
| 5 | Multiple independent confirmations, clear catalyst with a known date, clean technical level, no obvious counter-argument |
| 4 | Strong thesis with a dated catalyst; one meaningful counter-argument, addressed |
| 3 | Reasonable setup, thinner evidence or a vaguer catalyst window |
| 2 | Speculative — do not publish as a recommendation, route to watchlist |
| 1 | Noise |

Conviction is about **evidence quality**, not expected return. A 5 can be a
modest, high-probability move. A lottery ticket is never above a 2.

## Ranking

Rank by conviction first, then by reward-to-risk, then by catalyst proximity.
An idea whose catalyst is tomorrow outranks an equivalent idea whose catalyst is
in three weeks, because the capital turns over faster.

## What makes a catalyst

The `catalyst` field is the most valuable part of the report and the hardest to
fake. It must name **a specific thing that happens at a specific time**:

- Good: `Q3 earnings, Aug 27 after close ET — enter before, trim half into print`
- Good: `CPI release Aug 13 08:30 ET — wait for the print, do not front-run`
- Good: `Fed decision Sep 17 14:00 ET — position after the statement, not before`
- Bad: `continued AI momentum`
- Bad: `technical breakout` (that is a trigger, not a catalyst — put it in entry)

Where the right action is to **wait**, say so and give the condition to wait
for. "Do not enter until X" is a legitimate and often correct recommendation.

## Research priorities

Spend the research budget roughly like this:

1. **Macro and calendar first (~10%).** What prints this week, what the tape did
   overnight, where rates and the dollar are. This frames everything else.
2. **Catalyst hunting (~35%).** Earnings in the next 10 sessions, scheduled
   economic releases, FDA dates, product launches, index rebalances, unlocks,
   court dates, regulatory deadlines. Dated events beat vibes.
3. **News and filings sweep (~25%).** Overnight news, 8-Ks, guidance changes,
   insider transactions, analyst moves that actually move price.
4. **Level-setting (~20%).** For each surviving candidate, pull real price
   history and set entry, target, and stop on actual support/resistance and
   ATR — not round numbers.
5. **Falsification (~10%).** For each finalist, argue the other side. Anything
   that does not survive gets demoted or cut. This step is not optional and is
   the first thing people skip.

## Weekend behavior

US equities and futures are closed. A Saturday or Sunday run should shift
toward crypto and event contracts for actionable ideas, and treat equities as
week-ahead preparation — pre-positioning levels and the coming calendar rather
than same-day entries. Mark those `horizon: "swing"` and note that entry is for
the next open.
