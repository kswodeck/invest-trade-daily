# Research log — 2026-11-16

## [06:03 ET] MACRO — a bear steepener is the regime
Source: FRED via `market_data.py macro` (asof 2026-11-16T11:01Z)
- US10Y **5.10%** (2026-11-12) — source: https://fred.stlouisfed.org/series/DGS10
- US2Y **4.86%** (2026-11-12) — source: https://fred.stlouisfed.org/series/DGS2
- Fed funds effective **3.88%** — source: https://fred.stlouisfed.org/series/DFF
- 10y-2y **+0.27** (2026-11-13), prev +0.24 → steepening — source: https://fred.stlouisfed.org/series/T10Y2Y
- Unemployment **4.1%** (Oct), prev 4.2% — source: https://fred.stlouisfed.org/series/UNRATE
- CPI index 337.476 (Oct) vs 336.298 (Sep) = **+0.35% MoM**, ~4.3% annualized — source: https://fred.stlouisfed.org/series/CPIAUCSL
- TLT 79.38, -0.43% pre (finnhub) — our open TLT long is underwater

**Read:** the 10y sits 122bp ABOVE the funds rate with the curve steepening and
CPI running hot MoM. That is the long end demanding term premium, not pricing
cuts. Duration longs (TLT) are fighting this; it is a headwind we already own.

## [06:03 ET] DATA GAP — index/commodity quotes down
- Yahoo returning **429 Too Many Requests** on every index; finnhub refuses
  indices ("Market data subscription required for CFD indices"); stooq 404s on
  `^` symbols; no alphavantage key.
- FAILED: spx, ndx, dow, russell2000, vix, es/nq futures, DXY, us10y quote,
  gold, wti. Only bonds_20y (TLT) returned.
- Consequence: no live index level, no VIX. Must set equity levels from
  `history` (different path) and verify it works before trusting any level.

## [06:06 ET] CALENDAR — retail earnings week plus NVDA
Source: `market_data.py earnings` (finnhub calendar, fetched 06:05 ET)
Dated events inside the horizon, verified on the fetched calendar:
- **Mon 11/16 AMC: ACM** ← WE HOLD THIS, +5.6%. Decision required today.
- Mon 11/16 BMO: TSN, PDD, BIDU, XPEV; AMC: PARA
- **Tue 11/17 AMC: NVDA** — the week's dominant single event
- Tue 11/17 BMO: HD, DIS, WSM, VIK, KLAR, AS, TME, GFF, ATKR, ENR, SR
- Wed 11/18 BMO: LOW, TGT, TJX, ZIM, GLBE, GLNG, GDRX; AMC: PANW, KLIC, WWD, SNEX, NJR, UGI, SBLK; also ROST, CPRT, GAP, BBWI
- Thu 11/19 BMO: WMT, BABA, FUTU, NTES, VVV, WMG, MMS, ROAD; AMC: INTU, KEYS, ESTC, POST, GLOB, HP
- Fri 11/20 BMO: BJ
- Mon 11/23: **DKS** (we have DKS awaiting entry @144.5), ANF, BURL
- Tue 11/24: ADI, ADSK, DELL, HPQ, MDT, WDAY, SJM | Wed 11/25: DE

**Regime consequence:** this is a consumer/retail read week (HD, LOW, TGT, TJX,
ROST, WMT, BJ, GAP, BBWI) landing on top of a bear-steepened curve and hot CPI.
The correlation cap matters: a basket of retail longs is one bet on the consumer.
Of our open positions only ACM reports inside the window.

## [06:14 ET] POSITION UPDATE — ACM — opened 2026-11-07 @66.74, +5.6% at 70.50
- **reports TONIGHT 11/16 AMC** (fetched calendar, not memory)
- decision: **cut to half size before the 16:00 close; stop UNCHANGED at 61.50**
- why: +21% off the 10/19 close (58.02) in under a month; four sessions stalled
  at 70 with a 73.20 thrust on 11/12 rejected to a 70.11 close; and the prior
  quarter was a **-133.8% miss** (-0.50 vs 1.48 est) — source:
  https://finnhub.io/api/v1/stock/earnings
- analyst revisions **deteriorating**: bullish share 76.5%, -6.8pp since Aug
  (buy count 11→9) — source: https://finnhub.io/api/v1/stock/recommendation
- insiders: 3 open-market buys, $699K, 3 distinct buyers — but May/June 2026 and
  struck at 70.63-71.12, i.e. ABOVE spot. Stale; not counted as fresh support.
- deliberately did NOT raise the stop: 61.50 is 4.1 ATR out and clears the 2.0
  floor. Tightening into an earnings gap is the KRE failure mode in CLAUDE.md —
  it improves the printed ratio and makes the trade strictly worse.
- action: captured via add_candidate.py (conviction 4, half size)

## [06:17 ET] ACT AT THE OPEN — TWO CLOSE INSTRUCTIONS ON MONEY AT RISK
These are **exits on existing positions**, not new ideas. Neither can be a
candidate: a close has no target, so it cannot clear a reward-to-risk floor.
Synthesis must surface both at the top of the report anyway — they are the
highest-value instructions of the day and the only ones about money already lost.

### CLOSE #1 — BCC (Boise Cascade) — opened 2026-08-18 @76.50, **-16.8%** at 67.39
- **no stop was ever set** on this position, and it is 89 days old
- source: https://api.nasdaq.com/api/quote/BCC/historical
- five consecutive down sessions: 72.57 → 70.42 → 69.52 → 67.92 → 67.39
- **-23.8% off the 150-day high (88.43) and only 3.7% above the 150-day low (65.00)** — it is making new lows, not basing
- below a falling 20-day (74.27) and 50-day (75.03); ATR14 3.53 (5.24%)
- the standing target of 110.0 is **+63% from spot** — that is not a target, it
  is an anchor to the 2026-08 entry price, and it is why no stop ever got set
- **the macro moved against it**: 10y at 5.10% and steepening is a mortgage-rate
  regime, and BCC sells wood products into housing starts
- **decision: CLOSE at the open. Do not average down.** A 16.8% loss with no
  stop, at new lows, against a worsening rate backdrop, is the position this
  report's -6.2% average is made of.

### CLOSE #2 — TLT — opened 2026-11-04 @80.30, -1.1% at 79.38
- **the thesis is falsified by this morning's own macro pull**, which is the only
  honest reason to close a 3-day-old position at a small loss
- long duration needs the long end to rally. Instead: 10y **5.10%**, 122bp ABOVE
  the 3.88% funds rate, with 10y-2y **steepening** to +0.27 from +0.24, and CPI
  at **+0.35% MoM (~4.3% annualized)** — sources:
  https://fred.stlouisfed.org/series/DGS10 ,
  https://fred.stlouisfed.org/series/T10Y2Y ,
  https://fred.stlouisfed.org/series/CPIAUCSL
- price confirms: 81.96 → 80.88 → 80.92 → 79.72 → 79.38, below the 20-day
  (81.09) and 50-day (80.21), 3.9% off the 150-day low of 76.43
- **the stop is unworkable**: 78.80 is 0.58 below spot = **0.76 ATR** (ATR14
  0.76), far inside the 1.8 ATR ETF floor. It is a coin flip on one day's noise.
- **decision: CLOSE at the open.** Taking a 1.1% loss on a falsified thesis is
  the cheapest exit available; waiting for the 0.76-ATR stop is not risk control.

## [06:17 ET] POSITION UPDATE — RTX — hold as-is, no change
- 198.58 vs 199.00 entry (-0.2%); above rising 20-day (196.56) and 50-day (192.80)
- stop 186.00 = 2.26 ATR below spot (ATR14 5.57) — clears the 2.0 swing floor
- no new information, no catalyst inside the window → no amendment, no candidate

## [06:17 ET] POSITION UPDATE — ONON — hold as-is, marginal stop
- 33.63 vs 34.20 entry (-1.7%); gapped -7.5% on 11/10 (37.53 → 34.70)
- below 20-day (34.73) but above a rising 50-day (32.16)
- stop 30.69 measured from the 34.20 entry = 3.51 = **1.99 ATR** (ATR14 1.76) —
  passes the 2.0 swing floor only just; would fail if re-entered at spot
- target 41.41 is exactly the 150-day range high — no room above it
- decision: hold, no amendment. Flagging that it is the next position to fail a
  stop-distance check if ATR expands.

## [06:06 ET] TIMESTAMP CORRECTION
The blocks above are stamped 06:03-06:17 by estimate; `date` says the real time
is **06:06 ET**. Tool calls returned faster than assumed. The findings and the
order are correct; only the clock labels ran ahead. All blocks below use `date`.

## [06:07 ET] POSITION REVIEW — the remaining ten, levels all fetched
Source: https://api.nasdaq.com/api/quote/<SYM>/historical
| Sym | Close | vs entry | Stop | ATR14 | vs 20d / 50d | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| PFE | 28.89 | +4.7% | none | 0.80 | below 29.79 / above 28.80 | hold |
| KHC | 25.11 | +9.2% | 21.20 (2.44 ATR) | 0.74 | above both | hold |
| OXY | 58.75 | +8.8% | 50.15 | 1.84 | below 60.50 / below 59.76 | hold, target 62 near |
| HII | 306.24 | +16.9% | **none** | 13.64 | above both | **set a stop — see below** |
| UNP | 302.44 | +4.8% | 277.40 | 6.51 | above both | hold |
| ABT | 108.52 | +5.4% | 97.00 | 3.03 | above both | hold |
| PYPL | 59.28 | +4.9% | 54.10 | 1.69 | above both | hold |
| XLU | 44.04 | +1.7% | 41.80 | 0.60 | above both | hold (rate headwind noted) |
| AAL short | 13.17 | +1.4% | 14.40 | 0.61 | above both — drifting against | hold |

### MANAGEMENT INSTRUCTION — HII — set the missing stop at 278.00
- +16.9% at 306.24 from a 262.00 entry and **carrying no stop at all**, the
  largest unprotected gain in the book
- 278.00 sits just under the rising 50-day (280.52) and is 2.07 ATR below spot
  (ATR14 13.64) — a real level, not a round number, and wide enough to breathe
- **not captured as a candidate on purpose**: a stop above the filled entry makes
  risk negative, so entry/target/stop would compute a meaningless ratio. It is a
  management instruction on an existing fill, same category as the two closes.
- it would lock +6.1% against the 262.00 entry on a 24% off-high name in an uptrend

## [06:07 ET] BIAS CHECK — what the track record actually says
- overall **4/42 hit target (10%), avg -6.2%** — the book is long-biased and the
  longs are not working
- by class: **etf 3/14 (21%) avg -1.9%** vs **stock 1/28 (4%) avg -8.3%**. Single
  names are where the damage is; baskets are roughly flat. n=14 on ETFs is still
  under the ~15 noise floor, so this tilts the bar, it does not set policy.
- **long_term 0/4, avg -15.2%** — worst lane, and BCC (-16.8%, no stop) is a
  member of it. Raise the bar hard here; do not add a long-term single name today
  without a priced bear case.
- conviction 2: 0/6, avg -8.4%. The lottery lane has produced nothing yet.
- consequence for today: prefer baskets and defined-payoff structures over single
  names, and refuse anything that needs the long end to rally.

## [06:14 ET] REJECTED — KXCPIYOY-26NOV event contracts — my model was wrong, the market is right
Worth recording in full because the apparent edge was large and false.

**The apparent mispricing.** Kalshi's CPI-YoY ladder for the year ending Nov 2026
(deeply liquid: 20k-81k open interest per strike) prices, as fetched:
| Strike | Buy YES | 12-yr Nov seasonal base rate |
| --- | --- | --- |
| Above 3.8% | 19c | 83% (10/12) |
| Above 3.9% | 4c | 58% (7/12) |
| Above 4.0% | 2c | 42% (5/12) |
Mechanics (all fetched, none remembered): Nov-2025 NSA base **324.122**, Oct-2026
NSA **337.511**, so >4.0% needs only MoM >= -0.078% against a 12-year Oct->Nov
median of **-0.128%**. Sources: https://fred.stlouisfed.org/series/CPIAUCNS ,
https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXCPIYOY

**Method validated before being trusted.** The settled KXCPIYOY-26SEP market
resolved YES at "Above 3.6%" and NO at "Above 3.7%", i.e. BLS printed **3.7%**;
my same FRED arithmetic gave 3.738%. So the pipeline was right.

**Why the trade is still wrong.** The 12-year seasonal ignores *this* November's
energy complex, and I measured it:
- US regular gasoline: Oct avg **$4.309** -> Nov-to-date avg **$4.074** (**-5.5%**),
  latest weekly print $3.995 (**-7.3%** vs the Oct average) — source:
  https://fred.stlouisfed.org/series/GASREGW
- WTI spot: Oct avg **$102.07** -> Nov-to-date avg **$93.69** (**-8.2%**), latest
  **$89.62** (**-12.2%** vs the Oct average) — source:
  https://fred.stlouisfed.org/series/DCOILWTICO
Gasoline is ~3.5% of the CPI basket, so a 5.5-7% decline alone subtracts roughly
0.19-0.25pp from the headline NSA index. Stack that on the ordinary non-energy
seasonal and you arrive at about the **-0.32% MoM** the ladder is pricing, which
maps to a 3.8% print — exactly where the market is centred.
**Conclusion: no edge. The 2c is correct pricing, not a mispricing.** A 12-year
average is a crude model; 54,864 contracts of open interest against a measured
12% crude decline is not something to bet against on a base rate. No candidate.

## [06:14 ET] MACRO REFINEMENT — the duration selloff is NOT about inflation
This matters because it is the opposite of the obvious read and it *strengthens*
the TLT close rather than undermining it.
- Oil is collapsing (-12% off the Oct average) and the November CPI print is
  therefore set to come in soft, yet the 10y is at **5.10%** and the 10y-2y is
  **steepening** (+0.27 from +0.24).
- Long yields rising *while* the inflation impulse falls means the long end is
  demanding **term premium / absorbing supply**, not pricing inflation.
- Consequence: a soft November CPI will not rescue a duration long, because
  inflation is not what is driving the long end. Closing TLT stands.

## [06:14 ET] POSITION UPDATE — OXY — hold, no amendment (an assumption corrected)
I expected to find OXY had not yet priced the 12% crude decline. Fetched data
says the opposite, so the warning I was about to write would have been wrong.
- OXY already took the hit and bounced: 62.69 (11/02) -> **54.97 low (11/09)** ->
  58.75 (11/13), a 12% fall then a 5.3% recovery over four sessions. The 11/09
  low came within $4.80 of our 50.15 stop and held.
- XLE the same, five green sessions: 61.62 (11/06) -> **64.96** (11/13), back to
  its 50-day (64.99) — rising *while* WTI fell 90.40 -> 89.62. Energy equities
  refusing to make new lows against falling crude is a bullish divergence.
- source: https://api.nasdaq.com/api/quote/OXY/historical
- relative strength says OXY is the energy **laggard**: vs XLE 1m -0.76%, 3m
  -4.29%, 6m -10.75% — source: `market_data.py relstrength OXY --peer XLE`
- decision: **hold, no amendment.** +8.8% at 58.75, target 62 is 5.5% away, the
  stop was tested and held. Note for the record that the position is the weakest
  horse in a sector that just absorbed a 12% commodity shock.

## [06:14 ET] RISK FLAG — AAL short is being undermined by the fuel collapse
- we are short AAL from 13.35 (stop 14.40, target 10.60), now 13.17
- jet fuel tracks crude, and crude is **-12% off the October average**. Fuel is
  roughly a quarter of airline operating cost, so this is a direct margin
  tailwind for the company we are short.
- price agrees: AAL 13.17 is **above both its 20-day (12.90) and 50-day (12.94)**,
  i.e. drifting against the position
- decision: **hold but on notice** — stop stays 14.40 (2.0 ATR on ATR14 0.61).
  Not closed today because the position is still +1.4% and the 14.40 stop is
  intact and workable, unlike TLT's. If AAL closes above 13.60 the fuel tailwind
  has won and the short should go.

## [06:16 ET] REJECTED (and inverted) — long refiners on a widening crack
My first read was that retail gasoline falling less than crude (-5.5% vs -8.2%)
meant widening refining margins. **Retail is sticky and tells you nothing about
the refinery gate.** Fetched spot instead and the sign flips:
- NY Harbor conventional **gasoline spot**: Oct avg $3.0346 -> Nov avg $2.5383
  = **-16.4%**, latest (11/11) **$2.415** — source:
  https://fred.stlouisfed.org/series/DGASNYH
- WTI: Oct avg $102.07 -> Nov avg $93.69 = -8.2%, latest $89.62

**Gasoline crack, computed (42 gal/bbl):**
| | Crude $/gal | Gasoline $/gal | Crack $/gal | Crack $/bbl |
| --- | --- | --- | --- | --- |
| Oct avg | 2.4302 | 3.0346 | 0.6044 | **$25.38** |
| Nov avg | 2.2306 | 2.5383 | 0.3077 | **$12.92** |
| 11/11 | 2.1338 | 2.4150 | 0.2812 | **$11.81** |
**The gasoline crack has roughly halved in two weeks.** Products are falling
faster than the feedstock, so this is margin compression, not expansion.
Long refiners is rejected outright; the honest direction is the other way.

Distillate for completeness — also compressing, from a very high base:
NY Harbor heating oil $4.6954 -> $4.2112 (-10.3%), diesel $4.950 -> $4.468
(-9.7%), implying a distillate crack easing ~$95/bbl -> ~$83/bbl — sources:
https://fred.stlouisfed.org/series/DHOILNYH , https://fred.stlouisfed.org/series/DDFUELNYH

## [06:17 ET] CRACK COLLAPSE IS NOT SEASONAL — worst in 15 years
The obvious objection to shorting refiners is that gasoline cracks always
compress in autumn. Tested it against 15 years of the same two FRED series
(DGASNYH, DCOILWTICO), Oct average vs Nov average, $/bbl:
| Year | Oct | Nov | Change |
| --- | --- | --- | --- |
| 2018 | 14.44 | 11.52 | -20.2% (prior worst) |
| 2019 | 18.62 | 15.46 | -17.0% |
| 2020 | 11.06 | 9.04 | -18.3% |
| 2022 | 38.98 | 35.41 | -9.2% |
| 2024 | 18.38 | 18.76 | +2.1% |
| 2025 | 18.51 | 21.38 | +15.5% |
| **2026** | **25.39** | **12.92** | **-49.1%** |
- 15-year median **-5.7%**, mean **+0.4%**; 2026 ranks **1st worst of 15**
- -49.1% is **2.4x the worst prior year** (2018, -20.2%)
- the $12.92 November level is the 3rd lowest in 15 years, behind only 2020
  (COVID, $9.04) and 2018 ($11.52)
**Conclusion: the margin collapse is abnormal, not calendar.** The seasonal
objection is answered with data rather than dismissed.

**And refiner equities rallied straight through it** — source:
https://api.nasdaq.com/api/quote/VLO/historical
| Sym | 11/06 | 11/13 | bounce | vs 20d | vs 50d | off high | ATR% |
| --- | --- | --- | --- | --- | --- | --- | --- |
| VLO | 346.45 | 379.83 | **+9.6%** | 389.70 | 399.97 | -17.7% | 5.08 |
| MPC | 372.74 | 414.65 | **+11.2%** | 428.40 | 423.94 | -16.1% | 5.10 |
| PSX | 245.72 | 264.90 | +7.8% | 270.83 | 268.90 | -11.5% | 4.31 |
| DINO | 97.18 | 102.18 | +5.1% | 111.34 | 112.52 | -21.0% | 5.87 |
All four are still below both moving averages — this is a bounce inside a
downtrend, not a recovery. VLO is the purest refiner and the most liquid
($1.10B/day), so it is the vehicle to test.

## [06:21 ET] AWAITING-ENTRY RESOLUTION — /MBTZ6 short @74,075 — WITHDRAW the level
- published 2026-11-09, never filled per the tracker; BTC spot now **$64,644**
  (-1.12% 24h) — source: https://api.coingecko.com/api/v3/simple/price
- the 74,075 entry is **14.6% above spot** and will not fill
- BTC fell from **80,443 (11/05) to 64,711 (11/16) = -19.6% in 11 days**,
  accelerating into it: -3.0% on 11/13, -4.3% on 11/14, -6.1% on 11/15
- now only **3.1% above the 120-day low of 62,773**; sma20 74,291, sma50 79,384,
  so price is 13% below its own 20-day — source:
  https://api.coingecko.com/api/v3/coins/bitcoin/market_chart
- **decision: withdraw, do not re-level.** The move the short was built for has
  already happened. Re-pitching it 10,000 lower would be chasing, and chasing a
  -20% move with a 2.5-ATR futures stop (avg daily move 2.58% = ~$1,671) is how
  you buy the bottom of a crash from the wrong side.
- no new crypto candidate today: 3% above a 120-day low after -19.6% offers
  neither a clean short (chasing) nor a clean long (falling knife).

## [06:21 ET] MACRO — crypto is the risk-appetite canary and it is screaming
- BTC **-19.6% in 11 days** while SPY closed Friday only -0.36% at 754.37
- that divergence is worth stating plainly: the most liquidity-sensitive asset is
  repricing hard while equity indices sit near their highs. It is consistent with
  the long-end story (10y 5.10%, term premium rising) draining the speculative
  tail first. Not tradeable on its own today, but it argues against adding
  high-beta risk and for the defensive tilt already in the book.

## [06:21 ET] REJECTED — long XRT / XLY on the cheap-gasoline consumer tailwind
The thesis is real — retail gasoline $3.995 latest vs an Oct average of $4.309
(-7.3%) is genuine disposable income landing exactly on retail earnings week —
but **it is already in the price**, so there is no edge in the basket:
- XRT **91.05**, only **-4.1% off its 94.93 high**, above its 20-day (89.50),
  50-day (86.05) AND 200-day (85.70)
- XLY **119.98**, only **-2.4% off its high**, above all three (117.34 / 113.83 / 115.44)
- source: https://api.nasdaq.com/api/quote/XRT/historical
Buying either 2-4% below the highs, into a week carrying HD, LOW, TGT, TJX and
WMT prints, with the 10y at 5.10% raising every consumer credit cost, is a
momentum chase wearing a macro thesis. No candidate. If the tailwind is tradeable
it has to be in a name that has *not* priced it — screening individual retailers
instead.

## [06:22 ET] REJECTED — TJX long — the most de-rated retailer is de-rated for cause
It screened as the asymmetric candidate: **-21.0% off its high at 134.37**, the
only name in the cohort below its 20-day (140.77), 50-day (136.12) *and* 200-day
(150.46), just 9.4% off its low, reporting 11/18 BMO — a quality off-price
retailer that should win on consumer trade-down plus cheap gas. The evidence
killed it:
- **insiders: 0 open-market buys, 8 sells, net -$27.7M.** Nobody inside is buying
  this de-rating — source: https://finnhub.io/api/v1/stock/insider-transactions
- analyst revisions **deteriorating**: bullish share 77.8%, -6.8pp; strong-buy cut
  11 -> 8, holds 3 -> 5 — source: https://finnhub.io/api/v1/stock/recommendation
- orderly distribution, not a flush: 146.70 (10/23) -> 134.37 (11/13), -8.4% in
  three weeks of lower highs and lower lows, on **rising** volume (9.0M Friday vs
  a 4-6M norm), including a 10.0M-share outside-down reversal on 11/05 that
  opened 146.16, tagged 146.73 and closed 138.59
- source: https://api.nasdaq.com/api/quote/TJX/historical
Buying this two days before a print, with insiders selling and estimates falling,
is catching a knife — the exact pattern `relstrength` is in the workflow to stop.
Not a short either: -21% off the high with a 2-day earnings binary is a coin
flip, not an edge. **No position, either direction.**
Cohort for the record (close / off-high / vs 20d-50d-200d): TGT 161.45 -5.5% above
all; WMT 128.09 -5.2% above all; BJ 110.34 -2.7% above all; ROST 231.68 -9.9% at
MAs; HD 348.69 -12.3% above all; BBWI 21.39 -14.2% above 50/200; LOW 227.73
-22.3% but above 20d/50d and recovering; GAP 21.07 -28.2% below all.

## [06:24 ET] SELF-CORRECTION — the VLO short thesis was overstated. REVISED, not withdrawn.
I checked my own candidate and found the headline number wrong in my favour.
The -49.1% figure is the **gasoline-only** crack. A refiner also sells distillate,
and distillate cracks are extraordinarily high right now, which offsets much of
the gasoline damage. On the industry-standard **3-2-1 crack** (2 bbl gasoline +
1 bbl distillate per 3 bbl crude), computed from DGASNYH, DHOILNYH, DCOILWTICO:

| | Oct | Nov | Change |
| --- | --- | --- | --- |
| gasoline-only crack | $25.39 | $12.92 | **-49.1%** |
| **3-2-1 crack (the right measure)** | **$48.64** | **$36.34** | **-25.3%** |

Two findings, pulling opposite ways, and both must be stated:
1. **The rate of change still ranks 1st worst of 15 years** on 3-2-1 too
   (-25.3% vs a 14-year median of **-2.0%**, mean +3.1%; next worst 2019 at
   -15.1%). The seasonality objection remains answered.
2. **But the absolute level is exceptionally high.** $36.34 against a 14-year
   November median of **$19.24** — the second-highest November in the series
   after 2022's $48.98. Nov levels for context: 2020 $9, 2014-16 $15-16,
   2018 $17, 2019 $18, 2021 $19, 2024 $19, 2023 $26, 2025 $27, **2026 $36**.

**So "margins are collapsing and earnings must fall" is NOT supportable.** VLO is
still earning roughly 1.9x a normal November margin and could post a fine quarter.
The defensible thesis is narrower: a margin **far above normal, reverting at the
fastest rate in 15 years**, with $17/bbl of room down to the median — while the
equity rallied 9.6% in the same week. That is mean reversion from an extreme, not
a cliff, and it is slower and less certain.
**Action: revised VLO entry appended — conviction 4 -> 3, size 2% -> 1.5%, and
the absolute-level objection disclosed in `counter_argument` as a negative I
cannot answer rather than one I have.** The earlier entry stands in the log;
synthesis takes the last entry per symbol.

## [06:24 ET] CORRECTION TO THE AAL FLAG — the fuel rally was attempted and rejected
My 06:14 flag said cheap fuel was undermining the AAL short. Fetched the whole
group and that is too strong — the market already tried this trade and sold it.
Source: https://api.nasdaq.com/api/quote/DAL/historical
| Sym | 11/06 | spike (11/09-11) | 11/13 | gave back |
| --- | --- | --- | --- | --- |
| DAL | 87.20 | **92.20** | 86.25 | -6.5% |
| UAL | 112.74 | **120.56** | 109.31 | -9.3% |
| LUV | 44.45 | 46.48 | 44.94 | -3.3% |
| AAL | 13.18 | **14.16** | 13.17 | -7.0% |
The entire group spiked 11/09-11/11 as crude collapsed, then handed back all of
it by 11/13. UAL is -21.2% off its high and back at its 50-day. A fuel tailwind
the tape refuses to pay for is not a tailwind.
- **and the AAL stop was tested and held by 3.5 cents**: the 11/10 intraday high
  was **14.365** against our 14.40 stop, then it closed back at 13.17
- **decision: hold the short, and I withdraw the "on notice" framing.** The squeeze
  came within four cents of taking us out and failed. Stop stays 14.40. The
  13.60 close-above trigger from the earlier block still stands as the invalidation.

## [06:25 ET] CONSIDERED, NOT CAPTURED — natural gas long into winter
- Henry Hub **$3.00/MMBtu** (11/11), up 24% off the 10/30 low of 2.42; monthly
  averages Aug 2.785, Sep 2.950, Oct 2.988, Nov-to-date 2.737. 2026 range
  **2.42 - 30.72** — the high being a winter spike, so the tail is demonstrated.
  source: https://fred.stlouisfed.org/series/DHHNGSP
- the setup is suggestive: cheap gas, a **distillate crack near $83/bbl** implying
  tight competing heating fuel, and winter ahead
- **not captured.** The thesis needs a weather forecast and I have fetched none;
  "winter is coming" is a category, not a dated catalyst, and nat gas without a
  degree-day view is a guess dressed as a macro call. Recording it as a real
  setup I declined rather than one I missed.

## [06:26 ET] AWAITING-ENTRY TRIAGE — all 9 resolved
Levels all fetched: https://api.nasdaq.com/api/quote/<SYM>/historical
Not re-pitched where nothing changed — they are already tracked as pending, and
re-publishing an unchanged level is the anchoring the repetition guard is for.

### WITHDRAW (3) — the level is stale and chasing it is the error
- **GLD SELL @406.77** (10/25): GLD now **355.45**, so the entry is **14.4% above
  spot**. The short was *right* — GLD is -27.8% off its high and below its 20-day
  (368.78), 50-day (380.91) and 200-day (408.44) — and the move happened without
  us. Withdraw; do not chase a short 14% below where it was published.
- **CVS BUY @79.00** (11/05): CVS now **89.35**, **+13.1% above** the entry. Note
  the sequence — this name stopped us out on 11/04 and was re-pitched at 79.00 on
  11/05, right at the low, then ran 13%. Unreachable now. Withdraw. It sits
  exactly on all three MAs (89.55 / 89.66 / 89.17), which is a decision point, not
  an entry — no new idea here.
- **LEN BUY @79.50** (11/13): **withdraw on consistency grounds.** I am closing BCC
  this morning because the 10y at 5.10% and steepening is a mortgage-rate regime
  that breaks building products. A **homebuilder** long is the same bet with the
  same driver. LEN at 83.61 is -32.7% off its high and below its 200-day (89.92)
  for that reason. I cannot recommend closing BCC on a rate thesis and buying LEN
  into it on the same page.

### KEEP, levels unchanged and still real support (4)
- **XLV BUY @184.00**: now 188.85, above all MAs (183.65/175.05/160.20), only -1.8%
  off its high. The 184 entry sits on the **rising 20-day (183.65)** — genuine
  support, not a reflex discount. Live.
- **HUN BUY @9.00**: now 9.53. The 9.00 entry is the **50-day (9.01)**. -40.8% off
  high; $28M/day is thin but clears the floor — keep it lottery-sized. Live.
- **DKS BUY @144.50**: now 149.70, entry sits on the **20-day (144.09)**. Live, but
  **DKS reports 11/23**, inside a swing hold — the fill and the print may collide,
  and that event risk must be stated if it is republished.
- **CAG BUY @14.40**: now 14.73, entry just under the **50-day (14.45)**. Live.

### CAUTION (1)
- **ADM BUY @68.80**: now 72.90. ADM is below its 20-day (74.97), 50-day (79.82)
  AND 200-day (76.72) — a clean downtrend, -17.9% off high. A buy 5.6% below spot
  in that structure is likely to fill *because* the name keeps falling, which is
  exactly the pullback-entry selection effect in CLAUDE.md. Not withdrawn, but it
  should not be re-pitched without a reason the 68.80 level holds.

## [06:27 ET] MACRO SYNTHESIS — the market is pricing HIKES, and everything agrees
The single most useful number this morning is one I nearly walked past:
**the 2-year at 4.86% sits 98bp ABOVE the 3.88% effective funds rate.**
A 2-year yield that far above the policy rate is not a market pricing cuts — it
is pricing **tightening**. Sources: https://fred.stlouisfed.org/series/DGS2 ,
https://fred.stlouisfed.org/series/DFF
And the macro justifies it: CPI **+0.35% MoM** (~4.3% annualised) and
unemployment **improving to 4.1% from 4.2%**.
Every cross-asset reading I took today is consistent with that one regime:
| Asset | Observed | Fits hike-pricing? |
| --- | --- | --- |
| 10y | 5.10%, 122bp over funds, curve steepening | yes — term premium |
| Gold (GLD) | -27.8% off high, below 20/50/200-day | yes — rising real rates |
| Bitcoin | **-19.6% in 11 days** | yes — liquidity-sensitive tail first |
| Crude | **-16.7%** from 10/30 ($107.56 -> $89.62) | yes — demand/tightening |
| TLT | new lows, below 20/50-day | yes |
| SPY | 754.37, **0.4% off its high** | **NO — the odd one out** |
**The actionable conclusion:** this is a coherent tightening-regime selloff in
everything rate- and liquidity-sensitive, and the equity index has not
participated. That argues for defensive positioning, against adding duration,
against high-multiple and speculative length, and it is why TLT is closed and
BCC and LEN are refused this morning. It is *not* by itself a short-equity
signal — SPY's Friday bar (open 760.07, high 760.12, low 745.20, close 754.37,
a 2% range closing mid after opening at the high) is distribution, but one bar
is not a thesis and I will not publish an index short on it.

## [06:30 ET] SELF-AUDIT — arithmetic, and the ratio-clustering objection pre-answered
Recomputed every number rather than trusting what I wrote:
| Sym | R:R | stop in ATR | floor | baseline win | claimed | edge |
| --- | --- | --- | --- | --- | --- | --- |
| ACM | 2.00 | 2.41 | 2.0 | 0.333 | 0.38 | +4.7pp |
| VLO | 2.00 | 2.38 | 2.0 | 0.333 | 0.38 | +4.7pp |
| GLD | 2.00 | 1.98 | 1.8 (etf) | 0.333 | 0.42 | +8.7pp |
All clear the stop-distance floor; all carry positive expectancy; no claimed edge
exceeds 20pp over baseline, so none is a large claim the thesis cannot carry.

**All three ratios land on exactly 2.00, and that pattern is what got a prior
report in trouble, so here is why it is not the same thing.** The failure CLAUDE.md
records was *targets nudged until they passed*. Here the order was the one the
skill prescribes — stop first from structure, then the floor-implied target, then
a reachability test — and in each case the floor-implied target coincides with a
real level rather than being the reason for it:
- **ACM 77.22** is the pre-existing target on an open position, just above the
  120-day high of 76.85. Not newly derived at all.
- **VLO 296.00** is the 200-day moving average at **294.76**.
- **GLD 336.00** deliberately stops **3% short** of the 300-day low (326.19)
  rather than reaching through it — structure argued for more downside and I
  took less.
And in no case was the stop moved to make a ratio work: ACM's 61.50 is unchanged
from the original fill, VLO's 434 sits above the 10/19 close of 433.31, GLD's 381
above both the 11/09 swing close (379.53) and the 50-day (380.91).

## [06:30 ET] CORRELATION AND SKEW — stated rather than hidden
- today's new ideas are **two shorts** (VLO, GLD) plus **one trim** (ACM), and the
  book also holds a short (AAL). That is a directional lean, not a diversified set.
- VLO and GLD are **two expressions of one regime** — the tightening/commodity
  deflation read in the 06:27 block. Under the 3-per-driver cap, but only just,
  and a dovish surprise or a crude rebound hurts both together. Any further short
  on that driver today would breach the cap.
- **the skew is honest, not manufactured.** Per config I did not add a long for
  balance. The long candidates I examined were rejected on evidence: XRT/XLY
  priced, TJX insider-sold and knife-like, LEN refused on the same rate thesis
  that closes BCC, nat gas unresearchable without weather.

## [06:34 ET] VENUE CHECK — verified at runtime, not recalled
Two of today's three candidates are shorts, so tradeability was checked rather
than assumed (non-negotiable #1).

**Short selling on Robinhood: CONFIRMED, with two caveats.**
Source: https://robinhood.com/us/en/support/articles/short-selling/
- the page describes short selling as "a trading strategy that enables you to
  sell a stock you do not own" and states "you can only execute short sales in a
  **margin account**" — both VLO and GLD are marked `requires_margin: true`
- **caveat 1 — rolling release.** The page says "This is a rolling release, so if
  you don't see short selling yet, check back soon for it." So the feature may
  not be enabled on a given account. Must be checked in-app before the order.
- **caveat 2 — the page says "stock" and never mentions ETFs.** `config/universe.md`
  asserts `sell_short` for ETFs under `Robinhood Stocks`, and the open AAL short
  shows equity shorting is in use, but **ETF shorting is not confirmed by the
  fetched source**. This is a live uncertainty on the GLD idea and I am flagging
  it rather than papering over it. If ETF shorting is unavailable, GLD is not
  actionable as written.

**/MGC micro gold: CONFIRMED available** — 10 troy oz, 1/10th of /GC, $0.10 per
ounce tick ($1/contract) — source:
https://robinhood.com/us/en/learn/articles/what-are-metals-futures/
**But the gold short is deliberately NOT written as /MGC, and the reason is
non-negotiable #2.** `config/universe.md` prefers futures for a bearish gold view
and I am departing from that on purpose:
- this morning's `market_data.py macro` pull **failed on gold** (yahoo 429,
  finnhub "subscription required"), so I hold **no fetched gold futures price**
- pricing an entry, stop and target on /MGC would therefore mean inventing three
  numbers. A fabricated price is worse than a missing one.
- a futures framing also raises the stop floor from 1.8 ATR (etf) to 2.5 ATR,
  which on GLD's 7.597 ATR forces a 328 target — essentially *at* the 326.19
  300-day low. The ETF structure is genuinely the better trade, not just the
  only priceable one.
- if a gold futures quote is available to a later phase, the /MGC expression is
  the config-preferred one and should be re-derived from fetched prices.

## [06:32 ET] WATCHLIST (not actionable today) — LOW — wait for the print
The best long I found, and still not good enough to enter this morning.
- **the only name all day with IMPROVING analyst revisions**: bullish share 72.5%,
  **+4.2pp** — source: https://finnhub.io/api/v1/stock/recommendation
- reliable modest beater: +3.1%, +0.9%, +0.8%, +2.1% over four quarters
- -22.3% off its high at 227.73 yet back above its 20-day (213.43), 50-day
  (199.87) and 200-day (223.57) — a real recovery, not a bounce
- gets the cheap-gasoline consumer tailwind, and **reports 11/18 BMO** (dated)
- **on the housing-consistency question**: this is *not* the BCC/LEN trade. BCC is
  wood products into new construction and LEN builds houses, both driven directly
  by the mortgage rate. LOW is repair-and-remodel against the existing home stock,
  and a 5.10% 10y actually *supports* remodel by locking owners into the homes
  they have. The distinction is real, not a rationalisation.
**Why it is not a position today:** it is +13.9% above its 50-day two days before
a binary print, insiders are net sellers (0 buys, 2 sells, -$2.66M), and improving
revisions is a *single* evidence kind — a conviction-2 case at an extended price
into an earnings gap. Buying that is the chase I rejected XRT for.
**Condition to act: wait for the 11/18 print, then buy a hold of the 20-day.**
For the record HD is the same shape but weaker — bullish 63.0% (+2.1pp), 0 buys
against 4 sells (-$3.34M), and an erratic surprise record (+0.9%, -2.2%, +4.0%,
-5.4%). Not watchlisted.

## [06:32 ET] HOUSEKEEPING — PFE carries no stop and no stated invalidation
- PFE: entry 27.60, now **28.89** (+4.7%), target 42.00 (+45% from spot), **no stop**
- a +45% target with no stop is a `long_term` claim, and per config/strategy.md a
  long-term idea **must** carry an explicit invalidation condition even though a
  hard stop is optional. The tracker shows neither.
- below its 20-day (29.79) though above its 50-day (28.80); ATR14 0.80
- **not fixable from research alone** — I have not done the pipeline work to defend
  a 42.00 valuation anchor or name the development that breaks it, and inventing
  one to fill the field would be worse than flagging the gap. Recording it as a
  real hole in the book for a later run to close.

## [06:36 ET] ACM — earnings DATE IS CONTESTED, and corroboration of the thesis
- the finnhub calendar I fetched says **11/16 AMC**; MarketBeat says the date is
  **not company-confirmed** and estimates **Tue 11/17** — source:
  https://www.marketbeat.com/instant-alerts/aecom-nyseacm-updates-fy-2026-earnings-guidance-2026-08-10/
- SEC EDGAR holds **no 8-K announcing the date**, so I cannot settle it from a
  primary source. Latest ACM filings are a 13G (11/12), 8-Ks (9/16, 9/17), and
  the Q3 8-K + 10-Q (8/10, 8/11) — source:
  https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000868857
- **the instruction is robust to the ambiguity**: "trim to half before the print"
  works whether it lands tonight or tomorrow night, and trimming a day early
  costs nothing. Revised candidate appended saying 11/16-or-11/17 rather than
  asserting a date I could not verify.
- **independent corroboration of the miss**, from a different source than the
  finnhub figure in the original capture: the August reset cut FY26 adjusted EPS
  guidance from **$5.65-$5.85 to $3.95-$4.15** (~30% down) and the quarter missed
  by $1.96 on a -$0.50 actual. Treated as reported-not-primary — I tried to read
  Exhibit 99.1 of the 8/10 8-K and SEC EDGAR refused both the directory listing
  and the index to this client, so I am **not** claiming a `primary_document`
  evidence kind for it.
- attempted and failed: SEC Archives directory listing and index.json for
  accession 0001104659-26-093421 (no JSON returned; EDGAR requires a contact UA)

## [06:36 ET] RESEARCH COMPLETE
- **candidates: 5 entries, 3 distinct symbols** (synthesis takes the last per
  symbol): **ACM** buy/trim conv 4 (entry #5 supersedes #1 — adds the contested
  print date), **VLO** sell_short conv 3 (entry #3 supersedes #2 — the
  self-correction from the gasoline-only crack to the 3-2-1 measure), **GLD**
  sell_short conv 4.
- **plus four instructions on money already at risk that are NOT candidates**,
  because a close has no target and cannot clear a reward-to-risk floor. These
  are the highest-value output of the run and synthesis must surface them above
  the new ideas:
  1. **CLOSE BCC** — -16.8%, no stop, 89 days, five straight down days, 3.7% off
     its 150-day low, target implied +63%
  2. **CLOSE TLT** — thesis falsified by this morning's own macro; the 78.80 stop
     is 0.76 ATR and unworkable
  3. **SET HII'S MISSING STOP at 278.00** — +16.9% and wholly unprotected
  4. **WITHDRAW three stale pending entries** — GLD short @406.77 (14.4% above
     spot), CVS @79.00 (13.1% below spot), LEN @79.50 (refused on the same rate
     thesis that closes BCC); /MBTZ6 @74,075 also withdrawn
- holds reviewed and left unchanged: PFE, KHC, OXY, UNP, ABT, PYPL, XLU, RTX,
  ONON, AAL. Watchlist: **LOW** (wait for the 11/18 print).

### Coverage gaps — what I could not check
- **No implied-move test on any candidate.** `market_data.py implied` returns
  **401 Unauthorized** from yahoo-options, so the prescribed level-setting step
  "is the target inside what options price?" was impossible for all three. None
  of my targets has been checked against market-priced vol.
- **No VIX and no index levels at all** — so no volatility-regime read. The SPY
  distribution comment rests on a single daily bar.
- **No short interest for VLO** (nasdaq ReadTimeout) — materially relevant to a
  short idea, since a crowded short is fuel against it. Unchecked.
- **No `primary_document` evidence on any candidate.** SEC EDGAR refused the
  Archives directory listing and index.json to this client, so I never read a
  filing today. Every idea rests on market data and calendars.
- **Small and micro caps got no dedicated screen.** config/universe.md asks that
  they be hunted deliberately and I did not — the only sub-$2B name touched was
  HUN, and only as an existing pending entry. A real gap, not a judgement call.
- **No long_term candidate and no intraday candidate.** Not manufactured to fill
  the horizon table, per config: nothing in either lane cleared the bar. The
  long_term lane is a genuine omission though — it is 0/4 with avg -15.2% in the
  record and I raised the bar rather than researching it properly.
- Event contracts: researched hard but **no candidate is possible** — see the
  tooling bug below. The CPI ladder was the best opportunity found all morning
  and it was correctly priced.

### Sources that failed
- **yahoo finance: HTTP 429** on every index and commodity — spx, ndx, dow,
  russell2000, vix, es/nq futures, DXY, us10y, gold, wti all unavailable
- **finnhub indices**: "Market data subscription required for CFD indices"
- **stooq**: 404 on all `^`-prefixed symbols; **alphavantage**: no api key
- **yahoo-options: 401** (breaks `implied` entirely)
- **nasdaq short interest: ReadTimeout**
- **SEC EDGAR**: directory listing and index.json refused (needs a contact UA)
- Robinhood futures support article: **404** (worked around via their metals
  learn article, which confirmed /MGC)
- **equity quotes, history, earnings, insiders, analysts, relstrength, crypto and
  FRED all worked** — the run was not data-starved, but it was blind to
  volatility and options pricing.

### Repo bug worth fixing (not a data outage)
`market_data.py events()` returns **null for every price field**. Kalshi's API
now serves `yes_bid_dollars` / `no_bid_dollars` / `last_price_dollars`, and the
function still reads `yes_bid` / `no_bid` / `last_price`. It also fetches at most
200 unfiltered markets and filters client-side, so the sports parlays at the head
of the list crowd out every macro series — searching "CPI", "Fed", "inflation",
"recession" and "unemployment" all returned **count 0** while those series exist
and are deeply liquid. Both are why event contracts cannot be priced through the
tool today; I reached the ladder only by querying
`api.elections.kalshi.com/trade-api/v2/markets?series_ticker=...` directly.
