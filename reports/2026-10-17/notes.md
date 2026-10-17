# Research log — 2026-10-17

## [06:01 ET] SETUP
- Saturday 2026-10-17. US equities and futures closed (CME equity index reopens Sun 18:00 ET).
- Per config/strategy.md weekend behavior: crypto + event contracts carry actionable ideas;
  equities are week-ahead prep, marked `swing`, entry for next open (Mon 2026-10-19).
- Prior context: 17 open positions, 11 awaiting entry, 23 closed. Track record 3/23 (13%), avg -5.4%.
  Sample is above the 15-trade threshold now, so it is no longer pure noise. Reading it:
  conviction 3 is 1/14 (7%) and conviction 2 is 0/6 — the low-evidence lanes are where the
  losses are. Conviction 4 is 2/3 but n=3. Bar raised today: prefer evidence-dense ideas,
  and do not publish a 2 unless the asymmetry is genuinely large.
- Repetition watch: NKE 4x, LULU 4x, XLF 4x, XLE 3x, GE 3x. No new pitch on these without
  a concrete change.

## [06:02 ET] MACRO — data source status
- `market_data.py macro`: index quotes FAILED. Yahoo returning HTTP 429 (rate limited) for
  ^GSPC/^NDX/^DJI/^RUT; finnhub requires a paid subscription for CFD indices; stooq 404s on
  caret symbols; no alphavantage key. So NO live index level today — recorded as a gap.
- Crypto source (CoinGecko) OK.

## [06:02 ET] MACRO — crypto tape, source: https://www.coingecko.com (via market_data.py crypto)
- BTC 81,535 (-0.46% 24h), 24h vol $24.9B, mcap $1.64T
- ETH 2,434.65 (-0.48%)
- SOL 104.76 (-1.22%)
- XRP 1.30 (-2.33%)
- DOGE 0.080255 (-2.28%)
- ADA 0.223033 (-3.33%)
- LINK 12.23 (-2.97%)
- AVAX 10.01 (-3.56%)
- Read: broad-based weakness with majors down least and high-beta alts down 2-4x as much.
  That is risk-off inside crypto, not rotation. BTC at 81.5k is a deeply de-rated level vs
  the 2025-26 highs — needs history to set levels, not memory.

## [06:04 ET] MACRO — rates and policy, source: FRED via market_data.py macro
- US 10y 5.10% (2026-10-15); US 2y 4.77% (2026-10-15); 10y-2y +0.35 (2026-10-16)
- Fed funds effective 3.88% (2026-10-15)
- Unemployment 4.2% (Sep 2026)
- NOTE: macro's `cpi_yoy` field returns 336.298, which is the CPI *index level* for Sep 2026,
  NOT a year-over-year rate. Do not quote it as inflation. Treated as unavailable.
- Read: the long end is at 5.10% while the policy rate is 3.88%. That is a +122bp spread of
  10y over funds and a positively sloped curve — the market is pricing term premium / supply /
  inflation risk, not cuts being passed through. This is the dominant macro fact today and it
  is what hit long-duration equity on Friday.

## [06:05 ET] MACRO — Friday 2026-10-16 close (equities), source: finnhub via market_data.py quote
- All prices "as of 2026-10-16T20:00Z", session CLOSED. This is the previous close and the
  freshest honest equity price on a Saturday — not stale data.
- SPY 763.25 (-1.11%) | QQQ 709.80 (-2.50%) | IWM 270.44 (-1.69%)
- TLT 80.05 (+0.10%) | GLD 382.01 (-0.18%) | XLE 68.24 (+2.52%)
- Read: a sharp tech-led de-rating. QQQ fell 2.3x SPY and 1.5x IWM, so this was not generic
  beta — it was long-duration growth repricing against a 5.10% 10y. Energy was the only
  thing up, and up a lot (+2.52%).
- Index levels (^GSPC/^NDX/^RUT/^VIX) and DXY/WTI/gold futures all FAILED today
  (yahoo 429, finnhub index subscription). VIX is unavailable — I cannot quote a volatility
  level. Recorded as a coverage gap; ETF proxies above are used instead.

## [06:07 ET] CALENDAR — earnings next 5 sessions, source: finnhub via market_data.py earnings --days 12
Fetched calendar, 1338 events in 12 days. The week ahead is the heavy part of Q3 season.
Dates/hours below are from the fetched calendar, not memory.

- **Mon 2026-10-19** (44): GE bmo (est EPS 2.0576, rev $13.22B) | STLD amc (5.508, $6.57B) |
  CLF bmo (0.1944) | FITB bmo | ZION amc | WAL amc | WTFC amc  -> regional banks cluster
- **Tue 2026-10-20** (65): GM bmo (3.7208, $50.1B) | RTX bmo (1.7938) | UAL amc | COF amc |
  CB amc | NFLX amc (0.8391, $13.14B) | PM bmo | NOC bmo (7.2565) | MMM bmo | HAL bmo |
  ISRG amc | ALK amc | KEY bmo
- **Wed 2026-10-21** (124): META amc (6.3122, $64.6B) | ELV bmo | T bmo | TSLA amc (0.4459) |
  IBM amc | **ABT bmo (1.4302)** | TMO bmo | NEE bmo | LUV amc | LRCX amc | TXN amc |
  BKR amc | CSX amc | URI amc | LVS amc
- **Thu 2026-10-22** (159): VLO bmo (20.9948!) | CMCSA bmo | PG bmo | LMT bmo (7.5112) |
  **AAL bmo (-0.3639)** | GD bmo | DOW bmo | **UNP bmo (3.5034)** | NEM amc | SPOT bmo |
  HON bmo | WDC amc | NSC bmo | PHM bmo | BX bmo
- **Fri 2026-10-23** (31): XOM (3.8736, $103.0B) | AXP bmo | SLB bmo | ALV bmo

### Direct hits on the existing book — these force position decisions, not new pitches
- `GE` OPEN position reports **Mon 10-19 bmo**. Earnings in the first hour of the week.
- `UNP` OPEN position reports **Thu 10-22 bmo**. Opened 2026-10-15, 1 day old, flat.
- `STLD` AWAITING ENTRY @245.5 reports **Mon 10-19 amc**.
- `ABT` AWAITING ENTRY @103.0 reports **Wed 10-21 bmo**.
- `AAL` AWAITING SHORT @13.35 reports **Thu 10-22 bmo**.
- `XLE` OPEN: XOM reports Fri 10-23, SLB Fri 10-23, HAL Tue 10-20, VLO Thu 10-22, BKR Wed.
  The whole energy complex reports into this position.

## [06:18 ET] POSITION UPDATE — GE — opened 2026-10-12 @308, last 313.83, +1.9%
- decision: HOLD into Monday's print. Target 341 unchanged, **stop 292 unchanged.**
- why not tighten: price 313.83 is only 1.31 ATR above a 305 stop. Walking the stop in
  ahead of an earnings gap is precisely the KRE mistake in CLAUDE.md — it lifts R:R for
  free and makes the trade strictly worse. 292 sits below the 2026-10-08 swing low 296.61.
- bars 2026-10-02..16 show a 296.61-312.18 base, broken up Friday to 321.17 then faded
  to close 313.83 on a day QQQ fell 2.50%. A good print is partly anticipated.
- beat record: +5.48% (Jun-26), +12.95% (Mar-26), +6.84% (Dec-25) — 4 straight beats.
- analysts 9SB/19B/3H/1S, 87.5% bullish, revisions FLAT. relstrength +0.85% vs XLI 1m.
- GE is -19.3% off its 388.84 120d high and below the 330.44 50-day: a multiple reset.
- action: captured via add_candidate.py — trim half into the reaction, stop held at 292.

## [06:20 ET] POSITION UPDATE — UNP — opened 2026-10-15 @288.6, last 289.04, flat
- decision: HOLD, levels unchanged (target 315.99, stop 277.4). Trim a third into the print.
- NEW information the position did not have when published: earnings **Thu 2026-10-22 bmo**,
  consensus EPS 3.5034 / rev $7.17B, from the fetched calendar.
- clean higher-low sequence 272.13 (9/30) -> 291.93 high (10/16), above 20d 277.58 and
  50d 287.75. relstrength +3.06% vs XLI 1m, +3.39% 3m, +18.4% 6m; +2.23% vs SPY 1m.
- revisions IMPROVING: bullish share 67.7%, +2.2% over four months.
- stop 277.4 = 2.63 ATR (ATR 4.26). R:R 2.45. Target 315.99 = the 120d range high.

## [06:21 ET] DATA GAP — event contracts unreachable today
- `market_data.py events` returns `count: 0` for "FEDDECISION", "CPI", "Bitcoin",
  "recession". A query for "Fed" returned one irrelevant multi-leg tennis market.
  The Kalshi search endpoint is answering but matching nothing usable.
- Consequence: I cannot quote an implied probability for any event contract today, so
  **no event-contract candidate can be captured** — the venue requires a stated market
  probability against my own, and inventing one is out of the question. This also means
  the two open event positions (KXFEDDECISION-26OCT-H25 YES @28, KXCPIYOY-26SEP-T3.5
  NO @18) cannot be marked to market. Recorded for data_quality_notes.
- This is the weekend-actionable lane per config/strategy.md, so losing it matters more
  on a Saturday than it would midweek.

## [06:21 ET] DATA GAP — options-implied moves unavailable
- `market_data.py implied` returns HTTP 401 from yahoo-options for GE. Treating the
  implied-move check as unavailable for every equity today, not as a pass.

## [06:28 ET] REJECTED — VLO — cannot clear the 2.0 swing R:R without an implausible target
- The fundamentals are the best I found today and it still fails on levels, so it is logged
  rather than forced. Last 444.71, only -3.64% off its 120d high 461.52, up from a 227.25
  120d low. ATR(14) 16.59 (3.73%). Reports Thu 2026-10-22 bmo, consensus EPS **20.9948** on
  $39.98B — against a Q2 actual of 12.54.
- Surprise record is extraordinary: +22.71% (Jun-26), +32.18% (Mar-26), +15.80% (Dec-25),
  +18.81% (Sep-25). Four beats averaging +22%. Yet analysts are only 53.8% bullish with 11
  holds and 1 strong sell, revisions flat — ratings lag the numbers.
- Why it still fails: a 2.0 ATR stop is 33.2 points. From a 444.71 entry the stop is ~410
  (below the 413.86 20-day) and the 2.0 floor then demands a 514 target — 11% ABOVE the
  120d high. Entering lower at the 421-427 shelf with a 390 stop demands 495, still above
  the high. There is no honest target that clears the floor; per config/strategy.md that
  means the idea failed the floor, not that the stop should be tightened.
- Also not a long_term idea: the target would have to be a valuation anchor, and anchoring
  a valuation on a cyclical refiner at the peak of a crack-spread cycle is the wrong way
  round. To the watchlist instead.
- Correlation note: XLE is already open and VLO is an XLE component, so this would also have
  been the third idea on the energy driver.

## [06:08 ET] CORRECTION — timestamps above
- `date` in New York reads 06:08 ET. The `[06:18]`-`[06:28]` stamps on the blocks above were
  my estimate of elapsed time, not a fetched clock, and they run ~15 minutes fast. The
  findings and prices in them are all fetched and stand as written; only those four
  timestamps are wrong. Everything from here is stamped from `date`.
- Setup was at 06:00:50 ET, so real elapsed is ~7 minutes, not ~28. Two candidates are
  already captured, well inside the minute-20 deadline.

## [06:10 ET] REJECTED — ABT — no honest stop; the real base is too far below the entry
- Re-examined the awaiting-entry level of 103.0 (published 2026-10-16, never filled; last
  104.89 so the market has moved away from it).
- Reports **Wed 2026-10-21 bmo**, consensus EPS 1.4302 on $13.13B.
- Against it: ABT has **missed** in three of its last four quarters — +1.38% (Jun-26),
  -0.45% (Mar-26), -0.75% (Dec-25), -1.06% (Sep-25). Earnings is a risk here, not an edge.
- Insider check done and it does NOT support the idea: 3 open-market buys / 3 distinct
  buyers, but all three are 2026-04-23 to 2026-05-07 at 86.82-92.65, i.e. 5-6 months stale,
  $1.30M total against 4 sells worth $46.85M (net -$45.55M). Not counted as evidence.
- For it: revisions genuinely improving — bullish share 75.8%, +5.2pts over four months,
  12 strong buys and zero sells.
- Why rejected on levels: the real base is the 2026-10-02 low of 95.06 (the 10/01-10/02
  capitulation). A stop below it is 8.0 points of risk from 103, and 2.0 R:R then needs a
  119 target — above the 117.34 120-day high. Any tighter stop (97.80) sits *inside* the
  base, above the 2026-10-08 low of 97.20, so it is not a level, it is a number. Rejected
  rather than tightened. Watchlist.

## [06:11 ET] REJECTED — STLD — Friday printed a rejection bar straight into the entry
- Awaiting-entry level 245.5 (published 2026-10-10, never filled). Last 240.54.
- Reports **Mon 2026-10-19 amc**, consensus EPS 5.508 on $6.57B.
- Friday's bar is the problem: open 243.64, **high 248.92, close 240.54** — a wide-range
  reversal closing near the low, and it happened exactly at the 245.5 entry. The 10/05 high
  of 245.185 is the resistance the entry is trying to clear and Friday failed it.
- Beat record is modest, not a 20%-move record: +2.72% (Jun-26), -2.14% (Mar-26), +5.52%
  (Dec-25), +1.82% (Sep-25). Revisions improving but only +1.7pts, bullish 63.6%.
- Insiders: 0 open-market buys.
- Why rejected on levels: honest stop is 231.0, below the 10/07-10/08 lows (233.265/232.97)
  = 14.5 points = 2.08 ATR, fine. But the only real resistance above is the 288.74 120-day
  high, 20% away. A 276.5 target clears 2.0 R:R and is not a level; the 288.74 target that
  *is* a level needs a 7-ATR move on a +2% average beat record. Neither version is honest.
  Watchlist with a trigger: reclaim and hold above 248.92 after Monday's print.

## [06:14 ET] POSITION UPDATE — SMMT — opened 2026-10-09 @17.1, last 14.63, -14.4%
**This is the most urgent position in the book: 14.63 is 0.23 above the 14.4 stop, which is
0.20 of a 1.161 ATR. It is one ordinary day from stopping out.**
- prior_context listed last 15.37 (-10.1%); that was Thursday. **Friday closed 14.63**
  (open 15.39, high 15.41, low 14.56) — it made a new low and closed on it.
- Breakdown is 4 sessions old: 17.13 (10/12) -> 15.52 -> 15.13 -> 15.37 -> 14.63, -14.6%.
  Below the 20-day (16.49) and the 50-day (15.68). -34.67% off the 22.395 120-day high.
  ATR 1.161 = **7.94% of price** — a gap straight through 14.4 is an ordinary day here.
- Read the primary documents, and they explain the tape:
  - **8-K filed 2026-09-29 (event 2026-09-28)**: AstraZeneca Holdings B.V. is buying
    108,955.3686 Class A Convertible Preferred at $18,356.14 each for **$2.0B gross**.
    Each preferred converts to 1,000 common, implying **$18.3561 per common share.**
    Conversion is blocked until (a) HSR expires and (b) the charter authorises enough
    common. If the share increase is not effective within **18 months**, Summit must
    **redeem the preferred for cash** at a price tied to market value — a $2B cash call.
    Also a separate clinical-trial collaboration on sone-ve + ivonescimab, with no design,
    timing or data disclosed.
    source: https://www.sec.gov/Archives/edgar/data/1599298/000119312526405776/d178892d8k.htm
  - **PRE 14A filed 2026-10-06**: Proposal 1 doubles authorised common from 1,000,000,000
    to **2,000,000,000** to cover the 108,955,369 conversion shares plus the ATM. Record
    date 2026-10-01. **The meeting date is still a placeholder — "[●], 2026" at
    "[9:00 a.m.]" ET.** So there is no dateable catalyst.
    source: https://www.sec.gov/Archives/edgar/data/1599298/000119312526415755/d126889dpre14a.htm
- So the stock is **20.3% below the price a strategic buyer paid three weeks ago**, and the
  reason is a 109M-share supply overhang that cannot clear until a vote nobody can date.
- decision: **HOLD, stop UNCHANGED at 14.4, do not add, do not average down.** The stop was
  set 2.33 ATR below entry and is about to do its job; widening it to avoid the loss is the
  error this whole report is built to refuse. No amendment to any level.
- forward view: do NOT re-enter after the stop-out until the special meeting has a date and
  Proposal 1 has passed. The AZ price of 18.3561 is the valuation reference for later.
- action: captured via add_candidate.py with levels unchanged, conviction cut 4 -> 3, and an
  honest win_probability of 0.12 — below the 0.313 baseline for its 2.19 R:R. That is a
  negative expectancy on purpose: at 0.23 above the stop this is no longer a buyable idea,
  and I would rather state the real number and let 2d enforcement demote it to the
  watchlist than dress it up to survive.

## [06:15 ET] VENUE CHECK — FAILED. Robinhood's own product pages are unreachable.
- https://robinhood.com/us/en/support/articles/futures-contracts-available-on-robinhood/ -> **HTTP 404**
- https://robinhood.com/us/en/support/articles/cryptocurrencies-available-on-robinhood/ -> **HTTP 404**
  (this is the exact URL config/universe.md tells me to verify against)
- https://robinhood.com/us/en/support/futures/ -> **HTTP 404**
- WebSearch found no Robinhood-published contract list. The only source naming /MBT and /MET
  for Robinhood is metrotrade.com, a competitor's comparison page — marketing material, not
  the venue's own list. CME confirms MBT and MET exist as products (0.10 coin per contract)
  but CME listing something says nothing about whether Robinhood carries it.
  sources: https://www.metrotrade.com/robinhood-futures-trading-vs-metrotrade-compared/ ,
  https://cmegroup.com/markets/cryptocurrencies/micro-bitcoin-and-micro-ether-options.html
- Consequence, per non-negotiable #1 (verify at runtime, do not guess from memory): **no
  futures or event-contract recommendation today.** I cannot confirm a single contract is
  offered. Today's candidates are limited to US-listed equities and ETFs, where tradeability
  is not in genuine doubt.

## [06:16 ET] REJECTED — ETH short — the view is real but I cannot express it legally
- The divergence is measured and genuine, via the ETFs since no BTC/ETH daily history source
  works today: ETHA 61.29 (10/05) -> 54.51 (10/16) = **-11.1%**, while IBIT 48.56 -> 46.15 =
  **-5.0%**. ETH underperformed BTC by ~6 points in nine sessions.
  ETHA is below its 20-day (59.04) and under its 50-day (54.85), -13.29% off its 62.87
  120-day high, ATR 3.55%. IBIT is -6.56% off its high and still ABOVE its 50-day (44.10).
  Spot confirms the same ranking: BTC -0.46% on the day, ETH -0.48%, but SOL -1.22%,
  XRP -2.33%, DOGE -2.28%, ADA -3.33%, LINK -2.97%, AVAX -3.56%. Majors least hit, high-beta
  alts hit 2-4x harder — risk-off inside crypto, not rotation.
- Why rejected: config/universe.md is explicit that a bearish crypto view must be a short
  futures contract, because Robinhood Crypto cannot short at all and a spot `sell` makes no
  money if I am right. /MET is the correct instrument and I could not verify Robinhood
  offers it (see the venue check above). An unverifiable instrument is not tradeable, and a
  spot `sell` would be a recommendation that cannot profit. Dropped rather than mis-expressed.

## [06:16 ET] DATA GAP — no crypto daily history at all
- `history BTC-USD` fails on every source: nasdaq no rows, yahoo HTTP 429, twelvedata and
  alphavantage no api key, stooq no rows. `BINANCE:BTCUSDT` also fails.
- So there is no BTC or ETH ATR, 20-day or 50-day available today. Crypto levels could only
  be set by proxy off IBIT/ETHA, which is good enough to measure a divergence but not good
  enough to site a stop on the underlying. No crypto candidate captured.

## [06:17 ET] POSITION UPDATE — XLE — opened 2026-08-15 @63.9, last 68.24, +6.8%
- prior_context showed 66.56 (+4.2%); Friday added **+2.52% to 68.24, a 120-day-high close**
  (the 68.29 range high IS Friday's high). SPY -1.11% and QQQ -2.50% the same day.
- 61.54 (9/29) -> 68.24 (10/16) = +10.9% in 13 sessions, holding the 20-day (63.92) and
  50-day (63.54) every session since 10/01. relstrength vs SPY +5.74% 1m, +14.93% 3m,
  +16.55% 6m — leading on all three windows.
- decision: **HOLD, levels unchanged (target 70.5, stop 60.8). Do not add, do not chase.**
  This is XLE's 4th appearance in 10 days and I am not re-pitching it as a new entry.
- the one new instruction: **the whole sector reports into the last 3.3% of this trade** —
  HAL Tue bmo, BKR Wed amc, VLO Thu bmo, XOM + SLB Fri. Target is 1.7 ATR away, stop is
  5.6 ATR away, so the remaining reward is small and the open risk is not. Exit into the
  Friday XOM/SLB cluster if 70.5 has not printed by then rather than hold through five prints.
- macro fit: 10y 5.10% vs 3.88% effective funds. Energy is the one sector this rate regime
  pays rather than discounts, which is also why QQQ fell 2.5% on the same tape.

## [06:18 ET] SCREEN — week-ahead earnings names, levels feasibility
Pulled 120d history on five names reporting next week. Recorded because four of the five
fail on *arithmetic*, not on story, and that is the finding:
- NFLX 70.53 | ATR 1.65 (2.34%) | sma20 70.32 sma50 75.09 | -25.52% off 94.70 high, +8.37%
  off 65.08 low. Reports Tue amc. Below the 50-day, deeply de-rated.
- NOC 519.86 | ATR 11.93 | sma20 495.19 sma50 526.18 | -12.56% off 594.51. Reports Tue bmo.
- LMT 552.09 | ATR 10.72 (1.94%) | sma20 516.62 sma50 543.16 | -9.90% off 612.75. Thu bmo.
  Above both MAs — the best structure of the five after ISRG.
- ISRG 426.70 | ATR 10.91 | sma20 411.16 sma50 391.67 | -9.95% off 473.86. Tue amc. TAKEN.
- CMCSA 21.90 | ATR 0.51 | sma20 21.63 sma50 24.12 | -22.64% off 28.31. Thu bmo.
- **The structural reason most of these fail:** with ATRs near 2% of price and prices 10%
  below their 120-day highs, a 2.0 ATR stop plus a 2.0 R:R floor demands a target roughly
  4+ ATR up, which lands at or above the prior high. LMT is the clearest case — stop below
  the 516 20-day from a 552 market entry is 3.36 ATR of risk and needs a 624 target against
  a 612.75 high. That is not a reason to tighten the stop; it is the floor doing its job,
  and it is why today is a short list.

## [06:19 ET] ISRG — NEW IDEA, captured. Earnings Tue 2026-10-20 amc, est EPS 2.6956 / $2.96B
- beat +9.79% / +16.77% / +9.86% / +18.71% over four quarters, averaging **+13.8%**.
- analysts improving: 72.5% bullish (+2.5pts), 13 strong buy / 16 buy / 10 hold / 1 sell.
- relstrength +11.25% 1m and +20.82% 3m vs SPY (+11.16 / +17.97 pts); vs XLV +6.57% / +9.86%.
  BUT 6m is -9.06% vs SPY +7.48% and XLV +18.76% — a 27.8pt six-month deficit. The bear case
  is "dead-cat bounce"; the answer is that the bounce is 3 months old, has led XLV throughout
  and sits on four double-digit beats.
- insiders checked and do NOT support it: 0 open-market buys in 6 months, 35 sells worth
  $8.08M. At this market cap that is comp flow, so it is recorded as neutral, not negative.
- short interest UNAVAILABLE — `market_data.py short ISRG` read-timed out on api.nasdaq.com.
- levels, stop set first: 387 is below the 389.11 (10/05) / 391.39 (10/02) double bottom and
  below the 391.67 50-day. Entry 413 = the 10/07-10/08 shelf (closes 414.52 / 415.41) on the
  411.16 20-day. Risk 26.0 = 2.38 ATR. Target 468, just under the 473.86 120d high. R:R 2.12.
- action is **WAIT**: do not buy before Tuesday's print; buy 411-416 on the reaction, and if
  it gaps above 435 the entry is void because the 473.86 high is then too close to pay 2.0.

## [06:20 ET] POSITION UPDATE — TLT SHORT — opened 2026-09-24 @79.9, last 80.05, flat
- decision: **HOLD, stop UNCHANGED 82.0, target unchanged 75.7.** Do not add.
- macro case intact and it is the dominant fact today: 10y 5.10% and 2y 4.77% (both
  2026-10-15), effective funds 3.88%, 10y-2y **+0.35** (2026-10-16). 122bp of the long end
  is term premium on a positively sloped curve.
- tape is against it short-term: TLT 77.11 (10/05) -> 80.05 (10/16), **+3.8% in 8 sessions**,
  gapped up 10/15 (open 80.47 vs 78.89 prior close), and has reclaimed the 20-day 78.76.
  Still below the 50-day 80.73.
- the discretionary exit, stated so it is not a surprise: a weekly close above the 80.73
  50-day means the short is wrong before the 82.0 stop is reached.
- counter-argument answered: Friday was QQQ -2.50% with TLT +0.10%, which looks like duration
  being bought as a hedge. But a growth scare FLATTENS the curve and this curve is steep at
  +0.35. The 8-session rally is a 3.8% retracement inside an 8.82% drawdown from 87.79.

## [06:21 ET] POSITION UPDATE — SNX — opened 2026-09-19 @260, last 246.75, -5.1%
**The second position inside half an ATR of its stop. 4.25 above 242.5 = 0.44 of a 9.633 ATR.**
- prior_context showed 255.14; **Friday closed 246.75** (low 245.29) — a new low, closed on it.
- The fundamentals got BETTER and the stock fell anyway, which is the finding:
  **10-Q filed 2026-10-01** for the quarter ended 2026-08-31 beat consensus EPS by **19.60%**
  (5.68 vs 4.7493) — the 4th straight beat after +15.97%, +41.62%, +1.69%.
  source: https://www.sec.gov/Archives/edgar/data/1177394/000162828026064256/snx-20260831.htm
- Price spiked to 279.40 on the 10/01 report, then fell every leg: 281.46 (10/02) -> 246.75,
  **-12.3% in 11 sessions.** Below the 20-day 268.90 and the 50-day 261.72, -17.4% off 298.77.
- Insiders: 0 open-market buys in 6 months, **79 sells worth $15.13M**, and six Form 4s filed
  10/06 for 10/05 transactions — the week it topped. Weak evidence on its own, but not a bid.
- analysts 82.4% bullish, revisions FLAT.
- **Published stop was too tight from the start**: 17.50 of risk from 260 is 1.82 ATR, under
  the 2.0 stock floor in config/strategy.md. Worth flagging to 2b/2d as a pre-existing defect
  rather than something to fix by moving the stop now.
- decision: **HOLD, stop UNCHANGED 242.5, no adding, no averaging down.** Re-entry condition:
  reclaim and hold the 261.72 50-day. Captured with an honest win_probability of 0.08 against
  a 0.325 baseline — a deliberate negative expectancy, so 2d demotes it to the watchlist.
  That is the correct outcome for a position 0.44 ATR from its stop.

## [06:22 ET] OPEN BOOK SWEEP — all 17 positions marked to Friday's close
Fetched levels for every open position so nothing is left unreviewed. No new candidate for
the ones below: nothing material changed and re-pitching them would be the anchoring the
prior-context guard warns about.
| sym | last | sma20 | sma50 | ATR | ATR% | off 120d high | read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLE | 68.24 | 63.92 | 63.54 | 1.332 | 1.95 | -0.07% | updated above, at the high |
| GE | 313.83 | 312.88 | 330.44 | 6.735 | 2.15 | -19.29% | updated above, earnings Mon |
| UNP | 289.04 | 277.58 | 287.75 | 4.259 | 1.47 | -8.53% | updated above, earnings Thu |
| TLT | 80.05 | 78.76 | 80.73 | 0.837 | 1.05 | -8.82% | updated above |
| SNX | 246.75 | 268.90 | 261.72 | 9.633 | 3.90 | -17.41% | updated above, 0.44 ATR from stop |
| SMMT | 14.63 | 16.49 | 15.68 | 1.161 | 7.94 | -34.67% | updated above, 0.20 ATR from stop |
| DG | 134.36 | 124.15 | 124.42 | 3.944 | 2.94 | **-1.24%** | strongest in the book: 8% above both MAs, +34.9% off its low, 1.2% off the 120d high. Entry 134.5, so it has only just filled. Hold, target 155, stop 125.6 (2.26 ATR, R:R 2.30). No change needed. |
| PFE | 29.58 | 28.34 | 27.97 | 0.574 | 1.94 | **-1.00%** | above both MAs, +25.2% off its low, 1% off the high. long_term, no stop, target 42. Working. Hold. |
| XLF | 55.52 | 54.45 | 56.28 | 0.696 | 1.25 | -5.26% | +2.4%. Regional banks report Mon (FITB, ZION, WAL, WTFC) and COF/KEY Tue — the catalyst is inside the trade. Risk 1.43 = 2.05 ATR, fine. Hold; 4x recommended already, so no re-pitch. |
| FCX | 69.54 | 71.72 | 72.04 | 2.638 | 3.79 | -13.33% | +1.9% but now BELOW both MAs. Risk from entry 4.85 = 1.84 ATR, under the 2.0 stock floor — same pre-existing defect as SNX. Watch. |
| CEG | 271.37 | 273.81 | 275.69 | 16.700 | **6.15** | -17.47% | -0.2%, below both MAs. Risk from entry 22.0 = **1.32 ATR** on a 6.15% ATR name — much the tightest stop in the book relative to its own volatility. Flagging to 2b/2d; not fixing by moving a stop today. |
| HII | 272.00 | 265.99 | 285.41 | 7.405 | 2.72 | -26.75% | +3.8%, above the 20-day, below the 50-day. long_term, no stop, target 430. Hold. |
| BCC | 76.13 | 75.31 | 77.85 | 2.075 | 2.73 | -13.91% | ~flat vs the 76.5 entry. long_term, no stop, target 110 (+44%). With the 10y at 5.10% and mortgage rates following it, a building-products long needs its invalidation condition restated — and note the book also holds a pending ITB short at 89.8, which is the opposite housing bet. Not resolved today; flagged. |
| KHC | 23.68 | 22.96 | 24.24 | 0.571 | 2.41 | -15.70% | +3.0%, above the 20-day. Hold. |
| LULU | 97.10 | 96.97 | 106.74 | 3.198 | 3.29 | -34.69% | short +3.5%, price sitting exactly on the 20-day 96.97 with the 50-day 9.9% above. Working. 4x recommended — no re-pitch. |
| NKE | 37.13 | 35.46 | 37.55 | 1.228 | 3.31 | -22.07% | short +3.3%, but price is back ABOVE the 20-day 35.46 and at the 50-day 37.55. Weakest of the two shorts. 4x recommended — no re-pitch. |
| IYR | 97.39 | 96.15 | 100.06 | 1.368 | 1.40 | -9.97% | short +0.4%, flat. Risk 2.6 = 1.90 ATR, clears the 1.8 ETF floor. Hold. |

## [06:24 ET] LMT — NEW IDEA, captured. Earnings Thu 2026-10-22 bmo, est EPS 7.5112 / $20.69B
- The move that made me look: **504.02 (10/13) -> 522.23 -> 532.64 -> 552.09 (10/16, high
  553.14)**, +9.5% in four sessions, closing near the high on a day SPY fell 1.11%.
- I would not publish a 4-day 9.5% move without a mechanism, so I searched for one. It is
  specific: Lockheed is scaling missile/munitions production — a ~$14.7B award placed with
  Boeing to **triple PAC-3 MSE seeker output**, a **$300M Texas** missile-production
  investment, and a stated plan to add **6,000 US jobs**. Smaller awards in the same window:
  $117.1M Army (Apache radar interferometer support, running to 2031-10-12) and $208.96M
  Navy (AN/SLQ-32(V)6 EW modification). Q4-26 dividend set at $3.60.
  sources: https://www.benzinga.com/markets/large-cap/26/10/62376990/lockheed-martin-supercharges-us-missile-production-with-300-million-texas-investment ,
  https://www.fool.com/investing/2026/10/14/why-lockheed-martin-stock-popped-today/ ,
  https://www.gurufocus.com/news/9121979/lockheed-martin-lmt-secures-1171m-us-army-contract-for-apache-helicopter-radar-support
- Independent corroboration of the date: reporting also says Q3 is due 2026-10-22, matching
  the fetched calendar.
- **Source caution, recorded rather than used:** the ad-hoc-news.de pages in those results
  give a 52-week range of 437.25-692.00 and "26.82% below yearly high", which does not
  reconcile with my fetched 120-day range of 487.15-612.75. They read as auto-generated.
  **Every price and level in the candidate comes from the fetched candle data, not from
  these pages** — I took only the contract, dividend and date facts from the news sources.
- The counter-argument has a name and a number: **Bernstein cut its PT to $564 on
  funding-delay worries** — 2.2% above Friday's close, i.e. a covering analyst who thinks
  it is already fair value. Vertical Research has it a buy.
- analysts: bullish share **46.4%, +7.1pts** in four months, improving — the lowest bullish
  base of anything I screened today, so the upgrade cycle is a long way behind the price.
  surprises +10.51% / -5.20% / +28.99% / +8.18%.
- relstrength +2.60% 1m, +8.35% 3m vs SPY (+2.51 / +5.50 pts); vs XLI +3.34% / +14.17%.
  6m is -6.77% vs SPY +7.48% — same shape as ISRG, a de-rated name three months into a turn.
- insiders: 0 open-market buys, 9 sells worth **$117.6K** — trivial. Neutral, not negative.
- levels, stop set first: **503** is below the 504.02 (10/13) low that launched the move and
  below the 497.00-498.73 shelf (10/07-10/08). Entry **532** = the top of the unfilled gap
  between the 10/14 high 523.08 and the 10/15 open 531.00, and the 10/15 close 532.64.
  Risk 29.0 = **2.71 ATR**. Target **602** = one ATR below the 612.75 120d high, which is the
  only overhead reference in the fetched window, so the target does not need the high to
  print. **R:R 2.41.**
- action is **WAIT and do not chase**: a breakout entry above 553.14 fails the floor outright
  (risk 4.7 ATR against a 612.75 ceiling), so if the gap never fills the trade does not happen.
- correlation noted: HII is already open on the defense driver, and GD is also re-rating
  (326.63 on 10/07 -> 344.23, +5.4%, bullish share 66.7% and +6.1pts). That is 2 of the 3
  allowed on one driver, so GD was NOT also captured.

## [06:24 ET] REJECTED — GD — a second helping of the same driver
- Strong in its own right: 344.23 Friday (high 344.95), up 5.4% from 326.63 on 10/07, bullish
  share 66.7% and +6.1pts improving, -14.0% off its 400.00 120-day high, reports Thu 10-22 bmo.
- Rejected on the correlation cap, not on merit. HII is already open on defense and LMT was
  captured today; a third would make the report one bet on the appropriations cycle with
  extra steps. If LMT's gap entry never fills, GD is the substitute.

## [06:25 ET] SELF-CHECK — recomputed every captured candidate from source
CLAUDE.md says the model is undisciplined about its own arithmetic, so I recomputed R:R,
stop distance in ATRs, the 1/(1+R:R) baseline and the evidence-kind count for all of them
rather than leaving it to 2b. Two inconsistencies were mine and are now fixed:
- **SMMT** was conviction 3 against 3 distinct evidence kinds, which supports 4. Rather than
  inflate the score I removed the `valuation_anchor` entry — the AstraZeneca mark is a reason
  to look again after the vote, not a confirmation for holding a position 0.2 ATR from its
  stop. Now 2 kinds, conviction 3, consistent.
- **XLE** carried a 0.72 win probability against a 0.320 baseline, +40 points, which
  strategy.md calls a large claim needing the thesis to carry it. It is not an edge claim at
  all: from 68.24 the target is 1.70 ATR away and the stop 5.59 ATR away, so even a driftless
  walk touches the target first 7.44/(7.44+2.26) = 77% of the time. The baseline is computed
  from a 63.9 entry this position passed two months ago. Said so explicitly in the thesis.
Final state, all recomputed from fetched ATRs:
| sym | conv | kinds | R:R | stop ATRx | floor | wp | baseline | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GE | 4 | 3 | 2.06 | 2.38 | 2.0 | 0.40 | 0.327 | clean |
| UNP | 4 | 3 | 2.45 | 2.63 | 2.0 | 0.38 | 0.290 | clean |
| XLE | 4 | 3 | 2.13 | 2.33 | 1.8 | 0.72 | 0.320 | clean |
| ISRG | 4 | 3 | 2.12 | 2.38 | 2.0 | 0.42 | 0.321 | clean |
| LMT | 4 | 3 | 2.41 | 2.71 | 2.0 | 0.40 | 0.293 | clean |
| TLT | 3 | 2 | 2.00 | 2.51 | 1.8 | 0.36 | 0.333 | clean, R:R exactly at floor |
| CMCSA | 3 | 2 | 2.61 | n/a | 2.5 R:R | 0.40 | 0.277 | long_term, bear case 17.06 |
| SMMT | 3 | 2 | 2.19 | 2.33 | 2.0 | 0.12 | 0.314 | **expectancy negative on purpose** |
| SNX | 3 | 2 | 2.08 | **1.82** | 2.0 | 0.08 | 0.324 | **stop under floor (pre-existing) + expectancy negative on purpose** |
- The two negative-expectancy entries are deliberate and should be demoted by 2d. Both are
  positions sitting under half an ATR from their stops; stating the real probability and
  letting enforcement move them to the watchlist is the honest handling, and inflating
  either to survive validation would be the exact failure mode 2b-2d exist to catch.
- SNX's 1.82 ATR stop is a **defect in the already-published position**, not something I set
  today. I did not "fix" it by moving the stop, because moving a stop on a loser to clear a
  floor is the KRE error in reverse.

## [06:26 ET] CMCSA — NEW long_term IDEA, captured. The lane got deliberate time, not leftovers.
- Trailing four-quarter EPS **3.79** from fetched reported actuals (1.04 Jun-26, 0.79 Mar-26,
  0.84 Dec-25, 1.12 Sep-25). At 21.90 that is **5.78x**. Market cap $77.7B on 3,548.64M
  shares reconciles to the price, so the multiple is on a consistent share count.
- Beat in 3 of 4: +4.46%, +5.07%, +8.05%, -0.89%. Revisions improving +4.1pts — but from a
  low base: 40.0% bullish, 21 holds and 3 sells.
- valuation anchor: target **28.40 = 7.5x trailing**, which independently lands on the 28.31
  120-day high. Bear case **17.06 = 4.5x** (-22%). Entry 20.20 = 5.33x. One method, three
  numbers, shown.
- **R:R 2.61 against the 2.5 long_term floor** — and it only clears because the entry waits
  below the 120-day low of 20.48. At the 21.90 market price with the same 17.06 bear case the
  ratio is 1.34 and the idea fails, which is why the entry is staged under 20.50 rather than
  started now. I did not soften the bear case to make a market entry work.
- invalidation (replaces a stop): trailing 4Q EPS below 3.20, or consensus missed in two
  consecutive quarters.
- **positioning deliberately NOT counted as evidence**, because the measured read is negative:
  CMCSA lags SPY on every window (-4.41% 1m, -7.91% 3m, -26.09% 6m vs +0.09/+2.85/+7.48) and
  lags XLC by 2.60/7.48/18.72 points. Zero insider buys in 6 months — and zero sells, so no
  signal either way at 5.8x. Counting a negative positioning read as a confirmation of a long
  would be dishonest, so conviction is **3 on two kinds**, not 4 on three.
- the lane's record is in key_risk: long_term is 0/4 on target, avg -15.2%. Hence 2% and thirds.

## [06:26 ET] REJECTED — NFLX — a falling knife, not a de-rating
- 70.53, -25.52% off the 94.70 120-day high, below the 50-day 75.09, reports Tue 10-20 amc.
  Looked like the best de-rated large cap on the board until the record came back.
- **Missed four quarters running**: -0.52% (Jun-26), -10.15% (Mar-26), -0.50% (Dec-25),
  -17.39% (Sep-25). Revisions **deteriorating**, bullish share 74.1% and -3.5pts.
- Trailing 4Q EPS 2.647 (0.80+0.70+0.56+0.587) -> 26.6x at 70.53 on a $293.7B cap. So it is
  down 25% and still not cheap, while the estimates it is missing keep coming down. No anchor
  and no positive confirmation. Rejected outright, not watchlisted as a buy.

## [06:28 ET] SCREEN — 15 Tue-Thu reporters, structure first. Two passed, both then failed.
Screened GM, RTX, NOC, COF, TXN, LRCX, IBM, T, HON, URI, CSX, NSC, PG, NEM, MMM on whether
price holds both the 20- and 50-day. Only IBM and PG did; the rest were above the 20-day only
(GM, RTX, NOC, COF, HON, CSX, NSC, NEM) or below both (TXN, LRCX, T, URI, MMM).
- LRCX is worth recording for context: 263.94, **-39.81% off its 332-equivalent high**, ATR
  5.23%, far below both MAs. The semi de-rating that stopped MU out on 10-15 is still running.

## [06:29 ET] REJECTED — IBM — revisions are falling off a cliff into Wednesday's print
- 232.14, above the 20-day 226.33 and just over the 50-day 232.03, -30.18% off the 332.46
  120-day high. Reports **Wed 2026-10-21 amc**. The drawdown leaves plenty of overhead room,
  which is exactly what PG lacks, so the arithmetic would have worked.
- Killed by positioning: bullish share **51.6%, down 9.1 points** in four months, revision
  direction **deteriorating** (8 strong buy / 8 buy / 13 hold / 2 sell). Surprises are mixed
  and the most recent is a **miss**: -2.28% (Jun-26), +4.73%, +3.60%, +7.28%.
- Friday was a reversal bar like STLD's: high 236.98, close 232.14, -2.0% off the day's high.
- relstrength -2.36% 1m vs SPY, +8.99% 3m, -8.42% 6m (-27.29 vs XLK over 6m). Insiders: 0
  buys, one sale of $5.76M.
- A sharp downgrade cycle plus a miss plus a reversal bar, two sessions before earnings, is
  three reasons not to be long it. Rejected, not watchlisted as a buy.

## [06:29 ET] REJECTED — PG — no overhead reference, so no honest target
- 159.35, **-0.39% off its 120-day high** (~159.97), 6.6% above the 20-day 149.41 and 8.5%
  above the 50-day 146.87, +14.76% off its low. ATR 2.64 (1.65%). Reports Thu 10-22 bmo.
  A defensive staple leading the tape fits today's macro perfectly.
- Rejected on the same arithmetic as VLO: at the high there is no overhead level to site a
  target on. A 2.0 ATR stop is 5.28, so a 2.0 R:R needs +10.56 = 169.91, above the 159.97
  high — an invented number. And the only real pullback level, the 149.41 20-day, is 6.2%
  below the market, too far to fill inside a swing. Nothing honest to publish; watchlist.

## [06:30 ET] AWAITING-ENTRY REVIEW — AAL, and what I did not reach
- `AAL` SELL_SHORT @13.35 (published 2026-10-03): **drop it.** Last 11.88, so the market went
  11.0% the right way without ever filling the entry, and it is now below both the 20-day
  (12.98) and the 50-day (13.42). Re-pitching a short at 13.35 would need an 12.4% rally
  first; shorting 11.88 instead, two days before **Thu 2026-10-22 bmo** earnings with a
  -0.3639 consensus EPS already priced, is chasing a move that is over. ATR 0.4401, so the
  2.0 ATR floor alone is 0.88 of a stop on an 11.88 stock after a -11% slide.
- `STLD` and `ABT` reviewed and rejected above, with triggers for the watchlist.
- **NOT REACHED this run** — recorded as a gap, not as a judgement: `VST` BUY @132,
  `GLD` SELL @406.77, `OXY` BUY @54, `ITB` SELL_SHORT @89.8, `CVS` BUY @93, and the two event
  contracts `KXFEDDECISION-26OCT-H25` YES @28 and `KXCPIYOY-26SEP-T3.5` NO @18. The event
  pair could not be marked at all — see the event-contract gap at 06:21.

## [06:30 ET] NEWS — regional banks are NOT being paid for the steeper curve
Screened the four banks reporting Mon 10-19 amc, because a +0.35 10y-2y curve with the 10y at
5.10% is the textbook setup for regional net interest margin, and the tape disagrees:
- FITB 50.37 — below both MAs (s20 51.02, s50 53.52), -15.34% off high, +7.63% off low
- ZION 63.37 — above the 20-day only (62.93), below s50 66.39, -13.59% off high, +7.42% off low
- WAL 74.51 — below both (s20 75.55, s50 78.12), -12.89% off high, **+4.51% off low**
- WTFC 144.08 — above the 20-day only (143.98), below s50 149.99, -13.84% off high, +4.23% off low
- (CLF 12.12, reporting Mon bmo, below both MAs, ATR 5.42% — no edge, skipped)
- **Read, and it matters for the open XLF position:** every one of the four sits 13-15% below
  its 120-day high and only 4-8% above its low, while XLF is only -5.26% off its high and
  above its 20-day. XLF's strength is coming from the money-centre and capital-markets names,
  not from the regionals. A steeper curve is not being rewarded here, which is what you would
  expect if the market is pricing credit and securities-book marks ahead of margin. No new
  candidate taken — but it is a reason not to add to XLF into Monday's regional prints.

## [06:31 ET] RESEARCH COMPLETE
- **candidates: 9 distinct** (11 rows in candidates.jsonl; SMMT and XLE were each re-captured
  after my own self-check, and synthesis takes the last entry per symbol).
  - **Position updates (6)** — the first obligation, with 17 positions open:
    `GE` hold into Mon earnings, stop held at 292 | `UNP` hold, earnings Thu now dated |
    `XLE` hold at a 120-day high, exit into the Fri XOM/SLB cluster if 70.5 has not printed |
    `TLT` hold the short, 50-day at 80.73 is the discretionary exit |
    `SNX` hold, 0.44 ATR from the stop, honest wp 0.08 |
    `SMMT` hold, 0.20 ATR from the stop, honest wp 0.12
  - **New ideas (3)**: `ISRG` buy 411-416 after Tue's print (R:R 2.12, conv 4) |
    `LMT` buy the 528-536 gap, do not chase (R:R 2.41, conv 4) |
    `CMCSA` long_term, accumulate in thirds under 20.50 (R:R 2.61, conv 3)
- **rejections logged, 9**: VLO (no honest target at the high), PG (same), ABT (no honest
  stop), STLD (Friday reversal bar into the entry), IBM (revisions -9.1pts), NFLX (four
  straight misses, still 26.6x), GD (correlation cap — defense already has LMT + open HII),
  AAL (the move happened without us), ETH short (correct instrument unverifiable).
- **skew, stated rather than apologised for:** 6 updates to 3 new ideas, and 8 of 9 are
  equities/ETFs with no futures, no crypto and no event contract. On a Saturday that is the
  opposite of what config/strategy.md's weekend guidance expects, and the cause is not a thin
  tape — it is that all three weekend-tradeable venues were unverifiable or unpriceable today
  (see the gaps). Equities are therefore week-ahead prep, entries for the Mon 2026-10-19 open
  or later, as marked in each `catalyst.action`.
- **why the list is short:** a recurring arithmetic wall, logged at 06:18. With ATRs near 2%
  of price and most names 10% below their 120-day highs, a 2.0 ATR stop plus the 2.0 R:R
  floor demands a target ~4+ ATR up, which lands at or above the prior high. VLO, PG and LMT
  on a breakout all failed exactly there. That is the floor working, not a thin day.
- **drivers are spread** — Mon aero earnings (GE), Thu rails (UNP), the energy complex (XLE),
  Tue medtech (ISRG), Thu defense (LMT), the rate path (TLT), a multiple re-rating (CMCSA),
  and two management instructions (SNX, SMMT). No more than one idea per driver.

### coverage gaps — what I could not check
- **Event contracts: total loss.** `events` returns count 0 for FEDDECISION, CPI, Bitcoin and
  recession; "Fed" returned one irrelevant tennis market. No implied probability could be
  quoted, so no event candidate was possible AND the two open event positions
  (KXFEDDECISION-26OCT-H25, KXCPIYOY-26SEP-T3.5) could not be marked to market.
- **Robinhood venue verification: total loss.** All three product URLs 404, including the one
  config/universe.md names. No futures or event recommendation could be made responsibly.
- **Crypto levels: total loss.** No daily history from any source for BTC-USD or
  BINANCE:BTCUSDT, so no ATR, 20-day or 50-day. Spot prices and the IBIT/ETHA proxies were
  available and are quoted, but a stop cannot be sited on a proxy.
- **Index and volatility levels.** ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, DXY, WTI and gold futures
  all failed (yahoo HTTP 429, finnhub index subscription required, stooq 404 on caret
  symbols, no alphavantage key). **There is no VIX level in this report.** ETF proxies
  (SPY/QQQ/IWM/TLT/GLD/XLE) were used instead and are all previous-close, session closed.
- **Options-implied moves: unavailable for every name.** `implied` returns HTTP 401 from
  yahoo-options. No idea's target was checked against the straddle, including five sitting in
  front of earnings. This is the single biggest hole in today's level-setting.
- **Inflation.** macro's `cpi_yoy` returns 336.298, the Sep-2026 CPI *index level*, not a
  year-over-year rate. No inflation rate is quoted anywhere in this report.
- **Short interest.** api.nasdaq.com read-timed out on ISRG; not retried for others.
- **History depth.** `history --days 120` returns correct 120-day aggregates (ATR, SMAs,
  range high/low) but only ~20 bars in `recent`. So resistance *between* the current price
  and the 120-day high cannot be sited, which is why ISRG, LMT and STLD all had to anchor
  targets to the range high or one ATR below it. Stated in each candidate's evidence.
- **7 awaiting-entry names not reviewed**: VST, GLD, OXY, ITB, CVS and the two event contracts.
- **Open positions reviewed but not re-pitched**: DG, PFE, XLF, FCX, CEG, HII, BCC, KHC, LULU,
  NKE, IYR — all marked to Friday's close in the 06:22 sweep.

### two defects in already-published positions, flagged for 2b/2d rather than fixed here
- `SNX` stop 242.5 is **1.82 ATR** from its 260 entry, under the 2.0 stock floor.
- `CEG` stop 250.0 is **1.32 ATR** from its 272 entry on a name with a 6.15% ATR — the
  tightest in the book relative to its own volatility.
- `FCX` stop 63.35 is **1.84 ATR** from its 68.2 entry, also under the floor.
I did not move any of them. Widening a stop on a live position to make it pass a floor is the
KRE error run backwards, and all three were set when the positions were published.

### sources that failed
- query1/query2.finance.yahoo.com — HTTP 429 on all index and crypto history
- query1.finance.yahoo.com/v7/finance/options — HTTP 401 (every implied-move call)
- finnhub index quotes — "Market data subscription required for CFD indices"
- stooq.com — 404 on caret index symbols, no rows for BTC-USD
- api.nasdaq.com — read timeout (short interest)
- Kalshi market search via market_data.py events — returns 0 matches for every useful topic
- robinhood.com/us/en/support/articles/futures-contracts-available-on-robinhood/ — 404
- robinhood.com/us/en/support/articles/cryptocurrencies-available-on-robinhood/ — 404
- robinhood.com/us/en/support/futures/ — 404
- twelvedata, alphavantage — no API key configured
### sources that worked
- finnhub: quotes, 120-day candles/ATR/SMA, earnings calendar, recommendation trend and
  surprise record, insider transactions, company profile
- FRED: 10y, 2y, fed funds, 10y-2y curve, unemployment
- SEC EDGAR: SMMT 8-K and PRE 14A, SNX 10-Q, filings index
- CoinGecko: spot crypto prices
- WebSearch / WebFetch: LMT contract and production news, SMMT filing contents
