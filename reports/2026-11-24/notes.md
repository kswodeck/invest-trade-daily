# Research log — 2026-11-24

## [06:03 ET] MACRO — rates, crypto, regime
- US10Y **4.92%** (2026-11-20), prior 5.04 — long end rich but ROLLING DOWN from a 5%+ handle — source: https://fred.stlouisfed.org/series/DGS10
- US2Y **4.63%** (2026-11-20), prior 4.76 — source: https://fred.stlouisfed.org/series/DGS2
- Fed funds effective **3.88%** — policy rate well BELOW the 10y; the curve steepened, 10y2y **+0.29** — source: https://fred.stlouisfed.org/series/T10Y2Y
- Unemployment **4.1%** (Oct 2026), prior 4.2% — labour market not cracking — source: https://fred.stlouisfed.org/series/UNRATE
- CPI index 337.476 (Oct 2026) vs 336.298 prior — source: https://fred.stlouisfed.org/series/CPIAUCSL
- TLT (20y bond ETF proxy) 81.69, +0.29% — source: finnhub via market_data.py
- Crypto risk-off: BTC **$59,738 (-2.66% 24h)**, ETH **$1,681.63 (-2.44%)**, SOL **$70.34 (-2.64%)** — source: https://www.coingecko.com
- DATA GAP: every index quote (^GSPC ^NDX ^DJI ^RUT ^VIX), ES/NQ futures, DXY, gold and WTI returned ok:false — finnhub requires a CFD-index subscription and yahoo is rate-limiting (429). Using ETF proxies (SPY/QQQ/IWM/GLD/USO) for index context.

## [06:03 ET] REGIME READ — the track record is the macro signal
- 47 closed trades: 5 hit target (11%), avg **-5.9%**. 42 of 47 were swing LONGS. The one open winner is the `IWM` SELL_SHORT (+5.1%).
- That is not 47 bad stock picks; it is one bet — long equities into a tape that has been falling — made 47 times. Conclusion for today: **raise the bar hard on new dip-buying longs**, and do not add correlated beta.
- 10y at 4.92% with fed funds at 3.88% is a market pricing term premium / fiscal risk, not easing relief. BTC at $59.7k is down roughly 20%+ from where this report was shorting it at 74,075 on 2026-11-09 (that short never filled).

## [06:08 ET] TAPE — a two-day event: Fri 11/20 capitulation, Mon 11/23 snapback
All bars finnhub via market_data.py history; last bar 2026-11-23 official close (age ~843 min at 06:02 ET = a CLOSED market, not stale).

| ETF | 11/19 c | 11/20 c (low) | 11/23 c | 11/23 chg | sma20 | sma50 | off 90d high |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 715.87 | 689.81 (686.75) | 722.29 | **+4.71%** | 745.65 | 759.41 | -7.59% |
| QQQ | 645.04 | 608.45 (606.23) | 651.03 | **+7.00%** | 675.47 | 709.79 | -14.66% |
| IWM | 264.22 | 256.61 (256.32) | 265.74 | **+3.56%** | 275.66 | 277.82 | -12.92% |
| GLD | 335.18 | 322.87 (320.95) | 333.02 | +3.14% | 358.68 | 373.70 | **-22.45%** |
| TLT | 80.35 | 81.45 | 81.69 | +0.29% | 81.00 | 80.09 | -3.14% |

- **11/20 was a liquidation, not a growth scare.** Stocks, gold AND crypto fell together while Treasuries rallied — correlation-to-one is a deleveraging signature. SPY volume 151.4M shares vs ~39B$/day average turnover, QQQ 134.8M, IWM 57.5M, GLD 23.6M — all multiples of normal.
- **11/23 reversed but closed weak.** SPY opened 724.33 and closed 722.29 (below the open); QQQ opened 655.98, high 657.53, closed 651.03 — mid-range, off the high. A +7% day that fades from the open is short-covering, not accumulation.
- **Everything is still below its 20d and 50d.** QQQ needs +3.8% to reclaim sma20 and +9.0% for sma50. Nothing here is a confirmed trend reversal yet.
- ATRs for level-setting: SPY 18.45 (2.55%), QQQ 24.10 (3.70%), IWM 6.76 (2.54%), GLD 8.68 (2.61%), TLT 0.78 (0.95%). **These are enormous** — a 2.0 ATR swing stop on QQQ is 7.4%.
- GLD -22.45% from its 429.42 high is the single biggest dislocation on the board.

## [06:10 ET] NEWS — the driver of both days: the Nvidia CEO shock and its reversal
- **2026-11-13**: Jensen Huang **resigned** as NVDA CEO after reports of extramarital affairs, including one with an alleged Chinese intelligence operative (China denies). CFO Colette Kress became interim CEO. — source: https://www.cbsnews.com/news/nvidia-reinstates-jensen-huang-ceo/
- **Week of 11/16**: on the earnings call board chair Harvey Jones said the company "does not intend to reinstate Jensen as CEO." QQQ fell 679.89 (11/13) → 608.45 (11/20), **-10.5% in five sessions**, and all three indexes entered correction. — source: https://www.nbcnews.com/tech/tech-news/nvidia-reinstates-jensen-huang-rcna610864
- **2026-11-23**: board voted **unanimously** to reinstate Huang as President, CEO and board director; Kress returns to CFO; Jones stays chair. Board said it "received input from senior levels of the United States government" and is confident the reinstatement "poses no national security risk." — source: https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director
- **President Trump says he personally intervened**, speaking "directly and indirectly" with the board, and that Huang assured him he would work harder than before. — source: https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html
- NVDA closed **+31%**; MU +19.5%; Nasdaq Composite +6.5%, best session for Nasdaq and S&P since 2025-04-09. — source: https://www.tradingkey.com/analysis/stocks/us-stocks/262318800-dow-jumps-1400-points-nasdaq-rallies-as-jensen-huang-returns-to-nvidia
- **This morning the gains are already fading: Nasdaq-100 futures reported -1.61%** — source: https://cnbc.com/2026/11/23/stock-market-today-live-updates.html

### What this tells me about today
1. The event is **spent as an event**. A +31% single-day gap on a personnel reversal is not a catalyst I can still enter; it is the news being priced. Chasing the AI complex here is buying the second day of a squeeze.
2. **The governance fact is strictly worse than before the scandal**, and that is underpriced. A chair who said "no" on the earnings call reversed within days under direct presidential pressure, and the board had to publish a sentence about national-security risk. The allegations themselves have not been resolved.
3. **The real opportunity is in what got liquidated for no reason of its own.** 11/20 sold stocks, gold and crypto together — gold has nothing to do with who runs Nvidia. GLD -22.45% from its high is the dislocation worth working on.

## [06:14 ET] CALENDAR — verified dated catalysts
- **2026-11-25 08:30 ET — October Personal Income & Outlays (PCE price index)** AND **Q3 GDP second estimate + Corporate Profits**, both confirmed on BEA's own release schedule. — source: https://www.bea.gov/news/schedule
- Core PCE consensus reported at **3.2% y/y vs 3.1% prior** — i.e. consensus is for inflation to RE-ACCELERATE. — source: https://wisevoter.com/world/us/2026/11/23/us-inflation-gdp-consumer-confidence-data-week
- Weekly jobless claims pulled forward to **Wed 11/25** because of the holiday. — source: https://www.okx.com/en-us/orbit/insight/complete-economic-calendar-of-events-from-november-23-29-2026-capable-of-influencing-the-crypto-market-93571961527712
- **Today 11/24**: Conference Board November consumer confidence, consensus ~92.4; 2y FRN and 5y note auctions.
- **Thu 11/26 Thanksgiving — market closed. Fri 11/27 half day (13:00 ET close).** Liquidity drains from Wednesday afternoon. Next NFP 2026-12-04.
- So the week has **one** real macro event and it lands tomorrow morning, in a week where position-taking is thin and a surprise moves more than it should.

## [06:15 ET] GOLD — a 35% drawdown driven by rates and margin calls, not by demand
- Gold closed ~**$3,538/oz** on 11/20, roughly **-35% from its 2026-01-28 closing high of $5,417**; rebounded above $3,600 on 11/23. GLD: 333.02, -22.45% off its own 90d high of 429.42. — source: https://www.iforex.com/market-analysis/gold-price-november-2026-review/
- Attributed cause #1: rising Treasury yields, a stronger dollar, and **Federal Reserve rate HIKE expectations**. — source: https://beinsure.com/news/gold-price-crashes-from-record-high/
- Attributed cause #2: **forced selling** — margin calls from the tech selloff made leveraged holders sell metal to raise cash; futures liquidation rather than fading physical demand. — source: https://discoveryalert.com/analysis/gold-silver-selloff-liquidation-november-2026/
- **Official demand has NOT turned**: World Gold Council reports central banks bought **321 tonnes in Q3 2026** against a five-year quarterly average of ~227 tonnes. Central banks turning net sellers is listed as a risk to watch, not something that has occurred. — source: https://discoveryalert.com/analysis/precious-metals-selloff-gold-silver-november-2026/
- CAVEAT recorded for synthesis: the gold price levels and the cause attribution come from market commentary sites, not primary data. Q4 WGC central-bank data is not published yet. GLD's own OHLCV is primary (finnhub).
- **The reframe that matters more than gold**: if the market is pricing Fed HIKES with core PCE re-accelerating to 3.2%, then the open `TLT` long (entry 80.3, now 81.69) is fighting the stated regime, and every "rate relief" long in the book is mispriced.

## [06:19 ET] EVENT CONTRACTS — markets found, prices NOT available
- Verified live Kalshi series (Robinhood Prediction Markets is Kalshi-backed): `KXFEDDECISION-26DEC-*` (H0 maintain / H25 hike 25 / H26 hike >25 / C25 cut 25 / C26 cut >25), `KXFED-*` upper-bound ladders out to 2028, `KXCPIYOY-26NOV/26DEC-*` with strike buckets running **up to 5.0%**, and `KXRATECUT-26DEC31` "Will the Federal Reserve cut rates before 2027?".
- **December FOMC decision date confirmed: 2026-12-09**, from the `KXFEDDECISION-26DEC` close time of 2026-12-09T18:59Z (13:59 ET). — source: https://api.elections.kalshi.com/trade-api/v2/markets/KXFEDDECISION-26DEC-H0
- **DATA GAP: every one of these returns `yes_bid`, `yes_ask`, `last_price`, `volume` and `open_interest` as `null`** on both the list and single-market public endpoints. Without an implied probability I cannot state a probability disagreement, and `config/universe.md` requires exactly that. **So no event-contract recommendation can be honestly made today.** I will not invent an implied price to make one work.
- That a CPI ladder is quoted to 5.0% is itself a regime datum: the market is being offered inflation strikes far above target.
- NOTE for the open `KXFEDDECISION-26DEC-H0` YES @ 10 published 2026-11-21: it remains unfilled and **I cannot re-price it**. Buying "Fed maintains rate" at 10c implies the market put ~90% on a MOVE at the Dec 9 meeting, which squares with the rate-hike narrative in the gold coverage. Flagging for synthesis as unverifiable today, not as confirmed.

## [06:22 ET] THE CENTRAL FACT — this is a Fed HIKING cycle, ~95% priced, and the tape just squeezed the other way
- Target range **3.75–4.00%**, EFFR 3.88%. **December FOMC is 2026-12-08/09** and markets price a **25bp HIKE at ~94% (Kalshi/Polymarket) to ~97% (CME FedWatch)**, a hold at ~3% and a cut at ~2%, as of 2026-11-23. A month earlier the quarter-point odds were 76.3%. — sources: https://predictionmarketspicks.com/articles/fed-rate-december-2026-odds-half-point-hike-dot-plot-kalshi-polymarket-futures , https://247wallst.com/investing/2026/11/18/traders-now-see-a-95-chance-the-fed-hikes-rates-in-december/
- **A SECOND hike in January is ~55-60% priced.** — source: https://finance.biggo.com/news/78ad00f8-6255-4ebc-9b35-179f5a35e276
- The 50bp tail got erased by the equity selloff — futures stopped pricing any 50bp move after the slide; another source still carried ~5%. Governor Waller had floated a half-point. — source: https://finance.biggo.com/news/2616fca5-1fae-4363-895d-619748dd725f
- Real policy rate is only **+0.68%** (3.88% EFFR less 3.2% consensus core PCE). A hiking Fed that is still barely restrictive is not the same animal as a tightening cycle at a 2%+ real rate.

### Why this reframes the whole report
**Monday's +7% QQQ day repriced one man's job title. It repriced nothing about rates.** The Fed path, the 4.92% 10y and a core PCE consensus that RE-ACCELERATES to 3.2% tomorrow at 08:30 are all exactly where they were on Friday. So the squeeze is not information — it is a better price at which to be doing what the rate regime already implied.

This also explains the report's own 11% hit rate far better than 47 bad stock picks does: the book is long defensives, bond proxies and duration into a **hiking** cycle, and has been buying the dips in it.

### Open positions this fact directly indicts
- **`TLT` BUY 80.3 → 81.69, target 84.3.** Long 20-year Treasuries with the Fed ~95% to hike in two weeks, ~57% to hike again in January, and core PCE consensus rising. The 11/20 move to 81.45 was flight-to-quality inside a liquidation, NOT a rate-cut bet. Tomorrow's 08:30 PCE is a direct threat. **Must be addressed, not held passively.**
- **`XLU` BUY 43.3 → 43.32, target 46.6.** Utilities are the cleanest bond proxy in the sector lineup; same headwind, and the position has gone nowhere in 21 days.
- **`IWM` SELL_SHORT 270.5 → 265.74.** The Russell 2000 is the most rate-sensitive, most floating-rate-levered index on the board. The hiking path is the thesis, and Monday's +3.56% bounce improved the entry rather than breaking it. **This is the one position in the book aligned with the regime.**
- The pending **`KXFEDDECISION-26DEC-H0` YES @ 10** was a bet on "Fed maintains rate". The market now puts that at ~3%. The thesis has been falsified by the tape — **cancel rather than chase**. (Note the asymmetry I am declining for lack of a quotable price: ~3c for "Fed holds" is a cheap hedge against a market accident before Dec 9. Without a live bid/ask I will not publish it.)

## [06:25 ET] POSITION REVIEW — all 15 open, marked to the 2026-11-23 close (finnhub)

| Symbol | Entry | Target | Stop | 11/23 close | vs entry | Read |
| --- | --- | --- | --- | --- | --- | --- |
| HII | 262.0 | 339.76 | 238.5 | 286.57 | **+9.4%** | working; defence, rate-insensitive |
| KHC | 23.0 | 28.09 | 21.2 | 25.10 | **+9.1%** | working; staples |
| CAG | 14.4 | 19.48 | None | 14.86 | +3.2% | working; no stop — invalidation needed |
| TLT | 80.3 | 84.3 | 78.8 | 81.69 | +1.7% | see below — hedge, not a rates bet |
| IWM short | 270.5 | 238.69 | 284.5 | 265.74 | +1.8% | **captured as an update — hold** |
| ABT | 103.0 | 117.34 | 96.8 | 103.32 | +0.3% | flat 34 days |
| UNP | 288.6 | 315.99 | 277.4 | 288.89 | +0.1% | flat 39 days |
| XLU | 43.3 | 46.6 | 41.8 | 43.32 | +0.0% | flat 21 days, bond proxy into hikes |
| PFE | 27.6 | 42.0 | None | 27.40 | -0.7% | flat 69 days; no stop |
| ADM | 68.8 | 78.0 | 64.4 | 67.47 | -1.9% | |
| RTX | 199.0 | 226.5 | 186.0 | 194.77 | -2.1% | |
| OXY | 54.0 | 62.0 | 50.15 | 52.70 | -2.4% | energy was the ONLY sector red on 11/23 |
| XLV | 184.0 | 201.0 | 176.0 | 179.42 | -2.5% | |
| HUN | 9.0 | 10.82 | 8.09 | 8.54 | -5.1% | small cap, stop 8.09 is close |
| DKS | 144.5 | 175.5 | 129.0 | 133.67 | **-7.5%** | worst open position |

- Nothing is at its stop. HUN at 8.54 against a 8.09 stop is the nearest (-5.3% of room).
- The book is overwhelmingly **long defensives and bond proxies** — staples (KHC, CAG, ADM), healthcare (PFE, ABT, XLV), utilities (XLU), rails (UNP), duration (TLT). That is a cut-cycle book being run in a hike cycle.

## [06:27 ET] PROCESS FINDING — the pending shorts were RIGHT and earned nothing
Two of the six awaiting-entry orders are dead, and the reason is structural, not bad luck:
- **`GLD` SELL @ 406.77** (published 2026-10-25). GLD is **333.02**. The short entry was set *above* the market and never filled while gold fell ~18% from that level. The call was correct and made zero.
- **`/MBTZ6` SHORT @ 74075** (published 2026-11-09). BTC is **$59,738**. Same shape: entry above market, never filled, ~19% move captured in full by nobody.
- `config/strategy.md` already names the long-side version of this error — a pullback entry below the market "only fills once the trade first goes against you". **The short-side mirror is identical and is not yet written down: a short entry above the market only fills if the trade first goes against you.** Both of these needed a touch *up* that never came because the thesis was working immediately.
- Action for both: **cancel.** They are stale levels the market left behind weeks ago, not live orders. Re-pitching either at today's price would be a new trade needing its own levels, and after an 18-19% move neither has the reward left to clear its floor.

### Other pending orders, re-priced
- **`CVS` BUY @ 80.0** (published 11/05): now **79.65** — the entry level has finally been reached and this is live/actionable today. CVS has been pitched 4x in 10 days, so flag the repetition honestly.
- `LEN` BUY @ 79.5: now 81.80, still above the entry, unfilled, level unchanged.
- `VZ` BUY @ 46.0: now 46.45, close but unfilled, level unchanged.
- `KXFEDDECISION-26DEC-H0` YES @ 10: thesis falsified (hold now ~3% priced) — cancel.

## [06:30 ET] CRUDE DIVERGED — and it tells you what kind of inflation this is
- **USO closed 133.36 on 11/23, DOWN 4.49% from 139.63, on the single biggest risk-on day since April 2025.** It is -22.38% off its 90d high of 171.82, below sma20 148.46 and sma50 151.20. ATR 5.47 (4.10%). — source: finnhub OHLCV via market_data.py
- XLE was likewise the only sector ETF red on 11/23 (-1.06%).
- **Analytical consequence:** core PCE consensus re-accelerating to 3.2% while crude is down 22% means this inflation is NOT energy-led — it is services, shelter and goods. That is the stickier kind, the kind a Fed cannot wait out, and it is why the December hike is 95% priced rather than 50%.
- **Risk flag on the open `OXY` long** (entry 54.0, now 52.70, stop 50.15): OXY is a levered bet on a crude price that just made a lower low *while everything else squeezed*. The stop is only 4.8% below the current price. This is the open position whose underlying is most actively deteriorating.

## [06:31 ET] HOMEBUILDERS / FINANCIALS — checked, no clean trade
- XHB 99.72: below sma20 101.51 but **above** sma50 98.46, -10.64% off high, ATR 3.34. Builders have NOT broken down despite a 4.92% 10y — so the obvious "short the most rate-sensitive group" trade is not confirmed by the tape and I am not taking it.
- LEN 81.80: below sma20 85.67, sitting exactly on sma50 81.77, -14.09% off high, ATR 3.65.
- **Pending `LEN` BUY @ 79.5 — level unchanged and still unfilled.** Noting the conflict rather than re-pitching: a homebuilder long is the wrong side of a Fed that is 95% priced to hike on Dec 9 and ~57% to hike again in January. Flagging for the red team; I am not advancing it today.
- XLF 55.65: below sma20 57.17, just above sma50 55.84, -7.31% off high. Banks get a steepening curve (10y2y +0.29) and higher reinvestment yields, but 11/20 saw 81.9M shares of liquidation. No edge I can date — rejected.

## [06:32 ET] REJECTED — GLD long — the arithmetic fails its own floor, shown in full
Gold is the biggest dislocation on the board and I wanted this trade. It does not clear:
- **As `long_term`** (floor R:R 2.5 against a stated bear case): from 333.02, an honest bear case in a hiking cycle is a break of the 320.95 low toward ~300, so risk ≈ 33. A 2.5 ratio then demands a target of **415.5**, which is within 3.2% of gold's all-time high of 429.42. Claiming a near-complete round trip to the record is precisely the optimistic target-setting the floor exists to reject. **Fails.**
- **As `swing`** (floor 2.0, stop must clear 1.8 ATR for an ETF = 15.6 points): a stop below the capitulation low at 317 is only 1.61 ATR from a 331 entry and **fails the stop-distance floor**. Widening to 315 gives 1.84 ATR and risk 16.0, which then requires a target of **363.0 to reach exactly 2.00** — a ratio landing precisely on the floor, reachable only by setting the target at the pre-breakdown shelf. That is the "nudged until it passed" pattern `CLAUDE.md` names. **Fails on both honesty grounds.**
- Underneath the arithmetic, the fundamental driver is still adverse: gold fell 35% *because* of rising yields and hike expectations, and those have not reversed. The liquidation argument explains 11/18–11/20, not the 35%.
- **→ WATCHLIST with an explicit wait condition**, not a recommendation. Wait for either (a) GLD reclaiming its 20-day at 358.68, which would confirm the liquidation was the whole story, or (b) the Fed signalling a pause. SLV (-39.5% off high, ATR 4.52%) and GDX (-31.1%, ATR 5.85%) are the higher-beta versions of the same unconfirmed trade and are rejected for the same reason.

## [06:34 ET] INSIDERS — the one genuinely predictive signal, and it is present in three places
Checked per the skill's instruction on every de-rated equity finalist. Source: finnhub insider transactions (Code P = open-market purchase), 6-month window.

### DKS — a seven-person insider cluster bracketing today's price
`open_market_buys: 9, distinct_buyers: 7, buy_value_usd: $5,588,663`
| Date | Insider | Shares | Price |
| --- | --- | --- | --- |
| 2026-09-30 | Barnes Matthew | 3,665 | 136.39 |
| 2026-09-23 | Fitzgerald Larry Jr. | 1,860 | 131.67 |
| 2026-09-22 | Gupta Navdeep | 7,707 | 129.75 |
| 2026-09-01 | Colombo William J | 913 | 133.19 |
| 2026-08-27 | Barrenechea Mark J | 17,000 | 130.72 |
| 2026-08-27 | Colombo William J | 1,100 | 129.00 |
| 2026-08-26 | Eddy Robert W. | 4,000 | 128.70 |
| 2026-08-26 | Mathrani Sandeep | 1,550 | 128.89 |
- **Seven distinct insiders bought in a 128.70–136.39 band. DKS closed 133.67 — inside that band.** This is the cleanest "cheap rather than broken" confirmation available in public data, and it is sitting on the report's *worst* open position.
- DKS: -39.34% off its 90d high of 220.36; sma20 142.48, sma50 138.24; ATR 6.63 (**4.96%**); 90d low 120.15. 11/23 volume 3.76M was the heaviest of the window and came on an up day.

### CVS — the CEO bought, and the stock is now 5% below his price
`open_market_buys: 1, distinct_buyers: 1, buy_value_usd: $2,001,315, sells: 0`
- **Prem S. Shah (CEO), 23,855 shares @ $83.895 on 2026-11-06.** Zero insider sales in six months.
- CVS closed **79.65 — 5.1% BELOW the CEO's purchase price.** -28.04% off the 90d high of 110.68, 90d low 77.33, sma20 86.30, sma50 88.11, ATR 3.86 (4.85%).
- 11/23 printed a reversal bar: opened 77.80 (within 0.6% of the 90d low), closed 79.65.
- **The pending `CVS` BUY @ 80.0 from 2026-11-05 has now been reached.** Repetition warning honoured: CVS has been pitched 4x in 10 days and that is a flag, not conviction — but the insider buy is new information since the first pitch.

### HUN — the namesake CEO, but one buyer and underwater
- **Peter R. Huntsman, 100,000 shares @ $9.81 on 2026-08-03 ($981,000).** HUN is 8.54, i.e. 13% below the CEO's price. One buyer only. Open position at -5.1% with the stop at 8.09, just 5.3% below spot.

## [06:44 ET] POSITION UPDATE — DKS — opened 2026-11-13, -7.5% — decision: CLOSE
- Levels: entry 144.5 (filled, cannot be amended), target 175.5, stop 129.0. Spot 133.67. ATR 6.63 (4.96%).
- **The position is structurally broken and the arithmetic says so from spot rather than from entry:**
  - From entry the published numbers look fine — risk 15.5 (2.34 ATR, clears the 2.0 stock floor), reward 31.0, R:R exactly 2.0.
  - **From spot they are 9:1 against.** Target 175.5 is +31.3% away; stop 129.0 is -3.5% away, which is **0.70 ATR**. A driftless estimate of touching the target first is ~1/(1+9) ≈ **10%**, call it 15% with the insider edge. The break-even hit rate measured from the 144.5 entry is 33%. **Expectancy from here is negative at the position's own numbers.**
- **There is no honest repair available**, and I checked each route rather than assuming:
  - *Widen the stop* (the ATR argument for a 4.96% name): a stop at 120, below the 120.15 90d low, makes risk 24.5 from entry and R:R **1.27** — fails the 2.0 swing floor.
  - *Tighten the stop*: fails `check_stop_distance` and is the exact free-ratio gaming `CLAUDE.md` forbids.
  - *Amend the target down* to a reachable level: sma20 is 142.48, **below the 144.5 entry**, so any reachable target gives negative reward. The position cannot make money from its entry.
  - *Convert to `long_term`*: entry is fixed at 144.5; an honest bear case of 110 means risk 34.5 and a 2.5 floor demands a target of **230.75**, above the 220.36 90d high. Fails.
- **So: close it.** Entry price, not the thesis, is what is wrong — and an entry is the one thing a filled position may never amend.
- **The thesis itself is the best-evidenced long in the book, at a different price.** Seven distinct insiders bought $5.59M between 128.70 and 136.39, a band that brackets spot. 11/23 traded 3.76M shares, the heaviest of the window, on an up day. **Re-entry condition: a fresh long inside or below the 128.70-136.39 insider band, structured with its own 2.0+ ATR stop below the 120.15 low** — which is a genuinely separate trade once this one closes, not a re-pitch (see the re-trading rule in CLAUDE.md).

## [06:45 ET] DATA GAPS for data_quality_notes
- **Every index quote failed**: ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES/NQ futures, DXY, gold and WTI all `ok:false` — finnhub wants a CFD-index subscription, yahoo returned 429, stooq 404, no alphavantage key. All index context in this report is from **ETF proxies** (SPY/QQQ/IWM/GLD/USO/XLF/XHB), which are primary finnhub OHLCV.
- **Options-implied move unavailable**: `market_data.py implied` returned HTTP 401 from yahoo-options for both CVS and DKS, so the strategy's "is the target inside what options price" check **could not be run on any candidate today**. Targets are set on price structure and ATR alone.
- **Event-contract prices unavailable**: Kalshi's public endpoints returned null bid/ask/last/volume/OI for every `KXFEDDECISION`, `KXFED`, `KXCPIYOY` and `KXRATECUT` market. Hence zero event-contract recommendations despite the strategy actively wanting them — a probability disagreement cannot be stated without the market's price. The Fed odds quoted in this report come from news coverage of Kalshi/Polymarket/CME, not from a fetched quote.
- `market_data.py events "<topic>"` is **not a real search** — it pulls the first 200 open markets and substring-filters them, so "Fed" matched "Federico Bondioli" (a footballer) and returned no Fed markets. Series must be queried directly via `?series_ticker=`. Worth fixing.
- Gold's absolute price levels and the forced-selling attribution come from market commentary sites, not primary data; WGC Q4 central-bank figures are not published. GLD's own OHLCV is primary.
- All equity/ETF prices are the **2026-11-23 official close**, age ~843 minutes at 06:02 ET. That is a closed market ahead of a 09:30 ET open, not stale data.

## [06:54 ET] REMAINING POSITIONS — guidance not captured as candidates
Not every hold needs a recommendation. These are holds on unchanged levels with nothing new to say, plus two structural defects synthesis should surface.

- **`PFE` (entry 27.6, spot 27.40, target 42.0) and `CAG` (entry 14.4, spot 14.86, target 19.48) carry NO STOP and no stated invalidation condition.** `config/strategy.md` requires a stop *or* an explicit invalidation on every long equity idea, and neither has one. PFE has been open **69 days** and gone nowhere. This is a defect in how they were published, not a view on the businesses — flagging it rather than inventing a stop now, because a stop retro-fitted at a price the position never traded against is not a risk control.
- **`HUN`** (entry 9.0, spot 8.54, target 10.82, stop 8.09, ATR 0.3769 / 4.41%): CEO Peter Huntsman bought 100,000 shares at 9.81 on 2026-08-03, and the stock is 13% below his price. Same negative-expectancy shape as DKS — from spot the target is +26.7% and the stop -5.3%, roughly 5:1 against for a ~17% implied hit rate against a 33% break-even, and it cannot be repaired (a target at sma20 9.35 gives R:R 0.38). Lower conviction than DKS as an *idea* — one buyer, not seven. **Treated as a lottery ticket already struck; do not add, and let the 8.09 stop do its work.** Flagging for the red team rather than recommending, because at this size the exit saves little.
- **Holds on unchanged levels, nothing new to report**: `HII` (+9.4%, defence, rate-insensitive, working), `KHC` (+9.1%, working), `UNP`, `ABT`, `RTX`, `XLV`, `ADM`. None is near its stop.
- **Cancel these pending orders** (reasoning at 06:27 and 06:22): `GLD` SELL @ 406.77 and `/MBTZ6` SHORT @ 74075 — both stale by 18-19% of underlying move, right thesis, entry set above market, never filled, nothing earned. `KXFEDDECISION-26DEC-H0` YES @ 10 — thesis falsified, a hold is now ~3% priced.
- **Pending, levels unchanged, not advanced today**: `LEN` BUY @ 79.5 (spot 81.80 — regime conflict noted at 06:31), `VZ` BUY @ 46.0 (spot 46.45).

## [06:56 ET] CORRELATION AND SKEW — read this before synthesis adds anything
- Six of today's candidates, and the whole book, sit on **one driver: the Fed path into 2026-12-09**. The correlation cap in `config/strategy.md` is 3 ideas per driver. Today's new exposure respects it — `IWM` short is the only new directional rate bet; `TLT` and `XLU` are reframes of existing holds; `CVS` is deliberately rate-insensitive; `DKS` and `OXY` are risk reductions, not bets.
- **The honest skew to state in `data_quality_notes`: four of six candidates are position management, not new ideas, and only one (`CVS`) is a new entry.** That is what this tape deserves. The day after a +7% Nasdaq squeeze driven by a personnel reversal, with a 95%-priced hike eleven sessions out and a PCE print tomorrow morning, is not a day to add beta — it is a day to fix a book that is long defensives and duration into a hiking cycle.
- **Nothing intraday cleared the bar**, and nothing was forced to fill the lane: an intraday idea needs a same-session dated catalyst, and today's only scheduled item is Conference Board confidence. The real event is tomorrow at 08:30 ET.
- **No event contract and no futures idea**, both for stated reasons rather than neglect: event prices were unfetchable (06:19), and the futures-preferred short — `/MNQ` against the squeeze — was rejected because QQQ'\''s 3.70% ATR demands a 2.5 ATR futures stop of ~9.3%, which no reachable target repays, and because shorting the Nasdaq the session after Huang'\''s return with explicit White House backing is a fight I cannot size safely in a holiday week.
- Thanksgiving Thursday 11/26 is closed and Friday 11/27 is a 13:00 ET half day. Liquidity thins from Wednesday afternoon, which exaggerates any PCE surprise — a reason the `IWM` stop was left wide at 284.5 rather than pulled in.

## [06:58 ET] RESEARCH COMPLETE
- **candidates: 6** — IWM (short, hold, c4), TLT (hold as hedge, c3), CVS (new entry, c3), DKS (close, c3), XLU (hold, c3), OXY (hold on short leash, c2)
- **the day's central fact**: the Fed is ~95% priced to HIKE 25bp on 2026-12-09 with a second January hike ~57% priced, core PCE consensus re-accelerates to 3.2% at tomorrow 08:30 ET, and Monday'\''s +7.0% QQQ squeeze repriced a CEO'\''s job title while repricing nothing about rates.
- **coverage gaps**: no options-implied check on any candidate (yahoo 401); no event-contract prices (Kalshi public endpoints null); no index/VIX/DXY/futures quotes (finnhub subscription, yahoo 429, stooq 404) so all index context is ETF proxies; no fundamentals or valuation command exists in `market_data.py`, which is why CVS could not be published as `long_term` and why no `long_term` idea appears today; gold level and attribution data is commentary-sourced, not primary; did not reach small/micro-cap screening or crypto beyond the macro print.
- **sources that failed**: finnhub CFD indices (^GSPC ^NDX ^DJI ^RUT ^VIX), yahoo chart API (429), stooq (404), alphavantage (no key), yahoo-options (401), Kalshi public price fields (null), `market_data.py events` substring search (returns footballers for "Fed").
