# Research log — 2026-10-27

## [06:03 ET] MACRO — rates, policy, data gaps
- FRED 10y Treasury **5.00%** (2026-10-23) — source: https://fred.stlouisfed.org/series/DGS10
- FRED 2y **4.69%** (2026-10-23); 10y-2y curve **+0.32** (2026-10-26) — steepening, long end leading
- Fed funds effective **3.88%** (2026-10-23) — so 10y sits 112bp ABOVE funds: bear steepener
- Unemployment 4.2% (Sep 2026); CPI index 336.298 (Sep 2026)
- TLT (20y bond ETF proxy) 81.68 pre, prev close 81.34, +0.42% — source: market_data quote
- **DATA GAP: Yahoo Finance returning HTTP 429 on all index/FX/commodity queries.**
  SPX, NDX, DJI, RUT, VIX, /ES, /NQ, DXY, 10y yield quote, gold, WTI all FAILED.
  CoinGecko crypto prices also FAILED this call. Will retry; levels must come
  from whatever source answers (stooq/finnhub) and anything unfetched stays null.

## [06:04 ET] CALENDAR — dated events inside the horizon
- **FCX reports TODAY 2026-10-27 BMO** (est EPS 0.80, rev $7.5B) — OPEN POSITION, -4.4%
- **PYPL reports TODAY 2026-10-27 BMO** (est EPS 1.34, rev $8.9B) — AWAITING ENTRY @56.5
- Today BMO also: BA, KO, UPS, SHW, SPGI, HCA, ECL, ITW, JCI, PCAR, RCL, GLW, CNC
- Today AMC: V, NXPI, WM, STX, PPG, FE, CZR, LPLA, ACGL
- Wed 2026-10-28 AMC: **MSFT**, NOW, F, FDX, KLAC, TMUS, EBAY, CMG, CVNA, FTNT, EQIX
- Wed 2026-10-28 BMO: ADP, APH, BSX, BIIB, AEP, AER, CHRW
- source: market_data.py earnings (finnhub earnings calendar)

## [06:08 ET] PRICE SESSION NOTE — what "last" means this morning
- Run time 06:0x ET, equity market CLOSED. finnhub's `price` at this hour equals
  the **2026-10-26 close**; `prev_close` is the 2026-10-23 close. Confirmed by
  cross-check: GLD finnhub price 367.82 == nasdaq history last_close 367.82 for
  2026-10-26. So the "change_pct" below is Monday's actual session move, not a
  thin pre-market print. Every level in this run is set off the Oct-26 close.

## [06:08 ET] BOOK MARK-TO-MARKET — Oct 26 close vs prior_context (Oct 23)
| Sym | Oct-26 close | Mon move | note |
| --- | --- | --- | --- |
| FCX | 65.16 | -0.03% | **EARNINGS TODAY BMO** |
| PYPL | 54.99 | **-3.56%** | **EARNINGS TODAY BMO**; awaiting-entry @56.50 now ABOVE mkt |
| DG | 128.42 | **-3.22%** | long @134.50, stop 125.30 — 2.4% of room left |
| SMMT | 14.50 | **-6.27%** | long @17.10, stop 14.40 — **0.7% from stop** |
| BCC | 75.44 | -2.96% | long_term, no stop |
| LULU | 102.91 | **+3.94%** | short @100.61 — moving against, stop 112 |
| NKE | 37.91 | +1.64% | short @38.40 |
| XLE | 69.64 | +0.45% | long @63.90, target 70.50 — **1.2% from target** |
| IYR | 98.83 | +0.44% | short @97.80, stop 100.40 — 1.6% of room |
| TLT | 81.68 | +0.42% | short @79.90, stop 82.00 — **0.4% from stop** |
| ITB | 89.87 | -0.77% | short @89.80 |
| XLF | 56.02 | +0.21% | long @54.23, target 57.60 |
| STLD | 237.55 | -1.65% | long @245.50, stop 228.75 |
| HII | 281.05 | **+2.54%** | long @262.00, +7.3% |
| UNP | 296.97 | +1.40% | long @288.60, target 315.99 |
| ABT | 104.88 | +1.14% | long @103.00 |
| CVS | 92.53 | -1.01% | long @93.00 |
| PFE | 29.79 | -0.80% | long_term @27.60 |
| KHC | 24.73 | -0.28% | long @23.00 |
- source: market_data.py quote (finnhub), cross-checked against nasdaq history

## [06:09 ET] AWAITING-ENTRY TRIAGE
- `GLD` SELL @406.77 (pub 2026-10-25) — **unreachable and was never a live level.**
  GLD traded 373.5/369.0 on 10-22 and closed 367.82 on 10-26; range_high over the
  last 30 sessions is 403.15. An entry 10.6% above the market cannot fill. Kill it.
  Gold is already 8.8% off its high and broke down 10-22 on 17.5M shares (2.7x
  average volume). The short was right about direction and wrong about price —
  chasing it now at 367 is selling into a completed 9% decline. Stand aside.
  source: market_data.py history GLD (nasdaq), atr14 5.31 (1.44%), sma20 378.59
- `VST` BUY @132.00 (pub 2026-08-24) — mkt 141.73, 7.4% above entry. Stale. Not re-pitching.
- `OXY` BUY @54.00 (pub 2026-09-24) — mkt 64.07, 18.6% above entry. Stale.
- `AAL` SELL_SHORT @13.35 (pub 2026-10-03) — mkt 12.20, 8.6% BELOW the short entry. Stale.
- `KXCPIYOY-26SEP-T3.5` NO @18 — Sep CPI event, resolution date passed/expired. Dead.

## [06:12 ET] CATALYST — FOMC decision TOMORROW, Wed 2026-10-28 14:00 ET
- October FOMC is a two-day meeting, Oct 27-28; decision 14:00 ET Wed, presser 14:30 ET.
  No SEP at this meeting (SEP only Mar/Jun/Sep/Dec).
  source: https://thriveinmarkets.com/calendar/dates/fomc-2026/
- Sources DISAGREE on the current target range (3.50-3.75% vs 3.75-4.00%). FRED's
  effective fed funds rate prints **3.88%** for 2026-10-23, which is inside
  3.75-4.00% and outside 3.50-3.75%, so the 3.75-4.00% range is the one consistent
  with the data I actually fetched. Treating the level as 3.75-4.00% but NOT
  publishing any idea that depends on the exact range.
  source: https://fred.stlouisfed.org/series/DFF
- **This dominates the book.** Four live positions are direct rate expressions:
  TLT short, IYR short, ITB short, XLF long. Nothing new gets added on the rate
  path in front of a 14:00 ET decision tomorrow — that is a coin flip, not an edge.

## [06:13 ET] PRIMARY DOCUMENT — DG 8-K filed 2026-10-26 (Item 8.01)
- The FTC **and several states sued Dollar General on 2026-10-26** in the US
  District Court for the Middle District of Tennessee. Alleged: FTC Act s5(a),
  Gramm-Leach-Bliley Act, and state consumer-protection and **weights and measures**
  laws, over "marketing, advertising and sale of products". Plaintiffs seek
  injunctive relief, monetary judgment and civil penalties.
- DG had been cooperating with the FTC probe since **early February 2026**; it got a
  draft complaint, draft settlement order and "a significant monetary demand" on
  2026-09-23. It disputes the demand and the damage methodology.
- The company's own language: "intends to vigorously defend", "no assurances can be
  given", and it "could have a material adverse effect on the Company's consolidated
  financial statements as a whole".
- source: https://www.sec.gov/Archives/edgar/data/29534/000110465926118869/tm2628315d1_8k.htm
- This is NEW information that did not exist when DG was published as a conviction-4
  buy yesterday, and it is the kind that does not resolve on a quarter's timescale.

## [06:16 ET] POSITION UPDATE — DG — opened 2026-08-21 @134.50, -4.5% at 128.42
- decision: **CLOSE at the 2026-10-27 open.** Reverses yesterday's conviction-4 buy.
- why: FTC + states suit filed 2026-10-26 (8-K Item 8.01, read) seeking civil
  penalties the company itself calls potentially materially adverse; and the
  pre-committed 125.30 stop traded through to 124.62 the same session.
- note: the 125.30 stop was only 0.64 ATR below the prior close. It was never a
  durable level — that is the tight-stop failure mode this report keeps repeating.
- action: captured via add_candidate.py, conviction 3, size 0.

## [06:17 ET] POSITION UPDATE — SMMT — opened 2026-10-09 @17.10, -15.2% at 14.50
- decision: **CLOSE at the 2026-10-27 open.** Stop 14.40 breached (10-26 low 14.37).
- why: -6.27% session with no company disclosure behind it. EDGAR shows nothing
  between the 2026-09-29 8-K and the 2026-10-19 DEF 14A. Below 20d (16.24) and
  50d (15.81), 50.4% off the 29.23 high.
- data gap: `market_data.py short SMMT` → nasdaq ReadTimeout. No short interest.
  No dated news found for 2026-10-26 (WebSearch returned nothing past August).
- action: captured, conviction 2 (one confirmation only — thinness stated in key_risk).

## [06:17 ET] SMMT SANITY CHECK — fetched range 12.07 / 29.23 matches the
  independently reported 52-week range of $12.07-$29.23, so the nasdaq bar series
  is not a bad feed. source: https://www.rttnews.com (via search, Aug 2026 item)

## [06:13 ET actual] EVENT CONTRACTS — the FOMC market, priced and rejected
`market_data.py events` is unusable for this: it pulls 200 unsorted open markets
and substring-filters them, so "Fed"/"FOMC"/"CPI" returned tennis matches and
then nothing. Queried the Kalshi API directly by series instead; the list
endpoint returns null prices, the single-market endpoint returns live ones.

KXFEDDECISION-26OCT, resolves on the 2026-10-28 14:00 ET decision (close 17:59Z):
| Leg | Outcome | last | yes_bid/ask | OI | 24h vol |
| --- | --- | --- | --- | --- | --- |
| `-H0` | Fed maintains rate | **93c** | 92/93 | 4.24M | 1.23M |
| `-H25` | Hike 25bps | **7c** | 6/7 | 2.85M | 0.91M |
| `-H26` | Hike >25bps | 1c | 0/1 | 0.96M | 94K |
| `-C25` | Cut 25bps | 1c | 0/1 | 1.45M | 26K |
| `-C26` | Cut >25bps | 1c | 0/1 | 0.23M | 427 |
source: https://api.elections.kalshi.com/trade-api/v2/markets/KXFEDDECISION-26OCT-H0 (and -H25/-H26/-C25/-C26)

- Also `KXRATECUT-26DEC31` "Fed cuts at least once before 2027": last **6c**,
  previous 3c — a cut for the whole of 2026 has doubled in price and is still 6c.
  source: https://api.elections.kalshi.com/trade-api/v2/markets/KXRATECUT-26DEC31
- **The market prices a 7-9% chance of a HIKE tomorrow and ~1% of a cut.** Hike
  risk, not cut risk. That is consistent with the 10y at 5.00% against 3.88%
  effective funds.
- **REJECTED as a trade.** H0 YES at 93c risks 93 to make 7 and needs better than
  93% to break even; I hold no information the 4.2M-contract open interest does
  not. There is no stated probability disagreement here, and strategy.md says the
  edge must be exactly that. Noted as macro context, not an idea.

## [06:14 ET actual] MACRO REGIME — defensive rotation, strong dollar, 5% 10y
Index/VIX/DXY/gold/WTI quotes all failed (yahoo 429; stooq symbols 404). Rebuilt
the regime from ETF proxies, which did fetch. All as of the 2026-10-26 close:

| Proxy | Last | % off 150d high | vs 20d | vs 50d | ATR% |
| --- | --- | --- | --- | --- | --- |
| SPY | 765.37 | -2.1% | below (770.14) | below (767.59) | 0.95 |
| QQQ | 712.20 | -6.6% | below (734.02) | below (725.43) | 1.74 |
| IWM | 276.99 | -9.2% | at (277.04) | below (285.85) | 1.31 |
| **SMH** | 541.62 | **-19.4%** | below (582.63) | below (574.17) | 3.53 |
| XLK | 186.32 | -8.3% | below (192.82) | below (189.57) | 2.28 |
| **GDX** | 81.02 | **-23.3%** | below (86.23) | below (92.68) | 3.68 |
| XLI | 166.96 | -11.3% | below (168.12) | below (171.85) | 1.62 |
| XLU | 42.55 | -10.8% | above (41.29) | below (41.83) | 1.47 |
| **XLV** | 179.28 | **-1.6%** | **above** (172.88) | **above** (171.36) | 1.73 |
| **XLP** | 87.96 | **-2.3%** | **above** (84.60) | **above** (84.42) | 1.57 |
| **XLE** | 69.64 | **-0.3%** | **above** (65.78) | **above** (64.49) | 2.13 |
| KRE | 72.73 | -7.2% | above (70.14) | above (72.26) | 1.76 |
| XLB | 51.38 | -5.2% | above (50.02) | above (50.99) | 1.28 |
| **UUP** | 29.01 | **-0.8%** | **above** (28.96) | **above** (28.50) | 0.40 |
| HYG | 77.20 | -4.4% | above (77.07) | below (78.23) | 0.36 |
| LQD | 104.02 | -5.7% | above (102.78) | below (104.23) | 0.61 |
source: market_data.py history (nasdaq daily bars)

**Read:** a higher-for-longer unwind of the two most crowded trades. Semis -19%
and gold miners -23% off their highs while healthcare, staples and energy sit
within 2.3% of theirs and the dollar within 0.8% of its high. Credit is soft but
not breaking (HYG only -4.4%, above its 20d). This is rotation, not risk-off —
SPY is 2% off a high while its growth engine is 6.6% off one.

**Consequence for today: the existing book is already the regime trade.** Long
energy/staples/healthcare/financials, short REITs/housing/long bonds. The value
today is in managing that, not in adding a fourth correlated expression of it.
The correlation cap in strategy.md bites: ABT + CVS + PFE already make three
healthcare longs, so XLV does not get added however good its relative strength is.

## [06:17 ET actual] CALENDAR VERIFICATION — book names
- **XOM Q3 2026: Friday 2026-10-30, press release 05:30 CT / 06:30 ET, call 08:30 CT.**
  Confirmed on Exxon's own IR calendar, not a remembered date.
  source: https://investor.exxonmobil.com/news-events/ir-calendar/detail/20261030-3q-2026-earnings-call
- **CVX: 2026-10-30 BMO** per the finnhub calendar. CONFLICT: TipRanks shows
  2026-10-23 BMO and labels it estimated; that date has already passed without a
  print, so I am taking 10-30. Flagging the conflict rather than hiding it.
- **HII: Thursday 2026-10-29 BMO** (finnhub calendar). Confirms yesterday's date.
- BCC 2026-11-02 amc; PFE 2026-11-03; CVS 2026-11-04 bmo; KHC 2026-11-04 bmo.
- **Tool caveat worth recording:** `earnings --days 10` returned 1500 rows and
  dropped XOM, CVX, HII and even today's FCX; `--days 3` returned 834 rows and
  included them. The response is truncated at 1500 and the truncation is not
  flagged. Always cross-check a specific symbol with a narrow window.

## [06:18 ET actual] POSITION UPDATE — the rate book into a 14:00 ET Fed decision
Four live positions are rate expressions. Applying the stop-ATR floor from
strategy.md, measured from ENTRY (confirmed by reading `check_stop_distance`
in validate_report.py, line 276 — `abs(entry - stop) / atr`), ETF swing floor 1.8:

| Pos | Entry | Stop | ATR | stop/ATR | R:R | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| TLT short | 79.90 | 82.00 | 0.8313 | 2.53 | 2.00 | structure OK, but spot 81.68 is **0.38 ATR from the stop** |
| ITB short | 89.80 | 93.60 | 2.4996 | **1.52** | 2.18 | **fails the 1.8 floor** |
| IYR short | 97.80 | 100.40 | 1.4686 | **1.77** | 2.81 | **fails the 1.8 floor by 0.03** |
| XLF long | 54.23 | 52.80 | 0.7164 | 2.00 | 2.36 | passes both |

- **ITB is infeasible, not fixable.** Clearing the 1.8 ATR floor needs risk >= 4.50,
  but R:R >= 2.0 needs risk <= 4.15 against the 81.50 target — and 81.50 is already
  below the 150-day low of 82.08, so lowering it further to buy headroom would be
  precisely the reverse-engineering strategy.md forbids. No valid structure exists.
  **CLOSE.**
- **IYR is fixable.** Widening the stop to 100.90 — above the 99.74 swing high of
  2026-10-23 and the 99.41 high of 10-26, not a cosmetic 5c nudge — gives 2.11 ATR
  and R:R 2.35. **HOLD with the stop widened.**
- **TLT: CLOSE.** Nothing structural is wrong; the problem is sequencing. A short
  0.32 points from its stop, after four straight up sessions through both the 78.93
  20-day and the 80.55 50-day, going into a decision at 14:00 ET tomorrow, is a coin
  flip with a known loss and an unknown gain. Re-affirms the close ordered 2026-10-26.
- **XLF: HOLD as-is.** The curve at +0.32 and steepening with zero 2026 cuts priced
  is the bank-NIM trade; spot 56.02 is 53% of the way to the 57.60 target.

## [06:20 ET actual] POSITION UPDATES captured so far (9 candidates)
- `DG` CLOSE (FTC suit + stop breached) | `SMMT` CLOSE (stop breached)
- `TLT` CLOSE (0.38 ATR from stop into FOMC) | `ITB` CLOSE (no feasible structure)
- `IYR` HOLD, stop widened 100.40 -> 100.90 (above the 99.74/99.41 swing highs)
- `XLE` TAKE PROFIT continuing, flat by the 10-29 close (XOM/CVX 10-30 BMO)
- `XLF` HOLD unchanged | `FCX` CLOSE re-affirmed (reports BMO today)
- `PYPL` WAIT — old 56.50 order stays cancelled; re-specified 51.60-53.20 post-print

## [06:20 ET actual] PYPL — why the level moved rather than the idea
- 2026-10-26: -3.56% to 54.99 on a 54.47 low, the session BEFORE its own print, and
  the first close below both the 55.47 20d and 55.72 50d in the fetched window.
- analysts: bullish share change **-1.9%**, revision_direction **deteriorating**;
  surprise record +9.4 / -6.1 / +3.6 / +5.9, i.e. 3 beats of 4.
- The published 56.50 entry is now 2.7% ABOVE the market and above both averages.
  Re-pitching it unchanged would be the anchoring prior_context warns about.
- DATA GAP: `short PYPL` → nasdaq ReadTimeout. No short interest / days-to-cover.

## [06:21 ET actual] REJECTED — KXFEDDECISION-26OCT-H0 — 93c for a 7c payoff, and no
  stated probability disagreement. Rejected on the strategy.md rule that an event
  contract needs an explicit edge, not a lean.
## [06:21 ET actual] REJECTED — KXRATECUT-26DEC31 — NO side costs 96.4c to make 3.6c.
## [06:21 ET actual] REJECTED — XLV long — best sector relative strength on the board
  (-1.6% off high, above 20d and 50d) but ABT + CVS + PFE are already three healthcare
  longs. strategy.md caps correlated ideas at 3 per driver. Rejected on correlation,
  not on merit.
## [06:21 ET actual] REJECTED — KRE long — the cleanest curve expression and above both
  averages, but XLF is already that bet. Same correlation cap.
## [06:21 ET actual] REJECTED — GDX long — 23.3% off its high is the deepest discount on
  the board, but GDX was stopped out of this very report on 2026-10-07 at conviction 4,
  it is below its 20d (86.23) AND 50d (92.68), and there is no dated catalyst. Buying a
  name that already stopped you out, with no new information, is re-litigation.

## [06:24 ET actual] CRYPTO — fetched, and rejected
- BTC **$79,437** (-1.13% 24h, $26.4B volume); ETH **$2,297.18** (-1.34%);
  SOL **$99.18** (-2.14%). source: coingecko via market_data.py crypto
- Proxies: IBIT 45.22, -8.4% off its 49.39 high, below the 46.92 20d, at the
  45.33 50d, ATR 2.54%. ETHA 52.34, **-16.7%** off high, below 20d (56.95) and
  50d (56.24), ATR 3.96%. Ether is leading the complex down.
- **REJECTED.** The bearish expression would be a short /MBT (Robinhood Crypto
  cannot short), and a short crypto futures position entered the day before a
  14:00 ET Fed decision is a macro coin flip, not an edge. A 2.5 ATR crypto swing
  stop is ~7%, needing a 14%+ target to clear 2.0 R:R, and nothing in the fetched
  data argues for a move that size on a thesis I can defend. No crypto today.

## [06:25 ET actual] AWAITING-ENTRY — the stale resting orders, decided
`VST` BUY @132.00, published 2026-08-24, 64 days ago. Spot 141.73.
- VST fell **9.8% in one session on 2026-10-22**, 156.14 -> 140.83, and sits
  -17.3% off its 171.35 high, below the 150.30 20d and 145.07 50d. ATR 8.98 (6.33%).
- The 150-day range low is **132.66**, so the 132.00 limit sits BELOW the entire
  fetched range. It can only fill on a break to new lows.
- The AI-power theme behind it is the one actively unwinding: SMH -19.4%, and CEG
  — the same trade — was stopped out of this report on 2026-10-23. **CANCEL.**

`OXY` BUY @54.00 (pub 2026-09-24). Spot 64.07, **18.6% above the limit**, with OXY
only 5.0% off its 67.45 high and above both averages. The order cannot fill
without energy giving back a quarter of its advance. **CANCEL** — stale, not wrong.

`AAL` SELL_SHORT @13.35 (pub 2026-10-03). Spot 12.20, so the short limit is 9.4%
ABOVE the market and fills only on a rally. ATR 0.5682 (4.66%). A 2.0 ATR stop is
14.49; the 150-day low is 10.09, so even a target at 10.80 gives only 2.24 R:R on a
name already 35.1% off its high — most of the downside is behind it, and DAL was
stopped out of this report on 2026-10-14. **CANCEL.**

`GLD` SELL @406.77 (pub 2026-10-25). Covered above — 10.6% above spot, unreachable.
**CANCEL.**

`KXCPIYOY-26SEP-T3.5` NO @18 (pub 2026-09-30) — September CPI contract, resolved.
**RETIRE** from the book.

## [06:28 ET actual] CHECKPOINT — 23 candidates, the whole book is covered
Closes (6): DG, SMMT, TLT, ITB, FCX, and XLE as a take-profit in execution.
Cancels (4): VST, GLD, OXY, AAL resting orders.
Holds (12): IYR (stop widened), XLF, UNP (stop widened), HII, ABT, CVS, STLD,
KHC, LULU, NKE, PFE, BCC.
Wait (1): PYPL, re-specified 51.60-53.20 post-print.
Retire (0 captured): KXCPIYOY-26SEP-T3.5 has resolved; nothing to trade, noted only.

Two book-level findings worth recording, both of which should have been caught earlier:
1. **ITB short and BCC long were the same view taken both ways** — a housing short
   and a wood-products long held simultaneously since 2026-09-30. Different
   horizons, so defensible; not noticing it was not. The ITB close ends it today.
2. **Four positions had stops inside the ATR floor**: ITB 1.52, IYR 1.77, UNP 1.98,
   and FCX at 0.84 ATR from SPOT on an earnings morning. Two were fixable (IYR,
   UNP), two were not (ITB infeasible, FCX out of time). This is the single most
   common defect in the book and it is the documented cause of the stop-out record.

## [06:29 ET actual] NEW-IDEA HUNT — the constraint set, stated before searching
Not eligible today, with the reason:
- healthcare — ABT + CVS + PFE is already the 3-idea correlation cap
- financials/curve — XLF holds it; KRE rejected above
- rate direction — FOMC at 14:00 ET tomorrow; no new rate bet the day before
- crypto — rejected above; the bearish expression needs futures into the same Fed
- energy — XLE is being closed at a 150-day high; adding energy while harvesting
  it would be two opposite instructions on one driver in one report
- anything reporting 10-27 or 10-28 — entering before a print is a gap bet
That leaves consumer staples (only KHC, so 1 of 3 used) and genuinely idiosyncratic
small caps. Hunting staples value with an insider-buying filter, time-boxed.

## [06:31 ET actual] REJECTED — CPB — the insider "cluster" is 300 shares
Ran the insider filter on the four de-rated packaged-food names. CPB looked like
the hit — `open_market_buys: 3` — and it is noise:
- All three Form 4 purchases are the **same person on the same day**: Dorrance
  Bennett JR, 2026-06-09, 100 shares each at 21.45. **$6,435 in total**, four
  months ago, by one member of the founding family. `distinct_buyers: 1`.
- That is one confirmation reported three times, which is the exact failure
  strategy.md names for evidence counting, arriving here in insider form.
- CAG: 1 buy, 1 buyer. GIS: 0. SJM: 0. **No insider signal in the group.**
- source: market_data.py insiders (finnhub Form 4 aggregation)

## [06:31 ET actual] REJECTED — CAG / GIS / CPB / SJM — no catalyst, no anchor
All four are de-rated staples in the second-strongest sector, and all four share
one unexplained move: **2026-10-22 was a sector-wide spike** — CAG +7.3% (14.04 ->
15.07), GIS +8.0% (32.57 -> 35.18), CPB +8.7% (19.56 -> 21.26), SJM +4.4%. All four
then gave part of it back over the following two sessions.
- I could not establish what caused it. WebSearch returned nothing for the date.
  **An 8% sector move I cannot explain is not a base to build an entry on.**
- None reports inside the horizon (these are Dec/Jan fiscal reporters), so a swing
  idea would have no catalyst, and a long_term idea would need a defended valuation
  anchor I do not have time to build properly. The long_term lane is 0/4 at -15.2%;
  inventing an anchor to fill it would be the worst available use of that record.
- Chart profile is identical across all four: above the 20-day, below the 50-day,
  12-20% off the high. Genuine watchlist material, not a recommendation today.
  CAG 14.58 (20d 13.90 / 50d 14.82) | GIS 33.70 (32.73 / 35.83) |
  CPB 20.63 (19.66 / 21.07) | SJM 128.64 (122.70 / 123.71)
- **Watchlist condition**: a close above the 50-day on one of these, with an
  explanation for the 10-22 move in hand, makes it a real idea. Not before.

## [06:32 ET actual] ZERO NEW ENTRIES — and why that is a finding, not an omission
Today's 23 candidates are entirely decisions on an existing 18-position book plus
5 stale resting orders. **This is the second consecutive day with no new entry**,
and that deserves naming rather than burying: two days running is the point at
which "selective" starts to become "not looking".

The case that it is correct today:
- Six of the seven sectors a new idea could have come from are either already at
  the 3-idea correlation cap, or are the rate trade the day before a 14:00 ET
  FOMC decision, or are the energy position being harvested in this same report.
- The two genuinely uncrowded lanes were hunted and came up empty on evidence
  rather than on taste: crypto has no non-coin-flip expression into the Fed, and
  the staples value group failed the insider filter at $6,435.
- The book is already the regime trade. Long energy/staples/healthcare/financials,
  short duration — which is precisely what the relative-strength table says is
  working. Adding a fourth correlated expression is not diversification.

The case that it is a weakness, stated honestly: this report publishes 23 rows and
none of them is a new opportunity, so a reader who is flat gets nothing actionable
except the PYPL post-print condition. The honest summary is that today's edge was
in what the book should stop doing, and there was quite a lot of that — six closes,
four cancels, and two stops that were inside the floor.

## [06:33 ET actual] SOURCES THAT FAILED
- **yahoo finance: HTTP 429 on everything.** Killed every index, VIX, DXY, gold,
  WTI and futures quote in `macro`. Regime rebuilt from ETF proxies instead.
- **stooq: 404** on ^spx, ^dji, ^vix, 10usy.b, 2usy.b — not a usable fallback.
- **finnhub indices:** "Market data subscription required for CFD indices."
- **nasdaq short interest: ReadTimeout** on every symbol tried (SMMT, PYPL, LULU).
  No short-interest or days-to-cover read anywhere in this report. This matters
  most for LULU and NKE, where squeeze risk on two consumer shorts is unquantified.
- **market_data.py events:** structurally unable to find macro markets — it pulls
  200 unsorted open Kalshi markets and substring-filters, so "Fed" returned tennis
  and "FOMC"/"CPI"/"interest rate" returned nothing. Worked around by querying the
  Kalshi series endpoint directly; the list endpoint returns null prices, the
  single-market endpoint returns live ones. Worth fixing in the tool.
- **market_data.py earnings --days 10:** silently truncates at 1500 rows and drops
  near-dated names (XOM, CVX, HII, and FCX which reports today). `--days 3` is
  correct. The truncation is not flagged in the response.
- CoinGecko failed inside `macro` but succeeded on a direct `crypto` call.

## [06:34 ET actual] RESEARCH COMPLETE
- candidates: 23
- new entries: 0 — see the block above; this is deliberate and argued, and it is
  the second day running, which is itself flagged as a risk
- coverage gaps: no short interest anywhere (nasdaq timeouts); no index, VIX or
  DXY level fetched (yahoo 429) so the regime is inferred from ETF proxies; the
  cause of the 2026-10-22 packaged-food spike is unknown; CVX earnings date has
  conflicting sources (finnhub 10-30 vs a stale TipRanks estimate of 10-23)
- sources that failed: yahoo finance (429), stooq (404), finnhub CFD indices
  (subscription), nasdaq short interest (ReadTimeout), market_data.py events
  (cannot reach macro markets by design), market_data.py earnings --days 10
  (silent 1500-row truncation)

## [TIMESTAMP CORRECTION] my clock labels above ran ahead of the real one
The `[HH:MM ET]` labels earlier in this file were written from my own estimate of
elapsed time, which drifted ahead of the wall clock by about 4-6 minutes. Verified
against `date`: the run began 06:01 ET and the entries labelled 06:28-06:34 were
actually written 06:24-06:27. The ORDER of entries is accurate and no price or
figure is affected - every price in this file is the 2026-10-26 close. Entries
below this line carry verified wall-clock times.

## [06:29 ET verified] XLE CONCENTRATION — the exit date, verified at the issuer
Re-fetched the issuer's own page rather than carrying "about 42%" forward:
- **XOM 24.10%, CVX 18.14%, combined 42.24% of the fund, as of 2026-10-26.**
  (Index weights as of 10-23: XOM 24.08%, CVX 18.35%, combined 42.43%.)
- source: https://www.ssga.com/mainfund/xle (sectorspdrs.com 302-redirects there)
- **It is worse than the Friday print alone.** The same page gives COP 7.22%,
  MPC 4.83%, PSX 4.59%, VLO 4.55%, EOG 4.06%. Cross-referencing the fetched
  earnings calendar: MPC reports 2026-11-03 bmo, COP 2026-11-05 bmo, EOG
  2026-11-05 amc. So **roughly 58% of the fund reports between 10-30 and 11-05** —
  XOM+CVX 42.24%, plus COP 7.22%, MPC 4.83%, EOG 4.06%.
- That is the argument for the Thursday 10-29 time stop, now quantified: holding a
  9%-profit sector position past this week is not holding a sector, it is holding
  five earnings releases. Re-capturing XLE with the exact figure.

## [06:35 ET verified] PRIMARY DOCUMENT — SMMT 8-K of 2026-09-28: the $2.0bn AZ deal
I had recorded "no company disclosure behind the decline". **That was wrong**, and
reading the filing I had already listed but not opened is what found it.
8-K dated 2026-09-28, Items 1.01, 3.02, 5.03, 8.01, 9.01:
- Summit agreed to sell **108,955.3686 Class A Convertible Preferred shares at
  $18,356.14 each to AstraZeneca Holdings B.V.**, for "aggregate gross proceeds to
  the Company of $2.0 billion".
- Each preferred converts into **1,000 common**, so **108,955,369 common shares**
  at an effective **$18.3561 per common share**.
- Paired with a separate clinical trial collaboration to evaluate **sonesitatug
  vedotin with ivonescimab**.
- Conversion is **blocked** until the HSR waiting period expires AND an increase in
  authorized common shares takes effect. **If that increase is not effective within
  18 months, Summit must redeem the preferred for cash** at a price tied to the
  market value of the underlying common.
- Summit must file a **resale registration statement within 60 days of closing**
  (closing expected within five business days of signing).
- The filing's own risk language flags dilution, possible sales by the investor,
  and conflicts of interest.
- source: https://www.sec.gov/Archives/edgar/data/1599298/000119312526405776/d178892d8k.htm

**Three consequences, and the first one is a correction to my own note above:**
1. The **2026-11-04 annual meeting is not "not a data event"** — the DEF 14A filed
   2026-10-19 for that meeting is where the authorized-share increase is voted on,
   and that vote is what unlocks AZ's conversion and avoids the cash-redemption
   obligation. It is a genuine dated catalyst eight sessions out.
2. **SMMT closed 14.50, which is 21.0% BELOW the $18.3561 AstraZeneca paid.** The
   strategic investor is underwater on a deal struck four weeks ago.
3. The resale registration for ~109M shares lands around early December — a visible,
   dated overhang rather than a vague dilution worry.
This does not reverse the close (the 14.40 stop was still breached at a 14.37 low),
but it replaces "unexplained weakness" with a specific mechanism, and it upgrades
the evidence from one confirmation to two. Re-capturing SMMT.

## [06:37 ET verified] SHORT INTEREST — unavailable, confirmed on retry
Retried `market_data.py short` for LULU, NKE and SMMT. All three returned
`ReadTimeout` against api.nasdaq.com again, on a second attempt several minutes
after the first. **There is no short-interest or days-to-cover figure anywhere in
today's report.** It matters most for the two consumer shorts, LULU and NKE, where
squeeze risk is the main way to be right about the business and still lose; both
are held at 1.5% rather than 2.5% partly for that reason, and both now carry an
explicit cover-on-two-closes rule instead of relying on a distant stop.

## [06:38 ET verified] LESSON FROM THIS RUN, worth keeping
I listed SMMT's EDGAR filings early, used the index to conclude "no disclosure
explains the drop", and did not open the 8-K that was sitting in that same list.
The filing contained a $2.0bn AstraZeneca preferred placement, 108,955,369
conversion shares, a dilution vote on 2026-11-04 and a resale registration due in
early December - i.e. the entire mechanism. **A filing index is not a filing.**
Reading the list and reporting on it as though I had read the documents is the
same error class as counting three articles about one press release as three
confirmations. It cost nothing here only because the close was already correct on
the stop; on a hold it would have been a published thesis built on a gap I had
already been handed the answer to.

## [06:39 ET verified] FINAL — RESEARCH COMPLETE (supersedes the earlier block)
- candidates: 25 captures / 23 distinct symbols (XLE and SMMT each re-captured
  after verification improved them; synthesis takes the last entry per symbol)
- composition: 6 closes (DG, SMMT, TLT, ITB, FCX, + XLE as a take-profit in
  execution), 4 resting-order cancels (VST, GLD, OXY, AAL), 12 holds of which 2
  carry stop changes (IYR 100.40->100.90, UNP 277.40->277.00), 1 wait (PYPL)
- new entries: **0**, argued at length above and flagged as a two-day pattern
  rather than presented as a virtue
- every price in this report is the 2026-10-26 close, taken at 06:0x ET with the
  equity market shut. That is a closed market, not stale data.
- coverage gaps: short interest unavailable everywhere (nasdaq timeouts, retried);
  no index, VIX, DXY, gold or WTI level fetched (yahoo 429, stooq 404, finnhub
  CFD-gated) so the regime is inferred entirely from ETF proxies; the cause of the
  2026-10-22 packaged-food spike (CAG +7.3%, GIS +8.0%, CPB +8.7%) is unknown;
  CVX earnings date has conflicting sources
- sources that failed: yahoo finance (429 on everything), stooq (404), finnhub CFD
  indices (subscription required), nasdaq short interest (ReadTimeout x2 rounds),
  market_data.py events (cannot reach macro Kalshi markets by design - worked
  around via the series endpoint), market_data.py earnings --days 10 (silent
  1500-row truncation that dropped XOM, CVX, HII and today's FCX)

## [06:41 ET verified] CONVICTION DISTRIBUTION — flagging it myself
Of the 23 distinct candidates: **twenty score 3**, two score 2 (OXY and AAL, both
cancels with one confirmation each), one scores 4 (XLE). That is precisely the
shape CLAUDE.md calls unreadable — 39 of the first 57 ideas scored 3 and the
by-conviction table carried no information as a result. So it needs explaining
rather than leaving for the red team to find:

- Every 3 here is backed by exactly **two distinct evidence kinds**, which is what
  a 3 means under the rule. It is not a default; it is what the rule returns on a
  day whose work was position management.
- The reason it clusters is structural. A hold or a close on an existing position
  has a `technical_level` (the stop, the averages, the range, all from fetched
  bars) plus usually one more — a `dated_catalyst` where an earnings date exists,
  a `primary_document` where a filing explains it. There is rarely a third,
  because nobody re-underwrites a valuation anchor to decide whether to keep a
  position they already hold.
- Four candidates actually carry **three** kinds and I left them at 3 rather than
  claiming 4: IYR, PYPL, KHC and BCC. Validation will report that the evidence
  supports 4. **That under-claim is deliberate** — in each case the third kind is
  a sector relative-strength read that leans on the same fetched bar set as the
  technical level, and I would rather the red team raise a score than lower one.
- The one 4, XLE, earns it on four genuinely independent kinds: Exxon's own IR
  calendar, the issuer's holdings page, the bar series, and the cross-sectional
  relative-strength table.
- The honest read of the table: today's report is 20 conviction-3 decisions on a
  book, not 20 conviction-3 ideas. The by-conviction performance table should be
  expected to learn almost nothing from this day, and that is a property of the
  day rather than a scoring failure.
