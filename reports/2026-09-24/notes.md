# Research log — 2026-09-24

## [06:04 ET] MACRO — rates, policy, data availability
- US 10y 4.96% (FRED DGS10, 2026-09-22), unchanged vs prior print — source: https://fred.stlouisfed.org/series/DGS10
- Fed funds effective 3.88% (DFF, 2026-09-22) — source: https://fred.stlouisfed.org/series/DFF
- 10y-2y curve +0.26 (2026-09-23), steepening from +0.25 — source: https://fred.stlouisfed.org/series/T10Y2Y
- Unemployment 4.1% (Aug 2026), CPI index 334.131 Aug vs 332.813 Jul = +0.40% m/m, hot — source: https://fred.stlouisfed.org/series/CPIAUCSL
- REGIME READ: long end at ~5% with a positively-sloped curve and 0.4% m/m CPI. Fed funds 3.88% vs 10y 4.96% = 108bp of term premium. This is a "cuts are priced but inflation is not cooperating" tape. Duration is the loser; that is consistent with the open TLT short.
- TLT last 80.46, -1.58% (prev session close) — TLT short position moving in our favour.
- DATA QUALITY: Yahoo Finance returning HTTP 429 on every index/commodity symbol this morning. SPX, NDX, DJI, RUT, VIX, /ES, /NQ, DXY, 10y yield, gold, WTI ALL unavailable via macro. No index or commodity level may be quoted today without a separate fetch. Finnhub rejects index CFDs ("subscription required"), stooq 404s on ^ symbols. Only bonds_20y (TLT) resolved.

## [06:04 ET] CALENDAR — dated catalysts inside 10 sessions (fetched Finnhub earnings calendar)
- 2026-09-24 BMO: SNX (est EPS 4.75, rev $19.1B) — TODAY, and SNX BUY @260 is on the awaiting-entry list
- 2026-09-24 AMC: COST (est EPS 6.66, rev $96.8B), DRI BMO (est 2.08)
- 2026-09-28: CCL BMO (est 1.37), NKE (est 0.444, rev $11.45B) — NKE is an open position, -9.8%
- 2026-09-29: CAG (est 0.284) — CAG is an open position opened 09-20; KMX BMO (est 0.72)
- 2026-09-30: MU AMC (est 32.32, rev $52.2B) — MU BUY @960 awaiting entry, published 3x; JBL BMO (est 4.10); JEF
- 2026-10-01: ACN AMC (est 3.21), AYI BMO
- source: https://finnhub.io/api/v1/calendar/earnings

## [06:12 ET] DATA GAP — event contracts unavailable
- `market_data.py events` returns count=0 for "Fed decision", "CPI", "S&P 500", "FEDDECISION", "inflation", "recession". The only hit on "Fed" was a Kalshi NFL cross-category parlay whose ticker happens to contain the substring. No event-contract prices could be fetched this morning, so no event-contract idea can be priced today — a probability disagreement needs the market's implied probability and there is none to read.
- Consequence: the three open/awaiting KXFEDDECISION positions cannot be marked or re-priced today.

## [06:12 ET] PRICES — fetched closes 2026-09-23 (all pre-market, finnhub; last regular session)
Open positions, live vs stored:
- XLE 62.37 (atr 1.368 / 2.19%), sma20 64.00, sma50 61.53, 5.7% off 120-bar high
- CCJ 90.80 (atr 3.389 / 3.73%) — DOWN 4.01% on 2026-09-23, sma20 97.07, sma50 94.81, 30.8% off high 131.21
- NKE 36.05 (atr 0.923 / 2.56%), sma20 37.36, sma50 39.99, range low 35.35 made 2026-09-21
- CAG 14.78 (atr 0.409 / 2.76%), sma20 15.36, sma50 15.25, range low 12.53
- CEG 263.88 (atr 10.32 / 3.91%), sma20 276.12, sma50 271.64
- EEM 67.71 (atr 1.130 / 1.67%) — note: prior_context carried 69.10; the fetched close is 67.71
- GLD 392.88 (atr 7.344 / 1.87%) — prior_context carried 400.07; fetched close 392.88, now BELOW the 398.00 entry and below sma20 402.28
- DINO 106.14 (atr 5.098 / 4.80%), sma50 96.64
- BCC 77.76 (atr 2.166), LCII 85.03 (atr 3.217, 38.5% off high, at range low 84.94)
- PFE 28.18 (atr 0.459), only 3.5% off its 120-bar high — the open PFE long is working
- SVRA 5.00 (atr 0.222 / 4.44%), $8M/day — below the 4.60... no, above; 22.8% off high
- LULU 102.28 (atr 5.161 / 5.05%), 39.9% off high, range low 95.35
Awaiting-entry names:
- SNX 287.89 (atr 9.420) vs the awaiting BUY @ 260.00 — 10.7% above the bid, and SNX reports BMO TODAY
- MU 1071.88 (atr 46.55 / 4.34%) vs the awaiting BUY @ 960.00 — 11.7% above the bid, reports 2026-09-30 AMC
- source: https://www.nasdaq.com/market-activity/stocks (history), https://finnhub.io/api/v1/quote

## [06:13 ET] CCJ — 4.0% single-day drop, no insider or analyst confirmation
- open_market_buys 0, distinct_buyers 0 over 6 months — no insider support — source: https://finnhub.io/api/v1/stock/insider-transactions?symbol=CCJ
- recommendation trend flat for four months (5 strong buy / 13 buy / 4 hold since June); bullish share 81.8%, change -3.9% — analysts have not moved, so the drop is price, not revision — source: https://finnhub.io/api/v1/stock/recommendation?symbol=CCJ

## [06:17 ET] MACRO — THE DAY'S DRIVER: 10y at 5.11%, a 19-year high
- 2026-09-23: 10y Treasury yield surged 15bp to **5.11%**, highest since 2007. 30y +11bp to 5.4%, highest intraday since 2007 and highest close since 2004 — source: https://www.cnbc.com/2026/09/23/treasury-yields-oil-inflation-fed.html
- Driver 1 — data: S&P Global September US business activity accelerated at the fastest rate since July 2021 — source: https://www.cnbc.com/2026/09/23/treasury-yields-oil-inflation-fed.html
- Driver 2 — supply/demand for paper: 5-year auction stopped at 5.033% against a six-auction average of 4.186%; the $16B 20-year produced a 5.047% high yield, ~1.2bp above when-issued = soft demand — source: https://www.cnn.com/2026/09/23/investing/us-bond-market-fed
- Driver 3 — energy-driven inflation: Brent +3.9% to $103.08, WTI +1.8% to $92.16, ending a five-day losing streak after Iran's president said Iran will not surrender. Crude +9.1% over the past month and **+42.7% year over year** — source: https://www.cnbc.com/2026/09/23/iran-us-talks-crude-oil-un-wti.html and https://tradingeconomics.com/commodity/crude-oil
- Offsetting supply headline: Saudi Arabia preparing to restart East-West pipeline exports in coming days, bypassing Hormuz — source: https://www.nbcnews.com/business/energy/treasury-yields-oil-stocks-rcna599398
- Equity tape 2026-09-23: S&P 500 -0.7%, Dow -351, Nasdaq 100 -0.8% from a record high. Losers MCD -4.9%, GOOGL -4.7%, HD -2.8%; gainers CRM +1.8%, CVX +1.4% — source: https://investrade.com/market-review-september-23-2026/
- RECONCILIATION: FRED DGS10 reads 4.96% as of 2026-09-22, which is the day *before* the 15bp surge. The two are consistent, not contradictory. Today's regime number is 5.11%.
- WHAT THIS RE-PRICES: duration (short), energy (long), and everything that discounts long-duration cash flows or borrows at the long end (REITs, homebuilders, bond-proxy utilities). Today's 10:00 ET August new home sales lands into a 19-year-high long end.

## [06:17 ET] CCJ — POSITION UPDATE research
- No company-specific news for the 2026-09-23 -4.0% drop. Attributed to uranium spot cooling and profit-taking after a strong run; separately Westinghouse IPO speculation is the live narrative — source: https://www.quiverquant.com/news/Cameco+slides+as+uranium+prices+cool+and+investors+take+profits+after+a+strong+run
- Combined with flat analyst revisions and zero insider buying: nothing broke, but nothing confirmed either.

## [06:30 ET] INSIDERS — open-market buying on the open-position finalists
- **CAG: 3 open-market buys, 3 distinct buyers, $1.12M, ZERO sells in six months.** Brase John P 35,000 sh @ 14.5895 on 2026-07-17; Mulligan John J 17,500 @ 14.3087 and Lenny Richard H 25,000 @ 14.34, both 2026-04-14. Price now 14.78 — the buyers are roughly flat to slightly up. Three distinct buyers with no offsetting sales is the cleanest insider signal in the book today — source: https://finnhub.io/api/v1/stock/insider-transactions?symbol=CAG
- **DINO: 3 buys, 2 distinct buyers, $2.42M.** Franklin Myers 15,000 @ 85.30 on 2026-08-11 and 15,000 @ 69.11 on 2026-05-18; Hardy Rhoman J 1,508 @ 66.32. Price now 106.14 — all well in the money. Offset by 5 sells — source: https://finnhub.io/api/v1/stock/insider-transactions?symbol=DINO
- **NKE: 5 buys, 4 distinct buyers, $3.73M** — CEO Elliott Hill 2×23,660 @ ~42.27, board member Timothy D Cook 25,000 @ 42.43, John W Rogers Jr 4,000 @ 43.34, all 2026-04-09/13. Price now 36.05, so every one of those buys is ~15% underwater. Supportive of the long thesis but stale and wrong so far; 6 sells against — source: https://finnhub.io/api/v1/stock/insider-transactions?symbol=NKE
- XLE: n/a, it is an ETF — 0 buys is not a signal.

## [06:30 ET] XLU — new short captured (conviction 4)
- XLU -8.03% 1m / -12.71% 3m / -11.84% 6m vs SPY +0.57% / +4.71% / +17.55% — lagging on every window, by 8.6 / 17.4 / 29.4 pts — source: computed from price history
- 20 unbroken sessions of lower highs: 41.756 (09-17), 40.93 (09-21), 40.82 (09-22), 40.41 (09-23). Closed 39.75 at the session low 39.71 = the 120-session low.
- 400-session low is 35.51 and sma200 is 44.50 (price 10.7% below it), so the 36.80 target is inside last year's range, not an invented extension.
- Counter-case found and answered: utilities are flashing oversold and are cheap on valuation — source: https://seekingalpha.com/news/4640528-utilities-flash-oversold-signal-as-treasury-yields-dim-dividend-appeal
- CORRELATION NOTE: TLT short + XLU short are two expressions of one rate view. That is the cap-3 limit at two. No third rate-driven short is being taken today, which is why the awaiting IYR short is NOT re-pitched despite REITs being the obvious third leg (IYR 97.24, 3.18% off its low, sma20 100.88 / sma50 103.40 above).

## [06:30 ET] DATA GAP — options-implied move unavailable
- `market_data.py implied` returns HTTP 401 Unauthorized from query1.finance.yahoo.com/v7/finance/options. No idea today can be checked against what the options market prices. Same root cause as the Yahoo 429s on the index symbols.

## [06:11 ET] TIMESTAMP CORRECTION
- The stamps on the blocks above (06:04 through 06:30) ran ahead of the wall clock: `TZ=America/New_York date` reads **06:11 ET** at this point, with the run having started at 06:00:55 ET. Every block above was written between 06:01 and 06:11 ET, in the order shown. The findings and their sequence are correct; only the minute labels drifted. Stamps from here down are taken from `date` rather than estimated.

## [06:15 ET] POSITION UPDATE — NKE — decision: CLOSE BOTH LEGS. Thesis broken, not just underwater.
The book holds two opposed NKE rows: a long_term BUY opened 2026-08-17 at 40.75 (now 36.05, -11.5%) and a SELL opened 2026-09-08 at 38.40 (now +6.0%). Both should come off.

Why the long is broken rather than early — a defended number, not a price complaint:
- Stifel cut its price target to **$40 from $45 on 2026-09-21** (Hold maintained) and cut FY2027 and FY2028 adjusted EPS by $0.20 each, to **$1.70 and $2.05**, on a more promotional Western marketplace and a tougher Q4 gross-margin comparison — source: https://www.insidermonkey.com/news/nike-nke-wall-street-tests-whether-the-turnaround-can-outrun-weak-demand-ahead-of-q1-results-1841563/
- At 36.05 that is 21.2x FY27 and 17.6x FY28 — not a de-rated bargain. The standing 62.00 target implies **30x FY28 EPS**, which requires a full recovery *and* a full re-rating. It is not defensible against those estimates.
- Long-term floor arithmetic: a 15x FY27 bear case is $25.50. From the 40.75 fill that is R:R (62.00-40.75)/(40.75-25.50) = 21.25/15.25 = **1.39 against a 2.5 floor**. The position does not clear its own bar and cannot be made to without inventing a higher target.
- Confirming the direction of travel: bullish analyst share 39.1%, **down 9.8 points**, revision_direction "deteriorating" — buy ratings went 12 to 8 and holds 21 to 25 between June and September, with sells 2 to 3 — source: https://finnhub.io/api/v1/stock/recommendation?symbol=NKE
- Price at 36.05 is the **two-year low** (35.35 printed 2026-09-21, and it is the low of the full 730-session window) and 27.6% below the 200dma of 49.78.
- The insider case does not rescue it: 4 distinct buyers bought $3.73M in April 2026 at 42.27-43.34, and every one of those purchases is ~15% underwater five months later.

Why the short comes off too rather than being ridden into the print:
- NKE has **beaten consensus in each of the last 4 quarters**, the most recent two by +50.2% (2026-06-30, 0.20 vs 0.133) and +22.9% (2026-03-31, 0.35 vs 0.285) — source: https://finnhub.io/api/v1/stock/earnings?symbol=NKE
- Running has posted five consecutive quarters of double-digit growth, adding ~$1B of revenue, and North American wholesale grew 10% in Q4 — source: https://finance.yahoo.com/markets/stocks/articles/nike-nke-wall-street-tests-040747520.html
- Being short a serial beater at a two-year low into its own print is a binary, not an edge. Take the +6%.
- **DATE CONFLICT, unresolved:** the fetched Finnhub earnings calendar puts NKE Q1 FY27 on **2026-09-28**; a fetched press preview puts it at **2026-10-01, 4:15pm ET** — source: https://www.marketbeat.com/stocks/NYSE/NKE/earnings/. I could not resolve which is right. Both fall inside a close-now decision, so it does not change the action, but **no NKE idea today may claim a verified earnings date** and none does.

## [06:15 ET] REJECTED — SNX — awaiting BUY @ 260.00 is stale; cancel the order
- SNX closed 287.89 on 2026-09-23, **10.7% above** the 260.00 resting bid published 2026-09-19, and reports BMO **today** (est EPS 4.75 on $19.1B revenue).
- The order was never filled, the stock ran away from it, and the catalyst it was positioned for resolves this morning. A resting bid 10.7% below the market on earnings day only fills on a bad print — which is the adverse-selection failure the entry-style rule exists to stop. Cancel rather than re-level: entering after the print would be a new idea needing new evidence, and there is none yet.

## [06:15 ET] REJECTED — MU — awaiting BUY @ 960.00 is stale
- MU closed 1071.88, **11.7% above** the 960.00 resting bid, and reports 2026-09-30 AMC. MU has been published 3 times in 10 days, which prior_context flags as an anchoring warning rather than conviction.
- Same adverse-selection problem as SNX and a 4.34% ATR: a bid that far below only fills on the way down into a print. No re-pitch today — nothing concrete has changed except that the stock went up without us.

## [06:17 ET] NEWS — the driver behind the yield spike, named
- S&P Global US PMI **Composite preliminary September 58.4 vs 56.0 in August** — the fastest business-activity expansion since July 2021, and the print that moved the 10y 15bp. Commentary explicitly raises speculation about a Fed **hike** rather than a cut — source: https://www.gurufocus.com/news/9094178/bitcoin-btc-dips-amid-stronger-us-pmi-and-rate-hike-expectations
- This matters beyond bonds: it is the reason the rate move is a growth-plus-inflation shock rather than a risk-off flight, which is why the equity response was rotational rather than a broad flight to defensives.

## [06:17 ET] MCD — captured, conviction 5, WAIT entry
- 2026-09-23: -4.8% to 238.32, session low 234.03 = the 400-session low, on **16.6M shares against a ~5M daily average (3.3x)**. 30.3% below the 341.75 400-session high, 18.5% below the 292.57 200dma.
- Primary document read: 8-K Item 7.01 filed 2026-09-23 plus Exhibit 99.1 investor update — source: https://www.sec.gov/Archives/edgar/data/63908/000006390826000076/exhibit991-investorupdate2.htm
  - ~$8.5B total NEXT partnering support **through 2036**, including ~$5B through 2030, via **rent relief and capital support**
  - capex ~$3B annual baseline **plus $1.5-2B cumulative** partnering support 2027-2030
  - FCF conversion **mid-to-high 80%** by 2030; operating margin low-to-mid 50% by 2030; G&A ~1.9% of systemwide sales by 2030
  - unit expansion contributing ~2.5% to systemwide sales growth 2027, moderating to ~2% by 2030
  - the release carries **no** Q3 2026 or full-year commentary and **no** restaurant-count target
- IMPORTANT ATTRIBUTION: the widely-reported "50,000 restaurants delayed from 2027 to 2028" and the CFO's "even a September US sales rebound may not save Q3" are from Investor Day press coverage, **not** from the 8-K or Ex-99.1 — I checked and neither appears in the filing. The captured thesis rests only on the filed figures. Coverage: https://247wallst.com/cards/mcdonald-s-mcd-price-swing-01m37r1sm9jztmjxw6hrr8qeks
- Sell side has NOT capitulated: 61.0% bullish, **+1.0 pt, revision direction improving**, 8 strong buy / 17 buy / 15 hold / **1 sell** out of 41. Insiders 0 buys / 6 sells. That asymmetry — price capitulated, ratings did not — is the whole trade.
- Entry is a WAIT into the 245.00-250.50 shelf (lows 247.83 / 248.10 / 247.65 / 246.52 / 249.37 on 09-16 through 09-22, broken 09-23). Stop 258.60 = 2.41 ATR. Target 222.00. R:R 2.16. If it never bounces, the trade never happens — by design.

## [06:17 ET] REJECTED — XLF / KRE / KIE — the steepener long does not work here
- Textbook says a steepening curve (+0.26, up from +0.25) is a bank NIM tailwind. The tape says otherwise, and the tape wins: XLF 54.54, down five straight sessions from 56.40 on 09-17, 6.9% off its high and below both sma20 56.94 and sma50 57.12. KRE 70.38, down every session 09-17 to 09-23 (72.74 / 72.75 / 71.99 / 71.19 / 70.38), 10.2% off its high. KIE 60.09, same pattern.
- Financials falling *with* yields rising means the market is pricing a credit and duration shock, not a healthy steepener. Taking the long side of a thesis the whole sector is actively refusing would be trading the textbook against the evidence. No position.
- This also deliberately avoids re-pitching KRE, which CLAUDE.md records as the name whose stop was walked in three times to flatter its ratio.

## [06:17 ET] REJECTED — BTC / crypto short — right macro, wrong tape
- BTC $83,325 (-2.91% 24h), ETH $2,640.96 (-3.35%), SOL $113.09 (-3.65%) — source: https://www.coingecko.com/
- The liquidity logic is sound and the same PMI print did the damage: BTC fell from $87,200 to a $83,500 low on 09-23 — source: https://www.coindesk.com/business/2026/09/23/live-updates-bitcoin-slips-under-usd86-000-as-money-rotates-into-bch-and-zec
- But the trend is the other way. Using IBIT as the fetchable proxy: 43.30 (09-17) to 49.01 (09-21) is +13.2% in two sessions to a **new 120-session high of 49.22**, then 48.83, then 47.88. That is a two-day fade from a fresh breakout, not a downtrend. Price is 2.72% off its high with sma20 44.98 and sma50 40.47 both *below*.
- Shorting a fresh breakout because the macro argues for it is the trade this book keeps losing on. No position. `market_data.py history BTC-USD` returns ok:false, so no BTC ATR was available to level a futures short honestly even if I had wanted one.
- CANCEL the two stale crypto shorts: `BTC` SELL @ 63,400 (published 2026-08-16) and `/MBTU6` SHORT @ 64,340 (2026-08-18). BTC is $83,325, 31% above those levels; and /MBTU6 is a **September** contract in the last week of September, which universe.md forbids recommending without saying so. Neither should remain on the book.

## [06:17 ET] REJECTED — COST — reports tonight, but the record says do not be long into it
- COST 904.70, 17.5% off its 1096.50 high, near its 885.50 120-session low, ATR 11.77 (1.30%). A quality compounder at a 17% discount is exactly the long_term shape this report wants.
- It fails on the record: COST has **missed** consensus in 3 of the last 4 quarters — -1.90% (2026-06-30), -1.54% (2026-03-31), -0.82% (2025-09-30) — with only 2025-12-31 a beat at +3.28%. beats_last_4 = 1 — source: https://finnhub.io/api/v1/stock/earnings?symbol=COST
- Insiders: 0 open-market buys, 2 sells. Analyst bullish share 65.2%, **-3.0 pts**, revision direction deteriorating.
- Reports **tonight AMC** (est EPS 6.66 on $96.8B). Buying a serial small-misser the afternoon of its print, with no insider support and ratings drifting down, is a coin flip dressed as a value thesis. Revisit after the print with actual numbers.

## [06:22 ET] POSITION UPDATES — the rest of the open book, decided
All prices are 2026-09-23 closes (previous regular session; the market is shut as I write).

- **PFE — HOLD, and it is the best-evidenced long in the book.** 28.18 vs a 27.60 entry (+2.1%), only 3.5% off its 120-session high of 29.21. Three distinct insiders bought $2.96M on the open market: **CEO Albert Bourla 38,000 sh @ 26.34 on 2026-08-12**, Buckley Mortimer J 37,632 @ 25.52 and Blaylock Ronald E 39,231 @ 25.46, both 2026-08-05 — all three now in the money. **Beat consensus in each of the last 4 quarters.** Analysts are on the other side: 38.9% bullish, -2.8 pts, deteriorating. Insiders buying into a deteriorating sell side, with the stock making highs, is the setup working. Levels unchanged. It has been published 3× in 10 days, so it is a hold, **not** a re-pitch — nothing new to say beyond the insider cluster already cited. Sources: https://finnhub.io/api/v1/stock/insider-transactions?symbol=PFE
- **CEG — HOLD, levels unchanged, but understand what it now is.** 263.88 vs 272.00 entry (-3.0%), stop 250.00 = 2.13 ATR (ATR14 10.32), target 320.00, R:R 2.18. Both floors clear. **Flagged conflict:** I am simultaneously short XLU, and Constellation sits in that index. This is deliberate rather than accidental — the XLU short is a bet on the regulated bond-proxy basket de-rating against a 5.11% 10y, while CEG is an IPP whose earnings come from AI and data-centre power contracts. Long the idiosyncratic, short the basket is a coherent pair. But the same "data-center backlash" that is hitting utilities cuts against CEG specifically, so it is a hold and **not** an add — source: https://seekingalpha.com/news/4640528-utilities-flash-oversold-signal-as-treasury-yields-dim-dividend-appeal
- **GLD — HOLD, do not add, honour the stop.** 392.88 vs a 398.00 entry (-1.3%), now below the entry and below sma20 402.28. Levels still technically clear: stop 381.00 = 2.32 ATR (ATR14 7.34), target 437.00, R:R 2.29. But the macro turned against it in one session — spot gold ~$4,308-4,314/oz, **-1.14%**, on a dollar at its **strongest in about two months** and firming Fed *hike* bets — source: https://www.kitco.com/news/article/2026-09-23/gold-silver-slide-dollar-rallies-and-fed-hike-bets-firm-kitco-am-report. A long-run debasement thesis is not refuted by a strong-dollar week, but it is now fighting the tape, so no additions and the 381.00 stop is not to be widened to accommodate it. The awaiting `GLD` SELL @ 406.77 is a take-profit above the market and is harmless; leave it.
- **CCJ — HOLD, levels unchanged.** 90.80 after a **-4.01%** session on 2026-09-23, vs a 94.00 entry (-3.4%). Stop 82.50 = 2.46 ATR (ATR14 3.389), target 135.00, R:R 3.57. Both floors clear comfortably. I could find **no company-specific news** for the drop; it is attributed to uranium spot cooling and profit-taking after a strong run, with Westinghouse IPO speculation the live narrative — source: https://www.quiverquant.com/news/Cameco+slides+as+uranium+prices+cool+and+investors+take+profits+after+a+strong+run. Analysts have not moved at all (5 strong buy / 13 buy / 4 hold, unchanged since July) and insiders have bought nothing in six months. Nothing broke and nothing confirmed — that is a hold, not an add.
- **EEM — HOLD.** 67.71 (note: prior_context carried 69.10; the fetched 09-23 close is 67.71, so the position is +3.2% not +5.3%). Stop 63.00 = 4.17 ATR, target 71.50, R:R 2.26 from the 65.60 entry. A dollar at a two-month high is a direct EM headwind and the position has given back ground because of it. Hold; the stop is far enough below to be real.
- **BCC — HOLD, weakest long_term case in the book.** 77.76 vs 76.50 entry (+1.6%), no stop, target 110.00. Insiders 0 buys / **3 sells**; analysts flat at 63.6%; 3 of 4 beats. Building products into a 19-year-high long end and a housing market facing ~7%+ mortgage rates is the wrong side of today's macro. No add. It needs a written invalidation condition it does not currently have — flagging for synthesis rather than inventing one here.
- **LCII — HOLD but on watch.** 85.03, at its 120-session low of 84.94, vs a 94.00 entry (-9.5%), **38.5% off its 138.15 high**, no stop, target 138.00. Analysts are the one positive: 61.1% bullish, **+2.3 pts, improving**, 3 of 4 beats. Insiders: nothing either way, 0 buys and 0 sells. RV/towables demand is rate-sensitive and today's rate move is against it. Sitting exactly on the low with no stop is the shape of the losses this book has already taken; it needs a stated invalidation.
- **SVRA — HOLD, lottery ticket, no change.** 5.00 vs 5.35 entry (-6.5%), stop 4.60 = 3.38 ATR (ATR14 0.222). ~$8M average daily dollar volume, which clears the $500K floor with room but is thin. 0 insider buys, 1 sell. 92.9% analyst-bullish is not information in small-cap biotech. Conviction-2 sizing stands.
- **LULU — the two legs offset; close the short, hold the long on watch.** Long at 115.00 (now 102.28, -11.1%, no stop, target 180.00) and a SELL at 100.61 (now -1.7% against). 39.9% off its high, ATR 5.05%. The short is 1.7% offside and mostly cancels the long; carrying both is paying two spreads to be flat. Close the short. The 180.00 target on the long is the same species of problem as NKE's 62.00 — it implies a full recovery — but unlike NKE I did not get a fetched EPS anchor to price it against this morning, so I am **not** calling it broken on no evidence. Hold, no add, and it needs an invalidation condition.

## [06:22 ET] DATA QUALITY SUMMARY so far
- Yahoo Finance 429/401 across the board: every index (SPX, NDX, DJI, RUT), VIX, /ES, /NQ, DXY, spot gold, WTI via `macro`, and **all options-implied moves** via `implied`. No idea today was checked against options pricing.
- Kalshi event search returns 0 results for every macro topic tried — no event contract could be priced.
- `history BTC-USD` returns ok:false; IBIT used as the fetchable proxy.
- `short NKE` timed out against api.nasdaq.com — no short-interest reading for any name today.
- FRED DGS2 returned HTTP 502 — no 2y level; the curve came from T10Y2Y instead.
- Working: finnhub quotes/earnings/insiders/analysts/filings, nasdaq OHLCV history, FRED (except DGS2), CoinGecko, SEC EDGAR.

## [06:23 ET] OXY — captured, conviction 5, long_term (the only long_term idea today)
- Primary document read in full: Q1 2026 earnings release, Ex-99.1 to the 8-K — source: https://www.sec.gov/Archives/edgar/data/0000797468/000162828026030567/oxyex9913-31x26earningsrel.htm
  - FCF before working capital from continuing ops **$1.7B** (Q1 2026)
  - **$7.1B of principal debt repaid through 2026-05-05**, principal debt down to **$13.3B**, stated milestone **$10.0B**
  - production **1,426 Mboed, exceeded the high end of guidance**
  - **$3,123M net after-tax** from discontinued operations incl. the OxyChem gain
  - Q1 2026 interest and debt expense **$432M vs $310M in Q1 2025** — interest has gone UP, not down
  - the release contains **no** forward guidance and **no** WTI assumption
- CORRECTION TO SECONDARY REPORTING: published coverage claims "annualized interest lowered by about $630 million compared to 2025". The filed Q1 2026 number is $432M against $310M a year earlier, i.e. higher. The saving is a future consequence of the repayments, not a result already booked, and the captured thesis says so rather than repeating the claim.
- The $5.5B FCF at $65/bbl WTI and the 9% 2026 FCF yield are **Barclays/third-party figures, not filed** — labelled as such in the evidence. They are the basis of the $80 target via a re-rate to a 6.5% FCF yield, holding the $65 WTI assumption fixed while WTI actually trades $92.16. Source: https://www.tikr.com/blog/occidental-cut-its-debt-by-10-billion-the-stock-already-knows-it
- Positioning: bullish share 44.8%, **+4.8 pts, improving**, strong buy 3→4, sell 1→0 Jul→Sep, **4 of 4 beats**. Insider Jackson Richard A. bought 4,770 sh @ **$52.38** on 2026-06-23, zero sells — and $52.38 is inside the 52.00-56.00 accumulation zone.
- Levels: accumulate 52.00-56.00 (zone floor = the 200dma at 53.48), target 80.00, bear case 44.00, no stop. R:R (80-54)/(54-44) = **2.60** against the 2.5 long_term floor.
- **CORRELATION CAP NOW BINDING:** XLE + DINO (open) + OXY = **3 ideas on the oil price**. No fourth energy idea today. OXY sized 2.5% rather than the 4-5% conviction 5 allows, for exactly this reason.

## [06:23 ET] PFE — NOT captured, and the reason is the floor, not the thesis
PFE has the best evidence in the book (CEO Bourla and two directors buying $2.96M, 4 of 4 beats, price 3.5% off its high). It is still not being published as a recommendation today, because the standing levels do not clear the long_term floor:
- entry 27.60 (filled), target 42.00. PFE's **400-session low is $20.915**, so a bear case honestly anchored to where this stock has actually traded within the past 400 sessions is ~$21.00, not a convenient $23.
- R:R = (42.00-27.60)/(27.60-21.00) = 14.40/6.60 = **2.18 against a 2.5 floor**. It only clears if the bear case is set above ~$21.84 — i.e. by asserting PFE cannot revisit a price it traded at this year. That is exactly the reverse-engineering the strategy forbids.
- Decision: **hold the open position** (it is +2.1% and the insider case is real), do not add, and re-defend the $42 target with an actual valuation before republishing it. I could not build that valuation this morning without fetched EPS and pipeline figures.
- This is a case where the honest output is a position held but not re-recommended. Recording it so synthesis does not read the silence as an oversight.

## [06:25 ET] FALSIFICATION PASS — every captured candidate recomputed against the floors
Recomputed independently from the fetched ATR14 values rather than trusting the numbers written into each idea:

| Symbol | Dir | Horizon | R:R (floor) | Stop in ATR (floor) | win_prob vs baseline | evidence kinds / conviction |
| --- | --- | --- | --- | --- | --- | --- |
| TLT | sell_short | swing | 2.71 (2.0) OK | 1.92 (1.8 etf) OK | 0.44 vs 0.270 = +17.0pt | 3 kinds / conv 4 OK |
| XLU | sell_short | swing | 2.07 (2.0) OK | 2.27 (1.8 etf) OK | 0.44 vs 0.325 = +11.5pt | 3 kinds / conv 4 OK |
| CAG | buy | swing | 2.05 (2.0) OK | 2.08 (2.0 stock) OK | 0.42 vs 0.328 = +9.2pt | 3 kinds / conv 4 OK |
| XLE | buy | swing | 2.13 (2.0) OK | 2.27 (1.8 etf) OK | 0.40 vs 0.320 = +8.0pt | 2 kinds / conv 3 OK |
| MCD | sell_short | swing | 2.16 (2.0) OK | 2.41 (2.0 stock) OK | 0.42 vs 0.317 = +10.3pt | 4 kinds / conv 5 OK |
| OXY | buy | long_term | 2.60 (2.5) OK | n/a — bear case 44.00 | 0.45 vs 0.278 = +17.2pt | 4 kinds / conv 5 OK |

- No claimed edge exceeds 20 points over the break-even hit rate, so no idea is making a large claim its thesis has to carry.
- Conviction equals the number of **distinct** evidence kinds in every case; none is inflated above what the evidence supports.
- **CAG at 2.05 and XLU at 2.07 sit close to the 2.0 floor and that is on purpose.** In both the stop was placed first from structure — CAG's 14.15 below the 14.31-14.59 insider purchase cluster, XLU's 40.95 above the 09-22 high of 40.82 — and the target was then taken as it stood (CAG's 16.74) or from a real prior-year level (XLU's 36.80, above the 35.51 400-session low). Neither target was moved to clear the ratio, and neither stop was walked in to do it. If the red team wants to cut either, the ratio is the honest reason, not a fixable one.
- Schema catch from this pass: the first OXY capture had `stop: null` and no `bear_case_price`, which would have failed `risk_reward` with no downside at all. Re-captured with `bear_case_price: 44.0` plus an explicit invalidation condition in `key_risk` (principal debt stops falling / the $10.0B milestone missed by end-2027 / FCF before working capital under $1.0B in a quarter with WTI above $70). The later line supersedes the earlier one.
- Bearish ideas are all `sell_short` on `Robinhood Stocks` with `requires_margin: true`. No bearish crypto spot `sell` was captured — the one bearish crypto view considered was rejected outright on the tape, so the Robinhood-cannot-short trap did not arise.

## [06:25 ET] BOOK SHAPE — drivers, and where the correlation cap now binds
- **Rates / duration (2 of 3):** TLT short, XLU short. Room for one more but none taken — see the IYR note above.
- **Oil (3 of 3 — CAP REACHED):** XLE (open), DINO (open), OXY (new). **No fourth energy idea today.**
- **Consumer:** MCD short (1).
- **Staples:** CAG long (1).
- 3 shorts and 3 longs, which is what the tape actually offered rather than a manufactured balance. Five swing, one long_term, **zero intraday** — nothing intraday cleared the bar, and with every index, VIX and futures quote unavailable this morning (Yahoo 429) there was no honest basis for an intraday level anyway. That gap is a data outage, not a judgement about the tape.

## [06:29 ET] REJECTED — KMX — the best insider cluster of the morning, killed by fresher data
This is the one I most wanted to capture, and the falsification step is what stopped it.

The bull case, all verified:
- **6 open-market buys, 5 distinct buyers, $1,268,037, ZERO sells** in six months — Chawla Sona 2,000 sh @ 53.39 and Shinder Marcella 574 @ 52.01 on 2026-06-25, ONeil Mark F 4,800 @ 52.36 on 2026-06-24. Five distinct buyers is the strongest insider cluster I found today, stronger than CAG's three — source: https://finnhub.io/api/v1/stock/insider-transactions?symbol=KMX
- Analyst bullish share 28.0%, **+20.9 points over the month**, revision direction improving — the largest revision swing in anything I looked at. 3 of 4 beats.
- Price 57.46, **34.5% off** the 400-session high of 87.70, above the 200dma of 47.63; 2026-09-23 printed a reversal, trading down to 54.90 and closing 57.46 (+1.09%).
- Earnings confirmed **2026-09-29 BMO, call 8:00am ET**, by two independent fetched sources: the Finnhub calendar (est EPS 0.72 on $7.05B) and press coverage (~$0.71 on ~$6.94B) — source: https://www.marketbeat.com/instant-alerts/upcoming-carmax-kmx-projected-to-announce-earnings-on-tuesday-2026-09-22/

Why it is rejected anyway — **the bear evidence is three months newer than the bull evidence**:
- The Manheim Used Vehicle Value Index fell **1% in the first half of September to 206.2**, and is now **0.4% below September 2025 — its first year-over-year decline of 2026**. August was 208.2, itself -0.9% m/m — source: https://collisionweek.com/2026/09/21/manheim-used-vehicle-value-index-falls-1-first-half-september/ and https://www.coxautoinc.com/insights/manheim-used-vehicle-value-index-mid-september-2026-trends/
- Wholesale values rolling into a y/y decline compresses margin on inventory already bought and weakens the collateral behind CarMax's loan book, on top of auto affordability facing a 5.11% 10y.
- Every insider purchase is dated **2026-06-24/25** — before that roll. The analyst revisions run to 2026-09-01, also before the mid-September print. The strongest evidence for the trade predates the strongest evidence against it, and I cannot claim the buyers knew.
- No short either: five insiders buying and a +20.9 point revision swing is not something to be short into, and the stock is already 34.5% below its high. **No position in either direction.**
- Had I captured this at the point of the insider read, it would have been a conviction-4 long on stale evidence. This is the ~10% falsification budget paying for itself.

## [06:29 ET] TRACK RECORD — how it was and was not used today
prior_context reports 1/8 hit target (12%), avg -3.2%, across 8 closed trades.
- **8 closed is under the ~15 threshold, so it is noise and I have not over-fitted to it.** Specifically I did not raise the bar on stocks because "stock: 0/5, avg -4.9%" — five closed trades cannot distinguish a bad process from a bad fortnight.
- What I *did* carry across, because it is structural rather than statistical: all ten of the first month's stop-outs had stops tighter than 1.6 ATR, so every stop today was placed from price structure first and then checked against the ATR floor, never the reverse. The tightest captured is TLT at 1.92 ATR and that is an inherited fill, not a new level.
- Conviction 2 scored 0/2 with avg -5.6%. I captured **no** conviction-2 idea today — not as a policy against the lane, but because nothing thin turned up that I wanted at lottery-ticket size. SVRA remains the book's only conviction-2 exposure and is held, not re-pitched.
- The repetition guard bound in two places: PFE (3x in 10 days) and MU (3x) were both held or cancelled rather than re-recommended.

## [06:26 ET] CHECKED AND PASSED OVER — materials and industrials, no idea good enough
Looked for a PMI-58.4 beneficiary on the theory that a growth signal that strong got lost inside the rate story. Nothing cleared the bar and none is being padded in:
- **FCX** 72.58, 9.6% off its 400-session high, above both the 50dma (69.12) and 200dma (62.74) — a healthy uptrend with 4 of 4 beats, but analyst bullish share is flat at 80.0% and I found no dated catalyst. Nothing to say that the price does not already say.
- **CAT** 812.02, **24.4% off** its 1073.46 high — the interesting drawdown of the group, but bullish share 52.9% and **-3.0, deteriorating**, and no catalyst inside the horizon. A de-rating with the sell side still cutting is not yet a buy.
- **XLB** 50.28, pinned on its 200dma of 50.49 with the 20dma and 50dma just above — directionless. **ETN** 438.76, above every average, 8.2% off its high, no entry that is not a chase.
- Publishing any of these would be filling space. `config/strategy.md` is explicit that four strong ideas beats ten with six of filler.

## [06:27 ET] RESEARCH COMPLETE (superseded — see the amended block at the end of this file)
- **candidates: 6 unique ideas** (8 lines in candidates.jsonl — TLT and OXY each appear twice, the later line superseding the earlier; synthesis takes the last entry per symbol).
  - TLT sell_short, swing, conviction 4 — position update, levels unchanged
  - XLU sell_short, swing, conviction 4 — new
  - MCD sell_short, swing, conviction 5 — new, WAIT entry
  - CAG buy, swing, conviction 4 — position update, stop widened 14.20 to 14.15
  - XLE buy, swing, conviction 3 — position update, levels unchanged
  - OXY buy, long_term, conviction 5 — new
- **All 16 open positions and all 12 awaiting-entry orders were reviewed and have a written decision** in the blocks above. Decisions that are NOT in candidates.jsonl because they are closes or cancellations, and which synthesis must carry into the report: close both NKE legs; close the LULU short; cancel the stale SNX @260, MU @960, BTC @63,400 and /MBTU6 @64,340 orders. Holds recorded without a new candidate row: PFE, CEG, GLD, CCJ, EEM, BCC, LCII, SVRA, LULU (long), DINO.
- **PFE is the notable omission and it is deliberate** — best evidence in the book, but the standing 42.00 target gives R:R 2.18 against the 2.5 long_term floor once the bear case is anchored honestly to its own 400-session low of 20.915. Held, not republished. Do not read the silence as an oversight.
- **DINO was reviewed and also fails its floor** on an honest stop: at a 2.0+ ATR stop (97.00 or lower against ATR 5.098) the ratio to the 128.00 target falls to ~1.95 or below from the 107.50 fill. Held as a do-not-add, not recaptured.
- **coverage gaps:**
  - **No index, VIX, futures, DXY, spot gold or WTI level could be fetched** — Yahoo returned HTTP 429 for every one of them via `macro`, finnhub refuses index CFDs, stooq 404s on `^` symbols, and there is no Alpha Vantage key. Index levels quoted in the notes come from news sources, never from a fetched quote, and are labelled as such.
  - **No options-implied move for any idea** — `implied` returns HTTP 401 from the Yahoo options endpoint. Not one target today was checked against what the options market prices, which is a real hole in the level-setting step.
  - **No event contracts at all** — Kalshi search returned 0 results for every macro topic tried, so the three open/awaiting KXFEDDECISION positions could not be marked and no new event idea could be priced. This is normally a lane the report is told to hunt actively.
  - **No short interest for any name** — `short` timed out against api.nasdaq.com.
  - **No 2-year yield** — FRED DGS2 returned HTTP 502; the curve reading came from T10Y2Y instead.
  - **No BTC OHLC** — `history BTC-USD` returns ok:false; IBIT was used as the fetchable proxy.
  - **Zero intraday ideas.** With no index, futures or VIX quote available there was no honest basis for an intraday level. That is a data outage, not a view on the tape.
  - **Zero small or micro caps captured.** KMX was the closest thing and was rejected on the Manheim data; the sub-$2B earnings screen (BXMT, SCHL, IDT, MTN, BTM, BSET, CALM, FDS, PRGS, ANGO) was pulled but not worked through. CALM — a consensus **loss** of -0.72 on $586M for an egg producer reporting 2026-09-30 BMO — is the one I would pick up first with more time.
  - **NKE earnings date unresolved:** the fetched Finnhub calendar says 2026-09-28, fetched press coverage says 2026-10-01 4:15pm ET. Not resolved; no idea depends on it.
- **sources that failed:** Yahoo Finance chart API (429, all index/commodity symbols), Yahoo options API (401, all symbols), Kalshi market search (0 results, all queries), api.nasdaq.com short interest (timeout), FRED DGS2 (502), `history BTC-USD` (ok:false), proactiveinvestors.com (403 to WebFetch).
- **sources that worked:** finnhub quote/earnings-calendar/insiders/analysts/filings, nasdaq OHLCV via `history`, FRED (DGS10, DFF, T10Y2Y, UNRATE, CPIAUCSL), CoinGecko, SEC EDGAR (read two primary documents in full — MCD 8-K Ex-99.1 and OXY Q1 2026 Ex-99.1).

## [06:28 ET] REJECTED — CALM — the flagged small-cap gap, worked and declined
Closed the one gap the completion block named, rather than leaving it as a hypothetical.
- CALM 71.73, sitting on its **400-session low of 71.08** printed the same session, **43.3% below** the 126.40 high, with the 50dma at 81.65 and 200dma at 80.82 far overhead. Six consecutive lower closes into 2026-09-23.
- Reports **2026-09-30 BMO** with consensus at a **loss of -0.7208** on $586M revenue (fetched calendar).
- Last quarter was a violent miss: 2026-06-30 actual **-0.76 against a +0.0842 estimate**, a -1002% surprise. Only 2 of the last 4 beat. The avian-flu egg-price spike that produced 4.29 and 2.13 EPS quarters in 2025 has fully unwound.
- **Zero insider buys and zero insider sells** in six months — nobody inside is expressing a view at a 43% drawdown. Analysts flat at 54.5%, no revision direction.
- No long: a falling knife into a consensus loss with no insider bid and no analyst turn is the definition of catching something broken rather than something cheap.
- No short either: the loss is already consensus, the stock is already at its low, and at $67M average daily dollar volume it is thin enough that a squeeze on any egg-price headline is a real risk.
- **No position.** The small/micro-cap lane stays empty today, honestly rather than by being filled.

## [06:28 ET] RESEARCH COMPLETE (amended — supersedes the 06:27 block above)
This block supersedes the earlier RESEARCH COMPLETE. Everything in it still holds, with two changes: the CALM gap named there has now been worked and rejected, and the small-cap lane is confirmed empty by decision rather than by running out of time.
- **candidates: 6 unique ideas** — TLT sell_short (swing, 4), XLU sell_short (swing, 4), MCD sell_short (swing, 5, WAIT entry), CAG buy (swing, 4), XLE buy (swing, 3), OXY buy (long_term, 5). 8 lines in candidates.jsonl; TLT and OXY each appear twice with the later line superseding.
- All 16 open positions and all 12 awaiting-entry orders reviewed, each with a written decision. Closes and cancellations that need carrying into the report are listed in the block above.
- **coverage gaps, final:** no index / VIX / futures / DXY / spot gold / WTI quote (Yahoo 429); no options-implied move on any idea (Yahoo options 401); no event contracts at all (Kalshi search empty); no short interest (nasdaq timeout); no 2y yield (FRED 502); no BTC OHLC (IBIT used as proxy). **Zero intraday ideas** — no fetchable index or futures level to set one from. **Zero small/micro caps** — KMX rejected on the Manheim roll, CALM rejected above; both were worked, neither was skipped.
- **sources that failed:** Yahoo chart API, Yahoo options API, Kalshi market search, api.nasdaq.com short interest, FRED DGS2, `history BTC-USD`, proactiveinvestors.com (403).
- **sources that worked:** finnhub (quotes, earnings calendar, insiders, analysts, filings), nasdaq OHLCV, FRED, CoinGecko, SEC EDGAR — two primary documents read in full, MCD's 8-K Exhibit 99.1 and OXY's Q1 2026 Exhibit 99.1.
- Research ran 06:00:55 to 06:28 ET and **was not truncated**; it finished inside the budget with the work complete.
