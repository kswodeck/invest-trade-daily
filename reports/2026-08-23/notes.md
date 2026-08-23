# Research log — 2026-08-23

## [06:28 ET] SETUP — weekend run (Sunday)
- US equities/futures closed. Per config/strategy.md weekend behavior: shift toward
  crypto + event contracts for actionable ideas; equities are week-ahead prep with
  entries marked for the next open (Mon 2026-08-25).
- Prior context read: 20 open positions, 8 awaiting entry, 3 closed trades (0/3, avg -2.4%).
  Sample of 3 is NOISE — will not over-fit to it. Noted.

## [06:28 ET] MACRO — rates, policy, tape
- Yahoo Finance rate-limited (HTTP 429) across the board this morning; stooq 404s on
  index symbols; finnhub refuses index CFDs. So: NO live quote for SPX/NDX/DJI/RUT/VIX/
  DXY/UST10Y/gold/WTI/ES/NQ from market_data.py macro. Recorded as a data gap.
- FRED (working): US10Y 4.69% (2026-08-20), US2Y 4.19% (2026-08-20),
  fed funds effective 3.63% (2026-08-20), 10y-2y curve +0.50 (2026-08-21),
  unemployment 4.1% (2026-07-01), CPI index 332.813 (2026-07-01).
  source: https://fred.stlouisfed.org
- Read-through: curve positively sloped +50bp, funds at 3.63% vs 10y 4.69% — long end
  is NOT pricing an easing cycle that crushes term premium. TLT 82.05 (-0.35%, close
  2026-08-21) sits near the low end of its recent range.
- TLT is an open position (BUY 82.60, 2026-08-20, now 82.05, -0.7%). Live.

## [06:29 ET] CRYPTO — live (24/7 market, this is the actionable class today)
- BTC $76,814, +0.26% 24h, vol $27.35B, mcap $1.542T — source: coingecko via market_data.py
- ETH $2,416.30, +0.89% 24h, vol $13.83B, mcap $291.6B
- SOL $93.88, +2.48% 24h, vol $4.54B, mcap $54.76B
- ETH/BTC = 0.03146. SOL/BTC = 0.001222.

## [06:29 ET] POSITION UPDATE — CRITICAL — BTC / /MBTU6 SHORTS ARE BLOWN OUT
- Four open bearish-BTC positions: BTC SELL @62,950 (08-16), BTC SELL @63,400 (08-17),
  /MBTU6 SHORT @64,100 (08-18), /MBTU6 SHORT @64,340 (08-19).
- BTC is now 76,814. Every one of those stops (65,200 / 65,200 / 66,600 / 66,600) was
  breached by a wide margin. These are -20% to -22% against entry.
- The short-BTC thesis is DEAD and must not be re-pitched. Priority action item today.

## [06:33 ET] CALENDAR — earnings inside the next 10 sessions (finnhub, 261 names)
Dated catalysts that matter for week-ahead positioning (all ET):
- Mon 08-24 bmo: PDD ($18.40 est), XPEV; DKS ($3.80), PVH, TUYA amc
- Tue 08-25 amc: INTU ($3.65), ZM ($1.52), BOX, NCNO, SMTC, HEI; bmo WSM ($2.08), JKS; ANF, FIVE, KSS, GES
- Wed 08-26 amc: **NVDA ($2.13 EPS / $93.6B rev est)** — the week's dominant event;
  CRM ($3.31), CRWD ($0.30), SNPS, VEEV, OKTA, NTNX, HPQ, URBN, A; bmo BBWI, DCI, DY, SJM, PLAB, NAT, SFL; BURL, GMS, OLLI
- Thu 08-27 amc: MRVL ($0.94), ADSK, WDAY, ULTA ($6.29), ESTC, GAP, AFRM, S, RBRK, IREN;
  **bmo DG ($2.06 / $11.53B)** — DG is on the awaiting-entry list @119; BBY, HRL, HQY, BILI, CSIQ, TITN, MBUU
- Mon 08-31 bmo: FRO ($2.57); AEO, ASO, SAIC
- Tue 09-01 amc: PANW ($0.99); MDB, GTLB, DLTR, M, MDT, NIO, CRDO
- Wed 09-02 amc: **AVGO ($3.30 / $29.9B)**, **LULU ($1.84 / $2.51B)** (awaiting-entry @115),
  SNOW, HPE, NTAP, GOLD (Barrick); AGX, AI, CAL, ZUMZ
source: finnhub earnings calendar via scripts/market_data.py earnings --days 12
- CORRELATION NOTE: NVDA/AVGO/MRVL/CRDO/SNPS all resolve on the same AI-capex driver.
  Cap at 3 ideas depending on it per config/strategy.md.

## [06:33 ET] PRICES — Friday 2026-08-21 close (finnhub, session=closed, age ~38h)
- SPY 765.72 (+0.41%), QQQ 713.44 (+0.35%), IWM 299.96 (+0.77% — small caps led)
- TLT 82.05 (-0.35%), GLD 423.36 (**+1.95%**), XLE 63.64 (-0.17%)
- Open positions: CCJ 102.51 (**+7.24% Friday**), NKE 40.76 (+1.37%), PFE 28.07 (+1.01%),
  DHT 19.82 (+0.10%), HD 335.61 (+0.33%), LCII 101.98 (-3.28%), BCC 82.47 (+0.86%),
  TJX 140.53 (-0.11%), KRE 74.86 (+0.20%)
- GLD @423.36 has run away from the awaiting-entry level of 398 (published 08-22) by 6.4%.
  That order will not fill; needs re-levelling or dropping, not repeating.

## [06:47 ET] EVENT MARKETS — Kalshi FOMC ladder (the key macro read of the day)
Fetched directly from api.elections.kalshi.com (market_data.py `events` keyword search
returns 0 — it only filters the first 200 open markets, which are all sports parlays.
Workaround: query by event_ticker. Recorded as a tooling gap.)
- **KXFEDDECISION-26SEP (FOMC Sep 16 2026)**: Hike 25bp bid/ask **31/32c** (vol 2.78M, OI 1.74M);
  Hold 0bp 67/68c (vol 4.92M, OI 3.51M); Cut 25bp 0/1c; Cut >25bp 0/1c; Hike >25bp 0/1c
- KXFEDDECISION-26OCT (Oct 27-28): Hike 25bp 23/24c; Hold 71/73c; Cut 25bp 2/4c
- KXFEDDECISION-26DEC (Dec 8-9): Hike 25bp 23/28c; Hold 67/68c; Cut 25bp 7/9c
- **Regime read: the market prices essentially ZERO chance of a cut this year and a
  ~31% chance of a HIKE in September.** This is a hawkish/re-accelerating-inflation tape,
  not an easing cycle. Everything today must be framed against that.
- Corroborating: gold +1.95% Fri and +14% in three weeks; BTC +22% in a week; 10y 4.69%
  vs funds 3.63%; curve +50bp. Gold rallying INTO rising hike odds = debasement/inflation
  bid, not a rate-cut bid. That distinction matters for which gold expression works.
- Caveat to carry: Robinhood Prediction Markets carries a subset of Kalshi. KXFEDDECISION
  was published by this report on 2026-08-22, so it is carried. Others need verification.

## [06:48 ET] REJECTED — GLD long — fails the long_term 2.5 R:R floor on honest levels
- Levels (nasdaq, 120d to 2026-08-21): close 423.36, ATR14 7.94 (1.87%), SMA20 392.64,
  SMA50 383.03, 120d range 363.32-481.31, -12.0% off high.
- Price is 7.8% above SMA20 after a +14% three-week run (371.54 on 07-31 -> 423.36).
- Best honest construction: accumulate ~398 (the old published level), bear case 363
  (the 120d low), target 481 (the 120d high) => R:R 2.37. Under the 2.5 long_term floor.
- Chasing at 423 is worse: entry 412 / bear 363 / target 481 => R:R 1.41.
- GLD has been recommended 4x in 10 days and the 398 order never filled; the level is now
  6.4% below market. Not re-pitching it. Target would have to be reverse-engineered to pass,
  which config/strategy.md explicitly forbids.

## [06:52 ET] CAPTURED — CCJ — position update (continuing, not new)
- Opened 08-17 @95.00, added 08-18 @88.00; now 102.51 (+7.9% vs first entry).
- Friday 08-21: +7.24% on 3.94M shares vs ~2.3M average — volume-confirmed breakout
  through both SMA20 (94.24) and SMA50 (96.14) out of a 94-99 August base.
- Levels: ATR14 3.56 (3.47%), 120d range 83.15-131.21, -21.9% off the high.
- decision: HOLD. Add the last third only on a pullback into 92-100. Do not chase.
- bear case 83 (120d low), target 135 => R:R 3.0 from a 96 add. Clears the 2.5 long_term floor.
- Still to confirm: what drove Friday's move. No filing checked yet.

## [06:52 ET] LEVELS — the week's other majors (nasdaq, 120d, through 2026-08-21)
- NVDA 214.72 | ATR14 5.75 (2.68%) | SMA20 213.18 | SMA50 207.58 | range 164.27-236.54 | -9.2% off high
  Note: NVDA has fallen five sessions running into its 08-26 print (225.01 -> 214.72).
- DG 123.41 | ATR14 3.50 (2.84%) | SMA20 124.15 | SMA50 120.27 | range 99.57-155.51 | -20.6% off high
  DG is on the awaiting-entry list @119 and reports 08-27 bmo. Price never reached 119.
- TLT 82.05 | ATR14 0.66 (0.80%) | SMA20 82.53 | SMA50 84.17 | range 81.17-89.67 | -8.5% off high
  TLT is 1.1% off its 120-day LOW. Open BUY @82.60 from 08-20, stop 80.95.

## [06:56 ET] MACRO — THE WEEK AHEAD IS THE STORY (Aug 24-28)
- **Jackson Hole symposium runs Thu 2026-08-27 to Sat 08-29.** Theme: financial innovation
  and its implications for payments and policy.
- **Fed Chair Kevin Warsh delivers his first Jackson Hole keynote Fri 2026-08-28, ~10:00 ET**
  (prepared remarks post to the KC Fed site and cross the wires at that time). Warsh took
  office 2026-05-22; this is his debut as Chair at the symposium.
  sources: https://www.bloomberg.com/news/articles/2026-08-22/kevin-warsh-to-make-first-jackson-hole-speech-as-fed-chair
           https://www.regardsofwallstreet.com/news/jackson-hole-2026-dates-schedule-warsh-first-speech
           https://www.techtimes.com/articles/325228/20260821/jackson-hole-2026-what-watch-when-warsh-steps-podium-friday.htm
- **The 30-year Treasury yield surged to multi-decade highs last week** and CNBC's week-ahead
  frames the risk as bond-market turbulence "finally washing up to reach stocks."
  source: https://www.cnbc.com/2026/08/21/stock-market-next-week-outlook-for-aug-24-28-2026.html
  (article itself returns HTTP 403 to WebFetch — quoting the search-result summary only.)
- Fed funds futures: ~60% chance of a HOLD at 3.50-3.75%, up from ~45% a week earlier —
  i.e. futures put hike odds near 40%, vs Kalshi's 31/32c. Polymarket shows "no hike in 2026"
  at 53% vs "yes" 47%. source: https://finance.yahoo.com/economy/policy/articles/odds-fed-rate-hike-fall-083935313.html
- So: three separate venues price a live, roughly one-in-three-to-one-in-two chance of a
  RATE HIKE. There is no easing cycle in this tape.
- The five-day stretch stacks: NVDA earnings (Wed 08-26 amc), Jackson Hole (Thu), the Fed's
  preferred inflation report (PCE) and Warsh (Fri). Event risk is concentrated late-week.

## [06:56 ET] NEWS — CCJ, the Friday +7.24% driver (confirms the capture above)
- Drivers reported: nuclear-sector optimism tied to datacenter/AI power demand; Cameco's
  updated outlook for stronger realized pricing; 2026 production guidance held UNCHANGED
  despite temporary disruptions at Key Lake, McArthur River and Cigar Lake; raised 2026
  revenue/realized-price/cost outlook on a higher uranium spot price and a stronger USD;
  plus strategic value in Westinghouse and its proposed IPO path. RBC raised its target.
  sources: https://www.tradingkey.com/news/market-movers/262125359-market-movers-ccj-20260821
           https://www.quiverquant.com/news/Cameco+Gains+as+Investors+Focus+on+Higher+Uranium+Pricing+and+Nuclear+Growth+Signals
           https://www.investing.com/news/analyst-ratings/rbc-capital-raises-cameco-stock-price-target-on-uranium-strength-93CH-4765731
- Read-through: the move is fundamentally sourced, not a squeeze. The "hold, add on pullback"
  decision stands. A Westinghouse IPO is a discrete, un-dated catalyst worth tracking.

## [06:56 ET] POSITION UPDATE — TLT — open BUY @82.60 (08-20), now 82.05, stop 80.95
- TLT is 1.1% off its 120-day low and below both SMA20 (82.53) and SMA50 (84.17).
- The 30y is at multi-decade highs and hike odds are ~31-40%. This position is long duration
  into a hawkish Chair's debut keynote and a PCE print in the same 24 hours.
- decision: DO NOT ADD. The thesis is a rate-cut/duration bid that the tape and three
  separate prediction venues say is not happening. Keep the 80.95 stop; it is 1.3% away and
  Friday 08-28 can cover that before lunch. To be captured as an explicit reduce/avoid.

## [06:30 ET] CORRECTION — timestamps above
Entries above were labelled 06:47-06:56 from my own estimate of elapsed time rather than
from `date`. The real clock is 06:30 ET; the run started 06:26. Everything above was
logged between 06:26 and 06:30. Timestamps from here are read from `date`.

## [06:31 ET] MACRO — inflation is the reason hike odds are live
- **PCE price index 3.7% YoY, core PCE 3.3% YoY** as of the 2026-07-30 release (headline
  down from 4.1%, core down from 3.4%; both matched forecast).
  source: https://www.bea.gov/data/personal-consumption-expenditures-price-index
          https://www.investing.com/economic-calendar/core-pce-price-index-905
- Core at 3.3% against a 2% target, with fed funds effective at 3.63%, puts the real policy
  rate near zero. That is the arithmetic behind a 31-40% hike probability and behind gold
  at +14% in three weeks.
- Next PCE release date needs confirming — one source says Wed 2026-08-26 08:30 ET, CNBC's
  week-ahead implies it lands in the 08-24/08-28 window. Verifying against BEA directly.

## [06:32 ET] CALENDAR — CONFIRMED from BEA directly (this is the spine of the week)
- **Wed 2026-08-26 08:30 ET — Personal Income and Outlays, July 2026 (the PCE price index)
  AND GDP 2nd estimate + Corporate Profits, Q2 2026.** Both, same release slot.
  source: https://www.bea.gov/news/schedule
- **Wed 2026-08-26 after close — NVDA Q2 earnings** ($2.13 EPS / $93.6B rev est).
- **Thu 2026-08-27 — Jackson Hole opens.** Fri **2026-08-28 ~10:00 ET — Warsh keynote.**
- Next BEA release after that is 2026-09-03 (trade balance). Nothing in between.
- So the week is barbelled: everything macro lands Wed 08:30 and Fri 10:00, with the
  single largest equity event (NVDA) wedged between them Wed after the bell.
- PRACTICAL CONSEQUENCE: any swing idea entered Monday carries PCE + GDP + NVDA + Warsh
  before Friday's close. Position sizes should reflect that, and "wait for the print"
  is a legitimate action for most of them.

## [06:33 ET] LEVELS — precious metals complex is going parabolic (nasdaq, thru 08-21)
- GDX 102.83 | ATR14 3.84 (3.74%) | SMA20 85.83 | SMA50 80.42 | range 69.74-108.26 | **-5.0% off high**
  88.95 (08-18) -> 102.83 (08-21) = **+15.6% in three sessions**, on 22-44M shares vs a
  much lighter base. Price is **+19.8% above its 20-day and +27.9% above its 50-day.**
- SLV 62.72 | ATR14 1.84 (2.93%) | SMA20 56.65 | SMA50 55.64 | range 49.61-81.28 | -22.8% off high
  57.44 (08-18) -> 62.72 (08-21) = +9.2% in three sessions. +10.7% above the 20-day.
- GLD 423.36 (above): -12.0% off high, +7.8% above the 20-day.
- Shape of the complex: all three crashed from a spike high (GLD 481, SLV 81.28, GDX 108.26)
  down to a low (363 / 49.61 / 69.74) and are now V-recovering. **The miners have recovered
  furthest (-5% off high) while silver has recovered least (-22.8%).** Miners leading bullion
  is the signature of a real bull leg rather than a bounce.
- BUT: all three are stretched 8-20% above their 20-day averages after a three-day vertical.
  Buying any of them at Monday's open is chasing, and I am not going to dress that up.
  The tradeable question is whether the LAGGARD (silver) closes the gap, not whether the
  leader keeps running.

## [06:33 ET] LEVELS — other names in scope
- IWM 299.96 | ATR14 3.19 (**1.06% — unusually compressed**) | SMA20 298.60 | SMA50 296.68 |
  range 238.69-305.18 | -1.7% off high. Coiled just under the high on very low volatility.
- DHT 19.82 | ATR14 0.72 (3.64%) | SMA20 18.80 | SMA50 18.26 | -3.9% off high. Open +5.4%, working.
- NKE 40.76 | ATR14 1.15 (2.82%) | SMA20 41.49 | SMA50 42.49 | range 38.86-60.11 |
  **-32.2% off the 120-day high, only +4.9% off the low.** Below both averages. 58.7M shares
  on 08-17 (vs 14-22M since) looks like capitulation. Open positions @40.00 and @38.00.
- PFE 28.07 | ATR14 0.65 (2.31%) | SMA20 26.30 | SMA50 25.36 | range 23.62-28.745 |
  -2.4% off high, above both averages. Open @25.80 (08-18), +8.8%. Working.

## [06:35 ET] NEWS — what is actually driving the metals bid (this reframes the whole report)
- Spot gold ~$4,602.99/oz +1.86% Fri; spot silver ~$68.970/oz +1.29%. Gold at a 3-month high.
  sources: https://www.kitco.com/news/article/2026-08-21/gold-silver-extend-rally-dollar-slide-offsets-higher-yields-kitco-pm-report
           https://www.forbes.com/sites/conormurray/2026/08/21/gold-reaches-highest-price-in-three-months-as-dollar-weakens/
- **The driver is fiscal, not monetary.** US debt has topped $40 trillion and the Treasury made
  an UNEXPECTED announcement increasing long-term bond repurchases (buybacks) to try to cap
  rising borrowing costs. That revived debasement fears and is what gold is repricing.
  sources: https://www.advisorperspectives.com/articles/2026/08/21/gold-jumps-treasury-buybacks-concerns
           https://www.usagold.com/daily-precious-metals-market-report-august-21-2026/
- Dollar index has fallen **below 99.00**; a weaker dollar is the second leg of the bid.
- Third leg: the latest CPI came in **cooler than expected**, which dampened rate-hike
  expectations and removed a headwind that had suppressed gold for much of 2026.
  source: https://www.cnbc.com/2026/08/12/gold-prices-metals-fed-rate-hike-inflation.html
- Gold/silver ratio = 4602.99/68.97 = **66.7**.
- Note the tension worth trading: gold is rallying on a Treasury *buyback* of long bonds while
  the 30y yield sits at multi-decade highs. Buying back duration while the long end sells off
  is exactly the fiscal-dominance picture that bids gold and pressures the dollar.

## [06:37 ET] MACRO — the July CPI print, exactly (this is the anchor for the Fed trade)
- July 2026 CPI: **+0.1% m/m seasonally adjusted, +3.4% y/y, down 0.1pp from June.**
  All readings IN LINE with the Dow Jones consensus — not, as some secondary write-ups
  claimed, "cooler than expected." Correcting my 06:35 note on that point.
  sources: https://www.cnbc.com/2026/08/12/cpi-inflation-report-july-2026.html
           https://www.bls.gov/news.release/archives/cpi_08122026.htm
- Zandi: "a very benign report, right down the strike zone." The energy-fuelled burst earlier
  in 2026 is easing. +0.1% m/m annualises to ~1.2%.
- **On the 08-12 release, traders cut September hike odds to 42%.** Kalshi now prices 31/32c.
  So the odds have already fallen 42% -> ~31% over the last seven sessions.
  source: https://www.kiplinger.com/investing/economy/cpi-report-july-2026-what-to-expect
- Inflation stack: CPI 3.4% y/y and falling; core PCE 3.3% and falling; headline PCE 3.7%
  from 4.1%. Fed funds effective 3.63%. Unemployment 4.1%. Real policy rate ~+0.2%.
- My read: every inflation series is DECELERATING. A committee does not open a hiking cycle
  at the meeting immediately after a +0.1% m/m CPI. I put the September hike at 18-22%,
  against 31-32% priced.

## [06:39 ET] INSIDERS — checked on every equity finalist (finnhub, 6-month window)
- **PFE: 3 open-market buys, 3 distinct buyers, $2.96M bought vs $0.13M sold, net +$2.83M.**
  - **Albert Bourla (CEO) 38,000 sh @ $26.34 on 2026-08-12**
  - Mortimer J Buckley (director; former Vanguard CEO) 37,632 sh @ $25.52 on 2026-08-05
  - Ronald E Blaylock (director) 39,231 sh @ $25.46 on 2026-08-05
  This is a genuine cluster — three separate people, all inside the last three weeks, all
  open market. PFE now 28.07, i.e. 6.6% above the CEO's own fill.
- **NKE: 5 open-market buys, 4 distinct buyers, $3.73M bought vs $1.20M sold, net +$2.53M.**
  - Elliott Hill (CEO) 47,320 sh @ ~$42.27 on 2026-04-13 (two tickets)
  - **Timothy D Cook (director) 25,000 sh @ $42.43 on 2026-04-10**
  Real, but four months stale and both are underwater at 40.76.
- DG: zero open-market buys in six months. Absence is not a negative, per the brief.
- DHT: zero buys, one sale ($0.56M). Neutral-to-nothing.

## [06:39 ET] NEWS — NKE, why it is down 32% (context for the open position)
- Closed $39.09 on 2026-08-17, a **12-year low**, and is **-38.6% YTD**.
- Causes: Greater China FY26 revenue **-11% y/y** with DTC digital **-29%**; a sector-wide
  hit from On Holding's weak revenue guidance; downgrades from JPMorgan and UBS; and the
  P&L cost of the 'WinNow' turnaround programme.
  sources: https://finance.yahoo.com/markets/stocks/articles/nike-falls-12-low-selling-144808603.html
           https://www.schaeffersresearch.com/content/news/2026/08/04/nike-stock-downgraded-on-financial-concerns
           https://www.fool.com/investing/2026/08/18/nike-just-hit-a-12-year-low-is-the-bottom-near/
- Honest read on the open NKE position: the CEO and Tim Cook bought at 42.3-42.4 in April and
  are underwater. The existing targets of 62-65 imply +52-60% and are not defensible on
  anything I can source today. This needs to be re-levelled downward, not repeated.

## [06:45 ET] REJECTED — ZYME pre-PDUFA buy — the binary arithmetic does not clear 2.0
- Real, dated catalyst: **FDA PDUFA action date Tue 2026-08-25** for zanidatamab in 1L
  HER2+ locally advanced/metastatic gastroesophageal adenocarcinoma (sBLA, priority review,
  partner Jazz). US approval pays Zymeworks a **$250M milestone**, first of up to **$440M**
  in global regulatory milestones, plus a step-up in Ziihera royalties.
  sources: https://ir.zymeworks.com/news-releases/news-release-details/zymeworks-provides-corporate-update-and-reports-second-quarter-3
           https://www.globenewswire.com/news-release/2026/08/06/3340764/0/en/zymeworks-provides-corporate-update-and-reports-second-quarter-2026-financial-results.html
- Levels: 28.67 close, +7.9% Friday on 836K sh (vs 330-650K base), ATR14 1.18 (4.11%),
  SMA20 24.26, SMA50 24.32, 120d range 21.52-29.75, only -3.6% off the high.
  **25.12 (08-14) -> 28.67 (08-21) = +14.1% in six sessions, straight into the date.**
- Market cap ~$2.15B. The week's ~$270M of market-cap gain is approximately the $250M
  milestone. The event is largely in the price.
- Honest binary math from 28.67: approval reaction +15-25% => ~33-36; CRL or a review
  extension => -25-35% => ~19-21. Entry 28.67 / target 35 / stop 22 gives reward 6.33 against
  risk 6.67 = **R:R 0.95**. That is under the 2.0 swing floor and not close.
- The only way it passes is an entry near 25.5, which will not print before Tuesday.
- Watchlist, not a recommendation: revisit AFTER the 08-25 decision.
- Extra reason for caution, from the same sweep: SVRA's 08-22 PDUFA was extended three
  months. PDUFA dates slip, and a slip on ZYME here is a -25% day.

## [06:45 ET] SVRA — the PDUFA slipped, and that is the setup rather than the problem
- MOLBREEVI (molgramostim inhalation, GM-CSF via eFlow nebuliser) for autoimmune pulmonary
  alveolar proteinosis. Priority review, original PDUFA 2026-08-22.
- **FDA extended the review by three months to 2026-11-22**, deeming Savara's responses to
  information requests a major amendment. **The agency did not cite safety, efficacy or
  manufacturing concerns.** Phase 3 IMPALA-2 was positive; aPAP has no approved therapy.
  sources: https://www.investing.com/news/company-news/fda-extends-review-of-savaras-molgramostim-application-93CH-4616427
           https://investors.savarapharma.com/news/news-details/2026/Savara-Announces-the-U-S--Food-and-Drug-Administration-FDA-Filed-the-MOLBREEVI-Biologics-License-Application-BLA-in-Autoimmune-Pulmonary-Alveolar-Proteinosis-Autoimmune-PAP/default.aspx
- Levels: 5.59, ATR14 0.269 (4.82%), SMA20 5.50, SMA50 5.67, 120d range 4.695-6.475,
  -13.7% off the high. Friday volume 3.04M vs a 1.2-1.6M base.
- Shape: an administrative delay on a drug the FDA has not criticised, with a new dated
  catalyst 91 days out. Checking market cap, cash and burn before capturing.

## [06:39 ET] CAPTURED — SVRA (conviction 2, lottery-sized) — see notes above.

## [06:40 ET] REJECTED — SLV / silver catch-up — the ratio already went the other way
- Spot silver $68.97. **Silver set a record near $121/oz in late January 2026**, so the metal
  is -43% from its record, not cheap-and-forgotten. The 120-day picture (SLV -22.8% off its
  high) understates how far it already ran.
- **Gold/silver ratio is 66.7 and has fallen below 67 — its lowest since June 2021.** JPMorgan
  expects the physical market to *normalise the ratio back toward 70* over H2 2026, i.e.
  silver UNDERPERFORMING gold from here. My "the laggard closes the gap" hypothesis from
  06:33 is simply wrong; silver is the one that already outperformed.
- JPMorgan's end-2026 silver forecast is **$63.78** and the bank consensus range is $56-88.
  Spot at $68.97 is already ABOVE the central forecast.
  sources: https://www.jpmorgan.com/insights/global-research/commodities/silver-prices
           https://www.canadianminingreport.com/blog/silver-may-see-wild-volatility-in-2026-instead-of-steady-gains-warn-experts-amid-sixth-deficit
- The bull case is real but long-dated: a record **215 Moz** global supply deficit in 2026,
  the sixth consecutive deficit, ~820 Moz cumulative 2021-2026, and ~700 Moz of industrial
  demand from solar, EVs and datacenters. Against that, silver-thrifting in solar cells is
  spreading fast enough that solar silver demand could fall ~30% this year.
- Conclusion: no edge at $68.97 with the ratio at a five-year low and spot above consensus.
  Not captured. The whole precious complex stays a REJECT today on price, not on thesis.

## [06:41 ET] NEWS — BTC: what actually ran over the short positions
- BTC +23% over the past week to ~$77.5k intraweek; now $76,814 (coingecko, live).
- **US spot bitcoin ETFs took ~$1.6B of net inflows Mon-Thu, the strongest week of 2026**,
  including $606M on 08-20 alone and four consecutive days of net inflows.
- **More than $4.3B of crypto short positions were liquidated** as BTC broke higher —
  the first leg was forced buying, not fresh conviction.
- **Treasury Secretary Scott Bessent announced plans to DOUBLE long-term bond buybacks**,
  which pushed long yields down initially and weakened the dollar, bidding BTC and gold.
  sources: https://www.benzinga.com/etfs/sector-etfs/26/08/61368272/bitcoins-rally-is-shifting-from-short-squeeze-to-etf-demand-as-inflows-hit-1-6-billion
           https://crypto.news/bitcoin-price-breaks-76k-as-etf-inflows-accelerate/
           https://www.altcoinbuzz.io/bitcoin-price-surges-above-76000-rally
- **This is the SAME catalyst that bid gold** (see 06:35). Gold, BTC and any dollar-short are
  one trade this week, not three. The correlation cap in config/strategy.md binds here.

## [06:41 ET] POSITION UPDATE — BTC and /MBTU6 SHORTS — CLOSE ALL FOUR. DECISION: EXIT.
- Positions: BTC SELL @62,950 (08-16), BTC SELL @63,400 (08-17), /MBTU6 SHORT @64,100 (08-18),
  /MBTU6 SHORT @64,340 (08-19). Stops 65,200 / 65,200 / 66,600 / 66,600.
- BTC is 76,814. **Every stop was breached days ago; on any honest accounting these are
  already closed at the stop.** Marked-to-market they are -20% to -22%.
- decision: **CLOSE. Do not re-establish a short.** The bear thesis has been falsified by a
  named, dated, non-technical catalyst — Treasury doubling long-bond buybacks, a weaker
  dollar, and $1.6B of genuine ETF inflows. That is not a positioning wobble.
- I am NOT flipping long at 76,814 either. Two of the three legs of this rally (a $4.3B short
  liquidation cascade and a policy headline) are one-off. Chasing +23% in a week is how the
  short got run over in the first place, in reverse.
- action: flat BTC. Revisit only on a retest of the 64-66k breakout shelf, which is where the
  shorts were and where real support should now be.

## [06:43 ET] LEVELS — energy, tankers, consumer (nasdaq, thru 08-21)
- IBIT 43.68 | ATR14 1.08 (2.46%) | SMA20 37.00 | SMA50 36.28 | range 32.84-46.56 | -6.2% off high
  36.60 (08-18) -> 43.68 (08-21) = **+19.3% in three sessions**, +18.0% above its 20-day.
  This is the equity proxy for the BTC squeeze and is not buyable here for the same reason.
- XLE 63.64 | ATR14 1.23 (1.94%) | SMA20 60.29 | SMA50 57.51 | range 52.62-64.70 | -1.6% off high
- DINO 97.32 | ATR14 3.66 (3.76%) | SMA20 89.89 | SMA50 81.58 | range 52.25-97.63 |
  **-0.3% off high** — i.e. AT the high. +4.96% Friday on 2.90M sh vs a ~2.0M base.
  Was an awaiting-entry at 93.00 from 08-22; never filled and is now 4.6% above it.
  Note the base: 52.25 to 97.32 is +86% inside 120 days.
- FRO 43.67 | ATR14 1.52 (3.47%) | SMA20 40.32 | SMA50 38.96 | range 29.82-45.17 | -3.3% off high.
  Reports **Mon 2026-08-31 bmo**, $2.57 EPS est. Same tanker driver as the open DHT position.
- LULU 121.07 | ATR14 4.15 (3.43%) | SMA20 121.17 | SMA50 117.63 | range 104.44-175.46 |
  **-31.0% off high.** +4.65% Friday. Awaiting-entry at 115.00 from 08-22, unfilled.
  Reports **Wed 2026-09-02 amc**, $1.84 EPS / $2.51B rev est.

## [06:43 ET] POSITION UPDATE — XLE — three open lots (08-15 @60.80, 08-16 @60.50, 08-18 @60.80)
- XLE 63.64, +4.7% to +5.2% across the lots, and 1.6% from its 120-day high.
- XLE has been recommended **5 times in 10 days**. That is the anchoring pattern the brief
  warns about, and nothing has changed today that justifies a sixth. decision: HOLD, do not
  add, raise stops to 60.30 (the 20-day) so the whole position is at worst flat.
- Not capturing a new XLE candidate. The energy slot today, if any, should be a different name.

## [06:47 ET] REJECTED — DINO / refiners — record cracks at all-time highs is the wrong entry
- **The US diesel crack spread crossed $100/bbl in August 2026 for the first time on record.**
  Refining equities (DINO, MPC, PBF, PSX, VLO) printed all-time highs on it.
  Valero's realised refining margin roughly doubled y/y; Marathon's R&M margin went from
  $17.58 to $36.33/bbl.
  sources: https://www.forbes.com/sites/garthfriesen/2026/07/23/refining-stocks-soar-as-crack-spread-hits-record-high-in-2026/
           https://energynewsbeat.co/diesel/diesel-margins-top-100-a-barrel-to-reach-record-high-as-supply-crunch-grows/
           https://247wallst.com/investing/2026/08/18/diesel-prices-breaking-records-3-refiners-turning-the-crisis-into-record-profits/
- Cause: renewed hostilities around the **Strait of Hormuz** plus sustained **Ukrainian drone
  strikes on Russian refining infrastructure**. Global refinery crude throughput averaged only
  **80.9 mb/d in July, ~5 mb/d below a year earlier.**
- **US gasoline prices are +98% in 2026 against WTI +44%.** The spread IS the trade, and it
  has already been taken.
- CNBC, 08-17: "Refiner stocks are on a nearly unprecedented run. History says it could end soon."
  source: https://www.cnbc.com/2026/08/17/refiner-stocks-are-on-a-nearly-unprecedented-run-history-says-it-could-end-soon.html
- DINO is at 97.32, 0.3% off its 120-day high, +86% off the 120-day low, and 8.3% above its
  20-day. Crack spreads are the most violently mean-reverting series in energy. Buying a
  record margin at a record price is the definition of chasing. The 93.00 level from 08-22
  is not re-pitched; it is stale and the setup has deteriorated, not improved.

## [06:47 ET] FALSIFICATION — this cuts against my own Fed-hold candidate. Logging it against myself.
- Gasoline +98% YTD and diesel cracks at a record $100/bbl in AUGUST is an inflation impulse
  that lands AFTER the July CPI (+0.1% m/m) that my KXFEDDECISION-26SEP-H0 thesis rests on.
- **The August CPI prints 2026-09-11, five days before the Sep 16 FOMC.** A hot energy-driven
  August print would spike hike odds days before resolution, with no time to recover.
- This does not kill the trade — core PCE excludes energy and is at 3.3% and falling, and the
  Fed has explicitly treated the 2026 energy burst as transitory. But it is the single most
  likely way to lose, it is dated, and it belongs in the recommendation.
- Action: re-capturing the Fed candidate with this named in key_risk and the Sep 11 CPI in
  the plan. Estimate trimmed from 80% to ~75% hold; the market is at 67-68, so the edge
  narrows but survives. Conviction stays 3.

## [06:44 ET] NEWS — VLCC rates are at all-time records. This is the strongest fundamental
## fact I have found today.
- **TD3C (Middle East Gulf -> China) VLCC earnings are above $520,000/day**, with Gulf-to-Asia
  fixtures reported near $470,000-$500,000/day. The normal baseline for this route is
  **$20,000-$60,000/day** — so roughly a TENFOLD spike.
  sources: https://www.lloydslistintelligence.com/resources/blog/strait-of-hormuz-brief-19-august-2026
           https://www.seatrade-maritime.com/tankers/vlcc-rates-near-470-000-a-day-for-fixtures-through-hormuz
           https://www.lloydslist.com/LL1157631/VLCC-rates-spike-yet-again-as-confusion-continues-to-reign-at-Strait-of-Hormuz
           https://breakbulk.news/vlcc-rates-shatter-all-time-records-as-hormuz-blockade-splits-freight-markets-in-two/
- Cause: intensified Iranian military activity in the **Strait of Hormuz**, through which
  roughly one fifth of global petroleum shipments transit. Ships are avoiding the strait;
  ship-to-ship transfer activity off Oman and Fujairah is rising. Rates are climbing DESPITE
  falling global oil exports, on import demand, record refinery margins, and fading
  expectations of a near-term resolution.
- Same root cause as the record diesel cracks logged at 06:47[sic 06:47 entry]. Hormuz is one
  driver expressing itself in two places, so tankers and refiners must count together against
  the correlation cap. I rejected the refiners on price; the tanker owners have not run as far.

## [06:44 ET] POSITION UPDATE — DHT — opened 2026-08-18 @18.80, now 19.82, +5.4%
- Levels: ATR14 0.72 (3.64%), SMA20 18.80, SMA50 18.26, 120d range 15.98-20.62, -3.9% off high.
- decision: HOLD and RAISE BOTH LEVELS. The original target of 22.50 and stop of 17.60 were set
  before VLCC spot earnings printed above $520,000/day. A pure-play VLCC owner earning ten
  times its normal rate is a different company for as long as it lasts.
- new stop 18.30 (below the 20-day at 18.80, about 2 ATR); new target 24.50.
- why: the fact changed, not the price. Capturing via add_candidate.py.

## [06:48 ET] POSITION UPDATE — the remaining open book, decided one by one
Levels are nasdaq 120-day through 2026-08-21.

- **TJX** (entry 150.85 on 08-19, stop 145.50) — 140.53. **ALREADY STOPPED OUT**, and prior
  context shows an earlier TJX lot stopped on 08-19 too. Price 140.53 against a 120-day low of
  139.31 and a 20-day of 154.72 — it has fallen a full 9% below its own 20-day average.
  decision: **CLOSED. Do not re-pitch.** TJX was recommended 4x in 10 days and stopped twice.
  That is the anchoring failure the brief describes, and the right response is to stop.

- **KRE** (entry 76.80 on 08-15, stop 74.20) — 74.86, below both the 20-day (76.51) and the
  50-day (75.32). ATR14 is only 1.08 (1.44%), so the stop sits **0.6 ATR** away — inside a
  single ordinary day of noise. KRE has been recommended 4x in 10 days and stopped out twice
  already (08-17 and 08-18 lots, both stopped 08-19).
  decision: **CLOSE IT.** Not because 74.86 is a disaster but because a stop 0.6 ATR away is
  not a risk control, it is a coin flip, and the record says I keep re-buying this.

- **HD** (entries 340.00 on 08-18 and 337.49 on 08-19, stop 328.00) — 335.61, below the
  20-day (342.49) and the 50-day (340.08), -9.2% off the 120-day high. ATR14 8.88 (2.65%),
  so the 328 stop is **0.86 ATR** away. Same defect as KRE: too tight for the instrument.
  There is no dated catalyst before the stop is likely to be tested.
  decision: **CLOSE on any bounce toward 342 (the 20-day).** Widening the stop to ~322 would
  be adding risk to a position with no catalyst, which is the wrong direction.

- **BCC** (entry 81.00 on 08-18, stop 76.00, target 92.00) — 82.47, sitting on its 20-day
  (82.23) and well above the 50-day (77.98), -6.7% off the high. ATR 2.95 (3.57%), so the
  stop is 2.2 ATR away — correctly sized. decision: **HOLD unchanged.** Nothing new today.

- **LCII** (entry 94.00 on 08-18, target 138.00, no stop) — 101.98, +8.5%. Fell 3.28% Friday,
  below the 20-day (105.51), on its 50-day (102.17), -26.2% off the 120-day high of 138.15.
  decision: **HOLD**, but note the target of 138.00 is the exact 120-day high; that is a chart
  level dressed up as a valuation. Flagging it rather than repeating it as if defended.

- **TLT** (entry 82.60 on 08-20, stop 80.95, target 86.20) — 82.05. See the 06:56[06:29] entry.
  decision: **HOLD, DO NOT ADD.** Long duration into a hawkish Chair's debut keynote, a PCE
  print, and a 30-year yield at multi-decade highs is fighting the tape. Keep the stop.

- **XLE x3, CCJ x2, NKE x2, PFE, DHT, BTC x2, /MBTU6 x2** — decided above.

Net: of 20 open positions, 3 are to be closed (TJX already stopped, KRE, HD), 4 bearish-BTC
legs are dead and closed, 2 are re-levelled and captured (DHT, NKE), 2 are re-affirmed and
captured (CCJ, PFE), and the rest hold unchanged.

## [06:47 ET] THEME — AI/datacenter power: the fundamentals and the tape disagree
Fundamentals (PJM, the grid that serves most US datacenter growth):
- Average wholesale power **$114.50/MWh in H1 2026, +50.3% y/y.**
- **Capacity prices went from $28.92/MW-day (2024/25) to $329.17/MW-day (2026/27)** — 11x.
- Datacenters caused **63%** of the increase in the 2025/26 auction, ~$9.3B of cost recovered
  from PJM customers in higher rates.
  sources: https://ieefa.org/resources/projected-data-center-growth-spurs-pjm-capacity-prices-factor-10
           https://www.canarymedia.com/articles/data-centers/pjm-record-capacity-costs-rising-bills
           https://www.eenews.net/articles/data-centers-drive-76-surge-in-pjm-power-prices/
- Contracted demand: TLN supplies Amazon **1,920 MW** of nuclear through 2042; CEG has signed
  920 MW of hyperscaler PPAs; VST has Meta PPAs at Comanche Peak, FERC approval for a pending
  5,500 MW Cogentrix gas acquisition, a Helix JV with NVIDIA worth up to $1B, and Q2 ongoing
  adjusted EBITDA of $1.77B (+30%+ y/y).
  sources: https://finance.yahoo.com/energy/articles/3-nuclear-energy-stocks-riding-110022153.html
           https://www.investing.com/news/stock-market-news/ceg-vs-vst-nuclear-purity-against-diversified-value-in-the-ai-power-trade-93CH-4824092

The tape (nasdaq 120d thru 08-21) says the opposite:
- **TLN 314.46 | -30.1% off the 120d high (449.84), sitting ON the 120d low (301.45)** |
  SMA20 338.60, SMA50 367.23 | ATR14 17.68 (5.62%). Clean downtrend.
- **VST 136.21 | -21.3% off high (173.00), near the 120d low (132.66)** | SMA20 145.03,
  SMA50 153.35 | ATR14 5.42 (3.98%). Clean downtrend. Fell 4 of the last 5 sessions.
- CEG 272.88 | -17.9% off high | above SMA20 (270.24) and SMA50 (263.12). Holding up best.
  (CEG is an unfilled awaiting-entry at 266.00 from 08-21 and has been pitched 2x already.)
- TLN insiders: **zero open-market buys in six months, one sale of $988K.** No confirmation.
- This is the most interesting divergence I have found today and I am NOT going to capture it
  without understanding the sell-off. Searching the cause before deciding.

## [06:51 ET] THEME — why the IPPs sold off (the answer makes VST interesting, not scary)
- The decline is macro and rotational, not fundamental: rising Treasury yields hitting
  long-duration assets, fears that AI capital spending is becoming too aggressive with slow
  payback, and a semiconductor selloff dragging everything AI-adjacent that is not a chip.
  CEG, VST, TLN and NRG all fell together — a group move, not a company event.
- The key line from the coverage: "the pressure is not a referendum on datacentre electricity
  demand, because the demand forecasts kept going up the whole time the stock went down."
  sources: https://www.quiverquant.com/news/Vistra+slides+as+AI-power+names+weaken+and+no+fresh+company+catalyst+emerges
           https://www.ad-hoc-news.de/boerse/news/corporate-news/constellation-energy-stock-slips-as-power-demand-story-meets-market/69977622
           https://financefeeds.com/vistra-vst-stock-prediction-bull-bear-case/
- VST specifics: **2026 ongoing-ops adjusted EBITDA guidance REAFFIRMED at $6.8-7.6B, with
  98% of expected generation volumes hedged.** 2027 midpoint opportunity $7.4-7.8B EXCLUDING
  Cogentrix and the Meta PPA, though management flags ERCOT price softness pushing 2027 toward
  the low end. **$1.5B remaining on the buyback authorisation**, inside a $3B buyback/dividend
  plan with a 10b5-1 programme. Analyst consensus fair value **$221.57**; average 12-month
  target ~$225-230 across ~17-20 firms rating it Strong Buy.
  sources: https://seekingalpha.com/news/4629483-vistra-targets-6_8b-7_6b-2026-adjusted-ebitda-while-committing-up-to-1b-to-helix-partnership
           https://simplywall.st/stocks/us/utilities/nyse-vst/vistra/future
           https://www.stocktitan.net/sec-filings/VST/8-k-vistra-corp-reports-material-event-1c87c71fdb2e.html
- Decision: capture VST rather than TLN. TLN is 5.62% ATR, sitting on its 120-day low with
  zero insider buying and one $988K sale — a falling knife with no confirmation. VST has
  reaffirmed guidance, a 98% hedge book, and a buyback bidding the stock. CEG is excluded on
  the repetition rule (2x in 10 days, unfilled at 266) and because it has held up best, so
  it offers the least discount.
- Target set at 185, deliberately **17% BELOW** the $221.57 consensus fair value, so the idea
  does not depend on the street being right. Bear case 112 = a genuine AI-capex disappointment
  where VST is still a large hedged merchant generator collecting capacity payments.

## [06:48 ET] SCREENED, NOT CAPTURED — this week's earnings names (nasdaq 120d thru 08-21)
- PLAB 30.51 | ATR 4.18% | SMA20 31.49 | SMA50 30.93 | range 27.10-56.00 | **-45.5% off high**.
  Photomasks (semi pick-and-shovel), reports Wed 08-26 bmo. Deeply de-rated and sitting near
  its low. Genuinely interesting, but it reports the same morning as PCE/GDP and hours before
  NVDA — three uncorrelated shocks in one session. No edge on the print itself. WATCHLIST.
- OLLI 76.07 | -32.1% off high (112.00) | reports 08-26. Off-price retail — the exact category
  where TJX just fell 9% below its own 20-day. Not stepping into that ahead of a print.
- SMTC 124.09 | **ATR 9.32%** | -30.0% off high | reports 08-25 amc. Too volatile to hold
  through a print without a real edge.
- IREN 41.88 | ATR 8.30% | -40.8% off high | reports 08-27 amc. Bitcoin-miner/AI-datacenter
  hybrid — correlated to both the BTC squeeze and the NVDA print. Two binaries at once. No.
- KSS 17.60 (08-25), ANF 109.01 (08-25), URBN 74.24 (08-26), FIVE 250.24 (-0.55% off high,
  08-25), MBUU 29.50 (08-27) — screened, nothing with an edge I can defend.
- General principle applied here and to ZYME: **entering a name specifically to hold it
  through its own earnings print, with no informational edge, is a coin flip dressed as a
  catalyst trade.** None of these clear the R:R floor honestly, so none are captured.

## [06:51 ET] REJECTED — crypto, all of it, today. No candidate captured in this class.
- Live (coingecko): BTC $76,841 (-0.28% 24h), ETH $2,416.13 (+0.13%), SOL $93.75 (+0.74%),
  DOGE $0.0924, ADA $0.2221, LINK $11.43, AVAX $7.45, LTC $52.23.
- I went looking for an ETH catch-up trade and the premise was wrong. **ETH rose 27% in the
  week ending 2026-08-21** — it did not lag the BTC squeeze, it matched it. ETH is a laggard
  on the YEAR (-66% from the Aug 2025 ATH of $4,953, from ~$3,300 to ~$1,550 by late June),
  not on the week, and the year-long divergence is not something that closes because I noticed it.
  sources: https://naga.com/eu/news-and-analysis/articles/ethereum-price-prediction
           https://phemex.com/blogs/ethereum-price-analysis-2026-eth-etf-staking-glamsterdam-upgrade
- Structural positives exist — ~30% of circulating ETH staked (35.8M coins removed from liquid
  supply), the Glamsterdam upgrade, spot ETH ETF inflows turning positive ($356M in April after
  six negative months) — but none is dated, and analyst 2026 targets span $2,000 to $7,500,
  which is another way of saying nobody knows.
- Buying BTC or ETH after a 23-27% week, on a squeeze that liquidated $4.3B of shorts, is the
  mirror image of the mistake that just cost this report four short positions. Declining.
- **Weekend note for the report:** config/strategy.md says weekend runs should lean on crypto
  and event contracts because they trade now. Today crypto does not clear the bar on price,
  so this weekend's actionable lane is the single event contract, and the equity ideas are
  explicitly week-ahead levels for the Monday 08-24 open.

## [06:52 ET] EVENT MARKETS — screened, no second contract captured
- KXRECSSNBER-26 ("recession in 2026", two consecutive negative GDP quarters per BEA):
  6/8c, effectively resolved. KXRECSSNBER-27: 24/25c, but that is a 17-month hold and I have
  no defensible view on 2027 GDP. No edge, not captured.
- KXU3-26AUG ladder (August U-3, reported ~Sep 4): above 4.0% = 83/84c, above 4.1% = 52/56c,
  above 4.2% = 22/24c. Implies P(U3 >= 4.2%) ~54%, P(exactly 4.1%) ~30%, P(<=4.0%) ~16%.
  Current U-3 is 4.1%. I have not done the labour-market work to disagree with that ladder,
  and inventing a view to fill the event lane is exactly what the brief forbids. Not captured.

## [06:54 ET] CAPTURED — EEM at the unchanged 65.60 limit (2 prior publications, never filled)
- 67.12 close, above SMA20 65.21 and SMA50 66.09, -6.2% off the 120d high 71.57, ATR14 1.04
  (1.55% — unusually low, which is what lets a 2 ATR stop sit only 3.2% below entry).
- What changed since the 08-21/08-22 publications: DXY has broken **below 99.00** on the
  Treasury buyback announcement and $40T debt headline. The level is unchanged; the macro
  case behind it got stronger.
- This is now the ONLY weak-dollar expression in the report, by design — GLD, SLV, BTC and
  IBIT were all rejected on price. Stated as a concentration risk in key_risk.

## [06:55 ET] REJECTED — DG at 119 — will not re-pitch into a print I have no edge on
- 123.41, SMA20 124.15, SMA50 120.27, 120d range 99.57-155.51, -20.6% off the high.
- The 119.00 level from 08-21 is still sensible (it sits just below the 50-day) and still
  unfilled. But DG reports **Thu 08-27 bmo** ($2.06 EPS / $11.53B rev est), so a fill at 119
  this week means owning it through the print two days later.
- The trade-down thesis is genuinely two-sided right now: gasoline +98% YTD squeezes DG's
  low-income customer into the store, and out of the basket, at the same time. I cannot say
  which dominates, and zero insider buying in six months gives me nothing to lean on.
- Same rule I applied to ZYME, OLLI, SMTC and IREN: no edge on the print, no position.
  Consistency matters more than filling the retail slot.

## [06:56 ET] VENUE CHECK — Robinhood Prediction Markets carries FOMC decision contracts
- Robinhood publishes per-meeting FOMC decision events directly, e.g.
  https://robinhood.com/us/en/prediction-markets/economics/events/fed-decision-in-july-jul-29-2026/
  under https://robinhood.com/us/en/prediction-markets/economics . Event contracts are offered
  through Robinhood Derivatives LLC. The KXFEDDECISION series is therefore carried, which
  matches this report having published KXFEDDECISION-26SEP-H25 on 2026-08-22.
  source: https://www.fintechbrainfood.com/p/robinhood-bets
- Corroboration for the rate view from Kalshi's other Fed series: ~54% odds of any hike in
  2026, ~62% that the next hike comes before July 2027, and ~76% odds of ZERO cuts this year.
  Consistent with the 31/32c September hike and the 67/68c hold I captured.
  sources: https://kalshi.com/markets/kxfeddecision/fed-meeting/kxfeddecision-26sep
           https://kalshi.com/markets/kxfedhike/next-fed-rate-hike/fedhike

## [06:55 ET] SCREENED, NOT CAPTURED — insider-buying small caps (and a data correction)
- **MBC (MasterBrand)** 9.11 | ATR 4.77% | SMA20 9.00 | SMA50 9.03 | range 6.605-10.355 |
  -12.0% off high. Secondary coverage said CEO R. David Banyard bought 60,000 shares in
  "early August 2026"; the **Form 4 record says 2026-06-01 at $8.43** — the article's date is
  wrong. Using the filing, not the write-up.
  Real cluster: 4 open-market buys by **4 distinct buyers** between 06-01 and 06-11
  (Banyard 60,000 @ 8.43; Petratis 11,587 @ 8.82; Simon 5,000 @ 8.56; Fracassa 5,000 @ 9.11).
  BUT total buys $696K against $799K of sales — **net insider is NEGATIVE $103K** — the cluster
  is 2.5 months old, and the stock has gone nowhere (20-day 9.00 vs 50-day 9.03).
  Also housing-exposed with the 10-year at 4.69%, and correlated with the open BCC position
  and the HD position I am closing. Not enough. WATCHLIST.
- **LUMN (Lumen)** 5.94 | **ATR 6.78%** | -47.4% off the 120-day high (11.30), sitting on the
  120-day low (5.76). CEO Kathleen Johnson bought 100,000 shares @ $6.1268 on 2026-08-06 and
  is **already underwater 3%**. Only ONE buyer, and one sale of $355K against it. A single
  insider buying a heavily indebted telecom at its lows is not a cluster, it is a knife.
  sources: https://www.investing.com/news/stock-market-news/thursdays-insider-buys-and-sells-ceos-make-major-moves-93CH-4846553
           https://simplywall.st/stocks/us/capital-goods/nyse-mbc/masterbrand/news/undervalued-small-caps-with-insider-buying-to-watch-in-augus-1
- Honest gap for the report: I hunted the small-cap lane and it produced exactly ONE capture
  (SVRA). That is a thin result and I would rather say so than pad it.

## [06:56 ET] DATA PROVENANCE — read this before trusting the fields in candidates.jsonl
- `last_price` on every equity/ETF candidate is the **Friday 2026-08-21 close** (finnhub or
  nasdaq), session=closed, age ~38 hours. It is not stale data; it is the freshest honest
  price on a Sunday with US markets shut.
- `avg_dollar_volume` on each candidate is computed from the actual recent daily volumes in
  the nasdaq history response times the close. Grounded.
- **`market_cap_usd` is an order-of-magnitude ESTIMATE in every case**, entered only to drive
  the position-sizing tier. I did not fetch a share count for CCJ, PFE, NKE, LULU, VST or DHT.
  None of them is near the $300M/$2B sizing thresholds, so the estimate cannot change the tier
  — but synthesis and validation should treat these as unverified and `data_quality_notes`
  should say so. SVRA is the only one where the figure matters for sizing; verifying it now.

## [06:57 ET] VERIFIED — SVRA share count, straight from SEC XBRL
- **205,460,015 shares outstanding as of 2026-08-11** (dei:EntityCommonStockSharesOutstanding,
  Q2 2026 10-Q cover, CIK 0001160308).
  source: https://data.sec.gov/api/xbrl/companyconcept/CIK0001160308/dei/EntityCommonStockSharesOutstanding.json
- At the 5.59 close that is a **$1.1485B market cap** — my earlier $1.0B estimate was low.
  Well above the $300M threshold, so the "speculative" tier and 1.5% sizing stand unchanged.
- The $108.3M / 18.9M-share shelf is **9.2% of shares outstanding** — that is the dilution
  number and it belongs in the risk, not a vague warning. Re-capturing SVRA with both figures.

## [07:00 ET] FALSIFICATION — I recomputed the reward-to-risk on every captured candidate
## by hand rather than trusting what I wrote. One failed.
Floors: intraday 1.5 vs stop, swing 2.0 vs stop, long_term 2.5 vs the stated bear-case price.
- CCJ   long_term  (135-96)/(96-83)       = 3.00  PASS
- PFE   long_term  (38-26.4)/(26.4-23.6)  = 4.14  PASS
- LULU  long_term  (165-112)/(112-92)     = 2.65  PASS
- VST   long_term  (185-132)/(132-112)    = 2.65  PASS
- SVRA  swing      (8-5.35)/(5.35-4.6)    = 3.53  PASS
- DHT   swing      (24.5-19.4)/(19.4-18.3)= 4.64  PASS
- EEM   swing      (71.5-65.6)/(65.6-63.5)= 2.81  PASS
- TLT   swing      (85-82.05)/(82.05-80.95)=2.68  PASS
- FED   swing      (90-68)/(68-57)        = 2.00  PASS, exactly at the floor. Left alone
                   deliberately — 90c is the realistic pre-resolution exit and I am not going
                   to nudge it to 92 to buy margin.
- **NKE long_term  (56-39)/(39-32)        = 2.43  FAIL** (floor 2.5).
  Fix, and it is a discipline fix rather than a tuning fix: the ADD entry moves from 39.00 to
  **38.50**, below the 12-year low of 39.09 printed on 08-17. Buying an existing loser only
  below its own multi-year low is the correct rule anyway.
  Revised: (56-38.50)/(38.50-32) = **2.69 PASS**. Target 56 and bear 32 are unchanged — I did
  not touch either, which is the point.

## [07:04 ET] INSIDERS — verifying a claim I had asserted without checking. One held, one improved.
- I wrote in the VST counter-argument that "no Vistra executive is buying this dip." I had NOT
  actually checked that when I wrote it. Checked now, and it is true — and worse than I said:
  **VST has 0 open-market buys and 8 SALES totalling $6.86M over six months, net -$6.86M.**
  Strengthening the counter-argument with the real figure and re-capturing.
- **LULU: 3 open-market buys, 2 distinct buyers, $1.99M bought against $0.10M sold, net +$1.89M.**
  - **Charles V Bergh (chairman, former Levi Strauss CEO) 6,090 sh @ $164.20 on 2026-03-20,
    then 4,275 sh @ $117.05 on 2026-06-15** — he doubled down 29% lower.
  - Andre Maestrini 3,275 sh @ $151.02 on 2026-04-01.
  Bergh's June fill of $117.05 sits inside my 106-118 accumulation zone. This is a genuine
  confirmation I did not have when I captured LULU and it belongs in the thesis.
- CCJ: zero insider transactions either way in six months. My CCJ thesis made no insider claim,
  so nothing to correct — noting it so the absence is on the record rather than unexamined.

## [07:08 ET] CORRELATION AUDIT — config/strategy.md caps ideas sharing a driver at 3
Ten unique candidates, grouped by what actually decides them:
1. **Rates / dollar / duration — 3 ideas, AT THE CAP.** KXFEDDECISION-26SEP-H0 (no hike),
   EEM (weak dollar), TLT (long duration). **All three lose on the same event: a hawkish
   Warsh keynote on Fri 2026-08-28 ~10:00 ET.** Combined size 5% of capital (2+2+1). This is
   the single biggest concentration in the report and it must be stated in the published
   version, not buried. It is at the cap, not over it, and it is deliberately the smallest-sized
   group for exactly that reason.
2. **Datacenter/AI power demand — 2 ideas.** CCJ (nuclear fuel), VST (merchant generation).
   Both also carry NVDA-print risk on Wed 08-26; VST explicitly says wait for it.
3. **Consumer-discretionary de-rating — 2 ideas.** LULU, NKE. Both athletic apparel. Both
   carry the insider-conviction pattern; both insiders are underwater.
4. Hormuz / VLCC freight — 1 (DHT). 5. Pharma insider cluster — 1 (PFE).
   6. FDA binary — 1 (SVRA).
No driver exceeds 3. Total capital deployed if every idea fills: 22.5%.

## [07:08 ET] RESEARCH COMPLETE
- candidates: **10 unique** (15 lines in candidates.jsonl; SVRA, NKE, VST, LULU and the Fed
  contract were each re-captured after verification improved them — synthesis takes the last
  entry per symbol).
  - by horizon: long_term 5 (CCJ, PFE, LULU, NKE, VST), swing 5 (Fed, SVRA, DHT, EEM, TLT),
    **intraday 0** — US markets are shut, I have no live tape, and manufacturing an intraday
    level from a Friday close would be fiction. Equity entries are for the Mon 08-24 open.
  - by conviction: 4x four (CCJ, PFE, LULU, DHT), 4x three (Fed, NKE, VST, EEM), 2x two (SVRA, TLT).
  - position updates on open positions, all captured: CCJ, PFE, DHT, NKE, TLT.
  - explicit CLOSE decisions, logged but not captured as candidates because the schema has no
    way to express an exit: **BTC x2 and /MBTU6 x2 (blown through stops, thesis falsified),
    TJX (already stopped), KRE (stop 0.6 ATR away, 4 pitches and 2 stop-outs), HD (stop 0.86
    ATR away, no catalyst).** Synthesis must carry these into the report body.
- rejected with reasons logged: GLD, SLV/silver, DINO/refiners, ZYME, crypto (BTC/ETH/SOL/IBIT),
  DG, TLN, CEG, MBC, LUMN, OLLI, SMTC, IREN, KSS, ANF, URBN, FIVE, MBUU, PLAB, KXRECSSNBER,
  KXU3, XLE (repetition).
- coverage gaps:
  - **No fetched quote for SPX, NDX, DJI, RUT, VIX, DXY, UST10Y, gold, WTI, ES or NQ.** The
    dollar "below 99.00" and gold "$4,602.99" figures come from news text, NOT from a fetched
    price feed, and must be labelled that way in data_quality_notes.
  - **Zero futures candidates.** I did not verify Robinhood's current futures contract list this
    run, and none of today's views was best expressed as a contract I could name with a month.
    That is a real gap against the preference in config/universe.md.
  - The small-cap lane produced one capture (SVRA). Thin, and said plainly rather than padded.
  - `market_cap_usd` is an unverified estimate on every candidate except SVRA (see 06:56).
  - No 8-K/10-Q read in full: SEC Archives HTML returns 403 to the fetch tool. The XBRL API at
    data.sec.gov works with a User-Agent header and is how SVRA's share count was verified.
- sources that failed:
  - **Yahoo Finance: HTTP 429 on every symbol** — killed the whole `market_data.py macro`
    market block. stooq 404s on ^GSPC/^NDX/^DJI/^RUT. finnhub refuses index CFDs
    ("Market data subscription required"). alphavantage: no API key.
  - **`market_data.py events "<topic>"` returns 0 for every keyword** — it fetches only the
    first 200 open Kalshi markets (all sports parlays) and filters client-side. Worked around
    by querying api.elections.kalshi.com directly with `event_ticker` / `series_ticker`, and
    note the price fields are `yes_bid_dollars` / `yes_ask_dollars`, not `yes_bid`. **Worth
    fixing in the script.**
  - WebFetch 403 on cnbc.com and on sec.gov/Archives.
- what worked: finnhub quotes/earnings/insiders, nasdaq history, coingecko, FRED, BEA schedule,
  data.sec.gov XBRL, direct Kalshi API.

## [06:57 ET] ADDENDUM — MACRO GAP CLOSED. These are FETCHED numbers, not news text.
After RESEARCH COMPLETE I went back at the missing macro series. stooq is blocking every
request outright (404 on spx, vix, dx.f, xauusd, cl.f, es.f, nq.f, 10usy.b), but **FRED serves
all of it**, and `market_data.py` already has a working `fred_series()` — the macro command
just does not request these IDs. Fetched directly:
- **DGS30 — US 30-year Treasury yield 5.23% (2026-08-20).** This CONFIRMS from a primary
  source the "30-year at multi-decade highs" claim I had only from a CNBC summary. 5.23% on
  the long bond is the highest since the mid-2000s.
- DGS10 4.69%, DGS2 4.19% (both 2026-08-20).
  Curve: **30y-10y = +54bp, 10y-2y = +50bp.** A long end steepening away from the front end is
  a term-premium/fiscal story, not a growth story — which is exactly the debasement read that
  gold, the Treasury buyback announcement and the $40T debt headline all point at. My macro
  framing survives primary-source checking.
- **VIXCLS — VIX 16.01 (2026-08-20).** This matters: **the market is priced for calm going into
  a week that stacks July PCE + Q2 GDP (Wed 08:30), NVDA earnings (Wed after the close) and
  Warsh's Jackson Hole debut (Fri 10:00).** A 16 handle is not what a market that has priced
  those three events looks like.
- **DCOILWTICO — WTI $86.48 (2026-08-18)**, consistent with crude +44% YTD and with Hormuz.
- DTWEXBGS — broad trade-weighted dollar 118.90 (2026-08-14). NOTE: this is the Fed's BROAD
  index and is NOT on the same scale as DXY; it neither confirms nor contradicts the reported
  "DXY below 99.00", which remains a news-sourced figure. Flagging so nobody conflates them.
- sources: https://fred.stlouisfed.org/series/DGS30 , /VIXCLS , /DCOILWTICO , /DTWEXBGS , /DGS10 , /DGS2
- **Suggested fix for scripts/market_data.py:** add DGS30, VIXCLS, DCOILWTICO and DTWEXBGS to
  FRED_SERIES. It would have made today's entire macro block available despite Yahoo being
  rate-limited, instead of returning six failed sources.

## [06:58 ET] WHAT VIX 16.01 CHANGES — nothing in the ideas, and that is the point
- There is no clean long-volatility expression here: options are out of scope, VIX futures are
  a Cboe product rather than CME so they are not in Robinhood's futures list, and VIXY/VXX
  decay too fast to hold as a week-long hedge. So I am not manufacturing a trade out of it.
- What it does do is validate the sizing and the "wait" actions already captured: VST says wait
  for the NVDA print, LULU says wait for Sep 2-3, PFE and CCJ say add only on a pullback, and
  the whole rates/dollar cluster is capped at 5% of capital. Cheap options premium is the
  market telling you the event risk is underpriced, and the right response without options is
  smaller size and later entries — which is what is in the file.

## [07:00 ET] NEW IDEA — IBM. A $69B de-rating on a 3.7% revenue miss, with a named cause.
- **2026-07-14: IBM pre-announced Q2 and the stock fell ~25% in one session — its worst day on
  record, worse than 19 Oct 1987 (-23.7%). About $69B of market value erased.**
- The actual miss: adjusted EPS **$2.93 vs $3.01** expected (-2.7%), revenue **$17.2B vs
  $17.86B** (-3.7%). That is a modest miss producing a historic reaction.
- The stated cause is specific and, importantly, a TIMING story: per CEO Arvind Krishna,
  clients dramatically reprioritised technology spending **in the final weeks of June 2026**,
  redirecting budget from IBM software and infrastructure toward **hardware — servers, storage
  and memory chips — to secure supply-constrained capacity ahead of expected price increases.**
  Large deals did not close on expected timelines, and that slippage was the majority of the
  shortfall. IBM leadership failed to anticipate the magnitude of the shift.
  sources: https://www.cnbc.com/2026/07/14/ibm-warns-second-quarter-earnings-fell-short-of-expectations.html
           https://www.forbes.com/sites/tylerroush/2026/07/14/ibm-shares-crashed-25-in-worst-day-ever-heres-why/
           https://www.fool.com/investing/2026/07/19/ibm-stock-q2-preliminary-warning-ai-capex/
           https://fortune.com/2026/07/15/ibm-stock-price-crash-25-percent-analyst-reaction/
- Levels: 235.68 | ATR14 6.54 (2.77%) | SMA20 231.70 | SMA50 247.36 | 120d range 199.19-332.46 |
  -29.1% off the high, +18.3% off the low. **Has held a tight 228.85-238.42 range for three
  weeks** — the panic is over and it is base-building.
- Insiders: 2 open-market buys, but only $113K total and both from 2026-02-25, before the crash.
  Zero sales. Effectively no signal either way — stating that rather than dressing it up.
- Honest R:R work, which is what decides this: bear case is 190 (below the 199.19 post-crash
  low), because if the capex shift is permanent rather than a June timing effect, the stock
  breaks that low. Target 290, the multiple IBM held before a single quarterly warning.
  - At the current 235.68: (290-235.68)/(235.68-190) = 1.19 — **FAILS badly. Do not buy here.**
  - At 228 (the base low): 62/38 = 1.63 — still fails.
  - At **215**: (290-215)/(215-190) = 75/25 = **3.00 PASS.**
- So the recommendation is a limit 8.7% below market that may simply never fill. That is the
  correct answer, not a reason to move the target. Capturing it that way.
- Driver check: enterprise IT spending. Uncorrelated with every other idea in the report.

## [07:00 ET] FINAL — supersedes the counts in the 07:08[06:54] RESEARCH COMPLETE block
Two things were added after that block was written: the FRED macro addendum, and IBM.
Final state of `candidates.jsonl`: **16 lines, 11 unique symbols** (SVRA, NKE, VST, LULU and the
Fed contract were each re-captured after verification improved them; synthesis takes the last
entry per symbol).

Recomputed every reward-to-risk from the file itself, not from what I wrote in prose.
Long-term measured against `bear_case_price`, swing against `stop`:
| symbol | horizon | conv | entry | target | downside | R:R | floor | size |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PFE  | long_term | 4 | 26.40 | 38.00 | 23.60 | 4.14 | 2.5 | 3% |
| DHT  | swing     | 4 | 19.40 | 24.50 | 18.30 | 4.64 | 2.0 | 2% |
| SVRA | swing     | 2 | 5.35  | 8.00  | 4.60  | 3.53 | 2.0 | 1.5% |
| CCJ  | long_term | 4 | 96.00 | 135.00| 83.00 | 3.00 | 2.5 | 3% |
| IBM  | long_term | 3 | 215.00| 290.00| 190.00| 3.00 | 2.5 | 2% |
| EEM  | swing     | 3 | 65.60 | 71.50 | 63.50 | 2.81 | 2.0 | 2% |
| NKE  | long_term | 3 | 38.50 | 56.00 | 32.00 | 2.69 | 2.5 | 2% |
| TLT  | swing     | 2 | 82.05 | 85.00 | 80.95 | 2.68 | 2.0 | 1% |
| LULU | long_term | 4 | 112.00| 165.00| 92.00 | 2.65 | 2.5 | 3% |
| VST  | long_term | 3 | 132.00| 185.00| 112.00| 2.65 | 2.5 | 3% |
| FED  | swing     | 3 | 68c   | 90c   | 57c   | 2.00 | 2.0 | 2% |
All 11 clear their floor. Total capital if every limit fills: **24.5%**.

Updated driver groups (correlation cap 3):
1. Rates/dollar/duration — 3, AT THE CAP: Fed H0, EEM, TLT. All three lose on a hawkish Warsh
   keynote Fri 08-28 10:00 ET. Combined 5% of capital. **Must be stated in the report.**
2. Datacenter/AI power — 2: CCJ, VST. Both also exposed to the NVDA print Wed 08-26.
3. Consumer-discretionary de-rating — 2: LULU, NKE (both athletic apparel, both with
   underwater insider buyers).
4. Hormuz/VLCC freight — 1: DHT.  5. Pharma insider cluster — 1: PFE.
6. FDA binary — 1: SVRA.  7. Enterprise IT spending — 1: IBM.
Horizons: long_term 6 (CCJ, PFE, LULU, NKE, VST, IBM), swing 5 (Fed, SVRA, DHT, EEM, TLT),
intraday 0. Conviction: four 4s, five 3s, two 2s.

Three of the eleven are explicit WAIT recommendations with limits below market that may never
fill — VST (wait for NVDA), LULU (106-118, 8% below), IBM (215, 8.7% below) — plus CCJ, PFE
and NKE which are adds only on pullbacks. That is deliberate. The week stacks PCE + GDP
(Wed 08:30), NVDA (Wed pm) and Warsh (Fri 10:00) with the VIX at 16.01, and the honest response
to cheap event risk without access to options is later entries and smaller size.

Closing decisions on open positions, logged but NOT in candidates.jsonl because the schema has
no way to express an exit — **synthesis must carry these into the report body**:
CLOSE BTC x2 and /MBTU6 x2 (stops blown by 20-22%, thesis falsified by a named catalyst);
TJX (already stopped); KRE (stop 0.6 ATR away, 4 pitches / 2 stop-outs); HD (stop 0.86 ATR
away, no catalyst). XLE x3, BCC, LCII hold unchanged and were deliberately not re-captured.

STOPPING HERE. Nothing else cleared the bar, and the brief is explicit that padding is worse
than publishing fewer.
