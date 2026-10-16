# Research log — 2026-10-16

## [06:02 ET] MACRO — rates, policy, regime
- FRED DGS10 10y Treasury **5.19%** (2026-10-14), prev 5.21% — source: https://fred.stlouisfed.org/series/DGS10
- FRED DGS2 2y **4.82%** (2026-10-14), prev 4.79% — source: https://fred.stlouisfed.org/series/DGS2
- 10y-2y spread **+0.33** (2026-10-15), prev 0.37 — curve flattening at the margin — source: https://fred.stlouisfed.org/series/T10Y2Y
- Fed funds effective **3.88%** (2026-10-14), unchanged — source: https://fred.stlouisfed.org/series/DFF
- UNRATE **4.2%** (Sept 2026), prev 4.1% — labor softening — source: https://fred.stlouisfed.org/series/UNRATE
- CPIAUCSL **336.298** (Sept 2026) vs 334.131 (Aug) = **+0.65% m/m**, an annualized ~8% run rate. Hot. — source: https://fred.stlouisfed.org/series/CPIAUCSL
- Regime read: 10y above 5% with a 3.88% policy rate and rising unemployment = term-premium/inflation-driven long end, not a growth-driven one. That is a headwind to long-duration equity and to rate-sensitive sectors, and supportive of real assets.
- TLT proxy (bonds_20y) **79.97**, +1.37% on 2026-10-15 close — source: scripts/market_data.py macro
- DATA GAP: Yahoo returned HTTP 429 for every index/VIX/DXY/gold/WTI quote this morning (^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES, NQ, DX-Y, ^TNX, GC=F, CL=F all ok:false). Finnhub refuses CFD indices without a subscription. So **no index level, no VIX, no DXY, no gold, no crude price is available to this run** and none will be stated.

## [06:03 ET] CALENDAR — dated events inside 5 sessions (fetched Finnhub earnings calendar)
- **Fri 2026-10-16 (today) bmo**: TFC, MTB, RF, CFG, TRV — regional banks + insurer. Day 3 of bank earnings.
- **Mon 2026-10-19**: GE bmo (EPS est 2.0576), STLD amc (5.508), CLF bmo (0.1944), FITB bmo, ZION amc, WAL amc, WTFC amc, CCK amc, RLI amc, SFBS amc
- **Tue 2026-10-20**: NFLX amc (0.8391), GM bmo (3.7208), RTX bmo (1.7938), NOC bmo (7.2565), MMM bmo, COF amc, CB amc, ISRG amc, HAL bmo, PM bmo, UAL amc, ALK amc, KEY bmo, SYF bmo, EFX bmo, MSCI bmo, EWBC amc, OZK amc, HAS bmo, GPC bmo
- **Wed 2026-10-21**: ABT bmo (1.4302), CME bmo, BKR amc, CCI amc, CMA, CATY amc, CASH amc, BKU bmo
- source: scripts/market_data.py earnings --days 8 (Finnhub)
- Two of these land directly on the book: **GE reports Mon 10-19 bmo** (open position, entry 308) and **STLD reports Mon 10-19 amc** (awaiting entry @ 245.5).

## [06:04 ET] POSITION UPDATE — GE — opened 2026-10-12 @ 308, last 312.00 (+1.3%)
- decision: **hold, levels unchanged** (target 341, stop 292)
- why: Q3 earnings Mon 2026-10-19 bmo (fetched Finnhub calendar, EPS est 2.0576) is new information, but it argues for no change rather than a change. Entry cannot be re-cut on a filled position; stop 292 is 2.31 ATR (ATR14 6.93) and sits below the 296.61 low of 2026-10-08, so it is a real level. Widening it to cover an earnings gap would drop R:R from 2.06 to 1.43 and fail the swing floor — so the correct answer is the smaller size, not a wider stop.
- caveat stated in the candidate: a 07:00 ET pre-open gap can clear 292 without trading there, so realized risk may exceed the 16-point stated risk.
- action: captured via add_candidate.py as an UPDATE
- context: GE 312.00, SMA20 312.90, SMA50 331.65, -19.76% off the 388.84 120d high.

## [06:05 ET] DATA GAPS so far
- `market_data.py implied` is dead this morning — Yahoo options returns **HTTP 401 Unauthorized** for GE and NFLX. No idea today can cite an options-implied move.
- `market_data.py macro` index/VIX/DXY/gold/WTI all failed (Yahoo 429, Finnhub CFD subscription). FRED series all returned.
- `market_data.py short NFLX` — api.nasdaq.com read timeout.
- `market_data.py events "Fed"` returned **0 markets** from Kalshi.
- Equity/ETF quotes via Finnhub are working and are **2026-10-15 16:00 ET closes** — the previous close, which at 06:00 ET is the freshest honest price, not stale data.

## [06:08 ET] NEWS — why regional banks are 12-17% off their highs
- Risk Quantum (Risk.net), Q2 2026: aggregate **negative AOCI across seven US regional banks rose $951M, +8% q/q, to $12.9bn**, explicitly attributed to rising long-term rates — source: https://www.risk.net/risk-quantum/7963911/aoci-losses-widen-at-us-regional-banks
- Mechanism: with DGS10 at 5.19% the AFS/HTM marks get worse, so tangible book shrinks even when credit is fine. Regions Financial's Q2 10-Q puts net charge-offs at $102M = **0.42% of average loans, down year over year** — source: https://www.sec.gov/Archives/edgar/data/0001281761/000128176126000055/rf-20260630.htm
- So the de-rating is a **rates/book-value** story, not (yet) a credit story. That is a reason to be *careful* buying the dip, not a reason to buy it: the thing marking them down has not reversed.
- Uniform, not idiosyncratic — every one of these closed 2026-10-15 below its SMA50:
  FITB 50.35 (SMA50 53.66, -15.4% off high) | ZION 63.01 (66.53, -14.1%) | KEY 19.94 (21.33, -17.1%) | COF 198.86 (208.42, -12.8%) | SYF 74.04 (76.03, -9.6%)
- All five bounced 2026-10-15 (XLF +1.38% to 55.27). One green day inside a downtrend is not a turn.
- **Correlation note:** `XLF` is already an open position on this driver and has been recommended 4x in ten days. Bank earnings is therefore a driver at capacity — no new regional-bank long gets captured today on these grounds alone.

## [06:09 ET] REJECTED — FITB / ZION / KEY / COF / SYF dip-buys — the 5.19% long end that caused the de-rating has not turned, driver already carried by the open XLF position (4x recommended), and all five print Mon/Tue so any entry is a coin flip on a gap

## [06:09 ET] DATA GAP — event contracts unavailable today
- `market_data.py events` returned `ok: true, count: 0` for all seven of **Fed, CPI, inflation, S&P, Bitcoin, recession, unemployment, government shutdown**. The Kalshi source is reachable and returning an empty market set.
- Consequence: **no event-contract idea can be captured today**, because no implied probability could be fetched and the universe rules require stating the market's price against mine. An event contract priced from memory is exactly the fabricated number the non-negotiables forbid.

## [06:10 ET] REJECTED — CCJ — evidence is actively negative, not merely thin
- CCJ printed its 120-day LOW at 78.55 on 2026-10-15 and closed 83.23, +4.4% off the session open (79.70) on 5.47M shares vs ~2.4M typical. That reversal bar is real and is new information since yesterday's report — yesterday's CCJ was demoted by validation for expectancy (20% claimed vs 22% break-even at 3.57:1).
- But the fundamentals screened badly on every axis fetched: analyst revisions **deteriorating -3.9pp** (81.8% bullish, trend frozen at 5/13/4 for four months), earnings **3 misses in the last 4** including **-52.7%** (Jun-26) and **-77.2%** (Sep-25), **zero** insider open-market buys in six months, and -40.79% vs SPY over six months.
- Geometry fails independently: an honest stop below the 78.55 low (76.50) against a breakout entry at 84.80 is 8.30 = 2.39 ATR, but the nearest documented resistance is the 94.24 SMA50 / 94.57 high of 2026-10-06, which is only **1.16:1**. Clearing 2.0 would require a target above all mapped overhead — the reverse-engineering `config/strategy.md` forbids.
- source: https://finnhub.io/api/v1/stock/recommendation?symbol=CCJ , https://finnhub.io/api/v1/stock/earnings?symbol=CCJ , https://finnhub.io/api/v1/stock/insider-transactions?symbol=CCJ

## [06:10 ET] REJECTED — URA — same uranium driver as CCJ, and worse: -12.69% 1m / -34.65% 6m vs CCJ's -8.44% / -30.8%, 120-day low 34.31 printed 2026-10-15. An ETF also has no insider, surprise or revision evidence available at all, so it cannot score above conviction 2 on a technical bar alone.

## [06:11 ET] REJECTED — NFLX — 72.61, -33.35% off its 108.945 high with Q3 Tue 2026-10-20 amc. Every fetched evidence axis is negative: **0 of 4** earnings beats, revisions **deteriorating -3.5pp** (74.1% bullish, strong_buy 16->14 and buy 30->29 since July), zero insider buys. A 33% de-rating with a deteriorating analyst book and no beat record is a broken story, not a cheap one.

## [06:12 ET] NEWS — EFX +7.25% on 2026-10-15, and why it still does not qualify
- EFX closed **161.26, +10.90 (+7.25%)** from 150.36, opening 153.24 (gap) and closing 0.14% off the session high 161.49 on 1.99M shares — source: https://finance.yahoo.com/quote/EFX/
- Driver per Quiver Quant: no single confirmed catalyst; the move tracks a run of mortgage product launches — **Mortgage Ultimate on 2026-10-13** and **Mortgage Score Select on 2026-10-08** — source: https://www.quiverquant.com/news/Equifax+stock+jumps+as+mortgage+product+momentum+and+upcoming+earnings+draw+attention
- Morgan Stanley maintained **Overweight 2026-10-13 and cut its target 225 -> 205** — source: https://www.quiverquant.com/news/Equifax+stock+jumps+as+mortgage+product+momentum+and+upcoming+earnings+draw+attention
- Q3 **2026-10-20** confirmed on both the fetched Finnhub calendar (bmo, est 2.2286) and Yahoo — source: https://finnhub.io/api/v1/calendar/earnings
- Evidence is genuinely good: **4 of 4 earnings beats**, revisions **improving +3.3pp** to 70.0% bullish. GuruFocus puts P/E TTM 28.3x against a 5-year median 43.8x (third-party opinion, not a fetched fundamental) — source: https://www.gurufocus.com/news/9126754/is-it-too-late-to-buy-equifax-inc-efx-after-72-rally-gf-value-says-undervalued
- Structure: the 161.26 close **reclaimed the entire September breakdown shelf** (157.64-162.53 on 09-18 to 09-22) after bottoming at 137.01 on 09-30 — +17.6% in eleven sessions.

## [06:13 ET] REJECTED — EFX — the right business, the wrong morning
- ATR14 4.6896. The swing stock floor of 2.0 ATR is 9.38 points, so from any entry near 161.50 an honest stop sits at or below 152.12 and a 2:1 target sits at or above **180.26**.
- The only documented overhead level is the **167.88 SMA50**, 4.1% up. 180.26 is 7.4% beyond it, and the 20 bars the history endpoint returns do not map anything between 168 and the 200.09 high, so a 180 target would be a number invented to clear the floor rather than a level read off the tape.
- Compounding it: buying the session after a +7.25% gap that closed on its high, two sessions ahead of the print, is chasing. The gap 150.555-153.24 is unfilled; a retest there is the entry that would work, and a stop 2.0 ATR below *that* (140.20, under the 140.84 low of 10-07) is defensible — but then the target is still unanchored.
- WATCHLIST, not a trade. Trigger: a daily close above the 167.88 SMA50, which would both confirm and finally put a mapped level underneath an entry.

## [06:14 ET] LEVELS + CAPTURE — ABT (new, conviction 4)
- 104.68, ATR14 2.3644. Entry 103.60 (zone 102.80-104.80), stop 97.00 (below the 97.20 low of 10-08 and 97.39 of 10-05), target 117.34 (120-day high).
- Risk 6.60 = **2.79 ATR** (floor 2.0); reward 13.74 → **2.08:1** (floor 2.0); baseline win prob 1/(1+2.08) = 32.5%, claimed 38%.
- Insiders are the reason this is a 4 and not a 3: **3 distinct open-market buyers, $1,301,477** — Starks 10,000 @ 92.6537 (04-27), Boudreau 2,200 @ 91.50 (04-23), Stratton 2,000 @ 86.82 (05-07) — source: https://finnhub.io/api/v1/stock/insider-transactions?symbol=ABT
- Revisions improving +5.2pp to 75.8% bullish, strong_buy 10→12 over four months, zero sells in any month — source: https://finnhub.io/api/v1/stock/recommendation?symbol=ABT
- The "1 of 4 beats" screen reading is misleading and worth recording: all four prints landed within ±1.4% of estimate (+1.38%, -0.45%, -0.75%, -1.06%). ABT is a tight guider, not a chronic misser.
- Honest negative, stated in counter_argument: ABT lags XLV on every window — 1m -3.34%, 3m -6.02%, 6m -11.21%.
- Q3 2026-10-21 bmo, est 1.4302 — source: https://finnhub.io/api/v1/calendar/earnings

## [06:14 ET] LEVELS + CAPTURE — CVS (new, conviction 4)
- 92.58, ATR14 2.2738. Entry 93.00 **above the market** (zone 92.70-94.20, above the 92.64 high of 10-15 and the 91.80 SMA50), stop 85.40, target 110.68 (120-day high).
- Risk 7.60 = **3.34 ATR**; reward 17.68 → **2.33:1**; baseline 30.0%, claimed 38%.
- The signal: 10-15 closed 92.58 through the 91.8022 SMA50 on **14.27M shares, the heaviest of the window** (~1.5x the preceding average), after 85.69 on 09-30.
- Stop 85.40 sits under a real three-session shelf — 85.80 (10-09), 86.045 (10-12), 86.125 (10-13) — and under the 85.42 low of 09-30.
- Relative strength is the interesting split: **+10.57% vs SPY over 6m but -17.69% over 3m**, i.e. a drawdown inside an uptrend. Revisions +3.0pp to 84.8% bullish, 4 beats in 4 quarters.
- Q3 **2026-11-04 bmo, est 1.66** — source: https://finnhub.io/api/v1/calendar/earnings
- Deliberately an entry ABOVE the market: per CLAUDE.md the first month ran 31 pullback entries against 1 breakout with a 42% fill rate, and the fills selected for the ideas already failing.

## [06:15 ET] REJECTED — ELV — the best evidence on the tape and still no trade, for the second day running. 428.43 with the 436.24 high only **7.81 points = 0.74 ATR** overhead (ATR 10.5738). Evidence is the strongest screened today: revisions **+6.9pp** improving, **4/4 beats**, **3 insider open-market buys**, +51.68% off its low, 388.82→428.43 in eleven sessions. A 2.0 ATR stop puts risk at 21.15, so a 2:1 target is 470 — 7.7% above the period high, anchored on nothing. Watchlist; the geometry, not the thesis, is what fails.

## [06:15 ET] REJECTED — BMY — 60.57, revisions +4.0pp and 4/4 beats, but the tape contradicts it: below both the 60.80 SMA20 and the 63.59 SMA50, and 10-15 printed 62.25 and gave back 1.68 to close 60.57, a rejection rather than a reclaim. Analyst book is also only 42.9% bullish. No entry worth placing under a failed intraday high.

## [06:15 ET] REJECTED — HAL / SLB / BKR — energy services. `XLE` is already an open position (+5.8%) and has been recommended 3x in ten days, so the energy driver is near the correlation cap before any of these is considered. BKR separately disqualifies on evidence: 4/4 beats but revisions **deteriorating -5.3pp**, and it is below both SMAs 22.7% off its high.

## [06:16 ET] MACRO — what 2026-10-15 actually was, and why it colours every finding below
- It was a **single-session rotation out of AI/tech into beaten-down laggards**, not a broad rally. XLY +1% while SPY slipped; Dow up, Nasdaq trimming losses — source: https://247wallst.com/investing/2026/10/15/nike-climbs-5-as-beaten-down-consumer-names-catch-a-bid-lululemon-rises-4-on-holding-dips/ , https://finance.yahoo.com/markets/live/stock-market-today-dow-sp-500-rise-nasdaq-trims-losses-as-treasury-yields-sink-153611834.html
- Fetched closes consistent with that: SPY 771.79 **+0.28%**, QQQ 728.00 **-0.13%**, IWM 275.08 **+1.37%**, XLV 177.19 +1.86%, XLF 55.27 +1.38%, SLV 51.92 +3.39%, NEM 115.79 +3.79%, GLD 382.71 +1.79%, KRE 69.75 +1.77%, NKE +5.21%, LULU +5.31%, EFX +7.25%, CCJ +2.16%, URA +1.63% — against XLE 66.56 **-1.58%**, XLU 41.65 -0.17%, EWZ 41.58 -2.39%.
- **This is the single most important caveat on today's report.** Every "capitulation reversal" and "50-day reclaim" found this morning — CVS, ABT, EFX, CCJ, URA, SLV, NEM, MU, LULU, NKE, the banks — is the same one-day event seen through eleven tickers. They are one observation, not eleven, and none of them has a second day of confirmation.

## [06:17 ET] POSITION UPDATE — MU — opened 2026-09-18 @ 960, **STOPPED OUT 2026-10-15**
- The prior-context table still lists MU open at 914.13 because it was built from the 2026-10-14 close. The 2026-10-15 bar was **871.575 / 931.65 / 858.00 / 931.24 on 39,095,130 shares** — the session low of 858.00 is 12.00 **through** the published 870.00 stop.
- decision: **closed at the stop**, about -9.4%. Not re-entered.
- MU then reversed 8.5% off that low to close at the high of the day on the heaviest volume of the window. Declined anyway: nothing fundamental was fetched, MU is still -25.8% off its 1255.00 high and below both the 1039.85 SMA20 and the 983.17 SMA50 after 1097.39 (10-01) -> 858.00 in ten sessions, and buying it back the morning after being stopped out is revenge rather than evidence.
- action: captured via add_candidate.py as a closure notice with `wait: true` and an explicit do-not-re-enter condition.

## [06:17 ET] POSITION UPDATE — NKE — short opened 2026-09-08 @ 38.40, last 37.14 (+3.3%)
- decision: **hold, target 32.10 and stop 41.00 unchanged**, plus a new falsifiable exit rule: two consecutive daily closes above the **37.643 SMA50** means cover without waiting for 41.00.
- why: the 5.2% rally carried **no company-specific news** — two independent write-ups attribute it to rotation out of AI into beaten-down consumer. But it cleared the 35.38 SMA20 on 46.4M shares (2.3x recent) and stalled 0.50 under the SMA50, so the level test is the honest way to hold it. — source: https://www.fool.com/investing/2026/10/15/why-nike-stock-was-climbing-today/
- action: captured.

## [06:17 ET] POSITION UPDATE — LULU — short opened 2026-09-08 @ 100.61, last 99.09 (+1.5%)
- decision: **hold, target 77.00 and stop 112.00 unchanged**; cover on a daily close above the 107.294 SMA50.
- why, and this one is less comfortable than NKE: LULU's 5.3% move **did** carry company items — a Ganni collaboration and leadership-overhaul optimism, with one source saying the catalyst is not fully clear. Offsetting it: volume was only ~1.2x average against NKE's 2.3x, and the rally failed 8.20 below the SMA50. It traded 100.40 intraday, above the 100.61 entry, so the short has already been through break-even once. — source: https://www.tipranks.com/news/catalyst/lululemon-surges-as-bold-fashion-tie-up-ignites-hopes
- action: captured.

## [06:17 ET] POSITION UPDATE — SMMT — opened 2026-10-09 @ 17.10, last 15.37 (-10.1%)
- decision: **hold, stop 14.40 unchanged** — and state plainly what that stop now is: ATR14 is 1.1463, **7.46% of price**, so 14.40 sits **0.85 ATR** below the close. It is inside one ordinary day and will probably be taken by noise rather than by news.
- why not widen it: the entry is filled and the stop is published. Re-cutting it four sessions in would make every other stop in this report advisory.
- what changed: 2026-10-13 broke the base, 16.79 -> 15.465, closing 15.52 on 7.13M (~1.5x), below the 15.6583 SMA50. 10-14/10-15 held 15.04-15.55. Q3 is 2026-11-11 (est -0.2928), so nothing dated stands between here and the stop.
- action: captured, 1% lottery-ticket size, conviction 2 with the thinness named.

## [06:18 ET] DATA GAP — no futures idea can be published today
- `market_data.py macro` could not return a price for **es_futures or nq_futures** (Yahoo 429), and there is no other configured source for a CME contract. Gold and WTI failed the same way.
- `config/universe.md` requires naming the contract month and every futures idea carries a mandatory stop, both of which are prices. Stating `/MESZ6` or `/M2KZ6` levels I did not fetch would be fabricating exactly the kind of number that gets traded on, so **no futures candidate is captured**. The rotation read below would otherwise have pointed at a long /M2K against a short /MNQ.

## [06:19 ET] POSITION UPDATE — EEM — opened 2026-08-21 @ 65.60, **STOPPED OUT 2026-10-15**
- 2026-10-15 bar: **63.07 / 63.99 / 62.81 / 63.96** on 23,305,460 shares. The 62.81 low is **0.19 through the published 63.00 stop**, so the position is closed at the stop for about -4.0%.
- It then closed at **63.96, back above its own stop** — which is exactly why this has to be stated. A reader checking the last price sees a live position with room.
- The breach is 0.18 ATR (ATR14 1.0684) and intraday only. Recorded anyway: honouring a stop only when the breach looks decisive is how a tracker stops being worth anything.
- Noted without editorialising: yesterday's red team withdrew a discretionary EEM close and left "the open position stands on its unchanged 63.00 stop". It was hit the same session.
- decision: **closed**. No re-entry — EEM has closed lower in eight of nine sessions (68.73 on 10-05 -> 63.96) with the 67.06 SMA20 and 66.87 SMA50 both above price.
- action: captured as a closure notice, `wait: true`.

## [06:19 ET] POSITION UPDATE — SNX — opened 2026-09-19 @ 260.00, last 255.14 (-1.9%)
- decision: **hold, stop 242.50 unchanged** — and flagged as the weakest hold in the report, the first thing the red team should override.
- what changed: a three-session breakdown through both averages. 276.04 (10-13) -> 263.76 (10-14) -> gap-down open 255.88, low **248.386**, close 255.14 on 998,018 shares (10-15). Price is now 14.73 under the 269.87 SMA20 and 6.83 under the 261.97 SMA50.
- the stop is 1.33 ATR below the close but only **0.62 ATR below the 10-15 session low** (ATR14 9.4893), and SNX appeared on **no** fetched earnings-calendar window through 2026-11-10, so nothing dated stands between here and the stop.
- action: captured.

## [06:20 ET] DATA GAP — no crypto idea can be published today
- `market_data.py crypto` works and returned spot: **BTC 81,840 (+0.85% 24h), ETH 2,445.83 (+3.11%), SOL 105.89 (+2.87%)** — source: CoinGecko via scripts/market_data.py
- But `history BTC-USD` failed on **every** configured source (Nasdaq no rows, Yahoo 429, TwelveData and AlphaVantage no API key, Stooq no rows), so there is **no OHLC and therefore no ATR** for any coin.
- `config/strategy.md` sets the crypto swing stop floor at 2.5 ATR. Without an ATR that floor cannot be computed, so any stop I wrote would be a guess dressed as a risk control. **No crypto candidate captured.** A bearish crypto view would in any case need futures, which are also unpriceable today.

## [06:20 ET] HOLD, NOTHING CHANGED — the remaining open positions
Checked each against fetched 2026-10-15 closes; none has new information warranting an amendment, so none is re-pitched:
- `XLE` 66.56 (-1.58%) vs entry 63.90 — **+4.2%**, target 70.50, stop 60.80. Only sector red on a rotation day; restated yesterday; no change.
- `XLF` 55.27 (+1.38%) vs 54.23 — **+1.9%**. Recommended 4x in ten days; deliberately **not** re-pitched a fifth time. Stop 52.80 holds.
- `CEG` 275.00 (-1.62%) vs 272.00 — **+1.1%**. New but not actionable: Q3 confirmed **2026-11-09, est 3.8225** (fetched), 17 sessions out.
- `KHC` 23.28 (+2.56%) vs 23.00 — **+1.2%**. Q3 confirmed **2026-11-04 bmo, est 0.4275** (fetched).
- `HII` 267.22 (+1.02%) vs 262.00 — **+2.0%**, target 430, no stop. Four sessions old, nothing new.
- `BCC` 75.48 (+2.03%) vs 76.50 — **-1.3%**, no stop.
- `PFE` 29.44 (+0.79%) vs 27.60 — **+6.7%**, no stop; the best open long on the book.
- `IYR` 97.04 (+1.16%) short vs 97.80 — **+0.8%**, stop 100.40 is 3.5% above. Rate-sensitive short that a 1.4% financials rotation day went against; stop not yet threatened.
- `STLD` awaiting entry @ 245.50, last 240.76. Reports **2026-10-19 amc, est 5.508** (fetched). Not re-pitched: it was demoted by validation yesterday on a **5.84% bid/ask spread**, and nothing fetched today shows that spread has narrowed.

## [06:23 ET] LEVELS + CAPTURE — KMX (new, conviction 3) — best new find of the morning
- The divergence: **four consecutive beats of +56.1% / +32.4% / +46.8% / +34.5%** against an analyst book that is **28.0% bullish with 17 of 25 at hold** — source: https://finnhub.io/api/v1/stock/earnings?symbol=KMX , https://finnhub.io/api/v1/stock/recommendation?symbol=KMX
- **Five distinct insiders, six open-market buys, $1,268,037, ZERO sells in six months** — Chawla 2,000 @ 53.39 and Shinder 574 @ 52.01 (06-25), ONeil 4,800 @ 52.36 (06-24). KMX closed **52.62**, so they bought at today's price and are flat — the level they chose is the level on offer. Best insider cluster screened all morning. — source: https://finnhub.io/api/v1/stock/insider-transactions?symbol=KMX
- Sell side capitulating: over four months **sell 7 -> 1, strong_sell 1 -> 0, strong_buy 1 -> 4, buy 1 -> 3**; bullish share +20.9pp.
- Relative strength split like CVS: **+19.97% vs SPY / +33.55% vs XLY over 6m**, but **-12.86% / -13.44% over 1m**.
- Levels: 52.62, ATR14 2.5237 (4.8%). Entry **54.00 (band 53.85-54.25)**, stop 48.80 (below the 49.05 low of 10-14, the window low), target 65.28 (120-day high).
  Risk 5.20 = **2.06 ATR**; reward 11.28 → **2.17:1**; baseline 31.6%, claimed 38%.
  The band is 40 cents wide because both edges are arithmetic: under 53.85 the stop is inside 2.0 ATR, over 54.25 the ratio drops under 2.0. Recorded because a narrow band is the honest output here, not a defect.
- **Conviction deliberately held at 3, not 4.** Q3 is dated 2026-12-16 (est 0.4724, fetched) but that is **42 sessions out** — beyond a swing horizon — so counting `dated_catalyst` to reach 4 would be inflation. `counter_argument_answered` was also considered and declined: the beat record answers "the street is slow" but does **not** answer the actual strongest objection, which is the used-vehicle credit cycle with the 10y at 5.19% and unemployment up to 4.2%. Two kinds, conviction 3.
- Caveat carried: 10-15 was a gap-up day inside a slide from 59.14 (09-30) to 49.05 (10-14), and it is the same one-session rotation as everything else on the tape. KMX remains below both its 54.92 SMA20 and 58.30 SMA50.

## [06:24 ET] REJECTED — CLF — revisions **+21.3pp**, the largest improvement screened, and it still fails twice over. Bullish share is only 30.0% with **1 of 4 beats**, and the geometry does not close: 12.15 with ATR 0.69, an entry at 12.40 above the 12.14/12.01 averages and a stop at 10.90 below support gives risk 1.50 = 2.17 ATR against the 15.06 high = **1.77:1**. Steel is also the STLD driver, which reports the same morning (10-19).
## [06:24 ET] REJECTED — DG — 133.89 and **1.54% off its high**, so nothing to target; already on the awaiting-entry list at 134.50, which is above the market, so no amendment is needed.
## [06:24 ET] REJECTED — VICR — 90.0% bullish and 4/4 beats, but **-42.53% off its high on a 9.84% ATR** and below both the 272.32 SMA20 and 230.46 SMA50 with revisions flat at 0.0. A 2.0 ATR stop is 43 points; the position would be a lottery ticket with no catalyst inside the horizon beyond the 10-20 print.
## [06:24 ET] REJECTED — LRN — revisions **-11.1pp**, the worst screened. ## REJECTED — ALGN — revisions -6.8pp, below the 154.75 SMA50. ## REJECTED — F — revisions +8.1pp and 1 insider buy, but below both the 12.41 SMA20 and 13.34 SMA50 at 41.4% bullish, and its dated catalyst is GM's print rather than its own.
## [06:24 ET] REJECTED — PYPL (1 buy vs 19 sells, net -$1.74M), IP (1 buy vs 2 sells, net -$843K), CPB (3 buys, one buyer, 100 shares each, **$6,435 total** — trivial, not a signal). EL, SJM, BAX, DOW, LYB, MOS, CF, NTR, WBA, MRNA: **zero** insider buys.

## [06:27 ET] LEVELS + CAPTURE — DKS (new, conviction 4)
- What happened, now documented rather than inferred: **2026-08-25 DKS fell 30.7% to 124.31**, its worst session on record. Q2 adjusted EPS **3.53 vs 3.76** estimate; full-year adjusted EPS guidance cut to **11.00-12.00 from 13.50-14.50** against a consensus near 14.20. Foot Locker (acquired September 2025) comped **-3.6%** while the core DICKS banner comped **+4.9%** — source: https://www.tikr.com/blog/dicks-sporting-goods-stock-just-had-its-worst-day-in-three-years-and-plummeted-31-heres-why , https://tickeron.com/blogs/dick-s-sporting-goods-dks-shares-drop-30-5-after-earnings-miss-and-guidance-cut-16422/
- **Securities class action** filed over the Foot Locker integration and the guidance cut; lead-plaintiff deadline **2026-11-03**. Allegations unproven. This is why size is 2% on a conviction-4 idea — source: https://www.morningstar.com/news/pr-newswire/20260924ny55362/dks-investor-alert-dicks-sporting-goods-inc-securities-class-action-notice-contact-suewallst
- **Nine insider open-market buys by SEVEN distinct buyers, $5,588,664**, all inside the post-crash base in September at 129.75-136.39: Barnes 3,665 @ 136.39 (09-30), Fitzgerald 1,860 @ 131.67 (09-23), Gupta 7,707 @ 129.75 (09-22), Colombo 913 @ 133.19 (09-01). Largest distinct-buyer cluster screened today. Stated honestly in the candidate: four sales offset it, so **net insider value is only +$81,802** — source: https://finnhub.io/api/v1/stock/insider-transactions?symbol=DKS
- Structure, bracketed by querying four history windows: **30-day range 120.151-142.56; 45-day high 204.50; 90-day high 244.38.** So the base sits directly under the 08-25 crash gap, and the 142.56 30-day high was printed on 10-15 itself.
- Levels: entry **140.00 (band 138.00-141.30)**, stop 129.60 (below a four-touch shelf: 130.08 / 130.51 / 132.32 / 132.57), target **164.97 = the 22.41 base width projected from 142.56**.
  Risk 10.40 = **2.60 ATR** (ATR14 3.9962); reward 24.97 → **2.40:1**; baseline 29.4%, claimed 38%.
- The target arrives twice independently, which is the only reason it is not just a number above resistance: the base projection gives 164.97, and 164.97 against the company's own 11.50 guidance midpoint is **14.3x forward** — against 11.7-12.8x today.
- **Correlation note:** DKS long sits alongside the NKE and LULU shorts, which is three rows on consumer discretionary — the cap. It is coherent rather than contradictory (retailer over brand) and it is a partial hedge: all three rose together on 10-15.

## [06:30 ET] REJECTED — VFC — the clearest example today of the floor doing its job
- The move is explained: **2026-10-13 upgrades to buy from Piper Sandler and Truist, both with $20 price targets**, on a Piper survey suggesting the Vans turnaround is stabilising. VFC has run 14.06 (09-30) -> 17.00 (10-15), +20.9% in ten sessions, on 15-19M shares against a ~9M base — source: https://gurufocus.com/news/9120362/vf-corp-vfc-shares-rise-4-on-upgrades-highlighting-vans-brand-turnaround
- Insiders are genuinely good: **3 buys, 2 distinct buyers, $1,302,362, ZERO sells** — CEO **Bracken Darrell 32,894 @ 14.98** (07-31), Carucci 20,000 @ 14.73 (08-13) and 30,000 @ 17.167 (06-09) — source: https://finnhub.io/api/v1/stock/insider-transactions?symbol=VFC
- And it still fails, cleanly: ATR14 0.6468. Entry 17.10 with a stop at 15.00 (below the 15.105 low of 10-12) is risk 2.10 = 3.25 ATR, fine. But the **anchored** target is $20.00 — the number two firms set three days ago — which is only **1.38:1**. The target that clears 2.0 is the 22.27 period high, **11% above where the fresh upgrades put fair value**. Targeting past the street the week it upgrades is the reverse-engineering `config/strategy.md` forbids.
- Note on the data: Finnhub's recommendation trend ends 2026-09-01 and shows bullish share change 0.0, so the 10-13 upgrades are **not yet in it**. The screen understates the analyst move here.

## [06:31 ET] REJECTED — INTC — the one name that made a new low on a day everything else bounced
- CEO **Lip-Bu Tan bought 105,263 shares @ 95.00 on 2026-08-11, $9,999,985** — and INTC closed **95.37** on 10-15, so the market has given his entire position back — source: https://finnhub.io/api/v1/stock/insider-transactions?symbol=INTC
- 4/4 beats, revisions +2.4pp. Rejected anyway on the tape: 120.23 (09-30) -> 95.37, **-20.7% in eleven sessions**, with 10-15 trading a low of **90.02 on 147.2M shares** — the heaviest of the window — and closing **-2.8% on the day**. On a session where every laggard on the tape caught a rotation bid, INTC was a source of funds and made a new low. Below the 113.50 SMA20 and 103.37 SMA50 by 19% and 8%. ATR 5.85%.
## [06:31 ET] REJECTED — CAT (1 buy vs 35 sells, net **-$113.6M**), ETN (4 buys all one person, net -$16.6M), LIN (net -$2.6M). DE, HON, NEE, DUK, SO, WM, APD, SHW, TXN, AMAT, LRCX, ON, MCHP, ZBH, MDT, DXCM, KSS, BBY, EMR, DOV, ROK, TER: **zero** insider open-market buys.

## [06:32 ET] HONEST SKEW — what this report does not contain, and why
Per `config/strategy.md` the skew is to be reported, not corrected by manufacturing a mix.
- **No intraday idea.** Today's dated catalysts are five bmo bank/insurer prints (TFC, MTB, RF, CFG, TRV). At 06:00 ET every fetched price is the 2026-10-15 close and there is no pre-market quote source working, so an intraday level set now would be a guess about a print I have not seen. TRV in particular was yesterday's "cleanest rate-regime long" watchlist entry and reports this morning — which makes it un-enterable today, not attractive.
- **No long_term idea.** Attempted and declined rather than skipped. The lane requires a defended valuation target and a **stated bear-case price** clearing 2.5:1. ELV has the best evidence screened today (+6.9pp revisions, 4/4 beats, 3 insider buyers) but no fetchable full-year guidance to value it from. DKS was the closest: at 10x the low end of guidance the bear case is 110 and the pre-crash 204.50 gives only **2.15:1**, so clearing 2.5 would mean stretching the multiple to 19x — the forbidden move. It was captured as the swing it actually is instead.
- **No futures, no crypto, no event contract** — all three for data reasons recorded above, not for lack of looking.
- **Sector concentration to watch:** of four new ideas, ABT and CVS are both healthcare. That is two rows on one sector driver, under the cap of three, and they are different sub-drivers (medtech vs managed care) — but they bounced on the same single session and should not be read as independent confirmation of each other.

## [06:34 ET] SELF-CHECK — recomputed every captured candidate from its own levels
Ran an independent recomputation of R:R, stop-distance in ATRs, the `1/(1+R:R)` break-even and expectancy for all 11 rows rather than trusting what I wrote about my own ideas. Results:
- Nine rows pass both floors with positive expectancy: GE 2.06:1 / 2.31 ATR, ABT 2.08 / 2.79, CVS 2.33 / 3.34, NKE 2.42 / 2.08, LULU 2.07 / 3.60, SMMT 2.19 / 2.36, EEM 2.27 / 2.43 (ETF floor 1.8), KMX 2.17 / 2.06, DKS 2.40 / 2.60.
- Claimed edge over the break-even rate runs +2.4 to +12.8 points. Nothing is above the 20-point threshold that `config/strategy.md` calls a large claim.
- **Two rows fail a live check, both by design, and both are restatements of positions published weeks ago:**
  - `MU` — risk 90.00 = **1.91 ATR** against a 2.0 floor, and 2.00:1 at a claimed 33% is break-even. The levels are the 2026-09-18 published ones and ATR14 has since expanded to 47.0114. It is a **closure notice**, so demotion to the watchlist is the correct outcome, not an error. Annotated in the candidate so the demotion reason reads correctly.
  - `SNX` — risk 17.50 = **1.84 ATR** against the 2.0 floor, for the same reason: published 2026-09-19, ATR14 has since expanded to 9.4893. A filled position's stop cannot be re-cut, so the honest statement is that this position now carries a stop inside the noise of the instrument. Rewritten to say exactly that, and flagged as the weakest row in the report.
- Reference-point note for validation: NKE and LULU stop distances are quoted in the candidate text **from the last close** (3.09 and 4.08 ATR) because that is what matters to someone already holding them; measured from the original entry, as validation does, they are 2.08 and 3.60 ATR. Both figures are correct and neither is the other.

## [06:35 ET] DATA GAP — short interest unavailable all morning
- `market_data.py short` returned `ReadTimeout` from **api.nasdaq.com** on every attempt: NFLX, KMX, DKS, NKE, LULU. No short-interest or days-to-cover figure appears anywhere in today's candidates.
- This costs the two short rows the most. NKE and LULU are both held short in names down 42% and 50%+ year to date, and crowding is precisely the risk a rotation into laggards exposes — so the one measurement that would have sized that risk is the one that was unavailable.

## [06:36 ET] SELF-CHECK ROUND 2 — the band edges, and a real error it caught
The first self-check only tested the `ideal` price. Re-testing **every edge of every entry band** found two live ideas that would have published a fill at a ratio below the floor, which is the failure mode `config/strategy.md` is aimed at — a band whose upper edge quietly voids the arithmetic the idea was approved on.
- **ABT was wrong and is fixed.** The published band topped at 104.80, but at the 104.68 last close the ratio to 117.34 against the 97.00 stop is **1.65:1**. The valid band against those levels is **101.73-103.78**, so ABT was re-captured at ideal **103.00**, band **101.80-103.70** (2.39:1, 2.54 ATR), with the condition stating outright that the market price is deliberately outside the band.
- **CVS was wrong and is fixed.** Band topped at 94.20, which gives **1.87:1**. Re-captured with zone_high **93.80** (ratio 2.01 at that edge), ideal 93.00 unchanged.
- KMX (53.85-54.25) and DKS (138.00-141.30) were already correct at both edges, because both bands were derived from the two constraints in the first place.
- **All four new ideas now pass at every edge:** ABT 2.04-3.24:1 and 2.03-2.83 ATR; CVS 2.01-2.46:1 and 3.21-3.69 ATR; KMX 2.02-2.26:1 and 2.00-2.16 ATR; DKS 2.02-3.21:1 and 2.10-2.93 ATR.
- **The remaining band-edge failures are all on restated positions and are not orders.** GE, MU, NKE, LULU, SMMT, EEM and SNX each carry the band they were originally published with, and every one of those candidates says in `entry.condition` that it is already filled (or closed) and restated for the record. Judged at the `ideal` — the fill that actually happened — GE, NKE, LULU, SMMT and EEM all pass; only MU and SNX fail, both annotated above as volatility-expansion artifacts. A restated band should not be read as an order band.

## [06:37 ET] RESEARCH COMPLETE
- **candidates: 11 distinct symbols** (15 lines in candidates.jsonl; ABT, CVS, MU and SNX were each re-captured after the self-checks, and synthesis takes the last entry per symbol).
  - **4 new ideas:** `DKS` buy conviction 4 (2.40:1), `CVS` buy conviction 4 (2.33:1), `ABT` buy conviction 4 (2.39:1), `KMX` buy conviction 3 (2.17:1).
  - **7 position updates:** `GE` hold into Monday's print; `NKE` and `LULU` hold the shorts with new 50-day cover rules; `SMMT` and `SNX` hold with the stop-inside-the-noise problem stated; **`MU` and `EEM` closure notices — both stops were breached intraday on 2026-10-15 and the prior-context table does not know it yet.**
- **The single most important caveat:** 2026-10-15 was one rotation session out of AI/tech into laggards (IWM +1.37%, XLV +1.86%, XLF +1.38%, SLV +3.39% against QQQ -0.13%). Every reversal and 50-day reclaim in this report is that same one day seen through different tickers. One observation, not eleven, and none has a second day of confirmation.
- **coverage gaps:** no intraday idea (no pre-market source at 06:00 ET and today's five catalysts are all bmo prints); no long_term idea (attempted — nothing cleared 2.5:1 against a defensible bear-case price without stretching a multiple); no futures idea (no CME contract price obtainable); no crypto idea (spot available, but zero OHLC so no ATR and no computable stop floor); no event-contract idea (Kalshi returned an empty market set on all 8 topics tried). Short interest unavailable on every name. Options-implied move unavailable on every name. No index, VIX, DXY, gold or WTI level was obtainable, so none is quoted anywhere.
- **sources that failed:** Yahoo quotes/history (HTTP 429, all index and crypto symbols), Yahoo options (HTTP 401, so `implied` is dead), Finnhub CFD indices (subscription required), api.nasdaq.com short interest (ReadTimeout, every call), Kalshi events (reachable, 0 markets), Nasdaq history for TMHC and BTC-USD, Stooq (404/no rows), TwelveData and AlphaVantage (no API key).
- **sources that worked:** Finnhub quotes (2026-10-15 16:00 ET closes — previous close, which at 06:00 ET is the freshest honest equity price, not stale data), Finnhub history/ATR, Finnhub earnings calendar, Finnhub insider transactions, Finnhub recommendation trend and surprises, FRED, CoinGecko, computed relative strength.
