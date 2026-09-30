# Research log — 2026-09-30

## [06:03 ET] MACRO — rates, policy, regime
- US 10Y 5.24% (2026-09-28), prev 5.17% — **long end pushing to new highs** — source: https://fred.stlouisfed.org/series/DGS10
- US 2Y 4.92% (2026-09-28), prev 4.81% — source: https://fred.stlouisfed.org/series/DGS2
- Fed funds effective 3.88% (2026-09-28), unchanged — source: https://fred.stlouisfed.org/series/DFF
- 10y-2y spread +0.37 (2026-09-29) from +0.32 — **bear steepener**: long end rising faster than short. Fed at 3.88 vs 10y at 5.24 = 136bp of term premium/inflation concern above policy rate.
- Unemployment 4.1% (Aug 2026), unchanged — source: https://fred.stlouisfed.org/series/UNRATE
- CPI index 334.131 (Aug 2026) vs 332.813 prior month = +0.40% m/m, an annualized ~4.9% — hot — source: https://fred.stlouisfed.org/series/CPIAUCSL
- TLT (20y+ Treasury ETF) 78.23 as of 2026-09-29 20:00 UTC (prior close), -0.50% — source: market_data.py macro
- REGIME READ: sticky/re-accelerating inflation + rising long-end yields + a Fed already easing (3.88 funds vs 4.92 2y implies the market prices *hikes* or no cuts). This is a long-duration-hostile, real-asset-friendly regime. It explains the open book's pain in long-duration equity (LULU, NKE, LCII) and the TLT short working.

## [06:03 ET] DATA QUALITY — Yahoo Finance rate-limited (HTTP 429)
- ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES=F, NQ=F, DX-Y.NYB, ^TNX, GC=F, CL=F all failed: finnhub says "Market data subscription required for CFD indices", yahoo 429, stooq 404, no alphavantage key.
- Index levels, VIX and futures prices are UNAVAILABLE this run. Do not state them.
- Individual equity quotes via finnhub may still work — testing.

## [06:07 ET] CALENDAR — dated catalysts inside 10 sessions (fetched, finnhub earnings calendar)
Source: https://finnhub.io/api/v1/calendar/earnings (via scripts/market_data.py earnings --days 14)
- **2026-09-30 amc — MU (Micron)** — EPS est 32.32, rev est $52.24B. TONIGHT. MU is in the pending book (BUY @960, never filled; last 1065.08).
- **2026-09-30 bmo — JBL (Jabil)** EPS est 4.10, rev est $9.79B; FDS 4.38; CALM -0.72
- **2026-10-01 amc — NKE (Nike)** — EPS est 0.4444, rev est $11.45B. **NKE is an OPEN LOSING POSITION (BUY 40.75, last 35.84, -12.0%) with an unfilled exit.** Earnings in ~36h.
- **2026-10-01 bmo — ACN (Accenture)** EPS est 3.21, rev est $18.21B — AI-services bellwether; AYI 5.72
- 2026-10-05 bmo — MKC (McCormick) 0.76
- **2026-10-06 amc — STZ (Constellation Brands)** 3.61; bmo LW (Lamb Weston) 0.61, RPM 1.97, APOG 0.64
- 2026-10-07 — LEVI 0.37, TLRY -0.19, **APLD (Applied Digital) -0.31, rev est $137.6M** (AI datacenter)
- **2026-10-08 bmo — PEP (PepsiCo)** 2.32, rev est $25.25B; HELE 0.52
- **2026-10-09 — BLK 14.42, DAL (Delta) bmo 2.05**
- 2026-10-13/14 — bank kickoff: C, ABT, AZZ (13th); BAC, MS, STT, FAST (14th)
- NOTE: 2026-09-30 is US federal fiscal year end — Oct 1 shutdown risk is a live macro item; checking news.

## [06:12 ET] MACRO — shutdown risk is OFF the table (a real finding, not a non-event)
- Continuing resolution signed into law 2026-09-02, funding existing levels to **Dec 11 2026**. Senate 90-6 (Aug 8), House 370-48 (Sep 1).
- So today (fiscal year end) carries NO Oct 1 shutdown risk. The next cliff is 2026-12-11, outside every swing horizon here.
- sources: https://en.wikipedia.org/wiki/2026_United_States_federal_government_shutdowns , https://breakingdefense.com/2026/09/house-passes-funding-stopgap-averting-government-shutdown-in-october/ , https://www.nbcnews.com/politics/congress/senate-leaders-reach-deal-avert-shutdown-2026-elections-rcna590564

## [06:12 ET] LEVELS — fetched price history (nasdaq via market_data.py history --days 120)
All prices are 2026-09-29 closes (prior session; market is pre-open at 06:12 ET, so a close is the freshest honest equity price).

- **MU** 1065.08 | ATR14 43.71 (4.10%) | SMA20 1005.52 | SMA50 949.71 | 6m range 398.44-1255.00, -15.1% off high | $26.6B avg daily dollar volume
  - Path: 924.03 (9/14) -> 1108.72 high (9/25) -> 1053.98 (9/28) -> 1065.08 (9/29). Up 167% off the 6m low.
- **NKE** 35.84 | ATR14 0.9045 (2.52%) | SMA20 36.78 | SMA50 39.38 | 6m range 35.2159-47.645, **-24.8% off high and only +1.77% off the 6m LOW** | $1.12B avg dollar volume
  - Below both SMA20 and SMA50. Made the 6m low 35.2159 on 9/25. Closed 35.84 on 9/29 after failing at 36.43.
- **ACN** 177.12 | ATR14 6.98 (3.94%) | SMA20 184.02 | **SMA50 176.60** | 6m range 118.15-199.65, -11.3% off high | $887M avg dollar volume
  - Path: 195.00 (9/14) -> slid 8 sessions -> 172.11 intraday low (9/29) -> closed 177.12 near the session high 177.77. A reversal bar off SMA50 the day before the print.

## [06:06 ET] CLOCK CORRECTION
Real wall clock is behind my estimated stamps above: `date` reads 06:06 ET here. The 06:03/06:07/06:12 stamps above are estimates written ahead of the true time; the findings under them are all from fetches made between 06:01 and 06:06 ET. Timestamps from here are read from `date`.

## [06:06 ET] TAPE — prior-session closes (2026-09-29 20:00 UTC, finnhub)
SPY 764.20 -0.18% | QQQ 737.93 +0.19% | IWM 279.01 -0.36% | TLT 78.23 -0.50%
XLE 61.54 -0.90% | GDX 89.07 +1.34% | GLD 382.89 +1.32% | XLU 39.71 +1.17% | IYR 96.12 -0.04%
KRE 69.83 (10th straight lower close) | XLF 54.01 at its 20d low 53.72 | OXY 54.94 -2.07% | DINO 105.59 -0.57%
- **The rotation is the finding.** Long yields are making highs, and the things that "should" work on a steepener are the weakest on the board: KRE has closed lower ten sessions running (72.74 -> 69.83, -10.9% off its high, sitting on its 20d low), XLF is at its 20d low. Gold, miners and *utilities* are the bid. Rising long rates plus falling banks plus bid gold is a credit/inflation-risk tape, not a growth-reflation one. **Do not express the steepener as long banks — the tape is refusing it.**
- XLU +1.17% is against the open XLU SELL_SHORT (entry 39.60, last 39.71, now ~0.3% underwater). Utilities bid while the 10y rises 7bp is a defensive bid overriding the duration math.

## [06:06 ET] DATA QUALITY — options-implied moves unavailable this run
- `market_data.py implied` fails: `yahoo-options 401 Unauthorized` on https://query1.finance.yahoo.com/v7/finance/options/. Tested on DAL.
- So no idea today can cite what the straddle prices. Noted rather than guessed.

## [06:06 ET] LEVELS — more fetched history (nasdaq)
- **KRE** 69.83 | ATR 1.260 (1.80%) | SMA20 72.76 | SMA50 74.67 | -10.9% off high | 20d 69.45-75.50 | $958M
- **XLF** 54.01 | ATR 0.742 (1.37%) | SMA20 56.22 | SMA50 56.96 | -7.8% off high | 20d 53.72-58.60 | $1,800M
- **PEP** 128.69 | ATR 2.185 (1.70%) | SMA20 134.03 | SMA50 137.53 | **-19.6% off high (high 160.03)** | 20d 126.42-141.71 | $1,077M
- **DAL** 84.87 | ATR 2.467 (2.91%) | SMA20 80.48 | SMA50 84.05 | -11.3% off high (high 95.68) | 20d 75.99-85.47 | $548M

## [06:06 ET] REJECTED — DAL — best relative strength on the board, and it still fails the R:R floor
- The bull case is real: 1m +5.99% vs SPY -0.67% and XLI -4.52% (rel. strength +6.66% 1m, +13.39% 6m vs XLI); above SMA20 80.48 and SMA50 84.05; earnings 2026-10-09 bmo, EPS est 2.05 on rev est $17.77B; falling energy complex is a jet-fuel tailwind.
- It fails anyway, and the arithmetic is the point. ATR is 2.467 so a swing stop must clear 4.93. From 84.87 the widest honest stop is 79.60 (below the 9/17-9/18 closes 79.43/79.62 and SMA20), risk 5.27 = 2.14 ATR. 2.0 R:R then demands a target of 95.41 — **above nothing less than the 6-month high of 95.68.** Pulling the entry back to 82.60 makes it worse: an honest stop under the 20d low is 75.80 and 2.0 R:R needs 96.20.
- DAL has 12.7% of room to its 6m high against a 2.9% ATR. There is no version of this that clears 2.0 without either a sub-2-ATR stop or a target I cannot defend above the 6m high. **The idea failed the floor; it is not a target-setting problem.** Watchlist only, on a break and hold above 95.68.
- Insiders: 0 open-market buys, 14 sales worth $44.3M over 6 months — weak evidence either way, but no confirmation.
- sources: https://finnhub.io/api/v1/calendar/earnings , https://api.nasdaq.com/api/quote/DAL/historical

## [06:06 ET] REJECTED — ACN — de-rated into a print, but the confirmations are all pointing down
- 177.12, sitting on SMA50 176.60, closed near the session high after an intraday 172.11 low — a reversal bar the day before Q4 earnings (2026-10-01 bmo, EPS est 3.21, rev est $18.21B).
- Against it: **zero open-market insider buys, 10 sales worth $2.59M**; analyst bullish share 59.4% and **falling 10.3pp** (strong_buy+buy went 8+15 in June to 6+13 now, holds 10 -> 13). A de-rating with no insider buying and analysts leaving is the "cheap because it is broken" case, not the "cheap and fixable" case this report is supposed to hunt.
- No position ahead of a binary print on that evidence set.
- sources: https://finnhub.io/api/v1/stock/insider-transactions?symbol=ACN , https://finnhub.io/api/v1/stock/recommendation?symbol=ACN

## [06:09 ET] MACRO — THE FINDING OF THE DAY: this is a HIKING cycle, not a pause
- **The FOMC raised the target range 25bp on 2026-09-16, vote 12-0**, with the statement saying inflation "remained elevated" and the increase would support a timelier return to 2%. Current range **3.75-4.00%** (effective DFF 3.88% matches).
- **The Fed is projecting 4.1% by year end** — i.e. one more 25bp hike across the two remaining meetings.
- **Next FOMC: 2026-10-27/28, decision Wednesday 2026-10-28 14:00 ET.** Market-implied odds of a 25bp hike at that meeting: 68-69% (Kalshi / centralbank.watch), 76.9% (CME FedWatch).
- **2026-09-29 session: the 30-year yield reached above 5.6%, a level not seen since June 2002.** The 10-year topped 5.29% intraday (FRED close 5.24% on 9/28). Indices closed: Dow 51,349.92 -131.59 (-0.26%), S&P 500 7,670.84 (-0.16%), Nasdaq Composite 26,797.54 (-0.09%).
- Cause named in the reporting: persistent inflation raising the odds of *further* hikes. Banks slid — JPM, MS, BAC all lower, XLF lower.
- sources: https://fedratecalc.com/fomc-meeting-schedule/ , https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm , https://centralbank.watch/federal-reserve/ , https://rateprobability.com/fed , https://finance.yahoo.com/markets/stocks/articles/stock-market-news-sep-29-083000758.html , https://www.cnbc.com/2026/09/29/stock-market-today-live-updates.html
- **What this reframes.** Every long-duration thesis in the open book is fighting a 5.6% 30-year. It also explains the two things that looked contradictory at 06:06: gold bid *into* rising nominal yields is an inflation/debasement bid, not a duration bid; and banks falling into a steepener is credit fear beating the NIM arithmetic.
- **The clean, under-covered expression of a hiking Fed is not banks — it is float.** A life insurer reinvests a bond portfolio at 5.6% instead of 4%, with no credit book to mark. Screening life/annuity names next.

## [06:12 ET] CAPTURED — MU — buy the reaction, not the print
- Fetched surprise record: beat 4/4 by +17.33%, +27.28%, +17.39%, +2.85%. Analyst bullish share **91.4%** (18 SB / 35 B / 4 H / 1 S), -1.3pp.
- Company's own FQ4 guide: revenue $50B +/-$1B, adj EPS $31 +/-$1, gross margin ~86%. Street ~$50.8B / ~$31.5; finnhub calendar carries $52.24B / $32.32. ~$124 of annualised EPS on a 1065 tape = **8.6x**.
- The piece that decides it: "HBM is sold out for the year under fixed-price contracts, which supports revenue visibility but **caps upside surprise**." So the beat is close to assured and worth little; the FQ1-27 guide and the HBM/DRAM capacity split are the trade.
- Captured with `wait: true` — entry zone 1000-1045 only if the post-print session *closes* in it. Stop 920 = 2.29 ATR. Target 1230 (~10x forward), t2 1255 (6m high). R:R 2.10 vs a 32.3% break-even; claimed 45%.
- sources: https://news.alphastreet.com/micron-technology-mu-q4-2026-preview-eps-est-31-56-reports-september-30/ , https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/09/micron-a-look-at-memory-ahead-of-q4-earning , https://finnhub.io/api/v1/stock/recommendation?symbol=MU

## [06:12 ET] REJECTED (as a theme) — long financials on the steepener, including the insurer version
- The float thesis is sound on paper: a life insurer reinvests at a 5.6% long bond with no credit book. The tape refuses it across the whole complex. Every one of these closed 2026-09-29 below its SMA20, and five of seven below SMA50:
  MET 95.20 (SMA20 96.81 / SMA50 96.36) | PRU 115.06 (118.61 / 120.42) | EQH 52.19 (52.81 / 51.05) | CRBG 33.77 (34.24 / 33.21) | LNC 40.92 (42.77 / 43.42), -14.2% off high | AFL 113.66 (115.64 / 119.53), -12.7% off high | CB 332.08 (338.34 / 344.07)
- Together with KRE's ten consecutive lower closes and XLF at its 20d low, **there is no long expression of a hiking Fed inside financials that the tape is confirming today.** Not one of them is a buy here and I am not going to construct one. Revisit if a name reclaims its SMA50.
- source: https://api.nasdaq.com/api/quote/<SYM>/historical

## [06:12 ET] DATA QUALITY — short interest unavailable
- `market_data.py short` timed out on all four attempts (MU, PEP, NKE, KRE): `ReadTimeout api.nasdaq.com read timeout=20`. No short-interest or days-to-cover figure can be cited today.

## [06:12 ET] CRYPTO — fetched (coingecko)
- BTC 83,698 (-0.68% 24h), vol $27.9B, mkt cap $1.68T | ETH 2,689.34 (-1.08%) | SOL 119.25 (-0.57%)
- Context worth noting: the open book carries a BTC SELL @63,400 and a /MBTU6 SHORT @64,340, both published mid-August and both ~24% below the market. Those levels are stale, not close.

## [06:15 ET] REJECTED — PEP — the cheapest-looking idea on the board and it fails on its own arithmetic
- Setup looked ideal: -19.6% off the 160.03 high, a 1.70% ATR, Q3 earnings dated 2026-10-08 bmo (est 2.32 on $25.25B), Elliott Investment Management holding a **$4B stake** with a signed agreement — 20% of US SKUs eliminated, three Frito-Lay plants closed, a North America supply-chain review, and a commitment to **at least 100bp of margin expansion over three years**. 2026 guide: net revenue +4-6%, core EPS +5-7%.
- Valuation I can defend: fetched quarterly actuals 2.29 + 2.26 + 1.61 + 2.20 = **8.36 TTM EPS**, so 128.69 is 15.4x trailing and ~14.6x on a +5-7% forward. Re-rating to 17x on ~8.8 forward = **$149.60**.
- Bear case: the dividend is $1.4225/quarter = $5.69 annual, a 4.42% yield, on a **105% payout of earnings and 111% of free cash flow last year**. If that is cut the yield buyer leaves and 14x on flat 8.36 = **$112**.
- From a 127.00 accumulation entry that is 22.60 of reward against 15.00 of downside = **1.51, against a 2.5 long-term floor. It fails, and not narrowly.** The only entry that clears 2.5 is ~120, below the 6-month low, which is a level not a plan.
- Three independent confirmations all point the other way anyway: relative strength **-8.11% vs XLP over 1 month and -38.86% over 6 months** (PEP -17.94% while XLP is -0.04%); **zero open-market insider buys** in six months against one sale; analyst holds drifting 15 -> 17 with strong buys 3 -> 2.
- A 4.4% yield on a 105% payout is not a valuation floor, it is the thing at risk. Not a buy at any conviction today.
- sources: https://www.nasdaq.com/articles/pepsico-strikes-deal-elliott-unveils-2026-cost-cuts-and-plant-closures , https://finnhub.io/api/v1/stock/recommendation?symbol=PEP , https://finnhub.io/api/v1/stock/insider-transactions?symbol=PEP , https://api.nasdaq.com/api/quote/PEP/historical

## [06:15 ET] CORRECTION to the 06:06 tape read — one green day is not a trend, and I nearly traded off two
Pulling full history on the names that were up 2026-09-29 shows every one of them is a bounce inside a downtrend, not strength:
- **Gold is not making highs, it is correcting.** GLD 382.89 is **-14.7% off its 448.70 high**, below SMA20 396.51 and SMA50 395.93, and it printed a 20-day low at 376.88 on 9/28 before Tuesday's +1.32%. GDX 89.07 is -15.7% off high, below SMA20 95.23 *and* SMA50 90.71, 20d low 87.36 on 9/28.
- **The AI-power complex is broken, not bid.** VST 140.83 (-17.8% off high, below SMA20 142.73 and SMA50 144.91); CEG 264.58 (-19.5%, below 272.94 / 272.32); **NRG 97.17 (-44.6% off a 175.51 high**, below SMA20 107.12 and SMA50 116.75, sitting on its 20d low 96.73); SMR 7.76 (-45.7%); OKLO 37.11 (-54.5%); URA -32.1% off high and -7.55% below SMA50. Only TLN 314.84 is above its SMA20 (302.38).
- So the 06:06 line "gold, miners and utilities are the bid" was read off single sessions and is **wrong**. Retracted.

## [06:15 ET] MACRO — the real structure: an exceptionally narrow market breaking under a 5.6% long bond
Fetched vs-SMA and drawdown across the board (2026-09-29 closes):
| | vs SMA20 | vs SMA50 | off 6m high |
| --- | --- | --- | --- |
| SMH | +5.79% | +6.90% | -9.7% |
| XLK | +2.77% | +5.01% | -2.1% |
| QQQ | +2.07% | +3.31% | -1.4% |
| XLV | +0.88% | +1.54% | -3.3% |
| SPY | -0.11% | +0.23% | **-1.9%** |
| XLC | -0.95% | +0.11% | -6.7% |
| XLI | -1.04% | -4.73% | -10.1% |
| XLP | -1.79% | -3.24% | -7.8% |
| **ITB** | -1.69% | **-6.47%** | **-16.9%** |
| XLY | -2.66% | -4.74% | -10.7% |
| **IWM** | -2.81% | **-4.92%** | **-8.6%** |
| XLB | -3.34% | -4.95% | -9.4% |
| **XLRE** | -3.53% | **-6.41%** | -11.0% |
| URA | -7.23% | -7.55% | -32.1% |
- **SPY is 1.9% off its high while IWM is 8.6% off, ITB 16.9% off, XLRE 11.0% off and XLY 10.7% off.** Semis and large-cap tech are the only things above their 50-day and they are carrying the index on their own.
- This is exactly what a Fed hiking into 4.9% annualised CPI with a 5.6% thirty-year does: it kills anything financed, cyclical or rate-sensitive and leaves the cash-generative AI complex standing.
- **The two tradeable sides of the day are therefore: long what is leading (semis), and short what the long bond is killing (housing, REITs, small caps).** Not long financials, not long gold, not long power.
- source: https://api.nasdaq.com/api/quote/<SYM>/historical via scripts/market_data.py history

## [06:20 ET] CAPTURED — ITB sell_short 89.80 / stop 93.60 / target 81.50 (R:R 2.18, 1.86 ATR, conv 4)
- 30y Treasury above 5.60% on 9/29, highest since June 2002. **30y fixed mortgage only 7.03% as of 2026-09-24** (Freddie Mac PMMS, from 6.95%) — the consumer quote is lagging the bond, not leading it.
- **NAHB builder confidence 32 in September, the lowest reading of 2026**, -3 pts m/m. 66% of builders using sales incentives (+3pp m/m); 73% report higher material costs, some +15%.
- August new home sales +6.4% to 684k SAAR is the counter — answered: still below last year's pace, and the units were bought with incentives into rising costs.
- Fetched rel. strength vs SPY: -7.66pp (1m), -17.74pp (3m), -20.58pp (6m); XHB -7.29%/-16.09% confirms the group.
- sources: https://www.freddiemac.com/pmms , https://www.homes.com/news/builder-sentiment-sinks-to-2026-low-as-mortgage-rates-climb/1282321706/ , https://eyeonhousing.org/2026/09/new-home-sales-rise-as-affordability-challenges-continue/

## [06:21 ET] CAPTURED — IYR sell_short 97.80 / stop 100.40 / target 90.50 (R:R 2.81, 2.11 ATR, conv 3) — AMENDMENT
- Amends the IYR short published 2026-09-02 at 103.60, a level now 7.8% above the market that was never going to fill. Eight consecutive lower closes 98.65 -> 96.12; the 97.22/97.77 shelf broke; entry is that broken shelf on a bounce.
- Fetched rel. strength vs SPY -6.40/-8.33/-17.63pp; XLRE within a tenth of a point on every window, so it is the asset class.
- **Concentration flagged in key_risk**: open TLT short + new ITB short + this = one long-rate view in three costumes. Size as one.

## [06:21 ET] POSITION UPDATE — NKE — CLOSE THE LONG BEFORE THE 2026-10-01 PRINT
- Open long from 2026-08-17 @ 40.75, last 35.84 = **-12.0%**.
- FQ1-27 earnings 2026-10-01 amc. Consensus $0.44 on $11.33B = **revenue -3% y/y**; consensus EPS cut 2.2% over both 30 and 90 days. Street is 14 hold / 8 buy / 6 sell; fetched bullish share 39.1%, **-9.8pp** over four months.
- **The options market prices an 8.3% move = 2.97 points. NKE's ATR14 is 0.9045, so that is 3.3 ATRs.** No stop clearing the 2.0 ATR floor survives the gap. Holding through the print is not a managed position.
- Price sits 1.8% above the six-month low of 35.2159, below SMA20 36.78 and SMA50 39.38, -24.8% off the 47.645 high. NKE is -42% YTD.
- Counter considered and rejected as stale: 4 distinct insiders bought 5 lots on the open market to April 2026 — Timothy Cook 25,000 sh @ 42.43, CEO Elliott Hill 2x23,660 sh @ 42.27/42.265 — $3.73M of buys vs $1.57M of sales. Six months old and 18% underwater. A reason to revisit after the print, not to hold through it.
- decision: **close at the open, do not replace with a short** (the same 8.3% gap runs both ways and a turnaround print reverses it).
- action: captured via add_candidate.py as NKE `sell`, entry 35.84 on_open, target null.
- sources: https://www.tipranks.com/news/nike-stock-nke-could-swing-8-3-on-q1-earnings-options-market-signals , https://news.alphastreet.com/nike-q1-2027-earnings-preview-october-1-street-expects-0-44-eps/amp/ , https://finnhub.io/api/v1/stock/recommendation?symbol=NKE

## [06:26 ET] EVENT MARKETS — the CLI returned nothing, so I queried Kalshi's API directly. The web's numbers were wrong.
`market_data.py events` returned count 0 for FOMC / CPI / inflation / rate hike / Federal Reserve / KXFEDDECISION, and one unrelated market for "Fed". **Data gap in the CLI path.** Went direct to https://api.elections.kalshi.com/trade-api/v2/markets.

**Live Kalshi FOMC decision prices, fetched this morning:**
| Meeting | Hike 25bp | Hold | Hike >25 | Cut 25 |
| --- | --- | --- | --- | --- |
| **2026-10-28** (`KXFEDDECISION-26OCT`) | bid 0.43 / ask 0.44, OI 838,552 | **0.55/0.56, OI 843,147** | 0.00/0.01 | 0.00/0.01 |
| **2026-12-09** (`KXFEDDECISION-26DEC`) | **0.73/0.74**, OI 94,928 | 0.21/0.22 | 0.02/0.03 | 0.01/0.02 |

- **My 06:09 note is wrong and is corrected here.** I had 68-77% for the October hike from a web search. The live market is **43%**, and prices the hold at 56%. The December hike is the one at 73%. This is precisely what "never state a price you did not fetch" is for — I would have published a number 30 points off.
- The split is well explained rather than mispriced: the Fed's own projection of 4.1% by year end implies exactly one more 25bp hike, and the 2026-10-28 decision falls days before the November midterms. The market is saying "one hike, in December". **No edge in the FOMC ladder — I am not going to manufacture one.**
- The pending `KXFEDDECISION-26OCT-H25` YES @28 from 2026-09-02 is now bid 0.43: it never filled at 28 and the market has moved to 43. Not an entry today.

## [06:30 ET] EVENT MARKETS — the September CPI ladder is where the disagreement actually is
Contract `KXCPIYOY-26SEP-T3.5`, fetched rules: *"If the Consumer Price Index increases by **more than 3.5%** in the twelve months ending September 2026 (as represented by the **one-decimal-place value** reported by the BLS), then the market resolves to Yes."* So YES needs a printed **3.6% or higher**. Quotes: yes 0.82/0.83, **no 0.17/0.18**, last 0.83, OI 39,106, total volume 60,846, 24h volume 1,035, closes 2026-10-14 12:29Z.

**The whole ladder, fetched, restated as P(printed YoY >= X):**
3.2% -> 98% | 3.3% -> 97% | 3.4% -> 95% | 3.5% -> 91% | **3.6% -> 82.5%** | 3.7% -> 43% | 3.8% -> 11.5% | 3.9% -> 3%

**The arithmetic that has to hold, from the BLS primary series (FRED CPIAUCNS):**
- Aug 2026 NSA index **334.980**; Sept 2025 NSA index **324.800**. Aug 2026 YoY = **+3.397%** (BLS printed 3.4%).
- Sept 2026 YoY = 334.980 x (1 + m/m) / 324.800 - 1. So:
  | Sept m/m NSA | YoY | prints |
  | --- | --- | --- |
  | +0.00% | 3.134% | 3.1 |
  | +0.20% | 3.341% | 3.3 |
  | +0.254% (= Sept 2025) | 3.397% | 3.4 |
  | +0.306% | 3.45% | 3.5 |
  | **+0.403%** | **3.55%** | **3.6 <- YES threshold** |
  | +0.50% | 3.65% | 3.7 |
- **So YES at 82-83c is a bet that September NSA m/m comes in at +0.403% or hotter.**

**September NSA m/m, every year 2014-2025, computed from the same series:**
+0.075, -0.156, +0.240, +0.529, +0.116, +0.078, +0.139, +0.272, +0.215, +0.249, +0.160, +0.254
mean **+0.181%**, median +0.188%, stdev 0.161, max +0.529 (2017, the Harvey/Irma gasoline spike), min -0.156.
**Exactly 1 of 12 Septembers cleared +0.403%. The market prices it at 82.5%.**

**And 2026's recent run rate is colder, not hotter.** Jun/Jul/Aug 2026 NSA m/m: -0.349, -0.010, +0.318, averaging **-0.014%**. The same months in 2025: +0.341, +0.151, +0.287, averaging +0.260%. **2026 is running 0.27pp per month below 2025.** Headline YoY has already fallen 4.249% (May) -> 3.531% (Jun) -> 3.365% (Jul) -> 3.397% (Aug).
- If Sept 2026 merely repeats Sept 2025's +0.254%, YoY is **3.397% and prints 3.4** — the NO side wins with room.
- At the twelve-year seasonal mean of +0.181%, YoY is 3.32% and prints **3.3**. The market assigns 5% to a print at or below 3.4.

**What would make the market right:** a September energy or shelter shock, or tariff pass-through landing in one month. The energy complex is going the other way — XLE -0.90% and -7.0% off its high, OXY -2.07% on 2026-09-29. I have found no such shock. That residual is what the 40% I am *not* claiming pays for.
- **Correction to my 06:03 note:** I wrote CPI was "+0.40% m/m, an annualized ~4.9% — hot". That single SA month is real, but the YoY is **3.4% and decelerating from 4.25% in May**, and annualising one month was the wrong frame to carry into the rest of the day.
- sources: https://api.elections.kalshi.com/trade-api/v2/markets/KXCPIYOY-26SEP-T3.5 , https://fred.stlouisfed.org/series/CPIAUCNS , https://www.bls.gov/cpi/

## [06:31 ET] CAPTURED — the rest of the book, and the rejections that came with it

### CAPTURED — TLT sell — POSITION UPDATE, extend the target, trail the stop
- Short from 2026-09-02 @ 81.87, last 78.23 = **+4.4%**, and the original 78.00 target is **0.3% away**. It is about to close on a thesis still strengthening.
- New target 74.50 (t2 71.50), stop 83.30 -> **81.20**, just above the SMA20 at 80.94. Time stop 2026-12-09 (the December FOMC).
- **Stated loudly in key_risk and repeated here: the 81.20 stop is 0.67 BELOW the 81.87 entry, so any reward-to-risk computed from those three numbers is arithmetically inflated and is not a new-entry ratio.** A fresh TLT short at 78.23 today has far worse economics. This is a trail on a winner, not an invitation to add.
- Driver: 30y above 5.60% (2002 highs), 10y 5.24% from 5.17%, 2y 4.92% from 4.81%, 10y-2y +0.37 from +0.32. Kalshi December hike 0.73/0.74.

### CAPTURED — BCC sell — POSITION UPDATE, close for exposure consistency
- Long from 2026-08-18 @ 76.50, last 75.97 = -0.7%. Essentially flat; the price is not the reason.
- **The reason is that this report is today short ITB on a rising-mortgage thesis, and Boise Cascade sells engineered wood into the houses ITB builds.** Long BCC and short ITB is an unintentional hedge, paid for twice.
- Noted honestly: BCC is the *least* broken thing closed today (-0.54% vs SMA20, -1.79% vs SMA200, -17.4% off high), so this exit may well look early.

### HOLD, no change, no candidate emitted — and why each
- **PFE** 28.72 (+4.1% on a 27.60 entry). The strongest position in the book: **-1.7% off its 12-month high**, above SMA20 (+2.18%), SMA50 (+5.84%) and SMA200 (+8.92%). It is the only remaining position with no stop, and that is **deliberate and correct** — it was opened as a long-term hold with a 42.00 valuation target, and `config/strategy.md` is explicit that a hard stop on a multi-year thesis usually just sells the bottom. Invalidation stays the thesis, not a price.
- **CCJ** 86.88 (-7.6%), **CEG** 264.58 (-2.7%), **GDX** 89.07 (-2.3%), **XLU** short 39.71 (+0.9% but ~0.3% underwater vs the 39.60 entry) — **all four carry working stops** (82.50 / 250.00 / 85.40 / 40.95), between 0.5% and 5.5% away. A position with a defined stop does not need a discretionary exit today; let the stop do its job. Do not add to any of them.
  - CCJ deserves a flag rather than an action: the complex is broken, with URA -35.7% off its high, -7.23% below SMA20 and -17.03% below SMA200, and CCJ itself -35.8% off high and -17.85% below SMA200. It is a hold-to-stop, not a hold-with-conviction.
  - **XLU: my 06:06 note said utilities were "bid" and questioned the short. That was wrong** — XLU is -16.9% off its high, -7.74% below SMA50 and -10.63% below SMA200, sitting 1.7% above its 12-month low of 39.03. The +1.17% session was a bounce in a downtrend. **The short is correct; hold it.**
- **DINO** 105.59 (-1.8%), **SNX** 258.19 (-0.7%), **EEM** 67.40 (+2.7%), **XLE** 61.54 (-3.7%) — all above their SMA200 (+50.4%, +20.7%, +7.3%, +9.3%) and none impaired. Hold.
- **SVRA** 5.08 (-5.0%), stop 4.60. Micro-cap lottery ticket behaving as one. Hold to the stop.
- **Energy concentration noted:** XLE + DINO + XLE-adjacent OXY (pending @54.00, market 54.94 and now within 1.7% of filling) is at the 3-idea correlation cap on the crude driver. No new energy today.

## [06:31 ET] REJECTED — SMH, MRK, GILD, CME/ICE/CBOE/NDAQ — and the rejection is one finding, not four
Everything above its 50-day fails the reward-to-risk floor for the same structural reason, and everything below it is broken. Worked, not asserted:
- **SMH** 606.90, ATR14 16.158. The 1.8 ATR ETF floor puts the widest honest stop at 577.81; using 571.00 (under the SMA20 at 573.69 and the 9/18 close of 573.00) is risk 35.90 = 2.22 ATR. A 2.0 ratio then needs 678.70 — **above the 6-month high of 671.83.** At 671.00 the ratio is 1.79. Fails.
- **MRK** 149.28, ATR 3.350. Stop 142.00 = 2.17 ATR; 2.0 needs 163.84 against a 12-month high of 156.92. Fails. (+22.17% vs SMA200, up 82% off an 82.01 low — the move has happened.)
- **GILD** 151.28, ATR 3.458. Stop 144.00 = 2.11 ATR; 2.0 needs 165.84 against a 12-month high of 157.29. Fails.
- **The exchanges were the best remaining idea in financials and the tape refuses them too.** A high-rate, high-volatility regime should pay CME and CBOE twice over — record rate-futures volume plus float income on margin deposits, with no credit book. All four are below their SMA20 and SMA50: CME 263.22 (-3.91%/-2.34%/-5.51%, **-20.0% off high**), ICE 152.19 (-2.73%/-1.64%/-1.92%), CBOE 261.75 (-5.93%/-9.13%/-8.71%, **-29.5% off high**), NDAQ 91.85 (-1.92%/-3.19%/+1.28%).
- **So: not one long in financials, exchanges, staples, power, gold, uranium, REITs, housing or small caps clears the bar today.** Semis and large-cap tech lead and have already run past where a 2:1 can be built honestly. That is the report, and padding it with a 1.8 would be exactly the reverse-engineering `config/strategy.md` forbids.

## [06:31 ET] REJECTED — IWM / /M2K short — right idea, wrong report to put it in
- The narrowness is the cleanest short on the board: IWM -2.81% vs SMA20, -4.92% vs SMA50, **-8.6% off high while SPY is -1.9% off its own**, and small caps carry the most floating-rate debt into a hiking Fed.
- Not captured, for one reason: it would be the **fourth** position on a single long-rate driver, behind the open TLT short, the new ITB short and the IYR amendment. `config/strategy.md` caps that at three. **Four ideas that are one bet is one bet with three extra commissions.** Logged so synthesis does not re-derive it.

## [06:31 ET] DATA QUALITY — crypto levels unavailable, so no crypto idea today
- Spot is fetched and fine (coingecko: BTC 83,698 -0.68%, ETH 2,689.34 -1.08%, SOL 119.25 -0.57%), but `market_data.py history BTC-USD` fails on every source — nasdaq returns no rows, yahoo 429.
- **Without OHLCV there is no ATR and no swing structure, so there is no honest stop.** Rather than guess levels on the largest-ATR asset class in the universe, no crypto idea is captured today. The 2.5 ATR crypto floor cannot be checked against a number I do not have.

## [06:34 ET] REJECTED — STZ, MKC, LW, LEVI, BLK, APLD — and the reason unifies the whole day
These were screened because they are the names with a dated catalyst inside ten sessions *and* enough drawdown for a 2:1 to be arithmetically reachable:
| | last | vs SMA20 | vs SMA50 | off 12m high | 12m low | earnings |
| --- | --- | --- | --- | --- | --- | --- |
| STZ | 112.77 | -7.00% | -11.96% | -33.1% | 111.54 (1.1% below) | 2026-10-06 amc |
| MKC | 48.40 | -3.90% | -7.05% | -33.2% | 44.82 | 2026-10-05 bmo |
| LW | 43.27 | -8.63% | -14.56% | -35.5% | 37.62 | 2026-10-06 bmo |
| LEVI | 19.75 | -1.73% | -10.03% | -23.1% | 17.72 | 2026-10-07 |
| BLK | 1067.94 | -1.09% | -3.67% | -12.5% | 917.39 | 2026-10-09 |
| APLD | 25.41 | -2.87% | -7.74% | -49.9% | 19.00 | 2026-10-07 |
**Every one is below both its 20- and 50-day, i.e. a falling knife into a binary print — the exact setup rejected for ACN at 06:06, and consistency requires rejecting it here too.**

The confirmations do not rescue them:
- **STZ**: 0 open-market insider buys against 2 sales worth $939k. And the detail that matters — **STZ has beaten consensus four quarters running, by +6.06%, +9.48% and +14.99%, with analyst bullish share at 62.1% and actually *rising* 1.4pp — and the stock is 1.1% above its 12-month low, 33.1% off its high.**
- **MKC**: 2 insider buys totalling $161k, both underwater (1,100 sh @ 50.21 in July, 2,000 sh @ 52.98 in April, stock 48.40) against a single $10.83M sale. Bullish share 50.0%, unchanged. Beats 3 of 4.

**That STZ line is the finding, and it explains the rejections of PEP, MKC, LW and KHC together.** When the risk-free 10-year is 5.24% and the 30-year is above 5.60%, a 20x consumer-staples multiple is a 5% earnings yield — a bond substitute paying *less* than the bond it substitutes for. So these names de-rate through the beats. Beating the number does not help when what is repricing is the discount rate, and buying the beat is buying the wrong variable. **No staple is a buy on an earnings catalyst in this regime**, which is also the honest retrospective case against the PEP work at 06:15.

## [06:34 ET] REJECTED — TLN — the same bounce-in-a-downtrend I caught myself buying at 06:06
- The one power name turning up: 314.84, above its SMA20 at 302.38, up from 292.30 over eight sessions, **+6.33% over 1 month against SPY -0.67% and XLU -7.07%** (+7.0pp vs SPY, +13.4pp vs XLU). Room is not the problem — a 2.0 ATR stop is 25.13 against a 449.84 high.
- It fails on everything except that one month. Relative strength is **-20.4pp over 3 months and -20.34pp over 6 months**. Analyst bullish share 87.0% but **falling 4.3pp** (strong buys 6 -> 4). **Beats 1 of the last 4.** Zero open-market insider buys against one $988k sale. No dated catalyst on the fetched calendar.
- One confirmation, in the most broken complex on the board (NRG -44.6% off high, OKLO -54.5%, SMR -45.7%, URA -32.1%). **This is the same mistake as reading one green session in gold and utilities as a bid — made 28 minutes later with a different ticker.** Rejected.

## [06:34 ET] CORRECTION — LULU captured at conviction 4, re-captured at 3
Its evidence list carries two distinct kinds (technical_level, positioning), and the conviction table scores two kinds as a **3**. Re-captured at 3; synthesis takes the last entry per symbol.

## [06:35 ET] RESEARCH COMPLETE
- **candidates: 10** (9 distinct symbols; LULU appears twice, the second entry correcting its conviction)
  - **New directional ideas (3):** ITB sell_short (conv 4, R:R 2.18), IYR sell_short (conv 3, R:R 2.81, amends the stale 103.60 level), KXCPIYOY-26SEP-T3.5 NO @18c (conv 4, the largest claimed edge of the day)
  - **New idea, entry deferred (1):** MU buy (conv 4, R:R 2.10, `wait: true` — no entry before tonight's print)
  - **Position management (6):** TLT extend target and trail stop; NKE, LULU, LCII, BCC close
- **The shape of the day, stated plainly because it is the finding and not a shortfall.** The market is exceptionally narrow: SPY is 1.9% off its high while IWM is 8.6% off, ITB 16.9%, XLRE 11.0%, XLY 10.7%. Only SMH, XLK, QQQ and XLV sit above their 50-day. I screened financials, insurers, exchanges, staples, power, nuclear, uranium, gold, miners, housing, REITs, airlines, healthcare, emerging markets and crypto, and **found no long that clears the reward-to-risk floor on an honest stop.** The leaders have run past where a 2:1 can be built (SMH 1.79, MRK and GILD both needing new 12-month highs, DAL needing one too); the laggards are broken and have no confirming evidence. So the report is short-biased, and it is short-biased because that is what the tape offered, not by design.
- **Correlation, named rather than buried:** TLT + ITB + IYR are one long-rate view in three instruments. Size them as a single position. IWM was rejected purely because it would have been the fourth.
- **coverage gaps:**
  - Index levels, VIX, ES/NQ futures, DXY, and spot gold and crude — all unavailable (finnhub requires a CFD subscription for indices, yahoo returned 429 across the board, stooq 404, no alphavantage key). No index or futures idea could be levelled today.
  - Options-implied moves — `implied` returns yahoo-options 401 Unauthorized. No idea today cites what the straddle prices except NKE, where the 8.3% figure came from a news source rather than the CLI.
  - Short interest and days to cover — `short` timed out on all four attempts (api.nasdaq.com, 20s read timeout).
  - Crypto OHLCV — `history BTC-USD` fails on every source, so no ATR and no honest stop. Spot is fine (coingecko). **No crypto idea captured, deliberately, rather than one with guessed levels.**
  - `market_data.py events` returned zero markets for every Fed and CPI query; I went direct to the Kalshi REST API. **Worth fixing — the event-contract lane is invisible through the CLI today, and it produced the best idea of the run.**
  - Not reached: small and micro caps beyond SVRA and APLD; futures entirely, for want of a fetchable contract price.
- **sources that failed:** query1/query2.finance.yahoo.com (429 on quotes and history, 401 on options), stooq.com (404 on index symbols), alphavantage (no API key), finnhub index quotes (subscription required), api.nasdaq.com short-interest endpoint (read timeout), `scripts/market_data.py events` (returns count 0 against Kalshi).
