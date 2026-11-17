# Research log — 2026-11-17
- start 06:01 ET

## [06:02 ET] MACRO — regime
Prices are prev-close (2026-11-16 16:00 ET close), market session = pre. Source: finnhub via market_data.py.
- SPY 739.95, prev_close 754.37, **-1.91%** on 11/16. Intraday low 738.07, closed near the low.
- QQQ 661.75, **-2.67%** on 11/16 — tech led the decline. low 660.48, closed at the low.
- IWM 272.94, **-1.66%**. GLD 352.93 -0.71%. TLT 79.38 flat.
- FRED: US10Y **5.15%** (11/13), US2Y 4.88%, fed funds 3.88%, 10y-2y **+0.29** (11/16),
  unemployment 4.1% (Oct), CPI index 337.476 (Oct).
- Regime read: fed funds 3.88% vs 10Y 5.15% = 127bp of term premium above policy. Long end
  is NOT following cuts. Equity drawdown with QQQ underperforming SPY by 76bp in one session.
- SOURCE FAILURES: yahoo returning HTTP 429 for every index (^GSPC/^NDX/^DJI/^RUT/^VIX),
  futures (ES/NQ), DXY, 10Y quote, gold and WTI futures, and coingecko crypto prices all
  FAILED this call. finnhub refuses index CFDs ("subscription required"). So: **no VIX level,
  no overnight futures, no dollar, no crypto prices from the macro call.** Retry individually.

## [06:03 ET] CALENDAR — next 5 sessions (fetched via market_data.py earnings --days 12)
- **2026-11-17 AMC: NVDA** — consensus rev $111.28B, EPS $2.525. The dominant event of the week.
- 2026-11-17 BMO: HD ($44.08B), DIS ($25.43B), TME, VIK, AS, WSM, FUBO, KLAR, ATKR, ENR, GFF
- 2026-11-18 BMO: **TGT ($26.82B), LOW ($22.63B), TJX ($16.00B)**, ROST, GAP, ZIM, BRBR
- 2026-11-18 AMC: **PANW ($3.37B)**, UGI, WWD, CPA, SNEX, KLIC, SBLK
- 2026-11-19 BMO: **BABA ($275.21B), WMT ($189.14B)**, NTES, FUTU; AMC: **INTU**, KEYS, POST, HP, ESTC
- 2026-11-20 BMO: BJ ($6.14B), RLX, MOG.A, FRO, IESC
- 2026-11-24 AMC: ADI, ADSK; 2026-11-25 AMC: DE; 2026-11-26: MRVL
- Read: the week is **NVDA tonight, then the entire US consumer** (HD/TGT/LOW/TJX/ROST/WMT/BJ)
  in a 72-hour block. Two independent drivers, which matters for the correlation cap.

## [06:04 ET] NEWS — the single biggest fact on the tape: NVDA has no CEO
- **Jensen Huang resigned as NVIDIA president, CEO and board member** (~2026-11-12), after
  reports of extramarital affairs, one involving a woman suspected of ties to Chinese
  intelligence. 8-K filed. — source: https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm
- **Colette Kress is INTERIM CEO and remains CFO** until a permanent successor is named.
  — source: https://www.aljazeera.com/news/2026/11/12/why-did-nvidia-ceo-jensen-huang-resign-and-who-is-colette-kress
- NVDA fell 4.3% on 11/13 on this. Board has reportedly approached Arm CEO Rene Haas (FT,
  unconfirmed). — source: https://www.foxbusiness.com/fox-news-tech/new-candidate-emerges-replace-jensen-huang-nvidia-ceo
- A reinstatement campaign is live: ~180k-signature petition; shareholders Brad Gerstner and
  Gavin Baker open letter urging the board to keep "all options on the table, including the
  potential return of Jensen Huang"; allies reported to have formed a "war room".
  — source: https://www.cnbc.com/2026/11/16/nvidia-jensen-huang-return-tech.html
  — source: https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-could-be-plotting-return-as-nvidia-ceo-report-claims-allies-have-formed-a-war-room-to-drive-reinstatement-days-after-resignation-scandal
- **NVDA reports tonight (11/17 AMC) with an interim CEO who is also the CFO and no named
  successor.** The guidance call will be given by someone who may not be there in a month.
- Nasdaq entered a correction after the midterm elections; 11/05 saw NDX -6.36%, the worst
  day since 2020, on AI-capex/datacenter-buildout doubt.
  — source: https://www.investmentnews.com/equities/nasdaq-enters-correction-as-ai-stocks-sink-after-midterm-elections/268903
  — source: https://investinglive.com/stocks/nasdaq-100-suffers-worst-day-since-2020/
- **October PPI final demand +6.5% YoY** (slightly softer than expected on the month but a
  6-handle YoY). That is the reason the 10Y is at 5.15% with fed funds at 3.88%.

## [06:04 ET] IMPLICATION — do NOT take a directional NVDA position into tonight
Prior context: NVDA was published 2x in 10 days and stopped out 11/10 (opened 11/07, conviction 3).
A print delivered by an interim CEO, into a correction, with a reinstatement campaign running,
is not a setup — it is a coin flip with a headline generator attached. The honest trades today
are (a) the separate consumer-earnings driver, (b) the rates/inflation re-acceleration, and
(c) open-position management. Any NVDA-adjacent idea must be sized and stopped for a gap.

## [06:05 ET] LEVELS — NVDA (not a candidate; context for everything AI-adjacent)
history NVDA --days 60, source nasdaq, last_close 2026-11-16 = 156.14
- ATR14 **11.33 = 7.25% of price**. SMA20 195.64, SMA50 213.16. range_high 243.37,
  range_low 148.80. **pct_off_high -35.84%**.
- The resignation bar, 11/12: open 151.005, **low 148.80**, close 166.19 on **747.7M shares**
  (vs 180.6M 30d average). That is the highest-volume bar in the series and 148.80 is the
  only level in this decline with real volume under it.
- 11/13: 169.91 -> 162.85 (-4.3%). 11/16: 159.02 -> 156.14 (-4.12%), closed 1.1 off the low.
- **Why no directional NVDA swing today:** a 2.0 ATR swing stop is 22.7 points = 14.5% of
  price, and the event is an overnight gap, so the stop is not even honoured. Taking it
  tighter to make R:R work is precisely the failure CLAUDE.md names. REJECTED as a swing.

## [06:05 ET] NOTED DIVERGENCE — consumer retail split on 11/16 (SPY -1.91%)
- UP on a -1.91% tape: **WMT +0.25%** (reports 11/19 BMO), **BJ +1.40%** (reports 11/20 BMO)
- DOWN hard: **ROST -3.75%** (reports 11/18), **TJX -2.44%** (11/18), LOW -1.23%, HD -0.34%
- Clubs/supercenters bid, off-price sold, ahead of all four printing inside 72 hours.
  Worth testing whether that is a real trade-down signal or just defensive beta.

## [06:05 ET] DATA GAP — event contracts effectively unavailable this run
`market_data.py events "<topic>"` returns count=0 for Nvidia, Fed, inflation, CPI, recession
and bitcoin. An empty-string query returns 40 markets and **every one of them is a
multi-leg sports parlay** (KXMVECROSSCATEGORY-*). So the Kalshi feed reachable from here is
not surfacing economic or single-name markets today. No event-contract candidate can be
priced honestly, and `config/universe.md` requires a stated implied probability, so
**no event contracts in today's report.** This is a source gap, not an absence of markets.

## [06:06 ET] POSITION UPDATE — TLT — opened 2026-11-04 @ 80.30, now 79.38, -1.1%
- decision: **CLOSE at the 11/17 open.** Captured via add_candidate.py (direction sell, exit).
- why: the thesis needed the long end to rally with cuts. Fetched data says bear steepener —
  10Y 5.15% vs fed funds 3.88% (127bp term premium), 10y-2y +0.29 on 11/16, Oct PPI +6.5% YoY.
- also: stop 78.80 is only 0.58 below price = **0.75 ATR** (ATR14 0.777), well inside the
  repo's 1.8 ATR ETF floor. It will be hit by noise. Do not widen it — that is the mirror of
  the stop-tightening sin. Close instead.
- falsification checked: if risk-aversion duration bid were real, TLT should have rallied
  through two weeks of NDX correction. It did not; it sits below SMA20 81.09 and SMA50 80.15.

## [06:07 ET] POSITION UPDATE — BCC — opened 2026-08-18 @ 76.50, now 66.37, -13.2%
- decision: **CLOSE at the 11/17 open — restating the 11/15 instruction**, which the tracker
  still shows unexecuted (prior_context lists BCC open, last 67.39).
- why: new 90-day low (close 66.37 vs range_low 66.05), -24.9% off high 88.43, below SMA20
  73.83 and SMA50 74.78. Housing thesis needs a lower 10Y; 10Y is 5.15%. Position has no stop,
  which is how -13% accumulated over 90 days.
- captured via add_candidate.py.

## [06:08 ET] CLOCK CORRECTION
Earlier headings in this file were stamped from my own sense of elapsed time and ran ~14
minutes fast. `TZ=America/New_York date` says 06:07 ET. Timestamps above have been corrected
to real clock times; every price and figure above was fetched and is unaffected. Budget runs
06:01-07:01 ET; new research stops at 06:43.

## [06:12 ET] DATA GAP — options-implied move unavailable
`market_data.py implied BJ --entry ... --target ...` returns HTTP 401 Unauthorized from
query1.finance.yahoo.com/v7/finance/options. Same root cause as the yahoo 429s in the macro
call. So **no idea today can state the options-implied move**, and targets are justified from
price history and ATR only. Also failed: `short BJ` (api.nasdaq.com ReadTimeout).

## [06:11 ET] POSITIONING — staples leadership is real, not just defensive beta
- relstrength BJ --peer XLP: BJ +8.67% 1m, +20.7% 3m, +15.3% 6m. SPY -3.05% 1m, -3.58% 3m.
  **BJ vs SPY +11.72% 1m / +24.28% 3m.** BJ vs XLP +2.99% 1m / +12.5% 3m — so BJ is beating
  its own sector by 12.5 points over 3 months, which rules out "it is just the staples bid".
- XLP itself: 92.60, **-0.9% off its 120-day high 93.48**, above SMA20 89.75 and SMA50 85.81,
  ATR14 1.655 (1.79%). Rose on both 11/13 and 11/16 while SPY fell. Staples making highs
  inside an equity correction.
- BJ earnings surprise record, 4 for 4: +13.18% (9/30), +3.70% (6/30), +0.76% (3/31),
  +2.89% (12/31). Analyst revision_direction **flat** (9 strong buy / 9 buy / 13 hold / 1
  sell, unchanged across Aug-Nov) — so the sell side has not chased this; bullish share 56.2%.
- BJ bars: high 113.35 set 11/05, then a two-week 107.60-112.77 shelf, and 11/16 closed
  **111.88 on 1.997M shares** (above the 0.95-1.6M of the prior week) on a -1.91% SPY day.
  Coiled under the high on rising volume. Reports **2026-11-20 BMO**, consensus rev $6.14B,
  EPS $1.2924.

## [06:14 ET] REJECTED — TJX / ROST short — the "off-price breaking down" read has no sourced 2026 driver
Searched for a November 2026 off-price guidance/tariff driver. Results were overwhelmingly
**November 2025** coverage (TJX Q3 FY26 beat-and-raise, dated 2025-11-18). The only
2026-relevant item found — TJX lowering near-term sales guidance, a Marmaxx same-store miss,
$331M of tariff refunds — comes from tradersunion.com and I could not pin it to a date or to
a TJX filing. — source: https://tradersunion.com/news/financial-news/show/3038442-tjx-profit-outlook-marmaxx-sales/
So TJX -19.6% off high and ROST -13.2% off high are facts I have, with **no sourced reason**.
Shorting a defensive compounder into its own print on unexplained weakness, needing margin,
is not an idea. REJECTED both directions. (Had the reason checked out, the long side — buying
a 19.6% de-rating in a tariff beneficiary — would have been the better trade, not the short.)

## [06:15 ET] TRACK RECORD — the one signal in it that is not noise, and what I am doing about it
Closed-trade counts: **stock 1/28 hit target (4%), avg -8.3%** vs **etf 3/14 (21%), avg -1.9%**.
n=28 on stocks is past the ~15 threshold prior_context sets for noise, so the single-name
stock picking in this report is genuinely bad, not unlucky. ETFs at n=14 are just under the
line, so "ETFs are good" is NOT yet established — but "single names are losing" is.
Conviction 2: 0/6, avg -8.4% (n=9) — under the threshold, so noise, but no reason to reach.
**Action taken today:** single-name ideas must carry a dated catalyst AND a measured
positioning read AND a real technical level (3 evidence kinds, conviction 4+) to be captured;
a conviction-3 single name on a chart pattern is not getting published today. Index/sector
expressions are preferred where the thesis is macro rather than company-specific, per
config/universe.md's instrument-substitution rule. long_term shows 0/4, avg -15.2% on n=10 —
under threshold, noted, not over-fitted.

## [06:17 ET] SECTOR LEADERSHIP MAP — relstrength vs SPY (1m / 3m, computed from price history)
- **XLV +9.37 / +14.27** <- the leadership sector. Absolute +28.93% 6m. close 187.88, -2.3%
  off high 192.32, above SMA20 184.26 and SMA50 175.37, ATR 3.834 (2.04%), advol $1.95B.
  Fell only 0.5% on 11/16 against SPY -1.91%.
- **XLP +8.73 / +11.78** — close 92.60, -0.9% off high, above SMA20/SMA50.
- **XLF +7.84 / +4.17** — close 58.18, -3.1% off high 60.04, above SMA20 57.22, SMA50 55.97.
  Consistent with the bear steepener (10y-2y +0.29): NIM widens.
- KRE +6.46 / -2.48 — close 72.19, -7.9% off high, *below* SMA20 72.53. Regionals are NOT
  participating in the financials bid. (KRE is also the name CLAUDE.md records as the
  stop-walking offence; no KRE idea today.)
- XLE -3.62 / +3.60 — close lagging, -6.67% absolute 1m.
- **GLD -4.56 / -7.87** (absolute -15.65% 6m) and **SLV -14.66 / -22.62 (absolute -39.39%
  6m)**. Precious metals are in a severe bear move *while* PPI runs +6.5% YoY. Coherent:
  nominal 10Y 5.15% is a high bar for a zero-coupon asset. Note the 2026-11-16 run already
  published GLD sell_short @ 366 (tgt 336, stop 381); GLD closed 352.93, so that one is in
  profit and short of target.

## [06:17 ET] CORRELATION WATCH — healthcare is already at the cap
Open: PFE (+4.7%) and ABT (+5.4%), both XLV constituents. XLV BUY @ 184.00 is on the
awaiting-entry list from 11/09 and never filled (post-publication lows: 185.36, 186.70,
186.85, 187.60 — 184.00 was never touched). Adding the sector ETF on top of two of its own
members is a third unit of the same driver, which is the limit config/strategy.md sets.
Decide at consolidation whether XLV earns the third slot or whether PFE/ABT already express it.

## [06:19 ET] REJECTED — SLV short — right direction, wrong moment, and duplicates a live idea
SLV 42.39, **-38.9% off high 69.34, closed 2026-11-16 at a new 120-day low** (bar low 42.01,
gapped down from the 44.13 close). SMA20 47.27 is 11.5% above price, SMA50 52.52. ATR 1.648
(3.89%). The downtrend is intact and accelerating.
Rejected anyway: (a) the only honest entry is a bounce into the 44.00-45.20 shelf, i.e. the
trade has no entry at today's price without chasing a new low; (b) it is the **same driver**
as the already-published GLD short — both are a real-rates trade — so it would be a second
unit of one bet; (c) shorting an ETF needs margin.

## [06:19 ET] GLD — resolving whether the 2026-11-16 short filled. **It did not.**
The 11/16 run published GLD sell_short entry 366.00, target 336.00, stop 381.00. GLD's
*entire* 11/16 range was **351.96-356.29**, so 366.00 never traded after publication. The
short is awaiting entry, now 3.7% ABOVE market. (prior_context's "GLD SELL @ 406.77
(published 2026-10-25)" is the older, staler version of the same idea.)
GLD now: 352.93, -17.81% off high 429.42, range_low 351.96 set 11/16, SMA20 367.45,
SMA50 379.83, ATR14 7.566 (2.14%).
No new metals short today, for the SLV reasons above. The 366.00 level is a sell-the-bounce
entry that is still structurally valid (it sits between the SMA20 367.45 and the 11/11 high
369.38) but I am not re-pitching it — it needs a 3.7% rally to engage and I have no new
information since 11/16 that makes it better.

## [06:20 ET] POSITION UPDATE — ACM — opened 2026-11-07 @ 66.74, now 72.50, +8.6%
- decision: **CLOSE the remainder, take the profit.** Captured via add_candidate.py.
- what happened: ACM filed an **8-K on 2026-11-16** (accession 0001104659-26-128300) — I read
  it. FY2026 Q4/full-year release issued 11/16; board declared a quarterly dividend of
  **$0.34, +10% from $0.31**, payable 2027-01-22, record 2027-01-06. Revenue/EPS/backlog are
  in Exhibit 99.1 which I did NOT retrieve, so I am claiming no figures from it.
  — source: https://www.sec.gov/Archives/edgar/data/868857/000110465926128300/tm2629784d1_8k.htm
- tape: 11/16 open 70.40, high 72.68, close **72.50 (+2.8%) on 2.349M shares** vs 1.215-1.459M
  on each of the four prior sessions, on a day SPY fell 1.91%. The print was received well.
- why close rather than hold: the catalyst the position existed for has now occurred. From
  72.50, reward to the 77.22 target is 4.72; an honest 2.0-ATR stop (ATR14 2.264) is ~67.00,
  below the 11/09 low 67.17, so risk is 5.50. **Forward R:R 0.86:1** — below 1, and below the
  2.0 swing floor the idea had to clear to be published in the first place.
- and: this report's closed record is 4/42 reaching target (10%). Holding a +8.6% winner for
  the last 6.5% to a target is a one-in-ten bet here. Also ACM has been published **3x in 10
  days**, which prior_context flags as anchoring, not conviction.
- note on mechanics: I did NOT raise the stop above the 66.74 entry. A stop above entry makes
  the published risk negative and the R:R infinite, which is the number-inflation CLAUDE.md
  warns about. Closing is the honest version of the same decision.

## [06:17 ET] SYSTEMATIC AUDIT — stop distance across all 13 open positions with a stop
Two different measures, and conflating them gives the wrong answer. |entry-stop|/ATR is stop
*placement*; |close-stop|/ATR is how much room is left *now*. ATR used is today's ATR14, not
the ATR at entry, so the @entry column is approximate. Floors: 2.0 stock, 1.8 ETF.

| sym | entry | stop | close | ATR14 | @entry | @now |
| --- | --- | --- | --- | --- | --- | --- |
| KHC | 23.00 | 21.20 | 25.07 | 0.738 | 2.44 | 5.25 |
| OXY | 54.00 | 50.15 | 57.36 | 1.834 | 2.10 | 3.93 |
| AAL | 13.35 | 14.40 | 13.24 | 0.612 | **1.72** | 1.90 |
| UNP | 288.60 | 277.40 | 303.71 | 6.380 | **1.76** | 4.12 |
| ABT | 103.00 | 97.00 | 107.45 | 3.048 | **1.97** | 3.43 |
| PYPL | 56.50 | 54.10 | 58.83 | 1.605 | **1.50** | 2.95 |
| RTX | 199.00 | 186.00 | 194.89 | 5.705 | 2.28 | **1.56** |
| XLU | 43.30 | 41.80 | 44.12 | 0.603 | 2.49 | 3.84 |
| ONON | 34.20 | 30.69 | 32.76 | 1.719 | 2.04 | **1.20** |
| TLT | 80.30 | 78.80 | 79.38 | 0.777 | 1.93 | **0.75** |
| HII | 262.00 | **NONE** | 302.09 | 14.019 | - | - |
| PFE | 27.60 | **NONE** | 28.86 | 0.807 | - | - |
| BCC | 76.50 | **NONE** | 66.37 | 3.620 | - | - |

Readings:
- **Four stops were placed inside the floor**: PYPL 1.50, AAL 1.72, UNP 1.76, ABT 1.97 ATR.
  All four are in profit, so there is nothing to act on — but it confirms the pre-floor legacy
  book still carries stops the current validator would reject. Do not retro-widen them; they
  are filled positions and the exits are amendable, but widening a stop on a *winner* to
  "fix" a ratio is the same arithmetic massage in reverse.
- **RTX 1.56 / ONON 1.20 / TLT 0.75 @now** are not badly placed stops — ONON was placed at
  2.04 and RTX at 2.28. Price has simply travelled most of the way to them. **That is the stop
  working.** The only one of the three I am closing early is TLT, and for a thesis reason
  (bear steepener), not for being near its stop.
- **Three positions still carry no stop at all**: HII (+15.3%, ATR 14.02 — a 2.0 ATR stop is
  28 points wide), PFE (+4.5%), BCC (being closed today). HII and PFE are long-horizon-style
  holds; neither gets a retro-fitted stop from me today, but both should be flagged.

## [06:22 ET] POSITION UPDATE — ONON — opened 2026-11-03 @ 34.20, now 32.76, -4.2%
- decision: **CLOSE at the 11/17 open.** Captured via add_candidate.py.
- the fact that decides it: ONON filed **Q3 2026 results on Form 6-K on 2026-11-10** and
  **beat EPS by 12.88%** ($0.46 vs $0.4075) — and the stock fell **-7.5% that session**
  (37.53 -> 34.70) and closed lower in all four sessions since, to 32.76. Highs step down
  37.99, 35.58, 35.55, 34.51, 34.28, 33.64.
  — source: https://www.sec.gov/Archives/edgar/data/1858985/000185898526000025/a26q3-form6xk.htm
- analysts: revision_direction **deteriorating**, bullish share 81.6% and **-1.7pp**. So the
  high bullish share is being cut, not defended.
- this is thesis invalidation, not "the price fell": the position was opened for the print,
  the print beat, and the beat was rejected. Also consistent with PPI +6.5% YoY squeezing the
  discretionary wallet that buys premium footwear.
- stop 30.69 is only 1.20 ATR away so closing saves ~1 day's range; the reason is the thesis,
  not the stop distance.

## [06:22 ET] POSITION UPDATE — RTX — opened 2026-11-02 @ 199.00, now 194.89, -2.1% — HOLD
- stop 186.00 was placed at 2.28 ATR and is 1.56 ATR away now. That is the stop working, with
  room left. 11/16 closed 194.89 after a 199.67 open (an outside-down day with SPY -1.91%).
- no new information against the thesis: no 8-K, defense demand intact, HII (same driver) is
  +15.3%. **Levels UNCHANGED — stop stays 186.00, target 226.50. Do not add, do not widen.**
- not captured as a candidate: nothing changed, and re-pitching an unchanged hold is how the
  repetition problem starts. Recorded here as the decision.

## [06:22 ET] POSITION UPDATES — the rest of the book, all HOLD, levels unchanged
Decided from the stop audit above plus the 11/16 closes; none captured as candidates because
nothing changed for any of them, and a re-pitch with no new information is the anchoring
failure prior_context warns about.
- **KHC** 25.07, +9.0%, stop 2.44 ATR at entry / 5.25 now. Working. Hold.
- **OXY** 57.36, +6.2%, stop 2.10/3.93 ATR. Below SMA20 60.23 but well clear of the stop; XLE
  is the 1m laggard (-6.67%) so do not add. Hold.
- **AAL** short 13.24 vs 13.35 entry, +0.8%. Stop 14.40 placed at 1.72 ATR — inside the floor,
  but it is a filled short in small profit and retro-widening a stop is not a fix. Hold.
- **UNP** 303.71, +5.2%, target 315.99 now only 4.0% away, stop 4.12 ATR below. Hold; the
  next decision is at the target, not today.
- **ABT** 107.45, +4.3%, stop 3.43 ATR below. Healthcare is the leadership sector (XLV +14.27
  vs SPY 3m). Hold.
- **PYPL** 58.83, +4.1%, stop 2.95 ATR below. Hold.
- **XLU** 44.12, +1.9%, stop 3.84 ATR below. Hold.
- **HII** 302.09, **+15.3%, no stop**, ATR 14.019. Flagged: a 2.0 ATR stop would be 28 points
  wide. Hold, but this is the largest unprotected open profit in the book.
- **PFE** 28.86, +4.5%, no stop. Long-horizon hold. Hold.

## [06:25 ET] REJECTED — XLF long — sound thesis with an internal contradiction I cannot resolve
The bear steepener (10y-2y +0.29, 10Y 5.15% vs fed funds 3.88%) widens bank NIM, and XLF is
+7.84 vs SPY 1m, close 58.18, -3.1% off high 60.04, above SMA20 57.22 and SMA50 55.97.
But **KRE is -7.9% off its high and BELOW its SMA20 (72.53 vs 72.19 close), -2.48 vs SPY 3m.**
The credit-sensitive half of financials is not participating. In a 5.15% 10Y world that
divergence most plausibly says the market is pricing bank *credit* risk, which is the thing a
steepener thesis ignores. I cannot settle it in the time left, so no recommendation.
Watchlist-grade at best. (And no KRE idea today regardless — CLAUDE.md records KRE as the
stop-walking offence.)

## [06:25 ET] XLV — resolved. AMEND and capture, at conviction 3 not higher.
Captured. entry 183.50 (zone 182.00-184.00) on the rising SMA20 184.26, stop 174.50 below the
SMA50 175.37 (9.00 = 2.35 ATR vs the 1.8 ETF floor), target 203.50, R:R 2.22, worst in-zone
fill 184.00 still gives 2.05. win_probability 0.42 against a 1/(1+2.22)=31.1% baseline, so a
~11-point claimed edge.
- Amends the 11/09 XLV BUY @ 184.00 that never filled — post-publication lows were 185.36,
  186.70, 186.85, 187.75, 187.22, 187.60. Level essentially unchanged; the SMA20 rose to it.
- **Conviction 3, not 4.** Two distinct evidence kinds only: positioning (relstrength) and
  technical_level (price history). A sector ETF has no dated catalyst, and the obvious third
  entry — "counter_argument_answered" — would be argued from the *same* relstrength numbers
  already counted under positioning. That is the double-count config/strategy.md forbids.
- Correlation: this is the **third** idea on the healthcare driver (open PFE, open ABT). At
  the cap. No further healthcare idea today.

## [06:21 ET] POSITION UPDATE — PFE — opened 2026-08-18 @ 27.60, now 28.86, +4.5% — HOLD
- **Verified the insider cluster today** (insiders PFE, finnhub, 6-month window): **3 open-market
  buys by 3 distinct buyers, $2,960,110 of purchases against $134,661 of sales, net +$2,825,449.**
  - BOURLA ALBERT (CEO) — 38,000 sh @ 26.34 on 2026-08-12
  - Buckley Mortimer J — 37,632 sh @ 25.52 on 2026-08-05
  - BLAYLOCK RONALD E — 39,231 sh @ 25.46 on 2026-08-05
- **But it is not new information.** Those buys are from early August and the position was
  opened 2026-08-18, so this is almost certainly the evidence the original thesis rested on.
  Verifying it today confirms the position; it does not justify a re-pitch.
- PFE 28.86 is ~12% above the insiders' ~25.77 average cost. Healthcare is the leading sector.
  No stop on the position (long-horizon hold), target 42.00.
- decision: **HOLD, levels unchanged. Not captured as a candidate — nothing changed.**
- Also screened for insider clusters: TJX 0 buys, ROST 0, KHC 0, HUN 1 buyer, CVS 1 buyer.
  Only PFE shows a genuine multi-buyer cluster. (HUN @ 9.00 and CVS @ 79.00 are both on the
  awaiting-entry list; a single buyer is not the cluster signal and neither is re-pitched.)

## [06:24 ET] CRYPTO — fetched. coingecko worked on retry (it failed inside the macro call).
- **bitcoin 64,407** (-0.44% 24h, 24h vol $33.99B), **ethereum 1,804.79** (-0.32%),
  **solana 72.94** (+1.84%). asof 2026-11-17 ~06:23 ET. 24/7 market, so these are live prices,
  not a previous close.
- `history BTC-USD` returns ok:false, so for daily levels I used **IBIT** as the proxy:
  close 36.79, **-25.5% off its 120-day high of 49.39**, SMA20 43.68, SMA50 45.30, ATR14 1.506
  (4.09%). Closes 43.03, 42.88, 42.32, 41.68, 42.24, 40.36, 38.94, 36.79 — an accelerating
  decline, and 11/16 was the low of the series.

## [06:24 ET] REJECTED — /MBT short — the view was right, and I am not re-pitching it
`/MBTZ6` SHORT @ 74,075 was published 2026-11-09 (and is flagged 2x in 10 days). BTC is now
64,407, **13% below that entry — so the short never filled and the move happened without it.**
Re-pitching a short 25% into the decline is the SLV objection again: the only non-chasing
entry is a bounce, and I have no new information since 11/09. Also the same driver as GLD/SLV.
Honest record: right direction, entry never reached, no money made. That is an entry-placement
failure, not a thesis failure, and it is the third one today (GLD @ 366, XLV @ 184, /MBT @ 74075).

## [06:25 ET] REGIME SYNTHESIS — one trade is driving nearly everything on the tape
Put the day's measurements together and they are not six independent facts, they are one:
**a real-rate shock is repricing every asset whose value sits far in the future or pays no
cash, all at once.**
- Nominal 10Y **5.15%** against fed funds 3.88%; 10y-2y **+0.29** and steepening; Oct PPI
  final demand **+6.5% YoY**.
- Repriced down, hard: gold **-17.8%** off high, silver **-38.9%**, bitcoin/IBIT **-25.5%**,
  NVDA **-35.8%**, QQQ in correction, TLT -6.4% off high and below both MAs.
- Leading: **XLV +28.9% 6m**, XLP (-0.9% off its high), BJ, WMT — cash-generative,
  near-dated-cashflow defensives.
**Consequence for today's report, stated plainly:** BJ long and XLV long are the same side of
this one regime trade, and TLT/BCC/ONON/ACM closes are all exits of positions on its wrong
side. So the book I am proposing is **less diversified than the symbol count suggests** — two
new longs on one driver, not two drivers. If tonight's NVDA print reignites risk appetite and
the 10Y falls, both new ideas lose together. Synthesis must say so in data_quality_notes
rather than presenting six symbols as six bets.

## [06:27 ET] SMALL/MID-CAP HUNT — screened five earnings names, captured none. Why.
Screened the 11/18-11/20 earnings list for sub-$2B names fitting the defensive-leadership
regime. All five rejected, each for a stated reason:

- **REJECTED — BRBR** (BellRing Brands, 10.55, reports 11/18 BMO, advol $40.6M). Looked right
  on the chart: -26.2% off its 14.29 high but +44% off the 7.33 low and above a rising SMA20
  9.67 / SMA50 9.00, +14.93 vs SPY 1m. The fundamentals kill it. **Three EPS misses in four
  quarters: -20.06%, -56.54%, +14.55%, -8.65%** — that -56.5% is why it halved. Analyst
  revision_direction **deteriorating**, bullish share 63.6% and **-3.1pp** (a hold added in
  November). Insiders: one buyer, **$19,998** — not a cluster, it is a rounding error. Buying
  a serial misser 24 hours before it reports is how the 1-for-28 single-name record was made.
- **REJECTED — JJSF** (J&J Snack Foods, 88.26, reports 11/18 BMO, ~$1.7B cap, advol $18.7M).
  The best of the five and the closest call. Genuinely good positioning: revision_direction
  **improving**, bullish share **88.9%, +11.1pp**; last print +11.94%; +15.13 vs SPY 1m,
  +20.23 6m; above rising SMA20 86.55 and SMA50 82.35, -4.8% off the 92.75 high.
  **Rejected on the arithmetic, not the story.** ATR14 is only 2.638 (2.99%), so a 2.0-ATR
  stop is ~5.3-7.0 wide, and from a post-print breakout entry at 93.00 the 2.0 floor demands a
  **104-107 target = +17.8% to +21% from the last close, and 12-15% above its 120-day high**.
  That is a target built to clear the floor rather than a level I can defend on a $1.7B snack
  company over weeks — exactly what config/strategy.md forbids. Add two misses in four
  quarters and an 11.1pp analyst upgrade that has already raised the bar for tomorrow's print.
- **REJECTED — IESC** (165.90, **-59.4% off its 408.25 high**, SMA50 265.57, **ATR14 10.02%**,
  reports 11/20). An electrical/datacenter contractor mid-collapse. A 2.5-ATR stop is 25% wide.
  No time to establish whether the backlog is intact; not touchable on a chart alone.
- **REJECTED — ROAD** (79.12, -39.1% off its 129.91 high, ATR 8.11%, reports 11/19 BMO). Same
  objection as IESC, same lack of a researched reason for the de-rating.
- **REJECTED — NGVC** (28.45, -17.8% off high, below SMA20 29.55 and SMA50 29.69).
  **advol $2.9M** — clears the $500K floor but a position would be a large share of a day's
  volume, and it is in a downtrend. Not worth the exit risk.

## [06:28 ET] REJECTED — XLP long — concentration, and the target has to be stretched
XLP 92.60, -0.9% off its 93.48 high, above SMA20 89.75 and SMA50 85.81, +8.73 vs SPY 1m. A
clean uptrend. Rejected on two grounds: (a) it would be a **third** position on the
defensive-leadership driver behind BJ and XLV, which per the regime note above is really one
trade, not three; (b) ATR14 1.655 means a 1.8-ATR stop is ~3.0 wide and the 2.0 floor then
needs roughly +7% from an entry already at an all-time high. Same stretched-target objection
as JJSF. BJ is the better-evidenced expression of the same idea and is already captured.

## [06:26 ET] REJECTED — BABA (both directions) — but the disconnect is worth the watchlist
Checked it specifically to find an idea on a **different driver** from the US real-rate trade,
since both of today's new longs sit on the same one. It does not qualify either way.
- Price: 90.62, **-32.4% off its 134.09 high, closed 2026-11-16 at the 120-day low (90.57)**,
  SMA20 101.36, SMA50 106.42, ATR14 3.819 (4.21%), advol $908M. Reports **11/19 BMO**,
  consensus revenue $275.21B.
- **Four consecutive EPS misses: -20.69%, -89.50%, -38.47%, -22.09%.**
- Relative: -13.9 vs SPY 1m, -25.71 3m, **-32.18 6m**; -25.75 vs QQQ 6m.
- **And yet analyst bullish share is 91.5% with revision_direction flat — unchanged.** The
  sell side has not cut this name at all through a 32% decline and four straight misses.
- Rejected long: nothing has turned, four misses is a pattern not an accident, and the last
  bar closed on the low. Rejected short: it is the chasing objection again (new 120-day low,
  no non-chasing entry), it needs margin, 4.21% ATR, and Chinese ADRs carry violent
  stimulus-headline squeeze risk that a 2.5-ATR stop does not survive.
- **Watchlist-grade observation**, which synthesis may use: 91.5% bullish with flat revisions
  into a fifth print, after four misses, is a measured one-sided positioning set-up. If the
  11/19 print misses again, the downgrade cycle has not even started.

## [06:28 ET] ARITHMETIC CHECK — both new ideas recomputed from their own levels
Done before writing the completion block, because validation will recompute all of it anyway
and a number I wrote about my own idea is the one thing CLAUDE.md says never to trust.
- **BJ** entry 113.60, stop 107.40, target 126.00. risk 6.20, reward 12.40, **R:R 2.000**
  (floor 2.0, met exactly, not exceeded by nudging the target). Stop distance
  6.20/2.4775 = **2.503 ATR** against the 2.0 stock floor. Baseline win rate 1/(1+2.00) =
  **33.3%**; claimed win_probability 0.40, so the asserted edge is **+6.7 points** — small on
  purpose. Stated risk_reward 2.0 matches the recomputation.
- **XLV** entry 183.50, stop 174.50, target 203.50. risk 9.00, reward 20.00, **R:R 2.222**
  (floor 2.0). Stop distance 9.00/3.834 = **2.347 ATR** against the 1.8 ETF floor. Baseline
  1/(1+2.222) = **31.0%**; claimed 0.42, asserted edge **+11.0 points**. Stated 2.22 matches.
- Neither stop was moved to make a ratio work. BJ's 107.40 is set below the 107.60 shelf low
  and XLV's 174.50 below the SMA50 at 175.37; the targets were then derived from those stops,
  in that order.
- The four closes carry null target, null stop and null risk_reward by design — a position
  exit has no reward-to-risk and inventing one would be a fabricated number.

## [06:29 ET] VENUE CHECK
Every instrument in today's report is plain US-exchange-listed equity or a sector ETF on
`Robinhood Stocks`: BJ (NYSE), XLV (NYSE Arca), TLT (Nasdaq), BCC (NYSE), ACM (NYSE),
ONON (NYSE, Class A ADS). None requires margin — the two new ideas are long and the four
closes are exits of existing longs, so no `sell_short`, no futures contract, no crypto pair
and no event contract appears today. That removes the whole class of availability risk the
universe file warns about; nothing here rests on a remembered product list.

## [06:30 ET] COVERAGE GAP — no long_term idea today, and the reason
config/strategy.md asks for deliberate long-horizon time and I gave it the thought but am
capturing nothing. A long_term idea requires a defended valuation anchor with the method
shown, an explicit bear-case *price*, and a 2.5 reward-to-risk floor measured against it. I
did not build a defensible valuation for anything this morning, and assembling one in the
last ten minutes would be the fabricated number rule 2 forbids. The honest output is zero
long_term ideas plus this note, not a DCF invented to fill the lane. (Open PFE and HII are
long-horizon holds already carrying that exposure; both reviewed above, both HOLD.)

## [06:30 ET] RESEARCH COMPLETE
- **candidates: 6** — 2 new-money ideas and 4 position exits.
  - NEW: **BJ** buy swing conv4, breakout entry 113.60 (above the 113.35 high), stop 107.40,
    target 126.00, R:R 2.00, 3% — earnings 11/20 BMO.
  - NEW/AMENDED: **XLV** buy swing conv3, entry 183.50 (zone 182.00-184.00 on the rising
    SMA20), stop 174.50, target 203.50, R:R 2.22, 3% — amends the unfilled 11/09 XLV @ 184.00.
  - CLOSE: **TLT** (bear steepener contradicts the thesis), **BCC** (restates the unexecuted
    11/15 close; new 90-day low, no stop), **ACM** (+8.6%, catalyst passed 11/16, forward R:R
    0.86:1), **ONON** (-4.2%, Q3 beat on 11/10 was sold -7.5%, revisions deteriorating).
- **All 14 open positions were reviewed and decided.** 4 closes above; HOLD with levels
  unchanged on RTX, KHC, OXY, AAL, UNP, ABT, PYPL, XLU, HII, PFE — each with its reason
  recorded, none re-pitched, because none had new information.
- **The single most important caveat for synthesis:** BJ and XLV are **the same bet**, not
  two. Both are the long side of one real-rate-shock rotation (see the 06:25 regime note), and
  all four closes are exits from its wrong side. If tonight's NVDA print reignites risk
  appetite, both new ideas lose together. Say this in data_quality_notes.
- **NVDA reports tonight (11/17 AMC) with an interim CEO who is also the CFO, no named
  successor, and a live reinstatement campaign.** No position was taken for or against it, by
  choice; the reasoning is in the 06:04 and 06:05 notes.
- coverage gaps: **no long_term idea** (reason above); **no event contracts** — the Kalshi feed
  returned only sports parlays (06:05 note); **no options-implied move on any idea** — the
  yahoo options endpoint returns HTTP 401 (06:12 note); **no VIX, no overnight index futures,
  no DXY** — yahoo 429s in the macro call (06:02 note); no intraday idea, because every
  equity price available at 06:00 ET is the previous close and the only dated intraday
  catalysts today are the HD and DIS prints that land at the same time as this report.
- sources that failed: yahoo (HTTP 429 on ^GSPC/^NDX/^DJI/^RUT/^VIX/ES/NQ/DXY/gold/WTI;
  HTTP 401 on the options endpoint), finnhub (refuses index CFDs), stooq (404 on indices),
  alphavantage (no api key), api.nasdaq.com (ReadTimeout on `short BJ`), Kalshi events
  (count=0 for every economic topic), `history BTC-USD` (ok:false — used IBIT as the proxy).
  coingecko failed inside the macro call but **succeeded on a direct retry**.
- prices: every equity and ETF figure is the **2026-11-16 16:00 ET close**, fetched this
  morning with market_session=pre. That is a closed market, not stale data. Crypto figures are
  live (24/7). Run started 06:01 ET, on schedule — no late-run stamp applies.

## [06:33 ET] REJECTED — the whole shipping/tanker complex — no trend to trade
Checked specifically to find a driver orthogonal to the real-rate rotation (freight rates are
not a US duration story). Screened the five names reporting 11/18-11/26:
- **FRO** 45.44, -23.9% off high 59.75, below SMA20 49.99 and SMA50 50.92, ATR 5.60% (11/20)
- **NAT** 6.54, -26.4% off high, below both MAs (11/26)
- **DSX** 2.32, -27.5% off high, below both MAs, **advol $1.7M** — too thin (11/25)
- **SBLK** 27.40, -16.7% off high, below both MAs (11/18)
- **ZIM** 29.11, -6.0% off high 30.98 — the only one not in a downtrend, but it is pinned
  *between* its SMA20 28.90 and SMA50 29.37, i.e. no trend at all (11/18 BMO, EPS est $3.8456)
Four of five are below both moving averages, and the fifth has no direction. There is no long
setup here and no researched freight-rate driver I could verify in the time available, so the
orthogonal-driver slot stays empty rather than being filled with the least-bad chart.

## [06:34 ET] BJ — required insider check came back AGAINST the idea. Disclosed, size cut.
The skill mandates an insider check on every equity finalist, so I ran it on BJ and it is the
one genuinely negative fact I found today about an idea I was keeping:
- **0 open-market purchases. 27 sales. $35,591,483. net -$35,591,483** over the trailing six
  months. Form 144 notices filed 2026-10-15 and 2026-11-02; Form 4s on 10/15, 10/16 and 11/04.
  — source: https://finnhub.io/api/v1/stock/insider-transactions
- I cannot separate scheduled 10b5-1 and option-exercise sales from discretionary ones with
  this data, so this is not proof of anything. But config/strategy.md's "absence of insider
  buying is not a negative" covers an *empty* record, and this is not empty — it is $35.6M of
  one-way selling into a price 1.3% from the all-time high.
- Action: **re-captured BJ with the figures written into key_risk and counter_argument, and
  position_size_pct cut 3% -> 2%.** Not dropped: the entry is still conditional on a breakout
  above 113.35, so the market has to confirm before money is risked.
- **And a conviction correction worth recording.** I first re-captured BJ at conviction 5,
  because adding a `counter_argument_answered` entry made four distinct evidence kinds and the
  config table maps 4 kinds to 5. That was wrong twice over: the entry recycled the
  recommendation-trend and XLP numbers already counted under `positioning`, which is the
  double-count the config forbids; and raising conviction on the strength of evidence that came
  back *against* the idea, in the same breath as cutting its size, is precisely the inflation
  the file warns about. Re-captured again at **conviction 4** with three kinds. Three BJ lines
  now sit in candidates.jsonl; **synthesis must take the last one** (conviction 4, size 2%).

## [06:37 ET] XLV BREADTH CHECK — the gain is broad, and conviction still stays at 3
Tested the one way a sector-ETF thesis fails quietly: that the index gain is one or two
mega-caps, making the ETF a fragile proxy. relstrength on the eight largest constituents,
each measured against XLV:

| sym | 1m | 3m | 6m | vs XLV 3m |
| --- | --- | --- | --- | --- |
| TMO | +0.19 | +17.37 | **+56.41** | +6.68 |
| LLY | +13.89 | +16.80 | **+44.89** | +6.11 |
| AMGN | +6.90 | +8.71 | **+42.52** | -1.98 |
| ABBV | +3.20 | +13.76 | **+40.66** | +3.07 |
| MRK | -1.02 | +6.87 | **+28.34** | -3.82 |
| JNJ | +10.56 | +4.22 | **+23.43** | -6.47 |
| BMY | +5.32 | -4.72 | +9.81 | -15.41 |
| UNH | +2.64 | +4.59 | +5.34 | -6.10 |

**All eight positive over 6m; seven of eight over 3m; seven of eight over 1m.** So XLV's
+28.93% is not a single-name proxy. Re-captured XLV with this folded into the thesis and the
existing positioning entry.
- **Conviction stays 3.** Two temptations declined. It is the same evidence *kind* as the
  relstrength already counted (`positioning`), and two entries of one kind are one
  confirmation. And it does not answer the counter-argument I actually wrote, which is
  exhaustion — eight-for-eight positive over six months is, if anything, *consistent* with
  "everything here has already run," so filing it as `counter_argument_answered` to reach a
  fourth kind would be dressing up a confirmation as a rebuttal.
- That is the second declined conviction upgrade today (BJ was the first). Recording both
  because the repo's history is conviction inflation, and a score I talked myself out of
  raising is more informative than one I raised.

## [06:40 ET] RESEARCH COMPLETE — supersedes the 06:30 block
The 06:30 completion block was written with budget still left and is superseded by this one.
Work done after it: the BJ insider check and the size cut and conviction correction that
followed (06:34), the shipping-complex screen (06:33), and the XLV constituent breadth check
(06:37). Nothing recorded before 06:30 was retracted; the candidate count is unchanged at 6
distinct symbols.

**candidates: 6 distinct symbols across 9 lines in candidates.jsonl. Synthesis must take the
LAST line per symbol** — BJ has three (the final one is conviction 4, size 2%) and XLV has two
(the final one carries the breadth evidence; conviction 3 in both).

| symbol | dir | conv | size | entry | target | stop | R:R | win_prob |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BJ | buy | 4 | 2% | 113.60 (breakout >113.35) | 126.00 | 107.40 | 2.00 | 0.40 |
| XLV | buy | 3 | 3% | 183.50 (zone 182.00-184.00) | 203.50 | 174.50 | 2.22 | 0.42 |
| TLT | sell | 3 | - | 79.38 at market | CLOSE | - | - | - |
| BCC | sell | 3 | - | 66.37 at market | CLOSE | - | - | - |
| ACM | sell | 4 | - | 72.50 at market | CLOSE | - | - | - |
| ONON | sell | 4 | - | 32.76 at market | CLOSE | - | - | - |

Conviction equals the distinct-evidence-kind count on every line: 2 kinds -> 3, 3 kinds -> 4.
No line claims 5. Two upgrades were available on the arithmetic and both were declined (BJ at
06:34, XLV at 06:37) — reasons recorded at each.

- **All 14 open positions reviewed and decided.** 4 closes above; HOLD with levels unchanged
  on RTX, KHC, OXY, AAL, UNP, ABT, PYPL, XLU, HII, PFE, each with its reason recorded at
  06:22. None re-pitched, because none had new information.
- **The caveat synthesis must carry into data_quality_notes:** BJ and XLV are the same bet.
  Both are the long side of one real-rate-shock rotation (06:25) and all four closes are exits
  from its wrong side. Six symbols is not six drivers. If tonight's NVDA print reignites risk
  appetite and the 10Y falls, both new ideas lose together.
- **NVDA reports tonight 11/17 AMC with an interim CEO who is also the CFO, no named successor
  and a live reinstatement campaign.** Deliberately no position either way (06:04, 06:05).
- **Ideas rejected, with the reason, so synthesis does not re-litigate them:** TJX/ROST both
  ways (no sourced 2026 driver), SLV short (chasing a new low; same driver as GLD), GLD
  re-pitch (needs a 3.7% rally to engage, no new information), /MBT short (view was right,
  entry never filled, no new information), XLF long (KRE divergence unresolved), XLP long
  (third unit of one driver; stretched target), BRBR (three misses in four quarters,
  deteriorating revisions), JJSF (target had to be stretched to +17.8% to clear the floor),
  IESC and ROAD (-59% and -39% with 8-10% ATRs, no researched reason), NGVC (advol $2.9M),
  BABA both ways (four straight misses but no non-chasing short entry), FRO/NAT/SBLK/DSX/ZIM
  (four of five below both MAs, the fifth trendless).
- **coverage gaps:** no long_term idea — no defensible valuation anchor was built and inventing
  one would breach rule 2 (06:30); no event contracts — the Kalshi feed returned only sports
  parlays (06:05); no options-implied move on any idea — yahoo options returns HTTP 401
  (06:12); no VIX, no overnight index futures, no DXY (06:02); no intraday idea, because every
  equity price available at 06:00 ET is the previous close and today's only dated intraday
  catalysts are the HD and DIS prints landing with this report; no orthogonal-driver idea,
  searched for twice (BABA, shipping) and not found.
- **sources that failed:** yahoo — HTTP 429 on ^GSPC/^NDX/^DJI/^RUT/^VIX/ES/NQ/DXY/gold/WTI
  and HTTP 401 on the options endpoint; finnhub — refuses index CFDs ("subscription required");
  stooq — 404 on indices; alphavantage — no api key; api.nasdaq.com — ReadTimeout on
  `short BJ`, so no short-interest reading on any idea; Kalshi events — count=0 for Nvidia,
  Fed, inflation, CPI, recession and bitcoin; `history BTC-USD` — ok:false, IBIT used as the
  daily-level proxy. coingecko failed inside the macro call but succeeded on a direct retry.
- **prices:** every equity and ETF figure in this file is the **2026-11-16 16:00 ET close**,
  fetched this morning with market_session=pre and age_minutes ~842. That is a closed market,
  not stale data. Crypto figures are live. Run started 06:01 ET and finished research 06:40 —
  on schedule, not truncated, no late-run stamp applies.
