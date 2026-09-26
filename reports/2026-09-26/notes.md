# Research log — 2026-09-26

## [06:03 ET] MACRO — Saturday 2026-09-26, US equities and futures CLOSED
Weekend run. Per config/strategy.md weekend behavior: equities treated as
week-ahead preparation (entry at next open, Monday 2026-09-28), crypto and
event contracts carry the actionable weight.

Rates (FRED, fetched):
- US10Y 5.18% as of 2026-09-24, prev 5.11% — up 7bp. source: https://fred.stlouisfed.org/series/DGS10
- US2Y 4.87% as of 2026-09-24, prev 4.85% — up 2bp. source: https://fred.stlouisfed.org/series/DGS2
- Fed funds (DFF) 3.88% as of 2026-09-24, unchanged. source: https://fred.stlouisfed.org/series/DFF
- 10y-2y spread +0.36 as of 2026-09-25, prev +0.31 — STEEPENING. source: https://fred.stlouisfed.org/series/T10Y2Y
- Unemployment 4.1% (Aug 2026), unchanged from prior. source: https://fred.stlouisfed.org/series/UNRATE
- CPIAUCSL 334.131 (Aug 2026) vs 332.813 (Jul 2026) = +0.40% MoM, ~4.9% annualized.
  source: https://fred.stlouisfed.org/series/CPIAUCSL

READ: This is a bear steepener with the long end at 5.18% while the policy rate
sits at 3.88%. The 10y is 130bp ABOVE fed funds — the market is pricing term
premium/inflation risk, not growth. Monthly CPI at +0.40% is hot, not
disinflationary. That combination is hostile to long-duration equity proxies
(utilities, REITs, long Treasuries) and supportive of the short-TLT / short-XLU
positions already open.

- TLT 79.32 last, prev_close 79.42, as of 2026-09-25T20:00Z (session CLOSED,
  age 841 min = previous close, NOT stale — Saturday). source: finnhub via market_data.py

Crypto (CoinGecko, fetched 2026-09-26T10:01Z, 24/7 market so this is LIVE):
- BTC $83,986, -0.68% 24h, $30.6B vol, $1.687T cap
- ETH $2,681.12, -0.85% 24h, $11.9B vol
- SOL $119.92, +1.35% 24h
- LINK $14.02, -0.53%; DOGE $0.097146, +0.52%; AVAX $10.60, +1.71%
  source: https://www.coingecko.com/

## [06:03 ET] DATA QUALITY — Yahoo Finance returning HTTP 429 on every index symbol
spx, ndx, dow, russell2000, vix, es/nq futures, DXY, us10y_yield, gold, wti all
FAILED across finnhub (index subscription required), yahoo (429), stooq (404),
alphavantage (no key). Index levels for today are UNKNOWN — will not state one.
Finnhub DOES serve individual equities/ETFs, so ETF proxies are the workaround
(TLT worked). FRED served all rate series.

## [06:06 ET] DATA QUALITY — Kalshi event-contract search returning nothing usable
`market_data.py events` returned count=0 for: "Fed", "CPI", "FEDDECISION",
"Federal Reserve", "recession", "Bitcoin", "inflation", "shutdown",
"interest rate". An empty query returned 40 markets, all NFL/tennis parlays.
So the endpoint is reachable but the macro series are not matching the search.
I will NOT recommend an event contract whose price I could not fetch — prior
context shows three KXFEDDECISION lines already awaiting entry, and re-pitching
them at a remembered price would be a fabricated number. Logged as a gap.

## [06:07 ET] POSITION UPDATE — CAG — opened 2026-09-20, entry 15.00, last 14.32, -4.5%
Fetched history (nasdaq, 120d): last_close 14.32, ATR14 0.3986 (2.78%),
SMA20 15.194, SMA50 15.2602, range 12.53-16.735, avg $ vol 30d $151.9M.
- Standing stop 14.20. Price is 0.12 above it = **0.30 ATR**. One ordinary day
  takes it out. 2026-09-25 low was 14.22 — it already nearly touched.
- Tape: closes 15.18 (09/17) -> 15.13 -> 14.86 -> 14.78 -> 14.78 -> 14.67 ->
  14.32. Seven sessions, lower highs and lower lows, a new low for the move at
  14.22 on 09/25. Price is below SMA20 AND SMA50, both of which are flat-to-down.
- decision: **CLOSE EARLY / do not widen the stop.** The de-rating thesis wanted
  a base; what the tape gave was a fresh lower low on rising volume. Widening
  14.20 to give it room is exactly the stop-walking this repo demotes ideas for,
  in reverse. Taking -4.5% now beats waiting for -5.3% at the stop, and the
  0.30 ATR remaining means the stop carries no informational content anymore.
- action: captured via add_candidate.py as an update, direction sell to exit.

## [06:08 ET] TIMESTAMP CORRECTION
Wall clock via `date` is 06:06-06:08 ET. My stamps above (06:03-06:07) ran
slightly ahead of the real clock. All stamps from here are taken from `date`.
Nothing about the findings changes; only the minute labels were optimistic.

## [06:09 ET] CATALYST CALENDAR — fetched, next 12 sessions (finnhub)
The dated events worth trading, largest first:
- **2026-09-28 NKE** — eps est 0.4444, rev est $11.45B  <- open position BOTH sides
- 2026-09-28 bmo CCL — eps est 1.3712, rev est $8.38B
- 2026-09-29 bmo KMX — eps est 0.7199, rev est $7.05B
- **2026-09-29 CAG** — eps est 0.2842, rev est $2.61B  <- open position
- 2026-09-29 amc CNXC — eps est 2.7591, rev est $2.53B
- **2026-09-30 amc MU** — eps est 32.3202, rev est $52.24B  <- awaiting entry @960
- 2026-09-30 bmo JBL — eps est 4.0999; 2026-09-30 JEF — 0.9353
- 2026-10-01 bmo ACN — eps est 3.2131, rev est $18.21B
- 2026-10-05 MKC; 2026-10-06 STZ, RPM, LW; 2026-10-07 LEVI; 2026-10-08 PEP
source: https://finnhub.io/ via `market_data.py earnings --days 12`

## [06:10 ET] CAG — REVISED, supersedes the 06:07 entry above
**CAG reports 2026-09-29 (eps est 0.2842, rev est $2.61B).** This materially
strengthens the exit and I had not seen it when I first wrote the block.
A 0.12-wide stop (0.30 ATR) into an earnings print is not a stop at all — a
gap prints straight through it and the fill is wherever the tape opens, which
is the one scenario where "the stop protects me" is false. Holding a -4.5%
loser through a binary event on a 0.30 ATR leash is the worst of the three
choices available. Exit Monday 09-28, the session BEFORE the print.
- decision: **close early at Monday's open, ahead of the 09-29 print.**
- re-captured via add_candidate.py with the dated catalyst as evidence.

## [06:11 ET] NKE — the day's most important name. Earnings Monday 2026-09-28.
Two open rows conflict and must be reconciled in the report:
- `NKE` BUY opened 2026-08-17 @ 40.75, target 62.0, **no stop**, last 35.75 (-12.3%)
- `NKE` SELL opened 2026-09-08 @ 38.40, no target/stop (an exit call), +6.3%
The 09-08 exit call was correct — price fell from 38.40 to 35.75.

Fetched facts:
- Price 35.75 (2026-09-25 close). Range low **35.2159** — only **+1.52%** above it.
  Range high 68.49, so **-47.8% off the high**. ATR14 0.9099 = 2.55%.
  SMA20 37.0985, SMA50 39.6824. Below both; both rolling over.
  avg 30d dollar volume $1.14B — deeply liquid.
  source: https://www.nasdaq.com/market-activity/stocks/nke/historical
- **Serial beats on a cut bar**: +50.15% (Q 2026-06-30), +22.89% (2026-03-31),
  +39.22% (2025-12-31). Three straight beats of 20-50%.
  source: https://finnhub.io/
- **Insider cluster, 4 distinct buyers, 5 open-market buys, $3.73M bought vs
  $1.57M sold, net +$2.16M (6m)**. CEO **Elliott Hill bought 47,320 sh @ ~$42.27
  on 2026-04-13**; **Tim Cook bought 25,000 sh @ $42.43 on 2026-04-10**. Both are
  ~15-18% UNDERWATER at 35.75 — this is conviction buying that has been wrong so
  far, which is a caveat, not a negation. source: https://finnhub.io/
- **8-K filed 2026-09-16 (Item 5.02, event 09-15), READ**: Board expanded 11->12,
  **Alexandre Arnault appointed** — Deputy CEO of Moet Hennessy at LVMH, ex-Tiffany
  and RIMOWA, boards of Birkenstock, Carrefour, Moncler. $200K sign-on RSU.
  source: https://www.sec.gov/Archives/edgar/data/320187/000032018726000170/nke-20260915.htm
  A luxury brand operator joining a brand-repair story is a real governance signal
  but it is NOT confirmation of a two-week swing thesis, so I am deliberately NOT
  counting it in `evidence` — it goes in the thesis text. Counting it would take
  the score to 5 and that would be inflation of exactly the kind this repo tracks.
- **Analyst revisions DETERIORATING**: bullish share 39.1%, -9.8pp. buy 12->8,
  hold 21->25, sell 2->3 since June. source: https://finnhub.io/
- **Relative strength is worst-in-class**: NKE 6m -31.34% vs SPY +19.57% =
  **-50.91% vs benchmark**; 1m -8.05% vs SPY, -1.73% vs XLY. It is lagging even
  its own sector. source: computed via `market_data.py relstrength NKE --peer XLY`
- `implied NKE` FAILED (yahoo-options 401) and `short NKE` FAILED (nasdaq read
  timeout) — so I have NO options-implied move and NO short-interest read. Noted.

DECISION: **Do not buy before the print, and do not sell 1.5% off the range low
either.** Correct action is a conditional post-print entry — `wait: true`. A long
ahead of Monday has no stop that survives the gap, and the RS/revision evidence
says this knife is still falling; but flattening the existing long into a company
that has beaten by 20-50% three quarters running is selling the asymmetry.
Levels below are set stop-first per config/strategy.md.

## [06:13 ET] MACRO — THE KEY READ OF THE DAY: the tape is extremely narrow
All figures are 2026-09-25 closes, fetched OHLCV, 150-day windows.

| ETF | Close | % off high | vs SMA20 | vs SMA50 |
| --- | --- | --- | --- | --- |
| SPY | 771.35 | **-1.03%** | above (765.35) | above (761.57) |
| XLK | 196.27 | **-1.24%** | above (188.42) | above (184.47) |
| XLY (discretionary) | 110.56 | -9.52% | BELOW (112.92) | BELOW (114.82) |
| XRT (retail) | 82.47 | **-11.82%** | BELOW (84.36) | BELOW (87.23) |
| XLP (staples) | 82.06 | -8.88% | BELOW (83.66) | BELOW (84.71) |
source: https://www.nasdaq.com/market-activity/ via `market_data.py history`

**The index is within 1% of its high while the entire consumer complex is in a
downtrend.** Discretionary AND staples AND retail are all below both moving
averages together — which rules out a defensive rotation, because defensives are
falling too. When discretionary and staples fall at the same time it is not
positioning, it is the consumer.

This is consistent with, and probably caused by, the rate picture: 10y at 5.18%
against 3.88% fed funds and CPI running +0.40% MoM. Real income squeeze plus a
high cost of credit. The index is being carried by tech (XLK -1.24% off high).

**It also explains the single-name tape.** Every consumer name I priced this
morning is at or near its low:
- STZ 113.63, range low **113.335** — sitting ON the low, -32.6% off high, SMA20 123.04 / SMA50 128.92. Earnings 10-06.
- CCL 22.25, range low 21.45, -32.56% off high, SMA50 25.42. Earnings 09-28.
- NKE 35.75, range low 35.2159, -47.8% off high. Earnings 09-28.
- CAG 14.32, new low for the move. Earnings 09-29.
- LEVI 19.73, -23.23% off high, SMA50 22.13. Earnings 10-07.
- KMX 57.21, -12.36% off high, SMA20 59.81 / SMA50 59.39. Earnings 09-29.
Plus already in the book and underwater: LULU -11.6%, KHC awaiting, DG awaiting.

**Consequence for today's NKE idea — noted against my own candidate.** The sector
backdrop is hostile and this is the strongest argument against that trade. It is
why the NKE entry is `wait: true` and conditional on a post-print reclaim of
37.10 rather than a bid: in this tape the falling-knife branch must not fill.

## [06:14 ET] REJECTED — STZ — at its 113.335 range low, 13% below SMA50, no base. Knife.
## [06:14 ET] REJECTED — CCL — -32.6% off high, below SMA20 and SMA50, earnings 09-28 is a coin flip at the low.
## [06:14 ET] REJECTED — LEVI — same downtrend, only $45M/day dollar volume, catalyst 10-07 too far for the risk.
## [06:14 ET] REJECTED — KMX — a clean rates-to-auto-affordability short into 09-29 earnings, and I am declining it on the CORRELATION CAP, not on merit. The book already holds TLT SELL, TLT SELL_SHORT, XLU SELL_SHORT and IYR SELL_SHORT — four positions whose outcome depends on the long end staying high. KMX short would be a fifth bet on the same rate path wearing a consumer label. config/strategy.md caps same-driver ideas at 3; I am already over it.
## [06:14 ET] REJECTED — XRT / XLY short — same reason as KMX. The weakest chart of the day (XRT -11.82% off high, below both MAs) and I am still not shorting it, because it is the same rate-squeeze driver as four open positions. Recorded so synthesis does not re-litigate it.
## [06:14 ET] REJECTED — VLO — above SMA20 382.69 and SMA50 346.57, -7.6% off high, genuinely the strongest energy chart I priced. Declined because XLE and DINO are open longs and OXY is awaiting entry: a third refiner would be a fourth energy position on one crack-spread driver.

## [06:16 ET] CALENDAR — fetched, not recalled
FOMC 2026 remaining: **Oct 27-28** (decision 10-28 14:00 ET), **Dec 8-9** (with SEP).
No November meeting. September's meeting was Sep 15-16 and has already happened.
source: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm

CPI releases, all 08:30 ET:
- **September 2026 reference month -> released Tue 2026-10-14**
- October reference -> 2026-11-10; November reference -> 2026-12-10
source: https://www.bls.gov/schedule/news_release/cpi.htm

## [06:17 ET] BOOK HYGIENE — three stale "awaiting entry" rows that should be cancelled
These are in prior_context as still awaiting entry. They are not live ideas and
leaving them in the book is a real hazard, not just untidiness:

1. **`KXFEDDECISION-26SEP-H25` YES @ 32** (published 08-22) and
   **`KXFEDDECISION-26SEP-H0` YES @ 47** (published 09-03).
   The September FOMC was **Sep 15-16** per the fetched Fed calendar — both of
   these resolved over a week ago. They cannot fill. **Cancel.**
2. **`BTC` SELL @ 63,400** (published 08-16) and **`/MBTU6` SHORT @ 64,340**
   (published 08-18). BTC is **84,079** right now — 32.6% and 30.7% ABOVE those
   levels. Worse, `/MBTU6` is the **September** contract, which is at or past
   expiry. A resting short 30% below a trending market is an order that only ever
   fills in a crash, i.e. it fills at the worst possible moment and then keeps
   losing. **Cancel both.** The bearish BTC thesis they encoded has been wrong for
   six weeks and the tape has refuted it.
   source (BTC price): https://www.coingecko.com/
3. `KXFEDDECISION-26OCT-H25` YES @ 28 (published 09-02) is still live in principle
   — the October meeting is 10-27/28 — but I could NOT fetch a price for it this
   morning (see the Kalshi gap above), so I am not re-pitching it at a remembered
   price.

## [06:18 ET] LEVELS — GDX, the one genuinely new long I want today
Driver is distinct from the four rate-shorts and the three energy longs already
in the book. Gold miner operating leverage, measured not assumed:
- **GDX has beaten GLD by +15.32% over 3 months and +14.52% over 6 months**
  (GDX 3m +20.61% vs GLD 3m +5.29%). source: `market_data.py relstrength GDX --peer GLD`
- Structure: close 92.87, ATR14 3.1661 (3.41%), SMA20 96.2865, **SMA50 90.0118**.
  GDX is ABOVE its 50-day; GLD at 393.41 is BELOW both its SMA20 (399.34) and
  SMA50 (395.43). The miners are holding while the metal is not.
- Support shelf from fetched bars: **09-24 low 90.85**, **09-16 low 91.19**, with
  SMA50 90.01 underneath — a real three-point cluster at 90.0-91.2.
- Resistance: **08-28 high 104.78**, below the 150-day range high 105.67.
- GDX is -20.74% off its own range high, so this is buying a correction in an
  uptrend, not a breakout chase.
- HONEST LIMITATION: `history` returns only the last 20 bars, so I have no fetched
  swing low between 90.85 and the 250-day low of 68.13. The stop is therefore set
  by ATR beneath the shelf rather than on a swing low I can point at, and I am
  saying so rather than inventing a level.

## [06:19 ET] DATA QUALITY — no fetched OHLCV for bitcoin, and a trap worth recording
`history bitcoin`, `history BTC-USD`, `history BTCUSD` all FAIL (nasdaq has no
rows, yahoo 429). `history BTC` "succeeds" but returns a nasdaq-listed ticker at
**37.16 with $7,957 average daily dollar volume** — that is not bitcoin, it is a
micro-listed symbol that happens to share the string. **Discarded; do not use.**
A number that arrives with `ok: true` can still be the wrong instrument.
So all BTC levels below are derived from **IBIT** (iShares Bitcoin Trust) OHLCV,
and I state the derivation rather than passing it off as a spot level.
- IBIT close 47.57, ATR14 1.4208 (2.99%), SMA20 45.257, SMA50 40.9116,
  range 32.84-49.22, **-3.35% off its high**. source: nasdaq via market_data.py
- BTC spot 84,079 (-0.42% 24h), $30.5B volume. source: https://www.coingecko.com/
- Implied ratio 84,079 / 47.57 = **1,767 BTC per IBIT unit**, so IBIT SMA20 45.257
  maps to BTC ~**79,990** and SMA50 40.9116 to BTC ~**72,290**. Derived, not fetched.
READ: BTC is in an uptrend and 3.35% off its high. I have no edge going long at
84k with no dated catalyst, and I will not short an uptrend. The actionable item
is cancelling the stale shorts, not opening anything.

## [06:20 ET] POSITION UPDATES — the rest of the open book, all prices 2026-09-25 close
source for all levels: https://www.nasdaq.com/market-activity/ via `market_data.py history`

WORKING — hold as-is, no change, no re-pitch:
- **PFE** BUY @27.60, last **28.67** (+3.9%). Only -1.85% off its range high,
  ABOVE SMA20 28.06 and SMA50 26.98. The best-structured long in the book.
  ATR 0.4579. Hold. (Recommended 3x in 10 days already — deliberately NOT
  re-pitching; nothing changed and the anchoring guard applies.)
- **EEM** BUY @65.60, last **67.98** (+3.6%). Above SMA20 67.43 and SMA50 66.12,
  -5.02% off high. Stop 63.0 is 4.53 below = 4.1 ATR. Hold.
- **SNX** BUY @260.00, last **263.03** (+1.2%). Sitting on SMA20 263.30, above
  SMA50 256.88. Target 296.47, stop 242.5 (1.63 ATR of 12.61 — thin but it is an
  existing position and I am not walking it in). Hold.
- **BCC** BUY @76.50, last **77.14**. Reclaimed SMA20 76.59, still under SMA50
  79.16. -13.84% off high. Turning up. Hold, no stop change.
- **XLU** SELL_SHORT @39.60, last **39.51** (+0.6%). Working, but note the risk:
  price is only **0.96% above its range low of 39.125** and the 36.8 target sits
  BELOW that low. Hold with the 40.95 stop; do not add here — the easy part of
  this short is behind it.
- **TLT** SELL @81.87, last **79.32** (+3.0%). Thesis confirmed by the fetched
  10y at 5.18% (prev 5.11%). Target 78.0 intact. Hold.
- **CCJ** BUY @94.00, last **88.07** (-6.3%). -32.88% off high, below SMA20 95.19
  and SMA50 94.77. The 82.50 stop sits just under the 83.15 range low — that is
  correct placement and it is 1.75 ATR (3.1828) from the money. **Hold, no change.**
  I am explicitly not widening it and not cutting it: the stop is where the
  thesis breaks and it has room to work.
- **SVRA** BUY @5.35, last **5.00** (-6.5%). Micro cap, ATR 4.73%. Stop 4.60 is
  below the 4.695 range low — correct. 1.69 ATR away. Lottery-ticket size. Hold.
- **CEG** BUY @272.00, last **263.27** (-3.2%). Below SMA20 274.27/SMA50 271.94,
  -21.13% off high. Stop 250 is 1.48 ATR (8.9782) from the money — thinner than I
  would open with, but it sits above the 228.63 range low and this is an existing
  position. Hold.
- **DINO** BUY @107.50, last **106.82**. Above SMA50 97.48, at SMA20 107.77. Hold.
- **XLE** BUY @63.90, last **62.04** (-2.9%). Above SMA50 61.76, below SMA20 63.99.
  Stop 60.80 = 0.92 ATR (1.3539) from the money — uncomfortably tight but
  existing. Hold, do not widen.
- **GLD** BUY @398.00, last **393.41** (-1.2%). Below SMA20 399.34 and SMA50 395.43.
  Stop 381 = 1.85 ATR (6.7128), which clears the 1.8 ATR ETF floor. Hold.
  **RECONCILIATION:** prior_context also lists a `GLD` SELL @406.77 awaiting entry.
  That is not a second position and must not be read as one — treat 406.77 as a
  TRIM level on the open long, not a short. The open long's 437 target stands.

CUT — see the separate candidates for NKE and CAG. And one more:
- **LULU** — two rows: BUY @115.00 (-11.9%, **no stop**) and SELL @100.61 from
  09-08. Last **101.30**, -46.24% off high, below SMA20 105.13 AND SMA50 113.73,
  range low 95.35 just beneath. The 09-08 exit call was right and nothing has
  changed to reverse it. **Reaffirm the exit; the 115.00 long should be closed.**
  Not captured as a new candidate because 09-08 already published the exit — this
  is a restatement, and re-capturing it would open a fresh row for a decision
  already on the record.

## [06:24 ET] REJECTED — STZ as a long_term accumulation — no defensible valuation anchor
I rejected STZ as a swing above and came back to test it as a long_term idea,
which is a different claim (no stop needed, but a defended valuation and a
bear-case price are mandatory). It fails on exactly that requirement.
Fetched: market cap $19.41B, 170.78M shares, sector Beverages (finnhub profile).
Close 113.63, range low 113.335 — sitting ON the low. -32.6% off the 168.60 high.
- Three straight beats: +6.1%, +9.5%, +15.0%. Sell-side bullish 62.1%, improving +1.4pp.
- **Zero open-market insider buys in six months, two sells totalling $939,089.**
- **Relative strength is the worst I priced today: -25.58% vs its own sector XLP
  over six months, -10.61% over one month.** Underperforming staples in a period
  when staples themselves fell.
- WHY REJECTED: trailing EPS from the fetched surprise record gives only three
  usable quarters (3.43, 1.90, 3.06 = 8.39); the fourth row returned is a
  corrupt 2000-12-31 entry, so I cannot compute trailing EPS without inventing
  the missing quarter. config/strategy.md: "A long-term idea whose downside you
  cannot put a price on is not researched enough to publish." I will not
  manufacture the bear-case price to make the 2.5 floor computable.
  source: https://finnhub.io/ , `market_data.py profile|analysts|insiders|relstrength STZ`

## [06:25 ET] LONG_TERM LANE — deliberate check, and the honest outcome
I gave this lane its own pass rather than the leftovers. Every structural theme I
have fetched evidence for today is ALREADY represented by an open position:
- nuclear / datacenter power -> CCJ and CEG open, VST awaiting. Adding URA
  (-30.63% off high) would be a fourth bet on one driver.
- gold / real rates -> GLD open, GDX captured today. A third (SLV, -31.82% off
  high, 3m +9.12% vs GLD +5.29%) would be the same driver a third time.
- energy -> XLE and DINO open, OXY awaiting. VLO rejected above for this reason.
- healthcare -> PFE open and working (+3.9%).
The one genuinely new long_term candidate, STZ, fails for the reason above.
**So today's report carries no new long_term idea, and that is the honest
outcome rather than an omission.** Note it in data_quality_notes.

## [06:27 ET] REJECTED — IDT — best small-cap chart I found, rejected on its reaction record
$1.68B cap, Telecommunication. Close 67.46, sitting on SMA50 67.2616, below SMA20
68.981, only -6.47% off its 72.125 high — genuinely healthy, unlike the whole
consumer complex. $15.2M/day dollar volume, clears the floor easily.
**Relative strength strong: 6m +40.51% vs SPY +19.57% (+20.94pp), 3m +11.84pp.**
Earnings 2026-09-28 amc, eps est 0.9898.
WHY REJECTED:
- Earnings reaction record is a coin flip: +4.6%, **-7.6%**, +0.1%, **-17.3%** —
  two misses in four quarters. An earnings-catalyst trade needs better than that.
- **11 insider sells, 0 buys, $2,382,405 net selling**, plus three Form 144s
  (notices of proposed sale) filed in July. One-sided and persistent.
- Only 5 analysts cover it (1 strong buy / 3 buy / 1 hold), flat.
- The fresh 8-K (filed 09-24, event 09-22) is a routine **$0.07 quarterly dividend**,
  payable 10-14, record 10-05 — I read it; it is not a catalyst.
  source: https://www.sec.gov/Archives/edgar/data/1005731/000143774926031079/idt20260923_8k.htm
Good relative strength is one confirmation, and it is fading (1m -3.06% vs SPY).

## [06:27 ET] REJECTED — ACN — the de-rating is real and still going
176.11, -19.44% off the 218.595 high, on SMA50 175.3292 and below SMA20 185.4055
after seven straight down sessions (190.29 on 09-17 to 176.11). Earnings 10-01 bmo.
Bullish share 59.4%, **down 10.3pp, deteriorating**. 0 insider buys, 10 sells
$2,585,929. Relative strength contradicts itself: 3m +28.17pp vs XLK but
**6m -58.47pp vs XLK** and 1m -10.26pp. The AI-disruption de-rating on IT services
is the 6m number and it is still operating. Consistent but tiny beats (+1.4%,
+2.1%, +4.3%, +1.2%) will not re-rate it. Falling into a print with deteriorating
revisions and insider selling only.

## [06:28 ET] REJECTED — BYRN — $80M cap, -74.69% off high, $1.2M/day. Broken chart, ATR 5.43%, no thesis beyond cheapness.
## [06:28 ET] REJECTED — MTN — $4.85B, -15.19% off high, below SMA20 137.25 and SMA50 144.28. Consumer discretionary into a 09-28 print, which is the exact complex today's macro work says to avoid.

## [06:29 ET] REJECTED — BITCOIN, all expressions — fails the reward-to-risk floor. Arithmetic shown.
This matters because it is a WEEKEND run, where config/strategy.md says crypto
should carry more of the report. It cannot today, and here is exactly why.
**There is no fetched OHLCV for any coin** (see the data-quality note above), so
for BTC/ETH/SOL I have no ATR and therefore cannot set a stop that clears the
2.5 ATR crypto floor. That alone disqualifies a spot or futures crypto idea.
Using IBIT as the only instrument with real fetched bars, both expressions fail:
- **IBIT itself (etf, 1.8 ATR floor, ATR14 1.4208):** entry at SMA20 45.257,
  stop 42.70 (2.56 below = 1.80 ATR, the minimum), target at the 49.22 range high
  -> reward 3.96 / risk 2.56 = **R:R 1.55. FAILS the 2.0 swing floor.**
  Clearing 2.0 would need a 50.38 target, i.e. above the range high — undefendable.
- **BTC via /MBT (futures, 2.5 ATR floor):** derived ATR 2.99% of 84,079 = 2,514.
  Entry at the derived 20-day 79,990, stop 71,500 (below the derived 50-day
  72,290) = risk 8,490 = 3.38 ATR. Target at the derived range high 86,996 ->
  reward 7,006. **R:R 0.83. FAILS badly.** Clearing 2.0 needs ~96,970, 15% above
  the high.
**I am not widening the target or tightening the stop to make either pass** —
that is the precise failure mode this repo demotes ideas for. No BTC trade today.
The uptrend is real (IBIT -3.35% off its high, above SMA20 45.257 and far above
SMA50 40.9116); it is simply not buyable at a defensible ratio from here.
ALSO: no event contract today either, because Kalshi returned no priceable macro
market (gap logged at 06:06). So this weekend run carries NO crypto, NO futures
and NO event contract, and every one of those absences is a fetch failure or a
failed floor rather than a lane I skipped. Say so in data_quality_notes.

## [06:30 ET] ARITHMETIC CHECK — every captured idea, recomputed by hand
| Symbol | Entry | Stop | Target | Risk | Reward | R:R | Floor | Stop/ATR | ATR floor | win_p | baseline 1/(1+RR) | edge |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NKE | 37.10 | 34.60 | 42.30 | 2.50 | 5.20 | **2.08** | 2.0 OK | 2.50/0.9099 = **2.75** | 2.0 OK | 0.40 | 0.325 | +7.5pt |
| GDX | 91.20 | 85.40 | 104.40 | 5.80 | 13.20 | **2.28** | 2.0 OK | 5.80/3.1661 = **1.83** | 1.8 OK | 0.38 | 0.305 | +7.5pt |
| MU | 994.00 | 880.00 | 1255.00 | 114.00 | 261.00 | **2.29** | 2.0 OK | 114/44.5711 = **2.56** | 2.0 OK | 0.42 | 0.304 | +11.6pt |
CAG, LCII are exits (no stop/target/ratio by construction). No ratio sits in the
2.0-2.35 "nudged until it passed" band by accident — each target is a named level
(42.30 insider buy zone, 104.78 August high, 1255.00 range high) set AFTER the
stop, and no stop is inside its ATR floor. Claimed edges are all under 12 points.

## [06:32 ET] STRUCTURAL SCREEN — how I hunted, and what it revealed about the floor
I screened 20 names across healthcare, industrials, financials, materials, energy
services, semis and media for one structure: **well off the high (so a target has
overhead room) AND above the 50-day (so it is not a downtrend).** Results:
- Above SMA50 but <8% off high, so no target room: MRK -5.19, GILD -2.12,
  AMGN -7.25, VRTX -6.08, DE -4.26, AMD -1.31, DIS -5.11, ETN -7.95
- Off the high but BELOW SMA50, i.e. downtrends: BMY -8.42, CAT -23.46, JPM -6.40,
  GS -18.94, PGR -14.15, NUE -11.73, SLB -14.75, HAL -24.85, UBER -15.47, CMCSA -32.38
- Passed both: **TXN** (-16.75, above SMA50 271.01) and **MCHP** (-25.70, above SMA50 76.13)
source: `market_data.py history` across all 20, 150-day windows

**A genuine tension in the strategy, worth flagging to the red team.** In a tape
this narrow, the 2.0 reward-to-risk floor mechanically herds you into laggards:
clearing 2:1 needs a target far above entry, which needs overhead room, and today
everything with overhead room is in a downtrend while everything in an uptrend is
within 8% of its high. I tested this rather than asserting it — ETN, the best of
the near-high names: ATR 14.91, a 2.0 ATR stop is 29.8 wide, and the range high
478.0 is only 48 above a 430 entry, giving **R:R 1.6. Fails.** Same for IBIT and
XLK. That is not a reason to lower the floor; it is a reason the report is
light on new longs today, and it belongs in data_quality_notes.

## [06:34 ET] REJECTED — MCHP — the best new setup I found, and it still fails the floor. Arithmetic shown.
Microchip Technology, $42.73B cap, 543.01M shares, Semiconductors (finnhub profile).
This one hurt to drop, so the numbers are here in full.
THE CASE FOR IT was real:
- **Four consecutive beats with EPS ramping 117%**: 0.35 (Q 2025-09-30) -> 0.44 ->
  0.57 -> **0.76** (Q 2026-06-30); surprises +2.6%, +4.7%, +10.6%, +7.4%. A clean
  analog/MCU cycle recovery in the actual reported numbers.
- **Broke above its 50-day on 2026-09-25**: opened 75.20, high 78.96, low 74.93,
  closed **78.69 (+5.35%)** on 9.75M shares, above SMA50 76.1326 and SMA20 73.308.
- Rising lows off the 09-16 trough: 68.75, 70.10, 71.06, 72.74, 74.44, 73.13, 74.93.
- -25.70% off the 90.85 range high, so genuine overhead room. $660M/day dollar volume.
- 78.8% bullish sell side, **zero sell ratings** (9 strong buy / 17 buy / 7 hold).
WHY REJECTED — two independent disqualifications:
1. **No dated catalyst.** MCHP does not appear in the earnings calendar even at
   `--days 50` (1,500 rows fetched). I will not write a reporting date I cannot
   verify, and config/strategy.md is explicit that a breakout is a trigger, not a
   catalyst. So it cannot be a swing idea.
2. **As a long_term idea it fails the 2.5 floor against an honest bear case.**
   Trailing EPS from the four fetched actuals = **2.12**; latest quarter annualized
   = **3.04**, so 78.69 is 37.1x trailing and 25.9x run-rate. Target 90.85 is
   where two methods converge — the fetched range high, and 30x the 3.04 run-rate
   = 91.20. Bear case, if the recovery stalls and EPS reverts to the 0.44-0.57 the
   company actually printed 2-3 quarters ago (~2.00 annualized) at 31x = **62.00**.
   Accumulating at 76.50 (the reclaimed 50-day): reward 14.35, risk 14.50,
   **R:R 0.99. FAILS 2.5.**
   **AND HERE IS THE SHORTCUT I AM DECLINING.** I could swap the bear case for the
   fetched range low of 68.75 and the entry to 74.50, which gives reward 16.35 /
   risk 5.75 = **R:R 2.84 — it passes.** That is not a bear case. It is a nine-day-old
   technical low dressed up as a valuation floor, on a cyclical semiconductor, for
   a multi-year thesis. Making the downside shallow is the same gaming as walking
   the stop in, and it would have put a 0.99 idea on the page at 2.84.
3. Also against it: **zero insider buys and 14 sells totalling $52,051,695** over
   six months, and -25.56% vs XLK over 6 months / -18.88% over 3 months.
source: https://www.nasdaq.com/market-activity/stocks/mchp/historical , https://finnhub.io/

## [06:35 ET] REJECTED — TXN — passed the same structural screen (-16.75% off high, above SMA50 271.01 and SMA20 263.195) and rejected for the same two reasons: no verifiable earnings date in the 50-day calendar, and it is the same analog-semiconductor driver as MCHP, so it could not be a second idea even if it qualified.
## [06:35 ET] REJECTED — ETN — arithmetic in the block above. R:R 1.6.

## [06:36 ET] COHERENCE CHECK against my own recommendations
Flagging this so the red team does not have to find it. **I am recommending a NKE
long while cutting CAG and LCII and reaffirming the LULU exit — all consumer.**
That looks contradictory and here is the distinction I am relying on:
- The three exits are unconditional, and two of them (LCII, LULU) have **no stop**,
  so nothing closes them but a decision. They are making new lows with no
  confirmation — zero insider buying at LCII, a missed quarter, price under both
  averages.
- The NKE long is **conditional and above the market**: `wait: true`, and it only
  fills on a post-print reclaim of 37.10 holding above 35.22. In the falling-knife
  scenario — the one my own macro work says is more likely for this complex — it
  never fills at all. It also has the one confirmation the others lack: a $2.16M
  net insider buy cluster including the CEO and Tim Cook.
If the consumer keeps rolling over, this report exits three consumer positions and
never enters the fourth. That is the intended behaviour, not an accident.

## [06:38 ET] REJECTED — CMCSA short — no catalyst, and the target would be invented
$77.8B cap. Close 21.91 after -16.8% in 13 sessions (26.33 on 09-08 to 21.91), on
heavy volume (41.8M on the last bar). Below SMA20 24.592 and SMA50 24.8599,
-32.38% off the 27.35 high. Structurally the cleanest downtrend I found and the
book is long-heavy (13 longs vs 3 open shorts), so a non-rate short would have
been genuine diversification. Rejected because:
- **No dated catalyst** — CMCSA does not appear in the earnings calendar at
  `--days 50`, same as MCHP and TXN. I will not invent a reporting date.
- **The target cannot be anchored.** Price is only 3.0% above the 21.28 range low
  and I have no fetched structure below it. A 2.0 ATR stop (ATR 0.8074) is 1.61
  wide, so clearing 2:1 from a 22.00 entry needs an **18.78** target — 12% below
  the market with no level underneath it that I fetched. That number would be
  reverse-engineered from the floor, which is the thing the floor exists to stop.
- Shorting 3% above the low after a 17% slide is chasing.

## [06:39 ET] ENTRY-STYLE CHECK — deliberately addressing the 31:1 pullback skew
config/strategy.md records that the first month ran 31 pullback entries against 1
breakout, that only 42% ever filled, and that the ones which filled were the ones
already falling. Today's five:
- **NKE 37.10 vs 35.75 market -> entry ABOVE the market, a reclaim/breakout entry.**
  It cannot fill while the name is falling. This is the style the report has been short of.
- GDX 91.20 vs 92.87 -> pullback, -1.8%, onto a three-point shelf (90.85 low,
  91.19 low, SMA50 90.01). A level I can point at, not a reflex discount.
- MU 994.00 vs 1082.28 -> pullback, -8.2%, onto the SMA20, and marked `wait: true`
  precisely because it should NOT be chased at 1082.
- CAG, LCII -> market exits, no entry style.
So: 1 breakout, 2 level-anchored pullbacks (one of which is an explicit "do not
chase"), 2 exits. No reflex discounts.

## [06:40 ET] RESEARCH COMPLETE
- **candidates: 5 distinct symbols** (9 lines in candidates.jsonl; CAG, MU and LCII
  each appear twice because I re-captured them after auditing conviction against
  the evidence-kind count — synthesis takes the last entry per symbol).
  - **GDX** buy, swing, conv 4, R:R 2.28 — the only genuinely NEW idea
  - **NKE** buy, swing, conv 4, R:R 2.08, `wait: true` — conditional post-print
    entry, and the reconciliation of two conflicting open rows
  - **MU** buy, swing, conv 4, R:R 2.29, `wait: true` — re-levelled from a stale
    960 bid to the 994-942 band; do not chase at 1082
  - **CAG** sell, conv 4 — close the long before the 09-29 print
  - **LCII** sell, conv 4 — close the long; it has no stop and nothing else will
- All three ideas with stops clear both floors on recomputed arithmetic (see the
  06:30 table). Claimed edge over the random-walk baseline is +7.5 to +11.6 points.
- **Why only five, stated plainly rather than apologised for:** it is a Saturday
  with equities and futures closed, so nothing is entered before Monday; and the
  three lanes that normally carry a weekend run all failed for documented reasons
  — no priceable Kalshi macro market, no crypto OHLCV anywhere (so no ATR, so no
  compliant stop), and bitcoin failing the R:R floor at 1.55 via IBIT and 0.83 via
  /MBT. Three further real setups (MCHP, TXN, CMCSA) died on having no verifiable
  earnings date. I turned down a 2.84 R:R on MCHP that only existed by calling a
  nine-day-old low a bear case.
- **coverage gaps:**
  - Index levels for today are UNKNOWN — spx, ndx, dow, rut, vix, ES/NQ, DXY,
    us10y_yield, gold and wti ALL failed (finnhub needs an index subscription,
    yahoo 429, stooq 404, no alphavantage key). ETF proxies were the workaround.
  - No options-implied move on anything (`implied` returns yahoo-options 401), so
    no idea today was checked against what the straddle prices. This is the check
    config/strategy.md asks for at level-setting and I could not run it once.
  - No short interest / days to cover (`short` read-timed-out on nasdaq).
  - Kalshi: no priceable macro market for Fed, CPI, recession, inflation or
    shutdown. Three event-contract rows in the book could not be re-priced.
  - No crypto OHLCV: `history` fails for bitcoin / BTC-USD / BTCUSD. **`history BTC`
    returns a DIFFERENT instrument** (37.16, $7,957 daily dollar volume) with
    `ok: true` — a trap, discarded.
  - MCHP, TXN and CMCSA are absent from the earnings calendar even at `--days 50`.
  - Not reached: no long_term idea anywhere (every structural theme I can evidence
    is already an open position; the one new one, STZ, lacks a computable trailing
    EPS). No small cap captured — IDT was the best and its reaction record is a
    coin flip. Nothing in financials, industrials or media.
- **sources that failed:** yahoo (429 on all indices, 401 on options),
  finnhub (index quotes — subscription), stooq (404 on index symbols),
  alphavantage (no api key), nasdaq `short` endpoint (read timeout),
  Kalshi macro search (0 results), coingecko history (not wired to `history`),
  robinhood.com futures support article (404 — availability verified by web
  search instead: RH carries MES, ES, MNQ, NQ, MGC, MCL, MBT, MET plus new
  micro BTC/SOL/XRP).
- **what worked:** FRED (all rate series), coingecko spot, finnhub (equity/ETF
  quotes, earnings calendar, insiders, analysts, profile), nasdaq OHLCV,
  SEC EDGAR filings, BLS and Federal Reserve calendars.

## [06:33 ET] TIMESTAMP CORRECTION #2 — and the RESEARCH COMPLETE block above is SUPERSEDED
Real wall clock is **06:33 ET**, not the 06:38-06:40 I stamped. My minute labels
drifted ahead again. The RESEARCH COMPLETE block above was written at ~06:29 real
time with budget still remaining; **it is superseded by the amended block at the
bottom of this file.** I kept researching rather than stopping early.

## [06:34 ET] EVENT CONTRACTS — root-caused. Two separate findings, one a real bug.
Event contracts are "wanted, not tolerated" per config/universe.md and I had zero,
so I went back at it properly instead of accepting the gap.

**FINDING 1 — `market_data.py events` search is broken, and this is a code bug.**
`scripts/market_data.py:752-766` requests `/trade-api/v2/markets` with only
`status=open` and `limit=min(limit*5, 200)`, then filters the **search string
client-side over whatever 200 rows came back**. Kalshi has thousands of open
markets and the first 200 are NFL/tennis parlays, so a search for "Fed" or "CPI"
can never match no matter what is listed. That is why every macro query returned
count=0 while an empty query returned 40 sports markets.
The fix is server-side filtering: the endpoint accepts **`series_ticker`**. Macro
series confirmed to exist by direct query this morning:
- **`KXFEDDECISION`** — per-meeting, by size: `-H0` (maintain), `-C25` (cut 25bps),
  `-C26` (cut >25), `-H25`, `-H26`
- **`KXFED`** — fed funds upper bound above a threshold (T4.50 ... T6.00)
- **`KXCPI`** — monthly CPI above a threshold (T0.3 ... T1.0)
- **`KXCPIYOY`** — CPI year-over-year above a threshold (T3.9 ... T5.0)
I am NOT patching market_data.py from the research phase — CLAUDE.md requires a
test in `tests/` for logic changes, and that is a separate change from a morning's
research. Recording it so it can be fixed properly.

**FINDING 2 — the blocker is real regardless, so this gap would survive the fix.**
I queried four near-dated markets individually via `/markets/{ticker}`:
`KXFEDDECISION-26OCT-C25`, `KXFEDDECISION-26OCT-H0`, `KXCPI-26SEP-T0.4`,
`KXCPIYOY-26SEP-T4.9`. All four return `status: active` — and **`yes_bid`,
`yes_ask`, `no_bid`, `no_ask`, `last_price`, `volume`, `volume_24h`,
`open_interest` and `liquidity` are ALL null** on the unauthenticated endpoint.
So no event contract can be priced today without API credentials. config/universe.md
requires stating the market's implied probability against my own; with no price
there is no implied probability, and an event contract recommendation without one
would be exactly the "feels underpriced" thesis that file forbids.
**Conclusion: no event contract today, for a documented reason, not an oversight.**

**Bonus — the close times independently corroborate my calendar work.**
`KXFEDDECISION-26OCT-*` closes **2026-10-28T17:59Z** and `KXCPI-26SEP-*` closes
**2026-10-14T12:25Z**. Those match the Fed calendar (Oct 27-28 meeting) and the
BLS schedule (September CPI on Oct 14) that I fetched separately at 06:16 — two
independent sources agreeing on both dates my GDX catalyst rests on.
Also of note: Kalshi's September monthly-CPI ladder centres on **T0.4** and the
year-over-year ladder spans 3.9-5.0%, which brackets the +0.40% MoM and ~4.9%
annualized I computed from CPIAUCSL. The market's own threshold structure agrees
with where I put the inflation read, even though I cannot see its prices.
source: https://api.elections.kalshi.com/trade-api/v2/markets

## [06:36 ET] SECOND CATALYST SWEEP — the remaining dated names, all rejected
Screened every name left in the 12-day earnings calendar that I had not yet
priced, on the same structure test (off the high AND above the 50-day):
| Sym | Close | % off high | SMA20 | SMA50 | above50 | ATR% | earnings |
| --- | --- | --- | --- | --- | --- | --- | --- |
| JBL | 316.74 | -26.16 | 305.13 | 317.60 | no | 3.63 | 09-30 bmo |
| CNXC | 27.08 | -23.24 | 29.41 | 26.81 | **yes** | 7.75 | 09-29 amc |
| AYI | 319.42 | -15.64 | 316.41 | 332.61 | no | 2.91 | 10-01 bmo |
| RPM | 100.44 | -15.18 | 101.21 | 106.50 | no | 2.37 | 10-06 |
| LW | 43.58 | -21.76 | 48.51 | 50.79 | no | 3.25 | 10-06 |
| JEF | 47.68 | -25.48 | 50.76 | 53.21 | no | 3.87 | 09-30 |
| MKC | 47.94 | -32.79 | 51.00 | 52.21 | no | 2.43 | 10-05 |
Six of seven are below their 50-day — downtrends into a print, which is the CAG
setup I am exiting today, not one I want to open. Only CNXC passed the structure
test, so I took it the whole way.

## [06:37 ET] REJECTED — CNXC — looked like the deep-value find of the day; it is not
Concentrix Corp, Professional Services (BPO / customer experience), earnings
**2026-09-29 amc**, eps est 2.7591 on rev est $2.53B.
WHAT DREW ME: apparent 2.5x earnings. Trailing EPS from four fetched actuals
(2.63 + 2.61 + 2.95 + 2.78) = **10.97** against a 27.08 price. Above SMA50 26.814,
-23.24% off its high, and the AI-disrupts-call-centres de-rating is a genuine
distinct driver — a lane this book has zero exposure to.
WHY REJECTED — four independent problems, any one of which is enough:
1. **All four of the last four quarters MISSED**: -2.2%, -3.3%, -0.6%, -5.0%. An
   earnings-catalyst trade on a company that has not beaten once in a year is a
   bet against its own record.
2. **The "2.5x earnings" is unverifiable and almost certainly not what it looks
   like.** Market cap is only **$1.65B on 61.02M shares**, while 10.97 EPS implies
   roughly $670M of annual earnings. A company does not trade at 2.5x unless the
   equity is a thin stub over a large debt load — which is consistent with how
   this business was assembled — and I have **no fetched debt or EBITDA figure**,
   so I cannot compute the EV multiple that would actually matter. Publishing
   "trades at 2.5x earnings" would be a true number that tells a false story.
3. **A single insider sale of $133,500,000** — about 8% of the entire market cap —
   against 3 open-market buys totalling **$118,089** (1,000 and 2,500 share lots).
   The buys are real but trivial next to the exit.
4. **-50.44% vs XLK over six months**, -10.15% over one month, and a 7.75% ATR.
   It closed 2026-09-25 at 27.08, down 7.9% on the day, near the 26.70 low — one
   tick above the 50-day, not comfortably above it.
Also: under $2B market cap at $43M/day, so it would have been lottery-ticket sized
at best. source: https://finnhub.io/ , https://www.nasdaq.com/market-activity/stocks/cnxc/historical
## [06:37 ET] REJECTED — JBL, AYI, RPM, LW, JEF, MKC — all below their 50-day into a print. Table above.

## [06:38 ET] RESEARCH COMPLETE — AMENDED, supersedes the earlier block
This is the authoritative version. The earlier RESEARCH COMPLETE was written at
~06:29 real time with budget left; I kept working and added the event-contract
root-cause and a second catalyst sweep after it. Research was NOT truncated —
it ran to a deliberate stop with the deadline still ahead.

- **candidates: 5 distinct symbols**, 9 lines in `candidates.jsonl` (CAG, MU and
  LCII appear twice — I re-captured them after auditing claimed conviction against
  the distinct-evidence-kind count; synthesis takes the last entry per symbol).
  Every one now has conviction == the score its evidence kinds support.
  - **GDX** buy / swing / conv 4 / R:R 2.28 — the only genuinely NEW position
  - **NKE** buy / swing / conv 4 / R:R 2.08 / `wait: true` — conditional post-print
    entry above the market, and the reconciliation of two conflicting open rows
  - **MU** buy / swing / conv 4 / R:R 2.29 / `wait: true` — re-levelled off a dead
    960 bid to the 994-942 band; explicitly do not chase at 1082
  - **CAG** sell / conv 4 — exit the long on Monday, before the 09-29 print
  - **LCII** sell / conv 4 — exit the long; it has no stop, so nothing else closes it
- Entry styles: 1 above-market reclaim, 2 level-anchored pullbacks, 2 market exits.
  No reflex discounts — deliberate, given the 31:1 pullback skew on record.
- Arithmetic recomputed by hand for all three stopped ideas (table at 06:30). All
  clear both the R:R floor and the ATR stop floor; claimed edge over the
  `1/(1+R:R)` baseline is +7.5 to +11.6 points.
- **Central macro read:** a very narrow tape. SPY -1.03% and XLK -1.24% off their
  highs and above both averages, while XLY (-9.52%), XRT (-11.82%) and XLP (-8.88%)
  are all below both. Discretionary and staples falling together is the consumer,
  not rotation. Against 10y 5.18% / fed funds 3.88% / CPI +0.40% MoM.
- **Why only five, and why it is not thinness of effort:** Saturday, equities and
  futures shut, nothing enters before Monday. The three lanes that normally carry
  a weekend run are all blocked by documented fetch failures — no priceable Kalshi
  market (every quote field null unauthenticated), no crypto OHLCV anywhere (so no
  ATR, so no compliant stop), and bitcoin failing the R:R floor at 1.55 via IBIT
  and 0.83 via /MBT. Six further real setups (MCHP, TXN, CMCSA, CNXC, IDT, ACN)
  were worked to a conclusion and rejected on their merits. I declined a 2.84 R:R
  on MCHP that existed only by passing a nine-day-old low off as a bear case.
- **coverage gaps:** index levels unknown for today (spx/ndx/dow/rut/vix/ES/NQ/DXY/
  us10y_yield/gold/wti all failed; ETF proxies substituted). No options-implied
  move on anything (`implied` -> 401), so the straddle cross-check config/strategy.md
  asks for was never run. No short interest (`short` -> nasdaq timeout). No event
  contract priceable. No crypto OHLCV. MCHP/TXN/CMCSA absent from the 50-day
  earnings calendar. **No long_term idea** — every structural theme I can evidence
  is already an open position, and the one new one (STZ) has no computable trailing
  EPS. **No small cap captured.** Nothing in financials, industrials or media.
- **sources that failed:** yahoo (429 all indices, 401 options), finnhub (index
  quotes — subscription), stooq (404 index symbols), alphavantage (no key), nasdaq
  `short` (timeout), Kalshi (macro search broken client-side AND all prices null),
  coingecko (not wired into `history`), robinhood.com futures article (404 —
  availability confirmed by web search: MES, ES, MNQ, NQ, MGC, MCL, MBT, MET plus
  new micro BTC/SOL/XRP).
- **code bug to fix separately:** `scripts/market_data.py:752-766` filters the
  `events` search client-side over an arbitrary 200-row slice, so macro markets are
  unreachable. Needs `series_ticker` (KXFEDDECISION / KXFED / KXCPI / KXCPIYOY).
  Not patched here — CLAUDE.md requires a test in `tests/` for logic changes.
