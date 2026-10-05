# Research log — 2026-10-05

## [06:03 ET] MACRO — rates, crypto, regime (Mon 2026-10-05, pre-open)

Source: `python scripts/market_data.py macro` (FRED + CoinGecko legs OK; Yahoo leg
rate-limited 429 across ALL index/VIX/DXY/gold/WTI quotes).

- US 10y **5.24%** (2026-10-01), prior 5.29% — source: FRED DGS10
- US 2y **4.78%** (2026-10-01), prior 4.88% — **-10bp in one day** — source: FRED DGS2
- Fed funds effective **3.88%** — source: FRED DFF
- 10y-2y curve **+0.45** (2026-10-02), prior +0.46 — source: FRED T10Y2Y
- Unemployment **4.2%** (Sep print), prior 4.1% — source: FRED UNRATE
- CPIAUCSL index 334.131 (Aug), prior 332.813
- TLT (bonds_20y proxy) **77.48**, -0.30% — source: stooq, delayed
- BTC **$85,955** +0.85% 24h; ETH **$2,716.81** +0.56%; SOL **$120.61** -0.58% — source: CoinGecko

Regime read: **front end rallying hard while the long end stays at 5.24%.** A 10bp
one-day drop in the 2y against an unchanged 3.88% effective funds rate is the market
pricing cuts; the 10y barely moved, so the curve is steepening from the front. With
unemployment ticking 4.1 -> 4.2 that is a labour-driven cut narrative, not a
growth-acceleration one. 10y at 5.24% with funds at 3.88% is an unusual configuration —
term premium, not policy.

Implication for the open book: the XLU short (entry 39.6) is a bet against long-duration
equity proxies; a falling 2y does not help it but a 5.24% 10y does. The TLT short awaiting
entry at 79.9 is the cleaner expression and has NOT filled.

## [06:04 ET] DATA GAP — Yahoo 429
Every Yahoo-sourced quote in `macro` failed with HTTP 429 (rate limited), including
^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES/NQ futures, DXY, 10y yield quote, gold, WTI.
No index level, no VIX, no dollar, no gold/oil price is available from that call.
Will retry per-symbol via `quote`/`history`; anything still unavailable goes in
data_quality_notes as unknown. **No index or VIX level is stated anywhere in these
notes that was not fetched.**

## [06:05 ET] CALENDAR — earnings inside 10 sessions
Source: `python scripts/market_data.py earnings --days 9` (finnhub, 197 rows)

- 2026-10-06: **STZ** (Constellation Brands), **LW** (Lamb Weston), RPM, NEOG, APOG, WS, SAR
- 2026-10-07: **LEVI**, **APLD** (Applied Digital), NRIX, RGP, RELL
- 2026-10-08: **PEP**, **TLRY**, HELE, BYRN, ANGO, ODC, NG
- 2026-10-09: **DAL** (Delta), CLSD, CCEL, HOVR
- 2026-10-13: **JPM, GS, C, WFC, JNJ, UNH**, DPZ, AZZ, FBK
- 2026-10-14: **BAC, MS, BLK, STT**, FAST, CBSH, HOMB, WAFD

Bank earnings 2026-10-13/14 are the dense cluster — 6 sessions out. Consumer staples
(STZ, LW, PEP) front-load this week.

## [06:16 ET] CALENDAR — this week's dated events
Source: https://www.cnbc.com/investingclub/2026/10/04/here-are-3-things-were-watching-in-the-stock-market-in-the-week-ahead.html
and https://investinglive.com/news/week-ahead-ism-services-fed-minutes-and-canadian-jobs-lead-the-economic-calendar-be-aware/

- **Mon 2026-10-05 09:45 ET** S&P Global Composite PMI (final), consensus 58.4
- **Mon 2026-10-05 10:00 ET** ISM Services PMI — the one dated intraday catalyst today
- **Wed 2026-10-07** FOMC minutes, September meeting
- **Thu 2026-10-08** ECB monetary policy accounts
- **Fri 2026-10-09** Canadian employment; US consumer sentiment
- Q3 earnings season does not start until **2026-10-13** (JPM/GS/C/WFC/JNJ/UNH)

Week is deliberately light. Week-ahead commentary names **Treasury yields and oil** as
the primary drivers of price action, with Middle East developments on oil sentiment.

## [06:17 ET] POSITION DIAGNOSTICS — stop distances on the open book
Source: `market_data.py history <SYM> --days 90` (nasdaq), closes are 2026-10-02

| Sym | Close | ATR14 | sma20 | sma50 | 90d range | Stop | Stop dist in ATR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CCJ | 85.18 | 3.041 | 92.16 | 94.62 | 83.15-122.30 | 82.5 | **0.88** |
| GDX | 87.78 | 2.929 | 93.65 | 91.44 | 69.74-105.67 | 85.4 | **0.81** |
| SVRA | 4.81 | 0.252 | 5.22 | 5.38 | 4.73-6.475 | 4.6 | **0.83** |
| SNX | 278.37 | 13.165 | 265.70 | 258.69 | 234.03-298.77 | 242.5 | 2.72 |
| XLU | 39.83 | 0.562 | 40.97 | 42.68 | 39.03-46.625 | 40.95 | 2.40 |

**Three of the five stops are under 1.0 ATR.** CCJ, GDX and SVRA are each sitting within
1 ATR of a stop that is itself parked just under a 90-day low. That is precisely the
configuration CLAUDE.md records as having produced all ten of the first month's
stop-outs. Each needs either a widened stop or a close; none of them may be held at
these levels and called risk management.

## [06:18 ET] NEWS — uranium: record price, collapsing equities
Sources:
- https://247wallst.com/investing/2026/10/03/uranium-prices-just-broke-a-19-year-record-but-nuclear-stocks-are-collapsing-anyway
- https://www.fool.com/investing/2026/10/04/cameco-trades-near-85-heres-why-the-uranium-giant/

- Long-term uranium price **$96/lb**, an all-time record, above the mid-2007 $95/lb high.
- CCJ nonetheless **-6.9% YTD**, closing 85.18 on 2026-10-02. UEC -20% YTD. NLR -16.4% YTD.
- Stated cause: **utilities are balking at signing new term contracts at these prices**;
  producers see delayed revenue realization. Named key metric: **term contracting volume**.

This is a genuine de-rating on an identifiable and fixable problem, not a broken
business — but the transmission from spot/term price to producer earnings is the thing
that is broken, and it is not a swing-horizon fix. Re-framing the open CCJ position from
swing to long_term, with term contracting volume as the invalidation, is the honest
handling. A 135 swing target sits above the 90-day high of 122.30 and is not reachable
inside a swing.

## [06:33 ET] NEWS — gold: a rates-driven pullback with a named cause
Sources: https://tradingeconomics.com/commodity/gold ,
https://investinglive.com/commodities/is-it-time-to-buy-the-gold-miners/
- Gold **$4,138.78/oz** on 2026-10-05, -0.03% d/d, **-6.04% over the trailing month**
- Pullback attributed to the **10-year yield breaking above 5.00%** (FRED has 5.24%)
- Commentary: October is a frequent seasonal peak in metals; some further downside
  possible, gold "could slip briefly below $4,000"; miners hold a bull-flag read as long
  as they stay above **Thursday 2026-10-01 low of $86.48** (GDX)
This is the same single macro fact driving XLU short, GDX long and the unfilled TLT
short — **correlation watch: those three are one rate bet with three faces.**

## [06:34 ET] POSITION UPDATE — SVRA — opened 2026-08-23 at 5.35, last 4.81, -10.1%
- decision: **hold, widen stop 4.60 -> 4.31** (0.83 ATR -> 2.00 ATR)
- why: PDUFA for MOLBREEVI (molgramostim) in autoimmune PAP is dated **2026-11-22**,
  verified from the company release. Three-month extension was a "major amendment" from
  the Company's own responses, and the release states the Agency **did not cite any
  safety, efficacy, or manufacturing concerns**. Priority Review granted on BLA filing
  Feb 2026; positive Phase 3 IMPALA-2 topline.
  Source: https://investors.savarapharma.com/news/news-details/2026/Savara-Announces-the-U-S--Food--Drug-Administration-FDA-Has-Extended-the-Review-Period-for-the-Molgramostim-Inhalation-Solution-Molgramostim-Biologics-License-Application-BLA-in-Autoimmune-Pulmonary-Alveolar-Proteinosis-Autoimmune-PAP/default.aspx
- the old stop was the problem, not the thesis: a 4.60 stop on a 5.24% ATR name 48 days
  before a binary gets removed by noise before the event it was placed for
- action: captured via add_candidate.py

## [06:35 ET] POSITION UPDATE — CCJ — opened 2026-08-17 at 94.0, last 85.18, -10.3%
- decision: **CLOSE**
- why: the macro leg was confirmed and the equity fell anyway. Uranium term price $96/lb
  (19-year record) while CCJ is -6.9% YTD. Underneath it the micro deteriorated:
  EPS -52.7% vs consensus for Q/E 2026-06-30 and -77.2% for 2025-09-30, 1 beat of 4;
  finnhub revision_direction "deteriorating", bullish share -3.9%; **zero** open-market
  insider buys in 6 months. The 82.5 stop was 0.88 ATR out and sat under the 90-day low.
- action: captured via add_candidate.py as direction `sell` (exit, not a short)

## [06:36 ET] DATA GAP — event contracts
`market_data.py events "Fed"` returns 8 markets, all of them multi-leg tennis parlays
matching the substring "Fed" inside "Federico". Queries "FEDDECISION", "interest rate"
and "CPI" each return **zero** markets. Three Fed/CPI event contracts sit unfilled in
the awaiting-entry book (KXFEDDECISION-26OCT-H25 YES @ 28 among them) and **I cannot
price any of them today** — no implied probability is quoted anywhere in these notes.

## [06:55 ET] CORRECTION — the 06:17 stop diagnostic was measured wrong
The table at 06:17 divided each stop's distance from the **current price** by ATR and
called three stops "under 1.0 ATR". The floor in `config/strategy.md` and in
`validate_report.py` is measured from **entry**, not from the last print. Recomputed
properly (`|entry - stop| / atr14`, floor 2.0 x asset factor):

| Sym | Entry | Stop | ATRs from entry | Floor | Verdict | R:R |
| --- | --- | --- | --- | --- | --- | --- |
| CCJ | 94.0 | 82.5 | 3.78 | 2.00 | OK | 3.57 |
| GDX | 91.2 | 85.4 | 1.98 | 1.80 | OK | 2.28 |
| SVRA | 5.35 | 4.60 | 2.98 | 2.00 | OK | 3.53 |
| XLE | 63.9 | 60.8 | 2.48 | 1.80 | OK | 2.13 |
| EEM | 65.6 | 63.0 | 2.55 | 1.80 | OK | 2.27 |
| DINO | 107.5 | 97.75 | 1.85 | 2.00 | **FAIL** | 2.10 |
| SNX | 260.0 | 242.5 | **1.33** | 2.00 | **FAIL** | 2.08 |
| XLU | 39.6 | 40.95 | 2.40 | 1.80 | OK | 2.07 |

So GDX and SVRA had **no construction defect** — both stops were honestly placed from
entry and both clear their floors. Widening them, as the 06:28 and 06:34 captures did,
took GDX from R:R 2.28 to 1.52 and broke a passing idea to fix a problem it did not
have. Both are being **re-captured at their original stops**.

The two that actually fail the ATR floor from entry are **DINO (1.85 vs 2.00)** and
**SNX (1.33 vs 2.00)** — and SNX is the one I asserted was "2.72 ATR out" in its own
capture, from the same miscalculation.

What remains true from the 06:17 observation, stated correctly: CCJ, GDX and SVRA are
each within ~0.9 ATR **of their stops as of Friday's close**, so each is roughly one
ordinary session from being stopped. That is a live-risk fact worth putting in
`key_risk`; it is not evidence that a stop was set too tightly, and the 06:17 note was
wrong to invoke the CLAUDE.md stop-out history for it.

## [06:57 ET] POSITION UPDATE — SNX stop fails the ATR floor and cannot be fixed
- entry 260.0 (filled, so entry may not be amended), stop 242.5 = 1.33 ATR, floor 2.00
- clearing 2.00 ATR needs a stop at or below 233.67, which is **below the 90-day low of
  234.025** and would put R:R at 36.47/26.5 = **1.38**, failing the 2.0 reward-to-risk
  floor instead
- there is no stop that satisfies both floors from a fixed 260 entry with a 296.47
  target. This is a position whose construction does not meet today's bar and whose
  entry is unamendable because it filled.
- decision: **hold and manage to target** — it is +7.1% with price above both rising
  moving averages — while stating the below-floor stop openly. If the pipeline demotes
  it to the watchlist on that basis, that is the correct outcome and must not be
  worked around by moving the target.

## [06:58 ET] POSITION UPDATE — DINO — opened 2026-08-22 at 107.5, last 113.36, +5.5%
- stop 97.75 = 1.85 ATR from entry against a 2.00 floor — a marginal fail, R:R 2.10
- structure is the strongest in the book: 113.36 over sma20 109.15 and sma50 99.37,
  -4.25% off the 90-day high, +77.62% off the 90-day low
- decision: **hold, levels unchanged.** Widening the stop to clear 1.85 -> 2.00 ATR
  means a stop at 97.0, which lifts nothing and loosens risk on a winner; tightening is
  the forbidden move. Logged as a known marginal construction miss, not repaired.

## [07:02 ET] NEWS — copper at a record on a supply story, not a demand one
Sources: https://www.marketbeat.com/articles/coppers-record-rally-highlights-a-deeper-supply-problem/ ,
https://ng.investing.com/news/stock-market-news/freeportmcmoran-shares-surge-as-copper-hits-record-14694ton-2687947
- LME 3-month copper intraday all-time high **$14,694/t**, above the prior record
  $14,527.50 set January 2026; LME cash tested ~$14,779/t; COMEX ~$6.87/lb
- **Chile reported its weakest Q2 output in at least 19 years** and has cut its full-year
  production forecast for a **second consecutive quarter**, projecting a 2.6% annual decline
- Demand side named as AI and grid buildout
- FCX YTD +41.23%, 12-month +64.56%

**Caution on a figure I did not verify as current:** these sources describe an FCX
"record peak of $74.52". My own fetch has FCX closing **72.04 on 2026-10-02** with a
90-day range high of **80.24**, so $74.52 cannot be a record and the articles are stale
on that point. Using only the fetched numbers: FCX 72.04, +3.98% that session, ATR14
2.4235, sma20 71.788, sma50 70.536, range 56.00-80.24, -10.22% off high.

## [07:03 ET] NOT RE-PITCHED — FCX — published yesterday at 68.2, unchanged
FCX BUY @ 68.2 was published 2026-10-04 and has not filled; Friday's close was 72.04, so
the entry sits **5.3% below the market** and below both the 20-day (71.79) and 50-day
(70.54). The copper supply story above strengthens the thesis, but re-pitching a
one-day-old idea at a higher entry because the tape moved up 4% is chasing, and that is
the pullback-entry reflex `config/strategy.md` singles out (31 pullback entries to 1
breakout, 42% ever filled). **Level unchanged at 68.2, no new capture.**

## [07:04 ET] BOOK CONFLICT — BCC long vs ITB short are the same bet twice, opposed
- `BCC` BUY open since 2026-08-18 at 76.5, last **74.99**, -7.4%, **no stop**
  (sma20 76.11, sma50 79.05, range 67.045-88.43, -15.2% off high)
- `ITB` SELL_SHORT @ 89.8 published 2026-09-30, unfilled, last **86.64**
BCC is building products and ITB is homebuilders; both are levered to housing starts and
the mortgage rate. Holding one long and the other short is either an unstated hedge or an
incoherence, and with the 10-year at 5.24% the short is the side consistent with the rest
of the book. Flagged for synthesis rather than resolved: BCC needs either a stop or an
explicit invalidation, and it has neither. I did not have budget to research BCC's
repair-and-remodel mix, which is the thing that would legitimately separate it from ITB.

## [07:05 ET] NEWS — financials are rolling over INTO their own earnings
Source: `market_data.py history` (nasdaq), closes 2026-10-02
- `XLF` 53.49, sma20 55.56, sma50 56.81, range 50.52-58.60, **-8.72% off high**
- `JPM` 332.38, sma20 345.32, sma50 352.24, range 295.195-366.50, **-9.31% off high**
Both are below both moving averages eight sessions before the 2026-10-13/14 cluster
(JPM, GS, C, WFC on the 13th; BAC, MS, BLK, STT on the 14th). The read worth recording:
a curve steepening from the front end (10y-2y +0.45) is normally a tailwind for bank net
interest margin, so banks selling off into it points at **credit** rather than margin —
consistent with unemployment ticking 4.1% -> 4.2%. **No candidate captured.** A long here
is catching a knife into a binary, a short fights four names with strong beat records,
and I ran out of budget before I could check loan-loss provisioning, which is the fact
that would decide it. **Flagged as the best-defined unfinished thread for tomorrow.**

## [07:10 ET] OPEN BOOK — the nine positions held with NO new capture
Decided and deliberately not converted, because nothing changed and a re-pitch of an
unchanged position is noise. All closes are 2026-10-02 (Friday); Monday is pre-open.

| Sym | Entry | Last | % | Stop | ATRs from entry | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| XLE | 63.9 | 62.82 | -1.7% | 60.8 | 2.48 OK | hold, unchanged |
| EEM | 65.6 | 67.67 | +3.2% | 63.0 | 2.55 OK | hold, unchanged |
| DINO | 107.5 | 113.36 | +5.5% | 97.75 | 1.85 marginal fail | hold, unchanged |
| PFE | 27.6 | 27.80 | +0.7% | none | n/a | hold; see repetition flag |
| BCC | 76.5 | 74.99 | -7.4% | none | n/a | flagged, unresolved |
| KHC | 23.0 | 22.19 | -3.5% | none | n/a | flagged, needs invalidation |
| NKE | 40.75 | 33.87 | -15.3% | none | n/a | see bookkeeping flag |
| LULU | 115.0 | 94.46 | -17.9% | none | n/a | see bookkeeping flag |

- `XLE` 62.82 between sma20 63.47 and a **rising** sma50 62.12, -5.06% off the 90-day
  high, +19.38% off the low. Structure intact, stop and ratio both pass. **Recommended
  3x in the last 10 days — do not re-pitch.**
- `EEM` 67.67 above sma20 67.45 and sma50 66.41. Working, passes both floors. 2x in 10 days.
- `KHC` 22.19 is **+0.84% off its 90-day low** of 22.005, -21.0% off the high, below
  sma20 24.01 and sma50 24.99. A no-stop long with no invalidation condition sitting on
  its low is the weakest risk control in the book. It needs one or it needs closing; I
  did not have budget to research the thesis and will not guess at an invalidation.
- `PFE` has been **recommended 4x in 10 days** and `XLU` 4x. Per `prior_context.md` that
  is an anchoring warning, not conviction. PFE is +0.7% at 27.80 with sma20 28.01 just
  above and sma50 27.33 just below — genuinely nothing changed, so nothing is captured.

## [07:11 ET] BOOKKEEPING FLAG — NKE and LULU each hold a BUY and a SELL row
- `NKE` BUY 40.75 (2026-08-17, -15.3%) **and** `NKE` SELL 38.4 (2026-09-08, +11.8%)
- `LULU` BUY 115.0 (2026-08-22, -17.9%) **and** `LULU` SELL 100.61 (2026-09-08, +6.1%)
In both cases the SELL was an exit recommendation on the long, and because the two carry
different `direction` values `merge_report`'s one-live-position-per-(symbol, direction)
rule lets them coexist as separate rows. The effect is that each name now shows a losing
long and a winning short on the same thesis, and the "+11.8%" on NKE SELL is the long's
own loss counted a second time with the sign flipped. **For synthesis: this is a
tracking artefact, not two positions, and neither should be re-pitched today.** The
economic position in NKE is one long, -15.3%; in LULU one long, -17.9%.

## [07:12 ET] REJECTED — XLF / JPM — banks into 2026-10-13 earnings, thesis undecided
Both -8.7%/-9.3% off their highs and below both MAs eight sessions before their prints.
Could not check loan-loss provisioning inside budget, and without it a long is a knife
catch into a binary and a short fights 4-of-4 beat records. No candidate.

## [07:12 ET] REJECTED — FCX — level unchanged at 68.2, re-pitch would be chasing
See 07:03. Copper fundamentals improved (LME record $14,694/t, Chile -2.6% full-year
guide cut, second consecutive cut); entry stays where it was published yesterday.

## [07:13 ET] REJECTED — all event contracts — no price data available today
`events` returns tennis parlays for "Fed" and zero rows for "FEDDECISION", "interest
rate" and "CPI". An event contract requires a stated implied probability against my own,
and I have no implied probability for anything. The four unfilled Fed/CPI contracts in
the book are left exactly as published. **This is the biggest coverage gap today** and
it is a tooling gap, not a market one.

## [07:13 ET] REJECTED — new energy and new rate ideas — correlation cap reached
Energy already carries XLE, DINO and the unfilled OXY; the rate bet already carries XLU
short, GDX long and the unfilled TLT short. `config/strategy.md` caps a single driver at
3 ideas, and both are at 3. Oil was named by week-ahead commentary as a primary driver
this week, so this is a real opportunity declined on portfolio grounds, not an absence.

## [07:14 ET] RESEARCH COMPLETE
- candidates: **12 rows across 7 distinct symbols** — XLU, CCJ, GDX, SVRA, DAL, SNX,
  LCII (CCJ, GDX, SVRA, SNX and LCII were re-appended after the 06:55 correction;
  synthesis takes the last row per symbol, so the corrected versions are the live ones)
- **only 1 of the 7 is new risk: DAL.** Everything else is position management — one
  close (CCJ), one long-term reframe with a new invalidation (LCII), and four holds at
  unchanged levels (XLU, GDX, SVRA, SNX)
- **the one error to carry forward:** the 06:17 stop table divided by distance from the
  last print instead of from entry, and I acted on it before catching it at 06:55.
  GDX and SVRA were briefly "fixed" when they were not broken. Corrected captures
  supersede both. The real floor failures are SNX (1.33 ATR) and DINO (1.85 ATR), both
  disclosed and neither repairable without breaking the reward-to-risk floor instead.
- coverage gaps: **no index, VIX, DXY, gold-futures or WTI quote at all** (Yahoo 429 on
  every leg of `macro`); **no event-contract prices** (see 07:13); no options-implied
  move for any name (`implied` returns Yahoo 401); BCC and KHC left without a stop or an
  invalidation; bank loan-loss provisioning unchecked; ISM Services at 10:00 ET today has
  no fetched consensus, so no intraday candidate was built on it
- sources that failed: Yahoo chart API (429, all index/commodity/FX quotes), Yahoo
  options API (401, `implied`), Finnhub index quotes (CFD subscription required), Stooq
  (404 on ^GSPC/^NDX/^DJI/^RUT), Alpha Vantage (no API key), Kalshi via `events`
  (returns substring-matched parlays, no Fed/CPI markets)
- sources that worked: FRED (rates, unemployment, CPI index), CoinGecko (crypto),
  Finnhub (equity quotes, earnings calendar, analyst trend, insider transactions),
  Nasdaq (OHLCV and all ATR/SMA figures)
