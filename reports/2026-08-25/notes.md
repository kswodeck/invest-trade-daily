# Research log — 2026-08-25

## [06:37 ET] MACRO — rates, crypto, data-source status
- US 10y 4.74% (2026-08-21, prev 4.69) — rising; 2y 4.24 (prev 4.19); fed funds eff 3.63%; 10y-2y +0.46 (2026-08-24, prev 0.50, flattening) — source: FRED via market_data.py macro
- Unemployment 4.1% (Jul 2026, prev 4.2). CPI index 332.813 (Jul 2026).
- TLT 82.56, +0.62% on 2026-08-24 close (prev close basis, pre-market now)
- BTC $79,266 (+1.7% 24h), ETH $2,476.86 (+0.04%), SOL $99.47 (+4.82%) — source: CoinGecko
- **DATA GAP**: Yahoo Finance returning HTTP 429 across the board — SPX, NDX, DJI, RUT, VIX, ES/NQ futures, DXY, ^TNX, gold, WTI all `ok:false`. Finnhub refuses CFD indices. No live index/VIX/DXY/oil read this run unless another source works.
- Market session: pre (06:35 ET). Freshest honest equity price = 2026-08-24 close.

## [06:37 ET] POSITION REVIEW — the BTC short is the headline problem
- Open book carries BTC SELL (entry 62,950 / 63,400) and /MBTU6 SHORT (entry 64,100 / 64,340, stop 66,600). BTC now 79,266.
- The 66,600 stop was blown through long ago; 2026-08-24 notes already flagged a mandatory cover. Restate it today: **the short is wrong and must be closed**, not held.

## [06:43 ET] CALENDAR — dated catalysts inside 10 sessions (source: Finnhub via market_data.py earnings)
- **2026-08-26 AMC: NVDA** (est EPS 2.13, rev $93.6B) — the market-wide event of the week
- 2026-08-26 AMC: CRM, CRWD, SNPS, VEEV, OKTA, NTNX, HPQ, URBN; BMO: BBWI, DY, GMS, SJM, PLAB
- 2026-08-27 AMC: MRVL, ULTA, ADSK, WDAY, AFRM, ESTC, GAP, IREN, RBRK, S; BMO: **DG**, BBY, HRL, HQY, BILI, CSIQ
- 2026-08-25 (today) AMC: INTU, ZM, HEI, SMTC, BOX, NCNO, QFIN; BMO: WSM, JKS; unspecified: ANF, FIVE, KSS, GES
- 2026-09-01 AMC: PANW; also DLTR, MDB, M, MDT, NIO, CRDO, GTLB
- 2026-09-02 AMC: **AVGO**, **LULU**, SNOW, HPE, GOLD; also NTAP, AI, AGX
- 2026-08-31 BMO: FRO (tanker — relevant to DHT position), SAIC, ASO, AEO

## [06:43 ET] TAPE — semis de-risked into the NVDA print (source: Finnhub quotes, 2026-08-24 close)
- NVDA 208.48 -2.91% on 135.2M shares (highest volume since 8/3). MRVL 229.29 -3.27%. AVGO 358.76 -2.63%.
- NVDA history (Nasdaq via market_data.py): ATR14 5.89 (2.82%), SMA20 213.78, SMA50 207.65, 90d range 189.80-236.54, -11.9% off the high.
- Five-session slide 225.30 (8/13) -> 208.48 (8/24), closing right on the 50-day. Positioning is being cut ahead of the print, not after it.
- Retail was the opposite: FIVE +4.99%, ANF +3.07%, KSS +3.98%, ULTA +3.32%, DG +1.56%, LULU +1.41% — a rotation out of AI into consumer discretionary on 8/24.

## [06:40 ET] MACRO — the regime is HIKE risk, not cut hope (source: Kalshi API direct)
Kalshi KXFEDDECISION, live 2026-08-25 (prices in cents = implied probability):
- **Sep 16 2026 FOMC: hold 65/66, HIKE 25bp 33/34, cut 25bp 0/1, cut >25bp 0/1**
- Oct 28 2026: hold 72/73, hike 25bp 22/23, cut 25bp 3/4
- Dec 9 2026: hold 65/66, hike 25bp 24/28, cut 25bp 7/8, cut >25bp 2/3
- OI is real: Sep hold 4.03M contracts, Sep hike-25 1.83M. This is not a thin market.
- Read: the market assigns essentially ZERO probability to a cut at the next three meetings and a
  one-in-three chance of a hike in three weeks. Every rate-sensitive long in the book is fighting this.
- Consistent with FRED: 10y 4.74 (rising), 2y 4.24 (rising), curve +0.46 flattening from +0.50, eff FF 3.63.
- **DATA GAP / TOOLING BUG**: `market_data.py events` returns junk (multi-leg parlay markets) and shows
  bid/ask/last as null. Kalshi renamed the fields to `yes_bid_dollars`/`yes_ask_dollars`/`last_price_dollars`;
  the parser still reads `yes_bid`/`yes_ask`/`last_price`. Worked around by calling the Kalshi API directly.
  Worth fixing in scripts/market_data.py — event-contract hunting is blind without it.

## [06:40 ET] CALENDAR — this week's macro is front-loaded onto Wednesday
- **Wed 2026-08-26: July PCE + personal income/spending, Q2 GDP 2nd estimate, durable goods, CB consumer confidence.**
  Core PCE consensus +0.2% m/m, 3.3% y/y unchanged — source: https://letterstoayounginvestor.substack.com/p/weekly-economic-calendar-august-24 (via search snippet; page 403s to direct fetch)
- **Jackson Hole Symposium Thu-Sat 2026-08-27..29, remarks from Fed Chair Kevin Warsh.**
- So Wednesday carries PCE in the morning and NVDA after the close. That is the week.
- Core PCE at 3.3% against an effective funds rate of 3.63% is a ~0.3% real policy rate. That is what the
  33% September hike probability is pricing.

## [06:44 ET] POSITION UPDATES — four closes captured (candidates 1-4)
- `/MBTU6` SHORT — **COVER AT MARKET**. Entries 62,950-64,340, highest stop 66,600, BTC now 79,266 (+19% past the stop).
  Yesterday's report called this at 77,915 and it was not done; the loss has widened 1,351 pts/contract since. captured.
- `BTC` SELL (spot) — **abandon the view**. Robinhood Crypto cannot short so this was always exit-or-avoid. captured.
- `TLT` BUY — **CLOSE**. Opened 8/20 @82.60, now 82.56. The premise (a Fed easing path) has been repriced to zero:
  Sep hike 33c vs cut 0-1c. TLT below 50-day 84.10, 1.7% off the 120-day low 81.17. PCE Wed + Warsh at Jackson Hole Thu. captured.
- `TJX` BUY — **CLOSE**. Stop 145.50 breached 8/19, never recovered; 140.71 vs entry 150.85 (-6.7%), 90-day low 139.17,
  9.5% below the 50-day. Note the tell: on 8/24 the whole discretionary group ripped (FIVE +5.0, KSS +4.0, ANF +3.1,
  ULTA +3.3) and TJX closed +0.13%. Group bid, name not bid = company-specific. captured.
- NOTE FOR SYNTHESIS: validate_report.py demotes any idea lacking a real entry/target pair, so these four will likely land
  in the watchlist. They are ACTIONS, not watchlist items. Yesterday's report hit the same wall and the closes were not
  executed. Put them at the top of data_quality_notes again.
- Kalshi source URL: `https://api.elections.kalshi.com/trade-api/v2/markets/<TICKER>` returns 200 today (it 404'd for
  yesterday's validator). The `?event_ticker=` query form also returns 200 and is what I am citing.

## [06:47 ET] TAPE — 2026-08-24 close and the overnight (sources: CNBC, ts2.tech)
- SPX 7,652.86 -0.28%; Nasdaq Composite 25,980.19 -0.76%; Dow 53,417.16 +0.26% — a rotation day, not a risk-off day.
  source: https://www.cnbc.com/2026/08/23/stock-market-today-live-updates.html
- Chips/memory led the fall: MU -5.8%, Sandisk -6%, Seagate -6.5%, Coherent -4%, Lumentum -4%, AMD -3%, AVGO -2%,
  Corning -3%, NVDA -2.91%, MRVL -3.27%.
- Premarket 2026-08-25 ~05:09 ET: semis reversing higher, Sandisk and Micron leading, QQQ reclaiming ~711;
  QQQ -0.20% then +0.27%, SPY -0.13% then +0.16%, IWM +0.24% — source: https://ts2.tech/en/stock-market-today-08-25-2026/
  (treat as directional colour, not a tradeable level — pre-market prints, no depth.)

## [06:47 ET] MACRO — Warsh's first Jackson Hole is Friday 2026-08-28, not Thursday
- Kevin Warsh became Fed Chair 2026-05-22; **keynote Friday morning 2026-08-28**, symposium runs 8/27-8/29.
- Inflation still ~3.4% vs the 2% target. 69% of surveyed fund managers expect a neutral tone.
- Warsh has publicly argued AI-driven productivity gains are disinflationary — if he develops that at Jackson Hole
  it is a dovish surprise against 33c September hike pricing. That cuts against being long the hike contract.
- sources: https://www.xtb.com/en/education/jackson-hole-2026-warsh-fed-speech ,
  https://www.techtimes.com/articles/325228/20260821/jackson-hole-2026-what-watch-when-warsh-steps-podium-friday.htm ,
  https://finance.yahoo.com/economy/policy/articles/warsh-first-jackson-hole-speech-200000444.html

## [06:47 ET] NEW DATED CATALYST — Canada counter-tariffs on $20B of US goods effective 2026-09-08
- Canada set to apply counter-tariffs on $20B of US products on Sept 8; US/Canadian metals, lumber, automotive and
  retail names moved on it Monday. STLD and GOOS named. source: (CNBC 8/24 market wrap, via search)
- Read-across to the open book: **BCC** (Boise Cascade, building products/lumber) is an open long at 81.00.
  Lumber is directly in the crossfire. Needs a look before it is held through 9/8.

## [06:47 ET] OPEN POSITION LEVELS — 2026-08-24 closes, ATR14 and moving averages (source: Nasdaq via market_data.py)
| sym | close | ATR14 | %ATR | SMA20 | SMA50 | 120d hi | 120d lo | off hi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KRE | 74.76 | 1.04 | 1.39 | 76.47 | 75.36 | 78.35 | 61.80 | -4.6% |
| XLE | 63.11 | 1.20 | 1.90 | 60.52 | 57.63 | 64.70 | 52.62 | -2.5% |
| CCJ | 102.27 | 3.44 | 3.37 | 94.89 | 96.21 | 131.21 | 83.15 | -22.1% |
| NKE | 40.75 | 1.07 | 2.63 | 41.42 | 42.39 | 59.49 | 38.86 | -31.5% |
| PFE | 27.97 | 0.61 | 2.16 | 26.46 | 25.40 | 28.75 | 23.62 | -2.7% |
| DHT | 19.72 | 0.71 | 3.60 | 18.87 | 18.33 | 20.62 | 15.98 | -4.4% |
| HD | 337.43 | 8.56 | 2.54 | 342.55 | 340.31 | 369.57 | 289.10 | -8.7% |
| LCII | 104.51 | 3.62 | 3.47 | 105.56 | 102.42 | 138.15 | 89.00 | -24.4% |
| BCC | 82.24 | 2.64 | 3.22 | 82.43 | 78.21 | 88.43 | 65.00 | -7.0% |
- KRE 74.76 against a 74.20 stop — 0.54 away, half an ATR. It is the position most likely to be stopped this week.
- XLE, PFE, DHT all within 5% of their 120-day highs and working. CCJ +7.9%/+16% and reclaimed both MAs.

## [06:52 ET] INSIDERS — swept 33 names, two real clusters (source: Finnhub Form 4, 6-month window)
**NKE — the strongest insider signal in the sweep, and it is an existing position.**
- 5 open-market buys, 4 distinct buyers, $3.73M bought vs $1.20M sold, net +$2.53M.
- The names matter: **Elliott Hill (CEO) 47,320 sh @ ~$42.27 on 2026-04-13**; **Timothy D. Cook (director, Apple CEO)
  25,000 sh @ $42.43 on 2026-04-10**; **Robert H. Swan (director, ex-Intel CEO) 11,781 sh @ $42.44 on 2026-04-07**;
  **John W. Rogers Jr (director, Ariel) 4,000 sh @ $43.34 on 2026-04-09**. A tight four-person April cluster at $42-43.
- NKE closed 40.75 on 2026-08-24 — **below every price the insiders paid**, and -31.5% off the 120-day high of 59.49.
**ELV (Elevance Health) — 4 buys, 3 buyers, $2.24M, and the newest is recent**: 2026-07-17 at $366.05-368.25 (3,725 sh
  across three buyers) plus 3,000 sh @ $289.84 on 2026-03-05. Worth a look — not previously covered by this report.
- Minor: HUM 1 buy @185.21 (2026-02-23), F 1 buy 10,600 sh @14.05 (2026-06-23). Too thin to weight.
- **Zero open-market buys** at: OLLI, GAP, AEO, ASO, ULTA, STLD, WDC, LCII, BCC, KRE, DG, BURL, INTC, ON, MCHP, CVS,
  SBUX, EL, GM, ALB, MOS, CF, NEM, FCX, PARA, WBD, DXCM, MRNA, HSY. Absence is not a negative, but note the heavy
  one-way selling at WDC (102 sells, $29.5M), BURL (51, $15.0M), GAP (18, $23.2M) and **LCII (6, $13.1M — open position)**.

## [06:52 ET] SCREEN — retail is de-rated, software is not (2026-08-24 closes, 120-day windows)
- Discount/off-price: DLTR 136.75 (-0.2% off high — the group leader), DG 125.33 (-19.4%), BURL 330.64 (-12.6%, and
  7.1% BELOW its 20-day into an 8/26 print), OLLI 76.35 (-31.8%), ULTA 538.76 (-20.5%), GAP 20.36 (-27.5%),
  AEO 16.87 (-26.8%), ASO 46.15 (-25.3%), BBY 87.48 (-4.2%), URBN 76.05 (-5.5%).
- Enterprise software into this week's prints is the opposite — extended, not cheap: SNOW +172.9% off its 120-day low,
  PANW +144.5%, GTLB +124.4%, OKTA +109.0%, ESTC +98.0%, WDAY +80.5%, MDB +86.7%. CRM 209.06 is 1.9% off its high,
  ADSK 254.42 is 3.9% off, ESTC 5.6%, SNOW 5.6%, GTLB 4.1%.
- **REJECTED — long software into this week's prints (CRM, WDAY, SNOW, PANW, ESTC, GTLB, OKTA, MDB, ADSK)**: every one
  is within 6% of a 120-day high after a 80-170% run off the low. Buying an extended name into a binary print is not a
  setup, and I have no differentiated view on any of these numbers.
- Memory is the violent one: MU 910.43 (-5.83% on 8/24, -27.5% off the 1255 high but still +192% off its low),
  SNDK 1493.12 (-6.45%, -36.6% off high, 9.0% ATR), WDC 435.38 (-5.24%, -45.6% off high, 9.2% ATR).
  Drivers: peer capital-return disappointment in Asia, DRAM/NAND pricing-power-peak downgrades, talk of US rules
  allowing Chinese NAND/DRAM sourcing, and rising Treasury yields raising hyperscaler financing costs.
  source: https://www.fxleaders.com/news/2026/08/24/mu-stock-falls-below-900-as-memory-demand-china-competition-and-spending-risks-mount-for-micron/
- **REJECTED — memory (MU, WDC, SNDK) either way**: 6-9% ATRs, a live regulatory headline risk with no date, and no
  edge on where DRAM pricing peaks. Position sizing that survives a 9% ATR stop makes the trade too small to matter.

## [06:50 ET] CATALYST — Section 338: a 50% US tariff on Canadian PANELS took effect 2026-08-19 and BCC has not moved
- Trump issued three proclamations under **Section 338 of the Tariff Act of 1930 on 2026-07-20**, imposing **50% tariffs
  on Canadian plywood, wood veneers, laminated veneer lumber (LVL) and MDF, effective 2026-08-19**. These panel products
  had until now largely escaped the softwood-lumber duty regime. Dimensional softwood lumber is *spared* by Section 338.
  sources: https://kcma.org/insights/president-trumps-new-section-338-tariffs-products-canada ,
  https://woodcentral.com.au/section-338-tariffs-canada-lumber/ ,
  https://www.indexbox.io/blog/us-announces-50-tariffs-on-canadian-wood-products-raising-housing-cost-concerns/
- Escalation: US-Canada talks collapsed 2026-08-21; a further 50% on ~$20B of Canadian goods (electronics, industrial
  machinery, dairy) took effect 00:01 ET 2026-08-23. **Canada retaliates 2026-09-08, dollar-for-dollar, on US steel,
  dairy, appliances, agricultural machinery, paper and electronics.**
  sources: https://www.aljazeera.com/news/2026/8/22/us-imposes-50-tariffs-on-20bn-worth-of-canadian-goods-after-talks-fail ,
  https://www.npr.org/2026/08/22/nx-s1-5941584/us-canada-tariffs
- **The price reaction in the obvious beneficiary is zero.** BCC: 08-19 83.13, 08-20 81.77, 08-21 82.47, 08-24 82.24.
  The tariff went live on the 19th and the stock is down 1.1% since. WY 24.39 (-1.4% over the same four sessions),
  UFPI 89.23 (-1.3%). Nobody has repriced the panel complex.
- BCC Q2 2026 (reported 2026-08-03): sales $1.831B +5%, net income $57.3M, diluted EPS $1.63, adj EBITDA $126.2M,
  BMD EBITDA $85.6M, **Wood Products EBITDA $52.4M vs $37.3M a year ago (+40%)**, 35.2M diluted shares,
  cash $304.8M, total debt $452.5M. **Plywood net price $393/Mft, +15% y/y**, volume 368MMft vs 356MMft.
  EWP was the weak spot: I-joist pricing -7%, LVL -4% — and LVL is exactly what the 50% tariff now covers.
  sources: https://www.stocktitan.net/news/BCC/boise-cascade-company-reports-second-quarter-2026-w2rkx06awvdp.html ,
  https://www.sec.gov/Archives/edgar/data/1328581/000132858126000027/bcc-20260630.htm
- Second, separate positive: **BCC became sole nationwide distributor of James Hardie's full portfolio effective 2026-07-31.**
- Valuation: 82.24 x 35.2M = ~$2.90B market cap; net debt ~$148M; EV ~$3.04B. Annualising Q2 adj EBITDA gives ~$505M,
  so **EV/EBITDA ~6.0x**. 400-day range 65.00-131.27; stock is 37.4% below the 18-month high; SMA200 76.71.
- Management's own Q2 language flags "duties, tariffs" as a pricing driver — they see it coming.

## [06:55 ET] REJECTED — JELD — the tariff read was wrong, and I checked before trading it
- JELD-WEN went 1.84 (08-18) -> 2.04 (08-19, vol 3.02M vs ~1M normal) -> 2.08 -> 2.30 -> 2.49 (+8.3% on 08-24).
  +35% in four sessions beginning on the exact day the Section 338 panel tariff took effect. It looked like the
  purest tariff beneficiary in the group.
- **It is not.** JELD-WEN is a net importer: the company guides an annualised tariff impact of about **-$14M** at a 10%
  rate, i.e. tariffs are a cost line, not a benefit. The real drivers of the move are Q2 (2026-08-04): revenue $818M,
  adj EBITDA $42M at a 5.2% margin — its **first y/y adjusted EBITDA increase in ten quarters** — an adjusted loss of
  $0.11 against $0.14 expected, and a lifted outlook.
- The balance sheet is why this is not a buy at 2.49: **net debt leverage 11.3x**, projected **2026 FCF use of -$75M**,
  and management "actively evaluating options to address near-term maturities" with advisers. That is a refinancing
  option, not an equity. 400-day range 0.925-10.09, so the stock is 75.3% below its high.
- Liquidity is fine (1.74M sh x $2.49 = ~$4.3M/day, well clear of the $500K floor) and it would size as a 1% lottery
  ticket. It is rejected on entry quality and thesis quality, not on size: chasing +35% in four sessions into an
  11.3x-levered refinancing binary is a bet on a headline I do not have.
  sources: https://www.investing.com/news/company-news/jeldwen-q2-2026-slides-productivity-gains-drive-first-ebitda-rise-in-10-quarters-93CH-4834417 ,
  https://www.sec.gov/Archives/edgar/data/1674335/000167433526000123/jeld-20260627.htm
- WATCHLIST-WORTHY: if JELD announces a completed refinancing of the near-term maturities, the equity re-rates on the
  news and the leverage stops being the story. That is the trigger; do not pre-position for it.

## [06:55 ET] TARIFF LOSERS — Canada retaliates 2026-09-08 on steel, dairy, appliances, ag machinery, paper, electronics
- **DE 648.64** is the awkward one: -1.8% off its 120-day high after running 580.63 -> 620.94 -> 647.47 -> 648.64
  (+11.7% in three sessions) on its own print, straight into a dated Canadian tariff on agricultural machinery.
  A short into that is tempting and I am not taking it: shorting a name three days after a strong beat, on margin,
  against a tariff list that has not been published in detail yet, is a guess dressed as a catalyst. REJECTED, noted.
- Others in the retaliation crosshairs, for the record: NUE 244.64 (-12.7% off high, below the 20-day at 263.23),
  CLF 11.30 (-25.0%, 6.1% ATR), AGCO 110.13 (-18.1%), CNH 11.76 (-2.9% off high), WHR 40.13 (-35.1%),
  IP 41.04 (-8.4%), PKG 248.88 (-4.3%). No trade taken — the product list is not published yet, so the exposure
  per name is a guess. Revisit when Canada publishes the schedule.
- Homebuilders pay the panel tariff as a cost: DHI 148.97 (-12.8% off high), LEN 88.16 (-18.1%), TOL 147.45 (-11.3%),
  NVR 6397.59 (-12.8%), PHM 129.61 (-7.5%). All already below or near their 50-days, so the short is late.
  Kalshi KXFM30YMTG-26DEC31-T5.75 trades 4/11c: the market gives roughly a 4-11% chance the Freddie Mac 30-year
  mortgage is below 5.75% at 2026 year-end. Financing costs are not coming to the rescue. This is also the concrete
  bear case for the BCC idea above, and it is why BCC is sized as a 3% accumulation rather than a swing.

## [07:00 ET] POSITION UPDATES — captured (6-11)
- `BCC` — thesis upgraded to long_term on the Section 338 panel tariff + James Hardie sole-distribution win. The 76.00
  stop is deliberately removed and replaced with a stated invalidation. Accumulate 74-80, not at 82.24. captured.
- `NKE` — continuing accumulation. New evidence: the April insider cluster (CEO Hill, Cook, Swan, Rogers) at $42.27-43.34,
  all now underwater with the stock at 40.75, 55% off the 2-year high and 4.6% above the 2-year low of 38.86. captured.
- `KRE` — CLOSE. 74.76 against a 74.20 stop is half an ATR; curve flattened to +0.46; two prior KRE lots already
  stopped out on 08-19. Fourth pitch in ten days, and the rate thesis has inverted. captured.
- `XLE` — HOLD, raise all three stops from 57.80/58.60/59.20 to 60.20 (just under the 20-day at 60.52), making the
  position free. Explicitly DO NOT ADD at 63.11 with the 120-day high 2.5% away. captured.
- `DHT` — HOLD through the Frontline print 2026-08-31 BMO; raise the stop 17.60 -> 17.90. Entry level unchanged at
  19.40 for new money (has not filled twice). captured.
- `NVDA` — NEW, conditional. Buy only the post-print flush into 190-201 and only if revenue and the October guide are
  at or above consensus. stop 182, target 236. captured.
- `KXFEDDECISION-26SEP-H25` — NEW, conditional. Do NOT buy at 34 today. Buy 38-52 only after a non-dovish Warsh on
  2026-08-28. captured.

## [07:00 ET] POSITION UPDATES — HOLD, no change, not separately captured
- `CCJ` 102.27 (+7.9% from 95.00, +16.2% from 88.00), target 135, no stop. Reclaimed both the 20-day (94.89) and
  50-day (96.21) and is 22.1% below the 120-day high of 131.21. Nothing has changed in the uranium thesis and there is
  no dated catalyst inside the horizon. HOLD. No new money — it has been pitched 3x in ten days and is 8% above the
  most recent entry.
- `PFE` 27.97 (+8.4% from 25.80), target 38, long_term. 2.7% below the 120-day high of 28.75, above both MAs. HOLD.
- `HD` 337.43 against entries of 337.49 and 340.00 with a 328.00 stop. Flat, but below both the 20-day (342.55) and
  50-day (340.31). It is the position most exposed to today's macro on both sides: a hiking Fed and a 30-year mortgage
  the market does not expect below 5.75% this year hurt the demand side, while the 50% Section 338 panel tariff raises
  the cost of the plywood and EWP it sells. HOLD only because the 328 stop is 1.1 ATR away and still valid — but it is
  the next position to go if it loses 328. Do not add.
- `LCII` 104.51 (+11.2% from 94.00), target 138, no stop. **Flagged**: six insider sales totalling $13.1M in six months
  and zero open-market buys, in a rate-sensitive RV maker 24.4% below its 120-day high. Working, but the insider tape
  is one-way. HOLD with a mental stop at the 50-day (102.42); do not add.

## [07:03 ET] CRYPTO — why the short died, and why I am not flipping long
- BTC went from under $65,000 to ~$79,500 between 2026-08-19 and 08-21, a ~24% week — the biggest in over two years.
  Now $79,266, +1.7% in 24h. ETH $2,476.86 (+0.04%), SOL $99.47 (+4.82%).
- Five drivers, and two of them are dated: (1) **the US Treasury announced on 2026-08-19 it will double long-term bond
  buyback operations from $2B to $4B per operation starting 2026-09-09**; (2) the break above $65,000 triggered the
  largest short-liquidation cascade since November 2021, **over $3B in 24 hours, ~92% of it bearish positions** — that
  is literally what happened to this report's short; (3) record spot-ETF inflows, BlackRock taking 83% of $606M in a
  single day; (4) a White House crypto meeting and stated support for the **CLARITY Act ahead of its September vote**;
  (5) dollar weakness. sources: https://blog.bit2me.com/en/bitcoin-rally-august-2026-key-drivers/ ,
  https://www.benzinga.com/crypto/cryptocurrency/26/08/61352060/bitcoin-taps-79000-up-20-since-monday-so-why-should-bulls-be-careful
- **REJECTED — long BTC / long /MBTU6.** Buying after a 24% week driven substantially by forced short covering is the
  mirror image of the mistake already made. No new crypto exposure today in either direction.
- **HONEST COUNTERPOINT to the TLT close above**: the Treasury doubling long-bond buybacks from 2026-09-09 is a genuine
  bid for duration and cuts against that recommendation. It does not change the call — $4B per operation is small next
  to issuance and the rate market still prices zero cuts across three meetings — but it belongs on the record.

## [07:03 ET] NUCLEAR — the story stocks died, the producer did not
- SMR 9.05 (**-84.2%** from 57.42), OKLO 39.69 (-79.5% from 193.84), NNE 18.27 (-70.0% from 60.87),
  LEU 177.14 (-61.8% from 464.25) — the pre-revenue SMR complex has been destroyed over 250 sessions.
- Against that, **CCJ 102.27 is only -24.4% off its high and above both MAs**, and UEC 12.51 is 14.9% above its 20-day
  on $124M/day. The producers with cash flow held; the narrative names did not.
- This is direct support for HOLDING CCJ and for never having owned the SMR names. No new position — CCJ is already
  open twice and 8% above the most recent entry, and adding a second uranium name would breach the correlation cap.

## [07:06 ET] REJECTED — AGX — the insider check earned its keep a second time
- Argan looked like the best new idea on the screen: 468.98, **-41.8% off its 805.75 high**, far below its 20-day
  (559.61) and 50-day (626.84), $200.8M/day of dollar volume, earnings 2026-09-02 (consensus EPS 2.69 on $303.6M),
  and a business — building gas-fired generation — sitting directly under the datacenter power buildout.
- Then the insider tape: **26 open-market sales totalling $126.6M in six months, zero purchases.** Form 144s filed
  2026-06-22, 06-23 and 07-31 with Form 4s following each.
- And the price action is distribution, not a flush: 617.68 (08-04) -> 592.66 -> 578.51 -> 553.03 -> 528.01 -> 516.58
  -> 501.63 -> 468.98 (08-24), with volume *rising* into the decline (428K on 08-24 against a 137-300K baseline).
  Eleven consecutive lower closes on increasing volume is someone getting out.
- The bullish material I could find — a $2.9B backlog, three years of visibility — dates from the Q4 FY2026 call in
  March 2026 and explains nothing about August. I could not identify what changed, which is itself the answer.
- **REJECTED.** A -24% three-week slide into a print, against $126.6M of insider selling and no explanation I can
  source, is a falling knife. Revisit after the 2026-09-02 print, not before.
  sources: https://stockanalysis.com/stocks/agx/ , https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000100591&type=4
- Scorecard on the insider screen today: it produced the NKE thesis and it killed the AGX one. Worth running first,
  not last.

## [07:07 ET] EVENT CONTRACTS — hunted properly, one kept, one killed by its own arithmetic
- Kalshi's search endpoint is unusable (see the tooling bug above), so I walked series tickers directly. Almost every
  open market has zero 24h volume; scanning 200 open markets returned none above 5,000 contracts of 24h volume.
  The genuinely liquid, Robinhood-listed families are the FOMC decision series and the bitcoin price series.
- **KEPT (as a wait): KXFEDDECISION-26SEP-H25.** Captured above. Sep hold 65/66, hike-25 33/34, cut 0/1.
- **REJECTED — KXBTCMAXY-26DEC31-99999.99, "How high will Bitcoin get in 2026 / above $100,000".**
  This is a real, liquid, Robinhood-listed market (Kalshi 36 bid / 37 ask, 9,628 contracts of 24h volume; Robinhood's
  own page displays it around 39%, with Above $120,000 at 27% against Kalshi's 18/19).
  source: https://robinhood.com/us/en/prediction-markets/crypto/events/661d5219-00cc-43bd-893a-a1f21deaee1d/
  The idea was that this is a *barrier* contract — bitcoin only has to TOUCH $100,000 once before 2026-12-31 — and that
  the market prices it with terminal-price intuition. From $79,266 that is a 26.2% move with T=0.353 years. Running the
  standard first-passage probability for a driftless GBM:
      ann vol 40% -> 29.1%     ann vol 50% -> 38.5%     ann vol 60% -> 45.5%
      ann vol 45% -> 34.1%     ann vol 55% -> 42.2%     ann vol 70% -> 50.9%
  Bitcoin's annualised vol realistically sits in the 45-60% band, which puts fair value at **34-46% against a market at
  36-39%.** **There is no edge.** The market has this right and my "the crowd confuses touch with terminal" story was
  wrong. Rejected on the arithmetic, not on a feeling — and it is logged here so nobody re-litigates it tomorrow.
- Note the consistency check this also passes: having been wrong on bitcoin four times from the short side, the
  temptation is to flip. The arithmetic says there is nothing here, so nothing is what gets traded.

## [07:08 ET] SMALL CAPS — hunted, and none of them clear the exit test
The insider screen was run across twelve small and micro caps with catalysts inside the horizon (DAKT, MBUU, TITN,
SVRA, CULP, SPWH, ZUMZ, JILL, SHOE, CAL, VRA, DLTH). Two produced genuine buy clusters and both die on liquidity:
- **CULP** — 11 open-market buys by 5 distinct insiders, $120,972, **zero sells**, most recently 2026-07-13 at $3.45.
  Stock 3.45, 28.1% off its 250-day high, sitting on its 20-day (3.44) and 200-day (3.38), earnings 2026-09-02.
  A textbook cluster. **REJECTED: 15-day average dollar volume is $0.05M — one tenth of the $500K floor.** The
  position could not be exited. This is the floor doing exactly what config/universe.md says it is for.
- **VRA (Vera Bradley)** — 2 buyers, $204,821 on 2026-06-12 at $3.73/$3.87, zero sells, now 3.17 (below both buys),
  27.8% off the high, earnings 2026-09-02. **REJECTED: 15-day ADV $0.34M, still under the $500K floor.**
- DAKT: 1 token buy of $1,565 against $148K net selling — noise, not a signal. MBUU, TITN, SPWH, JILL, SHOE, DLTH:
  no insider activity either way. SVRA (already on the awaiting-entry list at 5.35, now 5.56): one insider SALE of
  $2.24M and no buys — worth knowing before anyone adds to it.
- **There is no small-cap idea in today's report and that is the honest outcome**, not an oversight. The two names
  that passed the thesis test failed the exit test, and a position that cannot be sold is worth nothing.

## [07:08 ET] LANES DELIBERATELY LEFT EMPTY
- **No intraday idea.** There is no US economic release today; the week's macro is front-loaded onto Wednesday
  (PCE, Q2 GDP second estimate, durable goods, consumer confidence) and Friday (Warsh). Manufacturing an intraday
  setup on a day with no catalyst would be padding.
- **No new crypto exposure**, long or short — see the bitcoin block above. The only crypto entries are exits.
- **No healthcare idea.** ELV was the one that surfaced, on a 3-buyer insider cluster at $366-368 on 2026-07-17,
  but it has already run to 402.63 (+9.9% above the insider prices) and 7.7% off its high. The edge was real and is
  now largely realised. Watchlist, not a trade.
- **No second housing or building-products name** beyond BCC, and no second uranium name beyond CCJ — the
  correlation cap in config/strategy.md, applied deliberately rather than discovered afterwards.

## [07:09 ET] RESEARCH COMPLETE
- candidates: 12 (in reports/2026-08-25/candidates.jsonl)
  - 4 mandatory/urgent CLOSES: /MBTU6 (cover the short), BTC (abandon the spot short), TLT (close the long),
    TJX (close, stop breached 4 sessions ago), plus KRE (close) = 5 exits in total
  - 4 new or restated ideas deploying capital: BCC (long_term, the unpriced Section 338 panel tariff — the best
    new work of the day), VST (long_term, level unchanged from yesterday, unfilled), NKE (long_term, insider cluster),
    NVDA (swing, conditional on the print)
  - 1 conditional event contract: KXFEDDECISION-26SEP-H25, explicitly WAIT until after Warsh on 2026-08-28
  - 2 position holds with changed risk: XLE (raise all three stops to 60.20), DHT (raise stop to 17.90, hold into FRO)
- Also decided and logged but not separately captured: CCJ hold, PFE hold, HD hold (next to go if 328 breaks),
  LCII hold with a flag on $13.1M of one-way insider selling.
- Rejections logged with reasons: AGX ($126.6M insider selling into an 11-day slide), JELD (the tariff read was
  backwards — it is a $14M cost to them, and the balance sheet is 11.3x levered), CULP and VRA (real insider
  clusters, both fail the $500K dollar-volume floor), DE short (tariff list not published), memory (MU/WDC/SNDK,
  6-9% ATRs and no edge), software into this week's prints (all within 6% of highs), homebuilders (short is late),
  KXBTCMAXY 100k (fair value 34-46% vs a market at 36-39% — no edge, shown with the arithmetic).
- Coverage gaps: no live index, VIX, DXY, oil or gold futures print all session — Yahoo returned HTTP 429 across
  every symbol and Finnhub refuses CFD indices, so market_context levels must come from the CNBC 2026-08-24 close
  (SPX 7,652.86, Nasdaq 25,980.19, Dow 53,417.16) and be labelled as a prior close in a closed market, not a live
  quote. No 30-year yield read. No Canadian retaliation product schedule (not published yet).
- Sources that failed: Yahoo Finance (429, all symbols); Finnhub for indices (subscription); Stooq (404 on ^-prefixed
  index symbols); Alpha Vantage (no API key); CNBC and Substack to WebFetch (403); `market_data.py events` (returns
  parlay junk and null prices — Kalshi renamed the price fields to `*_dollars`; this needs a one-line fix).
- Every price in this file and in candidates.jsonl was fetched. Where a number could not be fetched it is not stated.

## [07:12 ET] FALSIFICATION PASS — two candidates changed on their own arithmetic
- **XLE** was captured with entry 60.20 and stop 60.20, which is a data error that makes reward-to-risk undefined.
  Re-captured: existing lots' stops go to a single 59.90 (just under the 20-day); the 60.20 add level for NEW money
  carries a 57.40 stop, below the 50-day at 57.63, since a new tranche has no profit cushion. R:R 2.43.
- **VST** was captured at the 134.00 level published yesterday. Against a defensible 108 bear case that is
  (190-134)/(134-108) = **2.15 to 1, below the 2.5 long-term floor.** The wrong fix is to raise the target or soften
  the bear case; the right fix is to demand a better price. Re-captured at 128.00, which gives 3.10 to 1.
  Yesterday's 134.00 level was marginal on this measure and is superseded.
- Final reward-to-risk spread, recomputed from the captured entry, target and downside: BCC 2.91, NVDA 2.86,
  KXFEDDECISION 2.75, NKE 2.74, XLE 2.43, VST 3.10, DHT 2.07. Spread across the range rather than clustered at
  the floor, which is the failure mode this report has had before.
- The five exits (/MBTU6, BTC, TLT, TJX, KRE) carry entry == target by construction because they are closes, not
  trades. They will fail validate_report.py and be demoted to the watchlist. **They are actions for today.**

## [07:16 ET] LAST SWEEP — panel *consumers* checked as the mirror trade, nothing taken
If the 50% Section 338 tariff on Canadian plywood/veneer/LVL/MDF is a margin gain for BCC, it is a margin cost for the
US manufacturers that buy those panels. Checked the listed ones:
- PATK 85.12 — **-42.7% off its 148.50 high**, 4.7% above its 250-day low of 81.29, below all three MAs. Already priced.
- LZB 32.12 — fell from a 39.60 20-day to 32.12, now 10.6% above its 250-day low. Already broken.
- TREX 47.27 (-28.4% off high, composite decking, limited wood-panel input). PATK/TREX/LZB: the short is late.
- **MHK 134.07** is the only one still intact — 6.3% off its high, above its 20-day (132.13), 50-day (120.57) and
  200-day (112.85), $123.7M/day. It is the cleanest expression of the cost side, and I am **not taking it**: there is
  no dated catalyst, shorting an uptrend requires margin, and I have no evidence on Mohawk's specific Canadian panel
  exposure. Recording it as the idea I looked at and passed on, so tomorrow starts from here rather than from scratch.
- AMWD and AZEK: history source returned no data. Unchecked — a real gap in this sweep.

## [07:17 ET] FINAL — research phase ends here
- 12 unique candidates in reports/2026-08-25/candidates.jsonl (14 lines; XLE and VST each appear twice because both
  were re-captured after the falsification pass — synthesis should take the LAST entry per symbol).
- The single most important line in this file: **/MBTU6 must be covered and the BTC spot short abandoned.** That
  instruction was issued on 2026-08-24 at 77,915 and was not executed; bitcoin is now 79,266. It is not a watchlist item.
- The best new work is BCC: a 50% tariff on exactly the products the company makes took effect 2026-08-19 and the
  stock is down 1.1% since. If one idea in this report is worth the reader's attention, it is that one.
- Research ran 06:35-07:17 ET, about 42 minutes, and finished inside its budget rather than being cut off.
  `truncated` should be false. The [HH:MM ET] headings early in this file drift up to ~6 minutes fast because the
  first few were estimated before I started checking `date`; every price and level in them was fetched.
