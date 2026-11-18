# Research log — 2026-11-18

## [06:03 ET] MACRO — rates, policy, data sources
- US 10y Treasury **5.12%** (2026-11-16), prev 5.15% — source: FRED DGS10 https://fred.stlouisfed.org/series/DGS10
- US 2y **4.83%** (2026-11-16), prev 4.88% — source: FRED DGS2 https://fred.stlouisfed.org/series/DGS2
- Fed funds effective **3.88%** — source: FRED DFF https://fred.stlouisfed.org/series/DFF
- 10y-2y curve **+0.30** (2026-11-17), prev +0.29 — steepening slowly — source: FRED T10Y2Y
- Unemployment **4.1%** (Oct 2026), prev 4.2% — labour market not deteriorating — source: FRED UNRATE
- CPIAUCSL **337.476** (Oct 2026) vs 336.298 (Sep) = **+0.35% m/m** — not a disinflation print — source: FRED CPIAUCSL
- Regime read: fed funds 3.88% well BELOW 10y 5.12%. Long end is pricing term premium / fiscal supply, not growth. A 5.12% 10y with 4.1% unemployment is a restrictive-long-end, non-recessionary tape. Duration longs (TLT) are fighting the long end; that is the open TLT position's problem.
- TLT (bonds_20y proxy) **79.55**, +0.21% — source: finnhub via market_data.py
- **DATA GAP (material):** Yahoo Finance returning HTTP 429 on every index/VIX/DXY/gold/WTI call this run. SPX, NDX, DJI, RUT, VIX, /ES, /NQ, DXY, 10y quote, gold, WTI all `ok: false`. Finnhub works for US-listed equities/ETFs but refuses indices ("Market data subscription required for CFD indices"). So: **no VIX level, no index level, no futures level available this run.** Any futures idea today would require a fabricated price — so none will be published. Noting for data_quality_notes.

## [06:05 ET] OPEN POSITION MARKS — all 15, prev close 2026-11-17 (session=pre, age 842min = previous close, NOT stale)
source: finnhub via `python scripts/market_data.py quote` — https://finnhub.io
| Sym | Entry | Last (11/17 close) | %vs entry | 11/17 chg | Target | Stop |
| --- | --- | --- | --- | --- | --- | --- |
| BCC | 76.50 | 65.14 | -14.8% | -1.85% | 110.00 | none |
| PFE | 27.60 | 28.47 | +3.2% | -1.35% | 42.00 | none |
| KHC | 23.00 | 25.11 | +9.2% | +0.16% | 28.09 | 21.20 |
| OXY | 54.00 | 56.52 | +4.7% | -1.46% | 62.00 | 50.15 |
| AAL(short) | 13.35 | 12.92 | +3.2% | -2.42% | 10.60 | 14.40 |
| HII | 262.00 | 297.44 | +13.5% | -1.54% | 339.76 | none |
| UNP | 288.60 | 297.03 | +2.9% | -2.20% | 315.99 | 277.40 |
| ABT | 103.00 | 104.71 | +1.7% | -2.55% | 117.34 | 97.00 |
| PYPL | 56.50 | 58.11 | +2.8% | -1.22% | 62.70 | 54.10 |
| RTX | 199.00 | 198.00 | -0.5% | +1.60% | 226.50 | 186.00 |
| XLU | 43.30 | 43.42 | +0.3% | -1.59% | 46.60 | 41.80 |
| ONON | 34.20 | 31.85 | -6.9% | -2.78% | 41.41 | 30.69 |
| TLT | 80.30 | 79.55 | -0.9% | +0.21% | 84.30 | 78.80 |
| **ACM** | 66.74 | **80.53** | **+20.7%** | **+11.08%** | 77.22 | 61.50 |
| DKS | 144.50 | 140.87 | -2.5% | -4.18% | 175.50 | 129.00 |

- Tape read: 11/17 was broadly risk-off — ABT -2.6%, ONON -2.8%, UNP -2.2%, BCC -1.9%, DKS -4.2%. RTX +1.6% and TLT +0.2% the only green besides ACM. Defensive/duration bid, cyclicals sold.
- **ACM traded through its 77.22 target on a +11.08% day.** This is the single most important position event. Investigating cause next.
- ONON at 31.85 is $1.16 above its 30.69 stop — closest position to being stopped.

## [06:08 ET] POSITION UPDATE — ACM — opened 2026-11-07, +20.7% — TARGET HIT, CLOSED
- 11/16 close 72.50 → 11/17 **opened 79.50** (gap), high **83.55**, close **80.53** on 4.15M shares vs ~1.2-2.3M normal — source: finnhub history via market_data.py
- Cause: FY2026 results. 8-K filed 2026-11-16, **10-K filed 2026-11-18 for fiscal year ended 2026-10-02** — source: https://www.sec.gov/Archives/edgar/data/868857/000086885726000026/acm-20261002.htm
- Target was **77.22**; the 11/17 session traded 78.25–83.55, so the whole day was above target. Position is **closed at target** by grading.
- decision: **take the win, do not re-enter.** Re-publishing ACM today would open a *new* row at 80.53 — i.e. buying a +11% earnings gap after the news, with no new catalyst and the 10-K only landing this morning. That is chasing. No candidate emitted.
- This is the 5th target hit of 43 closed. Worth noting against the 10% hit rate: it came from a long-ish hold with a wide stop (66.74 entry / 61.50 stop = 7.9% risk), not a tight one.

## [06:10 ET] POSITION UPDATE — BCC — opened 2026-08-18, -14.8% — DETERIORATING, no stop
- 65.14, which is **0.22% off the 140-day low of 65.00**. Six consecutive down closes: 70.42 / 69.52 / 67.92 / 67.39 / 66.37 / 65.14 — source: nasdaq history via market_data.py
- SMA20 **73.27**, SMA50 **74.54** — price is 11% below the SMA20 and 12.6% below the SMA50. ATR14 3.53 (5.42%).
- Target is 110.00 against a 65.14 last. Position carries **no stop** and is a `long_term` idea; the long_term book is 0/4 target hits, avg -15.2%.
- Context: 10y at 5.12%. Boise Cascade is wood products into housing starts. A 5.12% long end is the thesis's problem, and it got worse, not better.
- decision: **needs a hard invalidation, and new lows every session is it.** Investigating fundamentals before committing to close vs. stop.

## [06:11 ET] POSITION UPDATE — ONON — opened 2026-11-03, -6.9% — HOLD, stop UNCHANGED
- 31.85. Stop 30.69 is 1.16 away = **0.65 ATR** (ATR14 1.79, 5.63%). Broke below SMA50 (32.35) on 11/17; SMA20 34.42 well above.
- From the 34.20 entry the 30.69 stop was 3.51 pts = **1.96 ATR**, i.e. published essentially at the swing floor. It was not a tight stop when written; the price has simply gone against it.
- decision: **hold, do NOT widen the stop.** Widening a stop because price approached it is the exact free-ratio manipulation `check_stop_distance` exists to stop, run in reverse. The stop is doing its job. No candidate emitted — nothing changed but price.

## [06:12 ET] POSITION UPDATE — DKS — opened 2026-11-13, -2.5% — HOLD into the 11/23 print
- 140.87. **11/17 was an outside day down: opened 148.11, high 149.46, low 140.71, closed 140.87 — at the low**, on 1.46M shares. That broke the SMA20 (144.14) the 143.00-146.50 entry zone was predicated on.
- SMA50 **137.95** is the next support and is still below price. Stop 129.00 = 11.87 below = **1.90 ATR** (ATR14 6.25).
- **Q3 FY2026 earnings confirmed 2026-11-23 on the fetched finnhub calendar** — 3 sessions away. Second print since the 2026-08-25 guidance cut (-30.7% day, FY adj EPS cut to $11-12 from $13.50-14.50).
- decision: **hold.** The thesis (DICKS banner comping +4.9%, Foot Locker the fixable loss) is unchanged and the print that tests it is the published catalyst. The SMA20 break is a real negative but the stop sits below the SMA50, which is the level that matters. No change to levels → no candidate emitted.
- Caveat for synthesis: this position is 100% exposed to a dated binary 3 sessions out. That is what was published; it is not new risk.

## [06:14 ET] DATA GAP — event contracts unavailable this run
- `market_data.py events` queried for "Fed", "FOMC", "interest rate", "recession", "inflation", "Bitcoin".
- "FOMC"/"interest rate"/"recession"/"inflation"/"Bitcoin" all returned **count 0**.
- "Fed" returned 17 markets, all of them Kalshi `KXMVECROSSCATEGORY` sports/tennis cross-category tickers matched on a substring, and **every one had yes_bid, yes_ask, last_price and volume all null**.
- So there is no quotable event-contract price this run. Per non-negotiable #2 no event contract will be published today — a cents entry I cannot fetch is a fabricated probability. Noting for data_quality_notes.
- Combined with the Yahoo 429 killing every index/VIX/futures quote, **today's report can only honestly cover US-listed equities and ETFs** (finnhub + nasdaq both working for those).

## [06:18 ET] ACM READ-ACROSS — what ACM's print actually said (grounds everything below)
Read ACM's Exhibit 99.1 FY2026 release — source: https://www.sec.gov/Archives/edgar/data/868857/000110465926128300/tm2629784d1_ex99-1.htm
- Q4 revenue $3,878m **down 7%** y/y; FY revenue $15.1bn **down 6%** — the top line SHRANK.
- Q4 NSR $1,920m +3%; FY NSR $7,328.6m. Q4 adj EPS **$1.63 (+20%)**; FY adj EPS **$4.03**.
- **Total backlog $28,016m, up 13%, a record.** Design-only backlog $26,115m. Book-to-burn **1.3x FY / 1.1x Q4**.
- Organic NSR, constant ccy: Americas +1% Q4 / +3% FY; International +5% Q4 / +1% FY.
- FY2027 guidance: organic NSR growth **4-6%**, adj EPS **$6.15-6.35**, adj EBITDA $1,350-1,390m, FCF ~$300m (incl. ~$500m cash use on two Construction Management projects).
- Dividend raised 10% to $0.34/qtr (8-K) — source: https://www.sec.gov/Archives/edgar/data/868857/000110465926128300/tm2629784d1_8k.htm
- **The honest decomposition of the +11% gap:** the FY27 adj EPS guide of $6.15-6.35 against FY26's $4.03 is a ~53% step-up, and a large part of that is company-specific — the two Construction Management projects rolling off. **That part does NOT read across to anyone.** What does read across is the demand signal: record design backlog +13% and 1.3x book-to-burn in infrastructure design is an end-market statement (water, transport, environmental), not an AECOM statement. That is the only part I will lean on.

## [06:19 ET] WATCHLIST — J (Jacobs Solutions) — good setup, FAILS the swing R:R floor at 158
Full workup done; it does not clear the bar, and the arithmetic is why. Recording so synthesis does not re-litigate it.
- Price 158.23 (11/17 close). ATR14 **5.1376 (3.25%)**. SMA20 153.51, SMA50 145.61. 140-day range 105.68-162.00; **-2.33% off the high**.
- **Earnings FY Q4 2026-11-23 amc**, confirmed on the fetched finnhub calendar (listed `J(amc)`).
- Structure is genuinely good: **162.00 resistance tested five times** — 11/03 161.59, 11/04 162.00, 11/12 161.65, 11/16 161.41, 11/17 161.50 — a seven-session coil, with the floor at the 11/05-11/06 washout (11/05 close 147.54, 11/06 low 144.55).
- The 11/05 -7.9% intraday break was **market-wide, not company news**: that was the AI-infrastructure selloff, Nasdaq -5% and the semi index -11% intraday. No company-specific cause found. Source: https://weissratings.com/en/instant-news-alerts/jacobs-solutions-inc-j-down-5-1-should-i-sell-into-strength
- Relative strength is exceptional and measured: J +14.38% 1m / +7.37% 3m / +40.16% 6m vs SPY -4.44 / -4.76 / -0.18 = **+18.82 / +12.13 / +40.34 points**; vs XLI +15.54 / +16.82 / +42.52. Leadership, not catch-up. Source: market_data.py relstrength
- **Why it is rejected as a recommendation — the arithmetic:**
  - Disciplined stop must clear 2.0 ATR = 10.28 pts. Real support is 147.50 (the 11/05 capitulation close); a 147.00 stop from a 158.00 entry = 11.00 = **2.14 ATR**, just clears.
  - Target derived independently, two ways, NOT reverse-engineered: (a) the ACM-gap equivalent, 158.23 × 1.11 = **175.6**; (b) the coil measured move, 162.00 + (162.00-144.55) = **179.45**. Conservative anchor **176.00**.
  - 176.00 target / 147.00 stop / 158.00 entry → reward 18.00, risk 11.00, **R:R = 1.64. The swing floor is 2.0.**
  - To pass at this entry the target must go to 180.00, which is the measured move rounded up and above every method I can defend — that is precisely the "targets nudged until they passed" failure. Alternatively the stop tightens to ~149, which is 1.75 ATR and fails the ATR floor. **Both routes to 2.0 are the manipulations the floors exist to catch, so the idea failed the floor.**
- Negative/neutral positioning worth stating: insiders **0 open-market buys, 2 sells ($2,478,583)** over 6 months. Analyst recommendation trend **flat for four straight months** (6 strong buy / 12 buy / 6 hold, 75% bullish, 0.0% change) — no revision impulse. The five Form 4s filed 11/17 are not purchases; the only 8-K since is a board appointment (Richard D. Phillips, effective 2026-12-01, Item 5.02) — source: https://www.sec.gov/Archives/edgar/data/52988/000162828026074196/j-20261112.htm
- **trigger to make it actionable:** either (a) a pullback into the 149.70-151.00 shelf (11/06 high 149.835, 11/09 open 150.96 / low 149.72), where a 140.00 stop is 2.04 ATR and 176.00 gives R:R 2.43; or (b) after the 11/23 print, a hold above 162.00 on volume, which converts it to a breakout with a measured target.
- Not published. **A momentum name 2.3% off its high cannot clear 2:1 against a 2-ATR stop without an invented target** — that is a structural point, not a J-specific one, and it is worth carrying into the rest of this run.

## [06:22 ET] MACRO — THE REGIME: this is a HIKING cycle, and it reframes the whole book
My FRED read (fed funds 3.88% vs 2y 4.83% = ~95bp of tightening priced into the front end) is confirmed by rate-market pricing:
- **Current target range 3.75%-4.00%.** The last move was a **+25bp HIKE in September 2026**. The October meeting was a **hold on a 10-2 vote, with Cook and Hammack dissenting in favour of a hike**.
- **December 8-9 FOMC: a +25bp hike is priced at ~91-95%.** Kalshi 91% hike / 6% >25bp / 5% no change; a later 11/16 snapshot 95% hike / 4% hold / 1% cut. Fed funds futures ~93% on 11/13. Governor Waller said he is "leaning toward supporting an increase in our policy rate of 25 basis points".
- **OIS priced a net +81.1bp of hikes over the next 12 months as of 2026-11-17** — about 3.2 more hikes at a 25bp step.
- Driver is inflation re-accelerating against a firm labour market: **Oct CPI +0.4% m/m headline, core +0.3%**, unemployment 4.1%, solid payrolls. My own FRED pull agrees: CPIAUCSL 336.298 → 337.476 = **+0.35% m/m**, and UNRATE fell 4.2% → 4.1%.
- Sources: https://kalshi.com/markets/kxfeddecision/fed-meeting/kxfeddecision-26dec | https://www.benzinga.com/markets/prediction-markets/26/10/62728825/will-the-fed-hike-rates-in-december-heres-what-the-prediction-market-is-saying | https://predictionmarketspicks.com/articles/fed-rate-december-2026-odds-half-point-hike-dot-plot-kalshi-polymarket-futures | https://www.pouyam.com/guides/fed-rate-hike-december-2026
- Caveat recorded honestly: these are prediction-market and aggregator pages, several inconsistent on the meeting date (Dec 8-9 vs Dec 9) and some low quality. The *direction* is corroborated four ways and by the FRED curve itself; treat the exact percentage as approximate.

**What this does to the existing book — the single most important framing for synthesis:**
- 14 of the 15 open positions are longs and three of them (**TLT, XLU, and to a lesser degree the XLRE-type exposure**) are duration/rate-sensitive longs. A long-duration Treasury position into 81bp of priced hikes with the 10y at 5.12% is fighting the Fed, not anticipating it.
- **Do not publish any new long-duration or rate-sensitive long today.** That lane is the one the macro is actively against.
- The corollary is the opportunity: the cleanest risk/reward available in a hiking cycle is on the SHORT side of rate-sensitive assets, and the book has exactly one short (AAL) in fifteen positions. That asymmetry is itself a finding.

## [06:26 ET] REJECTED — AMTM — first real level (SMA200 23.68) gives only 1.28:1; 2:1 needs a target in dead space
- Setup was genuinely attractive: 21.22, pulled back 5 sessions from the 11/10 high of 23.37 on **declining** volume (1.08M on 11/17, the lowest in 20 sessions, vs 1.9-3.0M on the advance — constructive, not distribution), holding above a rising SMA50 (20.24). Earnings **FQ4 2026-11-23** on the fetched calendar. Amentum is Jacobs' former Critical Mission Solutions business, so it is a direct ACM/J comp.
- Relative strength real: +8.93% 1m vs SPY -4.44% = **+13.37 pts**; +0.90% 3m vs -4.76% = +5.66; vs XLI +10.09 / +10.35. (6m is -6.05 vs SPY — recent leadership, not durable.)
- Against it: analyst revision direction **deteriorating**, bullish share 52.6% and -3.0%; **zero insider activity** in 6 months, neither buys nor sells.
- **The arithmetic that kills it:** ATR14 0.9456 (4.46%), so the 2.0-ATR stock floor needs ≥1.891 of risk. Real support is the late-Oct base 19.82-20.15 plus the SMA50; a stop below the whole base at 19.30 = **1.92 risk = 2.03 ATR**, just clears.
  - First defensible target is the **SMA200 at 23.6845** (400-day history: high 38.11, low 17.72). Reward 2.46 → **R:R 1.28. Fails the 2.0 floor.**
  - Clearing 2:1 requires a 25.06 target. The SMA200 is 23.68 and the 140-day high is 26.67, so **25.06 is dead space with no structure** — it is the 2:1 solve, not a level. Refused on that basis.
- Not published.

## [06:27 ET] STRUCTURAL FINDING — why so little is clearing today, and it is not a thin tape
Three full workups (J, AMTM, and BURL checked below) all failed the same way, so this is arithmetic rather than bad luck. R:R = (target-entry)/(entry-stop); with the stop floored at k·ATR (k = 2.0 stock, 1.8 ETF), clearing 2:1 requires the target to be **≥ 4·ATR away from entry**. In today's tape that means:
- a 4.46% ATR name (AMTM) needs **+17.8%**
- a 4.39% ATR name (BURL) needs **+17.6%**
- a 3.25% ATR name (J) needs **+13.0%**
- but a 1.6-2.2% ATR ETF needs only **+6.4% to +8.8%**
In a 4-6% ATR equity tape, a swing long can only clear 2:1 by targeting a level 15-20% away, which in almost every case is dead space above the nearest real resistance. **So the floors are rejecting swing equity longs almost categorically today — that is them working, not a thin opportunity set.**
The two lanes where the geometry can still be satisfied honestly are therefore:
1. **low-ATR ETFs**, where a real prior level sits 4+ ATR away, and
2. **`long_term`**, which needs no ATR-floored stop at all — only a defended valuation target and a stated bear-case price at 2.5:1.
Searching both deliberately rather than forcing a swing equity long. Also note BURL: 235.14, -37.9% off its high and 3.65% off its 140-day low, earnings 11/23, ADV$294m — the trade-down thesis is real in a hiking cycle, but stop 214.00 (2.05 ATR) against the SMA50 at 252.79 is **0.83:1**, and 2:1 needs 277.4 which is dead space. Rejected on the same arithmetic.

## [06:34 ET] CAPTURED — IWM sell_short — swing, conviction 4, R:R 2.27
- Entry 270.50 (zone 268.50-273.00), stop 284.50, target 238.69, target_2 228.90. Risk 14.00 = **2.41 ATR** (ATR14 5.8061, 2.16%) — clears the 1.8 ETF floor and the 2.25 "comfortable" level.
- The level work that makes it publishable, bracketed by running `history` at six windows: range_low is **267.865 for the 60, 90 AND 120-day windows**, then **238.69 at 180 days** and 228.90 at 250. So 11/17's low of 267.865 is a **120-session low** and the next real support is 11.3% below. The target is a read level, not a solve.
- MA cluster overhead is unusually tight: SMA20 278.12 / SMA200 279.51 / SMA50 279.79 — all three inside 1.67, i.e. within 0.29 ATR of each other, 3.5-4.0% above price.
- Breakdown volume 29.1M vs ~20M average on the prior eight sessions. Broke the 270.23/270.52 double low (11/05, 11/06) that had held eight sessions.
- **VENUE NOTE — a documented substitution, not an oversight.** `config/universe.md` prefers `/M2K` micro Russell futures over IWM for an index view, "especially to short". **I could not get a futures quote this run** — Yahoo is 429ing and finnhub refuses indices, so `russell2000`, `es_futures` and `nq_futures` all came back `ok: false`. Naming a `/M2KZ6` entry price would be a fabricated number, which non-negotiable #2 forbids outright. So the view is expressed in IWM with `requires_margin: true` and this reason stated. Had a quote been available the futures contract would have been the better instrument.
- Counter-argument carried on the page rather than argued away: IWM is -0.82% on 1m vs SPY -4.44%, so it has OUTPERFORMED by 3.62 points over the last month while breaking down in absolute terms. Sized 2% for that reason, and the scale plan covers into the 12/08-12/09 FOMC rather than through it.

## [06:35 ET] XLV — awaiting entry, UNCHANGED, deliberately not re-pitched
- Published 2026-11-09 @ 184.00, amended 2026-11-17 to entry 183.50 / stop 174.50 / target 203.50. Now **185.24**, so it still has not filled — it needs a 0.94% dip.
- Levels still clear the floors: ATR14 3.78 (2.04%), so the 9.00 risk from 183.50 = **2.38 ATR** ✓ and R:R = 20.00/9.00 = **2.22** ✓.
- decision: **leave it live, no amendment.** It was already amended yesterday and nothing has changed in one session. `XLV` is on the "recently recommended 2x" list; re-publishing a third time with identical levels is the anchoring the repetition guard exists to catch, not conviction. No candidate emitted.

## [06:38 ET] POSITION UPDATE — BCC — opened 2026-08-18, -14.8% — CLOSE (captured)
- decision: **close the position**, with a hard stop at 64.50 (just below the 65.00 140-day low) as the backstop. Captured via add_candidate.py as an amendment to the live `(BCC, buy)` row, entry restated UNCHANGED at 76.50 per the filled-entry rule.
- why, and it is arithmetic rather than a view: from the unamendable 76.50 entry, the 110.00 target against an honest 52.00 bear case is **1.37:1 against the 2.5 long_term floor**. It does not qualify to be held as a published long_term recommendation at any entry I am allowed to use.
- the invalidation, which this position never had: the thesis needed a falling long end. The 10y is 5.12%, the Fed last HIKED in Sept 2026, December is 91-95% priced for +25bp and 81bp of further hikes are priced over 12 months. The input reversed.
- Corroborated across the housing complex, not just BCC: **ITB 91.73 vs SMA200 95.51; XHB 99.09 vs SMA200 104.61** — both homebuilder ETFs below their 200-day averages. This is the sector, not one company.
- **Expect Phase 2d to flag or demote this on the R:R floor. That is the correct behaviour and must not be "fixed" by inventing a bear case above 63.10** — which is what a 2.5:1 would require from a 76.50 entry, and which would be a bear case 3% below a price the stock already trades at, i.e. not a bear case at all. If it is demoted to the watchlist, the demotion reason IS the recommendation.
- Flagged for synthesis: BCC ran **91 days with no stop**. PFE (63 days) and HII (35 days) are also open with `stop: None`. HII is +15.3% so it is not urgent, but PFE and the no-stop pattern are the same defect that let BCC run to -18% unchecked.

## [06:30 ET] POSITION UPDATE — PFE — opened 2026-08-18, +3.2% — HOLD, invalidation intact, no amendment
- 28.47. Fell 9.4% in nine sessions from the 11/05 high of 31.44. SMA20 29.68, SMA50 28.82 both above; SMA200 **27.01** below and still supporting. ATR14 0.8007 (2.81%). 400-day range 21.87-31.44.
- The published invalidation is specific and I checked the live limb of it: **"MEVPRO-1 fails in Q4 2026 and no replacement Phase III asset is in registration by end-2027"**. We are in Q4 2026, so this was the limb worth testing.
- **MEVPRO-1 has NOT read out.** ClinicalTrials.gov NCT06551324 shows overall status **ACTIVE_NOT_RECRUITING with the status verified October 2026** — enrolment complete, no efficacy data released. No Pfizer topline release or conference presentation found. Sources: https://clinicaltrials.gov/study/NCT06551324 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13203012/
- Design, for the record: ~600 patients, post-abiraterone mCRPC, enzalutamide ± mevrometostat 875mg BID, primary endpoint rPFS by blinded independent central review. The Phase 1/2 dose-expansion read median rPFS **14.3 months vs 6.2 months** (n=81). One stale summary lists primary completion as Dec 2025, which conflicts with the current status — treat that date as unreliable.
- decision: **hold, no amendment.** The 9.4% drawdown is a price move, not an invalidation; none of the three published invalidation limbs (FCF dividend coverage below 1.0x for two quarters, a dividend cut, or MEVPRO-1 failing with no replacement) has triggered. No candidate emitted.
- Live catalyst for synthesis to carry: **the MEVPRO-1 Q4 2026 readout window is still open**, so an open long_term position has an unresolved binary inside the next six weeks.

## [06:32 ET] AWAITING-ENTRY REVIEW — all 8, with marks
| Sym | Published entry | Last (11/17) | vs entry | Verdict |
| --- | --- | --- | --- | --- |
| GLD SELL | 406.77 (10/25) | **352.48** | entry 15.4% ABOVE mkt | **STALE — withdraw** |
| CVS BUY | 79.00 (11/05) | 85.81 | entry 7.9% BELOW mkt | **STALE — withdraw** |
| /MBTZ6 SHORT | 74075 (11/09) | unknown | unquotable | no futures quote this run |
| XLV BUY | 183.50 (11/17) | 185.24 | entry 0.94% below | live, unchanged (above) |
| HUN BUY | 9.00 (11/10) | 9.19 | entry 2.1% below | live, keep |
| ADM BUY | 68.80 (11/11) | 69.47 | entry 1.0% below | live, keep — but see below |
| LEN BUY | 79.50 (11/13) | 82.34 | entry 3.4% below | live, keep |
| CAG BUY | 14.40 (11/14) | 14.67 | entry 1.8% below | live, keep |

- **GLD is the lesson of the day, and it is about entry style, not direction.** The 10/25 SELL was *right*: gold has gone 406.77 → **352.48**, now **0.15% off its 140-day low of 351.96** and -19.4% off the 437.42 high, with SMA20 366.19 and SMA50 378.88 far above. The short needed a rally to 406.77 to fill; gold fell instead, so a correct call made nothing. An entry placed against the direction of your own thesis only fills when you are wrong. **decision: withdraw — do NOT re-pitch at 352.48.** Shorting 0.15% off a 140-day low is chasing, and the bounce risk is all of the remaining reward. No candidate emitted.
- **CVS: withdraw.** It stopped out 2026-11-04, was re-published at 79.00 on 11/05, then rallied to 90.71 by 11/16 without ever filling, and is 85.81 now — below SMA20 88.90 and SMA50 89.29 after a -3.1% day. The 79.00 level is 7.9% below market and is not a level today's tape is pointed at; chasing it upward would be the third CVS entry in a month.
- **ADM is the one to watch, and it is an entry-style problem too.** The 68.80 entry sits **0.01 above the 140-day low of 68.793**, with SMA20 73.93 and SMA50 79.24 far above in a steep downtrend. It will only fill on a break to new lows — the purest form of the pullback-entry trap the Performance tab now measures. Keeping the order because it is live and only 1.0% away, but flagging that a fill here is a fill into new-low momentum.
- **Tension declared rather than hidden:** I am closing BCC on a housing-and-rates argument while keeping the LEN buy order. They are genuinely different claims — LEN was published as 0.92x book with Berkshire buying $595m on the open market, and its own catalyst text says it is "NOT a call on the rate cycle turning". BCC's thesis *was* a demand call. Still, both are housing-levered, so if LEN fills, the book carries housing exposure the BCC close was meant to reduce. Synthesis should say so.

## [06:36 ET] EARNINGS RISK CROSS-CHECK — whole book against a 21-day calendar
Ran the 416-event finnhub calendar against all 15 open positions and all 8 awaiting-entry names.
- **Exactly one hit: DKS, 2026-11-23, consensus EPS $1.4242.** The calendar returns no `hour` for it, so bmo vs amc is **unconfirmed** — the 11/13 publication assumed 08:30 ET. Do not restate that time as verified.
- Nothing else in the book — BCC, PFE, KHC, OXY, AAL, HII, UNP, ABT, PYPL, RTX, XLU, ONON, TLT, ACM, HUN, ADM, LEN, CAG, CVS and the ETFs — has earnings inside 21 days. A useful negative: the book's only dated single-name event risk in the next three weeks is DKS.

## [06:38 ET] /MBTZ6 — awaiting entry, WITHDRAW — the same failure as GLD, for the same reason
- Published SHORT @ **74,075** on 2026-11-09. Bitcoin spot is **64,158** (-0.3% 24h, $30.0bn 24h volume) — source: coingecko via market_data.py.
- So the short entry sits **13.4% above** the market and never filled, while bitcoin fell ~13% exactly as the idea argued. **Two of the book's shorts (GLD, /MBTZ6) were directionally right and made nothing because their entries were placed above the market and only fill when the thesis is failing.** That is the mirror image of the pullback-entry problem the Performance tab tracks on longs, and it has now cost two correct calls in one month.
- decision: **withdraw.** Do not re-pitch a bitcoin short at 64,158, and in any case no futures quote is obtainable this run so a `/MBTZ6` entry price cannot be honestly stated. ETH 1,797.87, SOL 74.43 for the record.
- **This pattern is why today's IWM short is designed the way it is:** ideal 270.50 is only 0.54% above the 269.05 last price, the zone runs 268.50-273.00 so it includes the market and fills immediately, and the condition says do not chase below 266.00. The above-market ideal is a specific broken-shelf retest, not a reflex premium.

## [06:40 ET] REJECTED — ACM as a long_term re-entry at 80.53 — fails 2.5:1 by a wide margin
Tested deliberately, because `long_term` needs no ATR-floored stop and was the one lane that might have let the ACM thesis back in after the position closed at target. A closed position re-published is legitimately a new row, so this was a fair question.
- Valuation from the figures I read in the release, not from memory: 80.53 against the FY2027 adj EPS guide of **$6.15-6.35** (midpoint $6.25) is **12.9x**. Record backlog $28,016m (+13%), design backlog $26,115m, book-to-burn 1.3x FY, FY27 organic NSR growth 4-6%, adj EBITDA $1,350-1,390m. Normalised FCF is roughly $800m once the ~$500m of Construction Management cash use is added back to the ~$300m guide.
- Valuation anchor: 16-17x FY27 midpoint = **$100-106**; 18x = $112. Bear case: a guidance miss to ~$5.75 on a de-rate to 11x = **$63**.
- **The arithmetic:** (103 - 80.53) / (80.53 - 63) = 22.47 / 17.53 = **1.28:1** against a 2.5 long_term floor. Solving for the entry that would clear it gives **E ≤ 74.43** — below where ACM traded before the 11/17 gap, so it is not available.
- I could force a pass with an 18x target ($112) and a shallower $68 bear case — 31.47/12.53 = 2.51 — but that is tuning **two** inputs simultaneously until the floor is cleared, which is the exact failure `check_expectancy` and the red team exist to catch. **Refused.**
- This independently confirms the 06:08 decision not to re-enter ACM. The win is banked at the 77.22 target and the name is done for now. **Watchlist trigger: ACM becomes interesting again below 74.43**, which on the FY27 guide is 11.9x.

## [06:42 ET] CONSUMER — today's retail prints land AFTER this window, but the pre-release dispersion is itself a finding
LOW, TGT and TJX all report **before the open today (2026-11-18)**; PANW reports amc. Searched for actual results at 06:28 ET and **none were available or indexed yet**, so nothing here is a result — these are consensus and pre-release facts only.
- **TGT**: consensus ~$2.08 EPS on ~$26.50bn revenue (one source $2.07 / $26.49bn). The prior quarter was flattered by **$1.65 of tariff refunds**, so the underlying trend is what matters.
- **LOW**: consensus ~$2.88 EPS, **down from $3.06 a year ago**, on ~$22.36bn — and it goes in having **already LOWERED its full-year sales forecast**. Call at 9:00 ET.
- **TJX**: consensus ~$1.33-1.34 EPS on ~$15.82-15.85bn, revenue +4.8% — and it goes in having **already RAISED FY2027 pretax margin and EPS guidance**.
- Sources: https://www.newsquawk.com/headlines/newsquawk-daily-us-earnings-estimates-18th-november-2026---low-tgt-tjx-panw | https://www.benzinga.com/markets/equities/26/11/63277632/target-home-depot-tjx-and-lowes-report-earnings-as-their-stock-recoveries-stall | https://www.tjx.com/investors/financial-information/reporting-calendar
- **The dispersion is the signal, and it is coherent with the rest of today's work:** off-price (TJX) raising guidance into the print while home improvement (LOW) cuts its full-year sales outlook is a squeezed consumer **trading down**, with the housing-linked spend weak. That is the same picture as the BCC close (wood products into a 5.12% 10y) and as ITB/XHB both sitting below their 200-day averages. It is also the BURL thesis — which I rejected on geometry at 0.83:1, not on the fundamentals.
- **COVERAGE GAP, and a specific instruction for tomorrow's run:** these three prints, plus **WMT bmo on 11/19**, are the direct read-across to the **DKS print on 11/23** — the only earnings event in the entire book. They all land after this research window closed. Tomorrow's run should open by reading LOW/TGT/TJX/WMT actuals against the DKS position (entry 144.50, last 140.87, stop 129.00), because DICK'S own guidance cut on 2026-08-25 was blamed on the acquired Foot Locker unit rather than the core banner, and off-price strength vs home-improvement weakness bears directly on which of those two reads is right.

## [06:44 ET] WATCHLIST — consolidated for synthesis (7 entries, each with a trigger)
1. **J** (Jacobs Solutions) — Fully worked up; fails the swing floor at 1.64:1 from 158.23. *Trigger:* a pullback into the **149.70-151.00** shelf, where a 140.00 stop is 2.04 ATR and the 176.00 target gives 2.43:1; or, after the **11/23 amc** print, a hold above **162.00** on volume (resistance tested five times).
2. **AMTM** (Amentum) — Constructive pullback on declining volume into a **11/23** print, but the first real level is the SMA200 at **23.68**, giving only 1.28:1, and 2:1 needs a 25.06 target that is dead space. *Trigger:* a fill back toward the **20.15-20.53** base, where the SMA200 target clears 2:1; or a post-print hold above 23.68.
3. **BURL** (Burlington Stores) — Trade-down thesis is live and corroborated by TJX raising guidance, but 235.14 against the SMA50 at 252.79 is **0.83:1** with a 2.05-ATR stop. *Trigger:* a reclaim of the SMA50 at 252.79 that makes the 140-day high a reachable target, or a washout toward the 226.86 low that resets the geometry. Reports **11/23**.
4. **ACM** (AECOM) — Position closed at the 77.22 target on the 11/17 gap. Do **not** re-enter at 80.53; long_term is 1.28:1 there. *Trigger:* **below 74.43**, which is 11.9x the FY27 adj EPS guide of $6.15-6.35.
5. **GLD** — WITHDRAW the stale 406.77 SELL (gold is 352.48, entry 15.4% above market). *Trigger:* none. Do not re-short 0.15% off a 140-day low; revisit only on a rally back toward the SMA50 at 378.88.
6. **CVS** — WITHDRAW the stale 79.00 BUY (last 85.81, entry 7.9% below market, and this would be the third CVS entry in a month after the 11/04 stop-out). *Trigger:* a genuine re-underwrite, not a level.
7. **/MBTZ6** — WITHDRAW the stale 74,075 SHORT (bitcoin spot 64,158, entry 13.4% above market). *Trigger:* none, and no futures quote is obtainable this run in any case.

## [06:48 ET] ARITHMETIC VERIFICATION — both candidates, recomputed from source
**IWM sell_short (swing, etf):** entry 270.50, stop 284.50, target 238.69, ATR14 5.8061.
- risk 14.00 = **2.41 ATR** against the 1.8 ETF swing floor and the 2.25 "comfortable" level — clears both.
- R:R = 31.81/14.00 = **2.272** against the 2.0 swing floor ✓
- break-even / driftless baseline = 1/(1+2.272) = **30.6%**; claimed `win_probability` **0.42** → **11.4 points** of asserted edge, inside the 20-point "large claim" threshold.
- expectancy = 0.42×31.81 − 0.58×14.00 = **+5.24** per unit of risk ✓
- Conviction: four distinct evidence kinds are listed, which the table scores as a **5**. **I deliberately set 4.** The reason is specific: the `dated_catalyst` entry's *probability* (91-95%) comes from prediction-market and aggregator pages rather than a primary Fed document, and no `primary_document` or `valuation_anchor` underpins the idea at all. Validation will report "supported score 5" — that disagreement is intentional understatement, not an error to correct upward. The red team lowers conviction; it should not raise this one.

## [06:50 ET] BCC — why no `win_probability` is stated, and why that must not be "fixed"
This is a pipeline-mechanics decision with a real consequence, recorded so the red team does not reverse it.
- The honest estimate that 110.00 prints before 65.00, from a stock sitting at 65.14, is **well below** the 25.6% break-even baseline that 2.91:1 implies. That negative expectancy **is** the argument for closing.
- But `check_expectancy` treats a stated probability below the baseline as a **hard FAIL**, and a hard FAIL is demoted to the watchlist by Phase 2d. I confirmed that `positions_from_report` in `scripts/publish_sheets.py:518-520` iterates **only** `report["recommendations"]`. A demoted BCC therefore **never reaches the tracker**, the 64.50 stop is never applied, and the position goes on running with no stop — the precise defect this recommendation exists to fix.
- An absent `win_probability` is a **WARN**, not a FAIL (`validate_report.py:314-317`). So the field is omitted, the reasoning is stated in the thesis itself, and the stop reaches the position.
- **Do not "repair" this by inventing a win_probability above 25.6%.** That would be fabricating a figure to clear a floor, which is the single thing the 2b-2d phases exist to prevent. And do not widen or remove the 64.50 stop: it is 0.98% below the last price and 0.77% below the 140-day low *by design*, because the instruction is to exit.
- The pipeline cannot represent "close a losing position": every exit below an unamendable entry gives a negative reward, and a protective stop above entry inverts the R:R. A tight stop plus an explicit CLOSE instruction in `thesis` and `catalyst.action` is the closest honest encoding available.
- **Same structural gap, noted for the repo rather than acted on today:** HII is +15.3% (entry 262.00, last 297.44) with `stop: None`. A protective stop at 278.00, below the SMA50 at 281.04 and the 11/06 low of 281.34, would lock in roughly +6% — but it sits *above* the 262.00 entry, so |entry−stop| = 16.00 = **1.12 ATR**, failing the 2.0 floor, and the R:R goes negative. The only stop that satisfies the floor from entry is ~233.37, which is 21.5% below the market and protects nothing. **So a trailing protective stop on a filled winner is currently unrepresentable.** HII is therefore left unamended (hold, no change) rather than broken to fit the schema. PFE (63 days) also carries no stop; its published invalidation is intact, so it is left alone too.

## [06:30 ET] LOG CORRECTION — my own timestamps above drifted ahead of the wall clock
Called `date` and the real time is **06:30 ET**, not the 06:50 the preceding block is labelled. The timestamps from roughly the 06:18 block onward were estimated rather than read, and they run up to ~20 minutes fast. Everything recorded is in the correct **order** and no finding is affected, but a future run should not use these labels to judge pacing. Real elapsed at this point: **29 minutes** of a ~60 minute budget, started 06:01 ET. Checking `date` rather than trusting the estimate from here on, as the skill instructs.

## [06:33 ET] CORRELATION DISCIPLINE — three index shorts screened, ONE published, deliberately
Screened the same multi-window geometry that produced the IWM idea across XLK, XLY, XLB, XLF, SMH, QQQ, DIA, EEM and FXI. Three index shorts cleared the floors on the arithmetic alone:
| | close | ATR% | stop 2.0ATR | target (level) | distance | R:R | position vs MAs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **IWM** | 269.05 | 2.16 | 280.66 | 238.69 (180d low) | -11.3% / 5.5 ATR | 2.27 | **below all 3, clustered 278.12/279.51/279.79** |
| QQQ | 656.95 | 3.05 | 697.02 | 555.60 (180d low) | -15.4% / 5.1 ATR | 2.53 | below all 3, spread 689.58/682.59/715.49 |
| DIA | 507.31 | 1.69 | 524.45 | 450.44 (180d low) | -11.2% / 6.7 ATR | 3.32 | **sitting ON the SMA200 at 507.64** |
- **Only IWM is published.** All three are one bet — US equity beta against the rate path — and `config/strategy.md` caps ideas sharing a driver at 3 while warning that "eight ideas that are all one bet on semis is one idea with extra steps". Publishing three index shorts would be that error with a straight face, and it would read as three independent confirmations of the same view.
- **Why IWM and not the better raw ratio.** DIA has the best arithmetic (3.32) and the lowest ATR, but it is **shorting into support**: 507.31 against an SMA200 at 507.64 is a short entered at the one level most likely to hold, and its 450.44 target is a 180-day low last seen around March 2026. QQQ's target is 15.4% away with its MAs spread over 33 points, so there is no tight line that defines failure. IWM is the only one of the three that has **already broken down** — below a cluster of all three MAs sitting within 1.67 points (0.29 ATR) of each other, at a 120-session low — and it is the one where the macro argument is specific rather than generic beta, since small caps carry the most floating-rate and near-dated debt. A confirmed break beneath a tight, falling wall beats a better ratio into support.
- For the record, the rest failed outright: **EEM** 58.27 short 1.85 and long 4.17 on a +22.8% move (both fail — one on the floor, one on reachability); **FXI** 32.88 short 1.74, its 31.19 deep low only 5.1% away despite a 1.48% ATR; **XLF** 57.07 long 1.36 / short needs a 16.5%-away target; **XLB** 50.84 long 1.72, price pinned on its SMA50/SMA200 at 50.88/51.26; **XLY** 117.10 long 1.46; **XLK** 163.26 and **SMH** 460.10 are 2.22% and 3.21% off their 60-day lows after -19.7% and -31.5% drawdowns — too extended to short and with no basis to call a bottom.

## [06:35 ET] REJECTED — MDT — a 2:1 target would sit ABOVE the 400-day high; fourth confirmation of the structural finding
- Genuinely good setup on every axis except the one that counts: 102.32, ATR14 2.5833 (**2.52%**, the lowest of any single stock screened today), above SMA20 99.35, SMA50 94.10 and SMA200 88.26, ADV$1.99bn, **earnings 2026-11-24 bmo** on the fetched calendar, and in the healthcare complex that is this correction's leadership.
- Stop discipline: 2.0 ATR = 5.17, so a stop at 96.50 — below the SMA20 and above the SMA50 — is risk 5.82 = **2.25 ATR** ✓.
- 2:1 then requires a target of **113.96**. Multi-window highs: 60d 106.20, 120d 106.20, 180d 106.20, 250d 106.33, **400d 106.33**. So 113.96 is **7.2% above the highest price MDT has traded in 400 sessions, with no structure whatsoever** between. Dead space. Rejected.
- Also noted: ABT (open, medtech) and XLV (awaiting entry) already give the book two healthcare positions, so MDT would have sat at the 3-per-driver correlation cap alongside a near-identical medtech name.
- **This is the fourth independent confirmation** (J, AMTM, BURL, MDT) that a momentum long near its highs cannot clear 2:1 against a floored stop without inventing a target. It is a property of the arithmetic, not of today's names.

## [06:37 ET] MARKET CONTEXT — for synthesis
- **Regime: a hiking cycle into firm inflation with a solid labour market.** Target range 3.75-4.00%, last move a +25bp HIKE in Sept 2026, October a hold on a 10-2 vote with two dissents FOR a hike, and **December 8-9 priced 91-95% for another +25bp** with OIS carrying **+81.1bp over twelve months**. Oct CPI +0.4% m/m headline / +0.3% core; FRED CPIAUCSL +0.35% m/m; unemployment 4.1% (down from 4.2%).
- **Curve:** 10y **5.12%**, 2y **4.83%**, effective fed funds **3.88%**, 10y-2y **+0.30**. The 2y sitting ~95bp above effective funds is the front end pricing the hikes directly.
- **Tape:** 11/17 was broadly risk-off. Of 15 open positions only RTX (+1.60%), TLT (+0.21%) and ACM (+11.08%) closed green. Equity indices are below their moving averages across the board — IWM at a 120-session low, QQQ and XLK below all three MAs, SMH -31.5% off its high, XLK -19.7%.
- **The deflating-asset picture, which is the day's most striking cross-asset read:** gold **-19.4%** off its high and at a 140-day low (GLD 352.48), copper miners **COPX -35%**, metals **XME -34%**, ADM at a 140-day low, DE breaking below its SMA20/SMA50, housing weak (ITB and XHB both below their 200-day averages, BCC at a 140-day low). Commodities and cyclicals are deflating **while** services inflation keeps the Fed hiking — a late-cycle tightening pattern, and the reason a duration long is not the hedge it looks like.
- **Leadership:** healthcare (XLV -3.7% off its high, SMA50 175.74 well below price) and staples (XLP -2.2% off its high). Infrastructure design is the standout idiosyncratic strength — ACM +11.08% on record backlog, J +40.2% over 6m.
- **Honest skew to declare:** the one new idea published today is a **short**, and the only other entry is a **close**. That is not a house view imposed on the tape; it is what survived the floors. See the 06:27 and 06:35 blocks — four full workups of long ideas (J, AMTM, BURL, MDT) were rejected on arithmetic, not on sentiment.

## [06:42 ET] CAPTURED — CVS buy — long_term, conviction 5, R:R 2.77 — AND THIS SUPERSEDES THE 06:32 "WITHDRAW"
At 06:32 I listed CVS as "STALE — withdraw", with the trigger "a genuine re-underwrite, not a level". **I then did the re-underwrite, and it changed the answer.** The 79.00 entry published 2026-11-05 was approximately right; what it lacked was a defended valuation behind it. It now has one.
- **Primary document read** — Q3 2026 release, Exhibit 99.1 to the 2026-11-04 8-K: https://www.sec.gov/Archives/edgar/data/64803/000006480326000107/cvs_ex99x1q3-26.htm
  - Total revenues **$108.4bn, +5.4%**; Q3 adj EPS **$2.09**, GAAP diluted **$1.68**; nine-month operating cash flow **$15,318m**.
  - **HCB medical benefit ratio 91.3% vs 92.8%** a year earlier — a 150bp improvement in the exact metric that broke this stock.
  - **FY2026 guidance RAISED**: adj EPS to **at least $8.20** (was $7.90-8.10); GAAP to at least $6.98 (was $6.84-7.04); **operating cash flow to at least $15.5bn, from at least $11.5bn** — a $4bn raise in a single quarter.
  - **No 2027 financial guidance of any kind** is given. The only 2027 datapoint is operational: >69% of Aetna MA members in 2027 plans rated 4 stars or higher. That absence is in `key_risk`, because the most important number for this idea does not yet exist.
- **Valuation anchor, with the method shown:** 85.81 / $8.20 = **10.5x** guided adj EPS (12.3x the GAAP $6.98). Target **13x × $8.20 = $106.60**. The defence is that the tape already paid it — CVS traded **110.68** within the last 140 sessions, which is 13.5x the same $8.20. The target is below a multiple the market has granted this year, not one it must discover. target_2 114.80 = 14x. Bear case **67.00** ≈ 9.5x a relapsed $7.00.
- **Entry 77.50, zone 76.00-78.00** in thirds at 78.00 / 77.00 / 76.00. Solved, not guessed: the 2.5 floor breaks above **78.31**, so every fill in the zone clears it — 76.00 → 3.40, 77.00 → 2.96, 77.50 → **2.77**, 78.00 → 2.60, while 78.50 → 2.44 FAILS and the 85.81 market price gives **1.11**. The zone also brackets the 140-day low of 77.33.
- Baseline at 2.77:1 is 26.5%; claimed `win_probability` **0.45** → 18.5 points of asserted edge, just inside the 20-point threshold. Expectancy **+7.32** per unit of risk.
- **Positioning:** President **Prem S. Shah bought 23,855 shares open-market (code P) at $83.895 on 2026-11-06 for $2,001,315** — two days after the print, 2.3% from today's price. Adjusted EPS surprise record **+25.25% / +37.95% / +15.80% / +8.80%** across the last four quarters, which is why "at least $8.20" reads as a floor. Analyst revisions **improving**, 87.5% bullish (+2.7 pts), 8 strong buy / 20 buy / 4 hold / **0 sell**. Honest offset carried in the counter-argument: 8 sells totalling $352.7m against that one buy.
- Four distinct evidence kinds (primary_document, valuation_anchor, positioning, technical_level) → conviction **5**, which is the first 5 this report has published since the LEN idea and is earned on the count rather than on enthusiasm.
- **Declared risks:** (1) the zone is **9.7% below the market and may never fill** — the GLD and /MBTZ6 lesson from this same run, stated in `key_risk` rather than discovered later; (2) this is the **third CVS entry in a month** after the 2026-11-04 stop-out and the unfilled 11-05 re-entry, which is exactly the pattern the repetition guard exists to catch — the defence is that what changed is not the level but that a primary document and a valuation now stand behind it; (3) it is NOT rate-path dependent, which makes it the one idea today uncorrelated with the IWM short.

## [06:40 ET] RESEARCH COMPLETE
- **candidates: 3 distinct symbols** (5 lines in candidates.jsonl; BCC was captured three times and only the last counts — the first two were superseded as the framing was corrected, first to the published 65.00 bear case and then to drop `win_probability`).
  1. **IWM `sell_short`** — swing, conviction 4, entry 270.50 (zone 268.50-273.00), stop 284.50 (2.41 ATR), target 238.69, R:R **2.27**, wp 0.42 vs a 30.6% baseline, 2%. The one genuinely new trade idea. `requires_margin: true`.
  2. **CVS `buy`** — long_term, conviction 5, entry 77.50 (zone 76.00-78.00), no stop, bear case 67.00, target 106.60, R:R **2.77**, wp 0.45 vs a 26.5% baseline, 4%. Uncorrelated with the above.
  3. **BCC `buy`** — long_term, conviction 2, an AMENDMENT TO CLOSE: entry unchanged 76.50, stop 64.50, position_size 0%. Not a new position.
- **Driver spread:** one rate-path short, one idiosyncratic healthcare long, one exit. No correlation-cap breach.
- **Why only one new idea, stated plainly so it does not read as a thin run:** four long setups were fully worked up and rejected on arithmetic — **J** (1.64:1), **AMTM** (1.28:1), **BURL** (0.83:1), **MDT** (2:1 target would sit 7.2% above the 400-day high). Two more index shorts (**QQQ** 2.53, **DIA** 3.32) cleared the floors but were deliberately NOT published because all three are one bet on equity beta. See the 06:27 structural block: with the stop floored at 2.0 ATR, clearing 2:1 needs the target ≥4 ATR away, which in a 4-6% ATR tape means a 15-20% move and therefore, almost always, a target in dead space above real resistance. The floors are rejecting swing equity longs close to categorically today. That is them working.
- **coverage gaps:**
  - **No index, VIX, DXY, gold-spot, WTI or futures price is available this run.** Yahoo returned HTTP 429 on every attempt and finnhub refuses indices ("Market data subscription required for CFD indices"). SPX, NDX, DJI, RUT, VIX, /ES, /NQ, DXY, the 10y quote, gold and WTI all came back `ok: false`. **Consequence: no futures idea was published, and the IWM short is a documented substitution for the `/M2K` contract `config/universe.md` prefers** — naming a `/M2KZ6` price would have been fabricated. The stale `/MBTZ6` short also could not be marked.
  - **No event contract is quotable.** `events` returned count 0 for "FOMC", "interest rate", "recession", "inflation" and "Bitcoin"; "Fed" returned 17 Kalshi `KXMVECROSSCATEGORY` sports tickers matched on a substring, every one with null bid, ask, last and volume. So none was published, despite the skill asking for them actively.
  - `short` (short interest / days to cover) **failed on every symbol tried** — nasdaq `api.nasdaq.com` read timeout on J and AMTM. No short-interest evidence anywhere in today's work.
  - `implied` (options-implied move) **failed** — Yahoo options returns HTTP 401. So no idea today was checked against what the options market prices, including IWM.
  - **Today's retail prints land after this window.** LOW, TGT and TJX all report bmo today and were not available or indexed at 06:28 ET; PANW reports amc. These plus **WMT bmo 11/19** are the direct read-across to **DKS on 11/23**, the only earnings event in the entire book. Tomorrow's run should open there.
  - `sma200` is null on any symbol fetched with a 140-day window; where a 200-day average mattered (AMTM, MDT, IWM, CVS) a 400-day fetch was used instead. Worth knowing before trusting a null.
- **sources that failed:** Yahoo Finance chart API (429, all index/macro symbols), Yahoo options API (401), finnhub index endpoints (subscription), `api.nasdaq.com` short interest (read timeout), Kalshi event search (0 results or null prices).
- **Positions: all 15 open reviewed and decided, all 8 awaiting-entry marked.** ACM **hit its 77.22 target** on the 11/17 gap open (+20.7%) and is closed — take the win, do not re-enter below 74.43. BCC closes. ONON holds with its stop deliberately NOT widened at 0.65 ATR from the market. DKS holds into its 11/23 print. PFE holds — MEVPRO-1 is still ACTIVE_NOT_RECRUITING, so its invalidation is intact and the Q4 2026 readout window is still open. GLD, CVS-as-a-swing and /MBTZ6 are stale orders to withdraw — though the CVS withdrawal was **superseded** by the re-underwrite at 06:42, which is the one place in this log where a later block reverses an earlier one.
- **Flagged for the repo, not acted on:** a trailing protective stop on a filled winner is currently unrepresentable — HII is +15.3% with no stop, and any stop that protects the gain sits above the entry, which inverts the R:R and fails the ATR floor measured from entry. See the 06:50-labelled block.
