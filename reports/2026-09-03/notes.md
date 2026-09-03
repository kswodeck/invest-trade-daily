# Research log — 2026-09-03

## [06:03 ET] MACRO — rates, tape, crypto
- FRED 2026-09-01: US10Y 4.79% (prev 4.75), US2Y 4.39% (prev 4.34), fed funds eff 3.63%, 10y-2y +0.40 (2026-09-02). Long end backing up while the curve holds — bear steepening at the margin. — source: https://fred.stlouisfed.org/series/DGS10
- Unemployment 4.1% (Jul, prev 4.2). CPIAUCSL 332.813 (Jul).
- Prior close 2026-09-02 (finnhub, session=pre, age ~843 min — previous close, market shut, NOT stale):
  SPY 765.16 (+0.44%), QQQ 709.24 (+0.23%), IWM 294.01 (+1.18%), GLD 402.78 (+1.52%), TLT 81.95 (+0.10%).
  Small caps led, gold ripped +1.5% to a new high area — that combination with a rising 10y is a
  debasement/steepener tape, not a growth tape.
- Crypto 06:02 ET (coingecko): BTC 77,589 (+1.17% 24h), ETH 2,392.95 (+0.79%), SOL 100.14 (+1.58%).
- DATA GAP: yahoo is returning HTTP 429 across the board, so ^GSPC/^NDX/^VIX/DXY/WTI/ES/NQ all failed.
  No VIX, no dollar index, no crude print this morning. finnhub covers ETFs/equities fine.

## [06:04 ET] CALENDAR — dated catalysts inside 10 sessions (finnhub earnings calendar)
- 2026-09-03 AMC: **LULU** (est EPS 1.83, rev 2.51B) — this is an OPEN POSITION. Also ZS, DOCU, IOT, GWRE, PATH, ASAN, NX.
- 2026-09-03 BMO: CPB, CIEN, TTC, MOMO, ZGN, BRC, WLY, LE.
- 2026-09-07: GME, DBI. 2026-09-08: UNFI (bmo), CASY (amc), ABM, OXM, BRZE, TTAN.
- 2026-09-09: KR, CHWY (bmo), ASO, SIG, AEO (amc), RH, AVAV, COO, CNM.
- 2026-09-10 AMC: **ADBE** (est EPS 6.20, rev 6.82B), CPRT.

## [06:06 ET] POSITION UPDATE — LULU — opened 2026-08-22 @ 115.00, last close 120.07, +4.4%
- decision: HOLD at size, do not add, do not trim. Q2 FY26 prints TONIGHT 2026-09-03 amc (confirmed on
  today's fetched finnhub calendar; est EPS 1.8304, rev 2.507bn).
- analysts fetched today: 1 strong buy / 1 buy vs 31 hold / 5 sell / 2 strong sell. Bullish share 5.0%,
  -15.5pts since June. revision_direction "deteriorating". Q2 FY26 surprise record: -1.49% (Jun qtr).
- price: close 120.07, ATR14 4.5555 (3.79%), sma20 120.463, sma50 118.4571, 150d range 104.44-148.69,
  $384M/day dollar volume. Coiled between the 20 and 50 day into the print.
- action: captured via add_candidate.py, wait=true, add zone 104-114 POST-PRINT ONLY.

## [06:07 ET] POSITION UPDATE — SVRA — opened 2026-08-23 @ 5.35, last close 5.46, +2.1%
- decision: HOLD, no change to levels. Nothing happened. PDUFA for MOLBREEVI still 2026-11-22, 80 days out.
- price: close 5.46, ATR14 0.1996 (3.66%), sma20 5.5195, sma50 5.6708. Stop 4.60 sits 4.3 ATR below —
  wide enough for a 3.7% daily range name. Range 4.695-6.475, off high -15.7%.
- no new information, so no re-pitch. Not re-captured; the tracked position stands as published.

## [06:08 ET] MACRO — the regime is a hawkish Fed with a weak labour market
- Fed Chair **Kevin Warsh**, Jackson Hole 2026-08-28: inflation "more concerning" than the job market,
  said the Fed may have "work to do" and that inflation is unlikely to return to target on its own.
  CME FedWatch September hike probability jumped to **55.7%**, ~20pts higher in a day.
  — source: https://www.federalreserve.gov/newsevents/speech/warsh20260828a.htm , https://www.cnbc.com/2026/08/28/kevin-warsh-jackson-hole-federal-reserve-inflation.html
- **The jobs-report reaction function is inverted.** Through 2024-25 a weak payroll meant cuts; under
  Warsh a STRONG August print is hawkish and a soft one lowers hike odds. — source: https://www.top1markets.com/news/august-2026-jobs-report-nfp-preview
- **NFP Friday 2026-09-04 08:30 ET** — consensus +50-58K, u-rate 4.1%, AHE +0.2% m/m / +3.0% y/y.
  July actual was **-23K** against +83K expected, with May cut 66K and June 37K (103K of downward
  revisions), and participation 61.4%, lowest outside Covid since the mid-1970s.
  — source: https://www.bls.gov/news.release/empsit.nr0.htm
- **FOMC 2026-09-16.** Oil high-$80s WTI / low-$90s Brent on continuing Middle East skirmishes; yields
  ticking higher across 2s, 10s and 30s. — source: https://www.schwab.com/learn/story/stock-market-update-open
- ~~DATA GAP: Kalshi's public market endpoint returned null bid/ask/last for every KXFEDDECISION market,
  so I have no verifiable event-contract price and will not state one.~~ **SUPERSEDED at 06:17** — the
  `/markets` listing does return nulls, but the **`/markets/trades` endpoint works** and gives real last
  prints. Live prices were obtained and are in the 06:17 block below; this is NOT a data gap, and the
  Fed candidate captured today carries a fetched market price.
- The two Fed contracts already on the awaiting-entry list (KXFEDDECISION-26SEP-H25 YES @32 from 08-22,
  and -26OCT-H25 YES @28 from 09-02) were both priced BEFORE or around the Warsh repricing; with the
  September hike side now trading 52c, a 32c limit will not fill and should not be treated as live.
- DATA GAP: yahoo 429/401 all morning — no VIX, DXY, WTI, ES/NQ futures quotes, and the options
  `implied` subcommand is unavailable (401 on the options endpoint), so no options-implied-move checks today.

## [06:09 ET] SCREEN — dated catalysts inside 10 sessions, price context fetched
- CIEN reports TODAY bmo — close 354.16, ATR 23.79 (6.72%), -44.5% off the 637.51 high, eight sessions
  down from 418.72 on 08-27 to a 348.86 low on 09-02. REJECTED as an entry: a 6.7% ATR name printing in
  two hours is a coin flip, not a setup.
- AVAV 09-09 amc — close 145.39, **-52.5%** off the 306.00 high, sitting on the 150-day low (140.91).
- RH 09-09 — close 147.68, -34.9%, ATR 5.18%. Rate-sensitive furniture into a 4.79% 10y.
- ASO 09-09 bmo — close 43.60, -30.2%, at 150-day lows. SIG 09-09 amc — 81.73, -18.7%.
- KR 09-09 — close 58.22, -24.0% off high but ATR only 2.2%; the one defensive in the group.
- ADBE 09-10 amc — close 279.79, only -6.5% off its high after a 245.60 to 279.79 run off the 50-day.

## [06:11 ET] TAPE — 2026-09-02 close, verified
- Dow +295 to 53,061.95; S&P 500 7,666.60; Nasdaq 26,217.83. Small caps outperformed (IWM +1.18% vs
  SPY +0.44%), 9 of 11 sectors higher, ~60% of the index advancing.
- **WTI settled $91.01 (+0.88%), Brent $95.63 (+1.04%)**. CVX +2.4%, XOM +2.2%.
- **December gold settled $4,414.60 (+0.41%)**, spot quoted ~$4,455.
  — source: https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-sept-02-2026
- Cross-check on the GLD bear case: at GLD 402.78 against $4,414.60/oz the trust holds ~0.0912 oz per
  share, so the $3,600/oz bear case prices GLD at ~328 — the 330 used in the GLD candidate is right.

## [06:12 ET] REJECTED — with reasons
- **XLE** — close 65.10, a 150-day closing high, -0.37% off it, ATR 1.11 (1.71%). Crude at $91 is real,
  but an honest breakout stop below the base (62.10, under sma20 62.22 and the 08-26 low 61.31) is 3.01
  ATR of risk, and the 2.0 floor then demands a 72.15 target — +10.2% into blue sky with no prior level
  to point at. It only clears the floor with a stop walked in, which is exactly the failure mode the
  config forbids. Note separately: the awaiting-entry **XLE BUY @ 63.00** from 08-15 is now 3.2% BELOW
  market, so that order is a pullback bid on a breaking-out ETF, not a live setup.
- **XOP** — close 193.16, -0.86% off high, ATR 3.99 (2.07%). Same structure, marginally better: entry
  195 / stop 184 (2.76 ATR) / target 217 gives exactly 2.0. Rejected on two counts — the target needs
  Brent near $105 which I cannot underwrite, and with XLE @63 and DINO @99.5 already on the awaiting
  list a third energy long hits the correlation cap for one driver.
- **CIEN** — reports today bmo; 6.72% ATR into a print two hours away. Not a setup.
- **AVAV** — close 145.39 sitting on the 150-day low, -52.5% off the 306.00 high, earnings 09-09 amc.
  Rejected as a long: a material weakness in internal controls and an $89M goodwill restatement tied to
  the Space unit, FY26 net loss of $265M, FY27 guidance implying negative free cash flow with growth
  skewed to the back half, and an RBC downgrade to Sector Perform. Rejected as a short too: 85.7%
  analyst bullish share and improving revisions (10 SB / 14 B / 4 H) at the low is the wrong side to
  press. — source: https://www.tipranks.com/news/catalyst/aerovironment-stock-sinks-as-guidance-and-controls-bite
- **RH** — 147.68, -34.9%, earnings 09-09. Surprise record -11%, -23%, -33% before a +9.4% last quarter,
  and rate-sensitive furniture into a 4.79% 10-year is a bad long. Not shortable with conviction either:
  co-founder Carlos Alberini bought $1.83M open-market on 2026-06-29 at ~160, and short interest could
  not be fetched (nasdaq read timeout) so the squeeze risk is unmeasured. No trade.
- **SLV** — 59.07, -46.2% off the 109.83 high while gold prints records, which looks like a divergence.
  Rejected: SLV's oz-per-share is not something I could verify this morning, so any gold/silver ratio I
  quoted would be constructed rather than fetched, and it would be a third gold-correlated position.
- **KRE** — 74.24, below both the 20-day (75.51) and 50-day (75.60). The awaiting-entry **KRE BUY @ 76.80**
  from 08-15 needs a 3.4% rally to fill, and a Warsh hike flattens the front end that the thesis wanted
  steep. Standing that order down is the honest call; no new capture.
- **ASO** (43.60, at 150-day lows) and **SIG** (81.73) — discretionary retail into a hawkish Fed with
  5.2% and 3.6% ATRs. Same week, same driver, worse risk than KR. Passed over rather than rejected.

## [06:13 ET] POSITION UPDATE — RARE — SUPERSEDED, DO NOT USE
> **This entry was wrong and is retained only so the sequence is honest.** It was written before I
> checked the premarket board, concluded "no new filing or agency action found", and said HOLD. There
> WAS one — an 8-K filed 2026-09-02. See the 06:24 ET entry below, which replaces this in full. The
> decision is CLOSE, not hold. Nothing in this block should reach the report.
- ~~decision: HOLD, levels unchanged. Stop 22.90 is 2.98 ATR below the close (ATR14 1.2168).~~
- ~~UX111 PDUFA still 2026-09-19, now 16 days out. No new filing or agency action found this morning.~~
- Lesson for the log: I checked filings for IONS before I checked them for my own open position, and
  the fetched `filings RARE` call that would have surfaced the 8-K immediately was only run at 06:23.

## [06:17 ET] EVENT CONTRACTS — the Fed curve, priced from live Kalshi trades
Kalshi's `/markets` listing returns null bid/ask, but the **trades** endpoint works and gives real last
prints. Fetched 06:15-06:17 ET (times below are the trade timestamps, UTC):

| Meeting | Hold | Hike 25bp | Hike >25bp | Cut 25bp |
| --- | --- | --- | --- | --- |
| SEP (09-16) | **47c** (10:12:24Z) | **52c** (09:41:29Z) | 1c | 1c |
| OCT (10-28) | 69c | 28c | 2c | — |
| DEC (12-09) | 48c | 42c | 3c | — |

- SEP is the liquid one — both sides printed within the last hour. OCT and DEC last printed overnight or
  on 09-02, so treat those as indicative, not tradeable marks.
- The curve is priced for **one** hike, most likely September, with December the fallback.
- Robinhood carries this exact event ("Fed rate decision in September 2026"), verified against the RH
  prediction-markets URL, and its page displayed the hike side at 56%.
  — source: https://robinhood.com/us/en/prediction-markets/economics/events/fed-rate-decision-in-september-2026-sep-16-2026/
- Robinhood fees changed 2026-06-01 to a probability-weighted commission: 5% Gold, 10% standard. That is
  a real cost on a 47c entry and is not netted out of the levels.
- **Captured: KXFEDDECISION-26SEP-H0 YES @ 47.** The disagreement is 57 (mine) vs 47 (market), and it
  rests on Warsh's own conditioning language, read in the primary text: "Labor markets are quite stable.
  The jobless rate, at 4.1 percent, remains low by historical standards... I believe the labor markets
  are consistent with full employment." Against it, from the same speech: 12-month PCE 3.7%, six-month
  4.1%, "Otherwise, we have work to do", and an explicit refusal of forward guidance.
  — source: https://www.federalreserve.gov/newsevents/speech/warsh20260828a.htm
- **This reverses the 08-22 call.** The awaiting-entry KXFEDDECISION-26SEP-H25 YES @ 32 was priced six
  days before Warsh spoke; at a 52c market that bid cannot fill and it is now on the wrong side. Stand
  it down. The 26OCT-H25 YES @ 28 published 09-02 is at market (28c) and is NOT contradicted — a
  September hold makes an October hike more likely, not less, so leave that one live.

## [06:29 ET] WATCHLIST — IONS — good business, levels do not clear the floor
- Ionis Pharmaceuticals, $10.19B cap, 166.18M shares, TTM revenue $874.09M, 52w range 49.13-86.74.
  Close 61.33 (+2.42% on 09-02), ATR14 1.8654 (3.04%), sma20 59.231, sma50 62.0088, -29.3% off the high,
  $147M average daily dollar volume. — source: https://stockanalysis.com/stocks/ions/
- The case: **three dated catalysts inside two months** — zilganersen PDUFA (Alexander disease, Priority
  Review, first disease-modifying agent in the indication) **2026-09-22**; bepirovirsen PDUFA (chronic
  hep B, GSK-partnered) **2026-10-26**; pelacarsen HORIZON Lp(a) outcomes results expected in 2026.
- Fundamentals from the Q2 2026 release: revenue $268M, net loss $115M (H1 $207M), cash and short-term
  investments **$2.1B**. FY26 owned-product guidance TRYNGOLZA $100-110M and DAWNZERA $110-120M;
  WAINUA royalties $27M in H1. Management calls TRYNGOLZA the first Ionis-owned multi-billion-dollar
  medicine. — source: https://www.biospace.com/press-releases/ionis-reports-second-quarter-2026-financial-results-and-highlights-progress-on-key-programs
- **Insider buying:** CSO Michael R. Hayden bought 20,000 shares open-market for $1.06M on 07-30 and
  07-31 at 53.38 and 51.60 — near the low, ahead of the +11.4% month. One buyer only, against 60 sales.
- **Relative strength:** IONS -22.81% over 6 months against XBI +30.81% — a 34-point underperformance of
  its own sector — but +11.37% over the last month against XBI +8.88%. A lagger that has just turned.
- **Why it is NOT captured.** The target has to be a level I can point at. The only defensible one is the
  50% retracement of the 86.74-to-49.13 decline at **67.94**. Working backwards honestly: entry 60.00 at
  the tested 59.70-59.78 shelf with a stop at 55.60 below the 55.16/54.91 cluster gives 2.36 ATR of risk
  and **1.80:1** — under the 2.0 swing floor. Dropping the entry to the 20-day at 59.20 either puts the
  stop inside 2.0 ATR or makes the ratio worse (1.61 at a 53.80 stop). There is no combination that
  clears both floors without walking the stop in, so it goes on the watchlist rather than into the report.
  Revisit under 57, where the same 67.94 target does clear.
- DATA GAP: nasdaq returns only 20 bars in `recent` regardless of `--days`, so no mid-range resistance
  shelf between 64.19 and 86.74 could be identified — the retracement level is the best available.

## [06:30 ET] REJECTED / GAPS — additional
- **NUVL** (Nuvalent) — zidesamtinib PDUFA **2026-09-18**, a genuine dated catalyst 15 days out, but
  price history failed from every source (nasdaq returned no rows, yahoo 429) and the quote came back
  null. No levels means no candidate. Flagging for tomorrow.
  — source: https://www.marketbeat.com/fda-calendar/upcoming/
- **MRK** — I-DXd PDUFA 2026-10-10, outside the useful window for a swing and immaterial to a $200B+ cap.
- **Stale awaiting-entry orders that should be stood down**, noted for synthesis: `BTC SELL @ 63,400`
  (08-16) and `/MBTU6 SHORT @ 64,340` (08-18) both sit ~18% below a spot BTC of 77,589 this morning, so
  neither is a live order — they are bids on a breakdown that never came. `KRE BUY @ 76.80` needs a 3.4%
  rally to fill against a tape where it closed 74.24, below both its 20- and 50-day.

## [06:27 ET] CORRECTION — NUVL is not tradeable, and the FDA calendar that listed it is stale
- **Nuvalent (NUVL) was delisted on 2026-07-15** after GSK's $10.6B acquisition, tender offer at $124.00
  cash per share; last trade 123.96 on 2026-07-14. That is why every price source returned nothing for it
  this morning — not a data outage, a dead ticker.
  — source: https://stockanalysis.com/stocks/nuvl/
- MarketBeat's upcoming-PDUFA calendar still lists NUVL / zidesamtinib / 2026-09-18 as a live catalyst.
  It is not: the PDUFA may well still exist, but the equity expression of it does not. Treat that
  calendar as a lead source only, never as a tradeability check. This is exactly the case the universe
  config has in mind when it says to verify at runtime rather than from memory.
- Same source also lists MRK / I-DXd / 2026-10-10 (immaterial to a $200B+ cap) and RARE / UX111 /
  2026-09-19, which independently confirms the date on the open RARE position — that one is real.

## [06:26 ET] REJECTED — tankers, on price rather than thesis
- Crude tanker equities are all pinned at their 150-day highs: INSW 101.19 (-1.14% off high), FRO 45.42
  (-0.36%), DHT 20.07 (-2.67%), STNG 81.42 (-6.83%). The thesis is real — WTI settled $91.01 and Brent
  $95.63 on 09-02, and the war-risk/Hormuz disruption that drove VLCC Middle East-China rates to a record
  $423,736/day did so in **March 2026**, not this week.
- Rejected because I could not fetch a *current* VLCC spot rate from any source this morning, and buying
  a sector at its highs on a six-month-old rate spike is buying the news. Note for synthesis: the
  awaiting-entry **DHT BUY @ 19.10** (published four separate times) is now a pullback bid on a name
  sitting 2.7% off its high — the level is unchanged and still below market, so it is not stale in the
  way the BTC and KRE orders are, but four publications of one idea is the anchoring pattern the prior
  context warns about and it should not be published a fifth time without something new.
  — source: https://oilprice.com/Energy/Energy-General/Super-Tanker-Rates-Soar-Amid-Sanctions-Supply-Shifts-and-Strategic-Hoarding.html
- **DG** closed 130.89, up 6.5% in four sessions and through its 20- and 50-day (123.85 / 122.26). The
  awaiting-entry **DG BUY @ 121.00** is now 8% below market. Trade-down retail is the right regime call,
  but DG has been published 3× in ten days and has now run away from the level; not re-pitched.
- **CHWY** 24.17, ATR 0.93 (3.85%), earnings 09-09 bmo, above both its 20- and 50-day. Passed for the
  same reason as IONS: with nasdaq capped at 20 bars there is no identifiable resistance shelf between
  24.81 and the 30.95 high, so any target above 25 would be a number rather than a level.

## [06:24 ET] POSITION UPDATE — RARE — CLOSE. Phase 3 failure overnight, stop gapped through
**This replaces the 06:13 "hold" entry above, which was written before I saw the premarket board.**
- **Ultragenyx 8-K filed 2026-09-02**: the Phase 3 **Aspire** study of **apazunersen (GTX-102)** in
  **Angelman syndrome failed**. Read the filing directly: it "did not achieve the primary endpoint of
  change from Baseline in Bayley-4 cognitive raw score nor the key secondary endpoint of net response in
  Multidomain Responder Index", and "there were no differences between the treated and control groups
  that could support efficacy in the Bayley Cognition raw scores." Safety profile unchanged. The company
  will "evaluate the apazunersen program in light of this outcome" and "assess its planned operations to
  define and implement significant expense reductions."
  — source: https://www.sec.gov/Archives/edgar/data/1515673/000119312526380165/rare-20260902.htm
  — corroborated: https://www.statnews.com/2026/09/02/ultragenyx-drug-angelman-syndrome-clinical-trial/
- **RARE quoted 14.75 in the premarket, -44.40%**, the single largest decliner on the board.
  — source: https://stockanalysis.com/markets/premarket/
- Arithmetic on the open position: entry 25.20 on 08-31, prior close 26.53, stop 22.90. The gap is
  ~11.8 points against an ATR14 of 1.2168 — roughly **9.7 ATRs** — so the stop had no chance to execute.
  Realised loss at 14.75 is about **-41.5%** against a plan that risked -9.1%.
- decision: **SELL THE FULL POSITION AT THE OPEN.** Captured via add_candidate.py as direction `sell`,
  horizon `intraday`, explicitly an exit of the existing long rather than a short.
- why, in one line: the stop was gapped rather than hit, so holding from here is a new decision and it
  does not survive being made fresh — what remains is one binary (UX111 PDUFA 09-19) at a company that
  has simultaneously lost a Phase 3, already had setrusumab miss its primary fracture endpoint twice,
  and told the market it must cut expenses, with $294M of H1 operating cash burn behind it. The
  published key_risk on this position named an equity raise as the thing most likely to swamp the
  catalyst; this morning made that more likely, not less.
- the case against selling, stated honestly: the Angelman failure does not touch UX111's CMC review, so
  a 09-19 approval could rip from a 44% lower base and this exit would look like selling the low. That
  is being given up deliberately. If UX111 is genuinely mispriced at 14.75 it is a NEW trade, to be
  underwritten from flat at the post-gap price — not a reason to average a broken one.

## [06:26 ET] OPEN POSITIONS — filings re-checked after the RARE miss
- **SVRA**: most recent filings are an S-8 and the 10-Q, both 2026-08-11; last 8-K was 2026-06-08. No
  overnight news. The 06:07 HOLD stands.
- **LULU**: last 8-K 2026-08-13, last Form 4s 2026-06-29. Nothing since. The 06:06 HOLD-into-the-print
  stands; tonight's release will be the next 8-K.
- **GLD** is a trust, no company filings to check; the 06:06 amendment stands on price alone.

## [06:27 ET] WATCHLIST — SNOW — the fundamentals are there, the levels cannot be set today
- Snowflake reported Q2 FY27 on 2026-09-02 after the close and **gapped to 379.00 premarket, +23.92%**
  from a 305.84 close (it had fallen 4.4% into the print from a 319.80 prior close).
- The print: product revenue **$1.49B, +37% y/y**; total revenue +35%; net loss narrowed to $191.7M
  (-$0.55) from $297.9M (-$0.89). FY27 product revenue guidance **raised to $6.07B from $5.84B** in May;
  Q3 guided to $1.59B against $1.50B consensus; non-GAAP operating margin guided to **14.5% from 13.5%**.
  CoCo, the coding agent, at 9,100 accounts, +2,000 in the quarter.
  — source: https://www.cnbc.com/2026/09/02/snowflake-snow-q2-earnings-report-2027.html
  — source: https://www.sec.gov/Archives/edgar/data/1640147/000164014726000033/fy2027q2earnings.htm
- Context: 346.60M shares, $106.01B cap at the 305.84 close, TTM revenue $5.43B (+32%), 52-week range
  **118.30-341.95** — so the 379 premarket is above the 52-week high. ATR14 12.6849 (4.15%), sma20
  325.988, sma50 292.5088, $1.47B average daily dollar volume. — source: https://stockanalysis.com/stocks/snow/
- **Why it is NOT captured.** I worked the only structurally honest version: buy a pullback to 345, just
  above the 341.95 prior high that a successful breakaway gap should defend, stopping at 304.00 below
  the 303.89 low of 09-02 and the gap origin. That risk is 41.00, a comfortable 3.23 ATR, and the 2.0
  floor then demands a **427** target — $148B, or **24.4x** the raised FY27 product revenue guide,
  against 17.5x at last night's close. That is not a level, it is a 40% multiple expansion assumed into
  existence, and there is no price history above 341.95 to anchor it. Rejected on the target, not the
  business.
- Revisit once the post-gap range exists. If SNOW builds a base above 341.95 over the next week, the
  same stop becomes tighter in percentage terms and the arithmetic may work at an entry near 350-360.

## [06:27 ET] PREMARKET BOARD — context only, no trades taken
Movers fetched at 06:23 ET. Recorded because the RARE 8-K was found here, not because any is actionable.
- Losers: **RARE -44.40% @ 14.75** (acted on, above). ETD -10.89% @ 22.02 — furniture retail, the same
  rate-sensitive consumer the RH note rejects. BRTX, ADBT, WCT are sub-$2 and out of universe.
- Gainers: **SNOW +23.33%** (watchlisted, above). TLYS +29.66% @ 4.94 and DLTH +14.92% @ 4.16 are
  small-cap retail earnings reactions — both post-gap, both sub-$5, and neither has a settable stop
  before a post-gap range exists; the same objection that disqualified SNOW applies with less liquidity
  behind it. CHPT +17.92% @ 6.12. GIPR, GELS, MIMI, BTAI, GYGY are sub-$2 or micro and out of universe.
  — source: https://stockanalysis.com/markets/premarket/

## [06:29 ET] VALIDATION PRE-CHECK — arithmetic recomputed before handing off
Checked each capture against `scripts/validate_report.py` by hand rather than leaving it to phase 2b.
- **LULU** and **GLD** were first captured WITHOUT `bear_case_price`. Both are `long_term` with
  `stop: null`, and `check_risk_reward` falls back to `bear_case_price` when the stop is null — so as
  first written they would both have failed with "no bear_case_price, so risk is undefined" and been
  demoted. Re-captured with the numbers that were already argued in the text: LULU 88.00 (11x on 8.00 of
  EPS) giving **3.35:1** from the 108 add level, GLD 330.00 (~$3,600/oz) giving **2.78:1** from 375.
  Both clear the 2.5 long-term floor. Synthesis should take the LAST LULU and GLD lines.
- **KR** — entry 57.20, stop 53.90, target 65.40. Risk 3.30 = **2.58 ATR** on an ATR14 of 1.2794, which
  clears the 2.0 stock-swing floor and also the 2.5 "safe" guide. R:R **2.48:1** against the 2.0 floor.
  win_probability 0.38 against a 1/(1+2.48) = 28.7% baseline — a 9.3 point claimed edge, well inside the
  20 point level where a claim starts needing extraordinary support.
- **KXFEDDECISION-26SEP-H0** — entry 47, stop 30, target 100 gives 3.12:1. Expect two soft flags and
  neither is a defect: `stop_distance` will WARN because a Kalshi ticker has no fetchable ATR, and
  `check_expectancy` will show a 32.7 point gap between the claimed 57% and the 24.3% random-walk
  baseline. That gap is structural — a binary contract is not a random walk, so `1/(1+R:R)` is not its
  break-even. The real claim is 57 against a market price of 47: **ten points**, stated in the
  counter_argument so it is not read as a bigger assertion than it is.
- **RARE** — a close instruction, so `target` and `stop` are null by design and both
  `direction_consistency` and `risk_reward` will FAIL on missing fields. Flagged inside the thesis so
  the red team does not demote the most time-sensitive line in the report on a shape problem. The
  defended downside (~11.20, the commercial business at ~1.5x the 730-760m 2026 revenue guide) is stated
  in the text rather than in `bear_case_price`, because on a `sell` the schema requires the downside
  field to sit ABOVE the entry and 11.20 would have produced a misleading direction failure.

## [06:30 ET] CORRELATION CHECK — the cap is reached, do not add a fourth macro idea
Five captures, four distinct drivers:
- **LULU** — company-specific, tonight's guidance sentence. Uncorrelated with the rest.
- **RARE** — company-specific, an exit forced by a Phase 3 failure. Uncorrelated.
- **GLD**, **KR**, **KXFEDDECISION-26SEP-H0** — all three lean on the same complex: sticky inflation,
  a hawkish Warsh Fed and the September rate path. That is **exactly the 3-idea correlation cap** from
  `config/strategy.md`. They are not identical bets — GLD wins on debasement whatever the Fed does, KR
  wins on the stagflation consumer, and the event contract wins specifically if the Fed does NOT hike,
  so the Fed contract is partly a hedge on the other two rather than a third helping. But synthesis must
  not add a fourth idea driven by rates, the dollar or the September FOMC, and this is why XLE, XOP and
  a TLT re-pitch were all left out.

## [06:31 ET] RESEARCH COMPLETE
- **candidates: 5 distinct symbols** across 8 written lines (LULU, GLD and RARE were each re-captured to
  fix a field; take the last line per symbol).
  1. `RARE` **SELL — close the position at the open.** Phase 3 Angelman failure, stop gapped by ~9.5 ATR.
  2. `LULU` buy / long_term — HOLD into tonight's print, add zone 104-114 post-print only. wait=true.
  3. `GLD` buy / long_term — HOLD; add rungs amended down to 392 and 375, no adds at 402. wait=true.
  4. `KR` buy / swing — new idea, entry 57.20, stop 53.90, target 65.40, 2.48:1.
  5. `KXFEDDECISION-26SEP-H0` yes / swing — new idea, 47c, my 57% vs the market's 47%.
- **Also decided, deliberately not captured:** SVRA hold unchanged (no news, filings re-checked).
- **Watchlist material written up in full**: IONS (three dated catalysts, CSO insider buying, 34-point
  6-month lag to XBI — fails both stop and R:R floors at any honest level combination; revisit under 57)
  and SNOW (guidance raised, gapped +24% above its 52-week high — no post-gap structure to set a stop
  against; revisit if it bases above 341.95).
- **Rejected with reasons logged**: XLE, XOP, CIEN, AVAV, RH, SLV, KRE, ASO, SIG, CHWY, DG, INSW, FRO,
  STNG, DHT, MRK, and NUVL — the last because it was **delisted 2026-07-15** in GSK's $10.6B takeout,
  which the FDA calendar that surfaced it still had listed as a live catalyst.
- **Stale awaiting-entry orders flagged for synthesis**: `KXFEDDECISION-26SEP-H25 YES @32` (stand down —
  the market is 52c and today's capture takes the other side of it, which is a deliberate reversal on
  post-Warsh information), `BTC SELL @63,400` and `/MBTU6 SHORT @64,340` (both ~18% below a 77,589 spot),
  `KRE @76.80`, `XLE @63.00`, `DG @121.00` (all now well below a market that moved away from them).
  `KXFEDDECISION-26OCT-H25 YES @28` is at market and is NOT contradicted — leave it live.
- **Coverage gaps**: no VIX, DXY, WTI or index-futures quote all morning (yahoo 429), so the macro
  section is built from FRED, finnhub ETF closes and verified press accounts of the 09-02 settle rather
  than from live index data. No options-implied-move check on any idea (yahoo options endpoint 401), so
  nothing today was tested against what the options market already prices. `nasdaq` history returns only
  20 bars in `recent` regardless of `--days`, which is why IONS, CHWY and SNOW could not be given
  targets anchored to mid-range resistance. Short interest failed for AVAV, KR and RH (nasdaq timeouts).
  Kalshi's `/markets` endpoint returns null prices — the **`/markets/trades` endpoint works** and is how
  today's Fed prices were obtained; worth remembering for future runs.
- **Sources that failed**: yahoo (429 on quotes/history, 401 on options), nasdaq short interest
  (read timeouts), `market_data.py events` (Kalshi keyword search returns unrelated cross-category
  markets and no prices), ir.ultragenyx.com and ir.ionis.com (fetch timeouts — SEC EDGAR and biospace
  were used instead).
- **Process note worth keeping**: I wrote a "HOLD, no new filing or agency action found" line on RARE at
  06:13 and only found the 09-02 8-K at 06:23, from the premarket movers board. Checking the premarket
  board and running `filings` on every open position should come BEFORE any position update is written,
  not after the new-idea hunt. The superseded block has been left in place above rather than deleted.
