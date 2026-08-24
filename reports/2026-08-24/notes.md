# Research log — 2026-08-24

## [06:42 ET] MACRO — rates, regime, data availability
- FRED (2026-08-20/21): US10Y 4.69% (prev 4.65), US2Y 4.19%, Fed funds effective 3.63%, 10y-2y curve +0.50, unemployment 4.1% (Jul, down from 4.2%), CPI index 332.813 (Jul). Source: FRED via scripts/market_data.py macro
- **Long end is selling off while the front end is anchored** — 10s +4bp on the day, 2s flat. Curve steepening at +50bp. That is a term-premium / fiscal move, not a policy repricing. Bearish for long duration (TLT open position) and for rate-sensitive equities; supportive for banks' NIM but the KRE trade already stopped out.
- TLT last 82.05 as of 2026-08-21 close (finnhub, age 3759 min = previous close, market closed). Open TLT long from 08-20 @82.60 is -0.7%.
- DATA GAP: Yahoo Finance returned HTTP 429 (rate limited) for every index/futures/FX symbol. SPX, NDX, DJI, RUT, VIX, /ES, /NQ, DXY, US10Y quote, gold, WTI all `ok:false`. Finnhub covers single-name equities/ETFs only ("Market data subscription required for CFD indices"). **No live index level, no VIX, no DXY today.** Recorded for data_quality_notes.
- Crypto (CoinGecko, live): BTC $77,915 (+1.43% 24h), ETH $2,473.66 (+2.36%), SOL $94.90 (+1.25%). BTC mcap $1.56T.

## [06:43 ET] POSITION UPDATE — BTC / /MBTU6 short — THESIS DEAD, CLOSE
- Open shorts: BTC spot SELL 08-16 @62,950 (tgt 57,000, stop 65,200), BTC SELL 08-17 @63,400 (stop 65,200), /MBTU6 SHORT 08-18 @64,100 and 08-19 @64,340 (both stop 66,600).
- BTC is now $77,915. **Every one of those stops was breached and the market is ~20% above the highest stop.** The bearish crypto thesis is not "under pressure", it is refuted.
- decision: CLOSE ALL BTC/ /MBT SHORT EXPOSURE AT MARKET. Do not average, do not re-short, do not roll the target down.
- why: a short whose stop is 15%+ away in the wrong direction is no longer the trade that was published. Continuing to carry it is how a bad week becomes a bad quarter. Prior reports re-pitched this short 4× across 08-16..08-19 — textbook anchoring, and it is the single largest error in the open book.
- source: https://www.coingecko.com/en/coins/bitcoin

## [06:46 ET] PRICES — all equity marks are Fri 2026-08-21 close (age ~3760 min, market closed, pre-session Monday)
Open positions: KRE 74.86 | XLE 63.64 | CCJ 102.51 (+7.2% Fri) | NKE 40.76 | PFE 28.07 | DHT 19.82 | HD 335.61 | LCII 101.98 (-3.3% Fri) | BCC 82.47 | TJX 140.53 | TLT 82.05
Awaiting-entry names, all now ABOVE the published entry (levels missed): DG 123.41 (entry 119) | LULU 121.07 (entry 115, +4.7% Fri) | DINO 97.32 (entry 93, +5.0% Fri) | EEM 67.12 (entry 65.6) | GLD 423.36 (entry 398, +1.95% Fri) | CEG 272.88 (entry 266) | SVRA 5.59 (entry 5.35)
Others: NVDA 214.72 (-1.0% Fri) | MRVL 237.04 (**-5.6% Fri**) | AVGO 368.45 | DELL 442.08 | FRO 43.67 | STNG 78.49 | TNK 91.02 | MPC 360.72
- **Friday 08-21 was a broad risk-on / debasement day**: gold +1.95%, CCJ +7.2%, DINO +5.0%, LULU +4.7%, BTC to ~78k, while the 10y ROSE to 4.69%. Long-end yields up + gold up + risk assets up together is a term-premium/debasement tape, not a growth tape. Needs a news check before I lean on it.

## [06:47 ET] EARNINGS CALENDAR — next 10 sessions (finnhub)
- Mon 08-24 bmo: PDD, XPEV, DKS, PVH
- Tue 08-25 amc: INTU, ZM, HEI; bmo WSM, JKS; ANF, FIVE, KSS
- **Wed 08-26 amc: NVDA (est EPS 2.13, rev $93.6B) — the week's index-level event**; also CRM, HPQ, SNPS, CRWD, VEEV, OKTA, NTNX, URBN, BBWI
- **Thu 08-27: DG bmo (rev $11.5B), BBY bmo, MRVL amc, ULTA amc, WDAY amc, ADSK amc, GAP amc, AFRM amc**
- Mon 08-31: SAIC, ASO, AEO, **FRO bmo** (tanker read-across to DHT)
- Tue 09-01: NIO, MDT, DLTR, M, PANW, MDB
- Wed 09-02: **AVGO amc**, HPE, GOLD, **LULU amc**, NTAP, SNOW
- Thu 09-03: **DELL**, CIEN, ZS, DOCU, CPB

## [06:53 ET] MACRO — THE WEEK'S TWO EVENTS, AND THEY POINT OPPOSITE WAYS
- **Jackson Hole is 2026-08-27 to 08-29. Kevin Warsh delivers his FIRST keynote as Fed Chair on Friday 2026-08-28 at 10:00 ET**, at Jackson Lake Lodge. Warsh took office 2026-05-22. Theme: financial innovation, payments and policy. Source: https://www.regardsofwallstreet.com/news/jackson-hole-2026-dates-schedule-warsh-first-speech and https://thefrontmonth.com/articles/2026-08-21-warsh-jackson-hole-keynote-aug-28/
- **Markets price roughly one-in-three odds of a September rate HIKE** (Sept FOMC is three weeks after the keynote). This is not a cutting cycle. Source: same.
- **NVDA reports Wed 2026-08-26 after the close** (est EPS 2.13 / rev $93.6B). Two market-wide events in one week: NVDA Wed PM, Warsh Fri AM.
- Friday 08-21 closes: SPX 7,674.37 (+0.43%), Nasdaq 26,180.45 (+0.43%), Dow 53,277.01 (+0.98%). Source: https://www.cnbc.com/2026/08/20/stock-market-today-live-updates.html
- **The 30-year Treasury yield hit its highest level since 2007 last week.** Global bond yields surged. Source: https://kfgo.com/2026/08/21/nvidia-earnings-jackson-hole-to-test-pillars-of-stock-rally/
- The regime, stated plainly: **long-end yields at 19-year highs while gold, silver and bitcoin melt up together.** That is a term-premium / fiscal-dominance / debasement tape, not a growth tape and not an easing tape. Rising long yields are normally poison for gold; the two rising together says the market is repricing the currency, not the discount rate.
- CAUTION: one aggregator article quoted gold at "$2,547". That is wrong and I am not using it — GLD closed 423.36, which implies spot gold near $4,600/oz, consistent with the "Gold Tops $4,600" headline. Never take a level from a secondary summary when the ETF print is available.

## [06:54 ET] LEVELS — precious/industrial metals are extended, not cheap (Fri 08-21 closes, prior-close marks)
- GLD 423.36 | SMA20 392.64 | SMA50 383.03 → **+7.8% above its 20-day**. 150d high 509.70.
- SLV 62.72 | SMA20 56.65 → +10.7% above the 20-day. -42.9% off the 150d high of 109.83 (silver had a crash and is rebuilding).
- NEM 131.58 | SMA20 109.32 → **+20.4% above its 20-day**, only 2.45% off the 150d high. ATR 3.83%.
- FCX 76.66 | SMA20 67.11 → +14.2% above the 20-day, 0.87% off the 150d high.
- AGI 37.86 (+18.3% vs SMA20), PAAS 53.07 (+11.3% vs SMA20).
- Conclusion: **the debasement trade is right and I am late to it.** Every one of these is 8-20% above its 20-day into a Fed-chair keynote that is the single most plausible hawkish shock available. Chasing metals here at 06:00 ET Monday is the crowded trade. The prior report's GLD entry at 398 was correct and never filled; I am not raising it to chase.

## [06:54 ET] NEWS — MRVL
- MRVL -5.6% Friday to 237.04 on **profit-taking plus Aug opex**, after a two-day surge on an expanded Google custom-AI-silicon partnership. Not a fundamental de-rate. Reports 2026-08-27 after the close.
- MRVL sits +12.7% above its 20-day (210.42) with a 7.4% ATR and a 150-day range of 70.69-329.88. This is a stock that has more than tripled off its low. Into an earnings print, at 7.4% daily ATR, no stop I can set is both meaningful and survivable.
- Source: https://www.tipranks.com/news/why-marvell-stock-is-down-today-and-what-wall-street-expects-next-august-21
## [06:54 ET] REJECTED — MRVL — 7.4% ATR into an 08-27 earnings print while +12.7% extended above the 20-day; no stop is both survivable and meaningful. Momentum, not edge.

## [06:58 ET] EVENT CONTRACTS — Kalshi Sept FOMC ladder (fetched live from api.elections.kalshi.com, 2026-08-24 ~10:56 UTC)
| Contract | Outcome | Last | Yes bid/ask | Open interest |
| --- | --- | --- | --- | --- |
| KXFEDDECISION-26SEP-H26 | Hike >25bp | 1c | 0/1 | 662,490 |
| **KXFEDDECISION-26SEP-H25** | **Hike 25bp** | **32c** | **31/32** | **1,743,656** |
| KXFEDDECISION-26SEP-H0 | Hold | 68c | 67/68 | 3,509,363 |
| KXFEDDECISION-26SEP-C25 | Cut 25bp | 2c | 1/2 | 3,187,210 |
| KXFEDDECISION-26SEP-C26 | Cut >25bp | 1c | 0/1 | 693,109 |
Resolution 2026-09-16 (FOMC decision day). Source: https://api.elections.kalshi.com/trade-api/v2/markets/KXFEDDECISION-26SEP-H25
- Oct ladder: H25 23c, H0 73c, C25 3c (OI far thinner — 13.9k vs 1.74M, do not trade the Oct contract).
- The ladder is internally coherent and deeply traded. **A cut is already priced at 2c — there is no edge on the downside bucket**, so the only tradeable disagreement is on H25 at 32c.
- Corroboration that 32c is the real market and not a stale print: FRED 2y at 4.19% against an effective fed funds rate of 3.63% — **the 2-year already carries a 56bp hiking premium.** A market expecting no policy change would put the 2y near 3.7%.
- Prior report published KXFEDDECISION-26SEP-H25 YES @32 on 2026-08-22 and it was never filled; the level is unchanged at 32c today, so re-pitching it is not a level chase.

## [06:59 ET] INSIDERS — finalists checked (finnhub, 6-month window)
- AVGO: 1 open-market buy, 1 distinct buyer, $374k (Harry L. You, 2026-06-11 @ 373.57) against 147 sells worth $630M. One director buying near today's price is a footnote, not a signal.
- CCJ: zero open-market buys, zero sells. No information either way.
- NEM: zero buys, 18 sells worth $10.8M. Not a signal on its own but no confirmation of the melt-up.
- Reminder to self: absence of insider buying is not a negative. None of the above changes a thesis; recorded so it is not re-checked.

## [06:59 ET] NEWS — CCJ, why it rose 7.2% on Friday
- Cameco's **49%-owned Westinghouse confidentially filed a draft Form S-1 with the SEC on 2026-07-31** for a proposed IPO. Investors are re-marking what the stake is worth.
- Also: uranium spot at decade highs; 2026 production guidance held despite disruptions; stronger realized pricing.
- This is a genuine, dated structural catalyst for a long-term holding rather than a momentum move.
- Sources: https://www.quiverquant.com/news/Cameco+Gains+as+Investors+Focus+on+Higher+Uranium+Pricing+and+Nuclear+Growth+Signals , https://www.tradingkey.com/news/market-movers/262125359-market-movers-ccj-20260821

## [06:59 ET] NEWS — AVGO, the de-rate is a real share-loss story
- AVGO 368.45, **-25.6% off its 150-day high of 495**, below both the 20-day (396.06) and 50-day (388.53). Fell ~6% on 08-19, its sharpest day in two months.
- The proximate cause is not vibes: **Marvell struck a major custom-AI-silicon deal with Broadcom's largest customer (Google).** That is share loss in the exact franchise carrying the AI growth story, not a valuation wobble.
- Guidance stands at ~$29.4B revenue next quarter with AI semis at $10.8B. Reports **2026-09-02 after the close**.
- Sources: https://www.tipranks.com/news/why-broadcom-avgo-stock-is-sinking-today-august-14-2026 , https://www.marketbeat.com/instant-alerts/broadcom-nasdaqavgo-trading-down-46-heres-what-happened-2026-08-19/

## [07:00 ET] SCAN — nuclear / power / energy complex (Fri 08-21 closes)
| Sym | Last | ATR% | SMA20 | SMA50 | 150d hi | 150d lo | % off hi | $vol/day |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AVGO | 368.45 | 4.07 | 396.06 | 388.50 | 495.00 | 289.96 | -25.6 | 7,830M |
| LEU | 186.26 | 6.02 | 182.07 | 173.08 | 345.60 | 142.13 | -46.1 | 107M |
| UEC | 12.76 | 4.75 | 10.76 | 10.60 | 20.34 | 8.91 | -37.3 | 84M |
| SMR | 9.40 | 6.85 | 9.10 | 9.30 | 21.15 | 7.21 | -55.6 | 281M |
| **VST** | **136.21** | 3.98 | 145.03 | 153.35 | 178.31 | **132.66** | **-23.6** | 702M |
| TLN | 314.46 | 5.62 | 338.60 | 367.23 | 449.84 | 301.45 | -30.1 | 308M |
| CEG | 272.88 | 3.71 | 270.24 | 263.12 | 333.80 | 228.63 | -18.3 | 744M |
| LNG | 277.51 | 2.68 | 264.47 | 255.30 | 300.89 | 202.21 | -7.8 | 415M |
| PSX | 242.87 | 3.11 | 220.39 | 199.22 | 246.95 | 136.79 | -1.7 | 611M |
| VLO | 348.86 | 3.19 | 321.86 | 293.10 | 352.70 | 176.50 | -1.1 | 818M |
- **The split inside "AI power" is the day's most interesting dislocation.** CEG is -18% off its high and above both moving averages; VST is -23.6% off its high, sitting on its 150-day low of 132.66, below its 20-day (145.03) AND its 50-day (153.35); TLN is -30% off and also at its 150-day low. The merchant IPPs have been sold while the contracted one has not.
- Cause per reporting: **sector rotation, not a company setback.** The July-August semiconductor selloff dragged everything AI-adjacent that is not a chip, on fears AI capex is overbuilding. VST specifically has delivered hyperscaler PPAs, a record EBITDA print and a datacenter JV involving NVIDIA, and the shares fell anyway — down 28% over twelve months. Source: https://www.quiverquant.com/news/Vistra+slides+as+AI-power+names+weaken+and+no+fresh+company+catalyst+emerges and https://financefeeds.com/vistra-vst-stock-prediction-bull-bear-case/
- VST insiders: 0 open-market buys, 8 sells worth $6.9M in six months. No confirmation from the inside. Noted, not weighted against.
- Refiners PSX (-1.7% off high) and VLO (-1.1%) are at 150-day highs and 10-19% above their 50-days. Confirms the energy tape but they are the chase, not the value. Not captured.

## [07:00 ET] REJECTED — PSX, VLO — at 150-day highs, 10-19% above the 50-day. The energy view is already expressed through XLE at 3%; adding refiners here would be a third correlated bet on the same driver at the worst entry.
## [07:00 ET] REJECTED — SMR — -55.6% off high, 6.85% ATR, below both moving averages, no dated catalyst found inside the horizon. Falling knife with no date on it.
## [07:00 ET] REJECTED — UEC — +18.6% above its 20-day into the same uranium tape CCJ already expresses. Correlation cap: CCJ is the better-capitalised way to own it and is already held.

## [07:00 ET] CATALYSTS — FDA PDUFA dates inside the horizon (MarketBeat FDA calendar)
- JAZZ Ziihera (HER2+ biliary tract cancer) — 2026-08-25. Last 254.28, only -4.1% off its 150-day high; the approval looks priced.
- GILD BIC/LEN (HIV) — 2026-08-27.
- **NUVL zidesamtinib (ALK+ NSCLC) — 2026-09-18.** No price history returned by the data source (FAIL) — cannot set levels, so cannot capture. Recorded as a gap.
- RARE UX111 (Sanfilippo A) — 2026-09-19. Last 25.83, -29.4% off high, ATR 5.84%, $56M/day.
- IONS zilganersen (Alexander disease) — 2026-09-22. Last 59.74, -31.1% off high, ATR 3.13%, $138M/day.
- Source: https://www.marketbeat.com/fda-calendar/upcoming/

## [07:05 ET] CATALYST — RARE / UX111, the best dated setup found today
- FDA accepted the **resubmitted** BLA for UX111 (rebisufligene etisparvovec), AAV9 gene therapy for Sanfilippo syndrome type A, **PDUFA action date 2026-09-19**. Would be the first approved therapy for the disease.
- The July 2025 CRL was **CMC-only** — chemistry, manufacturing and controls. The FDA did not dispute efficacy or safety. Resubmission answers the CMC observations and adds up to 8 years of follow-up (sustained CSF-HS reduction, continued functional improvement vs natural history).
- RARE 25.83 | mcap $2.54B (98.49M shares) | $56M/day | ATR 5.84% | 20-day 25.94, 50-day 28.33 | -29.4% off the 150-day high of 36.57.
- Captured at 2%, stop 21.50, target 36.50. The stop is explicitly acknowledged as ineffective against a CRL gap.
- Sources: https://ir.ultragenyx.com/news-releases/news-release-details/ultragenyx-announces-us-fda-acceptance-bla-resubmission-ux111 , https://www.cgtlive.com/view/fda-accepts-ultragenyx-new-bla-submission-mps-iiia-gene-therapy-ux111

## [07:06 ET] SMALL CAPS — screened, all rejected
| Sym | Last | mcap | $vol/day | ATR% | Note |
| --- | --- | --- | --- | --- | --- |
| SVRA | 5.59 | $1.15B | 9M | 4.82 | prior 5.35 entry unfilled; **no dated catalyst inside the horizon found today** |
| BBAI | 3.22 | — | 72M | 5.22 | backlog +14% q/q to $281.9M, $53M sole-source award — but no DATE |
| ONDS | 8.71 | — | 656M | 7.09 | FY26 revenue target raised to $390M+ — but no DATE |
| PDYN | 6.13 | — | 6M | 5.41 | Q1 rev +107% to $3.5M — revenue base too small, $6M/day is thin |
## [07:06 ET] REJECTED — BBAI, ONDS, PDYN — real defense-tech backlog growth but not one dated event in the next 10 sessions. Contract awards are unschedulable by construction, which makes these momentum bets, not catalyst trades. config/strategy.md: "dated events beat vibes."
## [07:06 ET] REJECTED — SVRA — the 5.35 level from 2026-08-23 is unfilled and unchanged (last 5.59), but I could not find a dated catalyst inside the horizon to justify re-pitching it, and it sits below its 50-day (5.67). Leaving it alone rather than repeating it for the fourth time.
## [07:06 ET] REJECTED — IONS — zilganersen PDUFA 2026-09-22 is a real date, but Alexander disease is an ultra-rare indication against a $9.9B market cap. The event cannot move the stock enough to matter. RARE at $2.5B is the same trade with 4x the operational leverage.
## [07:06 ET] REJECTED — JAZZ — Ziihera PDUFA 2026-08-25 is inside the horizon but the stock is only 4.1% off its 150-day high. The approval is priced.
## [07:06 ET] REJECTED — /MESU6 short into the 08-26 NVDA print and the 08-28 Warsh keynote. Two market-wide binaries in one week is a reason for smaller positions, not for a directional index punt. The hawkish risk is already expressed cleanly through KXFEDDECISION-26SEP-H25, where the payoff is defined and the thesis is one falsifiable claim.
## [07:06 ET] REJECTED — GLD long_term at the prior 398 level. Reward-to-risk fails the long-term floor: target 500 (near the 509.70 150-day high) against a 340 bear case from a 398 entry is 1.76 against a required 2.5. The regime call is right and the trade still does not clear the bar. Not raising the target to make it fit.
## [07:06 ET] REJECTED — long BTC. Bitcoin at 77,915 is +23.8% from where this report shorted it a week ago. Flipping from short to long at the top of that move would be the same anchoring error in the opposite direction. Cover the short (captured as /MBTU6) and take no new view.

## [07:07 ET] MACRO — this week's US data calendar
- **Core PCE price index for July, 08:30 ET, consensus +0.2% m/m.** Sources disagree on whether it lands Tue 08-25 or Wed 08-26 — both place it BEFORE Warsh speaks on Friday 08-28. I am not asserting a day I cannot verify.
- Same session: Conference Board consumer confidence (August), durable goods orders (July).
- Wed 08-26 08:30 ET: Q2 GDP second estimate, GDP deflator, Q2 PCE and core PCE second estimates.
- Thu 08-27 08:30 ET: weekly jobless and continuing claims.
- Explicit consensus framing from the previews: a hotter-than-expected core PCE lifts the probability of a September hike; a softer one tempers it.
- Sources: https://www.newsquawk.com/headlines/newsquawk-weekly-economic-calendar---24th-28th-august-2026 , https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar , https://www.ig.com/en-ch/news-and-trade-ideas/week-ahead--24-august-2026-260821
- **This materially strengthens the KXFEDDECISION-26SEP-H25 idea**: the contract now has two dated tests inside eight days rather than one — core PCE at +0.2% consensus, then Warsh at 10:00 ET Friday. Note that FRED's July CPI index rose only 0.074% m/m; if core PCE prints in line at 0.2% that is a 2.4% annualised pace, above a strict 2% target and supportive of the long side of the contract.
- Note this week's shape for the reader: **there is no 8:30 print today.** Monday is empty. That is why nothing intraday was captured — see the rejection below.

## [07:07 ET] REJECTED — all intraday ideas. There is no US economic release on Monday 2026-08-24 and no overnight index or futures level was obtainable (Yahoo returned HTTP 429 for /ES, /NQ, SPX, NDX, RUT, VIX and DXY). An intraday recommendation written at 06:40 ET without a session catalyst and without an overnight futures mark would be a guess dressed as a level. Nothing intraday cleared the bar today.
## [07:07 ET] REJECTED — ULTA — reports 08-27 after the close, -27.1% off its 150-day high, sitting exactly on its 20-day (523.21). A genuine de-rate, but my only thesis would be "cheap into a print", which is not an edge; zero insider buying, two sales. DG is the better-specified consumer catalyst and the correlation cap is better spent there.
## [07:07 ET] REJECTED — GILD — BIC/LEN PDUFA 08-27 is dated, but at 146.12 the stock is 7.1% off its 150-day high and 7.4% above its 20-day. Large-cap HIV label expansion into a stock at highs is priced.
## [07:07 ET] REJECTED — EEM — the 65.60 level from three prior publications is unfilled and price is now 67.12, above it. The thesis is a weak dollar, and **I could not fetch the dollar index today (Yahoo 429)**. I will not re-pitch a currency-driven idea for the fourth time on a currency I could not price.
## [07:07 ET] REJECTED — SLV — 42.9% below its 150-day high looks like value until you note it is also 10.7% ABOVE its 20-day. Silver crashed and is mid-rebound; buying the fourth week of a bounce into a Fed-chair keynote that is the most plausible hawkish shock available is not a setup. Same reasoning as GLD.
## [07:07 ET] REJECTED — LEU — uranium enrichment, -46.1% off its high, above both moving averages. A real idea, but CCJ and VST already occupy two slots on the nuclear/power driver and LEU has a 6.02% ATR with no dated catalyst. Correlation cap, not a quality judgement.

## [07:10 ET] VENUE CHECK — Robinhood availability verified for every non-equity idea
- **KXFEDDECISION-26SEP-H25**: Robinhood lists the event as "Fed rate decision in September 2026" (resolves 2026-09-16) under Prediction Markets > Economics, and shows **69% on the maintain-rate leg** — consistent with the 68/69c I fetched from Kalshi for H0 and the 32c hike price. Also listed: an October 2026 Fed decision event and a "number of rate cuts in 2026" market showing **88% for exactly zero cuts**. Verified, not remembered. Source: https://robinhood.com/us/en/prediction-markets/economics/events/fed-rate-decision-in-september-2026-sep-16-2026/
- **/MBTU6** micro bitcoin futures: on Robinhood Derivatives per the substitution table in config/universe.md. September 2026 contract, not in its final trading week. The instruction is to COVER — holders should cover whichever /MBT contract month they actually hold.
- All equity ideas (VST, AVGO, DG, RARE, BCC, DHT, NKE, PFE, CCJ, LCII, HD, TJX, KRE) and ETFs (XLE, TLT) are US exchange-listed common stock or listed ETFs. No OTC, no warrants, no foreign ordinaries, no options.

## [07:11 ET] FALSIFICATION PASS — I recomputed every reward-to-risk from my own captured levels, and it killed four adds
Ran the arithmetic across all captured candidates against the config/strategy.md floors (intraday 1.5 / swing 2.0 / long_term 2.5):
| Symbol | Horizon | Entry I had written | R:R | Floor | Outcome |
| --- | --- | --- | --- | --- | --- |
| XLE | swing | 63.64 | **1.11** | 2.0 | add WITHDRAWN — re-captured as a stop-raise with no buy level |
| CCJ | long_term | 94.00 | **1.86** | 2.5 | add WITHDRAWN — hold only |
| LCII | long_term | 96.00 | **2.33** | 2.5 | add WITHDRAWN — hold only |
| PFE | long_term | 26.30 | **2.44** | 2.5 | add WITHDRAWN — hold only (misses by 0.06 and a near-miss is still a miss) |
| KRE | swing | 74.86 | 11.58 | 2.0 | passed only because the stop is 0.66 ATR away — a mirage. Re-captured with no entry level. |
| HD | swing | 335.61 | 3.99 | 2.0 | same mirage from a 0.84 ATR stop. Re-captured with no entry level. |
- **In no case did I move a target to make an idea pass.** Where the arithmetic failed, the add was withdrawn and the position downgraded to hold. That is the floor doing the job config/strategy.md assigns it: "The floor exists to reject ideas, not to calibrate targets."
- Two stated reward-to-risk figures were also wrong on recomputation and are corrected: PFE 2.40 -> 2.44 (still fails), NKE 2.93 -> 3.00 (passes).
- **After correction, every candidate with a published entry clears its floor**: DHT 3.88, NKE 3.00, DG 2.88, RARE 2.75, VST 2.71, BCC 2.40, KXFEDDECISION 2.33, AVGO 2.29.

## [07:11 ET] CORRELATION CHECK — 17 unique symbols, driver-by-driver (cap is 3 per driver)
- **Rates / Fed (1 with new capital)**: KXFEDDECISION-26SEP-H25 only. TLT and KRE are exits/holds with no new money, so they do not consume slots.
- **US rates & housing (3 — AT THE CAP)**: HD (hold), BCC (hold, stop raised), LCII (hold). No further housing exposure may be added; flagged in each entry.
- **Energy / shipping (2)**: XLE (hold), DHT (hold). PSX, VLO and DINO rejected partly to stay inside this.
- **Nuclear / power (2)**: CCJ (hold), VST (new). LEU and UEC rejected on the cap.
- **AI semis (1)**: AVGO (wait for 09-02).
- **Consumer / retail (2)**: DG (new, wait for 08-27), NKE (accumulate). TJX is a close.
- **Pharma / biotech (2)**: PFE (hold), RARE (new).
- **Crypto (0)**: /MBTU6 is a cover instruction; no crypto exposure remains after it.
- Verdict: no driver exceeds three, and only 8 of 17 entries deploy new capital. **The report is deliberately defensive this week** — two market-wide binaries (NVDA 08-26 PM, Warsh 08-28 AM) is a reason to manage the existing book rather than to add to it.

## [07:12 ET] SCAN — large-cap de-rated names for the long-term lane (Fri 08-21 closes)
| Sym | Last | ATR% | SMA20 | SMA50 | 150d hi | 150d lo | % off hi | % off lo | $vol |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LULU | 121.07 | 3.43 | 121.17 | 117.63 | 205.07 | 104.44 | -41.0 | +15.9 | 316M |
| NEE | 83.65 | 1.73 | 86.29 | 87.15 | 98.75 | 82.14 | -15.3 | **+1.8** | 969M |
| UPS | 102.01 | 2.20 | 104.92 | 108.40 | 122.41 | 93.86 | -16.7 | +8.7 | 577M |
| CVS | 93.02 | 3.22 | 98.90 | 102.01 | 110.68 | 69.51 | -16.0 | +33.8 | 805M |
| EL | 101.94 | 3.62 | 87.70 | 84.97 | 121.64 | 66.22 | -16.2 | +53.9 | 300M |
| TGT | 165.44 | 2.94 | 150.79 | 140.93 | 165.48 | 100.88 | -0.0 | +64.0 | 680M |
| MRNA | 145.13 | **11.1** | 72.57 | 67.60 | 176.66 | 36.66 | -17.9 | **+295.9** | 3,312M |
## [07:12 ET] REJECTED — NEE — the single most tempting chart on the board: 1.8% above its 150-day low, -15.3% off its high, 1.73% ATR, $969M/day. **I am rejecting it on internal consistency.** NextEra is a bond proxy, and the de-rate is the long-end yield surge. My highest-conviction new idea today is a bet that the Fed HIKES in September. Buying a rate-sensitive regulated utility at its low while simultaneously paying 32c for a hike is taking both sides of the same trade and calling it diversification. If the hike thesis resolves against me, NEE is where I look next — with a level, not today.
## [07:12 ET] REJECTED — LULU — reports 09-02 after the close, -41.0% off its 150-day high, and the prior 115.00 entry is unfilled (price rose 4.65% on Friday to 121.07, back above the 20-day). A real setup. Rejected on correlation: NKE is already a continuing athletic-apparel accumulation, and LULU plus NKE plus DG would be three consumer positions of which two are the *same* bet on athletic apparel. That is one idea with extra steps.
## [07:12 ET] REJECTED — UPS, CVS — both genuinely de-rated (-16.7% and -16.0% off their highs, both below both moving averages) and both plausible long-term candidates. Rejected for a reason I want on the record rather than dressed up: **I did not have time to read the filings.** config/strategy.md requires a defended valuation anchor and a priced bear case for a long_term idea, and I have neither. A half-researched long-term thesis is worse than none, because it reads with the same authority.
## [07:12 ET] REJECTED — TGT — at its 150-day high (165.44 against 165.48) and 17.4% above its 50-day. Whatever the story is, it is priced.
## [07:12 ET] REJECTED — EL — 16.2% off its high but 53.9% above its low and 16.2% above its 20-day. Mid-recovery, not a de-rate.

## [07:15 ET] NEWS — the week's biggest single-stock event, and why none of it is tradeable now
- **MRNA more than doubled on 2026-08-19**, adding roughly $30B of market value, on Phase 3 INTerpath-001 data: intismeran autogene (mRNA-4157/V940), an individualised mRNA cancer vaccine developed with Merck, met its primary endpoint in resected melanoma with significant improvements in recurrence-free AND distant-metastasis-free survival over Keytruda monotherapy.
- MRNA 145.13 against a 20-day of 72.57 — the stock is **+296% off its 150-day low** with an **11.1% ATR**. No stop is survivable. Not captured.
- **MRK is the 50% partner and the more interesting question**: Keytruda loses exclusivity in 2028 and is over half of Merck's pharmaceutical revenue, so this data speaks directly to the cliff. Morgan Stanley upgraded to overweight on 08-20 and raised its target to $179 from $116; RBC downgraded on the same data.
- Sources: https://www.biospace.com/business/mercks-moderna-partnered-vaccine-success-clears-view-of-post-keytruda-future , https://www.cnbc.com/2026/08/20/merck-is-finding-more-ways-to-boost-its-shares-morgan-stanley-says.html , https://finance.yahoo.com/healthcare/articles/merck-cancer-vaccine-trial-results-141558795.html

## [07:15 ET] REJECTED — MRK — on the arithmetic, not the story. MRK gapped from 135.17 (08-18) to 152.20 (08-19) and closed Friday at 152.55, **1.26% off its 150-day high** and 13.7% above its 20-day, up 45% year to date. Against Morgan Stanley's $179 target and a $120 bear case (below the pre-data 135), entry at 152.55 scores **0.81** and even a patient 137 entry on a gap-fill scores 2.47 — still short of the 2.5 long-term floor. Zero insider buying, 17 sales worth $30M. The thesis is good and the price is not. **This is the name to revisit on any pullback toward 134-137.**
## [07:15 ET] REJECTED — the sequencing read-across (ILMN, NTRA, TXG). Personalised cancer vaccines need tumour sequencing, so the second-derivative trade was the right instinct — and the market got there first. All three closed Friday within 0.55% of their 150-day highs: ILMN 219.40 (+15% since 08-18, high 220.43), NTRA 332.03 (high 333.56), TXG 65.12 (high 65.47). There is no edge left in an idea that has already moved 15% in three sessions.
## [07:15 ET] REJECTED — PACB — 1.35, 50.6% off its high, 7.51% ATR, only $9M/day of dollar volume and no dated catalyst. Below the practical liquidity bar for a position that has to be exitable.

## [07:17 ET] RESEARCH COMPLETE
- **candidates: 25 lines / 17 unique symbols** (synthesis takes the last entry per symbol; XLE, CCJ, PFE, LCII, KRE, HD, NKE and KXFEDDECISION were each re-captured after the falsification pass and only the later line should be used).
- **8 deploy new capital**: KXFEDDECISION-26SEP-H25 (yes @32c), VST (long_term), RARE (swing, PDUFA 09-19), DG (swing, wait for the 08-27 print), AVGO (swing, wait for the 09-02 print), NKE (long_term accumulate), DHT (swing, level unchanged at 19.40), BCC (swing, stop raised).
- **9 are position management**: /MBTU6 COVER the bitcoin shorts, TLT CLOSE, TJX CLOSE (stop already breached), XLE hold + stop raised to 60.60, CCJ / PFE / LCII hold with adds withdrawn, KRE and HD hold-to-stop.
- **The single most important line in this report is the bitcoin one.** Four short recommendations at 62,950-64,340 with stops at 65,200 and 66,600 are all still open against a spot price of 77,915 — roughly 17% beyond the highest stop, on a leveraged product. That is a risk-control failure, not a drawdown, and it should be closed before anything else is done.
- **Coverage gaps**
  - No live index, futures, VIX, dollar-index, gold or WTI level all session — Yahoo Finance returned HTTP 429 for every one of ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX, /ES, /NQ, DXY, gold and WTI. Finnhub covers single-name equities and ETFs only. Friday's index closes came from a news source, not from a price feed, and are cited as such.
  - No intraday ideas — there is no US economic release on Monday 08-24 and no overnight futures mark was obtainable. Stated plainly rather than filled with a guess.
  - NUVL (zidesamtinib PDUFA 09-18) returned no price history from any source, so levels could not be set on an otherwise qualifying catalyst.
  - UPS and CVS are plausible long-term de-rates whose filings I did not have time to read; no valuation anchor, so not captured.
  - Kalshi's non-Fed macro series (CPI, GDP, unemployment) were scanned but only far-dated annual contracts were listed; no near-dated liquid alternative to the Fed ladder was found.
  - The core PCE release day is unresolved — previews disagree between Tue 08-25 and Wed 08-26. Both are before Warsh on 08-28, which is what the trade depends on.
- **Sources that failed**: Yahoo Finance (429 on all index/futures/FX/commodity symbols), `market_data.py events` (returned 0 markets for "Fed", "rate", "interest rates", "recession", "CPI" — I bypassed it and queried api.elections.kalshi.com directly, which worked), `market_data.py history` for NUVL and EXAS, FRED rates block returned null (the FRED series were fetched individually and did work).
- **Timestamp correction**: the `[HH:MM ET]` headings in this file drifted up to ~4 minutes ahead of the real clock (they were written from estimate, not from `date`). Actual research window was **06:38 to 07:11 ET, about 33 minutes** (verified with `date`, not estimated). Every price, level and contract quote in this file came from a fetched source and is unaffected; only the heading times are approximate.
