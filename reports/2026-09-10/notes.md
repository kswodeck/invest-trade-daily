# Research log — 2026-09-10

## [06:03 ET] MACRO — rates, crypto, tape
Prices below are **prior-close (2026-09-09 16:00 ET)**; market is pre-open, so this is the freshest honest equity price, not stale data.
- US10Y 4.80% (FRED DGS10, 2026-09-08); US2Y 4.39%; 10y-2y +0.40 (2026-09-09); Fed funds effective 3.63% (2026-09-08) — source: https://fred.stlouisfed.org/series/DGS10
- Unemployment 4.1% (Aug 2026, unchanged); CPIAUCSL 332.813 (Jul 2026) — source: https://fred.stlouisfed.org/series/UNRATE
- Long end is the story: 10y 4.80% with funds at 3.63% = ~117bp of positive carry-adjusted term premium. TLT 81.73 (-0.57% on 9/09).
- Crypto weak: BTC $77,948 (-1.29% 24h), ETH $2,467 (-0.95%), SOL $101.06 (-2.41%) — source: https://www.coingecko.com/
- SPY 762.40 (-0.46% on 9/09), from 765.96 prev. XLE 65.31 (+0.83%) — energy the only green sector in the open book yesterday.
- GLD 403.35 (+0.91%) — new highs area; gold bid while long rates rise is the debasement/term-premium tell, not a growth trade.

## [06:03 ET] DATA GAPS
- market_data.py macro: spx/ndx/dow/rut/vix/es/nq/dxy/us10y-quote/gold/wti ALL failed (Yahoo 429 rate-limited, finnhub refuses indices without CFD sub, stooq 404). No VIX, no DXY, no index futures this run.
- Workaround: single-name and ETF quotes via finnhub work fine. Using ETF proxies for regime instead of index quotes.

## [06:06 ET] CALENDAR — dated events in the next 10 sessions
Source: finnhub earnings calendar via scripts/market_data.py earnings --days 9
- **2026-09-10 AMC — ORCL** (est EPS 1.78, rev $19.53B) — tonight, the biggest single-name catalyst in the window
- **2026-09-10 AMC — ADBE** (est EPS 6.20, rev $6.82B)
- 2026-09-10 AMC — CPRT (est 0.39, rev $1.16B)
- 2026-09-15 — GIS (est 0.72, rev $4.38B)
- **2026-09-16 — FDX** (est 4.05, rev $22.59B) — the global-freight read
- **2026-09-16 AMC — LEN** (est 1.31, rev $8.40B) — homebuilder read with the 10y at 4.80%
- 2026-09-22 AMC — KBH, AZO; 2026-09-22 bmo — THO
- Event contracts: `market_data.py events "Fed"` and `"CPI"` both returned **count: 0** from Kalshi. No event-contract prices available this run — cannot state an implied probability, so no event-contract idea can be honestly written today.

## [06:06 ET] LEVELS — indicator pulls (nasdaq, 120 bars to 2026-09-09)
- GDX 99.47 | ATR14 3.53 (3.55%) | SMA20 97.72 | SMA50 85.32 | 120d range 69.74–105.67 | -5.9% off high | $2.48B ADV
- ORCL 161.63 | ATR14 6.48 (4.01%) | SMA20 149.69 | SMA50 140.40 | 120d range 114.50–250.25 | **-35.4% off high** | $4.24B ADV
- XHB 99.23 | ATR14 2.01 (2.02%) | SMA20 104.96 | SMA50 107.14 | 120d range 93.57–117.91 | -15.8% off high | $179M ADV

## [06:06 ET] POSITION UPDATE — BCC — opened 2026-08-18 @ 76.50, now 75.93 (-0.7%)
- decision: CLOSE the long, flat exit, do not reverse to short
- why: the housing complex broke down under the position. XHB below SMA20/SMA50 and 6.1% off its 120d low; LEN 1.2% off its 120d low; DHI -18.7% off high. 10y at 4.80% vs funds 3.63% — the long end is not delivering the rate relief the thesis needed. BCC itself below SMA20 80.06 and SMA50 78.93.
- not a short: LEN's sell-side book is 2 strong_buy / 12 sell / 2 strong_sell (7.7% bullish) — the bear case is crowded and squeezes on any rate relief.
- action: captured via add_candidate.py (direction sell, exit in full)

## [06:07 ET] REJECTED — LEN short — thesis right, positioning wrong: 88% of the sell-side already at hold-or-worse (7.7% bullish share), revision_direction "improving", price 1.2% off the 120d low. Late.
## [06:07 ET] REJECTED — ORCL long into tonight's print — sell-side still 79.6% bullish after a 35% drawdown (15 strong_buy / 24 buy / 9 hold / 1 sell), revision_direction "deteriorating", and 12 insider sales worth $66.3M over six months with zero open-market buys. Crowded long + insider distribution into a 4.0% ATR name on earnings night is a coin flip against you.

## [06:10 ET] MACRO — THE REGIME: the market is pricing a Fed HIKE, and the long end has broken out
This reframes every idea below and is the single most important finding of the run.
- **10y Treasury ~4.85%, highest since October/November 2023.** It hit 4.818% on 2026-09-02 (highest since Nov 2023) and traded ~4.85% Thursday. FRED DGS10 last official print 4.80% (2026-09-08). — source: https://www.cnbc.com/2026/09/02/bond-yields-treasurys-inflation.html
- **Market-implied odds of a rate HIKE at the September FOMC ≈ 68%, up from ~40% a week earlier**, on rising oil and hawkish Fed commentary. Cut expectations are near zero. — source: https://www.cnbc.com/2026/09/08/us-treasury-yields-bonds.html
- **FOMC decision Wednesday 2026-09-16, 14:00 ET.** — source: https://www.financecalendar.com/fomc-meetings/
- **August CPI released tomorrow, Friday 2026-09-11, 08:30 ET.** Consensus headline +0.4% m/m / +3.4% y/y; core +0.4% m/m. Nowflation nowcast 3.34% headline y/y. — source: https://www.kiplinger.com/investing/economy/cpi-report-august-2026-what-to-expect
- Drivers named: inflation ~3.4%, fiscal deficits, heavy Treasury issuance, corporate borrowing, rising oil. Strategists flag a sustained break above 4.8% as causing "meaningful problems" across other asset classes. — source: https://www.cnbc.com/2026/09/07/us-treasury-yields-markets-scott-bessent.html
- Curve 10y-2y +0.40 and funds 3.63%: the front end has not moved yet, so the whole repricing is term premium and inflation, not growth.
- Consistency check against the tape: gold at highs (GLD 403.35) **while** nominal yields make multi-year highs is the fiscal/debasement signature, not a growth trade. Crypto weak (BTC 77,948 -1.3%). SPY 762.40 rolling over. XLE +0.83%, the only green thing in the book.

### What this rules IN and OUT for today
- OUT — long duration in any form. A 10y at fresh multi-year highs is the literal invalidation of a TLT long.
- OUT — shorting rate-sensitives (homebuilders, REITs). Right thesis, crowded trade: LEN's book is 7.7% bullish and it sits 1.2% off its 120d low. Squeeze risk on any soft CPI.
- IN — the CPI print tomorrow 08:30 ET and the FOMC 09-16 are the two dated catalysts everything should be orchestrated around. Most ideas today should say WAIT for the print rather than front-run it.
- GAP — Kalshi returned count:0 for both "Fed" and "CPI". The cleanest expression of a 68%-implied hike is an event contract and **I cannot price one honestly this run.** No event-contract idea today; recorded for data_quality_notes.

## [06:12 ET] MACRO — the engine: WTI $97 on a US-Iran shooting war
This is the cause of the yield/hike repricing above, not a separate story.
- **WTI crude $97.19 on 2026-09-09, +4.47% on the day, highest since May.** — source: https://tradingeconomics.com/commodity/crude-oil
- Drivers, all supply-side and geopolitical: Iran-backed Houthi militants attacked several Saudi energy facilities, forcing a temporary suspension of some operations; US officials say Iran attempted to attack Navy ships Monday after targeting an aircraft carrier with ballistic missiles over the weekend; Middle East total exports constrained with production shut-ins; China restocking dwindling inventories. — source: https://fortune.com/article/price-of-oil-09-09-2026/
- Causal chain for today: Middle East supply shock -> WTI $97 -> headline CPI consensus +0.4% m/m -> hike odds 68% -> 10y 4.85%. One driver, four markets. **Correlation cap applies hard today** — most of what looks like four ideas is one bet on the oil price.

## [06:12 ET] LEVELS — energy complex (nasdaq, to 2026-09-09 close)
- USO 149.97 | ATR 4.09 (2.72%) | SMA20 134.06 | SMA50 125.55 | range 102.42–154.08 | **-2.7% off high, +46.4% off low**
- XLE 65.31 | ATR 1.15 (1.77%) | SMA20 63.32 | SMA50 59.66 | range 52.62–65.915 | **-0.9% off high** | $1.72B ADV
- CVX 213.81 | ATR 3.89 (1.82%) | SMA20 204.84 | SMA50 192.83 | range 164.78–215.28 | -0.7% off high | $1.70B ADV
- XOM 164.23 | ATR 3.41 (2.08%) | SMA20 161.69 | SMA50 154.01 | range 134.95–176.41 | **-6.9% off high** | $2.30B ADV — the laggard of the majors
- XLF 57.06 | ATR 0.69 (1.20%) | SMA20 57.80 | SMA50 57.00 | -2.6% off high — banks NOT rallying on the hike repricing
- KRE 73.45 | ATR 1.09 | SMA20 75.13 | SMA50 75.59 | -6.3% off high — below both averages. Prior KRE long stopped out 2026-08-19; nothing here says try again.
- Divergence worth noting: crude +46% off its low while XLE is +24% and XOM is still 6.9% below its own high. The equities have not marked the oil move to market.

## [06:19 ET] DEFENSE — the anomaly, researched, and why it is NOT a trade
The complex is at/near 120-day lows during a shooting war: ITA 219.45 (-14.5% off high, only 4.8% off its LOW, below SMA20 236.09 and SMA50 239.26), LMT 524.46 (-18.1%), NOC 515.57 (-29.2%), RTX 197.55 (-12.9%). All four below both averages.
Cause is known and is not a mystery to be arbitraged:
- **"US defense stocks see no Iran war lift after early surge"** — the pattern is six months old, not a fresh dislocation. — source: https://www.militarytimes.com/news/your-military/2026/04/02/us-defense-stocks-see-no-iran-war-lift-after-early-surge/
- **No finalized defense appropriations bill.** Pentagon/prime framework agreements cannot be fully funded; continuing resolutions push revenue right and compress visibility. This is the same fiscal knot driving the 10y to 4.85%. — source: https://www.tikr.com/blog/lmt-defense-stocks-drop-as-white-house-summons-pentagon-officials-and-prime-contractors-to-address-domestic-munitions-shortages
- Program charges are real, not optical: NOC took $477M on B-21, $68M on Stand-in Attack Weapon, $91M on the GEM 63XL rocket motor after a launch anomaly forced a redesign. RTX warned tariffs could cut operating profit by up to $850M. — source: https://www.insidermonkey.com/blog/why-did-northrop-grumman-noc-fall-after-raising-its-2026-forecast-1803659/
- LMT is the quality case: FY26 guidance EPS $29.95–$30.65 and FCF $7.0–7.2B; record Q2 backlog $230.4B, +$36.8B YTD including a $35B THAAD award, ~30% converting to revenue within 12 months; Q2 segment operating profit +$1.6B on the Missiles and Fire Control munitions ramp; Q2 EPS beat 10.5% ($7.94 vs $7.18). Analyst book improving — 46.4% bullish, +7.1pts, 13 buy/strong-buy vs 14 hold vs 1 sell. — source: https://news.lockheedmartin.com/2026-07-23-Lockheed-Martin-Reports-Second-Quarter-2026-Financial-Results

## [06:19 ET] REJECTED — LMT long_term — fails the 2.5 reward-to-risk floor on its own arithmetic, and I will not soften the bear case to fix it
- Valuation anchor (bull): 20x an estimated ~$33 2028 EPS = **$660**. Backed by guided FY26 EPS $30.30 midpoint, record $230.4B backlog and the munitions ramp.
- Bear case: appropriations gridlock persists, charges recur, F-35 deliveries slip; EPS stalls near $28-30 and the multiple sits at 14x = **$425**. Plausible — primes do trade 13-14x in a procurement winter.
- At 524.46: reward 135.5, risk 99.5, **R:R 1.36**. At a 495 wait-entry: reward 165, risk 70, R:R 2.36 — still short, and 495 is a reflex discount rather than a level.
- The only ways to pass are lifting the bear to ~470 or the target to ~$700. Both are the "nudged until it passed" failure this report has already shipped once. **LMT is a fair price for a good business, not a mispricing.** Watchlist, not a recommendation.
- Insiders: 0 open-market buys at LMT in six months (11 sales, but only $118K total — noise). Nothing confirming from the inside.
## [06:19 ET] REJECTED — NOC/RTX/ITA — same fiscal cause, worse execution record (NOC three separate charges), and no cheaper entry than LMT on the numbers I could defend.

## [06:19 ET] REJECTED — refiners VLO / MPC / DINO — right thesis, fully paid. VLO 388.95 is 0.06% off its 120d high after +81% off the low; MPC 399.44 is -0.6% off high after +89.6%; DINO 108.14 is -1.6% off high after +95.1%. The pending DINO BUY @ 99.50 (published 2026-08-22) never filled and price ran 8.7% past it. Buying a doubled crack-spread trade the day after a +4.5% war spike is chasing a geopolitical premium that unwinds on one de-escalation headline.
## [06:19 ET] REJECTED — XOM long — the laggard major (-6.9% off high) but the natural target IS that prior high 176.41, giving reward 12.18 against a 7.73 stop = R:R 1.58, under the 2.0 swing floor. Widening the stop below SMA50 (153.0) makes it worse, not better.

## [06:14 ET] CORRECTION to the 06:03 MACRO block
I wrote "GLD 403.35 — new highs area". **That is wrong.** GLD's 120-day range is 363.32–448.70 and 403.35 is **-10.1% off its high**, sitting *below* its SMA20 409.87 and above its SMA50 390.09. Gold pulled back hard from 448.70 and is rebuilding, it is not breaking out. The debasement read still holds directionally (gold well above its SMA50 while nominal yields make multi-year highs) but nothing today should be written as "gold at highs".

## [06:14 ET] LEVELS — open positions (nasdaq, to 2026-09-09 close)
- TLT 81.73 | ATR 0.63 (0.77%) | SMA20 82.35 | SMA50 83.19 | range 81.17–87.79 | **0.69% off its 120-day LOW**
- GLD 403.35 | ATR 7.98 (1.98%) | SMA20 409.87 | SMA50 390.09 | range 363.32–448.70 | -10.1% off high
- SPY 762.40 | ATR 5.45 (0.72%) | SMA20 768.29 | SMA50 758.02 | range 629.28–779.37 | -2.2% off high
- SVRA 5.415 | ATR 0.207 (3.82%) | SMA20 5.458 | SMA50 5.629 | range 4.695–6.475 | -16.4% off high | ADV only $7.9M
- LULU 99.72 | ATR 6.13 (6.14%) | SMA20 116.39 | SMA50 117.82 | range 97.55–170.20 | -41.4% off high, 2.2% off LOW
- NKE 37.35 | ATR 1.01 (2.69%) | SMA20 39.43 | SMA50 41.37 | range 36.85–54.22 | -31.1% off high, 1.4% off LOW
- CCJ 100.41 | ATR 4.20 (4.18%) | SMA20 100.16 | SMA50 95.28 | range 83.15–131.21 | -23.5% off high — sitting exactly on its SMA20, still above SMA50

## [06:14 ET] CALENDAR — no clean dated energy catalyst inside the window
- **No OPEC+ ministerial meeting in September 2026.** The 41st ministerial was 2026-06-07; JMMC meets bi-monthly with no confirmed September date. — source: https://www.opec.org/pr-detail/243582-30-november-2025.html
- **EIA Short-Term Energy Outlook was released yesterday, 2026-09-09; next is 2026-10-06** — outside the window. — source: https://www.eia.gov/outlooks/steo/release_schedule.php
- So for energy the only dated events inside 10 sessions are the macro ones: CPI 2026-09-11 08:30 ET (energy is the swing factor in headline) and FOMC 2026-09-16 14:00 ET. Energy ideas today therefore carry a macro catalyst, not a sector one — stated rather than dressed up.

## [06:16 ET] POSITION UPDATE — LULU — opened 2026-08-22 @ 115.00, now 99.72 (-13.3%)
- decision: CLOSE. Reiterates the 2026-09-08 exit at 100.61; level effectively unchanged, but the *reason* is now on the record rather than technical.
- why: 2026-09-03 Q2 + **third FY2026 guidance cut of the year**. FY revenue $10.35-10.50B from $11.0-11.15B; FY EPS $9.48-9.73 from $10.95-11.15. Q3 revenue guided $2.29-2.32B = **-10% to -11% y/y** vs $2.53B consensus. Q2 revenue -4% to $2.4B (missed $2.46B). The $2.92 EPS "beat" vs $1.82 included $0.86 of tariff refunds/interest — ex-that, ~$2.06. Shares -18% after hours to an 8-year low. Incoming CEO Heidi O'Neill.
- action: captured via add_candidate.py — source: https://finance.yahoo.com/markets/stocks/articles/lululemon-shares-fall-17-fy2026-094142265.html

## [06:16 ET] REJECTED — NUVL (Nuvalent) — a real dated catalyst I cannot price
- The FDA PDUFA for zidesamtinib (ROS1+ NSCLC) is **2026-09-18**, squarely inside the window. — source: https://www.rttnews.com/corpinfo/fdacalendar.aspx
- But **no price is obtainable from any source**: finnhub returns all zeros, yahoo 429s, stooq 404s. Analyst coverage freezes at 2026-07-01 and the book collapsed from 23 buy/strong-buy in June to 8 with 15 holds in July — the signature of an announced acquisition, not of a live trading stock.
- No live price means no honest entry, target or stop. **Rejected on rule 2, not on the thesis.** If it is still listed and tradeable it is worth revisiting; do not carry my inference that it was acquired forward as fact.

## [06:16 ET] HOLDS — no change, no candidate emitted
- `CCJ` BUY @94.00, now 100.41 (+6.8%). Sitting exactly on SMA20 100.16, above SMA50 95.28, -23.5% off its high. Uranium/nuclear is the one driver in this book uncorrelated with the oil-and-rates shock. Nothing changed. Hold, target 135 intact.
- `GLD` BUY @398.00, now 403.35 (+1.3%). Above SMA50 390.09, below SMA20 409.87. Gold firm while nominal yields make multi-year highs is the fiscal/debasement read holding. Hold. (A GLD SELL @406.77 from 2026-09-08 is also pending and unfilled — that is a trim level, not a reversal.)
- `SVRA` BUY @5.35, now 5.415 (+1.2%), stop 4.60. Below SMA20 5.458 and SMA50 5.629, ADV only $7.9M. Marginal, but the stop is 15% away and intact and nothing new landed. Hold on the stop.
- `SPY` SELL_SHORT @773.00, now 762.40 (+1.4%), target 750, stop 783.50. Working, and 68% implied hike odds plus CPI tomorrow support it. Target 750 sits just under SMA50 758.02 — a real level. **Hold as written; I am deliberately not stretching the target now that it is winning**, which is the goalpost-moving this report has shipped before.

## [06:20 ET] CAPTURED — QCOM buy, long_term, conviction 5 — the best idea of the run
- Read the **8-K filed 2026-09-08** (agreement dated 2026-09-03) directly on EDGAR. Verbatim terms: warrant for "up to an aggregate of 25,000,000 shares" at "an exercise price of $161.26 per share"; vesting "tied to the execution of certain commercial arrangements, the placement of binding purchase orders and actual purchases of QTI's server chip products, technology, systems and manufacturing services by Amazon"; "up to a maximum amount of $60 billion in payments"; and **"3,750,000 shares being vested upon issuance of the Warrant based on initial purchase commitments"**. — source: https://www.sec.gov/Archives/edgar/data/804328/000110465926105718/tm2623289d1_8k.htm
- **Worth flagging for anyone re-checking this:** the 2026-09-08 press release itself contains NO warrant terms, no dollar commitment and no timeline. I fetched it specifically to test that, and every tradeable number here comes from the 8-K. A story sourced only to the release cannot support this thesis.
- Valuation: TTM EPS ~$11.36 (3.00/3.50/2.65/2.21) = **15.5x** at 176.40. Target $300 ~19x an estimated ~$16 FY29 EPS. Bear $130 ~13x an impaired ~$10 EPS — and 121.99 is the actual 120-day low, printed before this deal existed. R:R (300-174)/(174-130) = **2.86**, clears the 2.5 long_term floor at the accumulation entry without moving either anchor.
- Positioning is the reason this is still available: only 40.8% bullish, **26 of 49 analysts still at hold**, improving +4.1pts. RS turned — +7.91pts vs SMH on 1m after -11.30pts on 3m.
- Invalidation (not a price): two consecutive quarters with no disclosed server/datacenter revenue line, or an 8-K reporting forfeiture/expiry of unvested warrant tranches.

## [06:20 ET] CAPTURED — HAL buy, swing, conviction 4 — the services laggard
- entry 37.13 (zone 36.00-38.20), stop **34.00** (below SMA50 34.20) = 3.13 risk = **2.83 ATR**, target **43.59** = the 120-day high. R:R 2.06 vs the 2.0 swing floor. Stop set FIRST from the SMA50, then the target checked — not reverse-engineered.
- win_probability 0.42 against a 1/(1+2.06) = 0.327 baseline: a 9.3-point claimed edge, deliberately modest.
- Honest weaknesses, all in key_risk: no services-specific dated catalyst in the window, sell-side already 76.5% bullish, $17.7M of insider sales and zero open-market buys.

## [06:20 ET] REJECTED — XLE — the pending BUY @ 63.90 (published 2026-08-15) is stale and should not be re-pitched at a new level
XLE closed 65.31, **0.9% off its 120-day high** of 65.915, having run 2.2% past that unfilled entry. The driver did change materially (WTI $97 on the Iran war), which would normally justify a re-pitch — but there is no honest target left: the natural resistance IS the high the price is already touching, so any target is an extension and any stop wide enough to clear the ETF's 1.8 ATR floor kills the ratio. XLE has now been recommended 4x in ten days; the anchoring guard applies and I am not making it 5. HAL expresses the same view from the one part of the complex that has not repriced.
## [06:20 ET] REJECTED — insurers (MET, PRU, LNC, CB, AIG) — a good multi-year thesis with no entry today
Higher-for-longer reinvestment yields are a genuine structural tailwind to float and spread income, and it is a driver uncorrelated with the oil trade. But the market is not paying for it and I could not find a level: MET 95.69 is pinned between SMA20 96.18 and SMA50 94.72; PRU 117.59 and CB 337.62 and AIG 75.03 are all below both averages, AIG only 4.0% off its 120-day low. A thesis with no confirming tape and no support to lean on is a watchlist item, not a recommendation.

## [06:23 ET] CORRECTION #2 to the 06:03 MACRO block — "Crypto weak" was wrong
I called crypto weak off a single -1.3% day. The structure says the opposite. IBIT (spot BTC ETF, the cleanest proxy with real OHLC) closed 44.29, **above** its SMA20 41.98 and SMA50 38.47, only **4.9% off its 120-day high** of 46.56 and 34.9% above the 32.84 low. BTC $77,970. Bitcoin is in an uptrend, not weak — a down day is not a downtrend and I should not have written it that way.

## [06:23 ET] REJECTED — bitcoin short, and the two pending bearish crypto ideas are stale
- A short fights a live uptrend: BTC is above both averages and near its high.
- The arithmetic also refuses it from the long side. At 77,970 with a 3.48% ATR, the 2.5 ATR crypto floor forces a stop near 71,000 (2.57 ATR), and a 2.0 R:R then needs ~91,900 — **12% above the 120-day high**, i.e. an extension rather than a level. Same failure mode as XLE. No BTC idea today in either direction.
- **`BTC` SELL @ 63,400 (published 2026-08-16) and `/MBTU6` SHORT @ 64,340 (published 2026-08-18) should be treated as dead.** Both sit ~18% below spot, both were bearish calls into a rally that never came back to them, and /MBTU6 is a September contract now near expiry. They are not "awaiting entry", they are wrong and stranded.

## [06:23 ET] MACRO — a timing point that cuts against my own positioning, recorded deliberately
Tomorrow's print is **August** CPI. The 4.47% spike to WTI $97.19 happened on **2026-09-09** and is therefore NOT in it; the bulk of the Iran/Houthi supply shock lands in the September CPI released in October. August did carry elevated crude — Middle East exports were already constrained through the month — so the print is not clean, but the market has moved hike odds from ~40% to ~68% substantially on a shock that tomorrow's data mostly cannot show.
- Consequence: a benign August headline is a live possibility, and it would hit the TLT exit and the open SPY short at the same time. That risk is written into the key_risk of both rather than smoothed over.
- I deliberately did NOT trade this. Buying duration into the print one line after recommending the TLT long be closed would be a whipsaw, not a view, and the structural break in the long end is a separate and slower fact from one month of data.

## [06:23 ET] CAPTURED — URA buy, swing, conviction 3 — commodity at a 10-month high, equities de-rated
- Uranium spot **$89.65/lb (2026-09-08)**, +3.28% 1m, +16.81% y/y, a 10-month high, with $85-95/lb modelled through 2026. — source: https://tradingeconomics.com/commodity/uranium
- The whole equity complex lags it: URA -20.5% off its high, UEC -31.1%, LEU -22.8%, NLR -18.3%, CCJ -23.5%. Sector-wide, not one broken name.
- entry 46.86 (45.50-47.50), stop **42.80** below SMA50 43.18 = 4.06 risk = **2.35 ATR** (floor 1.8 for an ETF), target **58.97** = the 120-day high. R:R 2.98. win_probability 0.35 vs a 0.251 baseline.
- Flagged in key_risk: **overlaps the open CCJ long on the same driver** — size the pair together. Two positions on one uranium view is one position with extra steps.
- Policy backing that has already moved money: $2.7B DOE domestic enrichment investment; Cameco/Brookfield-Westinghouse term sheet with the US government for at least $80B of new reactor construction.
## [06:23 ET] REJECTED — LEU — the direct US enrichment play and the right policy story, but the numbers refuse it: at a 6.93% ATR the stop must sit near 153.00 (2.26 ATR), and against the 235.00 prior high that is R:R 1.88, under the 2.0 swing floor. Widening the stop makes it worse. URA carries the same thesis with a ratio that clears honestly.
## [06:23 ET] REJECTED — UEC — would be a third position on the uranium driver, hitting the correlation cap exactly, and it is the weaker chart of the two (below its SMA20 11.92 where URA is above). URA is the better vehicle for the same view.
## [06:23 ET] REJECTED — GDX — gold miners, 99.47, but the stop has to go below the SMA20 at 92.50 (1.97 ATR) and the only real target is the 105.67 prior high, giving R:R 0.89. Fails outright. The gold view stays expressed through the open GLD long.

## [06:26 ET] REJECTED — the whole small-cap earnings slate. None cleared the bar, and the reason is uniform.
Pulled every name on the fetched 9-day calendar under ~$1B revenue. All five are already bombed out and sitting on their lows, which makes them bad shorts (squeeze risk into a print) and bad longs (a binary print inside a downtrend):
- `PLAY` 8.19 — -45.5% off high but **1.8% off its 120-day LOW**, below SMA20 9.57 / SMA50 10.09, ADV only $12.6M. Reports 2026-09-14 amc.
- `SHOE` 12.93 — -35.0% off high, **2.4% off its low**, ADV $9.5M. Reported this morning bmo, so it is already untradeable on this report.
- `FPS` 30.99 — **-53.1% off high**, below SMA20 33.23 and SMA50 37.50. Reports 2026-09-15 bmo.
- `CBRL` 51.145 — -15.1% off high but +94.1% off its low, below both averages. Reports 2026-09-14 bmo.
- `LUXE` 7.30 — **ADV $798K**, barely over the $500K exit floor and effectively untradeable at any useful size. Reports 2026-09-16 bmo.
**No small-cap idea today.** The report wants this lane and I hunted it deliberately; it was empty. Recording that rather than forcing one in at 1%.

## [06:26 ET] NO INTRADAY IDEAS — deliberate, not an oversight
The day's only dated catalyst is tomorrow morning's CPI at 08:30 ET, which is after today's session. There is no 8:30 print today, no overnight gap worth fading, and no earnings reaction to trade — ORCL and ADBE report tonight, after the close. An intraday idea today would be a general lean dressed up as a setup.

## [06:26 ET] WHY THE COUNT IS SEVEN AND WHY FOUR OF THEM ARE EXITS
Not thinness of research — a structural feature of today's tape, and worth saying explicitly rather than apologising for.
- **One shock is driving four markets.** Middle East supply loss -> WTI $97 -> inflation -> 68% implied hike odds -> 10y 4.85%. The correlation cap bites hard: most of what looked like separate ideas was one bet on the oil price.
- **Almost everything is at an extreme, and extremes are where reward-to-risk dies.** Energy (XLE, CVX, VLO, MPC, DINO, FRO) is at or within 2% of its 120-day high, so every target is an extension with no level to name. Defense, housing, discretionary, utilities and the small-cap slate are at or near their lows, so every short is late and every long is a knife. Six ideas were rejected on arithmetic alone — XLE, XOM, LMT, LEU, GDX, BTC — and in each case the failure was the same: no defensible target left between the price and the nearest real level.
- **The open book was carrying three broken theses** (TLT on duration, BCC on housing, LULU and NKE on consumer turnarounds), and closing them is the highest-value work available today. Position management is the first obligation, not the residue after idea-hunting.
- Constructive ideas are diversified by driver as required: QCOM (AI datacenter silicon), HAL (oil services), URA (uranium/nuclear). No two share a driver, and URA's overlap with the open CCJ long is flagged on the idea itself.

## [06:27 ET] RESEARCH COMPLETE
- candidates: **7 distinct symbols in 8 lines** (BCC captured twice — the second line corrects its conviction from 3 to 4 to match its three evidence kinds; synthesis takes the last entry per symbol)
  - Exits / position updates: `BCC` sell (conv 4), `TLT` sell (conv 4), `LULU` sell (conv 4), `NKE` sell (conv 3)
  - New positions: `QCOM` buy long_term (conv 5), `HAL` buy swing (conv 4), `URA` buy swing (conv 3)
  - Holds with no candidate emitted, reasoned in the 06:16 block: `CCJ`, `GLD`, `SVRA`, `SPY` short
- coverage gaps:
  - **No event-contract idea was possible.** Kalshi returned `count: 0` for both "Fed" and "CPI". With hike odds at 68% and a CPI print tomorrow, an event contract was the single cleanest expression available today and I could not price one without inventing a number.
  - **No index or futures quotes all run.** spx/ndx/dow/rut/**vix**/es/nq/**dxy**/gold/wti all failed in `market_data.py macro`. No volatility or dollar reading informed any idea today; ETF proxies were substituted for regime reads.
  - No options-implied move for any finalist — `implied` returned HTTP 401 from yahoo-options on HAL.
  - `NUVL` has a real 2026-09-18 PDUFA and no obtainable price from any source; rejected on rule 2, not on the thesis.
  - No small-cap and no intraday idea, each for the documented reasons above rather than for lack of looking.
- sources that failed: yahoo (429 rate-limited throughout, and 401 on the options endpoint), finnhub indices (CFD subscription required), stooq (404 on all index symbols), alphavantage (no api key), kalshi (empty result set), nasdaq short-interest (read timeout on ORCL), cnbc.com (403 to WebFetch — search snippets used instead, and cited as such)
- prices: every figure in this log is the **2026-09-09 16:00 ET close** unless stated otherwise. The market was pre-open throughout this run, so that is the freshest honest equity price, not stale data. Crypto and uranium spot carry their own stated timestamps.
- two self-corrections are recorded above and stand: GLD is **not** at new highs (-10.1% off its 120-day high), and crypto is **not** weak (IBIT above both averages, 4.9% off its high).
