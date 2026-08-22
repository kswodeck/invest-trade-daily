# Research log — 2026-08-22

## [06:27 ET] MACRO — Saturday run, US equities and futures closed
Weekend run per config/strategy.md: crypto + event contracts carry actionable
weight; equities are week-ahead prep (swing, entry at next open Mon 2026-08-24).

Rates / macro (FRED, source: https://fred.stlouisfed.org/):
- US10Y 4.69% (2026-08-20); US2Y 4.19%; 10y-2y +0.50 (2026-08-21) — curve positively sloped
- Fed funds effective 3.63% (2026-08-20)
- Unemployment 4.1% (Jul 2026); CPI index 332.813 (Jul 2026)
- TLT close 82.05, -0.35% (2026-08-21 close) — long bond soft; open TLT position entered 82.60

Crypto (CoinGecko, https://www.coingecko.com/, asof 2026-08-22T10:25Z):
- BTC 76,648 (-1.69% 24h), mcap $1.538T, 24h vol $57.1B
- ETH 2,396.14 (-0.32%), mcap $289.2B
- SOL 91.62 (+0.41%)
- DOGE 0.08807 (+4.67%)
- XRP 1.45 (+5.48%), 24h vol $14.2B

DATA GAPS (record for data_quality_notes): Yahoo Finance returning HTTP 429
across the board; ^GSPC/^NDX/^DJI/^RUT/VIX/ES/NQ/DXY/US10Y-quote/gold/WTI all
FAILED. Finnhub rejects index CFDs. Stooq 404s on ^-prefixed symbols. Only
bonds_20y (TLT proxy) resolved. Index-level context is therefore unavailable
this morning — no index price is stated below unless separately fetched.

## [06:29 ET] OPEN POSITION REVIEW — 20 positions, prices are 2026-08-21 closes (Finnhub), market closed
All prices below fetched this morning; ATR figures from `market_data.py history --days 120` (source: nasdaq).

### POSITION UPDATE — /MBTU6 + BTC shorts (4 entries) — CLOSE AT MARKET, UNCONDITIONALLY
- spot BTC 76,648 (CoinGecko, 2026-08-22T10:25Z). IBIT last 43.68 vs sma20 37.00 — BTC is ~18% above its own 20-day.
- shorts: BTC sell @62,950 (08-16), BTC sell @63,400 (08-17), /MBTU6 short @64,100 (08-18), /MBTU6 short @64,340 (08-19)
- stops were 65,200 (spot) and 66,600 (futures). **Every one of them was violated days ago.** At 76,648 the
  spot shorts are ~-21% and the futures shorts ~-19% against, i.e. roughly 5x the intended risk on the futures leg.
- decision: **CLOSE ALL FOUR AT MARKET.** Not "at 66,600", not on a bounce. The stop is not a suggestion and a
  leveraged futures short that is 19% offside can lose more than the deposit.
- this was already flagged as "the most urgent action in this report" in the 2026-08-21 watchlist and the position
  is still open. Repeat it louder. **Do not re-pitch a new bitcoin short today** — four consecutive wrong shorts
  against an 18%-above-20dma tape is anchoring, not thesis.
- source: https://www.coingecko.com/en/coins/bitcoin

### POSITION UPDATE — CCJ — HOLD, continuing accumulation (open x2: 95.00, 88.00)
- last 102.51, **+7.24% on Friday 08-21** on 3.94M shares vs 2.11M Thursday — a real volume expansion, not drift
- 20d 94.24, 50d 96.14; reclaimed both. 120d range 83.15-131.21, -21.9% off the high
- ATR14 3.56 (3.47%)
- decision: HOLD both. +7.9% and +16.5% respectively. Target 135 unchanged. Set a protective stop at **93.00**
  (below the 20-day and ~2.7 ATR back) — the position had no stop at all, which was the flaw, not the target.
- cause of Friday's move not yet confirmed — see news sweep below before relying on it.

### POSITION UPDATE — XLE — HOLD x3, raise stop to 61.50
- last 63.64. Entries 60.80 (08-15), 60.50 (08-16), 60.80 (08-18). Targets 67.0 / 64.5 / 66.5.
- 120d high 64.70 — XLE is 1.64% off its own 120-day high, and the 08-16 entry's 64.50 target is within 1.4%
- 20d 60.29, 50d 57.51, ATR14 1.23 (1.94%)
- decision: **trim the 08-16 tranche into 64.50** (its stated target), hold the other two for 66.5/67.0, and raise
  the stop on all three to 61.50 — above every entry, so the whole position is now risk-free at worst.
- deliberately NOT re-pitched as a new idea: XLE has appeared 5x in 10 days. That is the repetition guard firing.

### POSITION UPDATE — TJX — CLOSE, already through the stop
- last 140.53 vs entry 150.85 (08-19), stop 145.50. -6.8%. Also stopped out on the 08-17 entry.
- 20d 154.72, 50d 156.01 — price is 9% below both. -17.3% off the 120d high of 170.00, sitting 0.9% above the
  120-day low (139.31).
- decision: CLOSE. Do not average down. TJX has been recommended 4x in 10 days and produced two stop-outs;
  **it is now on the do-not-pitch list until a new quarter of data exists.**

### POSITION UPDATE — KRE — CLOSE the remaining 08-15 long
- last 74.86 vs entry 76.80, stop 74.20. -2.5%, and the stop is 0.9% away — inside a single ATR14 (1.08).
- 20d 76.50, 50d 75.32 — below both. Two other KRE entries already stopped out on 08-19.
- decision: CLOSE rather than wait to be stopped. A position sitting inside one ATR of its stop with price below
  both moving averages has no favourable asymmetry left; taking -2.5% beats a gap through 74.20.
- KRE recommended 4x in 10 days, 2 stop-outs. Do-not-pitch alongside TJX.

### POSITION UPDATE — HD — CLOSE both
- last 335.61. Entries 340.00 (08-18) and 337.49 (08-19), stop 328.00. -1.3% and -0.6%.
- 20d 342.49, 50d 340.08 — below both. ATR14 8.88 (2.65%), so the 328 stop is well under 1 ATR away.
- decision: CLOSE. This repeats the 08-21 instruction, which was not acted on. Same reasoning: below both MAs,
  stop inside 1 ATR, recommended 3x in 10 days.

### POSITION UPDATE — LCII — CLOSE AND BOOK THE GAIN
- last 101.98, **-3.28% Friday**. Entry 94.00 (08-18), no stop, target 138.
- decision: CLOSE at +8.5%. Note this is worse than the +12.2% available when the same instruction was issued on
  08-21 and not acted on — which is the argument for acting on it now. 20d 105.51, price now below it; -26.2%
  off the 120d high with a 3.72% ATR and no stop is an unbounded position, and the 138 target was never defended.

### POSITION UPDATE — TLT — HOLD, no change
- last 82.05 vs entry 82.60 (08-20), target 86.20, stop 80.95. -0.7%.
- 20d 82.53, 50d 84.17. ATR14 only 0.657 (0.80%) — the 80.95 stop is 1.7 ATR away, correctly sized.
- 10y 4.69%, 2y 4.19%, curve +0.50 (FRED 08-20/08-21). Thesis unchanged; hold.

### POSITION UPDATE — PFE — HOLD, no change (long-term)
- last 28.07 vs entry 25.80 (08-18), +8.8%. 20d 26.30, 50d 25.36 — above both. Only -2.35% off the 120d high.
- long-term, no stop by design. Target 38.00 unchanged. Hold.

### POSITION UPDATE — DHT — HOLD, raise stop to 18.80
- last 19.82 vs entry 18.80 (08-18), +5.4%. Target 22.50, stop 17.60.
- 20d 18.80, 50d 18.26, ATR14 0.721 (3.64%). -3.9% off the 120d high.
- decision: HOLD and raise the stop from 17.60 to **18.80** — breakeven, and exactly on the rising 20-day.
  That converts a +5.4% open gain into a free option on the 22.50 target.

### POSITION UPDATE — BCC — HOLD, no change
- last 82.47 vs entry 81.00 (08-18), +1.8%. Target 92.00, stop 76.00. 20d 82.23, 50d 77.98 — above both.
- ATR14 2.95 (3.57%); the 76.00 stop is 2.2 ATR away, correctly sized. Hold.

### POSITION UPDATE — NKE — HOLD existing size, add nothing (long-term x2)
- last 40.76 vs entries 40.00 (08-17) and 38.00 (08-18). 20d 41.49, 50d 42.49 — still below both.
- **-32.2% off the 120d high of 60.11, and only 4.9% above the 120d low of 38.86.** The chart has not turned.
- decision: hold, add nothing, do not re-pitch. The 62-65 targets are a multi-year claim and the position is
  already 2x sized. Adding a third tranche to a name making lower highs is averaging into a downtrend.

## [06:31 ET] CALENDAR — week of 2026-08-24, the two events that organise everything
- **Wed 2026-08-26**: July PCE (headline + core), Q2 GDP second estimate, July durable goods — all pre-open;
  **NVDA fiscal Q2 earnings after the close** (Finnhub earnings calendar confirms NVDA 2026-08-26)
- **Thu 08-27 - Fri 08-28**: Jackson Hole symposium, topic "Financial Innovation: Implications for Payments and
  Policy". **Kevin Warsh is Fed chair and makes his Jackson Hole debut keynote on Friday 08-28.**
- annual nonfarm payroll benchmark revisions also due this week
- NVDA trading ~8% below its record high into the print
- **Brent has broken $94** (per week-ahead) — consistent with XLE sitting 1.6% off its 120-day high
- USD/JPY near 158
- source: https://www.actionforex.com/contributors/fundamental-analysis/651445-week-ahead-feds-jackson-hole-and-nvidia-earnings-to-dictate-markets/
- source: https://www.fxstreet.com/analysis/week-ahead-feds-jackson-hole-and-nvidia-earnings-to-dictate-markets-202608210946
- NOTE: a first-ever Jackson Hole keynote from a new chair whose stated brief is financial innovation/payments is
  a materially wider distribution than a Powell keynote would be. Any idea that depends on a dovish read of 08-28
  is a coin flip on an unknown speaker — size accordingly, and prefer ideas that do NOT depend on it.

## [06:31 ET] NEWS — CCJ +7.24% on 08-21 (open position), uranium sector +7.67%
- driver: nuclear/AI-datacenter baseload demand narrative, plus Westinghouse IPO optionality and US government
  funding supporting a sum-of-the-parts case. Sector-wide move, not company-specific news.
- daily high 102.53 / low 97.17, close 102.51 — closed on the high, on ~1.9x the prior day's volume
- source: https://www.tradingkey.com/news/market-movers/262125359-market-movers-ccj-20260821
- source: https://www.quiverquant.com/news/Cameco+shares+rise+as+uranium+sentiment+improves+and+long-term+contracting+remains+in+focus
- implication: this validates HOLDING CCJ but argues AGAINST adding here — a +7.2% sector-sentiment day that
  closes on the high is the worst possible entry, and CCJ is already open x2.

## [06:33 ET] EVENT CONTRACTS — hunted, and BLOCKED by a data failure. No event idea today.
> **SUPERSEDED at 06:48 — do not read this block standalone.** The prices were recovered later in the run and an
> event contract IS recommended. See "CORRECTION — EVENT PRICES RECOVERED". The diagnosis below is still
> accurate as a description of the `market_data.py events` bug; only the conclusion changed.
Series located and confirmed live on Kalshi (which backs Robinhood Prediction Markets):
- `KXFEDDECISION-26SEP-*` (Sep 2026 FOMC: C25/C26/H0/H25/H26), `KXFED-26SEP-T*` (funds upper bound)
- `KXCPIYOY-26AUG-T2.5..2.9`, `KXCPI-26AUG-T*`, `KXWTI-26AUG2514-T90.49..93.99` (WTI settle Aug 25)
- `KXU3-26NOV-T*`, `KXRECSSNBER-26` / `-27`
**Every one returns `yes_bid`, `yes_ask`, `last_price`, `volume` and `open_interest` as null** on the
unauthenticated `api.elections.kalshi.com/trade-api/v2/markets` endpoint, including with an explicit
`series_ticker`+`event_ticker` filter. Also note `market_data.py events` is near-useless as written: it pulls one
unfiltered 200-row page (overwhelmingly sports) and greps client-side, so "oil"/"Iran"/"inflation"/"Bitcoin" all
returned 0 and "Fed" returned two sports parlays.
- **Consequence: I cannot state an implied probability I did not fetch, so no event contract is recommended
  today.** The edge for these is by definition a stated probability disagreement, and without the market price
  there is no disagreement to state. Record in data_quality_notes.

## [06:33 ET] MACRO — the fact that organises today: there is a shooting war affecting oil supply
- **Brent settled 94.089 on 2026-08-21**, after peaking near 95.00 on 08-20; WTI ~86.30. Second consecutive
  weekly rise. Consolidating 93.50-94.10 on Friday.
- driver: **the stalemated US-Iran war** disrupting supply from the Gulf; plus a softer dollar (DXY at a
  two-and-a-half-month low that week)
- source: https://univest.in/blogs/crude-oil-price-today-august-21-2026-brent-iran
- source: https://hdfcsky.com/news/brent-crude-oil-price-today-august-21-2026-brent-dips-to-93-40-wti-at-86-30-as-us-iran-war-keeps-supply-risks-elevated
- source: https://www.vantagemarkets.com/en/market-analysis/brent-crude-wti-oil-price-today-august-21-2026/
**The tension to trade:** a war-driven oil supply shock is an inflation impulse arriving in the same week that
July PCE prints (Wed 08-26) and a brand-new Fed chair gives his first Jackson Hole keynote (Fri 08-28) into a
market pricing a September cut as near-certain and arguing only about 25 vs 50bp. Those two things cannot both
be comfortable. That argues for owning the supply shock directly rather than betting on the Fed's reaction to it.

## [06:34 ET] REJECTED — LMT / NOC / RTX / LHX — defense is de-rating on cash flow, not on peace
Tempting contrarian setup (LMT -18.6% off its 120d high, NOC -28.8%, both fell 1.4-2.3% on 08-21 *during* a
shooting war) and it does not survive:
- the de-rating is fundamental, not sentiment: LMT Q1 2026 EPS 6.44 vs 6.70 consensus, **free cash flow -$291M**,
  operating cash flow collapsed $1.41B -> $220M, segment operating margin 11.6% -> 10.1%
- press framing is "Defense Stocks Slide as Companies Warn of Profit Hits" — guidance-driven
- the war does not fix it: "US defense stocks see no Iran war lift after early surge" (Apr 2026). These are
  long-cycle fixed-price contracts; a Gulf conflict burns munitions inventory, it does not reprice the backlog
  this year.
- **insiders confirm: NOC 0 open-market buys / 30 sells ($5.49M); LMT 0 buys / 15 sells.** Not one executive at
  either company bought the 19-29% drawdown in their own stock in six months.
- source: https://www.itiger.com/news/2529209580
- source: https://www.militarytimes.com/news/your-military/2026/04/02/us-defense-stocks-see-no-iran-war-lift-after-early-surge/
- source: https://www.tikr.com/blog/lockheed-martin-has-fallen-nearly-25-from-its-2026-high-is-it-finally-time-to-buy

## [06:34 ET] INSIDERS — the one genuine signal found today: DINO
- **DINO: 3 open-market buys, 2 distinct buyers, $2.42M bought vs $1.71M sold — net +$706K, the only net
  insider BUYER among everything checked.** MYERS FRANKLIN bought 15,000 sh @ 85.30 on 2026-08-11, after
  15,000 sh @ 69.11 on 2026-05-18. A director buying the same size twice at a 24% higher price is scaling into
  strength, which is the rarer and stronger version of the signal.
- checked and clean/negative elsewhere: NOC 0 buys/30 sells, LMT 0/15, NEM 0 buys/18 sells ($10.8M),
  INSW 0 buys/25 sells, NVDA 0 buys/45 sells ($574M).
- **STNG insider data is CORRUPT and must not be used**: reports 1 buy of 234,637 sh at $5.87 (STNG trades $78)
  and sells totalling $18,934,837,500 — larger than the company. Discarded; STNG is judged on price and
  fundamentals only. Record in data_quality_notes.

## [06:37 ET] REJECTED — CEG — fails the long-term 2.5 reward-to-risk floor on an honest bear case
CEG was rank 2 on 2026-08-21 at entry 266.00, target 385, never filled, last 272.88. The PJM thesis is intact
and Friday's uranium/nuclear move (+7.67% sector) supports it. It still does not clear the floor:
- entry 266, target 385 -> 119 of upside. To clear 2.5x the bear case must be <= 218.4.
- CEG's 120-day range is 228.63-332.42. A bear case *above* the 120-day low is not a bear case.
- if the AI-power demand thesis breaks, CEG does not stop at its 120-day low - the entire premium IS the thesis.
  An honest number is 200-215. At 215: 119/51 = **2.33**. At 200: 119/66 = **1.80**. Both fail 2.5.
- **Not captured.** Per config/strategy.md, "do not reverse-engineer levels to clear the floor" - the only way to
  publish this is to invent a bear case above the 120-day low, so it goes to the watchlist instead.
- suggested watchlist note: thesis intact, valuation no longer offers long-term-grade asymmetry at 266.

## [06:37 ET] CRYPTO — deliberately no new crypto idea, and this is a decision not an omission
It is Saturday and crypto is the only live market, so the absence needs explaining:
- BTC 76,648 (-1.69% 24h), ETH 2,396.14 (-0.32%), SOL 91.62 (+0.41%), XRP 1.45 (+5.48%), DOGE 0.08807 (+4.67%)
- this report is carrying **four losing bitcoin shorts** and the correct action today is to close all of them.
  Flipping the same book from short to long after a 20% adverse move, in the same session, is capitulation
  dressed as a thesis. There is no new information here - only a loss.
- XRP +5.48% and DOGE +4.67% on a quiet weekend with no dated catalyst is noise, not a setup.
- **No crypto candidate captured. Do not read the BTC-short close as an implicit BTC long.**

## [06:37 ET] CORRELATION AUDIT — 7 candidates, and the dollar bucket is AT the cap
| Candidate | Driver |
| --- | --- |
| DINO | war-driven crude -> refining crack spread |
| STNG | war-driven rerouting -> product-tanker ton-miles |
| GLD | dollar debasement / fiscal dominance |
| GDX | dollar debasement, levered through miner cash flow |
| EEM | falling dollar easing EM debt service |
| NVDA | AI capex cycle (independent) |
| DG | low-income consumer trade-down (independent) |
- **oil/war bucket: 2 new (DINO, STNG), plus open XLE x3 and DHT.** Within the cap of 3 new ideas, but the book
  is already heavily long this driver — that is the argument for NOT adding a third and for the XLE trim above.
- **dollar/monetary bucket: 3 (GLD, GDX, EEM) — exactly at the correlation cap. Add no more.**
- GLD and GDX are close to the same bet. **If synthesis must cut one, cut GDX**: GLD is the cleaner expression,
  and GDX closed 19.8% above its 20-day, which is the worse entry of the two.

## [06:37 ET] FALSIFICATION — the case against each finalist
- **DINO** — strongest counter is timing, not thesis: it closed 0.32% from its 120-day high after a 107% run off
  47.00. Every dollar of the thesis is a war premium that a ceasefire headline removes over a weekend. Survives
  only because the entry refuses Friday's close (93.0 vs 97.32) and the insider buying is real and recent.
- **STNG** — the peer gap may be information, not opportunity. FRO and INSW are crude-weighted and near their
  highs; STNG is product-weighted and 10% below its own. If the disruption is crude-specific, the laggard stays
  a laggard. Sized speculative at 2% for exactly this reason, and its insider data was corrupt so no confirmation.
- **NVDA** — this is a "wait" recommendation whose most likely outcome is no trade at all. If NVDA gaps up on
  08-26 the 207.5 limit never fills. Published anyway because holding through a print that shares a session with
  July PCE, Q2 GDP and durable goods is the error worth naming.
- **GDX** — extended to the point of fragility: 19.8% above its 20-day, 3.74% ATR, and the 85 stop sits ON the
  20-day. Also GDX is 12.2% off its high while NEM is 2.5% off, so the ETF is carrying laggards. Weakest of the
  seven; first to cut.
- **GLD** — gold already had a ~24% drawdown this cycle (481.31 -> 363.32 -> 423.36), so this is not a one-way
  ratchet. The 398 entry is 6% below market and may simply never print, which is the honest failure mode.
- **EEM** — a short-dollar position in an equity wrapper, with the dollar path running through an unknown new Fed
  chair's first keynote on 08-28. Also exposed to the oil thesis in the opposite direction: EM is net
  oil-importing, so DINO/STNG working is EEM's terms-of-trade shock. **This is a genuine internal hedge, not a
  contradiction, but synthesis should say so out loud.**
- **DG** — entry 3.6% below the last close with earnings on 08-27 means the most likely outcome is no fill. It has
  also already run 24% off its 120-day low, so the de-rating may be half-repaired before the quarter proves it.

## [06:38 ET] TIMESTAMP CORRECTION
Earlier headings in this file were written from an estimate of elapsed time rather than a `date` call and ran up
to 44 minutes fast. They have been corrected in place to real ET. No finding, price or level was affected —
only the heading times. All prices remain as fetched and stamped by their source. Roughly 47 minutes of budget
remain, so research continues below rather than closing out here.

## [06:39 ET] CATALYST — CAPR — the clean uncorrelated binary, and it resolves TODAY
- **PDUFA target action date 2026-08-22** (today) for deramiocel, Class 2 resubmission, DMD cardiomyopathy
- July 2026 FDA advisory committee voted **3-9 against** evidence of effectiveness (non-binding)
- FDA lifted the earlier CRL and resumed review in March 2026 on new HOPE-3 data
- **HOPE-3 published in The Lancet: met its primary endpoint on upper-limb progression (PUL 2.0, p=0.029)**,
  with additional nominally significant functional and cardiac measures
- Q2 2026 loss ~$40.7M (10-Q filed 08-14, period 2026-06-30)
- price path into the date: 08-13 4.21 (16.7M sh) -> **08-14 6.65 on 66.3M shares** (Q2 print + Lancet) -> 7.45,
  7.08, 7.98 (08-19) -> 6.835 -> **6.29 on 08-21, -7.97%**. Faded 21% off the high in two sessions - the market
  is de-risking into the decision, not accumulating.
- last close 6.29, ATR14 0.9022 (**14.34%**), sma20 5.36, sma50 16.31, 120d range 2.96-36.82, -82.9% off high
- liquidity: 8.36M shares x 6.29 = **~$52.6M average daily dollar volume** - clears the $500K floor by 100x
- sources: https://www.capricor.com/investors/news-events/press-releases/detail/350/the-lancet-publishes-hope-3-data-for-capricor
  | https://www.stocktitan.net/news/CAPR/capricor-therapeutics-reports-second-quarter-2026-financial-results-bwpih3a29010.html
  | https://www.neurologylive.com/view/capricor-dmd-cardiomyopathy-cell-therapy-deramiocel-back-under-review-fda
- **captured as a conviction-2, 1% lottery ticket on the REJECTION branch only.** There is no pre-event entry:
  the decision lands before Monday's open. The specific asymmetry is that the panel voted on *cardiomyopathy*
  while the Lancet paper won on *upper limb* — a CRL washout to the pre-Lancet 4.21 would price the dataset at zero.
- note: the SEC 8-K for 08-13 returned HTTP 403 to direct fetch; details above come from the company press
  release and the 10-Q index rather than the 8-K body.

## [06:39 ET] REJECTED — TITN — an 11.55% move I could not source
Titan Machinery closed 20.18 on 08-21, **+11.55%**, with earnings due 2026-08-27. A double-digit move on an ag
equipment dealer six days before its print is exactly the sort of thing worth owning IF the cause is known.
I could not source it: the only material search returned was a 17% jump on 2026-03-21 on Q4 revenue, a different
event five months ago. **Not captured** — recommending an 11.5% one-day move whose driver I cannot name would be
a hunch with a chart attached. Worth a watchlist line so the next run checks the 08-27 print.

## [06:42 ET] LONG-TERM — LULU — the best idea found today, and it is not an energy trade
- last 121.07, sitting exactly on its 20-day (121.17), 50-day 117.63, ATR14 3.43%
- **-40.96% off the 120-day high of 205.07**, only 15.9% above the 120-day low of 104.44
- FY2026 guidance CUT: revenue $11.0-11.15B (was $11.35-11.5B) = flat to -1% (was +2-4%);
  EPS $10.95-11.15 (was $12.10-12.30) vs a $12.29 estimate
- Q1 gross margin **-410bp** on tariffs and promotional activity; North America comps down, China growing
- interim CEO Meghan Frank attributed it to "negative commentary in the media" and product launches that
  failed to wow shoppers — i.e. a merchandising problem, named by management
- **Heidi O'Neill becomes permanent CEO 2026-09-08** — 28-year Nike veteran, most recently President of
  Consumer, Product and Brand at Nike. Q2 earnings 2026-09-02, six days before she starts.
- **INSIDERS: 3 open-market buys, 2 distinct buyers, $1.99M bought vs $100K sold, net +$1.89M.**
  Board chair Charles Bergh bought 6,090 sh @ 164.20 (03-20) then 4,275 sh @ 117.05 (06-15) — averaging down.
  Andre Maestrini 3,275 sh @ 151.02 (04-01).
- valuation anchor for the 180 target: ~11x the cut EPS guide today; 180 is roughly 16x a partially recovered
  ~$11.3 and still 12% BELOW the 120-day high. Bear case 90 = ~8x on a broken-brand multiple, below the 104.44 low.
- sources: https://www.cnbc.com/2026/06/04/lululemon-lulu-earnings-q1-2026.html |
  https://www.fool.com/investing/2026/08/21/lululemon-is-down-45-from-its-all-time-high-should/
- **CROSS-READ FOR THE OPEN NKE POSITION: LULU is hiring away Nike's President of Consumer, Product and Brand.**
  That is a mild negative for NKE, which this report holds x2 long, and it reinforces the "hold, add nothing"
  decision recorded above rather than changing it.

## [06:42 ET] REJECTED — uranium juniors (UEC, DNN, NXE, UUUU, LEU) — chasing, and already correlated
Friday's closes: UEC 12.76 **+14.44%**, DNN 3.50 +11.47%, UUUU 15.14 +8.92%, NXE 10.86 +6.26%, LEU 186.26 +5.75%.
The whole complex melted up on the same AI-datacenter-baseload sentiment that lifted CCJ +7.24%.
Two reasons not to capture any of them: (1) buying a junior after a 14% single-day sentiment move with no
company-specific news is chasing, and (2) **this report already holds CCJ x2 on exactly this driver** — adding a
junior would be a third correlated bet on one narrative, at the worst price of the month.

## [06:43 ET] REJECTED — EQT / AR / RRC / CRK — good structure, wrong book
All four are de-rated and basing above both moving averages: EQT 53.72 (-21.3% off high), AR 37.94 (-17.1%),
RRC 41.06 (-15.0%), CRK 14.22 (-45.0%). EQT's 2.42% ATR makes it the cleanest chart of the group.
Rejected on two grounds: **zero open-market insider buying at any of the four** (EQT 0 buys/10 sells -$11.1M,
AR 0/8 -$11.2M, RRC 0/10 -$4.2M, CRK 0/1 -$1.0M), and portfolio concentration — the book already carries XLE x3
and DHT open plus DINO and STNG new. Henry Hub is genuinely a different driver from Brent, but a reader looking
at this sheet would see energy in seven places. Watchlist, not a recommendation.

## [06:43 ET] REJECTED — UNH, CVS — falling knives, no insider support
UNH 390.11 is -15.5% off its high and **below both its 20-day (406.00) and 50-day (413.79)**; CVS 93.02 is -16.0%
off its high and likewise below both (98.90 / 102.01). Both are still making lower highs, and neither has a single
open-market insider buy in six months (UNH 0 buys/2 sells). A de-rating is only interesting when something has
stopped the fall. Compare LULU, which is *on* its 20-day with the chair buying. Not captured.
- PEP also screened (143.48, -16.3% off high, ATR only 1.63%, above both MAs) and rejected on the same insider
  test: 0 open-market buys against $6.15M of sales.

## [06:44 ET] VENUE CHECK — verified at Robinhood, not assumed from memory
- **STNG** — confirmed tradeable: "Trade Scorpio Tankers 24 hours a day, five days a week on Robinhood." NYSE.
  Market cap **$3.93B**, **P/E 4.46**, dividend yield 2.19%, 52-week range 48.01-87.39, 85% Buy from 13 analysts.
  (The 4.46 P/E is a useful addition to the thesis: the laggard is also the cheap one.)
  RH page showed $78.25 intraday-stamped 2026-08-22 vs my 78.49 Friday close — immaterial, close is the level used.
  source: https://robinhood.com/us/en/stocks/STNG/
- **CAPR** — confirmed tradeable, Nasdaq. **Market cap $365.69M**, 52-week range 2.96-40.37, P/E -2.57.
  Above the $300M threshold, so the 1% sizing is a choice about the binary rather than a cap requirement; under
  $2B, so market cap and dollar volume are stated in the thesis as required. Re-captured with market_cap_usd set.
  source: https://robinhood.com/us/en/stocks/CAPR/
- **DINO** — confirmed tradeable. Market cap **$17.29B**, 52-week range 45.71-97.90 (my 120-day high of 97.63 is
  effectively the 52-week high — the "no overhead supply" risk in key_risk is real).
  source: https://robinhood.com/us/en/stocks/DINO/
- DG, NVDA, GLD, GDX, EEM, LULU are large-cap US-listed common stock and NYSE-Arca ETFs; no availability question.

## [06:44 ET] ARITHMETIC AUDIT — recomputed every candidate from its own levels
Recomputed R:R = (target - entry) / (entry - stop), or / (entry - bear_case) for long_term. All 10 lines,
9 unique symbols. Every stated `risk_reward` matched the recomputation to within 0.01, and every idea clears
its horizon floor on its own numbers rather than by a nudged target:
DG 2.286 / DINO 2.308 / STNG 2.111 / NVDA 2.522 / GDX 2.556 / EEM 2.269 (floor 2.0);
GLD 3.486 / LULU 2.600 (floor 2.5); CAPR 3.024 (floor 2.0). **Total position size 22%** across 9 ideas.

## [06:45 ET] REJECTED — small-cap screen, 12 names with next-week catalysts, none cleared
NSSC 38.09 / ELMD 39.45 / CTRN 71.71 / REX 44.67 / AVNW 20.83 / MCFT 25.46 / MBUU 29.50 / PD 12.32 / S 21.19 /
OLLI 76.07 / URBN 74.24 / ASO 45.83. Screened on drawdown, position vs the 20/50-day, and insider behaviour.
**Not one had a single net open-market insider buy** (CTRN shows 1 buy against -$42.4M net). The two most
tempting on price - OLLI at -36.3% off its high and ASO at -26.6% and sitting 4.8% above its 120-day low - are
both discount retail, i.e. the same low-income trade-down driver already expressed through DG, and both are
below their 20- and 50-day. Nothing captured. This is what an honest empty screen looks like.

## [06:45 ET] CONSIDERED AND REJECTED — a short leg, to balance an all-long book
All 9 candidates are long. In a week carrying NVDA earnings, July PCE and a new Fed chair's first Jackson Hole
keynote, that is a directional bet on the tape and worth naming rather than hiding.
The obvious short was defense - NOC 551.03 is -28.8% off its high and below both MAs, LMT -18.6% and below both,
with deteriorating FCF, warned-on margins, and zero insider buying between them. **Rejected anyway: shorting
aerospace-defense during an active US-Iran war is an uncapped tail.** One escalation headline over a weekend
gaps that position against you without a level to stop out at. A correct-looking thesis with an unbounded
overnight tail is not a trade. Synthesis should state the all-long skew in data_quality_notes.

## [06:46 ET] MACRO — index levels recovered, and they close the gap logged at 06:27
The Yahoo 429s that blocked ^GSPC/^NDX/^DJI at the start of the run are now covered from press reporting:
- **S&P 500 7,674.37, +33.21 (+0.4%)** on 2026-08-21
- **Dow 53,277.01, +517.80 (+1.0%)**
- **Nasdaq composite 26,180.45, +113.29 (+0.4%)**
- **but all three posted WEEKLY LOSSES** — Friday's bounce came after a bond sell-off pressured risk assets
  all week. Consistent with TLT closing 82.05 and the 30-year at a two-decade high.
- source: https://finance.yahoo.com/markets/world-indices/articles/major-us-stock-indexes-fared-202316400.html
- source: https://finance.yahoo.com/markets/live/stock-market-today-friday-august-21-dow-sp-500-nasdaq-bitcoin-080533702.html

## [06:46 ET] BTC PRICE CROSS-CHECK — the close-the-shorts instruction is on solid ground
Because "close all four bitcoin shorts at market" is the most consequential line in this report, the price was
verified against an independent second source rather than taken from one API:
- CoinGecko spot: **76,648**
- IBIT closed **43.68** on 08-21. IBIT holds ~0.00057 BTC/share, which implies **BTC ~76,632** — a 0.02% gap.
- corroborating: FBTC 67.02. **IBIT +6.02% and FBTC +5.93% on Friday alone** — the shorts got worse on 08-21,
  they are not sitting at a stale mark. Yahoo's own Friday headline was "bitcoin soars".
Two independent sources agree to within 0.02%. There is no data-quality escape hatch here: the shorts are
~19-21% offside through stops that were set at 65,200 and 66,600.

## [06:47 ET] NEWS — beneath a green Friday, the tech tape was weaker than the index
- Amkor (AMKR) **-15%** and Credo (CRDO) **-11%** over the prior five sessions; Meta **-7%** over the same stretch
- this matters for the NVDA candidate: semis were being sold into the week before the 08-26 print even as the
  Nasdaq closed green, which supports the "wait for the reaction, do not hold through it" framing rather than
  contradicting it
- Moderna +9% Friday, Merck +2%
- **Ross Stores rallied on a stronger-than-expected quarterly profit** — worth recording next to the TJX close
  decision above. Off-price retail is not uniformly broken; TJX specifically missed and broke down while its
  closest comparable beat. That is a company problem, not a sector problem, and it strengthens the case for
  closing TJX rather than averaging into it.
- source: https://finance.yahoo.com/markets/live/stock-market-today-friday-august-21-dow-sp-500-nasdaq-bitcoin-080533702.html
- NOT captured: ROST. It rallied on the print; the entry is gone and the driver overlaps DG.

## [06:47 ET] CATALYST DATES VERIFIED against the Finnhub earnings calendar
Every dated catalyst used in a candidate was re-checked rather than trusted from the week-ahead article:
- **NVDA 2026-08-26 `amc`** — EPS est 2.1283, revenue est **$93.63B**. Confirms the 08-26 16:20 ET stamp, and
  confirms it shares a session with July PCE / Q2 GDP / durable goods.
- **DG 2026-08-27 `bmo`** — EPS est 2.0559, revenue est $11.53B. Confirms entry must fill before 08-27.
- **LULU 2026-09-02 `amc`** — EPS est 1.8353, revenue est $2.51B. Six days before Heidi O'Neill starts on 09-08.
- **FRO 2026-08-31 `bmo`** — EPS est 2.5667. Confirms the STNG read-across catalyst.
- TITN 2026-08-27 `bmo` — **EPS estimate is -0.3697, a loss**. This makes Friday's unexplained +11.55% more
  suspect, not less, and confirms the decision not to capture it.

## [06:47 ET] NO FUTURES IDEA TODAY — a decision, not an oversight
config/universe.md prefers futures where they express the same view, so the absence needs a reason.
Each available micro contract was considered and declined on the correlation cap, not on the instrument:
- **/MGC (gold)** — same driver as GLD and GDX. The dollar/monetary bucket is already at the 3-idea cap.
- **/MCL (crude)** — same driver as DINO and STNG, on top of open XLE x3 and DHT. Adding leveraged crude to a
  book already long the oil complex in five places is concentration, not expression.
- **/MES, /MNQ, /M2K** — no directional edge into NVDA + PCE + a new Fed chair's first keynote. Taking a
  leveraged index position on a week whose two largest events are both unknowable would be a hunch with margin.
- **/MBT (bitcoin)** — the book is closing four losing bitcoin shorts today. Re-entering the same underlying in
  either direction in the same session is not a thesis.
The honest version of "prefer futures" is that it applies when a view exists to express. Today the views that
exist are equity-specific, and the macro views are already at their correlation limits.

## [06:48 ET] RESEARCH COMPLETE — SUPERSEDED, see the 06:50 block at the end of this file
> Written before event prices were recovered. It says 9 candidates and calls event contracts the biggest gap;
> both statements were overtaken within two minutes. Kept for the audit trail — use the 06:50 block instead.
- **candidates: 9 unique (10 lines; CAPR captured twice, the later line adds market_cap_usd — take the last)**
  DINO(4, swing) · LULU(4, long_term) · GLD(4, long_term) · DG(3, swing) · STNG(3, swing) · NVDA(3, swing) ·
  GDX(3, swing) · EEM(3, swing) · CAPR(2, swing, lottery)
- **the report's most urgent line is not a candidate**: CLOSE ALL FOUR BITCOIN SHORTS AT MARKET. Also close
  TJX, KRE, HD x2 and LCII; hold CCJ (add a 93.00 stop), XLE x3 (raise stop to 61.50, trim the 08-16 tranche
  into 64.50), TLT, PFE, BCC, NKE x2; hold DHT and raise its stop to 18.80 breakeven.
- **skew, stated plainly**: 9 of 9 are long, 2 of 9 are long_term, and there is no crypto, futures or event
  contract idea despite this being a weekend run. Each absence is argued above rather than left implicit.
- **coverage gaps**
  - event contracts: could not be priced at all (see 06:33) — the whole class is missing from a weekend report,
    which is the single biggest hole today
  - no international/ADR sweep, no rate-futures positioning data, no options-implied move for NVDA
  - TITN's +11.55% on 08-21 remains unexplained
  - the 08-13 CAPR 8-K body could not be read (SEC returned 403); CAPR detail comes from the press release and 10-Q
- **sources that failed**
  - Yahoo Finance: HTTP 429 on every index symbol (^GSPC ^NDX ^DJI ^RUT ^VIX ES NQ DXY gold WTI) at 06:25;
    index levels were recovered from press reporting at 06:46, but VIX, DXY and futures levels were never obtained
  - Finnhub: rejects index CFDs ("Market data subscription required")
  - Stooq: 404 on all ^-prefixed symbols; AlphaVantage: no API key configured
  - Kalshi: every price/volume/open-interest field returns null unauthenticated
  - `market_data.py events`: returns near-random results by design (one unfiltered 200-row page, grepped)
  - `market_data.py insiders STNG`: corrupt figures ($5.87 basis on a $78 stock, $18.9B of sales)
  - WebFetch 403 on sec.gov Archives and on actionforex/cnbc for one article each
- research ran 06:25-06:48 ET (~23 minutes). Timestamps between 06:29 and 06:37 were corrected once, in place,
  after a `date` check showed they had been estimated up to 44 minutes fast; see the 06:38 note. No price,
  level or finding was affected.

## [06:48 ET] CORRECTION — EVENT PRICES RECOVERED, AND THEY INVERT THE WEEK-AHEAD NARRATIVE
**The 06:33 note saying event contracts could not be priced is now superseded.** Kalshi has moved its quotes to
`*_dollars` string fields (`yes_bid_dollars`, `last_price_dollars`); `market_data.py events` reads the legacy
integer-cent fields (`yes_bid`, `last_price`), which no longer exist, so it returns null for every market.
**This is a fixable bug in scripts/market_data.py, not a dead source.** Working endpoint:
`/trade-api/v2/events/<EVENT_TICKER>?with_nested_markets=true`.

**Sep 2026 FOMC — KXFEDDECISION-26SEP, resolves 2026-09-16. Deeply liquid.**
| Outcome | yes bid/ask | last | volume | open interest |
| --- | --- | --- | --- | --- |
| Cut >25bps | 0.00 / 0.01 | 1c | 693,352 | 685,739 |
| **Cut 25bps** | 0.00 / 0.01 | **1c** | 3,189,249 | 2,892,612 |
| **Fed maintains rates** | 0.67 / 0.68 | **68c** | 4,860,136 | 3,474,820 |
| **Hike 25bps** | 0.31 / 0.32 | **31c** | 2,763,764 | 1,735,701 |
| Hike >25bps | 0.00 / 0.01 | 1c | 803,308 | 661,977 |

**This flatly contradicts the week-ahead reporting I logged at 06:31.** Those articles said markets price a
September cut as "a near-certainty" debating only 25 vs 50bp. The live market says the opposite: **a cut is a
1-cent lottery ticket and a HIKE is a 31% probability.** I am treating the traded market with 4.86M contracts of
volume as correct and the article summary as stale — most likely recycled from an earlier year. **Any statement
in this report that the Fed is about to cut is wrong and must not be repeated.**
- corroboration from the same exchange, KXFED-26SEP (funds rate after the Sep meeting): "Above 3.50%" = 99c,
  **"Above 3.75%" = 32c**, "Above 4.00%" = 1c. With fed funds effective at 3.63% (FRED 08-20), that is the same
  31-32% hike probability priced a second way, and it is internally consistent.
- **KXCPIYOY-26AUG** (Aug CPI YoY, resolves 09-11 — i.e. BEFORE the 09-16 FOMC): Above 3.2% = 87c,
  **Above 3.3% = 69c**, Above 3.4% = 26c, Above 3.5% = 10c. The market's central expectation is ~3.3% YoY.
- **KXRECSSNBER-26** (recession starts in 2026): **5c**, on 3.33M volume. No recession priced.
- all four events return `available_on_brokers: true` and `category: Economics`.

**This makes the oil thesis MORE coherent, not less.** I wrote at 06:33 that a war-driven inflation impulse and a
near-certain cut "cannot both be comfortable." The resolution is that the market already repriced: $94 Brent,
3.3% CPI and a 31% hike probability are one consistent picture. It is the news summary that was out of date.

## [06:49 ET] VENUE CHECK — Robinhood DOES carry the Sep FOMC market
Verified rather than inferred from Kalshi's `available_on_brokers` flag:
- **https://robinhood.com/us/en/prediction-markets/economics/events/fed-rate-decision-in-september-2026-sep-16-2026/**
  is a live Robinhood Prediction Markets event page. Robinhood also lists "Next Fed rate hike",
  "Fed rate decision in October 2026" and "Number of rate cuts in 2026" under Economics.
- **third independent corroboration that the cut narrative is dead: Robinhood's own "Number of rate cuts in
  2026" market shows 86% probability of EXACTLY ZERO cuts.** That is Kalshi's 1c cut price, the KXFED-26SEP
  ladder, and Robinhood's own tab all agreeing, against a news summary that said the opposite.
- fee note, material at a 32c entry: probability-weighted commission since 2026-06-01, a percentage of contract
  price x contracts, rounded up to the nearest $0.01 and **capped at $0.01 per contract**.
- Robinhood's Economics tab does NOT appear to list dedicated CPI/inflation markets, so KXCPIYOY is used here
  as evidence only — it is not recommended, because I could not confirm a reader can trade it.
- source: https://robinhood.com/us/en/prediction-markets/economics
- source: https://www.wallstreetsurvivor.com/robinhood-prediction-markets/

## [06:49 ET] THE EVENT CONTRACT IS ALSO THE BOOK'S ONLY HEDGE
Worth flagging for synthesis: KXFEDDECISION-26SEP-H25 is not just an uncorrelated idea, it is the **only
position in this report that profits from a hawkish surprise**. The other nine are long risk, and three of them
(GDX, EEM and to a lesser extent NVDA) are hurt specifically by the outcome this contract pays on. That is a
deliberate and useful property at 1% size, and it partly answers the all-long objection logged at 06:45 —
though it does not eliminate it, since 1% cannot offset 21%.

## [06:50 ET] RESEARCH COMPLETE (supersedes the 06:48 block, which was written before event prices were recovered)
- **candidates: 10 unique (11 lines; CAPR appears twice — take the LAST, which carries market_cap_usd).
  Total position size 23%.**

| Conv | Symbol | Horizon | Class | Dir | Size |
| --- | --- | --- | --- | --- | --- |
| 4 | DINO | swing | stock | buy | 3% |
| 4 | LULU | long_term | stock | buy | 4% |
| 4 | GLD | long_term | etf | buy | 4% |
| 3 | DG | swing | stock | buy | 2% |
| 3 | STNG | swing | stock | buy | 2% |
| 3 | NVDA | swing | stock | buy | 2% |
| 3 | GDX | swing | etf | buy | 2% |
| 3 | EEM | swing | etf | buy | 2% |
| 2 | CAPR | swing | stock | buy | 1% |
| 2 | KXFEDDECISION-26SEP-H25 | swing | event | yes | 1% |

- **The most urgent line in this report is not a candidate: CLOSE ALL FOUR BITCOIN SHORTS AT MARKET.** BTC 76,648
  verified against IBIT to within 0.02%; the 65,200 and 66,600 stops were violated days ago and the position is
  ~19-21% offside. Also close TJX, KRE, HD x2, LCII. Hold CCJ (add a 93.00 stop), XLE x3 (raise stop to 61.50,
  trim the 08-16 tranche into 64.50), TLT, PFE, BCC, NKE x2. Hold DHT and raise its stop to 18.80 breakeven.
- **The single most important correction for synthesis: DO NOT WRITE THAT THE FED IS ABOUT TO CUT.** Three
  independent sources — Kalshi's KXFEDDECISION-26SEP (cut = 1c), the KXFED-26SEP rate ladder, and Robinhood's own
  "Number of rate cuts in 2026" market (0 cuts at 86%) — agree there is no cut priced and a 31% chance of a HIKE.
  The week-ahead articles logged at 06:31 said the opposite and are stale.
- **skew, stated plainly**: 9 of 10 ideas are long risk; the event contract is the only hedge, and 1% cannot
  offset 23%. 2 of 10 are long_term. No crypto and no futures idea — both declined with reasons (06:37, 06:47),
  not overlooked. 5 of 10 entries sit BELOW Friday's close and require a pullback to fill, so a quiet up-week
  produces few fills; that is intended, not an accident.
- **coverage gaps**
  - VIX, DXY and index-futures levels were never obtained (only cash index closes, from press reporting)
  - no options-implied move for NVDA, no rate-futures positioning, no international/ADR sweep
  - TITN's +11.55% on 08-21 remains unexplained (and its 08-27 consensus is a loss of -0.37/sh)
  - the CAPR 08-13 8-K body could not be read (sec.gov returned 403)
  - CPI event contracts were priced but are NOT recommended: I could not confirm Robinhood lists them
- **sources that failed**
  - Yahoo Finance: HTTP 429 on every index symbol at 06:25 (^GSPC ^NDX ^DJI ^RUT ^VIX ES NQ DXY gold WTI)
  - Finnhub: rejects index CFDs. Stooq: 404 on ^-prefixed symbols. AlphaVantage: no API key.
  - **`market_data.py events` is BROKEN, not blocked — worth fixing before the next run.** Two defects: it reads
    Kalshi's retired integer-cent fields (`yes_bid`, `last_price`) instead of the current `*_dollars` strings, so
    every price returns null; and it greps one unfiltered 200-row page instead of filtering server-side by
    `series_ticker`. Working call:
    `/trade-api/v2/events/<EVENT_TICKER>?with_nested_markets=true`. I did not patch it mid-run because phases
    2b-2d import this module and a code change here would risk the rest of the pipeline.
  - `market_data.py insiders STNG`: corrupt ($5.87 cost basis on a $78 stock, $18.9B of reported sales)
  - WebFetch 403 on sec.gov/Archives and on cnbc.com
- research ran **06:25-06:50 ET (~25 minutes)**. One timestamp correction was made in place at 06:38 after a
  `date` check showed the early headings had been estimated up to 44 minutes fast; no price, level or finding
  was affected. All prices are 2026-08-21 closes (market closed) except crypto and event contracts, which are live.
