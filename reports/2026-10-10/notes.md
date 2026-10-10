# Research log — 2026-10-10

## [06:02 ET] SETUP — weekend run, Saturday 2026-10-10
- US equities and futures closed (CME equity index reopens Sun 18:00 ET). Crypto 24/7.
- Per config/strategy.md weekend behavior: lean crypto + event contracts for actionable;
  equities = week-ahead prep, `swing`, entry for next open (Mon 2026-10-12).
- Prior context digested: 15 open positions, 15 awaiting entry, 15 closed (2/15 target, avg -4.2%).
- Track record read: **stock 0/8 hit target, avg -6.5% (n=28)** vs etf 2/7 (29%), avg -1.5%.
  n=15 closed is right at the noise threshold the skill names, so NOT over-fitting — but the
  direction is consistent enough to raise the bar on single-name long equity today, especially
  conviction-2 single names (0/4, avg -8.3%).
- Repetition guard: XLU 5x, DAL 3x, CCJ 3x in last 10 days. XLU already stopped out 2026-10-06.
  Will not re-pitch XLU. CCJ/DAL only if something concrete changed.

## [06:04 ET] CRYPTO SPOT — live, coingecko (24/7 market, these are real-time)
- BTC 82,804 (+0.24% 24h), mcap 1.664T, 24h vol 22.4B
- ETH 2,494.45 (-0.26%), SOL 109.80 (-0.53%), XRP 1.41 (+0.42%)
- DOGE 0.086005 (+1.16%), ADA 0.25533 (**+6.97%** — the only big mover), AVAX 10.52 (+1.09%)
- LINK 12.95 (+0.42%), LTC 63.50 (-1.20%)
- source: scripts/market_data.py crypto (CoinGecko)
- Read: tape is flat/quiet across majors on the weekend. ADA +7% is the outlier worth a look.

## [06:10 ET] DATA GAP — event contracts have NO fetchable prices today
- `market_data.py events "<any>"` returns `ok: true, count: 0` for Fed, CPI, inflation,
  bitcoin, recession, unemployment, GDP. Cause found: the helper pulls only the first 200
  open Kalshi markets and filters client-side; all 200 returned were one series
  (KXMVECROSSCATEGORY — movie markets), so nothing can ever match. Tool limitation, not an
  empty market.
- Worked around it by querying Kalshi `series_ticker` directly. Series resolve fine, BUT
  **every price field comes back null** — `yes_bid`, `yes_ask`, `last_price`, `volume`,
  `open_interest` are all None, both on the /markets list and on individual /markets/<ticker>
  lookups (status reads `active`). Checked KXFEDDECISION-26OCT-C25/-H0, KXCPIYOY-26SEP-T3.5,
  KXBTCMAXY-26DEC31-99999.99, KXRECSSNBER-26.
- **Consequence: no event-contract candidate can be published today.** config/universe.md
  requires an explicit probability disagreement stated against the market's implied
  probability, and that number cannot be fetched. Will not estimate one — a made-up implied
  probability is exactly the fabricated number the non-negotiables forbid. Two event ideas
  already sit in "awaiting entry" (KXFEDDECISION-26OCT-H25 @28, KXCPIYOY-26SEP-T3.5 @18) and
  I cannot re-mark either without a live quote.

## [06:11 ET] CALENDAR — dated events, derived from fetched Kalshi market close times
- **Sep CPI: Tue 2026-10-14 08:30 ET** (KXCPIYOY-26SEP-* closes 2026-10-14T12:29Z)
  — source: https://api.elections.kalshi.com/trade-api/v2/markets/KXCPIYOY-26SEP-T3.5
- **FOMC decision: Wed 2026-10-28 14:00 ET** (KXFEDDECISION-26OCT-* closes 2026-10-28T17:59Z)
  — source: https://api.elections.kalshi.com/trade-api/v2/markets/KXFEDDECISION-26OCT-C25
- Oct jobs report: 2026-11-06 (KXU3-26OCT closes 2026-11-06T13:29Z). No KXU3-26SEP open, so
  the September employment report is already released.
- So: CPI lands inside a swing horizon (2 sessions out), FOMC is 12 sessions out.

## [06:08 ET] EARNINGS CALENDAR — next 5 sessions (fetched, finnhub via market_data.py earnings --days 14; 557 rows)
This is **Q3 bank earnings week**, and it is the dominant dated catalyst in the horizon:
- **Mon 2026-10-12**: nothing of size (16 micro/nano names, no eps estimates). US market open.
- **Tue 2026-10-13 bmo**: `JPM` (eps est 5.9185), `GS` (15.0539), `C` (2.7311), `WFC` (1.8754),
  `UNH` (4.1893), `JNJ` (2.5881), `DPZ` (4.4127); `AZZ` amc
- **Wed 2026-10-14 bmo**: `BAC` (1.1619), `MS` (3.1669), `BLK` (14.3954), `STT` (3.6838),
  `FAST` (0.3443), `CBSH` — **plus Sep CPI 08:30 ET**
- **Thu 2026-10-15**: `PNC` (4.9782), `USB` (1.3347), `SCHW` (1.7013), `BNY` (2.2764),
  `FHN` (0.5293), `MRSH`, `PLD`, `CMC`, `MAN`, `WHR`, `AA` amc, `IBKR` amc, `JBHT` amc
- **Fri 2026-10-16 bmo**: `TFC` (1.1263), `CFG` (1.4016), `RF` (0.6808), `MTB` (5.0006),
  `TRV` (6.8423), `EEFT`
- Also in window: `XOM`, `SLB`, `AXP` (10-23), `AAL`, `CMCSA`, `BX`, `DECK`, `DOV`, `CBRE` (10-22)
- Read: the single most concentrated catalyst cluster available is financials, 1-4 sessions out.
  `XLF` BUY @ 54.23 is already in awaiting-entry from 2026-10-09 — that is the clean expression
  and re-pitching it amends rather than duplicates. Correlation cap means I must NOT also add
  three single-name banks on top of it.

## [06:10 ET] MACRO / REGIME — Friday 2026-10-09 closes (fetched; equities shut, so these are
## previous-close prices in a CLOSED session, not stale quotes)
source: scripts/market_data.py quote + history --days 120

| Instrument | Close | vs 120d high | sma20 | sma50 | ATR14 |
| --- | --- | --- | --- | --- | --- |
| SPY | 778.57 | **-0.39%** (hi 781.62) | 767.98 | 767.57 | 6.26 (0.80%) |
| QQQ | 751.27 | — | — | — | — |
| IWM | 278.94 | **-8.60%** (hi 305.18) | 282.06 | 291.38 | 3.74 (1.34%) |
| SMH | 603.33 | -10.20% | 597.06 | 578.24 | 13.52 (2.24%) |
| XLF | 54.73 | -6.60% | 54.77 | 56.53 | 0.70 (1.27%) |
| XLE | 65.08 | -1.65% | 63.30 | 62.67 | 1.24 (1.91%) |
| TLT | 77.98 | -11.17% (120d low 76.43) | 79.28 | 81.08 | 0.87 (1.11%) |
| GLD | 384.58 | **-12.64%** (hi 440.25) | 388.01 | 397.03 | 5.96 (1.55%) |
| SLV | 54.78 | **-32.25%** (hi 80.86, lo 49.61) | 56.60 | 57.94 | 1.53 (2.80%) |

Friday moves: SPY +0.60%, XLF +0.92%, GLD +1.57%, SLV +2.49%, XLV +1.58%, XLU +0.83%,
XLP +0.01%, SMH **-0.65%**, TLT +0.14%, UUP +0.14%, HYG +0.12%.
(caveat: the quote helper returned an identical change_pct of 0.4936% for both QQQ and IWM,
which is almost certainly an artifact — I am not relying on those two change figures, only on
their price levels, which reconcile with the history series.)

**The regime read, and it is the most useful thing on this page:**
1. **SPY is at the top of its 120-day range (-0.39% off high) and breadth underneath it is
   bad.** IWM is -8.6% off its high and below BOTH its 20dma (282.06) and 50dma (291.38);
   SMH is -10.2% off its high and fell on a day SPY rose. A tape where the index makes highs
   while small caps sit under a falling 50dma is narrow, not strong.
2. **Long rates are at the hard end.** TLT 77.98 against a 120d low of 76.43 — i.e. 2% from
   the low, below its 20- and 50-day. That is the engine under the small-cap and
   rate-sensitive weakness and it is why `ITB`/`IYR` shorts were pitched earlier.
3. **Precious metals are in a genuine correction, not a dip.** GLD -12.6% off 440.25; SLV
   -32.3% off 80.86 having bottomed at 49.61. Both are below their 20- and 50-day, and both
   rallied hard Friday (+1.57%, +2.49%). A 32% drawdown in silver after a vertical move is a
   broken momentum trade mid-repair, not a buy-the-dip. Watchlist, not a position.
4. HYG +0.12% and essentially flat — credit is not confirming any stress, which argues against
   pressing an index short here.

**Implication for today's hunting:** the cleanest non-consensus observation is the
SPY-at-highs / IWM-under-50dma divergence, and the correlation cap means I should express the
rate-and-breadth view ONCE, not four times. `ITB`, `IYR`, `TLT` shorts already sit in
awaiting-entry on exactly this driver.

## [06:13 ET] LEADERSHIP SCAN — sector/theme ETFs, Friday closes, history --days 120
Ranked by position vs its own 20- and 50-day:

**Leading (above sma20 AND sma50):**
- `XLK` 198.78, -2.2% off high, sma20 194.52 / sma50 189.05 — tech is the leadership
- `XLE` 65.08, -1.65%, sma20 63.30 / sma50 62.67
- `XOP` 191.52, -4.66%, sma20 186.96 / sma50 184.98 — E&P producers
- `SPY` 778.57, -0.39%

**Lagging (below both, deep off highs):**
- `URA` 38.90, **-34.03%** off 58.97, sma20 40.95 / sma50 43.31, 120d low 37.18 — uranium capitulated
- `ITB` 84.76, -20.32%, sma20 87.75 / sma50 92.82, 120d low 83.69 — homebuilders breaking
- `OIH` 388.65, -15.38%, sma20 392.15 / sma50 404.76 — oil *services* lag badly
- `COPX` 85.75, -12.13% | `KRE` 69.01, -11.92% | `IYR` 96.10, -11.16% | `XLI` 169.25, -10.06%
- `XLB` 49.43, -8.78% | `XLY` 112.85, -7.64% | `XLC` 110.38, -7.34% | `EEM` 66.80, -6.66%
- `XLF` 54.73, -6.60%

Relative strength, measured (market_data.py relstrength ... --peer SPY):
- `XLF` vs SPY: 1m **-6.50%**, 3m -6.31%, 6m -6.79% — "lagging SPY on every window measured"
- `IWM` vs SPY: 1m -5.78%, 3m **-8.87%**, 6m -7.84% — same verdict

## [06:13 ET] REJECTED — XLF BUY @ 54.23 (awaiting entry since 2026-10-09) — NOT re-pitched
Bank earnings Oct 13-16 is a genuinely strong dated catalyst and the level is unchanged, so the
tempting move was to re-pitch it. I am not, and the reason is measured rather than a feeling:
XLF has underperformed SPY by 6.3-6.8% on *every* window (1m/3m/6m), sits below its 50dma
(56.53) at 54.73, and `KRE` is -11.9% off its high under both MAs. A limit at 54.23 is 0.9%
*below* Friday's close, so it only fills if financials keep losing to the index — the precise
"pullback entry that only fills once the trade goes against you" failure mode flagged in
config/strategy.md, and the first month ran 31 pullback entries at a 42% fill rate for exactly
this reason. The existing awaiting-entry row already carries the view; adding conviction to it
today would be anchoring, not information. Leaving it to fill or expire on its own.

## [06:14 ET] SOURCE FAILED — `market_data.py macro`
Hung twice and never returned: first attempt killed at 180s, second at 400s (exit 124). No
rates/VIX/DXY/FRED series this run. Substituted ETF proxies I could actually fetch — `TLT`
77.98 for the long end, `UUP` 29.02 for the dollar, `HYG` 77.23 for credit, `GLD`/`SLV` for
metals — which is why the regime block above is built from `quote` + `history` rather than
from `macro`. No VIX reading at all today; do not let synthesis imply one.

## [06:20 ET] NEWS — the bank complex is in correction while SPY makes highs (the day's key finding)
- KBWB (KBW Bank ETF) **-12% from its mid-August high** as large-cap banks enter correction
  ahead of Q3 earnings, while the broad market prints fresh highs.
  source: https://www.cnbc.com/2026/10/09/bank-stocks-selloff-q3-earnings.html
- 1-month moves cited: JPM -7%, GS -15%, BAC -16%, MS -13.7%, WFC -9% vs S&P 500 +4%.
- **Two drivers, and they are different in kind:**
  1. Rates/macro — higher Treasury yields, inflation, and the market entertaining *additional
     Fed hikes*. That squares with my own fetched data: TLT 77.98 within 2% of its 120d low,
     and the precious-metals crash (hawkish hold → dollar up, yields ~4.2%).
  2. **The OpenAI IPO was delayed**, which defers equity-capital-markets fees into 2027. This
     is the specific reason GS and MS led the decline, and it is a *deferral*, not an
     impairment — a distinction that matters for mean reversion.
     source: https://www.moomoo.com/news/post/72122611/goldman-sachs-and-morgan-stanley-led-the-decline-in-bank
- Counterview on the record: one strategist holds that bank fundamentals remain strong and the
  US is not near recession. No specific credit event is tied to the October drop; the private
  credit stress in the search results (Blue Owl gating a retail fund, MS redemption requests)
  is from earlier in 2026, not this week. Flagging that explicitly so synthesis does not
  present old stress as new.

## [06:20 ET] LEVELS — every bank reporting next week is below BOTH its 20- and 50-day
| Sym | Close | off 120d high | sma20 | sma50 | 120d low | ATR14 |
| --- | --- | --- | --- | --- | --- | --- |
| GS | 895.32 | **-22.42%** | 924.42 | 989.93 | 868.52 | 19.65 |
| MS | 190.02 | -18.18% | 195.99 | 207.33 | 182.47 | 4.18 |
| BAC | 54.32 | -16.72% | 55.88 | 60.07 | 49.30 | 1.02 |
| C | 129.64 | -12.38% | 131.24 | 133.63 | 119.76 | 2.82 |
| WFC | 83.55 | -9.17% | 83.30 | 85.75 | 72.775 | 1.86 |
| JPM | 332.99 | -9.14% | 339.37 | 350.14 | 293.67 | 5.73 |
| UNH | 379.30 | -17.83% | 374.92 | 389.18 | 345.23 | 8.86 |
| JNJ | 261.44 | -6.98% | 264.69 | 265.33 | 220.37 | 5.18 |
Friday was a broad bounce: WFC +1.85%, MS +1.38%, GS +1.44%, BAC +1.32%, C +1.22%, JPM +0.47%.

## [06:21 ET] CAPTURED — GS BUY swing, conviction 3, 1st candidate
entry 906.50 stop_limit (post-print reclaim of the 10-06 high 905.94), stop 857.00,
target 1010 / 1060. R:R 2.09, stop 2.52 ATR, target 5.27 ATR — all inside the floors.
`catalyst.wait: true` — the correct action today is NOT to enter. Picked GS over the others
because its drawdown has a specific *reversible* cause (ECM deferral) rather than a general
rate complaint, and because it is basing: 120d low 868.52 on 10-07, then higher lows 876.77
and 878.86, Friday closing 895.32 of a 899.67 high.
**Only ONE bank idea published, deliberately** — config/strategy.md caps 3 ideas per driver and
`XLF` BUY already sits in awaiting-entry on this exact driver. GS/MS/BAC all clear the floors
arithmetically; publishing three of them would be one bet with extra steps.

## [06:21 ET] REJECTED — WFC BUY — failed the reward-to-risk floor honestly, and is the
## clearest example today of the rule working
WFC was the one I *wanted*: the only bank above its 20-day (83.55 vs 83.30), a domestic lender
whose NII benefits from higher-for-longer, and the name least exposed to the OpenAI/IPO-delay
driver that hit GS and MS. Structure is genuinely good — fell to 78.00 on 10-01, higher low at
79.07 on 10-07, then 82.03 and 83.55 closing near Friday's 84.055 high.
But the arithmetic refuses it. A breakout entry at 84.20 with the stop under the 79.07 higher
low (78.90) risks 5.30 = 2.84 ATR, and the upside to the 120d high of 91.99 is only 7.80 —
**R:R 1.47**. The only ways to reach 2.0 were a stop inside 2.0 ATR or a target above the prior
high, i.e. the two forms of reverse-engineering config/strategy.md names explicitly. Dropped
rather than tuned. WFC's ATR of 1.86 is simply too large relative to its distance to
resistance for a swing to work here.

## [06:21 ET] REJECTED — MS, BAC — clear the floors, cut on the correlation cap, not on merit
MS (entry ~190.02, stop ~179.56 = 2.5 ATR, target 212) returns 2.10, and BAC (entry 54.32,
stop 51.78, target 60.07 = its 50-day) returns 2.26 with the target only 5.66 ATR away — BAC is
arguably the tidiest of the three. Both are the same trade as GS. Recording the levels here so
the work is not lost if a reader prefers BAC's cleaner target.

## [06:24 ET] NEWS + LEVELS — steel is in a measurable upgrade cycle
- Friday: `CLF` **+6.48%** to 12.98, `STLD` +1.80% to 238.38, `NUE` +1.70% to 250.33,
  `XME` +1.66%, `PICK` +2.33%, `FCX` +3.58%. `AA` was the exception at **-1.47%**.
- Catalysts are analyst actions, not a steel-price event: Wells Fargo upgraded CLF to
  Overweight from Equal Weight ($14 target) **citing steel pricing power**; GLJ Research raised
  CLF to $17.48 (Buy); JPMorgan raised CLF $11 → $13 (still Neutral). CLF had already jumped
  ~10% to $12.44 on 10-05 as "Stelco fallout faded".
  source: https://247wallst.com/investing/2026/10/05/cleveland-cliffs-jumps-10-as-stelco-fallout-fades-before-october-19-earnings-nucor-and-steel-dynamics-rise-5/
- Realised pricing confirms: CLF average selling price **$1,124/net ton in Q2 vs $1,048 in Q1**.
- Measured revision data (market_data.py analysts):
  - `CLF` bullish share 30.0%, **+21.3pp** — sell ratings collapsed 7 → 1 since June. The single
    strongest revision swing I measured today.
  - `STLD` bullish share 63.6%, +1.7pp, sells 2 → 1. Modest but same direction.
- Earnings (fetched): `STLD` 2026-10-19 amc (est 5.4904), `CLF` 2026-10-19 (finnhub says amc;
  a secondary source says bmo — **conflict, do not state an hour as settled**).

## [06:24 ET] CAPTURED — STLD BUY swing, conviction 4, 2nd candidate
entry 245.50 stop_limit (through the 10-05 high 245.185, which also clears the 241.36 50-day),
stop 228.75, target 281 / 288. R:R 2.12, stop **2.50 ATR** (at the comfortable level, not the
floor), target 5.30 ATR. Chose STLD over CLF on earnings quality: STLD earns 3.81/sh and beat
3 of 4, CLF has lost money four quarters running (-0.25, -0.42, -0.44, -0.51) and missed 3 of 4.

## [06:24 ET] WATCHLIST — CLF — best positioning signal of the day, worst arithmetic
Keeping the levels on the record because the revision swing (+21.3pp, sells 7→1) is real and
better than STLD's. Why it is not a published recommendation:
- Entry 13.10 would be chasing **+15% in a week** (≈11.3 → 12.98) two sessions after a +6.5%
  day, into a 10-19 print.
- The arithmetic is marginal in the way config/strategy.md names: the only version that reaches
  2.0 is entry 13.10 / stop 11.76 / target 15.80 — R:R 2.01 with the stop at **2.02 ATR**, i.e.
  sitting on the floor, and a target 5% *above* the 15.06 120-day high. A 2.5 ATR stop drops it
  to 1.14. That is an idea that only passes by being tuned, so it fails.
- Loss-making: EPS -0.25, -0.42, -0.44, -0.51 over four quarters, 3 misses in 4.
Would become interesting on a pullback into the 12.00-11.96 20/50-day cluster, which would let
a 2.5 ATR stop sit under the base with the 15.06 high still in front of it.

## [06:24 ET] REJECTED — NUE — fails R:R at every honest construction
250.33, sma50 255.23, ATR 6.71, 120d high 280.11. A 50-day-reclaim entry at 256 with a 2.5 ATR
stop (239.25) needs 289.50 to reach 2.0 — above the 120-day high. Against a 280 target it
returns 1.43. Same sector thesis as STLD, no setup. Nothing to tune; dropped.

## [06:24 ET] FLAG — AA (Alcoa) is the loudest dislocation I found and I am NOT publishing it
42.20, **-49.99% off its 120-day high of 84.38**, sitting on its 120-day low of 41.01, below
sma20 43.72 and sma50 47.45, with earnings 2026-10-15 amc (est 1.495). It also *fell 1.47% on a
day the entire rest of the metals complex rallied* — which is the reason for restraint rather
than enthusiasm. A name that halves and then declines while its peers rip has something
specific wrong with it that I have not identified, and I ran out of budget to find out. An
un-diagnosed 50% drawdown two sessions from an earnings print is not a trade, it is a question.
Recorded as the first thing to check tomorrow.

## [06:24 ET] SOURCE FAILED — `market_data.py implied`
`implied STLD --entry 242 --target 278` returned HTTP 401 Unauthorized from yahoo-options. So
**no options-implied move was available for any idea today** — the "is my target inside what
the market prices" check in config/strategy.md could not be run at all this run. Noted so
synthesis reports the gap rather than implying the check passed.

## [06:26 ET] POSITION REVIEW — all 15 open positions, decided one by one
Prices are Friday 2026-10-09 closes; ATR/MA figures from `history --days 120`. Stored horizons
read from `state/open_positions.json`, which matters — CCJ, NKE(buy), LCII, PFE and LULU(buy)
are all tracked as **long_term**, so they carry no ATR stop floor and are judged against a
bear-case price rather than a stop.

### A structural finding worth stating before the individual calls
**Two of the 15 "positions" are boxed pairs, so real directional exposure is 11, not 15.**
`state/open_positions.json` holds LULU `buy` @115 (long_term, no stop) *and* LULU `sell` @100.61
(swing, stop 112, target 77) simultaneously, and the identical shape in NKE: `buy` @40.75
(long_term, no stop) and `sell` @38.40 (swing, stop 41, target 32.10). Each pair is long and
short the same name at the same time. That is not a hedge anybody chose — it is two theses
written five weeks apart, neither closed, and the net effect is to pay the spread while making
both legs untestable. In both pairs the **short is the leg that is working** (+6.1% LULU,
+9.6% NKE) and the long is the leg with no stop and no invalidation.

**Decision on both: close the long leg, keep the short.** The trend is unambiguous and measured
— LULU 94.50 is below its 20-day (97.61) and 50-day (109.43) and 44.48% off its high; NKE 34.71
is below its 20-day (35.50) and 50-day (38.15) and 27.15% off its high, with its 120-day low at
31.97. The long legs are fighting that; the shorts are riding it.

**I deliberately did NOT capture these two closes as candidates, and synthesis must handle them
in prose instead.** The reason is mechanical and would have caused real damage: the existing
*short* positions are stored as `direction: "sell"` — not `sell_short` — so a `sell` candidate
on LULU or NKE would be merged by `merge_report` into the live short as an amendment and would
overwrite that short's stop and target. There is no direction value that expresses "exit a
long" without colliding with the short already on the book. Closing the long legs is therefore
a written instruction, not a row.

### Hold as-is — working, nothing changed, no candidate emitted
- **`PFE`** long_term, entry 27.60, last 28.28 (+2.5%). The quiet success of the value book and
  the only one of it in a technical uptrend: above its 20-day (27.99) *and* 50-day (27.62), just
  3.18% off its 120-day high. Target 42 is distant but the thesis is not under pressure. HOLD.
- **`DINO`** swing, entry 107.50, last 121.30 (**+12.8%**), target 128, stop 97.75. Best position
  on the book: 2.35% off its 120-day high, far above its 20-day (111.65) and 50-day (102.10).
  HOLD and trim into 128. I did *not* publish a tightened stop — see the note below on why.
- **`CEG`** swing, entry 272.00, last 298.07 (+9.6%), target 320, stop 250. Above both MAs
  (268.10 / 273.98). +4.56% on Friday. HOLD.
- **`SNX`** swing, entry 260.00, last 273.37 (+5.1%), target 296.47, stop 242.50. Above both MAs
  (268.89 / 261.34). HOLD.
- **`XLE`** swing etf, entry 63.90, last 65.08 (+1.8%), target 70.50, stop 60.80. Energy is one
  of only two leading sectors; 1.65% off its high, above both MAs. HOLD.
- **`EEM`** swing etf, entry 65.60, last 66.80 (+1.8%), target 71.50, stop 63.00. Sitting right on
  its 20-day (67.27) and 50-day (66.87) — directionless but unbroken. HOLD.
- **`LULU` sell** swing, entry 100.61, last 94.50 (+6.1%), target 77, stop 112. HOLD. Note 94.50
  is only 4.6% above the 120-day low of 90.38, so the easy part of this short is behind it.
- **`NKE` sell** swing, entry 38.40, last 34.71 (+9.6%), target 32.10, stop 41.00. HOLD, and take
  the target: 32.10 sits just *above* the 120-day low of 31.97, so the objective is essentially
  the low. Do not get greedy past it.

### Why no tightened stops were published on the winners — a mechanical trap, not laziness
The obvious management step on DINO (+12.8%) and CEG (+9.6%) is to raise the stop toward
break-even. **Every such amendment fails validation by construction**, and it took working the
arithmetic to see why: `check_stop_distance` measures the stop from `entry.ideal`, and
CLAUDE.md forbids changing the entry of a filled position. So on DINO a stop raised to 105 is
0.56 ATR from the 107.50 entry and fails the 2.0 floor outright; on CEG the *existing* 250 stop
is already only 1.51 ATR from the 272 entry because ATR has expanded to 14.52, so CEG would
fail today even unchanged. Publishing those amendments would have produced two ideas engineered
to be demoted to the watchlist. Trailing stops on winners belong in the management instruction,
and that is where I have put them: **DINO trail under the prior daily low above 112; CEG trail
under 268 (its 20-day).**

### Hold, but on notice
- **`CCJ`** long_term, entry 94.00, last 88.06 (-6.3%), target 135, stop 82.5. HOLD, do not add,
  and **not re-pitched** — it has appeared 3× in the last 10 days and a fourth would be the
  anchoring the repetition guard exists to catch. The split verdict is genuinely interesting:
  the *commodity* leg of the thesis has strengthened (uranium spot broke a 19-year record) while
  the *equity* leg broke down — URA -34.03% off its high, CCJ -32.89%, below its 20-day (89.54)
  and 50-day (94.77), with the 120-day low at 83.15 barely above the 82.5 stop. The reasons are
  identified: utilities are balking at contracting at these prices, flooding in northern
  Saskatchewan disrupted the McArthur River / Key Lake supply route, and Westinghouse earnings
  fell year-over-year — though 2026 production guidance was maintained. Against that, the stock
  carries a very high multiple (one snapshot showed a P/E near 148), there are **zero insider
  open-market buys in six months**, and measured analyst revisions are **deteriorating**
  (bullish share 81.8%, -3.9pp). Target 135 requires +53% from here and is 12.6 ATR away; it is
  not a realistic 15-session objective and synthesis should say so rather than carry it silently.
  source: https://247wallst.com/investing/2026/10/03/uranium-prices-just-broke-a-19-year-record-but-nuclear-stocks-are-collapsing-anyway/
- **`LCII`** long_term, entry 94.00, last 78.30 (-16.7%), target 138, no stop. Making **new
  120-day lows** (low 78.075) and 36.85% off its high — and I went in expecting to close it.
  The fundamentals argued me out of it: TTM EPS from the fetched surprise record is 2.70 + 2.59
  + 0.77 + 2.55 = **8.61**, so at 78.30 this is about **9.1x trailing earnings**, and measured
  analyst revisions are **improving** (+2.3pp to 61.1% bullish) with beats in 3 of the last 4
  quarters. That is a cyclical at a trough multiple, not a broken business. HOLD —
  **but the honest arithmetic is that from the 94.00 I own it at, this no longer clears the
  long-term 2.5 floor against any defensible bear case** (it needs a bear case above 87.6, and
  the stock is already at 78.30). That is the position failing its own bar, and it is why I am
  not re-pitching it as an add. **The invalidation it has never had, supplied now: close it if
  quarterly EPS turns negative, or if two consecutive quarters come in below 1.50.** "The price
  fell" is not an invalidation; a cyclical whose earnings roll over is.
  Liquidity note: $27.0M average daily dollar volume and a 29.02M share count — fine to exit,
  but the thinnest name on the book. (The fetched `market_cap_usd` of $1.90B is stale against
  the 78.30 close; 29.02M shares × 78.30 = **$2.27B**. Flagging the discrepancy, not resolving it.)
- **`BCC`** long_term, entry 76.50, last 73.57 (-3.8%), target 110, no stop. 16.8% off its high,
  below its 20-day (75.54) and 50-day (78.68), and $24.7M daily dollar volume — the thinnest on
  the book alongside LCII. The concern is not the drawdown, it is the **driver overlap**: BCC is
  building products, and the rate complex is the single most hostile thing in today's data —
  TLT within 2% of its 120-day low, ITB -20.32% off its high at its own 120-day low. BCC, LCII
  and the `ITB` short awaiting entry are **three positions on one rate call**, which is the
  correlation cap. HOLD, add nothing rate-sensitive today.
- **`KHC`** long_term, entry 23.00, last 22.27 (-3.2%), target 32, stop 21.20. 20.72% off its
  high, below both MAs (23.38 / 24.54), and the 120-day low of 21.75 sits just 2.6% above the
  21.20 stop. HOLD, but this one resolves itself soon — there is very little room between price,
  low and stop.
- **`DAL`** swing, entry 83.00, last 82.17 (-1.0%), target 94.50, stop 78.10. Sitting on its
  20-day (82.30), below its 50-day (83.65). Opened only 2026-10-05 and already pitched 3× in 10
  days, so it gets no fourth airing on a -1% move. HOLD, nothing changed.

## [06:31 ET] CRYPTO — the weekend lane, worked properly and rejected on arithmetic
Daily OHLC and true ATR14 fetched from Kraken (`api.kraken.com/0/public/OHLC`, interval 1440)
because `market_data.py` has no crypto history subcommand and CoinGecko's free `ohlc` endpoint
returns **4-day bars** at days=90 — I computed an "ATR" off those first and discarded it, since
a 4-day range is not a daily ATR and would have understated every stop. Spot cross-checked
against `market_data.py crypto`.

| Coin | Last | ATR14 (daily) | sma20 | sma50 | sma100 | 120d high | off high |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 82,721 | 2,003 (2.42%) | 84,370 | 80,805 | 72,690 | 87,229 | -5.2% |
| ETH | 2,491.31 | 76.70 (3.08%) | 2,661.97 | 2,553.58 | 2,223.57 | 2,806.69 | -11.2% |
| SOL | 109.42 | 4.5143 (4.13%) | 117.74 | 108.53 | 92.71 | 124.91 | -12.4% |
| ADA | 0.2546 | 0.0172 (**6.77%**) | 0.2504 | 0.2269 | 0.2021 | 0.2825 | -9.9% |

This week's move is real and uniform: all four peaked 2026-10-05/06 and broke down 10-07/10-08
(BTC 86,974 → 80,329 low; ETH 2,737 → 2,405; SOL 122.25 → 105.57; ADA 0.2825 → 0.2231), then
stabilised into the weekend. BTC is the only one still above its 50-day. ETH and SOL are below
both their 20- and 50-day.

**`ADA` is the relative leader and the only major in a clean uptrend stack** — price 0.2546 >
sma20 0.2504 > sma50 0.2269 > sma100 0.2021, and it was the only one to print a fresh 120-day
high on 10-06. It also carries actual news: the CIP-0113 token standard went live on mainnet
(KYC, sanctions screening and freeze controls — institutional/RWA plumbing), two governance
proposals close voting **2026-10-11**, the chain is tracking a record transaction count this
epoch, and the funding rate is reportedly at a 16-week low, which is a contrarian positive.
sources: https://tradersunion.com/news/cryptocurrency-news/show/3751552-cardano-jumps-7-02percent-today-after
         https://cryptonews.net/news/analytics/33567304/

**Rejected anyway, and here is the quantified reason — no major clears the floors long.**
The crypto swing stop floor is 2.5 ATR (config/strategy.md: weekends, no halts, fat tails).
Measured to each coin's *own* 120-day high, the best possible reward-to-risk with a compliant
stop is:

| Coin | 2.5 ATR stop costs | upside to 120d high | max R:R to the high |
| --- | --- | --- | --- |
| BTC | 5,008 (6.05%) | 4,508 (5.45%) | **0.90** |
| ETH | 191.74 (7.70%) | 315.38 (12.66%) | **1.64** |
| SOL | 11.29 (10.31%) | 15.49 (14.16%) | **1.37** |
| ADA | 0.0430 (**16.89%**) | 0.0279 (10.96%) | **0.65** |

Not one reaches 2.0. Every long I could construct required a target materially *above* the
prior high — ADA needed 0.3406, i.e. 21% past its own record — and that is reverse-engineering
the target to clear the floor, which config/strategy.md names as the failure mode and which
this report has already been caught doing. ADA's 6.77% daily ATR is the whole problem: the
honest stop is 17% wide, so the coin has to break out hard before the geometry works. **No
crypto long captured.** ADA becomes a real idea on a decisive close above 0.2825, where the
stop can sit under the breakout and the target is open-ended rather than borrowed from history.

**The one crypto construction that does pass, and why I am still not taking it.** ETH is the
genuinely broken major, so the short is the trade the data points at — and Robinhood Crypto
cannot short, so per config/universe.md it must be micro ether futures, not a spot `sell`.
Entry 2,491.31, stop 2,683.05 (2.5 ATR, and just under the 2,697-2,699 pre-breakdown shelf, so
a reclaim falsifies it cleanly), target 2,100 → **R:R 2.04**, target 5.1 ATR away. The thesis
would be coherent: ETH fell 8.7% in three sessions through both MAs while BTC held its 50-day,
ETH/BTC is 0.0301 and falling, and the macro leg is hostile (TLT near its 120-day low, the
metals unwind, a firm dollar — the liquidity bid leaving).
I am not publishing it for one honest reason: **I could not verify the contract.**
config/universe.md requires the specific contract month stated and verified, never recalled,
and with the October micro-ether contract inside its expiry window the choice between the
November and December listing is exactly the detail I would be guessing at. A guessed contract
code is a fabricated number by another name. Recorded in full so tomorrow's run can verify the
listing and take it if the setup survives.

## [06:32 ET] META-FINDING — why only three ideas cleared, stated as arithmetic
This is the most useful thing to carry into the report, because an honestly short report needs
an honest reason. I set levels on 13 instruments today with a compliant stop (2.0 ATR stock /
1.8 ETF / 2.5 crypto) and a target at or below the instrument's own 120-day high. Results:

**Cleared 2.0:** GS 2.09, STLD 2.12, UNH 2.26, BAC 2.26, MS 2.10 — and CLF at 2.01 only with
the stop sitting exactly on the floor, which is why CLF is on the watchlist instead.
**Failed:** WFC 1.47, NUE 1.43, FCX 1.66, ETH 1.64, SOL 1.37, BTC 0.90, ADA 0.65.

The split is not random, and the pattern is the finding: **everything that cleared is 16-23%
below its 120-day high with a dated earnings catalyst, and everything that failed is either a
leader too close to its high or a crypto asset whose ATR is too wide.** GS -22.4%, MS -18.2%,
UNH -17.8%, STLD -17.4%, BAC -16.7% all pass *because* the drawdown left room to mean-revert.
FCX (-8.2%), WFC (-9.2%) and NUE (-10.6%) fail because a 2.0-2.5 ATR stop costs more than the
distance to the prior high. The leaders I actually like on trend — XLE -1.65% off its high,
DINO -2.35% — have no room left at all, which is also why they are held rather than added to.

Two consequences synthesis must not paper over:
1. **Today's publishable set is one style bet.** Three different sectors (financials, steel,
   managed care) but one methodology: buy a capitulated large cap into its own print, entry
   above the market, confirmation required. If post-capitulation mean reversion does not work
   this month, all three fail together regardless of sector. The correlation cap counts drivers,
   not styles, so nothing in the config catches this — I am flagging it by hand.
2. **Every one of the three is an entry ABOVE Friday's close requiring confirmation**, and two
   of the three (GS, UNH) carry `catalyst.wait: true`. A likely and correct outcome is that
   some never trigger. That is deliberate: config/strategy.md records 31 pullback entries
   against 1 breakout in the first month with a 42% fill rate, and the fills selected for the
   ideas that were already falling.

## [06:33 ET] LONG-TERM LANE — worked, and deliberately left empty today
config/strategy.md says the long-term lane is the one most easily crowded out, so it gets a
decision rather than silence. **No new long_term idea captured, and the reason is portfolio
construction rather than a lack of candidates.**
The book already holds **8 long_term positions** (CCJ, NKE, LCII, PFE, LULU, BCC, KHC, plus the
uranium exposure) and **7 of the 8 are underwater**: LULU -17.8%, LCII -16.7%, NKE -14.8%,
CCJ -6.3%, BCC -3.8%, KHC -3.2%, with only PFE +2.5%. Nothing has closed, so the track record
reports "no closed trades yet (n=8)" and I must not claim the strategy is failing — the marks
are unrealised and the sample is literally zero.
But the *composition* is a finding that needs no closed trades: they are nearly all the same
idea — a de-rated consumer or industrial name bought on a recovery thesis that needs lower
rates to work — while today's data has TLT within 2% of its 120-day low, ITB at its own 120-day
low -20.3% off its high, IWM -8.6% and under its 50-day, and the market entertaining additional
Fed *hikes*. BCC, LCII and the awaiting-entry `ITB` short are three expressions of one rate
call. Adding a ninth correlated de-rated-value name today would be doubling a driver
concentration I can measure, on no new information.
Candidates I did work and declined, with the reason:
- **`URA` / uranium accumulation** (38.90, -34.03% off high, 120d low 37.18) — the genuine
  anomaly of the day: uranium spot broke a **19-year record** while the equities collapsed.
  Declined on the correlation cap, not on merit: `CCJ` and `CEG` are both already open on the
  nuclear driver, and URA would be a third. If CCJ is ever closed, this is the better
  instrument for the same thesis — a basket cannot be stopped out by one flooded mine shaft,
  which is precisely what happened to CCJ at McArthur River.
- **Oil services (`SLB` -19.0%, `HAL` -25.3%, `OIH` -15.4%, all below both MAs)** against
  producers leading (`XOP` -4.7%, above both). The 11-point producer/services gap looks like a
  mean-reversion setup and is the one I most wanted. Declined because the structural bear case
  is the one that has been right for years: producer discipline means free cash flow goes to
  buybacks rather than to rigs, so services stay cheap. Betting on that reversing needs capex
  guidance I did not have time to read. `HAL` reports 10-20 bmo and `SLB` 10-23 bmo — that is
  the work for a day with budget to read two transcripts.
- **Precious metals** (GLD -12.6%, SLV -32.3% off highs, both below their 20- and 50-day).
  Watchlist, not a position. A 32% drawdown in silver after a vertical move to ~$121 is a
  broken momentum trade mid-repair; the first honest entry is a reclaim of the 50-day, not a
  catch of the knife.

## [06:34 ET] VERIFICATION — recomputed every figure on all three captures, independently
Re-derived from entry/stop/target and the fetched ATR14 rather than trusting what I wrote into
the candidate (CLAUDE.md: never trust a figure the model wrote about its own idea):

| Sym | R:R | stop ATR | target ATR | baseline WP | claimed WP | claimed edge |
| --- | --- | --- | --- | --- | --- | --- |
| GS | 2.091 | 2.519 | 5.267 | 0.324 | 0.42 | +9.6pts |
| STLD | 2.119 | 2.500 | 5.298 | 0.321 | 0.40 | +7.9pts |
| UNH | 2.244 | 2.538 | 5.697 | 0.308 | 0.42 | +11.2pts |

All three clear the 2.0 swing R:R floor, all three clear the 2.0 ATR stop floor *and* the 2.5
ATR comfortable level, all three sit inside the 6.0 ATR target guide, and all three claim
positive expectancy with an edge well under the 20-point "large claim" threshold. **No figure
here was tuned to pass** — the ideas that needed tuning (CLF, WFC, NUE, FCX and every crypto
long) are in the rejection blocks above instead.

## [06:35 ET] VENUE CHECK — all three are unambiguously Robinhood-tradeable
`GS` (NYSE), `STLD` (Nasdaq) and `UNH` (NYSE) are large-cap US exchange-listed common stocks,
long only, no margin required — squarely inside `Robinhood Stocks` with nothing uncertain to
verify. The two instruments that *would* have needed runtime verification are the ones I did
not publish: the micro ether futures contract month (see the crypto block — this is exactly
why I declined it) and any event contract.

## [06:35 ET] RISK CONCENTRATION — the one thing the config cannot catch, flagged by hand
**September CPI on Tue 2026-10-14 08:30 ET is a shared single point of failure for two of the
three ideas, and the correlation cap does not see it.**
- `GS` reports Tue 10-13 pre-market; its entry triggers on the reaction that same day.
- `UNH` reports Tue 10-13 pre-market; same.
So both positions, if they trigger at all, are **one day old when CPI prints**. And the driver
behind both drawdowns *is* the rate path — the bank complex sold off specifically on fear of
additional Fed hikes, with TLT within 2% of its 120-day low. A hot September CPI re-fires the
exact cause of both setups while both positions are at their most fragile.
`STLD` is the diversifier here only by timing: its 10-19 print lands after CPI has resolved.
**Explicit instruction for the report: do not add size to GS or UNH before 10-14 08:30 ET**, and
treat a simultaneous trigger in both on 10-13 as one position's worth of risk, not two. Combined
size on GS + UNH is 4.5% of capital, which is within the 5%-per-idea rule only because the
config counts ideas rather than shared catalysts.

## [06:36 ET] RESEARCH COMPLETE
- **candidates captured: 3** (GS, STLD, UNH) — all `swing`, all `buy`, all equities.
  GS conviction 3, STLD 4, UNH 4. Combined position size 7.0% of capital.
- **Deliberately short.** 13 instruments had levels set; 5 cleared 2.0 R:R with a compliant
  stop and 2 of those 5 were cut on the correlation cap (MS, BAC — same trade as GS). The
  arithmetic for every rejection is in the blocks above. config/strategy.md: "if the count
  comes up short, publish fewer" — four strong ideas beat ten with six of filler, and today
  three is what the tape actually offered.
- **Honest skews synthesis must state, not hide:**
  - No crypto, on a weekend run where config/strategy.md says crypto should carry more of the
    report. Reason is quantified, not a shrug: no major clears 2.0 R:R to its own 120-day high
    with a 2.5 ATR stop (BTC 0.90, ETH 1.64, SOL 1.37, ADA 0.65).
  - No event contracts — **blocked by a data failure, not by judgment.** Every Kalshi price
    field returned null; I will not invent an implied probability.
  - No long_term idea, by portfolio-construction choice, with 8 already open and 7 underwater.
  - No intraday ideas: the market is shut, so same-session levels would be fiction.
  - All three ideas are one *style* (capitulated large cap into its own print, entry above the
    market, confirmation required) even though they are three sectors.
- **Position decisions: all 15 reviewed.** 8 hold-as-is, 4 hold-on-notice (CCJ, LCII, BCC, KHC),
  2 close instructions (the LULU and NKE boxed long legs), 1 held with no change (DAL).
  **Two decisions exist only as prose and synthesis MUST carry them**, because no candidate row
  could express them without corrupting live positions: closing the LULU and NKE long legs
  (a `sell` candidate would merge into the live short and overwrite its stop and target), and
  the trailing-stop instructions on DINO and CEG (any tightened stop fails the ATR floor
  measured from the original entry). Both are written up in the POSITION REVIEW block.
- **New invalidation supplied:** LCII had neither a stop nor an invalidation condition. Now it
  has one — close on negative quarterly EPS, or two consecutive quarters under 1.50.
- **Sources that failed:**
  - `market_data.py macro` — hung twice, killed at 180s and 400s (exit 124). No rates, VIX,
    DXY or FRED data at all. Regime read rebuilt from ETF proxies via `quote` + `history`.
    **There is no VIX figure in this run; synthesis must not imply one.**
  - `market_data.py events` — structurally broken for discovery: it fetches only the first 200
    open Kalshi markets and filters client-side, and all 200 returned belonged to one movie
    series, so every search returns 0. Worked around via `series_ticker`, but then **all price
    fields (yes_bid, yes_ask, last_price, volume, open_interest) returned null**, on both the
    list and per-ticker endpoints. Event contracts were therefore impossible this run.
  - `market_data.py implied` — HTTP 401 Unauthorized from yahoo-options. **The
    options-implied-move check could not be run on any idea today.**
  - `market_data.py short` — ReadTimeout from api.nasdaq.com on CCJ. No short-interest or
    days-to-cover data for any name.
  - CoinGecko `/market_chart` 429'd on the third coin; crypto OHLC sourced from Kraken instead.
  - WebSearch for a generic "week ahead" returned results from 2013-2016 and was useless; the
    targeted searches worked.
- **Coverage gaps / first things to check tomorrow:**
  1. **`AA` is down 49.99% from its 120-day high, sitting on its 120-day low, and fell 1.47% on
     a day every other metal rallied — with earnings 10-15 amc. I could not diagnose why.**
     That is the single biggest unexplained dislocation I found.
  2. Oil services vs producers: an 11-point gap (OIH -15.4% vs XOP -4.7%). Needs the HAL
     (10-20) and SLB (10-23) capex guidance read properly before it is tradeable.
  3. Verify the micro ether futures contract month and re-test the ETH short (construction and
     levels are in the crypto block; it returned 2.04).
  4. Re-test `CLF` on a pullback into its 11.96-12.04 MA cluster, where the geometry works.
  5. Small and micro caps got almost no time this run — IWM is -8.6% and under its 50-day, so
     nothing there passed a first look, but that is not the same as having hunted them.

## [06:36 ET] REJECTED — AA (Alcoa) — dislocation now DIAGNOSED, and it is impairment not mispricing
Went back and resolved the open question above, because publishing or rejecting a -50% name on
"I don't know why" is not research. The drawdown is fully explained and the explanation is
fundamental:
- **Aluminum prices fell hard.** A US-Iran framework reopening Strait of Hormuz shipments put
  LME aluminium at a two-month low in mid-June, three-month futures -3% to **$3,426/metric
  tonne**. Alcoa carries a **15-day pricing lag**, which compounded the late-June decline into
  the reported quarter.
- **Management cut production guidance.** 2026 alumina output now **up to 9.6Mt, down from at
  least 9.7Mt**, citing operational problems at the **Pinjarra refinery**. A guidance cut on a
  named operational fault is the opposite of a sentiment de-rating.
- **Q2 missed** (adj EPS 2.12 against roughly 2.32 expected per that reporting; note the fetched
  finnhub estimate was 2.1173, i.e. a +0.13% "beat" on a different estimate base — **the two
  sources disagree and I am not resolving which consensus is right**).
- **M&A overhang** from the planned South32 asset acquisition.
sources: https://www.barchart.com/story/news/3340561/aa-stock-dips-as-alcoa-cuts-aluminum-production-guidance
         https://www.gurufocus.com/news/8916316/alcoa-aa-shares-decline-amid-falling-aluminum-prices
         https://www.quiverquant.com/news/Alcoa+Slides+as+Metals+Weakness+Adds+to+Post-Earnings+and+Deal+Overhang
Measured confirmation that this is deterioration rather than a bottom: analyst revision
direction is **deteriorating** (bullish share 72.7%, -1.2pp, and a sell rating reappeared in the
Aug/Sep snapshots after being absent in July), with **zero insider open-market buys against 4
sales**. Earnings 10-15 amc.
**This also answers why AA fell 1.47% while every other metal rallied Friday** — its problem is
company-specific (Pinjarra, the pricing lag, South32) and alumina-specific, so it does not
participate in a base-metals beta day. Rejected. Coverage gap #1 above is now closed.

**Usefully, AA is the control case for the three ideas I did publish.** The discriminator I
applied was not size of drawdown but direction of revisions plus cause of drawdown:
- `UNH` -17.8%: revisions **improving** (+2.9pp), two consecutive beats (+28.8%, +8.9%) → published
- `STLD` -17.4%: revisions **improving** (+1.7pp), 3 beats in 4 → published
- `GS` -22.4%: cause is a **deferral** (ECM pipeline slipping to 2027), not an impairment → published
  at conviction 3 precisely because its revision/insider evidence is absent, unlike the other two
- `AA` -50.0%: revisions **deteriorating**, cause is a **guidance cut on a named operational
  fault** → rejected
- `CCJ` -32.9% (held, not added): revisions **deteriorating** (-3.9pp), cause is a supply-route
  flood plus utilities refusing to contract → hold, no add
A 50% drawdown is not a bigger opportunity than a 17% one. It is usually a better-informed market.

## [06:37 ET] PROCESS FINDING — 11 of 13 awaiting-entry ideas were directionally RIGHT and
## never filled, because the entry was placed on the wrong side of the move
I priced every one of the 15 awaiting-entry rows from prior_context against Friday's close.
Two are event contracts with no fetchable price. Of the 13 that could be priced:

| Idea | Entry | Friday close | Moved | Direction called? |
| --- | --- | --- | --- | --- |
| `VST` BUY | 132.00 | 161.48 | +22.3% past entry | **right**, never filled |
| `OXY` BUY | 54.00 | 60.11 | +11.3% past | **right**, never filled |
| `FCX` BUY | 68.20 | 73.69 | +8.1% past | **right**, never filled |
| `MU` BUY | 960.00 | 1029.00 | +7.2% past | **right**, never filled |
| `SMMT` BUY | 17.10 | 17.59 | +2.9% past | **right**, never filled |
| `XLF` BUY | 54.23 | 54.73 | +0.9% past | **right**, never filled |
| `ITB` SELL_SHORT | 89.80 | 84.76 | -5.6% past | **right**, never filled |
| `GLD` SELL | 406.77 | 384.58 | -5.5% past | **right**, never filled |
| `AAL` SELL_SHORT | 13.35 | 12.76 | -4.4% past | **right**, never filled |
| `TLT` SELL_SHORT | 79.90 | 77.98 | -2.4% past | **right**, never filled |
| `IYR` SELL_SHORT | 97.80 | 96.10 | -1.7% past | **right**, never filled |
| `DG` BUY | 134.50 | 127.23 | -5.4% away | wrong so far, still reachable |
| `KXCPIYOY`/`KXFEDDECISION` | — | no price | — | unknown |

**Eleven of thirteen called the direction correctly and earned nothing**, because the entry was
always on the far side of the move. The mechanism is not bad luck, it is arithmetic:
- Every long was pitched **below** the market, so it fills only if price first falls. When the
  bullish call was right and price simply rose, there was no fill. Six for six.
- Every short was pitched **above** the market, so it fills only if price first rises. When the
  bearish call was right and price simply fell, there was no fill. Five for five.

So the report has been selecting *against* its own correct calls. This is the same defect
config/strategy.md records from a different angle — 31 pullback entries against 1 breakout, 42%
fill rate, and the fills were the ones already falling — but the version above is sharper,
because it shows the unfilled ideas were not merely unfilled, they were **right**. The report's
research has been better than its fill rate suggests, and the entry convention has been eating
the alpha.

**This is why all three of today's captures use an entry ABOVE Friday's close with a
stop_limit trigger**, which until now I had justified only as "the report lacks breakout
entries." The real justification is this table: a long entry above the market fills precisely
when the call is right. The cost is real and should be stated — you pay up, the stop sits
further away in price terms, and a trigger can fill and immediately reverse. But it is the
correct trade-off against an 11-for-13 record of being right and unpaid.

**Recommendation for the config, not actioned here:** `config/strategy.md` should say that a
pullback entry needs a named support level *and* a stated reason the level will be reached,
rather than only the former. Flagging rather than editing — I am a research phase and this is a
strategy change.

## [06:38 ET] NO RE-PITCH — SMMT, and the rest of the awaiting-entry book
`SMMT` 17.59 (+2.45%), above its 20-day (17.03) and 50-day (15.46), -39.82% off its 29.23 high,
ATR 1.1778 (**6.7%**), $125M/day, earnings 10-19 (est -0.2959, pre-profit biotech). The level is
**unchanged at 17.10** and it was published only yesterday, so there is nothing to amend and no
new information to amend it with. Also worth recording that it is marginal on the same test CLF
failed: entry 17.10 / stop 14.74 / target 22.50 returns 2.29 but only with the stop at exactly
**2.00 ATR**, i.e. on the floor; widening to 2.5 ATR drops it to 1.84.
`VST` BUY @132 is now 22.3% below a 161.48 market and should be retired as stale rather than
carried as if it were live — it has not been a reachable idea for weeks. `DG` BUY @134.50 is the
only awaiting-entry long the market is still approaching from above (127.23).

## [06:39 ET] REVISION — MS added, GS re-sized. This supersedes the 06:36 RESEARCH COMPLETE block.
I pressure-tested my own bank pick after writing the first completion block, because GS was the
one candidate whose evidence I had *not* checked on the same axis I used to reject AA — analyst
revision direction. The check changed the answer:

| Bank | revisions | beat record | reports |
| --- | --- | --- | --- |
| `MS` | **improving, +4.4pp** to 60.6% | 4 of 4: +14.11%, +10.92%, +6.78%, +29.27% | 10-14 bmo |
| `GS` | **flat, 0.0pp**, 46.9% bullish (16 holds, 1 strong-sell) | 4 of 4: +40.71%, +3.31%, +16.53%, +8.14% | 10-13 bmo |
| `BAC` | **deteriorating, -3.5pp** | 4 of 4: +5.88%, +8.62%, +1.28%, +10.30% | 10-14 bmo |

By the discriminator I used to reject AA and to publish UNH and STLD — direction of revisions,
not depth of drawdown — **MS is the better idea than GS, and BAC is the worst of the three**,
which reverses my 06:21 note that BAC had "the tidiest arithmetic". Two further points favour MS:
its stop at 181.90 sits **below** the 182.47 120-day low (structurally correct, unlike UNH's,
which I flagged), and it reports on **CPI morning**, so earnings and the macro print clear within
two hours of each other rather than leaving a one-day-old position exposed the way GS does.

Actions taken rather than just noted:
- **Captured `MS`** BUY swing, conviction 4: entry 193.40 stop_limit through the 10-06 high
  193.14, stop 181.90, target 218 / 232. R:R 2.139, stop **2.749 ATR**, target 5.879 ATR.
- **Re-captured `GS`** with `position_size_pct` cut 2% → 1.5%, its positioning evidence corrected
  to include the flat revision trend and the 4-of-4 beat record, and its `key_risk` rewritten to
  state plainly that GS and MS are **one bet**. Synthesis takes the last entry per symbol, so the
  1.5% version governs. Combined GS + MS = 3.0% of capital, to be treated as a single position.
- GS kept rather than dropped because its 4-of-4 record includes a +40.71% Q2 surprise (20.98
  against 14.9103) and its drawdown has the most specifically reversible cause in the group. But
  it is now explicitly the junior of the pair, at conviction 3 against MS's 4.

## [06:40 ET] RESEARCH COMPLETE (final — supersedes the 06:36 block)
- **4 distinct candidates captured** from 5 writes (GS captured twice; the later 1.5% version is
  the live one). All `swing`, all `buy`, all US large-cap equities on `Robinhood Stocks`.
  Re-verified independently from entry/stop/target and fetched ATR14 — every one clears the 2.0
  R:R floor, the 2.0 ATR stop floor *and* the 2.5 ATR comfortable level, the 6.0 ATR target
  guide, and positive expectancy with claimed edge well under 20 points:

  | Sym | Conv | Size | Entry | Stop | Target | R:R | stop ATR | tgt ATR | baseline WP | WP |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | MS | 4 | 1.5% | 193.40 | 181.90 | 218.00 | 2.139 | 2.749 | 5.879 | 0.319 | 0.42 |
  | UNH | 4 | 2.5% | 389.50 | 367.00 | 440.00 | 2.244 | 2.538 | 5.697 | 0.308 | 0.42 |
  | STLD | 4 | 2.5% | 245.50 | 228.75 | 281.00 | 2.119 | 2.500 | 5.298 | 0.321 | 0.40 |
  | GS | 3 | 1.5% | 906.50 | 857.00 | 1010.00 | 2.091 | 2.519 | 5.267 | 0.324 | 0.42 |

  Total capital at risk 8.0%, but **GS + MS must be sized as one 3.0% position**, so the honest
  count is three independent bets totalling 8.0%.
- **All four entries sit ABOVE Friday's close and require a stop_limit trigger**, and three of
  the four carry `catalyst.wait: true`. A likely and correct outcome is that some never fill.
  This is the deliberate correction to the entry-placement finding above — 11 of 13 awaiting-entry
  ideas were directionally right and never filled because every long sat under the market.
- Everything else from the 06:36 completion block stands unchanged: the honest skews (no crypto,
  no event contracts, no long_term, no intraday — each with a quantified reason), all 15 position
  decisions, the two prose-only instructions synthesis must carry (close the LULU and NKE boxed
  long legs; trail stops on DINO and CEG), the new LCII invalidation, the five failed sources
  (`macro`, `events`, `implied`, `short`, CoinGecko 429), and the CPI concentration warning —
  which now covers **three** ideas, since MS also triggers off the 10-14 print.
- Coverage gap #1 (AA) was closed during the run; gaps 2-5 remain for tomorrow.
