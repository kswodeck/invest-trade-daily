# Research log — 2026-11-12

## [06:01-06:13 ET] MACRO — rates, crypto, regime
- FRED 10y `DGS10` **4.88%** (2026-11-09), prev 4.86 — rising. source: https://fred.stlouisfed.org/series/DGS10
- FRED 2y `DGS2` **4.56%** (2026-11-09), prev 4.51 — rising faster than the 10y. source: https://fred.stlouisfed.org/series/DGS2
- 10y-2y curve **+0.25** (2026-11-10), prev +0.32 — **flattening**, i.e. the front end is repricing *away* from cuts. source: https://fred.stlouisfed.org/series/T10Y2Y
- Fed funds effective **3.88%** unchanged. source: https://fred.stlouisfed.org/series/DFF
- Unemployment **4.1%** (Oct), prev 4.2% — labour market firmed, which is the mechanism behind the 2y selloff. source: https://fred.stlouisfed.org/series/UNRATE
- CPIAUCSL index 337.476 (Oct) vs 336.298 (Sep) = **+0.35% m/m**, an annualised ~4.3% — hot. source: https://fred.stlouisfed.org/series/CPIAUCSL
- TLT (20y proxy) 80.92, +0.05%. source: scripts/market_data.py macro
- Crypto: BTC **$73,391** (-0.78% 24h), ETH **$2,042.78** (-0.72%), SOL **$82.88** (-1.06%). source: https://www.coingecko.com
- **Regime read:** firm labour + hot CPI + flattening curve = the cut that equities were priced for is being taken away. This is a headwind to everything long-duration and to the 14 open longs. It argues for raising the bar on new longs, not for adding beta.

## [06:01-06:13 ET] DATA QUALITY — Yahoo rate-limited
- `market_data.py macro` returned ok:false for spx, ndx, dow, russell2000, vix, es_futures, nq_futures, dollar_index, us10y_yield, gold, wti_crude — Yahoo chart API is returning **429 Too Many Requests** on both query1 and query2, Finnhub refuses indices without a CFD subscription, stooq 404s on `^`-prefixed symbols.
- Only `bonds_20y` (TLT, 80.92) came through. No index/VIX/DXY/gold/WTI level today.
- Consequence: no live index or volatility level. Must be reported in `data_quality_notes`. Testing whether single-name `quote`/`history` still work.

## [06:01-06:13 ET] CALENDAR — earnings inside 10 sessions (fetched, finnhub)
- **Today 2026-11-12 amc**: CSCO (rev est 18.5B), AMAT (10.5B), NU (5.9B), STNE (3.8B), INTR (2.8B)
- 11-16: PDD (117B), BIDU, XPEV, TSN, IQ, ARMK, PAGS, **ACM amc (open position)**
- 11-17: **NVDA amc (111B)**, HD bmo, DIS bmo, TME, WSM, ATKR
- 11-18: TGT, LOW, TJX, ROST, GAP, PANW, CPRT, ZIM
- 11-19: BABA, WMT, NTES, INTU, FUTU, KEYS, POST
- source: scripts/market_data.py earnings --days 9 (finnhub)
- Note: **ACM reports 11-16 amc** and is an open position +5.8% — that is a dated event on money already at risk.

## [06:01-06:13 ET] TAPE — yesterday was a strong up day, but the month is down
- SPY closed **759.81**, +1.32% on the session (prev 749.92). source: finnhub quote
- But fetched relative-strength returns put **SPY at -2.34% over 1 month and -2.32% over 3 months** — the tape has been grinding lower and yesterday was a bounce inside that, not a trend. source: scripts/market_data.py relstrength
- This is the single most important context for the track record below: the report holds 14 long positions into a market down 2.3% on the month, and 4/41 closed trades hit target.
- Finnhub single-name quotes and nasdaq history both work; only the Yahoo-backed index/VIX/DXY/gold/WTI feeds are down.

## [06:01-06:13 ET] POSITION UPDATE — HII — opened 2026-10-12 at 262.00, now 313.96, +19.8%
- decision: **hold, and set a stop at 289.00** — it has had none for 29 days
- 289 sits between the fetched SMA20 (291.37) and SMA50 (279.82); at 27.00 above the entry it is 2.03 ATR from entry (ATR14 13.30), so it clears the 2.0 ATR stock floor measured from entry
- effect: the gain is locked — the position can no longer lose money
- cost: 289 is only 1.88 ATR below the last price, so an ordinary pullback can take it out. Accepted deliberately on a 67%-of-the-way-to-target holding with its earnings already reported.
- action: captured via add_candidate.py

## [06:01-06:13 ET] POSITION UPDATE — AAL — short opened 2026-10-03 at 13.35, now 14.10, -5.6%
- decision: **CLOSE THE SHORT AT THE OPEN**, by hand, do not wait for the 14.40 stop
- why the thesis is broken rather than merely offside: AAL **+12.8% 1-month vs SPY -2.34%** = +15.14 points of relative outperformance, and +5.12 vs XLY. Price 14.10 is above both SMA20 12.78 and SMA50 12.93, with the fast average above the slow one. source: scripts/market_data.py relstrength AAL --peer XLY
- checked for a rescue and found none: finnhub recommendation_trend is byte-identical across 2026-08/09/10/11 (strong_buy 4, buy 11, hold 14, sell 1, strong_sell 0), bullish share 50.0%, revision_direction **flat**. No downgrade cycle is coming. source: https://finnhub.io/api/v1/stock/recommendation?symbol=AAL
- the 14.40 stop is 0.30 away = **0.50 ATR** (ATR14 0.6022), i.e. inside one ordinary day. The exit is already forced; doing it deliberately at 14.10 saves ~2 points.
- **NOTE FOR SYNTHESIS/RED TEAM:** this row's reward-to-risk fails by construction. An exit-at-a-loss has a "target" above a short's entry, which the ratio cannot represent. A failing R:R here is the arithmetic working, not a defective idea — do not demote the instruction to the watchlist, where "not yet actionable" is the opposite of what it says.
- action: captured via add_candidate.py

## [06:01-06:13 ET] POSITION UPDATE — BCC — opened 2026-08-18 at 76.50, now 69.52
- decision: **CLOSE. The stated invalidation has fired** — this is not a drawdown to sit through
- fundamental trigger: fetched surprise record +47.2% (Dec-25), +18.3% (Mar-26), +30.8% (Jun-26), then **-7.7% (Sep-26: 1.04 actual vs 1.1269 est)**. Three big beats then a miss. source: https://finnhub.io/api/v1/stock/earnings?symbol=BCC
- sell side followed: buy 6 to 5 on 2026-11-01, bullish share 63.6% to 54.5%, revision_direction **deteriorating**. source: https://finnhub.io/api/v1/stock/recommendation?symbol=BCC
- cheap-or-broken test: **0 open-market insider buys, 0 distinct buyers**. No insider is treating a -24% de-rating as value.
- technicals: below SMA20 75.08, SMA50 75.40 *and* SMA200 76.75; 69.52 is 0.5% above the 65.00 200-day low, four sessions of lower lows (70.24 / 72.57 / 70.42 / 69.52)
- macro leg receded rather than arrived: 10y 4.88% rising, 2y 4.56% rising, curve flattening — the mortgage relief the housing thesis needed is being priced out
- note: carried **no stop for 85 days**, which is how an unmanaged loss got this large. Same defect just fixed on HII.
- action: captured via add_candidate.py

## [06:01-06:13 ET] REJECTED — all event contracts — Kalshi feed returned no economic markets today
- `market_data.py events "Fed"`, `"CPI"`, `"inflation"`, `"rate"` all returned **count 0**. An empty query returns 40 markets and every one is a multi-leg sports parlay (KXMVECROSSCATEGORY-*).
- So there is no Fed / CPI / macro event contract to price an edge against today, and the macro view below cannot be expressed as an event contract even though that would have been the cleanest vehicle for it.
- Coverage gap, not a judgement: do not read the absence of event ideas today as a view that they were unattractive. source: scripts/market_data.py events

## [06:01-06:13 ET] MACRO READ-THROUGH — the pending TLT long is fighting the fetched data
- `TLT` BUY @ 80.30 published 2026-11-04 is still awaiting entry; TLT last **80.92**.
- The thesis needed falling yields. Fetched: 2y **4.56% up from 4.51**, 10y **4.88% up from 4.86**, curve flattening 0.32 to 0.25, unemployment **4.1% improved from 4.2%**, CPIAUCSL +0.35% m/m (~4.3% annualised).
- Firm labour plus hot CPI plus a flattening curve is the front end pricing cuts *out*. That is the opposite of the TLT case.
- Treat as **do not chase**: leave the 80.30 limit unchanged rather than lifting it toward 80.92 to get filled. See the candidate captured for this.

## [06:01-06:13 ET] NEW-IDEA SCREEN — the 11-17/18/19 earnings slate, and why most of it fails
Screened HD, LOW, TGT, TJX, DIS, PANW, CPRT, ATKR on fetched history + revision trend + surprise record.

- **REJECTED — TGT** — best fundamental setup on the slate and it still fails the floor. Four straight beats (+4.5, +15.8, +12.1, +2.6), bullish share only **37.2%** (deeply doubted, and improving +0.8) — the skepticism was the edge. But last 162.70 against a fetched 200-day range high of **170.75**: an honest 2.0 ATR stop (ATR 5.81) sits at 151.00, giving 11.70 of risk against 8.05 of reward to the range high = **0.69:1**. Clearing 2.0:1 would need a 186 target, above anything it has traded in 200 days. That is the reverse-engineered target the strategy doc forbids, so the idea is dropped rather than dressed up.
- **REJECTED — LOW** — four straight beats, revisions improving +4.2 to 72.5% bullish, reclaimed the SMA200 (223.98). But **+25.05% vs SPY over one month** (+15.03 vs XLY) is a 23% run into a 11-18 binary, and with a 2.0 ATR stop at 217.79 the 2:1 target lands at 259.22 — exactly at the floor, which per the strategy doc means it failed the floor. Chasing a 23% month before a print is the pattern this report keeps losing on.
- **REJECTED — DIS** — 119.65 is 0.95% off its high, bullish share 87.2% (crowded) and revisions **deteriorating** -2.0. Crowded, extended, and being de-rated into an 11-17 print is the wrong side of all three.
- **REJECTED — PANW** — below SMA20 354.28 and SMA50 367.81, -22.6% off high, deteriorating, ATR 6.18%. Falling into 11-18 earnings; no support reclaimed yet.
- **REJECTED — CPRT** — revisions improving +6.5 and sitting on the SMA200 (32.01), but the fetched surprise record carries two ~10% *misses* in four quarters (-10.5, +3.8, -10.0, +3.5). An earnings trade on a name that misses half the time is a coin flip.
- **REJECTED — TJX** — revisions deteriorating -6.8; below SMA20 141.85 and SMA200 150.59.
- **REJECTED — HD** — mixed surprise record (+0.9, -2.2, +4.0, -5.4); no edge.
- **REJECTED — ATKR** — history fetch failed and bullish share collapsed -60.0 to 0.0. Not researchable in the time left; flagged rather than guessed.
- **The pattern across the whole slate is the finding:** yesterday was +1.32% on SPY inside a month that is -2.34%, and the names whose fundamentals improved have already travelled. Good business + already run = no reward-to-risk. That is why today's output is weighted to managing existing risk rather than opening new.

## [06:01-06:13 ET] DATA QUALITY — two more sources down
- `market_data.py implied` fails for every symbol: **Yahoo options returns 401 Unauthorized**. No options-implied move available today, so no candidate could be checked against what the market already prices.
- `market_data.py short` returns ok:false with null short_interest / days_to_cover for TGT and LOW. No short-interest or days-to-cover read today.
- Insider checks did work and were run on every equity finalist: BCC 0/0, TGT 0/0, LOW 0/0, PFE 3 buys/3 distinct, OXY 1/1, SMMT 6 buys/3 distinct.

## [06:14 ET] TIMESTAMP CORRECTION — read before trusting the times above
- Every heading above is stamped `06:01-06:13 ET`, which is the **verified** window: `date` returned 06:01:00 at setup and 06:13 when next read.
- They originally carried per-entry times (06:03 through 06:41) that were **estimated from my sense of pace, not read from the clock**, and were wrong by up to 40 minutes. They are corrected rather than left, because a fabricated timestamp is a fabricated number.
- Consequence for this run: ~47 minutes of budget remained at 06:14, not ~7. Research continued past this point rather than consolidating. All times from here are read from `date`.

## [06:19 ET] LONG-TERM LANE — screened 9 de-rated large caps, one cleared
Screened MRK, BMY, UPS, NKE, SBUX, GIS, DG, EL, MDT on insider buying + revision direction + four-quarter surprise record, then built a trailing-EPS multiple from the fetched quarterly actuals for the survivors. Insider buying was **0 buys / 0 distinct buyers on all nine** — so none of them has that confirmation and it is not carried as evidence for any.

- **CAPTURED — BMY** — trailing EPS **6.23** from the four fetched actuals (1.35 + 2.04 + 1.58 + 1.26) = **10.1x** at 62.91, against 12-16x for large-cap pharma. Four straight beats (+11.9, +10.4, +27.2, +17.0) with the two largest being the two most recent, i.e. already-cliff-adjusted estimates being beaten by a widening margin. 19 of 34 analysts still at hold (41.2% bullish, improving +1.2). **But at 62.91 the R:R against a 46.00 bear case is 1.01:1 against a 2.5 floor**, so it is captured as `wait: true` with a 53-57 accumulation zone, not as a buy today. Target 80.00 = 12.8x unchanged trailing EPS.
- **REJECTED — DG** — trailing EPS 7.44 (2.23+2.00+1.93+1.28) at 137.44 is **18.5x**. Revisions improving +5.0 and four beats, but 18.5x is not a value anchor and there is no de-rating to buy.
- **REJECTED — EL** — trailing EPS 2.91 at 112.33 is **38.6x**, and it has already run from a 66.22 low to 112.33 (+70%). The de-rating has been paid for.
- **REJECTED — MRK** — fetched actuals include -0.13 and -1.28, so trailing EPS of 3.17 is distorted by charges and no honest multiple can be built from it in the time available. Not rejected on the business; rejected as unmeasurable today. -6.2% off its high regardless.
- **REJECTED — NKE** — surprise record is huge (+10.0, +50.2, +22.9, +39.2) but bullish share **collapsed -10.5 points to 28.6%** and revision_direction is deteriorating. A falling knife with good prints; wants a base first.
- **REJECTED — SBUX, UPS, GIS, MDT** — UPS deteriorating -1.4; SBUX deteriorating -3.4 with a -6.3% miss in the record; GIS bullish share 10.7% and flat with a -12.7% miss; MDT improving but surprises are +3.4/-0.4/+0.9/+2.4, i.e. no gap between expectation and delivery to exploit.

## [06:19 ET] REJECTED — /MBTZ6 and all index futures — cannot verify levels today
- BTC spot **73,343** (-0.87% 24h), ETH 2,041.49 (-0.93%), SOL 82.93 (-1.11%). source: https://www.coingecko.com
- The pending `/MBTZ6` SHORT @ 74,075 (target 62,500, stop 79,800, published 2026-11-10) is live and only **0.99% below its entry**, so it is close to triggering, and the macro read above is directionally supportive.
- **But `history` fails for BTC-USD entirely** — nasdaq has no rows, Yahoo 429s, twelvedata and alphavantage have no API key, stooq has no rows. So there is **no fetched ATR for bitcoin today** and the 2.5 ATR futures stop floor cannot be checked.
- Therefore no amendment is made and no new crypto or index futures idea is captured: re-pitching /MBTZ6 a third time on unverifiable levels would be anchoring, and deriving /MES levels from SPY x 10 would be a fabricated number. Levels stand as published.

## [06:20 ET] STOP AUDIT — the single most important finding of this run
Recomputed every open position's stop distance in ATRs from fetched history, against the `MIN_STOP_ATR` floors in `config/strategy.md` (2.0 swing stock, 1.8 swing ETF). CLAUDE.md records that **all ten of the first month's stop-outs had a stop tighter than 1.6 ATR**, so this is the defect with the best-documented cost in this repo.

| sym | stop ATRs | floor | current R:R | verdict |
| --- | --- | --- | --- | --- |
| KHC | 2.54 | 2.0 | 2.83 | ok |
| OXY | **1.66** | 2.0 | 2.50 | TOO TIGHT — fixable |
| UNP | **1.65** | 2.0 | 2.45 | TOO TIGHT — fixable |
| ABT | 2.04 | 2.0 | 2.39 | ok, only just |
| PYPL | **1.37** | 2.0 | 2.58 | TOO TIGHT — **not** fixable |
| SMMT | 2.14 | 2.0 | 2.19 | ok |
| RTX | 2.26 | 2.0 | 2.12 | ok |
| XLU | 2.48 | 1.8 | 2.20 | ok |
| ONON | **1.71** | 2.0 | 2.40 | TOO TIGHT — fixable |
| ACM | 2.53 | 2.0 | 2.00 | ok |

Four of ten live stops are inside the floor. Three can be widened while keeping R:R above 2.0 and are captured as amendments; all three **widen** risk rather than tightening it, which is the opposite of the KRE stop-walking abuse:
- **OXY** 50.80 -> **50.15** (2.0 ATR), R:R 2.50 -> 2.08, new stop below the 53.66 range low
- **UNP** 277.40 -> **275.03** (2.0 ATR), R:R 2.45 -> 2.02. Also found the 315.99 target sits **1.84 above** the fetched 314.15 range high, so the scale plan now trims into 314.
- **ONON** 31.20 -> **30.69** (2.0 ATR), R:R 2.40 -> 2.05, new stop below the SMA50 at 31.95
- **PYPL** cannot be repaired: the 2.0 ATR stop at 53.00 drops R:R to **1.77**, under the floor, and a profit-protecting stop would have to be at/above 60.00 to clear 2.0 ATR measured from the 56.50 entry — above the 59.48 market. With no compliant stop in either direction, **size is the only lever**: trim half at the open, target cut 62.70 -> 62.00 (the old target was 0.03 under the 62.73 range high).
- ABT at 2.04 ATR is compliant by 0.04 and worth watching, not amending.

## [06:21 ET] POSITION UPDATE — holds with nothing changed (no candidate emitted, deliberately)
Checked and decided; no recommendation captured, because re-pitching an unchanged idea is what inflated this report's own by-conviction table. Levels verified compliant above.
- `KHC` 24.27 vs 23.00 entry, +5.5%. Stop 2.54 ATR, R:R 2.83. At the SMA20 (24.30). **Hold, unchanged.**
- `ABT` 109.29 vs 103.00, +6.1%. Stop 2.04 ATR — compliant by a hair. **Hold, unchanged**, watch the stop if ATR expands.
- `RTX` 201.29 vs 199.00, +1.2%. Stop 2.26 ATR, R:R 2.12. **Hold, unchanged.**
- `XLU` 43.82 vs 43.30, +1.2%. Stop 2.48 ATR against a 1.8 ETF floor; 1.86% off its range high. **Hold, unchanged.**
- `PFE` 29.45 vs 27.60, +6.7%, long-term, no stop (permitted). Fetched insiders: **3 open-market buys by 3 distinct buyers** — the cheap-vs-broken signal is present here and absent on BCC, which is the difference between the two. **Hold, unchanged.**

## [06:21 ET] PENDING ORDERS — levels re-verified, left alone
- `XLV` BUY @ 184.00 (last 188.95). Entry sits between the SMA20 182.51 and the market; R:R (201-184)/(184-176) = **2.13**, stop 2.14 ATR vs a 1.8 ETF floor. Still valid — **leave unchanged, do not chase** at 188.95 (1.75% off its high).
- `HUN` BUY @ 9.00 (last 9.78). The 9.00 entry sits on the fetched SMA50 of 9.01; R:R (10.82-9)/(9-8.09) = **2.00**, stop 2.06 ATR. 39.2% off its high. Still valid — **leave unchanged**; price is 8.7% above the limit, so do not lift it.
- `ADM` BUY @ 68.80 (last 70.92). Price is **below** the SMA20 76.06 and SMA50 80.34 and 20.1% off its high, so 68.80 is a bid under a downtrend rather than at support — the weakest of the three. 1.24 above the 66.06 range low. **Leave unchanged, do not lift**; if it does not fill, no trade.
- `GLD` SELL @ 406.77 (last **365.17**, -10.2% below the order). Moot — a `sell`/exit order 10% above the market cannot execute and expresses nothing. Treat as expired.
- `KXCPIYOY-26SEP-T3.5` NO @ 18 — the Kalshi feed returned no economic markets today, so this could not be re-priced at all. Unverifiable, left alone.

## [06:25 ET] NEW IDEA — TFC — the only financial in the book
(Heading corrected: when written this was the only new-money idea of the run; ALL, VVV and DLB were found afterwards.)
Screened KRE, USB, TFC, PNC, MET, PRU, AFL, ALL — financials have **no representation at all** in the current book, so this was the deliberate diversification hunt.
- **CAPTURED — TFC** — trailing EPS **4.60** from four fetched actuals = **10.9x** at 50.26, against 11.8x for USB computed identically. **37.0% bullish share** — the most doubted name in the screen — and improving +2.4. Four straight beats (+1.3, +8.6, +12.9, +3.7). Reclaimed the SMA200 (49.50); relative strength +11.79% vs SPY and +2.5% vs XLF over 1m. Insiders 2 buys but only **1 distinct buyer** — one person, not a cluster, recorded as thin.
- **Filed long_term, not swing, for a verifiable reason:** the fetched calendar puts the next TFC earnings at **2027-01-20 amc**, 69 days out, so no dated catalyst exists inside a swing horizon. A swing on it would have failed the catalyst test outright.
- **And it is `wait: true`:** at 50.26 the R:R against a 43.00 bear case is **1.00:1** (7.24 reward vs 7.26 risk, a literal coin flip) against a 2.5 floor. It qualifies only at or below ~47.14, so the entry is 47.00 with a 45.50-48.00 accumulation zone. Target 57.50 = 12.5x unchanged EPS.
- Invalidation is credit, not price: two consecutive quarters of rising net charge-offs with a reserve build taking trailing EPS below 4.00.

Rejected from the same screens:
- **ELV** 429.48 / ttm 30.35 = **14.2x**, -4.7% off high, above all MAs. Four big beats and improving, but not cheap and near the high. Also healthcare, where the book already holds PFE, ABT, XLV (pending) and now BMY — the correlation cap is the binding reason, not the business.
- **HUM** 446.31 / ttm 13.26 = **33.7x**, and already up from a 163.11 low (+174%). The de-rating has been paid for in full.
- **VTRS** 21.06 / ttm 2.56 = **8.2x** with four beats and improving revisions — genuinely cheap, but sits **0.19% off its 250-day high** after doubling off 10.15, so there is no support beneath an entry and no pullback to buy. **Worth carrying forward as a lead** if it ever pulls back to the 19.04 SMA20.
- **ALL** 262.18 / ttm 43.71 = **6.0x** with four beats of +40.1, +45.4, +44.7, +43.7 — the most striking number in any screen today. Not captured because that EPS is almost certainly catastrophe-light peak earnings and I could not verify a normalised figure from a filing in the time available. **The strongest lead left on the table** — a follow-up run should pull the 10-Q.
- **MCK / CAH / COR / CI / GILD / AMGN / PNC / AFL** — all deteriorating revisions, or no expectation gap to exploit, or (GILD) a charge-distorted ttm EPS of -0.31 that no multiple can be built from.

## [06:29 ET] ARITHMETIC SELF-AUDIT — recomputed every captured candidate
CLAUDE.md records that the model is "strong at research and undisciplined about its own arithmetic", so I recomputed R:R, stop distance in ATRs, the expectancy baseline and the evidence-kind count for all 13 candidates and corrected what disagreed. **Five real errors found in my own work:**
1. **TFC thesis stated the current R:R as 1.49:1; the true figure is 1.00:1.** Re-captured with the correct number and the arithmetic shown.
2. **CVS carried a bear case of 77.33** — the fetched range low, sitting 1.67 under the 79.00 entry — which produced an absurd **17.4:1** ratio. Corrected to 65.00, giving 2.07:1, which is *below* the 2.5 long-term floor and so became a second independent reason to cancel.
3. **HII claimed win_probability 0.52, a +26-point edge over its baseline.** Replaced with **0.49**, the actual driftless probability measured from the live price (24.96 of stop distance against 25.80 to target), so it asserts no edge at all. It still reads as +23 points against the *entry-based* baseline, and the thesis now explains why that baseline is the wrong reference for an already-profitable position rather than leaving the gap unexplained.
4. **Ten of thirteen candidates understated conviction against their own evidence lists** (e.g. ACM had 4 distinct kinds but claimed 4 instead of 5; TLT had 2 kinds but claimed 2 instead of 3). Corrected to the supported score in every case. Note the direction: I was *under*-claiming, which is still the score carrying no information — the failure CLAUDE.md describes as conviction collapsing to a default. TLT is the one worth flagging to the red team: it is now a 3 by evidence count while being an idea whose macro premise I explicitly described as weakened, so if any score should be cut on judgement it is that one.
5. Verified that OXY, UNP and ONON land at exactly 2.00 ATR after widening, and that all three keep R:R above 2.0 (2.08, 2.02, 2.05).

Flags deliberately left standing, because they are the arithmetic working rather than defects:
- **AAL** R:R 0.71, stop 1.74 ATR, WP below baseline — it is a close-at-a-loss instruction; a short being exited above its entry cannot produce a passing ratio.
- **CVS** R:R 2.07 below the 2.5 floor and WP at baseline — both now support the cancellation.
- **PYPL** stop at 1.37 ATR — that defect *is* the candidate; it is unfixable and the response is halving the size.

## [06:31 ET] NEW IDEA — ALL — captured, with its weakness stated
Followed up the lead flagged above rather than leaving it.
- ttm EPS **43.71** (9.76 + 8.99 + 10.65 + 14.31, all fetched actuals) = **6.0x** at 262.18.
- Four consecutive beats of **+43.7%, +44.7%, +45.4%, +40.1%** — consensus has been ~30% below the actual print every quarter for a year. The largest and most consistent expectation gap in any screen today.
- Valuation method shown: 25% haircut to normalise a benign cat year -> 32.78, at 10x (low end of the historical P&C range) -> **328** target. Bear case **198** = 9x a severe-year 22.00 EPS, which sits 6.9 above the 191.13 range low.
- `wait: true` — at 262.18 R:R is **1.03:1** against a 2.5 floor; qualifies only at/below ~235. Entry 235, zone 228-240, bracketing the SMA200 at 231.03.
- **Conviction deliberately held at 3, not 4, and positioning deliberately excluded from the evidence**, because the fetched recommendation trend cuts against the idea: sell + strong_sell rose from **1 (2026-08-01) to 3 (2026-11-01)** even as the buy count rose. The sell side is polarising, not capitulating. Insiders 0/0.
- Stated honestly in key_risk: **I did not read the 10-Q**, so the 25% normalisation is a judgement, not a figure traced to a filing. If normalised EPS is really ~25 then 10x is 250 and there is no idea. Invalidation: one quarter with cat losses taking EPS below 5.00 and a combined ratio above 100.

## [06:31 ET] REJECTED — remainder of the 11-16/11-17 slate
- **TSN** 59.87 / ttm 3.98 = **15.0x**, flat 47.4% bullish. Reports 11-16 bmo but 15x is no discount.
- **WSM** 262.09 / ttm 9.03 = **29.0x**; **VIK** 90.06 / 3.02 = **29.8x** — both expensive, VIK also 85.2% bullish (crowded).
- **ARMK** 86.4% bullish (crowded), flat, and a -14.4% miss in the record.
- **TME** and **PAGS** — ttm sums of 6.30 and 8.36 against prices of 9.22 and 7.94 give multiples of 1.5x and 0.95x, which means the fetched actuals are not in USD (CNY and BRL respectively). **Not rejected on merit — rejected as unmeasurable**, since any multiple I built from those numbers would be wrong. Both also have deteriorating revisions.
- **PDD, BIDU, XPEV, IQ, NVDA, HD, DIS** not individually screened for new entries: NVDA was stopped out 2026-11-10 and published twice in ten days (anchoring guard), DIS was rejected above, and the China ADR complex shares one driver so it would breach the correlation cap on its own.

## [06:31 ET] NEW IDEAS — VVV and DLB — the two actionable new swings, both found from the calendar
Built the small/mid-cap candidate pool **from the fetched earnings calendar** (revenue estimate between 80M and 800M in the next 9 days) rather than from remembered tickers, then screened POWL, GFF, DLB, KLIC, GLBE, BRBR, VVV, YETI and WWW. Two cleared.

- **CAPTURED — VVV (Valvoline)** — revisions **improving +6.0** to 72.7% bullish, surprises +12.3, +18.1, +12.3 in three of four quarters (the -4.7% miss is the oldest). 35.90 has reclaimed the SMA200 at 34.45. Entry **34.50** (the reclaimed 200-day, -3.9% vs market), stop **32.00** = **2.02 ATR**, target **41.00** = 0.08 under the 41.08 range high -> **2.60:1**. Dated catalyst **2026-11-19 amc** (fetched calendar, rev est 574M). 19.9x ttm 1.80 — a revisions-and-trend idea, not a value one, and said so.
- **CAPTURED — DLB (Dolby)** — the **largest revision improvement found anywhere today, +7.8** to 77.8% bullish. ttm EPS 4.11 = **15.7x** for a per-device royalty model with no manufacturing capex. SMA20 63.03 / SMA50 60.90 / SMA200 59.36 stacked in order. Entry **62.00** (under the SMA20), stop **58.70** = **2.01 ATR** and under the SMA200, target **69.50** = 0.45 under the 69.95 range high -> **2.27:1**. Dated catalyst **2026-11-17 amc** (fetched, rev est 376M).
- Both carry a **half-size-into-the-print rule**, because a pullback entry this close to a dated event means a fill is likely to be straight into the binary. Both are `wait: true` — if the level does not come, there is no trade.
- Honest weakness on DLB, stated in key_risk: the two most recent surprises are the two **smallest** (+1.2, +1.8 vs +19.7, +40.0 earlier), so the beat margin is compressing as the sell side warms up.

Rejected from the same pool:
- **POWL** — the theme is the most attractive on the board (electrical equipment into datacenter power, the exact driver `config/strategy.md` cites as a good long-term example) and the data says no anyway: **-55.5% off its 328.00 high**, below SMA20/50/200 (154.71 / 172.86 / 213.43), revisions **deteriorating -5.8**, and the two most recent quarters **missed** (-5.2%, -10.0%). A good story with a bad tape and falling estimates.
- **KLIC** — four big beats (+16.7, +15.7, +30.2, +24.1) and -46.1% off its high, but below all three averages with flat revisions. Wants a base before it is buyable; **worth re-checking** after the 11-18 print.
- **GFF** (91.7% bullish, 2.6% off high) and **GLBE** (95.0% bullish, deteriorating) — both too crowded to pay for.
- **BRBR** — -70.2% off high with misses of -20.1% and -56.5%. Broken, not cheap.
- **YETI** — revisions improving +5.6 but price is below both the SMA20 (43.99) and SMA200 (43.84), and it has **no earnings date inside the window**, so there is no swing catalyst.
- **WWW** — flat revisions, 15.1x, no dated catalyst in the window.

## [06:31 ET] NOTE FOR THE RED TEAM — conviction distribution
Applying the evidence-count rule from `config/strategy.md` mechanically (score = distinct `kind` count) produces **four 5s today** — BCC, ACM, BMY and DLB. That is a lot, and the rule is a floor on honesty rather than a judgement: it says what the evidence supports, not that the ideas are equally good. BMY is the strongest of them. If any should come down on judgement they are **ACM** (a 5 on what is really a trim instruction) and **TLT**, now a 3 by count on an idea whose macro premise I explicitly described as weakened. I have not lowered them myself because the research phase's job is to claim the supported score and the red team's is to cut it.

## [06:32 ET] RESEARCH COMPLETE
- **candidates: 16 unique symbols** (29 rows in `candidates.jsonl`; later rows supersede earlier ones for the same symbol, as synthesis expects)
- Horizons: **11 swing, 5 long_term, 0 intraday.** Conviction: four 3s, eight 4s, four 5s.
- **Nothing intraday cleared the bar and no mix was manufactured.** Yesterday was a +1.32% bounce in a month that is -2.34%, so there was no gap to fade and no 8:30 print today to trade.

**What this report is today: nine of the sixteen are instructions on money already at risk, and they matter more than the new ideas.**
Act on these at the open, in this order:
1. **AAL — close the short** (14.10, 0.50 ATR from its stop, leading SPY by 15.1 points over a month)
2. **BCC — close the long** (stated invalidation fired: first miss after three big beats, revisions deteriorating, 0 insider buys)
3. **HII — set a stop at 289.00** (+19.8% and unstopped for 29 days; this locks the gain)
4. **OXY 50.80 -> 50.15, UNP 277.40 -> 275.03, ONON 31.20 -> 30.69** — all three *widen* a stop that sits inside the 2.0 ATR floor
5. **PYPL — trim half** (its stop cannot be made compliant in either direction; size is the only lever)
6. **ACM — trim half before the 2026-11-16 close** (earnings confirmed on the fetched calendar)
7. **CVS — cancel the stale 79.00 limit** (11.8% below market; a standing order to buy a breakdown)
8. **SMMT — do nothing, deliberately** (the alarming -6.7% day is 0.94 of one ATR on a 7.57% ATR name)
9. **TLT — do not chase**; leave the 80.30 limit unmoved

New money, all four `wait: true` because nothing qualified at the market:
- **VVV** entry 34.50 (reclaimed 200-day), 2.60:1, earnings 11-19 amc
- **DLB** entry 62.00, 2.27:1, earnings 11-17 amc, largest revision improvement found today (+7.8)
- **BMY** accumulate 53-57, 10.1x trailing EPS, target 80 = 12.8x
- **TFC** accumulate 45.50-48.00, 10.9x, the only financial in the book
- **ALL** accumulate 228-240, 6.0x, published with its unverified cat-normalisation stated

**Coverage gaps — what I could not check:**
- **No index, VIX, DXY, gold or WTI level anywhere in this run.** Yahoo's chart API returned 429 on every index symbol and Finnhub refuses indices without a CFD subscription. SPY (759.81) is the only broad-market price here, via finnhub.
- **No options-implied move for any candidate** — Yahoo options returns 401 Unauthorized, so `implied` failed on every symbol. Not one target was checked against what the options market already prices.
- **No short interest or days-to-cover for anything** — `short` returned ok:false with null fields.
- **No event contracts at all.** Kalshi returned count 0 for "Fed", "CPI", "inflation" and "rate"; an empty query returns 40 markets, all sports parlays. The pending `KXCPIYOY-26SEP-T3.5` could not be re-priced.
- **No crypto or index futures idea, and no /MBTZ6 amendment** — `history` fails for BTC-USD on all five sources, so there is no fetched bitcoin ATR and the 2.5 ATR futures floor could not be checked. BTC spot 73,343 is 0.99% below the live short entry, so that order is near triggering on levels nobody re-verified today.
- **No micro caps** (nothing under ~$2B cleared) and **no small cap at all** — of nine screened from the calendar, two cleared and both are mid-caps.
- **ALL rests on an unread 10-Q.** The 25% catastrophe normalisation behind its 328 target is my judgement, not a figure from a filing. It is the biggest single unverified assumption in this report.
- **KLIC and VTRS left as live leads**, both deliberately: KLIC (four big beats, -46% off high) needs a base and reports 11-18; VTRS is 8.2x but sits 0.19% off its own high with no support under an entry.

**Sources that failed:** Yahoo chart API (429, all indices + BTC-USD), Yahoo options (401, all symbols), Finnhub indices (CFD subscription required), stooq (404 on `^` symbols and no BTC rows), twelvedata and alphavantage (no API key), `short` endpoint (null fields), Kalshi economic markets (count 0), nasdaq history for ATKR.
**Sources that worked:** finnhub quotes / earnings calendar / recommendations / insider transactions, nasdaq daily history, FRED, CoinGecko, SEC EDGAR filing index.
