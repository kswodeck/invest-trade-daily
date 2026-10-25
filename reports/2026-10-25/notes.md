# Research log — 2026-10-25

## [06:02 ET] SETUP
- Sunday run. US equities and futures cash closed; CME futures reopen 18:00 ET Sunday. Crypto 24/7.
- Per config/strategy.md weekend behavior: crypto + event contracts carry actionable ideas; equities are week-ahead prep, entries for Monday open, horizon=swing.
- Prior context: 20 open positions, 6 awaiting entry, 25 closed.
- **Track record is bad and the sample is now meaningful: 3/25 hit target (12%), avg -5.4%.**
  - stock: 1/17 (6%), avg -7.1% — the worst lane and the most used.
  - etf: 2/8 (25%), avg -1.8%.
  - conviction 2: 0/6, avg -8.4%. conviction 3: 1/15, avg -6.4%. conviction 4: 2/4, avg +2.7%.
  - n=25 closed is at the ~15 threshold, so this is no longer pure noise. Raising the bar today:
    new single-name equity longs need conviction >=3 with a dated catalyst, or they go to watchlist.
- Repetition warning: XLE 7x, ABT 7x, UNP 6x, PFE 5x, IYR 5x, GE 5x. Do not re-pitch without a change.

## [06:06 ET] MACRO — fetched
Sources: FRED via scripts/market_data.py macro; finnhub quotes. asof 2026-10-25T10:01Z.
- US10Y **4.96%** (2026-10-22), prior obs 5.13% — a 17bp drop. source: https://fred.stlouisfed.org/series/DGS10
- US2Y **4.65%** (2026-10-22), prior 4.81%. 10y-2y curve **+0.31** (10-23). https://fred.stlouisfed.org/series/T10Y2Y
- Fed funds effective **3.88%** — so the 10Y sits ~108bp ABOVE the policy rate. Steep. https://fred.stlouisfed.org/series/DFF
- Unemployment **4.2%** (Sept 2026), up from 4.1%. https://fred.stlouisfed.org/series/UNRATE
- CPIAUCSL Sept **336.298** vs Aug 334.131 = **+0.65% MoM**. Hot. https://fred.stlouisfed.org/series/CPIAUCSL
- Friday 2026-10-23 closes (finnhub, session=closed, age ~38h):
  SPY 759.97 (-0.52%), QQQ 704.40 (-0.01%), IWM 275.75 (-0.33%), TLT 81.34 (-0.49%),
  GLD 366.61 (-0.65%), SLV 48.72 (-1.26%), UUP 28.96 (+0.21%), XLF 55.90 (-1.32%)
  **USO 169.53 (+4.32%) and XLE 69.33 (+2.60%) — an oil spike on Friday. Needs a cause.**
- Crypto (coingecko, live): BTC **$80,255** (-0.38% 24h), ETH **$2,325.84** (-1.69%),
  SOL **$100.82** (-0.53%), XRP $1.29 (+1.28%), DOGE $0.0765, LINK $11.32, AVAX $8.80, LTC $56.14
  — crypto is in a deep drawdown; BTC 80k vs prior-cycle highs.
- FAILED sources this run: Yahoo returns HTTP 429 for every index symbol (^GSPC ^NDX ^DJI ^RUT ^VIX),
  so no VIX, no DXY, no index futures, no spot gold/WTI print. Finnhub refuses indices
  ("subscription required for CFD indices"). ETF proxies used instead and labelled as such.

## [06:10 ET] MACRO — the regime: a TIGHTENING Fed into a weakening labor market
This is the frame for everything today and it is not the usual one.
- **FOMC Wed 2026-10-28, 14:00 ET**, Chair **Kevin Warsh** presser. No new dot plot at this meeting.
  source: https://www.forbes.com/sites/simonmoore/2026/10/19/what-to-look-for-from-the-feds-october-meeting/
- Target range **3.75–4.00% following a September HIKE**. The Fed is tightening, not easing.
  source: https://www.chase.com/personal/investments/learning-and-insights/article/will-the-federal-reserve-hike-rates-at-october-2026-fomc-meeting
- Oct 28 pricing (as of 10-24): OIS ~**9.6% chance of a 25bp hike**, Kalshi ~**93% no change**,
  CME FedWatch ~80% hold. Consensus = hold with a tightening bias.
  sources: https://www.raisin.com/en-us/news/pre-fomc-preview-positioning-cash-october-2026/ ,
  https://kalshi.com/markets/kxfeddecision/fed-meeting/kxfeddecision-26oct
- **Markets firmly expect the next hike on Dec 9.** ~50bp of total hikes expected.
- PIMCO: hold at 3.75–4.00% while keeping a clear tightening bias.
  https://www.advisorperspectives.com/commentaries/2026/10/23/pause-still-recalibration
- Core PCE **3.0%** (Aug); Sept dot plot projects core PCE **3.4%** for 2026. CPI +0.65% MoM in Sept.
- **September payrolls +29,000.** Unemployment 4.2% and rising. NY Fed's Williams: "no need for urgency".
- Synthesis: inflation stuck near 3%+, labor market stalling, Fed still tightening. That is a
  stagflationary mix. It argues against duration longs, against rate-sensitive cyclicals and
  housing, and for real assets / energy / cash-generative value. It also explains the open book's
  IYR and ITB shorts and the TLT short.
- Note a dissonance worth watching: 10Y fell 4.96% from 5.24% two weeks ago (10-12 preview had
  S&P 7,811.54 and 10Y 5.24%) even with hot CPI — the bond market is pricing growth weakness
  over inflation. If FOMC is hawkish on Wednesday that move reverses.

## [06:13 ET] CALENDAR — earnings in the next 5 sessions (finnhub, fetched)
A very heavy week, and three of them land on open positions.
- **Mon 10-26**: VZ(bmo), NUE(amc), OKE(amc), SCCO, WHR(amc), WELL(amc)
- **Tue 10-27**: **FCX(bmo)** ←open position, **PYPL(bmo)** ←awaiting entry, BA(bmo), UPS(bmo),
  KO(bmo), V(amc), CNC(bmo), HCA(bmo), SHW(bmo), NXPI(amc), STX(amc), GLW(bmo), RCL(bmo), ITW(bmo)
- **Wed 10-28** (FOMC day, 14:00 ET): **GOOGL(amc)**, **MSFT(amc)**, F(amc), PSX(bmo), TMUS(amc),
  FDX(amc), GEV(bmo), NOW(amc), KLAC(amc), CMG(amc), BSX(bmo), VRT(bmo), DINO(bmo), CVNA(amc)
- **Thu 10-29**: **AMZN(amc)**, LLY(bmo), CAT(bmo), MRK(bmo), INTC(amc), **HII(bmo)** ←open position,
  MA(bmo), SBUX(amc), GILD(amc), LIN(bmo), DHI(bmo), PBF(bmo), LNG(bmo), MO(bmo), LHX(bmo), SYK(amc)
- **Fri 10-30**: **XOM(bmo)**, **CVX(bmo)** ←both drive the open XLE position, ABBV(bmo), REGN(bmo), CL(bmo)
Implication: MSFT+GOOGL on FOMC night and AMZN the next night means Wed-Thu carries both the
policy and the mega-cap-capex risk. Any index or tech idea this week is one bet, not three.
Also: the two homebuilder/housing shorts in the book (ITB, IYR) meet DHI earnings Thu 10-29 bmo.

## [06:18 ET] DATA QUALITY — no OHLCV history from the normal path
- `scripts/market_data.py history <SYM>` fails for every symbol: nasdaq empty, **yahoo HTTP 429**,
  stooq now behind a JS proof-of-work wall, twelvedata/alphavantage keys are present-but-empty
  (len 0) so the script correctly reports "no api key". Only FINNHUB (len 40) and FRED (len 32) work.
- finnhub `/stock/candle` returns "You don't have access to this resource" on this plan.
- Consequence: **ATR cannot be computed from the standard tooling this run.** Quotes still work
  (finnhub), so last price / open / high / low / prev_close are live and real.
- Working around it with a cookie-session Yahoo fetch at a slower cadence; anything it cannot
  return will be left without an ATR-derived stop rather than given a guessed one.

## [06:28 ET] EVENT CONTRACTS — Kalshi tooling is broken, prices fetched directly
- `scripts/market_data.py events "<anything>"` returns **count 0 for every query** — Fed, FOMC,
  CPI, inflation, Bitcoin, recession. The API itself is fine; Kalshi renamed its price fields to
  a `*_dollars` suffix (`yes_bid_dollars`, `last_price_dollars`, `open_interest_fp`) and the
  script still reads `yes_bid`/`last_price`, so every market parses as priceless and is dropped.
  **This is a real tooling bug, not an outage** — worth a fix outside this run.
- Fetched directly from https://api.elections.kalshi.com/trade-api/v2/markets

**KXFEDDECISION-26OCT** (resolves 2026-10-28 14:00 ET, close 17:59Z):
  - H0 "Fed maintains rate": yes 0.93/0.94, last 0.94, OI 2,995,965 — deep and liquid
  - H25 "Hike 25bps": yes 0.05/0.06, last 0.06, OI 2,287,107
  - C25 / C26 / H26: 0.00/0.01 — effectively zero
**KXFEDDECISION-26DEC** (resolves 2026-12-09):
  - **H25 "Hike 25bps": yes 0.73/0.74, last 0.74** — the market prices a December hike at ~74%
  - H0 "maintains": yes 0.23/0.24. H26 ">25bps": 0.03/0.05

## [06:30 ET] CPI — the actual numbers, computed from FRED CPIAUCSL
https://fred.stlouisfed.org/series/CPIAUCSL (seasonally adjusted index)
  2026-06 3.46% YoY | 2026-07 3.30% | 2026-08 3.35% | **2026-09 3.72%**
Sept MoM +0.65%. **YoY jumped 37bp in one month** — that is a genuine re-acceleration, not noise,
and it is the strongest argument for the December hike the market already prices at 74%.
Caveat: CPIAUCSL is seasonally adjusted; Kalshi's KXCPIYOY settles on NSA CPI, so these are
close but not the same series. Do not trade a Kalshi CPI strike off this number without pulling
CPIAUCNS first.

## [06:31 ET] REJECTED — KXFEDDECISION-26OCT — no probability disagreement, bad payoff
Market: 94% hold. My estimate: ~93-95% hold. PIMCO, Williams ("no need for urgency"), no dot
plot at this meeting, +29k Sept payrolls — everything points the same way the market already
points. Buying YES at 0.94 risks 94c to make 6c over three days on a view I do not hold more
strongly than the crowd does. **No edge, no trade.** This is the disciplined answer, not a gap.

## [06:11 ET] TIMESTAMP CORRECTION
The [06:02]-[06:31] stamps above were estimated, not read from the clock, and ran ahead of
real time — `date` says 06:11 ET here. Everything above was gathered between 06:01 and 06:11 ET.
Findings and prices are unaffected; only the stamps were wrong. Clock-read from here on.

## [06:12 ET] POSITION UPDATE — TLT — short opened 2026-09-24 @ 79.90, now 81.34 (-1.8%)
- decision: **HOLD, stop unchanged at 82.00, do not add.**
- why: thesis strengthened — Sept CPI 3.72% YoY vs 3.35% Aug, Fed hiked in Sept, range now
  3.75-4.00%, Kalshi prices a 74% Dec hike. Only 0.8% from the stop, but 82.00 IS the
  invalidation and widening it to survive Wednesday is the error this repo already paid for.
- action: captured via add_candidate.py, conviction 4.

## [06:15 ET] LEVELS — ATR recovered via a working source (Nasdaq), tooling bug noted
`_bars_nasdaq` in market_data.py reports "no rows" for every symbol, but
`https://api.nasdaq.com/api/quote/<SYM>/historical?assetclass=stocks|etf&fromdate=&todate=`
returns full daily OHLCV when sent a browser User-Agent and `Accept: application/json`.
The script's nasdaq path is a **second real tooling bug** alongside the Kalshi field rename.
All ATRs below are 14-day, computed from those bars, closes through 2026-10-23.

| Sym | ATR14 | ATR% | SMA20 | SMA50 | SMA200 | lo20 | hi20 | ADV20 $ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TLT  | 0.828 | 1.02 | 78.77 | 80.55 | 83.43 | 76.43 | 81.92 | 3.97B |
| CEG  | 15.87 | 6.26 | 273.16 | 274.20 | 274.48 | 247.20 | 309.80 | 1.08B |
| FCX  | 2.521 | 3.87 | 70.41 | 71.89 | 66.86 | 64.00 | 74.45 | 734M |
| XLE  | 1.473 | 2.12 | 65.40 | 64.34 | 59.78 | 60.95 | 69.72 | 2.22B |
| HII  | 6.990 | 2.55 | 267.09 | 280.07 | 304.67 | 255.35 | 280.42 | 153M |
| SMMT | 0.887 | 5.73 | 16.29 | 15.79 | 16.24 | 14.56 | 19.09 | 109M |
| ITB  | 2.436 | 2.69 | 86.59 | 90.38 | 94.11 | 82.08 | 91.34 | 295M |
| IYR  | 1.490 | 1.51 | 96.14 | 99.44 | 101.61 | 93.29 | 99.74 | 616M |
| DG   | 4.477 | 3.37 | 127.09 | 125.63 | 119.64 | 117.31 | 139.12 | 274M |
| STLD | 7.695 | 3.19 | 237.04 | 237.40 | 239.23 | 219.10 | 248.96 | 232M |
| LULU | 3.778 | 3.82 | 96.32 | 104.24 | 119.13 | 90.38 | 104.16 | 421M |
| NKE  | 1.043 | 2.80 | 35.88 | 37.17 | 41.23 | 31.97 | 38.44 | 1.59B |
| XLF  | 0.714 | 1.28 | 54.69 | 56.08 | 54.56 | 52.81 | 56.67 | 2.03B |
| UNP  | 5.566 | 1.90 | 281.88 | 287.43 | 278.61 | 268.68 | 299.38 | 721M |
| PYPL | 1.053 | 1.85 | 55.43 | 55.85 | 51.16 | 52.30 | 57.95 | 596M |
Crypto daily ATR14 (CoinGecko 4h bars aggregated to daily, 2026-09-25 -> 10-25):
| BTC | 2051.71 | 2.55% | 30d range 79,263 - 87,086 |
| ETH | 91.44 | 3.90% | 30d range 2,286.76 - 2,768.44 |
| SOL | 4.40 | 4.33% | 30d range 98.81 - 124.77 |

### Stop distance audit of the live book, in ATRs from the ENTRY
Floors: stock 2.0, etf 1.8, crypto/futures 2.5 (swing).
- TLT  2.10/0.828 = **2.54 ATR** — clears 1.8. Stop 82.00 also sits just above the 81.92 20-day high. Well placed.
- CEG  22.0/15.87 = **1.39 ATR — FAILS the 2.0 stock floor.** Never was a valid stop.
- FCX  5.10/2.521 = **2.02 ATR** — just clears.
- XLE  3.10/1.473 = **2.10 ATR** — clears 1.8.
- SMMT 2.70/0.887 = **3.04 ATR** — clears.
- STLD 16.75/7.695 = **2.18 ATR** — clears.
- DG   8.90/4.477 = **1.99 ATR** — at the floor.
- UNP  11.20/5.566 = **2.01 ATR** — at the floor.
- XLF  1.43/0.714 = **2.00 ATR** — clears 1.8.
- LULU 11.39/3.778 = **3.01 ATR** — clears.
- NKE  2.60/1.043 = **2.49 ATR** — clears.
- ITB  3.80/2.436 = **1.56 ATR — FAILS the 1.8 etf floor.**
- IYR  2.60/1.490 = **1.74 ATR — FAILS the 1.8 etf floor**, marginally.
Three legacy stops (CEG, ITB, IYR) are tighter than the floor the strategy now demands. They
cannot be widened after the fact — that is the KRE error — so the answer for each is either
hold and accept a noise stop-out, or close. Taken case by case below.

## [06:18 ET] POSITION UPDATES captured so far
- **TLT** short 79.90 -> 81.34 (-1.8%): HOLD, stop 82.00 unchanged, no add. Stop is 2.54 ATR
  and sits just above the 81.92 20-day high. FOMC Wed resolves it.
- **CEG** long 272.00 -> 253.45 (-6.8%): **CLOSE at Monday open.** Stop 250.00 is 1.39 ATR on a
  6.26%-ATR name and spot is 1.4% from it; 2026 guidance $11.00-12.00 vs $11.72 consensus, no new
  datacenter deals at the October update, MS target 360 from 385. Google 890MW deal still stands,
  so this is an exit on geometry + guidance, not a reversal.
- **XLE** long 63.90 -> 69.33 (+8.5%): **TAKE PROFIT.** Half at Monday open, limit the rest 70.50,
  flat before XOM+CVX Friday pre-open. Spot is at 69.72, the high of all 139 bars fetched.
- **FCX** long 68.20 -> 65.18 (-4.4%): **REDUCE to half** before Tue pre-open earnings. Stop 63.10
  is 2.02 ATR from entry but only 0.83 ATR from spot, directly in front of a gap event.
  Sell-side flat into the print (Oct 5/18/6/0/1 vs Aug 5/19/5/0/1).

## [06:18 ET] NEWS — CEG, the cause of the October breakdown
- 2026 adjusted operating EPS guidance initiated **$11.00-12.00 vs $11.72 consensus**; Calpine
  integration cost cited. Morgan Stanley cut target to **$360 from $385**, kept buy.
  No new datacenter contracts announced at the October investor update.
  ~31% below the 52-week high of $412.70 (2025-10-15). IPPs hit harder than regulated utilities.
  sources: https://www.trefis.com/stock/ceg/articles/619625/should-you-buy-the-dip-in-constellation-energy-stock/2026-10-21
           https://weissratings.com/en/instant-news-alerts/constellation-energy-corporation-ceg-down-4-9-time-to-get-out-while-ahead
- Still in force: 2026-10-06 Google agreement, 890MW additional nuclear output over 20 years.

## [06:19 ET] ANALYSTS (finnhub recommendation trend, read as the CHANGE not the level)
- FCX: Oct 5/18/6/0/1, Sep 5/19/5/0/1, Aug 5/19/5/0/1 — flat, one buy drifting to hold. Neutral.
- PYPL: Oct 4/10/34/3/0, Sep 4/10/35/3/0, Aug 4/11/34/3/0 — **34 of 51 are holds.** The street has
  no conviction either way; this is a show-me name into Tuesday's print.

## [06:21 ET] EVENT CONTRACTS — prices fetched, and why only one is tradeable
**KXU3-26OCT** (October unemployment rate, released 2026-11-06):
  T4.0 yes 0.94/0.95 | **T4.1 yes 0.68/0.71** | **T4.2 yes 0.31/0.34** | T4.3 yes 0.05/0.06
  September U3 printed 4.2%, so "Above 4.2%" = the market pricing 31-34% that October rises to 4.3%+.
**KXU3-26NOV** (released 2026-12-04): T4.0 0.75/0.76 | T4.1 0.46/0.54 | T4.2 0.15/0.17 | T4.3 0.08/0.09
**KXCPIYOY-26OCT**: no such event returned — the series exists but not for an October resolution.

## [06:22 ET] REJECTED — KXU3-26OCT-T4.2 — right idea, untradeable market
I do have a view here: +29k September payrolls is far below the pace that holds the rate flat,
and 4.1% -> 4.2% is the trend. I would put October at 4.3%+ nearer 40% than 34%. But:
- **24-hour volume is 0.00** on the T4.2 strike, and 0.00 on every KXU3-26OCT strike except
  T4.0 (10.00), T4.3 (29.00) and T4.4 (33.00). Open interest 5,573 contracts.
- The spread is 0.31/0.34 — 3 cents wide on a 32-cent contract, ~9%, which eats most of the
  claimed edge before the position exists.
A 6-point probability edge inside a 9% spread on a market that did not trade yesterday is not an
edge. **No trade.** Same conclusion for the November strikes, which are thinner still.

## [06:22 ET] REJECTED — KXFEDDECISION-26DEC-H25 @ 0.73/0.74 — no disagreement
The December hike at 74% is the liquid one (OI 154,476). CPI re-accelerating to 3.72% argues
for it; +29k payrolls and two more CPI and jobs reports before 2026-12-09 argue against. My own
estimate lands 72-78%, straddling the price. Buying at 0.74 to make 0.26 needs a confidence
I do not have. **The event-contract lane produced no trade today, and that is the finding** —
the liquid markets are efficiently priced and the mispriced ones do not trade.

## [06:23 ET] POSITION UPDATE — PYPL — awaiting entry @ 56.50, spot 57.02, 3rd publication
- decision: **level unchanged, order SUSPENDED until after Tuesday pre-open earnings.**
- why: a 0.9% pullback entry is a reflex discount, not a level — it has failed to fill three
  times because the only thing that fills it is bad news arriving first. Earnings Tue resolves it.
- stop set at 54.35 = 2.04 ATR below entry, under the 55.85 fifty-day. R:R (61.00-56.50)/2.15 = 2.09.
- action: captured.

## [06:23 ET] POSITION UPDATE — HII — long 262.00 -> 274.08 (+4.6%)
- decision: HOLD through Thursday pre-open earnings, no add before it, no add above 268.00.
- why: long_term, no stop by design, bear case 230. Insider record is a genuine negative —
  0 open-market buys in 6 months against 3 sales totalling $5.6M — so conviction stays 3.

## [06:27 ET] ** BOOK-LEVEL RISK — four live positions are the same bet **
This is the most important thing in today's notes and it is not visible from any single row.
Short TLT (duration), short ITB (homebuilders), short IYR (REITs) and the new conditional
short /MBTZ6 all pay off in the same state of the world: rates up, or at least not down.
strategy.md caps correlated ideas at **3 on one driver**; the live book plus today's addition
is **4**. Every one of them is hurt by the same event — a dovish FOMC on Wednesday 2026-10-28.
- The three live ETF/duration shorts cannot be unwound by this report without closing positions
  it otherwise wants to keep, so the honest mitigation is sizing, not cancellation.
- **The /MBTZ6 trigger should be taken at 1% rather than 1.5% if TLT and ITB are both still open
  when it fires**, and that instruction is written into the candidate's key_risk.
- Synthesis and the red team should treat this as a standing flag, not a per-idea one.

## [06:28 ET] REMAINING OPEN POSITIONS — reviewed, no change, deliberately not re-pitched
Twelve positions were checked against fresh quotes, fresh 14-day ATR and the fetched earnings
calendar. **None has a new dated catalyst inside the next five sessions and none has a stop
problem**, so all are unchanged holds. They are NOT captured as candidates, on purpose: prior
context flags XLE 7x, ABT 7x, UNP 6x and PFE 5x in ten days, and republishing an unchanged hold
over a weekend when no market traded is the anchoring behaviour that warning is about.
| Sym | side | entry | spot | stop | stop ATRs from entry | read |
| BCC  | buy  | 76.50  | 77.74  | none   | n/a  | long_term, +1.6%. ADV only $24.9M — thinnest name in the book. |
| PFE  | buy  | 27.60  | 30.03  | none   | n/a  | +8.8%, spot at the 30.44 139-bar high. No add. Earnings 11-03. |
| DG   | buy  | 134.50 | 132.69 | 125.60 | 1.99 | fell 4.6% Friday; no dated cause found, best available explanation is an overbought pullback after a 21.5% three-month rally. Spot still above SMA20/50/200. |
| IYR  | short| 97.80  | 98.40  | 100.40 | 1.74 | stop just under the 1.8 ETF floor; below SMA50 99.44 and SMA200 101.61. Same driver as ITB — see correlation flag above. |
| LULU | sell | 100.61 | 99.01  | 112.00 | 3.01 | +1.6% in favour. SMA50 104.24 remains the cover line. |
| NKE  | sell | 38.40  | 37.30  | 41.00  | 2.49 | +2.9% in favour. Spot 0.13 above the 37.17 fifty-day — live. |
| KHC  | buy  | 23.00  | 24.80  | 21.20  | 2.80 | +7.8%. Earnings 11-04, outside this week. |
| XLF  | buy  | 54.23  | 55.90  | 52.80  | 2.00 | +3.1%. Fell 1.32% Friday on the risk-off day. |
| SMMT | buy  | 17.10  | 15.47  | 14.40  | 3.04 | worst open position at -9.5%, but the stop is honest at 3.04 ATR and 1.2 ATR below spot. Biotech, 5.73% ATR, ADV $109M. Hold. |
| UNP  | buy  | 288.60 | 292.87 | 277.40 | 2.01 | +1.5%. |
| ABT  | buy  | 103.00 | 103.70 | 97.00  | 2.05 | +0.7%, below the 105.17 fifty-day. |
| CVS  | buy  | 93.00  | 93.47  | 85.40  | 3.36 | +0.5%, right at the 93.74 two-hundred-day. Earnings 11-04. |

## [06:29 ET] REMAINING AWAITING-ENTRY — two cancelled, three left standing
- `OXY` BUY @ 54.00 — **CANCELLED** (captured). Spot 64.17, the 139-bar high; order 6.4 ATR below market.
- `GLD` SELL @ 406.77 — **CANCELLED** (captured). Spot 366.61; the call was right by 9.9% and
  earned nothing because the level was never reachable. Order now 7.5 ATR above market.
- `VST` BUY @ 132.00 (2026-08-24) — left standing. Spot 140.16, 6.2% above the order, same IPP
  group as the CEG position being closed today. Flagged for tomorrow: if CEG's guidance problem
  is sector-wide this order should go too, but I did not get to VST's own numbers this run.
- `AAL` SELL_SHORT @ 13.35 (2026-10-03) — left standing. Spot 12.11, already 9.3% below the
  order, so like GLD the move happened without the fill. Probably a cancel; not checked properly.
- `KXCPIYOY-26SEP-T3.5` NO @ 18 (2026-09-30) — September CPI YoY computed at 3.72% on the
  seasonally adjusted series, i.e. above 3.5%, so a NO leg would have lost had it filled. The
  September event has resolved; this row should be retired as expired, not carried.

## [06:29 ET] REJECTED — this run, with reasons
- `KXFEDDECISION-26OCT` — 94% hold is my number too. No disagreement, and risking 94c to make 6c.
- `KXFEDDECISION-26DEC-H25` @ 0.74 — my estimate 72-78% straddles the price. No edge.
- `KXU3-26OCT-T4.2` @ 0.31/0.34 — I think it is closer to 40%, but 24h volume is 0.00 and the
  spread is 9% of the contract. The edge is smaller than the cost of expressing it.
- `BTC spot long` — the 6-month base at 62.8k-87.1k is real, but buying a non-yielding asset
  while the Fed is still raising into 3.72% inflation has no catalyst. Routed to a conditional
  SHORT trigger instead, since Robinhood Crypto cannot short and /MBT can.
- `Refiners into the crude spike` (PSX/DINO Wed, PBF Thu) — genuinely interesting, since Friday's
  4.32% USO move compresses cracks into three refinery prints this week. **Not researched** — I
  ran out of budget before pulling margin data, and an untested idea is not a candidate.
- `New single-name equity longs generally` — bar deliberately raised today. The closed record is
  stock 1/17 (6%), avg -7.1%, and conviction 3 is 1/15. On a Sunday with no tape and no new
  information, adding fresh single-name longs would be padding.

## [06:31 ET] AWAITING-ENTRY — the two I had left unchecked are now decided
Supersedes the "left standing / not checked properly" lines in the 06:29 block.
- **`VST` BUY @ 132.00 — CANCEL (captured).** Spot 140.16, ATR 9.93 (7.08%), below SMA20 150.12,
  SMA50 145.19 and SMA200 151.14, 139-bar range 132.66-171.35. The order sits *below the low of
  the entire window*, so it fills on an IPP breakdown — the same sector event that is closing CEG
  today. Guidance itself was reaffirmed at $6.8-7.6B adj. EBITDA, but $723M of $1.494B adj. EBITDA
  in the cited quarter was unrealised hedge gains, which is not the earnings quality that earns an
  automatic bid under support. source: https://www.tikr.com/blog/vistra-stock-fell-5-in-a-broad-power-selloff-heres-where-the-stock-could-go
- **`AAL` SELL_SHORT @ 13.35 — KEEP, unchanged (captured).** Spot 12.11, below SMA20 12.63,
  SMA50 13.11, SMA200 13.90; range 10.91-18.79. This is the opposite case to OXY/GLD: the order
  is *above* the market on a short, so it fills on a bounce into the 50/200-day cluster while the
  thesis is intact, rather than only once the thesis has failed. That distinction is the rule I
  used for all five pending orders today.

## [06:32 ET] SELF-CHECK — recomputed every captured candidate's arithmetic
Caught and fixed two of my own errors before they reached synthesis:
1. **GLD was captured with the stop at 377.50 — BELOW the entry on a short**, which is not a stop.
   Re-captured with the stop at 416.36 (1.8 ATR above the 406.77 entry).
2. **GLD then read as a 40% shot at 5.4:1** against a 15.6% break-even — a +24pt edge claim I do
   not hold. That ratio is an artifact of an entry stranded 11% above spot, not an edge.
   win_probability lowered to 0.20 and the artifact spelled out in key_risk.
Remaining flags, all intentional and disclosed in the candidates themselves:
- **CEG 1.39 ATR, ITA 1.69 ATR, ITB 1.56 ATR** stops are under the floor. For CEG and ITA the
  failing stop *is* the reason for the close; for ITB it is disclosed and the stop left alone.
  None was widened. If 2d enforcement demotes these three, the close/hold instruction must still
  reach the reader — they are decisions on live positions, not new entries.
- **XLE win_probability 0.60 vs a 31.9% break-even** is a deliberate +28pt claim and the one
  number in this run that most deserves challenge. The justification: the baseline is computed
  from the 63.90 entry, but the position is already at 69.33 with the 70.50 target 0.79 ATR above
  spot and the 60.80 stop 5.79 ATR below it. Reaching the target before the stop *from here* is
  genuinely far likelier than 32%. The claim is about a position 85% of the way home, not a new entry.

## [06:33 ET] RESEARCH COMPLETE
- candidates: **16 captured, 14 unique symbols** (GLD captured three times; synthesis takes the last).
  Breakdown: 9 decisions on live positions (TLT hold, CEG close, XLE take-profit, FCX halve,
  HII hold, ITB hold, STLD hold, ITA close, plus the book-level correlation flag), 5 decisions on
  resting orders (OXY/GLD/VST cancel, AAL keep, PYPL suspend), 1 genuinely new idea (/MBTZ6
  conditional short), and 12 live positions reviewed and deliberately left unchanged.
- **This is a Sunday run and reads like one.** US equities and futures were shut all session;
  every equity price is the 2026-10-23 16:00 ET close, ~38 hours old, and labelled as such on each
  candidate. Only crypto prices are live. Per config/strategy.md weekend behaviour, equities here
  are week-ahead preparation with entries for Monday's open, not same-day calls.
- **Only one new idea was added on purpose.** The closed record is 3/25 at target (12%), avg -5.4%,
  with single-name stocks at 1/17 (6%) and avg -7.1%. n=25 is past the ~15 threshold where the
  strategy says to stop calling it noise, so the bar for new single-name longs was raised and
  nothing cleared it on a day with no tape and no new information. Six good ideas beats twenty,
  and today the honest number was smaller still.
- coverage gaps:
  - **Refiners into Friday's crude spike** (PSX and DINO report Wed 10-28, PBF Thu 10-29) — the
    most promising unexplored thread. USO +4.32% compresses crack spreads into three prints. Not
    researched; no margin data pulled. Deliberately not captured rather than guessed.
  - **No cause established for Friday's 4.32% oil move.** Searched and found nothing dated to
    2026-10-23. Two recommendations (XLE take-profit, OXY cancel) explicitly rest on *not*
    extrapolating an unexplained gap, so this gap is load-bearing and should be re-checked Monday.
  - **No cause established for DG -4.6% on Friday.** Best available explanation is an overbought
    pullback after a 21.5% three-month rally; the article matching that description is undated,
    so it is not relied on.
  - GOOGL, MSFT, AMZN, INTC, CAT, LLY and the rest of the mega-cap week were not researched as
    ideas at all. With FOMC Wednesday 14:00 ET and MSFT+GOOGL that same evening, any index or
    mega-cap tech idea this week is one bet rather than several, and there was no budget to do
    it properly.
  - BCC's $24.9M average dollar volume is the thinnest in the book and was not examined.
- sources that failed, and two are real bugs worth fixing outside this run:
  - **`market_data.py events` returns count 0 for every query.** Kalshi renamed its price fields
    to a `*_dollars` suffix; the script still reads `yes_bid`/`last_price`. The API is healthy —
    all event prices in these notes were fetched directly. **This silently zeroed an entire
    asset class**, and the report would have read "no event contracts available" when in fact the
    Fed decision market has 3.0M contracts of open interest.
  - **`market_data.py history` fails for every symbol**, so no ATR from the standard path:
    nasdaq "no rows", yahoo HTTP 429 throughout, stooq now behind a JS proof-of-work wall,
    twelvedata and alphavantage keys present but empty (len 0). `_bars_nasdaq` is the bug —
    api.nasdaq.com returns full daily OHLCV given a browser User-Agent and `Accept:
    application/json`, which is how every ATR in this run was computed.
  - finnhub `/stock/candle` is not on this plan ("You don't have access to this resource").
  - Index quotes unavailable all run: finnhub refuses indices, yahoo 429. No VIX, no DXY, no spot
    WTI, no index futures. ETF proxies used throughout and labelled as proxies.
  - `market_data.py short PYPL` timed out against api.nasdaq.com; no short-interest data this run.
  - robinhood.com futures product page returns HTTP 404. Micro BTC availability confirmed instead
    via a Nasdaq article on Robinhood launching micro BTC/SOL/XRP futures, and the CME listing
    cycle of six consecutive monthly contracts — hence /MBTZ6 (December) rather than the October
    contract, which expires 2026-10-30.

## [06:34 ET] REFINERS — gap closed. No candidate, but it corroborates two calls already made.
I flagged this as the most promising unexplored thread at 06:33 and went back for it.
**Crack spreads are at records.** The 3-2-1 crack spread's 200-day average reached ~$43.62 on
2026-08-25, the highest reading in the series back to June 2006, with the daily spread at $65.82.
Diesel cracks are at records on Middle East and Ukraine conflict disruption, and analysts expect
VLO, MPC and PSX to post Q3 profits well above their near-record Q2.
sources: https://www.thetrading.tools/chart-of-the-day/2026-08-31-refining-margins-record
         https://investinglive.com/commodities/us-refiners-set-for-windfall-q3-profits-as-wars-push-diesel-margins-to-records/

Levels (Nasdaq daily bars through 2026-10-23), and the point is how extended the group is:
| Sym | spot | SMA20 | SMA50 | SMA200 | vs SMA200 | hi(139 bars) | ATR% | reports |
| PBF  | 76.17  | 82.62  | 77.09  | 58.65  | **+30%** | 92.46  | 6.20 | Thu 10-29 bmo |
| DINO | 121.66 | 119.04 | 109.74 | 86.31  | **+41%** | 129.37 | 3.47 | Wed 10-28 bmo |
| PSX  | 283.18 | 277.71 | 262.50 | 211.38 | **+34%** | 299.39 | 3.13 | Wed 10-28 bmo |
| VLO  | 419.28 | 425.50 | 392.41 | 311.01 | **+35%** | 461.52 | 4.07 | — |
| MPC  | 457.22 | 447.74 | 409.30 | 317.68 | **+44%** | 493.98 | 3.64 | — |

**No candidate, and the reason is the setup rather than the data.** This is record margins, fully
expected, into shares already 30-44% above their 200-day. Buying that is paying for news already
in the price; shorting it is fading a momentum group into prints consensus expects to be blowouts.
Neither is an edge, and the identified downside catalyst is not something I can handicap — the
same reporting notes refiner shares are "exposed to any de-escalation in the Iran conflict or a
reopening of Hormuz, either of which could compress margins quickly."

**Two things it does settle, though:**
1. **A likely cause for Friday's unexplained 4.32% USO move: Middle East supply disruption.**
   This is consistent with the conflict-driven crack-spread story, but I could find nothing dated
   to 2026-10-23 itself, so it stays a hypothesis. It does *not* upgrade the XLE or OXY calls.
2. **It strengthens both energy calls made today rather than contradicting them.** Taking XLE
   profit at 69.33 and cancelling the OXY bid are the right side of a complex priced for records
   with a binary de-escalation risk attached. Energy exposure should be coming down here, not up.

**Watchlist for tomorrow, explicitly not a candidate today:** PBF is the divergence in the group —
the only refiner trading *below* its 20-day (76.17 vs 82.62), 17.6% off a 92.46 high while DINO,
PSX, MPC and VLO sit at or near theirs, and it reports Thursday pre-open on a 6.2% ATR with a
$10.55 consensus EPS. Either the market knows something company-specific or it is the cheap way
into the same margin story. **I did not establish which, so it is not a recommendation** — it is
the first thing to pick up on Monday with a live tape.

## [06:35 ET] SELF-CHECK 2 — conviction scores were systematically one too LOW
Recomputed every candidate's conviction as the count of distinct `evidence` kinds, per the table
in config/strategy.md (1 kind = 2, 2 kinds = 3, 3 kinds = 4, 4+ = 5). **Eleven of fourteen were
scored one below what their own evidence supports.** Corrected by re-capturing each.
This matters in the direction people do not usually check. The known failure mode in this repo is
inflation — 39 of the first 57 ideas scored 3. I over-corrected into the opposite error, scoring
by feel and landing low: HII was held at 3 because the insider record is unhelpful, which is
exactly the "conviction as a feeling" the rule forbids. Evidence quality and expected return are
different axes, and an unhelpful insider record belongs in `counter_argument`, where it is,
not in the score. Under-scoring corrupts the by-conviction performance table just as surely as
inflation does, and it is harder to spot because it looks like modesty.
Final scores: XLE 5, ITB 5; CEG/FCX/HII/PYPL/ITA/GLD/VST//MBTZ6 4; TLT 4; STLD/AAL/OXY 3.

## [06:35 ET] CORRECTION to the 06:33 coverage-gap list
"Refiners into Friday's crude spike" is **no longer a gap** — it was researched at 06:34 above and
deliberately produced no candidate, which is a different and better outcome than an unexamined
thread. The remaining gaps in that block stand as written.

## [06:36 ET] FINAL STATE — and one caveat the red team should weigh
candidates.jsonl: **27 lines, 14 unique symbols** (re-captures supersede; synthesis takes the last
per symbol). No conviction mismatches, every candidate carries thesis, key_risk, counter_argument
and sources. Distribution: conviction 5 x2, 4 x9, 3 x3; swing 13, long_term 1; stock 8, etf 5,
futures 1; no event contracts and no crypto spot, for the reasons recorded above.

**Caveat on that distribution.** Nine fours and two fives is a high-conviction-looking book, and
it is the mechanical result of the counting rule rather than a claim that today's ideas are
unusually strong. Most of these rows are decisions about positions that already exist, and for
those the three evidence kinds come cheaply: a fetched earnings date, an ATR computed from real
bars, and a measured positioning read are all genuinely present, but they are easier to assemble
for a hold-or-close call than for a new thesis. The scores are honest by the stated rule; whether
a conviction-4 *cancellation* means the same thing as a conviction-4 *new idea* is a question the
rule does not answer, and the red team should feel free to lower rather than treat the count as
settled. Only one row here — /MBTZ6 — is a new idea in the ordinary sense, and it is gated on a
trigger that has not fired.
