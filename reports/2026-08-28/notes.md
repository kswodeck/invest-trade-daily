# Research log — 2026-08-28
started 11:54 ET Fri

## [11:56 ET] SETUP
- Run started 11:54 ET Fri 2026-08-28 — LATE run (normal window 6-11 ET). US equity market is OPEN and mid-session. Intraday ideas framed accordingly; equity levels are live intraday prices, not prior closes.
- Yahoo Finance is returning HTTP 429 across the board; index quotes (^GSPC/^NDX/^DJI/^RUT) all failed. Finnhub works for equities/ETFs. CoinGecko works for crypto. NOTE THIS IN data_quality_notes.

## [11:56 ET] MACRO — spot tape
- SPY 771.66 (+0.07%), QQQ 718.92 (-0.30%) — source: finnhub via market_data.py quote, asof 2026-08-28T15:54Z
- BTC 78,622 (-2.18% 24h); ETH 2,482.15 (-1.57%); SOL 105.54 (-1.47%) — source: coingecko via market_data.py crypto
- Rates (FRED, 2026-08-26): US10Y 4.66 (prev 4.64), US2Y 4.19, DFF 3.63, 10y-2y +0.47. Unemployment 4.1% (Jul, down from 4.2%). Long end drifting HIGHER — direct headwind to the open TLT long.
- Open-position marks 11:57 ET (finnhub): XLE 62.45, CCJ 100.71 (-5.29% TODAY), NKE 39.19 (+1.95%), PFE 27.94, DHT 19.55 (+1.03%), HD 329.14, LCII 101.80, BCC 77.46 (-1.66%), TJX 134.58, TLT 83.13

## [11:56 ET] CATALYST CALENDAR — next 10 sessions (finnhub earnings)
- Mon 08-31 bmo: SAIC, FRO
- Tue 09-01: DELL (amc), NIO (bmo), MDT (bmo), M, PANW (amc), MDB (amc)
- Wed 09-02: AVGO (amc), HPE (amc), GOLD (amc), NTAP, SNOW (amc), FIVE (amc), CPRT, OLLI (bmo), BF.B (bmo)
- Thu 09-03: LULU (amc), CPB (bmo), CIEN (bmo), TTC (bmo), ZS (amc), DOCU (amc), MOMO (bmo)
- Thu 09-10: ADBE (amc)
- source: python scripts/market_data.py earnings --days 14 (finnhub)

## [11:56 ET] SYSTEMS NOTE — why the /MBTU6 short will not die
- `state/open_positions.json` grades positions in publish_sheets.py via `_exit_hit` on fetched bars/live price. Futures symbols (/MBTU6) have NO price feed in this repo, so `last_price` stays null and the position can never be marked `stopped` — it shows `days 0` forever. That is why the same "COVER /MBTU6" instruction has appeared in the coverage-gap line on 08-24, 08-25 and 08-26 and the position is still listed as open.
- Also: validate_report.py --enforce demotes any idea whose entry/target/stop cannot produce an R:R above the horizon floor. A flatten-at-market order has no target and no stop by construction, so an exit instruction ALWAYS fails `risk_reward` and gets demoted to the watchlist. That is the mechanical reason the exits keep being buried. Both are repo issues to raise outside this run, not research findings.
- Research-phase action taken: the cover is written up as a POSITION UPDATE below and captured with levels that make it a real, checkable order rather than a naked "close it".

## [11:56 ET] EVENT CONTRACTS — Kalshi query degraded
- `market_data.py events "Fed"` returned 2 markets, both parlay/sports cross-category shards with null bids and null last_price. No Fed-decision market surfaced despite KXFEDDECISION-26SEP-H25 being published by this report on 08-22. The events search is returning junk today — treat event-contract coverage as a GAP, do not invent prices.

## [11:58 ET] POSITION UPDATE — CCJ — opened 2026-08-17 @95 and 2026-08-18 @88, now 100.63 (+5.9% / +14.4%)
- decision: HOLD both. Do not add above 100.00. CAPTURED via add_candidate.py.
- CCJ -5.36% today (106.33 -> 100.63, low 100.08) on no company news I could find (WebSearch found nothing dated 08-28). Ran 86.38 on 07-31 to 111.54 intraday on 08-26 = +29% in four weeks. Reads as profit-taking, but "I could not find the news" is not "there is no news" — stated as a risk in key_risk.
- levels: atr14 3.67 (3.45%), sma20 97.93, sma50 96.31, 90d range 83.15-131.21, -18.96% off high — source: market_data.py history CCJ --days 90 (nasdaq)
- insiders: 0 open-market buys, 0 distinct buyers, 6 months — source: market_data.py insiders CCJ (finnhub). Absence is not a negative, but there is no insider confirmation under this one.
- the add level is arithmetic, not taste: target 135, bear case 86 (actually traded 07-31) -> the 2.5:1 long-term floor is met only at E <= 100.00. At yesterday's 106.33 close the ratio was 1.41.

## [11:59 ET] LIVE TAPE — candidate set, 11:57 ET (finnhub)
LULU 118.23 (+2.81%) | CCJ 100.63 (-5.36%) | VST 138.63 (-0.84%) | DELL 464.37 (-1.67%) | AVGO 368.68 (-0.77%) | PANW 368.08 (-3.86%) | SNOW 328.32 (-0.24%) | ZS 185.27 (-1.08%) | OLLI 70.61 (-1.26%) | FIVE 244.21 (-1.12%) | CIEN 385.61 (-3.56%)
- Tape read: SPY +0.07% / QQQ -0.30% with software and networking notably weaker (PANW -3.9%, CIEN -3.6%, ZS -1.1%) into a week of software prints. That is a real, tradeable dispersion, not a general tape move.

## [12:02 ET] POSITION UPDATE — /MBTU6 — SHORT opened 2026-08-18 @64,100 and 2026-08-19 @64,340, stop 66,600 — COVER AT MARKET
- decision: CLOSE THE WHOLE THING TODAY. This is the highest-priority action in the report and it is the fourth consecutive day it has been ordered.
- BTC spot 78,622 (-2.18% 24h) — source: coingecko via market_data.py crypto. NO /MBTU6 futures feed exists in this repo, so this is a PROXY and the basis will move the figures. Said so in key_risk.
- the short is ~22% offside; the 66,600 stop was passed ~18% ago. A leveraged futures short with an ignored stop is the largest uncontrolled risk in the book.
- CAPTURED via add_candidate.py. Its reward-to-risk WILL fail the 1.5 intraday floor — a flatten-at-market has no target and no stop, so there is no arithmetic that can pass. Written into entry.condition so the red team does not demote it for that. See the 11:56 SYSTEMS NOTE for why this keeps disappearing.
- Related: the two BTC spot "SELL" lines (08-16 @62,950, 08-17 @63,400) are exit/avoid instructions on Robinhood Crypto, not shorts — there is nothing to close and no loss carried, but they should stop being carried as open positions.

## [12:04 ET] MACRO — the long end is the story
- 30-year UST above 5.30%, highest since 2007; 10-year 4.68% on 08-27 (4.66% FRED close 08-26, up from 4.64%) — source: cnbc.com/2026/08/20, tradingeconomics
- US Treasury announced 2026-08-19 it will AT LEAST DOUBLE long-dated buybacks, $2B -> $4B per operation, running 2026-09-09 through 2026-11-04 — source: cfr.org / cnbc. This is a dated, known-size official bid at the long end and it is the first real catalyst the open TLT long has had.
- BUT: yields REBOUNDED on 08-20 and wiped out the post-announcement decline. This catalyst has already been faded once. Reflected in counter_argument, not hidden.
- Attribution for the selloff is persistent inflation + rising government debt, i.e. term premium, not policy rates. Fed funds 3.63 with the curve at +47bp means cuts are not the driver.

## [12:04 ET] POSITION UPDATE — TJX — opened 2026-08-19 @150.85, stop 145.50, now 134.58 (-10.8%) — STOPPED, TREAT AS CLOSED
- The stop was passed by 7.5% and the position is still listed open. Same grading gap as /MBTU6. CAPTURED with re-entry at 122.00.
- Cause was guidance, not results: Q2 EPS 1.22 vs 1.19 est on ~15.2B sales; FY GAAP EPS guidance RAISED to 5.31-5.36 from 5.08-5.15; adjusted 5.15-5.20 MISSED the 5.22 consensus; Q3 guide 1.36-1.38 light. Jefferies cut to Hold 08-26, PT 180 -> 145 — sources: investing.com, qz.com, benzinga
- levels: 134.58, 90d range 134.17-170.00 (sitting 0.3% off the low), atr 3.38, sma20 150.37, sma50 153.63
- second time this report has been wrong on TJX (08-17 entry stopped 08-19). Re-entry deliberately set 9% below market to break the anchoring.

## [12:04 ET] POSITION UPDATE — HD — opened 2026-08-18 @340 and 2026-08-19 @337.49, stop 328.00, now 329.14 — HONOUR THE STOP
- 329.14 is 0.35% above the 328.00 stop. This is a live decision today.
- Q2 was fine: revenue 47.9B +5.7% y/y, adj EPS 4.92, comps +1.7%, FY26 guidance REAFFIRMED (sales +2.5-4.5%, adj EPS growth up to 4%), quarterly dividend RAISED to 2.33 — sources: 247wallst 08-19, yahoo finance video
- Do not convert the losing swing lots into the long-term thesis. Long-term accumulation captured separately at 296.00 (2.5:1 vs a 259 bear case and a 388 target; 388 = a 2.4% yield on the 9.32 annualised dividend).
- levels: atr 8.36 (2.54%), sma20 341.81, sma50 340.43, 90d range 289.10-361.64, -9.13% off high

## [12:00 ET] EVENT CONTRACTS — COVERAGE GAP, no candidates possible
- market_data.py events returned count 0 for "Fed decision", "CPI", "recession", "Bitcoin"; the "Fed" query returned 2 sports parlay shards with null prices. The Kalshi search is not returning usable markets today.
- Consequence: ZERO event-contract candidates today, and the KXFEDDECISION-26SEP-H25 YES @32 published 08-22 could not be re-priced or re-validated. This is a tooling failure, not an absence of opportunity. Do not invent an implied probability to fill the lane.

## [12:03 ET] INSIDERS — the one signal worth having today (finnhub, 6-month window)
- **PFE: 3 open-market buys, 3 DISTINCT buyers, $2,960,110 total.** CEO Albert Bourla 38,000 sh @ 26.34 on 2026-08-12; Mortimer J Buckley (ex-Vanguard CEO) 37,632 sh @ 25.52 on 2026-08-05; Ronald E Blaylock 39,231 sh @ 25.46 on 2026-08-05. Three different people, similar size, inside three weeks. This is the cluster pattern, not one-off diversification.
- **LULU: 3 buys, 2 distinct buyers, $1,994,952.** Charles V Bergh (chairman, ex-Levi Strauss CEO) 4,275 sh @ 117.05 on 2026-06-15 AND 6,090 sh @ 164.20 on 2026-03-20; Andre Maestrini 3,275 sh @ 151.02 on 2026-04-01. Bergh bought at 117.05 in June — within 1% of today's 118.23, and he was already down 29% on his March buy when he did it. That is averaging into his own name at the price this report is recommending.
- CCJ 0 buys / 0 sells. OLLI 0 buys / 3 sells. CIEN 0 buys / 45 sells. DHT 0/4. LCII 0/3. XLE n/a (ETF). AVGO returned nulls — source failed, not a zero.
- Absence of buying is NOT a negative and is not treated as one. Presence is weighted.

## [12:03 ET] REJECTED — OLLI — comps +1.7% vs a 2% guide, -25% since 3/31, 0 insider buys against 3 sells; it is the same consumer-trades-down bet as TJX in a worse-evidenced form, and the correlation cap does not justify two. source: simplywall.st, yahoo/finance OLLI Q2
## [12:03 ET] REJECTED — CIEN — -37% off high with earnings 09-03, but 45 insider sells and zero buys in six months, and a 7.1% ATR means any pre-print entry is a coin flip on noise
## [12:03 ET] REJECTED — PANW — -3.9% today on pre-earnings de-risking into the 09-01 print, but the stock is only 4.0% off its 150-day high and above its 20-day (364.87). De-risking in a name at highs is not a discount, and there is no thesis here beyond "it fell today". source: tradingkey.com 08-28
## [12:03 ET] REJECTED — DINO — awaiting-entry at 90.00/93.00 from 08-22 and 08-26 is UNFILLED and will not fill: DINO is 97.00, only 1.46% off its 150-day high. Level unchanged, no action, do not chase.

## [12:06 ET] SMALL CAP HUNT — insider-cluster screen (finnhub 6mo + simplywall.st Aug-2026 screens)
| sym | px | off 150d high | atr% | median 15d $vol | insider buys / distinct buyers / $ | buy prices |
| --- | --- | --- | --- | --- | --- | --- |
| MBC | 8.56 | -37.9% | 4.25% | $12.5M | 4 / **4** / $696,390 | 8.43-9.11, all June 2026 |
| GO | 12.20 | -4.3% | 4.64% | $30.5M | 16 / **7** / $8,016,761 | 6.35-9.37 |
| CLVT | 2.05 | -33.3% | 5.98% | $8.0M | 2 / 1 / $1,671,500 | 1.85-1.86, Aug 6-7 |
| SONO | 15.35 | -14.2% | 4.23% | $18.6M | 10 / 2 / $25,168,850 | 13.20-13.57, March |
- All four clear the $500K average dollar volume floor by a wide margin, so exit is not the constraint here.
- MBC is the cleanest shape in the group: FOUR distinct buyers and the stock is trading AT their purchase band rather than above it.

## [12:06 ET] REJECTED — GO (Grocery Outlet) — the strongest cluster on the screen (7 distinct buyers, $8.0M) but it already worked: they bought 6.35-9.37 and the stock is 12.20, only 4.3% off its 150-day high. The signal has been paid. Watchlist, not a buy.
## [12:06 ET] REJECTED — SONO — $25.2M of buying is almost entirely Coliseum Capital Management, a single institutional holder filing Form 4s as a >10% owner. That is one position being built, not several executives independently concluding the stock is cheap, and it is the March price (13.20-13.57) not today's 15.35.

## [12:05 ET] POSITION UPDATE — BCC — opened 2026-08-18 @81.00, stop 76.00, now 77.64 (-4.1%) — HOLD, AND A CORRECTION
- **Found an incoherence this report shipped:** an unfilled BUY at 76.50 (published 08-25, still on the awaiting-entry list) sits 50 cents ABOVE the 76.00 stop on the same stock. As published, the plan buys more at 76.50 and liquidates everything at 76.00. The 76.50 order is WITHDRAWN; the real add level is 74.00, below the stop.
- The 76.00 stop is 2.1% away against a 2.85% ATR — inside one normal day. This position is likelier to be stopped by noise than by the thesis failing. Accepting that rather than widening the stop after the fact.
- Facts: lumber below $650/mbf, ~-12% y/y after new US tariffs on Canadian wood; EWP realisations -7% (I-joists) and -4% (LVL) y/y; BUT August engineered-wood order file ~3x prior year. Q3 adj EBITDA guide $82-114M — a wide range that says management does not know. sources: fool.com Q2 transcript 08-10, investing.com
- CAPTURED. Conviction cut to 2: one volume datapoint against four price datapoints is not a 3.

## [12:05 ET] POSITION UPDATES — hold, no change, no candidate captured
- **XLE** 62.48 (+0.30%) — three lots from 60.50/60.80, targets 64.50-67.00, stops 57.80-59.20. Working; 3.7% off the 150-day high, above the 20-day (61.10) and 50-day (57.99). Nothing changed, no action.
- **DHT** 19.59 (+1.24%) — FOUR lots (08-18 @18.80 and three at 19.40 on 08-23/24/25) plus an unfilled 18.80 from 08-26. Recommended 5x in ten days; a sixth pitch would be conviction theatre. **SUPERSEDED at 12:24 — see the tanker block below. FRO did not report on 08-31 as the earnings calendar said; it reported THIS MORNING, and the read-across changed the risk enough to warrant a stop-tightening update.**
- **NKE** 39.23 (+2.06%) — two long-term lots. The 08-26 report already set the plan (add only at 34.00, the 40.75 re-entry withdrawn). Nothing has changed since; not re-pitching. Note the correlation with the LULU idea captured today — both are the same de-rated-athleisure bet and the reader should size them as one.
- **LCII** 102.85 (+0.54%) — from 94.00, target 138.00, no stop. +9.4%, 26% off its 150-day high, 0 insider buys / 3 sells. Hold. No new information today.
- **VST** 138.48 (-0.95%) — the 08-26 plan was accumulate in halves at 128/120 and it has not filled; VST is 138.48, 8% above the first rung. Level UNCHANGED, still a wait, no action, not re-pitched as new.

## [12:07 ET] REJECTED — AVGO — the setup is real (-24.9% off its 150-day high since the June Q2 print, when Hock Tan declined to raise the $100B full-year AI chip sales target; Q3 reports 09-02 amc) but I could not build a defensible valuation anchor. GuruFocus shows forward P/E 19.23 as of 08-28 against a trailing 52.29 and TTM EPS of $6.20 — those do not reconcile (19.23x on a $368 price implies ~$19 of forward EPS, three times trailing), and I am not going to publish a long-term target built on a number I cannot make add up. A swing into a 09-02 print with a 3.57% ATR and no edge beyond "it fell" is not a candidate either. sources: gurufocus.com/term/forward-pe-ratio/AVGO, fool.com 08-27
## [12:07 ET] NO CHANGE — GLD — 413.27 (-2.21% today) after running to 428.07 on 08-25; the 398.00 awaiting-entry level from 08-22 is UNCHANGED and still 3.7% below the market. GLD has been recommended 3x in ten days and nothing new happened today, so it is not being re-pitched. sma20 402.96, sma50 385.66, -17.1% off the 150-day high.
- Related and worth noting for the reader: SLV 61.32 (-2.31%) sits 42.9% below its 150-day high of 109.83 while GLD is only 17.1% below its own. Silver has had a spike-and-crash that gold has not. Not researched far enough today to be a candidate.

## [12:10 ET] MACRO — I WAS MISSING THE TWO BIGGEST THINGS. Corrected.
### 1. Fed Chair KEVIN WARSH delivered his Jackson Hole keynote THIS MORNING and it was HAWKISH
- Warsh: "while this summer's inflation readings were better than expected, they do not tell me that underlying trends have meaningfully improved."
- He again gave NO forward guidance and NO reaction function — the standing complaint about him.
- Reaction: 2-year yield +6 to +8bp to 4.298-4.31%, highest since late July. **30-year yield 2bp LOWER at 5.168%.** Stocks CLIMBED after digesting it. Described as "a deliberately hawkish speech that will put to rest any concerns about the Fed's willingness to raise rates to restore price stability."
- sources: cnbc.com/2026/08/28/kevin-warsh-jackson-hole-federal-reserve-inflation.html, cnbc.com/2026/08/28/treasury-yields-jackson-hole.html, finance.yahoo.com Jackson Hole live blog
- **This is a bull flattener and it is the opposite of the risk that was flagged going in.** SocGen's Jan Groen warned pre-speech that a big-picture speech with no hint that hikes were on the table would read DOVISH and push the 30-year to 5.5%+. That did not happen — Warsh was hawkish and the long end RALLIED slightly. A Fed credibly willing to hike compresses the term premium, which is the part of the curve TLT owns.
- Consequences across the book: constructive for TLT (revised below, conviction 3 -> 4). A headwind for rate-sensitive equities, which reinforces the HD "wait at 296" call rather than softening it. Consistent with GLD -2.21% and crypto -2% today.
- Note vs FRED: 2y was 4.19 on 08-26; it is 4.30 now. That is a real 11bp move and the FRED figures in this file are two days stale by construction.

### 2. There is an ACTIVE US-IRAN WAR and the Strait of Hormuz is the flashpoint
- US Navy blockade is slashing Iran oil exports; Trump rejected a return to ceasefire terms on 08-27 and oil settled +2%. Crude ~$83/bbl today, paring the prior session.
- Persian Gulf exports have RECOVERED to ~15-16 mb/d against 22-24 pre-conflict and a March low of 5-6 mb/d. Iran and Oman agreed a revenue-sharing framework for the strait; Tehran says that does not mean immediate reopening. Brent topped $89 earlier in August.
- The market has re-framed this as an economic/sanctions confrontation rather than a physical supply threat, which is why crude is drifting DOWN despite the headlines.
- sources: cnbc.com/2026/08/11/hormuz-oil-prices-us-iran.html, oilprice.com "Brent Tops $89", aljazeera 08-12, tradingeconomics crude
- Consequence for the open XLE longs: this IS the driver and it is intact but decaying — flows recovering is bearish for the flat price. Holding, not adding.
- **Consequence for DINO (recommended 08-22 and 08-26, unfilled at 90/93, now 97.00):** "Trump to meet refiners and fuel retailers as Iran war boosts gas prices ahead of midterms" (Reuters 08-27). A president convening refiners about pump prices before an election is political risk sitting directly on top of a refining-margin trade that is already 1.5% from its high. Reinforces the rejection — do not chase DINO.
- I did not have time to build a defensible crude or tanker candidate off this. Real coverage gap: the strongest macro story of the day and the report carries no direct expression of it beyond the pre-existing XLE longs.

## [12:13 ET] CCJ — CORRECTING MY OWN 11:58 ENTRY. The -5.7% does have a cause.
- I wrote at 11:58 that I could find no reason for the drop. Found it on a second pass, and it changes the shape of the idea:
- **Westinghouse (Cameco owns 49%) posted a NET LOSS of $10M (Cameco share) in Q2 2026, against +$126M a year earlier.** Group adjusted EBITDA -42% to US$391M, attributed primarily to that weaker equity income. — source: cameco.com Q2 2026 results
- Offsetting, and also hard numbers: 2026 revenue guidance RAISED to C$3.32-3.57B from C$2.85-3.06B; production guidance UNCHANGED at 19.5-21.5 Mlb (so it is a price effect); Q2 average realised uranium price $67.79/lb, +18% from $57.35 — source: cameco.com
- **Westinghouse has confidentially filed a draft Form S-1 with the SEC for an IPO.** That is a real, filed catalyst and it replaces the vague "utility contracting cycle" driver I first wrote.
- The 29% four-week run was a TRADE-POLICY narrative: Cameco owns the refinery at the centre of a Canadian uranium export threat (fool.com 08-26); CCJ closed +7.24% on 08-21 on it. Narrative moves round-trip, which is the best explanation of today.
- RE-CAPTURED with the two-sided evidence, the Westinghouse IPO as the catalyst, and a much sharper counter_argument. Conviction held at 3 — the guidance raise and the realised price are real, and they are roughly offset by a 49%-owned business swinging to a loss.

## [12:15 ET] ARITHMETIC AUDIT — I checked my own numbers and four of them failed
Recomputed reward-to-risk on every captured candidate from entry/target/downside before handing off. Four entries I had written failed their own floor, all by small margins — which is exactly the failure mode this repo was built to catch (the live report that once shipped eight ratios clustered at 2.04-2.33 against a 2.0 floor).

| sym | entry as first written | rr | corrected entry | rr |
| --- | --- | --- | --- | --- |
| TJX | 122.00 | 2.44 | **121.50** | 2.65 |
| HD | 296.00 | 2.49 | **295.00** | 2.58 |
| MBC | 7.00 | 2.49 | **6.90** | 2.62 |
| PFE | 27.29 | 2.4965 (only clears on rounding) | **27.20** | 2.57 |
| CLVT | 2.00 | 2.50 exactly, no margin | **1.95** | 2.68 |
| TLT | 82.70 | 2.00 exactly, no margin | **82.60** | 2.18 |
| BCC | 76.50 vs a 76.00 stop | **31.0 off a 50-cent risk — nonsense** | **74.00, new 70.00 stop** | 4.5 |

- **In every case I moved the ENTRY DOWN. I did not move a single target up or a single stop in.** That is the distinction that matters: the floor is there to reject ideas, and the correct response to failing it is to demand a better price, not a friendlier denominator.
- The BCC one was the real error — entry 76.50 against a 76.00 stop produced a 31:1 ratio out of a 50-cent risk, which is arithmetic that flatters a position rather than testing it. Corrected so the 76.00 stop stays with the EXISTING lot and any new lot at 74.00 carries its own 70.00 stop (4.00 = ~1.8 ATR), giving an honest 4.5:1.
- Only ONE candidate still fails: /MBTU6 at 1.22 against the 1.5 intraday floor. That is by construction and is documented in its entry.condition — a flatten-at-market order has no target and no stop, so no arithmetic can pass. It must not be demoted for this.

## [12:16 ET] FALSIFICATION AND CORRELATION PASS
- **The housing/construction cluster is AT the correlation cap of 3: HD, MBC, BCC.** All three depend on the same thing — US housing and remodel activity thawing — and all three now face the same fresh headwind, because this morning's hawkish Warsh speech pushed the 2-year to 4.30%, its highest since late July. A reader should treat these as ONE bet, not three, and size accordingly. NO fourth housing idea was added today for this reason. Mitigating: all three are WAIT levels 5-19% below the market, so the cluster carries no exposure unless housing gets materially worse first — which is itself the tell that they are the same trade.
- **Second cluster: consumer discretionary — TJX and LULU, plus the two open NKE lots.** TJX and LULU are both "quality brand de-rated, wait for a lower price"; NKE is the same trade already on the book. Flagged inside the LULU candidate itself.
- **The report is heavily skewed to `long_term` and to WAIT.** Of ten distinct ideas, seven are long_term and seven carry `wait: true`. That is not evasion and it was not engineered: SPY is 0.07% from flat near its highs, and a 2.5:1 long-term floor measured against an honest bear case simply does not clear at today's prices for most quality names. The honest output is a list of prices, not a list of buys.
- **Actionable TODAY rather than on a limit:** /MBTU6 (cover at market, urgent), CCJ (100.23 vs a 100.00 add level, 0.2% away), TLT (83.08 vs 82.60, 0.6%), PFE (27.91 vs 27.20, 2.5%).
- **What survived falsification with the least damage:** PFE — three distinct insiders including the CEO buying $2.96M in August is the only evidence in this report that is not a price, a multiple, or a management forecast. **What survived worst:** CCJ, where a 29% four-week run on a trade-policy narrative sits against a 49%-owned Westinghouse swinging from +$126M to -$10M. It is held at conviction 3 rather than raised.

## [12:24 ET] TANKERS — the best fundamental news in the report, and the tape rejected it
- **FRO reported Q2 2026 THIS MORNING (2026-08-28), not 08-31 as the finnhub earnings calendar said.** Record net profit $659.2M / $2.96 per share on $753.27M revenue — the best quarter in Frontline history. Average daily TCE: VLCC $152,700, Suezmax $111,400, LR2/Aframax $92,400. — source: globenewswire 2026/08/28 FRO Q2 results
- **Spot is running at roughly 3x that.** TD3C Middle East Gulf-China above $520,000/day; VLCC fixtures near $470,000/day. Hormuz cut VLCC volumes ~36% but lengthened voyages — Atlantic crude to Asia round the Cape, Galveston-Ningbo being 2.6x the Ras Tanura-Ningbo distance. Cargo rerouting via Fujairah, Khor Fakkan, Oman and the Jeddah land bridge. — sources: lloydslist.com LL1157100, oilprice.com, lloydslistintelligence Hormuz brief 08-19
- **And the tape did nothing with it.** FRO printed a new 150-day high at 45.29 intraday and FADED to 43.94 (+0.43%), 3.1% off the high. DHT 19.59 (+1.24%), INSW 99.09 (**-0.17%**), TNK 88.47 (+0.31%). Record results plus record spot rates producing a fade from a new high is the market saying the cycle is priced.
- **REJECTED — FRO as a new long.** Not because the numbers are bad — they are the best in the report — but because buying a cyclical at an all-time-record spot rate, 3.1% off its high, on the day it confirms the peak, is the trade that looks most obvious and works least. No insider buys and no insider sells (0/0), so no confirmation either way. Median 15d $vol $84M, liquidity is not the issue.
- **What it DID change: the open DHT position.** Four lots with stops scattered at 17.60/18.30/18.60/18.90 sit on a driver at a cyclical extreme where every dated development points to normalisation — Iran-Oman revenue-sharing framework agreed, Gulf exports back to 15-16 mb/d from the 5-6 March low, DP World accelerating Fujairah to bypass the strait permanently. Captured a POSITION UPDATE: consolidate stops at 18.60, withdraw the unfilled 18.80 buy (it sits ABOVE the raised stop — the same incoherence found in BCC), add nothing at 19.59, new money only at 17.80 with its own 16.60 stop. This is a risk change, not a sixth pitch, and it is the correct response to being right about fundamentals and late in a cycle.

## [12:26 ET] VENUE CHECK — /MBTU6
- The Robinhood futures support URL cited in the /MBTU6 candidate 404s. Verified availability independently instead: Robinhood offers Micro Bitcoin (MBT) futures, sized at 0.10 BTC, with contract months including Sep 2026 — so /MBTU6 is tradeable and the cover order can be placed. Micro WTI Crude (/MCL) is also offered, and Robinhood publishes a crypto-futures explainer. sources: brokerchooser.com Robinhood micro bitcoin futures fees, robinhood.com/us/en/learn/articles/what-are-crypto-futures/, cmegroup.com micro-bitcoin contract specs
- Equities/ETFs recommended today are all US exchange-listed common or ETFs (NYSE/Nasdaq): CCJ, PFE, TLT, LULU, TJX, HD, MBC, CLVT, BCC, DHT. CLVT at $2.05 is the only one near a price floor and it clears the $1 minimum comfortably, with $8.0M median daily dollar volume.

## [12:30 ET] BREADTH CROSS-CHECK — the hawkish Fed is visible in the tape
- Today: SPY +0.48%, QQQ +0.35%, DIA +0.31%, **IWM -0.50%.** Large caps up, SMALL CAPS DOWN, on the day the 2-year jumped 6-8bp to 4.30% on Warsh. That is the textbook signature of a hawkish repricing and it is an independent confirmation of the 12:10 macro read rather than a restatement of it. — source: stockanalysis.com/markets, cnbc.com/markets/us-market-movers
- Directly relevant to the two small caps captured today: **MBC and CLVT are both WAIT levels 5-19% BELOW the market, and the prevailing wind is now pushing small caps toward those levels rather than away.** That is a reason to be patient, not a reason to reach.
- It also means my earlier note that "stocks climbed" after the speech was true only of large caps. Correcting that here: the index rally was not broad.
- Note the earlier index figures in this file came from SPY/QQQ as proxies because Yahoo 429'd every index symbol; these are the ETF prints and they agree.

## [12:17 ET] RESEARCH COMPLETE
- candidates: 22 rows covering **11 distinct symbols** (synthesis takes the last per symbol) — /MBTU6, CCJ, PFE, TLT, LULU, TJX, HD, MBC, CLVT, BCC, DHT
- **THE ONE URGENT ITEM: cover the /MBTU6 short at market.** Fourth consecutive day it has been ordered; ~22% offside; its R:R will fail validation by construction and it must not be demoted for that.
- position updates decided: CCJ hold/no-add-above-100, /MBTU6 COVER, TJX stopped-treat-as-closed, HD honour-the-328-stop, TLT hold+add-82.60, PFE hold, BCC hold + withdraw the incoherent 76.50 order, DHT raise stops to 18.60 + withdraw the 18.80 order. Hold-no-change and deliberately NOT re-pitched: XLE, NKE, LCII, VST, GLD, DINO.
- **TWO published orders were found sitting ABOVE their own stop on the same stock** — BCC buy 76.50 against a 76.00 stop, and DHT buy 18.80 against a raised 18.60 stop. Both withdrawn. Worth a systematic check in synthesis: an awaiting-entry level should never be inside or above the stop of a live position in the same symbol.
- rejected with reasons logged: OLLI, CIEN, PANW, AVGO, GO, SONO, DINO, GLD, FRO
- **coverage gaps:**
  1. **Event contracts — total gap, zero candidates.** market_data.py events returned count 0 for "Fed decision", "CPI", "recession", "Bitcoin", "KXFED", "September", "inflation", "oil", "Hormuz"; the "Fed" query returned two sports parlay shards with null prices. Could not re-price the KXFEDDECISION-26SEP-H25 YES @32 published on 08-22. Tooling failure, not an absence of opportunity — and it bit on the one day when a hawkish Fed chair and a live Hormuz standoff both made prediction markets the natural expression.
  2. **PARTLY CLOSED at 12:24.** The US-Iran / Hormuz story is now covered through the tanker complex — FRO's record print was found, FRO was rejected as a late-cycle long, and the open DHT position was updated with tightened stops. Still missing: any direct CRUDE expression (/MCLV6 is tradeable on Robinhood) and any Gulf-infrastructure idea. Crude is a headline market in both directions and I had no probabilistic edge worth publishing, so none was manufactured.
  3. **No intraday ideas** other than the /MBTU6 cover, and no crypto view other than exiting one. Bearish crypto needs futures and I had no thesis worth the leverage.
  4. AVGO insider data returned nulls (source failed, not a zero). AVGO valuation abandoned — GuruFocus forward P/E 19.23 does not reconcile with trailing 52.29 on $6.20 TTM EPS.
- **sources that failed:** Yahoo Finance HTTP 429 across the board, so ALL index quotes (^GSPC, ^NDX, ^DJI, ^RUT) were unavailable and SPY/QQQ were used as proxies; Kalshi event search (above); CNN HTTP 451; finnhub insiders for AVGO.
- **stale-data warning for synthesis:** the FRED rates block in this file (10y 4.66, 2y 4.19) is dated 2026-08-26 and was superseded intraday — the 2-year is 4.298-4.31% and the 30-year 5.168% after this morning's speech. Use the later figures.
- run context: started 11:54 ET, a LATE catch-up run well outside the normal 6-11 ET window, with the US equity market open and mid-session throughout. Equity prices in this file are live intraday marks, not prior closes. Do NOT frame the report as a 6am pre-open view.


## [12:33 ET] FINAL — CCJ entry nudged 100.00 -> 99.50
- 100.00 computed exactly 2.50:1 against the 135 target and 86 bear case, i.e. zero margin, the same condition I corrected on CLVT and TLT earlier. 99.50 clears at 2.63:1. Applied for consistency: in every correction today the ENTRY moved down and no target or stop was touched.
- Final audit result: 22 rows, 11 distinct symbols, every candidate carries all required fields, at least 2 sources, sizing inside its tier cap, a bear case on every long_term idea and a stop on the futures idea. Ten of eleven clear their reward-to-risk floor on recomputation; the eleventh is the /MBTU6 flatten, which cannot and is documented.
