# Research log — 2026-09-02

## [06:05 ET] MACRO — regime
Session context: prices below are **previous close (2026-09-01)**, market closed, age ~842 min.
- SPY 761.78 (-0.69%), QQQ 707.64 (-1.27%), IWM 290.57 (-1.14%) — broad risk-off Sep 1, tech led down
- TLT 81.87 (-0.79%); GLD 396.75 (-2.9% intraday high 401.25) — duration AND gold sold together = a rates shock, not a growth scare
- XLE 64.77 (+1.27%) — only major sector up; energy is the standout bid
- FRED: US10Y 4.75 (2026-08-31, prev 4.73), US2Y 4.34, 10y-2y +0.40 (2026-09-01), fed funds eff 3.63, UNRATE 4.1 (Jul, prev 4.2)
- source: FRED via scripts/market_data.py macro; quotes finnhub
- READ: long end is selling while the front end is anchored — bear steepener. That is a term-premium/supply story, not a
  Fed-repricing story. It is directly hostile to TLT (open position) and to gold, and supportive of energy/value.
- DATA GAP: yahoo returned HTTP 429 for ^GSPC/^NDX/^DJI/^RUT/VIX/DXY/ES/NQ/gold/WTI futures — no VIX or DXY level today.

## [06:06 ET] CALENDAR — dated events in the next 10 sessions
- 2026-09-02 AMC: **AVGO** (est EPS 3.30, rev $29.9B), HPE, SNOW, NTAP, FIVE, GOLD(Barrick), OLLI, WOOF
- 2026-09-03 AMC: **LULU** (est EPS 1.83, rev $2.51B) — I HAVE AN OPEN LULU POSITION; also ZS, DOCU, PATH, GWRE, IOT
- 2026-09-03 BMO: CIEN, CPB, TTC, MOMO, ZGN
- 2026-09-07: GME, DBI
- 2026-09-08: CASY, ABM, UNFI
- 2026-09-09: CHWY, KR, RH, ASO, AEO, SIG, AVAV, CPRT, CNM, COO
- 2026-09-10 AMC: **ADBE** (est EPS 6.20, rev $6.82B)
- 2026-09-14 AMC: ORCL
- source: finnhub earnings calendar via market_data.py

## [06:09 ET] MACRO — THE DRIVER: oil shock -> global bond selloff -> Fed HIKE expectations
- Resumption of strikes in the **Iran war** pushed crude above **$95**, reigniting inflation fears and triggering a
  *global* bond selloff on 2026-09-01. — source: https://finance.yahoo.com/markets/live/stock-market-today-tuesday-september-1-dow-sp-500-nasdaq-080617884.html
- US 10Y hit a **20-month high, 4.788% (+3bp)** — highest since Jan 2025. Reports cite hawkish Fed signals and
  **expectations for a rate HIKE this month**. — source: https://www.fool.com/coverage/stock-market-today/2026/09/01/stock-market-midday-sept-1-stocks-slide-on-global-bond-sell-off/
- **XLE printed a new all-time intraday high** (highest since 1998 inception). — same source
- Gold -1.62% to ~$4,409 spot; GLD -2.9%. Gold selling *with* bonds = real-rate shock, not a risk-off bid.
- IMPLICATION FOR THE BOOK: this is hostile to the open TLT position (long duration into a bear steepener + hike risk)
  and supportive of energy, tankers, and short-duration/value. Do not add duration here.

## [06:10 ET] POSITION REVIEW — quotes are 2026-09-01 closes (market closed, age ~842min)
| sym | last | entry | stop | status |
| LULU | 118.00 | 115.0 | none | +2.6%, **earnings 2026-09-03 AMC** |
| TJX  | 133.27 | 150.85 | 145.50 | **stop breached** (-11.7%) — should already be closed |
| BCC  | 75.84 | 81.0 | 76.00 | **stop breached** (-6.4%) |
| CCJ  | 96.26 | 95.0/88.0 | none | +1.3% |
| NKE  | 38.12 | 40.0/38.0 | none | -4.7% |
| PFE  | 28.55 | 25.8 | none | +10.7% |
| DHT  | 19.69 | 18.8/19.4 | 17.6/17.9 | +4.7% |
| DINO | 103.97 | 93.0 | 86.5 | +11.8% |
| LCII | 100.77 | 94.0 | none | +7.2% |
| RARE | 25.81 | 25.2 | 22.9 | +2.4% |
| SVRA | 5.35 | 5.35 | 4.6 | flat |
| TLT  | 81.87 | 82.6 | 80.95 | -0.9%, thesis now actively contradicted |
| BTC/`/MBTU6` SHORT | BTC 76,659 | 62,950-64,340 | 65,200-66,600 | **stops blown by ~15%** — bookkeeping stale, must be closed |

## [06:07 ET] EVENT MARKET — FOMC Sep 16 2026 is priced for a HIKE
Kalshi KXFEDDECISION-26SEP (close 2026-09-16 17:59 UTC), bid/ask in cents:
- `H25` hike 25bp: **61/62**, last 62, vol 5.72M  <-- this report published YES @32 on 2026-08-22, never filled; it has doubled
- `H0` hold: 38/39, last 39, vol 10.6M
- `H26` hike >25bp: 1/2 | `C25` cut 25bp: 0/1 | `C26` cut >25bp: 0/1
- source: https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXFEDDECISION
- READ: the whole distribution is hike-or-hold. A cut is priced at ~1%. Every rate-sensitive position in this book is
  on the wrong side of that unless it is energy. At 62c the hike is no longer a mispricing — buying it risks 62 to make
  38 (R:R 0.61), so NOT a candidate on its own terms. The value is as a regime read, not a trade.

## [06:07 ET] CAPTURED — TLT sell (exit) — conviction 4
Closing the open TLT long at 81.87. Bear steepener + 62% hike odds + below 20d and 50d on rising volume.

## [06:08 ET] NEWS — the actual driver is a shooting war at the Strait of Hormuz
- **Two oil tankers struck by projectiles in the Strait of Hormuz on Monday night (2026-08-31)** — one Saudi, one South
  Korean, hit within minutes of each other; no casualties. — source: https://www.upi.com/Top_News/World-News/2026/09/01/iran-two-oil-tankers-struck-strait-of-hormuz/7601788274469/
- Trump vows to hit Iran "hard"; Tehran urging a return to the June deal. Iranian missiles and drones have reached
  **Jordan and Bahrain**. IRGC says it intercepted a US MQ-9 over the eastern Strait.
  — sources: https://www.cnbc.com/2026/09/01/us-iran-war-trump-hormuz-tanker-attack-shipping-sanctions-.html
    https://www.cbsnews.com/live-updates/iran-war-us-strikes-strait-of-hormuz-larak-island/
- Brent back over $90, **+~30% vs pre-war levels**. — https://tradingeconomics.com/commodity/brent-crude-oil/news/530749
- This is not a "sentiment" story. It is a physical-supply story with a live chokepoint, and it is what produced
  yesterday's bond selloff, XLE's all-time high, and 62c hike odds. Everything today should be sized against the
  possibility that a ceasefire headline lands overnight and reverses all of it in one session.

## [06:12 ET] STRUCTURAL — Qatar LNG is 96% offline and the damage is measured in YEARS, not weeks
This is the most important non-obvious fact of the day and it is not a sentiment story.
- **Qatar LNG exports have fallen ~96%** since the effective closure of the Strait of Hormuz — 18 cargoes shipped in the
  reporting period against 509 in the same period last year. — source: https://www.azernews.az/region/262917.html
- QatarEnergy has **extended force majeure into November** for Europe/Asia customers (Edison: 5 more cargoes cancelled
  late Sep-early Nov; Pakistan cancellations into October; Bangladesh extended past September).
  — sources: https://www.euronews.com/business/2026/08/31/qatarenergy-extends-lng-cancellations-into-november-as-hormuz-disruption-drags-on
    https://www.bloomberg.com/news/articles/2026-08-28/qatar-extends-lng-force-majeure-as-hormuz-traffic-remains-halted
- **Repairs to the damaged liquefaction trains are estimated at 3-5 years**, ~$20B of annual revenue lost. Analysts now
  see the global gas market not rebalancing until **2028** versus mid-2026 previously.
  — sources: https://gasoutlook.com/analysis/lng-markets-tighten-as-hormuz-disruption-expected-to-persist/
    https://www.gisreportsonline.com/r/gas-markets-hormuz-shock/
- Dutch TTF front-month ~EUR 69.4/MWh. — https://tradingeconomics.com/commodity/natural-gas/news/529885
- WHY IT MATTERS HERE: Qatar is ~20% of seaborne LNG. Losing it for years is a *structural* supply hole that only US
  export capacity can fill. Confirmed in yesterday's tape: on a day SPY fell 0.69% and QQQ fell 1.27%, **EQT closed
  +2.60% and AR +3.46%** — US gas producers were bid while everything else was sold. That is the market already
  starting to price the substitution, and it is a different driver from the crude/XLE/DHT positions already in the book,
  so it does not breach the correlation cap.

## [06:12 ET] REJECTED — AVAV — the de-rating is fundamental, not a war discount
Down 55% from its high (321 -> 144) and closed -2.8% on a day Iran fired missiles at Jordan and Bahrain. Tempting as a
"war stock on sale", but the cause is company-specific: the US Space Force reopened the **$1.7B SCAR program**, removing
an assumed sole-source position; a late-2025 shutdown forced an FY26 guidance cut; and there is securities litigation
alleging understated competitive risk plus accounting issues. Insider check: **0 open-market buys, 10 sells** over 6
months. Earnings 2026-09-09 is a dated catalyst but with live accounting questions it is a coin flip, not an edge.
— source: https://finance.yahoo.com/markets/stocks/articles/avav-stock-slumped-over-40-171703348.html

## [06:12 ET] REJECTED — KTOS, LMT as "war beneficiaries" — the whole defense complex sold off into the escalation
KTOS -59% off high and -3.2% on the day; LMT -21% off high and -3.0%. Whatever is repricing defense, it is not the
Iran headlines, and I could not establish the cause inside the budget. Do not buy a falling sector on a narrative that
the tape is actively rejecting. LMT insiders: 0 open-market buys, 11 sells in 6 months.

## [06:16 ET] EVENT MARKET — August CPI, and a trap I nearly walked into
Kalshi `KXCPIYOY-26AUG` (resolves on the 2026-09-11 08:30 ET BLS release; market closes 08:29 ET), bid/ask cents:
- Above 3.2%: 81/87 (last 82) | Above 3.3%: **50/55** (last 55) | Above 3.4%: **7/20** (last 14)
- Above 3.5%: 1/6 (last 6) | Above 3.8%: 0/3 (last 1)
- source: https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXCPIYOY
- Market's modal August print is ~3.33% YoY.
Ground truth pulled from FRED CPIAUCSL directly (https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL):
  Jul-2026 332.813, Jul-2025 322.169 -> **July YoY = 3.30%**; June YoY = 3.46%; Aug-2025 base = 323.291.
  So >3.4% in August needs the index above 334.28, i.e. **+0.44% m/m**; >3.3% needs +0.35% m/m.
**TRAP:** a web search surfaced a Benzinga "August CPI Preview" claiming headline rising 3.2% -> 3.6% on a 5.9% energy
surge with core falling 4.7% -> 4.3%. Those are the **August 2023** figures almost exactly, the article is undated in
the result, and the URL returns HTTP 403 so I could not confirm it. July 2026 actual is 3.30%, not 3.2%. **Discarded —
not used as evidence anywhere.** Had I traded it, the "edge" would have been a 3-year-old headline.
CONCLUSION: no established edge on the CPI contract. Not captured. The war's crude spike happened on **Sep 1**, which is
September data, not August, so the obvious inflation story does not even land in this print.

## [06:16 ET] ENERGY PRICE LEVEL — from the Kalshi gasoline market
`KXAAAGASW-26SEP07` (AAA national average, closes 2026-09-06 23:59 ET) implies a median around **$4.12/gal**:
above 4.020 at 99c, 4.060 at 94c, 4.080 at 83c, 4.100 at 66c, **4.120 at 48/49**, 4.140 at 34/36, 4.160 at 9/19,
4.200 at 5/6, 4.300 at 0/1. Useful as a corroborating price level for the energy shock even if not traded.

## [06:19 ET] CORRELATION AUDIT — read this before publishing
Nine candidates so far, but they are NOT nine bets. They resolve to four drivers, and the report must say so:
- **Driver A — Strait of Hormuz transit closure** (ends the day there is a ceasefire): `DHT`, `DINO`, `XLE`. That is
  exactly 3, at the correlation cap. Treat as ONE bet of roughly 6.5% of capital. **No further oil-complex names.**
  This is why `VLO`, `MPC`, `PBF`, `CVI` were rejected below, and why `FRO` was not captured despite qualifying.
- **Driver B — destroyed Qatari liquefaction capacity** (does NOT end with a ceasefire; the trains need 3-5 years):
  `EQT`, `CRK`. Two, with room. The distinction from Driver A is real and load-bearing: a ceasefire reopens the strait
  but does not rebuild the trains, so A and B have genuinely different invalidations.
- **Driver C — the rate/inflation consequence**: `TLT` (exit), `IYR` (short), `KXFEDDECISION-26OCT-H25` (yes). Three, at
  the cap.
- **Driver D — idiosyncratic**: `LULU` (Sep 3 earnings).
Second-order truth worth stating plainly: A, B and C all trace back to the same war. A ceasefire helps C (rates fall)
while hurting A, so the book is partially self-hedged — but a *sustained escalation* wins on every line at once, which
is the definition of concentration. Size accordingly.

## [06:19 ET] REJECTED — VLO, MPC, PBF, CVI — the refining trade is already at all-time highs
MPC closed 383.00 against a 150-day high of 383.01 (0.0% off). VLO -0.8% off high, CVI -1.4%, PBF -1.5%. PBF has gone
31.44 -> 74.99 and CVI 19.62 -> 42.87 in 150 days. These are war multiples on an entry with no margin of safety, and
`DINO` already carries the exposure. Correct action on refining today is raising DINO's stop, not adding a fifth name.

## [06:19 ET] REJECTED — FRO (Frontline) — merit fine, correlation cap says no
44.32, 2.1% off its 150-day high, ATR 3.6%, same Hormuz thesis as DHT which is already open. Would be the 4th name on
Driver A. Cut on correlation, not on merit — worth the watchlist.

## [06:19 ET] REJECTED — GLD / GDX — falling knife, no support until the 50-day
GLD 396.75, down from 428.07 on 2026-08-25 — **-7.3% in five sessions** — and -22.2% from the 180-day high of 509.70,
during a week when a shooting war escalated. Gold selling into a war means real rates are dominating, and the ATR is
8.06 with the next real support at the 50-day (386.74). GDX 94.67 sat exactly on its 20-day (94.81) and fell 3.90%.
There may be a trade here once the 50-day holds; there is no defensible entry today.

## [06:19 ET] POSITION UPDATE — BTC / `/MBTU6` SHORTS — stale book, these are long since stopped out
Four short lines are carried as open: BTC spot 2026-08-16 @62,950 (stop 65,200), 2026-08-17 @63,400 (stop 65,200), and
`/MBTU6` 2026-08-18 @64,100 and 2026-08-19 @64,340 (stop 66,600). **BTC is 76,592 this morning** (coingecko, -1.65%
24h). Every one of those stops was breached by roughly 15-19% and the trades are dead; the state file is bookkeeping,
not a position. BITO, the futures proxy, closed 10.38 above both its 20-day (9.50) and 50-day (8.94) in a 7.87-12.54
range — the trend is up.
- decision: **CLOSE all four, do not re-establish, and do not average into a losing short.** No new BTC candidate
  captured in either direction: nothing in today's research gives an edge on crypto, and re-shorting an asset that has
  run 19% against the book is anchoring.
- This cannot be expressed in the candidate schema (there is no "flatten" direction), so it is recorded here and must
  be carried into the report narrative and `data_quality_notes` by synthesis.

## [06:21 ET] POSITION UPDATE — TJX — the stop-out stands, do NOT re-enter. REJECTED as a new idea.
Open line: 2026-08-19 @150.85, stop 145.50. Last **133.27** — the stop was taken and the position is closed at roughly
-11.7%. Reviewed for re-entry because the setup is superficially attractive and, unlike everything else today, it is
uncorrelated with the war: off-price retail is the classic trade-down beneficiary of a consumer squeezed by $4.12
gasoline, and TJX sits at 133.27 against a 150-day low of 133.04.
The Q2 report on 2026-08-19 was good on the parts that matter: EPS 1.22 vs 1.19 expected, sales in line at $15.2bn,
and **full-year EPS guidance raised to 5.31-5.36 from 5.08-5.15** with pretax margin guidance raised to 12.3-12.4%
from 11.9-12.0%. The stock fell on a soft near-term profit outlook.
- decision: **do not re-enter.** At 133.27 on 5.31-5.36 of FY guidance, TJX trades at ~24.9x — the middle of its own
  historical 22-28x band, not a dislocation. The move from 170 to 133 is multiple normalisation, not a de-rating on a
  fixable problem. There is no dated catalyst, it is below both the 20-day (146.87) and 50-day (151.83), and on a
  defensible bear multiple of 22x (~118) against a 160 target the reward-to-risk is 2.0 — under the 2.5 long-term
  floor. A good business at a fair price with no catalyst is a watchlist entry, not a recommendation.
- source: https://www.fool.com/investing/2026/08/19/why-tjx-stock-dropped-today/ and
  https://www.investing.com/news/earnings/tjx-stock-drops-as-profit-outlook-falls-short-of-analyst-estimates-4867203

## [06:21 ET] POSITION UPDATE — BCC — thesis broken by the rate move, close it
Open line: 2026-08-18 @81.00, stop 76.00. Last **75.84** — the stop is breached and the position is closed at -6.4%.
Boise Cascade is a building-products levered bet on housing, and housing is the sector taking the direct hit from a 10y
at a 20-month high: ITB is -19.9% and XHB -18.3% from their highs, both five red days running. BCC has closed lower in
six of the last seven sessions (81.04 -> 75.84) and is below its 20-day (82.08) and 50-day (79.01).
- decision: **close at the stop, do not re-enter.** No candidate captured — re-buying a rate-sensitive cyclical two
  weeks before a meeting that is 62% priced for a hike is fighting the driver.

## [06:27 ET] POSITION UPDATE — NKE — hold with a stop finally attached; STOP RE-PITCHING IT
Two open lines, 2026-08-17 @40.00 and 2026-08-18 @38.00, **both with no stop**, targets 62-65. Last **38.12**, which is
0.4% above the 150-day low of 37.97, 44.3% below the high of 68.49, and below both the 20-day (40.36) and 50-day
(41.70). ATR 1.13.
- decision: **HOLD, attach a hard stop at 36.20** (about 1.7 ATR below the 150-day low), **add nothing**, and take the
  62-65 target off as a live number until there is fresh work to defend it.
- **Not captured as a candidate, deliberately.** NKE has appeared 4 times in 10 days. I did no NKE-specific research
  today, so there is no new information to justify a fifth appearance, and the only thing that has concretely changed —
  a fresh 150-day low into a consumer squeezed by gasoline at +29% year on year — argues for less exposure, not a
  re-pitch. Re-recommending it on macro I gathered for other names would be exactly the anchoring the prior context
  warns about. It belongs on the watchlist with a stop, not in the recommendations.

## [06:27 ET] POSITION UPDATE — PFE — the book's best position, and it has no stop either
Entry 25.80 on 2026-08-18, last **28.55, +10.7%**, and only 1.9% below its 150-day high of 29.09 with a 2.15% ATR — the
lowest-volatility winner in the book, and structurally defensive in a stagflationary tape. Target 38, no stop.
- decision: **HOLD, attach a stop at 26.80** (below the 20-day at 27.42, roughly 2.9 ATR down), which protects the
  entry. No candidate captured: nothing changed at Pfizer today and there is no reason to re-pitch a working position.

## [06:27 ET] POSITION UPDATE — RARE, SVRA — hold, both already carry stops, both uncorrelated with today's regime
- `RARE` entry 25.20 on 2026-08-31, last 25.81 (+2.4%), stop 22.90, target 31.50. One day old. Hold, no change.
- `SVRA` entry 5.35 on 2026-08-23, last 5.35 (flat), stop 4.60, target 8.00. Micro-cap, sized as a lottery ticket.
  Hold, no change.
- These two are the only positions in the book whose outcome does not depend on the war, rates or the consumer. That is
  worth noting rather than fixing.

## [06:28 ET] ARITHMETIC CHECK — all 12 candidates recomputed from entry/target/downside
Verified in code, not by eye: every candidate's direction ordering is correct (target/downside on the right sides of
entry) and every reward-to-risk clears its horizon floor. Tightest three are TLT 2.06, LCII 2.05 and EQT 2.12 against a
2.0 swing floor — all three levels were derived before the ratio was computed (TLT 78.30 from ~17 duration against a
10y at 5.05%; LCII 89.00 is the actual 150-day low; EQT 63.00 is chart resistance between the close and the 180-day
high of 68.24), not fitted to clear the floor. XLE shows 4.37 only because its entry is a pullback level close to the
raised stop — if XLE never trades back to 63.00 the new-money leg simply does not happen, and the update is then purely
the stop consolidation to 61.40.

## [06:29 ET] SECTOR — the merchant power / AI-datacenter-power complex is breaking
Closes 2026-09-01, with distance from the 150-day high, and position vs the 20-day and 50-day:
- `AGX` 404.75, **-49.8%** off high (805.75), 20d 521.48, 50d 593.71 — reports tonight 2026-09-02 AMC
- `NRG` 109.51, **-42.4%** off high, 20d 116.85, 50d 129.18 — closed at 109.51 vs a 150-day low of 108.34
- `TLN` 293.73, **-34.7%** off high, 20d 327.06, 50d 353.78
- `VST` 138.08, **-22.6%** off high, 20d 141.16, 50d 150.76
- `CEG` 280.31, **-16.0%** off high, 20d 274.77, 50d 265.08 — **above both**, and closed **+2.0%** on a -0.69% SPY day
Every one of these is below both moving averages except CEG. This is a theme being de-rated, not a dip.
- **CAPTURED: `CEG`** — the only name in the complex with a fuel-position reason to diverge (largest US nuclear fleet;
  power priced at the gas-fired margin), and the only one holding its averages. Entry raised to 265-278 from the
  unfilled 266.00 order of 2026-08-21.
- **REJECTED: `AGX`** — halved from its high with a 7.02% ATR and an earnings print tonight. Interesting as a gas-fired
  EPC contractor in an energy-security regime, but buying a knife into a binary event with no research on the cause of
  a 50% de-rating is gambling. Watchlist, revisit after the print.
- **REJECTED: `TLN`, `NRG`** — same complex, no fuel-position differentiator, both below both averages, NRG sitting on
  its 150-day low. No reason to catch these.
- **`VST` — CANCEL the resting orders.** The 2026-08-24 @134.00 and 2026-08-25 @128.00 buy levels are still unfilled
  and should be withdrawn, not left working. VST is 22.6% below its high and below both averages inside a complex that
  is unwinding; a limit order that fills only because the name keeps falling is not an entry plan, it is a passive
  short-volatility bet on a broken theme.

## [06:30 ET] REJECTED — DG, DLTR — right thesis, the entry left without me
The trade-down mechanism is real and it is the natural hedge to everything else in this report: gasoline at $4.1203
against $3.1869 a year ago squeezes exactly the low-income consumer who shifts spend into dollar stores. The tape
priced it yesterday — on a day SPY fell 0.69%, **DG closed +3.4% at 131.09 and DLTR +4.0% at 131.71**.
- But DG has already run 99.57 -> 131.09 (**+32% off its 150-day low**) and sits 6% above its own 20-day (123.65).
  DLTR is only 5.2% below its 150-day high. Neither is a de-rated business any more; the thesis is in the price.
- **Action on the book: the resting `DG` buy orders at 119.00 (2026-08-21) and 121.00 (2026-08-31) are now 8-10% below
  the market and should be cancelled**, not left working. They only fill if the trade-down thesis stops working.
- Not captured. Buying the day after a +3.4% move, with no dated catalyst inside the horizon and no DG-specific work
  done today, would be chasing a confirmed narrative.

## [06:30 ET] `EEM` — resting order stale, no view
Published at 65.60 three times (08-21, 08-22, 08-23), never filled; EEM is 66.77, above both its 20-day (66.42) and
50-day (65.78) and 6.7% off its high. I did no emerging-market work today, so I have no basis to re-pitch or to raise
the level. Leave the order or cancel it, but it should not appear as a fresh recommendation.

## [06:32 ET] FALSIFICATION — I stress-tested the one event that breaks half this report, and it got LESS likely
Eight of thirteen candidates lose money on a US-Iran ceasefire. So I went looking for evidence one is close. It is not:
- **Trump: "There are no talks or conversations going on, or scheduled, with the Islamic Republic of Iran"** and
  **"The Naval Blockade remains in full force and effect."** He has separately announced a "crushing economic
  operation" on Iran, with talks described as in limbo.
  — source: https://www.cbsnews.com/live-updates/us-iran-war-deal-strait-of-hormuz/
- Timeline for context: a two-week ceasefire in early April, direct Vance-Ghalibaf talks in Islamabad on April 11-12
  (highest-level US-Iran engagement since 1979) that agreed most points but not the nuclear one, a memorandum of
  understanding in mid-June, Trump calling Iranian strikes "a foolish violation" by June 27, and the agreement declared
  **"over" on July 7**. The MoU already failed once.
  — sources: https://www.congress.gov/crs-product/IN12678 and https://www.aljazeera.com/news/2026/8/16/us-iran-mou-is-set-to-expire-what-to-know
- WHY THIS MATTERS MORE THAN IT LOOKS: a **naval blockade** is a categorically more durable mechanism than sporadic
  strikes. Sporadic strikes end with a headline; a blockade ends with a negotiated settlement, and there are no talks
  scheduled. It also closes the strait to Qatari LNG regardless of the state of the damaged trains, which means
  Drivers A and B are both more robust than the "one ceasefire headline away" framing I wrote into the candidates.
- HONEST LIMIT: I am deliberately NOT raising any conviction score on the back of this. Ceasefire risk falling from
  "possible any day" to "requires a negotiation that is not scheduled" is a real update, but Iran publicly urging a
  return to the June deal (CNBC, 2026-09-01) is exactly how these things restart, and this war has already produced one
  ceasefire and one signed MoU in five months. The key_risk text on DHT, DINO and XLE stands as written. This block is
  here so the red-team phase weighs the evidence rather than the cliche.

## [06:32 ET] RESEARCH COMPLETE
- candidates: **13**, resolving to 4 drivers (see the correlation audit at 06:19)
  - Driver A, Hormuz transit closure (at cap): `DHT` hold+raise stop, `DINO` hold+raise stop, `XLE` hold+consolidate stops
  - Driver B, destroyed Qatari liquefaction: `EQT`, `CRK`, `CEG`
  - Driver C, rate/inflation consequence (at cap): `TLT` exit, `IYR` short, `KXFEDDECISION-26OCT-H25` yes @28c
  - Driver D, idiosyncratic: `LULU` (wait, Sep 3 print), `AVGO` (wait, Sep 2 print), `CCJ` (long-term accumulation),
    `LCII` exit
- By horizon: 10 swing, 2 long_term (`CCJ`, `LULU`), **0 intraday** — nothing intraday cleared the bar. With equity
  prices 14 hours stale at the previous close and the day's only 08:30 ET print absent, there was no honest basis for
  a level-precise same-session trade.
- Four of the thirteen are exits or risk-reduction (`TLT`, `LCII` sell; `DHT`, `DINO`, `XLE` stop raises). That skew is
  the point: 23 open positions, several with no stop at all, into a regime that inverted in two weeks.
- Position decisions recorded in notes but NOT capturable in the schema — synthesis must carry these into the report
  narrative: **close all four BTC / `/MBTU6` shorts** (stops breached by 15-19%), **TJX and BCC stopped out, do not
  re-enter**, **attach stops to `NKE` (36.20) and `PFE` (26.80)**, **cancel the stale `VST` 134/128 and `DG` 119/121
  resting orders**.
- coverage gaps:
  - **No VIX, DXY, index-level or futures quotes today** — yahoo returned HTTP 429 for ^GSPC, ^NDX, ^DJI, ^RUT, VIX,
    the dollar index, ES, NQ, gold and WTI futures. All index reads today are from SPY/QQQ/IWM ETF closes instead, and
    there is **no volatility or dollar read at all** in this report.
  - **No live crude print.** Crude is described from news (Brent back over $90, "above $95", +~30% vs pre-war), not
    from a fetched quote. Every crude number in this report is a citation, not a measurement.
  - All equity prices are the **2026-09-01 close**, age ~842 minutes, market closed. That is the freshest honest price
    at 6am ET, not stale data — but no candidate here has been checked against a live pre-market bid.
  - Did not reach: small and micro caps below $2bn (only `SVRA`, already open, occupies that lane — `CRK` at ~$4.7bn is
    the smallest new name), international/EM, biotech beyond the two open positions, and the Sep 4 08:30 ET jobs report,
    which I did not research and which lands before any of these swing horizons end.
  - Did not verify Robinhood availability of the Kalshi **gasoline** markets and therefore did not trade them despite
    finding a plausible edge (see 06:16); the October FOMC contract WAS verified on Robinhood's own economics page.
- sources that failed: yahoo finance chart API (HTTP 429, all index/futures/FX symbols), finnhub index quotes
  ("Market data subscription required for CFD indices"), alphavantage (no API key), `market_data.py events` keyword
  search (returned unrelated tennis markets for "Fed" — used the Kalshi REST API by series ticker instead),
  benzinga.com (HTTP 403), Kalshi `KXAAAGASD` (no open markets at this hour), `CTRA` quote (no data).
- one thing I got wrong and caught: a web search surfaced an "August CPI Preview" of 3.2% -> 3.6% that turned out to be
  **August 2023 figures**. Verified against FRED (July 2026 actual = 3.30%, not 3.2%) and discarded. See 06:16.

## [06:33 ET] FALSIFICATION — MAJOR, and it cuts AGAINST Driver C: the labour market is already contracting
Found after writing RESEARCH COMPLETE, and it is important enough to reopen the file.
- **The US economy SHED 23,000 jobs in July 2026**, following a **downwardly revised +20,000 in June**, against a
  forecast of +80,000. — source: https://tradingeconomics.com/united-states/non-farm-payrolls
- FRED UNRATE was 4.1% in July, down from 4.2% — so the unemployment rate is falling while payrolls shrink, which
  usually means participation is falling, not that the labour market is healthy.
- **The August Employment Situation is released Friday 2026-09-04 at 08:30 ET** — two sessions from now, and twelve
  days before the FOMC. — source: https://www.bls.gov/news.release/empsit.nr0.htm
WHAT THIS DOES TO THIS REPORT: Driver C — `TLT` exit, `IYR` short, October Fed hike at 28c — is a bet that the bond
market's inflation panic wins. But payrolls are already negative. The market is pricing a 62% hike into a labour market
that shed jobs last month, which is not a contradiction the Kalshi price acknowledges. A second negative print on
Friday prices the hike out fast: yields fall, TLT rallies (making the exit wrong), IYR bounces, and the October
contract halves.
ACTIONS TAKEN — re-captured all three Driver C candidates rather than leaving the omission standing:
- `TLT` conviction cut **4 -> 3**, payroll risk written into key_risk and counter_argument.
- `IYR` given a hard stand-down condition on the Friday print, conviction cut **3 -> 2**, size cut 2% -> 1.5%.
- `KXFEDDECISION-26OCT-H25` conviction cut **3 -> 2**, probability estimate cut 40% -> 35%, entry cap lowered to 29c,
  payroll gate written into catalyst.action.
This is the falsification pass doing its job. I did not find this by looking for reasons to like the trades.

## [06:36 ET] WATCHLIST — the trade-down lane reports today and tomorrow; no position taken
The consumer-squeeze mechanism is confirmed by price (DG +3.4%, DLTR +4.0% on a -0.69% SPY day) but every clean
expression is either extended or reports within hours, so nothing here was captured:
- `OLLI` Ollie's Bargain Outlet — reports **today 2026-09-02 before the open**, est EPS 1.16 on revenue ~$770mn. The
  purest extreme-value closeout retailer and the best read-through on whether $4.12 gasoline is actually pushing
  traffic down-market. Entering three hours before a print I have done no company work on is a coin flip.
- `FIVE` Five Below — today after the close, est EPS 1.41 on ~$1.24bn.
- `WOOF` Petco — today after the close, est EPS 0.07 on ~$1.52bn. Discretionary pet spend is the wrong side of a
  consumer squeeze, not the right one.
- These prints, plus `LULU` tomorrow, will settle whether the trade-down thesis is real or just two days of rotation.
  Revisit tomorrow with actual comparable-sales numbers rather than a narrative.

## [06:36 ET] SMALL-CAP LANE — honestly, I did not fill it, and here is why rather than an excuse
The report wants sub-$2bn names hunted deliberately. Today it has none new. `CRK` at roughly $4.7bn is the smallest new
name; `SVRA` is the only true small cap in the book and it is an existing position. The reason is structural rather
than laziness: every small cap I could research quickly today sat inside a driver already at its correlation cap —
`FRO` and the tanker complex under Driver A (full at 3), `FLNG` and the LNG shippers under Driver B (full at 3, and
the ton-mile logic there is genuinely ambiguous since US-to-Europe is a shorter haul than Qatar-to-Asia). Opening a
fourth driver properly needs more time than remains, and a micro cap researched in ten minutes is not a lottery
ticket, it is a guess. Recorded as a gap for tomorrow.

## [06:37 ET] RESEARCH COMPLETE (amended — supersedes the 06:32 block)
- **16 candidate lines resolving to 13 distinct symbols.** `TLT`, `IYR` and `KXFEDDECISION-26OCT-H25` were each
  captured twice: the second capture of each is the live one and exists because the payroll finding at 06:33 forced a
  downgrade. Synthesis should take the last line per symbol.
- Verified in code after the final capture: all 13 have correct direction ordering and clear their horizon
  reward-to-risk floor, with every candidate carrying 3 or more source URLs.
- Final set by driver:
  - **A — Hormuz transit closure (at cap):** `DHT` c3 hold+stop to 18.35, `DINO` c3 hold+stop to 94, `XLE` c3
    hold+stops consolidated to 61.40
  - **B — destroyed Qatari liquefaction (at cap):** `EQT` c4, `CRK` c3, `CEG` c3
  - **C — rate/inflation consequence (at cap, all downgraded at 06:33):** `TLT` c3 exit, `IYR` c2 short gated on
    Friday's jobs print, `KXFEDDECISION-26OCT-H25` c2 yes at 25-29c
  - **D — idiosyncratic:** `CCJ` c4 long-term accumulation, `LULU` c3 wait, `AVGO` c3 wait, `LCII` c3 exit
- Horizons: 11 swing, 2 long_term, **0 intraday** — stated plainly rather than padded. With every equity price 14 hours
  old and no 08:30 ET print today, there was no honest basis for a level-precise same-session trade.
- Conviction: one 4-rated pair (`EQT`, `CCJ`), eight 3s, two 2s. No 5s — nothing today had multiple independent
  confirmations *and* a clean counter-argument, because the biggest driver is a war.
- **Four of thirteen are exits or risk reduction**, and two more say wait. That is the honest shape of a day with 23
  open positions, several carrying no stop, and a regime that inverted inside two weeks.
- Not capturable in the schema, must be carried by synthesis into the narrative: close all four BTC / `/MBTU6` shorts
  (stops breached by 15-19%); `TJX` and `BCC` stopped out, do not re-enter; attach stops to `NKE` (36.20) and `PFE`
  (26.80); cancel the stale `VST` 134/128 and `DG` 119/121 resting orders.
- Coverage gaps and failed sources: unchanged from the 06:32 block — no VIX, DXY, index or futures quotes (yahoo 429),
  no live crude print, all prices at the 2026-09-01 close, no small caps below $2bn, no jobs-report event contract
  (could not enumerate the Kalshi series and Robinhood's economics page lists only Fed decisions), gasoline event
  markets found but Robinhood availability unverified so not traded.
