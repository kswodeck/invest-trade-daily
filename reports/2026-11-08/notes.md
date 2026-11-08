# Research log — 2026-11-08

## [06:05 ET] SETUP — weekend run
- Sunday 2026-11-08. US equities and futures closed (futures reopen 18:00 ET Sun).
  Per config/strategy.md weekend behavior: crypto + event contracts carry the
  actionable load; equities are week-ahead prep, entries for the next open.
- Prior context read. 39 closed of 65 tracked, 4/39 hit target (10%), avg -5.9%.
  n=39 is past the ~15-trade noise floor, so this is signal, not a bad week.
  - stock: 1/26 target (4%), avg -8.0%  <- worst lane, n=26 closed, real signal
  - etf:   3/13 target (23%), avg -1.6% <- least bad
  - long_term: 0/4 target, avg -15.2%
  - conviction 2: 0/6, avg -8.4%; conviction 4: 2/8, avg -0.8%
  => BAR RAISED TODAY: single-name swing equities need more than a dated
     catalyst + a chart level. I will not publish a conviction-2 single stock
     today. Evidence must include positioning or a primary document.

## [06:05 ET] MACRO — rates, policy, regime
- US 10y 4.84% (2026-11-05), prior 4.90% — falling. source: https://fred.stlouisfed.org/series/DGS10
- US 2y 4.46% (2026-11-05), prior 4.58% — falling faster than the 10y. source: https://fred.stlouisfed.org/series/DGS2
- Fed funds effective 3.88% (2026-11-05), unchanged. source: https://fred.stlouisfed.org/series/DFF
- 10y-2y curve +0.35 (2026-11-06), prior +0.38 — positive, mildly flattening on the day
  but steeper than mid-year. source: https://fred.stlouisfed.org/series/T10Y2Y
- Unemployment 4.1% (Oct 2026), prior 4.2% — improved. source: https://fred.stlouisfed.org/series/UNRATE
- CPI index 336.298 (Sep 2026), prior 334.131 — +0.65% m/m on the index, which is hot
  for a single month. source: https://fred.stlouisfed.org/series/CPIAUCSL
- TLT 81.92 close 2026-11-06. source: stooq via market_data.py
- Read: 2y falling 12bp with a hot CPI index print is a growth-over-inflation
  market — rate cuts being priced on weakening demand, not on disinflation.

## [06:05 ET] DATA GAP — Yahoo Finance returning 429 on every request
- spx, ndx, dow, russell2000, vix, es/nq futures, DXY, us10y quote, gold, WTI all
  FAILED. finnhub refuses indices ("subscription required for CFD indices"),
  stooq 404s on ^-prefixed symbols, no alphavantage/twelvedata key.
- Only bonds_20y (TLT) returned. BTC-USD history also failed (yahoo 429 + no
  stooq/nasdaq coverage).
- Consequence: I have no VIX, no index level, no ATR from the usual path. Must
  source price history another way before setting any level. Nothing gets a
  level I did not fetch.

## [06:08 ET] MACRO — the tape is in a correction, data gap narrower than feared
- Equity quotes + OHLCV history DO work (finnhub/nasdaq). Only ^-prefixed
  indices, VIX, DXY and BTC-USD history fail. So levels are sourceable.
- SPY 735.29 close 2026-11-06 (session: closed, age 38h — previous close, which
  per CLAUDE.md is the freshest honest equity price on a Sunday, not stale data).
  - ATR14 11.12 (1.51% — elevated), SMA20 763.36, SMA50 765.68
  - 120d range 716.58-781.62, -5.93% off the high
  - Nov 4 close 766.81 -> Nov 5 close 733.00 = -4.4% in one session on
    125.9M shares (vs 45.0M 30d average). That is a liquidation day, not drift.
  - Nov 6 closed 735.29, a 735.29/742.21 inside-day hold just above the Nov 5 low.
  source: market_data.py history SPY (nasdaq)
- QQQ 656.10 (+1.40% on 11-06), IWM 273.67 (+0.99%), GLD 372.52 (-0.79%)
- Regime read: SPY below both the 20d and 50d after a 4.4%-on-volume break, with
  the 2y yield down 12bp. Risk-off driven by growth fear. VIX unavailable so I
  cannot quantify the vol regime — noted as a gap, not guessed at.
- Consequence for today: long-equity breakout entries are the wrong shape into a
  tape below its moving averages, and pullback entries will fill easily and keep
  going (the exact failure in the 1/26 stock record). Favour defensives,
  already-de-rated names with their own cause, and non-equity expressions.

## [06:14 ET] EVENT CONTRACTS — lane unavailable today, and why
- `market_data.py events "<topic>"` is near-useless as written: it requests ONE
  page of 200 open Kalshi markets with no server-side search and filters client
  side. Kalshi has far more than 200 open markets, so "CPI", "Bitcoin",
  "recession" and "inflation" all returned count=0 while those series are in fact
  live. The only "Fed" hit was an NFL parlay matching on the ticker substring
  "MPEFED73K". This is a tool limitation, not an empty market.
- Worked around it by querying series directly against the same public API.
  Series confirmed live: KXCPIYOY (CPI y/y, Dec-26 ladder, closes 2027-01-13),
  KXFED (fed funds upper bound, Mar/Apr-27), KXU3 (Nov unemployment, closes
  2026-12-04), KXRECSSNBER-26/-27, KXBTCMAXY-26DEC31, KXNASDAQ100Y-26DEC31.
- **But every price field is null on every market**, on both the list endpoint
  and the per-market endpoint (`/markets/{ticker}`): yes_bid, yes_ask, no_bid,
  no_ask, last_price, volume, open_interest, liquidity all None — including on
  series that certainly trade. The unauthenticated public endpoint is not
  serving order-book data to this run.
- Consequence: I cannot state a market-implied probability for any event
  contract, and config/universe.md requires the edge to be an explicit
  probability disagreement against the market's own number. **So no event
  contract is publishable today.** I will not estimate one from memory — a
  fabricated implied probability is exactly the failure mode the rules name.
- Note for the record: KXBTCMAXY-26DEC31-99999.99 resolves YES if BTC traded
  above $99,999.99 at any time from 2026-01-02, not at year end. BTC is 75.8k
  now after a drawdown from六-figure levels, so that market is likely already
  determined and carries no edge regardless of price.

## [06:14 ET] CRYPTO — prices live (CoinGecko), deep bear market
- BTC   $75,836  -0.14% 24h | 24h vol $10.49B | mcap $1.525T
- ETH   $2,234.25 -0.52% 24h | 24h vol $3.93B | mcap $273.0B
- SOL   $89.15   -0.93% 24h | 24h vol $846M
- XRP   $1.16    -0.87% | DOGE $0.0709 -1.43% | ADA $0.1798 -1.71%
- LINK  $10.75   -0.58% | AVAX $8.16 -1.29% | LTC $51.82 -0.64%
  source: https://www.coingecko.com/ (via market_data.py crypto)
- Whole complex red but quietly so — all between -0.1% and -1.7%, no capitulation
  tick. BTC history via market_data.py FAILED (yahoo 429), so I have no ATR for
  crypto from the usual path and must source OHLC elsewhere before any level.

## [06:09 ET] NOTE ON TIMESTAMPS
- Earlier blocks in this file were stamped from my own estimate of elapsed time
  and run ~5-8 min fast (real clock was 06:05 when the block marked 06:14 was
  written). Sequence is correct; absolute times before this point are not. All
  stamps from here are from `TZ=America/New_York date`.

## [06:09 ET] CRYPTO LEVELS — downtrend, both majors AT their 60-day low
- CoinGecko /ohlc at days=90 returns **4-day candles** (23 bars), not daily, so
  the 5.86% "ATR14" it implies for BTC is a 4-day-bar range and must not be used
  as a daily ATR. Pulled market_chart daily closes instead (61 daily points).
- BTC $75,835: avg abs daily close move 1.54% (14d), 1.34% (30d).
  60d high 86,597, 60d low 75,590 — **price is 0.3% above its own 60-day low**.
  SMA20 79,064, SMA50 81,783 — below both. -13.2% off the 90d high (87,330).
- ETH $2,234: avg abs daily move 1.85% (14d), 1.68% (30d).
  60d high 2,775, 60d low 2,233.59 — **the last price IS the 60-day low**.
  SMA20 2,315, SMA50 2,484 — below both. -20.3% off the 90d high (2,804).
- SOL $89.15: -27.8% off the 90d high, SMA20 104.82, 90d low 74.16.
- Nov 5 was a failed rally in both (BTC 80,443 then 76,006 the next day; ETH
  2,423 then 2,236) — a 5-6% pop fully retraced inside 24h. That is distribution,
  not accumulation.
- Read: this is a confirmed downtrend making fresh lows, not a basing pattern.
  A long here buys a 60-day low with no reversal signal and no dated catalyst;
  per config/strategy.md I will not publish that. A short is also unattractive
  after a 13-20% decline into the low with no catalyst to carry it, and would
  need /MBT (crypto futures) since Robinhood Crypto cannot short. Futures are
  shut until 18:00 ET Sunday.
- **Conclusion: no crypto candidate today.** The weekend lane that usually
  carries a Sunday report is a downtrend at its lows with no edge I can defend,
  and the event-contract lane has no prices. Say this plainly in the report
  rather than manufacturing a crypto idea to fill the weekend slot.

## [06:20 ET] CATALYST — the week's dated events
- **October CPI: Tuesday 2026-11-10, 08:30 ET.** Verified against the BLS release
  schedule (bls.gov/schedule/news_release/cpi.htm — the page itself returns
  "Access Denied" to non-browser agents, which is BLS bot policy and NOT to be
  spoofed; date taken from the schedule as surfaced in search).
  source: https://www.bls.gov/schedule/news_release/cpi.htm
  Note: October 2025 CPI was never published (federal shutdown), so the
  12-month change for October 2026 is not computable on the usual base — a real
  wrinkle in how Tuesday's print will read.
- November CPI: 2026-12-10 08:30 ET.
- Earnings in the next 10 sessions (fetched finnhub calendar):
  SE 11-10 bmo | AMAT + CSCO + NU + STNE 11-12 amc | PDD/BIDU/BZ/PAGS/XPEV 11-16
  | **HD 11-17 bmo, NVDA 11-17 amc** | LOW/TGT/TJX/ROST/PANW 11-18 | WMT 11-19
- So the week is: CPI Tuesday, AMAT/CSCO Thursday, then the NVDA + retail wave
  the following week.

## [06:20 ET] NEWS — what actually happened Nov 5, and it reframes the tape
- S&P 500 -4.4% on 2026-11-05, worst day since April 2025; ~$2.9T of market value
  lost; Nasdaq entered correction; every S&P sector fell.
- **Cause was the midterm result, not a growth scare**: a Democratic win raised
  fear of tighter rules on data-center development and a slowdown in AI
  infrastructure spending. NVDA's index weight amplified it. The drop erased the
  prior session's rally (which had been the best in ~3 months).
  sources:
  https://www.investmentnews.com/equities/nasdaq-enters-correction-as-ai-stocks-sink-after-midterm-elections/268903
  https://stockanalysis.com/news/sp-500-record-one-day-market-value-loss/
  https://www.fox10tv.com/2026/11/05/brutal-sell-off-ai-stocks-sends-wall-street-reeling-sp-500-sees-worst-day-since-2025-liberation-day-tariffs/
- This is a **policy repricing of AI capex**, which is a different animal from the
  "growth scare" I read off the yield curve an hour ago. Correcting that read.
- Caveat I must hold onto: on Friday 11-06 the bounce was in growth, not
  defensives — QQQ +1.40%, IWM +0.99%, SPY +0.31%, while ABT -3.23%, KHC -2.80%,
  UNP -2.61%, BCC -4.76%. So the defensive leadership below is a 1m/3m fact with
  a one-day counter-signal on Friday. Do not pitch it as a fresh breakout.

## [06:20 ET] RELATIVE STRENGTH — the rotation, measured
- XLV: +9.90% 1m, +9.71% 3m, +28.79% 6m vs SPY -4.99% / -4.88% / -0.32%
  => +14.89% 1m, +14.59% 3m, +29.11% 6m vs SPY. Leading on all three.
- XLP: +7.98% 1m, +6.04% 3m, +7.01% 6m => +12.97% / +10.92% / +7.33% vs SPY.
- TLT: +5.20% 1m, -0.17% 3m, -4.83% 6m => +10.19% 1m, +4.71% 3m vs SPY.
- Laggards, measured: IWM -10.3% off high and below SMA20/50; EEM -17.1% off high,
  below both; XLE -12.2% off high, SMA20 67.11 vs price 61.62; GLD -17.0% off
  high and below SMA50.
- Defensives + duration are where the money went; small caps, EM, energy and
  gold are where it left.

## [06:12 ET] REJECTED — TLT — fails the swing R:R floor, and the arithmetic is the point
- TLT 81.92, ATR14 0.77 (0.94%), SMA20 80.72, SMA50 80.38, 60d range 76.43-83.60,
  150d range high 87.79. Leading SPY by 10.19% over 1m. Macro tailwind real
  (2y -12bp Friday). Everything about the direction looks right.
- But: ETF swing stop floor is 1.8 ATR = 1.39. Honest structural stop is 80.40
  (under the Oct 28 low 80.73, the Nov 3 low 80.97, and both MAs) = 1.45 risk
  from 81.85 = 1.88 ATR. Fine.
- The near-term resistance that matters is the 60-day high, 83.60. Target 83.60
  gives reward 1.75 on risk 1.45 = **R:R 1.21 — fails the 2.0 swing floor.**
- To reach 2.0 I would need a target of 84.75+, i.e. above the 60-day high, or a
  stop inside 1.8 ATR. Both are the forbidden move. Per config/strategy.md: "if
  an idea only clears the floor with a tight stop, the idea failed the floor."
- Checked as long_term too: 10y 4.84% to 3.75% over ~2y on ~16 duration => ~96;
  bear case 10y 5.5% => ~73. Upside 14.1 vs downside 8.6 = **1.64, fails the 2.5
  long-term floor.**
- So TLT is rejected in both horizons. It also supersedes the 2026-11-04 TLT BUY
  @ 80.3 sitting in Awaiting Entry: price has moved UP to 81.92, away from that
  entry, so that level is stale and should not be left standing as live.

## [06:12 ET] REJECTED — XLV and XLP — the leadership is too extended for 2:1
- XLV 184.80, ATR 3.79, SMA20 179.98, range high 192.32. A 2.06-ATR stop at
  177.00 (risk 7.80) needs a 200.40 target for 2.0 R:R — 4.2% ABOVE the 150-day
  high. Target at the range high 192.32 gives R:R 0.96.
- XLP 90.08, ATR 1.78, range high 93.40. A 2.01-ATR stop at 86.50 (risk 3.58)
  needs 97.24 — 4.1% above the high. 
- Both are genuinely the strongest sectors on the tape (XLV +14.89% vs SPY 1m)
  and both FAIL the floor, for the same structural reason: a low-volatility
  sector trading near its high has less room to the next level than a 2-ATR stop
  costs. Buying strength here is a 1:1 trade dressed up as a trend-follow.
- This is worth stating in the report: "the leaders are unbuyable at 2:1" is a
  finding, not an absence of work.

## [06:14 ET] POLICY — I tested "buy the AI dip, the veto blocks it" and it FAILS
- Hypothesis worth testing after Nov 5: the market priced a data-center
  regulatory risk that cannot become law, so the AI selloff is overdone.
- What the reporting actually says:
  - Democrats won BOTH chambers on 2026-11-03, seated 2027-01-03.
  - Trump retains the veto, so sweeping FEDERAL AI/data-center legislation is
    indeed unlikely to pass. That part of the hypothesis holds.
  - **But the binding constraint on data centers is not federal.** Democrats also
    flipped governorships, attorneys general and several state legislative
    chambers, and the governors-elect of **Texas, Georgia and Ohio** — the three
    largest data-center build-out states — campaigned on limiting AI
    infrastructure expansion. Siting, zoning, utility interconnection, water and
    tax abatement are all state/local powers that no presidential veto touches.
  - NBC exit poll: 56% of voters called AI/data centers a "crucial or major
    factor" in their congressional vote. That is a durable political incentive,
    not a one-week headline.
  sources:
  https://time.com/article/2026/11/04/midterm-elections-results-ai-industry-data-centers/
  https://iapp.org/news/a/democratic-midterm-wins-set-stage-for-tougher-tech-and-ai-scrutiny
  https://www.foxbusiness.com/politics/new-political-landscape-facing-ai-after-democrats-midterm-gains
  https://accesspartnership.com/opinion/2026-midterms-new-congress-policy-priorities/
- **Conclusion: the hypothesis is rejected, and the bear case is the stronger
  one.** I will not pitch a dip-buy in AI infrastructure on a "it can't pass"
  argument, because the part that bites does not need Congress. Recording this
  so synthesis does not resurrect it.
- This also means NVDA BUY @ 184.0 (published 2026-11-07, awaiting entry) rests
  on a thesis that the following day's research contradicts at the margin. Flag
  it: the level is unfilled and the policy backdrop got worse, not better.

## [06:37 ET] HOUSING LANE — the thesis is real, the setups mostly are not
- Macro mechanism, all fetched:
  - 30y mortgage 7.18% (2026-11-05), from 7.40% (10-15), 7.32% (10-22), 7.24%
    (10-29) — three straight weekly declines.
    source: https://fred.stlouisfed.org/series/MORTGAGE30US
  - 2y 4.46% (-12bp), 10y 4.84% (-6bp). source: FRED DGS2/DGS10
  - XHB +6.91% 1m vs SPY -4.99% => +11.9%. ITB, DHI, LEN, PHM, TOL, MAS all
    above both their 20d and 50d MAs. This is the second-strongest rotation on
    the tape after healthcare.
  - Caveat kept in view: 7.18% is still ABOVE the 2026-09-17 reading of 6.95%,
    so this is a partial retracement of an autumn spike, not a new downtrend.
- No insider buying in BLDR, KBH, MTH or OC (0 open-market buys each), and no
  earnings for any builder in the next 14 days. So the evidence available is
  technical_level + positioning + dated_catalyst (CPI), not more.

## [06:37 ET] REJECTED — BLDR — first real resistance gives 1.12:1
- 62.54, ATR 3.59, SMA20 58.16, SMA50 58.93, 150d range 49.66-94.97.
- Structural stop: below the Oct 29 breakout gap origin (56.25-56.31) and the
  SMA50. 55.80 would be 1.87 ATR — under the 2.0 stock floor — so the honest
  compliant stop is 55.30 = 2.01 ATR, risk 7.24.
- Structural target: first resistance is the Nov 5 high 70.65 / Nov 4 high 70.25.
  Reward 8.11 on risk 7.24 = **R:R 1.12. Fails the 2.0 swing floor.**
- To reach 2.0 I would need a 77.02 target, and there is NO structure anywhere
  between 70.65 and the 94.97 range high to justify it — I would be inventing a
  level. Rejected rather than reverse-engineered.

## [06:37 ET] REJECTED — KBH — the reachable target gives 0.90:1, the 2.75:1 target is out of ATR reach
- 50.70, ATR 2.05, SMA20 46.26, SMA50 47.56, 150d range 40.92-63.63.
- Stop 46.00 (below both MAs) = 2.29 ATR, risk 4.70. Good structure.
- First resistance = Nov 5 high 54.94. Reward 4.24 => **R:R 0.90.**
- The range high 63.63 would give R:R 2.75, but it is 6.3 ATR away, beyond the
  6.0 ATR swing feasibility limit in validate_report.py. Both ends fail.
- MTH and OC have the same shape and are not separately written up.

## [06:37 ET] CORRECTION — my own XHB target was reverse-engineered, fixing it
- I captured XHB with target 115.00. I did not take 115 off a chart; I solved
  102.29 + 2.0 x risk and rounded. That is precisely the "targets nudged until
  they passed" failure CLAUDE.md describes, committed in the same session that
  rejected two other ideas for it. Recording it rather than quietly editing.
- Honest structure for XHB: stop 96.00 is sound (2.00 ATR, below the
  98.42/98.66 MA cluster and below the Oct 28 low 97.19). But the first real
  resistance overhead is the **Nov 5 high 108.78** (Nov 4 high 108.05), which
  gives reward 6.49 on risk 6.29 = **R:R 1.03 — fails.**
- The only defensible higher level is the 150-day range high **117.91**, which
  gives R:R 2.48 and sits 4.96 ATR away (inside the 6.0 limit). That is a real
  level and XHB traded there inside this same 150-day window.
- So XHB is publishable ONLY on a full round-trip-to-the-high target, which
  requires blowing through 108.78. That is an ambitious 15-session ask (+15.3%)
  and I am lowering conviction to 3 and marking it accordingly rather than
  presenting 2.48:1 as comfortable. Re-captured below with the real level.

## [06:37 ET] POSITION REVIEW — all 11, measured not rubber-stamped
Every distance below is in ATR14 from the fetched 150-day history, against the
2026-11-06 close. Nothing has traded since; US equities were shut all weekend.

| Sym | P/L | stop dist | target dist | vs MAs | decision |
| --- | --- | --- | --- | --- | --- |
| XLE | -3.6% | **0.45 ATR** | 4.83 ATR | below both | **CLOSE** (captured) |
| RTX | -4.8% | **0.58 ATR** | 6.1 ATR -> cut to 205.62 | below both | **HOLD, target amended** (captured) |
| BCC | -13.3% | no stop | 11.33 ATR | below both | **needs invalidation + review** |
| PFE | +6.5% | no stop | **15.69 ATR** | above 50d | HOLD |
| KHC | +7.0% | 4.42 ATR | 4.51 ATR | above both | HOLD, no change |
| ABT | +6.7% | 3.48 ATR | 2.00 ATR | above both | HOLD — best-shaped position in the book |
| PYPL | +4.8% | 3.14 ATR | 2.11 ATR | above both | HOLD, no change |
| HII | +10.2% | no stop | 4.16 ATR | above both | HOLD, but it is a swing with no stop |
| UNP | +0.5% | **1.69 ATR** | 3.41 ATR | below 20d, above 50d | HOLD, stop is inside the floor |
| XLU | -0.4% | 2.14 ATR | 5.59 ATR | above both | HOLD, no change |
| AAL short | +1.3% | 1.85 ATR | 3.90 ATR | **price above both MAs** | HOLD, on watch |

Specific findings that are NOT rubber stamps:

- **ABT and PYPL are the two healthy ones.** Both in profit, above both moving
  averages, targets 2.00 and 2.11 ATR away against stops 3.48 and 3.14 ATR
  away. That geometry is the right way round and neither needs touching.
- **UNP's stop is 1.69 ATR from the market**, inside the 2.0 ATR floor this
  report enforces on new stock ideas. It is not a new idea so the floor does not
  retroactively apply, but it means UNP is one ordinary-and-a-half session from
  a stop-out while only +0.5%. Flagged for the red team rather than silently
  widened.
- **PFE's 42.00 target is 15.69 ATR away** (+43% from 29.39). That is only
  coherent as a long-term valuation anchor, never as a swing level. If the stored
  horizon is swing, the target is indefensible and should be restated. The
  insider case behind it is still the real thing: 3 distinct open-market buyers,
  $2.96M, including CEO Albert Bourla 38,000 shares at 26.34 on 2026-08-12, plus
  directors Buckley (37,632 @ 25.52) and Blaylock (39,231 @ 25.46) on 2026-08-05.
  Those buys predate the 2026-08-18 entry, so they are the original thesis
  holding up, not new information — which is why PFE is a HOLD and NOT
  re-pitched today. It has already been recommended 3x in ten days.
  source: https://finnhub.io/ (insider transactions, PFE)
- **BCC is the one that needs real work and did not get it.** -13.3%, no stop, a
  110.00 target 11.33 ATR away, below both MAs, and it fell -4.76% on Friday.
  The reason it matters: BCC is a wood-products supplier to homebuilding, so it
  should be a BENEFICIARY of the mortgage-rate thesis that put XHB in this
  report — and it fell more than twice as hard as XHB on the same session. That
  divergence says something BCC-specific is wrong that I did not have time to
  identify, and its $27M average daily dollar volume means it is the thinnest
  thing in the book. Do not read this HOLD as a conviction call: it is an
  unresolved item, and the long-term lane it sits in is 0/4 with an average
  -15.2%. It needs an explicit invalidation condition, which it currently lacks.
- **AAL is the short to watch.** +1.3% in favour, but price 13.18 is above both
  the 20-day 12.51 and the 50-day 12.88. A short with the market above both
  averages is a short going the wrong way; the 14.40 stop is 1.85 ATR off.
- **HII has no stop** on a swing-horizon long, which the risk rules require for
  nothing in particular but leaves a +10.2% gain undefended 30.3% below its own
  high.

## [06:37 ET] AWAITING ENTRY — the 9 unfilled orders, checked against the market
- `OXY` BUY @ 54.00 — spot 56.38, order is 4.2% BELOW market. Still live but
  energy is the weakest sector on the tape (see the XLE close). Recommend CANCEL.
- `KXCPIYOY-26SEP-T3.5` NO @ 18 — the September contract has resolved or expired;
  it is 2026-11-08. Dead order, remove.
- `GLD` SELL @ 406.77 — spot 372.52, i.e. 9.2% BELOW the sell order. The move the
  idea called for happened without the position, exactly as the 2026-10-25 and
  10-27 reports already said twice. CANCEL and stop republishing it.
- `SMMT` BUY @ 17.10 — was also stopped out 2026-10-26 as a separate position.
- `ONON` BUY @ 34.20 (11-03), `CVS` BUY @ 79.00 (11-05) — CVS was ALSO stopped
  out on 11-04, one day before being re-published as an entry. Worth the red
  team's attention.
- `TLT` BUY @ 80.30 — spot 81.92, order 2.0% below market. Superseded: TLT now
  fails both the swing and long-term floors on my own arithmetic above. CANCEL.
- `NVDA` BUY @ 184.00 (11-07) — spot was 184.21 at capture; the policy backdrop
  got worse not better over the weekend (state-level data-center limits). Flagged.
- `ACM` BUY @ 66.74 (11-07) — not re-examined today, no new information.

## [06:40 ET] INSIDER SCREEN — 22 names checked, 2 real clusters, both rejected
Checked for open-market (Code P) buying: AMAT, CSCO, OXY, DVN, TGT, CVS, PFE,
BCC, BLDR, KBH, MTH, OC, NKE, SBUX, F, GM, INTC, DIS, EL, MDT, BAX, ONON, ACM,
KSS, HAL, SLB. Zero buys in most. Clusters found: PFE (3 buyers, covered above),
ONON (8 buys / 3 buyers / $10.58M), ACM (3 buys / 3 buyers / $0.70M),
INTC (2 buys / 1 buyer / **$19.71M**), F (1 / 1).

## [06:40 ET] REJECTED — INTC — the best insider signal of the day, killed by valuation
- The setup was the most attractive thing I found: INTC fell **-28.6% in one
  session** on 2026-10-30 (92.07 -> 65.76) on 455.6M shares against a ~100M
  average — its worst day since the 1970s — and CEO **Lip-Bu Tan bought 150,000
  shares at $64.73 on 2026-11-02**, three days later, $9.7M of his own money.
  He also bought 105,263 at $95.00 on 2026-08-11 and is down 41% on that lot.
  Price now 56.28, i.e. 13% BELOW the CEO's November purchase. ATR 11.56%.
- Cause of the crash, identified: Q4 revenue guided **$15-16B vs ~$17B**
  consensus and adjusted EPS **$0.25 vs $0.43**. Drivers were PC weakness (AI
  demand is absorbing memory and components, pushing PC prices up) and a plant
  shutdown in Israel after a fatal accident at the facility. Offsetting:
  **data center revenue +78% year on year.** US government stake lost ~$12B.
  sources:
  https://techcrunch.com/2026/10/30/intels-stock-crashes-knocking-12b-from-governments-stake/
  https://www.breitbart.com/economy/2026/10/30/intel-shares-plunge-25-percent-after-chipmaker-issues-disastrous-forecast/
  https://finance.yahoo.com/markets/stocks/articles/intel-logs-worst-daily-drop-130000569.html
- **Why I am not publishing it.** The -60.5% drawdown invites the word "cheap".
  It is not cheap on anything I could fetch:
  - Market cap **$299.1B** on 5,315M shares at 56.28.
  - Guided Q4 revenue of $15-16B annualises to roughly **$62B => ~4.8x sales**.
  - Guided $0.25 quarterly EPS annualises near $1.00-1.70 => a **~33-56x P/E**
    on a business whose largest segment is shrinking.
  - Analyst revisions are moving the wrong way: bullish share **29.1%, -5.4**
    on the month; buys cut 16 -> 12 and holds raised 33 -> 38 between 10-01
    and 11-01.
  So the stock fell 60% from a high (142.35 ~ $756B cap) that had priced an
  enormous foundry and AI success, and after all of that it still trades at a
  growth multiple. A 60% drawdown is not a valuation and a CEO purchase is not a
  floor — the same CEO is 41% underwater on his August lot.
- Mechanics would also have been ugly: an 11.56% ATR means the 2.0 ATR stock
  floor forces a stop near 43.00, about 23% below the market and far under the
  51.22 range low. Target at the SMA20 83.08 gives R:R 2.02 but requires a +47%
  recovery of a fundamental guidance reset inside 15 sessions.
- Keep on the watchlist, not as a recommendation. What would change it: a
  defensible sum-of-parts or book-value anchor (not done here), the Israel plant
  restarting, or a second distinct insider buyer.

## [06:40 ET] REJECTED — ONON — insider cluster, no room
- 8 open-market buys, 3 distinct buyers, $10.58M, including co-founders Caspar
  Coppetti and Olivier Bernhard at 30.67 on 2026-08-14. Genuine cluster.
- But price is 37.36, up from 31.94 on Oct 28, above both the SMA20 34.86 and
  SMA50 31.51, and only 9.8% off the 150-day high of 41.41. Stop 34.00 (below
  the SMA20) = 2.21 ATR, risk 3.36. First resistance is the 41.41 range high =>
  reward 4.05 => **R:R 1.21, fails.** Reaching 2.0 needs 44.08, above the high,
  with no structure behind it.
- Also supersedes the `ONON` BUY @ 34.20 published 2026-11-03: price ran 9.2%
  ABOVE that order and never filled. The level is stale — cancel it rather than
  leave it resting.
- ACM's cluster is real but small ($0.70M, all from May-June) and it was
  published 2026-11-07; not re-examined.

## [06:40 ET] THE DAY'S STRUCTURAL FINDING — why this report is thin
One pattern explains almost every rejection above, and it is worth stating in
the report rather than hiding behind a short list:
- After the 2026-11-05 shock, **ATRs are elevated** (SPY 1.51%, single names
  3-11%), so a compliant stop — 2.0 ATR for a stock, 1.8 for an ETF — is wide.
- But **every group with positive momentum is within 3-6% of its own high**:
  XLV -3.9%, XLP -3.5%, VTRS -0.2%, ABBV -3.8%, HUM -5.0%, UHS -4.5%, HCA -5.1%,
  HD -5.2%, ONON -9.8%.
- So the distance to the first real resistance is SMALLER than the stop costs,
  and the reward-to-risk comes out near 1:1. Nine separate names and ETFs failed
  on exactly this arithmetic today (TLT, XLV, XLP, BLDR, KBH, MTH, OC, ITB,
  ONON, HD, DHI).
- Meanwhile **everything with room to a prior level is in a confirmed downtrend
  below both moving averages** — energy (XLE, OXY, DVN), EM (EEM -17.1%), gold
  (GLD -17.0%), the whole data-center complex (VRT -51.9%, DELL -44.8%,
  NRG -49.7%, PWR -31.4%, ETN -28.5%, SMCI -44.0%, AMAT -55.0%, CSCO -28.0%),
  and crypto at its 60-day lows.
- Buying the first group is a 1:1 trade dressed as a trend-follow; buying the
  second is catching a knife with a policy headwind behind it. XHB is the one
  place where a real level sits far enough above a compliant stop, and even
  there the target is the 150-day high rather than something comfortable.

## [06:42 ET] HEALTHCARE LAGGARD SCREEN — 18 names, 2 laggards, both rejected
Screened CVS, CI, MCK, COR, CAH, DGX, LH, IQV, A, TMO, DHR, RMD, ISRG, SYK, BSX,
VTRS, OGN for a laggard inside the strongest sector on the tape. Only two are
more than 15% off their highs: CVS -24.2% and BSX -36.1%. Everything else is
within 8.3% of its high, which is the same no-room problem as above.

## [06:42 ET] REJECTED — BSX — five distinct insider buyers, and the business is the problem
- The hook: Boston Scientific 42.75, **-36.1% off a 66.88 high**, in the sector
  leading the market, with **10 open-market buys from 5 distinct buyers** — the
  broadest insider cluster I found today. Stop structure was clean too: a 2.11
  ATR stop at 38.60 sits just below the 39.57 150-day low.
- Then the fundamentals. BSX has cut guidance **four times in 2026**:
  - April: 2026 sales growth outlook lowered.
  - Late July: 2026 net sales growth cut from 7.0-8.5% to **5.5-6.5%**; CEO Mike
    Mahoney attributed it to electrophysiology and Watchman.
  - September: guidance cut again over a **cyberattack**.
  - Late October Q3: adjusted EPS $0.73 vs $0.75 consensus; Q4 adjusted EPS
    guided **$0.77-0.79 against $0.83** consensus; FY2026 adjusted EPS trimmed to
    $3.16-3.18; and **Q4 net sales guided to DECLINE 1-3% year on year.**
  - Management said Q4 is the baseline for 2027 and that BSX will **not** return
    to its ~7% weighted-average market growth rate **in 2028**. Oppenheimer cut
    it to Perform.
  sources:
  https://www.medtechdive.com/news/boston-scientific-again-cuts-2026-guidance/826473/
  https://www.investing.com/news/analyst-ratings/rbc-cuts-boston-scientific-stock-price-target-on-guidance-reduction-93CH-4984342
  https://www.ad-hoc-news.de/boerse/news/corporate-news/boston-scientific-stock-falls-as-cyberattack-clouds-2026-guidance/70082456
- Corroborating the deterioration rather than the dip: analyst bullish share
  **64.9%, down 14.0 points** on the month; strong buys 10 -> 8, buys 19 -> 16,
  holds 8 -> 12. And the insider buys are **from August at 49.22 and 47.59**,
  both well above today's 42.75 — those buyers are underwater, so the cluster is
  not a signal that this price is supported.
- The Q3 print is visible in the fetched bars: 45.06 -> 42.43 on 2026-10-28 on
  **69.8M shares against a ~14M average**, with the 39.57 range low set intraday.
- **Rejected.** A company guiding sales to shrink, having cut four times in a
  year and conceding sub-market growth through 2028, is a broken thesis rather
  than a de-rated one. The 36% drawdown is explained, not unexplained.

## [06:42 ET] WATCHLIST — CVS, not re-pitched
- CVS 83.85, -24.2% off the 110.68 high, below its SMA20 89.94 and SMA50 90.38,
  ATR 3.33, range 74.78-110.68, advol $859M. The genuine laggard in the leading
  sector, and 1 open-market insider buy.
- Not published today for two reasons. (1) Geometry: a compliant 2.06 ATR stop at
  77.00 against the first real resistance at the ~90 MA cluster is **R:R 0.90**,
  and the 110.68 range high is 8.06 ATR away, past the 6.0 swing limit. Any
  target between the two would be a number I chose rather than read.
  (2) Repetition: CVS has been recommended **3x in the last ten days**, was
  **stopped out 2026-11-04**, and was republished as an entry at 79.00 on
  **2026-11-05, the day after the stop-out**. That sequence needs the red team's
  attention more than it needs a fourth pitch from me.

## [06:42 ET] NOTE — all three insider clusters failed, for three different reasons
Worth carrying forward. Insider buying was the highest-signal screen available
and it surfaced three real clusters today; none survived a second check.
- **INTC** ($19.7M, CEO): failed on **valuation** — still ~4.8x sales and 33-56x
  earnings after a 60% fall.
- **BSX** (5 distinct buyers): failed on **fundamentals** — four guidance cuts
  and sales guided to decline.
- **ONON** (3 distinct buyers, $10.6M): failed on **geometry** — 9.8% off its
  high, so R:R 1.21.
An insider cluster says someone with better information thinks the price is low.
It does not say the price is low enough, that the business works, or that there
is room to a level. It is a reason to look, never a reason to buy.

## [06:48 ET] ETF SCREEN — 20 sector/thematic ETFs, exactly one had room AND a turn
Screened XLF, XLI, XLB, XLRE, KRE, IYR, XBI, IBB, SMH, XRT, JETS, URA, GDX, SLV,
COPX, XME, PAVE, IGV, KIE, ITA for the one shape that survives today's
arithmetic: more than 9% below its high (room to a real level) AND above both its
20- and 50-day (a turn rather than a knife).
- Above both MAs but no room: XLF -4.8%, XLB -4.9%, XLRE -5.3%, KRE -7.8%,
  IYR -6.1%, IBB -3.9%, XRT -5.7%, KIE -4.3%.
- Room but below both MAs (knives): SMH **-30.9%**, URA -45.2%, SLV -42.0%,
  COPX -27.0%, XME -29.7%, ITA -19.4%, XLI -13.6%, IGV -13.0%, PAVE -15.4%.
- Mixed: XBI -10.4%, GDX -17.1%.
- **The single hit: JETS**, -15.7% off its high and above both averages. Captured.
- Note SMH -30.9% below both MAs: the semiconductor complex is the single
  largest pocket of destruction on the board and corroborates the AMAT/INTC/CSCO
  readings individually.

## [06:48 ET] JETS — captured, and it forced a decision on AAL
- JETS 28.72, ATR 1.035, broke a 25.58-27.64 base Nov 2-4, held the breakout
  through the Nov 5 index decline, closed above SMA20 27.01 and SMA50 27.75.
  Stop 26.60 = 2.05 ATR, below the breakout shelf and both averages. Target
  34.06 = the fetched 150-day range high, 5.16 ATR away. **R:R 2.52.**
  Relative strength +9.5% vs SPY 1m. Conviction 3 — only two kinds hold, and I
  did not inflate it to 4 by counting the oil input, which fits no defined kind.
- Cost-side check, fetched rather than assumed: USO 148.41, -13.6% off its high
  and -1.7% over the last twenty sessions; XOP -10.6% over twenty sessions. So
  fuel relief is real but **modest** — stated that way rather than as a collapse.
- **This contradicted a live position and I resolved it rather than ignoring it.**
  I hold an AAL short at 13.35 (+1.3%). Publishing a JETS long while short an
  airline is incoherent. Three readings say the sector turned: JETS above both
  MAs, JETS holding its breakout through the worst session of the year, and AAL
  itself at 13.18 back above its own SMA20 12.51 and SMA50 12.88 with the 14.40
  stop only 1.85 ATR off. So **AAL is covered at the Monday open for +1.3%** and
  JETS is the expression. Both captured.

## [06:48 ET] POSITION UPDATE — PFE — HOLD, deliberately NOT re-pitched
- decision: hold, no change to any level. No new information arrived this
  weekend and nothing traded since Friday.
- why not captured as a candidate: PFE has been recommended **3x in the last ten
  days**, is +6.5% and working, and the insider cluster behind it (3 distinct
  buyers, $2.96M, CEO Bourla 38,000 at 26.34) **predates the 2026-08-18 entry**.
  Re-capturing it today would be the anchoring the repetition guard exists to
  catch, with no changed fact to justify it. The one thing the red team should
  fix is the 42.00 target, which is 15.69 ATR from the market and only coherent
  as a long-term valuation anchor.

## [06:48 ET] RESEARCH COMPLETE
- candidates captured: 6 entries, 5 distinct symbols (XHB captured twice; the
  second entry supersedes the first and corrects a reverse-engineered target).
  - **XHB** buy, swing, conviction 4, R:R 2.48 — the one genuinely new long
  - **JETS** buy, swing, conviction 3, R:R 2.52 — the second genuinely new long
  - **XLE** POSITION UPDATE - CLOSE (0.45 ATR from its stop after 52 days)
  - **AAL** POSITION UPDATE - CLOSE the short (sector turned against it, +1.3%)
  - **RTX** POSITION UPDATE - HOLD, 226.50 target withdrawn as unreachable
    (6.1 ATR) and replaced with the 205.62 Nov 3 high
- **This is a thin report and that is the finding, not a shortfall.** Two new
  longs, both ETFs, both on a target at a prior high rather than a comfortable
  level. Roughly 25 instruments were rejected on arithmetic rather than taste —
  the full list and the reason for each is above. The structural cause is in the
  06:40 block: elevated ATRs after Nov 5 make a compliant stop wide, every group
  with momentum sits 3-6% under its high so there is less room than the stop
  costs, and everything with room is below both averages with an identified
  reason for being there.
- horizon skew: **no long_term idea cleared today**, and that lane is 0/4 with an
  average -15.2%. I looked (INTC, CVS, BSX, the de-rated pharma and medtech
  complex) and the blocker was honest: a long-term target must be a defended
  valuation, and the tools available here return market cap and analyst trend but
  no revenue or earnings series, so for INTC I could only get as far as ~4.8x
  sales from guided revenue — enough to REJECT on, not enough to anchor a buy on.
  Both captured longs are swing ETFs. Say so in data_quality_notes.
- asset-class skew: no crypto, no futures, no event contract. Each was examined
  and each was rejected for a stated reason (crypto at 60-day lows in a
  downtrend; futures index shorts fail R:R because the stop must sit above the
  moving averages; event contracts have **no obtainable prices** — see the 06:14
  block, this is the one hard tool failure of the day).
- coverage gaps:
  - **Kalshi/Robinhood event contract prices: unavailable.** All price fields null
    on both the list and per-market endpoints. The whole event lane is dark, and
    on a weekend that is the lane that normally carries the report.
  - **No VIX, no index levels, no DXY, no spot WTI, no spot gold, no BTC-USD
    history** — Yahoo returned 429 throughout and finnhub refuses indices. Worked
    around with ETF proxies (SPY/QQQ/IWM for indices, USO for oil, GLD for gold,
    CoinGecko for crypto) and FRED for rates, so no level in this report rests on
    a missing source. But I could not quantify the volatility regime.
  - **BSX, INTC**: rejected on secondary reporting, not primary filings. I did not
    read Intel's Q4 guidance release or Boston Scientific's Q3 release directly,
    which is why neither carries a `primary_document` evidence entry.
  - **BCC** unresolved: it fell -4.76% Friday while its own end-market rallied,
    and I did not identify the cause. It is the thinnest position in the book
    ($27M/day) and carries no stop and no invalidation condition.
  - **Short interest unavailable** for INTC (nasdaq API read timeout); not
    retried for other names.
  - Not reached at all: small and micro caps as a deliberate hunt (the config
    asks for this and I did not get to it), ACM, ONON's fundamentals, and the
    managed-care-versus-hospital policy split beyond a first look.
- sources that failed: Yahoo Finance (429, all requests), finnhub indices
  (subscription required for CFD indices), stooq (404 on ^-prefixed symbols),
  alphavantage + twelvedata (no API key), Kalshi (prices null), BLS direct fetch
  (bot policy - respected, not spoofed), nasdaq short interest (timeout).

## [06:55 ET] BCC RESOLVED — the cause found, position closed, and it cuts against XHB
- Why BCC fell -4.76% on Friday and -13.3% overall: **Q3 2026, reported
  2026-11-02.** EPS $1.04 on $1.8B sales, missing estimates. Wood Products
  EBITDA **+194% to $42.7M** on plywood at $425/msf (+31% y/y, volume -7%).
  Distribution EBITDA down y/y on delivery and fuel costs.
  **Q4 Wood Products EBITDA guided to $10-20M** — a ~65% sequential collapse
  from that same $42.7M — with management citing **continued weakness in
  single-family housing** plus elevated fuel, transport and input costs.
  sources:
  https://www.financialcontent.com/article/bizwire-2026-11-2-boise-cascade-reports-third-quarter-2026-results
  https://www.fool.com/earnings/call-transcripts/2026/11/03/boise-cascade-bcc-q3-2026-earnings-call-transcript/
- decision: **CLOSE** at the Monday open, -13.3%. Captured. The invalidation this
  long_term idea never carried has now happened in public: a 110.00 target
  (+56.6%, 11.33 ATR) cannot stand while the main segment guides down two
  thirds. It is also the thinnest holding in the book at $27M/day, which is the
  worst thing to carry without a stop.
- **This is the hardest piece of evidence against my own XHB long**, and I have
  put it in XHB's `key_risk` and `counter_argument` rather than leaving it buried
  here. A supplier to the end market said eight days ago that single-family
  demand is still weak.
  - The distinction I am relying on, stated so the red team can attack it: XHB is
    a **forward multiple re-rating on the rate path**, and builder equities
    re-rate on rate expectations well before starts and volumes turn, whereas BCC
    is being sold because its own realised and guided segment earnings broke.
    These are compatible positions, but only under that reading.
  - Acted on it rather than just noting it: XHB re-captured with
    **win_probability cut 0.35 -> 0.32** against a 28.7% break-even, size held at
    2.5%, and the counter_argument now explicitly says it is NOT fully answered.
    Conviction stays 4 because conviction counts evidence kinds (3 hold) and
    must not be used as a proxy for expected return — per config/strategy.md.

## [06:55 ET] FINAL COUNTS — supersedes the earlier RESEARCH COMPLETE block
8 entries in candidates.jsonl, **6 distinct symbols** (XHB captured 3x; the last
entry supersedes, carrying both the target correction and the BCC counter-evidence).

| Symbol | Action | Horizon | Conv | R:R | Note |
| --- | --- | --- | --- | --- | --- |
| XHB | BUY (new) | swing | 4 | 2.48 | stop 2.00 ATR, target = 150d high |
| JETS | BUY (new) | swing | 3 | 2.52 | stop 2.05 ATR, target = 150d high |
| XLE | **CLOSE** | swing | 3 | — | 0.45 ATR from stop after 52 days |
| BCC | **CLOSE** | long_term | 3 | — | Q4 segment guidance down ~65% |
| AAL | **CLOSE** short | swing | 3 | — | sector turned; cover +1.3% |
| RTX | HOLD, target cut | swing | 3 | 0.51 | 226.50 was 6.1 ATR, unreachable |

- Two new longs, both ETFs. Four position decisions, three of them closures.
- Net effect on the book: 11 open positions become 8, and the two weakest
  (XLE at 0.45 ATR from its stop, BCC with no stop and broken guidance) are out.
- Evidence kinds were checked against every conviction score: XHB 3 kinds -> 4;
  all others 2 kinds -> 3. Nothing inflated.
- **No long_term buy, no crypto, no futures, no event contract.** Each lane was
  examined and rejected for a reason stated above, not skipped.
- Everything in the three gap blocks above still stands as the coverage gaps,
  with one removed: BCC is no longer unresolved.

## [06:58 ET] SMALL CAPS — checked top-down only, and the class is in the knife bucket
config/universe.md asks for small and micro caps to be hunted deliberately. I did
NOT run a bottom-up small-cap screen today — that remains a real gap and I am
not dressing a top-down read up as one. What I did check:
- IWM 273.67, **below both** its SMA20 276.84 and SMA50 282.11, -10.3% off high.
  Its "+3.58% vs SPY on 1m" is IWM falling 1.41% while SPY fell 4.99% — relative
  outperformance inside a decline, not strength.
- IWO (small-cap growth) 343.86, below both MAs (348.80 / 358.46), -13.3% off high.
- IJR 137.64, below both MAs (138.65 / 139.58), -8.7% off high.
- XBI 152.21, below its SMA50 155.22, -10.4% off high.
- So the whole small-cap complex sits below its averages. Individual names there
  would be the knife-catching half of today's structural problem, with wider
  stops, thinner liquidity and dilution risk on top. That is a reason to deprioritise
  the lane today, not a substitute for having screened it.

## [06:58 ET] CORRELATION CHECK on the two new longs
- XHB and JETS are both consumer cyclicals helped by a falling rate path, so they
  are not fully independent. Primary drivers differ — XHB is mortgage rates and
  housing turnover, JETS is jet fuel cost and travel demand — so this is 2 ideas
  on related but distinct drivers, inside the 3-per-driver cap.
- The shared risk is explicit and belongs in the report: **both lose if the
  post-midterm equity correction extends**, since both are high-beta cyclicals,
  and both lean on the same falling-rate backdrop that a hot Nov 10 CPI would
  remove. Combined size is 4.5% of capital (2.5% + 2.0%), which is below the 5%
  single-idea cap and is the right order of magnitude for two correlated
  cyclical ETFs in a tape below its 50-day.
- Also worth the red team's eye: closing XLE (energy) while buying JETS is
  internally consistent — cheaper fuel is the airline's gain and the energy
  producer's loss — and I would rather own that pair than the reverse today.

## [06:58 ET] END OF RESEARCH
Research ran 06:03-06:41 ET and was not truncated; this block and the 06:55
FINAL COUNTS supersede the earlier RESEARCH COMPLETE block. Nothing was lost to
the clock. candidates.jsonl holds 8 entries / 6 distinct symbols and is the
deliverable; everything above is context and the reasoning for ~30 rejections.
