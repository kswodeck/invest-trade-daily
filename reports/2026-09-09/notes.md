# Research log — 2026-09-09

## [06:02 ET] SETUP
- Session: pre-market. Last equity prints are 2026-09-08 close (age ~842 min). Per CLAUDE.md that is a closed market, not stale data.
- market_data.py macro: index quotes (^GSPC/^NDX/^DJI/^RUT) all FAILED — finnhub requires CFD subscription, Yahoo returning 429, stooq 404. Use ETF proxies (SPY/QQQ/IWM) instead.
- quote subcommand via finnhub is WORKING for equities/ETFs.

## [06:02 ET] BOOK — closes 2026-09-08 vs prior_context "last" (which was 09-05 close)
- CCJ 101.97 (+1.2%), open BUY @94.0 → +8.5%
- NKE 38.10 (-0.8%), open BUY @40.75 → -6.5%
- BCC 76.86 (-3.0%), open BUY @76.50 → +0.5%
- TLT 82.20 (flat), open BUY @82.60 → -0.5%
- GLD 399.72 (-1.7%), open BUY @398.0 → +0.4%
- LULU 103.19 (+2.6%), open BUY @115.0 → -10.3%
- SVRA 5.53 (+3.0%), open BUY @5.35 → +3.4%
- SPY 765.96 (-0.5%), open SELL_SHORT @773.0 → +0.9% in favour
- XLE 64.77 (+1.1%) — pending BUY @63.90 still unfilled, market above
- DG 127.87 (-4.0%) — pending BUY @134.50 now BELOW market entry level; DG has crossed through
- DINO 108.31 (+2.8%) — pending BUY @99.50, market well above
- CEG 299.05 — pending BUY @272.0, market well above
- EEM 68.83 — pending BUY @65.60, market well above

## [06:05 ET] MACRO — the regime is an oil supply shock
- 2026-09-08 close: Dow -600pts to 52,786.07; S&P 500 7,673.52; Nasdaq 26,421.41. Sector rotation: healthcare and financials led declines; **energy, power and technology were the biggest gainers**. — source: https://investrade.com/market-review-september-08-2026/
- Oil is the centre of the tape. Brent traded as high as ~$99 intraday, WTI above $90, on renewed Middle East fighting **including attacks on Saudi energy facilities**. — source: https://investrade.com/market-review-september-08-2026/
- WTI settled 94.24 on 2026-09-08, +3.01% d/d. Brent above $98 after Iran said an Oman agreement to manage Strait of Hormuz shipping was nearing completion — read as Tehran gaining control of the waterway. Oil +~10% last week on renewed US-Iran fighting. — source: https://tradingeconomics.com/commodity/crude-oil
- EIA STEO: OPEC+ still unwinding the 2.2 mb/d cut through Sept 2026, but raises estimated Middle East shut-in production on Hormuz transit constraints; expects most regional output back near pre-conflict averages only in **early 2027**. — source: https://www.eia.gov/outlooks/steo/report/global_oil.php
- Healthcare selloff cause: Novartis (NVS) -12% on Phase 3 del-desiran failure in myotonic dystrophy type 1 (no significant improvement), plus a second failed trial; read-across dragged AMGN, DYN, SRPT. XLV -2.52%. — source: https://investrade.com/market-review-september-08-2026/
- FRED as of fetch: US10Y 4.78 (2026-09-04, prev 4.77), US2Y 4.37, 10y-2y +0.41 (2026-09-08), fed funds effective 3.63 (2026-09-07), unemployment 4.1% (Aug), CPIAUCSL 332.813 (Jul).
- Crypto (coingecko): BTC 78,974 (+0.39% 24h), ETH 2,490.34 (+0.07%), SOL 103.57 (+0.02%). Flat — crypto is not participating in the macro shock either way.
- DATA GAP: index quotes (^GSPC/^NDX/^DJI/^RUT) all failed — finnhub needs a CFD subscription, Yahoo 429, stooq 404. Using SPY/QQQ/IWM as proxies throughout.
- DATA GAP: `market_data.py events` returns unrelated sports shard tickers for "Fed" and zero rows for "CPI"/"interest rate". No usable event-contract pricing this run.

## [06:06 ET] SECTOR TAPE — 2026-09-08 closes (finnhub)
- Up: USO +2.87%, SMH +1.19%, XLE +1.11%, XLU +0.86%, XLK +0.32%
- Down: XLV -2.52%, XLF -1.38%, KRE -1.28%, XBI -1.15%, GDX -0.86%, SLV -0.75%, UNG -0.95%, XLP -0.66%, SPY -0.55%, IWM -0.45%
- Reads as: supply-shock energy bid, defensive utility bid, tech intact, and everything rate-and-credit sensitive sold. Gold sold WITH equities, which is a rates story rather than a risk story (10Y 4.78).

## [06:07 ET] LEVELS (200 bars, nasdaq via market_data.py history, through 2026-09-08)
- XLE 64.77 | ATR14 1.133 (1.75%) | sma20 63.10 sma50 59.42 sma200 54.93 | 200d range 43.77-65.52 | -1.14% off high | $1,713M/d
- DINO 108.31 | ATR14 3.968 (3.66%) | sma20 97.38 sma50 89.07 sma200 65.90 | range 45.71-109.86 | -1.41% off high | $288M/d
- CCJ 101.97 | ATR14 4.18 (4.10%) | sma20 100.08 sma50 95.34 sma200 105.46 | range 77.70-135.24 | -24.6% off high
- CEG 299.05 | ATR14 9.21 (3.08%) | sma20 280.09 sma50 267.12 sma200 296.16 | range 228.63-380.78
- VST 151.72 | ATR14 4.75 (3.13%) | sma20 142.32 sma50 149.41 sma200 157.65 | range 132.66-189.29
- GLD 399.72 | ATR14 8.59 (2.15%) | sma20 409.75 sma50 389.40 sma200 415.58 | range 363.32-509.70 | -21.6% off high
- SLV 59.37 | ATR14 1.845 (3.11%) | sma20 60.07 sma50 56.13 sma200 65.39 | range 44.76-109.83 | -45.9% off high
- GDX 98.41 | ATR14 3.92 (3.99%) | sma20 97.25 sma50 84.84 sma200 89.98
- ORCL 162.52 | ATR14 6.76 (4.16%) | sma20 148.88 sma50 140.12 sma200 168.50 | range 114.50-250.25 | -35.1% off high | $4,288M/d
- ADBE 257.26 | ATR14 10.40 (4.04%) | sma20 273.33 sma50 249.94 sma200 267.60 | -29.1% off high
- LEN 80.37 | ATR14 2.35 (2.92%) | sma20 85.58 sma50 85.45 sma200 98.18 | range 79.83-133.76 | **+0.68% off its 200-day LOW**
- FDX 314.13 | ATR14 8.00 (2.55%) | sma20 327.92 sma50 319.35 sma200 288.46
- LLY 1123.91 | ATR14 34.49 (3.07%) | sma20 1197.19 sma50 1189.82 sma200 1063.80 | 30d high 1292.65
- UNH 400.84 | ATR14 8.20 | sma20 396.52 sma50 411.20 sma200 351.93
- KR 57.20 | ATR14 1.38 | sma20 57.39 sma50 57.69 sma200 64.00
- CHWY 23.27 | ATR14 0.98 (4.23%) | sma20 23.38 sma50 22.34

## [06:07 ET] EARNINGS CALENDAR (finnhub, fetched) — next 8 sessions
- 2026-09-09 (today): KR, CHWY bmo, CNM bmo, ASO bmo, SIG bmo, AEO amc, COO amc, RH, KFY bmo, AVAV amc
- 2026-09-10 amc: **ORCL** (EPS est 1.7766, rev est $19.53B), **ADBE** (EPS est 6.1999, rev est $6.82B), CPRT amc
- 2026-09-14: CBRL bmo, PLAY amc
- 2026-09-15: GIS
- 2026-09-16: **FDX** (est 4.0486), **LEN amc** (est 1.3147)

## [06:11 ET] THEME — the Hormuz shock is the whole tape, and it has an LNG leg nobody is trading
- 2026 Strait of Hormuz crisis: a US-Iran MOU signed 2026-06-17 collapsed in July when Iran targeted commercial shipping; traffic has been severely disrupted for most of the past five months. — source: https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis
- Iranian missiles struck Ras Laffan on 18-19 March, damaging two LNG trains and a GTL facility — ~12.8 Mtpa, about **17% of Qatar's LNG export capacity**. ~20% of world seaborne LNG and ~25% of seaborne oil transited Hormuz pre-war. — source: https://www.csis.org/analysis/battle-hormuz-will-reshape-global-lng-market
- QatarEnergy force majeure cancellations to European and Asian buyers **extended into early November 2026** (reported 2026-08-31). — source: https://www.euronews.com/business/2026/08/31/qatarenergy-extends-lng-cancellations-into-november-as-hormuz-disruption-drags-on
- EIA: full-year US LNG export volumes near 17.0 Bcf/d; Golden Pass shipped first cargo in April, ninth operational US terminal. US is now the marginal global supplier. — source: https://www.eia.gov/outlooks/steo/
- Energy is uniformly extended EXCEPT Cheniere: VLO -0.37% off its 200d high, PSX -0.71%, OKE -2.34%, TRGP -4.43%, DINO -1.41%, XLE -1.14%, FRO -1.26%, DHT -1.56% — versus LNG at **-8.27%**. That is the entry.
- LNG relative strength (computed): +7.76% 1m / +16.66% 3m vs SPY -0.94% / +3.62%; vs XLE -4.88% 1m but +5.62% 3m. Sector leader that consolidated through the crude spike.
- LNG insiders (finnhub, 6mo): 0 open-market buys, 6 sells totalling $28.4M. Not supportive — carried into the counter-argument rather than ignored.
- CAPTURED: LNG buy 266-276.5, stop 252, target 310.
- DATA GAP: `market_data.py implied LNG` failed — yahoo-options 401 Unauthorized. No options-implied move available for any name this run.

## [06:12 ET] REJECTED — ORCL — earnings 2026-09-10 amc with options pricing an ~11% move; a directional swing into that is a coin flip, not an edge, and the target would sit inside one implied move. Analyst bullish share 79.6% and falling (-2.0pp). FY2026 FCF was -$23.7B with ~$40B more debt/equity planned in FY2027. Watchlist: react to the print, do not front-run it. — source: https://traderc.com/orcl-q1-fy2027-earnings-options/
## [06:12 ET] REJECTED — NVS — three trial setbacks in one week (rap-cel paused after three patient deaths, pelacarsen CV outcomes failure, del-desiran HARBOR Phase 3 miss on video hand opening time in ~150 DM1 patients). Worst day on record, -9.4%, now 137.70 vs 30d low 137.115. This is a pipeline-credibility de-rating, not one fixable problem, and the $12B Avidity deal is impaired. No knife-catching on day one. — source: https://www.statnews.com/2026/09/08/novartis-del-desiran-myotonic-dystrophy-harbor-trial-failure-neuromuscular/
## [06:12 ET] REJECTED — DYN read-across — del-desiran is an antibody-oligonucleotide conjugate against DMPK and Dyne's DYNE-101 is the same modality in the same disease, so the sympathy selling is a legitimate mechanism read-across, not a mispricing to fade.
## [06:13 ET] REJECTED — DAL/UAL/LUV/JETS short on jet fuel — the trade is already 14-22% done (DAL -14% in 30 sessions to 78.96, UAL 108.24 vs sma50 121.04, LUV 38.67 vs 30d low 37.58). Shorting after the move, on margin, with the fuel input at a geopolitical premium that can unwind on one headline, is the wrong side of the same coin flip.
## [06:13 ET] WATCHLIST — EQT 55.12 (below its 200d 56.13) and AR 39.08 are the laggard US gas producers levered to LNG feedgas demand; UNG 10.46 is -38.6% off its high but is a rolling futures ETF with contango decay. Cheaper optionality than LNG, weaker confirmation — not captured today.

## [06:14 ET] POSITION UPDATE — BCC — opened 2026-08-18 @76.50, last 76.86 (+0.5%)
- decision: CLOSE. Broke below the 20-day (80.54), 50-day (78.99) and 200-day (77.15) together; the housing chain is at lows (LEN 0.68% off its 200d low, analysts 12 sell/2 strong sell); $24.4M/day is thin.
- action: captured via add_candidate.py as a sell, zone 76.00-79.00.

## [06:14 ET] POSITION UPDATE — LULU — opened 2026-08-22 @115.00, last 103.19 (-10.3%)
- decision: CLOSE, at a better level than the 2026-09-08 call. LULU rose 2.56% on a day SPY fell 0.55%, so the 100.61 exit never filled and 102.50-108.00 is the improved zone.
- why: published 5x in ten days per prior_context — that is the anchoring signal, and the MA stack (20d 117.69 / 50d 118.11 / 200d 152.47) is unchanged.
- action: captured.

## [06:14 ET] POSITION UPDATE — NKE — opened 2026-08-17 @40.75, last 38.10 (-6.5%)
- decision: CLOSE, but staged into strength. NKE is 0.53% off its 200-day low (37.90); exiting at market is selling the low. Zone 38.60-40.10 at the 20-day (39.63); exit at market on a close under 37.90.
- why: no NKE entry anywhere in the fetched finnhub earnings calendar through 2026-09-21, so there is no dated event to hold for.
- action: captured.

## [06:15 ET] POSITION UPDATE — GLD — opened 2026-08-22 @398.00, last 399.72 (+0.4%) — HOLD, no change, not captured
- GLD closed 399.72, which is 0.8% above the 30-day low of 396.45. Selling here is selling into support, and the 2026-09-08 exit at 406.77 correctly did not fill.
- Gold is below its 20-day (409.75) and 200-day (415.58) and fell 1.73% alongside equities — a rates story with the 10Y at 4.78, not a risk-off story.
- Invalidation, stated so it is not re-litigated tomorrow: a daily close below 396.45 ends the position. Above that it is held. No recommendation emitted because nothing changed.

## [06:15 ET] POSITION UPDATE — CCJ — opened 2026-08-17 @94.00, last 101.97 (+8.5%) — HOLD, no change, not captured
- Power was among the leading sectors on 2026-09-08 and CCJ closed +1.22%. Thesis intact.
- But do NOT add here: the 200-day sits at 105.46, directly overhead as resistance, and the 135 target equals the 200-day range high of 135.24. Adding at 101.97 buys straight into the resistance.

## [06:15 ET] POSITION UPDATE — SPY short — opened 2026-08-31 @773.00, stop 783.50, target 750, last 765.96 (+0.9% in favour) — HOLD, stop unchanged, not captured
- Working. Target 750 sits below both the 50-day (757.60) and the 30-day low (759.48), so it is a real extension rather than a nearby level.
- Stop deliberately left at 783.50 (above the 200-day range high of 779.37). Walking it in would lift the printed reward-to-risk while making the trade strictly worse — the KRE mistake.

## [06:15 ET] POSITION UPDATE — TLT — BUY @82.60 and SELL @81.87 net flat, last 82.20 — no action, not captured
- TLT is 1.27% off its 200-day low (81.17) with the 10Y at 4.78 and rising and crude at 94.24 feeding headline inflation. Do not re-add the long. The netting from 2026-09-02 stands.

## [06:15 ET] POSITION UPDATE — SVRA — opened 2026-08-23 @5.35, stop 4.60, target 8.00, last 5.53 (+3.4%) — HOLD, not captured
- Closed +2.98%, back above its 20-day (5.47). Stop 4.60 is 3.6 ATR from entry (ATR14 0.209), which clears the swing floor comfortably. Nothing to change.

## [06:21 ET] REJECTED — the entire defense complex, and the evidence is why
- Every defense name is at or near multi-year lows in month five of a shooting war, which looked like a mispricing worth owning: LMT 536.15 (-22.5% off high), NOC 518.58 (-33.0%), HII 287.67 (-37.5%), LHX 255.74 (**0.96% off its 200-day low**), GD 356.58 at its 30-day low, RTX 198.81 at its 30-day low, ITA 223.53 at its 30-day low, AVAV 148.78 (-63.6% off high).
- It is not a mispricing, it is funding. "US defense stocks see no Iran war lift after early surge": without a finalized defense appropriations bill, framework agreements with the primes cannot be fully funded; the Pentagon cut the FY2026 F-35 request to 24 aircraft from a forecast 48; and long production cycles cap how fast output ramps even where money exists. — source: https://www.militarytimes.com/news/your-military/2026/04/02/us-defense-stocks-see-no-iran-war-lift-after-early-surge/
- The tell that settled it: **zero open-market insider purchases across all six primes** over six months (LHX 0 buys/1 sell, NOC 0/21, LMT 0/11, GD 0/19 with $84.2M sold, RTX 0/5, HII 0/3). Nobody who runs these businesses is buying the low. A war-replenishment thesis with no insider confirmation and a funding blocker is a hunch, and a hunch is a conviction 1, which does not publish.
- WATCHLIST TRIGGER, stated so it is not re-derived tomorrow: a signed FY2027 defense appropriations bill or a named munitions supplemental. Until then this stays off the page.
## [06:21 ET] REJECTED — AVAV — reports today 2026-09-09 after the close, ATR 5.0%, -63.6% off its high, with analyst fair value already cut from ~$370 to ~$308. A directional position taken hours before that print is a coin flip on guidance, not research.
## [06:21 ET] REJECTED — oil services (OIH 428.57, HAL 36.80, SLB 57.10, BKR 63.92, RIG 5.76, NOV 21.39) — a Hormuz supply-disruption premium is not a capex cycle. OPEC+ is still restoring 2.2 mb/d, so there is no signal to drill more; services lagging crude is rational, not a gap to close. Taking it would also have been a fourth position on the same driver.
## [06:21 ET] REJECTED — LNG shipping / FSRU small caps — checked EE 39.30 ($14.0M/day, sitting on a flat 20-day 38.39 and 50-day 38.38, no setup), GLNG 51.46, FLNG 30.98, and the tankers TNK 92.33 (-2.2% off high), INSW 103.81 (-2.7%), STNG 82.12 (-6.0%), DHT 20.82 (-1.6%), FRO 46.62 (-1.3%). The tankers are the right thesis at the wrong price — all within 6% of 200-day highs. NFE excluded outright at $0.2581, under the $1 universe floor.
## [06:21 ET] REJECTED — PFE 27.79 — fell 2.32% purely on Novartis read-across while sitting above its 50-day (26.05) and 200-day (26.18) and only 4.9% off its 200-day high. A 2.0 R:R needs a 30.00 target above the 200-day high of 29.21 on a 1.5-wide stop; that is a target reverse-engineered to clear the floor. The existing pending at 25.80 stands as the level.

## [06:22 ET] STALE PENDING ORDERS — levels the market has left behind
Not re-pitched as ideas; recorded so synthesis and the reader can see which unfilled levels are dead.
- `BTC` SELL @63,400 (2026-08-16) and `/MBTU6` SHORT @64,340 (2026-08-18): **withdraw both.** BTC is 78,986 (+0.31% 24h) — the levels are 19-20% away and unreachable. /MBTU6 is additionally a September 2026 contract now at or inside its final trading period, which universe.md forbids recommending without saying so. Crypto is flat and uninvolved in this regime (ETH 2,489.10 flat, SOL 103.76 +0.05%); no crypto or crypto-futures idea today.
- `LCII` BUY @94.00 (2026-08-18): **withdraw.** LCII closed 99.11, a new 30-day low, 200-day at 117.97, -37.9% off its high. It is the same RV/housing complex the BCC close is exiting; buying it would contradict that call.
- `CEG` BUY @272.00 (2026-08-21): stale, 9.0% below a 299.05 market. No new view — CEG sits just above its 200-day (296.16), which is the wrong side to chase. VST is the expression captured instead.
- `XLE` BUY @63.90 (2026-08-15): superseded by today's capture at 63.20 with a 60.70 stop.
- `DG` BUY @134.50 (2026-08-21): superseded — the level is now 5.2% ABOVE a 127.87 market and would buy strength instead of the pullback it was written for.
- `VST` BUY @128.00 (2026-08-24): superseded by today's 141-148 zone.
- Still live and left alone: `EEM` @65.60 (market 68.83, below the 66.95 twenty-day — a real pullback level); `DINO` @99.50 (market 108.31, near the 97.38 twenty-day); `PFE` @25.80 (market 27.79); `IYR` SELL_SHORT @103.60 (market 102.05, needs a 1.5% bounce — sensible with the 10Y at 4.78).
- `KXFEDDECISION-26SEP-H25` @32, `KXFEDDECISION-26OCT-H25` @28, `KXFEDDECISION-26SEP-H0` @47: **cannot be marked.** See the events data gap below.

## [06:22 ET] DATA QUALITY — what failed, and what it cost
1. **Event contracts are unusable this run.** `market_data.py events` returned zero rows for "CPI", "interest rate", "Federal Reserve", "FEDDECISION", "recession", "government shutdown" and "oil price", and for "Fed" returned three unrelated Kalshi multi-leg sports shard tickers with every price field null. No implied probability could be read for any macro market, so no event-contract candidate was captured and the three open KXFEDDECISION positions could not be marked. This is the single biggest gap today — the strategy explicitly wants this lane and an oil-driven inflation shock is exactly when a Fed-path contract would be worth pricing.
2. **Options-implied moves unavailable.** `market_data.py implied` returns HTTP 401 Unauthorized from yahoo-options for every symbol. Where an implied move appears in these notes (ORCL ~11%, ADBE ~8.07%) it is quoted from a named third-party preview and attributed, never computed here.
3. **Index quotes dead.** ^GSPC/^NDX/^DJI/^RUT all failed on all four sources. SPY/QQQ/IWM used as proxies; index levels quoted in the macro block come from a news source, not from a fetch.
4. **Short interest unavailable** — `market_data.py short` timed out against api.nasdaq.com. No days-to-cover read on any name, so no squeeze evidence anywhere today.
5. **Robinhood futures availability could not be verified** — the support URL in config/universe.md returns HTTP 404. Per the non-negotiable, an instrument that cannot be verified is not recommended, so **no futures candidate was captured today** even though the regime is a commodity shock and universe.md prefers futures. That is a real cost of the gap, not a stylistic choice.
6. **Prices are 2026-09-08 closes**, age ~842 minutes at fetch, market session `pre`. That is a closed market, not stale data. One source-vs-fetch conflict worth naming: a Yahoo article states DG "finished at USD 133.21, down 1.8 percent" on 2026-09-08, while the finnhub fetch gives DG 127.87 on 2026-09-08 with 133.21 as the prior close. The fetched data is used; the article appears to describe the 09-07 session.

## [06:22 ET] CORRELATION CHECK — stated because it is at the cap
Three of the five new ideas depend on the crude path: **XLE** directly, **LNG** through the Qatari supply loss that the same conflict caused, and **DG** through the gasoline pass-through to the low-income consumer. That is exactly the 3-idea limit in config/strategy.md and it should not be exceeded — a Hormuz de-escalation headline hurts all three at once, and DG is not the hedge it looks like, because a crude collapse removes its trade-down driver too. **ADBE** (software de-rating) and **VST** (contracted data-centre power) are the only two ideas today that do not move on an Iran headline.

## [06:22 ET] HORIZON SKEW — declared, not apologised for
Nothing intraday cleared the bar and nothing was manufactured to fill the lane: the two dated intraday-grade events in range are ORCL and ADBE tomorrow after the close, and both are priced for 8-11% moves, which is a coin flip rather than an edge. One long_term idea (ADBE), four swings, three of which are position closes. No crypto, no futures, no event contracts — for the reasons recorded above, each of which is a data gap or an unverifiable venue rather than a judgement that the lane was empty.

## [06:22 ET] RESEARCH COMPLETE
- candidates: 8 (5 new ideas: XLE, LNG, ADBE, VST, DG; 3 position closes: BCC, LULU, NKE)
- positions reviewed and held with no recommendation emitted, with reasons logged above: GLD, CCJ, SPY short, TLT, SVRA
- coverage gaps: event contracts (source returned nothing usable), futures (Robinhood availability page 404 — nothing recommended unverified), options-implied moves (401), short interest (timeout), index quotes (all four sources failed), and no dedicated small-cap screen was run — the small caps checked (EE, FLNG, NFE, LCII, SVRA) were reached through themes rather than through a liquidity screen
- sources that failed: finnhub index quotes (CFD subscription required), query1/query2.finance.yahoo.com (429 on history, 401 on options), stooq (404 on index symbols), alphavantage (no api key), api.nasdaq.com short interest (read timeout), kalshi via market_data.py events (zero or irrelevant rows on every macro query), robinhood.com futures support article (404)

## [06:23 ET] CORRECTION TO THE 06:22 DATA-QUALITY BLOCK — event contracts are NOT unavailable, market_data.py reads the wrong fields
Two separate defects, both diagnosed, neither fixed here (research phase does not change code; a fix needs a test in `tests/`):
1. **No server-side search.** `events()` calls `/trade-api/v2/markets?status=open&limit=min(limit*5,200)` and then filters the returned page client-side by substring. Kalshi has tens of thousands of open markets and the first 200 are overwhelmingly sports, so every macro query returned nothing — the three sports shard tickers matched on "fed" inside `S2026645EFED5416`. Passing `series_ticker=` returns the right markets immediately.
2. **Prices are read from legacy fields.** Kalshi now serves `yes_bid_dollars` / `yes_ask_dollars` / `last_price_dollars` as decimal strings; the integer-cent `yes_bid` / `yes_ask` / `last_price` / `volume` / `open_interest` keys that `events()` maps are all null. That is why every price field printed None even on the correct markets. `volume_fp` / `open_interest_fp` carry the sizes.
- Fetched directly this session as a workaround. Prices below are real, not estimated.

## [06:24 ET] EVENT MARKETS — the Fed is priced to HIKE, and this reframes the whole report
- **KXFEDDECISION-26SEP** (decision 2026-09-16): Hike 25bps **54 bid / 55 ask** (OI 4.04M) | Maintain **44 / 46** (OI 10.33M) | Cut 25bps 0 / 1 (OI 6.52M) | Cut >25bps 0 / 1 | Hike >25bps 1 / 2.
- **KXFEDDECISION-26OCT** (2026-10-28): Maintain **68 / 69** | Hike 25bps **27 / 28** (OI 35.1K) | Cut 25bps 3 / 4 | Cut >25bps 1 / 2.
- Corroboration from FRED, not just the contract: the 2-year at 4.37% sits **74bp above** effective fed funds of 3.63%. The bond market and the event market agree the next move is up.
- **KXCPI-26AUG** (released 2026-09-11 08:30 ET, liquid — OI 17K-37K): Above 0.2% 84/88, Above 0.3% **51/57**, Above 0.4% 11/13, Above 0.5% 0/10. So ~0.3% MoM is the consensus. **KXCPIYOY-26AUG Above 2.9% = 99 cents** — August YoY above 2.9% is effectively settled.
- **KXCPI-26SEP** (released 2026-10-14): Above 0.3% 47/95, Above 0.4% 31/71, Above 0.5% 15/73. **Not tradeable** — open interest is 500-1,900 and the spreads are 20-48 cents wide, so the ask is nothing like the last price. Recorded for information; no recommendation made into a book that thin.
- CAPTURED: KXFEDDECISION-26OCT-H25 YES at 28 (level unchanged from the 2026-09-02 publication), conviction 2, 1% lottery-ticket size.

## [06:24 ET] POSITION UPDATE — the three open event contracts can now be marked
- `KXFEDDECISION-26SEP-H25` YES @32 (published 2026-08-22) → market **54 bid / 55 ask**. Up 22 cents, +69%, the best call in the book. **But the 32 level is dead** — it cannot be bought at 32 any more, so as an unfilled order it is withdrawn on the same reasoning as the stale equity pendings. If it did fill, hold: the thesis is playing out and resolution is 2026-09-16.
- `KXFEDDECISION-26SEP-H0` YES @47 (published 2026-09-03) → market **44 bid / 46 ask**. Down ~3 cents and still buyable at 46. Note that this is the *opposite side* of the trade above — the book is long both the hike and the hold on the same meeting, which nets to a partial hedge rather than a view. Not re-pitched; flagged so synthesis does not read the pair as conviction.
- `KXFEDDECISION-26OCT-H25` YES @28 (published 2026-09-02) → market **27 bid / 28 ask**, unchanged. Re-affirmed and captured above with today's evidence.
- This removes gap (1) from the 06:22 data-quality block. Gaps 2-6 stand.

## [06:24 ET] REJECTED — a September FOMC event contract (either side) — the Sept 16 market is 54/44 with 14 million contracts of open interest across the two legs and one-cent spreads. Taking a side there needs FOMC minutes, a dot plot or speaker commentary, none of which were read this session. "Oil is up" is not an edge against a book that deep, and config/strategy.md rules out exactly this.
## [06:24 ET] REJECTED — September CPI ladder (KXCPI-26SEP) — the right thesis and the wrong book. The gasoline pass-through from a crude move that happened in September genuinely argues Above 0.4% is underpriced at a 35-cent last, but the ask is 71 and open interest is 1,515. Paying 71 for something worth maybe 45 is not the trade the thesis describes.

## [06:25 ET] RESEARCH COMPLETE — supersedes the 06:22 block
- candidates: 9 (6 new ideas: XLE, LNG, ADBE, VST, DG, KXFEDDECISION-26OCT-H25; 3 position closes: BCC, LULU, NKE)
- positions reviewed and held with no recommendation emitted, reasons logged above: GLD, CCJ, SPY short, TLT, SVRA, and the three KXFEDDECISION contracts now marked at 06:24
- horizon/class mix, declared not manufactured: 1 long_term, 7 swing, 1 event. No intraday (both dated events in range, ORCL and ADBE on 2026-09-10, are priced for 8-11% moves — a coin flip, not an edge). No futures: the Robinhood availability article is a 404 and universe.md forbids recommending an unverified venue. No crypto: BTC 78,986, ETH 2,489, SOL 103.76, all flat and uninvolved in this regime.
- correlation: three ideas (XLE, LNG, DG) sit on the crude path, which is the 3-idea cap in config/strategy.md and must not be exceeded. The Fed contract is inversely exposed to the same shock and is the only idea today that gains if the oil-driven inflation read hardens.
- coverage gaps that remain: options-implied moves (yahoo-options 401), short interest (api.nasdaq.com timeout), index quotes (all four sources failed, ETF proxies used), Robinhood futures availability (404), and no dedicated small-cap liquidity screen was run — small caps were reached through themes (EE, FLNG, LCII, NFE, SVRA) rather than screened for.
- sources that failed: finnhub index quotes (CFD subscription), query1/query2.finance.yahoo.com (429 history / 401 options), stooq (404 on index symbols), alphavantage (no api key), api.nasdaq.com short interest (read timeout), robinhood.com futures support article (404). `market_data.py events` did not fail — it returned wrong results for the two reasons diagnosed at 06:23, and was worked around.
