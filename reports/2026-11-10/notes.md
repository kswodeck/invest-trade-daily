# Research log — 2026-11-10

## [06:04 ET] SESSION FRAME
Prices below are the **2026-11-09 close** (asof 21:00 UTC, age ~841 min, session=pre).
At 06:00 ET the freshest honest equity price is the prior close. Not stale — closed market.

Yesterday (Mon 2026-11-09) was a broad risk-on session. Open-position closes:
- AAL +7.4% to 14.16 (I am SHORT from 13.35, stop 14.40 — 1.7% from stop)
- HII +5.4% to 304.36 | ACM +5.2% to 70.21 | RTX +3.6% to 196.31
- BCC +3.3% to 72.57 | UNP +2.4% to 297.01 | XLU +1.5% to 43.79
- PYPL +1.4% to 60.05 | XLE +0.5% to 61.94 | ABT +0.5% to 110.51
- PFE -0.5% to 29.23 | KHC -0.8% to 24.42
Airlines + defense + industrials + utilities all up together = index-level bid, not stock picking.

## [06:04 ET] DATA GAP — macro index quotes
`market_data.py macro`: spx/ndx/dow/russell2000/vix all ok:false.
- finnhub: "Market data subscription required for CFD indices"
- yahoo: HTTP 429 on both query1/query2 hosts
- stooq: 404 on ^-prefixed symbols
- alphavantage: no api key
Index levels unavailable this run. Will proxy regime with ETF quotes (SPY/QQQ/IWM/VIXY) instead.

## [06:11 ET] MACRO — the regime, and why yesterday's rally is not the whole story
Closes 2026-11-09 vs structure (history --days 90, finnhub):

| Px | Close | SMA20 | SMA50 | ATR14 | % off 90d high |
| --- | --- | --- | --- | --- | --- |
| SPY | 752.69 | 762.09 | 765.35 | 11.98 (1.59%) | -3.7% |
| QQQ | 679.35 | 704.30 | 720.23 | 17.62 (2.59%) | **-10.95%** |
| IWM | 282.51 | 277.07 | 281.84 | 5.05 (1.79%) | -7.43% |

**The key structural fact:** after a +2.4% SPY / +3.5% QQQ day, SPY and QQQ are
*still below both* their 20- and 50-day. QQQ sits 5.7% under its SMA50 and is
-11% off its high — a correction, not a dip. But **IWM closed back above both**
its SMA20 (277.07) and SMA50 (281.84). Small caps are the only one of the three
that has reclaimed its trend. That is a rotation read, not a beta read.

Rates/FX/commodities:
- US10Y 4.86% (FRED DGS10, 2026-11-06), prev 4.84. US2Y 4.51 (from 4.46).
  10y2y +0.32 (2026-11-09, from 0.35). Fed funds effective 3.88%.
- TLT 81.96, +0.05% — bonds did NOT rally with stocks. A +2.4% equity day with
  flat 20y and a 4.86% 10y is a risk-appetite move, not a rate-cut move.
- Unemployment 4.1% (Oct, from 4.2%). DXY proxy UUP 28.97 -0.55%.
- GLD 379.53 +1.88%; USO 142.66 **-3.87%**.
- VIXY 18.21, **-13.4%** — volatility crushed in one session.
- BTC 74,155 (+0.11% 24h), ETH 2,089.43 (-0.79%), SOL 84.40 (-1.65%).
  Crypto did NOT participate in the equity rally. Noted — that matters below.
sources: scripts/market_data.py macro | quote | history (finnhub/FRED/coingecko)

## [06:12 ET] MACRO — the narrative, sourced
- S&P fell **2.7% last week, a fourth consecutive weekly decline**; Nasdaq
  -3.4% and into correction. Worst S&P week since April 2025. ~$2.5T of AI
  market value wiped out. — source: https://www.cnbc.com/2026/11/09/ai-selloff-stock-market-year-end-rally.html
  and https://www.cnn.com/2026/11/05/markets/asian-markets-us-rout-ai-investment-intl-hnk
- Taiwan's benchmark -8%+ on the week, TSMC limit-down, Taiwanese officials
  asked state banks to support prices. — source: https://www.cnn.com/2026/11/05/markets/asian-markets-us-rout-ai-investment-intl-hnk
- Morgan Stanley (Wilson): "correction is entering its final phase... S&P
  catches down to breadth and approaches our **7100-7300** downside range. A
  final retest of last week's lows likely sets up a year-end rally."
  — source: https://www.cnbc.com/2026/11/09/ai-selloff-stock-market-year-end-rally.html
  NB SPY 752.69 implies S&P ~7,527. Wilson's own range is **3-6% below here.**
- Bear tell: **CoreWeave 5y default insurance above 1,000bp** (Reuters via
  Decrypt). AI capex is now a credit story, not just a multiple story.
  — source: https://decrypt.co/382770/ai-chip-stocks-bounce-global-rout-bubble-starting-burst
- Midterms 2026-11-03/04: **Democrats took both chambers.** S&P +1.72% to
  7,698.80 on 11-04; crude fell hard on a lower Iran escalation premium.
  Traders since reading a possible **slowdown in data-center buildout**.
  — source: https://www.bostonglobe.com/2026/11/04/business/midterms-stock-market-reaction-2/
  and https://stocktwits.com/news-articles/markets/equity/dow-s-and-p-500-nasdaq-futures-mixed-as-traders-weigh-ai-rebound-await-inflation-data-hims-ttd-nvda-mara-in-focus/

**Regime conclusion driving today's bar.** This is a fourth-down-week AI
correction with one violent two-day bounce on top, into still-broken trend, with
the 10y at 4.86% refusing to help. Chasing beta long at the top of a +2.4% day
is the single worst entry this report could make — and the track record says so
independently: 4/39 targets (10%), avg -5.9%, with pullback-reflex entries the
named culprit. So today: **raise the bar, favour what the rotation is going TO
(small caps, non-AI cash flows), demand a dated catalyst, and do not pay up.**

## [06:05 ET] CALENDAR — dated catalysts inside 10 sessions
source: scripts/market_data.py earnings --days 12 (finnhub), filtered to rev est >$1.5B

- **2026-11-10 (TODAY) amc: CRWV (CoreWeave)** — the single most loaded event on
  the tape. This is the name whose 5y default insurance just went through
  1,000bp. Also today: SE, VG, TDG, BN, ATAT (all bmo except CRWV).
- 2026-11-11: CTVA(amc), NIO
- 2026-11-12: **CSCO(amc), AMAT(amc)**, NU, STNE
- 2026-11-16: **ACM(amc)** <- I hold this, PDD, BIDU, TSN, XPEV
- 2026-11-17: **NVDA(amc)** <- awaiting entry @184, HD, **DIS(bmo)**, WSM
- 2026-11-18: **TGT, LOW(bmo), TJX, ROST, GAP, PANW**
- 2026-11-19: **WMT, BABA, INTU**, NTES, KEYS
- 2026-11-20: BJ

Two observations that shape the day:
1. **The AI complex has a dated test tonight (CRWV) and the decider on 11-17
   (NVDA).** Any AI-adjacent idea captured today is really a bet on those two
   prints. Correlation cap applies hard: no more than 3 ideas on that driver.
2. **Consumer/retail is the week-after story** (HD, TGT, LOW, TJX, ROST, WMT,
   GAP all 11-17..11-19). That is a genuinely *separate* driver from AI capex,
   which is what a report in a correlated tape needs.

## [06:06 ET] REJECTED — CRWV — earnings tonight, cannot be entered responsibly
Reports amc today, so any entry is a pre-print coin flip on the most levered
story in the market (CDS >1,000bp). No level set on real support would survive
the gap either way. Not an idea; it is the thing the other ideas have to survive.

## [06:08 ET] DATA GAP — event contracts unavailable this run
`market_data.py events` returned **count 0** for: "CPI", "inflation",
"recession", "interest rate", "fed funds", "Bitcoin", "S&P 500", "GDP",
"unemployment". The one query that returned anything ("Fed", count 2) returned
two Kalshi multi-category **sports** parlays with all price fields null.
So there is no usable macro event-contract pricing this run and **no event
contract candidate can be honestly captured today** — the edge has to be a
stated probability disagreement against a real implied price, and there is no
implied price to disagree with. Not padding this lane with a guess.
Also note: `KXCPIYOY-26SEP-T3.5` NO @18 still sits in "awaiting entry" from
2026-09-30 — a **September** CPI contract, i.e. long resolved/expired. It should
be retired from the awaiting-entry list rather than carried.

## [06:14 ET] POSITION UPDATE — AAL — short opened 2026-10-03 @ 13.35, now 14.16 (-6.1% against)
- decision: **CLOSE.** Buy to cover at the open.
- why: 14.16 is above both SMA20 (12.59) and SMA50 (12.89) and out of the quarter's
  range. ATR 0.6729. Stop 14.40 is 0.24 away = **0.36 ATR** — resolved by noise.
  Cost side turned: USO -3.87% on 11-09, crude repriced lower on the removed Iran
  premium. Cheap fuel is an airline short's own argument in reverse.
- action: captured via add_candidate.py as an update, action = CLOSE IT.

## [06:15 ET] POSITION UPDATE — XLE — long opened 2026-08-15 @ 63.9, now 61.94 (-3.1%)
- decision: **CLOSE.** 87 days held, thesis driver changed not just stalled.
- why: below SMA20 66.91 AND SMA50 65.06; -11.7% off 90d high. USO -3.87% on a
  day SPY was +2.37% = energy-specific. Stop 60.8 = 0.63 ATR, hit on an ordinary
  day. Re-levelling tested and fails: at the 1.8 ATR ETF floor (58.66) the ratio
  from 63.90 entry is **1.26**, under the 2.0 swing floor. Cannot be rescued by
  moving levels.
- note the one real counter: XLE +0.52% while USO -3.87% — the sector may have
  already discounted the barrel. That is a long_term accumulation argument with a
  stated bear price, not this swing position. Not shorting it.
- action: captured via add_candidate.py as an update, action = CLOSE IT.

## [06:10 ET] POSITION UPDATES — the rest of the book (all prices = 2026-11-09 close)

| Sym | Entry | Last | % | SMA20 | SMA50 | ATR14 | Target | Stop | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HII | 262.0 | 304.36 | +16.2% | 286.11 | 278.94 | 13.01 | 339.76 | none→**278** | hold, ADD STOP |
| PYPL | 56.5 | 60.05 | +6.3% | 57.43 | 55.22 | 1.66 | 62.7 | 54.1→**56.73** | hold, raise stop |
| ACM | 66.74 | 70.21 | +5.2% | 62.44 | 62.28 | 2.08 | 77.22 | 61.5 (keep) | hold, TRIM HALF 11-16 |
| ABT | 103.0 | 110.51 | +7.3% | 105.94 | 103.97 | 3.51 | 117.34 | 97.0 | hold as-is |
| UNP | 288.6 | 297.01 | +2.9% | 295.23 | 286.49 | 7.86 | 315.99 | 277.4 | hold as-is |
| KHC | 23.0 | 24.42 | +6.2% | 24.13 | 23.98 | 0.77 | 28.09 | 21.2 | hold as-is |
| XLU | 43.3 | 43.79 | +1.1% | 42.68 | 41.79 | 0.64 | 46.6 | 41.8 | hold as-is |
| RTX | 199.0 | 196.31 | -1.3% | 194.15 | 193.15 | 5.94 | 226.5 | 186.0 | hold as-is |
| PFE | 27.6 | 29.23 | +5.9% | 29.80 | 28.77 | 0.79 | 42.0 | none (LT) | hold, see below |
| BCC | 76.5 | 72.57 | -5.1% | 75.49 | 75.67 | 3.60 | 110.0 | none (LT) | hold, FLAG |

Captured as updates (action required): **AAL close, XLE close, HII add stop,
PYPL raise stop, ACM trim-half plan.** The seven marked "hold as-is" need no
change: each is above its stop with the stop at a defensible distance and the
thesis unchanged, and re-pitching them would be exactly the repetition the
prior-context guard warns about. Logged here rather than captured, deliberately.

Three notes on the holds:
- **HII was carrying no stop at all while +16.2%.** The 2.03-ATR stop at 278.00
  lands just under the SMA50 (278.94) — confluence, not a round number. This is
  the single most valuable change in today's book.
- **RTX reclaimed both MAs** (196.31 vs 194.15/193.15) after being -4.8% at the
  last check. Risk 199→186 = 13 = 2.19 ATR ✓; reward 27.5 → R:R 2.12 ✓. Target
  226.5 ≈ the 90d high 226.88, a real level. No change warranted.
- **UNP target 315.99 IS its exact 90d high** — fine, but it is 6.4% away and
  297.01 is only 0.6% over the SMA20. Marginal. Holding, not adding.

## [06:11 ET] FLAG — BCC — long_term position with no stated invalidation
BCC 72.57: below SMA20 75.49 AND SMA50 75.67, -17.9% off the 90d high 88.43, and
only **+3.6% off the 90d low (70.05)**. Target 110 with no stop, held 83 days,
-5.1%. ATR 4.97% — a volatile name.
This is the position I am least able to defend and I am not going to pretend
otherwise. A `long_term` idea is required to carry an explicit invalidation
condition and this one does not have one on the record; "the price fell" is not
an invalidation, but nor is "target 110" a thesis. Synthesis should carry it as
**hold with an explicit flag that the bear case was never priced** — the
long_term lane is 0/4 with avg -15.2%, which is the worst category in the book.
Not capturing a re-pitch: adding levels now would be inventing the research the
original idea skipped.

## [06:14 ET] SECTOR — consumer/retail into the 11-17..11-19 earnings cluster
Closes 2026-11-09, history --days 90. The whole complex is at its highs, which
makes it a *selling* setup, not a buying one:

| Sym | Close | SMA20 | SMA50 | %vs SMA50 | % off 90d high | Reports |
| --- | --- | --- | --- | --- | --- | --- |
| LOW | 232.10 | 206.01 | 197.62 | **+17.4%** | -1.13% | 11-18 bmo |
| HD | 353.42 | 324.23 | 309.85 | **+14.1%** | -2.49% | 11-17 |
| WMT | 125.66 | 121.21 | 112.93 | +11.3% | -4.67% | 11-19 |
| DIS | 119.12 | 112.42 | 108.26 | +10.0% | -1.39% | 11-17 bmo |
| TGT | 165.90 | 154.93 | 156.47 | +6.0% | -2.84% | 11-18 |
| ROST | 237.00 | 233.40 | 231.07 | +2.6% | -7.78% | 11-18 |
| GAP | 22.23 | 22.61 | 22.29 | -0.3% | -13.84% | 11-18 |
| **TJX** | **138.13** | **142.40** | 135.85 | **+1.7%** | **-15.28%** | **11-18** |

**REJECTED as longs — HD, LOW, WMT, TGT, DIS:** all within 4.7% of a 90-day
high and 6-17% above their 50-day, reporting inside 10 sessions. Buying a stock
at its high into a print means the good news is the price. No entry exists here
that is not a reflex discount, and the stop would have to sit 10%+ away under
the 50-day. This is the clearest "do not pay up" cluster on the tape.

**TJX is the one genuine divergence.** Off-price retail is 15.3% off its high
and *below* its 20-day while full-price retail (HD/LOW) sits within 2.5% of
highs. Either the trade-down consumer thesis is broken, or TJX is the one name
in the group not priced for a good print. Worth real work — following up.

## [06:15 ET] ROTATION — the small-cap read is measured, not a vibe
`relstrength IWM --peer SPY`:
- 1m: IWM **+1.28%** vs SPY **-3.32%** → **+4.60% relative**
- 3m: IWM -6.14% vs SPY -2.32% → -3.82% relative
- 6m: IWM -0.99% vs SPY +1.81% → -2.80% relative
Leadership: "outperforming SPY on 1m".

The 1m window **is** the window in which the Nasdaq fell into correction. Small
caps rose 1.28% while SPY fell 3.32% through an AI-led drawdown. That is a real
rotation out of mega-cap AI, not high-beta tagging along — if it were beta, IWM
would have fallen harder, which is exactly what it did over 3m and 6m.

Structure (IWM, --days 200): close 282.51 vs **SMA20 277.07, SMA50 281.84,
SMA200 279.09 — above all three.** ATR14 5.05 (1.79%). 90d range 269.875-305.18.
SPY and QQQ are both still below their SMA20 and SMA50. IWM is the only major
index ETF that has reclaimed its trend.

## [06:17 ET] REJECTED — TJX — lagging its own sector by 12.8% over 3m, insiders net -$27.7M
Tempting and it does not survive. The bull case was real: **TJX has beaten
estimates four quarters in a row** (surprise +1.63%, +15.94%, +1.89%, +3.70%;
`beats_last_4: 4`) and at 138.13 it is 15.3% off its high while HD and LOW sit
within 2.5% of theirs — the trade-down consumer should own this.

What killed it, both from fetched data:
- `relstrength TJX --peer XLY`: **1m -7.68%, 3m -12.79%, 6m -8.61%** relative to
  consumer discretionary. XLY returned +7.23% over 1m; TJX returned about
  -0.45%. This is the precise case `config/strategy.md` tells me to refuse —
  not buying leadership but catching something falling relative to everything
  around it. A 15% discount to its own high while its sector makes new ones is
  not a divergence I get to arbitrage; it is the market pricing something.
- `insiders TJX`: **0 open-market buys, 8 sells, $27.7M sold, net -$27.7M** over
  6 months. Sales are weak evidence alone, but zero buys removes the one leg
  that would have made a lagging name a contrarian buy.
Four straight beats with no insider willing to buy a 15% drawdown is the tell.
No candidate captured.

## [06:22 ET] POSITION UPDATE — ONON — pending order reports in ~3 hours. CANCEL IT.
The highest-urgency item found today. Pending BUY @ 34.20 from 2026-11-03.
ONON closed 37.53 (SMA20 34.97, SMA50 31.69, -4.33% off 90d high 39.23) and
**reports bmo today 2026-11-10** (finnhub calendar, EPS est 0.4046, rev $0.95B).
- The standing limit is **8.9% below the market with a print 3 hours away.** The
  only way it fills is a gap down on a miss. It is not an entry, it is a
  commitment to buy the outcome that falsifies the thesis — the adverse-selection
  pattern strategy.md names (42% of month-one pullback entries filled; the ones
  that filled were the ones falling).
- It also fails on its own numbers independent of the print: 2.0 ATR stop =
  31.07, risk 3.13, reward to 39.23 = 5.03, **ratio 1.61 < 2.0 floor**.
- ONON `beats_last_4: 4` (+87.4%, +20.9%, +51.5%, +1.8%) but revision_direction
  **deteriorating**, bullish share -1.7pts.
- decision: **CANCEL before 09:30 ET**, reassess post-print.
- action: captured via add_candidate.py, wait=true, action=CANCEL.

## [06:24 ET] VENUE CHECK — /M2K on Robinhood
Robinhood's own site (invest.robinhood.com futures page) lists **/M2K Micro
Russell 2000 Index Futures — $5 multiplier, tick 0.1 = $0.50, cash settled,
6 PM-5 PM** alongside /RTY. 2025 launch coverage says RH began with CME products
on the S&P 500, Nasdaq-100, **Russell 2000** and Dow.
— source: https://invest.robinhood.com/us/en/about/futures/
  and https://www.fow.com/insights/robinhood-starts-rolling-out-flagship-cme-futures
**Conflict recorded honestly:** one third-party 2026 guide
(firstcard.app/learn/robinhood-futures-trading) lists only S&P 500 and
Nasdaq-100 micros and omits the Russell. Robinhood's own domain outranks a
third-party summary, so I am treating /M2K as available, but the reader should
confirm in-app before placing it — RH's support pages themselves say the in-app
futures search is the authoritative product list.

## [06:28 ET] LEVELS — IWM long (the rotation expressed in the instrument I can price)
Captured. entry 277.00-279.50 (ideal 278.00) / target 298.50, t2 305.00 / stop 268.80
- risk 9.20 = **1.82 ATR** (ETF floor 1.8 ✓) | reward 20.50 | **R:R 2.23** ✓
- baseline win prob 1/(1+2.23) = 0.31; claimed **0.42** = 11 pts of asserted edge
  (deliberately under the 20-pt "large claim" line)
- entry confluence: SMA20 277.07 + SMA200 279.09 | stop just under the 90d low 269.875
- `relstrength IWM --peer QQQ`: **1m +10.85%**, 3m -0.70%, **6m +3.77%**

**Why IWM and not /M2K, against the universe doc's futures preference.** I could
not source a Russell 2000 *index* level this run: `macro` returned
russell2000 ok:false, and `quote` on both `RTY` and `^RUT` returned ok:false.
Setting /M2K entry/target/stop would mean converting from IWM by a remembered
divisor — a fabricated number, which rule 2 forbids outright. The futures
preference also does its real work on *short* and leveraged views; this is a
long, so IWM needs no margin and loses nothing by being spot. Recorded as a
deliberate departure with a reason, per universe.md ("Say which and why").

## [06:29 ET] DATA GAP — options-implied move unavailable
`market_data.py implied IWM --entry 278 --target 298.5` → ok:false,
yahoo-options **HTTP 401 Unauthorized**. So no implied-move sanity check on any
candidate this run, for IWM or anything else. Targets are set from the 90-day
range and ATR only. Synthesis should say so: the usual "is the target inside
what options price" check did not run.

## [06:33 ET] INSIDER SCAN — 33 small/mid caps checked, 6-month open-market window
`market_data.py insiders` across today/this-week reporters plus a cross-sector
sweep. Net sellers dominate; the clusters worth naming:

| Sym | buys | distinct buyers | buy $ | sells | net $ | note |
| --- | --- | --- | --- | --- | --- | --- |
| IBP | 27 | 4 | 1,042,804 | 1 | **+785,357** | see rejection below |
| REZI | 3 | 3 | 848,115 | 0 | **+848,115** | **reports amc TODAY** |
| GO | 3 | 2 | 356,400 | 1 | +340,218 | **reports amc TODAY** |
| EYE | 1 | 1 | 776,000 | 0 | +776,000 | single buyer, reports 11-12 |
| BRC | 1 | 1 | 1,000,025 | 2 | +384,584 | single buyer |
| LBRT | 4 | 4 | 895,638 | 10 | -970,609 | 4 buyers but net seller |
| PLAY | 3 | 2 | 188,600 | 0 | +188,600 | clean but tiny |
Heavy net sellers (avoided): MRCY -$43.7M/36 sells, OSCR -$101.2M/41 sells,
THC -$51.5M, MLI -$29.9M, CAKE -$25.5M, KBH -$17.9M, PTEN -$16.9M, TOL -$13.4M,
ZION -$6.5M, HIMS -$7.0M. Also checked, nothing: CTVA, BZH, EPC, SNV, STRL,
ATRO, SBH, WAL, CFR, SLG, BLDR, ROAD, FLO, TTEK, ENS, CSIQ.

**REZI and GO are the two cleanest clusters in the whole scan and both report
after the close TODAY.** Same bar as CRWV and ONON: no entry can be set on a
real level that survives tonight's gap, so neither is captured. Flagged for
tomorrow's run — if REZI holds up on the print, 3 distinct buyers and zero sells
is worth revisiting with a post-print level.

## [06:35 ET] REJECTED — IBP — the insider headline does not survive being read
This was the best-looking signal in the scan and it is mostly an artifact.
- `open_market_buys: 27` across 4 distinct buyers sounds like 27 confirmations.
  The detail says otherwise: every one of the 8 shown is **Miller Michael
  Thomas on the single date 2026-06-11**, in lots of 20-155 shares at 201.91-206.74.
  That is one person's one decision filled 8+ times, not a cluster — the same
  "three articles about one press release" error CLAUDE.md warns about. Real
  weight: one positioning confirmation, not a wall of them.
- The stock has left them behind: 223.45 now vs a ~202-207 cost basis, and
  **9.9% above both the SMA20 (203.33) and SMA50 (204.09)**. ATR 10.87 (4.87%).
- And it is not cheap. TTM EPS from the fetched surprise record =
  2.76 + 2.91 + 1.79 + 3.24 = **$10.70**, so 223.45 is **20.9x trailing** for a
  cyclical insulation installer. The 202-207 accumulation zone is still ~19x.
  There is no valuation anchor here, so the long_term framing fails too.
- Earnings quality is mixed, not improving: `beats_last_4: 2` — -2.6%, +13.2%,
  -9.8%, +16.1%. Most recent quarter was a **miss**.
- The one genuinely good leg: analyst revision_direction **improving**, bullish
  share 33.3% (+9.8pts), strong_buy 1→1→2→3 since August, 12 holds = under-owned.
Not enough. No dated catalyst (Q3 already reported), entry 8% below market, no
valuation edge, one real insider decision. Watchlist at best, not a captured idea.

## [06:40 ET] POSITION UPDATE — /MBTZ6 — pending short REAFFIRMED, level unchanged
Pending SHORT @ 74,075 from 2026-11-09. BTC spot now **74,305** (live, coingecko
2026-11-10T11:01Z) — the entry is at the market, not away from it.
What changed, and it confirms rather than contradicts:
- On 11-09 SPY +2.37%, QQQ +3.54%. **BTC +0.11%. ETH -0.36%. SOL -1.26%.**
  The whole complex declined into the best risk-on session of the quarter.
- IBIT proxy: 42.32 vs SMA20 45.30 / SMA50 45.78 (below both), -14.31% off high.
Levels: entry 74,075 / stop 79,800 (**2.51 ATR** ✓ crypto-futures floor 2.5) /
target 62,500. risk 5,725, reward 11,575, **R:R 2.02** ✓. baseline win prob
1/(1+2.02)=0.331, claimed 0.44 = 11 pts edge.
**Derivation disclosed:** could not quote /MBTZ6 or fetch BTC OHLC. BTC ATR
(~2,281) derived from IBIT's 3.07% ATR on spot; target from IBIT's 90d low
34.68 scaled by the IBIT/BTC ratio → ~60,890, so 62,500 sits just above it.
Derived from fetched data, **not** fabricated — and flagged in key_risk so the
reader checks the live contract. Dec contract ~6 weeks out, not final week.

## [06:41 ET] CORRELATION CHECK — before capturing anything else
Driver map of what is captured so far:
- **Rotation out of speculative duration into cheap domestic cash flow:**
  IWM long, /MBTZ6 short. = **2 ideas.** One more allowed on this driver.
  (These look opposed — long equity, short crypto — but they are the same bet:
  money leaving long-duration speculation. Counting them as one driver, not two.)
- **Position exits on a changed driver (crude):** AAL close, XLE close. Both are
  *reducing* exposure, not adding, so they do not consume correlation budget.
- **Defense/industrial longs already in the book:** HII, RTX, ACM = **3 ideas.**
  **This driver is FULL.** No new defense or government-services idea may be
  captured today, however good it looks. Recording this explicitly so synthesis
  does not add one.
- Risk-control-only updates: PYPL, ONON (a cancel). No driver exposure added.

## [06:46 ET] PENDING ORDER AUDIT — all 10 awaiting-entry items, gap to market
Quotes = 2026-11-09 close (GLD/TLT/XLV/CVS/OXY/SMMT/NVDA), BTC live.

| Item | Pending | Last | Gap | Verdict |
| --- | --- | --- | --- | --- |
| `NVDA` BUY | 184.00 | 178.67 | **-2.90%** | **CANCEL** — captured, see below |
| `ONON` BUY | 34.20 | 37.53 | +9.74% | **CANCEL** — reports bmo today, captured |
| `/MBTZ6` SHORT | 74,075 | 74,305 | +0.31% | **REAFFIRM** — captured, at the market |
| `CVS` BUY | 79.00 | 85.25 | **+7.91%** | retire — see below |
| `SMMT` BUY | 17.10 | 17.84 | +4.33% | stale, +9.25% on 11-09 — see below |
| `OXY` BUY | 54.00 | 55.76 | +3.26% | retire — crude thesis is the one I just closed XLE on |
| `XLV` BUY | 184.00 | 188.33 | +2.35% | leave standing — level still real |
| `TLT` BUY | 80.30 | 81.96 | +2.07% | leave standing |
| `GLD` SELL | 406.77 | 379.53 | **-6.70%** | dead level — GLD rising (+1.88%), needs a 6.7% rally to trigger |
| `KXCPIYOY-26SEP-T3.5` NO | 18 | n/a | — | **expired** — a September CPI contract. Retire. |

- **CVS: retire.** 3× in 10 days per prior_context, stopped out 2026-11-04, then
  re-published at 79.00 the next day, and it is now 85.25 — 7.9% above the entry.
  Re-pitching a stopped-out name and then watching it run away without you is the
  anchoring pattern the repetition guard exists for. The level is stale; a new
  CVS idea needs new work, which I have not done today.
- **SMMT: stale.** Stopped out 2026-10-26, re-published at 17.10, now 17.84 after
  a **+9.25%** session on 11-09. A 17.10 limit under a stock that just jumped 9%
  is the ONON defect again — it only fills on a reversal. No fresh research done
  on it today, so I am not re-levelling it; flagging for retirement, not capture.
- **OXY: retire for consistency.** I closed XLE today because the post-midterm
  removal of the Iran premium repriced crude lower. A standing crude-levered long
  contradicts that, and holding both would be incoherent.

## [06:48 ET] THE DAY'S REAL STORY — NVDA is not in the rally
This reframes the whole tape and it is the most important thing found today.
On 2026-11-09 QQQ rose **+3.54%** and NVDA fell **-4.27%**.
- NVDA 178.67: **-26.59% off the 90d high 243.37**, only **+4.95% off the 90d low
  170.24**; **14.6% below SMA20 (209.16)**, **18.4% below SMA50 (219.04)**. ATR 4.92%.
- `relstrength`: lagging SPY on **every** window — 1m -18.75%, 3m -15.53%,
  6m -20.39%; vs QQQ -12.5% / -12.41% / -13.82%.
- insiders: **0 open-market buys, 32 sells, $1,378,179,465** sold in 6 months.
- earnings **2026-11-17 amc**.
So the Nasdaq melted up 3.5% *without its largest component*, which is breadth
improving while the leader is distributed. That is the same fact the IWM
relative-strength number is measuring from the other side, and it is why the
rotation read is a rotation rather than a bounce.
**Pending NVDA BUY @ 184 cancelled** — captured. The deciding argument is
arithmetic, not sentiment: at 184 with an honest 2.0 ATR stop (166.40) and a
target back at the 50-day, R:R ≈ 2.0, whose **break-even hit rate is 33%**. A
stock lagging on all three windows into a binary print cannot be defended above
33%, so expectancy is negative and it fails on its own numbers.
**Deliberately NOT shorting it:** 5% off a 90d low into its own earnings, with
Wilson publicly calling a final-phase retest, is a squeeze risk I cannot size.

## [06:52 ET] LONG_TERM — the lane got deliberate time, and produced one idea: CAG
Screened 8 de-rated defensive names on insiders + structure + TTM EPS built from
fetched quarterly actuals. Results:

| Sym | Close | TTM EPS | P/E | bullish% | insiders (6m) | % off 90d high |
| --- | --- | --- | --- | --- | --- | --- |
| **CAG** | 15.29 | **1.72** | **8.9x** | **4.0%** | **+$510,632, 0 sells** | -8.63% |
| GIS | 34.88 | 3.44 | 10.1x | 10.7% | -$1.16M, 0 buys | -17.35% |
| DLTR | 137.23 | — | — | — | **-$248.7M**, 14 sells | -7.61% |
| MRK | 148.76 | — | — | — | -$30.0M, 17 sells | -5.20% |
| VZ | 46.06 | — | — | — | -$4.07M, 12 sells | -10.85% |
| DG | 136.68 | — | — | — | -$732K, 0 buys | -5.48% |
| BMY | 62.14 | — | — | — | -$678K, 0 buys | -9.47% |
| CPB | 22.86 | — | — | — | +$6,435 (trivial) | -5.77% |

**CAG captured.** entry 14.40-15.30 (ideal 14.80) / target 20.50 /
bear case **12.90** (no stop — long_term).
- reward 5.70, risk to bear case 1.90 → **R:R 3.00** ✓ (long_term floor 2.5)
- valuation method shown: TTM EPS 1.72 = 0.41+0.47+0.39+0.45 → 8.9x at 15.29;
  target = **12x the same 1.72**, requiring zero earnings growth
- bear case built two independent ways that agree: 8.9x on EPS -15% ($1.46) =
  ~13.00, and the 90d low is **12.88**. Not reverse-engineered to clear the floor.
- the standout fact: **4.0% bullish share — 0 strong buy, 1 buy, 14 hold, 8 sell,
  2 strong sell.** 10 of 25 analysts negative, against one insider buying 35,000
  shares at 14.5895 with zero sales.
- invalidation (mandatory, and it is not a price): **a dividend cut, or TTM EPS
  below $1.45 for two consecutive quarters.**
- **Conviction scored 4, not the 5 the mechanical count supports.** Four distinct
  evidence kinds hold, which the table maps to 5. I am publishing 4 because the
  positioning leg is a *single* buyer — the same thinness I rejected IBP over —
  and because this report's long_term lane is 0/4 with avg -15.2%. Understating
  is the safe direction; the red team can only lower.

**REJECTED — GIS:** cheap too (10.1x) and more de-rated (-17.4% off high), but
4 insider sells and zero buys. The whole CAG case rests on someone with the
volume data buying; GIS has the same narrative and nobody buying it.
**REJECTED — DLTR, MRK, VZ, DG, BMY:** all net insider sellers, DLTR heroically
so at **-$248.7M across 14 sells**. CPB's "3 buys" total $6,435 — noise, not a
signal, and exactly the headline-vs-detail trap IBP failed on.

## [06:56 ET] MACRO CALENDAR — **October CPI lands at 08:30 ET TODAY**
Nearly missed this and it is the most important dated event of the day.
- **Tue 2026-11-10, 08:30 ET — October CPI.** Consensus headline **+0.2% MoM**,
  **core +0.3% MoM**. Real earnings released alongside.
- Fri 2026-11-13, 08:30 ET — October PPI.
- Tue 2026-11-17, 08:30 ET — October advance retail sales (**same day as NVDA
  amc** — that is a loaded session).
- Already out: Fri 2026-11-06 08:30 ET October payrolls **+165K**, unemployment
  **4.1%** from 4.2% — which matches the FRED UNRATE 4.1% pulled earlier, so the
  two sources agree.
- Mon 2026-11-09: wholesale inventories, NY Fed consumer expectations.
sources: https://theinvestinggroup.substack.com/p/weekly-economic-brief-week-of-november-ccb
 | https://fedratecalc.com/us-economic-calendar/november-2026/
 | https://babypips.com/analysis/fundies-cheat-sheet-2026-11-09-cpi-ai-earnings-iran-oil
 | https://xoomar.com/markets/calendar
(Retail sales 11-17 appears on two independent calendars but I did not reach an
official Census page to confirm it — treat that one date as unverified.)

**Why this changes a captured idea.** CPI at 08:30 with the 10-year already at
4.86% is the single biggest input to the small-cap trade: IWM is the most
rate-sensitive of the three index ETFs because small caps carry more
floating-rate debt. Entering IWM at 09:00 would be front-running the print.
Re-capturing IWM with the CPI as its dated catalyst and an explicit
do-not-front-run instruction — `candidates.jsonl` is a log and synthesis takes
the last entry per symbol, so the amended version supersedes.

## [07:00 ET] REJECTED — PLAY — zero beats in four quarters, negative TTM EPS
Dave & Buster's 8.19, -31.46% off the 90d high 11.95, avg$vol $15.9M (clears the
$500K floor). Insiders: 2 distinct buyers, $188,600, zero sells — Lipman 24,000
sh @ 6.775 (2026-09-17), Hatton 4,000 sh @ 6.4999 (2026-09-28). Analysts 52.9%
bullish and improving.
Killed by the earnings record: **`beats_last_4: 0`** — missed all four quarters
by -245.3%, -74.1%, -384.2% and -18.3%, and **TTM EPS is -$2.57** on an $8.19
stock. There is no valuation anchor to build and no dated catalyst I verified.
The insiders are also 21% underwater-in-reverse — they bought at 6.50-6.78 and
the stock is 8.19, so the entry they liked is long gone. This could be dressed
up as a conviction-2 lottery ticket, and I am declining: conviction 2 is 0/6
with avg -8.4% in this report's own record, so the lane needs a *higher* bar,
not a turnaround with four consecutive large misses.

## [07:02 ET] REJECTED — EYE — the best-looking small cap, and it fails my own ONON test
National Vision 18.97, reports **11-12 bmo** (2 sessions out). The bull case was
the strongest in the small-cap scan: `beats_last_4: 3` (+33.2%, +4.1%, +146.3%,
-1.5%) and insider Nicholson bought **50,000 shares at 15.52** on 2026-06-05
($776,000) with zero sells.
Why it still fails:
- **Extended into the print.** 18.97 is 8.7% above SMA20 (17.46) and 11.6% above
  SMA50 (17.00), and 22% above the insider's own cost. ATR 5.75%.
- **Not cheap.** TTM EPS 0.98 (0.25+0.45+0.15+0.13) → **19.4x**, so there is no
  valuation cushion under a small cap with a 20.6% drawdown from its high.
- Analyst revision_direction **deteriorating**, bullish share -1.7pts.
- And the decisive point: every available entry is one I have already refused
  today. Buying 18.97 is front-running a print on an extended name; a limit at
  the 17.46 SMA20 is 8% below market and fills only on a miss — the exact ONON
  defect I cancelled an order over this morning. Rejecting ONON and capturing
  EYE would be incoherent.
Flagged for a post-print look on 11-12, which is the honest way to take it.

## [07:08 ET] INSIDER SWEEP 2 — 16 names, sectors absent from the book
Autos, chemicals, media, transport, apparel, specialty finance — chosen because
the book has no exposure to any of them. Three clusters with zero sells:

| Sym | buys | buyers | buy $ | sells | TTM EPS | P/E | %off high | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VFC | 3 | 2 | 1,302,362 | 0 | 0.97 | 21.5x | **-1.69%** | REJECT, too late |
| **HUN** | 1 | 1 | **981,000** | 0 | **-0.53** | n/a | -28.75% | **CAPTURED** |
| CE | 5 | 3 | 230,062 | 0 | **5.62** | **8.7x** | -5.50% | near miss, below |
| F | 1 | 1 | 148,880 | 0 | — | — | — | small, not pursued |
Net sellers: GM **-$111.4M**/29 sells, WBD **-$141.3M**/19 sells, FDX -$11.0M,
KSS -$1.8M, NWL -$1.4M, LYB -$742K, UPS -$877K, M -$667K. Nothing: DOW, PARA,
WU, SLM.

**HUN captured.** entry 8.90-9.15 (ideal 9.00) / target 10.82 / stop 8.09
- risk 0.91 = **2.00 ATR** ✓ | reward 1.82 | **R:R 2.00** ✓ (swing floor 2.0)
- baseline win prob 1/(1+2.0) = 0.333; claimed **0.40** = 7 pts of edge, modest
- entry = SMA20 9.00 / SMA50 9.01 convergence; stop just above the 90d low 7.995
- mkt cap ~$1.65B, avg$vol $29.6M — stated in thesis per the sub-$2B rule
- **conviction published 3, not the 4 the count supports.** Three distinct kinds
  hold, but TTM EPS is **-$0.53** and `beats_last_4: 1`, so there is no
  valuation anchor under it at all. Sized 1.5% speculative, dilution named.
- **Why this is not the ONON/EYE defect:** the 9.00 entry is 5.7% below market,
  but Q3 is already reported and there is no pending print, so the fill is
  conditioned on a drift into a real MA shelf rather than on a news event going
  against me. That is the distinction that makes a pullback entry legitimate.

## [07:10 ET] REJECTED — VFC — the insider signal already paid out
VF Corp 20.88. Three buys, 2 buyers, $1.30M, zero sells — the biggest clean
cluster in the sweep, and it is **stale**: Carucci bought 30,000 @ 17.167
(06-09) and 20,000 @ 14.73 (08-13), Darrell Bracken 32,894 @ 14.98 (07-31). The
stock is now 24-42% above those prices, **1.69% off its 90-day high**, 35% above
its SMA50 (15.46) and 15% above its SMA20 (18.13), at 21.5x TTM EPS of 0.97.
The market has already acted on exactly the information I would be acting on.
Buying the 90-day high because an insider bought 40% lower is not the signal, it
is the absence of one.

## [07:12 ET] NEAR MISS — CE — cheapest name found today, and the floor says no
Celanese 48.75 on **TTM EPS 5.62 (1.65+2.45+0.85+0.67) = 8.7x**, the lowest
multiple in either sweep. 3 distinct insider buyers, zero sells, revisions
improving, bullish 66.7%. Genuinely attractive and I could not make it clear the
long_term bar honestly:
- target at 11x the trailing 5.62 = **61.82**; entry ~47.00
- the bear case is where it fails. 8.7x on EPS 25% lower (4.22) = **36.6**.
  Using that: reward 14.82, risk 10.40 → **R:R 1.43**, against a 2.5 floor.
  I could instead call the bear case the 90d low of 41.11, which gives R:R 2.51
  and clears — and that is precisely the reverse-engineering `config/strategy.md`
  forbids. Choosing the bear case that makes the ratio work is not analysis.
So: no candidate. CE belongs on the watchlist at 8.7x pending either a lower
price or real work on normalised cyclical earnings, which I do not have fetched
data to do. Recorded so synthesis does not re-litigate it.

## [07:18 ET] SELF-CHECK — recomputed every ratio from the captured JSON
Ran my own arithmetic back over `candidates.jsonl` rather than trusting what I
wrote. Results, and they split into three groups:

**Clean passes (new/continuing entries):**
| Sym | reward | risk | R:R | stop ATR | floor | win prob | baseline | edge |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IWM | 20.50 | 9.20 | **2.23** | 1.82 | 1.8 | 0.42 | 0.310 | +11.0 |
| /MBTZ6 | 11,575 | 5,725 | **2.02** | 2.51 | 2.5 | 0.44 | 0.331 | +10.9 |
| HUN | 1.82 | 0.91 | **2.00** | 2.00 | 2.0 | 0.40 | 0.333 | +6.7 |
| ACM | 10.48 | 5.24 | **2.00** | 2.52 | 2.0 | 0.45 | 0.333 | +11.7 |
| CAG | 5.70 | 1.90 | **3.00** (vs bear 12.90) | n/a | 2.5 | n/a | n/a | n/a |
All five clear both floors and all four with a stop assert a *positive but
modest* edge — 6.7 to 11.7 points over baseline, none near the 20-point line
that would make the thesis carry a large claim. That is deliberate.

**Deliberate failures (exit and cancel recommendations).** These are *supposed*
to fail an entry test, because they are not entries:
- `AAL` R:R **-0.77** — covering at a loss. The negative ratio is the point.
- `NVDA` R:R 1.99 but win prob 0.25 vs baseline 0.335 = **negative expectancy**.
- `ONON` R:R **1.61** (under floor) and expectancy -3.4 pts.
- `HII`/`PYPL` show negative "risk" because the stop is now **above** the entry —
  protective stops on winners. Measured from the *last price* instead they are
  2.03 ATR (HII, 304.36→278.00) and 2.00 ATR (PYPL, 60.05→56.73), both correct.

**One subtlety worth stating, because it is this repo's signature failure mode.**
`XLE` as captured shows R:R **2.13**, which looks like a pass. It is not: that
ratio is only achieved by a stop at 60.80 that is **1.70 ATR**, below the 1.80
ETF floor — a ratio bought with a too-tight stop, exactly the KRE pattern. Widen
the stop to the floor (58.66) and the ratio collapses to **1.26**. It fails both
ways, which is the whole argument for closing it, and its expectancy is negative
too (0.25 vs a 0.320 baseline). Recording this so nobody reads the 2.13 and
concludes the position is fine.

## [07:22 ET] HANDOFF WARNING FOR SYNTHESIS AND ENFORCE — please read
`validate_report.py --enforce` demotes ideas that fail their floors to the
watchlist. **Five of today's twelve captures are exits or cancels and will fail
by design**: AAL (close), XLE (close), ONON (cancel), NVDA (cancel), and the two
protective-stop updates HII and PYPL whose stops sit above their entries.
Demoting those to a watchlist would bury the most time-critical items in the
report — *cancel the ONON order before 09:30 today* and *cancel the NVDA order
before 11-17* are the two highest-value sentences here, and they are worthless
as watchlist entries. They are instructions about positions that already exist,
not candidate entries competing for capital.
Recommend synthesis present them as a **position-management block ahead of the
new ideas**, and that the red team read `catalyst.action` (which says CLOSE or
CANCEL on each) before treating a failed ratio as a reason to drop the row.

## [07:24 ET] HORIZON SKEW — stated rather than papered over
Captured: **10 swing, 1 long_term, 0 intraday**, and 5 of the 10 swings are
position management rather than new risk. Net new exposure today is **three
ideas**: IWM, HUN, CAG.
**No intraday idea, deliberately.** It is 06:30 ET, the equity market is closed,
and every price I hold is the 2026-11-09 close. October CPI prints at 08:30 and
will reprice the open. strategy.md requires intraday levels to be *precise*, and
precise levels cannot be set from an 841-minute-old close across an unresolved
macro print — I would be inventing them. The CPI reaction is a real intraday
catalyst and the honest expression of it would have been an event contract,
which is the one lane `market_data.py events` could not price today (count 0 on
every macro query). So: no intraday row, and the reason is a data gap plus the
clock, not a quiet tape.
**Only one long_term** despite giving the lane deliberate time across two
screens of 24 names. CAG cleared; GIS, CE, DLTR, MRK, VZ, DG, BMY, CPB, IBP did
not. That lane is 0/4 with avg -15.2% in this report's record, so I raised the
bar rather than filling it.

## [07:30 ET] PENDING ORDERS — XLV and TLT reviewed, both LEFT STANDING
**XLV** (pending BUY @ 184.00, published 2026-11-09; last 188.33):
- `relstrength XLV --peer SPY`: **outperforming on 1m +13.58%, 3m +14.41%,
  6m +29.85% — leadership on every window measured.** This is the exact inverse
  of the NVDA and TJX readings that got those two refused today, and it is the
  strongest sector leadership I found anywhere on the tape.
- structure: 188.33 vs SMA20 180.80, SMA50 173.72 (8.4% above), -2.07% off the
  90d high 192.32, ATR 3.77 (2.0%).
- The 184.00 level sits *between* the market and the SMA20 — a shallow pullback
  into a rising trend, not a reflex discount, and not the ONON defect because no
  print is pending. Published yesterday, so re-pitching it today with the same
  level would be the repetition the prior-context guard is for. **Left standing,
  unchanged.** Noting only that the relative strength confirms it.

**TLT** (pending BUY @ 80.30; last 81.96): above both SMA20 (80.91) and SMA50
(80.36); the 80.30 entry is essentially *on* the 50-day. ATR 0.7379 — a 0.9%
ATR, the quietest instrument in the book. **Left standing.**
- Worth one distinction, since I cancelled ONON and NVDA this morning for having
  limits that only fill on bad news. TLT at 80.30 also fills only if CPI runs
  hot — but that is **not** the same defect. A hot CPI pushes yields up, and a
  buyer of duration whose thesis is "long rates are too high" gets a *better*
  entry on the same thesis; the thesis is not falsified by the fill. An earnings
  miss falsifies an equity thesis outright. Adverse selection is about whether
  the fill condition contradicts the thesis, not about whether the fill happens
  on a down move — collapsing those two would wrongly condemn every value entry.

## [07:33 ET] CORRELATION CAP — UPDATED, and the rotation driver is now FULL
Revising my earlier count. With XLV left standing, the "rotation out of
speculative long-duration into cheap/defensive cash flow" driver holds:
1. `IWM` long (captured today)
2. `/MBTZ6` short (reaffirmed today)
3. `XLV` long (standing from 11-09)
**That is 3 of a maximum 3.** No further idea on this driver may be added today,
which is the reason CE was left on the watchlist rather than argued harder and
the reason I did not pursue a QQQ or /MNQ short despite QQQ being 11% off its
high and below both MAs — that would have been a fourth expression of one bet.
Also still full: **defense/industrial longs at 3** (HII, RTX, ACM).
CAG (staples value) and HUN (chemicals cycle) are each the only idea on their
driver, which is why they were the two worth capturing from the screens.

## [06:31 ET] RESEARCH COMPLETE
Started 06:01 ET, finished 06:31 ET — 30 minutes of a ~60 minute budget, stopped
because the work was done rather than because the clock ran out. **Not
truncated.** First candidate captured at ~minute 6, well inside the minute-20
deadline; all 12 captures were written to `candidates.jsonl` as they were
finalised, never buffered.

- **candidates: 12 written, 11 distinct (symbol, direction)** — IWM appears
  twice and the later entry (with October CPI as its dated catalyst and a
  do-not-front-run instruction) supersedes the earlier one.

**Net new risk — 3 ideas:**
| Sym | Dir | Horizon | Conv | Entry | Target | Stop/Bear | R:R | Size |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IWM | buy | swing | 4 | 277.00-279.50 | 298.50 / 305 | 268.80 | 2.23 | 3% |
| CAG | buy | long_term | 4 | 14.40-15.30 | 20.50 | bear 12.90 | 3.00 | 3% |
| HUN | buy | swing | 3 | 8.90-9.15 | 10.82 | 8.09 | 2.00 | 1.5% |

**Position management — 9 actions, and today this is the more valuable half:**
- **CLOSE** `AAL` short (thesis broken by crude; stop was 0.36 ATR away)
- **CLOSE** `XLE` long (driver changed; fails the floor at an honest stop)
- **CANCEL** `NVDA` pending buy @184 (negative expectancy; -26.6% off high)
- **CANCEL** `ONON` pending buy @34.20 **before 09:30 — it reports bmo today**
- **ADD STOP** `HII` @278.00 (was running unstopped while +16.2%)
- **RAISE STOP** `PYPL` @56.73 (above entry; target is the 90d range high)
- **HOLD + TRIM HALF** `ACM` into its 2026-11-16 amc print
- **REAFFIRM** `/MBTZ6` short, level unchanged at 74,075 (now at the market)
- **RETIRE** (flagged, not captured): `CVS` @79 stale and 7.9% away after 3
  publications in 10 days; `SMMT` @17.10 after a +9.25% session; `OXY` @54 for
  contradicting the XLE close; `KXCPIYOY-26SEP-T3.5` long expired.
  `XLV` @184 and `TLT` @80.30 reviewed and **left standing**.

**Coverage gaps — what I could not check:**
- **Event contracts: no usable data.** `events` returned count 0 for CPI,
  inflation, recession, interest rate, fed funds, Bitcoin, S&P 500, GDP,
  unemployment; "Fed" returned 2 sports parlays with null prices. **Zero event
  contract candidates, and that is a data gap and not a judgement** — the lane
  requires a real implied probability to disagree with.
- **Options-implied move: none.** `implied` → yahoo-options HTTP 401. No
  candidate got the "is the target inside what options price" check.
- **Short interest: none.** `short` → api.nasdaq.com read timeouts on every
  name tried (IBP, HUN, CAG, IWM). So no crowding read in either direction,
  which matters most for HUN as a sub-$2B cap.
- **Index levels: none.** spx/ndx/dow/russell2000/vix/es/nq/dxy/us10y/gold/wti
  all ok:false from `macro` (finnhub CFD subscription, yahoo 429, stooq 404, no
  AV key). Regime was proxied via ETFs; **this is why the small-cap view is IWM
  and not /M2K** — `RTY` and `^RUT` both failed, so futures levels would have
  been fabricated.
- **No OHLC bars.** `history` returned null open/high/low/close in `recent` for
  every symbol; only the derived aggregates (ATR14, SMA20/50/200, 90d range,
  avg dollar volume) were usable. All levels are set from those, which is why
  entries sit on moving-average convergences and stops on range extremes.
- No intraday ideas (see the horizon-skew note at 07:24 — closed market, prices
  841 minutes old, CPI unresolved at 08:30).

**Sources that failed:** finnhub index quotes (CFD subscription required),
yahoo chart API (429 on query1 and query2), yahoo options API (401), stooq
(404 on ^-prefixed symbols), api.nasdaq.com short interest (timeout),
alphavantage (no API key), Kalshi macro event search (empty),
robinhood.com futures support article (404 — found the product list on
invest.robinhood.com instead).

**The one thing to carry forward:** on 2026-11-09 the Nasdaq rose 3.54% and
**NVDA fell 4.27%**, with NVDA now 26.6% off its high, 18.4% below its 50-day,
lagging SPY on every window, and carrying $1.378B of insider sales and zero
buys into a 2026-11-17 print. The index melted up without its largest component.
Everything captured today is downstream of that single fact.
