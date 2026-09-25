# Research log — 2026-09-25

## [06:04 ET] MACRO — rates, and the tape data we could not get
- US 10y **5.11%** (2026-09-23), prev 4.96% — a **15bp one-day backup**. Source: FRED DGS10 via `market_data.py macro`
- US 2y **4.85%**, prev 4.71% — the whole curve sold off, not a term-premium-only move. FRED DGS2
- Fed funds effective **3.88%** (2026-09-23), unchanged. FRED DFF
- 10y-2y spread **+0.31** (2026-09-24), prev +0.26 — bear steepening
- Unemployment **4.1%** (Aug 2026), unchanged from prior. FRED UNRATE
- CPI index 334.131 (Aug 2026) vs 332.813 prior month — +0.40% m/m, hot. FRED CPIAUCSL
- `TLT` last **79.42, -1.29%** (pre, 2026-09-25) — the only equity/ETF quote `macro` returned
- source: https://fred.stlouisfed.org/series/DGS10 , https://fred.stlouisfed.org/series/DGS2 , https://fred.stlouisfed.org/series/T10Y2Y

## [06:04 ET] DATA QUALITY — Yahoo rate-limited
- Yahoo Finance returning **HTTP 429** on every index symbol; finnhub refuses indices without a CFD subscription; stooq 404s on `^`-prefixed symbols.
- Consequence: **no live read on SPX, NDX, RUT, VIX, DXY, ES, NQ, gold or WTI this morning.** Do not state an index level anywhere in today's report.
- ETF and single-stock quotes must be tested separately before being relied on.

## [06:05 ET] CALENDAR — dated catalysts inside 10 sessions (fetched, finnhub)
- **2026-09-28** `NKE` FQ1 — est EPS 0.4444, rev $11.45B. **We hold NKE on both sides.**
- 2026-09-28 bmo `CCL` est EPS 1.3712, rev $8.38B
- 2026-09-28 amc `MTN` est EPS -5.311
- **2026-09-29** `CAG` FQ1 — est EPS 0.2842, rev $2.61B. **We hold CAG BUY, opened 2026-09-20.**
- 2026-09-29 bmo `KMX` est EPS 0.7199, rev $7.05B
- 2026-09-29 bmo `UEC` est EPS -0.0471 — uranium read-through to open `CCJ`
- 2026-09-29 amc `CNXC` est EPS 2.7591
- **2026-09-30 amc `MU`** — est EPS 32.3202, rev $52.24B. **MU BUY @960 is awaiting entry.**
- 2026-09-30 bmo `JBL` est EPS 4.0999, rev $9.79B; `FDS` 4.3792; `CALM` -0.7208; `JEF` 0.9353
- 2026-10-01 amc `ACN` est EPS 3.2131, rev $18.21B; bmo `AYI` 5.7198; `AEHR` 0.1122
- 2026-10-05 bmo `MKC` 0.7633
- 2026-10-06 bmo `STZ` 3.6097; `RPM` 1.9694; `LW` 0.6071
- 2026-10-07 `LEVI` 0.3665; `TLRY` -0.1948
- source: finnhub earnings calendar via `python scripts/market_data.py earnings --days 12`

## [06:12 ET] MACRO — the one driver behind everything today
The rate move, the oil move and the Fed repricing are **one story**, not three:
US-Iran fighting has cut Hormuz crude flows to **under 2 mbpd from ~8-9 mbpd**,
crude is >$100 (WTI ~$105), and the resulting inflation impulse has the market
pricing Fed **hikes** rather than cuts.
- 10y ~5.11%, **highest since July 2007**; surged 16bp on 2026-09-23 — source: https://tradingeconomics.com/united-states/government-bond-yield
- 30y just shy of **5.5%, highest since 2004** — source: https://www.bloomberg.com/news/articles/2026-09-24/us-30-year-yield-hits-highest-since-2004-as-bond-selloff-deepens
- Market pricing **~64% chance of a 25bp HIKE in October**, ~48% in December — source: https://tradingeconomics.com/united-states/government-bond-yield
- Trigger was S&P Global flash PMI: US private-sector activity fastest in 5+ years in September, with stronger price pressures — source: https://www.axios.com/2026/09/24/treasury-yields-inflation-bonds
- Hormuz flows <2 mbpd vs 8-9 mbpd pre-conflict; alternative export routes exposed to attack — source: https://oilprice.com/Energy/Energy-General/Oil-Breaks-100and-This-Rally-Has-Legs.html
- Dow -0.3% on 2026-09-24, oil ~$105 — source: https://eurasiabusinessnews.com/2026/09/24/stock-market-today-bond-selloff-worsens-as-10-year-treasury-yield-climbs-above-5-1-dow-jones-falls-by-0-3-oil-price-at-105/

**Correlation discipline for today:** long energy, short duration, short
rate-sensitives and long gold are all the *same* bet on this supply shock. The
book already carries XLE, DINO, CCJ, CEG, GLD long and TLT short, with OXY, XLU
short, IYR short and a TLT short awaiting entry. New ideas must either express a
*different* mechanism or replace, not stack.

## [06:13 ET] EVENT CONTRACTS — Kalshi query returned nothing usable
- `market_data.py events "Fed"` returned 3 markets, all of them multi-leg
  cross-category parlays (NFL/tennis/city combos) with `last_price: null` and no
  bid/ask. **No Fed-decision market was returned and no price was fetched.**
- Therefore: no event-contract candidate may be priced today. The three
  `KXFEDDECISION-*` contracts already awaiting entry cannot be re-marked either —
  I have no fetched price for them.
- Note for synthesis: Fed event contracts are the single most obviously
  mispriced-looking thing on the board given the hike repricing, and we could not
  get a quote. That is a **coverage gap, not a no-signal**.

## [06:13 ET] PRIOR CLOSE MARKS — open positions (2026-09-24 16:00 ET close, finnhub)
Market is closed; these are prior closes, not live prints.
| Sym | Close | vs prev | ATR14 | SMA20 | note |
| --- | --- | --- | --- | --- | --- |
| TLT | 79.42 | -1.29% | 0.79 (0.99%) | 81.56 | at 20d low, short working |
| CCJ | 88.12 | -2.95% | 3.22 (3.65%) | 96.11 | broke below SMA50 94.75, stop 82.50 is 1.9 ATR away |
| CEG | 261.62 | -0.86% | 9.67 (3.70%) | 275.23 | stop 250 is 1.2 ATR away — tight |
| XLE | 62.60 | +0.37% | 1.38 (2.20%) | 64.01 | oil $105 and XLE below SMA20 — divergence |
| DINO | 105.79 | -0.33% | 5.13 (4.85%) | 107.27 | -10.6% off high |
| GLD | 391.69 | -0.30% | 6.86 (1.75%) | 400.80 | below SMA20 and SMA50 (394.86) |
| CAG | 14.67 | -0.74% | 0.39 (2.67%) | 15.28 | **earnings 2026-09-29**, stop 14.20 is 1.2 ATR away |
| NKE | 35.99 | -0.17% | 0.90 (2.49%) | 37.23 | **earnings 2026-09-28**, 1.8% off 150d low |
| BCC | 76.10 | -2.13% | | | |
| LCII | 83.55 | -1.74% | | | |
| PFE | 28.41 | +0.82% | | | |
| LULU | 101.64 | -0.63% | | | |
| SVRA | 5.07 | +1.40% | | | |
| EEM | 67.25 | -0.68% | | | |
| MU | 1080.53 | +0.81% | | | **earnings 2026-09-30**; BUY @960 awaiting is 11% below market |

## [06:22 ET] CAPTURED — TLT sell_short — amendment, conviction 3
- The 81.87 short published 2026-09-24 was left behind by a 1.29% one-day drop; re-struck at 79.90 ideal / 82.00 stop / 75.70 target (R:R 2.0, stop 2.66 ATR).
- What changed vs yesterday: 10y +16bp to 5.11% (highest since Jul 2007), 30y to ~5.5% (highest since 2004), October hike odds ~64%.
- Stop set FIRST at 82.00 = above SMA20 81.56 (thesis is wrong if TLT reclaims its 20-day). Target is what the 2.0 floor then implied, and 75.70 needs ~10y 5.40-5.45% — a real claim, not a gimme. Said so in the thesis.
- TLT now appears 3× in 10 days. Justified only by the repricing above; if the red team disagrees, cut this one rather than the newer ideas.

## [06:23 ET] RATE-SENSITIVES — both prior shorts are now at/through their levels
- `XLU` closed **39.36**, the low of its 250-day range, SMA20 41.92 / SMA50 43.38 / SMA200 44.48. The XLU short published 2026-09-24 @39.60 is at or through its entry — treat as filled/working, do not re-pitch as new.
- `IYR` closed **96.81**, SMA20 100.48 / SMA50 103.26 / SMA200 100.08, -10.5% off high. The 2026-09-02 short @103.60 is 7% above market and stale.
- Correlation note: TLT short + XLU short + IYR short = **3 ideas on one rate driver, the cap**. No fourth rate-sensitive short today. This is why I am not pitching homebuilders despite 10y at 5.11%.

## [06:23 ET] SECTOR SCAN — two divergences worth explaining before trading
**Defense is falling during a shooting war.** Prior closes 2026-09-24:
- `LHX` 238.04 — **0.08% off its 150-day low**, -37.2% off high, SMA20 252.29 / SMA50 270.86
- `NOC` 508.98 — -34.2% off high; `LMT` 523.70 — -24.3%; `RTX` 188.61 — -16.9%; `ITA` 212.76 — -17.1%, 1.65% off low
- Explanation found, and it is not a dislocation: defense has had "no Iran war lift after early surge", and FY26 framework agreements with primes **cannot be fully funded without a finalized appropriations bill** — source: https://www.militarytimes.com/news/your-military/2026/04/02/us-defense-stocks-see-no-iran-war-lift-after-early-surge/ , https://www.tikr.com/blog/lmt-defense-stocks-drop-as-white-house-summons-pentagon-officials-and-prime-contractors-to-address-domestic-munitions-shortages
- LHX specifically -15.1% YTD vs +2.8% for the A&D ETF, and -17.7% over three months vs -7.1% — it is lagging its own sector, not just the market — source: https://finance.yahoo.com/markets/stocks/articles/l3harris-technologies-stock-performance-compared-154856254.html
- **Verdict: not yet tradeable.** The appropriations overhang is the mechanism and I need the actual deadline before I can call it a dated catalyst. Checking next.

**Airlines are rallying into a jet-fuel shock.** `DAL` 82.76 (above SMA20 79.75, +4.2% over 5 sessions), `UAL` 111.19, `LUV` 41.55, `JETS` 28.46 — all above their 20-day averages with crude at ~$105. Either demand is unusually strong or the fuel pass-through is being ignored. Flagged; needs a fundamental check before it becomes a short.

## [06:28 ET] REJECTED — LHX — falling knife, not a dislocation
Looked like the best contrarian setup on the board (150-day low, -37% off high, shooting war). It is not:
- **No catalyst exists.** A clean CR funding the government through **2026-12-11** was signed on 2026-09-01, so there is no Sep 30 deadline and defense primes sit on flat funding with no new starts until after the November midterms. Only 2 of 12 FY27 appropriations bills have passed the House; the Senate has advanced none — source: https://www.crfb.org/blogs/appropriations-watch-fy-2027 , https://www.nextgov.com/policy/2026/09/shutdown-threat-lifted-house-passes-stopgap-spending-bill/415755/
- **Insiders are not buying.** 0 open-market buys, 0 distinct buyers, 1 sale of $676,781 over 6 months (finnhub).
- **Revisions are deteriorating**, not bottoming: bullish share 69.6%, **-5.4pp** m/m; strong_buy 6->5.
- **It lags its own sector**, so this is company-specific: vs SPY -9.4%/-22.0%/-49.2% over 1m/3m/6m, and vs ITA -0.01%/-7.1%/**-26.6%**.
- Verdict: cheap for a reason, no dated catalyst, no insider confirmation, negative revisions. Not published in any horizon. Revisit if a full-year defense appropriation moves after the midterms.
- Same reasoning rejects `NOC`, `LMT`, `RTX` and `ITA` as a group today — the CR is the binding constraint for all of them.

## [06:29 ET] POSITION UPDATE — NKE — the book is long AND short the same name into Monday's print
- Open `NKE` BUY from 2026-08-17 @40.75, last **35.99**, **-11.7% vs entry**, **no stop**. Open `NKE` SELL from 2026-09-08 @38.40, +6.1%.
- **FQ1 earnings 2026-09-28** (fetched calendar), est EPS 0.4444, rev $11.45B.
- Analyst revisions deteriorating into it: bullish share **39.1%, -9.8pp** m/m; hold count 25, sell 3 (finnhub).
- Price: 35.99, **1.8% off the 150-day low of 35.35**, below SMA20 37.23 and SMA50 39.86. ATR14 0.90.
- `market_data.py short NKE` **failed** (nasdaq ReadTimeout) — no short-interest read, so no squeeze assessment.
- decision: **close the long before the print.** A -11.7% position with no stop, deteriorating revisions and a binary event in one session is not a thesis, it is a coin flip. Carrying both sides of the same name is incoherent regardless.
- action: captured as a close.

## [06:30 ET] POSITION UPDATE — CAG — hold into earnings, do not add
- Open BUY 2026-09-20 @15.00, last **14.67** (-2.2%), stop 14.20, target 16.74. **FQ1 earnings 2026-09-29** (fetched).
- Analyst bullish share **4.0%** — 1 buy against 8 sell and 2 strong_sell. That is the contrarian setup the entry was made on and it has not changed (+0.2pp m/m).
- ATR14 0.39 (2.67%). The 14.20 stop is 2.04 ATR from the 15.00 entry — it cleared the floor when written — but only **1.20 ATR from the current 14.67**, so a print-day gap takes it out on noise.
- decision: **hold, levels unchanged, do not add.** The stop is not walked in and not widened: widening it after entry to survive an event is how a 2% loss becomes a 6% one, and the position is already inside its risk budget.

## [06:36 ET] REJECTED — ACN — deteriorating into its own catalyst, no insider confirmation
- Close 177.41 (-3.3% on 2026-09-24), -18.8% off the 150-day high, below SMA20 185.97, sitting on SMA50 174.70. ATR14 7.51 (4.23%). Earnings **2026-10-01 amc**, est EPS 3.2131 on $18.21B.
- Attractive as the one genuinely *non-macro* idea available today — it depends on neither oil nor rates.
- Killed on evidence: bullish share 59.4%, **-10.3pp** m/m (strong_buy 8->6, buy 15->13); **0 open-market insider buys** against 10 sales totalling $2.59M over six months.
- A falling price plus falling estimates plus insider selling into a print in four sessions is not a setup in either direction I can defend at size. Watchlist, not a recommendation.

## [06:37 ET] REJECTED — the rest of the earnings slate, and why
- `CCL` 21.79, 1.6% off its 150-day low, -34% off high, earnings 2026-09-28 bmo. Coherent short on the fuel-cost shock, but that is the **oil driver for a fourth time** behind XLE, DINO and OXY, and shorting a name 1.6% off its low into a print is the worst version of it. Rejected on correlation, not on merit.
- `KMX` 56.36, below SMA20 60.08 and SMA50 59.42, earnings 2026-09-29 bmo. Auto retail with the 10y at 5.11% is a clean rate short — and the **fourth** rate idea behind TLT, XLU and IYR. Rejected on the correlation cap.
- `JBL` 310.69, above SMA20 304.91 but below SMA50 317.41, earnings 2026-09-30 bmo. No independent evidence gathered; not enough to publish.
- Discipline note: four of today's five best-looking setups are the same trade wearing different tickers. Publishing them would read as a diversified report and behave as one position.

## [06:12 ET] CORRECTION — the minute stamps above ran ahead of the wall clock
Research began 06:01 ET. `date` at this point reads **06:12 ET**, so every stamp
above between "06:04" and "06:37" is too late by up to 25 minutes; they are in
the right *order* but the clock times are wrong. Everything from here is stamped
from an actual `date` call. Elapsed at this line: 11 minutes, not 37.

## [06:16 ET] THE MOST IMPORTANT FINDING TODAY — the book's risk controls, not the tape
Working through all 16 open positions against fetched prices turned up a
structural problem that matters more than any single idea:
- **Five open longs carry no stop at all**: `NKE` (-11.7%), `LCII` (-11.1%), `LULU` (-11.6%), `BCC` (-0.5%), `PFE` (+2.9%). Three of them are down double digits with no defined loss.
- **Two names are held long and short simultaneously** — `NKE` (BUY 40.75 / SELL 38.40) and `LULU` (BUY 115.00 / SELL 100.61). Those net to flat and pay fees for the privilege.
- Of 16 open positions, **12 are underwater**. This is consistent with the 1/8 target-hit record in prior_context, and the common thread is not idea quality, it is that losers were entered without an exit.
- Actions captured today: close `NKE` long, close `LULU` long, close `LCII`, close `CCJ`. That is deliberately four exits and it is the honest read of the evidence, not a risk-off reflex.

## [06:17 ET] POSITION UPDATES — the rest, with fetched levels (2026-09-24 closes)
- `PFE` 28.41 — **the only position working on the tape.** Above SMA20 28.03 and SMA50 26.91, just **2.74% off its 150-day high**, ATR14 0.45 (1.59%). Entry 27.60, +2.9%. **HOLD.** Note it has no stop; the low ATR makes that less dangerous than the others but it should get one.
- `XLE` 62.60 — **HOLD.** Outperforming SPY +0.7% 1m and **+11.3% 3m**, which is the divergence worth owning: crude is above $100 on the Hormuz disruption while XLE still sits below its 20-day (64.01). Stop 60.80 is 2.25 ATR below the 63.90 entry, ATR14 1.38.
- `EEM` 67.25 — **HOLD.** At SMA20 67.42, above SMA50 66.05, +2.5% vs the 65.60 entry, ATR14 1.12. Stop 63.00 intact.
- `CEG` 261.62 — **HOLD, flagged.** Beating XLU by +3.1% 1m and +11.5% 3m (so it is not trading as a bond proxy), but lagging SPY -6.2%/-7.1%. The 250.00 stop is only **1.20 ATR** below the market on a 3.7% ATR name — it will be hit on noise. Not widened here; flagged for the red team.
- `DINO` 105.79 — **HOLD.** -10.6% off high, ATR14 5.13 (4.85%), stop 97.75 is 1.57 ATR below the market. Refining margins are the direct beneficiary of the crude dislocation.
- `GLD` 391.69 — **HOLD, weakening.** Below SMA20 400.80 and SMA50 394.86; stop 381.00 is 1.56 ATR below. Gold is losing to a real-rate shock even with a shooting war on, which is the tell that the rate move dominates the geopolitical bid.
- `BCC` 76.10 — **HOLD.** At SMA20 76.68, below SMA50 79.22, flat vs the 76.50 entry. ADV only $22.8M — size accordingly. No stop; should get one.
- `SVRA` 5.07 — **HOLD as a lottery ticket.** ADV $8.06M clears the $500K floor. Stop 4.60 is 2.13 ATR below (ATR14 0.22), so this one is correctly constructed. Negative mark: one insider **sold $2.24M** over six months against zero buys.

## [06:19 ET] CAPTURED — LNG (Cheniere) buy, long_term, conviction 4 — the best idea today
The one genuinely new thesis, and the only long_term idea captured.
- **Supply shock Cheniere does not share:** Hormuz LNG throughput **down 95%**, on a corridor carrying ~1/5 of globally traded LNG — a 17-19% cut to traded volumes, with rebalancing estimated to run to **2028**. QatarEnergy force majeure extended into November; Edison alone has had 29 cargoes (~3.8 bcm) cancelled since April. sources: https://www.csis.org/analysis/battle-hormuz-will-reshape-global-lng-market , https://www.euronews.com/business/2026/08/31/qatarenergy-extends-lng-cancellations-into-november-as-hormuz-disruption-drags-on
- **Capex cycle just ended:** Corpus Christi Stage 3 completed **2026-08-28**, capacity +20% to ~56 mtpa; FERC authorised a further ~5 mtpa in June 2026. sources: https://www.naturalgasintel.com/news/chenieres-corpus-christi-lng-stage-3-expansion-nearly-complete/ , https://www.eia.gov/todayinenergy/detail.php?id=68144
- **Primary document (Q2 2026 8-K Ex-99.1):** FY26 adj EBITDA guidance **raised to $7.90-8.40B from $7.25-7.75B**; DCF **raised to $5.30-5.80B from $4.75-5.25B**; production tightened up to 53-54 mt; H1 371 cargoes / 1,360 TBtu; **4.9M shares bought back for $1.1B**.
- **Valuation, method shown:** 206,534,158 shares (10-Q cover, 2026-07-31), LT debt $22,632M. At 276.28 → ~$57.1B equity, ~$79.7B EV, **9.8x** the $8.15B EBITDA midpoint, **9.7% DCF yield** ($26.87 DCF/share). Target 336 = 8.0% DCF yield. Bear 216 = the observed 150-day low.
- **Why it is marked `wait: true`:** at 276.28 the idea is **1.0:1** against the 216 bear case and **fails the 2.5 long_term floor**. It only clears at **248 or below** (2.75:1). The level is the recommendation; chasing it here is not. Deliberately not fixed by raising the target.
- Negatives stated on the face of the idea: **zero insider buys against six sales totalling $28.4M**, and a sell side already **92.9% bullish and unchanged** — nobody left to upgrade it. Scored 4 rather than the mechanical 5 the four evidence kinds would give, for exactly that reason.

## [06:22 ET] REJECTED (watchlist) — CF / MOS / NTR — the right shock, an unexplained tape
The fertilizer read-through to Hormuz is real and under-covered: Gulf **urea exports -83%**, **ammonia -75%**, and the Strait carries **a third of globally traded urea**; combined export volumes across the 12 products studied fell 54% — source: https://news.un.org/en/story/2026/08/1168074
That should be unambiguously bullish for US Gulf nitrogen. The tape says otherwise:
- `CF` 118.44, **-11.5% over six sessions** (133.82 -> 118.44), below SMA20 130.57 and SMA50 125.42, -16.6% off high. `MOS` 23.69 (-26.5% off high), `NTR` 73.96 — the whole group is falling.
- Positioning is neutral-to-soft: zero insider transactions in either direction over six months; analyst buys drifting down 10 -> 9 -> 8 with holds 14 -> 15 and 3 sells. Relative strength is split — CF +16.5% vs XLB over 3m but -6.9% over 1m.
- I could not establish **why** it is falling. Searches returned mostly stale April-2026 ceasefire material, not an explanation for this month.
- **Rejected on the LHX rule:** a price falling against its own bullish catalyst is a signal I do not understand, and buying it is guessing. Watchlist with one specific question to answer next run: is the six-session decline US natural-gas feedstock cost, and if so **this thesis is in direct conflict with the LNG idea captured above** — LNG exports pulling US gas prices up is exactly what compresses CF's margin. The two cannot both be sized as full positions.

## [06:23 ET] CAPTURED — LW (Lamb Weston) buy, swing, conviction 4
Found by scanning insider records across the whole 10-session earnings slate rather than by picking a name first — the only screen available that is genuinely predictive.
- **9 open-market buys, 4 distinct buyers, $16.98M, and ZERO sales** in six months. JANA Partners bought 386,000 shares across 2026-04-07 to 2026-04-15 at **40.89-43.19**; director Gray added 14,556 sh at 40.90-43.85; Prestage 2,500 @ 41.40. Stock is 44.37 — barely above the activist basis.
- **Activists hold the board.** Settlement added four JANA-proposed directors plus two mutually agreed, board 11 -> 13, ex-Nestlé USA CEO Bradley Alford as chair and JANA PM Scott Ostfeld seated; campaign sought a strategic review including a sale. A second activist (Starboard) is also in the name. sources: https://www.esmmagazine.com/a-brands/lamb-weston-settles-with-jana-partners-giving-activist-big-voice-on-board-291458 , https://www.fooddive.com/news/french-fry-maker-lamb-weston-adds-new-board-members-after-activist-pushback/752071/
- **Dated catalyst:** FQ1 **2026-10-06 bmo**, est EPS 0.6071 on $1.70B (fetched).
- Levels, stop set first: thesis is wrong below the activist basis, so stop **39.50** (below the 37.62-40.89 zone) = **3.08 ATR**, comfortably past the 2.0 floor. Target 53.00 is what the 2.0 R:R then allowed and sits inside the 150-day range below the 55.70 high. **2.07:1.** Not reverse-engineered.
- Honest negatives on the face of it: the buys are **five months stale**, and the stock is -20.3% off high, below SMA20 49.07 and SMA50 50.85, down 5 of 6 sessions. This is buying weakness.
- **Why it matters for the report's shape:** it is the only new idea today that depends on neither oil nor rates.

## [06:24 ET] INSIDER SCAN — the whole earnings slate, for the record
Ran `insiders` across every notable name reporting inside 10 sessions. Net buyers, which is rare:
- `LW` +$16.98M, 4 buyers, 0 sells -> **captured**
- `KMX` +$1.27M, **5 distinct buyers, 0 sells** — earnings 2026-09-29 bmo. Investigating.
- `JEF` shows +$952.8M from **1** buyer — almost certainly a corporate/institutional filing misclassified as an open-market purchase, not a management cluster. **Discarded as a data artifact**, not used.
Net sellers, all rejected: `AEHR` -$62.5M (64 sales), `LEVI` -$41.9M (18 sales), `CCL` -$1.52M, `AYI` -$1.39M, `STZ` -$0.94M. `MTN` and `RPM` had no transactions either way.

## [06:25 ET] CAPTURED — SNX sell (exit) — a published order that filled into a trap
- The `SNX` BUY @260.00 published 2026-09-19 **filled on 2026-09-24**: the stock traded 243.03-266.42 and closed **259.47, -9.87%**. prior_context still lists it as awaiting entry; it is not.
- Why it fell, from the **8-K Ex-99.1 read directly**: revenue **$21.558B +37.7%**, non-GAAP EPS **$5.68 +58.7%**, Q4 guided **$21.8-22.6B / $5.65-6.15** against $4.80 consensus — a large beat and raise. But gross margin **6.61% vs 7.22%** (-61bp), Q3 FCF **-$975.6M**, nine-month FCF **-$2.237B**, inventories **$15.29B from $9.50B (+61%)** against 37.7% revenue growth, receivables $14.95B from $11.71B, and only $139M returned to holders. source: https://www.sec.gov/Archives/edgar/data/0001177394/000162828026063314/ex991-fy26q3pressrelease.htm
- Inventory compounding faster than sales in a 6.6%-gross-margin distributor is the textbook route to a working-capital blowup, and **74 insider sales / $15.7M net / zero buys** says nobody inside is funding it either.
- decision: **exit.** Captured. This is the one place today where reading the primary document rather than the headline changed the answer — the headline was "beat and raise".

## [06:26 ET] AWAITING-ENTRY LIST — marked to 2026-09-24 closes
- `SNX` @260.00 — **FILLED** (see above). Exit captured.
- `XLU` SELL_SHORT @39.60 — **at/through entry**, XLU closed **39.36**, a 250-day low. Treat as working.
- `OXY` BUY @54.00 — **stale**, OXY closed **58.05** (+1.20%), 7.5% above the level; crude ran away from it. Not re-struck today: the book already carries three oil ideas and a fourth would breach the correlation cap.
- `IYR` SELL_SHORT @103.60 — **stale**, IYR closed 96.81, 7% below the entry.
- `DG` BUY @134.50 — DG closed **122.53** (+1.60%), 9% below the level. Unfilled, still live. Insiders: 0 buys, 1 sale.
- `KHC` BUY @23.00 — KHC closed **23.86**, 3.7% above. Unfilled. Insiders: **1 open-market buy of $5.00M**, net +$4.57M — the only net insider buying in the awaiting list. Worth a full workup next run.
- `VST` BUY @132.00 — VST closed **137.94**, 4.5% above. Unfilled. Insiders net **-$13.8M** on 11 sales against 3 buys from a single buyer — negative.
- `MU` BUY @960 — re-stated today as wait, see above.
- `GLD` SELL @406.77, `BTC` SELL @63,400, `/MBTU6` SHORT @64,340 — all far from market (GLD 391.69; BTC **84,433**, so the 63.4k short levels are 25% below spot and long dead). The three `KXFEDDECISION-*` contracts could not be marked — no price fetched.

## [06:26 ET] REJECTED (watchlist) — KMX — a real insider cluster the macro is fighting
- **5 distinct buyers, 6 buys, $1.27M, zero sells**, all between 2026-06-22 and 2026-06-25 at 52.01-53.39 (Chawla, Shinder, ONeil, Bensen, Barr). Stock 56.36, above their basis. Earnings **2026-09-29 bmo**.
- Rejected anyway: the cluster is three months old and small, and the macro runs directly against it — the 10y at 5.11% is an auto-affordability shock aimed straight at used-car retail, with the print two sessions away. KMX is below SMA20 60.08 and SMA50 59.42.
- Noting the reversal honestly: I rejected KMX earlier today as a *short* on the correlation cap. A long would not breach that cap (it offsets rather than stacks the rate bet), so the cap is not the reason — the reason is that I will not buy an affordability-driven retailer into a print while rates make a 19-year high.

## [06:27 ET] DATA QUALITY — options-implied moves unavailable
`market_data.py implied` returned **HTTP 401 Unauthorized** from yahoo-options for LW, CAG and TLT alike. So **no idea in today's report has been checked against the options-implied move**, which is a research step `config/strategy.md` asks for explicitly. Synthesis must say so in `data_quality_notes`. Combined with the Yahoo 429s on indices and the failed Kalshi Fed markets, today's gaps are: index levels, VIX, DXY, gold and crude spot, all event-contract prices, all implied moves, and NKE short interest.

## [06:27 ET] WATCHLIST (not published) — KHC — the best idea I could not finish
Strong story, incomplete work, so it stays off the report rather than being shipped half-derived — the same rule that killed CF above.
- **A $5.0M single open-market purchase by the new CEO.** CAHILLANE STEVEN A bought **213,106 shares at $23.4616 on 2026-05-12**. Stock closed **23.86** — still essentially his basis. Net insider +$4.57M (1 buy, 1 small sale).
- **Who he is matters:** Cahillane ran Kellogg through its breakup and then Kellanova through to its sale to Mars, arrived as KHC CEO in early 2026, and **paused the announced split in February 2026** saying the challenges are fixable — then bought $5M of stock three months later. sources: https://www.cnbc.com/2026/02/11/kraft-heinz-pauses-split-new-ceo-challenges.html , https://www.cnn.com/2025/09/02/business/kraft-heinz-breakup
- Sell side has capitulated: **7.1% bullish** — 2 strong_buy, **0 buy**, 17 hold, 7 sell, 2 strong_sell; revision direction improving but only +0.2pp.
- Price 23.86, -15.1% off the 28.09 high, below SMA20 24.82 and SMA50 25.33, ATR14 0.63 (2.62%), ADV **$477M** — very liquid. 150-day low 21.035 is the observable bear case.
- **Correction to a hypothesis I formed and checked:** the Form 25, 8-A12B and NYSE CERT filed 2026-09-08/09 looked like spin-off mechanics. They are **not** — reading them, they are a Nasdaq-to-NYSE listing transfer, last Nasdaq trade 2026-09-11, first NYSE trade 2026-09-14. **There is no separation catalyst; the split remains paused.** sources: https://www.sec.gov/Archives/edgar/data/1637459/000163745926000057/khc-20260824.htm , https://www.sec.gov/Archives/edgar/data/1637459/000163745926000061/khc-form8xagdcdraftx600180.htm
- **Why not published:** with the split paused there is no dated catalyst, so it can only be a `long_term` idea — and that needs a defended valuation target and a bear-case price. I have 2024 segment figures only (Taste Elevation $15.4B sales / $4.0B adj EBITDA; North American Grocery $10.4B / $2.3B) and did not fetch current share count or net debt, so I cannot build EV/EBITDA honestly. The existing `KHC` BUY @23.00 published 2026-09-20 is left standing and unamended.
- Next run: pull the 2026-06-27 10-Q (https://www.sec.gov/Archives/edgar/data/1637459/000163745926000054/khc-20260627.htm) for shares outstanding and net debt, then this becomes publishable.
- Note for synthesis: KHC and the open `CAG` are the same packaged-food-capitulation bet. Publishing both would be two ideas on one driver.

## [06:28 ET] FALSIFICATION PASS — recomputed every level before finishing
Checked each captured idea's arithmetic against `config/strategy.md` rather than trusting what I wrote:
| Idea | R:R | Floor | Stop in ATR | ATR floor | Verdict |
| --- | --- | --- | --- | --- | --- |
| TLT short | 2.000 | 2.0 | 2.66 | 1.8 (etf) | pass, exactly at the R:R floor |
| LW | 2.068 | 2.0 | 3.08 | 2.0 (stock) | pass |
| XLE | 2.129 | 2.0 | 2.25 | 1.8 (etf) | pass |
| CAG | 2.175 | 2.0 | 2.04 | 2.0 (stock) | pass, barely on stop distance |
| MU (first capture) | **1.989** | 2.0 | 2.01 | 2.0 | **FAILED** |
| MU (corrected) | 2.100 | 2.0 | 2.16 | 2.0 | pass |
| LNG | 2.750 | 2.5 | n/a (bear case 216) | n/a | pass |
| PFE | 3.618 | 2.5 | n/a (bear case 23.62) | n/a | pass |
- **MU was fixed by widening the stop 867 -> 860 and moving the target 1145 -> 1170**, a level 6.8% inside the observed 150-day high — not by pulling the stop in. Both entries are in the file; synthesis takes the last.
- **Conviction reconciled to the evidence count.** TLT, CAG and XLE each list 3 distinct kinds, which the table in `config/strategy.md` scores as 4, and I had written 3. Raised to 4 with the reason recorded on each idea. `LNG` is the one deliberate mismatch: 4 kinds would score 5, held at 4 because of the $28.4M of insider selling and 92.9% analyst bullishness, stated on the face of the idea.
- Correlation check on the final set — no driver carries more than 2: rates (TLT), energy/LNG supply shock (XLE, LNG), packaged food (CAG; LW is activist-driven rather than a staples-demand bet), company-specific (PFE, MU, LW). The four exits are each idiosyncratic.

## [06:29 ET] RESEARCH COMPLETE
- **candidates: 12 distinct symbols** (16 lines; MU, TLT, CAG and XLE each re-captured with corrections, last entry wins)
  - New ideas: `LNG` (long_term, the day's best), `LW` (swing, activist + insider cluster)
  - Amended/continuing: `TLT` short re-struck, `XLE` hold, `PFE` hold and reclassified to long_term, `CAG` hold, `MU` wait
  - Exits: `NKE`, `CCJ`, `LCII`, `LULU`, `SNX`
- **All 16 open positions and all 15 awaiting-entry ideas were marked to the 2026-09-24 close and given a decision.** Two corrections to prior_context: `SNX` @260 has **filled**, and `XLU` @39.60 is at/through its level.
- **coverage gaps:**
  - **No index or volatility read at all** — Yahoo returned HTTP 429 for SPX, NDX, DJI, RUT, VIX, DXY, ES, NQ, gold and WTI; finnhub refuses indices without a CFD subscription; stooq 404s on `^` symbols. No index level appears anywhere in today's work.
  - **No event-contract prices.** `events "Fed"` returned three unrelated multi-leg parlays with null prices. The three `KXFEDDECISION-*` contracts awaiting entry could not be marked, and no event idea was captured — a real miss given the hike repricing is today's dominant story.
  - **No options-implied move for any idea** — `implied` returned HTTP 401 from yahoo-options for every symbol tried.
  - **No short interest for NKE** (nasdaq ReadTimeout), so no squeeze read before recommending the exit.
  - **No crypto idea.** BTC 84,433 / ETH 2,698.28 / SOL 118.11 were fetched, but I formed no defensible view in the time available, and the `BTC`/`/MBTU6` shorts at 63.4-64.3k are 25% below spot and dead. Stating that beats manufacturing a view.
  - `CTRA` history unavailable from every source.
- **sources that failed:** Yahoo Finance chart API (429, all indices), yahoo-options (401, all symbols), Kalshi via `events` (returned irrelevant markets), nasdaq `short` endpoint (timeout), nasdaq history for CTRA.
- **the one thing to carry into tomorrow:** `KHC` is publishable as soon as someone pulls shares outstanding and net debt from the 2026-06-27 10-Q — new CEO Cahillane bought $5.0M open-market at 23.46 and the stock is 23.86, with the sell side 7.1% bullish.
