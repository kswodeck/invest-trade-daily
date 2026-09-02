# Strategy configuration

Everything here is a tunable knob. Edit this file to change what the daily
report looks for and how it ranks. The research and synthesis phases both read
it, so a change here takes effect on the next run with no code change.

## Output shape

| Setting | Value |
| --- | --- |
| Total recommendations | **no target — publish everything that clears the bar, up to 50** |
| Horizon mix | **no quotas — whatever the opportunities actually are** |
| Watchlist (not yet actionable) | up to 25 |
| Minimum conviction to publish | **2 of 5** |

There is no quota and no ideal count. Fifty is a hard ceiling to keep the sheet
readable, not a goal. Six genuinely good ideas is a good day; so is twenty-five
when the tape is rich. **Never cut a qualifying idea to hit a tidy number, and
never invent one to fill space.**

**There are no per-horizon targets, and you must not manufacture variety.** The
report's job is to surface the genuinely best opportunities available today, in
whatever form they take. If the best eight ideas are all long-term
accumulations, publish eight long-term ideas. If the tape offers three sharp
intraday setups and nothing else, publish three.

A balanced-looking report assembled by forcing a mix is worse than an honest
lopsided one, because the filler crowds out the real ideas and reads with the
same authority. Note the skew in `data_quality_notes` when it is pronounced —
"nothing intraday cleared the bar today, the tape was directionless" is useful
context, not an apology.

Likewise, if the count comes up short, **publish fewer**. Four strong ideas and
a note that the tape was thin beats ten with six of filler.

## Horizon definitions

Three horizons, all first-class. None is preferred over the others; the right
horizon is whichever one the opportunity actually fits.

**`intraday`** — entered and exited within the same US session. Levels must be
precise and are expected to be live only for the first few hours after the
open. Requires a specific intraday catalyst: an earnings reaction, an economic
print at 8:30 ET, a gap to fill, an overnight futures move. Not a general lean.

**`swing`** — held days to weeks. Entry may be a zone rather than a single
price. Thesis must survive an overnight gap, so a swing idea whose entire edge
is one scheduled event needs the event risk called out explicitly.

**`long_term`** — months to years. Buy and hold. This is a different kind of
claim from the other two and is judged differently:

- The thesis is about **the business or the asset**, not about a catalyst:
  earnings power, competitive position, balance sheet, secular demand,
  structural supply, monetary debasement. A dated event may inform the entry,
  but it is not the reason to own the thing.
- **Entry is a zone or an accumulation rule**, not a single tick —
  "accumulate below $118, add under $105" is a legitimate entry.
- **The exit target is a valuation anchor**, not a technical level: state what
  the asset is worth and why, and over roughly what period.
- `catalyst.datetime_et` may be `null`. Use `catalyst.event` to name the driver
  and `catalyst.action` to say how to build the position over time.
- **A hard stop is not required, but an explicit invalidation condition is
  mandatory** — the specific development that would mean the thesis is wrong,
  such as "gross margin below 40% for two consecutive quarters" or "the capex
  cycle rolls over". "The price fell" is not an invalidation.

Long-term ideas legitimately repeat across days while accumulation is
unfinished. That is not the anchoring problem the repetition guard is aimed at
— but say plainly that it is a continuing position rather than a new one.

## Risk parameters

- **Minimum reward-to-risk**, computed from entry, target, and the downside
  level. An idea that cannot clear its floor does not publish.

  | Horizon | Floor | Risk measured against |
  | --- | --- | --- |
  | `intraday` | 1.5 | the stop |
  | `swing` | 2.0 | the stop |
  | `long_term` | 2.5 | an explicit downside case with a price |

  Long-term risk is not a stop — it is what the asset is plausibly worth if the
  thesis is wrong. State that number. A long-term idea whose downside you cannot
  put a price on is not researched enough to publish.

  **Do not reverse-engineer levels to clear the floor.** The floor exists to
  reject ideas, not to calibrate targets. If a target only works by being
  optimistic, the idea failed the test.

- **Minimum stop distance**, in ATRs, because the floor above can be cleared
  two ways and only one of them is honest work.

  | Horizon | Stop must clear | Comfortable |
  | --- | --- | --- |
  | `intraday` | 0.75 ATR | 1.25 ATR |
  | `swing` | 1.5 ATR | 2.0 ATR |
  | `long_term` | n/a — the downside is a bear case, not a stop | |

  A stop closer to the entry than a normal day's range does not test the
  thesis, it tests whether the tape sits still. It is also the free way to lift
  reward-to-risk, and that is exactly how it was used: KRE was republished
  three times at an unchanged 76.80 entry with the stop walked in from 74.20 to
  75.20, lifting the ratio from 2.19 to 4.07 while making the trade strictly
  worse. Every one of the first ten stop-outs had a stop tighter than 1.6 ATR.

  **If an idea needs a tight stop to clear the reward-to-risk floor, it has
  failed the floor.** Widen the stop and re-check the ratio, or drop the idea.

- **State a win probability, and beat the baseline.** Reward-to-risk says
  nothing about whether an idea makes money — 3:1 at a 20% hit rate loses.
  Every idea with a stop carries `win_probability`: your estimate that the
  target is reached before the stop.

  The number to beat is not arbitrary. For a driftless random walk the chance
  of touching the target first is exactly `1 / (1 + R:R)` — which is also the
  break-even hit rate. So an idea at 3:1 needs better than 25% just to be worth
  nothing, and whatever you claim above that **is** the edge you are asserting.
  Validation prints the two side by side. An expectancy at or below zero is a
  hard failure; more than 20 points of claimed edge over the baseline is a
  large claim and the thesis has to carry it.

- **Every idea carries a downside.** Futures and short equity: a hard stop,
  mandatory, no exceptions. Long equity, crypto, and event contracts: a stop or
  an explicit invalidation condition. Long-term: an invalidation condition is
  required and a stop is optional, since a hard stop on a multi-year thesis
  usually just sells the bottom.
- **Position sizing** is a percentage of trading capital, not a dollar amount,
  and it falls out of conviction and risk tier rather than enthusiasm:

  | Tier | Size | Applies to |
  | --- | --- | --- |
  | Lottery ticket | 0.5–1% | conviction 2, micro caps, binary outcomes |
  | Speculative | 1–2% | small caps, futures, event contracts |
  | Standard | 2–3% | conviction 3–4 in liquid names |
  | High conviction | 4–5% | conviction 5, or a long-term core holding |

  Never more than 5% in a single idea, never more than 2% in a futures contract,
  and never more than 1% in anything below a $300M market cap.

  Small position sizing is what makes speculative ideas safe to publish. A
  conviction-2 micro cap at 1% is a sensible bet; the same idea at 5% is how
  accounts get damaged.
- **Correlation cap.** No more than 3 ideas whose outcome depends on the same
  driver — the same sector, the same macro print, the same rate path. Eight
  ideas that are all one bet on semis is one idea with extra steps.

## Conviction scale

**Conviction is a count of independent confirmations you actually made.** Not a
feeling about the idea, not a proxy for expected return, and not a default.

It became a default: of the first 57 published ideas, 39 scored 3. A number
that lands on the same value two times in three is carrying no information, and
the by-conviction table on the Performance tab is unreadable because of it.

So the score is now tied to the `evidence` array on each idea. List each
confirmation with its `kind`, and the score follows from **how many distinct
kinds** hold:

| Score | Distinct kinds of confirmation | Published? |
| --- | --- | --- |
| 5 | 4 or more | yes |
| 4 | 3 | yes |
| 3 | 2 | yes |
| 2 | 1 | yes, clearly marked |
| 1 | none — a hunch | no |

The kinds, and what each actually requires:

| `kind` | Counts only when |
| --- | --- |
| `dated_catalyst` | The event is verified against a calendar you fetched, not a date you remember |
| `primary_document` | You read the filing, transcript or release — not a story about it |
| `positioning` | A measured flow or crowding read: insider buys, short interest and days to cover, analyst revision direction, the options-implied move, relative strength |
| `valuation_anchor` | A defended number for what the asset is worth, with the method shown |
| `technical_level` | A level from real price history — prior swing, moving average, volume shelf — never a round number |
| `counter_argument_answered` | The strongest case against, answered with evidence rather than asserted away |

**Two entries of the same kind are one confirmation.** Three articles about one
press release are one fact; counting them as three is how a thin idea comes to
look sturdy. Validation checks the count of distinct kinds against the score
and names the supported score when they disagree — the red team lowers it.

**Conviction is about evidence quality, not expected return.** A 5 can be a
modest, high-probability move; a moonshot with one source is a 2 no matter how
large the upside.

**Conviction 2 is publishable and useful** — that is where asymmetric,
small-cap and early-thesis ideas live, and cutting them would remove exactly
the high-risk/high-return lane worth having. But it must be honest about what
it is: a 2 needs its thinness stated in `key_risk`, and it is sized like a
lottery ticket, not a position. Never inflate a 2 to a 3 to make it look
sturdier — with the evidence list on the page, the inflation is now visible.

## Ranking

Rank by **conviction** first, then by **reward-to-risk**. Break remaining ties
with catalyst proximity — but only between ideas of the same horizon, since a
long-term thesis has no near catalyst by construction and would otherwise be
penalised for being what it is.

Rank on merit alone. Do not interleave horizons to make the list look balanced,
and do not push a long-term idea down because it is slower. If the strongest
idea today is a five-year hold, it ranks first.

## What makes a catalyst

For `intraday` and `swing`, the `catalyst` field is the most valuable part of
the report and the hardest to fake. It must name **a specific thing that
happens at a specific time**:

- Good: `Q3 earnings, Aug 27 after close ET — enter before, trim half into print`
- Good: `CPI release Aug 13 08:30 ET — wait for the print, do not front-run`
- Good: `Fed decision Sep 17 14:00 ET — position after the statement, not before`
- Bad: `continued AI momentum`
- Bad: `technical breakout` (that is a trigger, not a catalyst — put it in entry)

For `long_term`, the same field carries **the driver and the accumulation
plan** instead, and a dated event is optional:

- Good: `Datacenter power demand outrunning generation capacity through 2029 —
  accumulate below $118 in thirds, add on any macro-driven drawdown under $105`
- Good: `Post-patent-cliff pipeline maturing 2027-2029; buy the de-rating —
  build over the next two quarters, no need to rush`
- Bad: `long-term growth story` (that is a category, not a driver)

The test is the same in both cases: could a reader act on this without
guessing what you meant?

Where the right action is to **wait**, say so and give the condition to wait
for. "Do not enter until X" is a legitimate and often correct recommendation.

## Research priorities

Spend the research budget roughly like this:

1. **Macro and calendar first (~10%).** What prints this week, what the tape did
   overnight, where rates and the dollar are. This frames everything else.
   Also check relative strength before committing to a name: `market_data.py
   relstrength SYM --peer <sector ETF>` says whether you are buying leadership
   or catching something falling relative to everything around it.
2. **Catalyst hunting (~30%).** Earnings in the next 10 sessions, scheduled
   economic releases, FDA dates, product launches, index rebalances, unlocks,
   court dates, regulatory deadlines. Dated events beat vibes.
3. **News and filings sweep (~20%).** Overnight news, 8-Ks, guidance changes,
   insider transactions, analyst moves that actually move price. `market_data.py
   analysts SYM` gives the recommendation trend across four months and the
   earnings surprise record — read the *change*, not the level. `market_data.py
   short SYM` gives short interest and days to cover, which matters in both
   directions: a crowded short is fuel under a long, and it is why a short idea
   can be right about the business and still lose.
4. **Durable mispricings (~15%).** The long-term lane, and the one most easily
   crowded out by the day's noise — so give it real time rather than whatever
   is left. What is structurally cheap or structurally favoured and likely to
   stay that way: a quality business de-rated on a temporary problem, a secular
   demand or supply imbalance with years to run, an asset repricing to a new
   monetary or regulatory regime. Read the actual filings. A holding you would
   be content to own through a 30% drawdown is worth more than a clever trade.
5. **Level-setting (~15%).** For each surviving candidate, pull real price
   history and set entry, target, and downside on actual support/resistance and
   ATR — not round numbers. For long-term ideas, anchor the target to a
   valuation you can defend and the downside to a stated bear case.

   Two things to check here that the report used to skip:

   - **What the options market already prices.** `market_data.py implied SYM
     --entry E --target T` returns the move priced by the at-the-money
     straddle, and how many of those moves your target sits away. Under 1.0 the
     market considers your target ordinary. Much above 2.0 you are not reading
     the market, you are disagreeing with it — which is allowed, but say so in
     the thesis and expect the red team to ask why.
   - **Where the entry sits relative to the market.** An entry below the market
     on a long only fills once the trade first goes against you, which selects
     for the ideas that were already failing. The first month was 31 pullback
     entries against 1 breakout, 42% of them ever filled, and the ones that did
     fill were the ones falling. The Performance tab now breaks fill rate and
     average move down by entry style. A pullback entry is fine when the level
     is real support you can point at; it is not fine as a reflex discount off
     the last print.
6. **Falsification (~10%).** For each finalist, argue the other side. Anything
   that does not survive gets demoted or cut. This step is not optional and is
   the first thing people skip.

These are proportions, not a schedule — a day with no earnings and a quiet
calendar should shift time from catalyst hunting into durable mispricings
rather than padding the trade lane with weak setups.

## Weekend behavior

US equities and futures are closed. A Saturday or Sunday run should shift
toward crypto and event contracts for actionable ideas, and treat equities as
week-ahead preparation — pre-positioning levels and the coming calendar rather
than same-day entries. Mark those `horizon: "swing"` and note that entry is for
the next open.
