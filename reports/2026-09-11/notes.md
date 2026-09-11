# Research log — 2026-09-11

## [06:04 ET] MACRO — rates, tape, regime
Session note: US equity market closed; freshest honest prices are 2026-09-10 closes (session=pre).
- FRED: US10Y 4.83% (2026-09-09), US2Y 4.43% (09-09), Fed funds eff 3.63% (09-09), 10y-2y +0.39 (09-10) — source: https://fred.stlouisfed.org/series/DGS10
- UNRATE 4.1% (Aug 2026) — source: https://fred.stlouisfed.org/series/UNRATE
- 2026-09-10 closes (finnhub): SPY 757.83 (-0.60%), TLT 80.78 (-1.16%), GLD 396.36 (-1.73%), XLE 64.93 (-0.58%), CCJ 97.42 (-2.98%), NKE 36.62 (-1.95%), BCC 75.05 (-1.16%), LULU 96.88 (-2.85%), SVRA 5.32 (-1.75%)
- SPY: atr14 5.36 (0.71%), sma20 767.56, sma50 758.25, 60d range 716.58-779.37, -2.76% off high
- Regime read: long bonds AND gold AND equities all down together = a rates/duration shock, not an equity-specific risk-off. 10y at 4.83% with a +39bp curve is a term-premium repricing.
- FAILED SOURCES: yahoo 429 on all index symbols (^GSPC ^NDX ^DJI ^RUT ^VIX), finnhub index quotes require CFD subscription, stooq 404. So no VIX, no index level, no DXY, no WTI, no /ES quote this run. CoinGecko crypto prices FAILED in macro block.

## [06:04 ET] POSITION UPDATE — TLT — BUY @82.60, stop 80.95, last 80.78
- TLT closed 2026-09-10 at 80.78, which is BELOW the 80.95 stop. This position is stopped out on the close, not a hold decision.
- Also note a separate TLT SELL (exit) row opened 2026-09-02 @81.87 — that exit call is now +1.3% right.

## [06:12 ET] CATALYST — the two dated events that frame today
- **Aug CPI released TODAY 2026-09-11 08:30 ET (BLS).** Consensus headline +3.4% YoY (matching July), core 2.4% YoY (down from 2.5%), m/m +0.4% headline / +0.3% core — source: https://insight.factset.com/consumer-price-index-cpi-for-august-2026-is-projected-to-rise-3.3-year-over-year and https://www.fxstreet.com/news/us-core-cpi-data-set-to-ease-in-august-as-markets-reprice-fed-september-rate-decision-202609110830
- **FOMC decision 2026-09-16** (Kalshi KXFEDDECISION-26SEP settles 2026-09-16T17:59Z).
- Aug PPI +0.4% m/m, **5.4% YoY** — source: https://www.cnbc.com/2026/09/09/stock-market-today-live-updates.html

## [06:12 ET] MACRO — the market now prices a Fed HIKE next week
Kalshi KXFEDDECISION-26SEP ladder, fetched 2026-09-11 ~06:10 ET (api.elections.kalshi.com):
| Leg | Last | Prev | yes_bid/ask | OI |
| --- | --- | --- | --- | --- |
| Hike 25bp (H25) | **0.61** | 0.55 | 0.60/0.61 | 4.80M |
| Maintains (H0) | **0.39** | 0.46 | 0.38/0.39 | 12.72M |
| Hike >25bp (H26) | 0.01 | 0.01 | 0.01/0.02 | 8.87M |
| Cut 25bp (C25) | 0.01 | 0.01 | 0.00/0.01 | 6.97M |
| Cut >25bp (C26) | 0.01 | 0.01 | 0.00/0.01 | 1.18M |
26OCT: H25 0.30 (prev 0.28), H0 0.68 (prev 0.69), C25 0.02 (prev 0.05).
- Read: 61% odds of a 25bp HIKE on Sep 16, up 6pts in one session. Oct then prices 68% hold — one hike, not a cycle.
- **Consequence: the prior report's pending `KXFEDDECISION-26SEP-H0` YES @47 (published 09-03) is now 39c and going the wrong way.** The thesis (Fed holds) is being repriced against us with CPI still to print.

## [06:12 ET] NEWS — oil supply shock is the driver, not an equity story
- 2026-09-10: stocks fell a 4th straight session; 10y Treasury yield above **4.95%**, highest since Oct 2023; 2y +15.2bp to 4.579% — source: https://www.kiplinger.com/investing/stocks/stocks-drop-as-treasury-yields-hit-new-highs-stock-market-today
- US CENTCOM destroyed five Iranian oil tankers 2026-09-08; Houthi strikes on Saudi oil facilities wounded 73. Brent closed $101.21 on 2026-09-09 (+3.4% session) — source: https://discoveryalert.com/news/brent-crude-101-iran-tankers-hormuz-september-2026/
- Regional Gulf exports fell 2.1 mb/d to 15 mb/d after the Strait was effectively closed again in early July — source: https://www.congress.gov/crs-product/R45281
- **This is a term-premium/inflation shock, not a growth scare.** That is why gold fell with bonds: real yields up beats the haven bid.

## [06:14 ET] LEVELS — energy complex, 2026-09-10 closes
Crude proxy USO **+5.61%** on the day. Energy EQUITIES did not follow, and split cleanly:
- Producers UP: DVN +2.12% (50.02), FANG +1.36% (205.39)
- Flat/down: OXY -0.23% (61.16), XOP +0.24% (195.47), XLE -0.58% (64.93)
- Down hard: OIH -2.13% (420.22), HAL -2.85% (36.07), SLB -1.82% (56.01), MPC -1.76% (392.42), VLO -0.91% (385.43), DINO -0.39% (107.72)
- Read: the tape is discriminating correctly. A Hormuz *supply* shock is unambiguously good for US onshore producers (full price capture, zero Gulf exposure), ambiguous for refiners (crude is their input) and bad for services (this is not a drilling cycle).
- Histories (120d): DVN atr14 1.163 (2.32%), sma20 47.98, sma50 45.25, range 40.00-52.71, -5.1% off high, $524M ADV.
  FANG atr14 5.431 (2.64%), sma20 203.45, sma50 196.59, range 170.10-216.90, $383M ADV.
  OXY atr14 1.404 (2.29%), sma20 59.95, sma50 56.83, range 47.77-67.45, **-9.33% off high**, $470M ADV.
  XLE atr14 1.205 (1.86%), sma20 63.51, sma50 59.89, range 52.62-66.17, -1.87% off high.

## [06:14 ET] REJECTED — OXY BUY — biggest laggard (-9.3% off high) but at a 2.18 ATR stop (58.10) the prior-high target 67.45 gives R:R 2.04, and widening the stop to the sma50 (56.83) drops it to 1.44. Bare-minimum ratio = failed the floor, not passed it.
## [06:14 ET] REJECTED — HAL / SLB / OIH — services fell 2-3% into a crude spike. Correct: a geopolitical supply premium does not fund a drilling capex cycle. No thesis in buying the dip here.

## [06:20 ET] LEVELS — rate-sensitives are already repriced, which kills the obvious short
120d histories, 2026-09-10 closes:
- ITB 88.22 (-2.31% on the day), atr14 1.90 (2.15%), sma20 95.41, sma50 97.00, range 84.98-106.38, **-17.07% off high, only +3.81% off the low**
- LEN 77.90 (-3.54%), atr14 2.227 (2.86%), sma20 84.88, sma50 85.00, range 76.63-97.94, **-20.46% off high, +1.66% off the low**
- IYR 99.97 (-0.93%), atr14 1.079 (1.08%), sma20 103.49, sma50 104.21, range 92.45-108.17
- TLT 80.78 (-1.16%), atr14 0.642 (0.79%), sma20 82.29, sma50 83.08, range 80.665-87.79 — **closed 0.14% off its 120-day low**
Also: KBH -3.98% (47.75), DHI -2.42% (135.57), PHM -2.12% (116.41), TOL -1.90% (132.48), XHB -2.34% (96.91)

## [06:20 ET] REJECTED — LEN / ITB SELL_SHORT — the 10y at 4.95% is a real headwind and LEN reports 2026-09-16 AMC, so the catalyst is dated and inside the horizon. But LEN closed 1.66% off its 120-day low and ITB 3.81% off its. Shorting a group that has already given back 17-20% from its high, at the bottom of its range, the session before an earnings print, is selling the hole. Right about the business, wrong about the entry — exactly the failure mode the short-interest rule warns about. No short.
## [06:20 ET] REJECTED — LEN BUY — the mirror is no better: -20% off the high is not a valuation case, it is a falling knife with a 4.95% 10y against it and earnings in three sessions. No thesis either way.
## [06:20 ET] POSITION UPDATE — IYR — SELL_SHORT @103.6 published 2026-09-02, never filled
- decision: withdraw, do not re-pitch. IYR is now 99.97, i.e. 3.5% BELOW the short entry, and a 1.8 ATR (etf) stop off 103.6 implies a target near 99.7 — the trade has already travelled its entire intended distance without ever filling. Re-publishing the same level would be pitching a move that has happened.

## [06:20 ET] CRYPTO — coingecko, fetched 06:19 ET
- BTC 77,104 (-1.12% 24h), ETH 2,472.69 (+0.14%), SOL 99.57 (-1.62%)
- BTC at 77.1k against the prior report's pending `/MBTU6` SHORT @64,340 and `BTC` SELL @63,400 — both levels are ~17% below spot and were published 2026-08-16/18. Those are stale shorts that the market has run away from; note for synthesis, do not re-pitch.
- Crypto is not confirming the inflation shock: a genuine debasement trade would have BTC bid with oil. It is drifting with equities instead. No crypto idea today on that basis.

## [06:33 ET] NEWS — the LNG leg of the Hormuz story, and why it is NOT a trade
- EIA (published 2026-04-28): the Strait closed **2026-02-28**, cutting >10 Bcf/d of global LNG supply, ~20% of world LNG trade, mostly Qatari. No laden LNG vessel crossed 2026-03-01 to 2026-04-24. QatarEnergy declared force majeure 2026-03-04 — source: https://www.eia.gov/todayinenergy/detail.php?id=67604
- TTF reached $14.80/MMBtu by w/e 04-24 (+35% since the closure); JKM $16.02 (+51%). Goldman: TTF could reach EUR74/MWh, +130%, on a full one-month halt — source: https://www.investing.com/news/commodities-news/european-gas-prices-could-jump-130-on-hormuz-disruption-goldman-estimates-4534261
- **Henry Hub FELL 9% since 2026-02-28** — US gas is insulated, prompt US gas under $3/mmBtu.
## [06:33 ET] REJECTED — LNG (Cheniere) — the LNG dislocation is 6+ months old (closure 2026-02-28), not new information, and the stock is acting like it: 277.84, -7.66% off its 120d high, gapped 292.00 -> 276.02 on 09-08 during the supply crisis it supposedly benefits from. A stock falling through its own bull catalyst is telling you the catalyst is priced.
## [06:33 ET] REJECTED — EQT / AR / RRC (US gas producers) — the mechanism does not reach them. They sell at Henry Hub, which is DOWN 9% since the closure and under $3/mmBtu; on 09-10 they barely moved (EQT +0.60%, AR +0.13%, RRC +0.34%) while USO rose 5.61%. No transmission channel, no trade.

## [06:36 ET] LEVELS — tankers are the one energy sub-sector the tape bid on 09-10
- FRO 48.40 (+2.52%), atr14 1.605 (3.32%), sma20 44.15, sma50 40.56, range 31.755-48.72, **-0.66% off high**, +52.4% off low, ADV $111M
- TNK 98.25 (+2.01%), atr14 3.529 (3.59%), sma20 90.14, sma50 80.52, range 64.04-98.40, -0.15% off high, ADV $47M
- STNG 84.51 (+1.75%), atr14 2.175 (2.57%), sma20 79.57, sma50 77.90, range 67.32-87.39, -3.3% off high, ADV $66M
- INSW 102.14 (-2.37%) is the odd one out and I did not resolve why — coverage gap.
- Captured FRO (most liquid, pure VLCC, most direct Hormuz rerouting exposure). Did NOT also capture TNK/STNG: three tanker longs would be one idea with extra steps and would breach the 3-per-driver correlation cap alongside DVN, which is already a Hormuz trade.
- Honest caveat recorded: FRO and TNK are both AT their 120-day highs, so clearing the 2.0 R:R floor with a proper 2.7 ATR stop requires an extension target (57.50, +18%). That is the weakest part of the idea and the red team should press on it.

## [06:36 ET] REJECTED — KXFEDDECISION-26SEP-H0 YES @39c (the pending position published 09-03 @47c) — do NOT average down.
- I went looking for an edge on the dovish side: core CPI is expected to EASE to 2.4% YoY today, the FOMC blackout began ~09-05 so the 46c->39c repricing came from oil and PPI rather than from Fed guidance, and central banks conventionally look through a supply shock.
- But the one independent probability source I could find (Chase, **published 2026-08-05**) cites ~65% for a hike, i.e. MORE hawkish than Kalshi's live 61%. A widely-quoted "82%" figure in search results does not trace to a dated primary source and I will not trade on it.
- So the live 61% is the best number available and I have no measurable disagreement with it. An event contract with no stated probability edge is explicitly not a thesis. No new position; the existing @47 pending entry should be reported as unfilled and going against us.

## [06:12 ET] TIMESTAMP CORRECTION
The clock labels on the blocks above were estimated rather than read, and ran ahead of the real clock — everything above was written between 06:01 and 06:12 ET, not 06:04-06:36. The findings, prices and sources are unaffected; only the labels were wrong. All blocks below carry a timestamp read from `date`.

## [06:15 ET] LONG_TERM candidate worked and REJECTED — LMT
Why it looked good: 530.12, **-16.98% off its 120-day high (638.51)**, below sma20 561.70 and sma50 556.36, into a live Gulf shooting war and a global rearmament cycle. Analyst trend is turning UP, not down: strong_buy 5->6, buy 6->7, hold 16->14, sell 1 across 2026-07-01 -> 2026-09-01 (finnhub).
Why it de-rated (the actual reason, not a guess): repeated fixed-price reach-forward losses — $1.7B in Q4 2024, $950M in 2025, $1.6B of program charges; Q1 2026 EPS $6.44 vs $6.70 est with FCF -$291M and operating cash flow $1.41B -> $220M; F-35 deliveries fell to 19 in Q2 2026 from 50 a year earlier. Investors now treat fixed-price execution risk as structural — source: https://seekingalpha.com/news/4469862-lockheed-martin-sinks-after-surprise-program-losses-slash-q2-earnings
Offsetting: Q2 2026 EPS $7.94 vs $7.20, revenue $20.06B +10.5% YoY, **record backlog $230.4B** (~2.85x annual sales), FY26 guidance EPS $29.95-30.65, sales $79.75-81.75B, FCF $7.0-7.2B, dividend $13.50 (2.55% at 530.12), 23 straight years of increases — source: https://www.investing.com/news/transcripts/earnings-call-transcript-lockheed-martin-beats-q2-2026-estimates-shares-jump-93CH-4809232
**Valuation arithmetic, and why it fails:** 530.12 / $30.30 midpoint FY26 EPS = **17.4x**. A defensible target is 19x ~$32 of 2027 earnings power = **$610**, i.e. +15% over 18-24 months. The honest bear case is not shallow: if fixed-price execution really is structural, 15x a charge-depressed ~$27 = **$405**, i.e. -24%. R:R = 80/125 = **0.64 against a 2.5 long-term floor**. Moving the entry down to the 120d low does not save it (115/90 = 1.28).
**REJECTED — LMT — +15% upside against a -24% bear case is 0.64 R:R, nowhere near the 2.5 long-term floor. A cheap-looking prime whose own bear case is four times the size of its upside is not a long-term holding, it is a value trap with a dividend.** No insider buying to offset (0 open-market buys in 6 months, 11 sells).

## [06:18 ET] NEWS — record refining margins, and the reason it is NOT a trade
- US Gulf Coast diesel crack vs WTI passed **$100/bbl on 2026-08-17, the first time ever**, and sits near $93-94 in late August — above the 2022 peak — source: https://rbnenergy.com/daily-posts/blog/100bbl-diesel-crack-or-how-2026-exposed-fragility-global-refining (page itself 403s to a non-browser fetch; figure taken from the search abstract and corroborated below)
- Total US distillate stocks ~105.6 million bbl w/e 2026-08-14, **lowest for the time of year since the mid-1990s**; national diesel average $5.78/gal on 2026-09-03 vs the June 2022 record $5.8159 — source: https://piptheory.com/research/diesel-crack-spread-record-100-august-2026
- Cause is cumulative: Middle East refineries damaged in the Iran conflict, Hormuz product flows disrupted, Russian refining repeatedly hit by Ukrainian drone strikes — source: https://www.eia.gov/todayinenergy/detail.php?id=67865
- Refining stocks were already reported as soaring on this in July — source: https://www.forbes.com/sites/garthfriesen/2026/07/23/refining-stocks-soar-as-crack-spread-hits-record-high-in-2026/

## [06:19 ET] REJECTED — VLO / MPC / DINO / PSX / PBF / DK (refiner longs)
My first read was that 09-10 (MPC -1.76%, VLO -0.91%, DINO -0.39% into USO +5.61%) was the market trading crude-as-input-cost while ignoring record cracks. The price history says that read is wrong. Gains off the 120-day low: **PBF +113.4%, DK +102.3%, DINO +94.3%, MPC +86.3%, VLO +79.5%, PSX +68.3%** — and every one of them closed within 2.0-3.7% of its 120-day high. This group has already doubled on the crack story. The one-day dip is noise inside a vertical move, not a dislocation.
Worse, the crack itself has already rolled: $100+ on 08-17, $93-94 by late August. Refiners de-rate *before* margins peak, because the market prices the next barrel. Buying a doubled cyclical 2% off its high as its margin driver eases is buying the top of a margin cycle.
## [06:19 ET] POSITION UPDATE — DINO — BUY @99.5 published 2026-08-22, never filled
- decision: **withdraw, do not re-pitch.** DINO is 107.72, 8.3% above the unfilled entry and 94% off its 120-day low. The level is stale and the thesis is now crowded. Chasing it 8% higher into a fading crack spread would be re-pitching an idea whose whole edge was the entry price.

## [06:25 ET] LEVELS — airlines, the paying side of the diesel/jet crack
120d, 2026-09-10 closes: AAL 12.85 (-0.70%), atr14 0.364 (2.84%), sma20 13.632, sma50 14.957, range 10.09-18.79, -31.61% off high, ADV $728M
UAL 106.49 (-0.59%), atr14 3.457, sma20 113.25, sma50 119.89, range 84.64-138.77, -23.26% off high
DAL 78.24 (-0.65%), atr14 2.071, sma20 81.92, sma50 85.70, range 62.68-95.68, -18.23% off high
JETS 27.84, atr14 0.573, sma20 29.37, sma50 30.76, -18.26% off high
- Captured AAL short (most fuel-levered, thinnest margins). Not UAL/DAL as well — one expression of the view is enough and the correlation cap binds (below).

## [06:25 ET] SOURCES THAT FAILED — material, affects two ideas
- `market_data.py short AAL/UAL/DAL` — nasdaq short-interest feed returned `ok: false` with all fields null for every symbol. **No short-interest or days-to-cover check was possible on any idea today**, which is a real gap for the AAL short specifically.
- `market_data.py implied AAL/DAL` — yahoo options endpoint returns HTTP 401. No options-implied-move check was possible on any idea today.
- yahoo chart API 429 throughout: no VIX, no index levels, no DXY, no WTI/Brent futures quote, no /ES or /MES quote. All crude references in these notes are USO (the ETF) and sourced Brent prints, never a futures quote I did not fetch.
- rbnenergy.com 403s to WebFetch.

## [06:26 ET] CORRELATION CAP — reached, and I am stopping here on this driver
DVN (long US producer), FRO (long tanker), AAL (short fuel consumer) are **three expressions of one bet: oil stays high**. That is the cap in `config/strategy.md`, and it is a genuine concentration — a negotiated Gulf de-escalation loses on all three simultaneously. No further oil-driven idea will be captured today regardless of how good it looks, and synthesis should state this concentration plainly in `data_quality_notes`.

## [06:19 ET] POSITION UPDATES — the rest of the open book (real clock from `date`)
- **CCJ** BUY @94.00, last 97.42 (+3.6%) — decision: **HOLD, and add a stop at 85.00 where there was none.** Uranium spot $90/lb on 2026-09-09, +3.69% m/m, +17.8% y/y; long-term contract price highest since 2008; Cameco raised its 2026 revenue/realized-price/cost outlook. Analyst trend unchanged and strong (5/13/4/0 since July). The 09-10 drop of 2.98% was the broad rates risk-off, not a uranium event. Captured. — sources: https://www.ans.org/news/article-8000/uranium-prices-reflect-strong-outlook-raise-supply-questions/ , https://tradingeconomics.com/commodity/uranium
- **BCC** BUY @76.50, last 75.05 (-1.9%) — decision: **CLOSE.** Market cap $2.62B, ADV only $23M. Its customers are at 120-day lows (LEN +1.66% off its low, ITB +3.81% off its) with the 10y above 4.95%. The housing thesis is being actively falsified. Captured as a `sell`.
- **SPY** SELL_SHORT @773.00, last 757.83 (+1.96%) — decision: **HOLD, all levels unchanged**, cover at the 750 target. Explicitly NOT trailing the stop: from a 773.00 entry a trailed stop would sit well under 1 ATR and would be the ratio-flattering move `config/strategy.md` forbids. Captured.
- **SVRA** BUY @5.35, stop 4.60, last 5.32 (-0.6%) — decision: **HOLD, stop unchanged.** Below sma20 5.44 and sma50 5.61 but well clear of the stop; atr14 0.199 (3.74%), ADV $7.8M (thin but above the $500K floor). No new information today and I did no biotech work this run — recording that as a gap rather than pretending to a view. No new recommendation: nothing changed.
- **GLD** BUY @398.00 target 520, last 396.36 (-0.4%) — decision: **HOLD, levels unchanged, no new recommendation.** Gold fell 1.73% on 09-10 because real yields rose, which is the one macro setup that genuinely hurts it. Invalidation to watch: two consecutive closes below the sma50 at 390.65. **Conflict flagged for synthesis:** a `GLD` SELL @406.77 published 2026-09-08 is still pending above the market alongside this open BUY. I did no gold valuation work today, so I am not re-pitching either side — the 520 target would not survive an honest bear case anyway (at a -14% bear case near 340 the long-term R:R is ~2.1, under the 2.5 floor).
- **NKE** BUY @40.75 / **LULU** BUY @115.00 — the exit calls published 2026-09-08 (NKE SELL @38.40, LULU SELL @100.61) were right and are both still right: NKE 36.62 is 0.19% off its 120-day low and 32.5% off its high; LULU 96.88 is 1.26% off its low and 43.1% off its high with a 6.27% ATR. Reaffirm closed. **No re-pitch in either direction** — a falling knife is not a value case and I did no consumer work today.
- **Stale pending shorts, for synthesis, not re-pitched:** `BTC` SELL @63,400 and `/MBTU6` SHORT @64,340 (published 2026-08-16/18) sit ~17% below a spot BTC of 77,104. The market ran away from them.

## [06:21 ET] LONG_TERM — DG captured, and the arithmetic behind it
DG 122.99 (-1.27% on 09-10, four straight down sessions from 133.21 on 09-04), atr14 4.270 (3.47%), sma20 125.03, sma50 123.28, range 99.57-134.125, -8.3% off high, ADV $288M, market cap $27.13B on 220.59M shares.
Q2 2026 call transcript read directly (published 2026-08-27) — source: https://www.investing.com/news/transcripts/earnings-call-transcript-dollar-general-tops-q2-2026-estimates-shares-jump-93CH-4879767
- EPS **$2.48 vs $2.00 estimate** (+24%); same-store sales **+3.5%** on traffic **+2.0%**; gross margin **32.6%, +127bp**
- FY26 guidance RAISED: net sales +4.0-4.3%, SSS +2.5-2.9%, diluted EPS **$7.80-8.00**
- Buyback restarts in Q3, **up to $700M in H2** against a $27.1B cap
- Vasos: the $100,000+ income cohort is shopping DG "on a more everyday basis", including non-consumables
- Management's OWN named headwind: "higher and more volatile fuel prices", "higher than anticipated fuel costs". ~$0.25/share of the beat was a tariff refund.
**Valuation:** 122.99 / $7.90 guidance midpoint = **15.6x**. Target 155 = 18.2x ~$8.50 FY27. Bear case 100 = 12.8x flat $7.80, and is the actual 120-day low (99.57), not a hypothetical. At 122.99 the long-term R:R is only 1.62 — **it does not clear the 2.5 floor at the current price**, which is precisely why the entry is an accumulation zone at 115 (R:R 2.67), not a buy here.
**DISCREPANCY RECORDED, not resolved:** the transcript reports net sales **+0.2% YoY** while a secondary source reported +5.2%; +0.2% alongside +3.5% SSS does not reconcile and I could not settle it in the time available. I used the primary-source figure and put the discrepancy in the counter-argument rather than quietly taking the flattering number.
Analyst trend flat: 10 strong_buy / 8 buy / **21 hold** / 1 sell, unchanged four months. No open-market insider buys in six months (0 buys, 0 sells).
**Why this is not a fourth oil bet:** DG is the one idea here that management themselves say is HURT by high fuel. It partially offsets the DVN/FRO/AAL concentration rather than adding to it.

## [06:21 ET] REJECTED — GIS / CAG (packaged food)
GIS 35.96 (-3.05%), down six straight sessions from 41.20 (08-31), -12.7% in six sessions; atr14 1.260 (3.5%), sma20 39.38, sma50 37.87, -14.79% off high. **Earnings 2026-09-15** (fetched calendar, EPS est $0.724, rev est $4.38B) — a genuine dated catalyst two sessions out.
CAG 14.70 (-2.71%), -12.16% off high, also falling.
The fundamental story is right — branded packaged food is squeezed from both ends by input and freight inflation and by the private-label trade-down DG is capturing. But shorting a name that has already fallen 12.7% in six sessions *into* its own earnings print is a binary bet at the worst possible moment, and buying it is catching the knife the trade-down thesis says should keep falling. **No position either way; the view is already expressed long DG, which is the same trade with a balance sheet behind it.**
## [06:21 ET] REJECTED — KR — 56.95, -23.51% off its 120-day high but only +5.17% off its low, below both SMAs. Same trade-down beneficiary logic as DG but with none of DG's evidence: I did not read a Kroger filing and had no time to. Not published on a hunch.

## [06:23 ET] EVENT CONTRACTS — the CPI ladder priced, and why I am not trading it
Kalshi KXCPIYOY-26AUG, headline CPI YoY, settles today 2026-09-11 12:29Z (08:29 ET). Fetched ~06:23 ET:
| Strike | Last | Prev | yes_bid/ask | OI |
| --- | --- | --- | --- | --- |
| Above 3.2% | 0.92 | 0.97 | 0.87/0.92 | 66.3k |
| Above 3.3% | 0.61 | 0.67 | 0.58/0.61 | 145.7k |
| Above 3.4% | 0.19 | 0.12 | 0.18/0.19 | 160.8k |
| Above 3.5% | 0.05 | 0.06 | 0.04/0.05 | 94.1k |
| Above 3.6% | 0.02 | 0.01 | 0.01/0.02 | 43.6k |
Implied distribution for the August print: **3.3% -> 31%, 3.4% -> 42%, 3.5% -> 14%, 3.6%+ -> 5%, 3.2% or below -> 8%.** Centred on the 3.4% Street consensus, with the tail shifting UP overnight (Above 3.4% went 0.12 -> 0.19 while Above 3.3% went 0.67 -> 0.61) — the oil move is being priced into the print.
## [06:23 ET] REJECTED — KXCPIYOY-26AUG (all strikes) — I have no independent CPI forecast to set against this, and the market's distribution already sits on consensus. `config/universe.md` requires an explicit probability disagreement with a stated reason for the gap; I do not have one, and the contract stops trading at 08:29 ET, roughly two hours after this report publishes. Recording the ladder as context for the reader is worth more than a coin-flip position.

## [06:26 ET] VENUE CHECK + LIQUIDITY
- **FRO** — Frontline plc, **NYSE-listed ordinary shares** (dual-listed NYSE and Oslo Bors), market cap $10.77B on 222.62M shares, SEC reporting (files 20-F, CIK 913290). It is NYSE-listed rather than OTC or an unsponsored foreign ordinary, so it satisfies `config/universe.md`. **Caveat recorded honestly: I could not find a source explicitly confirming FRO is offered in the Robinhood app.** No search result addressed it. Synthesis should treat this as "listed on an eligible US exchange, Robinhood availability not directly verified".
- Fleet composition per the FY2025 20-F: 80 tankers — **41 VLCCs**, 21 Suezmax, 18 LR2/Aframax — source: https://www.sec.gov/Archives/edgar/data/913290/000162828026021774/fro-20251231.htm . VLCCs are the exact class that lifts Gulf crude, which is why FRO and not a product-tanker name.
- Pre-market depth at ~06:26 ET (indicative, market is closed — these are NOT regular-session spreads): FRO 47.95/48.05 (0.21%), AAL 12.97/13.02 (0.39%), DVN 49.15/49.77 (1.25%), DG 122.75/132.88 (**7.93%**). The DG figure is a pre-market quote artifact, not a liquidity problem — DG runs $288M average daily dollar volume. Recorded so nobody reads it as one.
- All four captured equities clear the universe floors: DVN $524M ADV, FRO $111M, AAL $728M, DG $288M, CCJ $276M. BCC is the thinnest at $23M ADV and that is an exit, not an entry.

## [06:26 ET] LEVELS — 250-day check on the two breakout longs, and what it changed
Both targets sit above anything traded in a year. That is structurally unavoidable for a name at a 52-week high, but the degree matters and it differs sharply between the two:
- **DVN**: 250d range 31.47-52.71, sma200 43.72. Closed 50.02 on 09-10 = **highest close of the past year**. Target 55.50 is +5.3% above the 250d intraday high. Price is **14% above the 200-day** — an ordinary trend extension. DVN kept at conviction 4.
- **FRO**: 250d range 20.47-48.72, sma200 33.93. Closed 48.40 = 52-week high, **+136% off the 250-day low**, and **43% above the 200-day**. Target 57.50 is +18% above anything traded in a year.
**Action taken:** FRO re-captured at **conviction 3, size cut 2% -> 1.5%**, and the `counter_argument_answered` evidence entry REMOVED. The strongest case against FRO is the extension, and I could not answer it with evidence — so claiming that evidence kind would have been inflating the score. Conviction is a count of confirmations actually made; two kinds is what FRO has.
DVN re-captured with the 250d facts stated in `key_risk` and the 14%-vs-43% contrast added to its counter-argument.

## [06:26 ET] COVERAGE GAPS — what this run did not reach
- **No small or micro caps.** The skill asks for them deliberately and I found none. Every small-cap idea the day's themes pointed at was a fourth oil bet and the correlation cap was already reached. Noting the gap rather than padding with one I had not researched.
- **No intraday idea.** CPI at 08:30 ET is a genuine intraday catalyst but specifying a direction before the print is a coin flip, and the honest conditional version ("long if soft, short if hot") is two ideas pretending to be one. Nothing intraday cleared the bar.
- **No crypto and no futures idea.** BTC 77,104 is drifting with equities rather than bidding on the inflation shock, so there was no crypto thesis. Every futures expression available (/MCL crude, /MGC gold) would have been a fourth oil bet.
- **No short-interest and no options-implied check on any idea** — both feeds were down (see the failed-sources block).
- **No VIX, index level, DXY or crude futures quote** — yahoo 429 throughout. All crude references are USO or sourced Brent prints.
- Did not resolve why INSW (-2.37%) diverged from the other tankers.
- Did not re-underwrite the GLD or SVRA theses; both held unchanged on that basis rather than on a fresh view.

## [06:28 ET] LONG_TERM lane, second attempt — pharma worked and REJECTED
Looked for the classic "quality business de-rated on a fixable problem" in large-cap pharma, which is the one sector that is neither an oil bet nor rate-sensitive. **The de-rating has already happened and reversed.** 250-day positions:
- MRK 144.71 — range 77.58-156.92, **+86.5% off the low**, -7.78% off the high, **21% above its sma200 of 119.18**
- BMY 63.75 — range 42.52-68.64, +49.9% off the low, -7.12% off the high, sma200 58.41
- ABBV 255.00 — range 190.75-267.47, +33.7% off the low, -4.66% off the high, sma200 228.63
- PFE 27.65 — range 23.58-29.21, +17.3% off the low, -5.34% off the high, sma200 26.21 (least extended of the four)
The Merck Keytruda-cliff thesis is real and well-documented — >50% of sales exposed at 2028/29 expiry, ~$25B of oncology revenue at risk, subcutaneous Keytruda QLEX extending protection to 2030+ with a 30-40% conversion target by 2028, ~$70B of claimed mid-2030s opportunity — but the commentary citing 12x forward P/E and a "decade-low valuation" predates a near-doubling off the low. Even the bullish coverage now reads "the playbook is working, but valuation has caught up" — source: https://seekingalpha.com/article/4919574-merck-post-keytruda-playbook-is-working-but-valuation-has-caught-up
**REJECTED — MRK / BMY / ABBV / PFE — there is no de-rating left to buy. A stock 86% off its low and 21% above its 200-day is not a cheap quality compounder, and I did not do the valuation work that would justify buying it as an expensive one.** The long-term lane therefore carries one idea today (DG), not two, and that is the honest count.

## [06:27 ET] PENDING ENTRIES — status of the rest of the awaiting-entry book (prices are 2026-09-10 closes)
Not re-pitched unless stated. Recording status so synthesis can report them honestly rather than silently carrying them.
- `XLE` BUY @63.90 (pub 08-15) — XLE 64.93, **1.6% above the entry, still live**; it traded 63.96 on 08-31 and 64.06 on 09-04 without filling. Level unchanged and still reasonable. **Not re-pitched: it would be a fourth oil-driven idea and the correlation cap is already reached.**
- `LCII` BUY @94.00 (pub 08-18) — LCII 93.40 (-2.75%), i.e. the entry is **about to fill**. **Recommend withdrawing it.** LCII supplies RV and marine OEMs; that is the same rate-and-fuel-squeezed end market as the BCC position I am closing today, and filling into it now would open a new position into a thesis the tape is actively falsifying. Synthesis should drop this, not fill it.
- `CEG` BUY @272.00 (pub 08-21) — CEG 285.97 (-2.70%), 5.1% above the entry, never filled and ran away.
- `VST` BUY @128.00 (pub 08-24) — VST 147.05 (-2.68%), **14.9% above the entry**, long gone. Stale level.
- `EEM` BUY @65.60 (pub 08-21) — EEM 67.00 (-2.16%), 2.1% above the entry, never filled.
- `PFE` BUY @25.80 (pub 08-18) — PFE 27.65 (-0.47%), 7.2% above the entry. Stale, and see the pharma rejection above: there is no de-rating left to buy.
- `KXFEDDECISION-26SEP-H0` YES @47 (pub 09-03) — now 39c and moving against us. See the rejection block; not averaged down.
- `KXFEDDECISION-26SEP-H25` YES @32 (pub 08-22) — now **61c**, up 29 points. This one is deep in the money on a mark-to-market basis and resolves 2026-09-16. Worth synthesis noting as the one prior event-contract call that is working.
- `KXFEDDECISION-26OCT-H25` YES @28 (pub 09-02) — now 30c, roughly flat.
- `DINO`, `IYR`, `GLD` SELL, `BTC` SELL, `/MBTU6` SHORT — addressed in their own blocks above.
Note the pattern worth flagging to synthesis: of the 15 awaiting-entry ideas, the long entries that never filled (CEG +5%, VST +15%, EEM +2%, PFE +7%, DINO +8%) all ran away upward, while the ones that did fill were the ones falling. That is the pullback-entry selection effect `config/strategy.md` describes, visible in this book right now.

## [06:27 ET] CORRELATION AUDIT — final, across everything captured
| Driver | Ideas | Count |
| --- | --- | --- |
| Oil stays high | DVN (long producer), FRO (long tanker), AAL (short fuel consumer) | **3 — at the cap, not over** |
| Rates stay high | SPY short (multiple compression), BCC sell (housing demand) | 2 |
| Uranium contract repricing | CCJ | 1 |
| Consumer trade-down | DG | 1 |
No fourth oil idea was captured, and XLE was deliberately left un-re-pitched for that reason. DG is a partial offset: management themselves named high fuel as a headwind, so it loses some of what DVN/FRO/AAL win.

## [06:30 ET] Defense-tech de-rating worked and REJECTED — AVAV / KTOS
The screen that found them: both are down ~65% from their 250-day highs while a drone war is being fought in the Gulf, which is the shape of a real dislocation.
- KTOS 46.98 (+0.51%), 250d range 43.09-134.00, **-64.94% off high**, +9.03% off low, sma200 71.28, atr14 4.90%, cap $8.82B
- AVAV 147.07 (**+4.45%** on a red tape), 250d range 135.20-417.86, **-64.81% off high**, +8.78% off low, sma200 210.47, atr14 5.28%, cap $7.47B. It filed a 10-Q on **2026-09-10** and an 8-K on 09-09, so the green day was a filing reaction.
Analyst trend is *improving* on AVAV (strong_buy 8 -> 9 -> 10 across June-September, 14 buy, 4 hold, 0 sell), which is exactly the kind of divergence worth chasing.
**Why I am not buying either:**
- **AVAV has a specific, unresolved cause and it includes accounting.** It lost the SCAR Space Force contract worth ~$1.4B, cut FY2026 revenue guidance to $1.85-1.95B and non-GAAP EPS to $2.75-3.10 against Street $3.28-3.31, missed badly on revenue ($408.05M vs $487.94M expected), and is carrying **accounting issues and ongoing litigation**. I cannot underwrite an accounting question in the time available, and a 65% decline with one outstanding is not a discount, it is an open question. — source: https://finance.yahoo.com/markets/stocks/articles/aerovironment-avav-stock-sees-fair-value-cut-as-analysts-weigh-contracts-and-execution-risks
- **KTOS is cleaner but on the wrong side of today's driver.** Bernstein's Douglas Harned attributes the sector decline to capital rotation rather than fundamental deterioration — defense valuations were near historical highs when the Iran conflict began, and **higher discount rates compress the long-duration contract cash flows defense investors were underwriting at premium multiples**. That is the same 4.95% 10-year that is behind my SPY short and the BCC close. Buying KTOS today means fighting the exact force this report says is still strengthening. — source: https://finance.yahoo.com/markets/stocks/articles/drone-stocks-down-defense-backlogs-115500190.html
**REJECTED — AVAV (accounting and litigation unresolved) and KTOS (right thesis, wrong day — it needs rates to stop rising and they are not).** Worth revisiting KTOS if and when the rate impulse breaks.

## [06:29 ET] CONVICTION AUDIT — scores reconciled against the evidence count
`config/strategy.md` maps distinct evidence kinds to the score mechanically (1 kind = 2, 2 = 3, 3 = 4, 4+ = 5). Checked every captured candidate:
| Symbol | Distinct kinds | Score |
| --- | --- | --- |
| DVN | 3 (technical_level, positioning, counter_argument_answered) | 4 |
| DG | 3 (primary_document, valuation_anchor, technical_level) | 4 |
| SPY | 3 (dated_catalyst, technical_level, positioning) | 4 — **corrected up from 3** |
| FRO | 2 (technical_level, positioning) | 3 |
| AAL | 2 (technical_level, positioning) | 3 |
| CCJ | 2 (positioning, technical_level) | 3 |
| BCC | 2 (technical_level, positioning) | 3 |
SPY had been captured at 3 against three genuine kinds. Deliberately under-stating distorts the by-conviction table exactly as inflating does, so it is corrected rather than left "safely low". FRO was corrected the other way earlier (4 -> 3) when its third evidence kind turned out not to hold.
Note the shape of this: **no 5s and no 2s today.** Nothing had four independent confirmations, and nothing thin enough to be a 2 cleared the other floors.

## [06:30 ET] RESEARCH COMPLETE
- **candidates: 7 distinct ideas** (10 lines in candidates.jsonl — DVN, FRO and SPY were each re-captured once to correct levels or conviction; synthesis takes the last entry per symbol)
  - New: **DVN** buy swing conv4 (R:R 2.19), **FRO** buy swing conv3 (R:R 2.07), **AAL** sell_short swing conv3 (R:R 2.92, wait for a bounce to 13.30), **DG** buy **long_term** conv4 (R:R 2.67 at the 115 accumulation level)
  - Position updates: **CCJ** hold + add a stop at 85.00 (conv3), **SPY** hold short unchanged (conv4), **BCC** close (conv3)
- **Every idea passes its floors, checked arithmetically at 06:25 ET**: stop distance in ATRs — DVN 2.32, FRO 2.74, AAL 3.02, CCJ 2.17, SPY 1.96 (ETF floor 1.8); R:R — all at or above the 2.0 swing / 2.5 long_term floor; win_probability above the `1/(1+R:R)` baseline on all six with a stop, by 7-17 points, none over the 20-point "large claim" line.
- **The report is concentrated and says so.** Three of seven ideas are one bet that oil stays high (DVN long producer, FRO long tanker, AAL short fuel consumer) — exactly at the correlation cap, not over it. A negotiated Gulf de-escalation loses on all three at once. DG partially offsets, since its management named high fuel as their own headwind.
- **Horizon skew, unforced:** six swing, one long_term, zero intraday. No intraday setup cleared the bar — CPI at 08:30 ET is a real catalyst but picking a direction before the print is a coin flip. No quota was filled to make the mix look balanced.
- **Coverage gaps:** no small or micro caps (every candidate the day's themes pointed at was a fourth oil bet); no crypto idea (BTC 77,104 is drifting with equities, not bidding on the inflation shock); no futures idea (/MCL and /MGC would both be oil bets); no re-underwriting of GLD or SVRA, both held unchanged on that basis; INSW's -2.37% divergence from the other tankers unexplained; the DG net-sales discrepancy (+0.2% in the transcript vs +5.2% in a secondary source) recorded but unresolved.
- **Sources that failed, all material:**
  - yahoo chart API 429 throughout — **no VIX, no index level, no DXY, no WTI/Brent futures quote, no /ES or /MES quote all run.** Every crude reference in these notes is USO or a sourced Brent print, never a futures price I did not fetch.
  - `market_data.py short` (nasdaq) returned `ok: false` with null fields for every symbol — **no short-interest or days-to-cover check was possible on any idea**, which matters most for the AAL short and is stated in its `key_risk`.
  - `market_data.py implied` (yahoo options) returned HTTP 401 — **no options-implied-move check on any idea.**
  - finnhub index quotes require a CFD subscription; stooq 404s on index symbols; CoinGecko failed inside `macro` but succeeded via the `crypto` subcommand.
  - rbnenergy.com 403s to WebFetch (figure taken from the search abstract and corroborated against a second source).
- **Prices:** every level in these notes and in candidates.jsonl is a 2026-09-10 regular-session close, fetched from finnhub or nasdaq at 06:00-06:30 ET on 2026-09-11 with the US market closed. That is the freshest honest equity price at this hour — a closed market, not stale data. Kalshi contract prices were fetched live at ~06:10 and ~06:23 ET.
- **Rejections logged with reasons (14):** LEN/ITB short, LEN long, OXY, HAL/SLB/OIH, LNG (Cheniere), EQT/AR/RRC, VLO/MPC/DINO/PSX/PBF/DK, LMT, GIS/CAG, KR, MRK/BMY/ABBV/PFE, AVAV, KTOS, KXFEDDECISION-26SEP-H0, KXCPIYOY-26AUG.
- **Withdrawal recommended:** `LCII` BUY @94.00 is about to fill at 93.40 into the same rate-and-fuel-squeezed end market as the BCC position being closed. Synthesis should drop it rather than let it fill.
