# Research log — 2026-10-20

## [06:03 ET] MACRO — data availability
- `market_data.py macro`: Yahoo index/futures/FX/commodity quotes all returned
  HTTP 429 (rate limited) at 06:01 ET. SPX, NDX, DJI, RUT, VIX, /ES, /NQ, DXY,
  US10Y, gold, WTI all `ok: false`. Only `bonds_20y` resolved: TLT 79.46,
  -0.74% (pre session, i.e. prior close).
  — source: scripts/market_data.py macro, 2026-10-20T10:01:13Z
- Consequence: no live index/VIX/rates read this morning. Macro regime framing
  below is drawn from FRED and from single-name quotes that did resolve, and
  index-level claims are omitted rather than estimated.

## [06:03 ET] CALENDAR — fetched earnings, next 5 sessions
Source: `market_data.py earnings --days 12` (finnhub), 481 names through 10-26.
Dated events touching the existing book or watchlist:
- **UNP** — 2026-10-22 bmo, EPS est 3.5061, rev est $7.2B. OPEN POSITION
  (entered 10-15 @ 288.6). Earnings inside the horizon.
- **ABT** — 2026-10-21 bmo, EPS est 1.4297, rev est $13.1B. AWAITING ENTRY @ 103.
- **AAL** — 2026-10-22 bmo, EPS est -0.3639. AWAITING ENTRY short @ 13.35.
- **NEM** — 2026-10-22 amc, EPS est 2.1314 (gold; GLD short awaiting entry).
- **NUE** — 2026-10-26 amc, EPS est 5.9792 (steel; STLD open position).
- **CVX** — 2026-10-30 bmo (energy; XLE open position).
Other majors this week: GM/RTX/NOC/PM/MMM/HAL 10-20 bmo; NFLX/UAL/COF/CB/ISRG
10-20 amc; META/TSLA/IBM/LRCX/TXN/CSX 10-21; VLO/PG/LMT/GD/HON/DOW/NSC 10-22;
AXP/SLB 10-23.

## [06:06 ET] PRIOR CLOSES — whole open book (19 positions)
Source: `market_data.py quote` (finnhub), session `pre` = 2026-10-19 close.
XLE 67.80 (-0.64%) | BCC 75.12 (-1.33%) | PFE 29.44 (-0.47%) | DG 133.27 (-0.81%)
IYR 96.24 (-1.18%) | LULU 97.76 (+0.68%) | NKE 37.21 (+0.22%) | SNX 248.57 (+0.74%)
KHC 23.17 (-2.15%) | TLT 79.46 (-0.74%) | CEG 263.19 (-3.01%) | FCX 69.75 (+0.30%)
XLF 55.06 (-0.83%) | SMMT 15.57 (+6.43%) | STLD 245.17 (+1.92%) | HII 269.64 (-0.87%)
GE 311.28 (-0.81%) | UNP 287.01 (-0.70%) | CVS 92.68 (+0.35%)
Biggest movers vs the prior_context snapshot: CEG -3.0%, SMMT +6.4%, KHC -2.2%,
STLD +1.9%, IYR -1.2% (short, in favour).

## [06:10 ET] POSITION UPDATE — UNP — opened 2026-10-15 @ 288.6, now 287.01 (-0.55%)
- decision: HOLD, exits unchanged (target 315.99, stop 277.4)
- why: new fact is the confirmed Q3 earnings date, 2026-10-22 bmo, EPS est
  3.5061 / rev est $7.2B off the fetched finnhub calendar. Stop 277.4 is
  2.63 ATR below entry on ATR14 4.2648 (1.49%) — wide enough to survive the
  print's noise. Target 315.99 is the measured 120-day range high.
  Analyst trend improving: 73.3% bullish of 30 analysts, 0 sells, +7.8pts since
  July as holds converted to buys. No insider buys in 6 months (4 sells,
  $8.78M) — absent, not negative.
- `implied` unavailable: yahoo-options returned HTTP 401, so there is no
  options-implied move check on this idea.
- action: captured via add_candidate.py, conviction 4, R:R 2.45, win_prob 0.40
  vs a 0.29 baseline.

## [06:12 ET] POSITION UPDATE — CEG — opened 2026-10-01 @ 272.0, now 263.19 (-3.2%)
- decision: **CLOSE**. Not a re-pitch and not a short.
- why: volatility regime change, caught by arithmetic rather than by news.
  ATR14 is now 17.0994 = **6.50% of price**. That makes the 250.0 stop only
  **1.29 ATR** below entry and **0.77 ATR** below Monday's close — against a
  2.0 ATR swing floor for a stock. Re-cutting it honestly does not save it: a
  2.0 ATR stop from spot is 229.0, a point above the 228.63 120-day low, and
  the 320 target then pays 1.66:1 against the 2.0 floor. strategy.md is
  explicit — an idea that only clears the floor on a tight stop has failed it.
- tape confirms rather than contradicts: lower closes 5 of the last 6 sessions
  (300.40 on 10/06 → 263.19), below SMA20 273.86 and SMA50 275.55, and 10/19
  printed a 15.3-point range closing on its low at 263.19 on 3.82M vs 3.80M
  30-day average volume.
- accepted risk: this may sell the low on a name 19.95% off its 328.80 high.
- action: captured via add_candidate.py as a `sell` exit instruction with
  target null and stop null, since the resulting position is flat.

## [06:14 ET] MACRO — Monday 2026-10-19 close, from web (own feed was 429'd)
- **The day was one factor: rates.** 10-year **5.14-5.15%, +4 to +6bp**; 30-year
  reported near 2002 highs. Utilities **-2.01%** the worst S&P sector, real
  estate **-1.16%**. That single move explains CEG, IYR, KHC and TLT with no
  company-specific story in any of them.
  — source: https://investrade.com/market-review-october-19-2026/
- S&P 500 **7,690.73 +0.41%**; Nasdaq Composite **26,430.89 +1.11%**;
  Dow **51,966.03 -0.07%**; Russell 2000 ~2,728 +0.25% — a tech-led rebound
  with the Dow dragged by JPMorgan. — same source
- **VIX 18.44, -7.75%** (4:15pm ET 10/19) — source:
  https://www.bloomberg.com/quote/VIX:IND. Cboe's 10/19 digest: VIX had risen
  ~5pts w/w to ~20 into Fri 10/16 on a scramble for downside hedges, 1M SPX
  30-delta skew 15th → 82nd percentile, MOVE 99-102 —
  https://www.cboe.com/insights/posts/week-of-10-19-2026-scramble-for-downside-hedges-fuels-vix-surge-ahead-of-mega-cap-earnings
- **WTI $103.66, +2.22%**; Brent **~$110 intraday** on Houthi missile strikes on
  Saudi targets, attacks on shipping near Hormuz, and a Ukrainian strike on a
  Russian refinery. XOM/CVX/MPC all printed 52-week highs intraday.
  — https://stocktwits.com/news-articles/markets/equity/why-did-xom-cvx-mpc-stocks-surge-to-52-week-highs-today/cZxq1SXRBua
- Gold (Dec futures) **$4,160.10, -0.50%**. DXY **~101.8** (sources split
  101.82 vs 101.99 — recorded as a range, not a point).
- **UNVERIFIED / not used for any recommendation:** exact DXY settle, XLU's own
  % move, an Amazon/AEP 960MW nuclear story dated 10/19 that no primary source
  corroborates. Three supporting pages were snippet-only (HTTP 403 on direct
  fetch): CappNotes, cnttrading Substack, Constellation IR.

## [06:15 ET] CORRECTION — STLD 8-K of 2026-10-19 is NOT the earnings release
The 2026-10-19 8-K (tm2627861d1) is an Item 8.01 notice of a press release
titled "Steel Dynamics Announces Leadership Promotions" — no financials. The
Q3 results came separately, same day, after the close. Verified the actual
figures from the release rather than relying on the headline.

## [06:16 ET] POSITION UPDATE — STLD — opened 2026-10-10 @ 245.5, 245.17 pre-print
- decision: HOLD, stop unchanged 228.75, target unchanged 281.0
- the print (released after the 10/19 close): diluted EPS **$5.26** vs $5.42
  Zacks consensus and vs the company's own 2026-09-17 guide of **$5.34-5.38**
  — a miss on both. But the release reads strong: net sales $6.509B (+34.8%),
  net income $756.0M vs $403.7M, adj EBITDA $1.19B vs $663.8M, **record
  3,784,484 tons** shipped, steel ASP **$1,400/ton, +$102 sequential**,
  fabrication backlog **+50% y/y extending into Q2 2027**, $276M of Q3 buyback.
  — https://www.prnewswire.com/news-releases/steel-dynamics-reports-third-quarter-2026-results-302913069.html
- the variance is identifiable and dated: **Aluminum segment operating loss
  $(26.2)M** on $475.7M of sales while ramping; second CASH line commissioned
  early Q1 2027, management expects aluminum volumes and profitability to
  improve in Q4 2026 and through 2027. That loss is larger than the $0.16/sh
  gap to consensus.
- **data gap stated honestly:** no post-release price was obtainable. The only
  quote available is the 2026-10-19 16:00 ET close of 245.17, age 850 minutes.
  The report must not imply the reaction is known.
- action: captured, conviction 4. Added instruction: if it opens below 228.75,
  close at the open — a gap through a stop is not a stop.

## [06:17 ET] POSITION UPDATE — GE — opened 2026-10-12 @ 308.0, now 311.28 (+1.1%)
- decision: HOLD, do not add. **GE reports Q3 pre-open TODAY 2026-10-20**, so
  this report is published into the print. Consensus ~$1.99-2.01 adj EPS on
  ~$12.79-12.88B; standing FY26 guide from the 7/16 raise is adj EPS $7.65-7.85,
  op profit $10.55-10.75B, FCF $8.9-9.2B.
  — https://www.marketbeat.com/earnings/reports/2026-10-20-general-electric-stock/
- No Q3 8-K on EDGAR as of 06:10 ET (latest GE 8-K 2026-09-22), so the print
  was genuinely still pending when this was written.
- new since entry: 10/16 Turkish Airlines/CFM MOU for 600+ LEAP-1B engines.
  Negative: 10/19 defense names fell on midterm-driven spending worries.
- **conviction deliberately marked DOWN to 3**: GE has been published 6× in 10
  sessions. That is the anchoring signature, not conviction. Stop 292 is
  2.45 ATR below entry so the position is structurally sound; the instruction
  is to stop re-pitching it.

## [06:18 ET] POSITION UPDATE — SMMT — opened 2026-10-09 @ 17.10, now 15.57
- decision: HOLD, stop unchanged 14.40, trim ≥half into 2026-11-14
- **HARMONi PDUFA goal date 2026-11-14** (ivonescimab, EGFR-mut NSCLC) — the
  dominant event, ~3.5 weeks out.
- 10/19 +6.43% on 6.15M shares was an identified catalyst: global Phase II of
  ivonescimab regimens in advanced clear-cell RCC opened (SMT112-216 /
  NCT07877194, ~100 patients, vs nivo+ipi). The 10/16 low 14.56 held 16 cents
  above the 14.40 stop.
- **insiders: $103,616,650 of open-market buying, 3 distinct buyers, ZERO
  sells** in 6 months. Duggan and Zanganeh each 3,810,000 shares @ $13.12 on
  2026-06-12. Strongest positioning signal in today's report.
- AstraZeneca completed a ~$2B equity investment 2026-10-05; AZ/Daiichi Sankyo
  Datroway + ivonescimab collaboration 2026-10-02.
- stop discipline note: 14.40 is **2.74 ATR** below entry on today's ATR
  (0.9849) — compliant. This is the test CEG fails at 1.29 ATR, and the
  difference is why one is held and the other closed.
- action: captured, conviction 5, size cut to 1.5% because the PDUFA is binary
  and no stop placement survives a CRL gap.

## [06:19 ET] CALENDAR — FOMC verified
**2026-10-27/28, decision 2:00pm ET on day two. There is NO November meeting**
(next is 2026-12-08/09). Verified against the Chicago Fed's published Federal
Reserve calendars, and corroborated by its listed 2026-10-17 to 10-29
communications blackout bracketing the same dates.
— https://www.chicagofed.org/utilities/about-us/federal-reserve-calendars
NOT USED: a third-party tracker's claim of a 3.75-4.00% target range and a
+25bp hike on 2026-09-16 — could not be confirmed against a Fed source and
conflicts with other results, so no recommendation rests on it.

## [06:20 ET] POSITION UPDATE — XLE — opened 2026-08-15 @ 63.9, now 67.80 (+6.1%)
- decision: **RAISE STOP 60.80 → 65.40**. Trim half at 68.50. No new entry.
- why: the 60.80 stop was set 65 sessions ago and now sits 10.3% below market,
  turning a realised +6.1% into a potential -4.9%. 65.40 is below the 10/15
  swing low (66.17), 1.83 ATR under spot on ATR14 1.3129 (clears the 1.8 ATR
  ETF floor), and banks a worst case of +2.3%.
- leadership measured, not assumed: XLE +5.43%/+15.90%/+23.12% on 1m/3m/6m vs
  SPY +0.63%/+2.43%/+7.93% — outperforming on all three windows.
- only 2.70 points of upside remain to the 70.5 target vs 2.40 newly protected
  — ~1.1:1 from here, which is why protecting beats holding out.
- caveat in the thesis: the last 3 points are a Hormuz headline premium, not a
  change in production economics.

## [06:21 ET] POSITION UPDATE — TLT — opened 2026-09-24 @ 79.9 short, now 79.46
- decision: HOLD, levels unchanged (target 75.7, stop 82.0)
- why: this is the one position whose driver actually moved Monday — 10y to
  5.14-5.15%, 30y near 2002 highs. Stop 82.0 = 2.52 ATR above entry on ATR
  0.832 (ETF floor 1.8) ✓. R:R exactly 2.0.
- dated catalyst now in range: FOMC 10/28, and no second meeting until 12/09.
- noted honestly: target 75.7 is BELOW the 76.43 120-day low, so the trade needs
  new lows, not continuation. Half-trim placed at 76.43 for that reason.

## [06:22 ET] POSITION UPDATE — KHC — opened 2026-09-20 @ 23.0, now 23.17 (+0.7%)
- decision: **CLOSE**. The thesis expired; the price did not move.
- why: pitched on the two-company separation. That work was **paused in
  February 2026** and this run found no restart; May 2026 company language still
  called timing and completion uncertain. What KHC actually did in September was
  change listing venue — EDGAR shows Form 25 + Form 8-A12B both filed
  2026-09-08 with an NYSE CERT 2026-09-09. No separation 8-K in the 2026 list.
- without the split there is no mechanism for the published 32.0 target, which
  is ~15.5x the $2.030-2.090 FY26 adj EPS guide vs 11.2x being paid.
- **sell side is the worst in the book: bullish share 3.7%** — 1 strong buy,
  0 buy, 17 hold, 7 sell, 2 strong sell as of 2026-10-01, down 3.4 points.
  Barclays cut PT to $25 on 2026-10-17.
- beats_last_4 = 4, but against a repeatedly reset bar — clearing a lowered bar
  is not improving.
- COULD NOT CONFIRM: the Nov 4 earnings date or a Nov 12 Investor Day. Both
  appeared only as estimates in secondary sources, so neither is used as a
  catalyst and the exit is not timed to them.

## [06:23 ET] POSITION UPDATE — IYR — opened 2026-09-02 @ 97.8 short, now 96.24
- decision: HOLD, levels unchanged (target 90.5, stop 100.4)
- why: real estate was the 2nd-worst S&P sector Monday at -1.16% on the rate
  move. Thesis driver confirmed. FOMC 10/28 is the dated event.
- flagged: stop 100.4 is **1.88 ATR** above entry (ETF floor 1.8) — the
  thinnest cushion in the book, clearing by 0.08 ATR.
- **PORTFOLIO COHERENCE NOTE (the most useful thing found today):** the book
  held rate-sensitive LONGS (CEG, KHC) alongside rate-sensitive SHORTS (IYR,
  TLT) — a view hedged against itself. Closing CEG and KHC leaves the rate view
  expressed once, in two instruments, inside the 3-idea correlation cap.

## [06:24 ET] POSITION UPDATE — AAL — unfilled short @ 13.35 (published 2026-10-03)
- decision: **STAND DOWN**. Level left at 13.35; do not chase lower.
- why: the thesis worked and we were never paid — AAL is 11.68, **12.5% below**
  the short entry, so entry now needs a 14.3% rally. What remains is the bad
  half: shorting a name 37.84% off its high and 4.57% off its 120-day low, two
  sessions before a print the street models at -$0.36/sh.
- a lowered entry is explicitly refused: at 11.68 a 2.0-ATR-compliant stop
  (ATR 0.4441) sits near 12.80, above the 12.89 20-day and inside the 10/16
  range — hit by an ordinary bounce.
- conviction 2, lottery size, thinness stated: no filing read, no insider data,
  and **nasdaq short interest timed out twice** so days-to-cover is unmeasured.

## [06:25 ET] REJECTED — crypto (BTC/ETH/SOL) — no levels obtainable
Spot did fetch: BTC **81,442 (-1.63% 24h)**, ETH **2,383.53 (-2.14%)**,
SOL **103.97 (-1.41%)** — source coingecko via market_data.py crypto. A short
/MBT on rising real yields is a coherent and genuinely uncovered lane (1 crypto
idea tracked, 0 closed). **Not captured**: `history BTC-USD` failed on every
source (nasdaq no rows, yahoo 429, twelvedata/alphavantage no api key, stooq no
rows), so there is no ATR and no swing structure, and a futures idea needs a
stop clearing 2.5 ATR. Setting levels off a single spot print would be
fabrication. Recorded as a coverage gap instead.

## [06:25 ET] REJECTED — short gold — driver conflict, not a level problem
Rising real yields is the cleanest bearish input for gold and gold eased 0.50%
to $4,160.10 (Dec futures). Rejected anyway: the same session's Houthi strikes
on Saudi targets and Hormuz shipping attacks are a gold-POSITIVE shock, so the
two drivers of the trade point opposite ways. It would also have been the third
idea on the rates driver, at the correlation cap. The unfilled GLD SELL @
406.77 is left as published, untouched.

## [06:30 ET] DATA QUALITY — the fetched earnings calendar is INCOMPLETE
`market_data.py earnings` (finnhub) returned 1,356 names but **does not carry
GE, FCX, NEM, NUE, HII, BCC, SNX, DG, LULU or XLF** at any horizon tested
(12 and 20 days). GE is confirmed by two other sources to report pre-open
2026-10-20, and it is absent. **Consequence, applied throughout today's work:
presence on that calendar is reliable evidence of a date; absence from it is
evidence of nothing.** Dates used as `dated_catalyst` today are limited to
names the calendar actually carries (UNP 10/22, ABT 10/21, AAL 10/22, CVS 11/04,
PFE 11/03) plus the Chicago Fed FOMC calendar.
- **FCX earnings date: UNVERIFIABLE.** Sources give 10/15 (TipRanks,
  "confirmed" but self-described as an estimate), 10/21 and 10/15
  (MarketScreener, both "projected"), 10/22 (MarketBeat, estimated), 10/23
  (AJ Bell, with an inconsistent 11/18 call date) and 10/27 (the news sweep).
  None official. **No FCX date is claimed in any candidate.**
- Same treatment for HII (10/29 reported) and BCC (11/02 reported) — held as
  unverified, and the key_risk on each says the position may be carrying an
  unflagged print.

## [06:37 ET] SYSTEMATIC STOP-DISTANCE AUDIT — the highest-value finding today
Recomputed every open position's stop against **today's** ATR14 and the
asset-class floor from config/strategy.md. This caught three failures that no
amount of news reading would have surfaced, and in two of the three the
published reward-to-risk was clearing the 2.0 floor *only because* the stop was
too tight — the exact failure mode CLAUDE.md describes.

| Sym | close | ATR14 | ATR% | stop in ATR | floor | verdict | R:R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CEG | 263.19 | 17.099 | 6.50% | **1.29** | 2.0 | **FAIL** | 1.66 re-cut |
| SNX | 248.57 | 9.722 | 3.91% | **1.80** | 2.0 | **FAIL** | 1.86 re-cut |
| FCX | 69.75 | 2.606 | 3.74% | **1.86** | 2.0 | **FAIL** | 1.94 re-cut |
| IYR | 96.24 | 1.386 | 1.44% | 1.88 | 1.8 | pass by 0.08 | 2.81 |
| XLF | 55.06 | 0.686 | 1.25% | 2.08 | 1.8 | pass | 2.36 |
| NKE | 37.21 | 1.220 | 3.28% | 2.13 | 2.0 | pass | 2.42 |
| DG | 133.27 | 3.836 | 2.88% | 2.32 | 2.0 | pass | 2.30 |
| UNP | 287.01 | 4.265 | 1.49% | 2.63 | 2.0 | pass | 2.45 |
| GE | 311.28 | 6.535 | 2.10% | 2.45 | 2.0 | pass | 2.06 |
| SMMT | 15.57 | 0.985 | 6.33% | 2.74 | 2.0 | pass | 2.19 |
| STLD | 245.17 | 6.796 | 2.77% | 2.46 | 2.0 | pass | 2.12 |
| TLT | 79.46 | 0.832 | 1.05% | 2.52 | 1.8 | pass | 2.00 |
| LULU | 97.76 | 3.060 | 3.13% | 3.72 | 2.0 | pass | 2.07 |
| CVS | 92.68 | 2.226 | 2.40% | 3.41 | 2.0 | pass | 2.33 |
| BCC, PFE, HII | — | — | — | no stop (long_term) | n/a | see below | — |

Resolution of the three failures, applying the strategy.md rule "widen the stop
and re-check the ratio, or drop the idea":
- **CEG → CLOSE.** 1.29 ATR; honest re-cut gives 1.66 R:R. No catalyst before
  11/09 and the PJM backstop auction is suspended to 2026-02-28.
- **SNX → CLOSE.** 1.80 ATR; honest re-cut gives 1.86 R:R. Below both MAs and
  no FQ4 date announced — next catalyst ~3 months out.
- **FCX → WIDEN to 62.90 (2.03 ATR), no add, wind down.** Honest R:R 1.94, just
  under floor. Kept rather than closed because the tape is chopping, not
  trending down, and the only in-window analyst action was a raise.
- **IYR** passes by 0.08 ATR — the thinnest cushion in the book, flagged in its
  key_risk rather than silently accepted.

## [06:40 ET] LONG-TERM POSITIONS — all three were missing a required bear case
config/strategy.md makes a priced downside mandatory on `long_term`. BCC, PFE
and HII all carried `stop: None` and no `bear_case_price`. Anchors supplied from
measured 120-day lows, and the audit turned up a second pattern:
- **PFE** — bear 23.62 (range low), R:R **3.62** vs the 2.5 floor. Clean. The
  actionable correction is the add zone: at 29.44 PFE is 1.5% off its range
  high and above both MAs, the worst point in the position's history to add.
- **HII** — bear 230.00. The published **430 target is 26% above the most
  bullish published target found** (TD Cowen $340; Bernstein $307, both cut in
  October). Working target cut to 340, 430 demoted to target_2; R:R 2.44,
  marginally under the 2.5 floor and reported rather than nudged.
- **BCC** — bear 65.00 (range low), R:R 2.91 — but **only because the 110
  target is 29% above the highest published target** ($85 Goldman, cut from
  $91; BofA cut $89→$80). Conviction cut to 2, size to 1% lottery, target
  flagged UNVERIFIED for the red team. Against a defensible ~88 target the R:R
  is ~1.0 and the idea would not qualify.

## [06:42 ET] REVIEWED, HELD UNCHANGED, NOT RE-PITCHED (4 positions)
These passed the stop audit and had **no new information** in the 2026-10-16 to
10-20 window, so they are deliberately **not** captured as candidates —
re-pitching a position with nothing new is the padding strategy.md forbids, and
all four are already tracked. Recording them here so synthesis can say they
were reviewed:
- `DG` 133.27, stop 2.32 ATR, R:R 2.30, above both MAs. Latest item is a Gordon
  Haskett upgrade ~10/07, outside the window. Earnings Dec 3.
- `NKE` SELL 37.21, stop 2.13 ATR, R:R 2.42. 10/16 was a commentary cluster, no
  corporate event; reported 10/01. Short thesis intact.
- `XLF` 55.06, stop 2.08 ATR, R:R 2.36. Banks fell with yields Monday; no
  position-level change. Already published 4× in 10 days — no re-pitch.
- `CVS` 92.68, stop 3.41 ATR (widest in the book), R:R 2.33, above both MAs.
  Earnings **2026-11-04 confirmed on the fetched calendar**, EPS est 1.6596.
  The $315M DOJ opioid settlement (~10/14-15) predates the position's entry.
Untouched awaiting-entry items, left exactly as published: `VST` @132.0,
`GLD` SELL @406.77, `OXY` @54.0, `KXCPIYOY-26SEP-T3.5` NO @18, `ITB` @89.8.

## [06:43 ET] TRACK RECORD — how it was applied, without over-fitting
23 closed trades, 3/23 at target (13%), avg -5.4%. That is just past the ~15
threshold, so it was used to set the bar, not to pick sectors:
- **Conviction 3 is where the damage is**: 1/14 (7%), avg -6.5%, n=33 — and
  conviction 4 is 2/3 (67%), avg +5.8%. So nothing was captured today on two
  evidence kinds that could have carried three, and nothing was inflated to
  reach four: GE and LULU are held *down* at 3 deliberately, BCC cut to 2.
- **Conviction 2: 0/6, avg -8.4%.** Only two conviction-2 entries today (AAL
  stand-down, BCC) and both are sized ≤1% with the thinness stated.
- **long_term: 0/4, avg -15.2%** on n=9 — too small to act on as a category,
  but it is consistent with what the audit found independently: all three
  long-term positions had no priced downside and two had undefended targets.
  That is a process failure, which is fixable, rather than evidence the horizon
  does not work.
- Five recent stop-outs (MU, CAG, XLU, GDX, DAL) — four of five were
  conviction 3. Reinforces the above.

## [06:44 ET] RESEARCH COMPLETE
- candidates: **18** (16 distinct symbols; CEG captured twice, second entry is
  the one to use)
- shape of the day: **this is a position-management report, and that is stated
  rather than disguised.** 18 of 18 candidates concern the existing 19-position
  book or its 7 unfilled orders. **Zero new ideas were opened**, deliberately:
  with 19 open positions, a 13% hit rate, a correlation cap of 3 per driver
  already reached on rates, and three positions failing their stop floor, the
  honest use of today's budget was fixing the book rather than adding to it.
  strategy.md says publish fewer and note the skew — noted.
- **actions that are not holds** (the parts a reader must act on today):
  CLOSE `CEG`, CLOSE `KHC`, CLOSE `SNX`; RAISE STOP `XLE` 60.80→65.40;
  WIDEN STOP `FCX` 63.35→62.90; STAND DOWN `AAL`; WAIT on `ABT` until after
  tomorrow's print; HII target 430→340; BCC conviction 4→2 and size→1%.
- **GE reports pre-open TODAY** — the report is published into that print and
  says so.
- coverage gaps:
  - **No index, VIX, rates, DXY, gold or oil quote from our own feed** — every
    Yahoo-backed series returned HTTP 429 at 06:01 ET. Macro figures in this
    log are web-sourced with URLs; three supporting pages were snippet-only
    (HTTP 403): CappNotes, cnttrading Substack, Constellation IR.
  - **Event contracts: ZERO markets returned.** `events "Fed"`, `events "CPI"`
    and `events "recession"` all came back `ok: true, count: 0`. An actively
    wanted lane produced nothing and no event-contract idea was captured. The
    unfilled `KXCPIYOY-26SEP-T3.5` NO @18 is left as published.
  - **Crypto levels unobtainable.** Spot fetched (BTC 81,442 -1.63%, ETH
    2,383.53 -2.14%, SOL 103.97 -1.41%) but `history BTC-USD` failed on all
    five sources, so no ATR and no /MBT short could be levelled honestly.
  - **Short interest unavailable all run** — `short AAL` ×2, `short LULU`,
    `short SMMT` all `ReadTimeout` on api.nasdaq.com. Days-to-cover is
    unmeasured, which matters most for the two short positions (LULU, NKE) and
    the AAL stand-down, and is named in each key_risk.
  - **Options-implied move unavailable** — `implied UNP` returned HTTP 401
    (yahoo-options). No idea today was checked against what options price.
  - Not reached: small/micro-cap hunting, and the 4 awaiting-entry items left
    untouched above.
- sources that failed: yahoo (429 on all quotes/history, 401 on options),
  api.nasdaq.com short interest (repeated ReadTimeout), finnhub index quotes
  (CFD subscription required), kalshi events (0 results), stooq, twelvedata and
  alphavantage (no api key).

## [06:36 ET] EVENT CONTRACTS — the lane is NOT empty; `market_data.py events` is broken
Earlier this run `events "Fed"`, `events "CPI"` and `events "recession"` each
returned `ok: true, count: 0`, which read as "Kalshi has no macro markets." That
conclusion was wrong and the earlier gap note is superseded. Two separate bugs
in `scripts/market_data.py events()` (lines ~752-790):

1. **The query is not scoped.** It requests `status=open&limit=200` with *no*
   `series_ticker` and filters the returned page client-side. Kalshi returns an
   arbitrary page, which this morning was almost entirely sports parlays
   (`KXMVECROSSCATEGORY-*`), so every macro needle matched nothing. Calling the
   same endpoint with `series_ticker=KXFEDDECISION` returns 55 markets; with
   `KXCPIYOY`, 25; with `KXFED`, 25.
2. **It reads price fields that are now always null.** On the list endpoint
   `yes_bid`, `yes_ask`, `last_price`, `volume` and `open_interest` all come
   back `None`. The live values are under new names —
   `last_price_dollars`, `previous_yes_bid_dollars`, `previous_yes_ask_dollars`,
   `no_bid_dollars`, `no_ask_dollars`, `open_interest_fp` — and are populated on
   the single-market endpoint `/markets/<ticker>`.

Fix is a config-shaped change to the fetch, not to the thesis logic. Worth a
test in `tests/` per CLAUDE.md before next run.

## [06:38 ET] CALENDAR — market-implied FOMC distribution for 2026-10-28
Fetched per-market from the Kalshi API, series `KXFEDDECISION-26OCT`, close
2026-10-28T17:59:00Z. Mutually exclusive outcomes (cents = implied probability):

| Outcome | Last | Open interest |
| --- | --- | --- |
| Hike >25bp | 1c | 912,342 |
| Hike 25bp | **13c** | 1,457,131 |
| **Hold ("Fed maintains rate")** | **86c** | 1,941,894 |
| Cut 25bp | **1c** | 1,310,818 |
| Cut >25bp | 1c | 231,301 |

Sums to 102c, the normal bid/ask artifact. `rules_primary` on the hold leg:
"If the Federal Reserve does a Hike of 0bps on October 28, 2026, then the
market resolves to Yes."
— https://api.elections.kalshi.com/trade-api/v2/markets/KXFEDDECISION-26OCT-H0

**Why this mattered to today's report:** the distribution is skewed toward
tightening — a hike is priced at 13% against a cut at 1%. The main
counter-argument against both rate shorts was "a dovish surprise squeezes you,"
and that catalyst is now answered with a priced number rather than an opinion.
`TLT` and `IYR` were both re-captured with it as a fourth evidence kind,
conviction 4 → 5 on each. This is also the only genuinely *new* analytical
input found after the 70% mark.

## [06:39 ET] REJECTED — Fed-decision event contract — no probability disagreement
Having finally got prices, the honest answer is that there is no trade here.
Hold at 86c with ~1.9M open interest into a Fed already in its 2026-10-17/29
blackout — no new guidance can arrive before the decision — is a well-priced
market on which I hold no information advantage, and config/universe.md requires
an explicit probability disagreement, not a filled lane. Buying the 13c hike
tail was considered and rejected: my rates evidence is about the *long end*
(10y 5.14-5.15%, 30y near 2002 highs), which is term premium, and that is not a
reason the Fed moves the policy rate in eight days. **Capturing an event
contract merely because the lane was empty would be padding.** The unfilled
`KXCPIYOY-26SEP-T3.5` NO @18 is left as published, untouched.

## [06:45 ET] SELF-VERIFICATION PASS — recomputed every captured candidate
Re-derived R:R, stop-distance-in-ATR, and conviction-vs-evidence-kinds for all
20 lines (17 distinct symbols; `CEG`, `TLT` and `IYR` appear twice — **the
second entry of each is the one to use**). Three things to hand to the red team:

**1. `XLE` — read the stop against SPOT, not entry.** My audit script flagged
the new 65.40 stop as 1.14 ATR and FAIL. That is an artifact: 65.40 is *above*
the 63.90 entry, so on a long there is no risk to measure from entry and the
ratio is meaningless. Measured from the 67.80 close — the only meaningful
reference for a profit-protecting stop — it is **1.83 ATR, compliant** with the
1.8 ETF floor. `risk_reward` is deliberately `null` for the same reason: a stop
above entry has no loss case. Expect validation to flag this; it is understood,
not an oversight.

**2. Two ideas are knowingly published below their R:R floor**, disclosed in
their own thesis text rather than fixed by nudging a number:
- `FCX` **1.94** vs the 2.0 swing floor — after widening the stop to the
  compliant 2.03 ATR. Marked no-add / wind-down.
- `HII` **2.44** vs the 2.5 long_term floor — after cutting the target from the
  undefended 430 to the defensible 340. Demotion to the watchlist is the
  correct outcome if enforcement takes it.

**3. Four convictions sit BELOW their mechanically supported score.** Every
deviation is downward — nothing is inflated — and each has a stated reason:
- `AAL` 2 (kinds=2, supports 3) — the entry is a cancellation, not a position.
- `BCC` 2 (kinds=2, supports 3) — the 110 target has no defended valuation.
- `HII` 3 (kinds=3, supports 4) — target was undefended and had to be cut.
- `PFE` 3 (kinds=3, supports 4) — see the caveat below.
- `GE` 3 (kinds=2, supports 3) — matches; the markdown is already baked in.

**Caveat on `valuation_anchor` across the long_term ideas, and it is the real
weakness in today's work.** For `PFE`, `BCC`, `SNX` and `HII` the anchor I
supplied is a *measured 120-day range low*, not a defended valuation with a
method shown, which is what config/strategy.md actually asks for. It is an
honest floor, but it is closer to a `technical_level` than to a valuation. That
is why `PFE` and `HII` are left at 3 rather than raised to the mechanical 4:
counting a range low as a valuation anchor is how a thin long-term idea comes to
look researched. **The fix is filing work that this run did not have time for**,
and it is the single highest-value thing for the next run to pick up — the
long_term lane is 0/4 with avg -15.2%, and undefended targets are the most
likely reason.

Everything else: R:R and stop-ATR recomputed and consistent with what each
candidate claims; all four exit instructions (`CEG`, `KHC`, `SNX`, plus the
`AAL` stand-down) carry null target/stop by design.

## [06:46 ET] RESEARCH COMPLETE (supersedes the 06:44 block)
- candidates: **20 lines, 17 distinct symbols** (`CEG`, `TLT`, `IYR` re-captured
  once each with stronger evidence — take the last entry per symbol)
- shape: **a position-management report, stated rather than disguised.** All 17
  concern the existing 19-position book or its 7 unfilled orders. **Zero new
  ideas opened, deliberately** — with 19 open positions, a 13% hit rate, the
  rates correlation cap already at 2 of 3, and three positions failing their
  stop floor, the honest use of the budget was fixing the book, not adding to
  it. strategy.md says publish fewer and note the skew; noted.
- **actions a reader must take today:** CLOSE `CEG`, CLOSE `KHC`, CLOSE `SNX`;
  RAISE STOP `XLE` 60.80→65.40; WIDEN STOP `FCX` 63.35→62.90; STAND DOWN `AAL`;
  WAIT on `ABT` until after tomorrow's 10/21 print; `HII` target 430→340;
  `BCC` conviction→2 and size→1%. The other eight are holds.
- **`GE` reports pre-open TODAY** — this report is published into that print and
  says so. `STLD` already reported after Monday's close and **no post-print
  price was obtainable**, so its hold is stated against a 850-minute-old quote.
- coverage gaps, final:
  - **No index/VIX/rates/DXY/gold/oil quote from our own feed** — all
    Yahoo-backed series HTTP 429 at 06:01 ET. Macro figures are web-sourced
    with URLs; three supporting pages were snippet-only (403).
  - **`market_data.py events` is broken, not the market** — see the 06:36 entry.
    Macro series exist and are priced; the helper mis-scopes the query and reads
    retired field names. Needs a fix plus a test before the next run.
  - **Crypto levels unobtainable** — spot fetched (BTC 81,442, ETH 2,383.53,
    SOL 103.97) but `history BTC-USD` failed on all five sources, so no /MBT
    short could be levelled. Uncovered lane, 0 closed trades.
  - **Short interest unavailable all run** — api.nasdaq.com ReadTimeout ×4
    (AAL ×2, LULU, SMMT). Days-to-cover unmeasured; named in the key_risk of
    `LULU`, `NKE` and `AAL`.
  - **Options-implied move unavailable** — `implied UNP` HTTP 401. No idea today
    was checked against what options price.
  - **Earnings calendar incomplete** — missing GE, FCX, NEM, NUE, HII, BCC, SNX,
    DG, LULU, XLF. Presence is evidence; absence is not. FCX's date could not be
    pinned at all (five conflicting sources) and none is claimed.
  - Not reached: small/micro-cap hunting, and defended valuations for the four
    long_term positions (see 06:45).
- sources that failed: yahoo (429 quotes/history, 401 options), api.nasdaq.com
  short interest (ReadTimeout ×4), finnhub index quotes (CFD subscription),
  kalshi via our helper (0 results — helper bug, not the venue), stooq,
  twelvedata, alphavantage (no api key).
