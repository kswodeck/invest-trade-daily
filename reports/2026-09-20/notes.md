# Research log — 2026-09-20

## [06:03 ET] MACRO — Sunday run, US equities/futures closed
Weekend behavior per config/strategy.md: crypto + event contracts carry actionable
ideas; equities are week-ahead prep with entry marked for the next open.

FRED (fetched, source https://fred.stlouisfed.org):
- Fed funds effective **3.88%** as of 2026-09-17, prev **3.63%** — a ~25bp HIKE
  landed at the September FOMC. This is the single most important fact today.
- US10Y **4.94%** (2026-09-17), prev 5.01% — long end *fell* on the hike.
- US2Y **4.67%**, prev 4.74% — also fell.
- 10y-2y curve **+0.25** (2026-09-18), prev +0.27 — still positive, flattening slightly.
- Unemployment **4.1%** (Aug 2026), unchanged.
- CPIAUCSL **334.131** (Aug 2026) vs 332.813 prior = **+0.40% MoM**, an annualized
  ~4.9% — hot. Consistent with a Fed that hiked.

Read: the Fed hiked into sticky inflation and the curve *bull-flattened* rather than
selling off. That is the market pricing the hike as restrictive enough to slow growth
— a policy-error / growth-scare tape, not a reflation tape.

Sources that FAILED this run (note for data_quality_notes):
- Yahoo Finance returning HTTP 429 on every index symbol. spx, ndx, dow, russell2000,
  vix, es/nq futures, DXY, us10y quote, gold, wti all `ok: false`. stooq 404s on ^-prefixed
  index symbols. No Alphavantage key. So **no index or VIX level was fetched today** —
  I will not state one.
- TLT (bonds_20y) did fetch: **81.25**, -0.65% — previous close, market closed.

## [06:04 ET] CRYPTO — 24/7, so this is the live tape (source: coingecko)
- BTC **80,441** (-1.05% 24h), mcap $1.62T, 24h vol $24.2B
- ETH **2,579.12** (-2.34%)
- SOL **108.26** (-3.17%)
- DOGE **0.084932** (-2.65%)
- LINK **12.00** (-4.03%)
- AVAX **9.81** (**+8.97%**) — the only green name on the board, idiosyncratic, worth a look
- XRP **1.38** (-2.09%)
- LTC **56.92** (-0.52%)

Broad crypto is bleeding into a hiking Fed. AVAX +9% against a -2 to -4% tape is a
genuine outlier and the first thing to investigate.

## [06:08 ET] EVENT MARKETS — market_data.py events is broken for search; worked around
`python scripts/market_data.py events "<topic>"` returns nothing useful: it pulls only the
first 200 open Kalshi markets unsorted and filters client-side, so topical search returns
tennis and NFL markets. Querying the Kalshi API directly by `series_ticker` works, but the
`/markets` summary endpoint returns **null for every price field** (yes_bid/ask/last/volume/
open_interest). Prices ARE available from `/markets/{ticker}/orderbook` and
`/markets/trades?ticker=`. Derived yes_ask as 1 - best no_bid. All below traded this morning,
so these are live weekend quotes, not stale.

**October FOMC (closes 2026-10-28), source https://api.elections.kalshi.com:**
- `KXFEDDECISION-26OCT-H25` Hike 25bps — yes 54/55c, last trade 55c @ 09:39 UTC
- `KXFEDDECISION-26OCT-H0`  Hold      — yes 44/45c, last trade 44c @ 09:36 UTC
- `KXFEDDECISION-26OCT-H26` Hike >25  — yes 1/2c
- `KXFEDDECISION-26OCT-C25` Cut 25bps — yes ~1c

**December FOMC (closes 2026-12-09):**
- `KXFEDDECISION-26DEC-H25` Hike 25bps — yes 66/67c
- `KXFEDDECISION-26DEC-H0`  Hold       — yes 30/31c
- `KXFEDDECISION-26DEC-C25` Cut 25bps  — yes 1/2c

**Recession (NBER):** `KXRECSSNBER-26` 5/6c · `KXRECSSNBER-27` 22/23c

Read: the market prices a ~55% chance of a SECOND consecutive hike in October and ~66% by
December, and has essentially written off any cut this year (1-2c). Yet 2026 recession odds
are 5c and 2027 only 22c. So the consensus is "Fed keeps hiking AND nothing breaks."

## [06:19 ET] POSITION UPDATE — CEG — opened 2026-08-21 @ 272.00, now 254.71, -6.4%
- decision: **CLOSE** on the Monday open
- why: published stop 250.00 is 4.71 from price against ATR14 10.78 = **0.44 ATR**. Below
  SMA20 (277.89) and SMA50 (271.16). Widening the stop to the only real support (120d low
  228.63) gives 272→320 target vs 272→228.63 risk = **1.09:1**, under the 2.0 swing floor.
  The position fails the report's own rules at every honest stop level.
- action: captured via add_candidate.py (conviction 2, thinness stated — this is price
  structure only, no new fundamental information reached)

## [06:23 ET] CALENDAR — dated earnings inside the next 10 sessions (source: finnhub via market_data.py earnings)
Only the tradeable/liquid names; the list also carried ~100 micro/OTC tickers I ignored.

| Date | When | Symbol | EPS est | Why it matters here |
| --- | --- | --- | --- | --- |
| 09-22 | bmo | AZO | 54.80 | consumer, big-ticket deferral |
| 09-22 | bmo | THO | 0.92 | RV — rate-sensitive discretionary |
| 09-22 | bmo | FERG | 2.48 | building products |
| 09-22 | amc | KBH | 0.90 | **homebuilder into a hiking Fed** |
| 09-23 | bmo | CTAS | 1.38 | employment proxy |
| 09-23 | bmo | PAYX | 1.35 | **SMB payrolls proxy** |
| 09-24 | amc | COST | 6.67 | consumer staple |
| 09-24 | bmo | DRI | 2.07 | restaurants |
| 09-24 | bmo | **SNX** | 4.69 | **already published BUY @260 (09-19), pending — now has a dated catalyst 4 sessions out** |
| 09-25 | amc | UEC | -0.05 | uranium — reads across to the open CCJ long |
| 09-28 | — | **NKE** | 0.45 | **open BUY (-11.2%) AND open SELL both live — earnings forces the issue** |
| 09-28 | bmo | CCL | 1.37 | consumer credit |
| 09-28 | amc | MTN | -5.28 | discretionary |
| 09-29 | — | KMX | 0.72 | **used cars = consumer credit + rates** |
| 09-29 | — | CAG | 0.29 | staples |
| 09-30 | amc | **MU** | 32.22 | **already published BUY @960 (09-18), pending — earnings 9/30** |
| 09-30 | bmo | JBL | 4.10 | AI hardware supply chain |
| 09-30 | — | JEF | 0.95 | capital markets |

Three of the report's own pending/open ideas (SNX, MU, NKE) have earnings inside 10 sessions.
That is the priority: they are already on the sheet and the dated event changes how to hold them.

## [06:34 ET] CORRECTION — crypto is near its highs, NOT selling off
My 06:04 note read the 24h change as weakness. Daily series says otherwise and the
24h read was wrong. Fetched from CoinGecko market_chart (120d, daily):
- **BTC last 80,468** · avg |daily move| over 14d = **1.40%** (~$1,130) · SMA20 78,416 ·
  SMA50 73,193 · 120d high 81,264 · 120d low 58,566 · **-1.0% off the 120-day high**
BTC is above both averages and within 1% of its 120-day high. The -1% 24h print is noise
inside an uptrend. ETH/SOL/AVAX daily pulls hit CoinGecko 429 — not retried, no daily ATR
for them, so **I am not setting levels on ETH, SOL or AVAX today.**

CAUTION for anyone reading the 06:2x working numbers: CoinGecko's /ohlc endpoint at
days=90 returns **4-day candles, not daily** (23 rows for 90 days). An "ATR14" off that is a
14-period ATR of 4-day bars and overstates daily range by roughly 3-4x. Do not use it as a
daily ATR. The 1.40% figure above is the honest daily one.

AVAX was +8.97% on 24h and sits ~0.5% off its 90-day high — a real outlier, but I could not
get daily data for it and did not find the reason. **Not captured.** Logged as a gap.

## [06:38 ET] EVENT CONTRACT CAPTURED — KXRECSSNBER-27 YES @ 23c
- Verified on Robinhood: prediction-markets/economics/events/recession-in-2027-apr-24-2026
  (RH shows ~25%, Kalshi book 22/23c — note the venue basis).
- The ticker says NBER; **the rules do not.** rules_primary is two consecutive negative BEA
  advance-estimate real GDP quarters, Q4'26-Q4'27, and rules_secondary explicitly allows the
  Q4'26+Q1'27 pair. That kills the "NBER dates recessions two years late" objection, which
  was the reason I nearly rejected it. Read the rules, don't trust the ticker.
- My estimate 35% vs 22.5% implied; 3.35:1 payoff vs a 23% break-even. Conviction 4.

## [06:47 ET] POSITION UPDATE — NKE — the report is holding two contradictory rows
- `NKE` BUY opened 2026-08-17 @ 40.75, now 35.51, **-11.2%, no stop**
- `NKE` SELL opened 2026-09-08 @ 38.40, now **+7.5%**
Both live at once. The September exit was right; the August long is the stale row.
- decision: **CLOSE the remaining long**, flat before the 09-28 print
- levels: close 35.51 vs 120d low **35.50** (0.03% off it), SMA20 38.00, SMA50 40.45,
  -33.14% off the 120d high 53.11, ATR14 0.8907
- the genuine argument against, and it is not weak: **insiders bought** — 5 open-market
  purchases, 4 distinct buyers, $3.73M bought vs $1.20M sold, net **+$2.53M**/6mo
  (Hill Elliott 23,660 sh @ 42.27 on 2026-04-13). But those buys are 16% underwater, so
  they are evidence of a view, not a floor. Analyst trend drifting down: bullish share
  39.1%, hold 25, sell ratings 2 -> 3 since July.
- action: captured (conviction 3)

## [06:49 ET] POSITION UPDATE — SNX — entry unchanged, catalyst now dated
Published 09-19 @ 260, unfilled. Close 266.16, SMA20 257.66, SMA50 254.40, ATR14 7.78.
260 is above the 20-day = real support, not a reflex discount. **Earnings 09-24 bmo**,
four sessions out — it was undated when published. Added a hard cancel at the 09-23 close
so a stale limit cannot fill into the print. Stop 244 = 2.06 ATR, R:R 2.25. Captured.

## [06:51 ET] POSITION UPDATE — MU — WAIT; cancel the resting limit
Published 09-18 @ 960, unfilled. Close **1015.80**, i.e. the entry is 5.5% BELOW market.
The only way it fills inside 7 sessions is a selloff into the **09-30 amc** print — which
silently converts a swing idea into an unsized earnings bet. This is the exact
pullback-entry failure mode the strategy config already measured.
- 960 is itself fine: SMA20 is 959.60.
- but positioning is hostile: **0 insider buys / 187 sales / $214.3M** over 6 months, and
  **91.4%** analyst bullish share (18 SB, 35 B, 4 H, 1 S). Up **+226%** off the 120d low.
- decision: `wait: true`, cancel before 09-30, re-enter after the reaction. Captured.

## [06:53 ET] POSITION HYGIENE — two problems synthesis should not paper over
1. **`/MBTU6` SHORT @ 64,340 (published 2026-08-18) is on an expired contract month.**
   U6 = September 2026. On 2026-09-20 that contract is at or past its final trading date.
   It is also directionally stale: BTC is **80,468**, far above the 64,340 short entry.
   A short limit at 64,340 should have filled as price rose through it in August. Whatever
   the tracker says, this row cannot be carried forward as "awaiting entry" — flag it.
2. **Conflicting live rows on the same symbol**, same shape as NKE:
   - `GLD` BUY @ 398 (open, +0.8%) vs `GLD` SELL @ 406.77 (awaiting entry, 09-08)
   - `LULU` BUY @ 115 (open, -14.7%) vs `LULU` SELL @ 100.61 (open, +2.5%)
   LULU is the worse one — both sides are *open*. LULU closed 98.06, ATR 5.59 (5.7%),
   -42.4% off the 120d high, 2.8% off the 120d low, below SMA20 109.30 and SMA50 115.38.
   The unstopped BUY is the stale row, on the same logic as NKE.

## [06:55 ET] REJECTED — BTC / /MBT — strong uptrend, but no differentiated view
BTC 80,468, -1.0% off the 120d high, above SMA20 78,416 and SMA50 73,193, avg daily move
1.40%. Long at the highs into a Fed the same market says will hike twice more is not an
edge, and shorting a trend this intact is worse. Weekend rules push toward crypto, but
"it is Saturday" is not a thesis. No candidate — declining to pad.

## [06:56 ET] REJECTED — Oct vs Dec FOMC spread (KXFEDDECISION-26OCT/DEC)
Oct hike 55c vs Dec hike 66c is a genuinely interesting term structure, and the two are
not independent. But I did not reach the September FOMC statement or dot plot this run,
so any claimed disagreement would be the "feels underpriced" the universe config forbids.
Rejected for lack of a stated, sourced probability disagreement — not for lack of interest.
This is the single best follow-up for tomorrow.

## [06:57 ET] REJECTED — consumer-discretionary short basket (CCL, KBH, KMX)
Real and consistent: every one closed below both its 20- and 50-day average, CCL at 21.84
vs a 120d low of 21.81 and -30.9% off its high, KBH -25.9% off its high, KMX -12.4%.
All three report inside 10 sessions (CCL 09-28, KMX 09-29, KBH 09-22 amc). Rejected on two
counts: (a) the correlation cap — the book already runs `TLT` SELL and a pending `IYR`
SELL_SHORT on the same rate-path driver, and these would make five; (b) initiating shorts
at 120-day lows the week of earnings is chasing, not edge. The observation is instead used
as the `positioning` evidence under the recession contract, where it belongs.

## [06:12 ET] CORRECTION — every timestamp above this line is wrong
I estimated elapsed time instead of calling `date`, which the skill explicitly warns
against, and drifted badly. Run started **06:00:51 ET**; the real time at the LULU capture
was **06:12:12 ET**, not the 06:57 I had written. So the blocks above labelled 06:03
through 06:58 actually span roughly **06:01 to 06:12**. The findings, prices and sources in
them are unaffected — only the clock labels are wrong. Timestamps from here are from `date`.

Consequence: I have ~48 minutes of budget left, not ~2. Resuming research rather than
closing out. Six candidates are already captured and safe on disk.

## [06:17 ET] MACRO — the September FOMC, read from the primary source
**Primary document** — Fed statement, 2026-09-16
(https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm):
- Raised the target range by 1/4 point to **3-3/4 to 4 percent**. **Unanimous, 12-0, no dissents.**
- "Inflation remains elevated. Today's policy action will support a timelier return to the
  Committee's 2 percent goal."
- **First hike since 2023.**
**Dot plot / SEP** (two independent secondary sources agree): end-2026 median raised to
**4.10%** from 3.80% in June. Of 18 participants: **12 at 4.125%** (one more hike), **4 at
4.375%** (two more), **2 at current** (none). So 16 of 18 see at least one more, and the
**central case is exactly ONE more hike** across the two remaining meetings.
Remaining 2026 FOMC dates: **Oct 27-28** (decision Wed Oct 28, 2:00pm ET) and **Dec 9**.
Kalshi's Oct close time of 2026-10-28T17:59Z lines up with the 2pm ET announcement.
Gap: could not retrieve Powell's September press conference; CNBC 403'd and the Fed's SEP
PDF would not parse. No October-specific guidance from Powell was read.

## [06:26 ET] CORRECTION + REJECTED — the Fed-path trade I thought I had does not exist
I had reasoned from the per-meeting contracts (Oct hike 55c, Dec hike 66c) that the market
implied a ~99% chance of at least one more hike, against the dots' 89% — and concluded the
market was overpricing tightening. **That inference was invalid.** Those two events are
strongly negatively correlated (hiking in October reduces the need to hike in December), so
adding or multiplying them under independence is meaningless. The cumulative contract says
so directly:
- `KXFED-26DEC-T4.00` (upper bound above 4.00% = **at least one more hike**) — **84/85c**
- `KXFED-26DEC-T4.25` (above 4.25% = **two more hikes**) — **34/35c**
- `KXFED-26DEC-T4.50` — 1/4c
Backing out the market's coherent joint distribution for 2026:
| Outcome | Implied |
| --- | --- |
| No further hike | **15%** |
| One hike, October only | 20% |
| One hike, December only | 31% |
| Hikes at both meetings | **35%** |
This cross-checks against the per-meeting quotes exactly (0.35+0.20 = 0.55 Oct; 0.35+0.31 =
0.66 Dec), so the ladder is internally consistent. **85% vs the dots' 89% means the market is
if anything slightly LESS hawkish than the committee.** My thesis was backwards.

The one genuine disagreement left: the market prices **back-to-back hikes at 35%** where only
**4 of 18** officials (22%) project a 4.375% midpoint. But that can only be traded from the NO
side at ~65c, i.e. **0.54:1** — it fails every reward-to-risk floor in the strategy config, and
a near-coinflip binary like October HOLD at 45c caps out at 1.22:1 no matter how good the edge.
**Rejected: real edge, untradeable ratio.** Not captured, and not dressed up to look tradeable.

## [06:28 ET] AMENDED — KXRECSSNBER-27 re-captured with corrected wording
The original capture said the venue prices "a 55% chance the Fed hikes again in October and
66% by December". The second half was loose: 66c is the December *meeting* contract, whereas
"by December" cumulatively is the 85c T4.00 contract. Re-captured with the cumulative figure
and the full implied distribution, which actually strengthens the setup — the market says 85%
more tightening and only a 15% chance the Fed is already done, while pricing a 2027 contraction
at 22-23c. Thesis unchanged; the numbers backing it are now stated correctly.

## [06:47 ET] LONG_TERM — KHC — captured, conviction 4
The long_term lane was empty until now; config says it is the one most easily crowded out,
so it got deliberate time rather than leftovers. Screened ten de-rated defensives
(CAG KHC GIS PGR TRV CB BMY MRK GILD VZ). MRK, GILD, TRV and CB are all above their 50-day
and near highs — working, not cheap. The de-rated group is packaged food: KHC -13.0% off
high, GIS -13.9%, CAG -9.6%, all three below both averages.

KHC is the one with something behind the cheapness rather than just decline:
- **Price/FCF 7.12 vs a 10-year median of 13.75** — a 48% discount. FCF $3,661M, $3.33/share
  against a $24.43 price = **13.6% FCF yield**. Dividend $1.60 (**6.50%**), covered **2.1x**.
- The TTM **-$5.76B loss is goodwill impairment** on the 2015 merger, not cash — which is why
  the P/E screens as null. That accounting/cash gap is most of the mispricing.
- EV/EBITDA 8.18. Net debt $17.04B on $24.99B revenue — levered, not distressed.
- **CEO Steven Cahillane bought 213,106 shares at $23.4616 on 2026-05-12 — $5.0M**, the only
  open-market insider buy in six months. He is currently in profit, unlike NKE's buyers.
- **Analysts 7.1% bullish**: 2 strong buy, 0 buy, **17 hold, 7 sell**, flat four months.
- Break-up **paused** Feb 2026 by the new CEO, who redirected $700M into brands. That removed
  the story's only dated catalyst — hence long_term accumulation, no stop.
- Target $33.30 = 10x FCF (still 27% under its own 10Y median). Bear case $19.50. Entry in
  thirds 24.50 / 23.50 / 21.75. Invalidation stated in key_risk: FCF/share under $2.50 for
  two consecutive quarters, or a dividend cut. Not "the price fell."
- GIS rejected by comparison: zero insider buys, 3 sells, bullish share falling 3.6 points.
  Same cheapness, nobody inside it buying. CAG left for the 09-29 print.

## [06:19 ET — verified by `date`] SECOND TIMESTAMP CORRECTION
Drifted again. The blocks labelled 06:17 / 06:26 / 06:28 / 06:47 above were written between
**06:12 and 06:19 ET** real time. Run start 06:00:51; verified checkpoints: 06:12:12 (LULU
capture), 06:18:51 (KHC sanity check). Roughly 18 minutes elapsed, not the ~47 I had been
labelling. Every price, source and figure is unaffected — clock labels only. From here I am
pasting `date` output rather than estimating.

## [06:19 ET] CANDIDATE SANITY CHECK — all 8 lines / 7 unique symbols pass their floors
| Symbol | Dir | Horizon | Conv | R:R | Break-even | Claimed | Edge | Stop in ATR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KXRECSSNBER-27 | yes | long_term | 4 | 3.35 | 0.230 | 0.35 | +12.0 | n/a (premium at risk) |
| KHC | buy | long_term | 4 | 2.94 | 0.254 | 0.42 | +16.6 | n/a (bear case 19.50) |
| SNX | buy | swing | 3 | 2.25 | 0.308 | 0.42 | +11.2 | **2.06** |
| MU | buy | swing | 4 | 2.05 | 0.328 | 0.40 | +7.2 | **2.05** |
| CEG / NKE / LULU | sell | swing | 2/3/2 | exits — no target or stop by design | | | | |
Floors: swing R:R 2.0, long_term 2.5, stock stop 2.0 ATR. All clear. No claimed edge exceeds
the 20-point "large claim" threshold. MU is the marginal one at 2.05 R:R on a 2.05 ATR stop —
it clears on both axes but only just, and it is a `wait` recommendation anyway.

## [06:20 ET] CORRECTION to the 06:53-labelled position-hygiene note — GLD is not like LULU
I listed `GLD` BUY @398 (open) vs `GLD` SELL @406.77 (awaiting entry) as a contradictory pair.
On re-reading that is wrong, or at least overstated: GLD trades at 401.17, so a SELL resting at
**406.77 is above the market** — that is a take-profit on the existing long, not an opposing
directional call. It is coherent. The LULU pair genuinely is contradictory because **both legs
are open positions** and the short was struck below the long's entry; NKE is the middle case
(one open, one pending, struck below). Only LULU and NKE were captured as exits. GLD left alone.

## [06:22 ET] NOT CAPTURED — CPI YoY ladder: an 84-point discrepancy I could not explain
The most interesting thing I found today, and deliberately **not** turned into a candidate.

**Setup.** `KXCPIYOY-26SEP-*` resolves on the BLS one-decimal CPI-U YoY for the twelve months
ending September 2026, released ~2026-10-14. Rules read from the API. Using **NSA (CPIAUCNS)**,
which is the right basis — my first pass used CPIAUCSL and would have been wrong:
- Aug-2026 NSA 334.98 vs Aug-2025 323.976 → **YoY 3.3966%** (reports as 3.4%)
- Sep-2025 base = 324.8
- So Sept-2026 YoY = 1.031343 x (1 + Sept MoM) - 1. Required MoM by threshold:

| Contract resolves YES if reported YoY... | needs Sept NSA MoM | market implied | 11y Sept base rate |
| --- | --- | --- | --- |
| `T3.4` > 3.4, i.e. >= 3.5 | **>= +0.306%** | **93.5%** | 1/11 = **9%** |
| `T3.6` > 3.6, i.e. >= 3.7 | **>= +0.518%** | **46.5%** | 1/11 = **9%** |
| `T3.8` > 3.8, i.e. >= 3.9 | >= +0.71% | 4% | 0/11 |

**September NSA MoM, 2015-2025:** -0.156, +0.240, +0.529, +0.116, +0.078, +0.139, +0.272,
+0.215, +0.249, +0.160, +0.254. Mean **+0.191%**, median +0.215%, stdev 0.158. The only year
clearing +0.306% was **2017** (+0.529%, Harvey/Irma gasoline spike).
And 2026's own recent NSA prints are soft, not hot: Jun **-0.349%**, Jul **-0.010%**, Aug +0.318%.

**Why I did not trade it.** The gap on T3.4 is ~84 points. That is not a mispricing, that is a
signal that I have something wrong. I checked the obvious explanation — stale or illiquid
quotes — and it is not that: **T3.4 has 25,741 contracts bid at 0.92**, spreads are 1c wide,
and all four strikes traded within the last few hours. This is deep, live, real money.

Candidate explanations I could not rule out inside the budget:
1. **A September-specific shock I do not know about** — tariff pass-through, an energy move, or
   a BLS methodology/weight change. Most likely explanation.
2. **A base-period problem.** FRED returns **None for 2025-10-01** in CPIAUCNS, which is
   unusual and hints at a late-2025 data disruption; the contract's own `rules_secondary` has
   explicit government-shutdown language. If the 2025 base months are estimated or revised, my
   Sep-2025 = 324.8 base may not be what resolution uses.
3. I have mis-specified the rounding boundary, though I checked it twice.

**Follow-up for the next run, high priority:** re-pull these quotes fresh, check whether a
September tariff or energy event explains a +0.5% print, and confirm the Sep-2025 NSA base
against BLS directly rather than FRED. If the market is still at 93c on T3.4 and none of
1-3 holds, the NO side at ~6c is the largest edge this report has ever found — which is
itself the reason to be suspicious and to verify before acting, not after.

Recording the discrepancy is the deliverable here. Trading an 84-point edge I cannot explain
would be the opposite of what the conviction rules are for.

## [06:25 ET] SMALL CAP SCREEN — documented negative result, nothing captured
Config wants small caps hunted deliberately, so they got a real pass rather than a mention.
Screened 10 names carrying dated catalysts inside 10 sessions. Liquidity floor applied first:
**BSET rejected outright at $388K average daily dollar volume**, under the $500K floor.

| Sym | Close | ATR% | off 120d high | off low | $vol30 | Catalyst | Insider buys | Analysts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UEC | 9.81 | 5.91 | -41.7% | +10.2% | $81.5M | 09-25 amc | **0** | 84.6% bull |
| AIR | 112.77 | 4.37 | -26.8% | +13.2% | $44.7M | 09-21 | **0**, 7 sells -$10.4M | 75%, **-6.8pts** |
| CALM | 72.89 | 2.64 | -23.5% | **+0.2%** | $64.6M | 09-30 | 0 (none either way) | 54.5% |
| SCHL | 34.75 | 3.84 | -27.7% | +1.8% | $12.0M | 09-24 amc | **0**, 8 sells -$14.3M | **0% bull** |
| MLKN | 20.66 | 3.81 | -16.4% | +49.3% | $11.6M | 09-22 bmo | 0 | 75% |
| WOR | 57.38 | 4.02 | -9.1% | +14.1% | $18.0M | 09-22 amc | 0, 3 sells | 75% |
| SFIX | 2.84 | 4.29 | -38.0% | +1.1% | $4.2M | 09-23 amc | — | — |
| TAYD | 60.08 | 3.15 | -20.7% | +24.1% | $2.6M | 09-29 | — | — |
| IDT | 69.84 | 2.57 | -3.2% | +46.8% | $14.0M | 09-28 | — | — |

**Not one of them has a single open-market insider purchase.** That is the discriminator the
skill names — executives buy for one reason — and without it each of these is a chart plus an
earnings date, which is two evidence kinds at best and no confirmation that a de-rated name is
cheap rather than broken. AIR is the clearest trap: down 27%, no insider buying, 7 insider
sales worth $10.4M, and analysts still **75% bullish and falling** — the downgrade cycle
probably is not finished, so it is neither a long nor a short I would initiate into Monday's
print. SCHL is the mirror image: 0% bullish already, 8 insider sales, nothing left to
de-rate on but nobody inside buying either.
**Nothing captured. Publishing fewer beats padding with six of filler.**

## [06:26 ET] OPEN POSITION REVIEW — a decision on all 16, recomputed from fetched data
Stop distances in ATRs, from entry and from the current price, with R:R recomputed:

| Sym | Side | %vs entry | stop ATR (entry) | stop ATR (now) | R:R | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| XLE | BUY | +0.6% | 2.33 | 2.64 | 2.13 | **HOLD** — clean on every axis, above both MAs |
| EEM | BUY | +2.2% | 2.70 | 4.18 | 2.27 | **HOLD** — clean |
| GLD | BUY | +0.8% | 2.22 | 2.64 | 2.29 | **HOLD** — the 406.77 SELL is a take-profit, not a conflict |
| TLT | SELL | +0.8% | 2.07 | 2.96 | 2.71 | **HOLD** — short bonds into a hiking Fed, working |
| SVRA | BUY | +0.4% | 3.69 | 3.79 | 3.53 | **HOLD** — lottery ticket, sized as one, stop is wide enough |
| CCJ | BUY | -2.5% | 3.41 | 2.70 | 3.57 | **HOLD** — structurally fine though below both MAs; UEC 09-25 is the read-across to watch |
| DVN | BUY | -2.0% | **1.98** | **1.25** | 2.19 | **HOLD, flagged** — see below |
| DINO | BUY | +7.8% | 2.24 | — | 2.24 | **AMEND** — stop 97.75 -> 105.00, captured |
| CEG | BUY | -6.4% | 2.04 | **0.44** | — | **CLOSE**, captured |
| LCII | BUY | -8.9% | **no stop** | — | — | **CLOSE**, captured |
| NKE | BUY | -11.2% | **no stop** | — | — | **CLOSE**, captured |
| LULU | BUY | -14.7% | **no stop** | — | — | **CLOSE**, captured |
| BCC | BUY | -1.1% | **no stop** | — | — | HOLD, see below |
| PFE | BUY | +0.2% | **no stop** | — | — | HOLD, see below |
| LULU/NKE SELL legs | SELL | +2.5% / +7.5% | — | — | — | **HOLD** — these are the correct side |

Three things flagged but deliberately **not** captured, with reasons:
- **DVN** was published with a stop **1.98 ATR** from entry — fractionally inside the 2.0 floor,
  so it should not have passed validation. It is now only **1.25 ATR** from the market. But it
  is a filled position: widening the stop to a compliant 2.5 ATR (46.19) drops R:R to **1.73**,
  under the swing floor, so there is no amendment that fixes both. Left alone and recorded.
- **BCC and PFE carry no stop at all.** Both are within ~1% of entry so neither is in distress,
  and unlike CEG/LCII neither is at a low or below its range. I did not capture stop-additions
  for them because every such amendment mechanically inflates the published R:R from an
  unchanged entry — the KRE pattern — and doing it twice more on positions that are not
  actually in trouble trades a real reporting distortion for a theoretical risk reduction.
  Flagged here so it is on the record rather than silently fixed.
- **PFE has now been recommended 4x in 10 days** and its target of 42.00 implies +52% from the
  27.60 entry. Deliberately not re-pitched today: that frequency is the anchoring signal
  prior_context warns about, and nothing new was found on it this run.

## [06:27 ET] REJECTED — KXBTCMAXY-26DEC31 BTC year-end ladder — priced correctly, no edge
Weekend rules push toward crypto and event contracts, so this got a full quantitative pass
rather than a glance. Result: **the market is fair.** Recording the arithmetic because a
documented "no edge" is worth as much as a candidate.

**Rules catch that changes the trade** (read from the API, not assumed from the title): the
barrier window opens **2026-01-02 18:00 ET**, not today — it is a whole-year look-back on the
CF Bitcoin Real-Time Index. BTC's trailing-365d max is **$124,740**, but that is from late
2025, outside the window; the $100k strike trading at 27c rather than ~99c is the market
confirming the barrier has not been touched since January.

**Realized volatility, computed from 366 daily CoinGecko closes** (stdev of log returns):
| Window | daily sigma | annualized |
| --- | --- | --- |
| 14d | 2.043% | **39.0%** |
| 30d | 1.919% | 36.7% |
| 60d | 2.109% | 40.3% |
| 120d | 2.064% | 39.4% |
| 365d | 2.338% | 44.7% |
Note my earlier 1.40% "avg daily move" understated this — converting an average absolute move
to sigma assumes normality, and BTC has fat tails. Using proper realized vol matters: at 33.5%
the model said 22% and the contract looked rich; at 39% it does not.

**Model vs market**, BTC spot 80,312, 102 days to 2026-12-31, driftless barrier-touch
(P_touch ~= 2 x N(ln(K/S)/sigma)):
| Vol used | Model touch prob | Market |
| --- | --- | --- |
| 30d (37%) | 25.8% | **27/28c** |
| 120d (39%) | 29.3% | 27/28c |
| 60d (40%) | 30.3% | 27/28c |
| 365d (45%) | 35.3% | 27/28c |
The market sits inside the model range on every window. Higher strikes are similarly sane
(110k at 15/16c vs 7.8-20% modelled; 150k at 3/4c). **No candidate.** An edge that exists only
under one hand-picked volatility assumption is not an edge, it is the assumption.

Also checked and rejected: `KXBTCD`/`KXETHD` daily strikes all close **2026-09-20T11:00Z**,
about 30 minutes after this run — they would settle before any reader could act.

## [06:29 ET] INSIDER SCAN — the discriminator that actually produced ideas today
Ran `market_data.py insiders` across every beaten-down liquid name already priced this run.
Open-market purchases (Code P) only; sales noted but weighted as weak evidence.

| Sym | Buys | Distinct buyers | Buy value | Sells | Net | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| **KMX** | 6 | **5** | $1,268,037 | **0** | +$1.27M | **captured** (wait @ 53) |
| **CAG** | 3 | **3** | $1,119,535 | **0** | +$1.12M | **captured** (buy @ 15.00) |
| **KHC** | 1 | 1 (CEO) | $4,999,808 | 1 | +$4.57M | **captured** (long_term) |
| NKE | 5 | 4 | $3,734,194 | 6 | +$2.53M | counter-evidence on the NKE exit; stated, not hidden |
| VST | 1 | 1 | $270,000 | 7 | **-$4.98M** | one small buy against seven sales — not a cluster |
| CCL | 0 | 0 | — | 4 | -$1.52M | no |
| KBH | 0 | 0 | — | 8 | -$16.58M | no |
| BCC / GIS / SFIX / MLKN / DG / AIR / UEC / CALM / SCHL / WOR / MU / SNX | 0 | 0 | — | — | — | no |

Three names with a genuine buy cluster and no offsetting sales, and all three became candidates.
Everything else screened had zero. That ratio is why the scan is worth running before setting
levels rather than after.

Two analyst-revision reads worth recording — the config says read the *change*, not the level:
- **KMX bullish share 7.1% (June) -> 28.0% (September), +20.9 points**, sell ratings 8 -> 1.
  Largest revision swing found this run, and it lines up with the insider cluster.
- **CAG at 4.0% bullish**: 0 strong buy, 1 buy, 14 hold, 8 sell, 2 strong sell. Ten negative
  ratings against one positive. Lower than KHC's 7.1%.

**KMX honesty note.** I used KMX's own chart as evidence of consumer weakness in the recession
contract and then captured it long. Those are in real tension. Reconciled narrowly — the
recession trade is a five-quarter aggregate-GDP claim, this is a single company with improving
insider and analyst signals — and the tension is written into the KMX counter_argument along
with the statement that if only one survives red-teaming it should be the recession contract.
It is also why KMX is `wait: true` at a price 7.4% below the market rather than a buy today.

## [06:30 ET] NOT CAPTURED — VST, despite one insider buy
`VST` BUY @128.00 is already pending from 2026-08-24. Burke James A bought 2,000 shares at
135.00 on 2026-08-24 — but against **seven sales totalling a net -$4.98M**. One small purchase
inside heavy net selling is not the signal; a cluster with no sellers is. Left as-is, not
re-pitched, and specifically not dressed up as insider support.

## [06:32 ET] INSIDER SCAN, ROUND 2 — 16 more liquid names; one large cluster found
Scanned F GM INTC WBA TGT DLTR EL CVS HUM BA NCLH ULTA CROX ETSY CHWY PARA.
Only three had any open-market buying at all, and only one was a cluster:
- **NCLH: 10 buys, 7 distinct buyers, $29,163,646, ZERO sells** — by dollar value the largest
  insider cluster found in this entire run, ~6x the KHC CEO purchase and ~23x the KMX cluster.
- F: 1 buy (Thornton, 10,600 @ 14.05) — single buyer, not a cluster.
- BA: 1 buy (Tilden, 1,370 @ 218.50) — token size.
- The other 13: zero open-market purchases.

## [06:33 ET] NCLH — captured as a TRIGGERED entry, and why not as a dip buy
All eight NCLH purchases: Pagliuca 685,000 @ 18.06 and 695,000 @ 18.16 (~$25M of the $29M),
Chidsey 153,000 @ 16.37, Cohen 30,000 @ 15.83, Cil 10,000 @ 14.91 + 5,000 @ 15.25,
MacDonald 15,000 @ 16.54, Lansberry 11,400 @ 17.28. Range **$14.91-$18.16**.
**NCLH closed at 14.12 — below every one of them.** Pagliuca is down ~22% on $25M.

Fetched levels: close 14.12, ATR14 0.525 (3.72%), SMA20 15.60, SMA50 17.77, 120d range
14.07-22.22, **+0.36% off the low**, -36.45% off the high, $211M/day so liquidity is ample.
Analysts moving the wrong way: 41.2% bullish, **-8.8 points**, buys 11 -> 8 as holds 15 -> 19.

So the largest insider signal of the day sits on top of the worst tape of the day, in leveraged
consumer discretionary, against a Fed the event market says hikes again with 85% probability,
with peer CCL also pinned to its own 120-day low. Captured as `wait: true` with a **stop_limit
entry at 15.60 — 10% ABOVE the last close** — requiring a daily close back over the 20-day
before any position exists. Stop 14.05 (under the 120d low) = 2.95 ATR; target 19.00 (the
insider zone) = R:R 2.19.

The reason for the structure is sitting in today's own notes: **NKE has 4 insider buyers, net
+$2.53M, and they are 16% underwater with the stock at its low** — I cited that as the reason
the NKE cluster is "evidence of a view, not evidence of a floor," and the identical logic
applies here with a bigger number attached. A cluster marks conviction; it does not mark a
bottom. Paying 10% for confirmation is the price of not learning that twice in one report.

## [06:33 ET] RESEARCH COMPLETE
- **candidates: 14 lines / 12 unique symbols** (synthesis takes the last entry per symbol;
  KXRECSSNBER-27 and DINO were each re-captured once, deliberately, and the later line is the
  one to use — see the amendment notes above).
- All 12 clear every floor in `config/strategy.md`: swing R:R >= 2.0, long_term >= 2.5, swing
  stops >= 2.0 ATR, every win_probability above its break-even, no claimed edge above 20 points.
- Conviction spread **2:x2, 3:x5, 4:x5** — no collapse to a default 3, and every score is the
  count of distinct evidence kinds actually gathered.

**Shape of the day.** Sunday, US equities and futures shut, so every equity level is the
2026-09-18 close and every equity entry is for the next open. Five of the twelve are position
management rather than new ideas, which is the honest output given 16 open positions and a
hiking Fed — **CEG, NKE, LULU and LCII to close, DINO to trim by half**. New money ideas are
KHC (long_term), KXRECSSNBER-27 (long_term event), CAG (swing), and three deliberate waits
(MU, KMX, NCLH).

**The macro frame everything hangs off.** The Fed raised to 3.75-4.00% on 2026-09-16,
unanimously 12-0, its first hike since 2023, and the event market prices an 85% chance of at
least one more by December against only a 15% chance it is done. The dots say one more is the
central case (12 of 18). CPI YoY is 3.35-3.40%.

**Coverage gaps — what I could not check:**
- **No index or VIX level was fetched all run.** Yahoo returned HTTP 429 on every index symbol
  (SPX, NDX, DJI, RUT, VIX, ES, NQ, DXY, gold, WTI) and stooq 404s on `^`-prefixed tickers.
  No Alphavantage key. I stated no index level anywhere as a result.
- **No daily crypto data for ETH, SOL or AVAX** — CoinGecko 429'd after BTC. AVAX was +8.97%
  on 24h and near its 90-day high, an unexplained outlier I could not research. BTC only.
- **Powell's September press conference** — CNBC 403'd and the Fed's SEP PDF would not parse.
  Dot-plot figures came from two agreeing secondary sources, not the primary table.
- `market_data.py short` timed out on NCLH, so **no short-interest read on any candidate**.
- **`market_data.py events "<topic>"` is effectively broken** and I worked around it all run:
  it fetches only the first 200 open Kalshi markets unsorted then filters client-side, so any
  topical search returns tennis and NFL. The `/markets` summary endpoint also returns null for
  every price field; prices must come from `/orderbook` and `/trades`. Worth fixing in code.

**Sources that failed:** Yahoo Finance (429, all indices + crypto history), stooq (404 on index
symbols), Alphavantage (no key), CoinGecko market_chart (429 after ~2 calls), CNBC (403),
federalreserve.gov SEP PDF (unparseable), nasdaq short interest (timeout).

**Highest-value follow-up for the next run, in order:**
1. **The CPI YoY discrepancy.** `KXCPIYOY-26SEP-T3.4` trades 93/94c with 25,741 contracts bid
   at 0.92, implying September NSA MoM >= +0.306%, against an 11-year September mean of
   +0.191% where only 2017 cleared it. An ~84-point gap on a deep, liquid book means I am
   missing something — a tariff or energy effect, or a 2025 base-period problem (FRED returns
   null for 2025-10 CPIAUCNS). Resolve it before anyone trades it. Do not trade it on this note.
2. The Oct/Dec FOMC term structure with Powell's actual guidance in hand.
3. AVAX's +8.97% outlier.

## [06:35 ET] KHC UPGRADED to conviction 5 — read the actual 10-Q
Went back for the primary document rather than leaving the best idea resting on an aggregator.
**10-Q, quarter ended 2026-06-27, filed 2026-08-05** (SEC, CIK 0001637459). Six months:
| Line | 2026 | 2025 |
| --- | --- | --- |
| Net cash from operations | **$2,088M** | $1,929M |
| Capital expenditures | $429M | $425M |
| **Free cash flow** | **$1,659M** | $1,504M |
| Dividends paid | $949M | $951M |
Net loss attributable to shareholders **$(4,662)M**, containing **goodwill impairment $2,441M
+ intangible impairment $4,924M = $7,365M of non-cash charges.**
Balance sheet: cash $2,419M, LT debt $17,619M + $1,382M current = **~$19,001M total**, net ~$16.6B.

This is the thesis confirmed on the primary source: **the loss is impairment; operating cash
flow ROSE year over year.** A genuine melting ice cube does not grow OCF. Dividend covered
**1.75x** by FCF on the filed six-month figures.

**It also made me cut my own target.** The aggregator's TTM FCF/share of 3.33 implied 33.30 at
10x. The filed six-month run-rate annualises nearer $3,318M, about **3.02/share** — so I lowered
the target to **32.00** (~10.6x the conservative figure, ~9.6x the TTM figure) rather than keep
the flattering multiple. R:R 23.00 -> 32.00 against a 19.50 bear case = **2.57**, still clearing
the 2.5 long_term floor, but honestly rather than by choosing the input that worked.
Both FCF figures are now stated in the evidence rather than just the better one.
Evidence kinds now 4 — primary_document, valuation_anchor, positioning, technical_level —
so conviction 5 is earned by count, not by enthusiasm.

Also confirmed from the filing list: Forms **25** and **8-A12B** (2026-09-08) plus NYSE
certification (2026-09-09) — the Nasdaq-to-NYSE move is real. Still US-exchange-listed common
stock, so Robinhood-tradeable; no venue issue.

## [06:36 ET] BOOK COHERENCE CHECK — correlation caps and the long/short tension
| Driver | Ideas | Cap |
| --- | --- | --- |
| Packaged food / staples | KHC, CAG | 2 of 3 |
| Consumer discretionary | KMX, NCLH | 2 of 3 |
| Tech / semis | SNX, MU | 2 of 3 |
| Aggregate US growth | KXRECSSNBER-27 | 1 of 3 |
| Energy (pre-existing book) | XLE, DVN + DINO trim | at cap, nothing added |
All within the cap of 3 on one driver.

On the apparent contradiction of holding a recession bet while capturing two consumer longs:
**both KMX and NCLH are `wait: true`** — KMX needs a 7.4% decline to 53.00, NCLH needs a daily
close 10% higher at 15.60. Neither is a position today. The book reads coherently as "the macro
says tighten up; here are the two names with real insider clusters and the exact conditions
under which they become buyable." That is deliberate, and the tension is written into each
idea's counter_argument rather than smoothed over.

Second insider scan of 18 names across healthcare, financials, industrials, materials and tech
(MRNA BIIB VTRS BAX ZBH SCHW USB TFC ALLY COF EMR FDX NSC NEM MOS CF QCOM ADBE) found
**zero clusters with 2+ distinct buyers.** Documented negative result; nothing forced from it.

## [06:37 ET] INSIDER SCAN, ROUND 3 — 22 names (utilities, telecom, transport, REITs, retail)
Scanned ED AEP D EXC T VZ TMUS UPS CHRW XPO ODFL O VICI WPC IRM PSA HAS VFC PVH KSS BBY DKS.
Two hits, **neither captured**:

- **DKS — REJECTED on the net.** 5 buys by 4 distinct buyers, $3.72M, at $128.70-$130.72 in
  late August. But **9 sells and net -$43,393,485**. A buy cluster sitting inside $43M of net
  selling is not the signal; this is the same test that rejected VST earlier today, applied
  consistently. A cluster only counts when there is nothing going the other way.

- **VFC — REJECTED as strictly dominated.** Clean on the net (2 buyers, $1,007,762, zero
  sells): Bracken 32,894 @ 14.98 on 07-31, Carucci 30,000 @ 17.167 on 06-09. But: close
  **12.79**, only 2.69% off the 120-day low of 12.455 and -42.6% off the high, below SMA20
  13.31 and SMA50 14.77, ATR 3.48%. **Both buyers underwater** (-14.6% and -25.5%). Analysts
  flat at 42.9% for four straight months — no revision signal at all.
  This is the same trade as NCLH — beaten-down consumer discretionary, underwater insider
  buying, sitting on the low — but weaker on every axis: **2 buyers and $1.0M versus NCLH's
  7 buyers and $29.2M**, and NCLH at least has a defined trigger. It would also have been a
  third consumer-discretionary name, taking that driver to the cap of 3 for a strictly inferior
  version of a position already captured. **Capturing it would have been padding, so I did not.**

Across all three insider scans: **56 names screened, 5 clean clusters found** (NCLH, KHC, CAG,
KMX, VFC), 4 captured, 1 rejected as dominated, 2 rejected on net selling (DKS, VST).

## [06:37 ET] RESEARCH COMPLETE — AMENDED (supersedes the 06:33 block)
The 06:33 completion block was written when I still expected less remaining budget. Four
things were added after it: the NCLH capture, the KHC upgrade to conviction 5 on the 10-Q,
and insider scan rounds 2 and 3. Final state:

- **15 lines / 12 unique symbols.** Synthesis takes the last entry per symbol. Three symbols
  were re-captured deliberately and only the later line should be used:
  **KHC** (upgraded to conviction 5 on the 10-Q, target cut 33.30 -> 32.00),
  **KXRECSSNBER-27** (corrected wording on the cumulative Fed pricing),
  **DINO** (restructured from a stop-raise to a half-trim).
- **Every candidate clears every floor**, and **every conviction score equals its count of
  distinct evidence kinds** — verified mechanically, not asserted.

| Conv | Symbol | Dir | Horizon | Size | Wait | R:R | Edge |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | KHC | buy | long_term | 3% | no | 2.57 | +14.0 |
| 4 | KXRECSSNBER-27 | yes | long_term | 1.5% | no | 3.35 | +12.0 |
| 4 | CAG | buy | swing | 2% | no | 2.17 | +13.5 |
| 4 | KMX | buy | swing | 2% | **yes** | 2.73 | +15.2 |
| 4 | MU | buy | swing | 2% | **yes** | 2.05 | +7.2 |
| 3 | SNX | buy | swing | 2% | no | 2.25 | +11.2 |
| 3 | NCLH | buy | swing | 1.5% | **yes** | 2.19 | +8.7 |
| 3 | NKE / LCII / DINO | sell | swing | exit / exit / half-trim | | | |
| 2 | CEG / LULU | sell | swing | exit / exit | | | |

**Only four ideas call for action on Monday's open**: close CEG, NKE, LULU and LCII, and trim
half of DINO. Of the new money ideas, CAG is the one enterable now; KHC is an accumulation
starting under 24.50; KMX, MU and NCLH are all explicit waits. That is the honest shape of a
Sunday with 16 open positions and a Fed that just hiked.

**Three things I got wrong during the run and corrected in place**, all recorded above rather
than quietly fixed: (1) I twice wrote timestamps from estimation instead of `date` and drifted
by up to 35 minutes; (2) I inferred an ~99% implied probability of further hiking by
multiplying two negatively-correlated per-meeting contracts, when the cumulative contract says
85% — my "market overprices tightening" thesis was backwards and was abandoned; (3) my first
DINO amendment raised a stop under a fixed historical entry, manufacturing an 8.20 R:R and a
39-point edge claim, which is the KRE pattern this report already learned from.

Coverage gaps, failed sources, and the high-priority CPI follow-up are unchanged from the
06:33 block above and still apply.

## [06:38 ET] RELATIVE STRENGTH — the config check I nearly skipped, and it changed an idea
`market_data.py relstrength SYM --peer <sector ETF>` on every captured long. Sector-relative,
which is the read that matters — "everything in staples is down" is different from "this one is."

| Symbol | Peer | vs peer 1m | vs peer 3m | vs peer 6m | Read |
| --- | --- | --- | --- | --- | --- |
| **KMX** | XLY | **+3.42%** | **+11.85%** | **+33.78%** | leading its sector badly; confirms the insider + revision read |
| **CAG** | XLP | -2.40% | **+15.22%** | -2.76% | strong 3m leadership despite a weak month — supportive |
| **KHC** | XLP | -0.55% | **+7.66%** | **+11.26%** | outperforming staples; not a falling knife relative to its group |
| SNX | XLK | +2.46% | -5.51% | +34.39% | mixed; 1m improving |
| MU | XLK | +5.15% | -9.46% | **+91.68%** | momentum name, 3m consolidation |
| **NCLH** | XLY | **-12.20%** | **-25.69%** | **-29.32%** | **lagging SPY on every window measured** |

Three of the four insider-cluster ideas got independent confirmation from a completely
different measure — KMX, CAG and KHC are all *outperforming their own sectors* on 3m despite
being cheap and disliked, which is exactly the combination worth owning.

**NCLH did the opposite and I re-captured it because of that.** Down 25.7 points against XLY
over three months and 29.3 over six is not a sector being repriced — it is the market
discriminating against this specific company while its peers hold up, and a $29M insider
cluster has failed to arrest it in three months. The idea was already `wait: true` behind a
20-day reclaim, which is the right protection, but the earlier capture buried this. The
re-captured version puts the relative-strength numbers in the evidence array as explicit
counter-evidence alongside the insider cluster, makes it the headline of `key_risk`, and states
in the counter_argument that buying idiosyncratic underperformance on purchases made three
months and 22% ago is the trade this report keeps losing money on.

Worth recording as a method note: the insider scan and the relative-strength check disagree
only on NCLH, and they disagree loudly. Where two independent measures conflict that sharply,
the answer is a trigger, not a position.

## [06:40 ET] COMPLIANCE CHECK — clean, and the skew is deliberate
Ran every candidate against `config/universe.md`: venue strings, direction vocabulary per
venue, `unit` (cents for the event contract, usd elsewhere), position sizing against the 5% cap
and tier table, downside present on every idea, no sub-$1 names, liquidity floor on everything
where I fetched dollar volume. **All 12 clean. No margin required by any idea** (no
`sell_short`; the four `sell` entries are exits of existing longs, not new shorts).

**Asset classes present: stock and event only. Horizons: swing and long_term only.**
That is a pronounced skew and synthesis should say so plainly in `data_quality_notes` rather
than let the reader assume the other lanes were searched and found empty. Each has a reason:

- **No `intraday`.** It is Sunday. US equities and futures are shut, every equity price here is
  the 2026-09-18 close, and an intraday idea would be fiction. Not a gap — a fact about the day.
- **No crypto**, despite weekend rules pushing toward it. BTC got a full quantitative pass and
  the year-end ladder came back fairly priced against realized vol on every window (27/28c
  against a 26-35% model range). ETH, SOL and AVAX could not be priced at all because CoinGecko
  rate-limited after BTC, so I had no daily ATR for them and set no levels. AVAX's +8.97% move
  is an unexplained outlier carried into the follow-up list.
- **No futures.** No futures expression with an edge turned up, and the one futures row already
  in the book — `/MBTU6` SHORT @ 64,340 — is on an expired September contract and directionally
  stale with BTC at 80,468. Flagged for removal rather than replaced with something invented.
- **Five of twelve are position management** rather than new ideas. With 16 open positions, four
  of them unstopped and one stopped 0.44 ATR from the market, that is where the value actually
  was today. The skill says manage open positions before hunting new ones, and doing it properly
  consumed a real share of the budget.

Nothing was added to fill a lane. Six complete candidates beat fifteen fragments; twelve with
every floor cleared and every conviction score matching its evidence count is the day's output.
