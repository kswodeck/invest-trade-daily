# Research log — 2026-09-18

## [06:03 ET] MACRO — regime as of the 2026-09-17 close
All equity prices below are the **previous close (2026-09-17 20:00 UTC)**, taken
in a closed market during the 06:00 ET pre-session. Not stale — the freshest
honest equity print at this hour.

- Yesterday was a broad risk-on session, and bonds rallied with stocks — the
  signature of a dovish FOMC (Sep 16-17 meeting, decision 2026-09-17 14:00 ET):
  SPY 762.60 +1.13%, QQQ 716.92 +1.73%, IWM 285.43 +0.53%, SMH 560.61 +2.76%,
  XBI 158.25 +2.64%, EEM 66.91 +1.81%, GLD 398.36 +1.69%, TLT 81.78 +1.11%.
  VIXY 16.98 -3.90%. — source: scripts/market_data.py quote (finnhub)
- Rates (FRED): US10Y **5.01%** (2026-09-16), US2Y 4.74%, effective fed funds
  3.63%, 10y-2y curve **+0.27** (2026-09-17). — source: scripts/market_data.py macro (FRED)
- The shape matters more than the level: policy near 3.6% with a 5.01% 10y is a
  steep curve driven by the long end, i.e. term/fiscal premium, not growth
  optimism. A Fed cutting into a 5% long bond is the central tension today.
- Unemployment 4.1% (Aug), CPI index 334.131 (Aug). — source: FRED

## [06:03 ET] DATA GAPS
- Yahoo Finance returning HTTP 429 (rate limited) across the board; ^GSPC, ^NDX,
  ^DJI, ^RUT, ^VIX, ES/NQ futures, DXY, ^TNX, gold and WTI all FAILED in `macro`.
  Finnhub covers individual equities/ETFs fine, so ETF proxies are used instead
  of index quotes throughout (SPY/QQQ/IWM for indices, GLD for gold, USO for WTI).
- CoinGecko `crypto.prices` FAILED in the macro call — retrying separately.

## [06:05 ET] CRYPTO — 24/7 tape
- BTC $78,143 (+2.34% 24h), ETH $2,507.18 (+2.96%), SOL $106.37 (+6.31%).
  — source: scripts/market_data.py crypto (CoinGecko)
- Note vs prior context: the open `BTC` SELL @ 63,400 and `/MBTU6` SHORT @ 64,340
  are ~18% below spot and were never filled. They are stale shorts against a
  market that has gone the other way.

## [06:05 ET] CATALYST CALENDAR — dated earnings inside 10 sessions
From `scripts/market_data.py earnings --days 14` (finnhub), 51 names with
estimates. The ones that matter here, and *why* they matter:

- **2026-09-22 bmo THO** (Thor Industries, rev est $2.20B, eps 0.9159) — Thor is
  the largest RV OEM and **LCII's single biggest customer**. We are long LCII at
  -7.3%. This is a dated read-through catalyst for an open position, not a new idea.
- **2026-09-22 amc KBH** (KB Home, rev est $1.31B) and **2026-09-22 FERG**
  (Ferguson, rev est $8.17B) — homebuilder + building-products distributor, both
  direct demand read-throughs for **BCC** (Boise Cascade), open at -7.0%.
- **2026-09-28 NKE** (rev est $11.47B, eps est 0.4495) — we hold NKE BUY at
  -10.6% *and* an NKE SELL. A dated print inside the horizon of an open position.
- **2026-09-30 amc MU** (Micron, rev est $52.10B, eps est 32.22) — the largest
  dated tech catalyst in the window, into SMH +2.76% yesterday.
- Others logged for completeness: AZO, MLKN, WOR (9/22); CTAS, PAYX, FUL, SFIX
  (9/23); COST, SNX, DRI (9/24); CCL (9/28); KMX, CAG, CNXC (9/29); JBL, JEF,
  FDS, CALM (9/30); ACN, AYI (10/1).
- source: https://finnhub.io/api/v1/calendar/earnings

## [06:09 ET] LEVELS — fetched 120-day history (nasdaq), all as of the 2026-09-17 close
Note: this source returns computed aggregates (ATR14, SMAs, range) but the
per-bar OHLC in `recent` comes back null, so intraday swing levels are not
available today — levels below are set off SMAs, the 120-day range and ATR.
SMA200 is null for every name (only 120 bars fetched).

| Sym | Close | ATR14 | ATR% | SMA20 | SMA50 | 120d high | 120d low | off high | $vol/day |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MU | 977.50 | 42.89 | 4.39 | 957.53 | 926.77 | 1255.00 | 311.49 | -22.1% | 26.5B |
| DINO | 116.62 | 4.36 | 3.74 | 103.83 | 94.29 | 116.69 | 55.43 | -0.1% | 284M |
| LCII | 86.49 | 3.34 | 3.86 | 98.18 | 102.43 | 138.15 | 86.26 | -37.4% | 22.3M |
| BCC | 75.53 | 2.25 | 2.98 | 77.84 | 79.00 | 88.43 | 65.00 | -14.6% | 21.4M |
| NKE | 36.36 | 0.90 | 2.48 | 38.24 | 40.59 | 53.11 | 35.72 | -31.5% | 1.04B |
| CCJ | 92.80 | 3.48 | 3.75 | 98.92 | 94.87 | 131.21 | 83.15 | -29.3% | 238M |
| CEG | 262.80 | 10.78 | 4.10 | 278.80 | 271.08 | 328.80 | 228.63 | -20.1% | 696M |
| GLD | 398.36 | 8.52 | 2.14 | 407.32 | 392.51 | 448.70 | 363.32 | -11.2% | 4.55B |
| XLE | 64.48 | 1.33 | 2.06 | 64.08 | 60.99 | 66.17 | 52.62 | -2.6% | 1.82B |
| DVN | 48.72 | 1.38 | 2.82 | 48.71 | 46.08 | 52.71 | 40.00 | -7.6% | 528M |

## [06:09 ET] CAPTURED — DINO (position update, conviction 3)
- decision: **hold, levels unchanged** (entry 107.50, target 128, stop 97.75)
- +8.5% from entry; closed 116.62 against a 120-day high of 116.69
- R:R from the filled entry = 20.5/9.75 = 2.10, stop 2.24 ATR — both clear
- deliberately did NOT walk the stop up to lock in gain: at 116.62 a "raised"
  stop near 105 would sit 0.57 ATR from the entry and fail the stop floor. That
  is the exact free-ratio move `check_stop_distance` exists to refuse.
- relative strength is the confirming evidence: +20.6pp vs XLE over 1m, +59.0pp over 3m

## [06:10 ET] CAPTURED — MU (new, conviction 4)
- entry 950-975 (on the SMA20 at 957.53), target 1255 (the 120-day high), stop 872 (below the SMA50)
- R:R = 295/88 = 3.35; stop = 2.05 ATR (floor for a stock swing is 2.0) — clears without nudging
- win_probability 0.32 vs a 1/(1+3.35) = 23.0% baseline, so ~9pp of claimed edge
- **the bear case is real and is written into `counter_argument`**: finnhub's
  recommendation trend shows `revision_direction: deteriorating`, bullish share
  91.4% and falling 1.3pp. A 91% bullish book into a print has no marginal
  upgrade left. This did NOT count as a 4th evidence kind — it is unanswered.
- failed sources on MU: `implied` (yahoo-options HTTP 401 Unauthorized) and
  `short` (nasdaq ReadTimeout), so **the options-implied move is unknown today**
  and the 30.7% target could not be checked against what the straddle prices.

## [06:13 ET] EVENT CONTRACTS — could not reach the macro markets (coverage gap)
`market_data.py events` is searching Kalshi by substring and only returns
`KXMVECROSSCATEGORY` sports parlays. Queries run and their counts:
- "Fed" → 2 matches, both sports parlays (matched the letters "fed" inside a hash)
- "FEDDECISION" → 0, "CPI" → 0, "inflation" → 0, "recession" → 0,
  "Fed funds" → 0, "rate" → 0, "bitcoin" → 0, "gold" → 14, all sports parlays
**No event contract idea is captured today.** The three `KXFEDDECISION-*` rows in
prior context could not be re-priced, and the two 26SEP ones resolved at
yesterday's FOMC in any case. Fabricating an implied probability without the
market price is exactly the failure this report is built to avoid.

## [06:15 ET] POSITIONING — insider sweep across the de-rated complex
`market_data.py insiders`, 6-month window, Code P open-market purchases only:
- **NKE: 5 buys, 4 distinct buyers, $3.73M gross, net +$2.53M.** Buyers are
  Elliott Hill (CEO, 47,320 sh @ ~42.27 on 2026-04-13), Timothy D Cook
  (25,000 @ 42.43, 2026-04-10), John W Rogers Jr (4,000 @ 43.34, 2026-04-09),
  Robert H Swan (11,781 @ 42.44, 2026-04-07). **Every one of them is underwater:
  they paid ~$42.40 and the stock closed 36.36, -14%.** A real signal that has
  not worked yet — which is information, not a reason to discount it.
- LCII: zero buys, zero sells. THO: zero, zero. FERG: zero, zero.
- BCC: 0 buys, 3 sells ($666K). COST: 0 buys, 2 sells ($1.54M).
- **KBH: 0 buys, 8 sells, $16.58M net sold** — into a print on 2026-09-22.
- source: https://finnhub.io/api/v1/stock/insider-transactions

## [06:15 ET] THE DAY'S ACTUAL SIGNAL — dispersion, not direction
The single most striking thing in today's data is not a name, it is a split.
Fetched 120-day positions, all at the 2026-09-17 close:

*Pinned to their 120-day lows:* LCII -37.4% off high (0.27% off the low), THO
-19.0% (0.35% off low), FERG -20.3% (0.68% off low), COST -18.5% (0.66% off
low), NKE -31.5% (1.79% off low), KBH -23.7%, BCC -14.6%.

*Ripping:* SMH +2.76% yesterday, QQQ +1.73%, MU -22% off high but above its
SMA20 and SMA50, DINO and XLE at their 120-day highs.

The rate structure explains it: effective fed funds 3.63% against a **5.01% 10y**
is a long end pricing term premium, and a 5% 10-year is precisely what breaks
housing, RVs, building products and the financed consumer while doing nothing to
the AI capex cycle. Every de-rated name above is a rate-sensitive consumer
durable. That is one macro driver, so the **correlation cap binds hard here** —
LCII, BCC, THO, KBH, FERG and COST are six expressions of a single bet, and no
more than three may be published.

## [06:16 ET] TIMESTAMP CORRECTION
The three blocks above stamped 06:09-06:15 were written between 06:08 and 06:13
ET; I stamped them from estimate rather than from `date`. Corrected here rather
than by editing them, since notes are append-only. All *market* data timestamps
in this file are fetched values and are unaffected.

## [06:16 ET] POSITIONING — relative strength across the open book
`market_data.py relstrength`, percentage points vs the named peer:

| Sym | vs peer | 1m | 3m | 6m | read |
| --- | --- | --- | --- | --- | --- |
| DINO | XLE | +20.6 | +59.0 | — | leading hard |
| XLE | SPY | +1.9 | +15.0 | -5.0 | leading |
| CEG | XLU | +3.8 | +4.6 | -6.4 | leading its sector |
| EEM | SPY | +3.0 | -5.3 | +0.9 | turning up |
| MU | SMH | +5.5 | +3.9 | — | leading |
| GLD | SPY | +0.6 | -0.4 | -25.7 | neutral to lagging |
| CCJ | XLE | -4.6 | -30.1 | -25.5 | **lagging badly** |
| NKE | XLY | -5.0 | -14.2 | -32.7 | **lagging badly** |
| LCII | XLY | -12.0 | -0.1 | -29.5 | **collapsing** |

## [06:16 ET] CAPTURED — position updates, all holds at unchanged levels
- **EEM** conv 3 — hold. R:R 2.27, stop 2.59 ATR. Dovish-FOMC beneficiary, +3.0pp vs SPY 1m.
- **CEG** conv 3 — hold. R:R 2.18, stop 2.04 ATR. Beating XLU by 4.6pp over 3m.
- **XLE** conv 3 — hold. R:R 2.13, stop 2.34 ATR. +15.0pp vs SPY 3m.
- **GLD** conv 2 — hold, sized 1%. R:R 2.29, stop 2.00 ATR. Only one evidence
  kind, so a 2 and marked as such; four weeks held for zero.
In every case entry is unchanged because the position is filled and a filled
entry is not amendable. No stop was walked in on any of them.

## [06:19 ET] CAPTURED — the rest of the open book
- **NKE** conv 4, long_term — hold into the 2026-09-28 print, **target LOWERED
  62.00 -> 53.11**. The old target was above everything in the fetched 120-day
  history and could not be defended from any number gathered today; 53.11 is the
  120-day high, a level actually traded. This makes the ratio from the filled
  40.75 entry worse, not better, and that is the honest direction for it to move.
  Carried by the insider cluster (CEO + 3 directors, $2.53M net) against a
  -14.17pp 3m relative-strength read. Note the book also holds an NKE SELL @ 38.40.
- **CCJ** conv 2, 1% — hold, do not add, third appearance in ten days. Lagging
  XLE by 30.12pp over 3m; target 135 is above the 120-day high of 131.21.
- **LCII** conv 3, 1% — hold, **stop ADDED at 79.00 where there was none**. THO
  reports 2026-09-22 bmo and is LCII's largest customer.
- **PFE** conv 4, long_term — continuing accumulation 26.50-28.10. Valuation
  anchor computed from 3 fetched quarters (0.77+0.75+0.66 = 2.18, ann. ~2.90):
  9.5x now, 14.5x at the 42.00 target, 8.1x at the 23.50 downside case. R:R 3.51.
  38.9% bullish share and falling against 3 straight beats averaging +9.75%.
- **SVRA** conv 2, 1% — hold, no verified catalyst date found in the SEC index.
  S-8 (2026-08-11) and Form 144 (2026-06-22) noted as dilution/sale signals.

## [06:21 ET] REJECTED — open positions that no longer clear the bar
Each of these was worked through with fetched levels and fails on arithmetic, not
on taste. They are logged here so synthesis does not re-litigate them.

- **REJECTED — DVN — stop floor and R:R cannot both be met.** Entry 49.60, target
  55.50, stop 46.90, ATR14 1.3751. The stop is 2.70 from entry = **1.96 ATR,
  under the 2.0 stock swing floor**. Widening it to 46.60 (2.18 ATR) drops R:R to
  5.90/3.00 = **1.97, under the 2.0 floor**. The target cannot be raised to fix
  it: 55.50 is already above the 120-day high of 52.71. Published 4x in ten days.
  Energy is also already at the 3-idea correlation cap via DINO and XLE.
- **REJECTED — BCC — target is undefendable and the ratio fails without it.**
  Entry 76.50, no stop, close 75.53, ATR14 2.2499. Target 110.00 is +45.6% above
  the 120-day high of 88.43 and nothing fetched today supports it. Re-anchoring
  the target to that 88.43 high with a 70.00 stop gives 11.93/6.50 = **1.84**;
  widening the stop to 68.00 makes it **1.40**. Insiders sold $665,842 across 3
  transactions with zero open-market buys.
- **REJECTED — LULU — fails the long-term floor from its filled entry.** Entry
  115.00, no stop, close 99.39, ATR14 5.7616 (5.8%). Target 180.00 is above the
  120-day high of 170.20. Against an honest bear case of 85.00, R:R from the
  filled entry is 65.00/30.00 = **2.17, under the 2.5 long-term floor**. The book
  separately holds a LULU SELL at 100.61 that is +4.6%, so the exposure is
  already largely offset.
- **REJECTED — COST — not actually cheap, so the de-rating is not the idea.**
  Close 893.93, 0.66% off the 120-day low, -18.5% off the high, earnings
  2026-09-24 amc, ATR14 13.3356. On the fetched 6.6729 quarterly EPS estimate
  (~27/yr) it is ~33x. A 40x target is 1080 and a 28x bear case is 756, giving
  186.07/137.93 = **1.35 against the 2.5 long-term floor**. As a swing, the only
  real level above is the SMA50 at 936.89, which yields 1.69. Insiders sold
  $1.54M, zero buys. A de-rated compounder that is still on 33x is a narrative,
  not a mispricing.
- **REJECTED — THO — a duplicate of the LCII bet, not a second idea.** 68.84,
  0.35% off its 120-day low, ATR14 2.5291, reports 2026-09-22 bmo. Entry 68.50
  with a 63.30 stop (2.06 ATR) and the 85.00 120-day high as target gives 3.17,
  which clears. It is rejected on the **correlation cap**: THO and LCII are the
  same RV-cycle bet on the same print, and LCII is already captured.
- **REJECTED — KBH — reports 2026-09-22 into $16.58M of insider selling** across
  8 transactions with zero buys. Not a setup worth taking the other side of.

## [06:21 ET] STALE ORDERS — the two crypto shorts in prior context are dead
`BTC` SELL @ 63,400 (published 2026-08-16) and `/MBTU6` SHORT @ 64,340
(published 2026-08-18) sit **18-19% below spot** at BTC $78,143. They have not
filled and on any reasonable read will not. They are not positions and should not
be carried as live orders; flagging rather than re-pitching. `/MBTU6` is also a
September 2026 contract and would be at or past expiry in any case.

## [06:24 ET] NEWS/FILINGS — insider sweep #2, across the de-rated earnings names
Ran `insiders` over KMX, CAG, MLKN, WOR, CCL, JBL, DRI, AZO, SFIX, PAYX. Two
clean clusters — meaning multiple distinct buyers and **zero** offsetting sales:

- **KMX: 6 buys, 5 distinct buyers, $1,268,037, zero sells.** Chawla Sona 2,000
  @ 53.39, Shinder Marcella 574 @ 52.01 (both 2026-06-25), ONeil Mark F 4,800 @
  52.36 twice (2026-06-24). Reports 2026-09-29.
- **CAG: 3 buys, 3 distinct buyers, $1,119,535, zero sells.** Brase John P 35,000
  @ 14.5895 (2026-07-17), Mulligan John J 17,500 @ 14.3087 and LENNY RICHARD H
  25,000 @ 14.34 (both 2026-04-14). Reports 2026-09-29.
- Net sellers, i.e. nothing to see: MLKN 0/0; WOR 3 sells $3.26M; CCL 4 sells
  $1.52M; DRI **18 sells $18.29M**; SFIX **21 sells $3.51M**; PAYX 4 sells $3.39M.
  JBL and AZO each show a single token buy against $14.2M and $4.19M net selling
  respectively — those are not clusters and are not counted as signals.

## [06:24 ET] CAPTURED — KMX (new, conviction 4, **wait: true**)
- entry 55.00-56.50 (ideal 56.00), target 65.28 (the 120-day high), stop 52.00
- R:R = 9.28/4.00 = **2.32**; stop = 2.39 ATR. Both clear.
- **At the 58.38 last close the ratio is 1.78 and fails the 2.0 floor**, so the
  idea is published as a wait with a stated limit rather than nudged to fit. This
  is the one case today where the honest answer was "good setup, wrong price".
- The 52.00 stop is placed just under the 52.01-53.39 band where five insiders
  actually bought — a level with a reason behind it, not a round number.
- analyst revision swing +20.9pp is the largest in today's sweep; beats of
  +32.35%, +46.80%, +34.53% in the last three quarters, against a -40.06% miss
  one year ago which is named in the counter-argument.

## [06:24 ET] REJECTED — new ideas worked through that did not clear
- **REJECTED — CAG — real signal, geometry does not pay.** 15.18, ATR14 0.3911,
  SMA50 15.17 (price is sitting on it), range 12.53-16.735. Three insiders bought
  with zero sells and only **4.0% of analysts are bullish**, which is about as
  hated as a large cap gets. But with a 14.25 stop (2.38 ATR, below the insider
  band) and the 16.735 120-day high as target, R:R is 1.555/0.93 = **1.67**. As a
  long_term idea at ~13.3x the 0.285 quarterly estimate, a 16x target of 18.24
  against a 12.53 bear case gives **1.15 vs the 2.5 floor**. A low-volatility
  staple has a downside too near to clear these floors. Signal noted, not bought.
- **REJECTED — KRE — the CLAUDE.md trap, declined.** 72.74, ATR14 1.3046, below
  both SMA20 74.08 and SMA50 75.41, lagging XLF by 1.96pp over 1m and SPY by
  4.72pp. The curve-steepening story is good and the arithmetic is not: a 70.00
  stop (2.10 ATR) with the 78.35 120-day high as target gives **2.05**, which
  clears only barely and only because the stop is as tight as the floor permits.
  This is the exact name and the exact manoeuvre CLAUDE.md records as having been
  abused three times. No dated catalyst either. Declined.
- **REJECTED — SMH — passes the floors, fails the premise.** 560.61, ATR14
  14.4875, entry 557 with a 520 stop (2.55 ATR) and the 671.83 120-day high as
  target gives 3.10. But SMH is **lagging SPY by 13.07pp over 3m** and 0.98pp
  over 1m, so the positioning read is negative rather than absent — leaving one
  evidence kind and a conviction of 2 for a +20% target. MU already carries the
  semis exposure and is the name *leading* this basket by 5.52pp. Not doubled up.
- **REJECTED — XBI — no target that clears.** 158.25, ATR14 3.9914, above SMA50
  157.72. Entry 157.75 with a 150.00 stop (1.94 ATR, at the ETF floor) targeting
  the 169.89 120-day high gives 12.14/7.75 = **1.57**. Rate-cut-beneficiary logic
  is sound; the range offers nothing to aim at.

## [06:24 ET] REJECTED — the three unfilled orders in prior context, all three
Re-pitching an unfilled order amends rather than duplicates, so each was worked
through properly. None requalifies, and the honest conclusion is that all three
should be **cancelled rather than carried**:

- **REJECTED — VST — the order is 12% below a market that left without it.**
  Published BUY @ 128.00 on 2026-08-24; close is 143.56. Re-entering at the SMA20
  of 142.18 with a 131.50 stop (2.16 ATR, under the 132.66 120-day low) and the
  171.35 high as target gives 2.80, which passes. It is rejected on evidence and
  correlation instead: insiders are **7 sells against 1 buy, net -$4.98M**, so the
  positioning read is negative, leaving one evidence kind and conviction 2 — and
  CEG plus CCJ already put the datacenter-power theme at the 3-idea cap.
- **REJECTED — DG — no target that clears.** Published BUY @ 134.50; close
  124.95, coiled between SMA50 124.21 and SMA20 125.93, ATR14 4.1588. Entry 124.00
  with a 115.00 stop (2.16 ATR) targeting the 134.125 120-day high gives
  10.13/9.00 = **1.13**. Zero insider activity in either direction, no dated
  catalyst. Nothing here.
- **REJECTED — IYR — only clears with the stop inside a real level.** Published
  SELL_SHORT @ 103.60; close 98.94, and the relative-strength read genuinely
  confirms the short (-4.02pp vs SPY 1m, -4.59pp 3m, -13.13pp 6m, and a 5.01%
  10-year is a direct attack on REIT cap rates). Shorting at 98.94 with a 101.30
  stop and the 92.45 120-day low as target gives 2.75 — but 101.30 is *below* the
  SMA20 of 102.26, i.e. inside the first resistance a short should be stopped
  above. Placing the stop properly above the SMA20 at 102.40 (2.71 ATR) drops R:R
  to **1.88**. The idea only worked with the stop in the wrong place, so it fails.

## [06:24 ET] NEWS/FILINGS — second insider sweep, nothing further
ACN, SNX, JEF, FDS, AIR, FUL, CNXC, AYI, CALM, FERG. No qualifying cluster:
ACN 0 buys/9 sells; SNX 0 buys/**61 sells** -$14.4M; AIR 0/7 -$10.4M; FDS, CALM
and FERG show no transactions at all. CNXC (3 buys, 2 buyers, $118K) and AYI
(2 buys, 2 buyers, $341K) are token purchases against -$133M and -$727K of net
selling respectively — not clusters, not counted. JEF nets +$628M on 2 buys and
2 sells, which is too large to be open-market activity read at face value and is
discarded as unreliable rather than reported as a signal.
**KMX and CAG remain the only two clean clusters found today.**

## [06:26 ET] FALSIFICATION PASS — self-audit of the captured set
Recomputed every candidate from its own fetched numbers rather than trusting what
I wrote about it. Conviction equals distinct evidence kinds on all 13 (1 kind→2,
2→3, 3→4), no exceptions. Reward-to-risk against the correct floor, and
win_probability against its own 1/(1+R:R) baseline:

| Sym | Horizon | Conv | R:R | Floor | Baseline | wp | Edge |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MU | swing | 4 | 3.35 | 2.0 | 23.0% | 0.32 | +9.0pp |
| KMX | swing | 4 | 2.32 | 2.0 | 30.1% | 0.38 | +7.9pp |
| PFE | long_term | 4 | 3.51 | 2.5 | 22.2% | 0.40 | +17.8pp |
| **NKE** | long_term | 4 | **1.15** | **2.5** | 46.5% | 0.30 | **-16.5pp** |
| DINO | swing | 3 | 2.10 | 2.0 | 32.3% | 0.50 | +17.7pp |
| EEM | swing | 3 | 2.27 | 2.0 | 30.6% | 0.42 | +11.4pp |
| CEG | swing | 3 | 2.18 | 2.0 | 31.4% | 0.40 | +8.6pp |
| XLE | swing | 3 | 2.13 | 2.0 | 31.9% | 0.42 | +10.1pp |
| LCII | swing | 3 | 2.93 | 2.0 | 25.4% | 0.28 | +2.6pp |
| TLT | swing | 3 | 2.71 | 2.0 | 27.0% | 0.36 | +9.0pp |
| GLD | swing | 2 | 2.29 | 2.0 | 30.4% | 0.40 | +9.6pp |
| CCJ | swing | 2 | 3.57 | 2.0 | 21.9% | 0.27 | +5.1pp |
| SVRA | swing | 2 | 3.53 | 2.0 | 22.1% | 0.28 | +5.9pp |

Two things the audit changed rather than merely confirmed:
- **NKE is published knowing it fails**, at 1.15 against a 2.5 floor, because the
  reader holds it and needs the decision. Demotion to the watchlist is the
  correct destination for "hold, do not add" and is not an error to be fixed by
  moving the target back up. The target went *down* today; the ratio got worse as
  a direct result, and that is the honest direction.
- **PFE's win probability was cut from 0.45 to 0.40.** At 0.45 the claimed edge
  was 22.8pp, over the 20pp mark at which the thesis must carry the claim — while
  my own counter-argument concedes I could not verify whether the beats are
  earnings quality or cost cuts. A claim the thesis does not support had to move.

## [06:26 ET] CORRELATION CHECK — the cap binds, and one factor dominates
Grouped by what actually has to happen for each to pay:
- rate-sensitive consumer: **NKE, LCII, KMX — 3, at the cap.** THO, KBH, COST and
  CAG were all rejected partly to stay inside it.
- energy/refining margin: **DINO, XLE — 2.** DVN rejected, which also kept it at 2.
- datacenter power: **CEG, CCJ — 2.** VST rejected, which kept it there.
- pharma/biotech: PFE, SVRA — 2. Semis: MU — 1.
- rates/macro: TLT (short), EEM, GLD — 3, at the cap.

**The honest caveat for synthesis:** the rate path is not really three ideas, it
is the factor underneath most of the book. EEM, GLD and the TLT short key off it
directly, CEG is discounted by it, and all three consumer names are at 120-day
lows because of it. A single repricing of the long end moves ten of thirteen
lines together. That is a genuine concentration and it should be said in
`data_quality_notes` rather than hidden behind five tidy-looking buckets.

## [06:31 ET] **CORRECTION — THE FED HIKED. MY EARLIER MACRO READ WAS WRONG.**
This supersedes the 06:03 MACRO block and everything built on it. Verified
against primary sources, not inferred from price action:

- The FOMC **raised** the target range by 25bp to **3.75%-4.00%**, announced
  **2026-09-16** (meeting 15-16 Sep, not 16-17), effective 2026-09-17. IORB
  raised to 3.90%, primary credit to 4.00%, standing repo 4.00%, ON RRP 3.75%.
  — source: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a1.htm
- September SEP medians: **fed funds 4.1% end-2026** (another hike implied from
  the 3.875% midpoint), 4.1% end-2027, 3.9% end-2028, 3.2% longer run.
  **PCE inflation 3.7% for 2026, core PCE 3.4%.** Unemployment 4.1%, GDP 2.3%.
  — source: https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm
- Chair **Warsh**: "Inflation is too high and has been for too long."
  — source: https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20260916.pdf

**How I got it wrong, because it is worth recording.** I inferred "dovish FOMC"
from the 2026-09-17 tape — stocks and bonds rallying together — and treated that
inference as a fact for the next twenty minutes. It is a real pattern and it was
the wrong call here; a fully-priced hike can produce the same signature. The
FRED effective fed funds print of 3.63% (2026-09-16) that I quoted is the
**pre-hike** reading and I should have noticed it could not reflect the decision.
**Nothing in this file may rest on an inferred central bank action again — the
statement is one fetch away and I did not make it until minute 30.**

What actually holds now: policy 3.75-4.00% and rising, 2y 4.74%, **10y 5.01%**,
curve +0.27, core PCE 3.4%. This is a hiking cycle against elevated inflation.

**Consequences for the captured set, worked through one by one:**
- **TLT (short) — strengthened, and the reasoning was rewritten.** I had it right
  by accident: I argued "cutting into a steep curve" when the truth is "hiking
  with core PCE at 3.4% and one more hike in the dots". A hiking Fed is a
  straightforwardly better case for short duration. win_probability 0.36 -> 0.42.
- **EEM — the thesis was backwards and is rewritten.** I claimed a Fed easing into
  a weaker dollar as the driver. A hiking Fed and a firmer dollar is a *headwind*
  for emerging markets. The technical and relative-strength evidence still stands
  on its own fetched numbers, so the idea survives as a hold, but the macro is now
  against it and the thesis says so. win_probability 0.42 -> 0.34.
- **GLD — the "easing" case is dead, the inflation case is not.** Rising nominal
  and real short rates raise the cost of holding a non-yielding asset; 3.4% core
  PCE is the only remaining leg. Stays conviction 2. win_probability 0.40 -> 0.33.
- **LCII / KMX / NKE — unaffected but better explained.** Each already named the
  5.01% 10-year as hostile in `key_risk` rather than as support. A hiking Fed is
  *why* the whole rate-sensitive consumer complex is at 120-day lows, so those
  ideas were framed correctly and the framing is now properly grounded.
- **CEG — unaffected.** Its rate reference was already a risk, not a tailwind.
- **MU, KMX, DINO, XLE, PFE, SVRA, CCJ — no easing claim was made in any of them.**

## [06:33 ET] VENUE CHECK — Robinhood tradeability
All 13 candidates are US exchange-listed common stock or ETFs on
`Robinhood Stocks`, which is the venue with no availability ambiguity. Nothing
today required verifying a futures contract, a crypto listing or an event
contract, so no product-list lookup was needed:
- Stocks: MU, DINO, NKE, CCJ, CEG, LCII, PFE, SVRA, KMX — all NYSE/Nasdaq listed.
- ETFs: XLE, EEM, GLD, TLT — all major, multi-hundred-million daily dollar volume.
- Smallest name is **SVRA at $5.42**, above the $1 floor, avg daily dollar volume
  $7,795,402, clearly above the $500K floor. Sized at 1%.
- **TLT is a short and carries `requires_margin: true`.** It is the only position
  in the set that does.
- No futures substitution was applicable: `config/universe.md` prefers futures for
  index and crypto *direction* views, and no candidate today is one. The TLT short
  is a specific duration view on a fund that can be shorted directly.
- Nothing in the set moved more than 40% in the prior session.

## [06:33 ET] RESEARCH COMPLETE
- **candidates: 13 unique** (21 lines; MU, DINO, EEM, CEG, XLE, GLD, NKE, CCJ,
  LCII, PFE, SVRA, TLT, KMX — synthesis should take the last entry per symbol,
  since EEM, GLD, TLT, PFE and NKE were each re-captured after the Fed correction
  or the bear-case fix).
- **2 genuinely new ideas** (MU, KMX); **11 are position updates** on an open book
  of 16. That skew is real and should be stated rather than smoothed: with 16 live
  positions and a tape that offered few clean new setups, managing what is open
  was the higher-value work. **Nothing intraday cleared the bar** — see gaps.
- **NKE is published knowing it fails its floor** (1.15 vs 2.5). The reader holds
  it; the watchlist is the right destination for "hold, do not add".
- Changes made to open positions today, all of which should survive into the
  report: **LCII gained a stop (79.00) it never had**; **TLT gained both a target
  (78.00) and a stop (83.30)** it never had; **NKE's target was lowered 62.00 ->
  53.11**, which made its ratio worse. No stop was walked in anywhere.
- Recommended cancellations, all worked through and logged above: **VST @ 128.00,
  DG @ 134.50, IYR @ 103.60, BTC @ 63,400 and /MBTU6 @ 64,340** — none requalify
  and the two crypto shorts are 18-19% below spot on a contract that is at or past
  expiry.

**Coverage gaps — what I could not check:**
- **Event contracts: unreachable.** `market_data.py events` matched only
  `KXMVECROSSCATEGORY` sports parlays on every macro query tried (Fed,
  FEDDECISION, CPI, inflation, recession, Fed funds, rate, gold, bitcoin). No
  event contract idea was captured and none was invented.
- **Crypto: no levels possible.** `history` has no crypto source
  (`nasdaq returned no history for BTC-USD`), so ATR and stop distances could not
  be computed. Spot prices were fetched (BTC $78,143, ETH $2,507.18, SOL $106.37)
  but a candidate without a defensible stop is not publishable.
- **No intraday candidates, for a concrete reason:** the `history` source returned
  aggregates but a **null `recent` OHLC array for every symbol**, so no intraday
  or swing-level support/resistance could be read. All levels today are set off
  SMA20/SMA50, the 120-day range and ATR14. This is why several ideas were
  rejected for having "no target that clears" — the only levels available to aim
  at were the range extremes.
- **Options-implied moves: unavailable.** `implied` returns HTTP 401 from
  yahoo-options, so no target was checked against what the straddle prices — this
  matters most for **MU**, whose target is a 30.7% move into a print.
- **Short interest: unavailable.** `short` timed out against api.nasdaq.com.
- **SMA200 is null on every name** (only 120 bars fetched), so no long-term trend
  filter was applied.
- Yahoo returned HTTP 429 throughout, so index/VIX/DXY/futures quotes all failed
  and ETF proxies were used instead.

**Sources that failed:** yahoo (429 on all index/macro quotes; 401 on options),
api.nasdaq.com `short` (ReadTimeout), `market_data.py events` (returns unrelated
markets), `history` for crypto (no source). FRED, finnhub, CoinGecko,
api.nasdaq.com `history`/`insiders`/`analysts`/`relstrength`, SEC EDGAR and
federalreserve.gov all worked.

**The one thing synthesis must not lose:** the Fed **hiked** to 3.75-4.00% on
2026-09-16 with core PCE projected at 3.4% and another hike in the dots. An
earlier block in this file called it dovish; that block is corrected at 06:31 and
the correction is the accurate one.
