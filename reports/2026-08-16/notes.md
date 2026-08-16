# Research log — 2026-08-16

## [06:25 ET] SETUP — Sunday 2026-08-16, weekend run
- US equities/futures closed. Per config/strategy.md weekend rules: crypto + event
  contracts carry actionable weight; equities = week-ahead prep, entry at next open
  (Mon 2026-08-18 — correction: Mon is 2026-08-17).
- Open positions to manage: KRE (buy 76.8, tgt 82.5, stop 74.2, opened 08-15),
  XLE (buy 60.8, tgt 67.0, stop 57.8, opened 08-15). Both 1 day old, 0 closed trades.
- Track record: 0 closed of 2 — sample is nil, no category bar adjustment justified.
- Prior gap: 2026-08-14 produced ZERO candidates from 38k chars of notes. 2026-08-15
  produced 5 (target 6-8). Priority today: capture early, capture often.

## [06:25 ET] MACRO — rates, curve, crypto
- US10Y 4.63% (2026-08-13), prev 4.68 — source: FRED DGS10
- US2Y 4.15% (2026-08-13), prev 4.20 — source: FRED DGS2
- 10y-2y curve +0.51 (2026-08-14), prev +0.48 — steepening — source: FRED T10Y2Y
- Fed funds effective 3.63% (2026-08-13), unchanged — source: FRED DFF
- Unemployment 4.1% (Jul 2026), prev 4.2% — source: FRED UNRATE
- BTC $62,934 (-0.04% 24h); ETH $1,878.12 (+0.04%); SOL $75.15 (-0.13%)
  — source: CoinGecko via market_data.py, 2026-08-16T10:24Z
- 20y Treasury proxy 82.04 (-0.67%) — source: finnhub
- Read: crypto is dead flat over 24h — low realized vol into the weekend. Rates
  easing at both ends with a steepening curve; fed funds 3.63% vs 2y 4.15% means
  the 2y is pricing NO near-term cuts and possibly a hike premium. That is a
  hawkish-repricing tape, not a cutting tape.

## [06:25 ET] DATA QUALITY — source failures
- Yahoo Finance returning HTTP 429 (rate limited) for ALL index/ETF symbols:
  ^GSPC ^NDX ^DJI ^RUT ^VIX ES=F NQ=F DX-Y.NYB ^TNX GC=F CL=F all FAILED.
- Finnhub rejects indices ("Market data subscription required for CFD indices").
- Stooq 404s on ^-prefixed symbols. AlphaVantage: no API key configured.
- CONSEQUENCE: no live VIX, no index levels, no gold/WTI/DXY spot yet. Must source
  equity/ETF levels from `history` subcommand or web; will retest quote endpoint.

## [06:28 ET] LEVELS — Friday 2026-08-14 closes (finnhub, asof 20:00 UTC = 16:00 ET)
SPY 776.34 (-0.20%) | QQQ 731.07 (-0.14%) | IWM 305.09 (+0.52%) | TLT 82.04 (-0.67%)
GLD 401.48 (+0.63%) | SLV 58.48 (+0.55%) | GDX 89.97 (+1.93%) | USO 126.60 (+1.26%)
XLF 58.16 (-0.17%) | XLU 44.31 (+0.61%) | XLV 167.37 (-0.60%) | SMH 587.82 (-0.22%)
XBI 157.41 (+0.35%) | ARKK 81.10 (-1.80%) | EEM 66.61 (-0.10%) | FXI 34.89 (+0.09%)
URA 44.93 (-0.71%) | COPX 85.70 (+0.21%)
- Friday tape read: precious metals + energy led (GDX +1.9, USO +1.3, GLD +0.6);
  long duration and high-beta growth lagged (TLT -0.67, ARKK -1.8). That is a
  reflation/inflation-hedge rotation, not a risk-off. IWM +0.5 vs QQQ -0.14
  confirms it is rotation within risk, not de-risking.

## [06:28 ET] CATALYST CALENDAR — dated earnings inside 10 sessions (finnhub)
RETAIL/CONSUMER WEEK is the dominant cluster:
- Mon 2026-08-17 amc: FN
- Tue 2026-08-18 bmo: **HD** (rev~$48.7B, eps~4.88), BIDU, BZ; amc: KEYS, TOL
- Wed 2026-08-19 bmo: **TGT** (~$26.3B), **LOW** (~$26.5B), **TJX** (~$15.3B),
  **ADI** (~$4.0B), ROST, EL
- Thu 2026-08-20 bmo: **WMT** (~$188.8B), **BABA** (~$274.3B CNY), **DE** (~$11.1B), NTES
- Fri 2026-08-21: BJ
- Mon 2026-08-24 bmo: PDD; XPEV, DKS, PVH
- Tue 2026-08-25 amc: INTU, ZM
- Wed 2026-08-26 amc: **NVDA** (rev est ~$93.6B, eps~2.13), CRM, HPQ, CRWD, SNPS
- Implication: Aug 18-20 is a concentrated US-consumer verdict (HD+LOW = housing,
  WMT+TGT+TJX+ROST = staples/discretionary split). NVDA is the megacap AI print
  but sits 8 sessions out — too far for a same-week swing entry today.

## [06:29 ET] SOURCE FAIL — Kalshi event contracts return 0 markets
- `market_data.py events` queried for "Fed", "CPI", "Bitcoin", "recession" — all
  returned ok:true but count:0. The API is reachable; the market list is empty.
- CONSEQUENCE: I have no live event-contract prices. Per the no-fabrication rule I
  will publish ZERO `Robinhood Prediction Markets` ideas today rather than quote a
  cents price I did not fetch. This removes an asset class the weekend playbook
  normally leans on and pushes weight onto crypto + week-ahead equity prep.

## [06:33 ET] MACRO — what actually drove last week's tape
Two independent shocks, and they explain the whole Friday rotation:
1. **Cooler-than-expected CPI (~Aug 12)** cut the odds of a Fed rate HIKE (2026's
   regime is hike-risk, not cut-hope). Gold broke a five-month correction; gold
   miners had their best week in years, benchmark funds +20%+.
   - source: https://www.cnbc.com/2026/08/12/gold-prices-metals-fed-rate-hike-inflation.html
   - source: https://www.mining.com/gold-miners-surge-more-than-20-in-breakout-week/
   - source: https://www.fool.com/investing/2026/08/13/gold-is-up-sharply-in-august-whats-driving-it-high/
2. **Strait of Hormuz re-escalated Friday Aug 14** — fresh tanker attacks and
   sharper Washington/Tehran rhetoric. NYMEX WTI Sep settled **$82.40** (+$1.15,
   +1.42%) Friday; +5% on the week, +7.8% over 7 days.
   - source: https://www.dtnpf.com/agriculture/web/ag/news/world-policy/article/2026/08/14/oil-prices-rise-tanker-attacks
   - source: https://www.tradingkey.com/news/market-movers/262104960-market-movers-usoil-20260814
- IMPORTANT NUANCE: earlier in the week the tape was trading a *prospective
  US-Iran Hormuz agreement*, which pushed oil DOWN and helped the disinflation
  story. Friday reversed it. So Hormuz is a two-sided headline generator, not a
  one-way bull driver — this caps how much conviction any oil-long deserves.
- These two shocks partly conflict: an oil spike is inflationary and undercuts the
  cooler-CPI/no-hike premise that gold just rallied on. They cannot both keep
  working. That tension is the single most important thing in this week's tape.

## [06:34 ET] VENUE CHECK — Robinhood prediction markets ARE live
- Found live RH prediction-market event pages (e.g. WTI oil price events dated
  2026-08-14), so the venue exists and carries commodity events.
  - source: https://robinhood.com/us/en/prediction-markets/financial/events/oil-price-wti-on-aug-14-2026-aug-14-2026/
- BUT my Kalshi feed returns 0 markets, so I still have no live cents price. I am
  NOT publishing an event contract on a price I could not fetch. Gap, not a reject.

## [06:36 ET] CATALYST CALENDAR — economic events, week of 2026-08-17
- Mon 08-17: Empire State Manufacturing, NAHB Housing Market Index
- Tue 08-18: Export Prices, **Housing Starts**
- Wed 08-19 (afternoon, standard 14:00 ET): **FOMC minutes of the July 28-29
  meeting** — the week's single most important scheduled event. THREE officials
  dissented in favour of a rate HIKE at that meeting.
- **Reddit (RDDT) joins the S&P 500 this week** — flagged as a headline event.
- Jackson Hole symposium is **27-29 Aug**, i.e. the FOLLOWING week. Fed Chair is
  **Warsh**; this is his first Jackson Hole keynote. Not tradeable inside a
  10-session swing entered Monday, but it is the reason positioning stays tight.
- source: https://www.capitalstreetfx.com/market-analysis/week-ahead-1721-august-2026-fomc-minutes/
- source: https://www.fxstreet.com/analysis/forecasting-the-upcoming-week-focus-shifts-to-the-fomc-minutes-and-the-jackson-hole-symposium-202508151843
- READ: macro data is light; the week is (a) the retail-earnings verdict on the US
  consumer, (b) Wednesday's minutes as a hawkishness gauge, (c) an index event.
  Three genuinely independent drivers — good for diversifying the book.

## [06:40 ET] REJECTED — AVB/EQR merger arb — spread is 0.10%, no edge
- EQR and AvalonBay are merging all-stock at a FIXED 2.793 EQR per AVB share.
  - source: https://www.stocktitan.net/sec-filings/EQR/s-4-equity-residential-business-combination-registration-cfa05948eab6.html
- Math on Friday 2026-08-14 closes: 2.793 x 65.97 (EQR) = $184.25 implied.
  AVB closed $184.06. Spread $0.19 = 0.10%. Deal closes 2H 2026.
- That is well inside transaction cost for a multi-month hold. No trade. AVB is
  now simply a levered EQR proxy, so it also carries no independent thesis.
- Worth noting for the RDDT idea below: this merger is WHY there is an S&P 500
  vacancy at all — the index change is off-cycle, driven by AVB's pending
  acquisition, not by a quarterly rebalance.

## [06:41 ET] CATALYST — RDDT joins S&P 500 before the open Tue 2026-08-18
- S&P DJI announced 2026-08-13; RDDT replaces AVB effective prior to the open on
  Tuesday 2026-08-18. Shares jumped as much as 11% after hours on the news.
  - source: https://www.morningstar.com/news/business-wire/20260814586211/reddit-will-be-added-to-the-sp-500
  - source: https://qz.com/reddit-sp-500-inclusion-rddt-stock-081426
- Price confirms it: RDDT 158.12 (08-13) -> 178.09 (08-14), +12.6% in one session.
- KEY MECHANIC: index funds must own RDDT at the Tuesday open, so their buying
  executes at the **Monday 2026-08-17 close**. After that print, the entire
  forced bid is gone and the marginal buyer disappears overnight. The
  announcement-pop-then-reversal pattern in index additions is well documented
  and the inclusion premium has decayed sharply in the modern era.
- LEVELS: RDDT last 178.09, atr14 12.25 (6.88% - very high), sma20 165.84,
  sma50 175.03, 120d high 208.05, low 119.27, -14.4% off high.
- So the fade target is the pre-announcement close of 158.12; 175.03 (sma50) and
  165.84 (sma20) are the waypoints. This is a SHORT, entered after the forced
  buying completes, not before.

## [06:43 ET] REJECTED — RDDT short into the post-inclusion fade — R:R will not clear 2.0
- The thesis is sound and the catalyst is precisely dated, but the volatility
  makes it unsizeable. RDDT atr14 = 12.25 points (6.88% of price).
- Best-case construction: short 180.00, stop 196.00 (1.3 ATR, still inside normal
  noise), target 158.12 (the pre-announcement close) = reward 21.9 / risk 16.0 =
  **R:R 1.37**. Widening the stop to a defensible level (208.05, the 120-day high)
  drops it to ~1.0. An intraday version clears 1.5 only with a 0.6-ATR stop that
  daily noise would take out on a normal session.
- Config minimum is 2.0 on swing. It does not publish. Routing the observation to
  the week-ahead watchlist instead of forcing a bad stop onto a good idea.
- Second reason to stand aside: RDDT is a retail-favourite name and shorting it
  requires margin. Squeeze risk is asymmetric against a short with a wide stop.

## [06:47 ET] NEWS/LEVELS — retail week has a clean priced-for-perfection split
Friday 2026-08-14 closes and 120-day structure:
- **HD** 338.86 (-0.83%) | atr 8.52 (2.51%) | sma20 340.69 | sma50 337.70 |
  hi 394.35 lo 289.10 | -14.1% off high. Fell 355.62 (08-07) -> 338.86, -4.7% in
  five sessions, straight INTO its Tuesday print. Sitting exactly on the 50-day.
- **TGT** 154.48 (-0.66%) | atr 3.92 (2.54%) | sma20 145.85 | sma50 137.71 |
  hi 156.47 lo 111.11 | **-1.3% off high**, +12% above its 50-day, +39% off the
  120-day low. Bought hard INTO its Wednesday print.
- **WMT** 115.27 (-0.39%) | atr 2.56 | sma20 112.13 | sma50 114.49 | -14.7% off high
- **LOW** 218.47 | **TJX** 152.11 (-1.11%) | **ROST** 245.36 | **DE** 608.85
- **ADI** 389.39 (+2.16% Friday) | atr 12.68 (3.26%) | sma20 376.53 | sma50 391.57
- READ: the tape has already voted opposite ways on the same consumer. TGT is
  priced for a beat at the top of its range; HD is priced for a miss at its 50-day.
  The interesting one is HD, because its support is real and testable and the
  downside is already partly paid for.

## [06:48 ET] CATALYST CLUSTER — housing gets three dated events in 36 hours
- Mon 08-17: NAHB Housing Market Index
- Tue 08-18 08:30 ET: Housing Starts
- Tue 08-18 bmo: **HD** earnings (rev est ~$48.7B, eps est ~4.88)
- Tue 08-18 amc: **TOL** (Toll Brothers) earnings (rev est ~$2.6B, eps est ~2.94)
- Plus the rate tailwind: 10y fell to 4.63% from 4.68%, and the cooler CPI cut
  hike odds. Lower long rates are the direct transmission into mortgage demand.
- This is a genuinely independent driver from the energy/Hormuz book and from the
  Fed-minutes book, so it diversifies rather than doubling up.

## [06:53 ET] CRYPTO — the weekend tape is dead flat and pinned at support
- Live (CoinGecko, 2026-08-16 ~10:30Z): BTC $62,953 (**-0.01%** 24h), ETH $1,878.65
  (+0.06%), SOL $75.17 (-0.10%), LINK $9.40 (+0.59%), LTC $44.32 (+0.68%),
  ADA $0.1758 (-1.68%), DOGE $0.0697 (-0.40%), AVAX $6.35 (-3.39%).
- Three majors moving less than 0.15% over a full 24 hours is volatility
  compression, not calm. Compression resolves into expansion; it does not persist.
- Structure: BTC is down from **above $93,000 at the start of 2026**, trades below
  BOTH its 20-day and 50-day EMAs, and is caught between **$62,500 support** and
  **$65,000-70,000 resistance**. $62,500-63,500 is explicitly flagged as a
  whipsaw/no-trade chop zone. A confirmed loss of $62,000-62,500 opens $60,000,
  then $57,000. Named drivers: Fed uncertainty and **weakening ETF demand**.
  - source: https://www.investing.com/news/cryptocurrency-news/bitcoin-tests-62k-support-with-breakout-looming-live-levels-93CH-4829888
  - source: https://www.thecoinrepublic.com/2026/08/14/bitcoin-price-usd-could-fall-to-57k-if-62k-support-breaks-now/
  - source: https://blog.bitfinex.com/bitfinex-alpha/strong-resistance-continues-long-term-holder-supply-declines/
- CONFLICTING SOURCE, flagged rather than resolved: one aggregator described BTC
  "recovering to the $75,000-85,000 range" in 2026. That is inconsistent with my
  own fetched spot of $62,953 and with every level-based source above. I am
  trusting the fetched price and the level analysis; noting the disagreement.
- TRADE LOGIC: a long here has ~$2,200 of room to resistance and ~$3,000 to the
  first downside objective, with spot sitting inside a declared chop zone. That is
  a bad long. Robinhood Crypto has no spot shorting, so the expressible bearish
  view is `sell` = reduce/avoid, per config/universe.md.

## [06:58 ET] LEVELS — precious metals are extended, not broken
- GLD 401.48 | atr14 7.38 (1.84%) | sma20 383.06 | sma50 381.30 | 60d hi 421.82
  lo 363.32. Ran 371.54 (07-31) -> 404.92 (08-12), +9%, then consolidated tightly
  398.28-407.36 for five sessions. That is a continuation flag, not a top.
- GDX 89.97 | atr 3.43 (3.81%) | sma20 80.38 | 120d hi 117.18. Ran 74.10 (07-31)
  -> 90.96 (08-12), **+22.8% in eight sessions**, and closes 12% above its 20-day.
- SLV 58.48 | atr 1.75 (3.0%) | sma20 54.71 | -31% off its 120-day high of 85.27.
- CHOICE: GLD over GDX and SLV. GDX at +12% over its 20-day is a chase with a
  3.81% ATR — the same view with worse entry mechanics. Analysts covering the
  move are explicitly eyeing a pullback.
  - source: https://primexbt.com/news/gold-silver-rally-resumes-after-five-month-correction-as-analysts-eye-pullback/
- The breakout-buy math is bad and I am not going to pretend otherwise: buying the
  flag at 407.50 with a stop under 393.00 targets 421.82 for **R:R 0.99**. Only the
  pullback entry into the 383/381 moving-average confluence works. So the
  recommendation is a resting limit that may never fill. That is the honest trade.

## [06:59 ET] LEVELS — TJX is being dumped into its own print
- TJX 152.11 (-1.11% Fri) | atr 3.33 (2.19%) | sma20 157.04 | sma50 157.70 |
  60d hi 170.00 **lo 148.27**. Fell 162.06 (08-06) -> 152.11, -6.1% in six
  sessions, through both moving averages, to within 2.6% of the 60-day low.
  Reports Wed 2026-08-19 bmo.
- Driver is the US off-price consumer — distinct from the Fed book and the oil
  book, so it does not breach the correlation cap.

## [06:59 ET] LEVELS — BABA holding its 20-day into a Thursday print
- BABA 123.81 (+1.35% Fri) | atr 3.93 (3.17%) | sma20 121.81 | sma50 113.76 |
  60d hi 135.89 lo 91.99. Backed off 132.32 (08-10) to 123.81 but holds well above
  a rising 50-day, +35% off the 60-day low. Reports Thu 2026-08-20 bmo.
- Gap support from the Aug 3 breakout: Jul 31 low 119.22, Aug 3 low 126.04.
- China internet is a genuinely independent driver from everything else in the book.

## [07:00 ET] REJECTED — DE (Deere, earnings Thu 08-20) — no edge in the structure
- 608.85, atr 16.89, sma20 611.23, sma50 602.23, 60d range 515.15-643.99. Price is
  pinned between its own 20- and 50-day in the middle of its range. There is no
  support to lean the stop on and no proximate resistance to target. Pass.

## [07:00 ET] CORRELATION AUDIT — driver concentration check
- Oil/Hormuz: XLE (1)
- Fed path / rates: KRE, BTC, GLD (3) — **at the config cap of 3, do not add more**
- Housing + own earnings: HD (1)
- US off-price consumer: TJX (1)
- China internet: BABA (1)
- This is why I am NOT adding a micro Russell (/M2K) or micro gold futures idea
  despite having no futures exposure in the book — both would be a fourth Fed bet.
  An empty asset class is better than breaching the correlation cap.

## [07:05 ET] FALSIFICATION — the case against the book as a whole
Each candidate carries its own counter_argument. These are the objections that
apply to the SET, and they are the ones synthesis should surface to the reader:

1. **The book is 7-of-8 long.** The only bearish expression is trimming BTC. That
   is not a deliberate bullish call — it is what happens when you build from
   beaten-down-into-catalyst setups. If the FOMC minutes read hawkish on
   Wednesday, five of these ideas lose at once regardless of their own merits.
2. **The oil trade and the gold trade contradict each other.** XLE needs Hormuz
   supply fear to persist; GLD needs the cooler-CPI/no-hike premise to hold.
   Sustained $82 crude is inflationary and revives hike risk. Both are in the
   book on purpose — they hedge each other — but they should not be read as
   mutually reinforcing, and nobody should size them as if they were.
3. **HD and TJX are more correlated than the sector labels suggest.** Both are
   "buy a de-rated retailer after its print", and both print inside 24 hours of
   each other. Treat them as roughly 1.5 positions, not 2.
4. **Five of eight say WAIT.** HD, TJX, BABA, ADI and GLD all instruct the reader
   not to enter today. That is the honest answer to a week that is one long
   earnings gauntlet plus a Fed-minutes release, but it means this report is
   mostly a set of resting orders and conditions, not same-day trades.
5. **Conviction is capped at 4, once.** Seven ideas are conviction 3. No idea this
   week has multiple independent confirmations plus a clean level plus no serious
   counter-argument. Publishing seven 3s rather than inventing 4s is the point.
6. **Every earnings entry is post-print by construction** because ATRs here
   (HD 8.52, ADI 12.68, BABA 3.93 with 8% gap history, TJX 3.33) are smaller than
   typical earnings gaps. Stops on these will fill at the opening auction, not at
   the stated level. That is stated in each key_risk and it is not a formality.

## [07:06 ET] REJECTED — AVB intraday index-deletion dislocation (Mon 08-17 close)
- Considered trading AVB against parity into the forced index sell at Monday's
  close. Killed for two reasons: the arb spread is already 0.10%, so any
  dislocation worth trading is ~1%, giving roughly R:R 0.9 against a sensible
  stop; and the trade cannot be run without a live EQR quote to price parity
  against, which I do not have on a Sunday. Not tradeable as specified.

## [07:07 ET] RESEARCH COMPLETE
- candidates: 8 (XLE, KRE, HD, BTC, GLD, BABA, TJX, ADI)
  - 2 of these are POSITION UPDATES to open trades: XLE (hold, raise stop
    57.80 -> 58.60, cap first target at 64.50) and KRE (hold, raise stop
    74.20 -> 75.30, new money waits for Wednesday minutes).
  - all 8 clear the 2.0 swing reward-to-risk minimum; ratios verified by hand.
  - conviction: one 4 (XLE), seven 3s. No 5s and no 2s.
- horizon mix: 8 swing, **0 intraday** — deliberate. It is Sunday, US equities and
  futures are shut, and config/strategy.md directs weekend runs to treat equities
  as week-ahead preparation. Every equity entry here is for the next open or
  later. This misses the 2-3 intraday target and synthesis should say so.
- asset-class mix: 4 stock, 3 etf, 1 crypto, **0 futures, 0 event contracts**.
- coverage gaps:
  - **Event contracts: none published.** The Kalshi feed returned 0 markets for
    every query, so I had no live cents prices. Robinhood prediction markets are
    demonstrably live (verified an RH WTI event page), so this is my data gap, not
    a venue absence. Publishing a probability disagreement against a price I did
    not fetch would violate the no-fabrication rule.
  - **Futures: none published.** Not a data gap — a correlation decision. The
    obvious micro contracts (/M2K, /MGC) would each have been a fourth idea keyed
    to the Fed path, and the config cap is three per driver.
  - No live VIX, index levels, DXY, spot gold, or WTI reading from the tooling —
    Yahoo returned HTTP 429 across the board and Finnhub will not serve indices.
    The $82.40 WTI settle used in the XLE thesis is sourced from news, not fetched.
  - Did not reach: WMT/TGT/LOW/ROST level work, NVDA (Aug 26, outside horizon),
    insider Form 4 detail, sector breadth, or crypto beyond the top eight coins.
- sources that failed: Yahoo Finance (429 on all symbols), Finnhub indices
  (subscription required), Stooq (404 on ^-prefixed symbols), AlphaVantage (no API
  key), Kalshi events (reachable, 0 markets returned), nasdaq history for BTC-USD.
- sources that worked: Finnhub quotes/earnings, Nasdaq daily history, FRED,
  CoinGecko, SEC EDGAR, WebSearch.
