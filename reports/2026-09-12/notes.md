# Research log — 2026-09-12

## [06:02 ET] SETUP — Saturday run
- 2026-09-12 is a **Saturday**. US equities and futures cash sessions closed.
  Per config/strategy.md weekend rules: crypto and event contracts carry the
  actionable load; equities are week-ahead preparation with entries for the
  next open (Mon 2026-09-14). All equity ideas marked `swing`.
- Prior context read. 11 open positions, 15 awaiting entry, 6 closed trades
  0/6 to target, avg -3.9%. **Sample is 6 closed — under the ~15 threshold, so
  it is noise and I will not over-fit to it.** One pattern is still worth
  respecting: all 6 closed were `swing`, and 5 of the last 5 stop-outs were
  long equity in a tape that has been unkind to longs.

## [06:02 ET] MACRO — rates, policy, tape
- FRED US10Y **4.95%** (2026-09-10) — source: https://fred.stlouisfed.org/series/DGS10
- FRED US2Y **4.56%** (2026-09-10) — source: https://fred.stlouisfed.org/series/DGS2
- FRED effective fed funds **3.63%** (2026-09-10) — source: https://fred.stlouisfed.org/series/DFF
- FRED 10y-2y spread **+0.33** (2026-09-11) — source: https://fred.stlouisfed.org/series/T10Y2Y
- FRED unemployment **4.1%** (2026-08-01) — source: https://fred.stlouisfed.org/series/UNRATE
- Read: the long end at 4.95% with effective funds at 3.63% is a **bear
  steepener** — policy rate well below the 10y and the curve positively sloped
  by a third of a point. Term premium, not growth. This is the single most
  important macro fact on the page today and it frames the equity lane:
  long-duration equity and rate-sensitive assets (REITs, utilities, long
  Treasuries) are fighting the tape; real assets and short-duration cash flows
  are not.
- TLT proxy `bonds_20y` last 80.87, +0.11% (2026-09-11 close, session closed)
- DATA GAP: Yahoo returned **HTTP 429 (rate limited)** on every index and
  equity quote this run — ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES, NQ, DXY, ^TNX,
  gold and WTI all failed across finnhub/yahoo/stooq/alphavantage. No index
  level, no VIX level and no dollar level is available this morning. I will
  not state one. Equity prices below come from whatever source answers, and
  where none does the price is recorded as unknown.

## [06:03 ET] CRYPTO — 24/7, the live market today
- BTC **$77,323**, +0.39% 24h, $32.8B volume, $1.553T cap — source: https://www.coingecko.com/en/coins/bitcoin
- ETH **$2,530.22**, +2.49% 24h, $23.9B volume — source: https://www.coingecko.com/en/coins/ethereum
- SOL **$101.99**, +2.62% 24h, $4.50B volume — source: https://www.coingecko.com/en/coins/solana
- Note vs prior context: the 2026-08-16 `BTC SELL @ 63,400` and 2026-08-18
  `/MBTU6 SHORT @ 64,340` never filled, and BTC is now 77.3k — roughly 20%
  above those levels. Those short entries are stale by a wide margin and
  should not be re-pitched at those prices.

## [06:12 ET] CALENDAR — the week ahead
Dated events inside the next 10 sessions (all fetched, none remembered):
- **FOMC decision Wed 2026-09-16**, Kalshi market close 17:59Z = **13:59 ET**
  — source: https://api.elections.kalshi.com/trade-api/v2/markets/KXFEDDECISION-26SEP-H0
- Earnings (finnhub calendar, fetched this run):
  - Mon 2026-09-14 bmo **CBRL**, amc **PLAY**
  - Tue 2026-09-15 **GIS**, bmo **VRA**
  - Wed 2026-09-16 **FDX** (est EPS 4.05, rev $22.59B), amc **LEN** (est EPS 1.31, rev $8.40B)
  - Tue 2026-09-22 amc **AZO**, amc **KBH** (est 0.90), bmo **THO** (est 0.92, rev $2.195B), **FERG**
  - Wed 2026-09-23 **CTAS**, **PAYX**, amc **SFIX**
  - Thu 2026-09-24 amc **COST** (est 6.69), **DRI**, bmo **BXMT**, bmo **SNX**
  - source: https://finnhub.io/api/v1/calendar/earnings
- Next CPI print is **September CPI on 2026-10-14** (KXCPI-26SEP close 12:25Z),
  i.e. **outside** a 10-session window. August CPI has already resolved. So the
  FOMC is the only tier-one macro print next week.

## [06:14 ET] MACRO — THE finding of the day: the Fed is priced to HIKE
Kalshi KXFEDDECISION-26SEP, fetched per-market (see data note below):

| Outcome | Yes bid/ask | Last | Previous | Open interest |
| --- | --- | --- | --- | --- |
| Cut >25bp | 0/1c | 1c | 1c | $1.27M |
| Cut 25bp | 0/1c | 1c | 1c | $7.47M |
| **Hold (0bp)** | **20/21c** | **21c** | **39c** | $16.5M |
| **Hike 25bp** | **80/81c** | **81c** | **61c** | $6.29M |
| Hike >25bp | 1/2c | 2c | 1c | $10.6M |

- The market prices an **81% probability the Fed hikes 25bp on Wednesday**, and
  it has repriced hard — the hike leg went 61c -> 81c and the hold leg 39c ->
  21c. $8.1M traded in the hold leg alone in 24h, so this is a liquid, actively
  repriced view, not a stale quote.
- Path beyond September: **Oct** hold 62c / hike 38c; **Dec** hold 44c / hike
  58c. That is a hike-pause-hike path, not a one-off.
- source: https://api.elections.kalshi.com/trade-api/v2/markets/KXFEDDECISION-26SEP-H25
- **This reframes the entire report.** Effective funds 3.63%, 10y 4.95%, curve
  +33bp, and a Fed that the market thinks is *tightening*. Consequences I will
  trade off rather than around:
  - Long duration and rate-sensitives (TLT, REITs, utilities) are the wrong
    side. The existing TLT exit and IYR short are consistent with this.
  - Crypto is a liquidity asset going into a tightening print.
  - Housing-levered cyclicals face 4.95% tens with LEN printing the same day.
  - I will NOT pitch the 81c hike leg itself. 81c into a two-day-out, heavily
    traded FOMC is the consensus, and buying consensus at 81c risks 81 to make
    19 with no information the market lacks. There is no probability
    disagreement to state, so per config/universe.md there is no trade.

## [06:14 ET] DATA QUALITY — market_data.py events is returning null prices
- `scripts/market_data.py events` reports every price field as `null`. Cause:
  Kalshi's API now returns `yes_bid_dollars` / `yes_ask_dollars` /
  `last_price_dollars` / `volume_24h_fp` / `open_interest_fp`, and the parser in
  `events()` (scripts/market_data.py:752) still reads the old `yes_bid`,
  `yes_ask`, `last_price`, `volume`, `open_interest` names. Secondary problem:
  it fetches at most 200 open markets and filters client-side, so a search for
  "Fed" or "CPI" returns sports markets and a count of 0 rather than the series.
- Worked around this run by querying the series and market endpoints directly.
  **Every event price in these notes came from that direct fetch**, not from the
  CLI. Flagging for the synthesis phase: this is a code bug, not a dead source.

## [06:19 ET] LEVELS — fetched price history, 120 sessions, source nasdaq via market_data.py
| Sym | Close 2026-09-11 | ATR14 | ATR% | SMA20 | SMA50 | 120d hi | 120d lo | off hi | $vol 30d |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 764.29 | 5.60 | 0.73% | 766.88 | 758.62 | 779.37 | 629.28 | -1.93% | $30.8B |
| TLT | 80.87 | 0.66 | 0.82% | 82.20 | 82.99 | 87.79 | 80.665 | -7.88% | $2.67B |
| GLD | 398.77 | 7.90 | 1.98% | 409.43 | 391.22 | 448.70 | 363.32 | -11.13% | $4.49B |
| BCC | 75.44 | 2.22 | 2.94% | 79.16 | 78.88 | 88.43 | 65.00 | -14.69% | $23.1M |
| LCII | 91.02 | 3.20 | 3.51% | 101.67 | 103.68 | 138.15 | 89.00 | -34.12% | $23.7M |
| CCJ | 96.68 | 3.76 | 3.89% | 100.03 | 95.18 | 131.21 | 83.15 | -26.32% | $267M |
| NKE | 36.80 | 0.94 | 2.55% | 39.01 | 41.16 | 54.22 | 36.55 | -32.13% | $996M |
| LULU | 98.97 | 5.81 | 5.87% | 114.16 | 117.13 | 170.20 | 95.67 | -41.85% | $557M |
| SVRA | 5.30 | 0.197 | 3.72% | 5.44 | 5.60 | 6.475 | 4.695 | -18.15% | $7.77M |
| DVN | 50.23 | 1.18 | 2.34% | 48.27 | 45.45 | 52.71 | 40.00 | -4.70% | $525M |
| XLE | 65.14 | 1.21 | 1.86% | 63.72 | 60.14 | 66.17 | 52.62 | -1.56% | $1.74B |
| IYR | 100.75 | 1.10 | 1.10% | 103.29 | 104.17 | 108.17 | 92.45 | -6.86% | $513M |
| PATK | 73.40 | 2.66 | 3.63% | 82.37 | 84.37 | 121.39 | 73.055 | -39.53% | $33.5M |
- Note: `sma200` came back null for every symbol — the 120-day window cannot
  compute a 200-day average. Not a source failure, a window limit.

## [06:22 ET] POSITION UPDATE — SPY — SELL_SHORT opened 2026-08-31 @ 773, last 764.29, +1.1%
- decision: **hold as-is** through Wednesday's FOMC. No level changed.
- why: the catalyst improved after the position was opened — the Sept hike leg
  repriced 61c -> 81c. Entry 773, stop 783.50, target 750 gives R:R 2.19 and a
  stop 1.88 ATR away (ATR14 5.60), clearing the 1.8 ATR ETF floor. I deliberately
  did NOT walk the stop in to flatter the ratio; the stop sits above the 779.37
  120-day high, which is where the thesis is actually wrong.
- added a second target at 735 for the runner, kept target 1 at 750.
- action: captured via add_candidate.py.

## [06:30 ET] POSITION UPDATE — LCII — BUY opened 2026-08-18 @ 94.00, last 91.02, -3.2%
- decision: **CLOSE Monday. Thesis invalidated — and invalidated by a fact that
  was true before the position was ever opened.**
- LCII has been under an **all-stock merger agreement with Patrick Industries
  (NASDAQ: PATK) since 2026-06-30**, at a fixed **1.2440 PATK shares per LCII
  share**. Source (read in full):
  https://www.sec.gov/Archives/edgar/data/763744/000076374426000049/pressreleasefinal.htm
- Deal math, all from fetched closes: PATK 73.40 x 1.2440 = **$91.31** of deal
  value against LCII at **$91.02**. Gross spread **0.32%**.
- The open position's **138 target requires PATK at 110.93**, a +51% move in the
  acquirer. It is not a price target, it is an arithmetic impossibility.
- The -11.3% slide in LCII from 2026-09-04 to 2026-09-11 is not LCII news: PATK
  fell -11.4% over the identical five sessions. The ratio held. LCII is a PATK
  proxy.
- **New dated development**: 2026-09-10 Form 425/8-K discloses the HSR
  notification was **voluntarily withdrawn 2026-09-04 and refiled 2026-09-09**,
  restarting the waiting period — the standard pull-and-refile used to give the
  FTC more time instead of taking a Second Request. Horizontal merger between the
  two largest RV component suppliers. 0.32% is not payment for that risk.
  Source: https://www.sec.gov/Archives/edgar/data/763744/000076374426000085/lciiform-hsrrefiling2026.htm
- **Process note for the record, not an excuse:** the merger was announced
  2026-06-30 and the position was opened 2026-08-18 — seven weeks later — with a
  138 target. A prior run recommended a company that was already being acquired
  and set a target above the deal value. Checking `filings` before publishing an
  equity would have caught it; I am flagging it so synthesis reports it rather
  than quietly closing the trade.
- action: captured via add_candidate.py as a `sell` (close), conviction 5.

## [06:31 ET] REJECTED — LCII merger arb — 0.32% gross spread with an HSR pull-and-refile live; not paid for antitrust risk.
## [06:31 ET] REJECTED — KXFEDDECISION-26SEP-H25 YES @ 81c — consensus at 81c two days out, $6.3M OI; no probability disagreement to state, so no trade under config/universe.md.

## [06:08 ET] TIMESTAMP CORRECTION
The `[06:12]`–`[06:31]` stamps above were estimated, not read off the clock, and
they ran ahead of it — a `date` call at this point in the run returns **06:08
ET**. The findings and their order are unaffected; only the labels were wrong.
All stamps from here are read from `date`. Logged rather than silently fixed,
since notes.md is the audit trail for when a finding was actually made.

## [06:15 ET] MACRO — why the Fed is hiking: inflation re-accelerated
Kalshi KXCPIYOY-26SEP (CPI YoY, year ending Sept 2026, resolves 2026-10-14),
fetched per-market:

| Strike | Yes bid/ask | Last | Previous | OI |
| --- | --- | --- | --- | --- |
| >3.0% | 96/100c | 97c | 96c | $1.1K |
| >3.2% | 91/100c | 88c | 83c | $3.9K |
| **>3.4%** | **73/96c** | **77c** | **54c** | $5.0K |
| >3.6% | 24/28c | 28c | 32c | $3.1K |
| >3.8% | 8/25c | 9c | 10c | $2.7K |
| >4.0% | 3/11c | 2c | 6c | $0.7K |

- Implied central expectation is CPI YoY around **3.45–3.55%** — 77% above 3.4%,
  28% above 3.6%. Against a 2% target that is the reason for the hike, and the
  **>3.4% leg repriced 54c -> 77c**, so the inflation surprise is recent.
- This makes the whole picture coherent and worth stating once: inflation
  re-accelerated to ~3.5%, the Fed is priced 81% to hike Wednesday, the 10y is
  at 4.95% and the curve is +33bp. Every idea below is positioned inside that.
- source: https://api.elections.kalshi.com/trade-api/v2/markets/KXCPIYOY-26SEP-T3.4
- Kalshi KXU3-26SEP (Sept unemployment, resolves 2026-10-02): >4.0% 68/69c,
  >4.1% 45/47c, >4.2% 11/15c. Last actual U3 is 4.1% (Aug). So the labour market
  is not what is driving this — the market sees essentially no unemployment
  spike. It is an inflation-driven hike, not a policy error being priced.
- **LIQUIDITY WARNING on the macro event lane.** Open interest on every CPI and
  U3 strike above is $700–$8,400 and spreads are enormous — the >3.4% CPI leg is
  73 bid / 96 ask, a 23-cent spread on a 77c mid. These are not tradeable at any
  size and I am **not** recommending any of them. Recording the prices because
  they are the best read available on priced inflation, not because they are a
  trade. Only the KXFEDDECISION-26SEP legs ($6–17M OI) are genuinely liquid.

## [06:16 ET] LEVELS — crypto, true DAILY bars
CoinGecko 4-hourly OHLC over 30 days, aggregated to daily by me, so ATR below is
a real daily ATR. (An earlier 90-day pull returned 4-DAY candles and an "ATR" of
$4,086 for BTC — that figure is a 4-day range and must not be used as a daily
ATR. Discarded.)

| Coin | Last (Sat 06:16 ET) | Daily ATR14 | ATR% | 90d high | 90d low |
| --- | --- | --- | --- | --- | --- |
| BTC | 77,258 | 1,982 | 2.57% | 82,108 | 57,779 |
| ETH | 2,523 | 86.69 | 3.44% | 2,647.68 | 1,513.48 |
| SOL | 101.64 | 4.11 | 4.04% | 110.17 | 64.04 |
- All three are in strong uptrends — BTC +33.7% off its 90-day low and only 6%
  below the high, ETH +66.7% off its low, SOL +58.7%.
- **The tension worth naming: crypto is rallying into a tightening Fed, while
  gold is 11.1% BELOW its 120-day high.** If this were one shared debasement
  trade the two would move together and they are not. That contradiction is why
  I am NOT taking a directional crypto position today — I cannot tell from
  fetched data whether crypto is leading a liquidity story or lagging a
  repricing, and "BTC looks strong" is a vibe, not a thesis. Recorded as an open
  question rather than dressed up as a trade.

## [06:17 ET] REJECTED — homebuilder short (LEN/KBH/ITB) — the move already happened.
- LEN 79.60 (-18.7% off 120d high, ATR 2.25), KBH 49.16 (-22.7%, ATR 1.60),
  ITB 89.54 (-15.8%, ATR 1.93). All three below both SMA20 and SMA50.
- The setup looks tempting — LEN prints 2026-09-16 amc, the same day as the
  FOMC, and KBH 2026-09-22, with the 10y at 4.95%. But shorting a group already
  down 16–23% and sitting near its 120-day low, into a print, with the hike 81%
  priced, is selling the news after the move. Rejected as late, not as wrong.
- Kept as the honest counterweight to the BCC decision below rather than traded.

## [06:13 ET] POSITIONING — relative strength, fetched not asserted
| Pair | 1m | 3m | 6m |
| --- | --- | --- | --- |
| XLE vs SPY | **+7.79%** | **+10.44%** | -1.48% |
| CCJ vs XLE | -9.10% | -16.35% | -29.42% |
| GLD vs SPY | -0.46% | -0.38% | **-29.34%** |
| NKE vs XLY | -8.10% | -23.53% | **-46.77%** (vs SPY) |
- **Energy is the leadership group** and it is the one real-asset expression
  that is actually working in a 3.5%-inflation regime. XLE 65.14, only 1.56%
  below its 120-day high, +23.79% off the low.
- **Gold is not working**, and uranium is lagging even energy.
- Absolute: XLE +6.73%/+14.04%/+13.27% (1m/3m/6m) vs SPY -1.06%/+3.60%/+14.75%.

## [06:17 ET] POSITION UPDATE — BCC — BUY opened 2026-08-18 @ 76.50, last 75.44
- decision: **CLOSE Monday**, roughly flat, on changed information not on loss.
- why: BCC is a housing-starts bet and the macro input inverted — the thesis
  needed rate relief and got an 81%-priced hike with the 10y at 4.95%.
- the distinction from the rejected homebuilder short, stated because it is the
  obvious objection: BCC is **14.69%** off its 120-day high where KBH is 22.74%
  and LEN 18.73%. BCC has not yet discounted what the builders have. That is one
  observation, and it argues both against a fresh short down there and against a
  long up here.
- action: captured via add_candidate.py.

## [06:19 ET] POSITION UPDATE — GLD — BUY opened 2026-08-22 @ 398.00, last 398.77
- decision: **CLOSE at market. AMENDMENT — the standing 2026-09-08 exit at
  406.77 is lowered to ~398.77.** Stop waiting for a 2% bounce into a hawkish
  catalyst.
- why: the inflation-hedge thesis failed a test I could actually run. Over the
  window in which the Kalshi CPI >3.4% leg repriced 54c -> 77c, GLD fell to
  11.13% below its 120-day high and gave up 29.34 points to SPY over 6 months.
  Gold is trading off the real yield, and 4.95% nominal against ~3.5% CPI is a
  positive real yield that a hiking Fed widens.
- the 520 target was a debasement call. Debasement is not what is being priced.
- action: captured via add_candidate.py.

## [06:20 ET] CORRELATION CAP — energy is full, deliberately not adding a 4th
XLE leadership is the cleanest signal on the page and I am **not** trading it,
for two reasons that both come from the config:
- The book already carries **three** unfilled energy ideas — XLE @ 63.90,
  DINO @ 99.50, DVN @ 49.60. config/strategy.md caps ideas sharing one driver at
  three. A fourth would be one bet with extra steps.
- XLE has been recommended **4 times in 10 days** per prior_context.md, and its
  63.90 entry is now stale — the ETF is at 65.14 and ran away without filling.
  Re-pitching it a fifth time at a higher price is the anchoring failure the
  repetition guard exists to catch, not conviction.

## [06:22 ET] REJECTED — KXFEDDECISION-26OCT-H25 YES @ 38c — the "mispricing" is the SEP calendar
- Tempting setup: October hike priced 37/38c but **December priced 58c**. A
  higher probability at the later meeting looks like the market expecting a
  skip, and at the start of an inflation-driven hiking cycle consecutive moves
  are the historical norm. That would make 38c cheap.
- **Falsified it before pitching it.** Fetched the remaining 2026 meeting dates
  from the Kalshi series: **Sept 16, Oct 28, Dec 9** — and September and December
  are Summary of Economic Projections meetings while **October is not**. The Fed
  strongly prefers to move at SEP meetings. So Oct 38c < Dec 58c is explained by
  the meeting calendar, which is an institutional fact, not a mispricing.
  There is no probability disagreement left to state once that is accounted for.
- source: https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXFEDDECISION
- Combined with the September leg being consensus at 81c and every CPI/U3 strike
  being untradeably illiquid, **the event-contract lane produces nothing today.**
  That is the honest outcome, not a gap I failed to fill — config/universe.md
  wants these hunted, and I hunted them; it also requires a stated probability
  disagreement, and I do not have one.

## [06:24 ET] CRYPTO — no directional trade, and why
- Crypto is the only live market on a Saturday, so a blank here needs a reason.
- BTC 77,258 (daily ATR14 1,982 = 2.57%), ETH 2,523 (86.69 = 3.44%), SOL 101.64
  (4.11 = 4.04%). All three in strong uptrends: BTC +33.7% off the 90-day low
  and 6.0% below the high.
- The case for a short into Wednesday is that crypto is a liquidity asset going
  into a tightening print. The case against is that it has already rallied
  straight through the entire hike repricing — the Sept leg went 61c -> 81c while
  BTC went up. The liquidity mechanism has visibly not been operating.
- Against that, gold is 11.1% BELOW its high over the same period. Crypto up,
  gold down, both supposedly debasement assets. **I cannot reconcile those two
  from fetched data**, and a directional crypto bet here would be a guess about
  which one is telling the truth.
- So: no crypto candidate. Under config/universe.md a bearish view would have to
  be a short /MBT contract anyway, and I am not putting a leveraged futures short
  on a hunch. Recorded as the day's biggest open question.

## [06:26 ET] POSITION UPDATE — NKE — BUY opened 2026-08-17 @ 40.75, last 36.80
- decision: **complete the exit**, reaffirming the 2026-09-08 sell at 38.40.
- new evidence the original exit did not have: RS **-46.77% vs SPY over 6m**,
  the worst of anything examined today; analyst bullish share 39.1% and **-9.8
  points**, buys cut 12 -> 8 and sells raised to 3 since June; price 0.68% off
  the 120-day low. Earnings 2026-09-28 (fetched), est EPS 0.4523.
- the honest tension: 4 insiders bought **$3.73M** open-market in April at
  ~$42.27-42.43. That is a real cluster and it argues the other way. It is also
  five months old and 13% underwater, so it has been tested and has failed.
- action: captured.

## [06:27 ET] POSITION UPDATE — LULU — BUY opened 2026-08-22 @ 115.00, last 98.97
- decision: **complete the exit**, reaffirming the 2026-09-08 sell at 100.61.
- why: bullish share **5.0%**, -15.5 points (1 SB / 1 B / 31 H / 5 S / 2 SS), and
  crucially **no earnings until 2026-12-09** — no dated mechanism inside a swing
  horizon to close the gap. -13.9% vs entry.
- counterweight stated rather than buried: 5% bullish with 3 beats in the last 4
  prints is washed-out positioning and this is the profile that snaps back
  hardest. The exit is on timing, not on the business.
- action: captured.

## [06:28 ET] POSITION UPDATE — SVRA — BUY opened 2026-08-23 @ 5.35, last 5.30
- decision: **hold, levels unchanged** (stop 4.60, target 8.00).
- checked rather than assumed: latest filings are a 10-Q and S-8 both 2026-08-11,
  no 8-K, no dated catalyst. Insiders: **0 open-market buys, 1 sale of $2.24M**.
- stop is 3.81 ATR from entry, well clear of the 2.0 floor. Stays a 1% lottery
  ticket. The negative insider print is published rather than omitted.
- action: captured at conviction 2 with the thinness in key_risk.

## [06:29 ET] POSITION UPDATE — TLT — SELL @ 81.87 opened 2026-09-02, last 80.87, +1.3%
- decision: **exit stands, and I am deliberately NOT opening a new TLT short.**
- the macro says short duration: 10y 4.95%, Fed 81% to hike, curve +33bp. But
  two things say do not act on it here:
  - TLT at 80.87 is **0.25% above its 120-day low of 80.665**. Shorting the low
    after the hike is 81% priced is the same "late" objection I used to reject
    the homebuilder short, and I will not apply it inconsistently.
  - **TLT has been recommended 5 times in 10 days** — the single largest
    repetition count in prior_context.md. That is the anchoring signal the guard
    exists for.
- no candidate captured. Being right about duration does not entitle the report
  to a sixth TLT pitch at the low.

## [06:24 ET] THEME — bond proxies are de-rating, and that is the tradeable read
Everything that competes with a 4.95% risk-free yield is being sold, and the
fetched numbers line up across unrelated sectors:
| Proxy | Last | Off 120d high |
| --- | --- | --- |
| XLU (utilities) | 42.39 | **-11.14%** (1.27% off the LOW) |
| GIS (staples) | 35.85 | **-15.05%** (38.29 -> 35.85, -6.4% in 5 sessions) |
| IYR (REITs) | 100.75 | -6.86% |
| TLT (duration) | 80.87 | -7.88%, 0.25% off the low |
| GLD | 398.77 | -11.13% |
- That is five unrelated things falling for one reason. It is the clearest
  regime signal on the page, and it is the reason GLD and BCC are exits above.
- I am not shorting any of them. All five have already made the move, which is
  the same objection that rejected the homebuilder short and the TLT re-pitch.
- **The way to trade a theme this late is the long side of it**, which is MET.

## [06:27 ET] NEW IDEA — MET — BUY @ 97.14, stop 92.90, target 106.00 / 112.00
- The only long initiated today and the only genuinely new idea, the rest of the
  report being position management.
- mechanism: a life insurer earns the yield on its float, so it reinvests
  maturing bonds at the new higher curve. Higher-for-longer is a direct earnings
  tailwind — the opposite sign to every other name here.
- confirmation, fetched: MET vs XLF **+1.56% / +7.32% / +26.46%** (1m/3m/6m);
  analyst bullish share **70.8% and improving** (+1.2); **beat 4 of last 4**
  prints. Above both SMA20 (96.17) and SMA50 (95.16). $308.6M average daily
  dollar volume, so liquidity is a non-issue.
- **stop set before the target**, per config/strategy.md: 92.90 sits below the
  50-day and below the 2026-09-09 swing low of 94.88, at **2.29 ATR** (ATR14
  1.8536) — clear of the 2.0 stock floor. Only then the target: 106.00 gives
  **2.09:1**, just over the 2.0 swing floor. I did not tighten the stop to
  improve that number; if 2.09 is too thin for the red team, the idea should be
  cut rather than the stop moved.
- entry is **at the market, not a reflex pullback discount** — prior_context
  shows 31 pullback entries against 1 breakout with a 42% fill rate, and MET is
  in an uptrend 3.76% off its high. An entry below the market here would only
  fill if the thesis first broke.
- win_probability 0.42 against a 0.324 baseline = **+9.6 points of claimed edge**.
- insider check run and it is a mild negative, published rather than omitted:
  one $1.74M sale, zero open-market buys in 6 months.
- action: captured, conviction 4 (3 distinct evidence kinds).

## [06:28 ET] REJECTED — PATK BUY — considered seriously, rejected on the cycle
- Tempting: PATK 73.40 is at its 120-day low (73.055) and **-39.53%** off the
  high, and I had already read the merger release — the LCII deal creates the
  dominant RV components supplier with **$150M+ stated run-rate synergies**.
  Buying the acquirer at a 40% drawdown is the classic setup.
- Rejected because an RV supplier is the most rate-sensitive discretionary
  supply chain there is, and the macro is a hiking Fed with the 10y at 4.95%.
  The read-through confirms it: THO, the largest RV OEM, is 72.86 and -14.29%
  off its high, printing 2026-09-22. Buying the bottom of a rate-driven
  discretionary downcycle two days before the Fed tightens into it is not a
  contrarian entry, it is an early one. Antitrust risk from the pull-and-refile
  sits on top.
- Noted also because it would have been inconsistent to sell LCII for being a
  PATK proxy and then buy PATK the same morning without saying why.

## [06:29 ET] REJECTED — GIS / CBRL / PLAY / FDX earnings setups — all late or thin
- GIS 35.85 prints 2026-09-15, but it has already fallen 6.4% in five sessions
  into the print; shorting that is chasing and buying it is catching it.
- CBRL 49.48 (prints 2026-09-14 bmo) is -17.89% off its high with a 4.37% ATR;
  PLAY 8.14 (2026-09-14 amc) is -45.81% off its high. Both are small-cap
  earnings coin flips with no evidence edge I could fetch — exactly the
  conviction-1 hunch the config says not to publish.
- FDX 311.99 prints 2026-09-16 amc, the same afternoon as the FOMC. A freight
  bellwether stacked on top of a rate decision is two binary events on one
  position; no.

## [06:31 ET] SECTORS — full relative-strength sweep vs SPY (1m/3m/6m)
| Sector | Absolute | vs SPY |
| --- | --- | --- |
| XLE energy | +6.73/+14.04/+13.27 | **+7.79/+10.44/-1.48** |
| XLF financials | -1.16/+8.80/+17.24 | -0.10/+5.20/+2.49 |
| XLK tech | -0.63/+2.43/+36.15 | +0.43/-1.17/**+21.40** |
| XLV healthcare | -1.83/+7.31/+10.12 | -0.77/+3.71/-4.63 |
| XLC comms | +2.11/+0.43/-2.32 | +3.17/-3.17/-17.07 |
| XLP staples | -2.00/-2.22/-1.03 | -0.94/-5.82/**-15.78** |
| **XLI industrials** | **-7.27/-1.59/+4.31** | **-6.21/-5.19/-10.44** |
- XLP at -15.78% over 6m is the bond-proxy de-rating quantified at sector level.
- **XLI is the standout weak spot**, and uniquely its 1m relative loss (-6.21) is
  WORSE than its 3m (-5.19) — the only sector where the damage is accelerating
  rather than fading. That shape is what separates it from housing and duration.

## [06:33 ET] NEW IDEA — XLI — SELL_SHORT @ 175.50 (wait for the bounce), stop 180.80, target 161.00
- thesis: Fed tightening into a decelerating goods economy. FDX, the freight
  bellwether, is already -9.66% off its high and prints 2026-09-16, the same
  afternoon as the decision.
- **entry waits for a bounce into 174.00-177.50** — I am not shorting 172.37 at
  the low, which is the exact mistake I rejected twice already today. The zone is
  the declining 20-day SMA at 177.58. `wait: true`. If it never bounces the idea
  does not fill, and that is the correct outcome rather than a miss.
- stop first at **180.80**, above the declining 50-day (180.32) = **2.29 ATR**
  (ATR14 2.3125), clear of the 1.8 ETF floor. Target 161.00 then falls out at
  **2.74:1**, and sits above the 120-day low of 156.08 so it is inside ground
  already traded.
- win_probability 0.38 vs a 0.268 baseline = **+11.2 points** of claimed edge.
- **correlation disclosed, not buried**: XLI is a component of SPY and I am
  already short SPY. The two lose together. Sized **2%** rather than 3% for that
  reason, and that is 2 of the 3 ideas permitted on one driver.

## [06:35 ET] SKEW — this report is deliberately defensive, and here is the honest count
Of 10 candidates: 1 new long (MET), 2 shorts (SPY existing, XLI new), 5 exits
(LCII, BCC, GLD, NKE, LULU), 2 holds (CCJ, SVRA). That is a lopsided,
risk-reducing report and config/strategy.md asks that the skew be named rather
than balanced away:
- It is earned by fetched data, not by mood — a Fed priced 81% to hike, CPI
  ~3.5%, a 4.95% 10y, five unrelated bond proxies de-rating together, and
  industrials breaking down.
- It is NOT an attempt to fit the 0/6 track record. Six closed trades is well
  under the ~15 threshold and is noise; I have not raised any bar because of it.
- **No intraday ideas.** It is a Saturday — there is no intraday setup to have,
  and inventing one would be fabrication. All equity entries are for the Monday
  2026-09-14 open.
- **No crypto and no event contracts**, each rejected with a stated reason above
  rather than skipped. On a weekend run that is the lane expected to carry the
  report, so the absence is a real finding: the FOMC leg is consensus at 81c,
  every CPI/U3 strike is untradeably illiquid, and the crypto/gold divergence is
  unresolved.

## [06:38 ET] STALE RESTING ORDERS — checked all 15 awaiting-entry items. Two need action.
Fetched every pending level against Friday's close. Distances are market vs the
published entry:

| Pending | Entry | Last | Distance | Read |
| --- | --- | --- | --- | --- |
| `KXFEDDECISION-26SEP-H0` YES | **47c** | **20/21c** | **-55%** | **CANCEL — see below** |
| `DG` BUY | 134.50 | 124.58 | **-7.38%** | **stale, needs re-underwriting** |
| `VST` BUY | 128.00 | 148.38 | +15.92% | dead level, will not fill |
| `DINO` BUY | 99.50 | 107.84 | +8.38% | far below market |
| `PFE` BUY | 25.80 | 27.72 | +7.44% | far below market |
| `CEG` BUY | 272.00 | 284.75 | +4.69% | below market |
| `EEM` BUY | 65.60 | 67.84 | +3.41% | below market |
| `XLE` BUY | 63.90 | 65.14 | +1.94% | below market, ran away |
| `IYR` SELL_SHORT | 103.60 | 100.75 | -2.75% | needs a 2.8% bounce to fill |
| `BTC` SELL @ 63,400 / `/MBTU6` SHORT @ 64,340 | — | BTC 77,258 | **+22%** | dead, ~20% through |

**1. `KXFEDDECISION-26SEP-H0` YES @ 47c must be cancelled. This is the single
most urgent line in today's report.** It is a resting order to buy "the Fed
maintains rate" at 47 cents. That contract is **20 bid / 21 ask** right now and
it **resolves Wednesday 2026-09-16**. Paying 47c for a 21c outcome is paying
more than twice the market's probability for something that settles in two
sessions, and there is no time for it to be wrong-but-early. Note this is *not*
a view that the hold outcome is mispriced — I declined to trade the other side
at 81c for lack of an edge. It is only that 47c is the wrong price for it.
source: https://api.elections.kalshi.com/trade-api/v2/markets/KXFEDDECISION-26SEP-H0

**2. `DG` BUY @ 134.50 needs re-underwriting before it is allowed to execute.**
The market at 124.58 is 7.38% **below** the published entry, so a resting limit
buy at 134.50 is no longer a pullback entry at all — the pullback already
happened and overshot. The target and stop that were set around 134.50 do not
describe the trade a fill would now produce. I did not have budget to research
DG properly today, so I am flagging it rather than silently repricing it:
**re-underwrite or cancel, do not let it fill on the old levels.**

The remaining buy orders are simply below market and harmless — they wait, which
is what a limit order is for. `VST` at 128.00 against a 148.38 market is 15.92%
away and should be treated as expired rather than pending.

## [06:41 ET] REJECTED — DG — re-underwrote it properly; it no longer clears the floors
Followed up rather than leaving the flag above as a punt, and the answer is a
clean no. The business case is fine and arguably better than when it was
written: DG has **beaten in 4 of its last 4 prints**, and consumer trade-down is
a real mechanism with CPI near 3.5% and the Fed tightening. Against that,
analyst bullish share is 45.0% and **deteriorating** (-1.2).
- What kills it is the risk arithmetic at today's price, not the story. DG is
  124.58 with **ATR14 4.2695 (3.43%)** — a wide daily range against its own
  range:
  - The 2.0 ATR stock stop floor requires a stop **at or below 116.04**.
  - A stop that wide requires a target **at or above 141.66** to clear the 2.0
    swing reward-to-risk floor.
  - The **120-day high is 134.125**. So the minimum compliant target sits
    **5.62% above the highest price DG has traded in 120 sessions.**
- The only ways to make it pass are to tighten the stop inside 2.0 ATR or to
  pick an above-range target, and config/strategy.md forbids both by name —
  "if an idea needs a tight stop to clear the reward-to-risk floor, it has
  failed the floor," and do not reverse-engineer levels.
- So: **cancel the 134.50 order and do not replace it.** DG belongs on the
  watchlist, not in the report. It becomes interesting again nearer the 120-day
  low of 99.57, or after the ATR compresses.
- 124.58 currently sits between the 50-day (123.47) and 20-day (125.16) SMAs.

## [06:43 ET] CORRELATION CHECK — run explicitly, because this report leans one way
config/strategy.md caps ideas sharing a driver at 3. Counting only ideas that
**create or keep** exposure, since an exit removes risk rather than adding it:
- Rate-path driver: **SPY short, XLI short, MET long = 3.** At the cap, not over
  it — and MET is the **opposite sign** to the two shorts, so the three together
  are less directional than the count suggests, not more.
- Idiosyncratic, uncorrelated to the rate path: **CCJ** (uranium contracting),
  **SVRA** (single-asset biotech).
- The five exits (LCII, BCC, GLD, NKE, LULU) create no exposure.
- Energy was held at its existing 3 pending ideas and deliberately not extended
  — see the 06:20 note.

## [06:44 ET] CCJ — one more piece of evidence, and it cuts against the position
Checking the stale pending orders turned up something relevant to CCJ that I did
not have when I captured it: the **power-demand complex is working, and CCJ is
not participating in it.**
- `VST` last 148.38 vs its 128.00 pending entry — **+15.92%**, ran away.
- `CEG` last 284.75 vs its 272.00 pending entry — **+4.69%**, ran away.
- `CCJ` meanwhile is **-29.42% vs XLE over 6 months** and -2.31% absolute on 3m.
- So the datacenter-power thesis that underpins owning uranium is visibly being
  bought in the generators and is not reaching the fuel supplier. That is a
  stronger version of the concern already in the CCJ candidate, and it makes the
  dated invalidation (underperformance at the 2026-11-03 print) the operative
  test rather than a formality. **I did not raise CCJ's conviction; if anything
  this argues the position is the laggard in a working theme.**

## [06:45 ET] VENUE CHECK — all 10 candidates are Robinhood-tradeable
Final list is entirely US exchange-listed common stock and ETFs on
`Robinhood Stocks`: SPY, XLI, GLD (NYSE Arca ETFs); MET, CCJ, BCC, LCII (NYSE);
NKE, LULU, SVRA, DG-rejected (NASDAQ/NYSE). Market caps verified where it
matters — SVRA $1.09B (NASDAQ NMS), MET $61.7B, CCJ $42.1B, BCC $2.63B, all far
above the $50M floor, and every name clears the $500K average dollar volume
floor by three orders of magnitude or more.
- Two candidates require margin and are marked `requires_margin: true`: the SPY
  and XLI shorts.
- **No futures, crypto or event contracts reached the final list**, so no
  contract-month or Robinhood-listing verification was needed. Each of those
  lanes was hunted and rejected with a stated reason above.

## [06:46 ET] RESEARCH COMPLETE
- candidates: **10 distinct ideas** (17 lines in candidates.jsonl; synthesis
  takes the last entry per symbol — 6 lines are conviction corrections and 1 is
  an SVRA re-capture adding market cap).
  - New: **MET** buy (conviction 4), **XLI** short (4)
  - Updates/holds: **SPY** short hold (4), **CCJ** hold (3), **SVRA** hold (2)
  - Exits: **GLD** (5), **NKE** (5), **LCII** (4), **BCC** (4), **LULU** (4)
- **Highest-value single finding: LCII.** It has been under an all-stock merger
  since 2026-06-30 at 1.2440 PATK shares, so its 138 target requires PATK at
  110.93 (+51%). The position should never have been opened at 94.00 seven weeks
  after the deal was announced. Close it.
- **Most urgent action: cancel the `KXFEDDECISION-26SEP-H0` YES order at 47c.**
  That contract is 20/21c and resolves Wednesday.
- coverage gaps, stated rather than glossed:
  - **No index, VIX or dollar level anywhere in this report.** Yahoo returned
    HTTP 429 on every index symbol (^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, ES, NQ, DXY,
    ^TNX, gold, WTI) across all four fallback sources. Equity single names came
    from finnhub and nasdaq and were unaffected.
  - `sma200` is null throughout — the 120-day window cannot compute it. Not a
    source failure.
  - Crude oil: no price fetched, so no oil-based idea was attempted.
  - Did not re-underwrite PFE, CEG, EEM, DINO, VST or IYR beyond checking their
    pending levels against the market.
  - Crypto direction left unresolved on purpose (06:24 note).
- sources that failed: **yahoo (429, all index symbols)**; alphavantage (no API
  key); stooq (404 on index tickers); finnhub indices (CFD subscription
  required); `market_data.py short NKE` (nasdaq read timeout).
- **code bug found, not a dead source**: `market_data.py events` returns null
  prices for every Kalshi market — the Kalshi API now uses `yes_bid_dollars` /
  `yes_ask_dollars` / `last_price_dollars` / `volume_24h_fp` / `open_interest_fp`
  and `events()` at scripts/market_data.py:752 still reads the old names. It
  also samples only 200 open markets and filters client-side, so "Fed" and "CPI"
  both return count 0. Every event price in these notes came from a direct
  series/market fetch instead. Worth a fix before the next run.

## [06:50 ET] CORRECTION — `--peer` does not change `vs_benchmark_pct`. Two candidates re-captured.
Caught while checking XLV. `relative_strength()` (scripts/market_data.py:1095)
always computes **`vs_benchmark_pct` against `--benchmark`, which defaults to
SPY**, and puts the peer comparison in a **separate `vs_peer_pct` field**. My
extraction printed only `vs_benchmark_pct`, so any figure I labelled "vs
<sector ETF>" taken from that field was really vs SPY.
- **MET** — captured as "vs XLF +1.56/+7.32/+26.46". Those are **vs SPY**.
  True vs XLF: **+1.66 / +2.12 / +23.97**. Re-captured with both stated
  separately. The idea survives — MET leads SPY *and* XLF on all three windows —
  but the 3-month sector edge is **+2.12, not +7.32**, which is a materially
  weaker claim and is now written into `key_risk` rather than buried.
- **NKE** — captured as "-8.10/-23.53 vs XLY". Those are **vs SPY**. True vs
  XLY: **-4.98 / -17.06 / -33.31**. Re-captured. Conclusion unchanged and in fact
  better evidenced: NKE underperforms both SPY and its own sector on every
  window, so the weakness is company-specific rather than sector drift.
- **CCJ was NOT affected** — I derived -9.10/-16.35/-29.42 by hand from the raw
  `returns_pct` table rather than from the benchmark field, and re-running with
  `vs_peer_pct` confirms those three numbers exactly.
- **GLD and XLI were NOT affected** — both were run with `--peer SPY` against the
  default SPY benchmark, so the "vs SPY" labels were already correct, as was the
  whole sector sweep table at 06:31.
- Logged rather than quietly amended. CLAUDE.md's rule is that every number
  traces to a source and that a figure the model wrote about its own idea is not
  to be trusted — this is exactly that failure, caught by re-deriving it.

## [06:52 ET] REJECTED — XLV long — the relative case is real, the outright long is not
- Went looking for something **uncorrelated to the rate path** to diversify a
  report that leans one way, and healthcare was the candidate: defensive, rate-
  insensitive, and the natural other side of the XLI short in a late-cycle
  rotation. The pair case checks out — **XLV vs XLI is +5.44 / +8.90 / +5.81**
  (1m/3m/6m), computed from the raw returns rather than the benchmark field.
- But an outright long fails on its own chart. XLV is **165.36, below both its
  20-day SMA (170.89) and its 50-day (166.24)**, having fallen from 171.45 on
  2026-09-04 — a -3.6% week — and it is -0.77 vs SPY over 1m. That is buying
  something in a downtrend, below two declining averages, inside a tape I am
  otherwise positioned short in.
- "Better than XLI" is not a reason to be long XLV; it is a reason to be short
  XLI, which I already am. I cannot express the pair cleanly in this format, so
  the honest output is one leg and a rejection, not two legs dressed as
  conviction. **The report keeps its one-sided skew rather than importing a weak
  long to balance the optics** — config/strategy.md is explicit that a balanced
  report assembled by forcing a mix is worse than an honest lopsided one.

## [06:54 ET] RESEARCH COMPLETE (supersedes the 06:46 block)
This block replaces the earlier RESEARCH COMPLETE at 06:46, which was written
before the benchmark-labelling correction and the XLV work. Counts and findings
below are the final ones.

- candidates: **10 distinct ideas**, 19 lines in candidates.jsonl. Synthesis
  takes the last entry per symbol. The extra lines are 6 conviction corrections,
  1 SVRA re-capture adding market cap, and 2 re-captures (MET, NKE) fixing
  mislabelled benchmarks. **Every one of the 10 now has conviction exactly equal
  to its distinct-evidence-kind count**, verified programmatically.

| Idea | Dir | Horizon | Conv | Note |
| --- | --- | --- | --- | --- |
| GLD | sell | swing | 5 | exit, amends the 406.77 order to market |
| NKE | sell | swing | 5 | exit |
| BCC | sell | swing | 4 | exit |
| LCII | sell | swing | 4 | exit — the day's key finding |
| LULU | sell | swing | 4 | exit |
| **MET** | **buy** | swing | 4 | **new** — the only long initiated |
| SPY | sell_short | swing | 4 | hold, unchanged levels |
| **XLI** | **sell_short** | swing | 4 | **new** — waits for a bounce |
| CCJ | buy | long_term | 3 | hold, dated invalidation added |
| SVRA | buy | swing | 2 | hold, unchanged levels |

- **Key finding: LCII.** Under an all-stock merger with Patrick Industries since
  2026-06-30 at 1.2440 PATK/share. At PATK 73.40 the deal is worth 91.31 against
  a 91.02 close — a 0.32% spread. The standing 138 target requires PATK at
  110.93 (+51%) and is arithmetically unreachable. Close it.
- **Most urgent action: cancel the `KXFEDDECISION-26SEP-H0` YES order at 47c.**
  The contract is 20/21c and resolves Wednesday.
- **Second action: cancel `DG` BUY @ 134.50** — re-underwrote it and it no
  longer clears the floors at any compliant stop (working shown at 06:41).
- coverage gaps:
  - **No index, VIX or dollar level in this report at all** — Yahoo returned HTTP
    429 on every index symbol across all four fallbacks. Single-name equity data
    (finnhub, nasdaq) was unaffected.
  - `sma200` null throughout; the 120-day window cannot compute it.
  - No crude oil price fetched, so no oil idea was attempted.
  - PFE, CEG, EEM, DINO, VST, IYR checked only for level staleness, not
    re-underwritten.
  - Crypto direction deliberately unresolved — the crypto-up/gold-down
    divergence could not be reconciled from fetched data (06:24).
- sources that failed: yahoo (429, all indices); stooq (404 on index tickers);
  finnhub indices (CFD subscription required); alphavantage (no key);
  `market_data.py short NKE` (nasdaq read timeout, so no short-interest data
  anywhere in this report).
- **two code bugs found, both worth fixing before the next run:**
  1. `events()` at scripts/market_data.py:752 returns null prices for every
     Kalshi market — the API now uses `*_dollars` / `*_fp` field names. It also
     samples only 200 open markets and filters client-side, so "Fed" and "CPI"
     return count 0. All event prices here came from direct series fetches.
  2. `relative_strength()` at scripts/market_data.py:1095 — `--peer` populates
     `vs_peer_pct`, while `vs_benchmark_pct` stays vs SPY. Not a bug in the code
     so much as a trap in the output shape; it cost me two mislabelled
     candidates, caught and corrected at 06:50.
