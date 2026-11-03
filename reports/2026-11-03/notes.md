# Research log — 2026-11-03

## [06:01 ET] SETUP
- Tue 2026-11-03, pre-market. Last equity close = Mon 2026-11-02.
- Prior context read: 14 open positions, 8 awaiting entry, 32 closed.
- **Track record is bad and it must raise the bar: 3/32 hit target (9%), avg -5.7%.**
  n=32 is above the ~15 noise threshold overall, so this is a real signal, not a bad week.
  stock 1/21 (5%), avg -7.6%; etf 2/11 (18%), avg -2.2%. long_term 0/4, avg -15.2%.
  Conviction 4 is the only tier with a positive-ish record (2/7, avg -0.5%).
  => Today: fewer ideas, higher evidence bar, prefer ETFs over single stocks where the
  view is sectoral, and be very reluctant to publish conviction-2/3 single-stock swings.

## [06:05 ET] OPEN POSITION PRICES — pre-market 2026-11-03 (market_data.py quote, session=pre)
| Sym | entry | stop | target | pre-mkt | vs entry |
| XLE | 63.9 | 60.8 | 70.5 | 67.25 | +5.2% |
| BCC | 76.5 | none | 110.0 | 75.00 | -2.0% |
| PFE | 27.6 | none | 42.0 | 30.67 | +11.1% |
| IYR (short) | 97.8 | 100.6 | 90.5 | 100.90 | -3.2% (ABOVE STOP) |
| LULU (sell) | 100.61 | 112.0 | 77.0 | 107.83 | -7.2% |
| NKE (sell) | 38.4 | 41.0 | 32.1 | 39.12 | -1.9% |
| KHC | 23.0 | 21.2 | 28.09 | 24.93 | +8.4% |
| XLF | 54.23 | 52.8 | 57.6 | 57.56 | +6.1% (AT TARGET) |
| STLD | 245.5 | 228.75 | 281.0 | 251.91 | +2.6% |
| HII | 262.0 | none | 339.76 | 313.70 | +19.7% |
| UNP | 288.6 | 277.4 | 315.99 | 307.00 | +6.4% |
| ABT | 103.0 | 97.0 | 117.34 | 110.16 | +6.9% |
| CVS | 93.0 | 85.4 | 110.68 | 88.51 | -4.8% |
| PYPL | 56.5 | 54.1 | 62.7 | 58.78 | +4.0% |
- XLE -3.96% and BCC -4.86% on the session vs prior-context last price: energy and
  building products both sold off Monday. Needs a reason — checking news.
- IYR short is through its 100.6 stop on pre-market quote. Must be addressed.
- XLF is at/through its 57.6 target.

## [06:06 ET] CALENDAR — earnings (finnhub via market_data.py earnings --days 12)
- **Data gap: the feed returns nothing dated 2026-11-03 or 2026-11-04.** First dated
  entries are 2026-11-05 (179) and 2026-11-06 (65). So today's and tomorrow's reporters
  are NOT visible to this source. Any "reports today" claim would be unsourced — not made.
- Nov 5 bmo: CI, CAH, COP, ARW, CMI, DUK, BDX, AAP, EPAM, CELH, BSY
- Nov 5 amc: EOG, DVN, ED, ABNB, AEE, DKNG, AFRM, AKAM, ARM, CENX, DBX, BILL, DIOD
- Nov 6 bmo: HUM, CHTR, PAGP, **VST**, FLR, DK, PPL, BIP, BEN, BAM, UAA, **ELAN**, MRNA, SLVM, STWD
- VST reports 2026-11-06 bmo and VST is already on the awaiting-entry list @132 — a real
  dated catalyst for a level already published.
- ELAN reports 2026-11-06 bmo; ELAN was captured in the 2026-11-02 run.

## [06:06 ET] MACRO — Monday 2026-11-02 close (prices from market_data.py quote/history, session = prior close)
- `market_data.py macro` **FAILED** — timed out twice at 120s/180s with zero output
  (exit 143). No FRED/VIX/DXY figures from the CLI this run. Macro reconstructed from
  ETF proxies + web. Record as a data gap.
- SPY 752.10 (-0.48%) | QQQ 681.09 (-1.36%) | IWM 279.14 (-0.07%) | TLT 81.73 (-0.13%)
- GLD 361.65 (+1.65%) | USO 156.87 (**-7.08%**) | UUP 28.96 (-0.14%)
- Sectors: XLE 67.25 (**-3.96%**) | XLK 174.22 (**-2.95%**) | XLP 90.83 (+1.58%)
  | XLU 43.67 (+0.55%) | XLV 184.60 (-0.15%) | XLF 57.56 (+1.86%)
- Index closes: Dow 51,983.98 (+0.41%), S&P 500 7,541.40 (-0.51%), Nasdaq Comp
  25,164.32 (-1.07%). 7 of 11 S&P sectors green; energy -3.97% and tech -2.66% the
  laggards — source: https://english.news.cn/20261103/ad0fc40ddfe343ab80c64d24566dedcb/c.html
- **THE OIL EVENT.** WTI settled $96.46, -7.4%, biggest daily loss since 27 July;
  Brent $104.77, -7.6%. Driver: US and Iranian officials both signalled they will
  pursue diplomacy, deflating the war premium built through October over an
  eight-month West Asia conflict. No concrete agreement yet — this is a signal, not
  a deal. source: https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Plunge-7-as-US-and-Iran-Signal-Room-for-Diplomacy.html
  and https://www.ebc.com/forex/oil-prices-biggest-drop-since-july-2026
- Note the absolute level: WTI near $96 even AFTER a 7.4% crash. The war premium is
  deflating from a very high base, not from normal.
- **MIDTERM ELECTIONS ARE TODAY, Tue 2026-11-03**, plus a jobs report this week —
  traders were positioning for both on Monday. source: the Xinhua close report above.
- Single-name tech damage: ORCL -8.6% on a plan to raise $20B in shares and bonds;
  MRVL -13% on a $115B agreement to buy Lumentum (LITE -18%).
  source: https://www.stocktitan.net/articles/stock-market-today-live-november-2-2026
- Regime read: this is not a broad risk-off. It is (a) a war-premium unwind in energy,
  (b) an AI-capex/financing scare in tech, (c) money moving into staples, utilities,
  gold, financials and cyclicals. XLP closed 90.83 against a 120d high of 90.99.

## [06:07 ET] CALENDAR — this week's dated macro
- **Tue 2026-11-03 (today): US MIDTERM ELECTIONS.** Also JOLTS (Sep) and factory orders.
- Wed 2026-11-04: ADP employment 08:15 ET; ISM Services PMI 10:00 ET.
- Thu 2026-11-05: weekly jobless claims, Q3 productivity.
- **Fri 2026-11-06 08:30 ET: October nonfarm payrolls**, consensus ~68K after 29K in
  September. This is the week's main scheduled risk event.
- Mon 2026-11-02 ISM Manufacturing (Oct) printed 55.5 vs 54.7 forecast; prices paid
  eased to 75.2. source: https://fxleaders.com/news/2026/11/03/gold-price-forecast-xau-usd-tests-3920-on-midterm-election-day-after-2-oil-driven-rebound-nfp-friday
  (Trading Economics still shows no actual, so treat 55.5 as single-sourced.)
- Gold spot ~$3,920/oz on the morning of 2026-11-03 (same source). GLD 361.65.
- Implication for every swing idea captured today: a payroll print on Friday sits
  inside the horizon, and a 29K prior means the labour market is already weak — a
  miss is a live possibility, not a tail.

## [06:08 ET] RATES — from Kalshi market prices (direct API, the CLI `events` command
  only samples the first 200 open markets and is useless for this)
- `KXFED-26DEC-T4.00` "fed funds upper bound above 4.00% after the Dec 9 2026 meeting":
  last 0.74, no_bid 0.26 / no_ask 0.27, open interest 58,086. So the market prices
  roughly a 26% chance of a December cut that takes the upper bound to 4.00% or below.
- Kalshi lists `KXCPIYOY-26DEC` strikes up to 5.0% — inflation is not back at target.
- **No Senate/House control series found** under the Politics category listing, so I
  cannot price the midterm outcome and will not guess at one. Not traded.

## [06:09 ET] POSITION UPDATE — XLE — opened 2026-08-15 @ 63.90, +5.2% (67.25)
- decision: HOLD, stop unchanged at 66.50 (raised 2026-11-02). Do not widen it.
- why: the driver has turned against the position — WTI -7.4% on US-Iran diplomacy —
  but the stop raised last session is already 1.1% under the market, so the position
  is effectively resolved within days either way. Widening it to "give the thesis
  room" would be exactly the rewriting-of-the-past the stop exists to prevent.
- action: captured via add_candidate.py, levels unchanged, thesis rewritten.
- flagged: this is XLE's 7th publication in 10 days. Repetition noted as a warning.

## [06:09 ET] POSITION UPDATE — IYR SELL_SHORT — opened 2026-09-02 @ 97.80
- **STOPPED OUT.** Stop was 100.60; Monday 2026-11-02 traded h 101.08, closed 100.90.
- decision: CLOSE. The stop was hit intraday and the position is gone at roughly -3.1%.
- why not re-pitch: the short was a bet on REITs de-rating, and IYR has instead gone
  from a 97.30 20-day SMA to a 100.90 close in four sessions as money rotated into
  rate-sensitive defensives. There is no new information that makes the short better
  at 100.90 than it was at 97.80, and re-shorting here would be averaging into a
  losing thesis. No candidate captured.

## [06:10 ET] POSITION UPDATE — XLF — opened 2026-10-09 @ 54.23, +6.1% (57.56)
- Monday close 57.56 against the published 57.60 target — 4 cents short, and the
  session high was 57.695, so the target traded.
- decision: TAKE THE PROFIT. Target reached; nothing to amend. No candidate captured —
  a closed winner is not re-pitched, and the ranking rules say re-trading is a
  separate decision needing its own evidence, which I do not have for financials here.

## [06:11 ET] RATES — CORRECTED AND MUCH MORE IMPORTANT THAN THE FIRST READ
Kalshi's per-market endpoint returns prices (the list endpoint returns nulls). Dec 9
2026 FOMC, `KXFEDDECISION-26DEC`, all five outcomes, with open interest:
- **Hike 25bps: last 0.71, bid 0.71 / ask 0.72, OI 378,387**
- Hold ("maintains rate"): last 0.27, bid 0.26 / ask 0.27, OI 489,927
- Hike >25bps: 0.02 | Cut 25bps: 0.01 | Cut >25bps: 0.01  (sums to ~1.01)
- Cross-check: `KXFED-26DEC-T4.00` ("upper bound above 4.00% after the Dec 9 meeting")
  last 0.74, OI 58,086. That is only consistent with a **current upper bound of 4.00%**
  and P(hike) ~0.72-0.74 — two independent markets agreeing.
- **So the market prices a ~71% chance the Fed HIKES 25bp on 2026-12-09.** I had this
  backwards an hour ago reading the T4.00 market alone. This is a tightening cycle,
  not an easing one, which is the frame for everything below.
- Consistent with: Kalshi listing CPI YoY strikes up to 5.0% for Dec 2026, gold near
  $3,920/oz, and ISM prices-paid at 75.2.
- Consistent too with the week's real tension: **a Fed about to hike into a labour
  market that added 29K jobs in September.** Friday's payrolls (consensus ~68K) is
  therefore the highest-stakes print of the week, not a routine one.

## [06:12 ET] VENUE CHECK — Robinhood prediction markets, fetched today
Fetched https://robinhood.com/us/en/prediction-markets/ directly rather than trusting
memory. Categories listed: Featured, Sports, Live, NBA, **Midterms, Climate, Companies,
Commodities, Crypto, Economics, Education, Elections, Entertainment, Financial,
Metals, Politics, Technology**. Specific markets the page named:
- Economics: **"How high will US gas prices get in 2026"**, "Number of rate cuts in
  2026", "Fed rate decision in December 2026".
- Metals: palladium / platinum / copper price on November 30.
- Crypto: Bitcoin price at end of 2026; Bitcoin above $200k by 2027.
- **No WTI or Brent market appeared.** Kalshi lists plenty (`KXWTIMONTHLY`, `KXWTIW`,
  `KXBRENTW`), and Robinhood lists a Commodities category, but the page did not show
  one and the content came back truncated. **I will not recommend a WTI contract on
  that basis** — universe.md says verify, not infer.
- **No Senate/House control market appeared** either, and no such series exists under
  Kalshi's Politics category listing. The midterm result is not traded here today.

## [06:13 ET] EVENT CONTRACT CANDIDATE — US gas price annual maximum, 2026
`KXAAAGASMAX-26DEC31`, "How high will US gas prices get in 2026?" — **this exact
market is named on Robinhood's own prediction markets page**, so venue is verified.
Resolution 2026-12-31 06:25Z, AAA US national average.
- Above $4.60: yes 0.24 bid / 0.26 ask, **no 0.74 bid / 0.76 ask**, OI 204,342
- Above $5.00: yes 0.11 / 0.15, no 0.85 / 0.89, OI 106,238
- Above $5.40: yes 0.09 / 0.11, no 0.89 / 0.91, OI 63,349
- Because this resolves on the year's MAXIMUM, the $4.60 strike sitting at 24c proves
  the 2026 year-to-date peak is already BELOW $4.60 — otherwise it would be at 99c.
  Need the live AAA average and the YTD peak before pricing an edge. Fetching next.

## [06:15 ET] GAS PRICE EVENT CONTRACT — priced, and NOT published. Here is why.
- AAA US national average **$4.1694 as of 2026-11-02**, down 11 cents week-on-week and
  $1.14 above a year ago. The 2026 climb was Feb-March: $2.98 on 26 Feb to $4.064 by
  1 April. sources: https://gasprices.aaa.com/ and
  https://www.wglr.com/2026/11/02/gas-prices-down-11-cents-from-last-week/
- `KXAAAGASMAX-26DEC31-4.60` NO = 0.74 bid / 0.76 ask. To resolve YES the national
  average must reach $4.60 at some point in the remaining 59 days: **+$0.43, +10.3%**
  from today, in the seasonally weakest demand window, on winter blend, with the
  retail lag from Monday's 7.4% crude crash still to come (so the realistic starting
  point in two weeks is lower than $4.17, making the required move larger).
- My estimate of YES: **8-12%.** The market's 24-26% looks too high. Expectancy on the
  NO at 0.76 is 0.90x24 - 0.10x76 = **+14.0c on 76c risked, +18.4% over 59 days.**
- **REJECTED anyway, on the reward-to-risk floor.** Held to resolution the NO risks 76
  to make 24 — 0.32:1 against a 2.0 floor. That is what buying a favourite always
  looks like, and strategy.md says an idea that cannot clear its floor does not
  publish. I will not manufacture a 2.0 by inventing a 64c "stop" on a contract I
  would in fact hold to 31 December. Flagging it as watchlist material instead, with
  the numbers above, so the call is visible and reviewable rather than quietly dropped.
- Also checked the Dec 9 FOMC market for an edge and found none I can defend: Hold at
  0.27 would be 2.7:1, but claiming P(hold) > 27% requires an informational edge on
  the FOMC that I do not have, and "the labour market is weak so they might not hike"
  is already in a 490K-open-interest price. "Feels underpriced" is not a thesis.

## [06:17 ET] REJECTED — JETS / airlines — the fuel trade, already paid for
- Airlines were Monday's mechanical winners from the crude crash: JETS 26.93 to 28.05
  (+4.2%), UAL +4.8%, ALK +7.2%, DAL +4.1%, LUV +3.6%.
- JETS close 28.05, just reclaimed the SMA50 at 27.85; SMA20 26.84; ATR(14) 0.9257
  (3.3%); 17.7% below the 120-day high of 34.06; avg dollar volume $115.8M.
- Relative strength (market_data.py relstrength JETS --peer SPY): **1m +1.96% vs SPY,
  3m -13.53%, 6m +5.60%.** A coherent lagging-then-inflecting read — airlines wore the
  fuel spike and are turning as it unwinds.
- **Rejected: the edge left is a bet on US-Iran diplomacy, which I have none.** The
  market paid for the fuel relief in one session; from here JETS needs crude to keep
  falling, and a collapse in talks gaps it straight back. Evidence available tops out
  at two distinct kinds (technical_level, positioning) = conviction 3, and the
  counter-argument can only be "answered" by re-using the same relative-strength
  number, which is one confirmation not two. Conviction 3 is 1/19 on this report's
  record. Not published. **Watch 27.40-27.60 (the SMA50 retest) if crude stays soft.**
- Short interest unavailable: `market_data.py short` returned
  `ReadTimeout` on api.nasdaq.com for JETS, DAL and UAL. Data gap.

## [06:20 ET] POSITION UPDATE — CVS — opened 2026-10-16 @ 93.00, -4.8% (88.51)
- **CVS reports Q3 tomorrow, 2026-11-04, before the open, call 08:00 ET.** Consensus
  ~$1.62-1.65 EPS on ~$104.7-105.0B revenue. FY26 guidance into it: adj EPS $7.90-8.10
  (raised from $7.30-7.50 at Q2 on 2026-08-05), operating cash flow >= $11.5B.
  sources: https://www.marketbeat.com/earnings/reports/2026-11-4-cvs-health-co-stock/
  and https://www.theglobeandmail.com/investing/markets/stocks/UNH/pressreleases/8454605/cvs-health-q3-earnings-preview-how-to-approach-the-stock/
- **This pipeline'"'"'s earnings calendar missed it.** `market_data.py earnings --days 12`
  returned zero rows dated 2026-11-03 or 2026-11-04 — the Finnhub feed has a two-day
  blind spot at the front. Worth fixing; today it nearly hid a print on an open book.
- Context: CI reports 2026-11-05, HUM 2026-11-06 on a consensus LOSS of -$1.01, so the
  managed-care cost trend gets three readings this week, not one.
- decision: **CUT TO HALF SIZE before tomorrow'"'"'s open.** Levels unchanged.
- why: the 85.40 stop is 3.5% below the market and 3.57 ATR away — it stops a drift and
  does nothing about a guidance gap. The only lever available before an 08:00 release
  is size. Halving is the honest middle between the Q2 record (+37.95% EPS surprise,
  guidance raised) and the tape (fresh 120-day-area lows, zero insider buying in six
  months against $359M of sells).
- action: captured via add_candidate.py at position_size_pct 1.5, levels unchanged.
- data gap: `market_data.py implied CVS` returned HTTP 401 from yahoo-options, so I have
  no options-implied move for the print. Stated as unknown rather than guessed.

## [06:21 ET] DATA GAPS so far
- `market_data.py macro` — timed out twice (120s, 180s), zero output. No FRED/VIX/DXY.
- `market_data.py earnings` — two-day blind spot at the front of the window (no
  2026-11-03 or 2026-11-04 rows). Caught CVS by hand; may have missed others.
- `market_data.py short` — ReadTimeout on api.nasdaq.com for JETS, DAL, UAL.
- `market_data.py implied` — HTTP 401 from yahoo-options (CVS). No implied moves today.
- `market_data.py events` — only samples the first 200 open Kalshi markets, so it
  cannot find a named series. Worked around by calling the Kalshi API directly.

## [06:22 ET] POSITION UPDATE — KHC — opened 2026-09-20 @ 23.00, +8.4% (24.93)
- **KHC reports Q3 tomorrow, 2026-11-04, before the open, call 07:00 ET.** Confirmed on
  MarketChameleon; MarketBeat carries the same date as an estimate off last year.
  Again missed by `market_data.py earnings`. source:
  https://marketchameleon.com/Overview/KHC/Earnings/Earnings-Dates/
- The evidence here is unusually asymmetric and worth stating plainly:
  - **CEO Steven Cahillane bought 213,106 shares on the open market 2026-05-12 at
    $23.4616 — $5.0M.** Only insider buy in six months; only sale was $427K; net +$4.57M.
  - Sell side is maximally negative: **7.1% bullish** — 1 strong buy, 1 buy, 17 hold,
    7 sell, 2 strong sell — and unchanged for four months.
  - Four consecutive EPS beats: +4.79%, +14.17%, +8.64%, +4.38%.
  - Close 24.93, above SMA20 23.4755 and SMA50 24.029, coiled 0.7% under the
    22 October high of 25.115 (that day closed 25.09). ATR 0.6664.
- decision: **HOLD FULL SIZE through the print.** Do not trim into it and do not add.
- why hold where CVS gets halved: CVS is at fresh lows with zero insider buying against
  $359M of sells; KHC is above both averages with a $5M CEO buy and four straight beats
  into a consensus that is already on the floor, which is where a beat has room to work.
- post-print conditionals (not to be acted on before it): above 25.115 held, raise the
  stop to 23.40, under the SMA20; back below 23.4755, exit there rather than waiting for
  the 21.20 stop, which is 15% away and is a thesis stop, not a working one.
- action: captured via add_candidate.py, conviction 5, levels unchanged.

## [06:23 ET] DEFENSE — my peace-equals-defense-selloff hypothesis is WRONG on the tape
I expected the US-Iran diplomacy signal to hit the defense complex, which matters
because RTX was published yesterday at 199 and HII is open +19.7%. Monday says no:
- RTX 199.80 to **202.79 (+1.5%)**, ITA 209.74 to **214.68 (+2.4%)**, HII 316.88 to
  313.70 (-1.0%).
- So the market did not price a peace discount into defense on Monday. I am recording
  the hypothesis as not supported rather than writing it into a thesis.
- HII's move is earnings, not geopolitics: it reported **2026-10-29**, record Q3
  revenue $3.5B and diluted EPS $5.48, and gapped 279.26 to 316.21 that session.
  source: https://www.sec.gov/Archives/edgar/data/0001501585/000150158526000054/hii2026q3earningsrelease.htm
- HII decision: HOLD. Stop 288.00 (raised 2026-11-02) now protects +9.9% on a 262.00
  fill; price 313.70, target 339.76. Catalyst is spent, the trail does the work.
  No amendment, so nothing captured.
- RTX decision: the 199.00 limit published 2026-11-02 stands and is 1.9% below Monday's
  202.79 close. Level unchanged, nothing changed, so no re-pitch — re-publishing a
  one-day-old unfilled limit with no new information is the padding the repetition
  guard exists to stop.

## [06:25 ET] POSITION UPDATE — LULU and NKE shorts — both are structurally broken, CLOSE
- `LULU` SELL from 100.61 (2026-09-08), now **107.83, -7.2%**. Above SMA20 99.343 and
  SMA50 102.781, up five sessions, 19.3% above the 120-day low. Stop 112.00 is 3.9%
  away — 0.95 ATR on a 4.3685 ATR. It will very likely be taken.
- `NKE` SELL from 38.40 (2026-09-08), now **39.12, -1.9%**. Above SMA20 36.787 and
  SMA50 36.9116, up four sessions. Stop 41.00 is 4.8% away, 1.78 ATR on a 1.0587 ATR.
- **The driver has flipped against both, and that is the reason to close rather than to
  wait for the stops.** Monday's crude crash is a direct real-income transfer to the US
  consumer — AAA national average already $4.1694 and falling 11c/week — and consumer
  discretionary was one of the two LEADING S&P sectors on Monday, with XLY closing
  118.16, +2.4%, after a 119.205 high. Shorting two consumer-discretionary brands into
  a gasoline-driven consumption tailwind is being short the wrong thing, which is a
  different and worse problem than being early.
- decision: **CLOSE BOTH at Tuesday's open**, -7.2% and -1.9%, rather than holding for
  a 112.00 and a 41.00 stop that are now the likely outcome.
- **Not captured via add_candidate.py, deliberately.** The schema can only express an
  open recommendation: capturing LULU would publish a row reading "sell LULU, target
  77.00", which is the opposite of this instruction no matter what the scale plan says.
  **Synthesis must carry these two as position-close notes in the report prose, not as
  recommendation rows.** Flagging it here because silence would lose the call entirely.

## [06:26 ET] REJECTED — AAP — the catalyst date does not verify and the beats are cost-led
AAP looked like the best new idea of the morning and it does not survive falsification.
- The setup that attracted me: 5.7% bullish share (2 strong buy, 0 buy, 24 hold, 8
  sell, 1 strong sell; holds 25→24 and sells 7→8), four consecutive EPS beats of
  +26.7%, +68.2%, +103.7% and +21.2%, close 47.92 within 0.25% of the session high of
  48.04 which is the highest print since 2026-08-31, SMA20 44.1715, SMA50 42.9642,
  ATR 1.7446, avg dollar volume $77.1M, and +6.2% on Monday with the consumer tailwind.
- **Killed by three things.** (1) **The earnings date does not verify.** My Finnhub
  calendar says 2026-11-05 bmo; stockanalysis.com lists the next report as 2026-10-29,
  and a Barron's headline describes a surprise third-quarter loss with reduced guidance
  and no date attached. The 29 October bar (o46.57 h46.75 l44.89 c45.73) shows no such
  reaction, so I think Finnhub is right — but "I think" is not a verified calendar and
  `dated_catalyst` requires one.
- (2) **The beats are the wrong kind.** On 2026-08-20 AAP fell 25% to 42.39 on a Q2
  where adjusted EPS beat and *sales missed*, comps -0.5%, DIY down on "tighter
  household budgets", with reaffirmed revenue guidance whose midpoint was under
  consensus. So the surprise record is cost-out against lowered bars on a shrinking top
  line, which is not the same fact as four beats.
  source: https://finance.yahoo.com/markets/live/earnings-live-updates-advance-auto-parts-stock-drops-24-as-constrained-customer-spending-weighs-on-sales-growth-115925351.html
- (3) **There is no room left.** RBC cut its target to $49 from $52 on 2026-10-23
  saying the high end of 2026 guidance "feels increasingly unlikely"; AAP closed 47.92.
  source: https://www.investing.com/news/analyst-ratings/rbc-cuts-advance-auto-parts-stock-price-target-on-cost-pressures-93CH-4969903
- Also note the mechanism I liked — cheaper gasoline, more miles driven, more parts — is
  contradicted by the company's own DIY commentary about tight household budgets.

## [06:27 ET] REJECTED — UAA — a real insider datum, but the entry is a chase
- `market_data.py insiders UAA`: Fairfax Financial bought 1,178,344 shares across
  12-14 May 2026 at 4.9934 / 4.9733 / 5.00 — $5.87M, zero sells. 9.1% bullish share.
  Surprises +184%, -69%, +537%, +61% (on near-zero estimates, so the percentages are
  noise). Reports 2026-11-06 bmo, consensus EPS -$0.0066.
- Rejected: close 5.24 is 8% above both the SMA20 (4.8445) and SMA50 (4.8628) after a
  run from 4.67 on 27 October, two sessions before a print, and Fairfax's purchase is
  six months stale at a price 5% below the market. Buying the chase is not buying what
  Fairfax bought. Watch 4.95-5.05 after the print.

## [06:28 ET] POSITION UPDATE — BCC — thesis deteriorating on every axis, CLOSE
- Open long from 76.50 (2026-08-18), now **75.00, -2.0%**, no stop, target 110.00.
- **BCC reported Q3 on Monday 2026-11-02 and the tape rejected it hard:** o 79.92,
  high 82.00, low 74.83, close 75.00 — an 8.5% intraday reversal from the high.
  Revenue $1.80B, +8.1% y/y and a beat; GAAP EPS $1.04, **7% BELOW consensus**, with
  lumber prices at 2026 lows going in.
  sources: https://stockstory.org/us/stocks/nyse/bcc/news/earnings/boise-cascade-nysebcc-surprises-with-q3-2026-sales
  and https://investing.com/news/earnings/boise-cascade-earnings-up-next-as-lumber-prices-hit-2026-lows-93CH-4990477
- Every measurable has turned: first EPS miss in four quarters (-7.7% after +30.8%,
  +18.3%, +47.2%); analyst bullish share **54.5%, deteriorating -9.1 points**, buys cut
  6→5; zero insider buys in six months against 3 sells (net -$666K); Loop Capital cut
  to Hold on 2026-10-26 and BofA holds a Sell with an $80 target against a 75.00 close.
  Close 75.00 is under both the SMA20 (75.498) and SMA50 (76.3016). ATR 2.6553 (3.54%).
- decision: **CLOSE.** This was a long_term position carrying no stop and a 110.00
  target, i.e. +47% from here, and I cannot defend 110 on today's evidence — a
  long_term idea whose downside I cannot price is by strategy.md's own rule not
  researched enough to hold, let alone republish. Average dollar volume is only $25.9M,
  so exiting is best done on the open rather than late in a thin tape.
- Not captured via add_candidate.py, for the same schema reason as LULU and NKE:
  a BCC row would have to carry a target, and the only honest target is "flat".
  **Synthesis must carry this as a position-close note in the prose.**

## [06:28 ET] POSITION SWEEP — the rest, no amendment needed, nothing captured
- `PFE` buy 27.60 (2026-08-18), **30.67, +11.1%**, long_term, target 42.00, no stop.
  HOLD. Nothing dated this week; the de-rating thesis is unchanged and the position is
  working. Recommended 5x in ten days already — no reason to make it 6.
- `STLD` buy 245.50 (2026-10-10), **251.91, +2.6%**, stop 228.75, target 281.00.
  HOLD. Materials was one of Monday's two leading sectors; STLD still faded from a
  259.24 high to 251.91, so the breakout has not confirmed. Stop 228.75 is 1.76 ATR
  (9.5193) below entry and already published — unchanged.
- `UNP` buy 288.60 (2026-10-15), **307.00, +6.4%**, stop 277.40, target 315.99 (the
  120-day high, 2.85% away). HOLD. Diesel is a top-three rail operating cost and
  Monday's crude crash is a direct tailwind; the position is working and the target is
  close. No amendment — the printed stop is wide but it is the thesis stop.
- `ABT` buy 103.00 (2026-10-16), **110.16, +6.9%**, stop 97.00, target 117.34.
  HOLD. +3.7% on Monday, above the SMA20 (102.8365) and SMA50 (104.2104), 6.1% off the
  120-day high which is also the target. I did not establish what drove Monday's move
  and am not going to assert one.
- `PYPL` buy 56.50 (2026-10-21), **58.78, +4.0%**, stop 54.10, target 62.73 (the
  120-day high). HOLD. +3.1% Monday, above SMA20 56.4032 and SMA50 55.3076. No PayPal
  earnings date could be confirmed either way — recorded as unknown, not as "none".
- `HII`, `XLF`, `IYR`, `XLE`, `KHC`, `CVS`, `LULU`, `NKE`, `BCC` — all covered above.

## [06:29 ET] AWAITING-ENTRY SWEEP — published levels not yet filled
- `OXY` buy 54.00 (2026-09-24). **Reports 2026-11-09 after the close (provisional —
  MarketBeat says the company has not confirmed).** Monday's 7.4% crude crash will push
  OXY toward this limit for exactly the wrong reason. Same rule as VST: do not take the
  fill ahead of the print. source: https://www.marketbeat.com/stocks/NYSE/OXY/earnings/
- `AAL` sell_short 13.35 (2026-10-03). **This one has turned against itself.** Jet fuel
  is an airline's largest variable cost and crude just fell 7.4%; airlines were
  Monday's mechanical winners (UAL +4.8%, ALK +7.2%, DAL +4.1%, LUV +3.6%, JETS +4.2%).
  A short entry 13.35 would now fill into a fuel-cost tailwind. **Recommend
  withdrawing the order.** Not captured — same schema problem as the closes.
- `GLD` sell 406.77 (2026-10-25). LEAVE AS IS. GLD closed 361.65 (+1.65%) with spot
  near $3,920, so the limit is 12.5% above the market and only fills on a melt-up,
  which is a defensible place to fade. Note the regime is against the short, though:
  a Fed priced at 71% to HIKE into 4-5% CPI and a 29K-payroll labour market is the
  stagflation setup gold is rallying on.
- `SMMT` buy 17.10 (2026-10-27). Left alone — a PDUFA-dated idea from last week, and
  SMMT already stopped out once on 2026-10-26 from an earlier entry. No new information.
- `RTX` buy 199.00 and `XLU` buy 43.30, both published 2026-11-02. Levels stand, one
  day old, nothing changed — re-publishing them would be padding. One caveat worth
  recording for XLU: it closed 43.67, through the 43.30 limit, and a utility long is
  structurally fighting a Fed the market prices at 71% to hike on 9 December.
- `KXCPIYOY-26SEP-T3.5` NO @ 18 (2026-09-30). The September CPI contract this refers to
  has a resolution date in the past relative to today. Flagging it as stale rather than
  re-pricing it; it should not still be sitting in awaiting-entry.

## [06:30 ET] FALSIFICATION PASS — all six captured candidates, arithmetic recomputed
Recomputed every ratio by hand rather than trusting what I wrote into the JSON.

| sym | entry | stop | target | R:R | floor | stop ATR | floor | win p | b/e | expectancy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLE | 63.90 | 66.50 | 70.50 | 2.54 | 2.0 | **1.69** | **1.8** | 0.42 | 0.282 | +0.49R |
| VST | 132.00 | 117.00 | 162.70 | 2.05 | 2.0 | 2.07 | 2.0 | 0.37 | 0.328 | +0.13R |
| CVS | 93.00 | 85.40 | 110.68 | 2.33 | 2.0 | 3.57 | 2.0 | 0.35 | 0.300 | +0.17R |
| KHC | 23.00 | 21.20 | 28.09 | 2.83 | 2.0 | 2.70 | 2.0 | 0.44 | 0.261 | +0.69R |
| ELAN | 23.00 | 21.30 | 27.98 | 2.93 | 2.0 | 2.28 | 2.0 | 0.42 | 0.254 | +0.65R |
| CELH | 27.90 | 25.50 | 36.15 | 3.44 | 2.0 | 2.07 | 2.0 | 0.30 | 0.225 | +0.33R |
- All six clear the R:R floor and all six have positive expectancy at their own stated
  hit rate. No claimed edge exceeds 20 points over break-even (largest is KHC at +17.9).
- **XLE will fail `check_stop_distance` and be demoted, and that is an artifact — read
  this before "fixing" it.** 66.50 is a protective trail on a position filled at 63.90
  on 2026-08-15 and now at 67.25; it is 0.49 ATR *below the market*, not inside the
  noise of a new entry. The validator measures stop distance from the recorded fill,
  which is the right rule for a new idea and the wrong one for an amendment. **Do not
  widen the 66.50 stop to clear the floor** — that is the KRE mistake running backwards.
  Demotion to the watchlist is the lesser error; the stop stays where it is.
- Each idea's own biggest hole, stated rather than argued away:
  - **XLE** — the driver has turned against the position. Held only because the stop is
    1.1% away. If the stop is widened by anyone, close the position instead.
  - **VST** — 132.00 is *below* the 120-day low of 132.66 on a stock making lower lows
    four weeks running. R:R 2.05 is barely over the floor. The idea is only sound
    because `wait` is true and the condition requires 130 to hold on the print.
  - **CVS** — halving may be selling the bottom of a name that beat by 38% last quarter.
    Keeping half is the hedge against my own call being wrong.
  - **KHC** — Cahillane's buy is six months old at 23.46 and the stock is 24.93, so he
    is up 6% and this is not his entry. Holding full size through a binary is the most
    aggressive call in the book today and it rests on the 7.1% bullish share leaving
    room on the upside, which is an argument about positioning, not about the numbers.
  - **ELAN** — the insider cluster is nearly three months old and the limit sits 4.6%
    under the market, so it fills on weakness into a print or not at all.
  - **CELH** — the target is the 120-day high, a 29.6% move, and the thing most likely
    to produce the fill is a second consecutive earnings miss.

## [06:31 ET] CORRELATION AND BOOK-SHAPE WARNING — synthesis must carry this
- **Five of six captured ideas resolve on an earnings print inside four sessions**:
  CVS and KHC on 2026-11-04, CELH on 11-05, VST and ELAN on 11-06. Different companies
  and five different sectors, so this is not one bet with extra steps — but it is one
  *week*, and a reader should know the book is dense with event risk rather than spread.
- **Every captured idea is long, and today's recommendations also close two shorts
  (LULU, NKE) and withdraw a third (AAL).** So the book goes from mixed to one-sided
  on the morning of a midterm election and three days before a payroll print whose
  prior was 29K. That concentration is a deliberate consequence of the evidence, not
  an oversight, and it is the single thing most likely to make today's report wrong
  together rather than wrong one idea at a time.
- Sector doubling worth naming: KHC and CELH are both consumer packaged goods; CVS and
  ELAN are both healthcare-adjacent. Two in each, under the cap of three.

## [06:32 ET] HOW THE TRACK RECORD CHANGED TODAY'S BAR
3/32 hit target (9%), avg -5.7%, with stocks 1/21 (5%) and conviction-3 ideas 1/19 (5%).
n=32 is past the ~15-trade noise line, so I treated it as signal and it changed outcomes:
- **Nothing conviction-3 was published as a new idea.** JETS was the day's most obvious
  trade and was rejected explicitly because its evidence topped out at two kinds.
- **Insider open-market buying became the primary screen** rather than a confirmation,
  because it is the one evidence kind this report has been under-using and the one the
  skill flags as genuinely predictive. It produced ELAN (7 buyers), CELH (4 buyers),
  KHC (CEO, $5.0M) and VST (CEO) — and its absence is what killed AAP and BCC.
- **Three of six ideas say "wait"** (VST, CELH, and ELAN at half size). On a day with
  this many prints inside the horizon, not entering is the recommendation.
- Six ideas is the honest count, not a shortfall. I did not publish the gas-price
  contract I believe is mispriced, because it fails the R:R floor; I did not publish
  JETS, AAP, UAA or XLY, because each failed a specific test written down above.

## [06:33 ET] NEW IDEA — ONON — all three co-founders bought, and the level is their average
Found by running the insider screen across next week's large reporters (NRG, CNH, DDS,
HIMS, TTD, ONON, SBH, WIX, CTVA, TTWO, FERG, SE). Only two clusters came back:
- **ONON: 8 open-market buys, 3 distinct buyers, $10.58M against $115K of sales.** All
  three co-founders — Coppetti, Bernhard, Allemann — each took ~60,000 shares on
  2026-05-14 at 36.754/35.973, then Coppetti and Bernhard each added 65,000 on
  2026-08-14 at 30.6737. Weighted average about **$34.14** on 310,000 shares.
- WIX: 8 buys by 6 distinct buyers but only **$186K total** — about $31K each, against
  15 sells. Six names does not make a cluster when the dollars are that small.
  Rejected on size, not on count.
- The ONON confluence is what makes it tradeable rather than just interesting: the
  founders' average 34.14, the SMA20 34.135 and Monday's session low 34.18 are the same
  price to within 7 cents, and the stock closed 35.52 just under the 36.08 resistance
  after a +5.2% day. Earnings 2026-11-10 bmo, consensus revenue $947.6M / EPS $0.4038.
- Captured at entry 34.20, stop 31.20 (below the 27 October low of 31.28, 2.31 ATR),
  target 41.41 (the 120-day high), R:R 2.40, win probability 0.36 vs a 0.294 baseline.

## [06:34 ET] FALSIFICATION — ONON added to the table
| sym | entry | stop | target | R:R | stop ATR | win p | b/e | expectancy |
| ONON | 34.20 | 31.20 | 41.41 | 2.40 | 2.31 | 0.36 | 0.294 | +0.22R |
- ONON's own biggest hole: the founders were buying at 36.75 and the stock then fell to
  26.37, so their timing has been wrong by 28% once already, and averaging down is what
  a controlling owner does regardless of the setup. The idea leans on the price
  confluence, not on the signal alone. Second hole: the beat streak has flattened —
  Q2 2026 was +1.8% after +51.5%, +20.9% and +87.4%.
- Correlation recheck with ONON added: consumer-adjacent longs are now **KHC, CELH,
  ONON — exactly three**, which is at the cap in `config/strategy.md` and not over it.
  Healthcare-adjacent is CVS and ELAN (two). VST is power, XLE energy.
- Conviction audit across all seven: the score equals the count of distinct evidence
  kinds in every case — XLE 2 kinds/3, VST 3/4, CVS 3/4, KHC 4/5, ELAN 3/4, CELH 3/4,
  ONON 3/4. Nothing is rounded up. Four candidates were held at 4 rather than 5
  specifically because `counter_argument_answered` did not honestly hold: for VST and
  CELH I am waiting for the print rather than answering the bear case, and for ELAN and
  ONON I could not research the actual strongest objection (Elanco's leverage and
  generic exposure; On's exposure to a constrained premium consumer).

## [06:35 ET] RESEARCH COMPLETE
- **candidates: 7** — XLE, VST, CVS, KHC, ELAN, CELH, ONON. All seven long.
  Three are amendments to open positions (XLE, CVS, KHC), two are amendments to
  unfilled published levels (VST, ELAN), two are new (CELH, ONON).
  Three carry `wait` or a hold-fire condition (VST, CELH, and ELAN at half size).
- **Position decisions that could NOT be captured in the schema** and which synthesis
  must carry as prose, not as recommendation rows — each is a CLOSE or WITHDRAW, and a
  candidate row would have had to carry a target, which would read as "keep holding":
  - `IYR` sell_short — stopped out, Monday traded 101.08 against a 100.60 stop.
  - `XLF` buy — target reached, Monday traded 57.695 against a 57.60 target.
  - `LULU` sell and `NKE` sell — both structurally broken by the gasoline tailwind to
    the consumer; close at the open rather than wait for the 112.00 and 41.00 stops.
  - `BCC` buy — first EPS miss in four quarters, analyst revisions deteriorating -9.1,
    zero insider support, lumber at 2026 lows, and an 82.00-to-75.00 reversal on the
    print. A 110.00 target I cannot defend. Close.
  - `AAL` sell_short @ 13.35 — withdraw the unfilled order; crude -7.4% is a jet-fuel
    tailwind and the short would now fill into it.
  - `KXCPIYOY-26SEP-T3.5` NO @ 18 — stale, its September resolution is in the past.
- **coverage gaps**
  - `market_data.py macro` produced nothing at all (two timeouts, 120s and 180s). No
    FRED series, no VIX, no DXY this run. The macro picture here is reconstructed from
    ETF proxies, Kalshi prices and the web, and is stated that way throughout.
  - `market_data.py earnings` has a two-day blind spot at the front of its window — no
    rows dated 2026-11-03 or 2026-11-04. **CVS (11-04) and KHC (11-04) both report
    inside it and I only caught them by hand.** Anything else reporting today or
    tomorrow may have been missed. This is the most consequential gap today.
  - `market_data.py implied` is returning HTTP 401 from yahoo-options, so no idea today
    carries an options-implied move and none of the five earnings-driven ideas could be
    checked against what the straddle prices.
  - `market_data.py short` timed out on api.nasdaq.com, so no short-interest or
    days-to-cover reading on anything.
  - `market_data.py events` is unusable for finding a named market — it samples only the
    first 200 open Kalshi markets. Worked around via the Kalshi API directly, but note
    that the list endpoint returns null prices and only the per-market endpoint has them.
  - No Senate/House control market exists under Kalshi's Politics series listing and
    none appeared on Robinhood's page, so **the midterm election happening today is not
    traded in this report** — not because it was ignored, but because I could not
    verify a tradeable instrument for it.
  - AAP's earnings date could not be reconciled between sources and the idea was
    dropped for that reason alone; PYPL's next earnings date could not be found at all.
- **sources that failed**: `market_data.py macro` (timeout x2), `market_data.py short`
  (api.nasdaq.com ReadTimeout), `market_data.py implied` (yahoo-options HTTP 401),
  Robinhood prediction-markets page (returned truncated, so the Commodities category
  could not be enumerated and no WTI market was recommended).
- **why seven and not more**: the day had one dominant macro event (crude -7.4% on
  US-Iran diplomacy) and a dense earnings week, and the ideas that cleared the bar are
  the ones where fetched insider data, a verified earnings date and a real price level
  lined up. JETS, AAP, UAA, XLY and the gas-price contract were each rejected for a
  specific reason written down above, and the gas contract is the one I believe is
  genuinely mispriced but cannot publish because a favourite at 0.76 can never clear a
  2.0 reward-to-risk floor. Seven is the honest count.

## [06:36 ET] LATE AND IMPORTANT — **PFE REPORTS THIS MORNING**, and the calendar hid it
Kept screening after writing the RESEARCH COMPLETE block above, which is why this
comes after it. **This block supersedes that one on the candidate count.**
- **Pfizer reports Q3 2026 today, 2026-11-03, before the open, call 10:00 ET** — listed
  as *Confirmed* on TipRanks. Consensus adjusted EPS **$0.73 against $0.87** a year ago.
  sources: https://www.tipranks.com/stocks/pfe/earnings and
  https://www.marketbeat.com/earnings/reports/2026-11-3-pfizer-inc-stock/
- PFE is an **open long_term position at +11.1% carrying NO STOP**, and it reports in
  about two hours. That is the third print on this book that the Finnhub calendar's
  two-day front blind spot concealed, after CVS and KHC on 11-04. All three were found
  by hand. **This is now the most important engineering finding of the run.**
- What the data says, all fetched this morning:
  - **3 open-market insider buys by 3 distinct buyers, $2.96M**, within a week in
    August: CEO **Albert Bourla** 38,000 shares at 26.34 (08-12), director Mortimer
    Buckley 37,632 at 25.52 and director Ronald Blaylock 39,231 at 25.46 (both 08-05).
    Net +$2.83M after 2 sells.
  - Sell side at a **38.2% bullish share** and deteriorating — 5 strong buy, 8 buy,
    18 hold, 2 sell, 1 strong sell, with the sell count up from 1 to 2 on 2026-11-01.
  - Four consecutive EPS beats: +11.4%, +3.5%, +14.3%, +36.0%.
  - Monday printed **31.04, a new 120-day high**, closing 30.67, 1.19% under it; 29.9%
    above the 120-day low of 23.62. SMA20 29.3315, SMA50 28.5986. ATR 0.6289 (2.05%).
    Average dollar volume $948.1M.
- decision: **HOLD through the print. No add, no trim.** A long-term holder does not
  trade an earnings reaction. The value of publishing it is the invalidation, which a
  stopless position needs written down before the open and not discovered at 10:00:
  **a cut to full-year guidance, or management conceding the post-LOE pipeline will not
  cover the revenue coming off patent through 2028.** Bear-case anchor **25.00**, below
  all three August insider purchases and above the 23.62 low.
- arithmetic: R:R (42.00 - 27.60) / (27.60 - 25.00) = 14.40 / 2.60 = **5.54**, against
  the 2.5 long_term floor; break-even 15.3%; stated 32%; expectancy **+1.09R**.
- Honest caveat: PFE is now its 6th publication in ten days and the 42.00 target is the
  standing published one — **I did not re-derive that valuation this run** and say so
  rather than implying fresh work. The only new fact is the print date, which is
  exactly the thing the repetition guard asks you to name.
- Also checked and clean: UNP already reported **2026-10-22** (SEC 8-K), so the open UNP
  long has no print inside the week. ABT, PYPL and STLD dates could not be confirmed
  either way from the sources that answered — recorded as unknown, not as "none".

## [06:37 ET] FINAL SCREENS — two more insider sweeps, nothing published
- Next-week reporters (NRG, CNH, DDS, HIMS, TTD, ONON, SBH, WIX, CTVA, TTWO, FERG, SE):
  produced ONON, published. WIX rejected — 8 buys by 6 buyers but **$186K total**, about
  $31K each against 15 sells; six names is not a cluster when the dollars are that small.
- Nov 11-13 consumer reporters (YETI, WWW, FLO, SPB, EYE, GFF, EPC, PSFE, BZH, GLOB):
  no clusters. Single stale buyers only — FLO $38K, SPB $182K, EYE $776K, GLOB $972K,
  all one buyer and all May-June. Nothing published.
- Remaining 2026-11-05 reporters (EPAM, AKAM, AFRM, COMP, CENX, ASTH, ACIW, ENOV, BILL,
  DKNG): one near-miss. **ENOV** has 9 buys by 2 distinct buyers (CEO Damien McDonald
  among them) at 18.80-19.46 in early September, $542K, zero sells, reporting 11-05.
  **Not published**: two buyers and $542K is materially below the bar the three
  published clusters cleared (ELAN 7 buyers, CELH 4, ONON 3 at $10.6M), and healthcare
  already holds two of the three slots the correlation cap allows. Padding the report
  with the weakest evidence of the set is the thing today's track record argues against.

## [06:38 ET] FINAL COUNTS — supersedes the RESEARCH COMPLETE block above
- **candidates: 8** — PFE, KHC, ELAN, CELH, ONON, CVS, VST, XLE. All eight long.
  Ranked on evidence: KHC is the only conviction 5 (4 distinct evidence kinds); PFE,
  VST, CVS, ELAN, CELH and ONON are conviction 4 (3 kinds); XLE is a conviction 3
  position amendment (2 kinds).
- **Six of the eight resolve on an earnings print inside six sessions**: PFE today,
  CVS and KHC on 11-04, CELH on 11-05, VST and ELAN on 11-06, ONON on 11-10. Six
  different sectors, so it is not one bet — but the book is dense with event risk in a
  single week, on a midterm election day, three days before a payroll print whose prior
  was 29K. Synthesis should say so plainly.
- **Insider open-market buying is the spine of this report**: PFE (3 buyers incl. CEO
  Bourla, $2.96M), ELAN (7 distinct buyers, $1.67M, zero sells), CELH (4 buyers incl.
  CEO Fieldly, $2.55M, zero sells), ONON (all 3 co-founders, $10.58M), KHC (CEO
  Cahillane, $5.0M), VST (CEO Burke, $1.17M). Its absence is what killed AAP and BCC.
- coverage gaps and failed sources: unchanged from the block above — `macro` produced
  nothing, `earnings` has a two-day front blind spot that hid three prints on the open
  book, `implied` returns HTTP 401, `short` times out, and no tradeable midterm
  instrument could be verified on the day of the election.
