# Research log — 2026-09-17

## [06:03 ET] MACRO — rates, and a broken quote layer
- FRED 2026-09-15: US10Y **5.00%**, US2Y **4.67%**, effective fed funds **3.63%**, 10y-2y **+0.27** (2026-09-16). Unemployment 4.1% (Aug). — source: https://fred.stlouisfed.org/
- The shape is the story: funds at 3.63% against a 5.00% 10y is a ~137bp gap. The Fed has cut into a long end that refuses to follow — a bear steepener. Term premium / fiscal supply, not growth optimism.
- TLT 80.88 (prev close 80.71, +0.21%), asof 2026-09-16T20:00Z. Confirms the long end near its lows.
- **DATA GAP:** Yahoo returned HTTP 429 across the board. SPX, NDX, DJI, RUT, VIX, /ES, /NQ, DXY, US10Y quote, gold, WTI **all failed**. Finnhub refuses indices ("subscription required for CFD indices"). Stooq 404s on ^-prefixed symbols. CoinGecko crypto prices also failed this call.
- Consequence: no index level, no VIX, no dollar today unless the rate limit clears. Do not state one from memory. Retry later; use ETF proxies (SPY/QQQ/IWM/GLD/USO/UUP) which route through a different symbol path.

## [06:08 ET] LEVELS — open-position board (all prices = 2026-09-16 close, market closed, via nasdaq/finnhub)
| Sym | Close | ATR14 | ATR% | SMA20 | SMA50 | SMA200 | % off 200d high |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 754.05 | 6.48 | 0.86 | 764.67 | 759.19 | 715.49 | -3.25 |
| DVN | 48.44 | 1.379 | 2.85 | 48.68 | 45.98 | 44.00 | -8.1 |
| DINO | 113.97 | 4.222 | 3.70 | 102.73 | 93.53 | 67.60 | **-0.71** |
| GLD | 391.74 | 8.178 | 2.09 | 408.10 | 392.04 | 416.13 | -23.14 |
| CCJ | 90.90 | 3.600 | 3.96 | 99.18 | 94.91 | 105.78 | -32.79 |
| CEG | 259.53 | 10.393 | 4.00 | 279.36 | 270.71 | 293.87 | -31.84 |
| LULU | 95.98 | 5.692 | 5.93 | 111.18 | 116.04 | 150.28 | -57.53 |
| NKE | 35.78 | 0.869 | 2.43 | 38.47 | 40.73 | 50.51 | -48.25 |
| PFE | 27.46 | 0.529 | 1.93 | 28.09 | 26.48 | 26.25 | -5.99 |
| BCC | 75.31 | 2.183 | 2.90 | 78.22 | 78.91 | 77.26 | -18.11 |
| LCII | 87.11 | 3.246 | 3.73 | 99.24 | 102.71 | 117.34 | -45.44 |
| EEM | 65.72 | 0.943 | 1.43 | 67.09 | 65.83 | 62.21 | -8.17 |
| SVRA | 5.13 | 0.198 | 3.87 | 5.42 | 5.54 | 5.60 | -26.77 |
| TLT | 80.88 | 0.662 | 0.82 | 82.07 | 82.73 | 85.95 | -10.98 |

**The honest read of this board:** 11 of 14 sit below their 20- AND 50-day. LULU (95.98 vs 200d-low 95.67), NKE (35.78 vs 35.76) and TLT (80.88 vs 80.46) are each making new 200-day lows *today*. The only two things working are the **SPY short** and **DINO**. That is not a coincidence — it says the book is long a basket of falling knives into a tape that is de-rating them, and the track record (0/6 to target, avg -3.9%) is that fact already scored.
- Bar for a NEW long today is therefore raised: it must be something the tape is *already* rewarding, or a genuinely structural long_term case, not another de-rated name bought because it looks cheap.

## [06:09 ET] REJECTED — event contract lane — Kalshi search returned count=0 for "CPI", "rate", "FEDDECISION", "Fed decision", "recession"; the one "Fed" hit was a garbage cross-category sports market. No priceable event contract sourced this run.

## [06:14 ET] MACRO — THE DAY'S DRIVER: the Fed hiked yesterday
This is the single fact that reframes every idea below. Yesterday, 2026-09-16 14:00 ET:
- FOMC **raised** the target range 25bp to **3.75%-4.00%** — the **first hike since 2023**, and the vote was **unanimous**. — source: https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html
- Dot plot: the median official sees **at least one more hike in 2026**; reported distribution for 2027 was 8 for another hike, 6 hold, 4 cuts. — source: https://finance.yahoo.com/markets/stocks/articles/stock-market-today-sept-16-133949098.html
- Chair **Kevin Warsh**: inflation has been "too high ... for too long"; "We must be confident that underlying inflation is moving to our objective clearly and at sufficient speed... Today, the FOMC decided that this standard has not been satisfied." Stocks turned lower *during* the presser, not on the statement.
- **10-year closed ~5.01%, the highest since 2007** (low of 4.94% intraday before reversing up). Long end led. — source: https://finance.yahoo.com/markets/live/stock-market-today-wednesday-september-16-dow-sp-500-nasdaq-fed-meeting-decision-080356525.html
- Tape: Dow **-1.2%**, S&P 500 **-0.4%**, Nasdaq ~flat. Selling was concentrated in the rate-sensitive/value side of the index, not in tech.
- Reported overnight: **futures rose** after the sell-off. — source: https://www.cnbc.com/2026/09/16/stock-market-today-live-updates.html

**What this does to the book.** It explains the whole losing board above in one line: this report has been long duration-ish, rate-sensitive, de-rated value (CCJ, CEG, LCII, BCC, NKE, LULU, PFE) and long gold, into a Fed that has turned from cutting to hiking. Effective funds was 3.63% on 09-15 against a 5.00% 10y; the curve is +0.27 and the hiking cycle restarting pushes the *front* end up into it.
- Implication 1: the SPY short is the position most confirmed by yesterday, not the one to take profit on reflexively.
- Implication 2: **do not add new long-duration or rate-sensitive longs today.** That is the exact trade that produced 0/6.
- Implication 3: GLD long is now fighting rising real rates. It is also already -23% off its high and sitting exactly on its 50-day (392.04 vs 391.74 close). That level is the whole argument.
- Implication 4: a *hawkish* hike is genuinely two-sided for the long end — credible inflation-fighting can pull the 10y down even as the front end rises. Yesterday it did not. Respect that this is the main counter-argument to any short-duration idea.

## [06:15 ET] NEWS — DVN -5.63% yesterday (open position, opened 2026-09-11 @ 49.60)
- Closed 48.44 from 51.33. Partly mechanical: DVN went **ex-dividend $0.32 on 2026-09-15**, which is ~0.6% of the 5.6% — the other ~5% is real. — source: https://investors.devonenergy.com/investors/stock-information/default.aspx
- No company-specific news surfaced. The move is consistent with the broad Fed-day de-rating of cyclicals/value (Dow -1.2%).
- Level check: close 48.44 sits exactly on the 20-day (48.68); 50-day 45.98; stop 46.90 is 1.12 ATR below the close — **too tight to still be honest** on a 2.85% ATR name. Decision logged below.

## [06:11 ET] NEWS — housing: the FOMC and LEN landed on the same night
- LEN Q3 (2026-09-16 AMC) **missed**: EPS $1.19 (adj $1.23) vs $1.29 consensus; revenue **$8.05B vs $8.32B** expected. Home-sales gross margin guided ~16% on aggressive incentives. — source: https://www.dailypolitical.com/2026/09/16/lennar-nyselen-releases-quarterly-earnings-results-misses-expectations-by-0-05-eps.html
- Housing complex closes 2026-09-16: ITB 88.12 (-23.6% off high, ATR 2.043, SMA20 93.63, 200d low 84.98), XHB 96.80, LEN 78.36 (-41.4% off high), DHI 138.32, KBH 48.67 (-28.0% off high). All below their 20/50/200-day.
- ITB traded 90.11 high / 87.49 low on 09-16, so yesterday's published 90.00-91.60 short zone was touched intraday; treat that position as possibly filled and do not re-cut its entry.
- KBH Q3 is **2026-09-22 AMC** (est EPS 0.9022, rev $1.307B) — confirmed on the fetched Finnhub calendar.

## [06:12 ET] CORRELATION BUDGET — the "rates up" driver is already full
Per config/strategy.md the cap is **3 ideas on one driver**. Against the hike, the book already carries: the XLU short and the ITB short (both published 2026-09-16), the standing TLT exit, and now the CEG exit. That is at or past the cap on a single macro bet.
- So the right response to the most confirmed macro view of the day is **not to add another rates-up short**. KBH short into 09-22, XHB short, a bond short — all rejected below on correlation grounds, not on merit.
- Research time redirected to drivers that are genuinely independent: refined-product supply, the dollar, crypto, and the long_term lane.

## [06:13 ET] REJECTED — VLO / PSX / MPC (refining longs) — right driver, wrong entry
- The driver is real and is **not** the rate trade: NY Harbor ULSD crack vs WTI hit **$107.35 on 2026-09-01**; the WTI 3-2-1 crack is near **$59/bbl** against a 2010-2021 average of about **$19**. Cause is a refined-*product* shortage, not crude: >7M bpd of Middle Eastern and Russian product flows offline, global refinery throughput 4.2M bpd below last year. — source: https://oilprice.com/Energy/Crude-Oil/Global-Fuel-Squeeze-Triggers-US-Refiners-Stocks-Rally.html and https://www.forbes.com/sites/garthfriesen/2026/07/23/refining-stocks-soar-as-crack-spread-hits-record-high-in-2026/
- But the entry is indefensible. VLO 403.28 is **-0.98%** off its 200-day high after a ~143% 12-month total return; PSX 264.63 is -1.0% off; DINO 113.97 is -0.71% off. Buying a record crack spread at a record share price is buying the peak of a mean-reverting series.
- CNBC flagged exactly this on 2026-08-17: "Refiner stocks are on a nearly unprecedented run. History says it could end soon." — source: https://www.cnbc.com/2026/08/17/refiner-stocks-are-on-a-nearly-unprecedented-run-history-says-it-could-end-soon.html
- **No new refining long.** The report already owns this driver through DINO opened 2026-08-22 at 107.50, which is the position to hold, not to double.

## [06:15 ET] CALENDAR — today, 2026-09-17, all at 08:30 ET
- **Initial jobless claims** — consensus 211K, +2K.
- **Philadelphia Fed manufacturing survey** — consensus **25.0 vs 41.4 prior**, a large expected deceleration.
- **New Residential Construction (housing starts / permits)**.
— source: https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar
- All three land the morning after a hawkish hike, so today's tape is a referendum on whether the Fed is tightening into a slowing economy. Housing starts in particular is the read-across to the already-published ITB short; it needs no new idea from me.

## [06:16 ET] NEWS — GNRC: an 8-K worth reading in full (captured, conviction 4)
- Generac and Amazon executed a long-term supply agreement **2026-09-16** for **up to $8B** of backup power generators for Amazon data centers. Initial deliveries specified at **$2.4B across 2027 and 2028**.
- Equity-linked: warrant over **1,693,745 shares at $200.9266**, expiring **2033-09-16**; **307,954 vested immediately**, remainder vesting in tranches on aggregate gross payments up to $8B. No exclusivity or termination terms disclosed. — source: https://www.sec.gov/Archives/edgar/data/0001474735/000143774926030550/gnrc20260915_8k.htm
- GNRC closed **175.11** (-40.9% off its 200-day high of 296.44, under SMA50 204.56 and SMA200 209.78), then traded ~**240.80** after hours, about **+37.5%**.
- Analysts pre-deal: 10 strong buy / 11 buy / 7 hold / 0 sell, 75.0% bullish and improving (+4.6pp over four months) — fetched, not remembered.
- **Venue check:** GNRC is NYSE-listed common stock, so `Robinhood Stocks`, no margin needed for the long. Not an OTC/warrant/foreign-ordinary problem.
- Entry deliberately set at 205-218 rather than at the open. The universe rule on >40% prior-session moves is engaged here and the disclosure is explicit: the move IS the thesis, and the risk spelled out is that a 4.51% ATR computed before the gap understates today's true volatility.

## [06:17 ET] TENSION LOGGED — closing CEG while buying GNRC
Both are "datacenter power demand". Stating the distinction rather than hiding it, because the red team should get to judge it:
- CEG is a capital-intensive IPP whose cash flows are long-duration and discounted at the rate the Fed just raised; it is a component of XLU, which this report is already short; and it has **no dated catalyst** — it is 3.7% above its stop waiting for one.
- GNRC is short-cycle equipment with a **signed contract and a delivery schedule in 2027-2028**, and it sits in industrials, not utilities.
- The honest summary: I am not abandoning the datacenter-power driver, I am moving from the leg of it that is a rate-discounted promise to the leg that has a filing behind it. If the red team disagrees, the CEG exit is the weaker of the two calls and should go first.

## [06:18 ET] MACRO SYNTHESIS — why energy and the hike are the same story
Crude is not soft, which changes the read on the whole tape: USO 156.17 (**-4.4%** off its 200-day high, SMA200 110.45), BNO 61.71 (-3.6% off high, SMA200 44.09), XOP 191.80 (-4.5% off high, above all SMAs). Crude has roughly doubled versus its own 200-day average.
- So the inflation Warsh says has been "too high for too long" has a large energy component, and the Fed is hiking into it. Energy leadership and the hike are **one** story, not two, and that is why energy is the only sector on the board that is working.
- Consequence for idea selection: energy longs are the coherent hedge to the rate view, not a contradiction of it.

## [06:19 ET] POSITION UPDATE — DVN — close; DINO — hold (both captured)
- Fetched relative strength settles it. DVN vs XLE: **-0.49% (1m), -2.72% (3m)**; DVN vs SPY -10.26% (6m). DINO vs XLE: **+17.66% (1m), +55.52% (3m)**, 95.05% absolute over 6m.
- DVN levels never worked: the 55.50 target is **above** the fetched 200-day range high of **52.71**, and the 46.90 stop is **1.96 ATR** from the 49.60 entry — under the 2.0 swing floor. Target needing a one-year breakout + stop inside the noise = the shape config/strategy.md says has already failed this report ten times. Exit.
- DINO held unamended: stop already 2.31 ATR from entry, so risk is defined. Explicitly **not** raising the stop — that is the KRE mistake.

## [06:20 ET] POSITION UPDATE — SPY short — the 750 target traded; not re-pitching
- SPY 2026-09-16 bar: open 759.50, high 761.67, **low 749.60**, close 754.05. The short opened 2026-08-31 at 773.00 carried a 750.00 target, and **749.60 < 750.00**, so the target printed intraday. `grade_position` reads levels per bar and should close this at target (+2.97%) without my help; I am not publishing a duplicate recommendation that would muddy the row.
- **Not opening a new SPY short.** SPY has been recommended 4x in the last 10 days, it closed back above the low at 754.05, futures were reported higher overnight, and the 200-day is far below at 715.49. Re-shorting here would be the anchoring the prior-context guard exists to catch, not conviction.

## [06:21 ET] CORRELATION BUDGET — recount, because exits do not consume it
Re-examined the cap. An instruction to **close** a position removes exposure rather than adding it, so the CEG, GLD, DVN and TLT exits do not spend correlation budget. The ideas actually carrying rates-up risk are the **XLU short and the ITB short** (both published 2026-09-16). That is 2 of 3, so there is room for exactly one more rates-linked idea — and it should be a **long**, because the book is now heavily net-short/flat and a fourth short expression would make the report one trade.

## [06:23 ET] REJECTED — MET / EQH / life insurers — right driver, fails the floor on arithmetic
Spent real time here because it is the one *long* that fits a hiking Fed: an annuity writer's portfolio rolling from legacy ~3% coupons into 5%+ reinvestment is a durable multi-year earnings uplift, not a mean-reverting spread. The sector is also the only long lane holding up — MET 97.23 (-3.67% off high, above SMA20 96.27 / SMA50 95.58 / SMA200 82.71), EQH 53.88 (-1.67% off high), VOYA 100.28, all above their 200-day in a tape where almost nothing is.
- MET fundamentals are genuinely good: adjusted ROE **17%** in Q1 2026 against a 15-17% target; total investment spread **119bps at the top of the 100-120bps guided range**; FY2025 BVPS $39.02 (+14%), adjusted BVPS $57.07; **four consecutive EPS beats** (2.43/2.32, 2.42/2.29, 2.58/2.37, 2.37/2.34); 70.8% of analysts bullish and improving, zero sells. — source: https://www.sec.gov/Archives/edgar/data/1099219/000109921926000008/ex991earningsreleasetables.htm
- **It still fails.** Long_term floor is 2.5 against a priced bear case. Trailing adjusted EPS ~$9.80, so 97.23 is ~9.9x. Target at 12x on ~$10.40 forward = **124**. Bear case — core spread compressing from 95bps, credit losses — ~$8.60 EPS at 9x = **77.40**. From a 96 accumulation: (124-96)/(96-77.40) = **1.51**. Nowhere near 2.5.
- Tried it as a swing instead: ATR 1.875, so a 2.0 ATR stop is 3.75 wide, and a 2.0 R:R target from 97.23 lands at 104.89 — **above the 200-day high of 100.93**. Same defect I just closed DVN for. Refused to reverse-engineer either leg.
- EQH separately disqualified on its own data: analyst revisions **deteriorating (-5.8pp)** and **30 insider sells worth $14.06M with zero open-market buys** over six months.
- Logged in full because the work is the point: the driver was right and the price was not, and config/strategy.md says publish fewer rather than force it.

## [06:24 ET] POSITION UPDATE — PFE — continue accumulating, and give it the invalidation it never had (captured, long_term, conviction 4)
This was the **last open long in the book with neither a stop nor a stated invalidation** — a real risk-control gap, now closed with a named condition rather than a price.
- **Insider buying is the find of the day.** Fetched: 3 open-market buys, 3 distinct buyers, **$2.96M bought vs $0.13M sold** over six months. **CEO Albert Bourla bought 38,000 shares at $26.34 on 2026-08-12.**
- Guidance reaffirmed FY2026: revenue $59.5-62.5B, **adjusted EPS $2.80-3.00** → 27.46 is **9.2-9.8x** with a ~6% dividend. — source: https://www.tikr.com/blog/pfizer-raises-2026-revenue-guidance-to-62-billion-heres-whats-behind-the-beat
- Cliff quantified: LOE erodes ~$1.5B (2026), $4.5B (2027), **$6B+ (2028)**, ~$17-18B cumulative. Offsets: ~20 Phase 3 oncology programs (Seagen, $43B) and Metsera obesity — 10 pivotal studies in 2026, first approval targeted 2028. Company guides high-single-digit revenue CAGR from 2029.
- Beat consensus **all four** of the last four quarters (0.77/0.69, 0.75/0.72, 0.66/0.58, 0.87/0.64) while only 38.9% of analysts are bullish and revisions are **deteriorating (-2.8pp)**. That disagreement is the idea.
- **Ratio sensitivity published on purpose:** target 42 (12.5x on ~$3.40), bear case **22.00** → R:R **2.66**, clears the 2.5 long_term floor. At a **20.00** bear case (dividend cut) it is **1.95** and **fails**. The red team should attack that assumption, not a single flattering number.
- Relative strength: PFE vs XLV +1.77% (1m) but -4.25% (3m) and -12.08% (6m) — recently turning, not yet leadership. Noted as a weakness, which is why conviction is 4 and not 5.

## [06:25 ET] REJECTED — AZO — closed 2849.04, the exact low of the session AND its 200-day low, 3 sessions before Q4 earnings (2026-09-22 BMO, confirmed on the fetched calendar). -28.7% off its high, below SMA20/50/200. Mixed surprise record (2 beats, 2 larger misses). 81.2% of analysts bullish with **zero sell ratings** into a 28.7% drawdown is downgrade fuel, not support. Long is a knife into a binary; short is a coin flip on a print. Neither clears.

## [06:26 ET] REJECTED — COST — -18.5% off high, below all SMAs, revisions **deteriorating (-3.0pp)**, missed 3 of the last 4 quarters. A genuine de-rating, but earnings 2026-09-24 make it binary and it is the same consumer-weakness driver already represented; shorting a compounder into a print is not an edge.

## [06:27 ET] POSITION UPDATE — EEM — hold, no publication
EEM 65.72 vs the 65.60 entry, essentially flat, stop 63.00 sitting **3.05 ATR** below (ATR 0.943). The dollar is a genuine headwind — UUP 28.40 is only 0.7% off its 200-day high and above its 20/50/200-day — and EEM has slipped under its SMA20 (67.09) and SMA50 (65.83). But it remains well above its SMA200 (62.21) and the stop is wide, defined and doing its job. Nothing to amend; publishing a "hold, unchanged" here would be noise. Revisit if 65.00 breaks.

## [06:28 ET] NOT RE-PITCHED — CCJ — the 2026-09-16 report said in terms: "do not re-pitch this name again without new primary evidence." I found none today. CCJ closed 90.90, -32.8% off its high and below all three moving averages, with the 82.50 stop intact from that same update. Holding under the existing stop. Recording the restraint rather than quietly dropping it.

## [06:26 ET] NOTE ON TIMESTAMPS
Earlier headings in this file drifted ahead of the wall clock — I was estimating elapsed time instead of reading it. The `date` calls are the truth: this run started **06:01 ET**. Entries from here carry real clock times. The finding content is unaffected; flagging it rather than quietly editing the file, since `reports/` is a record.

## [06:26 ET] FALSIFICATION — CEG re-captured after actually hunting the bull case
Went looking for the case against my own exit and found a real one, so the candidate was rewritten rather than left one-sided:
- The deals **are** landing: long-term agreements with **Microsoft, Meta and CyrusOne**, plus an additional **920 MW** of 15-20 year PPAs with investment-grade customers; and on **2026-09-10 CEG agreed to acquire Risec from Shell for $715M**, described as accretive. The published sell-side framing is literally "buy the pullback before data center deals arrive." — source: https://seekingalpha.com/article/4910051-constellation-energy-buy-the-pullback-before-data-center-deals-arrive
- Relative strength **refuses to convict it**: CEG vs XLU is **-0.24% (1m), +5.14% (3m)**. It is performing in line with its sector, not lagging. That is weaker support for an exit than I expected, and it is recorded in the evidence as evidence *against* the idea.
- The exit still stands, on one argument only: those PPAs **begin 2029-2032**, the longest-duration cash flow on the board on the day the discount rate turned, and the report **cannot coherently be short XLU while long an XLU component**. The candidate now says explicitly: if the red team prefers the CEG long, it must cut the XLU short instead. Do not keep both.
- Stock fell on **deal delays and a weak outlook**, not on a broken thesis. — source: https://www.tradingview.com/news/invezz:e5416c5b5094b:0-constellation-stock-falls-as-weak-outlook-deal-delays-dent-sentiment/

## [06:27 ET] STRUCTURAL FINDING — why today produced so few new-money longs
Worth stating because it explains the shape of the report rather than excusing it. Config requires a swing stop of **>=2.0 ATR** (1.8 ETF) **and** a reward-to-risk of **>=2.0**. Together those mechanically demand a target at least **~4 ATR** away. In today's tape the names that are *working* are all within 4 ATR of their 200-day highs, so the target has to be printed above the 52-week high to clear the floor — which is precisely the defect I closed DVN for. Worked examples, all rejected on this arithmetic and not on the story:
- **XOM** 163.32 (ATR 3.89): a 2.06 ATR stop at 154.00 forces a 178.00 target, above the 200-day high of **176.41**. At a defensible 176.00 target the ratio is **1.75** — fails.
- **MET** 97.23 (ATR 1.875): 2.0 ATR stop → 104.89 target, above the 200-day high of **100.93**. Fails.
- **VLO / PSX / DINO**: 0.7-1.0% off their highs; there is no room at all.
The rule is doing its job. A tape where leadership sits on its highs and everything else is falling simply does not offer many honest swing longs, and the correct response is to publish fewer rather than to print a target above the 52-week high and call it a plan. **GNRC clears precisely because the 37.5% after-hours gap opened a genuine 46-point gap between a 212 pullback entry and a 258 target against 16 points of risk** — the geometry exists there and nowhere else I looked today.

## [06:29 ET] NEWS — JBHT warned, and it is the refining trade seen from the other side (captured, conviction 4)
- **J.B. Hunt warned on 2026-09-16 that Q3 earnings will fall 5-10%**, naming **surging diesel prices** and driver compensation outpacing pricing; commentary came around the Morgan Stanley Laguna Conference on 09-15 (CFO Brad Delco, Intermodal President Darren Field). — source: https://www.cnbc.com/2026/09/16/jb-hunt-stock-jbht-earnings.html
- Verified in the tape, not just the headline: gapped from a **273.05** close to a **242.885** open, closed **236.73** on **4.81M shares against ~850K typical (5.7x)**, closing **below its 200-day (240.94)**.
- **Why this is not a fourth rates-up short.** The stated cause is diesel, and diesel is the same variable behind today's refining research — ULSD vs WTI at $107.35, the 3-2-1 near $59/bbl versus a ~$19 average. Refiners capture that spread; intermodal carriers pay it, with a lag because contract resets trail spot. If the Fed pivots dovish tomorrow, the XLU and ITB shorts suffer and this one does not necessarily — different driver, and that is the test the correlation cap actually asks.
- Q3 print confirmed on the fetched calendar: **2026-10-13 AMC, consensus EPS 2.1835**.
- **DATA GAP:** `market_data.py short JBHT` timed out against api.nasdaq.com (also failed for GNRC). I do **not** know how crowded this short is, which is the single most relevant positioning fact for a short after a 13% drop. Size held to 2% and the gap is stated in `key_risk` rather than papered over.

## [06:30 ET] CONCENTRATION CHECK — DINO long and JBHT short share one variable
Flagging deliberately: both positions pay off if **diesel crack spreads stay wide**, and both lose if cracks normalise. That is 2 of the permitted 3 on a single driver, and it is a *coherent* pair rather than an accidental one — but it is concentration, not diversification, and a reader should know that DINO and the JBHT short are closer to one trade than two. No third crack-spread idea may be added.
Current live risk-adding ideas by driver: **rates-up** — XLU short, ITB short (2 of 3, both published 09-16); **diesel cracks** — DINO long, JBHT short (2 of 3); **datacenter power** — GNRC long (1); **pharma re-rating** — PFE (1); **single-asset FDA binary** — SVRA (1).

## [06:31 ET] RESEARCH COMPLETE
- **candidates: 9 lines, 8 unique symbols** (CEG captured twice; the second entry supersedes after the falsification pass).
  - New money: **GNRC** buy (conv 4, R:R 2.88), **JBHT** sell_short (conv 4, R:R 2.08)
  - Continue/hold: **DINO** buy (conv 4, R:R 2.10), **PFE** long_term buy (conv 4, R:R 2.66 vs a 22.00 bear case), **SVRA** buy (conv 3, R:R 3.53)
  - Exits: **CEG**, **GLD**, **DVN** (all conv 4, size 0, closing positions)
- Audited before writing this block: every stop clears its ATR floor (GNRC 2.03, DINO 2.31, SVRA 3.78, JBHT 2.55 — all above the 2.0 stock floor); every ratio clears its horizon floor; every claimed win probability sits 11-16 points above its `1/(1+R:R)` baseline, none above the 20-point "large claim" line; conviction equals the count of distinct evidence kinds on every idea.
- **The day in one line:** the Fed hiked for the first time since 2023 and the book was positioned for the opposite, so three longs are closed, the two that fit the new regime are held, and only two new positions are opened.
- **Deliberate skew, stated rather than apologised for:** nothing intraday, no futures, no crypto and no event contracts today. Three of those are judgement (no intraday setup cleared; no futures view I could express better than the cash leg; crypto had no catalyst I could source), and one is a data failure (event contracts, below).
- **Coverage gaps and failed sources:**
  - **Event contracts — lane unusable.** Kalshi returned `count: 0` for CPI, rate, FEDDECISION, Fed decision, recession, Bitcoin, S&P, inflation, GDP and unemployment; an unfiltered call returned 40 markets that were cross-category sports parlays with **null prices on every leg**. No event contract could be priced, so none was recommended.
  - **Index and macro quotes — Yahoo HTTP 429 all run.** SPX, NDX, DJI, RUT, VIX, /ES, /NQ, DXY, the 10y quote, gold and WTI all failed; Finnhub refuses indices outright. Worked around with ETF proxies (SPY, QQQ, IWM, UUP, GLD, USO) and FRED, which is why every index figure in this report is quoted as an ETF or a FRED series and never as an index level.
  - **Short interest — api.nasdaq.com read timeouts** on both GNRC and JBHT. Material for JBHT specifically and disclosed in that idea's `key_risk`.
  - Not reached at all: small/micro-cap screening beyond the open SVRA position, and the crypto lane beyond spot prices (BTC 76,355 +0.53%, ETH 2,434.76 +1.36%, SOL 99.89 +2.8%; IBIT 43.04 sits above both its 50-day 39.35 and 200-day 42.16, a divergence from the hike worth a look tomorrow that I could not source a catalyst for today).
- **All prices in this file are the 2026-09-16 close** (asof 20:00 UTC) unless stated. At 06:00 ET with the market shut that is the freshest honest equity price, not stale data.

## [06:34 ET] REJECTED — crypto long (BTC / IBIT) — divergence explained, but no defensible edge and no fetchable levels
Chased down the one thing I had flagged as unexplained, and it resolves into a rejection rather than an idea. Recording it because the gap in the block above is now closed.
- **The divergence is real and has a cause.** Spot bitcoin ETFs took **$3.52B of net inflows in August across 16 of 21 trading days**, BTC's best month since November 2024 (+25%); the week ending 2026-09-05 added **$986.9M**, a three-week total of **$3.8B** — the strongest sustained streak of 2026 — including ~**$731M on 2026-09-04**, the largest single day since January 14. Institutional demand, not retail momentum, is what held the price against a hawkish macro. — source: https://crypto.news/fed-rate-hike-september-crypto-thesis-etf-demand/
- The hike was also **~87% priced** going in, so "event risk clears" is not the fresh catalyst it would otherwise be. — source: https://usethebitcoin.com/bitcoin/bitcoin-price-september-13-2026/
- **Why it still fails.** The dot plot points to **at least one more hike in 2026**, so the headwind is extended rather than removed — the opposite of the "overhang cleared" setup this would need. And the actual post-hike reaction was **+0.53% over 24h** on BTC, which is resilience, not confirmation. Buying on "flows beat the Fed" would be asserting an edge from flow data that is already ~2 weeks stale.
- **Second, independent blocker: I could not fetch BTC's own price history.** `history BTC-USD` failed on every source (nasdaq no rows, Yahoo 429, no API keys for twelvedata/alphavantage, stooq no rows), so I have **no BTC ATR and no BTC swing levels**. Crypto carries a 2.5 ATR swing floor and I will not infer that from an ETF proxy and publish it as a bitcoin level.
- Levels I **can** stand behind, recorded for tomorrow: spot BTC **76,355** (+0.53% 24h), ETH **2,434.76** (+1.36%), SOL **99.89** (+2.8%) from CoinGecko; **IBIT 43.04**, ATR 1.4157 (3.29%), SMA50 39.35, SMA200 42.16, 200-day range 32.84-55.60. IBIT sitting above both its 50- and 200-day is the part worth re-checking once there is a catalyst to hang it on.

## [06:35 ET] AMENDMENT TO RESEARCH COMPLETE
The gap list above said the crypto lane was "not reached". It has now been reached and **deliberately rejected** — see the entry immediately above. Everything else in that block stands: **9 candidate lines, 8 unique symbols**, two of them new money (GNRC, JBHT), three continuations (DINO, PFE, SVRA), three exits (CEG, GLD, DVN). Final research time 06:01-06:35 ET.
