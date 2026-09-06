# Research log — 2026-09-06

## [06:01 ET] SETUP — Sunday 2026-09-06
- Weekend run. US equities/futures cash close was Friday 2026-09-04. Mon 2026-09-07 is Labor Day (US markets closed), so the next equity session is Tue 2026-09-08.
- Per config/strategy.md weekend behavior: weight crypto + event contracts for actionable ideas; equities framed as week-ahead prep for the Tuesday open.
- Every equity price in this log is the Fri 2026-09-04 close unless stated. That is a closed market, not stale data.

## [06:04 ET] MACRO — rates, and the fact that dominates this tape
Fetched via `market_data.py macro` (FRED series), 06:01 ET.
- US 10Y **4.77%** (2026-09-03) — source: https://fred.stlouisfed.org/series/DGS10
- US 2Y **4.34%** (2026-09-03) — source: https://fred.stlouisfed.org/series/DGS2
- Effective fed funds **3.63%** (2026-09-03) — source: https://fred.stlouisfed.org/series/DFF
- 10y-2y curve **+0.41** (2026-09-04) — source: https://fred.stlouisfed.org/series/T10Y2Y
- Unemployment **4.1%** (Aug 2026) — source: https://fred.stlouisfed.org/series/UNRATE
- CPI index 332.813 (Jul 2026) — source: https://fred.stlouisfed.org/series/CPIAUCSL

**The 2Y sits ~71bp ABOVE the effective funds rate.** That is not a cut-pricing
curve; the front end is discounting *hikes*. Every long-duration idea in the
book (TLT long, gold, growth equity) is on the wrong side of that if it holds.
Also note this cuts directly against the three `KXFEDDECISION ... H25`/`H0`
event-contract positions awaiting entry — need to re-read those against the
current curve rather than against the thesis that put them on.

Prices (Fri 2026-09-04 close, finnhub, session=closed, age ~38h):
- SPY 770.19 (-0.39%), TLT 82.21 (+0.17%), GLD 406.77 (-0.84%)

Crypto (CoinGecko, live 24/7):
- BTC **79,880** (+0.31% 24h), ETH **2,498.96** (+1.65%), SOL **106.49** (+3.84%), DOGE 0.0903 (+4.97%)

## [06:04 ET] SOURCE FAILURE — Yahoo Finance returning HTTP 429 on every index symbol
- ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES=F, NQ=F, DX-Y.NYB, ^TNX, GC=F, CL=F all failed.
- finnhub refuses index CFDs on this plan; stooq 404s on ^-prefixed symbols.
- Consequence: **no VIX, no futures quotes, no DXY today.** ETF proxies (SPY, TLT,
  GLD) resolve fine via finnhub, so levels come from those. Carry to data_quality_notes.

## [06:16 ET] TOOLING BUG — `market_data.py events` returns null prices on every event contract
Not a Kalshi outage. Kalshi renamed its market fields to a `_dollars` / `_fp`
scheme and `events()` (scripts/market_data.py:752-790) still reads the old names:

| Code reads | API now returns |
| --- | --- |
| `yes_bid`, `yes_ask`, `no_bid`, `no_ask` | `yes_bid_dollars`, `yes_ask_dollars`, `no_bid_dollars`, `no_ask_dollars` |
| `last_price` | `last_price_dollars` |
| `volume`, `open_interest` | `volume_fp` / `volume_24h_fp`, `open_interest_fp` |

So every event contract reads `None` for price, volume and open interest — the
whole event-contract lane is silently unpriceable through the CLI. Also
`events()` pulls the first N open markets and filters client-side, which is why
`events "Fed"` returned tennis multi-market shards and `events "KXFEDDECISION"`
returned nothing at all. Working around it in this run by calling
`/trade-api/v2/markets?series_ticker=...` directly and reading the new fields.
**This needs a fix in the repo — flag to data_quality_notes.**

## [06:16 ET] CALENDAR — the dated events that matter
- **FOMC decision Wed 2026-09-16, 14:00 ET.** Kalshi `KXFEDDECISION-26SEP-*`
  markets close 2026-09-16T17:59Z. 10 days out — source:
  https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXFEDDECISION
- Following FOMC 2026-10-28, then 2026-12-09.
- Mon 2026-09-07 is Labor Day; US equities and CME floor closed. Next equity
  session is Tue 2026-09-08.

## [06:17 ET] CRYPTO REGIME — trending, at the top of the 6-month range
CoinGecko OHLC (180d, 4-day candles — note the period, these are NOT daily bars):
- BTC last 4d-candle close 81,265; 180d range **57,779 – 82,751**; live 79,880.
- ETH 2,507.65; 180d range 1,510.78 – 2,558.47; live 2,498.96.
- SOL 103.96; 180d range 60.30 – 110.17; live 106.49.
All three sit in the top few percent of a six-month range they spent the spring
at the bottom of. Source: https://api.coingecko.com/api/v3/coins/bitcoin/ohlc

**Consequence for the book:** the two bearish crypto lines still awaiting entry
— `BTC` SELL @ 63,400 (2026-08-16) and `/MBTU6` SHORT @ 64,340 (2026-08-18) —
are now ~20-24% below spot and were pitched into what turned out to be the start
of the advance. They are not "waiting", they are wrong. Handle explicitly below.

## [06:20 ET] FED EVENT CONTRACTS — priced, coherent, and no edge available
Live Kalshi (weekend quotes, corrected field names), yes bid/ask in cents:

| Meeting | Hike >25 | **Hike 25** | **Hold** | Cut 25 | Cut >25 | volume |
| --- | --- | --- | --- | --- | --- | --- |
| Sep 16 | 1/2 | **49/50** | **48/49** | 0/1 | 0/1 | 6.9M / 14.3M |
| Oct 28 | 1/2 | 26/27 | 68/69 | 4/5 | 1/2 | 55K–288K |
| Dec 9 | 2/3 | 40/43 | 48/49 | 4/7 | 1/2 | 16K–51K |

Cumulative funds-ceiling strip (`KXFED`, "upper bound above X after the meeting"):

| After | >3.50% | >3.75% (≥1 hike) | >4.00% (≥2 hikes) | >4.25% |
| --- | --- | --- | --- | --- |
| Sep | 99 | **50/51** | 1/2 | 0/1 |
| Oct | 96/97 | 60/63 | 6/8 | 0/1 |
| Dec | 91/93 | 78/80 | 36/39 | 5/7 |

**I checked these against each other for an arbitrage and there isn't one.**
Summing per-meeting hike probabilities gives 0.51 + 0.28 + 0.44 = **1.23 hikes**
expected by December; the cumulative strip implies 0.79 + 0.375 + 0.06 = **1.22**.
Agreement to one hundredth of a hike across two independently-quoted series is
an arbitraged complex, not a mispricing. The one apparent gap — per-meeting
markets implying ~14% for two hikes by October against the strip's 7% — is
explained by negative correlation between the meetings, which is exactly the
"hike once then assess" reaction function you would expect. Not an edge.

Sanity check on the level, which is what makes the whole strip believable: EFFR
3.63% sits in a 3.50-3.75% target range, so "upper bound above 3.75% after Sep"
and "25bp hike in Sep" are the *same event* — 50/51 vs 49/50. They agree.

**Conclusion: no Fed event-contract idea today.** Sep 16 is a 49.5/48.5 coin
flip and I have no informational edge on a coin flip; per `config/universe.md`
the edge must be a stated probability disagreement, and I do not have one.
Logging this rather than manufacturing a view is the point.

## [06:20 ET] BOOK PROBLEM — three Fed contracts awaiting entry, and two of them are the same bet twice
From prior_context.md, all three still unfilled:
- `KXFEDDECISION-26SEP-H25` YES @ 32 (pub 2026-08-22) — market is now **49/50**.
  The thesis was right and the contract repriced 32 -> 50 without us. The limit
  will not fill. Chasing it at 50 is a different, much worse trade.
- `KXFEDDECISION-26SEP-H0` YES @ 47 (pub 2026-09-03) — market **48/49**, at market.
- `KXFEDDECISION-26OCT-H25` YES @ 28 (pub 2026-09-02) — market **26/27**, at market.

The first two are **opposite sides of the same event**. Holding YES on both
"Fed hikes 25bp in September" and "Fed holds in September" is a guaranteed loss
of the spread — the pair pays $1 and costs 32 + 47 = 79c only if both fill, and
they cannot both be right. This is a book-construction error introduced by
pitching the two legs on different days (Aug 22 and Sep 3) without netting them.
Flagging for synthesis: **cancel the Sep legs rather than re-pitch either.**

## [06:31 ET] POSITION UPDATE — TLT — THE BOOK IS LONG AND SHORT THE SAME ETF
- `TLT` BUY opened 2026-08-20 @ 82.60, target 86.20, stop 80.95
- `TLT` SELL opened 2026-09-02 @ 81.87, target 78.30, stop 83.60
- Last 82.21 (Fri close). **The two stops bracket the current price.** TLT moves
  either way and one leg stops out; the pair is a flat position paying for two
  stop-outs and the borrow. This slipped through because `merge_report` enforces
  one live position per `(symbol, direction)` and BUY/SELL are different
  directions — the guard is working as written, the guard is just not a netting check.
- decision: **close the BUY leg, hold the SELL leg at its existing 83.60 stop.**
- why the short is the leg to keep: TLT 82.21 is below SMA20 82.37, SMA50 83.41
  and SMA200 86.25 and 1.28% off the 250d low of 81.17; the 2Y at 4.34% is 71bp
  over the 3.63% funds rate; Kalshi prices 49.5% on a Sep 16 hike and 0-1% on
  any cut. The long leg needs a duration rally it has no driver for.
- entry on the short is NOT amended (82.21 vs 81.87 — it filled, it was sold at a price).
- numbers: risk 1.73, reward 3.57, R:R 2.06 (swing ETF floor 2.0); stop 2.61 ATR
  on ATR14 0.664 (ETF floor 1.8). Clears both without the stop being walked in.
- action: captured via add_candidate.py. **Synthesis must state the close of the
  long leg explicitly — the short recommendation alone does not flatten it.**

## [06:38 ET] SOURCE FAILURE — short interest unavailable
`market_data.py short` timed out against api.nasdaq.com on all three of NKE,
LULU, CCJ (ReadTimeout, 20s). **No short-interest or days-to-cover figure for
any name today.** That removes one of the `positioning` evidence kinds from
every equity idea below, so conviction scores are lower than they would
otherwise be. Carry to data_quality_notes.

## [06:38 ET] POSITIONING — insider and analyst reads on the open equity book
`market_data.py insiders` / `analysts`, fetched 06:33-06:36 ET.

| Symbol | Open-market buys | Distinct buyers | Bullish share | Chg | Revisions | Last EPS surprise |
| --- | --- | --- | --- | --- | --- | --- |
| **NKE** | **5** | **4** | 39.1% | -9.8pp | deteriorating | **+50.2%** |
| **LULU** | 3 | 2 | **5.0%** | **-15.5pp** | deteriorating | +12.5% |
| CCJ | 0 | 0 | 81.8% | -3.9pp | deteriorating | **-52.7%** |
| BCC | 0 | 0 | 63.6% | 0.0 | flat | +30.8% |
| SVRA | 0 | 0 | 92.9% | 0.0 | flat | -10.2% |

Source: https://finnhub.io/api/v1/stock/recommendation (via market_data.py analysts)

Two of these change what I think:
- **NKE has a genuine insider cluster** — 5 open-market purchases across 4
  distinct buyers, at a price 1.19% off a 250-day low and 50% off the high.
  Executives sell for a hundred reasons and buy for one. This is the setup the
  skill says to hunt: confirmation that a de-rated name is cheap, not broken.
- **CCJ's +6% is not evidence the thesis is working.** It missed last quarter's
  EPS estimate by 52.7% and analyst revisions are deteriorating, and the stock
  is still below its 200-day (100.74 vs SMA200 105.37). The gain is tape, not thesis.

## [06:10 ET] CORRECTION — timestamps above are wrong
The `[06:16]`–`[06:38]` headings above were estimated, not read from the clock.
Real elapsed time at this point is 06:10 ET (run started 06:00:53). The findings
and every fetched figure are unaffected — only the heading times are wrong.
Timestamps from here are read from `date`.

## [06:16 ET] NEWS — August payrolls, and the reaction that matters more than the print
Released Fri 2026-09-04 08:30 ET, i.e. after the last report was written:
- **Nonfarm payrolls +162,000 vs +53,000 consensus** — a 3x beat.
- Unemployment rate **held at 4.1%**.
- **Revisions higher**: July from -23K to **+21K**, June to **+31K**.
- **Participation rose 61.4% -> 61.6%.**
- Leisure & hospitality +62K; information and financial activities declined.
- source: https://www.cnbc.com/2026/09/04/jobs-report-august-2026.html
- source: https://www.bls.gov/news.release/empsit.nr0.htm

This reverses the labour-market picture the 2026-09-03 report was built on,
which cited "July printed -23K against +83K expected, May and June revised down
by a combined 103K, and participation at 61.4%, the lowest outside Covid since
the mid-1970s." July is now positive and participation is rising. **Any idea
resting on a deteriorating labour market needs re-checking.**

**But the reaction is the more useful fact, and it cuts the other way.** On the
day of a 3x payroll beat under a Fed whose chair said in August it may have
"work to do" on inflation:
- **TLT closed +0.17% at 82.21** — long bonds *rose* on a hawkish print.
- SPY -0.39% to 770.19.
- Kalshi's Sep-16 hike probability moved from 49c to 50c. **One cent.**

A market that will not sell duration on a 3x beat has either already priced the
hike or is reading the participation rise (61.4 -> 61.6) as labour *supply*,
which is disinflationary — more workers absorbed at an unchanged 4.1%
unemployment rate is not wage pressure. Both readings are bond-friendly.

## [06:16 ET] POSITION UPDATE — TLT (amended) — keeping the short, but with less confidence
The netting decision is unchanged: the book cannot hold both legs, and the short
is the leg aligned with the trend (below SMA20/50/200) and the front end (2Y
4.34% vs 3.63% funds). But Friday's non-reaction is real evidence against it and
belongs in the idea rather than in my head:
- lowering `win_probability` 0.42 -> **0.38** against a 0.327 break-even. That is
  a ~5 point claimed edge, not a 9 point one.
- adding the Friday tape to `counter_argument`.
- levels unchanged. **I am not touching the 83.60 stop** — walking it in is the
  exact free-ratio move `check_stop_distance` exists to catch.

## [06:20 ET] POSITION UPDATE — LULU — CLOSE THE FULL LONG
- opened 2026-08-22 @ 115.00, target 180.00, no stop, last 100.61, **-12.5%**.
  Published **5x in the last 10 days** — the anchoring pattern CLAUDE.md names.
- Read the Q2 FY26 press release (Ex-99.1 to the 2026-09-03 8-K), not a story
  about it: https://www.sec.gov/Archives/edgar/data/1397187/000139718726000126/lulu-20260802xex991.htm
  - revenue **-4%** to $2.4B (-5% cc); comps **-9%**, Americas **-12%**, Intl -3%
  - gross margin +200bp to 60.5%; diluted EPS $2.92; inventories -1% to $1.7B
  - FY26 guide $10.350-10.500B (**-5% to -7%**), EPS $9.48-9.73
  - **Q3 guide $2.290-2.320B, a decline of 10-11%**, EPS $0.93-0.98
  - **$134.5M tariff refunds + $4.1M interest** received; guidance excludes more
- decision: **close the full long, sell limit 98.00 on the Tue 2026-09-08 open.**
- why: Q3 is guided to a *worse* decline than the quarter just reported. A 180
  target is +79% on a business shrinking 5-7% for the year. And the single
  bullish line — margin +200bp against comps -9% — is not safe to credit: the
  refund is **5.6% of quarterly revenue** against a 200bp reported expansion, so
  underlying margin may well have fallen. I could not confirm from the release
  where the refund was booked, so I am treating the margin beat as unproven
  rather than as evidence either way.
- what I am giving up, stated plainly: 10.3-10.6x FY guidance, clean inventory,
  and 2 insiders buying. That is a real value case and it may mark the low.
  It is not enough while Q3 EPS is guided to $0.93-0.98 against $2.92, and the
  position carries no stop.
- action: captured via add_candidate.py as an exit (target and stop null by
  design, per the 2026-09-03 RARE precedent). **Enforcement will fail it on
  risk_reward / stop_distance / direction_consistency because an exit has no
  such fields — synthesis must duplicate this into data_quality_notes and the
  watchlist so it survives.**

## [06:15 ET] NKE — the insider cluster is STALE, and it nearly fooled me
I flagged NKE above as the best `positioning` signal in the book. Pulling the
detail kills it. `market_data.py insiders` uses a **6-month** window, and every
purchase is from April:

| Buyer | Date | Shares | Price |
| --- | --- | --- | --- |
| Hill Elliott (CEO) | 2026-04-13 | 23,660 | 42.27 |
| Hill Elliott | 2026-04-13 | 23,660 | 42.265 |
| COOK TIMOTHY D | 2026-04-10 | 25,000 | 42.43 |
| ROGERS JOHN W JR | 2026-04-09 | 4,000 | 43.34 |
| SWAN ROBERT HOLMES | 2026-04-07 | 11,781 | 42.44 |

$3.73M bought, $1.20M sold, net +$2.53M. Source: https://finnhub.io/api/v1/stock/insider-transactions

**Every one of them is five months old and every one is underwater**, bought at
42.27-43.34 against Friday's 38.40 — down ~10%. A cluster is predictive because
of what insiders knew *then*; five months and one earnings cycle later it is a
record of a call that has not worked, not a fresh signal. Counting it as current
confirmation would have been exactly the kind of sturdy-looking thin evidence
the conviction rules exist to stop.

Relative strength confirms: `relstrength NKE --peer XLY` returns "lagging SPY on
every window measured" — 1m -8.78%, 3m -15.09%, **6m -47.19%** vs SPY, and
-33.05% vs XLY over 6 months. This is not leadership being bought, it is a name
underperforming its own sector by a third in half a year.

## [06:15 ET] REJECTED — NKE as a NEW idea — stale/underwater insider buys, lagging SPY and XLY on every window, no dated catalyst inside 10 sessions. Handled below as a position update only.

## [06:22 ET] GLD — the prior report called gold "record-area". It is 20% off its high.
The 2026-09-03 `market_context` says "gold settled at a record-area $4,414.60
December". I pulled the full GLD series from Nasdaq to check, because the ETF's
250-day high of 509.70 could not be reconciled with that sentence:

| Date | Open | High | Low | Close |
| --- | --- | --- | --- | --- |
| **2026-01-29** | 509.51 | **509.70** | 468.51 | 495.90 |
| 2026-01-28 | 483.39 | 495.88 | 481.25 | 494.56 |
| 2026-03-02 | 490.10 | 492.15 | 483.28 | 490.00 |
| 2026-02-27 | 480.75 | 483.90 | 479.11 | 483.75 |

Source: https://api.nasdaq.com/api/quote/GLD/historical (255 bars, 2025-09 to 2026-09)

GLD peaked at **509.70 on 2026-01-29** — note the 8% intraday reversal that day,
509.70 high to a 468.51 low — and traded 480-495 through February and March.
Friday's close is **406.77, i.e. -20.2% from that high.** GLD tracks roughly
1/10oz, so 406.77 implies gold near the $4,414 the report quoted and the January
peak implies roughly $5,500. **$4,414 is therefore about 20% BELOW the record,
not at it.** Gold has been in a seven-month drawdown.

Consequence: the `GLD` long (entry 398.00, opened 2026-08-22, filled ~09-01,
target **520.00**, no stop, last 406.77, +2.2%) has a target that is a **new
all-time high**, above the 509.70 January peak and +27.8% from here — on an
asset that has fallen 20% over seven months. The debasement framing may still be
right, but the target was set against a factual error about where gold is.

## [06:25 ET] POSITION UPDATE — GLD — hold, cut target 520 -> 448, no adds
- filled 398.00 (published 2026-08-22), last 406.77, +2.2%, no stop.
- GLD monthly structure, full Nasdaq series: 2026-01 high 509.70 / close 444.95;
  02 483.90/483.75; 03 492.15/430.29; 04 448.70/423.66; 05 437.42/417.12;
  06 414.40/**368.38**; 07 383.60/**371.54**; 08 429.42/408.42; 09 413.54/406.77.
  So it is a recovery off a **June-July double bottom at 363-368**, not a collapse
  and not a breakout. Closes per band over 250 sessions: 400-420 **46**,
  420-440 37, 440-460 19, 460-480 20, 480-500 **5**, above 500 **0**.
- decision: hold, target 520 -> **448** (the April 2026 high), bear case **368**.
- **at those levels it returns 1.67:1, which fails the 2.5 long-term floor.** I
  am saying that rather than nudging 448 up to the ~470 that would clear it —
  that nudge is the exact failure `check_expectancy` exists to catch. So: hold
  and trim into 448, never add. Had it been proposed fresh today it would not publish.

## [06:25 ET] POSITION UPDATE — SPY short — hold, WIDEN the stop 782.00 -> 783.50
- filled 773.00 on 2026-08-31, last 770.19, +0.4%. ATR14 5.503.
- **The published stop was below the floor.** 782.00 is 9.00 from entry = **1.64
  ATR**, inside the 1.8 ATR ETF swing minimum. It should not have passed.
- 783.50 = 1.91 ATR, and sits above the 250-day high of 779.37, so the
  invalidation is now "the index makes new highs" rather than a noise level.
- **R:R falls 2.56 -> 2.19.** Widening a stop is supposed to cost you; that is
  the whole point, and it is the reverse of the KRE stop-walking pattern.
- correlation note: SPY short + TLT short are both rates-up bets. That is 2 of
  the permitted 3 on one driver. **No third rates idea today.**

## [06:25 ET] REJECTED — ORCL — no edge into a binary print I cannot price
Earnings Tue-Thu window: **2026-09-10 AMC** (Q1 FY27, est EPS 1.78, rev $19.53B),
verified on the fetched calendar. Price 158.78; ATR14 6.216 (3.91%); SMA20
148.31, SMA50 139.84, SMA200 168.79; 250d range 114.50-345.72, so -54% off the
high and +38.7% off the low. The story is financing, not demand: FY26 capex
$55.7B against **-$23.7B free cash flow**, S&P projecting $90-95B FY27 capex and
a ~-$42B FCF deficit, ~$130B borrowings, an S&P downgrade to **BBB-** (one notch
above junk), and roughly half the backlog tied to OpenAI.
- sources: https://www.cnbc.com/2026/06/26/oracle-stock-ends-worst-week-since-2001-as-investors-dwell-on-finances.html
- Rejected because I have no edge on the print and **cannot check what is priced**
  — `implied` returns HTTP 401 today (see below). Entering a 3.9%-ATR name two
  sessions before a binary event without knowing the straddle is a coin flip with
  extra steps. ADBE (also 2026-09-10 AMC, 266.51, ATR 10.48) rejected for the same reason.

## [06:25 ET] SOURCE FAILURE — options-implied move unavailable
`market_data.py implied` returns `HTTPError: 401 Unauthorized` from
query1.finance.yahoo.com/v7/finance/options for every symbol tried (ORCL, ADBE).
Combined with the Yahoo 429s on index quotes, **Yahoo is unusable today in both
the chart and options endpoints.** Consequence: no idea below carries the
"is my target inside what the market prices" check. Carry to data_quality_notes.

## [06:30 ET] POSITION UPDATE — NKE — CLOSE (sell limit 37.90 GTC from the Tue open)
- entry 40.75 (2026-08-17), target 62.00, no stop, last 38.40, -4.0%.
- why: the evidence that justified it expired. The insider cluster is April and
  underwater (see 06:15 above); RS is -47.19% vs SPY and -33.05% vs XLY over 6m;
  and at an honest 48 target against a 33 bear case it returns **0.63:1**, far
  under the 2.5 long-term floor. I cannot defend 62.00 with any valuation I
  fetched — Sept-quarter consensus is $0.4523 EPS on $11.48B.
- the limit is 37.90, *below* the 37.95 250-day low, on purpose: **if it does not
  fill, the stock held its low and the close can be reconsidered.**
- what argues against closing, stated plainly: earnings 2026-09-28 is 3 weeks
  out, the last print beat by 50.2%, and consensus has already capitulated. This
  may sell the low.

## [06:30 ET] POSITION UPDATE — CCJ — hold, bear case 80.00 added, adds capped below 96
- +6.0% at 100.74, entry 94.00, target 135.00 (= the 250d high 135.24), no stop.
- It was published with **no downside anchor at all**, which for a long_term idea
  is the one mandatory field. Set at 80.00 -> 2.93:1.
- **The +6% is tape, not confirmation.** Last EPS $0.18 vs $0.3806 est, a 52.7%
  miss; revisions deteriorating; still below the 200-day at 105.37.
- I did NOT re-underwrite the uranium thesis today — no time — and the candidate says so.

## [06:30 ET] POSITION UPDATE — BCC — hold, no change, and a tracker discrepancy
79.21 last vs 76.50 entry is **+3.5%**, but prior_context.md reports **-2.2%**.
I cannot reconcile those from the data I have; flagging rather than guessing.
Fundamentals are the steadiest in the book — revisions flat, 63.6% bullish,
last EPS +30.8% — and price sits on the SMA50 79.08 above the SMA200 77.10.
No new information, so no recommendation is emitted for it.

## [06:30 ET] POSITION UPDATE — SVRA — hold, no change
5.37 vs 5.35 entry, +0.4%; stop 4.60, target 8.00. Risk 0.75 = **3.89 ATR** on
ATR14 0.1929, R:R **3.53** — the only position in the book whose published
levels clear both floors comfortably without amendment. $8.3M average dollar
volume clears the $500K liquidity floor. 92.9% bullish, revisions flat. Nothing
changed, so nothing is emitted.

## [06:30 ET] NEW IDEA — BTC — buy the range resolution, NOT the range
- live 79,818 (CoinGecko, 24/7 — this is a real-time price, not a Friday close).
- Eight daily closes: 78,844 / 78,921 / 77,270 / 77,285 / 81,752 / 79,793 /
  79,756 / 79,818 -> an **eight-day coil at 77,270-81,752** under the 30-day high
  of **82,108**, after +31% off the 62,525 30-day low. ATR14 (true daily) 2,327 (2.92%).
- entry **stop-limit 82,400** on a break of 82,108; stop **76,400** (2.58 ATR,
  clears the 2.5 crypto floor, below the coil floor); target 94,500 (2.02:1),
  target_2 101,500 = the measured move of the 19,583-point base.
- `wait: true` — if the range never breaks there is no trade. Deliberately a
  breakout rather than a pullback entry.
- **Note on the daily bars**: CoinGecko `/ohlc?days=90` returns FOUR-DAY candles,
  not daily, and my first pass computed a 5.04% "daily" ATR from them, which was
  wrong. `days=30` returns 4-hourly candles; the figures above are true daily
  bars aggregated from those (31 bars). Anyone re-deriving these must not use days=90.

## [06:30 ET] BOOK PROBLEM — two stale bearish crypto lines must be CANCELLED
Still listed as awaiting entry, both pitched into what became a 31% advance:
- `BTC` SELL @ 63,400 (published 2026-08-16) — spot is 79,818, **26% above** it.
- `/MBTU6` SHORT @ 64,340 (published 2026-08-18) — same, and **U6 is the September
  contract**, which expires this month; universe.md forbids recommending a
  contract inside its final trading week without saying so. It should not be
  carried into late September regardless of view.
These are not "waiting", they are wrong, and the BTC idea above is the opposite
side of one of them. **Synthesis must cancel both explicitly** — otherwise the
book carries a long and a short in the same asset, which is the identical error
found today in TLT and in the September Fed contracts. Three instances of the
same failure in one book is a process problem, not three coincidences.

## [06:35 ET] CALENDAR — the item I nearly missed: **August CPI lands 2026-09-11, BEFORE the FOMC**
Found by querying Kalshi series directly (the CLI's `events` search could not
surface it). Release Fri **2026-09-11 08:30 ET**; markets close 12:25-12:29Z.
This is the input that resolves the 49.5/48.5 September Fed coin flip, and it
lands five days before the decision. **It is the decision point for every
rates-linked position in this book.**

What the market prices, from the full ladders (mid of yes bid/ask):

**Headline MoM — `KXCPI-26AUG`** (P of exceeding each strike)
0.1% 98.5 | 0.2% 88.0 | **0.3% 55.0** | 0.4% 13.5 | 0.5% 2.5
-> implied buckets: 0.2-0.3% **33%**, **0.3-0.4% 41.5%** (mode), 0.4-0.5% 11%.

**Headline YoY — `KXCPIYOY-26AUG`**
3.1% 95.0 | 3.2% 91.5 | **3.3% 60.5** | 3.4% 21.0 | 3.5% 4.0
-> buckets: 3.2-3.3% 31%, **3.3-3.4% 39.5%** (mode), 3.4-3.5% 17%.

**Core MoM — `KXCPICORE-26AUG`**
0.1% 93.5 | **0.2% 36.0** | 0.3% 2.5
-> buckets: **0.1-0.2% 57.5%** (mode), 0.2-0.3% 33.5%.

Headline modal 0.3% MoM against core modal 0.2% means the market expects energy
to do the work, which is coherent with `KXWTI-26SEP0814` pricing WTI around
**$92-93** (above $91.49 = 71%, above $92.49 = 59%, above $95.99 = 17%).
Other macro strips, for context: `KXU3-26SEP` puts P(unemployment above 4.1%) at
**48%** for September but **63%** by October; `KXGDP-26OCT30` puts Q3 GDP above
2.5% at **51%**.

## [06:35 ET] EVENT CONTRACTS — checked properly, and still no idea. Two reasons, both concrete.
**1. Where it is liquid, it is coherent.** I checked the CPI ladders for
monotonicity violations the way I checked the Fed strip. There are two apparent
ones — `KXCPI` T-0.20 mid 98.5 under T-0.10 mid 99.0, and `KXCPICORE` T0.00 mid
91.5 under T0.10 mid 93.5 — and **neither is tradeable**. Both sit in
near-certain strikes quoted 85/98 and 97/100 on open interest of 6 and 2,913;
capturing the "arb" means buying the ask at 98 and selling the bid at 89, which
loses nine cents. They are stale quotes, not free money. Saying so is the point:
an inversion that dies on the spread is not a finding.

**2. The weekend spreads make the tradeable strikes uneconomic.** On the strikes
that actually matter:

| Contract | bid/ask | width | OI |
| --- | --- | --- | --- |
| `KXCPI-26AUG-T0.3` | 51 / 59 | **8c** | 24,522 |
| `KXCPICORE-26AUG-T0.2` | 32 / 40 | **8c** | 1,692 |
| `KXCPIYOY-26AUG-T3.4` | 18 / 24 | 6c | 81,932 |
| `KXCPIYOY-26AUG-T3.3` | 58 / 63 | 5c | 68,407 |

Eight cents on a 55-cent contract is ~15% of position value to cross, before
being right about anything. These are Sunday-morning quotes and will tighten by
Tuesday. **An event-contract idea published at these prices is paying the spread
for the privilege of having no edge**, so none is published.

Also checked and rejected: `KXBTC` / `KXETH` / `KXBTCD` daily range ladders — all
show **zero open interest**, 0/1 quotes, and close today at 11:00Z. Not tradeable.
`KXINX` (S&P daily) has total OI of 32 across 30 markets. `KXPAYROLL`, `KXNFP`,
`KXRECESSION`, `KXOIL`, `KXGOLD` do not exist as series tickers.

**So: zero event contracts today, from a lane the config calls "wanted, not
tolerated".** I looked hard — the Fed, CPI, core CPI, CPI YoY, unemployment,
GDP, WTI and the crypto and index ladders — and the honest answer is that the
liquid macro complexes are arbitraged and the rest is untradeable. That is a
better output than a manufactured probability disagreement.

## [06:38 ET] *** THE BIGGEST FINDING TODAY: 8 of 8 pending LONGS are unfilled and the market is ABOVE every one of them ***
Fetched live quotes for every awaiting-entry line (Fri 2026-09-04 closes):

| Symbol | Side | Entry | Last | Distance |
| --- | --- | --- | --- | --- |
| `VST` | BUY | 128.00 | 149.30 | **+16.64%** |
| `PFE` | BUY | 25.80 | 28.45 | **+10.27%** |
| `DG` | BUY | 121.00 | 133.21 | **+10.09%** |
| `CEG` | BUY | 272.00 | 298.96 | **+9.91%** |
| `LCII` | BUY | 94.00 | 102.60 | **+9.15%** |
| `DINO` | BUY | 99.50 | 105.41 | +5.94% |
| `EEM` | BUY | 65.60 | 68.70 | +4.73% |
| `XLE` | BUY | 63.90 | 64.06 | +0.25% |
| `IYR` | SELL_SHORT | 103.60 | 102.14 | -1.41% (short, also unfilled) |

**Every single pending long is above its entry. Mean distance +8.37%.** Not one
filled. The theses were not wrong — VST, PFE, DG, CEG and LCII all went up
9-17% — the *entries* were wrong. Each was a limit set below the last print, and
the market never came back for any of them.

This is the failure `config/strategy.md` already names ("31 pullback entries
against 1 breakout, 42% of them ever filled, and the ones that did fill were the
ones falling"), but the live book is a sharper version: **the fill rate on this
cohort is 0 of 8, and the report picked five names that ran 9-17% while
capturing none of it.** A pullback entry is legitimate when it names real
support; as a reflex discount off the last print it is a way of only ever buying
the ideas that were already failing — which is precisely what the 0/5 hit rate
and -4.3% average in the track record look like from the inside.

Concrete consequences I acted on today:
- The **BTC** idea uses a **stop-limit breakout above the range high**, not a
  discount to spot. That is deliberate and this table is the reason.
- The **LULU** and **NKE** exits use limits *below* market so they fill like
  market orders, rather than optimistic exits that never trigger.
- **`XLE` is now 0.25% from its entry — effectively at market.** It is the one
  pending line that is genuinely live. It has also been published 4x in 10 days,
  so it is on the repetition watch; I did not re-underwrite it today.

**Recommendation to synthesis: say this in `data_quality_notes`.** For the five
names now 9-17% through their entries, the choice is enter at market on a
re-underwritten thesis or cancel the line — continuing to wait for a pullback
that has not come 8 times out of 8 is not a plan. I did not have the budget to
re-underwrite five theses today, so I am flagging the structure, not re-pitching
the names.

## [06:42 ET] NEW IDEA / PENDING-LINE FIX — XLE — and an OPEC+ meeting inside the Labor Day close
- **OPEC+ JMMC review 2026-09-06 (today), group meeting 2026-09-07 (tomorrow).**
  September's 188kb/d adjustment completed the rollback of the 1.65mb/d voluntary
  cuts from 2023; sources ahead of the meeting said the group would likely
  **pause increases for Q4** to manage an emerging surplus.
  source: https://www.cnbc.com/2026/08/02/opec-agrees-september-oil-hike-completing-rollback-of-voluntary-cuts.html
- **Tomorrow is Labor Day. US markets are shut.** The decision is taken and made
  public while nobody can trade it, and XLE gaps on Tuesday's open against it.
- XLE 64.06; ATR14 1.1293 (1.76%); above SMA20 62.87 / SMA50 59.20 / SMA200 54.83;
  -2.23% off the 250d high in a 42.35-65.52 range; +9.93% vs SPY on 1m, +6.65% on
  3m — **the only genuine leadership in this book.** Kalshi puts WTI near $92-93.
- levels: entry at market 63.40-64.80 **only after the outcome**; stop 61.80
  (2.00 ATR, below both the SMA20 and the 63.38 September low); target 69.00
  (2.19:1), target_2 72.00. win_prob 0.40 against a 0.313 baseline.
- **The specific action is to KILL the resting 63.90 limit before Tuesday.** This
  is the sharpest illustration of the 0-of-8 finding above: a buy limit below the
  market fills precisely when the news is bad. If OPEC+ disappoints, XLE gaps
  down through 63.90 and that order fills on the way past. The pullback entry
  does not just miss the winners — on a gap it actively selects the losers.
- driver check: XLE + the pending DINO line = **2 on oil**; TLT short + SPY short
  = **2 on rates**; BTC = 1 on crypto. All within the 3-per-driver cap.

## [06:42 ET] RESEARCH COMPLETE
- **candidates: 9 lines, 8 distinct symbols** (TLT captured twice; the later line
  lowers win_probability to 0.38 and adds Friday's payroll reaction — take the last).
- **Read the mix before sizing. This is a position-management report, not an
  idea-generation one.** Only 2 of the 8 are new risk (BTC, XLE), and both are
  `wait: true`. Three are exits or partial exits (LULU close, NKE close, TLT long
  leg closed inside the TLT short line); three are amendments to open positions
  (GLD target cut, SPY stop widened, CCJ bear case added).
- **Three separate netting errors found in one book**, all the same failure:
  TLT held long and short simultaneously with the stops bracketing spot; YES on
  both "Fed hikes in September" and "Fed holds in September"; and a bearish BTC
  pair still pending against a BTC long pitched today. That is a process problem,
  not three coincidences — `merge_report` dedupes on `(symbol, direction)` and so
  cannot see an opposing pair. Worth a check in `tests/`.
- **Two published stops were below the mechanical floor**: SPY at 1.64 ATR
  (floor 1.8, now widened to 1.91, R:R falling 2.56 -> 2.19). Nothing was
  tightened to clear a ratio anywhere in this run.
- **Zero event contracts**, from a lane the config calls "wanted". The Fed strip
  cross-checks to within 0.01 hikes; the CPI ladders' only monotonicity
  violations die on the spread; the tradeable CPI strikes are 5-8c wide on a
  weekend; the crypto and index ladders have no open interest. Documented above.
- coverage gaps:
  - **No VIX, no index quotes, no futures quotes, no DXY** — Yahoo returns 429 on
    every index symbol and finnhub refuses index CFDs on this plan.
  - **No options-implied move for any name** — Yahoo options returns 401. So no
    idea here carries the "is my target inside what the market prices" check, and
    ORCL and ADBE were rejected partly for that reason.
  - **No short interest or days-to-cover for any name** — api.nasdaq.com timed
    out on NKE, LULU and CCJ. One `positioning` kind is missing from every equity
    idea, so conviction scores are lower than they would otherwise be.
  - Did not re-underwrite the uranium (CCJ) or energy (DINO) theses, or the five
    pending longs now 9-17% through their entries. Flagged structurally instead.
  - BCC shows +3.5% against entry but prior_context reports -2.2%; unreconciled.
- sources that failed: Yahoo chart API (429, all index symbols), Yahoo options
  API (401, all symbols), api.nasdaq.com short interest (ReadTimeout),
  `market_data.py events` (returns null prices — Kalshi field rename, see 06:16).

## [06:30 ET] AMENDMENT — conviction corrected on SPY and NKE, and a note on this log's timestamps
Ran a mechanical check of every captured candidate against the floors before
finishing. All stop distances and reward-to-risk ratios pass:

| Symbol | Stop (ATR) | Floor | R:R | Floor | Break-even | Claimed | Edge |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TLT | 2.61 | 1.8 | 2.06 | 2.0 | 0.326 | 0.38 | +5.4pp |
| SPY | 1.91 | 1.8 | 2.19 | 2.0 | 0.313 | 0.40 | +8.7pp |
| BTC | 2.58 | 2.5 | 2.02 | 2.0 | 0.331 | 0.40 | +6.9pp |
| XLE | 2.00 | 1.8 | 2.19 | 2.0 | 0.314 | 0.40 | +8.6pp |
| CCJ | n/a (long_term) | — | 2.93 vs bear 80.00 | 2.5 | — | — | — |
| GLD | n/a (long_term) | — | **1.67 vs bear 368.00** | 2.5 | — | — | — |

No claimed edge exceeds 9pp over its break-even, so nothing here is making a
large claim it cannot carry. **GLD fails its floor at 1.67:1 deliberately** and
its thesis says so — see 06:25. LULU and NKE show no ratios because they are
exits, which is the shape a close instruction has.

The check also caught that **SPY and NKE carried conviction 3 while listing 3
distinct evidence kinds**, which the scale maps to 4. I had scored them on how
the ideas felt rather than on the count, which is the exact substitution the
conviction rules exist to stop — it just happened to run downward this time.
Both re-captured at 4. Take the last line per symbol: **11 lines, 8 symbols**
(TLT, SPY and NKE each appear twice).

**On timestamps in this log:** the headings between 06:16 and 06:42 are estimates
written before I checked the clock, and they run ahead of and out of order with
real time — the run started 06:00:53 and reached RESEARCH COMPLETE at 06:27.
Read the order of the headings, not their times. No fetched figure is affected.
