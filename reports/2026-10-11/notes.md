# Research log — 2026-10-11

## [06:04 ET] MACRO — rates, regime, data sources
Run is **Sunday 2026-10-11**. US equities and futures closed; weekend rules apply
(crypto + event contracts carry the actionable load, equities are week-ahead prep
with entry at the Monday open).

- US 10y **5.22%**, prev 5.28% (as of 2026-10-08) — source: FRED DGS10
- US 2y **4.75%**, prev 4.77% (2026-10-08) — source: FRED DGS2
- Fed funds effective **3.88%** (2026-10-08) — source: FRED DFF
- 10y-2y curve **+0.44**, prev +0.47 (2026-10-09) — source: FRED T10Y2Y
- Unemployment **4.2%**, prev 4.1% (Sep) — source: FRED UNRATE
- CPIAUCSL **334.131** (Aug) vs **332.813** prior month = **+0.40% MoM**, ~4.9%
  annualized — source: FRED CPIAUCSL
- Regime read: long end 134bp **above** the funds rate with inflation re-accelerating
  MoM and unemployment drifting up. That is a term-premium/stagflation-lean tape,
  not a soft-landing tape. It argues against duration longs and against rate-cut-
  dependent theses, and for real assets and energy.

### Closing prices (Friday 2026-10-09 close, market closed — not stale, just shut)
- SPY 778.57, QQQ 751.27, IWM 278.94, GLD 384.58 — source: finnhub via market_data
- TLT proxy bonds_20y 77.98

### Crypto (live, 24/7) — source: CoinGecko via market_data
- BTC **$82,961** (+0.19% 24h), ETH **$2,500.28** (+0.21%), SOL **$109.40** (-0.44%)
- XRP $1.39 (-0.99%), DOGE $0.0853 (-0.91%), ADA $0.2472 (-3.22%),
  AVAX $10.32 (-2.01%), LINK $12.87 (-0.72%), LTC $63.63 (+0.20%)
- Majors are flat-to-soft on the weekend with alts leading down — risk appetite
  inside crypto is weak, no weekend squeeze underway.

## [06:04 ET] DATA QUALITY — Yahoo is 429 rate-limited this run
- All of ^GSPC/^NDX/^DJI/^RUT, VIX, ES/NQ futures, DXY, us10y quote, gold and WTI
  **failed** via market_data macro: finnhub refuses indices ("subscription required
  for CFD indices"), Yahoo returned HTTP 429 on both hosts, stooq 404s on `^` symbols.
- Equity/ETF single-name quotes **do** work via finnhub. FRED works. CoinGecko works.
- Consequence for this run: **no VIX, no DXY, no index futures level, no live WTI/gold
  futures price.** Index-level and vol-regime claims must be sourced some other way
  or not made. Must land in data_quality_notes.

## [06:15 ET] MACRO — THE REGIME: the Fed is HIKING, not cutting
This is the single most important frame for today and it inverts the usual read.

- Sept 2026 FOMC **raised** the target range to **3.75-4.00%** — first hike since
  2023, unanimous. Effective funds 3.88% (FRED DFF) cross-checks the range.
  — source: https://www.cnbc.com/2026/10/07/fed-officials-see-another-hike-coming-but-no-sign-as-to-when-minutes-show.html
- Minutes of the Sept 15-16 meeting (released ~Oct 7) say most officials expect
  **another increase before year-end**, with no signal on which meeting.
  **16 of 18** officials see at least one more 25bp hike in 2026.
  — source: https://www.federalreserve.gov/monetarypolicy/fomcminutes20260916.htm
- Fed projections: 2026 PCE **3.7% headline / 3.4% core**; no return to 2% until
  **2029**. Inflation has run above target for 5+ years.
- Dissent is about timing, not direction: Vice Chair **Jefferson** and NY Fed's
  **Williams** have both said they may want more data before backing another hike.
  — source: https://thehill.com/business/6135206-fed-officials-project-future-increases/amp/
- As of Sept 29 fixed-income leaned to **Oct 28** as the likely hike meeting
  — source: https://www.forbes.com/sites/simonmoore/2026/09/29/what-to-expect-from-interest-rates-for-the-rest-of-2026/

### What the event market prices now (Kalshi, live, Sunday 06:10 ET)
Fetched per-market from api.elections.kalshi.com (the `events` CLI cannot find
these — see DATA QUALITY below). Prices in cents = implied probability.

| Meeting | Hike 25bp | Hold | Cut 25bp | Hike >25bp | OI |
| --- | --- | --- | --- | --- | --- |
| **Oct 28** | **16** (yb15/ya16) | 85 | 1 | 1 | 1.48M hold / 1.09M H25 |
| **Dec 9** | **74** (yb72/ya74) | 25 | 2 | 1 | 176k hold / 126k H25 |

- Expectations have **migrated from October to December** since Sept 29: the Oct
  hike is only 16c now, the Dec hike 74c. Consistent with the Jefferson/Williams
  "wait for data" line.
- **The implied conditional is the interesting number.** Backing out:
  P(Oct hike)=0.16. If a back-to-back Dec hike follows an Oct hike ~30% of the
  time, that branch contributes ~0.05 to Dec-H25. So the remaining
  0.74-0.05=0.69 over the 0.84 no-Oct-hike branch implies
  **P(Dec hike | Oct hold) ≈ 82%** — near-certainty about a specific action two
  months and *four* major data releases out, from a committee with two named
  members publicly asking to wait.

### Inflation and labour are priced TAME, which is in tension with the hike
- `KXCPI-26OCT-T0.4` Above 0.4% MoM: **16c** (yb16/ya17)
- `KXCPI-26OCT-T0.5` Above 0.5% MoM: **8c**
- `KXCPIYOY-26NOV-T4.0` Above 4.0% YoY: **25c** (yb23/ya26)
- `KXCPIYOY-26DEC-T4.5` Above 4.5% YoY: **6c**
- `KXRECSSNBER-26` recession starts 2026: **3c**; `KXRECSSNBER-27`: **20c**
- So the market expects a hike **without** expecting inflation to re-accelerate.
  The hike case rests on the *level* (3.4-3.7% core vs a 2% target), not momentum.
- Against that: **unemployment is rising, 4.1% -> 4.2%** (FRED UNRATE, Sep).
  Hiking into a rising unemployment rate is the hardest version of this vote.
- Illiquid, excluded from use: `KXCPIYOY-26DEC-T4.0` (bid 14 / ask 43),
  `KXU3-26NOV-T4.3` (bid 9 / ask 49). Spreads that wide are not prices.

### Regime consequences I will trade off
1. Duration is the wrong side — 10y 5.22%, a hiking Fed, no 2% inflation until 2029.
2. Rate-cut-dependent and long-duration equity theses get a higher bar today.
3. Real assets / energy favoured; crypto is a liquidity asset into tightening.

## [06:13 ET] CALENDAR — the week ahead (equities closed today; entries are for the Monday open)
- **Mon Oct 12** — US equity markets open; **bond market closed** (Columbus Day).
  Nothing material on the earnings tape (16 names, all micro/no-estimate).
- **Tue Oct 13 bmo** — **JPM, GS, C, WFC, JNJ, UNH**, DPZ. Q3 season opens.
- **Wed Oct 14 08:30 ET** — **September CPI**. Also BAC, MS, BLK, STT, FAST bmo.
- **Thu Oct 15 08:30 ET** — September PPI + advance retail sales. PNC, USB, SCHW,
  MRSH, PLD, CMC bmo; IBKR, JBHT, AA amc. WHR, HRI, IRDM.
- **Fri Oct 16 08:30 ET** — import/export prices. TFC, RF, CFG, MTB, TRV bmo.
- **Wed Oct 28** — FOMC decision. **Wed Dec 9** — FOMC decision.
- Earnings dates from the fetched finnhub calendar. CPI/PPI dates from calendar
  aggregators (eco3min, fedratecalc) — **I could not reach bls.gov directly to
  confirm**, so treat Oct 14 08:30 as high-confidence but not primary-sourced.
  — source: https://eco3min.fr/en/next-us-cpi-release/

## [06:16 ET] CPI ARITHMETIC — base effects computed from the FRED index, not guessed
CPIAUCSL monthly (SA), fetched from FRED. MoM, actual:

| Month | Index | MoM |
| --- | --- | --- |
| 2026-03 | 330.293 | +0.865% |
| 2026-04 | 332.407 | +0.640% |
| 2026-05 | 333.979 | +0.473% |
| 2026-06 | 332.568 | **-0.422%** |
| 2026-07 | 332.813 | +0.074% |
| 2026-08 | 334.131 | +0.396% |

- Trailing 6-month mean **+0.338%/mo**; trailing **4-month mean only +0.130%/mo**.
  The 6-month figure is inflated by a Mar-May spike that partly reversed in June.
  **Headline level is high (~3.5%) while recent momentum is ambiguous to soft.**
- Note: **2025-10 is absent from CPIAUCSL** (the 2025 shutdown data gap). It does
  not affect a November YoY, which needs only the Nov-2025 level (325.063).

### What the market prices for Sep CPI (released Oct 14), and whether it is coherent
- `KXCPI-26SEP-T0.4` >0.4% MoM: **92c**; `-T0.5` >0.5%: **64c** (OI 420k, the focal
  market); `-T0.6` >0.6%: **15c**
- `KXCPIYOY-26SEP-T3.5` >3.5%: **87c**; `-T3.6`: **48c**; `-T3.7`: **10c**
- Sep YoY needs base Sep-2025 = 324.245. For YoY >3.6% the index must reach
  324.245 x 1.036 = **335.919**, i.e. MoM **>+0.535%** from 334.131.
- Interpolating the MoM ladder (64c at >0.5%, 15c at >0.6%) gives ~47c at +0.535%.
  The YoY >3.6% market sits at **48c**. **These agree to one cent.**
- **REJECTED — the September CPI complex is precisely arbitraged.** There is no
  probability disagreement to take, and inventing one here would be a hunch
  dressed as arithmetic. Expected print: ~+0.5% MoM, ~3.6% YoY. Hot, and already in.

## [06:17 ET] REJECTED — KXCPIYOY-26NOV-T4.0 YES @ 26 — the answer is assumption-dependent, not edged
- Nov YoY >4.0% needs index >= 325.063 x 1.04 = **338.066**, i.e. **+1.178% cumulative
  over Sep+Oct+Nov** from 334.131.
- Granting the market's own September expectation (+0.53%), Oct+Nov then need only
  +0.645% total = **+0.322%/mo** — just under the 6-month mean of +0.338%.
- At the 6-month run rate the print lands at **~4.04% YoY** — essentially *on* the
  strike, which would argue 26c is cheap.
- **But at the 4-month run rate (+0.130%) it lands at ~3.60%** — nowhere near it.
  The whole answer is the run-rate assumption, and the two defensible assumptions
  straddle the strike. 26c is a fair price for that tail. No trade.

## [06:17 ET] REJECTED — the Fed-decision complex (KXFEDDECISION 26OCT / 26DEC) — efficient and against me
- Oct-28 hike **16c**, Dec-9 hike **74c** (table above). My first read was that the
  implied ~82% conditional on a December hike was overconfident, and that rising
  unemployment (4.1->4.2%) made it a hard vote.
- **Reading the actual minutes killed that.** They say participants "generally
  viewed the labor market as close to maximum employment", the statement says "the
  unemployment rate has changed little", a majority saw the labour market
  *strengthening* recently, inflation risks are "skewed to the upside", and several
  participants see policy as **not restrictive or only mildly restrictive**. The
  4.1->4.2 tick is noise to this committee, and they are targeting the *level* of
  inflation, so soft recent CPI momentum does not stop a hike either.
  — source: https://www.federalreserve.gov/monetarypolicy/fomcminutes20260916.htm
- The Oct contract is also deeply liquid (OI 1.09M, volume 2.68M) and the minutes
  have been public since Oct 7 — the 16c already contains them. No edge.
- Worth recording: prior run published `KXFEDDECISION-26OCT-H25` YES @ 28 on
  2026-09-02 and it still shows awaiting-entry. It now trades at **16c**, i.e. the
  October hike de-rated hard as expectations migrated to December. **I am not
  re-pitching it at the cheaper price** — the reason it is cheaper is that the
  committee signalled it would wait, which is the thesis failing, not a discount.

## [06:18 ET] POSITION REVIEW — all 17 open positions, levels re-fetched
Closes are Friday 2026-10-09; market is shut, so these are the freshest honest prices.

| Sym | Entry | Last | % | sma20 | sma50 | off 120d high | Read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLE | 63.90 | 65.08 | +1.9 | 63.30 | 62.67 | -1.7% | leadership, trend intact |
| CCJ | 94.00 | 88.06 | -7.3 | 89.54 | 94.77 | **-32.9%** | broken, target unreachable |
| NKE buy | 40.75 | 34.71 | -13.2 | 35.50 | 38.15 | -27.2% | downtrend, no stop |
| NKE sell | 38.40 | 34.71 | +9.6 | — | — | — | working |
| BCC | 76.50 | 73.57 | -9.2 | 75.54 | 78.68 | -16.8% | downtrend, no stop |
| LCII | 94.00 | 78.30 | -16.7 | 84.39 | 95.65 | **-36.9%** | sitting ON its 120d low 78.075 |
| PFE | 27.60 | 28.28 | +2.5 | 27.99 | 27.62 | -3.2% | quietly working, above both SMAs |
| EEM | 65.60 | 66.80 | +1.8 | 67.27 | 66.87 | -6.7% | flat, no edge either way |
| DINO | 107.50 | 121.30 | +12.8 | 111.65 | 102.10 | -2.4% | best position, near target 128 |
| LULU buy | 115.00 | 94.50 | -17.8 | 97.61 | 109.43 | **-44.5%** | downtrend, no stop |
| LULU sell | 100.61 | 94.50 | +6.1 | — | — | — | working |
| SNX | 260.00 | 273.37 | +5.1 | 268.89 | 261.34 | -8.5% | above both SMAs, hold |
| KHC | 23.00 | 22.27 | -3.2 | 23.38 | 24.54 | -20.7% | low 21.75 vs stop 21.20 — stop is live |
| CEG | 272.00 | 298.07 | +9.6 | 268.10 | 273.98 | -9.4% | working, power theme |
| DAL | 83.00 | 82.17 | -1.0 | 82.30 | 83.65 | -14.1% | flat, earnings already passed |
| XLF | 54.23 | 54.73 | +0.9 | 54.77 | 56.53 | -6.6% | captured as update, hold |
| SMMT | 17.10 | 17.59 | +2.9 | 17.03 | 15.46 | -39.8% | above both SMAs, uptrend, hold |

### [06:18 ET] POSITION UPDATE — the book holds two self-cancelling pairs
- **NKE is both BUY (40.75, no stop) and SELL (38.40, target 32.10, stop 41.00).**
- **LULU is both BUY (115.00, no stop) and SELL (100.61, target 77.00, stop 112.00).**
- In each case the long is a long-term thesis with no stop and the short is a swing,
  so they are not literally one position hedged flat — but the net exposure is near
  zero and **the two legs cannot both be right**. Both shorts are in profit and both
  longs are deep underwater, which is the market's verdict so far.
- This is a book-construction problem rather than a new trade, so I am recording it
  here for synthesis to surface rather than inventing a fresh recommendation. The
  honest resolution is to close the losing long legs: NKE -27.2% and LULU -44.5%
  off their highs, both below both moving averages, both with **no stop** to stop them.

### [06:18 ET] POSITION UPDATE — CCJ — close early, the target is no longer reachable
- decision: **close / demote**. Entry 94.00, last 88.06, target 135.00, stop 82.50.
- why: CCJ is **-32.9% off its 120-day high of 131.21** and trades below both the
  20-day (89.54) and the 50-day (94.77). The published target of 135 is **above the
  120-day high** — it requires +53% from here and a new all-time area, which is not
  a target, it is a hope. Held 39 days.
- It is also the anchoring case: **recommended 3x in the last 10 days**. Per the
  prior-context rule that is a warning sign, not conviction, and nothing concrete
  changed to justify the repeats.
- action: captured below as a demotion rather than silently left to grind to the stop.

### [06:18 ET] POSITION UPDATE — hold, no change
- **DINO** +12.8%, -2.4% off high, above both SMAs, target 128 only +5.5% away. Let
  it run to target; I am deliberately **not** walking the 97.75 stop up, because a
  stop raised to flatter the ratio is the exact failure mode this repo logs.
- **SMMT** +2.9%, above sma20 17.03 and sma50 15.46, stop 14.4 = 2.3 ATR. Hold.
- **CEG** +9.6%, **SNX** +5.1%, **PFE** +2.5%, **XLE** +1.9% — all above or at their
  20-day, theses intact, no action.
- **EEM** +1.8% and **DAL** -1.0% are flat at their 20-day with no live catalyst; no
  action, but neither is earning its slot.
- **KHC** -3.2% is the one to watch: the 120-day low is 21.75 against a 21.20 stop,
  so an ordinary 2.4% ATR day puts it at the stop. No change — the stop is correct
  and letting it work is the point.

## [06:22 ET] SECTOR — refining is the tape's leadership, and I am already in it
The strongest trend on the board, confirmed fundamentally:

- 3-2-1 crack spread **~$69.72/bbl** as of 2026-10-09 — source: https://rbnenergy.com/market-data/3-2-1-crack-spread
- NY Harbor 3-2-1 averaged **$65.61/bbl in August 2026, the highest monthly value
  since 2006**; diesel's premium over crude has been above **$100/bbl**
  — source: https://rbnenergy.com/daily-posts/blog/what-2026s-record-crack-spreads-tell-us-about-refining-economics
- Cause is lost global capacity — Ukrainian drone strikes on Russian refineries plus
  US plant closures — and US refiners are already at practical limits, so record
  margins cannot pull in much extra supply
  — source: https://www.forbes.com/sites/garthfriesen/2026/07/23/refining-stocks-soar-as-crack-spread-hits-record-high-in-2026/

Prices (2026-10-09 close): VLO 433.75 (-3.6% off high, 120d low 224.36),
MPC 455.03 (-3.2%, low 213.06), PSX 278.18 (-2.9%, low 155.58). All three roughly
**doubled off their 120-day lows** and sit above rising 20- and 50-day averages.

## [06:23 ET] REJECTED — VLO / MPC / PSX long — right theme, wrong entry, and I already own it
Four reasons, and the last is the decisive one:
1. **The EIA's own October outlook expects crack spreads to decrease**, while
   remaining high versus history. Initiating on a margin peak the primary forecaster
   says is rolling over is buying the top of the cycle.
   — source: https://www.eia.gov/outlooks/steo/report/petro_prod.php
2. **No insider is buying and several are selling.** 6-month open-market buys:
   VLO **0** buys / 2 sells ($3.66M); MPC **0** buys / 11 sells ($11.8M); PSX 1
   token buy of $30k against 17 sells. Absence of buying is not a negative on its
   own, but net selling into a record-margin print is not confirmation either.
3. Entry would be within 3% of the 120-day high after a ~100% move, with no
   pullback level to lean on nearer than the 20-day (VLO 402, MPC 414).
4. **`DINO` already gives me this exact exposure** at +12.8% from 107.50, and the
   correlation cap is 3 ideas per driver. Adding a second refiner would be paying a
   worse price for a bet I already hold at a good one.
- The reverse trade is also rejected: EIA expects compression but nothing dates it,
  and shorting a record-margin uptrend with no catalyst is worse than not trading.

## [06:25 ET] REJECTED — EQT / natural gas long — the secular imbalance runs the wrong way
I went looking for a de-rated name inside a favoured secular theme (LNG export ramp
plus datacenter load) and the primary forecasts say the imbalance is **supply**, not
demand:

- EIA July 2026 STEO: Henry Hub **~$3.49/MMBtu in 2027** against ~$3.67 in 2026
  — source: https://www.eia.gov/todayinenergy/detail.php?id=67004
- 2027 forecasts have been **cut** through the year: Enverus/EIR to **$3.25**,
  expecting supply additions to exceed incremental LNG demand by ~1.3 Bcf/d by
  end-2027; East Daley to $3.57 on Permian associated gas
  — source: https://www.enverus.com/newsroom/u-s-gas-supply-growth-could-outpace-lng-demand-through-2027/
  — source: https://naturalgasintel.com/news/permian-supply-surge-drives-2027-natural-gas-price-cut-despite-lng-growth/
- LNG feedgas demand does grow ~11% (1.7 Bcf/d) in 2027 — real, but smaller than the
  supply response. Spot was ~$2.88 in late Sept with storage ~114 Bcf **above** the
  five-year average.
- **Relative strength says the same thing.** EQT 1m **-3.9%** vs XLE +0.2% and SPY
  +2.7%; 6m EQT **-10.0%** vs XLE +14.3% and SPY +14.6%. That is a ~24-point
  six-month underperformance of its own sector — the "catching something falling
  relative to everything around it" case strategy.md warns about, not a de-rating.
- Insiders: **0** open-market buys, 5 sells ($15.3M). Analysts are the lone positive
  (80% bullish, +4.1pp) and that is not enough against the above.
- Datacenter-gas sizing for 2027: the only source I found was dated Oct 2025, so I am
  **not** claiming it. Treated as unknown.

## [06:26 ET] REJECTED — NRG long — deteriorating, not de-rated
- 6m **-34.2%** vs XLU -11.8% and SPY +14.6%; 3m -22.6% vs XLU -9.4%. That is 22-27
  points of underperformance against its *own* sector, so this is not a sector trade.
- The reason is in the prints: **two consecutive EPS misses**, Q2-26 actual 1.49 vs
  1.7142 est (**-13.1%**) and Q1-26 actual 1.48 vs 1.7967 (**-17.6%**).
- Insiders 0 buys / 3 sells. Analysts are 81% bullish and **unchanged for four
  months** — stale ratings on a falling stock, which is the opposite of a positive.

## [06:26 ET] REJECTED — TLN long — chasing someone else's catalyst
- TLN closed 378.57, **+19.5% above its 20-day (316.86)** after jumping ~12% on
  2026-10-06. The catalyst was a **Google-Constellation 3.6 GW nuclear deal** — i.e.
  CEG's news, not Talen's — partly offset the same day by **FERC suspending PJM's
  one-time Reliability Backstop Procurement**, a sector-wide negative.
  — source: https://www.timothysykes.com/news/talen-energy-corporation-tln-news-2026_10_06/
- Talen is also levered into a **$3.5B purchase of 2.6 GW of PJM gas plants** and has
  just handed over its CEO, with weaker PPL-zone pricing flagged as the near risk.
  — source: https://www.utilitydive.com/news/talen-in-deal-to-buy-26-gw-of-gas-plants-in-pjm-for-35b/809826/
- **POSITION UPDATE — CEG: the Google deal is confirmation of the position I already
  hold** (+9.6% from 272.00). No change to levels; the right exposure to this theme
  is the one already on, not the name that moved on its press release.

## [06:28 ET] MACRO — the cyclical complex is pricing a slowdown the macro contracts are not
Fetched 120-day closes, % off 120-day high, all below both their 20- and 50-day:
- **AA 42.20, -50.0%** off high (120d low 41.01) | **WHR 28.83, -50.9%** (low 28.39)
- **HRI 123.46, -29.9%** | **JBHT 229.26, -23.5%** | **CMC 63.89, -20.1%**
- **STLD 238.38, -17.4%** | **SCHW 96.70, -15.6%** | **PLD 129.49, -15.6%** (low 126.62)
Aluminium, appliances, equipment rental, trucking, steel, industrial REITs — the
real-economy cyclicals are in deep drawdowns while refining sits 3% off its highs.
That is a stagflation signature: input and energy strength with weak end demand.

## [06:29 ET] REJECTED — KXRECSSNBER-27 YES @ 20 — thin edge, 15-month hold, wrong instrument for my evidence
Worth recording the **resolution mechanics, because the ticker is misleading**:
despite the `NBER` in the name there is no committee judgment and no declaration lag.
- Rule: **two consecutive quarters of negative QoQ annualised real GDP growth,
  Q4 2026 through Q4 2027, on the BEA Advance Estimate.** Expires ~2028-01-31.
- So it is a *technical* recession. 2001 was an NBER recession without two
  consecutive negative quarters; 2022 had two negative quarters and was not an NBER
  recession. The bar is stricter and narrower than "a recession".
- Unconditional base rate for two consecutive negative prints is ~13-16%/yr, so at
  **20c the market is already above the base rate** — it is not asleep.
- And the decisive counter: **real fed funds is only ~+0.3%** (3.88% nominal against
  ~3.6% CPI). The committee itself calls policy "not restrictive". Recessions follow
  genuinely tight policy, and hiking *from* a loose setting is not that. My evidence
  is equity drawdowns in specific cyclicals — sector earnings, not aggregate GDP, so
  it does not map onto the resolution criterion.
- Honest estimate 22-28% against a 20c ask: inside my own error bars, on a 15-month
  capital commitment. No trade.

## [06:30 ET] REJECTED — AA long or short — a levered commodity producer mid-downcycle
AA 42.20, **-50.0%** off its 120-day high, 120-day low 41.01, reports **Oct 15 amc**.
Q2-26 was genuinely strong (record $4B revenue, adjusted net income +51% sequentially
to $562M, record Aluminum segment EBITDA $1,073M), so this is not a broken business.
But the drawdown has four real causes, not a sentiment swing:
- falling aluminium prices and **escalating US-Canada trade tensions** (AA's smelter
  base is heavily Canadian)
- an operational problem at the **Pinjarra** refinery; 2026 alumina shipment guidance
  cut to 11.5-11.6 Mt on Q2 instability
- analysts cut FY26 EPS by **10-12%**
- it closed a **$2.6B senior notes offering in September** to fund the cash portion of
  the South32 bauxite/alumina/aluminium acquisition — i.e. it levered up *into* a
  falling commodity
— source: https://www.sec.gov/Archives/edgar/data/0001675149/000119312526399499/aa-ex99_1.htm
Long is rejected on the leverage-into-downcycle combination; short is rejected
because it sits 1.2 ATR above its 120-day low two sessions before a print, which is
squeeze risk, not reward. **New macro fact worth carrying forward: US-Canada trade
tension is live and is an input cost/tariff channel.**

## [06:31 ET] REJECTED — GS long — the laggard of a lagging sector
GS 895.32, -22.4% off its 120-day high, 120-day low 868.52, reports Oct 13 bmo with
consensus EPS ~$15.39 against $12.25 a year ago (+25.6%), and BofA holds a Buy with a
PT cut to $1,050 from $1,300. That reads like a de-rated compounder — until
relative strength, which strategy.md says to check *before* committing:
- GS 1m **-12.2%** vs XLF -3.76%; 3m **-14.4%** vs XLF -2.39%; i.e. **-14.9pp and
  -18.3pp against its own sector.** 6m -1.4% vs XLF +7.8%.
- So the de-rating is **name-specific**, most plausibly the private-credit exposure GS
  expanded aggressively into, and that question resolves *on* Tuesday's print.
- `XLF` already owns this earnings catalyst at index level, which is the diversified
  way to hold it without taking the single-name credit risk being repriced. No trade.
- Could not fetch: `short GS` (nasdaq read timeout) and `implied GS` (yahoo-options
  401). So no short-interest or options-implied check on any name this run.

## [06:33 ET] SECTOR — P&C insurance is the week's real opportunity, and TRV is the sharp end
The 2026 Atlantic hurricane season effectively did not happen:
- **Five tropical storms and no hurricanes** as of 2026-10-06 — the latest first
  hurricane on record in the satellite era
  — source: https://www.verisk.com/blog/the-perils-shaping-u-s-insured-losses-arent-the-ones-youd-expect/
- **No US hurricane landfall, the first such year in ten.** NOAA's was the first
  below-normal seasonal outlook since 2015, on a strengthening El Nino.
- H1-26 global insured nat cat losses **$44-47B** (Munich Re / Gallagher Re / Aon) —
  the lowest half-year since 2018. Swiss Re: North Atlantic cyclones are normally
  **38%** of full-year weather-related insured losses and fall in H2.
- **The timing is the whole point: Q3 ended Sept 30, so the cat line is already
  fixed and no later storm can change it.** Q3 is the quarter being reported.

Complex scan (250-day history), with earnings dates from the fetched calendar:

| Sym | Close | vs sma20 / sma50 / sma200 | off high | Earnings |
| --- | --- | --- | --- | --- |
| **TRV** | 368.75 | **above / ~at / +14.5%** | -7.5% | **Oct 16 bmo** |
| WRB | 71.91 | above / above / above | -8.9% | Oct 19 amc |
| CB | 341.20 | above / ~at / above | -6.8% | Oct 20 amc |
| AIG | 77.04 | above / above / just below | -11.7% | not in 20d |
| HIG | 129.11 | ~at / below / below | -11.6% | Oct 22 amc |
| CINF | 163.39 | below / below / below | -16.1% | Oct 26 |
| ALL | 229.43 | below / below / ~at | -17.2% | not in 20d |
| KIE (ETF) | 60.08 | below / below / above | -9.7% | n/a |

- **TRV captured** (conviction 4): earliest catalyst, best relative strength, only
  name above all three averages with momentum. Entry 367, stop 352 (2.32 ATR),
  target 398 (the 250-day high) = 2.07:1.
- **WRB and CB are watchlist, deliberately not captured.** Both clear a technical
  screen, but they are the *same driver* three days later, and the correlation rule
  exists to stop one thesis becoming three ideas. WRB is also specialty/commercial
  and so less property-cat geared — the thesis fits CB better than WRB.
- Note the ETF **KIE is weaker than the three leaders**, which says the strength is
  name-concentrated and argues against expressing this through the basket.

## [06:35 ET] CRYPTO — examined properly, and there is no qualifying setup
Weekend runs should lean here, so this is a considered "no", not an omission.
Daily OHLC aggregated from CoinGecko 4-hourly bars (`market_data history` cannot
serve crypto this run — nasdaq has no coverage and Yahoo is 429).

- **BTC 82,948**, daily ATR14 **1,859.86 (2.24%)**, 30d high 87,330, low 75,038.
  Rallied to 85,711 by Oct 5, then **broke down Oct 7-8** (85,611 to an 80,427 low),
  and has consolidated 82-83k for three sessions just under the break.
- **ETH 2,498.85**, daily ATR14 **71.82 (2.87%)**, 30d high 2,804.42, low 2,361.16.
  Broke harder — 2,692 on Oct 6 to 2,409 on Oct 8, **-10.5% in two days** — and is
  the weaker of the two.
- Alts led down on the 24h tape (ADA -3.2%, AVAX -2.0%) with majors flat, so there is
  no weekend squeeze underway.

**REJECTED — short /MBT (micro bitcoin futures).** The bear case is real — a failed
push at 85-87k, a clean two-day break, and a tightening Fed draining the liquidity
this asset trades on — but it **cannot clear the floors honestly**:
- The invalidation level is a new 30-day high, so the stop belongs above 87,330, call
  it 87,700. From an 83,000 entry that is 4,700 of risk = **2.53 ATR**, which is the
  minimum the 2.5 ATR futures/crypto floor allows.
- Clearing the 2.0 R:R floor on 4,700 of risk then demands 9,400 of reward — a
  **73,600 target, below the 30-day low of 75,038.** Against the 76,000 target the
  chart actually supports, the ratio is **1.49:1** and the idea fails.
- Tightening the stop to make it work is the exact failure mode this repo logs, so
  the idea is dropped rather than re-cut. **No crypto candidate today.**

## [06:37 ET] REJECTED — CB and WRB long — dominated by TRV on the same driver
Both clear a technical screen and both would be the *same* thesis as TRV, so the
question was only whether either is the better horse. Neither is:
- **CB** 341.20, broke out Oct 8 (335.27 low to 344.97) exactly like TRV, above sma20
  335.98 and sma200 330.58, -6.8% off the 250-day high, earnings **Oct 20 amc**.
  Technically it clears: entry 341, stop 329 (below the sma200) = 2.32 ATR, target 366
  = 2.08:1. But relative strength is only +4.05% over 6m against XLF +7.8% and SPY
  +14.59%, and 3m **-3.82%**; analysts are already **51.4% bullish** so there is far
  less room to re-rate; and its four beats are small (+4.4%, +0.3%, +7.7%, +18.2%)
  against TRV's +83.4% in Q2. Insiders 0 buys / 6 sells.
- **WRB** 71.91 is above all three averages, -8.9% off high, earnings Oct 19 amc — but
  it is specialty/commercial, so it is the *least* property-cat geared of the three and
  the quiet-season thesis applies most weakly to it. Its only honest entry is the
  69.60 sma50/sma200 confluence, 3.2% below the market.
- Chubb is the best *thesis* fit and Travelers the best *setup*; TRV wins on evidence
  on every axis, so one position, not three. **Both go to the watchlist.**

## [06:38 ET] REJECTED — defense (LMT/NOC/GD/RTX/LHX/HII/ITA) — a real signal I could not explain in time
Every name is below its 20-, 50- **and** 200-day, which is a sector event, not rotation:
- NOC 480.72 **-37.9%** off high (sma200 596.09) | LHX 236.97 **-37.5%** (sma200 309.38)
- HII 264.80 **-42.4%** (sma200 342.39) | LMT 509.59 -26.4% (sma200 563.66)
- RTX 185.97 -18.0% | GD 331.27 -17.2% | ITA (ETF) 206.65 -19.5%
Searching gives a *mixture* and no clean catalyst: Q1 earnings misses and free-cash-flow
and capex concerns at LMT and NOC, a Space Systems charge, no finalised defence
appropriations bill so agreements cannot be fully funded, and fears of a political shift
cutting budgets. Sources are commentary aggregators, not primary.
— source: https://www.tikr.com/blog/lockheed-martin-has-fallen-nearly-25-from-its-2026-high-is-it-finally-time-to-buy
**No trade:** a 38-42% drawdown with no base and no reliably sourced cause is not an
entry, and I will not put a position on a guess. **This is the top research priority
for the next run** — if the cause is appropriations timing it is a dated catalyst and a
large opportunity; if it is structural budget reduction it is a value trap.

## [06:39 ET] WATCHLIST — not actionable today, with the condition to wait for
- **CB** — buy 341 / stop 329 / target 366 **after** TRV reports Oct 16. If TRV confirms
  a cat-light quarter, CB's Oct 20 print is the second, better-cat-geared read.
- **WRB** — buy only on a pullback to the 69.60 sma50/sma200 confluence, stop 66.80,
  target 78.00 (3.0:1). Do not chase it at 71.91.
- **GS** — reconsider only *after* the Oct 13 print answers the private-credit question.
  A credit-clean result with the stock near its 868.52 low would be a real idea; it is
  not one before the print.
- **Defense / ITA** — wait for a reliably sourced cause and any base at all.
- **STLD** buy 245.5 (published 2026-10-10) is unfilled with price at 238.38; level
  unchanged, nothing to amend.
- Equities **were closed all day**, so every equity entry above is for the **Monday
  Oct 12 open** (equity markets open, bond market closed for Columbus Day).

## [06:40 ET] DATA QUALITY — what failed this run, for data_quality_notes
1. **Yahoo returned HTTP 429 on both hosts all run.** Consequences: **no VIX, no DXY,
   no index level (SPX/NDX/DJI/RUT), no ES/NQ futures, no gold or WTI futures price.**
   No vol-regime or index-level claim is made anywhere above, and no futures idea was
   written, because I could not price a futures contract honestly.
2. **`market_data.py history` cannot serve crypto** — nasdaq has no coverage and Yahoo
   was 429. Worked around by aggregating CoinGecko 4-hourly bars into daily UTC OHLC to
   get a true daily ATR (BTC 2.24%, ETH 2.87%). Without that the available series give
   4-day bars (6.23%) or 4-hourly (0.52%) and **both would have mis-set a crypto stop by
   a factor of 2-3.**
3. **`market_data.py events` cannot find any macro market.** It requests only the first
   200 open Kalshi markets and filters client-side, so against tens of thousands of open
   markets the result is effectively arbitrary — "Fed" returned a single football market
   and "CPI", "inflation", "bitcoin" returned zero. **Worked around** by querying
   `api.elections.kalshi.com` per series and per event ticker; note prices live in the
   `*_dollars` fields on the single-market endpoint and are **null on the list endpoint**.
   Every event price above came from the per-market endpoint. *This is a code defect, not
   a data outage — it needs a `series_ticker` parameter and a test.*
4. **`short <SYM>` failed** (nasdaq read timeout) and **`implied <SYM>` failed**
   (yahoo-options HTTP 401). So **no short-interest and no options-implied-move check was
   possible on any name**, including TRV. The TRV target is therefore set on price
   structure alone and has **not** been tested against what options price.
5. Could not reach **bls.gov** to confirm the Sept CPI date primarily; Oct 14 08:30 ET is
   from calendar aggregators. Earnings dates are all from the fetched finnhub calendar.
6. Robinhood product pages were **not** re-verified this run — unnecessary, as every
   captured idea is a US-listed large-cap stock or ETF (XLF, TRV, CCJ, LCII, LULU, NKE).
   No futures, crypto or event contract was captured, so no availability check was owed.

## [06:41 ET] RESEARCH COMPLETE
- **candidates: 6** — 1 genuinely new idea, 2 amendments to open positions, 3 exits.
  - **TRV** buy 367 / stop 352 / target 398, conviction 4 — the one new idea
  - **XLF** hold, levels unchanged, conviction 3 — update, bank earnings Oct 13-16
  - **CCJ** target cut 135 -> 108 and downgraded to conviction 2 — flagged as failing
    the 2.0 floor from its fixed entry, i.e. would not publish as new today
  - **LCII / LULU / NKE** `sell` = **close the long leg**. LCII sits on its 120-day low
    with no stop and a +76% target; LULU and NKE were each held long *and* short at the
    same time with risk defined on only one side.
- **The honest shape of today: this is a management day, not an idea day, and I am not
  padding it.** One new position cleared the bar. Energy and refining lead and I already
  own them (XLE, DINO); power leads and I own it (CEG, confirmed by the Google-
  Constellation deal); the REIT, housing and duration shorts are already live as
  unfilled orders (IYR, ITB, TLT); and the bank earnings catalyst is already owned at
  index level through XLF. The cyclicals that are cheap are cheap at their lows with no
  base, and the macro event contracts priced to the cent.
- **The regime call is the most useful output and should lead the report:** the Fed is
  **hiking**, not cutting — 3.75-4.00% now, a 74c implied probability of another 25bp on
  Dec 9, inflation risks "skewed to the upside", policy judged "not restrictive", and no
  return to 2% until **2029**. Energy and real assets strong, cyclicals and duration
  weak. Every rate-cut-dependent thesis should carry a higher bar than it did last week.
- **Track record was applied, not noted and ignored:** 2/15 overall, stocks **0/8**, and
  conviction-2 **0/4**. So GS, AA, EQT, NRG, TLN, CB, WRB and the refiners were all
  rejected rather than written up thin, the only new stock idea carries 4 kinds of
  evidence, and CCJ was cut to conviction 2 at 1% rather than defended.
- **coverage gaps:** defense sector cause (top priority next run); no short-interest or
  options-implied check on anything (both sources down); no VIX/DXY/index/futures prices
  all run; PGR and ALL have no earnings date inside 20 days and were not researched;
  small/micro caps were scanned only via next-week earnings, not screened deliberately.
- **sources that failed:** Yahoo Finance (429 all run, both hosts), yahoo-options (401),
  nasdaq short interest (timeout), finnhub indices (subscription required), stooq
  (404 on `^` symbols), bls.gov (unreachable); `market_data.py events` returned no usable
  macro market and was bypassed via the Kalshi API directly.

## [06:45 ET] ADDENDUM to RESEARCH COMPLETE — defense, partially resolved, still not a trade
Spent remaining budget on the run's biggest unexplained signal. The picture is now
half-answered, and the half that is answered points the *opposite* way to the tape:

- **The FY2027 budget direction is sharply UP, not down.** The administration requested
  ~$1.1 trillion discretionary for DOD plus $350B mandatory via reconciliation; the
  White House budget document frames FY2027 at $1.5 trillion, **a 44% increase**. The
  House Appropriations Committee approved its bill in June 34-27 at a $1.072 trillion
  discretionary allocation.
  — source: https://www.congress.gov/crs-product/R49023
  — source: https://appropriations.house.gov/news/press-releases/committee-approves-fy27-defense-appropriations-act
- **What is broken is timing, not level.** Congress has enacted no FY2027 defense
  appropriations and no FY2027 NDAA; Senate appropriators are stalemated over the
  defense/nondefense balance; CSIS expects full-year discretionary appropriations
  **not before early December**. Under a CR, agreements cannot be fully funded, which
  delays awards and hits near-term revenue and cash conversion.
  — source: https://www.csis.org/analysis/tracking-fy-2027-defense-appropriations-reconciliation-and-supplemental-request
- Plus genuine company-specific execution: LMT's Q1 miss and weaker free cash flow,
  NOC's Space Systems charge and a $200M capex increase with FY EPS guidance slightly
  below consensus.

**Still no trade, for three reasons I will not argue myself out of at the end of a run:**
1. A **+44% budget request against a 38% drawdown** is too large a disconnect to be
   explained by funding timing alone. A gap that big usually means the market knows
   something I have not found, and the honest statement is that I have not found it.
2. **My sources conflict on the central fact.** A House Appropriations page carries a
   headline saying a bill went to the President's desk and averted an October shutdown,
   which contradicts CSIS and Breaking Defense. I could not resolve which is current,
   and the whole thesis turns on it.
3. Nothing has based. Every name is still below all three moving averages, so there is
   no level to lean a stop on.

**Watchlist, with the condition to wait for:** the primes report in roughly ten days
(LMT, NOC, GD, RTX all late October), which prices the execution half. The
appropriations half resolves around early December. **ITA is the right instrument if
this becomes a trade** — the drawdown is sector-wide (-18% to -42%) and spread across
execution problems at different companies, so the basket avoids picking which
management team is the broken one.

**Next run should open here with a sharper question**, in this order: (a) confirm from
congress.gov or appropriations.house.gov *primary* pages whether FY2027 defense
appropriations or a CR is actually enacted as of that date; (b) if the budget is rising
and the drawdown is timing plus execution, size ITA off the post-earnings base. Do not
re-derive the sector scan — the levels are in the 06:38 block above.
