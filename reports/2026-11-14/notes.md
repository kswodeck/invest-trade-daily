# Research log — 2026-11-14

## [06:03 ET] SETUP — Saturday run, US cash equities and futures closed
- Weekend run per config/strategy.md: crypto and event contracts carry the actionable
  ideas; equities are week-ahead preparation, entry at the next open (Mon 2026-11-17).
- Freshest honest equity price today = Friday 2026-11-13 close. Not stale, just closed.

## [06:03 ET] MACRO — rates (FRED, fetched)
- US 10y 5.10% (2026-11-12) — source: https://fred.stlouisfed.org/series/DGS10
- US 2y 4.86% (2026-11-12) — source: https://fred.stlouisfed.org/series/DGS2
- 10y-2y +0.27 (2026-11-13) — curve positive but flat; long end is the pressure point
- Fed funds effective 3.88% — policy rate well BELOW the 10y: the long end is
  repricing term premium / supply, not near-term policy. This is the key macro fact.
- Unemployment 4.1% (Oct 2026)
- TLT proxy bonds_20y 79.38, -0.43% on 2026-11-13 close
- NOTE: a 5.10% 10y with fed funds at 3.88% is a 122bp positive spread. Open TLT
  position (entry 80.30, last 79.72) is a bet this reverses; it has not yet.

## [06:03 ET] DATA QUALITY — Yahoo Finance returning HTTP 429 on every index/ETF call
- macro: spx, ndx, dow, russell2000, vix, es/nq futures, DXY, us10y_yield, gold,
  wti ALL failed (finnhub needs a paid sub for indices; stooq 404s on ^ symbols;
  no alphavantage key). Only FRED and bonds_20y (TLT) returned.
- Consequence: no VIX, no index level, no DXY, no gold/crude print this run unless
  another source answers. Must be stated in data_quality_notes.

## [06:04 ET] MACRO — crypto (CoinGecko, fetched 11:01 UTC)
- BTC $67,235, -2.97% 24h — source: https://www.coingecko.com/en/coins/bitcoin
- ETH $1,907.67, -2.17% 24h
- SOL $75.68, -5.90% 24h
- XRP $0.9904, -3.06% 24h  | DOGE $0.0629, -3.41% 24h
- Risk is coming OFF into the weekend across the whole complex, with SOL the weakest.
- Relevant to the open book: /MBTZ6 SHORT @ 74,075 published 2026-11-09 never filled
  because BTC never traded back up to it — the direction was right and the entry
  was above the market, which is the pullback-entry failure mode in reverse.

## [06:06 ET] MACRO — the regime, from fetched bars
- SPY 754.37 (Fri 2026-11-13 close). ATR14 12.77 = 1.69% — elevated.
  SMA20 759.02, SMA50 764.43. Price is BELOW both. 90d range 729.10-781.62, -3.49% off high.
- 2026-11-05 was a shock day: open 765.47, low 732.71, close 733.00 on 125.9M shares
  (3x the 30d average of 44.1M). Bounce to 759.81 on 11-11 has already faded.
- Fri 11-13 itself: open 760.07, high 760.12, low 747.88, close 754.37 — opened at the
  high, sold all day, closed mid. Sellers on strength.
- source: Nasdaq daily bars via scripts/market_data.py history SPY --days 90
- READ: this is a long-end-yield / liquidity shock, not a growth scare. 10y 5.10% with
  fed funds 3.88%, unemployment 4.1%. Confirmation it is liquidity and not growth:
  equities, gold AND crypto all fell together. A growth scare bids bonds and gold.

## [06:07 ET] CRYPTO — BTC is in a bear market, not a dip
- IBIT (fetched BTC proxy, 2y of bars): close 38.94, -45.78% from its 71.82 2y high.
  SMA200 41.06 — price is BELOW the 200d. SMA20 44.16, SMA50 45.47. ATR14 1.35 = 3.48%.
  2y range low 32.84. source: market_data.py history IBIT --days 500
- The tape is relentless, not spiky: 11-09 42.32, 11-10 41.68, 11-11 42.24, 11-12 40.36,
  11-13 38.94. Lower closes with no bounce held.
- BTC spot 67,235 now vs an implied Friday close near 69.2k — it has kept falling
  through the weekend session while equities are shut.
- IBIT/BTC ratio from Friday ~1772, so the 2y IBIT low of 32.84 maps to BTC ~58.2k.
- CONCLUSION: no long here. Below the 200d, -46% from the high, making new lows with
  no reversal signature. The only honest crypto expression is short, and per
  config/universe.md that must be a futures contract, not a spot sell.

## [06:10 ET] DATA GAP — Kalshi event-contract search returned nothing usable
- queried: "Bitcoin" (0), "CPI" (0), "inflation" (0), "interest rate" (0), "S&P" (0).
  "Fed" returned 1 market, an unrelated multi-sport parlay with null bid/ask/volume.
- So NO event contract idea can be sourced this run. This is the lane the strategy
  file most wants hunted, and it is unavailable, not unexamined. Must say so in
  data_quality_notes. Open event position KXCPIYOY-26SEP-T3.5 NO @ 18 cannot be
  re-priced either.

## [06:04 ET] NOTE ON TIMESTAMPS
- The four blocks above are labelled 06:03-06:10 but were all written between
  06:01 and 06:04 ET — I estimated elapsed time instead of reading the clock.
  Corrected here rather than rewritten. Timestamps from this point are from `date`.

## [06:05 ET] CALENDAR — next week is the consumer read, and NVDA
- Fetched from finnhub earnings calendar (market_data.py earnings --days 10), 452 events.
- The dated catalysts that matter, all inside a swing horizon:
  - **NVDA — Mon 2026-11-17 AMC**, rev est $111.2B. The single largest event on the tape.
  - HD Tue 11-17 bmo ($44.1B) | DIS Tue 11-17 bmo ($25.4B)
  - TGT 11-18 bmo ($26.8B) | LOW 11-18 bmo ($22.6B) | TJX 11-18 bmo ($16.0B)
    | ROST 11-18 | GAP 11-18 | PANW 11-18 amc
  - WMT Thu 11-19 bmo ($189.1B) | BABA 11-19 bmo | NTES 11-19 | INTU 11-19 amc
  - BJ 11-20 bmo | DKS 11-23 | KSS 11-23 | BURL 11-23 | HPE 11-23
  - DELL 11-24 | HPQ 11-24 | MDT 11-24 | ADI 11-24 | WDAY 11-24
  - PDD 11-16 bmo ($117.1B) | BIDU 11-16 | XPEV 11-16
- THEME: HD, LOW, TGT, TJX, ROST, GAP, WMT, BJ, KSS, BURL all report inside five
  sessions. That is a complete read on the US consumer landing in one week, into a
  tape that just took a 4% single-day hit with the 10y at 5.10%.
- Correlation warning for synthesis: these are ONE bet, not ten. Cap at 3 per
  config/strategy.md. I will not publish a basket of retail earnings longs.
- Note on the open book: DKS BUY @ 144.5 (published 11-13, never filled) now has
  earnings on 11-23 behind it — that is new information on an unfilled level.

## [06:06 ET] REJECTED — /MBTZ6 SHORT — direction right, reward-to-risk fails. Arithmetic:
- BTC spot 67,235 (CoinGecko, 11:01 UTC). BTC ATR from IBIT's 3.48% ATR14 = ~2,340.
- Crypto/futures swing stop floor is 2.5 ATR (config/strategy.md) = ~5,850 minimum.
- Entry 68,500 (zone 68,000-70,000 — a modest bounce to Friday's broken high near
  69,600, NOT the 74,075 that never filled). Stop 74,500, just above the IBIT 42.0-42.7
  shelf of 11-09 to 11-11, whose reclaim would end the downtrend. Risk 6,000 = 2.56 ATR ✓
- Target 58,200 = the 2-year IBIT low of 32.84 at the 1772 ratio. Reward 10,300.
- **R:R = 1.72 against a 2.0 floor. FAILS.**
- To clear 2.0 the target must be <= 56,500, which is BELOW the 2-year low and is a
  number I cannot defend from any fetched level. Entering higher (70,000) shrinks the
  stop to 1.91 ATR and fails the stop floor instead. The geometry is the problem: a
  2.5 ATR stop on a 3.5% ATR instrument costs 8.75%, so the target has to be 17.5% away.
- This is the trap config/strategy.md names outright — an idea that only clears the
  floor with a tight stop has failed the floor. Not published.

## [06:06 ET] POSITION UPDATE — /MBTZ6 — SHORT @ 74,075 (published 11-09) — STAND DOWN
- decision: cancel the resting order; do not chase it lower.
- why: BTC is 67,235, i.e. 9.2% BELOW the published entry, so the order never filled
  and now sits 10% above the market. Re-striking it at a fillable level produces the
  1.72 R:R computed above. The direction was correct and the entry was unreachable —
  that is the pullback-entry failure mode inverted, and the fix is not a lower entry.

## [06:07 ET] REJECTED — crypto longs (BTC, ETH, SOL) — no reversal signature
- IBIT -45.8% off its 2y high, BELOW its 200d (41.06 vs 38.94 close), five consecutive
  lower closes 11-09 to 11-13 (42.32, 41.68, 42.24, 40.36, 38.94) and still falling
  through the weekend. ETH 1,907.67 -2.17%, SOL 75.68 -5.90%, XRP 0.9904 -3.06%.
- SOL is the weakest of the complex, so the "buy the worst" version is worse, not better.
- No capitulation bar, no reclaim of a level, nothing dated. A bear market below the
  200d is not a dip.
- NET: the weekend lane that config/strategy.md says should carry a Saturday report is
  empty in both directions today. Crypto offers no long and no short that clears a
  floor, and the event-contract source returned nothing. So this report is
  week-ahead equity preparation plus management of 15 open positions, and it must
  say that plainly rather than padding the weekend lane.

## [06:08 ET] BOOK REVIEW — all 15 open positions, repriced to Friday 2026-11-13 close
prior_context.md's "Last" column was a day stale on every row; these are fetched.
source: scripts/market_data.py quote (finnhub, asof 2026-11-13T21:00:00Z)

| Symbol | Side | Entry | Stop | Target | Fri close | vs entry | decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BCC | buy | 76.50 | none | 110.00 | 67.39 | -11.9% | **CLOSE** |
| SMMT | buy | 17.10 | 14.40 | 23.00 | 14.15 | -17.3% | **STOPPED OUT** |
| ACM | buy | 66.74 | 61.50 | 77.22 | 70.50 | +5.6% | **TRIM HALF before Mon print** (captured) |
| HII | buy | 262.00 | none | 339.76 | 306.24 | +16.9% | **INSTALL STOP 279.00** |
| TLT | buy | 80.30 | 78.80 | 84.30 | 79.38 | -1.1% | hold, stop unchanged |
| PFE | buy | 27.60 | none | 42.00 | 28.89 | +4.7% | hold, needs an invalidation |
| KHC | buy | 23.00 | 21.20 | 28.09 | 25.11 | +9.2% | hold |
| OXY | buy | 54.00 | 50.15 | 62.00 | 58.75 | +8.8% | hold, 5.5% from target |
| AAL | sell_short | 13.35 | 14.40 | 10.60 | 13.17 | +1.3% | hold |
| UNP | buy | 288.60 | 277.40 | 315.99 | 302.44 | +4.8% | hold |
| ABT | buy | 103.00 | 97.00 | 117.34 | 108.52 | +5.4% | hold |
| PYPL | buy | 56.50 | 54.10 | 62.70 | 59.28 | +4.9% | hold, 5.8% from target |
| RTX | buy | 199.00 | 186.00 | 226.50 | 198.58 | -0.2% | hold |
| XLU | buy | 43.30 | 41.80 | 46.60 | 44.04 | +1.7% | hold, but see rate note |
| ONON | buy | 34.20 | 30.69 | 41.41 | 33.63 | -1.7% | hold |
- 11 of 15 are in profit. The two problems are both positions that were published
  WITHOUT a stop (BCC, and HII in the other direction), which is the one structural
  thing this book keeps getting wrong.

## [06:09 ET] POSITION UPDATE — SMMT — STOPPED OUT, book the loss
- Summit Therapeutics. Entry 17.10 (2026-10-27), stop 14.40, Friday close 14.15.
- The stop was breached intraday on Friday 2026-11-13: low 14.06 against a 14.40 stop.
  It is out at -17.3%. source: Nasdaq bars, 2026-11-13 o15.20 h15.20 l14.06 c14.15
- This was NOT a noise stop-out. ATR14 is 1.3369 = 9.45% of price, and the 2.70 stop
  distance was 2.02 ATR — i.e. it cleared the floor. The thesis was simply wrong:
  17.84 (11-09) -> 17.83 -> 16.64 -> 15.075 -> 14.15, a -20.7% four-session collapse
  with no bounce, -25.9% off the 19.09 high of the last 120 sessions.
- decision: closed at the stop. Do NOT re-pitch — nothing in the move looks like a
  level being defended, and the 11-13 report had already called for a close at 15.075.
- action: no candidate captured. A stop that has already triggered is not an
  instruction, it is a fact, and the report should state it as a realised loss.

## [06:10 ET] POSITION UPDATE — BCC — CLOSE AT MARKET at Monday's open
- Boise Cascade. Entry 76.50 (2026-08-18, 87 days ago), NO STOP, target 110.00,
  Friday close 67.39 = -11.9%.
- decision: close in full at the 2026-11-17 open. This repeats the 11-13 red team's
  call at 67.92; the price is lower and one more negative has landed, so the
  instruction stands rather than being re-litigated.
- Six independent reasons, all fetched, none of them price-alone:
  1. New low. Friday's 66.85 low IS the 120-session range low. Five consecutive lower
     closes: 72.57, 70.42, 69.52, 67.92, 67.39. -23.8% off the 88.43 range high.
  2. Earnings inflected. 2026-09-30 actual 1.04 vs 1.1269 estimate, -7.7% — the first
     miss after +47.2%, +18.3% and +30.8%. source: finnhub stock/earnings?symbol=BCC
  3. Analyst revisions deteriorating: bullish share 54.5%, -9.1 points over four
     months, a buy moved to hold. source: finnhub stock/recommendation?symbol=BCC
  4. No insider conviction: 0 open-market buys and 0 distinct buyers in six months
     against 3 sells totalling $665,841. source: finnhub stock/insider-transactions
  5. The thesis input is moving the wrong way. A building-products long needs lower
     long rates; the 10y is 5.10% with fed funds at 3.88%, and the spread is widening.
  6. The 110.00 target is +63% from the 76.50 entry and +63% from here. It was never
     a defended valuation and at -11.9% it is not a reason to stay.
- ATR14 is 3.5338 = 5.24%, so installing a stop now at the 2.0 ATR floor would sit at
  60.32 — another -10.5% of permission to lose. That is not risk control on a thesis
  with nothing left supporting it, which is why this is a close and not a stop.
- action: close instruction, no candidate. A full exit has no entry/target/stop and
  therefore no reward-to-risk; it must publish as a position instruction, not an idea.

## [06:11 ET] POSITION UPDATE — HII — install a 279.00 stop, hold the position
- Huntington Ingalls. Entry 262.00 (2026-10-12), NO STOP, target 339.76,
  Friday close 306.24 = +16.9%. The largest unprotected gain in the book.
- decision: hold, and install a stop at 279.00. Worst case becomes +6.5% instead of
  the current "whatever happens".
- why 279.00 and not higher: ATR14 is 13.6432, so the 2.0 ATR swing floor from 306.24
  is 278.96, and 279.00 also sits just under the 280.52 SMA50 — a level, not a round
  number. Anything tighter would be the KRE mistake, buying a better-looking ratio by
  making the trade worse. The trend is intact: 306.24 over an SMA20 of 295.14 and an
  SMA50 of 280.52, +19.9% off the 255.36 low of the last 120 sessions.
- IMPORTANT for synthesis — do NOT publish this as a fresh entry at 306.24. From the
  live price the reward is 33.52 and the 2.0 ATR risk is 27.24, an R:R of 1.23 against
  a 2.0 floor. It only looks fine measured from the 262.00 fill, and a filled entry is
  not amendable. This is management of an existing position, not a new buy.

## [06:12 ET] UNFILLED LEVELS — all 9 repriced, and 7 of 9 are the same pathology
source: scripts/market_data.py quote, Friday 2026-11-13 close

| Symbol | Published level | Fri close | gap |
| --- | --- | --- | --- |
| GLD SELL | 406.77 | 355.45 | -12.62% |
| CVS BUY | 79.00 | 89.35 | +13.10% |
| XLV BUY | 184.00 | 188.85 | +2.64% |
| HUN BUY | 9.00 | 9.53 | +5.89% |
| ADM BUY | 68.80 | 72.90 | +5.96% |
| LEN BUY | 79.50 | 83.61 | +5.17% |
| DKS BUY | 144.50 | 149.70 | +3.60% |
| /MBTZ6 SHORT | 74,075 | 67,235 | -9.24% |
- **Every single long sits ABOVE its limit and both shorts sit below theirs.** Not one
  of the eight is on the fillable side. This is precisely the pathology config/strategy.md
  records — 31 pullback entries against 1 breakout, 42% ever filled — and it is now
  8 for 8 against. The entries were reflex discounts off the last print, not levels.
- CONSEQUENCE FOR TODAY: I am setting entries at or near the market, or as genuine
  accumulation zones straddling a fetched moving average, and not as discounts.
- Of the eight, GLD, CVS and HUN were already WITHDRAWN by the 11-13 red team and
  should stay withdrawn. XLV (+2.64%), DKS (+3.60%) and LEN (+5.17%) are still
  plausibly reachable; ADM (+5.96%) rose 2.72% on Friday and is moving away.
- DKS now has earnings on 2026-11-23 behind the unfilled 144.50 limit — new information
  on an old level, and it means filling it late buys a binary.

## [06:14 ET] MACRO — Friday was a rotation, not a selloff. SPY -0.36%, but underneath:
XLP +1.42% | XLC +1.05% | XLE +0.98% | XLF +0.81% | XLV +0.54% | XLU +0.53%
KRE +0.30% | ITB +0.26% | XLRE +0.02% | XLB -0.21% | XLI -0.39% | XLY -0.40%
**XLK -2.01% | SMH -2.99%**
- source: scripts/market_data.py quote, 2026-11-13 closes
- Staples led and semis were dumped on a day the index barely moved. That is money
  leaving long-duration growth for short-duration cash flow, which is the correct
  response to a 5.10% 10y, and it is the same trade as crypto -46% and gold -20.8%.
- Drawdowns off the 150-session high, all fetched: SMH -27.55%, GLD -20.78%,
  IWM -9.06%, XLE -7.40%, SPY -3.49%, XLF -2.27%, XLP -1.12%.
  The dispersion IS the regime: XLF and XLP at their highs, SMH in a 27.5% bear market.

## [06:15 ET] REJECTED — XLP long — the right read, no reward-to-risk. Arithmetic:
- XLP is genuinely the leader: +6.54% 1m vs SPY -2.26% (+8.80pp), +11.43pp 3m,
  +7.05pp 6m, outperforming on all three. Closed Friday AT its high, 92.35, and
  -1.12% below the 93.40 high of 150 sessions. source: market_data.py relstrength XLP --peer SPY
- Entry 92.60. ATR14 1.6429. Stop 88.70, under the 88.87 low of 2026-11-06 = 2.37 ATR,
  clearing the 1.8 ETF floor. Risk 3.90.
- For 2.0 R:R the target must be 100.40 — 4.75 ATR and +8.7% on a 1.78%-ATR defensive
  basket whose entire 6-month range is 80.10 to 93.40. I cannot defend that number.
- **R:R at a defensible 97.00 target is 1.13. FAILS.** Not published.
- This is worth stating as a structural finding rather than a near-miss: a low-ATR
  leader near its range high cannot clear a 2.0 floor with an honest 1.8+ ATR stop,
  because the stop costs 4.2% and the target would have to be 8.4% away. The floors
  screen for buying near the BOTTOM of a wide range, not for buying leadership. So I
  redirected the hunt to de-rated names near support, which is how CAG was found.

## [06:16 ET] REJECTED — BURL — a 4-for-4 beat record breaking down, not basing
- Burlington Stores 242.86, -35.81% off its 378.33 high, +7.06% off its 226.85 low.
- The attraction was real: 4 of 4 beats, the last by +33.0% (2.96 vs 2.2248), and
  20 of 26 analysts bullish with zero sell ratings.
- Rejected on three counts:
  1. It is breaking DOWN, not basing. Friday gapped from a 251.87 close to a 244.00
     open and closed 242.86, the lowest close in the visible window, below both the
     247.83 SMA20 and the 253.80 SMA50, -3.58% on the day.
  2. Zero open-market insider buys against 39 sells worth $14,359,239 in six months.
  3. The 76.9% bullish share with ZERO sell ratings on a stock down 36% is downgrade
     risk ahead of it, not support. Revisions "improving" by +0.9pp over four months
     while the stock halves is stale sentiment, not a tailwind — read the change.
- Earnings 2026-11-23 would make it an unhedged binary on top of all that.
- DATA GAP: market_data.py short BURL timed out (api.nasdaq.com read timeout), so
  short interest and days to cover are unknown for this name.

## [06:17 ET] REJECTED — SMH / semis — the drawdown is real, NVDA on 11-17 makes it a coin flip
- SMH 486.75, -27.55% off its 671.83 high, below the 518.14 SMA20 and the 559.80 SMA50,
  -2.99% on Friday. A genuine bear market in the AI complex.
- No short: a 1.8 ATR stop on a 27.235 ATR is 49.0, so the 2.0 R:R target is 388.75 —
  below the 435.15 low of 150 sessions and a number I cannot defend.
- No long either, and no position at all: NVDA reports 2026-11-17 after the close
  (verified on the fetched calendar, EPS est 2.5225), which reprices the whole complex
  in one print. This report already lost NVDA that way — bought 11-07, stopped 11-10.
- The honest action on semis this week is to have no position into Monday's close.

## [06:18 ET] REJECTED — HD and LOW shorts — the tape falsified the thesis
- The idea was that housing-linked retail should be shorted into a 5.10% 10y with
  HD reporting 11-17 and LOW 11-18. The data says no: HD 348.69 is only -3.79% off its
  362.44 high and ABOVE its 333.83 SMA20 and 312.15 SMA50; LOW 227.73 is likewise above
  both. Both are in uptrends, +25.8% and +27.6% off their 150-session lows.
- Shorting two uptrends into their own earnings because a macro story says they should
  be falling is the trade the tape is already disagreeing with. Dropped.

## [06:18 ET] REJECTED — GLD long at the low — a level with no thesis
- GLD 355.45, -20.78% off its 448.70 high and only +0.72% above the 352.91 low of 150
  sessions, below the 368.78 SMA20 and the 380.91 SMA50.
- The geometry works and the thesis does not. Gold fell in the same liquidation as
  crypto and semis while the 10y went to 5.10% — rising real rates are a gold headwind,
  so "it is at support" is the entire case, and config/strategy.md calls that a trigger
  rather than a catalyst. Also note the report was SHORT GLD at 406.77 and was right;
  flipping long 52 points lower on no new information is whipsaw, not a reversal signal.

## [06:19 ET] METHOD — the screen that produced today's two new ideas
After XLP and BURL both failed for structural reasons, I stopped hunting themes and
ran one mechanical screen instead: **open-market insider buying, then a trailing
multiple from reported EPS, then range position.** Insider buying is the signal
config/strategy.md calls out as strongest exactly where this report is weakest —
telling a cheap name from a broken one — and I had found none anywhere until I looked
for it directly. 36 names screened via market_data.py insiders.
- Zero open-market buys in six months: BCC, TGT, WMT, BURL, GIS, KVUE, SJM, HSY, K,
  APA, VTRS, BMY, MRK, CNC, HUM, UNH, GILD, AMGN, BAX, SOLV, LYB, DOW, MOS, CF, NTR,
  HAS, WBD, PARA, UPS, FDX, KEY, CFG, TAP.
- Buys found: CAG (1 buyer, $510,632, 0 sells), ELV (2 buyers, $1,368,280),
  VFC (2 buyers, $1,302,362, 0 sells), CE (3 buyers, $230,062, 0 sells),
  TFC (1 buyer, $2,224,627), EMN (1 buyer, $159,989), DVN (1 buyer, $199,876),
  CPB (1 buyer, $6,435 — trivial, dismissed).
- The discriminator that mattered was not the buy, it was **whether the stock is still
  near the insider's price.** CAG is 1.0% above it and TFC 3.3%; ELV is 17% above,
  VFC 25-40% above, CE 13% above. A cluster that has already paid out is a different
  trade from the one the insider made.

## [06:20 ET] CAPTURED — CAG buy, long_term, conviction 5 — the best idea today
- Conagra 14.73 = 8.56x trailing EPS of 1.72 (0.41+0.47+0.39+0.45 reported).
- Street 4.0% bullish: 0 strong buy / 1 buy / 14 hold / 8 sell / 2 strong sell.
- 3 of 4 quarters beat; 2026-09-30 beat by +43.9% (0.41 vs 0.285).
- Insider Brase bought 35,000 shares at 14.5895 on 2026-07-17 ($510,632), zero sells.
- Sector is the tape leader: XLP +6.54% 1m vs SPY -2.26%.
- Entry zone 13.90-14.80 in thirds, first tranche 14.40 under the 14.4524 SMA50.
  Target 19.75 = 11.5x the same 1.72. Bear case 12.40 = 8.5x a 15%-eroded 1.46,
  corroborated by the 12.53 low of 200 sessions. R:R 5.35/2.00 = 2.68 vs a 2.5 floor.
- CORROBORATION that the de-rating is sector-wide and real, from the same screen:
  TAP 8.39x, GIS 9.98x, CPB 10.49x, STZ 12.00x, SJM 13.75x, HRL 15.45x, KVUE 16.23x.
  CAG is the cheapest but one, and the only one of them where an insider acted.

## [06:21 ET] CAPTURED — TFC buy, swing, conviction 4 — a different driver
- Truist 49.97 = 10.86x trailing EPS 4.60 (1.16+1.23+1.09+1.12), ALL FOUR beat,
  Street only 37.0% bullish and improving 2.4 points.
- Lyons bought 25,000 @ 48.362 on 10-28 and 21,000 @ 48.3608 on 09-17 = $2,224,627
  on two dates; stock is 3.3% above his price.
- Driver is the one macro tailwind available: 10y 5.10% vs effective fed funds 3.88%,
  a 122bp positive spread, 10y-2y +0.27. Banks fund short and lend long.
- Laggard in the leading sector: XLF -2.27% off its high, TFC -11.08% off its own,
  and the gap has begun closing (+7.3% 1m vs XLF +6.17%).
- Entry 49.97 AT MONDAY'S OPEN, zone 49.20-50.30. Stop 47.50 under the whole October
  base (below the 48.12 low of 10-28 and the 47.83/47.88 cluster), 2.08 ATR.
  Target 56.00 under the 56.195 200-session high. R:R 6.03/2.47 = 2.44.
- Conviction 4 and not 5 deliberately: I did NOT count counter_argument_answered,
  because four beats say nothing about the securities-book mark a 5.10% long end
  creates, and claiming otherwise would be inflating the count.

## [06:22 ET] REJECTED — ELV — the insider cluster already paid
- Elevance 429.69. The signal was real and is spent: Boudreaux bought 2,725 shares and
  Peru 1,000 on 2026-07-17 at 366.05-368.25, and the stock is 17% above that.
- 4 of 4 beats, the last +47.8% (6.99 vs 4.7291), 67.9% bullish improving, 14.16x
  trailing EPS of 30.35 — a good company. The problem is purely geometry: +56.34% off
  its 274.84 low and only -4.66% off its 450.69 high, above all three moving averages.
- A 2.0 ATR stop is 26.62, so the 2.0 R:R target is 483.07, above every price in the
  200-session window. As long_term against a 12x bear case near 330 the ratio is
  under 1.0. Nothing clears. Buying 17% above the insiders is not their trade.

## [06:22 ET] REJECTED — VFC — same shape, further gone
- VF Corp 20.68, +66.04% off its 12.455 low, -7.14% off its 22.2699 high, above the
  SMA20, SMA50 and SMA200. Insiders Carucci and Bracken bought $1,302,362 with zero
  sells — at 14.73, 14.98 and 17.167, so the stock is 25-40% above their prices.
  2 of 4 quarters beat and trailing EPS is 0.97, a 21.3x multiple. Signal spent.

## [06:23 ET] WATCHLIST — CE (Celanese) — a real cluster, wrong moment
- 51.41 = 9.15x trailing EPS of 5.62, -27.28% off its 70.70 high. Five open-market
  buys by three people (Kyrish, Duffie, Murray) on 2026-08-11/14 at 45.51-45.60 with
  zero sells — the biggest cluster by headcount in the whole screen.
- Not captured, for three reasons: the dollars are small ($230,062 across three
  people), only 2 of 4 quarters beat, and it has run +10.6% in five sessions
  (46.49 on 11-06 to 51.41) straight into its 51.7302 SMA200, which is resistance.
  An entry there is buying into the level that has to break.
- TRIGGER to revisit: a pullback to the 48.75 SMA20 with the 46.116 low of 11-06
  holding, or a daily close clearly above 51.73. Stop would be 46.00 under that low
  (2.49 ATR), target ~62.50 at 11.1x, R:R 2.03 — which is too close to the floor to
  publish on a name that is also extended. Wait for the better entry.

## [06:24 ET] POSITION UPDATE — TLT — hold, stop UNCHANGED at 78.80, do not add
- 79.38 against an 80.30 fill (-1.1%). Stop 78.80 is 0.58 away = 0.76 ATR on a 0.761
  ATR14. Five consecutive lower closes: 81.96, 80.88, 80.92, 79.72, 79.38. Below the
  81.0925 SMA20 and the 80.2095 SMA50, -9.58% off the 87.79 high of 150 sessions.
- decision: hold and let the stop do its job. It will probably be hit this week.
- **Explicitly NOT widening the stop.** The thesis is a long-end rally and the long end
  is at 5.10% and rising, so widening is buying more time for a thesis the dominant
  macro force is actively refuting. That is the KRE error run backwards — moving a stop
  to avoid recording a loss is worse than moving it to flatter a ratio, not better.
- Also not closing early: the position is -1.1%, the stop is 0.73% away, and
  front-running your own stop to save 70bp is not a decision worth making. The real
  lesson is upstream — a 1.97 ATR stop on a 0.96%-ATR instrument gives a multi-week
  macro thesis about two days of room, and that was too tight at publication.

## [06:25 ET] POSITION UPDATE — PFE — hold, and the missing piece is an invalidation
- 28.89 against a 27.60 fill (+4.7%), NO STOP, target 42.00 (+52% from here).
  Below the 29.79 SMA20, at the 28.80 SMA50, -8.11% off the 31.44 high of 120 sessions.
- A 42.00 target with no stop is a long-term thesis, and config/strategy.md requires an
  explicit invalidation condition for exactly that shape. The position has run 59 days
  without one, which is the same gap that let BCC fall 11.9% unchallenged.
- decision: hold, and record the invalidation rather than a price stop —
  **a dividend cut, or two consecutive quarters of declining total revenue excluding
  the COVID franchises.** "The price fell" is not an invalidation and 42.00 is not a
  level I re-derived today, so I am not amending the target on no new information.

## [06:26 ET] POSITION UPDATE — OXY — hold, and note the target is now uphill
- 58.75 against a 54.00 fill (+8.8%), stop 50.15, target 62.00.
- New information: OXY has rolled over BELOW both moving averages — 60.50 SMA20 and
  59.76 SMA50 — and sits -9.55% off its 64.955 high. The 62.00 target is now above both,
  so reaching it requires reclaiming the averages first, which was not true when it
  was set. The stop at 50.15 is 4.67 ATR away on a 1.842 ATR14 — unusually loose, so
  there is no stop decision to make.
- decision: hold unchanged. Trim at 62.00 as published rather than extending the
  target; raising a target on a winner that is below its own moving averages is
  wishful, and the ratio was already earned.

## [06:26 ET] POSITION UPDATE — PYPL — hold, but the target IS the resistance
- 59.28 against a 56.50 fill (+4.9%), stop 54.10, target 62.70. Above the 57.91 SMA20
  and the 55.61 SMA50, -5.5% off the 62.73 high of 120 sessions.
- Worth saying plainly: the 62.70 target and the 62.73 range high are the same level.
  The position cannot reach its target without breaking a 120-session high, so expect
  it to stall at 62-62.70 and take the trim there rather than hoping through it.
- decision: hold unchanged.

## [06:27 ET] POSITION UPDATE — KHC, XLU, UNP, ABT, RTX, AAL, ONON — hold, no change
- KHC 25.11 vs 23.00 (+9.2%), stop 21.20, target 28.09 — above the 24.43 SMA20 and
  23.88 SMA50; the 28.09 target is the 120-session high. Working. Hold.
- XLU 44.04 vs 43.30 (+1.7%), stop 41.80 (3.74 ATR on a 0.599 ATR14), target 46.60
  which is the 46.625 range high. Above both averages. Hold — but note the headwind:
  utilities are the most rate-sensitive thing in the book and the 10y is at 5.10%.
- UNP 302.44 vs 288.60 (+4.8%), ABT 108.52 vs 103.00 (+5.4%), RTX 198.58 vs 199.00
  (-0.2%), AAL short 13.17 vs 13.35 (+1.3%), ONON 33.63 vs 34.20 (-1.7%) — all inside
  their published levels with nothing dated inside the horizon and nothing new today.
  Hold unchanged. I am not re-pitching seven positions to fill a report.

## [06:28 ET] CORRELATION — read this before ranking
- CAG (new) and KHC (open, +9.2%) are the SAME driver: a de-rated packaged-food
  multiple re-rating. Two of the permitted three. Do not add a third staple — TAP at
  8.39x and GIS at 9.98x were both examined and both lack the insider confirmation
  that is the whole reason CAG was picked over them.
- TFC (new) is the only financial and the only idea in the book that WANTS a high long
  end. Everything rate-sensitive currently held — TLT, XLU, and BCC until it is closed
  — is positioned for the 10y to fall. That is worth stating: the open book is net long
  duration into a 5.10% 10y, and TFC is the first position pointing the other way.
- The retail earnings cluster (HD, LOW, TGT, TJX, ROST, GAP, WMT, BJ, KSS, BURL) all
  report 11-17 to 11-23 and would have been one bet with ten tickers. Nothing from it
  was captured, which is the correlation cap working rather than a coverage gap.

## [06:29 ET] REJECTED — HBAN — and a DATA INTEGRITY warning on its insider records
- Huntington Bancshares 15.82 = 10.48x trailing EPS of 1.51 (0.38+0.39+0.37+0.37),
  -18.68% off its 19.455 high and only +6.75% off its 14.82 low. The geometry is better
  than TFC's and the screen flagged 7 open-market buys by 2 buyers, $854,780.
- **The insider prices do not survive a look.** Rollins is recorded buying at 19.43 AND
  at 14.855 on the same day, 2026-10-26, and at 20.30, 20.35, 16.46 and 16.50 across
  2026-06-02 to 06-04. The 200-session range is 14.82 to 19.455, so a 20.35 print does
  not exist and a 19.43/14.855 same-day pair cannot both be the common stock. Those
  records are mixing transaction or security types under code P. Only Torgow's 12,700
  at 15.735 on 2026-10-27 is consistent with the tape, and that is ~$199,800 by one
  person — a different fact from "$854,780 by two".
- Rejected on the fundamentals as well, so the data problem is not what decides it:
  only 2 of 4 quarters beat, and revisions are DETERIORATING (-1.6pp to 70.4% bullish)
  where TFC's are improving on 4 of 4 beats. Between two banks at the same ~10.5x
  multiple, TFC is the one with the verifiable insider and the better prints.
- Noting the mechanism because it is reusable: an insider dollar total is a sum of
  records, and a sum is worth nothing until the individual prices are checked against
  the price history. CAG's 14.5895 and TFC's 48.362/48.3608 both check out.
- Also screened with zero open-market buys: ZION, CMA, SNV, VLY, ONB, WAL, PB, CFR, FHB.

## [06:31 ET] DATA GAP — no index, VIX, gold or crude price is obtainable this run
- Tried ^GSPC, SPX, ES=F, GC=F, CL=F, ^VIX through market_data.py quote. All four
  sources exhausted on every one: finnhub returns "Market data subscription required
  for CFD indices", Yahoo returns HTTP 429 on both query hosts, stooq 404s on ^ symbols,
  and there is no alphavantage key.
- CONSEQUENCE: **no equity-index or commodity futures idea is possible today.** /MES,
  /MNQ, /M2K, /MGC and /MCL all need a fetched contract price to set levels and I have
  none. I am NOT deriving an S&P level from SPY 754.37 x 10 — that is a guess with a
  decimal point, and the one rule above all others here is never to state a price I did
  not fetch. /MBT is the only Robinhood futures contract I could price today, from
  CoinGecko BTC, and it failed reward-to-risk at 1.72.
- Also unavailable: the options-implied move. market_data.py implied returns HTTP 401
  from yahoo-options (tested on ACM), so no idea today carries the "is my target inside
  what the market prices" check that config/strategy.md asks for at level-setting.

## [06:32 ET] REJECTED — MP (MP Materials) — the closest call of the day
- The insider signal is the strongest and freshest in the entire 50-name screen, and
  unlike HBAN the prices verify against the tape:
  Weisenburger 55,000 @ 36.00, Rosenthal 17,000 @ 36.27 and 10,000 @ 37.20 (2026-11-10),
  Rosenthal 5,000 @ 37.30 (11-11), Corbett 2,776 @ 35.68 and 2,700 @ 36.84 (11-10).
  Three distinct people, roughly $3.34M, within two sessions, three days ago. The
  2026-11-10 bar ranged 35.60-37.27 and 11-11 ranged 36.71-38.25, so every print sits
  inside its day's range. Verified.
- 38.76, -49.53% off its 76.80 high, +21.5% off its 31.90 low, above the 38.168 SMA20,
  below the 43.9328 SMA50 and the 53.7199 SMA200. Closed Friday strong, 38.76 after a
  39.795 high.
- **Rejected because I cannot anchor a target, not because the signal is weak.**
  Stop 33.30 under the 33.82 low of 2026-11-06 is 5.46 = 2.02 ATR on a 2.7032 ATR14,
  which is the floor met honestly. For 2.0 R:R the target must be 49.68, and every
  candidate for that number fails: 50.00 is a round number, the 53.7199 SMA200 is a
  FALLING average that will be lower by the time price could reach it, and a prior
  consolidation near 50 is not something I can verify — the history call returns only
  20 recent bars. Targeting the SMA50 at 43.9328, the one level I can defend, gives
  R:R 0.95. Reverse-engineering the number to clear the floor is the exact thing
  config/strategy.md forbids, so the idea does not publish.
- Two independent reasons not to stretch for it anyway: trailing EPS is 0.15
  (0.04, -0.01, 0.03, 0.09), a 258x multiple, so there is no valuation anchor at all;
  and the Street is 93.1% bullish and DETERIORATING (-3.3pp) on a stock down 50%, which
  is downgrade risk still ahead of it — the same count that rejected BURL.
- Evidence would have been 2 kinds (positioning, technical_level) = conviction 3, and
  conviction 3 is this report's documented worst bucket: 2 of 27 closed reached target
  (7%), avg -6.9%, on n=43 tracked. That is past the ~15-closed noise threshold, so it
  is a real result and it argues for raising the bar rather than filling the lane.
- TRIGGER to revisit: a close above the 43.93 SMA50 with the 33.82 low intact would
  make the SMA200 a trend target rather than a hope, and 200 sessions of bars would
  let the 48-52 area be checked for a real shelf.

## [06:33 ET] REJECTED — PLAY (Dave & Buster's) — insider buy on a loss-making business
- 8.02, -61.26% off its 20.70 high. Hatton 4,000 @ 6.4999 (09-28) and Lipman 24,000 @
  6.775 (09-17), $188,600, zero sells — but the stock is 18-23% above their prices.
- Decisive against: EPS of -0.36, 0.16, -1.15 and -1.22 over the last four quarters,
  i.e. losing money with 0 of 4 beating. There is no earnings power to anchor a
  valuation and no multiple to re-rate. Average dollar volume is $15M, which clears the
  $500K floor but is thin enough that the position itself would move it.
- Also screened with zero open-market buys: ALB, WHR, NWL, LEG, SWK, MAS, AZEK, TREX,
  CRGY, CIVI, CAKE, SMG.

## [06:35 ET] WATCHLIST — SIRI — Berkshire is buying, and the entry is gone
- **Berkshire Hathaway bought 924,281 shares across three sessions**: 743,965 @ 28.8913
  on 2026-10-30, 66,968 @ 29.466 on 11-02, 113,348 @ 30.233 on 11-03 — about $26.9M,
  filed on Form 4 because Berkshire is a >10% holder. The three prices rise in step with
  a rising tape and sit consistently around the 29.7973 SMA20, so they are coherent;
  I could not check them against their own daily bars, which are outside the 20-bar
  window the history call returns.
- Analyst revisions improved by **+31.0 points** to 50.0% bullish — the largest
  revision swing in anything I screened today. Trailing EPS 2.44 (0.78+0.70+0.72+0.24)
  gives 13.05x at 31.85. Only 1 of 4 quarters beat, which is the blemish.
- NOT CAPTURED, on geometry: 31.85 is +60.53% off the 19.84 low and only -5.66% below
  the 33.76 high, above all three averages. An honest 2.0 ATR stop on a 1.0516 ATR14
  is 29.75 at best; placing it at 28.70 under Berkshire's own lowest print makes risk
  3.15 and the 2.0 R:R target 38.15 — 13% above the highest price in 200 sessions.
  Against a defensible 33.70 target just under the high, R:R is 0.59.
- TRIGGER: a pullback into 29.80-30.25, i.e. back to Berkshire's own range and the
  SMA20, would make risk ~1.5 against a 33.70 target and the ratio work honestly.
  Buying 9% above Berkshire is not Berkshire's trade.

## [06:36 ET] WATCHLIST — INTC — the CEO is $19.7M in and underwater, and I still cannot set levels
- **Lip-Bu Tan bought 150,000 shares at 64.7312 on 2026-11-02 (~$9.71M) and 105,263 at
  95.00 on 2026-08-11 (~$10.0M)** — $19.7M of open-market stock by the chief executive.
  INTC closed Friday at 59.66, so the stock is **7.8% below his November purchase and
  37% below his August one.** Unlike every other cluster found today, this signal has
  not paid and is available cheaper than the insider got it.
- The earnings curve supports him: 4 of 4 quarters beat and EPS rose sequentially
  0.15 -> 0.29 -> 0.42 -> 0.52, a tripling over four quarters. Trailing 1.38 is 43.2x
  at 59.66, so the multiple is a recovery multiple, not a value one.
- Against it: -58.09% off the 142.35 high, below the 73.744 SMA20, the 94.9734 SMA50
  AND the 87.3992 SMA200; analysts 29.1% bullish and deteriorating -5.4 points.
- NOT CAPTURED, and the reason is level-setting rather than the thesis. ATR14 is 6.2185
  = **10.42% of price**, so a 2.0 ATR stop is 21% wide. Put it under the 51.51 low of
  2026-11-05 at 50.90 and it is only 1.41 ATR — fails the stop floor. Widen it to 47.00
  to clear 2.04 ATR and it is no longer on any level I can see, because the history call
  returns 20 bars and the structure between 40.63 and 142.35 is invisible to me. The
  2.0 R:R target from that stop is 84.98, which is a falling SMA200 and +42% away.
- This is the same wall as MP: honest stop, no anchorable target. I would rather publish
  nothing than publish a 21%-wide stop under a level I guessed at.
- TRIGGER: pull 200 sessions of actual bars and find the real shelf between 60 and 90.
  If one exists, this becomes publishable, and it is the first idea I would work on next
  run. **Flagging it as the top coverage gap today.**

## [06:38 ET] STRUCTURAL FINDING — why today produced three ideas and not twelve
Worth recording, because it is about the tape and the floors rather than the effort.
- Nine genuinely interesting setups were rejected on arithmetic, not on judgement:
  XLP (R:R 1.13), /MBTZ6 (1.72), BURL, ELV (<1.0), VFC, SMH, HBAN, MP (0.95 on the only
  defensible target), SIRI (0.59), INTC (no anchorable target), CE (2.03, too close).
- The pattern: after the 2026-11-05 shock, ATR is elevated everywhere, so a 2.0 ATR stop
  costs a lot of price — 4.2% on XLP, 8.75% on BTC, 21% on INTC. The 2.0 reward-to-risk
  floor then demands a target twice that far. Names clear it only if they sit near the
  BOTTOM of a wide range. Everything that already recovered (ELV +56% off its low,
  VFC +66%, SIRI +60%, KSS +111%) has no room left; everything still falling (BURL, SMH,
  BCC, crypto) has no base to put a stop under.
- The two that did clear are the two with LOW volatility relative to their range
  position: CAG at a 3.38% ATR basing above its SMA50 after a 27.5% de-rating, and TFC
  at a 2.37% ATR coiling in an eight-session shelf. That is not a coincidence and it is
  what the floors are for.
- So three ideas is the honest count today, and config/strategy.md is explicit that
  publishing fewer beats padding. I did not stop early: 50 names were screened for
  insider buying and 11 setups were taken to full level-setting before being rejected.

## [06:39 ET] RESEARCH COMPLETE
- candidates captured: 3 — CAG (buy, long_term, conviction 5), TFC (buy, swing,
  conviction 4), ACM (buy, swing, conviction 4, a POSITION UPDATE not a new idea).
- position instructions carried in notes for synthesis to publish, NOT as candidates
  because a close or a stop-install has no entry/target/stop triple and therefore no
  reward-to-risk: **BCC close at market**, **SMMT stopped out at 14.40 (fact, book it)**,
  **HII install a 279.00 stop**, PFE record an invalidation, TLT hold stop unchanged,
  OXY/PYPL hold and trim at target, and seven holds with no change.
- withdrawn / stood down: /MBTZ6 short @ 74,075 (unfillable, 9.2% through it);
  GLD, CVS, HUN stay withdrawn from 11-13.
- coverage gaps, in priority order:
  1. **INTC** — the CEO is $19.7M in and underwater; blocked only by not having the
     mid-range bars to anchor a target. Work this first next run.
  2. **Event contracts entirely** — Kalshi search returned 0 markets for Bitcoin, CPI,
     inflation, interest rate and S&P, and one unrelated sports parlay for "Fed". The
     lane config/strategy.md most wants hunted on a weekend was unavailable, not skipped.
  3. **All index and commodity futures** — no ^GSPC, SPX, ES=F, GC=F, CL=F or ^VIX price
     from any of the four sources, so /MES, /MNQ, /M2K, /MGC and /MCL could not be
     priced and none was published.
  4. **Options-implied move** — yahoo-options returns HTTP 401, so no idea carries the
     implied-move check.
  5. **Short interest** — api.nasdaq.com timed out on BURL; not retried elsewhere.
  6. Small and micro caps: screened (PLAY, MP, CE, EMN and others) and none cleared.
     No sub-$2B name is in today's three.
- sources that failed: Yahoo Finance (HTTP 429 on every index symbol, 401 on options),
  finnhub indices (subscription required), stooq (404 on ^ symbols), alphavantage (no
  key), Kalshi events (empty), api.nasdaq.com short interest (timeout on BURL).
- sources that worked: finnhub quotes/earnings-calendar/insider-transactions/
  recommendations, Nasdaq daily bars, FRED, CoinGecko, SEC EDGAR filing index.

## [06:41 ET] INTC — GAP CLOSED, AND THE ANSWER IS STILL NO (supersedes the 06:36 note)
I said at 06:36 that INTC was blocked on not having the mid-range bars and was the top
item for next run. I then got them, so here is the resolution rather than a hand-off.
Called `market_data._load_bars('INTC', 400)` directly — `history` hardcodes
`rows[-20:]` for its `recent` field, which is why the structure was invisible; the
loader itself returns 551 rows from Nasdaq. Monthly OHLC, 2025-11 to 2026-11:

| Month | open | high | low | close |
| --- | --- | --- | --- | --- |
| 2025-11 | 40.25 | 40.59 | 32.89 | 40.56 |
| 2025-12 | 39.86 | 44.02 | 34.95 | 36.90 |
| 2026-01 | 37.77 | 54.60 | 37.76 | 46.47 |
| 2026-02 | 45.63 | 51.49 | 42.88 | 45.61 |
| 2026-03 | 44.20 | 49.17 | 40.63 | 44.13 |
| 2026-04 | 45.00 | 95.69 | 44.98 | 94.48 |
| 2026-05 | 93.20 | 132.75 | 92.61 | 114.68 |
| 2026-06 | 109.43 | 142.35 | 98.33 | 139.63 |
| 2026-07 | 135.00 | 135.74 | 81.79 | 90.20 |
| 2026-08 | 88.40 | 107.57 | 85.14 | 89.51 |
| 2026-09 | 86.84 | 127.44 | 85.72 | 120.23 |
| 2026-10 | 118.73 | 126.00 | **63.20** | 65.76 |
| 2026-11 | 65.40 | 65.72 | 51.51 | 59.66 |

- The real levels do exist: a three-month shelf at **81.79 / 85.14 / 85.72** (the July,
  August and September lows), the **98.33** June low above it, and below the market the
  **51.51** November low and then the **40.63** March low — with a structural VOID
  between 51.51 and 40.63, because April 2026 gapped 45 to 95 and never traded back
  through it. That void is why no stop can sit at 2.0 ATR: 2.0 ATR is 47.22 and there
  is no level there at all.
- Best honest construction, from the market: entry 59.66, stop 40.00 under the March
  low (19.66 = 3.16 ATR), target 98.33 at the June low. **R:R = 38.67 / 19.66 = 1.97.
  Fails 2.0.** It only clears on a 55.00 entry (R:R 2.89), which is a 7.8% discount off
  the market — the exact pathology that left eight of this report's nine unfilled
  longs stranded — on a target 65% away.
- **And the decisive objection is not arithmetic.** INTC opened October at 118.73 and
  printed 63.20 inside the same month, a ~47% collapse, and I cannot say why. The 8-K
  of 2026-10-29 and the 10-Q of 2026-10-30 (period ended 2026-09-26) are where the
  answer is and I have not read them. Separately, an S-3ASR with a 424B5 and an FWP on
  2026-08-10 to 08-12 is an equity offering — dilution — and Lip-Bu Tan's 95.00
  purchase on 08-11 sits inside that window, which changes what that buy means.
- Publishing a long on a name that halved in a month for reasons I have not established
  would be the opposite of research. **INTC is rejected, not deferred.**
- What is genuinely worth carrying forward is the method, not the ticker:
  `history`'s 20-bar `recent` window hid real structure on every name today. MP and
  SIRI were both rejected partly for "unverifiable levels" and both deserve a re-look
  through `_load_bars` rather than `history`. **That is the top coverage gap — a tool
  limitation I worked around only on the last name, not a missing ticker.**

## [06:42 ET] RESEARCH COMPLETE — FINAL (supersedes the 06:39 block)
- candidates captured: **3** — CAG (buy, long_term, conviction 5), TFC (buy, swing,
  conviction 4), ACM (buy, swing, conviction 4, a POSITION UPDATE, not new risk).
- Nothing was captured after 06:21; the remaining 20 minutes went on falsification,
  which rejected MP, SIRI, INTC, HBAN, PLAY, ELV and VFC. That is the 10% of budget
  config/strategy.md allocates to it, spent as intended.
- unchanged from the 06:39 block: the position instructions (BCC close, SMMT stopped
  out, HII install a 279.00 stop, PFE invalidation, TLT hold stop unchanged, OXY and
  PYPL trim at target, seven holds), the stand-down on /MBTZ6, and the failed sources.
- revised coverage-gap priority:
  1. **`history` returns only 20 recent bars**, so levels beyond a month are invisible.
     Use `market_data._load_bars(sym, 400)` instead. This silently weakened every
     level-setting decision today.
  2. Event contracts — the whole lane, unavailable (Kalshi returned 0 markets).
  3. Index and commodity futures — no price from any source, so no /MES, /MNQ, /MGC, /MCL.
  4. Options-implied move — yahoo-options HTTP 401.
  5. What happened to INTC in October 2026 — read the 2026-10-29 8-K and the 10-Q.

## [06:45 ET] LEVEL RE-CHECK on full history — one of my own claims was wrong
Re-pulled MP, SIRI, CAG and TFC through `_load_bars(sym, 400)` instead of `history`,
15 months of monthly OHLC each. Three confirmations and one correction.

**MP — rejection CONFIRMED, now on real levels rather than missing ones.**
Monthly lows back to 2025-09: 31.90 (Nov 2026) is the lowest of the 15. Above it sit
37.11 and 37.81 (Oct/Jul lows), 40.65 (Aug), a 44.43/44.75 shelf (Mar/Sep), 48.65
(Oct high), then 52.42/53.57/53.89. From 38.76 with the stop at 31.50 under the
all-window low, risk is 7.26 (2.69 ATR) and the ratios are: 48.65 target -> **1.36**,
52.42 -> **1.88**, 53.89 -> 2.07 at +39%. It fails on verified structure. Settled.

**SIRI — rejection CONFIRMED and the reason is now exact.**
The 33.76 November high is the highest print in all 15 months; July 2026's 32.66 was
the prior one. There is no resistance above the market to target, because the market
IS the high. Stop 28.70 under the 28.85 July low is 3.0 ATR, risk 3.15, and a 33.70
target gives **0.59**. Berkshire's 924,281 shares at 28.89-30.23 were bought into a
range it has since left. Settled.

**CAG — my captured levels hold, and the structure adds a point in their favour.**
Feb 2026 high 20.32 and Jun 2026 low 12.53 both match what I used. The bear case of
12.40 sits below BOTH observed lows, 12.53 (Jun) and 12.88 (Oct) — good. The entry
zone is live: the November low is 14.28, so the 14.40 first tranche is reachable and
13.90 sits in Sep/Oct territory (13.27, 12.88).
NEW and favourable: resistance above runs 15.54 (Nov high), 15.70 (Jul), 16.07 (Apr),
16.36 (Sep), 16.73 (Aug) — **and then nothing at all until 19.48.** CAG collapsed
through that zone inside March 2026 (19.48 high to 15.04 low in one month) and has not
traded there in the eight months since. So the 19.75 target, which is defended on
valuation at 11.5x and not on the chart, also sits above a vacuum rather than above a
wall. Once 16.73 goes there is no supply until the target.

**TFC — CORRECTION. My own evidence overstated the stop.**
I wrote that the 47.50 stop sits "under the entire October base". That is **wrong**,
and it came from reading a 70-day window that began on 2026-10-19. On the full history:
- October 2026 low was **45.05** and September 2026 low was **46.16** — both BELOW the
  47.50 stop, not above it.
- What is true: 47.50 is below the eight-session shelf at 49.16/49.185/49.235, below the
  48.12 low of 10-28, below the 47.83/47.88 cluster of 10-21 and 10-23, and 2.08 ATR
  from the entry. It clears the mechanical floor. It does NOT sit under the autumn base.
- Consequence, stated rather than buried: a drift back to 46-45 stops this out without
  breaking any 15-month structure. Moving the stop to 44.90 under the October low makes
  risk 5.07 (4.28 ATR) and the ratio **1.19**, which fails — so widening is not available
  and the idea has to be taken with the stop where it is, or not at all.
- Also now visible: the path from 49.97 to the 56.00 target crosses FOUR layers of
  supply — 51.89 (Sep high), 52.26 (Nov high), 53.53 (Aug high), 54.22 (Jul high) —
  before the 56.20 February high the target sits under. The published scale plan already
  trims half at 52.26, which was the right instinct; the rest of the stack was not
  something I had seen when I set it.
- ACTION: re-captured TFC with the corrected technical_level evidence and both facts in
  key_risk. Levels unchanged — entry 49.97, stop 47.50, target 56.00, R:R 2.44 — because
  they still clear the floors; only the description of them was false, and a red team
  checking the October low would have caught it.
- METHOD NOTE: this is the second time in ten minutes the 20-bar window produced a wrong
  statement. Any level claim sourced from `history` alone should be treated as unverified.

## [06:48 ET] ACM — SECOND CORRECTION, and it reversed my own instruction
Checked `validate_report.check_stop_distance` rather than assuming how it measures.
It computes `abs(entry - stop) / atr` — **from `entry.ideal`, not from the live price.**
- My first ACM capture raised the stop from the published 61.50 to 64.40 to "protect the
  gain". From the 70.50 market that is 2.80 ATR and looks fine. From the 66.74 FILL it is
  2.34 / 2.1749 = **1.08 ATR**, against a 2.0 floor for a swing stock. A hard fail.
- The error was conceptual, not arithmetic. **Tightening the stop on a filled position to
  protect a profit is the same forbidden move as tightening one to flatter a ratio** —
  it buys a better-looking number by making the trade worse, which is the KRE lesson
  pointed at a winner instead of a loser. A profit is protected by selling, not by
  moving a line.
- So the stop stays at the published 61.50 (2.41 ATR from the fill) and the whole
  instruction is carried by the trim: **half off at Monday's open, before the print.**
- A second defect in the same capture: I claimed win_probability 0.32 against an R:R of
  2.0, whose break-even baseline is 1/(1+2) = 33.3%. That is **negative expectancy** and
  a hard failure — I had published an idea that loses money at its own numbers. The
  honest figure is assessed from the live 70.50, where the target is 9.5% away and the
  stop 12.8% away: 0.48, a 14.7-point claimed edge. And the deeper reading is that if I
  could not honestly clear 33.3% on the balance, the correct action would have been the
  full close the 11-13 red team called for.

## [06:50 ET] VERIFICATION — all three candidates run through the real check functions
Imported `validate_report` and ran `check_stop_distance` plus the R:R, expectancy and
evidence-count arithmetic against the last entry per symbol. Results:

| Idea | stop distance | R:R vs floor | win prob vs baseline | kinds |
| --- | --- | --- | --- | --- |
| CAG long_term | n/a — bear case, no ATR floor | **2.675** vs 2.5 PASS | 0.45 vs 0.272, +17.8pp | 4 -> 5 |
| TFC swing | 2.08 ATR, clears 2.0 (warn: under the 2.5 guide) | **2.441** vs 2.0 PASS | 0.40 vs 0.291, +10.9pp | 3 -> 4 |
| ACM swing | 2.41 ATR, clears 2.0 (warn: under the 2.5 guide) | **2.00** vs 2.0 PASS | 0.48 vs 0.333, +14.7pp | 4 -> 5 |

- No FAILs. Two WARNs, both the same: a stop that clears the 2.0 floor but sits under the
  2.5 ATR level where this report's stop-outs have clustered. Stated rather than fixed,
  because widening either one breaks its reward-to-risk (TFC at 44.90 gives 1.19) and
  the rule is that an idea needing a tighter stop has failed — not that an idea may be
  re-cut until both numbers look good.
- ACM's four evidence kinds support a 5; it is left at 4 deliberately. It is a trim
  instruction on money already at risk, and promoting it to the report's top conviction
  tier would pull 4-5% sizing toward a position being reduced to 1.5%.
- ACM's R:R is exactly 2.00, which is the ratio the idea was originally published with
  on 2026-11-07 — unchanged, because entry, target and stop are all unchanged. It is at
  the floor rather than over it, and that is the published trade, not a new one.

## [06:51 ET] RESEARCH COMPLETE — FINAL
- **3 unique candidates in candidates.jsonl (5 lines; TFC and ACM were each re-captured
  after I found errors in my own first versions — synthesis takes the last per symbol).**
  CAG buy long_term conviction 5 | TFC buy swing conviction 4 | ACM buy swing conviction 4
- All three verified against validate_report's own functions: no failures.
- Two self-corrections are logged above and both mattered: TFC's stop was described as
  under a base it is not under, and ACM's was tightened into a 1.08 ATR floor breach
  while carrying a below-baseline win probability. Both were found by checking my
  sources and the validator instead of trusting my own earlier arithmetic — which is
  the one habit CLAUDE.md says this pipeline exists to enforce.
- Position instructions for synthesis to publish from these notes (not candidates,
  because a close or a stop-install has no entry/target/stop triple and so no R:R):
  **BCC close at market Monday**, **SMMT stopped out at 14.40 — a fact, book -17.3%**,
  **HII install a 279.00 stop**, PFE record an invalidation, TLT hold with the stop
  unchanged at 78.80, OXY and PYPL hold and trim at target, KHC/XLU/UNP/ABT/RTX/AAL/ONON
  hold with no change. Stand down the unfillable /MBTZ6 short at 74,075; GLD, CVS and
  HUN stay withdrawn.
- Elapsed: 06:00 to 06:51 ET. 50 names screened for insider buying, 11 setups taken to
  full level-setting, 3 published. The weekend lanes config/strategy.md leans on were
  both unavailable or unqualified — event contracts returned zero markets, and crypto
  offered no long (bear market under its 200d) and no short that clears a floor (1.72).
