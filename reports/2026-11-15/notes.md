# Research log — 2026-11-15

## [06:03 ET] SETUP — Sunday 2026-11-15, US equities and futures closed
- Weekend run per config/strategy.md: crypto + event contracts are the actionable lane.
  Equities = week-ahead prep, entries for the NEXT open (Mon 2026-11-16), marked swing.
- Budget start 11:00 UTC / 06:00 ET. Minute-20 hard deadline 11:20 UTC. 70% mark 11:42 UTC.

## [06:03 ET] MACRO — crypto tape (source: coingecko via market_data.py crypto)
- BTC 65,527 (-2.56% 24h), mkt cap 1.317T, 24h vol 56.1B
- ETH 1,829.42 (-4.12% 24h), mkt cap 223.5B
- SOL 72.08 (-4.80% 24h), mkt cap 42.6B
- Read: broad crypto risk-off, alts leading down (ETH/SOL ~-4 to -5% vs BTC -2.6%).
  BTC dominance rising inside a falling tape = defensive rotation within crypto, not a bid.

## [06:03 ET] PRIOR-POSITION FACT — /MBTZ6 SHORT @ 74,075 (published 2026-11-09) never filled
- BTC spot is now 65,527, ~11.5% BELOW that short entry. The move happened without us.
- Chasing a short here is selling into an already-extended decline. Do NOT re-pitch at a
  lower entry just to get filled — that is the reverse of the stop-walking error in CLAUDE.md.

## [06:07 ET] DATA GAP — event contracts unavailable this run
- `market_data.py events` returns ok:true with count:0 for Fed, CPI, bitcoin, inflation,
  recession. The source answers but lists nothing. That is a SOURCE GAP, not evidence that
  no event markets exist. No event-contract candidate can be honestly priced this run:
  the entry would have to be a cents price I did not fetch. Carrying none.
- Consequence: the weekend lane narrows to crypto only, since equities/futures are shut.

## [06:06 ET] DATA SOURCE MAP for this run (matters for what I can honestly claim)
- `quote` -> finnhub WORKS. `history` -> nasdaq WORKS (ATR/SMA available).
- `macro` -> TIMED OUT (killed at 120s, exit 143). Using individual quotes instead.
- yahoo -> HTTP 429 rate-limited all run. stooq -> connect timeout. No twelvedata/alphavantage key.
- No crypto history subcommand exists, and yahoo 429 blocks BTC-USD history.
  => I cannot compute a fetched ATR for BTC/ETH this run. Any crypto futures idea would need
  a stop clearing 2.5 ATR that I CANNOT verify. Per CLAUDE.md rule 2 I will not invent one.

## [06:07 ET] MACRO — SPY, the one index read I could fetch (source: nasdaq history + finnhub quote)
- SPY last close 754.37 as of 2026-11-13T21:00Z (Friday close; market "closed", age 2285 min)
- ATR14 12.77 (1.69%), SMA20 759.02, SMA50 764.43, SMA200 unavailable from this source
- 120d range 716.58-781.62; 3.49% off the high
- Price is BELOW both SMA20 and SMA50 = corrective tape, not an uptrend to buy blindly.
- The Nov 5 shock is the structure that matters: open 765.47 -> close 733.00, low 732.71 on
  125.9M shares (~3x the 44.1M 30d average). That is a capitulation bar, not drift.
- Since then: bounce to 759.81 (Nov 11) then fade to 754.37. Lower highs vs the 781.62 high,
  but holding well above the 732.71 shock low. Range-bound between ~733 and ~762.

## [06:17 ET] CALENDAR — week ahead is dense (source: finnhub earnings via market_data.py)
- Mon 11-16 bmo: PDD(117.1B rev est), BIDU, XPEV, TSN; amc: **ACM**, PAGS
- Tue 11-17 amc: **NVDA** (111.2B rev est, eps 2.52); bmo: HD(44.1B), DIS(25.4B), WSM
- Wed 11-18 bmo: TGT(26.8B), LOW(22.6B), TJX(16.0B), ROST, GAP; amc: PANW
- Thu 11-19 bmo: BABA(275.2B), WMT(189.1B), NTES; amc: INTU, KEYS
- Fri 11-20 bmo: BJ
- Read: this is retail-earnings week bracketed by NVDA Tue amc. The whole tape's direction
  Wed-Fri is downstream of NVDA + the consumer read from HD/TGT/LOW/WMT. That is a
  CORRELATION CAP problem for any new long: almost everything cyclical this week is one bet.
- `implied` is UNAVAILABLE all run (yahoo-options 401 Unauthorized), so I cannot check any
  target against the options-priced move. Noted as a gap, not guessed at.

## [06:18 ET] POSITION UPDATE — ACM — opened 2026-11-07, entry 66.74, now 70.50, +5.6%
- EARNINGS TOMORROW: 2026-11-16 after the close (fetched calendar, eps est 1.5938, rev 1.9B).
  This was NOT a known dated catalyst when the position was opened per prior context.
- Levels (nasdaq, 120d): ATR14 2.1749 (3.08%), SMA20 64.724, SMA50 62.5754,
  range 56.39-76.8499, 8.26% off high, 30d avg dollar volume 91.6M (ample).
- Structure: ran 65.68 (11-02) -> 70.50 and then coiled 70.21/70.63/70.25/70.11/70.50 for
  five sessions. A tight consolidation well above both MAs going into a print.
- decision: HOLD, raise stop 61.50 -> 64.50, trim half into the print.
- why: 64.50 sits just under SMA20 (64.724) - a real level, not a round number - and is
  2.76 ATR below the current 70.50, so it is not a noise stop. The old 61.50 stop is now
  4.14 ATR / 12.8% away and no longer protects a +5.6% gain.
- HONEST CAVEAT I am flagging for the red team: because this position is in profit, a stop
  near the original entry makes the entry-measured R:R read ~4.7:1. That number is an
  artifact of the position having worked, NOT new edge, and it is exactly the stop-walking
  pattern CLAUDE.md flags on KRE. Measured from TODAY's 70.50 the trade is risk 6.00 to
  reward 6.72 = 1.12:1, which FAILS the 2.0 swing floor. So: do not treat this as a fresh
  entry. No new money at 70.50 ahead of a binary print.
- A stop does not protect against an earnings gap. Trimming half is the only real hedge.

## [06:23 ET] POSITION UPDATE — BCC — opened 2026-08-18, 88 days, entry 76.50, now 67.39, -16.8%
- decision: **CLOSE at the Monday open.** This is the worst position on the book and the only
  one with no stop and no working thesis.
- Levels (nasdaq 120d): ATR14 3.5338 = 5.24% (violent), SMA20 74.266, SMA50 75.0332,
  range 66.85-88.4299. Price is 23.79% off the high and **0.81% off the 120-day LOW**.
- Eight-session slide: 77.98 (11-04) -> 73.75 -> 70.24 -> 72.57 -> 70.42 -> 69.52 -> 67.92
  -> 67.39. Below SMA20 and SMA50 by ~9-10%. Making new lows, not basing.
- The 10-Q (filed 2026-11-02, period 2026-09-30) is the pivot: the decline starts the next
  session. The market read the quarter and sold it.
  source: https://www.sec.gov/Archives/edgar/data/1328581/000132858126000034/bcc-20260930.htm
- INSIDERS: 0 open-market buys in 6 months, 0 distinct buyers, 3 sells totalling $665,841.
  No insider is defending this price. source: finnhub insider transactions
- The stored target of 110.0 is +63% from 67.39. That was never a swing target and is not a
  defensible valuation anchor either - nobody re-underwrote it in 88 days.
- Why not just set a stop and hold: a 2.0-ATR stop is 7.07 wide = 60.32, another 10.5% of
  downside on a position already -16.8%, to hold an asset with no insider support making new
  lows after a bad quarter. And a target that would clear the 2.0 swing floor from 67.39
  requires 81.53, above SMA50 and +21% - that is reverse-engineering a target to clear a
  floor, which CLAUDE.md forbids. The idea fails the floor, so the idea is over.
- Captured as direction `sell` = EXIT a held long. This is NOT a short recommendation.

## [06:11 ET] REGIME READ — a real divergence, from fetched levels (nasdaq 120d)
| sym | last | sma20 | sma50 | off high | read |
| --- | --- | --- | --- | --- | --- |
| XLP | 92.35 | 89.485 | 85.647 | -1.12% | staples leading, above both MAs |
| XLV | 188.85 | 183.646 | 175.046 | -1.80% | healthcare leading, above both MAs |
| HD | 348.69 | 333.833 | 312.154 | -3.79% | repair/remodel strong |
| LOW | 227.73 | 213.434 | 199.867 | -3.09% | repair/remodel strong |
| TGT | 161.45 | 156.361 | 156.371 | -5.45% | MAs converged = coil |
| SPY | 754.37 | 759.022 | 764.428 | -3.49% | BELOW both MAs |
| LEN | 83.61 | 85.370 | 81.582 | -12.93% | homebuilder breaking down |
| BCC | 67.39 | 74.266 | 75.033 | -23.79% | building products collapsing |
| GLD | 355.45 | 368.784 | 380.906 | -17.23% | gold collapsing, below both MAs |
- The coherent story: defensives (XLP/XLV) and repair-remodel retail (HD/LOW) are leading
  while NEW CONSTRUCTION (LEN, BCC) collapses and the index sits below both its MAs.
  High rates kill new builds; existing owners renovate instead. That is one driver, so
  HD+LOW+TGT would be THREE ideas on one consumer/rates bet - at the correlation cap.
- Gold down 17.2% off its high is a regime change worth more than a single trade.

## [06:12 ET] STALE PENDING — GLD SELL @ 406.77 (published 2026-10-25) — CANCEL IT
- GLD closed Friday at 355.45. The short entry at 406.77 is 51.3 points / 14.4% ABOVE the
  market. Gold has already fallen 17.23% off its 429.42 high and sits 0.72% above its
  120-day low of 352.91, below SMA20 368.78 and SMA50 380.91.
- The bearish view was RIGHT and the order never filled. Leaving a resting short 14% above
  a market that already collapsed is not a live idea; re-pitching it at 355 would be
  chasing a 17% decline into the range low, which is the mirror of the /MBTZ6 error.
- action: cancel. Do not re-enter short gold here.

## [06:12 ET] POSITION UPDATE — TLT — opened 2026-11-04, entry 80.30, now 79.38, -1.1%
- Levels: ATR14 0.761 (0.96%), SMA20 81.0925, SMA50 80.2095, range 76.43-87.79, -9.58% off
  high. Slid 81.96 (11-09) -> 80.88 -> 80.92 -> 79.72 -> 79.38. Below SMA20 AND SMA50.
- The stop at 78.80 is now only 0.58 away = **0.76 ATR from the current price.**
- decision: **HOLD. Levels unchanged. Explicitly DO NOT widen the stop.**
- why: the 78.80 stop was set correctly - 1.5 from the 80.30 entry = 1.97 ATR, which clears
  the 1.8-ATR ETF floor. Price has simply come to it. Widening a stop because the market
  approached it converts a planned, sized loss into an unplanned larger one, and it is the
  same walk-the-stop dishonesty CLAUDE.md flags on KRE, just in the other direction.
  If 78.80 trades, the thesis was wrong and the ~1.9% loss is the one we underwrote.
- Note the stop is inside one day's range, so a noise tick can take it out. That is a cost
  of the original entry, not something to fix now by moving the line.

## [06:13 ET] POSITION UPDATE — PFE — opened 2026-08-18, entry 27.60, now 28.89, +4.7%
- decision: HOLD, no change. NOT republishing with the stored 42.00 target.
- Levels: ATR14 0.7982 (2.76%), SMA20 29.7925, SMA50 28.8018 (price sitting ON the SMA50),
  range 23.62-31.44. Support cluster of recent lows at 28.54/28.62/28.82.
- market cap 164.7B, 5,699.67M shares (finnhub profile).
- Why I will not republish the 42.00 target: 42 is +45% from 28.89 and is a VALUATION claim
  I cannot defend with a method in this run's budget. Analyst drift is mildly AGAINST it -
  bullish share 38.2%, change -0.7%; strong_buy 6->6->5->5 and sells 1->1->1->2 across
  Aug/Sep/Oct/Nov. That is weak negative positioning, not support for a 45% re-rating.
- Holding is still right: defensive pharma is the leading sector group, price is on SMA50
  support with a tight 2.76% ATR, and the position is green. But an undefended +45% target
  on the page is the kind of number this report has been wrong with before.

## [06:13 ET] POSITION UPDATE — XLU — opened 2026-11-02, entry 43.30, now 44.04, +1.7%
- decision: HOLD, no change. Working as designed, nothing to amend.
- ATR14 0.5987, SMA20 43.0725, SMA50 41.8928 - above both, closed at the top of its recent
  range (44.04 after 43.81/43.82/43.73). Stop 41.80 is 3.74 ATR away, target 46.60.
  Entry-measured R:R 2.20 clears the floor. Leave it alone.

## [06:17 ET] INSIDER SCREEN on the de-rated / pending-entry names (source: finnhub insiders, 6mo)
| sym | last | open-mkt buys | distinct buyers | buy $ | sells | sell $ |
| --- | --- | --- | --- | --- | --- | --- |
| DKS | 149.70 | **9** | **7** | **5,588,663** | 2 | 4,581,338 |
| CVS | 89.35 | 1 | 1 | 2,001,315 | 8 | 352,742,694 |
| HUN | 9.53 | 1 | 1 | 981,000 | 0 | 0 |
| CAG | 14.73 | 1 | 1 | 510,632 | 0 | 0 |
| ADM | 72.90 | 1 | 1 | 196,756 | 0 | 0 |
- DKS is the only genuine CLUSTER. Seven distinct insiders is the signal CLAUDE.md calls
  out; one buyer is an anecdote. CVS's single 2.0M buy sits against 352.7M of sales.

## [06:18 ET] DKS — best new idea of the run
- 149.70 last. ATR14 6.0096 (4.01%), SMA20 144.0875, SMA50 137.6248, 120d range
  120.151-244.38, **38.74% off high**, 30d avg dollar volume 330M (ample). Market cap
  13.31B, 88.93M shares (finnhub profile) - mid cap, so no small-cap size obligations.
- Insider buys clustered 2026-09-01 to 2026-09-30 at **129.75-136.39**: Gupta Navdeep 7,707
  sh @129.75, Barnes Matthew 3,665 @136.39, Fitzgerald Larry Jr. 1,860 @131.67, Colombo
  William J 913 @133.19, and others - 9 buys / 7 buyers / 5.59M total.
  They bought BELOW today's price and price has since reclaimed both MAs. Signal confirmed.
- DATED CATALYST: earnings **2026-11-23** (fetched calendar), eps est 1.4178, rev est 5.13B.
- THE CASE AGAINST, which is real and I am not asserting away:
  - two consecutive EPS MISSES: period 2026-09-30 actual 3.53 vs est 3.801 = **-7.13%**;
    period 2026-06-30 actual 2.90 vs est 2.9279 = -0.95%. (Prior two were beats: +19.08%, +1.46%.)
  - analyst bullish share 53.1% and **falling 8.2 points**; strong_buy 8->8->7->7,
    hold 11->11->12->13 across Aug/Sep/Oct/Nov. Analysts are downgrading into the print.
  - 2 insider sells worth 4.58M, so NET insider dollars are only ~+1.0M.
- How the structure answers it: the stop goes BELOW the entire insider cluster. If DKS
  trades under 129 then the seven people with the best information were wrong, which is a
  clean, non-arbitrary invalidation rather than a price-based one.
- LEVELS - stop set FIRST, per the rule:
  - invalidation level = below SMA50 137.62 AND below the lowest insider buy 129.75 -> 129.00
  - risk from a 144.50 entry = 15.50 = **2.58 ATR**, clears the 2.0 stock swing floor
  - target 175.50 = the 45th percentile of the 120d range, NOT a new high -> reward 31.00
  - R:R = 31.00 / 15.50 = **2.00**, exactly at the swing floor. Not reverse-engineered:
    the stop was placed on the insider cluster first and the target is a retracement level.
  - entry 144.50 is the SMA20 (144.0875), a real support level 3.5% under Friday's close -
    a routine pullback for a 4.01% ATR instrument, not a reflex discount.
  - win_probability 0.42 vs the 1/(1+2.0) = 0.333 baseline = a 9-point claimed edge. Modest
    deliberately; the insider cluster is the edge, the two misses are why it is not larger.
- Earnings 11-23 falls INSIDE the horizon, so the event risk is called out: trim half into
  the print. The edge here is the insider cluster, NOT a guess at the print.

## [06:21 ET] POSITION UPDATE — AAL SELL_SHORT — opened 2026-10-03, entry 13.35, now 13.17, +1.4%
- decision: HOLD the short. Levels unchanged (stop 14.40, target 10.60).
- Levels: ATR14 0.6129 (4.65%), SMA20 12.8998, SMA50 12.9387, range 11.63-18.79, -29.91% off high.
- SUPPORTS the short: 0 open-market insider buys in 6 months against 9 sells worth 5,669,689.
  Nobody inside is buying a 30%-off-the-high airline.
- AGAINST the short, and I am flagging it: price 13.17 is ABOVE both the SMA20 (12.90) and
  SMA50 (12.94). A short with price above both MAs is fighting the near-term trend, and the
  11-09 spike to 14.16 came within 0.24 of the 14.40 stop.
- Honest defect in the original entry: the 14.40 stop is 1.05 from the 13.35 entry = **1.71
  ATR**, inside the 2.0-ATR stock swing floor. That is a legacy of how the position was
  opened and I am NOT widening it to fix the arithmetic - that is the KRE error. Entry-
  measured R:R is 2.62 (reward 2.75 / risk 1.05), which clears, but the stop is thin.
- The 10.60 target is 19.5% below spot. That is a large ask; this is the position I would
  close first if the 14.16 high is exceeded.

## [06:22 ET] POSITION UPDATE — ONON — opened 2026-11-03, entry 34.20, now 33.63, -1.7%
- decision: HOLD, levels unchanged (stop 30.69, target 41.41).
- Levels: ATR14 1.7631 (5.24%), SMA20 34.73, SMA50 32.1614, range 26.365-41.41, -18.79% off high.
- Fell 38.62 (11-04) -> 33.63, i.e. -12.9% in eight sessions. Now BELOW SMA20, still ABOVE
  SMA50. The SMA50 at 32.16 is the line that matters; the 30.69 stop sits 4.6% below it.
- Entry-measured risk 3.51 = 1.99 ATR (at the floor), R:R 2.05 (reward 7.21). Clears, barely.
- Note the stored target 41.41 is EXACTLY the 120-day range high. That is a resistance level,
  not a conservative target, so treat the upside as the full trip back to the highs.

## [06:23 ET] LEN — notable but UNVERIFIED, so no candidate
- LEN insiders: 24 open-market buys, **but only 1 distinct buyer**, totalling 329,017,222 USD,
  0 sells. A single filer accumulating 329M dollars.
- That is a big number and one decision-maker. CLAUDE.md's standard is a cluster with
  SEVERAL distinct buyers (DKS: 7). One buyer at this dollar size is more likely a 10%
  holder or an affiliated trust than seven officers forming an independent view, and I did
  not have budget to read the Form 4s and confirm who it is.
- So: NOT captured as a candidate. Identifying the filer is the single highest-value
  follow-up for the next run - if it is officers rather than an affiliate, LEN is a better
  version of the DKS setup.
- Context cuts against it anyway: LEN is -12.93% off its high, fell 91.58 (11-09) -> 83.61,
  and is below SMA20 85.37. Its sector read-across is ugly - BCC (building products) is
  being closed today for collapsing to new lows. New construction is the weak leg of the
  divergence while HD/LOW (repair/remodel) lead.
- The existing pending BUY @ 79.50 stands UNCHANGED. 79.50 is below the SMA50 (81.58) and
  4.9% under spot; no reason to chase it up, no reason to cancel it.

## [06:24 ET] PENDING-ORDER HYGIENE — four of the ten awaiting-entry items are dead levels
| pending | published | level | spot now | gap | action |
| --- | --- | --- | --- | --- | --- |
| `GLD` SELL @ 406.77 | 10-25 | 406.77 | 355.45 | 14.4% above mkt | **CANCEL** - gold already fell 17.2% off its high |
| `/MBTZ6` SHORT @ 74075 | 11-09 | 74075 | 65527 (BTC spot) | 11.5% above mkt | **CANCEL** - the decline happened without us |
| `CVS` BUY @ 79.00 | 11-05 | 79.00 | 89.35 | 13.1% below mkt | **CANCEL** - see below |
| `KXCPIYOY-26SEP-T3.5` NO @ 18 | 09-30 | 18c | n/a | event dated 26SEP | **CANCEL** - a September CPI contract still sitting in the pending list in mid-November is a stale row, not a live order |
| `XLV` BUY @ 184.00 | 11-09 | 184.00 | 188.85 | 2.6% below | leave - 184 is just above SMA20 183.65, a real level |
| `CAG` BUY @ 14.40 | 11-14 | 14.40 | 14.73 | 2.2% below | leave - closest to filling, SMA20 14.68 |
| `HUN` BUY @ 9.00 | 11-10 | 9.00 | 9.53 | 5.6% below | leave - below SMA50 9.01 |
| `ADM` BUY @ 68.80 | 11-11 | 68.80 | 72.90 | 5.6% below | leave - ADM jumped 69.30 -> 72.90 in 3 sessions; 68.80 is still near the 68.793 range low |
| `LEN` BUY @ 79.50 | 11-13 | 79.50 | 83.61 | 4.9% below | leave (above) |
| `DKS` BUY @ 144.50 | 11-13 | 144.50 | 149.70 | 3.5% below | **RE-AFFIRMED and upgraded** - captured today with the insider cluster |
- CVS specifically: it was STOPPED OUT 2026-11-04 and re-published the next day at 79.00.
  It has since rallied 83.85 (11-06) -> 89.35 and is sitting on its SMA20 89.55 / SMA50 89.66.
  Insiders are no support: 1 buy of 2.0M against **8 sells worth 352.7M**. A resting bid 13%
  under a market that rallied away from it is not an idea; chasing it to 89 after being
  stopped out at the start of the month would be the anchoring CLAUDE.md warns about.

## [06:29 ET] INSIDER SCREEN — the negative result, which matters
- TGT 0 buys / 6 sells 18,715,036 | NKE 0 / 9 sells 1,574,773 | EL 0 / 20 sells 25,135,334
  | BIIB 0 / 2 sells 239,750 | F 1 buy 148,880 / 0 sells | PARA 0 / 0
- NOT ONE cluster outside DKS. That is why DKS is in the report: it is distinctive on this
  signal, not one of a dozen names that screened the same way.
- TGT specifically: zero insider buying and 18.7M of selling going into 2026-11-18 earnings.
  That kills any thought of a TGT long into the print, which the converged SMA20/SMA50 at
  156.36/156.37 would otherwise have made tempting.

## [06:30 ET] REMAINING OPEN POSITIONS — decision on each (levels from nasdaq 120d)
| sym | entry | last | P/L | stop | sma20 | sma50 | decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KHC | 23.00 | 25.11 | +9.2% | 21.20 | 24.431 | 23.881 | HOLD, unchanged |
| OXY | 54.00 | 58.75 | +8.8% | 50.15 | 60.498 | 59.759 | HOLD but **WATCH** |
| HII | 262.00 | 306.24 | +16.9% | **none** | 295.136 | 280.518 | **SET A STOP at 278.50** |
| UNP | 288.60 | 302.44 | +4.8% | 277.40 | 298.374 | 287.276 | HOLD, unchanged |
| ABT | 103.00 | 108.52 | +5.4% | 97.00 | 106.963 | 103.910 | HOLD, unchanged |
| PYPL | 56.50 | 59.28 | +4.9% | 54.10 | 57.914 | 55.609 | HOLD, unchanged |
| RTX | 199.00 | 198.58 | -0.2% | 186.00 | 196.558 | 192.799 | HOLD, unchanged |
- KHC, UNP, ABT, PYPL, RTX are all above BOTH their MAs with stops below both. Nothing to
  do; they are working as designed. Note UNP (315.99), ABT (117.34) and PYPL (62.73) all
  carry targets set EXACTLY at the 120-day range high, i.e. at resistance - so the last leg
  of each is the hardest, and none should be added to here.
- **OXY is the one deteriorating**: +8.8% on paper but it closed 58.75, BELOW both the SMA20
  (60.498) and SMA50 (59.759). A position in profit that has lost both moving averages is
  how a winner becomes a loser. Stop 50.15 is 4.67 ATR away (ATR 1.842) - far too loose to
  protect the gain, but tightening it mid-trade is the KRE error, so: HOLD, do not add, and
  this is second after AAL in the close-first queue.
- **HII needs a stop and this is the real change.** +16.9%, the largest gain on the book,
  and completely unprotected 88... (opened 2026-10-12, 32 days). ATR14 13.6432 = 4.46%, so
  any stop respecting its volatility must sit ~9% away. 278.50 is 2.03 ATR below spot and
  just under the SMA50 (280.518) - a real level. It still locks in +6.3% against the 262.00
  entry. A tighter trail at the SMA20 (295.14) would be 0.81 ATR and would be taken out by
  one ordinary day.
- HONEST NOTE on HII arithmetic: with the stop (278.50) ABOVE the entry (262.00) the
  entry-measured reward-to-risk is not a real number - risk is negative, the position cannot
  lose from here if the stop holds. I am publishing `risk_reward: null` rather than an
  invented large figure. This is the same artifact I flagged on ACM and it must not be read
  as edge.

## [06:34 ET] CORRECTION — ACM, my own arithmetic was wrong and I am superseding it
- I first proposed raising the ACM stop 61.50 -> 64.50. Re-checking against the floor:
  - 64.50 is only (66.74-64.50)/2.1749 = **1.03 ATR** from the 66.74 entry -> FAILS the
    2.0-ATR stock swing floor.
  - the ORIGINAL 61.50 stop is (66.74-61.50)/2.1749 = **2.41 ATR** -> already clears it.
- So "tightening" the stop would have broken a floor the position already satisfied, and it
  would have lifted entry-measured R:R from 2.00 to 4.68 by moving the stop in - which is
  precisely the KRE stop-walking pattern, committed by me, in the name of prudence.
- SUPERSEDED DECISION: **leave the ACM stop at 61.50.** The real protection against an
  earnings gap is trimming half into the print, which no stop placement can substitute for.
  Re-captured with stop 61.50, R:R 2.00, win_probability 0.45 vs a 0.333 baseline.
- Lesson for the report: on a position in profit, "raise the stop" is not automatically the
  conservative choice. Measure it from the ENTRY against ATR before calling it risk control.

## [06:36 ET] REJECTED — XLP — leadership is real but the floor is not clearable
- 92.35, ATR 1.6429, SMA20 89.485, SMA50 85.6474, 120d range 80.1-93.4, only 1.12% off high.
- Honest construction: entry 89.49 (the SMA20, real support), 1.8-ATR ETF stop = 2.96 wide
  -> 86.53 (just above SMA50). Target needed for 2.0 R:R = 95.41, which is ABOVE the
  120-day high of 93.40. Measured to the range high instead, R:R = 3.91/2.96 = **1.32**. Fail.

## [06:36 ET] REJECTED — XLV — same failure, same reason (and it is already a pending entry)
- 188.85, ATR 3.6954, SMA20 183.6455, SMA50 175.0456, range 145.31-192.32, 1.80% off high.
- Entry 183.65 (SMA20), 1.8-ATR stop = 6.65 -> 177.00 (above SMA50). Target for 2.0 R:R =
  196.95, above the 192.32 range high. To the range high: R:R = 8.67/6.65 = **1.30**. Fail.
- The existing pending BUY @ 184.00 stands; I am not upgrading it to a fresh recommendation.

## [06:37 ET] THE SHAPE OF TODAY, and why the report is thin
- The leaders (XLP, XLV, HD, LOW) are 1-4% off their highs with elevated ATRs, so an honest
  2.0-ATR stop leaves no room for a 2:1 target inside the known range. They fail the floor.
- The laggards (BCC, LEN, CVS, ADM, HUN, CAG) have no insider cluster behind them - one
  buyer each at most, and CVS has 352.7M of insider SELLING.
- DKS is the one name that is both de-rated AND has seven insiders buying. That is why it is
  the only new idea captured rather than one of six.
- Both weekend lanes are closed by data gaps today: event contracts return count:0, and
  crypto has no fetchable OHLC history (no crypto history subcommand; yahoo 429 blocks
  BTC-USD), so no crypto futures stop can be validated against a 2.5-ATR floor.
  I am NOT inventing an ATR to publish a /MBT or /MET idea.

## [06:40 ET] ENR — the best thing I found that is NOT a recommendation, and why
- Screen hit: 41 open-market buys, 2 distinct buyers, 19,284,501 USD, **zero sells**, and
  earnings 2026-11-17 bmo (fetched calendar). On the raw numbers this looked better than DKS.
- **It is not an officer cluster.** Every purchase I could read is "Aqua Capital, Ltd." -
  a fund, buying 20,000-share blocks at 20.29-21.09 on 2026-07-23/24. That is a 13D-style
  accumulation by one institution, not independent judgements by people who run the company.
  `distinct_buyers: 2` read naively would have put a fund's position on the page as insider
  conviction. Same trap as LEN's single 329M buyer.
- Levels: 24.13 last, ATR14 0.9529 (3.95%), SMA20 23.527, SMA50 22.2588, range 17.80-25.83,
  -6.58% off high but **+35.56% off the low**. Market cap 1.65B, 68.48M shares,
  30d avg dollar volume 23.4M (clears the 500K floor comfortably).
- Why it fails the floor, honestly, at every entry I tried:
  - entry 23.53 (SMA20), 2.0-ATR stop = 1.91 -> 21.62: target for 2:1 = 27.35, which is 6%
    ABOVE the 25.83 range high. To the range high instead: R:R = 2.30/1.91 = **1.21**. Fail.
  - entry 22.26 (SMA50), stop 20.35 (inside Aqua's accumulation zone - a real level):
    to the range high R:R = 3.57/1.91 = **1.87**. Still short of 2.0, and 22.26 is 7.7%
    below spot with earnings in two days, so it almost certainly will not fill first.
  - The only way to 2:1 is a target above the 120-day high, and I have no valuation anchor
    to defend a re-rating. So I am not publishing one.
- verdict: **REJECTED as a recommendation; it is the strongest WATCHLIST name of the run.**
  Condition to revisit: a post-earnings pullback into 22.26-23.53 that holds the SMA50,
  which would put a 2.0-ATR stop under Aqua's 20.29-21.09 cost basis.

## [06:41 ET] VERIFICATION — why DKS's cluster is real where ENR's and LEN's are not
- I checked the buyer NAMES rather than trusting the distinct_buyers count:
  - DKS: Gupta Navdeep, Barnes Matthew, Fitzgerald Larry Jr., Colombo William J and others -
    seven natural persons, i.e. officers and directors forming independent views.
  - ENR: "Aqua Capital, Ltd." - one fund, 41 times.
  - LEN: one filer, 24 times, 329M - almost certainly an affiliate or 10% holder.
- This is the check that separates the one idea worth publishing from two that screened
  better on the raw count. It is worth making a standing habit.

## [06:23 ET] (clock correction: my earlier ET stamps in this log ran ~20 min fast; real
## elapsed at this point is 23 minutes, not 43. Times from here are accurate.)

## [06:23 ET] DKS — RELATIVE STRENGTH, the material negative I had not checked
- source: market_data.py relstrength DKS --peer XRT (computed from fetched history)
| window | DKS | XRT (retail) | SPY | DKS vs SPY |
| --- | --- | --- | --- | --- |
| 1m | **+6.29%** | +3.68% | -2.26% | **+8.55%** |
| 3m | -23.72% | +4.01% | -2.37% | -21.35% |
| 6m | **-30.85%** | **+15.12%** | +2.06% | **-32.91%** |
- This is the single most important thing I learned about DKS and it cuts both ways:
  - AGAINST: a 46-point gap to its OWN sector over 6 months (-30.85 vs +15.12) means this is
    a COMPANY-specific problem, not a cheap sector. strategy.md warns precisely about
    "catching something falling relative to everything around it", and that is what the
    3m and 6m columns describe. The two consecutive EPS misses are that problem.
  - FOR: the 1-month column has turned - DKS +6.29% now BEATS both XRT (+3.68%) and SPY
    (-2.26%). The relative bleeding stopped, and it stopped around when the seven insiders
    were buying at 129.75-136.39. That is the coherent read: insiders marked the low.
- Net: the idea survives but it is a bet on a company-specific turn against a 6-month
  relative downtrend, eight days ahead of a print that has missed twice. Keeping conviction
  at 4 and size at 2%; re-capturing DKS so the counter-argument carries this properly
  instead of leaving it in the notes where the reader never sees it.
- DATA GAP: `short DKS` failed (nasdaq api ReadTimeout), so short interest and days-to-cover
  are UNKNOWN for this idea. I am not guessing at a squeeze component.
- Filings seen: Form 4s dated 2026-10-01, 10-06, 10-29 (further insider activity after the
  September cluster) and 13G/A amendments 2026-11-05 and 2026-11-13 (institutional position
  changes). Budget did not allow reading each; the September cluster is already confirmed
  by named natural persons.

## [06:32 ET] MACRO — rebuilt from individual quotes after `macro` failed twice
- `market_data.py macro` timed out at 120s AND again at 300s with zero output. Dead for this
  run. The following are finnhub quotes, all as of 2026-11-13T21:00:00Z (Friday close):
| instrument | last | Friday chg |
| --- | --- | --- |
| SPY | 754.37 | -0.36% |
| QQQ | 679.89 | **-1.20%** |
| IWM | 277.54 | -0.32% |
| VIXY (vol proxy) | 17.94 | **+2.46%** |
| UUP (dollar) | 29.50 | +0.27% |
| IEF (7-10y UST) | 90.04 | -0.19% |
| TLT (20y+ UST) | 79.38 | -0.43% |
| GLD | 355.45 | +0.16% (but -17.23% off its high) |
| USO (oil) | 145.58 | -0.34% |
| XLE | 64.96 | +0.98% |
- COHERENT READ - rising real yields: the dollar firm, BOTH Treasury tenors down (IEF and
  TLT), gold 17% off its high, and the long end below its MAs. That one driver explains
  nearly everything else observed today: defensives (XLP/XLV) leading because they are
  bond-proxy-adjacent *earnings* rather than duration; gold falling as real yields rise;
  and the growth complex de-rating - QQQ -1.20% was more than triple SPY's -0.36%.
- Volatility was BID into the weekend (VIXY +2.46%) with the index only -0.36%. That is
  someone paying up for protection ahead of NVDA Tuesday, not a calm tape.
- NOT verified this run, and I am not asserting them: the actual 10y/2y yield levels, the
  VIX index itself, DXY, and every FRED series. The `macro` subcommand carries those and it
  never returned. VIXY and UUP are ETF *proxies* I did fetch - do not read them as the index.

## [06:33 ET] DATA GAP CONFIRMED — event contracts dead across 8 topics
- count:0 for: Fed, CPI, bitcoin, inflation, recession, "Bitcoin price", "S&P", election, GDP.
  The Kalshi source answers ok:true every time and lists nothing. On a WEEKEND run this is
  the costly gap, because strategy.md's weekend rule leans on exactly this lane.
- Combined with no crypto OHLC history, BOTH 24/7 lanes are unavailable today. That is why
  a Sunday report is carrying equity week-ahead prep instead: not a choice, a data outage.

## [06:34 ET] REJECTED — XLE and XLF — and this is now a SYSTEMATIC finding, not four misses
- XLE 64.96, ATR 1.7101, SMA20 66.1685, SMA50 64.9858, range 52.62-70.151, -7.4% off high.
  Rising six sessions straight (61.62 -> 64.96) but still BELOW its SMA20, so an SMA20 entry
  would be a breakout not a pullback. Tested both ways:
    entry 66.17 / 1.8-ATR stop 63.09 / risk 3.08 -> target for 2:1 = 72.32, above the 70.151
    range high. R:R to the range high = **1.29**. Fail.
    entry 64.99 (SMA50, ~spot) / stop 61.91 / risk 3.08 -> needs 71.15, still above. R:R 1.68. Fail.
- XLF 58.68, ATR 1.0112, SMA20 57.063, SMA50 55.9666, range 50.52-60.04, only -2.27% off high.
    entry 57.06 / stop 55.24 / risk 1.82 -> target for 2:1 = 60.70, above the 60.04 range
    high. R:R to the range high = **1.64**. Fail.
- **The pattern across XLP, XLV, XLE and XLF is identical**: every leading group is 1-7% from
  its 120-day high with an ATR wide enough that an honest 1.8-ATR stop makes a 2:1 target
  land ABOVE the range high. To publish any of them I would have to either tighten the stop
  (the KRE error) or assert a breakout to new highs I have no evidence for.
- That is a real description of this tape, and it is the reason today's report is thin
  rather than long: the strong things are extended and the cheap things have no insider
  support. Four independent floor tests failing the same way is a market condition.

## [06:35 ET] POSITION UPDATE — OXY — opened 2026-09-24, entry 54.00, now 58.75, +8.8%
- decision: HOLD, levels UNCHANGED (stop 50.15, target 62.00), but flag it - this is the
  deteriorating winner on the book and second in the close-first queue after AAL.
- Levels: ATR14 1.842 (3.14%), SMA20 60.4975, SMA50 59.7588, range 47.77-64.955, -9.55% off high.
- The flag: at 58.75 OXY is BELOW BOTH its SMA20 (60.50) and SMA50 (59.76) despite being
  +8.8% on paper. A position in profit that has lost both moving averages is the shape a
  winner has just before it becomes a loser, and it is easy to miss precisely because the
  P/L is still green.
- Inconsistent with its own sector, which is the tell: XLE rose six sessions straight into
  Friday (+0.98% on the day, 61.62 -> 64.96) while OXY sat below both MAs. OXY is lagging a
  rising sector.
- Levels stay because they are sound, not from inertia: risk 3.85 from entry = **2.09 ATR**
  (clears the 2.0 floor) and entry-measured R:R = 8.00/3.85 = **2.08** (clears). Tightening
  the 50.15 stop to "protect" the gain would both break the ATR floor and inflate the ratio -
  the exact mistake I caught myself making on ACM earlier in this run.

## [06:37 ET] SELF-VALIDATION of all 7 captured ideas (recomputed from fetched ATRs)
| sym | R:R | stop in ATR | floor | verdict | wp | baseline | edge | expectancy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ACM | 2.00 | 2.41 | 2.0 | PASS | 0.45 | 0.333 | +11.7pt | +1.83 |
| DKS | 2.00 | 2.58 | 2.0 | PASS | 0.42 | 0.333 | +8.7pt | +4.03 |
| OXY | 2.08 | 2.09 | 2.0 | PASS | 0.40 | 0.325 | +7.5pt | +0.89 |
| TLT | 2.67 | 1.97 | 1.8 (etf) | PASS | 0.40 | 0.273 | +12.7pt | +0.70 |
| AAL | 2.62 | 1.71 | 2.0 | **FAIL** | 0.36 | 0.276 | +8.4pt | +0.32 |
| HII | n/a | n/a | 2.0 | **artifact** | 0.55 | see below | | |
| BCC | n/a - an exit, no target or stop by construction | | | | | | | |
- Every expectancy is positive and no claimed edge exceeds 20 points except HII's artifact.
- **AAL's FAIL is real and left standing on purpose.** The 14.40 stop is 1.71 ATR from the
  13.35 entry, inside the 2.0 floor. It is inherited from an entry made on 2026-10-03 and
  the only ways to "fix" it are to widen the stop (which is what CLAUDE.md calls the KRE
  error) or to close the position. I am recommending neither on arithmetic grounds alone,
  so validation SHOULD flag it and the red team is right to demote it. Disclosed, not hidden.
- **HII is an arithmetic artifact, not edge, and I am restating it precisely.** The amended
  stop (278.50) sits ABOVE the entry (262.00), so "risk" measured from entry is negative:
  if the stop holds the position cannot lose from its fill. Any ratio computed from entry
  is therefore meaningless, which is why `risk_reward` is published as null.
  Measured from Friday's actual 306.24, which is the only honest frame for a position being
  managed: 33.52 to target vs 27.74 to stop = **1.21:1**, baseline 1/(1+1.21) = **0.452**,
  so a 0.55 win probability is a ~10-point edge, not the 37.5 points an entry-measured
  computation would wrongly imply. Re-capturing with that spelled out.

## [06:39 ET] RESEARCH COMPLETE
- candidates: **10 rows / 7 unique symbols** (ACM, BCC, DKS, TLT, AAL, HII, OXY).
  ACM, DKS and HII each appear twice; the later row supersedes and corrects the earlier one,
  and synthesis takes the last entry per symbol.
- RESEARCH WAS NOT TRUNCATED. Started 11:00 UTC / 06:00 ET, finished this block at ~06:39 ET
  of a ~60 minute budget, with room to spare. Every section below is a reached conclusion,
  not an abandoned one.

### What this run actually is
Only ONE of the seven is a new idea (**DKS**). The other six are decisions on money already
at risk, which is the obligation prior_context puts first. All 14 open positions were
reviewed and given an explicit decision:
- **CLOSE: BCC** (-16.8%, no stop, 0.81% off its 120-day low after a post-10-Q eight-session
  slide, zero insider buying against 666K of selling).
- **ACT: HII** (set a 278.50 stop on the book's largest unprotected gain, +16.9% for 32 days
  with no stop at all).
- **ACT: ACM** (trim half into tomorrow's 2026-11-16 after-close print; stop stays 61.50).
- **FLAGGED HOLDS: OXY** (green but below both MAs while its sector rallies - close second),
  **AAL** (short working, but price above both MAs and its stop is inside the ATR floor -
  close first), **TLT** (0.76 ATR from its stop; hold the line, explicitly do not widen it).
- **UNCHANGED HOLDS, no candidate needed:** KHC, UNP, ABT, PYPL, RTX, XLU (all above both
  MAs with stops below both), PFE (held, but I declined to republish its undefended +45%
  target), ONON (above SMA50, at the floor).
- **CANCEL four dead pending orders:** GLD SELL @406.77, /MBTZ6 SHORT @74075, CVS BUY @79.00,
  and the stale KXCPIYOY-26SEP-T3.5 NO @18 September CPI contract.

### Coverage gaps
- **Event contracts: total outage.** count:0 on all 9 topics tried. On a weekend run this is
  the expensive gap, since strategy.md leans this lane for Sat/Sun actionability.
- **Crypto: no OHLC history obtainable.** No `crypto history` subcommand exists and yahoo
  429'd BTC-USD all run, so no ATR -> no validatable 2.5-ATR stop. I fetched BTC 65,527
  / ETH 1,829.42 / SOL 72.08 spot but published no crypto idea rather than invent an ATR.
- **`macro` subcommand dead** (timed out at 120s and again at 300s, no output). Rebuilt what
  I could from individual quotes; actual 10y/2y yields, the VIX index, DXY and all FRED
  series are UNVERIFIED and are not asserted anywhere.
- **Options-implied moves unavailable** (yahoo-options 401 all run), so no target was checked
  against a straddle-priced move - including DKS's.
- **Short interest unavailable for DKS** (nasdaq api ReadTimeout); no squeeze claim made.
- Did not reach: micro caps as a deliberate lane, FDA calendars, index rebalances, unlocks.

### Sources that failed
yahoo (429 on all history), yahoo-options (401), stooq (connect timeout), nasdaq api for
short interest (ReadTimeout), market_data.py macro (timeout x2), Kalshi events (ok but empty).
Worked: finnhub (quotes, earnings, insiders, analysts, profile), nasdaq (equity history),
SEC (filings), CoinGecko (crypto spot).

### Honest notes for synthesis
- **The report is thin on purpose and the reason is specific.** Four independent floor tests
  (XLP, XLV, XLE, XLF) failed the SAME way: every leading group sits 1-7% off its 120-day
  high with an ATR wide enough that an honest 1.8-ATR stop pushes a 2:1 target above the
  range high. Meanwhile the de-rated names have no insider support. That is a market
  condition worth stating, not a shortfall to apologise for.
- **~24 names were insider-screened and DKS was the only genuine officer cluster.** Two
  names that screened better on raw counts were disqualified by reading the buyer NAMES:
  ENR's 41 buys / 19.3M are all "Aqua Capital, Ltd." (a fund) and LEN's 24 buys / 329M are
  one filer. DKS's seven are natural persons. Recommend making that check standing practice.
- **Two ideas knowingly carry defects, both disclosed in their own key_risk:** AAL's stop is
  1.71 ATR (inside the 2.0 floor, inherited from October, not widened on principle), and
  HII's entry-measured R:R is an artifact of a stop above its entry (published as null;
  from spot it is 1.21:1 against a 0.452 baseline).
- **I corrected my own error mid-run.** I first proposed tightening ACM's stop to 64.50 as
  prudence; it would have sat 1.03 ATR from entry, breaking a floor the original 61.50 stop
  already cleared at 2.41 ATR, and would have lifted R:R 2.00 -> 4.68 purely by moving the
  stop. Superseded. On a position in profit, "raise the stop" is not automatically conservative.
- Equities are closed: every equity level here is for the **next open, Monday 2026-11-16**,
  and all prices are the Friday 2026-11-13 close (age ~2285 min, session "closed" - a closed
  market, not stale data).
- Correlation note: DKS is consumer/retail; the week's dense retail calendar (TGT, LOW, HD,
  WMT, TJX, ROST Nov 18-19) plus NVDA Nov 17 means one consumer print could move it on
  sympathy. It is the only new consumer exposure added, deliberately.
- Track-record caution: long_term is 0/4 and conviction-2 is 0/6, but both samples are far
  under the ~15-trade threshold, so they are noise and I did not over-fit to them. I
  published no long_term idea today and no conviction-2 idea - not because of the record,
  but because no long_term valuation anchor was defensible inside this budget and nothing
  thin enough to be a 2 was worth the row.

## [06:42 ET] SIRI — Berkshire is accumulating; publishable ONLY at a much lower entry
- Wider screen (PHM, DHI, TOL, MOS, CF, WBA, DG, DLTR, SWKS, QRVO, WBD, SIRI): every one
  zero buys except SIRI. DLTR 14 sells, QRVO 30, WBD 19 - heavy distribution in those.
- SIRI insiders: 3 open-market buys, 1 distinct buyer, 26,894,245 USD, 2 small sells (739,913).
  The buyer is **BERKSHIRE HATHAWAY INC**, and the purchases are RECENT and INTO strength:
    2026-10-30  743,965 sh @ 28.8913
    2026-11-02   66,968 sh @ 29.4660
    2026-11-03  113,348 sh @ 30.2330
  ~924k shares, average around 29.1, buying up rather than averaging down.
- Characterise it correctly: this is a >10% holder filing Form 4s, i.e. ONE institution, not
  the seven-officer cluster DKS has. It is a strong signal of a different type and must not
  be dressed up as "insiders are buying".
- Levels: 31.85 last, ATR14 1.0516 (3.30%), SMA20 29.7973, SMA50 28.1949,
  range 25.305-33.76, -5.66% off high, 30d avg dollar volume 148.7M. Market cap 10.72B.
- Floor tests at 2.0 ATR (= 2.10 risk), target = the real 33.76 range high:
  - entry at spot 31.85 -> R:R **0.91**. FAIL badly. Do not chase.
  - entry at SMA20 29.80 -> R:R **1.88**. FAIL, and it misses by only 0.12 - which is exactly
    the margin CLAUDE.md says gets "nudged until it passes". I am not nudging it.
  - entry at SMA50 28.19, stop 26.09 -> R:R **2.65**. PASS, on entirely fetched levels.
- So SIRI publishes at 28.19 and nowhere higher. Honest weakness, stated in the idea: that
  entry is 11.5% BELOW spot and below Berkshire's own lowest fill (28.89), so the fill
  probability is low - this is the extreme form of the pullback-entry problem (the first
  month ran 31 pullback entries at a 42% fill rate). Its value is as much "do not pay up for
  this" as "buy it here".

## [06:43 ET] REJECTED — the rest of the wide screen
- PHM 0 buys/1 sell, DHI 0/0, TOL 0/3, MOS 0/1, CF 0/0, WBA 0/0, DG 0/1, DLTR 0/14,
  SWKS 0/0, QRVO 0/30, WBD 0/19. No officer cluster anywhere.
- Running total: **~36 names insider-screened this run, exactly one officer cluster (DKS).**

## [06:46 ET] CORRECTION — SIRI stop 26.09 -> 26.08 (my rounding broke the floor)
- I computed the 2.0-ATR stop as 28.19 - 2.0(1.0516) = 26.0868 and wrote it as **26.09**.
  Rounding the stop UP moved it closer to the entry: 2.10/1.0516 = **1.9970 ATR**, i.e.
  fractionally INSIDE the 2.0 floor. Tiny, but it is a fail, and a marginal pass created by
  rounding in the favourable direction is precisely the 2.04-2.33 cluster problem.
- Fixed to **26.08** -> 2.0065 ATR (passes), risk 2.11, R:R 2.6398, baseline 0.2747,
  win_probability 0.38 = a 10.5-point edge, expectancy +0.81. Re-captured.
- Rule for next time: round a stop AWAY from the entry, never toward it.

## [06:48 ET] RESEARCH COMPLETE (FINAL — supersedes the 06:39 block, which said 7 symbols)
- candidates: **12 rows / 8 unique symbols** — ACM, BCC, DKS, TLT, AAL, HII, OXY, **SIRI**.
  ACM, DKS, HII and SIRI each appear more than once; the LAST row per symbol is the correct
  one and synthesis takes it. The earlier rows are superseded corrections, not alternatives.
- RESEARCH WAS NOT TRUNCATED. Ran 11:00–11:36 UTC (06:00–06:36 ET) of a ~60 minute budget
  and finished with time in hand. Nothing below was abandoned for want of clock.
- SIRI was added after the first completion block: Berkshire Hathaway accumulating, which
  the wider insider screen turned up late. Its stop was then corrected 26.09 -> 26.08
  because my own rounding had left it at 1.997 ATR, fractionally inside the 2.0 floor.

### Final self-validation (all recomputed from fetched ATRs)
| sym | dir | conv | kinds | R:R | stop ATR / floor | edge vs baseline | expectancy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DKS | buy | 4 | 4 | 2.00 | 2.58 / 2.0 ok | +8.7pt | +4.03 |
| SIRI | buy | 3 | 3 | 2.64 | 2.01 / 2.0 ok | +10.5pt | +0.81 |
| ACM | buy | 3 | 3 | 2.00 | 2.41 / 2.0 ok | +11.7pt | +1.83 |
| OXY | buy | 3 | 3 | 2.08 | 2.09 / 2.0 ok | +7.5pt | +0.89 |
| TLT | buy | 3 | 2 | 2.67 | 1.97 / 1.8 ok | +12.7pt | +0.70 |
| AAL | sell_short | 3 | 3 | 2.62 | **1.71 / 2.0 FAIL** | +8.4pt | +0.32 |
| HII | buy | 3 | 2 | n/a (artifact) | n/a | see note | — |
| BCC | sell | 4 | 4 | n/a — an exit | — | — | — |
- Six of eight clear every floor. The two that do not are disclosed in their own `key_risk`
  and both are legacy positions, not new risk: AAL's stop is 1.71 ATR (inherited 2026-10-03;
  widening it would be the KRE error, so validation SHOULD flag it), and HII's stop sits
  ABOVE its entry so any entry-measured ratio is meaningless — published as `risk_reward:
  null`; from spot it is 1.21:1 against a 0.452 baseline, a ~10pt edge, not 37.
- Every conviction score is at or BELOW what its evidence count supports. None is inflated.

### Three things worth carrying into the next run
1. **Read the buyer NAMES, never the `distinct_buyers` count.** ~36 names screened, three
   looked like clusters, and only DKS was one: ENR's 41 buys are all "Aqua Capital, Ltd.",
   LEN's 24 are one filer, SIRI's three are Berkshire. All real signals — none is officers.
2. **"Raise the stop" is not automatically conservative.** I nearly shipped ACM with a stop
   1.03 ATR from entry in the name of protecting a gain, which would have broken a floor the
   original 61.50 already cleared and inflated R:R 2.00 -> 4.68 by moving the line.
3. **Round stops away from the entry.** SIRI's 26.09 was a floor failure created purely by
   rounding in the favourable direction.
