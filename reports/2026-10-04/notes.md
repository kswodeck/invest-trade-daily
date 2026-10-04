# Research log — 2026-10-04

## [06:01 ET] MACRO — Sunday run; equities/futures closed, crypto 24/7
Regime read from fetched data (FRED + CoinGecko):

- **US10Y 5.24%** (prev 5.29), date 2026-10-01 — source: https://fred.stlouisfed.org/series/DGS10
- **US2Y 4.78%** (prev 4.88), 2026-10-01 — source: https://fred.stlouisfed.org/series/DGS2
- **Fed funds effective 3.88%**, 2026-10-01 — source: https://fred.stlouisfed.org/series/DFF
- **10y-2y +0.45** (prev 0.46), 2026-10-02 — source: https://fred.stlouisfed.org/series/T10Y2Y
- **Unemployment 4.2%** (prev 4.1%), Sep 2026 — rising — source: https://fred.stlouisfed.org/series/UNRATE
- **CPIAUCSL 334.131** Aug-2026 vs 332.813 Jul = **+0.40% MoM** (~4.9% annualised) — source: https://fred.stlouisfed.org/series/CPIAUCSL
- TLT proxy `bonds_20y` 77.48, -0.30%, prev close 2026-10-02 (market closed)

**The single dominant fact: fed funds 3.88% against a 5.24% 10y is a 136bp
positive spread with the Fed easing.** The long end is refusing the cuts while
core prices run ~0.4% MoM and unemployment drifts up. That is a
stagflation/fiscal-dominance tape, not a soft-landing one. It argues for: hard
assets, short long-duration bonds and bond-proxy equities, and against anything
whose valuation is a discounted-cash-flow story.

Note this is already the book's existing bias (XLU short, TLT short pending,
IYR short pending, GDX long). **Correlation cap applies** — do not add a fourth
expression of "long rates rise".

### Source failures (for data_quality_notes)
- Yahoo Finance returning **HTTP 429 on every index/equity call** this run:
  spx, ndx, dow, russell2000, vix, es/nq futures, DXY, us10y, gold, wti all
  `ok: false`. Finnhub refuses indices ("subscription required for CFD
  indices"), stooq 404s on `^` symbols, no AlphaVantage key.
- Consequence: **no VIX, no DXY, no spot gold/WTI print this run.** Equity level
  work depends on whether `history` finds a non-Yahoo path — testing next.

## [06:02 ET] CRYPTO — prices live, 24/7 venue, so this is where Sunday risk can actually be taken
source: https://www.coingecko.com/ (asof 2026-10-04T10:01Z)

| Coin | Price | 24h | 24h volume |
| --- | --- | --- | --- |
| BTC | 85,226 | +0.77% | $14.9B |
| ETH | 2,701.14 | +0.78% | $4.68B |
| SOL | 121.30 | +1.66% | $1.69B |
| XRP | 1.50 | +1.08% | $1.04B |
| LTC | 70.41 | +2.57% | $297M |
| LINK | 14.12 | +1.23% | $228M |
| DOGE | 0.0934 | +0.68% | $372M |
| ADA | 0.2452 | +0.40% | $236M |
| AVAX | 11.01 | +0.45% | $260M |

Quiet, uniformly mildly green weekend tape — no dislocation to trade off the
24h move alone. Need trend/level context before any crypto idea.

## [06:02 ET] PRIOR-BOOK FLAG — stale pending short to withdraw
`/MBTU6` SHORT @ 64,340 has sat unfilled since 2026-08-18 with BTC now 85,226.
A resting short 25% below spot is not a live order, and the U6 contract month is
long past its window. Flagging for an explicit withdraw rather than leaving it
on the page.

## [06:05 ET] TOOL BUG — `market_data.py events` is silently blind
Two independent faults, both worth fixing before the next run:

1. **Kalshi renamed its price fields.** The API now returns `yes_bid_dollars`,
   `yes_ask_dollars`, `last_price_dollars`, `volume_fp`, `open_interest_fp` (and
   prices as decimal dollar strings, e.g. `"0.1300"`). `events()` at
   `scripts/market_data.py:770` still reads `yes_bid`/`yes_ask`/`last_price`/
   `volume`/`open_interest`, so **every event contract comes back with null
   prices**. Confirmed by dumping a full market object.
2. **There is no server-side search.** `events()` pulls `limit*5` (max 200)
   open markets unfiltered and greps titles client-side. Kalshi has tens of
   thousands of open markets and the first 200 are all NFL, so **every topic
   search returns count 0** — tested Fed, CPI, inflation, Bitcoin, recession,
   unemployment, government, shutdown, GDP. All zero. The fix is to pass
   `series_ticker`.

Worked around this run by querying
`https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=<S>` directly
and parsing the `*_dollars` fields. Note the old host `trading-api.kalshi.com`
now 401s with a migration notice. **The source is healthy; the client is wrong.**

## [06:06 ET] CPI — the Oct 14 print, from the actual index history
BLS API v1, series CUSR0000SA0 (headline SA), CUUR0000SA0 (headline NSA),
CUSR0000SA0L1E (core SA) — source: https://api.bls.gov/publicAPI/v1/timeseries/data/

Headline SA index: Mar 330.293, Apr 332.407, May 333.979, Jun 332.568,
Jul 332.813, Aug 334.131. So **SA MoM: Mar +0.86%, Apr +0.64%, May +0.47%,
Jun -0.42%, Jul +0.07%, Aug +0.40%**.
Core SA: Jun -0.02%, Jul +0.22%, Aug +0.29% — core is running ~0.25%/mo and
gently accelerating. Headline NSA Aug 334.980 vs Aug-2025 323.976 = **+3.40% YoY**.
Sep-2025 NSA base = 324.800.

Kalshi Sep-2026 markets, all closing 2026-10-14 (= the release date, which is how
the catalyst date is verified rather than remembered):

| Market | Strike | yes bid/ask | volume | OI |
| --- | --- | --- | --- | --- |
| KXCPI-26SEP | >0.4% | 89/90 | 139,857 | 67,304 |
| KXCPI-26SEP | >0.5% | 58/60 | 145,617 | 105,011 |
| KXCPI-26SEP | >0.6% | 17/18 | 100,128 | 24,874 |
| KXCPI-26SEP | >0.7% | 1/3 | 14,384 | 10,281 |
| KXCPIYOY-26SEP | >3.5% | 82/84 | 76,607 | 42,856 |
| KXCPIYOY-26SEP | >3.6% | 49/50 | 191,552 | 120,901 |
| KXCPIYOY-26SEP | >3.7% | 16/19 | 52,534 | 26,443 |

**Coherence check, and it passes.** Working the YoY back through the Sep-2025 NSA
base of 324.800: a 3.7% YoY needs NSA Sep-2026 = 336.818, i.e. NSA MoM +0.549%;
September's NSA-minus-SA wedge was -0.04pp in 2025 (NSA +0.254% vs SA +0.295%),
so that maps to SA MoM ~0.59%. The MoM and YoY ladders imply **the same**
distribution. There is no cross-market arbitrage here, and the pricing is the
work of someone who has done this arithmetic.

**REJECTED — the CPI MoM "it can't be that hot" fade.** My first read was that
58% on >0.5% MoM looked rich against a 3-month SA run rate of ~+0.02%/mo, which
would have made NO at 42 a large edge. It is not, and the reason is energy: USO
has gone from a 150-day low of 83.20 to 147.37, **+77%**, so a large positive
energy contribution on top of ~0.29% core is exactly what a 0.6% headline needs.
The market is pricing the oil pass-through correctly and I have no edge fading it.
Recording this rather than trading it — the ~145k-contract strike is not where a
keyless research run finds free money.

**Open question that gates any CPI trade: threshold semantics.** BLS publishes
MoM and YoY to one decimal. Whether "Above 0.5%" resolves on the rounded print
(so 0.5% published = No) or on an unrounded computation changes the modal
expectation from 0.5% to 0.6% and shifts every number above. Not yet verified —
fetching `rules_primary` next. **Do not capture a CPI candidate until this is
settled**; the whole edge would be a rounding convention.

## [06:07 ET] ENERGY — the engine under the whole macro picture
- **USO 147.37** (2026-10-02 close), ATR14 5.98 (4.06%), sma20 150.70, sma50 137.37,
  150-day range **83.20-163.35**, -9.8% off high, **+77.1% off low**.
  source: https://www.nasdaq.com/market-activity/funds-and-etfs/uso/historical
- **XLE 62.82**, ATR14 1.2505 (1.99%), sma20 63.47, sma50 62.12,
  150-day range 52.62-66.17, -5.1% off high, **+19.4% off low**. avg$vol 30d $2.01B.
  source: https://www.nasdaq.com/market-activity/funds-and-etfs/xle/historical

Crude up 77% off the low; the energy equity complex up 19%. That gap is the most
interesting single number this run. Caveat carried into the thesis: USO is a
front-month roll vehicle, so some of 77% is contango, not spot.

This also explains the bond market — fed funds 3.88% while an oil-driven headline
CPI prints ~3.7% YoY is why the 10y sits at 5.24% refusing the cuts.

## [06:08 ET] POSITION UPDATE — XLE — opened 2026-08-15 @ 63.90, now 62.82, -1.7%
- decision: **hold, levels unchanged** (target 70.50, stop 60.80)
- why: crude/equity divergence above; XLE still on its 50-day mean 62.12
- explicitly NOT adding — price is below entry, add only on a close over 63.47
- R:R (70.5-63.9)/(63.9-60.8) = 2.13 clears the 2.0 swing floor; stop is 2.48 ATR
  below entry, clearing the 1.8 ATR ETF floor
- action: **captured** via add_candidate.py (conviction 3, 2 evidence kinds)

## [06:08 ET] CORRELATION CAP — noted before hunting, to stop myself
The open book is already **three expressions of one "long rates rise" bet**:
`XLU` SELL_SHORT (open), `TLT` SELL_SHORT (pending 79.9), `IYR` SELL_SHORT
(pending 97.8). `config/strategy.md` caps the same driver at 3. However good the
5.24%-10y story looks today, **a fourth rates-up idea must not be captured** —
that includes the tempting long-regional-banks steepener, which is the same bet
wearing a different hat. Logged so the synthesis phase can see it was a decision,
not an oversight.

## [06:16 ET] REGIME CORRECTION — I had the Fed backwards, and it changes everything
My 06:01 macro block read "the Fed is easing and the long end is refusing the
cuts". **That was wrong, and the error came from reading FRED alone.** DFF at
3.88% flat month-on-month looked like a pause after cuts. It is not.

- **The Fed hiked last month (September 2026)** and **16 of 19 FOMC members
  project at least one more hike in 2026** — source:
  https://finance.yahoo.com/economy/policy/article/fed-officials-forecasts-project-one-more-rate-hike-to-come-in-2026-183856618.html
- **Chair is Kevin Warsh**: "Inflation is too high and has been for too long",
  predominant focus on the price-stability side of the mandate.
- **Vice Chair Jefferson and NY Fed's Williams want more data** — hence skip
  October, act in December — source:
  https://www.bnnbloomberg.ca/business/economics/2026/10/02/fed-may-skip-october-but-pull-us-rate-hike-trigger-in-december/
- JPMorgan's chief US economist: "one more hike at the December meeting, in line
  with the revised median FOMC expectations".
- The oil move is a **US-Iran war supply shock**, not demand — and the 10y
  touched **5.33%**, the 30y **5.67%**, multi-decade highs, before easing on a
  soft jobs report Friday 2026-10-02 — source:
  https://www.troweprice.com/personal-investing/resources/insights/global-markets-weekly-update.html

Corrected regime: **an openly hawkish Fed in a live hiking cycle, into a
war-driven oil shock pushing headline CPI from 3.4% toward 3.7%, with the long
end at multi-decade highs and unemployment nonetheless drifting up (4.1 to 4.2).**
The Kalshi ladder is the cleanest statement of it: zero probability of a cut at
any meeting out to March 2027.

| Meeting | Hold | Hike 25bp | Volume (hike) |
| --- | --- | --- | --- |
| Oct 28 2026 | 82/83 | **17/18** | 2,415,521 |
| Dec 9 2026 | 25/28 | **70/71** | 188,953 |
| Jan 27 2027 | 60/63 | 32/37 | 55,710 |
| Mar 17 2027 | 41/50 | 50/55 | 18,155 |
source: https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXFEDDECISION

## [06:16 ET] REJECTED — KXFEDDECISION-26DEC-H25 NO @ 30 — killed by falsification
This was my best idea of the run for about ten minutes and it was wrong.

The setup looked excellent: NO at 30 cents is 2.33:1, break-even 30%, and I had
P(no December hike) at 45-50% on four arguments — the Fed would have to reverse
its own cuts, supply shocks are looked through, unemployment is rising, and an
Iran de-escalation would collapse headline CPI. A 15-20 point edge on a liquid
market.

**Three of those four arguments rested on a false premise.** The Fed is not
easing, so there is no reversal to be embarrassed by; it hiked in September and
its own dot plot projects another. 16 of 19 members, the Chair, and the sell
side all point the same way, and the two officials arguing for patience are
arguing for *December rather than October*, not against hiking. The market's 70%
is not a crowd error, it is the dot plot priced correctly, and if anything 70%
is generous to my side.

Lesson for the file: **an event-contract edge that comes from my own macro
narrative rather than from a number the market cannot see is not an edge.** The
falsification step earned its 10% of the budget today.

## [06:16 ET] REJECTED — other event contracts screened, none captured
- **KXFEDDECISION-26OCT-H0 YES @ 83** — probably a genuinely correct 83-90%
  read, but the payoff is 17 on 83 risked = **0.21:1**, and break-even at 83
  cents *is* 83%. High-probability contracts structurally cannot clear the 2.0
  R:R floor. Correct to skip, not a near miss.
- **KXFEDDECISION-26OCT-H25 YES @ 18** — 4.56:1, break-even 18%. But Jefferson
  and Williams have publicly signalled patience and the Sept CPI lands Oct 14,
  before the Oct 28 meeting, so the market has the sequencing right. No stated
  disagreement, so no trade.
- **KXU3-26OCT-T4.2 YES @ 30** (October U-3 above 4.2%, resolves on the Nov 6
  release). Trend genuinely supports it — 4.1 to 4.2 with a soft Oct 2 print and
  a hiking Fed — and I would put P(4.3%+) near 35% against a 30% break-even. But
  the quote is **26/30 on a 28-cent contract, a 14% spread**, against 7,354
  contracts of volume. The spread eats a 5-point edge. **Rejected on
  transaction cost, not on thesis** — worth revisiting if it tightens.
- **KXRECSSNBER-27 YES @ 17** — a 2027 recession at 17% is close to the
  unconditional base rate; no edge, and Jan-2028 resolution is dead capital.
- **Headline CPI ladder** — see the 06:06 block. Internally coherent, correctly
  priced for the oil pass-through, and the key strike carries 145k contracts.
  Rules now verified: the market's `rules_primary` says "increases by more than 0.5%
  **(single-decimal)**" and the expiration value is "the single-decimal value
  published at the Source Agency", so these resolve on the **rounded** print.
  That settles the semantics question from 06:06: "Above 0.5%" needs a published
  0.6%, so the market's modal expectation is **0.6% MoM / 3.7% YoY**, not
  0.5%/3.6%. Coherent either way, and no edge either way.

**Net: zero event contracts captured despite this being a Sunday and the lane
being explicitly wanted.** That is the honest outcome — the macro ladder is
liquid and correctly priced, and the one disagreement I could construct was built
on a factual error about Fed policy. Noting it so synthesis does not read the
absence as a gap in coverage.

## [06:16 ET] VENUE CHECK — Robinhood does carry Fed decision contracts
Confirmed Robinhood lists Fed rate decision event contracts for Oct 2026, Dec
2026, Jan 2027, Mar 2027 and beyond, Kalshi/ForecastEx routed, $1 per winning
contract — sources:
https://robinhood.com/us/en/prediction-markets/economics/fed-decision/ ,
https://robinhood.com/us/en/prediction-markets/
Not acted on today, but the availability question is settled for future runs.

## [06:25 ET] THE FINDING OF THIS RUN — the book has made one mistake nine times
Screening across sectors produced the same picture everywhere, and it reframes
the track record from bad luck into a single repeated error.

Everything screened today that is **at or within a few percent of its 150-day
low**, all below both their 20- and 50-day means:

| Sector | Names (% off 150-day high / % off low) |
| --- | --- |
| Defense | NOC -38.2/+1.7, LHX -37.6/+1.1, HII -41.6/+4.6, LDOS -35.0/+19.1, LMT -27.0/+3.8, RTX -18.6/+8.1, GD -17.5/+7.6 |
| Staples | MKC -36.9/+3.3, STZ -33.0/+1.2, PEP -25.8/**+0.6**, LW -21.7/+15.9, KHC -21.0/+5.5 |
| Discretionary | LULU -47.3/+1.1, NKE -45.0/+5.9, LCII -40.1/+1.4, BCC -15.2/+15.4 |
| Materials ex-copper | AA -50.3/**+2.3**, MOS -34.7/+6.4, CLF -24.8, CF -19.0, NUE -14.2 |
| Uranium / precious | CCJ -35.1/+2.4, GDX -25.1 |

Meanwhile **SPY is 769.64, only -1.25% off its 779.37 high**, and NVDA led the
Nasdaq to an intraday record on 2026-10-01. Copper (FCX -10.2%, SCCO -7.2%) and
refining (DINO -4.2%, +125% off its low) are near highs.

**This is one of the narrowest tapes imaginable: the index is at a record while
the median stock outside AI and copper is at a 52-week low.** It is internally
coherent — a 5.24-5.33% 10y plus a hiking Fed plus 3.7% headline inflation
destroys anything that is a bond proxy or a margin-squeezed price-taker, and
leaves self-funded secular capex untouched.

Now read the open book against it. Every losing position is the same trade:
NKE -15.3%, LULU -17.9%, LCII -11.9%, CCJ -10.3%, SVRA -10.1%, BCC -7.4%,
KHC -3.5%, GDX -3.8% — **a de-rated name bought on a value thesis.** The stock
line of the track record is 0 for 7 with an average of -5.4%. That is not seven
bad picks, it is **one mistake made nine times**: buying things that are cheap in
a regime that is systematically repricing cheapness downward. CAG stopped out
2026-09-28 and KHC is the same trade still open.

**So the bar for any new de-rated-value long is raised sharply for the rest of
this run, and I captured none.** The one new long captured today (FCX) is in
something *working* and near its high, entered at a tested shelf — deliberately
the opposite shape of trade. This is the "raise the bar for a losing category"
instruction in prior_context.md being applied rather than noted.

Caveat kept honest: **12 closed trades is under the ~15 the instructions call
noise**, so this is a regime argument supported by a cross-sectional screen, not
a conclusion drawn from the sample size. The screen is the evidence; the record
is corroboration.

## [06:25 ET] REJECTED — the entire defense sector, despite an active war
NOC, LHX, HII, LMT, RTX, GD, LDOS all 17-42% off their highs during a live
US-Iran conflict. That is counterintuitive enough to demand a cause, and there
are three real ones — this is a value trap, not an opportunity:

1. **De-escalation is being priced.** Reuters reported Iran offered to reopen
   the Strait of Hormuz within seven days if the US eased military pressure;
   defence names fell and oil slid on it, and a US-Iran interim deal did the same
   — source: https://247wallst.com/investing/2026/09/22/defense-stocks-fall-while-oil-slides-on-hormuz-reopening-report-lockheed-martin-and-rtx-drop-3-boeing-dips/
2. **The budget is worse than the headline.** The FY27 request is a record
   $1.5T, but no congressional bill accounted for the $350B reconciliation
   portion, so the markups are an effective $350B cut with procurement and R&D
   taking the worst of it. The Pentagon **began FY27 on a stopgap CR** on
   2026-10-01, the Senate rejected a $1B advance-procurement anomaly for a
   $17.5B Navy program, and the CR rejected the fast-track exceptions to restock
   PAC-3, Tomahawk, AMRAAM and SM-3 — the exact munitions the Middle East
   operations depleted — sources:
   https://news.clearancejobs.com/2026/10/01/the-pentagon-starts-fiscal-2027-on-a-stopgap-heres-how-it-affects-defense-jobs/ ,
   https://dsm.forecastinternational.com/2026/08/10/how-congress-is-reshaping-the-pentagons-fy27-spending-plans/
3. **Company-level cash burn.** LMT free cash flow swung to -$291M from +$955M
   a year earlier; NOC guided full-year revenue and EPS at or below the low end
   — source: https://www.tikr.com/blog/lockheed-martin-has-fallen-nearly-25-from-its-2026-high-is-it-finally-time-to-buy

A war does not fund a contractor whose appropriation is frozen by a continuing
resolution. **Note for the record: HII was ranked #1 on the 2026-10-02 report and
is now -41.6% off its high** — it does not appear in today's open-position or
awaiting-entry tables, which is worth a look by whoever owns the tracker.

## [06:25 ET] REJECTED — staples into earnings, on the track record
MKC (reports 2026-10-05), STZ (10-06 amc), LW (10-06), PEP (10-08 bmo) are all
at 150-day lows with dated catalysts inside the horizon — on the surface exactly
what this report hunts. **Rejected as a category.** Staples are a triple squeeze
right now: oil +77% inflating input costs, no pricing power left after three
years of elasticity damage, and a bond-proxy multiple against a 5.3% 10y. This
report has already paid for that lesson twice — CAG stopped out 2026-09-28 and
KHC sits open at -3.5%, below both means. Buying a third is the nine-times
mistake above.

## [06:25 ET] REJECTED — SCCO, and FCX nearly went the same way
SCCO 205.54 is the better chart (above both means, +35.8% off its low) but a
2.0 ATR stop (6.79 ATR, so 13.6 points) from any entry near the 199-200 mean
needs a 227 target against a 221.50 range high — **the 2:1 floor is unreachable
without demanding a new high.** That is the floor working as designed on a name
near its high, and the same arithmetic nearly killed FCX: at the 72.04 market, a
2 ATR stop needs a 81.80 target against an 80.24 high. FCX only became publishable
because it has a genuine shelf 5.3% lower (67.01/67.80/68.20, three tests) that
puts the target back inside the range. **FCX is captured as a resting limit that
may well never fill, and that is stated in the entry condition rather than
papered over.**

A long_term FCX framing was also considered and dropped: clearing the 2.5 floor
needs a defended target near 110, and the only honest method — copper-price
leverage on annual pounds produced — needs a production figure I did not fetch.
**Not published rather than estimated.**

## [06:25 ET] POSITION UPDATE — DINO — opened 2026-08-22 @ 107.50, now 113.36, +5.5%
- decision: **hold, levels unchanged**, and deliberately NOT trailing the stop
- 113.36, -4.2% off the 118.39 high, above the 20-day 109.15 and 50-day 99.37
- I started to raise the stop from 97.75 to ~102 and stopped: the existing stop is
  already only 1.85 ATR from the 107.50 entry (9.75 / 5.26), and walking it to 102
  would cut that to **1.05 ATR** while lifting the printed ratio from 2.10 to 3.73.
  That is the KRE pattern CLAUDE.md names explicitly — a better-looking ratio for a
  strictly worse trade. Respecting the ATR floor means accepting that I cannot lock
  a profit here, and that is the correct cost.
- not captured as a candidate, because nothing changed

## [06:25 ET] POSITION UPDATE — held with no change, so not captured
Per the skill, only positions where something changed are emitted. These were
reviewed and left alone:
- **XLU** SELL_SHORT 39.83 (entry 39.60, stop 40.95, target 36.80) — working; price
  under both means, 2.0% off its 150-day low, and a hiking Fed is pure headwind for
  a bond proxy. Stop is 2.0 ATR above. Hold. Also recommended 5x in 10 days, so it
  must not be re-pitched.
- **SNX** 278.37, +7.1%, above both means, target 296.47 only 6.5% away. Hold.
- **EEM** 67.67, +3.2%, above both means. Hold.
- **PFE** 27.80, +0.7%, above the 50-day, -4.8% off its high. Hold.
- **BCC** 74.99, -7.4%, below both means but +15.4% off its low — rate-exposed
  building products, the same regime problem as LCII but not yet at lows. **Watch,
  invalidate on a close below 65.00.**
- **KHC** 22.19, -3.5%, below both means. The staples argument above says close it;
  it is left open because it is 14 days old and the loss is small. **Explicit
  invalidation: a close below the 150-day low of 21.04 closes it.** Flagged rather
  than acted on, deliberately — I did not want a fifth exit on a same-day sector call.
- **NKE / LULU** — exits were already issued 2026-09-08 and both show as open SELL
  rows at +11.8% and +6.1%. Those are tracker artifacts of the already-issued exit,
  not new decisions. Not re-issued.

## [06:25 ET] FLAG for synthesis — AAL short, pending @ 13.35, published 2026-10-03
Not overridden, but the risk changed the day after it was written. AAL is 12.94,
-31.1% off its high and already +28.2% off its low, and the short's driver is jet
fuel. The Hormuz-reopening and interim-deal reports cut directly against it: a
de-escalation is lower fuel and an airline rally, into a 2026-10-15 print. The
resting order is above the market so it only fills on a bounce. **Keep the order;
know that its core driver is one headline from reversing**, and consider that
13.35 is a short entry in a name already down a third.

## [06:28 ET] CRYPTO LEVELS — the only live market today, and the workaround used
`market_data.py history BTC-USD` fails completely: nasdaq has no rows, Yahoo is
429, twelvedata and alphavantage have no key, stooq has no history. So **no daily
crypto OHLC is available through the CLI this run.**

Worked around it with CoinGecko's OHLC endpoint at `days=30`, which returns
4-hour candles, aggregated into 31 daily bars. Note the trap: `days=180` returns
**4-day** candles, and the ATR14 computed off those is about 2x the daily figure
(BTC 4,719 against a true daily 2,210). An ATR taken from the 180-day call would
have produced a stop twice as wide as it should be.

- **BTC 85,086**, daily ATR14 **2,210 (2.60%)**, 30d range 75,038-87,330.
  Ten sessions coiled 83,230-87,086 under the 87,330 high; consolidation floor
  82,581 (2026-09-28).
- **ETH 2,705.58**, daily ATR14 **76.86 (2.84%)**, 30d range 2,361.16-2,804.42.
  Same shape, coiled 2,653-2,768 under 2,804.

Driver is measured flow: $3.55B of crypto fund inflows in a week, $102.7M net
into US spot BTC ETFs on 2026-10-01, liquidations easing to ~$35M, +33.4% over 90
days — sources:
https://finance.yahoo.com/markets/crypto/articles/too-crypto-october-2026-3-230323461.html ,
https://finance.yahoo.com/markets/crypto/articles/weekly-wrap-crypto-rallies-start-223800297.html

**Deliberately excluded from the evidence:** "Uptober" seasonality (+18.52%
average) and Citigroup's $113,000 target. A monthly average return is a statistic
and a sell-side target is an opinion; neither is a confirmation, and BTC is
captured at conviction 3 rather than 4 because of that exclusion.

**ETH not captured** — the setup is the same shape as BTC and taking both would be
one idea twice, against the correlation rule. BTC has the deeper ETF flow
evidence, so it is the one published.

## [06:28 ET] SELF-CHECK — arithmetic recomputed on every captured idea
Not trusting my own numbers, per the standing instruction. Recomputed from the
captured fields:

| Symbol | R:R (floor 2.0) | stop in ATR (floor) | break-even | win prob | edge | expectancy |
| --- | --- | --- | --- | --- | --- | --- |
| FCX | 2.124 | 2.001 (2.0 stock) | 32.0% | 42% | +10.0 pts | +0.312R |
| BTC | 2.143 | 2.534 (2.5 crypto) | 31.8% | 40% | +8.2 pts | +0.257R |
| XLE | 2.129 | 2.479 (1.8 etf) | 32.0% | 36% | +4.0 pts | +0.126R |

All three clear both floors with positive expectancy, and no claimed edge exceeds
20 points. Conviction equals the distinct-evidence-kind count on all seven ideas
(asserted in code, not eyeballed).

**Warning for the red team, stated rather than engineered around:** FCX at 2.001
and BTC at 2.534 sit a hair above their ATR floors, and those multiples use *my*
ATR — 2.4235 for FCX from the nasdaq history, 2,210 for BTC from aggregated
CoinGecko 4-hour candles. If validation's own ATR comes in higher, both fail.
I did not widen the stops or lift the targets to buy margin, because 68.20 with a
stop under the 67.01 shelf is where the chart puts them and 78.50 is deliberately
under the 80.24 range high. Checked the alternatives: entry 67.80 gives 1.84 ATR
and entry 69.50 gives a 1.46 R:R, so 68.20/63.35 is the only geometry that clears
both. **If the recomputed ATR fails these, fail them — do not nudge the levels.**

## [06:28 ET] RESEARCH COMPLETE
- **candidates: 8 rows, 7 distinct symbols** (XLE captured twice; the later
  conviction-2 revision supersedes the earlier conviction-3 version)
- **2 genuinely new ideas**: FCX (copper, new long) and BTC (breakout long)
- **4 exits**: CCJ, GDX, SVRA, LCII — three of them triggered by the same
  mechanical fact, a stop sitting inside 1 ATR of the market (0.88, 0.81, 0.84)
- **1 hold with a changed thesis**: XLE, conviction cut 3 to 2
- **9 open positions reviewed and left alone** with reasons logged: DINO, XLU,
  SNX, EEM, PFE, BCC, KHC, and the NKE/LULU exit artifacts

**Read the shape of this report honestly:** it is risk reduction, not opportunity.
Four of seven rows are exits and only two are new risk. That is the conclusion the
cross-sectional screen forced — the index is 1.25% off a record while the median
name outside AI and copper is at a 52-week low, and every losing position in this
book is the same de-rated-value trade. The bar for new value longs was raised and
nothing cleared it.

### Coverage gaps
- **Zero event contracts captured**, on a Sunday, with the lane explicitly wanted.
  Not for lack of looking: the Fed, CPI, CPI-YoY, U-3 and recession ladders were
  all priced and screened. The macro complex is liquid and correctly priced, the
  one disagreement I could build rested on a factual error about Fed policy, and
  the one surviving candidate (KXU3-26OCT-T4.2) has a 14% spread. Absence here is
  a finding, not a gap.
- **No VIX, DXY, spot gold or spot WTI print all run** — every Yahoo-dependent
  index call 429'd. Equity-level work survived on the nasdaq source; macro
  breadth did not. Used USO and GLD as proxies and said so.
- **No options-implied move for any candidate.** `implied FCX` returned Yahoo
  401. So the "is my target inside what the market prices" check in
  config/strategy.md was **not performed on any idea today.**
- **No short interest / days to cover** — `short FCX` timed out on api.nasdaq.com.
- **Intraday horizon: nothing, correctly.** US equities and futures are shut; a
  Sunday cannot produce an intraday equity setup.
- **long_term: nothing new.** FCX was considered and dropped for it (no defensible
  valuation anchor without a production figure I had not fetched). This lane has 9
  open positions and 0 closed, and it got less time than config/strategy.md's ~15%
  allocation because the position review and the defense/staples investigations
  consumed it. Flagging it as the real gap of the run.
- **Futures: nothing**, beyond flagging the stale /MBTU6 short for cancellation.

### Sources that failed
- **Yahoo Finance — HTTP 429 on everything**: all index/VIX/DXY/futures quotes via
  `macro`, all `history` fallbacks, BTC-USD history entirely.
- **Yahoo options — HTTP 401**: `implied` unusable for every symbol.
- **api.nasdaq.com — ReadTimeout**: `short FCX`.
- **fred.stlouisfed.org/graph/fredgraph.csv — ReadTimeout** at 30s. FRED's series
  path inside `macro` worked fine; only the CSV graph endpoint failed. Used the
  **BLS public API v1** instead, which worked and is the better source anyway.
- **Finnhub — refuses indices** ("Market data subscription required for CFD
  indices"); its earnings calendar and insider/analyst endpoints worked well.
- **stooq — 404** on all `^`-prefixed index symbols.
- **EIA — API_KEY_MISSING**, so no direct gasoline series; inferred energy from USO.
- **No API key present** for twelvedata or alphavantage.
- **`market_data.py events` — returns nothing usable**; see the 06:05 block. Two
  real client-side bugs (renamed Kalshi price fields, no server-side search).
  Every event contract figure in these notes came from a direct API call instead.

## [06:30 ET] NARROWNESS, REFINED — it is not "AI", it is NVDA
Screened the AI-capex and power complex looking for a long in something working,
since that was today's lesson. The complex does not hold together:

| Name | Last | % off 150d high | vs 20d / 50d means |
| --- | --- | --- | --- |
| NVDA | 233.95 | **-1.6%** | above / above |
| ETN | 436.11 | -8.8% | above / above |
| PWR | 676.56 | -14.2% | above / above |
| GEV | 988.70 | -17.3% | above / **below** |
| VST | 140.02 | -20.7% | below / below |
| CEG | 257.49 | -22.9% | below / below |
| AVGO | 355.14 | -28.2% | below / below |
| VRT | 252.18 | -33.6% | below / below |

So the tape is narrower than the 06:25 block said. It is not buying the AI theme
— **AVGO is -28% and VRT -34% while NVDA is -1.6% off its high.** Only NVDA and
the electrical-equipment names (ETN, PWR) are actually working. Power IPPs and
datacentre infrastructure have de-rated with everything else.

**NVDA considered and rejected as a swing.** The geometry works — 233.95 with a
stop at 223.65 just under the 20-day mean at 223.79 is 2.0 ATR, and a 254.55
target is 2.0:1 — but there is **no dated catalyst inside the horizon** (earnings
are late November), and config/strategy.md is explicit that a technical breakout
is a trigger, not a catalyst. Publishing it would mean dressing trend continuation
up as an event. Not captured. A long_term NVDA framing hits the same wall as FCX:
no defensible valuation anchor from the data I can fetch.

## [06:30 ET] FLAG for synthesis — two resting BUY orders should not be republished
Both are in "awaiting entry", so amending them double-counts nothing. Today's
cross-sectional finding argues directly against both, and I am flagging rather
than capturing because the pipeline has a watchlist for exactly this.

- **CEG BUY @ 272.00 (published 2026-10-01).** CEG **stopped out on 2026-09-30**
  and was re-pitched the next morning at 272 — which is **5.6% above the current
  257.49** — in a name below both means and 22.9% off its high. Buying back a
  stop-out at a higher price than it trades, one day later, is the anchoring
  CLAUDE.md and prior_context.md both warn about. **Recommend demoting to the
  watchlist with a trigger, not carrying it as a live buy.**
- **VST BUY @ 132.00 (published 2026-08-24).** 140.02 now, below both means and
  only 5.5% off its 150-day low of 132.66. The resting 132 entry sits just above
  that low, so it fills precisely if the downtrend continues — the
  "pullback entry that selects for the ideas already failing" pattern named in
  config/strategy.md, where 42% of 31 such entries filled and the fills were the
  fallers. **Recommend demoting to the watchlist.**

Neither is a new loss today. Both would be new losses in the regime identified
above, which is the cheapest kind of mistake to avoid.

## [06:30 ET] RESEARCH COMPLETE — final
Supersedes the earlier completion block only in the counts; everything else there
stands.
- **candidates: 8 rows, 7 distinct symbols.** 2 new ideas (FCX, BTC), 4 exits
  (CCJ, GDX, SVRA, LCII), 1 hold with a cut conviction (XLE).
- **2 resting orders flagged for watchlist demotion** (CEG, VST) — see above.
- **11 open positions reviewed and left alone**, reasons logged: DINO, XLU, SNX,
  EEM, PFE, BCC, KHC, NKE/LULU exit artifacts.
- Ran 06:00-06:30 ET, inside the cap. Not truncated.
