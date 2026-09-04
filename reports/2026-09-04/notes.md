# Research log — 2026-09-04

## [06:02 ET] MACRO — rates, policy, tape
Data source health: **Yahoo Finance is returning HTTP 429 across the board** this morning.
`market_data.py macro` failed on spx/ndx/dow/russell/vix/es/nq/dxy/us10y/gold/wti and on crypto.
Finnhub is working for equity/ETF quotes and earnings. FRED is working. Note this for
`data_quality_notes` — index and crypto spot levels are unavailable this run except via proxies.

- Fed funds effective **3.63%** (2026-09-02) — source: FRED via market_data.py macro
- US 10y **4.79%**, US 2y **4.39%**, 10y-2y curve **+0.43** (2026-09-02/03) — source: FRED
- Unemployment **4.1%** (Jul 2026 print) — source: FRED
- Prior close (2026-09-03, 16:00 ET, finnhub): SPY 773.17 (+1.05%), QQQ 717.67 (+1.19%),
  IWM 295.19 (+0.40%), TLT 82.07 (+0.15%), GLD 410.22 (+1.85%)
- Read: risk-on close, mega-cap led (QQQ > SPY > IWM), **gold +1.85% on the same day** —
  that combination is a liquidity/debasement bid, not a growth bid.
- 10y at 4.79% with fed funds at 3.63% = ~116bp of positive term spread. Long end is not
  cooperating with the cuts already delivered.

**All prices above are the 2026-09-03 close (market closed, age ~842 min). That is the
freshest honest equity price at 6am ET — it is a closed session, not stale data.**

## [06:18 ET] MACRO — the regime is a HIKE debate, not a cut debate
This is the single most important framing for today and it inverts the usual read.

- **August employment report, today 2026-09-04 08:30 ET.** Dow Jones consensus **+53,000**
  nonfarm payrolls, unemployment **4.1%** unchanged, average hourly earnings **+0.2% m/m**.
  June and July together were a **net -3,000 jobs**. — sources:
  https://www.cnbc.com/2026/09/03/august-2026-jobs-report-payrolls.html ,
  https://www.kiplinger.com/investing/economy/jobs-report-august-2026-what-to-expect
- **The September 16 FOMC is priced as a coin flip on a 25bp HIKE.** Odds were ~63% for a
  hike, and fell to ~50% Thursday after Governor Waller said he would be inclined to
  support holding, absent an inflation surprise. — source:
  https://finance.yahoo.com/markets/stocks/articles/dow-rises-635-points-fed-170855232.html
- 2026-09-03 tape: Dow +635 (+1.2%), S&P +1.0%, Nasdaq +1.3% — the Dow's best day since
  Aug 4 — on the Waller remarks. 10y fell to ~4.75% from its highest since Nov 2023.
  Gold +2.3% on a softer dollar.
- FRED (fetched): fed funds 3.63%, 2y 4.39%, 10y 4.79%, 10y-2y +0.43.

**What this means for today's ideas.** The tape is not trading growth, it is trading the
policy path, and the whole path hinges on one 8:30 print. Anything whose thesis is "rates
come down" and anything whose thesis is "rates go up" are the same trade with opposite
signs — the correlation cap applies hard. Front-running the print is not edge.

## [06:20 ET] DATA GAPS this run
- Yahoo Finance: **HTTP 429 on every request**. No index levels, no VIX, no DXY, no WTI,
  no crypto spot from `macro`. Finnhub covers equities/ETFs; FRED covers rates.
- **Kalshi event-contract prices are unavailable.** `market_data.py events` returns
  unrelated markets for "Fed"/"payrolls", and the public
  `api.elections.kalshi.com/trade-api/v2/markets/<ticker>` endpoint returns the
  KXFEDDECISION-26SEP series as `status: active` with **null yes_bid / yes_ask /
  last_price / volume / open_interest**. So no event contract can be priced this morning,
  and per the no-fabricated-numbers rule **no new event-contract idea is captured today**.
  The three already-published Fed contracts stay as they are; I cannot quote a live mark
  for them. Verified tickers exist and close 2026-09-16T17:59Z (SEP) / 2026-10-28T17:59Z (OCT).

## [06:09 ET] POSITION UPDATE — LULU — opened 2026-08-22 @ 115.00, now ~100.08 (-13.0%)
- decision: **CLOSE IN FULL AT THE OPEN.** Captured via add_candidate.py (direction `sell`, conviction 4).
- why: Q2 FY2026 released 2026-09-03 after the close is a thesis break, not a drawdown.
  Net revenue 2.4B -4%; comps -9% with the Americas at **-12%**; gross margin 60.5% flattered
  by a **134.5M tariff refund worth 0.86 of the 2.92 diluted EPS**. Q3 guided to -10%/-11%
  revenue and 0.93-0.98 EPS against 2.59 a year ago. **FY EPS cut to 9.48-9.73 from 13.26.**
  Shares -17.81% after hours to 100.08, through the 104.44 52-week low.
  — sources: https://www.stocktitan.net/news/LULU/lululemon-athletica-inc-announces-second-quarter-fiscal-2026-ztmlx8ipmavo.html ,
    https://www.investing.com/news/company-news/lululemon-q2-2026-presentation-revenue-drops-4-stock-plunges-18-93CH-4888642
- the 180 target implied ~18.7x the new 9.60 FY base on a business shrinking double digits.
- positioning corroborates: fetched finnhub recommendation trend shows bullish share 8/39 in
  June to **2/40 (5.0%)** on 09-01, revision direction deteriorating — *before* this print.
- **LULU was published 5x in the last 10 days.** That is the anchoring pattern prior_context
  warns about, and it cost 13%. Worth stating in the report rather than quietly closing.

## [06:09 ET] POSITION UPDATE — RARE — opened 2026-08-31 @ 25.20, closed 09-03 at 14.85 (-41%)
- decision: **CLOSE, restated.** The 09-03 report already instructed selling at the open; the
  tracker still carries it open and `prior_context` still shows a stale 26.53 last price, so
  it is restated once. Captured via add_candidate.py.
- 09-03 regular-session close was **14.85**, -44.03% from 26.53 (finnhub, fetched 06:0x ET).
  The 22.90 stop was gapped through by ~9.6 ATR (ATR14 was 1.22).

## [06:09 ET] POSITION CONFLICT — TLT is held long AND short at the same time
- `TLT` BUY opened 2026-08-20 @ 82.60, target 86.20, stop 80.95 — last 82.07, -0.6%
- `TLT` SELL opened 2026-09-02 @ 81.87, target 78.30, stop 83.60 — last 82.07, -0.2%
- These are the same instrument in opposite directions. Net exposure is approximately zero
  and the pair pays two spreads to express no view. It has to be resolved today, and today
  is the day the information arrives: the 08:30 payroll print.

## [06:12 ET] EVENT CONTRACTS — live Kalshi marks obtained, from the trades endpoint
The `markets` endpoint returns nulls for bid/ask, but
`trade-api/v2/markets/trades?ticker=...` returns real executions. Fetched 2026-09-04 ~06:11 ET
(trade timestamps 2026-09-04T10:0x UTC), last traded YES price in cents:

| Contract | Sep 16 FOMC | Oct 28 FOMC |
| --- | --- | --- |
| Hike >25bp | **2** | — |
| Hike 25bp | **43** (prior print 42) | **26** |
| Hold | **56** (prior print 57) | **69** |
| Cut 25bp | **1** | **4** |
| Cut >25bp | **1** | — |

Cross-check: fed funds futures put a September hike at **50.4%** after Waller, down from
63.2% — source https://finance.yahoo.com/markets/stocks/articles/dow-rises-635-points-fed-170855232.html
Kalshi's hike total is 43+2 = **45%**. Consistent within the usual basis; nothing mispriced there.

### [06:12 ET] REJECTED — KXFEDDECISION-26SEP-H0 YES @ 56 — no defensible edge, and the R:R floor cannot be cleared honestly
I like the hold case — a governor publicly leaning hold two weeks out, into a July payroll
print of **-23,000** — and I would put hold nearer 70% than 56%. It still does not publish:

1. **The 08:30 print is 2h15m away and moves this contract 15 points either way.** Buying
   before it is not edge, it is a coin flip on a number nobody has.
2. **A binary at 56c cannot clear a 2.0 reward-to-risk floor without a manufactured stop.**
   Held to resolution it risks 56 to make 44 — 0.79:1. The only way to a 2:1 is to invent a
   stop at 40 and a target at 94, and then the implied break-even hit rate is 33% against a
   claimed 62%, a ~29 point edge on a two-week macro binary. That is the exact
   walk-the-stop-in pattern this report has already been burned by. Not published.

The good event-contract trades are cheap tails and expensive near-certainties. 56c is neither.

### [06:12 ET] STALE LIMITS — the two pending Fed contracts should be cancelled, not left resting
- `KXFEDDECISION-26SEP-H25` YES limit **32** (published 08-22) — market is **43**. The limit
  is 11 points below the market and only fills if the hold case wins, i.e. it fills exactly
  when it has become worthless. Cancel.
- `KXFEDDECISION-26SEP-H0` YES limit **47** (published 09-03) — market is **56**. Same
  structure inverted: it fills only on a hawkish payroll print. Cancel.
- `KXFEDDECISION-26OCT-H25` YES limit **28** (published 09-02) — market is **26**, so this
  one is live and near the money. It is the only one of the three still doing anything.

## [06:21 ET] PENDING-ORDER AUDIT — where the 15 resting limits actually sit
Fetched 2026-09-03 closes against the published limits. Distance matters: a limit far below
a rising market is not patience, it is a setup that only fills if the thesis breaks.

| Setup | Limit | 09-03 close | Gap | Read |
| --- | --- | --- | --- | --- |
| `SPY` SELL_SHORT | 773.00 | **773.17** | **0.0%** | at the trigger — **cancelled**, see below |
| `IYR` SELL_SHORT | 103.60 | 102.88 | through it | filling / filled |
| `XLE` BUY | 63.00 | 64.62 | -2.5% | live and well placed — **amended**, stop widened |
| `EEM` BUY | 65.60 | 67.47 | -2.8% | live |
| `CEG` BUY | 272.00 | 285.05 | -4.6% | live |
| `DINO` BUY | 99.50 | 106.15 | -6.3% | far |
| `LCII` BUY | 94.00 | 101.04 | -7.0% | far |
| `DG` BUY | 121.00 | 131.26 | -7.8% | far, but 121 sits on the 50-day (122.50) — a real level, leave it |
| `PFE` BUY | 25.80 | 28.81 | -10.5% | stale |
| `VST` BUY | 128.00 | 144.22 | -11.2% | **dead** — 128 is below the 150-day low of 132.66 |
| `KXFEDDECISION-26SEP-H25` | 32 | 43 | -11 pts | stale, cancel |
| `KXFEDDECISION-26SEP-H0` | 47 | 56 | -9 pts | stale, cancel |
| `KXFEDDECISION-26OCT-H25` | 28 | 26 | +2 pts | live, near the money |
| `BTC` SELL / `/MBTU6` SHORT | 63400 / 64340 | unpriced | — | crypto quotes unavailable this run (Yahoo 429) |

## [06:21 ET] POSITION UPDATE — SPY short — **CANCELLED before it fills**
- Published 08-31 at 773.00 short, target 750, stop 782, conviction 2. SPY closed 773.17.
- It fills on this morning's open, two hours before the payroll print, by accident of where
  the limit was left rather than by any decision made today.
- With ATR14 now 5.5098 the 782 stop is 1.63 ATR — **under the 1.8 ATR ETF floor**. SPY is
  0.80% off its 150-day high and above both the 20-day (769.21) and 50-day (756.14).
- Captured with a **null entry** so the setup cannot fill; that also marks it not-filled and
  keeps it out of P&L, which is the honest accounting for a withdrawn setup.

## [06:21 ET] POSITION UPDATE — XLE — amended, **stop widened and target cut**
- Entry unchanged 63.00. Stop **61.40 → 60.70** (1.45 ATR → 2.08 ATR, now clears the 1.8 ATR
  ETF floor). Target **70.00 → 68.50**. R:R falls 4.4 → 2.39. Both legs moved against the
  position; this is the opposite of the KRE stop-walking pattern.
- New dated catalyst: **OPEC+ ministerial Sunday 2026-09-06** on October quotas. September's
  188k bpd tranche completed the rollback of the whole 1.65m bpd 2023 voluntary cut, and
  delegates have briefed a hold for the rest of 2026 — source
  https://www.cnbc.com/2026/08/02/opec-agrees-september-oil-hike-completing-rollback-of-voluntary-cuts.html
- Brent 95-99 / WTI 90-91 after US strikes near the Strait of Hormuz on 09-01.
- XLE is the tape's leadership: +12.76% 1m vs SPY +0.44%, ahead on 3m and 6m, above the 20-,
  50- and 200-day. `wait: true` — the limit is not live until the Sunday decision is known.

## [06:24 ET] REJECTED — the LULU share-taker trade — the whole category is broken, not just LULU
The obvious second-order trade off this morning's print is to buy whoever is taking LULU's
women's share. Fetched history says there is no such name:

| | last | off 150d high | vs 150d low | 20d | 50d |
| --- | --- | --- | --- | --- | --- |
| ONON | 28.36 | **-43.6%** | 27.56 (at it) | 30.67 | 34.47 |
| DECK | 84.50 | **-30.9%** | 83.25 (at it) | 90.12 | 97.52 |
| AS | 28.51 | **-33.3%** | 28.10 (at it) | 32.19 | 33.86 |
| NKE | 38.77 | -30.4% | 37.95 (near) | 39.99 | 41.56 |
| LULU | 121.77 pre-print | -28.5% | 104.44 | 120.32 | 118.63 |

Every one of them is at or within a per cent of its 150-day low and below both moving
averages. That is a category demand contraction — inflation, tariffs and the end of the
comfort-apparel cycle — not share moving from one brand to another. — source:
https://www.fool.com/investing/2026/08/11/nike-lululemon-deckers-and-on-holding-have-all-plu/
**No long in this group publishes today**, and it strengthens rather than weakens the LULU exit.

## [06:24 ET] POSITION UPDATE — NKE — opened 2026-08-25 @ 40.75, last 38.77 (-4.9%)
- decision: **hold, no change captured.** Nothing today alters the levels, and the invalidation
  already published (bear case 33.00) is intact.
- what is genuinely new, and it cuts both ways:
  - **Insider cluster, fetched:** 5 open-market buys, **4 distinct buyers**, $3.73m in six
    months, net +$2.53m. Includes **Tim Cook 25,000 shares at ~$42.00 (2026-04-10)** and CEO
    **Elliott Hill 47,320 shares at ~$42.27 (2026-04-13)**. The stock at 38.77 is **below**
    where all of them bought. This is the strongest single public signal type and it is here.
  - Against it: the table above says NKE's drawdown is the category's, not a fixable
    company-specific problem, and LULU's Americas comp of -12% is a demand reading for the
    whole segment. NKE has been at a 12-year low this week.
- next dated catalyst: **Q1 FY2027 results 2026-10-01 after the close** — Hill's first real
  test of the Sport Offense reorganisation. Outside the 10-session window, so no trade today.
  — source: https://earningscountdown.com/stock/nke/
- **Discipline note: NKE has been re-pitched 6 times in 14 days** at entries of 40.00, 38.00,
  38.50, 40.75, 34.00 and 39.00, with the target moving 65 → 62 → 56 → 62. That is the
  anchoring pattern, and re-pitching it a seventh time today with nothing new would be it
  again. Holding without a new pitch is the correct action.

## [06:24 ET] POSITION UPDATE — SVRA — opened 2026-08-23 @ 5.35, last 5.37 (+0.4%)
- decision: **hold, no change.** Levels intact (target 8.00, stop 4.60, 3.8 ATR of room).
- **Horizon is mislabelled and worth fixing at synthesis:** it is published `swing` but the
  catalyst is the MOLBREEVI (molgramostim, aPAP) PDUFA, which the FDA **extended on
  2026-04-15 from 08-22 to 2026-11-22** — 79 days out — after deeming the company's responses
  a major amendment. The agency cited no safety, efficacy or manufacturing concern.
  — source: https://www.biopharminternational.com/view/fda-extends-review-of-savara-s-molgramostim-bla-for-pap
  A days-to-weeks label on an 11-week binary misrepresents how long the capital is committed.

## [06:24 ET] POSITION UPDATE — CCJ — opened 2026-08-17 @ 94.00, last 100.62 (+7.0%)
- decision: **hold, no change.** Long-term, target 135.00, bear case 78.00.
- thesis confirmed rather than changed: uranium spot ~$85 but the **long-term contract price
  is ~$94, an 18-year high and the first time above $90 since 2008**, and utility contracting
  is expected to reaccelerate in September as the summer lull ends.
  — source: https://sprott.com/insights/uranium-s-tale-of-two-markets/
- fetched: +4.4% on 09-03 to 100.62; ATR14 4.3879, SMA20 99.68, SMA50 95.45, -23.3% off the
  131.21 range high. Relative strength +6.74% 1m vs XLU -1.44%, but still -11.75% over 3m.
- no new pitch: the position is working and nothing today improves on 135/78.

## [06:24 ET] POSITION UPDATE — GLD — last 410.22, +1.85% on 09-03
- decision: **hold, no change.** Long-term, target 500, bear case 330 (re-pitched 09-03 at 375).
- gold rose 2.3% on 09-03 on a softer dollar and lower yields. Worth naming precisely because
  it is the *odd* part of the tape: gold bid while the FOMC is a coin flip on a **hike** is a
  debasement/liquidity bid rather than a real-rates one, and it is the reason this position
  is not redundant with the equity book.
- fetched: ATR14 8.5071, SMA20 409.48, SMA50 388.13, -11.4% off the 462.80 range high.

## [06:24 ET] POSITION UPDATE — BCC — opened 2026-08-25 @ 76.50, last 77.12
- decision: **hold, no change.** Long-term, target 110, bear case 65.
- fetched: ATR14 2.3711, SMA20 81.30, SMA50 79.09 — below both, -12.8% off the 88.43 high.
- the headwind is explicit and unchanged: the 10-year at 4.768% and the 30-year at 5.2433%
  with the FOMC debating a hike is not the rate path a wood-products housing thesis needs.
  It is inside the 65.00 bear case, so it holds, but it is the weakest of the open longs.

## [06:28 ET] CRYPTO — the biggest thing the book was not seeing
`market_data.py crypto` works even though the Yahoo-backed `macro` crypto block fails.
Fetched 2026-09-04 ~06:2x ET, cross-checked against Coinbase spot:

| | CoinGecko | Coinbase | 24h |
| --- | --- | --- | --- |
| Bitcoin | **80,842** | 80,836 | **+4.13%** |
| Ether | 2,517.56 | 2,517.73 | +5.06% |
| Solana | 103.66 | — | +3.45% |

The report is carrying **two bearish bitcoin rows against this**:
- `BTC` SELL, published 08-17 at **63,400**, invalidation 65,200 — market is **+27.5%** past
  the entry and **+24.0%** past the invalidation. It was also always a no-op: Robinhood
  Crypto cannot short, which the 08-18 report itself identified.
- `/MBTU6` SHORT, published 08-19 at **64,340**, stop **66,600** — market is **+25.6%** past
  the entry and **+21.4%** past the stop. On a 0.1 BTC micro contract that is roughly
  **-$1,650 per contract against a stop designed to risk about $226**.

**Both are captured as cancellations with a null entry.** The important part is *why* this was
invisible: `prior_context` lists both under "awaiting entry — the market never reached the
entry", because the crypto price refresh has been failing, so nothing ever marked them filled
and nothing ever marked them stopped. A stop that the pipeline cannot price is not a stop.
This belongs in `data_quality_notes` — it is a tracking failure, not a market one.

## [06:28 ET] REJECTED — NOC — the best long-term candidate I found, and it still fails the floor
Worth writing up because the business case is genuinely good and the arithmetic still says no.
- Q2 2026: net awards $20.0bn, **book-to-bill 1.84x**, **record backlog $104.7bn** (~2.4x
  annual sales). Guidance **raised**: FY26 sales $43.75-44.25bn, adjusted EPS **$28.60-29.10**,
  FCF reaffirmed $3.1-3.5bn. Q2 EPS 7.68 vs 6.888 estimate, +11.5% (fetched surprise record).
  — sources: https://seekingalpha.com/news/4615846-northrop-grumman-raises-2026-outlook-as-backlog-hits-record-105b ,
    https://www.investing.com/news/company-news/northrop-grumman-q2-2026-slides-record-backlog-drives-raised-outlook-93CH-4803774
- Fetched: last 528.24, ATR14 13.31, SMA20 558.86, SMA50 543.45, SMA200 603.14, 200-day range
  479.02-774.00, **-31.75% off the high**. So guidance was raised while the stock fell a third.
- **Why it still fails.** 528.24 is **18.3x** the midpoint of the raised FY26 adjusted EPS
  guide (28.85). That is a normal multiple for a prime, not a distressed one — the 774 high
  was Iran-war euphoria and this is a round trip to fair, not a de-rating to cheap. An honest
  valuation anchor is ~19x a 2028 EPS near 34, so **650**; an honest bear case is a budget
  scare taking it to 15x a flat 28, so **420**, below the 479.02 200-day low. That is
  **(650-528.24)/(528.24-420) = 1.12:1** against a 2.5 long-term floor.
  Stretching the target to the 700 "narrative fair value" only gets to 1.59:1.
- The only ways to publish it are a euphoria multiple or a bear case that pretends a
  de-rate cannot continue. Neither is available. **No trade.** Watchlist it under 470.
- Also against: fetched insiders show **0 open-market buys and 22 sells** in six months, and
  the recommendation trend is deteriorating (bullish share 60.7%, -3.6 points).

## [06:28 ET] REJECTED — the tanker complex — the Hormuz premium is already paid
US strikes near the Strait of Hormuz on 09-01 are the obvious tanker catalyst, and the whole
group has already taken it: FRO 45.42 (**-1.15%** off its 120-day high), INSW 102.24 (-0.77%),
DHT 20.19 (-2.09%), TNK 91.83 (-2.76%), STNG 80.11 (-8.33%). Four of five are within 3% of
their highs and every one is above its 20- and 50-day. Entering at the high on public news,
with no pullback level to lean on and Trump saying the campaign will not run "too long", is
buying the headline. Note that **DHT was stopped out of this report on 08-26 and is now back
near its high** — that is the cost of a 1.6-ATR stop, not a reason to re-enter here.

## [06:28 ET] REJECTED — MAX (MediaAlpha) — real news, levels do not clear
Genuinely interesting: 8-K press release **2026-09-03** says Q3 revenue, Contribution and
adjusted EBITDA will be **at or above the top end** of the ranges given on 07-29 — that is
≥$355m revenue against $316.9m in Q2 (+26% y/y) and ≥$35.0m adjusted EBITDA against $29.3m.
The stock **fell 2.5% to 12.22** on 808k shares because the same 8-K announced a **CFO
transition** (Tigran Sinanyan in 10-01, Patrick Thompson out).
— sources: https://www.sec.gov/Archives/edgar/data/0001818383/000181838326000229/max-20260902.htm ,
  https://www.sec.gov/Archives/edgar/data/0001818383/000181838326000198/maxq22026-earningsreleasex.htm
Fetched: ATR14 0.5238 (4.29%), SMA20 12.911, SMA50 13.112, range 7.09-14.70, ADV $8.7m
(clears the $500k floor). A 2.0 ATR stop puts the invalidation at ~10.85; the nearest real
resistance is the 14.70 range high. **(14.70-12.22)/(12.22-10.85) = 1.81:1**, under the 2.0
swing floor, and the only way past it is a 15+ target that exists nowhere in the price
history. Watchlist, not a trade.

## [06:28 ET] REJECTED — PL (Planet Labs) — a beat with a guide-down inside it
Q2 FY27 on 09-03: revenue **$116.1m, +58% y/y**, beating the $104.2m consensus by 11%, and a
first adjusted-profitable quarter at **$13.9m** adjusted EBITDA, driven by an NGA award and a
German government tender. But **Q3 is guided to $101-105m — a sequential decline** — with
adjusted EBITDA back to **-$6m to -$1m**, and FY27 adjusted EBITDA of only $3-10m.
— source: https://www.investing.com/news/company-news/planet-labs-q2-fy27-slides-58-revenue-growth-profitability-milestone-93CH-4888670
Fetched: 18.35 close on 09-03 (**-8.2% on 31.95m shares against a 6.7m average**), then +4.4%
after hours to ~19.16. **-64.6% off the 51.76 high**, below the 20-day (22.12) and 50-day
(23.73), sitting on the 17.83 range low. The quarter was lumpy government revenue and the
company's own guide says so. Buying a 4% after-hours bounce in a -65% downtrend on a
sequential guide-down is not a setup. No trade.

## [06:28 ET] REJECTED — ADBE, ORCL, AVAV, RH — earnings inside 10 sessions, none underwritten
Logged so synthesis does not re-litigate them.
- **ADBE** (09-10 amc): 285.75 and only **-4.55%** off its 150-day high after running from
  190.12 — the de-rating people are still talking about has largely repaired. Consensus target
  ~261 is **below** the price and Morgan Stanley is at Underweight/240. Nothing cheap left.
- **ORCL** (09-10 amc): 154.04, -38.5% off the 250.25 high. The de-rate is real and so is the
  reason — FY26 capex +162% to ~$55.7bn, FY27 net capex guided ~$70bn, ~$130bn of debt, a
  $23.7bn free-cash-flow deficit. That is a balance-sheet outcome I cannot handicap two
  sessions before the print, and 0 insider buys against 12 sells does not help.
- **AVAV** (09-09 amc): 147.21, **-51.4%** off the high, below the 20-day (166.19) and 50-day
  (158.80), ATR 5.49%. A falling knife into a print is a coin flip, not an idea.
- **RH** (09-09): 146.61, -35.4% off the high. The one genuine positive is CEO Alberini's
  three open-market buys on 2026-06-29 totalling ~$1.83m at ~160 — but that is one buyer, the
  stock is 9% below where he bought, and a housing-linked retailer with the 10-year at 4.768%
  reporting in three sessions is not something to underwrite this morning.

## [06:28 ET] REJECTED — an intraday index trade on the payroll print
IWM is the tempting one: **295.19, below both its 20-day (299.14) and 50-day (297.07)** while
SPY sits 0.8% off its high above both, and fetched relative strength has IWM **-1.97% vs SPY
over one month**. Small caps are the highest-beta expression of the hike being priced out, so
a weak print should move them most. Two reasons it does not publish:
1. It is a directional bet on a number nobody has yet, dressed as a setup.
2. **Futures cannot be priced this run** — Yahoo 429s on RTY=F/ES=F, finnhub returns zeros,
   and stooq has no contract. The universe rules prefer /M2KU6 over IWM here, and I will not
   write an entry, target and stop for a contract whose price I could not fetch.

## [06:31 ET] NEW IDEA — GDX BUY @ 97.00 — captured
The one new long besides the XLE amendment, and the reasoning is the odd part of the tape.
- On 2026-09-03 the market cut September hike odds from 63% to 50% **and gold rose 2.3%**,
  with GLD closing 410.22 (+1.85%). Bullion bid while the policy argument is about *tightening*
  is a fiscal/term-premium bid, not a real-rates one — the 30-year is still 5.2433%.
- Fetched GDX: 101.49, ATR14 3.9478 (3.89%), SMA20 96.3835, SMA50 83.942, SMA200 89.7478,
  200-day range 69.74-117.175. GDX is **13.4% below its range high while GLD is 11.4% below
  its own** — the miners have not caught the metal up, and they carry the operating leverage.
- Entry **97.00** on the 20-day, inside the 09-01/09-02 pullback that already held (lows 94.49
  and 96.30). Stop **89.50**, below the 08-17/08-18 lows of 90.315 and 88.775 — 7.50 away,
  **1.90 ATR**, clearing the 1.8 ATR ETF floor. Target **117.00** just under the range high.
  R:R **2.67**, win probability 0.42 against a 27.1% baseline — a 15 point claimed edge.
- `wait: true`: the limit stays working through the 08:30 print rather than entering at 101.49.
  A hot payroll number is what produces the pullback the order wants.
- **Correlation declared:** this is a second position on gold alongside the open GLD long. Two
  of a maximum three on one driver, sized at 2%, and stated in `key_risk` rather than hidden.

## [06:31 ET] WATCHLIST, NOT A TRADE — bitcoin has broken out and I am not chasing it
Fetched from CoinGecko (90 and 60 day daily series, cross-checked against Coinbase spot):
- BTC **80,846-80,902 today, +4.13% in 24h**, a new 60-day high. 30-day low **62,844**, so
  bitcoin is **+29% in a month**. ETH 2,517.56 (+5.06%), SOL 103.66 (+3.45%) — broad, not a
  single-venue print. Two weeks of consolidation between 77,297 and 80,268 (08-23 to 09-03)
  broke this morning.
- Mean absolute daily close-to-close move over the last 30 days is **1,125 (1.39%)**; the
  median is 557. Note that this is derived from daily closes, **not a fetched ATR** — the
  CoinGecko series carries no intraday high/low, so a true range is unavailable.
- The setup I would want: pullback to **78,000** (the broken consolidation top), stop below
  **72,900**, target **92,000** (bitcoin traded above 93,000 at the start of 2026, which is
  this report's own prior-thesis level).
- **Three reasons it is not published today.**
  1. I cannot compute a real ATR for it, and a crypto swing needs a 2.5 ATR stop. Publishing
     levels on an estimated volatility measure is the kind of number this report does not write.
  2. This report was short bitcoin at 64,340 two weeks ago. Turning long the same morning the
     short is cancelled, after a 26% adverse move, is whipsaw rather than analysis. If the
     retest comes, it will still be there tomorrow with better information.
  3. Entry would be into the 08:30 print at the top of a +4% day.
- Flagged for tomorrow's run: **if BTC retests 78,000 and holds, this is a real setup.**

## [06:31 ET] CORRELATION CHECK on what was captured
New directional risk added today is small and deliberately so:
- **XLE** (energy, amended, `wait`) and **GDX** (gold miners, new, `wait`) — one commodity
  each, different drivers, both conditional on an event that has not happened yet.
- Everything else captured **reduces** risk: LULU close, RARE close, TLT long close, SPY short
  cancelled, BTC spot cancelled, /MBTU6 short cancelled.
- Driver concentration after today: gold 2 (GLD open + GDX), energy 1 (XLE), uranium 1 (CCJ),
  rates 1 (TLT short), consumer/apparel 1 (NKE), housing 1 (BCC), biotech 1 (SVRA). Nothing
  is at the 3-idea cap.

## [06:32 ET] MACRO ADDENDUM — the dollar, and a source disagreement worth flagging
- **The dollar is at its lowest since May**, and yen strength is doing part of the work in
  easing inflation worries. Nikkei +1.2%. WTI quoted around **90.72**, gold around **4,530**
  — the latter cross-checks GLD's 410.22 close at a plausible NAV factor.
  — source: https://marketrebellion.com/news/daily-iv-report/pre-market-iv-report-september-4-2026/
- A weakening dollar with gold at 4,530 and hike odds still near 50% is the same debasement
  signal the GDX idea rests on, arrived at from a different direction. Good confirmation.
- **Source disagreement, stated rather than smoothed over:** CME FedWatch is quoted at a
  **54%** chance of a September hike this morning; the fed funds futures figure reported after
  Waller was **50.4%**; **Kalshi's own contracts imply 45%** (H25 43 + H26 2, both fetched
  from the exchange trades endpoint). The three do not agree and I am not going to average
  them into a single number. The honest range is **45-54%**, which is a coin flip on every
  measure, and that is all any idea in this report leans on.

## [06:32 ET] RESEARCH COMPLETE
- **candidates: 8** — and the shape of them is the story of the day. Six of the eight reduce
  risk and only two add any:
  - **Closes:** LULU (thesis broken by the Q2 print), RARE (restated), TLT long (resolving a
    simultaneous long and short in the same ETF).
  - **Cancellations:** SPY short (about to fill by accident, stop under the ATR floor),
    /MBTU6 short and BTC spot sell (bitcoin is 21-24% through both invalidations and the
    pipeline could not see it).
  - **New/amended longs:** XLE (stop widened, target cut, OPEC+ 09-06 catalyst, `wait`) and
    GDX (new, `wait`, entry on the 20-day).
- Nothing intraday was manufactured beyond the two exits, and nothing was published on the
  08:30 payroll print itself. That is deliberate: front-running a number nobody has is not
  edge, and the report already has plenty of exposure to how it resolves.
- **coverage gaps:**
  - **Futures cannot be priced this run at all** — Yahoo 429s, finnhub returns zeros for
    RTY=F/ES=F, stooq has no contract. Any /MES, /MNQ, /M2K or /MGC idea would have required a
    fabricated level, so none was written. This also means the open `/MBTU6` row could not be
    marked to market except through spot bitcoin.
  - **Index, VIX, DXY and WTI levels** unavailable from `market_data.py macro` for the same
    reason; the equity and ETF book was covered by finnhub and rates by FRED.
  - **Options-implied moves unavailable** — `market_data.py implied` returns HTTP 401 from
    the Yahoo options endpoint, so no idea today carries the "is the target inside what the
    market prices" check.
  - **Short interest unavailable** — api.nasdaq.com read-timed out.
  - Small and micro caps got less time than they deserve. MAX was the only one worked through
    to levels and it failed the R:R floor; the 09-07 to 09-11 small-cap earnings list
    (ODD, TTAN, IBEX, ANAB, MCFT, LOVE, SHOE, AVO) was read but not researched.
- **sources that failed:** Yahoo Finance (HTTP 429 on every request, 401 on options),
  api.nasdaq.com (read timeout on short interest), stooq (404 on index and futures symbols),
  Kalshi `/markets` endpoint (returns null prices — the `/markets/trades` endpoint works and
  is what the event-contract marks came from), cnbc.com via WebFetch (HTTP 403).
- **for tomorrow:** bitcoin at 78,000 on a retest of the broken 77.3k-80.3k consolidation is a
  real setup and today's data could not support levels for it. And the crypto price-refresh
  failure that hid a 21% blown stop for two weeks is a pipeline bug, not a research gap.

## [06:35 ET] SMALL-CAP SWEEP — 11 names with prints inside 5 sessions, none published
Closing the gap I flagged above. Screened the 09-08 to 09-11 small-cap earnings list on
fetched history; ADV is 30-day average dollar volume.

| | close | ATR% | vs 20d / 50d | off high | ADV$ | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| IBEX | 39.41 | 2.97 | above / above | **-1.4%** | 4.0m | uptrend at the high, into a 09-10 print |
| PPIH | 27.58 | 3.63 | above / above | -24.9% | 2.1m | best story, still rejected — below |
| ANAB | 57.46 | 4.17 | at / at | -20.6% | 24.1m | no readout found inside the horizon |
| AVO | 12.57 | 2.82 | below / below | -19.1% | 8.0m | consumer, and below both averages |
| MCFT | 23.33 | 3.87 | below / below | -18.0% | 4.1m | boats into a weak consumer |
| LOVE | 15.95 | 3.93 | below / below | -17.1% | 3.1m | same |
| SHOE | 13.65 | 4.94 | below / below | -36.8% | 9.1m | footwear — see the category note above |
| ODD | 14.13 | 6.39 | above / below | -58.5% | 10.8m | -58% and under the 50-day |
| RFIL | 10.18 | 5.98 | below / below | -54.4% | 2.1m | same |
| LSAK | 4.61 | 3.47 | below / below | -16.8% | **0.46m** | **fails the $500k liquidity floor** |
| NNOX | 0.71 | 8.91 | below / below | -76.7% | 0.74m | **under $1 — excluded by universe rules** |

### [06:35 ET] REJECTED — PPIH — the one that nearly made it
The story is real: FY2025 was a record (net sales +33%, EPS 2.09), and Q1 FY2026 backlog rose
**12% to $136.5m** from $121.6m, helped by **newly awarded AI data-centre work** alongside
infrastructure, energy and water bidding. Q2 reports **2026-09-09 before the open**, consensus
EPS 0.561 on ~$52.0m revenue (fetched calendar). Market cap ~$220m, so it would size at 1%.
— sources: https://www.businesswire.com/news/home/20260608028241/en/Perma-Pipe-International-Holdings-Inc.-Announces-First-Quarter-2026-Financial-Results ,
  https://www.businesswire.com/news/home/20260416587944/en/Perma-Pipe-International-Holdings-Inc.-Announces-Record-Fourth-Quarter-and-Fiscal-2025-Results-Net-Sales-Increase-33-and-Net-Income-Grows-89

Three reasons it does not publish, and the first is the one that matters:
1. **The stop is fiction into this print.** Fetched `avg_volume_30d` is **77,032 shares** —
   about $2.1m a day. A micro cap that misses gaps through a stop rather than trading to it.
   That is not a hypothetical: **RARE cost this report 41% on 09-03 when a 22.90 stop was
   gapped by 9.6 ATR**, and PPIH is a twentieth of RARE's liquidity.
2. **The earnings trend is against it.** Q1 net sales rose 7.5% to $50.3m but **EPS fell to
   0.22 from 0.61** on weaker gross margins, higher operating costs, higher interest and a
   higher tax rate. Consensus asks for 0.561 on Monday — a return to the prior-year level that
   the last quarter gave no evidence for.
3. **Its growth region is now a war zone.** MENA demand is the driver, and the company's own
   Q1 filing flags regional security risk and operational uncertainty. US strikes on Iranian
   targets around the Strait of Hormuz on 2026-09-01 raise that materially. It is the same
   fact as the XLE thesis, pointed the other way.
Also: **zero insider transactions in six months** — no buys and no sells — so there is no
positioning read at all. Watchlist through the print; a beat with backlog above $140m and the
stock holding 27 is a cleaner setup on 09-10 than a guess on 09-08.

### [06:35 ET] REJECTED — IBEX — right trend, wrong moment
39.41, **1.43%** off its 150-day high, above the 20-day (36.88) and 50-day (35.03), ATR 2.97%,
ADV $4.0m. This is genuine leadership and the only small cap on the list making highs. It
still does not publish: earnings **09-10 after the close**, and buying a small cap at its high
three sessions before a print is taking the binary with none of the cushion. If it reports and
holds, it is a better idea on 09-11 than it is today.

## [06:35 ET] HONEST SUMMARY OF THE DAY'S SHAPE
Two new longs is a thin day and it should be read as one. The reason is not a quiet tape — it
is that most of today's available edge was in the book already and pointed the wrong way:
- a long whose company guided FY EPS down 27% overnight (LULU),
- a long already down 41% on a gapped stop (RARE),
- an ETF held long and short simultaneously (TLT),
- a short about to fill by accident, minutes before a payroll print (SPY),
- and two bitcoin shorts 21-24% through their invalidations that the pipeline could not see.
Cleaning that up **is** the day's work, and it is worth more than five manufactured longs.
What was added is deliberately conditional: both XLE and GDX carry `wait: true` and neither
is live until an event that has not happened yet.

## [06:36 ET] CONVICTION AUDIT — all 8 candidates re-scored against the evidence table
I had scored conviction as the *count* of distinct evidence kinds rather than the table in
`config/strategy.md` (1 kind = 2, two = 3, three = 4, four or more = 5), so seven of eight
were a point low. Corrected lines appended — `candidates.jsonl` is a log and synthesis takes
the last entry per symbol, so the file now holds 15 lines resolving to **8 distinct symbols**.

Two of the corrections went the other way, by removing an evidence entry rather than raising
a score, and both are worth stating:
- **XLE** carried a `counter_argument_answered` entry whose answer to the EIA's $69/bbl 2027
  forecast was "sized at 2% with a time stop". That is position management, not evidence, and
  the kind explicitly requires the case against to be *answered with evidence rather than
  asserted away*. Entry removed; the EIA forecast stays in `key_risk`, which is where it was
  always doing its real work. Conviction stays **4** on three kinds.
- **GDX** carried a `positioning` entry comparing how far GDX and GLD each sit below their
  highs. It would have qualified and taken the score to 5 — and with it the 4-5% sizing tier,
  which is more gold than this book should carry alongside the open GLD long. Removed; the
  observation stays in the thesis. Conviction **4**, sized **2%**.

Final scores, all now matching their evidence: LULU 5 (close), RARE 4 (close), TLT 4 (close),
/MBTU6 4 (cancel), XLE 4, GDX 4, SPY 3 (cancel), BTC 3 (cancel).
