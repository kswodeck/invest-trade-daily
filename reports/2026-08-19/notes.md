# Research log — 2026-08-19

## [06:33 ET] MACRO — regime, prev close 2026-08-18
Source: scripts/market_data.py macro + quote (stooq/FRED/coingecko), all prev-close (market closed, pre session).
- Rates: US10Y 4.72% (prev 4.68), US2Y 4.19% (prev 4.17), fed funds eff 3.63%, 10y-2y +0.52. Long end backing up — bear steepening. TLT proxy (bonds_20y) 81.66 +0.38%.
- Equities prev close: SPY 767.45 -0.68%, QQQ 717.51 -1.69%, IWM 300.23 -1.26%. **Tech-led risk-off; QQQ underperformed SPY by 100bp.**
- XLE 63.68 **+1.76%** — energy the only green sector, 3rd straight day of relative strength.
- GLD 398.55 -1.71% (sharp reversal), CCJ 96.03 -2.59%, BCC 80.18 -2.15%.
- Crypto: BTC $64,340 +0.37% 24h, ETH $1,916.6 +1.15%, SOL $77.20 +1.92%. BTC still sub-65k, chopping.
- FAILED SOURCES: ^GSPC/^NDX/^DJI/^RUT/VIX/DXY/gold-futures/WTI all failed (Yahoo 429 rate-limited + finnhub index subscription). No live VIX or DXY today — noted for data_quality_notes.

## [06:33 ET] OPEN POSITIONS — 19 live, marks vs entry (prev close 08-18)
- XLE 63.68 vs 60.5/60.8 entries = **+4.7% to +5.3%**, above 3 of 3 targets? no — target 64.5/66.5/67.0. First target 64.5 is 1.3% away.
- LCII 103.27 vs 94.0 entry = **+9.9%** in 1 day. Target 138.
- CCJ 96.03 vs 88.0/95.0 = +9.1%/+1.1%. NKE 40.06 vs 38.0/40.0 = +5.4%/+0.2%.
- KRE 76.85 vs 76.8 = +0.1% (flat, 4 days). TJX 150.85 vs 151.5 = -0.4%. HD 337.49 vs 340 = -0.7%.
- DHT 19.31 vs 18.8 = +2.7%. PFE 27.25 vs 25.8 = +5.6%. BCC 80.18 vs 81.0 = -1.0%.
- BTC short: spot 64,340 vs 62,950/63,400 entries = **losing 1.5-2.2%**; /MBTU6 short entered 64,100, stop 66,600 — still live but the trade is not working.
- REPETITION WARNING: XLE 4x, KRE 4x, TJX 3x in last 10 days. Do not re-pitch without a concrete change.

## [06:32 ET] CALENDAR — earnings next 8 sessions (finnhub)
- **TODAY 08-19 bmo: LOW ($26.5B est rev), TGT ($26.3B), TJX ($15.3B), ADI, EL, ROST (amc)**
- 08-20 bmo: **WMT ($188.8B)**, **BABA ($274B)**, DE ($11.1B), NTES, SPR, AAP
- 08-21 bmo: BJ, UI
- 08-24 bmo: PDD, XPEV, DKS, PVH
- 08-25 amc: INTU, ZM, HEI; bmo WSM, JKS, KSS, ANF, FIVE
- **08-26 amc: NVDA ($93.6B est rev)**, CRM, HPQ, CRWD, SNPS
- 08-27: DG, BBY, MRVL, WDAY, ULTA, ADSK, AFRM, GOLD(Barrick)
- Read: retail earnings week is the whole catalyst calendar. Consumer is the tradeable theme, not semis (NVDA is 5 sessions out).

## [06:32 ET] ** TJX IS AN OPEN POSITION REPORTING TODAY bmo ** — must decide before the open.

## [06:33 ET] MACRO — the regime, named
Sources: https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-18-2026 ; https://finance.yahoo.com/markets/live/stock-market-today-monday-august-17-dow-sp-500-nasdaq-094421171.html
- **30-year Treasury yield at its highest level in nearly two decades.** Driver named as persistent inflation risk + heavy government borrowing + debt issuance tied to the AI capex boom. This is a supply/term-premium story, not a growth story.
- Nasdaq Composite -1.3% on 08-18; **the semiconductor gauge fell 5.5%** in one session.
- Oil at a 2-week high on US-Iran tensions (Trump signalling more economic pressure on Iran) — this is what XLE has been trading on.
- Headline references "Fed hike bets" following a jobs report. Fed funds eff still 3.63%; 2Y at 4.19% is ~56bp ABOVE the funds rate = market pricing tightening, not cuts.
- Coherent read: term premium + inflation risk repricing. Long-duration equity de-rates, energy and hard assets bid, banks get a steeper curve.

## [06:34 ET] POSITION UPDATE — TJX — opened 2026-08-17 @151.50, mark 150.85 (-0.4%), **reports today bmo**
- levels: last 150.85, ATR14 3.09 (2.05%), sma20 156.59, sma50 157.35, 120d range 146.14-170.00, -11.3% off high. 8 sessions of selling into the print.
- consensus: $1.19 EPS / $15.17B rev vs $1.10 / $14.40B LY. Trailing 4-qtr avg surprise +8.8%. Call 11:00 ET.
- insiders: 0 open-market buys, 9 sells / $32.5M over 6 months. No support from that signal.
- decision: **HOLD through the print, do not add before it.** Withdraw the 146.50 stop — it is unenforceable across an earnings gap and would just guarantee selling the bottom tick. Reset to 141.00 after the gap settles.
- captured via add_candidate.py as an update (conviction 3, 2%).

## [06:35 ET] CATALYST — Strait of Hormuz is effectively closed. This is the dominant macro fact.
Sources: https://easternherald.com/2026/08/18/oil-prices-today-august-18-2026/ ; https://www.lloydslist.com/LL1157100/Hormuz-crisis-slashes-VLCC-volumes-by-36-but-voyages-are-longer ; https://www.seatrade-maritime.com/tankers/vlcc-rates-near-470-000-a-day-for-fixtures-through-hormuz ; https://www.eia.gov/outlooks/steo/
- **~3 ships/day transiting Hormuz vs ~130/day pre-war.** Brent $90.97, WTI >$84, third straight up session.
- The June US-Iran MOU **expired Monday 2026-08-17**; Trump ruled out extending it and threatened Oman, the mediator. Escalation, not de-escalation — and the expiry is 2 days old, so this is live news, not history.
- **VLCC Mideast-to-China day rates hit ~$498,000 last Friday**; benchmark peaked $423,736/day in March. Normal is $30-50K/day — this is roughly a 10x.
- VLCC cargo volume 16.1m bpd (Mar 15-Aug 9) is **down 27% YoY** — tonnes down, miles up. The ton-mile trade works through longer Atlantic-basin voyages to Asia, not through volume.
- **EIA STEO: ~0.6m bpd of disruption expected to persist through end-2027.** Multi-year, not a one-week headline.

## [06:35 ET] LEVELS — tanker complex (prev close 08-18)
| sym | last | atr% | sma20 | sma50 | 150d hi | off hi |
| FRO | 43.50 | 3.32 | 39.54 | 38.48 | 43.89 | -0.9% |
| INSW | 98.77 | 3.73 | 93.40 | 87.92 | 99.68 | -0.9% |
| TNK | 89.10 | 3.71 | 79.07 | 74.71 | 90.32 | -1.4% |
| DHT | 19.31 | 3.63 | 18.57 | 18.07 | 20.55 | -6.0% |
| STNG| 79.34 | 3.51 | 77.59 | 77.02 | 87.39 | -9.2% |
| ASC | 18.01 | 3.80 | 16.91 | 16.38 | 20.03 | -10.1% |
- Crude tankers (FRO/INSW/TNK) are all pinned within 1.5% of range highs. Product tankers (STNG/ASC) lag by 9-10%. DHT is the crude laggard.
- **FRO reports 2026-08-31 bmo, est EPS $2.57 on $750M rev — a dated catalyst inside the horizon.**

## [06:35 ET] LEVELS — precious metals, post-blowoff
- GLD 398.55, ATR 1.75%, sma20 386.14, sma50 381.23, 150d range 363.32-509.70, **-21.8% off high**. Above both averages; basing after a parabolic top.
- SLV 57.44, **-47.7% off its 109.83 high**. Silver blew off far harder than gold and has retraced roughly half. sma20 55.36 ~= sma50 55.51 (flat, no trend).
- GDX 88.95 (-24.1% off high), sma20 82.17 / sma50 79.02 — trading **+12.6% above its 50d**. Miners are leading gold, not lagging it.

## [06:36 ET] REJECTED — memory/AI semis (MU, SNDK, WDC) — not a dip, a broken parabola
- SNDK 1625.78 after 1271->1786 in four sessions (+40%) then -9%; ATR 9.95%. MU ATR 7.48%, 868->1011->940. WDC ATR 9.29%.
- The 08-18 "chip selloff" (SOX -5.4%, >$680B of value) came off a vertical melt-up, not a base. Nothing here has a level worth defining and stops at 1 ATR are coin flips. Pass.

## [06:37 ET] CLOCK CORRECTION
Timestamps above were estimated, not read; corrected against `date`. Real elapsed at this point is 7 minutes, not ~28. All subsequent timestamps are read from the clock. Budget runs to ~07:30 ET.

## [06:37 ET] INSIDERS — tankers
- FRO: 0 open-market buys, 0 sells, 6mo. No signal either way (Bermuda-domiciled, Fredriksen holds via Hemen — not captured in Form 4 flow).
- DHT: 0 buys, 1 sell / $0.56M. Nothing.
- Absence is not a negative per the brief; recording it so nothing is implied.

## [06:39 ET] REJECTED — TGT — priced for perfection into today's print, no edge either way
Source: https://www.benzinga.com/trading-ideas/previews/26/08/61280292/target-q2-preview-retailer-could-be-taking-market-share-from-walmart-will-stock-gains-continue ; https://www.tipranks.com/news/target-tgt-stock-could-swing-more-than-7-on-q2-earnings-options-market-signals
- TGT 152.48, only -2.6% off its 150d high of 156.47, **+50% YTD**, sma20 147.12 / sma50 138.85 (+9.8% above the 50d).
- Consensus $26.15B rev / $2.31 EPS. Options imply a **7.08%** move. Sell-side average price target implies ~**5% downside**; ratings 12 buy / 15 hold / 2 sell.
- Long into a +50% YTD name where the average target is below spot is a bad risk; short into a company whose Q2 store visits ran **+4.7% YoY vs WMT +0.7%** is worse. No position.

## [06:39 ET] LEAD — the consumer divergence is TGT winning traffic from WMT
- WMT 115.20 is **-14.8% off its 135.16 high** and below its 50d (114.35 vs sma20 112.48) — it has quietly de-rated all year while TGT rallied 50%.
- WMT reports **tomorrow 08-20 bmo**, est rev $188.8B. If the traffic-share loss shows in comps, a consensus mega-cap long is exposed.
- Holding this as a watch item rather than a trade: WMT ATR is only 2.03%, a short needs margin, and it is the defensive name in a risk-off tape. Flagging, not capturing.

## [06:41 ET] DATA GAP — event contracts unusable today
- `market_data.py events` was queried for: inflation, Fed, rate, Iran, oil, gas, S&P, Bitcoin, GDP, shutdown, Powell.
- Every query returned either 0 markets or multi-leg sports parlay shards (`KXMVECROSSCATEGORY-...`) with **null yes_bid/yes_ask/last_price/volume**. Not one priced macro or econ market came back.
- The brief requires an event-contract thesis to state the market's implied probability against my own. With no price I cannot do that, so **no event contracts are captured today**. This is a source failure, not an absence of opportunity — flag it in data_quality_notes.

## [06:46 ET] POSITION UPDATE sweep — all 19 open positions reviewed
Marks are prev close 08-18. **Important caveat: several 08-18 "entries" sit BELOW where the stock traded all week and were almost certainly never filled** — prior_context scores them mechanically as gains anyway. Flag for synthesis:
- LCII entry 94.00 while the stock traded 103-107 all week (never below 103 in 5 sessions) — unfilled.
- CCJ entry 88.00 while the stock traded 96-99 — unfilled.
- NKE entry 38.00 while the stock traded 39-41 — unfilled.
These are accumulation limits, not open positions, and the "+9.9% / +9.1% / +5.4%" in prior_context is an artefact.

### Captured as updates
- **BCC — CLOSE EARLY.** 80.18, five straight down days (84.25->80.18), back below the 20d at 81.46, -12.8% off high. Housing complex confirming the break (LEN -31.6% off high and near range low; ITB and XHB both below 20d and 50d). The 30y at a two-decade high is a direct hit to the only demand driver BCC has. Exit rather than wait for the 76.00 stop. Captured as `sell`.
- **XLE — HOLD, raise stops to 61.00, raise target to 68.50.** 63.68, -0.05% off the 150d high, +11.4% above the 50d at 57.17. Three entries (60.50/60.80/60.80) all now profitable; 61.00 locks a gain on each. MOU expiry removed the de-escalation path the old 64.50-67.00 targets assumed.

### Held with no change — deliberately NOT re-captured, to avoid re-pitching
- **KRE 76.85** — flat four sessions, ATR only 1.32%, -1.9% off high, above 20d (76.60) and 50d (75.09). Curve steepened to +52bp, which is the thesis working slowly. Nothing changed, and KRE has been recommended 4x in 10 days. Hold as-is; no recommendation emitted.
- **CCJ 96.03** — below the 50d (96.28), -29% off high, -2.6% on the day. Long-term uranium thesis, no stop by design. Nothing new. Hold.
- **NKE 40.06** — -41.5% off high, below 20d/50d, 1.2 ATR above the 150d low of 38.86. Long-term turnaround, accumulation unfinished. Hold.
- **PFE 27.25** — working, +5.6% vs the 25.80 entry, above 20d (25.81) and 50d (25.22). Hold.
- **HD 337.49** — -15.1% off high, below both 20d (341.22) and 50d (338.79), -0.7% vs the 340.00 entry. Same rate problem as BCC but repair/remodel is less starts-sensitive than wood products. Hold with the 328.00 stop, which is 1.1 ATR away and adequate. Watch: if HD closes below 328 the housing read-through has generalised.
- **TJX** — handled above, reports today.
- **DHT** — see below, thesis strengthened.

## [06:43 ET] LONG-TERM — silver, and the arithmetic that made it a "wait" not a "buy"
Sources: https://www.canadianminingreport.com/blog/silver-price-drops-from-121-peak-to-59-should-long-term-investors-consider-buying-the-dip-in-2026 ; https://www.financemagnates.com/trending/why-silver-is-crashing-how-low-can-xagusd-go-and-silver-price-prediction-2026/ ; https://www.devere-group.com/whats-next-for-silver-in-2026-mid-year-outlook/
- Silver peaked **$121/oz January 2026**, fell to $85 intraday on Jan 30 (-39% in a session), lost ~27% in March alone, now ~$63. **>50% off the all-time high.**
- Crash drivers: profit-taking off a parabola, stronger USD, high real rates, easing tariff fears, industrial demand hit by higher energy costs. **Note none of these are supply-side.**
- Supply story intact: multi-year structural deficits, solar PV + EV + electronics demand, constrained mine supply. JPMorgan and others model **$70-90/oz average for the rest of 2026**.
- SLV 57.44, sma20 55.36 ~= sma50 55.51 (flat = basing, not falling), -47.7% off the 109.83 high.
- **Arithmetic check, done honestly:** at spot 57.44 with a defensible bear case of 44 (silver ~$48) and a 76 target (silver ~$83), R:R = (76-57.44)/(57.44-44) = **1.38 — fails the 2.5 long-term floor.** Nudging the target to 88 to make it pass would be exactly the reverse-engineering the strategy forbids.
- Therefore captured as **accumulate below 54.00 only**: at 52 entry, (76-52)/(52-44) = **3.0**, clears the floor honestly. Action is explicitly `wait: true`.

## [06:43 ET] REJECTED — life insurers (MET/PRU/LNC/EQH/CRBG) — the rising-yield trade is already paid for
- Every one is in an uptrend above its 20d and 50d and within 2.5-5.4% of its 150d high: MET 96.73 (-4.2%), PRU 124.54 (-2.5%), EQH 50.84 (-4.7%), CRBG 33.12 (-4.9%), LNC 45.08 (-5.4%).
- The reinvestment-yield thesis is consensus and in the price. No entry with an acceptable downside. Pass.

## [06:43 ET] REJECTED — P&C insurers (PGR/TRV/ALL/AFL) — cheaper, but for a reason
- PGR 207.23 is -13.4% off high and below BOTH its 20d (211.66) and 50d (213.95) — the only genuinely de-rated name in the group.
- But the de-rate tracks the auto-pricing cycle turning after two years of exceptional margin, which is a real earnings headwind, not a fixable temporary problem. That fails the "quality business de-rated on a fixable problem" test. Pass.

## [06:43 ET] REJECTED — homebuilders (LEN/DHI/PHM/TOL) as longs — falling knife, driver still worsening
- LEN 84.94 is -31.6% off high and 6% above its 150d low; DHI -14.7%, PHM -12.8%, TOL -15.2%; ITB and XHB both under their 20d and 50d.
- Cheap, but the 30y is at a two-decade high and still rising — the input is moving against them. As shorts they need margin and are already heavily discounted. No position; used instead as confirming evidence for the BCC exit.

## [06:48 ET] REJECTED — ZIM merger arb — real opportunity, but it fails the R:R floor and I will not bend the floor
Sources: https://investors.zim.com/news/news-details/2026/ZIM-to-be-Acquired-by-Hapag-Lloyd-for-35-00-per-Share-in-Cash-at-Aggregate-Cash-Consideration-of-Approximately-4-2-Billion-New-Israeli-Company-New-ZIM-to-Acquire-Portion-of-ZIMs-Business/default.aspx ; https://247wallst.com/investing/2026/03/21/why-zim-shares-trade-7-below-hapag-lloyds-offer-price/
- Hapag-Lloyd to acquire ZIM at **$35.00/share cash**, ~$4.2B equity value, signed 2026-02-17. Expected close **late 2026**.
- ZIM last 28.49 => gross spread **$6.51 = 22.8%** to a close roughly 4 months out (~70% annualised). ZIM reports Q2 today bmo but has **cancelled the earnings call because of the pending deal** — so today's print is not the driver; the deal is.
- Why so wide: needs ZIM shareholder approval, EU clearance, AND **State of Israel sign-off under the Special State "Golden Share"**, which is where the reported concern sits. The spread has been stuck near $7 since March — this is a persistent, well-known risk premium, not a fresh mispricing I found.
- **Arithmetic:** reward to $35.00 = 6.51. Break case: unaffected price was $15.50 (2025-08-08); a realistic break lands ~19-20. Risk = ~9.5. **R:R = 0.69, versus a 2.0 swing floor.**
- Merger arb is structurally high-probability/low-payoff and will always fail an R:R floor. The floor is there to reject ideas, so I am rejecting it rather than re-drawing the downside to make it pass. Worth surfacing to the reader as a rejected-but-interesting item.

## [06:48 ET] WATCHLIST not candidate — UI (Ubiquiti) — de-rated hard, but I could not verify the fundamentals
- Price is real (fetched): UI 583.13, **-47.0% off its 1099.99 150d high**, yet holding ABOVE a rising 20d (556.74) and 50d (553.27). $52.6M/day dollar volume. Reports 2026-08-21 per the finnhub calendar.
- **I could not get trustworthy consensus numbers.** Web results for "UI August 21 2026 earnings" returned what appear to be prior-year figures (a "$3.54 vs $2.23 beat" reported as already released, and a "$488.79 one-year high" that contradicts the fetched 1099.99). Reporting an earnings result for a date two sessions in the future is a tell that the source is stale.
- Not capturing on unverifiable numbers. Watchlist only, with the reason stated.

## [06:48 ET] REJECTED — solar (CSIQ -37.5%, JKS -46.9%) — cheap, but no dated catalyst I can underwrite and 6.07%/4.43% ATR
- CSIQ 14.74 below both 20d (15.02) and 50d (15.30); JKS 16.41 below its 50d (16.63). Both still making lower highs. Reports 08-27 / 08-25 but I have no differentiated view on either print. Pass.

## [06:47 ET] LONG-TERM — the AI-power de-rate is the best mispricing I found today
Sources: https://www.gartner.com/en/newsroom/press-releases/2026-06-10-gartner-says-data-center-electricity-demand-to-grow-26-percent-in-2026 ; https://www.bloomberg.com/news/articles/2026-08-11/texas-power-demand-forecast-trimmed-after-data-center-pause ; https://www.ropesgray.com/en/insights/viewpoints/102mvfl/data-center-investment-in-2026-ai-demand-power-constraints-and-private-equity ; https://www.quiverquant.com/news/Vistra+slides+as+AI-power+names+weaken+and+no+fresh+company+catalyst+emerges

**The prices (fetched, prev close 08-18):**
| sym | last | off 150d high | vs sma20 | vs sma50 | ATR% |
| CEG | 266.83 | -23.1% | below (270.48) | **above** (261.61) | 4.13 |
| VST | 140.52 | -23.0% | below (149.09) | below (153.63) | 4.49 |
| TLN | 317.66 | -29.4% | below (346.74) | below (369.36) | 6.04 |
| NRG | 115.56 | -39.2% | below (126.86) | below (132.39) | 6.59 |
| GEV | 1004.53 | -16.0% | below (1005.81) | below (1031.27) | 4.82 |
| BE  | 209.01 | -40.5% | below (212.38) | below (244.97) | 12.04 |

**What actually broke — regional, and priced as if national:**
- Texas imposed a **pause on new data-centre projects**; forecast ERCOT load growth cut from 14% to **5.6%**.
- NRG missed: EPS $1.49 vs $1.73 prior, because **Houston power cleared $33/MWh against a $52 plan.**
- Coverage describes the move as "sector-wide selling rather than company-specific issues," with investors questioning how fast the infrastructure spend converts to profit.

**What did NOT break — the demand curve:**
- Gartner: data-centre electricity consumption **+26% in 2026**; global data-centre power demand **104GW -> 132GW (+27%)**.
- AMZN/GOOGL/META/MSFT combined 2026 capex guidance **$635-670B**. MSFT alone tracking $120B+ in FY26.
- **~40% of announced AI data-centre projects are delayed by power infrastructure, not chip supply.** 30-50% of 2026-planned capacity slips to 2028+.
- US capacity under construction -5.7% from end-2024, first contraction since 2020 — because of permitting/power procurement, i.e. supply constraint, not demand loss.
- Hyperscaler nuclear PPAs (MSFT/Three Mile Island, plus GOOGL/AMZN) are the specific mechanism.

**Why CEG and not the cheaper ones:** contracted nuclear baseload is the asset the PPAs are actually written against; CEG is PJM-weighted rather than ERCOT-exposed, so the thing that broke the sector is not its problem; and it is the only name in the group holding above its 50-day. VST/NRG are cheaper precisely because they carry the Texas exposure that caused the de-rate.

**Arithmetic, done before choosing the entry:** at spot 266.83 with a 205 bear case (well below the 228.63 150d low, reflecting a genuine AI-capex disappointment against contracted cash flows) and a 355 target, R:R = (355-266.83)/(266.83-205) = **1.43 — fails the 2.5 floor.** Solving (355-E)/(E-205) >= 2.5 gives **E <= 247.9**. Hence entry 245, zone 232-248, `wait: true`. R:R at 245 = 110/40 = **2.75**.
- Nat-gas E&Ps are the tell that this is not a demand story: EQT 53.14, AR 37.04, RRC 39.86 are ALL above their 20d and 50d and only -17% to -22% off highs. The fuel is holding while the generators broke — that is a valuation/regional-pricing de-rate, not a demand collapse.

## [06:47 ET] REJECTED — VST, NRG, TLN, BE — same theme, wrong vehicle
- VST/NRG carry the exact ERCOT and Texas-pause exposure that caused the de-rate; buying them is betting against the specific thing that went wrong.
- TLN 6.04% ATR and BE **12.04% ATR** with BE -40.5% off high — position sizing that respects those ATRs makes the ideas too small to matter, and BE is not a contracted-cash-flow business. Pass.

## [06:51 ET] POSITION UPDATE — LCII — CANCEL the unfilled 94.00 limit (consistency with the BCC exit)
Sources: https://seekingalpha.com/news/4626936-lci-industries-forecasts-2026-adjusted-eps-of-8_25-8_75-while-cutting-rv-shipment-outlook-to ; https://www.stocktitan.net/sec-filings/LCII/8-k-lci-industries-reports-material-event-bab7c27a10a4.html
- LCII **cut its own 2026 NA RV wholesale shipment forecast to 280-300K from 315-330K** (~10% cut), naming higher interest rates, affordability, inflation, and input costs (aluminium +80% YoY, steel +20%).
- Q2 2026: net sales -4% to $1.1B, **OEM net sales -10%, towable RV wholesale units -20%.** Margins DID expand on cost cuts; 2026 guide $3.9-4.1B revenue, adj EPS $8.25-8.75 (~12x at 103.27).
- The 94.00 limit was never filled — LCII has not printed below 103 in five sessions. This is an order cancellation, not an exit.
- **Consistency test:** BCC and LCII are both rate-driven big-ticket cyclicals. I closed BCC on the 30y move; keeping a resting bid in LCII would be incoherent. Same driver, same treatment.

## [06:52 ET] WATCHLIST not candidate — POWL — record backlog, three straight EPS misses, no dated catalyst
Sources: https://www.investing.com/news/company-news/powell-q3-2026-slides-24b-backlog-offsets-earnings-miss-93CH-4841804 ; https://simplywall.st/stocks/us/capital-goods/nasdaq-powl/powell-industries/news/powell-industries-powl-stock-price-cools-as-backlog-swells-p
- The bull case is real: **backlog $2.375B, the highest in the company's 79-year history**; Q3 orders **$934M, nearly triple** the year-earlier level, including a single **>$400M data-centre order**; data centres are ~15% of backlog.
- The bear case is also real: **Q1, Q2 AND Q3 fiscal 2026 all came in below consensus.** Three consecutive misses is a pattern, not noise.
- Price confirms the bears for now: 203.55, **-37.9% off the 328.00 high**, below the 20d (213.08) and far below the 50d (245.32), ATR 6.82%.
- **No dated catalyst** — next report is fiscal Q4 around November. Buying a downtrend with no event and three misses behind it is not a setup. Watchlist. **Becomes actionable on one quarter where EPS actually meets** and the backlog starts converting; that is the falsifiable trigger.

## [06:52 ET] REJECTED — PRIM — record backlog, but the misses are margin blowups
- 79.80, **-61.2% off its 205.50 high**; fell 36% in a single premarket on the Q1 miss and guidance cut; an analyst called it "tough to defend."
- Record $13.9B backlog ($8.2B MSA), plus a $399.5M data-centre construction acquisition — but the shortfall came from **cost overruns and delays on renewables projects compressing margins.** Fixed-price contractor margin risk is the whole business model risk, not a temporary problem. Pass.

## [06:52 ET] STRUCTURAL NOTE — the electrical complex has split, and the split is informative
- At/near highs, above both averages: **ATKR 93.44 (-0.7% off high), IESC 738.79 (-9.5%), ETN 431.33 (-9.8%), AZZ 146.43 (-9.7%)** — conduit, contracting, components.
- Crushed, below both averages: **POWL -37.9%, MYRG -35.7%, PRIM -61.2%, VRT -28.3%**, alongside the generators CEG/VST/NRG/TLN at -23% to -39%.
- Read: the market is paying for firms that *deliver* the buildout on time and punishing anyone whose margins slipped while doing it. That is an execution-quality dispersion, not a demand verdict — which supports the CEG thesis (contracted cash flow, no fixed-price execution risk) over the switchgear and contractor names.

## [06:53 ET] SELF-AUDIT — recomputed every reward-to-risk before finalising; two failed and were fixed
Ran the arithmetic myself rather than trusting what I wrote:
- **TJX failed at 1.23** (entry 150.85, target 163.00, stop 141.00). The 141.00 stop was a number I invented ("after the gap settles"), not a level. Replaced with **145.50, just under the 146.14 150-day low** — a real level, and tighter rather than looser. Target 163.00 is unchanged and is the 162.06 early-August pivot where the slide began. Now **2.27**.
- **XLE failed at 1.80** (entry 63.68, target 68.50, stop 61.00). The failure was the honest signal: at 0.05% off the range high there is no acceptable new entry. Restructured to `wait: true` — existing lots hold with stops raised to 61.00, new money waits for **61.50** with a **59.20** stop below the 20-day at 59.65. Target unchanged at 68.50. Now **3.04**.
- **I did not move a single target to fix either one.** Both were fixed by putting the stop on a real level or by refusing the entry.
- Final spread: TJX 2.27, FRO 2.45, XLE 3.04, DHT 3.11, /MBTU6 3.25. No clustering just above the 2.0 floor, which is the pattern the repo warns about.
- Long-term pair carry no stop by design; R:R against a stated bear price: **SLV 3.0** (52 entry, 76 target, 44 bear), **CEG 2.75** (245 entry, 355 target, 205 bear). Both bear prices are named in the candidate text, not just here.

## [06:55 ET] FALSIFICATION — the case AGAINST my own Hormuz book, and it is stronger than I assumed
Sources: https://www.axios.com/2026/08/05/us-iran-strait-of-hormuz-deal-nears ; https://www.cnn.com/2026/08/08/world/live-news/iran-war-trump ; https://www.cnn.com/2026/08/04/world/live-news/iran-war-trump ; https://www.aljazeera.com/news/2026/8/16/us-iran-mou-is-set-to-expire-what-to-know
I built XLE, FRO and DHT on "escalation." Searching for the opposite found a second, live track I had missed:
- **2026-08-05, Axios: "US nears Iran deal to reopen Strait of Hormuz."** 08-04 CNN: US signals optimism on a deal.
- **Iran's FM Araghchi says the two sides are "very close"** to a deal on *managing the waterway*; **Oman's Foreign Ministry calls the talks "positive and constructive."**
- Iran is negotiating a **separate agreement with Oman on new shipping routes through Hormuz**, distinct from the political track.
- The catch, and why the trade is not simply dead: reopening is "subject to other conditions" — Iran demands **US concessions** and amends for the alleged June MOU violation first, and analysts say a Hormuz deal may be achievable while a lasting peace deal stays far off.
- **Net read: this is two tracks, not one.** The political track deteriorated (MOU expired 08-16, Trump ruled out extension and threatened Oman). The shipping track is reportedly near agreement. I framed only the first and treated the second as a vague tail risk. It is not a tail — it is an active negotiation both parties describe as close.
- **Action: cut conviction on every Hormuz-dependent idea and put the specific evidence in the counter-argument rather than a generic "a deal could happen."** XLE 4->3, DHT 4->3, FRO 3->2 with size cut 2%->1%. Levels unchanged — the falsification changes how much I bet, not where the levels are.
- This does NOT change the BCC exit or the CEG thesis, which rest on the 30-year yield and data-centre load respectively, neither of which is Hormuz-dependent.

## [06:56 ET] POSITION UPDATE — HD — hold, but flag the LOW read-through as an unpriced event today
- **LOW reports bmo TODAY** (consensus revenue $26.5B, per the finnhub calendar). That is a direct same-morning read-through to HD which the 08-18 entry thesis never accounted for.
- HD 337.49, -15.1% off its 397.63 high, below the 20d (341.22) AND the 50d (338.79). Five-session grind: 343.43, 341.70, 338.86, 337.88, 337.49. ATR 8.43; the 328.00 stop is 1.13 ATR below spot.
- Decision: **HOLD, stop unchanged at 328.00, do not add before LOW prints.** Captured so the flag travels with the position rather than sitting only in notes. R:R from here 3.0.
- Stated plainly in the candidate: holding HD while exiting BCC and cancelling LCII is defensible only because repair/remodel is stickier than housing starts. If HD breaks 328 that distinction has failed and the exit is automatic.

## [06:56 ET] CORRELATION AUDIT — against the 3-per-driver cap
- **Hormuz / oil supply: XLE, FRO, DHT = 3. AT the cap.** No further energy or shipping ideas captured today for this reason — ASC and STNG (product-tanker laggards, -10% and -9% off highs) were live candidates and were dropped purely on concentration, not on merit.
- **Long-end yields / rate-sensitive demand: BCC (exit), LCII (cancel), HD (hold-with-warning) = 3. AT the cap.** /MBTU6 short is partly the same risk-appetite driver — noted, but its mechanism is crypto-specific (failed 66,500 resistance, Korean retail rotation) rather than rates alone.
- Uncorrelated with both: **CEG** (data-centre load), **SLV** (metals/debasement), **TJX** (off-price consumer).
- Direction balance: 6 bullish (TJX, XLE, DHT, FRO, SLV, CEG, HD = 7 including HD), 3 bearish/exit (BCC, LCII, /MBTU6). Three of the bullish are `wait: true` — XLE, FRO, SLV, CEG — so the report is less long than the raw count suggests.

## [06:56 ET] VENUE CHECK — verified at runtime rather than recalled
Source: https://www.tradealgo.com/trading-guides/futures/futures-trading-on-robinhood ; https://robinhood.com/us/en/support/articles/before-trading-a-futures-contract/ ; https://www.firstcard.app/learn/robinhood-futures-trading
(The canonical RH futures-list support article now 404s — noted as a source failure; used secondary coverage plus RH's own "before trading a futures contract" page.)
- **Micro Bitcoin /MBT (0.1 BTC) IS offered** — confirms the /MBTU6 short is executable. RH lists BTC (5 coin), MBT (0.1), BFF (1/50th), plus SOL and XRP crypto futures.
- Equity index micros, crude, gold confirmed within "40+ CME Group products."
- **Robinhood does NOT offer interest rate or Treasury futures.** This is the single most consequential constraint on today's report: my strongest macro read is the term-premium blowout at the long end, and there is **no direct way to trade it in this account** — no /ZB, no micro 10Y yield. It has to be expressed second-hand through rate-sensitive equities, which is exactly what the BCC exit, the LCII cancellation and the HD warning are.
- Also unavailable: options on futures, agricultural futures. Options are out of scope by choice anyway.

## [06:58 ET] CORRECTION — I had the CEG differentiator backwards. Found it by checking my own claim.
Sources: https://investors.constellationenergy.com/news-releases/news-release-details/constellation-completes-calpine-transaction-powering-americas ; https://www.lspower.com/news/constellation-announces-agreement-to-sell-pjm-generation-assets-to-ls-power-as-part-of-ferc-u-s-doj-resolution-of-calpine-transaction/
- My first CEG capture claimed it was "PJM-weighted rather than ERCOT-exposed, so the thing that broke the sector is not its problem." **That is false.**
- **Constellation closed the $16.4B Calpine acquisition on 2026-01-07** (50M new shares + $4.5B cash). Calpine is 78 facilities / ~27,000 MW, predominantly natural gas, **historically with significant Texas ERCOT exposure**. Combined fleet 55GW; the deal adds ~$2B annual FCF.
- **And CEG is selling PJM generation assets to LS Power** as the largest tranche of DOJ-required divestitures. So the direction of travel is *more* ERCOT, *less* PJM — the exact opposite of what I wrote.
- Consequence: the Texas pause IS CEG's problem. The specific reason I preferred it over VST and NRG is gone. What survives is the nuclear fleet being the contracted, irreplaceable asset hyperscalers write PPAs against, plus $2B of incremental FCF.
- **Action: conviction 4 -> 3, size 4% -> 3%, and the error written into `key_risk` rather than quietly deleted.** Levels unchanged — the error changes how much I bet, not where the levels sit. Note Calpine also brings Texas data-centre contracts (e.g. a 190MW hyperscale deal), so the ERCOT exposure cuts both ways.
- Lesson worth recording: the thesis was built on sector price action plus demand data and I asserted the company-specific detail from memory. The check took two minutes and changed the recommendation.

## [06:57 ET] DURABLE-MISPRICING SWEEP — quality names de-rated (prev close 08-18, all fetched)
| sym | last | off 150d high | vs sma20 | vs sma50 | note |
| LULU | 119.01 | -44.7% | below (120.27) | **above** (117.66) | biggest de-rate in the sweep, basing on the 50d |
| NKE | 40.06 | -41.5% | below | below | already an open long-term position |
| EL | 84.27 | -30.7% | below (85.04) | ~at (84.18) | **reports today bmo**, coiled exactly on both averages |
| MRNA | 62.96 | -26.5% | above (58.38) | above (61.37) | 5.97% ATR, binary pipeline risk |
| DG | 120.84 | -23.6% | below (123.47) | **above** (119.46) | **reports 08-27** — the trade-down peer to TJX |
| ADI | 376.63 | -15.5% | ~at | below (390.30) | reports today bmo, semi exposure |
| UNH | 393.93 | -14.7% | below | below | still in a downtrend |
| CVS | 94.91 | -14.3% | below (101.02) | below (102.25) | falling, no base |
| ELV | 398.27 | -8.7% | above | above | recovering already |
| SBUX | 106.01 | -4.1% | above | above | no longer de-rated |

## [06:57 ET] WATCHLIST — DG, deliberately NOT captured today, and the reason is information sequencing
- DG 120.84, -23.6% off its 158.23 high, holding **above** a rising 50d (119.46). **Reports 2026-08-27**, six sessions out — a real dated catalyst.
- It is the same trade-down thesis as TJX: a consumer squeezed by sticky inflation moves to off-price and to dollar stores.
- **Reason to wait rather than capture:** TJX, TGT and LOW all print within the next three hours, and WMT tomorrow. Those four prints are a direct test of whether trade-down traffic is actually showing up in comps. Capturing DG this morning would be taking the same bet twice *before* the evidence arrives.
- Concrete trigger for tomorrow's run: **if TJX comps confirm trade-down traffic today, DG into its 08-27 print is the follow-on**, entry near the 119.46 50-day. If TJX shows the consumer weakening without the trade-down offset, DG is dead and so is the TJX add.

## [06:58 ET] UNVERIFIED ASSERTION — flagged rather than left implicit
- In the DHT counter-argument I asserted its fleet is older and its charter mix less spot-levered than Frontline's. **I did not verify that from a filing.** It sits in the counter-argument, so if it is wrong it only made me more cautious, not less — but it should not be read as a sourced fact.
- Every price, ATR, moving average and range figure in this log was fetched via `market_data.py`. No price in this file was estimated.

## [06:58 ET] RESEARCH COMPLETE
- **candidates: 10 unique** (16 lines in candidates.jsonl; TJX, XLE, FRO, DHT and CEG were each re-captured after the self-audit and falsification passes — synthesis should take the LAST entry per symbol).

**The report in one line:** the tape is being driven by a term-premium blowout at the long end (30y at a two-decade high on inflation risk, government borrowing and AI-capex debt issuance) plus a Hormuz closure that is being actively negotiated away — so the honest posture is holding energy rather than adding to it, cutting rate-sensitive cyclicals, and doing the real buying in the AI-power de-rate.

**Composition:** 5 new/adjusted longs (TJX, XLE, DHT, FRO, HD), 2 long-term accumulations both marked `wait: true` (SLV, CEG), 2 exits (BCC close, LCII limit cancellation), 1 short (/MBTU6). Total deployed size if every level fills: **18%**. Four of ten are `wait: true`.
- **Horizon skew, stated rather than fixed:** 8 swing, 2 long_term, **0 intraday**. Three large retail prints land this morning (TJX, TGT, LOW) so intraday catalysts existed — I had no differentiated view on any of them and did not manufacture one. TGT was explicitly rejected as priced-for-perfection.
- Conviction: one 2 (FRO, sized 1% as a lottery ticket), eight 3s, one 4 (BCC exit). **No 5s — nothing today deserved one.**

**Two passes that changed the output, both worth reading in full above:**
1. **Self-audit (06:53):** recomputed every R:R myself. TJX failed at 1.23 and XLE at 1.80. Both were fixed by moving stops to real levels or by refusing the entry outright — **no target was moved.** Final spread 2.27 / 2.45 / 3.00 / 3.04 / 3.11 / 3.25, no clustering above the floor.
2. **Falsification (06:55) and correction (06:58):** searching for the case against my own book found (a) an active Oman-mediated Hormuz reopening track that Iran's FM calls "very close," which cut XLE 4->3, DHT 4->3, FRO 3->2 and FRO's size 2%->1%; and (b) that my stated reason for preferring CEG was **factually backwards** — post-Calpine it has more ERCOT exposure and is divesting PJM assets — which cut CEG 4->3 and 4%->3%.

**Coverage gaps — what I could not check:**
- **Event contracts: total source failure.** Eleven queries (inflation, Fed, rate, Iran, oil, gas, S&P, Bitcoin, GDP, shutdown, Powell) returned either zero markets or unpriced sports parlay shards. No implied probability was obtainable, so none were captured. This is a gap, not an absence of opportunity.
- **No live VIX, DXY, SPX/NDX/DJI/RUT, gold or WTI futures quotes** — Yahoo returned HTTP 429 throughout and finnhub requires an index subscription. Index context came from stooq ETF proxies and news; the macro read leans on FRED rates, which did resolve.
- **No small caps captured.** The lane was hunted (POWL, PRIM, MYRG, AZZ, IESC, ATKR, ASC, STNG, ZIM, JKS, CSIQ, GMS, SPR, AMWD) but everything either failed liquidity/data fetch, was a falling knife with no dated catalyst, or was correlated into the already-full Hormuz bucket. Recorded as a genuine gap rather than filled with a weak name.
- **Two ideas dropped on the correlation cap, not on merit:** ASC and STNG, the product-tanker laggards at -10% and -9% off highs, with Hormuz already 3-deep.
- **ZIM merger arb rejected on arithmetic** ($35 cash bid vs 28.49, but R:R 0.69 against the 2.0 floor) and **UI rejected on unverifiable consensus** — both are real opportunities a reader may want despite my rules.
- Robinhood's canonical futures-list support article now **404s**; venue verification used RH's "before trading a futures contract" page plus secondary coverage.

**Sources that failed:** Yahoo Finance chart API (429, all indices), finnhub index quotes (subscription), stooq for ^GSPC/^NDX/^DJI/^RUT, Kalshi events endpoint (returned unpriced sports shards for every macro query), robinhood.com futures-contracts support article (404), market_data.py history for GMS/SPR/AMWD/NVEE.
