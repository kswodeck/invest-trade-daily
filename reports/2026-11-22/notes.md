# Research log — 2026-11-22

## [06:04 ET] SETUP
- Sunday run. US equities/futures closed; every equity price here is the Friday 2026-11-20 close.
- Per config/strategy.md weekend behavior: shift toward crypto + event contracts for actionable
  ideas; equities are week-ahead prep with entries for the next open (Mon 2026-11-23).
- Budget start 06:01 ET. Minute-20 hard deadline 06:21 ET. Stop-new-research 06:43 ET.

## [06:04 ET] MACRO — rates, curve, risk
- FRED US10Y **5.04%** (2026-11-19); US2Y **4.76%**; fed funds effective **3.88%**;
  10y-2y spread **+0.29** (2026-11-20). Source: https://fred.stlouisfed.org/
- That shape is the thing to notice: policy rate 3.88% but 10Y at 5.04% = ~116bp of
  term premium above the funds rate. The long end is NOT rallying with cuts; this is a
  fiscal/term-premium regime, not a duration-friendly easing regime.
- TLT 81.45, +1.37% on Fri 2026-11-20 close (finnhub). Source: market_data.py macro
- Unemployment 4.1% (2026-10-01). CPI index 337.476 (2026-10-01).
- DATA GAP: ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES, NQ, DXY, 10Y quote, gold, WTI all
  returned ok:false — finnhub requires a CFD subscription for indices and Yahoo is
  HTTP 429 rate-limited this morning. Will use ETF proxies (SPY/QQQ/IWM/GLD/USO/UUP)
  for index context instead of stating index levels.

## [06:05 ET] MACRO — crypto (live, 24/7, the only open market)
- BTC **$60,810**, +5.16% /24h, vol $37.8B, mcap $1.223T
- ETH **$1,707.28**, +4.20% /24h, mcap $208.8B
- SOL $70.55 (+3.75%), XRP $0.9308 (+3.95%), DOGE $0.05551 (+4.74%),
  ADA $0.14559 (+4.58%), LINK $8.81 (+5.28%), AVAX $6.67 (+4.72%), LTC $39.66 (+2.76%)
- Source: https://api.coingecko.com/api/v3/simple/price (coingecko), as of 06:0x ET
- Context: the /MBTZ6 SHORT published 2026-11-09 was waiting at 74,075 and never filled.
  BTC is now 60.8k — i.e. the bearish crypto view was right and the entry was above the
  market the whole way down. That is the pullback-entry failure mode in config/strategy.md
  §Level-setting, on a short: the limit sat where price never returned.
- Entire complex is up 3-5% in 24h together = one beta bounce, not nine signals.
  Correlation cap applies: at most ONE directional crypto beta idea today.

## [06:06 ET] MACRO — Friday 2026-11-20 was a liquidation day, not a rotation
All figures = official Friday close via nasdaq/finnhub (market CLOSED, not stale):
| ETF | Close | Fri % | ATR14 | ATR% | SMA20 | % off 45d high | Fri volume vs 30d avg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 689.81 | -3.64% | 16.07 | 2.33 | 747.81 | -11.75% | 151.4M vs 52.2M = **2.9x** |
| QQQ | 608.45 | -5.67% | 21.13 | 3.47 | 678.53 | **-20.24%** | 134.8M vs ~45M = ~3x |
| IWM | 256.61 | -2.88% | 6.28 | 2.45 | 276.23 | -11.19% | 57.5M vs ~24M = ~2.4x |
| GLD | 322.87 | **-3.67%** | 7.81 | 2.42 | 360.42 | **-19.44%** | 23.6M vs ~10M = ~2.4x |
| TLT | 81.45 | **+1.37%** | 0.78 | 0.96 | 80.99 | -1.17% | 66.1M vs ~38M = 1.7x |
| XLV | 177.24 | -0.12% | 3.88 | 2.19 | 184.35 | -7.84% | 18.1M |
| HYG | 76.33 | -0.26% | - | - | - | - | - |
- Source: scripts/market_data.py history/quote (nasdaq + finnhub)
- READ: SPY closed at 689.81 against a daily low of 686.75 — i.e. **on the low**, on 2.9x
  volume. QQQ closed 608.45 vs low 606.23, also on the low. No intraday reversal bid.
- **Gold -3.67% on the same day equities fell 3.6% is the tell.** In a growth scare gold
  rises. Gold and stocks and crypto falling together while only Treasuries rise is a
  *deleveraging/margin* event — correlated assets sold to raise cash. GLD -19.4% off its
  own high says the gold trade unwound violently too.
- Confirming cross-check: HYG only -0.26% and TLT +1.37%. Credit did NOT crack. If this
  were a solvency/recession repricing, HYG would be down multiples of that. So the
  deleveraging read is supported by credit holding and contradicted by nothing yet.
- QQQ -20.2% off high = Nasdaq proxy in a technical bear market; SPY -11.8% = correction.
  The dispersion (QQQ -5.67% vs XLV -0.12% on the same day) says this is concentrated in
  long-duration growth/AI, not broad.

## [06:07 ET] NEWS — what Friday 2026-11-20 actually was
- Nasdaq Composite -5.28% to 22,617.73; S&P 500 -3.7% into correction on a SEVENTH
  straight losing session; Nasdaq 100 -5.6%, worst WEEK since 2020, centred on an
  AI/semiconductor unwind. Source: https://finance.biggo.com/news/81c15013-c97c-4909-99a7-f0ad2147a10e
- Spot gold ~$3,520-3,540, down ~2.4-2.8% on the session.
  Source: https://www.kitco.com/news/article/2026-11-20/gold-falls-toward-3500-silver-slides-stock-markets-enter-correction
- Attributed causes (ANALYST INTERPRETATION, not confirmed fact — flagging as such):
  Kitco -> liquidation + restrictive policy expectations + global growth concern.
  Others -> **expectations of further Fed rate INCREASES**.
  Stocktwits -> tightening liquidity, persistent inflation, year-end cash demand,
  leveraged positions. Source: https://stocktwits.com/news-articles/markets/equity/why-gold-silver-and-bitcoin-are-crashing-together-the-great-cash-grab/cNbnYXsR91w
- Gold fell even though yields and the dollar weakened, which normally supports it —
  read by multiple outlets as unwinding of a crowded long to raise cash/meet margin.
  Source: https://www.newsweek.com/what-golds-price-collapse-means-for-millions-of-americans-12745775
- CAVEAT ON THESE SOURCES: aggregator/commentary quality, and the gold prints differ by
  time of day. The *prices* I trade off are the fetched ETF closes above, not these.
- The single most important regime fact: **the market is debating Fed HIKES, not cuts**,
  with fed funds at 3.88% and US10Y at 5.04%. Every long-duration idea in the open book
  (TLT, XLU, growth) is on the wrong side of that if it is true.

## [06:08 ET] POSITION UPDATE — IWM — short opened 2026-11-18 @270.5, +5.1%
- decision: HOLD, levels unchanged (entry 270.5 / target 238.69 / stop 284.5)
- why: thesis intact and strengthening (hike risk hits floating-rate small-cap debt
  hardest); closed at 45-session low 256.61 on 2.4x volume, on the low.
- deliberately NOT walking the stop in from 284.5 to lock gains — that is the exact
  KRE anti-pattern in CLAUDE.md (ratio improved, trade made strictly worse). 284.5 is
  2.23 ATR from entry and clears the 1.8 ATR ETF floor.
- R:R from entry = (270.5-238.69)/(284.5-270.5) = 31.81/14 = **2.27:1**, floor 2.0 OK.
- action: captured via add_candidate.py. #1 candidate.

## [06:09 ET] MACRO — THE headline finding: the market prices a Fed HIKE on Dec 9
Kalshi `KXFEDDECISION-26DEC-*`, FOMC decision 2026-12-09 (market close 18:59Z).
The summary endpoint returns null bid/ask/last for every Kalshi market this morning,
so these came from the **order books** (`/markets/<ticker>/orderbook`), best bid each
side, yes_ask derived as 1 - best_no_bid:
| Outcome | yes_bid | yes_ask | Implied prob |
| --- | --- | --- | --- |
| Hike 25bps | 0.89 | 0.90 | **~89%** |
| Hike >25bps | 0.02 | 0.03 | ~2-3% |
| Fed maintains rate (H0) | 0.07 | 0.08 | ~7-8% |
| Cut 25bps | — | 0.01 | ~1% |
| Cut >25bps | — | 0.01 | ~1% |
- Source: https://api.elections.kalshi.com/trade-api/v2/markets/KXFEDDECISION-26DEC-H25/orderbook
- This is the regime, and it explains every price above at once: fed funds effective
  3.88% going to ~4.13%, US10Y 5.04%, gold -19.4% off its high (real rates up),
  QQQ -20.2% (long-duration growth de-rated), IWM leading down. Nothing here is a
  growth scare — it is a **discount-rate** event with a dated trigger.
- IMPLICATION FOR THE OPEN BOOK: it is long TLT (duration), long XLU (bond proxy) and
  long 13 other cash equities into a telegraphed hike. The book is on the wrong side
  of the one macro fact that is nearly fully priced.

## [06:09 ET] REJECTED — KXFEDDECISION-26DEC-H0 YES @7-8c — no defensible edge, and the
  closest precedent is against me
- Prior context lists this as awaiting entry, published 2026-11-21 YES @ 10. It is now
  7-8c, i.e. cheaper, and the tempting pitch is "Friday's crash makes the Fed blink".
- I am NOT pitching it, because the single closest historical analogue runs the other
  way: **Dec 2018** — the S&P was ~15% off its high into the Dec 19 meeting and the Fed
  hiked anyway. An 8c hold price against a telegraphed hike is roughly fair, and to
  publish YES I would have to claim 15-20% while naming no mechanism the committee has
  not already seen. That is a hunch, which is conviction 1, which does not publish.
- RECOMMENDATION ON THE OPEN LINE: it never filled at 10. Leave the order unfilled /
  cancel rather than chasing it down to 7. Logged here so synthesis does not re-pitch it.

## [06:10 ET] CRYPTO LEVELS — BTC daily closes, coingecko market_chart 60d
- Last $60,889 (06:3x ET Sun). 60-day high **$86,490**, 60-day low $58,818 (set 2026-11-21).
- **-29.6% off the 60-day high.** SMA20 $69,334 — price is 12.2% BELOW its own 20-day.
- Daily closes 11-10 through 11-22: 75,267 / 73,721 / 73,974 / 71,372 / 68,314 / 64,120 /
  65,305 / 64,841 / 64,889 / 62,997 / 61,921 / 58,818 / 60,889 — 9 down days in 12.
- Avg absolute daily close-to-close move, last 14d: **$1,573** (~2.6%). Used as the ATR proxy.
- Source: https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=60
- market_data.py history BTC-USD returned ok:false (no error string) — used coingecko directly.

## [06:10 ET] REJECTED — short /MBTZ6 — the regime trade, and I cannot build it honestly
- The thesis is right-shaped: BTC is the purest liquidity-beta asset and the Fed hikes in
  17 days at 89% implied. But every version of the trade fails a rule:
  - Entry at the declining SMA20 (~68,500) needs a **+12.5% bounce to fill**. That is
    precisely why the 2026-11-09 /MBTZ6 short @74,075 never filled while BTC fell to
    58,818 — the short limit sat where price never returned. Repeating it is not a plan.
  - Entry near the market with a stop above the 73.7-75.3k Nov 10-12 shelf gives risk
    ~7,000. Clearing the 2.5 futures R:R floor then needs a target of ~51,000 — a new
    low 13% below the 60-day low. That is reverse-engineering the target to pass the
    floor, which config/strategy.md says means the idea failed the floor.
- Also: BTC is already -29.6% and bouncing +5.2% in 24h. Shorting the eleventh down day
  of thirteen is chasing, not positioning.
- CONSEQUENCE FOR THE OPEN LINE: `/MBTZ6` SHORT @74,075 (published 2026-11-09) is stale by
  18%. Cancel the order. Do not re-pitch it lower — the move happened without us.

## [06:10 ET] CANCEL — GLD SELL @406.77 (published 2026-10-25) — same failure mode
- GLD closed Friday at **322.87**, i.e. 20.6% BELOW the 406.77 short entry that never
  filled. The call was directionally right and the limit was never reached.
- Do not re-pitch a gold short here: GLD is -19.44% off its 45-day high and fell 3.67%
  on Friday in what multiple sources read as forced liquidation. Shorting that is
  chasing a completed move. Cancel and stand aside.
- Source: scripts/market_data.py history GLD (nasdaq close 2026-11-20)

## [06:10 ET] NOTE — the entry-style lesson this run keeps re-learning
Three awaiting-entry shorts/levels (GLD 406.77, /MBTZ6 74,075, and the IWM entry at
270.5 which DID fill) make the point in config/strategy.md §Level-setting concrete: a
limit placed away from the market only fills if price comes back, and in a trending
tape it does not. Two of the three best directional calls this book made produced zero
P&L for that reason. Where a level is real support/resistance, a pullback entry is
fine; as a reflex discount off the last print it selects for the ideas already failing.

## [06:11 ET] CORRECTION — note timestamps above
The headings from "MACRO — Friday" onward were first written with estimated clock
times (06:09-06:40) that ran ahead of the real wall clock. A `date` check at the
3-candidate mark returned **06:10:31 ET**, so ~9 minutes had elapsed, not ~45. The
headings are now corrected to real times. No price, level or probability was affected
— every figure in this log came from a fetched source, not from the clock. Recording
the correction rather than silently editing, since the log is the audit trail.
Real budget position: started 06:01 ET, 3 candidates captured by 06:10, minute-20
deadline met with 11 minutes to spare. New-research cutoff stands at 06:43 ET.

## [06:13 ET] CATALYST CALENDAR — dated events, next 10 sessions (finnhub earnings)
Source: scripts/market_data.py earnings --days 12 (356 events). Thanksgiving is
2026-11-26, so this is a four-session week: Mon 23, Tue 24, Wed 25, half-day Fri 27.
- **Mon 2026-11-23 (134 names)** — retail cluster: **DKS**, ANF, URBN, KSS, BURL, GES,
  SNBR, CENT/amc. Tech: ZM/amc, HPE/amc, A/amc, SMTC/amc, SYM/amc, TUYA/amc,
  FLNC/amc. Also GDRX/bmo, J/amc, DRVN, PSNY.
- **Tue 2026-11-24 (54)** — **ADI**/bmo, **MDT**/bmo, **BBY**/bmo, DLTR, SJM/bmo,
  DY/bmo, ITRN/bmo, BILI/bmo, BZUN/bmo, KC/bmo; after close: **DELL**, **HPQ**,
  **WDAY**, **ADSK**, **NTNX**, AMBA, QFIN, VREX, **CLSK**.
- **Wed 2026-11-25 (17)** — **DE**/bmo (Deere), BZ/bmo, DSX/bmo, NNOX/bmo, IMKTA, FINV/amc.
- Thu 2026-11-26 — holiday, 8 micro names only. Fri 2026-11-27 — 8 micro names.
- READ: the week's real information is (a) **US consumer**, via the Mon retail cluster
  plus BBY/DLTR Tue, and (b) **enterprise AI capex digestion**, via ADI Tue bmo then
  DELL/HPQ/WDAY/ADSK/NTNX Tue after the close. Given Friday was an AI-unwind day, that
  Tuesday-evening block is the highest-stakes event of the week for the Nasdaq.
- Macro: FOMC 2026-12-09 (see 06:09 block). No FOMC this week.

## [06:14 ET] POSITION UPDATE — DKS — URGENT, earnings Monday 2026-11-23
- DKS is an OPEN position: opened 2026-11-13 @144.5, stop 129, target 175.5, last 132.25
  (-8.5%). ATR14 = 6.81 (5.15% of price), SMA20 143.02, 45d range 120.15-150.35.
- **It reports earnings Monday 2026-11-23**, confirmed on the fetched finnhub calendar.
- The position sits **0.48 ATR above its own stop** going into a print. That is the worst
  possible geometry: a typical DKS earnings gap is multiples of the 3.25 of room left,
  so the stop is not a risk control here — it is a coin flip that will be resolved by a
  gap through it, filling well below 129 rather than at it.
- This is also the position that was published 2x (per prior_context), so there is an
  anchoring warning attached to it already.

## [06:16 ET] LEVELS/REJECTED — ADI — right thesis, cannot build it inside the floors
- ADI reports **Tue 2026-11-24 bmo** (fetched calendar). The divergence is the most
  striking thing I found today: close **345.92**, -20.24% off the 45d high and only
  **0.58% off the 45d low** (343.94), having fallen 8.3% on Friday alone (377.44 ->
  345.92) — while the fundamental record is immaculate: **4 beats of 4**
  (+2.43%, +5.33%, +5.38%, +0.75%), revisions **improving**, bullish share **91.9%**
  (+5.4). SMA20 397.59, so price is 13% below its own 20-day.
- Mechanism for a real mispricing: ADI is analog/industrial/auto, sold inside an
  AI-datacenter basket unwind it does not belong to.
- WHY I AM NOT PUBLISHING IT: ATR14 is **22.56 (6.52% of price)**. The 2.0 ATR swing
  floor forces the stop to 300.8 or lower; risk from a 346 entry is then ~45, so the
  2.0 R:R floor demands a target of ~436 — **above the 433.72 45-day high**, i.e. a
  full round-trip of the unwind, and 38.7x trailing EPS of $11.26. I will not publish
  a target that only works by being optimistic; config/strategy.md calls that failing
  the floor. Long_term fails too: 30.7x trailing is not a valuation anchor.
- Insider check (required for equity finalists): `insiders ADI` -> 0 open-market buys,
  0 distinct buyers. Absence is not a negative, per the skill, but there is no
  confirmation there either.
- DISPOSITION: **watchlist**, not a recommendation. The condition to wait for is the
  Tuesday print — if ADI beats a fifth time and the stock holds above 343.94, the ATR
  compresses and the same trade becomes buildable inside the floors.

## [06:16 ET] REJECTED — DLTR — best relative strength on the board, no room left
- Close **137.96**, ABOVE both SMA20 (136.49) and SMA50 (125.11) while SPY sits 7.8%
  below its own 20-day — genuine relative strength; only -7.12% off its high. Reports
  **Tue 2026-11-24**. 3 beats of 4, including **+131.9%** in the Sept quarter
  ($2.70 actual vs $1.164 est). Revisions improving. Trade-down tailwind fits the regime.
- WHY NOT PUBLISHED: it has already run from 85.88 to 148.54 over 150 days. Trailing EPS
  $8.21 (2.70+1.74+2.56+1.21) puts it at 16.8x — fully priced. A 2.0 ATR stop (ATR 6.23)
  sits at ~124; clearing 2.0 R:R then needs ~165, which is 11% ABOVE the 150-day high.
  As long_term, an honest bear case of 13x on $8.00 = ~104 (it traded at 85.88 this year)
  gives at best 1.6:1 against a 171 target — well under the 2.5 floor.
- Insiders: 0 open-market buys, 0 distinct buyers.
- DISPOSITION: watchlist. Momentum is not the problem; the absence of a gap between
  price and any defensible target is.

## [06:17 ET] NOTE — why two good-looking names failed the same way
ADI and DLTR failed for opposite reasons and it is worth recording the pattern: ADI's
ATR is so inflated by the crash week (6.52%) that an honest 2-ATR stop forces an
optimistic target; DLTR's price is so close to its own high that no honest target
leaves room. The floors did exactly what CLAUDE.md says they are for — rejecting ideas
rather than calibrating targets. Publishing either would have required nudging a number.

## [06:17 ET] CVS — captured, conviction 4 (amends the unfilled 2026-11-05 line @77.5)
- Close 80.84 = **9.7x** trailing four-quarter EPS of **$8.33** (2.09+2.58+2.57+1.09,
  all fetched actuals); **-26.96%** off the 150d high of 110.68; range low 76.10.
- 4 beats of 4; revisions **improving**; bullish share **87.5%** (+2.7). $924M avg daily
  dollar volume. SMA20 86.94, SMA50 88.43 — price below both.
- Levels set stop-first, per the rule: stop **71.5** below the 76.10 range low =
  **2.17 ATR** (ATR 3.913), clears the 2.0 stock floor. Entry 80.0 -> risk 8.5.
  Target **101.5 = 12.18x** the same trailing EPS and **8.3% BELOW** the 150d high,
  so reward 21.5 and **R:R 2.53** clears 2.0 without stretching the target.
- win_probability 0.42 vs a 0.283 baseline = 13.7 pts of claimed edge (under the 20-pt
  large-claim line).
- Conviction counted honestly at 4, not 5: three distinct kinds hold (valuation_anchor,
  positioning, technical_level). I did NOT claim counter_argument_answered as a fourth,
  because the only evidence answering the bear case is the same 4-of-4 beat record
  already counted under positioning — reusing one fact is one confirmation.
- Entry moved UP from the stale 77.5 to 80.0 deliberately: that line sat unfilled 17
  days while the stock rose. Closer to market, not further.
- NOTE correlation: with XLV and ABT open, CVS is the THIRD healthcare-driver position.
  That is the cap in config/strategy.md. No fourth healthcare idea today.

## [06:21 ET] POSITION AUDIT — all 15 open positions, geometry from the Friday close
ATR14 fetched per symbol (nasdaq, 45 sessions). "room" = distance from Friday close to
the stop, in ATRs. "stop@entry" = how many ATRs the stop sat from the entry when published.
| Sym | Last | Stop | Room (ATR) | stop@entry (ATR) | R:R@entry | %vs entry | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KHC | 25.39 | 21.2 | **5.31** | 2.28 | 2.83 | +10.4% | healthiest in the book |
| OXY | 53.90 | 50.15 | 2.03 | 2.08 | 2.08 | -0.2% | hold, compliant |
| ABT | 103.00 | 97.0 | 1.96 | **1.96** | 2.39 | 0.0% | marginally under floor |
| XLU | 42.69 | 41.8 | 1.39 | 2.35 | 2.20 | -1.4% | hold |
| UNP | 287.29 | 277.4 | 1.31 | **1.49** | 2.45 | -0.5% | **stop below the 2.0 floor** |
| ADM | 66.95 | 64.4 | 1.16 | 2.01 | 2.09 | -2.7% | hold, at range low |
| RTX | 190.17 | 186.0 | **0.71** | 2.22 | 2.12 | -4.4% | hold, one day from stop |
| HUN | 8.36 | 8.09 | **0.69** | 2.31 | 2.00 | -7.1% | hold, one day from stop |
| XLV | 177.24 | 176.0 | **0.32** | 2.06 | 2.13 | -3.7% | captured, hold |
| DKS | 132.25 | 129.0 | **0.48** | 2.28 | 2.00 | -8.5% | captured, EXIT (earnings Mon) |
| IWM | 256.61 | 284.5 | 4.44 (short) | 2.23 | 2.27 | +5.1% | captured, hold |
| TLT | 81.45 | 78.8 | 3.38 | 1.91 | 2.67 | +1.4% | captured, hold |
| PFE | 27.40 | none | n/a | n/a | n/a | -0.7% | long_term, no stop by design |
| CAG | 14.92 | none | n/a | n/a | n/a | +3.6% | long_term, no stop by design |
| HII | 280.34 | none | n/a | n/a | n/a | +7.0% | **no stop, not long_term** |
Two findings the per-idea view would never surface:
- **UNP was published with a stop inside the floor.** 288.6 entry, 277.4 stop, ATR 7.536
  -> **1.49 ATR**, against a 2.0 requirement for a stock. The R:R of 2.45 it published at
  was therefore bought with a stop that was too tight, which is the exact mechanism
  CLAUDE.md records for KRE. Re-deriving it honestly: a floor-compliant stop is ~273.0
  (2.07 ATR), and R:R then becomes (315.99-288.6)/(288.6-273.0) = **1.76 — it fails the
  2.0 floor.** The idea does not qualify at a compliant stop. ABT is the same problem one
  rounding away (1.96 ATR) and is left alone.
- **HII carries no stop and is not a long_term idea.** PFE and CAG legitimately have none.
  HII at +7.0% is a swing-shaped position with unbounded downside; ATR 11.75, SMA20
  299.41, -14.47% off its 45d high.
- **Five of fifteen positions sit under 1.4 ATR from their stop** (XLV 0.32, DKS 0.48,
  HUN 0.69, RTX 0.71, ADM 1.16, XLU 1.39). That is not six independent judgements, it is
  one fact: the book is long into an 11.75% SPY drawdown. Expect several to close this week.

## [06:22 ET] POSITION UPDATE — UNP — close it, on the rule
- decision: **CLOSE** at Monday open, near flat (-0.5%)
- why: see audit. The published stop at 277.4 is 1.49 ATR from entry, below the 2.0 stock
  floor; widening it to a compliant 273.0 drops R:R to 1.76, under the 2.0 floor. The
  position cannot be made rule-compliant and profitable-by-its-own-numbers at once.
- this is NOT a view on Union Pacific. It is the floor applied retroactively to a position
  that should not have cleared it. Closing flat is the cheapest possible outcome.
- no earnings within 40 days (checked), so there is no gap risk forcing urgency.

## [06:23 ET] POSITION UPDATES — hold, levels unchanged, no recommendation emitted
Logged here so synthesis does not mistake silence for an oversight. None has earnings
inside 40 days (verified against the fetched calendar), so each stop can function.
- **OXY** 53.90, 2.03 ATR room, -17.02% off high, at range low (+1.2% off it). Hold.
- **XLU** 42.69, 1.39 ATR room, below SMA20 43.38. Bond proxy; the Dec 9 hike is the risk,
  but 89% priced. Hold, do not add.
- **ADM** 66.95, 1.16 ATR room, -22.51% off high and only 0.47% off its 45d low. Hold;
  weakest fundamental momentum of the longs but the stop is compliant and can work.
- **ABT** 103.00, flat, 1.96 ATR room. Hold. Stop 1.96 ATR from entry is a rounding
  breach, not worth paying a spread to fix.
- **PFE** 27.40, long_term, no stop by design. -12.85% off high. Hold.
- **CAG** 14.92, +3.6%, long_term, no stop by design. Above SMA20 14.77. Hold.
- **KHC** 25.39, +10.4%, 5.31 ATR room, above SMA20 — the one unambiguously working long.
  Hold; trim a third at 28.09 rather than reaching for more.
- **HII** 280.34, +7.0%, NO STOP on a swing-shaped position. Flagged in the audit above.

## [06:22 ET] POSITION UPDATE — HUN — hold, stop unchanged (logged, not captured)
- 8.36, -7.1% vs 9.0 entry, stop 8.09 = **0.69 ATR** of room (ATR 0.3936, 4.71% of price).
  -18.0% off the 45d high; SMA20 9.364. Avg daily dollar volume $23.5M — thin but well
  clear of the $500K floor; small-cap dilution and halt risk apply.
- decision: HOLD, stop unchanged at 8.09. No earnings inside 40 days, so the stop can
  function rather than being gapped through (the DKS problem). Reasoning is identical to
  RTX, so no separate recommendation is emitted — this line is the record of the decision.
- NOT widening it: R:R at entry was exactly 2.00, the bare minimum, so there is no slack
  to give away and a wider stop would drop it below the floor.

## [06:22 ET] VZ — captured, conviction 4 — the second genuinely new idea
- 46.48 close = **9.33x** trailing four-quarter EPS of **$4.98** (1.31+1.30+1.28+1.09).
- Relative strength is the core evidence and it is persistent, not a one-month flinch:
  | Window | VZ | SPY | XLC (own sector) |
  | --- | --- | --- | --- |
  | 1m | **+2.83%** | -9.71% | -6.88% |
  | 3m | -7.32% | -9.65% | -10.94% |
  | 6m | -3.87% | -7.49% | -13.36% |
  Source: scripts/market_data.py relstrength VZ --peer XLC
- Above SMA20 (45.47) AND SMA50 (45.83) while SPY sits 7.8% below its own 20-day.
- ATR14 0.9776 = **2.1% of price, the lowest of anything screened today** — which is why
  the floors work here and failed on ADI (6.52%) and DLTR (4.52%): a low-ATR name needs a
  small target to clear 2.0 R:R. Stop 43.9 = 2.15 ATR below the 46.0 entry; target 51.0
  is **1.29% BELOW** the 45d high of 51.665. R:R **2.38**, nothing stretched.
- win_probability 0.42 vs 0.296 baseline = 12.4 pts of claimed edge.
- Insiders: 0 open-market buys, 0 distinct buyers (absence is not a negative).
- Honest weakness, stated in key_risk: VZ is heavily indebted into an 89%-priced hike,
  and only 2 of 4 beats — materially weaker than CVS's 4 of 4.
- Diversification: telecom, no overlap with the healthcare (3), defence (2) or staples
  clusters already in the book.

## [06:23 ET] VENUE CHECK — Robinhood event contracts, verified not remembered
- Robinhood's prediction markets are Kalshi-backed (KalshiEX LLC) and offered through
  Robinhood Derivatives LLC; the Economics category covers **Fed interest rate decisions,
  CPI prints, nonfarm payrolls and GDP**, with monthly CPI/inflation contracts listed
  through 2026 (e.g. "Inflation in November 2026 (CPI YoY)").
- Sources: https://robinhood.com/us/en/prediction-markets/economics/indicators/ ,
  https://robinhood.com/newsroom/robinhood-prediction-markets-hub ,
  https://robinhood.com/us/en/policy/futures-and-event-contracts
- CAVEAT: the pages the search surfaced are mixed-date snapshots, several for contracts
  that have already settled. The *categories* are verified; any specific ticker must be
  confirmed in the app before trading. Fee noted: ~$0.01/contract commission.
- So the Fed and CPI markets I priced ARE on-venue. The reason none is recommended is
  edge, not availability — see below.

## [06:23 ET] NO EVENT CONTRACT TODAY — a decision, not an oversight
Event contracts are explicitly wanted by config/universe.md and I am publishing none.
Reasoning, so synthesis reports it as a deliberate call:
- The Dec 9 FOMC book is the one market where I have a confident read, and the read is
  that it is **efficiently priced**: 89-90c hike / 7-8c hold. To trade it I must assert a
  probability disagreement with a mechanism, and the only mechanism available ("Friday's
  crash makes the committee blink") is contradicted by the closest precedent, Dec 2018,
  when the Fed hiked into a ~15% drawdown. That is a hunch = conviction 1 = unpublishable.
- CPI markets are on-venue and dated, but I have no differentiated inflation forecast —
  FRED gives me the Oct index level (337.476) and nothing that beats consensus. Buying an
  event contract without a probability estimate of my own is the "feels underpriced"
  thesis universe.md prohibits.
- A defined-payoff instrument does not make a weak view safe; it makes it precise.

## [06:23 ET] NO CRYPTO IDEA TODAY — also a decision
config/strategy.md says a weekend run should lean toward crypto since it is the only open
market, and I am still publishing nothing there. Both directions fail honestly:
- **Long** fights the regime: the one macro fact I am confident about is an 89%-priced
  hike, and BTC is the purest liquidity-beta asset on the board.
- **Short** is chasing: BTC is -29.6% off its 60-day high on the ninth down day of twelve
  and bounced +5.16% in the last 24h. Every honest construction failed the floors — see
  the 06:10 block.
- The whole complex moved +2.8% to +5.3% in 24h together (BTC, ETH, SOL, XRP, DOGE, ADA,
  LINK, AVAX, LTC), so it is one beta bet with nine tickers, not nine ideas. Under the
  correlation cap that is at most one position, and I could not build that one honestly.

## [06:24 ET] SELF-CHECK — every published number, recomputed before handoff
Reward-to-risk and the `1/(1+R:R)` break-even baseline, recomputed from the captured
entry/target/stop rather than from anything I asserted:
| Sym | R:R | floor | baseline | claimed wp | edge (pts) |
| --- | --- | --- | --- | --- | --- |
| IWM | 2.27 | 2.0 | 0.306 | 0.45 | 14.4 |
| XLV | 2.12 | 1.8 etf | 0.320 | 0.40 | 8.0 |
| TLT | 2.67 | 1.8 etf | 0.273 | 0.40 | 12.7 |
| CVS | 2.53 | 2.0 | 0.283 | 0.42 | 13.7 |
| KHC | 2.83 | 2.0 | 0.261 | 0.48 | **21.9 — over the 20pt line** |
| RTX | 2.12 | 2.0 | 0.321 | 0.38 | 5.9 |
| HII | 3.31 | 2.0 | 0.232 | 0.40 | 16.8 |
| VZ | 2.38 | 2.0 | 0.296 | 0.42 | 12.4 |
All clear their floor. Stop distances in ATRs, all clearing the asset-scaled floor:
IWM 2.23 (1.8), XLV 2.06 (1.8), TLT 1.91 (1.8), CVS 2.17 (2.0), KHC 2.28 (2.0),
RTX 2.22 (2.0), HII 2.00 (2.0), VZ 2.15 (2.0).

**Two things flagged deliberately for the red team, not accidents:**
1. **KHC claims 21.9 points of edge, over the 20pt large-claim line.** I am leaving it
   rather than trimming the number to dodge the flag. Reason: the baseline is derived from
   the *entry* R:R, and KHC is a filled position already +10.4%. From the actual 25.39
   price it is 2.70 from target and 4.19 from stop, so touching the target first is more
   likely than not and 0.48 is if anything conservative. The flag is an artifact of
   measuring a live position from its entry. Lower it if you disagree — do not let me
   nudge it to 0.45 just to pass.
2. **DKS and UNP carry `direction: "sell"`, `stop: null`, `win_probability: null`.**
   These are **exits of existing longs**, not short recommendations and not new ideas.
   config/universe.md lists buy/sell_short for Robinhood Stocks, so `sell` is the schema's
   generic exit; there is no stop or win probability because the instruction is to be flat.
   position_size_pct is 0 for the same reason. If validation flags a missing stop on
   these two, that is the flag misreading an exit as an entry.

## [06:24 ET] CONVICTION — scored at or below what the evidence supports, never above
Distinct evidence kinds vs claimed score (table in config/strategy.md: 1 kind=2, 2=3,
3=4, 4+=5):
- IWM 4 kinds (supports 5) -> claimed **4**. DKS 4 kinds (supports 5) -> claimed **4**.
- CVS 3 (supports 4) -> **4**. VZ 3 (supports 4) -> **4**. UNP 2 (3) -> **3**. KHC 2 (3) -> **3**.
- XLV 3 (supports 4) -> claimed **3**. TLT 3 (4) -> **3**. RTX 3 (4) -> **3**. HII 3 (4) -> **3**.
Four ideas are scored one BELOW what the kind-count supports. That is intentional, not
sloppiness: on XLV, TLT, RTX and HII the third kind is `counter_argument_answered` or a
relative-strength read that leans on data already counted under another kind, and
CLAUDE.md is explicit that reusing one fact is one confirmation. Given this book has a
realised 11% hit rate, erring low on conviction is the correct direction of error.
No idea anywhere claims more than its evidence supports.

## [06:24 ET] CORRELATION CAP — checked across the 10 captured ideas
Cap is 3 ideas per driver (config/strategy.md).
- **Healthcare: 3** — XLV, CVS, plus ABT already open. **At the cap.** This is why no
  fourth healthcare name was pitched despite the sector being the day's leadership.
- **Defence: 2** — RTX, HII. Room for one more, not taken.
- **Staples: 1 captured** (KHC) + CAG, ADM open = 3. At the cap.
- **Short/duration hedges: 2** — IWM short, TLT long. These offset the longs rather
  than adding to them.
- **Telecom: 1** — VZ. The only genuinely uncorrelated new exposure added today.
- **Exits: 2** — DKS, UNP. Reduce gross exposure; no driver added.
No single macro print carries more than 3. The Dec 9 FOMC touches nearly everything, but
in opposite directions (IWM short and TLT benefit from what hurts the longs), which is
the point rather than a violation.

## [06:24 ET] RESEARCH COMPLETE (first pass — budget remained, see addendum below)
- **candidates: 10** (reports/2026-11-22/candidates.jsonl), all schema-valid, unique symbols
  - 2 genuinely new ideas: **CVS** (conv 4), **VZ** (conv 4)
  - 6 position updates, levels unchanged unless stated: IWM, XLV, TLT, KHC, RTX, HII
    (HII is the one real change — a stop added where there was none)
  - 2 rule-driven exits: **DKS** (earnings Monday, stop unenforceable), **UNP** (stop
    below the ATR floor and fails R:R at a compliant stop)
  - 2 cancellations of stale unfilled orders, logged not captured: GLD @406.77, /MBTZ6 @74,075
- **watchlist candidates (researched, deliberately not recommended):** ADI and DLTR —
  both failed the floors honestly; conditions to wait for are in the 06:16 blocks.
- **the day's framing, for synthesis:** Friday 2026-11-20 was a correlated liquidation
  (SPY -3.64% on 2.9x volume closing on the low, QQQ -5.67% and -20.2% off its high,
  GLD -3.67%, TLT the only major asset up, HYG only -0.26% so credit did NOT crack), and
  the regime behind it is a **Fed hike priced at 89% for Dec 9**. The open book is 13 longs
  into that. Five of fifteen positions sit under 1.4 ATR from their stops; expect several
  to close this week. That is the honest headline, not any single new idea.
- **coverage gaps / sources that failed:**
  - `^GSPC ^NDX ^DJI ^RUT ^VIX`, ES/NQ futures, DXY, the 10Y quote, gold and WTI all
    returned ok:false — finnhub needs a CFD subscription for indices, Yahoo returned
    HTTP 429 all morning, stooq 404s on `^`-prefixed symbols, no alphavantage key. I used
    ETF proxies (SPY/QQQ/IWM/GLD/USO/UUP/TLT/HYG) and never stated an index level.
  - Kalshi's `/markets` summary endpoint returned null bid/ask/last for **every** market;
    all event prices came from `/markets/<ticker>/orderbook` instead. Worth fixing in
    `market_data.py events`, which currently reports prices as null and also matched
    sports parlays for the query "Fed".
  - `market_data.py implied` failed for DKS — Yahoo options returned HTTP 401. **No idea
    today was checked against the options-implied move.** That is a real gap.
  - `market_data.py short DKS` timed out (nasdaq read timeout, 20s). No short-interest
    read on any name today.
  - `market_data.py history BTC-USD` returned ok:false with no error string; used the
    coingecko market_chart endpoint directly.
  - Insider data returned 0 open-market buys for every name checked (CVS, VZ, ADI, DLTR).
    Treated as no confirmation rather than as a negative, per the skill.
  - **Everything equity/ETF here is the Friday 2026-11-20 official close.** Sunday run:
    that is a closed market, not stale data. Crypto is live. No same-day equity entries —
    all equity entries are for the Monday 2026-11-23 open.
  - Not reached: no sector-by-sector relative strength sweep beyond VZ/XLC; no 13F or
    ownership work; no read on the Tuesday AI-capex earnings block (ADI/DELL/HPQ/WDAY/
    ADSK/NTNX) beyond the ADI rejection, which is the week's highest-stakes event.

## [06:27 ET] ADDENDUM — budget remained after the first RESEARCH COMPLETE, so I kept going
Elapsed at first completion block: 23 of ~60 minutes. Used the remainder on the two gaps
I had just flagged: the Tuesday AI-capex earnings block, and retrying the dead sources.

### REJECTED — the whole Tue/Wed earnings block — DELL, HPQ, DE
Screened the week's highest-stakes reporters. All three fail, and for one shared reason.
| Sym | Reports | Last | % off 150d high | ATR% | Trailing EPS | P/E | Revisions | Beats |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DELL | Tue amc | 278.02 | **-53.31%** | **12.48%** | 18.38 | 15.1x | deteriorating -1.3 | 4/4 |
| HPQ | Tue amc | 27.96 | -22.82% | 4.04% | 3.32 | 8.4x | flat 0.0 | 3/4 |
| DE | Wed bmo | 609.25 | -15.53% | 3.27% | 18.00 | 33.8x | **improving +8.8** | 3/4 |
- **DELL**: unbuildable. A 2.0 ATR stop is 69.38 wide = **25% of the price**. Nothing
  honest clears the R:R floor against that. Down 53% from its high with revisions
  deteriorating is a falling knife, not a de-rating.
- **HPQ**: cheapest on the board at 8.4x, but **bullish share is 7.7% and flat** — that
  is not a contrarian setup, it is a declining PC/print business nobody is revising
  toward. Geometry is marginal anyway: stop 25.7, target 32.5, R:R **2.01**.
- **DE**: best revision momentum I measured all day (+8.8 points, 70.6% bullish), but
  33.8x trailing is a trough-cycle multiple I cannot defend as a valuation anchor without
  inventing a normalised earnings number. R:R also lands at exactly **2.00**. And ADM is
  already open in ag — correlation.

### The structural reason this week's best catalysts are untradeable
Worth recording, because it explains the shape of the whole report rather than one
rejection: **every dated catalyst available this week is an earnings gap, and an earnings
gap makes a stop unenforceable.** A 2.0 ATR stop is sized for an ordinary session; a print
routinely moves these names several ATRs at the open, so the stop is not touched at its
level, it is gapped through. That is the exact argument for exiting DKS, and it applies
identically to DELL, HPQ and DE as entries.
So the two new ideas today are deliberately the two names with **no earnings inside 40
days** — CVS and VZ — resting on valuation and measured relative strength instead of on a
dated event. That is the opposite of the usual instruction to prefer dated catalysts, and
it is a considered inversion for this specific week, not a failure to find catalysts.
A thin calendar would shift time to durable mispricings; a calendar full of *ungated* gap
risk should too.

### Dead sources, retried and confirmed dead
- `market_data.py short` retried on CVS, VZ and IWM: all three `ReadTimeout` against
  api.nasdaq.com (20s). Confirmed a sustained outage, not a blip. **No short-interest or
  days-to-cover read on any name today** — relevant because a crowded short is fuel under
  a long, and the IWM short idea in particular would be better evidenced with it.
- `market_data.py implied` remains unusable (Yahoo options HTTP 401), so **no idea today
  was checked against the options-implied move.** For CVS the target is a 25.6% move and
  for VZ 10.9%; I could not confirm whether the options market considers those ordinary.
  Both are flagged for the red team.
- Yahoo (HTTP 429) and finnhub indices (CFD subscription) both still failing.

## [06:28 ET] RESEARCH COMPLETE (final)
- **candidates: 10**, unchanged by the addendum — the extra time produced three
  well-evidenced rejections rather than new ideas, which is the correct outcome when the
  floors say so. Nothing was padded to use up budget.
- watchlist now: ADI, DLTR, HPQ, DE (DELL excluded — unbuildable, not merely unattractive).
- Ran 06:01-06:28 ET of a ~60 minute budget; closed with this block, so nothing was lost
  to the clock. All deadlines met: first candidate captured 06:19 against a 06:21 target.
