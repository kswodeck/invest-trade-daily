# Research log — 2026-08-14

## [07:52 ET] MACRO — rates & policy (FRED, live)
- US 10y yield 4.68% (2026-08-12), prev 4.70% — source: https://fred.stlouisfed.org/series/DGS10
- US 2y yield 4.20% (2026-08-12), prev 4.22% — source: https://fred.stlouisfed.org/series/DGS2
- Fed funds effective 3.63% (2026-08-12), flat — source: https://fred.stlouisfed.org/series/DFF
- 10y-2y curve +0.48 (2026-08-13), flat vs prev — positively sloped, no inversion stress
- Unemployment 4.1% (Jul 2026), down from 4.2% (Jun) — source: https://fred.stlouisfed.org/series/UNRATE
- CPI index 332.813 (Jul 2026) vs 332.568 (Jun) = +0.074% m/m headline NSA index change
- TLT 82.59 +0.58% (2026-08-13 close, finnhub)
- NOTE: 10y at 4.68% with fed funds 3.63% = ~105bp positive term spread; long end is not pricing rapid cuts.

## [07:52 ET] DATA GAP
- Yahoo Finance returning HTTP 429 (rate limited) for ALL index/futures symbols: ^GSPC ^NDX ^DJI ^RUT ^VIX ES=F NQ=F DX-Y.NYB ^TNX GC=F CL=F
- Finnhub rejects index/CFD symbols ("Market data subscription required for CFD indices")
- Stooq 404s on ^-prefixed index symbols
- CoinGecko crypto block failed in macro call
- Consequence: no live index/VIX/futures level. Will proxy with ETFs (SPY/QQQ/IWM/GLD/USO/UUP) via finnhub.

## [07:55 ET] MACRO — tape (2026-08-13 close, finnhub, delayed/EOD)
- SPY 777.88 +0.70% | QQQ 732.07 +1.16% | IWM 303.50 +0.26% | DIA 537.91 +0.14%
- Leadership = large-cap tech. XLK 190.77 +1.01%, SMH 589.12 +0.73%. Breadth narrow: IWM/DIA lagged badly.
- Defensives also bid: XLP 86.00 +1.08%, XLU 44.04 +0.46% — unusual to see staples lead alongside tech; suggests rotation OUT of cyclicals.
- Commodities sold: GLD 398.96 -1.47%, SLV 58.16 -1.52%, USO 125.03 -1.78%. XLE 61.06 +0.05% flat despite crude down.
- Credit fine: HYG 79.79 +0.23%. TLT +0.58%. UUP 28.18 -0.07% (dollar flat/soft).
- Regime read: risk-on but narrow (tech + staples up, small caps flat, commodities down). Yields easing slightly. No stress signal in credit or vol proxies I could fetch.
- source: finnhub quote endpoint via scripts/market_data.py

## [07:57 ET] CALENDAR — dated earnings catalysts inside 10 sessions (finnhub earnings calendar)
- 2026-08-18 bmo: HD (rev est 48.7B, eps 4.88), BIDU, TOL(amc), KEYS(amc)
- 2026-08-19 bmo: LOW (26.5B), TGT (26.3B), TJX (15.3B), ROST, ADI (4.0B, semis), EL
- 2026-08-20 bmo: WMT (188.8B, eps 0.75), BABA (274.3B RMB, eps 10.62), DE (11.1B), NTES
- 2026-08-21: BJ
- 2026-08-24: PDD (117.5B RMB), XPEV, DKS
- 2026-08-25 amc: INTU (4.4B); KSS, WSM
- 2026-08-26 amc: **NVDA (rev est 93.6B, eps 2.13)**, CRM (11.4B), HPQ (14.4B); SNPS
- 2026-08-27: MRVL (2.8B), WDAY(amc), ADSK, ULTA, DG (11.5B), BBY (9.6B), GOLD(amc)
- Structure of the week: Aug 18-21 is a pure US CONSUMER/RETAIL week (HD, LOW, TGT, TJX, ROST, WMT, BJ). Aug 25-27 is the TECH/SEMI week capped by NVDA on 8/26 AMC.
- Implication: two distinct, uncorrelated catalyst clusters to build ideas around, satisfying the correlation cap.
- source: https://finnhub.io/api/v1/calendar/earnings (via scripts/market_data.py earnings --days 14)

## [07:59 ET] MACRO — regime + this week's tape
- S&P 500 closed at a RECORD Thursday 2026-08-13, clearing 7,800 for the first time. SPY 777.88 confirms.
- Driver: softer-than-expected inflation data eased concerns about another Fed RATE HIKE. Note the direction — the 2026 market fear is HIKES, not cuts. Fed funds 3.63%, 10y 4.68%.
- Friday 8/14 premarket: S&P futures little changed, Dow futures +0.1%, Nasdaq-100 futures slightly below flat. Asia positive (KOSPI +1.4%, Nikkei +0.8%).
- source: https://finance.yahoo.com/markets/live/stock-market-today-friday-august-14-dow-sp-500-nasdaq-102635519.html
- source: https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-14-2026

## [07:59 ET] CALENDAR — Jackson Hole 2026-08-27 to 2026-08-29
- Kansas City Fed symposium, Jackson Lake Lodge. Topic: "Financial Innovation: Implications for Payments and Policy."
- Fed Chair **Kevin Warsh** delivers keynote Friday morning 2026-08-28.
- This is a first-order macro catalyst 10 sessions out and it lands the day AFTER NVDA earnings (8/26 amc). Vol event risk clusters 8/26-8/28.
- source: https://www.kansascityfed.org/research/jackson-hole-economic-symposium/

## [07:59 ET] LEAD — RDDT S&P 500 inclusion
- Reddit (RDDT) reported +12.4% premarket 8/14 on news it is joining the S&P 500. Index-inclusion catalyst with a dated rebalance effective date. Needs verification of effective date + whether the move already ran.
- source: https://finance.yahoo.com/markets/live/stock-market-today-friday-august-14-dow-sp-500-nasdaq-102635519.html

## [08:01 ET] CATALYST — S&P 500 index change, effective before open TUE 2026-08-18
- RDDT (Reddit, NYSE) REPLACES AVB (AvalonBay Communities, NYSE) in the S&P 500, effective prior to the open Tue 2026-08-18.
- Announced by S&P DJI after close 2026-08-13. RDDT +11% after-hours, +12% premarket 8/14.
- AVB is being REMOVED because it agreed to be acquired by Equity Residential (EQR) — that deal created the vacancy.
- Mechanical flows: passive S&P trackers must BUY RDDT and SELL AVB at/into the 8/18 open. Both are dated, non-discretionary flows.
- Caveat flagged in coverage: Google AI traffic concerns are an active bear case on RDDT.
- sources: https://www.spglobal.com/spdji/en/documents/indexnews/announcements/20260813-1484396/1484396_avb54wbs.pdf , https://www.prnewswire.com/news-releases/reddit-set-to-join-sp-500-and-sun-communities-to-join-sp-midcap-400-302851432.html , https://www.benzinga.com/trading-ideas/movers/26/08/61198738/reddit-stock-pops-on-long-awaited-sp-500-inclusion

## [08:07 ET] DATA GAP — resolved with a fallback
- `market_data.py history` is DEAD for all symbols today: yahoo returns 429 (both query1 and query2 hosts), stooq now sits behind a JavaScript proof-of-work challenge, finnhub /stock/candle returns "You don't have access to this resource" on this key, alphavantage has no key.
- Workaround used for ALL levels below: stockanalysis.com daily OHLCV JSON (https://stockanalysis.com/api/symbol/s/<SYM>/history?range=6M&period=Daily), with SMA/ATR computed locally in /tmp/levels.py. Cross-checked against nasdaq.com historical API and finnhub quote for 2026-08-13 close on NVDA — all three agree (225.30). Treat levels as reliable.
- Delayed/EOD only: every level below is as of the 2026-08-13 close. No live intraday prices available this run.

## [08:08 ET] LEVELS (2026-08-13 close; stockanalysis.com OHLCV, SMA/ATR computed locally)
- NVDA 225.30 | sma20 209.28 sma50 206.31 | atr14 7.58 (3.4%) | 6m 164.27-236.54 | -4.8% off 6m hi | +8.6% 20d
- RDDT 158.12 | sma20 166.00 sma50 174.85 sma100 163.45 | atr14 11.47 (7.3%) | 6m 119.27-208.05 | -24.0% off 6m hi | -14.7% 20d
- AVB 183.91 | sma20 188.03 sma50 188.02 | atr14 3.77 (2.1%) | 6m 160.09-198.63 | -7.4% off hi
- EQR 65.97 | sma20 67.32 sma50 67.51 | atr14 1.38 (2.1%) | 6m 57.57-71.50 | -7.7% off hi
- WMT 115.72 | sma20 112.08 sma50 114.52 sma100 120.35 | atr14 2.65 (2.3%) | 6m 106.79-135.16 | -14.4% off hi | +0.7% 20d
- TGT 155.51 | sma20 145.10 sma50 137.11 | atr14 4.07 (2.6%) | 6m 111.11-156.47 | -0.6% off 6m hi | +10.9% 20d  <-- extended into 8/19 print
- HD 341.70 | sma20 340.69 sma50 337.18 | atr14 8.75 (2.6%) | 6m 289.10-394.35 | -13.4% off hi | -1.8% 20d
- LOW 218.22 | sma20 213.02 sma50 215.20 sma100 223.53 | atr14 5.76 (2.6%) | 6m 199.40-289.87 | -24.7% off hi
- Read: US consumer/retail complex (WMT -14%, HD -13%, LOW -25% off 6m highs) is broadly de-rated going INTO its earnings week, while TGT alone has ripped +10.9% in 20d to a 6m high. That divergence is the tradeable asymmetry of next week.

## [07:55 ET] TIMESTAMP CORRECTION
- Entries above were labelled 07:52-08:08 by estimate; true wall clock at this point is 07:55 ET. Research started 07:51 ET. All subsequent timestamps are read from the system clock. Price data as-of stamps are unaffected and correct.

## [07:55 ET] CATALYST — EQR/AVB merger closes MON 2026-08-17
- All-stock merger, $69B enterprise value. Exchange ratio **2.793 EQR shares per AVB share**.
- Both shareholder bases approved 2026-08-12; merger expected to CLOSE 2026-08-17 (Monday).
- AVB holders will own ~51.2% of the combined company. $175M gross synergies targeted within 18 months of close.
- Arithmetic on 8/13 closes: deal value of AVB = 2.793 x 65.97 = **184.25**; AVB traded 183.91. Gross spread $0.34 = **0.18%** with ~1 trading day to close.
- sources: https://www.cnbc.com/2026/05/21/equity-residential-eqr-and-avalonbay-avb-to-merge.html , https://www.stocktitan.net/sec-filings/EQR/s-4-equity-residential-business-combination-registration-cfa05948eab6.html , https://seekingalpha.com/news/4631896-equity-residential-avalonbay-shareholders-approve-merger

## [07:55 ET] REJECTED — AVB merger-arb long AVB / short EQR — 0.18% gross spread is below transaction cost; requires margin short of EQR; R:R unquantifiable on a 1-day deal-break tail. Correctly priced, no edge.

## [07:55 ET] NEWS — RDDT fundamentals vs. the de-rate
- Q2 2026 (reported 2026-07-30): EPS $1.25 vs $0.96 est; revenue $805M, **+61% y/y** — eighth straight quarter of 60%+ growth. Q3 guide $860-870M vs $828M consensus (guided ABOVE).
- Global DAU 130.3M +18% y/y; US DAU 53.2M +6% y/y — both ahead of estimates.
- Yet the stock fell 7-10% on the print and is -24% off its 6m high. The bear case is entirely structural, not financial: CEO Steve Huffman called Google search referrals "choppy"; Google's AI summaries cut referral traffic to publishers; the $60M Google data-licensing deal expires 2027 and renewal terms are contested (WSJ, 2026-07-22, reported Reddit weighing restricting Google's access to its content for AI training).
- So: accelerating financials, collapsing multiple, and now a forced-buyer event on 8/18.
- sources: https://www.cnbc.com/2026/07/30/reddit-rddt-q2-2026-earnings-report.html , https://www.techtimes.com/articles/322357/20260730/reddit-revenue-soars-past-estimates-flags-google-search-traffic-choppy.htm , https://www.fxleaders.com/news/2026/07/23/rddt-stock-drops-8-as-google-ai-data-deal-uncertainty-overshadows-reddits-q2-earnings-outlook/

## [07:55 ET] MACRO — crypto is in a deep bear market while equities print records (coingecko, live)
- BTC $62,840 (-0.9% 24h), mkt cap $1.261T, 24h vol $20.2B
- ETH $1,878.31 (+0.07% 24h), mkt cap $226.7B
- SOL $75.47 (-0.13% 24h), mkt cap $43.97B
- DOGE $0.069426 (-0.79% 24h), mkt cap $10.8B
- This is the single most important divergence on the board today: S&P 500 at an all-time record above 7,800 on 8/13 while BTC sits at $62.8k. Whatever "risk-on" means in this tape, it is NOT flowing to crypto. Any equity idea premised on generalized risk appetite has to survive this.
- Volatility is low in coin terms right now (all four majors within +/-1% on 24h) — a compressed tape, not a capitulating one.
- source: https://www.coingecko.com/ (via scripts/market_data.py crypto)

## [07:56 ET] MACRO — the 2026 backdrop, and a SAME-DAY catalyst
- BTC peaked $126,198 in Oct 2025; now ~$62.8k = roughly **-50% from the record**. This is a genuine crypto bear market, not a dip.
- Drivers per CoinDesk Research: US spot BTC ETF redemptions — **eight consecutive weeks with >$8B of outflows**; -$144.6M on 2026-08-10 alone. Plus corporate selling: MicroStrategy (MSTR) SOLD 1,690 BTC (~$108.6M). The largest structural buyer of the last cycle has flipped to seller.
- Macro overlay: US-Iran fighting intensified from late Feb 2026, with repeated attacks on shipping around the **Strait of Hormuz**. Oil spikes revived inflation fears and pushed central banks toward tighter-for-longer. THIS is why the 2026 fear is a rate HIKE, not a cut, and why 10y sits at 4.68% over a 3.63% funds rate.
- **>>> SEC votes on its "Regulation Crypto" framework TODAY, 2026-08-14 <<<** — follows delays to the Senate's Clarity Act. Outcome could move institutional crypto appetite hard in either direction. NEEDS VERIFICATION of exact time and agenda.
- sources: https://www.investing.com/analysis/bitcoin-falls-as-record-etf-outflows-and-strategy-sale-hit-sentiment-200681446 , https://www.interactivecrypto.com/bitcoin-holds-steady-near-63-400-amid-etf-outflows-and-macro-uncertainty-aug-2026 , https://www.tradingkey.com/analysis/cryptocurrencies/btc/261945885-crypto-bitcoin-btc-price-crashing-usd-strategy-fed-tradingkey

## [07:56 ET] CATALYST — VERIFIED — SEC open meeting TODAY 2026-08-14 10:00 ET
- One item on the agenda: whether to **propose** new rules creating a tailored offering regime for certain investment contracts involving crypto assets ("Regulation Crypto"). Public meeting at SEC HQ, webcast.
- First formal crypto rulemaking of Chairman **Paul Atkins**' tenure. Notice landed Monday night 2026-08-10 with unusually short lead time. The proposal runs ~400 pages.
- **Critical nuance:** today's vote only decides whether to PUBLISH the proposal for public comment. Final adoption comes later, expected effective date **2027**. Nothing becomes law today.
- Why it exists: the Senate failed a cloture vote on the Digital Asset Market Clarity Act before summer recess; consideration deferred to **2026-09-15**. The SEC is routing around dead legislation.
- Base rate: a proposal vote, on the chair's own signature initiative, noticed by that chair — passage is close to a formality. The uncertainty is in the 400 pages of content, not the vote.
- sources: https://www.coindesk.com/policy/2026/08/11/u-s-sec-sets-meeting-to-propose-reg-crypto-to-support-certain-digital-assets-offerings , https://www.tftc.io/sec-reg-crypto-august-14-open-meeting-proposed-rule , https://crypto.news/sec-sets-aug-14-meeting-on-crypto-offering-rules/

## [07:56 ET] CATALYST — Senate Digital Asset Market Clarity Act, cloture deferred to 2026-09-15
- Outside the 10-session horizon but frames the crypto regulatory tape into September.
- source: https://crypto.news/clarity-act-dying-sec-regulation-crypto-replacement/

## [07:57 ET] DATA NOTE — Kalshi puller in market_data.py is broken; worked around
- `market_data.py events` fetches only the first 200 open markets unfiltered and then greps client-side, so it returns junk (a tennis market for query "Fed") and zero results for "Bitcoin"/"CPI". It also reads `yes_bid`/`last_price`, which Kalshi has RENAMED to `yes_bid_dollars`/`last_price_dollars` (values in dollars, not cents) — so every price came back null.
- Worked around with a direct series-ticker query (/trade-api/v2/markets?series_ticker=...) reading the *_dollars fields. All event-contract prices below are live from that, fetched this morning.
- Flagging for the maintainer: this is a real bug, not a transient outage.

## [07:57 ET] EVENT MARKET — Fed path (Kalshi, live 2026-08-14 AM, cents = implied prob)
- Current fed funds target upper bound = 3.75% (implied: KXFED-26SEP-T3.50 "above 3.50%" trades 98/100c).
- **Sep 16, 2026 meeting** — KXFED-26SEP-T3.75 "above 3.75%" (= a 25bp HIKE): yes **23/27c**, last 29c, **prev 35c**, OI 156,436. Above 4.00%: 0/1c (OI 57,876) — no chance of 50bp.
  -> Market: ~25% hike, ~2% cut, ~73% hold at Sept. The hike probability fell 35c -> 29c on this week's soft CPI.
- **Dec 9, 2026 meeting** — above 3.75%: **54/55c** (OI 18,746); above 4.00%: 23/27c (OI 8,237); above 3.50%: 80/81c, prev 84c (OI 13,842).
  -> Market: ~54% at least one hike by December, ~20% a cut by December (up from 16% pre-CPI), ~26% unchanged.
- Read: an unusually WIDE two-sided distribution by year end. The market genuinely does not know whether the next move is a hike or a cut. That is the macro fact of this tape.
- Liquidity is real (Sep T3.75 OI >156k contracts), so this is tradeable size, not a screen artifact.
- source: https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXFED

## [07:58 ET] MACRO — Warsh Fed: hawkish chair, evenly split committee
- Fed left rates UNCHANGED at the 2026-07-29 meeting (upper bound 3.75%). Warsh's second press conference.
- Warsh's prepared remarks were hawkish: inflation target is a strict 2%; asked about inflation rising again in recent months he said **"No tolerance."**
- CNBC's read (2026-07-31): "Markets heard a dovish Kevin Warsh. The Fed chairman's own words suggest a rate hike." Press conference was widely described as muddled — a perceived hawk appearing to talk DOWN inflation worries, with vague answers.
- Committee is now **evenly split** between members expecting hikes later this year and members expecting further cuts. That is the source of the wide Kalshi distribution.
- Therefore Warsh's Jackson Hole keynote (Fri 2026-08-28 AM) is the highest-leverage scheduled macro event in the horizon: a hawkish chair, a split committee, and a market that just rallied to records on one soft CPI print.
- sources: https://www.cnbc.com/2026/07/31/kevin-warsh-fed-inflation-rate-hike-markets.html , https://www.cnbc.com/2026/07/29/fed-meeting-today-live-updates.html , https://www.pbs.org/newshour/economy/federal-reserve-chair-warsh-emphasizes-political-independence-signals-focus-on-inflation

## [07:58 ET] MACRO — July CPI (rel. 2026-08-12 08:30 ET) was IN LINE, not soft. Correcting earlier note.
- Headline CPI +0.1% m/m SA (consensus +0.1%); **3.4% y/y**, down 0.1pp from June.
- Core CPI +0.2% m/m; **2.5% y/y**, down 0.1pp from June. Matched forecast.
- Every reading matched the Dow Jones consensus. The Yahoo live blog's "softer-than-expected inflation" framing is loose; BLS numbers are the authority here. NBC's headline was "Inflation remained stubborn."
- **The structural detail that matters:** headline 3.4% vs core 2.5% = a ~90bp wedge driven by food and energy. That is the Strait of Hormuz oil premium showing up in the CPI. Core is close to target; headline is not.
- This is why September hike odds fell (23/27c) despite Warsh's "no tolerance": the committee can argue the overshoot is an energy shock to look through. If oil rolls over, the hike case dies. If Hormuz re-escalates, it revives fast.
- Kiplinger framing confirms: "July CPI Report Lowers September Rate-Hike Odds."
- sources: https://www.bls.gov/news.release/archives/cpi_08122026.htm , https://www.cnbc.com/2026/08/12/cpi-inflation-report-july-2026.html , https://www.nbcnews.com/business/economy/cpi-inflation-july-2026-rcna591698 , https://www.kiplinger.com/investing/economy/cpi-report-july-2026-what-to-expect
- **Consequence for trade construction: oil is the hinge variable of this entire tape.** It drives headline CPI -> Fed path -> the record-high equity market. Any macro idea should be built on that chain.

## [07:59 ET] LEVELS — macro proxies & crypto equities (2026-08-13 close)
- SPY 777.88 | sma20 754.54 sma50 748.48 | atr14 8.48 (**1.09%** — very compressed) | 6m 629.28-779.37 | AT the 6m high
- QQQ 732.07 | sma20 702.34 sma50 713.21 | atr14 13.76 (1.88%) | 6m 555.60-748.65 | -2.2% off hi
- IWM 303.50 | sma20 296.16 sma50 294.75 | atr14 3.93 (1.29%) | 6m 238.69-305.05 | **-0.5% off 6m hi**
- USO 125.03 | sma20 125.64 sma50 120.64 | atr14 5.60 (**4.48%**) | 6m 75.18-154.08 | -18.9% off hi | **+5.2% 5d, +4.8% 20d**
- XLE 61.06 | sma20 58.94 sma50 56.90 | atr14 1.41 | 6m 52.62-63.46 | -3.8% off hi | +7.1% 20d
- GLD 398.96 | sma20 381.41 sma50 381.43 sma100 403.12 | 6m 363.32-492.15 | **-18.9% off hi** | +9.3% 20d
- SLV 58.16 | sma20 54.33 sma50 55.90 sma100 62.32 | 6m 49.61-85.27 | **-31.8% off hi** | +15.4% 20d
- COIN 153.90 | sma20 156.53 sma50 158.25 | atr14 8.89 (5.8%) | 6m 139.11-222.35 | -30.8% off hi | **+5.8% 5d**
- HOOD 99.37 | sma20 95.09 sma50 98.84 | atr14 4.94 (5.0%) | 6m 63.52-120.05 | -17.2% off hi | **+9.6% 5d**
- MSTR 97.10 | sma20 96.61 sma50 102.12 sma100 129.07 | 6m 81.81-197.00 | **-50.7% off hi**

## [07:59 ET] CORRECTION to my earlier breadth read
- I called breadth "narrow" off one day's sector moves. The 6-month levels say otherwise: **IWM is 0.5% from its own 6-month high** and SPY is at its high. Breadth is broad, not narrow. What 8/13 showed was one day of tech-plus-staples leadership, not a regime.
- The more interesting fact: **SPY ATR14 is 1.09%** — vol is heavily compressed at an all-time high, into a calendar with NVDA (8/26) and Jackson Hole (8/27-29) stacked back to back. Compressed vol into a dense catalyst cluster is the setup, whichever way it breaks.

## [07:59 ET] MACRO — oil is NOT rolling over; it is re-accelerating
- USO +5.2% over 5 sessions and +4.8% over 20, sitting just under sma20 125.64 and well above sma50 120.64, after a 6-month round trip of 75.18 -> 154.08 -> 125.03. ATR 4.48%/day.
- XLE +7.1% in 20 days, 3.8% from a 6-month high, above every moving average. Energy equities are confirming the crude move, and did NOT follow crude's -1.8% down day on 8/13 (XLE +0.05%). That non-confirmation is bullish for energy.
- Ties directly to the CPI wedge: headline 3.4% vs core 2.5%. Re-accelerating oil pushes headline back up, which is the one thing that revives the September hike trade currently priced at 23/27c.

## [07:59 ET] LEAD — crypto equities have front-run today's SEC vote
- COIN +5.8% and HOOD +9.6% over the last 5 sessions into a 10:00 ET vote that has been publicly noticed since Monday night. MSTR only +0.3% over 5d (it is the BTC-beta name and BTC has not moved).
- The divergence is the tell: COIN/HOOD are trading the REGULATORY event; MSTR is trading BTC spot, which is flat at $62.8k. The regulatory optimism has not transmitted to the underlying coin at all.

## [08:00 ET] MACRO — Strait of Hormuz: still closed, negotiations deadlocked
- US/Israeli operations against Iran began late Feb 2026. Iran attacked tankers transiting Hormuz along Oman's coast; US responded with airstrike waves and **reimposed a naval blockade**.
- Traffic: **8-15 vessels/day crossed on Aug 4, 5, 6** (MarineTraffic) vs ~**130/day pre-conflict**. A ~90% collapse in the world's most important oil chokepoint, still in force.
- A US-Iran MOU signed **June 17** to reopen the strait collapsed within days over which routes vessels could use. Iran's Foreign Ministry: "as long as the U.S. naval blockade continues, the necessary conditions for the reopening of the Strait of Hormuz do not exist."
- Prices: Brent rose >2% overnight into Wed 8/12 to near **$90**; on the earlier escalation WTI closed **$82.13** (+5%) and Brent settled **$87.72** (+5%).
- No de-escalation path is currently visible. This is a persistent, unresolved supply shock — not a headline that decays.
- sources: https://www.aljazeera.com/economy/2026/8/12/oil-prices-rise-as-attacks-dent-hopes-for-strait-of-hormuz-reopening , https://www.cnbc.com/2026/08/10/oil-prices-today-brent-wti-hormuz-trump-iran.html , https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis , https://www.aljazeera.com/economy/2026/7/10/strait-of-hormuz-shipping-grinds-to-halt-as-us-iran-resume-fighting

## [08:00 ET] EVENT MARKETS — Kalshi, live 2026-08-14 AM (cents = implied prob)
- **KXCPIYOY-26AUG-T3.4** "CPI y/y above 3.4% for year ending Aug 2026": yes 26/38c, last 31c, **prev 45c**, OI 6,110, resolves 2026-09-11. NOTE 12c bid/ask spread — poor execution.
- KXCPIYOY-26AUG-T3.3 "above 3.3%": yes 68/73c, last 73c, prev 78c, OI 5,835.
- KXCPIYOY-26AUG-T3.2 "above 3.2%": yes 78/87c, last 87c, OI 6,329.
  -> Market expects August headline CPI to land in the 3.3-3.4% band. Nobody is pricing a return toward 2%.
- **KXBTCMAXY-26DEC31-99999.99** "BTC above $100,000 at any point by Dec 31 2026": yes **12/13c**, OI **344,169**. Above $120k: 6/7c. Above $150k: 3/4c. Above $200k: 2/3c (OI 291,394).
- **KXRECSSNBER-26** "US recession starts in 2026": yes **6/9c**, last 6c, prev 8c, OI **887,409** — the largest OI on the board.
- KXRECSSNBER-27 "recession in 2027": yes **30/31c**, OI 81,963, tight 1c spread.
- BTC intraday (KXBTC-26AUG1417, resolves today 17:00 ET): modal bucket $62,500-62,999.99 at 36/39c; $63,000-63,499.99 at 27/29c. Consistent with $62,840 spot.
- ETH intraday: $1,860-1,899.99 bucket at 65/66c (prev 8c — repriced hard into spot $1,878).
- source: https://api.elections.kalshi.com/trade-api/v2/markets (series KXCPIYOY, KXBTCMAXY, KXRECSSNBER, KXBTC, KXETH)

## [08:00 ET] CATALYST DETAIL — NVDA Q2 FY2027, WED 2026-08-26 after close
- Press release ~16:20 ET (13:20 PT), call 17:00 ET. Covers fiscal quarter ended 2026-07-27.
- Company guided **$91.0B +/- 2%** ($89.18-92.82B). Street is ABOVE the guide at **$93-95B**; finnhub consensus $93.6B, EPS $2.13. $91B would be +95% y/y.
- Q1 FY2027 Data Center revenue was $75.2B, +92% y/y, +21% q/q; hyperscale vs AI cloud/enterprise now ~50/50.
- Watch items: Data Center growth rate, **Vera Rubin ramp** (management says full production, shipments begin Q3), inference share, margin sustainability.
- Sell-side positioning is one-sided: **43 of 47 analysts at strong buy**, 3 moderate buy, 1 strong sell. That is a crowded setup — the bar is the whisper, not the consensus.
- NVDA 225.30, 4.8% below its 6m high 236.54, sma20 209.28, atr14 7.58 (3.4%/day).
- sources: https://www.hudson-labs.com/research/nvidia-q2-2027-earnings-preview-nvda-revenue-guidance-key-factors , https://www.itechguides.com/nvidia-stock-earnings-preview-q2-fy27-report-date-estimates-and-key-risks/ , https://www.financecalendar.com/event/nvda-earnings-august-2026/

## [08:01 ET] VENUE CHECK — Robinhood Derivatives futures list (verified)
- Robinhood offers: Micro E-mini S&P 500 (MES), Micro E-mini Nasdaq-100 (MNQ), E-mini S&P 500 (ES), E-mini Nasdaq-100 (NQ), **Crude oil (CL) and Micro crude oil (MCL)**, Gold (GC) and Micro gold (MGC), Natural gas (NG), select FX. Also micro crypto futures for BTC, SOL, XRP.
- MCL spec: 100 barrels WTI = 1/10 of CL. $100 per $1.00 point, $0.01 tick = $1.00.
- The canonical RH support URL in config/universe.md (robinhood.com/us/en/support/articles/futures-contracts-available-on-robinhood/) now returns **HTTP 404** — flag for maintainer. Verified via secondary sources instead.
- **Contract month warning:** CME WTI for September 2026 delivery (/CLU6, /MCLU6) terminates trading ~2026-08-20 — that is INSIDE this week. Any crude idea must use **October 2026 (/MCLV6)**, not September.
- sources: https://www.firstcard.app/learn/robinhood-futures-trading , https://lpfutures.com/micro-crude-oil-futures/ , https://www.barchart.com/story/news/33121416/hood-unveils-micro-futures-for-btc-sol-xrp-riding-on-crypto-demand

## [08:01 ET] PRICE — WTI/Brent, live 2026-08-14
- **WTI crude $81.51/bbl, +0.26 (+0.32%)**, quoted 2026-08-14 (tradingeconomics).
- **Brent $87.09/bbl, +0.02 (+0.02%)**, same timestamp.
- "Crude oil was above $81 a barrel on Friday, **gaining nearly 5% this week**" on Middle East supply-route tensions.
- This is the live number behind the USO chart above. Reconciles with the +5.2% 5-day USO move.
- source: https://tradingeconomics.com/commodity/crude-oil

## [08:01 ET] CATALYST DETAIL — WMT Q2 FY2027, THU 2026-08-20 before open
- Consensus EPS **$0.742**, revenue **$186.73B** (vs $177.40B a year ago). Company guided Q2 EPS **$0.720-0.740** — consensus sits AT/ABOVE the top of the company's own guide. FY27 EPS guide $2.75-2.85.
- Stock is **-7.27% since the Q1 FY27 print** and -14.4% off its 6m high (115.72 vs 135.16), but has stabilised: above sma20 112.08 and back above sma50 114.52, +3.3% over 5 days.
- Q1 flagged **higher fuel costs** and **signs of stress on lower-income consumers**. Neither has improved — WTI is up ~5% this week and the Hormuz blockade is intact.
- Positioning: 29 of 39 analysts strong buy, 6 moderate buy, 4 hold. Sell-side is leaning the same way it always does.
- **The link to the macro spine:** the same oil shock that is driving headline CPI (3.4% vs core 2.5%) is a direct COGS and consumer-wallet headwind for WMT. Consensus at the top of guidance into that is an asymmetric setup to the downside.
- sources: https://finance.yahoo.com/markets/stocks/articles/walmarts-quarterly-earnings-preview-know-121442246.html , https://www.benzinga.com/analyst-stock-ratings/analyst-color/26/08/61154613/walmart-could-return-to-its-beat-and-raise-playbook-this-quarter-analyst-says , https://www.fool.com/investing/2026/08/10/should-you-buy-walmart-stock-before-aug-20/

## [08:02 ET] VENUE CHECK — Robinhood Prediction Markets carries Fed decision contracts (verified)
- Live Robinhood event page exists for the Fed decision, e.g. https://robinhood.com/us/en/prediction-markets/economics/events/fed-decision-in-july-jul-29-2026/ , and the economics hub at https://robinhood.com/us/en/prediction-markets/economics
- Robinhood surfaces Kalshi contracts; users predict FOMC decisions to change or hold the target range, $1 per correct contract. So a KXFED-series idea IS placeable in Robinhood.
- Corroboration on the Fed split: CNBC (2026-07-09) "Kalshi traders see roughly 50% odds of a rate hike in 2026 as Fed is split on policy"; as of July, ~54% likelihood of a hike this year. That squares with today's KXFED-26DEC-T3.75 at 54/55c — the December hike probability has been pinned near 54% for over a month and did NOT fall on the in-line CPI, even though the SEPTEMBER contract dropped 35c -> 29c.
- **That divergence is the anomaly worth trading: the market took hike risk OUT of September but left it fully priced for December. It has pushed the same risk one quarter later rather than repricing it.**
- sources: https://www.cnbc.com/2026/07/09/kalshi-traders-see-roughly-50percent-odds-of-a-rate-hike-in-2026-as-fed-is-split-on-policy.html , https://robinhood.com/us/en/prediction-markets/economics

## [08:02 ET] CATALYST DETAIL — TGT Q2, WED 2026-08-19 before open
- Consensus: revenue **$26B**, EPS **$2.30** (finnhub: rev 26.3B, EPS 2.3095). Options market implies a **+/-7.08%** move on the print.
- TGT has rallied **+59% YTD** and +10.9% in the last 20 sessions, closing 155.51 — **0.6% from its 6-month high** (156.47) and far above sma20 145.10 / sma50 137.11.
- Analyst PTs: UBS $166 Buy; RBC $166, lifting Q2 comp growth forecast to 3% from 2%; **TD Cowen $155 with a HOLD**, explicitly warning "expectations remain elevated heading into next week's Q2 earnings."
- So the stock is trading AT the most cautious PT on the street and 6% below the bullish ones, after a 59% run, into a print with a 7% implied move. Priced for the turnaround to be confirmed.
- Contrast with the rest of the complex: WMT -14%, HD -13%, LOW -25% off their 6m highs. TGT is the only one carrying full expectations into its print.
- sources: https://www.tipranks.com/news/target-tgt-stock-could-swing-more-than-7-on-q2-earnings-options-market-signals , https://finance.yahoo.com/markets/stocks/articles/tgt-stock-rallied-over-50-084409199.html , https://www.tradingpedia.com/2026/08/10/targets-rally-faces-tough-test-ahead-of-q2-earnings/ , https://www.fool.com/investing/2026/08/13/should-you-buy-target-stock-before-aug-19/

## [08:03 ET] EVENT MARKETS — Fed decision ladder, live (Kalshi; enormous liquidity)
- **KXFEDDECISION-26SEP-H25** "Hike 25bps at the Sep 16 2026 meeting": yes **26/27c**, last 26c, **prev 33c**, OI **1,447,531**
- KXFEDDECISION-26SEP-H0 "maintains rate": yes 72/73c, last 73c, **prev 66c**, OI **2,850,260**
- KXFEDDECISION-26SEP-C25 "cut 25bps": yes 1/2c, OI 1,632,499 | H26 (>25bp hike) 0/1c | C26 0/1c
- KXFEDDECISION-26OCT-H25: 22/23c (OI 13,073) | 26OCT-H0: 70/75c | 26OCT-C25: 4/5c (OI 64,383)
- KXFEDDECISION-26DEC-H25: 26/27c (OI 10,648)
- **FEDHIKE-26DEC31** "any hike before 2027": yes **52/54c**, OI **779,732**, 2c spread
- **KXRATECUT-26DEC31** "any cut before 2027": yes **12/15c**, last 13c, prev 16c, OI 468,769
- FEDHIKE-27JUN30: 72/73c (OI 82,139) | FEDHIKE-27DEC31: 77/78c
- Spreads are 1-2c with OI in the millions. This is the deepest, cleanest pricing available anywhere on the board today.
- **The repricing:** on the 2026-08-12 CPI, Sep hike-25 went 33c -> 26c and Sep hold went 66c -> 73c. A 7-point move on a print that MATCHED consensus on every line.
- source: https://api.elections.kalshi.com/trade-api/v2/markets (series KXFEDDECISION, KXFEDHIKE, KXRATECUT)

## [08:03 ET] CORRELATION-CAP BOOKKEEPING (per config/strategy.md, max 3 per driver)
- Driver "Hormuz oil shock / inflation re-acceleration": crude long, Fed-hike-yes, WMT-short(fuel costs) = 3. **AT THE CAP.** Nothing further on this driver.
- Driver "US consumer/retail expectations": TGT short (idiosyncratic valuation/turnaround), WMT short (also counted above) = 2.
- Driver "index/flow mechanics": RDDT S&P inclusion = 1.
- Driver "AI/semis capex": NVDA = 1.
- Driver "crypto regulation": COIN/HOOD SEC vote = 1.

## [08:04 ET] LIVE PREMARKET (nasdaq.com quote API, timestamps ~08:02-08:04 ET 2026-08-14)
- **RDDT $175.16 +10.78%** (vs 158.12 close) — the index-inclusion gap. Sitting ON sma50 174.85.
- COIN $152.63 **-0.83%** | HOOD $99.49 +0.12% | MSTR $95.72 **-1.42%**
- TGT $156.00 +0.32% (new 6m high territory) | WMT $115.91 +0.16% | NVDA $225.80 +0.22% | MRVL $225.38 +1.44%
- SPY $778.69 +0.10% | QQQ $734.15 +0.28% | IWM $303.51 +0.00% | SMH $591.00 +0.32%
- XLE $61.31 +0.41% | USO $125.32 +0.23% | GLD $401.32 +0.59%
- **Tell of the morning:** COIN is DOWN and MSTR is down 1.4% in the two hours before a 10:00 ET SEC vote on the first-ever crypto rulemaking. The crypto complex is NOT bidding this event. Whatever the 5-day run-up was, it is not continuing into the print.
- source: https://api.nasdaq.com/api/quote/<SYM>/info?assetclass=stocks

## [08:05 ET] FALSIFICATION RESEARCH — the index-inclusion effect is weaker than folklore
- HBS working paper 23-025 (Greenwood et al.), "The Disappearing Index Effect": the announcement-to-effective-date price effect has largely eroded as index assets scaled and pre-positioning became routine. Morningstar: "The S&P 500 Bump That Doesn't Last."
- Long-horizon evidence is worse: additions underperform matched non-added peers by ~28% at 1yr, 33.1% at 2yr, 40.2% at 3yr, 55.2% at 5yr (significant at 1%). Standard explanation: firms are added near peak valuation.
- **But that explanation does not fit RDDT.** RDDT is being added 24% BELOW its 6-month high after a de-rating, not at a valuation peak. The usual mechanism for post-inclusion underperformance is absent here.
- Practical conclusion: do NOT chase the +10.8% gap for the flow. The flow edge is largely gone. Any RDDT long has to stand on the fundamentals (rev +61% y/y, guide above consensus) plus a pullback entry, not on the index event.
- sources: https://www.hbs.edu/ris/Publication%20Files/23-025_563e45c6-df92-4d9c-ae05-608d4d0acab1.pdf , https://www.morningstar.com/funds/sp-500-bump-that-doesnt-last , https://www.nber.org/digest/nov13/stock-price-reactions-index-inclusion

## [08:05 ET] *** TODAY'S DATED INTRADAY CATALYSTS — 2026-08-14 ***
- **08:30 ET — July Retail Sales.** Headline consensus **+0.2% to +0.3% m/m** (prev +0.2%). Core/ex-autos consensus **+0.2% m/m** (prev **-0.2%**).
- **10:00 ET — U. Michigan Consumer Sentiment, August preliminary.** Headline consensus **54.1** (prev 55.2). Current Conditions 55.0 (prev 54.8). Expectations 55.0 (prev 55.4). **1-year inflation expectations 4.2%, unchanged.**
- **10:00 ET — SEC open meeting, Regulation Crypto proposal vote** (see earlier entry).
- **Read this carefully: UMich at ~54 is a recessionary-level sentiment print, and 1-year inflation expectations at 4.2% are more than double the Fed's target.** That combination — collapsed confidence plus unanchored short-run inflation expectations — is the textbook stagflation signature, and it is the precise reason the Fed committee is split.
- It also supplies the fundamental floor under the bearish consumer-retail read: sentiment 54, 1yr inflation expectations 4.2%, low-income stress flagged by WMT, and fuel costs rising 5% this week — into HD (8/18), TGT/LOW (8/19) and WMT (8/20) prints.
- Note the asymmetry in the ex-autos number: consensus wants +0.2% after a **-0.2%** prior. A second negative core print would be the first genuinely new bearish data in weeks.
- sources: https://x.com/marketsday/status/2085942627464257800 , https://x.com/marketsday/status/2086435767212196273 , https://www.investing.com/economic-calendar/michigan-consumer-sentiment-320

## [08:06 ET] DATA CONFLICT — UMich levels. Trust FRED, flag the calendar.
- FRED UMCSENT (authoritative published series, monthly): **Jun 2026 49.5**, May **44.8**, Apr 49.8, Mar 53.3, Feb 56.6, Jan 56.4, Dec 2025 52.9, Nov 51.0. No July or August value published yet.
- FRED MICH (1-yr inflation expectations): **Jun 2026 4.6%**, May 4.8%, Apr 4.7%, Mar 3.8%, Feb 3.4%, Jan 4.0%.
- The X-sourced calendar I found quotes "Aug prelim est 54.1, prev 55.2" and "1-yr inflation expectations 4.2%". **Those do not reconcile with FRED**, which has June at 49.5 and 4.6%. I could not verify the consensus figures from a primary source.
- **Do not publish the 54.1 / 55.2 / 4.2% numbers as fact.** What IS verified from FRED: consumer sentiment has been running in the **mid-40s to low-50s** all year — May's 44.8 is at or below the prior record low — while 1-year inflation expectations have sat at **4.6-4.8%**, more than double target.
- The qualitative conclusion is unchanged and is well supported by the FRED series alone: US consumer sentiment is at recessionary levels while short-run inflation expectations are unanchored. Stagflationary consumer.
- The 10:00 ET UMich prelim today is still a real dated catalyst; I simply cannot state its consensus.
- sources: https://fred.stlouisfed.org/series/UMCSENT , https://fred.stlouisfed.org/series/MICH

## [08:06 ET] CATALYST DETAIL — HD Q2, TUE 2026-08-18 before open
- Consensus revenue **$47.5B**; EPS **$4.71** vs $4.68 a year ago — **+0.6% y/y. Flat earnings.**
- Slow housing market and macro uncertainty continue to weigh on demand. Management has been reiterating "ho-hum" FY guidance (fiscal year ending Jan 2027), drawing muted reactions.
- Direct oil linkage on the record: on 2026-07-20 HD fell >1% as **rising crude pushed the 10-year Treasury yield to 4.60%**, hurting the housing-demand outlook. The 10y is now 4.68% — higher still.
- Watch: comparable-store sales, Pro vs DIY demand split, digital growth, FY guidance.
- HD 341.70, at sma20 340.69, -13.4% off its 6m high.
- sources: https://finance.yahoo.com/markets/stocks/articles/ahead-home-depot-hd-q2-131502062.html , https://www.tikr.com/blog/home-depot-reports-q2-2026-earnings-on-august-18-can-it-finally-break-out , https://www.fool.com/investing/2026/08/12/should-you-buy-home-depot-stock-before-aug-18/
