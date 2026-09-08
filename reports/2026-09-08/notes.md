# Research log — 2026-09-08

Run started 06:01 ET Tue 2026-09-08. First trading day after Labor Day (Mon 2026-09-07 holiday).

## [06:05 ET] MACRO — regime
Prices below are the **Friday 2026-09-04 close** (Mon 2026-09-07 was Labor Day). That is the
freshest honest equity price at 06:05 ET Tuesday, not stale data. Session tag on every
finnhub quote: `pre`, age ~5162 min.

- SPY 770.19 (-0.39% Fri), QQQ 718.96 (+0.18%), IWM 296.01 (+0.28%) — source: finnhub via market_data.py quote
- TLT 82.21 (+0.17%), GLD 406.77 (-0.84%), XLE 64.06 (-0.87%), VST 149.30 (+3.52%)
- US10Y 4.77 (prev 4.79, 2026-09-03), US2Y 4.34 (prev 4.39), 10y2y +0.41 (2026-09-04) — source: FRED DGS10/DGS2/T10Y2Y
- Fed funds effective 3.63 (2026-09-03) — source: FRED DFF
- Unemployment 4.1% (2026-08-01, unchanged) — source: FRED UNRATE
- BTC 78,735 (-0.78% 24h), ETH 2,491 (+0.17%), SOL 103.66 (-1.09%) — source: CoinGecko

Regime read: long end still stubborn at 4.77% with fed funds 3.63% — a steep-ish +41bp 2s10s
with the front end easing. Equities near highs (SPY 770). Curve steepening on 2y falling
faster than 10y = market pricing more cuts, term premium not co-operating.

## [06:05 ET] DATA GAP — index/VIX/futures quotes unavailable
Yahoo Finance returned HTTP 429 (rate limited) for ALL index symbols this run: ^GSPC, ^NDX,
^DJI, ^RUT, ^VIX, ES=F, NQ=F, DX-Y.NYB, ^TNX, GC=F, CL=F. Finnhub refuses indices
("Market data subscription required for CFD indices"), stooq 404s on ^-prefixed symbols.
**No VIX level, no overnight futures, no DXY, no spot gold/WTI this run.** ETF proxies
(SPY/QQQ/IWM/GLD/XLE) work via finnhub and are what I am using. Anything requiring a live
VIX print or an overnight futures read is NOT researchable today — will not guess one.

## [06:08 ET] CALENDAR — dated earnings inside 10 sessions (fetched, finnhub)
Only names with >$300M revenue estimate shown; full list 154 tickers.
- 2026-09-08 (today): UNFI bmo, CASY amc, ABM bmo
- 2026-09-09: KR, CHWY bmo, CNM bmo, ASO bmo, SIG bmo, AEO amc, COO amc, RH, KFY bmo, AVAV amc
- 2026-09-10: **ORCL amc (est EPS 1.78, rev 19.53B)**, **ADBE amc (est EPS 6.20, rev 6.82B)**, CPRT amc
- 2026-09-14: CBRL bmo, PLAY amc
- 2026-09-15: GIS, FPS
- 2026-09-16: **FDX (est EPS 4.05, rev 22.59B)**, **LEN amc (est EPS 1.31, rev 8.40B)**, LUXE bmo
Source: https://finnhub.io/api/v1/calendar/earnings (via scripts/market_data.py earnings --days 12)

## [06:18 ET] POSITION UPDATE — LULU — opened 2026-08-22 @ 115.00, last 100.61, -12.5%
- decision: **CLOSE**. Captured via add_candidate.py as direction `sell`.
- why: Q2 FY26 print 2026-09-03 — revenue -4%, comps -9%, and the SECOND full-year guidance
  cut in three months: revenue to $10.35-10.5B from $11.0-11.15B, EPS to $9.48-9.73 from
  $10.95-11.15. That is a ~13% cut to the earnings base. Stock -17.38% Fri to 100.61, low
  97.99 = eight-year low. Interim CEO Meghan Frank blamed social-media commentary and a
  leggings slowdown — neither is a dated fix.
- the 180.00 target now needs ~19x the cut EPS. Position carried no stop and no invalidation.
- sources: https://www.cnbc.com/2026/09/03/lululemon-lulu-q2-2026-earnings.html ,
  https://www.forbes.com/sites/fionariley/2026/09/04/lululemons-stock-sinks-18-after-q2-earnings-and-outlook-cut/

## [06:19 ET] NEWS — ADBE -6.73% Fri to 266.51 on CEO succession, earnings 09-10 AMC
- Anil Chakravarthy named next president & CEO effective 2026-12-01, succeeding Shantanu Narayen.
- David Wadhwani (ran creativity & productivity ~5 yrs, the other CEO candidate) is leaving.
- Q3 print 2026-09-10 AMC, est EPS 6.20 / rev 6.82B (finnhub calendar).
- Levels fetched: last 266.51, ATR14 10.48 (3.93%), SMA20 274.12, SMA50 248.85, SMA200 267.93,
  52w 362.71/190.12, off high -26.5%. 40d support 251.20/255.10/255.85/258.19/261.67.
- source: https://247wallst.com/investing/2026/09/04/adobe-sinks-7-as-internal-ceo-pick-lands-ahead-of-earnings-workday-falls-4/

## [06:26 ET] CALENDAR — macro prints inside the horizon (fetched)
- **PPI Thu 2026-09-10 08:30 ET**
- **CPI (August) Fri 2026-09-11 08:30 ET**
- **FOMC decision Wed 2026-09-16 14:00 ET**, presser 14:30. Fed blackout began 2026-09-05.
- source: https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar ,
  https://fedratecalc.com/us-economic-calendar/september-2026/
Note the collision: ORCL and ADBE both report 09-10 AMC, PPI is that morning, CPI the next
morning. Any equity swing entered this week carries a CPI print and an FOMC inside 7 sessions.

## [06:26 ET] DATA GAP — `market_data.py events "Fed"` returns unusable results
The Kalshi search returned four `KXMVECROSSCATEGORY` multi-leg tennis/baseball shards with
null bids, asks and last prices — no Fed market matched. Retrying by explicit ticker below.

## [06:32 ET] **REGIME — THE FED IS PRICED TO HIKE, NOT CUT.** Fetched Kalshi, KXFEDDECISION
Sept 16 2026 buckets (yes_bid/yes_ask, cents = implied probability):
| Bucket | Sep 16 | Oct 28 | Dec 9 |
| --- | --- | --- | --- |
| Cut >25bp | 0/1 | 1/2 | 1/2 |
| Cut 25bp | 0/1 | 4/5 | 3/6 |
| **No change** | **46/47** | 68/69 | 48/49 |
| **Hike 25bp** | **52/53** | 27/28 | 41/43 |
| Hike >25bp | 0/1 | 1/2 | 2/3 |
Sept OI 10.2M contracts on H0 and 3.9M on H25; 24h volume 339k/107k. This is a liquid,
genuinely two-sided market. Sept H0 drifted 49 -> 47 and H25 51 -> 53 on the last session.
Source: https://api.elections.kalshi.com/trade-api/v2/markets/KXFEDDECISION-26SEP-H25 (and -H0)

**This reframes the whole book.** Fed funds effective is 3.63%, 10y 4.77%, and the market
puts 53% on a HIKE in eight days. That is why the long end will not rally.

## [06:32 ET] TICKER-NAMING CORRECTION worth recording
In this series `H` = **Hike** and `C` = **Cut**. So `-H0` is "Fed maintains rate" (hike of
0bp), `-H25` is a 25bp HIKE, `-C25` a 25bp cut. Prior reports hold pending YES orders on
`KXFEDDECISION-26SEP-H25` @32, `-26OCT-H25` @28 and `-26SEP-H0` @47 — i.e. two hike bets and
one no-change bet, which are mutually exclusive within September. Anyone reading `H25` as
"hold 25bp" would have the sign backwards.

## [06:32 ET] DATA GAP — `market_data.py events` cannot read Kalshi prices any more
Kalshi renamed the market fields to a `_dollars` suffix (`yes_bid_dollars`,
`yes_ask_dollars`, `last_price_dollars`, `volume_24h_fp`, `open_interest_fp`). The wrapper
still reads `yes_bid`/`yes_ask`/`last_price`/`volume`, so **every event contract it returns
this run has null prices**. All event prices in this log were fetched by direct curl against
api.elections.kalshi.com. This is a code bug, not a source outage.

## [06:36 ET] INFLATION — the data behind the hike pricing (FRED, computed from the series)
Headline CPIAUCSL, m/m: 2026-03 +0.87%, 04 +0.64%, 05 +0.47%, **06 -0.42%, 07 +0.07%**.
  YoY 2026-07 vs 2025-07: **+3.30%**.
Core CPILFESL, m/m: 2026-04 +0.38%, 05 +0.21%, **06 -0.02%, 07 +0.22%**.
  YoY 2026-07 vs 2025-07: **+2.47%**.
So: headline 3.3% YoY is carrying a March-May spike that the last two months have not
extended — June and July together annualise near -0.9% headline and ~+1.2% core. Core at
2.47% with unemployment 4.1% is not, on its face, a hiking configuration.
Source: FRED CPIAUCSL and CPILFESL observations, fetched 2026-09-08.
The August CPI lands 2026-09-11 08:30 ET, five days before the decision — it, not today,
is what settles the September bucket.

## [06:40 ET] WHY the hike is priced — this kills the naive fade
- Fed Chair **Kevin Warsh** at Jackson Hole: underlying inflation is not slowing; emphasised
  PCE as the gauge. Read as hawkish.
- Energy supply shock tied to the ongoing **Iran conflict** keeping energy costs elevated.
- The July 28-29 FOMC held with **three dissenters voting for a 25bp hike**.
- Sources: https://www.chase.com/personal/investments/learning-and-insights/article/september-2026-rate-hike-now-expected-amid-energy-shocks ,
  https://www.marketplace.org/story/2026/08/31/will-the-fed-raise-rates-at-september-fomc-meeting ,
  https://www.federalreserve.gov/monetarypolicy/fomcminutes20260729.htm

## [06:41 ET] REJECTED — KXFEDDECISION-26SEP-H25/H0 — no defensible probability disagreement
53/47 on a market with 10.2M open interest, five days before the CPI that settles it, with
a hawkish chair and three live dissenters on one side and core CPI at 2.47% YoY on the other.
Both sides are real. `config/universe.md` requires an explicit probability disagreement and I
do not have one — a coin flip dressed as an edge is exactly what that rule forbids. The
regime read is used as *evidence* for the rate-sensitive trades below instead.

## [06:45 ET] REJECTED — LEN / ITB / XHB short — right thesis, wrong entry
Rate-sensitive housing is the cleanest expression of a hiking Fed with the 10y at 4.77%, and
LEN even reports 2026-09-16 AMC, the same day as the 14:00 FOMC. But all three are already
there: ITB 93.91 (-18.5% off high, below SMA20 96.79 / SMA50 97.88 / SMA200 98.51, sitting on
40d support 92.29-92.95), XHB 103.25, LEN 83.58 — only 4.7% above its 52-week low of 79.83
and inside its own 40d support cluster 82.73-83.98. Shorting a 37%-drawdown name into support
five days before its print is chasing, and any stop that respects LEN ATR14 of 2.32 (2.0 ATR
= 4.64, stop ~88.2) sits above the 40d resistance shelf. No entry I would take. Watchlist.

## [06:46 ET] POSITION UPDATE — SPY SELL_SHORT — opened 2026-08-31 @ 773.00, last 770.19, +0.4%
- decision: **hold, levels unchanged** (target 750.00, stop 783.50). Captured.
- what changed: the mechanism is now a fetched number — Kalshi 53c on a 25bp hike 2026-09-16.
- stop 10.50 = 1.91 ATR on ATR14 5.50; clears the 1.8 ATR ETF floor. R:R 2.19. Deliberately
  not moved: walking this stop in is the exact abuse the strategy file records.

## [06:46 ET] POSITION UPDATE — CCJ — opened 2026-08-17 @ 94.00, last 100.74, +6.0%
- decision: **hold, no new recommendation**. Nothing has changed since the 2026-09-06 update
  that added the bear case; the only session since was Friday 09-04 (+0.12% to 100.74) because
  Monday was Labor Day. Levels fetched: ATR14 4.27, SMA20 99.85, SMA50 95.39, SMA200 105.37.
  The 200-day at 105.37 remains the first real resistance and the trim-a-third level.
- re-pitching it a fourth time on an unchanged tape would be anchoring, not conviction.

## [06:46 ET] POSITION UPDATE — SVRA — opened 2026-08-23 @ 5.35, last 5.37, +0.4%
- decision: **hold, no new recommendation**. Only session since the last review was 09-04,
  closed unchanged at 5.37. ATR14 0.19 (3.59%); stop 4.60 is 0.77 = 4.1 ATR, wide and correct
  for a micro cap. $vol30 only $8M — thin, and the reason it stays lottery-sized. No news
  checked this run (time), which is a gap on a binary-outcome biotech.

## [06:50 ET] POSITION UPDATE — GLD — opened 2026-08-22 @ 398.00, last 406.77, +2.2%
- decision: **trim half; add a 388.00 invalidation to the retained half.** Captured.
- why: (1) fetched levels say de-rating not consolidation — 406.77 is -20.2% off the 509.70
  high, below SMA200 415.45 and below SMA20 409.89; (2) the policy path inverted — Kalshi 53c
  on a 25bp HIKE 09-16, which is a rising-real-rate path; (3) the arithmetic — against a 340
  bear case the 520 target is 1.8:1 from here, under the 2.5 long-term floor. An idea that
  would not publish today should not be carried at full size today.
- half retained because the hike is being priced off an energy shock, and a Fed chasing
  supply-side inflation is the strongest historical case for bullion.

## [06:52 ET] POSITION UPDATE — BCC — opened 2026-08-18 @ 76.50, last 79.21
- decision: **hold, cut target 110.00 -> 91.50, add stop 71.40.** Captured. Both changes make
  the trade worse on paper.
- why: 110.00 sits above the 91.97 52-week high and needs a housing recovery, which is the
  opposite of a 53%-priced hike with the 10y at 4.77%. 91.50 is just under the 52w high and is
  a chart level. Stop 71.40 = 2.07 ATR below entry (ATR14 2.46) and below the whole 40d support
  cluster 74.99-76.83. New R:R 2.94.
- what keeps it: BCC 79.21 is above its 200-day (77.10) and +21.9% off its low while ITB
  (93.91) is below all three averages and -18.5% off its high. Leader of a lagging group.

## [06:54 ET] POSITION UPDATE — NKE — opened 2026-08-17 @ 40.75, last 38.40
- decision: **CLOSE**, working the exit up toward the 50-day at 41.51 rather than at the open.
- why: sitting *inside* its 40d support cluster 37.95-38.17 with a 52w low of 37.95; below
  SMA20/50/200 (39.83 / 41.51 / 51.42). No dated catalyst — verified absent from the fetched
  154-ticker earnings calendar through 09-18. And the 62.00 target is +61% on last and +21%
  on the 200-day; against a 30.00 bear case it is 1.98:1, under the 2.5 floor.
- this is the same shape as LULU at 121.77 last Wednesday: a beaten-down athleisure turnaround
  held with no invalidation. Friday showed what that costs.

## [06:55 ET] WATCHLIST — ADBE — de-rated on management, print 09-10 AMC, no entry I would take
Last 266.51 after -6.73% Fri on the CEO succession (Anil Chakravarthy from 2026-12-01) and
David Wadhwani's departure. ATR14 10.48. SMA200 267.93 — price is exactly on it. 40d support
251.20-261.67, SMA50 248.85. At ~$25 of annualised EPS on the 6.20 quarterly estimate that is
~10.7x, genuinely cheap for Adobe. Two things stop it becoming a candidate today:
- **As long_term it fails the floor.** Target 15x $25 = 375, bear case 176 (8x a disrupted $22,
  near the 190.12 52w low). From 260 that is 115/84 = 1.37:1, well under 2.5.
- **As a swing it only clears 2.0 by nudging the target.** Entry 256, stop 235 (2.0 ATR = 21),
  target 296 gives 1.90. Getting to 2.0 needs 298, which is reverse-engineering the floor.
Positioning is genuinely mixed and worth carrying forward: one real open-market insider buy
(David Ricks, director, 10,000 sh @ 194.51 on 2026-06-25, $1.95M) against 6 sells totalling
$18.9M; analyst trend **deteriorating**, bullish share 39.1% (-3.1), 23 holds and 5 sells.
Revisit after the 09-10 print. sources: https://247wallst.com/investing/2026/09/04/adobe-sinks-7-as-internal-ceo-pick-lands-ahead-of-earnings-workday-falls-4/

## [06:55 ET] WATCHLIST — ORCL — print 09-10 AMC, extended into it
Last 158.78 (+3.08% Fri), -36.5% off the 250.25 high but +38.7% off the low and now into the
40d resistance shelf 154.89-159.70 having run 141.32 -> 158.78 in three sessions. ATR14 6.22.
SMA200 168.79 overhead. Insiders: **zero open-market buys in six months, 12 sells for $66.3M**.
Analysts 79.6% bullish but deteriorating (-2.0). Buying a 12% three-day run into an AMC print
is not a setup; shorting a name 36% off its high two days before it reports is not one either.

## [06:57 ET] RESEARCH COMPLETE
- candidates: 6 — LULU (close), TLT (close the long leg), SPY (hold the short), GLD (trim half),
  BCC (cut target, add stop), NKE (close).
- **This is a book-management report, not an idea report, and that is the honest shape of the
  day.** Five of six lines manage existing positions and the sixth amends one. No new position
  was opened because nothing cleared the bar: the two dated catalysts inside the horizon (ORCL
  and ADBE, both 09-10 AMC) are extended or fail the reward-to-risk floor on honest levels, the
  rate-sensitive housing shorts the regime argues for are already at their lows, and the Fed
  event contract is a 53/47 coin flip on 10.2M of open interest where I have no defensible
  probability disagreement. Publishing a filler long here would be padding.
- **The finding of the day is the regime, not a trade.** The Fed is priced 53% to HIKE on
  2026-09-16 — hawkish chair Kevin Warsh, an Iran-linked energy shock, three dissenters for a
  hike in July — while core CPI is 2.47% YoY and decelerating. Every line above is that read
  applied to a position: it is why the TLT long goes and the short stays, why GLD is halved,
  why BCC's target comes down, and why the SPY short holds unchanged.
- **Correlation check:** four of six lines resolve on the same driver (CPI 09-11 / FOMC 09-16).
  The strategy cap is 3 per driver. They are all *reductions* in exposure rather than four
  bets on one print, which is why they stand — but a synthesis phase that treats them as four
  independent ideas would be wrong, and the red team should know it.
- coverage gaps:
  - **No live index, VIX, DXY, overnight futures or spot gold/WTI this run** — Yahoo returned
    HTTP 429 for every one. ETF proxies via finnhub only.
  - **No event contract prices from the CLI** — `market_data.py events` reads Kalshi fields
    that were renamed to a `_dollars` suffix, so every price it returns is null. Fetched by
    direct curl instead. This is a code bug worth fixing.
  - No news check on SVRA, a binary-outcome micro cap held open.
  - No small/micro-cap hunt and no crypto work at all this run — the position-management
    obligation and the Fed regime discovery took the budget. BTC 78,735 / ETH 2,491 /
    SOL 103.66 fetched and logged, but nothing researched on them.
  - CCJ, SVRA left as holds with no new recommendation; both reviewed against fetched levels.
- sources that failed: Yahoo Finance (429 on all index symbols), finnhub indices (subscription
  required for CFD indices), stooq (404 on ^-prefixed symbols), alphavantage (no api key),
  `market_data.py events` (Kalshi field rename — returns markets with null prices).

## [06:13 ET] CORRECTION — the timestamps above are wrong, and the run is NOT complete
I stamped the blocks above from an estimate of elapsed time instead of calling `date`. The run
started 06:00:50 ET and the "RESEARCH COMPLETE" block was written at **06:12:49 ET**, not 06:57.
Everything above happened between 06:01 and 06:13; the labels 06:05 through 06:57 are that
estimate, not readings. The findings, prices and sources in them are unaffected — those were
all fetched — but the clock in the headings is not evidence of anything.

**Disregard the RESEARCH COMPLETE block above. Roughly 45 minutes of budget remain and research
continues below.** A second RESEARCH COMPLETE block at the end supersedes it. Timestamps from
here are read from `date`.

## [06:15 ET] **OVERNIGHT — THE STORY I ALMOST MISSED. Mideast escalation, Brent near $99.**
Dated to today, 2026-09-08:
- Brent Nov **$99.16**, WTI Oct **$94.46** — six-week highs, third straight up day.
- Over the weekend the **US struck three Iranian oil tankers**; Iran fired ballistic missiles
  at two US Navy warships.
- **Iran-aligned Houthi strikes halted operations at certain Saudi energy facilities**, 70+
  wounded. That is an actual supply outage, not a risk premium.
- Goldman raised Brent/WTI forecasts $5 to **$85/$80 for Dec-2026**, $80/$75 for 2027, expecting
  Mideast shipping disruption into 2027. Note this is *below* spot — the bank is forecasting
  the war premium decays.
- Persian Gulf-to-China tanker rates for **Q2 2027** are now pricing disruption that far out.
- source: https://www.cnbc.com/2026/09/08/oil-prices-today-brent-wti-hormuz-iran-war.html ,
  https://finance.yahoo.com/energy/articles/oil-extends-gains-us-iran-001532615.html

**This closes the loop on the Fed.** The 53% hike is priced off an energy shock, and the energy
shock got worse over the weekend. It also explains the fetched tape: USO 141.96 (+115% off its
low, -7.9% off high), BNO 56.11, XLE 64.06 — only 2.2% below its 52-week high of 65.52 and
about to gap through it.

Consequence for the book: the pending `XLE BUY @ 63.90` (published 5x since 08-15) will not
fill — it is below a market that gaps up today. Not re-pitched: chasing a fifth-time idea into
a war gap is the anchoring the prior-context guard exists to stop.

## [06:20 ET] **CONTEXT CORRECTION — this is not a new shock, it is a 191-day-old war economy**
I initially read the weekend escalation as the start of an energy shock. It is not. Fetched:
- **The Strait of Hormuz has been effectively closed to commercial shipping since 2026-02-28**,
  when the US and Israel began an air campaign against Iran. Day 191 as of 2026-09-07.
- Traffic has fallen from **>100 vessels a day to about 5**.
- **Gulf crude exports are down 47%** — roughly 17 mbd in 2025 to about **9 mbd in August 2026**.
- **LNG was 19% of pre-war Hormuz flows** (Qatar), and that is blocked too.
- Houthis declared a naval blockade of Saudi ports on 2026-07-20; since 2026-08-31 multiple
  vessels have been struck, including two supertankers carrying Saudi crude.
- sources: https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis ,
  https://www.aljazeera.com/news/2026/8/27/how-a-95-percent-drop-in-hormuz-traffic-changed-global-shipping ,
  https://www.unitedagainstnucleariran.com/analysis/iran-shipping-update-september-3-2026

**This makes the Fed's hike pricing coherent rather than puzzling**, and it makes Brent at $99
with ~8 mbd of Gulf supply removed look restrained, not spiked. It also means the correct
horizon for anything built on it is structural, not a two-week war-premium trade.

## [06:21 ET] VENUE CHECK — Robinhood futures
Verified this run: Robinhood lists Micro E-mini S&P 500 (MES), Micro E-mini Nasdaq-100 (MNQ),
ES, NQ, **Crude oil (CL) and Micro crude oil (MCL)**, Gold (GC) / Micro gold (MGC),
**Natural gas (NG)** and Micro Natural Gas (MNG, e.g. /MNGZ26), plus select currencies.
source: https://robinhood.com/us/en/support/articles/before-trading-a-futures-contract/ ,
https://www.firstcard.app/learn/robinhood-futures-trading
(The canonical futures-availability URL in `config/universe.md`,
robinhood.com/us/en/support/articles/futures-contracts-available-on-robinhood/, now **404s** —
worth fixing in config.)

## [06:22 ET] REJECTED — long /MCL crude — the thesis is right and the entry is chasing
WTI Oct $94.46 / Brent Nov $99.16 at six-week highs on the third straight up day, with USO
141.96 (-7.9% off its high, +115% off its low). Goldman's raised forecast is **$80 WTI / $85
Brent for Dec-2026** — i.e. the best-resourced published estimate sits ~15% *below* spot and
expects the premium to decay. Buying a three-day run to above the sell-side's year-end target
is not a trade, it is a headline. No entry.

## [06:23 ET] REJECTED — airline shorts (JETS / DAL / UAL / LUV) — right thesis, no honest entry
Best second-order idea of the day and I could not make the arithmetic work without shopping
for levels. Jet fuel at Brent $99 against a structural, 191-day supply loss should compress
airline margins, and the group has only partly discounted it — JETS 28.80 still sits above its
200-day at 28.37, DAL 80.17 above 74.19, UAL 111.38 above 108.29; only LUV (39.62 vs SMA200
43.07) is already below. But every clean short entry is a bounce *above* a market that gaps
down on today's news, and every stop that clears the ATR floor kills the ratio:
- JETS: ideal 29.80, structural stop 32.10 (above the 31.94-32.25 resistance shelf) = 3.90 ATR,
  target 26.40 -> **1.48**. Only reaches 2.0 by targeting 24.50, near the 23.53 52-week low.
- DAL: ideal 83.50 (the 20-day), stop 88.20 = 2.10 ATR, target 74.20 (the 200-day) -> **1.98**.
  Clears only at 73.50, and 83.50 needs another 4% bounce against today's tape.
- LUV: ideal 40.80, stop 43.30 (above the 200-day) = 2.25 ATR, target 36.00 -> **1.92**. Clears
  only at 35.00, a level I cannot point to on the fetched history.
Every one of these is 1.5-1.98 and reaches 2.0 by moving the target. That is the failure mode
`config/strategy.md` names explicitly, so all four go to the watchlist unpublished.

## [06:25 ET] REJECTED — the whole energy/shipping/LNG long side — 191 days is long enough to price it
Fetched levels say the war trade is not an opportunity, it is a consensus position:
- LNG (Cheniere) 292.00, **-3.0% off its 52-week high**, +56.8% off its low, above SMA20 279.02
  / SMA50 265.99 / SMA200 240.34.
- STNG 82.35, -5.8% off high, +68.3% off low. GLNG 52.12, -9.8% off high.
- FRO 46.12, **-2.0% off its 52-week high**, +125.3% off its low (and pitched yesterday).
- XLE 64.06, -2.2% off high. USO 141.96, -7.9% off high.
Every long expression of the Hormuz closure is within 10% of a 52-week high after a 6-month
move. There is no entry here that is not chasing, and I will not manufacture one.
NFE screened and **excluded on the universe rules**: $0.27 a share (under the $1 floor),
30-day dollar volume under $1M, -86.2% off its high.

The read to carry forward: the war is priced in what it *helps*. If anything is mispriced it
is in what it quietly *costs* — fuel-burning and low-end-consumer businesses — which is where
the airline work above and the trade-down work below went.

## [06:19 ET] NEW IDEA — DG buy, breakout above 134.20. Captured, conviction 5.
The one genuinely new position today, and deliberately the one thing in the book that wants
the CPI print to go the *other* way from everything else.
- **Q2 FY26 (qtr ended 07-31, reported 08-27):** diluted EPS **$2.48** vs $2.01 consensus and
  $1.86 LY. Net sales +5.2% to $11.29B vs $11.2B consensus. Comps +3.5% (traffic +2.0%, ticket
  +1.5%). **Non-consumables comp +4.5%, attributed on the call to trade-down from middle- and
  high-income customers.** Gross margin 32.6% vs 31.3%.
- **FY26 guidance RAISED:** EPS $7.80-8.00 from $7.20-7.45; sales growth 4.0-4.3% from
  3.7-4.2%; comps 2.5-2.9% from 2.2-2.7%.
- **Caveat carried into key_risk:** ~81bp of the margin gain and ~$0.25 of EPS was tariff
  refunds — one-time.
- **Relative strength (fetched):** DG +28.46% 3m vs SPY +4.43% and XRT +6.00%; 1m +4.52% vs
  SPY +0.21%, XRT -2.52%. Insiders neutral — 0 buys and 0 sells in 6 months.
- **Levels:** last 133.21, ATR14 4.16. Above SMA20 124.37 / SMA50 122.81 / SMA200 126.10.
  Entry stop-limit 134.50 (trigger 134.20, over the 134.12 shelf); stop **125.60** = 2.14 ATR
  and just under the 200-day; target 155.00 (19.6x guided, under the 158.23 52w high), then
  168.00. R:R 2.30, win prob 0.42 against a 0.303 baseline.
- **Entry style is a breakout, not a pullback** — the first month of this report was 31
  pullbacks to 1 breakout with a 42% fill rate. The 08-21 limit at 121.00 is replaced, not
  repeated: 121 now only prints if the thesis is broken.
- sources: https://www.investing.com/news/transcripts/earnings-call-transcript-dollar-general-tops-q2-2026-estimates-shares-jump-93CH-4879767 ,
  https://finance.yahoo.com/markets/stocks/articles/dollar-general-q2-2026-earnings-175159974.html

## [06:20 ET] HOUSEKEEPING — stale unfilled orders that should be cancelled, not carried
These are working orders the book still shows as "awaiting entry" and the market has left
behind. None is a position; none is re-pitched here; all should be pulled:
- `BTC SELL @ 63,400` (08-16) and `/MBTU6 SHORT @ 64,340` (08-18) — **BTC is 78,735**, fetched
  from CoinGecko. Both are 21-23% away and were bearish calls the tape refuted. `/MBTU6` is
  additionally the **September contract, inside its final trading period** — per
  `config/universe.md` that alone disqualifies carrying it silently.
- `KXFEDDECISION-26SEP-H25 YES @ 32` (08-22) — the market is now **52 bid / 53 ask**. The
  order was right about direction and will never fill at 32; leaving it working is a
  standing bid nobody will hit.
- `XLE BUY @ 63.90` (08-15, published 5x) — XLE closed 64.06 and gaps up on today's escalation.
- `EEM BUY @ 65.60` (08-21) — EEM closed 68.70, +4.7% above the limit.
- `CEG BUY @ 272.00` (08-21) — CEG closed 298.96 after +4.88% Friday, 9.9% above the limit.
- `VST BUY @ 128.00` (08-24) — VST closed 149.30 after +3.52% Friday, 16.6% above.
- `DINO BUY @ 99.50` (08-22) — DINO closed 105.41, 5.9% above.
Not researched enough to re-price today; flagged so synthesis does not present them as live
opportunities at levels the market abandoned weeks ago.

## [06:22 ET] NEW IDEA — LMT buy, long_term, ACCUMULATE ONLY BELOW 495. Captured, conviction 4.
The anomaly that started it: **defense is in a bear market during a shooting war.** Fetched —
LMT 525.28 (-24.1% off its 692.00 high), NOC 514.98 (-33.5% off high, only +7.5% off its
479.02 low), RTX 200.79 (-11.5%), ITA 225.61 sitting on its 200-day at 229.45. All below their
20- and 50-day averages, on day 191 of a US-Iran air and naval campaign.
- **Why they fell** (searched, not assumed): production ramps bottlenecked behind appropriations
  not yet through Congress; NOC cut its own guidance on a space-program wind-down and cited
  inflation, labour and supply chain; the group entered 2026 on premium multiples. The White
  House has separately summoned Pentagon officials and the primes over **domestic munitions
  shortages** — a demand signal the tape read as blame.
- **What did not deteriorate:** LMT quarterly actuals 6.95 / 7.43 / 6.44 / 7.94 = **$28.76 TTM**,
  beats of +8.2%, +29.0%, +10.5% against one -5.2% miss. 525.28 = **18.3x**.
- **Divergence:** analyst revision direction **improving** — bullish share 46.4% (+7.1),
  strong_buy 5->6, hold 16->14, while the stock fell 24%.
- **Against it:** ZERO open-market insider buys at LMT, NOC or RTX in six months. Recorded in
  key_risk as a conspicuous absence, not spun as neutral.
- **The level is the discipline.** From 525 the ratio against a 437.25 bear case (the actual
  52-week low, 15.2x) is **1.45** and it does not publish. Below 495 it is **2.51**. So the
  recommendation is `wait: true` and accumulate in thirds under 495 / 475 / 460.
- Invalidation is a development, not a price: two consecutive quarters of segment margin
  decline with new fixed-price charges, or an enacted FY27 baseline below $895B in real terms.
- sources: https://www.tikr.com/blog/lockheed-martin-has-fallen-nearly-25-from-its-2026-high-is-it-finally-time-to-buy ,
  https://www.defensenews.com/news/your-military/2026/04/02/us-defense-stocks-see-no-iran-war-lift-after-early-surge/

## [06:23 ET] CRYPTO — swept, nothing captured
Fetched CoinGecko: BTC 78,721 (-0.86% 24h, $1,581B cap, $28.1B vol), ETH 2,488.55 (-0.04%),
SOL 103.67 (-1.28%), XRP 1.40 (-0.13%), DOGE 0.09 (+1.10%), ADA 0.22 (+0.88%),
AVAX 8.17 (+3.66%), LINK 12.70 (-4.57%). A flat, directionless 24 hours across the complex
with no dispersion worth trading and no catalyst I could date. Nothing captured rather than
something manufactured. Note BTC at 78.7k is ~23% above the two stale bearish orders the book
still has working at 63,400 and 64,340 — see the housekeeping block.

## [06:24 ET] POSITION UPDATE — SVRA — coverage gap from earlier in this run, now closed
Earlier I recorded "no news checked on SVRA" as a gap. Checked, and it mattered:
- **The PDUFA date is 2026-11-22, not 2026-08-22.** The FDA extended the MOLBREEVI
  (molgramostim inhalation solution, autoimmune PAP) BLA review by three months in April.
- Reason: the company's **own responses to information requests were deemed a major amendment**
  to the BLA. The agency **cited no safety, efficacy or manufacturing concern**. Breakthrough
  Therapy + Fast Track + Orphan Drug (FDA and EMA).
- decision: **hold, unchanged levels, but the horizon was wrong.** This is a 75-day hold on one
  agency decision, filed as a swing. Re-captured with the dated catalyst attached and a
  2026-11-25 time stop. Size stays 1%, tier lottery: 30-day dollar volume ~$8M, and a CRL gaps
  through the 4.60 stop rather than filling at it. Dilution risk named — a pre-commercial
  company approaching a launch is the standard profile for a raise.
- R:R 3.53, stop 3.95 ATR below entry (ATR14 0.19). win_prob 0.35 vs a 0.221 baseline.
- sources: https://www.stocktitan.net/news/SVRA/savara-announces-the-u-s-food-drug-administration-fda-has-extended-x7v5whz88c2u.html ,
  https://www.biopharminternational.com/view/fda-extends-review-of-savara-s-molgramostim-bla-for-pap

## [06:25 ET] SELF-CHECK — every captured candidate recomputed from its own numbers
Ran the arithmetic independently of what I wrote in each candidate (R:R from entry/target/risk
level, stop distance in ATRs against the asset-class floor, win probability against the
1/(1+R:R) baseline, and evidence-kind count against the claimed conviction):

| Sym | Dir | Horizon | R:R (floor) | Stop ATRs (floor) | win_p vs base | Expectancy | Evid kinds -> conv |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | sell_short | swing | 2.19 (2.0) OK | 1.91 (1.8) OK | 0.42 vs 0.313 OK | +0.340 | 4 -> supports 5, claimed 4 |
| BCC | buy | swing | 2.94 (2.0) OK | 2.07 (2.0) OK | 0.38 vs 0.254 OK | +0.498 | 3 -> supports 4, claimed 3 |
| DG | buy | swing | 2.30 (2.0) OK | 2.14 (2.0) OK | 0.42 vs 0.303 OK | +0.387 | 4 -> supports 5, claimed 5 |
| LMT | buy | long_term | 2.51 (2.5) OK | n/a (bear case) | 0.40 vs 0.285 OK | +0.404 | 3 -> supports 4, claimed 4 |
| SVRA | buy | swing | 3.53 (2.0) OK | 3.95 (2.0) OK | 0.35 vs 0.221 OK | +0.587 | 3 -> supports 4, claimed 4 |
LULU, TLT, GLD and NKE are exit instructions with no target, so they carry no ratio by design.
No conviction score exceeds what its evidence supports; three are claimed *below* it.

**One number the red team should press on: LMT at 2.51 against a 2.5 floor.** That is the
smell of a level tuned to pass, so here is exactly what was tuned. The target (640) and the
bear case (437.25, the actual 52-week low) were set first and never moved; the **entry** was
then solved for the floor, which is why the recommendation is "do not buy at 525, accumulate
below 495" rather than a target stretched to make 525 work. For a `long_term` idea an entry
rule is the prescribed shape, and refusing to buy above a price is a stricter constraint than
the alternative, not a looser one. If that reasoning does not hold, the idea should be cut
rather than re-levelled.

## [06:29 ET] MACRO — the market's full distribution for Friday's August CPI (Kalshi KXCPI-26AUG)
Buckets resolve on the single-decimal m/m print, 2026-09-11. Fetched by direct curl
(yes_bid/yes_ask cents), then differenced into a distribution:
| Market | "Above X%" | yes bid/ask | => P(print >= X+0.1) |
| --- | --- | --- | --- |
| T0.1 | above 0.1% | 97/100 | 99% |
| T0.2 | above 0.2% | 86/96 | 96% |
| T0.3 | above 0.3% | 64/65 | 64% |
| T0.4 | above 0.4% | 12/13 | 12% |
| T0.5 | above 0.5% | 0/13 | ~0-13% (illiquid, no bid) |
Implied bucket probabilities: **0.3% -> 32%, 0.4% -> 52%, 0.5% -> 12%, <=0.2% -> 4%.**
**The modal expectation is +0.4% m/m**, and the market repriced *hotter* on the last session:
T0.2 went 85 -> 96 and T0.3 went 52 -> 64. Open interest 16.7k / 25.3k / 27.6k on the three
live buckets. Source: https://api.elections.kalshi.com/trade-api/v2/markets/KXCPI-26AUG-T0.3

Context for how big that is: headline m/m was **-0.42% in June and +0.07% in July**. A +0.4%
August is a sharp re-acceleration, and the obvious mechanism is energy — USO ran from the
low 120s through August to 141.96, and gasoline follows crude with a two-to-four week lag.

## [06:30 ET] REJECTED — KXCPI-26AUG buckets — the market repriced on information I do not have
Tempting, because I have the underlying series and the market's whole distribution. But my own
estimate (+0.25% to +0.35%, built from core running ~+0.22% at a 79% weight plus an energy
contribution I eyeballed off USO) is *less* precise than the market's, not more — I have no
August retail gasoline survey, no used-vehicle auction data and no shelter read. Forecasting a
single-decimal CPI print against 25k of open interest that moved 12 points on the last session
is a guess wearing a probability. `config/universe.md` requires an explicit and defended
probability disagreement; I have an explicit *agreement*.

**It is used as evidence rather than traded, and it points the same way as the book.** A 96%
chance of >=0.3% and a 52% modal 0.4% five days before an FOMC already 53% priced to hike is
confirmation for the SPY short, for closing the TLT long, and for the DG trade-down thesis —
DG is the one position that wants exactly this print.

## [06:28 ET] REJECTED — refiners (VLO / MPC / PSX / DINO) — the purest form of today's problem
Fetched, and the numbers speak for themselves:
| Sym | Last | Off 52w high | Off 52w low | vs SMA200 |
| --- | --- | --- | --- | --- |
| VLO | 370.72 | **-1.2%** | +131.8% | 239.67 |
| MPC | 388.90 | **-2.4%** | +140.2% | 241.67 |
| PSX | 255.09 | **-2.1%** | +100.6% | 172.39 |
| DINO | 105.41 | **-2.6%** | +130.6% | 65.64 |
Four refiners that have roughly doubled or better, every one within 3% of a 52-week high.

**This is the single clearest statement about today's tape and it is why this report opens no
new energy position.** Crude (USO -7.9% off high), refiners (-1.2% to -2.6%), tankers (FRO
-2.0%, STNG -5.8%), LNG (Cheniere -3.0%) and energy equities (XLE -2.2%) are ALL within 10% of
52-week highs after six months of a closed Strait of Hormuz. The market has had 191 days to
price this and has done so thoroughly. Anything bought here is bought from someone who was
early. The two positions this report did open — DG and LMT — are both on the *cost* side of the
same shock rather than the beneficiary side, which is deliberate.

## [06:29 ET] REJECTED — cruise lines (CCL / RCL / NCLH) and FDX — the victims are priced too
Last check of the cost side of the energy shock, and it closes the loop:
| Sym | Last | Off 52w high | Off 52w low | Position |
| --- | --- | --- | --- | --- |
| CCL | 23.51 | -30.9% | **+1.9%** | inside its 40d support 23.07-23.89, at the 52w low |
| NCLH | 15.57 | -38.0% | +7.2% | inside its 40d support 15.31-15.48 |
| RCL | 265.19 | -25.6% | +14.3% | inside its 40d support 262.04-267.45 |
All three below SMA20/50/200. Fuel is 10-15% of cruise operating cost and the customer is the
same one trading down to DG, so the thesis is right — and it is already in the price. Shorting
a name 1.9% off its 52-week low is not a trade.
FDX 322.52 reports **2026-09-16 AMC, the same afternoon as the 14:00 FOMC**. -6.6% off its
high, above SMA50 319.44 and SMA200 287.93. A fuel-exposed logistics print colliding with a
rate decision is two coin flips in one session, not an edge. Watchlist.

## [06:30 ET] THE SHAPE OF THE TAPE, in one line
Every beneficiary of the Hormuz closure is within 3% of a 52-week high after a 100-140% move;
every victim of it is within 8% of a 52-week low. The shock is 191 days old and the market has
priced both sides of it thoroughly. The only two things I found that it has *not* priced are
beneficiaries filed under the wrong heading: **DG**, a defensive retailer whose own guidance
raise names middle-income trade-down as the driver, and **LMT**, a war contractor de-rated 24%
on a congressional appropriations calendar rather than on demand. Both are captured. Everything
else this run went to the watchlist or to position management, and the six-line house-keeping
block above matters as much as the two new ideas.

## [06:31 ET] DG RE-CAPTURED — a claim in the first version was imprecise, and the bars fixed it
I wrote that "the 08-27 print re-rated the stock through its 200-day". Pulled the daily bars to
check and it did not happen that way:
- 08-26 c122.78 → **08-27 (print) o127.84 h132.50 l124.50 c125.89 on 6.4M** — gapped up, ran,
  and **faded to close near the low of the gap**.
- 08-28 c122.89 on 3.3M — gave back essentially all of it.
- Then 126.75 / 131.09 / 130.89 / 131.26 / 133.21 on 4.2 / 3.9 / 2.8 / 1.7 / 1.7M.
- The 200-day at 126.10 was reclaimed on **2026-09-01**, three sessions after the print.
That is post-earnings drift — a re-rating the market *rejected* on the day and accepted over the
following week — which is a better setup than a headline gap, not a worse one, and it is why the
134.20 trigger sits above both the 132.50 print high and the 134.12 drift high.
**The bars also produced a risk the first version missed and the re-capture carries:** the drift
into resistance is on FALLING volume, 1.7M on each of the last two sessions against 6.4M on the
print. A breakout carried by the thinnest tape of the month is the kind that fails back into the
range. Added to key_risk; the 125.60 stop under the 200-day is what it is for.
Synthesis takes the last entry per symbol, so the corrected DG line is the one that counts.

## [06:32 ET] RESEARCH COMPLETE (final — supersedes the premature block at 06:12)
Timestamp read from `date`. Run started 06:00:50 ET.

**candidates: 10 lines, 9 distinct symbols** (DG captured twice; the second, corrected line is
the one synthesis should take).

| Symbol | Action | Horizon | Conv | Kind |
| --- | --- | --- | --- | --- |
| DG | BUY, breakout stop-limit >134.20, stop 125.60, target 155 | swing | 5 | **new** |
| LMT | BUY, accumulate **only below 495**, bear case 437.25, target 640 | long_term | 4 | **new** |
| SVRA | HOLD — PDUFA re-dated to 2026-11-22, horizon fixed | swing | 4 | amend |
| SPY | HOLD the short, levels unchanged, mechanism now measured | swing | 4 | amend |
| BCC | HOLD — target cut 110 → 91.50, stop 71.40 added | swing | 3 | amend |
| GLD | **TRIM HALF**, 388.00 invalidation on the remainder | swing | 3 | reduce |
| TLT | **CLOSE THE LONG LEG**, keep the short (netting fix) | swing | 4 | reduce |
| LULU | **CLOSE** | swing | 4 | close |
| NKE | **CLOSE** | swing | 3 | close |

**Every line was recomputed independently — see the 06:25 self-check.** All five with ratios
clear their floor, all four with stops clear the ATR floor, all five beat the win-probability
baseline with positive expectancy, and no conviction exceeds what its evidence supports.

**The finding of the day is a regime, and both new ideas fall out of it.** The Strait of Hormuz
has been effectively closed for 191 days; Gulf crude exports are down 47%; Brent is near $99.
The Fed under Kevin Warsh is priced **53% to HIKE on 2026-09-16**, and Friday's August CPI is
priced 96% to come in at +0.3% or hotter. Against that, the market has priced the shock
thoroughly on both sides — every beneficiary (refiners, tankers, LNG, energy equities, crude) is
within 3% of a 52-week high after a 100-140% move; every victim (airlines, cruise lines) is
within 8% of a 52-week low. **The only two things I found unpriced were beneficiaries filed
under the wrong heading:** DG, a defensive retailer whose own guidance raise names middle-income
trade-down as the driver, and LMT, a war contractor de-rated 24% on an appropriations calendar
rather than on demand.

**Correlation warning for synthesis and the red team.** Four lines (SPY, TLT, GLD, BCC) resolve
on the same driver — the 09-11 CPI and the 09-16 FOMC — against a stated cap of 3. They stand
because they are exposure *reductions* rather than four bets on one print, and because DG is
deliberately positioned on the opposite side of that same print. But they must not be counted as
four independent ideas.

**Also for synthesis: the 06:20 housekeeping block is not optional.** Seven unfilled orders the
book still shows as "awaiting entry" are at levels the market abandoned weeks ago — including a
BTC short at 63,400 and a `/MBTU6` short at 64,340 against a spot of 78,721, with `/MBTU6` now
inside its final trading period. They should be presented as cancellations, not opportunities.

**coverage gaps:**
- **No live index, VIX, DXY, overnight futures or spot gold/WTI.** Yahoo returned HTTP 429 for
  every index symbol. ETF proxies via finnhub only. No volatility read this run at all.
- **No small- or micro-cap hunt** beyond the SVRA position already held. The 36 sub-$300M-revenue
  names reporting inside 12 days were listed and none researched — buying a small cap before a
  print is a coin flip I had no time to handicap.
- **Nothing captured in crypto or futures.** Crypto was swept (8 coins, all flat, no dispersion,
  no dateable catalyst). No futures idea: the one the regime argued for, long /MCL, is chasing a
  three-day run to above the sell-side's own year-end target.
- **No event contract captured, and both candidates were rejected on the same principle** — I had
  no defensible probability disagreement on either the FOMC (53/47, 10.2M OI) or the August CPI
  (where my own estimate was *less* precise than the market's). Both are used as evidence instead.
- CCJ reviewed against fetched levels and left as a hold with no recommendation; its bear case
  (80.00) and ratio (2.93) from 2026-09-06 still stand and nothing changed over the single
  intervening session.
- ORCL, ADBE, ITA/NOC/RTX, JETS/DAL/UAL/LUV, LEN/ITB/XHB, CCL/RCL/NCLH, FDX and the refiners
  were all worked and rejected with levels and reasons — see the REJECTED blocks. They are
  watchlist material, not unexamined.

**sources that failed:**
- Yahoo Finance — HTTP 429 on every index symbol (^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES=F, NQ=F,
  DX-Y.NYB, ^TNX, GC=F, CL=F).
- finnhub indices — "Market data subscription required for CFD indices".
- stooq — 404 on all ^-prefixed symbols. alphavantage — no API key.
- `market_data.py short LMT` — nasdaq read timeout.
- **`market_data.py events` — a code bug, not an outage.** Kalshi renamed its market fields to a
  `_dollars`/`_fp` suffix (`yes_bid_dollars`, `yes_ask_dollars`, `last_price_dollars`,
  `volume_24h_fp`, `open_interest_fp`); the wrapper still reads `yes_bid`/`yes_ask`/`last_price`/
  `volume`, so **every event contract it returns has null prices**, and a search for "Fed"
  returned four multi-leg tennis and baseball shards. All event prices in this log came from
  direct curl against api.elections.kalshi.com. Worth fixing before the next run.
- The Robinhood futures-availability URL cited in `config/universe.md`
  (`.../futures-contracts-available-on-robinhood/`) now **404s**; availability was verified
  against `.../before-trading-a-futures-contract/` instead. Also worth fixing in config.

## [06:33 ET] ADDENDUM after RESEARCH COMPLETE — financials swept, rejected, picture now closed
The one sector the regime argued for that I had not checked: a hiking Fed with a +41bp 2s10s
should be a net-interest-margin tailwind for banks. Fetched, and it is already in the price:
- **XLF 58.10 — 0.8% off its 52-week high of 58.60**, above SMA20 57.86 / SMA50 56.86 /
  SMA200 53.49. There is no entry in an index sitting on its high with a 1.15% ATR.
- KRE 75.27, -3.9% off high, sitting **exactly on** its 20-day (75.38) and 50-day (75.63) — a
  neutral chart with no edge either way. Separately and decisively: **KRE is this report's
  canonical failure**, republished three times at an unchanged 76.80 entry with the stop walked
  from 74.20 to 75.20 to lift a ratio while making the trade worse, then stopped out
  2026-08-19. It is not being pitched a fourth time on a flat chart.
- KBE 69.34, -3.6% off high, also pinned to its 20- and 50-day.

**With financials checked, the picture is closed and it is consistent.** Everything the energy
shock and the rate path *help* — refiners, tankers, LNG, energy equities, banks — trades within
4% of a 52-week high. Everything they *hurt* — airlines, cruise lines, homebuilders, athleisure
— trades within 8% of a 52-week low. A tape that has fully expressed a view in both directions
offers position management and two odd-lot exceptions, which is exactly what this run produced.
No change to the candidate file; nothing here cleared the bar.
