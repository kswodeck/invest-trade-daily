# Research log — 2026-09-01

## [06:03 ET] MACRO — regime snapshot (Tue 2026-09-01, pre-open; equity prices are 2026-08-31 close)
- FRED: US10Y 4.73% (2026-08-28), US2Y 4.34%, fed funds effective 3.63%, 10y-2y +41bp (2026-08-31), unemployment 4.1% (Jul). Curve positively sloped; long end elevated vs a ~3.6% policy rate = term-premium/fiscal story, not a growth story. — source: FRED via scripts/market_data.py macro
- Prior close (finnhub, asof 2026-08-31T20:00Z): SPY 767.05 (-0.30%), QQQ 716.76 (+0.05%), IWM 293.93 (-0.62%), GLD 408.42 (-0.11%), XLE 63.96 (+2.04%), TLT 82.52 (-0.43%)
- Breadth skew yesterday: energy +2.0% while small caps -0.6% and SPY -0.3%. Nasdaq flat. Commodity/inflation leadership, not risk-on.
- Crypto (coingecko, live 24/7): BTC 77,889 (-0.74% 24h), ETH 2,451.90 (+0.29%), SOL 101.96 (-1.01%)
- DATA GAPS: index quotes (^GSPC/^NDX/^DJI/^RUT), VIX, /ES, /NQ, DXY, ^TNX, gold futures, WTI all returned ok:false — yahoo 429 rate-limited, finnhub refuses index CFDs, stooq 404. Using ETF proxies (SPY/QQQ/IWM/GLD/XLE/TLT via finnhub) instead. No live VIX today.

## [06:05 ET] CALENDAR — dated catalysts inside 10 sessions (finnhub earnings, rev est > $400M)
- 09/01 amc: DELL, PANW, MDB, CRDO | bmo: MDT, NIO | M (Macy's)
- 09/02 amc: **AVGO** (rev est $29.95B, eps 3.30), HPE, SNOW, NTAP, FIVE, WOOF | bmo: OLLI, BF.B, GIII
- 09/03 amc: **LULU** (rev est $2.51B, eps 1.83) — OPEN POSITION, ZS, DOCU, PATH, GWRE, IOT | bmo: CIEN, CPB, TTC
- 09/07: GME, DBI (note: 2026-09-07 is Labor Day Monday — these dates look like finnhub placeholders, verify)
- 09/08 amc: UNFI, CASY | 09/09: KR, CHWY, ASO, SIG, AEO, RH, CPRT, AVAV
- 09/10 amc: **ADBE** | 09/14: **ORCL** | 09/15: GIS
- Macro calendar to verify by web: ISM Manufacturing (Sep 1 10:00 ET), ISM Services (Sep 3), **August jobs report Fri Sep 4 08:30 ET**, CPI ~Sep 10, FOMC Sep 16-17.

## [06:07 ET] NEWS — overnight drivers
- **US and Iran exchanged strikes** for the first time since July; WTI +3%+ on 08/31. Energy equities led (XLE +2.04%). This is the day's dominant macro driver. — source: https://www.cnbc.com/2026/08/30/stock-market-today-live-updates.html
- PG&E (PCG) -16% after California lawmakers blocked a proposal capping individual claims against utilities whose equipment ignited wildfires. — same source
- Futures pre-open (secondary source, not a fetched quote): S&P -0.27%, Nasdaq +0.06%, Dow -0.60%, Russell -0.61%. VIX ~14.92, 10Y 4.758%. — source: https://www.schwab.com/learn/story/stock-market-update-open (treat as context, not entry levels)
- LULU 08/31 volume 13.65M vs 4.2M average (3.2x) into the 09/03 print; range 118.20-124.47, close 120.26. Consensus looks for **EPS -42% YoY**; stock -42% YTD. — sources: https://stockanalysis.com/stocks/lulu/ , https://www.cnbc.com/quotes/LULU

## [06:09 ET] MACRO — the regime is a live US-Iran war, month 6+
- US struck Iranian launchers on Larak Island **in the Strait of Hormuz** Sun 08/30; Iran says it retaliated against US bases in Jordan. First US action in a month.
- Brent $90.91 (+3.2%) 08/31; WTI ~$85.02 (+1.94%). Hormuz carries ~20% of world oil shipments and traffic is already curtailed.
- US national average gasoline was **above $4/gal every day in August, the first time ever** (AAA).
- Sources: https://www.thenationalnews.com/business/energy/2026/08/31/oil-rises-to-above-90-as-us-and-iran-resume-strikes/ , https://energynow.com/2026/08/oil-jumps-more-than-3-as-u-s-iran-military-strikes-reignite-hormuz-supply-fears/ , https://fortune.com/2026/08/31/gas-prices-oil-us-iran-strikes-strait-hormuz/ , https://www.congress.gov/crs-product/R45281
- This ties the whole tape together: 10Y 4.73% with fed funds 3.63% (supply-shock inflation, not growth), gold GLD 408 near highs, XLE leading, IWM lagging. Book is ALREADY long this driver via XLE x3, DINO, DHT, CCJ — correlation cap of 3 per driver is the binding constraint today, so new energy ideas must clear a high bar or express a *different* leg of it.
- Under-covered leg worth hunting: **Qatari LNG also transits Hormuz** (~20% of global LNG). US LNG exporters are the substitution trade, and that is not in the book.

## [06:07 ET] POSITION UPDATE — BTC / /MBTU6 shorts — ALL FOUR ARE STOPPED OUT AND SHOULD ALREADY BE FLAT
- Book shows: BTC SELL 62,950 (08/16, stop 65,200), BTC SELL 63,400 (08/17, stop 65,200), /MBTU6 SHORT 64,100 (08/18, stop 66,600), /MBTU6 SHORT 64,340 (08/19, stop 66,600).
- BTC is 77,889 right now (coingecko, live). Every one of those stops was taken out weeks ago; the marks in prior_context showing "—" are a tracking artifact, not open risk.
- **Decision: closed, at the stop, not at the current print.** Loss is roughly -3.5% on the spot shorts and -3.9% on the futures. Do not re-mark them to 77,889 and do not roll them.
- Lesson for today: that was a four-line bet on ONE view (BTC lower) taken across four days, which is exactly the correlation-cap failure `config/strategy.md` warns about. It also went the wrong way into a geopolitical bid for hard assets — the same bid that has GLD at 408.
- No new BTC recommendation today: at 77,889, +23% above where the short thesis was framed, there is nothing left of the original setup and re-shorting a trend after being run over is revenge, not analysis.

## [06:08 ET] POSITION UPDATE — LULU — opened 2026-08-22 @115, last 120.26 (+4.6%)
- decision: HOLD, do not add before the 09/03 print; captured via add_candidate.py with entry re-cast as a post-print accumulation zone and `wait: true`
- why: FY26 guidance EPS 10.95-11.15 (cut from 12.10-12.30 in June) puts the stock at ~10.9x its own reset number; Q2 bar is management's 1.76-1.81 vs 2.68 pre-cut consensus. Bear case 88 = 11x on 8.00 EPS. R:R from 112 = (175-112)/(112-88) = 2.63.
- 08/31 volume 13.65M vs 4.2M avg = crowded into the print, which is why adding beforehand is the wrong move even holding the thesis.

## [06:14 ET] EVENT CONTRACTS — August CPI YoY (Kalshi KXCPIYOY-26AUG, resolves 2026-09-11 08:30 ET)
- Verified Robinhood carries it: https://robinhood.com/us/en/prediction-markets/economics/events/inflation-in-august-2026-cpi-yoy-sep-11-2026/
- Live ladder (Kalshi API, yes_bid/yes_ask in cents), and note the strike convention: T3.3 YES pays if the *reported* one-decimal print is >= 3.4.
  - T3.2 (>=3.3 printed) 80/89 | T3.3 (>=3.4) 45/57 | T3.4 (>=3.5) 16/20 | T3.5 (>=3.6) 1/5
  - Implied: P(>=3.3)=84.5%, P(>=3.4)=51%, P(>=3.5)=18%. Deep liquidity: T3.3 has 58.5k volume / 40k OI.
- Arithmetic from FRED CPIAUCNS: Jul-26 = 333.918, Aug-25 base = 323.976. Jul YoY = 3.365%. For a reported 3.4% the Aug index must land 334.83-335.15, i.e. **MoM +0.274% to +0.370%**. Reported 3.3% needs MoM +0.177% to +0.274%.
- Base rate: August NSA MoM 2010-2025 averages **+0.157%**, and cleared +0.274% in only 6 of 16 years (37.5%).
- The bull case for a hot print is gasoline: GASREGW August weeks 4.079 / 4.006 / 4.049 / 4.085 vs July 3.777 / 3.855 / 4.001 / 4.096, so ~+3.1% MoM on a ~3.1% CPI weight = **+0.09pp** above a seasonally normal August. That lifts the historical hit rate to roughly 44%.
- **REJECTED — KXCPIYOY-26AUG — my estimate P(>=3.4) is 44-50% against a 51% market. That gap is smaller than my own modelling error, so there is no stated probability disagreement to trade.** Recording it because the ladder is worth re-checking after Friday's jobs print, not because it is actionable today.

## [06:10 ET] THEME — the Hormuz LNG shock is the under-covered leg, but the obvious expression is wrong
- Iranian missiles hit **Ras Laffan** (world's largest LNG export hub) in March 2026, taking ~17% of Qatar's export capacity offline. QatarEnergy has since extended **force majeure** on European and Asian supply, with Pakistani cargo cancellations now running into October/November. LNG through Hormuz has contracted ~95%; pre-war roughly a fifth of global LNG traded through the strait.
- Sources: https://www.euronews.com/business/2026/08/31/qatarenergy-extends-lng-cancellations-into-november-as-hormuz-disruption-drags-on , https://www.csis.org/analysis/battle-hormuz-will-reshape-global-lng-market , https://www.gisreportsonline.com/r/gas-markets-hormuz-shock/ , https://news.un.org/en/story/2026/08/1168074
- **FALSIFICATION — the domestic gas producer trade does not work and the tape says so.** UNG is 10.54, **-38% off its 200-day range high of 17.03 and below its 200-day SMA of 11.81**, after six months of the worst LNG supply shock on record. EQT 54.18 sits below its 200-day SMA (56.24) and 20.6% off its high; AR 38.48; RRC 41.32. On 08/31 UNG rose 2.0% while EQT fell 0.7% and RRC fell 0.3%.
- The reason is structural, not sentiment: Henry Hub is a domestic market and US export capacity is a fixed physical constraint. Terminals were already running near nameplate, so a global shortage cannot pull materially more molecules out of Appalachia. **REJECTED — EQT / AR / RRC — the shortage is offshore, the bottleneck is liquefaction and shipping, and the producers are not the ones capturing it.**
- The economics land instead on (a) whoever owns merchant/spot LNG volumes and captures the JKM-vs-Henry-Hub spread, and (b) **ton-miles** — replacing Qatar-to-Asia with US-Gulf-to-Asia is roughly triple the voyage distance for the same cargo, which tightens the carrier fleet without a single new molecule.

## [06:13 ET] FERTILIZER — the second-order Hormuz trade is real, and both expressions fail on entry
- Mechanism confirmed: the Middle East is ~35% of globally traded urea and ~30% of traded ammonia. Iran halted ammonia production; Qatar suspended urea, ammonia and sulfur after facility damage. Urea went ~$400/mt to >$850/mt in April before falling back to $453/mt in June. World Bank warned fertilizer could rise 30%+ in 2026 if the disruption persists. — sources: https://blogs.worldbank.org/en/opendata/fertilizer-prices-surge-as-strait-of-hormuz-disruptions-tighten- , https://www.wto.org/english/blogs_e/data_blog_e/blog_dta_10jul26_451_e.htm , https://www.cnbc.com/2026/03/25/fertilizer-price-iran-war-food-security-inflation-urea-potash-nitrogen-farmers.html
- **REJECTED — CF — the news is in the price and the direction of the commodity has turned.** CF closed 130.03 (+3.37%), +62% YTD, 8.4% off a record 141.96, above every SMA (20d 121.80 / 50d 118.55 / 200d 107.02). Tampa ammonia settled **$635/mt for August, down from the first-half peaks** — the margin driver is moderating while the equity sits at a record. Zero open-market insider buys in six months against 34 sales worth $60.65M.
- **REJECTED — LXU — the laggard has a company-specific reason for lagging, and it is insider distribution.** LXU 10.67 is -38% off its 17.22 high and below both its 50d (10.75) and 200d (11.45) while CF made a record; ADV $8.6M so liquidity is fine. But six-month insiders show **$76.13M of sales against $9,890 of buying (one 1,000-share purchase at 9.89 on 08/12)** — roughly 10% of a ~$740M market cap sold. Q2 was fine on its own terms (adj EBITDA $53M, +40% YoY, on $168M sales, absorbing a $35-40M turnaround hit). A supply overhang that size is why a good quarter did not move the stock, and it is not something a thesis outruns.
- Also looked at and passed: UAN 126.40 (pure nitrogen but ADV only $7.0M on 55.7k shares/day, and it is a variable-distribution MLP), MOS, IPI, NTR, ICL.

## [06:14 ET] POSITION REVIEW — all 21 open lines re-marked against 08/31 closes (finnhub)
| Symbol | Entry | Stop | Now | Status | Decision |
| --- | --- | --- | --- | --- | --- |
| TJX | 150.85 | 145.50 | 133.91 | **STOP BLOWN by 8.0%** | **CLOSED at 145.50 (-3.5%). Do not carry it.** |
| BTC/MBT x4 | 62,950-64,340 short | 65,200/66,600 | 77,889 | STOP BLOWN weeks ago | CLOSED at the stops (see 06:07 entry) |
| DINO | 93.00 | 86.50 | 101.61 | +9.3%, target 108 is 6.3% away | HOLD, **raise stop to 95.00** |
| XLE (08/16 tranche) | 60.50 | 58.60 | 63.96 | +5.7%, target 64.50 is 0.8% away | HOLD, **trim that tranche into 64.50** |
| XLE (08/15, 08/18) | 60.80 | 57.80 / 59.20 | 63.96 | +5.2%, targets 67.0 / 66.5 | HOLD unchanged |
| BCC | 81.00 | 76.00 | 78.01 | -3.7%, only 2.6% above the stop | HOLD, stop unchanged — do not widen it to avoid being wrong |
| PFE | 25.80 | none | 28.46 | +10.3%, target 38 | HOLD |
| DINO/CCJ/LCII/NKE/DHT/SVRA/TLT | — | — | — | inside their bands | HOLD unchanged |
| CCJ | 95.00 / 88.00 | none | 98.76 | +4.0% | HOLD |
| LCII | 94.00 | none | 100.63 | +7.1% | HOLD |
| NKE | 40.00 / 38.00 | none | 39.06 | -2.4% / +2.8% | HOLD |
| DHT | 18.80 / 19.40 | 17.60 / 17.90 | 19.60 | +4.3% / +1.0% | HOLD |
| TLT | 82.60 | 80.95 | 82.52 | flat | HOLD |
| SVRA | 5.35 | 4.60 | 5.39 | +0.7% | HOLD |
- **Pattern worth naming: two of the six lines carrying a hard stop (TJX, and the four BTC shorts) are sitting in the book well past their stops.** The 0/9 track record is partly a bookkeeping failure, not only a selection failure — positions that stopped out are still being carried and re-marked. Stops that are not honoured are not risk controls.

## [06:15 ET] POSITION UPDATE — DINO and XLE are management decisions, not new entries, and are deliberately NOT captured as candidates
- DINO 101.61: +90% off its 6-month low (53.39) and 1.3% below its 6-month high (102.98); ATR14 3.68; sma20 91.92. **Decision: hold, trail the stop up to 95.00 (about 1.8 ATR below spot, under the 08/24-08/25 consolidation at 93-95), trim into the 108 target.**
- XLE 63.96: 1.1% below its 6-month high (64.70); ATR14 1.09. **Decision: hold all three tranches; trim the 08/16 tranche into its 64.50 target, which is 0.8% away.**
- **Why these are not in candidates.jsonl:** entering DINO at 101.61 against a 95.00 stop and a 108 target is R:R 0.97, and XLE at 63.96 against a 64.50 target is worse. Both fail the 2.0 swing floor as *new* entries, and `config/strategy.md` is explicit that the floor exists to reject ideas rather than to calibrate targets. Nudging the DINO target to 115 to make the arithmetic pass would be exactly the failure this pipeline was built to catch.
- **Instruction to synthesis: carry DINO, XLE, TJX and BCC in the WATCHLIST as open-position management notes, not as recommendations.** TJX is closed at its 145.50 stop; BCC holds with its 76.00 stop unchanged.

## [06:17 ET] MACRO — the biggest thing in the tape: the market prices a Fed HIKE on 09/16
- Kalshi KXFEDDECISION-26SEP (close 2026-09-16 17:59Z), deep liquidity: **Hike 25bp 57/58c (5.31M contracts, 3.22M OI)**, Fed maintains 41/42c (9.64M contracts), Hike >25bp 1/2c, Cut 25bp 0/1c. Curve out: Oct hike 26/27c, Dec hike 42/44c.
- Driver: **Chair Kevin Warsh's Jackson Hole keynote on 08/28** recommitted to the 2% PCE target and said "this summer's inflation readings were better than expected... they do not tell me that underlying trends have meaningfully improved." CME FedWatch moved to **60.4%** for a September hike, from ~56% on Friday. Deutsche Bank looks for +50bp this year (September and December).
- The public dissent is unusually senior: Treasury Secretary Bessent — "It is my belief that we've seen a supply shock, and traditionally you don't raise into a supply shock unless you see second- or third-order effects."
- Sources: https://www.federalreserve.gov/newsevents/speech/warsh20260828a.htm , https://www.cnbc.com/2026/08/31/stock-market-today-live-updates.html (Jackson Hole roundup), https://www.cnbc.com/2026/08/31/markets-see-warsh-endorsing-a-rate-hike-in-september-not-everyone-is-convinced.html , https://www.npr.org/2026/08/28/nx-s1-5947903/federal-reserve-inflation-jackson-hole-interest-rates
- **REJECTED — KXFEDDECISION-26SEP-H25 — no probability disagreement worth trading.** Kalshi 57-58 against CME fed funds futures at 60.4 is a ~3-point gap in the same direction, i.e. Kalshi is marginally cheap rather than wrong, and 3 points does not survive the spread. The prior report already took the YES side at 32c on 08/22; it is now 57c, so the original call was right and the remaining edge has been paid out. Buying it again here is chasing my own winner.
- **This reprices everything else in the report, and it is the single most useful thing to carry forward:** a 57% chance of a HIKE, not a cut, with the 2Y at 4.34% already 71bp above a 3.63% effective funds rate. It is a headwind for gold (GLD at 408 near its high is fighting it), a headwind for small caps carrying floating-rate debt (IWM -0.62% on 08/31 while QQQ was flat), and the strongest argument for owning things whose cash flows rise with the supply shock rather than things discounted by the rate that fights it.
- **The 09/04 08:30 ET August jobs report is the swing factor** — unemployment last printed 4.1%. An uptick collapses the 57%, and a hot number cements it.

## [06:19 ET] DEFENSE — the sector is down hard in a war year, and it is not a mispricing
- Backdrop is as strong as it gets: the White House requested **$87.6B in emergency supplemental** for Operation Epic Fury (the US-Iran war began 2026-02-28), a $67B FY26 supplemental is proposed, the FY27 request seeks **+42%**, Deputy SecDef Feinberg gave contractors three weeks to produce faster-delivery plans, and **LMT was awarded $35.3B** to rebuild consumed missile-defense stockpiles. — sources: https://www.washingtonpost.com/politics/2026/08/08/iran-war-weapons-stockpile-pentagon-defense-industry/40384f66-9396-11f1-9fdc-0a725c989a7b_story.html , https://www.cnbc.com/2026/08/09/pentagon-defense-contractors-weapons-production.html , https://www.techtimes.com/articles/319033/20260625/iran-war-supplemental-pentagon-requests-876b-munitions-stockpiles-run-low.htm , https://www.defenseone.com/business/2026/08/theres-no-shortcut-replenish-us-munitions-stockpiles/415558/
- And yet on 08/31, the day the US struck Iran and Brent rose 3.2%, the whole group **fell**: ITA -1.92%, XAR -2.01%, GD -2.10%, RTX -1.88%, KTOS -1.96%, NOC -1.08%. The tape is not confused; the money is not flowing yet. NBC: "The Pentagon has no new munitions contracts amid concerns about a weapons shortage." — https://www.nbcnews.com/politics/national-security/pentagon-no-new-munitions-contracts-concerns-weapons-shortage-rcna342451
- **REJECTED — AVAV — the 64% drawdown is a broken acquisition, not a de-rated war winner.** 148.35, -63.7% from a 408.25 high and only 9.7% off the 135.20 low, with the 200-day at 215.53. Cause is company-specific: a ~46% adjusted-EPS miss, FY26 EPS guidance cut to $3.40-3.55 from $3.60-3.70, **$151M of goodwill impairment**, and FY26 guided to a net loss of $201-218M (loss per diluted share $4.10-4.44) as the BlueHalo integration goes badly. Reports 09/09. Zero open-market insider buys in six months. A loss-making integration story is not the way to own a munitions cycle.
- **REJECTED — KTOS — same drawdown, worse insider tape.** 50.98, -62.0% from 134.00, 200-day at 72.10, and **140 insider sales worth $39.25M against zero open-market purchases** in six months.
- LMT 561.23 is the only one with a defensible chart (200-day 555.44, ATR 2.36%, ADV $550M) but it sits below its 20-day (582.72) with no dated catalyst inside ten sessions, and the $35.3B award is public. Not enough to publish; noting it as the sector's re-entry vehicle if awards start landing.

## [06:20 ET] TANKERS — why the book keeps getting stopped out of DHT, and why I am not adding to it
- On 08/31 crude rose 3.2% and the tanker complex did **not** follow: DHT -0.31%, FRO -0.93%, INSW -0.17%, TNK +1.06%. That is not noise, it is the mechanism: a Hormuz closure raises the *price* of crude by removing barrels, but it simultaneously removes **VLCC loadings out of the Gulf**. Fewer cargoes is bearish tanker demand even as it is bullish the barrel. The ton-mile gain from re-routing only pays if the tonnes still move.
- This is the missing piece behind the track record. `DHT` has been recommended **5 times in ten days and stopped out 3 times** (08/23, 08/24, 08/26 entries, all stopped 08/26). Re-pitching it as an oil proxy is the anchoring failure `prior_context.md` warns about, and the instrument does not do what the thesis assumes.
- **Decision: hold the two existing DHT lines on their stops (17.60 / 17.90), add nothing, and do not open FRO / INSW / TNK.**
- Same reasoning shuts down a fifth energy long. XLE (three tranches) + DINO already put four open lines on "the oil supply shock persists". `config/strategy.md` caps correlated ideas at three per driver, so PBF (72.99, the most beaten-down refiner) and VLO (358.92) are **REJECTED on the correlation cap, not on the merits** — the crack-spread case with gasoline above $4 all August is good, and there is simply no room for it.

## [06:23 ET] LONG_TERM — GLNG (Golar LNG), captured. The scarce asset is liquefaction, not molecules.
- Verified tradeable on Robinhood: https://robinhood.com/us/en/stocks/GLNG/ (page shows Golar LNG Ltd, mkt cap 5.23B). ADV $65.5M on 1.27M shares — liquidity is not an issue.
- Balance sheet at 2026-06-30: gross debt $2,717,707k, cash $1.16B, **net debt ~$1.60B**; 101.76M shares; at 51.49 that is a $5.23B cap and ~$6.8B EV.
- Guidance: **~$800M run-rate adjusted EBITDA by 2028** (Gimi + Hilli + Esperanza), >$1.2B by 2030 if the fourth unit contracts like Esperanza. So today is **8.6x 2028**, before commodity upside, on 20-year contracts.
- Contract quality is the part that makes it a long_term rather than a story: Hilli's 20-year SESA Argentina deal is $285M/yr adj EBITDA to Golar **plus 25% of FOB prices**; Hilli ran 100% uptime and finished its 8-year Cameroon contract; Gimi is running ~15-19% above its contracted base rate; the fourth Mark II with CIMC Raffles lifts controlled capacity **+41% to over 12 mtpa**.
- **Entry is deliberately below the market (41-47, ideal 44) and it is not reverse-engineering — it is what the arithmetic requires.** At today's 51.49 against a 36 bear case and a 65 target, R:R is 1.85 and fails the 2.5 long-term floor. At 44 it is 2.63. The idea is good; the price is not, so it goes in as an accumulation with `wait: true` and may sit unfilled. Zero insider data is uninformative — Golar is a foreign private issuer and does not file Forms 4.

## [06:27 ET] EVENT CONTRACTS — AAA national gas price on Sep 30 (Kalshi KXAAAGASM-26SEP30, Robinhood carries the gas-price category)
- **Live fetched underlying: AAA national average regular = $4.0954 as of 2026-09-01** (yesterday $4.0807, week ago $4.0969, month ago $4.1013, year ago $3.1909 — so +28.4% YoY and dead flat for a month). — source: https://gasprices.aaa.com/
- Ladder (yes_bid/yes_ask, resolves on AAA's Sep 30 print): >4.00 **58/68**, >4.10 **31/41**, >4.20 14/19, >4.30 8/11, >4.40 8/13, >4.50 7/12. The >3.70 (26/87) and >3.90 (49/90) quotes are stale-wide and untradeable.
- Base rate from FRED GASREGW, last weekly August observation vs last weekly September observation, 2006-2025: **mean -1.68%, median -0.92%, negative in 12 of 20 years**, range -16.4% to +7.7%. Applied to 4.0954 the median lands at $4.058 and the mean at $4.027.
- Offsetting force: Brent rose 3.2% to $90.91 on 08/31 and retail lags crude by roughly two weeks, so pass-through of ~50-60% adds an estimated 5-7c (about +1.6%) into mid-September, against the post-Labor-Day winter-blend switch and demand fall in the back half.
- Net: my estimate for P(AAA > $4.10 on Sep 30) is roughly **45-50%** against a 31/41 market (36 mid).
- **REJECTED — KXAAAGASM-26SEP30-4.10 — and rejected on the same standard I applied to the CPI ladder at 06:14, deliberately.** The estimated edge is 4-9 points, buying the offer costs 10 points of spread, and both the seasonal base rate and my crude pass-through figure are my own models rather than measurements. Volume is 1,418 contracts with 719 OI. A 6-point edge inside a 10-point spread is not an edge. Checked >4.00 (est. 65% vs a 68 ask) and >4.20 (est. ~15% vs 14/19) as well; neither is better.
- **No event contract is published today.** Three ladders were priced and worked through — Fed September, August CPI, September gas — and all three were within my own error bars. That is a real outcome for the day, not a gap in coverage.

## [06:28 ET] EVENT CONTRACTS — August unemployment (KXU3-26AUG, resolves Fri 09/04 08:30 ET). Rejected, but the pricing is the day's most important macro fact.
- Ladder, and note the spreads are **1-3 cents wide on 206k / 80k / 28k contracts** — this is the efficiently priced one: >4.0% 81/83, **>4.1% 51/52**, >4.2% 21/24, >4.3% 4/5.
- Implied distribution off a 4.1% July print: P(>=4.1) 82%, **P(>=4.2) 51.5%**, P(>=4.3) 22.5%; so P(4.1) ~30%, P(4.2) ~29%, P(<=4.0) ~18%.
- **REJECTED — KXU3-26AUG — I have no differentiated view on a payroll print, and a 1-cent spread on 206k contracts is the market telling me it does not need my opinion.**
- **But read the two ladders together and the regime is explicit: the market simultaneously prices a 51% chance unemployment RISES to 4.2%+ and a 57% chance the Fed HIKES on 09/16.** That is stagflation being priced directly, and it is the correct frame for the whole report: a policy rate going up into a weakening labour market, driven by a supply shock the Fed cannot fix.
- Consequence for the IWM short captured at 06:19: the 09/04 print cuts both ways within the same week — a rising unemployment rate collapses the hike odds (bad for the short near term) while confirming the growth problem (good for it later). The captured `catalyst.action` already says to stand down rather than hold through the print; that instruction is deliberate and should survive synthesis.
- Also noted, not actionable: analysts are now publishing $5,000/oz year-end gold targets while GLD sits at 408.42 near its high. Gold is fighting a hiking Fed and winning, which is the same debasement bid that ran over the book's BTC shorts.

## [06:29 ET] VERIFICATION — dates and instruments checked rather than assumed
- **LULU 09/03 confirmed from the company itself**: lululemon announced on 08/20 (Business Wire) that Q2 FY26 results are released **Thursday, September 3, 2026**, with the call at 4:30pm ET. The captured catalyst timestamp of 2026-09-03T16:05 is right. — https://secure.businesswire.com/news/home/20260820681602/en/lululemon-athletica-inc.-announces-second-quarter-fiscal-2026-earnings-conference-call
- **UAL re-captured with `datetime_et: null`.** The first capture asserted a 2026-10-14 Q3 date that I had not verified; UAL reports "mid-October" but no confirmed date was published, so asserting one would have been a fabricated figure. The candidate now says plainly that there is no dated catalyst, which is also the reason it is conviction 2.
- **PCG re-captured with a day-level `datetime_et` of 2026-09-01.** The vote is confirmed for Tuesday but the time of day is not published, and the original 12:00 ET stamp was invented precision.
- **GLNG tradeability verified on Robinhood's own page** (Golar LNG Ltd, $5.23B cap) rather than assumed — it is a Nasdaq-listed common share, not a foreign ordinary or an ADR.
- **Instrument substitutions I wanted and could not make honestly:** `config/universe.md` prefers /M2K over IWM and /MGC over GLD, but ^RUT, ^GSPC, ^NDX, ^DJI, VIX, DXY, gold and WTI all failed on every source this morning (finnhub refuses index CFDs, yahoo 429, stooq 404). Quoting futures levels I could not fetch would be exactly the fabrication this pipeline exists to prevent, so the index short is the ETF and carries `requires_margin: true`.
- **GLD not re-pitched.** It closed 408.42, 2.5% above the 398.00 entry published on 08/22 and never filled. Re-pitching the same idea 2.5% higher because it went up is chasing, and gold is additionally fighting a Fed the market thinks hikes in two weeks.

## [06:30 ET] ECON CALENDAR — this week, all times ET
- **Tue 09/01 10:00** — ISM Manufacturing, and **JOLTS** job openings (same slot)
- **Wed 09/02 08:15** — ADP National Employment Report
- **Thu 09/03** — jobless claims and ISM Services
- **Fri 09/04 08:30** — **Employment Situation: nonfarm payrolls and the unemployment rate.** This is the week's event; the Kalshi ladder prices a 51% chance the rate rises to 4.2%+ from 4.1%.
- **Fri 09/11 08:30** — August CPI (market centres on 3.3% YoY)
- **Wed 09/16 14:00** — **FOMC decision.** Market: 57-58c on a 25bp HIKE, 41-42c on no change.
- Source: https://www.investing.com/news/stock-market-news/manufacturing-pmi-ism-pmi-and-jolts-job-openings-due-tuesday-93CH-4883128 , https://www.newyorkfed.org/research/calendars/i-sep26.html , https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar

## [06:31 ET] FALSIFICATION — the case against each of the five, and whether it survives
1. **GLNG (conviction 3, long_term).** Against: Golar has promised for a decade that the next unit re-rates it, and the shares sit 10.9% below their own 12-month high in the middle of the largest LNG supply shock on record — the market is voting against the 2028 number. Argentina is the anchor counterparty. My $2.2B 2028 net-debt figure is an estimate, not a disclosure. **Survives, but only because the entry is 15% below the market.** At 51.49 the R:R is 1.85 and it would not publish at all; at 44 it is 2.63. It may sit unfilled and that is the correct outcome.
2. **IWM short (conviction 3, swing).** Against: a hike is 57% priced, not 0% priced, and IWM is only 3.7% off its 52-week high with a 0.96% ATR — an orderly pullback, not a breakdown. It also stacks with the SPY short published 08/31 at 773, so the book would carry **two index shorts that die on the same headline**. **Survives** on the strength of the entry (short into a 296.50-301.50 bounce, not at 293.93) and a hard dated catalyst, but synthesis should treat IWM and SPY as one position for sizing, not two.
3. **LULU (conviction 3, long_term, position update).** Against: brands rarely recover a premium multiple once taste moves on, and 11x is a bet on taste. **Survives as a HOLD, not as an add** — and the distinction is the whole recommendation. `wait: true` is doing real work here; adding before a print where 13.65M shares traded into a 4.2M average would be the mistake.
4. **PCG (conviction 2, long_term).** Against: utility specialists moved $8B-plus across PCG and EIX in one session after reading the full bill text; assuming they overreacted because two sell-side targets lag by a day is weak. **Survives only at 1% size, below the market, and with `wait: true`.** If the AB 1054 liability cap does not survive the passed text, this idea should be killed outright rather than trimmed.
5. **UAL short (conviction 2, swing).** Against: already 22.2% off its high at ~12x the midpoint of its own cut guidance, airfares +26% YoY, five points of capacity coming out — that is the discipline that protects pricing. No dated catalyst. **Weakest of the five and marked as such.** Survives at 1% with a stop, because the entry is 5% above the market and will only fill on a bounce that would itself improve the setup.
- **Correlation audit.** New ideas by driver: *Hormuz/oil persists* — UAL short and GLNG long (2). *Fed hikes / rates up* — IWM short (1, plus the published SPY short). *Idiosyncratic* — LULU, PCG (2). Within the 3-per-driver cap on new ideas. **But the combined book is not**: XLE x3 + DINO + UAL + GLNG is six lines on the war, and that concentration is the single biggest risk in the report, not any individual idea.

## [06:32 ET] STAPLES — the uncorrelated lane I wanted, and it does not clear the bar
- The complex is at multi-year lows and is genuinely uncorrelated with the war and the rate path: GIS 41.20, CPB 23.68, KHC 25.67, CAG 16.02, HRL 21.85, SJM 131.16. GIS has just crossed back above its 200-day (40.05) after a long decline and reports 09/15, inside the window.
- **REJECTED — GIS — cheap on the multiple, but the earnings are going the wrong way.** FY27 guidance is adjusted diluted EPS **$3.00-3.20** with adjusted operating profit **down 8-13%** in constant currency off a $2.8B FY26 base, and organic sales -1.5% to +0.5%. At 41.20 that is 12.9-13.7x a *declining* number, with a dividend consuming roughly three quarters of it, and no insider has bought in six months against $958k of sales. "Cheap and shrinking" is not a durable mispricing, and a bond-proxy yield is the wrong thing to own two weeks before a Fed the market thinks hikes.
- **REJECTED — CPB — same category problem, one degree better on the tape.** 23.68, -30.7% off its 34.18 high, above its 20-day and 50-day, ADV $125M, and the only insider signal in the whole staples group: **zero sales in six months and three small open-market purchases by a Dorrance family director at 21.45 on 06/09** (only $6,435, so it is a token, not a cluster). Reports 09/03 bmo. Worth carrying on the watchlist for the print; not worth publishing on a $6k signal.

## [06:33 ET] ARITHMETIC CHECK — recomputed independently from candidates.jsonl, not from what I wrote about my own ideas
| Symbol | Horizon | Dir | Conv | Size | Entry | Target | Downside | R:R | Floor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GLNG | long_term | buy | 3 | 3% | 44.00 | 65.00 | 36.00 (bear) | **2.62** | 2.5 OK |
| IWM | swing | sell_short | 3 | 2% | 298.50 | 274.00 | 305.50 (stop) | **3.50** | 2.0 OK |
| LULU | long_term | buy | 3 | 3% | 112.00 | 175.00 | 88.00 (bear) | **2.62** | 2.5 OK |
| PCG | long_term | buy | 2 | 1% | 12.40 | 21.00 | 9.50 (bear) | **2.97** | 2.5 OK |
| UAL | swing | sell_short | 2 | 1% | 113.50 | 92.00 | 122.50 (stop) | **2.39** | 2.0 OK |
- Five distinct symbols across seven lines (UAL and PCG were each re-captured to remove an invented catalyst timestamp; synthesis takes the last line per symbol). Total capital at risk 10%. No ratio sits suspiciously just above its floor — the two closest, LULU and GLNG at 2.62, are there because the entry was set below the market rather than because the target was raised to fit.

## [06:34 ET] RESEARCH COMPLETE
- **candidates: 5 distinct symbols (7 lines) — GLNG, IWM, LULU, PCG, UAL.** Skew is deliberate: 3 long_term, 2 swing, 0 intraday. Nothing intraday cleared the bar; with equities closed and the index/VIX feeds all down, there was no honest way to set an intraday level this morning.
- **Zero event contracts published, from three ladders actually priced and worked through** (Fed September 57/58c, August CPI, September AAA gas). Each was inside my own modelling error and all three are written up with the arithmetic. That is a result, not a coverage gap.
- **Documented rejections: EQT/AR/RRC, CF, LXU, UAN, AVAV, KTOS, PBF/VLO (correlation cap), FRO/INSW/TNK, GIS, CPB, GLD (chasing), and the three event ladders.**
- **Position management: TJX and all four BTC//MBT shorts are past their stops and must be marked closed, not carried.** DINO trails to a 95.00 stop, the 08/16 XLE tranche trims into 64.50, BCC holds its 76.00 stop, LULU holds without adding into 09/03. DINO, XLE, TJX and BCC belong on the watchlist as management notes, not as recommendations — their R:R as *new* entries is below floor.
- **coverage gaps:** no live VIX, DXY, ^GSPC/^NDX/^DJI/^RUT, gold or WTI quote all morning, so the report has no futures idea and the index short is an ETF rather than /M2K. Did not reach: Asia/Europe overnight tape, SEC 8-K sweep beyond GLNG, small-cap screening beyond the fertilizer and defense names, or crypto beyond spot prices.
- **sources that failed:** yahoo finance (HTTP 429 on every index symbol, all morning), finnhub index CFDs (subscription required), stooq (404 on all index tickers), alphavantage (no api key), `market_data.py events` (returns unfiltered Kalshi page-1 parlay noise — I queried the Kalshi series and event endpoints directly instead, which is the workaround worth keeping), SEC EDGAR direct fetch (403), globenewswire (timeout).
