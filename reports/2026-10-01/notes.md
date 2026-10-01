# Research log — 2026-10-01

## [06:03 ET] SETUP
- Session: pre-market. Freshest honest equity prices are 2026-09-30 closes (age ~842 min). Not stale — closed market.
- 16 open positions, 15 awaiting entry. Track record 2/11 target (18%), avg -2.8%. n=11 closed is BELOW the ~15 noise floor, so no category gets banned on it; stock 0/6 is noted but not over-fitted.
- Repetition warnings from prior context: MU 3x, PFE 3x, XLU 2x, GDX 2x, XLE 2x, TLT 2x. Avoid fresh pitches on these without new information.

## [06:03 ET] DATA QUALITY — macro index quotes failed
- ^GSPC / ^NDX / ^DJI / ^RUT all failed: finnhub requires a CFD subscription for indices, Yahoo returned HTTP 429, stooq 404, no AlphaVantage key.
- Index level reading today must come from ETF proxies (SPY/QQQ/IWM) rather than the index itself.

## [06:04 ET] OPEN POSITION PRICES — 2026-09-30 close
| Sym | Entry | Close 9/30 | Stop | Note |
| --- | --- | --- | --- | --- |
| XLE | 63.90 | 61.50 | 60.80 | -3.8%, stop 1.1% away — live risk |
| CCJ | 94.00 | 86.67 | 82.50 | -7.8% |
| NKE | 40.75 | 35.40 | none | -13.1% |
| BCC | 76.50 | 74.15 | none | -3.1%, fell 2.4% on 9/30 |
| LCII | 94.00 | 83.67 | none | -11.0%, fell 2.0% on 9/30 |
| PFE | 27.60 | 28.52 | none | +3.3% |
| CEG | 272.00 | 254.02 | 250.00 | -6.6%, FELL 3.99% on 9/30, stop 1.6% away — live risk |
| EEM | 65.60 | 66.79 | 63.00 | +1.8% |
| DINO | 107.50 | 107.32 | 97.75 | -0.2%, rose 1.6% on 9/30 |
| LULU | 115.00 | 96.19 | none | -16.4% |
| SVRA | 5.35 | 5.16 | 4.60 | -3.6% |
| SNX | 260.00 | 256.85 | 242.50 | -1.2% |
| XLU (short) | 39.60 | 39.44 | 40.95 | +0.4% in favour |
| GDX | 91.20 | 89.07* | 85.40 | -2.3% (*see refetch) |

## [06:06 ET] MACRO — rates and policy (FRED, fetched)
- US 10y 5.26% (2026-09-29); US 2y 4.89% (2026-09-29); 10y-2y +0.41 (2026-09-30); fed funds effective 3.88% (2026-09-29); unemployment 4.1% (2026-08); CPI index 334.131 (2026-08)
- source: https://fred.stlouisfed.org
- READ: the curve is steep with the 10y at 5.26% against a 3.88% policy rate — 138bp of term premium. Long-end yields this high with policy this low is a fiscal/term-premium regime, not a growth regime. TLT proxy (bonds_20y) 77.78, -0.58% on 9/30 and making new lows. This is the single most important macro fact of the day and it argues AGAINST long duration and against bond-proxy equities (utilities, REITs, staples).
- DATA GAP: VIX, DXY, ES/NQ futures, gold, WTI all FAILED (finnhub index subscription + Yahoo 429). Crypto via coingecko also returned prices FAILED on the macro call.

## [06:07 ET] CATALYST — NKE REPORTS TODAY 2026-10-01 AMC. This is an open-position event.
- Fetched calendar: NKE 2026-10-01, hour `amc`, EPS est $0.4364, revenue est $11.429B — source: finnhub earnings calendar via scripts/market_data.py earnings
- I hold BOTH sides: NKE BUY opened 2026-08-17 @ 40.75 (no stop, long-term) now 35.40 = -13.1%, AND NKE SELL opened 2026-09-08 @ 38.40 now 35.40 = +6.7% in favour.
- NKE also fell -1.23% on 9/30 into the print.
- This needs a decision TODAY, before 16:00 ET, and it is the highest-priority item in this run.

## [06:07 ET] CATALYST CALENDAR — next 10 sessions (fetched finnhub)
- 2026-10-01 (today): NKE amc; ACN bmo (est 3.2141 EPS / 18.21B rev); AYI bmo; AEHR; PKE
- 2026-10-02: VFS (est -0.3333)
- 2026-10-05: MKC bmo (est 0.7633 / 1.997B)
- 2026-10-06: STZ amc (est 3.6021 / 2.568B); LW bmo (est 0.606 / 1.704B); RPM bmo (est 1.966 / 2.245B); APOG bmo; NEOG amc; PENG amc; WS amc
- 2026-10-07: APLD amc (est -0.3098 / 137.6M); LEVI amc (est 0.3649 / 1.647B); NRIX; RGP amc
- 2026-10-08: PEP bmo (est 2.319 / 25.23B); TLRY (est -0.1948); HELE (est 0.5151); KARO; BYRN; ANGO
- 2026-10-09: DAL bmo (est 1.9868 / 17.78B); CCEL; CLSD amc
- 2026-10-15: Q3 bank/industrial season opens — BX bmo, AA amc, AAL, ALK, CMC bmo, BALY amc
- READ: this is a genuinely thin earnings window. Oct 1-9 is the tail of the Aug-quarter reporters and Q3 season does not start until Oct 15. Per config/strategy.md, a quiet calendar means shifting budget from catalyst hunting into durable mispricings, not padding the trade lane.

## [06:16 ET] OPEN BOOK — stop distance audit, measured from ENTRY (all ATR14 fetched 150d)
Measured from entry, not from the current price — validation uses entry, and a position that has drifted toward a correctly-set stop is a stop working, not a stop too tight.

| Sym | Entry | Stop | ATR14 | Stop dist (ATR) | Floor | Pass | R:R from entry |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XLE | 63.90 | 60.80 | 1.2569 | 2.47 | 1.8 etf | yes | 6.60/3.10 = 2.13 |
| CCJ | 94.00 | 82.50 | 3.0971 | 3.71 | 2.0 | yes | 41.0/11.5 = 3.57 |
| CEG | 272.00 | 250.00 | 9.5828 | 2.30 | 2.0 | yes | 48.0/22.0 = 2.18 |
| EEM | 65.60 | 63.00 | 1.1065 | 2.35 | 1.8 etf | yes | 5.90/2.60 = 2.27 |
| DINO | 107.50 | 97.75 | 5.2507 | 1.86 | 2.0 | NO (marginal) | 20.5/9.75 = 2.10 |
| SVRA | 5.35 | 4.60 | 0.2284 | 3.28 | 2.0 | yes | 2.65/0.75 = 3.53 |
| SNX | 260.00 | 242.50 | 12.6371 | **1.38** | 2.0 | **NO** | 36.47/17.50 = 2.08 |
| XLU short | 39.60 | 40.95 | 0.5750 | 2.35 | 1.8 etf | yes | 2.80/1.35 = 2.07 |
| GDX | 91.20 | 85.40 | 3.1711 | 1.83 | 1.8 etf | yes (bare) | 13.20/5.80 = 2.28 |

- **SNX is the one real failure and it is the textbook pattern CLAUDE.md warns about.** Its 2.08 R:R is only reached *because* the stop is 1.38 ATR. Widen it honestly to 2.0 ATR (25.27 -> stop 234.73) and R:R falls to 36.47/25.27 = **1.44**, which fails the swing floor. SNX ATR is 4.92% of price; a 1.38 ATR stop on a name that moves 5% a day is a coin flip on noise. It did not clear the floor on its own merits.
- Correction to my own first pass: I initially measured stop distance from the *current* price and concluded XLE and CEG had unusably tight stops. From entry both are fine (2.47 and 2.30 ATR). They are simply close to the stop now because the trade moved against them. Logging the error so the synthesis phase does not inherit it.

## [06:17 ET] OPEN BOOK — the systematic finding worth more than any single idea
Of the 14 long positions, 11 sit below BOTH their 20d and 50d SMA, and four are within ~4% of their own 150-day LOW:
- LULU 96.19, **0.88%** off its 150d low (95.35), -48.9% off high, SMA20 101.86 / SMA50 112.61
- NKE 35.40, **0.70%** off its 150d low (35.155), -45.6% off high, SMA20 36.64 / SMA50 39.23
- LCII 83.67, **1.08%** off its 150d low (82.775), -39.4% off high, SMA20 90.27 / SMA50 98.97
- CCJ 86.67, 4.23% off its 150d low (83.15), -34.0% off high, SMA20 93.47 / SMA50 94.80
Only PFE (+3.3%, above SMA20 28.107 and SMA50 27.207, 2.4% off its 150d HIGH) and EEM (+1.8%, above SMA50) are in confirmed uptrends.
- READ: the book is long a basket of still-falling knives, which is the same thing the track record says from the other direction (stock 0/6 hit target, avg -5.0%) and the same thing config/strategy.md records about entry style (31 pullback entries vs 1 breakout, 42% fill, the fills being the ones falling). Today's bar: do not add another reflex-discount pullback long to a downtrend. Require either confirmed strength or a genuine structural reason the de-rating is over.
- Sample caveat: 11 closed trades is below the ~15 noise floor, so this raises the bar; it does not ban a category.

## [06:35 ET] DATA QUALITY — event contracts unavailable today
- `market_data.py events` returned ZERO markets for "Fed decision", "inflation", "FEDDECISION", "recession", "unemployment", "shutdown", "bitcoin". The query "Fed" returned 2 markets, both irrelevant cross-category sports parlays (tennis/football), i.e. the search matched "Federico"/"Federation" not the Federal Reserve.
- CONSEQUENCE: no new event contract can be published today. config/universe.md requires stating the market's implied probability against my own, and I cannot fetch an implied probability. Pitching one from memory would be fabricating a price.
- This also means the two open event ideas awaiting entry (`KXFEDDECISION-26OCT-H25` YES @ 28, `KXCPIYOY-26SEP-T3.5` NO @ 18) cannot be re-priced or updated today. Their levels stand unchanged by default, not by confirmation.
- Event class has 4 tracked ideas and no closed trades, so this gap is also why that lane has no record yet.

## [06:36 ET] THE HOUSE VIEW CONTRADICTS TWO OF ITS OWN LONGS
With the 10y at 5.26% against a 3.88% policy rate, this report is already short the duration complex in four places: XLU short (open), and IYR short / TLT short / ITB short (awaiting entry). ITB is the homebuilder ETF.
- But the book is simultaneously LONG `LCII` (Lippert Components — RV and manufactured-housing components) and LONG `BCC` (Boise Cascade — wood products and building materials). Both are levered to exactly the housing and big-ticket-durable demand that a 5.26% long end suppresses, and that the ITB short is a bet against.
- You cannot be short homebuilders on a rate thesis and long their suppliers on a recovery thesis. One of the two is wrong, and the tape says which: LCII is 1.08% off its 150-day low and -39.4% off its high, below SMA20 (90.27) and SMA50 (98.97). BCC is below SMA20 (76.30) and SMA50 (79.14) and fell 2.40% on 9/30.
- RESOLUTION: keep the rate-duration short view, which the tape confirms daily, and close the two contradicting longs. Logged as position updates below.
- Correlation-cap note: with four duration shorts already live, I am NOT adding a fifth (no XLP short today) even though staples are the cleanest expression. config/strategy.md caps ideas on one driver at 3; the existing book is already over it, which is itself a finding.

## [06:50 ET] POSITION UPDATES — all 14 captured via add_candidate.py
The operative criterion today was **stop quality, not thesis quality**. A position with an honestly-placed working stop is held even when deeply underwater, because its loss is bounded. A position with no stop, or with a stop inside the ATR floor, is closed — regardless of how good the story is.

CLOSE (6):
- **NKE** — sell to close at the open, BEFORE tonight's print. Exit was already decided 9/8 at 38.40 and never filled (placed 8.5% above market); stock fell another 7.8% since. At a 150-day low, no stop, binary event tonight. From the 40.75 entry an honest bear case (28-30, not the 35.155 low it is sitting on) gives 1.98 R:R, failing the 2.5 long_term floor.
- **LULU** — sell to close. Same stale-exit pattern (100.61 from 9/8, unfilled 22 days, 4.6% above market); -16.4%, 0.88% off its 150d low, no stop.
- **LCII** — sell to close. Contradicts the report's own ITB/TLT/IYR/XLU duration shorts; 1.08% off its 150d low, no stop, no catalyst in 12 sessions.
- **BCC** — sell to close. Second half of the same contradiction; thinnest of the four closes and marked as such (only -3.1%, still 14.1% above its low).
- **SNX** — sell to close on the stop floor. 1.38 ATR vs a 2.0 floor; its 2.08 R:R existed only because of that. At an honest 2.0 ATR stop (234.73) R:R is 1.44.
- **DINO** — sell to close on the same floor test. 1.86 ATR vs 2.0; at an honest 97.00 stop R:R is 1.95. Its 128.00 target was also above its own 150d high of 118.39, so the ratio was flattered at both ends. Closed despite being the best-trending name in the book, because the criterion is the process not the trade.

HOLD UNCHANGED (8):
- **PFE** conv 4 — the single best position. Only long above SMA20 AND SMA50, 2.4% off its 150d HIGH, +19.43% 3m vs SPY +2.26% / XLV +5.57%, 3 insider buyers net +2.83M USD, 4 straight EPS beats. R:R 3.62 long_term.
- **XLU short** conv 4 — the best-evidenced view in the report: 10y 5.26% vs 3.88% funds. Stop 2.35 ATR, R:R 2.07. No add (1.05% off its low).
- **CCJ** conv 3 — held where LCII/BCC are closed purely on stop quality: 3.71 ATR, R:R 3.57, and 4.23% above its low rather than printing new ones.
- **CEG** conv 3 — stop 2.30 ATR, R:R 2.18, 11.1% low cushion. Held PROVISIONALLY: I could not establish why it fell 3.99% on 9/30 (see gaps).
- **XLE** conv 3 — stop 2.47 ATR, R:R 2.13. Crude confirms (USO +1.61%) but only refiners followed, so hold with no add.
- **EEM** conv 3 — one of two working longs; stop 2.35 ATR, R:R 2.27, above SMA50.
- **GDX** conv 3 — reluctant hold, bare 1.83 ATR pass vs the 1.8 floor. Now below SMA50 as well as SMA20. Flagged as the first thing to cut tomorrow and as a 3rd-day re-pitch.
- **SVRA** conv 2 — lottery-ticket size, stop 3.28 ATR, liquidity 9.69M USD/day vs the 500K floor. Thinness stated: no dated catalyst verified.

## [06:52 ET] REJECTED / NOT PITCHED — and why
- **XLP short** — cleanest expression of the rate thesis available today (staples broke 1.53% on 9/30 with PEP, STZ, NKE, KHC, MKC all at/near 150d lows), but REJECTED on the correlation cap: XLU short is open and IYR, TLT and ITB shorts are awaiting entry, which is already 4 ideas on one driver against a cap of 3. Adding a 5th would make the report one bet with extra steps.
- **PEP** BUY — rejected. 126.72, only 0.24% off its 150d low, -25.6% off high, below SMA20 (133.38) and SMA50 (137.37). Has a dated catalyst (Oct 8 bmo, est 2.319 EPS / 25.23B rev) but buying it is the exact reflex-discount-into-a-downtrend trade that stopped out CAG on 9/28 and that the 0/6 stock record is made of.
- **STZ** BUY — rejected, same shape. 113.06, 1.36% off its 150d low, -32.9% off high, below SMA20 (120.38) and SMA50 (127.74). Dated catalyst Oct 6 amc.
- **NKE** fresh long into tonight's print — rejected as a NEW idea even though the beat record is 3/3 (+50.2%, +22.9%, +39.2%). A coin flip on a binary event is not an edge. Legitimate as a fresh idea TOMORROW, after the print, with its own levels — re-trading the name once today's close completes is a separate trade, not a duplicate.
- **APLD** — not pitched. 24.37, -52.0% off high, ATR 6.38%, earnings Oct 7 amc (est -0.3098). Interesting asymmetry but I ran out of budget before reading any filing, and a conviction-2 on a 6.4% ATR name with no primary document is not worth the slot.
- **New event contracts** — impossible today, see the 06:35 data-quality block. Cannot state an implied probability I could not fetch.

## [06:54 ET] RESEARCH COMPLETE
- candidates: 14 (6 closes, 8 holds), across 14 distinct symbols, all of them position updates on the existing book
- **The honest headline: there are ZERO new ideas today.** Every one of the 14 is an update to an open position. That is a real shortfall, not a stylistic choice, and synthesis should say so plainly rather than let 14 rows read as 14 fresh opportunities. Two causes, both recorded above: the earnings calendar between Oct 1 and Oct 9 is genuinely empty of large-cap catalysts (Q3 season does not open until Oct 15), and the one clean new expression I found — short the staples/duration complex — was blocked by the correlation cap because the existing book already holds 4 ideas on that driver.
- coverage gaps:
  - **CEG's 3.99% drop on 2026-09-30 is unexplained.** I did not fetch news or filings for it. The hold is provisional on that and it is written into the candidate's key_risk.
  - No news/8-K/filings sweep was run on ANY name today — the budget went to the open-book audit and to levels. No candidate today carries a `primary_document` evidence kind except XLU (FRED series).
  - Short interest unavailable for NKE (nasdaq read timeout); not attempted for others.
  - No crypto idea assessed beyond spot levels (BTC 83,567, ETH 2,681.97, SOL 117.22 from coingecko). The two open bearish BTC ideas awaiting entry (BTC SELL @ 63,400, /MBTU6 SHORT @ 64,340) are now ~24% BELOW spot and are stale — they were not re-examined and should be reviewed or withdrawn tomorrow rather than left sitting.
  - No intraday idea: no 8:30 ET print was identified and the macro calendar was not independently verified by web search.
- sources that failed:
  - `market_data.py macro`: spx, ndx, dow, russell2000, vix, es_futures, nq_futures, dollar_index, us10y_yield, gold, wti_crude ALL failed (finnhub "Market data subscription required for CFD indices" + Yahoo HTTP 429 + stooq 404 + no AlphaVantage key). Index and VIX levels today are read through ETF proxies only; DXY through UUP.
  - `market_data.py events`: returned 0 markets for "Fed decision", "inflation", "FEDDECISION", "recession", "unemployment", "shutdown", "bitcoin", "CPI"; the query "Fed" matched only irrelevant sports parlays. Event-contract lane is dark today.
  - `market_data.py short NKE`: nasdaq read timeout after 20s.

## [06:57 ET] CONVICTION — five scores are deliberately BELOW what the evidence count supports
Validation will flag these as under-claimed rather than inflated; that is intentional and should not be "corrected" upward:
- PFE (4 kinds, supports 5, set 4), NKE (4 kinds, supports 5, set 4), XLU (4 kinds, supports 5, set 4), XLE (3 kinds, supports 4, set 3), SVRA (2 kinds, supports 3, set 2).
- Reason: the distinct-kind count is a ceiling on what the evidence can bear, not a floor I am obliged to claim. SVRA in particular — its `positioning` entry is a liquidity measurement, which is the weakest thing that kind can hold, and the thesis has no dated catalyst and no document, so a 3 would overstate it. The other four are held one notch down because each carries a stated unanswered weakness (PFE: deteriorating revisions; NKE: closing into a 3/3 beat record; XLU: over the correlation cap; XLE: only refiners confirmed).
- The red team lowers conviction and does not raise it, so under-claiming is the safe direction. The nine remaining rows match their evidence count exactly.
