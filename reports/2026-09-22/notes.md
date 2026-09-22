# Research log — 2026-09-22

## [06:03 ET] MACRO — rates, policy, data sources
- FRED: US10Y **5.01%** (2026-09-18), US2Y **4.76%** (2026-09-18), Fed funds effective **3.88%** (2026-09-18), 10y-2y curve **+0.20** (2026-09-21), unemployment **4.1%** (2026-08), CPI index 334.131 (2026-08) — source: https://fred.stlouisfed.org
- Notable: 10y at 5.01% sits ~113bp ABOVE effective fed funds of 3.88%. That is a steep term premium / long-end repricing, not a normal easing-cycle curve. Long-duration bonds remain pressured; supports the existing TLT short.
- TLT last 81.80 (2026-09-21 close via market_data bonds_20y), prev close 81.25, +0.68%.
- **DATA GAP:** Yahoo Finance returning HTTP 429 (rate-limited) for ALL index symbols. spx/ndx/dow/rut/vix/es/nq/DXY/us10y-quote/gold/wti ALL failed. Finnhub refuses indices ("Market data subscription required for CFD indices"). Stooq 404s on ^-prefixed tickers. No AlphaVantage key.
- **DATA GAP:** CoinGecko crypto prices failed this run.
- Consequence: I have NO live index level, NO VIX, NO DXY, NO spot gold/crude this morning. Any idea requiring those must be dropped or sourced elsewhere. Will not estimate.

## [06:03 ET] CALENDAR — dated earnings inside 10 sessions (finnhub, fetched)
- 2026-09-22 (today) bmo: AZO (est EPS 54.80, rev 6.78B), THO (0.92, 2.20B), MLKN; amc: KBH (0.90), WOR
- 2026-09-23 bmo: CTAS (1.375, 3.04B), PAYX (1.347, 1.66B); amc: FUL, SFIX
- 2026-09-24 bmo: **SNX (4.689, 19.05B)**, DRI (2.074, 3.24B); amc: **COST (6.673, 96.75B)**
- 2026-09-28 bmo: CCL (1.365, 8.38B); **NKE (0.4495, 11.47B)**
- 2026-09-29: CAG (0.285, 2.61B), KMX (0.717, 7.01B), CNXC
- 2026-09-30 bmo: JBL (4.10, 9.79B), JEF; amc: **MU (32.22, 52.10B)**, FDS
- 2026-10-01 amc: ACN (3.21, 18.21B); bmo: AYI
- source: https://finnhub.io/api/v1/calendar/earnings
- Direct read: SNX (09-24), NKE (09-28), CAG (09-29) and MU (09-30) are all ALREADY open/awaiting-entry items in prior_context. Those are position-management decisions with a hard date, not new ideas.

## [06:12 ET] MACRO — crude is the day's driver
- WTI fell to **$95.59/bbl on 2026-09-21, -4.69%** — fourth consecutive down session. Brent settled **$100.34**, -7.7% from its 2026-09-15 peak, and traded briefly under $100 intraday.
  source: https://tradingeconomics.com/commodity/crude-oil
- **Cause is de-escalation, not demand.** Trump reportedly decided against striking Yemen for now and signalled openness to diplomacy with Iran, rejecting Saudi calls to hit the Houthis. Middle East exports have stayed resilient despite Saudi Arabia closing the East-West pipeline after attacks — 2.9 mb/d through Hormuz over the prior six days.
  source: https://tradingeconomics.com/commodity/crude-oil
- OPEC and the IEA both cut 2026 demand outlooks. source: https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Fall-as-OPEC-and-IEA-Slash-2026-Demand-Outlooks.html
- Read-through: crude near $95-100 carries a **geopolitical risk premium that is actively deflating**. The report holds THREE correlated energy longs (XLE, DINO, DVN) — that is exactly at the `config/strategy.md` correlation cap of 3 on one driver. Today's correct action is to manage those, not add a fourth.

## [06:13 ET] TAPE — 2026-09-21 closes (finnhub, prev session; market is closed pre-open)
- SPY **773.50 +1.55%** — broad tape strong.
- Energy sold off AGAINST that tape: XLE **62.46 -2.88%**, DINO **109.29 -5.70%**, DVN **47.59 -2.10%**. That divergence is the crude premium coming out, not a market event.
- XLE has now closed below its SMA20 (64.05) for the first time in the recent run; SMA50 61.32 is the next shelf.
- Power/IPP still de-rating: CEG **262.11** (-31.2% off high, SMA200 292.33), VST **140.78** (-22.9% off high, SMA200 156.27). Both below their 200-day and falling.
- Other opens: CCJ 93.23, BCC 75.66, LCII 86.95, PFE 27.74, EEM 68.83, GLD 398.38, LULU 101.30, SVRA 5.45, TLT 81.80.
- NOTE: prior_context.md quotes the 09-18 close, so it is one session stale (e.g. it shows CEG 254.71; the 09-19/09-21 close is 262.11). Working from freshly fetched 09-21 closes throughout.

## [06:14 ET] POSITION UPDATE — NKE — BUY opened 2026-08-17 @ 40.75, last 36.10, -11.4%
- decision: **CLOSE the long.** Do not carry it into the print.
- why: NKE closed 36.10 on 09-21 against a 200-session low of 35.35 — it is 2.1% off the low, 47.8% off the high, and stacked below SMA20 37.77 / SMA50 40.28 / SMA200 50.08, all declining. The position carries **no stop at all** (prior_context: Stop = None) and Q1 earnings are confirmed for **2026-09-28** on the fetched finnhub calendar (est EPS 0.4495, rev 11.47B). An unstopped long, down 11%, at a 52-week low, four sessions from a binary print is the worst risk configuration available.
- the report already said exit once: a NKE SELL was published 2026-09-08 @ 38.40 and is +7.5%. The long apparently persisted alongside it. This completes that exit rather than opening a new view.
- this is NOT a short. I am not pitching bearish NKE — the stock is at a low with a catalyst that could resolve either way. The claim is only that this specific unstopped long should not be the vehicle.
- action: captured via add_candidate.py.

## [06:15 ET] THEME — merchant power (VST, CEG): the AI-power trade has de-rated, insiders are buying
- Whole merchant-generation complex reset in 2026. CEG -31.2% off high, VST -22.9% off high; both under a declining SMA200.
- **Driver is ERCOT 2027 forward power prices, not operations.** Forwards are materially below where they sat on 2025-10-31, the date framing VST's original 2027 EBITDA opportunity of $7.4-7.8B. YTD ERCOT wholesale has run ~$30/MWh and CEO Jim Burke said plainly that level does not support new construction.
  source: https://www.tikr.com/blog/vistra-is-down-36-from-its-all-time-high-is-the-ai-power-trade-still-worth-owning
- Operations have NOT broken: VST Q2-26 ongoing-ops adj EBITDA **$1.767B, +30% YoY**, and management **reaffirmed** FY2026 guidance of **$6.8-7.6B**.
  source: https://finance.yahoo.com/markets/stocks/articles/vistra-ceo-bought-1-17-054858384.html
- **INSIDER BUY (VST) — the signal of the day.** CEO/President James Burke bought via JAMEB, LP (spousal LP): 2,000 sh @ $135 on 08-24; 2,200 sh @ wtd-avg $135.99 on 08-31; 4,465 sh @ wtd-avg $135.25 on 09-01. **8,665 shares, $1.17M total.** Vehicle already held 1,146,352 shares afterwards — this is a man with maximum existing exposure choosing to add more.
  sources: https://finance.yahoo.com/markets/stocks/articles/vistra-ceo-bought-1-17-054858384.html , https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001692819&type=4
  (finnhub 6-mo insider window independently confirms the 08-24 tranche: BURKE JAMES A, 2,000 sh @ 135.00, code P.)
- **INSIDER BUY (CEG):** director Roger W. Crandall, 1,500 sh @ $278.62 on 2026-08-11 ($417,931). Zero insider sells at CEG in the 6-month window. source: finnhub insider-transactions
- Analyst revision direction splits the two: **VST improving** (bullish share 91.7%, +0.4; 7 strong buy / 15 buy / 2 hold / 0 sell) vs **CEG deteriorating** (82.1%, -3.1; a buy moved to hold in September). source: finnhub recommendation-trends
- Relative strength splits them too: over 1 month **VST +1.32% vs XLU -7.11% = +8.43% vs peer** — VST is leading a sector that is being sold. Over 3m it lagged (-6.75% vs peer) and 6m it is -22.85% vs SPY. The turn is one month old, which is honest to say rather than to oversell.
- Valuation: VST at **10.8x EV/EBITDA** on the reaffirmed $7.2B 2026 adj EBITDA midpoint. Street median 12-month target **$221** across 20 analysts, range **$106-$305**, mean ~$225.
  source: https://www.tikr.com/blog/is-vistra-stock-undervalued-in-2026-the-street-thinks-so-at-225-mean-target
- That $106 low end is the honest bear anchor and I am using it rather than the median.

## [06:17 ET] DATA GAP — event contracts could not be screened this run
- `market_data.py events` returns `{"ok": true, "count": 0}` for every macro term tried: "Fed decision", "FED", "KXFED", "interest rate", "inflation", "Powell", "recession", "government", "CPI", "oil", "Bitcoin", "S&P". The one term that returned anything ("Fed") returned unrelated sports markets (KXMVECROSSCATEGORY tennis/basketball tickers), which is a matching artefact, not a Fed market.
- So the Kalshi-backed prediction-market lane is unscreened today. **No event-contract candidate will be captured**, and that is a source failure rather than an absence of opportunity — notably the Trump-Xi summit below is exactly the kind of binary an event contract prices better than an equity. Synthesis should say so in data_quality_notes.
- Three KXFEDDECISION contracts sit in prior_context awaiting entry; I cannot re-price them without the feed, so I am leaving them untouched rather than guessing.

## [06:18 ET] CATALYST — Trump-Xi summit 2026-09-23 to 09-25, rare earths central
- Trump and Xi meet in Washington **Sept 23-25**, with the US-China tariff truce expiring **2026-11-10**. Rare-earth magnet and critical-mineral flows are a headline agenda item; US officials say current flows are insufficient.
  sources: https://www.cnbc.com/2026/09/20/bessent-chinas-he-to-hold-talks-on-ai-trade-minerals-reuters.html , https://www.usnews.com/news/top-news/articles/2026-09-20/us-treasurys-bessent-chinas-he-to-launch-talks-on-ai-trade-critical-minerals
- Treasury Secretary Bessent and Vice Premier He Lifeng met Sunday 09-20 to tee up agreements on AI, tariffs and critical minerals.
- Bloomberg 09-21: **China's rare-earth magnet exports to the US dropped ahead of the meeting.** source: https://www.bloomberg.com/news/articles/2026-09-21/china-rare-earth-magnet-exports-to-us-drop-before-xi-trump-meet
- Structural, and independent of the summit: **DFARS 252.225-7052 expands 2027-01-01** — covered defense procurement then requires NdFeB magnets free of covered-country material across the entire chain: mining, refining, separation and finished magnet. source: https://rareearthexchanges.com/news/trump-xi-summit-rare-earth-trade/
- 09-21 tape already moving on it: USAR +9.2% to 16.78 on a rare-earth separation partnership. source: https://stockanalysis.com/markets/premarket/

## [06:19 ET] MP Materials — structural floor, but the summit is a coin flip in 1-3 sessions
- DoD partnership (fetched): **10-year NdPr price floor at $110/kg**, structured as a contract-for-difference with DoD paying the gap to market; $400M DoD convertible preferred; $150M loan for heavy rare-earth separation; DoD guarantees **100% offtake of 10X Facility magnets for 10 years**.
  sources: https://mpmaterials.com/news/mp-materials-announces-transformational-public-private-partnership-with-the-department-of-defense-to-accelerate-u-s-rare-earth-magnet-independence/ , https://fas.org/publication/unpacking-dod-and-mp-partnership/
- Q2-26 NdPr production **840 metric tons, +41% YoY**; the price floor produced **$17.6M of real price-protection income** in the quarter — the floor is not theoretical, it is already paying.
  source: https://rareearthexchanges.com/news/mp-materials-raises-ndpr-output-41-as-mine-to-magnet-execution-becomes-the-real-test/
- Analysts 96.4% bullish and improving (9 strong buy / 18 buy / 1 hold / 0 sell). source: finnhub recommendation-trends
- **Against it:** insider flow is net badly negative — 2 open-market buys by ONE buyer (Rosenthal, 17,000 @ 56.62 on 05-20 and 10,000 @ 54.30 on 06-09, $1.51M) against **20 sells totalling $79.9M**, net -$78.4M over six months. I am not counting this as a positioning confirmation; it cuts the other way.
- **Also against it:** MP is lagging everything. vs SPY: -10.59% 1m, -20.98% 3m, -20.45% 6m. vs XLB: -3.99% 1m, -13.37% 3m. The tool's own verdict: "lagging SPY on every window measured".
- Levels (fetched, 200 sessions): last 50.00, ATR14 2.49 (4.99%), SMA20 53.53, SMA50 50.87, SMA200 57.22, range 37.81-76.80 (-34.9% off high), avg $vol 288.3M/day.
- **Judgement: do not buy before the summit.** A deal that restores Chinese magnet flows removes the scarcity premium and takes MP lower; no deal takes it higher. That is a diplomatic coin flip 1-3 sessions out, and buying into it is the same unstopped-long-into-a-binary configuration I am closing NKE to avoid. The DFARS Jan-2027 rule and the $110/kg floor are the durable part and they will still be there on 09-26. Capture as long_term with wait=true.

## [06:20 ET] THEME — refining cracks are at all-time records, which SPLITS the energy book
- US ULSD (diesel) crack hit an intraday record **$108.02/bbl on 2026-09-03**; diesel refining margins above **$106/bbl**, an all-time high.
  source: https://www.bloomberg.com/news/articles/2026-09-01/diesel-margins-surge-to-highest-on-record-as-supply-tightens
- 3-2-1 crack spread record close **$69.66/bbl**. Retail regular gasoline **$4.29/gal**, retail diesel **$6.05/gal** (all-time high) as of 2026-09-11.
  source: https://www.eia.gov/todayinenergy/detail.php?id=68104
- Cause is physical, not speculative: US refineries running **97.2-98% of operable capacity** against a typical ~90%, leaving no spare capacity if a plant goes down; **distillate inventories 14% below the five-year seasonal average**.
  source: https://stillwaterassociates.com/low-tanks-high-margins-why-product-cracks-are-at-records-and-how-long-they-are-likely-to-last/
- **This is the correction to my 06:12 note.** I wrote that XLE, DINO and DVN are three positions on one driver. They are not. Falling crude is a *cost* for a refiner and a *revenue* for an E&P, so the crude de-escalation that hurts DVN is the best thing that can happen to DINO: feedstock falling while product cracks sit at records. The cluster is really two bets pointing opposite ways plus a diversified basket, which is why they are being decided differently below.

## [06:21 ET] POSITION UPDATE — DINO — BUY opened 2026-08-22 @ 107.50, last 109.29, +1.7%
- decision: **HOLD. Target 128 unchanged, stop 97.75 unchanged.**
- why: the thesis got better, not worse. DINO is a refiner and the 09-21 crude break to $95.59 cuts its feedstock cost while the 3-2-1 crack sits at a record $69.66 and diesel at $106+. Refinery utilisation at 97.2-98% and distillates 14% below the five-year average mean the margin is supply-driven and not quickly competed away.
- 09-21 was -5.70% to 109.29 after running 106.91 -> 116.62 between 09-14 and 09-17. Refiners trade with crude on the day regardless of the margin logic; that is noise against a round trip, not a thesis break.
- **Explicitly NOT walking the stop in.** ATR14 is 4.73, so the 97.75 stop sits 2.06 ATR below the 107.50 entry — right at the swing floor. Tightening it to lock in the 1.7% gain would lift the printed reward-to-risk while making the trade strictly worse, which is the KRE error in CLAUDE.md. Left alone.
- against it: DINO analyst revisions are deteriorating (52.2% bullish, -2.3). Refiner coverage lags cycle turns, but it is a real dissent and is stated rather than dismissed.
- action: captured via add_candidate.py as a hold/update.

## [06:22 ET] POSITION UPDATE — DVN — BUY opened 2026-09-11 @ 49.60, last 47.59, -4.1%
- decision: **CLOSE.** This is the energy position to cut.
- why, four things that all point the same way:
  1. DVN is a pure E&P. Its revenue IS the crude price, and the crude price just fell four sessions running to $95.59 because a war premium is deflating on Yemen/Iran de-escalation — not because of anything DVN can influence. OPEC and the IEA both cut 2026 demand outlooks.
  2. It is 1.47% above its own stop. Last 47.59 against a 46.90 stop with ATR14 1.35 — that is **0.51 ATR** of room. A stop that close is not protection, it is a coin flip on one ordinary session.
  3. It is lagging its own sector on every window measured: vs XLE -1.45% (1m), -4.99% (3m), -7.51% (6m).
  4. Insider flow: 0 open-market buys, 3 sells, net -$5.26M over six months.
- the one thing against closing: DVN analyst revisions are genuinely improving (87.9% bullish, +6.7 — the strongest revision move in anything I looked at today) and it outperformed SPY over 3m. That is why this is a close-at-market rather than a short.
- also relevant: prior_context shows DVN recommended **3x in the last 10 days**. Re-pitching it a fourth time to defend the position would be the anchoring the repetition guard exists to catch. Cutting it is the opposite of anchoring.
- action: captured via add_candidate.py.

## [06:23 ET] POSITION UPDATE — XLE — BUY opened 2026-08-15 @ 63.90, last 62.46, -2.3% — HOLD, no change, no candidate
- XLE closed -2.88% at 62.46, its first close below SMA20 (64.05) in this run, but it is still above SMA50 61.32 and far above SMA200 55.81. The 60.80 stop sits below the SMA50, which is a defensible place for the thesis to be wrong; it is 2.31 ATR below entry, above the 1.8 ATR ETF floor.
- XLE is a diversified basket holding both E&Ps and refiners, so the crack-spread record partly offsets the crude decline inside the same ticker. That is the reason it does not get the DVN treatment.
- Nothing changed enough to warrant a recommendation, so no candidate is captured for it. Holding as published.

## [06:25 ET] REJECTED — VLO, MPC, PSX, PARR — record cracks are fully priced; every refiner is parabolic
- I went looking for a second refiner to express the record-crack theme and found the theme is not a secret. Fetched 200-session history, all four sit within 5-7% of their highs and 100-150% above their lows:
  - VLO 393.27, -6.15% off high, +145.9% off low, SMA200 250.57 (price is 57% above its own 200-day)
  - MPC 402.38, -6.66% off high, +148.5% off low, SMA200 252.31
  - PSX 261.75, -5.55% off high, +105.8% off low, SMA200 178.78
  - PARR 82.00, -6.52% off high, +138.6% off low, SMA200 57.94
- Buying any of these today is buying a parabolic move *after* an all-time-record margin print, which is where refining cycles usually end rather than begin. The record crack is the reason they are up 150%, not an argument they go higher.
- DINO is held only because it is an existing position entered at 107.50 before this run, with an honest 2.06 ATR stop already in place. I would not open it here either, which is why the update says do not add above 110.50.
- No new refiner candidate captured. The correlation cap would have allowed one; the price does not.

## [06:26 ET] POSITION UPDATE — CEG — BUY opened 2026-08-21 @ 272.00, last 262.11, -3.6% — HOLD, no change, no candidate
- I expected to cut CEG in favour of VST and the relative-strength data refused it: CEG beats XLU on **every** window (+3.15% 1m, +4.21% 3m, +1.89% 6m). It lags SPY, but so does the whole utility complex. Insider flow supports it too — director Roger W. Crandall bought 1,500 sh @ $278.62 on 2026-08-11 ($417,931) and there are **zero** insider sells in the six-month window.
- Against: analyst revisions deteriorating (82.1% bullish, -3.1; a buy moved to hold in September), and price 262.11 is below SMA20 277.35 / SMA50 271.37 / SMA200 292.33.
- **Flag for the record:** the published stop of 250.00 is **1.91 ATR** below the 272.00 entry (ATR14 11.49), which is *inside* the 2.0 ATR swing floor in config/strategy.md. It should not have shipped that way. I am not widening it now — amending risk upward on an open losing position is the mirror of walking a stop in, and I refused that for DVN twenty minutes ago. It holds as published and the sub-floor stop is disclosed rather than quietly fixed.
- VST is the better vehicle for the same theme (improving vs deteriorating revisions, CEO buying vs one director, +8.43% vs XLU on 1m against CEG's +3.15%), which is why VST is today's new merchant-power capture and CEG is only a hold. Two positions on one driver is within the correlation cap of 3.

## [06:27 ET] POSITION UPDATE — TLT — SELL opened 2026-09-02 @ 81.87, last 81.80 — HOLD, unchanged, no candidate
- Thesis is intact and the macro reading reinforces it: US10Y **5.01%** against effective fed funds **3.88%** is a 113bp term premium at the long end. TLT is below SMA20 81.94, SMA50 82.56 and SMA200 85.83.
- Levels check out as published: stop 83.30 is **2.10 ATR** above the 81.87 entry (ATR14 0.68), clearing the 1.8 ATR ETF floor; reward-to-risk to the 78.00 target is 2.71.
- The honest caveat: TLT is only **1.67% above its 200-session low of 80.46**, so the 78.00 target requires a break to new lows rather than a move within the range. Yields fell on 09-21 (TLT +0.68%) alongside the crude break, which is the mechanism that most plausibly stalls this.
- Nothing changed; no candidate captured.

## [06:28 ET] CRYPTO — feed recovered on retry
- BTC **$86,059** (+1.8% 24h, $54.7B volume), ETH **$2,746.45** (+1.04%), SOL **$117.07** (+1.25%). source: coingecko via market_data.py crypto
- Relevant to prior_context: the `BTC` SELL @ 63,400 (published 08-16) and `/MBTU6` SHORT @ 64,340 (published 08-18) are awaiting entry **~26% below spot**. Those levels are stale to the point of being inert — BTC would have to fall a quarter to reach them. Flagging rather than re-pitching: I have no fresh bearish crypto thesis today, and moving a short entry up 26% to chase price would be exactly the reverse-engineering the strategy config forbids.
- No crypto candidate captured today. BTC at 86k with a +1.8% session and no dated catalyst I could source is not an edge, and /MBT would be the vehicle if it were.

## [06:29 ET] REJECTED — DAL, UAL — the fuel-cost short thesis is backwards right now
- I looked at airlines as a short on record distillate cracks (jet fuel is a distillate; inventories 14% below the five-year average). The tape says no: DAL +3.7% to 82.50 and UAL +5.2% to 114.39 on 09-21, the day crude fell 4.69%. The market is trading airlines as crude beta, and crude is falling.
- Both are also well off their highs (DAL -13.8%, UAL -17.6%) rather than extended, so there is no valuation cushion for a short either. Dropped.

## [06:32 ET] NEWS — JBHT warned on 2026-09-16 and fell 13.3% — the cleanest de-rating on the board
- At Morgan Stanley's 14th Annual Laguna Conference on **2026-09-16**, J.B. Hunt guided Q3 earnings **down 5-10% from Q2**. Stock fell 13.3% that session (273.05 -> 236.73) and dragged the trucking group with it.
  sources: https://www.cnbc.com/2026/09/16/jb-hunt-stock-jbht-earnings.html , https://seekingalpha.com/news/4643318-jb-hunt-sounds-the-alarm-on-costs-sending-trucking-stocks-lower
- Composition of the warning matters and is where most write-ups are sloppy: **$25M additional driver expenses** (recruiting, training, signing bonuses) and **$10M or more from fuel**. Fuel is under a third of it. The driver-cost piece is structural and does not go away when diesel does.
  source: https://www.benzinga.com/markets/guidance/26/09/61819951/jb-hunt-stock-sinks-as-rising-driver-and-fuel-costs-hit-q3-outlook
- The mechanism CFO Brad Delco described is the interesting part: JBHT passes fuel to customers via surcharges, **but the surcharges are delayed**, so the company carries the cost until the fees catch up. He called the recent moves "some of the most radical and abnormal swings" in fuel the company has experienced.
- **That lag is symmetric.** With crude now down four sessions to $95.59, surcharges set on lagged higher fuel keep collecting while the cost of the fuel actually burned falls. The same mechanism that produced the warning becomes a margin tailwind on the way down. I am not overstating it: it addresses the $10M fuel line, not the $25M driver line.
- Earnings bridge: Q2-26 actual was $1.91; down 5-10% is ~$1.72-1.81, against Q3-25 actual of $1.76. So the warning describes a roughly **flat year-over-year quarter**, and the market took 13.7% off for it.
- Surprise record is 4-for-4 beats: +7.88% (Q2-26), +1.36% (Q1-26), +2.73% (Q4-25), +17.79% (Q3-25). source: finnhub earnings-surprises
- Analyst revisions improving but far from crowded: 61.3% bullish, +1.3 — 8 strong buy / 11 buy / **11 hold** / 1 sell. Room to upgrade rather than a consensus long.
- **Against:** insiders 0 open-market buys against 7 sells (-$4.74M, six months); lagging SPY -15.38% (1m) and IYT -6.52% (1m), -8.04% (3m).
- Post-warning base, from fetched daily lows: 235.16 (09-16), 236.80 (09-17), 232.93 (09-18), **230.36 (09-21)**. Four sessions of tight consolidation, closes 236.73 / 236.80 / 234.25 / 236.17. Gap origin is 273.05; SMA50 271.28; SMA200 241.78 sits just above price.
- action: captured via add_candidate.py.

## [06:19 ET] CORRECTION — timestamps above drifted ahead of the wall clock
- The `[HH:MM ET]` stamps on the blocks above were written from my own sense of elapsed time and ran ahead of the real clock — the block labelled 06:32 was actually written at 06:18 ET. Run start was 06:01 ET. The ordering of the blocks is correct and every one was appended immediately as the finding landed; only the absolute minute is wrong, by up to ~14 minutes.
- Leaving the originals in place rather than rewriting them, and stamping from `date` from here on. Noting it because a research log whose times are quietly wrong is worse than one that says where it drifted.

## [06:22 ET] PATTERN — five of the sixteen open positions carry NO stop, and three of those are at 52-week lows
- Unstopped longs in prior_context: NKE, BCC, LCII, PFE, LULU. Of those, the three sitting at or near their 200-session lows are **NKE (-11.4%), LCII (-7.5%), LULU (-11.9%)**.
- This is one decision, not three coincidences: a long with no stop that is making new lows has undefined downside and no rule that will ever close it. Each is being exited today. BCC (-1.1%) and PFE (+0.5%) are also unstopped but are flat and not at lows, so they hold — with the flaw recorded below rather than ignored.

## [06:22 ET] POSITION UPDATE — LCII — BUY opened 2026-08-18 @ 94.00, last 86.95, -7.5% — CLOSE
- decision: **CLOSE the long.** No stop, new lows, and the worst relative strength on the board.
- LCII closed 86.95 against a 200-session low of **85.07** — 2.21% above it — and 45.5% below the high. Stacked below SMA20 96.44 / SMA50 101.82 / SMA200 116.91, all declining. The last eight closes are a straight line down: 99.11, 96.04, 93.40, 91.02, 90.19, 87.60, 87.11, 86.49, 85.60, 86.95.
- Relative strength is the clincher: **-45.25% vs SPY over six months, -30.16% vs XLY**, and still -18.97% / -13.73% over the last month. This is not a name that stopped falling.
- Fundamentals give no offsetting signal: Q2-26 was a **miss** (-3.60% vs estimate), and insider activity over six months is literally zero — no buys and no sells, so nobody inside is stepping in.
- The one thing in its favour: analyst revisions nominally improving (61.1% bullish, +2.3) — but that is 5 strong buy / 6 buy / **7 hold**, which is a split book, not support.
- Macro against it: LCII supplies RV and manufactured housing. US10Y at 5.01% is a direct demand headwind for financed big-ticket discretionary, and the target of 138 assumed a rate path that has not arrived.
- action: captured via add_candidate.py.

## [06:24 ET] INSIDER CLUSTER — CAG: three distinct buyers, zero sells, and the street at 4% bullish
- Fetched insider transactions, six-month window, **3 open-market buys by 3 DISTINCT buyers, 0 sells, $1,119,535 total**:
  - Brase John P — 35,000 sh @ $14.5895 — 2026-07-17
  - Mulligan John J — 17,500 sh @ $14.3087 — 2026-04-14
  - LENNY RICHARD H — 25,000 sh @ $14.3400 — 2026-04-14
  source: https://finnhub.io/api/v1/stock/insider-transactions
- Three separate people buying and nobody selling is the specific pattern the research brief singles out as predictive, and it is pointed at exactly the case it is supposed to be good for — telling a de-rated name that is cheap from one that is broken.
- Sentiment is at an extreme: **4.0% analyst bullish share** (improving, +0.2). A single-digit bullish share means essentially nobody on the street has a buy on it.
- Dated catalyst: **CAG Q1 FY27 earnings 2026-09-29**, est EPS 0.285 on rev 2.61B, verified on the fetched finnhub calendar.
- Levels (fetched): last 14.86, ATR14 0.4061 (2.73%), SMA20 15.52, SMA50 15.23, SMA200 15.75, 200-session range 12.53-20.32 (-26.9% off high). Recent swing low **14.305 on 2026-09-11** — which sits right on the Mulligan/Lenny cost basis of 14.31/14.34. Shelf of lows at 14.62-14.78 since.
- prior_context has CAG BUY awaiting entry @ 15.00 from 2026-09-20. **What changed:** price is now 14.86, below that level, and the stop/target have been set properly off the 14.305 swing low rather than left open. Re-pitching amends that pending entry, it does not open a second one.
- action: captured via add_candidate.py.

## [06:25 ET] KHC — same shape, weaker case, no candidate
- CEO Steven Cahillane bought **213,106 shares @ $23.4616 = $5.0M** on 2026-05-12 (1 buy, 1 sell, net +$4.57M). Larger dollar amount than CAG but **one buyer**, not a cluster, and four months stale.
- KHC last 24.37, above the 23.00 pending entry, below SMA20 25.02 / SMA50 25.42, just above SMA200 24.00. Analysts 7.1% bullish, improving.
- Not captured: the 23.00 pending level is unchanged and price has not reached it, and I have no dated catalyst inside the horizon for KHC the way CAG has 09-29. Leaving the pending entry as published rather than chasing it up 6%.

## [06:25 ET] POSITION UPDATE — LULU — BUY opened 2026-08-22 @ 115.00, last 101.30, -11.9% — CLOSE
- decision: **CLOSE the long**, completing the exit the 2026-09-08 SELL @ 100.61 already called for. This amends that exit rather than opening a second one.
- LULU is 101.30, 6.24% above its 200-session low of 95.35 and **55.2% below its high**, under SMA20 108.31 / SMA50 115.03 / SMA200 149.03. No stop on the position.
- The analyst book has collapsed: **5.0% bullish, -15.5 on the month** — 1 strong buy / 1 buy / **31 hold** / 5 sell / 2 strong sell. Seven outright sell ratings against two buys.
- Relative strength: **-57.04% vs SPY and -41.95% vs XLY over six months**, still -13.87% / -8.63% over one month.
- **The insider data here is a warning, not support, and this is the useful lesson of the morning.** LULU shows 3 buys by 2 buyers worth $1.99M — Bergh 6,090 @ $164.20 (03-20) and 4,275 @ $117.05 (06-15), Maestrini 3,275 @ $151.02 (04-01). Every one of them is heavily underwater at 101.30, and nobody has bought since June. An insider cluster is evidence that insiders think it is cheap; it is not evidence they are right. Contrast CAG, where the buys are at 14.31-14.59 against 14.86 spot — near the money and recent.
- action: captured via add_candidate.py.

## [06:26 ET] POSITION SWEEP — the remaining open positions, all HOLD, no candidates captured
Each was checked against fresh 09-21 closes and fetched history. None had a change material enough to warrant a recommendation, and I am not capturing "hold, unchanged" as a candidate — that would pad the report with rows that ask the reader to do nothing.

- **CCJ** BUY @ 94.00, last 93.23 (-0.8%), stop 82.50, target 135. Stop is 3.37 ATR below entry (ATR14 3.415) and R:R to target is 3.57 — both comfortable. Price is below SMA20 98.26 / SMA50 94.74 / SMA200 105.84 and -31.1% off the high. **Against it:** analyst revisions deteriorating, 81.8% bullish and -3.9 on the month. Also recommended 3x in the last 10 days per prior_context, so I am deliberately not writing a fourth pitch. Hold as published; if it deteriorates further it should be cut rather than re-argued.
- **BCC** BUY @ 76.50, last 75.66 (-1.1%), **no stop**. Flat for ten sessions (76.86 -> 75.66), below SMA20 77.19 / SMA50 79.06 / SMA200 77.27, -17.7% off high, 16.4% above the low. Thin at $22.6M/day. Unstopped, which is the flaw flagged at 06:22, but it is neither at its lows nor losing materially, so it holds. It should be given a stop the next time it is touched.
- **PFE** BUY @ 27.60, last 27.74 (+0.5%), **no stop**. Above SMA50 26.69 and SMA200 26.29, just under SMA20 28.04, only -5.0% off its high. ATR14 0.478 (1.72%) — the quietest thing in the book. Recommended **4x in the last 10 days**, the highest repeat count in prior_context, so it gets no fifth pitch today on principle. Hold.
- **EEM** BUY @ 65.60, last 68.83 (**+4.9%**, the best open position), stop 63.00, target 71.50. Closed +2.69% on 09-21 and is only 3.83% off its 200-session high; above SMA20 67.24 / SMA50 65.88 / SMA200 62.41. Target 71.50 is 3.9% away. Leaving target and stop alone — raising the stop to bank the gain is the KRE error, and raising the target because it is working is reverse-engineering. Hold.
- **GLD** BUY @ 398.00, last 398.38 (+0.1%), stop 381.00, target 437. Levels are sound: stop 2.20 ATR below entry (ATR14 7.71, ETF floor 1.8), R:R 2.29. Above SMA50 393.40, below SMA20 405.37 and SMA200 416.30, -21.8% off the 509.70 high. Hold.
  **CONFLICT TO FLAG:** prior_context also carries a pending `GLD` SELL @ 406.77 from 2026-09-08 against this open long with a 437 target. Those are contradictory instructions on one instrument — a sell order 8 points below the long's own target. Synthesis should reconcile them; I am not adding a third GLD instruction on top.
- **SVRA** BUY @ 5.35, last 5.45 (+1.9%), stop 4.60, target 8.00. The book's only micro cap. Liquidity clears the universe floor comfortably at $8.0M/day average dollar volume. Stop is 3.80 ATR below entry (ATR14 0.197) — appropriately wide for the class. Sitting between SMA20 5.40 and SMA50 5.49. Hold.
- **XLE**, **TLT**, **CEG** — decided above at 06:23 / 06:27 / 06:26. All hold.

## [06:27 ET] PENDING-ENTRY SWEEP — what to do with the 13 awaiting-entry rows
- **SNX** BUY @ 260.00 (pub 09-19) — **level unchanged, do not chase.** Price ran +5.05% on 09-21 to 279.59, 7.5% above the entry, two sessions before a **09-24 bmo** print. Beat record is excellent (+15.97%, +41.62%), but insider flow is **61 sells, 0 buys, net -$14.4M** over six months and revisions are flat at 82.4%. I built the levels a 260 entry would need — a 2.0 ATR stop lands at ~242 and the reward-to-risk to the 296.47 range high comes out at exactly **2.00**, sitting precisely on the swing floor. An idea that only just touches the floor is one the floor is meant to reject, so no candidate. Leave 260 pending.
- **MU** BUY @ 960.00 (pub 09-18) — level unchanged. Price 1043.96, 8.7% above entry; earnings **09-30 amc** confirmed on the fetched calendar. Recommended 3x in 10 days. Not chasing it up, not re-arguing it.
- **KHC** BUY @ 23.00 (pub 09-20) — unchanged, see 06:25.
- **CAG** BUY @ 15.00 (pub 09-20) — **amended today**, see 06:24.
- **DG** BUY @ 134.50 (pub 08-21) — **flag for validation:** DG closed 121.91 on 09-21 and has traded well below 134.50 for weeks, so a limit at that level should have filled long ago. prior_context still lists it as awaiting entry. Either the fill tracking missed it or the entry was never live; worth a look downstream. On the merits it is -22.9% off its high and below SMA20/50/200, so if it did fill it is a loser that needs a stop.
- **IYR** SELL_SHORT @ 103.60 (pub 09-02) — the view was right and the entry was unreachable. IYR never traded up to 103.60; it fell to 98.90 instead, -8.57% off its high and now resting on SMA200 100.05. Chasing the short down 4.5% after the move is how a good call becomes a bad trade. Leave it pending and let it expire.
- **BTC** SELL @ 63,400 and **/MBTU6** SHORT @ 64,340 — inert, ~26% below the 86,059 spot. See 06:28 crypto note.
- **GLD** SELL @ 406.77 — conflicts with the open GLD long; flagged above.
- **NKE** SELL @ 38.40 and **LULU** SELL @ 100.61 — these are the exits I am completing today with fresh captures at 36.10 and 101.30.
- **KXFEDDECISION-26SEP-H25 @ 32**, **-26OCT-H25 @ 28**, **-26SEP-H0 @ 47** — cannot be re-priced, the Kalshi feed returned zero markets for every term tried. Untouched rather than guessed. The 26SEP contracts also reference a decision that has already occurred.

## [06:29 ET] INSIDER SCREEN — ran the six-month insider window across 13 near-dated earnings names
Screened KMX, CCL, THO, KBH, DRI, ACN, JBL, KNX, CNXC, SFIX, FUL, MLKN, WOR. One hit, and it is the strongest positioning signal of the morning.
- **KMX — 6 open-market buys by 5 DISTINCT buyers, $1,268,037, ZERO sells.** All inside four days, 2026-06-22 to 06-25, at $52.01-53.39:
  - Barr Keith — 9,400 sh @ $53.005 — 06-22
  - Bensen Peter J — 2,500 sh @ $52.20 — 06-22
  - ONeil Mark F — 4,800 sh @ $52.36 — 06-24 (two filings)
  - Chawla Sona — 2,000 sh @ $53.39 — 06-25
  - Shinder Marcella — 574 sh @ $52.01 — 06-25
  source: https://finnhub.io/api/v1/stock/insider-transactions
- Five separate people buying in one week with nobody selling is a board-level cluster, not a personal liquidity event. At 57.86 they are ~9% up, so the signal has already begun working rather than sitting dead.
- **The analyst book capitulated alongside it.** Bullish share **28.0%, +20.9 points** — the largest revision swing in anything I looked at today. July stood at 2 strong buy / 1 buy / 17 hold / **7 sell / 1 strong sell**; September is 4 strong buy / 3 buy / 17 hold / **1 sell / 0 strong sell**. Eight bearish ratings became one.
- Surprise record: **+32.35%, +46.80%, +34.53%** in the last three quarters. Dated catalyst: earnings **2026-09-29**, est EPS 0.717 on rev 7.01B, fetched calendar.
- Levels: last 57.86, ATR14 1.792 (3.1%), SMA20 61.09, SMA50 59.39, SMA200 47.44, range 35.17-65.28 (-11.4% off high, +64.5% off low), $103.2M/day. Five sessions down from 61.69 to 57.21 before the 09-21 bounce.
- **The idea does not clear the risk floors at 57.86, and I am not bending them.** An honest stop goes below the whole insider cluster, i.e. under 52.01. From a 57.20 entry that is 51.50, a 3.18 ATR stop and 5.70 of risk, which needs a target above 68.60 — above the 65.28 range high. Pulling the stop up to 53.60 to make the ratio work puts it *inside* the cluster, stopping out exactly where five insiders bought, and still only reaches 2.03. Both are the reverse-engineering config/strategy.md forbids.
- **It works one level lower.** Entry 53.80 at the top of the insider band, stop 50.20 (2.01 ATR, below the whole band), target 64.50 under the range high: **R:R 2.97**. Captured that way, with entry conditional on the 09-29 print, rather than captured at a price that fails.
- Everything else screened clean or negative: KBH -$16.6M, KNX -$16.2M, DRI -$18.3M, JBL -$14.2M net insider selling; CCL, ACN, SFIX, WOR, FUL negative; THO and MLKN zero activity. CNXC showed 3 buys by 2 buyers but only $118K against -$133M net — not a cluster.

## [06:30 ET] INSIDER SCREEN, second batch — 14 more names, no further clusters
Screened AZO, PAYX, CTAS, FERG, FDS, JEF, CALM, AYI, LEU, USAR, DAL, UAL, AEHR, MDRX.
- Nothing qualified. AZO had 1 buyer ($492,855) but net -$4.19M; AYI had 2 buyers but only $340,746 against net -$727K. Heavy net selling at DAL (-$44.3M), AEHR (-$47.5M), UAL (-$38.4M). FERG, FDS, CALM and MDRX showed no insider activity in either direction.
- **ANOMALY, not traded: JEF reports 2 open-market buys by 1 buyer worth $628,739,636.** A $629M "open-market purchase" by a single insider is not a credible Form 4 code-P transaction at Jefferies' size; it is far more likely a parent/holding-company transfer or a unit-vs-dollar miscoding in the feed. I did not have time to verify it against the actual filing and **I am not capturing an idea on an unverified number** — flagging it here so it is on the record rather than silently dropped. If someone re-runs this, check EDGAR directly.
- Net result of both screens (27 names): two genuine clusters, **CAG** (3 distinct buyers, 0 sells) and **KMX** (5 distinct buyers, 0 sells). Both captured.

## [06:31 ET] SELF-CHECK — recomputed every captured candidate's arithmetic
Ran entry/target/stop/ATR back through the floors in config/strategy.md before finishing, because the report's own history is that these get nudged.
- Reward-to-risk vs floor: VST 2.90 (need 2.5), MP 2.64 (2.5), DINO 2.10 (2.0), JBHT 2.13 (2.0), CAG 2.24 (2.0), KMX 2.97 (2.0). All pass.
- Stop distance in ATRs vs the asset-class floor: DINO 2.06, JBHT 2.11, CAG 2.09, KMX 2.01 — all stocks, floor 2.0. All pass, none by more than 0.11 ATR of slack, which is the honest consequence of setting stops from structure first and checking the ratio second.
- Win probability vs the 1/(1+R:R) baseline: DINO +9.8pts, JBHT +10.0pts, CAG +13.1pts, KMX +14.8pts. All positive, none above the 20-point "large claim" line.
- NKE, DVN, LCII and LULU are exits with a null target, so reward-to-risk does not apply to them by construction.
- **One discrepancy I am leaving as-is and disclosing:** DVN carries 3 distinct evidence kinds, which under the conviction table supports a 4, and I wrote 3. It is an exit recommendation and I would rather under-claim than inflate; flagging it so the red team does not have to discover it.

## [06:32 ET] CORRELATION CHECK — no driver carries more than two captured ideas
- Merchant power / AI load: **VST** (new) + CEG (held) = 2. Under the cap of 3.
- US-China rare earths: **MP** only = 1.
- 2026-09-29 earnings prints: **CAG** + **KMX** = 2. Both are insider-cluster ideas and both report the same morning, which is a genuine shared risk even though the businesses are unrelated — worth stating rather than hiding behind "different sectors".
- Diesel: **DINO** and **JBHT** are on **opposite sides** of the same variable. DINO wants cracks wide; JBHT wants the fuel bill to fall. That is a hedge, not a doubled bet, but a reader sizing both should know they partly offset.
- Crude: the only crude-levered longs left after today are XLE (held, diversified) and DINO (refiner, inverse). DVN, the pure E&P, is being closed.
- Exits (NKE, LCII, LULU) share a *diagnosis* — unstopped long at 52-week lows — but they are not a correlated position.

## [06:33 ET] RESEARCH COMPLETE
- **candidates: 10 unique symbols** — 5 new/amended longs (VST, MP, CAG, KMX, JBHT), 1 position hold with a restated thesis (DINO), 4 exits (NKE, DVN, LCII, LULU).
- horizon skew: 8 swing, 2 long_term (VST, MP), **0 intraday**. Nothing intraday cleared the bar — with no live index, VIX or futures quotes this morning (see the macro data gap) I had no basis to set precise intraday levels, and inventing them would have been the worse failure. Stated rather than padded.
- asset-class skew: **all 10 are equities.** No crypto (no fresh thesis at BTC 86,059; the two pending shorts are 26% out of the money), no futures, and no event contracts (feed returned zero markets).
- coverage gaps:
  - **Index and macro market data unavailable all run.** Yahoo returned HTTP 429 for every index; Finnhub refuses indices without a subscription; Stooq 404s on ^-prefixed tickers; no AlphaVantage key. So: no SPX/NDX/DJI/RUT level, no VIX, no DXY, no /ES or /NQ, no spot gold or WTI quote from the tool. The crude and rates figures used today come from fetched news and FRED, and are sourced as such.
  - **Kalshi event-contract feed returned `count: 0` for all 12 macro terms tried.** The whole prediction-market lane is unscreened, including the three pending KXFEDDECISION contracts.
  - **Options-implied move unavailable** — `implied` returns HTTP 401 from yahoo-options, so no candidate was checked against what the straddle prices. This matters most for CAG and KMX, both of which sit in front of a 09-29 print.
  - **Short interest unavailable** — `short` timed out against api.nasdaq.com.
  - Did not reach: small/micro-cap hunting beyond the existing SVRA position, and no systematic screen below $2B market cap. The two clusters found (CAG, KMX) are both large caps because the screen was built off the earnings calendar rather than off size.
  - JEF insider anomaly unverified (see 06:30).
- sources that failed: query1/query2.finance.yahoo.com (429 on all history and index calls, 401 on options), finnhub index quotes (subscription), stooq (404 on index symbols), api.nasdaq.com `short` endpoint (timeout), api.nasdaq.com history for KMX (timed out once, succeeded on retry), Kalshi market search via market_data.py events (zero results), coingecko (failed on the first call, succeeded on retry).
- notes on method today: the highest-yield tool by a wide margin was `market_data.py insiders`. Across 27 screened names it produced two clean clusters (CAG, KMX) and confirmed the VST CEO purchase, and it also produced the most useful *negative* — LULU's insider buying, which reads as support until you notice every purchase is 15-60% underwater and four months stale.

## [06:35 ET] JEF ANOMALY RESOLVED — the $629M is real, and it is still a REJECT
Went back and verified the number I flagged at 06:30 rather than leaving it hanging.
- It is genuine and it is not a coding error. **Sumitomo Mitsui Financial Group (SMBC), which sits on Jefferies' board and therefore files Form 4s**, bought **6,429,337 shares on 2026-05-01** at a final adjusted $54.83 and **5,906,542 shares on 2026-07-15** at a final adjusted $54.86 — about 12.34M shares for roughly $677M, in open-market purchases.
  sources: https://www.sec.gov/Archives/edgar/data/0000096223/000119312526306696/ownership.xml , https://www.sec.gov/Archives/edgar/data/0000096223/000119312526360109/ownership.xml
- The purpose is disclosed: SMBC intends to raise its economic ownership to **up to 20%** on an as-converted fully diluted basis by buying **approximately 13 million shares** in the open market, under the Global Strategic Alliance between the two firms.
- **REJECTED — JEF — the buyer is not a value signal, is 12.7% underwater, and is nearly out of shares to buy.**
  1. This is a strategic stake-building programme on a pre-announced size, not an insider forming a view on price. It would have bought at $60 or $40 alike.
  2. It is **the LULU trap again, at institutional scale.** JEF closed 47.85 on 09-21 against SMBC's $54.83-54.86 — the buyer is down 12.7%. Insider buying is evidence somebody thought it was cheap, never evidence they were right.
  3. **The bid is almost exhausted.** ~12.34M of the ~13M planned shares are bought, leaving roughly 0.66M. Anyone buying JEF for the SMBC bid is buying the last 5% of it.
  4. Fundamentals point the other way: **two consecutive large earnings misses** — -27.51% (Q1-26) and -12.64% (Q2-26) — with analyst revisions deteriorating hard, bullish share 55.6% and **-14.4** on the month.
  5. The tape is a knife, not a base: 55.72 on 09-08 to 47.35 on 09-16, -15% in six sessions, now -28.15% off the high and below SMA20 51.86 / SMA50 53.84 / SMA200 53.26. Another print lands **2026-09-30** (est EPS 0.9474, rev 2.14B).
- Worth keeping on a watchlist for after 09-30: if the print is clean and it bases above ~44, a strategic holder at 20% with a 12% paper loss is a real floor-ish argument. It is not one today.

## [06:36 ET] REJECTED — MSS — the "7 insider buys" are a market maker, not management
- MSS screened as 7 open-market buys by 2 buyers, which looked like a cluster until I read it: six of the seven are **HRT FINANCIAL LP** (a quantitative market-making firm, a >10% holder filing Form 4s) at $1.33-1.42 on 08-10/12/13, totalling $58,105. The seventh is Xu John at $0.12.
- That is inventory, not conviction, and the total is too small to signal anything regardless. The stock also trades near $1.40, close to the universe's $1 exclusion floor. Dropped.
- Lesson worth recording for the screen: `distinct_buyers` counts entities, not executives. A >10% institutional holder or a market maker registers identically to a CFO. Check the names, not just the count — CAG's three (Brase, Mulligan, Lenny) and KMX's five (Barr, Bensen, ONeil, Chawla, Shinder) are people; MSS's are a trading desk.

## [06:37 ET] SMALL-CAP SCREEN — ran it, found nothing, which is an outcome not a gap
- Pulled the earnings calendar filtered to $20M-$300M revenue estimates inside 11 sessions and screened insiders across all of them: MANU, BXMT, SCHL, MTN, PRGS, BSET, ANGO, PKE, MSS, BTM.
- No qualifying cluster. BXMT had one buyer at $143K against three sells; SCHL -$14.3M, PKE -$9.4M net selling; MANU, MTN, BSET and BTM showed no insider activity at all; MSS rejected above.
- So the 06:33 coverage-gap line about small caps is **corrected**: the screen did run, it covered the small-cap names with dated catalysts inside the horizon, and it produced nothing that clears the bar. The remaining genuine gap is small caps *without* a near-dated earnings event, which this method cannot reach.

## [06:38 ET] RESEARCH COMPLETE — amended, supersedes the 06:33 block
The 06:33 block stands except where corrected here; I had budget left and kept working rather than stopping on a round number.
- **candidates: 10 unique symbols, unchanged** — VST, MP, CAG, KMX, JBHT (new/amended longs), DINO (hold, restated), NKE, DVN, LCII, LULU (exits). The extra 25 minutes produced two well-documented rejections rather than an eleventh idea, and that is the honest result: JEF and MSS both looked like insider clusters and neither survived reading the names on the filings.
- **Correction to the 06:33 gap list:** small caps WERE screened (see 06:37). The narrower true gap is small caps with no earnings inside 11 sessions.
- **Correction to the 06:30 note:** the JEF $628,739,636 figure is not a feed error. It is SMBC buying toward a 20% stake. Verified against the Form 4 and Form 4/A on EDGAR, and rejected on the merits at 06:35 rather than on suspicion of bad data.
- All other coverage gaps and failed sources from 06:33 stand: no index/VIX/DXY/futures quotes (yahoo 429, finnhub indices gated, stooq 404), no event contracts (Kalshi returned zero markets for 12 terms), no options-implied move (yahoo-options 401), no short interest (nasdaq timeout).
- Total run: 06:01-06:38 ET. Every candidate was captured the moment it was specified; the file never sat empty after 06:06.

## [06:40 ET] EVENT CONTRACTS — feed IS reachable; the tool's query is the problem, and the data changes the macro read
Went back at this after writing it off, and the lane is not dead — `market_data.py events` is querying it wrongly.
- **Diagnosis.** `events()` hits `https://api.elections.kalshi.com/trade-api/v2/markets` with a limit and filters client-side. That endpoint's default page is almost entirely sports, all with 0 bid / 1.00 ask, so a keyword filter over it returns nothing for every macro term — which is exactly the `count: 0` seen at 06:17. Passing **`series_ticker`** returns the real markets immediately. Fetching the bare endpoint independently reproduced the sports-only page, so this is the tool's query shape, not a Kalshi outage. Worth fixing in `scripts/market_data.py`.
- **Fetched, with a max_close_ts bound to reach 2026** (the unbounded query sorts to 2027-2028 meetings):

  | Ticker | Outcome | Yes bid/ask (cents) | Volume | Open interest | Closes |
  | --- | --- | --- | --- | --- | --- |
  | KXFEDDECISION-26OCT-H25 | Hike 25bps | **53 / 54** | 563,495 | 345,358 | 2026-10-28 |
  | KXFEDDECISION-26OCT-H0 | Maintain | 46 / 47 | 685,138 | 440,951 | 2026-10-28 |
  | KXFEDDECISION-26OCT-C25 | Cut 25bps | 0 / 1 | 515,110 | 396,270 | 2026-10-28 |
  | KXFEDDECISION-26DEC-H25 | Hike 25bps | **66 / 67** | 118,282 | 85,077 | 2026-12-09 |
  | KXFEDDECISION-26DEC-H0 | Maintain | 28 / 29 | 115,579 | 91,488 | 2026-12-09 |
  | KXFEDDECISION-26DEC-C25 | Cut 25bps | 1 / 2 | 85,750 | 66,648 | 2026-12-09 |
  source: https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXFEDDECISION
- **The market is pricing a HIKING cycle**: 53% for a 25bp hike in October, **67% by December**, and a cut is priced at essentially zero at both meetings. That is fully consistent with the morning's FRED reading — US2Y 4.76% sits 88bp above the 3.88% effective fed funds rate, which is the bond market pricing the same tightening.
- **No event candidate captured, deliberately.** config/universe.md requires an explicit probability disagreement, and I do not have one: 53% for October and 67% for December are close to what the 2-year already implies, so the contracts and the curve agree. Buying either would be paying for a consensus I share, which is a hunch dressed as a trade. The lane was screened, properly, and produced nothing — that is different from the 06:17 note and supersedes it.
- **Records fix for the three pending KXFEDDECISION rows:**
  - `KXFEDDECISION-26OCT-H25` YES @ **28** (published 09-02) — the market is now **53/54**. The view was right and the entry never filled; it is 25 cents out of the money in our favour, which means the opportunity is gone, not that the position is winning. Do not chase it at 53.
  - `KXFEDDECISION-26SEP-H25` YES @ 32 and `KXFEDDECISION-26SEP-H0` YES @ 47 — both reference the **September 2026 meeting, which has already passed**. They are not open markets and should be resolved out of the pending list rather than carried.
- No arbitrage in the ladder: October bids sum to ~99-100 and December asks to ~101, i.e. normal spreads.

## [06:41 ET] CROSS-CUTTING RISK the hiking data introduces — flagging, not re-capturing
A 53%/67% priced hiking path is a headwind that touches several of today's captures, and the honest thing is to name it in one place rather than quietly leave it out:
- **Confirms** the TLT short (held, unchanged) and the decision to close the rate-sensitive **LCII** long.
- **Argues against** the pending `IYR` short being cancelled — a hiking cycle is precisely the environment for it — but it still does not justify chasing the entry 4.5% down, so the 06:27 call stands.
- **Adds risk to KMX**, whose key_risk already names US10Y at 5.01%: used-vehicle affordability is a financing story and two more hikes make it worse. The 52.00-54.50 conditional entry and the wait=true flag are the right shape for that.
- **Adds risk to JBHT** (cyclical freight) and to **CAG** (a bond-proxy staple that de-rates as rates rise). Neither thesis depends on rates, but neither is helped.
- **Least affected:** VST and MP, whose drivers are contracted offtake and statute rather than the discount rate — though both are long-duration equities and would de-rate with the rest.
Red team should weigh this against CAG and JBHT in particular.

## [06:31 ET] TIMESTAMP CORRECTION (second) — stamped from `date` this time
- The drift flagged at "06:19" got worse, not better: the blocks labelled 06:40 and 06:41 were written at **06:30 ET**. Every stamp from here is taken from `date` rather than estimated. Run start was **06:01 ET**; this block is genuinely 06:31. Block ordering and the immediacy of each append are unaffected — only the absolute minutes on the estimated stamps are wrong, by up to ~11 minutes.

## [06:31 ET] REJECTED — /MCL crude futures short — the one lane I screened and deliberately left empty
Crude is the day's largest macro move and the universe config prefers a futures contract for a commodity view, so the absence of one needs a reason rather than silence.
- The bear case is real: WTI $95.59 on 09-21, -4.69% and a fourth consecutive down session, with the driver being a deflating war premium (Trump declining to strike Yemen, signalling openness to Iran diplomacy) plus OPEC and IEA both cutting 2026 demand outlooks.
- **Three reasons it is not captured:**
  1. **I have no fetched crude price.** Every quote path for WTI failed this morning — yahoo 429, finnhub indices gated, stooq 404. The $95.59 comes from news reporting, which is fine for framing a thesis and **not** fine for setting entry, target and stop on a leveraged contract that config/universe.md requires to carry a hard stop. Setting futures levels off a number I could not fetch is the precise thing CLAUDE.md forbids.
  2. **It is selling into the move.** Four sessions and roughly 8% have already gone; the premium has been coming out, not about to.
  3. **The tail is a headline.** Saudi Arabia's East-West pipeline is closed following attacks and exports are running through Hormuz. A single strike re-prices this overnight, against a leveraged short, in a market that trades while US equities do not.
- The crude view is already expressed properly elsewhere in the book without leverage: **DVN is being closed** (long crude beta removed) and **DINO is held** (refiner, which gains as feedstock falls). That is the same direction, taken in instruments I have real prices for.

## [06:31 ET] RESEARCH COMPLETE — final, supersedes the 06:33 and 06:38 blocks
Run: **06:01 - 06:31 ET**. Worked the full budget rather than stopping at the first complete-looking point; the last 30 minutes produced no new candidate and three documented rejections plus a tooling diagnosis, which is the honest return on that time.

- **candidates: 10 unique symbols**, all captured at the moment they were specified. First capture at 06:06, well inside the minute-20 deadline.
  - New / amended longs: **VST** (5), **MP** (4, wait), **CAG** (4), **KMX** (4, wait), **JBHT** (3)
  - Hold with restated thesis: **DINO** (3)
  - Exits: **NKE**, **DVN**, **LCII**, **LULU** (all 3)
- **Skew, stated rather than corrected:** 8 swing / 2 long_term / **0 intraday**, and **all 10 are equities**. No intraday idea cleared the bar because I had no live index, VIX or futures quote to set precise levels from. No futures, crypto or event-contract candidate — each of those lanes was screened and each is documented as empty with a reason, not skipped.
- **Four of ten are exits.** That is unusual and it is the finding: five of the sixteen open positions carried no stop, and the three of those sitting at 52-week lows (NKE, LCII, LULU) are all being closed. One more (DVN) sat 0.51 ATR from its stop with its driver broken.
- **Method note:** `market_data.py insiders` was by far the highest-yield tool — 37 names screened across three batches, producing VST, CAG and KMX. It was equally valuable negatively: LULU's buying is stale and underwater, JEF's $629M is a strategic stake not a view, and MSS's "cluster" is a market maker. **Read the names and the cost basis, never just the count.**
- **Rejections logged, with reasons:** VLO/MPC/PSX/PARR (parabolic), DAL/UAL (thesis backwards), JEF (stake-building, underwater, bid nearly exhausted), MSS (market maker), /MCL (no fetched price), SNX (R:R exactly 2.00), KHC, IYR, MU.
- **Tooling defect found and diagnosed, not fixed** (out of scope for this phase): `market_data.py events` returns zero macro markets because it filters the unfiltered Kalshi `/markets` page, which is sports-dominated. Passing `series_ticker` works. Leaving it to whoever owns `scripts/market_data.py`, with the reproduction in the 06:40 block.
- **Coverage gaps that remain real:**
  - No index / VIX / DXY / equity-futures / spot commodity quotes all run (yahoo 429 throughout, finnhub gates indices, stooq 404s on ^ symbols, no AlphaVantage key). Rates and crude figures come from FRED and fetched news, sourced as such.
  - No options-implied move on any candidate (yahoo-options 401) — matters most for CAG and KMX, both in front of 09-29 prints.
  - No short interest (api.nasdaq.com timeout).
  - Small caps **with** a near-dated earnings catalyst were screened and produced nothing. Small caps **without** one were not reached; that method gap stands.
- **Flagged downstream, needing someone else's decision:** the GLD long/pending-sell conflict (06:26), the DG pending entry that looks like it should have filled weeks ago (06:27), the two already-resolved September Fed contracts still listed as pending (06:40), and CEG's published stop at 1.91 ATR which is inside the config floor (06:26). I disclosed all four rather than quietly amending positions I did not open.
