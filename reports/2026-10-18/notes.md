# Research log — 2026-10-18

## [06:01 ET] SETUP — Sunday 2026-10-18, weekend run
- US equities and futures cash session closed. Per `config/strategy.md` weekend
  behavior: shift toward crypto and event contracts for actionable ideas; treat
  equities as week-ahead preparation (entry for next open, horizon `swing`).
- Prior context: 19 open positions, 9 awaiting entry, 23 closed of 54 tracked.
- Track record read honestly: 3/23 hit target (13%), avg -5.4%. n=23 is above
  the ~15 threshold overall but every *sub*-bucket is under it, so the only
  conclusion I will draw is the aggregate one: this report's swing-long equity
  setups have been entering too early into a tape that kept going. By-conviction
  (4: 2/3, 3: 1/14) is n=3 and n=14 — noise, not a signal to chase conviction-4.
- First obligation is position management on 19 live rows, not new hunting.

## [06:02 ET] MACRO — data sources degraded
- `market_data.py macro`: Yahoo returning **HTTP 429 Too Many Requests** on all
  index symbols (^GSPC, ^NDX, ^DJI, ^RUT, ^VIX); Finnhub refuses indices
  ("Market data subscription required for CFD indices"); stooq 404s on ^-prefixed
  symbols; no AlphaVantage key. So **no live index or VIX level this run** —
  recorded as a gap, not estimated.
- Crypto via CoinGecko is healthy and is the live market today.

## [06:02 ET] CRYPTO — spot, as of 2026-10-18T10:01Z (24/7 market, live)
- BTC $82,073, +0.73% 24h, 24h vol $15.6B, mcap $1.650T — source: CoinGecko
- ETH $2,422.48, -0.39% 24h, vol $6.98B — source: CoinGecko
- SOL $103.91, -0.69% 24h, vol $1.85B — source: CoinGecko
- XRP $1.30, -0.36%; DOGE $0.0794, -0.91%; ADA $0.2212, -0.70%
- LINK $12.04, -1.43%; AVAX $9.86, -1.39%; LTC $59.45, +0.36%
- Read: a flat, slightly-red weekend tape with no dispersion — every major but
  BTC and LTC down well under 1.5%. That is a low-energy consolidation, not a
  trend to join in either direction. Noted; it argues against a momentum crypto
  entry today.

## [06:04 ET] MACRO — rates are the regime, via FRED (live, dated)
- US10Y **5.10%** (2026-10-15) — source: FRED/market_data.py macro
- US2Y **4.77%** (2026-10-15); 10y-2y curve **+0.35** (2026-10-16)
- Fed funds effective **3.88%** (2026-10-15)
- Unemployment **4.2%** (2026-09-01); CPI index 336.298 (2026-09-01)
- TLT (20y proxy) **$80.05**, +0.10% (Fri 2026-10-16 close) — source: finnhub
- **The read:** the 10y sits 122bp ABOVE the effective funds rate with the
  curve positively sloped at +0.35. That is not a market pricing cuts into
  weakness — it is term premium / long-end supply doing the work while the
  front end is anchored. A 5.10% 10y is the highest-pressure input for every
  long-duration equity and every rate-sensitive asset in the book.
- Consequence for the book: this *confirms* two open shorts (TLT short, IYR
  short) and is a headwind to nothing I hold long except CEG/VST-type duration.

## [06:04 ET] DATA GAPS — record for data_quality_notes
- No live index level, VIX, DXY, gold or WTI this run: Yahoo HTTP 429 across all
  index symbols, Finnhub refuses indices, stooq 404s on ^-prefixed tickers, no
  AlphaVantage key. Equity/ETF single-name quotes DO work via finnhub.
- All equity prices this run are **Friday 2026-10-16 20:00Z close** — a closed
  market, which on a Sunday is the freshest honest price, not stale data.

## [06:05 ET] CALENDAR — earnings inside 10 sessions hitting the book (finnhub)
**Two open positions report within 36 hours of this report being read:**
- `GE` **2026-10-19 BMO** (tomorrow), EPS est 2.0576 — OPEN POSITION, +1.9%
- `STLD` **2026-10-19 AMC** (tomorrow), EPS est 5.508 — OPEN POSITION, -2.0%
- `UNP` 2026-10-22 BMO, EPS est 3.5034 — OPEN POSITION, +0.1%
- `ABT` 2026-10-21 BMO, EPS est 1.4302 — AWAITING ENTRY @ 103.0
- `AAL` 2026-10-22 BMO, EPS est -0.3639 — AWAITING SHORT @ 13.35
- `FCX` 2026-10-27, EPS est 0.7928 — OPEN POSITION, +2.0%
- `HII` 2026-10-29 BMO, EPS est 4.458 — OPEN POSITION, +3.8%
- Season weight: Oct 28-29 are the heavy days (258, 363 reporters). Oct 19-23 is
  the front edge — 44/65/124/159/31.
- This is the highest-value thing in today's run and it is all position
  management, which is the first obligation anyway.

## [06:06 ET] LEVELS — fetched history, 90d (finnhub candles)
| Sym | Last (Fri) | ATR14 | SMA20 | SMA50 | 90d low | 90d high |
| --- | --- | --- | --- | --- | --- | --- |
| GE | 313.83 | 6.7348 | 312.878 | 330.4376 | 296.61 | 388.84 |
| STLD | 240.54 | 6.9658 | 234.4515 | 239.3913 | 216.36 | 288.74 |
| UNP | 289.04 | 4.2591 | 277.5755 | 287.7512 | 255.2202 | 315.99 |
| SMMT | 14.63 | 1.1613 | 16.4877 | 15.6801 | 12.07 | 19.09 |
| SNX | 246.75 | 9.6328 | 268.8955 | 261.72 | 234.025 | 298.7699 |
| CVS | 92.36 | 2.2098 | 87.6505 | 91.725 | 84.23 | 110.68 |

## [06:07 ET] POSITION UPDATE — SMMT — opened 2026-10-09, -14.4%
- Price 14.63 vs stop 14.40: **0.20 ATR of room** (ATR14 1.1613). Below both the
  20-day (16.49) and the 50-day (15.68). The original stop was sound — 2.33 ATR
  from the 17.10 entry — but the trade has ground down to the point where any
  ordinary session takes it out.
- **Insider signal is genuinely strong and cuts the other way**: 6 open-market
  buys, 3 distinct buyers, **$103.6M bought, zero sells** in 6 months —
  R.W. Duggan 3,810,000 sh @ $13.12 (2026-06-12) and 100,000 @ $14.60
  (2026-06-04); CEO M. Zanganeh matching size on both dates; CFO M.S. Soni
  50,000 sh @ $14.43-14.46 (2026-06-04). Source: finnhub insider-transactions.
- decision: **hold the stop at 14.40 unchanged. No widening.**
- why: widening a stop on a losing position to avoid being stopped is the exact
  mirror of the KRE error this repo already shipped once — it makes the trade
  strictly worse while making the ratio look better. The insider buying is a
  reason to want to *own* SMMT, not a reason to keep this entry at 17.10 alive.
  If 14.40 trades, the trade is closed and the insider thesis becomes a new,
  separate trade nearer the 90-day low of 12.07 — which per CLAUDE.md is a
  genuinely separate position, not a re-pitch.
- action: captured via add_candidate.py with levels unchanged.

## [06:07 ET] DATA GAP — Kalshi event search is largely non-responsive
- `events "CPI"`, `events "Bitcoin"`, `events "interest rate"`,
  `events "government shutdown"` all return **count: 0**.
- `events "Fed"` returns 4 markets, all of them false positives: tennis markets
  (`KXMVECROSSCATEGORY-*`) matching the substring "Fed" inside "Federico". All
  four have null bid/ask/last/volume.
- So I have **no live event-contract prices this run**. Since the weekend lane is
  supposed to lean on event contracts, this is the most costly gap today and it
  is recorded rather than papered over: I will not state an implied probability
  I could not fetch, which rules out any new event-contract idea. The two
  pending ones (KXFEDDECISION-26OCT-H25 @ 28, KXCPIYOY-26SEP-T3.5 @ 18) cannot
  be re-priced either.

## [06:09 ET] POSITION SCAN — all 19 open rows, distance to stop in ATRs
Computed from fetched 90d candles (ATR14) against Friday's close. This is the
triage that decides which rows actually need a decision today.

| Sym | Side | Last | ATR14 | P/L% | ATR to stop | SMA20 | SMA50 | 90d lo | 90d hi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLE | BUY | 68.24 | 1.332 | +6.8 | 5.58 | 63.92 | 63.54 | 52.62 | 68.29 |
| BCC | BUY | 76.13 | 2.075 | -0.5 | none | 75.31 | 77.85 | 67.38 | 88.43 |
| PFE | BUY | 29.58 | 0.574 | +7.2 | none | 28.34 | 27.97 | 23.62 | 29.88 |
| DG | BUY | 134.36 | 3.944 | -0.1 | 2.22 | 124.15 | 124.42 | 107.59 | 136.05 |
| IYR | SHORT | 97.39 | 1.368 | +0.4 | 2.20 | 96.15 | 100.06 | 93.29 | 108.17 |
| LULU | SELL | 97.10 | 3.198 | +3.5 | 4.66 | 96.97 | 106.74 | 90.38 | 128.86 |
| NKE | SELL | 37.13 | 1.228 | +3.3 | 3.15 | 35.46 | 37.55 | 31.97 | 46.31 |
| SNX | BUY | 246.75 | 9.633 | -5.1 | **0.44** | 268.90 | 261.72 | 234.03 | 298.77 |
| KHC | BUY | 23.68 | 0.571 | +3.0 | 4.34 | 22.96 | 24.24 | 21.76 | 28.09 |
| TLT | SHORT | 80.05 | 0.837 | -0.2 | 2.33 | 78.76 | 80.73 | 76.43 | 87.79 |
| CEG | BUY | 271.37 | 16.70 | -0.2 | **1.28** | 273.81 | 275.69 | 228.63 | 309.80 |
| FCX | BUY | 69.54 | 2.638 | +2.0 | 2.35 | 71.72 | 72.04 | 56.00 | 80.24 |
| XLF | BUY | 55.52 | 0.696 | +2.4 | 3.91 | 54.45 | 56.28 | 52.04 | 58.60 |
| SMMT | BUY | 14.63 | 1.161 | -14.4 | **0.20** | 16.49 | 15.68 | 12.07 | 19.09 |
| STLD | BUY | 240.54 | 6.966 | -2.0 | **1.69** | 234.45 | 239.39 | 216.36 | 288.74 |
| HII | BUY | 272.00 | 7.405 | +3.8 | none | 265.99 | 285.41 | 255.35 | 334.53 |
| GE | BUY | 313.83 | 6.735 | +1.9 | 3.24 | 312.88 | 330.44 | 296.61 | 388.84 |
| UNP | BUY | 289.04 | 4.259 | +0.2 | 2.73 | 277.58 | 287.75 | 255.22 | 315.99 |
| CVS | BUY | 92.36 | 2.210 | -0.7 | 3.15 | 87.65 | 91.72 | 84.23 | 110.68 |

Four rows carry under 2.0 ATR of room — SMMT 0.20, SNX 0.44, CEG 1.28, STLD 1.69
— and those are the only ones where this week's tape decides the outcome. Three
rows (BCC, PFE, HII) carry no stop by construction as long-term theses.

- **XLE at 68.24 against a 90-day high of 68.29** is the standout: the position
  is +6.8% and price is AT the top of its range, so the 70.5 target is a
  breakout rather than a reversion. It has also been published 4x in 10 days.
- **FCX and CEG are both below their 20- and 50-day** while nominally flat to
  positive, which is the configuration that precedes a stop-out.
- **Book concentration is real and worth flagging**: GE, STLD, FCX, UNP, BCC,
  XLE and HII are one cyclical-industrial bet with seven tickets. That is past
  the 3-idea correlation cap in `config/strategy.md`, inherited rather than
  opened today, and it argues against adding any new industrial long.

## [06:09 ET] POSITION UPDATE — SNX — opened 2026-09-19, -5.1%
- 246.75, **0.44 ATR from the 242.5 stop** (ATR14 9.633). Below the 20-day
  (268.90) AND the 50-day (261.72); 90-day low 234.03.
- The original stop was already too tight to publish under current rules: 17.5
  points from a 260.00 entry on a 9.633 ATR is **1.82 ATR**, inside the 2.0 ATR
  stock floor. This position would not pass validation if pitched today.
- No earnings inside the 10-session window (TD Synnex reports on a November
  fiscal year, next print late December).
- decision: **hold the 242.5 stop unchanged; no widening, no adding.**
- why: same reasoning as SMMT. The stop being too tight at entry is an argument
  about how the trade was published, not a licence to move it now that price has
  arrived there — moving it is the KRE error run backwards.

## [06:09 ET] POSITION UPDATE — CEG — opened 2026-10-01, -0.2%
- 271.37, 1.28 ATR from the 250.0 stop on a very wide ATR14 of 16.70 (6.2% of
  price). Below the 20-day (273.81) and 50-day (275.69). 90-day 228.63-309.80.
- Macro cuts against it: the 10y at **5.10%** is the direct discount-rate
  headwind for an IPP valued on long-dated power contracts, and that rate is
  122bp above effective fed funds, so the pressure is term premium rather than
  something a Fed cut relieves.
- decision: hold, stop unchanged at 250.0, do not add.
- why: 1.28 ATR of room on a 6.2% ATR name is roughly one bad session, so this
  resolves itself quickly either way; the thesis (datacenter power demand) is
  intact and unbroken by price alone. But with the 10y at 5.10% there is no case
  for adding to duration-sensitive length here.

## [06:10 ET] AWAITING-ENTRY REVIEW — 9 pending rows, priced at Friday's close
| Sym | Pending | Last (Fri) | Gap to entry | Read |
| --- | --- | --- | --- | --- |
| `VST` BUY @ 132.0 | 2026-08-24 | 152.02 | +15.2% above | stale — never filled, price ran away |
| `OXY` BUY @ 54.0 | 2026-09-24 | 62.38 | +15.5% above | stale — ran away, +2.8% Friday |
| `GLD` SELL @ 406.77 | 2026-09-08 | 382.01 | 6.1% below | thesis played out without filling |
| `ITB` SHORT @ 89.8 | 2026-09-30 | 86.40 | 3.8% below | played out without filling |
| `AAL` SHORT @ 13.35 | 2026-10-03 | 11.88 | 11.0% below | played out without filling; earnings 2026-10-22 |
| `ABT` BUY @ 103.0 | 2026-10-16 | 104.89 | 1.8% above | live and close; **earnings 2026-10-21 BMO** |
| `KXFEDDECISION-26OCT-H25` YES @ 28 | 2026-09-02 | unknown | — | cannot re-price, Kalshi search dead |
| `KXFEDDECISION-26SEP-H0` YES @ 47 | 2026-09-03 | unknown | — | September market, now expired |
| `KXCPIYOY-26SEP-T3.5` NO @ 18 | 2026-09-30 | unknown | — | cannot re-price, Kalshi search dead |
- Five of nine never filled and the move happened anyway — four of them pullback
  entries on longs and shorts set below the market. That is the fill-rate problem
  `config/strategy.md` already names (31 pullback entries to 1 breakout in month
  one, 42% filled), showing up again. Worth stating in the report rather than
  quietly re-pitching the same levels.
- `KXFEDDECISION-26SEP-H0` is a September-dated market and should be retired.

## [06:10 ET] REJECTED — new crypto entry — flat tape, no dispersion, no edge
- Every major coin within -1.5% to +0.8% on the day with BTC the only real
  gainer. On a Sunday the only honest crypto idea would be a momentum or
  mean-reversion entry, and a 9-coin tape clustered inside 2% supports neither.
- No crypto futures idea either: the view that would justify `/MBT` is directional
  and I do not have one at 82,073 with no catalyst fetched.
- Declining to manufacture the weekend crypto idea the calendar invites.

## [06:10 ET] REJECTED — all new event contracts — cannot price them
- The weekend lane is supposed to lean here, but Kalshi search returns count 0
  for CPI, Bitcoin, interest rate and government shutdown, and the only "Fed"
  hits are tennis markets with null prices. An event-contract thesis requires
  stating the market's implied probability against mine; with no fetched price
  that is a fabricated number, so nothing is captured. Gap, not an idea.

## [06:10 ET] REJECTED — new industrial/cyclical longs — correlation cap breached
- GE, STLD, FCX, UNP, BCC, XLE and HII are seven rows on one cyclical-industrial
  driver, against a cap of 3 in `config/strategy.md`. Inherited, not opened
  today, but it disqualifies adding another — so no new energy, steel, rail,
  copper or aerospace long was pursued even where the setup looked reasonable.

## [06:10 ET] NOT REACHED — recorded as coverage gaps
- No small/micro-cap hunting this run. The 19-row book and two earnings prints
  inside 36 hours consumed the budget on position management, which is the first
  obligation per the skill, but it means the asymmetric lane got nothing today.
- No long-term lane work. BCC, PFE and HII are the three existing stopless
  long-term theses and none was re-underwritten against current filings; PFE at
  29.58 is at its 90-day high of 29.88 against a 42.00 target and HII at 272.00
  sits below its 50-day at 285.41 with a 430.00 target, both of which deserve a
  valuation re-check this report did not do.
- No `implied` figures anywhere: Yahoo options returns HTTP 401 Unauthorized, so
  no target was checked against the straddle-implied move this run.
- No relative-strength checks (`relstrength`) — not run, budget.
- DG, IYR, LULU, NKE, KHC, FCX, XLF, CVS, BCC, PFE, HII: all reviewed in the
  position scan above and all carry 2.2 ATR or more of stop room (or no stop by
  design), so none required an amendment today and none was captured. That is a
  decision to leave them as-is, not an omission.

## [06:11 ET] RESEARCH COMPLETE — SUPERSEDED, see the later block below
- candidates: 9 captured, 8 distinct symbols (GE captured twice; the later
  conviction-4 entry with positioning evidence supersedes the first)
- all 9 are position management on existing rows. **Zero new ideas today**, and
  that is the honest output rather than a shortfall: a Sunday with no live
  equity session, a dead event-contract feed, a flat crypto tape, a 19-position
  book already past the correlation cap, and two open positions reporting
  earnings inside 36 hours.
- the four decisions that matter: GE hold through a BMO print tomorrow (no
  action available), STLD cut to half before tomorrow's AMC print (stop is
  1.69 ATR and cannot contain a steel gap), UNP hold full size through Thursday
  (2.73 ATR stop is adequate), XLE raise the stop to 65.50 to bank +6.8%.
- SMMT (0.20 ATR) and SNX (0.44 ATR) are held to their stops with no widening.
- coverage gaps: no index/VIX/DXY/gold/WTI levels (Yahoo 429, Finnhub refuses
  indices, stooq 404s on ^ symbols, no AlphaVantage key); no event-contract
  prices (Kalshi search returns 0); no options-implied moves (Yahoo options 401);
  no small-cap or long-term lane work; no relative-strength checks.
- sources that failed: query1/query2.finance.yahoo.com (429 on indices, 401 on
  options chains), finnhub index quotes (subscription), stooq (404 on ^GSPC,
  ^NDX, ^DJI, ^RUT, ^VIX), Kalshi market search (empty for all macro topics).
- sources that worked: finnhub quotes/candles/earnings/recommendations/insiders,
  FRED macro series, CoinGecko crypto, SEC EDGAR filings.

## [06:12 ET] CORRECTION — my own timestamps, and budget remaining
- The stamps above were written from my *estimate* of elapsed time, not from
  `date`. A `date` call at the end of the first pass read **06:11 ET**, against
  stamps that had reached 06:57. They have been remapped to the real elapsed
  clock. Recording this rather than quietly fixing it: the skill says to check
  the clock rather than trust a sense of elapsed time, and I did the thing it
  warns about. No market number was affected — every price above came from a
  fetched source with its own `asof`.
- Consequence: the 06:11 RESEARCH COMPLETE block was premature. Roughly 49
  minutes of budget remain, so research continues into the two lanes that block
  listed as gaps — the long-term book and small caps.

## [06:15 ET] LONG-TERM LANE — the three stopless theses, re-underwritten
Method: trailing earnings base = sum of the four most recent *reported* quarterly
EPS actuals from finnhub, against fetched market cap and price. Stated as a
multiple so the target is a derived number rather than a chart level. All three
positions were published with no stop, so each needs a real invalidation.

| Sym | Price | TTM EPS base | Trailing x | Published target | Target as x | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| PFE | 29.58 | 3.05 | 9.70x | 42.00 | 13.77x | **defensible — accumulate** |
| HII | 272.00 | 16.78 | 16.21x | 430.00 | **25.63x** | undefended — halve, target → 335.60 (20x) |
| BCC | 76.13 | 2.95 | 25.8x | 110.00 | **37.3x** | undefended + macro broken — **close** |

- **PFE is the one that holds up, and it is the strongest idea in today's report.**
  38.9% analyst bullish share and *deteriorating* (-2.8) against four consecutive
  beats, insiders net buyers of $2.83M across 3 distinct buyers, and relative
  strength that is leadership rather than decline: +19.52% 3m vs SPY +2.85% and
  XLV +10.96%, i.e. **+16.67% vs SPY over three months**. A 42.00 target is 13.77x
  an unchanged earnings base — an ordinary pharma multiple, requiring no estimate
  increase. This is precisely the "de-rated quality" case the skill says insider
  data is strongest for. Bear case 24.40 = 8.0x. R:R from the 27.60 entry = 4.50.
- **HII**: best revision improvement in the whole book (+5.9 to 58.8%) and a +37%
  Q2 beat (5.27 vs 3.84), but the 430.00 target was 25.63x trailing and I never
  derived it. At a defensible 20x (335.60) the R:R from entry against a 13x bear
  case (218.14) is **1.68 — under the 2.5 long-term floor**. So: halve, mark the
  target down, and do not restore it without reading the backlog disclosure.
  Insiders net -$5.6M with zero buys. Earnings 2026-10-29 BMO.
- **BCC**: closing. The 110.00 target was 37.3x trailing, and more importantly the
  invalidation has effectively already fired — a housing/repair-remodel thesis
  needs mortgage rates down, mortgage rates track the 10-year, and the 10-year is
  **5.10%**, 122bp above fed funds, i.e. term premium that a Fed cut does not fix.
  Position is -0.5%, so the exit is free. Corroboration: the pending ITB
  homebuilder short has fallen 89.80 → 86.40 without ever filling.
- Note on method honesty: trailing P/E is the *wrong* lens for a cyclical at
  trough earnings, and BCC at 25.8x may genuinely be cheap on mid-cycle numbers.
  I have no mid-cycle EPS, book value or backlog figure for it, which is exactly
  why it is being closed rather than shorted — the problem is that the published
  target rested on a multiple no fetched figure supports, not that I have proven
  the business is bad.

## [06:16 ET] SCHEMA NOTE — for synthesis
- `scripts/report_schema.json` sets `additionalProperties: false` on the idea
  definition, so there is no `invalidation` field; my first PFE capture was
  rejected for inventing one. Long-term invalidation conditions are written into
  `key_risk` prefixed "INVALIDATION", per `config/strategy.md`, and the numeric
  downside goes in `bear_case_price`.

## [06:19 ET] POSITION UPDATE — NKE — opened 2026-09-08, +3.3%
- decision: take half off, tighten stop 41.00 → 39.60 (2.01 ATR, above entry)
- why: **one-month relative strength has flipped positive**, +2.12% vs SPY
  +0.09% (so +2.03% relative), and price 37.13 has reclaimed the 20-day at
  35.46. The 3m (-17.43%) and 6m (-26.82%) relative readings still support the
  short, but a short whose near-term momentum has turned is a different trade.
- action: captured.

## [06:21 ET] POSITION UPDATE — LULU / FCX
- `LULU` +3.5%: **hold, unchanged**, and deliberately NOT trimmed alongside NKE.
  The distinguishing test is measured: LULU 1m relative is still -2.39% vs SPY
  where NKE is +2.03%. LULU is -19.62% 3m and -49.43% 6m vs SPY while XLY is only
  -6.6% over 6m, so it is losing ground to a benchmark that itself fell — company
  deterioration still in progress. 4.66 ATR of stop room. Scale first third at
  the 90-day low 90.38.
- `FCX` +2.0%: hold, unchanged, no adds; earnings 2026-10-27. 3m relative
  +15.44% vs SPY is real leadership, but 1m is -1.94% and price is below both the
  20- and 50-day. Also noted: its stop is **1.84 ATR from entry, inside the 2.0
  floor** — a second position (with SNX at 1.82) published with a sub-floor stop.

## [06:26 ET] REJECTED — regional banks long into earnings — thesis failed its own test
Tested properly and dropped, because the macro case looked good and every
fetched confirmation contradicted it.
- The case: 14+ regional banks report 2026-10-19 to 10-21 (FITB, ZION, WAL,
  WTFC, EWBC, KEY, CMA, OZK, HWC, CBSH, FNB, BOKF, AUB, CATY, FULT...), and a
  positively sloped curve (+0.35) with the 10y at 5.10% is a net-interest-margin
  tailwind. Financials are only 1 of 19 open rows, so there is room under the
  correlation cap.
- The screen killed it:

| Sym | Cap | Last | SMA50 | vs 50d | Revisions | Insider net |
| --- | --- | --- | --- | --- | --- | --- |
| ZION | $10.1B | 63.37 | 66.39 | **below** | deteriorating -3.5 | **-$6.58M, 0 buys** |
| EWBC | $17.4B | 126.88 | 128.56 | **below** | flat 0.0 | **-$12.11M, 0 buys** |
| WAL | $8.4B | 74.51 | 78.12 | **below** | flat 0.0 | **-$3.78M, 0 buys** |
| FITB | $45.7B | 50.37 | 53.52 | **below** | deteriorating -2.7 | **-$1.31M, 0 buys** |

- **Four for four below the 50-day, four for four with zero open-market insider
  buying and net selling, two with deteriorating revisions.** ZION beat by 65%
  last quarter (3.05 vs 1.8453) and still sits near its 90-day low of 60.76 with
  revisions falling. Not one independent confirmation available for a long.
- The inference matters more than the rejection: **the credit channel is
  dominating the NIM channel.** A curve steepening from the *long end* at 5.10%
  rather than from Fed cuts raises funding costs and stresses commercial real
  estate at the same time, so the NIM tailwind is being swamped. That is a
  coherent reading of why banks fall on a steep curve, and it corroborates the
  open `IYR` REIT short rather than arguing for a bank long.
- `config/universe.md`-adjacent caution also noted: KRE is the name this report
  already mishandled three times per CLAUDE.md. Regional banks have earned care.

## [06:22 ET] POSITION UPDATE — IYR / XLF — the one real conflict in this book
- `IYR` short +0.4%: **hold unchanged**, conviction raised to 4 on new evidence.
  The bank screen above is the third independent leg: term-premium rates (10y
  5.10%, 122bp over funds), price below the 50-day (100.06), and lenders to CRE
  trading badly with directors selling into their own prints. Bank earnings
  2026-10-19 to 10-21 are now the dated catalyst *for this short*, not for a bank
  trade. Scale first half at the 90-day low 93.29.
- `XLF` long +2.4%: **hold, explicitly do not add.** Declared conflict: this
  report is short REITs on a credit thesis while long the banks that lend against
  that credit. The reconciliation is composition — XLF is weighted to
  money-centre, insurance and payments earnings rather than the regional CRE book
  — and it is only a partial answer, so conviction stays 3 and the position is
  capped. **The falsification test is dated**: if the 2026-10-20/10-21 prints show
  reserve builds at the money centres too, the distinction fails and XLF closes.
  Writing the kill condition down now rather than rationalising later.

## [06:24 ET] ABT — pending idea amended from BUY-the-level to WAIT
- Pending since 2026-10-16 at 103.00; never filled, price 104.89. Earnings
  **2026-10-21 BMO**, est 1.4302.
- Found what the original pitch missed: ABT has **missed consensus in 3 of its
  last 4 quarters** (1.15/1.1552, 1.50/1.5113, 1.30/1.3139 all misses; only
  1.31/1.2922 a beat), and insiders are **net sellers of $45.55M** despite 3
  distinct buyers. Against that, revisions are improving hard (+5.2 to 75.8%).
- When the sentiment signal and the base rate disagree, the sell side is the one
  that has been wrong here. So: do not pre-position into a BMO print on the wrong
  side of its own base rate. Levels set from real structure — stop 98.00 (below
  the 20-day at 100.98, 2.10 ATR), target 117.34 (the 90-day high), R:R 2.87.
- Healthcare is also genuine diversification from seven cyclical-industrial rows.

## [06:25 ET] REVIEWED, NO CHANGE — DG, KHC, CVS
Reviewed in the position scan, all with adequate stop room and no earnings inside
the fetched window, so no amendment is warranted and none is captured. Recording
the decision so absence from the report is not read as an oversight:
- `DG` -0.1%, 134.36, **2.22 ATR** to stop 125.60. Price is well ABOVE both the
  20-day (124.15) and 50-day (124.42) near its 90-day high of 136.05 — the
  healthiest chart structure of any long here. Hold.
- `KHC` +3.0%, 23.68, **4.34 ATR** to stop 21.20. Above the 20-day (22.96), below
  the 50-day (24.24). Ample room. Hold.
- `CVS` -0.7%, 92.36, **3.15 ATR** to stop 85.40. Above the 20-day (87.65) and at
  the 50-day (91.72); target 110.68 is the 90-day high. Hold.

## [06:26 ET] PENDING ENTRIES — four to retire, one expired
Not re-pitched, and the reason is recorded so synthesis does not quietly carry
them forward another day:
- `VST` BUY @ 132.00 (2026-08-24) — price 152.02, **15.2% above** the level after
  eight weeks. Retire: the level is stale, and re-levelling it would add a third
  power/energy row against XLE and CEG, breaching the correlation cap.
- `OXY` BUY @ 54.00 (2026-09-24) — price 62.38, **15.5% above**. Retire, same
  reasoning plus XLE already carries the energy exposure.
- `GLD` SELL @ 406.77 (2026-09-08) — price 382.01. The thesis **played out
  without ever filling**, so there is nothing left to capture. Retire.
- `ITB` SELL_SHORT @ 89.80 (2026-09-30) — price 86.40, played out unfilled.
  Retire, but note it corroborates the BCC close and the IYR short.
- `AAL` SELL_SHORT @ 13.35 (2026-10-03) — price 11.88, 11% through the level
  unfilled. Earnings 2026-10-22. Retire rather than chase a short 11% lower.
- `KXFEDDECISION-26SEP-H0` YES @ 47 — a **September-dated market, now expired**.
  Must be retired rather than re-reported.
- `KXFEDDECISION-26OCT-H25` YES @ 28 and `KXCPIYOY-26SEP-T3.5` NO @ 18 cannot be
  re-priced at all this run — Kalshi search returns nothing (see the gap note).
  Left untouched rather than restated at a price I could not fetch.
- **Pattern worth stating in the report**: five of nine pending ideas never filled
  and the move happened anyway — four were entries set below the market on longs
  or above it on shorts. That is the fill-rate problem `config/strategy.md`
  already documents (31 pullback entries to 1 breakout, 42% filled) recurring.

## [06:25 ET] REJECTED — the entire weekend lane, with the reason verified
`config/strategy.md` says a Sunday run should lean on crypto and event contracts.
Both are unavailable this run, and I checked rather than assumed:
- **Crypto: spot works, history does not.** `history BTC-USD` and `history BTCUSD`
  both fail every source — nasdaq returns no rows for crypto, Yahoo is 429, and
  twelvedata/alphavantage have no API key. So there is **no ATR, no 20/50-day and
  no 90-day range for any coin**. The crypto swing stop floor is 2.5 ATR; with no
  ATR I cannot place a stop from real structure, and inventing one is exactly the
  fabricated number CLAUDE.md forbids. CoinGecko gives me a price and a 24h
  change and nothing to build levels on.
- **Event contracts: no prices at all.** Kalshi search returns count 0 for CPI,
  Bitcoin, interest rate and government shutdown. An event-contract thesis
  requires stating the market's implied probability against mine; without a
  fetched price that is a made-up number.
- So the two classes that were supposed to carry a Sunday both produce nothing,
  and the report is 100% equity/ETF position management as a result. That is a
  tooling outcome, not a judgement that nothing was out there — worth saying
  plainly in `data_quality_notes` because it is the single biggest limitation of
  this run.

## [06:26 ET] REJECTED — a third rate-driven idea — correlation cap
- The 10y at 5.10% is comfortably the strongest fact available this run, and the
  temptation is to add another expression of it. Declined: TLT short, IYR short,
  CEG (hurt by it), BCC (being closed because of it) and XLF (helped by it) are
  already five rows turning on the same rate path, against a cap of 3 per driver.
- Also declined for the same reason: a short-utilities idea. `XLU` short was
  opened 2026-09-24 and stopped out 2026-10-06 — the same trade, already paid for
  once.

## [06:28 ET] SELF-CHECK — every candidate recomputed against the floors
I recomputed R:R, stop distance in ATRs, and expectancy vs the `1/(1+R:R)`
baseline for all 17 captured ideas from the fetched ATRs, rather than trusting
what I wrote. Ten flags came back. **All ten are deliberate**, and each is
explained below so the red team can tell an intended flag from a mistake.

### Negative expectancy, on purpose (3)
`SMMT` wp 0.18 vs baseline 0.314, `SNX` wp 0.22 vs 0.324, `BCC` wp 0.25 vs 0.433.
These are the three positions being **exited** — two held to their stops, one
closed outright. A stated win probability below the break-even hit rate is the
honest claim for a trade I expect to lose, and inflating it to clear
`check_expectancy` would be precisely the "numbers nudged until they passed"
failure CLAUDE.md documents. If validation demotes these to the watchlist that is
an acceptable outcome; the management instruction still reaches the reader. **Do
not raise these numbers.**

### Reward-to-risk below the long-term floor, on purpose (2)
`HII` 1.68 and `BCC` 1.31 against a 2.5 long-term floor. **The failure IS the
recommendation** — it is the stated reason HII is being halved with its target
marked down from 430.00 (25.63x earnings) to 335.60 (20x), and the reason BCC is
being closed. Raising either target to clear the floor would re-introduce exactly
the undefended multiple being withdrawn.

### Pre-existing sub-floor stops, inherited not chosen (3)
`SNX` 1.82 ATR, `FCX` 1.84 ATR, `CEG` 1.32 ATR from entry, against a 2.0 stock
floor. All three were published that way before today and the entries are filled,
so the stops cannot be re-placed — a filled position's entry is a fact. Recorded
as a finding about how these were published, not as something today's run chose.
**CEG's is the one I understated earlier**: I wrote "1.28 ATR from spot", and from
the 272.00 entry it is 1.32 ATR, which is a floor violation and should be read as
one. Three sub-floor stops among 19 open rows is a pattern worth naming.

### Trailing stops above entry — a measurement artefact, DO NOT "FIX" (2)
`XLE` 1.20 ATR and `NKE` 0.98 ATR from entry. Both are flagged only because the
floor check measures entry-to-stop, and in both cases **the stop is now on the
profitable side of the entry**:
- `XLE` long, entry 63.90, new stop **65.50** — above entry, so the position's
  risk from entry is *negative*; it has a locked-in gain. Forward risk from spot
  (68.24) is **2.06 ATR**, which clears the 1.8 ETF floor.
- `NKE` short, entry 38.40, new stop **39.60** — above entry on a short is also
  the protected side. Forward risk from spot (37.13) is **2.01 ATR**, clearing the
  2.0 stock floor.
A red team applying the ATR floor mechanically here would widen these stops back
toward the entry and **hand back realised gains on two winning positions** — the
opposite of the rule's purpose. The floor exists to stop a *new* entry being
published with a noise-distance stop; it does not describe a trailing stop on an
open winner. Measure these two from spot, not from entry.

### Conviction vs evidence — no inflation anywhere
Claimed conviction is at or below the score the distinct-kind count supports on
all 17. Two are deliberately *below* it: `HII` claims 3 on 3 kinds (4 supported)
because its valuation anchor argues against the trade, and `BCC` claims 2 on 3
kinds for the same reason. Erring low is the safe direction.

## [06:30 ET] CATALYST VERIFICATION — finnhub's calendar was WRONG on GE
Second-sourced the two dates today's most consequential calls depend on. One
confirmed, one did not — and the correction changes the recommendation.

**`GE` — finnhub said 2026-10-19 BMO. The real date is 2026-10-20, 07:30-08:20
EDT.** Confirmed by GE Aerospace's own investor-relations events page
(<https://www.geaerospace.com/investor-relations/events-reports/ge-aerospace-3rd-quarter-2026-earnings-webcast>),
with TipRanks listing "Oct 20, 2026, Before Open (Confirmed)" and MarketBeat
giving the same 7:30am ET call. Third-party aggregators disagreed wildly —
Zacks and ChartRow Oct 20, bullstory Oct 19, EarningsWhispers Oct 15,
MarketScreener a projected Oct 26 — which is itself the lesson.
- **Why it matters:** my first GE capture said the print lands before Monday's
  open, so "there is no action available between reading this and the event".
  That was wrong. The reader has **all of Monday 2026-10-19** to act before a
  Tuesday-morning print. A recommendation built on "you cannot act" has to be
  rebuilt now that the reader can.
- GE recaptured with the corrected date and a real Monday decision window.

**`STLD` — CONFIRMED, and with a material addition.** The company's own
announcement puts Q3 results after market close **Monday 2026-10-19**, call
Tuesday 10-20 at 11:00 ET (Millett/Wagler). Matches finnhub exactly.
- **New and important:** Steel Dynamics' own 2026-09-17 guidance is **$5.34-$5.38
  per diluted share**, while the street sits ABOVE it — finnhub consensus 5.508,
  Zacks ~5.42, another ~5.40. Consensus above a company's own fresh guide is a
  set-up for a technical "miss" against expectations, and it meaningfully
  strengthens the case for cutting size before an AMC print. STLD recaptured
  with this as primary-document evidence.

**Consequence for every other date in this report:** finnhub's earnings calendar
is demonstrably off by a day on at least one name, so the remaining unverified
dates — `UNP` 10-22, `ABT` 10-21, `FCX` 10-27, `HII` 10-29 — should be treated as
approximate to within a day and re-confirmed before acting. I verified the two
inside 36 hours and did not have budget to verify the rest. Flagging this for
`data_quality_notes` rather than leaving the impression all dates are equally
solid.

## [06:30 ET] CATALYST VERIFICATION — round two, UNP and ABT both CONFIRMED
Having caught finnhub out on GE, I second-sourced the other two dates my advice
actually turns on. Both hold, so the calendar is wrong on one of four checked,
not broadly unreliable — worth stating precisely rather than impugning the feed.
- **`UNP` 2026-10-22 CONFIRMED** by the company's own Business Wire release:
  results at **07:45 ET**, call 08:45 ET. My captured `datetime_et` of
  2026-10-22T07:45 is exactly right. Earnings Whispers also lists it confirmed,
  consensus $3.44 (vs finnhub 3.5034).
- **`ABT` 2026-10-21 CONFIRMED** by Abbott's own 2026-09-30 press release:
  results Wednesday 10-21 **before market open**, call 09:00 ET. (One calendar
  page listed 10-19; the company's announcement governs.)
- **New ABT fact that argues AGAINST my own recommendation**, recorded because it
  does: Abbott guided Q3 adjusted diluted EPS to **$1.38-$1.46**, and consensus
  at ~$1.42 sits at the *midpoint* of that range. So the bar is well calibrated —
  the opposite of STLD, where the street is above the company's guide. A tightly
  guided quarter makes a miss less likely than the raw 3-of-4 miss record implies,
  because those misses were against less-anchored estimates.
- I am keeping the WAIT instruction anyway, and the reason is asymmetry rather
  than probability: the entry at 103.00 is a pullback level 1.8% *below* spot, so
  waiting three days costs nothing if the thesis is intact, while pre-positioning
  into a BMO print on a name with net insider selling of $45.55M risks a gap
  through the 98.00 stop. But the guidance calibration is a real point against and
  belongs on the page. ABT recaptured with it.
- **Net correction tally for this run: 1 of 4 fetched dates was wrong (GE), and
  it was the single most consequential one.** Verification earned its budget.

## [06:31 ET] REJECTED — DHR and ISRG — tested the PFE template, neither fits
Last honest attempt at a genuinely new name, in healthcare because that is the
one sector with room under the correlation cap and because the PFE setup worked.
The template is: cheap, analysts negative, insiders buying. Neither matches.
- `DHR` (earnings 2026-10-21): 229.04, extended above both the 20-day (221.47)
  and 50-day (213.90), near its 90-day high of 233.02 after a 38% run off 165.75.
  Beat 4 of 4, but bullish share is **84.4% and deteriorating (-5.6)** and
  insiders are **net -$12.97M with zero open-market buys**. Crowded, extended,
  insiders leaving — the inverse of PFE, not an echo of it.
- `ISRG` (earnings 2026-10-20 AMC): 426.70, also extended above both averages
  (411.16/391.67) near its 90-day high of 443.84 after +30% off 328.57. Genuinely
  strong operationally — four beats averaging well above estimate, revisions
  improving +2.5 — but **zero insider buying, net -$8.08M**, and entering 3.2%
  below a 90-day high into an after-the-close print is a chase. The first month of
  this report was 42% fill rate on entries set below a rising market; this is the
  same mistake with better fundamentals.
- Correlation also binds: PFE and ABT already make two healthcare rows, so a third
  would sit exactly at the 3-idea cap with the weakest evidence of the three.
- **Conclusion: no new symbol clears the bar today, and that is a tested result
  rather than an untested assumption.** Three separate new-idea attempts were made
  and all three were rejected on fetched evidence — regional banks (4 names),
  DHR and ISRG. The report is 100% position management because that is what the
  evidence supported, not because hunting was skipped.

## [06:32 ET] RESEARCH COMPLETE (supersedes the premature 06:11 block)
- **candidates: 21 lines, 17 distinct positions.** Synthesis takes the last entry
  per symbol; GE, STLD and ABT each appear twice and the later entry governs in
  every case (GE for the corrected earnings date, STLD for the guidance release,
  ABT for the confirmed date and guidance range).
- conviction spread: one 5 (STLD), five 4s (ABT, GE, IYR, PFE, UNP), nine 3s, two
  2s (BCC, SNX). Deliberately not clustered — and two are claimed *below* the
  score their evidence count supports (HII, BCC), never above.
- horizons: 14 swing, 3 long_term, 0 intraday. No intraday is correct on a Sunday.
- asset classes: 13 stock, 4 etf. **No crypto, futures or event contracts** — see
  the verified weekend-lane gap; this is a tooling limit, not a judgement.
- all 17 are `Robinhood Stocks`, all large/mid-cap US-listed, so tradeability is
  not in question. Two require margin and are flagged: TLT and IYR shorts.

**The six decisions that matter, in order of urgency:**
1. `STLD` — reduce to half before **Monday's close**, ahead of a company-confirmed
   AMC print. Stop is 1.69 ATR and cannot contain a steel gap; consensus (~5.40-
   5.51) sits above the company's own 2026-09-17 guide of $5.34-$5.38.
2. `GE` — **date corrected to Tuesday 2026-10-20** (not Monday). Hold full size;
   3.24 ATR of stop room absorbs an ordinary gap. You have all Monday to act.
3. `BCC` — **close the full position** Monday. Target was 37.3x trailing earnings
   and the invalidation has fired: a housing thesis needs mortgage rates down and
   the 10-year is 5.10%, 122bp above fed funds. Position is -0.5%, so exit is free.
4. `HII` — halve and mark the target 430.00 → 335.60. At a defensible 20x the R:R
   is 1.68, under the 2.5 long-term floor.
5. `XLE` — raise the stop 60.80 → 65.50, banking +6.8% at the 90-day high.
   `NKE` — take half, tighten 41.00 → 39.60; 1-month relative strength has flipped.
6. `PFE` — keep accumulating below 30.00. Strongest idea in the report: 9.70x
   trailing earnings, four straight beats, insiders +$2.83M net, +16.67% vs SPY
   over three months while analysts are at 38.9% and falling.
- `SMMT` (0.20 ATR) and `SNX` (0.44 ATR) are held to their stops with **no
  widening** — their negative expectancy is an honest statement, not an error.
- `XLF` carries a declared conflict with the `IYR` short and a dated kill
  condition: if the 10-20/10-21 bank prints show money-centre reserve builds, close.

**coverage gaps:** no index/VIX/DXY/gold/WTI level (Yahoo 429, Finnhub refuses
indices, stooq 404s on ^ symbols, no AlphaVantage key); no event-contract prices
at all (Kalshi search returns 0 for every macro topic); **no crypto price history,
so no ATR and no publishable crypto levels**; no options-implied move anywhere
(Yahoo options 401); no small/micro-cap screening (no screener available keylessly
— the three new-idea attempts were name-by-name); three of four open long-term
theses not re-read against current filings (PFE, HII, BCC were; nothing else).
**sources that failed:** query1/query2.finance.yahoo.com (429 indices, 401 options,
429 crypto history), finnhub index quotes (subscription), stooq (404 on ^GSPC/^NDX/
^DJI/^RUT/^VIX), Kalshi market search (empty), api.nasdaq.com short interest
(read timeout), nasdaq crypto history (no rows).
**sources that worked:** finnhub quotes/candles/earnings/recommendations/insiders/
profile, FRED, CoinGecko spot, SEC EDGAR, computed relative strength, web search
and company IR pages for date verification.
**one data error found and corrected:** finnhub's earnings calendar had GE on
2026-10-19; the company says 2026-10-20. 1 wrong of 4 verified.

## [06:33 ET] NOTE ON THE STAMPS IN THIS FILE
A few headings above are out of strict chronological order by two to four minutes
(the regional-bank rejection, the IYR/XLF update, the weekend-lane rejection).
Those stamps are my estimates written between `date` calls, not fetched times —
the same fault recorded in the 06:12 CORRECTION. The `date`-verified anchors are:
run start **06:00**, first-pass end **06:11**, GE date correction **06:27**, final
block **06:30**. Sequence within the file is reliable; individual minute stamps in
the second half are approximate. **No market datum is affected** — every price,
level, multiple and date above carries its own fetched source and `asof`.

## [06:33 ET] COVERAGE CONFIRMATION — all 19 open rows accounted for
Captured as candidates (16): XLE, BCC, PFE, IYR, LULU, NKE, SNX, TLT, CEG, FCX,
XLF, SMMT, STLD, HII, GE, UNP.
Reviewed, hold, no amendment warranted, recorded in the 06:25 block (3): DG, KHC,
CVS — each with 2.2 ATR or more of stop room and no earnings in the window.
Plus ABT, amended from the pending list = **17 distinct captured positions**.
Nothing in the book was left unexamined.
