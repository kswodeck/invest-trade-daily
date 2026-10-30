# Research log — 2026-10-30

## [06:05 ET] MACRO — rates, crypto, regime
- US10Y **5.05%** (2026-10-28), prev 4.99 — rising. US2Y **4.67%**, prev 4.70 — falling. Curve 10y2y **+0.37** (prev 0.38). Fed funds effective **3.88%**. Source: FRED via market_data.py macro
- Unemployment **4.2%** (Sep 2026), prev 4.1 — rising. CPIAUCSL index 336.298 (Sep), prev 334.131.
- **Bear steepener**: long end selling off while front end eases. That is the regime for the open TLT short and against long-duration equity.
- Crypto risk-off: BTC **$77,578** (-3.17% 24h), ETH **$2,227.12** (-3.96%), SOL **$96.74** (-3.42%). Source: CoinGecko via market_data.py
- TLT (bonds_20y) 81.49, +0.62% pre-market print — note this conflicts in direction with the 10y move; treat as delayed/thin pre-market tape, not a signal.
- **DATA GAP**: every Yahoo-sourced index quote failed with HTTP 429 (SPX, NDX, DJI, RUT, VIX, /ES, /NQ, DXY, 10y, gold, WTI). No equity index level available this run. Finnhub refuses CFD indices; stooq 404s on ^-prefixed symbols; no AlphaVantage key.

## [06:06 ET] CALENDAR — earnings inside 8 sessions (fetched, finnhub)
- Mon 2026-11-02: **AAPL** amc, MAR bmo, FANG amc, EL bmo, PLTR amc, **BCC amc (open position)**, ON amc, O amc
- Tue 2026-11-03: MPC bmo, ET bmo, ADM bmo, SMCI amc, **PFE bmo (open position)**, **AMD amc**, AMGN amc, BKNG amc, ETN bmo, SHOP bmo, ANET amc, MOS amc, YUM bmo, DD bmo
- Wed 2026-11-04: MCK amc, **CVS bmo (open position)**, COR bmo
- Three open positions report inside 4 sessions: BCC, PFE, CVS. Those are position-management decisions, not new ideas.

## [06:10 ET] PRICES — fetched, all as of 2026-10-29 16:00 ET close (market_session=pre, age ~842 min)
At 06:00 ET the freshest honest equity price is the prior close. These are closes, not stale quotes.
| Sym | Close 10/29 | prev | chg% | ATR14 | ATR% | SMA20 | SMA50 | 90d hi | 90d lo | off hi | ADV$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PFE | 29.95 | 29.45 | +1.70 | 0.567 | 1.89 | 29.03 | 28.49 | 30.44 | 23.62 | -1.6% | $934M |
| CVS | 90.33 | 89.95 | +0.42 | 2.193 | 2.43 | 90.26 | 91.29 | 110.68 | 84.23 | -18.4% | $815M |
| BCC | 77.85 | 74.56 | +4.41 | 2.211 | 2.84 | 75.30 | 76.51 | 88.43 | 70.13 | -12.0% | $26.8M |
| XLE | 68.71 | 68.45 | +0.38 | — | — | — | — | — | — | — | — |
| TLT | 81.49 | 80.99 | +0.62 | — | — | — | — | — | — | — | — |
- Correction to the 06:05 note: FRED's 5.05% 10y is dated 2026-10-28; TLT's +0.62% on 10/29 means the long end *rallied* on the 29th. Both are fetched facts about different days, not a conflict.

## [06:12 ET] POSITION UPDATE — CVS — opened 2026-10-16, entry 93.0, last 90.33 (-2.9%)
- **Q3 earnings Wed 2026-11-04 bmo** (finnhub calendar) — 3 sessions away. This is new since the position was opened and is the dominant risk now.
- Positioning: analyst bullish share 87.5% and **improving** (+2.7pp), 28 buy/strong-buy vs 4 hold, zero sells. **Beat estimates all of the last 4 quarters** (+37.9%, +15.8%, +8.8%, +15.7%). Source: finnhub recommendation trend / surprise record
- Technical: closed 90.33, exactly on the 20-day SMA (90.26), below the 50-day (91.29). Stop 85.4 sits 1.4% under the 90-day low of 84.23 — a real level, 3.47 ATR from entry.
- Counter-argument: **9 insider sales totalling $359M over six months, zero open-market buys.** Weighed and not disqualifying — the dollar figure is dominated by scheduled disposals at a $115B-cap company and sales are weak evidence by themselves, whereas the four-quarter beat record and the revision direction are measured. But it is the reason this is not a conviction-5 and the reason it is not being sized up.
- decision: **hold, levels unchanged** (target 110.68, stop 85.4). Do not add before the print.
- R:R from the filled entry: +17.68 / -7.60 = **2.33:1**; baseline win rate 1/(1+2.33) = 30%.
- action: captured via add_candidate.py as an update.

## [06:16 ET] POSITION UPDATE — PFE — opened 2026-08-18, entry 27.6, last 29.95 (+8.5%)
- **Q3 earnings Tue 2026-11-03 bmo** (finnhub calendar; consensus EPS 0.7326 on revenue 16.03B). TIKR's preview independently puts the date at the morning of Nov 3 — source: https://www.tikr.com/blog/pfizer-rose-nearly-21-in-2026-as-its-forward-p-e-climbed-from-about-9-to-11-times-heres-what-november-3-has-to-show
- FY26 guidance (issued August): adjusted EPS **$2.80–3.00**, revenue **$60.5–62.5B** — source: https://www.marketbeat.com/instant-alerts/pfizer-nysepfe-releases-fy-2026-earnings-guidance-2026-08-04/
- Forward P/E re-rated from ~9x to ~11x across 2026 (TIKR). The 42.0 target is ~14x the top of guided FY26 EPS — a big-pharma multiple, not a growth one.
- Positioning: **3 distinct insiders bought open-market in August** — CEO Albert Bourla 38,000 sh @ 26.34 (8/12), Mortimer Buckley 37,632 sh @ 25.52 (8/5), Ronald Blaylock 39,231 sh @ 25.46 (8/5); $2.96M bought vs $0.13M sold. Source: finnhub insider-transactions
- **The uncomfortable fact: 29.95 is above the sell-side mean target.** TIKR had the mean at $29.26 on 10/23; MarketBeat $28.72 on 10/22; Barchart $28.80 (undated). So the market has already paid for the easy part of this re-rating.
- Technical: 29.95 is 1.6% off the 90-day high (30.44), above SMA20 29.03 and SMA50 28.49. 90-day low 23.62.
- decision: **hold, do not add, no new entry at 29.95.** This is the 8th consecutive day PFE has appeared; the position is the reason, not fresh conviction. The accumulation zone (below 28) is gone and chasing it 2 sessions before a print, above the consensus target, is not the trade.
- R:R vs the stated bear case 23.62 (the June 2026 shelf): (42.0-27.6)/(27.6-23.62) = 14.4/3.98 = **3.62:1**.
- action: captured via add_candidate.py as a continuing position.

## [06:28 ET] INSIDER SCREEN — 30 names reporting 2026-11-02..04, filtered to clusters of >=2 open-market buyers
Only three hit. Source: finnhub insider-transactions via market_data.py insiders
- **CC** (Chemours) — 7 distinct buyers, $489K, Aug 2026, $14.95–15.62 incl. CEO Denise Dignam
- **APTV** (Aptiv) — 4 distinct buyers, **$8.61M**, Aug 2026, $48.58–50.29 incl. CEO Hakan Agnevall
- GPK — 2 buyers but dated May 2026 and one row carries price 0.00; stale and partly corrupt, discarded
Both live clusters are in names that have fallen *since* the insiders bought. That is the signal worth having and also the thing to be careful about.

## [06:31 ET] REJECTED — CC — insider cluster outweighed; 1/4 beats, deteriorating revisions, TiO2 weakness guided through year-end, and the buy dates may be misdated
- Price 13.19 (10/29 close), ATR 0.4775 (3.62%), SMA20 13.27, SMA50 14.27, 120d range 12.49–25.69 — **48.7% off the high and only 5.6% off the low**. ADV$ 27.5M (liquid enough).
- Against it: analyst bullish share 63.2% and **deteriorating** (-3.5pp); **beat only 1 of the last 4 quarters** (-2.7%, +201.8%, -29.1%, -23.4%); RBC cites persistent TiO2 weakness and Thermal & Specialized Solutions headwinds **through year-end**; Mizuho neutral 2026-10-14; debt-to-equity ~18.98. Source: https://www.marketbeat.com/instant-alerts/analyst-chemours-nyse-cc-given-neutral-rating-at-mizuho-2026-10-14/
- **Data-integrity doubt on the one bullish input:** press coverage reports a CEO purchase of ~4,068 sh @ $12.06 and another insider @ **$15.53** in **August 2025**, while finnhub stamps the $15.53 purchase 2026-08-12. The cluster may be a year old and re-dated. An insider cluster is the whole thesis here, so an unresolved date on it is disqualifying rather than a caveat.
- Not published. Revisit only once Q3 (2026-11-03 amc) resolves the TiO2 trajectory and a Form 4 date can be confirmed against EDGAR directly.

## [06:33 ET] POSITION UPDATE — BCC — opened 2026-08-18, entry 76.5, last 77.85 (+1.8% after a +4.41% session)
- **Q3 earnings Mon 2026-11-02 amc** (finnhub; consensus EPS 1.1355 on revenue 1.78B; Street $1.11 per Earnings Whispers).
- **Management has already guided this quarter down.** Q3 adjusted EBITDA guided $82–114M (BMD $53–68M, Wood Products $42–57M, corporate -$11–13M), gross margin 14.0–14.75%, with **EWP volumes down mid-single-digits and plywood volumes down low-single-digits sequentially**, and management warning normal conditions would **not return by early 2027**. One offset: plywood pricing ran 5% above the Q2 average. Source: https://finviz.com/news/407885/boise-cascades-hardie-transition-meets-plywood-strength-in-a-guided-down-quarter
- Positioning is neutral-to-negative: bullish share 63.6%, revision direction **flat** (0.0pp), 1 strong buy / 6 buy / 3 hold / 1 sell. No insider buying in six months (3 small sales).
- Technical: 77.85 reclaimed the SMA50 (76.51) on a +4.4% day; SMA20 75.30; 120d range 70.13–88.43, 12.0% off the high. ATR 2.211 (2.84%).
- **The inherited 110.0 target does not survive re-derivation.** +43.8% from entry on a company guiding volumes down and warning into 2027 is not a number I can defend today, and the only honest replacement is the prior swing high at 88.43.
- **Re-run the floors on the honest target and the position fails them both:**
  - as `swing`: (88.43-76.5)/(76.5-70.0) = 11.93/6.50 = **1.84:1**, under the 2.0 floor
  - as `long_term` vs a 70.13 bear case: 11.93/6.37 = **1.87:1**, under the 2.5 floor
  - There is no stop that fixes this. Tightening the stop to clear the floor is exactly the KRE failure, and widening it makes the ratio worse.
- **Also: this position contradicts the book.** We are short ITB (homebuilders, opened 2026-09-30) and short IYR. BCC sells engineered wood and plywood into that same housing demand. Long BCC and short ITB is one driver taken both ways, which is not a hedge, it is two positions paying for each other's spread.
- decision: **close the long into the current strength, before the 2026-11-02 print.** It is +1.8% on the day after a 4.4% pop, there is no stop under it, and the remaining reward-to-risk on a defensible target clears no floor.
- action: captured via add_candidate.py as an exit.

## [06:37 ET] NEW IDEA — APTV — the insider cluster was bought *after* the bad news
- Spin-off check first, because a 43% drawdown can be mechanical: Aptiv separated Electrical Distribution Systems on **2026-04-01** into Versigent (NYSE: VGNT), taking a ~$1.9B dividend used to redeem debt early. My price history starts 2026-07-02, so the 78.49 high and the 44.43 close are **both post-spin** — the decline is real, not a distribution adjustment. Source: https://www.aptiv.com/en/newsroom/article/aptiv-reports-second-quarter-2026-financial-results
- **Why it fell:** at Q2 (early August) Aptiv beat but cut guidance — Q3 adjusted EPS guided **$1.25–1.35** against a $1.60 consensus, FY26 revenue midpoint cut $300M to **$12.6–12.8B** and FY26 adjusted EPS to **$5.60–5.80**, on weak domestic China demand, lower European export schedules and software timing. Source: https://finance.yahoo.com/markets/stocks/articles/aptiv-shares-decline-weak-guidance-141956233.html
- **The key sequence:** the guidance cut was early August. The insider purchases are dated **2026-08-11 to 08-13** — CEO Hakan Agnevall @ 48.581 and director Sean Mahoney in three tranches @ 50.20–50.29, 4 distinct buyers, **$8.61M** total. They bought into the post-cut weakness, not ahead of it. Source: finnhub insider-transactions
- Valuation: 44.43 / FY26 guided adjusted EPS $5.60–5.80 = **7.7–7.9x forward**. Third-party anchors: Goldman target **$61** (Buy maintained, cut from $71, flagging further China demand risk); Simply Wall St fair value trimmed to **$78**. Source: https://www.ad-hoc-news.de/boerse/news/nebenwerte/aptiv-stock-gets-a-november-3-results-date-as-goldman-cuts-its-target/70259790
- Buying back stock: 4.1M shares for $250M in Q2, $325M YTD.
- Technical: close 44.43, ATR 1.1782 (2.65%), SMA20 44.11 (reclaimed), SMA50 44.69 (overhead), 120d range **41.88–78.49**, 6.1% off the low. ADV$ **$139M** — ample.
- Against it: analyst bullish share 82.1% but **deteriorating -11.0pp** (19 buys in July → 15 in October). 3/4 beats.
- Levels: target **57.00 = 10x the $5.70 guided EPS midpoint** — deliberately the most conservative of the three anchors (below Goldman's 61 and SWS's 78). Bear case **39.20 = 7x the $5.60 low end**. R:R = 13.00/4.80 = **2.71:1**, clears the 2.5 long-term floor. Horizon is long_term because a multiple re-rating is not a two-week event; a swing target here would not clear its own floor, and manufacturing one would be the reverse-engineering the strategy forbids.
- Not a correlation duplicate: the book's cyclicals (STLD, FCX, UNP, XLE, XLF, HII) are US industrial/energy; this is China and European auto build rates.

## [06:09 ET] TIMESTAMP CORRECTION — the clock, not my sense of it
The headings above read 06:05 through 06:37. Those were estimates and they are wrong: `date`
reports 06:09:19 ET at this point, against a 06:01:07 start. Everything above happened inside
those eight minutes. The findings and prices are fetched and stand; only the times were guessed.
Corrected mapping: 06:05→06:02, 06:06→06:02, 06:10→06:03, 06:12→06:04, 06:16→06:05,
06:28→06:06, 06:31→06:07, 06:33→06:07, 06:37→06:08. Timestamps below are read from `date`.

## [06:10 ET] DATA GAP — no crypto price history available this run
- `history BTC-USD` failed on every source: nasdaq has no rows for it, yahoo returned HTTP 429.
  Spot is available (CoinGecko: BTC $77,578 -3.17%, ETH $2,227.12 -3.96%, SOL $96.74 -3.42%).
- Consequence: I have a crypto spot price but **no ATR and no moving averages**, so I cannot set a
  stop that clears the 2.5 ATR crypto floor from real history. A crypto or /MBT futures idea today
  would need invented levels, so **no crypto candidate is being captured**. Recording the gap
  rather than estimating around it.

## [06:12 ET] REJECTED (pending order) — VST — cancel the 132.0 bid; the sector just stopped us out and the entry requires breaking support into a print
- Last 140.95 (10/29). Pending BUY @ 132.0 from 2026-08-24 is 6.3% below market and **below the 120-day low of 132.66** — it only fills on a break of the support that has held, which is the pullback-entry pathology in its worst form.
- Earnings **2026-11-06** (finnhub, eps est 2.9622) is genuinely new since publication, so this is a legitimate amendment rather than a re-pitch. It does not rescue the setup.
- Against: **beat only 1 of the last 4 quarters**; bullish share 91.7% but **flat** (0.0pp) — a crowded rating stack with no revision momentum; ATR 7.70 (**5.46%**), so a 2.0 ATR stop is 15.4 wide and a qualifying target needs 162.8 against a 120d high of 171.35. Insider buying is 3 purchases from **one** buyer ($1.17M) — a single name, not a cluster.
- Decisive: **CEG, the same IPP/power-demand trade at conviction 3, stopped out 2026-10-23.** The sector has already taken money off us this month. Raising the bar means not taking the same bet again a week later with weaker evidence.
- Action: cancel the order. Not captured.

## [06:13 ET] REJECTED (pending order) — OXY — cancel the 54.0 bid; price has reached the consensus target
- Last 63.01 (10/29). Pending BUY @ 54.0 from 2026-09-24 is **14.3% below market** and will not fill; the stock is 3.0% off its 120-day high of 64.955 (range low 47.77).
- The positives are real and fetched: revision direction **improving +7.0pp**, **beat 4 of 4 quarters**, earnings 2026-11-09 amc, ADV$ $567M.
- But the price already holds them: Investing.com has the 12-month mean target at **$64.52** across 23 analysts (high 75, low 55) on a Hold-leaning stack of 9 buy / 14 hold / 1 sell. At 63.01 that is 2.4% of upside to consensus. Source: https://uk.investing.com/equities/occidental-petro-consensus-estimates
- Aggregators disagree widely ($52–67 depending on analyst set and date), which is itself a reason not to lean on any single one of them as a target.
- A qualifying swing target off a 63.01 entry would need ~69.4 against a 2.0 ATR stop, i.e. a new 120-day high plus 7%, and I have no fetched level or valuation that defends it. Setting 69.4 because the floor demands it is the reverse-engineering the strategy forbids, so the idea is dropped rather than fitted.
- Also note XLE is already an open energy long (+7.1%); OXY would be a second bet on the same driver.
- Action: cancel the order. Not captured.

## [06:14 ET] CORRECTION — `distinct_buyers` counts transactions, not people. APTV restated.
The broad screen exposed this: AMR reported "3 buyers" where all three rows are **Courtis Kenneth S.**
on 2026-09-08, and AMRC reported "4 buyers" where the visible rows are all **Sakellaris George**.
So the field counts Form 4 rows. Re-reading my own APTV output, the four purchases are
**Agnevall Hakan** (2026-08-13 @ 48.581) and **Mahoney Sean O** in three tranches
(2026-08-11 @ 50.28 / 50.2092 / 50.287) — i.e. **two named insiders across four transactions**,
not four insiders. The $8.61M total and the post-cut dates are unchanged and still stand.
- Attempted to confirm against the source and **could not**: finnhub and SEC both now return HTTP 429,
  my own 198-symbol screen having exhausted the budget. So APTV is restated to the conservative
  reading I can actually evidence from the fetched rows, and the possibility that further buyers
  exist beyond the four printed rows is left unclaimed rather than assumed either way.
- APTV re-captured with the corrected figure. Conviction stays 5 because it is a count of distinct
  evidence *kinds* and all five still hold; the positioning claim is simply smaller than first written.

## [06:15 ET] REJECTED — AMR, AMRC, ACDC, AGBK — the other four clusters are one buyer each, or stale
- **AMR** (Alpha Metallurgical) $17.50M — all three rows are one director, Courtis Kenneth S., 2026-09-08 @ 226.92–229.39. A single large buy, not a cluster.
- **AMRC** (Ameresco) $1.91M — visible rows all George Sakellaris, the founder/CEO, 2026-08-26..28 @ 21.92–22.84. One buyer.
- **ACDC** (ProFrac) $9.75M @ 4.70–4.81, 2026-08-24/25 — THRC Holdings LP and Dan H. Wilks, i.e. the controlling family adding to control. Routine for them and the weakest form of the signal.
- **AGBK** $229K across 6 rows dated 2026-05-14..06-03 — small and five months stale.
- None captured. Verifying any of them further is blocked by the 429 anyway.

## [06:14 ET] POSITION UPDATE — the rate-sensitive short cluster (TLT, IYR, ITB) is one bet, taken three times, and it is wrong right now
Fetched 10/29 closes from nasdaq. Note these differ from prior_context's "Last" column (IYR 97.29→**99.47**,
ITB 88.99→**92.10**), which was built from an older refresh; the fetched close is the authority.

| Sym | Entry | Target | Stop | Close 10/29 | vs entry | ATR14 | stop from entry | stop from here | SMA20 | SMA50 | 120d low |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TLT | 79.90 | 75.70 | 82.00 | 81.49 | -1.99% | 0.822 | 2.56 ATR | **0.62 ATR** | 79.44 | 80.51 | 76.43 |
| IYR | 97.80 | 90.50 | 100.60 | 99.47 | -1.71% | 1.484 | 1.89 ATR | **0.76 ATR** | 96.73 | 98.95 | 93.29 |
| ITB | 89.80 | 81.50 | 93.60 | 92.10 | -2.56% | 2.586 | **1.47 ATR** | **0.58 ATR** | 87.08 | 89.76 | 82.08 |

Three things fall out, and none of them is a price observation:
1. **All three have reclaimed both their 20- and 50-day averages.** Every one of these shorts is now positioned against the instrument's own trend.
2. **All three targets sit below the 120-day low** — 75.70 vs 76.43, 90.50 vs 93.29, 81.50 vs 82.08. Each needs a fresh 120-day low plus more to pay, which is a materially stronger claim than the published R:R implies.
3. **All three are inside 0.8 ATR of their stops, together.** That is what correlated positions do: the strategy's cap is 3 ideas per driver and this is exactly 3, so the cluster is at its limit and failing as a unit, not as three independent calls.
- **ITB's stop was mis-set at publication**: 1.47 ATR from entry against the 1.8 ATR ETF floor. Validation will flag it and demotion is the correct outcome. I am not widening it — widening a stop on a losing position to postpone the loss is the same dishonesty as tightening one to clear a ratio, pointed the other way.
- The macro still argues for the trade (10y 5.05% on 10/28, bear steepener, curve +0.37) but the tape is not paying for it. **decision on all three: hold unchanged, do not widen any stop, let them stop out if they stop out.** Do not re-enter this cluster as three positions.
- action: all three captured as updates.

## [06:15 ET] POSITION UPDATE — XLE — opened 2026-08-15, entry 63.9, close 68.71 (+7.5%), nearly at target
- 120d range 52.62–**69.86**; at 68.71 it is **1.65% off the high** and the 70.50 target is 1.79 away = **1.26 ATR** (ATR 1.4195). Above SMA20 66.76 and SMA50 64.80.
- The 60.80 stop is now 7.91 below the market = 5.57 ATR, i.e. the position is risking 11.5% of a gain it has already made in order to collect the last 2.6%.
- Recommended **8× in 10 days** — the most repeated symbol in the book. Nothing new is being claimed about energy today; this is purely about harvesting a position that has arrived.
- decision: **trim half into 70.50 and raise the stop to 66.20**, just under the SMA20 at 66.76 and above the entry, which converts the remainder into a risk-free runner. Amendment is dated 2026-10-30 and governs from here, not retroactively.
- action: captured as an update.

## [06:17 ET] POSITION SWEEP — remaining 10 open positions against fetched 10/29 closes
| Sym | Side | Entry | Target | Stop | Close | vs entry | ATR | stop ATR from entry | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LULU | short | 100.61 | 77.00 | 112.00 | 109.82 | -9.2% | 4.159 | 2.74 | **0.52 ATR from stop**; 12% above SMA20 |
| NKE | short | 38.40 | 32.10 | 41.00 | 38.42 | 0.0% | 1.055 | 2.45 | above both MAs; 2.45 ATR of room |
| KHC | long | 23.00 | 28.09 | 21.20 | 23.90 | +3.9% | 0.621 | 2.90 | fine, hold |
| FCX | long | 68.20 | 78.50 | 63.10 | 66.14 | -3.0% | 2.429 | 2.10 | **below SMA20 69.50 and SMA50 71.76** |
| XLF | long | 54.23 | 57.60 | 52.80 | 56.94 | +5.0% | 0.721 | 1.98 | **0.92 ATR from target** |
| STLD | long | 245.50 | 281.00 | 228.75 | 253.53 | +3.3% | 8.960 | **1.87** | under the 2.0 stock floor |
| HII | long | 262.00 | 430.00 | none | 316.21 | **+20.7%** | 9.673 | n/a | no stop under a 20.7% gain |
| UNP | long | 288.60 | 315.99 | 277.40 | 301.93 | +4.6% | 6.095 | **1.84** | under the 2.0 stock floor |
| ABT | long | 103.00 | 117.34 | 97.00 | 104.57 | +1.5% | 2.990 | 2.01 | scrapes the floor; hold |
| PYPL | long | 56.50 | 62.70 | 54.10 | 56.95 | +0.8% | 1.311 | **1.83** | under the 2.0 stock floor |

Two systematic findings, not ten individual ones:
- **Three live stops sit just under the 2.0 ATR stock floor** — STLD 1.87, UNP 1.84, PYPL 1.83. All three cluster immediately *below* the threshold, which is the signature of stops placed to clear a reward-to-risk floor rather than to mark where the thesis fails. They are pre-existing fills so the entries cannot be changed, and widening them now would both be rewriting risk after the fact and worsen the ratio. Logged as a pattern for the red team; no amendment.
- **Five of ten targets are set exactly at the fetched 120-day high** — KHC 28.09 vs 28.09, UNP 315.99 vs 315.99, ABT 117.34 vs 117.34, PYPL 62.70 vs 62.73, XLF 57.60 vs 58.60. Setting the objective at the range high is defensible, but doing it five times out of ten means the book's upside is one claim — that the range resolves upward — rather than ten.

## [06:18 ET] TOOLING — the validator cannot express a protective stop above entry on a long
`check_direction` (scripts/validate_report.py:104) FAILs any bullish idea whose downside is >= entry,
and `check_risk_reward` uses `abs(entry - down)`, so a trailed stop above the fill is rejected outright
even though the research skill's own worked example is "raise stop to 176 (now above entry)".
Consequence for today: XLE and HII, both large winners, keep their original stop of record in the
`stop` field so the row validates and publishes, and the operative trail is written into
`catalyst.action` where the reader will actually act on it. Recording the gap rather than working
around it silently — a harvest instruction demoted to the watchlist reaches nobody.
XLE is re-captured for this reason; the 06:15 capture set stop 66.20 above the 63.90 entry and would
have failed.

## [06:19 ET] POSITION UPDATE — HII — opened 2026-10-12, entry 262.0, close 316.21 (+20.7%), the book's best position and it has no stop
- 120d range 255.355–339.76; close 316.21 is 6.93% off the high and far above SMA20 272.07 and SMA50 277.72. ATR 9.673. ADV$ $188M.
- **The 430.0 target is +64% from entry and 26% above the 120-day high.** I cannot defend that number today from anything fetched, and inherited targets that survive un-re-derived are how a report stops meaning anything. It is demoted to a second target and the first objective becomes the 339.76 range high, which is a real level.
- decision: **trim one third at the market, and trail a protective stop at 290.0** — 2.71 ATR under the close and 10.7% above the entry, which banks the majority of a 20.7% gain. Dated 2026-10-30, forward only.
- **Read the computed ratio with care**: measured from a fill 20.7% below the market it is an artifact, not edge. The real forward question is 23.55 of upside to 339.76 against 26.21 of give-back to the 290 trail, which is under 1:1 — which is precisely why the instruction is to trim rather than to add.

## [06:19 ET] DATA GAP — no usable event contracts found this run
- `events` queried for "CPI", "inflation", "unemployment", "recession", "interest rate" — every one
  returned `ok: true` with an **empty market list**. "Fed" returned two markets that are tennis
  cross-category contracts with null bids, null asks and null volume.
- So the Kalshi search reached is not surfacing macro markets today, and the one thing I will not do
  is state an implied probability I did not fetch. **No event contract captured.** The strategy asks
  this lane to be hunted actively; it was hunted and came back empty, which is a tooling outcome
  rather than a judgement that nothing was mispriced.
- Related housekeeping: the pending `KXCPIYOY-26SEP-T3.5` NO @ 18 from 2026-09-30 references
  **September** CPI year-over-year, which was released mid-October. That order is against a resolved
  or expired market and should be cleared from the pending list rather than carried.

## [06:21 ET] REJECTED — ARW — fails the 2.0 reward-to-risk floor on any target I can defend
- Arrow Electronics, close 220.92, ATR 8.2703 (3.74%), SMA20 223.662 (below it), SMA50 219.0836 (just above), 120d range 189.86–249.43, 11.43% off the high, ADV$ $105M.
- Genuinely attractive positioning: **beat 4 of 4 quarters** (+20.99%, +81.19%, +21.90%, +3.5%) and revision direction **improving +10.0pp** (buy 4→5, hold 4→3). Earnings inside 2026-11-04..13.
- But the arithmetic refuses it. A 2.0 ATR stop off a 220.92 entry is 204.4, i.e. 16.54 of risk. A target at the fetched 120-day high of 249.43 gives 28.51 of reward = **1.78:1, under the 2.0 swing floor**. To clear the floor the target must exceed the 120-day high, and I have no valuation anchor that defends a new high.
- I can make it pass by moving the entry down to ~215 (R:R 2.09), and that is precisely the move the strategy forbids: 215 is not a level I can point at, it is the number that makes the ratio work. Reverse-engineering the entry is the same error as reverse-engineering the stop.
- Also against: zero open-market insider buys against **7 sales worth $10.76M**, and a weak stack at 60% bullish (1 strong buy, 5 buy, 3 hold, 1 sell).
- Not captured.

## [06:22 ET] REJECTED — AFRM — insiders selling $24M and I could not re-fetch the analyst data
- Close 74.84, **ATR 3.9756 = 5.31% of price**, SMA20 74.17, SMA50 73.11, 120d range 59.75–90.44, 17.25% off the high, ADV$ $285M.
- It cleared the screen on improving revisions (+8.9pp, 83.3% bullish) and 4/4 beats, but on the confirming call `analysts AFRM` returned nulls — a rate-limit flake — so **that evidence is unverified at the time of writing** and I am not building on a number I could not re-read.
- Against it regardless: **13 insider sales worth $24.07M with zero open-market buys.** On a BNPL lender whose ATR is 5.3% of price, a 2.0 ATR stop is 10.6% wide, which pushes any floor-clearing target above the 120-day high.
- Not captured.

## [06:24 ET] CORRECTION REVERSED — APTV really does have four distinct insider buyers
The 06:14 correction was over-cautious and is itself now corrected. Printing the full name set rather
than the first four rows gives **['Agnevall Hakan', 'CLARK KEVIN P', 'MEISTER PAUL M', 'Mahoney Sean O']**
— four distinct people, $8,606,661 bought against $365,400 sold. My earlier slice showed Mahoney three
times only because I truncated to the top four rows. So `distinct_buyers` was right for APTV; what the
AMR and AMRC rows showed is that the field is unreliable *in general*, which is a different claim and
still true. APTV re-captured at the verified figure. The lesson kept: print the names, never trust the count.

## [06:25 ET] CC DATE DOUBT RESOLVED — the 06:31 rejection is overturned
The 429 error message exposed the query finnhub is actually being sent:
`from=2026-04-27&to=2026-10-30`. Every transaction it returns is therefore inside 2026, so the
August dates cannot be 2025 re-stamps and my date doubt was unfounded — the press item I found
describes a different, earlier purchase. The full list is **7 distinct insiders, 2026-08-06 to 08-12,
zero sales in six months**: HOSTETTER SHANE @ 14.94, CRANSTON MARY B @ 15.825, Martinko Joseph T. @ 15.47,
Foley Michael Robert @ 15.51, Cowan Alister @ 15.62, Dignam Denise (CEO) @ 14.95, Familiar Calderon Gerardo @ 15.53.
- **Volume-weighted insider cost basis: $488,618 / 31,537 sh = $15.49.** The stock closed **13.19**, i.e.
  14.8% below where seven insiders — effectively the board — put their own money three months ago.
- That basis is a real anchor for a target, not a fitted number, which is what makes this publishable where ARW was not.
- The fundamental objections stand and are not answered: **1 of 4 quarters beaten**, revisions
  **deteriorating -3.5pp**, RBC citing TiO2 weakness and Thermal & Specialized Solutions headwinds
  through year-end, debt-to-equity ~18.98. So it is captured at conviction 4 on three evidence kinds
  and sized as a 1% lottery ticket, not as a position. I am not claiming the counter-argument is
  answered, because I have no evidence that the TiO2 cycle turns.
- Levels: stop **12.20**, below the fetched 120-day low of 12.49, risk 0.99 = **2.07 ATR** (floor 2.0).
  Target **15.49** = the insider basis, reward 2.30 → **2.32:1**. Baseline win rate 1/(1+2.32) = 30.1%.

## [06:26 ET] REJECTED — ADT — the insider cluster is five months old and has already paid off
- 5 distinct buyers, $477,415, **zero sells** — broad and clean. But every purchase is dated
  **2026-05-08 to 05-29 at $6.75–6.91**, and the stock closed **9.87**. The insiders are up ~43%; the
  signal has been collected.
- The chart says the same: 9.87 against SMA20 **6.8325** and SMA50 **6.9248** — the price is 44% above
  its own 20-day average, 63.68% off the 120-day low and **1.25% off the 120-day high** of 9.995. A move
  of that shape in a $133M-a-day name is a corporate event I have not identified, and the universe rules
  say not to touch a move like that unless the move itself is the thesis.
- Revisions **deteriorating -14.5pp** (bullish share 45.5%) even with 4/4 beats.
- Buying 1.25% off the high on a three-month-old insider basis 43% lower is the opposite of the APTV
  setup, where the insiders are underwater and the price is near the low. Not captured.

## [06:27 ET] FALSIFICATION PASS — arguing against everything captured

**1. The rate complex carries four ideas, which is over the cap of three.**
TLT short, IYR short and ITB short are three bearish-duration positions — the stated limit. But
**XLF long is the same bet in a fourth wrapper**: a steepening curve with a 5.05% 10-year is exactly
what the three shorts need, so short duration and long banks are one view, not two. Four of twelve
ideas resolve on the long end of the curve.
- Mitigation, and it is a real one: **every one of the four is instructed to reduce or hold, none to
  add.** XLF trims half, XLE trims half, the three shorts hold unchanged with explicit do-not-widen
  instructions. No new capital is being committed to the driver, so the concentration is being worked
  down rather than built. It is still over the cap and the red team should see it stated plainly
  rather than discover it.

**2. Five of twelve ideas resolve inside a three-day window.** BCC 11/02, PFE 11/03, APTV 11/03,
CC 11/03, CVS 11/04. These are five different sectors so it is not one driver, but it is one *week*,
and a broad risk-off tape into that cluster hits all five regardless of the individual theses. Worth
the reader knowing before sizing.

**3. LULU does not survive its own numbers — changed from hold to close.**
I wrote win_probability 0.26 against a baseline of 1/(1+2.07) = **0.326**. That is a claim of
*negative* expectancy, and the strategy calls an expectancy at or below zero a hard failure. If I
genuinely believe the short is more likely to stop than to work, then "hold and let the stop execute"
is incoherent — it donates the remaining 2.18 points (2%) for nothing. The honest action is to buy it
back now. Re-captured as a buy-to-close.

**4. The strongest case against APTV, which is today's best new idea.** Four insiders bought at
48.58-50.29 and the stock is 44.43 — they are 9-12% underwater, so the cluster has already been wrong
for eleven weeks. Goldman's own target cut names the reason it could keep being wrong (Chinese vehicle
sales), revisions are deteriorating, and my 7.7x multiple is cheap only against guidance that was
itself cut once already. **It survives** because the entry is staged in thirds with the second third
explicitly withheld until 2026-11-03 confirms the guide held — so being early costs a third of a 3%
position, not the position. But it survives as a staged accumulation, not as a conviction trade, and
that is why the action text matters more than the conviction number.

**5. CC is the weakest thing captured and is marked as such.** Seven buyers is breadth, but $489K
across seven people is under $100K each — board solidarity is a real alternative explanation and I
cannot distinguish it from conviction. One beat in four quarters, deteriorating revisions, TiO2 guided
weak through year-end, 19x debt-to-equity. It is in at 1% because the target is an anchor I did not
invent and the stop is below a real low; it would not be in at 3%.

**6. HII's 430 target was inherited and I removed it from the first objective.** The thing I could not
do is defend it, and the thing I did not do is quietly keep it — it is now a second target behind the
339.76 range high. If the red team wants it gone entirely, that is a defensible cut.

## [06:29 ET] TOOLING — exit recommendations cannot pass `check_risk_reward`
`check_risk_reward` FAILs any idea without both an entry and a target, and an exit has no target by
nature — the instruction is "get out", not "get out and then go to X". So today's two closes
(**BCC**, **LULU**) will fail validation and `--enforce` will demote them to the watchlist.
- I am **not** inventing targets to make them pass. A fabricated target on an exit is worse than a
  demoted row, because it would read as a new position.
- **Note for synthesis:** these two are the most actionable items in the whole report and they will
  arrive flagged as failures. Carry them in the report text and in `data_quality_notes` regardless of
  where enforcement puts them. A demoted "close this" that the reader never sees is the one failure
  mode that costs real money today.

## [06:30 ET] DELIBERATE NO-ACTION HOLDS — six positions reviewed, no amendment
NKE, KHC, STLD, UNP, ABT, PYPL were each checked against fetched 10/29 closes in the 06:17 sweep and
need no change: all are within their published levels, none is near a stop or a target, and none has
new information against it. **No candidate was captured for them, and the absence of a row is the
recommendation** — not an oversight and not a truncated run. The two defects found among them
(STLD/UNP/PYPL stops at 1.87/1.84/1.83 ATR, under the 2.0 floor) are pre-existing fills whose entries
cannot be changed and whose stops would only get worse by widening, so they are logged as a pattern
rather than amended.

## [06:28 ET] REJECTED — BG — insider-basis target does not clear the 2.0 floor
- Bunge, close **96.02**, which is 0.3% above its own 120-day low of 95.75 and 28.8% off the 134.865 high.
  Price below SMA20 104.319 below SMA50 111.0126 — an unbroken downtrend, not a base. ATR 3.0321, ADV$ $166M.
- One buyer only: Christopher Mahoney, 6,500 sh across 2026-07-31 and 08-04, $689,050, zero sells —
  volume-weighted **$106.01**, so he is ~9.4% underwater. 90% bullish but **flat** revisions, 3/4 beats.
  Earnings 2026-11-03 bmo.
- The same arithmetic that killed ARW: a 2.0 ATR stop below the 120-day low is ~89.50 (risk 6.52 =
  2.15 ATR), and a target at the insider basis of 106.01 gives 9.99 of reward = **1.53:1**. Under the floor.
  One underwater buyer is not enough to justify reaching past his own basis for a target. Not captured.

## [06:29 ET] REJECTED — CDW — same shape as ADT: stale cluster, price at the high, net selling
- Close **165.20**, **0.57% off the 120-day high** of 166.15, far above SMA20 151.03 and SMA50 146.68.
- Buys are CEO Christine Leahy @ 103.395 (2026-05-18) and David W Nelms @ 111.43 (2026-05-27) — five
  months old and up roughly 50%. And they are **net sellers**: $2.51M bought against $3.67M sold.
- Flat revisions, 3/4 beats. The cluster has been collected; buying it now is paying 50% more than the
  insiders did for the same information. Not captured.

## [06:30 ET] CONVICTION SCORES — four deliberate mismatches with the mechanical count, and why
`check_conviction_evidence` derives the score from the number of distinct evidence kinds. Four rows
are scored **below** what that count implies, and in three cases that is intentional rather than an error:
- **FCX (2 kinds, scored 2 not 3)** and **ITB (2 kinds, scored 2 not 3)** — because *the evidence
  points against the position*. FCX's two kinds are "closed below both moving averages" and "insiders
  sold $8.39M with zero buys"; both are bearish facts on a long. **Counting evidence kinds without
  regard to their direction means evidence against an idea raises its conviction**, which is plainly
  wrong, and I am not going to score a deteriorating long a 3 because I documented why it is
  deteriorating. The red team should read these two as 2.
- **BCC (4 kinds, scored 4 not 5)** — the four kinds genuinely support the exit, but the
  counter-argument is live (3 of 4 quarters beaten, plywood pricing +5% above the Q2 average), so 4 is
  the honest number for a decision to sell before a print that could beat.
- **CVS (4 kinds, scored 4)** — this one I have corrected *upward* to 5 and re-captured. My reason for
  holding it at 4 was the $359M of insider selling, but I had already counted the weighing of that
  selling as the fourth evidence kind, so scoring it down again was double-counting a single concern —
  a feeling overriding the count, which is exactly what the conviction rule exists to stop. The concern
  now lives only in `counter_argument`, where it belongs.

## [06:31 ET] RELATIVE STRENGTH — both new ideas are laggards, not leadership. Stated, not hidden.
| Name | 1m | 3m | 6m | peer 1m | peer 3m | peer 6m | SPY 1m/3m/6m |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APTV vs XLY | +3.28% | -21.32% | -26.27% | +6.76% | +0.09% | -1.82% | +0.88 / +2.99 / +7.05 |
| CC vs XLB | **-2.80%** | -20.59% | **-51.06%** | +7.86% | +4.16% | +2.06% | same |
- **APTV** is beating SPY over 1 month (+3.28 vs +0.88) but still trailing its own sector (+6.76), and it
  is 21 points behind XLY over 3 months. The thesis is explicitly mean reversion to a valuation anchor,
  not momentum, so a laggard is what it is *supposed* to look like — but it has not yet begun
  outperforming even its sector, so there is no confirmation of the turn, only the insider cluster and
  the multiple. Added to the counter-argument rather than left out.
- **CC is the damaging one.** Down 51.06% over six months while materials rose 2.06%, and over the last
  month it is still *falling* (-2.80%) while XLB rallied 7.86%. There is no sign of a turn on any
  timeframe. It stays captured only because it is already sized as a 1% lottery ticket with a target
  that is the insiders' own basis and a stop below a real low — but this is now the second independent
  strike against it after 1-of-4 beats, and it is the first row the red team should consider cutting.
- Both re-captured with the figures in `counter_argument`.

## [06:32 ET] DATA GAP — options-implied move unavailable
`implied APTV` and `implied CC` both returned **HTTP 401 Unauthorized** from yahoo-options. So the
strategy's "what does the options market already price" check **could not be run for any idea today**,
and no straddle-implied move or target-in-sigma figure appears anywhere in this research. Recording it
rather than reasoning around it: for APTV the 57.00 target is +28% from the entry, and whether the
options market considers that ordinary or a disagreement is simply unknown to this run.

## [06:33 ET] RESEARCH COMPLETE
Started 06:01:07 ET, finished 06:33 ET — inside budget, not truncated. This block exists, so nothing
above was cut off mid-write.

- **candidates: 13 distinct symbols across 20 capture lines.** Synthesis takes the last line per
  symbol. The re-captures are deliberate corrections, not duplicates: APTV ×3 (insider count restated
  down, then verified back up, then relative strength added), CVS ×2 (conviction corrected 4→5), CC ×2
  (relative strength added), XLE ×2 (stop moved back below entry so the row can validate), LULU ×2
  (hold changed to close after the falsification pass).

**What is in the file**
- 2 new ideas: **APTV** (long_term buy, conv 5) and **CC** (swing buy, conv 4, 1% lottery ticket)
- 2 closes, and these are the most actionable rows: **BCC** sell to close a long, **LULU** buy to close a short
- 9 position updates: CVS, PFE (hold, explicitly do not add), XLE and XLF (trim half), HII (trim a
  third, trail 290), TLT / IYR / ITB (hold, do not widen), FCX (hold to the stop, stop re-pitching it)

**Not in the file, deliberately**
- 6 no-action holds: NKE, KHC, STLD, UNP, ABT, PYPL — reviewed against fetched closes, no change warranted
- 3 pending orders that should be cancelled rather than re-pitched: **VST** @132.0, **OXY** @54.0,
  and **KXCPIYOY-26SEP-T3.5** NO @18 (references September CPI, already resolved)
- 10 names researched and rejected with reasons: ARW and BG (fail the 2.0 R:R floor on any defensible
  target), AFRM, ADT and CDW (stale or contradicted insider signals), AMR, AMRC, ACDC, AGBK
  (single-buyer or stale clusters misreported as clusters by `distinct_buyers`)

**Pronounced skew, which synthesis should state rather than apologise for**
- **Horizon:** 10 swing, 3 long_term, **0 intraday.** No intraday setup was pursued because no index
  level could be fetched at all (see gaps) — an intraday idea with no reference price would be invented.
- **Asset class:** all 13 are stocks and ETFs. **No crypto, no futures, no event contract**, each for a
  specific tooling reason below rather than because none was attractive. The universe config explicitly
  prefers futures for index and crypto views, and this run could not price a single one.
- **Only 2 of 13 rows are new ideas.** That is the intended shape today: 29 closed trades at a 10% hit
  rate and -5.8% average is above the ~15-trade noise threshold, so the bar was raised and the time
  went into managing 17 open positions rather than adding to them.

**Coverage gaps and failed sources**
- **Yahoo HTTP 429 throughout**: no level available for SPX, NDX, DJI, RUT, VIX, /ES, /NQ, DXY, 10y, gold
  or WTI. The macro regime was reconstructed from FRED and CoinGecko instead.
- **No crypto price history** (`history BTC-USD` failed on nasdaq and yahoo). Spot was available but ATR
  was not, so no stop could clear the 2.5 ATR crypto floor from real data.
- **No usable event contracts**: "CPI", "inflation", "unemployment", "recession", "interest rate" all
  returned empty; "Fed" returned tennis markets with null prices.
- **Options-implied unavailable**: yahoo-options returned HTTP 401 for every symbol, so the
  "what does the options market already price" check ran for nothing today.
- **finnhub rate-limited mid-run, self-inflicted.** My 198-symbol insider screen exhausted the budget
  and briefly broke `insiders`, `quote` and `analysts`. It recovered, but it cost the re-verification of
  AFRM's analyst data, which is why AFRM was rejected partly as unverified.

**Two tooling defects found, both recorded above and both affecting this report's own output**
1. `check_direction` rejects a long whose stop sits above its entry, so a protective trail on a winner
   cannot be expressed in the `stop` field (XLE, HII, XLF put it in `catalyst.action` instead).
2. `check_risk_reward` fails any idea without a target, so both exits (BCC, LULU) will be demoted to
   the watchlist. **Synthesis must carry them in the report text regardless of where enforcement puts
   them** — a "close this position" that the reader never sees is the only failure here that costs money.
