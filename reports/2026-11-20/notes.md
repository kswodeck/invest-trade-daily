# Research log — 2026-11-20

## [06:02 ET] PRIOR CONTEXT — read, and it changes the bar today

Track record is now **44 closed trades** — past the ~15 noise threshold in
`config/strategy.md`, so it is signal and must move the bar rather than be
waved off.

- Overall 5/44 hit target (11%), avg **-5.5%**
- `stock` 2/30 (7%), avg **-7.1%** — the worst lane and the most-used one
- `etf` 3/14 (21%), avg -1.9% — the least-bad lane
- `long_term` 0/4, avg -15.2%
- conviction 2: 0/6, avg -8.4%. conviction 4: 2/9, avg -0.4%

Pattern, stated plainly: this report has been running a book of long-only
pullback entries in single-name equities and losing money at it slowly and
consistently. 18 open positions is also a large book for one account, and
almost every one is a `BUY`.

**Bar for today, in consequence:**
1. A new single-name long needs more than a clean chart. Conviction 4 (three
   distinct evidence kinds) or it does not publish.
2. No new conviction-2 single-name equity longs. 0/6 is enough.
3. Prefer ETFs, futures and event contracts, where the record is not yet damning
   and where the instrument matches the view (per `config/universe.md`).
4. Position management on the 18 open rows is the first job, not the last.

## [06:08 ET] MACRO — yesterday was a key reversal day, and everything fell together

All prices are the **2026-11-19 close** (fetched 11-20 06:01 ET, age ~842 min,
session `pre`). At 6am ET the previous close is the freshest honest equity
price, not stale data.

| ETF | Open | High | Close | Prev close | Day % | High→close |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 737.46 | 739.90 | **715.87** | 730.20 | -1.96% | **-3.25%** |
| QQQ | 671.09 | 676.49 | **645.04** | 659.51 | -2.19% | **-4.65%** |
| SMH | 473.05 | 479.96 | **447.48** | 459.54 | -2.62% | **-6.77%** |
| IWM | 271.08 | 271.80 | **264.22** | 270.12 | -2.18% | -2.79% |
| GLD | 339.88 | 340.52 | **335.18** | 341.19 | -1.76% | -1.57% |
| XLV | 180.40 | 181.25 | **177.46** | 181.17 | -2.05% | -2.09% |
| XLP | 90.05 | 90.17 | **89.86** | 91.18 | -1.45% | -0.34% |
| XLU | 43.33 | 43.44 | **43.01** | 43.55 | -1.24% | -0.99% |
| XLE | 61.71 | 61.94 | **60.89** | 61.29 | -0.65% | -1.70% |
| TLT | 80.08 | 80.45 | **80.35** | 80.22 | +0.16% | -0.12% |

Source: `scripts/market_data.py quote` (finnhub). Two facts matter more than the
percentages:

1. **Every index closed at or within a tick of its session low** (SPY low
   715.65 / close 715.87; QQQ 644.34 / 645.04; SMH 447.20 / 447.48; IWM 263.74 /
   264.22). A close on the low after a gap-up open is distribution, not a dip.
2. **Semis gapped up ~2.9% and finished -2.6%** — a 6.8% high-to-close
   round trip. That is the shape of good news being sold, which is a different
   and worse signal than bad news being sold.

And the breadth of it: **gold, staples and utilities all fell with the tape.**
A rotation has somewhere to rotate into. Nothing was green except TLT at
+0.16%. That is de-grossing / margin-driven liquidation, where correlations go
to one and defensives are sold because they are liquid, not because they are
disliked.

Rates (FRED, as of 2026-11-18):
- US10Y **5.07%**, US2Y **4.80%**, fed funds **3.88%**, 2s10s **+0.28**
- Unemployment 4.1% (Oct)

The 2Y sits **92bp above the effective funds rate**. That is not a market
pricing cuts — it is a market pricing the next move as a hike, with a 10Y at
5.07% to match. A 5% long bond is the competing asset for every equity
multiple on the page, and it is the cleanest single explanation for why a
semis beat could not hold a gap.

Regime call for today: **risk-reduction tape, rates-driven, with a confirmed
reversal bar.** That argues against adding single-name long beta, which is
exactly what this report's 2/30 stock record has been doing.

## [06:08 ET] DATA GAPS — Yahoo is rate-limited this run
- `^GSPC`, `^NDX`, `^DJI`, `^RUT`, `^VIX`, ES/NQ futures, DXY, 10Y quote, gold
  and WTI futures quotes **all failed**: finnhub refuses indices without a CFD
  subscription, Yahoo returned **HTTP 429 on every call**, stooq 404s on
  `^`-prefixed symbols, no AlphaVantage key.
- Consequence: **no VIX level and no overnight futures print this run.** I
  cannot say where the tape is trading at 6am, only where it closed. Every
  index read below is from the ETF proxies, which are cash-session only.
- CoinGecko `prices` also failed on the macro call — retrying separately.

## [06:12 ET] LEVELS — the indices are at the lows, not at the highs

From `market_data.py history --days 150` (nasdaq source, daily bars):

| | Close | 20dma | 50dma | 150d range | Off high | Off low | ATR14 | ATR% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 715.87 | 751.32 | 761.67 | 702.28–781.62 | **-8.4%** | +1.9% | 14.70 | 2.05% |
| QQQ | 645.04 | 683.33 | 713.09 | 642.21–762.86 | **-15.4%** | +0.4% | 19.73 | 3.06% |
| IWM | 264.22 | 277.18 | 278.91 | 263.74–305.18 | **-13.4%** | +0.2% | 5.91 | 2.24% |

This reframes the reversal bar. Yesterday was **not** a top being made — the
correction is already well advanced and yesterday's gap-up was a failed bounce
inside it. All three sit below a declining 20dma and 50dma.

Structure differs by index, and the difference is the trade:

- **SPY broke down.** The Nov 5–18 range floor was 726.80 (Nov 18 low) with the
  Nov 5 low at 732.71. The Nov 19 close of 715.87 is cleanly through both. Next
  real support is the 702.28 range low.
- **QQQ is sitting ON support, not through it.** Lows of 647.05 (Nov 5), 646.64
  (Nov 17), 644.34 (Nov 19) are a triple test of a 644–647 shelf, with the 150d
  low at 642.21 just beneath. **This is where a short gets hurt** — I will not
  initiate a Nasdaq short into a thrice-defended shelf two points away.
- **IWM is making new lows.** 270.52 → 267.87 → 263.74 is an unbroken
  lower-low sequence and yesterday printed the 150-day low itself. This is the
  only one of the three with no support beneath it.

So the bearish index expression is the Russell, and I am already short it.

## [06:18 ET] POSITION UPDATE — IWM — opened 2026-11-18 @ 270.50, now 264.22 (+2.3%)
- decision: **HOLD, levels unchanged.** Target 238.69, stop 284.50.
- why: the breakdown to a new 150-day low is the thesis confirming. The stop
  sits above the Nov 11 swing high of 283.72, and that structural level has not
  moved — walking it in to 278 would improve the printed ratio while making the
  trade strictly worse, which is the exact KRE failure `CLAUDE.md` names.
- R:R 2.27 from entry, stop 2.37 ATR (etf floor 1.8). win_prob 0.42 vs a 0.306
  break-even baseline.
- action: captured via add_candidate.py. **Candidate #1 — minute-20 deadline met.**

## [06:24 ET] POSITION BOOK — refetched, and prior_context was a day stale

`prior_context.md` carries 2026-11-18 closes. Refetched every open row at the
2026-11-19 close. **Two rows changed status materially and one is gone.**

| Symbol | Entry | Stop | 11-19 close | Day low | % vs entry | Dist to stop |
| --- | --- | --- | --- | --- | --- | --- |
| `BCC` | 76.50 | 64.50 | 64.38 | **63.96** | -15.8% | **BREACHED** |
| `ONON` | 34.20 | 30.69 | 30.82 | **30.705** | -9.9% | **+0.4%** |
| `DKS` | 144.50 | 129.00 | 136.14 | 136.01 | -5.8% | +5.2% |
| `RTX` | 199.00 | 186.00 | 193.44 | 192.87 | -2.8% | +3.8% |
| `ADM` | 68.80 | 64.40 | 67.13 | 66.90 | -2.4% | +4.1% |
| `PFE` | 27.60 | none | 27.54 | 27.44 | -0.2% | n/a |
| `HUN` | 9.00 | 8.09 | 8.97 | 8.815 | -0.3% | +9.8% |
| `PYPL` | 56.50 | 54.10 | 56.37 | 56.25 | -0.2% | +4.0% |
| `OXY` | 54.00 | 50.15 | 53.81 | 53.26 | -0.4% | +6.8% |
| `UNP` | 288.60 | 277.40 | 290.63 | 289.665 | +0.7% | +4.6% |
| `ABT` | 103.00 | 97.00 | 103.87 | 103.61 | +0.8% | +6.6% |
| `TLT` | 80.30 | 78.80 | 80.35 | 79.81 | +0.1% | +1.9% |
| `CAG` | 14.40 | none | 14.68 | 14.24 | +1.9% | n/a |
| `XLV` | 184.00 | 176.00 | 177.46 | 176.96 | -3.6% | **+0.8%** |
| `XLU` | 43.30 | 41.80 | 43.01 | 42.75 | -0.7% | +2.8% |
| `HII` | 262.00 | none | 286.56 | 282.35 | +9.4% | n/a |
| `KHC` | 23.00 | 21.20 | 24.92 | 24.73 | +8.3% | +14.9% |
| `IWM` short | 270.50 | 284.50 | 264.22 | 263.74 | +2.3% | +7.7% |

**`BCC` stopped out on 2026-11-19.** Low 63.96 against a 64.50 stop — the
position closed intraday yesterday at the stop. It is not a live row and I am
not re-pitching it. It was published twice in the last ten days per
`prior_context.md`, and the second pitch bought more of a name that was already
-15% against the first. That is the anchoring the repetition guard exists for,
and it cost the full 12-point risk.

**`XLV` is 0.8% above its stop** (176.96 low vs a 176.00 stop) having been
opened only 2026-11-09 at 184.00. **`ONON` is 0.4% above its stop** (30.705 low
vs 30.69) — it missed stopping out by one and a half cents.

The whole book is long except `IWM`, and 13 of 18 rows are below entry on a day
when the only green close in the market was `TLT`. That is one position, held
eighteen times.

## [06:25 ET] CLOSED — BCC — stopped 2026-11-19 at 64.50 (entry 76.50, -15.7%)
- No candidate emitted. The row is closed; grading picks it up from the bar.

## [06:30 ET] MACRO — the regime is a Fed HIKING cycle. This explains the whole tape.

This is the single most important finding of the run and it reframes every idea
below. I had inferred it from the curve before finding it confirmed in news.

- The Fed **raised rates in September 2026 — its first hike in three years** —
  and has kept signalling more. The 10Y crossed 5% in mid-September for the
  first time since 2023.
  — source: https://www.fxstreet.com/news/us-10-year-yield-crosses-5-rubicon-as-fed-hike-looks-locked-202609141440
- Target range is **3.75%–4.00%** after a hold on October 28. Matches the 3.88%
  effective funds rate from FRED.
  — source: https://kalshi.com/economics/fed-rate-odds
- **Next FOMC is December 8–9, 2026, decision 14:00 ET on Dec 9.** Then
  January 26–27 and March 16–17.
  — source: https://pro.thestreet.com/stock-market-today/feds-musalem-wants-several-hikes-before-spring-but-note-his-record
- **St. Louis Fed's Musalem, Buenos Aires, Tuesday 2026-11-17**: the economy
  will likely need "several interest rate increases before the spring of 2027",
  starting "soon". He wants the **real** funds rate "solidly between 2% and
  2.5%" by spring, up from "the lower end of the 1% to 1.5% range". Caveat the
  article itself makes: he does not vote until 2028 and pivoted off a hawkish
  call in 2024. — same source
- Futures price quarter-point hikes at **both December and January** plus one
  more by June. CME FedWatch after the Oct CPI print on 2026-11-10 had a 25bp
  December hike at **85–89%** and a 50bp at **11–15%**.
  — source: https://www.regardsofwallstreet.com/news/december-2026-fed-meeting-dates-hike-odds
- NVDA reported (its first report without Huang), beat, and **raised FY28
  revenue growth guidance to 75%** — and the tape sold it anyway. Coverage
  frames the beat as "not enough to ease worries about AI spending".
  — source: https://pro.thestreet.com/stock-market-today/nvidia-clears-the-bar-in-its-first-report-without-huang

**Why this ties the whole day together.** A single driver accounts for every
number in the 06:08 table: a Fed tightening into re-accelerating inflation
lifts the discount rate, which (a) compresses the multiple on the longest-duration
equity — hence semis giving back a 4.4% gap on a *raised* guide, (b) raises the
refinancing cost of the most levered cohort — hence IWM making new lows, and
(c) raises real rates, which is the one thing that reliably sells **gold**, the
otherwise inexplicable -1.76% in an everything-down session.

So yesterday was not an AI-sentiment wobble. It was a discount-rate repricing,
and the 2Y sitting 92bp above effective funds says it is not finished.

**Consequence for this report: the December 9 FOMC is the dominant dated
catalyst in the market, and a 25bp hike is already 85–91% priced.** Being long
that outcome is not an edge. The edge, if there is one, is in the *size* of the
move or in what is still mispriced relative to a 5% long bond.

### What I will NOT do with this
Lean the whole report short. Four reasons it would be wrong:
1. QQQ is two points above a thrice-defended 644–647 shelf (06:12 note).
2. A 25bp December hike is priced, so the bearish catalyst is largely in.
3. `config/strategy.md` caps same-driver ideas at **3**, and "the Fed is
   hiking" would be the driver of all of them.
4. Positioning is already one-sided short in the one index with no support
   beneath it (IWM), which is the correct single expression.

## [06:36 ET] LEVELS — ATR against stop distance on every row needing a decision

| Symbol | Close | ATR14 | ATR% | Stop | Stop dist from *price* | Stop from *entry* | 50dma |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DKS` | 136.14 | 6.63 | **4.87%** | 129.00 | **1.08 ATR** | 2.34 ATR | 138.24 |
| `ONON` | 30.82 | 1.81 | **5.88%** | 30.69 | **0.07 ATR** | 1.94 ATR | 32.54 |
| `XLV` | 177.46 | 3.76 | 2.12% | 176.00 | 0.39 ATR | 2.13 ATR | **176.26** |
| `TLT` | 80.35 | 0.73 | 0.91% | 78.80 | 2.12 ATR | 2.05 ATR | 80.06 |

## [06:38 ET] REJECTED — XLE / energy — the relative-strength idea is false
Yesterday's -0.65% against SPY's -1.96% looked like leadership. It is not.
`relstrength XLE --peer SPY`: XLE **-10.67% over 1m** against SPY -7.40% —
**underperforming by 3.27%**. Price 60.89 is below both the 20dma (65.06) and
50dma (64.79) and 13.2% off its 150-day high, down from 70.15 on 2026-11-02.
One day of smaller losses in a correlated selloff is not relative strength, and
I would have published a long on it. Dropped.

Worth flagging against the open book: **`OXY` is a long in this sector.** It is
+6.8% clear of its stop so no action is forced, but it is not the defensive
holding the lower daily beta makes it look like.

Also from that call: **SPY is -7.40% over one month.** This is a broad
correction, not a semis event.

## [06:40 ET] AWAITING-ENTRY REVIEW — three of the four levels are dead
These were published and never filled. Re-checked against the 2026-11-19 close,
and the result is a pattern worth naming, not four isolated misses:

| Idea | Published | Entry | Now | Entry is |
| --- | --- | --- | --- | --- |
| `GLD` SELL | 2026-10-25 | 406.77 | 335.18 | **21.4% above market** |
| `/MBTZ6` SHORT | 2026-11-09 | 74,075 | 61,921 (BTC) | **19.6% above market** |
| `CVS` BUY | 2026-11-05 | 77.50 | 80.04 | 3.2% below market |
| `LEN` BUY | 2026-11-13 | 79.50 | 79.93 (low 79.685) | **about to fill** |

The two short ideas were **right about direction and made nothing**, because
both asked the market to rally into the entry first. GLD fell 17.6% and BTC
fell 16.4% from where those shorts were set, with neither ever filling. That is
the mirror image of the pullback-entry problem `config/strategy.md` names in
the level-setting section — an entry placed on the wrong side of the market
selects for the ideas that were already failing, in both directions.

`LEN` is the urgent one: it is a homebuilder about to fill a long **0.3% away**,
into a Fed signalling several more hikes with the 10Y at 5.07%. Filling that
order is taking the single worst-positioned long in the book for this regime.
Retiring it is an action, and today is the last day the action is available.

## [06:58 ET] POSITION UPDATE — DKS — opened 2026-11-13 @ 144.50, now 136.14 (-5.8%)
- decision: **CLOSE before Monday's print.**
- why: Q3 earnings 2026-11-23 (fetched calendar). ATR 6.63 = **4.87% of price**,
  so the 129.00 stop is 1.08 ATR away and an earnings gap opens straight
  through it. A stop the event jumps over is not risk control. And the
  remaining trade is not the published one: +28.9% to target against -5.2% to
  stop is ~20% honest win probability against a 33% break-even at 2.0:1.
- action: captured. Expect `check_expectancy` to FAIL this — correctly. The flag
  is the argument for closing, not an error to tune away.

## [07:00 ET] POSITION UPDATE — ONON — opened 2026-11-03 @ 34.20, now 30.82 (-9.9%)
- decision: **CLOSE at the open.**
- why: the 2026-11-19 low of 30.705 is **1.5 cents** above the 30.69 stop —
  0.07 ATR on a 5.88%-ATR instrument. That is not a position, it is a coin flip
  on the opening tick, and every index closed at its session low so the
  gap-weighted opening price sits below the stop rather than at it.
- action: captured.

## [07:02 ET] CORRECTION — LEN — I was wrong at 06:40. Do NOT cancel.
I flagged the resting 79.50 LEN long for retirement on the grounds that a
homebuilder is the worst-positioned long for a hiking cycle. **That reasoning
is backwards and I am reversing it.**

Pulling the 2026-11-13 record: LEN was published as a **conviction-5
`long_term`** idea with `stop: null`, a 108.50 target at **1.20x book value**,
a bear case at 68.00, and an accumulation plan of thirds at 84.00 / 81.00 /
77.50 plus a fourth under 72.00 — explicitly the 77.12–81.90 band **Berkshire
bought in on 2026-10-02**.

Two things follow:
1. A sub-book price in a quality builder is **produced by** the rate cycle. High
   rates are the mechanism of the discount, not a refutation of it. Cancelling
   on "rates are high" overrides a valuation thesis with a macro view.
2. `config/strategy.md` says a long-term idea legitimately repeats while
   accumulation is unfinished, and the plan was already built to absorb this —
   there are two tranches below the current price by design.
- decision: **HOLD the order, level unchanged at 79.50.** The 11-19 low of
  79.685 is 0.2% away, so the second third should fill today.
- Captured at conviction **4**, not the original 5: I can evidence
  valuation_anchor, positioning (the 13F) and technical_level — three distinct
  kinds — but not a fourth, so 5 was not supported.

The GLD / `/MBTZ6` conclusions at 06:40 stand and are unaffected: those are
swing shorts whose entries are 21.4% and 19.6% **above** the market with no
valuation anchor underneath. Cancel both.

## [06:13 ET] CORRECTION — the timestamps above are wrong, and I have 47 minutes left
I estimated elapsed time instead of calling `date`, which the skill explicitly
warns against. Real clock on calling it: **06:13 ET**, 13 minutes into a ~60
minute budget — not the 07:02 the heading above claims.

Every heading from `[06:02]` to `[07:02]` is **inflated by up to 49 minutes**.
Their ORDER is correct and their content is unaffected; only the absolute
labels are wrong. True span of everything above: 06:00–06:13 ET. Left in place
rather than rewritten, because a fabricated-looking fix to a timestamp record
is worse than a labelled error.

**All timestamps from here down are read from `date`.** The practical
consequence is that I stopped researching at what I thought was 70% of budget
and was actually at 22%, so the four candidates captured so far are the
position-management core and there is real time for the hunting the day still
needs.

## [06:25 ET] TOOLING BUG — `market_data.py events` cannot find any macro market
`events()` requests `/markets?status=open&limit=200` with **no series filter**
and then substring-filters the result in Python. The first 200 open Kalshi
markets are **all sports multi-leg parlays** (`KXMVECROSSCATEGORY-*`), every one
with `yes_bid: null`. So "Fed", "FOMC", "CPI", "inflation", "S&P", "bitcoin" and
"recession" all returned **count 0** — not because the markets are absent but
because the filter never sees them.

This is very likely why `prior_context.md` shows **event contracts with 4
tracked ideas and no closed trades**: the lane has been unreachable through the
CLI. Worth a fix outside this run — pass `series_ticker` to the API instead of
filtering client-side.

**Workaround used today:** query the series endpoint directly. Note the list
endpoint returns `yes_bid: null` for everything; prices only appear on the
**single-market** endpoint, in `*_dollars` fields.
`curl .../markets/<TICKER>` → `no_bid_dollars` / `no_ask_dollars`, and
`yes_bid = 1 - no_ask`.

## [06:22 ET] EVENT CONTRACTS — real prices, fetched per-market

**December 9 FOMC** (`KXFEDDECISION-26DEC-*`, close 2026-12-09T18:59Z = 13:59 ET):

| Outcome | yes bid/ask | Last | Prev | Open interest |
| --- | --- | --- | --- | --- |
| Hike 25bp | **0.91 / 0.92** | 0.92 | 0.92 | 2,351,761 |
| Hike >25bp | 0.04 / 0.05 | 0.04 | **0.07** | 2,881,296 |
| Maintain | 0.04 / 0.05 | 0.05 | 0.04 | 3,726,448 |
| Cut 25bp | 0.00 / 0.01 | 0.01 | 0.01 | 915,335 |

**January 26–27 FOMC** (`KXFEDDECISION-27JAN-*`):

| Outcome | yes bid/ask | Last | Prev | OI |
| --- | --- | --- | --- | --- |
| Hike 25bp | **0.59 / 0.61** | 0.62 | 0.58 | 83,349 |
| Maintain | 0.39 / 0.40 | 0.40 | 0.40 | 71,123 |
| Hike >25bp | 0.01 / 0.03 | 0.03 | 0.02 | 36,588 |

**November CPI year-over-year** (`KXCPIYOY-26NOV-T*`, resolves on the
2026-12-10 release):

| Strike | P(above) | OI |
| --- | --- | --- |
| above 3.2% | 0.99 | 14,792 |
| above 3.4% | 0.98 | 26,268 |
| above 3.6% | **0.79** | 108,448 |
| above 3.8% | **0.12** | 83,705 |
| above 4.0% | 0.01 | 61,127 |

Read: the market puts **67% of all probability in the single 3.6–3.8% bucket**
and a modal print of **3.7%**. That is a genuinely useful macro number — CPI
near 3.7% against a 3.75–4.00% funds rate means the **real policy rate on CPI
is roughly zero**, which is the cleanest available explanation for why this Fed
is hiking rather than cutting into a 15% Nasdaq drawdown. Musalem's "real funds
rate at the lower end of 1% to 1.5%" must therefore be on core PCE, not CPI.

## [06:26 ET] REJECTED — all event contracts — no defensible probability disagreement
`config/universe.md` requires an event idea to state the market's implied
probability, my own estimate, and **why the gap exists**. I have the first and
not the second, on any of the three ladders:

- **Dec 25bp hike at 92%** — efficient on 2.35M open interest. Buying a 92c
  yes to make 8.7% is not an edge, it is a funding trade with tail risk.
- **Jan 25bp hike at 60%** — I have two *opposing* weak arguments and therefore
  no edge. For a higher number: Musalem wants "several" increases before spring
  2027, and from December the only meetings available are Dec, Jan and Mar, so
  "several" needs January. For a lower number: the Fed's revealed pattern this
  cycle is **alternating** — hiked September, held October, hiking December —
  which points at a January hold and makes 40% look about right. Two
  contradictory reads at comparable strength is the definition of no edge.
- **Nov CPI above 3.8% at 12c** — tempting, because 7.7:1 on a re-accelerating
  inflation print has the right shape, and a hiking Fed implies official
  concern about upside surprises. **I am not taking it, for a concrete reason:
  I never fetched October CPI YoY.** `market_data.py macro` returns
  `cpi_yoy: 337.476`, which is the CPI **index level**, not a year-over-year
  rate. Without the October YoY I cannot compute the base effect, cannot build
  a nowcast, and would be asserting a fat right tail from the regime narrative
  alone. A 12% probability of a ≥0.2pp upside surprise three weeks out is close
  to the historical base rate, so there is no reason to think it is wrong.

Publishing any of these would be the "feels underpriced" thesis the config
forbids. The lane was finally reachable today and the honest answer is still no.

## [06:20 ET] MACRO REFINEMENT — one month is a rotation, one day was a liquidation
My 06:08 read ("everything fell together, so this is de-grossing") is right about
**yesterday** and wrong as a description of **the month**. Both are true at
different timescales and the distinction decides whether anything is buyable.

`relstrength <sector> --peer SPY`, with SPY itself at **-7.40% over 1m**:

| Sector | 1m | 3m | 6m | vs SPY 1m | vs SPY 6m |
| --- | --- | --- | --- | --- | --- |
| **XLP** staples | **+3.16%** | +4.50% | +6.14% | **+10.56** | +9.76 |
| XLU utilities | +2.40% | +0.56% | -4.42% | +9.80 | -0.80 |
| XLRE real estate | +1.95% | -4.88% | -3.64% | +9.35 | -0.02 |
| XLY discretionary | +0.30% | -1.81% | -2.38% | +7.70 | +1.24 |
| XLF financials | -0.82% | -3.31% | **+7.44%** | +6.58 | **+11.06** |
| XLB materials | -3.70% | -7.70% | -1.20% | +3.70 | +2.42 |
| XLI industrials | -4.13% | -10.48% | -5.38% | +3.27 | -1.76 |
| **XLK tech** | **-14.77%** | -12.34% | -10.03% | **-7.37** | -6.41 |

**The entire index drawdown is tech.** Staples are *up* 3.16% in a month while
SPY fell 7.40%, and are positive on 1m, 3m and 6m. So the month is a clean
rotation out of long-duration growth into short-duration defensives — exactly
what a rising discount rate should produce — and yesterday was a liquidation
day layered on top of it, in which even the leaders were sold for being liquid.

**The book is already positioned for this rotation**: KHC, CAG, ADM, XLU, XLV,
PFE and ABT are seven defensive longs. The correct conclusion is therefore NOT
to add more of it.

## [06:21 ET] REJECTED — XLF — the relative strength is backward-looking
+6.58% vs SPY over 1m and +11.06% over 6m made this the best new-idea lead, and
it is the one sector the book has no exposure to. The daily bars kill it: XLF
has fallen **58.68 (Nov 13) → 55.58 (Nov 19), -5.3% in four sessions**, and the
2026-11-19 close is **below the 50dma of 55.925** on 57.99M shares against a
~30M average. A sector whose 1m relative number is good *because of what it did
three weeks ago* while it breaks its 50dma on expanding volume is not a buy
setup. Credit is the fundamental objection too: a bear-flattening curve
(2s10s +0.28) compresses the lending spread the hiking is supposed to widen.

## [06:22 ET] REJECTED — XLP — fails the reward-to-risk floor on arithmetic
The strongest sector in the screen, and I could not make a publishable trade of
it. Close 89.86, above a rising 50dma of 86.25, 3.87% off its 150-day high of
93.48, ATR(14) 1.65.
- The 1.8 ATR ETF stop floor demands at least 2.97 points of stop, so the
  nearest honest stop is ~86.00 (just under the 50dma) = 3.86 points of risk.
- The 2.0 swing floor then demands 7.72 points of reward = a **97.58 target**,
  which is **4.4% above the 150-day high**. Targeting the 93.48 high instead
  gives 3.62 of reward against 3.86 of risk = **0.94**, a clear fail.

So the obvious defensive trade is unavailable, and the floors are the reason —
a low-volatility sector sitting near its own range high cannot clear a 2.0
ratio without inventing upside. That is the floors working as designed and it
says the easy rotation trade is **late**, not that the rotation is wrong.

## [06:23 ET] REJECTED — QQQ long off the 644–647 shelf — fails on win probability
Tested properly rather than dismissed. The shelf is real: lows 647.05 (Nov 5),
646.64 (Nov 17), 644.34 (Nov 19), with the 150-day low at 642.21. But the 1.8
ATR floor on a 19.73 ATR means 35.5 points of stop — 609.50, far below the
shelf — and the 2.0 ratio then needs a **716 target, an 11% rally** back through
the 683 20-dma. The ratio computes to exactly 2.0, so it passes on paper and
fails on the question that matters: I do not believe QQQ reaches 716 before
609.50 at better than the 33% break-even, in a hiking cycle with XLK -14.77% in
a month. Passing the ratio while failing the probability is precisely the trap
`check_expectancy` exists for. No trade.

## [06:24 ET] REJECTED — insider buying in the de-rated semis — no cluster exists
The best available non-correlated idea would be a long in the cohort that
caused the drawdown (XLK -14.77% in a month), confirmed by insiders buying it.
`market_data.py insiders` across the obvious names:

| | open-market buys | distinct buyers |
| --- | --- | --- |
| AMD | 0 | 0 |
| MU | 0 | 0 |
| AVGO | 1 | 1 |
| QCOM | 0 | 0 |
| MRVL | 0 | 0 |
| INTC | 2 | 1 |

A single buyer is not a cluster, and the skill is explicit that several
`distinct_buyers` is what carries signal. **Nobody inside these companies is
buying this dip.** Per the skill, absence is not a negative and I am not
treating it as one — but it is not the confirmation I was looking for, so there
is no long here.

## [06:25 ET] CATALYST — the calendar gap I had left, and it matters
I had checked earnings and not economic releases. Fixing that turns up the
single most important date between now and the FOMC:

- **October core PCE — Wednesday 2026-11-25, 08:30 ET.** Also that morning: Q3
  GDP second estimate, initial jobless claims, October new home sales; Beige
  Book at 14:00 ET.
  — source: https://www.financecalendar.com/event/us-personal-income-and-outlays-pce-november-2026/
- **Thursday 2026-11-26 is Thanksgiving — market closed.** One source claimed an
  early 13:00 ET close on Nov 25; I believe the half session is normally the
  Friday *after*, so I am **not** asserting either and it should not be relied
  on for execution.
- The October employment report already landed on 2026-11-06, so there is no
  jobs print in the window.

**Why this is the key date.** November CPI does not release until
**2026-12-10** — the Kalshi `KXCPIYOY-26NOV` contracts resolve on it — which is
the **day after** the December 9 FOMC. So the Fed decides without November CPI,
and the **Nov 25 core PCE is the last major inflation reading it sees.** A 92%-priced
December hike means that print's real work is on the **January** decision, which
is the genuinely undecided one at 59-61c hike / 39-40c hold.

Execution consequence: it lands at 08:30 ET in a holiday-thinned pre-Thanksgiving
session, where gaps are larger for the same news.

## [06:26 ET] POSITION UPDATE — IWM — re-captured with the dated catalyst
The 06:18 capture had `catalyst.datetime_et: null`. It now carries the Nov 25
PCE print and the Dec 9 FOMC, which is a real gain in actionability.
- **Conviction deliberately left at 4, not raised to 5.** Adding a
  `dated_catalyst` entry would make four distinct evidence kinds and mechanically
  support a 5. I am not claiming it: the PCE print is **two-sided event risk**
  for this position, not directional evidence for it, and this report's history
  is conviction inflation (39 of its first 57 ideas scored 3). Conviction 4 is
  also its best-performing bucket (2/9, -0.4%), which is not a reason to award
  one.

## [06:27 ET] REJECTED — GLD long — gold is not bottoming, it is in free-fall
Tested because a confluence would have been genuine: if TLT is bottoming, the
rising-real-rate headwind on gold should be abating, which would make gold a
long. The bars refute it. GLD closed **335.18 at its 150-day low** (range low
335.05, 0.04% off it), **-24.84% off its 445.93 high**, and the decline is
*accelerating* — 379.53 (Nov 9) → 335.18 (Nov 19), **-11.7% in eight sessions**,
with the last two bars closing at their lows on rising volume. Price is 7.6%
below the 20dma (362.61) and 11.0% below the 50dma (376.42). No trade.

The decoupling is itself worth recording, because it **strengthens the TLT
case** rather than duplicating it: gold is -24.84% off its high and making new
lows while TLT is only -8.47% off its high and making higher lows. Rising real
rates are hitting gold hard while the nominal long end stabilises — so the TLT
idea is not a second expression of a single "rates" view, and the two are not
double-counted against the correlation cap.

## [06:28 ET] POSITION UPDATE — the remaining ten holds, no change to any level
Decided, per the skill's requirement of a decision on every open row, but
**deliberately not emitted as candidates**: nothing changed on any of them, and
ten boilerplate re-publications would be padding that crowds the real calls.

| Symbol | % vs entry | Dist to stop | Decision and reason |
| --- | --- | --- | --- |
| `KHC` | +8.3% | +14.9% | HOLD. Best row in the book and a staples name, the sector leading at +3.16% over 1m. Target 28.09 intact. |
| `HII` | +9.4% | no stop | HOLD. +9.4% and defense is budget-driven, so it is the least rate-sensitive long held. Invalidation remains a contract//budget event, not a price. |
| `PFE` | -0.2% | no stop | HOLD. Flat, healthcare, no stop by design. |
| `ABT` | +0.8% | +6.6% | HOLD. Ample room, same defensive logic as XLV. |
| `UNP` | +0.7% | +4.6% | HOLD, but note it fell 3.41% yesterday — rails are a cyclical read and XLI is -4.13% over 1m. Watch, do not add. |
| `PYPL` | -0.2% | +4.0% | HOLD. Flat; fintech, not a bank, so the XLF breakdown does not govern it. |
| `OXY` | -0.4% | +6.8% | HOLD, downgraded in character. Energy was **rejected as a new long today** (XLE -10.67% 1m). Room to the stop means no forced action, but do not add and do not read its low daily beta as defensiveness. |
| `XLU` | -0.7% | +2.8% | HOLD. Utilities +2.40% over 1m; the stop is only 2.8% away so this resolves soon either way. |
| `HUN` | -0.3% | +9.8% | HOLD. Widest stop clearance in the book; materials are mid-pack. |
| `ADM` | -2.4% | +4.1% | HOLD. Staples-adjacent, 4.1% of room, nothing new. |
| `CAG` | +1.9% | no stop | HOLD. Staples, in the leading sector, no stop by design. |
| `RTX` | -2.8% | +3.8% | HOLD. Defense, same logic as HII. Fell 2.03% yesterday with the tape, not on news. |

Collectively: **this is a defensively-positioned long book that is correctly
aligned with the month's rotation** (XLP +3.16%, XLU +2.40% against SPY -7.40%)
and was still down almost across the board yesterday because a liquidation day
sells the leaders too. That is a reason to stop adding, not a reason to
capitulate — which is why the only closes today are the two rows whose own
stops are already reached or about to be jumped.

## [06:29 ET] NOTE — conviction on TLT held at 4, not the 5 the count supports
TLT carries four distinct evidence kinds, which mechanically supports a 5. I
left it at 4 on an evidence-quality judgment: the `positioning` entry is a
single session's cross-asset breadth rather than the measured flow read the
config describes (insider buys, short interest, days to cover, revision
direction, implied move), and one day's relative performance is the weakest of
the four. Under-claiming is the safe direction — the red team lowers conviction,
it never raises it — and this report's documented failure mode is inflation, not
timidity. Size stays at 2% regardless: a counter-trend duration long should not
be sized at the 4-5% the high-conviction tier allows just because an evidence
count crossed a threshold.

## [06:31 ET] ARITHMETIC CHECK — every published number recomputed from source
`CLAUDE.md` is explicit that the model is "undisciplined about its own
arithmetic", so I recomputed every ratio, stop distance and expectancy rather
than trusting what I wrote.

| Idea | R:R recomputed | R:R published | Stop in ATR | Floor | Verdict | Baseline | win_prob | Claimed edge |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IWM | 2.272 | 2.27 | 2.369 | 1.8 | PASS | 0.306 | 0.42 | +11.4pp |
| TLT | 2.667 | 2.67 | 2.053 | 1.8 | PASS | 0.273 | 0.40 | +12.7pp |
| XLV | 2.125 | 2.13 | 2.130 | 1.8 | PASS | 0.320 | 0.38 | +6.0pp |
| LEN | 2.522 | 2.52 | n/a (bear case 68.00) | 2.5 | PASS | 0.284 | 0.45 | +16.6pp |
| DKS | 2.000 | 2.00 | 2.337 | 2.0 | PASS | 0.333 | 0.20 | **-13.3pp** |
| ONON | 2.054 | 2.05 | **1.937** | 2.0 | **FAIL** | 0.327 | 0.18 | **-14.7pp** |
| GLD | 5.398 | 5.40 | **1.302** | 1.8 | **FAIL** | 0.156 | 0.20 | +4.4pp |
| /MBTZ6 | 2.350 | 2.35 | n/a (cancel) | 2.5 | cancel | 0.299 | 0.40 | +10.1pp |

Every published ratio reconciles to the recomputation. No claimed edge exceeds
the 20pp "large claim" threshold. **All three failures sit on the four ideas
being closed or cancelled, and none on a live one** — which is the right place
for them, but two are worth recording as findings rather than noise:

- **`ONON` was published with a stop 1.94 ATR from entry, under the 2.0 stock
  floor.** Marginal, and it is being closed today for unrelated reasons, but it
  means the 2026-11-03 idea should not have passed `check_stop_distance` as
  written. Worth a look at whether the ATR used at publication differed.
- **`GLD`'s 416.36 stop was described on 2026-10-25 as "1.8 ATR, the ETF
  floor". Against today's ATR of 7.3674 it is 1.30 ATR.** This is not an
  arithmetic error — gold's ATR has *expanded* as it fell, so a stop that was
  1.8 ATR then is 1.30 ATR now. It is a good illustration of why a resting
  order's risk profile decays even when nobody touches it, and a second
  independent reason to cancel it.
- **DKS and ONON both carry negative claimed edge** (-13.3pp and -14.7pp
  against baseline). That is intentional and is the argument for closing them.
  `check_expectancy` should fail both. If `--enforce` demotes them to the
  watchlist, the close instructions in `entry.condition` and `catalyst.action`
  still stand and must not be lost.

## [06:33 ET] DATA GAP — the options-implied check is unavailable this run
`market_data.py implied` failed on all four live ideas with **HTTP 401
Unauthorized** from `query1.finance.yahoo.com/v7/finance/options/...`. Note this
is a *different* failure from the 429 rate-limiting that killed the index
quotes at 06:08 — the options endpoint now refuses unauthenticated access
outright, so it is a permanent break rather than a throttle that will clear.

**Consequence: I cannot say whether any target sits inside what the options
market prices.** The skill names this as a check the report used to skip, and
today it is unavailable rather than skipped.

**Substitute used** — target distance in ATRs and against the 150-day range,
which answers a narrower version of the same question:

| Idea | Spot | Target | Points | ATRs away | 150d high | Target vs that high |
| --- | --- | --- | --- | --- | --- | --- |
| IWM | 264.22 | 238.69 | 25.53 | 4.32 | 305.18 | -21.8%, inside range |
| TLT | 80.35 | 84.30 | 3.95 | **5.41** | 87.79 | -4.0%, inside range |
| XLV | 177.46 | 201.00 | 23.54 | **6.27** | 192.32 | **+4.5%, ABOVE THE HIGH** |
| DKS | 136.14 | 175.50 | 39.36 | 5.94 | 244.38 | -28.2%, inside range |

Two things this surfaces that I had not written down:

- **`XLV`'s 201.00 target is 4.5% above the highest price in 150 days.** The
  position therefore needs healthcare to make a new high, which is a materially
  stronger claim than "hold the 50dma" — the thesis I actually argued for it at
  06:22. The existing scale plan partly covers this by trimming a third at
  192.32, the level that already rejected price on 2026-11-05, but the full
  target is a new-high claim and should be read that way. This is the weakest
  live idea on the page and the 0.39-ATR stop clearance means it resolves soon
  regardless.
- **`TLT`'s target is 5.41 ATR away** on a 0.91%-ATR instrument. That is a large
  multiple of a small number — a 4.9% move — and it sits inside the range, 4.0%
  below the 150-day high of 87.79. Reachable, but not a quick move: at this ATR
  it is a multi-week hold, which is consistent with the Dec 9 FOMC being the
  catalyst rather than the Nov 25 print.

## [06:35 ET] REJECTED — SMH short — the volatility makes an honest frame impossible
The best-looking short on the tape and it does not survive the floors. The
setup is genuinely attractive: SMH gapped up 2.9% on NVDA raising FY28 revenue
growth guidance to 75%, ran to +4.4%, and closed **-2.62% at 447.48** — a 6.8%
high-to-close reversal on the single best piece of news the sector could get.
It is 33.4% off its 671.83 high.

Two independent reasons it is not a trade:

1. **It is on the same thrice-defended shelf as QQQ.** Lows of 445.59 (Nov 5),
   **445.3158 (Nov 17)** and 447.20 (Nov 19) — spot is 0.49% off the 150-day
   low. Initiating a short 2 points above a triple bottom is where shorts pay
   for the privilege.
2. **ATR(14) is 27.46 — 6.14% of price — and that breaks the arithmetic.** An
   honest structural stop above the 2026-11-11 high of 516.65 is 69 points, or
   2.5 ATR. The 2.0 swing floor then demands **138 points of reward, a 309
   target — roughly 54% off the high.** Even the minimum 1.8 ATR stop (49.4
   points, ~497) demands a 348.70 target, 48% off the high. Neither is a
   credible swing target, and the only way to make the ratio work is to pretend
   the stop can sit inside the shelf — which is the KRE failure exactly.

**This is the general reason today's report is thin, and it is worth stating
plainly:** the instruments that are actually moving have 3–6% ATRs (QQQ 3.06%,
ONON 5.88%, DKS 4.87%, SMH 6.14%), and at those volatilities a 2.0 ratio with a
compliant stop requires a target so distant it stops being a forecast. The
instruments that are calm enough to frame — XLP at 1.84%, XLF at 1.97% — are
either near their highs (XLP, fails the ratio) or breaking down (XLF). The
floors are not blocking good ideas today; they are correctly reporting that the
tape offers volatility without offering structure.

## [06:36 ET] RESEARCH COMPLETE
- **candidates: 8 unique symbols** (9 lines — IWM captured twice, the second
  adding the dated catalyst; synthesis takes the last entry per symbol)
- Ran **06:00–06:36 ET** of a ~60 minute budget, closing with this block, so
  **nothing was lost to the clock.** The headings between `[06:02]` and
  `[07:02]` are inflated by up to 49 minutes — see the `[06:13] CORRECTION` —
  because I estimated elapsed time instead of calling `date`. Their order and
  content are sound; only the labels are wrong.

**WHAT THIS REPORT IS.** Eight ideas, and **not one is a new position.** Three
holds (`IWM`, `TLT`, `XLV`), one continuing accumulation (`LEN`), two closes
(`DKS`, `ONON`) and two order cancellations (`GLD`, `/MBTZ6`). That is the
honest output of the day rather than a shortfall, and `config/strategy.md` is
explicit that publishing fewer beats padding.

**WHY NO NEW ENTRIES.** Six candidate ideas were researched and rejected on
evidence, each logged above with the arithmetic: `XLE`/energy (relative
strength was false — -10.67% 1m vs SPY -7.40%), `XLF` (good 1m relative number,
but it broke its 50dma on expanding volume in the last four sessions), `XLP`
(strongest sector, fails the 2.0 ratio — the nearest compliant stop forces a
target 4.4% above its 150-day high), `QQQ` long off the 644–647 shelf (passes
the ratio at exactly 2.0, fails the win probability), `SMH` short (on the same
shelf, and a 6.14% ATR makes the compliant target ~50% off the high), and
`GLD` long (not bottoming — at its 150-day low, -24.84% off the high and
accelerating). Insider screens across AMD, MU, AVGO, QCOM, MRVL and INTC found
**no cluster** — a single buyer at AVGO and at INTC.

**THE BAR WAS RAISED DELIBERATELY, AND THAT IS MOST OF THE EXPLANATION.** The
track record is now 44 closed trades, past the noise threshold: 5/44 to target
(11%), avg -5.5%, with single-name stocks at **2/30 (7%), avg -7.1%** and
conviction-2 ideas at 0/6. So at 06:02 I set the bar at conviction 4 for any new
single-name long and barred new conviction-2 single-name longs. Nothing I found
today cleared it. The book is also already 17 longs deep and correctly aligned
with the month's rotation (XLP +3.16%, XLU +2.40% against SPY -7.40%) — the
error available today was adding an eighteenth correlated defensive long, not
publishing seven.

**REGIME, in one line:** a **Fed hiking cycle** — first hike in three years in
September 2026, 25bp more priced at 91–92c for Dec 9, the 10Y at 5.07% and the
2Y 92bp above effective funds — repricing the discount rate. The whole index
drawdown is tech (XLK -14.77% 1m); the rest of the market has rotated, not
fallen.

**coverage gaps:**
- **No VIX, no overnight futures, no index quotes.** Yahoo returned HTTP 429 on
  every call and finnhub refuses indices. So I know where the market closed and
  **not** where it is trading at 6am — every index read here is from ETF
  proxies at the 2026-11-19 cash close.
- **No options-implied check on any idea.** Yahoo's options endpoint now returns
  **401 Unauthorized** — a permanent break, not a throttle. Substituted a
  target-distance-in-ATR table at 06:33, which surfaced that **XLV's 201 target
  sits 4.5% above its 150-day high**.
- **Event contracts: priced for the first time, but via a workaround.**
  `market_data.py events` is **broken** — it filters client-side over an
  unfiltered first 200 markets, which are all sports parlays, so every macro
  query returns 0. This is very likely why the lane shows 4 tracked ideas and no
  closed trades. I queried Kalshi's series endpoints directly; prices live only
  on the single-market endpoint, in `*_dollars` fields.
- **No independent inflation estimate.** `macro` returns `cpi_yoy: 337.476`,
  which is the CPI **index level**, not a year-over-year rate. Without the
  October YoY I could not build a nowcast, which is the specific reason I
  declined the Nov CPI >3.8% contract at 12c despite its attractive shape.
- **Not reached:** small and micro caps got no dedicated screen — the lane the
  universe config asks to be hunted hardest. With IWM at 150-day lows I judged a
  rate-driven small-cap screen low-yield, but that is a judgment, not coverage.
  Also not reached: `filings`, `analysts` and `short` on anything, and no
  individual-name catalyst work beyond the earnings calendar.

**sources that failed:** Yahoo chart API (429, all index and futures quotes),
Yahoo options API (401, all `implied` calls), finnhub indices (CFD subscription
required), stooq (404 on `^`-prefixed symbols), AlphaVantage (no API key),
CoinGecko within the `macro` call (succeeded standalone),
`market_data.py events` (returns 0 for every macro query — a client-side filter
bug, not an upstream outage).

## [06:38 ET] SMALL-CAP SCREEN — closing the gap I had just declared
I flagged small caps as uncovered in the RESEARCH COMPLETE block above and then
had clock left, so I ran the screen rather than leaving the gap standing.
Method: insider buying across the small and mid caps reporting inside the next
four sessions, so a dated catalyst is attached by construction.

| | open-market buys | distinct buyers | reports |
| --- | --- | --- | --- |
| SYM | 0 | 0 | 11-23 amc |
| **FLNC** | 2 | **2** | 11-23 amc |
| SMTC | 0 | 0 | 11-23 amc |
| AMBA | 0 | 0 | 11-24 amc |
| TITN | 0 | 0 | 11-24 bmo |
| **DY** | 3 | **3** | 11-24 bmo |
| CMP | 0 | 0 | 11-23 amc |
| CENT | 0 | 0 | 11-23 amc |

### REJECTED — DY (Dycom) — the best finding of the run, and still a no
The insider cluster is the real thing this report is told to hunt: **3 distinct
buyers, $551,307, and zero sells in six months.**
- Sabater Carmen M — 350 sh @ 280.62, 2026-09-23
- Peyovich Daniel S — 850 sh @ 296.76, 2026-09-09
- Fallon David Joseph — 700 sh @ 286.92, 2026-09-01

**And then the price: DY closed 221.36.** The insiders are **down 21–25% on
every one of those purchases**, and that inverts what the signal is worth. The
skill's case for insider buying is that it confirms "a de-rated name is cheap
rather than broken." Here three officers bought and the stock fell another 23%,
which is evidence on the *other* side of exactly that question.

The rest of the picture says broken, not cheap:
- **-60.92% off the 150-day high of 566.465**, range 186.25–566.465
- **-43.67% over 3m and -46.59% over 6m**, against XLI -10.48% and -5.38% —
  underperforming its own sector by **33.2pp over 3m and 41.2pp over 6m**. A
  drawdown that size relative to the sector is a company event, not a regime.
- ATR(14) 13.12 = **5.93%**, 20dma 222.16, 50dma 252.04 — price below both
- Avg daily dollar volume $129M, so liquidity is fine; that is not the problem

Three reasons not to buy it today, any one sufficient:
1. **It reports 2026-11-24 bmo.** Opening a position two sessions before a print
   is the identical risk I just closed `DKS` to avoid, and on a 5.93% ATR name
   the gap jumps any compliant stop. Doing both in one report would be incoherent.
2. **It fails my own bar from 06:02** — two distinct evidence kinds
   (`dated_catalyst`, `positioning`) supports conviction 3, and I set the bar at
   4 for any new single-name long given the 2/30 stock record.
3. **Win probability.** A compliant stop below the 186.25 low (184, = 2.85 ATR)
   needs a 296 target to clear 2.0 — a **+34% move, back to where the insiders
   bought**. I do not believe that happens before -17% at better than the 33%
   break-even, and I am not going to reverse-engineer a nearer target to make
   the ratio print.

**No candidate emitted, and I deliberately did not manufacture one.** I could
have built a "wait for the print" entry off the 186.25 shelf, and that is how a
contrived idea gets onto a page — levels invented for a name I had already
decided not to own. **For the watchlist instead: revisit DY after the 2026-11-24
print, with levels drawn from the actual reaction.** If the quarter stabilises
revenue, three officers buying into a 61% drawdown with no offsetting sales
becomes a genuinely asymmetric setup; until the print it is a falling knife with
a catalyst attached.

`FLNC` (2 buyers, reports 11-23 amc) was not taken further — same
position-before-earnings objection, a weaker cluster, and no time to do it
justice.

## [06:40 ET] ADDENDUM TO RESEARCH COMPLETE — one coverage gap is now closed
The gap list above says small and micro caps "got no dedicated screen". **That
is no longer true** and the line should be read as superseded: the 06:38 screen
covered eight small/mid caps reporting inside four sessions, found insider
clusters at `DY` (3 buyers) and `FLNC` (2 buyers), and rejected both with
reasons. `DY` goes to the watchlist for post-2026-11-24 reassessment.

Standing gaps, revised and final:
- No VIX, no overnight futures, no index quotes (Yahoo 429; finnhub indices
  need a CFD subscription). Everything here is the 2026-11-19 cash close.
- No options-implied check on any idea (Yahoo options 401). Substituted
  target-distance-in-ATRs at 06:33.
- No independent inflation nowcast — `macro` returns the CPI index level, not
  YoY. This is the stated reason the Nov CPI >3.8% contract at 12c was declined.
- `market_data.py events` is broken (client-side filter over 200 sports
  parlays). Worked around via Kalshi series endpoints; worth a real fix.
- `filings`, `analysts` and `short` were not run on anything. `insiders` was,
  across 14 names.
- Micro caps specifically (sub-$300M) still unscreened — the 06:38 screen was
  driven off the earnings calendar, which skews larger.

Final count: **8 unique candidates, 9 lines, zero new positions**, closing at
06:40 ET of a ~60 minute budget with time unused rather than truncated.
