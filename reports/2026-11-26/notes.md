# Research log — 2026-11-26

## [06:02 ET] SETUP — calendar context
- Today is **Thursday 2026-11-26 = US Thanksgiving Day**. US equity markets (NYSE/Nasdaq)
  are closed all day. Bond market closed (SIFMA). CME equity-index/metals/energy futures
  are closed during the US day session and reopen ~18:00 ET tonight. Crypto trades 24/7.
- Consequence per `config/strategy.md` "Weekend behavior": this run behaves like a weekend
  run. Equity ideas are **week-ahead preparation** with entry for the **next open =
  Friday 2026-11-27, which is a 13:00 ET early close** (half session, thin liquidity).
  Actionable-today lanes are crypto and event contracts.
- No intraday equity ideas are possible today. That is a calendar fact, not a thin tape.

## [06:02 ET] PRIOR CONTEXT — what it demands
- 16 open positions, 5 awaiting entry. Track record 5/48 target (10%), avg -5.9%.
- conviction 2: 0/7 target, avg -10.1% (n=9). Under 15 closed so formally noise, but it is
  the worst bucket and the direction matches conviction 4 being the best (2/10, -1.4%).
  **Action: raise the bar on conviction-2 today — only capture a 2 if the asymmetry is
  genuinely large, and size 0.5-1%.**
- long_term 0/5, avg -16.3% (n=8) — sample is tiny (8), and these are multi-year theses
  being graded in weeks. Do not abandon the lane; do demand a priced bear case.
- stock 2/34 (6%) vs etf 3/14 (21%). Single-name selection is where the damage is.
- IWM re-recommended 6x — do not touch unless something concrete changed.

## [06:03 ET] MACRO — the regime, from fetched data
All equity/ETF prices are the **2026-11-25 close** (markets shut for Thanksgiving);
`asof 2026-11-25T21:00Z`, age ~840 min. That is a closed market, not stale data.

| Instrument | Close 11/25 | ATR14 | ATR% | SMA20 | SMA50 | % off 120d high | % off 120d low |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 716.70 | 16.88 | 2.36 | 740.33 | 757.89 | **-8.3** | +4.4 |
| QQQ | 633.93 | 23.32 | 3.68 | 666.73 | 707.05 | **-16.9** | +4.6 |
| IWM | 268.87 | 6.24 | 2.32 | 274.39 | 277.16 | -11.9 | +4.9 |
| GLD | 327.45 | 8.87 | 2.71 | 354.04 | 371.04 | **-23.8** | +4.3 |
| TLT | 82.24 | 0.80 | 0.97 | 81.05 | 80.13 | -6.3 | **+7.6** |

- source: `scripts/market_data.py history <sym> --days 120` (nasdaq), quote via finnhub.
- Rates (FRED, 2026-11-24): 10y **4.91%** (prev 4.92), 2y **4.63%**, fed funds **3.88%**,
  10y-2y **+0.24** on 11/25 vs +0.28 prior — flattening. UNRATE 4.1% (Oct, from 4.2%).
  CPIAUCSL Oct 337.476 vs Sep 336.298 = **+0.35% m/m**, an uncomfortable monthly print.
- Crypto (CoinGecko, live): BTC **$60,454** (+2.8% 24h), ETH **$1,693** (+2.9%),
  SOL **$70.47** (+4.0%), LINK $9.19 (+6.3%), LTC $43.37 (+7.1%), XRP $0.949 (+4.1%).
  Everything green on the day, inside a very deep drawdown.
- **Read: this is a leveraged-risk unwind, not an inflation trade.** Nasdaq -16.9%,
  gold -23.8% and crypto deeply broken *while* long bonds rally (TLT above both its
  20d and 50d, +7.6% off its low) is the signature of de-grossing/liquidation — gold
  and bonds would not diverge that hard on an inflation impulse. QQQ at a 3.68% daily
  ATR is a market where any stop tighter than ~7% is noise.
- **Consequence for sizing and stops:** vol is roughly 1.5x normal. Every swing stop
  today has to be set off ATR, not off a chart-pretty level, or it is a coin flip.
- FAILED SOURCES (noted for data_quality_notes): Yahoo chart API returning **HTTP 429**
  for every symbol, so `macro` lost spx/ndx/dow/rut/vix/es/nq/DXY/us10y/gold/WTI.
  Finnhub refuses index CFDs ("Market data subscription required"). Stooq 404s on
  `^`-prefixed indices. **No VIX, no DXY, no futures quote available this run** — index
  levels below are proxied by their ETFs, which is an honest substitute for direction
  but not for a futures entry level.

## [06:04 ET] MACRO — THE DRIVER: the Fed is **hiking**, and that reframes everything
Kalshi (which backs Robinhood Prediction Markets), fetched live, event
`KXFEDDECISION-26DEC`, FOMC decision **2026-12-09 14:00 ET** (market close_time
2026-12-09T18:59Z):

| Outcome | yes_bid | yes_ask | last | volume | OI |
| --- | --- | --- | --- | --- | --- |
| Hike 25bps (`-H25`) | 92c | 93c | 92c | 5.09M | 3.06M |
| Hike 0bps / hold (`-H0`) | 4c | 5c | 5c | 10.77M | 6.01M |
| Hike >25bps (`-H26`) | 2c | 3c | 3c | 8.19M | 3.88M |
| Cut 25bps (`-C25`) | 0c | 1c | 1c | 1.69M | 1.52M |
| Cut >25bps (`-C26`) | 0c | 1c | 1c | 1.04M | 1.03M |

- source: https://api.elections.kalshi.com/trade-api/v2/markets?event_ticker=KXFEDDECISION-26DEC
- Forward path, same source: **27JAN H25 56/57c**, H0 43/44c; **27MAR H25 50/54c**,
  H0 44/46c, C25 3/7c. So ~1.6 further hikes priced through March 2027 after December.
- **Correction to my 06:03 read.** I called gold -23.8% a "liquidation signature, not an
  inflation trade". With a 92% hike priced and CPI running +0.35% m/m, the cleaner
  reading is a **hawkish real-rate repricing**: gold de-rates on rising real yields,
  Nasdaq de-rates on a higher discount rate, crypto (the longest-duration risk asset)
  de-rates hardest. Long bonds hold up because a hiking Fed into slowing growth is a
  bull flattener — and the curve did flatten, 10y-2y +0.28 -> +0.24.
- **This is now the correlation-cap constraint of the day.** Almost every idea available
  today is some expression of "the Fed is hiking into a slowdown". Per
  `config/strategy.md` no more than 3 ideas may share one driver, so candidates must be
  deliberately spread across *different* drivers, not across different tickers that mean
  the same bet.
- Open-position implication, flagged for the position-update pass: `TLT` BUY (entry 80.3,
  now 82.24) is long duration into a Fed that the market says hikes in 13 days, and
  `XLU` BUY is a bond-proxy. Both are the wrong side of a hike in the near term and the
  right side of a growth slowdown. Neither is yet near its stop.

## [06:07 ET] POSITION UPDATE — TLT — opened 2026-11-04 @ 80.30, now 82.24 (+2.4%)
- decision: **HOLD, levels unchanged** (target 84.30, stop 78.80). Captured via add_candidate.
- why: the curve flattened (+0.28 -> +0.24, FRED T10Y2Y) *while* TLT made a higher high
  with a 92% hike priced. That is a bull flattener — the market treating the hike as
  credible inflation-fighting rather than as more term premium. From 82.24 the target is
  +2.1% away and the stop -4.2%, so the remaining distribution improved since entry.
- deliberately NOT raising the stop. Raising it to ~80.60 would lift the printed R:R
  while making the trade strictly worse-tested — that is the KRE pattern CLAUDE.md names.
  78.80 is where the uptrend is actually wrong (below the 11/13 pivot at 79.11).
- caveat recorded: 78.80 is 1.88 ATR from entry against the 1.8 ATR ETF floor. It clears
  by 0.08 ATR. I would not open this fresh at that stop.

## [06:09 ET] MACRO — what actually broke, and the rotation that followed
Relative strength vs SPY, `market_data.py relstrength <s> --peer SPY` (computed from
fetched history). SPY itself: 1m **-6.9%**, 3m -7.1%, 6m -5.0%.

| Sector | 1m abs | 1m vs SPY | 3m vs SPY | 6m vs SPY |
| --- | --- | --- | --- | --- |
| XLP staples | +5.9% | **+12.8** | +15.5 | +14.3 |
| XLV health | +2.5% | +9.4 | +14.1 | +26.8 |
| XLU utilities | +1.8% | +8.7 | +8.1 | +2.7 |
| IWM small caps | -4.0% | +2.8 | -3.3 | -2.9 |
| XLE energy | -10.7% | -3.8 | +4.8 | +12.0 |
| SMH semis | **-24.3%** | **-17.4** | -19.2 | -24.6 |

- The news, 2026-11-25: Nasdaq **-4% intraday** before recovering to close SPX only
  -0.25%; NVDA -8.6%, AMD -9.6%, SOX -5.8%. NDX briefly entered a **bear market, -20%
  from its early-October peak**. SPX was -11.6% from the Oct 6 record as of Nov 20.
  Goldman's strategists say it has not bottomed.
  sources: https://www.cnbc.com/amp/2026/11/25/nvidia-ai-stock-tech-selloff.html ,
  https://www.fool.com/coverage/stock-market-today/2026/11/25/stock-market-midday-nov-25-nasdaq-plunges-4-as-ai-sell-off-deepens-and-inflation-remains-stubborn/
- Three stacked causes, not one: (1) doubt that AI capex earns its cost of capital,
  (2) a Fed that the market says hikes on Dec 9 with core PCE +3.8% y/y in October,
  (3) **fresh US tariff proposals** and post-midterm fears of AI regulatory scrutiny
  after a Democratic sweep. (2) and (3) are both inflationary; (1) is deflationary.
- **The important thing for today: the defensive side is not a fresh idea any more.**
  Everything in the rotation has already run. Off their 120-day lows: AZO +24.7%,
  CPB +29.6%, KR +29.0%, DG +34.6%, OLLI +54.8%. Off their highs: AZO -0.6%,
  CPB -1.8%, KR -2.8%, DG -3.7%. Buying a trade-down retailer into a December print at
  the top of a 35% run is chasing, and the first month of this report already showed
  what chasing costs. **REJECTED as a lane, not as individual names** — see below.

## [06:09 ET] REJECTED — DG, OLLI, KR, CPB, AZO — right thesis, wrong price; all within 4% of 120d highs after 25-55% runs, each with an earnings print inside 14 days

## [06:11 ET] NEWS — the day's real, dated, under-priced catalyst: Section 301 on "structural excess capacity"
- **2026-11-25**: USTR proposed new **Section 301 tariffs on 14 trading partners** for
  "structural excess capacity" in manufacturing. Named sectors: **batteries, cement,
  chemicals, processed food**. China and Vietnam 20%, Cambodia/Indonesia 18%, India 17%;
  EU, Japan, Korea, Taiwan, Thailand, Malaysia, Singapore, Switzerland, Bangladesh also
  named. **Semiconductors, autos, steel and aluminium are explicitly carved out** (they
  sit under separate authority). Separately: proposed 10% tariff on finished Embraer
  aircraft, and higher above-quota duties on Brazilian sugar.
- Process, and this matters for horizon: the rates are **proposals**, subject to a public
  comment period, "likely to come into effect in January at the earliest". So this is a
  weeks-to-months re-rating, not a one-day pop. A swing horizon fits; an intraday one
  does not.
  sources: https://www.cnbc.com/2026/11/25/us-tariffs-trump-section-301.html ,
  https://www.rte.ie/news/us/2026/1125/1600630-us-tariffs/ ,
  https://finance.yahoo.com/markets/article/us-announces-new-tariffs-of-up-to-20-on-china-the-eu-and-12-other-nations-131802359.html
- **The tape already voted, and this is the measured part.** On 2026-11-25, a day the
  Nasdaq was down 4% intraday and SPX closed -0.25%, the named-sector complex closed up
  on raised volume (closes and volumes from `market_data.py history`):

| Symbol | 11/25 close | 11/25 % | volume | prior-day volume | % off 120d high |
| --- | --- | --- | --- | --- | --- |
| OLN | 16.83 | **+6.4%** | 2.99M | 3.04M | -37.3 |
| HUN | 9.29 | **+6.2%** | 3.51M | 2.42M | -42.2 |
| EXP (cement) | 187.41 | **+4.8%** | 417K | 207K | -23.7 |
| WLK | 62.59 | +3.4% | 1.14M | 1.17M | -30.0 |
| DOW | 29.66 | +2.5% | 7.65M | 7.09M | -17.7 |
| LYB | 56.96 | +2.4% | 3.33M | 5.20M | -17.6 |
| CE | 45.44 | +2.4% | 1.73M | 1.78M | -15.9 |
| EMN | 61.64 | +1.5% | 1.18M | 1.06M | -20.1 |

- **Why this is the one worth working today.** Global chemical and cement overcapacity
  out of Asia is the precise mechanism that has de-rated these names 15-42% — it is not a
  vague macro wish, it is the single line item in their margin story. An action aimed at
  exactly that is a change in the thing that broke them. And unlike the staples trade,
  the complex is near its *lows*, not its highs, so the entry is not a chase.
- **Correlation cap applies hard here.** `config/strategy.md` allows at most 3 ideas on
  one driver. HUN is already an open position in this lane, so at most two more.

## [06:14 ET] FILINGS/PRIMARY — Section 301: what the notices actually say
Read via the law-firm walkthrough of the 14 Federal Register notices (the USTR PDF itself
is a compressed stream I could not extract, and the USTR landing page still shows only the
March-2026 investigation dates — recorded as a source limitation):
https://www.cmtradelaw.com/2026/11/ustr-proposes-new-section-301-tariffs-on-14-economies-over-structural-excess-capacity/

- Determinations and proposed notices issued **2026-11-25**; investigations opened
  2026-03-11. **Comments due 2027-01-05**, requests to appear 2027-01-05,
  **public hearing 2027-01-25 10:00 ET at the USITC**. **No effective date is stated** —
  the notices say nothing takes effect yet.
- Proposed ad valorem rates (proposal / alternative): **Vietnam up to 35%**, India up to
  25%, **China up to 20%** generally (10% on Annex A, 0% on Annex B, a 40% figure also
  appears in the table), Singapore up to 20%, Bangladesh / Cambodia / Indonesia /
  Malaysia / Thailand up to 18%, **EU 15%**, Japan / Korea / Switzerland up to 15%,
  Taiwan 15%. Mexico and Norway: no determination.
- **Exclusions matter as much as inclusions**: articles already under Section 232 are
  carved out — aluminium, steel and copper and derivatives, passenger and commercial
  vehicles and parts, wood products, patented pharmaceuticals, and **semiconductors**.
  China's notice has no 232 carve-out at all.
- **So this is explicitly NOT a rescue for semis.** The one complex that has been
  destroyed is the one excluded. Anyone reading the tariff headline as a semi trade has it
  backwards, which is part of why the chemicals move is under-owned.
- **Honest limits on the dated catalyst**: the only hard dates are 2027-01-05 (comments)
  and 2027-01-25 (hearing). There is no implementation date, and press reporting of a
  "January at the earliest" start is an inference, not a notice. Any idea in this lane is
  a **re-rating over weeks on a policy process**, and that must be stated rather than
  dressed up as an imminent event. The sector list (batteries, cement, chemicals,
  processed food) comes from press reporting of the USTR official's remarks, **not** from
  an annex I was able to read — flagged for data_quality_notes.

## [06:18 ET] REJECTED — OLN — the obvious tariff long is the same security as an open position, on 5.2x leverage
Read Olin's Q3 2026 earnings 8-K exhibit directly
(https://www.sec.gov/Archives/edgar/data/74303/000007430326000091/exhibit991q32026earningspr.htm):
- **OLN and HUN are merging.** All-stock *merger of equals* announced 2026-06-16 to form
  **OlinHuntsman Corporation**, expected to **close Q1 2027**. Both shareholder votes have
  passed, the US HSR waiting period has expired, remaining regulatory approvals pending.
- So OLN and HUN are one bet at a fixed stock ratio, and the fact that they printed
  +6.4% and +6.2% on the same day is largely **one move in one security**, not two
  confirmations. Publishing OLN alongside the open HUN position would be the duplicate
  the correlation cap exists to stop. **OLN rejected on that ground alone.**
- And the balance sheet says don't, independently: **net debt $2,798.3M, leverage 5.2x**
  adjusted EBITDA at 2026-09-30, up from 3.7x a year earlier — and Q4 2026 adjusted
  EBITDA is guided to **$80-100M against Q3's $191.4M**, a ~50% sequential fall, which
  annualises the leverage toward ~7x. Into a Fed that the market says hikes on Dec 9.
  Q3 diluted EPS $0.13 vs $0.37; Chlor Alkali segment earnings $71.3M vs $127.6M, $32.1M
  of that a Freeport VCM operating issue. Epoxy only just broke even at +$0.6M.
- Note for the record: Olin's Q4 outlook language is "continued pressure from subsidized
  Asian exports" — the mechanism is real and management names it. The equity is still the
  wrong vehicle at 5-7x levered.
- Correction to my 06:11 read: the 11/25 chemicals move is **narrower** than that table
  made it look, because its two biggest movers are one company. The independent
  confirmations are DOW +2.5%, LYB +2.4%, WLK +3.4%, CE +2.4%, EMN +1.5%, EXP +4.8%.
- Trade-case context (secondary, flagged as such): US AD duties were imposed on epoxy
  resins from Korea, Taiwan and Thailand in 2025; the **China and India cases were
  terminated** on a USITC negligible-imports finding. The EU imposed definitive duties on
  China/Taiwan/Thailand in July 2025. So epoxy is a case where China is *already* largely
  shut out of the US, which is a reason the Section 301 read-through to epoxy is weaker
  than the headline suggests. source:
  https://www.resourcewise.com/blog/global-epoxy-producers-face-the-choice-defend-price-or-volume

## [06:18 ET] POSITION UPDATE — HUN — opened 2026-11-10 @ 9.00, now 9.29 (+3.2%)
- decision: **HOLD, levels unchanged** (target 10.82, stop 8.09). Captured.
- what changed, concretely: (a) Section 301 chemicals proposal 11/25 and a +6.2% close on
  the heaviest volume in a month, an outside-up bar (8.67 open, 8.53 low, 9.36 high, 9.29
  close) three sessions off the 8.32 pivot; (b) the Olin merger has cleared both
  shareholder votes and HSR, close expected Q1 2027.
- market cap $1.63B, $27.1M/day dollar volume (`market_data.py profile/history`) — under
  $2B so the figure is stated in the thesis and size is held at 2%.
- stop honesty: 8.09 is below the 11/23 pivot 8.32 but ABOVE the 120-day low 7.995, and
  that is said in key_risk. 0.91 from entry = 2.28 ATR on a 0.40 ATR, clears the 2.0 stock
  floor. R:R exactly 2.00 — at the floor, not above it, and I am not nudging the target to
  improve the look of it.
- win_probability 0.38 against a 0.333 baseline: a 4.7-point claimed edge, deliberately
  small. From 9.29 the target is 3.8 ATR away and the stop 3.0 ATR away, so the *remaining*
  path is slightly adverse even though the R:R from entry is 2.0. That asymmetry is why
  the claim is modest rather than the 50%+ the headline would invite.

## [06:18 ET] REJECTED — WLK, DOW, LYB, CE, EMN, EXP — the rest of the Section 301 chemicals lane
- Already one open position (HUN) in this driver; the cap is 3 ideas per driver, and I am
  not spending the other two on names with weaker evidence than the one already held.
- `insiders`/`analysts` fetched for each: **no open-market insider buying in any of them**
  (WLK 0 buys / $3.12M sold, DOW 0/0, LYB 0/0, EXP 0 buys / $1.70M sold), and
  `revision_direction` "deteriorating" for all four. DOW is the one with real earnings
  momentum — **4 of 4 quarters beaten** (+10.2, +11.6, +51.8, +27.5%) — and is the name to
  revisit if this lane earns a second slot; it closes 29.66, below both its 20-day 31.69
  and 50-day 30.33, so there is no hurry.
- EXP (cement, $5.70B) is the cleanest *mechanism* — imported cement from Vietnam and
  Turkey at a proposed 35%/— rate — but its analyst mix went from 5 bullish of 16 to
  **0 bullish of 19** in two months (bullish share -31.2 points), insiders sold $1.70M,
  and 1 beat in 4. A sector tailwind does not fix a company every analyst is backing away
  from. **Watchlist, not a recommendation.**

## [06:23 ET] EVENT CONTRACTS — worked properly, and the honest answer is "no trade"
The `market_data.py events` helper is **not fit for this purpose** and should be treated as
broken: it pulls the first 200 open Kalshi markets unsorted and filters client-side, so
`events "CPI"`, `events "Bitcoin"` and `events "recession"` all returned **nothing** while
`events "Fed"` returned five esports roster markets. All event work below went straight to
the Kalshi REST API by series and event ticker. **Worth fixing in `scripts/market_data.py`
— it accepts a `series_ticker` and `event_ticker` parameter that the helper never uses.**

### Core CPI, November 2026 — the one real candidate, and why it is a watchlist item
- `KXCPICORE-26NOV-T0.2`, "Will CPI Core rise more than 0.2% in November?" Resolves on
  the **seasonally adjusted** BLS core CPI m/m for Nov 2026, **single-decimal as published**
  — so YES needs a printed 0.3% or higher. Closes 2026-12-10 08:25 ET, minutes before the
  08:30 release; `can_close_early: true`; OI 34,680 but **200 contracts of 24h volume**.
  Quotes now: yes 45/46c, **no 54/55c**, last 44c.
- Fetched core CPI (FRED `CPILFESL`) m/m, unrounded: Jul +0.22, Aug +0.29, **Sep +0.33,
  Oct +0.30**. Three straight prints that would each have resolved this YES.
- Fetched the **Cleveland Fed inflation nowcast, updated 11/25**: core CPI Nov m/m
  **+0.21%**, headline -0.00%, core PCE +0.27%, headline PCE +0.14%.
  source: https://www.clevelandfed.org/indicators-and-data/inflation-nowcasting
- A printed 0.3 needs an unrounded >= 0.25, i.e. +0.04pp above the nowcast. At a nowcast
  σ of 0.09-0.13pp that is P(YES) ~ 33-38%, against the market's 45-46%. NO at 55c would
  be a ~9-point edge, +16% expected over 14 days.
- **I am not taking it, and the reason is the number the market already shows.** Back out
  the market's distribution: P(<=0.1) 12.5%, P(0.2) 42%, P(0.3) 35.5%, P(>=0.4) 9.5% —
  mean **~0.24%**. That is almost exactly halfway between the nowcast's 0.21 and the
  0.30 three-month run rate. The market is not mispriced; it is explicitly splitting the
  model against the momentum, and "NO" is just a wholesale bet on the model. With core
  accelerating 0.22 -> 0.29 -> 0.33 -> 0.30 and tariff passthrough still arriving, betting
  the model against the trend is not an edge I can defend.
- **WATCHLIST with a condition**: if the Cleveland Fed core-CPI nowcast drifts to **0.18%
  or below** while `KXCPICORE-26NOV-T0.2` still bids 45c or better, buy NO. That is a real
  disagreement rather than a coin-flip; today it is not.

## [06:23 ET] REJECTED — KXCPI-26NOV (headline) — a rounding/seasonality trap, not an edge
The ladder implies a modal November headline of **-0.1% m/m** (P(>-0.2)=68c, P(>-0.1)=32c,
P(>0.0)=7c), while the Cleveland Fed nowcasts -0.00% and SA headline CPI has printed
+0.40, +0.65, +0.35 the last three months. That 40-point "gap" is almost certainly a
basis difference: the core market's rules say "seasonally adjusted" explicitly and the
headline market's rules **do not**, and NSA headline CPI falls in November on gasoline
seasonality. Comparing an SA nowcast to an NSA contract would have manufactured an
enormous fake edge. No trade.

## [06:23 ET] REJECTED — KXBTCY (BTC end-of-2026 range) — efficiently priced
Full 28-strike ladder fetched. Implied: P(BTC 60-65k on 2027-01-01) 25.0%, 55-60k 20.1%,
65-70k 15.6%, 50-55k 9.6%, 70-75k 7.6%; P(>=100k) ~1.4%; P(<=20k) 0.9%. BTC spot 60,454.
Realized daily sigma from 20 sessions of IBIT closes is **3.04%**, so ~25 trading days to
Jan 1 gives a 15.2% sigma, i.e. a 1σ band of 51.2k-69.6k. The market puts 70.3% in
50-70k against ~73% for a 1.1σ normal. There is nothing to disagree with.

## [06:23 ET] REJECTED — Fed December event contracts — 92c is not a trade
`KXFEDDECISION-26DEC-H25` at 92/93c offers 7-8% gross for carrying FOMC risk 13 days; the
`-H0` hold leg at 4/5c is the interesting side of it and is addressed separately under
awaiting-entry housekeeping. Jan (56/57c) and Mar (50/54c) are coin flips with no
information I hold that the curve does not.

## [06:26 ET] REJECTED — the three fresh ideas I worked and could not make clear the floors
Each is rejected on arithmetic, with the arithmetic shown, so synthesis does not re-open them.

- **DOW** — the best of the chemicals complex on fundamentals: **4 of 4 quarters beaten**
  (+10.2, +11.6, +51.8, +27.5%), $21.5B cap, close 29.66, -17.7% off the 120-day high.
  But the honest stop is 26.40, below the 26.605 120-day low, which is 3.26 = **2.96 ATR**
  away; 2.0 R:R then needs a target of **36.18, above the 36.04 120-day high**. The idea
  only publishes by asserting a full round trip to the high, and the only `positioning`
  read available is analyst revisions, which are *deteriorating*. It is a conviction-3
  deep cyclical, levered, needing a complete retrace, into a hiking Fed. No.
- **Gold / GLD long after the washout** — the genuinely interesting long-term story of the
  day: ~$3,565 spot (GLD 327.45) against a late-January peak near $5,590, a 35-37%
  drawdown, with 10y TIPS real yields at **2.88%** (up 22bp in seven sessions to 11/18)
  as the stated cause, and reported central-bank buying of 321t. The arithmetic kills it:
  anchor the target to a 100bp fall in real yields once the cycle ends and you get roughly
  $4,200 / GLD ~385, +17.6%; an honest bear case of real yields to 3.5% with central banks
  pausing is ~$2,800 / GLD ~257, -21%. That is **0.82:1 against a 2.5 long-term floor** —
  it fails by a factor of three. A 35% drawdown is not an edge while the thing that caused
  it is still going. **Watchlist with a condition: the 10y real yield back below 2.70%.**
  sources: https://www.cnbc.com/2026/11/19/gold-prices-fall-fed-rates-dollar.html ,
  https://goldsilver.com/industry-news/article/gold-price-outlook-november-2026/
- **NKE / DECK short on the proposed 35% Vietnam rate** — the rate is the highest of the
  14, above China's 20%, and Vietnam is where footwear went to escape the China tariffs,
  so the setup looked sharp. It is wrong, and the tape says so: NKE went 32.92 (11/20) ->
  33.76 -> 35.75 -> **36.66, +11.4% in three sessions straight through the announcement**.
  The mechanism: the notices' product annexes exclude, among others, **"products not
  produced in sufficient U.S. quantities"**, and the US makes almost no footwear — so
  apparel and footwear are the textbook exclusion, and the action targets excess-capacity
  manufacturing sectors, not consumer goods. **This also resolves the LULU question**: the
  Vietnam rate does not materially raise the risk on the open LULU idea.

## [06:26 ET] POSITION UPDATE — HII — opened 2026-10-12 @ 262.00, now 299.34 (+14.3%)
- decision: **HOLD, hard stop unchanged at 238.50, trailing plan added.** Captured.
- the change: trim half at **325.00** (below the 334.53 120-day high), trail the rest under
  **279.80** (the 11/20 swing low; 50-day 282.11 just above). Deliberately an addition to
  `scale_plan` rather than a move of the published stop — moving the stop to 280 would
  print a 5.98:1 ratio on a trade actually taken at 3.31:1, which is the exact arithmetic
  dishonesty CLAUDE.md records.
- why now: 48% of the entry-to-target distance is covered while the hard stop sits 20.3%
  below the market. There was no risk management on the report's second-largest winner.
- evidence: outperforming SPY **and ITA** on 1m/3m/6m (+6.4/+12.6/+5.7 vs sector) —
  leadership inside a lagging group. Against it: 3 insider sells totalling $5.61M, 0 buys.

## [06:26 ET] POSITION UPDATES — the other thirteen, decided and recorded, no capture
Live prices fetched (finnhub, 11/25 close). `vs entry` recomputed from the prior-context
entries. **Decision for every one of these is hold, unchanged**, so none is re-published:
re-publishing an unchanged idea is the anchoring pattern `prior_context.md` warns about.

| Symbol | Now | vs entry | Note |
| --- | --- | --- | --- |
| KHC | 26.51 | **+15.3%** | +3.68% on 11/25; **only 6.0% from the 28.09 target** — let it run to target, no change |
| DKS | 158.59 | +9.8% | +3.54% on 11/25; target 175.50 |
| CAG | 15.67 | +8.8% | +3.91% on 11/25; **carries no stop** — invalidation, not a level, per the long-term rule |
| ABT | 108.00 | +4.9% | target 117.34 |
| UNP | 298.38 | +3.4% | +2.60% on 11/25 |
| PFE | 28.46 | +3.1% | **no stop**; unchanged on 11/25 |
| VZ | 47.28 | +2.8% | opened 11/22 |
| CVS | 81.06 | +1.3% | 4x recommended — explicitly not touching it |
| XLU | 43.61 | +0.7% | a bond proxy into a 92%-priced hike; outperforming SPY 1m/3m/6m, so held, and the Fed read is carried in the TLT update instead |
| XLV | 183.68 | -0.2% | -0.56% on 11/25, the only open position down on the day |
| OXY | 53.95 | -0.1% | XLE -10.7% on 1m and -3.8% vs SPY; weakest open lane, stop 50.15 intact |
| RTX | 196.19 | -1.4% | stop 186.00 |
| IWM | 268.87 | -0.6% (short, so ~+0.6%) | **6x recommended.** Macro supports it, but IWM is *outperforming* SPY on 1m (+2.8) — the damage is mega-cap AI, not small caps, so the thesis is working for the wrong reason. Hold, and do not re-pitch a 7th time. |

- Worth flagging for synthesis: the open book is **long defensives in size** — XLP-type
  staples (KHC, CAG), health (PFE, ABT, CVS, XLV), utilities (XLU), duration (TLT) — and
  on 11/25 all of it rallied against a -4% intraday Nasdaq. That is the book working, and
  it is also a concentration: twelve of sixteen open positions share one driver.

## [06:30 ET] AWAITING-ENTRY HOUSEKEEPING — four of the five should be retired
These were published and never filled, so they are not positions. Re-pitching one amends
rather than duplicates — but three of them have levels the market has left behind by
double digits, and a level nobody can reach is not a recommendation, it is clutter on the
sheet. **Synthesis should retire these rather than carry them forward:**

- **`GLD` SELL @ 406.77** (published 2026-10-25). GLD is **327.45** — the entry sits
  **24.2% above the market** and will not be reached. The thesis was right and the fill
  never came. Re-shorting now would be selling 4.3% off the 120-day low of 313.96 after a
  23.8% fall, which is the mirror image of chasing, and `config/universe.md` would route a
  fresh bearish gold view to `/MGC` rather than a margin short of GLD anyway. **Retire.**
- **`/MBTZ6` SHORT @ 74075** (published 2026-11-09). BTC is **$60,454** — the entry is
  **18.4% above the market**; the whole move happened without a fill. Z6 is also the
  December contract and is approaching expiry, which `config/universe.md` forbids
  recommending into. Rolling to F7 and shorting 60k after a ~52% drawdown is not the same
  idea. **Retire.**
- **`LEN` BUY @ 79.5** (published 2026-11-13). LEN is **86.79**, i.e. **9.2% above** the
  entry — the market ran away. And the fundamental case got worse, not better: the 10-year
  is at 4.91% and the Fed is 92% priced to hike, which is the wrong backdrop for a
  homebuilder. **Retire** rather than chase. (TOL reports 2026-12-07 if the lane is worth
  revisiting.)
- **`KXFEDDECISION-26DEC-H0` YES @ 10** (published 2026-11-21). Now **4c bid / 5c ask**,
  so it is available cheaper than the published level, which is the one case where a stale
  level is stale in the holder's favour. I am still retiring it, because the thesis — that
  market stress forces a pause — has a direct precedent against it: the Fed hiked on
  2018-12-19 in the middle of a ~20% S&P drawdown. With core PCE at 3.8% y/y I put a hold
  at 6-8% against a 5c ask; that gap is inside the bid/ask spread. **No edge. Retire.**
- **`LULU` BUY @ 106.05** (published 2026-11-25, one day old). LULU is **107.44**, 1.3%
  above the entry, and earnings are **2026-12-09 (after the close)**, confirmed on the
  fetched finnhub calendar. The level is live and current. I checked the one thing that
  could have broken it — the proposed 35% Vietnam rate — and concluded it does not (see the
  NKE rejection). **Level stands unchanged, no re-pitch needed.**

## [06:30 ET] REJECTED — HRL — the best fresh idea of the day, killed by the correlation cap
4 of 4 quarters beaten (+3.7, +11.0, +4.8, +5.0%), **a director open-market buy** — William
A. Newlands, 10,000 shares at $20.10 on 2026-10-05 ($201K) — an analyst book with 1 strong
buy, 5 buys, 9 holds and **zero sells**, earnings **2026-12-03** on the fetched calendar,
23.09 against a 21.04 50-day, and processed food is a Section 301 named sector. Three
distinct evidence kinds, a conviction 4.
**Rejected anyway**: `config/strategy.md` caps three ideas per driver, and the defensive
consumer-staples driver is already carried by the open KHC and CAG positions plus the whole
XLP leadership read. HRL would be the fourth. Secondary doubts that make the cap easy to
accept: it is +21.8% off its 120-day low, 11/25 was a down bar on the heaviest volume of
the month (open 23.555, high 23.59, low 22.78, close 23.09 on 6.85M), and an honest stop
below the 11/11 low of 21.68 needs a 26.07 target to clear 2.0 R:R — a 12.9% move to a
four-month high, through an earnings print five sessions away. **Top of the watchlist.**

## [06:30 ET] REJECTED — ERJ (Embraer) — no price from any working source, so no levels
The cleanest *mechanism* on the board: the White House proposed a **10% tariff on finished
aircraft made by Embraer**, a single-company trade action, and US regional carriers are
Embraer's largest market. An entirely different driver from everything else today.
Unpublishable: `quote` and `history` both failed on every source — finnhub returns the B3
listing with all zeros, nasdaq has no rows for the ADR, Yahoo is HTTP 429. `profile` works
(Embraer SA, Aerospace & Defense, exchange B3 S.A.). **Never state a price I did not fetch**,
so there are no levels and there is no candidate. Recorded as a coverage gap, not an idea.

## [06:32 ET] REJECTED — crypto, both directions — and the reason generalises, so it is worth stating
The only driver with no open position against it, and the one lane tradeable today while
the equity market is shut. Fetched live: BTC **$60,454** (+2.8% 24h), ETH **$1,693**
(+2.9%), SOL **$70.47** (+4.0%), LINK $9.19 (+6.3%), LTC $43.37 (+7.1%) — everything green
inside a deep drawdown. IBIT printed a **new low at 32.35 on 11/25 and closed 34.07**, up
on the day, after a 109M-share capitulation bar on 11/20. Tempting.
- Realized daily sigma from 20 sessions of IBIT closes: **3.04%**. ATR14 **4.75%**.
- `config/strategy.md` sets the crypto swing stop floor at **2.5 ATR = 11.9%**, and the
  swing R:R floor at 2.0 — so any compliant crypto swing needs a **23.8% target**.
- Long: stop ~53,250, target ~**74,850**. Short: stop ~67,650, target ~**46,065**.
- Now price those targets off Robinhood's *own other venue*. The `KXBTCY` ladder for
  2027-01-01 (36 days) implies **P(BTC >= 75k) ~ 10.5%** and **P(BTC <= 46k) ~ 7%**.
- Both are far under the **33.3% break-even** that 2.0 R:R demands. **At today's realized
  volatility no crypto swing trade can clear the reward-to-risk floor with a compliant
  stop, in either direction** — the required target is a ~10% outcome on the event market.
  That is not a view about Bitcoin; it is the floors and the vol doing their job, and it is
  the cleanest expectancy rejection available because one Robinhood venue priced the other.
- A bearish crypto view would in any case have to be `/MBT` short, not a spot `sell`
  (Robinhood Crypto cannot short) — and the stale `/MBTZ6` entry is retired above.

## [06:32 ET] HRL — footnote to the rejection: the arithmetic kills it too, not just the cap
My cap reading is arguable (KHC and CAG are open *positions*; today's report carries no
staples idea), so here is the level work that makes the rejection safe either way.
- Honest pullback entry is the 22.35-22.60 shelf — the 20-day at 22.35 with the 11/16 low
  22.38 and the 11/18 low 22.335, which is real support rather than a reflex discount.
  From 22.45 a stop below the 11/11 low of 21.68 is 0.90 = **1.42 ATR, failing the 2.0 ATR
  stock floor**. Widening to 21.10 (2.13 ATR) puts the 2.0 R:R target at **25.15**, above
  anything traded in 60 days.
- And the structure is the real problem: that is **a pullback entry placed across an
  earnings date**. It fills only if HRL first falls 2.8%, and the most likely way it falls
  2.8% is a 12/03 miss that goes straight through 21.10 as well. Entering at the market
  instead needs a 27.07 target — above the 26.6 120-day high — to clear 2.0.
- Either way it fails on its own numbers. Watchlist, and revisit **after** 12/03 prints.

## [06:34 ET] FILINGS — HUN insider check, and the correction it forced
Pulled HUN's EDGAR filing list and read the two most recent primary documents directly,
because I had already published insider buying as evidence and a Form 4 dated 11/24 plus a
Form 144 dated 11/23 appeared in the list:
- **Form 4, filed 2026-11-24**: Scott J. Wright, **Division President** (officer, not a
  director). Transaction 2026-11-23, code **S** (disposition), **10,317 shares at $8.441**,
  **183,850 shares held afterwards**.
  https://www.sec.gov/Archives/edgar/data/1307954/000121465926014712/marketforms-74411.xml
- **Form 144, filed 2026-11-23**: aggregate market value **$87,085.80**, approximate sale
  date 11/23/2026, nature of payment **Compensation** — i.e. the same transaction, in
  shares received as pay.
- Read: **small and not a signal, but it had to be disclosed.** $87K is 5.3% of his
  holding, it was compensation stock, and he sold within 1.5% of the 8.32 swing low. It
  does not offset the CEO's $981,000 open-market purchase at 9.81 on 2026-08-03 — above
  today's 9.29, and after the merger was announced.
- **HUN re-captured** with this in `counter_argument` and in the evidence detail.
  Conviction unchanged at 4: the Form 4 is a second `primary_document`, and two entries of
  the same kind are one confirmation, so reading it correctly cannot raise the score.
- `short` interest is **unavailable all run**: `api.nasdaq.com` read-timed-out on every
  attempt (HUN, OLN, EXP). So no days-to-cover or crowding read on anything today.

## [06:34 ET] MACRO — energy, for the OXY hold
No WTI quote available (Yahoo 429, and the `KXOIL` Kalshi series returned no open events),
so oil is proxied by USO: last **139.89**, **-18.6% off** its 120-day high of 171.82 but
**+36.6% off** its low of 102.42, below the 20-day 145.71 and the 50-day 150.35, ATR 3.4%.
Oil bounced +3.3% on 11/25.
- So energy is a pullback inside a large up-move, not a breakdown — which is both why XLE
  is -10.7% on the month and why oil is part of the inflation problem the Fed is hiking
  into. OXY'S stop at 50.15 is 7.0% below the 53.95 last; the position is flat and the
  hold needs no amendment. This is the weakest open lane and the one to watch.

## [06:33 ET] REJECTED — ENS (EnerSys) — a 46% fall I could not account for is a research gap, not an idea
The single most interesting disconnect I found, and I am not publishing it.
- $4.55B cap, $81.5M/day dollar volume. Close **127.77**, **-46.2% off** the 120-day high
  of 237.52 and only **+4.2% off** the 120-day low of 122.60, which it set on 11/25.
- Against that: **4 of 4 quarters beaten**, and an analyst book of 4 strong buy / 3 buy /
  3 hold / **0 sell** — a 70.0% bullish share, the highest of anything I looked at today —
  plus one (tiny, $24,675) open-market insider buy and no sales. Batteries are a Section
  301 named sector, so the policy lane applies to it too.
- Checked the obvious explanation and it is not the explanation: the 8-K of 2026-10-27 is
  ENS **acquiring** Ultralife Corp at $16.00/share cash via tender offer, no financing
  condition, outside date 2027-04-27, $10.3M termination fee — so a deal of roughly $340M
  against a $4.55B acquirer. Too small to explain a 46% de-rating.
  https://www.sec.gov/Archives/edgar/data/1289308/000119312526434415/d143472d8k.htm
- Nor was it the print: the 10-Q and 8-K of 2026-11-12 sit in the middle of the slide
  (147.65 on 11/11, 147.80 on 11/12, 143.00 on 11/13). The two worst days were **11/04-05,
  168.19 open to 142.58 close, -15%**, a week before earnings, and I could not establish
  what happened then.
- The tape is a relentless grind with no base — 168, 156, 142, 147, 151, 147, 143, 138,
  136, 135, 132, 124, 132, 127, 127 — at a **5.66% daily ATR**. A -46% move whose cause I
  cannot name is a falling knife and the bullish analyst book is a lagging indicator, not a
  confirmation. **Explicit coverage gap: find out what happened to ENS on 2026-11-04.**

## [06:33 ET] RESEARCH COMPLETE
- **candidates captured: 3 unique symbols, 4 lines** (HUN appears twice; the second line is
  the one to use — synthesis takes the last entry per symbol — and it adds the Form 4
  disclosure to the counter-argument). All three are **position updates on open positions**:
  `TLT` hold, `HUN` hold, `HII` hold with a trailing plan.
- **Zero new recommendations, and that is the finding rather than a shortfall.** The report
  already holds 16 positions, twelve of them on the one driver that is working — defensives
  and duration against a hiking Fed — and on 11/25 all of it rose against a -4% intraday
  Nasdaq. Every fresh idea I worked failed a stated floor, with the arithmetic recorded
  above: DOW needs a target above its 120-day high to clear 2.0 R:R; gold clears 0.82
  against a 2.5 long-term floor; HRL's honest stop is 1.42 ATR against a 2.0 floor and its
  entry would straddle an earnings date; crypto cannot clear 2.0 R:R in either direction at
  a compliant 2.5 ATR stop, since the required target is a ~10% outcome on Kalshi's own
  ladder; the core-CPI contract is priced exactly between the nowcast and the trend; NKE
  was falsified by its own +11.4% three-day rally through the news; ENS I could not
  explain; ERJ had no price from any source.
- **Day-type note for synthesis**: today is **Thanksgiving**. US equities, bonds and the CME
  day session are closed, so every equity level here is the **2026-11-25 close** and no
  intraday idea was possible. The next session is **Friday 2026-11-27, a 13:00 ET early
  close** — thin, half-session liquidity, which is a bad tape in which to start new
  positions and a further reason three holds is the right answer.
- **Retire from awaiting-entry** (details above): `GLD` SELL @406.77 (24.2% above market),
  `/MBTZ6` SHORT @74075 (18.4% above market, and a December contract near expiry), `LEN`
  BUY @79.5 (9.2% below market, and the rate backdrop got worse),
  `KXFEDDECISION-26DEC-H0` YES @10 (no edge at the 5c ask; the Fed hiked on 2018-12-19 in a
  ~20% drawdown). **Keep** `LULU` BUY @106.05 — one day old, 1.3% below market, earnings
  2026-12-09 amc, and the Vietnam-tariff risk checked out as immaterial.
- **Watchlist, each with the condition that would make it a trade**:
  `HRL` — revisit after the 2026-12-03 print; `DOW` — the chemicals lane's second slot if
  it gets back under its 50-day with a reachable target; `EXP` — cement mechanism, but 0
  bullish analysts of 19; `KXCPICORE-26NOV-T0.2` NO — buy if the Cleveland Fed core nowcast
  drifts to <=0.18% while it still bids 45c; `GLD` long — if the 10y real yield falls back
  below 2.70%; `ENS` — only after the 11/04 fall is explained.
- **coverage gaps**: no VIX, no DXY, no index or futures quote, no WTI, and **no options-
  implied move for any name** — so not one idea today was checked against what options
  price, which `config/strategy.md` asks for at the level-setting stage. No short-interest
  or days-to-cover read on anything. No ERJ price. No small- or micro-cap screen was
  possible without a screener, so that lane went unhunted. ENS's November decline unexplained.
- **sources that failed**:
  - **Yahoo Finance chart + options API — HTTP 429 all run.** This is the big one: it cost
    `macro` its spx/ndx/dow/rut/**vix**/es/nq/**DXY**/us10y/gold/WTI legs, cost every
    `implied` call (401/429), and cost ERJ entirely.
  - **api.nasdaq.com `short` — ReadTimeout on every call** (HUN, OLN, EXP).
  - **finnhub** — refuses index CFDs ("Market data subscription required"); returns all
    zeros for the ERJ ADR.
  - **stooq** — 404 on every `^`-prefixed index symbol.
  - **alphavantage** — no API key configured.
  - **`market_data.py events` is effectively broken** — it fetches the first 200 open Kalshi
    markets unsorted and filters client-side, so `events "CPI"`, `"Bitcoin"` and
    `"recession"` all returned nothing and `events "Fed"` returned esports rosters. All
    event work went direct to the Kalshi REST API by `series_ticker`/`event_ticker`, which
    the helper already accepts but never passes. **Worth fixing.**
  - **USTR's own Federal Register PDF** would not extract (compressed streams), and the USTR
    landing page still shows only the March-2026 investigation dates, so the Section 301
    sector list rests on press reporting of the official's remarks rather than on an annex
    I read. Flagged for `data_quality_notes`.

## [06:36 ET] ADDENDUM — ENS: the gap is now closed, and the rejection is stronger for it
Went back at the 11/04 question with the time left. Partial answer, and it changes the
framing from "unexplained" to "explained and still a no":
- **Fiscal Q2 (reported ~2026-11-11/12): adjusted EPS $3.22 against $3.20 expected — a
  beat — but revenue missed, $949.9M against $972.35M.** So `beats_last_4 = 4` was reading
  the EPS line of a company whose top line is deteriorating, which is exactly the kind of
  confirmation that looks like evidence and is not.
- **The bullish analyst book is actively being marked down**: Oppenheimer cut its target
  from $250 to $210 on 2026-11-13 (keeping Outperform, which is why the rating counts never
  moved), and Weiss downgraded buy to hold on 2026-11-11. That reconciles the 70% bullish
  share with the "deteriorating" revision direction — the ratings are stale and the targets
  are not.
- Still not established: what specifically took 168.19 to 142.58 on 11/04-05, a week before
  the print. It coincides with the broad AI-power de-rating, but I could not source it.
- **So: rejection confirmed, and the earlier note overstated the disconnect.** A 46% fall
  with a revenue miss, a 16% target cut and a downgrade is a stock being re-rated, not a
  stock being overlooked. source:
  https://www.marketbeat.com/instant-alerts/price-enersys-nyse-ens-hits-new-1-year-low-heres-what-happened-2026-11-19/

## [06:36 ET] LANE GAP — long_term got no idea today, deliberately, and here is the shortlist
`config/strategy.md` gives durable mispricings ~15% of the budget and warns the lane is the
one most easily crowded out. It was crowded out today, and I would rather say so than fill
it. The one long-term thesis I worked properly — gold after the washout — failed its floor
by a factor of three (0.82 against 2.5), and I am not starting a second from scratch with
20 minutes left, because a long-term idea needs a defended valuation anchor *and* a priced
bear case and a rushed one is worse than none.
**Shortlist for tomorrow, framed by this regime** (rates higher for longer + Section 301 on
14 economies + AI capex doubt), none of them researched:
- **Insurance and brokers** — a hiking Fed raises investment income on float, and there is
  no financials exposure anywhere in the open book of 16. XLF is only -5.9% off its high and
  above its 50-day, so the lane is working without being crowded.
- **US domestic industrials with imported competition and domestic inputs** — the Section
  301 beneficiary that is not a levered commodity chemical. The screen to run is "names
  whose competitors are imported and whose inputs are not".
- **Semis after the carve-out is understood.** SMH is -37% and semiconductors are
  *explicitly excluded* from the Section 301 relief, so the complex has no policy put. That
  is a reason to wait, but it is also the only place a genuine long-term de-rating is on
  offer, and at some price it is the idea of the year rather than the trap of the month.
