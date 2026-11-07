# Research log — 2026-11-07

## [06:05 ET] SETUP — Saturday run
- 2026-11-07 is a **Saturday**. US equities and futures closed. Freshest honest
  equity price is Friday 2026-11-06 close (session: closed, age ~842 min).
  Crypto and event contracts are the only same-day-actionable lanes.
- Equity ideas today are week-ahead prep: entries for the Monday 2026-11-09 open
  or later, marked `swing`.

## [06:05 ET] DATA QUALITY — Yahoo is rate-limited this run
- `market_data.py macro`: every Yahoo-backed field FAILED with HTTP 429
  (query1 and query2). That kills spx/ndx/dow/rut/vix/DXY/us10y price/gold/WTI
  and the ES+NQ futures quotes for this run.
- Working: finnhub for equities/ETFs (`quote`), nasdaq for OHLCV (`history`),
  CoinGecko for crypto, FRED for rates. bonds_20y came through.
- Consequence: **no VIX reading, no live futures quote, no DXY** today. Index
  regime has to be read off SPY/QQQ/IWM ETF closes instead. Logged for
  data_quality_notes.

## [06:06 ET] MACRO — rates (FRED, fetched)
- US 10y 4.84% (2026-11-05); US 2y 4.46% (2026-11-05); fed funds 3.88%
  (2026-11-05); 10y-2y curve +0.35 (2026-11-06)
  — source: https://fred.stlouisfed.org/series/DGS10
- Unemployment 4.1% (2026-10-01); CPI index 336.298 (2026-09-01)
  — source: https://fred.stlouisfed.org/series/UNRATE
- Read: 10y at 4.84% sits ~96bp **above** fed funds with a +35bp 2s10s. That is
  a term-premium / long-end problem, not a growth-expectations one. Long
  duration (TLT) is the thing being repriced.

## [06:06 ET] MACRO — equity regime (Friday 2026-11-06 closes, finnhub)
- SPY 735.29 +0.31% (prev 733.00); QQQ 656.10 +1.40% (prev 647.05);
  IWM 273.67 +0.99% (prev 270.98)
- SPY context from 30d OHLCV (nasdaq): SMA20 763.36, range high 781.62,
  range low 732.71, **-5.93% off the high**, ATR14 11.12 (1.51%).
- Read: **SPY is in a ~6% correction and trades 3.7% below its own 20-day MA.**
  Friday was a bounce off the low of the range, led by Nasdaq, not a breakout.
- This is the single most important frame for today, because of the next entry.

## [06:07 ET] TRACK RECORD — the sample is no longer noise, and it is bad
- 39 closed of 63 tracked: **4/39 hit target (10%), avg -5.9%**.
- stock 1/26 (4%), avg -8.0%. etf 3/13 (23%), avg -1.6%. conviction 4 best
  (2/8, -0.8%); conviction 2 worst (0/6, -8.4%). long_term 0/4, avg -15.2%.
- n=39 is past the ~15-trade noise threshold, so this is signal: the report has
  been **systematically buying pullbacks in long equity while SPY corrected**,
  and 10 of the first 11 open positions are long.
- Of the 11 open positions, 10 are BUY and 1 is SELL_SHORT. That is a
  directional book, not a portfolio.
- **Bar for today:** a new long equity swing idea must carry something the
  losing cohort did not — a dated catalyst inside the horizon, or evidence
  beyond "it is cheap and near support". Pullback-entry longs into a 6%
  correction are exactly the losing pattern. Prefer ETFs (the only class with a
  positive-ish record), crypto, and event contracts.

## [06:07 ET] MACRO — crypto (CoinGecko, fetched 06:04 ET)
- BTC $75,923 (-0.06% 24h), vol24h $22.4B, mcap $1.527T
- ETH $2,244.60 (+0.50% 24h), vol24h $7.9B
- SOL $89.91 (0.00% 24h), vol24h $1.7B
- Read: crypto is in a deep drawdown, not a dip. BTC $75.9k against a
  2025 cycle high well above $100k. Needs history before any level is set.

## [06:09 ET] CALENDAR — dated earnings, next 10 sessions (finnhub, fetched)
Source: https://finnhub.io/api/v1/calendar/earnings (via market_data.py earnings --days 12)
- Mon 2026-11-09 bmo: **CEG** $9.5B rev est, EPS 3.89; FERG; CNH
- Tue 2026-11-10 amc: **CRWV** (CoreWeave) EPS est -1.18; bmo SE, TDG
- Wed 2026-11-11: NIO
- Thu 2026-11-12 amc: **CSCO** ($18.5B), **AMAT** ($10.5B, EPS 4.13)
- Mon 2026-11-16 bmo: PDD, BIDU; TSN amc
- Tue 2026-11-17 amc: **NVDA** ($111.4B rev est, EPS 2.53); bmo **DIS**, **HD**
- Wed 2026-11-18: **TGT**, **LOW**, **TJX**, **ROST**, **PANW**
- Thu 2026-11-19: **WMT** ($189.2B), NTES, INTU
- Read: the week ahead has two hinges — **AMAT Thu Nov 12 amc** (semicap, the
  read-through on AI capex orders) and **NVDA Tue Nov 17 amc**, which is the
  event that settles the AI-capex question for the whole tape. Retail
  (HD/TGT/LOW/TJX/WMT) lands Nov 17-19 and is the consumer read.
- Consequence for today: anything long-semis or long-index into Nov 17 is one
  bet on NVDA, and the correlation cap (max 3 per driver) binds hard.

## [06:10 ET] DATA QUALITY — event contracts unavailable this run (hard gap)
- `market_data.py events "<topic>"` returns count 0 for Fed, CPI, Bitcoin. Cause
  found: the helper fetches the *first 200 open markets unordered* and filters
  client-side; Kalshi returns ~200 sports parlays (KXMVECROSSCATEGORY), so no
  macro series is ever in the window. Not a market fact — a query defect.
- Queried the API directly by `series_ticker` instead. The series are all live:
  KXCPIYOY, KXFED, KXFEDDECISION, KXU3, KXBTC, KXBTCD, KXGDP, KXRECSSNBER.
- **But every market returns `yes_bid`, `yes_ask`, `last_price`, `volume`,
  `open_interest` and `liquidity` as null**, on both the list and the
  single-market endpoint (checked KXRECSSNBER-27, KXCPIYOY-26DEC-T3.0,
  KXU3-26NOV-T4.3). No implied probability is obtainable without auth.
- **Consequence: zero event-contract candidates today.** The universe rule
  requires stating the market's implied probability against mine, and I will not
  state a price I could not fetch. This is a tooling gap, not "nothing was
  mispriced" — flagged for data_quality_notes.
- Side benefit: a Kalshi parlay leg quoted "Target Price: $75,894.06" for BTC,
  which independently corroborates the CoinGecko BTC print of $75,923.

## [06:11 ET] POSITION REVIEW — pulling live levels for all 11 open positions
All prices = Friday 2026-11-06 close (finnhub), ATR14/SMA from 120 bars (nasdaq).
Source: https://finnhub.io/api/v1/quote , https://api.nasdaq.com (via market_data.py)

**Friday's tape inside the book is the headline finding.** SPY +0.31% and
QQQ +1.40%, but of the 11 open positions 8 fell: BCC -4.76%, ABT -3.23%,
KHC -2.80%, UNP -2.61%, PFE -1.64%, RTX -1.22%, XLU -0.39%, XLE -0.02%; only
AAL (+1.93%, a short, so against us) and PYPL (+0.47%) rose. Friday was a
narrow tech-led bounce and this book is long the exact factor that was sold.
That is the mechanism behind the -5.9% average, not bad luck on 39 names.

| Sym | Close | Entry | Stop | Tgt | ATR14 | ATR% | SMA20 | SMA50 | Stop dist (ATR, from close) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLE | 61.62 | 63.9 | 60.8 | 70.5 | 1.84 | 2.98 | 67.11 | 65.07 | **0.45** |
| RTX | 189.53 | 199.0 | 186.0 | 226.5 | 6.04 | 3.19 | 193.67 | 193.45 | **0.58** |
| BCC | 70.24 | 76.5 | none | 110.0 | 3.51 | 5.00 | 75.53 | 75.80 | n/a |
| KHC | 24.61 | 23.0 | 21.2 | 28.09 | 0.77 | 3.14 | 24.03 | 24.01 | 4.42 |
| AAL | 13.18 | 13.35 | 14.40 | 10.6 | 0.66 | 5.02 | 12.51 | 12.88 | 1.85 (short) |
| HII | 288.74 | 262.0 | none | 339.76 | 12.25 | 4.24 | 284.09 | 278.73 | n/a |
| UNP | 290.16 | 288.6 | 277.4 | 315.99 | 7.56 | 2.61 | 294.46 | 286.70 | 1.69 |
| ABT | 109.93 | 103.0 | 97.0 | 117.34 | 3.71 | 3.38 | 105.51 | 104.01 | 3.49 |
| PYPL | 59.24 | 56.5 | 54.1 | 62.7 | 1.64 | 2.76 | 57.23 | 55.10 | 3.14 |
| XLU | 43.13 | 43.3 | 41.8 | 46.6 | 0.62 | 1.44 | 42.57 | 41.77 | 2.14 |
| PFE | 29.39 | 27.6 | none | 42.0 | 0.80 | 2.74 | 29.75 | 28.74 | n/a |

## [06:14 ET] POSITION UPDATE — XLE — opened 2026-08-15, 51 days, -3.6%
- decision: **close early**, do not wait for the stop.
- why: three things, none of which is "the price fell". (1) The stop at 60.80 is
  **0.45 ATR** below Friday's 61.62 — less than half an ordinary day's range, so
  it is no longer a thesis test, it will be taken out by noise. (2) Price is
  below both SMA20 (67.11) and SMA50 (65.07) and -12.2% off the 120-day high;
  the energy trade has not worked for 51 days. (3) The published stop was
  1.69 ATR from entry (3.10 / 1.84) against the **1.8 ATR ETF floor** — it never
  cleared the floor, so this position was mis-risked from the start and the
  right correction is to exit, not to widen it now.
- target 70.5 is +14.4% and sits above both MAs and near the range high — not
  reachable inside this horizon on current trend.
- XLE appears 2x in the last 10 days' recommendations. Re-pitching it long would
  be the anchoring failure prior_context warns about. Closing instead.
- action: captured via add_candidate.py as an exit.

## [06:15 ET] POSITION UPDATE — RTX — opened 2026-11-02, 2 days, -4.8%
- decision: **hold, stop unchanged at 186.00.** Explicitly declining to widen.
- why: the stop was set 2.15 ATR from entry (13.00 / 6.04), which cleared the
  2.0 ATR stock floor honestly at publication. Price has since gone against it
  and the stop now sits 0.58 ATR from the close. Moving it down to buy room
  would be rewriting risk after the fact — the precise abuse CLAUDE.md records
  (KRE walked 2.19:1 to 4.07:1), just in the opposite direction. If 186 breaks,
  the thesis is wrong and the trade should end.
- context: price below SMA20 193.67 and SMA50 193.45, -16.5% off the 120d high.
  Defense has been a poor lane here — ITA stopped out 2026-10-23 at conviction
  4 — though HII (+10.2%) is the counter-example, so this is name-specific risk
  rather than a sector verdict.
- no amendment, so no candidate emitted. Noted for the record.

## [06:16 ET] POSITION UPDATE — KHC — opened 2026-09-20, 37 days, +7.0%
- decision: **hold, raise stop 21.20 -> 22.90.**
- why: price 24.61 is above SMA20 24.03 and SMA50 24.01, the first time both
  have been reclaimed in this position. The old stop was 4.42 ATR below the
  close, which risks 3.41 of open profit to protect nothing. 22.90 sits 2.22 ATR
  below the close (1.71 / 0.77), so it still clears the 2.0 ATR floor, and it is
  below the 23.00 entry so the position cannot turn into a loss on a stop-out.
- target 28.09 unchanged; it is the exact 120-day high, +14.1% away.
- action: captured via add_candidate.py as an update with the revised stop.

## [06:17 ET] POSITION UPDATE — ABT — opened 2026-10-16, 17 days, +6.7%
- decision: **hold, raise stop 97.00 -> 102.40.**
- why: 97.00 is 3.49 ATR below the close and gives back the entire gain plus
  6% more. 102.40 is 2.03 ATR below (7.53 / 3.71) — still clears the floor —
  and sits just below the 103.00 entry, so the worst case is roughly flat.
  Price holds above SMA20 105.51 and SMA50 104.01 despite Friday's -3.23%.
- caution worth stating: target 117.34 is +6.7% and *is* the 120-day high, so
  the remaining reward here is thin relative to the risk still on the table.
  Raising the stop is what keeps the ratio honest rather than lifting the target.
- action: captured via add_candidate.py as an update with the revised stop.

## [06:18 ET] POSITION UPDATE — PYPL — opened 2026-10-21, 11 days, +4.8%
- decision: **hold, raise stop 54.10 -> 55.90.**
- why: the healthiest chart in the book — 59.24 above SMA20 57.23 and SMA50
  55.10, only -5.6% off the 120-day high, and up on a day the rest of the book
  fell. Old stop 3.14 ATR below the close; 55.90 is 2.04 ATR below
  (3.34 / 1.64), clearing the floor while cutting the worst case to -1.1% from
  entry.
- target 62.70 = the 120-day high exactly, +5.8% away. Unchanged.
- action: captured via add_candidate.py as an update with the revised stop.

## [06:19 ET] POSITION UPDATE — HII — opened 2026-10-12, 24 days, +10.2%
- decision: **hold, add a stop at 264.00** (position currently has none).
- why: the best open gain in the book with no downside defined at all. Price
  288.74 holds above SMA20 284.09 and SMA50 278.73. 264.00 is 2.02 ATR below
  the close (24.74 / 12.25) and just above the 262.00 entry, so it converts an
  undefended +10.2% into a position that cannot lose. Adding a stop to a
  profitable position is an exit amendment, which is permitted; the entry is
  untouched.
- target 339.76 (+17.7%) is above the 120-day high 334.53. Left unchanged
  rather than trimmed toward the current price — the ratio must not be improved
  by moving the target either.
- action: captured via add_candidate.py as an update.

## [06:20 ET] POSITION UPDATE — UNP — opened 2026-10-15, 22 days, +0.5%
- decision: **hold, no change.** Nothing new to act on.
- why: 290.16 sits between SMA50 286.70 (above) and SMA20 294.46 (below) after
  Friday's -2.61%. Stop 277.4 is 1.69 ATR below the close and 1.48 ATR from
  entry — tighter than I would publish today, but it is a *live* stop on a
  position near breakeven and widening it would be the RTX error.
- no amendment, no candidate.

## [06:20 ET] POSITION UPDATE — XLU — opened 2026-11-02, 4 days, -0.4%
- decision: **hold, no change.**
- why: 4 days old, flat, above SMA20 42.57 and SMA50 41.77. Stop 41.80 is
  2.14 ATR below the close and 2.42 ATR from entry — correctly set. R:R from
  entry 2.20:1. Lowest ATR% in the book (1.44%). Nothing has changed.
- XLU appears 2x in the last 10 days; holding is not re-pitching. No candidate.

## [06:21 ET] POSITION UPDATE — PFE — opened 2026-08-18, 52 days, +6.5%
- decision: **hold, no change.** Deliberately not re-pitched.
- why: long_term, target 42.00 is a valuation anchor +42.9% away, well above the
  120-day high 31.44. Price 29.39 just under SMA20 29.75, above SMA50 28.74 —
  the thesis is intact and unfinished, which is the legitimate reason a
  long_term idea persists. But PFE has been recommended **3x in the last 10
  days**, the single most repeated name in the book, so emitting it again today
  would be anchoring dressed as conviction. Holding silently is the correct
  action.
- no candidate. Flagging the repetition rather than feeding it.

## [06:22 ET] POSITION UPDATE — AAL (short) — opened 2026-10-03, 4 days, +1.3%
- decision: **hold, stop unchanged at 14.40 — but the thesis is deteriorating.**
- why: still marginally in the money (entry 13.35, close 13.18) yet AAL rose
  1.93% on Friday and has now reclaimed **both** SMA20 (12.51) and SMA50
  (12.88), closing at 13.18 above each. A short whose underlying is back above
  both moving averages has lost its technical footing; what is left is the
  -29.9%-off-high downtrend and the 14.40 stop, which is 1.85 ATR above the
  close and therefore still a real test.
- invalidation to watch, stated so it is not re-litigated later: a daily close
  above 13.60 ends this short regardless of the 14.40 stop.
- no level change, so no candidate. Tightening the stop toward 13.60 would
  improve the ratio by shrinking risk — the forbidden move — so the condition
  is recorded as a judgement call, not smuggled in as a level.
TODO-CONSOLIDATION: re-emit XLE candidate, thesis has a typo 'FriComing close' -> 'Friday close'.

## [06:26 ET] POSITION UPDATE — BCC — opened 2026-08-18, 80 days, -8.2%
- decision: **close early.** The clearest-cut call of the review.
- Friday's -4.76% was not the earnings reaction: BCC filed its 10-Q for the
  period ended 2026-09-30 and an 8-K on **2026-11-02**, four sessions earlier.
  So this is continued post-earnings deterioration, not a single-day event.
  — source: https://www.sec.gov/Archives/edgar/data/1328581/000132858126000034/bcc-20260930.htm
  — source: https://www.sec.gov/Archives/edgar/data/1328581/000132858126000033/bcc-20261102.htm
- **Relative strength is what settles it.** BCC vs XHB (homebuilders):
  1m BCC -5.36% against XHB **+6.91%** — lagging its own sector by 12.27 points
  in a month; 3m BCC -17.12% vs XHB -5.50%, lagging by 11.62. vs SPY: -12.24
  over 3m. Verdict string: "lagging SPY on every window measured".
  — source: market_data.py relstrength BCC --peer XHB
- Why that matters: the hold case for BCC was always "housing is cyclical, wait
  for the turn". **Housing is turning and BCC is not participating** — XHB is up
  6.9% in a month while SPY fell 5.0%. That removes the thesis's only support
  and makes this company-specific, not cyclical.
- Confirming: insiders 0 open-market buys / 0 distinct buyers over 6 months
  against 3 sells totalling $665,841. Analyst bullish share 54.5%, **-9.1 points**
  month-over-month (one buy moved to hold between 2026-10-01 and 2026-11-01).
  — source: https://finnhub.io/api/v1/stock/insider-transactions?symbol=BCC
- Structure: `long_term`, target 110.0 (+56.6%), **no stop and no stated
  invalidation condition** — which strategy.md requires of every long_term idea.
  Price 70.24 is below SMA20 75.53 and SMA50 75.80, -20.6% off the 120-day high,
  ATR 5.00%, and the 120-day low is 65.00, only 7.5% below.
- long_term as a class is 0/4 hit target, avg -15.2%. This is the worst
  instance of it in the book.
- action: captured via add_candidate.py as an exit.

## [06:27 ET] MACRO — a second read worth having: XHB +6.91% in a month
- XHB 1m +6.91%, 3m -5.50% vs SPY 1m -4.99%, 3m -4.88%. Homebuilders are
  **leading by ~12 points over one month while the index corrects**, with the
  10y at 4.84%. That is the market front-running easing/mortgage relief even as
  the long end stays high. Noted as regime context; not traded directly today
  because the driver is the same rate path XLU and TLT already express.

## [06:31 ET] CRYPTO — levels fetched, and why no BTC/ETH candidate follows
- Spot (CoinGecko, 06:04 ET): BTC $75,923 (-0.06% 24h, $22.4B vol);
  ETH $2,244.60 (+0.50%); SOL $89.91 (0.00%).
- BTC OHLC (CoinGecko /ohlc, 90d): last close 75,776; range **high 87,330,
  low 62,525**; -13.23% off the high, **+21.19% off the low**; 20-bar SMA 80,454.
- ETH: last 2,236.24; range high 2,804.42, low 1,854.88; -20.26% off high,
  +20.56% off low; 20-bar SMA 2,479.64.
- **Caveat recorded so nobody reuses the number wrongly:** CoinGecko's free
  /ohlc returns only 23 bars for days=90, i.e. ~4-day buckets. The 4,439 "ATR14"
  that falls out of it is a 4-day-bar range and is **not** a daily ATR. For a
  daily crypto ATR I used IBIT instead (below), which is a real daily series.
- IBIT (iShares Bitcoin Trust, Robinhood-tradeable, nasdaq daily bars, 120d):
  close 42.88, **ATR14 1.3256 = 3.09% daily**, SMA20 45.53, SMA50 45.81,
  range 32.84-49.39, -13.18% off high. The -13.18% matches BTC's own -13.23%,
  so IBIT is tracking spot and its 3.09% is the honest daily volatility read.
- **Decision: no crypto candidate today.** Not for lack of an instrument —
  /MBT, /MET, IBIT and spot are all available — but for lack of an edge I can
  defend. BTC sits mid-range: it fell to 62,525 and has recovered 21%, and now
  trades 5.8% below its own trend. There is no dated crypto catalyst this week,
  and the honest crypto stop at the 2.5 ATR floor is 7.7% wide (~$5,870 on
  BTC), which needs a ~19% target to clear the 2.0 swing floor — i.e. $90k,
  above the 90-day high. I am not willing to assert that without a driver.
- strategy.md says a weekend run should shift toward crypto for actionable
  ideas. It also says never manufacture one. The second rule wins here, and the
  consequence is that **this Saturday report has no same-day-tradeable idea** —
  stated plainly rather than filled with a coin flip.

## [06:34 ET] NEWS/REGIME — **the AI-capex complex has deleveraged, hard**
This is the most important finding of the run and it reframes the whole week.
Source: market_data.py relstrength / quote (finnhub + nasdaq), fetched 06:33 ET

Trailing returns vs SPY (SPY: 1m -4.99%, 3m -4.88%, 6m -0.32%):

| Name | 1m | 3m | 6m | Fri 2026-11-06 |
| --- | --- | --- | --- | --- |
| AMAT | **-34.71%** | -36.28% | -23.59% | +4.22% |
| SMH | **-23.60%** | -18.52% | -18.11% | +3.62% |
| NVDA | **-19.02%** | -14.21% | -13.27% | +2.78% |

Friday's closes and moves across the complex: LRCX 200.44 **+8.23%**, KLAC
138.49 **+6.69%**, TSM 375.44 **+6.33%**, CRWV 46.40 +6.28%, MU 690.00 +5.12%,
AMAT 332.715 +4.22%, SMH 463.96 +3.62%, NVDA 186.64 +2.78%, AVGO 293.69 +0.74%.

Two conclusions:
1. **Semis fell ~24% in a month against an index down 5%.** This is a
   sector-specific unwind of the AI-capex trade, not a market correction. It
   also explains the whole shape of Friday: QQQ +1.40% and SPY +0.31% while 8
   of 11 open defensive/value positions fell. Friday was a violent reflex bounce
   in the most-damaged group, not a broad risk-on day — and the book is
   positioned on the other side of it.
2. **It runs straight into two dated catalysts**: AMAT Thu 2026-11-12 amc
   (EPS est 4.1345, rev est $10.5B) and NVDA Tue 2026-11-17 amc (EPS est 2.5263,
   rev est $111.4B). Those two prints now decide whether this was a de-rating or
   the start of an earnings reset.

**AMAT is the one to be careful about.** Down 34.7% in a month, but insiders
sold into it: **0 open-market buys, 0 distinct buyers, 36 sells totalling
$169,016,277 net** over six months. A washout with no insider bid underneath it
is not yet a value signal, and AMAT reports in 3 sessions.
  — source: https://finnhub.io/api/v1/stock/insider-transactions?symbol=AMAT

## [06:35 ET] SCREEN — other names checked against the same lens
- **CEG** (Constellation Energy, earnings Mon 2026-11-09 bmo): 1m -12.32%,
  3m -7.57%, 6m -17.68%, lagging SPY on every window. But **1 open-market
  insider buy, 1 distinct buyer, $417,931** — the only insider bid found today.
  Datacenter-power name sold off alongside the AI complex with an officer buying
  into it. Earnings are **one session away**, which is a coin flip, not an edge.
  Carrying it forward as a watchlist/level question, not a pre-earnings entry.
- **TJX**: 1m -2.49% — **outperforming SPY on 1m**, the only relative strength
  found — but 3m -14.81%, 6m -11.78%, and 0 insider buys against 8 sells
  ($27.7M net). Earnings Wed 2026-11-18. Off-price retail is the trade-down
  beneficiary with unemployment at 4.1%; worth levels.

## [06:40 ET] LEVELS + VALUATION — testing the "semis are washed out" bull case
Levels, 120 daily bars (nasdaq), Friday 2026-11-06 close:

| Sym | Close | ATR14 | ATR% | SMA20 | SMA50 | 120d high | 120d low | off hi | off lo | $vol/day |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SMH | 463.96 | 24.64 | 5.31 | 536.94 | 565.64 | 671.83 | 445.59 | -30.94% | +4.12% | $4.52B |
| NVDA | 186.64 | 8.02 | 4.30 | 211.55 | 219.81 | 243.37 | 181.46 | -23.31% | +2.85% | $21.57B |
| AMAT | 332.72 | 23.11 | 6.95 | 400.83 | 444.84 | **739.67** | 316.95 | **-55.02%** | +4.97% | $2.48B |
| CEG | 249.95 | 12.02 | 4.81 | 263.47 | 270.02 | 310.45 | 228.63 | -19.49% | +9.33% | $1.05B |
| TJX | 135.30 | 3.77 | 2.78 | 142.59 | 135.79 | 170.00 | 122.78 | -20.41% | +10.20% | $0.91B |
| ROST | 231.09 | 7.44 | 3.22 | 232.84 | 230.90 | 257.00 | 205.92 | -10.08% | +12.22% | $0.50B |

**Trailing P/E computed from the four fetched quarterly actuals** (not a
remembered multiple). Source: https://finnhub.io/api/v1/stock/earnings
- **AMAT**: actuals 3.50 + 2.86 + 2.38 + 2.17 = **$10.91** trailing.
  At 332.72 -> **P/E 30.5**. At the 120-day high of 739.67 -> **P/E 67.8**.
- **NVDA**: actuals 2.22 + 1.87 + 1.62 + 1.30 = **$7.01** trailing.
  At 186.64 -> **P/E 26.6**. At the 120-day high of 243.37 -> P/E 34.7.
  Next-quarter estimate 2.5263 -> ~$10.1 annualised run-rate -> forward ~18.5x.
  EPS path 1.30 -> 1.62 -> 1.87 -> 2.22 -> est 2.53 = **~95% YoY growth**.

**This splits the sector and kills half the bull case.** AMAT de-rated from 68x
to 30x trailing — that is a bubble multiple normalising, and the SMA20 above it
is a receding ceiling, not a magnet. NVDA de-rated from 35x to 27x while
compounding EPS ~95% YoY — an ordinary correction in a name whose multiple was
never extreme. So "buy the washed-out semis" is right about NVDA and wrong
about AMAT, and a basket trade owns both.

- Analyst posture, same lens: AMAT bullish share **88.9%, +2.2** (buy 27->28),
  having beaten 4 straight quarters (+1.1/+5.2/+5.9/+1.6%) — i.e. the stock has
  halved while the sell side has not cut. That is estimate-cut risk standing
  directly in front of the 2026-11-12 print, and the reason I will not touch
  AMAT long.
- NVDA bullish share **95.7%, +1.6** (strong_buy 23->25 over four months),
  beats of +2.0/+3.6/+4.3/+3.8%. Mcap $4.50T, $21.57B/day — no liquidity risk.

## [06:41 ET] REJECTED — SMH — right driver, wrong vehicle; it owns AMAT
- Structure was tradeable: close 463.96 only 4.12% off the 120-day low, 1.8 ATR
  ETF stop = 44.4 wide, target at 2.0 R:R = 552.7 vs SMA20 536.94. It works
  arithmetically.
- Rejected because the basket's second-largest de-rating is AMAT at 30x trailing
  coming off 68x with no analyst cuts yet. Buying SMH is buying NVDA's ordinary
  correction *and* AMAT's multiple unwind in one ticket. NVDA direct expresses
  the half of the thesis the evidence supports. Also honours the correlation cap
  — NVDA and SMH are one driver and only one should be published.

## [06:42 ET] REJECTED — AMAT — the de-rating is a multiple unwind, not a dislocation
- -55.02% off the 120-day high, -34.71% in one month, ATR 6.95% daily.
- Trailing P/E still 30.5 after halving; it was 67.8 at the high. Not cheap for
  a cyclical whose cycle may be turning.
- 0 open-market insider buys, 0 distinct buyers, **36 sells / $169,016,277 net**
  over six months.
- Analysts 88.9% bullish and *rising* into a print 3 sessions away — the cuts
  have not happened yet. No long and certainly no pre-earnings long.

## [06:43 ET] DATA QUALITY — options-implied move unavailable
- `market_data.py implied TJX` and `implied SMH` both fail: Yahoo options
  endpoint returns **HTTP 401 Unauthorized**. Same Yahoo outage as the macro
  429s.
- Consequence: I could not check any target against the straddle-implied move,
  which strategy.md asks for. Target feasibility below is therefore argued from
  **ATR multiples and prior swing levels only**, and said so on each idea.
- `market_data.py short BCC` also failed (nasdaq ReadTimeout), so no short
  interest / days-to-cover on any name today.

## [06:48 ET] REJECTED — TJX — "at SMA50 support" was the wrong reading; it is breaking down
- I came to TJX for the trade-down thesis (off-price retail, unemployment 4.1%,
  four straight beats: +1.6%, +15.9%, +1.9%, +3.7%, earnings Wed 2026-11-18)
  and because 135.30 sat right on the SMA50 of 135.79.
- The daily bars say the opposite of support. Source: nasdaq 120-bar history
  - 2026-10-19 close 147.36, then a continuous slide
  - **2026-11-05**: opened 146.16, high 146.73, low 138.455, **closed 138.59** —
    an outside-down reversal giving back the whole prior-day rally
  - **2026-11-06**: gapped to open 135.39, low 134.69, **closed 135.30**, i.e.
    at the bottom of its own range and through the SMA50
- A price slicing through a moving average on a gap, closing on the low, is not
  resting on it. Two sessions of distribution, no reversal bar, no insider bid
  (0 buys, 8 sells / $27.7M), and analyst bullish share **-6.8 points**
  (strong_buy 11 -> 8). No entry.

## [06:49 ET] REJECTED — ROST — same spike-and-fail, and the thesis is contradicted
- Structure: 231.09, ATR 7.4361 (3.22%), SMA20 232.84, SMA50 230.90, only
  -10.08% off the 120-day high — the better-looking of the two charts.
- But the same two-day pattern: **2026-11-04** ran to a high of 249.05 and
  closed 245.74 (+6%); **2026-11-05** opened 249.30 and collapsed to close
  235.23; **2026-11-06** closed 231.09, the entire move retraced. Both off-price
  names spiked on 2026-11-04 and gave it all back by Friday.
- **The relative-strength read kills the thesis outright.** ROST 1m +2.62% beats
  SPY -4.99%, but **XRT is 1m +6.66%** — ROST lags the broad retail ETF by 4.04
  points over 1m and 8.11 over 3m, and TJX lags it far more. If the consumer were
  trading down, off-price would *lead* retail, not trail it. Retail is strong and
  the off-price names are the laggards within it, which is the opposite of the
  mechanism I was trying to buy. Rejected on evidence, not on the chart.
- Keeping the observation: **XRT 1m +6.66% vs SPY -4.99%** is a second
  consumer-resilient signal alongside XHB's +6.91%, and it argues the correction
  is concentrated in AI capex rather than being macro. That is now three
  independent reads pointing the same way (SMH -23.6%, XHB +6.91%, XRT +6.66%).

## [06:53 ET] WATCHLIST — CEG — wait for Monday's print, do not pre-position
- Setup looked strong: gapped down 2026-11-04 from a 263.40 close to open 248.78
  and close 245.72 (-6.7%), bottomed 2026-11-05 at **231.30** against a 120-day
  low of 228.63, then recovered to close **249.95 (+4.3%)** on Friday. A washout
  into support that held, with earnings Mon 2026-11-09 bmo (EPS est 3.8857).
- Analysts 86.2% bullish, **+3.4** points. Trailing EPS from the four fetched
  actuals 3.04 + 2.30 + 2.74 + 2.55 = **$10.63**, so 23.5x at 249.95. Sector
  Utilities, mcap $88.6B, $1.05B/day.
- **The insider buy does not say what I hoped.** It is dated **2026-08-11 at
  $278.62** (Crandall, Roger W, 1,500 shares, $417,931) — nearly three months
  old and now 10.3% underwater. Zero sells, which still beats every other name
  checked today, but a stale purchase is not a buy into this washout.
  — source: https://finnhub.io/api/v1/stock/insider-transactions?symbol=CEG
- **Not recommended for entry: the print is one session away.** Pre-positioning
  into a before-open report is a coin flip, and strategy.md's own example says
  position after the statement, not before. There is also a thesis problem — CEG
  is a datacenter-power name and today's main finding is that the AI-capex
  complex is deleveraging, which is a headwind to exactly the PPA growth the
  valuation rests on. Monday's guidance is the thing to read.
- condition to wait for: the 2026-11-09 bmo print, specifically whether
  datacenter PPA guidance holds. Below 228.63 the washout low has failed.

## [06:54 ET] REGIME — the finding that ties the day together: it is not a market correction
Source: market_data.py relstrength (computed from nasdaq daily bars), 06:52 ET

| Window | RSP (equal-wt) | SPY (cap-wt) | QQQ | RSP vs QQQ |
| --- | --- | --- | --- | --- |
| 1m | **+1.97%** | -4.99% | **-12.24%** | **+14.21 pts** |
| 3m | -1.89% | -4.88% | -8.98% | +7.09 pts |
| 6m | **+5.85%** | -0.32% | -7.75% | +13.60 pts |

RSP verdict string: "outperforming SPY on 1m/3m/6m".
RSP levels: close 216.05, ATR14 2.7456 (**1.27%**), SMA20 216.72, SMA50 214.78,
120d range 200.70-224.20, **only -3.64% off the high**, $2.15B/day.
IWM: 273.67, 1m -1.41% (also beating SPY), but -10.33% off its high and below
both SMA20 276.84 and SMA50 282.11 — small caps are *less* bad, not strong.

**The equal-weight S&P is up 1.97% over the month the Nasdaq fell 12.24%.** The
median US stock is within 4% of its high. So "SPY is 5.9% off its high and in a
correction" — my own 06:06 framing — was the cap-weighted index telling me about
its own concentration, not about the market. Four independent reads now agree:
RSP vs QQQ +14.21, XHB +6.91%, XRT +6.66%, against SMH -23.60%.
This is an AI-capex de-rating inside a healthy tape.

Consequence I should have drawn earlier: the book's problem is not that it is
long. It is that it is long a narrow defensive/value slice that is also lagging
the median stock, while the one thing genuinely cheap relative to its growth
(NVDA) sat unowned.

## [06:58 ET] LONG_TERM LANE — deliberate pass, and it comes up empty. Here is the work.
Screened 8 large caps for a genuine de-rating (120-bar history, nasdaq):
UNH -14.62% off high, NKE -19.01%, PEP -7.36%, TGT -7.23%, MRK -6.49%,
SBUX -5.46%, MDT -4.14%, DIS -3.35%. Six of the eight are within 8% of their
120-day highs and MDT is +38.86% off its low — **a fifth confirmation that the
weakness is confined to AI capex.** Only UNH and NKE were de-rated enough to
work on, so both got the full treatment.

### UNH — the best long-term candidate of the day, and it still fails the floor
- Price 394.15, sitting on the SMA50 of 390.65, -14.62% off the 120-day high of
  461.62, +8.70% off the 120-day low of 362.60. ATR 3.04%.
- **Trailing EPS $20.41** from the four fetched actuals (4.69 + 6.38 + 7.23 +
  2.11) -> **19.3x** at 394.15. The 2.11 is the depressed Dec-2025 quarter, so
  the last three quarters annualise to (4.69+6.38+7.23)/3 x 4 = **$24.40**,
  i.e. **16.2x** forward run-rate.
  — source: https://finnhub.io/api/v1/stock/earnings?symbol=UNH
- Three consecutive large beats: **+12.18%, +28.80%, +8.88%** (the fourth,
  Dec 2025, -0.57%). Analyst bullish share **84.4%, +5.0 points**, hold count
  7 -> 5 — the sell side is upgrading into the de-rating. Insiders immaterial:
  0 buys, 2 sells / $660,910.
- That is the textbook shape — quality business, fixable problem, margins
  visibly recovering in the actuals, sell side turning. **It fails anyway, on
  the reward-to-risk floor, and I am not going to tune it through.**
  - Target, built with **no multiple expansion assumed**: hold today's 19.3x on
    the $24.40 already-reported run-rate -> **$470**.
  - Bear case, if margins do not normalise: trailing $20.41 at the lowest
    multiple the market actually paid in this window (17.8x, at the 362.60 low)
    -> **$360**.
  - R:R = (470 - 394.15) / (394.15 - 360) = 75.85 / 34.15 = **2.22**, against a
    `long_term` floor of **2.5**.
  - Clearing 2.5 needs the target at >=479.5 or the bear case at >=363.8. Both
    are available and both are reverse-engineering, which is the one thing
    strategy.md says the floor exists to prevent. The floor rejected the idea;
    that is the floor working.
  - As a swing instead: stop 370.19 (2.0 ATR), target 442.07, R:R 2.0 — the
    arithmetic clears, but UNH already reported the 2026-09-30 quarter so the
    next print is mid-January, **outside any swing horizon**. No dated catalyst,
    so it is not a swing idea either.
- **Verdict: watchlist, not a recommendation.** It becomes a buy on a pullback
  toward the 362.60 low (which fixes the ratio honestly by improving the entry
  rather than by moving the target), or on the January print confirming a fourth
  quarter of margin recovery.

## [06:59 ET] REJECTED — NKE — the beats are off cut estimates and the sell side is capitulating
- 38.59, -19.01% off the 120-day high of 47.645, +20.71% off the low.
- Trailing EPS 0.48 + 0.20 + 0.35 + 0.53 = **$1.56** -> **P/E 24.7** at 38.59.
  That is *more* expensive than UNH at 19.3x and NVDA at 26.6x-with-95%-growth,
  on earnings that have collapsed.
- The beats look spectacular (+9.99%, +50.15%, +22.89%, +39.22%) and mean little:
  they are against estimates cut to 0.13-0.44 a quarter. Beating a floored
  number is not evidence of earnings power.
- Analysts are actively giving up: bullish share **28.6%, -10.5 points**, with
  **sell 6 -> 7 and strong_sell 0 -> 2** between 2026-10-01 and 2026-11-01. Only
  14 of 49 ratings are buy or better.
- 0 insider buys, 9 sells / $1,574,773. Nothing confirms. Rejected.

## [07:02 ET] WATCHLIST — XHB — strongest relative strength found, but no dated catalyst
- 102.29, ATR 3.1463 (3.08%), above SMA20 98.66 and SMA50 98.42, -13.25% off the
  120-day high of 117.91, +11.34% off the low of 91.87. $232M/day.
- Relative strength is the best on the board: 1m **+6.91%** vs SPY -4.99%, and it
  even leads XLU (+5.02%) which this report already owns. Homebuilders leading a
  correcting tape with the 10y at 4.84% is the market pricing mortgage relief.
- Structure clears the floors cleanly: stop 95.50 is 2.16 ATR below and sits
  under both moving averages; target 115.87 just beneath the 117.91 prior high
  gives R:R exactly 2.0.
- **Three reasons it stays on the watchlist rather than being published:**
  1. **No dated catalyst.** The driver is the rate path, and I have no fetched
     economic-release calendar this run — the macro helper's Yahoo fields all
     failed — so I will not name a CPI or housing print date I did not verify.
     A swing idea whose catalyst I cannot date is not a swing idea.
  2. **It was distributed on 2026-11-05.** Bars show 2026-11-04 high 108.045 /
     close 107.52, then 2026-11-05 opened 107.44, tagged 108.78 and collapsed to
     close 103.85, with Friday closing lower again at 102.29. That is -4.9% off
     Wednesday's high, not a base.
  3. **Correlation.** XLU is open and TLT is awaiting entry, both on the rate
     path. XHB would be the third idea on one driver, at the cap, and RSP
     already carries homebuilders inside the median-stock thesis at a 1.27% ATR
     instead of 3.08%.
- condition to wait for: a daily close back above **104.58** (the 2026-11-02
  close, the level the 11-05 reversal broke), or a pullback into the 98.4-98.7
  SMA20/SMA50 cluster, which would clear the ratio by improving the entry.

## [07:03 ET] NOTE — 2026-11-04/05 was a pivot day across every rate-sensitive group
Seen independently in four names' bars while setting levels, worth recording:
- XHB: 11-04 close 107.52 -> 11-05 close 103.85 -> 11-06 102.29
- ROST: 11-04 close 245.74 (high 249.05) -> 11-05 235.23 -> 11-06 231.09
- TJX: 11-04 close 144.76 -> 11-05 138.59 -> 11-06 135.30
- CEG: 11-03 close 263.40 -> 11-04 245.72 (gap down) -> 11-05 low 231.30 -> 11-06 249.95
Rate-sensitives and consumer names spiked into 2026-11-04 and reversed hard on
11-05; the AI complex bottomed 11-05 and bounced 11-06. I could not identify the
release behind it — no economic calendar was reachable this run — so this is
recorded as an observed pattern, **not** attributed to a cause I did not fetch.

## [07:04 ET] REJECTED — AMAT short — right thesis, unacceptable variance
- Considered deliberately, because the book is 10 long to 1 short and I am
  closing two more longs today, so a bearish idea would be welcome.
- The thesis is the strongest bear case I found: 30.5x trailing after halving
  from 67.8x, analysts 88.9% bullish and *rising* into the 2026-11-12 print so
  the estimate cuts have not happened, and $169,016,277 of net insider selling.
- Rejected on execution risk, not on the thesis. AMAT is -55.02% off its high
  and sits **4.97% above its 120-day low** with a **6.95% daily ATR**; it rose
  4.22% on Friday while LRCX rose 8.23% and KLAC 6.69%. A 2.0 ATR stop on a
  short is 13.9% wide, the squeeze risk into a print three sessions away is
  severe, and `sell_short` requires margin. Being right about the multiple and
  wrong about the week is the likeliest outcome.
- Recorded so it is not re-litigated: the honest expression of this view is
  simply **not owning semis**, which is what the report does by publishing NVDA
  alone and rejecting SMH.

## [07:08 ET] VENUE CHECK
- **NVDA** — US-listed common stock (Nasdaq), `Robinhood Stocks`. In scope with
  no ambiguity; mcap $4.50T, $21.57B/day.
- **RSP** — Invesco S&P 500 Equal Weight ETF, US exchange-listed, $2.15B/day,
  `Robinhood Stocks`. Judged available on the same standard as the ETFs this
  report already holds and trades (XLE, XLU, IYR, TLT, GLD are all listed the
  same way), rather than on a remembered product list. Flagging the basis
  honestly: I did **not** reach Robinhood's support pages this run, so this is
  an inference from the class, not a verified lookup. Mainstream ETFs of this
  size are not the uncertain case the universe rule is aimed at, but if
  validation can check it, it should.
- **XLE, BCC, KHC, ABT, PYPL, HII** — all existing, already-filled positions, so
  tradeability is proven by the fills.
- No crypto, futures or event-contract candidate today, so none of those venues
  needed verification. Options were never in scope.

## [07:09 ET] ARITHMETIC CHECK — recomputed independently, not trusted from the ideas
| Idea | R:R | floor | stop in ATR | ATR floor | baseline wp | claimed wp | edge | target move |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NVDA | 2.000 | 2.0 | **2.245** | 2.0 (stock) | 0.333 | 0.40 | +6.7 pts | 4.49 ATR |
| RSP | 2.000 | 2.0 | **2.021** | 1.8 (etf) | 0.333 | 0.42 | +8.7 pts | 4.04 ATR |
Both clear their floors with the stop set **first** from the ATR floor and the
target taken from what the R:R floor then implied — not the reverse. Both land at
exactly 2.00 because that is what the floor produces when the stop is honest;
neither was nudged. Claimed edge over the driftless baseline is 6.7 and 8.7
points, well inside the 20-point level at which strategy.md says the thesis has
to carry a large claim.

Note on **BCC conviction**: its `evidence` carries **4 distinct kinds**
(positioning, primary_document, technical_level, counter_argument_answered),
which the conviction table mechanically scores as a **5**. It is recorded as a
**4** deliberately, because it is an exit with `position_size_pct` 0 and a
conviction-5 label would imply the 4-5% sizing tier for a position being closed.
Stating the discrepancy rather than leaving validation to find it.

## [07:10 ET] RESEARCH COMPLETE
- candidates: **8 unique symbols, 9 lines** (XLE emitted twice; the second
  corrects a typo and synthesis takes the last entry per symbol)
  - exits (2): XLE, BCC — both closes of filled positions
  - stop amendments on filled positions (4): KHC 21.20->22.90, ABT 97.00->102.40,
    PYPL 54.10->55.90, HII none->264.00
  - new ideas (2): **NVDA** buy conviction 5, **RSP** buy conviction 3
- holds with no amendment, documented in notes and deliberately not emitted as
  candidates (5): RTX (stop held at 186, declined to widen), UNP, XLU, PFE
  (not re-pitched — already 3x in 10 days), AAL short (deteriorating; close
  above 13.60 ends it)
- watchlist, with the condition to wait for stated on each (3): **UNH** (best
  long-term candidate of the day; fails the 2.5 long_term R:R at 2.22 and I
  declined to tune it), **CEG** (earnings Mon 2026-11-09 bmo, do not pre-position),
  **XHB** (strongest relative strength found, no dateable catalyst)
- rejected with reasons logged (5): SMH (owns AMAT), AMAT long, AMAT short,
  TJX, ROST, NKE
- **skew, stated rather than apologised for:** 6 of 8 candidates are position
  management and only 2 are new ideas. That is the honest output of a Saturday
  with no event-contract prices, no crypto edge, and a book of 11 open positions
  that needed decisions more than it needed additions.
- **coverage gaps:**
  - **Event contracts: total loss.** The `events` helper filters the first 200
    unordered Kalshi markets, which are all sports parlays, so every macro search
    returns 0; querying by `series_ticker` directly found the series live but
    every price field (`yes_bid`/`yes_ask`/`last_price`/`volume`/`open_interest`)
    is null without auth. Zero event candidates, and that is a tooling gap, not
    an absence of mispricing. This is the most valuable thing to fix.
  - **No VIX, no DXY, no index or futures quotes, no gold, no WTI** — every
    Yahoo-backed macro field returned HTTP 429. Equity regime had to be read off
    SPY/QQQ/IWM/RSP ETF closes instead.
  - **No options-implied move on anything** (Yahoo options HTTP 401), so no
    target was checked against a straddle. Target feasibility is argued from ATR
    multiples and prior swings only, and said so on each idea.
  - **No short interest or days-to-cover on any name** (nasdaq ReadTimeout).
  - **No economic-release calendar**, which is why XHB has no dateable catalyst
    and why the 2026-11-04/05 pivot across rate-sensitives is recorded as an
    observed pattern with no cause attributed.
  - No crypto OHLCV at daily resolution (CoinGecko free returns ~4-day buckets);
    daily crypto volatility was taken from IBIT instead.
- sources that failed: Yahoo Finance chart API (429, all macro), Yahoo options
  (401), Kalshi prices (null, unauthenticated), nasdaq short interest (timeout),
  nasdaq history for BTC-USD/ETH-USD (no rows).
- sources that worked: finnhub (quotes, earnings calendar, insiders, analyst
  trend, quarterly actuals), nasdaq (daily OHLCV/ATR/SMA), FRED (rates,
  unemployment, CPI), CoinGecko (crypto spot + 4-day OHLC), SEC EDGAR (filings).

## [07:18 ET] SMALL/MID-CAP HUNT — insider-cluster screen over the earnings calendar
The RESEARCH COMPLETE block above was written at minute 25 with budget left, and
I had not hunted small caps at all — a real coverage gap, since strategy.md asks
for it deliberately. **The block below supersedes it.**

Method: took the fetched earnings calendar for **2026-11-12 to 2026-11-19**
(enough lead time to act, unlike the 285 names reporting Mon 11-09), filtered to
revenue estimates of $30M-$3B, and ran `market_data.py insiders` over all
**170 unique names**, keeping anything with >=2 distinct open-market buyers, or
1 buyer committing >=$250K. Insider buying is the one genuinely predictive
public signal and it cannot be screened by sector, only name by name — 170 calls
was the affordable way to do it.

11 hits: ACM (3 buys / **3 distinct** / $699K / **0 sells**), AIIR (3/2/$80K/0),
AUNA (6/1/$357K/1), BAER (8/1/$573K/12), BORR (18/5/$66.7M/7),
BRBR (2/2/$57K/0), BRC (1/1/$1.00M/2), CDNL (18/**7**/$9.57M/**0**),
CMCL (3/2/$1.08M/1), ENR (41/2/$19.3M/0), EYE (1/1/$776K/0).

## [07:19 ET] REJECTED — CDNL — the screen's top hit is a falling knife, and worth recording why
- Cardinal Infrastructure Group, mcap $691M, $16.6M/day. On the raw screen it is
  the best signal of the 170: **7 distinct insiders, 18 purchases, $9,567,174,
  zero sells.**
- Then the price: close **14.56** against a 120-day high of **96.40** — **-84.9%**
  — with SMA20 15.46, SMA50 **25.08**, and a **9.49% daily ATR**.
- **The buys are dated 2026-08-14 to 2026-08-17 at $36.53-$39.75.** Those seven
  insiders are down roughly 62%. The cluster did not mark a floor; it marked a
  level the stock went on to lose three-fifths of.
- Rejected, and recorded as the counter-example to the screen that found it:
  insider buying is predictive on average and is **not** a floor, and a cluster
  three months stale on a stock that has since fallen 60% is evidence about
  August, not about Monday. Any 9.5%-ATR name 85% off its high also fails the
  universe's 40%-prior-move and exitability tests in spirit.

## [07:20 ET] REJECTED — the rest of the insider hits, one line each
- **BORR** — 5 distinct buyers and $66.7M is the largest commitment found, but
  7 sells alongside it and offshore drilling is a leveraged, oil-price-levered
  balance sheet; no time left to do it justice. Best unexamined idea of the day.
- **ENR** — 41 purchases / $19.3M / 0 sells, but **all of it is one buyer**
  ("Aqua Capital, Ltd.", 2026-07-22 to 07-24 at $20.08-$21.09) and that is a
  holder accumulating, not officers signalling. Only 2 distinct. Earnings
  2026-11-17 amc.
- **BAER** — 8 buys by 1 buyer against **12 sells**. Mixed, not a cluster.
- **BRC**, **EYE** — single buyer each, $1.00M and $776K; BRC has 2 sells. One
  buyer is one confirmation, not a cluster.
- **AIIR, BRBR** — 2 distinct buyers but tiny amounts ($80K, $57K), below the
  level at which an officer is really committing.
- **AUNA, CMCL** — 1 and 2 buyers with sells alongside; CMCL is a small gold
  miner whose driver is the metal, not the company.

## [07:26 ET] REJECTED — BORR — $66.7M of insider buying, all of it underwater
- Borr Drilling, mcap $999.6M, $31.7M/day, Energy. Close **3.24** against SMA20
  4.11, SMA50 4.24 and a 120-day high of 6.62 — **-51.06% off the high and only
  4.18% above the 120-day low of 3.11**. Daily ATR **9.52%**.
- The cluster is real and recent: **Tor Olav Troim bought on 2026-10-05, 10-06,
  10-07, 10-09, 10-13 and 10-15** — 9.5M shares across those dates — plus Harvey
  Snowling on 10-14, **at prices of $4.13 to $4.93**. Total $66,718,982 across 5
  distinct buyers. Against 7 sells.
- The stock is **3.24**. Troim is down roughly 25-30% on purchases made three
  to four weeks ago. Rejected.

## [07:27 ET] META-FINDING — insider buying needs price confirmation, and today proved it twice
Worth carrying into future runs, because the screen that found today's best idea
also found its two worst traps, and the discriminator was not the insider data:

| Name | Cluster | Buy prices | Friday close | Price structure | Verdict |
| --- | --- | --- | --- | --- | --- |
| CDNL | 7 buyers, $9.57M, 0 sells | $36.53-39.75 (Aug) | **14.56** | -84.9% off high, SMA50 25.08 | reject |
| BORR | 5 buyers, $66.72M | $4.13-4.93 (Oct) | **3.24** | -51.1% off high, 4.2% off low | reject |
| ACM | 3 buyers, $699K, 0 sells | $70.63-71.12 (May/Jun) | **66.74** | **above SMA20 and SMA50, +12.24% 1m** | **buy** |

The two rejects had *larger* clusters, more buyers and far more money committed
than the idea I published. Ranking on the insider signal alone would have picked
exactly the two falling knives. What separated ACM was that **price confirmed**:
it has reclaimed both moving averages and leads its sector by 16 points, while
the other two sit below every average near 120-day lows. The skill notes say a
cluster of open-market buys is one of the few genuinely predictive public
signals — true on average, and today it was predictive only in conjunction with
trend. Use it as a *filter over* names whose price is already working, never as
a reason to catch something falling.

## [07:28 ET] FINAL COUNTS — supersedes the 07:10 RESEARCH COMPLETE block
Research ran 06:01-06:31 ET. Nothing was lost to the clock; the earlier
RESEARCH COMPLETE block was written at minute 25 and the small/mid-cap insider
hunt was done after it with the remaining budget, which is what this block adds.

- **candidates: 9 unique symbols, 10 lines** (XLE emitted twice, the second
  correcting a typo; synthesis takes the last entry per symbol)
  - **new ideas (3):** NVDA buy conviction 5 (2.0 R:R, stop 2.25 ATR),
    **ACM buy conviction 5** (2.0 R:R, stop 2.76 ATR), RSP buy conviction 3
    (2.0 R:R, stop 2.02 ATR)
  - **exits (2):** XLE, BCC — both closes of filled positions
  - **stop amendments on filled positions (4):** KHC 21.20->22.90,
    ABT 97.00->102.40, PYPL 54.10->55.90, HII none->264.00
- **holds, documented but deliberately not emitted (5):** RTX (declined to widen
  the stop), UNP, XLU, PFE (not re-pitched, already 3x in 10 days), AAL short
  (deteriorating — a close above 13.60 ends it)
- **watchlist with a stated condition (3):** UNH, CEG, XHB
- **rejected with reasons logged (9):** SMH, AMAT long, AMAT short, TJX, ROST,
  NKE, CDNL, BORR, and the six smaller insider hits as a group
- **correlation check:** NVDA is AI capex; ACM is infrastructure with its own
  guidance catalyst; RSP is index breadth. No driver carries more than two
  ideas, inside the cap of three. The one real tension — NVDA long alongside
  RSP's rotation-away-from-megacap — is stated in RSP's counter_argument rather
  than hidden.
- **known gaps, unchanged from the 07:10 list:** no event-contract prices (the
  `events` helper's 200-market window is all sports parlays, and Kalshi returns
  null prices unauthenticated — the single most valuable thing to fix), no VIX /
  DXY / index / futures / gold / WTI quotes (Yahoo 429), no options-implied move
  anywhere (Yahoo options 401), no short interest (nasdaq timeout), no economic
  release calendar, no daily-resolution crypto OHLCV.
- **no same-day-tradeable idea on this Saturday run**, stated plainly: no crypto
  edge I could defend and no event-contract prices to disagree with. Every
  candidate is for the Monday 2026-11-09 open or later.
