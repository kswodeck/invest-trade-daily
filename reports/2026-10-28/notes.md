# Research log — 2026-10-28

## [06:03 ET] MACRO — rates, dollar, equity indices
- FRED (fetched): US10Y **5.00%** (2026-10-26), US2Y 4.68%, Fed funds eff 3.88%,
  10y-2y curve **+0.29** (2026-10-27), unemployment 4.2% (Sep), CPI index 336.298 (Sep)
  — source: https://fred.stlouisfed.org/
- 10y at 5.00% with fed funds at 3.88% = a steepening, term-premium-driven back end.
  That is the single most important macro fact today: long duration is being repriced
  while the front end is anchored. Bearish long bonds, bearish long-duration equity
  proxies (REITs, homebuilders, utilities), supportive of banks' NIM.
- TLT proxy `bonds_20y` (finnhub, pre-market): 81.63, -0.06% — source: finnhub quote
- **DATA GAP**: ^GSPC, ^NDX, ^DJI, ^RUT, VIX, ES, NQ, DXY, ^TNX, gold, WTI all
  returned ok:false. Yahoo is HTTP 429 (rate-limited) across the board; finnhub
  rejects CFD indices without a subscription; stooq 404s on ^-prefixed symbols.
  Index level, VIX and overnight futures are **unknown** this morning.

## [06:08 ET] MACRO — THE REGIME: the Fed is HIKING, and the decision is TODAY 14:00 ET
This reframes the whole book. Verified facts:
- **FOMC meets Oct 27-28 2026; statement today 14:00 ET, presser 14:30 ET.** No SEP
  at this meeting. — source: https://fedratecalc.com/fomc-meeting-schedule/october-2026/
- **Sept 16 2026: the Fed HIKED 25bp to 3.75%-4.00%, unanimous 12-0 — its first
  increase since 2023.** Committee called inflation "elevated". Chair **Kevin Warsh**
  (took over May 2026): "inflation is too high and has been for too long"; said
  underlying inflation trends had not meaningfully improved. Oil prices tied to the
  **US-Iran conflict** cited as a key driver.
  — source: https://www.cnbc.com/2026/09/16/treasury-yield-bond-market-fed-decision.html
- Corroborated by FRED: effective fed funds 3.88% = midpoint of 3.75-4.00%.
- **10y closed ~5.01% on hike day, highest since 2007**; had crossed 5% on Sep 14;
  reported ~5.17% in late September. Today FRED has it back at **5.00%** (10/26).
  — source: https://www.cnn.com/2026/09/16/business/live-news/federal-reserve-interest-rate-september
- **Late Sept: >70% odds priced of ANOTHER hike in October, and 16 of 19 FOMC
  members projected at least one more hike by year-end.**
  — source: https://easternherald.com/2026/09/25/us-treasury-yield-19-year-high-fed-october-hike-warsh/
- Curve: 2y 4.68% sits **80bp ABOVE** effective funds 3.88% — the market prices
  roughly three more hikes. 10y-2y +0.29 and steepening from the long end.

### What follows for today, mechanically
- Long-duration liabilities get repriced: **REITs, homebuilders, utilities, long
  bonds** are the structural shorts in this regime (IYR, ITB, TLT already on the book).
- **Banks** benefit from a steeper curve and a higher front end (XLF on the book).
- A hawkish hold or a hike both keep the trade intact; the risk is a dovish surprise
  from a Chair who has given no reason to expect one.
- **Nothing should be entered before 14:00 ET today.** Any intraday or swing entry
  priced this morning is priced into a known binary four hours away. Where a level
  is unchanged, the right action is wait-for-the-statement, not front-run it.

## [06:08 ET] DATA GAP — Kalshi "Fed" query returned 0 markets (ok:true, count:0)
So I cannot quote a live implied probability for today's decision from our own feed.
Will not state one I did not fetch.

## [06:12 ET] MACRO — what is actually priced for today, and where the real catalyst is
- **Today's decision is a near-certainty and therefore NOT a trade.** Kalshi ~93%
  hold / ~6% hike 25bp / ~1% cut; CME FedWatch 92.8% hold into the close; a Reuters
  poll had 94 of 100 economists expecting no change.
  — source: https://www.forbes.com/sites/digital-assets/2026/10/27/markets-predict-over-90-odds-fed-will-leave-rates-unchanged-this-month/
  — source: https://news.kalshi.com/p/interest-rate-odds-fed-october-2026
- **The repricing is in December, and it has moved hard.** CME-based odds of a
  December hike **73%, up from 42% one month ago**; Kalshi ~79%. And **all 100** of
  the Reuters-polled economists forecast a December hike.
  — source: https://www.kiplinger.com/investing/live/fed-meeting-updates-and-commentary-october-2026
- Backdrop: **CPI +3.7% y/y through September**; **nonfarm payrolls +29,000**. That is
  the conflict — inflation well above target with a labour market close to stalling.
  "A two-speed economy, with AI and housing at the poles."
  — source: https://fortune.com/2026/09/22/fed-rate-hike-housing-debt-borrowing-costs/
- So the tradeable event today is **the statement language and the Warsh presser**,
  which is what marks December to market. Not the decision.

## [06:12 ET] CALENDAR — dated prints bearing on the open book (fetched)
- **Today AMC**: GOOGL, MSFT, F, TMUS, FDX, CVNA, ORLY, BSX, GEV. Today BMO: AEP, PSX.
- **Oct 29 BMO: DHI** (the ITB catalyst), CAT, LLY, MRK, MA, TT, CARR, LHX; **AMC**: AMZN, INTC, SBUX, GILD.
- **Oct 30 BMO: XOM and CVX** (together a large share of XLE), **D, EXC** (utilities), ABBV, CL, REGN.
- Nov 3 BMO: **PFE** (open position). Nov 4 BMO: **CVS, KHC** (open positions).
- Nov 5: **SPG** (the REIT read-through for IYR), DUK, SO, ED, NRG, COP, EOG, DVN.
- Nov 6: **VST** (awaiting entry @132). Nov 9 AMC: **OXY** (awaiting entry @54), CEG.
- Nov 11: **SMMT** (awaiting entry @17.1).

## [06:13 ET] TRACK RECORD — reading it honestly, because 29 closed is no longer noise
- Overall 3/29 to target (10%), avg **-5.8%**. Two splits are large enough to act on:
  - **By conviction, the evidence count is working as designed**: conviction 4 is
    2/6 (33%) and avg **+0.1%**; conviction 3 is 1/17 (6%), avg -7.0%; conviction 2
    is 0/6, avg -8.4%. More independent confirmations -> materially better outcomes.
  - **By asset class, ETFs beat single names by a wide margin**: etf 2/9 (22%), avg
    **-2.0%** vs stock 1/20 (5%), avg **-7.6%**.
- Both point the same way: this report is better at regime and sector calls than at
  single-name timing. So today's bar: **prefer the ETF or futures expression of a
  macro view, and treat conviction 3 as the exception rather than the default.**
- The last five stop-outs (CEG, DAL, SMMT, GE, ITA) were **all longs**, four of five
  conviction 3. Consistent with the above.

## [06:13 ET] POSITION UPDATE — IYR — opened 2026-09-02, -1.1%
- decision: **hold**, amend stop 100.40 -> 100.60, target 90.50 unchanged
- why: the old stop was 1.79 ATR from entry, just under the 1.8 ATR ETF floor. Fixing
  a stop that sat below the volatility floor, not walking it to flatter the ratio
  (the risk got WIDER, the ratio fell 2.81 -> 2.61). SPG reports Nov 5.
- action: captured via add_candidate.py

## [06:17 ET] HOUSING — the fundamentals got worse while the stocks went up
- **September pending home sales: record-low index reading of 66.** Builders are
  cutting prices at a **record pace**; 30-year fixed averaged **7.32%** in the week
  of 10/22, down from 7.40%.
  — source: https://247wallst.com/investing/2026/10/27/builders-are-slashing-prices-at-a-record-pace-as-the-housing-market-freezes/
- **The 10/22 homebuilder rally was a rotation, not a housing event.** XHB +3.8%,
  LEN +9% on a day the Nasdaq fell; attributed to lower rates, tech investors
  looking elsewhere, and cheap valuations — and it landed on the same day as the
  record-low pending sales print.
  — source: https://www.fool.com/investing/2026/10/23/if-the-ai-bubble-bursts-these-stocks-will-be-winners/
- ITB fetched levels: close 90.35, ATR14 2.4196, 200-day SMA **96.32** overhead,
  20-day 86.75, 50-day 90.05, 400-day range 82.08–118.00. The 10/22 bar ran
  85.97→91.34 on 3.14m shares. Swing high 91.67 (10/26).

## [06:17 ET] POSITION UPDATE — TLT — opened 2026-09-24, -2.2%
- decision: **EXIT.** Hold into 14:00 ET with the 82.00 stop unchanged per the
  2026-10-25 plan, then be flat by Friday's close regardless.
- why: geometry, not a changed macro view. 81.63 is **0.47 ATR** from the 82.00 stop
  and 7.5% from the 75.70 target — nearly the whole remaining distribution is a
  loss. And what happened was a **flattening**: 10y 5.17% (late Sep) → 5.00% (10/26)
  while December hike odds went 42% → 73%. Front end hawkish, long end bid = the
  market pricing a policy error on a 29k payroll print. That is the opposite of the
  trade I was in. Widening 82.00 to survive today is the banned move.
- action: captured via add_candidate.py

## [06:17 ET] POSITION UPDATE — ITB — opened 2026-09-30, -0.1%
- decision: **HOLD what is filled, ADD NOTHING.** Stop of record 93.60 unchanged.
  Carry-or-exit decided on the DHI reaction tomorrow, not today.
- why: the thesis is the best on the board (above) and DHI reports 10/29 BMO — closing
  a short the day before its catalyst is bad timing. But the position's geometry is
  broken and cannot be repaired: 93.60 is **1.57 ATR** from entry, inside the 1.8 ATR
  ETF floor, and widening it to the only real level overhead (the 200-day at 96.32)
  puts risk at 6.52 vs 8.30 reward = **1.27 R:R**, which fails. A filled position's
  entry may not be amended, so there is no version of this row that publishes
  cleanly. Hence hold-only, and expect validation to flag the stop. That flag is
  correct and I am not dressing it up.
- action: captured via add_candidate.py

## [06:20 ET] ENERGY — the single most important finding of this run
The oil complex is a geopolitical position, not a supply/demand one, and the
asymmetry has just flipped.
- **There is an active US-Iran war with exchanged strikes.** Brent ~$112-116, WTI
  ~$100-103. Earlier in the move Brent passed $117 and WTI $103; Brent was $104.28
  on 10/08 and ~$90 roughly two months ago.
  — source: https://oilprice.com/Energy/Oil-Prices/Oil-Prices-Surge-as-US-and-Iran-Exchange-Strikes.html
  — source: https://www.cnbc.com/2026/10/08/oil-prices-today-brent-wti-hormuz.html
- **Physical disruption is real and large: ~9.5 mbd exited Hormuz in the week ended
  Tuesday, ~30% below pre-war normal (Kpler).**
  — source: https://moneycheck.com/oil-prices-today-brent-and-wti-swing-as-iran-talks-continue
- **And diplomacy is live: Saudi, Turkish and Pakistani officials have travelled to
  Tehran to discuss an end to hostilities.** Oil has fallen on talks headlines even
  with the threat of new US strikes.
  — source: https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Drop-Despite-Threat-of-New-US-Strikes-on-Iran.html
- Yesterday's tape agrees: **XOM -2.51%, CVX -1.63%, XLE -2.05%, USO -1.41%.**
- XLE fetched levels: 68.21, only **2.36% off its 140-day high** (69.86) and
  **+29.63% off its low** (52.62). ATR 1.4936, sma20 66.11, sma50 64.61.
- **Read:** a +9% long in XLE is a long war-premium position that has already been
  paid, held into live peace talks, with XOM and CVX — a large share of the fund —
  reporting Friday BMO. Continued war is largely in the price; a ceasefire is not.
  Exit. **Do NOT flip short**: Hormuz at -30% means one strike gaps it the other way,
  and selling a physical shortage because the diplomats are travelling is how you get
  run over.

## [06:20 ET] MACRO — the link that makes the rest of the report consistent
Energy is the inflation driver the Fed named by name. So the November CPI ladder and
the December hike contract are both, underneath, **long the war**. That matters for
the event-contract section below: the market's 23% December-hold probability is
plausibly pricing the peace scenario that a forecaster survey does not contain. The
apparent "edge" of 100/100 economists against a 75c contract is mostly this.

## [06:20 ET] REJECTED — KXFEDDECISION-26OCT-H0 — today's decision is settled at 94/97, no edge at any size
Live orderbook fetched 06:1x ET: "Fed maintains rate" YES bid **94** / ask **97**, with
>$1.2m resting on the NO book. H25 (hike 25bps) 3/6. There is nothing to disagree with.

## [06:20 ET] REJECTED — KXFEDDECISION-26DEC-H25 — right side, fails the reward-to-risk floor
Live orderbooks fetched this morning for the Dec 9 meeting:
- H25 "Hike 25bps": YES bid **74** / ask **77**; last trade **75c** at 09:29:40Z today
- H0 "Fed maintains rate": YES ~**22/24**
- H26 "Hike >25bps": YES ~**4/6**;  C25 "Cut 25bps": YES ~**1/3**
So P(any December hike) ~= **80%**, P(hold) ~= 23%.
Directionally I agree with YES — all 100 Reuters-polled economists forecast a December
hike and 16 of 19 FOMC members projected one by year-end — but **buying at 77c to
resolve at 100 is 23 of reward against 77 of risk, a ratio of 0.30 against a 2.0
floor**, and no honest stop fixes it (a stop at 65 gives 1.92, and a 9c stop to reach
2.56 is inside the noise of a 72-77 market). A high-probability YES is structurally
the wrong side of an event contract. Rejected on arithmetic, and see the oil note
above for why the residual 23% is probably not free money either.

## [06:20 ET] REJECTED — KXCPIYOY-26NOV ladder — coherent distribution, no defensible disagreement
Live ladder fetched (next open print; closes 2026-12-10). YES bid/ask: >3.4% 96/97,
>3.5% 94/95, >3.6% 84/90, >3.7% 74/76, >3.8% 62/63, >3.9% 44/45, >4.0% 31/32,
>4.2% 11/18, >4.5% 8/9. Implied median ~**3.85-3.90%**, i.e. the market already prices
acceleration from the September 3.7%. I have no inflation model that beats that, and
"feels underpriced" is banned. Noted oddity: >4.5% asks 9 while >4.2% bids 11, which is
a 2c ladder inconsistency in a thin market, not a tradeable idea at this size.
No October CPI market exists on Kalshi, so the next print is November.

## [06:20 ET] REJECTED — /MBTZ6 short — the conditional trigger did not fire
The 2026-10-25 pitch was explicit: "WAIT for a daily close below 79,263... If 79,263
holds through the week, there is no trade." BTC is **81,396, +2.44% on 24h** (CoinGecko,
fetched). The level held and price is moving away from it. No trade, by the plan's own
terms. ETH 2,366.76 (+3.0%), SOL 102.88 (+3.71%) — the whole complex is bid, which is
the opposite of the setup.

## [06:20 ET] REJECTED — XLU short — the bond-proxy thesis is contradicted by the AI power story
XLU 42.85, +9.79% off its 140-day low, back above both the 20-day (41.44) and 50-day
(41.81) — the same bounce shape as IYR and ITB. But utilities are *both* poles of the
two-speed economy: they are long-duration bond proxies AND the datacenter power demand
trade. This report is already long that demand story through VST (awaiting entry), and
CEG was stopped out of it. Shorting XLU would be betting against a thesis the same
report holds. It would also be a third idea on one driver, at the correlation cap.
Rejected on coherence, not on the chart.

## [06:22 ET] NEW IDEA — IWM short — the index divergence is the cleanest read on the tape
Fetched levels (all three same call):
- SPY **769.66**, only -1.53% off its high (781.62), sitting ON its 20-day (770.41) and
  50-day (767.53). ATR 7.28 (0.95%).
- QQQ **721.25**, -5.45% off its high, **below** 20-day (733.18) and 50-day (725.26).
- IWM **280.18**, -8.19% off its high (305.18), **below** its 50-day (285.37).
So the index is fine, the Nasdaq wobbled, and **small caps are the weakest cohort.**
Relative strength confirms it is small-cap-specific, not risk-off: IWM is negative vs
SPY on **every** window (-0.47% 1m, -8.42% 3m, -5.86% 6m) while QQQ is **+3.48%**
relative on 3m.
- Mechanism: Russell 2000 balance sheets carry floating-rate debt that reprices with
  the front end, not on a refi calendar. Front end 3.88%, ~80% priced on a Dec hike.
- October structure: a 269.88-284.64 range. Swing-high cluster **283.57 / 284.24 /
  284.64** sits right under the 50-day at **285.37** — a genuine confluence. Low shelf
  269.88 / 270.35.
- Setup: **wait**, sell 283.00-285.20 (ideal 284.20) after 14:00 ET, stop 290.80
  (1.85 ATR, beyond the confluence), target 269.90 (the October range low, R:R 2.17),
  target_2 258.90 (the 140-day low). Invalidated by two closes above 285.40.
- **Correlation note: this is the THIRD idea on the hiking-Fed driver** (IYR, ITB, IWM)
  and therefore exactly at the cap. XLF long is the same driver inverted, which is a
  hedge rather than a fourth leg, and TLT comes off today. Stated in key_risk.
- action: captured via add_candidate.py

## [06:22 ET] POSITION UPDATE — BCC — opened 2026-08-18, -6.9% vs entry (last 76.02 vs 76.50 entry)
- decision: **CLOSE at the open.**
- why: it is a straight contradiction, not a call on the stock. Boise Cascade sells
  wood products into single-family starts; the housing data I fetched this morning —
  record-low pending sales, record-pace builder price cuts, 7.32% mortgages — is the
  same evidence justifying the ITB short. Long building products + short homebuilders
  on one dataset is paying two spreads to be flat. The accumulation case needed a
  trough forming; this is a trough deepening, which is the thesis's own invalidation.
  Exit is near-free at 76.02 vs a 76.50 entry. Also the thinnest name in the book at
  **$25.5m** average dollar volume — leave while the exit is cheap.
- action: captured via add_candidate.py

## [06:22 ET] POSITION REVIEW — the remainder, decided and deliberately NOT re-published
Reviewed with fetched prices; no new instruction needed, so no candidate written. A
re-pitch with nothing changed is the anchoring this report is told to avoid, and these
symbols are already at 4-7 publications in ten days.
- **FCX** 65.95 (-4.5%): exit already ordered twice (10/26 "exit at Monday open",
  10/27 "be flat into it") and the print has passed — it is not on the fetched
  calendar through 11/09. Price is **below both the 20-day (69.83) and 50-day (71.81)**
  and -17.81% off its high, with a 78.5 target 19% away. The standing exit stands;
  reaffirming it a third time adds nothing.
- **PFE** 29.80 (+7.9%): **reports 11/03 BMO.** Only -2.10% off its 140-day high
  (30.44) and +26.16% off its low. long_term valuation thesis to 42.00, no stop by
  design. Hold through the print — a 4-session print does not settle a multi-year
  pipeline thesis — but it is published 7x in 10 days and needs no new row today.
- **STLD** 246.80 (now above its 245.50 entry, +3.89% yesterday): above both the
  20-day (238.65) and 50-day (236.81), +32.42% off its low. Stop 228.75 is 1.94 ATR
  from entry against a 2.0 stock floor — marginally tight, but it is a filled position
  whose entry cannot be amended and the ratio to 281.00 is 2.12. Hold as is.
- **KHC** 24.06 and **CVS** 91.13: both report **11/04 BMO**. The 10/27 report already
  set the carry-or-exit decision for 11/03. That plan is correct and dated; leave it.
- **NKE** 37.56: 10/27 set a cover rule on two closes above 38.50. Unchanged.
- **LULU** 104.59 (-2.3%), **HII** 281.32 (+7.3%), **UNP** 299.88 (+2.9%), **ABT**
  103.10 (+1.8%), **PYPL** 56.09 (1 day old, -2.7%): no new information, no dated
  catalyst inside 10 sessions on the fetched calendar, levels of record intact. Hold.
- **Awaiting entry, unchanged and still unfilled**: VST 132.00 (reports 11/06),
  OXY 54.00 (reports 11/09 AMC), AAL 13.35, KXCPIYOY-26SEP-T3.5 NO @18 (that
  September print has resolved — no October market exists on Kalshi, so this row is
  stale and should not be carried forward).

## [06:24 ET] INSIDER SCREEN — ran it, found nothing, which is not a negative
Checked `market_data.py insiders` on the de-rated names with prints inside two
sessions: **MRK 0 buys, GILD 0, CL 0, REGN 0, F 1 buy / 1 distinct buyer.** No
cluster anywhere, so no idea earns a `positioning` kind from insider activity today.
Per config, absence of insider buying is not evidence against a name — it simply means
the signal is unavailable and no thesis today leans on it.

## [06:24 ET] REJECTED — KIE long (insurance, long_term) — no defensible valuation anchor
The mechanism is the best structural one this regime offers: P&C float reinvested at a
5.00% 10-year against a legacy portfolio yielding far less is a multi-year earnings
tailwind that does not depend on guessing a reaction to a print. Fetched levels: KIE
62.46, ATR 0.9525, 20-day 61.23, 50-day 61.98, range 54.13-66.53 (-6.12% off high),
ADV $73.3m. Relative strength +2.05% vs XLF on 1m, -3.56% on 3m.
**Rejected on two counts, both hard:**
1. A `long_term` idea needs a defended valuation target and a **bear case with a
   price**, at a 2.5 R:R. I have no book value, ROE or combined-ratio data from any
   source I can reach this morning, so any target would be a number I made up.
   Config is explicit: "A long-term idea whose downside you cannot put a price on is
   not researched enough to publish."
2. Taken as a swing instead, it is the **fourth** idea on the hiking-Fed driver after
   IYR, ITB and IWM, which breaks the correlation cap of 3.
Worth revisiting when a fundamentals source is available. Not today.

## [06:24 ET] LONG_TERM LANE — nothing published, and the reason is not laziness
This lane got deliberate time rather than leftovers, and produced **one close (BCC) and
zero new entries.** Two reasons, stated so synthesis can say it plainly:
- The lane's own record is the worst in the book — **0/4 to target, avg -15.2%** — so
  the bar was raised, not lowered, and nothing cleared it.
- A 5.00% risk-free rate is the hurdle every long-term valuation has to clear, and
  clearing it requires fundamental data (earnings power, book value, balance sheet)
  that no reachable source gave me this morning. A long-term thesis built on a chart
  is a swing trade wearing a longer horizon, and the lane already has four of those.

## [06:25 ET] FALSIFICATION — every captured idea's arithmetic recomputed from fetched inputs
Floors: swing R:R 2.0; stop 1.8 ATR (etf), 2.0 ATR (stock); expectancy > 0.
| Idea | Risk | Reward | R:R | Stop ATR | Baseline | Claimed | Edge | Expectancy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IYR short 97.80/100.60/90.50 | 2.80 | 7.30 | **2.61** | **1.93** ok | 0.277 | 0.40 | +12.3 | +0.44R |
| IWM short 284.20/290.80/269.90 | 6.60 | 14.30 | **2.17** | **1.85** ok | 0.316 | 0.44 | +12.4 | +0.39R |
| XLF long 54.23/52.80/57.60 | 1.43 | 3.37 | **2.36** | **2.00** ok | 0.298 | 0.48 | +18.2 | +0.61R |
| ITB short 89.80/93.60/81.50 | 3.80 | 8.30 | **2.18** | **1.57 FAILS** | 0.314 | 0.42 | +10.6 | +0.34R |
| XLE exit 63.90/60.80/70.50 | 3.10 | 6.60 | **2.13** | **2.08** ok | — | — | — | exit, no claim |
| TLT exit 79.90/82.00/75.70 | 2.10 | 4.20 | **2.00** | **2.67** ok | — | — | — | exit, no claim |
- **ITB's 1.57 ATR stop is a real failure and is disclosed in its own key_risk.** It is
  left alone rather than widened because the entry of a filled position may not be
  amended and widening to the only real level overhead (the 200-day, 96.32) drops the
  ratio to 1.27. Expect validation to flag it; the flag is correct.
- No idea needed a tight stop to clear its ratio: every stop was placed at a fetched
  structural level **first** (IYR the falling 50-day at 99.19; IWM beyond the
  283.57/284.24/284.64 cluster and the 50-day at 285.37; XLF below the 50.42 range
  base), and the target checked afterwards.
- Both exits (XLE, TLT) and both withdrawals (GLD, BCC) carry **no win_probability**,
  following the 10/26-10/27 precedent: a close instruction asserts no edge on reaching
  the target, so stating one would be a fabricated number.
- **Conviction is scored one below the mechanical distinct-kind count on five ideas**
  (IYR, ITB, XLF, TLT, BCC), deliberately. Several `counter_argument_answered` entries
  are reasoning over evidence already cited under another kind rather than independent
  confirmations, so the honest independent count is one lower. Validation will flag the
  disagreement and name the higher score; it should not be raised. The track record is
  why — conviction 4 is the only cohort with a non-negative average (+0.1%) and six
  freshly-minted 5s would destroy exactly the signal that table just started to carry.
- **Correlation cap: at 3 and not over.** IYR, ITB and IWM are one driver (the hiking
  Fed de-rating long-duration and rate-sensitive assets). XLF is that driver inverted —
  a hedge, not a fourth leg. TLT comes off today. KIE was rejected for being the fourth.

## [06:25 ET] RESEARCH COMPLETE
- candidates: **9 captures across 8 distinct symbols** (XLE captured twice; the second
  entry supersedes). Five are decisions on the live book (IYR amend, TLT exit, ITB
  hold-only, XLE take-profit, XLF hold), two are withdrawals (GLD unfillable order,
  BCC thesis contradiction), **one is a new entry (IWM short, and it is a WAIT)**.
- **Deliberately thin on new ideas.** With 17 open positions, a 10% hit rate over 29
  closed trades and five straight stop-outs, the useful work today was pruning and
  resolving contradictions, not adding rows. One new entry is the honest count.
- coverage gaps:
  - **Index levels, VIX, overnight futures, DXY, spot gold and spot WTI were all
    unfetchable** — Yahoo returned HTTP 429 across every symbol, finnhub requires a
    subscription for CFD indices, stooq 404s on `^`-prefixed tickers, no AlphaVantage
    key. Index ETFs (SPY/QQQ/IWM) and FRED filled most of the gap; **no futures
    contract price could be fetched at all**, which is why the small-cap short is
    expressed as IWM rather than the preferred /M2K. That is a data limitation, not a
    style choice.
  - **No fundamentals source reachable**, which is what killed the long_term lane.
  - `market_data.py events` returned `count: 0` for every Fed, rates and inflation
    query and one garbage row for "CPI" — the Kalshi path in that subcommand looks
    broken. Worked around by querying `api.elections.kalshi.com` directly, where the
    `/orderbook` endpoint gave live two-sided prices even though `/markets` returns
    null bid/ask/last fields. **Worth fixing in `market_data.py`.**
  - Could not confirm today's FOMC outcome (it has not happened) nor a live intraday
    index print. Every price in these notes is a prior close or a pre-market quote and
    is labelled as such.
- sources that failed: Yahoo Finance quote/chart API (429, all symbols), finnhub index
  quotes (subscription), stooq (404 on indices), AlphaVantage (no key),
  `market_data.py events` (0 results), kalshi.com web UI (429), Kalshi
  `/markets/<ticker>` price fields (null).
