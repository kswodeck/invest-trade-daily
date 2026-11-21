# Research log — 2026-11-21

## [06:03 ET] SETUP — Saturday run, week-ahead framing
- US equities and futures closed. Freshest honest equity price = Fri 2026-11-20 close.
- Per config/strategy.md weekend behavior: shift toward crypto + event contracts for
  actionable ideas; equities are week-ahead prep (horizon swing, entry at next open).
- Budget: started 06:01 ET, ~60 min. Minute-20 hard deadline 06:21. 70% stop-new-research 06:43.

## [06:03 ET] PRIOR CONTEXT — the track record is now signal, not noise
- 45 closed trades. Overall 5/45 hit target (11%), avg -5.8%. Above the ~15 threshold,
  so this is NOT a noise sample and must change today's bar.
- By asset class: stock 2/31 (6%), avg -7.6% <- the worst and the biggest book.
  etf 3/14 (21%), avg -1.9% <- the best. crypto/event/futures: no closed trades.
- By conviction: 2 -> 0/7, avg -10.1%. 3 -> 3/29 (10%), avg -6.4%. 4 -> 2/9 (22%), avg -0.4%.
  Conviction 2 has never worked here. RAISING THE BAR: no conviction-2 equity longs today
  unless the evidence is genuinely a 3+ and I am scoring it honestly low.
- 17 open positions, 16 of them long equity/ETF, 1 short (IWM). The single short is the
  only green-ish recent add (+2.3%). The book is structurally long-only into a tape that
  has been punishing longs: ONON -9.9%, DKS -5.8%, XLV -3.5%, RTX -2.8%, ADM -2.4%.
- CONCLUSION for today: the failure mode is not idea selection, it is DIRECTION and
  CROWDING. Default to very few new ideas, favour position management, and prefer
  non-equity expressions (crypto futures, event contracts) that do not add to a long book.

## [06:08 ET] MACRO — Friday 2026-11-20 was a tech-led liquidation day
All figures = Friday 2026-11-20 official close via finnhub (market closed, age ~842 min).
| ETF | Close | Open | High | Low | Chg |
| --- | --- | --- | --- | --- | --- |
| SPY | 689.81 | 713.56 | 718.29 | 686.75 | -3.64% |
| QQQ | 608.45 | 638.84 | 643.28 | 606.23 | -5.67% |
| XLK | 149.01 | 158.71 | 159.01 | 148.09 | **-7.27%** |
| IWM | 256.61 | 263.32 | 265.85 | 256.32 | -2.88% |
| GLD | 322.87 | 326.98 | 328.60 | 320.95 | -3.67% |
| TLT | 81.45 | 80.74 | 81.71 | 80.69 | **+1.37%** |
| XLP | 90.46 | 90.93 | 92.03 | 90.32 | **+0.67%** |
| XLV | 177.24 | 179.00 | 180.64 | 176.71 | -0.12% |
| XLE | 60.51 | 60.71 | 61.50 | 60.34 | -0.62% |
| XLF | 54.57 | 55.68 | 56.03 | 54.43 | -1.82% |
- source: python scripts/market_data.py quote (finnhub), 2026-11-21T11:0x UTC
- SHAPE OF THE MOVE: reversal from a higher open (SPY opened +0.0 vs prev but ran to
  718.29 then closed at 689.81 = closed 4.0% off the high, on the low). Tech-led:
  XLK -7.27% is a two-standard-deviation-plus sector day. Staples UP, long bonds UP,
  healthcare flat = textbook risk-off rotation, not an indiscriminate selloff.
- GLD -3.67% alongside the equity drop is the tell for FORCED LIQUIDATION / margin,
  not a growth scare: in a pure growth scare gold rallies with bonds.
- RATES (FRED, 2026-11-19/20): 10y 5.04% (prev 5.07), 2y 4.76% (prev 4.80),
  fed funds 3.88%, 10y-2y +0.29 (prev +0.28). Curve positively sloped and steepening
  slightly; 10y at 5.04% is restrictive and is the backdrop for a tech de-rating.
- CPI index (CPIAUCSL) Oct 337.476 vs 336.298 = +0.35% m/m, hot. Unemployment 4.1%
  (prev 4.2%). So the Fed has no cover to cut quickly -> duration-sensitive growth
  multiples are the pressure point. This is consistent with XLK being the epicentre.
- FAILED SOURCES: Yahoo returned 429 (rate-limited) for every index symbol, so ^GSPC,
  ^NDX, ^VIX, ^DXY, ^RUT, ES/NQ futures, gold and WTI futures all unavailable this run.
  **No VIX level fetched -> I will not state one.** ETF proxies above are used instead.

## [06:05 ET] NEWS — what drove Friday: the AI capex trade is unwinding
- Nasdaq Composite -5.28% to 22,617.73, erasing ALL of its 2026 gains. S&P 500 -3.7%
  to 6,910.39. Dow only -1.93% to 48,147.33. Dow/Nasdaq spread of 335bp in one session
  is a rotation, not a liquidation of everything.
  - source: https://www.upi.com/Top_News/US/2026/11/20/stocks-dow-jones-nasdaq-correction-territory/1061795214998/
- Dow and S&P 500 have entered **correction territory** (>10% off highs). same source.
- NVDA: Reuters reports the SEC is probing Nvidia over its **accounting practices**.
  NVDA -13/14% Friday, and **-47.5% from its 2026-10-06 peak, ~$2.7T of market cap gone**.
  - source: https://www.tradingkey.com/analysis/stocks/us-stocks/262316111-nasdaq-falls-ai-stock-selloff-nvidia-sec-probe-tradingkey
- Nasdaq lost >$4 trillion of market value over five sessions (WSJ via secondary).
- Anthropic IPO debuted Friday and FELL 8.5% after an initial gain — the marginal buyer
  for new AI supply is gone. That is the cleanest read on sentiment available.
  - source: https://www.cnn.com/2026/11/20/investing/us-stocks-anthropic-ai
- Named drivers per Richard Saperstein (Treasury Partners): slowing datacenter buildouts,
  reduced funding sources for AI projects, slower tech earnings growth trajectory.
- VALUATION ANCHOR: S&P 500 info-tech sector forward P/E entered Friday at its
  **lowest level since March 2020** (FactSet, via CNN/secondary). This is the first
  genuine valuation argument for tech in this cycle and it cuts against chasing shorts.

## [06:05 ET] REGIME READ — my working frame for today
- This is a crowded-trade unwind in AI/semis, not (yet) a macro recession trade:
  staples +0.67%, long bonds +1.37%, healthcare -0.12%, energy -0.62% all held up while
  XLK lost 7.27%. Credit/macro stress would not spare XLP and XLV.
- But GLD -3.67% says there IS a funding/margin component. Gold does not fall 3.7% with
  bonds up on a pure growth scare. Forced de-risking across books.
- IMPLICATION: shorting tech here is late (NVDA already -47.5%, tech P/E at a 6-year low)
  and buying it is early (no sign the capex revision cycle has finished). The honest
  trade is NEITHER. I will not chase either side of semis today.
- The actionable lanes on a Saturday after a day like this: crypto (24/7, already
  repriced, and shortable via futures), event contracts on the macro path, and
  defensive/week-ahead equity levels. Plus managing 17 open longs that just got hit.

## [06:06 ET] DATA GAP — event contracts unusable today, so none are recommended
- `market_data.py events "<topic>"` returned count 0 for Fed, interest rate, recession,
  CPI, inflation, Bitcoin, Nasdaq, S&P. Cause found: the helper pulls ONE unsorted
  200-market page from Kalshi and filters client-side, so the needle is matched against
  an arbitrary slice of thousands of open markets. Not a market-availability finding.
  (Worth a fix + test in scripts/market_data.py; out of scope for the research phase.)
- Worked around it by querying Kalshi directly. The series exist and are relevant:
  KXFED (fed funds upper bound by meeting), KXEMERCUTS (emergency cuts), KXNBERRECESSQ
  (next recession start), KXRATECUTS, KXFEDDISSENT.
- **But every one of 200 KXFED markets returned yes_bid/yes_ask/last_price/volume/
  open_interest = null**, as did KXEMERCUTS and KXNBERRECESSQ. No price data from the
  public endpoint this run, and no Dec-2026 Fed meeting market in the open set at all.
- CONSEQUENCE: universe.md requires an event-contract idea to state the market's implied
  probability against mine, and strategy.md forbids stating a number I did not fetch.
  **So zero event contracts today.** On the day a violent macro repricing made this the
  single most interesting lane, which is a real cost — recorded, not papered over.

## [06:06 ET] OPEN POSITIONS — repriced to Friday 2026-11-20 close (finnhub)
prior_context.md was built on Thursday's closes, so every line below is worse than it
reads there. Friday's -3.6% SPY day has NOT been reflected in the inherited table.
| Sym | Entry | Target | Stop | Fri close | Fri low | % vs entry | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PFE | 27.6 | 42.0 | none | 27.40 | 27.35 | -0.7% | hold |
| KHC | 23.0 | 28.09 | 21.2 | 25.39 | 25.25 | +10.4% | working, +1.9% Fri |
| OXY | 54.0 | 62.0 | 50.15 | 53.90 | 53.35 | -0.2% | hold |
| HII | 262.0 | 339.76 | none | 280.34 | 279.80 | +7.0% | hold |
| UNP | 288.6 | 315.99 | 277.4 | 287.29 | 286.37 | -0.5% | hold |
| ABT | 103.0 | 117.34 | 97.0 | 103.00 | 102.80 | +0.0% | hold |
| PYPL | 56.5 | 62.7 | 54.1 | 53.29 | 53.10 | -5.7% | **STOP BREACHED Fri (low 53.10 < 54.10)** |
| RTX | 199.0 | 226.5 | 186.0 | 190.17 | 189.58 | -4.4% | 2.0% above stop |
| XLU | 43.3 | 46.6 | 41.8 | 42.69 | 42.63 | -1.4% | hold |
| ONON | 34.2 | 41.41 | 30.69 | 29.97 | 29.91 | -12.4% | **STOP BREACHED Fri (low 29.91 < 30.69)** |
| TLT | 80.3 | 84.3 | 78.8 | 81.45 | 80.69 | +1.4% | working, +1.4% Fri |
| XLV | 184.0 | 201.0 | 176.0 | 177.24 | 176.71 | -3.7% | 0.7% above stop |
| HUN | 9.0 | 10.82 | 8.09 | 8.36 | 8.36 | -7.1% | 3.2% above stop, closed ON its low |
| ADM | 68.8 | 78.0 | 64.4 | 66.95 | 66.64 | -2.7% | hold |
| DKS | 144.5 | 175.5 | 129.0 | 132.25 | 131.66 | -8.5% | 2.5% above stop |
| CAG | 14.4 | 19.48 | none | 14.92 | 14.86 | +3.6% | working, +1.6% Fri |
| IWM | 270.5 (short) | 238.69 | 284.5 | 256.61 | 256.32 | **+5.1% in favour** | the one winner |
- PYPL and ONON both traded through their stops on Friday. They are closed trades as of
  2026-11-20 and grading will record them; I am NOT re-pitching either.
- PATTERN, and it is the useful part: everything working is defensive/anti-cyclical —
  KHC +10.4%, CAG +3.6%, TLT +1.4%, and the IWM SHORT +5.1%. Everything losing is
  cyclical/consumer/industrial — ONON, DKS, HUN, RTX, XLV, ADM. The book is positioned
  for a cycle that is not happening, and Friday widened the gap rather than closing it.

## [06:08 ET] POSITION UPDATE — IWM SHORT — opened 2026-11-18 @ 270.5, +5.1%
- decision: COVER HALF at Monday's open (~256.61), hold half on the ORIGINAL 284.5 stop.
- why: IWM closed at the lowest close of the 120-day window, on the low, 2.2x volume
  (57.46M vs 26.1M avg) — momentum intact. BUT relative strength has flipped against the
  short: IWM -7.25% 1m vs SPY -9.71% (outperforming by 2.46pp). Friday's weak leg was
  mega-cap tech (XLK -7.27%) not small caps (-2.88%). Forward R:R from 256.61 is only
  0.64:1 (17.92 to target vs 27.89 to stop) even though it is 2.27:1 from entry.
- why NOT tighten the stop: on a 270.5 entry, any stop tight enough to protect the gain
  sits inside 0.5 ATR of entry and lifts the printed ratio to ~17:1 while making the trade
  strictly worse. That is the KRE anti-pattern in CLAUDE.md verbatim. Half off instead.
- action: captured via add_candidate.py, conviction 4, size cut to 1.5%.

## [06:08 ET] POSITIONS — the four near their stops, and why I am NOT widening any stop
| Sym | Fri close | Stop | Headroom | Decision |
| --- | --- | --- | --- | --- |
| XLV | 177.24 | 176.00 | +0.7% | HOLD stop. Likely stops Monday on any weakness. |
| RTX | 190.17 | 186.00 | +2.2% | HOLD stop. |
| DKS | 132.25 | 129.00 | +2.5% | HOLD stop. |
| HUN | 8.36 | 8.09 | +3.2% | HOLD stop. Closed ON its low Friday. |
- Widening a stop on a losing position to avoid taking the loss is the single most
  expensive habit available and none of these four has NEW information justifying it —
  only an adverse price move, which strategy.md says is not an invalidation. XLV is the
  closest call, because healthcare was the best-relative sector Friday (-0.12% vs SPY
  -3.64%) and the defensive thesis is working in relative terms. It is still a no: the
  stop was set where the thesis was wrong and 176.00 has not moved.
- PYPL (-5.7%) and ONON (-12.4%) already traded through their stops on Friday and are
  closed. Not re-pitched — nothing about either thesis improved, and ONON at -12.4% in
  10 days was a conviction error, not an execution one.

## [06:08 ET] STALE PENDING ORDERS — two levels that can no longer fill
- `GLD` SELL @ 406.77 (published 2026-10-25). GLD closed Friday at **322.87**, i.e. the
  short entry sits **26.0% ABOVE** the market after gold fell to it instead of rallying
  into it. This level is dead and should be withdrawn, not carried forward as "awaiting
  entry" — a 26%-away short reads as a live idea on the sheet and is not one.
- `/MBTZ6` SHORT @ 74075 (published 2026-11-09). Bitcoin is **57,822** right now, 21.9%
  BELOW the short entry. Same failure mode, same conclusion: the trade was right in
  direction and never filled because the entry was above the market and price left.
  WITHDRAW. This is the pullback-entry problem in strategy.md running in reverse.
- `CVS` BUY @ 77.5 — CVS closed 80.84, still 4.3% above the entry. Level unchanged, alive.
- `LEN` BUY @ 79.5 — LEN closed 80.74, 1.5% above. Friday low 80.55. Alive, close.

## [06:10 ET] MACRO CORRECTION — the Fed is expected to HIKE in December, not cut
This overturns the frame I was carrying two entries ago and is the most important
finding of the run. Correcting it explicitly rather than quietly.
- CME FedWatch has ~**78% odds of a further 25bp HIKE at the December meeting**.
  Minutes of the October FOMC showed almost all officials thought further rate
  increases would likely be appropriate.
  - source: https://beincrypto.com/why-is-gold-price-falling-november-2026/
  - source: https://www.kitco.com/news/article/2026-11-19/gold-falls-below-3650-silver-tumbles-fed-rate-concerns-pressure-metals
- Dollar reported at a **19-month high**; yields high (10y 5.04%); CPI +0.35% m/m in Oct.
- WHAT I GOT WRONG EARLIER: at 06:05 I wrote that GLD -3.67% implied a one-day forced
  liquidation and that a correction makes a "dovish Fed pivot" more likely. Both wrong.
  Gold is not having a bad day, it is in a **bear market**: GLD 365.17 (11-11) -> 322.87
  (11-20) = **-11.6% in 7 sessions**, **-24.8% from the 120-day high of 429.42**, closed
  at a 120-day low, with SMA20 at 360.42 and SMA50 at 374.90 far ABOVE price. Spot gold
  is reported near $3,500-3,600, a 14-month low, worst week since March.
  - source: https://www.kitco.com/news/article/2026-11-20/gold-falls-toward-3500-silver-slides-stock-markets-enter-correction
  - source: https://finance.yahoo.com/markets/commodities/articles/gold-falls-14-month-low-124723754.html
- THE COHERENT REGIME, which explains every move in one mechanism: inflation is
  re-accelerating, the Fed is expected to keep HIKING, the dollar is at a 19-month high
  and real yields are rising. Every long-duration asset is de-rating at once —
  mega-cap tech (XLK -7.27%), gold (-24.8% from high), crypto (BTC -21.9% from 74k).
  That is not three stories, it is one discount-rate story.
- Corollary that matters for every idea today: **this is a rising-real-rate regime, not a
  risk-off flight-to-quality**. The haven bid is in the DOLLAR, not in gold and not
  reliably in duration. Anything whose thesis needs the Fed to ease is wrong today.
- CAVEAT ON SOURCING: the 78% figure reaches me through secondary commentary
  (beincrypto, kitco) citing CME FedWatch, not from FedWatch itself, and the search tool
  flagged some of these as low-quality. Verifying next before any idea leans on it.

## [06:11 ET] MACRO VERIFIED — dated catalyst: FOMC 2026-12-08/09, a HIKE is ~95% priced
- Current target range **3.75%-4.00%** (consistent with the FRED DFF print of 3.88%).
  The last move was a **12-0 quarter-point HIKE on 2026-09-16**. This is a hiking cycle.
- CME FedWatch at the 2026-11-17 close: **~95% odds of a 25bp hike at the Dec 8-9
  meeting**, remainder priced on a 50bp move. A 2026-11-19 report gives 95.7% for 25bp
  and 4.3% for 50bp.
  - source: https://247wallst.com/investing/2026/11/18/traders-now-see-a-95-chance-the-fed-hikes-rates-in-december/
  - source: https://en.sedaily.com/society/2026/11/19/us-dec-rate-hike-odds-at-957-percent-as-fed-resists-bigger
- Fed speakers split on SIZE, not direction: NY Fed's Williams has **ruled out** 50bp;
  Governor **Waller has opened the door to 50bp**. So the distribution is 25bp with a
  live upside tail, and essentially no probability of a cut.
- Labour market gives them cover: October payrolls **+165,000**, unemployment 4.1%
  (down from 4.2%). October CPI was hot. There is no recession in the data.
  - source: https://www.fool.com/investing/2026/11/16/theres-now-100-chance-fed-rate-hike-in-december-thats-not-worst-news-for-wall-street/
- DATED CATALYST for the report: **2026-12-09 14:00 ET FOMC decision**, ~12 sessions out.
- SOURCING NOTE: these are secondary reports of CME FedWatch, dated 11-16 to 11-19, i.e.
  BEFORE Friday's correction. Friday's rout may well have moved the December pricing and
  I have no post-Friday read. Any idea leaning on this must treat ~95% as a pre-Friday
  number. I will not claim a live probability I did not fetch.

## [06:11 ET] HOW THE REGIME CHANGES THE BOOK
- **Confirms** the IWM short: a December hike hits small caps hardest (most floating-rate
  debt, least pricing power). My first IWM capture named a "dovish pivot squeeze" as the
  main risk — at 95% priced for a hike that risk is much smaller than I wrote. Revising.
- **Argues against** the TLT long (entry 80.3, now 81.45) on the inflation leg: hot CPI
  plus a hiking Fed plus a 10y-2y curve steepening to +0.29 all point to higher long
  yields. BUT it is defensible as the book's only policy-mistake hedge — hiking into a
  correcting equity market with a 19-month-high dollar is how a growth scare starts, and
  that rallies the long end. Two-sided. DECISION: hold, no change, flag the conflict.
- **Kills** any idea needing easier policy: gold long, high-multiple growth, duration.
- **Favours** the dollar, which is where the haven bid actually went, and cash-generative
  short-duration value. Checking the dollar expression next.

## [06:13 ET] EVENT CONTRACTS RECOVERED — live Dec FOMC orderbook, fetched 2026-11-21
Earlier I logged the event lane as unusable. Partly wrong, and worth correcting: the
/markets endpoint returns null for yes_bid/yes_ask/last_price/volume, but
`/markets/<ticker>/orderbook` DOES return resting depth. Best YES bid = top of
`orderbook_fp.yes_dollars`; best YES ask = 100 - top of `no_dollars`.
Series `KXFEDDECISION`, Dec 8-9 2026 meeting, fetched live this morning:
| Market | Outcome | YES bid | YES ask | Depth at top of book |
| --- | --- | --- | --- | --- |
| KXFEDDECISION-26DEC-H0 | Hike 0bps (pause) | 8c | **9c** | $33,934 on the NO side |
| KXFEDDECISION-26DEC-H25 | Hike 25bps | 89c | 90c | $76,384 / $141,543 |
| KXFEDDECISION-26DEC-H26 | Hike >25bps (50bp) | 2c | 3c | $104,549 / $146,629 |
| KXFEDDECISION-26DEC-C25 | Cut 25bps | — | ~1c | $1,107,847 on NO |
- Internally consistent: asks sum to ~103, bids to ~99. Real two-way book, not a stub.
- **THIS IS POST-FRIDAY PRICING** and it is the only post-crash macro read I have.
  Against the pre-Friday FedWatch figures (95.7% for 25bp, 4.3% for 50bp, ~0% pause):
  - 25bp hike: 95.7% -> **89-90%**
  - pause:     ~0%   -> **8-9%**
  - 50bp hike:  4.3% -> **2-3%**
- READ: Friday's correction has moved December pricing, and in a specific shape. The
  market has not started pricing cuts — it has started pricing a PAUSE, and has taken
  the 50bp tail off the table. The hiking bias is intact but the distribution has
  shifted toward "the Fed stops" rather than "the Fed reverses". That is exactly what
  you would expect from a financial-conditions shock landing on top of hot inflation.

## [06:17 ET] VENUE CHECK — the Dec FOMC contract is genuinely on Robinhood
- Robinhood's own event page lists it, Kalshi-backed (KalshiEX LLC via Robinhood
  Derivatives), event day 2026-12-09, payout ~1 hour after resolution, $1 per winning
  contract. Prices from that page this morning: maintain **10c**, hike 25bp 89c,
  hike >25bp 5c, cut 25bp 3c, cut >25bp 2c.
  - source: https://robinhood.com/us/en/prediction-markets/economics/events/fed-rate-decision-in-december-dec-09-2026/
- FEE WARNING, and it is material at a 10c entry: the trade panel displayed "$0.00
  commissions and fees" but the About section says additional fees apply, and
  Robinhood's prediction-markets launch carried 2c per contract (1c to Kalshi, 1c to
  Robinhood). A 1-2c round trip moves break-even from 10% to 11-12%. Flagged in key_risk.
- Captured: BUY YES "Fed maintains rate" @ 10c, target 25c, stop 4c, 1.5% size.
  Edge asserted is 5 points (my ~15% against the market's 10%), deliberately modest.

## [06:17 ET] CORRELATION CHECK — my first two ideas share ONE driver. Cap reached at 2.
- I initially read the IWM short and the Fed-pause contract as opposing bets (one needs
  a hike, the other a pause). That is wrong. Both pay off on **"the correction
  continues"**: if equities keep falling, IWM falls AND the pause probability reprices
  higher. If equities stabilise over the next fortnight, IWM bounces AND the pause
  contract decays to 4c. Same driver, two expressions.
- strategy.md caps this at 3 ideas per driver. So I have ONE slot left on
  "correction continues" and I am not going to spend it — any further idea today must
  rest on a genuinely different driver or it is one bet with extra steps.
- This also kills several things I was about to look at: short /MNQ, short /MES, short
  semis. All of them are the same trade as the IWM short in a different wrapper.

## [06:18 ET] REVISING THE IWM CAPTURE — my first key_risk was mis-weighted
- The first IWM capture named a "dovish Fed pivot squeeze" as the dominant risk. With
  the December meeting priced at 89% hike / 10% pause / 0-3% cut, a pivot is close to
  unpriceable inside this horizon, so that was the wrong risk to headline.
- The REAL risk to the short is plainer: IWM is 15.9% off its high and already
  outperforming SPY by 2.46pp on 1m, so it is the most mean-reversion-prone leg of the
  market, and a bounce does not need the Fed at all.
- Re-capturing with that corrected. Keeping conviction at 4 (3 distinct evidence kinds)
  and NOT adding the Dec 9 FOMC as a 4th kind: it is the same driver already carrying
  the Fed idea, and the rates/small-cap link is a mechanism I reasoned to rather than a
  confirmation I measured. Promoting this to a 5 would put a position I am half-closing
  at the top of the report, which is the conviction inflation strategy.md warns about.

## [06:24 ET] CALENDAR — dated events inside the horizon (fetched finnhub calendar)
Next week is holiday-shortened: Thanksgiving Thu 2026-11-26 (closed), Fri 11-27 half day.
- **2026-11-23 (Mon)**: DKS, ANF, BURL, KSS, GES retail cluster; HPE (amc)
- **2026-11-24 (Tue)**: ADI (bmo), BBY (bmo), DELL (amc), HPQ (amc), ADSK, WDAY, MDT, NTNX
- **2026-11-25 (Wed)**: DE (bmo). Also **PCE price index 08:30 ET** — carried forward from
  this report's own 2026-11-20 edition, which flagged it as a two-sided event.
- **2026-12-01**: MRVL, CRDO, CRWD, MDB, OKTA, DLTR, FIVE, PVH
- **2026-12-02**: CRM, SNOW, ZS, KR
- **2026-12-03**: ULTA, DG, M, DOCU, VEEV, SAIC
- **2026-12-07**: TOL (amc), OLLI, ASO, GME
- **2026-12-08/09**: FOMC decision, 14:00 ET on the 9th
- READ: DELL (11-24 amc), ADI (11-24 bmo), then MRVL + CRDO (12-01) are the first hard
  reads on AI datacenter demand AFTER the crash. They will settle the "capex is rolling
  over" question rather than leaving it to narrative. I am deliberately NOT trading them:
  every one of those is the same "correction continues" driver I am already at 2/3 on,
  and going into a binary print on a crowded thesis is how the NVDA long died on 11-10.

## [06:24 ET] POSITION UPDATE — DKS — opened 2026-11-13 @ 144.5, now 132.25, -8.5%
- decision: **CLOSE before Monday's print.** Captured via add_candidate.py.
- why, and it is an arithmetic reason rather than a view: ATR14 is 6.81 = **5.15% of
  price**, and the 129.00 stop sits **0.48 ATR** below Friday's close. A beaten-down
  retailer reporting Q3 gaps 10-20% routinely, so the stop is a level the stock trades
  THROUGH, not one it stops at. The position's real risk is therefore uncapped by
  anything except where it reopens — that is not a risk-controlled position.
- supporting: -45.9% from the 120-day high of 244.38, SMA20 143.02 and SMA50 138.18 both
  overhead, closed 132.25 vs a 131.655 low. The 2026-11-15 plan was to trim half into
  this print and the stock has lost a further 8.5% since, removing that plan's cushion.
- the earnings date is corroborated twice: the fetched finnhub calendar AND this report's
  own 2026-11-15 edition. Timing within the day is NOT confirmed (hour field blank), so
  Monday's open is treated as the risk point.
- followed the existing repo convention for an exit (BCC, 2026-11-18): levels unchanged,
  risk_reward null, "CLOSE THE POSITION" as the operative instruction in catalyst.action.

## [06:19 ET] RISK SWEEP — every open position's stop measured in ATRs from its entry
No open position other than DKS reports earnings inside the next 16 days (checked against
the fetched finnhub calendar), so DKS was the only event-risk case in the book.
| Sym | Close | ATR14 | ATR% | Stop | ATR from entry | Floor | Headroom | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PFE | 27.40 | 0.77 | 2.82 | none | n/a | n/a | n/a | no stop by design (long-term) |
| KHC | 25.39 | 0.79 | 3.11 | 21.20 | 2.28 | 2.0 | 16.5% | OK, best position in the book |
| OXY | 53.90 | 1.85 | 3.43 | 50.15 | 2.08 | 2.0 | 7.0% | OK |
| HII | 280.34 | 11.75 | 4.19 | none | n/a | n/a | n/a | no stop by design |
| UNP | 287.29 | 7.54 | 2.62 | 277.40 | **1.49** | 2.0 | 3.4% | **stop below policy floor** |
| ABT | 103.00 | 3.06 | 2.97 | 97.00 | **1.96** | 2.0 | 5.8% | marginally below floor |
| RTX | 190.17 | 5.86 | 3.08 | 186.00 | 2.22 | 2.0 | 2.2% | OK, near stop |
| XLU | 42.69 | 0.64 | 1.50 | 41.80 | 2.35 | 1.8 | 2.1% | OK, near stop |
| TLT | 81.45 | 0.78 | 0.96 | 78.80 | 1.91 | 1.8 | 3.3% | OK |
| XLV | 177.24 | 3.88 | 2.19 | 176.00 | 2.06 | 1.8 | **0.7%** | OK but AT the stop |
| HUN | 8.36 | 0.39 | 4.71 | 8.09 | 2.31 | 2.0 | 3.2% | OK |
| ADM | 66.95 | 2.19 | 3.27 | 64.40 | 2.01 | 2.0 | 3.8% | OK |
| CAG | 14.92 | 0.55 | 3.66 | none | n/a | n/a | n/a | no stop by design |
- UNP (1.49 ATR) and ABT (1.96 ATR) were published with stops that do NOT clear the
  current policy floor, so both can stop out on an ordinary two-session move — the exact
  failure CLAUDE.md records as having caused all ten of the first month's stop-outs.
- **DECISION: do not widen either stop.** Amending a filled position's exits is permitted,
  but using a rule that exists to REJECT too-tight stops as a licence to LOOSEN a live
  one inverts its purpose and adds risk after the fact. Both positions are near flat
  (UNP -0.5%, ABT 0.0%), so the cost of being stopped is small; the lesson belongs at
  publication time, not here. Flagged, held, no change. Same answer for XLV at 0.7%
  headroom, RTX at 2.2% and XLU at 2.1% — all hold at published levels.
- DKS was the one position where the stop was non-functional AND a binary event was one
  session away. That combination, not the tightness alone, is why DKS is the only close.

## [06:20 ET] REJECTED — UUP (dollar long) — real trend, not enough reward per unit of risk
- UUP 29.62, within 0.15% of its 120-day high (29.665), above SMA20 29.23 and SMA50 28.96,
  and it did not even flinch on Friday (29.63 -> 29.62). Cleanest uptrend on the board and
  the regime (19-month-high dollar, hiking Fed) is behind it.
- But ATR14 is 0.1293 = **0.44% a day**. An ETF-compliant 1.8 ATR stop is 0.23 wide, so a
  2.0 R:R target is 30.09 — **+1.6% of upside**. Not worth a position slot at any size
  strategy.md permits, and the entry would be at a 120-day high.
- Second and better reason to reject: a long dollar is substantially the OPPOSITE side of
  the Fed-pause contract I already captured. If the Fed pauses, the dollar falls. Holding
  both is paying two spreads to hold a hedge, not an edge.

## [06:20 ET] CREDIT TELL — banks at lows say this is not only a multiple story
- XLF 54.57, -9.11% off high, below SMA20 57.19 AND SMA50 55.87; fell five straight
  sessions 58.18 -> 54.57.
- KRE 68.32, -12.8% off high and only **0.78% above its 120-day low** of 67.79.
- This matters for interpretation: a hiking Fed with a steepening curve should be good for
  bank net interest margin. Banks making new lows instead says the market is pricing
  credit, not margin. Together with gold -24.8% and a 19-month-high dollar, that is a
  funding/deleveraging signature rather than a pure AI-valuation one. It reinforces
  "correction continues" — which is exactly why I am NOT adding a third idea to it.

## [06:26 ET] REJECTED — energy — Friday's "resilience" was a one-day artifact
- I flagged XLE -0.62% at 06:08 as a sector holding up. Looking at the trend, that is wrong
  and I am correcting it: XLE 60.51 is **-13.74% off its 120-day high**, BELOW both SMA20
  (64.61) and SMA50 (64.70), and fell five sessions running 63.69 -> 63.36 -> 61.29 ->
  60.89 -> 60.51. It is a downtrend that happened to fall less than tech on one day.
- USO 139.63 likewise -18.73% off high, below SMA20 150.11 and SMA50 151.67.
- No long here, and no short either — the move is mature and OXY is already in the book.

## [06:26 ET] REJECTED — crypto — the only live market, and nothing tradeable in it
- Live now (coingecko, 2026-11-21): BTC **57,822 (-6.67% /24h)**, ETH 1,638.18 (-6.61%),
  SOL 68.06 (-5.90%), XRP 0.8956 (-6.80%), DOGE 0.052989 (-7.32%), AVAX 6.37 (-7.83%),
  LTC 38.59 (-6.93%), LINK 8.37 (-5.62%), ADA 0.1392 (-6.51%). Uniformly down 5.6-7.8%,
  i.e. one beta, nine tickers — there is no dispersion to pick from.
- IBIT closed Friday 33.02, **-33.14% off its 120-day high** of 49.39, SMA20 41.34 and
  SMA50 44.57 far above, ATR 4.69%/day, down six sessions 38.94 -> 33.02. BTC has fallen
  a further 6.67% since that close, so IBIT gaps down Monday.
- A short is late: BTC is already 21.9% below the 74,075 level this report wanted to short
  on 2026-11-09. A long is a knife-catch in the regime least kind to zero-cashflow
  long-duration assets. Crypto is also the SAME driver as the two ideas I already hold.
  Nothing captured.
- **WITHDRAW `/MBTZ6` SHORT @ 74075** (published 2026-11-09, never filled). The direction
  was right and the fill never came because the entry sat above the market and price left
  without it. A resting short 21.9% above spot is not a live idea and should not read as
  one on the sheet. Not re-pitched at a lower level — see "late" above.
- **WITHDRAW `GLD` SELL @ 406.77** (published 2026-10-25, never filled). Same failure mode,
  further gone: GLD closed 322.87, so the entry is 26.0% above the market.

## [06:27 ET] PENDING ORDER DECISIONS — LEN cancelled, CVS left standing
- **LEN BUY @ 79.50 — CANCEL.** Captured. Published 2026-11-13, missed filling by 0.185 on
  11-19 (low 79.685). A homebuilder long is a leveraged bet on rate relief and the Dec 8-9
  meeting is priced **89% hike / 10% pause / 0-3% cut**, with the 10y at 5.04% and CPI
  +0.35% m/m — the premise has inverted since publication. Portfolio reason is the stronger
  one: today's Fed-pause contract at 10c is the same rate-relief view with a defined loss
  and no equity beta, so keeping LEN pays twice for one thesis through the worse vehicle.
  LEN was also recommended 2x in ten days; cancelling stops the re-litigation.
- **CVS BUY @ 77.50 — LEAVE STANDING, unchanged, and NOT re-pitched.** CVS closed 80.84,
  only 4.1% above the entry, so the accumulation plan is working as designed (long_term,
  no stop by intent, accumulate in thirds). It is -26.96% off its 120-day high of 110.68
  and 4.54% above the 120-day low, falling 89.35 -> 80.84 in six sessions with a 4.84%
  ATR. Two honest caveats recorded rather than buried: CVS was already STOPPED OUT once
  (opened 10-16, stopped 11-04) before being re-framed as a long-term hold, and it has
  been published repeatedly. I am not capturing a fourth pitch — the level is unchanged
  and there is no new information, so re-stating it would be anchoring, not conviction.
  Pharmacy/benefits cash flows are short-duration and fit a rising-real-rate regime, which
  is why the level stands rather than being cancelled like LEN.

## [06:29 ET] CATALYST SEQUENCE VERIFIED — 11-25 PCE is the last inflation read before Dec 9
- October PCE price index: **2026-11-25 08:30 ET**. BEA's own PCE topic page lists
  "Current release: October 29, 2026 — Next release: November 25, 2026".
  - source: https://www.bea.gov/taxonomy/term/716
- November CPI: **2026-12-10**. Next PCE: **2026-12-23**. BOTH are AFTER the Dec 8-9 FOMC.
- So the Fed decides on Dec 9 having seen the Nov 25 PCE as its **last major inflation
  print**. That is a precise and useful fact: the pause case has exactly one clean
  opportunity to be priced in, four sessions from now, with no later data to reverse it
  before the meeting. Re-captured the Fed contract with this as the near catalyst and
  with the hot-PCE scenario named as the concrete way the trade dies.
- Carried into the IWM short too as a two-sided event, consistent with this report's own
  2026-11-20 edition which already flagged 11-25 PCE that way.

## [06:29 ET] INSIDERS — checked six equity names; one real cluster, and it is not new
- **PFE: 3 open-market buys, 3 distinct buyers, $2.96M bought vs $135K sold (net +$2.83M).**
  CEO Albert Bourla 38,000 sh @ 26.34 on 2026-08-12; director Mortimer Buckley 37,632 sh
  @ 25.52 and director Ronald Blaylock 39,231 sh @ 25.46, both 2026-08-05.
- That is a genuine cluster — three buyers including the CEO, roughly $1M each — and it
  supports HOLDING PFE (entry 27.6, now 27.40, no stop by design, long-term target 42.0).
  **But it is NOT new information**: the buys are from early/mid August and the position
  was opened 2026-11-18... correction, 2026-08-18, i.e. days AFTER them, so this was
  almost certainly the original thesis. Nothing changed, so PFE is NOT re-pitched.
- HUN 1 buy / 1 buyer, CVS 1/1, ADM 1/1, OXY 1/1 — single buys are not clusters and are
  weak evidence alone. RTX 0 buys. No new idea came out of this sweep, which is the
  honest result rather than a reason to manufacture one.

## [06:30 ET] DATA GAP — options-implied moves unavailable this run
- `market_data.py implied IWM --entry 270.5 --target 238.69` and the same for TLT both
  returned `ok: false` with HTTP 401 Unauthorized from yahoo-options.
- Same root cause as the index-quote failures at 06:03 (Yahoo 429/401 across the run), so
  the "is my target inside what options price?" check that strategy.md asks for at
  level-setting **could not be run on any idea today**. Recorded, not worked around:
  I have no straddle-implied move for IWM, so the report must not imply one was checked.

## [06:31 ET] LEVELS — week-ahead reference, all from Friday 2026-11-20 closes
Per strategy.md weekend behaviour, equities below are week-ahead PREPARATION, not
same-day entries. Entry on any of them is for the Monday 2026-11-23 open at the earliest.
| Instrument | Close | ATR14 | ATR% | SMA20 | SMA50 | 150d high | Off high | Off 150d low |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 689.81 | 16.07 | 2.33% | 747.81 | 760.18 | 781.62 | **-11.75%** | +0.45% |
| QQQ | 608.45 | 21.13 | 3.47% | 678.53 | 710.96 | 762.86 | **-20.24%** | +0.37% |
| XLK | 149.01 | 6.92 | 4.64% | 172.46 | 184.41 | 203.25 | **-26.69%** | +0.62% |
| IWM | 256.61 | 6.28 | 2.45% | 276.23 | 278.26 | 305.18 | -15.92% | +0.11% |
| GLD | 322.87 | 7.81 | 2.42% | 360.42 | 374.90 | 429.42 | -24.81% | +0.60% |
| XLP | 90.46 | 1.69 | 1.87% | 90.25 | 86.40 | 93.48 | -3.23% | +12.93% |
| TLT | 81.45 | 0.78 | 0.96% | 80.99 | 80.07 | 87.79 | -7.22% | +6.57% |
| UUP | 29.62 | 0.13 | 0.44% | 29.23 | 28.96 | 29.665 | -0.15% | +6.62% |
| XLF | 54.57 | 1.12 | 2.06% | 57.19 | 55.87 | 60.04 | -9.11% | +8.02% |
| KRE | 68.32 | 1.58 | 2.31% | 72.17 | 71.33 | 78.35 | -12.80% | +0.78% |
| XLE | 60.51 | 1.68 | 2.77% | 64.61 | 64.70 | 70.151 | -13.74% | +14.99% |
- **QQQ is -20.24% from its high, which is a bear market, not a correction.** Worth saying
  precisely: the press framing is "Nasdaq erased its 2026 gains", and the drawdown figure
  is the harder fact. XLK -26.69% is worse still.
- SPY has now fallen **six consecutive sessions**, 754.37 -> 689.81 = **-8.6%**, closing
  Friday at 689.81 against a 686.75 low. QQQ -10.5% over the same six. This is a waterfall,
  not an orderly de-rating, and Monday is as likely to be a violent bounce as a
  continuation — every instrument above except XLP, TLT and UUP closed within 0.7% of its
  150-day low, which is where short-covering rallies start.
- ONLY THREE THINGS ARE IN UPTRENDS: UUP (29.62, above both SMAs, 0.15% off its high),
  XLP (90.46, above SMA20 90.25 and SMA50 86.40) and TLT (81.45, above SMA20 80.99 and
  SMA50 80.07). Everything else on the board is below both moving averages.
- First resistance on any bounce, for anyone sizing a short rather than chasing: SPY
  713.56-718.29 (Friday's open/high), QQQ 638.84-643.28, XLK 158.71-159.01. Those are
  Friday's own range, the most recent supply, and they sit well below the SMA20 in all
  three cases.

## [06:32 ET] REJECTED — long tech on the valuation argument — the most tempting trade today
- The setup looks compelling: info-tech forward P/E at its **lowest since March 2020**
  (FactSet via CNN), QQQ -20.2% and XLK -26.7% off their highs, NVDA -47.5% from its
  2026-10-06 peak. strategy.md's durable-mispricing lane is exactly "a quality business
  de-rated on a fixable problem", and this is the lane I am most at risk of skipping.
- Rejected anyway, on one analytical point that I think is decisive: **"cheapest forward
  P/E since March 2020" is a comparison across two completely different discount rates.**
  In March 2020 the funds rate was at zero and the 10-year near 0.7%; today the range is
  3.75-4.00% with the 10-year at 5.04% and the Fed 89% priced to hike again. A multiple
  is the reciprocal of a discount rate plus growth — comparing today's to a zero-rate
  era's and calling the difference "cheap" is the error, not the insight. Cheap relative
  to its own history is the weak form of valuation, and it is the only form I have.
- Second reason: I cannot defend a valuation anchor. strategy.md requires a long_term
  target to be a defended number with the method shown, plus a bear-case PRICE clearing
  a 2.5 R:R. I did not read a single 10-Q or build an earnings estimate for any tech name
  today, so any target I wrote would be a chart level wearing a valuation costume.
- Third: the capex revision cycle has not visibly finished. DELL (11-24 amc), ADI (11-24
  bmo), then MRVL and CRDO (12-01) are the first hard reads on datacenter demand after
  the crash. Buying ahead of four prints that could each confirm the bear case is paying
  to find out. The long_term record here is also 0/5 at -16.3% average — n=10 so it is
  closer to noise than signal, but it is not an argument for loosening the bar.
- Kept as a WATCHLIST observation rather than a recommendation: if the 11-24 and 12-01
  prints hold up and XLK stabilises above the 148.09 Friday low, the valuation case gets
  a catalyst and becomes worth underwriting properly, with actual filings read.

## [06:33 ET] REJECTED — a third "correction continues" expression — on purpose
- Considered and declined: short /MESZ6, short /MNQZ6, short XLP as a crowded-safety
  hedge, and a BTC short via /MBT.
- The correlation cap allows a third idea on this driver and I am choosing not to use it.
  Reasons, in order: (1) the entries are all bad right now — SPY closed 0.45% above its
  150-day low after six straight down sessions, so every one of these is chasing into the
  zone where short-covering rallies begin; (2) the Fed-pause contract at 10c already
  expresses "stress continues" with a defined maximum loss and roughly 9:1 payoff, which
  is a strictly better structure than a leveraged futures short at the lows; (3) covering
  half the IWM short and simultaneously opening an index short is churn, not a position.
- If the tape bounces to the resistance noted above, a short becomes a real idea with a
  real entry. Today it would be a worse version of something I already own.

## [06:34 ET] CORRECTION TO MY OWN WORK — LEN was long_term, and I nearly shipped it wrong
- I captured LEN at 06:26 as a SWING cancellation with target 95.00 and a 72.00 stop.
  **All three were my invention.** Checking the published record: LEN was published
  2026-11-13 and restated 2026-11-20 as **long_term, entry 79.50, target 108.50,
  target_2 122.00, stop None (by design), rr 2.52, conviction 5 then 4.**
  Derived bear case from that ratio: 29.00/2.5217 = 11.50, so bear case 68.00.
- The error mattered beyond the numbers. My cancellation argument was that the December
  FOMC has turned against a homebuilder long — but that attacks a SWING premise, and this
  was never a swing idea. A multi-year housing-undersupply thesis is not refuted by one
  meeting's rate decision, and strategy.md explicitly says long-term ideas legitimately
  repeat and tolerate drawdowns while accumulation is unfinished.
- CORRECTED DECISION: **do not cancel LEN — slow it.** Take only the first third at
  79.50-80.50 (about to fill with the stock at 80.74), then WAIT for Dec 9 before adding;
  second third under 74.00, final third under 68.00. Levels unchanged, no stop by design.
  Conviction lowered 4 -> 3, because I did not re-underwrite the business today: no
  filings read and no order-book data fetched, so my evidence is two kinds about the rate
  path and the chart, not about Lennar.
- Added the concrete invalidation the long_term lane requires and that I had omitted:
  new-order gross margin below ~18% for two consecutive quarters, or net new orders
  falling y/y for two consecutive quarters while incentives rise. Not a price level.
- Also verified against the published record rather than prior_context alone: DKS was
  swing, entry 144.50, target 175.50, stop 129.00, size 2.0 (2026-11-15) — my capture
  matches. IWM was entry 270.50, target 238.69, stop 284.50, **size 2.0** — so "cover
  half" is 2.0 -> 1.0, and I had written 1.5. Fixed.
- Noted in passing: IWM was published LONG on 2026-11-10 (entry 278.00, target 298.50)
  and flipped SHORT on 11-18. The flip was right, but a symbol recommended in both
  directions inside eight days belongs in the anchoring column, not the conviction one.

## [06:36 ET] RESEARCH COMPLETE
- candidates: **4 distinct** (10 lines in candidates.jsonl; synthesis takes the last entry
  per symbol, and three symbols were deliberately re-captured after I corrected my own
  work — IWM twice, the Fed contract twice, LEN twice, DKS twice).

**What the four are, and why the count is small on purpose:**
| Symbol | What it is | Conv | Size | Note |
| --- | --- | --- | --- | --- |
| `KXFEDDECISION-26DEC-H0` | **the one genuinely NEW idea** — buy YES "Fed maintains rate" @ 10c | 4 | 1.5% | event contract, Dec 9 FOMC |
| `IWM` | position update — cover half of the short at the Monday open | 4 | 2.0 -> 1.0% | the book's only winner, +5.1% |
| `DKS` | position update — CLOSE before Monday's earnings | 4 | -> 0% | stop is non-functional across a gap |
| `LEN` | amendment — slow the accumulation to thirds, do not cancel | 3 | 1.5% | long_term, levels unchanged |

ONE new idea is the honest output of this tape, and the reason is specific rather than a
shortfall of effort:
1. **Everything that has fallen is late to short and early to buy.** QQQ -20.2% from its
   high, XLK -26.7%, GLD -24.8%, BTC -21.9% below the level this report wanted to short on
   11-09, NVDA -47.5% from its October peak. Of eleven instruments I levelled, eight closed
   within 0.7% of their 150-day low. Shorting there is chasing; buying there is a knife.
2. **The book is already full of the ideas that would otherwise qualify.** 14 long equity
   positions, seven of them defensive (KHC, CAG, ADM, XLU, XLV, ABT, PFE). The
   correlation cap of 3 per driver is not nearly met — it is massively exceeded — so the
   defensive-rotation lane that is actually working (XLP the only equity ETF in an uptrend)
   is closed to me by the book I already hold.
3. **The one driver I have real conviction on is already expressed twice**, and I declined
   the third slot on purpose rather than through oversight. See the 06:33 rejection.

**Coverage gaps — what I could not check:**
- **Options-implied moves on every single idea.** `implied` returned HTTP 401 from
  yahoo-options for IWM and TLT. strategy.md asks at level-setting whether the target sits
  inside what the market prices; that check ran on nothing today. No straddle figure is
  claimed anywhere.
- **All index and futures quotes.** Yahoo 429/401 across the whole run killed ^GSPC, ^NDX,
  ^VIX, ^RUT, ^DXY, ES/NQ futures, and gold/WTI futures. **No VIX level was fetched, so
  none is stated** — I used ETF proxies throughout and said so. A futures recommendation
  was therefore impossible to price, which is part of why no /MES, /MNQ or /MBT idea exists.
- **A post-Friday CME FedWatch reading.** My 95%/4.3% figures are secondary reports dated
  11-16 to 11-19, i.e. PRE-correction. The post-Friday read I do have is the Kalshi/
  Robinhood orderbook itself (pause 8-10c), which is why the Fed idea leans on that.
- **Any company fundamentals.** I read no 10-Q, 8-K or transcript today. Consequently there
  is no new long_term idea, and the tech-valuation case — the most tempting trade on the
  board — was rejected partly for exactly that reason (06:32).
- Not reached at all: FDA calendars, index rebalances, lockup expiries, court dates,
  small/micro caps (no screener), and `short`/`analysts` on any name.

**Sources that failed:**
- `yahoo` — HTTP 429 on all index/futures quotes; HTTP 401 on all options chains.
- `finnhub` — refused index quotes ("Market data subscription required for CFD indices");
  worked fine for ETFs and single stocks.
- `stooq` — 404 on every index symbol. `alphavantage` — no API key configured.
- `coingecko` — the `macro` subcommand's crypto block returned prices FAILED, but the
  standalone `crypto` subcommand worked; both were tried.
- `market_data.py events` — structurally broken, not a market-availability problem: it
  filters one unsorted 200-market Kalshi page client-side, so every topic returns 0.
  Worked around via the Kalshi `/markets/<ticker>/orderbook` endpoint, since `/markets`
  returns null for yes_bid/yes_ask/last_price. **Worth a fix plus a test** — without the
  workaround the richest lane in today's tape would have been invisible.

**Two things I got wrong mid-run and corrected in place, flagged so synthesis trusts the
later entry over the earlier one:**
- At 06:05 I read gold's -3.67% and the equity drop as a one-day forced liquidation that
  made a dovish pivot more likely. Both wrong: gold is in a 24.8% bear market and the Fed
  is 89% priced to HIKE. Corrected at 06:10/06:11. Anything in this log before 06:10 that
  assumes easing is superseded.
- At 06:26 I captured LEN as a swing cancellation with a target and stop I invented. It is
  a long_term idea with published levels and no stop. Corrected at 06:34.

## [06:38 ET] REJECTED — Nov CPI YoY event contracts — I tested an edge and did not have one
Worth recording in full because the process is the output, and because the by-product
matters more than the trade would have.
- Robinhood/Kalshi list `KXECONSTATCPIYOY-26NOV-*`, EXACT-bucket markets in 0.1pp steps
  from 2.0% to 4.5%, resolving 2026-12-10. Orderbook (fetched live, YES bid/ask in cents):
  3.5 -> 5/6, 3.6 -> 19/20, **3.7 -> 38/39**, 3.8 -> 23/28, 3.9 -> 7/9,
  4.0 -> -/1, 4.1 -> -/1, 4.2 -> -/1, 4.3 -> -/1, 4.4 -> -/2, 4.5 -> -/2.
  Mass sums to ~98 and is centered on **3.7%** with ~1% above 3.9%.
- MY FIRST PASS said ~4.0-4.1% and looked like a 50-point edge. Arithmetic: Oct 2026
  CPIAUCNS = 337.511, Nov 2025 CPIAUCNS = 324.122, so YoY = 337.511 x (1+m) / 324.122 - 1.
  The 16-year Oct->Nov NSA seasonal is **mean -0.117%, median -0.093%** (2009-2024; 2025
  absent because **October 2025 CPI was never published** — a real gap in both CPIAUCNS and
  CPIAUCSL, almost certainly the 2025 shutdown). At the median that gives **+4.03%**, and
  P(YoY >= 4.0%) looked like 9 of 16 years = 56% against a market price of 1-2c.
- A 50-point edge against a liquid, tightly-priced market means I am missing something, so
  I went and looked. **I was missing November gasoline.** FRED GASREGW, weekly US regular:
  Oct 2026 weeks 4.354 / 4.331 / 4.284 / 4.269 (avg **4.309**); Nov 2026 so far
  4.153 / 3.995 / **3.805** (avg **3.984**) = **-7.55% m/m and still falling**, with the
  Nov 16 week 11.7% below the October average.
- At a ~3.5% CPI basket weight that is about **-0.26 to -0.31pp** from gasoline alone, which
  takes a plausible November NSA m/m to roughly -0.25% to -0.35% and **YoY to ~3.82-3.92%**.
  The market's 3.7% center implies -0.40%, a bottom-2-of-16 seasonal outcome — and that is
  exactly what an energy collapse produces (the only two comparable years, 2012 at -0.474%
  and 2014 at -0.540%, were both oil-crash Novembers).
- VERDICT: **no trade.** My corrected estimate (~3.85%) sits one or two buckets from the
  market's center, which is well inside my own error bars — I do not know the final November
  week, the non-energy contribution, or the exact gasoline weight, and an EXACT-bucket market
  requires being right to ~0.05pp. There may be a small edge in the 3.8 bucket at 23-28c, but
  "possibly one bucket cheap" is not the explicit probability disagreement universe.md
  demands. The naive version of this idea would have been a 50-point claim built on my own
  ignorance of a number I could have looked up in two minutes.

## [06:39 ET] MACRO BY-PRODUCT — the Fed decides BEFORE it can see this disinflation
This is the most useful thing the CPI work produced and it refines today's Fed idea.
- Energy disinflation is happening NOW and is large: gasoline -7.55% m/m in November.
- But the release calendar puts it out of the Fed's reach on Dec 9:
  - **2026-11-25 PCE covers OCTOBER**, when gasoline averaged 4.309 against roughly 4.355
    in September — about -1.1% m/m, i.e. mild. **The Nov 25 print predates the collapse.**
  - November CPI: **2026-12-10**, the day AFTER the decision.
  - November PCE: **2026-12-23**, two weeks after.
- So the Fed votes on Dec 9 having seen no official data containing the November energy
  drop. It cuts both ways and I am recording both rather than the convenient one:
  AGAINST the pause (no soft official print in hand to justify waiting, and the Nov 25
  October data may even read firm), FOR the pause (a visible, verifiable real-time
  disinflation impulse plus a 20% Nasdaq drawdown is precisely the "wait one meeting and
  see" argument, and FOMC members do watch weekly energy).
- ACTION: amending the Fed candidate so it does NOT imply the 11-25 print carries the
  November disinflation. My earlier framing called it "the decisive input"; the accurate
  statement is that it is the last major inflation print before the meeting AND that it
  covers October, which is a weaker thing to lean on.

## [06:42 ET] ADDENDUM TO RESEARCH COMPLETE — supersedes the 06:36 block where they differ
The 06:36 RESEARCH COMPLETE block stands except for the following, which came out of the
CPI/gasoline work done after it. Research continued past that block because budget
remained; nothing above was abandoned.
- **The Fed contract is re-captured at conviction 5, up from 4**, and it is now the
  best-evidenced idea in the report rather than merely the only new one. The fourth
  distinct evidence kind is `primary_document`: I read the federal statistical series
  directly (FRED GASREGW weekly gasoline, CPIAUCNS) rather than commentary about them.
  Four kinds is a 5 on the strategy.md rubric, and in this case the score went UP for the
  right reason — more independent confirmation, not a better feeling about the idea.
- Its thesis now carries a **verifiable** disinflation leg (gasoline -7.55% m/m in
  November, worth about -0.3pp on the CPI index) instead of resting only on the narrative
  that an AI-capex bust is disinflationary.
- Its key_risk now carries the sequencing problem I found, which argues AGAINST the trade
  and is stated as such: the Fed votes on Dec 9 with no official data containing the
  November energy drop, because November CPI prints 12-10 and November PCE 12-23.
- The 11-25 PCE is no longer described as "the decisive input". It is the last major
  inflation print before the vote, but it covers OCTOBER and predates the collapse.
- Candidate count is unchanged at **4 distinct** (11 lines; synthesis takes the last per
  symbol). One new idea, two position updates, one accumulation-pace amendment.
- Add to coverage gaps: I did not fetch a professional CPI nowcast (e.g. Cleveland Fed) or
  a sell-side November CPI consensus. Had I needed to trade the CPI buckets rather than
  reject them, that would have been mandatory rather than optional — the market's -0.40%
  implied m/m is effectively the consensus and I had no independent read on it.
- Add to sources used: FRED GASREGW and CPIAUCNS, both queried directly with the repo's
  configured FRED key rather than through `market_data.py macro`, whose fixed
  `FRED_SERIES` map does not include either.

**Final shape for synthesis, in rank order by conviction then reward-to-risk:**
1. `KXFEDDECISION-26DEC-H0` — yes @ 10c, conv 5, R:R 2.5 — the only NEW idea.
2. `IWM` — sell_short, conv 4, R:R 2.27 — cover half at Monday's open, 2.0% -> 1.0%.
3. `DKS` — buy, conv 4, R:R null — CLOSE before Monday's print, -> 0%.
4. `LEN` — buy, conv 3, R:R 2.52, long_term — first third only, then wait for Dec 9.
Plus two withdrawals that are decisions rather than ideas and carry no levels:
`GLD` SELL @ 406.77 and `/MBTZ6` SHORT @ 74075, both 22-26% away from the market and
unfillable. And `CVS` BUY @ 77.50 left standing, unchanged, deliberately not re-pitched.

**The one-line honest summary of today:** a tech-led liquidation took the S&P into
correction and the Nasdaq into a 20% drawdown, driven by an AI-capex unwind against a Fed
that is still 89% priced to HIKE on Dec 9 — so nothing long-duration is buyable and
everything already broken is late to short. The report's value today is in what it closes
and trims, not in what it adds.
