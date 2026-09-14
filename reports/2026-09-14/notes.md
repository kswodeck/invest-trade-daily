# Research log — 2026-09-14

## [06:05 ET] MACRO — rates ripping, CPI hot, FOMC this week
- US10Y **4.95%** (prev 4.83) — +12bp in a day. Source: FRED DGS10 2026-09-10 via `market_data.py macro`
- US2Y **4.56%** (prev 4.43) — +13bp. FRED DGS2 2026-09-10
- 10y-2y curve **+0.33** (prev 0.39), flattening from the front end = market pricing FEWER cuts
- Fed funds effective **3.63%** (DFF 2026-09-10) — so 2Y at 4.56 is ~93bp ABOVE the policy rate.
  The 2s are pricing hikes, not cuts. That is a regime statement.
- CPIAUCSL Aug 2026 **334.131** vs Jul 332.813 = **+0.396% m/m** (~4.9% annualized). Hot.
- Unemployment 4.1% (Aug, unchanged) — no labor-market cover for cutting into that CPI
- TLT 80.87, prev close 80.78, session=pre, age 3722min (Fri 11 Sep close). Source: finnhub
- Crypto (coingecko, live): BTC 78,164 (+1.8% 24h), ETH 2,525.69 (+1.7%), SOL 102.02 (+2.2%)
- FAILED SOURCES: yahoo 429 on every index (^GSPC ^NDX ^DJI ^RUT ^VIX), finnhub refuses index CFDs.
  No SPX/VIX/DXY/WTI level today. Record as a gap.
- **Regime read:** front-end yields above the funds rate with a 0.4% m/m CPI print is a market
  that has stopped believing in the cutting cycle. That is the single driver to trade this week,
  and it argues against long duration, long gold-as-rate-cut-trade, and long high-multiple equity.


## [06:15 ET] MACRO — REGIME CONFIRMED: market prices a HIKE, not a cut
**This inverts the prior read. The 2s were not "pricing hikes" figuratively — a hike is the base case.**

### FOMC: THIS WEEK. Sep 15-16 2026.
- Statement 2:00pm ET Wed **2026-09-16**; Powell presser **2:30pm ET**.
  Source: https://www.federalreserve.gov/newsevents/2026-september.htm (primary, Fed calendar)
- SEP/dot-plot: secondary sources say yes, Fed calendar page does not confirm. UNVERIFIED on SEP.

### August CPI — released Fri 2026-09-11 08:30 ET (BLS, primary)
- Headline **+0.4% m/m**, **+3.4% y/y** — in line with consensus
- Core **+0.3% m/m**, **+2.4% y/y** — core m/m came in ABOVE expectations (the surprise)
  Source: https://www.bls.gov/news.release/cpi.nr0.htm
- NOTE: my earlier CPIAUCSL calc of +0.396% m/m matches the official +0.4%. Good.

### Fed odds (CME FedWatch, as of 2026-09-10)
- **Cut 0.0% / Hold 37.6% / HIKE 62.4%** for the Sep 16 meeting
- One week earlier it was 50.6 hold / 49.4 hike — repriced hard on CPI+oil
  Source: https://www.oddsshopper.com/articles/prediction-markets/fed-rate-cut-odds-september-2026
- Post-CPI Friday, fed funds futures reportedly ~90% hike. NEEDS CONFIRMATION.

### Friday 2026-09-11 price action
- 2Y closed ~**4.65%** — a 2-year high (above my FRED 9/10 print of 4.56)
- 10Y traded **4.975%**, highest intraday since Oct 2023; global bond selloff, 10Y "cusp of 5%"
  Source: https://www.bloomberg.com/news/articles/2026-09-11/global-bond-selloff-sends-10-year-treasury-yields-to-cusp-of-5
- Driver: **crude oil testing $100/bbl** -> inflation fear -> yields. Oil is the macro variable.
- Equities: Dow fell; indices on a losing streak into the CPI print.

## [06:25 ET] CORRECTION + THE REAL DRIVER: an OIL SUPPLY SHOCK (Hormuz/Iran)
**Correction to my own 06:15 note: Friday was NOT a down day.** Intraday it fell, but it CLOSED UP,
snapping a 4-day losing streak as oil backed off. Do not write "Friday selloff".

### Friday 2026-09-11 CLOSE (source: https://investrade.com/market-review-september-11-2026/)
- S&P 500 **7,656** (+65.15, **+0.86%**)
- Nasdaq **26,333** (+251.31, +0.96%)
- Dow **52,657** (+508.71, +0.98%)
- Russell 2000 **2,903** (+12.99, +0.45%)
- WTI **$100.05** (-2.37% on the day — it had been higher)
- Gold **$4,408.90** (+1.60)
- 2Y ~**4.65%** (2-yr high), 10Y **4.975%** intraday (highest since Oct 2023)
- VIX / DXY: NOT PUBLISHED in that recap. Still a gap.
- Movers up: RH, CPRT (acquiring ACVA @ $10.50/sh), KR, SG, ORCL, DELL, HPE, IP (upgrade)
- Movers down: ZUMZ, ADBE, SYK, RMD; airlines ALK ALGT AAL DAL UAL JBLU LUV all cut by Barclays

### OVERNIGHT SUN/MON — this is the story
- **Brent toward $108** (first time since May), WTI near **$103**; Brent +3% overnight,
  +~9% last week. Source: https://www.nbcnews.com/business/energy/us-crude-oil-iran-trump-hormuz-rcna596997
- Cause: **attack on a Saudi oil pipeline**, Houthi advance, strikes on ships in the Gulf.
  **Iran/Gulf-Arab meeting in Oman on opening the Strait of Hormuz was POSTPONED.**
- Futures: **Nikkei -2%**, **S&P 500 futures -0.5%**, **Nasdaq futures -1%**
- Gold **$4,336** (-0.3%) — falling despite a war headline, because real yields are winning
  Source: https://finance.yahoo.com/markets/articles/shares-slip-asia-oil-climbs-231039187.html
- **BOJ may also hike this week** — dual central-bank risk, not just the Fed

### August PPI — released Thu 2026-09-10 08:30 ET (BLS primary)
- Final demand **+0.4% m/m**, **+5.4% y/y** unadjusted
- Core (ex food/energy/trade) **+0.3% m/m**, **+4.7% y/y**
- Final demand goods **+1.1%**; energy **+4.2%**; **diesel +24.1% m/m**
  Source: https://www.bls.gov/news.release/ppi.nr0.htm
- **PPI IS NOT THIS WEEK.** It was last Thursday. Don't put it on the Sep 14-18 calendar.

### Week of Sep 14-18 2026 calendar (times ET)
- Tue 9/15 08:30 Empire Manufacturing (Sep); 13:00 Treasury $18B 20Y; FOMC day 1
- Wed 9/16 08:30 **Retail Sales m/m (Aug)** + ex-autos; 08:30 import/export prices
- Wed 9/16 10:00 Business inventories (Jul), NAHB housing market index
- Wed 9/16 **14:00 FOMC DECISION**, 14:30 Powell presser
- Thu 9/17 08:30 **Jobless claims** + continuing claims + **housing data**; 08:30 **Philly Fed (Sep)**
- Thu 9/17 10:00 Pending home sales (Aug)
- Fri 9/18 09:15 Industrial production (Aug) + cap utilization; 10:00 Leading index
  Source: https://investrade.com/weekly-event-calendar-09-14-2026-09-18-2026/
- Housing STARTS specifically: listed only as "housing data" Thu 8:30. UNCONFIRMED as starts.
- Earnings: LEN, HAIN, CODA, HYFT

## [06:35 ET] OVERNIGHT DETAIL — two shocks at once (energy + AI valuation)
Multiple independent sources agree on the picture. Numbers vary by timestamp; ranges given.

### Oil — the proximate cause is SPECIFIC and verifiable
- **Saudi Arabia halted flows through its East-West pipeline** after drone strikes near pumping stations
- Brent **$107.18-$107.72** (+2.5% to +3.0%); WTI near **$103**; Brent +~9% last week
- Iran/Gulf-Arab Oman talks on reopening Hormuz **postponed**; "fresh Houthi front"
  Sources: https://www.tickmill.com/blog/daily-market-outlook-september-14-2026
           https://nordfx.com/market-news/market-pulse-september-14-2026

### Rates / Fed odds — CONVERGENT across four sources
- CME FedWatch **~87-90% chance of a 25bp HIKE** Wed 9/16
- Kalshi (as of 9/11): **hike 25bp 81% / hold 19% / hike >25bp 2%**
  Source: https://news.kalshi.com/p/fed-rate-hike-odds-core-cpi-september-2026
- Goldman and JPMorgan both moved forecasts to a hike
  Source: https://finance.yahoo.com/economy/policy/articles/fomc-september-2026-odds-rate-201618784.html
- US 10Y **~5.00%**; German 10Y **3.53%**, highest since 2009 — this is a GLOBAL duration event
- **BOJ Friday: ~76% odds of +25bp to 1.25%.** Second hike risk this week.

### Cross-asset overnight
- S&P futures **-0.5% to -0.7%**; Nasdaq futures **-1.2% to -1.7%**; Dow futures -0.25%
- Nikkei 225 **-1.51% to 63,045** (six-week low); Kospi **-2.8%**; Hang Seng -0.5% to 24,687
- Gold **$4,325-4,333 (-0.4% to -1.9%)** — DOWN on a war headline. Real yields dominate.
- DXY **+0.2%**; USDJPY **154.46** (+0.6%); EURUSD 1.1535-1.1598
- BTC **~$77,324 (+0.12%)** per nordfx vs my 06:05 coingecko read of 78,164. Drifting down.

### AI VALUATION WOBBLE — second, independent shock
- **SoftBank -13% in Tokyo** after **Sam Altman confirmed no OpenAI IPO this year**
- SK Hynix and Samsung Electronics both **-3.5%+**; semis leading Asia down
- Tickmill ties it to AI execs committing to slow advanced-model development. UNVERIFIED detail.
- This is why Nasdaq futures (-1.2/-1.7%) are down ~2x the S&P. It is NOT just oil.

### Tradeable read
Energy up + duration down + high-multiple tech down + gold not working as the hedge.
Airlines are the clean short-side expression of $107 Brent (DAL/UAL 2026 guidance is
reportedly built on much lower crude) and Barclays already downgraded the whole group Friday.

## [06:45 ET] THE MACRO CONTEXT I WAS MISSING: a US-Iran war + Hormuz closed
This reframes everything above. The oil move is not a "geopolitical wobble", it is a
physical supply interruption on top of an already-closed chokepoint.

- **Iran has effectively shuttered the Strait of Hormuz** amid the 2026 US-Iran war.
- Saudi had been rerouting **~5 million bbl/day** around it via the 1,200km **East-West
  pipeline** to the Red Sea port of **Yanbu**. That was the workaround.
- **10-11 Sep 2026: drones launched from IRAQ hit the East-West pipeline** (Riyadh and
  Medina areas), causing fires, injuries, material damage. **Saudi shut the pipeline.**
- So the primary route AND the alternate route are both down. Reports put potential loss at
  **~4% of global crude availability** while it stays inoperable.
- Saudi says it will **not retaliate for now**, at Baghdad's request. (De-escalation signal.)
  Sources: https://www.aljazeera.com/news/2026/9/12/saudi-arabia-shuts-critical-oil-pipeline-after-drone-attack-what-happened
           https://www.aljazeera.com/news/2026/9/11/saudi-arabia-says-east-west-pipeline-hit-by-drones-launched-from-iraq
           https://en.wikipedia.org/wiki/2026_East%E2%80%93West_Crude_Oil_Pipeline_attack
           https://oilprice.com/Latest-Energy-News/World-News/Drone-Strikes-Hit-Saudi-Arabias-Vital-East-West-Oil-Pipeline.html
- One source references a "US-Iran ceasefire announcement" just before the strike. The
  war/ceasefire state is FLUID and is the single largest risk to any oil-linked position
  in either direction. Headline risk is two-sided and enormous. UNVERIFIED as of now.

### SoftBank / OpenAI — confirmed, with a caveat on the magnitude
- Altman confirmed **no OpenAI IPO in 2026**, calling a 2026 listing "ill-advised" given
  the focus on AI safety. Anthropic CEO Dario Amodei called for slowing AI development.
- SoftBank fell — sources disagree: **-11%, -12%, or -13.18%**. Report as ~11-13%.
- SoftBank's OpenAI stake: **$64.6bn cumulative**, ~**13% ownership**.
  Sources: https://asia.nikkei.com/business/markets/softbank-shares-slip-over-12-on-openai-ipo-delay-concerns
           https://www.investing.com/news/stock-market-news/softbank-group-stock-slides-11-after-openai-says-it-will-not-seek-a-2026-ipo-4898822
           https://www.businesstoday.in/markets/stocks/story/softbank-shares-tumble-as-openai-anthropic-raise-ai-safety-alarm-555328-2026-09-14
- NOTE: one source's SoftBank price math is internally inconsistent (6540 vs prev close
  5678 is a RISE). Do not quote the yen levels. Percentage only.

## [06:14 ET] LEVELS — the tape is long energy, short housing
Source for all: `market_data.py history <sym> --days 120` (nasdaq). Closes are 2026-09-11.

| sym | last | ATR14 | ATR% | sma20 | sma50 | 120d hi | 120d lo | % off hi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DVN | 50.23 | 1.18 | 2.34 | 48.27 | 45.45 | 52.71 | 40.00 | -4.7 |
| XLE | 65.14 | 1.21 | 1.86 | 63.72 | 60.14 | 66.17 | 52.62 | -1.6 |
| XLF | 57.25 | 0.66 | 1.16 | 57.70 | 57.11 | 58.60 | 47.67 | -2.3 |
| KRE | 73.90 | 1.16 | 1.57 | 74.75 | 75.52 | 78.35 | 63.05 | -5.7 |
| FDX | 311.99 | 7.61 | 2.44 | 325.14 | 318.97 | 345.37 | 269.36 | -9.7 |
| GLD | 398.77 | 7.90 | 1.98 | 409.43 | 391.22 | 448.70 | 363.32 | -11.1 |
| BCC | 75.44 | 2.22 | 2.94 | 79.16 | 78.88 | 88.43 | 65.00 | -14.7 |
| ITB | 89.54 | 1.93 | 2.15 | 94.91 | 96.75 | 106.38 | 84.98 | -15.8 |
| SVRA | 5.30 | 0.20 | 3.72 | 5.44 | 5.60 | 6.48 | 4.70 | -18.2 |
| LEN | 79.60 | 2.25 | 2.82 | 84.48 | 84.85 | 97.94 | 76.63 | -18.7 |
| DHI | 137.89 | 3.42 | 2.48 | 144.91 | 147.33 | 170.79 | 132.39 | -19.3 |
| CCJ | 96.68 | 3.76 | 3.89 | 100.03 | 95.18 | 131.21 | 83.15 | -26.3 |
| LCII | 91.02 | 3.20 | 3.51 | 101.67 | 103.68 | 138.15 | 89.00 | -34.1 |

- **Energy is leadership** (XLE -1.6% off high, above both averages; DVN -4.7%, 20>50).
- **Anything rate-sensitive and big-ticket is the wreck**: homebuilders -16 to -19%, BCC (wood
  products) -14.7%, LCII (RV components) -34.1% and printing new 120-day lows.
- This matters for the book, not just for new ideas: **three open longs — LCII, BCC, and to a
  lesser degree NKE/LULU — are the same bet on the rate-sensitive consumer**, taken before the
  10-year went to 4.95%. That is the correlation cap being breached by drift rather than by choice.

## [06:17 ET] POSITION UPDATE — LCII — opened 2026-08-17 @ 94.00, now 91.02, -3.2%
- decision: **CLOSE**. Captured via add_candidate.py as a `sell`.
- why: new 120-day lows (traded 90.37 vs 89.00 low) with no stop under the position, in the exact
  factor the rate move is punishing. THO reports 2026-09-22 and is the read-through.
- this is not a stop-out — there was no stop. It is a discretionary exit on a broken thesis.

## [06:18 ET] REJECTED — ITB/LEN short — right thesis, no reward left
- The homebuilder short is the obvious expression of 10Y 4.95%, and it does not clear the floor.
  ITB entry ~90.50 with an honest 1.8-ATR ETF stop (3.47 → stop 95.20, risk 4.70) needs a 81.10
  target for 2.0:1 — that is 4.6% BELOW the 120-day low of 84.98, i.e. the ratio only works by
  assuming a breakdown to new lows. Shorting a group already -16 to -19% off its high, after the
  move, is paying for the part that already happened. Not published.
- Same arithmetic kills a LEN short, and LEN reports 2026-09-16 AMC, so it is a single-name gap
  bet on top of that.

## [06:19 ET] DATA GAPS so far
- yahoo returns HTTP 429 for every index: ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX. finnhub refuses index
  CFDs ("Market data subscription required"). stooq 404s them. **No SPX, VIX, DXY, WTI or 10Y
  quote level today** — rates come from FRED instead, which is 2026-09-10/11 vintage, not live.
- `market_data.py events` returns count=0 for "FEDDECISION", "Fed funds", "interest rate", "CPI"
  and "recession", and returns unrelated sports cross-category markets for "Fed". **No event
  contract pricing available this run.** The three open KXFEDDECISION positions cannot be marked.

## [06:52 ET] Hormuz status + what I could NOT verify
- **Strait of Hormuz has been CLOSED SINCE MARCH 2026.** This is not new news today.
  The US-Israel/US-Iran war began **2026-02-28**. Exports "far below normal" since.
- East-West pipeline normally moves **4-5 million bbl/day = 4-5% of global supply**.
  Both of Saudi's primary export routes are now down simultaneously.
- **Repair timeline unknown** — Saudi has not disclosed damage extent. An April 2026 attack
  on a pumping station was repaired in **three days**, which is the only precedent available.
  That precedent argues this oil spike could reverse violently and fast.
- **No ceasefire** per Al Jazeera 9/12. (A barchart headline referenced a "US-Iran ceasefire
  announcement" just before the strike — I could NOT reconcile these. Treat as UNVERIFIED
  and treat the war state as unknown.)
  Source: https://www.aljazeera.com/news/2026/9/12/saudi-arabia-shuts-critical-oil-pipeline-after-drone-attack-what-happened

### UNVERIFIED / NOT ESTABLISHED — do not use in the report
- No major M&A confirmed as announced TODAY 9/14. Items surfaced (Union Pacific/Norfolk
  Southern, Conagra guidance, DraftKings prediction markets, BioMarin/Amicus $4.8bn) came
  back **undated** from search and could not be tied to 2026-09-14. Do not publish them.
- Only confirmed deal in the window is Friday's: **CPRT acquiring ACVA at $10.50/share**.
- CNTB (Connect Biopharma) Seabreeze asthma topline reportedly due today 9/14 — single
  low-quality source, UNVERIFIED.
- Pre-market single-stock movers list from search was low-quality scraped micro-caps.
  Not usable. No reliable US pre-market mover data obtained.
- Still no VIX, DXY level, or SPX futures price (only percentages). Yahoo 429 all morning.
- SEP/dot-plot at this meeting: secondary sources say yes, Fed calendar does not confirm.

## [06:09 ET] TIMESTAMP CORRECTION — earlier headings in this file are estimates, not clock reads
Every `[HH:MM ET]` heading above this line was written from my own sense of elapsed time and is
wrong, in both directions: my own run to 06:19, and the news sub-agent's block headed 06:25-06:52.
`date` says **06:09 ET** at this point in the run. The findings and their sources are unaffected —
only the heading times are. Headings below this line are real `date` reads.
Real start of run: 06:01 ET.

## [06:09 ET] REJECTED — airline short (JETS/DAL/UAL/LUV) — after the move, and one-way war risk
- Mechanism is real: Brent ~107 and jet fuel is the biggest variable cost. But the group has
  already taken it — JETS -17.3% off high, DAL -16.5%, UAL -20.9%, LUV -26.1%, all below their
  20- and 50-day averages. JETS even closed UP 1.2% Friday *into* the Barclays sector downgrade.
- The trade is really a bet that the supply interruption persists. The April 2026 precedent is a
  Saudi pumping station repaired in three days, and Saudi has said it will not retaliate for now
  at Baghdad's request. Shorting a -20% group on a headline that can reverse in 72 hours is
  selling the tail, not the trend. Not published.

## [06:09 ET] REJECTED — index futures (/MES, /MNQ) — cannot price them today
- The Nasdaq-vs-S&P split overnight (NQ -1.2/-1.7% vs ES -0.5/-0.7%) is the most interesting
  thing on the screen and I am not going to trade it, because **every index source failed**:
  yahoo 429 on ^GSPC/^NDX/^RUT/^VIX, finnhub refuses index CFDs, stooq 404. I have no fetched
  /MES or /MNQ level, and `universe.md` prefers futures precisely for this kind of view.
- Setting a futures entry, stop and target off a remembered index level would be fabricating
  three numbers on a leveraged instrument. Recorded as a coverage gap instead.

## [06:17 ET] REJECTED — defense (LMT/NOC/GD/RTX/LHX/KTOS/AVAV/ITA) — and WHY matters
Every defense name is deeply de-rated during an active shooting war, which is the opposite of the
reflex. Closes 2026-09-11, `market_data.py history`:

| sym | last | % off 120d high | vs sma20 | vs sma50 |
| --- | --- | --- | --- | --- |
| KTOS | 46.69 | -45.9 | below | below |
| AVAV | 146.71 | -34.0 | below | below |
| LHX | 245.54 | -32.6 | below | below (120d low 244.76 — sitting ON it) |
| NOC | 518.97 | -26.8 | below | below |
| LMT | 524.19 | -17.8 | below | below |
| ITA | 219.01 | -14.7 | below | below |
| RTX | 197.68 | -12.9 | below | below |
| GD | 355.90 | -11.0 | below | below |

**The mechanism, and it is not a mispricing:** the Iran war is *consuming* the defense budget, not
expanding it. Hegseth put the war's cost at $37.5bn through end-September, and the Pentagon is
draining equipment and facility maintenance budgets and cancelling training to cover an operational
shortfall — O&M dollars burned on deployments and munitions expenditure are not procurement dollars
that become prime revenue.
- source: https://www.cnn.com/2026/05/27/politics/iran-war-spending-cancelled-trainings-delayed-maintenance
- source: https://www.washingtonpost.com/national-security/2026/07/21/pentagon-sinking-billions-into-iran-is-quickly-running-short-cash/
- source: https://breakingdefense.com/2026/09/what-options-does-the-pentagon-have-to-cover-its-mounting-fy26-operational-costs/

On top of that, **Pentagon funding hit a snag in Congress on 2026-09-13** — yesterday — with the war
unpopular going into the 2026-11-03 midterms and no serious legislative movement expected until
after them. source: https://www.washingtontimes.com/news/2026/sep/13/pentagon-funding-hits-snag-congress-returns-amid-iran-war-ahead/
Defense News had already called this in April: "US defense stocks see no Iran war lift after early
surge" — source: https://www.defensenews.com/news/your-military/2026/04/02/us-defense-stocks-see-no-iran-war-lift-after-early-surge/

- **No long.** The market has this right and the near-term news flow (funding snag, midterms) is against it.
- **No short either.** Same test the homebuilders and airlines failed: at -11% to -46% off the highs
  the move has happened. An LHX breakdown short below 244.76 needs a 2.0-ATR stop (11.20, → 256.20)
  and a 221.70 target to clear 2.0:1 — another 9.4% into fresh lows on a name already down a third.
- Recorded so a later run does not make the "war, therefore buy defense" mistake.

## [06:18 ET] PATTERN — today's tape has already made the obvious macro moves
Four separate sector shorts all failed the SAME test: homebuilders (-16/-19%), airlines (-17/-26%),
defense (-11/-46%), and to a degree gold. Each has the right mechanism and no reward left, because
the reward-to-risk floor only clears by targeting fresh multi-month lows. Meanwhile the obvious
longs — tankers — are pinned at their 120-day highs (TNK -0.08%, FRO -0.71%, DHT -1.26%).
**This is a tape that has repriced, not one that is repricing.** So today's report is deliberately
weighted to managing the twelve open positions — six of which carry no stop at all going into a
hiking FOMC — rather than to adding new directional risk. That is the honest shape of the day and
should be said in `data_quality_notes` rather than papered over with filler ideas.

## [06:22 ET] REJECTED — MET (MetLife) long_term — good company, fails the 2.5:1 floor on arithmetic
Researched properly as the long-term lane candidate, because a 5% 10-year is the best environment
for a life insurer's reinvestment yield in twenty years. The evidence is genuinely strong:
- Adjusted ROE **17%** in Q1 and Q2 2026, top of the company's 15-17% target range; adjusted BVPS
  $57.71 at Q2 2026 — source: https://www.metlife.com/about-us/newsroom/2026/august/metlife-announces-second-quarter-2026-results/
- Four straight earnings beats: +4.93% (Q2 26), +5.49% (Q1 26), +9.06% (Q4 25) — finnhub
- Analyst revisions **improving**; bullish share 70.8%, up 1.2pts; 17 buy/strong-buy vs 7 hold, zero sells
- Relative strength leading: +1.56% vs SPY 1m, +7.32% 3m, **+26.46% 6m**; also beating XLF on all three
- Last 97.14, above its 20-day (96.17) and 50-day (95.16), only 3.76% off the 120-day high

**Why it is not published.** MET has already re-rated — it is +41.2% over six months and sits 3.8%
off its high. Running the long-term floor honestly:
- Run-rate adjusted EPS ~$9.70 (Q1 2.42 + Q2 2.43 annualised) → 97.14 is ~10.0x
- A defensible target is 12x a modestly grown ~$10.50 = **$126** (MET's historical band is ~8-12x)
- A defensible bear case, if long rates round-trip and the multiple goes back to 8x on $9.00, is
  **$72-75** — consistent with where it actually traded six months ago (120-day low 67.33)
- Reward-to-risk from 97.14: (126 - 97.14) / (97.14 - 75) = 28.86 / 22.14 = **1.30:1**
- Even accumulating down at 93 it is only 1.83:1, against a **2.5 floor**
Getting to 2.5 needs a $140 target, which is 13.3x — a multiple MET has not held. That is precisely
the reverse-engineering `config/strategy.md` forbids, so the idea is rejected rather than stretched.
Insider flow is also mildly negative: zero open-market buys, one sale of $1,738,823 in six months.
**Worth revisiting on a drawdown into the mid-80s**, where the same target clears the floor easily.

## [06:25 ET] REJECTED — EQT long_term (US natgas / LNG) — thesis real, evidence points the wrong way
The idea: Hormuz closed since March plus both Saudi export routes down makes non-Gulf energy
structurally more valuable, and US gas is the marginal global LNG supply. EQT is the largest US
natgas producer, 20.8% off its 120-day high while crude rips — the laggard of the complex.
Why it does not publish:
- **Insider flow is clearly negative**: zero open-market buys against **6 sales totalling
  $6,408,457** in six months — finnhub. Contrast NKE's 4 buyers.
- **The most recent quarter MISSED**: Q2 2026 actual 0.39 vs 0.4041 estimate (-3.49%), breaking a
  run of +11.05%, +19.95%, +19.76% — finnhub
- **Six-month relative strength is bad**: -31.1% vs SPY, -29.6% vs XLE
- The lag has a fundamental reason rather than being a mispricing: Henry Hub is set by domestic
  storage and weather, not Brent, and UNG at -17.9% off its high confirms domestic gas is genuinely
  weak. The LNG linkage is real but slow, gated on export capacity.
- No dated catalyst, and I have **no fetched valuation** for EQT, so a `long_term` idea here would
  need a target number I cannot defend. Analyst revisions are the one positive (80% bullish, +4.1pts,
  24 buy/strong-buy vs 6 hold, zero sells) and that is not enough on its own.

## [06:26 ET] NO LONG-TERM IDEA TODAY — and that is a finding, not an omission
Both long-term candidates researched to a conclusion (MET, EQT) were rejected on their own
arithmetic rather than skipped for time. `config/strategy.md` says publish fewer rather than pad,
so today's report carries **zero `long_term` ideas** and the reason should be stated plainly in
`data_quality_notes`: after a 6-month run in which SPY is +14.8% and the leaders are at their highs,
the durable-mispricing lane is genuinely empty at these prices. Both names are worth revisiting on a
drawdown — MET into the mid-80s clears its floor easily.

## [06:26 ET] AWAITING-ENTRY REVIEW — three orders are stale and one is dangerous to leave working
From `prior_context.md`, 14 unfilled orders. Most are fine to leave. These are not:
- **`BTC` SELL @ 63,400 (published 2026-08-16)** and **`/MBTU6` SHORT @ 64,340 (2026-08-18)** —
  **CANCEL BOTH.** Bitcoin is 78,164 as of this morning (coingecko, live), 23% ABOVE the short
  trigger. These are month-old bearish orders on an asset that has gone the other way; leaving a
  short working 23% below the market is an order that can only fill in a crash, which is the worst
  time to be getting short. Note `/MBTU6` is also a September contract and near expiry.
- **`KXFEDDECISION-26SEP-H0` YES @ 47 (2026-09-03)** — that is the *no-change* outcome, and the
  market now prices a hike at 81-90%, i.e. hold at roughly 19%. The order is stale by 28 points.
- **`KXFEDDECISION-26SEP-H25` YES @ 32 (2026-08-22)** — the *hike* outcome, and this call was right:
  Kalshi had it at 81% on 2026-09-11. It never filled. **I cannot mark or re-price any of the three
  event positions today** because `market_data.py events` returns nothing usable (see data gaps), so
  no event contract is recommended this run despite it being the cleanest expression of the week.
- `IYR` SELL_SHORT @ 103.60 (2026-09-02) — leave working; a REIT short is more right at a 5% 10-year
  than it was when published. Not re-pitched only because rates already carry TLT and SPY, which is
  the 3-idea correlation cap.

## [06:29 ET] SELF-CHECK — recomputed every stop in ATRs FROM THE ENTRY, and caught one
Re-derived each stopped idea rather than trusting what I wrote the first time. Floors: 2.0 ATR for a
stock swing, 1.8 for an ETF.

| idea | entry | stop | risk | ATR14 | stop in ATR | floor | R:R | baseline 1/(1+R:R) | claimed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TLT short | 80.55 | 82.30 | 1.75 | 0.660 | 2.65 | 1.8 | 2.14 | 0.318 | 0.42 |
| SPY short | 773.00 | 783.50 | 10.50 | 5.599 | 1.88 | 1.8 | 2.19 | 0.313 | 0.45 |
| XLE | 63.90 | 61.50 | 2.40 | 1.209 | 1.98 | 1.8 | 2.33 | 0.300 | 0.44 |
| DVN | 49.60 | 46.90 | 2.70 | 1.177 | 2.29 | 2.0 | 2.19 | 0.314 | 0.50 |
| SVRA | 5.35 | 4.60 | 0.75 | 0.197 | 3.80 | 2.0 | 3.53 | 0.221 | 0.30 |
| CCJ | 94.00 | 88.50 | 5.50 | 3.763 | **1.46** | 2.0 | 4.36 | — | — |

**CCJ failed and has been re-captured with the stop at 86.00.** The error was measuring the stop
from the last price (96.68 - 88.50 = 8.18 = 2.17 ATR) instead of from the filled entry
(94.00 - 88.50 = 5.50 = 1.46 ATR). Since the position is already filled at 94.00, the entry is the
only number that can be used — it was bought at a price. Corrected: stop 86.00, risk 8.00 = 2.13 ATR,
R:R 3.00, baseline 0.25 against a claimed 0.30.
Note SPY at 1.88 ATR and XLE at 1.98 ATR clear their 1.8 ETF floor but are not comfortable; both are
disclosed rather than tightened, because tightening is the free way to flatter the ratio.

## [06:22 ET] RESEARCH COMPLETE
- **candidates: 11 distinct ideas** (12 lines — CCJ appears twice; the second, with the corrected
  86.00 stop, supersedes the first).
- **Shape of the day, and it is unusual — say this in `data_quality_notes`:**
  - **All 11 are `swing`. Zero `intraday`, zero `long_term`.** Not a quota failure: both long-term
    candidates (MET, EQT) were researched to a conclusion and rejected on their own arithmetic, and
    no intraday setup existed with the index feeds down.
  - **7 of 11 are position management, not new risk** — LCII, GLD, BCC, LULU, NKE are exits; SPY,
    DVN, SVRA and CCJ are holds/amendments. Only TLT (new short) and XLE (unfilled re-pitch) add
    exposure. That is deliberate: twelve positions were open, **six with no stop at all**, into a
    week with a hiking FOMC.
  - The tape has already made the obvious macro moves. Four sector shorts with correct mechanisms
    (homebuilders, airlines, defense, and gold) were rejected because the reward-to-risk only
    cleared by targeting fresh multi-month lows.
- **The regime changed and the book was on the wrong side of it.** The market prices a 25bp Fed
  HIKE on 2026-09-16 at 81-90%, the 10-year is ~5.00%, and 4-5% of global oil supply is offline.
  The open book held three rate-sensitive consumer/housing longs (LCII, BCC, LULU/NKE) taken before
  that. Cutting the correlation is the single most valuable thing in today's report.
- **Coverage gaps:**
  - **No index data at all.** yahoo returned HTTP 429 on ^GSPC, ^NDX, ^DJI, ^RUT and ^VIX for the
    whole run; finnhub refuses index CFDs; stooq 404s them. No SPX/VIX/DXY/WTI/10Y *quote*. Rates
    came from FRED (2026-09-10/11 vintage) and index levels from sourced news, not fetched feeds.
    **This is why no `/MES` or `/MNQ` idea was published**, despite the NQ-vs-ES split overnight
    being the most interesting thing on the screen — `universe.md` prefers futures for exactly that
    view and I had no fetched contract price to set a stop against.
  - **No event contracts.** `market_data.py events` returned count=0 for FEDDECISION, FOMC, "Fed
    hike", KXFED, "Fed funds", "interest rate", CPI, recession, rate, oil, Brent and gas, and
    returned unrelated sports cross-category markets for "Fed". The three open KXFEDDECISION
    positions could not be marked and no event idea was published, in a week where a Fed contract
    would have been the cleanest expression available.
  - `market_data.py implied TLT` — yahoo-options HTTP 401. No options-implied move for any idea.
  - `market_data.py short TLT` — nasdaq read timeout. **No short-interest data fetched for any
    name this run**, so no idea cites a crowding read from that source.
  - `history` failed for CTRA and SWN (natgas screen).
  - NKE's next earnings date is NOT on the fetched 12-day calendar and is unconfirmed; SVRA has no
    verified dated catalyst. Both are disclosed in the ideas themselves.
- **Sources that failed:** yahoo chart API (429, all indices), yahoo options API (401),
  finnhub index CFDs (subscription), stooq (404 on indices), nasdaq api (timeout on short
  interest; CTRA/SWN history), Kalshi via `events` (no usable macro markets).
- **Sources that worked:** FRED (rates, CPI, unemployment), finnhub (equity/ETF quotes, insiders,
  analysts, earnings calendar), nasdaq historical (all levels and ATRs), coingecko (crypto),
  federalreserve.gov (FOMC calendar, primary), BLS (CPI/PPI, primary), Census (housing starts).
- **One process note for the next run:** my sense of elapsed time was badly wrong — I believed it
  was 06:40 when `date` said 06:09. Every heading above the 06:09 correction block is an estimate.
  Call `date` for timestamps; do not estimate them.

## [06:23 ET] VERIFIED INDEPENDENTLY — the hike odds four ideas rest on
The 81-90% hike figure cited in the TLT, SPY, GLD and BCC ideas came to me second-hand, and four
recommendations lean on it, so I checked it directly rather than trusting the relay:
- **CME FedWatch puts a 25bp hike at 85.6% for the 2026-09-16 meeting**, up from 48.4% on 2026-08-11.
  source: https://finance.yahoo.com/economy/policy/articles/just-5-days-next-fomc-145150594.html
- Corroborating the path: ~56% earlier in August, 57%, then 66% on 2026-08-31 (Forbes), then 85.6%.
  source: https://www.forbes.com/sites/digital-assets/2026/08/31/cme-fedwatch-provides-a-66-chance-fed-will-hike-rates-in-september-/
- FOMC date and SEP status confirmed at the primary source, the Fed's own calendar: meeting
  2026-09-15/16, one of the four 2026 SEP meetings.
  source: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
**The 81-90% range used in the ideas holds.** 85.6% sits inside it.

### One factual conflict I could not resolve — flagged, not hidden
On August CPI (released 2026-09-11), my two sources disagree on the *surprise*:
- One reports core +0.3% m/m as an upside surprise
- This search reports headline 3.4% y/y and core +0.3% m/m **matched expectations**, offering
  "little evidence that inflation is moving cleanly toward the Fed's 2% target"
The *levels* agree (3.4% y/y headline, +0.3% m/m core) and no idea depends on the surprise, only on
the level and the resulting hike odds. But it does shift the attribution: the rate move is better
explained by the oil supply shock plus the hike repricing than by a CPI beat. **No recommendation
claims a CPI surprise.** Primary source for the levels: https://www.bls.gov/news.release/cpi.nr0.htm

## [06:27 ET] REJECTED — the AI-complex short — the de-rating already happened, except in NVDA
Revisited the overnight AI shock (SoftBank -11/-13% on OpenAI ruling out a 2026 IPO; SK Hynix and
Samsung -3.5%+; NQ futures down roughly double ES) using single names, since I can price those from
nasdaq historical even with every index feed down. Closes 2026-09-11:

| sym | last | % off 120d high | vs sma20 | vs sma50 |
| --- | --- | --- | --- | --- |
| ARM | 264.79 | -41.5 | above | below |
| VRT | 257.06 | -32.3 | below | below |
| AVGO | 361.99 | -26.9 | below | below |
| MU | 975.26 | -22.3 | above | above |
| SMCI | 40.10 | -22.0 | above | above |
| **NVDA** | **218.29** | **-7.7** | below | above |

The finding: **the AI trade already broke over the summer** — four of six are 22-42% off their highs.
Monday's shock is landing on a group that has already halved its multiple, which is the same reason
the homebuilder, airline and defense shorts were rejected. The exception is NVDA at -7.7%, still
above its 50-day: the last one standing.

**Why NVDA is still not published as a short**, despite being the only one with room:
- The reward-to-risk lands on **exactly 2.00** and only there. Entry 218.00 with an honest 2.0-ATR
  stop (ATR 7.69 → 15.39, so stop 233.50, risk 15.50 = 2.01 ATR) needs a 187.00 target for 2.00:1.
  An idea that clears its floor to the second decimal and no further has failed the floor in spirit —
  `config/strategy.md` is explicit that the floor rejects ideas rather than calibrating them.
- **There is no NVDA-specific catalyst.** The news is about SoftBank's stake and OpenAI's IPO
  timing, not about NVDA's demand, and NVDA does not appear on the 12-day earnings calendar I
  fetched. Shorting the strongest name in a group on a headline about a different company is a
  correlation bet dressed as a stock idea.
- It would be a **third** equity-beta short alongside SPY and TLT, which is the correlation cap.
- MU is the sharper-looking short on paper (-22.3% off a high that was itself a 4x from 311.49 to
  1255.00 in 120 days) and is rejected for the opposite reason: a 4.53% ATR on a name that has
  tripled cuts both ways, and there is no fetched short-interest data this run to tell me how
  crowded the trade already is. That gap matters most precisely here.

## [06:26 ET] SMALL-CAP SWEEP — names with a dated catalyst this week. Nothing publishable.
`config/universe.md` asks these to be hunted deliberately, so I screened the small caps on the
fetched earnings calendar for the next 8 sessions. Liquidity check FIRST, per the rule:

| sym | last | avg $ vol/day | % off high | earnings | verdict |
| --- | --- | --- | --- | --- | --- |
| HAIN | 0.6194 | **$458,016** | -35.9 | 2026-09-14 bmo | **EXCLUDED** — under the $500K floor AND under $1 |
| VRA | 3.14 | **$329,675** | -28.5 | 2026-09-15 bmo | **EXCLUDED** — under the $500K floor |
| EPM | 3.72 | $2,081,995 | -25.5 | 2026-09-15 amc | rejected, see below |
| APOG | 37.88 | $6,907,873 | -25.6 | 2026-09-22 | rejected |
| PLAY | 8.14 | $12,816,984 | -45.8 | 2026-09-14 amc | rejected |
| CBRL | 49.48 | $37,686,939 | -17.9 | 2026-09-14 bmo | rejected |

- **HAIN and VRA are excluded by the floors, not by judgement** — both under $500K average daily
  dollar volume, and HAIN also trades under $1. The floor is about exit, and it did its job.
- **EPM** looked like the best fit on paper — a small-cap oil producer with a dated print inside an
  oil supply shock. It is rejected on a timing point that matters: EPM's June-ending fiscal quarter
  **ended before the 2026-09-10/11 pipeline strike**, so the print is backward-looking and says
  nothing about the price environment that is the actual thesis. A catalyst that cannot speak to the
  thesis is not a catalyst. It is also largely non-operated/royalty with hedges, so pass-through is
  unclear and I did not have time to read the filings to establish it.
- **CBRL** reports 2026-09-14 bmo — before this report can be read and acted on. Not tradeable as
  published.
- **PLAY** sits on its 120-day low (7.94) at 8.14, -45.8% off its high, with a **6.78% ATR**, and
  reports tonight. Entering a broken discretionary small cap the afternoon of a binary print is a
  coin flip, not an edge.
- **APOG** is architectural glass — construction demand, i.e. the exact factor a 5% 10-year is
  destroying — and is already 25.6% off its high and below both averages. Same rejection as the
  homebuilders: correct mechanism, no reward left.

## [06:27 ET] RESEARCH COMPLETE (supersedes the 06:22 block — same conclusions, wider coverage)
- **candidates: 11 distinct ideas**, 12 lines (CCJ twice; the second, with the corrected 86.00 stop,
  supersedes the first). All validate: every venue is a Robinhood venue, and no conviction score
  exceeds what its distinct evidence kinds support.
- Everything in the 06:22 block stands. Added since: the small-cap sweep above, the AI-complex
  rejection, and independent verification of the hike odds (**CME FedWatch 85.6%** for 2026-09-16,
  which confirms the 81-90% range that TLT, SPY, GLD and BCC rest on).
- **Final shape: 11 swing ideas, 0 intraday, 0 long_term; 7 of the 11 are position management.**
  Two new-risk ideas only — TLT short (new) and XLE (unchanged unfilled level). Six sector shorts
  with correct mechanisms were rejected for having no reward left (homebuilders, airlines, defense,
  AI complex, APOG, and gold as a short rather than the exit it became), and both long-term
  candidates were rejected on their own arithmetic.
- The one-line version for `data_quality_notes`: **the regime flipped to a hiking Fed with an oil
  supply shock, the tape had already repriced nearly everything by Friday, and the book was holding
  three correlated rate-sensitive consumer longs with no stops — so today's value is in cutting
  that, not in adding new directional risk.**
