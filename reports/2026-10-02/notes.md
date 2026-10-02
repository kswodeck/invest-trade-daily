# Research log — 2026-10-02

## [06:03 ET] MACRO — rates, policy, data gaps
- FRED (source: https://fred.stlouisfed.org/): US10Y **5.29%** (2026-09-30), US2Y **4.88%** (2026-09-30),
  effective fed funds **3.88%** (2026-09-30), 10y-2y curve **+0.46** (2026-10-01),
  unemployment **4.1%** (Aug 2026), CPI index 334.131 (Aug 2026).
- Read: a 5.29% 10y with funds at 3.88% is a **term-premium / long-end problem**, not a
  policy-tightening one. 2y at 4.88% well above funds is the market pricing the path *up*
  from here, i.e. cuts are off the table and hikes are partly priced. Bear-steepener regime.
- TLT proxy TLH/20y bond gauge: 77.71, -0.09% (prev close 2026-10-01 16:00 ET). Market session: pre-market.
- DATA GAP: Yahoo chart API returning **HTTP 429** for all index/VIX/futures/commodity quotes
  (^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES=F, NQ=F, DX-Y.NYB, ^TNX, GC=F, CL=F all failed);
  finnhub refuses indices without a CFD subscription; CoinGecko price call failed this pass.
  So: **no index level, no VIX, no spot gold/crude, no crypto price** from the macro call.
  Will retry per-symbol; anything still unavailable stays `null`.

## [06:06 ET] OPEN POSITION MARKS — all prices = 2026-10-01 close (prev session), pre-market now
| Sym | side | entry | last (10-01 close) | %vs entry | target | stop |
| XLE | buy | 63.90 | 62.70 (+1.95% on the day) | -1.9% | 70.50 | 60.80 |
| CCJ | buy | 94.00 | 85.69 (-1.13%) | -8.8% | 135.00 | 82.50 |
| NKE | buy | 40.75 | 35.15 (-0.71%) | -13.7% | 62.00 | none |
| BCC | buy | 76.50 | 74.70 (+0.74%) | -2.4% | 110.00 | none |
| LCII | buy | 94.00 | 82.11 (-1.86%) | -12.6% | 138.00 | none |
| PFE | buy | 27.60 | 28.12 (-1.40%) | +1.9% | 42.00 | none |
| EEM | buy | 65.60 | 66.81 (+0.03%) | +1.8% | 71.50 | 63.00 |
| DINO | buy | 107.50 | 112.70 (**+5.01%**) | +4.8% | 128.00 | 97.75 |
| LULU | buy | 115.00 | 95.86 (-0.34%) | -16.6% | 180.00 | none |
| SVRA | buy | 5.35 | 5.045 (-2.23%) | -5.7% | 8.00 | 4.60 |
| SNX | buy | 260.00 | 271.76 (**+5.80%**) | +4.5% | 296.47 | 242.50 |
| KHC | buy | 23.00 | 22.46 (-1.14%) | -2.3% | 32.00 | none |
| XLU | short | 39.60 | 39.68 (+0.61%) | -0.2% | 36.80 | 40.95 |
| GDX | buy | 91.20 | 86.74 (-1.21%) | -4.9% | 104.40 | 85.40 |
- source: finnhub via scripts/market_data.py quote, asof 2026-10-01T20:00Z
- Two movers to explain before deciding anything: **DINO +5.0%** and **SNX +5.8%**.
- XLU short is 1.27 away from its 40.95 stop and the 10y is at 5.29% — the macro is with it.

## [06:11 ET] MACRO — the two things that frame today
1. **Long end at a 24-year high.** 10y closed 5.248% on 2026-10-01 after spiking to ~5.34%
   intraday, a new multidecade high. S&P 500 closed 7,666 (+0.20%), Dow 50,927 (+0.04%),
   Nasdaq 26,871 (+0.04%), Russell 2000 2,806 (+0.35%) — equities clawed back as yields eased.
   Leaders: XLK, semis (SOX), IGV, XLI, XLE (+38% YTD). Laggards: **homebuilders, mortgage,
   banks (BAC/C/WFC/JPM), REITs (-9% since late August)**.
   source: https://investrade.com/market-review-october-01-2026/ ; https://www.fool.com/coverage/stock-market-today/2026/10/01/stock-market-midday-oct-1-stocks-edge-lower-as-treasury-yields-surge-to-24-year-high/
2. **Oil repriced hard.** WTI **$92.87 (+$2.45)**, Brent **$102.31 (+$4.28)** on 10-01.
   Gold $4,203.30 (+$15.60). Brent through $100 is the proximate cause of DINO +5.0% and XLE +1.95%.
   source: https://investrade.com/market-review-october-01-2026/
3. **DATED CATALYST TODAY: September Employment Situation, 2026-10-02 08:30 ET.**
   Consensus +84k payrolls, unemployment held at 4.1%.
   source: https://www.bls.gov/news.release/empsit.nr0.htm ; https://www.cnbc.com/2026/10/01/the-september-jobs-report-will-be-released-friday-heres-what-to-expect.html
- Regime read: **bear steepener + oil shock**. That combination is stagflationary at the margin,
  and it is why rate-sensitives (utilities, REITs, homebuilders, long bonds) are the short side
  and energy is the long side. Three existing positions already sit on exactly that axis
  (XLU short, XLE/DINO long, TLT short awaiting entry) — the correlation cap binds here.

## [06:12 ET] MACRO — why oil moved: this is a war premium, not a demand story
- Brent +4.4% to $102.31 on 2026-10-01 after the WSJ reported the US is sending a **third
  carrier strike group** to the Middle East (USS Theodore Roosevelt, arriving end of November),
  read as preparation to escalate against Iran. Strait of Hormuz transit risk is the live tail.
  source: https://www.cnbc.com/2026/10/01/oil-prices-today-wti-brent.html
- Context: oil already touched **$108** on 2026-09-10 on the Iran war and a diesel squeeze,
  so $102 is not the top of this range — it is mid-range in an active conflict.
  source: https://www.cnn.com/2026/09/10/investing/oil-iran-war-diesel
- Consequence for the book: long-energy and short-airline/short-rate-sensitive are **the same
  bet** on this driver. The correlation cap (max 3 per driver) is already close to binding
  with XLE, DINO, CCJ long and OXY awaiting. New energy ideas must earn their slot against
  those, not stack on top of them.

## [06:24 ET] CAPTURED — XLU sell_short (update to the 2026-09-24 position)
- hold, levels unchanged at entry 39.60 / target 36.80 / stop 40.95. R:R 2.07, stop 2.35 ATR.
- decision rationale: macro moved *for* the thesis (10y at a 24-year high) and the chart has
  not turned. Did NOT walk the stop in to improve the ratio — that is the KRE failure mode.

## [06:11 ET] TIMESTAMP CORRECTION
Earlier headings in this file were written from an estimate, not from `date`, and ran
~10-13 minutes fast. Real wall clock: research started **06:00:57 ET**, and the block above
this one was written at **06:10:50 ET**. Everything below is stamped from `date`. The
findings and prices are unaffected — only the heading times were wrong.

## [06:11 ET] DATA GAP — event contracts are unpriceable this run
- `market_data.py events` returns `count: 0` for CPI / oil / unemployment / recession / Hormuz,
  and junk (a college-football parlay) for "Fed".
- Queried Kalshi directly: `api.elections.kalshi.com/trade-api/v2/markets/KXFEDDECISION-26OCT-*`
  returns the markets as **active** but with `yes_bid`, `yes_ask`, `last_price`, `volume` and
  `open_interest` all **null** on the unauthenticated endpoint.
- Confirmed from that call: the **October FOMC decision closes 2026-10-28 17:59Z**, and the
  December one 2026-12-09. Those dates are fetched and usable.
- Consequence: **no event-contract candidate today.** An event contract whose thesis is a
  probability disagreement needs the market's implied probability, and I cannot fetch one.
  Writing an entry in cents I did not read would be the fabrication rule 2 forbids.
  The three Fed event contracts awaiting entry (26SEP-H25, 26OCT-H25, 26SEP-H0) also cannot be
  re-marked; 26SEP ones are past their event and should be expired by the tracker, not re-pitched.

## [06:11 ET] NEWS — NKE reported last night, and it breaks the open long's thesis
- Primary document read (8-K exhibit 99.1, filed 2026-10-01): Q1 FY27 revenue **$11.2B, -4%
  reported / -5% currency-neutral**; diluted EPS **$0.48**; gross margin **42.8%, +60bps**;
  inventory $7.8B, -3%; **Greater China -22% reported, -26% currency-neutral**.
  FY27 guidance: **revenue to decline high-single-digits**, adjusted diluted EPS **$1.15-$1.35**
  excluding ~$0.15 of Pace restructuring charges. Pace: ~$2.5B cumulative savings through FY31
  against ~$1.0B pre-tax charges plus $0.3B severance.
  source: https://www.sec.gov/Archives/edgar/data/0000320187/000032018726000184/q1fy27exhibit991er.htm
- Shares fell ~8% after hours. source: https://www.cnbc.com/2026/10/01/nike-nke-q1-2027-earnings.html
- Why this is decisive and not just a bad quarter: the open NKE long (entry 40.75, target 62)
  was a turnaround-inflection thesis. Management has now guided revenue **down** for the full
  year and said the China and Sportswear fixes take multiple seasons. At the FY27 guide midpoint
  of $1.25, a $62 target is ~50x forward earnings on shrinking revenue. That is not a de-rating
  to buy; it is the thesis being deferred past the horizon. **Close.**

## [06:11 ET] NEWS — ACN printed its best day on record, and that is the day's uncorrelated signal
- Accenture Q4 FY26, reported 2026-10-01: GAAP EPS **$3.29** (beat by $0.11), revenue **$18.7B,
  +6.3% y/y** (~$660M above consensus), Q4 new bookings **$22.2B**, **record $84.5B annual
  bookings**; FY27 guide **+3-6% revenue growth in local currency**, operating margin +10-30bps.
  Stock **+22%, its best single day on record**.
  source: https://finance.yahoo.com/markets/stocks/articles/accenture-q4-2026-earnings-beat-172435987.html
  source: https://finance.yahoo.com/markets/stocks/articles/acn-stock-jumps-accenture-posts-114431202.html
  source: https://www.sec.gov/Archives/edgar/data/0001467373/000146737326000037/q4fy26earnings8-kexhibit.htm
- **This is what moved SNX +5.8%** — IT distribution reads across from IT services demand, and
  SNX had no company news of its own. It also reframes yesterday's decision to close SNX.
- Crucially this driver is **neither oil nor the long end**, which is the whole reason it matters:
  the book is already at the correlation cap on both of those axes.

## [06:25 ET] THE DAY'S BEST FINDING — defense is priced for the peace deal the oil market just un-priced
- **Why defense de-rated:** a US-Iran **interim peace agreement** removed the geopolitical risk
  premium that had supported defense valuations, prompting rotation out of legacy primes.
  ITA -16.18% over 3m. HII fell from 460 to 274.33 (-40.4% off its 400-day high); GD -16.8% off
  its 120-day high at 332.72, below both SMA20 (348.69) and SMA50 (370.54).
  source: https://www.ad-hoc-news.de/boerse/news/vorboerse/huntington-ingalls-stock-at-usd-264-02-on-september-25-2026/70191378
- **Why that premise broke on 2026-10-01:** third US carrier strike group ordered to the region;
  Brent +4.4% to $102.31. **Oil repriced escalation; defense equities did not.** HII +2.72%,
  BA +3.35%, GD +0.27%, LMT -0.74%, NOC -0.31%, RTX -0.34% — the sector barely moved.
  source: https://www.cnbc.com/2026/10/01/oil-prices-today-wti-brent.html
- Primary document read (HII Q2 2026 8-K, 2026-07-30): revenue $3.4B +10.9%, diluted EPS $5.27
  vs $3.84 est (+37.2%), **backlog $57.3B**, Q2 FCF **-$150M**; FY26 shipbuilding revenue
  **raised to $10.2-10.4B from $9.7-9.9B**, margin low end lifted to **6.0-6.5%**, Mission Tech
  $3.0-3.2B at 8.4-8.6% EBITDA, FY26 FCF **$500-600M**. CEO targeting 15% throughput improvement.
  source: https://www.sec.gov/Archives/edgar/data/0001501585/000150158526000045/hii2026q2earningsrelease.htm
- Profile: market cap **$10.81B**, 39.4M shares, ADV $127.9M. FCF yield 4.6-5.6%; backlog 4.2x revenue.
- Analyst revisions **improving** (+5.9pp, 2/7/8/0 -> 3/7/7/0) — the only improving name screened today.
- **Honest strike against it:** HII lags SPY on 1m/3m/6m (-6.2/-5.9/-30.3). This is a counter-trend
  reversal, not leadership. It outperforms ITA on 1m/+1.54 and 3m/+10.29 — best house in a bad
  street. Sized 3%, not the 4-5% the conviction-5 evidence count would allow.
- **CAPTURED: HII buy** 275.50 / target 330.00 / stop 256.00. R:R 2.79, stop 2.78 ATR,
  win_prob 0.40 vs a 0.264 baseline.
- CAVEAT on the spread: `depth HII` read bid 270.00 / ask 308.57 = 13.3% at **05:53 ET pre-market**.
  That is an empty pre-market book, not the tradeable spread — HII turns over $128M a day.
  Re-check in session before letting a spread flag demote this.
- Why not GD or ITA instead: GD is the same driver and the cap allows only so many; ITA is ~20%
  Boeing and BA has already moved +3.35% on its own $20B F/A-XX award (2026-09-29), so the ETF
  is part-spent. HII is the undisplaced one with the raised guidance.

## [06:20 ET] LEVELS — the open book, triaged on fetched ATR and range position
source for all: scripts/market_data.py history <sym> --days 120 (nasdaq), end 2026-10-01

| Sym | last | ATR14 | SMA20 | SMA50 | 120d low | 120d high | off high | verdict |
| XLE  | 62.70 | 1.3062 | 63.56 | 62.05 | 52.62 | 66.17 | -5.2% | HOLD — structure still valid |
| DINO | 112.70 | 5.3411 | 108.79 | 98.88 | 55.45 | 118.39 | -4.8% | CLOSE into strength |
| SNX  | 271.76 | 13.2157 | 264.91 | 258.08 | 198.84 | 298.77 | -9.0% | CLOSE — catalyst spent |
| GDX  | 86.74 | 3.0643 | 94.34 | 91.18 | 69.74 | 105.67 | **-17.9%** | CLOSE — thesis broken on costs |
| BCC  | 74.70 | 2.1845 | 76.22 | 79.08 | 65.00 | 88.43 | -15.5% | CLOSE |
| LCII | 82.11 | 2.5828 | 89.24 | 98.49 | 81.665 | 138.15 | **-40.6%** | CLOSE — 0.54% off its low |
| LULU | 95.86 | 3.5028 | 100.65 | 112.26 | 95.35 | 170.20 | **-43.7%** | CLOSE — 0.53% off its low |

- **LCII and LULU are both sitting within 0.6% of their 120-day lows with no stop under them.**
  That is the single worst configuration in the book and it is the third day it has been true.
  Both close.
- **XLE is the one hold whose arithmetic actually works:** entry 63.90, stop 60.80 = 3.10 = 2.37 ATR
  (clears the 1.8 ETF floor), target 70.50 = 6.60 reward, **R:R 2.13**. And the thesis improved
  overnight: Brent through $100, XLE +38% YTD and named a sector leader on 2026-10-01.
- **DINO — why the gain gets taken rather than ridden.** Insider buying is real and I found it:
  **3 open-market buys, 2 distinct buyers, $2.42M**, including director Franklin Myers buying
  15,000 shares at 85.30 (2026-08-11) and 15,000 at 69.11 (2026-05-18). Market cap $20.04B.
  source: finnhub insider transactions via scripts/market_data.py insiders DINO
  But the arithmetic from the **filled entry of 107.50, which cannot be amended**, no longer
  closes: the 2.0 ATR stock floor needs the stop at or below 96.82, and at a stop of 96.50 the
  risk is 11.00, so clearing the 2.0 R:R floor needs a target of 129.50+ — above the 118.39
  two-year high, with no level or fetched valuation to defend it. Keeping the existing 97.75 stop
  instead gives R:R 2.10 but on a stop just **1.83 ATR** wide, which is the KRE failure exactly.
  Neither leg can be fixed without inventing a number, so the position is closed at +4.8% after a
  +5.0% war-premium day, 4.8% below its two-year high. A **fresh** DINO long on a pullback to the
  108.79 SMA20, with its own stop and its own R:R, is a legitimate separate trade -> watchlist.
- **SNX — the catalyst is behind it.** 10-Q for the period ending 2026-08-31 was filed 2026-10-01
  and the 8-K on 2026-09-30; fiscal Q3 actual EPS **5.68 vs 4.75 est, +19.6%**. So the +5.8% on
  10-01 is post-print drift plus the ACN read-across, not a pending event. There is now no dated
  catalyst until the December print. Against that: **zero insider open-market buys and 74 sales
  totalling $15.7M** in six months, and analyst bullish share flat at 82.4% (no revision signal).
  Structure also fails: from the filled 260.00 entry the 2.0 ATR floor needs the stop at or below
  233.57, which against the 296.47 target gives **R:R 1.30**. Close at +4.5%.
  source: https://www.sec.gov/Archives/edgar/data/1177394/000162828026064256/snx-20260831.htm
- **GDX — the divergence is the tell, and it is not in our favour.** Gold rose $15.60 to
  **$4,203.30** on 2026-10-01 and GDX fell **1.21%**, leaving it **17.9% below its 120-day high**
  with SMA20 (94.34) and SMA50 (91.18) both overhead. Miners failing to confirm a gold price at
  record levels points at the cost line, and the cost line is exactly what this morning's macro
  did: **diesel and energy are miners' largest consumable input and Brent just went through $100**.
  A levered-to-gold thesis does not survive its own input cost repricing. The 85.40 stop is 1.34
  away — 0.44 ATR from the last price — so this closes on the next ordinary down day anyway;
  closing deliberately is better than being stopped by accident.

## [06:26 ET] CALENDAR — dated catalysts inside the next 10 sessions (fetched, finnhub)
- 2026-10-02 **08:30 ET — September Employment Situation**, consensus +84k, unemployment 4.1%
- 2026-10-05 bmo MKC (0.7633)
- 2026-10-06 bmo LW (0.606), bmo RPM (1.966), **amc STZ (3.6021 on $2.568B)**
- 2026-10-07 **amc APLD (-0.3098 on $137.6M)**, amc LEVI (0.3649)
- 2026-10-08 **bmo PEP (2.319 on $25.23B)**, bmo HELE, KARO
- 2026-10-09 **bmo DAL (1.9868 on $17.78B)**
- 2026-10-13 C, DPZ, GS, JNJ, JPM, UNH, WFC — Q3 bank season opens
- 2026-10-14 BAC, BLK, FAST, MS, STT; 2026-10-15 AA amc, AAL, ALK; 2026-10-16 CFG, MTB, RF, TFC, TRV
- 2026-10-28 FOMC decision (from the Kalshi market close time, fetched)
- **CALENDAR GAP:** `earnings --days 40` returns only 2026-11-03 to 2026-11-11 while `--days 12`
  returns 2026-10-02 to 2026-10-16. Nothing I ran covers **2026-10-17 to 2026-11-02**, so I have
  no fetched earnings date for HII, GD, LMT, NOC, RTX, PFE, CCJ or KHC. The HII idea is therefore
  **not** keyed to its Q3 print — I have not verified when that is and have not claimed it.

## [06:26 ET] REJECTED — and the cap is the reason for the biggest one
- **REJECTED — DAL sell_short** — the best remaining setup on the board and killed by the
  correlation cap, not by the thesis. Earnings 2026-10-09 bmo confirmed (est 1.9868 on $17.78B),
  jet fuel is a distillate and the distillate crack is the blown-out part of this oil move, and
  the levels work: 84.13 last, ATR 2.4347, SMA50 84.04 right at the price, 120-day range
  65.76-95.68, so a short at ~84.50 with a 89.50 stop (2.05 ATR) and a 74.50 target is R:R 2.00.
  **But a short airline is a long-oil bet.** Counting the Iran-escalation driver honestly, the
  book already has three: XLE long (held today), the OXY order awaiting entry, and the new HII
  long. DAL would be the fourth bet on one headline. Being over the cap is the finding.
- **REJECTED — MU buy / CANCEL the awaiting order at 960.** MU last 1097.39, so the 2026-09-18
  order at 960 is 12.5% below the market and will only fill on a 12% break. Chasing it here is
  worse: the FQ4 beat is already out (period 2026-09-30, actual 33.42 vs 32.5625, **+2.6%**) and
  that is the thinnest of four quarters, after +17.3%, +27.3% and +17.4%. Analyst revisions
  **deteriorating** (-1.3pp, a hold added). 12.56% below the 1255.00 high. Catalyst spent.
- **REJECTED — APLD buy** (yesterday's watchlist item, earnings 2026-10-07 amc confirmed).
  24.16, -52.4% off its 50.725 high and only 5.36% off its 22.93 low; ATR 6.45% of price;
  market cap $7.23B on 291.47M shares; ADV $374.6M and a real-time spread of 0.285%, so it is
  perfectly tradeable. Rejected on the driver, not the liquidity: APLD is a **debt-financed
  datacenter developer**, so a 24-year-high 10-year at 5.248% is the thing that halved it. Buying
  it is a fourth position on the rates axis and on the losing side of the one the book is short
  through XLU. Analysts are still 18 buys to 2 holds with the stock down 52% — unrevised
  consensus is a warning, not support. Zero insider buys, 4 sales totalling $3.5M.
- **REJECTED — PEP buy** (earnings 2026-10-08 bmo). 125.60, **0.06% off its 120-day low** of
  125.525, -21.5% off the 160.025 high, below SMA20 132.63 and SMA50 137.17. Same rejection as
  yesterday and now with today's fetched levels: a staples long is a duration long, which
  contradicts the XLU short and the TLT and ITB orders. It is the BCC contradiction again.
- **REJECTED — STZ buy** (earnings 2026-10-06 amc). 112.99, 1.3% off its 111.54 low, -33.0% off
  the 168.60 high, below SMA20 119.56 and SMA50 127.36. Falling knife with no catalyst-independent
  reason to catch it.
- **REJECTED — EPAM buy.** The ACN read-across looked best here on the surface: EPAM 114.35,
  -15.3% off its 135.00 high, and **-14.58% versus ACN over 1m and -25.02% over 3m**. Killed by
  the mechanism. ACN is winning scaled GenAI transformation deals; EPAM sells headcount-based
  engineering, which the same technology disintermediates — so the divergence may be correct
  rather than a gap to close. Confirmed by revisions: **deteriorating**, bullish share 57.7%,
  -3.8pp, a strong buy moving to hold. And the apparent insider signal is a mirage — 6 "buys"
  by 6 buyers totalling just **$45,260, all 78 shares each at exactly 96.71 on 2026-04-30**,
  which is a uniform director fee election, not six people deciding anything. Not cited as evidence.
- **REJECTED — INSW / FRO / STNG buy (tankers).** The Hormuz re-routing play, and the best
  momentum on the screen: INSW 114.60 at its 2-year high, +14.88% 1m against XLE -3.2%,
  +42.06% vs SPY over 6m. Two reasons it does not publish. First, it is a fourth Iran bet.
  Second and worse, **at a 2-year high there is no resistance to anchor a target on**, and the
  2.0 R:R floor off a 2.12 ATR stop at 105.50 needs 135.50+ — a number I can only reach by
  extrapolation. Insiders: 0 buys, 13 sales, -$4.6M. Watchlist, not a recommendation.
- **REJECTED — a second defense name (GD).** 332.72, -16.8% off its 400.00 high, below SMA20
  348.69 and SMA50 370.54, ATR 6.1184. Same trade as HII with a $90.0B market cap instead of
  $10.8B, so less torque on the same driver, and it would be a second slot on one headline.
  ITA is the other expression and is part-spent: it is roughly a fifth Boeing, and BA already
  moved +3.35% on its own $20B F/A-XX award (2026-09-29).

## [06:27 ET] POSITION UPDATE — held unchanged, NOT re-published, and why that is the right call
`merge_report` keeps one live position per (symbol, direction) and a position stays open whether
or not it appears in today's report. So where nothing changed today, re-stating the idea would
only add a row and another tick to the repetition counter. These five were examined and left alone:

- **CCJ** buy, entry 94.00, last 85.69 (-8.8%), target 135.00, stop 82.50. Nothing new today.
  Uranium is its own driver and the stop is live 3.19 below the market. Held unchanged, as yesterday.
- **EEM** buy, entry 65.60, last 66.81 (+1.8%), target 71.50, stop 63.00. One of only two
  profitable longs. Notable but not actionable: EM held up on a day the 10-year hit a 24-year
  high, which a strong dollar normally punishes. Held unchanged.
- **PFE** buy long_term, entry 27.60, last 28.12 (+1.9%), target 42.00, no stop. Yesterday's
  rank 1. Long-term by construction so a hard stop is optional; nothing new today. Held.
- **KHC** buy, entry 23.00, last 22.46 (-2.3%), target 32.00, no stop. Opened 2026-09-20.
  Flagged for a future run, not acted on today: it is a staples long, which is the same duration
  exposure that got PEP rejected and BCC closed. It survives today only on being newer and
  smaller than those. If the 10-year stays above 5.2%, it is next.
- **SVRA** buy, entry 5.35, last 5.045 (-5.7%), target 8.00, stop 4.60. Yesterday's validation
  demoted it on a **7.55% bid/ask spread** — the round trip costs 15% of the target move. That
  has not changed and no re-pitch can fix it. Held, untradeable to add to.
- **CEG** buy, entry 272.00 — appears in yesterday's report as an open position but the order at
  272.00 is listed in today's prior context as *awaiting entry* (published 2026-10-01) after a
  stop-out on 2026-09-30. Flagging the inconsistency rather than guessing which is true.

## [06:27 ET] STALE ORDER HYGIENE — 15 orders awaiting entry, and several cannot ever fill
These were published but never filled, so they are not positions. Four are now so far from the
market that leaving them live is misleading:

- **BTC SELL @ 63,400** (published 2026-08-16) and **/MBTU6 SHORT @ 64,340** (2026-08-18).
  Fetched: BTC **$86,344, +3.18% over 24h** (CoinGecko), so both sit **~26-27% below spot**.
  These are not entries, they are dead orders. **Cancel.** Also note /MBTU6 is a U6 (September
  2026) contract and September is past — the contract has expired regardless of price.
  source: scripts/market_data.py crypto bitcoin
- **MU BUY @ 960** (2026-09-18) — 12.5% below the 1097.39 market, catalyst spent. **Cancel**, per
  the rejection logged above.
- **KXFEDDECISION-26SEP-H25 YES @ 32** (2026-08-22) and **KXFEDDECISION-26SEP-H0 YES @ 47**
  (2026-09-03) — the September FOMC has happened. These should be expired by the tracker, not
  carried as awaiting entry, and they must not be re-pitched. The October contract closes
  **2026-10-28** (fetched) but is unpriceable today, see the event-contract data gap above.
- Left alone, still plausible: DG @ 134.50, VST @ 132.00, IYR short @ 97.80, GLD sell @ 406.77,
  OXY @ 54.00, TLT short @ 79.90, ITB short @ 89.80, KXCPIYOY-26SEP-T3.5 NO @ 18, CEG @ 272.00.
  I did not re-level these; with gold at $4,203.30 the GLD sell at 406.77 is worth a look next run.

## [06:27 ET] WATCHLIST MATERIAL for synthesis to lift
- **DINO** — re-entry on a pullback to the 108.79 SMA20 with its own stop is a legitimate separate
  trade; insider buying is real ($2.42M, 2 buyers). Closed today only because the filled 107.50
  entry cannot carry a compliant stop.
- **INSW** — 114.60 at a 2-year high, strongest relative strength on the screen (+14.88% 1m).
  Needs a defensible target above all-time highs before it can publish. Not a rejection on merit.
- **DAL** — short, earnings 2026-10-09 bmo. Full levels in the rejection above. Blocked only by
  the correlation cap; if XLE or OXY comes off, this is the replacement.
- **XLP** — carried over from yesterday's watchlist, same cap problem, and PEP at a 120-day low
  is the same trade. Still the cleanest expression of the 5.248% ten-year.
- **GLD sell @ 406.77** — stale order, and gold printed $4,203.30. Needs re-levelling.

## [06:28 ET] REJECTED — the rate-sensitive short side is late, and the data says so plainly
Checked all four rate shorts the book holds or has pending against their own ranges:

| Sym | last | 120d low | off its low | 120d high | order standing | ATR14 |
| TLT | 77.71 | 76.76 | **+1.24%** | 87.79 | short @ 79.90 awaiting | 0.8439 |
| IYR | 94.47 | 93.81 | **+0.70%** | 108.17 | short @ 97.80 awaiting | 1.2515 |
| ITB | 87.37 | 84.81 | +3.02% | 106.38 | short @ 89.80 awaiting | 2.0504 |
| XLU | 39.68 | 39.03 | +1.67% | 47.296 | short, open @ 39.60 | 0.5736 |

- All three pending shorts are limits **2.8-3.5% ABOVE the market**, so each fills only if the
  trade first goes against it — the mirror image of the pullback-entry defect that left 42% of
  the first month's longs unfilled, and the reason none of these three has filled.
- **REJECTED — re-levelling the TLT short to the market.** It is the purest expression of the
  thesis and I intended to do it. The data stopped me: **TLT 120-day low of 76.76 is also its
  600-day low** (600-day range 76.76-101.64). A compliant short from 77.71 needs a stop near 79.50
  (2.12 ATR, under the 80.53 SMA20) and therefore a target at or below 74.13 — below every price
  TLT has traded in two years. That target is reachable only by extrapolation, and "no level
  because nothing has traded there" is a reason not to publish, not a licence to invent one.
  The same objection applies to IYR at 0.70% off its low. Leave the orders; do not chase.
- **The XLU short survives this test, and that is why it is the one kept.** XLU 600-day range is
  **33.7975-47.80**, so the last price of 39.68 sits 17.41% *above* its two-year low and the 36.80
  target is inside territory XLU actually traded during the last two years. The target is an
  anchored level, not an extension. Re-captured with that evidence corrected.
- Broader read worth carrying forward: the book published **four** separate shorts on the long-end
  move and all four instruments now sit within 3% of 120-day lows. The thesis has been right and
  the expression is crowded and late. That argues for consolidating into the one with a real
  target, not for adding a fifth.

## [06:30 ET] CORRECTION to the MU rejection — the print was far bigger than I first said
My earlier rejection leaned on a +2.6% surprise from the finnhub field. The actual release is much
stronger and the record should say so: **FQ4 adjusted EPS $33.42 vs $31.61 estimate; revenue
$54.23B vs $51.069B; and FQ1 revenue guided $60.0-63.0B against a $57.4B consensus** — a midpoint
roughly 7% above the street. MU closed +3.03% at 1097.39 on 2026-10-01.
source: https://investrade.com/morning-preview-october-01-2026/

**Still rejected, and now for a better reason than a thin beat.** Annualising the quarter, adjusted
EPS of about $134 against 1097.39 is roughly **8.2x earnings**. That is not evidence of cheapness
— MU's 120-day range is **408.50 to 1255.00**, so the stock has roughly tripled in six months, and
a single-digit multiple on a cyclical that has just tripled is what a cycle *peak* looks like, not
a durable mispricing. Buying the low multiple there is the oldest mistake in cyclical investing,
and I am not going to make it under a time cap with no mid-cycle earnings estimate to anchor on.
- The awaiting order at **960 is better-placed than I credited**: it sits essentially on the SMA50
  (954.35), a real level, and from 960 a 2.05 ATR stop at 868 against a 1150 target (under the
  1255.00 high) gives **R:R 2.07** — a compliant structure. **Left awaiting entry, not cancelled,
  and I withdraw the "cancel" from the earlier note.** It is not re-pitched because I cannot
  defend the valuation case today, not because the level is wrong.
- Separately, note the structural pattern that killed MU, INSW and the TLT re-level alike: an
  instrument with a 4%+ ATR sitting near its high cannot satisfy both a 2.0 ATR stop and a 2.0
  reward-to-risk floor without a target beyond all prior resistance. That is the floors working
  as designed, and it is why today produced one new idea rather than five.

## [06:30 ET] NEWS — two facts that cut against positions in this report, recorded anyway
- **CEG rose on a 20-year Amazon power agreement with a $3B infrastructure investment** (reported
  in the 2026-10-01 preview). This is direct evidence for the datacenter-power-demand case, which
  is the counter-argument to the open **XLU short**. It does not change the XLU decision — the
  sector de-rating still tracks the long end week by week — but it is the strongest version of the
  other side and it is now dated and sourced rather than hypothetical.
  source: https://investrade.com/morning-preview-october-01-2026/
- **CALENDAR CAVEAT:** the fetched finnhub calendar lists **MKC on 2026-10-05 bmo**, but the
  2026-10-01 preview reports MKC has already released Q3 (adj EPS $0.86 vs $0.76, net sales
  +17.4%). One of the two is wrong and I did not resolve it. Treat near-dated calendar entries as
  needing confirmation against a filing before an idea is keyed to one.

## [06:31 ET] REJECTED — financials, the last independent driver available
- **XLF** 53.46, -8.77% off its 58.60 high, 6.03% off its 50.42 low, below SMA20 55.82 and SMA50
  56.86, ATR 0.7629. **KRE** 69.95, -10.72% off its 78.35 high, 5.31% off its 66.42 low, below
  SMA20 72.39 and SMA50 74.43, ATR 1.2793. Banks were named among the worst groups of 2026-10-01
  with the curve *steepening* to +0.46, which is normally margin-expansionary — so the market is
  pricing securities marks, mortgage origination and CRE credit over net interest margin.
- Rejected both directions. **Short** is a fifth bet on the long-end driver, already over the cap.
  **Long** is the contrarian side of that same driver, so it does not escape the cap either, and
  I have no fetched price-to-tangible-book or reserve-coverage figure to build the valuation
  anchor such a call would need — Q3 earnings on 2026-10-13/14 are confirmed and are precisely
  when that case gets settled, which is a reason to wait rather than to guess.
- **XBI** 154.51, -9.05% off its 169.89 high but +23.54% off its 125.07 low, sat between SMA20
  157.76 and SMA50 158.01. Mid-range with no catalyst and no edge. No idea here.
- **KRE note for the record:** this is the symbol CLAUDE.md names as the walked-in-stop failure.
  It was examined and rejected on the driver, with no stop proposed at all.

## [06:33 ET] LONG_TERM LANE — worked deliberately, and it produced nothing publishable
`config/strategy.md` warns this lane gets the leftovers, so it got dedicated time rather than
what was left. The thesis hunted was **P&C insurers as the beneficiary of a permanently higher
long end**: a 5.248% ten-year means float reinvested at yields not seen in 25 years, and unlike
the four short-duration trades in this book that thesis only needs rates to *stay* high, not to
keep rising — a genuinely different claim from the same macro fact.

The whole group has de-rated in step, which is what made it look like an opportunity:

| Sym | last | off 120d high | SMA20 | SMA50 | ATR14 | mcap | revisions |
| TRV  | 361.64 | -9.29% | 368.57 | 371.94 | 6.7107 | $75.43B | **deteriorating, -7.6pp** |
| CB   | 331.30 | -9.46% | 337.26 | 343.25 | 4.7397 | $127.82B | deteriorating, -2.9pp |
| WRB  | 68.90 | -11.04% | 69.08 | 70.18 | 1.3197 | — | not checked |
| ACGL | 94.26 | -11.98% | 95.99 | 98.33 | 1.8954 | $32.16B | flat, 0.0pp |

**REJECTED — all of them, and the reason is a gap in my own work rather than a flaw in the idea.**
Two things stopped it:
1. **The de-rating has a real cause my thesis does not address.** TRV has beaten by **83.4%, 7.9%,
   24.6% and 27.0%** over four quarters and the sell-side has been *cutting* into it — bullish
   share is down to **25.7%**, and sell ratings went 1 to 2 to 5 across the 2026-06-01 through
   2026-09-01 snapshots. Analysts downgrading through an 83% beat is them pricing the P&C
   underwriting cycle rolling from a hard market into a soft one. Softening rate-on-line
   compresses underwriting margin at the same time float income expands, and my thesis only
   covered the second of the two. Revision *direction* is what strategy.md says to read, and it
   points the other way.
2. **I cannot put a price on the downside, which a long_term idea is required to do.** The floor
   is 2.5 measured against an explicit bear-case price, and for an insurer that number is built
   from book value per share and normalised ROE. Neither is available from any source I have
   here, and estimating them from memory is the one thing the non-negotiables forbid outright.
   An idea I cannot put a defensible bear-case price on is not researched enough to publish.
- **Watchlist, with the work already done: TRV, earnings 2026-10-16 bmo confirmed** (est 6.8423
  on $11.49B revenue). The question that settles it is whether the print shows written premium
  rate decelerating; the float thesis is live if it does not. Worth a future run with a source
  for book value.

## [06:33 ET] RESEARCH COMPLETE
- **candidates: 15 rows, 10 distinct symbols** (synthesis takes the last row per symbol;
  XLU, NKE, GDX, LCII and LULU were each re-captured once to correct evidence or conviction).
- **1 genuinely new idea: HII buy.** Everything else is position management:
  2 holds (XLU short, XLE long) and 7 exit orders (NKE, DINO, SNX, GDX, LCII, LULU, BCC).
  **Do not read 10 rows as 10 new opportunities — only HII is new risk.**
- Self-check run over the file before finishing: every idea with levels clears its
  reward-to-risk floor and its ATR stop floor, and **every conviction score equals the count of
  distinct evidence kinds behind it**. Four scores did not and were corrected rather than shipped
  (NKE 4->5, GDX 4->3, LCII 4->3, LULU 4->3).
- **Why one new idea and not five.** Both of the day's live drivers were already at the
  correlation cap before I started: the Iran escalation (XLE held, OXY awaiting, now HII) and the
  long end at a 24-year high (XLU short open, plus IYR, TLT and ITB awaiting). DAL short, XLP
  short, a TLT re-level and a second defense name were all rejected on the cap rather than on
  merit, and their levels are written up so a later run can lift them. The third driver, AI and IT
  services demand, was real and verified via Accenture but its best expressions failed on their
  own merits: SNX catalyst spent with $15.7M of insider selling, EPAM mechanically contradicted,
  MU a cyclical that has tripled in six months.
- **coverage gaps:**
  - **Event contracts: none publishable.** Kalshi returns markets as active but with null bid,
    ask, last and volume on the unauthenticated endpoint, and `market_data.py events` returns
    count 0 for every macro topic tried. A probability-disagreement thesis needs the market's
    implied probability and I could not fetch one.
  - **Earnings calendar hole 2026-10-17 to 2026-11-02.** `--days 12` covers Oct 2-16 and
    `--days 40` returns only Nov 3-11. So I have no fetched earnings date for HII, GD, LMT, NOC,
    RTX, PFE, CCJ or KHC, and the HII idea is deliberately **not** keyed to its Q3 print.
  - **No index, VIX, futures, dollar or spot commodity quote** from `macro` — Yahoo returned
    HTTP 429 across the board and finnhub refuses indices. Index levels and crude, Brent and gold
    prices in these notes come from fetched news, not from a market-data call, and are attributed.
  - **No options-implied move for any idea.** `implied` returns HTTP 401 from yahoo-options, so
    the check on whether a target sits inside what the market prices was not run on HII or XLE.
  - **Short interest unavailable** — `short` timed out against api.nasdaq.com on every attempt.
  - **No crude-oil futures contract idea** (`/MCL`), despite the universe file preferring futures
    for a commodity view, because I had no fetched futures price or contract-month data.
  - **CEG inconsistency unresolved:** yesterday's report carries it as an open position, today's
    prior context as awaiting entry after a 2026-09-30 stop-out. Flagged, not guessed at.
  - **MKC calendar conflict unresolved** — listed as reporting 2026-10-05 but reported as already
    having released Q3.
- **sources that failed:** Yahoo chart API (429, all index/VIX/futures/FX/commodity symbols);
  yahoo-options (401, `implied`); api.nasdaq.com `short` (read timeout, every symbol);
  Kalshi unauthenticated market prices (null on all fields); `market_data.py events` (count 0);
  CoinGecko on the first `macro` pass (recovered on a direct `crypto` call).
