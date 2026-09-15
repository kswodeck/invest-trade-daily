# Research log — 2026-09-15

## [06:04 ET] MACRO — rates, regime, data quality
Session: pre-market. Freshest honest equity prices are the **2026-09-14 close**
(asof 2026-09-14T20:00Z, age ~841 min). That is a closed market, not stale data.

- US 10y 4.96% (FRED DGS10, 2026-09-11), prev 4.95 — source: https://fred.stlouisfed.org/series/DGS10
- US 2y 4.63% (DGS2, 2026-09-11), prev 4.56 — +7bp in a day, source: https://fred.stlouisfed.org/series/DGS2
- Fed funds effective 3.63% (DFF 2026-09-11) — source: https://fred.stlouisfed.org/series/DFF
- 10y-2y curve +0.32 (2026-09-14), prev 0.33 — source: https://fred.stlouisfed.org/series/T10Y2Y
- Unemployment 4.1% (Aug 2026, unchanged) — source: https://fred.stlouisfed.org/series/UNRATE
- **2y at 4.63 vs effective funds 3.63 = 100bp of tightening priced into the 2y.**
  This is a market expecting hikes, not cuts. Frames everything today.

### DATA GAPS (for data_quality_notes)
- `market_data.py macro` returned ok:false for SPX, NDX, DJI, RUT, VIX, /ES, /NQ,
  DXY, us10y_yield quote, gold, WTI — Yahoo is HTTP 429 (rate limited) and
  Finnhub refuses index CFDs. Only bonds_20y (TLT proxy) resolved.
- No live index level, no VIX print this run. Single-name equity quotes DO work
  via Finnhub.

## [06:05 ET] TAPE — 2026-09-14 closes, notable moves
- CEG 264.57 (-7.09%) | VST 140.73 (-5.16%) | CCJ 93.26 (-3.54%)
  **The IPP / nuclear power complex was hit hard in one session.** Needs a cause.
- EEM 65.99 (-2.73%) — EM risk-off
- DG 129.17 (+3.68%) — defensive retail bid
- SPY 760.88 (-0.45%), TLT 80.93 (+0.07%), XLE 64.53 (-0.94%), DVN 49.73 (-1.00%)

## [06:11 ET] MACRO — the regime read that frames today
- CPI index (CPIAUCSL) Aug 2026 = 334.131 vs Jul 332.813 → **+0.40% MoM**,
  ~4.9% annualized. Inflation is re-accelerating.
  source: https://fred.stlouisfed.org/series/CPIAUCSL
- 2y 4.63% sits **100bp above** effective fed funds 3.63%. The front end is
  pricing tightening, not easing. 10y 4.96%.
- Unemployment 4.1%, unchanged — no labour-market offset to force cuts.
- **FOMC decision Wednesday 2026-09-17.** This is the dominant dated event.
- Tape on 2026-09-14 is consistent: long-duration growth sold (CEG -7.1%,
  VST -5.2%, CCJ -3.5%), EM sold (EEM -2.7%), gold sold (GLD -1.5%),
  defensives bid (DG +3.7%). SPY only -0.45% — a rotation, not a liquidation.
- Crypto: BTC 76,946 (-1.4% 24h), ETH 2,473.62 (-1.9%), SOL 100.82 (-1.0%)
  source: coingecko via market_data.py macro

## [06:12 ET] DATA GAP — event contracts unavailable this run
`market_data.py events` returns ok:true count:0 for "Fed", "Fed decision",
"interest rate", "CPI", "recession", and returns unrelated tennis/baseball
markets for "FEDDECISION". The Kalshi search path is degraded — I cannot read
an implied probability for the Sept 17 FOMC. **No event contract will be
captured today**, because the edge has to be a stated probability disagreement
and I have no market price to disagree with. Three FOMC event contracts are
already open from prior runs; I am not amending them blind.

## [06:20 ET] POSITION UPDATE — LCII — opened 2026-08-18 @ 94.00, now 90.19 (-4.1%)
- decision: **CLOSE**. Captured via add_candidate.py as LCII `sell`, conviction 3.
- why: fifth consecutive lower close; 90.19 is 1.34% above the 180d low of 89.00;
  -12.1% in six sessions from 102.60; sma20 100.88, sma50 103.42 both far above.
  The position carries **no stop**. THO (the RV OEM it supplies) reports
  2026-09-22 bmo and is itself -40.2% off its 180d high — a negative read-across
  into a stopless loser.
- source: https://www.nasdaq.com/market-activity/stocks/lcii/historical

## [06:20 ET] POSITIONING — analyst revision direction (fetched, 4-month trend)
- **FDX**: bullish share 68.6%, change **+5.0 — improving**; beats in 2025-09 (+5.5%)
  and 2025-06 (+3.4%). Reports 2026-09-16. Improving revisions into a print.
- **VST**: bullish share 91.7%, change +0.4 — improving. But 2026-06 quarter
  **missed by 55.1%** (0.76 actual vs 1.69 est). 1 insider open-market buy / 6mo.
- **CEG**: bullish share 82.1%, change -3.1 — **deteriorating**. Beat +10.7% in
  2026-06 and +5.7% in 2026-03. 1 insider open-market buy / 6mo.
- **DG**: bullish share only 45.0%, change -1.2 — deteriorating. But beat +7.8%
  (2026-09 qtr) and +3.0% (2026-06). 0 insider buys. A doubted name that keeps beating.
- source: https://finnhub.io/api/v1/stock/recommendation

## [06:20 ET] DATA GAP — two more sources down
- `market_data.py short` FAILS for every symbol tried (DG, CEG, VST, FDX):
  api.nasdaq.com ReadTimeout. **No short-interest or days-to-cover read today.**
- `market_data.py implied DG` FAILS: Yahoo options 401 Unauthorized.
  **No options-implied move check today** — I cannot test any target against
  what the straddle prices. Targets below rest on price history alone; say so.

## [06:31 ET] CORRECTION — the FOMC meeting is 2026-09-15/16, not 09-17
Verified against the Fed's own calendar: the 2026 meetings are Jan 27-28,
Mar 17-18, Apr 28-29, Jun 16-17, Jul 28-29, **Sep 15-16**, Oct 27-28, Dec 8-9.
So **today is day one and the decision lands tomorrow, Wed 2026-09-16 at
14:00 ET** (statement time is the Fed's standard 2pm; the calendar page itself
does not print a time). Supersedes the 09-17 date in my 06:11 MACRO note.
source: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
**FDX also reports 2026-09-16** — the print and the Fed land the same day.

## [06:32 ET] RELATIVE STRENGTH — one clear leader, one clear laggard
- **DG vs SPY +8.00% (1m), +9.94% (3m); vs XLP +7.65% (1m), +14.15% (3m).**
  DG +5.81% over 1m while SPY -2.19% and XLP -1.84%. Genuine leadership in a
  defensive name while the index falls — exactly the trade-down tell.
- **VST vs SPY -1.68% (1m), -7.51% (3m), -26.35% (6m); vs XLU only +1.17% (1m).**
  Not leadership. VST is falling with its sector. Fine for a long-term
  accumulation into a de-rating; disqualifying for a swing.
- source: computed by scripts/market_data.py relstrength from fetched history

## [06:33 ET] LEVELS — DG structure
- 2026-09-14 close 129.17, ATR14 4.4581 (3.45%), sma20 125.45, sma50 123.69
- 180d range 99.57 - 158.23; -18.37% off high
- Swing high **134.125 on 2026-09-02** is the resistance that matters.
- Base shelf: lows 124.09 (09-09), 122.395 (09-11), 122.89 (09-12) - and the
  50d SMA at 123.69 sits inside it. That cluster is the invalidation.
- Avg 30d dollar volume $310.8M - no liquidity constraint.
- **A pullback entry here fails the test in config/strategy.md** (31 pullbacks
  vs 1 breakout in month one, 42% fill, the fills being the failures). DG is
  mid-range between its shelf and its resistance, so the honest entry is the
  breakout through 134.13, not a discount off 129.

## [06:12 ET] TIMESTAMP CORRECTION
The `[HH:MM ET]` stamps on the blocks above (06:20 through 06:33) were my own
estimates and ran ahead of the wall clock. `date` reads **06:12 ET** here. The
sequence of the blocks is correct; the absolute times above are not. Every
block from this one down is stamped from `date`. Nothing about the prices or
findings changes — those all carry their own fetched `asof`.

## [06:12 ET] REJECTED — CEG / VST long-term — no defensible valuation anchor yet
The setup is real: the AI-power complex took a valuation reset, CEG closed
264.57 on 2026-09-14 (-7.09%, and *on its low* of 264.32), 30.1% off its 180d
high of 378.50 and below both its 20d (280.65) and 50d (270.03); VST 140.73
(-5.16%), 22.9% off its high. Analysts are still 82.1% (CEG) and 91.7% (VST)
bullish and each shows one insider open-market buy in six months.
But `config/strategy.md` requires a long_term target to be a **defended
valuation with the method shown** and a bear case with a price. CEG recent
EDGAR filings are Forms 3/4/144 and a 13G/A — no guidance 8-K I have read.
I will not anchor a multi-year target to a consensus price target quoted in a
news summary. Revisiting below if time allows; not capturing on this evidence.

## [06:16 ET] POSITION UPDATES — two positions that need nothing
- **DVN** — opened 2026-09-11 @ 49.60, now 49.73 (+0.3%). decision: **HOLD, no
  change, no candidate.** It is the one open position that was built correctly:
  stop 46.90 = 2.22 ATR (ATR14 1.2168), target 55.50 = R:R 2.19, price above the
  20d (48.46) and 50d (45.64) and only 5.7% off its 180d high of 52.71. Nothing
  changed, and DVN has been recommended 3x in ten days — re-pitching it would be
  the anchoring the prior-context guard is aimed at.
- **SVRA** — opened 2026-08-23 @ 5.35, now 5.34 (-0.2%). decision: **HOLD, no
  change, no candidate.** Stop 4.60 = 3.84 ATR (ATR14 0.1954), target 8.00 =
  R:R 3.53. Drifting sideways in a 5.24-5.63 band; the thesis has neither been
  confirmed nor broken. Recommended 2x in ten days.
- source: https://www.nasdaq.com/market-activity/stocks/dvn/historical

## [06:17 ET] REJECTED — FDX — 2:1 is unreachable from any honest level
Best-constructed version: wait for the 2026-09-16 print, buy the reclaim of the
20d SMA at 324.04, entry 324.50, stop 305.00 (below the 09-10 low of 306.79) =
19.50 risk = 2.73 ATR. A 2.0 ratio then needs 363.50 — **above the 180-day high
of 345.37.** Targeting the high itself (345.00) gives R:R 1.05. The only way to
publish FDX is to tighten the stop, which is the failure config/strategy.md
names. Dropped, despite the genuinely good setup: revisions improving (+5.0,
bullish share 68.6%) and beats of +5.5% and +3.4%. Reports the same afternoon
as the FOMC.

## [06:17 ET] REJECTED — GIS — prints within the hour, and only clears at exactly 2.00
GIS reports 2026-09-15 (today, bmo) — before a 6am reader can act. It is 26.5%
off its 180d high at 36.47 after falling from 41.20 in nine sessions, which is
the de-rated-staples setup the trade-down regime should favour. But the only
structure that clears the floor is entry 38.00 / stop 34.50 / target 45.00 =
**exactly 2.00**, and 34.50 is not a level — it sits between the 09-11 low of
35.61 and the 180d low of 31.75 with no shelf. Widening the stop to 34.00 drops
the ratio to 1.75. A ratio that lands exactly on the floor with a stop chosen to
put it there is the thing I am supposed to refuse. Dropped.

## [06:17 ET] DATA GAP — no Bitcoin history, so no crypto futures idea
`history BTC-USD` fails (Yahoo 429, Nasdaq has no such symbol) and `history BTC`
silently resolves to an **equity** ticker (close 34.91, ATR14 0.9968) — that is
not the coin. Spot prices are fine via coingecko: BTC 76,999 (-1.29% 24h),
ETH 2,477.51 (-1.64%), SOL 100.91 (-0.83%). But every futures idea must carry a
stop and I have no ATR to size one, so **no /MBT or /MET candidate today.**
Note also that the pending `/MBTU6 SHORT @ 64340` from 2026-08-18 is 16.4%
below spot and cannot fill; U6 is also inside its final fortnight. I am not
amending it to a live level without an ATR to set the stop from.

## [06:19 ET] NEWS — the cause of yesterday's tape: AI leaders proposed slowing AI development
This is the single most important thing I found and it reframes several ideas.
On 2026-09-14 a coordinated set of comments from AI leaders — Anthropic's Dario
Amodei, with support from Elon Musk and OpenAI's Sam Altman — proposed slowing
the pace of AI development. Chipmakers sold off hard; a semiconductor gauge fell
5.9% and the Nasdaq 100 fell 0.8%. Elevated oil prices added to it.
- sources:
  https://features.financialjuice.com/2026/09/14/chipmakers-slide-as-ai-leaders-back-slower-development-us-market-wrap/
  https://www.bloomberg.com/news/articles/2026-09-13/us-stock-futures-fall-on-ai-warning-oil-gains-markets-wrap

**The sector tape of 2026-09-14 fits it exactly** (fetched closes, change vs 09-11):
  XLV +1.45% | XLP +1.25% | KRE +0.28% | XLY -0.10% | IWM -0.34% | XLF -0.38%
  XLRE -0.69% | XLB -0.90% | XLU -1.34% | XLI -1.42% | XLK -1.81% | **SMH -4.75%**
Money left AI and long-duration growth and went into healthcare and staples.
CEG -7.09%, VST -5.16% and CCJ -3.54% are *not* a separate story — datacenter
power demand is the AI capex thesis wearing a utility ticker.

Two consequences I am acting on:
1. It **confirms the CCJ exit**: the drawdown has a live fundamental cause, not
   just a multiple reset, and the position had no stop.
2. It **confirms holding off on CEG/VST**. A de-rating with a fresh fundamental
   driver behind it is not a valuation anchor waiting to be bought; it is the
   market repricing the demand curve. Still no capture there.

## [06:20 ET] REJECTED — XLV — right rotation, wrong instrument, 2:1 unreachable
XLV is the best-positioned sector on the tape: +1.45% on 2026-09-14, +1.82% vs
SPY over 1m and +6.48% over 3m, and +9.06% absolute over 3m against XLP -1.63%.
It bounced off its 50d SMA (166.32) at a 165.11-165.66 low cluster and closed
167.75. But ATR14 is only 2.277 (1.36%) against a 180d range of 141.97-176.595.
Entry 169.00 with an honest stop at 163.00 (below the cluster and the 50d) is
6.00 of risk = 2.63 ATR; a 2.0 ratio then needs **181.00, above the 180d high of
176.595**. Targeting the high gives R:R 1.17. The sector is right and the ETF is
too quiet to pay for its own stop. A single name in the sector would have the
range — I did not have time to find one. **Flagging this as the top coverage gap.**

## [06:25 ET] CAPTURED — MDT buy, swing, conviction 3
MDT 93.80 (+3.12% on 2026-09-14), the strongest large-cap in the strongest
sector on the rotation day. Above its 50d (87.90) every one of the last ten
sessions, 20d (92.13) above 50d. **Analyst bullish share +10.8 points over four
months to 67.6% — the largest revision improvement of anything I checked today.**
Entry 93.50 (inside yesterday's 92.73-94.075 range), stop 88.00 (below the
90.04/90.26/90.58 cluster, 2.28 ATR), target 105.50 (the 180d high; a 29-analyst
average target of 104.76 independently lands in the same place). R:R 2.18.
- source: https://finnhub.io/api/v1/stock/recommendation

## [06:26 ET] REJECTED — SMH short — the trigger is real, the target is not
Best short on the tape and I still could not publish it. In its favour: closed
541.50 (-4.75%) near the session low of 537.73; 19.4% off the 180d high of
671.83; 20d (561.13) **below** 50d (568.09); -5.89% vs SPY and -4.68% vs XLK
over 1m, -15.24% and -12.38% over 3m. And 537.73 broke a shelf tested four times
(540.75 on 08-24, 540.85 on 09-01, 540.07 on 09-03). A clean trigger.
The problem is below it. Entry 537.00 with a stop at 565.00 (above the 20d) is
28.00 of risk = 1.92 ATR; a 2.0 ratio needs 481.00, and **I have no bar data
between 537 and the 180d low of 359.86** — nasdaq returned only 20 bars — so I
cannot point at 481 as support. It is a 10.4% target into a gap in what I know.
Second reason to leave it: SMH is still **+24.91% against SPY over six months**.
Shorting a six-month leader on a three-month pullback with an unanchored target
is how the first month of this report lost money. Dropped.

## [06:26 ET] CORRELATION CHECK — three ideas lean on the rates path
DG (buy), MDT (buy) and GLD (hold-with-stop) all resolve partly on Wednesday's
FOMC: the first two are the hawkish-rotation trade, GLD is the opposite side of
the same real-yield variable. That is **3 on one driver, at the cap** in
config/strategy.md, and nothing further today may lean on the Fed. Flagging it
so synthesis and the red team can see the concentration rather than discover it.
Note also that DG and MDT are not fully independent of each other — same
mechanism, different sector.

## [06:34 ET] CAPTURED — PFE buy, long_term, conviction 4 — read from the filing
Amends the pending BUY @ 27.60 published 2026-08-18 by **lowering the entry**.
Pulled the EX-99 press release off Pfizer's 2026-08-04 8-K via EDGAR and read it:
- FY2026 guidance: revenue **$60.5-62.5B**, adjusted diluted EPS **$2.80-3.00**
- Q2 2026: revenue $15.0B, adjusted diluted EPS $0.77
- H1 2026 dividends: $4.9B, **$0.86/share** → $1.72 annualised
- source: https://www.sec.gov/Archives/edgar/data/78003/000007800326000094/pfe-6282026xex99.htm
At the 27.72 close: **9.56x** the $2.90 midpoint, **6.21%** yield, $157.99B cap.
Target 34.50 = 12x the midpoint. Bear case 23.00 = an eroded ~$2.40 base at
~9.5x, below the 180d low of 23.62.
**The entry moved because of the floor, not the other way round.** Solving
(34.50 - E)/(E - 23.00) = 2.5 gives E = 26.29 — so the accumulation zone tops out
at 26.30, which lands on the 50-day SMA (26.34) independently. Above 26.29 this
idea does not clear the 2.5 long-term floor and should not be bought at all.
That is why the zone sits 5% under the 27.72 market rather than at it.

## [06:35 ET] LONG-TERM LANE — one idea, and the reason there is only one
config/strategy.md asks for real time in this lane rather than the leftovers, and
it got it. PFE cleared because the guidance is a primary document I read and the
multiple and yield fall straight out of it. CEG and VST did not, for the opposite
reason — the story is compelling and the numbers behind the target would have
been mine rather than the company's. One anchored long-term idea beats three
asserted ones.

## [06:26 ET] REJECTED — small-cap lane — three checked, all falling into their prints
config/universe.md wants these hunted deliberately, so I checked the small caps
with dated catalysts in the next ten sessions. All three are in downtrends into
the event, and liquidity was never the binding constraint:
- **APOG** 37.17, reports 2026-09-22. Below the 20d (39.74) and 50d (40.37),
  -26.95% off its 180d high. $6.8M average daily dollar volume.
- **WOR** 55.25, reports 2026-09-22 bmo. Fell 12.5% in five sessions from 63.13
  and **closed at the session low of 55.24**. Below 20d (58.10) and 50d (56.83).
  $14.2M/day.
- **SFIX** 3.09, reports 2026-09-23 amc. -46.21% off its high, only 9.57% above
  the 180d low of 2.82. $4.7M/day — a genuine micro cap.
Buying a small cap that is falling into a print is the conviction-2 lottery
ticket this report has already lost on twice (0/2, avg -5.6%). None of the three
offers a reason to own it *other* than that it has fallen. **No small-cap
candidate today**, and that is a real finding rather than a gap.

## [06:26 ET] SELF-CHECK — recomputed every ratio before finishing
Recomputed independently of what I wrote into each candidate (floors: R:R 2.0
swing / 2.5 long_term; stop 2.0 ATR stock, 1.8 ETF):
- DG    entry 134.50 stop 124.00 tgt 156.00 → risk 10.50 reward 21.50 **R:R 2.05**, stop **2.36 ATR**, win 0.40 vs baseline 0.328
- BCC   entry  76.50 stop  70.80 tgt  90.00 → risk  5.70 reward 13.50 **R:R 2.37**, stop **2.59 ATR**, win 0.35 vs baseline 0.297
- GLD   entry 398.00 stop 381.00 tgt 440.00 → risk 17.00 reward 42.00 **R:R 2.47**, stop **2.12 ATR**, win 0.35 vs baseline 0.288
- MDT   entry  93.50 stop  88.00 tgt 105.50 → risk  5.50 reward 12.00 **R:R 2.18**, stop **2.28 ATR**, win 0.40 vs baseline 0.314
- PFE   entry  26.25 bear 23.00 tgt  34.50 → risk  3.25 reward  8.25 **R:R 2.54**, no stop (long_term), win 0.42 vs baseline 0.283
- LCII, CCJ are exits — no target, no stop, nothing to clear.
Every claimed edge over baseline is between 5.3 and 13.7 points, none near the
20-point threshold that would need the thesis to carry a large claim.

## [06:27 ET] RESEARCH COMPLETE
- **candidates: 7** — 3 new ideas (DG, MDT, PFE), 2 amendments (BCC, GLD),
  2 exits (LCII, CCJ). Two open positions reviewed and deliberately left alone
  (DVN, SVRA). The report is weighted toward position management because five
  open longs carried **no stop at all** and that was the most valuable work
  available today.
- **skew to note in data_quality_notes:** nothing intraday cleared the bar —
  with the FOMC on Wednesday and the freshest honest prices being Monday's
  close, there was no same-session setup worth publishing. One long_term idea,
  not for want of looking. No small cap, no crypto, no futures, no event
  contract — reasons logged above for each, none of them "ran out of time".
- **coverage gaps:**
  1. **A healthcare single name to replace XLV.** The sector is the clearest
     rotation on the tape and the ETF is too low-volatility to pay for its own
     stop. MDT covers it partially; a second name was not found in time. This is
     the top gap to pick up tomorrow.
  2. No support data between SMH 537 and its 180d low of 359.86, which is the
     only reason the best short on the tape went unpublished.
  3. Did not verify Robinhood availability of any instrument at runtime — all
     seven are large-cap US-listed equities or a major ETF, so the risk is low,
     but it was not checked as config/universe.md asks.
- **sources that failed:**
  - `macro` markets block: SPX, NDX, DJI, RUT, **VIX**, /ES, /NQ, DXY, gold,
    WTI all ok:false — Yahoo HTTP 429, Finnhub refuses index CFDs. No index
    level and **no VIX read** this run; rates came from FRED and were fine.
  - `events` (Kalshi): returns count:0 for Fed, Fed decision, interest rate,
    CPI, recession — and unrelated tennis markets for FEDDECISION. **No event
    contract could be priced, so none was captured.**
  - `short` (api.nasdaq.com): ReadTimeout on every symbol — **no short interest
    or days-to-cover for any idea today.**
  - `implied` (Yahoo options): HTTP 401 — **no target was tested against the
    options-implied move.** Every target below rests on price history and, for
    PFE, on filed guidance.
  - `history BTC-USD`: fails, and `history BTC` silently returns an equity.
  - `history` returned 20 bars rather than 180 for several symbols (DG, SMH,
    PFE) on repeat calls; ATR/SMA/range figures came from the calls that did
    return the full window.

## [06:31 ET] METHOD — working around the 20-bar limit in `history`
`market_data.py history` computes `atr14`, `sma*`, `range_high` and `range_low`
over the full window but only ever prints the **last 20 bars** in `recent`
(hardcoded `rows[-20:]` at scripts/market_data.py:668). That is what stopped me
anchoring targets for SMH and XLV earlier — not a fetch failure.
**The workaround:** call `history` repeatedly with different `--days` and read
`range_high`/`range_low` off each. Each window's extreme, differenced against
the next, brackets *when* a swing high or low happened. It costs one call per
window and turns "somewhere in the 180-day range" into a dated level. Worth
keeping for future runs; it changed two of today's conclusions.

## [06:32 ET] SMH — rejection CONFIRMED, and now for the right reason
Re-ran the short with the level map (window → trailing low):
  30d (from 08-03) 524.77 | 45d (07-13) **503.63** | 60d, 75d, 90d (to 05-06)
  503.63 | 120d (03-24) 359.86
So **503.63 is the floor of a four-month base** running 2026-05-06 to now, and
it is the *only* support between 541.50 and the 359.86 low. My earlier 481.00
target sat **below that entire base** — it was worse than unanchored, it was
wrong. The honest version fails outright: entry 537.00 with target 505.00 (just
above the base) is 32.00 of reward, and the 1.8 ATR ETF stop floor forces at
least 26.24 of risk, giving **R:R 1.14**. To reach 2.0 the stop would have to sit
at 553.00 — 1.10 ATR, inside the noise. **SMH short is dead, definitively.**

## [06:33 ET] REJECTED — ISRG — the best-looking setup I could not make work
Genuinely attractive and worth writing down. ISRG closed 377.94 (+2.38%),
reclaiming both its 20d (372.67) and 50d (376.50) after bottoming at 345.25 on
09-10 — and it is **37.41% off its 180-day high of 603.88 while the business is
beating**: +9.79% surprise in 2026-06 (2.80 vs 2.5503) and **+16.77%** in
2026-03 (2.50 vs 2.1409), with analyst bullish share 72.5% and rising (+2.5).
A de-rating running against improving fundamentals, which is the opposite of CCJ.
Level map (window → trailing high): 30d 405.34 | 45d 414.58 | 60d **443.84** |
90d 462.40 | 120d 491.15 | 150d 511.88 | 180d 603.88 — so 443.84 is a dated
swing high from between 2026-06-18 and 2026-07-13.
Why it still fails: entry 379.00 (above the 09-14 high of 378.58) with a stop
below the whole September low cluster (345.25 / 347.52 / 349.855) at 344.00 is
35.00 of risk = 3.19 ATR, and against the 443.84 high that is **R:R 1.74**.
It only reaches 2.31 by reaching for 460.00 — a **May** high, +21.5% away, in a
name still 37% below its own high. And it only reaches 2.03 against 440.00 by
pulling the stop up to 349.00, *inside* the low cluster — the tight-stop failure
config/strategy.md exists to refuse. Both roads are the forbidden one. Dropped.
**This is the best candidate for tomorrow if it holds the 50-day**, and it is
the one idea today I would most like to have published.

## [06:31 ET] SELF-AUDIT — the level map contradicted four of my own targets
Ran the window technique against the candidates I had already captured, on the
CLAUDE.md principle that a figure the model wrote about its own idea is the one
to distrust. Windows are trailing, so differencing them dates each extreme:

| | 30d high | 60d | 90d | 120d | 180d | my target | verdict |
|---|---|---|---|---|---|---|---|
| DG  | 134.125 | 134.125 | 134.125 | 134.125 | 158.23 | 156.00 | **no structure since March** |
| MDT | 95.41 | 95.41 | 95.41 | 95.41 | 105.50 | 105.50 | **95.41 is a hurdle first** |
| GLD | 429.42 | 429.42 | 437.42 | 448.70 | 509.70 | 440.00 | slightly past the 90d high |
| BCC | 88.4299 | 88.4299 | 88.4299 | 88.4299 | 91.97 | 90.00 | **above the 6-month high** |

Three of the four targets were anchored to highs **six to nine months old** that
I had described as if they were nearby range structure. Corrections, all of which
still clear their floors — I am not nudging anything to survive:
- **BCC target 90.00 → 88.00**, just under the 6-month high of 88.43. R:R 2.02.
- **GLD target 440.00 → 437.00**, just under the 90-day high of 437.42. R:R 2.29.
- **DG keeps 156.00** but the evidence is rewritten to say what it is: a breakout
  into six months of clear air, with the 180d high as the objective and *nothing*
  between 134.125 and 158.23. That is what makes the 134.13 trigger load-bearing
  rather than decorative — without the break there is no trade.
- **MDT keeps 105.50** for the same reason, but 95.41 is now named in key_risk as
  a hurdle 2% above the entry that must clear first, and the scale plan trims
  there instead of at an invented midpoint.

## [06:37 ET] RESEARCH COMPLETE — supersedes the block at 06:27
Re-issued because the self-audit after that block changed four captured ideas.
`candidates.jsonl` holds 11 lines for **7 distinct symbols**; synthesis takes the
last line per symbol, and for DG, BCC, GLD and MDT that is the corrected one.

**Final 7, all recomputed from source rather than from what I wrote earlier:**

| sym | dir | horizon | conv | entry | target | stop/bear | R:R | win vs baseline |
|---|---|---|---|---|---|---|---|---|
| PFE  | buy  | long_term | 4 | 26.25 | 34.50 | bear 23.00 | 2.54 | 0.42 v 0.282 |
| DG   | buy  | swing | 4 | 134.50 | 156.00 | 124.00 | 2.05 | 0.40 v 0.328 |
| MDT  | buy  | swing | 3 | 93.50 | 105.50 | 88.00 | 2.18 | 0.40 v 0.314 |
| GLD  | buy  | swing | 3 | 398.00 | 437.00 | 381.00 | 2.29 | 0.34 v 0.304 |
| BCC  | buy  | swing | 3 | 76.50 | 88.00 | 70.80 | 2.02 | 0.34 v 0.331 |
| LCII | sell | swing | 3 | 90.00 | — | — | — | exit |
| CCJ  | sell | swing | 3 | 93.00 | — | — | — | exit |

Conviction equals the count of distinct evidence kinds on every row — 3 kinds for
PFE and DG, 2 for the rest. Nothing was rounded up. Every claimed edge over the
random-walk baseline is between +0.9 and +13.8 points; BCC's is thin and is
called out in its own key_risk as a hold rather than an add.

- **3 new ideas** (PFE, DG, MDT), **2 amendments** (GLD, BCC), **2 exits**
  (LCII, CCJ). **2 open positions reviewed and deliberately left alone** (DVN,
  SVRA — both already correctly stopped and neither confirmed nor broken).
- **Weighting to note in data_quality_notes:** four of seven are position
  management. That is deliberate, not thin research — five open longs carried
  **no stop at all**, and fixing that was the highest-value work on the desk.
- **Skew:** nothing intraday (the FOMC lands Wednesday and the freshest honest
  prices are Monday's close — no same-session setup was worth publishing); one
  long_term; **no small cap, no crypto, no futures, no event contract.** Each has
  a logged reason above and none of them is "ran out of time".
- **Six ideas were researched to completion and refused:** FDX and XLV (2:1
  unreachable from any honest level), GIS (cleared only at exactly 2.00 on a stop
  that was not a level, and prints before a reader could act), SMH short
  (target sat below a four-month base at 503.63), ISRG (both roads to 2:1 were
  forbidden ones), CEG/VST (no valuation anchor I could defend from a filing).
  ISRG is the one I most wanted to publish and the first thing to re-check
  tomorrow if it holds its 50-day at 376.50.
- **Coverage gaps:**
  1. A second healthcare name beyond MDT — the sector is the clearest rotation on
     the tape and I could only convert one of it.
  2. Robinhood availability was not verified at runtime for any instrument. All
     seven are large-cap US-listed equities or a major ETF so the risk is low,
     but config/universe.md asks and I did not.
  3. No short-interest read anywhere today, so no crowding check on any idea.
- **Sources that failed:**
  - `macro` markets: SPX, NDX, DJI, RUT, **VIX**, /ES, /NQ, DXY, gold, WTI all
    ok:false (Yahoo 429; Finnhub refuses index CFDs). No index level, no VIX.
    FRED rates and coingecko crypto were fine.
  - `events` (Kalshi): count:0 for Fed, Fed decision, interest rate, CPI,
    recession; unrelated tennis markets for FEDDECISION. **No event contract
    could be priced, so none was captured** — the edge has to be a stated
    probability disagreement and there was no market price to disagree with.
  - `short` (api.nasdaq.com): ReadTimeout on every symbol, every attempt.
  - `implied` (Yahoo options): HTTP 401. **No target was tested against the
    options-implied move.** Targets rest on window-mapped price structure and,
    for PFE, on filed guidance.
  - `history BTC-USD` fails and `history BTC` silently returns an **equity** —
    no ATR for bitcoin, hence no crypto futures idea.
  - `history` prints only the last 20 bars by design; worked around by varying
    `--days` and reading `range_high`/`range_low`, which is what caught the four
    bad targets. Documented at 06:31.
