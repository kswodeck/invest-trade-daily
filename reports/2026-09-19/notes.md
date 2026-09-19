# Research log — 2026-09-19

## [06:02 ET] MACRO — rates, crypto, session state
- **Saturday run.** US equities and futures CLOSED. Per config/strategy.md weekend
  behavior: crypto + event contracts carry actionable ideas; equities are
  week-ahead prep priced off the 2026-09-18 close (a closed market, not stale).
- FRED US10Y **4.94%** (2026-09-17); US2Y **4.67%**; 10y-2y curve **+0.25**;
  fed funds effective **3.88%** (2026-09-17) — source: https://fred.stlouisfed.org/
- Unemployment **4.1%** (2026-08); CPI index 334.131 (2026-08) — source: FRED
- 10Y at 4.94% against 3.88% effective funds = the long end is pricing term
  premium / inflation, not cuts. That is the frame for everything rate-sensitive.
- TLT **81.25** close 2026-09-18, -0.65% — source: market_data.py macro (stooq)
- Crypto (CoinGecko, live 24/7): BTC **81,305** +4.04% 24h; ETH **2,641.63**
  +5.39%; SOL **111.89** +5.22%. Broad risk-on bid across majors overnight.
- FAILED SOURCES (Yahoo 429 + finnhub index entitlement): ^GSPC, ^NDX, ^DJI,
  ^RUT, ^VIX, ES, NQ, DXY, ^TNX, gold, WTI all returned ok:false. No live index,
  VIX, dollar or commodity level available this run. Recorded for data_quality_notes.

## [06:02 ET] CALENDAR — earnings inside 10 sessions (finnhub)
- 09-22: AZO (bmo), FERG, KBH, THO, WOR, MLKN
- 09-23: CTAS, PAYX, SFIX, FUL, MANU
- 09-24: COST, DRI, BXMT, SNX, SCHL
- 09-25: UEC  <- uranium; CCJ is an open position
- 09-28: NKE <- open NKE position both sides; also CCL, MTN
- 09-29: KMX, CAG, CNXC
- 09-30: MU <- MU BUY @960 is awaiting entry; also JBL, JEF, FDS, CALM

## [06:07 ET] DATA GAP — event contracts unusable this run
- `market_data.py events` returns count=0 for Fed, FOMC, CPI, inflation, interest
  rate, recession, GDP, unemployment, oil price, S&P, Bitcoin. An empty query
  returns 40 rows, all multi-leg SPORTS parlays, every one with
  yes_bid/yes_ask/last_price/volume = **null**.
- So there is no fetched price for any macro event contract this run. Per the
  no-fabricated-numbers rule I am recommending **zero event contracts today**
  rather than quoting an implied probability I did not fetch. This is a source
  failure, not an absence of opportunity — flag in data_quality_notes.
- Consequence for the 3 open event positions (KXFEDDECISION-26SEP-H25 @32,
  -26OCT-H25 @28, -26SEP-H0 @47): I cannot mark or update them. The 26SEP
  contracts reference a September FOMC that has already passed; they need
  resolution checked by a run with a working feed.

## [06:07 ET] POSITION UPDATE — NKE — opened 2026-08-17 @ 40.75, now 35.51 (-12.8%)
- decision: **CLOSE the long** before the 2026-09-28 print
- why: fresh 150-day low (35.51 close vs 35.50 prior range low) — no measurable
  support beneath; below sma20 38.00 and sma50 40.45, both falling; original
  62 target is +75% from here; position carries NO stop
- an open NKE SELL from 2026-09-08 @ 38.40 (+5.3%) already banked part of this
- action: captured via add_candidate.py (sell, conviction 3)
- source: https://api.nasdaq.com/api/quote/NKE/historical

## [06:07 ET] LEVELS — reference closes, all 2026-09-18 (market closed)
| Sym | Close | ATR14 | ATR% | SMA20 | SMA50 | 150d hi | 150d lo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NKE | 35.51 | 0.89 | 2.51 | 38.00 | 40.45 | 68.49 | 35.50 |
| MU | 1015.80 | 42.97 | 4.23 | 959.60 | 927.26 | 1255.00 | 311.49 |
| UEC | 9.81 | 0.58 | 5.91 | 11.58 | 10.84 | 16.84 | 8.905 |
| COST | 895.31 | 12.53 | 1.40 | 924.60 | 936.54 | 1096.50 | 888.04 |
| KMX | 57.21 | 1.77 | 3.09 | 61.30 | 59.31 | 65.28 | 35.17 |
| CCJ | 91.62 | 3.38 | 3.68 | 98.72 | 94.79 | 131.21 | 83.15 |
| GLD | 401.17 | 7.65 | 1.91 | 406.62 | 392.97 | 492.15 | 363.32 |
| TLT | 81.25 | 0.69 | 0.85 | 81.96 | 82.61 | 90.86 | 80.46 |
| SLV | 59.93 | 1.75 | 2.93 | 59.76 | 56.82 | 85.27 | 49.61 |
| IBIT | 46.02 | 1.44 | 3.13 | 44.34 | 39.71 | 46.56 | 32.84 |
- source: https://api.nasdaq.com/api/quote/<SYM>/historical

## [06:08 ET] CRYPTO — BTC structure, and why it is REJECTED
- BTC live **81,305** +4.04% 24h (CoinGecko, fetched 06:01 ET). ETH 2,641.63 +5.39%,
  SOL 111.89 +5.22%.
- Structure from CoinGecko OHLC (4-day bars, 180d): BTC gapped out of a 62-67k
  range on the 2026-08-23 bar (64,686 open -> 79,320 high). Since 08-24 it has
  consolidated in **75,038 - 82,108** for roughly four weeks. 81,305 is the top
  of that range. — source: https://api.coingecko.com/api/v3/coins/bitcoin/ohlc
- Daily ATR: CoinGecko free tier only serves 4-day bars at this window, so the
  4,181 figure it implies is a 4-BAR range, not a daily one — not usable as ATR.
  Using IBIT's real daily bars instead: ATR14 3.13% of price = **~2,545/day** on
  BTC at 81,305. — source: https://api.nasdaq.com/api/quote/IBIT/historical
- ## [06:08 ET] REJECTED — BTC (and /MBT) long — breakout fails the R:R floor at an honest stop
  - Setup would be: buy the break of 82,108, stop below the four-week range low
    75,038 (say 74,800 — a structural level, not a round number).
  - Entry 82,200, stop 74,800 = 7,400 risk = **2.9 ATR**, which correctly clears
    the 2.5 ATR crypto floor.
  - Measured move = range width 7,070 added to 82,108 = **~89,200** target.
  - R:R = 6,800 / 7,400 = **0.92**. Floor for a crypto swing is 2.0. It fails.
  - To reach 2.0 I would need a 97,000 target (+18%) or a stop inside the range.
    Both are reverse-engineering — per config/strategy.md, "if an idea only
    clears the floor with a tight stop, the idea failed the floor." Dropped.
  - This is the one lane that trades today, and it does not clear the bar. Saying
    so beats publishing a 0.92:1 crypto trade because it is Saturday.
- **Stale short levels flagged:** the awaiting-entry `BTC` SELL @ 63,400 and
  `/MBTU6` SHORT @ 64,340 are 28% and 26% below spot and pre-date the 08-23
  breakout. They are dead, not pending. `/MBTU6` is additionally a September
  contract now inside its final trading period. Neither should be re-pitched.

## [06:08 ET] POSITION UPDATE — MU — published 2026-09-18 @ 960, never filled
- decision: **hold the 960 level UNCHANGED**; do not chase 1015.80
- why: 960 is the sma20 (959.60) with a 902-928 shelf beneath it from 09-14/15/16.
  MU ran 924 -> 1015.80 in four sessions. Raising the entry to market would mean
  buying a 4.23%-ATR semi at a four-session high nine sessions before it reports.
- stop 870 = 2.09 ATR below entry; target 1140 gives exactly 2.0:1; 150d high 1255
- earnings **2026-09-30** confirmed on the fetched calendar
- action: captured via add_candidate.py (buy, conviction 4)

## [06:08 ET] POSITION UPDATE — CCJ — opened 2026-08-17 @ 94.0, now 91.62 (-2.5%)
- decision: **hold, no change** — no candidate emitted, nothing to amend
- why: the stop at 82.50 is already correctly placed just below the 150-day low
  of 83.15, which is 2.7 ATR (ATR14 3.38) below spot. The sector is weakening —
  UEC broke to 9.81 on 09-18, 41.8% off its high and below both averages — and
  CCJ missed by 52.7% last quarter (0.18 vs 0.38 est). That is real deterioration,
  but it is deterioration the existing stop already governs. Tightening the stop
  here would be the KRE mistake: improving the ratio by making the trade worse.
- sources: https://api.nasdaq.com/api/quote/CCJ/historical,
  https://finnhub.io/api/v1/stock/recommendation

## [06:08 ET] REJECTED — COST — de-rating, not de-rated; earnings 09-24 in 3 sessions
- 895.31, 18.4% off high, 0.8% off the 150-day low (888.04), below sma20 924.60
  and sma50 936.54. Looks like a quality-name discount until you check the rest:
- lagging SPY on **every** window measured (-5.5% 1m, -7.9% 3m, -23.6% 6m) and
  lagging its own sector XLP too (-2.1%/-5.3%/-9.2%) — source: relstrength
- insiders: **zero** open-market buys in 6 months, 2 sells ($1.54M) — no
  confirmation from the people who would know it was cheap
- missed last quarter (4.93 vs 5.03 est) and earnings land 09-24, 3 sessions out
- at 397B cap on ~443.5M shares and roughly 20/share of annualised earnings it is
  near 45x — I cannot defend a valuation anchor that says this is cheap, and a
  long_term idea without one is not researched enough to publish
- verdict: no long. Not a short either — I have no bear catalyst, only weakness.

## [06:09 ET] NOTE ON TIMESTAMPS
- Blocks above originally carried estimated clock times. Corrected against `date`
  at 06:08:13 ET — the run is far ahead of where I assumed it was. All timestamps
  from here are read from the clock, not estimated.

## [06:14 ET] MACRO READ — what the sector tape actually says
Sector ETFs, all 2026-09-18 closes — source: https://api.nasdaq.com/api/quote/<SYM>/historical
| ETF | Close | vs sma20 | vs sma50 | off 150d high |
| --- | --- | --- | --- | --- |
| XLK | 189.60 | above (185.37) | above (183.12) | -4.6% |
| SMH | 573.00 | above (557.82) | below (564.78) | -14.7% |
| XLV | 168.39 | below (170.29) | above (166.75) | -4.7% |
| XLF | 55.86 | below (57.38) | below (57.18) | -4.7% |
| XLU | 41.10 | below (42.54) | below (43.82) | -14.0%, **at its 150d low 41.08** |
- One coherent regime: **10Y at 4.94% against 3.88% effective funds**, utilities
  (the bond proxy) at their lows, financials weak on credit stress, and mega-cap
  tech the only thing holding near highs. Hard assets bid overnight (BTC +4%).
- This explains CEG (-13% in 7 sessions) as sector, not company.
- **It also explains why so little clears the bar today** — see the rejections
  below. In a de-rating tape, longs in broken names cannot clear 2:1 once the
  stop is placed honestly beyond the low they are sitting on.

## [06:14 ET] REJECTED — four longs that failed the R:R floor at an honest stop
All four have the identical failure: the stop must sit beyond an extreme the
name is already sitting on, which makes the risk wide, and the 2.0x target then
lands above every piece of real structure. Reverse-engineering either leg is
what config/strategy.md forbids.
- **AZO** — 2855.31, printed a reversal bar off the exact **400-day low 2815.00**
  on 09-18 (o 2825.28 / l 2815.00 / c 2855.31), earnings 09-22 bmo. Honest stop
  below 2815 = 2720 (135 risk, 2.10 ATR). 2.0x needs **3125**; the highest high
  since 08-25 is 3046.47 and every rally since has made a lower high. Nearest
  real resistance 2974 gives **0.88:1**. Insider buy is stale — 2026-05-29 at
  2987, one buyer, now underwater.
- **IYR** — 98.00, the awaiting-entry SELL_SHORT @103.60 never filled because the
  move happened without us. Honest stop above sma20 101.92 = 102.10 (3.50 risk,
  2.75 ATR). 2.0x needs **91.60**, below the 150-day low of 92.45 — a 6.5% fall
  in a 1.3%-ATR ETF. Best structural target 92.60 gives **1.71:1**. Rejected.
- **SLV** — 59.93. Silver fell 109.83 to 49.61 over 200 days and is bouncing, not
  trending. Stop 55.90 below the 09-16 low (4.03 risk, 2.30 ATR). 2.0x needs
  **68.00**; nearest real resistance is the 08-21 high 63.20 = **0.81:1**.
  Would also have been a second precious-metals bet alongside the open GLD.
- **JEF** — 47.90, -13% in 7 sessions. Rejected on cause, not levels: First
  Brands exposure with ~$715M owed to its Point Bonita unit, an August securities
  investigation, a Morgan Stanley downgrade on credit. Sumitomo Mitsui bought
  $629M of stock (07-15 at 53.96, 05-01 at 48.22) and is underwater, but SMFG is
  a contractual alliance partner accumulating to a target stake, not a price
  signal. Unquantifiable credit risk into a 09-30 print. No.
  - sources: https://seekingalpha.com/article/4830761-jefferies-stock-drop-on-credit-cockroaches-looks-like-fear-selling-still-a-buy
    https://www.investing.com/news/analyst-ratings/morgan-stanley-downgrades-jefferies-stock-rating-on-credit-concerns-93CH-4549046
- **CTAS / PAYX** — both below sma20 and sma50, ~9-10% off highs, into 09-23
  prints. CTAS missed 3 of its last 4 quarters; PAYX bullish share is **8.3%**.
  No edge either way. Rejected.

## [06:15 ET] SYSTEMIC FINDING — five open longs carry NO STOP
NKE, LULU, LCII, BCC and PFE were all published without a stop, and the three
that are deepest underwater are three of those five: LULU -14.7%, NKE -12.8%,
LCII -8.9%. That is not coincidence — a position with no stop is one that
nothing can demote, so it stays in the book while it decays. All three are also
sitting within 3% of a 150-day low. Acting on all three today.

## [06:15 ET] POSITION UPDATE — LULU — opened 2026-08-22 @ 115.0, now 98.06 (-14.7%)
- decision: **CLOSE the remainder** (an open LULU SELL from 09-08 @ 100.61 began it)
- why: no stop; 2.8% off the 150-day low 95.35; -49% off the high; sma20 109.30
  and sma50 115.38 both above and falling; September made lower highs every
  session; 180 target implies +84%; ATR 5.7% a day
- action: captured via add_candidate.py (sell, conviction 3)

## [06:15 ET] POSITION UPDATE — LCII — opened 2026-08-18 @ 94.0, now 85.60 (-8.9%)
- decision: **CLOSE before THO reports 2026-09-22**
- why: no stop; 0.6% off the 150-day low 85.07; -46% off the high; LCII supplies
  RV OEMs and Thor reports in 2 sessions; THO is itself 0.68% off its 150-day low
- action: captured via add_candidate.py (sell, conviction 3)

## [06:15 ET] POSITION UPDATE — DINO — opened 2026-08-22 @ 107.5, now 115.90 (+7.8%)
- decision: **HOLD, no change** — the best open position in the book
- why: 115.90 is 1.53% off its 150-day high (117.70), far above sma20 104.99 and
  sma50 95.06, +146.6% off the 150-day low. Target 128 is still 10.4% away and
  above the high, so it is a live objective, not a stale one.
- **deliberately NOT trailing the stop.** Raising 97.75 to protect the gain would
  put the stop inside 2.0 ATR of the 107.50 entry (2.0 ATR = 8.72, so any stop
  above 98.78 fails the floor) and would lift the published R:R while making the
  trade worse — the KRE mistake in config/strategy.md. Stop stays 97.75 (2.24 ATR).

## [06:15 ET] POSITION UPDATE — no-change holds, with reasons
- `XLE` 64.31 vs entry 63.90 (+0.6%): above sma20 64.11, 2.8% off high. Hold.
- `GLD` 401.17 vs entry 398.00 (+0.8%): above sma50 392.97, stop 381 is 2.6 ATR
  below spot. Hold. Gold fell 509.70 to 363.32 over 200 days and is recovering —
  the position is fine, but this is a bounce, not a trend. No new metals exposure.
- `TLT` SELL 81.78 vs entry 81.87 (+0.1%): the short is right on the macro —
  10Y 4.94%. TLT 81.25 close, 0.98% off its 150-day low 80.46. Target 78, stop
  83.30 (2.96 ATR). Hold unchanged.
- `DVN` 48.61 vs entry 49.60 (-2.0%): at sma20 48.67, stop 46.90 is 1.25 ATR —
  thin, but it is a filled position and tightening is not the fix. Hold.
- `EEM` 67.03 vs entry 65.60 (+2.2%): at sma20 67.15. Hold.
- `PFE` 27.66 vs entry 27.60 (+0.2%): flat, no stop, 5.3% off high. Hold — but
  it is one of the five stopless longs and should be given one.
- `BCC` 75.69 vs entry 76.50 (-1.1%): no stop, below both averages but 16% above
  its 150-day low, so not the same emergency as NKE/LULU/LCII. Hold, needs a stop.
- `SVRA` 5.37 vs entry 5.35 (+0.4%): stop 4.60 intact, 14% off its low. Hold.
- **CORRELATION NOTE:** XLE, DINO and DVN are three open positions on one crude
  driver — at the cap of 3 in config/strategy.md. No new energy idea today.

## [06:16 ET] TIMESTAMP CORRECTION (second)
- Blocks written between 06:09 and 06:15 again carried estimated times, corrected
  against `date`. The run is much faster than my sense of it. Remaining entries
  read the clock in the same command that writes them.

## [06:22 ET] METHOD NOTE — finnhub pbAnnual is NOT a current P/B
Finnhub's `pbAnnual` is priced at the company's fiscal-year end, not today.
DINO shows pbAnnual 0.92 against a quarterly book of 57.85 and a 115.90 close —
a true current P/B of 2.00. Using pbAnnual would have called DINO a
below-book value stock while it trades at twice book. **Current P/B must be
computed as fetched price / `bookValuePerShareQuarterly`.** That is how the THO
number below was derived. Source:
https://finnhub.io/api/v1/stock/metric?symbol=<SYM>&metric=all

## [06:22 ET] VALUE SCREEN — current P/B, computed price / quarterly book
| Sym | Price | Book/sh | **P/B** | D/E | ROE | NetMgn | CurR | DivY | Earnings |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KBH | 47.12 | 61.93 | **0.76** | 0.52 | 7.04 | 4.94% | 6.61 | 1.51% | 09-22 |
| THO | 67.77 | 82.88 | **0.82** | 0.22 | 6.10 | 2.67% | 1.71 | 1.90% | 09-22 |
| SCHL | 34.75 | 40.15 | **0.87** | 0.15 | 6.61 | 3.58% | 1.23 | 2.00% | 09-24 |
| MLKN | 20.66 | 19.69 | 1.05 | 0.96 | 6.94 | 2.38% | 1.58 | 2.93% | 09-22 |
| CAG | 15.13 | 13.29 | 1.14 | 1.14 | -24.3 | -17.0% | 0.90 | 4.91% | 09-29 |
| BCC | 75.69 | 57.99 | 1.31 | 0.24 | 5.12 | 1.64% | 2.71 | 0.70% | — |
| KMX | 57.21 | 43.12 | 1.33 | 2.99 | 3.67 | 0.84% | 2.70 | — | 09-29 |
| LCII | 85.60 | 58.89 | 1.45 | 0.60 | 15.25 | 5.24% | 2.49 | 3.75% | — |
| DINO | 115.90 | 57.85 | 2.00 | 0.28 | 19.86 | 6.31% | 1.97 | 3.32% | — |
- **THO taken** as the long_term idea — see the candidate. It is not the cheapest
  on book, it is the cheapest one that can survive being wrong: D/E 0.2185 against
  KBH's 0.52 and MLKN's 0.96, with a covered 1.90% dividend.

## [06:22 ET] REJECTED — KBH — cheapest on book, but it contradicts an open position
- 0.76x book, D/E 0.52, P/E 10.94, current ratio 6.61, earnings 09-22. Genuinely
  cheap on the numbers and the cheapest name the screen found.
- Rejected on **coherence**, not valuation: this report is short TLT, a position
  that makes money if long rates stay high or rise, with the 10Y at 4.94%. A
  homebuilder long needs the opposite. Publishing both would be one book betting
  against itself, and the homebuilder is the lower-conviction half. Skipped.
- It is also 30% off its high, below sma20 51.81 and sma50 54.55, 7% off its
  150-day low — cheap and still falling, with the driver pointed the wrong way.

## [06:22 ET] WATCHLIST — SCHL — below book, near-debt-free, NOT researched enough to publish
- Scholastic: 34.75, **0.87x** quarterly book of 40.15, **D/E 0.15**, P/E 11.69,
  ROE 6.61%, net margin 3.58%, current ratio 1.23, dividend 2.00%. Earnings 09-24.
  27.7% off its 150-day high of 48.07, 12.8% above its low of 30.81. Avg daily
  dollar volume ~$12M, so exitable.
- Two anchors agree on roughly the same target: 1.2x book = 48.18, and the
  150-day high is 48.07. A 0.65x-book bear case is 26.10.
- **Why it is a watchlist line and not a candidate:** at an entry near the market
  (34.00) the ratio is 1.79, short of the 2.5 long_term floor; it only clears at
  2.74 if entry is staged down to 32.00. More importantly I have not established
  whether the book is tangible or whether children's publishing and school book
  fairs are in structural decline, and a long_term valuation anchor I cannot
  defend is not researched enough to publish. Flagging, not recommending.
- sources: https://finnhub.io/api/v1/stock/metric?symbol=SCHL&metric=all ,
  https://api.nasdaq.com/api/quote/SCHL/historical

## [06:22 ET] NEW IDEA — SNX — the one long that cleared the bar today
- TD SYNNEX 266.16, above a rising sma20 257.66 and sma50 254.40, 10.2% off its
  150-day high 296.47. Earnings **2026-09-24**.
- Outperforming SPY +6.7pp (1m) / +55.9pp (6m) and sector proxy XLK +2.5pp /
  +34.4pp — leadership, not a bounce. Beat 3 straight: +15.97%, +41.62%, +1.69%.
- Entry 260 on the rising 20-day; stop 242.50 below the 08-24 swing low 243.43
  = 2.25 ATR. **The tighter stop under the 09-10 low 253.34 was rejected at 1.03
  ATR** — it fails the floor. Target 296.47 (the 150-day high) = **2.08:1**.
- Honest negative recorded: 61 insider sells / $14.4M, zero open-market buys.
- action: captured via add_candidate.py (buy, conviction 4)

## [06:24 ET] REJECTED — all three crypto majors, for one shared structural reason
This is the lane that actually trades on a Saturday, so it got a proper look.
All three broke out violently on the 2026-08-23 bar and have consolidated since;
all three sit at the TOP of that consolidation. The problem is the same in each
case: **an honest stop below the four-week range is wider than the measured move
above it**, so the R:R is under 1 before any judgement is applied.
Live prices fetched 06:01 ET, structure from CoinGecko 4-day OHLC bars.
| Coin | Live | Post-08-24 range | Stop (below range) | Measured-move target | R:R |
| --- | --- | --- | --- | --- | --- |
| BTC | 81,305 | 75,038 - 82,108 | 74,800 | 89,200 | **0.92** |
| ETH | 2,641.63 | 2,357.48 - 2,647.68 | 2,340 | 2,937.88 | **0.90** |
| SOL | 111.89 | 91.83 - 110.17 | 100.40 | 128.51 | **1.45** |
- SOL is the closest and the most tempting — it is the only one already trading
  **above** its 90-day high (110.17), i.e. a genuine breakout in progress, and a
  breakout entry is the style this report is short of (31 pullbacks to 1 in the
  first month). Even entering on a retest of 110.17 it only reaches 1.88, and it
  needs a 130 target — beyond the measured move — to show 2.03. That is
  reverse-engineering the target, so no.
- **Caveat recorded honestly:** CoinGecko's free OHLC endpoint serves 4-day bars
  at every window I could request, so I have no true daily ATR for any coin. The
  stops above are set below four-week structural lows rather than by an ATR
  multiple, and are wide enough that the 2.5-ATR crypto floor is very unlikely to
  bind. validate_report.py should recompute.
- sources: https://api.coingecko.com/api/v3/coins/<id>/ohlc?vs_currency=usd&days=90 ,
  https://api.coingecko.com/api/v3/simple/price

## [06:24 ET] REJECTED — small/mid caps — the lane came up empty, and why
Deliberately hunted, since config/universe.md wants it and the report has none.
- **AIR** (AAR Corp, 112.77, earnings **09-21**, one session away) got the closest
  look: it has beaten four straight quarters by 9.43%, 7.35%, 13.06% and 8.55%,
  and is 26.8% off its high. Rejected on the tape: 138.58 on 08-26 to 112.77 on
  09-18 with every rally failing, and **09-18 volume of 1,424,273 against a
  ~300K recent average — roughly 3.5x — on a down day closing near its low, one
  session before the print.** That is distribution into an event, not an entry.
  There is also no support shelf between 112.77 and the 150-day low of 99.62, so
  a 2.0-ATR stop at 102.50 would sit in empty space rather than on a level.
  Analyst bullish share is falling (-6.8pp) and insiders are 0 buys / 7 sells.
- **SFIX** (2.84, earnings 09-23): levels do technically work — stop 2.59 is 2.05
  ATR, target 3.34 sits under the 50-day 3.50, giving 2.0:1. Rejected anyway on
  **expectancy**: the baseline win rate at 2.0:1 is 33.3%, the company is
  unprofitable (ROE -9.35%, net margin -1.43%) at a 150-day low, and I have no
  information about the quarter. Claiming better than 33.3% would be asserting an
  edge I do not have, and at 33.3% the expectancy is zero. A conviction-2 lottery
  ticket still has to beat its own baseline.
- **EBF** (21.32), **MANU** (19.69), **UEC** (9.81): no evidence beyond a date on a
  calendar. UEC additionally missed by 117.8% last quarter and would have been a
  second uranium bet alongside the open CCJ. All skipped rather than padded.

## [06:24 ET] REJECTED — MLKN, CAG, KMX, CCL, JBL, MTN, LCII-as-a-long
Screened on fundamentals, all failed on balance sheet or trend:
- MLKN 1.05x book but D/E 0.96 into a 09-22 print, in a structurally shrinking
  office-furniture market — the opposite of THO's survive-the-trough premise.
- CAG 1.14x book, **ROE -24.3%, net margin -17.0%** — losing money, 4.91% yield
  is not support. KMX D/E **2.99**, ROE 3.67%, net margin 0.84%, P/E 39.4.
- CCL 21.84, 0.14% off its 150-day low, D/E **1.92**, current ratio **0.33**.
- JBL D/E 2.55 and MTN D/E **5.48** — neither survives a downturn cheaply.

## [06:25 ET] AWAITING-ENTRY REVIEW — the four stale resting orders
All ten awaiting-entry lines from prior_context are now accounted for. MU was
amended (level unchanged) and IYR rejected above; BTC/`/MBTU6` are dead, noted
in the crypto block. The remaining four:
- **DG BUY @ 134.50** (published 2026-08-21): DG closed **122.41**, so the entry
  sits 9.9% ABOVE the market and above the 130.76 high the stock failed at on
  09-15. It has not filled in four weeks, DG is 22.6% off its high and below both
  its 20-day (126.02) and 50-day (124.34), and I have no fresh catalyst for it.
  **Recommend cancelling the order.** A resting bid nobody is re-underwriting is
  not a position, it is a forgotten one.
- **VST BUY @ 128.00** (published 2026-08-24): VST closed **140.67**, so the entry
  is 9.0% BELOW the market — and below VST's 150-day low of 132.66, meaning it
  fills only on a break to new lows. **Recommend cancelling.** This report is
  closing CEG today on the power complex breaking down (XLU is at its own 150-day
  low, VST is -21% off its high and under sma20 142.27 / sma50 147.46). Leaving a
  bid that buys the same breakdown, with no stop attached, contradicts that call.
  The datacenter-power thesis is unchanged and worth re-entering — with a fresh
  level, a stop and a dated reason, not a four-week-old resting order.
- **GLD SELL @ 406.77** (published 2026-09-08): stands. GLD closed 401.17, so this
  is an unfilled limit trim 1.4% above the market on a long held at 398.00. It is
  coherent with holding the position and needs no change.
- **KXFEDDECISION-26SEP-H25 @32, -26SEP-H0 @47, -26OCT-H25 @28**: cannot be
  reviewed — the Kalshi feed returned no macro markets this run (see the 06:07
  block). The two 26SEP contracts reference a September FOMC that has already
  passed and may have resolved. **Flagging for the next run with a working feed;
  I will not guess at a price or a resolution.**

## [06:26 ET] MARKET FRAME — the index is fine; the market underneath it is not
All 2026-09-18 closes — source: https://api.nasdaq.com/api/quote/<SYM>/historical
| Index ETF | Close | sma20 | sma50 | Off 150d high |
| --- | --- | --- | --- | --- |
| SPY | 761.69 | 764.30 | 759.73 | **-2.3%** |
| QQQ | 721.45 | 713.24 | 709.95 | **-3.6%** (above both averages) |
| IWM | 284.10 | 292.49 | 295.14 | **-6.9%** (below both) |
- SPY is 2.3% from an all-time-range high. Yet this session's work found NKE,
  LULU, LCII, THO, CCL, AZO, KBH, COST, CCL and XLU **at or within 3% of 150-day
  lows**, and JEF and CEG each -13% in seven sessions.
- That gap is the finding. This is a narrow tape: QQQ above both averages, IWM
  below both, mega-cap tech holding the index up while breadth rots underneath.
  With the 10Y at 4.94% against 3.88% funds, the de-rating is happening name by
  name rather than at the index level.
- It is also why today's output is shaped the way it is: **four exits, one new
  long in a name with actual relative strength (SNX), one long-term accumulation
  in a low-leverage cyclical (THO), and one unchanged amendment (MU).** In a tape
  like this the honest edge is in not owning the wrong things.

## [06:26 ET] RESEARCH COMPLETE
- **candidates: 7 unique symbols (8 lines — THO captured twice, the later line
  adds the explicit long_term invalidation condition and supersedes it).**
  - Exits / position updates: **NKE**, **CEG**, **LULU**, **LCII** (all `sell`)
  - Amendment, level unchanged: **MU** (buy @ 960, conviction 4, 2.00:1)
  - New swing long: **SNX** (buy @ 260, conviction 4, 2.08:1, earnings 09-24)
  - New long-term: **THO** (accumulate 58-70, conviction 4, 2.64:1 vs a 55 bear
    case, WAIT until after the 09-22 print)
- All 16 open positions were reviewed and each has a written decision. All 10
  awaiting-entry lines were reviewed; DG and VST are recommended for cancellation.
- Horizon skew is real and not manufactured: **no intraday ideas**, because the
  US market is closed on a Saturday and every equity level here is the 09-18
  close. All equity entries are for the next open or later.
- **Conviction floor note:** nothing scored 5, and nothing scored 2. Every
  published idea carries either 2 or 3 distinct evidence kinds and is scored at
  exactly what that supports — no idea was rounded up.

### Coverage gaps — things I could not check
- **Event contracts: entirely unavailable.** Kalshi returned 0 markets for Fed,
  FOMC, CPI, inflation, interest rate, recession, GDP, unemployment, oil and S&P;
  an empty query returned 40 rows, all sports parlays with null prices. **Zero
  event contracts published as a result** — not for lack of hunting. Three open
  event positions could not be marked or resolved.
- **Futures: no idea published, because no futures or index price could be
  fetched.** macro returned ok:false for ES, NQ, DXY, ^TNX, ^VIX, gold and WTI
  (yahoo 429 plus a finnhub index entitlement error). Index context above is from
  ETF proxies instead. I will not name a contract month I cannot price.
- **No true daily ATR for any crypto** — CoinGecko's free OHLC endpoint served
  4-day bars at every window requested. Crypto stops in the rejection table are
  set below structural lows rather than by ATR multiple.
- **No live prices anywhere** — market closed. Every equity figure is the
  2026-09-18 close, correctly labelled as a closed session rather than stale data.
- Not reached: FDA/PDUFA calendar (two sources returned no readable dates), index
  rebalances, unlocks, court and regulatory dates, international markets.
- **SCHL** is flagged as a watchlist line above, explicitly not researched enough
  to publish as a long_term candidate.

### Sources that failed
- Kalshi events API — 0 results for every macro query (returns sports only)
- Yahoo Finance — HTTP 429 on all index/FX/commodity symbols
- Finnhub index quotes — "Market data subscription required for CFD indices"
- Stooq — 404 on ^GSPC, ^NDX, ^DJI, ^RUT
- Alpha Vantage — no API key
- nasdaq `short UEC` — read timeout
- biopharmcatalyst.com PDUFA calendar — returned only a cookie notice

## [06:27 ET] ADDENDUM — systematic screen of the full earnings calendar, nothing added
After writing RESEARCH COMPLETE there was budget left, so rather than stop early
I screened **every symbol on the fetched 12-day earnings calendar** (151 names)
on fundamentals, not just the ones I had already looked at.
- Filter: net margin >5%, ROE >10%, D/E <0.8, 0 < P/E < 25, with a real quarterly
  book value. Across the whole M-Z half, **zero names passed** — the calendar
  beyond the large caps is almost entirely micro caps with negative margins
  (many at -100% to -20,000%) and closed-end bond funds.
- **AYI** (Acuity Brands) was the only quality name the screen surfaced: P/E 19.1,
  ROE 16.85%, net margin 10.25%, D/E 0.24. **Rejected** — earnings 2026-10-01 is
  13 days out, outside the 10-session window, so there is no catalyst inside the
  horizon; the stock is 20% off its high and below both its 20-day (323.94) and
  50-day (334.78) in a clean downtrend; it is 3.20x book so there is no value
  case either; and the 2.0-ATR stop at 285 would sit in empty space between the
  296-298 shelf and the 150-day low of 257.04. Watchlist at best.
- Data-quality note on this screen: several micro caps returned obviously broken
  metrics (net margins of 392%, 6,331% and -20,671%, CTRM at a 0.27 P/E). I did
  not act on any of them and would not without a primary filing.
- **Conclusion: the candidate list stands at 7 unique symbols.** The screen was
  run to find reasons to add, and found none that clear the bar. Recording that
  explicitly so the next run knows this ground was covered rather than skipped.
