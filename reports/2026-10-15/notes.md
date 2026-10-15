# Research log — 2026-10-15

## [06:03 ET] MACRO — rates, policy, regime
Session: pre-market (US equities closed; freshest honest equity price = prior close 2026-10-14).
- US 10y 5.21% (FRED DGS10, 2026-10-13) — source: https://fred.stlouisfed.org/series/DGS10
- US 2y 4.79% (FRED DGS2, 2026-10-13) — source: https://fred.stlouisfed.org/series/DGS2
- Fed funds effective 3.88%, unchanged d/d (FRED DFF 2026-10-13) — source: https://fred.stlouisfed.org/series/DFF
- 10y-2y spread +0.37, down from +0.42 the prior day (FRED T10Y2Y 2026-10-14) — source: https://fred.stlouisfed.org/series/T10Y2Y
- Unemployment 4.2% Sep, up from 4.1% Aug (FRED UNRATE) — source: https://fred.stlouisfed.org/series/UNRATE
- CPIAUCSL Sep 336.298 vs Aug 334.131 = +0.65% m/m index change, high for one month — source: https://fred.stlouisfed.org/series/CPIAUCSL
- TLT proxy: bonds_20y (TLT) 78.89, +0.66% pre (finnhub)
REGIME READ: 10y at 5.21% with effective funds at 3.88% is a ~133bp positive
spread of the long end over policy — the long end is selling off while policy is
easy. That is term premium/fiscal, not growth. Rising unemployment (4.1->4.2)
alongside a hot monthly CPI print is the stagflationary corner. Implication:
long-duration equity multiples under pressure, real assets and short-duration
cash-generative businesses favoured, and rate-sensitive housing/REITs stay hard.

## [06:03 ET] DATA GAP
- market_data.py macro: spx/ndx/dow/rut/vix/es/nq/dxy/us10y-quote/gold/wti all
  ok:false. Yahoo returning HTTP 429 (rate limited) on every index; finnhub
  refuses indices ("Market data subscription required for CFD indices");
  stooq 404; no alphavantage key. Only bonds_20y (TLT) returned.
- Consequence: no live index level, no VIX, no DXY, no spot gold/WTI this run.
  Equity single-name quotes via finnhub are unaffected (verified below).

## [06:04 ET] CALENDAR — earnings inside the next 7 sessions (fetched, finnhub)
- Thu 2026-10-15 (today): PNC bmo, USB bmo, SCHW bmo, FHN bmo, MRSH bmo, MAN bmo,
  CMC bmo, PLD bmo, BNY bmo; AA amc, IBKR amc, JBHT amc, INDB amc, CNS amc; WHR.
- Fri 2026-10-16: TFC bmo, CFG bmo, MTB bmo, RF bmo, TRV bmo, EEFT.
- Mon 2026-10-19: GE bmo (OPEN POSITION), STLD amc (AWAITING ENTRY), CLF bmo,
  FITB bmo, CCK amc, ZION amc, WAL amc, WRB amc, RLI amc, WTFC amc, BOKF amc.
- Tue 2026-10-20: NFLX amc, GM bmo, COF amc, CB amc, ISRG amc, MMM bmo, NOC bmo,
  RTX bmo, HAL bmo, PM bmo, GPC bmo, EFX bmo, MSCI bmo, UAL amc, ALK amc, KEY bmo.
- Wed 2026-10-21: TSLA amc, META amc, IBM amc, LRCX amc, TXN amc, T bmo, ABT bmo,
  ELV bmo, DHR bmo, TMO bmo, NEE bmo, CME bmo, CSX amc, LUV amc, LVS amc, URI amc.
- Thu 2026-10-22: PG bmo, GD bmo, LMT bmo, HON, NEM bmo, DOW bmo, VLO bmo,
  UNP bmo, NSC bmo, CMCSA bmo, SPOT bmo, GILD, DECK, BX bmo, NVR bmo, PHM bmo.
- Fri 2026-10-23: XOM, AXP bmo, SLB bmo, FCNCA.
Source: https://finnhub.io/api/v1/calendar/earnings (via scripts/market_data.py earnings --days 12)
Note: this week is a bank/financials week; next week is the megacap + industrial week.

## [06:06 ET] TAPE — 2026-10-14 close (all prices = prior close, session closed, finnhub, asof 2026-10-14T20:00Z)
Risk-off, and specifically a *duration* risk-off. Down hard: CCJ -5.43%,
CEG -5.49%, SNX -4.45%, MU -4.10%, DAL -3.67%, SMMT -2.51%, EEM -2.05%.
Up: HII +2.59%, PFE +2.96%, KHC +1.20%, XLE +0.64%, TLT +0.66%.
Crypto also down: BTC 81,185 (-2.35% 24h), ETH 2,372.79 (-4.85%), SOL 103.04
(-3.19%) — source: https://www.coingecko.com/
This is the regime read confirming itself in one session: 10y at 5.21% hit
high-multiple/long-duration (power, memory, uranium, EM) and lifted defensives
(pharma, staples, energy, defense, Treasuries). Note the tell — TLT up *and*
equities down is not a growth scare, it is positioning unwinding off an
oversold long end.

## [06:07 ET] POSITION UPDATE — CCJ — opened 2026-08-17, entry 94.00, last 81.47 (-13.3%)
- STOP BREACHED. Stop was 82.50; 2026-10-14 close 81.47 is 1.03 below it.
- decision: CLOSE. Not a stop to move, not a thesis to re-argue — it triggered.
- why: the stop is the level at which the thesis was declared wrong, and a -5.43%
  session took it through. CCJ has been recommended 2x in the last 10 days; the
  prior-context repetition warning plus a breached stop is a close, not a hold.
- action: captured via add_candidate.py as a close/exit update.

## [06:07 ET] POSITION UPDATE — DAL — opened 2026-10-05, entry 83.00, last 76.65 (-7.7%)
- STOP BREACHED. Stop was 78.10; 2026-10-14 close 76.65 is 1.45 below it.
- decision: CLOSE. DAL was recommended 3x in 10 days — exactly the anchoring
  pattern prior_context flags. UAL reports 2026-10-20 amc and AAL 2026-10-22,
  so the sector catalyst is still ahead, but that is a reason to re-enter later
  on evidence, not to sit through a triggered stop.
- action: captured via add_candidate.py as a close/exit update.

## [06:12 ET] LEVELS — fetched 120-day history, prior-close basis (nasdaq via market_data.py)
| Sym | Close 10-14 | ATR14 | ATR% | 20d | 50d | range low-high | off high |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PM   | 205.58 | 4.44  | 2.16% | 193.25 | 190.72 | 160.67-207.76 | -1.05% |
| LMT  | 522.23 | 9.80  | 1.88% | 515.96 | 544.67 | 487.15-612.75 | -14.77% |
| TRV  | 377.82 | 5.96  | 1.58% | 366.09 | 369.19 | 287.11-398.70 | -5.24% |
| STLD | 242.92 | 6.53  | 2.69% | 234.42 | 240.31 | 216.36-288.74 | -15.87% |
| SCHW |  96.80 | 1.73  | 1.79% |  98.95 | 105.03 |  83.96-114.53 | -15.48% |
| NOC  | 495.69 | 10.70 | 2.16% | 496.78 | 528.29 | 470.06-594.51 | -16.62% |
| CCJ  |  81.47 | 3.22  | 3.95% |  88.46 |  94.46 |  81.22-125.60 | -35.14% |
| DAL  |  76.65 | 2.50  | 3.26% |  82.29 |  82.94 |  65.82- 95.68 | -19.89% |

## [06:13 ET] REJECTED — TRV — price at the highs but the street is going the other way, and the print is tomorrow
TRV looked like the cleanest rate-regime long on the tape: an insurer reinvesting
at a 5.21% 10y, closing 377.82 above both the 366.09 20-day and the 369.19
50-day, only 5.24% off its 398.70 range high, with Q3 out 2026-10-16 bmo.
The positioning read kills it. Analyst bullish share is 25.7% and FALLING 7.6pp
over four months, with the sell count rising 1 -> 2 -> 5 -> 5 and hold stuck at
21 of 35 — revision_direction "deteriorating". Insiders are net -$36.3M over six
months on 25 sales and zero open-market buys. A long here is buying a chart the
analysts are leaving, one session before a binary print, where Q3 is the
hurricane-loss quarter. At a 1.58% ATR the 2.0 ATR swing floor puts the stop at
365.9 — exactly where a cat-loss miss would gap straight through.
- source: https://finnhub.io/api/v1/stock/recommendation (via market_data.py analysts TRV)
- source: https://finnhub.io/api/v1/stock/insider-transactions (via market_data.py insiders TRV)

## [06:13 ET] POSITIONING — the two names that passed the analyst screen
- PM: bullish share 74.1%, improving +1.0pp; 20 of 27 ratings buy-or-better and
  ZERO sell or strong_sell across all four months. No insider sales at all in six
  months. Price 205.58, 1.05% off the 207.76 range high, 6.4% above the 20-day.
  source: https://finnhub.io/api/v1/stock/recommendation
- LMT: bullish share 46.4%, improving +7.1pp — the largest positive revision in
  the batch. strong_buy 5 -> 6 and hold 16 -> 14, so the move is upgrades out of
  hold, not new initiations. Price 522.23 but 14.77% off the 612.75 high and
  BELOW the 544.67 50-day. Insiders ~flat (9 sales totalling $118K, immaterial).
  source: https://finnhub.io/api/v1/stock/recommendation

## [06:13 ET] DATA GAP — event contracts
- market_data.py events returns count 0 for "KXFEDDECISION", "Fed decision",
  "interest rate" and "10-year", and for "CPI" and "recession". The query "Fed"
  returns six markets, all of them unrelated tennis cross-category contracts
  with null bids, asks and volume.
- Consequence: no event-contract idea can be sourced this run. Two event
  contracts already sit in Awaiting entry (KXFEDDECISION-26OCT-H25 YES @ 28,
  KXFEDDECISION-26SEP-H0 YES @ 47) and I cannot re-price either, so neither is
  amended today. The 26SEP contract is by its ticker already past resolution.

## [06:16 ET] REJECTED — ITB / PHM / NVR — the housing short is right and already paid
The regime read points straight at a homebuilder short: 10y 5.21%, builders
report 10-20 to 10-22 (TMHC 10-20, MHO 10-21, NVR/PHM 10-22). The prices say
the trade has already happened and there is nothing left to sell into:
- ITB 83.39, which is 1.6% off its 120-day LOW of 82.0801 and 21.6% off the high.
  The pending 2026-09-24 short was published at 89.80 — that is now 7.7% ABOVE
  the market. It never filled, the sector went our way without us, and chasing
  it at the range low is selling the hole.
- PHM 109.35, 2.05% off its 107.155 range low, 20d 116.00 and 50d 122.14 overhead.
- NVR 5733.12, 4.22% off its 5501.01 range low (and a short needs a whole
  $5.7K share on margin).
Decision: do NOT amend ITB to a chaseable level. Leave the 89.80 pending short
where it is and let it expire unfilled. A short entry 7.7% above the market is
honest about never filling; moving it down to 83 would be reverse-engineering an
entry to the price, which is the failure mode this report is built against.
- source: https://www.nasdaq.com/market-activity/etf/itb/historical

## [06:16 ET] LEADERSHIP — energy is the only sector at a new high
- XLE 67.63, 0.13% off its 120-day high 67.718; 20d 63.62, 50d 63.15. Up 10
  sessions out of 11 from 61.54 on 09-29. ATR 1.22 (1.81%).
- XOM 177.01, 0.24% off its 120-day high 177.43; 20d 164.77 (+7.4% above),
  50d 162.74 (+8.8% above). 161.35 -> 177.01 in 11 sessions. Q3 on 2026-10-23.
  ATR 3.21 (1.81%). 30d avg dollar volume $2.32B.
This is the one place where the leadership and the macro agree: energy is a
short-duration real-asset cash flow, which is exactly what a 5.21% 10y rewards,
and it was green on a day that took 5% out of uranium and power.
- source: https://www.nasdaq.com/market-activity/stocks/xom/historical

## [06:17 ET] EARNINGS SURPRISE RECORDS (fetched, finnhub; last 4 quarters act vs est)
- PM:   2.20/2.1077 +4.4%, 1.96/1.8821 +4.1%, 1.69/1.7501 -3.4%, 2.24/2.1573 +3.8% -> 3 of 4
- LMT:  7.94/7.1846 +10.5%, 6.44/6.793 -5.2%, 7.43/5.76 +29.0%, 6.95/6.4242 +8.2% -> 3 of 4
- NOC:  7.68/6.8881 +11.5%, 6.14/6.1157 +0.4%, 7.23/7.0357 +2.8%, 7.67/6.5201 +17.6% -> 4 of 4
- STLD: 3.81/3.7092 +2.7%, 2.78/2.8409 -2.1%, 1.82/1.7248 +5.5%, 2.74/2.6911 +1.8% -> 3 of 4
- source: https://finnhub.io/api/v1/stock/earnings

## [06:17 ET] DATA GAP — short interest
- market_data.py short returns ok:false for PM, LMT, NOC and STLD, all with
  "ReadTimeout ... api.nasdaq.com ... (read timeout=20)". No short interest or
  days-to-cover figure is available this run, so no idea below cites one.

## [06:17 ET] REJECTED — NOC — best earnings record on the tape, worst revision trend
4-for-4 beats including +17.6% and +11.5%, and +2.97% on 10-14. But bullish
share is 60.7% and FALLING 3.6pp, price 495.69 sits BELOW both the 496.78 20-day
and the 528.29 50-day, and Q3 is 2026-10-20. LMT is the same sector trade with
the revision trend pointing the other way (+7.1pp) and price above its 20-day,
so NOC is the redundant one under the 3-per-driver correlation cap — HII is
already a live defense position.

## [06:17 ET] REJECTED — TLT / duration long — contradicts the live book
A 5.21% 10y is the most interesting long-duration entry in two decades and TLT
closed 78.89 (+0.66%). Not taken: the book already carries a pending TLT
SELL_SHORT at 79.90 and a live IYR short, both of which are the same bet the
other way, and the regime read above says the long end is selling off on term
premium rather than rallying on growth fear. Publishing a duration long today
would be the report arguing with itself inside one sheet.

## [06:24 ET] 52-WEEK HIGHS — and why the leadership does not pass the floor
Fetched 250-day history. XOM, PM and XLE are all at **52-week highs** — their
120-day high and their 250-day high are the same number, so there is no overhead
resistance anywhere to anchor a target to:
- XOM 177.01, 250d range 110.385-177.43, sma200 151.16 (price +17.1% above it)
- PM  205.58, 250d range 142.11-207.76, sma200 179.43 (price +14.6% above it)
- XLE  67.63, 250d range  42.35- 67.718, sma200 57.39 (price +17.9% above it)

## [06:25 ET] REJECTED — XOM — the right sector, an extended entry, and the floor says so
Entry on a breakout above the 177.43 high = 178.20. The true invalidation is
the pre-breakout consolidation top: lows 166.71 (10-08) and 167.82 (10-09), with
the 20-day at 164.77. A stop at 166.40 is 11.80 points = 3.67 ATR of risk.
Conservative continuation target: XOM added 15.66 points in 11 sessions
(161.35 -> 177.01 = 1.42/session); haircut to half that rate over 20 sessions
gives 192.4. That is reward 14.20 against risk 11.80 = **1.20:1**, far under the
2.0 swing floor.
The only way to make XOM print a 2:1 is a stop at 170.80 — tucked under the
10-12 low, 2.30 ATR, inside the move it is supposed to survive. That is the KRE
pattern CLAUDE.md names explicitly: lifting the ratio by walking the stop in
while making the trade strictly worse. Not doing it. XOM goes to the watchlist
as the sector's confirmation, not as today's entry.

## [06:26 ET] REJECTED — PM — same structure, same verdict, stronger evidence wasted
PM has the best analyst book screened (74.1% bullish, improving, zero sells in
four months, no insider sales in six), 3-of-4 beats, and Q3 on 2026-10-20 bmo.
It still fails. Entry above the 207.76 high = 208.40. The real invalidation is
the 10-08 breakaway day's low of 192.97, which is also where the 193.25 20-day
sits — below there the whole October move (187.46 on 10-02 to 205.58, +9.7% in 9
sessions) has failed. Stop 192.40 = 16.00 points = 3.60 ATR. Conservative
continuation at half the realised 2.01/session rate over 20 sessions = 228.5,
so reward 20.10 against risk 16.00 = **1.26:1**. Under the floor.
Forcing it would mean a 198.40 stop at 2.25 ATR, 10 points under an entry on a
9-session vertical move. Watchlist, and worth re-testing after the 10-20 print
from a consolidated base rather than from the top of the move.

## [06:27 ET] REJECTED — LMT — no real resistance sits far enough away
LMT is the best *evidence* on the tape: revision trend +7.1pp, the largest in the
batch, driven by upgrades out of hold (strong_buy 5->6, hold 16->14); 3-of-4
beats including +29.0% and +10.5%; Q3 2026-10-22; and it outperformed its own
sector over 3m (+1.70% vs XLI -7.28%) while lagging SPY badly over 6m
(-14.54% vs +9.95%), which is the de-rating in one line.
It fails on geometry. Entry 524.00 on continuation of the 10-14 engulfing bar
(508.01 open to 522.23 close, high 523.08, on 1.48M shares vs ~0.9M typical).
True support is the 497.00/498.55 two-week floor, so stop 496.50 = 27.50 points
= 2.81 ATR. The nearest real resistance is the September shelf at 537-542.61
(highs 542.61, 538.10, 537.82, 537.00) reinforced by the 544.67 50-day — only
+3.5% to +4.0% away, which is reward 24.61 against risk 27.50 = **0.89:1**.
Clearing 2:1 needs a 579 target and there is no level at 579; the next real one
is the 612.75 120-day high at +16.9%, which is a 9-ATR move and not a swing.
Watchlist. Re-test after the 10-22 print if it builds a base above 545.
- source: https://www.nasdaq.com/market-activity/stocks/lmt/historical

## [06:27 ET] DATA GAP — options-implied move
- market_data.py implied returns ok:false, "HTTPError: 401 Client Error:
  Unauthorized for url: https://query1.finance.yahoo.com/v7/finance/options/..."
  No idea this run cites an options-implied move or compares a target to it.

## [06:28 ET] METHOD NOTE — what today's tape does to the floor
Three of the four strongest names screened are at 52-week highs on 9-11 session
vertical moves. A breakout at a 52-week high has no overhead level to target and
its true invalidation is the base it left, which is 3.5-3.7 ATR below — so the
2:1 floor and the 2.0 ATR stop floor cannot both be satisfied without inventing
a target or tightening the stop. That is the framework working, not failing: it
is refusing momentum chases. The names that pass today are mid-range ones with a
real level above and a real level below, which is why STLD qualifies and XOM,
PM and LMT do not.

## [06:30 ET] SCREEN — mid-range names with a dated catalyst inside 10 sessions
Fetched 250-day history on GM, COF, DOW, UNP, GILD, HAL. One passed.
- UNP 286.43 | atr 4.00 (1.4%) | 20d 276.78 | 50d 288.01 | 200d 266.55 | 250d 215.53-315.99 | -9.35% off high -> **TAKEN**
- GM 83.05 | atr 2.14 | 20d 81.83 | 50d 84.52 | 200d 80.68 | 250d 56.81-91.85 | -9.58% off high
- COF 194.35 | atr 4.38 | 20d 197.86 | 50d 208.88 | 250d 174.24-228.14 | -14.81% off high
- DOW 29.19 | atr 0.77 | 20d 28.29 | 50d 29.60 | 200d 32.22 | 250d 20.93-42.74 | -31.70% off high
- GILD 153.54 | atr 3.56 | 20d 149.34 | 50d 145.82 | 250d 121.39-154.20 | -0.43% off high
- HAL 32.83 | atr 0.79 | 20d 32.63 | 50d 34.07 | 200d 35.62 | 250d 21.46-43.59 | -24.68% off high

## [06:31 ET] REJECTED — GM — mid-range, right catalyst, 1.44:1
Q3 2026-10-20 bmo, consensus 3.7208. Entry above the 84.52 50-day = 84.80. True
support is the 80.04 (09-24) / 80.63 (10-07) low cluster reinforced by the 80.68
200-day, so stop 79.90 = 4.90 = 2.29 ATR. The only real level above is the 91.85
250-day high: reward 7.05 against risk 4.90 = **1.44:1**. A 2:1 needs 94.60 and
there is no level at 94.60.

## [06:31 ET] REJECTED — COF — below both moving averages into a print
194.35 sits under the 197.86 20-day AND the 208.88 50-day, 14.81% off the high,
with Q3 on 10-20 amc. A long is fighting both averages; a short into a print on a
name already 15% de-rated is selling the hole. Neither side qualifies. No row.

## [06:31 ET] REJECTED — GILD — at the 52-week high, same geometry as XOM and PM
153.54 against a 250-day high of 154.1999, so 0.43% off it, with the 20-day
(149.34) and 50-day (145.82) both below and rising. Q3 10-22. No overhead level
to target and the true invalidation is the base below the 20-day, so the breakout
cannot clear 2:1 honestly. Watchlist with XOM and PM.

## [06:32 ET] REJECTED — HAL and DOW — real de-ratings, but only a 25-44% target clears the floor
Both are the most interesting *value* on the tape and neither works as a swing:
- HAL 32.83 is 24.68% off its 43.59 high and BELOW its 35.62 200-day, compressed
  into 31.26-33.19 for four weeks, while XLE sits at a 52-week high — a genuine
  intra-sector divergence worth remembering. Entry above the 34.07 50-day = 34.20,
  stop 31.10 under the 31.26/31.415/31.45 base lows = 3.10 = 3.94 ATR. The next
  real level up is the 35.62 200-day: reward 1.42 against risk 3.10 = **0.46:1**.
  Only the 43.59 high clears the floor, at +27.5%, which is not a swing.
- DOW 29.19 is 31.70% off its 42.74 high, below the 32.22 200-day. Entry above the
  29.60 50-day = 29.70, stop 27.10 under the 26.605/27.20 base lows = 2.60 =
  3.37 ATR. Next real level is the 32.22 200-day: **0.97:1**. Only the 42.74 high
  clears, at +43.9%.
Both are the shape of a long_term idea rather than a swing, and neither is taken
today because I have no fetched valuation anchor for either — no earnings power,
no replacement-cost number, no balance sheet read. Publishing a long_term call on
a chemical or an oil-service trough without a defended bear-case price would be
the thing config/strategy.md refuses: "a long-term idea whose downside you cannot
put a price on is not researched enough to publish." Both to the watchlist, named
as the next run's first stop.

## [06:33 ET] REJECTED — crypto — no fetched BTC history, and the proxy fails the floor anyway
- market_data.py history BTC-USD returns ok:false on all five sources (nasdaq no
  rows, yahoo HTTP 429 twice, twelvedata and alphavantage no api key, stooq no
  rows). So there is NO fetched BTC OHLCV, no BTC ATR and no BTC support level
  this run. Spot is available (coingecko: BTC 81,185 -2.35%, ETH 2,372.79 -4.85%,
  SOL 103.04 -3.19%) and a spot price alone cannot underwrite a level.
- Used IBIT as the only fetchable BTC proxy: 46.24, 250d range 32.84-65.9699 so
  29.91% off the high, 20d 47.26, 50d 43.71, 200d 41.83, ATR 1.12 (2.42%).
  A short on a break of the 45.44 range floor (10-08 low) entered 45.20 with the
  stop at 48.00 above the 47.44 10-13 high and the 20-day is 2.80 of risk = 2.50
  ATR, which clears even the crypto floor. But the nearest real level beneath is
  the 41.83 200-day: reward 3.37 against risk 2.80 = **1.20:1**. Only the 32.84
  250-day low clears the floor, at -27%, which is not a swing.
- Also note: IBIT's 4pm ET 10-14 close and coingecko's 6am 10-15 BTC spot are
  taken ~14 hours apart, so I cannot map one to the other precisely enough to
  translate IBIT levels into /MBT levels. No crypto or crypto-futures idea today.

## [06:34 ET] REJECTED — RTX / MMM / HON / ELV / TXN / AXP — second screen, nothing passed
- RTX 186.47 | Q3 10-20 bmo | base floor 179.02/179.95, stop 178.40 = 3.04 ATR;
  the 194.98 200-day gives 0.76:1 and the 201.43 50-day 1.45:1. Fails.
- MMM 164.46 | Q3 10-20 bmo | entry 165.20 above the 164.99 20-day, stop 158.40
  below the 159.21 base low and the 160.68 200-day = 2.01 ATR. Resistance is a
  tight five-day cluster at 170.43-170.98 reinforced by the 170.94 50-day:
  reward 5.55 against risk 6.80 = **0.82:1**. Only the 184.895 high clears.
- HON 207.61 | the fetched 250-day "range high" of 479.88 is a pre-separation
  price and is not comparable to today's share, so every off-high and range
  figure for HON this run is meaningless. Excluded on data grounds, not on merit.
- ELV 428.09 | 1.87% off its 436.24 high with the 20-day 403.10 and 50-day 402.36
  6.2% below. At-the-high geometry, same as XOM/PM/GILD. Watchlist.
- TXN 280.65 | Q3 10-21 amc | the closest thing to a pass and still marginal:
  entry 292.00 above the 291.635 10-07 high, stop 271.50 below the 272.31 50-day
  = 2.52 ATR, target the 334.03 250-day high = **2.05:1**. Not taken — 2.05 is
  inside the margin where the ratio is really a rounding artifact, the first real
  resistance at 297.06-298.75 is only +2% away and would have to break first, and
  MU is already a live memory position so a second semi is the same driver.
- AXP 306.95 | 3.28% off its 297.20 range LOW and below the 322.70 50-day. Q3
  10-23. Nothing to buy and nothing left to short.

## [06:35 ET] POSITION UPDATE — holds, no change, no row needed
Checked all 17 open positions against the 2026-10-14 closes. Two closed above
(CCJ, DAL); XLE and GE carry rows. The rest are holds with nothing material
changed, logged here rather than published as filler:
- BCC 73.98 vs 76.50 entry (-3.3%), target 110, no stop (long_term). Hold.
- PFE 29.21 vs 27.60 (+5.8%), +2.96% on the rates-shock day — behaving as the
  defensive it was bought as. Hold.
- IYR 95.93 short vs 97.80 (+1.9% in favour), target 90.50, stop 100.40. The
  5.21% 10y is the thesis and it is working. Hold.
- LULU 94.09 short vs 100.61 (+6.5%), NKE 35.30 short vs 38.40 (+8.1%). Both
  working, both well inside their stops. Hold.
- MU 914.13 vs 960.00 (-4.8%), stop 870 is 4.8% below the last print. Took
  -4.10% in the duration shock. No earnings date inside the fetched 12-day
  calendar. Hold, but it is the next stop-out candidate if the 10y keeps rising.
- SNX 263.76 vs 260.00 (+1.4%), KHC 22.70 vs 23.00 (-1.3%). Hold.
- CEG 279.54 vs 272.00 (+2.8%) after -5.49% in one session; stop 250 is 10.6%
  below. The single worst-hit name in the book on 10-14 and still in profit.
  Hold — the stop has room and the 10-14 move was macro, not company news.
- XLF 54.52 vs 54.23 (+0.5%). Its catalyst is TODAY: PNC, USB, SCHW bmo this
  morning and TFC, CFG, MTB, RF, TRV tomorrow bmo. Published 4x in 10 days per
  prior_context, so no fifth row — the position is open and the plan stands.
- SMMT 15.13 vs 17.10 (-11.5%), stop 14.40 is 4.8% below. A conviction-2 small
  cap doing what a lottery ticket does. Hold to the stop.
- HII 264.53 vs 262.00 (+1.0%), long_term, pacing already updated 10-14. Hold.

## [06:38 ET] LONG_TERM LANE — worked HAL properly, and it fails on the downside
Gave the long-term lane dedicated time rather than leftovers, per
config/strategy.md. HAL was the candidate: the clearest intra-sector divergence
on the tape, 24.68% off its 43.59 high and BELOW its 35.62 200-day while XLE
prints a 52-week high and XOM sits 0.24% off its own.
Evidence gathered, and it is good:
- market cap $27.35B on 833.13M shares (finnhub profile), so a liquid large cap.
- Analyst book 76.5% bullish and improving +0.7pp: 26 of 34 buy-or-better,
  one sell. source: https://finnhub.io/api/v1/stock/recommendation
- **4-for-4 earnings beats**: 0.55/0.5435 +1.2%, 0.55/0.5035 +9.2%,
  0.69/0.551 +25.2%, 0.58/0.5047 +14.9%. source: https://finnhub.io/api/v1/stock/earnings
- READ THE PRIMARY DOCUMENT. The only 8-K since 2026-08 is the 2026-09-16 filing
  (event 2026-09-15), and it is Item 8.01 housekeeping: Maurice S. Smith elected
  Lead Independent Director with a $40,000 additional annual retainer, Robert A.
  Malone remaining a director. No guidance, no charge, no restructuring. So there
  is no company-specific disclosure explaining a 25% de-rating.
  source: https://www.sec.gov/Archives/edgar/data/45012/000004501226000064/hal-20260915.htm
- Insiders: 11 sales $18.2M, zero open-market buys. Absence is not a negative.
Valuation anchor, built from fetched figures only:
- Trailing four quarters actual EPS 0.55+0.55+0.69+0.58 = **$2.37**.
- At 32.83 that is **13.9x trailing**.
- Upside anchor: the 43.59 52-week high is **18.4x** the same $2.37 — a multiple
  the market actually paid for this earnings stream inside the last twelve
  months, not one I invented. 18x on $2.37 = **$42.66**.
- Bear anchor: the 21.46 52-week low is **9.1x** that $2.37. A 20% earnings
  decline to ~$1.90 at an 11x trough multiple is also ~**$21**.
REJECTED on the floor: entry 32.60, target 42.66 (reward 10.06), bear case 21.46
(risk 11.14) = **0.90:1** against a 2.5:1 long-term floor. The de-rating is real
and the downside is as large as the upside, which is precisely the case
config/strategy.md says not to publish. Reaching 2.5:1 off a $21.5 bear case
needs a $60 target, ~38% above the 52-week high, and I cannot defend that.
Watchlist. DOW fails the same test harder (31.70% off high, below its 32.22
200-day, no fetched valuation anchor at all).

## [06:39 ET] NO LONG_TERM IDEA TODAY — and why that is the right answer
Prior context: long_term is 0/3 hit target, avg -15.9% across 9 published ideas.
Three closed trades is noise and I am not over-fitting to it, but it does mean
the lane gets no benefit of the doubt. HAL was the one candidate that earned the
research time and it failed 0.90:1 against a 2.5:1 floor. HII remains the live
long-term position and its pacing was updated 2026-10-14; nothing changed today.
Publishing a long-term call on HAL or DOW without a defended bear-case price
would be filler in the lane least able to afford it.

## [06:40 ET] CONVICTION — scores reconciled to distinct evidence kinds
Re-emitted three candidates after auditing the evidence arrays against the
config/strategy.md table (5 = 4+ kinds, 4 = 3, 3 = 2, 2 = 1):
- STLD raised 4 -> 5. It carries four genuinely distinct kinds
  (dated_catalyst, technical_level, positioning, counter_argument_answered).
- CCJ held at 4, but a bogus `dated_catalyst` entry was REMOVED: "the stop
  triggered on 10-14" is not an event verified against a fetched calendar, it is
  a price fact, and it was already carried by `technical_level`. Three real
  kinds, score 4.
- EEM raised 3 -> 4 and a bogus `dated_catalyst` entry REMOVED for the opposite
  reason: the entry said "no catalyst exists", which is the *absence* of a dated
  catalyst and cannot be evidence of one. Three real kinds, score 4.
A miscounted kind inflates a score invisibly, which is the failure the evidence
array exists to prevent, so the audit matters more than the direction it moves.

## [06:41 ET] WATCHLIST — for synthesis, with the reason each is not actionable
All screened and sourced this run; none clears the floor today.
1. XOM 177.01 — 52-week high, 1.20:1 to a conservative continuation target
2. PM 205.58 — 52-week high, 1.26:1; best analyst book screened (74.1%, 0 sells)
3. GILD 153.54 — 0.43% off its 52-week high, same geometry
4. ELV 428.09 — 1.87% off its 52-week high, same geometry
5. LMT 522.23 — 0.89:1 to the 537-542/50-day resistance shelf; revisions +7.1pp
6. HAL 32.83 — long_term 0.90:1 vs a 2.5 floor; 4-for-4 beats, 76.5% bullish
7. DOW 29.19 — 0.97:1 to its 200-day; no defensible valuation anchor fetched
8. TXN 280.65 — 2.05:1 but resistance at 297-299 first, and MU already holds semis
9. MMM 164.46 — 0.82:1 to the 170.4-171.0 cluster
10. RTX 186.47 — 0.76:1 to its 200-day
11. GM 83.05 — 1.44:1 to its 52-week high
12. IBIT / BTC — 1.20:1 to the 200-day; no fetched BTC history at all
13. ITB 83.39 — pending 89.80 short is 7.7% above market; deliberately not chased
14. COF 194.35, AXP 306.95, NOC 495.69, TRV 377.82, SCHW 96.80 — see rejections

## [06:42 ET] RESEARCH COMPLETE
- candidates: 7 distinct symbols (10 jsonl entries; later entries supersede)
  - CLOSE/EXIT: CCJ (stop breached), DAL (stop breached), EEM (early exit)
  - NEW/AMENDED: UNP (conviction 5, 2.45:1), STLD (conviction 5, 2.51:1)
  - HOLD UPDATES: XLE (at 52-week high, scale plan), GE (trim due at the 10-19 open)
- rejections logged: 20 named symbols plus the crypto and long_term lanes
- SKEW TO REPORT HONESTLY: only two new long ideas, and three of seven rows are
  exits. The tape is bifurcated — the leadership (XOM, PM, XLE, GILD, ELV) is at
  52-week highs where a breakout has no overhead level to target and its true
  invalidation sits 3.5-3.7 ATR below, and the laggards (ITB, PHM, NVR, AXP, HAL,
  DOW) are at or near 52-week lows with nothing left to sell. A 2:1 floor with a
  2.0 ATR stop needs mid-range setups, and UNP and STLD are the two that exist.
  This is the framework refusing momentum chases, not a thin research run.
- coverage gaps: no index/VIX/DXY/gold/WTI levels (yahoo 429 on every index);
  no event contracts at all (Kalshi search returns 0 for every rates/CPI query
  and noise for "Fed"), so neither pending KXFEDDECISION contract was repriced;
  no options-implied move (yahoo options 401); no short interest or days-to-cover
  for any name (api.nasdaq.com read timeouts); no BTC OHLCV on any of five
  sources, so no crypto or crypto-futures idea; HON's range figures are
  pre-separation and unusable. No small-cap idea — there is no screener in
  market_data.py and I did not find one worth publishing by hand.
- sources that failed: yahoo (429 on indices and BTC-USD; 401 on options),
  finnhub indices (CFD subscription required), stooq (404 on index symbols),
  api.nasdaq.com short interest (read timeout, 5 symbols), Kalshi via
  market_data.py events (0 results on 6 of 7 queries)

## [06:43 ET] CONVICTION — DAL reconciled too
DAL's `dated_catalyst` entry (UAL 10-20, AAL 10-22 on the fetched calendar) was
removed on the same reasoning applied to CCJ: those prints are context for a
later re-entry, not evidence for closing the position today — the close is
driven by the breached stop, which `technical_level` already carries. Three real
kinds, score 4. All seven candidates now have conviction matching their count of
distinct evidence kinds: CCJ 3->4, DAL 3->4, EEM 3->4, XLE 3->4, STLD 4->5,
UNP 4->5, GE 2->2.

## [06:44 ET] CONVICTION — GE is deliberately BELOW what its evidence count supports
GE carries two distinct evidence kinds, which the table would score a 3, and it
is published at **2 on purpose**. The 2026-10-14 red team lowered it from 3 to 2
and cut the size from 2.5% to 1% to match, and no new evidence arrived today —
GE closed 307.63 then and 307.02 now. config/strategy.md gives the red team the
power to lower a score, not the model the power to restore one on unchanged
facts, so raising it back to 3 today would quietly reverse a downgrade by
arithmetic. **Do not "correct" GE upward in synthesis or enforcement**; the
mismatch is the record of a deliberate downgrade, and the 1% lottery-ticket size
is tied to it. Every other candidate matches its kind count exactly.

## [06:47 ET] METHOD — the screen that should have been run first
After rejecting 20 names one at a time, the rejections all had one shape, and it
is measurable in a single number: **`pct_off_high / atr14_pct` = how many
ordinary days of range sit between the price and the level you would target.**
A 2:1 ratio on a 2.0 ATR stop needs roughly 4 ATRs of reward, so the target
level has to be **at least ~4.5 ATRs away** or no honest stop can clear the
floor. Checked against every name screened today it explains all of them:
- PASS: UNP 6.9 ATRs to high, STLD 5.9, CME 5.9
- FAIL: XOM 0.1, PM 0.5, GILD 0.2, ELV 0.7, DHR 2.7, LMT 2.1 (to its real shelf
  at 537-542, not to its distant high), CB 2.8, URI 3.6
This is why today's rejections are not fastidiousness: a tape where the leaders
sit 0-1 ATRs from their 52-week highs cannot produce a 2:1 long in the leaders,
by arithmetic. Worth running as the FIRST filter on future runs instead of last.

## [06:48 ET] SCREEN 3 — ran the ratio across 18 more names with catalysts in 10 sessions
ABT, DHR, URI, DECK, CMCSA, NDAQ, CSX, NSC, CME, MSCI, ISRG, CB, LVS, IBM, T,
NEM, SLB, GD. Ratio alone is necessary and not sufficient — it also needs price
to be above its 50-day (otherwise the "room to the high" is just a downtrend) and
a tight base to stop against. Only CME satisfied all three.
- **CME 285.59 | 5.86 ATRs to high | above the 20d 270.96, 50d 272.68 AND 200d
  278.54 -> TAKEN at 2.33:1**
- CSX 48.28 (7.20) and NSC 323.73 (7.09) both qualify on geometry and are RAILS —
  the same driver as UNP, which is already taken. Declined on the correlation
  cap rather than on merit; CSX reports 10-21 amc and NSC 10-22 bmo, so both are
  live reads on the UNP thesis and are named in its catalyst action.
- MSCI 560.52 (7.14) above the 20d and 50d but below the 572.35 200-day, which
  sits only 2.1% overhead and caps any target. Fails.
- GD 334.66 (9.84), IBM 227.88 (13.16), T 23.05 (8.12), SLB 48.51 (6.84),
  NEM 111.56 (5.97), LVS 37.02 (20.46) — all BELOW their 50-day, several below
  their 200-day. The room to the high is a measure of how far they have fallen,
  not of upside. No base to stop against. All fail.
- ABT 102.97, DECK 82.82, CMCSA 21.05 — below their 50-day and 200-day. Fail.
- CB 350.15 (2.84) — 4.31% off its high. At-the-high geometry. Fail.
- NDAQ 91.96 (4.49) below the 20d and 50d; entry above the 94.67 50-day with the
  stop under the 90.52 200-day gives 1.38:1. Fail.

## [06:49 ET] REJECTED — ISRG — the 200-day sits directly on top of it
420.24, 11.10 ATRs off the 603.88 high, above the 407.27 20-day and well above the
389.56 50-day, Q3 10-20 amc. Looks ideal on the ratio and is killed by one level:
the 200-day is 441.10, just 2.5% overhead. Entry 430.50 above the 430.00 high of
10-13 with the stop at 407.00 below the 407.70 low of 10-08 and the 20-day is
23.50 of risk = 2.04 ATR, against reward 10.60 to the 200-day = **0.45:1**. The
only level beyond it is the 603.88 high at +40%, which is not a swing. This is the
clearest case of the ratio being necessary but not sufficient.

## [06:50 ET] CORRELATION CHECK — drivers across the 8 published rows
Per the 3-per-driver cap in config/strategy.md:
- Rates/financials: CME (rate-futures volume) + XLF (open, banks, not in a row
  today) = 1 published row. CSX and NSC were declined partly to keep rails at 1.
- Rails/freight: UNP = 1.
- Steel/industrial cyclical: STLD = 1.
- Energy: XLE = 1 (XOM rejected, which also keeps this at 1).
- Defense/aerospace: GE = 1 (HII open but not in a row; LMT, NOC, RTX, GD all
  rejected).
- Exits: CCJ, DAL, EEM — no forward driver exposure.
No driver carries more than one new row. The report is not eight versions of one
bet; the honest criticism is the opposite, that it is thin on new longs.

## [06:51 ET] RESEARCH COMPLETE (supersedes the 06:42 block)
- candidates: **8 distinct symbols** (12 jsonl entries; the last entry per
  symbol is the live one and supersedes all earlier entries for that symbol)
  - NEW/AMENDED LONGS: UNP (conv 5, 2.45:1), STLD (conv 5, 2.51:1, amended entry
    247.80 from the pending 245.50), CME (conv 5, 2.33:1)
  - CLOSE/EXIT: CCJ (stop breached intraday 10-14), DAL (stop breached intraday
    10-14), EEM (early exit, stop 1.36 ATR away after five lower closes)
  - HOLD UPDATES: XLE (52-week high, scale plan, stop deliberately NOT raised),
    GE (trim of half the remaining 1% due at the 10-19 open)
- rejections logged with levels and ratios: XOM, PM, LMT, NOC, TRV, GM, COF,
  GILD, HAL, DOW, RTX, MMM, ELV, TXN, AXP, SCHW, ITB, PHM, NVR, HON, ISRG, DHR,
  URI, NDAQ, CSX, NSC, MSCI, GD, IBM, T, SLB, NEM, LVS, ABT, DECK, CMCSA, CB,
  TLT, IBIT/BTC — 39 named symbols plus the long_term and crypto lanes
- SKEW TO REPORT HONESTLY: three new longs, three exits, two holds. Three of the
  eight rows reduce risk rather than add it. No long_term idea (HAL failed
  0.90:1 against a 2.5 floor), no crypto idea (no fetched BTC history and the
  IBIT proxy failed at 1.20:1), no event contract (no market data at all), no
  small cap (no screener available and none found by hand), no intraday idea
  (the tape offered no gap or dated intraday print worth one). All three new
  longs are conviction 5 and all three are breakout entries ABOVE the market,
  which is deliberate: prior context records the first month ran 31 pullback
  entries against 1 breakout with a 42% fill rate, the fills selected for the
  ideas already failing. Expect a low fill rate here and treat never-filling as
  the modal outcome, not a failure.
- coverage gaps: no index, VIX, DXY, spot gold or WTI level (yahoo HTTP 429 on
  every index symbol, finnhub refuses indices, stooq 404); no event contracts
  (Kalshi returns 0 results for KXFEDDECISION, "Fed decision", "interest rate",
  "10-year", "CPI" and "recession", and unrelated tennis markets for "Fed"), so
  neither pending KXFEDDECISION contract could be repriced and the 26SEP one is
  past resolution by its own ticker; no options-implied move (yahoo options 401);
  no short interest or days-to-cover for any name (api.nasdaq.com read timeouts
  on 5 of 5 attempts); no BTC OHLCV on any of five sources; HON's range figures
  are pre-separation and unusable.
- sources that failed: yahoo chart API (429 on indices and BTC-USD), yahoo
  options API (401), finnhub indices (CFD subscription required), stooq (404 on
  index symbols), api.nasdaq.com short interest (read timeout x5), Kalshi via
  market_data.py events (0 results on 6 of 7 queries)

## [06:53 ET] ** HANDOFF TO SYNTHESIS AND RED TEAM — READ THIS BEFORE --enforce **
I pre-computed what `validate_report.py` will say about all eight candidates,
using its own formulae (`abs(target-entry)/abs(entry-stop)`,
`baseline = 1/(1+rr)`, `expectancy_r = wp*rr - (1-wp)`, `stop ATR = abs(entry-stop)/atr14`):

| sym | rr | baseline | wp | expectancy | stop ATR | floor | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CCJ  | 3.57 | 0.219 | 0.20 | **-0.086R** | 3.57 | 2.0 | expectancy FAIL |
| DAL  | 2.35 | 0.299 | 0.20 | **-0.330R** | **1.96** | 2.0 | expectancy FAIL + stop ATR FAIL |
| EEM  | 2.27 | 0.306 | 0.25 | **-0.182R** | 2.55 | 1.8 | expectancy FAIL |
| STLD | 2.51 | 0.285 | 0.36 | +0.264R | 2.50 | 2.0 | pass |
| UNP  | 2.45 | 0.290 | 0.38 | +0.311R | 2.80 | 2.0 | pass |
| CME  | 2.33 | 0.300 | 0.39 | +0.299R | 2.82 | 2.0 | pass |
| XLE  | 2.13 | 0.319 | 0.60 | +0.878R | 2.54 | 1.8 | pass, expect an edge WARN |
| GE   | 2.06 | 0.327 | 0.36 | +0.102R | 2.28 | 2.0 | pass, thinnest on the page |

**The three expectancy failures are the three EXIT rows, and the failure is the
point of them.** CCJ, DAL and EEM are recommendations to SELL. A close carries
negative forward expectancy by definition — that the trade no longer pays is
precisely why it is being closed — and the low `win_probability` on each is an
honest statement that the historical target will not be reached, not a defect in
the idea.

`--enforce` removes FAIL ideas from `recommendations` and rewrites them as
watchlist entries reading "Republish only once the numbers check out." Applied
here that **deletes the instruction to sell three positions**, two of which have
already breached their stops, and leaves them looking like ideas awaiting a
better entry. That is a worse outcome than any number being wrong.
**Do not let enforcement demote CCJ, DAL or EEM.** If the pipeline cannot
exempt them, the red team should keep them in `recommendations` and record the
expectancy flag in their validation block as expected-and-correct.

Two further notes on that table:
- **DAL's 1.96 ATR stop is a genuine finding, not an error to fix.** The 78.10
  stop was published on 2026-10-05 against a 2.5022 ATR, so it was set 0.04 ATR
  INSIDE the 2.0 floor at the time. It is left unchanged because a filled
  position keeps the entry it was bought at and the stop it was published with —
  and it is one more instance of the pattern CLAUDE.md records, that all ten of
  the first month's stop-outs had a stop tighter than 1.6 ATR. Do not widen it
  retroactively; the position is being closed.
- **XLE's 0.60 win_probability will trip the >20-point edge WARN (+28pp over the
  0.319 baseline) and it is defensible.** The baseline formula assumes entry at
  the current price; XLE is a position filled at 63.90 that now trades 67.63, so
  5.8% of the move to the 70.50 target has already happened. The remaining
  question is whether 70.50 (4.24% up) trades before 60.80 (10.1% down), from a
  52-week high, with the 20-day 5.9% below. A probability well above a driftless
  coin flip is the honest answer to that, not an inflated claim. If the red team
  disagrees it should lower the number and say so, rather than the number having
  been chosen to avoid the flag.

## [06:56 ET] SMALL-CAP LANE — screened six, rejected six
Hunted deliberately rather than leaving it to leftovers, using the Oct 19-23
earnings calendar for names under ~$2B with a dated catalyst, then the same
ATRs-to-high ratio plus the config/universe.md liquidity floor ($500K average
daily dollar volume) and the above-the-50-day requirement.
| sym | px | mcap | advol/day | off high | atr% | ATRs to high | vs MAs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IIIN | 29.75 | $0.58B | $4.1M | -22.63% | 2.35 | 9.63 | above 20d, below 50d/200d |
| ASPN |  5.16 | $0.43B | $4.5M | -44.80% | 5.34 | 8.39 | below 20d/50d, above 200d |
| TTMI | 103.31 | $10.9B | $221.5M | -53.84% | 8.61 | 6.25 | below all three |
| THRM | 30.61 | $1.67B | $46.2M | -36.69% | 6.27 | 5.85 | below all three |
| MXL  | 78.82 | $7.15B | $235.9M | -38.57% | 10.75 | 3.59 | below 20d, above 50d |
| NPK  | 145.16 | $1.04B | $15.5M | -8.23% | 2.80 | 2.94 | below 20d/50d, above 200d |
All clear the $500K liquidity floor. None is publishable:
- TTMI, THRM below all three moving averages; MXL on a 10.75% ATR, which makes
  any honest stop a 21% move; NPK fails the ratio at 2.94 ATRs.
- **IIIN was the only one above its 20-day and it disqualifies itself on
  evidence, decisively.** The analyst book is **0.0% bullish** — zero buys
  against 3 holds, 1 sell and 2 strong sells, unchanged for four months — and the
  earnings record is 0.46 vs 0.7803 (**-41.0%**), 0.27 vs 0.6528 (**-58.6%**),
  0.39 vs 0.408 (-4.4%) and 0.74 vs 0.6885 (+7.5%): three misses in four
  quarters, two of them by roughly half. Q3 lands 2026-10-22 against consensus
  0.4998 from a company that has missed by 41% and 59% in consecutive quarters.
  That is not an asymmetric early-thesis bet, it is a falling knife with a dated
  trigger attached, and average volume of 138,273 shares a day means the exit is
  narrow when the knife lands.
  sources: https://finnhub.io/api/v1/stock/recommendation , https://finnhub.io/api/v1/stock/earnings
- ASPN at $5.16 with a 5.34% ATR is the only genuine lottery-ticket shape left
  and it sits below both its 20-day and 50-day with no catalyst I could date.
**No small-cap idea today.** config/strategy.md wants this lane and says
explicitly not to pad it; six screened and six rejected on stated grounds is the
honest outcome. Note for future runs: market_data.py has no screener, so the
small-cap lane is limited to names reachable by hand off the earnings calendar,
which is a structural coverage gap rather than a one-day miss.

## [06:58 ET] VENUE CHECK — all eight candidates
- UNP, CME, STLD, GE, CCJ, DAL: US-listed common stock (NYSE/Nasdaq),
  `Robinhood Stocks`, direction `buy` on every row including the three exits,
  which amend existing long positions. No margin required on any of them.
- XLE, EEM: US-listed ETFs, `Robinhood Stocks`, long. Not leveraged or inverse,
  so no decay caveat applies.
- Nothing recommended is OTC, a warrant, a foreign ordinary, an option, a
  leveraged ETF, under $1, or under the $50M/$500K floors. No `sell_short` row
  today, so no `requires_margin` flag is set anywhere.
- No futures and no event contract this run, so no contract month to state and
  no Robinhood product availability to verify beyond plain listed equities and
  ETFs. The one place a futures substitution would have been required — a
  bearish bitcoin view, which must be `/MBT` rather than a spot `sell` — did not
  produce an idea, because there is no fetched BTC history to set levels on.

## [07:00 ET] RESEARCH COMPLETE (FINAL — supersedes the 06:51 and 06:42 blocks)
- candidates: **8 distinct symbols**, 12 jsonl entries. The LAST entry per symbol
  is the live one.
  - NEW LONGS (all conviction 5, all breakout entries above the market):
    UNP 288.60 -> 315.99, stop 277.40, 2.45:1, 2.80 ATR, +0.311R
    STLD 247.80 -> 288.74, stop 231.50, 2.51:1, 2.50 ATR, +0.264R (amends the
      pending 245.50, which had been published into 247.10 resistance)
    CME 286.80 -> 329.16, stop 268.60, 2.33:1, 2.82 ATR, +0.299R
  - EXITS: CCJ (stop breached intraday 10-14, low 81.22 vs 82.50 stop),
    DAL (stop breached intraday 10-14, low 76.12 vs 78.10 stop),
    EEM (discretionary early exit, stop 1.36 ATR away after five lower closes)
  - HOLDS: XLE (52-week high, scale plan, stop deliberately NOT raised — see the
    counter_argument on that row), GE (trim half the remaining 1% at the 10-19 open)
- 45 named symbols rejected with levels and ratios recorded, plus the long_term,
  crypto, event-contract and small-cap lanes.
- See the 06:53 HANDOFF block before running --enforce: the three exit rows will
  hard-fail check_expectancy by design and must not be demoted to the watchlist.
- coverage gaps and failed sources: unchanged from the 06:51 block — no index/
  VIX/DXY/gold/WTI levels, no event contracts, no options-implied move, no short
  interest, no BTC OHLCV, HON unusable. Added: no screener for the small-cap lane.
