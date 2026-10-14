# Research log — 2026-10-14

## [06:02 ET] MACRO — rates, regime, data availability
- US 10Y Treasury yield **5.24%** (FRED, 2026-10-09); 2Y **4.80%**; curve 10y-2y **+0.42** (2026-10-13). Source: https://fred.stlouisfed.org/series/DGS10
- Fed funds effective **3.88%** (2026-10-12). Source: https://fred.stlouisfed.org/series/DFF
- Unemployment **4.2%** (Sept 2026). Source: https://fred.stlouisfed.org/series/UNRATE
- Regime read: long end at 5.24% with fed funds at 3.88% = a steep, term-premium-driven curve. Long-duration assets (TLT 20y proxy 78.37, +0.41%) remain pressured; this is a headwind for REITs/utilities/long-duration growth and a tailwind for bank NIM.
- SPY prev close **778.01** (-0.01%, finnhub, asof 2026-10-13T20:00Z = previous close, market closed).

## [06:02 ET] DATA QUALITY — source failures this run
- Yahoo Finance returning **HTTP 429** on every index symbol: ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX all FAILED across finnhub(CFD subscription)/yahoo(429)/stooq(404). **No VIX reading available this run.**
- Futures quotes (ES, NQ), DXY, gold, WTI all FAILED for the same reason. Futures ideas cannot be priced from live data today.
- CoinGecko crypto prices FAILED this run — no crypto ideas can be priced.
- Finnhub **does** serve individual US equities/ETFs — equity work proceeds normally on previous-close data.

## [06:02 ET] CALENDAR — earnings inside 10 sessions (finnhub, fetched)
- Today 2026-10-14: BAC, BLK, FAST, MS, STT (big-bank Q3 kickoff)
- 10-15: PNC, USB, SCHW, PLD, AA, IBKR, JBHT, CMC, WHR, BNY, MRSH, MAN
- 10-16: TFC, MTB, RF, CFG, TRV (regional banks)
- 10-19: **GE**, **STLD**, CLF, FITB, CCK, WRB
- 10-20: TSLA, NFLX, GM, RTX, NOC, COF, CB, UAL, ALK, MMM, PM, HAL, ISRG
- 10-21: META, IBM, TXN, LRCX, T, CSX, DHR, TMO, ABT, NEE, LUV, LVS, CME, KMI
- 10-22: PG, HON, LMT, GD, BX, CMCSA, NSC, UNP, GILD, VLO, NEM, WDC, AAL, DOW, PHM, NVR
- 10-23: XOM, AXP, SLB, DVA, ALV

## [06:03 ET] DATA QUALITY — event contracts unavailable
- `market_data.py events "Fed"` and `events "CPI"` both return `ok: true` with **count 0** — the Kalshi source lists nothing this run. No event-contract price can be quoted, so **no event contracts are published today**. This is a source gap, not an absence of markets; the two pending Fed contracts (KXFEDDECISION-26OCT-H25, KXFEDDECISION-26SEP-H0) could not be re-priced.
- Consequence: the two pending CPI/Fed event lines from prior runs are left untouched rather than amended on a guessed price.

## [06:04 ET] POSITION UPDATE — XLF — opened 2026-10-09 @ 54.23, last 54.82 (+1.1%)
- decision: **hold, levels unchanged** (entry 54.23 / target 57.60 / stop 52.80)
- why: catalyst arriving not passing — BAC/MS/BLK/STT today, PNC/USB/SCHW 10-15, TFC/MTB/RF/CFG 10-16 (fetched finnhub calendar). Curve 10y-2y +0.42, 10Y 5.24% vs 3.88% funds = NIM tailwind.
- caution: XLF -6.5% off the 58.60 range high, still below sma50 56.44. R:R from the 54.23 entry = 2.36; stop is 2.2 ATR (ATR14 0.649) vs the 1.8 ATR ETF floor.
- action: captured via add_candidate.py, unchanged levels.

## [06:05 ET] POSITION REVIEW — DINO — opened 2026-08-22 @ 107.5, last 128.23 (+19.3%)
- **Target 128.00 was reached on 2026-10-13** (high 128.56, close 128.23, source nasdaq history). This position has hit its objective and grades as a win; it is not re-pitched.
- Context: refiners ran hard — DINO +4.3% on 10-13 on 2.21M shares. I could **not** source a dated reason for the move (searched; no DINO 8-K, no same-day report found). Recording it as unexplained rather than attributing it to crack spreads I did not fetch.
- No new DINO entry: chasing a +4.3% day into a hit target is exactly the re-pitch the prior-context guard warns about.

## [06:05 ET] POSITION REVIEW — SMMT — opened 2026-10-09 @ 17.1, last 15.52 (-9.2%)
- Fell **-9.4% on 2026-10-13**. Checked SEC filings: most recent are a PRE 14A (10-06) and an 8-K (09-29) — **no filing explains the drop**. Web search returned only undated/older ivonescimab stories, none matching 10-13.
- decision: **hold, no change**. Stop 14.4 is intact and 7% below; the position is sized as a speculative biotech and the stop is the risk control. Tightening it after a drop with no sourced cause would be reacting to noise.
- Not re-captured — unchanged levels on an unexplained move is not new information.

## [06:08 ET] DATA QUALITY — further source failures
- `implied` (options-implied move) fails all run: yahoo-options returns **HTTP 401 Unauthorized**. No idea today can be checked against what the options market prices. This is the second check `config/strategy.md` asks for at level-setting and it is unavailable.
- `short` (short interest / days to cover) **timed out** on api.nasdaq.com for TRV. Short-interest positioning is unverified today.

## [06:09 ET] NEW — TRV — captured, conviction 4
- Thesis: P&C insurer is structurally long the 5.24% 10Y via reinvestment of float; sector-leading relative strength; dated Q3 print 2026-10-16 (fetched calendar).
- Levels from real history: last 373.28, ATR14 5.62. Entry zone 366-372 (sma20 366.14 / sma50 369.18 converging), stop 356.50 below the 10-07 swing low 357.09 = 2.4 ATR, target 398.00 = the 398.695 range high. R:R 2.07 on a 370 entry. Baseline win rate 1/(1+2.07) = 32.6%; claimed 40%.
- Honest negatives recorded in counter_argument: analyst revisions **deteriorating** (bullish share 25.7%, -7.6pts; sells 1→5 since June), insiders 0 open-market buys / 25 sells / -$36.3M over 6 months.
- Q3 catastrophe losses could not be sourced — stated as the key_risk rather than assumed benign.

## [06:10 ET] REJECTED — ITB SELL_SHORT (pending @ 89.8 from 09-30) — entry level is stale and unfillable
- ITB last 84.64, i.e. the market moved 5.7% *away* from the 89.8 short entry in the trade's favour without ever filling it. Re-pitching at 89.8 would publish a level that cannot fill.
- A fresh short at 84.64 sits 1.1% above the 83.69 range low: shorting into a completed breakdown, with the 2.0 R:R only reachable on a target 5.7% below the range low. Thesis (10Y 5.24% -> mortgage rates -> builders, ITB -20.4% off high, below sma20 87.22 and sma50 92.37) is intact, but no honest entry exists today. Left for the watchlist, not re-captured.

## [06:12 ET] SECTOR — defense/aerospace de-rating now has a sourced, dated cause
- iShares US Aerospace & Defense ETF ~**-18.2%** from its 2026-08-14 record close; worst monthly and quarterly decline since March 2020. Source: https://tradersunion.com/news/financial-news/show/3659983-us-defense-stocks-bear-market-turn/
- Cause is budget timing, not demand: Congress has passed **no FY2027 appropriations bill**; a **continuing resolution runs to 2026-12-11** holding funding at 2026 levels. Bernstein's Douglas Harned calls the **2026-11-03 midterms** a possible clearing event and advises **waiting before buying**. Source: https://www.investing.com/news/stock-market-news/should-you-buy-selloff-in-defense-stocks-bernstein-answers-4913539
- Midterm risk framing (a Democratic gain delaying funding): https://www.bloomberg.com/news/articles/2026-09-17/risk-of-midterm-blue-wave-leaves-defense-stocks-out-of-favor
- Measured drawdowns off 120-day highs (fetched nasdaq history, 10-13 closes): **HII -30.6%** (257.84, new 120-day low 255.355 set 10-13), **NOC -19.3%** (481.38), **LMT -17.7%** (504.02), **GD -16.9%** (332.42). All four below both their 20- and 50-day averages.
- This gives the sector a **dated catalyst (11-03) it did not have yesterday**. It does not make it a buy today — the sell-side view is explicitly "wait".

## [06:13 ET] POSITION UPDATE — HII — opened 2026-10-12 @ 262.0, last 257.84 (-1.6%)
- decision: **hold, zone and target unchanged; pacing updated.** Accumulate the first third inside 240-268; **hold the second third until after 11-03** rather than averaging in ahead of the midterms.
- why: the de-rating's cause is now named and dated, and it is a funding-*timing* story. Virginia Block VI / Columbia are multi-year, already-awarded, sole-source — the line least exposed. But a CR does block new starts and can delay incremental funding, which is the real risk and is now stated as such.
- action: captured via add_candidate.py, conviction 5, bear case 195.

## [06:14 ET] POSITION UPDATE — GE — filled 2026-10-12 @ 308.0, last 307.63 (flat)
- decision: **hold, levels unchanged** (302-312 band / target 341 / stop 292). Trim half into the 10-19 open as already planned.
- new and negative: GE now **lags SPY on every window** (-5.4% 1m, -17.7% 3m, -15.3% 6m) and lags XLI -8.3% over 3m. Recorded because it argues against the position.
- analyst trend frozen at 87.5% bullish for four straight months (9/19/3/1 unchanged) — read as sell-side inertia through a 21% drawdown, not support.
- red-team condition from 10-12 restated and now operative: **do not average under 302**.
- action: captured via add_candidate.py.

## [06:15 ET] RE-PITCH — STLD — unfilled stop-limit from 2026-10-10, levels unchanged
- Never triggered: entry trigger 245.185 (10-05 session high / top of the base), last 240.63. Catalyst is now 3 sessions out rather than 7 — that is the only change, and it is stated as such.
- Levels re-verified against today's history: sma50 240.76 still caps every close since 09-18; stop 228.75 below the 09-28 low 227.10, 2.58 ATR at ATR14 6.49; R:R 2.12.
- action: captured via add_candidate.py.

## [06:16 ET] DATA HYGIENE — a drawdown is not always a drawdown
- **HON shows -56.8% off its 120-day high (479.88 -> 207.29) and this is a corporate action, not a de-rating.** The price path steps down and then trades flat in a 197-214 band for the whole recent window; the "high" is pre-separation Honeywell. Anything screening on `pct_off_high` will surface it as the cheapest large cap on the board. Not pitched, and recorded so a later run does not rediscover it as a bargain.
- NFLX's 94.70 -> 70.46 range is post-split pricing throughout and **is** a real -25.6% de-rating.

## [06:18 ET] REJECTED — WDC — real de-rating, but no defensible valuation anchor
- The de-rating is real and sourced: -52.4% off the 799.87 range high to 380.71, driven by Toshiba's planned HDD capacity expansion (Toshiba ~17% share vs WDC 40%+) raising supply-glut and pricing fears, plus price-target cuts and broader AI-spend concerns. Sources: https://www.benzinga.com/markets/tech/26/10/62333317/western-digital-stock-under-pressure-as-rising-asian-production-raises-supply-concerns | https://www.gurufocus.com/news/9108148/western-digital-wdc-shares-plunge-over-10-amid-sector-selloff-on-october-2-2026
- Fundamentals genuinely strong: revenue +43.8% YoY to $3.75bn, EPS beat in **4 of the last 4** quarters (+11.6%, +10.0%, +12.7%, +7.0%), EPS trajectory 1.78 -> 2.13 -> 2.72 -> 3.56 with 4.0949 estimated for the 10-22 print on $4.16bn revenue.
- **Why it is still rejected:** the numbers do not make it cheap. Trailing four-quarter EPS = 10.19, so 380.71 is **37.4x trailing**; annualising the 4.09 estimate gives 16.36 and **23.3x forward**. A cyclical hardware maker at 23x forward, after halving, is not a value anchor — it is a stock that was at ~78x trailing when it was $800. The sell-side average target of $618.63 implies ~38x the annualised run-rate, which is a momentum target, not a valuation.
- Reinforcing negatives: revisions **deteriorating** (bullish share 77.4%, -8.8pts; holds 4->7), insiders **0 open-market buys against 128 sells** (-$35.6M/6m).
- A supply glut is precisely the event that compresses a cyclical's multiple, so the bear case attacks the one thing holding the price up. No long. No short either — shorting a 4-for-4 beater into its print is the wrong side of the surprise record.

## [06:19 ET] NFLX — serial earnings misser in a severe relative downtrend; short candidate
- **Missed EPS in 4 of the last 4 quarters**: -17.4%, -0.5%, -10.2%, -0.5% (finnhub surprise record). A company that misses consistently is being modelled wrong by the street, and the street has not finished adjusting.
- Revisions deteriorating: bullish share 74.1%, -3.5pts; strong-buys 16 -> 14, holds 13 -> 15.
- Insiders: **0 open-market buys, 23 sells, -$93.3M** over 6 months.
- Relative strength: lagging SPY on every window — **-14.5% 1m, -7.4% 3m, -45.7% 6m**; vs XLC -9.9% / -3.4% / -30.0%.
- Price 70.46 (post-split), -25.6% off the 94.70 high, below sma20 70.81 and sma50 75.25. ATR14 1.4546 (2.06%).
- Catalyst: Q3 earnings **2026-10-20 after the close**, consensus EPS 0.8385 on $13.14bn revenue (fetched calendar).

## [06:20 ET] MACRO — the oil leg, and how it fits the 5.24% 10Y
- WTI is running around **$93-95** and Brent **$105-109** on Middle East supply risk — Saudi facility attacks and tanker strikes reviving Hormuz fears; WTI crossed $100 roughly five weeks ago during US-Iran fighting. OPEC projects demand growth of 2.6 mb/d in 2027. Source: https://oilprice.com/Latest-Energy-News/World-News/
- **Price caveat: these are undated live tickers and they disagree** ($94.74 / $93.38 / $91.89 for WTI across three sites), and `market_data.py macro` could not fetch WTI at all. I am treating "oil in the low-to-mid $90s" as the usable fact and **not** quoting a precise crude print anywhere.
- This makes the macro read coherent rather than two unrelated observations: an oil shock at ~$93 is inflationary, and an inflationary impulse is what puts term premium into a 10Y at 5.24% while the funds rate sits at 3.88%. The rate trade and the energy trade are the same trade seen from two ends.

## [06:21 ET] SECTOR — energy's internal divergence, and why it is not a services buy
- Producers and the index are **at 120-day highs**: XLE 67.20 (-0.07% off high), XOM 174.08 (-0.46%), KMI 33.43 (-3.95%). Refiners ran hardest — VLO 456.46 sits 0.16% off its high after a 10-13 close up ~4.7%, DINO +4.3%.
- Oil **services are in a bear market at the same time**: SLB 48.77 (-19.3% off high), BKR 56.45 (-19.8%), HAL 32.79 (-24.8%). All three below both their 20- and 50-day averages.
- That divergence is the opposite of the usual relationship and the tempting trade is to buy the laggard. **Not taken.** The most likely explanation is that producers are returning cash rather than raising capex, so a high crude price does not convert into rig activity — but I could not source that, and buying a 25% drawdown on an unsourced hypothesis is the value trap this report keeps paying for. Logged as an open question for a future run.

## [06:22 ET] REJECTED — VLO — right thesis, no honest entry
- VLO 456.46 is **0.16% from its 120-day high** after doubling off the 227.25 range low, and sits 22% above its 372.94 50-day. A 2.0 ATR stop at ATR14 16.85 lands near 423, below which there is no structure at all until the high 300s; the 2.0 R:R target would be ~523, a 14% new high.
- Working against it: RBN reports the USGC 3-2-1 crack averaged $65/bbl through Oct 5, **down 8% from September**, with diesel cracks down 10% to $93/bbl. The equity is making highs while the margin data I can actually source is softening. Source: https://rbnenergy.com/daily-posts/analyst-insight/usgc-crack-spread-turns-down-volume-after-september-rally
- Chasing a 101% run into a 10-22 print on softening cracks is not a trade, it is momentum. Rejected.

## [06:22 ET] REJECTED — OXY — pending entry at 54.00 is stale and unfillable
- Published 2026-09-24 at 54.00; OXY closed 61.65, i.e. **14% above the entry** and only 3.3% off its 63.77 range high, above both averages. The market left the level behind. Re-publishing 54.00 would be publishing an order that cannot fill; re-pitching at 61.65 would be chasing. Left for the watchlist.

## [06:23 ET] REJECTED — TLT SELL_SHORT re-pitch — thesis strengthened, structure too thin, and the correlation cap binds
- The driver genuinely improved: oil in the low $90s plus a 10Y at 5.24% is the inflation impulse the short is built on, and TLT at 78.37 is below both its 79.01 20-day and 80.92 50-day.
- But at ATR14 0.782 (1.0% a day), the 1.8 ATR ETF stop floor and the 2.0 R:R floor together force the whole trade into a ~3.5% range: entry 79.90, stop ~81.31, target ~77.08 — and 77.08 is still above the 76.43 range low. R:R lands at exactly 2.00, which is the floor being met rather than cleared.
- **Correlation cap is the deciding reason.** XLF and TRV are already two ideas underwritten by the same rate path; a TLT short would be the third, and IYR and ITB shorts are pending on it too. Three is the cap and I would rather spend it on the two financials, which have dated catalysts this week, than on a thin duration short. Not captured.

## [06:24 ET] POSITION TRIAGE — the eleven remaining open positions
All prices are 2026-10-13 closes (market shut; previous close is the freshest honest price at 06:00 ET).

- **DAL** 79.57 vs 83.00 entry (-4.1%). **The one that needs saying out loud: it is 1.47 points from its 78.10 stop, 0.6 ATR, after eight consecutive lower closes (84.09 -> 79.57) straight through the 82.35 20-day and 83.26 50-day. The 10-13 low was 78.52.** decision: **hold, stop unchanged at 78.10.** Not closed early, because the remaining risk to the stop is 1.8% against 18.8% to target, and not widened, because moving a stop away from a losing position is how a 1.8% loss becomes a 10% one. An ordinary day takes this out and that is the stop working, not failing. Noting for the record that the original 78.10 stop was 1.99 ATR from entry — it cleared the 2.0 floor by rounding, and this is what that looks like three weeks later.
- **XLE** 67.20 vs 63.90 (+5.2%). At its 120-day high (67.245), 5.9% above the 63.44 20-day. decision: **hold, levels unchanged**; target 70.50 is 4.9% away and the oil backdrop is intact. Extended, so no adding here.
- **CCJ** 86.15 vs 94.00 (-8.4%). -34.3% off its 131.21 high, below both averages, stop 82.50 now 4.2% away and the 83.15 range low sits between price and stop. Revisions mildly deteriorating (81.8%, -3.9pts); insiders show no transactions either way. decision: **hold, stop unchanged.** The stop is below the range low and will answer this; no case for tightening it into weakness.
- **BCC** 74.08 vs 76.50 (-3.2%), no stop, long-term, target 110. -16.2% off high, below both averages. Thin for its size at $24.6M average daily dollar volume. decision: **hold**, no new information today.
- **CEG** 295.79 vs 272.00 (+8.7%). Above both averages, target 320 is 8.2% away. ATR is 5.17% a day, so this moves. decision: **hold, levels unchanged.**
- **SNX** 276.04 vs 260.00 (+6.2%), target 296.47. decision: **hold.**
- **LULU** short 94.34 vs 100.61 (+6.2% in favour), target 77.00, stop 112.00. decision: **hold.**
- **NKE** short 35.33 vs 38.40 (+8.0% in favour), target 32.10, stop 41.00. decision: **hold.** Both consumer shorts are working and neither has new information today.
- **PFE** 28.37 vs 27.60 (+2.8%), **EEM** 65.74 vs 65.60 (+0.2%), **KHC** 22.43 vs 23.00 (-2.5%). decision: **hold all three**, no new information, no level changes.
- None of the eleven is re-captured: an unchanged position with nothing new to say does not belong in the report as an idea. Only XLF, GE, HII and STLD had something that changed.

## [06:25 ET] SMALL-CAP SWEEP — what the earnings window actually contained
- Filtered the fetched calendar to 10-14..10-22 for revenue estimates between $40M and $600M: **153 names, and the overwhelming majority are small regional banks** (CBSH, EQBK, HOMB, WAFD, BANF, FFIN, GBCI, INDB, SFNC, BOKF, FNB, SFBS, AUB, HWC, OZK, UCB, BANR, BKU, CATY, EFSC...). All of them would be the same rate-path bet as XLF and TRV, which are already two of the three the correlation cap allows. Not pursued for that reason, not because none is any good.
- Non-bank small caps checked on price history: IRDM 46.73 (-18.3% off high, below both averages, no setup), PEGA 34.38 (sitting exactly on both averages, directionless), BJRI 60.03 (-19.5%, below both), BCPC 169.72 (-7.3%, mid-range), EPAC 35.22 (-7.3%, below both). None offered an entry worth publishing.
- **VICR was the one that did** — see below.

## [06:26 ET] NEW — VICR — captured, conviction 3, speculative size 1.5%
- Vicor, power conversion into datacenter build-out. Q3 print 2026-10-20, consensus EPS 1.03 on $172M revenue (fetched calendar). ADV $240M, liquid.
- The signal: **beat consensus in 4 of 4 quarters by +341.2%, +126.6%, +19.8%, +58.5%** on only ten analysts' coverage.
- Levels: last 267.24, ATR14 19.39 (**7.25% a day**). Entry 258-272, stop 225.00 below both the 10-13 reversal low (244.53) and the 230.06 sma50 = 2.17 ATR, target 351 below the 382.65 range high. R:R 2.00.
- 10-13 was a reversal bar: low 244.53, close 267.24, upper third of the range after nine down sessions, ending a 26% drawdown from the 10-01 high of 331.
- **The honest other side, stated in the idea:** insiders sold **567 times for $202.6M with zero open-market buys**, and consensus has risen from 0.1428 a year ago to 1.03 — the bar is 7x higher than the one it beat by 341%, so the surprise edge is largely competed away. Sized 1.5% accordingly.

## [06:28 ET] OPEN QUESTION, NOT PUBLISHED — why are oil services 20-25% off their highs with crude in the low $90s?
- Researched deliberately as the most interesting anomaly of the day and **deliberately not published**, because the evidence came back conflicting and the one bullish source is unreliable.
- For: Halliburton reportedly added **30 rigs to the US land market** in the quarter; Diamondback is said to be abandoning the capital-discipline framework and adding rigs and frac crews, with Continental reversing a planned 20% spending cut. **That source reads as promotional and speculative and I am not underwriting a position on it.** Source: https://oilprice.com/Energy/Energy-General/5-Oilfield-Services-Stocks-Built-for-a-Post-Hormuz-World.html
- Against: E&P consolidation has flattened activity, and Halliburton's 2025 revenue *fell* to $22.18bn from $22.94bn. SLB guided 2026 capital investment to ~$2.5bn, roughly flat with 2025. Sources: https://discoveryalert.com/analysis/investing-fracking-supply-chain-oilfield-services-stocks/ | https://investorcenter.slb.com/news-releases/news-release-details/slb-announces-first-quarter-2026-results
- Also note a genuine conflict with my own fetched data: a September piece puts SLB **+27% and HAL +13% year to date**, while nasdaq history has them 19.3% and 24.8% **below their 120-day highs**. Both can be true — up on the year, sharply off a recent peak — and it is a reminder that "off its high" and "down" are different statements.
- **Resolving datapoints are already dated: HAL reports 2026-10-20 and SLB 2026-10-23.** A future run should take the anomaly up again with those prints in hand rather than guessing ahead of them. If capex really is turning, services is the highest-torque long in energy and it is currently the cheapest part of the sector.

## [06:29 ET] LONG-TERM LANE — why only one, and why that is not padding
- Only HII was captured in the long-term lane today, and it is an update rather than a new thesis. The lane is not neglected: **CCJ, BCC and PFE are already open long-term positions** and all three were reviewed above; none had new information warranting a change.
- The two new long-term theses I actually worked on both failed on evidence rather than on time: **WDC** (de-rating real, but 23.3x forward on an annualised run-rate is not a valuation anchor) and **oil services** (sourcing too weak). Publishing either would have been filling the lane rather than finding something for it.

## [06:31 ET] FINAL CHECK — every captured idea recomputed against the floors
Recomputed from the levels actually written to candidates.jsonl, using the ATR14 values fetched this morning. Nothing here is taken from what the idea claims about itself.

| Sym | Dir | Horizon | Conv | Entry | Target | Stop/Bear | R:R | Stop (ATRs) | Floor | Baseline win% | Claimed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLF | buy | swing | 3 | 54.23 | 57.60 | 52.80 | 2.36 | 2.20 | 1.8 (etf) | 29.8 | 42 |
| TRV | buy | swing | 4 | 370.00 | 398.00 | 356.50 | 2.07 | 2.40 | 2.0 | 32.5 | 40 |
| STLD | buy | swing | 3 | 245.50 | 281.00 | 228.75 | 2.12 | 2.58 | 2.0 | 32.1 | 38 |
| HII | buy | long_term | 5 | 258.00 | 430.00 | 195.00 (bear) | 2.73 | n/a | 2.5 R:R | n/a | n/a |
| GE | buy | swing | 3 | 308.00 | 341.00 | 292.00 | 2.06 | 2.24 | 2.0 | 32.7 | 36 |
| NFLX | sell_short | swing | 4 | 73.00 | 64.00 | 76.10 | 2.90 | 2.13 | 2.0 | 25.6 | 38 |
| VICR | buy | swing | 3 | 267.00 | 351.00 | 225.00 | 2.00 | 2.17 | 2.0 | 33.3 | 40 |

- All seven clear both floors. The largest claimed edge over baseline is XLF at +12.2 points, well inside the 20-point threshold where a thesis has to carry an unusual claim.
- No stop was moved inward to make a ratio work. VICR is at exactly 2.00 and was left there rather than trimmed to 230 to manufacture 2.3.

## [06:32 ET] CORRELATION CHECK — drivers behind the seven
- **Rate path / financials (2):** XLF, TRV. Cap is 3; the third slot was deliberately left empty rather than spent on the TLT short (see 06:23).
- **Defense budget (1):** HII. **Industrial earnings (1):** GE. **Steel earnings (1):** STLD. **Media earnings short (1):** NFLX. **Datacenter power (1):** VICR.
- No driver carries more than two ideas. Note that GE, STLD and VICR all resolve on prints inside 10-19..10-20, so while their *theses* are independent their *timing* is not — a bad tape that week marks all three at once.

## [06:33 ET] RESEARCH COMPLETE
- candidates: **7** (XLF, TRV, STLD, HII, GE, NFLX, VICR)
- of which: 4 are updates or re-pitches of existing lines (XLF hold, GE hold, HII pacing update, STLD unfilled re-pitch) and **3 are genuinely new** (TRV, NFLX short, VICR)
- horizon skew: **6 swing, 1 long_term, 0 intraday**. Nothing intraday was published and that is a deliberate consequence of the data: every equity price available at 06:00 ET is the 2026-10-13 close, and `config/strategy.md` requires precise levels for an intraday idea. Setting intraday levels off a previous close would be inventing them.
- asset-class skew: **6 stock, 1 etf, and zero crypto, futures or event contracts.** This is a source outage, not a judgement — see the gaps below. On an ordinary day at least one of those three would have been in scope, and the bearish-crypto and index-view substitutions in `config/universe.md` were simply unavailable to me.
- track record applied: the report is 2/18 to target overall and **0/11 on single stocks**, so the bar was raised rather than the count. WDC, VLO, OXY, ITB, TLT and the oil-services long were all worked up and all rejected; six rejections against seven captures is the right shape for a day with that record. The sample is under the ~15 closed trades at which a by-category read stops being noise for most buckets, so I have not cut a category outright.
- **coverage gaps:**
  - No index level anywhere: ^GSPC, ^NDX, ^DJI, ^RUT and **^VIX** all failed on every source (finnhub needs a CFD subscription, yahoo returned HTTP 429, stooq 404). I have no volatility reading at all today.
  - No crypto prices (CoinGecko failed), so no crypto idea could be priced or stopped.
  - No futures quotes (ES, NQ), no DXY, no gold, no WTI from `macro`. The WTI figure used for context came from undated third-party tickers that disagreed by ~$3, and is deliberately described only as "low-to-mid $90s" rather than quoted.
  - No event contracts: Kalshi returned `ok: true` with **count 0** for both "Fed" and "CPI". The two pending Fed contracts could not be re-priced and were left untouched.
  - No options-implied move for any idea: yahoo-options returns **HTTP 401** on every call. The "is your target inside what the market prices" check could not be run once today.
  - No short interest or days-to-cover for any name: api.nasdaq.com timed out on NFLX, TRV and WDC. This matters most for the NFLX short, where squeeze risk is the main risk and is stated as unquantified in its key_risk.
  - Could not source a cause for two real moves: DINO +4.3% on 10-13 (position hit its 128.00 target) and SMMT -9.4% on 10-13. Both recorded as unexplained rather than attributed.
- sources that failed: yahoo finance chart API (429), yahoo options API (401), stooq (404 on indices), CoinGecko, finnhub index quotes (subscription), Kalshi via market_data events (empty), api.nasdaq.com short-interest endpoint (timeout).
- sources that worked: finnhub quotes and earnings calendar and analyst/insider endpoints, api.nasdaq.com historical bars, FRED, SEC EDGAR filings, WebSearch.

## [06:34 ET] CORRECTION + MAJOR CATALYST — event contracts ARE available, and **CPI prints at 08:30 ET today**
**This supersedes the 06:03 note "event contracts unavailable" and part of the 06:33 RESEARCH COMPLETE gap list.** `market_data.py events` returning count 0 was a failure of the wrapper, not of the source. Querying the Kalshi API directly returns live, deep markets.

**September CPI is released today, 2026-10-14 at 08:30 ET** — about two hours after this report publishes. Confirmed two ways: the `KXCPIYOY-26SEP` contracts all close at 2026-10-14T12:29:00Z (08:29 ET), and the published BLS schedule lists the September CPI for 08:30 ET today. Prior print (August, released 09-11) was **3.4% YoY**. Source: https://eco3min.fr/en/next-us-cpi-release/

Market-implied distribution for September CPI YoY (Kalshi yes bid/ask, fetched 06:30 ET):

| Threshold | Yes bid/ask | Implied P(above) |
| --- | --- | --- |
| Above 3.3% | 0.98 / 0.99 | ~98% |
| Above 3.4% | 0.95 / 0.98 | ~96% |
| Above 3.5% | 0.88 / 0.90 | ~89% |
| **Above 3.6%** | **0.44 / 0.48** | **~46%** |
| Above 3.7% | 0.09 / 0.11 | ~10% |
| Above 3.8% | 0.01 / 0.03 | ~2% |

Read: the market expects CPI to **accelerate from 3.4% to roughly 3.6%**, with almost no weight below 3.4%. That is consistent with everything else today — oil in the low $90s, a 10Y at 5.24%, and the Fed path below.

Fed decision markets (Kalshi, fetched 06:30 ET), open interest in the hundreds of thousands to 1.5M contracts:
- **2026-10-28 FOMC:** maintain **81-82c**, hike 25bps **17-18c**, any cut ~1c.
- **2026-12-09 FOMC:** **hike 25bps 73-75c**, maintain 22-24c, hike >25bps 2-3c, any cut ~1c.
- Read: the market has a hold in October and a **74% chance of a 25bp HIKE in December**. The easing cycle is priced as over and reversing.

## [06:36 ET] NO EVENT CONTRACT PUBLISHED — and this time for the right reason
- The markets are live, deep (OI 122k on the 3.6% strike, 1.58M on the October hold) and tightly quoted at 1-4c wide. `config/universe.md` requires the edge to be an explicit probability disagreement with a stated reason.
- **I do not have one.** I have no independent September CPI estimate — I could not fetch the monthly crude path or the energy weight, and headline-versus-core is exactly where the print is decided. Taking the other side of a deep, tight market two hours before resolution on the strength of "oil is high, so CPI runs hot" is the hunch the config forbids, and the market has already priced that reasoning into the 3.4% -> 3.6% acceleration.
- So: no event idea today, but the gap list must say *"no defensible edge"*, **not** *"source unavailable"*. Those are different failures and only one of them is mine.

## [06:37 ET] PENDING ORDER — KXCPIYOY-26SEP-T3.5 NO @ 18 (published 09-30) — **recommend cancelling before 08:30 ET**
- The contract resolves **today at 08:30 ET**. NO on "Above 3.5%" is a bet that September CPI lands at or below 3.5%; the market now prices that at **10-12c**, i.e. ~11%.
- The order has never filled and sits at 18c against an offer around 11c. Filling it today means buying a ~11% shot with hours to resolution and no independent estimate behind it. There is no edge and no time for one to appear.
- **Action: cancel the resting order.** It is not a loss — it never filled — but leaving it live into a print is an unmanaged bet, and it would be the only idea in the book with no thesis behind it as of this morning.

## [06:40 ET] RESEARCH COMPLETE — ADDENDUM, supersedes the 06:33 block
The 06:33 block stands except where corrected here. Three things changed after it was written.

**1. The event-contract gap was mine, not the data's.** `market_data.py events` returns count 0, but the Kalshi API queried directly returns live, deep markets. The 06:33 gap list said "no event contracts available"; the correct statement is **"event contracts available, no defensible edge found"**. Recovering that source also turned up the single most important fact of the morning, which the first pass missed entirely.

**2. September CPI prints TODAY at 08:30 ET**, two hours after this report publishes, and the market prices an acceleration from 3.4% to ~3.6%. Confirmed against the BLS schedule and the 08:29 ET close on the `KXCPIYOY-26SEP` contracts. Kalshi also prices a **74% chance of a 25bp Fed HIKE on 2026-12-09** and ~1c on any cut. XLF and TRV were **re-captured** to carry this: the 08:30 print is now named in both catalysts and stated first in both key_risks, because nothing in any price quoted in this report reflects it. TRV's entry instruction changed from a resting order to "let the print clear first".

**3. Two conviction scores were wrong and are fixed.**
- **TRV** was briefly raised to 5 on a fourth evidence kind labelled `valuation_anchor`. That was an inflation: the entry was a rate-path argument, not a defended valuation with a method shown. Reclassified to a second `positioning` read, which adds no kind. **Back to 4.**
- **GE** carried its negative relative-strength figure in `evidence`, which would have counted a fact arguing *against* the idea toward its conviction. Moved into `counter_argument`. **Stays 3**, now on 2 genuine kinds.
- **VICR** was under-scored at 3 against three genuine confirmations and is now **4**; the insider selling that made me hesitate is a risk, and it lives in `key_risk` and `counter_argument` where risks belong.

**Final state: 7 candidates, every conviction score equal to its count of distinct evidence kinds, every R:R and stop distance above its floor.**

| Sym | Dir | Horizon | Conv | Kinds | R:R | Stop (ATRs) |
| --- | --- | --- | --- | --- | --- | --- |
| HII | buy | long_term | 5 | 4 | 2.73 | n/a (bear case 195) |
| XLF | buy | swing | 4 | 3 | 2.36 | 2.20 |
| TRV | buy | swing | 4 | 3 | 2.07 | 2.40 |
| NFLX | sell_short | swing | 4 | 3 | 2.90 | 2.13 |
| VICR | buy | swing | 4 | 3 | 2.00 | 2.17 |
| STLD | buy | swing | 3 | 2 | 2.12 | 2.58 |
| GE | buy | swing | 3 | 2 | 2.06 | 2.24 |

**Corrected gap list** (replaces the 06:33 one): no index or VIX level anywhere (yahoo 429, finnhub subscription, stooq 404); no crypto prices (CoinGecko); no futures, DXY, gold or WTI quotes; no options-implied move for any idea (yahoo-options 401); no short interest for any name (api.nasdaq.com timeout) — which is the main unquantified risk in the NFLX short; and no sourced cause for DINO +4.3% or SMMT -9.4% on 10-13. **Event contracts are NOT a gap** — they were fetched, priced and deliberately not traded.

One thing for whoever reads this next: **the oil-services anomaly at 06:28 is the best unfinished idea on the page**, and HAL on 10-20 and SLB on 10-23 are the prints that resolve it.
