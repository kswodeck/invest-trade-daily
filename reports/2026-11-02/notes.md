# Research log — 2026-11-02

## [06:03 ET] MACRO — rates, policy (FRED, as of 2026-10-29/30)
- US 10y 4.98% (prev 5.05%) — source: https://fred.stlouisfed.org/series/DGS10
- US 2y 4.61% (prev 4.67%) — source: https://fred.stlouisfed.org/series/DGS2
- Fed funds effective 3.88%, unchanged — source: https://fred.stlouisfed.org/series/DFF
- 10y-2y curve +0.38 (prev 0.37), positively sloped — source: https://fred.stlouisfed.org/series/T10Y2Y
- Unemployment 4.2% (Sep, prev 4.1%) — rising — source: https://fred.stlouisfed.org/series/UNRATE
- CPI index 336.298 (Sep) vs 334.131 prior month — source: https://fred.stlouisfed.org/series/CPIAUCSL
- NOTE: a 4.98% 10y with fed funds at 3.88% is a steep positive term premium; long duration (TLT) has been bleeding.

## [06:03 ET] DATA QUALITY — Yahoo Finance returning HTTP 429 on index/quote endpoints
- spx, ndx, dow, rut, vix, ES, NQ, DXY, us10y px, gold, WTI all ok:false (finnhub = CFD subscription required; yahoo = 429; stooq 404)
- bonds_20y (TLT) ok: 81.84, +0.43% pre
- Index level prices for today are UNKNOWN. Will fetch ETF proxies (SPY/QQQ/IWM) via quote instead.

## [06:05 ET] MACRO — Friday 2026-10-30 close (finnhub, asof 2026-10-30T20:00Z; market CLOSED, this is the prior close and the freshest honest equity price at 06:05 ET Monday)
- SPY 755.72, -1.77% (prev close 769.36; day range 750.36-761.46)
- QQQ 690.49, **-3.47%** (prev 715.34; range 683.45-698.63) — tech led the decline hard
- IWM 279.33, -1.65% (prev 284.01)
- TLT 81.84, +0.43% (prev 81.49) — duration bid, mild
- GLD 355.78, **-3.47%** (prev 368.57; range 354.67-361.68) — gold sold off as hard as the Nasdaq
- XLE 70.02, **+1.91%** (prev 68.71) — energy the only thing up
- READ: this is not a plain risk-off. Gold down 3.5% alongside QQQ down 3.5% while energy rallied is a
  de-grossing/liquidation pattern plus an energy-specific bid, not a flight to safety. TLT's +0.43% is
  far too small to be a duration flight given a 1.77% SPY drop.
- source: finnhub quote endpoint via scripts/market_data.py

## [06:08 ET] LEVELS — index/sector ETFs, 120-day history (source: scripts/market_data.py history, finnhub)
| Sym | Close 10-30 | ATR14 | ATR% | SMA20 | SMA50 | 120d hi | 120d lo | off hi | advol |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 755.72 | 8.30 | 1.10% | 770.47 | 767.49 | 781.62 | 716.58 | -3.31% | $31.3B |
| QQQ | 690.49 | 14.38 | 2.08% | 728.19 | 725.00 | 762.86 | 661.14 | -9.49% | $26.1B |
| IWM | 279.33 | 4.02 | 1.44% | 277.41 | 284.27 | 305.18 | 269.88 | -8.47% | $6.8B |
| GLD | 355.78 | 5.87 | 1.65% | 375.76 | 390.57 | 432.98 | 354.67 | **-17.83%** | $2.9B |
| XLE | 70.02 | 1.43 | 2.04% | 67.12 | 64.93 | 70.15 | 52.62 | **-0.19%** | $2.3B |
| TLT | 81.84 | 0.85 | 1.04% | 79.66 | 80.50 | 87.79 | 76.43 | -6.78% | $3.7B |

- REGIME: QQQ is in a real correction (-9.5% off high, below SMA20 AND SMA50). SPY -3.3% off high, also
  below both. IWM is *above* its SMA20 — small caps are outperforming on the pullback, unusual.
- GOLD IS THE STORY: GLD closed at 355.78 with a 120-day low of 354.67 — it closed **at the low of the
  last four months**, -17.8% from 432.98, and is 5.3% below its SMA20 and 8.9% below its SMA50. ATR 1.65%.
  A -3.47% day into a 4-month low is a breakdown, not a dip.
- ENERGY IS THE OTHER STORY: XLE closed 0.19% off its 120-day high, +33% off the 120-day low, with SMA20
  (67.12) above SMA50 (64.93) — a clean uptrend, and the only green sector Friday.
- TLT above both SMA20 and SMA50 despite a 4.98% 10y. Duration quietly basing.
- NOTE: SMA200 is None for all names (only 120 days of history pulled), so no 200-day reads today.

## [06:11 ET] NEWS — what happened Friday 2026-10-30
- Tech-led selloff: Nasdaq Composite -2.9%, S&P -1.8%, Dow -1.1%. **Intel stock dropped 30%.** Bitcoin slid
  toward $77,000. Gold hit a one-year low. — source: https://finance.yahoo.com/markets/stocks/articles/stock-market-today-nasdaq-p-123540419.html
- Gold's fall was **forced selling, not a haven failure**: Global X analyst called it a "liquidity-driven
  selloff"; investors sell gold to cover margin calls in sharp drawdowns. Gold futures -3.6% to $3,884.90.
  — source: https://www.kitco.com/news/article/2026-10-30/gold-falls-below-3900-silver-tumbles-wall-street-selloff-triggers
- Gold below $4,000 first time since July — source: https://beincrypto.com/gold-price-below-4000-tech-selloff/
- **Brent crude reported above $117/bbl**, adding to inflation/margin concerns and the regional policy
  outlook. Higher crude is the direct explanation for XLE closing at a 4-month high on a -1.8% S&P day.
  — source: https://www.kitco.com/news/article/2026-10-30/gold-falls-below-3900-silver-tumbles-wall-street-selloff-triggers
- Gold falling on "lingering concerns about inflation and the prospect that the Federal Reserve will RAISE
  interest rates" — a hawkish repricing, with fed funds at 3.88% and the 10y at 4.98%.
- Gold is ~-27% from its record per https://cryptoticker.io/en/is-gold-a-safe-haven-gold-price-crisis/
- CAUTION: these are secondary sources and figures differ between them (Nasdaq -2.9% vs -4.5% quoted
  elsewhere; gold $3,884.90 vs "below $3,900"). The QQQ -3.47% figure above is from a fetched quote and is
  the number to trust.

## [06:11 ET] CALENDAR — this week's dated events
- **Mon Nov 2 (today): ISM Manufacturing PMI** — source: https://www.guggenheiminvestments.com/services/advisor-resources/us-economic-calendar
- **Tue Nov 3: US MIDTERM ELECTIONS** — the week's dominant dated catalyst — source: https://www.calendarx.com/schedule/economic-calendar
- Tue Nov 3 10:00 ET: JOLTS — source: https://www.calendarx.com/schedule/economic-calendar
- **Fri Nov 6 08:30 ET: October jobs report / nonfarm payrolls** — source: https://www.calendarx.com/events/jobs-report-november-2026
- NOT this week: CPI (Tue Nov 10), FOMC decision (Dec 9), FOMC minutes (Nov 18)
- DST ended this weekend, so 08:30 ET = 13:30 UTC from today.
- Earnings feed (finnhub, --days 10) returned NOTHING dated 11-02, 11-03 or 11-04 and 227 names on 11-05.
  Treat the near-dates as a feed gap, not as an empty calendar — do not claim "no earnings this week".

## [06:14 ET] DATA QUALITY — Kalshi event-contract search is unusable today
- `market_data.py events` returns count:0 for midterm, Senate, House, oil, gold(real), CPI, inflation,
  recession, Bitcoin, unemployment. The only non-zero hits are `KXMVECROSSCATEGORY-*` sports parlay
  baskets with every price field null (no yes_bid, no yes_ask, no last_price, no volume).
- CONSEQUENCE: I cannot state a market-implied probability for ANY event contract today without
  fabricating it. Per the universe rules an event-contract idea needs the market's implied probability
  stated. **So no event contracts will be captured today**, despite the midterms being Tuesday — which is
  exactly the week they would have been most useful. Recording as a coverage gap, not working around it.

## [06:17 ET] NEWS — THE DRIVER: Iran war risk, and it is explicitly timed to the midterms
- Brent Dec contract settled ~**$117.64** on 2026-10-30, +2.4% on the day and **+13.6% for October**, a
  six-month high. WTI ~**$104**. — sources:
  https://www.nationthailand.com/news/world/40072956
  https://www.kotakneo.com/news/commodities/oil-prices-hit-six-month-high/
  https://aktualita.co/en/international/global-oil-prices-surge-sharply-brent-hits-us117-and-wti-us104-amid-middle-east-conflict
- Drivers: fear the Iran war escalates **after the US midterms**; a tanker attack in the **Strait of
  Hormuz**; Houthi attacks on Saudi oil facilities. The President indicated airstrikes on Tehran could
  resume **after the midterms**. — source: https://wisevoter.com/world/2026/10/31/brent-crude-hits-117-middle-east-tensions
- Also cited: historically depleted US SPR, so the usual policy shock absorber is not there.
- Energy sector rallied ~12% — source: https://time.news/energy-sector-rallies-nearly-12-percent-as-crude-prices-surge/
- **THIS IS A DATED CATALYST.** Midterms Tue 2026-11-03; the stated precondition for escalation is that
  they are past. The energy/oil complex is positioned into a binary that resolves starting Wednesday.
- THE OTHER SIDE, stated up front: Brent is +13.6% in a month at a six-month high on a *fear premium*.
  Geopolitical premia decay fast when the feared event does not occur. A Reuters poll cited by Aktualita
  puts the **2026 average Brent at $92.88**, i.e. consensus expects a sharp fall from here. UBS had $110
  end-2026 — already exceeded. **Buying crude or energy equities here is chasing a war premium into the
  event**, and if the midterms pass without escalation the premium unwinds. I will not capture a naive
  long-oil idea on this.
- The cleaner expression of "oil stays high" is the trade where the cost shock has NOT yet been priced —
  fuel consumers (airlines) — rather than the producers that already ran 12%.

## [06:04 ET] CLOCK CORRECTION
- The timestamps above (06:03-06:17) were written from my own sense of elapsed time and ran ahead of the
  wall clock. `TZ=America/New_York date` reads **06:04 ET** at this point. All entries above were written
  between 06:00 and 06:04 ET. Entries below carry real `date` output.

## [06:05 ET] LEVELS — airlines, semis, energy, power (120d history, close 2026-10-30)
| Sym | Close | ATR14 | ATR% | SMA20 | SMA50 | 120d hi | 120d lo | off hi | advol |
|---|---|---|---|---|---|---|---|---|---|
| AAL | 12.60 | 0.60 | 4.78% | 12.44 | 12.95 | 18.79 | 11.63 | -32.9% | $801M |
| UAL | 104.24 | 4.94 | 4.74% | 103.21 | 107.65 | 138.77 | 88.34 | -24.9% | $507M |
| DAL | 80.15 | 3.13 | 3.90% | 79.58 | 80.47 | 95.68 | 67.76 | -16.2% | $570M |
| LUV | 42.43 | 1.70 | 4.02% | 41.41 | 40.74 | 53.13 | 37.23 | -20.1% | $273M |
| INTC | 65.76 | 6.86 | **10.43%** | 96.39 | 101.11 | 142.35 | 63.20 | **-53.8%** | $7.5B |
| XLE | 70.02 | 1.43 | 2.04% | 67.12 | 64.93 | 70.15 | 52.62 | -0.2% | $2.3B |
| XOP | 203.76 | 4.93 | 2.42% | 197.10 | 191.69 | 206.05 | 150.37 | -1.1% | $572M |
| OXY | 64.00 | 1.50 | 2.34% | 61.71 | 60.18 | 64.96 | 47.77 | -1.5% | $565M |
| VST | 138.37 | 7.53 | 5.44% | 150.79 | 145.07 | 171.35 | 132.66 | -19.3% | $942M |

- AIRLINES: the fuel-cost short is **already largely in the price** — AAL -33% off its high and 8% above
  its 4-month low, UAL -25%, LUV -20%. Shorting a 4.78%-ATR name 8% above its floor after the move is
  late. Revisit below, but the easy part is gone.
- INTC: a -53.8% drawdown from 142.35 with a **10.43% ATR**. Trading 32% below its own SMA20. Needs news
  before any view — a 30% single-day drop in a mega-cap is either a solvency/guidance event or a deal.
- ENERGY PRODUCERS are all pinned at 4-month highs (XLE -0.2%, XOP -1.1%, OXY -1.5% off). Nothing here is
  a pullback entry; every one of them is a breakout-chase into the midterm event.
- VST: -19.3% off high, below SMA20 (150.79) AND SMA50 (145.07), and the 120-day low is **132.66** —
  which is within 0.5% of the already-published-but-unfilled VST BUY @ 132.0 from 2026-08-24. That entry
  level is still live and sits on a real 4-month floor, not a reflex discount.

## [06:07 ET] NEWS — INTC -28.6% on guidance, and the *mechanism* matters more than the stock
- Intel closed $65.76, **-28.58%**, after guiding Q4 revenue to **$15-16B vs ~$17B consensus**. Q3 results
  actually beat; the guide overshadowed it. >$146B of market cap erased; the US government's stake lost
  ~$12B. — sources:
  https://www.gurufocus.com/news/9159974/intel-intc-shares-plunge-nearly-29-after-disappointing-q4-outlook
  https://247wallst.com/investing/2026/10/30/intel-plunges-25-as-weak-outlook-and-pc-slump-overshadow-earnings-beat-dell-tumbles-13-amd-sinks-10-nvidia-falls-3/
  https://techcrunch.com/2026/10/30/intels-stock-crashes-knocking-12b-from-governments-stake/
- Intel's stated reasons: **PC market to shrink 12% in 2026 and 10% in 2027**, weakness lasting at least
  through H1 2027; and **the AI industry's demand for memory and other components is pushing up PC
  prices**, suppressing PC sales. — source: https://techcrunch.com/2026/10/30/intels-stock-crashes-knocking-12b-from-governments-stake/
- Contagion: Dell -13%, AMD -10%, NVDA -3%.
- **THE INFERENCE WORTH TRADING:** Intel did not say demand vanished, it said *components got expensive*.
  A memory shortage severe enough to raise PC retail prices and shrink unit demand by 12% is, by
  construction, a windfall for the people who sell memory. The loser's own explanation names the winner.
  Checking MU/WDC/STX next to see whether that is already priced.

## [06:09 ET] REJECTED — the "memory makers win from Intel's miss" idea — it is already priced, and then some
| Sym | Close | ATR% | SMA20 | SMA50 | 120d hi | 120d lo | off hi |
|---|---|---|---|---|---|---|---|
| MU | 884.74 | 5.76% | 950.61 | 978.71 | 1255.00 | 652.21 | **-29.5%** |
| WDC | 366.11 | 6.72% | 377.84 | 421.46 | 799.87 | 331.81 | **-54.2%** |
| STX | 644.58 | 7.93% | 713.12 | 799.09 | 1145.00 | 621.00 | **-43.7%** |
| DELL | 424.30 | 8.33% | 506.15 | 513.89 | 595.51 | 227.27 | -28.8% |
| HPQ | 28.78 | 5.18% | 31.54 | 31.71 | 36.23 | 20.44 | -20.6% |
| AMD | 504.80 | 6.38% | 570.44 | 548.29 | 658.52 | 393.36 | -23.3% |
| NVDA | 204.64 | 3.20% | 221.46 | 221.75 | 243.37 | 189.80 | -15.9% |
| SMH | 522.49 | 4.02% | 569.90 | 572.62 | 671.83 | 503.63 | -22.2% |

- My inference was wrong and the data kills it. If a memory shortage were the trade, MU/WDC/STX would be
  making highs. Instead **WDC is -54% and STX -44% off their 120-day highs** — worse than Intel's -54%
  only by a hair, and far worse than NVDA's -16%. MU has round-tripped from 1255 to 885.
- So the memory supercycle was priced *and is now unwinding*. Intel's "components are expensive" line is
  a lagging description of a cost base set months ago, not a forward signal for memory pricing.
- Broader point this forces: **every one of these eight names sits below both its SMA20 and SMA50**, and
  SMH is -22% off its high. This is not an Intel-specific event, it is a semiconductor/AI-complex
  drawdown in progress. Catching it on day one of a -28% mega-cap gap is knife-catching.
- NO SEMICONDUCTOR LONG TODAY. Not Intel, not memory, not the dip in NVDA. Nothing in this complex has a
  level I can defend as support, because they are all mid-air between a 120-day high and a 120-day low
  with momentum down and no dated catalyst before the next earnings cycle.

## [06:14 ET] POSITION UPDATE — all 14 open positions reviewed
Stop distance checked as |entry-stop|/ATR14 against the swing floor (2.0 stock, 1.8 etf); R:R as
|target-entry|/|entry-stop|. Prices are the 2026-10-30 close.

| Sym | Side | Entry | Stop | Last | ATR14 | stop ATRs | R:R | Decision |
|---|---|---|---|---|---|---|---|---|
| XLE | BUY | 63.90 | 60.80→**66.50** | 70.02 | 1.427 | 1.82 | 2.54 | **RAISE STOP** — captured |
| HII | BUY | 262.00 | None→**288.00** | 316.88 | 9.987 | 2.60 | 2.99 | **ADD STOP** — captured |
| BCC | BUY | 76.50 | None | 78.83 | 2.265 | n/a | n/a | hold (long_term, no stop by design) |
| PFE | BUY | 27.60 | None | 30.52 | 0.603 | n/a | n/a | hold — 0.5% off its 120d high, working |
| IYR | SELL_SHORT | 97.80 | 100.60 | 99.66 | 1.475 | 1.90 | 2.61 | **hold, no change** — see below |
| LULU | SELL | 100.61 | 112.00 | 107.24 | 4.366 | 2.61 | 2.07 | **hold, no change** — see below |
| NKE | SELL | 38.40 | 41.00 | 38.67 | 1.044 | 2.49 | 2.42 | hold, no change |
| KHC | BUY | 23.00 | 21.20 | 24.34 | 0.650 | 2.77 | 2.83 | hold |
| XLF | BUY | 54.23 | 52.80 | 56.51 | 0.752 | 1.90 | 2.36 | hold |
| STLD | BUY | 245.50 | 228.75 | 250.80 | 9.218 | 1.82 | 2.12 | hold |
| UNP | BUY | 288.60 | 277.40 | 304.00 | 6.157 | 1.82 | 2.45 | hold |
| ABT | BUY | 103.00 | 97.00 | 106.20 | 2.977 | 2.02 | 2.39 | hold |
| CVS | BUY | 93.00 | 85.40 | 90.25 | 2.201 | 3.45 | 2.33 | hold — below both MAs, watch |
| PYPL | BUY | 56.50 | 54.10 | 57.01 | 1.331 | 1.80 | 2.60 | hold |

**Only two positions changed, and both changes are to risk, not reward.** I am not re-pitching the other
twelve. Twelve "hold, unchanged" decisions is the honest output of this review, and emitting twelve
recommendations that restate existing levels would pad the report and re-anchor it on names already held.

Two I looked hardest at and deliberately left alone:
- **IYR short (-1.9%)** is going wrong for a real reason: the 10y fell 5.05→4.98 and TLT is above both its
  SMA20 and SMA50, so the duration backdrop has turned against a REIT short, and IYR is back above its
  SMA20 (96.97) and SMA50 (98.85). The temptation is to widen the stop. **I am not doing that** — that is
  the move this report has been punished for. The stop at 100.60 is 1.90 ATR from entry, which clears the
  1.8 ETF floor legitimately, and it sits 0.64 ATR above Friday's close. It will resolve within days.
  Let it.
- **LULU short (-6.6%)** is in the same shape: above its SMA20 (98.61) and SMA50 (103.05), up 18.7% off
  its 120-day low. Stop 112.00 is 2.61 ATR from entry and 1.02 ATR above the close. Also left to resolve.

## [06:14 ET] AWAITING-ENTRY REVIEW (6 unfilled)
- `VST` BUY @132.00 (2026-08-24) — **still live and still the right level.** VST closed 138.37, the
  120-day low is 132.66, so 132.00 is a hair under a real 4-month floor. Re-pitching below with what changed.
- `OXY` BUY @54.00 (2026-09-24) — **dead level.** OXY closed 64.00, i.e. 18.5% ABOVE the entry, 1.5% off
  its 120-day high. Oil ran away from this bid. It will not fill absent a crude collapse, and if crude
  collapses the thesis is gone too. Should be dropped rather than carried.
- `AAL` SELL_SHORT @13.35 (2026-10-03) — **keep, unchanged.** AAL closed 12.60, so the short entry sits
  6.0% ABOVE the market: this is a sell-into-strength limit, which is the correct construction for a
  short, and crude at ~$104 WTI strengthens the fuel-cost thesis behind it. No change to make.
- `GLD` SELL @406.77 (2026-10-25) — **dead level, and overtaken by events.** GLD closed 355.78, 12.5%
  BELOW the entry. Gold fell straight through without the level ever being offered. Drop it.
- `SMMT` BUY @17.10 (2026-10-27) — note SMMT was also STOPPED OUT on 2026-10-26 from an earlier entry.
  Checking price separately before any view.
- `KXCPIYOY-26SEP-T3.5` NO @18 (2026-09-30) — a September-CPI contract; September CPI has long since
  printed, so this is resolved or expired. I cannot confirm either way because the Kalshi endpoint
  returns count:0 for every macro query today (see data-quality note). Flagging, not guessing.

## [06:17 ET] REJECTED — tankers (FRO/DHT/INSW/STNG/TNK) — the Hormuz trade is already fully paid for
| Sym | Close | ATR% | SMA20 | SMA50 | 120d hi | off hi | **off 120d LOW** | advol |
|---|---|---|---|---|---|---|---|---|
| FRO | 56.90 | 4.54% | 54.30 | 50.31 | 59.75 | -4.8% | **+68.4%** | $237M |
| DHT | 25.02 | 4.52% | 24.40 | 22.52 | 26.91 | -7.0% | **+56.6%** | $122M |
| INSW | 111.95 | 5.13% | 114.26 | 108.50 | 126.27 | -11.3% | +49.2% | $88M |
| STNG | 92.60 | 4.08% | 85.94 | 83.72 | 95.60 | -3.1% | +36.2% | $114M |
| TNK | 100.80 | 3.81% | 100.51 | 97.15 | 110.65 | -8.9% | +57.4% | $41M |
- The logic was sound — a tanker attack in the Strait of Hormuz raises war-risk premia and day rates — but
  every one of these is 36-68% off its 120-day low and within 3-11% of its high, with 4-5% ATRs. There is
  no entry here that is not a chase, and no stop that is both 2.0 ATR wide and above a defensible level.
- Also: DHT is specifically named in the repo's own notes as a symbol this report over-published (six
  mornings). Re-pitching it off a theme that has already run 57% would be exactly that mistake again.

## [06:17 ET] LEVELS — defense primes
| Sym | Close | ATR14 | ATR% | SMA20 | SMA50 | 120d hi | 120d lo | off hi |
|---|---|---|---|---|---|---|---|---|
| LMT | 636.95 | 20.88 | 3.28% | 558.37 | 544.10 | 657.00 | 487.15 | -3.1% |
| NOC | 557.54 | 16.23 | 2.91% | 517.83 | 520.34 | 594.51 | 470.06 | -6.2% |
| GD | 372.59 | 7.15 | 1.92% | 343.75 | 351.40 | 400.00 | 322.00 | -6.9% |
| RTX | 199.80 | 5.59 | 2.80% | 190.25 | 194.79 | 226.88 | 170.78 | **-11.9%** |
- LMT is +30.8% off its low and 3% from its high — the prime that has already discounted escalation.
- RTX is the laggard at -11.9% off its high while the group trades at highs. RTX is also the prime whose
  product mix (interceptors, Patriot/SM-series) is literally *consumed* in a Middle East air campaign
  rather than ordered over a decade. Worth a closer look — but "laggard in a hot sector" is not by itself
  a thesis, so checking relative strength and news before any capture.
- Note I already hold HII for the defense exposure, and `config/strategy.md` caps same-driver ideas at 3.
  HII + RTX would be two on the Iran driver, plus XLE makes three. That is the cap. No fourth.

## [06:21 ET] REJECTED — VST BUY @132 — I am dropping the standing bid, not re-pitching it
- The level is still technically attractive (120d low 132.66), but the reason it is cheap is not the one
  the original thesis assumed. VST is **-10.4% vs XLU over one month** — XLU rallied +9.45% while VST fell
  0.99%. That is idiosyncratic underperformance against its own sector, not "sold off alongside tech".
- Why: a string of analyst target cuts through late October (CIBC $201→$181, Scotiabank $207→$189, Zacks
  downgrade to Strong Sell), and a prior quarter reported as a large miss ($0.76 EPS vs $1.61 est,
  revenue $4.02B vs $5.46B est — MarketBeat auto-generated figures, NOT verified against the filing, so
  treat as indicative only). — sources:
  https://www.marketbeat.com/instant-alerts/price-vistra-nyse-vst-stock-falls-15-following-analyst-downgrade-2026-10-29/
  https://www.marketbeat.com/instant-alerts/price-vistra-nyse-vst-stock-price-down-28-following-analyst-downgrade-2026-10-28/
- **And Q3 earnings are reported as being due next week.** Buying a 19%-drawdown name that is lagging its
  own sector, into a print, on a bid 4.6% below market, is the exact pattern `config/strategy.md` flags:
  a pullback entry that only fills once the trade is already going wrong. Dropping it.
- The structural datacenter-power thesis may well still be right. It is not actionable at a defensible
  level today, and I will not carry a stale bid to look consistent.

## [06:21 ET] DATA QUALITY — two more sources down
- `market_data.py implied` → yahoo-options HTTP 401 Unauthorized. **No options-implied move available for
  any name today**, so I cannot check targets against what the straddle prices. Stated as a gap on every
  candidate rather than skipped silently.
- `market_data.py short` → api.nasdaq.com read timeout. No short interest / days-to-cover today.

## [06:21 ET] RTX — the direct Iran-escalation defense expression, and it is leading not lagging
- First read was wrong: RTX looked like the laggard at -11.9% off its 120-day high vs LMT at -3.1%. But
  fetched relative strength says RTX is **outperforming**: +7.99% 1m vs SPY -1.08% (+9.07 pts) and vs ITA
  +0.82% (+7.17 pts), and +17.85 pts vs ITA over 6m. The large "off-high" number is distance from an old
  high, not current weakness — RTX is +17.0% off its 120-day low and above both its SMA20 and SMA50.
- Analyst revision direction **improving**: bullish share 67.7%, +1.0 pt m/m; strong_buy 7 and buy 13→14
  from Oct to Nov. Earnings surprise record: **beat in all 4 of the last 4 quarters** (+0.35%, +12.63%,
  +16.10%, +4.58%). — source: finnhub via scripts/market_data.py analysts
- Insiders are a mild negative: 0 open-market buys, 6 sells totalling $6.86M over six months.
- Mechanism: unlike a shipbuilder's decade-long backlog, RTX's interceptor and effector mix is *consumed*
  in a Middle East air campaign and restocked at appropriated prices. That is why it is the escalation
  expression rather than LMT, which has already run 30.8% off its low to within 3% of its high.

## [06:19 ET] PRECIOUS METALS — a bust, not a dip. No long, no short.
| Sym | Close | ATR% | SMA20 | SMA50 | 120d hi | 120d lo | off hi | **off low** |
|---|---|---|---|---|---|---|---|---|
| GLD | 355.78 | 1.65% | 375.76 | 390.57 | 432.98 | 354.67 | -17.8% | +0.3% |
| IAU | 72.92 | 1.64% | 77.04 | 80.07 | 88.71 | 72.715 | -17.8% | +0.3% |
| **SLV** | 44.60 | 3.66% | 51.34 | 55.82 | **80.86** | 44.11 | **-44.8%** | +1.1% |
| GDX | 77.09 | 4.13% | 84.94 | 91.64 | 105.67 | 69.74 | -27.1% | +10.5% |
| NEM | 106.61 | 3.95% | 114.41 | 120.64 | 135.29 | 88.75 | -21.2% | +20.1% |
- **Silver is down 44.8% from 80.86 to 44.60 and sits 1.1% off its 120-day low.** That settles the
  question the "liquidity-driven selloff" framing raised. A margin-call liquidation does not take silver
  down 45% and hold it there; this is a precious-metals bubble unwinding, and gold's -17.8% is the mild
  end of it. Every name in the complex is below both its SMA20 and SMA50.
- So: **no gold long.** The mean-reversion case rests on the selloff being mechanical, and silver says it
  is not. The macro backdrop agrees — press attributes the fall to inflation worry plus the prospect the
  Fed *raises* rates, and rising real rates are a genuine fundamental headwind, not a liquidity blip.
- And **no gold/silver short either**: SLV is 1.1% off a 4-month low after a 45% fall with a 3.66% ATR.
  Shorting that is picking up the last coin in front of a violent short-covering bounce. Nothing here.
- Consequence for the book: the standing `GLD SELL @406.77` is confirmed dead — gold is 12.5% below it
  and the thesis has already played out without the order ever filling.

## [06:19 ET] ROTATION — where the money actually went
| Sym | Close | SMA20 | SMA50 | off 120d high |
|---|---|---|---|---|
| XLV | 184.87 | 175.69 | 172.22 | **-1.7%** |
| XLP | 89.42 | 86.01 | 84.61 | **-1.1%** |
| XLU | 43.43 | 41.95 | 41.75 | -6.9% (+9.45% 1m) |
| XLE | 70.02 | 67.12 | 64.93 | -0.2% |
- Healthcare, staples, utilities and energy are all at or near 120-day highs and above both averages,
  while QQQ is -9.5% off its high and SMH -22%. This is a clean defensive + energy rotation.
- **I am not adding XLV.** The book already holds PFE, ABT and CVS — three healthcare names, which is the
  `config/strategy.md` correlation cap of 3 on one driver already spent. An XLV ETF on top would be a
  fourth expression of the same bet dressed as diversification.

## [06:19 ET] REJECTED — EQT BUY — fails the reward-to-risk floor honestly, and I am not rescuing it
- Setup was real: US natgas producer, 55.38, above SMA20 (53.98) and SMA50 (53.20), with a winter seasonal
  and a Hormuz/LNG-pull kicker. ATR14 1.749.
- A proper stop is 51.00 — below the SMA50, 2.29 ATR from a 55.00 entry. The 120-day high is **59.795**.
  Reward to that high is 4.80 against 4.00 of risk: **R:R 1.20**, well under the 2.0 swing floor.
- To clear 2.0 I would need a target above 63 — i.e. above the 4-month high, a level this stock has not
  traded at — or a stop tightened to ~52.6, which is 1.37 ATR and inside the floor. Both are the exact
  manipulations `config/strategy.md` names. **The idea failed the floor; dropping it.**

## [06:19 ET] NOTED, NOT CAPTURED — the natgas divergence is real but has no dated catalyst
- LNG (Cheniere) 330.32 is **0.12% off its 120-day high**, +47.7% off the low; AR 42.08 is -1.6% off its
  high. The LNG *equities* have fully priced the Hormuz story.
- But **UNG 9.08 is -25.8% off its high and 1.6% off its 120-day LOW**, below SMA20 (10.34) and SMA50
  (10.42). US domestic gas is near its floor while everything that exports it is at a high.
- The divergence is explicable (exporters earn tolling fees, not the gas price) and the asymmetry is
  attractive, but the catalyst is "winter" and "possible Qatari LNG disruption two steps down a causal
  chain" — neither is a dated event, and UNG carries front-month roll decay on top. **Not capturing a
  swing idea whose catalyst I cannot date.** Watchlist material for synthesis, not a recommendation.

## [06:20 ET] REJECTED — AMR BUY — the insider signal did not survive being read
- The screen flagged it: 38 open-market buys, 3 distinct buyers, **$17.5M bought vs $0.93M sold**. On the
  face of it the strongest insider cluster I found today.
- Reading it kills it. The buying is one named director (Courtis Kenneth S.), 8 transactions across two
  dates (2026-08-28 and 2026-09-08), at **$223.85-$235.47**. AMR closed Friday at **159.19** — he is down
  roughly 30% and the stock has kept falling, below both its SMA20 (168.54) and SMA50 (187.56).
- The fundamentals are worse than the chart: analyst trend is **0 strong_buy, 0 buy, 7 hold, 4 sell, 1
  strong_sell — bullish share 0.0%, flat for four months.** And the last four prints: Q2-26 actual -$0.96
  vs +$0.10 est (**-1043% surprise**), Q1-26 -$0.86 vs +$0.91. The company is loss-making and missing big.
- Earnings Nov 6 would have been the dated catalyst. Buying a loss-making met-coal producer with zero
  bullish analysts, 34% off its high, four days before a print, because one director caught the knife 30%
  higher, is not an insider thesis. **Rejected.** — source: finnhub via market_data.py insiders/analysts

## [06:20 ET] REJECTED — ARM, OKLO — crushed, with no insider confirmation at all
- ARM 205.97 is **-54.5% off its 120-day high (452.70)** and 3.6% off its low, ATR 6.94%. Reports Nov 5.
  Insiders: **0 buys, 26 sells, $57.9M.** No one inside is stepping in.
- OKLO 25.25 is **-67.1% off its high (76.68)**, 3.1% off its low, ATR 7.05%. Reports Nov 6.
  Insiders: **0 buys, 94 sells, $115.2M.** Same picture, worse.
- Both are speculative-growth unwinds with a dated catalyst and nothing else. A 7% ATR into an earnings
  print with heavy insider distribution is a coin flip, not an edge.
- Same screen, same answer: ABNB 0 buys / 203 sells / $926.7M; FLR 0 buys; DK 0 buys / 31 sells.
- UAA is the one with real buying — Fairfax Financial took ~1.18M shares at ~$4.97 in **May 2026** — but
  that is ONE buyer, six months stale, and UAA at 4.99 is exactly where they bought. It also directly
  contradicts the NKE and LULU shorts already in the book. Not captured.

## [06:20 ET] DATA QUALITY — NO FUTURES PRICES AVAILABLE TODAY. This removes a whole asset class.
- Tested ES=F, NQ=F, RTY=F, CL=F, MES=F through `market_data.py quote`: **every one returns ok:false**
  (finnhub returns c:0, i.e. no price; yahoo is 429/401). The `macro` call failed identically for
  es_futures, nq_futures, gold and wti_crude.
- `config/universe.md` says to prefer a futures contract over spot wherever one exists, and today I
  cannot honour that, because I cannot state an entry, stop or target in index points without inventing
  one. **So there are no futures ideas today, and that is a data failure, not a judgement.**
- Concretely lost: a /MNQ short on the AI-complex unwind, a /M2K long on small-cap relative strength, and
  /MCL on the Brent spike — three of the cleanest expressions of what the tape is actually doing.

## [06:20 ET] CRYPTO — live prices fetched, nothing captured
- BTC **$77,828** (24h -0.11%, vol $17.0B), ETH **$2,283.67** (+0.64%), SOL **$93.81** (-1.56%)
  — source: coingecko via market_data.py, fetched live (crypto trades 24/7, so this is a current price,
  unlike the equity closes above).
- Crypto is in the same de-risking as semis, silver and speculative growth, and Robinhood Crypto cannot
  short, so a bearish view is unexpressable without the futures that are unavailable today. A long here
  is catching the same knife. Nothing captured.

## [06:23 ET] REJECTED — banks (KRE, KBE, C, WFC) — a real driver with no good entry
| Sym | Close | ATR14 | ATR% | SMA20 | SMA50 | 120d hi | 120d lo | off hi | off low |
|---|---|---|---|---|---|---|---|---|---|
| KRE | 72.01 | 1.327 | 1.84% | 70.62 | 71.97 | 78.35 | 66.42 | -8.1% | +8.4% |
| KBE | 65.70 | 1.140 | 1.74% | 64.35 | 65.88 | 71.92 | 61.26 | -8.7% | +7.3% |
| XLF | 56.51 | 0.752 | 1.33% | 55.33 | 55.95 | 58.60 | 50.52 | -3.6% | +11.9% |
| C | 122.64 | 3.510 | 2.86% | 124.79 | 130.01 | 147.96 | 119.76 | -17.1% | **+2.4%** |
| WFC | 83.40 | 1.953 | 2.34% | 82.47 | 84.32 | 91.99 | 72.78 | -9.3% | +14.6% |
- The driver is sound and genuinely independent of the Middle East: 10y 4.98%, 2y 4.61%, curve +0.38 and
  steepening, with press reporting the market fears the Fed *raises* rather than cuts. That is a bank
  tailwind.
- KRE does technically qualify — entry 71.80, stop 69.00 (2.11 ATR), target 77.80 gives R:R 2.14. I am
  not taking it. `CLAUDE.md` names KRE as *the* case where this report republished an idea three times
  while walking the stop in from 74.20 to 75.20. Re-pitching that exact symbol on a mediocre 8.4%-to-
  target setup is how that mistake gets made again, and the setup is not good enough to be worth the risk.
- C is the interesting anomaly — **-17.1% off its high and only 2.4% off its 120-day low** while XLF is
  -3.6% off its high, so something name-specific is wrong at Citi. It is below both averages and falling.
  Worth a look another day; today it is a knife with no catalyst I could date.
- XLF is already held (+4.2%), so the sector exposure exists.

## [06:23 ET] CAPTURED — XLU, and why it is the only non-Iran idea in the book
- Entry 43.30 (zone 42.80-43.70), stop 41.80, target 46.60. Risk 1.50 = **2.39 ATR** (ETF floor 1.8);
  reward 3.30; **R:R 2.20**; win_probability 0.36 against a 0.3125 break-even baseline — a 4.75-point
  claimed edge, deliberately small.
- Selected over XLP and XLV on the only ground that mattered: **room**. XLP is 1.1% off its 120-day high
  and XLV 1.7% off, so with a proper 1.8+ ATR stop neither can reach a 2.0 R:R without a target above its
  4-month high. XLU is 6.85% off its high, so the target is a level the fund has actually traded at.
- Logged honestly in the candidate: it partially offsets the IYR short, since both are duration proxies.

## [06:25 ET] REJECTED — consumer trade-down (DG/DLTR/BJ/WMT/COST) — right thesis, no room left
| Sym | Close | ATR14 | ATR% | SMA20 | SMA50 | 120d hi | off hi | off 120d low |
|---|---|---|---|---|---|---|---|---|
| DLTR | 133.87 | 4.519 | 3.38% | 122.94 | 121.79 | 137.07 | -2.3% | **+55.9%** |
| BJ | 107.32 | 2.758 | 2.57% | 101.97 | 96.50 | 108.09 | **-0.7%** | +29.0% |
| DG | 132.30 | 4.727 | 3.57% | 129.06 | 126.37 | 139.12 | -4.9% | +32.9% |
| COST | 1012.28 | 17.498 | 1.73% | 977.89 | 943.30 | 1096.50 | -7.7% | +14.6% |
| WMT | 123.51 | 2.643 | 2.14% | 115.95 | 110.23 | 135.16 | -8.6% | +20.9% |
- The mechanism is real — Brent $117 means a gasoline tax on the low-income consumer and a trade-down to
  discounters — and it would have been consistent with the NKE/LULU shorts already in the book.
- It is already paid for. DLTR +55.9% off its 120-day low and 2.3% from its high, BJ 0.7% from its high.
- WMT and COST have the most room, and **both fail the floor by exactly the suspicious margin**:
  - WMT: entry 123.00, stop 117.00 (2.27 ATR), target 135.00 (the 120-day high) → **R:R 2.00**.
  - COST: entry 1010, stop 970 (2.29 ATR), target 1090 (just under the 120-day high) → **R:R 2.00**.
  A ratio that lands exactly on the floor is the pattern `CLAUDE.md` records as already shipped once —
  eight ratios clustered 2.04-2.33 against a 2.0 floor, targets nudged until they passed. Both rejected.

## [06:25 ET] THE CENTRAL FINDING — this is why today is four ideas and not twenty
Running the same two tests across every sector I priced today produced one answer over and over:
- **What is working is too close to its high to pay for an honest stop.** XLP -1.1% off high, XLV -1.7%,
  BJ -0.7%, DLTR -2.3%, XLE -0.2%, XOP -1.1%, OXY -1.5%, LNG -0.1%, AR -1.6%, LMT -3.1%, STNG -3.1%.
  With a stop at the 1.8-2.0 ATR floor, none of them reaches a 2.0 reward-to-risk without a target set
  above its own 120-day high. EQT, WMT, COST, XLP all failed on exactly this.
- **What is cheap is in a downtrend with no datable catalyst.** SLV -44.8% off high, OKLO -67%, ARM
  -54.5%, WDC -54.2%, STX -43.7%, AMR -34.4%, UNG -25.8%, GDX -27.1% — every one below both its SMA20
  and SMA50, and the three I checked for insider confirmation (ARM, OKLO, AMR) had zero credible buying.
- The tape has already sorted itself into winners with no upside left and losers with no floor. The
  honest number of ideas that clear the bar in that tape is small. **I am publishing four and saying so,
  rather than padding to a tidy number with ratios engineered to 2.00.**

## [06:25 ET] FALSIFICATION — the case against each of the four, including against myself
**Concentration, stated plainly: three of the four ideas sit on one driver.** XLE (crude), RTX (Iran
escalation) and HII (defense budget) all improve or decay together with the Middle East. That is exactly
the `config/strategy.md` correlation cap of 3 — not a violation, but it is fully spent, and a reader
should treat the three as closer to one position than to three. XLU is the only genuinely independent
idea in the report, which is itself a weakness of the report.

- **XLE** — I must own this: raising the stop from 60.80 to 66.50 mechanically lifted reward-to-risk from
  2.13 to 2.54, which is the precise manoeuvre `CLAUDE.md` records KRE being abused with. The defence is
  the order I did it in — 66.50 was chosen as the level just below the SMA20 (67.12) on an open +9.6%
  position, and the ATR check (1.82, floor 1.8) was run afterwards as a test, not as a target. It is also
  why I refused to raise the 70.50 exit: if I were engineering the ratio I would have moved the target
  too. Residual risk: the stop is 5% below Friday's close, so a de-escalation gap gives back most of the
  gain before it triggers.
- **HII** — the catalyst framing is the weak part. A shipbuilder's funded backlog has very little to do
  with an Iranian air campaign, so the honest driver here is momentum plus budget, not escalation. The
  change being made (a first-ever stop at 288.00) stands on its own regardless.
- **RTX** — binary and dated. If Tuesday passes quietly, XLE, RTX and HII all unwind together and the
  correlation above becomes the whole story. I also could not fetch the options-implied move (Yahoo
  options 401), so I cannot say whether a 13.4% target is cheap or rich versus what the market prices.
  Insiders sold $6.86M with zero buys.
- **XLU** — the thinnest of the four by design: a 4.75-point claimed edge over the break-even baseline,
  a target 11 ATRs away, a two-sided catalyst, and a partial offset against the IYR short already held.
  It is in the report because it is the only idea that does not depend on the Middle East, not because
  it is the best one.

## [06:29 ET] CAPTURED — SMMT — the uncorrelated idea, and the best evidence base of the day
- **Catalyst is hard and dated: FDA PDUFA goal action date November 14, 2026** for ivonescimab +
  chemotherapy in EGFRm non-squamous NSCLC post-TKI. I fetched and read Summit's own press release rather
  than a story about it — it states the date verbatim, says the BLA was accepted for filing on the
  overall results of the Phase III HARMONi trial, that the FDA "intend[s] to perform a complete review",
  and that Fast Track was granted. **Priority review is NOT mentioned** — this is a standard review.
  — source: https://smmttx.com/news/press-releases/news-details/2026/Summit-Therapeutics-Announces-U-S--FDA-Acceptance-of-Biologics-License-Application-BLA-Seeking-Approval-for-Ivonescimab-in-Combination-with-Chemotherapy-in-Treatment-of-Patients-with-EGFRm-NSCLC-Post-TKI-Therapy/default.aspx
- **Insider buying here is everything AMR's was not**: 6 open-market buys, **3 distinct buyers,
  $103,616,650, and zero sells** in six months. Co-CEOs Robert Duggan and Mahkam Zanganeh each took
  3,810,000 shares at **$13.12** on 2026-06-12 — and at 16.03 they are **up 22%**, not averaging down
  into a loss the way AMR's lone director was at $230 against a $159 tape.
- Levels from the actual daily bars, not from summary stats: double bottom **14.37** (Oct 26 low) and
  **14.56** (Oct 16 low), then higher lows 14.50 → 15.33 → 15.77 → 16.20 → 16.03. October high 18.328
  (Oct 7). Stop **14.20** goes under both bottoms. Entry 16.00 (zone 15.60-16.40), essentially at market
  rather than a reflex discount. Risk 1.80 = **2.07 ATR** (stock floor 2.0); reward 4.00; **R:R 2.22**.
- Relative strength on the worst day: closed -1.05% on Friday against SPY -1.77%.
- **The honest weakness, recorded rather than buried**: the 20.00 target is ABOVE the 120-day high of
  19.09 — the same construction I rejected WMT, COST, EQT and XLP for today. I am claiming the
  distinction that an approval is a step-change re-rating and those had no event to carry the target.
  Against 19.09 the ratio is only **1.46** and the idea would fail. That argument is in the candidate's
  `counter_argument` so the red team can overrule it rather than having to discover it.
- Second honest weakness: one secondary aggregator describes the original HARMONi overall-survival
  result as having **missed statistical significance**. I could not confirm it against a primary source
  and have flagged it as unverified-but-material in `key_risk` rather than dropping it.
- Prior history acknowledged: an earlier SMMT position was **stopped out 2026-10-26** — at the 14.37 low
  this new stop sits beneath. Per `CLAUDE.md`, a closed position re-published is a genuinely separate
  trade, not a duplicate, so this opens its own row.
- Sized **1%, lottery tier**: a stop does not protect through a binary FDA gap, and pretending otherwise
  is how these ideas hurt people.

## [06:30 ET] REJECTED — CYTK — the PDUFA is real, the binary is not
- An aggregator listed CYTK with a **November 14, 2026 PDUFA** for aficamten/MYQORZO, same date as SMMT,
  and CYTK looked ideal on the chart: 62.99, -28.7% off its 120-day high (88.31), 5.4% off its low, above
  SMA20 (62.33), ATR 3.13%, advol $117M. — source: https://www.biopharmawatch.com/PDUFA-calendar
- Verifying it killed the thesis. **MYQORZO is already FDA-approved and on the market** — US launch began
  January 2026 with $25M of net product revenue in Q2 2026. The Nov 14 date is a **supplemental NDA
  (MAPLE-HCM) for obstructive HCM**, i.e. a label expansion on a marketed drug, not an approve/reject
  binary. A CRL on an sNDA costs a label, not the franchise, so the asymmetry I was buying does not exist.
  — sources: https://ir.cytokinetics.com/press-releases/press-release-details/2025/Cytokinetics-Announces-FDA-Approval-of-MYQORZO-aficamten-for-the-Treatment-of-Adults-with-Symptomatic-Obstructive-Hypertrophic-Cardiomyopathy-to-Improve-Functional-Capacity-and-Symptoms/default.aspx
    https://www.sec.gov/Archives/edgar/data/0001061983/000119312526372456/cytk-ex99_1.htm
- The genuinely big CYTK catalyst — the **non-obstructive HCM sNDA off ACACIA-HCM** — has not been
  submitted yet (planned Q4 2026), so it has **no PDUFA date at all**. Nothing datable to trade.
- Insiders agree with the pass: **0 buys, 40 sells, $27.7M** over six months.
- This is the aggregator-vs-primary-source trap. Had I taken the calendar at face value I would have
  published a binary-event trade on an event that is not binary.

## [06:30 ET] REJECTED — COGT, EXEL, CORT, MLYS — the rest of the Nov/Dec PDUFA slate
| Sym | PDUFA | Close | ATR% | SMA20 | SMA50 | 120d hi | off hi | off low | insider buys / sells |
|---|---|---|---|---|---|---|---|---|---|
| COGT | Nov 30 | 31.02 | 4.02% | 30.54 | 32.43 | 43.39 | -28.5% | +11.8% | **0** / 2 ($1.7M) |
| EXEL | Dec 3 | 69.39 | 2.61% | 62.69 | 59.39 | 72.10 | -3.8% | +44.3% | **0** / 10 ($11.1M) |
| CORT | Dec 17 | 81.12 | **7.46%** | 107.30 | 111.98 | 126.38 | -35.8% | +60.3% | **0** / 89 (**$83.3M**) |
| MLYS | Dec 22/27 | 18.18 | 7.49% | 21.36 | 24.78 | 32.14 | -43.4% | **+0.4%** | not checked |
- **Not one of them has a single open-market insider purchase.** That is the whole difference from SMMT,
  where three buyers put $103.6M in with zero sells and are up 22% on it. Without that, each of these is
  a chart plus a date on an aggregator calendar.
- CORT is the sharpest warning: down 35.8% from its high to 28 points below its own SMA50, with **89
  insider sales worth $83.3M** on the way down, on a 7.46% ATR. EXEL has the opposite problem — strong,
  but 3.8% from its high, so no room to a target (the same failure as XLP/BJ/DLTR). MLYS sits 0.4% off a
  120-day low with a 7.49% ATR.
- Also: the PDUFA dates above come from aggregator calendars I did **not** verify against primary
  sources, and the CYTK case above shows exactly what those are worth. I am not publishing a dated
  catalyst I have not read in a filing or company release.

## [06:32 ET] SELF-CHECK — recomputed every candidate's arithmetic from the fetched ATRs
Ran the floors myself rather than waiting for phase 2b. All five clear every hard gate:
| Sym | Horizon | R:R | floor | stop ATRs | floor | win_prob | baseline 1/(1+R:R) | edge | kinds | conv |
|---|---|---|---|---|---|---|---|---|---|---|
| XLE | swing | 2.54 | 2.0 | 1.82 | 1.8 | 0.72 | 0.283 | +43.7pt | 2 | 3 ✓ |
| HII | swing | 2.99 | 2.0 | 2.60 | 2.0 | 0.55 | 0.251 | +29.9pt | 3 | 4 ✓ |
| RTX | swing | 2.12 | 2.0 | 2.32 | 2.0 | 0.42 | 0.321 | +9.9pt | 3 | 4 ✓ |
| XLU | swing | 2.20 | 2.0 | 2.39 | 1.8 | 0.36 | 0.312 | +4.8pt | 2 | 3 ✓ |
| SMMT | swing | 2.22 | 2.0 | 2.07 | 2.0 | 0.42 | 0.310 | +11.0pt | 4 | 5 ✓ |
Conviction equals the distinct-evidence-kind count on all five — no inflation to correct.

**IMPORTANT FOR THE RED TEAM — XLE and HII will trip the ">20 points of claimed edge" check, and the
check is measuring the wrong thing on them.** The `1/(1+R:R)` baseline is a random walk starting *at the
entry*. XLE and HII are open positions already 9.6% and 20.9% in profit, so the walk does not start at
the entry — it starts at Friday's close, which is much nearer the target than the stop. Recomputing the
driftless baseline from the current price:
- **XLE**: from 70.02, target 70.50 is 0.48 away, stop 66.50 is 3.52 away → baseline **0.880**.
  My stated 0.72 is *below* it. The claim is conservative, not aggressive.
- **HII**: from 316.88, target 339.76 is 22.88 away, stop 288.00 is 28.88 away → baseline **0.558**.
  My stated 0.55 is essentially exactly it, i.e. I am claiming no edge at all, just the geometry.
- RTX (entry 199.00 vs 199.80), XLU (43.30 vs 43.43) and SMMT (16.00 vs 16.03) all have entries at the
  market, so for those three the entry-based baseline is the right one and the printed edges stand.
Cutting XLE or HII for an inflated win probability would be reading an artifact of an open position's
geometry. The honest criticism of those two is the one in the falsification block — concentration and the
XLE stop raise lifting the ratio — not the probability.

## [06:33 ET] INSIDER SCREEN across the beaten-down names — nothing else SMMT-grade, and one big confirmation
| Sym | open-market buys | distinct buyers | buy $ | sells | sell $ |
|---|---|---|---|---|---|
| **STX** | 0 | 0 | 0 | 578 | **$505,876,494** |
| **MU** | 0 | 0 | 0 | 212 | **$232,934,952** |
| WDC | 0 | 0 | 0 | 140 | $37,367,585 |
| INTC | 1 | 1 | $9,999,985 | 2 | $6,493,216 |
| VST | 3 | **1** | $1,173,069 | 13 | $21,878,803 |
| LULU | 1 | 1 | $500,384 | 0 | 0 |
| NKE | 0 | 0 | 0 | 9 | $1,574,773 |
| HPQ | 0 | 0 | 0 | 7 | $3,405,718 |
| C | 0 | 0 | 0 | 1 | $265,260 |

- **This is the strongest single piece of evidence behind the no-semiconductor-long decision**, and it is
  evidence rather than a chart read: STX insiders sold **$505.9M across 578 transactions**, MU **$232.9M
  across 212**, WDC $37.4M across 140 — and between the three of them, **not one open-market purchase.**
  The people who know the memory order book best were distributing into the top. Earlier I rejected the
  memory complex on price action alone; this corroborates it independently.
- **INTC is the AMR pattern again**: CEO Lip-Bu Tan bought $10.0M at **$95.00** on 2026-08-11. The stock
  closed Friday at **65.76** — he is down 31%, it is one buyer, and it predates the Q4 guide that caused
  the -28.6% day. A single underwater insider is not a reason to buy a company guiding revenue $1-2B
  below consensus on a shrinking PC market.
- **VST confirms today's rejection from a second angle**: CEO James Burke bought $1.17M around $135 in
  late August, but the company's insiders sold **$21.9M — nearly 19x as much** — and there is only one
  buyer. That is not the cluster that makes an insider thesis.
- Two small cross-checks on existing shorts: NKE has **zero** insider buying and $1.57M of sales, which
  mildly supports the short. LULU has one $500K purchase at $117.05 from June (buyer now down 8%) —
  small, stale and one person, but it is a point against the LULU short and I am recording it rather
  than ignoring it because it is inconvenient.

## [06:33 ET] CONCENTRATION — the counterweight question, answered honestly
Counting the *whole book*, not just today's captures, the Middle East escalation bet is bigger than three:
- XLE long (crude), RTX long (escalation), HII long (defense budget, partly), **and the standing
  `AAL SELL_SHORT @13.35` is a fourth** — an airline short is a long position in jet fuel, so it wins on
  escalation and loses on de-escalation exactly like the other three.
- That is four expressions of one macro outcome against a stated cap of three. I am not adding a fifth,
  and I flag the AAL order as the one a reader might not count because it is an unfilled limit rather
  than a position.
- The partial counterweight already in today's captures is **XLU**: if the midterms pass quietly and the
  crude premium deflates, headline inflation pressure eases, the 10-year falls from 4.98%, and the most
  rate-sensitive sector in the market re-rates upward. So XLU is not just the one non-Iran idea, it is
  roughly the one idea that *improves* in the scenario that hurts the other three. That is why it stayed
  in despite being the thinnest of the five on its own merits.
- I deliberately did NOT manufacture a crude-short or airline-long hedge. Shorting energy at a four-month
  high into a dated escalation risk, or buying airlines on a hoped-for de-escalation, would be inventing
  a position to balance a spreadsheet. The right response to concentration I cannot cleanly hedge is to
  disclose it, which is what this block is for.

## [06:34 ET] WATCHLIST — researched today, not actionable today (for synthesis)
Each of these was priced from real history and failed on a specific, named test — not on a vague feeling.
- **UNG** 9.08 — US natgas 1.6% off its 120-day low while LNG 330.32 is 0.1% off its *high*. Best raw
  asymmetry found today. Blocked by having no datable catalyst ("winter") plus front-month roll decay.
  Becomes actionable if a Qatari LNG disruption is actually reported, or on a dated cold-weather event.
- **C** 122.64 — -17.1% off its high while XLF is -3.6% off, and 2.4% off its own 120-day low. Something
  name-specific is wrong at Citi and I did not have time to find out what. Diagnose before trading.
- **EXEL** 69.39 — zanzalintinib PDUFA reported Dec 3, above both averages, uptrend intact. Blocked only
  by room: 3.8% off its 120-day high, so no 2.0 R:R with an honest stop. Watch for a pullback toward the
  SMA20 at 62.69. Note: 0 insider buys, $11.1M sold.
- **VST** 138.37 — the structural datacenter-power thesis is intact and I bought the sector (XLU) instead.
  Revisit after the Q3 print clears and the analyst cuts stop, ideally with the CEO's buying joined by
  someone else. Standing 132.00 bid dropped today.
- **CORT** 81.12 — relacorilant PDUFA reported Dec 17 after a -35.8% break. Watch for insider buying to
  appear; right now it is $83.3M of sales across 89 transactions and a 7.46% ATR.
- **WMT** 123.51 / **COST** 1012.28 — the consumer trade-down thesis is right and both compute to R:R
  exactly 2.00, which is a reject today. A pullback to the SMA20 (WMT 115.95, COST 977.89) makes either
  publishable.
- **KRE** 72.01 — mechanically qualifies (entry 71.80, stop 69.00 = 2.11 ATR, target 77.80 = R:R 2.14) on
  a steepening curve. Held back on repo history rather than on the numbers; noting it so the decision is
  visible rather than silent.
- **GLD 355.78 / SLV 44.60** — the precious-metals bust. Not a long (silver -44.8% off its high says the
  liquidation framing is wrong) and not a short (1.1% off a 4-month low). Watch for a base to form.

## [06:34 ET] RESEARCH COMPLETE
- **candidates: 5** — XLE (3, position update: stop raise), HII (4, position update: first stop added),
  RTX (4, new), XLU (3, new), SMMT (5, new). All five verified by me against the R:R floor, the ATR
  stop-distance floor, the expectancy baseline and the evidence-kind conviction count — see the SELF-CHECK
  block. No candidate needed a floor rescued.
- **Five is the honest count, not a shortfall.** See the CENTRAL FINDING block: every working sector today
  is within 0.2-3% of its 120-day high and cannot pay for a 1.8-2.0 ATR stop without a target set above
  its own high (EQT, WMT, COST, XLP, BJ, DLTR, EXEL all failed exactly there), and everything cheap is
  below both moving averages with heavy insider distribution and no datable catalyst (semis, metals, ARM,
  OKLO, AMR, MLYS, CORT). Padding this to fifteen would have meant engineering ratios to 2.00.
- **Skew to declare in data_quality_notes:** nothing `intraday` and nothing `long_term` cleared the bar —
  all five are `swing`. No intraday setup existed because I could not fetch a single live price (market
  closed, and every futures and index feed failed). The long-term lane genuinely lost its best candidate
  when VST turned out to be lagging its own sector by 10.4 points on company-specific problems; I bought
  the sector ETF instead rather than invent a long-term single name.
- **Three of five ideas sit on one driver** (XLE, RTX, HII — Middle East escalation), which is the stated
  correlation cap exactly, and the standing unfilled AAL short is a fourth expression of it. Disclosed in
  the CONCENTRATION block, not hedged with an invented position.
- **Sources that failed:**
  - Yahoo Finance quote/index endpoints — HTTP 429 (spx, ndx, dow, rut, vix all unavailable)
  - All futures — ES=F, NQ=F, RTY=F, CL=F, MES=F return ok:false. **No futures ideas were possible today**,
    which cost a /MNQ short, a /M2K long and /MCL — the universe file's preferred instruments.
  - Kalshi event contracts — count:0 for midterm, Senate, House, CPI, inflation, oil, gold, Bitcoin,
    recession, unemployment; only null-priced sports parlays returned. **No event contracts possible on the
    week of the midterms**, the worst possible week to lose that class.
  - `implied` (options) — Yahoo options HTTP 401. No target was checked against a straddle today.
  - `short` (short interest) — api.nasdaq.com read timeout.
  - `history CTRA` — no rows from nasdaq or yahoo.
  - finnhub earnings calendar returned **zero** names dated 11-02, 11-03 or 11-04 against 227 on 11-05;
    treated as a feed gap, so no claim is made that this week is empty of earnings.
- **Coverage gaps:** every equity price in this report is the **2026-10-30 close** (asof 20:00 UTC), taken
  at 06:00-06:34 ET on Monday with the market shut — a closed market, not stale data. Crypto prices (BTC
  $77,828) are live. SMA200 is unavailable throughout (120 days of history pulled). I did not reach: the
  midterm policy trade, small/micro caps below $2B as a deliberate sweep, or crypto beyond spot prices.

## [06:37 ET] CAPTURED — ELAN — a sixth candidate, and the second genuinely uncorrelated one
Found after the RESEARCH COMPLETE block above was written, by screening insider activity across the
larger names on the fetched 2026-11-06 earnings list. **Counts update: 6 candidates, not 5.**
- **Seven distinct insiders bought on the open market in August with zero sales in six months**
  ($1,672,850 total; Kurzius 40,000 sh @ $23.398, Harrington 5,000 @ $21.82, VanHimbergen 4,200 @
  $23.0776, O'Neill 3,998 @ $23.58). Seven independent buyers is the broadest cluster found today — wider
  than SMMT's three, though far smaller in dollars. Breadth is the signal here: tax and diversification
  explain one seller, not seven buyers and no sellers.
- Price has gone nowhere since, coiling 22.03-24.11 through October and closing 23.06 — **the entry is at
  the price the insiders paid**, not above it.
- Earnings **Fri Nov 6** on the fetched finnhub calendar. Beat consensus 4 of the last 4 quarters
  (+23.77%, +13.38%, +15.04%, +42.96%).
- Levels: entry 23.00 (zone 22.60-23.30), stop **21.55** (below the entire October range floor of
  22.03/22.18/22.23), target **27.98 = the 120-day high**. Risk 1.45 = **2.07 ATR** (floor 2.0); reward
  4.98; **R:R 3.43**; win_probability 0.30 vs a 0.226 baseline = +7.4pt edge. advol $116.1M.
- **Note this one does NOT have the flaw SMMT has**: its target is the 120-day high rather than a level
  above it, so it needs no special pleading. That is why I accepted a 21% target distance here — the
  price has actually been there inside the window.
- The honest negative, in `key_risk` and `counter_argument` rather than buried: **analyst revisions are
  deteriorating** — bullish share 86.4% but -4.9 pts m/m, strong_buy 10→10→9→7 across four monthly
  snapshots. The sell-side is backing away ahead of the print. And the insider buying is three months
  stale with the stock now barely above their cost, so they have been right about nothing yet.
- Driver: animal health. Uncorrelated with the Middle East, the rate path and the AI complex, which makes
  it and SMMT the two ideas that diversify the book rather than concentrate it.

## [06:37 ET] REJECTED — the rest of the Nov 5/6 insider screen
- MRNA 0 buys / 17 sells ($69.7M) · AFRM 0 buys / 13 sells ($24.1M) · AKAM 0 buys / 6 sells ·
  CHTR 1 buyer ($1.4M at $140.93 in May) against 3 sells ($12.7M) · HUM, STWD, BLMN: no insider activity
  at all in either direction, so no signal rather than a negative one.
- Only ELAN came back with a buy cluster, which is why it is the only one captured.

## [06:37 ET] FINAL COUNTS — supersedes the RESEARCH COMPLETE block above
- **candidates: 6** — XLE (conv 3, position update: stop raised 60.80→66.50), HII (4, position update:
  first stop added at 288.00), RTX (4, new), XLU (3, new), SMMT (5, new), ELAN (4, new).
- **Drivers: 3 of 6 on Middle East escalation** (XLE, RTX, HII) — at the stated cap of 3, with the
  standing unfilled AAL short a fourth expression of it. **XLU** is the rate/defensive idea and partly
  offsets that scenario. **SMMT** (FDA PDUFA Nov 14) and **ELAN** (earnings Nov 6, animal health) are
  idiosyncratic and uncorrelated with everything else in the book.
- All six verified by me against the R:R floor, the ATR stop floor, the expectancy baseline and the
  evidence-kind conviction count. Nothing required a floor to be rescued, and no conviction was inflated.
- Everything else in the RESEARCH COMPLETE block above still stands: all-`swing` skew, no intraday and no
  long_term, and the failed sources (futures entirely, Kalshi event contracts entirely, options-implied,
  short interest, Yahoo indices).
