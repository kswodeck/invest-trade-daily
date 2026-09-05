# Research log — 2026-09-05

## [06:03 ET] SETUP
- Saturday 2026-09-05. US equities and futures CLOSED. Per config/strategy.md weekend behavior:
  crypto + event contracts carry the actionable lane; equities are week-ahead prep priced off
  Friday's close (2026-09-04), marked swing, entry for next open (Mon 2026-09-08).
- Labor Day was Mon 2026-09-07? No — Labor Day 2026 is Mon 2026-09-07. VERIFY: if so, next
  US equity open is Tue 2026-09-08.

## [06:03 ET] MACRO — rates, curve, policy
- US10Y 4.77% (2026-09-03), prev 4.79 — source: FRED DGS10
- US2Y 4.34% (2026-09-03), prev 4.39 — source: FRED DGS2
- Fed funds effective 3.63% (2026-09-03), unchanged — source: FRED DFF
- 10y-2y curve +0.41 (2026-09-04), prev +0.43 — source: FRED T10Y2Y
- Unemployment 4.1% (2026-08-01), unchanged — source: FRED UNRATE
- CPIAUCSL 332.813 (2026-07-01) vs 332.568 prev
- NOTE the shape: fed funds 3.63% but 10y at 4.77% and 2y at 4.34%. Both 2y and 10y sit ABOVE
  the policy rate, and the curve is positively sloped by 41bp. Market is pricing term premium /
  no near-term easing, or inflation risk. This is a bear-steepener-ish regime, matters for TLT.
- TLT 82.21 close 2026-09-04 (finnhub, session closed, age 841min) — the only equity print macro got.

## [06:03 ET] DATA QUALITY — Yahoo Finance is 429 rate-limited this run
- FAILED via all sources: ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES/NQ futures, DXY, ^TNX, gold, WTI.
- finnhub returns "Market data subscription required for CFD indices" for index symbols.
- Consequence: no index level, no VIX, no DXY, no futures print this run unless another path works.
  Will price index views off ETF proxies (SPY/QQQ/IWM/GLD/USO) via finnhub instead, and say so.

## [06:09 ET] DATA QUALITY — `market_data.py events` returns all-null prices (source bug, not a market gap)
- Kalshi renamed its market price fields. The API now returns `yes_bid_dollars`,
  `yes_ask_dollars`, `last_price_dollars`, `open_interest_fp`, `volume_24h_fp` (decimals,
  0.00-1.00), where `market_data.py` reads `yes_bid`/`yes_ask`/`last_price`/`volume`.
  Result: every event contract prints `None` for every price.
- Second bug: `events "<kw>"` filters only the first unsorted page of /markets (40 rows of
  sports shards), so every macro keyword returned count=0. Series must be queried by
  `series_ticker`.
- Workaround used this run: direct GET
  https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=<SERIES>&status=open
  and read the `_dollars` fields. All event prices below came from that call at 06:07 ET.
- FOR SYNTHESIS: put this in data_quality_notes. It is a code bug worth fixing — event
  contracts are an explicitly wanted lane and they are currently unpriceable through the CLI.

## [06:10 ET] MACRO — THE REGIME: the market prices a coin-flip Fed HIKE on Sep 16
Kalshi KXFEDDECISION, quotes 06:07 ET Sat 2026-09-05 (market open 24/5-ish; these are
Friday-evening-quality quotes). Series resolves on the FOMC decision date.
- **Sep 16, 2026 FOMC** (KXFEDDECISION-26SEP, closes 2026-09-16):
  - Hike >25bp: 1/2c   | Hike 25bp: **49/50c** | Hold: **48/50c** | Cut 25bp: 0/1c | Cut >25bp: 0/1c
  - open interest is real: H0 9.85M, C25 5.92M, H26 6.18M, H25 3.81M contracts; 24h vol H0 1.16M
- **Oct 28, 2026 FOMC**: Hike25 26/27c, Hold 68/69c, Cut25 4/5c
- **Dec 9, 2026 FOMC**: Hike25 39/43c, Hold 48/50c, Cut25 4/7c
- Read: a ~50% chance of a hike in 11 days, and cumulatively the market has more hike than
  hold priced by December. Cuts are priced at ~1-5c, i.e. off the table.
- Cross-check against FRED: fed funds effective 3.63%, 2y 4.34%, 10y 4.77%. The 2y sitting
  71bp ABOVE the effective funds rate is the cash market saying the same thing the event
  market is: the next move is up, not down. These two independent sources agree.
- **This is the single most important fact of the day and it should frame the whole report.**
  Consensus positioning built over 2025-26 has been "the Fed cuts eventually". It is not
  what is priced anymore.

## [06:11 ET] MACRO — CPI is the trigger, and it prints Fri Sep 11
Kalshi KXCPIYOY-26AUG (August CPI YoY, closes 2026-09-11) — the distribution:
- Above 3.0%: 96/99c | Above 3.1%: 93/96c | Above 3.2%: 87/90c | **Above 3.3%: 53/61c**
- Above 3.4%: 18/23c | Above 3.5%: 3/7c | Above 3.6%: 0/2c | Above 4.0%: 0/1c
- Implied consensus: August CPI lands **3.3% YoY** (the 3.3 strike is the coin-flip).
  Tails are thin: only ~20% above 3.4%, essentially nothing above 3.6%.
- FRED CPIAUCSL 332.813 (Jul) vs 332.568 (Jun) = +0.074% m/m NSA, so the level series is
  not obviously accelerating m/m; the 3.3% YoY is a base-effect/level story.
- So: inflation ~3.3% against a 2% target, policy rate 3.63% => real policy rate ~0.3%.
  That is the arithmetic behind the hike pricing.
- **CPI Sep 11 08:30 ET is the dated catalyst that resolves the Sep 16 FOMC coin flip.**

## [06:12 ET] MACRO — recession pricing contradicts the hike pricing, mildly
- KXRECSSNBER-26 (recession STARTS in 2026): 5/6c, OI 894k
- KXRECSSNBER-27 (recession in 2027): 25/26c, OI 163k
- So the market sees a hiking Fed into a 4.1% unemployment rate with only a 25% chance of
  a 2027 recession. That is the soft-landing-with-inflation trade. Coherent, but it is a
  crowded coherence — the hike path and the no-recession path are both consensus.

## [06:13 ET] MACRO — the tape itself is flat and dull
Finnhub, all Friday 2026-09-04 closes (session closed, age ~13h — the correct freshest print):
- SPY 770.19 (-0.39%) | QQQ 718.96 (+0.18%) | IWM 296.01 (+0.28%) | VIXY 17.00 (+0.30%)
- GLD 406.77 (-0.84%) | SLV 59.82 (-1.21%) | USO 141.96 (-0.09%) | XLE 64.06 (-0.87%) | TLT 82.21 (+0.17%)
- SPY history (nasdaq): ATR14 5.503 (0.71%), SMA20 769.05, SMA50 756.86, 90d range 708.37-779.37,
  1.18% off the high. Twenty sessions have gone 761.78-777.88. This is a coiled range, not a trend.
- Crypto is the one thing actually moving, and it is moving DOWN — see next block.

## [06:17 ET] NEWS — why the Fed is priced to hike (this is the missing mechanism)
- Fed Chair **Kevin Warsh** said underlying inflation trends have not "meaningfully improved"
  and that more action could be needed if inflation does not move convincingly to 2%. The
  repricing dates to ~Aug 28. — source: https://www.chase.com/personal/investments/learning-and-insights/article/september-2026-rate-hike-now-expected-amid-energy-shocks
- Two named drivers: (1) **ongoing Iran conflict** producing energy supply shocks that keep
  energy costs elevated, (2) investor doubt about the Fed's inflation credibility after the
  July hold. — same source; also https://www.marketplace.org/story/2026/08/31/will-the-fed-raise-rates-at-september-fomc-meeting
- FOMC is **Sep 15-16, 2026**, decision on the 16th. Confirms the Kalshi close date.
- CME FedWatch was reported at **~66%** for a 25bp September hike. Kalshi H25 is 49/50c.
  DO NOT trade that gap without verifying FedWatch directly — the snippet is undated and the
  two venues also differ in what they aggregate. Logged as a lead, not a signal.
- Gold: ~$4,369/oz at the start of September, **-21.8% from the Jan 28 record high**; fell ~3%
  on Aug 28 on the Warsh repricing; ~-6% over three sessions into Sep 1.
  — source: https://www.cbsnews.com/news/golds-price-down-by-over-21-percent-where-will-it-head-september-2026/
  and https://www.usagold.com/daily-precious-metals-market-report-september-1-2026/
- Yields cited in press match FRED: 10y ~4.79%, 2y ~4.35-4.39%.

## [06:18 ET] SYNTHESIS OF THE REGIME — one driver, and the correlation cap matters today
Everything above is ONE trade: **the front end is repricing to a hiking Fed on an energy-led
inflation impulse.** Long energy, short duration, short gold, short crypto, short long-duration
equity are all the SAME BET. config/strategy.md caps this at 3 ideas per driver. I will hold
to that and hunt genuinely uncorrelated ideas for the rest, rather than publish eight versions
of "the Fed hikes".

## [06:22 ET] POSITION UPDATE — TLT — the book holds a LONG and a SHORT in the same ETF
- `TLT` BUY  opened 2026-08-20, entry 82.60, target 86.20, stop 80.95 — last 82.21, -0.5%
- `TLT` SELL opened 2026-09-02, entry 81.87, target 78.30, stop 83.60 — last 82.21, -0.4%
- These are the same instrument in opposite directions. Net exposure is approximately zero and
  the book is paying spread and borrow to hold nothing. This is not a hedge, it is an
  unresolved disagreement between a 2026-08-20 view and a 2026-09-02 view.
- **decision: the long is the one that is wrong.** It was opened on a cutting-Fed premise. As
  of 06:07 ET today Kalshi prices ANY September cut at 0/1c and the 2y sits 71bp above the
  effective funds rate. The 86.20 target needs a rally the market has stopped pricing.
- **action: SELL THE FULL TLT LONG at market on the next open (Tue 2026-09-08 — Mon is Labor
  Day, verify). Keep the short.** Do not net them off in place.
- CAPTURE PROBLEM, for synthesis: candidates.jsonl is de-duplicated per SYMBOL (last entry
  wins), so emitting a second TLT candidate with direction `buy` would silently overwrite the
  short captured at 06:20. I have therefore NOT captured the close as its own candidate — it
  is written here and folded into the TLT short's scale_plan instead. **Synthesis must carry
  the "sell the TLT long" instruction into the report explicitly.** It is the single highest-
  value housekeeping action available today.

## [06:23 ET] POSITION UPDATE — GLD — long at 398 with a 520 target, into a hiking Fed
- `GLD` BUY opened 2026-08-22, entry 398.00, target 520.00, no stop — last 406.77, +2.2% vs entry
- Gold is ~$4,369/oz, **-21.8% from the Jan 28 2026 record high**, and fell ~3% on Aug 28 on
  the Warsh repricing alone. GLD 120d: last 406.77, ATR14 8.615 (2.12%), SMA20 409.89,
  SMA50 388.88, 180d range 363.32-509.70.
- The 520 target is above the 180-day high. It is a bull-case number set before the regime
  changed, and rising real rates are the textbook headwind for a non-yielding asset.
- **decision: hold the position but CUT THE TARGET to 462.21 (the 120-day high, a level the
  tape has actually traded) and set an invalidation at a close below 388.88 (SMA50).** The
  position is +2.2% and gold above its SMA50 in a debasement regime is still a legitimate
  long; a 520 print inside this Fed is not a forecast, it is a leftover.
- Not yet captured — needs the R:R arithmetic below before it is publishable.

## [06:06 ET] TIMESTAMP CORRECTION
The blocks above are stamped 06:03-06:23 from my own estimate of elapsed time. The wall clock
says 06:06. The findings and all fetch times are correct; the stamps above run fast by up to
17 minutes. Everything below this line is stamped from `date`.

## [06:13 ET] POSITION UPDATE — LULU — *** THE URGENT ONE: -17.4% on Friday, thesis broken ***
- `LULU` BUY opened 2026-08-22, entry 115.00, target 180.00, **no stop** — recommended **5x in
  the last 10 days**, the single most repeated name in the book.
- prior_context.md shows this position at 121.77, +5.9%. **That is stale by one session.**
  Friday 2026-09-04 close is **100.61, -17.38% on the day** (finnhub + nasdaq history agree).
  The position is **-12.5% vs the 115.00 entry**, not +5.9%.
- What happened: Q2 reported 2026-09-03 (8-K and 10-Q both filed 09-03, fetched from SEC EDGAR
  https://www.sec.gov/Archives/edgar/data/1397187/000139718726000126/lulu-20260903.htm).
  **Third guidance cut of 2026.** Revenue -4% YoY to $2.4B vs $2.46B consensus; comparable
  sales **-9%**, Americas comps **-12%**; FY revenue guided $10.35-10.5B vs $11.03B consensus;
  FY EPS guided down to $9.48-9.73 from $10.95-11.15. The $2.92 adjusted EPS "beat" included
  $0.86 of tariff refunds — ex-that it was $2.06.
  — sources: https://www.fool.com/coverage/stock-market-today/2026/09/04/stock-market-today-sept-4-lululemon-plummets-17-after-slashing-guidance/
    and https://finance.yahoo.com/markets/stocks/articles/lululemon-stock-drops-18-8-020500072.html
- Analyst trend (finnhub) confirms the break rather than a wobble: bullish share **20% -> 5%**
  since June (strong_buy+buy 8 of 39 in June, 2 of 40 in September); sell+strong_sell 1 -> 7.
- Levels: 100.61 last, ATR14 6.096 (6.06%), SMA20 118.92, SMA50 118.40, SMA200 152.77,
  200d range 97.99-225.98, **-55.5% off the high and at an 8-year low**.
- **decision: EXIT. Sell the full LULU long at market on the next open.**
- The arithmetic that settles it: from the filled 115.00 entry, the smallest stop this report's
  own rules permit for a swing stock is 2.0 ATR = 12.19, i.e. 102.81. Friday closed at 100.61.
  **Had this position carried the mandated stop it would already have been closed.** It only
  still exists because it was published without one. There is no version of the risk/reward
  from 115.00 that clears the 2.0 floor, which is exactly why it should not be held.
- The 180 target implied ~18.6x the NEW guidance midpoint and was set against the OLD numbers.
  It is a leftover, not a forecast.
- **This is the anchoring failure the repetition guard exists to catch, caught one session too
  late.** Five publications in ten days on a name that had already cut guidance twice in 2026.

## [06:15 ET] POSITION UPDATE — NKE — hold, do not re-pitch, target is too high but the stop is moot
- `NKE` BUY opened 2026-08-17, entry 40.75, target 62.00, no stop — last **38.40** (-5.8%).
- Nothing has happened since it was opened. No filing, no guidance, no news. Next catalyst is
  **Q1 FY27 earnings Thu 2026-10-01 ~16:15 ET**, outside a swing horizon from here.
  — source: https://www.tipranks.com/stocks/nke/earnings
- Context: -38% year to date; FY26 revenue $46.40B (+0.19%), net income $3.11B (-3.45%).
  finnhub analyst trend **deteriorating**: bullish share 39.1%, -9.8pp; but it has **beaten EPS
  4 of the last 4 quarters**. Street 12-month target $50.46, well below the report's 62.
- Levels: ATR14 1.056, SMA20 39.83, SMA50 41.51, SMA200 51.42, 200d low 37.95. Below all three
  moving averages and sitting on the 200-day low.
- **decision: HOLD, and stop republishing it.** Two things make this a hold rather than an
  action: (1) the 2.0 ATR stop from the 40.75 entry sits at 38.64 and the stock is at 38.40,
  so a correctly-stopped version is ~0.6% through — inside the noise, not a decisive break like
  LULU; (2) there is no new information to act on either way.
- **It also does not clear the bar to be republished as a fresh idea, and I am not capturing
  one.** Re-framed as long_term with an honest bear case (~$31, roughly 1x sales on 1.48B
  shares) the reward-to-risk from the 40.75 filled entry is (62-40.75)/(40.75-31) = 2.18,
  under the 2.5 long-term floor. Kept as a position; not re-recommended. The 62 target is a
  leftover and the reader should treat the street's ~50 as the realistic anchor.

## [06:16 ET] POSITION UPDATE — CCJ / BCC / SVRA — hold, nothing changed
- `CCJ` BUY 2026-08-17, entry 94.00, target 135.00, no stop — last 100.74, **+7.2%**.
  ATR14 4.272 (4.24%), SMA20 99.85, SMA50 95.39, SMA200 105.37, -25.5% off the 135.24 high.
  Above the 20 and 50 day, below the 200. Note the 135.00 target is the exact 200-day high —
  a round trip, not a new-high call. **decision: hold, no change.** No filing or news this week.
- `BCC` BUY 2026-08-18, entry 76.50, target 110.00, no stop — last 79.21, **+3.5%**.
  ATR14 2.463, SMA20 80.93, SMA50 79.08, SMA200 77.10, -13.9% off the 91.97 high. Holding above
  the 50 and 200 day. ADV only $25M — thin for the size, worth remembering on exit.
  **decision: hold, no change.**
- `SVRA` BUY 2026-08-23, entry 5.35, target 8.00, stop 4.60 — last 5.37, **+0.4%**.
  ATR14 0.193 (3.59%), SMA20 5.48, SMA50 5.65, SMA200 5.58, ADV $8M. Last SEC filings are the
  2026-08-11 10-Q and an S-8; no 8-K, no clinical or FDA news since entry.
  **decision: hold, no change.** The stop at 4.60 is 0.75 from entry = 3.9 ATR, correctly wide
  for a micro-cap biotech. This is the one position in the book carrying a properly sized stop.
- `SPY` SELL_SHORT 2026-08-31, entry 773.00, target 750.00, stop 782.00 — last 770.19, **+0.36%**.
  ATR14 5.503 (0.71%), SMA20 769.05, SMA50 756.86. Stop 782 is 9.00 from entry = 1.64 ATR,
  **below the 1.8 ATR ETF swing floor** — it was published too tight and should not be tightened
  further. Target 750 is just under the SMA50 at 756.86, a level the tape has traded.
  **decision: hold.** The Fed-hike repricing is a live reason for the short to work and the
  index is 1.2% off its high in a 20-session 762-778 coil. Do not add: SPY and the TLT short
  are the same bet and the correlation cap is already tight today.

## [06:16 ET] REJECTED (kill these stale awaiting-entry orders) — BTC / /MBTU6
- `BTC` SELL @ 63,400 (published 2026-08-16) and `/MBTU6` SHORT @ 64,340 (published 2026-08-18)
  are both stale by 26%. Bitcoin was ~62,800 on 2026-08-17 and is **79,627 now** (coingecko,
  06:02 ET). It ran to ~79,000 by 08-27 and has held 77-81k since. **Cancel both orders.** A
  resting short 20%+ below the market is not a trade waiting to happen, it is a stale order that
  will only ever fill on the way to being right for a day and wrong for a year.

## [06:18 ET] THE CENTRAL ANALYTICAL FACT — headline and core have split by ~100bp, and it is all energy
Computed from FRED, not quoted from anywhere:
- **Headline CPI YoY, July 2026 = 3.30%** (CPIAUCSL 332.813 / 322.169 - 1). Market prices
  August at 3.3% (the 3.3 strike is the 53/61c coin flip).
- **Core CPI YoY, July 2026 = 2.47%** (CPILFESL 336.789 / 328.682 - 1). Market prices August
  core at ~2.3-2.4% (T2.3 62/66c, T2.4 24/32c) — i.e. core DECELERATING.
- So the market expects a ~95bp headline-over-core gap, and expects it to widen.
- The energy source of it, from FRED weekly regular gasoline (GASREGCOVW): August weekly prints
  3.935 / 3.864 / 3.919 / 3.949 / 3.916, average **$3.917**, against a July average of ~$3.797
  — **+3.2% m/m**. WTI (DCOILWTICO) 91.48 on 2026-09-01 vs an August average in the mid-80s.
- **This is the report's most useful single observation: the Fed is priced ~50% to hike on a
  headline number produced by an oil supply shock, while core sits near target.** Central banks
  conventionally look through supply shocks; Warsh is explicitly not, on credibility grounds.
  Whatever one thinks of that, it is the fault line every trade today sits on.

## [06:20 ET] REJECTED — the core-CPI event trade — I checked for an edge and there is not one
This is the falsification step, written down because a plausible-looking mispricing that
dissolves on arithmetic is worth as much as a trade.
- Candidate: KXCPICOREYOY-26AUG-T2.3 "core above 2.3%", 62 bid / 66 ask, OI 4,377, 24h vol
  3,787 — genuinely liquid. Resolves on the August CPI release **2026-09-11**.
- Fetched the actual rule rather than assuming it: resolution is on **the one-decimal-place
  value published by BLS**, and the strike is "increases by MORE than 2.3%". So YES needs a
  published 2.4%, which needs a true YoY of >=2.35%, which needs core m/m **>= +0.1954%**.
- Core m/m from CPILFESL, eleven clean months (Oct-2025 is missing from FRED — the print gap):
  +0.313 +0.310 +0.218 +0.233 +0.295 +0.216 +0.196 +0.376 +0.208 **-0.017** +0.215.
- A naive count says 10 of 11 clear the threshold => 91%, which would make 66c a huge edge.
  **That count is wrong**, because it throws away the size of the June miss. Mean +0.233,
  sd 0.101; z = (0.1954 - 0.233)/0.101 = -0.373; **P = 64.5%**.
- The market is 62/66. Fair value 64.5% sits inside the spread. **There is no edge. No trade.**
- The lesson worth keeping: the threshold is only 0.37 sd below the mean, so this is close to a
  coin flip, and a base-rate count made it look like a lock. The single -0.017 June print is the
  whole distribution.
- The September CPI markets (KXCPIYOY-26SEP, closes 2026-10-14) would capture the September oil
  spike and are the more interesting question — but they are **untradeable on liquidity**:
  T3.4 is 54/97, T3.5 is 39/94, T3.3 is 61/88, on open interest under 350. Paying a 30-50 cent
  spread destroys any edge that might be there. Noted and rejected on execution, not on view.

## [06:21 ET] REJECTED — the Bitcoin year-end event contracts — priced about right
- BTC 79,627 (coingecko 06:02 ET), -1.75% 24h. 2026 high **96,899 on Jan 15**, 2026 low
  **58,566 on Jul 1**, started the year at 87,575 — so BTC is **down ~9% YTD** and has never
  touched 100k this year, which is why these contracts are still live.
- KXBTCMAXY-26DEC31-99999.99, 27 bid / 28 ask, OI 349,888. Fetched the rule: it is a **TOUCH**
  market, not a terminal one — "is above $99,999.99 starting 01/02/2026 06:00 PM and before
  Dec 31, 2026 11:59 PM ET". That is worth far more than a year-end-close market and is exactly
  the kind of detail that has to be read rather than assumed.
- Realized vol computed from 365 days of coingecko daily closes: 30d **46.4%**, 60d 39.0%,
  90d 36.8%, 180d 38.1%, 364d 44.3%.
- Barrier-touch probability, martingale in price (drift = -sigma^2/2), T = 117 days = 0.3205y,
  barrier 100,000 from 79,627:
  | sigma | P(touch 100k) | P(touch 110k) |
  | 35% | 22.3% | 8.7% |
  | 40% | 28.0% | 13.0% |
  | 45% | 33.0% | 17.3% |
  | 50% | 37.4% | 21.5% |
  | 60% | 44.6% | 28.8% |
- **At the 60-180 day realized vol of 37-39%, fair value is 26-28% and the ask is 28c. Fair.**
  Only if you use the 30-day 46.4% does it look cheap (fair ~34c), and one month of vol after a
  26% ten-day rally is the least reliable estimate available.
- The 110k contract is the opposite: 18c ask against 13.0% fair at 40% vol — **overpriced**, but
  buying NO at 83c to capture ~4c of expectancy locks capital for four months and the whole edge
  is inside my vol uncertainty (35% vol makes NO worth 91c, 45% makes it 83c). **No trade.**
- And the drift assumption cuts the wrong way for YES: the martingale calc assumes zero drift,
  while a Fed repricing toward a hike is a headwind for the highest-beta risk asset there is.
  Real P(touch) is likely BELOW the table. **No crypto event trade today.**
- No directional crypto trade either. Robinhood Crypto cannot short, so a bearish view would
  have to go through /MBT futures, and I do not have a view strong enough to justify a leveraged
  contract - BTC is mid-range between its 58.6k July low and its 96.9k January high.

## [06:22 ET] DURABLE MISPRICING — US natural gas is $2.90 and the rest of the world pays ~$25
This is the largest dislocation I found today and it is structural, not a headline.
- **Henry Hub spot $2.90/mmbtu** on 2026-09-01 (FRED DHHNGSP); monthly average $2.78 in August,
  $2.89 July, $3.15 June — versus **$7.72 in January 2026** (MHHNGSP).
- **Asian spot LNG ~$25/mmbtu**, up >140% from a ~$10 pre-crisis level; Dutch TTF above
  EUR60/MWh. Qatar's LNG exports are **down 96%**, removing >10 bcf/d — about **20% of global
  LNG supply** — mostly from Ras Laffan. Kpler has moved its base case to a prolonged crisis
  with transit constrained **through end-2026**, recovering in Q1 2027.
  — sources: https://www.eia.gov/todayinenergy/detail.php?id=67604 ,
    https://www.kpler.com/blog/global-lng-and-natural-gas-prices-surge-as-us-and-iran-resume-hot-war ,
    https://www.azernews.az/region/262917.html
- That is roughly an **8x spread between the US wellhead and the Asian cargo**.
- **REJECTED — EQT and AR as the way to own it.** EQT 55.17 (-19.2% off its 120d high of 68.24),
  AR 39.41 (-13.9% off). It is tempting to read the lag as opportunity. It is not: Appalachian
  producers sell into Henry Hub at $2.90 and capture none of the $25, because the binding
  constraint is liquefaction capacity, not gas. **Their underperformance is correct pricing, and
  buying them on an LNG headline is buying the wrong end of the trade.** Writing this down so
  synthesis does not resurrect it.
- The spread accrues to whoever owns the toll booth between the two prices. That is Cheniere.

## [06:24 ET] DIVERGENCE — oil moved 9.5% in five sessions and energy equities moved 2.2%
Both series from nasdaq daily closes, same five sessions (2026-08-28 to 2026-09-04):
- **USO 129.70 -> 141.96, +9.45%.** Now 7.6% above its SMA20 (131.94) and **14.6% above its
  SMA50** (123.88), 7.9% off the 120d high. WTI itself (FRED DCOILWTICO) 84.57 on 08-28 ->
  **91.48 on 09-01**.
- **XLE 62.68 -> 64.06, +2.20%.** Only 1.9% above its SMA20 (62.87) and 8.2% above its SMA50
  (59.20), 2.2% off the 120d high of 65.52.
- So the commodity took the Sep 1 escalation almost fully and the equities took about a quarter
  of it. XLE still leads the index handily (+10.14% 1m vs SPY +0.21%) — it is not that energy
  is out of favour, it is that the last leg has not been passed through.
- The honest counter, which belongs in the idea: energy equities deliberately do NOT capitalise
  a war premium at face value, because a war premium is the most mean-reverting kind of oil
  price there is. Some of this gap is correct pricing, not a lag. That is why the target is set
  near the top of the recent range rather than extrapolating the full 9.5%.
- XLE has been published 3x before (open order BUY @ 63.00 from 2026-08-15, never filled).
  **What changed:** the Sep 1 US-Iran escalation, the reimposition of the US naval blockade, and
  a $6.91 move in WTI, none of which existed when 63.00 was set. Re-pitching at a revised level.

## [06:26 ET] PROCESS FINDING — all seven unfilled long orders sit 4-14% BELOW the market
Quotes 06:25 ET, Friday closes, against the published limit:
| Symbol | Published | Order | Last | Order is |
| `VST`  | 2026-08-24 | 128.00 | 149.30 | **-14.3%** below market |
| `PFE`  | 2026-08-18 |  25.80 |  28.45 | -9.3% |
| `DG`   | 2026-08-21 | 121.00 | 133.21 | -9.2% |
| `CEG`  | 2026-08-21 | 272.00 | 298.96 | -9.0% |
| `LCII` | 2026-08-18 |  94.00 | 102.60 | -8.4% |
| `DINO` | 2026-08-22 |  99.50 | 105.41 | -5.6% |
| `EEM`  | 2026-08-21 |  65.60 |  68.70 | -4.5% |
| `IYR`  | 2026-09-02 | 103.60 (SELL_SHORT) | 102.14 | +1.4% above market |
- **Every long idea published in the second half of August was right about direction and never
  got filled**, because each entry was set below the market and the market went up. This is not
  seven separate misses, it is one systematic habit — the pullback-entry reflex CLAUDE.md
  already names: 31 pullback entries against 1 breakout in the first month, 42% ever filled,
  and the ones that filled were the ones falling.
- `IYR` is the same error mirrored: a short entry ABOVE the market only fills once the trade has
  first gone against you.
- **recommendation: cancel the five most stale (VST, PFE, DG, CEG, LCII — all 8%+ away).** A
  resting bid 14% under the market is not patience, it is an order nobody will ever be filled on
  except in a crash, at which point the thesis that justified it is gone anyway.
  `EEM` (-4.5%) and `DINO` (-5.6%) are inside a normal pullback and can stand.
- **This is why the XLE idea above raises its level instead of restating 63.00 for a fourth time.**

## [06:27 ET] POSITION UPDATE — the three open Fed event-contract orders contradict each other
- `KXFEDDECISION-26SEP-H25` YES @ **32** (published 2026-08-22) — market now **49 bid / 50 ask**
- `KXFEDDECISION-26SEP-H0`  YES @ **47** (published 2026-09-03) — market now **48 bid / 50 ask**
- `KXFEDDECISION-26OCT-H25` YES @ **28** (published 2026-09-02) — market now **26 bid / 27 ask**
- The first two are **YES on a hike and YES on a hold at the same September meeting**. They are
  mutually exclusive by the contract's own rules ("This market is mutually exclusive... Only one
  bucket, at maximum, can resolve to Yes"). Holding both is buying the whole distribution for
  more than a dollar. The same unresolved-disagreement problem as the TLT long against the TLT
  short.
- **recommendation: cancel all three.** Not because the direction is wrong but because there is
  no longer a price disagreement to trade: the September hike bucket is at 50c and the hold
  bucket is at 50c, which is the market saying it does not know, and I do not know better. The
  32c entry on H25 was a good call that the market has since paid out on paper — it just never
  filled. Chasing it at 50c is buying a coin flip after the information arrived.
- The October hike at 26/27c is reachable at the 28 order, but the meetings are strongly
  correlated (a soft Sep 11 CPI kills the hike at BOTH meetings), so it is not the independent
  second bet it looks like. Cancel.

## [06:28 ET] REJECTED — Cheniere (LNG) as the way to own the gas dislocation
- LNG 292.00, ATR14 7.2305 (2.48%), SMA20 279.02, SMA50 265.99, SMA200 240.34,
  400d range 186.20-300.89, **-2.95% off the high**, +56.8% off the low. ADV $500M.
- The thesis was attractive: own the toll booth between $2.90 Henry Hub and $25 Asian LNG.
- **Rejected on two counts.** (1) Crowding: finnhub has **92.9% of analysts bullish** — 26 of 28
  at buy or strong buy, flat for four months, with two holds and no sells. There is nobody left
  to upgrade it. (2) The mechanism is weaker than the headline: Cheniere's capacity is largely
  sold forward on fixed-fee take-or-pay terms, so it collects a liquefaction fee rather than the
  spot spread, and the eye-catching Q2 EPS of $14.65 against a $3.07 estimate sits next to a Q1
  of **-$16.75 against +$4.23** — those are derivative marks swinging, not cash margin on
  cargoes. A 377% "beat" followed by a 496% "miss" is one number telling you nothing.
- Kept in the notes because the underlying dislocation is real and durable; the instrument is
  the problem, not the idea. If it pulls back to the SMA50 near 266 it becomes interesting again.

## [06:30 ET] REJECTED — Adobe (ADBE) — the right kind of idea at the wrong price, and the floor says so
The long_term lane wants exactly this shape — a high-margin business de-rated on a problem that
may or may not be fixable — so it got a real look rather than a glance.
- ADBE 266.51, **-6.7% on Friday 2026-09-04** (285.75 -> 266.51) after naming Anil Chakravarthy,
  a long-time internal executive, as CEO. The market read it as the wrong background for the
  problem: his record is enterprise data and marketing software, furthest from the creative
  tools where the generative-AI threat is sharpest.
  — source: https://247wallst.com/investing/2026/09/04/adobe-sinks-7-as-internal-ceo-pick-lands-ahead-of-earnings-workday-falls-4/
- Down ~26-28% year to date and 28.1% off the 250-day high of 370.86; two consecutive down
  calendar years on the same fear. Q1 FY2027 earnings **2026-09-10 amc** (fetched calendar).
- Levels: ATR14 10.4808 (3.93%), SMA20 274.12, SMA50 248.85, SMA200 267.93, 250d range
  190.12-370.86, ADV $1.29bn.
- Positives that made it worth the time: **one open-market insider purchase, $1.945M by David A.
  Ricks** (six sells totalling $18.9M against it, so not a cluster); recent relative strength
  turning (+2.41% 1m vs QQQ +0.60%) after a dreadful six months (-6.03% vs QQQ +19.88%).
- **Valuation, method shown:** the last four quarterly actuals are 5.96 / 6.06 / 5.50 / 5.31 =
  **$22.83 trailing**, so at 266.51 the stock is on **11.7x**. A re-rating to 14x gives **$320**.
  The bear case is that AI genuinely erodes Creative Cloud, earnings go sideways at ~$22 and the
  multiple compresses to 9x = **$198**, which is close to the 190.12 the tape actually traded
  this year — so it is a real level, not a scare number.
- **Reward-to-risk = (320 - 266.51) / (266.51 - 198) = 53.49 / 68.51 = 0.78, against a 2.5
  long_term floor. It fails, and it fails by a mile.** Cheap on the multiple is not the same as
  cheap against the bear case, and the floor exists to catch exactly that confusion.
- It would clear the floor at an entry near **230** ((320-230)/(230-198) = 2.81). I am **not**
  capturing that as a candidate, because a limit 13.7% under the market is precisely the stale
  pullback order I criticised four blocks up. It goes on the watchlist as a level to revisit if
  the September 10 print takes it there.

## [06:31 ET] CORRELATION AUDIT — what is actually independent in today's list
Written explicitly because today has one dominant driver and the 3-per-driver cap is easy to
breach without noticing.
- **Energy supply shock (Hormuz):** `XLE`, `FRO` — 2 ideas. At the cap once `TLT` is counted as
  a descendant of the same shock (energy -> headline CPI -> Fed hike pricing). **I stopped
  adding energy ideas here.** Rejected on these grounds rather than on merit: refiners (DINO),
  airlines as a fuel short, LNG, and the natural gas producers.
- **Fed/rates:** `TLT` short. `GLD` is the deliberate other side of the same variable and is
  flagged as such in its own key_risk. `SPY` short (held, not re-captured) is a third.
- **Genuinely independent:** `ORCL` (AI capex financing, Sep 10 print), `LULU` (an exit).
- A reader should understand that if the Strait of Hormuz reopens next week, `XLE` and `FRO`
  both gap against the stop, `TLT` short loses its driver, and `GLD` is the only thing in the
  book that benefits. That concentration is the honest shape of today's tape, not an oversight.

## [06:32 ET] RESEARCH COMPLETE
- **candidates: 6** (TLT sell, LULU exit, GLD, FRO, XLE, ORCL) — all fully specified with
  levels drawn from fetched price history, all sourced.
- **The frame for synthesis:** the market has stopped pricing a Fed that cuts and started
  pricing one that HIKES on Sep 16 (Kalshi 49/50c, cuts at 0-1c, 2y 71bp above effective funds),
  driven by an energy shock that has headline CPI at 3.3% while core sits at 2.3-2.4%. Sep 11
  CPI is the trigger. Everything else follows from that.
- **Actions that matter more than the new ideas, and must survive into the report:**
  1. **SELL THE LULU LONG** — -17.4% Friday on a third guidance cut; prior_context still shows
     it at +5.9%, which is one session stale.
  2. **SELL THE TLT LONG**, keep the TLT short — the book holds both and nets to nothing.
  3. **Cancel the three Fed event orders** — two of them bet on opposite outcomes of the same
     meeting, and both buckets now trade at 50c.
  4. **Cancel the five stale limits** (VST, PFE, DG, CEG, LCII), all 8-14% under the market.
- **coverage gaps:**
  - **Small and micro caps were not hunted at all.** This is the real gap today and it is not a
    data problem, it is a time allocation: position management on nine open positions plus a
    17% one-day loss on one of them took the budget. Nothing under $2bn was screened.
  - No intraday ideas — it is Saturday and there is no session to trade.
  - Robinhood availability of the Kalshi contracts discussed was NOT verified against
    Robinhood's own prediction-markets list; since no event contract was captured, nothing
    depends on it, but do not let one through synthesis without that check.
  - `market_data.py short` timed out on FRO, so no short-interest read on any tanker.
- **sources that failed:**
  - **Yahoo Finance 429 on everything** — no index level, no VIX, no DXY, no ES/NQ futures print
    this run. Priced index views off ETF proxies via finnhub and said so.
  - **finnhub returns "Market data subscription required for CFD indices"** for ^GSPC/^NDX/^DJI/^RUT.
  - **`market_data.py events` is broken twice over** (renamed Kalshi price fields, and keyword
    search that only scans the first unsorted page). Every event price in these notes came from
    a direct API call instead. Worth fixing — event contracts are a wanted lane and are
    currently unpriceable through the CLI.
  - `market_data.py implied` returns 401 from Yahoo options, so **no options-implied move was
    available for any idea today** — the "is the target inside what the market prices" check
    could not be run on FRO, XLE or ORCL.
  - `quote CTRA` failed; `short FRO` timed out.

## [06:34 ET] AMENDMENT to RESEARCH COMPLETE — the small-cap gap was partly closed after all
The 06:32 block listed "small and micro caps were not hunted" as the day's coverage gap. Time
remained, so they were hunted. **The outcome is that none cleared the bar** — which is a
different and better answer than "not looked at", so the gap note above is superseded by this.

### The screen
Every name on the fetched 14-day earnings calendar with a dated catalyst inside the next ten
sessions and a sub-$2bn or beaten-down profile, priced from nasdaq daily history:
| Sym | Last | ATR% | SMA200 | 200d high | off high | ADV |
| AVAV | 144.65 | 5.22 | 212.47 | 408.25 | **-64.6%** | $178M |
| FPS  |  31.35 | 5.80 |   n/a  |  66.00 | -52.5% | $200M |
| PLAY |   8.72 | 6.06 |  13.49 |  22.10 | -60.5% | $13M |
| OXM  |  30.87 | 6.23 |  38.66 |  49.58 | -37.7% | $11M |
| SHOE |  14.07 | 4.96 |  17.24 |  21.61 | -34.9% | $10M |
| LUXE |   7.72 | 4.44 |   8.32 |  11.38 | -32.2% | **$1M** |
| ASO  |  44.94 | 3.54 |  52.36 |  62.45 | -28.0% | $69M |
| SIG  |  85.30 | 3.37 |  88.66 | 104.56 | -18.4% | $57M |
| AVO  |  12.68 | 2.72 |  12.83 |  15.53 | -18.4% | $8M |
| SAIL |  18.82 | 5.87 |  16.01 |  21.96 | -14.3% | $59M |
| CBRL |  54.69 | 4.13 |  36.99 |  60.26 |  -9.2% | $43M |
- `LUXE` fails the universe liquidity floor outright at ~$1M average dollar volume.

### REJECTED — AVAV — the one that looked like the trade, and is not
A drone and loitering-munition maker down 64.6% from its high **during an active US-Iran war**
is the most counterintuitive chart on the screen, so it got the work. The market is not being
slow; it is pricing real damage:
- FY2027 guidance is revenue **$2.125-2.225bn** but EPS of only **$0.16-0.48** — at 144.65 that
  is roughly **300-900x forward earnings**. Whatever this is, it is not cheap.
- Q3 FY2026 was a **$3.15 loss per share**, net loss widening ~$155M year on year, with revenue
  missing estimates by 14%; it has beaten in only **1 of the last 4 quarters** (0.32 vs 0.377,
  0.44 vs 0.794, 0.64 vs 0.705, 1.84 vs 1.494).
- The decline is attributed to **contract-termination fallout, accounting issues, and ongoing
  litigation**, plus dilution from the $200M Empirical Systems Aerospace acquisition of
  2026-03-16, $160M of which was paid in stock.
  — source: https://simplywall.st/stocks/us/capital-goods/nasdaq-avav/aerovironment
- **Accounting issues are where I stop.** Everything else on the list is a valuation question;
  that one is a question about whether the numbers mean anything, and it cannot be answered from
  outside before a **2026-09-09 amc** print.
- Two confirming reads point the same way: **zero open-market insider buys** in six months
  against nine sells, and the sell side at **85.7% bullish and still improving** (24 of 28 at
  buy or better, no sells) — an analyst base that has not marked to the facts is a warning here,
  not support. Same pattern as ORCL, and there it is priced into the plan.
- Not captured, at any size. A conviction-2 lottery ticket is for a thin thesis, not for a
  company with control problems reporting in four days.

## [06:35 ET] CROSS-CUTTING — the consumer is being squeezed, and the screen shows it
Not a trade, but it is the context the LULU exit sits in and synthesis should say it.
- Of the eleven names above, seven are consumer discretionary and every one is deeply de-rated:
  `PLAY` -60.5%, `OXM` -37.7%, `SHOE` -34.9%, `LUXE` -32.2%, `ASO` -28.0%, `SIG` -18.4%,
  and `LULU` itself -55.5% and at an 8-year low after a third guidance cut.
- The mechanism is on the same page as everything else in these notes: **retail gasoline
  averaged $3.92 in August, +3.2% m/m** (FRED GASREGCOVW), with WTI at 91.48 on Sep 1 — an
  energy shock is a regressive tax on exactly this cohort's discretionary budget.
- So the energy longs in this report (`XLE`, `FRO`) and the consumer wreckage are two ends of
  one transfer, and a reader should not treat the retail earnings cluster of Sep 9-10
  (`KR`, `CHWY`, `ASO`, `SIG`, `AEO`, `RH`) as independent of the oil trade. It is not.
- No short captured against it: these names are already down 30-60% with the catalyst inside
  five sessions, which is the worst moment to initiate a short.

## [06:37 ET] VENUE CHECK — FRO is genuinely Robinhood-tradeable (verified, not assumed)
`config/universe.md` excludes "most foreign ordinaries", and Frontline plc is Cyprus-domiciled,
so this is exactly the case the rule is aimed at and it was checked rather than remembered.
- Frontline's **ordinary shares are NYSE-listed under FRO** and have been since 2001-08-06
  (they also trade in Oslo). They are not an ADR and not an OTC foreign ordinary.
  — source: https://www.frontlineplc.cy/frontline-ltd-announces-approval-for-listing-by-new-york-stock-exchange-and-filing-of-registration-statement/
- Robinhood carries it: https://robinhood.com/us/en/stocks/FRO/ renders a live "Buy FRO" ticket.
- **Price discrepancy worth flagging:** the Robinhood page shows **46.69** against the 46.12
  nasdaq/finnhub Friday close I set levels from. 46.69 still sits inside the 44.50-47.30 entry
  zone so nothing needs changing, but validation should re-price from a live quote rather than
  trust either number. All other captured symbols (TLT, GLD, XLE, ORCL, LULU) are unambiguously
  Robinhood-supported US listings and were not separately checked.

## [06:38 ET] CALENDAR VERIFIED AT THE PRIMARY SOURCE — and the September meeting has a dot plot
Fetched federalreserve.gov/monetarypolicy/fomccalendars.htm rather than relying on the press:
- **Sep 15-16, 2026 — WITH a Summary of Economic Projections**
- Oct 27-28, 2026 — no SEP
- Dec 8-9, 2026 — with SEP
These match the fetched Kalshi contract close dates exactly (26SEP closes 2026-09-16, 26OCT
2026-10-28, 26DEC 2026-12-09), so the event market and the Fed's own calendar agree.
- **The dot plot matters and was not in the thesis when TLT was captured.** September is not
  just a hike-or-hold decision, it is the first published rate path since the market flipped
  from pricing cuts to pricing hikes. A 50/50 decision is one event; a 50/50 decision plus a
  revised dot plot is the whole 2027 curve getting repriced in one afternoon. That raises the
  variance on both sides of the TLT short and on `SPY`, and synthesis should say so.
- Also worth stating plainly for the reader: **Mon 2026-09-07 is Labor Day** (first Monday in
  September — Sep 1 2026 was a Tuesday), so the NYSE is shut and every "next open" instruction
  in today's candidates means **Tue 2026-09-08**.

## [06:39 ET] FINAL STATE
- 6 candidates captured, all complete: `TLT` sell (5), `FRO` buy (4), `XLE` buy (4),
  `ORCL` buy (4), `GLD` buy long_term (3), `LULU` buy (2, an EXIT instruction).
- 9 open positions all reviewed and dispositioned; 14 unfilled orders all reviewed.
- 6 documented rejections with the arithmetic shown: core-CPI event contract (no edge, 64.5%
  fair inside a 62/66 market), BTC touch contracts (fair on realized vol), Cheniere (crowded,
  wrong mechanism), Adobe (fails the 2.5 long-term floor at 0.78), AVAV (accounting issues),
  EQT/AR (wrong end of the LNG spread).
- Nothing here was truncated; this run finished with budget remaining and used it to close the
  small-cap gap the 06:32 block had reported as open.
