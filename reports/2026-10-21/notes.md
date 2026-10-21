# Research log — 2026-10-21

## [06:02 ET] MACRO — rates, crypto, data sources
- US 10y 5.15% (2026-10-19), prev 5.09 — long end still selling off; 2y 4.77 (prev 4.74) — source: FRED DGS10/DGS2
- 10y-2y +0.33 (2026-10-20) vs +0.38 prior — source: FRED T10Y2Y
- Fed funds effective 3.88% (2026-10-19) — source: FRED DFF
- Unemployment 4.2% (Sep 2026), prev 4.1% — source: FRED UNRATE
- CPI index 336.298 (Sep 2026) vs 334.131 (Aug) = +0.65% MoM — hot print — source: FRED CPIAUCSL
- BTC $83,345 (+2.36% 24h), ETH $2,454.03 (+3.02%), SOL $106.57 (+2.52%) — source: CoinGecko via market_data.py macro
- TLT last close 80.13 (+0.84%), as of 2026-10-20 20:00 UTC (prev close, market closed) — source: market_data.py macro bonds_20y
- DATA GAP: every index/VIX/DXY/gold/WTI quote failed. Yahoo returning HTTP 429; Finnhub refuses CFD indices; no AlphaVantage key. No SPX/VIX/DXY level available this run.

## [06:06 ET] CALENDAR — dated events inside 10 sessions (source: market_data.py earnings, Finnhub)
- 2026-10-21 bmo: ABT, ELV, T, TMO, PM, NEE, DHR, WAB | amc: META, TSLA, IBM, TXN, LRCX, BKR, URI, KMI, CSX, LVS, PKG
- 2026-10-22 bmo: **UNP**, PG, LMT, GD, HON, NSC, CMCSA, VLO, DOW, PCG, **AAL**, PHM, NVR, TSCO, BX | amc: NEM, WDC, OMC, FIX
- 2026-10-23 bmo: AXP, SLB, BAH
- 2026-10-26: VZ(bmo), NUE(amc), OKE, SCCO, WHR, CDNS, EA
- 2026-10-27 bmo: BA, UPS, KO, HCA, CNC, PYPL, **FCX**, SHW, GLW, SPGI, ITW | amc: V, WM, NXPI, STX
- 2026-10-29 bmo: **HII**
- 2026-11-02 amc: AAPL | **BCC**
- Positions with earnings inside the horizon: UNP (tmrw bmo), FCX (10/27), HII (10/29), BCC (11/02). Awaiting-entry with earnings: ABT (TODAY bmo), AAL (tmrw bmo).

## [06:07 ET] LEVELS — open-position price history (source: market_data.py history, nasdaq; all closes 2026-10-20, market closed)
| sym | last | ATR14 | ATR% | sma20 | sma50 | 90d high | 90d low |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GE | 299.87 | 7.35 | 2.45 | 311.52 | 327.93 | 388.84 | 294.22 |
| CEG | 258.84 | 16.30 | 6.30 | 273.63 | 275.32 | 309.80 | 228.63 |
| SNX | 248.21 | 9.82 | 3.96 | 265.59 | 261.53 | 298.77 | 234.03 |
| SMMT | 16.09 | 0.95 | 5.93 | 16.37 | 15.74 | 19.09 | 12.07 |
| IYR | 98.00 | 1.40 | 1.43 | 95.98 | 99.78 | 108.17 | 93.29 |
| UNP | 287.61 | 4.14 | 1.44 | 279.10 | 287.54 | 315.99 | 255.22 |
| XLE | 67.97 | 1.38 | 2.03 | 64.50 | 63.90 | 68.51 | 52.62 |
| DG | 134.19 | 3.72 | 2.77 | 125.29 | 124.79 | 137.08 | 107.91 |
- GE fell -3.67% on 10/20 to 299.87, 1.9% off its 90d low, below both MAs — the only broad-market decliner of the book on an up day. Needs a reason, see NEWS.
- CEG five consecutive lower closes 279.54 -> 258.84; stop 250.0 is now 0.54 ATR away.
- XLE 0.79% off its 90d high and 2.5 ATR above sma20 — the book's one clean winner.

## [06:05 ET] NEWS — defense tape
- NOC +4.57% on 10/20 to 534.00. 8-K filed 2026-10-20 (primary doc): Q3 sales +7% / +$699M, all four sectors up, Aeronautics Systems +14%, Defense Systems +12%, offset by $95M higher intercompany eliminations. Operating income +2%/+$27M on $68M higher segment operating income less a $52M FAS/CAS decrease; operating margin 11.4% vs 11.9% — source: https://www.sec.gov/Archives/edgar/data/0001133421/000113342126000037/noc-09302026xearningsrelea.htm
- July 2026 guide raise (pre-Q3): FY sales $43.75-44.25B (+$250M), adj EPS $28.60-29.10 — source: as above
- Read-through: LMT and GD both report 2026-10-22 bmo. LMT 548.71 (ATR 11.48, sma20 518.58, sma50 541.27, -10.45% off 90d high). GD 344.44 (ATR 5.83, sma20 334.90, sma50 357.06, -13.89% off high). HII 272.23 (ATR 7.06, sma20 265.73, sma50 283.15), reports 10/29.
- GE filed 10-Q and 8-K on 2026-10-20 — Q3 confirmed; the 8-K is a cover page only, figures are in Exhibit 99. Stock -3.67% to 299.87 on the day. Source: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000040545

## [06:05 ET] UNP — POSITION UPDATE captured (conviction 3)
- decision: hold through tomorrow's bmo print, levels unchanged (entry 288.6 / target 315.99 / stop 277.4)
- why: earnings 10/22 bmo confirmed on the fetched calendar (est EPS 3.5061, rev $7.193B); STB has had the $85B NSC application since the May 2026 completeness acceptance
- caveat logged: stop 277.4 = 2.70 ATR, clears the 2.0 swing floor; target 315.99 is the 90d high and 6.6 ATR away

## [06:05 ET] SCHEMA NOTE — trailing stops cannot be expressed
- `check_stop_distance` measures `abs(entry.ideal - stop) / ATR` from the ORIGINAL entry, so raising a stop toward entry on a winner fails the ATR floor and `--enforce` would demote the idea to the watchlist. XLE (+6.1%, entry 63.9, stop 60.8) therefore stays at its published stop rather than being trailed to the 20-day at 64.50, which would read as 0.65 ATR. Recorded as a limitation, not as a view that the stop should not move.

## [06:08 ET] LEVELS — remaining book and the awaiting-entry list (source: market_data.py history/quote; all 2026-10-20 closes)
| sym | last | ATR14 | ATR% | sma20 | sma50 | 90d hi | 90d lo | off hi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BCC | 76.28 | 2.06 | 2.69 | 75.14 | 77.45 | 88.43 | 70.13 | -13.7% |
| PFE | 30.11 | 0.60 | 1.98 | 28.54 | 28.08 | 30.25 | 23.62 | -0.5% |
| LULU | 99.94 | 3.09 | 3.10 | 96.60 | 105.57 | 128.86 | 90.38 | -22.4% |
| NKE | 37.88 | 1.23 | 3.24 | 35.61 | 37.37 | 46.31 | 31.97 | -18.2% |
| KHC | 23.83 | 0.56 | 2.35 | 22.89 | 24.17 | 28.09 | 21.76 | -15.2% |
| TLT | 80.13 | 0.85 | 1.06 | 78.57 | 80.63 | 87.79 | 76.43 | -8.7% |
| FCX | 68.87 | 2.49 | 3.61 | 71.32 | 72.01 | 80.24 | 56.00 | -14.2% |
| XLF | 55.72 | 0.70 | 1.26 | 54.45 | 56.18 | 58.60 | 52.81 | -4.9% |
| STLD | 244.37 | 7.48 | 3.06 | 235.73 | 238.56 | 288.74 | 216.36 | -15.4% |
| ABT | 102.45 | 2.55 | 2.49 | 100.97 | 105.67 | 117.34 | 87.07 | -12.7% |
| AAL | 12.11 | 0.49 | 4.01 | 12.81 | 13.28 | 18.79 | 11.63 | -35.6% |
| ITB | 87.32 | 2.34 | 2.68 | 86.50 | 90.98 | 106.38 | 82.08 | -17.9% |
| OXY | 62.92 | 1.59 | 2.53 | 59.13 | 59.54 | 63.77 | 47.77 | -1.3% |
| GLD | 377.65 | 4.92 | 1.30 | 382.26 | 396.31 | 429.42 | 363.32 | -12.1% |
| VST | 150.32 | 9.14 | 6.08 | 148.98 | 145.21 | 171.35 | 133.44 | -12.3% |

## [06:08 ET] STOP-FLOOR RECHECK at today's ATR — three published stops no longer clear the floor
Measured as `|entry - stop| / ATR14`, the way `check_stop_distance` does it:
- CEG 1.35 ATR (floor 2.0) — volatility expanded to 6.3%; cannot be fixed, see the CEG exit case
- SNX 1.78 ATR (floor 2.0) — (260.0-242.5)/9.82
- FCX 1.95 ATR (floor 2.0) — (68.2-63.35)/2.49; widening the stop 15c to 63.20 restores 2.00 ATR and leaves R:R 2.06, so this one is a re-mark to current volatility rather than a broken idea
Everything else clears: IYR 1.86 (ETF floor 1.8), TLT 2.47, XLF 2.04, DG 2.39, STLD 2.24, UNP 2.70, GE 2.18, SMMT 2.83, KHC 3.21, XLE 5.19.

## [06:09 ET] AWAITING-ENTRY TRIAGE — three of seven levels are now stale, not merely unfilled
- `OXY` BUY @ 54.0 (2026-09-24): OXY is 62.92, 1.3% off its 90-day high and 5.7% above its own 50-day. A limit 14.2% under the market is not a pullback level any more, it is a level the thesis has outrun. WITHDRAW rather than chase.
- `GLD` SELL @ 406.77 (2026-09-08): gold already fell to 377.65, 12.1% off the 429.42 high and below both MAs. The call was right and never filled; the level is 7.7% above the market and selling here is selling after the move. WITHDRAW.
- `AAL` SELL_SHORT @ 13.35 (2026-10-03): AAL is 12.11, -35.6% off its high, below both MAs, and reports tomorrow bmo (est EPS -0.3639). A 10.2% above-market short limit will not fill, and initiating a short in a $12 airline the day before its own print is not a trade this report should carry. WITHDRAW.
- `VST` BUY @ 132.0 (2026-08-24): VST is 150.32 — 13.9% above the limit, and the same rate-sensitivity that is taking CEG apart applies. Leave unfilled, do not reprice up.
- `ITB` SELL_SHORT @ 89.8 (2026-09-30): still live and 2.8% above the market, and it now has a dated catalyst — PHM and NVR both report 2026-10-22 bmo — with the 10-year at 5.15% and rising. RE-PITCH with the level unchanged. See below.
- `ABT` BUY @ 103.0 (2026-10-16): earnings are TODAY bmo, so the published instruction ("enter only if the band fills before the print") has run out of time. See the ABT update.
- `KXCPIYOY-26SEP-T3.5` NO @ 18 (2026-09-30): September CPI is already published (index 336.298), so this contract is at or past resolution. Not re-pitched; see EVENT CONTRACTS.

## [06:11 ET] EVENT CONTRACTS — nothing found, and this is a source gap not a judgement
- `market_data.py events` returned 0 markets for FOMC, CPI, "interest rate", recession and inflation. A query for "Fed" returned 3 markets, all of them tennis listings matched on the substring (Federica, Feng), with every price field null.
- So there is no fetched implied probability to disagree with today and no event-contract candidate is captured. Not "none were attractive" — the Kalshi query surfaced no macro market at all. Recorded for `data_quality_notes`.
- The awaiting-entry `KXCPIYOY-26SEP-T3.5` NO @ 18 is moot regardless: September CPI is published (CPIAUCSL 336.298, 2026-09-01), so the contract is at or past resolution.

## [06:11 ET] TARGET-FEASIBILITY RECHECK (swing guide is 6.0 ATR, `ATR_LIMIT`)
- UNP target 315.99 is 6.61 ATR from the 288.6 entry — over the guide, expect a WARN. Kept because it is the 90-day high rather than an invented number, and because the position is already open at that target; it is flagged here rather than quietly trimmed to pass.
- ITB published target 81.50 is 3.55 ATR, target_2 78.00 is 5.04 ATR — both inside the guide.
- GE 4.49 ATR, XLE 4.78 ATR, STLD 4.75 ATR, DG 5.51 ATR — all inside.

## [06:22 ET] PROGRESS — 19 candidates captured; all 19 open positions plus ABT addressed
Decisions taken: HOLD unchanged — XLE, IYR, TLT, XLF, DG, STLD, UNP, GE, KHC, SMMT, LULU, NKE, HII, PFE, BCC.
AMENDED — FCX stop 63.35 -> 63.20 (re-mark to a 2.49 ATR, restoring the 2.00 ATR floor).
CLOSE EARLY — CEG and SNX, both because the published stop no longer clears the ATR floor at today's volatility and neither can be re-cut to clear both floors at once.
CONVICTION LOWERED — SMMT 5 -> 4, BCC 4 -> 3, KHC 3 -> 2, DG 3 -> 2, SNX 4 -> 2, XLE 4 -> 3. Each is a count of distinct evidence kinds actually verified this run, not a change of view.
WAIT — ABT, where the published "enter before the print" instruction has expired because the print is this morning.
WITHDRAWN from awaiting-entry — OXY, GLD, AAL (levels outrun by 14.2%, 7.7% and 10.2% respectively); VST left unfilled.

## [06:22 ET] REJECTED — ITB SELL_SHORT — cannot clear both floors at today's ATR
The idea is good and the catalyst is real: PHM and NVR both report 2026-10-22 bmo, FOMC is 2026-10-28, the ten-year is 5.15% and rising, ITB sits below its 96.59 two-hundred-day having lost 22.05% to SPY over six months. But the arithmetic refuses it. ATR14 is 2.34, so the published 93.60 stop is 1.62 ATR from the 89.80 entry, under the 1.8 ATR floor for an ETF. Widening to 94.10 restores the floor and drops reward-to-risk against the 81.50 target to 1.93:1, under the 2.0 floor. The only pair that clears both uses the 78.00 target, which is 5% below the 82.08 two-hundred-fifty-day low — a number I would be choosing because it makes the ratio work, not because I can defend it. Per `config/strategy.md`: "If an idea needs a tight stop to clear the reward-to-risk floor, it has failed the floor." Passed to synthesis as a WATCHLIST entry, not a recommendation.

## [06:22 ET] DATA GAP — short interest unavailable
`market_data.py short` returned a read timeout from api.nasdaq.com for LULU, NKE and SMMT. No short-interest or days-to-cover figure is cited anywhere in today's candidates; the positioning evidence used is open-market insider purchases, analyst recommendation trend and measured relative strength instead.

## [06:22 ET] CORRELATION CHECK — the rate bet is at its cap
IYR short, TLT short and the CEG exit are three expressions of "long yields keep rising", which is the cap of 3 in `config/strategy.md`. That is why ITB was not added even before the arithmetic rejected it, and why BCC's counter_argument names the contradiction with its own long side rather than hiding it.

## [06:25 ET] REGIME — reconstructed from single names, because no index quote was available
Every index, VIX and dollar quote failed this run, so the regime below is inferred from the 90-day drawdowns of individual names rather than read off an index. Treat it as an inference, not a measurement.
- The AI and semiconductor-hardware complex has been taken apart over 90 days: GLW -51.3% off its 90-day high (271.78 -> 132.26), STX -41.0% (1145.00 -> 675.13), NXPI -27.5% (327.50 -> 237.60), GE -22.9%, CEG -16.5%, VST -12.3%, SNX -16.9%. Source: market_data.py history, each name.
- What is holding: XLE -0.8% off its high, PFE -0.5%, OXY -1.3%, DG -2.1%, XLF -4.9%, NUE -6.6%, SCCO -8.4%, PYPL -8.9%. Energy, staples, banks, steel, metals.
- And 2026-10-20 itself was a broad up day in those survivors — IYR +1.83%, KHC +2.85%, PFE +2.28%, CVS +2.23%, LULU +2.23%, NKE +1.80%, BCC +1.54%, XLF +1.20%, NOC +4.57% — while GE fell 3.67% on a beat-and-raise.
- Rates are the other half: 10y 5.15% and rising, 2y 4.77%, curve +0.33 and flattening, fed funds 3.88%, unemployment 4.2% up from 4.1%, September CPI +0.65% MoM.
- Read: a rotation out of long-duration AI capex into near-term cash flow, with the long end doing the discounting. That is the frame behind the CEG and SNX exits, the IYR and TLT shorts being held, and PYPL being the only new long.
- Crypto does not fit the frame: BTC $83,201 (+2.05% 24h), ETH $2,445.71 (+2.50%), SOL $106.01 (+1.95%), and IBIT as the dollar proxy is +42.2% off its 90-day low and only 5.4% off its high. Bitcoin is near a 90-day high while AI hardware halves. Noted and NOT traded — see the rejection below.

## [06:26 ET] REJECTED — GLW, STX, NXPI — real dislocations, wrong trade shape
All three report 2026-10-27 and all three are down 27-51% in 90 days, and the sell side is still positive and in GLW's case improving through the fall (GLW 2026-07: 6 strong buy / 9 buy / 6 hold, 2026-10: 7 / 10 / 5; STX unchanged at 7 / 19 / 4; NXPI drifting slightly worse). What is missing is the confirmation that matters most in a drawdown this size: ZERO open-market insider purchases in the fetched six-month window for all three. The people who know the order books are not buying. Combined with a GLW ATR of 6.27% and an STX ATR of 8.07% — a 2.0 ATR stop is 12.5% and 16.1% wide respectively — entering four sessions before the print would be a position whose stop is wider than the thesis. Rejected on shape, not on the dislocation being unreal.

## [06:26 ET] REJECTED — BTC / /MBT long — no verified contract and a thin thesis
IBIT is 5.4% off its 90-day high and 42.2% above its low, so the observation is a bullish one, and `config/universe.md` says to prefer the micro futures contract over spot. But two things are missing and neither is fixable in the time left: the specific /MBT contract month has not been verified against Robinhood's own futures list this run, and the only dated catalyst available is the 2026-10-28 FOMC, which is shared with two positions already on the book. One dated catalyst plus one technical level is a conviction 3 whose thesis would be "bitcoin is strong", and `config/strategy.md` is explicit that a moonshot with one real confirmation is not sturdier for being large. Not captured.

## [06:26 ET] REJECTED — NUE, SCCO — right theme, already owned
NUE 261.50 is 6.6% off its 90-day high and 21.9% off its low, above both moving averages, and reports 2026-10-26 amc. SCCO 202.34 is 8.4% off its high. Both are confirmations of positions the book already holds (STLD long, FCX long) rather than independent ideas, and adding either would put four ideas on one industrial-metals-and-steel driver against a correlation cap of 3. The NUE strength is cited as evidence inside the STLD update instead.

## [06:26 ET] DATA GAP — options-implied move unavailable
`market_data.py implied` returned HTTP 401 from the Yahoo options endpoint. No candidate in today's report cites an options-implied move, so no target was checked against what the straddle prices — including PYPL, which is held into its own print. Recorded for `data_quality_notes`.

## [06:30 ET] FALSIFICATION — ran `validate_report.py` against a throwaway copy of the candidates, before synthesis
A dry run on `/tmp/dryrun.json` (NOT `reports/2026-10-21/report.json`, which is synthesis's file) put every one of the 20 ideas captured at that point through the real validator. Four classes of problem came back; three are now fixed in `candidates.jsonl` and one is deliberately left standing.

**FIXED — every idea cited a dead URL.** `https://api.nasdaq.com/api/quote/<SYM>/historical` is the endpoint `market_data.py` calls with query parameters; a bare HEAD against it returns 404, so `check_sources` scored all twenty as citing an invented source. Replaced throughout with the human-facing `https://www.nasdaq.com/market-activity/{stocks|etf}/<sym>/historical`, which is the same provider's page for the same data and returns a bot-block rather than a 404. Worth remembering: a real API URL can still read as fabricated to a HEAD request.

**FIXED — GE's catalyst was dated in the past.** I stamped it 2026-10-20, the day the Q3 release landed, and `catalyst_date` failed it with "already passed — positioning around it is wrong", which is correct: there is nothing left to position around. The driver is now stated with a null date.

**FIXED — DG and KHC were sized above their own conviction.** Both were marked down to conviction 2 this run but left at 2% size, and `position_size` fails anything over the 1% lottery-ticket ceiling at that score. Both cut to 1%, which is a real instruction to trim an existing 2% position, not a bookkeeping change.

**LEFT STANDING — CEG and SNX fail `expectancy`, and that is the finding, not a defect.** CEG: 30% claimed against a 31% break-even at 2.18:1, expectancy -0.05R. SNX: 28% against 32% at 2.08:1, expectancy -0.14R. The validator's words are "the idea loses money at its own stated hit rate" — which is precisely why both are exit recommendations. Raising either probability to clear the floor would be inventing an edge in order to keep a position this report wants closed. Expect `--enforce` to demote both to the watchlist; the exit instruction must survive the demotion, because a reader who holds CEG and SNX needs it more than a reader who does not.

## [06:30 ET] PRE-MARKET SPREAD FLAGS ARE ARTIFACTS — do not kill positions on them
The dry run failed `spread` on four ideas using 6am bid/ask: BCC 119.02%, SNX 54.15%, STLD 10.65%, HII 6.27%. TLT came back "no bid/ask available (normal outside regular hours)". These are closed-market quotes with no two-sided market behind them — a 119% spread on a $76 stock is not a tradeable fact. Every entry in today's report is a limit order for exactly this reason. Flagging so the red team does not demote STLD, HII or BCC over a quote taken when nothing was trading. The underlying prices are all previous closes stamped 2026-10-20T20:00Z, which at 6am ET is the freshest honest equity price, not stale data.

## [06:30 ET] OTHER VALIDATOR NOTES, not acted on
- `earnings_date` warned "claims an earnings catalyst but <SYM> is not on the fetched calendar" for UNP, FCX, ABT, HII, BCC and PYPL — every one of which I confirmed against my own Finnhub calendar pull (1,459 symbols) before capturing. The validator's own pull returned 1,485 symbols and resolved DG correctly to 2026-12-02, so the two fetches disagree about which names they carry. The dates in the candidates are the ones I verified; the warning is a source discrepancy, not an unverified claim.
- UNP target 6.62 ATR, KHC 16.07, CVS 7.89, LULU 7.64 and SMMT 6.18 all exceed the 6.0 ATR swing guide. All are published-and-open positions whose targets are being left as published rather than trimmed to pass, with the trim levels in each `scale_plan` carrying the realistic part of the plan.
- `entry_vs_live` passed on everything, including PYPL, whose band straddles the last close deliberately.

## [06:33 ET] SMALL-CAP LANE — hunted, and it comes back empty, which is a result rather than an omission
`config/universe.md` asks for small and micro caps deliberately, and the report carries none today. The hunt: filtered the fetched earnings calendar to the 179 names reporting 2026-10-26 to 2026-10-28 with revenue estimates between $40M and $600M and a positive EPS estimate, then checked liquidity and levels on the three that fit themes already understood well enough to judge quickly.
- `ENPH` 32.23 — -43.1% off its 90-day high, ATR 5.19%, below the 35.36 fifty-day, sitting exactly on the 32.20 twenty-day, $156.5M average daily dollar volume, reports 2026-10-27. REJECTED on the same ground as GLW and STX: a 2.0 ATR stop is 10.4% wide and the thesis would need a policy read on solar tariffs and credits that this run has not done. A technical level alone dressed up as a thesis is padding.
- `GRBK` 61.99 — -25.5% off its high, 4.9% above its 90-day low, below both moving averages, ATR 3.15%, $23.4M daily dollar volume, reports 2026-10-28. REJECTED: the only honest expression is a short, which runs into the same arithmetic that rejected ITB, and it would mean initiating a short four sessions before the company's own print.
- `AWI` 169.51 — -10.1% off its high, above both moving averages, ATR 1.87%, $56.9M daily dollar volume, reports 2026-10-27. REJECTED on correlation and on homework: it is the same building-products end market as the BCC position already held, and I have no read on its own margin structure.
All three clear the $500K liquidity floor comfortably, so liquidity is not why they were refused. **Six complete candidates beat fifteen fragments**, and a small cap captured to fill the lane would have been a fragment.

## [06:33 ET] WATCHLIST — for synthesis, with the condition that would make each actionable
Not recommendations. Each is a thing to watch with a stated trigger, levels from fetched history.
- `ITB` SELL_SHORT — the full arithmetic is in the rejection above. Actionable only if ITB bounces to 94-96, where a stop above the 96.59 two-hundred-day leaves the 81.50 target clearing 2.0:1 without a stop inside the noise. Catalyst: PHM and NVR 2026-10-22 bmo, FOMC 2026-10-28.
- `GD` BUY — 344.44, 13.9% off its 400.00 ninety-day high and below the 357.06 fifty-day, reports 2026-10-22 bmo. NOC's 2026-10-20 print showed defense volume growing at every segment with margin slipping; GD is the same question asked of a different mix. Trigger: a post-print close that HOLDS the 357.06 fifty-day. Do not buy before the print.
- `LMT` BUY — 548.71, above the 518.58 twenty-day and the 541.27 fifty-day, 10.5% off its 612.75 high, reports 2026-10-22 bmo. Already the strongest of the three large primes going in, which is the argument against buying it before the print rather than for it. Same trigger: the reaction, not the anticipation.
- `NUE` BUY — 261.50, 6.6% off its high and above both moving averages, reports 2026-10-26 amc. Held off the recommendation list only by the correlation cap against STLD and FCX. If STLD is stopped out, this is the better horse in the same race.
- `BTC` / `/MBT` LONG — IBIT 46.71 is 42.2% off its 90-day low and 5.4% off its high while AI hardware halves. Actionable once the specific micro contract month is verified against Robinhood's futures list and a second confirmation exists beyond the FOMC date already used twice in this report.
- `GLW` BUY — 132.26 after a 51.3% ninety-day drawdown, with the sell side upgrading through the fall (2026-07: 6 strong buy / 9 buy / 6 hold; 2026-10: 7 / 10 / 5) and ZERO insider buying. Trigger: an open-market insider purchase, or the 2026-10-27 print followed by a close back above the 151.36 twenty-day. Not before.
- `OXY` BUY — the awaiting-entry level of 54.00 is withdrawn, not replaced. OXY is 62.92, 1.3% off its ninety-day high. A re-entry needs a pullback to the 59.13 twenty-day with the energy complex still bid, not a chase.

## [06:34 ET] FOR `data_quality_notes` — everything that failed, in one place
Sources that worked: Finnhub quotes (all 40+ symbols requested), Finnhub earnings calendar (1,459 symbols), Finnhub recommendation trends and insider transactions, FRED (DGS10, DGS2, DFF, T10Y2Y, UNRATE, CPIAUCSL), CoinGecko, Nasdaq historical OHLCV via `market_data.py history`, SEC EDGAR filings and documents, the Federal Reserve's own FOMC calendar.

Sources that failed, and what each cost:
- **Every index and macro-market quote.** SPX, NDX, DJI, Russell 2000, VIX, /ES, /NQ, DXY, the 10-year yield quote, gold and WTI all returned `ok: false`. Yahoo answered HTTP 429 on all of them, Finnhub refuses CFD indices on this subscription, Stooq 404s the index symbols, and there is no AlphaVantage key. Cost: **this report contains no index level, no VIX and no dollar level, and the regime read is inferred from individual names rather than measured.** The only macro market quote that worked was TLT at 80.13.
- **Options-implied moves.** `market_data.py implied` returns HTTP 401 from the Yahoo options endpoint. Cost: no target in this report has been checked against what the straddle prices, including PYPL and ABT, both of which involve an earnings print.
- **Short interest and days to cover.** `api.nasdaq.com` read-timed-out for LULU, NKE and SMMT. Cost: no short-interest figure is cited anywhere; the positioning evidence is insider purchases, analyst revision direction and measured relative strength instead.
- **Event contracts.** The Kalshi query returned zero markets for FOMC, CPI, "interest rate", recession and inflation, and three unrelated tennis listings with null prices for "Fed". Cost: **no event-contract idea at all, and that is a source failure rather than a judgement that none was attractive.**
- **Pre-market bid/ask.** The spreads the validator read at 6am are artifacts of a closed market (BCC 119%, SNX 54%, STLD 11%, HII 6%), and TLT had no bid/ask at all.

Honest framing of what this report is: **predominantly position management**, for the fourth consecutive day. 19 of the 21 candidates are decisions on the existing book; `PYPL` is the only new entry and `ABT` is a previously published idea whose instruction had expired. Five ideas were researched and rejected with the arithmetic shown (ITB, GLW/STX/NXPI as a group, BTC, NUE/SCCO, and the ENPH/GRBK/AWI small-cap pass), and seven watchlist entries carry triggers. The skew is not a shortage of effort; it is a book of 19 open positions in a tape where the names worth owning are largely the ones already owned.

Prices: every equity and ETF figure in this report is the **2026-10-20 close**, stamped 20:00 UTC. At 6am ET that is the freshest honest price, taken in a closed session — not stale data. Crypto figures are live (CoinGecko, 2026-10-21).

## [06:36 ET] SUGGESTED RANKING — conviction first, then computed reward-to-risk
Ranks are synthesis's to assign; this is the ordering the rules in `config/strategy.md` produce from the validator's own recomputed ratios, offered so the order is not re-derived from scratch. Horizons are deliberately NOT interleaved — the two long-term ideas rank on merit, which puts HII second and PFE sixth.

| # | sym | conv | computed R:R | horizon | note |
| --- | --- | --- | --- | --- | --- |
| 1 | IYR | 4 | 2.81 | swing | short, FOMC 10/28 |
| 2 | HII | 4 | 2.73 | long_term | accumulation, 1 of 3 filled |
| 3 | PYPL | 4 | 2.58 | swing | the only new entry today |
| 4 | ABT | 4 | 2.39 | swing | WAIT for this morning's print |
| 5 | SMMT | 4 | 2.19 | swing | PDUFA 11/14, conviction cut from 5 |
| 6 | PFE | 3 | 3.62 | long_term | accumulation, no adds here |
| 7 | BCC | 3 | 2.91 | long_term | conviction cut from 4 |
| 8 | UNP | 3 | 2.45 | swing | earnings tomorrow bmo |
| 9 | NKE | 3 | 2.42 | swing | short, cover rule part-fired |
| 10 | XLF | 3 | 2.36 | swing | |
| 11 | CVS | 3 | 2.33 | swing | ELV read-through this morning |
| 12 | XLE | 3 | 2.13 | swing | best-performing open position |
| 13 | STLD | 3 | 2.12 | swing | NUE read-through 10/26 |
| 14 | LULU | 3 | 2.07 | swing | short |
| 15 | FCX | 3 | 2.06 | swing | stop amended to 63.20 |
| 16 | GE | 3 | 2.06 | swing | hold, do not add, pitched 7x already |
| 17 | TLT | 3 | 2.00 | swing | short, ratio exactly at the floor |
| 18 | KHC | 2 | 5.00 | swing | size cut to 1%, target 16 ATR away |
| 19 | DG | 2 | 2.30 | swing | size cut to 1% |
| 20 | CEG | 2 | 2.18 | swing | **EXIT** — fails expectancy by design |
| 21 | SNX | 2 | 2.08 | swing | **EXIT** — fails expectancy by design |

Correlation audit against the cap of 3 per driver: rising long yields = IYR short, TLT short, CEG exit (3, at cap — ITB was refused partly for this). Industrial metals and steel = STLD, FCX (2, with NUE and SCCO refused to stay under). Managed care and pharma = CVS, ABT, PFE (3, at cap — different drivers within it: ELV's loss ratio today, ABT's own print today, PFE's pipeline over years). Defense = HII alone, with GD and LMT on the watchlist. Energy = XLE alone, OXY withdrawn.

## [06:36 ET] VERIFICATION — re-ran the validator after the fixes; hard failures went from 30 to 8
Second dry run on a throwaway copy of all 21 candidates. Verdicts: 16 `warn`, 5 `fail`. Every one of the 21 dead-source failures is gone, GE's past-dated catalyst is gone, and the DG and KHC sizing failures are gone. The eight remaining hard failures are, in full:
- `CEG` — stop_distance 1.35 ATR, expectancy -0.05R. **Intentional.** This is the exit case; see above.
- `SNX` — stop_distance 1.78 ATR, expectancy -0.14R, spread 54.15%. **Intentional, plus one artifact.**
- `STLD` — spread 10.65%. Artifact of a 6am quote.
- `HII` — spread 6.27%. Artifact.
- `BCC` — spread 119.02%. Artifact; the stock is $76.
Nothing else fails. The four spread failures are the only ones where enforcement would demote an idea for a reason that is not about the idea, and all four entries are limit orders.

## [06:36 ET] CONVICTION NOTE — two scores are deliberately BELOW what the evidence supports
CEG and SNX each carry two distinct evidence kinds, which supports a 3, and both are scored 2. That direction is the safe one — the rule exists to stop inflation, and `check_conviction_evidence` names the supported score for the red team to lower, not raise. Both are exit recommendations and neither should read as a sturdier idea than it is. Every other score equals its evidence count exactly: DG and KHC have one kind and score 2; UNP, GE, XLE, TLT, XLF, STLD, FCX, LULU, NKE, PFE, BCC and CVS have two and score 3; IYR, SMMT, ABT, HII and PYPL have three and score 4. Nothing in this report scores 5, because nothing in it has four independent confirmations.

## [06:37 ET] RESEARCH COMPLETE
- candidates: 21 (42 lines in candidates.jsonl; 21 distinct symbol/direction pairs, last entry per symbol wins)
- all 19 open positions decided: 15 hold unchanged, 1 amended stop (FCX), 2 close early (CEG, SNX), 1 size cut from the conviction rule (DG and KHC both, so 2)
- awaiting-entry list triaged: ABT re-pitched with an expired instruction replaced, ITB moved to the watchlist on arithmetic, OXY/GLD/AAL withdrawn as stale, VST left unfilled, the September CPI contract retired as resolved
- new entries: 1 (PYPL). Rejections logged with the arithmetic: ITB, GLW, STX, NXPI, BTC/MBT, NUE, SCCO, ENPH, GRBK, AWI
- watchlist material: 7 entries, each with a trigger
- verified against `validate_report.py` twice, before synthesis, and the first run's findings were fixed rather than noted
- coverage gaps: no index, VIX, dollar, gold or crude quote (Yahoo 429, Finnhub index subscription, no AlphaVantage key) so the regime read is inferred from single names; no options-implied move (Yahoo options 401); no short interest (Nasdaq read timeout); **no event-contract idea at all, because the Kalshi query returned zero macro markets** — a source failure, not a judgement; no small cap, hunted across 179 near-term reporters and refused on shape rather than on liquidity
- sources that failed: query1/query2.finance.yahoo.com (429 on every index, 401 on options), finnhub CFD indices, stooq index symbols, api.nasdaq.com short-interest (timeout), Kalshi macro market search
- this is the fourth consecutive position-management-dominated report; the reason is a 19-position book, and it is stated in the data-quality notes rather than disguised
