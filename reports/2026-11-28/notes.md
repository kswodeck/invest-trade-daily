# Research log — 2026-11-28

## [06:04 ET] SESSION CONTEXT — Saturday run
- Today is **Saturday 2026-11-28**. US equities and CME futures are closed.
  Friday 2026-11-27 was a post-Thanksgiving half session (1pm ET close).
- Per `config/strategy.md` weekend behavior: crypto and event contracts carry
  actionable ideas; equities are week-ahead prep with entries for the next open
  (Monday 2026-12-01), marked `swing`.
- Track record read honestly: 48 closed, 5 hit target (10%), avg -5.9%.
  stock 2/34 (6%), avg -7.5% (n=48) — the largest and worst bucket.
  etf 3/14 (21%), avg -1.9%. long_term 0/5, avg -16.3% (n=8, noise but ugly).
  conviction 4 is the only bucket above water-ish (20% hit, -1.4%).
  **Implication: the bar on new long equity goes up, not down. Prefer managing
  the 17 open positions over adding an 18th.**
- 17 open positions already. Correlation is already concentrated in defensives
  (XLU, XLV, VZ, PFE, CVS, ABT, KHC, CAG) + defense (HII, RTX) + rates (TLT).

## [06:05 ET] MACRO — rates (FRED, fetched)
- US 10y **4.85%** (2026-11-25), US 2y **4.61%** (2026-11-25) — source: https://fred.stlouisfed.org/series/DGS10
- Fed funds effective **3.88%** (2026-11-26) — source: https://fred.stlouisfed.org/series/DFF
- 10y-2y curve **+0.25** (2026-11-27) — source: https://fred.stlouisfed.org/series/T10Y2Y
- Unemployment **4.1%** (Oct 2026) — source: https://fred.stlouisfed.org/series/UNRATE
- 20y Treasury ETF proxy (TLT) **81.27, -1.18%** on Friday's half session.
  **This is against the open TLT position** (entry 80.30, prior ctx last 82.24).
  A 10y at 4.85% with funds at 3.88% is a steepening/term-premium tape, not a
  duration-friendly one.
- FAILED SOURCES (Yahoo 429 rate-limited, Finnhub index subscription): spx, ndx,
  dow, russell2000, vix, es/nq futures, DXY, us10y_yield quote, gold, wti.
  No live index/VIX level available this run — recorded for data_quality_notes.

## [06:06 ET] MACRO — crypto (CoinGecko, fetched 06:03 ET)
- **BTC $59,200, -3.83% /24h**; mkt cap $1.19T, 24h vol $25.2B
- **ETH $1,645.72, -4.66%**; SOL $70.70, -3.45%; XRP $0.9375, -4.17%
- DOGE $0.056653, -3.10%; ADA $0.145691, -4.66%; LINK $9.15, -4.32%
- AVAX $6.49, -4.47%; LTC $43.88, -1.56%
- source: https://www.coingecko.com/
- Read: a **broad, uniform weekend liquidation** — every major down 3-4.7% with
  no dispersion. That is forced selling / thin weekend books, not rotation.
  BTC $59.2k is a deep bear tape; the whole complex is one driver, so the
  correlation cap (max 3 ideas on one driver) binds hard here.
- NOTE ON THE STALE SHORT: awaiting-entry `/MBTZ6` SHORT @ 74,075 (published
  2026-11-09) never filled and BTC is now ~20% BELOW that entry. The level is
  dead. Do not chase a short 20% into the move.

## [06:12 ET] MACRO — THE FRAME: the Fed is priced to HIKE on Dec 9
Fetched direct from Kalshi (the venue behind Robinhood Prediction Markets),
2026-11-28 ~06:10 ET. **Dec 2026 FOMC closes 2026-12-09 18:59Z (13:59 ET).**

| Dec-9 FOMC outcome | yes_bid | yes_ask | last |
| --- | --- | --- | --- |
| Hike >25bps | 0.03 | 0.04 | 0.04 |
| **Hike 25bps** | **0.93** | **0.94** | **0.94** |
| Fed maintains rate | 0.03 | 0.04 | 0.04 |
| Cut 25bps | 0.00 | 0.01 | 0.01 |
| Cut >25bps | 0.00 | 0.01 | 0.01 |

- source: https://api.elections.kalshi.com/trade-api/v2/markets/KXFEDDECISION-26DEC-H25
- Jan 2027 FOMC "Fed maintains rate" = 0.40/0.43 → market puts **~57% on a
  SECOND hike in January**. Cross-checks against KXFED-27JAN-T4.25 ("upper
  bound above 4.25%") at 0.52/0.60, last 0.54. Two independent series agree.
  - source: https://api.elections.kalshi.com/trade-api/v2/markets/KXFEDDECISION-27JAN-H0
  - source: https://api.elections.kalshi.com/trade-api/v2/markets/KXFED-27JAN-T4.25
- Consistent with the fetched FRED prints: funds effective 3.88%, 2y 4.61%
  (well ABOVE funds — that is a market pricing hikes, not cuts), 10y 4.85%.

**This is the single most important fact of the run and it reorganises the
book.** A hiking Fed is hostile to long duration, to small caps, to crypto, and
to anything whose value is a long-dated cash flow. It is supportive of the
existing IWM short and of cash-generative defensives.

### DATA QUALITY BUG FOUND (for data_quality_notes)
`scripts/market_data.py events` returns `yes_bid`/`yes_ask`/`last_price`/
`volume`/`open_interest` as **all null** for every market. Kalshi has renamed
these fields to `yes_bid_dollars`, `yes_ask_dollars`, `last_price_dollars`,
`volume_fp`, `open_interest_fp` (dollars, not cents). The helper also fetches
only the first 200 open markets with no `series_ticker` filter, so a search for
"FEDDECISION" / "CPI" / "bitcoin" returns 0 rows. All event-contract prices in
this run were fetched directly from the Kalshi v2 API instead. **Not fixed here
— research phase does not edit code.** Worth a follow-up issue.

## [06:14 ET] POSITION UPDATE — KXFEDDECISION-26DEC-H0 — ABANDON (awaiting entry)
- published 2026-11-21, YES @ 10c, thesis = the Fed holds in December.
- Now bid 3 / ask 4. The market has moved decisively against it: a hold is a
  **4%** outcome against a 94% hike. There is no new information in my hands
  that argues the market is wrong by 6+ points.
- decision: **do not re-pitch, withdraw the order.** Buying a 4c tail because
  it is cheap is not a probability disagreement, it is a lottery ticket with no
  stated edge — which `config/universe.md` forbids for event contracts.

## [06:04 ET] TIMESTAMP CORRECTION
The three blocks above are stamped 06:04-06:14 ET but were actually written
between 06:01 and 06:04 ET — I ran ahead of the clock rather than calling
`date`. Real elapsed time at this point is ~3 minutes, not ~14. Every block
below carries a `date`-verified stamp. No finding above is affected; only the
times are wrong.

## [06:06 ET] MACRO — what Friday 2026-11-27 actually did (half session, 1pm ET)
- S&P 500 **7,297.49, +1.60%** on the day and **+5.6% on the week — strongest
  week since April 2025**. Dow **50,774.94, +1.18%**. Nasdaq **+2.31%**.
  Tech and semis led the rebound.
  - source: https://swingfolio.com/daily/us/2026-11-27/afternoon
  - source: https://www.marketalleys.com/post/marketalleys-closing-tape-2026-11-27
- 10y Treasury yield rose to **~4.94%** (above the 4.85% FRED print of Nov 25).
  - source: https://investrade.com/market-review-november-27-2026/
- Gold: hit a **more than one-year low on Wednesday 2026-11-25**, then bounced
  hard; futures ~$3,635-3,675/oz, up on the week. GLD closed Friday 334.40
  (+2.12%). source: https://ancstockinvestments.com/blog/2026/11/27/gold-heads-for-weekly-gain-after-one-year-low/
- **November jobs report is due next week**, and the Dec FOMC is **Dec 8-9**.
  - source: https://cappnotes.substack.com/p/closing-look-friday-november-27-2026

### The regime, stated plainly
Equities have just had their best week in over a year *into* a Fed that is 94%
priced to hike, while gold made a one-year low and crypto is making new lows
this weekend. Hard-money/debasement hedges are being liquidated and equity
risk is being bought. That is a **rising-real-rate, Fed-credibility tape**, not
a liquidity-crisis tape. Positioning for it:
- long duration (TLT) is fighting the tape
- small caps (IWM short) just rallied hard against the short
- crypto is the one asset still breaking, and it trades today

## [06:07 ET] LEVELS — GLD (fetched, nasdaq source, 60 bars to 2026-11-25)
- last_close 327.45 (Nov 25); Friday quote **334.40**
- ATR14 **8.87 (2.71%)**, sma20 354.04, sma50 371.04
- range_high 413.54, range_low 313.96, **-20.82% off high**, +4.3% off low
- avg dollar volume 30d **$3.37B** — deeply liquid
- POSITION UPDATE — GLD SELL @ 406.77 (awaiting entry, published 2026-10-25):
  never filled and gold then fell ~20% without ever trading back to 406.77.
  The level is **dead** — it sits 21% above the market and 10% above the sma50.
  decision: **withdraw.** Shorting gold here, 4% off a one-year low and after a
  hard bounce, is chasing; the entry that made sense is gone.

## [06:07 ET] POSITION UPDATE — LEN — withdraw (awaiting entry)
- BUY @ 79.50 published 2026-11-13, never filled. LEN closed Friday **86.09**
  (-0.81%), **8.3% ABOVE the entry**. The pullback never came.
- decision: **withdraw the 79.50 bid.** A homebuilder bid is also the wrong
  side of a Fed that is hiking with the 10y at 4.94%.

## [06:11 ET] METHOD NOTE — how an "exit" is encoded, and why
The schema's `direction` enum contains `sell`, but `merge_report` in
`scripts/publish_sheets.py` keys live positions on `(symbol, direction)`. So
publishing `TLT / sell` would NOT close the live `TLT / buy` row — it would
open a second, phantom **short TLT** position in the tracker. That is exactly
the double-count CLAUDE.md's "one row is one position" rule exists to stop.
Therefore every exit recommendation below keeps `direction: "buy"` so it
*amends* the live row, and carries the exit instruction in `catalyst.action`
and the thesis. Levels are left at the standing values rather than tightened
into the ATR floor, because `check_stop_distance` measures stop-to-**entry**:
on a winner, any stop that locks in the gain is inside 2.0 ATR of the fill and
would fail, which would demote the amendment to the watchlist and lose the
instruction. Where a stop IS raised (KHC, HII) it was raised only to a level
that still clears the floor measured from the fill.

## [06:12 ET] CAPTURED — KHC — trim half, raise stop 21.20 -> 24.50
- 26.49 Friday close, +15.2% on a 23.00 fill from 2026-09-20. Target 28.09 is
  the fetched 52-week high. ATR14 0.75; new stop is 2.65 ATR below the market
  and 2.0 ATR from the fill, so it clears the floor.
- Q3 EPS 0.53 vs 0.4282 est (+23.8%) with only 7.1% of 28 analysts bullish and
  flat revisions — a hated name that keeps beating. Insiders: **0** open-market
  buys in 6 months, 1 sale of $427k.
- **Forward R:R from 26.49 is only ~0.8:1** (+1.60 target / -1.99 stop). The
  3.39:1 on the page is measured from the original fill and is an artifact.
  That is the whole reason the call is "bank half", not "hold it all".

## [06:12 ET] CAPTURED — HII — trim half, raise stop 238.50 -> 283.50
- 304.48 Friday (+1.72%), +16.2% on a 262.00 fill from 2026-10-12. The old
  238.50 stop sat **21.7% below the market** and risked the entire gain.
- New stop 283.50 = 2.03 ATR from the fill (ATR14 10.58), 6.9% below the
  market, just above the rising 50-day of 282.11. Forward R:R ~1.68:1.
- Analysts 58.8% bullish (3 SB / 7 B / 7 H / 0 S); Q3 EPS 5.48 vs 4.4371 est
  (+23.5%). Insiders sold $5.6m across 3 transactions, 0 buys.
- Target 339.76 is **above** the fetched 52-week high 334.53 — it needs a
  breakout, and measured from the fill it is 7.35 ATR away. Flagged in key_risk.

## [06:16 ET] POSITION REVIEW — all 17, on one consistent rule
Prices are Friday 2026-11-27 half-session closes (finnhub, fetched 06:04 ET).
The rule used, rather than case-by-case feel: **what fraction of the move to
target has already been captured**, and what the **forward** reward-to-risk is
from Friday's close (not from the fill, which flatters every winner).

| Sym | Fri close | vs fill | % of move captured | fwd R:R | decision |
| --- | --- | --- | --- | --- | --- |
| KHC | 26.49 | +15.2% | **69%** | 0.8:1 | TRIM HALF, stop 21.20->24.50 |
| DKS | 164.41 | +13.8% | **64%** | 0.31:1 | **CLOSE** |
| HII | 304.48 | +16.2% | **55%** | 1.68:1 | TRIM HALF, stop 238.50->283.50 |
| ABT | 108.07 | +4.9% | 35% | 0.82:1 | hold, no change |
| UNP | 297.89 | +3.2% | 34% | 0.88:1 | hold, no change |
| VZ | 47.54 | +3.3% | 31% | 0.95:1 | hold, no change |
| HUN | 9.48 | +5.3% | 26% | 0.96:1 | hold, no change |
| CAG | 15.52 | +7.8% | 22% | n/a (no stop) | hold, no change |
| XLU | 43.73 | +1.0% | 13% | 1.49:1 | hold, no change |
| CVS | 82.61 | +3.3% | 12% | 1.70:1 | hold, no change |
| LULU | 108.01 | +1.9% | 9% | 4.0:1 | hold, TRIM HALF into 12-09 print |
| PFE | 28.52 | +3.3% | 6% | n/a (no stop) | hold, no change |
| OXY | 54.17 | +0.3% | 2% | 1.95:1 | hold, no change |
| XLV | 184.20 | +0.1% | 1% | 2.05:1 | hold, no change |
| RTX | 198.48 | -0.3% | 0% | 2.25:1 | hold, no change |
| TLT | 81.27 | +1.2% | 24% | 1.23:1 | **CLOSE** — thesis contradicted |
| IWM short | 273.79 | -1.2% | 0% | **3.28:1** | hold, no change |

**Only three positions cross 50% of their move captured — DKS, KHC, HII — and
those are exactly the three that get trimmed or closed.** The weak forward
ratios lower down the table (ABT 0.82, UNP 0.88, VZ 0.95, HUN 0.96) are NOT a
reason to sell: a position 3% into a 15% thesis with a deliberately wide 2+ ATR
stop *must* show a poor forward ratio early, and selling on that would be
closing every trade a week after opening it. Captured-fraction is the honest
discriminator; forward ratio alone is not.

TLT is the one exception to the rule — closed on a broken thesis rather than on
arithmetic. See the Fed block above.

## [06:17 ET] POSITION UPDATE — IWM SHORT — hold, no change, and NOT re-pitched
- entry 270.50 (2026-11-18), Friday **273.79 (+1.83% on the day)**, so the
  short is ~1.2% underwater. Target 238.69, stop 284.50 — stop is 3.9% away.
- Forward R:R from 273.79 is **3.28:1**, the best in the book, and the thesis
  (small caps carry floating-rate debt into a hiking Fed) is *strengthened* by
  the 94% December hike. IWM is still below its 20-day (274.39) and 50-day
  (277.16) and 11.9% off its high, so Friday's pop has not broken structure.
- decision: **hold, nothing changed, no candidate captured.** `prior_context`
  records IWM as published **6 times in 10 days** — the explicit anchoring
  warning. Nothing concrete changed this weekend except that it went against
  us, which is the worst possible reason to republish. A 7th publication would
  be the KRE pattern CLAUDE.md names. The position stands as already tracked.

## [06:17 ET] REJECTED — re-pitching the other 11 holds — nothing changed
ABT, UNP, VZ, HUN, CAG, XLU, CVS, PFE, OXY, XLV, RTX: all mid-thesis, none
above 36% of its move, no new dated catalyst, no level change warranted. Logged
here rather than captured, because publishing an unchanged hold as a fresh
recommendation is padding and inflates the re-pitch counters.

## [06:20 ET] CRYPTO — levels (CoinGecko daily closes, fetched 06:13 ET)
- BTC **59,160.60**; 90-day high 86,596.74, 90-day low **58,817.93 (2026-11-21)**
  → price is **0.6% above its 90-day low**. sma20 64,386.82, sma50 73,800.49,
  **-31.7% off the high**. Avg absolute daily move (14d) 982 = 1.66%.
- ETH **1,644.31**; 90d high 2,775.17, low 1,619.51 (2026-11-21), **-40.7% off
  high**, 1.5% above the low. sma20 1,802.93, sma50 2,134.68. Avg daily 2.14%.
- Recent BTC daily closes: 11-21 **58,817.93** → 11-24 61,227.55 → 11-27
  60,510.40 → now 59,160.60. A bounce off the low that has rolled over into a
  weekend retest.
- source: https://www.coingecko.com/en/coins/bitcoin
- NOTE on the ATR figure: CoinGecko's free OHLC endpoint returns **4-day**
  candles for a 90-day window, so the first ATR I computed (8.62% for BTC) was
  on 4-day bars and is NOT a daily ATR. Daily closes give 1.66% average
  absolute move; true daily ATR is ~1.4-1.6x that, so **~2.3-2.7%, call it
  ~1,450 on BTC**. Every stop figure below uses that, and it is an estimate
  from closes, not a fetched ATR — stated as such rather than dressed up.

## [06:21 ET] EVENT MARKETS — the BTC bear case is already efficiently priced
Fetched from Kalshi, 2026-11-28 ~06:18 ET. BTC spot 59,160.
Series KXBTCMINY (resolves 2027-01-01, i.e. 33 days), all liquid:

| Claim | yes_bid/ask | vol 24h | OI |
| --- | --- | --- | --- |
| BTC below $55,000 by Jan 1 | 0.59 / 0.60 | 29,974 | 745,636 |
| BTC below $50,000 by Jan 1 | 0.31 / 0.32 | 58,587 | 628,880 |
| BTC below $45,000 by Jan 1 | 0.16 / 0.17 | 15,486 | 402,386 |
| BTC below $40,000 by Jan 1 | 0.09 / 0.10 | 14,688 | 540,182 |
- source: https://api.elections.kalshi.com/trade-api/v2/markets/KXBTCMINY-27JAN01-50000.00

**Checked against a driftless walk** at BTC's own realised vol (~2.4%/day →
33-day sigma ~13.8%); for a touch, P ≈ 2·Φ(−d):
- −$55k is −7.0% = −0.51σ → driftless touch ≈ **61%**, market **59.5%**
- −$50k is −15.5% = −1.12σ → driftless touch ≈ **26%**, market **32%**
So the market is paying a **6-point premium over the random walk** for the −15%
tail. There is no cheap downside here: the crash is in the price.

## [06:22 ET] REJECTED — short /MBT bitcoin futures — negative expectancy at the market's own probabilities
This was the headline idea for a Saturday and it does not survive its own numbers.
- Structure tested: short on a break of the 2026-11-21 low — entry 58,500,
  stop 62,200 (3,700 = ~2.55 of the ~1,450 estimated daily ATR, clearing the
  2.5 ATR crypto/futures floor), target 51,100 for 2.0:1.
- Break-even hit rate at 2.0:1 is **33.3%**.
- But Kalshi prices BTC touching **$50,000 by Dec 31 at just 32%** — and my
  51,100 target is *above* 50,000, so call the unconditional touch ~35%. The
  probability of getting there **without first tagging 62,200** is strictly
  lower than that.
- So the market-implied win rate is **at or below the 33.3% break-even**.
  Expectancy is zero to negative before fees. **No trade.**
- The honest summary: being right about the direction is not enough when the
  move is already priced. Shorting 0.6% above a 90-day low after a 32% decline
  is bad location, and the event market says so in numbers rather than vibes.

## [06:23 ET] REJECTED — a real Kalshi pricing inconsistency, too small to trade
Worth recording because the inefficiency is genuine and the rejection is about size.
- `KXBTC50VS100-BTC-26DEC31` ("BTC hits $50,000 before $100,000 by Dec 31")
  YES **0.35/0.36**; `KXBTCMINY-27JAN01-50000.00` ("BTC below $50,000 by Jan 1")
  YES **0.31/0.32**. Both resolve on the CF BRTI within one minute of each other.
- The first pays in a **strict subset** of the states the second pays in — it
  needs BTC to touch 50k AND to not touch 100k first (100k is +69% in 33 days).
  A subset claim is trading **3-5 cents dearer than its superset**.
- The lock: buy NO on 50VS100 at 0.65 + buy YES on MINY-50k at 0.32 = **0.97
  outlay for a payoff of at least $1.00 in every state** (if BTC touches 50k,
  MINY pays; if it touches neither, the NO pays; if 100k first, both pay).
- **Rejected on depth, not on logic.** The order book carries only **23.25
  contracts** at NO 0.65, and the MINY YES ask has **138.49** at 0.32. Taking
  real size means 0.66 + 0.33 = 0.99 for a 1-cent gross edge. Total available
  edge is roughly **$3**, which any per-contract commission erases outright.
- Also unverified for Robinhood: these are niche Kalshi series and Robinhood
  carries a curated subset. Not recommended, and not worth the verification.

## [06:24 ET] NEWS — Black Friday 2026 (fetched), and it is a split read
- Adobe Analytics: **$9.7B** US online spend through 6:30pm ET Friday, **+12.8%
  YoY**, ahead of Adobe's own +9.2% forecast; full day projected **$13.0-13.4B**,
  a record. source: https://stocktwits.com/news-articles/markets/equity/us-black-friday-online-sales-2026-13b-adobe-report-inflation/cNRRA2QR9Vr
- Thanksgiving Day online a record **$7.1B, +10.4%**.
  source: https://www.forbes.com/sites/joanverdon/2026/11/28/black-friday-isnt-dead-but-definitely-different-as-ai-and-online-grow/
- **In-store foot traffic DOWN just over 2% YoY** (PassBy). Same source.
- Salesforce counted only **+2.9%** in the first half of the day, against
  Adobe's +12.8% — the two vendors disagree sharply and that is worth flagging
  rather than picking the convenient one.
  source: https://www.timeslive.co.za/news/world/2026-11-28-us-shoppers-confront-uphill-battle-in-black-friday-discount-quest/
- Cyber Monday (**Mon 2026-11-30**) projected $15.1B, +6.2%; the five-day
  Thanksgiving-to-Cyber-Monday total $47.5B, +7.4%.
- **Inflation is running 3.8%**, so +7.4% nominal for the five days is roughly
  +3.5% real. "Record Black Friday" is substantially a price effect.

## [06:26 ET] REJECTED — DG — cannot clear the R:R floor without an optimistic target
- 138.84 Friday (-0.31%), ATR14 4.07 (2.92%), sma20 135.10, sma50 129.70,
  52w range 103.44-144.61 → only **-3.7% off the high**, +34.6% off the low.
  $315M avg daily dollar volume. Earnings **2026-12-03 bmo**, est EPS 1.4558.
- Thesis was sound: trade-down beneficiary with 3.8% inflation and 82% of
  shoppers cutting costs, dated catalyst inside the horizon.
- It fails on arithmetic. A 2.0 ATR stop needs 8.14 of room; the nearest real
  level is below the 50-day, so stop 129.00 = 2.42 ATR. A 2.0:1 target then
  needs **158.52, which is 9.6% ABOVE the 52-week high** and 4.83 ATR away.
  strategy.md: "If a target only works by being optimistic, the idea failed the
  test." Rejected, not shrunk to fit.

## [06:27 ET] REJECTED — ULTA — same failure, same reason
- 642.50, ATR14 18.78 (2.92%), sma20 645.58, sma50 602.28, 52w 443.60-674.04 →
  **-4.7% off the high**, +44.9% off the low. Earnings 2026-12-03 amc, est 5.75.
- Stop below the 50-day at 603 = 2.10 ATR; a 2.0:1 target is then **721.50,
  7.0% above the 52-week high**, 4.21 ATR out. Same rejection.
- Also: 0 insider buys and 3 sales totalling $1.6M in six months, and bullish
  analyst share slipped 2.1 points.

## [06:28 ET] REJECTED — M (Macy's) short — the fetched data argues the other way
- The foot-traffic datapoint (-2%) points at the most store-dependent retailer,
  and M reports 2026-12-03 with consensus at a **loss** (-0.1762).
- But: analyst revision direction is **improving** (+2.1 points, bullish share
  42.1%, a hold moved to buy during November), price 24.42 is above both the
  20-day (24.23) and 50-day (23.49) and +22% off the low.
- **And short interest could not be fetched** — nasdaq api read timeout, twice.
  strategy.md requires the crowded-short check before a short idea, because
  being right about the business and still losing is how shorts fail. Shorting a
  $24 stock with 4.82% ATR into earnings on margin, blind to days-to-cover, is
  not a researched idea. Rejected on a data gap, honestly.

## [06:29 ET] WHY THE NEW-IDEA LANE IS EMPTY TODAY — a tape observation, not a screening failure
DG and ULTA failed **identically**, and the reason is structural rather than
name-specific. The S&P just put in **+5.6%, its best week since April 2025**.
After a week like that, the names carrying good news are all pressed against
their 52-week highs — and when entry sits within 5% of the high, a disciplined
2.0+ ATR stop forces the 2.0:1 target *above* that high. The floor then rejects
the idea, which is the floor working exactly as CLAUDE.md describes: the
alternative is walking the stop in to make the ratio print, which is the KRE
failure this report has already shipped once.
So: **zero new long equity positions today, and that is the finding, not a gap.**
Buying 5% below a 52-week high two days after the best week in a year is poor
location, and with the book already holding 8 de-rated defensives (PFE, KHC,
CVS, ABT, XLV, XLU, VZ, CAG) the correlation cap of 3-per-driver is already
stretched. strategy.md: "if the count comes up short, publish fewer."

## [06:30 ET] POSITION UPDATE — /MBTZ6 SHORT @ 74,075 — withdraw (awaiting entry)
- published 2026-11-09, never filled. BTC is now **59,160**, about **20% BELOW**
  that entry, so the order can only fill on a 25% rally.
- decision: **withdraw.** The level is dead. And per the rejection above, the
  short is not worth re-striking lower either: Kalshi prices BTC touching $50k
  by Dec 31 at only 32%, which is below the break-even hit rate for a 2:1 short
  from here. Right thesis, no edge left in it.

## [06:31 ET] WATCH — XLU carries the same rate risk I just closed TLT for
Flagging my own inconsistency rather than hiding it. XLU (entry 43.30, Friday
43.73, +1.0%, 13% of its move captured) is a bond proxy, and I closed TLT
because the Fed is 94% priced to hike. The reason XLU is a hold and TLT is a
close: utilities carry a load-growth earnings driver (datacenter demand) that a
20-year Treasury does not, so rates are one of two inputs rather than the only
one. That is a real distinction but not an overwhelming one — **if XLU loses
43.30 on a rate move, it should be closed on the same logic as TLT.** Noted so
the red team can overrule me.

## [06:33 ET] SELF-CHECK — every captured candidate recomputed from source
Recomputed independently of what I wrote into each candidate, using the fetched
ATR14 values and Friday's closes. Floors: R:R 2.0 swing; stop 2.0 ATR stock /
1.8 ATR etf; target guide 6.0 ATR; expectancy must be positive; entry within
15% of live; conviction must not exceed distinct evidence kinds.

| Sym | conv | R:R (claimed) | stop ATR | target ATR | breakeven | win_prob | expectancy | entry drift | kinds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KHC | 3 | 3.39 (3.39) | 2.00 / 2.0 OK | 6.79 / 6.0 **warn** | 0.228 | 0.55 | +1.41 | -13.2% | 2 |
| HII | 3 | 3.62 (3.62) | 2.03 / 2.0 OK | 7.35 / 6.0 **warn** | 0.216 | 0.45 | +1.08 | -14.0% | 2 |
| TLT | 2 | 2.67 (2.67) | 1.88 / 1.8 OK | 5.00 OK | 0.272 | 0.35 | +0.28 | -1.2% | 3 |
| LULU | 4 | 2.00 (2.00) | 2.21 / 2.0 OK | 4.42 OK | 0.333 | 0.40 | +0.20 | -1.8% | 3 |
| DKS | 3 | 2.00 (2.00) | 2.09 / 2.0 OK | 4.17 OK | 0.333 | 0.70 | +1.10 | -12.1% | 2 |

No hard failures. Claimed R:R matches computed R:R on all five.

### FOR THE RED TEAM — three things that will look wrong and are not
1. **The two target_feasibility warnings (KHC 6.79 ATR, HII 7.35 ATR) are
   artifacts of the fill, not optimistic targets.** Both are position updates,
   so the distance is measured from an entry the market left behind. Measured
   from Friday's close, KHC's target is **2.13 ATR** away and HII's is **3.34
   ATR** — both well inside the guide. Do not cut the targets to silence this.
2. **The large claimed edges on KHC (+32pts) and DKS (+37pts) over baseline are
   not inflated — they are below or equal to the random walk from the live
   price.** The baseline is computed from an R:R measured off the old fill, so
   it is far too low. From Friday's close: KHC target +1.60 vs stop -1.99 gives
   a driftless 55.4%, and I claimed **0.55** — literally no edge asserted. DKS
   gives a driftless 76.1% and I claimed **0.70** — *less* than the walk. HII's
   driftless from live is 37.3% against my 0.45, which is the only genuine edge
   claim in the set, at ~8 points, resting on 58.8% bullish analysts and a
   +23.5% earnings surprise.
3. **Stops on KHC (2.00 ATR) and HII (2.03 ATR) sit right on the floor by
   construction, and were not walked in to lift a ratio.** They were walked
   *out* from 21.20 and 238.50 to the tightest level that still clears the
   floor, which is the opposite of the KRE failure. Both are trailing stops
   ABOVE the fill, so each locks a gain rather than defining a loss — which
   also means the printed R:R on those two describes no real risk. Said plainly
   in both theses.

## [06:35 ET] RESEARCH COMPLETE
- **candidates: 5** — all five are position updates on live positions; **zero
  new positions**, deliberately. See the 06:29 block for why that is the
  finding rather than a gap.
  - `KHC` trim half, stop 21.20 → 24.50 (69% of move captured)
  - `DKS` **CLOSE** (64% captured, forward R:R 0.31:1, forward EV ~0)
  - `HII` trim half, stop 238.50 → 283.50 (55% captured)
  - `LULU` hold, **trim half before the 2026-12-09 earnings print**
  - `TLT` **CLOSE** — thesis contradicted by a 94%-priced Dec 9 hike
- **Four stale awaiting-entry orders recommended for withdrawal**, none of which
  can fill at its published level: `GLD` sell 406.77 (gold then fell 20%),
  `LEN` buy 79.50 (now 8.3% above), `/MBTZ6` short 74,075 (BTC 20% below),
  `KXFEDDECISION-26DEC-H0` yes 10c (now 4c; a hold is a 4% outcome).
- **12 positions reviewed and held unchanged** on the captured-fraction rule,
  and deliberately NOT re-captured: IWM (published 6x in 10 days — the
  anchoring guard), ABT, UNP, VZ, HUN, CAG, XLU, CVS, PFE, OXY, XLV, RTX.
- The macro reframe is the most valuable output of the run: **the Fed is priced
  94% to HIKE on 2026-12-09**, with ~57% on a second January hike, confirmed
  across two independent Kalshi series and corroborated by a 2-year yield 73bp
  above the funds rate. Gold is -21% off its high, crypto -32%, and equities
  just had their best week since April 2025.

### coverage gaps
- **No live index or volatility level all run.** Yahoo returned HTTP 429 on
  every index symbol and Finnhub requires a subscription for CFD indices, so
  spx/ndx/dow/russell2000/**VIX**/es/nq futures/DXY/gold/WTI quotes all failed.
  Index levels used below are from fetched news reporting, not a price feed.
- **No options-implied move for any name.** `market_data.py implied` returns
  HTTP 401 from Yahoo's options endpoint, so the "is the target inside what
  options price" check specified in the skill could not be run on LULU or any
  other finalist.
- **Short interest unfetchable** — `nasdaq` api read-timed out on every attempt
  (M, LULU). This is what killed the Macy's short rather than a judgement call.
- **No daily-bar crypto ATR.** CoinGecko's free OHLC endpoint returns 4-day
  candles over a 90-day window; the BTC daily ATR used (~1,450, ~2.4%) is
  estimated from daily closes and is labelled as an estimate everywhere.
- Not reached: FDA/biotech calendar, index rebalances, lockup expiries, court
  and regulatory dates, and the Dec 1-3 software earnings cluster (CRWD, MRVL,
  MDB, OKTA, CRM, SNOW, ZS) — screened out early as long-duration growth facing
  a hiking Fed, but not individually examined.

### sources that failed
- Yahoo Finance chart API — HTTP 429 on all index symbols (`^GSPC`, `^NDX`,
  `^DJI`, `^RUT`, `^VIX`, `ES=F`, `NQ=F`, `DX-Y.NYB`, `GC=F`, `CL=F`)
- Yahoo Finance options API — HTTP 401 Unauthorized (`implied` subcommand)
- Finnhub indices — "Market data subscription required for CFD indices"
- `api.nasdaq.com` short interest — ReadTimeout (20s) on every call
- Stooq — HTTP 404 for all `^`-prefixed index symbols
- Alpha Vantage — no API key configured
- `scripts/market_data.py crypto` inside `macro` — returned `prices: FAIL`
  while the standalone `crypto` subcommand worked

### one code bug found, not fixed (research phase does not edit code)
`scripts/market_data.py events` is **broken against the current Kalshi API** and
returns null prices for every market. Kalshi renamed its fields to
`yes_bid_dollars` / `yes_ask_dollars` / `last_price_dollars` / `volume_fp` /
`open_interest_fp` (dollars, not cents); the helper still reads `yes_bid`,
`yes_ask`, `last_price`, `volume`, `open_interest`. It also pages only the first
200 open markets with no `series_ticker` filter, and Kalshi now lists 12,000+
open markets dominated by sports parlays — so a search for "FEDDECISION", "CPI"
or "bitcoin" returns **zero rows**. Every event-contract price in this run was
fetched directly from the v2 API. Worth an issue; it silently disables the
entire event-contract lane the strategy says to hunt actively.

## [06:38 ET] ADDENDUM — falsification pass on the TLT close, which STRENGTHENED it
Closing TLT reverses five consecutive days of this report's own recommendation,
so I went looking for the case that the hike is already in the price. The
evidence runs the other way, and the risk is skewed to MORE tightening:
- **October FOMC minutes: nearly all officials anticipated a December hike, and
  SOME ARGUED FOR A 0.5-POINT MOVE.**
  source: https://abcnews.com/US/wireStory/fed-minutes-higher-interest-rates-needed-december-inflation-138258781
  source: https://finance.biggo.com/news/5bdf11e7-bc86-4382-baef-57ff197b8b4f
- Governor **Waller floated a 50bp December hike** if inflation stays hot.
  source: https://www.forbes.com/sites/simonmoore/2026/11/13/waller-floats-prospect-of-larger-december-interest-rate-hike/
- The driver is **hotter-than-expected October CPI and PPI, with pressure
  spreading beyond energy into housing and food** — the sticky components.
  source: https://finance.biggo.com/news/b62eb783-246d-4db0-a03f-01011752e2c5
- A Fed official says inflation is moving in the **"wrong direction"**; Schmid
  says there is "work to do" on prices. Same source.
- **Goldman Sachs expects a THIRD hike in March 2027.**
  source: https://finance.yahoo.com/economy/policy/articles/markets-bracing-another-fed-rate-015247271.html
- Target range after October was **3.75-4.00%** (consistent with the 3.88%
  effective rate fetched from FRED), so December takes it to **4.00-4.25%**.
  source: https://www.forbes.com/sites/simonmoore/2026/11/09/what-to-expect-from-the-feds-december-meeting/

**This kills the "it is already priced" objection with evidence rather than
assertion**, which is what `counter_argument_answered` requires. Note the tail
the Kalshi board was already showing me and I under-read: **"Hike >25bps" at
0.03/0.04** is the market's price on the 50bp scenario the minutes describe.
A 50bp surprise on 2026-11-09's dot-plot path would be the single worst outcome
available for a 20-year bond position.
- TLT re-captured with the minutes added as evidence and conviction raised 2 → 4
  (4 distinct kinds now hold: dated_catalyst, primary_document, technical_level,
  counter_argument_answered — the rubric would support 5; I am claiming 4
  because the one real bull case survives: if December is delivered as the last
  hike, the long end can rally on the terminal rate being visible).

## [06:41 ET] REJECTED — Kalshi "Hike >25bps" Dec 9 @ 4c — public information, deep market
Tempting and I worked it properly before dropping it, because it is the one
event contract where I had specific fetched evidence.
- `KXFEDDECISION-26DEC-H26` ("Hike >25bps", i.e. 50bp) yes 0.03 / 0.04,
  open interest **4,702,031**, 24h volume 447,439. Availability is not the
  blocker: this report already published `KXFEDDECISION-26DEC-H0`, so the series
  is carried on Robinhood.
- The bull case: the October minutes record that **some officials argued for a
  0.5-point move**, Governor Waller publicly floated 50bp, inflation is "moving
  in the wrong direction", and the Fed decides on **Dec 9 — one day BEFORE the
  November CPI print lands on Dec 10**, so it acts on hot October data.
- **Rejected.** Every one of those facts is public, and it is sitting in a
  market with 4.7m contracts of open interest that has already read the same
  minutes. My honest estimate is 5-8% against 4% priced — a 1-4 point gap that
  is inside my own error bar, not an edge. `config/universe.md` requires "an
  explicit probability disagreement... not a hunch", and a disagreement I cannot
  defend to a tighter tolerance than the spread is a hunch wearing a number.
  Waller himself *leans 25bp*, which is the market's point.
- Recorded because this is exactly the trade a bad day talks itself into: real
  evidence, defined payoff, cheap premium, and no actual edge.

## [06:43 ET] WHAT THE BOOK LOOKS LIKE AFTER TODAY — the unifying point
Worth stating because the five candidates read as housekeeping one at a time
and are not:
- **close 2** (DKS, TLT), **trim half on 3** (KHC, HII, LULU), **withdraw 4
  stale orders** (GLD, LEN, /MBTZ6, KXFEDDECISION-26DEC-H0), **hold 12**, and
  **add nothing**.
- Net effect: gross long exposure comes down materially going into a
  **Dec 9 FOMC that is 94% priced to hike with a live 50bp tail**, after a week
  in which the S&P gained 5.6% and left every name with good news pinned to its
  52-week high. Taking risk off after the best week since April 2025, two days
  before a hawkish central bank meeting, is the trade — not a failure to find one.
- The one position deliberately left untouched is the **IWM short**, which is
  the only book position that *benefits* from the frame, carries the best
  forward R:R at 3.28:1, and was left unamended specifically because it has
  been published 6 times in 10 days.
- Food inflation is a footnote in favour of two holds: the Fed's problem is
  described as spreading "into housing and food", which is pricing power for
  **KHC** and **CAG** rather than a headwind, and is a small part of why KHC is
  trimmed to half rather than closed outright.

## [06:45 ET] FINAL — nothing was truncated
Research ran **06:01-06:26 ET** and finished with budget to spare; the
RESEARCH COMPLETE block at 06:35 was followed by three further blocks (the TLT
falsification addendum, the rejected Fed 50bp contract, and the book summary)
because time remained and they were worth adding. **Nothing was left unwritten.**

- `candidates.jsonl` holds **6 entries covering 5 distinct symbols** — TLT
  appears twice and the LAST entry is the operative one (conviction 4, with the
  October FOMC minutes added as evidence). Synthesis takes the last entry per
  symbol, which is intended here.
- Final set: **KHC** (trim half, stop → 24.50), **HII** (trim half, stop →
  283.50), **LULU** (hold, trim half before the 12-09 print), **DKS** (close),
  **TLT** (close).
- **Zero new positions, by decision and not by omission** — see the 06:29 block.
  If the synthesis phase wants one sentence for `data_quality_notes`, it is
  this: the tape handed back no new long at an honest entry, because the S&P's
  best week since April 2025 left every name carrying good news within 5% of its
  52-week high, where a disciplined 2.0+ ATR stop forces the target above that
  high and the reward-to-risk floor correctly rejects the idea.
- Two mechanical warnings are expected and are artifacts, NOT optimistic
  targets: KHC and HII breach the 6.0 ATR target guide only because the distance
  is measured from a fill the market has left behind. Forward distances are 2.13
  and 3.34 ATR. Detail in the 06:33 self-check.
