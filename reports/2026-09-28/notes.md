# Research log — 2026-09-28

## [06:03 ET] MACRO — rates, crypto, regime
Monday 2026-09-28, pre-open. Source: `scripts/market_data.py macro` @ 10:01 UTC.

- **US 10Y 5.18%** (2026-09-24, prev 5.11) — the dominant fact on the page. Long
  end keeps backing up. source: https://fred.stlouisfed.org/series/DGS10
- US 2Y 4.87% (prev 4.85). Fed funds effective 3.88%.
  source: https://fred.stlouisfed.org/series/DGS2
- **10y-2y curve +0.36** (2026-09-25, prev 0.31) — steepening via the long end,
  not via cuts. That is a term-premium/fiscal steepener, not an easing steepener.
  source: https://fred.stlouisfed.org/series/T10Y2Y
- Unemployment 4.1% (Aug, unch). CPI index 334.131 (Aug).
- TLT 79.32, prev close 79.42 (finnhub, session 'closed', asof 2026-09-25T20:00Z,
  age ~3722 min — this is Friday's close, correct for 6am Monday).
- Crypto risk-off: BTC **82,632** -2.66% 24h; ETH **2,640.11** -2.74%;
  SOL **117.70** -5.36%. source: coingecko via market_data.py

REGIME READ: long-end yields at 5.18% with the funds rate at 3.88% is a bond
market repricing term premium while the Fed is already easing. That is a headwind
for long-duration equity and for rate-proxy sectors (utilities, REITs), and it
is the explicit thesis behind the open XLU short and TLT short. Crypto is
selling with it.

## [06:03 ET] DATA GAPS
- Yahoo Finance returning **429 Too Many Requests** on every index symbol, so
  ^GSPC / ^NDX / ^DJI / ^RUT / ^VIX / ES / NQ / DXY / gold / WTI all returned
  ok:false this run. Finnhub has no index entitlement ("Market data subscription
  required for CFD indices"). Equity/ETF single-name quotes via finnhub still work.
- Consequence: no live VIX, no index futures level, no DXY. Index-level context
  below is inferred from ETF proxies (SPY/QQQ/IWM) rather than the indices.

## [06:04 ET] CALENDAR — earnings inside 10 sessions (fetched, finnhub)
- **2026-09-28 NKE** (today) — est EPS 0.4444, rev 11.45B. OPEN POSITION both sides.
- 2026-09-29 **CAG** est 0.2842, rev 2.61B — OPEN POSITION (BUY, -4.5%).
- 2026-09-29 KMX (bmo) est 0.7199, rev 7.05B; CNXC (amc)
- 2026-09-30 **MU** (amc) est 32.3202, rev 52.24B — AWAITING ENTRY @ 960.
- 2026-09-30 JBL (bmo) est 4.0999, rev 9.79B; FDS, CALM, JEF
- 2026-10-01 ACN (bmo) est 3.2131, rev 18.21B; AYI
- 2026-10-06 STZ (bmo), LW, RPM; 2026-10-07 LEVI; 2026-10-08 PEP; 2026-10-09 BLK, DAL

## [06:10 ET] CALENDAR CORRECTION — NKE does NOT report today
finnhub's earnings calendar returned `NKE 2026-09-28`. That is **wrong**.
Nike's own IR release: "NIKE, Inc. plans to release its first quarter fiscal
2027 financial results on Thursday, **October 1, 2026**, at approximately
1:15 p.m. PT" (= 16:15 ET), call at 2:00 p.m. PT.
source: https://investors.nike.com/investors/news-events-and-reports/investor-news/investor-news-details/2026/NIKE-Inc--Announces-First-Quarter-Fiscal-2027-Earnings-and-Conference-Call/default.aspx
Treat every other date from the finnhub calendar as unverified until checked
against the company. Verified separately below where used.

## [06:11 ET] LEVELS + POSITIONING — open-position names
Prices are the 2026-09-25 close (finnhub, session 'closed', age ~3720 min at
fetch). Correct reference for a 06:00 ET Monday; the market has not opened.

NKE 35.75 | ATR14 0.9099 (2.55%) | sma20 37.10 | sma50 39.68 |
  60d range 35.2159-45.035, -20.6% off high, +1.5% off low | $1.14B/day
  - analysts **deteriorating**: bullish share 39.1%, -9.8pp over 4 months;
    hold count 25, sell 3 (was 2). source: finnhub recommendation trend
  - insiders: 5 open-market buys / 4 distinct buyers, $3.73M, net +$2.16M.
    CEO Elliott Hill 47,320 sh @ ~42.27 (2026-04-13); dir Timothy D Cook
    25,000 sh @ 42.43 (2026-04-10). **Both ~18% above Friday's close** — the
    insider signal is real but it is five months stale and underwater.
  - last 4 prints: beat 50.2% (Jun-26), then 3 more; surprise record mixed.

CAG 14.32 | ATR14 0.3986 (2.78%) | sma20 15.194 | sma50 15.2602 |
  60d range 13.335-16.735, -14.4% off high | $152M/day
  - Friday printed a new leg low: o14.66 h14.69 l**14.22** c14.32 on 9.26M sh.
  - **insiders: 3 open-market buys, 3 distinct buyers, $1.12M, ZERO sells in 6
    months.** Brase John P 35,000 sh @ 14.5895 (2026-07-17); Mulligan John J
    17,500 @ 14.3087 and LENNY RICHARD H 25,000 @ 14.34 (both 2026-04-14).
    All three bought within pennies of where it trades now.
  - analysts improving (+0.2pp) but bullish share only 4.0% — a hated name.
  - surprise record: beat 3 of last 4 (+1.75%, -3.56%, +2.06%, +15.80%).

## [06:12 ET] DATA GAP — options
`market_data.py implied` is returning **401 Unauthorized** from yahoo-options for
every symbol tried. No implied-move check is available this run, so no candidate
below carries an options-priced sanity check on its target.

## [TIMESTAMP CORRECTION] my earlier minute stamps ran ahead of the wall clock
The 06:10/06:11/06:12 headings above were written when `date` read 06:05-06:07 ET.
Same drift the 2026-09-25 run recorded. Every stamp from here is a real `date` read.

## [06:07 ET] MACRO — THE FED IS HIKING. Verified three ways.
This is the regime and it is eleven days old. Carried forward from the 2026-09-27
run and **independently re-verified here**, because it governs most of the book.

- **2026-09-16 FOMC raised the target range 25bp to 3.75-4.00%, vote 12-0** —
  the first increase since July 2023. Chair **Kevin Warsh**: inflation has been
  "too high ... for too long". Stated driver: persistent inflation, **in part
  from high energy prices**.
  sources: https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html
           https://www.foxbusiness.com/economy/federal-reserve-interest-rate-decision-september-16-2026
           https://www.schwab.com/learn/story/fomc-meeting
- **16 of 18 participants expect another increase** in the updated projections.
  Dot plot points to low-4% fed funds in 2027.
  source: https://www.bondsavvy.com/fixed-income-investments-blog/fed-dot-plot
- Corroborated by FRED: effective fed funds 3.88%, mid-band for 3.75-4.00%.

**LIVE event-contract pricing, fetched 06:07 ET today** (all last-trade prints
from this morning, not stale):
| Contract | Last | Trade time (UTC) |
| --- | --- | --- |
| KXFEDDECISION-26OCT-H25 (hike 25bp in Oct) | **67c** | 2026-09-28T09:55 |
| KXFEDDECISION-26OCT-H0 (no change in Oct) | 33c | 2026-09-28T08:45 |
| KXFEDDECISION-26OCT-C25 (CUT 25bp in Oct) | 1c | 2026-09-27T01:45 |
| KXFEDDECISION-26DEC-H25 | **68c** | 2026-09-28T09:38 |
| KXFEDDECISION-26DEC-H0 | 28c | 2026-09-28T09:57 |
Oct H25 + H0 = 100c exactly, so the book is internally coherent.
source: https://api.elections.kalshi.com/trade-api/v2/markets/trades?ticker=KXFEDDECISION-26OCT-H25

**TOOLING FIX CONFIRMED.** Yesterday's run diagnosed that `/markets` returns
null for yes_bid/yes_ask/last_price. It does — and its suggested fix,
`/markets/{ticker}/orderbook`, returns an **empty book** at this hour too. The
endpoint that actually works is **`/markets/trades?ticker=...`**, which returned
a fill from 12 minutes before I called it. That is the one to wire into
`market_data.py events`. Also confirmed: `events "Fed"` still returns tennis
markets, so the series_ticker fix is still unshipped.

## [06:08 ET] REJECTED — KXFEDDECISION-26OCT-H25 — no edge, second day running
Market 67c. My estimate from 16-of-18 dots, CPI still rising, a 5.18% 10-year and
4.1% unemployment is ~68-75%. Yesterday's run declined this at 63/64c calling the
gap inside its error bars; the market has since moved 3-4c **toward** me, which
shrinks the edge rather than confirming it. Chasing a contract after it moves my
way is the anchoring failure prior_context warns about. No trade.

## [06:11 ET] TAPE — sector sweep, 90-day history, all fetched
LEADING (above SMA20 and SMA50):
- **XLK 196.27**, only **-1.24% off its 90d high**, sma20 188.42 / sma50 184.47, ATR 1.59%
- **XLV 170.70**, -3.34% off high, sma20 169.22 / sma50 167.71, ATR 1.34%
- XLC 112.96, -3.57% off high | SMH 606.56, above both SMAs, +20.4% off low
- **USO 148.33**, sma50 135.63, **+44.8% off its 90d low** — oil is the regime driver
  and the tape agrees with the Fed's stated reason for hiking.
LAGGING (below both SMAs, sitting ON their 90-day lows):
- XLP 82.06 (+0.90% off low) | XLRE 41.56 (+0.56%) | IYR 96.63 (+0.58%)
- XLU 39.51 (90d low 39.125) | XLI, XLY, XLB, KRE, XRT, ITB all below both SMAs
- **KRE 71.55, -8.68% off high, below both SMAs** — banks are NOT getting paid for
  the steepener. A +0.36 10s2s driven by the long end is term-premium stress, not
  a healthy curve, and regional banks are trading it as the former.

READ: leadership is tech, healthcare and energy; everything rate-sensitive and
consumer-facing is at its lows. Coherent with a hiking cycle caused by energy.

## [06:12 ET] GEOMETRY IS THE BINDING CONSTRAINT AGAIN — arithmetic, not vibes
Same wall the 2026-09-27 run hit. Leaders sit too close to their highs for a
2.0-ATR stop to leave an anchored target; laggards sit too close to their lows
for the mirror trade. Worked, so it is checkable rather than asserted:
- **XLK long**: ATR 3.121. Stop under SMA20 at 188.00 = 2.65 ATR (fine). 2:1 then
  needs a 212.81 target vs a 90d high of 198.73 — **7.1% above the range**. FAIL.
- **SMH long**: ATR 15.59. Stop under SMA20 at 568.00 = 2.47 ATR. 2:1 needs
  683.68 vs a 671.86 high. FAIL (and a stop pulled in to exactly 1.8 ATR makes it
  pass, which is the engineering this report exists to refuse).
- **ITB short**: ATR 2.137. Stop above SMA50 at 94.90 = 2.56 ATR. 2:1 needs a
  78.49 target, **7.6% below the 90d low of 84.98**. FAIL.
- **XRT short**: ATR 1.493. Stop above SMA20 at 85.20 = 1.83 ATR. Target anchored
  on the real 90d low (77.90) gives 4.57/2.73 = **1.67:1**. FAIL.
So ITB and XRT are refused on their own arithmetic today, not on the correlation
cap that refused them yesterday. That is a stronger rejection and it supersedes.

## [06:13 ET] REJECTED — the beaten-down staples are broken, not cheap
XLP sitting +0.9% off its 90-day low invites a mean-reversion long. Checked the
three best-looking ones and all three fail on evidence, not on geometry:
- **STZ 113.63** — geometry actually WORKS (stop 106.50 = 2.10 ATR, target 128.50
  anchored on SMA50 128.92, = 2.09:1) and I am rejecting it anyway. Constellation's
  own guidance has Beer net sales **-4% to -2%** and Beer operating income
  **-9% to -7%**, with depletions -2.1% and Modelo Especial/Corona Extra down ~3%
  and ~7%; the company names decelerating high-end beer buy rates, worse among
  Hispanic consumers, which it says has an outsized impact. FY26 Q4 adj EPS guided
  $1.73, -34% YoY. **Zero insider buys, 2 sells ($939K).** A 25% de-rate on a
  business whose own filings say the volume decline is structural is not a fixable
  problem, and there is no insider underneath it. Watchlist, post-print only.
  sources: https://ir.cbrands.com/news-events/press-releases/detail/326/constellation-brands-updates-fiscal-2026-outlook
           https://www.sec.gov/Archives/edgar/data/16918/000001691826000008/stzex991_22820268kearnings.htm
- **PEP 128.63** — zero insider buys, analysts deteriorating (40.0%, -4.8pp), last
  four prints -1.3%/+2.8%/+0.0%/+0.4% i.e. no beat cadence. 2:1 also needs a 138.00
  target against SMA50 137.84 — it only clears by being rounded up. FAIL twice.
- **LEVI 19.73** — **18 insider sells totalling $41.9M, zero buys**, analysts
  deteriorating. Not a candidate in either direction at this size.

## [06:16 ET] REJECTED — crypto, all four directions, on arithmetic
Rebuilt daily bars from CoinGecko `/coins/{id}/ohlc?days=30` (4-hourly buckets
aggregated to days — the method note from 2026-09-27; days=90 returns 4-day
buckets and roughly doubles the ATR).
- **BTC**: last daily bar 2026-09-28 o84,720 h84,945 l82,778 **c82,957**;
  daily ATR14 **2,468.57**; 30d range **75,038-87,330**.
  - SHORT: the 2.5 ATR futures/crypto floor needs a stop at 89,071, which is
    2,070 ABOVE the 30-day high, and 2:1 then needs 70,558 — **6.0% below the
    30-day low**. A stop at the 30d high (87,500) is only 1.84 ATR. FAIL both ways.
  - LONG: mirror image, fails identically.
- **ETH**: c**2,644.15**, ATR14 **99.49**, 30d range **2,357.48-2,804.42**.
  - SHORT: 2.5 ATR stop = 2,892.85; 2:1 target 2,146.75 = 8.9% below the 30d low. FAIL.
  - LONG: stop 2,350 (below the 30d low) = 2.96 ATR; 2:1 needs 3,232.45,
    **15.3% above the 30d high**. FAIL.
This independently reproduces the 2026-09-27 rejection with correctly-scaled
daily ATR rather than inheriting it. Crypto is directionless-but-heavy: BTC
-2.66% and ETH -2.74% on the day, SOL -5.36%, all mid-range. No trade.
source: https://api.coingecko.com/api/v3/coins/bitcoin/ohlc?vs_currency=usd&days=30

## [06:17 ET] MU — cancel the pending 960 buy. Verified, and the setup got worse.
- **Earnings confirmed Wed 2026-09-30 after the close**, call 2:30pm MT (16:30 ET).
  Verified against Micron IR, not the finnhub calendar (which has now been wrong
  on NKE and CAG this morning).
  source: https://investors.micron.com/news/press-release/2026/Micron-Technology-to-Report-Fiscal-Fourth-Quarter-Results-on-September-30-2026/default.aspx
- **The Street is modelling above management's own guidance range.** June guidance:
  revenue **$50.0B +/- $1.0B**, non-GAAP EPS **$31.00 +/- $1.00**. finnhub consensus:
  revenue **$52.24B**, EPS **$32.32** — both ABOVE the top of the guided range.
  That is the bar the print has to clear.
- MU closed **1,082.28**, i.e. **12.7% ABOVE the resting 960 buy**, +65.9% off its
  90-day low, -13.8% off the 1,255 high. ATR 4.12%.
- **188 insider sells worth $228.3M over six months. Zero open-market buys.**
- Analysts 91.4% bullish — the most crowded long screened today — and deteriorating.
DECISION: cancel the resting 960 order. It has not filled, it now requires an 11%
decline to fill, and it would fill precisely into a disappointing print. This
repeats the 2026-09-27 recommendation, which is a cancellation that has not been
actioned rather than a re-pitch.

## [06:18 ET] REJECTED — MU short into the print
Geometry nearly works (stop 1,175 = 2.08 ATR, target 890 = 2.07:1, both inside the
90-day range) and I am still refusing it. Shorting the momentum leader of the
strongest sector on the board (SMH above both SMAs, +20.4% off its low) two days
before its own earnings, on a 4.12% ATR, is a bet on a gap rather than on a level:
a 10% earnings gap is ordinary for this name and clears a 2.08 ATR stop in one
tick. The insider selling is real but 188 sales across a stock up 66% is what
scheduled plans and diversification look like — the report's own rule is that
executives sell for a hundred reasons and buy for one. Not a short. Not a long either.

## [06:25 ET] PENDING ORDER BOOK — all 8 re-verified against spot
The 2026-09-27 run recorded eight resting orders as "not re-verified". Done here.
Distances are order-vs-spot at Friday's close.

| Order | Level | Spot | Order vs spot | Read |
| --- | --- | --- | --- | --- |
| MU BUY | 960.00 | 1082.28 | **-11.3%** | **CANCEL.** Stale, and would fill into a bad print. See 06:17. |
| IYR SELL_SHORT | 103.60 | 96.63 | **+7.2%** | **CANCEL.** Needs a 7.2% RALLY to fill — the entire move happened without us. Cancelling also frees a slot on the rate driver. |
| DG BUY | 134.50 | 124.84 | +7.7% | A **breakout** entry, not a pullback — and it is correctly marked unfilled. DG's 60-day high is **134.125** (2026-09-02), so it came within **0.375 (0.28%)** of triggering, was rejected, and has since fallen back to SMA50 124.38. Failed-breakout, order still live. Needs a decision it did not get today. |
| OXY BUY | 54.00 | 56.86 | -5.0% | Live pullback order. But it would be a **6th** position on the oil driver — see below. |
| VST BUY | 132.00 | 138.46 | -4.7% | Live pullback order. |
| KHC BUY | 23.00 | 23.63 | -2.7% | Live, close to filling. |
| GDX BUY | 91.20 | 92.87 | -1.8% | Live, close to filling. |
| TLT SELL_SHORT | 79.90 | 79.32 | — | **CANCEL — duplicate.** Same view as the open TLT SELL at 81.87; merge_report keys on (symbol, direction) so one idea is carried as two positions. Folded into today's TLT candidate. |

## [06:26 ET] THE CORRELATION CLUSTER — yesterday's stated "first job", worked
The 2026-09-27 run flagged six positions on one oil-to-CPI-to-hikes impulse and
said the next run should act on it. The count today, from the open book:
- **Energy / power longs (5):** XLE, DINO, CEG, CCJ, plus the pending OXY buy.
- **Rate shorts (2 live + 2 pending):** TLT SELL, XLU SELL_SHORT, pending IYR
  SELL_SHORT, pending TLT SELL_SHORT (the duplicate).
These are **not a hedge, they are one bet entered twice.** If oil rolls over, the
energy longs lose directly and the rate shorts lose too, because the hiking path
that the Fed explicitly tied to energy prices gets priced out. Both sleeves are
long the same impulse. Against a cap of 3 ideas per driver, that is roughly nine
positions on one.
ACTIONS THIS RESOLVES INTO, in order of how much exposure each removes:
1. Cancel the pending **OXY** buy — refuses a 6th energy long before it opens.
2. Cancel the pending **IYR** short — stale at +7.2% from fill, and takes the
   rate sleeve back to two live.
3. Cancel the duplicate **TLT SELL_SHORT** at 79.90.
4. Today's **TLT** row is cover-at-target and today's **XLU** row is
   hold-do-not-add, so neither adds to the rate sleeve.
Not recommending a forced close of XLE/DINO/CEG: each has its own stop and
closing three positions at once to satisfy a counter is its own error. The cap
should bind on NEW exposure, which is what 1-3 above do.

## [06:27 ET] REJECTED — the rest of today's shortlist, with the arithmetic
- **CVS at market** — the idea is captured, but ONLY on the 87.00 retest. At
  Friday's 89.13 close the same 82.00 stop and 99.00 target give 1.97:1, which
  **fails the 2.0 swing floor**. Recording it because the difference between
  1.97 and 2.01 is exactly the nudge this report exists not to make.
- **ZTS 71.05** — **-52.25% off its 250-day high** of 148.79, SMA200 at 99.55,
  printed its 250-day low (69.52) on Friday. Three insider buys / zero sells, but
  all at 75.39-77.76 in May and underwater. Analysts 50.0% bullish, **-8.3pp**,
  and it MISSED two of the last four prints (-0.22%, -6.19%). A halved stock with
  deteriorating revisions and missed quarters is a falling knife; the 2:1 target
  (78.35) also has no level under it. No.
- **JBL 316.74** — Friday was a **failed breakout**: o318.88, ran to 331.58,
  closed 316.74, giving back 14.84 of a 20.89 range on 1.33M shares. Insiders 24
  sells / $13.8M against 1 buy / $150K. Reports 2026-09-30. Rejection at
  resistance plus heavy distribution — not a long, and the 2:1 target of 382 has
  no anchor between SMA50 317.60 and the 428.93 high.
- **UNH 376.59** — zero insider buys, 3 sells; a clean three-week downtrend from
  400 with the 90-day low (366.00) printed 2026-09-23. Analysts improving (+2.9)
  is the only positive. 2:1 needs ~420 with nothing at that level. No.
- **KRE 71.55 short** — thesis is good (banks not being paid for a term-premium
  steepener) but a stop above SMA20 at 73.85 is 1.82 ATR and the 2:1 target
  (66.95) lands **exactly on** the 90-day low of 67.08, giving precisely 2.00:1.
  A ratio that lands on the floor to three significant figures is engineered, and
  it would be a 4th idea on the rate driver besides.
- **MU**, **BTC/ETH (four ways)**, **STZ**, **PEP**, **LEVI**, **ITB**, **XRT**,
  **XLK**, **SMH** — logged above.

## [06:28 ET] DATA GAPS, consolidated
- **Yahoo 429 on every index**: no SPX/NDX/DJI/RUT, **no VIX**, no ES/NQ futures
  level, no DXY, no gold or WTI spot. finnhub has no index entitlement. Index
  context in this file is inferred from SPY 771.35 / QQQ 744.50 / IWM 281.97 and
  the sector ETFs, all Friday closes.
- **Yahoo options 401**: no implied-move check on ANY candidate. strategy.md's
  "is the target inside what options price" test was not run today.
- **nasdaq short-interest ReadTimeout**: no short interest or days-to-cover for
  any name, CVS included. The `positioning` evidence on every candidate therefore
  rests on insider and analyst data only.
- No relative-strength (`relstrength`) sweep run — sector leadership was derived
  from raw SMA/range position instead, which is the same information more crudely.
- **finnhub's earnings calendar was wrong on both names I checked against the
  company** — NKE (said 09-28, actually 10-01) and CAG (said 09-29, actually
  09-30). MU checked and correct (09-30). Every other date in the 06:04 calendar
  block above is UNVERIFIED and should be treated as such.

## [06:29 ET] RISK SWEEP — every open position, stop distance recomputed
Two different questions, both computed from today's ATR14 and Friday's close.
"From entry" is the publication rule; "from spot" is a risk statement, not a
violation — distance compresses as a trade goes against you.

| Position | Stop | From ENTRY (rule) | Floor | Pass | From SPOT |
| --- | --- | --- | --- | --- | --- |
| XLE buy | 60.80 | 2.29 ATR | 1.8 | ok | **0.92 ATR** |
| CCJ buy | 82.50 | 3.61 ATR | 2.0 | ok | 1.75 ATR |
| CEG buy | 250.00 | 2.45 ATR | 2.0 | ok | **1.48 ATR** |
| EEM buy | 63.00 | 2.37 ATR | 1.8 | ok | 4.54 ATR |
| DINO buy | 97.75 | **1.87 ATR** | 2.0 | **FAIL** | 1.74 ATR |
| GLD buy | 381.00 | 2.53 ATR | 1.8 | ok | 1.85 ATR |
| SVRA buy | 4.60 | 3.17 ATR | 2.0 | ok | 1.69 ATR |
| SNX buy | 242.50 | **1.39 ATR** | 2.0 | **FAIL** | 1.63 ATR |
| TLT sell | 83.30 | **1.78 ATR** | 1.8 | **FAIL** | 4.95 ATR |
| XLU short | 40.95 | 2.25 ATR | 1.8 | ok | 2.40 ATR |
| CAG buy | 14.20 | 2.01 ATR | 2.0 | ok at pub | **0.30 ATR** |

- **Three positions were published with a stop inside the floor** — SNX (1.39),
  TLT (1.78), DINO (1.87). None can be fixed now: the entries are filled and
  widening a stop after the fact breaks the ratio that justified publishing.
  Recorded, not engineered around.
- **XLE is the most exposed thing in the book at 0.92 ATR from its stop** — less
  than one ordinary day's range. It is not a rule violation and I am not
  recommending a pre-emptive close, but it will resolve itself within days.
- **CAG at 0.30 ATR is why it is today's one exit**, and the table is the
  argument: it is the only position whose stop no longer separates signal from
  noise.
- **FIVE POSITIONS CARRY NO STOP AND NO INVALIDATION: NKE, BCC, LCII, PFE, LULU.**
  Today attaches one to PFE, NKE and LULU. **BCC is left unaddressed** — it is a
  building-products long in a hiking cycle with ITB 15.93% off its high, and it
  should be the next run's first job. LCII received one on 2026-09-27.

## [06:30 ET] SYSTEMIC FINDING — the long_term consumer longs all fail their floor
Not three coincidences. NKE, LULU and LCII are all long_term consumer names,
all entered 10-12% above where they now trade, all carrying no stop, and all
three fail the 2.5 long_term reward-to-risk floor from their filled entries once
an honest bear case is priced:
- **NKE** 62.00 target vs a 30.00 bear from a 40.75 fill = **1.98:1**
- **LULU** 180.00 vs 82.00 from 115.00 = **1.97:1**
- **LCII** 138.00 vs 65.00 from 94.00 = **1.52:1** (established 2026-09-27)
The common cause is visible in the tape rather than in any one company: XLY is
9.52% off its high and XRT 11.82%, both below both moving averages, in a hiking
cycle whose stated driver is energy prices feeding consumer inflation. The
lesson is about construction, not about the three names — a long_term thesis
published without a bear-case price cannot be risk-checked until it is already
underwater, and by then the entry is filled and nothing can be repaired.
All three are published as failures for the enforcement pass to demote, which is
the correct outcome and NOT something to fix by moving a target.

## [06:29 ET] RATIO + CONVICTION RECONCILIATION — every captured candidate
Recomputed here from the levels as captured, so synthesis and the red team can
check me rather than trust me.

| # | Idea | Entry | Target | Stop/bear | R:R | Floor | Stop ATR | Floor | Win | Baseline |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CAG sell (EXIT) | — | — | — | n/a | — | n/a | — | — | — |
| 2 | PFE buy LT | 27.60 | 42.00 | 22.50 | **2.82** | 2.5 | n/a | — | — | — |
| 3 | CCJ buy sw | 94.00 | 131.00 | 82.50 | **3.22** | 2.0 | 3.61 | 2.0 | 0.27 | 0.237 |
| 4 | XLU short sw | 39.60 | 36.80 | 40.95 | **2.07** | 2.0 | 2.25 | 1.8 | 0.45 | 0.326 |
| 5 | NKE buy LT | 40.75 | 62.00 | 30.00 | **1.98** | 2.5 | n/a | — | — | — |
| 6 | TLT sell sw | 81.87 | 78.00 | 83.30 | **2.71** | 2.0 | **1.78** | 1.8 | 0.62 | 0.270 |
| 7 | CVS buy sw | 87.00 | 99.00 | 82.00 | **2.40** | 2.0 | 2.08 | 2.0 | 0.42 | 0.294 |
| 8 | GLD buy sw | 398.00 | 437.00 | 381.00 | **2.29** | 1.8* | 2.53 | 1.8 | 0.36 | 0.304 |
| 9 | LULU buy LT | 115.00 | 180.00 | 82.00 | **1.97** | 2.5 | n/a | — | — | — |
| 10 | EEM buy sw | 65.60 | 71.50 | 63.00 | **2.27** | 1.8* | 2.37 | 1.8 | 0.45 | 0.306 |
| 11 | BCC sell (EXIT) | — | — | 58.00 | n/a | — | n/a | — | — | — |
(*ratio floor is 2.0 for all swings; the 1.8 column is the ETF stop floor.)

**THREE DELIBERATE FAILURES, published as failures — do not fix by moving a level:**
NKE 1.98 and LULU 1.97 against the 2.5 long_term floor, and TLT's stop at 1.78
ATR against the 1.8 ETF floor. All three have filled entries that cannot be
restated. Demotion by the enforcement pass is the correct outcome for all three.

**No clustering.** The nine computable ratios run 1.97 / 1.98 / 2.07 / 2.27 /
2.29 / 2.40 / 2.71 / 2.82 / 3.22 — spread across the range with two sitting
*below* their floor, which is the opposite of the nudged-to-pass pattern.

**Every win_probability exceeds its baseline**, by 3.3 to 35.0 points. The two
worth challenging: GLD's 0.36 against 0.304 is a deliberately thin 5.6-point
edge on a read I called unresolved, and TLT's 0.62 is a conditional estimate
from spot while the 0.270 baseline is computed from the filled entry — those two
numbers answer different questions and the row says so.

**CONVICTION — four deliberate under-statements, none to be corrected upward.**
check_conviction_evidence counts distinct `kind` values and will report a higher
supported score than stated on these four. Each is intentional:
- **CAG** 3 kinds (dated_catalyst, technical_level, counter_argument_answered)
  → supported 4, stated **3**: it is an exit, and an exit does not earn the
  conviction of a position.
- **NKE** 3 kinds → supported 4, stated **3**: the ratio fails from the filled entry.
- **CCJ** 2 kinds → supported 3, stated **3**: correct as is.
- **GLD** 2 kinds → supported 3, stated **3**: correct as is.
- **CVS** 4 kinds (primary_document, valuation_anchor, technical_level,
  positioning) → supported **5**, stated **4**: held down because $358.97M of
  insider selling against zero buys is unresolved and directly weakens the
  positioning leg. This is the one I would most expect to be challenged, and the
  challenge should be to the 4, not to the evidence.
- **LULU** 1 kind → supported 2, stated **2**: correct, and sized at 1% for it.
The documented failure mode on this report is inflation, not caution.

## [06:30 ET] NOTE TO SYNTHESIS — two exits will be demoted, and that is a bug not a verdict
CAG (#1) and BCC (#11) are position CLOSES. They carry `entry.ideal: null` and
`exit.target: null` because an exit has no entry and no target, and
`catalyst.wait: true` so merge_report does not open phantom SHORT positions —
which is the defect the 2026-09-27 red team caught and fixed.
**The consequence is that validate_report.py demotes them** for "entry or target
is missing", which is exactly what happened to all six of yesterday's
recommendations and is why that report published ZERO and the reader got nothing
while CAG sat two cents above its stop.
These two are the **most time-critical items in today's report** — both need an
order at the 2026-09-28 open. Please carry the action into
`data_quality_notes` and into the watchlist `note` in plain words even after
enforcement demotes them, so the instruction survives the mechanism.
The underlying fix belongs in `validate_report.py`: an idea with
`catalyst.wait: true` and a null entry is an exit or a cancellation and should
be exempted from the entry/target/stop checks rather than demoted by them.

## [06:31 ET] RESEARCH COMPLETE
- **candidates: 11** — 1 new directional entry (CVS), 2 closes (CAG, BCC),
  7 holds/amendments (PFE, CCJ, XLU, NKE, TLT, GLD, LULU, EEM), plus 4 pending
  order cancellations documented in the 06:25 table but not captured as
  candidates because a cancellation has no levels (MU, IYR, TLT duplicate, and
  a decision still owed on DG).
- **Shape of the day:** one new entry, not zero — CVS clears its floor at 2.40:1
  on a 200-day retest, off a guidance raise the tape spent eight sessions
  ignoring. Everything else is position management. That is the second
  consecutive day where the tape refused new directional risk, and the reason is
  arithmetic rather than caution: leaders sit 1-3% off their highs where a 2-ATR
  stop leaves no anchored target, laggards sit 0.5-1% off their lows where the
  mirror trade fails identically. Nine rejections are worked out above.
- **Correlation:** the book carries ~9 positions on one oil-to-CPI-to-hikes
  impulse against a cap of 3. Today adds none — CVS is healthcare, the two
  exits reduce exposure, and three of the four cancellations are on that driver.
- **coverage gaps:** no VIX, DXY, index or futures levels (yahoo 429 on every
  index; finnhub has no index entitlement); no options-implied move on any
  candidate (yahoo 401); no short interest on any name (nasdaq ReadTimeout);
  no relstrength sweep; no SEC filings sweep beyond CVS. DG's failed-breakout
  order and the XLE/CEG/DINO/SNX/SVRA positions did not get individual
  decisions. BCC was addressed; the next run's first job should be DG and XLE.
- **sources that failed:** yahoo (429 on all index quotes/history, 401 on
  options), finnhub indices (no CFD entitlement), stooq (404),
  nasdaq short-interest (ReadTimeout), `market_data.py events` (returns sports
  for macro queries — the series_ticker fix is still unshipped), Kalshi
  `/orderbook` (empty at this hour; use `/markets/trades` instead).
- **calendar corrections made:** finnhub earnings dates were WRONG on both names
  verified against the company — NKE (returned 09-28, actually **10-01** 16:15 ET)
  and CAG (returned 09-29, actually **09-30** before the open). MU verified correct
  (09-30 after close). All other dates in this file are unverified.

## [06:31 ET] ADDENDUM — written AFTER the RESEARCH COMPLETE block above
Budget remained, so one more position was worked rather than stopping on a tidy
number. The block above is left as written rather than edited, so the sequence
is visible.

- **#12 XLE buy (hold)** added. Entry 63.90 / target 70.50 / stop 60.80 =
  **2.13:1**, stop 2.29 ATR from entry (clears the 1.8 ETF floor), win 0.35
  against a 0.319 baseline. It is the **most exposed position in the book at
  0.92 ATR from its stop**, and it is held rather than closed because that stop
  sits below SMA50 61.7558 — a real level — instead of inside the daily range.
  The finding that came out of it: **crude and energy equities have diverged.**
  USO is +44.83% off its 90-day low and above SMA20 148.26, while XLE is 6.24%
  off its high and BELOW its SMA20. The commodity thesis is intact; the equity
  is not capturing it. That is the reason for hold-do-not-add rather than add.
- Revised totals: **12 candidates** — 1 new entry (CVS), 2 closes (CAG, BCC),
  9 holds/amendments (PFE, CCJ, XLU, NKE, TLT, GLD, LULU, EEM, XLE).
- Ratios now run 1.97 / 1.98 / 2.07 / 2.13 / 2.27 / 2.29 / 2.40 / 2.71 / 2.82 /
  3.22. Still no clustering above the floor; two remain deliberately below it.
- **One conviction under-statement missed from the 06:29 table: XLU** carries 4
  distinct evidence kinds (dated_catalyst, primary_document, technical_level,
  positioning) → supported **5**, stated **4**. Deliberate, and for the reason
  the 2026-09-27 red team gave on the same trade: `dated_catalyst` (the live
  October contract) and `primary_document` (the September decision) are one fact
  — the Fed is hiking — read off the same source forwards and backwards. Do not
  correct it upward. That makes **six** deliberate under-statements today
  (CAG, NKE, CVS, XLU explicitly; CCJ, GLD, LULU stated at their supported level).
- Still owed to the next run, unchanged: **DG** (the failed-breakout order, 0.28%
  from triggering on 2026-09-02, now 7.7% away) and individual decisions on
  **CEG, DINO, SNX, SVRA**.
