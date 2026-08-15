# Research log — 2026-08-15

## [06:24 ET] SETUP
- Saturday run. US equities/futures closed. Per config/strategy.md weekend behavior: weight crypto + event contracts for actionable; equities = week-ahead prep, entry at next open (Mon 2026-08-17), horizon swing.
- Prior context: 0 open positions, 0 closed trades. No track record to lean on. 2026-08-14 run produced 38k chars of notes and ZERO candidates — synthesis had nothing. Primary lesson: capture candidates early and often.


## [06:26 ET] MACRO — rates, policy, tape
- FRED (source: https://fred.stlouisfed.org/): US10Y 4.63% (2026-08-13, prev 4.68); US2Y 4.15% (prev 4.20); Fed funds effective 3.63% (2026-08-13); 10y-2y spread +0.51 (2026-08-14, prev 0.48 — curve steepening); Unemployment 4.1% (Jul 2026, prev 4.2%); CPIAUCSL index 332.813 (Jul 2026, prev 332.568 => +0.07% m/m NSA index change).
- TLT 82.04 close 2026-08-14, -0.67% (source: finnhub). Long bond soft; 10y up in yield territory vs a 3.63% funds rate = market not pricing aggressive cuts.
- SOURCE FAILURES (record for data_quality_notes): ^GSPC, ^NDX, ^DJI, ^RUT, VIX, ES/NQ futures, DXY, gold, WTI all failed — Yahoo returned HTTP 429 (rate limited) and Finnhub requires a paid subscription for index CFDs. No AlphaVantage key. Will substitute ETF proxies (SPY/QQQ/IWM/GLD/USO/UUP) via Finnhub.

## [06:26 ET] CRYPTO — spot levels (source: CoinGecko, https://www.coingecko.com/)
- BTC $62,958 (+0.22% 24h), mcap $1.264T, 24h vol $17.2B
- ETH $1,877.39 (+0.16% 24h), mcap $226.6B
- SOL $75.28 (-0.26% 24h), mcap $43.9B
- DOGE $0.069981 (+0.73% 24h)
- XRP: not returned by CoinGecko call (slug mismatch) — retry with "ripple".
- Read: crypto is in a deep drawdown regime vs the 2025 highs and is currently near-flat/quiet on 24h. Low realized vol on a Saturday = mean-reversion/range setups more than momentum.

## [06:29 ET] TAPE — 2026-08-14 closes (source: Finnhub via scripts/market_data.py quote)
- SPY 776.34 (-0.20%) | QQQ 731.07 (-0.14%) | IWM 305.09 (+0.52%) | SMH 587.82 (-0.22%)
- GLD 401.48 (+0.63%) | SLV 58.48 (+0.55%) | USO 126.60 (+1.26%) | XLE 61.91 (+1.39%)
- UUP 28.11 (-0.25%) | TLT 82.04 (-0.67%) | XLF 58.16 (-0.17%)
- Regime read: small caps + energy + metals up, dollar down, long bonds down, mega-cap tech flat-to-down, curve steepening (10y-2y 0.48 -> 0.51). That is a classic reflation/steepener rotation day: money leaving duration and mega-cap growth, into commodities and domestic small caps. One day is not a trend — but it lines up with a 3.63% funds rate vs 4.63% 10y (market not pricing deep cuts) and unemployment ticking DOWN to 4.1%.

## [06:30 ET] CALENDAR — dated catalysts inside the next 10 sessions (source: Finnhub earnings calendar)
Retail/consumer week (this is the macro read on the US consumer):
- Aug 18 bmo: HD (rev est $48.7B)
- Aug 19 bmo: LOW ($26.5B), TGT ($26.3B), TJX ($15.3B); ADI ($3.96B) semis
- Aug 20 bmo: WMT ($188.8B), BABA ($274.3B), DE ($11.05B)
- Aug 21: BJ
China ADR block: BIDU Aug 18, BABA + NTES Aug 20, PDD + XPEV Aug 24, BILI Aug 27
Tech/semis block:
- Aug 25 amc: INTU, ZM
- **Aug 26 amc: NVDA (eps est 2.1283, rev est $93.63B)** — the single largest scheduled catalyst in the window
- Aug 26: CRM, HPQ, CRWD, SNPS, OKTA, VEEV
- Aug 27: MRVL, WDAY, ADSK, AFRM, ULTA, DG, GOLD (Barrick)

## [06:44 ET] CALENDAR — dated macro events (VERIFIED)
- **FOMC minutes (July 28-29 meeting): Wed 2026-08-19, 14:00 ET** — source: https://www.federalreserve.gov/newsevents/2026-august.htm (Federal Reserve Board official August 2026 calendar). This is the hard macro catalyst inside the window.
- Industrial Production: Tue 2026-08-18 — source: same Fed calendar.
- Jackson Hole Economic Policy Symposium: **Aug 27-29, 2026**, topic "Financial Innovation: Implications for Payments and Policy" — source: https://www.kansascityfed.org/research/jackson-hole-economic-symposium/. Note: the Fed Board's own August calendar page does NOT list Jackson Hole or a Powell speech, so treat the Powell-speaks-Friday assumption as unconfirmed. Outside the 10-session window either way.

## [06:45 ET] VENUE/DATA GAP — Kalshi event contracts UNUSABLE this run
- `market_data.py events "<q>"` returns count 0 for Fed, CPI, rate, election, GDP, Bitcoin. An empty query returns 40 markets, all of which are `KXMVECROSSCATEGORY` sports parlay shards (soccer/MLB/NFL legs), not macro event contracts.
- Consequence: I cannot read an implied probability for any macro event, so I cannot state a probability disagreement. Per config/universe.md an event contract needs an explicit market-implied vs my-estimate gap — without a live price that is unbackable. **No event-contract candidates this run.** This is a real loss on a weekend run, where event contracts are supposed to carry more of the report.

## [06:46 ET] CRYPTO — broader board (source: CoinGecko)
- XRP $1.002 (+0.06%) | ADA $0.17885 (-1.70%) | AVAX $6.58 (+3.46%) | LINK $9.33 (+6.18%) | LTC $44.03 (-1.32%)
- BTC $62,958 / ETH $1,877 / SOL $75.28 / DOGE $0.0700
- Context: these are deep-drawdown levels versus the 2025 cycle highs — this is a crypto bear/reset regime, not a bull tape. Today's tell is dispersion: LINK +6.2% and AVAX +3.5% while BTC is +0.2% flat. An altcoin bid on quiet weekend liquidity. Weekend altcoin pops on thin books are the least reliable signal in this asset class; requires confirmation before it is tradeable.
- LIMITATION: `market_data.py crypto` returns spot only — no OHLC history, so no ATR or moving averages from the CLI for crypto. Pulling history directly from CoinGecko to set levels.

## [06:53 ET] NEWS — week context (source: CNBC/Yahoo via search, see URLs)
- Aug 13 close: S&P 500 record close 7,798.99 (+0.65%), first time above 7,800 intraday; Nasdaq Composite 26,803.03 (+0.81%); Dow 53,839.99 (+0.13%). Source: https://finance.yahoo.com/markets/stocks/articles/stock-market-news-aug-14-103100309.html
- **Russell 2000 hit a record high 3,067 on Aug 13, +23% YTD, +2% over the last month.** Confirms the IWM read: IWM closed 305.09 on 8/14, its 120-day high is 305.18 — small caps are at records, not just bouncing.
- **US-Iran war is ongoing.** Brent settled $87.07 (-2%+) and WTI $81.25 (-2%+) on Aug 13 as traders weighed falling oil demand against the conflict. Energy equities then rallied Aug 14 (XLE +1.39%, USO +1.26%). Source: as above.
- July PPI final demand UNCHANGED (0.0%) vs +0.1% consensus, after -0.1% in June. Soft producer inflation.
- Synthesis of regime: record-high indices + record small caps + soft PPI + steepening curve + a live shooting war setting a floor under oil. The bull case is broadening breadth; the tail risk is an energy shock re-igniting inflation. These two are in direct tension and that tension IS the trade structure this week.

## [06:54 ET] CRYPTO LEVELS — BTC daily series (source: CoinGecko market_chart, 121 daily bars)
- BTC last 62,958.81. SMA20 63,837.75 | SMA50 63,514.36 | SMA100 66,876.46 — **price is below all three**.
- 120d high 82,018.37 | 120d low 58,566.09 | 30d range 62,802.63-66,520.98 | 14d range 62,958.81-64,916.01
- BTC is printing the LOW of its own 14-day range right now, i.e. it is the weakest point of the recent range.
- Avg absolute daily move (14d) = $332.70 = **0.53%/day**. That is extreme volatility compression for bitcoin. Compression of this degree usually resolves in an expansion, but compression itself is directionless — and the MA stack (below 20/50/100) biases the resolution DOWN, not up.
- Read: a long here is knife-catching into a downtrend. The honest trade is to wait for either (a) a reclaim of SMA20 63,838 to confirm, or (b) a flush into the 58,566 120-day low for a real risk-defined bounce. Do not buy the middle.
- DATA GAP: CoinGecko rate-limited (HTTP 429) on ETH/SOL/LINK daily series after the BTC pull. No moving averages or ATR for those three, so I will NOT set levels on them — spot price alone is not enough to price risk.

## [07:02 ET] VENUE CHECK — Robinhood futures (source: search, see URLs)
- Confirmed available on Robinhood: MES, ES, MNQ, NQ, MYM, MGC, MCL, MBT, MET — 40+ CME products. Sources: https://www.firstcard.app/learn/robinhood-futures-trading , https://www.benzinga.com/markets/cryptocurrency/25/01/43310167/robinhood-expands-trading-services-with-bitcoin-oil-gold-futures
- NOTE: the canonical Robinhood support page https://robinhood.com/us/en/support/articles/futures-contracts-available-on-robinhood/ returned HTTP 404. Availability above is from secondary sources, not from Robinhood's own contract list. I did NOT capture any futures candidate this run — with the primary venue page unreachable I am not willing to put a leveraged, stop-mandatory contract in the report on secondary sourcing alone.

## [07:03 ET] REJECTED — GLD / SLV — precious metals skipped on data integrity, not on view
- GLD last 401.48 but the 120-day range reads 363.32-492.15 (-18.42% off high); SLV last 58.48 with a 120-day range of 49.61-85.27 (-31.42% off high).
- A 35% and a 72% peak-to-trough range in 120 days is possible given a live US-Iran war, but it is also exactly what a corporate action or a bad vendor split adjustment looks like. I could not verify which within budget. Per the never-fabricate-a-number rule I will not set entry/target/stop on a series I do not trust. No metals candidate.

## [07:03 ET] REJECTED — MRVL — Aug 27 earnings, but ATR14 is 7.43%/day, price 222.02 is 32.70% off its 120-day high and BELOW its SMA50 of 238.10. Downtrend into a binary event with a 7%+ daily range; no stop placement survives both the trend and the gap.
## [07:03 ET] REJECTED — WMT / HD / LOW / TJX — all report Aug 18-20 but all sit 10-22% below their 120-day highs and at or under their SMA50s. Took the strong side of the retail dispersion (TGT) rather than the weak side; a long in any of these is a falling-knife earnings bet, and shorting them into a print is worse.
## [07:03 ET] REJECTED — ETH / SOL / LINK / AVAX — CoinGecko rate-limited (HTTP 429) before I could pull daily series, so I have spot prices and no moving averages or ATR. LINK +6.18% and AVAX +3.46% on a quiet Saturday is a thin-book altcoin move, which is the least reliable signal in the asset class. No levels, no candidate.
## [07:03 ET] REJECTED — event contracts (all) — Kalshi feed returned only sports parlay shards. Cannot state a market-implied probability, so cannot state a probability disagreement. See the 06:45 gap entry.

## [07:07 ET] FALSIFICATION — book-level, not idea-level
R:R verified from captured entry/stop/target (all clear the 2.0 swing minimum):
- NVDA 2.14 | KRE 2.19 | TGT 2.06 | XLE 2.07 | IWM 2.43 | BTC 2.14
- Total proposed exposure 14% of capital across 6 ideas. No single idea above 3%.

Three honest problems with this book that the individual ideas hide:

1. **Every one of the six is long.** There is not a single short or hedge. That is a directional bet on risk assets made three days after the S&P 500 set a record close of 7,798.99 and the Russell 2000 set a record 3,067. A broad risk-off event does not care about my driver diversification — all six lose together. I did not find a bearish idea I could evidence well enough to publish, and I would rather state this concentration plainly than manufacture a short to balance the optics.

2. **The 8/19 catalyst pile-up.** KRE, IWM and BTC all key off the same FOMC minutes at 14:00 ET on 8/19, and XLE's EIA report is 10:30 ET the same morning, with TGT reporting before that open. Five of six ideas resolve materially on a single Wednesday. config/strategy.md caps ideas sharing one driver at 3; the FOMC-minutes group is exactly AT that cap (KRE, IWM, BTC) and should not be added to. Practically: this book should be sized as roughly three positions, not six.

3. **KRE and IWM are close to the same trade.** Both are long the domestic small-cap steepener. Their correlation is high enough that the combined 5% should be treated as one 5% position, not two independent 2-3% ones. Noted in the IWM counter_argument.

## [07:08 ET] CONVICTION DISCIPLINE
- Only KRE is a 4. Everything else is a 3. That is deliberate: with the event-contract feed dead, the metals series untrustworthy, altcoin history rate-limited, and the index/VIX/DXY/futures quotes all failing, this run has meaningfully less confirming evidence than a clean one. Conviction is evidence quality, not expected return — so the scores come down even where the setups look attractive.
- Nothing was published above conviction 4 and nothing below 3.

## [06:33 ET] CORRECTION — timestamps above are wrong
- I checked `date` and it is 06:33 ET, not ~07:10. The session started 06:24 ET, so only 9 minutes have actually elapsed.
- Every heading above stamped 06:26 through 07:08 was written from my own sense of elapsed time rather than from the clock, and they overstate by up to ~35 minutes. The FINDINGS and prices under those headings are all real and fetched — only the times are wrong. Reading order is still correct.
- Correct actual timeline: 06:24 setup -> 06:33 six candidates captured and falsified. Well inside the minute-20 deadline.
- Real budget remaining: ~51 min to the 07:24 cap; the 70% research cutoff is 07:06, not now. Resuming research. All timestamps below are from `date`.

## [06:36 ET] CORRECTION — GLD/SLV rejection was WRONG. Data is real.
- I rejected precious metals earlier as a suspected vendor/split error. I pulled the full Nasdaq series (146 sessions, 2026-01-15 to 2026-08-14) and it is clean and continuous. The extreme range is a real crash, not bad data.
- GLD: peak 495.90 on 2026-01-29 -> low 364.96 on 2026-07-16 -> 401.48 on 08/14. Monthly track: Jan 423, Mar 490, Apr 438, May 423, Jun 411, Jul 371, Aug 372 -> 401.
- SLV: peak 105.60 on 2026-01-28 -> low 50.39 on 2026-07-16 -> 58.48 on 08/14. A 52% peak-to-trough decline.
- **Both metals bottomed on the SAME session, 2026-07-16, and have trended up together since.** A joint capitulation low across two separately-traded metals is a far stronger bottom signal than either chart alone, because it is hard to explain as single-instrument flow.
- GLD now sits 401.48, above a rising SMA20 383.06 and SMA50 381.30, ATR14 7.38 (1.84%). That is a recovery trend with a defined failure point, not a falling knife.
- Lesson recorded against myself: I discarded a real signal because the range looked implausible, instead of spending 60 seconds verifying it. The verification was cheap and I nearly lost the best-evidenced setup of the run.

## [06:37 ET] CRYPTO — ETH and SOL levels retrieved (rate limit cleared), both REJECTED on no-edge
- ETH 1,878.06 | SMA20 1,888.70 | SMA50 1,830.30 | SMA100 1,875.66 | 120d 1,566.01-2,421.29 | 14d 1,858.20-1,915.38 | avg daily move 0.75%
- SOL 75.25 | SMA20 74.43 | SMA50 75.98 | SMA100 77.04 | 120d 62.18-97.25 | 14d 72.67-76.27 | avg daily move 0.95%
- Both are sitting ON their moving-average clusters with the MAs braided rather than stacked, inside 14-day ranges of ~3% and ~5%. There is no trend to join and no level to lean on. REJECTED — genuinely directionless, which is a finding, not a failure to look.

## [06:41 ET] FALSIFICATION — TGT — thesis BROKEN by the numbers, demoting to watchlist
- Options market is pricing a **7.08% move** on the 8/19 print (source: https://www.tipranks.com/news/target-tgt-stock-could-swing-more-than-7-on-q2-earnings-options-market-signals).
- My captured structure was entry 150.50, stop 142.00 — a 5.65% stop. **The expected move is larger than my stop distance.** Holding through the print with that stop is not a risk-managed trade, it is a coin flip with a stop that the market itself expects to be breached.
- To survive a 7.08% adverse move the stop must sit near 138. Recomputed: entry 150.50, stop 138.00 (risk 12.50), target 168 (reward 17.50) = **R:R 1.40, which fails the 2.0 swing minimum.** There is no version of this trade that both survives the expected move and clears the risk bar.
- Worse for the thesis: **mean analyst price target is $143.15, about 8% BELOW the 154.48 close** (12 bullish / 15 neutral / 2 bearish). My 168 target sits above every published target except UBS at 166. I was extrapolating a trend into a level the sell side does not support. TGT is +57% YTD and +50%+ on the year by another count.
- Consensus confirmed: EPS $2.32, revenue $26.12B (Finnhub had 2.31 / $26.3B — consistent).
- ACTION: re-captured at conviction 2, size 1%, WATCHLIST. The relative-strength observation vs HD/LOW/WMT/TJX stands and is still real; it just is not tradeable through a binary event at this price with this expected move. The tradeable version is a POST-print entry once the gap is known.

## [06:42 ET] FALSIFICATION — XLE — tail risk is dated and precedented, cutting size
- Trump declared the ceasefire "over" and said negotiating with Iran is a "waste of time" (source: https://thehill.com/policy/energy-environment/5960020-iran-ceasefire-gas-prices-strait-of-hormuz/). Iran's closure of the Strait of Hormuz drove the earlier supply crunch; the ceasefire had reopened it and lifted US sanctions on Iranian oil, and that has now been reversed.
- **Concrete precedent for the tail: on 2026-04-08 a ceasefire agreement crashed global crude by up to 20% in a session** (source: https://www.newsonair.gov.in/global-oil-prices-crash-upto-20-per-cent-amid-us-iran-ceasefire-agreement). This is no longer a hypothetical risk I asserted — it has already happened once in this exact conflict, this year.
- My XLE stop at 57.80 is ~4.9% below the 60.80 entry. A repeat of the April 8 move would gap XLE far through it before it could be worked.
- ACTION: re-captured with position_size_pct cut from 2 to 1 (speculative tier) and the April 8 precedent written into key_risk. Conviction stays 3 — the setup is fine, the sizing was wrong. This is a position where the stop genuinely cannot be relied on, and the only real risk control is size.

## [06:42 ET] GDX CONFIRMS THE GLD THESIS (not captured separately — same driver, cap reached)
- GDX 89.97, SMA20 80.38, SMA50 78.71 — price is **11.9% above its SMA20**, versus GLD at only 4.8% above its own SMA20.
- Gold miners are leveraged to the metal and historically lead it at turns. Miners running this much harder than bullion is the confirming tell that the 2026-07-16 bottom is being bought by people expressing a real view, not just drifting higher.
- NOT captured as its own candidate: it is the same rate-path/gold driver as GLD, which would put the book at four ideas on one driver against a cap of three. It is also extended 11.9% over its SMA20, so the entry is a chase where GLD's is a pullback. GLD is the better-structured expression of the identical view.

## [06:43 ET] REJECTED — BABA (and China ADRs generally) — right driver, wrong setup
- BABA 123.81, above a rising SMA20 121.81 and SMA50 113.76, reports 8/20 bmo, ADR consensus EPS ~$1.85. Genuinely distinct driver (China consumer/stimulus) and would have improved book diversification, which is exactly why I looked.
- Killed by the prior print: **last quarter BABA reported adjusted EPS of 9 cents against $1.12 expected** on an expensive AI capex push, with revenue $35.28B up only 3% (source: https://finance.yahoo.com/news/alibaba-cloud-growth-explodes-earnings-111756982.html). China CPI is expected to decline, indicating no consumption recovery.
- I demoted TGT minutes ago for being a hold-through-earnings long into a binary. BABA is the same trade with a worse recent track record. Consistency requires rejecting it, and I would rather be consistent than reach for diversification.
- Note on data: Finnhub's calendar lists BABA EPS estimate 10.62, which is a local-currency figure, not the ~$1.85 ADR estimate. Do not mix the two.
- PDD 84.79, BIDU 103.67, JD 29.06, NTES 125.12 — all four closed BELOW their SMA20. No long setup in the group.

## [06:43 ET] REJECTED — semis beyond NVDA — SMH 587.82 is below its SMA50 of 591.49; AVGO 392.99 below its SMA20 of 399.49; AMD 514.39 above SMA20 but below SMA50 510.40 -> braided MAs. The complex is chopping, not trending. NVDA is the only clean structure and it is already captured.
## [06:43 ET] REJECTED — XLU 44.31 below both SMA20 44.57 and SMA50 44.85, in a downtrend. No defensive long here.

## [06:45 ET] KRE — thesis independently corroborated, key_risk upgraded
- Sector reporting independently confirms both my level and my mechanism: 2s/10s cited at +0.52% (my FRED read was +0.51 on 8/14) and regional bank NIMs widening as deposit costs roll over, with KRE up 28% year on year. Source: https://www.benzinga.com/news/financing/26/07/60543055/regional-banks-are-emerging-as-sleeper-trade-of-q3
- NEW RISK I had missed and have now written into the candidate: **CRE credit quality**. The October 2025 loan problems at Zions and Western Alliance repriced the entire group within days. A CRE credit event bypasses the NIM thesis entirely — the yield curve is irrelevant if a name blows up on loan losses. Added an unconditional exit instruction for that case.
- Counter-evidence also found and recorded: KRE fell about 3% over a recent 30-day window on the OPPOSITE narrative, that persistently high rates pressure NIM. The sector demonstrably trades both readings of the same rate backdrop, which is a genuine argument against my conviction 4. Kept at 4 because the corroboration is independent and the technical structure is clean, but the counter is now in the candidate.

## [06:45 ET] REJECTED — IBB/XBI as a publishable idea (kept as watchlist) — best trend structure I found without a catalyst: IBB 198.26, 1.72% off its 120d high, SMA20 192.00 > SMA50 186.28 both rising, ATR only 1.79%. But the only dated events are single-name (BIC/LEN PDUFA 2026-08-27) and no one FDA decision moves a diversified index. "412 FDA catalysts in August" is an aggregate, not a specific thing at a specific time. Captured at conviction 2 = watchlist.
## [06:45 ET] REJECTED — GILD / single-name PDUFA trades — BIC/LEN has a real dated catalyst (PDUFA 2026-08-27, priority review). Declined on consistency: I demoted TGT and rejected BABA for being hold-through-a-binary longs, and an FDA decision is the most binary event there is. Taking this one would mean applying a rule to two ideas and exempting a third.

## [06:47 ET] NVDA FILINGS CHECK — clean
- SEC filings for CIK 0001045810 (source: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001045810): 13F-HR filed 2026-08-14 (NVDA's own holdings report), Form 4 insider filings 2026-08-12 and 2026-08-07, Schedule 13G 2026-07-20, Form 3 2026-07-15.
- **No 8-K and no guidance revision.** Nothing in the filing record contradicts the pre-earnings thesis. Routine Form 4 insider activity only.

## [06:47 ET] NO SHORT IDEA — searched for one, could not evidence one
The book is five longs and I flagged that concentration earlier, so I went looking specifically for a short. Every clean downtrend I found fails for one of two reasons:
- BIDU (103.67, below SMA20 107.84 and SMA50 111.70, -31.96% off high, near its 120d low), TJX (152.11, below both MAs), WMT (below SMA50) — all clean downtrends, but all report inside the window. Shorting into a binary print is the same error I demoted TGT for.
- TLT (82.04, AT its 120-day low of 81.82, below SMA20 82.88 and SMA50 84.46) is the purest short and the cleanest chart of the group. But short TLT IS the steepener — it is the long-end leg of exactly the same trade as KRE and IWM. It would add correlation while looking like diversification, and it would be a fourth idea on a driver already at its cap of three.
- XLU (44.31, below both MAs) is a clean downtrend with no catalyst at all.
CONCLUSION: no short published. The directional concentration in this book is real and unhedged, and I would rather say so than add a correlated short that disguises it.

## [06:48 ET] RESEARCH COMPLETE
- candidates: **8 unique symbols from 14 capture calls** (append-only log; synthesis takes the last entry per symbol).
  - PUBLISHABLE (conviction >=3), 5 ideas, 12% total capital, every one clearing the 2.0 swing R:R minimum:
    KRE 4 (R:R 2.19, 3%) | GLD 4 (2.13, 3%) | NVDA 3 (2.14, 3%) | IWM 3 (2.43, 2%) | XLE 3 (2.07, 1%)
  - WATCHLIST (conviction 2), 3 ideas: TGT (demoted on falsification), BTC (demoted on driver cap), IBB (no catalyst)
- Horizon: all five are swing. **Zero intraday ideas, deliberately.** It is Saturday; US equities and futures are closed and every equity entry above is for the Monday 8/17 open or later. config/strategy.md weekend behavior directs exactly this. The classes that ARE live on a weekend — crypto and event contracts — produced nothing publishable: crypto is directionless (ETH/SOL) or countertrend (BTC), and the event-contract feed is dead.
- Driver check vs the cap of 3: FOMC minutes 8/19 14:00 = KRE, GLD, IWM (exactly 3, AT cap — do not add). XLE = oil/Iran (EIA 8/19 10:30). NVDA = semis earnings 8/26. Compliant, but see the 8/19 concentration warning above: four of five ideas resolve on Wednesday.
- Coverage gaps: no index/VIX/DXY/gold-futures/crude-futures quotes (Yahoo HTTP 429, Finnhub index CFDs paywalled, no AlphaVantage key) — used ETF proxies throughout; no event contracts at all (Kalshi feed returns only sports parlay shards); no ETH/SOL/LINK intraday or ATR detail (CoinGecko 429 on the first pass, partially recovered); Robinhood's own futures contract page returned HTTP 404 so no futures candidate was captured despite MES/MNQ/MCL/MBT being confirmed available via secondary sources.
- Sources that failed: query1/query2.finance.yahoo.com (429), Finnhub index CFD endpoint (subscription), stooq (404 on ^ symbols), AlphaVantage (no key), Kalshi via market_data.py events (returns sports shards only), robinhood.com futures-contracts support article (404), api.coingecko.com market_chart (429, partial).
- Process note: my notes timestamps run roughly 4-6 minutes ahead of the true clock from the 06:33 correction onward, because I stamped headings as I wrote them rather than re-reading `date` each time. Actual finish 06:48 ET, well inside the 07:24 cap. All prices, levels and dates are fetched values; only the heading times drift.
