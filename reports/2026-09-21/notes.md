# Research log — 2026-09-21

## [06:04 ET] MACRO — rates and policy
- Fed funds effective (DFF) **3.88%** on 2026-09-17, prior **3.63%** — a **25bp HIKE at the September FOMC**. source: https://fred.stlouisfed.org/series/DFF
- US 10y 4.94% (2026-09-17), prior 5.01% — long end RALLIED into the hike. source: https://fred.stlouisfed.org/series/DGS10
- US 2y 4.67%, prior 4.74% — also lower. source: https://fred.stlouisfed.org/series/DGS2
- 10y-2y curve +0.25 (2026-09-18), prior +0.27 — flattening slightly, still positive. source: https://fred.stlouisfed.org/series/T10Y2Y
- Unemployment 4.1% (Aug 2026), unchanged from prior. source: https://fred.stlouisfed.org/series/UNRATE
- CPIAUCSL 334.131 (Aug 2026) vs 332.813 prior month = +0.40% m/m NSA — hot monthly print, consistent with a hiking Fed. source: https://fred.stlouisfed.org/series/CPIAUCSL
- TLT last 81.25 (2026-09-18 close, finnhub), prev_close 81.78, -0.65%. age 3722min = Friday close. source: market_data.py macro

**Regime read:** The Fed is *hiking* into 4.1% unemployment and a firm CPI. Both
2s and 10s fell on the week, so the market is reading the hike as
growth-restrictive rather than inflation-permissive. That is a bear-flattener
setup unwinding into a bull-flattener. Implication: long-duration bonds are no
longer an obvious short, and the open `TLT` SELL (entry 81.87, +0.8%) needs a
hard look rather than a hold-by-default.

## [06:04 ET] DATA QUALITY — source failures
- Yahoo Finance returning **HTTP 429 (rate limited)** on every index/FX/commodity symbol: ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES=F, NQ=F, DX-Y.NYB, ^TNX, GC=F, CL=F all FAILED.
- Finnhub refuses CFD indices ("Market data subscription required").
- Stooq 404s on ^-prefixed index symbols.
- CoinGecko `crypto.prices` FAILED inside macro.
- Working: FRED (all series), finnhub single-equity/ETF quotes (TLT returned fine).
- Consequence: **no live index, VIX, DXY, gold or crude print this run.** Will use liquid ETF proxies via finnhub instead of naming index levels I cannot fetch.

## [06:06 ET] TAPE — Friday 2026-09-18 closes (finnhub, prev session; market shut)
| ETF | Close | Chg% |
| --- | --- | --- |
| SPY | 761.69 | -0.12 |
| QQQ | 721.45 | +0.63 |
| IWM | 284.10 | -0.47 |
| XLE | 64.31 | -0.26 |
| XLU | 41.10 | **-1.42** |
| XLF | 55.86 | -0.04 |
| XLV | 168.39 | -0.25 |
| XLP | 82.80 | -0.83 |
| GLD | 401.17 | +0.71 |
| SLV | 59.93 | **+1.63** |
- Read: mega-cap tech (QQQ) led, breadth poor (IWM red, SPY flat). Rate-sensitive
  defensives (XLU -1.4%, XLP -0.8%) were the worst — consistent with the 25bp hike.
  But **precious metals rose into the hike** (SLV +1.6%, GLD +0.7%), which is not
  what a pure real-rate story predicts. That divergence is the most interesting
  thing on the tape and is worth a trade rather than a comment.
- All prices `asof` 2026-09-18 20:00 UTC = Friday's close. That is the freshest
  honest equity price at 06:06 ET Monday, not stale data.

## [06:18 ET] POSITION REVIEW — all 16 open positions
Decisions, from fetched Friday closes + ATR14 (nasdaq history, 150 bars):

| Sym | Side | Entry | Stop | Close | ATR14 | Stop dist (ATR) | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLE | BUY | 63.9 | 60.8 | 64.31 | 1.33 | 2.33 | hold, unchanged |
| CCJ | BUY | 94.0 | 82.5 | 91.62 | 3.38 | 3.41 | hold, unchanged (already 3x in 10d — not re-pitching) |
| NKE | BUY | 40.75 | none | 35.51 | 0.89 | n/a | thesis broken; exit already on record as the 09-08 NKE SELL |
| BCC | BUY | 76.5 | none | 75.69 | 2.19 | n/a | hold |
| LCII | BUY | 94.0 | none | 85.6 | 3.32 | n/a | WATCH — at the 150d low (85.07), -46% off high |
| PFE | BUY | 27.6 | none | 27.66 | 0.53 | n/a | hold (4x in 10d — not re-pitching) |
| CEG | BUY | 272.0 | 250.0 | 254.71 | 10.78 | **0.44** | **CLOSE — captured** |
| EEM | BUY | 65.6 | 63.0 | 67.03 | 0.96 | 2.70 | hold, working (+2.2%) |
| DINO | BUY | 107.5 | 97.75 | 115.9 | 4.36 | 2.24 | hold — see note below |
| GLD | BUY | 398.0 | 381.0 | 401.17 | 7.65 | 2.22 | hold, thesis strengthening |
| LULU | BUY | 115.0 | none | 98.06 | 5.59 | n/a | thesis broken; exit already on record as the 09-08 LULU SELL |
| SVRA | BUY | 5.35 | 4.6 | 5.37 | 0.20 | 3.70 | hold |
| TLT | SELL | 81.87 | 83.3 | 81.25 | 0.69 | 2.07 | **CLOSE — captured** |
| LULU | SELL | 100.61 | none | 98.06 | 5.59 | n/a | hold (this IS the LULU exit) |
| NKE | SELL | 38.4 | none | 35.51 | 0.89 | n/a | hold into the 09-28 print |
| DVN | BUY | 49.6 | 46.9 | 48.61 | 1.36 | **1.25** | hold; flag — stop was set inside the 2.0 ATR floor at publication (4x in 10d, not re-pitching) |

**DINO note (no candidate captured, deliberately).** DINO is +7.8% and 1.5% off
its 150-day high — the instinct is to raise the stop from 97.75. I am not doing
it: entry 107.50 less 2.0x ATR14 (4.359) is 98.78, so *any* raise puts the stop
inside the floor, and validation would read the improved ratio as exactly the
stop-walking CLAUDE.md documents on KRE. The right amendment here is none.

**GLD SELL @ 406.77 (awaiting entry, published 09-08) conflicts with the open
GLD BUY.** Metals just rose through a 25bp hike (GLD +0.71%, SLV +1.63% Friday).
That resolves the conflict in the long's favour — treating the resting sell as
stale rather than re-pitching it.

## [06:19 ET] REJECTED — event contracts — Kalshi search returning junk this run
- `market_data.py events` for "Fed", "FEDDECISION", "interest rate", "CPI",
  "recession" all returned only `KXMVECROSSCATEGORY-*` tennis/target-price
  markets, 22-27 rows, every one with null bid/ask/last/volume.
- No Fed or macro series reachable, so **no event contract idea can be priced
  this run.** I will not state an implied probability I could not fetch. Three
  event contracts sit in "awaiting entry" and none can be re-checked today.

## [06:24 ET] REJECTED — COST BUY — de-rating is real but every confirmation points the wrong way
Looked hard at it: Costco 895.31, 18.4% off its 150-day high, 0.8% off the low,
earnings 2026-09-24 amc (confirmed on the fetched finnhub calendar, est EPS 6.67
on $96.75B). The "quality compounder on sale into a catalyst" shape is there.
Three fetched checks killed it:
- `relstrength COST --peer XLP`: **lagging SPY on every window measured** — 1m
  -5.5%, 3m -7.9%, 6m -23.6%; and lagging its own sector 1m -2.1%, 3m -5.3%,
  6m -9.2%. It is not being dragged down by staples, it is the weak one inside them.
- `analysts COST`: revision_direction **deteriorating**, bullish share 65.2% and
  -3.0pts over four months.
- `insiders COST`: **0 open-market buys, 0 distinct buyers**, 2 sells worth $1.54M
  over six months. No insider is treating this price as cheap.
A pullback entry into a deteriorating name the session before a print is the
reflex discount `config/strategy.md` names. No candidate.
- sources: https://finnhub.io/ , https://www.nasdaq.com/market-activity/stocks/cost/historical
- Also failed this run: `short COST` — nasdaq api ReadTimeout. No short-interest read.

## [06:25 ET] THEME — the consumer is at 150-day lows *while* the Fed hikes
Not one name, a cohort. Every fetched consumer-facing close, % off its 150-day high
and % above its 150-day low:
| Sym | Close | off high | above low | earnings |
| --- | --- | --- | --- | --- |
| COST | 895.31 | -18.4% | +0.8% | 09-24 amc |
| AZO | 2855.31 | -26.5% | +1.4% | 09-22 bmo |
| CCL | 21.84 | -34.2% | **+0.1%** | 09-28 bmo |
| KBH | 47.12 | -30.3% | +7.0% | 09-22 amc |
| KMX | 57.21 | -12.4% | +62.7% | 09-29 |
| NKE | 35.51 | -48.2% | **+0.03%** | 09-28 |
| LULU | 98.06 | -49.1% | +2.8% | — |
Seven discretionary/staples names, six of them within 7% of a 150-day low, into a
Fed that just *hiked*. This is the single most coherent signal on the tape and it
argues the opposite of buying these dips: the cohort is discounting a consumer
slowdown that tighter policy makes worse, not better. It also explains the bond
rally through the hike (10y 5.01 -> 4.94) — same trade, different instrument.
Consequence for today: **do not go bargain-hunting in this cohort**, and treat
the two broken consumer longs already on the book (NKE -11.2%, LULU -14.7%) as
confirmation that catching this knife has already cost money once.

## [06:36 ET] CAPTURED — XRT SELL_SHORT — conviction deliberately set to 3, not 4
Three distinct evidence kinds hold (technical_level, positioning, dated_catalyst),
which the `config/strategy.md` table scores as a 4. I set 3 on purpose and am
recording why so the red team does not "fix" it upward: the dated_catalyst is
AZO's print, which is a **read-across** to XRT rather than XRT's own event. A
read-across is weaker than the table assumes, so the score is discounted by one.
Under-claiming is the safe direction; the red team lowers, it never raises.

Chose XRT over XLY deliberately: XLY is dominated by two mega-caps, so shorting
it is mostly a bet on those two rather than on the consumer. XRT is the retail
basket, which is the thing the thesis is actually about. XLY numbers for the
record — close 111.03, sma20 114.48, sma50 115.37, lagging SPY 1m -5.41%,
3m -7.23%, 6m -14.23%.

## [06:36 ET] REJECTED — SLV BUY — the target only clears the floor by being stretched
Silver was the most interesting thing on Friday's tape: SLV +1.63%, the best of
the ten ETFs fetched, closing 59.93 above its 20d SMA (59.757) and well above its
50d (56.815), in the same week the Fed hiked. Metals up through a hike is a real
signal. It still does not make a publishable swing:
- Honest stop is below the 2026-09-16 intraday low of 56.275, call it 55.90.
  From 59.93 that is 4.03 = 2.30x ATR14 (1.7546) — properly wide, clears the 1.8 ETF floor.
- Real overhead structure is 60.95 (09-03 high), 61.71 (09-09), 63.03 (08-24), 64.31 (08-28 spike).
  Target 64.31 gives reward 4.38 against risk 4.03 = **R:R 1.09**.
- To reach the 2.0 floor the target has to go to 68.00, which is above every
  level in 60 sessions of bars. That is reverse-engineering the target, which
  `config/strategy.md` names as the thing the floor exists to prevent. Dropped.
- Relative strength is also weaker than the Friday candle suggests: SLV vs GLD is
  +2.93% over 1m but **-2.92% over 3m**, and SLV vs SPY is **-24.19% over 6m**.
  This is a heavy laggard having one good week, not leadership.
- GLD is already an open position on this exact driver, so a second metals idea
  would spend correlation budget for a weaker version of a bet already held.
- Silver miners for the record: SIL 95.20 (sma20 97.78, sma50 87.60, ATR 3.71),
  GDX 95.48 (sma20 98.63, sma50 87.97, ATR 3.36). Same shape, same problem.

## [06:13 ET] CORRECTION — my own timestamps above are wrong
The `[06:18]`..`[06:36]` headings above were estimated, not read from the clock.
A `date` call at this point returns **06:12 ET**, so everything above happened
between roughly 06:01 and 06:12 — I was running ~25 minutes fast against myself.
The findings and prices are unaffected (every price carries its own fetched
`asof`), but the headings are not a reliable timeline and the run has far more
budget left than I had assumed. Timestamps from here are read from `date`.

## [06:13 ET] REJECTED — ACN BUY — a 42% three-month run with analysts cutting into it
ACN 181.29, -4.7% on Friday alone, 20.9% off the 150-day high — reads like the
"quality business de-rated" long_term shape. The fetched checks say otherwise:
- `relstrength ACN --peer XLK`: **+41.65% over 3m**, +39.65% vs SPY. This is not
  a de-rated name, it is a name that already ran. The 6m figure (-10.94%) is the
  crash it already recovered from.
- `analysts ACN`: revision_direction **deteriorating**, bullish share 59.4% and
  **-10.3 points** over four months — the sharpest deterioration of anything I
  priced today, arriving *after* the run.
- `insiders ACN`: **0 open-market buys, 9 sells** worth $2.57M in six months.
- Earnings 2026-10-01 amc (fetched calendar, est 3.21 on $18.21B). Surprise
  record is positive but small and shrinking: +4.3%, +1.2%, +2.1%, +1.4%.
Buying a 42% three-month move into a cutting sell-side with insiders only selling
is the opposite of the de-rating trade. No candidate.

## [06:14 ET] REJECTED (to watchlist) — IBIT / BTC long — a real breakout, but the target has to be invented
This is the best *setup* I found and I am still not capturing it, so the levels
are here for the watchlist:
- BTC spot **84,599, +5.29% in 24h**, $37.6B 24h volume (coingecko, live — crypto
  is the only genuinely current price this run). ETH 2,721.15 +5.71%, SOL 115.75 +7.15%.
- IBIT closed **46.02 Friday, +6.3% on the day**, against a 90-day range high of
  **46.525** — so the breakout began Friday in the equity wrapper and the weekend
  confirmed it in spot. Two independent sources agreeing is the strong part.
- ATR14 1.4421 (3.13%), sma20 44.34, sma50 39.71, 90-day base 32.84-46.525,
  +40.1% off that low. ADV $2.56B.
- Honest levels: retest entry 46.50 (the broken 90-day high), stop 42.30 (under
  the 09-16 low of 42.425) = risk 4.20 = **2.91 ATR**, which clears even the 2.5
  crypto floor. Good stop.
- **The problem is the target.** There is no overhead structure at all — it is a
  90-day high — so any target is constructed. Clearing R:R 2.0 requires 54.90
  (+18%) on top of a 40% run, with no catalyst I fetched. 54.90 gives exactly
  2.00:1, which is the "nudged until it passed" cluster CLAUDE.md documents.
  I will not ship a number I reverse-engineered. Watchlist, not a recommendation.
- Also noting two stale resting shorts this invalidates: `BTC` SELL @ 63,400 and
  `/MBTU6` SHORT @ 64,340 are both ~25% below spot and were never filled. They
  should not stay on the book as live levels.
- Instrument note: a BTC *long* has no reason to prefer futures — the futures
  preference in `config/universe.md` exists because Robinhood Crypto cannot
  short. I also could not verify a tradeable /MBT contract month this run, and
  /MBTU6 would be inside its expiry window, so I would not have named one.

## [06:15 ET] SECTOR SCAN — 10 more ETFs, Friday closes (nasdaq, 150 bars)
| ETF | Close | ATR14 | sma20 | sma50 | off 150d high | above 150d low |
| --- | --- | --- | --- | --- | --- | --- |
| XLK | 189.60 | 2.93 | 185.37 | 183.12 | -4.6% | +49.7% |
| XBI | 156.72 | 3.79 | 161.63 | 157.57 | -7.8% | +32.6% |
| XLB | 49.99 | 0.77 | 52.04 | 51.77 | -7.8% | +7.0% |
| KRE | 72.75 | 1.32 | 73.98 | 75.37 | -7.2% | +17.7% |
| IYR | 98.00 | 1.27 | 101.92 | 103.72 | -9.4% | +6.0% |
| XLI | 169.75 | 2.43 | 173.99 | 178.98 | -9.8% | +8.8% |
| SMH | 573.00 | 14.45 | 557.82 | 564.78 | -14.7% | +59.2% |
| ITB | 87.41 | 2.06 | 92.63 | 95.68 | -23.8% | **+2.9%** |
| URA | 41.65 | 1.53 | 45.00 | 43.15 | -29.4% | +12.0% |
| XOP | 190.61 | 4.79 | 191.03 | 180.43 | -5.1% | +33.3% |
Read: **only XLK and SMH are above both moving averages.** Everything
rate-sensitive or consumer-facing (ITB, IYR, XLI, KRE, XLB) is below both. That
is one market with two halves, and it is the same split as Friday's tape
(QQQ +0.63% against IWM -0.47%).

## [06:16 ET] REJECTED — ITB SELL_SHORT — right thesis, arrived too late to price
Homebuilders are the purest expression of "Fed hikes into a soft consumer" and
there is a dated catalyst: **KBH earnings 2026-09-22 amc** (fetched calendar,
est EPS 0.90 on $1.31B), with KBH itself at 47.12, -30.3% off its high. I still
cannot make the numbers work:
- ITB 87.41 is **only 2.9% above its 150-day low (84.98)**. The target is used up.
- An honest bounce entry at 90.50 needs a stop at 94.20 to clear the 1.8 ATR ETF
  floor (risk 3.70 = 1.80 ATR). Target 84.98 = reward 5.52 = **R:R 1.49**.
- Reaching 2.0 requires a target of 83.10, *below* the 150-day low. That is
  inventing a level, so the idea failed the floor. Dropped.
This is also the check that confirms XRT was the right instrument for the same
theme: XRT sits 5.4% above its low with the range low as a real target, so it
clears at 2.46 without constructing anything. Same thesis, one of the two is
priced and the other is not.

## [06:16 ET] DATA GAP — event contracts unavailable, confirmed on a second pass
Re-queried `events` for "Fed decision", "unemployment", "GDP", "government
shutdown", "Bitcoin": **0 markets returned for every one**. The earlier "Fed"
query returned 22-27 rows that were all `KXMVECROSSCATEGORY-*` tennis markets
with null prices. The Kalshi source is degraded this run.
Consequence: **no event contract can be priced or re-checked today**, including
the three sitting in "awaiting entry" (`KXFEDDECISION-26SEP-H25` @32,
`KXFEDDECISION-26OCT-H25` @28, `KXFEDDECISION-26SEP-H0` @47). The first and
third reference a September decision that has now *happened* — the Fed hiked
25bp — so they are resolved or near-resolved, but I could not fetch a settlement
price and will not state one. Synthesis should say this plainly.

## [06:20 ET] DATA GAP — options-implied move unavailable
`market_data.py implied SMH --entry 582 --target 671.83` and the same for XRT
both returned **HTTP 401 Unauthorized** from yahoo-options. `config/strategy.md`
asks for this check on every level-set and I could not run it on either
candidate. Neither target has been tested against what options price; synthesis
should carry that in `data_quality_notes` rather than let the omission pass
silently.

## [06:20 ET] CAPTURED — SMH BUY — deliberately a breakout entry
Noting the entry style on purpose. `config/strategy.md` records that the first
month was 31 pullback entries against 1 breakout, 42% of them ever filled, and
that the ones which filled were the ones already falling. SMH is entered at
582.00 **above** Friday's 573.00 close, on a stop-limit through the 580.57/580.81
double top. It fills only if the market proves the level, and if it never fills
the idea costs nothing — which is the correct failure mode for a high-beta long
on a tape with poor breadth.

## [06:24 ET] INSIDER SWEEP — 10 de-rated names, 6-month open-market buys
| Sym | Buys | Distinct buyers | Buy $ | Sells | Sell $ |
| --- | --- | --- | --- | --- | --- |
| **KMX** | **6** | **5** | **$1,268,037** | **0** | **$0** |
| NKE | 5 | 4 | $3,734,194 | 6 | $1,203,534 |
| LULU | 3 | 2 | $1,994,952 | 1 | $100,142 |
| AZO | 1 | 1 | $492,855 | 2 | $4,684,436 |
| CCL | 0 | 0 | $0 | 4 | $1,524,389 |
| KBH | 0 | 0 | $0 | 8 | $16,580,060 |
| BCC | 0 | 0 | $0 | 3 | $665,842 |
| PAYX | 0 | 0 | $0 | 4 | $3,391,925 |
| CTAS | 0 | 0 | $0 | 3 | $3,562,049 |
| LCII | 0 | 0 | $0 | 0 | $0 |
Only KMX shows a clean cluster with no offsetting sales. Captured.

**NKE and LULU insider buying is real but stale and underwater — it argues the
opposite of what it looks like.** NKE: Elliott Hill 23,660 sh and Tim Cook
25,000 sh at 42.27-42.43, all 2026-04-09/13. NKE is now **35.51**, so those
buyers are -16%. LULU: Charles Bergh at 164.20 (03-20) and 117.05 (06-15),
Maestrini at 151.02 — now **98.06**, -16% to -40%. Insiders bought these
de-ratings early and were wrong twice. That is a direct answer to the "insiders
are buying, so it is cheap not broken" read on both names, and it supports
leaving the 09-08 exits in place rather than re-entering.

**KBH is the counter-example worth naming:** 8 sells worth $16.58M, zero buys,
into a 09-22 print, with the stock 30.3% off its high. Nobody inside is defending
that price. It reinforces the ITB read even though ITB itself did not price.

## [06:24 ET] CONFLICT DECLARED — KMX long vs XRT short
These are both captured and they point opposite ways at the same cohort, so
synthesis should not treat it as an error. The XRT short is the *basket* of
retail, which is lagging SPY on every window. KMX is the one constituent-type
name beating that basket by 33.78% over 6m with insiders buying it. Long the
divergence, short the aggregate — it reduces net consumer exposure rather than
doubling it, and neither idea depends on the other being right.

## [06:29 ET] POSITION UPDATE — LCII — it is a merger, and nobody told the tracker
The find of the run, and only visible by reading the filings rather than the chart.
`market_data.py filings LCII` returned a **Form 425** (business-combination
communication) filed 2026-09-10 alongside an 8-K. Read both:
- LCI Industries agreed **2026-06-30** to be acquired by **Patrick Industries
  (PATK)** in an **all-stock** merger, fixed exchange ratio **1.2440 PATK per LCII**.
  LCII holders take ~48% of the combined company; >$150M run-rate synergies
  claimed; pro forma ~$8.1B revenue, ~$1.0B adj. EBITDA; close expected H1 2027.
- 8-K Items 8.01/9.01: HSR notifications filed **2026-08-05**; LCI **voluntarily
  withdrew 2026-09-04** and **refiled 2026-09-09**, restarting the waiting
  period. No reason disclosed; no Second Request mentioned. A pull-and-refile is
  the standard way to give the agency more time without drawing a Second Request
  — it is a soft antitrust signal, not a disclosed problem, and both firms are
  Auto Components suppliers, so the horizontal-overlap question is real.

**The arithmetic (all fetched, 2026-09-18 closes):**
    parity = 1.2440 x PATK 68.71 = 85.4752
    LCII    = 85.60
    spread  = +0.1248  =  **+0.146% — LCII trades ABOVE its own deal value**
- So there is **no arb discount to collect**, and LCII's -46% drawdown from
  158.75 is not an LCII story at all: it is PATK, which closed **0.31% above its
  own 150-day low** (68.50) and -52.4% off its high.
- Holding LCII = holding 1.244 PATK **plus** writing the deal-break risk for
  zero premium. The 94.00 entry implied PATK at 75.56; PATK is 68.71.
- Decision: **close. Captured, conviction 4.**
- Considered and rejected: the textbook arb (short LCII / long PATK). The spread
  is 0.15% gross, which does not survive costs, and it needs margin. Not published.
- Considered and rejected: switching the long into PATK. Same economics without
  deal risk, but PATK is 0.31% off a 150-day low in a 52% downtrend — that is a
  falling knife, and "the cheaper way to own it" is not a reason to own it.

## [06:29 ET] REJECTED — SLV as a long_term idea too (the swing version failed earlier)
Retested silver under the long_term rules, where the floor is 2.5 against a
stated bear-case price and no stop is needed. Built the anchor from fetched
prices only — the GLD/SLV price ratio: 401.17/59.93 = **6.69 today**, against
492.15/85.27 = **5.77** at the two 150-day highs, i.e. silver has cheapened ~16%
against gold. Mean-reverting that ratio with GLD held flat gives SLV
401.17/5.77 = **69.53**.
    entry 58.00 -> target 69.53 = reward 11.53
    bear case 49.61 (SLV 150-day low) = risk 8.39
    R:R = **1.37**, against a 2.5 floor.
Fails on the long horizon as well as the swing. Silver is genuinely the most
interesting thing on the tape and it does not price on either clock. Watchlist.

## [06:30 ET] INSIDER SWEEP 2 — 12 diverse large caps, nothing comparable to KMX
BMY 0 buys/3 sells; CVS 0/9 ($359.0M sold); UPS 0/0; **F 1 buyer $148,880 @14.05
(06-23)**; GM 0/28 ($110.0M sold); INTC 0/2; DOW 0/0; LYB 0/1; NUE 0/23 ($37.6M);
**OXY 1 buyer $249,853 @52.38 (06-23)**; FDX 0/9; TGT 0/6.
F and OXY are single-buyer, sub-$250K purchases — that is a director topping up,
not a cluster, and `config/strategy.md` weights *distinct buyers*. Neither
becomes a candidate. Recording it because the absence is the finding: across 22
names checked today, **KMX is the only clean multi-buyer, zero-sell cluster**,
which is most of why it is the one single-stock long captured.

## [06:32 ET] FILINGS SWEEP — 9 open/pending names. Three flagged, all resolved
After LCII, I read the filing list for every remaining open position and pending
order. Three threw a flag and I chased all three to the document:

- **KHC — Form 25 (delisting) 2026-09-08 + 8-A12B + CERT. FALSE ALARM, resolved.**
  This looked serious: a Form 25 is a notification of removal from listing, and
  `KHC` BUY @23.00 was published *yesterday*. Read both documents: the Form 25 is
  a **voluntary** withdrawal from **Nasdaq** under 17 CFR 240.12d2-2(c), and the
  8-A12B registers the same common stock on the **NYSE**, "trading will begin on
  the NYSE at market open on September 14, 2026". It is a **listing transfer, not
  a delisting** — no reorganisation, no spin-off, same ticker, same shares.
  KHC remains NYSE-listed and Robinhood-tradeable; the pending buy stands
  unchanged. KHC closed 24.43 Friday, still above the 23.00 entry, so unfilled.
  sources: https://www.sec.gov/Archives/edgar/data/1637459/000163745926000062/khc-form25gdcdraftx6001812.htm
           https://www.sec.gov/Archives/edgar/data/1637459/000163745926000061/khc-form8xagdcdraftx600180.htm
- **VST — S-3ASR + 424B5 + FWP + 424B2, 09-09 to 09-14. Debt, not dilution.**
  $1.5B junior subordinated notes (Series A $850M at 7.000%, Series B $650M at
  7.250%, maturity 2057), guaranteed by Vistra on a subordinated basis. Proceeds
  ~$1.48B for general corporate purposes **including redeeming preferred stock**
  with October and December 2026 reset dates. No share issuance — the pending
  `VST` BUY @128.00 is not invalidated. Worth naming anyway: 7% junior sub money
  is expensive, and it was raised the same week the Fed hiked. VST closed 140.67,
  **9.9% above the 128.00 entry** and unfilled since 08-24 — that order is stale.
  source: https://www.sec.gov/Archives/edgar/data/1692819/000114036126036415/ny20081693x3_424b2.htm
- **CAG — three Form 3s and a DEFA14A. Routine, but not flattering.**
  Not a merger and not an activist: it is additional proxy material on Proposal 2,
  the say-on-pay advisory vote, ahead of the **2026-09-23 annual meeting**. Both
  **ISS and Glass Lewis recommended against**, and the board is arguing back.
  Conagra concedes FY26 was "challenging", cut incentive payouts 7.6% and paid
  long-term performance shares at 35.7% of target. Governance noise rather than a
  thesis break, but a proxy-adviser double-down against management on a name we
  are trying to buy belongs on the record. CAG closed **15.13** against the
  pending 15.00 entry — this one is about to fill, with earnings 09-29 six
  sessions later. source: https://www.sec.gov/Archives/edgar/data/23217/000002321726000044/cag-20260914xdefa14a.htm
- Clean, nothing material: SVRA (last 8-K 06-08), BCC, DINO, DVN, DG, SNX.

## [06:38 ET] SMALL CAP HUNT — 5 near-dated names, none cleared
Screened from the fetched earnings calendar rather than from memory, then checked
liquidity, insiders and structure. All rejected:
| Sym | Name | Mcap | Close | ATR14 | Earnings | Killed by |
| --- | --- | --- | --- | --- | --- | --- |
| AEHR | Aehr Test Systems | $3.05B | 93.49 | 8.15% | 10-01 | **49 insider sells, $47.5M** |
| WOR | Worthington Ent. | $2.74B | 57.38 | 4.02% | 09-22 | 0 buys / 3 sells, no edge into a print |
| MLKN | MillerKnoll | $1.42B | 20.66 | 3.81% | 09-22 | below both SMAs, no insider signal |
| CALM | Cal-Maine Foods | $3.42B | 72.89 | 2.64% | 09-30 | 0.16% off its 150-day low, falling knife |
| SFIX | Stitch Fix | $379M | 2.84 | 4.29% | 09-23 | 21 sells; and it is the XRT cohort I am short |

**AEHR is the one worth writing down**, because everything except the insiders
said buy: analysts 90.9% bullish and **improving** (+10.9pts), last quarter beat
by 1529% (0.11 actual vs -0.0077 est), price +14.6% off the 09-15 low of 81.58
and back above the 50d SMA, earnings 10-01, ADV $256M. Against that:
**49 open-market sells worth $47.54M in six months against zero buys** — roughly
1.6% of a $3.05B company sold by its own insiders into exactly that strength.
`config/strategy.md` says sales are weak evidence on their own; 49 of them
totalling 1.6% of the float is not "on their own", it is the signal. Rejected.
Its levels would also have been constructed: 2.0 ATR is 15.24 points, so a 2:1
target is +32.6% with no fetched resistance between 93.49 and the 147.40 high.

## [06:39 ET] SMH STOP — re-examined, disclosed, NOT walked in
Flagging this explicitly because it is the exact failure mode CLAUDE.md records
on KRE, and I want the red team to see the working rather than rediscover it:
    stop 555.00 -> risk 27.00 = **1.87 ATR**, R:R **3.33**, break-even hit 23.1%
    stop 537.00 -> risk 45.00 = **3.11 ATR**, R:R **1.996**, break-even hit 33.4%
The tighter stop gives the better ratio, which is precisely the tell. I did not
pick it for that. 555.00 was derived independently: it sits below the 09-17 low
(557.56), below the 20d SMA (557.82), and below the midpoint of the 537.73-580.81
base — a breakout that gives all of that back has failed. But the honest reading
is that this idea is **borderline**: the structurally safest stop leaves it at
1.996, a hair under the 2.0 floor, so the wide-stop version does not publish at all.
Mitigations taken rather than hidden: size cut 3% -> 2%, the whole calculation put
in `key_risk`, and the unavailable options check named in `counter_argument`.
If the red team cuts one idea today, it should be this one.

## [06:39 ET] LONG_TERM — nothing cleared, and I am not manufacturing one
Zero long_term candidates captured, deliberately. `config/strategy.md` asks for
real time on this lane, and it got it: silver was tested on both the swing and
the long clock and failed both (R:R 1.37 against a 2.5 floor); ACN, COST and the
power complex were all examined as de-ratings and rejected on fetched evidence.
The blocker is specific and worth naming: a long_term idea needs **a defended
valuation anchor and a bear-case price**, and `market_data.py` exposes no
fundamentals — no earnings power, book value, FCF or multiple. The only
valuation anchor I could build all run was LCII's, and that one existed because a
merger fixed the exchange ratio for me. Anything else would have been a number I
invented, which is the one thing the report must never ship.

## [06:30 ET] REJECTED (confirmed over 150 days) — IBIT / ETHA — still no overhead
Re-ran both over the full 150-day window rather than the 90 I first used, in case
the short window was hiding real resistance. It was not:
- IBIT close 46.02, **150-day high 46.56** — 1.16% off it. (90-day high was 46.525.)
- ETHA close 19.92, **150-day high 20.12** — 0.99% off it. ATR14 0.76 (3.82%).
Both sit at the highs of every bar available with genuinely nothing above them,
so every target remains constructed and both stay on the watchlist. The earlier
rejection was right for the right reason, now checked against the longer window.

## [06:30 ET] ARITHMETIC CHECK — recomputed every stopped candidate from source
Not trusting my own figures. Recomputed risk, reward, ratio, ATR multiple and the
1/(1+R:R) break-even hit rate independently:
| Sym | Risk | Reward | R:R | ATRx | Floor | Break-even | Claimed | Edge |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XRT | 2.70 | 6.64 | 2.46 | 1.88 | 1.8 | 28.9% | 38% | +9.1pt |
| KMX | 4.20 | 12.28 | 2.92 | 2.37 | 2.0 | 25.5% | 36% | +10.5pt |
| SMH | 27.00 | 89.83 | 3.33 | 1.87 | 1.8 | 23.1% | 33% | +9.9pt |
All three clear their ATR floor and the 2.0 swing floor, and all three claim an
edge of 9-11 points over break-even — none above the 20-point threshold that
would need a bigger thesis to carry it. The ratios are 2.46 / 2.92 / 3.33, which
is deliberately *not* clustered just above 2.0.

## [06:27 ET] RESEARCH COMPLETE
- **candidates: 8 lines, 7 unique symbols.** 3 new ideas, 4 position closes.
  - new: `XRT` sell_short (c3), `SMH` buy (c4), `KMX` buy (c4)
  - closes: `CEG` sell (c3), `TLT` buy-to-cover (c3), `LCII` sell (c4), `NKE` sell (c4)
  - SMH appears twice; the later line supersedes it (stop disclosure, size 3% -> 2%).
- **Skew, stated rather than apologised for:** all 7 are `swing`, and 4 of 7 are
  exits. That is what a 16-position book with a 1/7 hit rate and four unstopped
  or noise-stopped losers actually needed this morning. No intraday idea (the
  market was shut all weekend and I had no live equity tape), no long_term (no
  fundamentals source for a defensible valuation anchor), no crypto, futures or
  event contract (reasons below). I did not manufacture any of them.
- **Coverage gaps:**
  - **Index/macro prices unavailable all run** — Yahoo returned HTTP 429 for
    ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES=F, NQ=F, DX-Y.NYB, ^TNX, GC=F, CL=F.
    No VIX, no dollar, no futures print anywhere in this report. Used liquid ETF
    proxies via finnhub instead and said so.
  - **Options-implied move unavailable** — yahoo-options HTTP 401 on every
    symbol. The SMH and XRT targets were NOT checked against what options price,
    which `config/strategy.md` requires. Named in SMH's counter_argument.
  - **Event contracts unavailable** — Kalshi returned 0 markets for "Fed
    decision", "unemployment", "GDP", "government shutdown", "Bitcoin", and only
    null-priced tennis markets for "Fed". Three event contracts are sitting in
    "awaiting entry" and none could be re-checked; two reference a September Fed
    decision that has now happened.
  - **Short interest unavailable** — `short` timed out on api.nasdaq.com for both
    COST and KMX. No days-to-cover read on any name today.
  - Not reached: healthcare/biotech beyond the XBI level, financials beyond KRE,
    international ex-EEM, and any systematic small-cap screen (I could only reach
    small caps via the earnings calendar, which is a narrow door).
- **Sources that failed:** yahoo (429, all index/FX/commodity), yahoo-options
  (401), kalshi/events (empty), api.nasdaq.com `short` (ReadTimeout x2),
  coingecko `prices` inside `macro` (the standalone `crypto` call worked).
- **Sources that worked:** FRED (all series), finnhub (quotes, earnings calendar,
  insiders, analysts, profile), nasdaq (history/ATR/SMA), SEC EDGAR (filings —
  the LCII merger and the KHC listing transfer both came from there), coingecko
  (standalone), computed relstrength.
