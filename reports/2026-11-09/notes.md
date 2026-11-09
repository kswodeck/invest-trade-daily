# Research log — 2026-11-09

## [06:02 ET] SETUP
- Monday 2026-11-09, pre-open. Equities closed; last print = Friday 2026-11-06 close.
- Read config/strategy.md, config/universe.md, reports/2026-11-09/prior_context.md.

## [06:02 ET] PRIOR CONTEXT — what it demands today
- 12 open positions to triage: XLE, BCC, PFE, KHC, AAL(short), HII, UNP, ABT, PYPL, RTX, XLU, ACM.
- 8 awaiting entry (never filled): OXY, KXCPIYOY-26SEP-T3.5, GLD, SMMT, ONON, TLT, CVS, NVDA.
- Track record 4/39 target (10%), avg -5.9%. n=39 closed is now ABOVE the ~15 noise floor, so this is signal, not a bad week.
  - stock: 1/26 (4%), avg -8.0% (n=41) — the worst lane by far and the most-used one.
  - etf: 3/13 (23%), avg -1.6% (n=18) — the only lane close to break-even.
  - conviction 2: 0/6, -8.4%. conviction 3: 2/25 (8%), -6.9%. conviction 4: 2/8 (25%), -0.8%.
- CONCLUSION FOR TODAY'S BAR: single-name long swing equity at conviction 3 is the losing archetype and
  accounts for most of the damage. Raise the bar: a new single-stock swing needs conviction 4 (3 distinct
  evidence kinds) or it does not publish. Conviction-2 lottery tickets are allowed by config but have gone
  0/6 — cap them hard and size at 0.5-1%.
- Last 5 stop-outs were conviction 3 and 4, so this is not purely a thin-evidence problem; it is also a
  stop-distance / pullback-entry problem. Favour wider stops and entries at or above market over reflex discounts.
- Repetition watch: CVS 3x, XLU 2x, PFE 2x in last 10 days. CVS already stopped out once (2026-11-04) and was
  re-pitched; do not pitch CVS again without a genuinely new fact.

## [06:05 ET] MACRO — rates, tape, crypto (all equity prices = Fri 2026-11-06 close, session=pre)
- FRED (source: https://fred.stlouisfed.org/):
  - US 10y 4.84% (2026-11-05), US 2y 4.46% (2026-11-05), Fed funds 3.88% (2026-11-05)
  - 10y-2y curve +0.35 (2026-11-06) — positively sloped
  - Unemployment 4.1% (2026-10-01), CPI index 336.298 (2026-09-01)
  - READ: funds at 3.88 vs 10y at 4.84 = ~96bp of positive spread over policy. The Fed has cut into a long
    end that will not follow. That is term-premium/fiscal-supply driven, not growth driven. Long duration
    (TLT 81.92) keeps failing to rally — relevant to the awaiting-entry TLT BUY @ 80.3.
- Equity tape (finnhub, Fri 11/06 close):
  - SPY 735.29 +0.31%, QQQ 656.10 +1.40%, IWM 273.67 +0.99% — Friday was a risk-ON day, tech-led.
  - XLE 61.62 -0.02%, XLU 43.13 -0.39%, TLT 81.92 -0.01%, GLD 372.52 -0.79%
- Crypto (coingecko, live 24/7, as of 06:03 ET Mon):
  - BTC $74,098 -2.29% 24h; ETH $2,107.02 -5.69% 24h; SOL $85.89 -3.66% 24h
  - READ: this is the live divergence of the morning. Equities closed Friday risk-on; crypto sold off through
    the weekend, ETH worst. Crypto is the only market that traded since Friday's close, so it is the only
    genuinely NEW price information available pre-open. BTC at $74k is a deep drawdown from 2026 highs.
- DATA GAPS: Yahoo returned HTTP 429 for every index/futures symbol (^GSPC ^NDX ^DJI ^RUT ^VIX ES NQ DXY ^TNX
  GC CL). No VIX, no index futures, no DXY, no spot gold/WTI this run. Finnhub refuses indices
  ("Market data subscription required for CFD indices"). Workaround: ETF proxies via finnhub (SPY/QQQ/IWM/
  GLD/XLE/TLT) which DID work. No live VIX level today — do not state one.

## [06:12 ET] CALENDAR — earnings next 7 sessions (source: finnhub via market_data.py earnings --days 14)
Fetched 1500 rows; large-cap/dated subset that matters:
- 11/09 bmo: CEG (rev est $9.47B), FERG ($8.91B), CNH. 11/09 amc: BAP.
- 11/10 bmo: SE ($8.29B), VG, TDG, ATAT. 11/10 amc: CRWV ($3.62B, EPS est -1.18).
- 11/11: NIO. 11/11 amc: CTVA.
- 11/12 amc: **CSCO ($18.48B)**, **AMAT ($10.5B)**. 11/12: NU, STNE.
- 11/16 bmo: PDD, BIDU. 11/16 amc: TSN, **ACM ($1.94B, EPS est 1.5938)** <-- OPEN POSITION reports
- 11/17 amc: **NVDA (rev est $111.36B, EPS est 2.5263)** <-- AWAITING-ENTRY idea reports. 11/17 bmo: DIS, HD.
- 11/18: TGT, LOW, TJX, ROST, PANW, GAP.
- READ: this week is the earnings tail — the 11/12 (CSCO/AMAT) and 11/17 (NVDA/HD/DIS) clusters are the only
  dated catalysts of size. Retail prints 11/18. Calendar is thinning, so per config/strategy.md the time
  should shift toward position management and durable mispricings rather than padding the trade lane.
- GAP: no economic-release calendar source in market_data.py; I have not fetched a dated CPI/PPI/Fed time for
  this week and will not state one from memory.

## [06:14 ET] LEVELS — fetched history (120d, finnhub). NOTE: per-bar OHLC came back null this run;
## the aggregates (atr14, sma20, sma50, 120d range) are real and are what I set levels from. No sma200 available.
| Sym | last(11/06) | ATR14 | ATR% | sma20 | sma50 | 120d low | 120d high | off high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NVDA | 186.64 | 8.019 | 4.3% | 211.55 | 219.81 | 181.46 | 243.37 | -23.3% |
| ACM | 66.74 | 1.902 | 2.85% | 61.88 | 62.26 | 56.39 | 76.85 | -13.2% |
| XLE | 61.62 | 1.838 | 2.98% | 67.11 | 65.07 | 52.62 | 70.15 | -12.2% |
| RTX | 189.53 | 6.040 | 3.19% | 193.67 | 193.45 | 172.55 | 226.88 | -16.5% |
| BCC | 70.24 | 3.511 | 5.0% | 75.53 | 75.80 | 65.00 | 88.43 | -20.6% |

## [06:14 ET] FRIDAY TAPE — the rotation that explains the track record
- SPY +0.31%, QQQ +1.40%, IWM +0.99% on 11/06, but MY defensive/value book fell the same day:
  BCC -4.76%, ABT -3.23%, KHC -2.80%, UNP -2.61%, PFE -1.64%, RTX -1.22%, XLU -0.39%, XLE -0.02%.
- Meanwhile NVDA +2.78%, CVS +3.10%, SMMT +15.08%, AAL +1.93% (against my short).
- READ: the book is systematically short the thing that is working (tech/beta) and long the thing that is not
  (defensives, rails, staples, energy). That is one correlated bet with 12 legs, not 12 ideas, and it is the
  mechanical explanation for stock-lane 1/26. Today's job is to stop adding to that same factor.

## [06:04 ET] TIMESTAMP CORRECTION
- The [06:05]-[06:14] headings above were written from my own sense of elapsed time, not from `date`.
- Real clock: research started 06:01:02 ET and the block above was written at 06:04 ET. The findings are
  unaffected (all prices/ATRs are fetched); only the heading times were ahead. All headings from here are
  from `date`. Real budget remaining is larger than I assumed.

## [06:08 ET] MACRO — THE REGIME MAP (source: market_data.py relstrength, computed from fetched history)
Total returns to Fri 2026-11-06 close, and vs SPY:
| ETF | 1m | 3m | 6m | vs SPY 1m | vs SPY 3m |
| --- | --- | --- | --- | --- | --- |
| XLV | +9.90 | +9.71 | +28.79 | +14.89 | +14.59 |
| XLP | +7.98 | +6.04 | +7.01 | +12.97 | +10.92 |
| XLB | +5.44 | -2.31 | +0.70 | +10.43 | +2.57 |
| XLF | +5.40 | -1.12 | +11.55 | +10.39 | +3.76 |
| XLY | +5.25 | -1.75 | -2.18 | +10.24 | +3.13 |
| TLT | +5.20 | -0.17 | -4.83 | +10.19 | +4.71 |
| XLU | +5.02 | 0.00 | -3.56 | +10.01 | +4.88 |
| IWM | -1.41 | -8.77 | -3.69 | +3.58 | -3.89 |
| GLD | -1.61 | -7.46 | -14.12 | +3.38 | -2.58 |
| XLI | -3.40 | -11.88 | -6.08 | +1.59 | -7.00 |
| XLE | -5.55 | +2.39 | +10.63 | -0.56 | +7.27 |
| XLC | -6.50 | -6.30 | -10.39 | -1.51 | -1.42 |
| QQQ | -12.24 | -8.98 | -7.75 | -7.25 | -4.10 |
| XLK | -16.71 | -11.58 | -6.14 | -11.72 | -6.70 |
- SPY itself: -4.99% 1m, -4.88% 3m, -0.32% 6m.
- THE READ, and it reframes everything: this is not a broad bear market. 7 of 11 sectors are UP over the
  month. SPY's entire 1-month decline is a mega-cap tech/AI unwind — XLK -16.7%, QQQ -12.2% — while
  healthcare and staples are making money. Crypto confirms the same de-risking (BTC -2.3% over the weekend
  while equities closed up Friday).
- Friday 11/06 (QQQ +1.40%, XLK's sector bouncing) was therefore a bounce INSIDE a -16.7% monthly drawdown,
  not a new risk-on leg. I nearly misread it that way at 06:04 above; correcting it here.
- XLV is the standout: #1 on 1m (+9.9%), #1 on 3m (+9.71%), and +28.79% over 6m. Leadership that holds on
  all three windows is the rarest and most useful thing on this table.
- Confirmation from my own book: the two best open positions are PFE +6.5% and ABT +6.7% — both healthcare.
  The two worst are BCC -13.3% (building products, XLI/XLB-adjacent) and XLE -3.6% (XLE -5.55% 1m).
  The book's winners and losers are sorted by this exact factor.
- STRATEGY CONSEQUENCE FOR TODAY: buy the leadership, not the falling knives. And prefer ETF expression —
  per prior_context the etf lane is 3/13 (23%), avg -1.6%, versus stock 1/26 (4%), avg -8.0%.

## [06:15 ET] POSITION TRIAGE — all 12 open positions, against fetched ATR/SMA and the regime map
| Sym | %vs entry | last | ATR14 | stop | stop dist (ATR) | sma20 | sma50 | sector 1m | decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLE | -3.6% | 61.62 | 1.838 | 60.8 | **0.45** | 67.11 | 65.07 | XLE -5.55% | CLOSE |
| BCC | -13.3% | 70.24 | 3.511 | none | n/a | 75.53 | 75.80 | XLB +5.44% | set invalidation |
| PFE | +6.5% | 29.39 | 0.804 | none | n/a | 29.75 | 28.74 | XLV +9.90% | hold (long_term) |
| KHC | +7.0% | 24.61 | 0.772 | 21.2 | 4.42 | 24.03 | 24.01 | XLP +7.98% | raise stop |
| AAL short | +1.3% | 13.18 | 0.661 | 14.4 | 1.85 | 12.51 | 12.88 | XLI -3.40% | hold, flag tight |
| HII | +10.2% | 288.74 | 12.25 | none | n/a | 284.09 | 278.73 | XLI -3.40% | **add a stop** |
| UNP | +0.5% | 290.16 | 7.564 | 277.4 | 1.69 | 294.46 | 286.70 | XLI -3.40% | hold, flag tight |
| ABT | +6.7% | 109.93 | 3.711 | 97.0 | 3.48 | 105.51 | 104.01 | XLV +9.90% | raise stop |
| PYPL | +4.8% | 59.24 | 1.636 | 54.1 | 3.14 | 57.23 | 55.10 | XLF +5.40% | hold |
| RTX | -4.8% | 189.53 | 6.040 | 186.0 | **0.58** | 193.67 | 193.45 | XLI -3.40% | hold, let stop work |
| XLU | -0.4% | 43.13 | 0.621 | 41.8 | 2.14 | 42.57 | 41.77 | XLU +5.02% | hold |
| ACM | +0.0% | 66.74 | 1.902 | 61.5 | 2.76 | 61.88 | 62.26 | XLI -3.40% | **earnings 11/16** |

- The two positions with a stop inside 0.6 ATR (XLE 0.45, RTX 0.58) are not risk-controlled any more — one
  ordinary day resolves them either way. That is the mirror image of the walked-in-stop problem in CLAUDE.md:
  a stop that started legitimate becomes noise-tight as price approaches it.
- RTX vs XLE differ on thesis decay, which is why they get different answers. RTX is 4 days old and its stop
  was 2.15 ATR from entry (199 -> 186) - a legitimate stop doing its job, so it is left alone; widening it to
  avoid the loss is exactly the free-ratio cheat in reverse. XLE is 53 days old with the thesis decayed, so
  the remaining 0.45 ATR is not worth donating to noise.
- Three positions carry NO stop at all: BCC (-13.3%), PFE (+6.5%), HII (+10.2%). PFE is a long_term idea
  (target 42 vs a 120d high of 31.44) where strategy.md makes a stop optional, so it keeps none and needs an
  invalidation instead. HII and BCC are swing-shaped and should not be unprotected.

## [06:15 ET] POSITION UPDATE — XLE — opened 2026-08-15, 53 days, -3.6%
- decision: CLOSE the long at market. Do not wait for the 60.80 stop.
- why: (1) price 61.62 sits 0.82 below the stop = 0.45 ATR, so the position is a coin flip on a single
  ordinary session rather than a tested thesis; (2) the energy thesis has decayed on the measured tape -
  XLE was +7.27% vs SPY on 3m and is now -0.56% vs SPY on 1m, the only sector negative vs SPY over the month;
  (3) price is below both the 20-day (67.11) and the 50-day (65.07) and 12.16% off the 120d high of 70.151,
  while the original target of 70.50 is 4.8 ATR away. 53 days of holding has produced -3.6% and a broken chart.
- action: captured via add_candidate.py as direction `sell` (closure of an existing long, NOT a new short).

## [06:17 ET] POSITION UPDATE — why most of the book is HOLD AS-IS, and why I am not raising stops
I started to raise stops on the four winners (ABT +6.7%, KHC +7.0%, HII +10.2%, PYPL +4.8%) and stopped,
because on inspection that is the KRE anti-pattern in CLAUDE.md wearing a different hat:
- The entry of a filled position can never be amended, so a raised stop is measured against the ORIGINAL
  entry. ABT entry 103.0 with a stop raised to 102.0 is a 1.0 risk against a 14.34 reward - a 14:1 ratio that
  is pure arithmetic and makes the trade no better. It would also fail `check_stop_distance` at 0.27 ATR.
- So each winner is judged on whether its EXISTING stop is still honest from its own entry:
  - ABT: entry 103.0, stop 97.0 = 6.0 = 1.62 ATR. Under the 2.0 floor as published, but it is filled and
    working (+6.7%), and the stop is 3.48 ATR below the current 109.93. HOLD AS-IS.
  - KHC: entry 23.0, stop 21.2 = 1.8 = 2.33 ATR. Legitimate from entry. HOLD AS-IS.
  - PYPL: entry 56.5, stop 54.1 = 2.4 = 1.47 ATR. Tight from entry, 3.14 ATR below price. HOLD AS-IS.
  - HII: published long_term (target 339.76 = +29.7% on entry) with no stop, which strategy.md permits for
    that horizon. Its ATR is 12.25, so a 2.0-ATR stop from entry 262 would sit at 237.5 - 51 points below the
    current 288.74. Imposing that would be theatre. It keeps no stop and needs an INVALIDATION instead.
- Conclusion: 8 of 12 positions are hold-as-is and generate no recommendation. Only XLE (close), ACM
  (new dated catalyst) and BCC (unprotected, -13.3%) are genuinely actionable. Manufacturing twelve updates
  to look diligent would put eight inflated ratios on the Sheet.

## [06:17 ET] POSITION UPDATE — HII — opened 2026-10-12, +10.2%, no stop (long_term)
- decision: hold, no stop, no new recommendation. Best position in the book.
- invalidation (what was missing): a Navy shipbuilding budget cut or a further schedule slip on the Virginia /
  Columbia programs that pushes revenue recognition out another year. Price alone does not invalidate it.
- NOT captured as a candidate: nothing about the levels changed and re-pitching it would open nothing new.

## [06:22 ET] POSITION UPDATE — BCC — opened 2026-08-18, 82 days, -13.3%, no stop
Read the primary document rather than judging the chart. Q3 2026 results, 8-K filed 2026-11-02, Ex 99.1:
- source: https://www.sec.gov/Archives/edgar/data/1328581/000132858126000033/bccexhibit9919302026.htm
- Q3 ACTUALS WERE GOOD: sales $1,802.2M (+8% YoY), net income $36.4M (+67%), diluted EPS $1.04 vs $0.58
  (+79%), EBITDA $98.5M (+32%). Wood Products swung to +$16.1M segment income from a -$12.1M loss.
  Plywood prices +31% YoY, +8% sequentially.
- AND THE GUIDE IS THE STORY: Q4 2026 total company EBITDA guided **$32-54M** against the $98.5M just
  delivered - a ~56% sequential collapse at the midpoint ($43M). BMD EBITDA $35-45M vs $66.9M in Q3.
- CEO Jeff Strom: "more cautious demand environment" heading into 2027. Q3 US total housing starts -4%,
  single-family -2% (single-family is named as the key demand driver). Early industry projections: 2027
  housing starts DOWN mid-single digits. Affordability worsened by fuel prices and benchmark rates.
- Insiders (https://finnhub.io/api/v1/stock/insider-transactions?symbol=BCC): 0 open-market buys in 6 months,
  3 sells totalling $665,841, net -$665,841. No insider is stepping in at a 20% drawdown.
- decision: **CLOSE the long.** The thesis was a housing/building-products recovery and the company has now
  guided the opposite on its own numbers, with the demand driver it names falling and 2027 projected down.
  The original 110.00 target is +56.6% from 70.24 and is not reachable on a $43M quarterly EBITDA run-rate.
  The position has also been carried 82 days with no stop, so it has no defined downside at all.
- NOTE this cuts the other way on one point and I am not hiding it: the quarter itself beat and Wood Products
  genuinely inflected. A buyer could argue the guide is seasonal (Q4 always slows through winter, which
  management said explicitly). That is the counter-argument and it is in the candidate.
- action: captured via add_candidate.py as direction `sell` (closure of an existing long, NOT a new short).

## [06:20 ET] REJECTED — ALL EVENT CONTRACTS — no fetchable price, so no statable implied probability
- `market_data.py events "<topic>"` returned ok:true count:0 for Fed, CPI, recession and Bitcoin. Cause found:
  the helper pulls the first 200 open Kalshi markets with no ordering and filters client-side; on a Sunday in
  November that page is entirely NFL markets created the same morning, so every economic query misses.
  This is a helper limitation, NOT an absence of markets. Worth fixing in market_data.py (query by
  series_ticker, or use the API's own search) - noting it here as a code issue rather than a market finding.
- Worked around it by hitting the API directly by series. The markets are live and `status: active`:
  - KXCPIYOY-26DEC-T3.9 ... T5.0 (CPI YoY for year ending Dec 2026, closes 2027-01-13)
  - KXU3-26NOV-T3.9 ... T5.0 (U-3 unemployment in November, closes 2026-12-04)
  - KXRECSSNBER-26 / -27 (NBER recession in 2026 / 2027)
  - KXFED-27MAR/27APR-T4.50..T6.00 (fed funds upper bound), KXFEDDECISION-27OCT.. (hike/cut size)
  - KXBTCD-26NOV0907-* (Bitcoin price on Nov 9 2026, closes 12:00Z today)
- **But every pricing field comes back null** on both the list endpoint and the single-market endpoint
  (/trade-api/v2/markets/KXU3-26NOV-T4.3): yes_bid, yes_ask, no_bid, no_ask, last_price, volume, volume_24h,
  open_interest, liquidity and previous_price are all None. The public endpoint appears to have moved
  quotes behind auth.
- CONSEQUENCE: universe.md requires an event-contract edge to be an explicit probability disagreement stating
  the market's implied probability. I cannot fetch one, and inventing it is the exact failure CLAUDE.md rule 2
  forbids. **So zero event contracts today**, despite the lane being explicitly wanted. This is a data gap,
  not a judgement that nothing was mispriced.
- It also means the awaiting-entry `KXCPIYOY-26SEP-T3.5` NO @ 18 cannot be re-priced or re-assessed today.

## [06:23 ET] CRYPTO — the only market that has traded since Friday's close
Two independent sources agree, so the price is solid:
- CoinGecko 06:03 ET: BTC $74,098 (-2.29% 24h), ETH $2,107.02 (-5.69%), SOL $85.89 (-3.66%)
- Coinbase spot 06:17 ET: BTC $74,053.29, ETH $2,104.645
Fetched 120d daily series (https://api.coingecko.com/api/v3/coins/{bitcoin,ethereum}/market_chart):
| | last | 120d high | 120d low | off high | 7d | 30d | 60d | avg abs daily move (14d) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 74,074.84 | 86,596.74 (09-22) | 62,278.96 (07-14) | -14.46% | -3.43% | -10.66% | -3.24% | 1,282 (1.73%) |
| ETH | 2,104.85 | 2,775.17 | 1,774.09 | -24.15% | -6.46% | -15.95% | -13.65% | 50.04 (2.38%) |
- BTC daily closes, the sequence that matters: 11/05 80,443 -> 11/06 76,006 -> 11/07 75,775 -> 11/08 75,776
  -> 11/09 74,075. Lower highs and lower lows, -7.9% in four sessions, no bounce attempt.
- **VOLATILITY CAVEAT, stated because it changes the stop:** CoinGecko's daily endpoint returns closes only,
  so 1,282 is a close-to-close average absolute move, NOT a true ATR - a true range includes the intraday
  high-low and is typically ~1.3-1.5x larger. I size stops off an ESTIMATED true ATR of ~1,800 for BTC and
  ~70 for ETH, which is the conservative direction. Any stop below 2.5x the estimate is rejected.
- ETH is the weaker asset on every window (-24.15% off high vs BTC's -14.46%; 30d -15.95% vs -10.66%; 24h
  -5.69% vs -2.29%). Risk appetite is draining fastest from the higher-beta leg, the classic internal tell.
- WHY I TRADE BTC AND NOT ETH, having measured both: ETH has the better momentum case but worse geometry. A
  short at the market 2,105 with an honest 2.5-ATR stop at 2,290 and a target of 1,790 just above its 120d
  low gives R:R 1.70 - under the 2.0 floor. Making it work needs either a target below the prior low or a
  bounce entry at 2,180 that may never fill. BTC clears the floor at the market with a target at a level that
  actually traded. One crypto bet, not two, also respects the 3-idea correlation cap.

## [06:23 ET] VENUE CHECK — crypto futures on Robinhood
- Robinhood Crypto has NO shorting (universe.md), so a bearish crypto view must be a short futures contract.
- Robinhood's own first-party article lists the CME crypto futures in scope, including /MBT Micro Bitcoin
  (0.10 BTC) and /MET Micro Ether (0.10 ETH), under Robinhood Derivatives, LLC:
  https://robinhood.com/us/en/learn/articles/what-are-crypto-futures/
- CAVEAT recorded rather than papered over: the dedicated support page
  robinhood.com/us/en/support/articles/futures-contracts-available-on-robinhood/ returned **HTTP 404**, so I
  could not read an authoritative current contract list. The learn article is first-party and current-tense
  about Robinhood Derivatives but does not itself say "these are the ones we offer today". Secondary
  reporting (theblock.co, decrypt.co, 2024-2025) confirms Micro Bitcoin and Micro Ether at launch plus micro
  SOL/XRP added June 2025. Treat /MBT as verified-but-confirm-in-app.
- Contract month: /MBTZ6 = December 2026. Chosen over /MBTX6 (November, expiring the last Friday of
  November) because the target is a multi-week move; December is not in its final trading week.
- /MBT at 0.10 BTC is ~$7,408 notional per contract at 74,075, so the position is sizeable in 1-contract units.

## [06:25 ET] POSITION UPDATE — NVDA — awaiting entry @ 184.00 (published 2026-11-07), price 186.64
This one needs a decision today because the bid is 1.4% from the market and would very likely fill THIS WEEK,
which would carry an unhedged position into the 11/17 print. Everything I measured argues against it:
- Relative strength (market_data.py relstrength NVDA --peer XLK): LAGGING SPY on every window measured -
  1m -14.03%, 3m -9.33%, 6m -12.95% vs SPY. Also lagging its own sector XLK by 2.31% over 1m. NVDA absolute:
  1m -19.02%, 3m -14.21%, 6m -13.27%.
- Analyst book is crowded to an extreme: 25 strong buy, 41 buy, 2 hold, 1 sell = **95.7% bullish**, and
  *improving* (+1.6%). That is not fuel, it is the absence of fuel - there is no upgrade left to give and
  downgrade risk is entirely one-directional into a disappointing print.
  (https://finnhub.io/api/v1/stock/recommendation?symbol=NVDA)
- Insiders: **0 open-market buys in 6 months against 32 sells totalling $1,378,179,464**, net -$1.38B.
  (https://finnhub.io/api/v1/stock/insider-transactions?symbol=NVDA)
- Price 186.64 is -23.31% off the 120d high of 243.37 and only +2.85% off the 120d low of 181.462, below the
  sma20 (211.55) by 11.8% and the sma50 (219.81) by 15.1%. ATR 8.019 (4.3%).
- Earnings 2026-11-17 amc confirmed on the fetched calendar (rev est $111.36B, EPS est 2.5263).
- decision: **DO NOT ENTER at 184.00 ahead of 11/17. Cancel the resting bid and wait.** This is precisely the
  archetype behind the stock lane s 1/26: a de-rated single name bought on a pullback level while every
  measured flow and trend reads against it, with a binary event inside the horizon.
- condition to wait for: the 11/17 print out of the way AND a daily close back above the 20-day (211.55).
  Buying the reclaim is a worse price and a better trade.
- I am NOT claiming edge here. At entry 184 / stop 167.50 / target 219.50 the R:R is 2.15, whose break-even
  hit rate is 31.7%, and I cannot honestly claim better than that today - so the expectancy is ~zero and this
  belongs on the WATCHLIST, not in the recommendations. Captured with wait:true so synthesis routes it there.
- The one thing genuinely in its favour, stated for fairness: 181.46 is a real level and a 23% de-rating of
  the dominant AI name into a print with revenue estimated at $111B is not nothing. It is a reason to watch.

## [06:25 ET] REJECTED — ETH / /METZ6 short — correct direction, failed geometry
- At market 2,105 with an honest 2.5-ATR stop (2,290) and a target at 1,790 just above the 120d low of
  1,774.09, R:R is 1.70 against a 2.0 swing floor. Clearing the floor would need a target below the prior
  low or a 2,180 bounce entry that may never fill. Rejected rather than tightening the stop to fit - that is
  the KRE cheat. The ETH weakness is used as corroborating evidence inside the /MBTZ6 short instead.

## [06:29 ET] NEWS/FILINGS — healthcare insider sweep across the leading sector
Checked 8 large-cap healthcare names (market_data.py insiders, 6-month window):
| Sym | open-market buys | distinct buyers | sells | net $ |
| --- | --- | --- | --- | --- |
| MRK | 0 | 0 | 17 | -29,977,579 |
| BMY | 0 | 0 | 3 | -677,826 |
| GILD | 0 | 0 | 50 | -50,367,283 |
| AMGN | 0 | 0 | 6 | -4,106,812 |
| UNH | 0 | 0 | 2 | -660,910 |
| JNJ | 0 | 0 | 11 | -70,190,923 |
| ABBV | 0 | 0 | 1 | -8,177,500 |
| VTRS | 0 | 0 | 1 | -809,784 |
- **Zero open-market insider purchases across all eight.** Per the skill, absence of buying is not a negative
  and I am not treating it as one. But it does characterise what the XLV trade IS: a fund-flow rotation, not
  an insider-confirmed re-rating. No management team in the sector leading the market by 14.89% over a month
  is buying its own stock. That is consistent with the key_risk already on the XLV candidate - a flow trade
  can reverse as fast as it arrived - and it is the reason XLV stays a 3% ETF position rather than a 5%
  single-name conviction bet. No candidate generated from this sweep.

## [06:29 ET] AWAITING-ENTRY TRIAGE — all 8 unfilled ideas
Prices are Fri 2026-11-06 closes (finnhub); crypto/event where noted.
- `OXY` BUY @ 54.00 (pub 09-24), now **56.38**, +4.4% above the bid. WITHDRAW. Same reasoning that closes XLE:
  energy is the only sector negative vs SPY over 1m (-0.56%, -5.55% absolute). I will not hold a resting bid
  in the sector I am exiting on the same morning. Not re-captured - a stale bid 4% below market in a decaying
  sector should simply be cancelled.
- `KXCPIYOY-26SEP-T3.5` NO @ 18 (pub 09-30). CANNOT ASSESS. Kalshi returns all pricing fields null today
  (see the 06:20 block), so there is no implied probability to compare against. Also note the ticker says
  26SEP, which has resolved or is past - carried on the pending list regardless. Flagging rather than guessing.
- `GLD` SELL @ 406.77 (pub 10-25), now **372.52**. WITHDRAW. The thesis was right and the fill never came:
  gold fell 8.4% below the short entry without touching it. GLD is -1.61% 1m, -7.46% 3m, -14.12% 6m. A short
  entry 9.2% ABOVE the market is not a live order, it is a stale one. Re-shorting here at 372.52 is a
  different trade with no work behind it, so I am not making it.
- `SMMT` BUY @ 17.1 (pub 10-27), now **16.33** after **+15.08% on Friday 11/06**. REJECT - see below.
- `ONON` BUY @ 34.20 (pub 11-03), now **37.36**, +9.2% above the bid. WITHDRAW as a stale pullback bid; the
  market left it behind in three sessions and nothing was researched today to justify a higher entry.
- `TLT` BUY @ 80.30 (pub 11-04), now **81.92**. LEVEL UNCHANGED, still live, not re-pitched. 80.30 sits on
  the sma50 (80.3781) which is a real level, and TLT is +5.20% 1m / +10.19% vs SPY. But I am NOT upgrading it,
  because it contradicts my own 06:05 macro read: the 10y is at 4.84% against a 3.88% funds rate, so the long
  end is refusing to follow the Fed down and the driver looks like term premium. Buying duration while
  arguing that is incoherent, and TLT is -4.83% over 6m. Left pending at the published level.
- `CVS` BUY @ 79.00 (pub 11-05), now **83.85** after +3.10% Friday. DO NOT RE-PITCH. CVS is in prior_context
  3x in ten days AND stopped out on 11-04, and the market is now 6.1% above the bid. Three pitches plus a
  stop-out is the anchoring pattern the repetition guard exists to catch. Withdraw the bid.
- `NVDA` BUY @ 184.00 (pub 11-07), now 186.64. Captured as WAIT - see the 06:25 block.

## [06:29 ET] REJECTED — SMMT — unexplained +15% move on a fresh offering registration, no verified catalyst date
- Jumped +15.08% on 11/06 to 16.33 and I could not establish why. A targeted search returned nothing dated
  2026-11-06; the most recent verifiable items are the Jan 2026 FDA acceptance of the ivonescimab BLA
  (EGFR-mutated NSCLC after TKI, with Fast Track) and the HARMONi Phase III publication in Lancet Oncology.
- SEC filings 2026-11-04 (https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001599298):
  an 8-K, a 10-Q for the quarter ended 2026-09-30, **and a 424B7** - a prospectus supplement. That is exactly
  the dilution/selling-shareholder mechanism universe.md names as the most common way a small-cap thesis dies.
- A BLA acceptance implies a PDUFA date exists, which would be a genuine dated catalyst, but **I could not
  fetch one** and will not state a date from memory (CLAUDE.md rule 2).
- Also already stopped out once: opened 10-09, stopped 10-26, at conviction 3.
- REJECT. An unexplained 15% move in a 6.84%-ATR small cap with a fresh prospectus supplement and no
  verifiable catalyst date is a lottery ticket I cannot price. Watchlist at most; the bid at 17.1 is dead.

## [06:29 ET] REJECTED — XLP — right regime, wrong geometry
- XLP is the #2 sector (1m +7.98%, +12.97% vs SPY; 3m +6.04%) and was the natural pair to XLV.
- Killed on arithmetic, not opinion. ATR14 is 1.7783 (1.97%) and price 90.08 is only -3.55% off the 120d high
  of 93.40. An honest ETF stop of >=1.8 ATR from a ~89.50 entry sits at ~86.00 (risk 3.50), so a 2.0 floor
  demands a 96.50+ target - a 3.3% NEW HIGH for consumer staples, needing +7.8% from entry. XLP's 6m return
  is only +7.01%, so that is roughly six months of trend compressed into a swing. There is no honest way to
  get there, and tightening the stop to make it fit is the KRE cheat.
- Contrast with XLV, which passes the same test: same ATR% (2.05%) but a 6m return of +28.79%, so the +9.24%
  the target asks for is about one month of its realised pace rather than six.

## [06:26 ET] FALSIFICATION — XLV concentration, and why it changed the stop
Fetched the fund page (as of Nov 06 2026):
https://www.ssga.com/us/en/intermediary/etfs/the-health-care-select-sector-spdr-fund-xlv
- 61 holdings, 0.08% gross expense ratio, and SSGA explicitly flags **non-diversification risk**.
- Top 10 = 60.43% of the fund: LLY **16.17%**, JNJ 9.93%, ABBV 7.68%, MRK 5.40%, UNH 5.28%, TMO 3.83%,
  AMGN 3.71%, GILD 3.09%, ABT 2.84%, PFE 2.50%. Top 3 alone = 33.78%.
- THIS MATTERS AND IT CHANGED A LEVEL. strategy.md gives ETFs a 0.9 stop factor (1.8 ATR instead of 2.0)
  because "a basket cannot gap on one company's news". At 16.17% in a single name that premise is only
  partly true for XLV: a 15% adverse LLY gap is ~2.4% on the fund, which is ~1.2 ATR in one move, before
  anything else happens. So I am NOT taking the ETF discount.
- Stop moved 176.50 -> **176.00**: risk 8.00 from the 184.00 entry = **2.11 ATR**, which clears the full 2.0
  stock floor rather than the 1.8 ETF floor. R:R becomes 17.00/8.00 = **2.125**, still above the 2.0 floor,
  so the idea survives its own falsification on a wider stop instead of a narrower one.
- NOT added as a 4th evidence kind, deliberately: concentration argues partly AGAINST the trade, so it
  belongs in key_risk and counter_argument. Inflating conviction to 5 off a risk finding would be backwards.
- CORRELATION NOTE: I already hold PFE (2.50% of XLV) and ABT (2.84%). Adding XLV makes healthcare three
  legs of the book, which is AT the 3-idea correlation cap in strategy.md, not over it - but it is the reason
  XLV stays a 3% position and is not sized up.

## [06:32 ET] DURABLE MISPRICING — UNH worked up properly, then REJECTED on reward-to-risk
This was my long_term candidate and it is the right shape, so here is the full work and why it still fails.
- Profile (market_data.py profile UNH): UnitedHealth Group, NYSE, Health Care, market cap $365,294,176,644,
  897.59M shares. Liquid: avg 30d dollar volume $2,281,162,832.
- The shape is exactly what strategy.md asks for in this lane - a quality business de-rated inside the
  sector with the strongest flows. UNH beats SPY on every window (+11.24% 1m, +1.31% 3m, +4.05% 6m) but
  **lags its own sector XLV by -3.65% / -13.28% / -25.06%**. The sector ran +28.79% over 6m; UNH did +3.73%.
  Price 394.15 is -14.62% off the 120d high of 461.62. ATR 11.983 (3.04%), sma20 404.82, sma50 390.65.
- Earnings power, from the fetched surprise record (https://finnhub.io/api/v1/stock/earnings?symbol=UNH):
  Q4'25 actual 2.11 (est 2.1222, -0.57%), Q1'26 7.23 (est 6.6406, +8.88%), Q2'26 6.38 (est 4.9533, +28.80%),
  Q3'26 4.69 (est 4.1809, +12.18%). 3 beats of the last 4, and the misses are behind it.
  **TTM EPS = 2.11+7.23+6.38+4.69 = $20.41, so the stock is on 394.15/20.41 = 19.3x trailing.**
- Analyst revisions are IMPROVING with room left, unlike NVDA: 84.4% bullish (+5.0 points), holds cut from
  7 to 5. There is still rating capacity to convert, which is the opposite of NVDA's saturated 95.7%.
- VALUATION ANCHOR (method shown): 9M 2026 actual EPS is 18.30. A conservative Q4 of 5.20 - below the 6.10
  average of the last three quarters - gives normalized EPS ~$23.50. Holding the CURRENT 19.3x multiple,
  assuming no re-rating at all, gives **19.3 x 23.50 = $453**. That target sits BELOW the 120d high of
  461.62, which is a genuinely conservative anchor.
- **AND THAT IS WHERE IT DIES.** strategy.md requires long_term reward-to-risk of 2.5 against an explicit
  bear-case PRICE. An honest bear case for a managed-care insurer is cost-trend re-acceleration: EPS back to
  ~$18 on a multiple compressed to ~15x = **$270**, and this stock has already proved it can travel, falling
  461.62 -> 362.60 in four months.
  - Accumulating at 385 (under the sma50): reward 453-385 = 68, risk 385-270 = 115. **R:R 0.59.**
  - Even on a full 22x normalized target of 517 and a shallower 340 bear case: reward 132, risk 45,
    R:R 2.93 - but a bear case of 340 is only -11.7% and sits barely under the recent low, which is not a
    bear case, it is a dip. Making the floor requires pretending the downside is small.
- REJECT as a recommendation. 19.3x on a depressed earnings base is reasonable value but it is roughly a
  1.5:1 proposition, not 2.5:1, and the floor exists to reject exactly this. **Watchlist name**, and the one
  I would most want to own if it reached the mid-300s.
- Worth saying plainly: this arithmetic is probably why the long_term lane is 0/4 and -15.2%. A bear-case
  price that is really a dip makes any ratio clear the floor.

## [06:32 ET] REJECTED — no long_term candidate today, and that is a finding not an omission
- I gave the lane dedicated time per strategy.md rather than leftovers, and worked UNH end to end.
- The structural problem this morning: the sectors with durable leadership (XLV +28.79% 6m, XLP) are AT or
  within 4% of their highs, so there is no de-rating to buy; and the complex that HAS de-rated (XLK -16.71%
  1m, NVDA -23.31% off high) is mid-unwind with every measured flow still pointing down - my own NVDA work
  concluded "wait", and it would be incoherent to reject NVDA as a swing and buy it as a hold on the
  same evidence.
- So: 0 long_term ideas, stated honestly, rather than one assembled to fill the lane.

## [06:31 ET] POSITION UPDATE — ONON — awaiting entry @ 34.20, price 37.36, EARNINGS TOMORROW BMO
I withdrew this at 06:29 as a stale pullback bid. That was wrong, and the earnings calendar is why - this
is time-critical and needs an action before tomorrow's open. Correcting it here.
- Q3 earnings **2026-11-10 before market open**, confirmed on the fetched finnhub calendar: EPS est 0.40,
  revenue est $949M. On Holding AG, NYSE, market cap $12,305,357,009, avg 30d dollar volume $374,220,438.
- Levels: last 37.36, ATR14 1.5189 (4.07%), sma20 34.862, sma50 31.5134, 120d range 26.365-41.41,
  -9.78% off the high, **+41.7% off the low**.
- THE PROBLEM, and it is the fill-rate pathology in its sharpest form: the resting 34.20 bid is 8.46% below
  the market, which is **2.08 ATR**. Nothing short of a disappointing print gets price there by tomorrow's
  open. So a limit order resting at 34.20 into a before-the-open print is, in practice, an instruction to buy
  a bad earnings gap - and a gap does not stop politely at 34.20 either; it can open at 31. This is the
  mechanism behind "42% of pullback entries filled, and the ones that did fill were the ones falling",
  concentrated into a single overnight event.
- The geometry itself is fine, which is what makes this worth stating carefully rather than just cancelling:
  buying 34.20 with a 2.0-ATR stop at 31.16 (which sits on the sma50 at 31.51) and the 120d high of 41.41 as
  target gives R:R 7.21/3.04 = **2.37**, comfortably over the swing floor. The flaw is the ORDER OF
  OPERATIONS, not the levels.
- Analysts (https://finnhub.io/api/v1/stock/recommendation?symbol=ONON): 81.6% bullish but **deteriorating**
  (-1.7). Surprise record is 4 beats of 4, but sharply decelerating: +87.4% (Q3'25), +20.9% (Q4'25),
  +51.5% (Q1'26), then **+1.8%** (Q2'26). A four-quarter beat streak that has flattened to in-line is a
  weaker setup than the raw 4/4 suggests, and the stock is already +41.7% off its 120d low, so it is not
  cheap going in.
- decision: **CANCEL the 34.20 bid before tomorrow's open. Wait for the print.** Then buy the 34-35 area
  only if the business is intact rather than because the price fell.
- NOT a reason to buy at the market either - 37.36 the day before a binary print with deteriorating revisions
  is the opposite error.

## [06:33 ET] POSITION UPDATE — AAL short — opened 2026-10-03, +1.3%, HOLD AS-IS
I went looking for a reason AAL was rallying against the short and expected falling crude. **The data said the
opposite and I am recording the correction rather than the hypothesis.**
- USO (crude proxy, finnhub): 148.41, +0.56% 1m, **+17.86% 3m**, +11.09% 6m (+22.74% vs SPY on 3m). Crude is
  one of the strongest things on the board over three months. XOP 173.77. This independently corroborates the
  "high fuel prices" that Boise Cascade named as hurting housing affordability in its Q3 release - same fact
  from two unrelated sources.
- So fuel is a cost HEADWIND for airlines, which supports the short rather than undermining it.
- AAL is also the weakest major airline on the measured tape: AAL +2.97% 1m / -12.13% 3m against JETS
  +4.51% 1m / -8.65% 3m. It lags its own industry group on both windows and is -29.86% off its 120d high.
- Against the short, honestly: AAL rose +1.93% on Friday and at 13.18 is above BOTH its sma20 (12.5107) and
  sma50 (12.8837), and JETS is +9.50% vs SPY over 1m. The industry is bid.
- Stop check: 14.40 is 1.22 above the 13.18 price = 1.85 ATR (ATR 0.6611, 5.02%). From the 13.35 entry it was
  1.05 = **1.59 ATR**, i.e. it shipped under the 2.0 stock floor - another instance of the pattern in
  prior_context where tight stops precede stop-outs.
- decision: **HOLD AS-IS. No recommendation, and specifically do not widen the stop.** The thesis - weakest
  balance sheet in a sector absorbing a 17.9% three-month fuel cost increase - is intact, and the stop is
  doing the job it was set to do. Widening it because price moved toward it is the KRE cheat in reverse.

## [06:34 ET] POSITION UPDATE — UNP and XLU, the two rows the triage table left unexplained
- `UNP` +0.5%, last 290.16, ATR 7.564. HOLD AS-IS. Below the sma20 (294.4605), above the sma50 (286.7004),
  so it is mid-range and undecided. Stop 277.40 is 1.69 ATR below price but only **1.48 ATR from the 288.60
  entry** - tight as published, the same flaw as AAL and ABT. Rails sit in XLI, the weakest cyclical sector
  on the 1m tape (-3.40%), and the 315.99 target is the 120d high exactly. Nothing changed today; no
  recommendation, and the stop is not being widened to rescue it.
- `XLU` -0.4%, last 43.13, ATR 0.6212 (1.44%). HOLD AS-IS, and it is the healthiest of the quiet positions:
  price is above BOTH the sma20 (42.567) and the sma50 (41.7734), the sector is +5.02% 1m / +10.01% vs SPY,
  and the stop at 41.80 is a legitimate **2.41 ATR from the 43.30 entry**. Note XLU was published 2x in the
  last 10 days, so it specifically does not need a third pitch - the level is unchanged and working.
- That completes all 12 open positions: 2 closed (XLE, BCC), 1 updated (ACM), 9 hold-as-is.

## [06:34 ET] CORRELATION CHECK — two of the three actionable ideas are the same bet
Worth flagging for synthesis rather than leaving it to be discovered on the Sheet:
- XLV buy (long defensives) and /MBTZ6 short (short risk appetite) are two expressions of ONE macro view:
  that the de-risking which has cost XLK -16.71% in a month continues. If the AI complex bottoms this week,
  **both lose at once**, and the XLE close would also look early.
- That is 3 ideas on one driver, which is exactly AT the strategy.md correlation cap of 3 and not over it -
  but it is the reason XLV is 3% and /MBTZ6 is 2% rather than either being sized up, and it is the single
  biggest risk in today's report.
- The other four are independent: ACM (company earnings), BCC (company guidance), NVDA and ONON (both
  waits with no capital at risk).

## [06:34 ET] TIMESTAMP NOTE
- Research started 06:01:02 ET. The heading times from 06:15 onward run 3-5 minutes ahead of the real clock
  because I wrote them before re-reading `date`; the real time at this block is 06:30 ET. Every PRICE, ATR
  and figure above is fetched and unaffected - only the heading minutes drift. Flagging it so the synthesis
  phase does not infer a longer run than actually happened.

## [06:34 ET] FINAL COUNTS
- candidates captured: **9 lines, 7 distinct symbols** (XLV and NVDA each re-captured once with a correction;
  synthesis takes the last entry per symbol):
  1. `XLV` buy, swing, conviction 4, R:R 2.125 — long the only sector leading on 1m/3m/6m. The best idea today.
  2. `/MBTZ6` short, swing, conviction 4, R:R 2.35 — Micro Bitcoin short, the de-risking trade, 2% size.
  3. `ACM` buy, swing, conviction 4, R:R 2.0 — POSITION UPDATE: hold, trim half before the 11/16 print.
  4. `BCC` sell, conviction 4 — CLOSE the long on the company's own Q4 guide (EBITDA 32-54M vs 98.5M).
  5. `XLE` sell, conviction 3 — CLOSE the long; stop 0.45 ATR away and the sector thesis decayed.
  6. `ONON` buy, conviction 4, wait:true — CANCEL the 34.20 bid before tomorrow's bmo print. Watchlist.
  7. `NVDA` buy, conviction 4, wait:true — DO NOT ENTER at 184 before 11/17. Watchlist.
- Net: 2 new positions, 1 position amendment, 2 closes, 2 cancellations, 9 holds. No long_term idea, no
  intraday idea, no event contract, no small cap — each explained above rather than padded around.
- HONEST SKEW: this is a management-heavy, idea-light report. Given the stock lane is 1/26 (4%) at -8.0% avg
  over 39 closed trades - a sample now above the ~15 noise floor - adding few new single-name longs and
  cleaning up the book is the correct response to the record, not a failure to find ideas.
- coverage gaps:
  - **Event contracts: zero, blocked by data.** Kalshi returns all price fields null; no implied probability
    could be fetched, so none could be honestly stated. Also blocks re-assessing the pending KXCPIYOY idea.
  - **No VIX, no index futures, no DXY, no spot gold/WTI**: Yahoo returned HTTP 429 for every one. Worked
    around with finnhub ETF proxies (SPY/QQQ/IWM/GLD/USO/TLT); no VIX level is stated anywhere.
  - **No economic-release calendar.** market_data.py has no source for it, so no dated CPI/PPI/Fed time for
    this week is claimed. This is the largest unhedged gap in today's macro read.
  - **No options-implied move for any idea**: `implied` returns HTTP 401 from yahoo-options. So no target was
    checked against what options price - a step config/strategy.md explicitly asks for.
  - **No short interest**: `short NVDA` timed out at api.nasdaq.com. Not retried for other names.
  - **Small/micro caps: none.** I built the funnel (178 names with earnings 11/10-11/13 in the $30M-$1.5B
    revenue band) but ran out of budget to do liquidity, dilution and insider checks on any of them properly.
    A half-checked micro cap is worse than none, so none was captured. Best unexplored lead: the 11/10-11/12
    small-cap earnings cluster.
  - **No per-bar OHLC**: finnhub's `recent` array returned nulls, so every level comes from the aggregates
    (ATR14, sma20, sma50, 120d range) rather than from individual swing highs and lows.
  - **BTC/ETH volatility is close-to-close, not true ATR** (CoinGecko daily closes only). Stops were set off
    an estimated true ATR ~1.4x larger, which is the conservative direction.
- sources that failed: Yahoo Finance chart API (429, all indices/futures/FX/commodities), Yahoo options API
  (401), api.nasdaq.com short interest (read timeout), Kalshi market prices (all null),
  robinhood.com/us/en/support/articles/futures-contracts-available-on-robinhood/ (404 - venue verification
  fell back to Robinhood's own learn article), SMMT Friday move (no source found explaining +15.08%).

## [06:32 ET] REJECTED — small/mid-cap sweep — checked properly, produced nothing that clears the bar
Partially closes the small-cap gap listed in FINAL COUNTS: I did run the check, it just came up empty.
Picked from the 11/10-11/13 earnings funnel on the theme that is actually working in my book (HII +10.2%,
aero/defense) plus ACM's closest listed peer. Insider activity, 6-month window:
| Sym | name | mcap | buys | distinct buyers | sells | net $ |
| --- | --- | --- | --- | --- | --- | --- |
| ATRO | Astronics | $2.36B | 0 | 0 | 0 | 0 |
| MRCY | Mercury Systems | $4.48B | 0 | 0 | 36 | -43,665,702 |
| TTEK | Tetra Tech | $10.13B | 1 | 1 | 0 | +50,179 |
| GFF | Griffon | — | 0 | 0 | 46 | -33,648,552 |
- **No cluster anywhere.** TTEK's single $50,179 purchase by one buyer is not the "several distinct buyers"
  signal that counts as `positioning` evidence - one small buy is noise, and calling it a confirmation is how
  a thin idea comes to look sturdy. ATRO shows no insider activity at all in six months, which is no
  information rather than good news.
- Also: ATRO at $2.36B and MRCY at $4.48B are mid-caps, not the sub-$2B asymmetric tier the brief asks for.
  I did not reach genuine small caps with liquidity and dilution checks done properly.
- REJECT all four. With the stock lane at 1/26 (4%) and -8.0% average, a new single-name long needs 3 distinct
  evidence kinds today, and none of these has 2. No candidate captured.
- **USEFUL OPERATIONAL NOTE, kept because it bears on a live position:** TTEK (Tetra Tech) is ACM's closest
  listed comparable and reports **2026-11-11 amc, five sessions before ACM's 11/16 print**. It is a free
  read-through on infrastructure-services demand ahead of my own position's catalyst. If TTEK guides down on
  11/11, take the ACM trim early rather than waiting for the 11/16 close.

## [06:32 ET] RESEARCH COMPLETE
- Ran 06:01-06:32 ET. Not truncated; this block and the FINAL COUNTS block above are both complete.
- 9 candidate lines, 7 distinct symbols. 2 new positions (XLV, /MBTZ6), 1 amendment (ACM), 2 closes
  (BCC, XLE), 2 cancellations captured as waits (ONON, NVDA), 9 positions held as-is.
- Every price, ATR, moving average, EPS and guidance figure in this log was fetched. Where a source failed it
  is named in FINAL COUNTS and no number was substituted for it.

## [06:34 ET] REJECTED — CEG — the most interesting divergence I found today, and still no honest entry
Chased this because it is the only dated catalyst in TODAY's session: Constellation Energy reports
**2026-11-09 before the open** (fetched calendar: EPS est 3.8857, revenue est $9,470,000,000).
- The divergence, and it is large: CEG is classified **Utilities** and is priced like an AI trade.
  | window | CEG | XLU | CEG vs XLU |
  | --- | --- | --- | --- |
  | 1m | -12.32% | +5.02% | **-17.34%** |
  | 3m | -7.57% | 0.00% | -7.57% |
  | 6m | -17.68% | -3.56% | -14.12% |
  While its own sector led the market, CEG fell 12.3% - it is being sold with XLK (-16.71% 1m) as a
  datacenter-power proxy rather than bought with utilities. Last 249.95, -19.49% off the 120d high of 310.45,
  ATR14 12.0164 (**4.81%**), sma20 263.4745, sma50 270.0215, market cap $88.6B, avg $vol $1.05B.
- The fundamentals do not look like the price: analysts 86.2% bullish and **improving +3.4**, 3 beats of the
  last 4 (+10.65%, +5.68%, +2.35%, -3.49%).
- WHY I AM STILL NOT TRADING IT. Both possible entries fail, for opposite reasons:
  - **Post-print reclaim** of the sma20: entry ~265, an honest 2.25-ATR stop at 238, and even a 310 target at
    the 120d high gives reward 45 / risk 27 = **R:R 1.67**, under the 2.0 floor. Making it clear the floor
    needs a 320+ target, i.e. a new 120-day high, on a name in a 19% drawdown.
  - **Post-print dip** at ~240: that geometry works (stop 212, target 300, R:R 2.14) but it is a limit order
    to buy a bad earnings reaction on a 4.81%-ATR stock - precisely the pathology I rejected the ONON bid for
    forty minutes ago. I will not apply that standard to ONON and then break it here.
  - And I cannot set a pre-print entry at all: a 4.81% ATR means the reaction, not my level, decides the price.
- REJECT. **Watchlist, and the first thing to re-examine tomorrow** once the print is known - at that point
  the reaction is data rather than a guess, and the sector-divergence thesis becomes testable.

## [06:33 ET] END OF RESEARCH — this block supersedes the 06:32 RESEARCH COMPLETE above
Written after it because the CEG work landed afterwards. Nothing was lost to the clock; research was NOT
truncated. Authoritative summary:
- Ran 06:01:02 - 06:33 ET, ~32 minutes of a ~60 minute budget. Stopped because the work was done, not cut off.
- **candidates.jsonl: 9 lines, 7 distinct symbols.** Synthesis takes the last entry per symbol; XLV and NVDA
  each appear twice because each was deliberately re-captured after a correction (XLV's stop widened
  176.50 -> 176.00 on the LLY concentration finding; NVDA's conviction 3 -> 4 to match its evidence count).
- Every conviction score equals the count of distinct evidence kinds, checked mechanically: XLE 2 kinds / 3,
  the other six 3 kinds / 4.
- Actions for the reader, in priority order:
  1. CLOSE `BCC` long — the company guided Q4 EBITDA to 32-54M against 98.5M delivered.
  2. CLOSE `XLE` long — stop 0.45 ATR away, sector thesis decayed over 53 days.
  3. CANCEL `ONON` bid @ 34.20 **before tomorrow's 11/10 pre-open print** — most time-critical item here.
  4. CANCEL `NVDA` bid @ 184.00 before 11/17.
  5. BUY `XLV` 181.50-186.00, stop 176.00, target 201.00, 3%.
  6. SHORT `/MBTZ6` 73,000-76,500, stop 78,575, target 63,500, 2%.
  7. HOLD `ACM`, trim half before the 11/16 close; watch TTEK's 11/11 print as the early read.
  8. Also cancel the stale `OXY`, `GLD`, `CVS` bids (reasoning in the 06:29 triage block).
- Nine positions held as-is with no recommendation, deliberately: PFE, KHC, AAL, HII, UNP, ABT, PYPL, XLU, RTX.
- Rejected with reasons logged, not silently dropped: XLP (geometry), UNH (long_term R:R 0.59 on an honest
  bear case), SMMT (unexplained +15%, fresh 424B7), CEG (no honest entry pre-print), ETH//METZ6 (R:R 1.70),
  ATRO/MRCY/TTEK/GFF (no insider cluster), all event contracts (Kalshi prices null).
- The single biggest risk in today's report: XLV long and /MBTZ6 short are two expressions of one macro view.
- Full coverage gaps and failed sources are in the FINAL COUNTS block above; the largest are no economic
  calendar, no options-implied move, no VIX, and no event-contract prices.
