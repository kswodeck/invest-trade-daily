# Research log — 2026-08-21

## [06:36 ET] MACRO — rates, dollar, crypto
- FRED: US10Y **4.65%** (2026-08-19), US2Y **4.19%**, fed funds effective **3.63%**, 10y-2y curve **+0.50** (2026-08-20). Curve steepening with long end selling off — 10y is ~102bp above fed funds. Source: https://fred.stlouisfed.org/series/DGS10
- Unemployment 4.1% (Jul 2026). CPI index 332.813 (Jul 2026).
- TLT (20y+ Treasury ETF) last **82.34**, -0.82% on 2026-08-20 close. Long duration still making lows. Source: market_data.py quote
- **CRYPTO IS THE STORY**: BTC **$77,894, +8.34% / 24h**; ETH **$2,399, +5.11%**; SOL **$91.23, +4.44%**. BTC 24h volume $67.0B (elevated). Source: CoinGecko via market_data.py crypto
- DATA GAP: SPX/NDX/DJI/RUT/VIX/DXY/gold/WTI/ES/NQ all returned ok:false — Yahoo 429 rate-limited, Finnhub requires index subscription, stooq 404. Index level context unavailable this run; will use ETF proxies (SPY/QQQ/IWM) instead.

## [06:38 ET] TAPE — 2026-08-20 closes (equities closed; these are prior-close, not stale)
- SPY 762.60 (-0.84%), QQQ 710.93 (-0.72%), IWM 297.67 (-1.34%), GLD 415.26 (+0.34%)
- Broad equity risk-off with small caps worst, gold bid, and crypto up 8% — a divergence that says the crypto move is crypto-specific, not a general risk-on.
- Open-position marks: TJX 140.69 (**through the 145.50 stop — trade is dead, -6.7% vs 150.85 entry**), HD 334.49 (stop 328, -0.9% away), KRE 74.71 (**at the 74.20 stop**), BCC 81.77, DHT 19.80, XLE 63.75, CCJ 95.59, NKE 40.21, PFE 27.79, LCII 105.44

## [06:40 ET] MACRO — the regime: yields up, consumer cracking, crypto decoupling
- 2026-08-20 close: S&P 500 **-0.87% to 7,641.16**; Nasdaq Composite **-1.0% to 26,067.17**; Dow **-1.32%, -703.84 to 52,759.21**. Source: https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-20-2026
- Driver 1 — **rising long yields**: 10y pushed to **4.70%** despite the Treasury's extraordinary long-bond buyback operation. The buyback failed to hold the long end down, which is the bearish read: supply/term-premium is winning over the buyback bid. Source: https://finance.yahoo.com/markets/stocks/articles/stock-market-today-aug-20-214858123.html
- Driver 2 — **consumer cracking**: Walmart **-9%** on 2.6% same-store sales and soft FY guidance; management explicitly blamed **$4 gasoline** for a psychological hit to spending. Source: same
- This is one coherent trade, not two: **$4 gas is simultaneously the bull case for energy and the bear case for discretionary retail.** XLE closed green (+0.27%) on a -0.87% tape.
- Driver 3 — **crypto has decoupled**: BTC ran ~$64k → $77.9k in three sessions on (a) Treasury buyback liquidity, (b) SEC token-fundraising exemption proposals + White House push for the Clarity Act market-structure bill, (c) **>$1B of shorts liquidated in one hour** through $69k, (d) $517M spot-BTC-ETF inflow on 08-19, best since May. Sources: https://www.ig.com/uk/trading-strategies/bitcoin-69000-rally-treasury-buyback-260820 , https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-thursday-august-20-2026-crypto-prices-surge-after-president-trump-pushes-for-clarity-act-154014757.html

## [06:44 ET] POSITION UPDATE — /MBTU6 SHORT — opened 08-18 @ 64,100 and 08-19 @ 64,340 — **CLOSE NOW, AT MARKET**
- decision: **exit both contracts immediately. Do not average down. Do not re-short.**
- BTC spot is **$77,894**. Both shorts blew through the 66,600 stop days ago and are roughly **-21% against entry on the underlying** — on a leveraged futures contract that is the whole risk budget and then some.
- why the thesis broke, concretely: the short was a bet on continuation below $63k. What actually arrived was three independent bullish catalysts at once — Treasury long-bond buybacks easing liquidity, SEC token-fundraising exemptions plus a White House push on the Clarity Act, and $517M of spot-ETF inflows — into a market where 1.2M BTC had accumulated at a ~$63k cost basis. That accumulation base was the fuel: **>$1B of shorts were liquidated in a single hour** through $69k. This position was on the wrong side of that liquidation cascade.
- **the real lesson, and it is a process failure not a market one**: this short was re-pitched on two consecutive days (08-18, 08-19) at progressively worse prices while the stop was never respected. The repetition guard in prior_context flagged `/MBTU6 — 2×` and `BTC — 2×` and the run pitched it anyway. A stop that is written but not honoured is not a risk control.
- action: exit instruction only — deliberately NOT captured via add_candidate.py, because a `short` candidate on /MBTU6 is exactly what must not be published again today. Recorded here as an exit.
- Sources: https://www.ig.com/uk/trading-strategies/bitcoin-69000-rally-treasury-buyback-260820 , CoinGecko via market_data.py

## [06:45 ET] POSITION UPDATE — TJX BUY — opened 08-19 @ 150.85 — **STOPPED OUT, CLOSE**
- last **140.69** (-6.7%), through the 145.50 stop. This is the second TJX stop-out in three sessions (the 08-17 entry also stopped 08-19).
- why: the thesis was trade-down-to-off-price as the consumer weakens. The consumer did weaken — Walmart's 2.6% comps and the "$4 gas" commentary confirm it — but off-price got sold with the rest of discretionary rather than bid as a defensive. The mechanism was right and the trade still lost, which usually means the factor (discretionary beta) dominates the idiosyncratic story.
- **TJX has now been recommended 4× in 10 days and stopped out twice. Bar for a third pitch: not today.** Logging as a rejection below.
- decision: close, do not re-enter.

## [06:45 ET] REJECTED — TJX — 4× repeat, 2 stop-outs in 3 sessions, no new information since; anchored not convinced
## [06:45 ET] REJECTED — KRE — 4× repeat, stopped out twice on 08-19; a rising 10y at 4.70% steepens the curve which is the bull case, but regional banks kept falling through it. Thesis is not being confirmed by price and I have no new catalyst.

## [06:47 ET] CALENDAR — dated catalysts inside 10 sessions (source: Finnhub via market_data.py earnings)
- **Aug 24 bmo**: PDD ($117.5B rev est), XPEV; DKS, PVH
- **Aug 25**: INTU (amc), KSS, ANF, FIVE, WSM, ZM
- **Aug 26 amc**: **NVDA ($93.6B rev est)** — the index-level event of the window; also CRM ($11.4B), HPQ, CRWD, SNPS, BURL, URBN
- **Aug 27 bmo**: **DG (Dollar General, $11.5B)**, BBY ($9.6B); amc: MRVL, ULTA, ADSK, WDAY, AFRM, GAP
- **Sep 1**: DLTR, M (Macy's), MDT, PANW
- **Sep 2 amc**: AVGO ($29.9B), LULU, SNOW, HPE
- **Read**: this is a consumer-tape fortnight bracketed by one semi print. Nearly every dated event in the window is a retailer, which means the $4-gas/weak-comps question gets answered repeatedly and quickly. That argues for expressing the consumer view where trade-down *helps* rather than where it hurts.

## [06:37 ET] DATA GAP — event contracts unusable this run
- `market_data.py events` returned count 0 for: inflation, interest rates, Bitcoin, S&P 500, unemployment, CPI, recession, government shutdown. The one hit for "Fed" was a mis-indexed soccer parlay (`KXMVECROSSCATEGORY-...`, Arsenal/Man Utd/Real Madrid legs) with null bid/ask and null volume — i.e. the Kalshi search index is returning garbage, not that the markets do not exist.
- Consequence: **no event-contract candidates today, and that is a source failure rather than a judgement that none were attractive.** Robinhood Prediction Markets is a wanted lane per config/universe.md; it is simply unreachable this run. Recording so synthesis reports it in data_quality_notes rather than implying the lane was checked and found empty.
- I will not guess an implied probability from memory to fill the lane — an event-contract thesis requires the market's actual quoted cents, and I do not have them.

## [06:39 ET] MACRO — the long end is broken, and that is the regime trade
- Treasury Sec. Bessent more than **doubled the buyback cap from $2B to at least $4B**, effective **Sept 9 through Nov 4**. Announced 08-19; yields fell on the announcement. Source: https://www.cnbc.com/2026/08/19/treasury-announces-upscaled-buyback-operation-for-longer-term-debt-sending-yields-lower.html
- **The relief lasted one session.** On 08-20 the 10y rose 4.7bp to **4.70%** and the **30y rose 5.5bp to 5.249%** — anyway. Source: https://finance.yahoo.com/economy/policy/articles/bonds-bounce-us-buybacks-relief-040238251.html
- Strategists attribute the June-onward long-end selloff to three things that a buyback cannot fix: a **deficit set to exceed its 2025 level**, **persistently above-target inflation**, and **heavy corporate issuance competing with Treasurys**. Source: https://www.cnbc.com/2026/08/20/treasury-bond-buybacks-long-term-yields.html
- Bessent is also publicly leaning on Warsh's Fed to ease. Source: https://www.cnbc.com/2026/08/19/bessent-treasury-buybacks-yields-warsh-fed.html
- **This is the single most important fact of the day.** When the sovereign issuer's own bid cannot hold its long end, and the Treasury is simultaneously pressuring the central bank to cut, that is a fiscal-dominance signature. It explains what otherwise looks like three unrelated tapes: gold at highs, bitcoin +22% in three sessions, and equities de-rating on the discount rate. They are one trade.

## [06:39 ET] REJECTED — TLT long @ 82.6 (carried over as "awaiting entry" from 08-20)
- Do not re-pitch. The 08-20 idea was to buy duration into the buyback. The buyback has now happened, was doubled in size, and the 30y still made a fresh two-decade high the very next session. That is the cleanest possible falsification of a long-duration thesis: the most bullish catalyst available arrived and the bond fell anyway.
- Buying TLT here requires believing the deficit, inflation and issuance picture all turn — none of which has a date on it.

## [06:40 ET] LEVELS — precious metals: I had this backwards, correcting from fetched data
- **GLD 415.26**, ATR14 1.80%, SMA20 390.07 / SMA50 382.05 / **SMA200 413.21**, range 361.39-509.70, **-18.53% off the 52w high**.
  Gold did *not* go straight up. It corrected 18.5% and is only now reclaiming its 200-day from below, with the 20- and 50-day well underneath. That is an early-recovery structure, not an extended one.
- **GDX 99.85**, ATR 3.79%, SMA20 84.45 / SMA50 79.84 / SMA200 88.39, -14.79% off high, adv20 $2.03B. Miners have reclaimed the 200-day but sit **+25% above the 50-day** — the right thesis at a short-term extended price. Chasing this specific candle is not the trade.
- **SLV 61.66**, ATR 2.98%, SMA200 64.46 — **still below its 200-day**, **-43.86% off the 109.83 high**. Silver is the laggard of the complex by a wide margin.
- Why silver broke: it ran to an all-time high near **$121.67 in January**, then fell **~30% in a single session on Jan 30** when **CME raised futures margin** and forced liquidation of a spec long near five-year highs (CFTC net long >60,000 COMEX contracts). That was a positioning and plumbing event, not a demand event. Source: https://www.financemagnates.com/trending/why-silver-is-crashing-how-low-can-xagusd-go-and-silver-price-prediction-2026/
- **But the bear case on silver is structural and I am not going to wave it away**: the Silver Institute has a 6th consecutive deficit at 46.3Moz, while **solar silver demand is set to fall ~30% this year, a ~60Moz year-over-year reduction** on thrifting and outright substitution. The demand loss is *larger than the deficit*. Gold:silver ratio is back near 70 from below 50 in January. Sources: https://silverinstitute.org/global-silver-investment-to-remain-strong-in-2026-against-the-backdrop-of-a-sixth-consecutive-annual-market-deficit/ , https://investingnews.com/daily/resource-investing/precious-metals-investing/silver-investing/silver-forecast/
- **Conclusion: gold over silver.** Same debasement driver, but gold's demand base is monetary and improving while silver's largest industrial leg is actively shrinking. Silver is the higher-beta expression of a thesis whose fundamentals are weaker. Rejecting silver.

## [06:40 ET] REJECTED — SLV / PAAS / SIL — solar substitution is removing ~60Moz of demand vs a 46.3Moz deficit; the "silver deficit" bull case is being falsified by its own demand data. Gold expresses the same macro with an intact fundamental.

## [06:40 ET] LEVELS — other reference points
- NVDA 216.85, ATR 2.90%, SMA20 212.78 / SMA50 207.29 / SMA200 195.25, -8.32% off the 236.54 high, adv20 $24.8B. Above every moving average into the Aug 26 print.
- SPY 762.60, ATR 0.84%, -2.15% off high, SMA200 707.14. IWM 297.67, ATR 1.14%, -2.46% off high. Neither index is broken — this is a de-rating on rates, not a growth scare.

## [06:41 ET] VENUE CHECK — Robinhood Derivatives, what is actually listed
- Available: equity index (**/ES, /MES, /NQ, /MNQ**), **metals including micro gold /MGC**, energy (crude, natural gas), FX (euro, yen, sterling), and crypto micro futures (BTC, SOL, XRP). 40+ CME products, 23/5 with some 24/7.
- **NOT available: interest-rate / Treasury futures (/ZB, /ZN, /ZT).** Also no options on futures and no agricultural contracts. Sources: https://www.tradealgo.com/trading-guides/futures/futures-trading-on-robinhood , https://www.firstcard.app/learn/robinhood-futures-trading
- **Consequence, and it is a real constraint on today's best idea**: the cleanest expression of "the long end is broken" would be a short /ZB. It cannot be traded in this account. The fiscal-dominance view therefore has to be routed through its second-order beneficiary — gold — rather than shorted directly in rates. Saying so explicitly because the substitution changes the risk: gold can fall even if I am right about the deficit.
- On gold specifically I am choosing **GLD (spot ETF) over /MGCZ6 (micro gold futures)** despite universe.md's futures preference, for the reason universe.md itself carves out: the horizon is long_term and multi-year roll costs make a futures expression of a buy-and-hold thesis worse, not better. Second reason: `market_data.py macro` could not return a gold price this run, so I have a live GLD print and would be **guessing** a /MGCZ6 contract price. I will not set futures levels off a number I did not fetch.

## [06:43 ET] MACRO — the confirming tell: yields up AND dollar down
- Overnight into 08-21: equity futures modestly higher, but **the 30y yield sits near 5.25% while the dollar is at a three-month low**, keeping the tone defensive. Gold rallying alongside. Source: https://ts2.tech/en/stock-market-today-08-21-2026/
- **This combination is the whole argument.** Higher yields normally pull the dollar *up* — that is the carry mechanism, and it is what happens when a central bank is tightening. Yields up while the dollar falls is the opposite signature: investors are demanding more compensation to hold the debt *and* leaving the currency. That is term premium and fiscal risk, not policy tightening.
- It also resolves the objection I raised against my own gold idea. The bear case for gold was "real yields grind higher and gold falls with bonds". A three-month low in the dollar is direct evidence that is *not* the regime currently in force. Gold conviction stays at 4 rather than being cut.
- Gold spot 08-20 close **$4,475.46/oz, -1.05%** (physical eased as the Treasury moved to cap yields; silver held a two-month high). Source: https://www.usagold.com/daily-precious-metals-market-report-august-20-2026/

## [06:43 ET] NEWS — guidance changes in recent 8-Ks worth screening
- **TheRealReal (REAL)** — *raised* FY26 guidance and issued Q3 guidance, as of 08-06. Luxury resale; a direct trade-down beneficiary on the same consumer thesis as DG but from the aspirational end. Source: https://www.sec.gov/Archives/edgar/data/0001573221/000157322126000052/real-20260807xex991pressre.htm
- **Mistras Group (MG)** — raised FY guidance to $740-755M revenue, $92-95M adj. EBITDA. Asset-integrity inspection services, heavily energy/infrastructure exposed. Source: https://www.sec.gov/Archives/edgar/data/0001436126/000162828026055344/a8kexhibit991-q22026.htm
- **Dorman Products (DORM)** — *cut* FY26 net sales growth from 7-9% to **3-5% on tariffs**. Negative; noting as a tariff read-through for auto aftermarket, not a candidate.
- **Medline (MDLN)** — raised organic sales to 9-10% but **cut adj. EBITDA to $3.3-3.4B from $3.5-3.6B**. Growing revenue while margin guidance falls is a low-quality raise; not a candidate.

## [06:46 ET] POSITION REVIEW — the book has one correlated bet it did not intend to make
Reviewing all 19 open positions against today's macro, four of them — **HD, BCC, LCII, NKE** — are the same trade: long US discretionary demand that is financed at long-term rates and squeezed by fuel costs. The 30y just printed **5.249%, a two-decade high**, and Walmart just blamed **$4 gas** for a comp miss. Both legs of that bet moved against the book in the same session. Per config/strategy.md the correlation cap is 3 ideas on one driver; this is 4, and nobody chose it — it accumulated one day at a time.
Individually:

## [06:46 ET] POSITION UPDATE — HD — opened 08-18 @ 340.00 and 08-19 @ 337.49 — **CLOSE, do not wait for the 328 stop**
- last **334.49** (-1.6% / -0.9%), fell 2.85% on 08-20. Below the 20-day (342.35), the 50-day (339.74) and the 200-day (346.25); **-15.88% off the 397.63 high**. Every moving average is now overhead resistance.
- decision: **exit**. The thesis was a housing-turnover recovery. The single most important input to housing turnover is the long end of the curve, and the long end just made a two-decade high *after* the Treasury doubled its buyback to defend it. That is the thesis being falsified by the news, not by the price.
- Waiting for 328 buys nothing: it is 2% lower, inside a single 9.32 ATR day, and the reason to hold to a stop is that the thesis might still work. Here it specifically cannot while 30y yields rise.

## [06:46 ET] POSITION UPDATE — LCII — opened 08-18 @ 94.00, target 138, no stop — **TAKE THE PROFIT, close**
- last **105.44, +12.2%**. Below the 200-day (118.32), -33.96% off the 159.66 high, adv20 only $28.2M.
- decision: **close and book the 12%.** LCI supplies RV components. An RV is the single most rate-sensitive, most fuel-sensitive big-ticket discretionary purchase in the US consumer basket — it is financed over 10-15 years at long rates and it gets roughly 6-10 mpg. **$4 gas and a 5.25% 30y attack this position from both sides simultaneously.** A 138 target (+31% more) requires a discretionary recovery that the tape is actively pricing out.
- This is the position I would most regret holding, precisely because it is green and therefore easy to leave alone.

## [06:46 ET] POSITION UPDATE — BCC — opened 08-18 @ 81.00, stop 76, target 92 — **hold, but raise the stop to 79.40**
- last **81.77** (+0.95%), sitting exactly on its 20-day (82.00), above the 50-day (77.69) and 200-day (76.58). ATR 4.04%, adv20 $27.7M.
- decision: **hold with a tighter stop.** Weaker version of the HD problem — Boise Cascade is wood products into new residential construction, so rates hurt it, but unlike HD its structure is still intact (above both the 50- and 200-day) and builders are less rate-elastic than resale turnover. The original 76 stop is 7% away, which is too much room to give a thesis the macro is arguing against. 79.40 sits just under the recent consolidation shelf and is ~0.7 ATR below spot.
- captured via add_candidate.py with the revised stop.

## [06:46 ET] POSITION UPDATE — NKE — opened 08-17 @ 40.00 and 08-18 @ 38.00, target 65/62, no stop — **hold, but cut the target to 52 and set a hard invalidation at 38.60**
- last **40.21**. **-41.84% off the 69.14 high and only +3.47% above its 52-week low of 38.86.** Below the 20-day (41.54), 50-day (42.56) and 200-day (52.72).
- decision: hold the position, **but a 65 target (+62%) is not defensible into a consumer the tape is repricing lower.** That target was set for a turnaround in a normal consumer; Walmart's 2.6% comps say this is not one. Cutting to **52**, which is the 200-day and a level the stock actually traded at — a defended level rather than an aspiration.
- The no-stop structure is also wrong here. NKE is 3.5% above a 52-week low; "no stop" on a name making new lows is not patience, it is an unlimited-downside bet on a turnaround with no date. Invalidation: **a close below 38.60**, under the 52-week low, which would say the de-rating is not finished.

## [06:47 ET] LEVELS — correcting my own BCC stop before capturing it
- I first wrote 79.40. That is **0.72 ATR** below spot on a name with a **4.04% ATR** — a stop that close is not a risk control, it is a coin flip on daily noise, and it is exactly the mistake config/universe.md warns about ("a micro cap with a 9% ATR stopped at 4% is a coin flip on noise").
- Revised to **76.90**: 1.48 ATR below spot, sited **just below the 50-day (77.69) and just above the 200-day (76.58)**. A close under the 50-day is a real technical event; 79.40 was not. R:R against a 92 target from an 81 entry = **2.68**, which clears the swing floor of 2.0 on its own merits rather than by tightening the denominator.

## [06:48 ET] POSITION UPDATE — XLE — open 3× (08-15 @ 60.80, 08-16 @ 60.50, 08-18 @ 60.80) — **hold, raise stop to 59.80, but do NOT re-pitch**
- last **63.75, +4.9%** on all three entries. **-1.47% off the 52-week high of 64.70**, +18.5% above the 200-day (53.80). ATR only 1.98%.
- decision: **hold with the stop raised from 57.80/58.60/59.20 to a single 59.80**, sited just below the 20-day (60.08) so a genuine trend break takes it out rather than noise. That is roughly a free trade on all three tranches.
- **Deliberately not captured as a candidate.** Remaining reward to the 67 target is +5.1% against 6.2% of risk to the new stop — **R:R 0.82, which fails the swing floor of 2.0.** XLE has also now been recommended **5 times in 10 days** and sits 1.5% from a 52-week high. An idea that is right, crowded, extended, and out of reward is a hold, not a recommendation. Publishing it a sixth time would be the anchoring the prior-context guard exists to catch.
- The thesis itself is being confirmed — Walmart naming $4 gas is a direct read-through to energy revenue — which is exactly why the discipline matters: a confirmed thesis at a bad price is still a bad entry.

## [06:48 ET] POSITION UPDATE — PFE — opened 08-18 @ 25.80, target 38, no stop — **hold, best-behaving position in the book**
- last **27.79, +7.7%**. Above the 20-day (26.12), 50-day (25.31) and 200-day (25.98); **-3.32% off its 52-week high** of 28.745, adv20 $1.06B.
- decision: hold, no change. This is the only open position that is both working and structurally uncorrelated to the two things breaking today (long rates, the discretionary consumer). Pharma cash flows are the natural place to be when the consumer cracks. Not re-pitched — nothing changed and it needs nothing.

## [06:48 ET] POSITION UPDATE — CCJ — open 2× (08-17 @ 95.00, 08-18 @ 88.00), target 135, no stop, long_term — **hold, continuing accumulation**
- last **95.59**. Below the 200-day (104.82) but above the 20-day (93.51); **-29.32% off the 135.24 high**, adv20 $274.9M.
- decision: hold. This is a long-term accumulation and per config/strategy.md it legitimately repeats while unfinished — **stating plainly that it is a continuing position, not a new idea.** The uranium/datacenter-power thesis has no dated catalyst and is not disturbed by today's macro; if anything a fiscal-dominance regime favours hard assets and regulated power. Not re-captured today because there is no new information and no level change — re-pitching it would just be noise.

## [06:50 ET] CALENDAR — the dated catalyst I nearly missed: Jackson Hole, Aug 27-29
- **Kevin Warsh delivers his first Jackson Hole keynote as Fed chair on the morning of Friday, Aug 28.** He took office May 22, 2026. The symposium runs Aug 27-29; theme is financial innovation and its implications for payments and policy. It lands **19 days before the Sept 16 FOMC**. Sources: https://www.regardsofwallstreet.com/news/jackson-hole-2026-dates-schedule-warsh-first-speech , https://note.com/umaki11/n/nc14166e90e51?hl=en
- **This is the most important dated event in the window and it is not an earnings print.** A new Fed chair's debut keynote is the single highest-variance scheduled macro event available, because there is no track record to price against - the market has 11 years of reaction data for the *symposium* and zero for *this speaker*.
- It also sits directly on top of every macro trade in this report: the dollar is at a three-month low (**DXY 98.558 on 08-20, lowest since May 14**), the 30y is at a two-decade high, and gold is reclaiming its 200-day. Warsh's tone moves all three at once. Source: https://www.investing.com/news/economy-news/dollar-hugs-threemonth-lows-as-treasury-seeks-to-sooth-the-bond-market-4868503
- The political overlay makes it sharper: Bessent is publicly pressuring Warsh to ease while simultaneously buying back the long end. A hawkish debut would be read as Fed independence reasserting itself; a dovish one as fiscal capture. Those two readings send gold and the dollar in opposite directions.
- **Operational consequence: any dollar-sensitive entry today should be sized for, or wait for, Aug 28.** This is the reason the GLD entry is an accumulation plan with wait:true rather than a buy-here - and I am now stating that explicitly rather than leaving it as a technical preference.

## [06:50 ET] LEVELS — EM on a falling dollar
- **DXY 98.558**, lowest since May 14; long-end yields highest since 2007. Flows into the two largest EM equity ETFs are **the strongest in over a decade**. Sources: as above, plus https://www.alliancebernstein.com/corporate/en/insights/investment-insights/how-us-dollar-weakness-could-buoy-emerging-markets.html
- EEM 66.62, ATR 1.59%, SMA20 65.03 / SMA50 66.04 / SMA200 61.07, -6.92% off the 71.57 high, adv20 $1.42B
- VWO 60.02, only -2.43% off high — less room than EEM
- EWZ 34.14, -18.75% off high, **below all three moving averages** — Brazil is the laggard but it is falling, not basing
- FXI 35.67, -13.46% off high, below the 200-day (36.96)

## [06:50 ET] REJECTED — MU — the "record tech insider buying" article names Micron as an AI-memory beneficiary, but `market_data.py insiders MU` shows **0 open-market buys and 159 sells worth $175.5M over six months, net -$175.5M**. The insider signal here is absent, not present. MU is also +405.9% off its 52-week low with a 6.03% ATR. Not buying a five-bagger on someone else's thesis while the people who run it are only selling.
## [06:50 ET] REJECTED — VWO, FXI, EWZ — VWO has just 2.4% to its high (no room); FXI and EWZ are both below their 200-day, so the weak-dollar bid is not yet showing up in their price. EEM is the one with both room and structure.

## [06:52 ET] SMALL CAPS — screened for insider clusters, verified each against Finnhub Form 4 data
Screener source: https://simplywall.st/stocks/us/diversified-financials/nyse-evtc/evertec/news/top-undervalued-small-caps-with-insider-activity-in-august-2/amp
I checked every name rather than trusting the screener, and the difference mattered — most "insider buying" headlines dissolve on contact with the actual filings.

| Symbol | Buys | Distinct buyers | Buy $ | Sells $ | Verdict |
| --- | --- | --- | --- | --- | --- |
| **EVTC** | 7 | **5** | $2.25M | $1.4M | **genuine cluster — captured** |
| ENOV | 13 | 1 | $0.24M | $0 | one director repeatedly; not a cluster |
| SONO | 11 | 2 | $29.69M | $0.7M | Coliseum Capital, a fund accumulating — not management |
| ADV | 9 | 3 | $0.37M | $0 | buy prices span $0.69 to $34.60 — data looks corrupt |
| PMTS | 2 | 1 | $0.19M | $0.1M | one buyer, $0.21B cap |
| RM | 3 | 2 | $0.35M | $4.7M | **29 sells vs 3 buys — net negative** |

- **REJECTED — SONO** — the $29.69M is Coliseum Capital Management, a large outside holder adding to a stake, not executives buying their own company. Config flags insider *executive* purchases as predictive because they buy for one reason; a fund accumulating is an ordinary position build. Sonos is also consumer-durables discretionary, which is the exact exposure I am cutting elsewhere today.
- **REJECTED — RM (Regional Management)** — 29 sells worth $4.7M against 3 buys worth $0.35M. It is also a subprime consumer lender, i.e. levered to the borrower Walmart just described as cutting back on $4 gas. Wrong side of today's macro with a negative insider signal.
- **REJECTED — ADV (Advantage Solutions)** — Form 4 buy prices range from $0.69 (Kilts, March) to $34.60 (Peacock, May) in the same six-month window. That is either a corporate action the data does not reflect or bad data. **I will not set levels on a price series I cannot trust.**
- **REJECTED — PMTS (CPI Card Group)** — one buyer, and a $0.21B market cap caps sizing at 1% under config/strategy.md. Q2 sales grew to $149.2M from $129.8M, but a single director purchase is not enough evidence to carry a micro cap.
- **HELD BACK — ENOV (Enovis)** — 26.18, ATR 6.53%, -19.22% off the 32.41 high, above the 50-day (25.11) and 200-day (25.12), adv20 $33.3M. Thirteen open-market purchases with **zero sales** over six months is persistent conviction, but all thirteen are Oliver Engert alone. That is one person's view, not five independent ones, and config is explicit that it is the *cluster* of distinct buyers that carries the signal. Watchlist, not a recommendation.

## [06:52 ET] REJECTED — REAL (TheRealReal) — the trade-down idea that did not survive its own filing
- 11.65, ATR 6.24%, -33.02% off the 17.39 high, below the 200-day (12.14), adv20 $40.0M.
- The fundamentals are genuinely good: Q2 GMV +22%, revenue +17%, gross margin 74.4%, adjusted EBITDA margin 7.0% (+290bp), FY26 revenue guidance raised to $788-797M.
- **But it fell 11.7% on the day it raised guidance, because it filed a shelf registration alongside.** That is precisely the failure mode universe.md names for small caps — "a secondary offering is the most common way these theses die well before the fundamental case is settled" — and here it is not hypothetical, it is filed. Net loss also widened 140% to $27.2M, so the company has a reason to use the shelf.
- Killed on reward-to-risk, honestly measured: against a bear case of ~8.50 that assumes the shelf gets used, an entry near 11.00 and the 17.39 prior high give **1.83 R:R**, under the 2.5 long-term floor. I could clear the floor by marking the bear case at 8.05, but that would be tuning the denominator to pass the test — exactly what config/strategy.md forbids. There is also no dated catalyst before Q3 earnings in November.

## [06:54 ET] CRYPTO — no new position, and the reason is specific
- Live prices (CoinGecko, fetched): **BTC $77,894 (+8.34%/24h), ETH $2,399.05 (+5.11%), SOL $91.23 (+4.44%)**. BTC 24h volume $67.0B.
- The rally is attributed to Treasury buyback liquidity, SEC token-fundraising exemptions, **White House support for the Clarity Act**, $517M of spot-BTC-ETF inflows, and >$1B of short liquidations through $69k.
- **But the Clarity Act leg is much weaker than the tape implies. The Senate delayed its vote to September, and prediction markets now price only about a 16% chance it becomes law in 2026, down sharply from earlier expectations.** Source: https://coingape.com/markets/bitcoin-ethereum-and-xrp-price-outlook-after-clarity-act-vote-pushed-to-september/
- So a meaningful part of a 22%-in-three-sessions move rests on legislation the betting markets say probably will not pass this year, plus a **one-time** liquidation flow that by definition cannot repeat — those shorts are already gone.
- **Decision: no new crypto candidate, long or short.** Chasing BTC at 77,894 after a squeeze is buying the exit liquidity of the people who were just liquidated. Re-shorting is worse: I just closed two shorts for a ~21% loss doing exactly that, and the honest lesson is that a broken short does not become a good short at a higher price. There is no edge here in either direction today, and "no trade" is the correct output rather than a manufactured one.
- Caveat on sourcing: several Clarity Act articles quote stale prices (BTC ~$64,400, ETH ~$1,900) from before this week's move. I am using them **only** for the legislative timeline and the 16% probability, not for levels. Levels come from the CoinGecko fetch above.

## [06:54 ET] REJECTED — AVGO — 364.03, -26.46% off the 495 high, **below its 20-day (396.74), 50-day (388.58) and 200-day (369.17)**, earnings Sep 2 amc. The setup looks tempting but insiders are net **-$630.1M** over six months (147 sells, a single $373K buy by one director in June). Buying a broken 200-day into a doubted AI-capex print while management sells $630M is the wrong side of both signals.
## [06:54 ET] REJECTED — NVDA — 216.85, above every moving average, earnings Aug 26 amc, consensus $93-95B revenue and ~$2.06 EPS. No candidate because **I have no differentiated view**. Everything I know about this print is in the consensus, the stock is 8.32% off its high with $24.8B a day of liquidity discounting it continuously, and "own the biggest name into the biggest catalyst" is a position, not an edge. Capturing it would be padding the report with the most obvious idea available.

## [06:54 ET] CORRELATION CHECK — I am at the cap on one driver, so I am stopping
Counting the captured book by what actually has to happen for each to work:
- **falling dollar / fiscal dominance: GLD, EEM, EVTC — that is 3, exactly the config/strategy.md cap.** All three lose together if Warsh delivers a hawkish debut on Aug 28 and DXY bounces off its three-month low. **No further dollar-sensitive idea gets added today**, regardless of how good it looks.
- weak US consumer: DG, NKE (a downgrade, not an addition) — 2
- energy/shipping: DHT — 1
- rates/housing: BCC — 1, and reduced from 4 by closing HD and LCII
The concentration is real and deliberate rather than accidental, which is the difference from the HD/BCC/LCII/NKE cluster I found in the open book. Synthesis should state the Aug 28 single-point-of-failure plainly.

## [06:56 ET] LEVELS — US power, the sharpest fundamental-vs-price divergence I found today
- PJM capacity price: **$28.92/MW-day (2024/25) -> $329.17/MW-day (2026/27)**, more than tenfold. Data centers added ~$6.3B to electricity costs across 13 states in one auction and **$29.4B across the last four**. Sources: https://ieefa.org/resources/projected-data-center-growth-spurs-pjm-capacity-prices-factor-10 , https://thehill.com/policy/technology/5970522-data-center-power-costs-pjm/
- **PJM's capacity auction failed to secure enough supply for the June 2027-May 2028 delivery period — the first time in the grid operator's history.** PJM plans a reliability backstop procurement auction for Autumn 2026. Data centers add >30GW of peak demand by 2030; the 2026/27 forecast peak alone rose 5,400MW. Source: https://pro.edgex.exchange/en-US/news/article/pjm-first-capacity-shortfall-data-centers
- And yet the owners of that scarce capacity are at or near 52-week lows:

| Symbol | Last | Off 52w high | Above 52w low | SMA200 | Insiders (6mo) |
| --- | --- | --- | --- | --- | --- |
| **CEG** | 272.92 | -29.1% | +19.4% | 300.36 | **1 buy $417,931, 0 sells** |
| VST | 138.94 | -29.4% | **+4.7%** | 160.12 | 0 buys, **8 sells $6.86M** |
| NRG | 115.36 | **-39.3%** | **+2.5%** | 149.73 | not checked |
| GEV | 966.01 | -19.2% | +82.2% | 866.18 | not checked |

- **Why the divergence, and it is not irrational**: New York imposed a one-year moratorium on environmental permits for large data centers, and the Trump Administration together with mid-Atlantic governors floated **capping electricity rates in the region**. A political cap turns a scarcity windfall into a regulated return. That, plus a below-consensus 2026 adjusted earnings guide and Calpine digestion, is what took CEG down ~35% in H1. Source: https://www.foreignpolicyjournal.com/2026/07/19/constellation-energy-nasdaq-ceg-stock-price-trades-at-deep-discount-as-new-york-moratorium-tightens-power-outlook/
- **Chose CEG over VST and NRG on the insider tape and on structure.** CEG is the only one of the three where insiders are net buyers with zero sales, and it is the only one holding above its 20-day (270.31) and 50-day (262.50) — basing rather than falling. VST and NRG are 4.7% and 2.5% off 52-week lows respectively and below every moving average.
- **REJECTED — VST** — 0 open-market buys against 8 sells worth $6.86M in six months, price below the 20-, 50- and 200-day, 4.73% off a 52-week low. Same thesis, worse evidence, worse structure. Deeper de-rating is not the same as better value.
- **REJECTED — NRG** — the deepest drawdown at -39.27%, but it carries the largest retail electricity book of the three, which is a direct claim on the same squeezed household Walmart just described. Retail power exposure in a $4-gas consumer is the wrong end of this trade.
- **REJECTED — GEV** — the equipment supplier rather than the asset owner, and already +82.2% off its low and above its 200-day. The scarcity is in the megawatts, not in the turbines, and GEV has not de-rated.

## [06:59 ET] FALSIFICATION — arguing against my own book
Not per-idea (each candidate carries its own `counter_argument`), but against the *portfolio*, which is where the correlated mistakes live.

**1. Three of eight ideas die on the same morning.** GLD, EEM and EVTC all require the dollar to keep falling. Warsh's Jackson Hole debut is **Fri Aug 28** and he has a hawkish record. If he uses his first keynote to assert Fed independence against Bessent's public pressure, DXY bounces off a three-month low and all three lose together. This is at — not over — the config correlation cap of 3, but the cap counts ideas, not conviction-weighted capital, and these are 4%, 2.5% and 2% of capital, the three largest sizes in the report. **Mitigation actually applied**: GLD is `wait:true` with a staged accumulation below spot, and EEM is explicitly half-size before the speech. Neither is a full position into Aug 28.

**2. The report is 100% long, in a tape that fell on the discount rate.** Eight buys, no shorts, no hedge. I considered a short /MES and did not take it: I have no differentiated view on the index, and manufacturing a hedge I do not believe in to make the book look balanced is the same sin as manufacturing a horizon mix. But the reader should see the skew plainly — **if the 30y keeps rising, essentially every idea here gets marked down together**, and the fiscal-dominance thesis that makes gold work is the same one that de-rates equities. Synthesis should carry this in `data_quality_notes`.

**3. My losing trades and today's best ideas have the same shape — this is the one that worries me most.** The three closed trades are 0/3, all conviction 3, avg -2.4%, and both stop-outs (TJX, KRE ×2) were "buy the de-rated thing because the macro should help it". DG, CEG and EVTC are all that same trade. At **n=3 the sample is statistically noise** and config is explicit not to over-fit a bad week — I am not raising the bar on that basis. But the *mechanism* of those losses is informative independent of sample size: in both cases the thesis was arguably right and the factor exposure (discretionary beta, regional-bank beta) overwhelmed the idiosyncratic story before it could play out. The defence today is that DG, CEG and EVTC each carry a company-specific confirmation the losers did not have — accelerating traffic data, a net-positive insider tape, and a five-buyer insider cluster respectively — rather than a macro syllogism alone.

**4. BCC is my least consistent call, and I am flagging it rather than hiding it.** I am closing HD and LCII because the long end at 5.249% breaks rate-sensitive discretionary demand, then holding BCC, which sells wood into houses. The distinction I drew — builders with rate-buydown budgets are less rate-elastic than existing-home turnover, and BCC alone still holds above its 50- and 200-day — is real but thin. If a reader wants one exit rather than three, **BCC is the defensible fourth close.** The 76.90 stop is what makes holding it a bounded decision rather than a conviction.

**5. Where I let a floor kill an idea rather than tuning to pass it.** REAL cleared on fundamentals (GMV +22%, 74.4% gross margin, guidance raised) and failed on reward-to-risk at 1.83 against a shelf-registration bear case. Moving the bear case from 8.50 to 8.05 would have passed it. I did not. Same with NKE, published at a stated **1.44 R:R that fails its own 2.5 long-term floor** — captured as an honest downgrade for existing holders and flagged so that validation demotes it to the watchlist, which is the correct outcome rather than something to engineer around.

## [07:01 ET] AUDIT — recomputed every reward-to-risk from entry/target/downside, and caught two of my own errors
Ran the arithmetic back from the captured fields rather than trusting what I wrote, because config/strategy.md records a live report that once shipped eight ratios clustered just above a 2.0 floor.

| Symbol | Entry | Target | Downside | Recomputed | I had written | Floor | Pass |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DG | 119.0 | 135.0 | 112.0 (stop) | 2.29 | 2.29 | 2.0 | yes |
| GLD | 398.0 | 520.0 | 360.0 (bear) | 3.21 | 3.21 | 2.5 | yes |
| BCC | 81.0 | 92.0 | 76.9 (stop) | 2.68 | 2.68 | 2.0 | yes |
| **DHT** | 19.6 | 22.5 | 18.6 (stop) | **2.90** | **2.25** | 2.0 | yes |
| EEM | 65.6 | 71.5 | 63.0 (stop) | 2.27 | 2.27 | 2.0 | yes |
| **NKE** | 40.0 | 52.0 | 32.0 (bear) | **1.50** | **1.44** | 2.5 | **no** |
| EVTC | 29.4 | 48.0 | 22.0 (bear) | 2.51 | 2.51 | 2.5 | yes |
| CEG | 266.0 | 385.0 | 220.0 (bear) | 2.59 | 2.59 | 2.5 | yes |

- **Two errors, both mine, both now corrected in candidates.jsonl.** In each case I had divided using the *last price* instead of the *entry* — DHT off 19.80 rather than 19.60, NKE off 40.21 rather than 40.00.
- Both errors ran in the **conservative** direction, understating the ratio, which is the harmless direction to be wrong in — but they were still wrong, and the point of the check is that I could not tell which direction the error went until I ran it.
- Worth noting what the spread looks like: 1.50, 2.27, 2.29, 2.51, 2.59, 2.68, 2.90, 3.21. These are **not** clustered just above their floors, and one of them fails outright. That is the signature of levels set first and ratios measured afterwards, which is the intended order.
- NKE's 1.50 against a 2.5 floor is left in deliberately, correctly labelled, so `validate_report.py --enforce` demotes it to the watchlist. It is a downgrade notice for existing holders, not a recommendation to buy.

## [07:03 ET] REJECTED — PRAX (Praxis Precision Medicines) — the catalyst moved, and the calendar was stale
- Chased this because a September PDUFA date for relutrigine (SCN2A/SCN8A developmental and epileptic encephalopathies) would have been a clean dated binary in an uncorrelated driver — exactly what this report is short of.
- **It is not in the window. The FDA extended the review by three months: the PDUFA target moved from Sept 27, 2026 to Dec 27, 2026.** The extension followed Praxis submitting additional sensitivity analyses of existing data, which the FDA deemed a "major amendment"; **no new clinical studies were requested and no safety or manufacturing concerns were cited** — so it is a procedural delay rather than a signal about approval. Source: https://www.stocktitan.net/news/PRAX/praxis-precision-medicines-announces-extension-period-for-nvfzxh6lpq52.html
- Two more reasons not to force it even as a longer-dated idea: PRAX is **+136.05% off its 52-week low** at 364.58 and only 7.16% off its high, so the approval is substantially priced; and insiders show **0 open-market buys against 12 sells worth $3.61M** in six months. Cash and investments of ~$1.4B at Mar 31 with runway into 2028 means dilution risk is genuinely low, which is the one thing here that is better than it looks.
- **The lesson worth recording: the earnings/catalyst calendar I pulled at 06:47 was stale on this name.** I only found the extension because I searched the specific drug rather than trusting the date. Any dated catalyst in this report that came from a calendar rather than from the company's own filing should be treated as provisional.

## [07:03 ET] RESEARCH COMPLETE
- **candidates captured: 8 unique** (11 lines; DG, DHT and NKE were each re-captured with corrections — synthesis takes the last entry per symbol)
  - DG (3, swing, 2.29) · GLD (4, long_term, 3.21) · BCC (3, swing, 2.68) · DHT (3, swing, 2.90) · EEM (3, swing, 2.27) · NKE (2, long_term, 1.50 — **fails its floor by design**, a downgrade notice) · EVTC (4, long_term, 2.51) · CEG (3, long_term, 2.59)
- **exit instructions recorded in notes only, deliberately not captured as candidates** because a `buy`/`short` row would misrepresent them: **/MBTU6 close both shorts at market** (~21% against, the day's most urgent action), **TJX close** (stopped out), **HD close**, **LCII close and book +12.2%**. Plus holds: XLE (stop to 59.80, not re-pitched — R:R now 0.82), PFE (no change), CCJ (continuing accumulation, no change).
- **horizon skew, stated rather than corrected**: 4 long_term, 4 swing, **0 intraday**. Nothing intraday cleared the bar — the equity session was closed all through this run and the one dated intraday-grade event, Warsh at Jackson Hole, is seven days out. No day trade was manufactured to fill the lane.
- **direction skew: 8 of 8 are long.** Flagged in the falsification block; synthesis should carry it in `data_quality_notes`. I declined to add a short /MES purely to balance the book.
- **coverage gaps**
  - **Event contracts: zero, and this is a source failure, not a judgement.** `market_data.py events` returned count 0 for CPI, inflation, interest rates, Bitcoin, S&P 500, unemployment, recession and government shutdown; the only "Fed" hit was a mis-indexed soccer parlay with null pricing. Robinhood Prediction Markets went unchecked today.
  - **Index and commodity quotes unavailable**: SPX, NDX, DJI, RUT, **VIX**, DXY, gold, WTI, ES and NQ all failed (Yahoo 429, Finnhub index subscription required, stooq 404). Worked around with ETF proxies (SPY/QQQ/IWM/GLD) and with sourced press figures for gold spot and DXY — **no index level in these notes came from a fetch that failed**.
  - No VIX reading at all, so nothing in this report is calibrated to implied volatility.
  - Crypto: prices fetched, no candidate taken by choice (see the 06:54 entry).
  - Did not reach: ag/fertiliser, defence, REITs, Japan/Europe single names, or a systematic small-cap screen beyond the insider-cluster list.
- **sources that failed**: Yahoo Finance chart API (HTTP 429 throughout), Finnhub index quotes (subscription), stooq index symbols (404), Kalshi search via market_data.py (returns unrelated markets), Robinhood's own futures-availability support page (**HTTP 404** — futures availability was verified from secondary sources instead, which is weaker evidence than I would like for a venue check).
- run window: 06:32-07:03 ET, ~31 minutes.

## [07:06 ET] ADDENDUM — research continued past the RESEARCH COMPLETE block above
I had budget left, and config/strategy.md is explicit that there is no target count and no stopping early. I ran a second insider-cluster sweep. **It produced no new candidates**, which is a result worth recording rather than a gap.

### Verified every screener claim against Finnhub Form 4 data — most did not survive
| Symbol | Screener claim | What the filings actually show | Verdict |
| --- | --- | --- | --- |
| ORN | "4 insiders bought $320.8K on Aug 17" | 5 buys / 4 distinct, but dated **Jul 31**, and **5 sells worth $1.83M against $0.37M of buys — net -$1.46M** | rejected |
| VRCA | "4 insiders bought $210.9K on Aug 18" | **0 buys and 0 sells** in the six-month window | unverifiable, rejected |
| EDAP | "4 insiders bought $142.5K on Aug 17" | **1 buy, $0.04M, dated May 11** | unverifiable, rejected |
| PAL | "director bought $272.5K Aug 13" | confirmed: 7 buys / **3 distinct** / $0.38M on **Aug 13-14** vs $0.31M sells | real cluster, rejected on other grounds |
| CLPR | "director/10% owner bought $488.8K" | confirmed $0.49M, zero sells — but **1 distinct buyer**, not a cluster | rejected |

- **The ORN case is the instructive one**: the headline "4 insiders buying" was true and still misleading, because the same window contains five sales worth five times the purchases. A cluster-buy screener that does not net against sales will keep producing this. This is why config says to check `open_market_buys` and `distinct_buyers` directly rather than reading a list.
- **REJECTED — PAL (Proficient Auto Logistics)** — the one genuine fresh cluster, and I am still passing. 5.21 with a **9.0% ATR**, **-52.51% off its high**, only 7.42% above its 52-week low, below its 20-day (6.37), 50-day (6.88) and 200-day (7.55), adv20 $4.1M. **The insiders bought at 5.43-5.55 on Aug 13-14 and it already trades at 5.21 — they are underwater within a week.** More decisive: PAL hauls new vehicles for dealers, so its revenue is new-vehicle unit volume — a big-ticket, rate-financed consumer purchase. That is the same demand I am closing HD and LCII to get away from. Buying it here would contradict the central judgement of this report.
- **REJECTED — CLPR (Clipper Realty)** — one buyer, and a levered NYC residential REIT at $3.29 is a direct claim on long-term rates, which is the thing I am arguing is broken. Wrong side of the day's most important fact.

### Revised close
- **candidates: still 8 unique.** The second sweep added zero, and that is the honest outcome — four of five screener-flagged clusters failed verification, and the one that passed contradicts the report's own thesis. Padding the file with PAL to make the sweep look productive would have been the failure mode.
- **Additional coverage gap for `data_quality_notes`**: third-party insider-cluster screeners disagreed with Finnhub Form 4 data on 3 of 5 names checked (VRCA and EDAP showed essentially no filings; ORN omitted offsetting sales). Any insider claim in this report that was not verified through `market_data.py insiders` should be treated as unsourced. **The one insider claim that was verified is EVTC's — 7 buys, 5 distinct buyers, $2.25M against $1.4M of sales — and it is the reason EVTC carries conviction 4.**
- run window: 06:32-07:06 ET, ~34 minutes.

## [07:09 ET] INTEGRITY CHECK — replaced three market caps I had estimated rather than fetched
CLAUDE.md rule 2 is "never fabricate a number", and on review three `market_cap_usd` values in captured candidates were my own recollection, not a fetch. Verified each against stockanalysis.com and corrected in candidates.jsonl:

| Symbol | I had written | Actual (fetched 2026-08-21) | Error |
| --- | --- | --- | --- |
| DG | $26.5B | **$26.60B** | -0.4% |
| BCC | $3.0B | **$2.85B** | +5.3% |
| DHT | $3.2B | **$3.19B** | +0.3% |

- None of the three was large enough to change a sizing tier or trip a small-cap rule, so no thesis changes. **That is luck, not process** — BCC was out by 5.3% and I had no way of knowing which direction until I checked.
- The values that were already fetched and correct: EVTC $1.78B with 59.75M shares outstanding, forward P/E 7.15, trailing P/E 19.19 (stockanalysis.com); DG P/E now reads 17.05 against the 16.9x I cited from a 08-13 article, consistent within the price move since.
- Every `avg_dollar_volume` in the file is computed from fetched OHLCV (20-day mean of volume x close), not estimated.
- NKE also corrected: $59B (estimated) -> **$59.65B** (fetched). GLD, EEM and CEG carry `market_cap_usd: null` deliberately — GLD and EEM are ETFs where the field is meaningless, and I did not fetch CEG's, so it is left null rather than guessed. All four remaining figures in the file are now fetched values.
