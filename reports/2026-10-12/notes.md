# Research log — 2026-10-12

## [06:03 ET] MACRO — rates, regime, and data availability
- Run start 2026-10-12 06:00 ET (Monday). Columbus Day: US equity markets open, US bond market closed (no cash Treasury trading) — so rate-sensitive moves today are futures/ETF-driven only.
- FRED (fetched): US10Y **5.22%** (as of 2026-10-08), US2Y **4.75%** (2026-10-08), fed funds effective **3.88%** (2026-10-08), 10y-2y curve **+0.44** (2026-10-09), unemployment **4.2%** (2026-09-01). Source: https://fred.stlouisfed.org
- A 5.22% 10y against a 3.88% policy rate is a steep, term-premium-driven curve — long end selling off while the front end is anchored. That is a headwind for long-duration equities and REITs, a tailwind for bank NIM (XLF already held).
- `bonds_20y` (TLT) 77.98, +0.14% pre, via finnhub. Consistent with the TLT short already awaiting entry at 79.90.
- **DATA GAP:** Yahoo Finance is returning HTTP 429 (rate limited) for every index/ETF symbol this morning, and finnhub refuses index CFDs. So ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES/NQ futures, DXY, gold and WTI all returned `ok: false`. Index-level context today is inferred from FRED + individual quotes, not from a fetched index print. Recorded for `data_quality_notes`.

## [06:08 ET] MACRO — the dominant driver today is Middle East oil supply risk
- Friday close (finnhub, asof 2026-10-09T20:00Z): SPY 778.57 (+0.60%), QQQ 751.27 (+0.49%), XLF 54.73 (+0.92%), XLE 65.08 (-0.25%). These are **Friday closes on a closed market**, not live prices.
- **Houthi strikes on Saudi Arabia escalated over the weekend.** King Khalid International Airport in Riyadh was struck again Sunday 2026-10-11, a day after a strike that killed 12. A tanker was attacked near the Strait of Hormuz. Brent ~**$105**, WTI ~**$92**. Saudi Arabia said Monday that oil supply continues to flow despite the Riyadh attacks.
  - source: https://bloomberg.com/news/articles/2026-10-11/latest-oil-market-news-and-analysis-for-oct-12
  - source: https://thenationalnews.com/business/energy/2026/10/12/saudi-arabia-says-oil-supply-to-continue-to-flow-despite-riyadh-attacks
  - source: https://thehill.com/policy/energy-environment/6088763-oil-prices-jump-houthi-attacks/
- Background: September strikes hit Aramco energy infrastructure directly and halted the East-West pipeline; flows had recovered to ~5.8 mbd of ~7.0 mbd capacity by 2026-10-06. Brent exceeded $108 intra-September. So this is a **two-month-old, escalating** supply-risk regime, not a one-day headline.
  - source: https://www.aljazeera.com/economy/2026/9/25/oil-prices-jump-after-yemens-houthis-claim-attacks-on-saudi-facilities
  - source: https://oilprice.com/Latest-Energy-News/World-News/Brent-Back-Above-100-as-Houthis-Hit-Saudi-Infrastructure.html
- Futures this morning mixed-to-higher (S&P +0.1% to +0.5% depending on source/time), with crude *pulling back from intraday highs* — the tape is treating "supply still flowing" as relief. Tickmill called the relief fragile. source: https://finance.yahoo.com/markets/live/stock-market-today-monday-october-12-dow-sp-500-nasdaq-080321571.html
- **Calendar this week:** Q3 bank earnings begin Tue 2026-10-13 (JPM, GS, C, WFC, JNJ, UNH, DPZ); Wed 10-14 BAC, MS, BLK, STT, FAST; Thu 10-15 SCHW, PNC, USB, IBKR, PLD, AA, CMC, WHR, JBHT; Fri 10-16 TFC, RF, MTB, CFG, TRV. **US CPI reported as due Wednesday.** Next week: GE/STLD/CLF 10-19; NFLX/TSLA/GM/RTX/COF/UAL/ALK/HAL 10-20; LMT/GD/AAL/NEM/VLO 10-21..22. source: finnhub earnings calendar via scripts/market_data.py
- Crypto (coingecko, live): BTC 83,473 (+0.61% 24h), ETH 2,557.48 (+2.28%), SOL 111.64 (+2.06%), XRP 1.40, DOGE 0.0871. BTC is ~34% below its 2025-10-06 record of 126,198 and bottomed near 59,300 in June 2026 — a year-old bear market, now stabilising with leverage at its lowest since Aug 2024. source: https://www.ccn.com/education/crypto/crypto-october-10-crash-anniversary-2026-liquidation-risk/

## [06:09 ET] THESIS SHORTLIST from the oil regime
1. Jet fuel is a cost shock → airlines short. **This contradicts the open DAL BUY.** Must resolve as a POSITION UPDATE.
2. Tanker rates: a tanker attacked near Hormuz lifts war-risk premia and ton-miles → FRO/DHT/STNG/INSW.
3. Defense primes on Iran-proxy escalation; LMT/GD/NOC/RTX all report 10-20..22.
4. Headline CPI Wednesday with crude at $105 → event contract on CPI.
5. Refiners already working (DINO +12.8% open).

## [06:05 ET] LEVELS — the oil-shock trades are mostly already priced (fetched 120d history, nasdaq source)
| Sym | Close 10-09 | ATR14 | ATR% | SMA20 | SMA50 | % off 120d high | 30d $vol |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AAL | 12.76 | 0.432 | 3.39 | 13.15 | 13.81 | -32.1% | $861M |
| UAL | 107.46 | 3.976 | 3.70 | 110.52 | 114.68 | -22.6% | $441M |
| LUV | 41.66 | 1.198 | 2.88 | 41.39 | 41.87 | -21.6% | $253M |
| ALK | 39.36 | 1.481 | 3.76 | 40.01 | 42.59 | -27.5% | $111M |
| DAL | 82.17 | 2.470 | 3.01 | 82.30 | 83.65 | -14.1% | $598M |
| FRO | 56.10 | 1.918 | 3.42 | 51.24 | 46.17 | **-1.3%** | $215M |
| DHT | 24.64 | 0.941 | 3.82 | 22.84 | 20.82 | **-1.7%** | $100M |
| STNG | 85.14 | 3.087 | 3.63 | 84.85 | 81.17 | -5.5% | $92M |
| INSW | 119.82 | 4.693 | 3.92 | 111.04 | 103.04 | -2.4% | $94M |
| TNK | 106.14 | 4.065 | 3.83 | 99.59 | 91.91 | -1.2% | $53M |
| VLO | 433.75 | 17.38 | 4.01 | 402.26 | 367.50 | -3.6% | $1.52B |
| LMT | 509.59 | 10.16 | 1.99 | 519.06 | 549.08 | -16.8% | $577M |
| GD | 331.27 | 6.320 | 1.91 | 340.50 | 363.88 | -17.2% | $429M |
| NOC | 480.72 | 11.58 | 2.41 | 503.15 | 531.90 | **-26.4%** | $437M |
| RTX | 185.97 | 3.540 | 1.90 | 188.94 | 203.30 | -18.0% | $720M |

Three conclusions, two of which kill a thesis I walked in with:

- **REJECTED — tankers (FRO/DHT/INSW/TNK) long:** the trade is done. FRO is +21% above its own 50-day and 1.3% off a 120-day high; DHT, INSW and TNK are all within 2.4% of highs having run 25-65% off their lows. Buying a parabolic move two months into the catalyst is the opposite of the pullback-vs-breakout discipline. No entry here that is not a chase.
- **REJECTED — airlines short (AAL/UAL/ALK) on jet fuel:** also done. AAL is -32% off its high and 7% below its own 20-day. The fuel shock is in the price; the asymmetry now sits with any de-escalation headline, and the Houthis attacked an *airport*, which is a headline risk that cuts toward airlines but is not a fuel-cost mechanism. The existing `AAL` SELL_SHORT @ 13.35 is left as-is (level unchanged, now above market).
- **PURSUE — defense primes are de-rating *through* the escalation.** NOC -26.4% off its high and near a 120-day low, RTX -18%, GD -17%, LMT -16.8%; all four below both their 20- and 50-day averages. That is the single most interesting dislocation on the board, because the direction is backwards from the news. Either the market knows something about budgets/margins, or this is a de-rating in a business whose demand signal just got louder. Investigating before capturing anything.

## [06:11 ET] MACRO — this is a war tape, and that is the fact the defense de-rating has to be read against
- There is an **active US–Iran war**. The 8 April 2026 Pakistan-mediated truce, later extended indefinitely by Trump, broke down on 8 July and fighting resumed. source: https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire
- Weekend of 10–11 Oct: Houthi strikes on Riyadh's King Khalid International Airport **killed 12 and injured more than 300** (Saudi officials, 10 Oct); the Houthis claim at least four operations against the airport since Saturday; **airport operations have been shut down** by Saudi Arabia's aviation authority and airlines have cancelled flights. Saudi Arabia says it flew **120+ airstrikes** on Houthi-held Yemen in 24 hours. **Trump said the US is considering joining Saudi military operations against the Houthis.**
  - source: https://www.cbsnews.com/live-updates/iran-war-trump-us-elections-saudi-arabia-yemen-houthis/
  - source: https://www.nbcnews.com/world/middle-east/saudi-airport-attack-trump-us-join-fight-houthis-rcna602744
- Hormuz: Iran's attempted blockade is unresolved; Iran called Washington's reply to its seven-condition proposal for reopening the strait "insufficient" and talks are stalled with Qatar mediating. CENTCOM says US forces destroyed 10 shadow-fleet tankers carrying sanctioned Iranian oil. source: https://www.france24.com/en/middle-east/20261004-iran-us-military-middle-east-war-peace-talks
- **So the September defense selloff had a specific cause that has now been falsified.** LMT and RTX each fell ~3% on 22 Sep when Reuters reported Iran had offered to reopen Hormuz — a risk-premium deflation trade. That offer is now rejected and stalled, and the US is weighing direct entry. source: https://247wallst.com/investing/2026/09/22/defense-stocks-fall-while-oil-slides-on-hormuz-reopening-report-lockheed-martin-and-rtx-drop-3-boeing-dips/
- **The other, non-falsified cause is real and is the bear case:** RBC downgraded NOC on 2026-10-02 (PT 640 → 525) citing limited international exposure, **slower US defense budget growth after FY2027**, and B-21 early-lot margin drag (~$2.0bn cumulative losses on fixed-price lots); NOC also lost F/A-XX to Boeing on 2026-09-29. A multiple compression on post-FY2027 budget math is not cured by a war headline. source: https://www.marketscreener.com/news/guidance-raised-shares-down-northrop-grumman-fails-to-win-over-the-market-ce7f51d8db8ff523
- **CPI: Wednesday 2026-10-14, 08:30 ET** (BLS). Consensus headline **3.7% YoY** vs August 3.4%; Cleveland Fed nowcast ~3.6% with ~+0.5% MoM; core ~2.4%. The driver is record September petrol prices — i.e. the oil shock arrives in the inflation print this week. Fed meets 27–28 Oct.
  - source: https://nowflation.com/cpi-release-dates
  - source: https://investinglive.com/stocks/us-cpi-preview-energy-set-to-lift-inflation-to-3-7-core-seen-steady-at-2-4
- **DATA GAP — event contracts unavailable.** `market_data.py events "CPI"` returned 0 markets and `events "Fed"` returned one unrelated sports cross-category market with null prices. I cannot state a Robinhood prediction-market implied probability I did not fetch, so **no event contract is captured today**, despite CPI being the week's cleanest binary. Recorded for `data_quality_notes`.

## [06:12 ET] LEVELS — ITA (iShares US Aerospace & Defense)
- Fetched 90d bars: swing low **201.00** on 2026-10-08, then 10-09 made a higher low at 203.90 and closed 206.65 near the day's high on the lightest volume of the month (471,634 vs ~850k average) — a reversal attempt off the low, not yet a trend change.
- ATR14 3.6382 (1.76%). SMA20 210.82, SMA50 227.36. -19.5% off the 120d high of 256.60. 30d dollar volume $170M.
- Stop **198.50**, below the 201.00 pivot = 7.5 pts from a 206.00 entry = **2.06 ATR**, clearing the 1.8 ATR ETF swing floor with room. First target **227.00**, the 50-day, = 21.0 pts → **R:R 2.80**.
- Chose the ETF over RTX deliberately: the bear case is concentrated in single-name execution (B-21 fixed-price losses at NOC, F/A-XX lost to Boeing, LMT's Q1), and a basket is the instrument that takes the sector-risk-premium view without taking those.

## [06:18 ET] DATA GAP — event contracts are unreachable this run
- Tried `market_data.py events` with CPI, FEDDECISION, "Fed decision", "interest rate", inflation, CPIYOY, Brent, oil, "gas price". Every one returned `count: 0`; "Fed" returned a single unrelated sports cross-category market with all prices null.
- Yesterday's run quoted `KXFEDDECISION-26DEC-H25` at 72/74 cents, so this is a transient source failure, not a delisting. **No event contract is captured today and no implied probability is stated**, because I did not fetch one. This is the week's cleanest binary (CPI Wed 08:30) and it is being left on the table for that reason alone.
- Also broken this run: `market_data.py implied` (yahoo-options 401 Unauthorized) and `market_data.py short` (api.nasdaq.com read timeout). So no options-implied-move check and no short-interest read on anything today.

## [06:19 ET] POSITION UPDATE — DAL — opened 2026-10-05 @ 83.00, last 82.17 (-1.0%)
- decision: **CLOSE the long.** The catalyst it was opened for has been delivered and went against it.
- Q3 reported 2026-10-09 before the open (8-K and 10-Q both filed that day): adj EPS **$1.72** vs ~$1.75 consensus, adj revenue **$17.59bn** vs ~$17.67bn. Revenue +16% with premium mix strong — the demand side held.
- The guide is what matters: **FY2026 adj EPS cut from $6.50–7.50 to $5.10–5.60**, pre-tax ~$4.5bn, FCF cut to ~$2.5bn from $3–4bn, absorbing a **$6bn** fuel increase. Q3 adjusted fuel +62% YoY to $4.14bn at $3.61/gal (+60%), **$500M worse than the July guide**. Non-fuel unit costs +7.3%.
  - source: https://www.sec.gov/Archives/edgar/data/27904/000002790426000035/dal-20261009.htm
  - source: https://www.cnbc.com/2026/10/09/delta-air-lines-dal-q3-2026-earnings.html
  - source: https://finance.yahoo.com/markets/stocks/article/delta-reports-q3-earnings-miss-cuts-guidance-as-fuel-costs-surge-62-from-year-ago-103121231.html
- **The forward-looking problem:** Q4 guidance assumes all-in fuel of ~$4.25/gal **struck against the forward curve as of 2026-10-02**, including ~$0.40/gal of Trainer refinery benefit. Brent was $101.49 on 10-07 and ~$105 on 10-11/12 after the Riyadh strikes. The curve has risen since the assumption was set, so the Q4 fuel line is already behind.
- **Why close rather than re-target.** A filled position's entry cannot be amended — it is 83.00. With the published 78.10 stop the risk is 4.90, which is 1.98 ATR on an ATR14 of 2.4702, so a valid swing needs a target at or above **92.80** to clear the 2.0 floor. On post-cut FY EPS of $5.10–5.60 that is ~17x for an airline absorbing a $6bn fuel increase with the fuel assumption already stale. I cannot defend 92.80, and the rule is that an idea needing a reverse-engineered level has failed the floor. So it is closed, not re-priced.
- honest counter: the tape absorbed the cut. DAL fell to 79.16 intraday and closed **82.17, +0.04%**, on the heaviest volume of the month (11.93M vs ~7.3M average). And DAL alone among US airlines owns a refinery (Trainer), worth ~$0.40/gal of its own fuel assumption. If crude mean-reverts, DAL is the airline that re-rates first. That is a real argument for holding; it is not an argument that 92.80 is reachable inside the horizon.
- action: captured via add_candidate.py as `direction: buy` so it amends the live long rather than opening a phantom short row.

## [06:24 ET] CORRECTION — prime earnings dates, read off the fetched calendar
- GE **2026-10-19 bmo** (est 2.0444) · RTX **2026-10-20 bmo** (1.7854) · NOC **2026-10-20 bmo** (7.2411) · LMT **2026-10-22 bmo** (7.5222) · GD **2026-10-22 bmo** (4.2524). My first ITA capture said LMT 10-21; that was wrong and ITA is being re-captured with the corrected dates. Also on the docket: UAL 10-20, LUV 10-21, AAL 10-22, VLO 10-22 bmo (18.518), GE and STLD 10-19.
- Nothing for DINO, CCJ, MPC, PSX or OXY inside 10 sessions — OXY 2026-11-09, DK 2026-11-05, CEG 2026-11-04.

## [06:25 ET] REJECTED — refiners as a *new* idea (MPC, PSX, PBF, DK, CVI, PARR) — the trade is fully priced
- 3:2:1 crack spreads are at or near all-time records: CME reported the spread above its June 2022 record near $64 in July; snapshots on 2026-10-08/09 read $63 (worldoilmonitor), $63.5 (OilPriceAPI), $69.7 (RBN). New York Harbor 3:2:1 averaged ~$65.61/bbl in August 2026, the highest monthly figure since 2006.
  - source: https://www.cmegroup.com/newsletters/fresh-from-the-trading-room/2026-07-14.html
  - source: https://rbnenergy.com/daily-posts/blog/what-2026s-record-crack-spreads-tell-us-about-refining-economics
- And the equities have already taken it: off their 120-day lows MPC +113%, CVI +123%, PBF +132%, DK +97%, PARR +67%, PSX +79% — every one of them within 3-9% of a 120-day high. Entering a record-margin cyclical at the high of a record is the same mistake as chasing the tankers. **No new refiner exposure.** The existing DINO long is the position that already owns this and it is managed below.
- Brent-WTI: sources disagree badly ($11.14 on 10-08 per one tracker; Rigzone around 10-01 quotes the gap easing from $13-14 toward ~$7 while Standard Chartered called WTI's discount wider than $12, the widest since early May; a third site prints -$29.20, an obvious outlier). **I am not stating a Brent-WTI number I cannot pin down** — the spread is wide and volatile, which is all the sources support. source: https://www.rigzone.com/news/analysts_look_at_wtibrent_spread-01-oct-2026-184747-article/

## [06:26 ET] CROSS-ASSET — the war is NOT lifting the usual hedges, and that is informative
- GLD 384.58, **-12.6% off its 120-day high**, below both its 20-day (388.01) and 50-day (397.03). GDX -15.5%, SLV -32.3% off high. Gold falling during a regional war with headline CPI heading to 3.7% only makes sense through real rates: the 10y is at 5.22% and yesterday's run fetched Kalshi pricing a 72-74% chance of a **25bp hike** on Dec 9. Gold is losing the real-rate fight, not the risk fight. The `GLD` SELL awaiting at 406.77 is 5.5% above market and will not fill; level left unchanged.
- URA 38.90, -34.0% off high, below its 20-day (40.95) and 50-day (43.31) — uranium is in a downtrend, which is the sector backdrop for the open CCJ long.

## [06:27 ET] POSITION UPDATE — CCJ — opened 2026-08-17 @ 94.00, last 88.06 (-7.3%)
- decision: **no new recommendation; the existing CLOSE instruction from the 2026-10-08 report stands.** CCJ sits at 88.06 against a 120-day low of 83.15, below its 20-day (89.54) and 50-day (94.77) and -32.9% off its high, with URA confirming the sector downtrend and no earnings inside 30 sessions.
- Nothing has happened to CCJ since 10-08 that changes the call, and it has already been recommended twice in ten days. Re-publishing the same close a third time would be the repetition the guard exists to catch, so it is recorded here rather than captured. Its 82.5 stop remains a valid stop 6.3% below market.

## [06:28 ET] POSITION UPDATE — XLE — opened 2026-08-15 @ 63.90, last 65.08 (+1.9%)
- decision: **hold, every level unchanged.** Thesis is working — XLE is 1.65% off its 120-day high, above its 20-day (63.30) and 50-day (62.67), with Brent ~$105 and the Saudi supply risk escalating.
- Explicitly **not** raising the stop. From the fixed 63.90 entry the published 60.80 stop is 3.10 = 2.49 ATR (ATR14 1.2425); the most I could tighten it to and still clear the 1.8 ATR ETF floor is ~61.30, a 0.50 improvement that would lift the published ratio while making the trade worse. That is the KRE stop-walk, and it is declined. No candidate captured — unchanged is the honest answer.

## [06:33 ET] REJECTED — LNG shipping (FLNG, CCEC, GASS, DLNG) — the volume collapse beats the ton-mile boost
- The theme looked compelling: Qatar halted LNG output after drone strikes on its industrial cities (TTF +35% in a session to >EUR60/MWh in March), Qatar later halted all maritime activity, TTF printed its highest close since January 2023, European storage is substantially below seasonal average, and Goldman wrote that TTF at EUR65 is not enough for Europe to get through winter without more Persian Gulf LNG.
  - source: https://www.kpler.com/blog/global-lng-and-natural-gas-prices-surge-as-us-and-iran-resume-hot-war
  - source: https://gasoutlook.com/analysis/lng-markets-tighten-as-hormuz-disruption-expected-to-persist/
- **And the freight data falsifies it.** By late August, Atlantic LNG spot rates had fallen to ~$20,000/day — Spark Commodities called it the lowest spot level *on record* for the time of year — with Pacific at ~$61,500/day. ICIS counted ~33 cargoes exiting in six months against a normal 90-100 *per month*. Cargoes you do not load do not need ships, and the lost Qatari volume swamps the longer Atlantic voyages. 59 new carriers deliver in 2026, +28% YoY, on top of that. source: https://pgjonline.com/news/2026/august/asian-spot-lng-prices-hit-five-month-high-on-hormuz-impasse
- Confirmed by the tape: FLNG -7.7% off high and below both MAs, CCEC -13.9%, GASS -14.2%, DLNG -12.8%, GLNG -17.1%. The whole complex is below its 20- and 50-day averages during the biggest gas dislocation in three years. That is the market agreeing with the freight print, not missing the story.
- Also noted and **not acted on**: Windward posted that VLCC charter rates to transit Hormuz were assessed just over **$1,000,000/day**, the highest on record, up from ~$500,000 a month earlier after the US "tanker-for-tanker" pledge disabled 10 Iranian-trading tankers; Seatrade had fixtures near $470,000/day. That is a war-risk premium on one voyage few owners will take, not fleet-wide earnings, and the primary source is an X post. **Not building a trade on a tweet**, and the tanker equities are at their highs anyway.
  - source: https://x.com/WindwardAI/status/2100117534062035048
  - source: https://www.seatrade-maritime.com/tankers/vlcc-rates-near-470-000-a-day-for-fixtures-through-hormuz

## [06:36 ET] LEVELS + VALUATION — HII (Huntington Ingalls), the long-term lane
- Read the Q2 FY2026 8-K earnings release directly. Revenue **$3,418M, +10.9%**; segment operating income $224M at a **6.6% margin**, up from 5.6% a year earlier; net earnings $208M; **diluted EPS $5.27** vs $3.86. New awards **$6.7bn**; **total backlog $57.3bn** at 2026-06-30. FY26 shipbuilding revenue **raised to $10.2-10.4bn** from $9.7-9.9bn; shipbuilding margin guided **6.0-6.5%**, low end raised from 5.5%; Mission Technologies $3.0-3.2bn at ~5%; **FY26 FCF $500-600M reaffirmed**. source: https://www.sec.gov/Archives/edgar/data/0001501585/000150158526000045/hii2026q2earningsrelease.htm
- The one genuinely bad line: **Q2 FCF was negative $150M** against +$730M a year earlier. That is the problem, and management reaffirmed the full-year $500-600M alongside it, so the company is calling it timing on a ramp rather than a break.
- Backlog driver: a **$76.6bn** submarine award (Virginia Block VI + Columbia), ~$25bn of it to Newport News. source: https://finance.yahoo.com/markets/stocks/articles/huntington-ingalls-industries-inc-hii-010451663.html
- Price: 264.80, ATR14 7.4239 (2.80%), sma20 269.09, sma50 291.20, **-32.1% off the 120-day high of 390.00 and 3.1% above the 120-day low of 256.79**. 30d dollar volume $132M.
- Relative strength (fetched): HII **-32.86% over 6m vs SPY +14.59%**, i.e. -47.45pp against the benchmark — but **+5.04pp against ITA over 3m**. So the damage is a six-month de-rating, and over the last quarter it has stopped lagging its own sector.
- Multiple math, shown: H1 FY26 EPS = 3.79 + 5.27 = **$9.06**; annualising H1 gives ~$18.1, so 264.80 is **~14.6x**. Peers on 4x their fetched Q3 consensus: GD 331.27/17.01 = **19.5x**, LMT 509.59/30.09 = **16.9x**, NOC 480.72/28.96 = **16.6x**, RTX 185.97/7.14 = **26.0x**. HII is the cheapest in the group and the only monopoly in it.
- Analyst revisions improving: bullish share **58.8%, +5.9pp** across four monthly snapshots to 2026-09-01 (strong_buy 2→3, hold 8→7, zero sells throughout), against a **+37.2% EPS surprise** for the quarter ended 2026-06-30.
- Insiders: **zero** open-market buys in six months, 3 sells totalling $5.6M. Absence of buying is not a negative and is not counted as evidence either way; the sells are weak evidence on their own and are recorded for completeness.
- **Why long_term and not swing:** HII does not report inside 30 sessions on the fetched calendar, so there is no dated catalyst to carry a swing. Checked the swing version anyway — entry 263, stop 247 below the 256.79 low is 2.16 ATR and needs a 295 target for 2.0:1, which is the 50-day; it would pass, but with no catalyst it is a chart trade on a franchise story, which is the wrong instrument for the thesis.

## [06:40 ET] AWAITING-ENTRY AUDIT — fetched every published level against Friday's close
| Symbol | Side | Published entry | Last | Distance | Verdict |
| --- | --- | --- | --- | --- | --- |
| VST | BUY | 132.00 | 161.48 | **+22.3%** | **dead** — published 2026-08-24, the stock ran away and never looked back; a limit 18% under market is not a live idea |
| OXY | BUY | 54.00 | 60.11 | **+11.3%** | **dead** — published 2026-09-24 into a rising crude tape; the pullback never came |
| FCX | BUY | 68.20 | 73.69 | +8.0% | **dead** — published 2026-10-04, 7.5% under market |
| MU | BUY | 960.00 | 1029.00 | +7.2% | stale but plausible as a pullback; waiting since 2026-09-18 |
| DG | BUY | 134.50 | 127.23 | -5.4% | live breakout entry, 5.7% above market |
| STLD | BUY | 245.50 | 238.38 | -2.9% | **live** — 3.0% above market with earnings 2026-10-19 amc (est 5.4904); the best of the awaiting set |
| GLD | SELL | 406.77 | 384.58 | -5.5% | resting short limit 5.8% above market; level unchanged, see the cross-asset note |
| ITB | SELL_SHORT | 89.80 | 84.76 | -5.6% | resting; builders already -20.3% off high and 1.3% above a 120-day low, so the short is late even if it fills |
| AAL | SELL_SHORT | 13.35 | 12.76 | -4.4% | resting 4.6% above market; level unchanged |
| TLT | SELL_SHORT | 79.90 | 77.98 | -2.4% | resting; 10y at 5.22% supports it but TLT is 2.0% off a 120-day low, so the entry is the whole edge |
| IYR | SELL_SHORT | 97.80 | 96.10 | -1.7% | resting, closest to filling of the shorts |
| KXCPIYOY-26SEP-T3.5 | NO @ 18 | — | unquotable | **cannot be marked** — the Kalshi source returned nothing today; see the event-contract data gap. Note that consensus for Wednesday's print is 3.7% headline, which is *against* a NO on a 3.5 threshold |
| KXFEDDECISION-26SEP-H0 | YES @ 47 | — | expired | the September FOMC has been and gone; this should not still be listed as awaiting entry |

## [06:42 ET] POSITION UPDATES — the rest of the book, held unchanged, recorded rather than captured
Nothing new has reached these since their last publication, and re-pitching an unchanged idea is the anchoring the guard exists to catch. Prices are Friday's close.
- `XLF` 54.73 vs 54.23 entry (+0.9%) — **hold**, every level unchanged. Updated only yesterday; the Q3 prints that *are* the thesis start tomorrow (JPM, GS, C, WFC 10-13; BAC, MS 10-14). Bloomberg Intelligence has the majors entering the quarter with strong credit quality, which is the fear being tested. Consensus: JPM EPS ~$5.90-5.93 on ~$51.2bn; GS $12.87 on $16.83bn. source: https://www.tipranks.com/news/jpm-gs-bac-what-to-expect-from-big-bank-earnings-this-week
- `CEG` 298.07 vs 272.00 (+9.6%) — **hold**. 9.4% off its high, 11% above its 50-day, earnings 2026-11-04, outside the horizon. No change.
- `SNX` 273.37 vs 260.00 (+5.1%) — **hold**. Above both averages, 8.5% off high. No change.
- `KHC` 22.27 vs 23.00 (-3.2%) — **hold**. 22.27 against a 120-day low of 21.75 and -20.7% off high, below both averages. Thesis was corrected on 10-09 and nothing has reached it since.
- `PFE` 28.28 vs 27.60 (+2.5%) — **hold**. Above both averages, 3.2% off its high. The best-behaved long-term position in the book.
- `EEM` 66.80 vs 65.60 (+1.8%) — **hold**, already halved on 10-08. A stronger dollar and a 5.22% 10y are the standing headwind; nothing new today.
- `BCC` 73.57 vs 76.50 (-9.2%) — **hold** with a note: this position still has **no stop**, like LCII before it, and builders are -20% off their highs with the 10y at 5.22%. It needs an invalidation level the next time it is pitched.
- `SMMT` 17.59 vs 17.10 (+2.9%) — **hold**. Opened 10-09, 2 days old, 39.8% off its high with a 6.7% ATR; nothing to do on day three.
- `LCII`, `LULU` long leg, `NKE` long leg — the 2026-10-11 report already recommended closing all three at today's open. Those instructions stand and are not re-issued.
- `LULU` SELL 100.61 (+6.1%) and `NKE` SELL 38.40 (+9.6%) — **hold both shorts**, which is the other half of yesterday's decision. LULU is -44.5% off its high at 94.50 against a 120-day low of 90.38, and NKE -27.2% at 34.71 against a low of 31.97. Both targets (77.00, 32.10) are below those lows, so both need new lows to pay.

## [06:47 ET] REJECTED — four names that looked like setups and failed the falsification pass
- **LRN (Stride)** — the only thing supporting it was the chart: 85.59, above both its 20-day (79.77) and 50-day (81.80), -17.4% off high, earnings 10-20. The measured positioning read is against it: bullish share 66.7% but **-11.1pp** (strong_buy 4→3, hold 2→3), revision direction **deteriorating**, and it **missed by 5.5%** last quarter. A breakout with falling revisions and a miss behind it is a chart, not a thesis.
- **CMC (Commercial Metals)** — the one name all day with real insider buying: **2 distinct open-market buyers, $604,468** — McPherson 1,390 sh @ 71.92 on 2026-08-13 and Matt 8,230 sh @ 61.30 on 2026-07-10 — with earnings 10-15. Rejected on arithmetic: at 63.89 with ATR 1.8539, a 2.0 ATR stop must sit at or below 60.18 (the 120-day low is 59.96), which puts risk at ~4.70 from a 63.50 entry and **requires a 72.90+ target** to clear 2.0:1. That is +14.8% and above one of the insider's own purchase prices, on a name below both averages with revisions deteriorating (-3.9pp) and a mixed surprise record (+0.2%, -11.9%, +16.7%, -0.5%). An idea that only clears the floor with a stretch target has failed the floor.
- **CLF (Cleveland-Cliffs)** — the biggest revision swing on the board, bullish share 30% but **+21.3pp**, sells collapsing 7→1 and strong_sell 1→0, trading above both averages with earnings 10-19. Rejected: it has lost money in all four reported quarters (-0.25, -0.42, -0.44, -0.51) and **missed by 22.2% and 21.4%** in the last two. A loss-making cyclical at 5.1% ATR is a lottery ticket, and the steel driver is already represented by the live STLD breakout entry.
- **UNH** — strongest analyst support in the whole screen (**79.4% bullish, +2.9pp, zero sell ratings, 28 of 34 positive**) with **+28.8%** and **+8.9%** EPS surprises in the last two quarters, 379.30 and -17.8% off high, **reporting tomorrow 10-13 bmo**. Rejected for honest reasons rather than bad ones: I have not verified the medical-cost-ratio story behind the de-rating, and a 2.0 ATR stop (17.73 on an ATR of 8.8649) is not a risk control on a managed-care name the night before a print — UNH gaps multiples of that. Positioning is not a thesis. **Watchlist it for a post-print entry on 10-13**, which is the honest version of this idea.
- **Crypto** — no idea captured. BTC 83,473 is 34% below its 2025-10-06 record with leverage at its lowest since Aug 2024, which is a stabilising setup, but the macro is pointed the wrong way: headline CPI heading to 3.7%, a 10y at 5.22% and a Fed priced ~74% to hike in December. I have no probability disagreement to assert, so there is nothing to publish.

## [06:49 ET] STLD — live awaiting-entry, deliberately NOT re-pitched
- The 245.50 stop-limit trigger from 2026-10-10 is unchanged and 3.0% above Friday's 238.38, with earnings **2026-10-19 amc** (est 5.4904) now inside the 10-session window. Re-verified today: bullish share 63.6%, +1.7pp improving (sells 2→1); four consistent small beats (+2.7%, -2.1%, +5.5%, +1.8%); 0 insider buys against 13 sells. Bars confirm the shelf — 10-05 high 245.185, sma20 233.88, sma50 241.36.
- Nothing specific to STLD has changed since 10-10, so the order stands and is not re-published; it was already red-teamed to conviction 3.
- **One new cross-current for the next run to resolve, recorded rather than guessed:** STLD is a pure electric-arc-furnace producer, so the energy shock cuts both ways — Brent at ~$105 and European gas at its highest close since January 2023 raise *its* power costs while also raising import prices and curtailing European mills, which supports steel pricing. I cannot net those two out with the data I have and will not pretend to.

## [06:52 ET] LEVELS — GE Aerospace, and the correlation count
- 308.20, ATR14 7.6783 (2.49%), sma20 313.68, sma50 336.70, -20.7% off the 120-day high of 388.84. Bars: 10-08 printed the 60-day low at **296.61** on the heaviest volume in weeks (6.39M), and 10-09 reversed to close 308.20. $1.30bn 30d dollar volume.
- Positioning is the strongest and the most two-sided thing about it. Bullish share **87.5%** — 9 strong_buy, 19 buy, 3 hold, 1 sell — the highest of anything screened today, and **exactly flat for four consecutive monthly snapshots**. Earnings surprises: **+5.5%, +13.0%, +6.8%, +10.9%**, four straight beats averaging ~+9%. Insiders: 0 buys, 8 sells.
- Relative strength kills the hypothesis I came in with. I expected GE to be a mis-grouped victim of a *defense budget* de-rating despite being mostly commercial aero. In fact GE is **-0.05% over 6m against ITA's -10.01%, +9.96pp ahead of its sector** — it held up and only joined the selloff in the last three months (-12.79% vs ITA -12.08%). So the idea is a three-month drawdown in a franchise with a four-quarter beat streak, not a sector misclassification. Recorded because the weaker, true version is the one being published.
- Stop **292.00**, below the 296.61 low = 16.20 from a 308.00 entry = **2.11 ATR**, clearing the 2.0 stock floor. Target **341.00**, just above the 336.70 50-day = 33.00 → **R:R 2.06**. The 10.7% move required is symmetric with the 9.5% drop from 327.09 (09-25) to 296.61 (10-08) that just happened in nine sessions.
- **Correlation, counted explicitly:** ITA, HII and GE are three ideas in aerospace and defense, which is exactly the cap of 3 in config/strategy.md, and ITA holds both GE and HII. Their drivers do differ — a sector risk-premium swing, a naval shipbuilding monopoly re-rating, and a commercial-aero aftermarket print — but they would sell off together. This is at the limit, stated so the red team can cut one rather than discover it.

## [06:55 ET] REJECTED — every non-aerospace candidate screened today, and the pattern is the finding
- **AA (Alcoa)** — the thesis was good: aluminium is the most electricity-intensive metal, Alcoa's smelters are largely hydro-powered while European and Asian competitors burn gas and coal, so an energy shock is a *relative* cost tailwind plus a supply-curtailment catalyst — and it is -50.0% off its high at 42.20, 2.9% above a 120-day low, reporting 10-15. Rejected on the data: revisions **deteriorating** (72.7%, -1.2pp, sell back to 1), an erratic surprise record (+0.1%, -9.0%, +33.6%, +90.6%) that gives no basis for forecasting the print, and zero insider buying against 4 sells. A -50% name into earnings needs confirmation, not a story.
- **TRV (Travelers)** — fascinating divergence, no trade. Four enormous beats (**+83.4%, +7.9%, +24.6%, +27.0%**) while the analyst book *deteriorated* to 25.7% bullish, -7.6pp, with sells going 1 → 5. But it is only -7.5% off its high and sitting on both its averages, so there is no entry discount to underwrite, and insiders are 0 buys against **25 sells**. Watchlist-grade curiosity.
- **IBKR** — 81.0% bullish but **-7.2pp deteriorating**, holds 2 → 4, -11.0% off high, reports 10-15. The "6 insider buys" are 25-share automatic purchases by a single person totalling $13,019 — one distinct buyer in dribbles is not the clustered open-market signal that is worth weighting, and calling it one would be exactly the inflation the evidence rules exist to stop.
- **The pattern is worth stating, because it is why this run is concentrated.** On Friday's close the names with *improving* analyst revisions were almost all in aerospace, defense and steel — HII +5.9pp, RTX +3.4pp, STLD +1.7pp, CLF +21.3pp — while everything else screened deteriorated: LRN -11.1, IBKR -7.2, TRV -7.6, CMC -3.9, AA -1.2, with GE exactly flat. That is not a preference for the sector, it is where the revision tape actually points this week, and it is the honest reason the report skews the way it does rather than a manufactured mix.

## [06:58 ET] SELF-CHECK — recomputed every captured idea's arithmetic before the phase ends
| Idea | Horizon | Entry | Downside | Target | R:R | Stop in ATRs | Floor | win_prob vs baseline | Conviction vs evidence kinds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | swing | 206.00 | 198.50 | 227.00 | **2.80** | 2.06 | 1.8 (etf) | 0.42 vs 0.263 (+15.7pt) | 4 = 3 kinds ✓ |
| GE | swing | 308.00 | 292.00 | 341.00 | **2.06** | 2.08 | 2.0 | 0.42 vs 0.327 (+9.3pt) | 4 = 3 kinds ✓ |
| DINO | swing | 107.50 | 97.75 | 128.00 | **2.10** | 2.17 | 2.0 | 0.48 vs 0.322 (+15.8pt) | 3 = 2 kinds ✓ |
| HII | long_term | 262.00 | 205.00 (bear case) | 430.00 | **2.95** | n/a | 2.5 | n/a — no stop by design | 5 = 4 kinds ✓ |
- Every floor cleared on recomputation, every claimed edge under the 20-point ceiling, every conviction score equal to its count of distinct evidence kinds.
- **DAL is the exception and it is being re-captured because of it.** My first capture set the stop to Friday's close (82.17) to force the tracker to close the row, the way the 2026-10-11 LCII/LULU/NKE exits did. That puts the stop 0.34 ATR from the entry, which fails `check_stop_distance` outright and risks `--enforce` demoting the close instruction to the watchlist, where it loses its force. The prior exits survived because they were labelled `long_term`, which exempts the check — DAL was published as a swing and relabelling it to dodge a validator is precisely the gaming this pipeline exists to catch.
- So DAL is re-captured with its **published 78.10 stop left untouched**. R:R then computes to 2.35 and passes; the stop distance is **1.98 ATR against a 2.00 floor** and will warn. That 1.98 is a real defect in the original idea, not something introduced today, and the correct response is to record it rather than widen a stop on a position being closed. **Red team: do not "fix" this by moving the stop.** The close instruction lives in `exit.scale_plan` and `catalyst.action`.

## [07:02 ET] CORRECTION TO MY OWN EARLIER NOTE — event contracts are NOT down, `events` is broken
Earlier I recorded the event-contract gap as a transient source failure. That was wrong, and the real cause is a bug worth fixing because it is why this lane keeps falling out of the report. Queried the Kalshi API directly and got live prices on the first try.

**Two defects in `market_data.py events()`:**
1. **Renamed fields.** Kalshi now returns `yes_bid_dollars`, `yes_ask_dollars`, `no_bid_dollars`, `no_ask_dollars`, `last_price_dollars` (decimal strings) and `volume_fp`, `open_interest_fp`. The function reads `yes_bid`, `yes_ask`, `last_price`, `volume`, `open_interest`, which no longer exist — hence every price coming back `null` even when the market is found and `status: active`.
2. **No server-side filtering and no pagination.** It fetches `limit=min(limit*5, 200)` open markets and then substring-filters client-side. Kalshi has thousands of open markets, so the search only ever sees an arbitrary first 200 — which is why `events "Fed"` returned a basketball cross-category market this morning. The fix is `event_ticker=` / `series_ticker=` / `tickers=` on the request, all of which work: `?status=open&event_ticker=KXCPIYOY-26SEP` returned the full 21-strike ladder.

## [07:05 ET] EVENT MARKETS — the live implied distribution for Wednesday's CPI
Fetched from the Kalshi `KXCPIYOY-26SEP` ladder (resolves on the 2026-10-14 08:30 ET BLS release; close_time 2026-10-14T12:29Z). Kalshi strikes are "above X%" and CPI YoY prints to one decimal, so "above 3.5" means 3.6 or higher.
| Market | Price (yes) | Implied | Open interest |
| --- | --- | --- | --- |
| T3.4 — above 3.4% | 0.95/0.96 | P(≥3.5) = 95% | 29,927 |
| T3.5 — above 3.5% | 0.86/0.88 | **P(≥3.6) = 88%** | 50,315 |
| T3.6 — above 3.6% | 0.49/0.52 | **P(≥3.7) = 52%** | 138,487 |
| T3.7 — above 3.7% | 0.11/0.12 | **P(≥3.8) = 11.5%** | 49,612 |
| T3.8 — above 3.8% | 0.02/0.03 | P(≥3.9) = 2.5% | 75,340 |

Differencing the ladder gives the market's full distribution: **P(≤3.5) 12% · P(3.6) 36% · P(3.7) 40.5% · P(≥3.8) 11.5%.** Modal outcome 3.7%.

- **No event contract is captured, and the reason is that I have no edge rather than no data.** Street consensus is 3.7% and the Cleveland Fed nowcast is ~3.6%; the market has placed 36% and 40.5% on exactly those two outcomes. It is pricing the same two forecasts I am reading, efficiently. The rule is that the edge must be a stated probability disagreement, and I do not have one — the October crude move is irrelevant to a September print, so the energy input here is already observable and already in the nowcast.
- **POSITION UPDATE — `KXCPIYOY-26SEP-T3.5` NO @ 18, awaiting entry since 2026-09-30:** NO now trades **0.12/0.14**, i.e. the market puts **88%** on the outcome that makes it worthless, and it resolves in two days. The level is stale and the thesis is contradicted; it should be **retired, not re-pitched**. Recorded here rather than captured because it never filled and so is not a position.

## [07:07 ET] EVENT MARKETS — the Fed path, fetched live
| Meeting | Hold | Hike 25bp | Hike >25bp | Cut 25bp |
| --- | --- | --- | --- | --- |
| **Oct 28, 2026** | **0.84/0.85** | 0.15/0.16 | 0.01 | 0.01 |
| **Dec 9, 2026** | 0.23/0.25 | **0.71/0.74** | 0.02/0.03 | 0.01/0.02 |
- So the market has the Fed holding in October at 84% and **hiking 25bp in December at ~71-74%** (≈73-77% for any hike). This confirms yesterday's 72/74 read and is the single most important frame for the whole report: with the 10y at 5.22%, headline CPI heading to 3.6-3.7% and a hike priced for December, long-duration assets, gold, REITs, builders and rate-sensitive cyclicals are all leaning into a headwind — which is exactly what the tape shows (GLD -12.6% off high, NEE -21.6%, ITB -20.3%, TLT 2.0% off a 120-day low).
- `KXFEDDECISION-26SEP-H0` is still listed as awaiting entry. That meeting has been and gone; the row should be cleared.
- **No Fed contract captured either.** Buying October "Hike 25bps" at 16 cents as a cheap option on a hot print is tempting and is not a thesis: the 3.6-3.7% print is what the market already expects, so it is not news the Fed would break its own October guidance over, and I have no information the 1.49m contracts of open interest do not.

## [07:10 ET] RESEARCH COMPLETE
- candidates captured: **7 captures, 5 distinct symbols** — ITA (new, swing, conv 4), GE (new, swing, conv 4), HII (new, long_term, conv 5), DINO (position update, conv 3), DAL (position CLOSE, conv 3). ITA and DAL were each re-captured once to correct an error; synthesis takes the last entry per symbol.
- **The skew is real and should be stated plainly in `data_quality_notes`:** three of the five are aerospace and defense, which is exactly the correlation cap of 3, and ITA holds both GE and HII. It is not a manufactured theme — on Friday's close the only names screening with *improving* analyst revisions were in aerospace, defense and steel (HII +5.9pp, RTX +3.4pp, STLD +1.7pp, CLF +21.3pp) while everything else deteriorated (LRN -11.1, TRV -7.6, IBKR -7.2, CMC -3.9, AA -1.2) and GE was flat. Five ideas is a thin day honestly arrived at; the red team should feel free to cut one of the three A&D ideas rather than treat the cap as satisfied.
- nothing intraday cleared the bar: the market was closed all weekend, there is no 08:30 print today, and every level here is set off Friday's close.
- **coverage gaps:**
  - No index-level context fetched. Yahoo returned HTTP 429 for every index and futures symbol and finnhub refuses index CFDs, so ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES, NQ, DXY, gold and WTI all came back `ok: false`. SPY/QQQ closes were used as proxies.
  - `market_data.py implied` is down (yahoo-options 401 Unauthorized) — **no options-implied-move check was run on any finalist**, so no idea here has been tested against what the straddle prices.
  - `market_data.py short` timed out (api.nasdaq.com) — no short-interest or days-to-cover read on anything.
  - Brent-WTI spread could not be pinned down; sources ranged from $7 to $29 and I declined to state a number.
  - UNH is the one idea I left on the table for lack of time rather than lack of merit: 79.4% bullish, +28.8% and +8.9% surprises, -17.8% off high, reporting 10-13 bmo. Unverified medical-cost-ratio story. Worth a post-print look tomorrow.
  - 12 of the 17 open positions were reviewed and held unchanged with the reasoning recorded above rather than captured as candidates.
- **sources that failed:** Yahoo Finance chart API (429 on all indices), Yahoo options API (401), api.nasdaq.com short interest (read timeout), `market_data.py events` (broken field names + no pagination — worked around by calling Kalshi directly).

## [07:18 ET] ADDENDUM — UNH researched after all, and it supersedes the earlier rejection
I rejected UNH at 06:55 for lack of time to verify the medical-cost story. Time was available, so the work was done and the rejection is withdrawn. **This block supersedes the UNH line in the 06:55 REJECTED note.**

- Read the Q2 2026 8-K earnings release directly: revenue **$112,032M**; **MCR 86.7%**, which "was affected by **$860 million of net favorable prior period development**"; **adjusted EPS $6.38**, GAAP diluted $6.04; cash flow from operations **$11.1bn in the quarter, 1.9x net income**, $19,964M for H1. Medicare Advantage seniors served **contracted by 965,000 since year-end 2025**, though the people-served table shows the MA line going 8,445k → 7,565k (-880k) and the release does not reconcile the two figures — noted rather than smoothed over.
- **FY2026 guidance (as of 2026-07-16): MCR 88.1% ± 25bp, adjusted EPS $19.50-20.00, reported diluted $18.45-18.95, cash flow from operations ~$24bn. No full-year revenue guidance is given.** The January outlook had MCR at 88.8% ± 50bp, so **the cost-ratio guide improved 70bp during the year** — which is the exact fear that de-rated managed care being refuted by the company's own number.
  - source: https://www.sec.gov/Archives/edgar/data/0000731766/000073176626000191/earningsrelease2q26_7152.htm
- Q3 2026 reports **tomorrow, 2026-10-13 before the open** (on the fetched calendar), consensus **EPS $4.12 on ~$111.4bn**. source: https://site.financialmodelingprep.com/market-news/unitedhealth-q3-earnings-preview-medicare-advantage
- Guide is internally coherent, which matters for reading the Q3 bar: H1 adjusted EPS was 7.23 + 6.38 = **$13.61**, so the $19.50-20.00 FY guide implies H2 of only $5.89-6.39 — Q3 at $4.12 plus a Q4 near $2.0, against an actual Q4 2025 of $2.11. That is normal Medicare seasonality, not a collapse, so I am **not** claiming the Q3 bar is artificially low.
- Valuation: 379.30 on $19.75 midpoint adjusted EPS is **~19.2x**, and ~14x the ~$24bn operating cash flow guide. Not statistically cheap — this is a de-rating-reversal idea, not a value idea, and the thesis is stated that way.
- Positioning: **79.4% bullish, +2.9pp, improving — 8 strong_buy, 19 buy, 7 hold and zero sells of 34 analysts**, the most supportive book of anything screened today; EPS surprises **+28.8%** and **+8.9%** in the last two quarters. Insiders 0 buys, 3 sells.
- Relative strength, which again corrects my framing: UNH is **+24.63% over 6m against XLV +15.95% (+8.68pp)** and has only broken down over three months (-11.6% vs XLV +5.82%, i.e. **-17.42pp**). Like GE, this is a three-month drawdown in a six-month winner, not a chronic laggard.
- Bars: a two-week base between the **362.60** 60-day low (10-01) and 10-09's high of **387.52**, the latter printed on 7.47M shares, the heaviest in the sample, closing 379.30 above the 374.92 20-day and below the 389.18 50-day. ATR14 8.8649. A preview flags 408 as the resistance above that. source: https://www.ig.com/en-ch/news-and-trade-ideas/unitedhealth-stock-q3-2026-earnings-preview-261006
- **Why `wait: true` rather than an entry today.** Every pre-print variant fails honestly. At a 379 entry, a 2.0 ATR stop must sit at or below 361.3, so risk is ~18 and the target must be 415+ to clear 2.0:1 — above the 408 resistance, which is the stretch target I rejected CMC for. Dropping the entry to 370 to shrink risk puts the stop at 352 with nothing structural under it, and sets a limit 2.5% below the market hours before a binary event, which only fills if the print is bad. That is the pullback trap in its sharpest form. Waiting for the print removes the largest single source of variance, and that mechanical variance reduction — not optimism — is where the claimed edge over the 0.327 baseline comes from.

## [07:25 ET] RESEARCH COMPLETE — FINAL, supersedes the 07:10 block
- candidates: **9 captures, 6 distinct symbols.** Synthesis takes the last entry per symbol; ITA was re-captured once to fix a wrong earnings date and DAL twice for the reasons below.

| Idea | Side | Horizon | Entry | Stop / bear | Target | R:R | Stop ATRs | win_prob vs baseline | Conv = kinds | Size | Wait |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITA | buy | swing | 206.00 | 198.50 | 227.00 | 2.80 | 2.06 (fl 1.8) | 0.42 vs 0.263 → +15.7pt | 4 = 3 | 3% | no |
| HII | buy | long_term | 262.00 | 205.00 bear | 430.00 | 2.95 | n/a | n/a by design | 5 = 4 | 4% | no |
| UNH | buy | swing | 379.00 | 361.00 | 416.00 | 2.06 | 2.03 (fl 2.0) | 0.44 vs 0.327 → +11.3pt | 5 = 4 | 3% | **yes** |
| GE | buy | swing | 308.00 | 292.00 | 341.00 | 2.06 | 2.08 (fl 2.0) | 0.42 vs 0.327 → +9.3pt | 4 = 3 | 3% | no |
| DINO | buy | swing | 107.50 | 97.75 | 128.00 | 2.10 | 2.17 (fl 2.0) | 0.48 vs 0.322 → +15.8pt | 3 = 2 | 2% | no |
| DAL | buy | swing | 83.00 | 78.10 | 94.50 | — | 1.98 **warn** | null by design | 3 = 3 | — | no |

- Every reward-to-risk floor clears on recomputation, every stop clears its asset-class ATR floor except DAL's, every claimed edge sits between 9 and 16 points — inside the 20-point ceiling — and every conviction score equals its count of distinct evidence kinds.
- **DAL was re-captured a third and final time** to set `risk_reward` and `win_probability` to null. The second version claimed 0.30 against a 0.299 baseline — a 0.1-point edge, which is a rounding error away from a hard expectancy failure and, worse, was asserting an edge in a trade whose whole point is that it no longer has one. Nulls are the honest values on an exit row and match the 2026-10-11 LCII/LULU/NKE convention. **Red team: leave them null, and leave the 78.10 stop alone.**
- **Driver mix is now balanced rather than at the cap:** aerospace and defense 3 (ITA, HII, GE — still at the correlation limit, and ITA holds the other two), oil and refining 1 (DINO), healthcare 1 (UNH), plus the DAL exit. The 07:10 block flagged the A&D concentration as the run's main weakness; UNH fixes part of it, and the three A&D ideas still deserve a hard look from the red team.
- **One idea deliberately waits.** UNH is `wait: true` — do not enter before Tuesday's print. That is the whole structure of the idea, not a hedge, and the edge over the baseline is claimed on variance removal rather than on a forecast of the print.
- nothing intraday cleared the bar: the market was shut all weekend, there is no 08:30 print today, and every level here comes off Friday's close. Four names were rejected in the falsification pass with the reasons recorded (LRN, CMC, CLF, AA), plus TRV and IBKR, plus tankers, LNG shipping, refiners as a new idea, airlines short, and crypto.
- **Two event-contract positions need clearing rather than re-pitching:** `KXCPIYOY-26SEP-T3.5` NO @ 18 now trades 0.12/0.14 with the market at 88% against it and resolves Wednesday; `KXFEDDECISION-26SEP-H0` refers to a meeting that has already happened. Three awaiting-entry equity levels are dead on distance: VST @132 (+22.3%), OXY @54 (+11.3%), FCX @68.20 (+8.0%).
- **coverage gaps:** no fetched index or futures context at all (Yahoo 429 across ^GSPC/^NDX/^DJI/^RUT/^VIX/ES/NQ/DXY/gold/WTI; finnhub refuses index CFDs), so SPY and QQQ closes stand in; **no options-implied-move check on any finalist** (yahoo-options 401), so nothing here has been tested against what the straddle prices; no short-interest or days-to-cover read on anything (api.nasdaq.com timeout); Brent-WTI spread not stated because sources ranged $7 to $29; 12 of 17 open positions reviewed and held with reasoning recorded rather than captured.
- **sources that failed:** Yahoo Finance chart API (429, all indices), Yahoo options API (401 Unauthorized), api.nasdaq.com short interest (read timeout), and `market_data.py events` — which is **broken rather than down**: it reads Kalshi's retired `yes_bid`/`yes_ask`/`last_price`/`volume`/`open_interest` fields instead of the current `*_dollars` and `*_fp` names, and it never paginates or filters server-side, so it only ever sees an arbitrary first 200 open markets. Worked around by calling Kalshi directly with `event_ticker=`, which returned the full CPI ladder and the Fed path on the first attempt. **Fixing that function is the single highest-value code change available to this pipeline** — it is why the event-contract lane keeps coming up empty.
