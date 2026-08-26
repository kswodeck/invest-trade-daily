# Research log — 2026-08-26

## [06:38 ET] MACRO — rates and policy
- FRED 2026-08-24: US10Y **4.70%**, US2Y **4.24%**, effective fed funds **3.63%**, 10y-2y curve **+0.47** (2026-08-25). Unemployment 4.1% (Jul), CPI index 332.813 (Jul).
- Notable: 2y sits **~61bp ABOVE** effective fed funds. The market is pricing net *tightening*, not cuts, over the next two years. That is the single most important frame today — it argues against long-duration and against rate-cut-dependent theses (KRE, TLT, small caps).
- TLT $83.47, +1.10% on 2026-08-25 (stooq, prev close 82.56). Source: FRED via scripts/market_data.py macro
- **DATA GAP:** Yahoo Finance returning HTTP 429 across the board — SPX, NDX, DJI, RUT, VIX, ES, NQ, DXY, gold, WTI all FAILED. CoinGecko crypto prices also FAILED this call. Finnhub blocks CFD indices. Will retry / route around.

## [06:41 ET] CALENDAR — earnings inside 10 sessions (finnhub)
- **TODAY 2026-08-26 AMC: NVDA** — rev est $93.63B, EPS est $2.13. The dominant event of the week; sets the tone for all AI/semi/power names.
- Also today AMC: CRM ($11.4B), CRWD, HPQ, SNPS, VEEV, OKTA, NTNX, URBN. BMO: BBWI, DY, SJM, DCI.
- **2026-08-27 BMO: DG** — EPS est $2.06, rev $11.53B. *We have an unfilled awaiting-entry at $119 from 2026-08-21.* Live dated catalyst.
- 2026-08-27 AMC: MRVL, ULTA, WDAY, ADSK, AFRM, GAP, ESTC, RBRK, S, IREN. BMO: BBY, BILI, HRL, CSIQ, HQY.
- 2026-08-31: AEO, ASO, **FRO** (Frontline, tankers — relevant to our DHT position), SAIC.
- 2026-09-01: PANW, MDB, DLTR, M, MDT, CRDO, GTLB, NIO.
- 2026-09-02: **AVGO** ($29.9B), AGX, plus small caps.
- source: scripts/market_data.py earnings --days 10 (finnhub)

## [06:48 ET] PRICES — all quotes are 2026-08-25 16:00 ET closes (market closed, pre-session at 06:4x ET). source: finnhub
NVDA 213.05 (+2.19%) | DG 122.58 (-2.19%) | SPY 765.91 (+0.32%) | TLT 83.47 (+1.10%)
KRE 74.33 (-0.58%) | XLE 62.06 (-1.66%) | CCJ 106.96 (+4.59%) | NKE 39.48 (-3.12%)
PFE 28.57 (+2.15%) | DHT 19.17 (-2.79%) | HD 337.88 (+0.13%) | BCC 81.04 (-1.46%)
TJX 139.48 (-0.87%) | LCII 104.78 (+0.26%)
Crypto 06:44 ET (CoinGecko): BTC 78,638 (-0.76% 24h) | ETH 2,457.79 (-0.78%) | SOL 96.72 (-2.65%)

## [06:47 ET] POSITION UPDATE — TJX — opened 2026-08-19 @150.85, now 139.48, -7.5%
- decision: **CLOSE at the open**. Stop was 145.50; closed 139.48, ~4% through it. Fresh 150-day low (range low 139.17, only 0.22% below).
- 20d SMA 152.87 / 50d SMA 154.88, both far overhead. No timeframe confirms the thesis.
- captured via add_candidate.py as a `sell`.

## [06:48 ET] POSITION UPDATE — /MBTU6 short — opened 2026-08-18/19 @64,100 / 64,340, stop 66,600
- BTC spot **78,638**. The short is ~22% offside and the stop is 12,000 points behind price.
- Micro BTC = 0.1 BTC, so ~$1,450 loss per contract against a sizing that assumed ~$250 risk.
- **This is the third consecutive report to flag it** (08-24 and 08-25 both said cover). decision: **COVER AT MARKET**, highest urgency.
- captured via add_candidate.py as a `long` (buy-to-close).

## [06:48 ET] DATA GAP — Kalshi event contracts returning count=0 for "Fed", "Bitcoin", "CPI"
- The events endpoint is up (ok:true) but returning empty market lists. Event-contract lane may be unavailable today. Will retry with other terms.

## [06:52 ET] DATA GAP — event contracts effectively unavailable today
- Kalshi endpoint returns ok:true but count=0 for "Fed", "CPI", "Bitcoin", "recession", "inflation", "Fed Funds", "interest rate", "S&P", "GDP".
- An empty-string query returns 40 markets, all `KXMVECROSSCATEGORY` sports parlay shards with null bids/asks/volume.
- Conclusion: the financial event-contract series are not reachable through this endpoint today. **No event-contract candidates can be honestly priced**, so none will be captured. Prior open position KXFEDDECISION-26SEP-H25 cannot be marked to market.

## [06:53 ET] POSITION UPDATE — KRE — opened 2026-08-15 @76.80, now 74.33, -3.2%
- decision: **CLOSE at the open**. Stop 74.20 is 13 cents away = 0.12 ATR on a 1.04 ATR instrument.
- Macro premise inverted: 2y (4.24%) is ~61bp ABOVE effective fed funds (3.63%) — curve pricing tightening, not the cuts a regional-bank re-rating needs.
- Third KRE long to fail (08-17 and 08-18 entries both stopped 08-19). Pattern, not luck.
- captured via add_candidate.py as a `sell`.

## [06:53 ET] POSITION UPDATES — HOLD, no change (levels unchanged, thesis intact)
- `XLE` 62.06 — three longs @60.5/60.8, stops 57.8-59.2. +2-3%. Above 20d (60.75) and 50d (57.72). HOLD.
- `CCJ` 106.96 (+4.59% on 08-25) — longs @95 and @88, target 135. +12.6%/+21.5%. Broke decisively above 20d (95.89) and 50d (96.33). Best-performing open position. HOLD, long_term, no stop by design.
- `PFE` 28.57 (+2.15%) — long @25.80, target 38. +10.7%, and only 0.61% off its 150-day high. HOLD.
- `LCII` 104.78 — long @94, target 138. +11.5%. HOLD.
- `DHT` 19.17 — long @18.80, stop 17.60. +2.0%, above 20d (18.90) and 50d (18.36). FRO reports 2026-08-31 BMO, a read-through for tanker rates. HOLD.
- `HD` 337.88 — longs @340.00 and @337.49, stop 328. Flat. ATR 8.52, so stop is 1.16 ATR away — tight but defensible. HOLD.
- `BCC` 81.04 — long @81.00, stop 76.00. Flat. HOLD.
- `TLT` 83.47 (+1.10%) — long @82.60, target 86.20, stop 80.95. +1.1%. FLAGGED: the 2y-above-fed-funds picture is a headwind to a long-duration position; holding on the 10y at 4.70% being restrictive, but this is the open position I have least confidence in.
- `BTC` spot entries dated 08-16/08-17 are `sell` (exit/avoid) markers, not positions — nothing to close.

## [07:00 ET] CALENDAR — today is a two-event day
- **08:30 ET TODAY: Q2 GDP + PCE inflation.** PCE is the Fed's preferred gauge. Roughly 90 minutes from now. source: https://tradingeconomics.com/united-states/calendar
- **After the close TODAY: NVDA fiscal-Q2-2027.** Street ~$2.09 EPS on ~$92.2B revenue (+97% y/y); finnhub carries $2.13 / $93.6B. 58 of 61 analysts Buy/Strong Buy — consensus is crowded to one side.
- NVDA gap history: 24 gaps >=5% in 5 years, 14 up / 10 down, gap-ups avg +8.9%. source: https://finance.yahoo.com/markets/stocks/articles/nvidia-stock-soar-aug-26-084401610.html
- Futures flat pre-open: Dow +0.09%, S&P -0.05%, Nasdaq-100 -0.2%, Russell 2000 -0.05%. source: https://stockmarketwatch.com/live/stock-market-today

## [07:00 ET] INSIDERS — 6-month open-market purchases (finnhub, Form 4 code P)
- **PFE: 3 buys, 3 distinct buyers, $2.96M gross, $2.83M net.** CEO **Albert Bourla bought 38,000 sh @ $26.34 on 2026-08-12**; **Mortimer Buckley** (ex-Vanguard CEO, PFE director) 37,632 sh @ $25.52 on 2026-08-05. Both are buying two weeks ago, below today's 28.57. Strong confirmation of the existing PFE long.
- **NKE: 5 buys, 4 distinct buyers, $3.73M gross, $2.53M net** vs only $1.20M of sales. Elliott Hill (CEO) 2x 23,660 sh @ ~$42.27 on 2026-04-13 — above the current 39.48, so they are underwater too, but it is real conviction money.
- DG: zero open-market buys in 6 months. Neutral, not negative.
- CCJ: zero open-market buys in 6 months. Neutral, not negative.

## [07:00 ET] DG — earnings 2026-08-27 09:00 ET call, release BMO
- Consensus rev $11.17B (+4.2% y/y), EPS $2.00 (+7.5% y/y). Finnhub carries $2.06 / $11.53B — sources disagree; treat $2.00-2.06 as the range.
- Trailing 4-quarter avg earnings surprise **+21%**; last quarter beat by 5.8%.
- FY2026 guidance $7.20-$7.45 EPS. At 122.58 that is **16.5-17.0x** current-year earnings.
- Analysts expect management to REAFFIRM rather than raise, on higher fuel costs.
- DG closed -2.19% on 2026-08-25 into the print. 22.5% off the 150-day high of 158.23, 23.1% off the low.
- sources: https://finance.yahoo.com/markets/stocks/articles/whats-dollar-generals-probability-earnings-155700505.html , https://www.stocktitan.net/news/DG/dollar-general-corporation-announces-webcast-of-its-second-quarter-bipz3jdcgxs4.html

## [07:10 ET] NEWS — 2026-08-25 session, the day was about retail, not tech
- **DKS -30.7% to 124.31 — worst day in company history.** Adj EPS $3.53 vs $3.78 est; revenue $5.59B vs $5.65B. FY26 adj EPS guided to **$11.00-$12.00 vs $14.20 consensus** (-19% at the midpoint). Core DICK'S comps **+4.9%**; acquired Foot Locker proforma comps **-3.6%** with a **$31.9M operating loss**. Exec chairman Ed Stack: promotional backdrop in athletic footwear/apparel "deteriorated as the quarter advanced".
  - Closed at 124.31 = the exact low of the day (day range 124.00-146.48). No dip buyer at any point. ATR 10.91 (8.78%). 49.1% off the 150-day high.
  - Insiders: **0 open-market buys, 9 sells, $47.1M** over 6 months. No confirming purchase.
  - sources: https://seekingalpha.com/news/4636761-dicks-sporting-goods-plunges-31-after-earnings-miss , https://www.sec.gov/Archives/edgar/data/1089063/000108906326000033/dks-20260824.htm
- **Read-through hit the whole athletic complex:** ASO -5.80% to 43.475 (0.5% off its 150-day low), BURL -4.65% to 315.27, **NKE -3.12% to 39.48**.
- Gainers: **AMD +4.91% to 479.18** on a Raymond James upgrade to Strong Buy, PT $641. **MRVL +4.84% to 240.38** (reports 08-27 AMC). SFT +5.7%, DT +3%.
- source: https://www.cnbc.com/2026/08/25/stocks-making-the-biggest-moves-midday-dks-mrvl-amd-kura.html

## [07:11 ET] POSITION UPDATE — NKE — longs @40.00 (08-17) and @38.00 (08-18), now 39.48, target 65/62
- **New adverse information.** DKS is Nike's largest US wholesale partner and it just told the market the athletic footwear/apparel category is increasingly promotional and got *worse* through the quarter. That is a direct margin warning for NKE, and NKE traded -3.12% on it.
- Offsetting: NKE insider cluster is real — 5 open-market buys, 4 distinct buyers, $3.73M vs $1.20M of sales; CEO Elliott Hill bought 47,320 shares around $42.27 on 2026-04-13, above today's price.
- NKE is 1.6% off its 150-day low (38.86) and 42.4% off the high. 20d 41.24 / 50d 42.28 both overhead.
- decision: **HOLD, but the invalidation is now explicitly named** — this is a long_term turnaround with no stop by design, and a second consecutive quarter of category-wide promotional pressure showing up in NKE's own gross margin is the condition that kills it, not the price. Not re-pitched as a new idea; no new capital.

## [07:11 ET] REJECTED — ASO — 0.5% off 150-day low on the same DKS read-through, reports 2026-08-31; no edge over DKS itself and same driver — correlation cap
## [07:11 ET] REJECTED — AMD — +4.9% on a sell-side upgrade with NVDA reporting tonight; buying a semi at 479 hours before someone else's print is a leveraged bet on a coin flip, not a thesis
## [07:11 ET] REJECTED — BURL — -4.65%, no dated catalyst inside the horizon and the same promotional-retail driver already expressed via DG and DKS

## [07:16 ET] LONG-TERM — uranium/nuclear evidence supporting the existing CCJ hold
- Uranium spot **US$85-86/lb** in Aug 2026. Bank of America forecasts **US$130/lb average in 2027** (+52%).
- Cameco 2026 plan: mine **19.5-21.5 Mlb**, deliver **29-32 Mlb** — bridging the ~10 Mlb gap with inventory and purchased pounds. That is a producer short its own book.
- US utilities have contracted maximum deliveries covering only **48% of anticipated requirements through 2035**.
- Westinghouse (Cameco 49%-owned) pursuing up to **91 potential AP1000 projects**. Meta signed for up to 7.8 GW of nuclear in Q1 2026; Microsoft >800 MW for datacenters.
- sources: https://theoregongroup.com/commodities/uranium/why-bank-of-america-still-sees-130-lb-uranium-cameco-is-the-warning/ , https://www.cruxinvestor.com/posts/ai-power-demand-utility-undercontracting-tighten-uranium-supply-as-contract-prices-reach-90-per-pound , https://www.cameco.com/invest/markets/supply-demand
- **decision: HOLD CCJ, target 135 unchanged, no new capital.** CCJ has been recommended 3x in 10 days and is +12.6% from the 95 entry at 106.96; adding here is chasing. NOT captured as a candidate — no action changes.

## [07:16 ET] POSITION UPDATE — PFE — long @25.80, now 28.57, +10.7%, target 38
- New confirming evidence: CEO Albert Bourla bought 38,000 sh @ $26.34 (2026-08-12) and director Mortimer Buckley 37,632 sh @ $25.52 (2026-08-05) — both open-market, both within the last three weeks.
- decision: **HOLD, no change to levels, no new capital.** 0.61% off the 150-day high, so this is not an add price. Not captured — nothing changes.

## [07:17 ET] REJECTED — /MES intraday around the 08:30 GDP+PCE print
- The event is real and dated but I have no directional edge on it. The 2y at 4.24% sits 61bp above effective fed funds, so tightening is already priced — which tells you positioning, not which way the print lands. Trading an index future into a print on no view is a coin flip with leverage. `config/strategy.md` calls this out explicitly: a general lean is not an intraday catalyst.

## [06:45 ET] TIMESTAMP CORRECTION
Entries above are labelled 06:37-07:17 but real wall clock at this point is **06:45 ET**. The
early timestamps were my own estimate of elapsed time, not `date` output, and they ran ahead of
reality. Everything above is accurate as to content and ordering; only the clock labels are
inflated. Entries below this line are stamped from `date`.

## [06:45 ET] MACRO — energy is a headwind to the open XLE longs
- WTI opened **$84.95** on 2026-08-25 and was **$82.28 (-3.15%)** by 08:18 ET. Crude fell >3% below $82 on Monday after a 2.4% loss the session before, on signs of easing US-Iran tension.
- Forecasts point DOWN from here: EIA has Brent ~$85 in Q3 2026; **J.P. Morgan has Brent $86 Q3 → $80 Q4 → $78 at year end**.
- **OPEC+ implements a final 188,000 bpd quota increase in September**, completing the rollback of voluntary cuts. Supply is being added into a softening price.
- Offsetting: Strait of Hormuz transits remain severely constrained, with ~0.6 mb/d of disruption expected to persist through end-2027 and regional production not back to pre-conflict averages until early 2027.
- sources: https://fortune.com/article/price-of-oil-08-25-2026/ , https://www.eia.gov/outlooks/steo/report/global_oil.php , https://www.jpmorgan.com/insights/global-research/commodities/oil-prices
- **Read-through to open positions:** XLE (three longs @60.5-60.8, now 62.06, -1.66% yesterday) is exposed to a forecast path that declines all the way to year-end. DHT/tankers benefit from the opposite leg — Hormuz disruption lengthens voyages and tightens tonne-miles even as crude falls.

## [06:50 ET] TANKERS — the strongest new setup found today
- **VLCC MEG-China assessed $14.42/mt, +28% y/y** (Platts). Crude tanker rates hit a six-year high; tonne-mile demand at record levels.
- **Hormuz crisis cut VLCC volumes 36% but lengthened voyages** — fewer cargoes, far more tonne-miles. More Atlantic-basin crude loading for Asia.
- BIMCO: balanced crude-tanker supply/demand for 2026, demand growth forecast lifted 0.5%; the growing oil surplus itself drives more cargo.
- Three tailwinds stack: (1) falling crude ($82 WTI) cuts bunker fuel, the largest tanker opex line; (2) OPEC+ adds 188k bpd in September, which is more cargo; (3) Hormuz disruption of ~0.6 mb/d persists through end-2027, lengthening routes.
- sources: https://www.lloydslist.com/LL1157100/Hormuz-crisis-slashes-VLCC-volumes-by-36-but-voyages-are-longer , https://oilprice.com/Latest-Energy-News/World-News/Oil-Tanker-Rates-Surge-to-Six-Year-High.html , https://www.spglobal.com/energy/en/news-research/latest-news/refined-products/082825-bimco-forecasts-steady-freight-rates-for-crude-tankers-product-tankers-to-falter

## [06:52 ET] VENUE / DATE CHECK — FRO earnings date, finnhub was WRONG
- finnhub `earnings` listed FRO on **2026-08-31**. The company's own invitation says: *"Frontline plc.'s preliminary second quarter 2026 results will be released on **Friday August 28, 2026**, and a webcast and conference call will be held at 3:00 p.m. CEST (9:00 a.m. U.S. Eastern Time)."*
- **Use 2026-08-28, not 08-31.** source: https://www.frontlineplc.cy/fro-invitation-to-q2-2026-results-conference-call-and-webcast/
- FRO is NYSE-listed common stock, so Robinhood Stocks is the correct venue.

## [06:53 ET] FRO — Q2 is already in the bank (primary source: company Q1 2026 release)
- Q1 2026: profit **$559.1M / $2.51 per share**; **adjusted profit $344.9M / $1.55 per share**, which the company called "the strongest since the fourth quarter of 2004". Declared **$1.55/sh cash dividend**.
- Q1 release's forward booking table for the quarter that has since ended:
  - **VLCC $181,700/day, 82% covered**
  - **Suezmax $131,300/day, 79% covered**
  - **LR2/Aframax $125,000/day, 68% covered**
- Company caveat, quoted: *"We expect the spot TCEs for the full second quarter of 2026 to be lower than the spot TCEs currently contracted, due to the impact of ballast days during the second quarter of 2026."*
- Outlook: *"heightened global focus on energy security, together with more diversified oil sourcing by key importers in Asia, will benefit the tanker market for years to come."*
- Street consensus for the print: EPS $2.57 on $750M revenue (finnhub) vs $1.55 adjusted in Q1 — the Street has already modelled the bookings, so a beat is not the edge. **The dividend declaration is.**
- Levels: 43.46, ATR 1.47 (3.38%), 20d 40.83, 50d 39.19, 150d high 45.17 (-3.79%), low 25.09 (+73.2%).
- Insiders: 0 open-market buys, 0 sells in 6 months. Neutral.
- sources: https://www.frontlineplc.cy/fro-first-quarter-2026-results/ , https://seekingalpha.com/article/4921417-frontline-stock-q2-maintaining-strong-buy

## [06:53 ET] POSITION UPDATE — DHT — long @18.80, now 19.17, stop 17.60, +2.0%
- Thesis strongly confirmed by the tanker data above. HOLD, levels unchanged.
- **Honest negative:** DHT insiders show **0 open-market buys and 4 sells totalling $8.64M** over six months (Form 4s filed 2026-08-24 for 2026-08-21). Sales are weak evidence alone, but there is no confirming purchase.
- DHT has been recommended 4x in 10 days — that is the anchoring warning the prior context flags. **Not re-pitched today**; the tanker view is expressed instead through FRO, which has a dated catalyst DHT does not.

## [06:50 ET] REJECTED — AGX (Argan) — expensive and insiders are heavy sellers
- 450.46 (-3.95%). Backlog $2.9B, ~2x the prior $1.4B; FY26 rev $944.6M (+8%), EBITDA $162.8M (+43%), GM 20.5% vs 16.1%. Four US gas projects >4.1 GW under construction. Genuinely good business.
- But **insiders: 0 open-market buys, 26 sells totalling $126.6M** over six months. And on ~$163M of EBITDA the equity is priced in the multiple tens of times EBITDA. A great story already fully paid for. No entry price that clears the bar.
- source: https://finance.yahoo.com/markets/stocks/articles/argans-2-9b-backlog-spark-155000466.html
## [06:50 ET] REJECTED — AVAV — 0 insider buys / 10 sells; earnings 2026-09-09 is outside a clean setup and no differentiated view
## [06:50 ET] REJECTED — IREN — +6.03% to 42.21 into a 08-27 AMC print; a bitcoin-miner-turned-AI-datacenter is two coin flips stacked (BTC and NVDA) with no independent thesis
## [06:50 ET] REJECTED — CRDO — 226.51, reports 09-01 AMC; pure NVDA-derivative beta, would breach the correlation cap alongside the NVDA idea

## [06:51 ET] GOLD — structural bid is real, but the price has run
- Gold ~**$4,400/oz** after CPI week, **+10% in August** from near $4,000 — best month since January.
- **Central banks bought a quarterly record 288.9 tonnes in Q2 even as prices fell.** Official-sector demand is price-insensitive in a way private demand is not, and is the most-cited structural driver of the 2022-2026 rally.
- Bank forecasts: HSBC year-end 2026 **$4,750**; Deutsche Bank 2027 **$5,150**; J.P. Morgan **$6,000 by end-2026** and $6,300 possible in 2027. Range of year-end calls spans ~$4,000-$6,300 — wide, and some houses have trimmed.
- Levels: GLD 428.07 (+0.32%), ATR 7.19 (1.68%), 20d 398.18, 50d 384.67, 150d high 509.70 (-16.0%), low 363.32. GDX 105.52 (+1.91%), already +51.3% off its low.
- **Derived ratio:** GLD 428.07 against gold ~$4,400 implies ~0.0973 oz per share. Using that to convert forecasts: HSBC $4,750 -> GLD ~462; Deutsche $5,150 -> ~500; JPM $6,000 -> ~583. This ratio is derived from two fetched numbers, not a published constant, and it decays slowly with fund expenses.
- **Floor arithmetic, done honestly:** with a bear case of $3,600/oz (GLD ~350, below the 150-day low of 363.32) and a defended target of GLD 500 (Deutsche 2027), the long_term 2.5 R:R floor is only cleared at an entry near **392 or lower**. At today's 428 the R:R is ~1.4 and the idea **does not qualify**. Using JPM's $6,000 top-of-range to make 428 work would be reverse-engineering the target to clear the floor, which `config/strategy.md` forbids.
- **Conclusion: publish as accumulate-on-pullback with wait=true, not as a buy today.** The previously published 398 entry (2026-08-22) never filled — the market ran to 428 instead — so this is essentially the same level restated, not a new one.
- sources: https://www.jpmorgan.com/insights/global-research/commodities/gold-prices , https://financefeeds.com/gold-price-forecast-2026-central-bank-demand/ , https://goldsilver.com/industry-news/article/gold-price-outlook-august-2026/

## [06:52 ET] CRYPTO — post-mortem on the short, and why there is no new crypto candidate
- **BTC 78,638 (-0.76% 24h), after a +22% WEEK.** It touched $81,257 on 2026-08-25 — a three-month high, first time above $80,000 since mid-May — then faded to ~$78,800.
- What actually drove it: (1) US spot BTC ETFs took in **~$1.918B over five sessions through 2026-08-21, the strongest weekly inflow of 2026**; (2) **>$4.3B of short positions liquidated**; (3) the US Treasury expanded its long-term bond buyback programme. Open interest is now **$140B**.
- **This is the mechanism that destroyed our /MBTU6 short** — not a slow drift against us but a squeeze that our own position was fuel for. Support cited at $77,000-78,000. Standard Chartered forecasts $100,000 by year end.
- source: https://www.bloomberg.com/news/articles/2026-08-25/bitcoin-reaches-three-month-high-of-80-000-as-momentum-returns , https://news.bitcoin.com/market-updates/bitcoin-price-reclaims-79000-as-open-interest-hits-140b/

## [06:53 ET] REJECTED — BTC / /MBT long — no new position after covering
- Buying BTC at 78,638 after a +22% week driven by $4.3B of forced short covering is the mirror image of the mistake we are closing today. Open interest at a record $140B means the crowding has simply flipped sides.
- The correct action after a stopped-out short is flat, not reversed. **Cover and stand aside.**

## [06:53 ET] REJECTED — ETH — the most interesting crypto setup, still not good enough
- ETH 2,457.79 (-0.78%). ETH/BTC ratio computes to **0.0313** (2457.79/78638) against a 10-month low of 0.024-0.027 in May, so the ratio has already recovered ~20-30% off the bottom.
- Genuine positive: **Ethereum ETFs out-drew Bitcoin ETFs in July 2026 for the first time**, and ETH rallied ~20% vs BTC's ~7% between 08-19 and 08-21.
- Against it: five structural drags are unresolved — weaker ETF flows historically, higher Nasdaq correlation, no corporate-treasury floor of the kind BTC has, Layer-2 value-capture leakage, and direct competition from Solana. The cited base case is the ratio grinding sideways near its lows.
- **No dated catalyst inside the horizon and no probability disagreement I can state.** Rejected on the absence of a catalyst, not the absence of a story.
- source: https://crypto.news/ethereum-price-prediction-will-eth-underperform-bitcoin-2026/ , https://www.ig.com/uk/trading-strategies/why-is-ethereum-falling-faster-than-bitcoin-2026-260616

## [06:53 ET] REJECTED — SOL — 96.72 (-2.65%), no dated catalyst, and it is the competitive winner in the ETH story rather than an independent thesis

## [06:54 ET] LIVE CRUDE — this is new information and it changes two captured ideas
- **WTI $80.32, -$2.04 (-2.48%), quoted 2026-08-26.** Brent $86.08 (-2.82%). Crude "fell toward $80 per barrel on Wednesday, extending losses into a **third consecutive session**" on **diplomatic developments between Iran and Oman regarding maritime corridors in the Strait of Hormuz**.
- source: https://tradingeconomics.com/commodity/crude-oil
- Confirming: USO closed **-4.58%** at 126.15 and BNO **-4.77%** at 50.26 on 2026-08-25. XOP -1.88%. UNG +0.79% (gas decoupled).
- **Two consequences:**
  1. **XLE — upgrade from "tighten the stop" to "close it."** A 60.40 breakeven stop will simply be hit with slippage on this. Take the +2% deliberately instead.
  2. **FRO — the Hormuz leg of the tanker thesis is now a live risk, not a tailwind.** The Lloyd's List mechanism was that the crisis cut VLCC volumes 36% *but lengthened every voyage*, pushing tonne-miles to records. If Iran-Oman diplomacy reopens the corridor, volumes recover and voyages SHORTEN — the tonne-mile boost unwinds. FRO's Q2 is already contracted so the dividend catalyst is unaffected, but the forward guide and the 56 second target are.
- **REJECTED — /MCL short WTI:** the thesis is right and now largely spent. WTI at $80.32 is already at J.P. Morgan's Q4 Brent-implied target. To a $74 target with an $84 stop the R:R is (80.32-74)/(84-80.32) = **1.72**, under the 2.0 swing floor. Correct view, no edge left at this price.

## [06:55 ET] HOUSING / HD / BCC — holds, with the tight-stop problem stated
- 30-year fixed mortgage **6.65%** (2026-08-20). Fannie Mae forecasts **6.7% in Q3 and 6.8% in Q4** — rates going UP, not down. Consistent with the 2y at 4.24% above fed funds.
- Housing itself is not collapsing: sales +6.1% y/y, inventory up, new listings +2.4% y/y in June, strongest spring for listings since 2022.
- **HD Q2 (reported 2026-08-18): beat.** Sales +5.7% to $47.86B vs $47.27B expected. Repair/maintenance demand strong; big-ticket remodels weak. Contractor demand outpaced DIY; $1,000+ transactions +2.4%. Management warns 2026 growth depends on a housing recovery.
- decision: **HOLD both HD longs, stop 328 unchanged.** But note honestly: HD's ATR is 8.52 and the stop is only 9.88 below spot = **1.16 ATR**. That is tight enough to be hit on noise. I am not widening it — widening a stop after entry is how small losses become large ones — but the reader should expect this position to be stopped out on an ordinary down day.
- decision: **HOLD BCC @81.00, stop 76.00.** Flat. BCC is building products and shares the same rate-driven demand risk as HD; together with HD that is 3 open positions on one housing/rates driver, which is the correlation cap. **No new housing exposure today.**
- sources: https://www.investing.com/news/economy-news/home-depot-beats-quarterly-sales-estimates-on-steady-repair-demand-4864685 , https://www.freddiemac.com/pmms , https://www.lendingtree.com/home/mortgage/rates/mortgage-interest-rates-forecast/

## [06:57 ET] VST — quality de-rated while the fundamentals delivered. Best long-term find today.
- Hard numbers (10-Q filed 2026-08-10 for period ending 2026-06-30):
  - **Q2 2026 adjusted EBITDA $1,767M**, up **>30%** from $1.35B in Q2 2025.
  - **FY2026 guidance: adjusted EBITDA $6.8-7.6B**, management "comfortable delivering at or above the midpoint".
  - **Adjusted FCF before growth guided $3.925-4.725B** against a **$46.63B market cap** = a **8.4-10.1% forward FCF yield**.
  - Forward P/E **13.57x**, EV/EBITDA **10.04x**, trailing FCF $2.26B (4.84% yield), 335.64M shares, 85.6% institutional.
- **The paradox:** every bull-case item arrived — hyperscaler PPAs with Meta and Amazon, a record EBITDA print, a datacenter JV with NVIDIA in it — and the stock fell **28% over twelve months**, from above $219 to $139.03. Sector-wide de-rating of AI-power as investors question how fast infrastructure spend converts to profit, not a company-specific setback.
- **Insider: CEO JAMES A. BURKE bought 2,000 shares at $135.00 on 2026-08-24 — two days ago, open market.** Only $270K, and set against 8 sells totalling $6.86M, but it is a purchase at almost exactly today's price by the person who wrote the guidance.
- External anchors: analyst consensus PT **$219.72**, bull **$313**, **bear $106**.
- Levels: 139.03 (+2.48%), ATR 4.56 (3.28%), 20d 143.48, 50d 152.96 — both overhead, confirmed downtrend. 150d high 178.31 (-22.0%), low 132.66 (+4.8%).
- **Floor arithmetic:** using the published $106 bear case and an 18x-forward-P/E target of $184 (deliberately below the $219.72 consensus), the 2.5 long_term floor is cleared only at an entry near **128** — which is below the 150-day low and is the same level published on 2026-08-25 that never filled. At 139 the R:R is 1.5 and it does not qualify. So: same level, restated, wait.
- sources: https://financefeeds.com/vistra-vst-stock-prediction-bull-bear-case/ , https://www.sec.gov/Archives/edgar/data/1692819/000169281926000019/vistra-20260630.htm , https://www.sec.gov/Archives/edgar/data/1692819/000126840626000007/xslF345X06/wk-form4_1787601817.xml

## [06:59 ET] REFINING — the inverse of the XLE trade, and a genuinely different driver
- **Diesel crack spread hit a record $102.20/bbl on 2026-08-17** — first time in history above $100, against a normal historical range of **$15-25**.
- Drivers are supply-side and sticky: distillate inventories fell a further 1.5M bbl and sit well below the five-year average; refinery strikes and **Russia's export ban** created a shortage that crude releases cannot fix.
- EIA expects high crack spreads **through end-2026**. BofA's Francisco Blanch: diesel stays tight and expensive **well into next year**.
- MPC and VLO share prices have roughly **doubled in 2026**; both more than doubled per-barrel refining margins in Q2 and together returned >$5B via buybacks and dividends.
- **Key point: falling crude is a TAILWIND here, not a headwind.** A crack is product minus crude, so WTI dropping to $80.32 while diesel stays bid widens the margin. This is the correct way to stay long energy while exiting XLE flat-price beta.
- sources: https://discoveryalert.com.au/diesel-crack-spread-record-high-refining-margins-2026/ , https://www.forbes.com/sites/garthfriesen/2026/07/23/refining-stocks-soar-as-crack-spread-hits-record-high-in-2026/ , https://www.eia.gov/outlooks/steo/report/petro_prod.php

## [06:59 ET] DINO — the pick of the refiners, and our published 93 entry is now live
- **Q2 2026 (8-K): net income $892M / $4.93 per diluted share** vs $208M / $1.10 in Q2 2025. **Adjusted $960M / $5.31/share** vs $1.70. EBITDA $1,404M, adjusted EBITDA **$1,482M — more than doubled**.
- Dividend raised **5% to $0.525/quarter**; $265M returned to shareholders in Q2.
- **Named corporate catalyst: separation of the Lubricants & Specialties segment into a new independent public company, over the next 12-18 months.**
- **Insiders: 3 open-market buys, 2 distinct buyers, $2.42M against $1.71M of sales.** Director **Franklin Myers bought 15,000 sh @ $85.30 on 2026-08-11** and 15,000 sh @ $69.11 on 2026-05-18 — the same buyer scaling up twice, the second time two weeks ago and 8% below today.
- By contrast **VLO: 0 open-market buys, 5 sells, $5.65M.** DINO is the one with insider confirmation.
- Levels: 93.24 (-2.04%), ATR 3.51 (3.76%), 20d 90.31, 50d 82.53, 150d high 98.39 (-5.2%), low 47.00 (+98.4%).
- **Horizon call — this is a SWING, not a long_term hold, and the arithmetic is why.** Against an honest cyclical bear case (cracks revert to the $15-25 norm, DINO earns Q2-2025-like numbers, ~$62), a 112 target gives R:R of 0.79 and fails the 2.5 long-term floor outright. Against a chart stop at 82 it gives 2.75 and clears the 2.0 swing floor. A crack spread at 4x its normal range cannot be underwritten for years — so do not pretend it is a hold.
- sources: https://www.sec.gov/Archives/edgar/data/0001915657/000191565726000046/dinoex99106-30x2026.htm , https://www.sec.gov/Archives/edgar/data/0001915657/000191565726000046/dinoex992strategictransform.htm , https://www.investing.com/news/company-news/hf-sinclair-reports-q2-earnings-of-493-per-share-93CH-4816101

## [06:59 ET] REJECTED — VLO / MPC — same record-crack driver as DINO but 0 insider buys (VLO: 5 sells, $5.65M) and no company-specific catalyst; correlation cap means one refiner, and DINO is the one with the Form 4s and the spin-off

## [07:00 ET] STALE UNFILLED LEVELS — explicitly withdrawn, so synthesis does not re-litigate them
- **LULU @115 (published 2026-08-22) — WITHDRAWN.** LULU closed 118.33 (-3.62%) on the DKS read-through. DICK'S just told the market that athletic footwear and apparel is increasingly promotional and got worse through the quarter; that is adverse information for a premium-priced athleisure brand, and the 115 level was set before it existed. Re-underwrite from scratch or not at all.
- **EEM @65.6 (published 08-21, 08-22, 08-23) — WITHDRAWN.** EEM is 67.25 (+1.72%), 2.5% above the level, which has now failed to fill three times. I gathered no new information on emerging markets today and the dollar-index fetch failed, so I have no basis to restate it. Three re-pitches without a fill is the anchoring pattern the prior context warns about.
- **CEG @266 (published 2026-08-21) — NOT re-pitched.** CEG 278.42 (+1.83%) is 4.7% above the level. VST is the better expression of the identical AI-power thesis: cheaper (13.6x forward vs CEG's premium), with the CEO buying on 2026-08-24. Correlation cap allows one, and it is VST.
- **SVRA @5.35 (published 2026-08-23) — NOT re-pitched.** SVRA 5.60. I did no work on it today and will not restate a small-cap biotech level on stale research.
- **BCC @76.5, NKE @40.75, DHT @19.4, VST @134 (published 2026-08-24/25) — superseded.** BCC and NKE are held; DHT's re-entry is withdrawn above; VST's level is restated at 128 with fresh evidence.

## [07:01 ET] FALSIFICATION PASS — the case against each finalist
- **FRO** — the Hormuz leg is actively unwinding on Iran-Oman talks, which is the mechanism that made tonne-miles a record. Q2 is banked so the dividend is safe, but the forward guide is not. Handled by cutting size to 1.5%, lowering targets to 48.50/53, and shortening the time stop to 09-18.
- **DINO** — a $102 crack against a $15-25 norm is 4x normal and mean-reverts by definition. Handled by making it a swing with a hard 82.00 stop and a 2026-11-28 time stop, and stating explicitly that it FAILS the long-term floor.
- **VST** — the market may be correctly pricing hyperscaler counterparty and renegotiation risk rather than being wrong. The 128 entry requires a break of the 150-day low, so it fills only if sentiment worsens. The CEO's buy is $270K against $6.86M of insider sales.
- **DG** — the +21% average surprise cuts both ways: the buy side already expects a beat, so in-line is a disappointment. Handled by refusing to hold into the print at all.
- **NVDA** — the base rate is against the setup: 14 of 24 qualifying gaps were UP, averaging +8.9%. This candidate expires unfilled more often than it fills, and that is stated.
- **DKS** — Foot Locker may not be fixable, and the stock closed on the low of a 31% day with zero insider buying against $47.1M of sales. Handled with conviction 2, 1.5% sizing, and a wait below 112.
- **GLD** — the target rests on bank forecasts spanning $4,000-$6,300, which is not a forecast. Handled by anchoring to Deutsche's $5,150 rather than JPM's $6,000 and refusing to buy at 428.
- **Exits (TJX, KRE, XLE, /MBTU6)** — the case against all four is the same: each is being sold below its recent high, and three of the four could bounce. The answer is that a breached stop is not a position, it is an unpriced new trade.

## [07:02 ET] SMALL CAPS — screened, nothing cleared. Logged rather than forced.
- Screened for open-market insider buying across the small caps with catalysts inside 10 sessions: PLAB, MBUU, DAKT, CAL, JILL, TLYS, CURV, DLTH, CXM, AVNW, ODD, LUCK.
- Result: **zero meaningful clusters.** PLAB has 27 sells and no buys. CXM 18 sells, ODD 6, CURV 4, TLYS 3. The only two with any buys are trivial: DAKT one purchase of **$1,565** and LUCK three totalling **$10,223** — amounts consistent with plan mechanics, not conviction.
- **No small-cap candidate today.** `config/universe.md` wants this lane hunted deliberately and I did hunt it; the honest outcome is that nothing passed. Padding it with a conviction-2 name I have no evidence for would be worse than the gap. This belongs in `data_quality_notes`.

## [07:03 ET] PFE — a named risk to the open long that the reader should see
- **Eliquis (apixaban), co-marketed by Bristol Myers Squibb and Pfizer, has key protections expiring mid-2026** — it is one of the drugs at the centre of a patent cliff estimated to strip ~$300B, a sixth of industry revenue, by 2030. Pfizer's Xeljanz (tofacitinib) is also on the 2026 expiry list.
- This does not change the HOLD: CEO Bourla bought 38,000 shares at $26.34 on 2026-08-12 with full knowledge of the Eliquis timeline, and director Buckley bought 37,632 at $25.52 on 08-05. But it is the concrete mechanism by which the PFE thesis fails, and it should be stated rather than left implicit.
- source: https://www.pharmavoice.com/news/big-pharma-navigating-patent-cliff-300-billion-jnj-merck-abbvie/810915/ , https://www.labiotech.eu/best-biotech/pharma-patent-cliff/

## [07:05 ET] KURA — the small-cap idea the screen failed to find, surfaced by the insider tape
- **KURA +9.60% to 13.59 on 2026-08-25** after CEO **Troy Wilson disclosed buying 100,000 shares at $12.39 on 2026-08-24 = $1,239,000** open market (Form 4 filed 2026-08-24). One buy, one distinct buyer, against 6 sells totalling $1.04M — net positive $198K.
- **LIQUIDITY CHECK (required before anything else): 20-day average dollar volume $23.5M** on ~2.10M shares/day. That is ~47x the $500K floor. Position sizing is not remotely constrained.
- **Market cap ~$1.21B** (88.855M weighted-average shares x 13.59; the wire quoted "$1.00B" at the lower pre-move price). **Cash, equivalents and short-term investments $519.0M** at 2026-06-30, so **enterprise value is roughly $690M**.
- The business is commercial, not pre-revenue: **KOMZIFTI (ziftomenib) received full FDA approval on 2025-11-13** for relapsed/refractory NPM1-mutated AML — the first and only once-daily targeted therapy for it.
  - Q2 2026 **net product revenue $9.1M, +57% quarter over quarter**; ~115 new patient starts (+35%); >250 total prescriptions (+59%); **majority share of new patient starts in the R/R NPM1-mutant AML menin inhibitor class**.
  - Collaboration revenue $11.8M. Net loss $68.3M. R&D $61.9M, G&A $31.8M.
- **Partner: Kyowa Kirin — ~$330M upfront, up to ~$1.2B in development/approval/marketing milestones.** With $180M of anticipated collaboration payments, the company states cash funds the ziftomenib AML programme **through Phase 3 KOMET-017 topline in 2028**. That neutralises the dilution risk that kills most small-cap theses.
- **Dated catalyst cluster, all 2H 2026:** updated KOMET-007 data in newly diagnosed AML; initial KOMET-007 data with quizartinib; initial KOMET-008 data with gilteritinib; MEIS1-associated AML exploratory analysis. Then FIT-001 Phase 1b enrolment completion 1H 2027 and data 2H 2027.
- Levels: 13.59, ATR 0.81 (**5.98%** — stop must be wide), 20d 10.52, 50d 10.63, 150d high 13.90 made yesterday, low 7.36 (+84.7%).
- **The problem: it closed at a new 150-day high after a +9.6% day.** Entry must be a pullback, and the CEO's own $12.39 is the natural anchor.
- sources: https://www.stocktitan.net/news/KURA/kura-oncology-reports-second-quarter-2026-financial-afoyfysnf2rs.html , https://ir.kuraoncology.com/news-releases/news-release-details/kura-oncology-and-kyowa-kirin-announce-fda-approval-komziftitm , https://www.sec.gov/Archives/edgar/data/1422143/000119312526363812/xslF345X06/ownership.xml , https://www.cnbc.com/2026/08/25/stocks-making-the-biggest-moves-premarket-dks-amd-kura.html

## [07:04 ET] VENUE CHECK — /MBT confirmed tradeable on Robinhood
- Robinhood's own futures-availability support URL returned **HTTP 404**, so it could not be used. Verified through a secondary source instead: **Robinhood offers CME Micro Bitcoin futures (MBT), representing 0.1 Bitcoin**, at a benchmark fee of $3.75 per 5-contract trade. This confirms both the venue and the 0.1 BTC multiplier used to compute the ~$1,450-per-contract loss on the open short.
- Caveat recorded honestly: contract selection on Robinhood is described as limited relative to dedicated futures brokers. source: https://brokerchooser.com/broker-reviews/robinhood-review/micro-bitcoin-futures-fees
- All other candidates are US-exchange-listed common stock or ETFs on `Robinhood Stocks`, which needs no special verification. FRO is NYSE-listed common stock, not a foreign ordinary.

## [07:05 ET] R:R AUDIT — every candidate recomputed against its floor
- Cleared: DINO 2.75, GLD 2.57, VST 2.55, KURA 3.00, DKS 2.81, NVDA 2.43, DG 2.35, FRO 2.23, TLT 2.18.
- **NKE FAILED at 2.40 against the 2.5 long_term floor** (entry 38, target 62, bear 28). Rather than move the target or soften the bear case, the entry was reset to **34.00** — the price at which new capital actually qualifies — and the recommendation restated as hold-and-do-not-add. Re-captured; R:R at 34 is 4.67.
- **DHT computes 7.4 and that number is misleading.** It is an artefact of a position update: the entry field carries the original 18.80 fill while the stop has been raised to 18.30, so the denominator is tiny. It is not a new 7:1 opportunity and must not be ranked as one.
- Exits (TJX, KRE, XLE, /MBTU6) carry no target or stop by design — they are closes, and R:R is not a meaningful measure for them.

## [07:06 ET] PRE-OPEN TAPE — final check
- **Today's 08:30 ET block is bigger than first logged:** July **PCE and core PCE**, July personal income and spending, **Q2 GDP second estimate**, and **July durable goods orders**. All in one print.
- S&P 500 futures -0.1%, Nasdaq-100 futures -0.2%. "US stocks slipped as traders held back from taking risk ahead of the latest earnings report from Nvidia Corp."
- Chipmakers reclaimed some ground ahead of the NVDA print.
- **Treasuries retreated across the curve ahead of the PCE print, shrugging off a third straight decline in oil.** Yields UP means **TLT opens lower** — adverse for the open TLT long, which sits at 83.47 with a stop at 80.95, so ~3% of room remains. No change to the levels; the 08:30 print decides it either way, which is exactly why it was captured as conviction 2.
- Confirms the third consecutive down session in crude that drove the XLE exit and the FRO risk downgrade.
- sources: https://www.bloomberg.com/news/articles/2026-08-25/asian-stocks-set-to-gain-as-oil-extends-declines-markets-wrap , https://www.earningswhispers.com/calendar

## [07:07 ET] RESEARCH COMPLETE
- **candidates: 18 captures, 15 unique symbols** (synthesis should take the last entry per symbol — NKE, FRO and XLE were each deliberately re-captured after new information arrived mid-run).
  - **Exits / risk actions (4):** /MBTU6 cover (conv 5, most urgent), TJX close, KRE close, XLE close.
  - **Position updates, hold (3):** DHT (stop raised 17.60 -> 18.30), NKE (hold, do not add, entry reset to 34), TLT (hold into the 08:30 print, flagged weakest).
  - **New swing (5):** DINO (conv 4), DG, NVDA, FRO, KURA.
  - **New long_term (3):** VST (conv 4), GLD, DKS (conv 2).
- **Skew, stated honestly:** 6 of 15 carry `wait: true`. That is not indecision — the tape is extended (gold +10% on the month, BTC +22% on the week, refiners and tankers near highs) and in most cases the reward-to-risk floor is simply not met at today's price. Four ideas are closes rather than opens. This is a risk-reduction day.
- **Correlation check:** cheap-crude beneficiaries FRO/DHT/DINO = 3 (at the cap, and DINO's driver is product cracks rather than tonne-miles). Consumer/retail DG/DKS = 2. AI NVDA/VST = 2. Monetary GLD = 1. Biotech KURA = 1. No breach.
- **Coverage gaps:**
  - **Event contracts — a total gap.** Kalshi returned ok:true with count=0 for every financial query tried (Fed, CPI, Bitcoin, recession, inflation, Fed Funds, interest rate, S&P, GDP). An empty query returned only sports parlay shards with null prices. No event-contract idea could be honestly priced, and the open KXFEDDECISION-26SEP-H25 position could not be marked to market.
  - **Small caps — hunted, nothing qualified.** Screened twelve names with catalysts inside 10 sessions for insider buying; found only $1,565 (DAKT) and $10,223 (LUCK). KURA was surfaced instead via the insider tape, not the screen.
  - **Futures beyond the /MBT cover — none.** The /MCL short was the honest candidate and was rejected on arithmetic: at WTI $80.32 the R:R to $74 with an $84 stop is 1.72, below the 2.0 floor. No index-futures idea because I had no directional edge into the 08:30 print.
  - **Crypto — deliberately empty.** Both BTC and ETH were examined and rejected with reasons logged.
  - **DG consensus is unresolved:** Zacks-sourced $2.00 EPS / $11.17B revenue vs finnhub $2.06 / $11.53B. Treated as a range rather than picking one.
- **Sources that failed:** Yahoo Finance HTTP 429 across all index/macro symbols (SPX, NDX, DJI, RUT, VIX, ES, NQ, DXY, gold, WTI); Finnhub blocks CFD indices; AlphaVantage has no API key; CoinGecko failed on the first `macro` call but succeeded standalone; Kalshi events empty for all financial queries; Robinhood's futures-availability support page returned HTTP 404; `stocktitan` DG figures and finnhub disagree; **finnhub's earnings calendar had FRO on 2026-08-31 when the company says 2026-08-28** — the only date error caught, and worth distrusting that field generally.
