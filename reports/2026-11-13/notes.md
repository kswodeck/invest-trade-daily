# Research log — 2026-11-13

## [06:03 ET] MACRO — regime: term premium shock, gold unwind, small caps weak
Prices are 2026-11-12 US close (session=pre at 06:03 ET; freshest honest equity price).
- US 10Y 4.98% (FRED 2026-11-10), US 2Y 4.73%, fed funds eff 3.88%, 10y-2y +0.24 — source: https://fred.stlouisfed.org/series/DGS10
- TLT 79.72, **-1.48%** on the day, closed at the low of day (79.72 = low). Long bond breaking down. — source: market_data.py quote
- GLD 354.89, **-2.82%** — large one-day gold unwind alongside higher real rates.
- IWM 278.44 -1.64%; SPY 757.12 -0.35%; QQQ 688.17 -0.32%. Small caps underperforming large by ~1.3pp.
- Read: this is a rates-up / duration-down day, not a growth scare (QQQ outperformed IWM). Anything long duration (TLT, gold, small caps, utilities) is fighting the tape today.
- DATA GAP: Yahoo endpoints 429 rate-limited this run; ^GSPC/^VIX/^DXY/^TNX/futures/crypto via macro all FAILED. Finnhub works for US equities/ETFs. Will use ETF proxies (SPY/QQQ/IWM/TLT/GLD/UUP) instead of indices.

## [06:06 ET] CALENDAR — dated catalysts inside 10 sessions (fetched, finnhub)
- **ACM Q4 earnings 2026-11-16 amc** — this is an OPEN POSITION (opened 11/07 @66.74, now 70.25 +5.3%). Only open position with earnings inside the horizon. Requires a decision today.
- NVDA Q3 2026-11-17 amc — the single largest event of the window. NVDA was stopped out 2026-11-10; do not re-pitch into the print.
- DIS 11/17 bmo, HD 11/17 bmo
- Retail week: LOW/TGT/TJX/ROST/GAP/BBWI 11/18, WMT 11/19 bmo, BJ 11/20
- PANW 11/18 amc, INTU 11/19 amc, KEYS 11/19 amc
- China ADRs: PDD 11/16, BIDU 11/16, XPEV 11/16, BABA 11/19, NTES 11/19
- 11/23-25: DKS, BURL, ANF, KSS, URBN, HPE, ZM, A, J | ADI, ADSK, BBY, DELL, HPQ, MDT, WDAY | DE 11/25
- No earnings in the window for BCC, PFE, KHC, OXY, AAL, HII, UNP, ABT, PYPL, SMMT, RTX, XLU, ONON.

## [06:05 ET] POSITION UPDATE — ACM — opened 2026-11-07 @66.74, now 70.11, +5.0%
- decision: **HOLD, TRIM HALF BY MONDAY'S CLOSE (2026-11-16)**, stop unchanged at 61.50
- why: Q4 earnings 2026-11-16 amc (fetched finnhub calendar). Structure intact (above rising SMA20 64.146, SMA50 62.502) but 11/12 printed a reversal bar 73.20 high → 70.11 close on 1.42M shares. The 2026-06-30 quarter missed by -133.8% (actual -0.50 vs est 1.4809), so this name does gap on prints.
- stop NOT tightened on purpose: 61.50 is 2.41 ATR (ATR14 2.1777) and sits under the 10/28 low 61.19 + SMA50. Walking it in to improve R:R is the KRE anti-pattern.
- insiders: 3 distinct open-market buyers, $699,391, zero sells/6mo — Rudd 4,225@71.02, Kapoor 1,420@71.12 (both 5/14), Poloni 4,224@70.63 (6/16). Note they are flat on it at 70.11.
- analysts DETERIORATING: bullish share 83.3% (Aug) → 76.5% (Nov); one buy → hold.
- action: captured via add_candidate.py

## [06:06 ET] POSITION UPDATE — SMMT — opened 2026-10-27 @17.10, now 15.075, -11.8%
- **-9.4% on 2026-11-12**, two-day drop 17.83 → 15.075 (-15.5%). Day's low 14.975 vs stop 14.40.
- ATR14 1.3444 (8.92% of price). Stop 14.40 is only **0.50 ATR** below the close. At entry it was 2.0 ATR; the move has eaten it.
- cause, part 1 (tape): XBI -3.27%, IBB -2.16% on 11/12 — broad biotech de-rating, not SMMT-specific. SMMT is the high-beta expression of it.
- cause, part 2 (filing, primary): 8-K dated **2026-11-04** discloses a prospectus supplement to the automatic S-3 shelf (Reg. No. 333-296642), with a **424B7** filed the same day — equity supply registered into a falling tape. Read the 8-K; it carries only the legality opinion, no share count or price, so the size is unknown.
  - source: https://www.sec.gov/Archives/edgar/data/1599298/000119312526447661/d170975d8k.htm
  - source: https://www.sec.gov/Archives/edgar/data/1599298/000119312526447652/d170959d424b7.htm
- web search found NO confirmed November 2026 ivonescimab/trial catalyst; all coverage returned was 2024-2025. Recording that as an unknown, not as "no news".
- decision: **CLOSE AT MARKET.** A position with 0.50 ATR of room is not a risk-controlled position, it is a bet on the next tick. The alternative — widening the stop on a loser — is the precise failure this report's rules forbid, and the 8-K says the float is growing while the sector de-rates.
- NOT doing: re-pitching lower. No evidence the drop is finished and the offering size is undisclosed.

## [06:07 ET] SECTOR SCAN — 2026-11-12 closes (finnhub). One sector up, and it is energy.
```
GDX    81.84  -3.95%   | XLF   58.21  -0.72%
XBI   151.20  -3.27%   | XLV  187.83  -0.59%
ITA    71.73  -2.06%   | KRE   72.52  -0.59%
XLB    52.34  -1.28%   | XLRE  44.36  -0.52%
SMH   501.73  -1.03%   | XLY  120.46  -0.44%
XLC   107.56  -0.96%   | XLP   91.06  -0.43%
XLI   169.44  -0.89%   | XLK  173.77  -0.34%
                       | XLU   43.81  -0.02%
                       | UUP   29.42  +0.24%
                       | XLE   64.33  +1.51%
                       | USO  146.07  +3.25%
```
- **The whole tape is red except crude and energy equities.** USO +3.25% and XLE +1.51% against GDX -3.95% and TLT -1.48% is a specific combination: an oil supply/demand shock, not a risk-on day.
- Gold complex is the mirror image: GLD -2.82%, GDX -3.95% (miners leveraged 1.4x the metal) with the 10Y at 4.98%. A real-rate-driven unwind.
- Defense is weak: ITA -2.06%, and open positions HII -1.79% and RTX -1.46% with it.
- Biotech worst single group ex-metals: XBI -3.27% — explains SMMT's -9.4% as beta, not news.

## [06:07 ET] NEWS — crude: a geopolitical risk premium on top of a loosening balance
- WTI Dec (CLZ26) closed **+2.55% at ~$88-89** on 2026-11-12. Drivers, in order cited: US-Iran talks deadlocked with Trump saying the US "doesn't need a deal"; attacks on Saudi energy infrastructure (Aramco); renewed Hormuz shipping disruption.
  - source: https://finance.yahoo.com/energy/articles/crude-prices-surge-dimming-us-201547431.html
  - source: https://fxempire.com/forecasts/article/oil-news-wti-and-brent-rise-as-hormuz-shipping-disruptions-renew-supply-fears-1644337
- **Against it:** OPEC+ raised output by over 2.0m bpd and Brent was $93 on 11/11 having dipped earlier in the week — source: https://invezz.com/sg/news/2026/11/11/oil-price-today-brent-rebounds-to-dollar93-despite-a-massive-opec-output-surge/
- Read: this is a supply-*risk* bid into a supply-*surplus* tape. Those usually decay unless a barrel is actually lost. I will not chase long crude on a headline premium; sources disagree on the exact level (87/88.29/89.06) so I am not setting futures levels off them.

## [06:08 ET] DATA GAP — event contracts unreachable this run
- `market_data.py events` returned **count 0** for "oil", "Fed", "CPI", "inflation", "recession", "Bitcoin". The only non-zero results ("gold", "Brent") were NBA/NFL cross-category parlay tickers with `yes_bid`, `yes_ask`, `last_price` and `volume` all null.
- So there is no priced probability available to disagree with, and the universe rule requires stating the market's implied probability. **No event-contract idea can be honestly published today.** Not a judgement that none was attractive — the quotes were not obtainable.
- Also failed this run: all Yahoo-backed index/futures/crypto quotes (HTTP 429).

## [06:15 ET] NEW IDEA — DKS — de-rated 40%, seven insiders buying, relative strength turning
- captured via add_candidate.py. entry 144.50 (rising SMA20 143.82), stop 132.25 (2.03 ATR, under twin lows 135.02/135.29 and SMA50 137.43), target 170.00 (13.43x trailing EPS 12.66), R:R 2.08, conviction 4, size 2.5%.
- insiders: **9 buys / 7 distinct buyers / $5,588,664** at 129.75-136.39 in Sep 2026, vs 2 sells $4,581,338. Gupta (CFO) 7,707sh @129.75.
- relstrength TURNED: 1m +7.97pp vs SPY (DKS +6.35 vs SPY -1.62); 3m -25.4pp, 6m -35.43pp. The damage is historical, the last month is not.
- structure: close 145.66 > SMA20 143.82 (rising) > SMA50 137.43; higher high 150.35 on 11/10; 11/12 pullback on 1.14M shares = lightest of 20 sessions.
- against it: last TWO quarters missed (-7.1%, -1.0%); analyst bullish share 61.3% -> 53.1%, two outright sells. Weakest sell-side configuration screened today.
- earnings 2026-11-23 (fetched calendar).

## [06:15 ET] REJECTED — BURL — improving revisions but still losing to its own sector: -12.37pp vs XLY over 1m while XLY was +8.04%. 4 straight beats incl +33.0% (9/30), -33.43% off high, zero insider buys and $14.4M of sales. Watchlist, not a trade: the de-rating has not stopped.
## [06:15 ET] REJECTED — PANW — -25.37% off high into 11/18 earnings, but below SMA20 (-8.3%) AND SMA50 (-12.2%), revisions deteriorating, ZERO insider buys against 109 sells / $67.9M, and the four beats are small (2.4-7.2%). ATR 6.18% would need a 20-point stop. No evidence the de-rating is wrong.
## [06:15 ET] REJECTED — LOW/HD/WMT/BJ/DIS/MDT — all 2-5% off 120-day highs and 8-14% above SMA50 into next week's prints. No room: a 2.0-ATR stop sits above or at the last support, so the floor can only be cleared by inventing a target.
## [06:15 ET] REJECTED — TJX — 11/18 earnings, -20.01% off high, but below SMA20, revisions deteriorating -6.8pp, zero insider buys / $27.7M sold. Same shape as BURL and the same verdict.
## [06:15 ET] DATA GAP — `market_data.py short` ReadTimeout on api.nasdaq.com for ALL of PANW, TJX, BURL, DKS. No short-interest or days-to-cover read available this run. `market_data.py implied` returns HTTP 401 from yahoo-options, so no options-implied move either — I cannot say whether any target today sits inside what the market prices.

## [06:16 ET] ACT AT THE OPEN — THREE CLOSE INSTRUCTIONS ON MONEY ALREADY AT RISK
**Synthesis: carry these three sentences into `data_quality_notes` verbatim and near the top. They are not new positions, they are exits, and none of them can be expressed as a candidate that clears a reward-to-risk floor — a close has no target.**

1. **SMMT — CLOSE AT MARKET.** 15.075, -11.8% from the 17.10 fill. The 14.40 stop is 0.50 ATR away (ATR14 1.3444, 8.92% of price) so the position is a bet on the next tick, and the 2026-11-04 8-K registered an undisclosed amount of new equity. Do not widen the stop.
2. **HII — CLOSE AT MARKET, or at minimum trim half and place a 279.00 stop on the remainder.** 308.33, **+17.7%** from the 262.00 fill, and carrying NO STOP after 30 days. Forward reward-to-risk is 1.07:1 (31.43 to the 339.76 target against 29.33 to a 279.00 stop), and the 339.76 target is ABOVE the 120-day high of 334.53. Defense is the second-worst group on the board (ITA -2.06%). Taking +17.7% beats holding a 1.07:1.
3. **BCC — CLOSE AT MARKET.** 67.92, -11.2% from the 76.50 fill, no stop, and it closed 2026-11-12 at 67.92 against a 120-day low of 67.045 — a new low, below SMA20 74.703 and SMA50 75.2278. The evidence has turned with the price: analyst bullish share 63.6% -> 54.5% (-9.1pp), the 2026-09-30 quarter MISSED by -7.7% (1.04 vs 1.1269), zero insider buys against three sales. With the 10Y at 4.98% the housing-demand thesis has no near-term route back. The 2026-11-11 report already called this invalidation met and the red team cut it; one more session produced a new low.

## [06:16 ET] POSITION UPDATE — HOLDS, no change needed (stops and targets unchanged)
- `AAL` SHORT 13.35 -> 13.31. **HOLD the short.** Fell -5.6% on 11/12, now back to the fill after being -5.7% underwater on 11/11. Stop 14.40 = 1.81 ATR above (ATR14 0.6029); target 10.60; R:R from the fill 2.62. Still above SMA20 12.835 and SMA50 12.935, so the break is not confirmed — but the stop is intact and the thesis is.
- `ONON` BUY 34.20 -> 33.07, -3.3%. **HOLD, stop unchanged at 30.69.** Evidence got BETTER, not worse: 8 open-market buys by 3 distinct insiders totalling $10,581,880, and four consecutive beats (+12.9/+1.8/+51.5/+20.9%). Above SMA50 32.056, below SMA20 34.786. Already published 3x in ten days — this is a hold note, NOT a re-pitch.
- `OXY` +8.1% (54.00 -> 58.40, +2.0% on the day): hold. The only sector that rose on 11/12 was energy (XLE +1.51%, USO +3.25%); target 62.00 is 1.0 ATR away.
- `KHC` +6.4%, `UNP` +5.4%, `ABT` +4.1%, `PYPL` +3.2%, `PFE` +4.5%, `XLU` +1.2%, `RTX` -0.3%: all hold, no amendment. None has an earnings date inside the window (checked against the fetched calendar) and none is within 1 ATR of its stop.

## [06:23 ET] NEW IDEA — LEN — Berkshire bought $329m at 0.85x book; the Street is 7% bullish
- captured. long_term, entry 79.50 (zone 77.00-84.00, thirds at 84/81/77.50), target 108.50 (1.197x book), bear case 68.00 (0.75x book), R:R 2.52, conviction 5, size 4%.
- **PRIMARY DOC READ** — Q3 FY2026 8-K, qtr ended 2026-08-31: equity $21,558,959k / 237,756k wtd dil shares = **$90.68 book/share**. Price 83.58 = **0.92x book**. GM on home sales 15.8%. Orders 20,879 vs 23,004 LY (**-9.2%**). Deliveries 20,840 vs 21,584. EPS 1.19 (1.23 adj). HB cash $1,150,115k. Net HB debt $3,147,136k = **12.7% of total capital**. $650m drawn on a $3.1bn revolver.
  - source: https://www.sec.gov/Archives/edgar/data/0000920760/000162828026062287/ex991-2026831x8kq3.htm
  - BVPS ~$91 / equity ~$22bn also stated by management on the Q3 call: https://www.fool.com/earnings/call-transcripts/2026/09/17/lennar-len-q3-2026-earnings-call-transcript/
- **BERKSHIRE HATHAWAY INC: 24 open-market Form 4 buys, $329,017,222, all dated 2026-10-02, prices 77.12-81.90, zero sales.** Largest blocks 842,753sh @80.04 and 342,553sh @79.03. That is 0.85-0.90x book.
- sell side is the most bearish screened today: **7.1% bullish** — 2 strong buy / 0 buy / 11 hold / 13 sell / 2 strong sell. Four straight MISSES: -9.2 / -1.1 / -3.9 / -13.7%.
- structure: 83.58 on SMA50 81.5992 after -12.2% in five sessions from the 95.22 high (11/05). Accumulation shelf = 10/20 low 76.48, 10/21 low 77.20. ATR14 3.887.
- invalidation (NOT a price move): equity per share falls two quarters running, or HB gross margin prints below 14.0%.
- **deliberate tension, stated in the candidate:** I am closing BCC out of the same end-market today. BCC sells commodity OSB at a spot price, has no book floor, -7.7% miss, zero insider buys, new 120-day low. LEN owns a land bank at 12.7% net leverage with Berkshire under it. Not the same bet.

## [06:23 ET] WATCHLIST — KMX — the beat record nobody believes, but no structure and stale insiders
- 52.58, -19.45% off high, +30.47% off low. Below SMA20 53.542 AND SMA50 55.5322 — a 51-58 chop with no trend. ATR14 2.3537 (4.48%), ADV $138M.
- four consecutive beats and they are enormous: **+56.1% (9/30), +32.4%, +46.8%, +34.5%**. Street is 29.2% bullish and IMPROVING — 5 strong buy / 2 buy / 17 hold, zero sells now (was 1).
- insiders: 6 buys / 5 distinct / $1,268,037 / **zero sells** — but all dated 2026-06-22 to 06-25 at 52.01-53.39, five months ago, and the stock is flat on them. Stale evidence.
- why not a trade today: no dated catalyst inside the window, price below both moving averages, and a 2.0-ATR stop (4.71) would sit at 47.87 — under the whole range, which means the R:R only works on a target I cannot anchor. Watchlist until it reclaims SMA50 55.53.

## [06:27 ET] NEW IDEA — VVV — the one clean breakout-with-evidence in the screen
- captured. entry 34.50 (7-session shelf low 34.41), stop 31.80 (2.14 ATR, back inside the broken 30.705-33.09 range, under the 10/30 low 32.095), target 40.30 (120-day high 41.08 less margin), R:R 2.15, conviction 4, size 2.5%.
- breakout 11/02: 32.29 -> 34.37 close on **4,040,405 shares**, highest of 20 sessions, out of a six-week 30.705-33.09 range. High 36.415 on 11/04. Held 34.41-34.85 for seven sessions since.
- insiders 4 buys / **4 distinct** / $500,876 vs $239,156 sold. Willis (CFO) 10,000sh @31.80 (5/14), Freeland 3,100@32.37, Slater 1,000@32.53, Denny 1,506@33.20 (8/12). All bought BELOW today's price.
- analysts **IMPROVING** 66.7% -> 72.7% (+6.0pp). Beats: +12.3 / +18.1 / +12.3 / -4.7%.
- relstrength: 1m +14.61% vs SPY -1.62% = **+16.23pp**; +6.57pp vs XLY. Leadership, not a bounce.
- earnings **2026-11-19 bmo** (fetched calendar), eps est 0.4253, rev est $567m.
- honest weakness noted in key_risk: +11.8% above SMA50, so no valuation cushion; and no 10-Q read.

## [06:27 ET] REJECTED — INTC — the market's largest dislocation, and the company confirmed the bear case itself
- 61.20, **-57.01% off a 142.35 high**. ATR14 6.3103 = **10.31%** of price. Gapped 2026-10-30 from a 92.07 close to a 68.36 open, closing 65.76 on **455,599,400 shares** — reported as the steepest one-day fall since 1974. Low 51.51 on 11/05.
- cause: Q3 BEAT (adj EPS 0.52 vs ~0.41) but Q4 guided to **$15-16bn revenue and $0.25 adj EPS against ~$17bn and $0.43** expected; PC shipments guided -12% in 2026 and -10% in 2027; Foundry lost **$1.85bn** in Q3 operating. BofA cut Buy->Neutral, target 145 -> 100.
  - source: https://www.cnbc.com/2026/10/30/intel-guidance-analyst-price-targets.html
  - source: https://247wallst.com/investing/2026/10/30/intel-plunges-25-as-weak-outlook-and-pc-slump-overshadow-earnings-beat-dell-tumbles-13-amd-sinks-10-nvidia-falls-3/
- the one thing arguing the other way is strong: **CEO LIP-BU TAN bought 150,000 shares @64.7312 on 2026-11-02 ($9.71m)**, on top of 105,263 @95.00 on 2026-08-11. $19.7m total, and he is underwater on both.
- why rejected anyway: a 2.0-ATR stop is 12.62 wide (20.6% of price), so entry 61.20 / stop 48.50 needs a 86.60 target to clear 2.0:1 — which is back above the pre-gap price and requires the company's OWN Q4 guidance to be wrong. Still below SMA20 75.2535 (-18.7%) and SMA50 95.6136 (-36.0%). One CEO purchase against a confirmed secular PC decline and a $1.85bn/quarter foundry loss is not a 2:1 trade.
- WATCHLIST CONDITION, specific: a close back above SMA20 75.25 with the Q4 print (late January) at or above the $16bn high end.

## [06:27 ET] REJECTED — small-cap earnings screen, 24 names, three finalists cut
- `BRBR` 10.24 — best structure of the group (+7.0% vs SMA20, +13.8% vs SMA50, +39.7% off low) but 3 of 4 quarters MISSED and badly: -20.1%, -56.5%, -8.7%. Insider buys total $56,938 — two people, immaterial. Revisions deteriorating.
- `LZB` 32.53 — -27.55% off high and above both MAs, earnings 11/17 amc, but ZERO insider buys against $2,403,173 sold, revisions flat, and the 9/30 quarter missed -13.7%.
- `GLOB` 45.75 — **four consecutive misses** (-8.7, -1.7, -2.1, -2.8%), 51.7% bullish and flat. One insider buy in May. No.
- `POWL` -55.28%, `SMTC` -40.87%, `SYM` -37.12%, `KLIC` -46.67%, `AMBA` -36.63%, `ESE` -35.02%, `NTNX` -19.89%: all below BOTH moving averages. Deep drawdown plus a broken chart is not a setup, it is a falling knife; none had an insider cluster to argue otherwise.
- `PERI` 11.37 — at its 120-day high, +22.7% above SMA50, ADV only $8M. No room and thin.

## [06:29 ET] FALSIFICATION — DKS — my own valuation anchor was wrong; RE-CAPTURED with the fix
**Synthesis: use the SECOND DKS line in candidates.jsonl. The first anchored on trailing EPS and overstated the cheapness.**
- what I got wrong: I computed 11.5x from the four reported trailing actuals (12.66). The company GUIDED FY2026 adjusted EPS down to **$11-12 from $13.50-14.50** on 2026-08-25. Forward, 145.66 is **12.67x** the $11.50 midpoint.
- and the correction kills the easy version of the thesis: 179.33 pre-cut was **12.81x** the old $14.00 midpoint. The multiple is essentially UNCHANGED. **The entire 40% drawdown is the EPS cut, not a de-rating** — so there is no multiple compression to collect and it must not be pitched as a cheapness trade. It is a bet that $11-12 is the trough. Target 170.00 restated as 12.6x a recovery to the old $13.50, the same multiple on restored earnings.
- what the research ADDED, and it is the strongest part: the cut was not the core. On 2026-08-25 DKS fell **30.7% in one session (179.33 -> 124.31), its worst on record**, with the DICKS banner comping **+4.9%** while Foot Locker pro forma comps fell **-3.6%**. Foot Locker guidance swung from a **$110-150m operating profit to a $40-80m operating loss**. UBS kept Buy, blaming excess legacy footwear inventory and promotions. Management reiterated **$100-125m** of cost synergies.
  - source: https://finance.yahoo.com/markets/stocks/articles/dks-cuts-2026-profit-outlook-155500380.html
  - source: https://www.fool.com/investing/2026/08/25/dicks-sporting-goods-core-business-grows-49-but-foot-locker-losses-and-weak-guidance-send-shares-tumbling/
  - source: https://ecmsource.com/dicks-sporting-goods-dks-q2-fy26-foot-locker-guidance-cut-august-2026/
- conviction held at **4 although five distinct evidence kinds now hold** (dated_catalyst, positioning, technical_level, valuation_anchor, counter_argument_answered). Reason: no primary document read for DKS — the guidance figures are from secondary coverage, unlike LEN where I read the 8-K. Validation will name 5; 4 is the honest claim.
- stop risk restated honestly: this name fell 30.7% in a day three months ago, so a 2.03-ATR stop at 132.25 WILL be gapped through rather than touched. The real risk is the full 12.25 or worse. That is in key_risk.

## [06:30 ET] AWAITING-ENTRY TRIAGE — all 8 unfilled published levels, each given a verdict
Prices are 2026-11-12 closes. Prior context listed these as published-but-never-filled; none had a verdict, so here is one for each.

- **`TLT` BUY @80.30 (pub 2026-11-04) — THIS ONE FILLED AND THE TRACKER HAS NOT NOTICED.** TLT traded 80.81 high / **79.72 low** on 2026-11-12 and closed 79.72. The range brackets 80.30, so the limit was touched. It should be an OPEN POSITION at 80.30, now -0.7%. **Synthesis/publish: this is a data-integrity item, not a trade idea.** On the merits the position is uncomfortable — the 10Y is at 4.98%, TLT closed at the low of the day below SMA20 81.126 and SMA50 80.2633, and the 120-day low is 76.43. ATR14 is only 0.7575 so there is no stop that is both meaningful and survivable; treat it as a small duration position and name 76.43 as the invalidation.
- **`GLD` SELL @406.77 (pub 2026-10-25) — WITHDRAW.** Gold went the predicted way without us: GLD is 354.89, **12.8% BELOW** the short entry, which is 6.8 ATR (ATR14 7.6586) above the market. The call was directionally right and unfillable. Re-shorting here means selling a close that WAS the 120-day low (352.91 low, closed 354.89, -2.82%) after a -17.36% decline — I will not. No new gold idea today.
- **`CVS` BUY @79.00 (pub 2026-11-05) — WITHDRAW.** CVS is **89.79, 13.7% above** the limit. It was stopped out on 2026-11-04 and re-pitched the next day at a level the stock never revisited; it has now been published 3x in ten days. That is the anchoring pattern prior context warns about, not conviction. Do not publish a fourth.
- **`HUN` BUY @9.00 (pub 2026-11-10) — WITHDRAW.** 9.66, **7.3% above** the limit. The 2026-11-11 re-pitch was already cut by the red team for claiming unchanged levels that had changed; two sessions later the gap is wider.
- **`/MBTZ6` SHORT @74,075 (pub 2026-11-09) — WITHDRAW, direction was right.** BTC spot is **69,252, -5.54% in 24h** (ETH 1,951 -4.42%, SOL 80.39 -2.98%) — already **6.5% below** the short entry. A sell-limit 7% above a market that is falling is not actionable, and chasing the break at 69,252 after -5.5% is not a trade I can set a 2.5-ATR stop on with no futures quote available (all Yahoo futures/crypto endpoints 429'd this run).
- **`KXCPIYOY-26SEP-T3.5` NO @18 (pub 2026-09-30) — REMOVE AS RESOLVED/EXPIRED.** It is a SEPTEMBER 2026 CPI contract and today is 2026-11-13; the referenced print is long past. I cannot confirm the resolution because `market_data.py events` returns count 0 for every macro topic this run. Flag for manual removal rather than carrying it as live.
- **`XLV` BUY @184.00 (pub 2026-11-09) — KEEP, LEVEL UNCHANGED.** 187.83, 2.1% above the limit, -0.59% on the day. Still a reachable pullback limit and nothing in the thesis changed. Nothing to say beyond: the level stands.
- **`ADM` BUY @68.80 (pub 2026-11-11) — KEEP, LEVEL UNCHANGED.** 70.97, 3.2% above the limit; the 11/12 low was 70.51. Published two days ago and still live. The level stands.

## [06:31 ET] REJECTED — the whole energy complex, despite being the only sector that rose
- XLE +1.51%, USO +3.25%, XOP +5.4% over four sessions (173.77 -> 183.11). It is the only bid on the board, so I screened it properly rather than assuming.
- insider sweep, 13 energy names: **not one cluster.** XOM 0 buys / 0 sells. CVX 0 buys / 24 sells. FANG 0 / 35. PSX 0 / 16. MPC 0 / 11. WMB 0 / 11. TRGP 0 / 10. EOG 0 / 4. COP 0 / 3. VLO 0 / 2. APA 0 / 1. OKE 0 / 0. KMI the only buy — 1 buyer, $14,994,200, against 9 sells.
- and the structure says bounce, not breakout: **XLE 64.33 is BELOW SMA50 64.979 and 3.0% below SMA20 66.3325**; XOP 183.11 is below SMA20 191.558 and SMA50 190.4072. Both are counter-trend rallies INTO resistance from underneath.
- plus the fundamental is pointing the other way: OPEC+ added over 2.0m bpd while the rally is a US-Iran/Hormuz/Aramco risk premium. A premium decays unless a barrel is actually lost.
- verdict: no new energy idea. The existing `OXY` long (+8.1%) is the right amount of exposure to this and it is already on. Holding it is the position, not a reason to add a second.

## [06:31 ET] CONCENTRATION AND CORRELATION CHECK — read before publishing
- four candidates captured and **all four are long US equity** on a session where every sector except energy fell. That is a real skew and should be said plainly rather than dressed up.
- drivers are genuinely distinct, so the 3-per-driver cap holds: `LEN` is rates/housing book value, `DKS` is a Foot Locker inventory recovery, `VVV` is a vehicle-services momentum continuation, `ACM` is an existing infrastructure position being trimmed into a print. `DKS` and `VVV` are both consumer-adjacent — that is 2 on the consumer, inside the cap.
- **nothing short, nothing in futures, nothing in crypto, nothing in event contracts today, and only one of those four is a judgement call.** Futures/crypto: the only expression I would have wanted was a continuation short, and all Yahoo futures and crypto quote endpoints returned HTTP 429, so I could not set a contract-month level or an ATR-based stop on any of them honestly. Event contracts: quotes unobtainable (count 0 on every macro topic). Gold and bitcoin shorts were both declined on merit — chasing a 120-day low and a -5.5% day respectively.
- the honest summary of the day: **three new ideas, one position trim, three closes, and five stale levels withdrawn.** The tape was mostly falling knives and counter-trend bounces into resistance; the three names that survived did so because an insider cluster or a read balance sheet said the drawdown was wrong, not because the chart looked good.

## [06:31 ET] ARITHMETIC SELF-CHECK — recomputed every captured number from source
Recomputed R:R, stop distance in ATRs, expectancy vs the 1/(1+R:R) baseline, and evidence-kind count against the claimed conviction for all four. All pass.
```
ACM swing  e=66.74 t=77.22 stop=61.50  RR=2.00 (floor 2.0)  stop=2.41 ATR (need 2.0)  wp=0.42 vs base 0.333 = +8.7pp  kinds=3 supports=4 claimed=4
DKS swing  e=144.50 t=170.00 stop=132.25 RR=2.08 (floor 2.0) stop=2.03 ATR (need 2.0)  wp=0.40 vs base 0.325 = +7.5pp  kinds=5 supports=5 claimed=4
VVV swing  e=34.50 t=40.30 stop=31.80  RR=2.15 (floor 2.0)  stop=2.14 ATR (need 2.0)  wp=0.40 vs base 0.318 = +8.2pp  kinds=3 supports=4 claimed=4
LEN long   e=79.50 t=108.50 bear=68.00 RR=2.52 (floor 2.5)  n/a (bear case, not a stop) wp=0.45 vs base 0.284 = +16.6pp kinds=4 supports=5 claimed=5
```
- ACM sits EXACTLY on the 2.00 floor and LEN at 2.52 against 2.50. Neither was tuned to get there: ACM's stop is the published 61.50 and I deliberately did NOT walk it in, and LEN's target is 1.197x a book value computed from the filing. Both are thin margins and the red team should know they are thin rather than comfortable.
- DKS claims 4 while five evidence kinds hold. Deliberate — no primary document was read for DKS.

## [06:31 ET] RESEARCH COMPLETE
- **candidates: 4 unique symbols in 5 rows** (DKS captured twice; the SECOND row is the corrected one — use it).
  - `LEN` buy long_term conviction 5 — NEW
  - `DKS` buy swing conviction 4 — NEW
  - `VVV` buy swing conviction 4 — NEW
  - `ACM` buy swing conviction 4 — EXISTING POSITION, trim half by Monday's close
- **three close instructions are in notes only and MUST be carried into data_quality_notes: SMMT, HII, BCC.** A close has no target so it cannot clear a reward-to-risk floor and cannot be a candidate; see the ACT AT THE OPEN block. Five stale published levels withdrawn (GLD, CVS, HUN, /MBTZ6, KXCPIYOY-26SEP-T3.5); two kept unchanged (XLV @184.00, ADM @68.80); **TLT @80.30 appears to have FILLED on 2026-11-12 and is not marked as a position.**
- coverage gaps:
  - **event contracts entirely** — `events` returned count 0 for oil, Fed, CPI, inflation, recession and Bitcoin; the only hits were null-priced sports parlays. No implied probability to disagree with, so no event idea could be honestly written.
  - **futures and crypto levels** — every Yahoo-backed quote (indices ^GSPC/^NDX/^DJI/^RUT/^VIX/^DXY/^TNX, ES/NQ futures, gold, WTI) returned HTTP 429. Crypto spot came from CoinGecko, but with no futures quote I could not set a contract-month entry or a 2.5-ATR stop on /MBT, /MES, /MNQ, /M2K, /MGC or /MCL. **This is why there is no futures idea today, and it is a tooling failure, not a judgement.**
  - **short interest and days-to-cover: zero coverage.** `market_data.py short` ReadTimeout on api.nasdaq.com for every symbol attempted (PANW, TJX, BURL, DKS).
  - **options-implied move: zero coverage.** `market_data.py implied` returns HTTP 401 from yahoo-options, so no target today was checked against what the straddle prices.
  - no 10-Q read for DKS or VVV (LEN's Q3 8-K was read in full).
  - intraday horizon not covered: prices are 2026-11-12 closes at a 06:00 ET start, which is a closed market, not stale data — there is no intraday setup to be had before the open.
- sources that failed: Yahoo chart API (429, all index/futures/crypto/macro symbols), Yahoo options API (401), api.nasdaq.com short interest (ReadTimeout), Kalshi via `events` (0 results on every macro query), finnhub index quotes (CFD subscription required). Working: finnhub quotes/earnings/insiders/analysts/filings, nasdaq history, CoinGecko, FRED, SEC EDGAR, WebSearch/WebFetch.

## [06:32 ET] INSIDER SWEEP — ~75 names across six sectors; six clusters in the whole market
The bar: at least 3 open-market Form 4 purchases by at least 3 DISTINCT insiders. Everything below was checked, not assumed.
- **PASSED (6):** `LEN` Berkshire Hathaway $329,017,222 / 24 buys (1 holder, but the size and the 0.85x book make it the strongest single signal found) · `DKS` 7 distinct / $5,588,664 · `KMX` 5 distinct / $1,268,037 / zero sells · `VVV` 4 distinct / $500,876 · `ACM` 3 distinct / $699,391 / zero sells · `ONON` 3 distinct / $10,581,880 (already an open position).
- **financials, 15 names, no cluster:** KEY, C, RF, CFG, MTB, ZION, FITB, ALLY, BAC, WFC, PNC, USB all zero buys. HBAN 7 buys but only 2 distinct and 6 offsetting sells. SOFI 2 buys / 1 distinct / 8 sells. TFC 2 / 1 / 3.
- **healthcare, 13 names, no cluster:** MRK (17 sells), GILD (51 sells), DXCM (24), MRNA (16), AMGN, ABBV, VTRS, BIIB, ZBH, BAX, SOLV, CNC, MOH all zero buys. ELV 3 buys but 2 distinct against 17 sells.
- **industrials/defense, 10 names, no cluster:** GD (26 sells), PH (17), NOC (15), LMT (12), EMR, DOV, LHX all zero buys. ROK 3 buys / 1 distinct / 11 sells. ETN 3 / 1 / 4.
- **energy, 13 names, no cluster** (logged above).
- why this matters more than any single name: insider buying is the one signal this report is thin on and it is genuinely scarce right now — six clusters in seventy-five liquid names. Three of today's four candidates are in that six, and that is the reason they are the four, rather than the charts.

## [06:32 ET] ADDENDUM — log order note and final state
The RESEARCH COMPLETE block above was written at 06:31; the six-sector insider sweep that follows it was run afterwards and produced **no new candidate**, so everything RESEARCH COMPLETE says still holds. Research ran 06:00-06:33 ET and finished inside its budget — it was NOT truncated.
Final: `candidates.jsonl` = 5 rows / **4 unique symbols** (LEN, DKS, VVV, ACM). DKS appears twice; the later row (06:29:22) is the corrected one.
I stopped with budget remaining rather than padding. KMX was the only near-miss and is on the watchlist with a specific condition (reclaim SMA50 55.53) rather than being stretched into a long_term idea it cannot support — 15.8x trailing EPS of 3.32 is not a valuation anchor, and its insider cluster is five months stale.
