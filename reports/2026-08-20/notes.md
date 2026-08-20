# Research log — 2026-08-20

## [06:34 ET] MACRO — violent overnight debasement/risk-on move
- Bitcoin $71,905, **+11.77% 24h** (coingecko) — vol24h $63.7B
- Ethereum $2,282.10, **+19.09% 24h**; Solana $87.32, +13.13%
- GLD $413.84 **+3.84%**; SLV $60.01 **+4.47%** (prev close, pre-market session)
- TLT $83.02 **+1.67%** (long bond rallying); UUP $27.88 **-0.92%** (dollar down)
- VXX $19.05 -3.05%; SPY 769.06 +0.21%; QQQ 716.08 -0.20%; IWM 301.72 +0.50%
- FRED: US10Y 4.71 (2026-08-18), US2Y 4.19, fed funds 3.63, 10y2y +0.46 (was +0.52)
- Equities did NOT move much — this is a **currency/hard-asset** move, not an equity rally.
  Gold+silver+crypto+bonds up together with dollar down = monetary/debasement repricing.
- source: scripts/market_data.py macro + quote, 2026-08-20T10:33Z
- INDEX QUOTES FAILED: ^GSPC ^NDX ^DJI ^RUT ^VIX DXY 10Y gold futs WTI all ok:false
  (finnhub CFD subscription + yahoo 429 rate limit + stooq 404). Using ETF proxies instead.

## [06:34 ET] POSITION UPDATE — /MBTU6 SHORT — STOP BLOWN, MUST CLOSE
- two open shorts: 2026-08-18 @ 64,100 and 2026-08-19 @ 64,340; both stop 66,600
- BTC now 71,905 — gapped **through** the stop overnight; loss ~ -11.8% / -11.7% notional
- decision: **CLOSE IMMEDIATELY at market.** Thesis (BTC downside to 57k) is dead.
- also open: BTC spot SELL 2026-08-16 @62,950 and 2026-08-17 @63,400 — both wrong, close/abandon
- lesson: shorting a debasement asset into a dovish surprise. Do not re-short here.

## [06:37 ET] MACRO — THE DRIVER: Treasury doubles long-bond buybacks
- 2026-08-19: US Treasury announced it will raise "liquidity support" buyback operations
  on **longer-dated nominal coupons from $2B per operation to at least $4B**,
  running **Sept 9 – Nov 4, 2026**. Read by the market as quasi-QE / curve support.
- Reaction: dollar index to a **3-month low** (-0.8%); gold +3.5% to **$4,487/oz**,
  highest since June; silver +3.86%; BTC +~8%, **$1.4B of shorts liquidated** — the
  largest short wipeout in records back to 2021; ETH +8.8%; SOL +7%; XRP +6%.
- sources:
  https://www.coindesk.com/markets/2026/08/19/bitcoin-surges-above-usd68-000-liquidating-usd1-4-billion-shorts-as-treasury-buybacks-boost-risk-appetite
  https://finance.yahoo.com/markets/commodities/articles/gold-bitcoin-rally-u-treasury-191147069.html
- NOTE: coingecko has BTC at 71,905 as of 10:33Z — i.e. it kept going *past* the
  $68-69.7k levels in yesterday's stories. The move extended overnight.

## [06:37 ET] CALENDAR — the dated catalyst that dominates the next 10 sessions
- **Jackson Hole Economic Symposium, Aug 27-29 2026.** Theme: "Financial Innovation:
  Implications for Payments and Policy."
- **Kevin Warsh is Fed Chair** and delivers his **first keynote Fri Aug 28, morning ET.**
  (Powell stepped down as Chair but remains a Governor to 2028.)
- source: https://www.regardsofwallstreet.com/news/jackson-hole-2026-dates-schedule-warsh-first-speech
- WHY THIS MATTERS: Warsh's public record is hawkish/hard-money. The Treasury buyback is
  a *fiscal-side* liquidity injection; Warsh has historically criticised exactly that
  kind of Fed/Treasury blurring. **A hawkish Warsh debut on Aug 28 is the single
  biggest risk to every long-hard-asset trade set up today.**
- Trade implication: hard-asset longs entered now must either (a) trim into Aug 28,
  or (b) carry an explicit stop sized for that event. Do not enter naked size.

## [06:40 ET] LEVELS — precious metals complex already ripped (prev close, 2026-08-19)
- GDX 97.33 **+9.42%** | GDXJ 126.55 +9.64% | SIL 95.87 +9.53% | SILJ 31.42 +9.55%
- AG 20.85 **+12.82%** | HL 20.54 **+14.43%** | CDE 20.93 +13.07% | PAAS 50.30 +7.94%
- AEM 207.72 +11.12% | WPM 147.43 +11.10% | NEM 125.08 +7.85% | FNV 251.07 +7.77%
- CAUTION: a one-day +9-14% in miners is a chase, not an entry. The metal moved 3.5-4.5%;
  the miners moved 3x that on operating leverage. Buying the day-2 open here is paying
  for the gap. Any metals idea today must be a pullback zone, not a market order.

## [06:40 ET] CALENDAR — dated earnings catalysts, next 10 sessions (finnhub)
- **Aug 20 bmo: WMT** (eps est 0.749, rev est $188.8B) — today, consumer read-through
- Aug 20 bmo: BABA, DE, NTES, FUTU, SPR | amc: FLO, OSIS
- Aug 21 bmo: BJ, UI
- Aug 24: PDD (bmo), DKS, PVH, XPEV (bmo)
- Aug 25: INTU (amc), ZM (amc), ANF, FIVE, KSS, WSM, HEI (amc)
- **Aug 26 amc: NVDA** (eps est 2.128, rev est $93.6B) — the index-level event
  also Aug 26: CRM (amc), CRWD (amc), SNPS, VEEV, OKTA, HPQ, NTNX, A, BURL, GMS, DY
- **Aug 27: MRVL, ULTA, DG, BBY, GAP, ADSK, WDAY (amc), AFRM (amc), ESTC, S, IREN (amc)**
- Aug 31: FRO (bmo, tankers — relevant to open DHT position), AEO, ASO, SAIC
- NOTE the collision: **NVDA Aug 26 amc, then Warsh's Jackson Hole keynote Aug 28 am.**
  Two index-moving events 2 days apart. Anything held through both carries double event risk.

## [06:48 ET] DECISION — no BTC recommendation today, in either direction
- The four open bearish BTC lines (spot SELL 8/16 @62,950 and 8/17 @63,400;
  /MBTU6 SHORT 8/18 @64,100 and 8/19 @64,340, both stop 66,600) are **all wrong and
  all stopped**. BTC 71,905. **Action: flatten every one of them at market.**
- I am deliberately NOT capturing a BTC candidate. Re-shorting after the largest
  short liquidation on record ($1.44B) is how the same mistake gets made twice, and
  buying spot after +11.8% in 24h is chasing. **Stand aside on BTC.**
- The instruction to close is recorded here and must survive into the report.

## [06:48 ET] LEVELS — TLT is the un-extended leg of the trade (nasdaq, thru 2026-08-19)
- TLT 83.02. ATR14 0.653 (0.79%). SMA20 82.63, SMA50 84.28. 120d range 81.17-90.86.
- **Printed its 120-day low 81.17 on Aug 18 — the day before the announcement — then
  reversed to 83.02 on 51M shares vs ~30M average.** Key reversal off the low on 2x volume.
- Contrast: GDX 97.33 is **+17% above its SMA20** (83.20) and +30% since Jul 24.
  SLV 60.01 vs SMA20 55.67, but still -29.6% off its 120d high of 85.27 (silver had a
  blowoff to ~85 and a crash to 49.61 earlier this year).
- Conclusion: metals have already paid; the long bond has not. Captured TLT.
- CAPTURED: TLT buy 82.60 (82.20-83.10) / tgt 86.20 / stop 80.95 / conv 3 / R:R ~2.2

## [06:54 ET] LEVELS — the rest of the hard-asset complex (prev close 2026-08-19)
- FCX 69.09 +4.18% | SCCO 194.68 +3.66% | COPX 88.28 +3.17% | XME 117.07 +3.03%
- URA 45.01 +3.19% | URNM 55.55 +3.06%  (relevant: CCJ is an open position)
- PPLT 16.46 **+5.78%** | PLTM 17.47 +6.14%  (platinum out-ran gold)
- ITB 99.26 +3.10% | XHB 108.23 +2.15% (homebuilders bid on the lower long end)
- EEM 66.11 +1.18% | FXI 35.68 +1.77% | EWZ 34.26 +1.66% (weak-dollar EM bid, muted)
- Extension check vs SMA20: FCX 69.09/66.02 = +4.7%; ITB 99.26/98.10 = +1.2% (NOT extended);
  SLV 60.01/55.67 = +7.8%; PPLT 16.46/15.38 = +7.0%; GDX +17.0% (most extended by far)
- % off 120d high: FCX -4.4%, ITB -8.3%, GDX -16.9%, PPLT -23.6%, SLV -29.6%
- CAUTION on the "silver has room" argument: SLV's 85.27 high was a squeeze that broke
  to 49.61 inside 120 days. That print is not a valuation anchor and I will not use it
  as evidence of upside. Same caveat applies to PPLT.

## [06:54 ET] CORRELATION BUDGET — hard limit 3 ideas per driver
- Driver A (Treasury buyback / weak dollar / hard assets): **TLT captured = 1 of 3.**
  Metals are the crowded expression and are extended; spend the other 2 slots carefully.
- Must find ideas on other drivers: earnings catalysts, consumer, idiosyncratic, shipping.

## [06:54 ET] TAPE — premarket 2026-08-20 flat, no follow-through yet
- S&P 500 -0.05%, Nasdaq 100 +0.05%, Dow -0.14%, Russell 2000 -0.15% premarket
- "bifurcated: extreme micro-cap volatility against flat-to-lower mega-cap semis"
- source: https://www.thedesperatetrader.com/premarket-movers
- Read: the hard-asset move is NOT bleeding into equities this morning. Confirms the
  move is a currency/rates event, not a risk-on event. Reinforces TLT over miners.

## [06:57 ET] GAP — biotech/FDA catalyst lane not covered
- Searched the Aug/Sep 2026 PDUFA calendar; results were aggregator landing pages
  (rttnews, marketbeat, biopharmawatch) with no specific ticker+date pairs returned.
  August 2026 reportedly has 412 catalysts, September 119, several first-in-indication.
- Running down individual names would cost more time than I have. **Logged as a
  coverage gap rather than guessed at.** No biotech candidate today.
- source: https://www.marketbeat.com/fda-calendar/upcoming/

## [07:00 ET] LONG-TERM — platinum: structural supply, near-term de-rate already delivered
- WPIC: **2026 is the 4th consecutive year of platinum deficit**, forecast 297 koz.
- BUT the deficit **contracted >70% YoY** (2025 ~1.1 Moz -> 2026 ~297 koz). Kitco's WPIC
  headline is literally "A balanced platinum market in 2026 won't fix fundamental
  long-term issues" — near-term balanced, long-term tight. I will not hide this.
- Supply +2% YoY to 7,377 koz, and **every ounce of growth is recycling (+10%)**;
  mine guidance is flat — miners did not respond to a >90% price surge off Q2-2025.
- **South Africa + Russia + Zimbabwe = ~90% of primary PGM supply.** Q1-26 production
  declines at Norilsk Nickel and Zimplats.
- Above-ground stocks fall to **just under 3 months of demand cover** by end-2026.
- Price: platinum passed $1,900 in Dec 2025; Metals Focus raised its 2026 forecast to
  **$2,190/oz**. A competing deficit-return case argues only $1,750 by year-end. Noted.
- sources: https://www.kitco.com/news/article/2025-11-19/balanced-platinum-market-2026-wont-fix-fundamental-long-term-issues-wpic
  https://platinuminvestment.com/supply-and-demand/2-to-5-year-view
  https://investingnews.com/platinum-forecast/
- PPLT 16.46, SMA20 15.38, SMA50 15.11, 120d 14.06-21.54, ATR 2.72%. Off high -23.6%.
  The de-rate from ~21.5 to ~16.5 is the narrowing deficit already in the price.
- PLAN: do NOT chase +5.8%. Accumulate on a pullback toward the 20/50 SMA cluster.

## [07:00 ET] INSIDERS — checked every equity finalist and every open equity position
- **NKE: 5 open-market buys, 4 distinct buyers** — a real cluster. NKE is an OPEN
  position (8/17 @40.00 and 8/18 @38.00; last 41.16, +2.9%). This is NEW evidence.
- **PFE: 3 open-market buys, 3 distinct buyers** — also an OPEN position (8/18 @25.80,
  last 28.32, +9.8%). Also new supporting evidence.
- HL 0, AG 0, DHT 0, PPLT 0 (n/a, it is a trust). Absence is not a negative.

## [07:07 ET] POSITION UPDATE — PFE — opened 2026-08-18 @ 25.80, last 28.24, +9.5%
- decision: **HOLD, do not add at 28.24.** Add only on a pullback into 25.60-27.20.
- why (NEW evidence): insider cluster is recent, concentrated and CEO-led —
  * **Albert Bourla (CEO): 38,000 sh @ $26.34 on 2026-08-12** (~$1.0M)
  * Mortimer Buckley (director, ex-Vanguard CEO): 37,632 sh @ $25.52 on 2026-08-05
  * Ronald Blaylock (director): 39,231 sh @ $25.46 on 2026-08-05
  * 3 distinct buyers, $2.96M bought vs $0.13M sold, net +$2.83M, all inside 3 weeks
- price action: 26.80 -> 28.24 over three sessions, 59M shares on 8/19 vs ~30M typical.
  PFE is now **-1.8% off its 120d high (28.745)**; SMA20 25.98, SMA50 25.27, ATR 2.21%.
- The stock has already moved through the entire insider buy zone. Chasing the breakout
  is not what the insider signal argues for — the insiders paid 25.46-26.34.
- action: captured via add_candidate.py as a continuing long_term position with the
  add-on zone at 25.60-27.20, NOT at the current price.

## [07:07 ET] POSITION UPDATE — NKE — opened 8/17 @40.00 and 8/18 @38.00, last 41.05
- decision: **HOLD both, do NOT add, no new candidate.**
- insider check: 5 open-market buys / 4 distinct buyers looks strong at a glance, but
  every purchase is from **April 2026 at $42.27-43.34** (incl. Tim Cook, 25,000 @ 42.43
  on 2026-04-10) — four months stale and **all underwater at 41.05**.
- Treating a stale, underwater April cluster as fresh August evidence would be exactly
  the anchoring error the prior-context guard warns about. It is not new information.
- technicals still broken: NKE -34.6% off its 120d high (62.72), below SMA20 (41.58)
  AND SMA50 (42.65). Both open lines are in profit; let them run to the 62-65 targets.
- note: prior_context lists last 41.16; actual 2026-08-19 close is **41.05**.

## [07:11 ET] GAP — event contracts unusable today
- Queried market_data.py events for "Fed", "gold", "interest rate", "inflation",
  "recession", "bitcoin". Five returned **count 0**; "gold" returned 2 markets that
  were **Korean baseball parlays** (KXMVECROSSCATEGORY shards) with null bids/asks.
- The Kalshi search endpoint is matching badly, not returning a thin market list.
- **No event-contract candidate today.** I will not invent an implied probability I
  could not read off a live book. This is a real coverage gap, not an absence of ideas.

## [07:12 ET] FALSIFICATION — the case against each captured candidate

### TLT (buy 82.60, tgt 86.20, stop 80.95, conv 3)
- Strongest bear case: **buybacks are debt management, not new money.** Treasury funds
  a buyback by issuing elsewhere — usually shorter. Net duration removed is real but far
  smaller than a "$2B -> $4B" headline implies, and the program is only 8 weeks.
- Second: if the announcement is read as monetisation, **term premium rises** and the
  long end sells off while the Treasury buys. Gold +3.5% and a 3-month-low dollar say
  a chunk of the market already chose that reading. TLT gained only 1.67% vs gold 3.5%
  — the bond market gave this the *smallest* vote of any asset. That is a warning.
- Third: **Warsh at Jackson Hole Aug 28.** A hawkish debut is the direct kill shot.
- SURVIVES, but at conviction 3 and no higher, with the explicit instruction to trim
  half before Aug 28. The 81.17 stop-out level is only 2.5% away, so the loss is bounded.

### PPLT (accumulate 15.00, tgt 20.50, bear 13.00, conv 3, long_term)
- Strongest bear case: **the deficit is collapsing, not persisting** — 1.1 Moz -> 297 koz,
  a >70% contraction, and WPIC's own framing is a "balanced" 2026. One more year of that
  is a surplus and the thesis is simply wrong.
- Second: all supply growth is **recycling**, which is price-elastic and scales with the
  higher price — a self-limiting mechanism that caps the metal.
- Third: EV adoption structurally erodes autocatalyst demand, the largest end-use.
- Fourth: **I could not fetch a live platinum spot price** — only PPLT's share price.
  The $2,190/oz Metals Focus target and the $1,750 competing case cannot be mapped to a
  precise PPLT share target without an oz-per-share conversion I did not verify. The
  20.50 target is therefore anchored to **PPLT's own 2026 trading range (120d high
  21.54)**, not to a claimed ounce conversion. Stated plainly so nobody reads it as
  precision it does not have.
- SURVIVES as a patient accumulation only, sized 2.5%, and only below the 50-day.

### PFE (add 26.40, tgt 38.00, bear 22.50, conv 4, long_term, CONTINUING)
- Strongest bear case: **the entry is gone.** Insiders paid 25.46-26.34; the stock is
  28.24. The signal was actionable at $25.50, and it is a different trade at $28.24.
  This is precisely why the candidate says add only into 25.60-27.20 and hold otherwise.
- Second: patent cliff is a real, quantified revenue hole; cheap multiples on declining
  post-cliff earnings are the classic value trap.
- Third: a $1M purchase is small relative to CEO compensation and directors buy for optics.
- Fourth: the 3-session pop may just be the defensive-pharma leg of yesterday's rotation
  out of the dollar, in which case it is macro noise wearing an insider costume.
- SURVIVES at conviction 4 — three distinct buyers inside three weeks, CEO-led, with a
  17:1 buy/sell value ratio, is a genuinely rare configuration. Conviction is in the
  *evidence*, not the entry, and the entry discipline is handled by the add-on zone.

## [07:13 ET] REJECTED — logged so synthesis does not re-litigate these
- **GDX / GDXJ / SIL / SILJ / AG / HL / CDE** — +9% to +14.4% in a single session; GDX is
  +17% above its SMA20. Buying the day-2 open is paying for the gap. No entry, not a view.
- **SLV** — +7.8% over SMA20; the "-29.6% off the high" bull argument leans on an 85.27
  print that crashed to 49.61 inside 120 days. A broken squeeze is not a valuation anchor.
- **ITB / XHB** — genuinely the least-extended rates-geared equity (+1.2% over SMA20,
  -8.3% off high) and I wanted it. Killed on two counts: R:R only ~1.90 from 98.00 to a
  107.50 target with an honest 2-ATR stop at 93.00, which fails the 2.0 swing floor; and
  **HD is already open on three separate lines**, so housing+rates is at the correlation
  cap before ITB is added.
- **BTC / ETH / SOL** — no recommendation in either direction. See the 06:48 block.
- **NVDA (Aug 26 amc)** — the largest dated catalyst on the calendar and the most crowded
  trade on the tape. No differentiated view, no edge in the print. Skipped deliberately.
- **FCX / SCCO / COPX** — only -4.4% off the high and +4.7% over SMA20; no dated catalyst.
- **EEM / FXI / EWZ** — the weak-dollar EM bid was muted (+1.2% to +1.8%) and I have no
  country-level thesis to justify it. Vague.
- **Biotech/FDA** — see the 06:57 gap. Not researched, not guessed.

## [07:14 ET] BOOK-LEVEL NOTE — today's priority is repair, not expansion
- The book carries **22 open positions** and four of them (2x /MBTU6 short, 2x BTC spot
  sell) are wrong and require closing this morning. XLE appears 5x, TJX 4x, KRE 4x, HD 3x.
- Deliberately capturing **3 well-diversified candidates rather than padding to a tidy
  number**. Per config/strategy.md: four strong ideas beat ten with six of filler.
  Adding a large new risk book on the same morning four lines blew through their stops
  would be bad risk management dressed up as productivity.
- Driver diversification of the three: TLT = US rates/duration; PPLT = PGM structural
  supply (long-term); PFE = single-name idiosyncratic insider signal. No two share a driver.

## [07:14 ET] RESEARCH COMPLETE
- candidates: 3 (TLT swing conv3, PPLT long_term conv3, PFE long_term conv4)
- position actions required: CLOSE 2x /MBTU6 short + 2x BTC spot sell (stops blown,
  BTC 71,905 vs 66,600 stops). HOLD NKE x2 (no add, insider cluster is stale/underwater).
  HOLD PFE (no add above 27.20).
- coverage gaps: event contracts (Kalshi search returned count 0 / mismatched markets);
  biotech FDA calendar (no ticker-level dates retrievable in budget); no live platinum
  spot price; index quotes (^GSPC ^NDX ^DJI ^RUT ^VIX DXY WTI) all failed - ETF proxies
  used throughout, so every index figure here is a proxy, not the index.
- sources that failed: finnhub index quotes (CFD subscription required), yahoo (HTTP 429
  rate limited on every index symbol), stooq (404 on ^-prefixed symbols), alphavantage
  (no api key), kalshi events search (returns 0 or irrelevant markets).
- sources that worked: coingecko (crypto), FRED (rates/CPI/unemployment), nasdaq
  (OHLCV history), finnhub (equity quotes, earnings calendar, insider transactions).

## [07:18 ET] VENUE CHECK — PPLT confirmed tradeable on Robinhood
- Robinhood carries PPLT: https://robinhood.com/us/en/stocks/PPLT
- NYSE Arca listed. AUM **$2.04B**, market price 15.85 / NAV 15.82 as of 2026-08-07,
  net expense ratio **0.60%**. Physical metal vaulted in London, audited twice yearly
  by Bureau Veritas (once at random).
- source: https://www.aberdeeninvestments.com/en-us/institutional/funds/view-all-funds/abrdn-physical-platinum-shares-etf-us0032601066
- Liquidity: 1.5-4.1M shares/day x ~$16 = **$24M-65M/day**. Far above the $500K floor.
- Flag the 0.60% expense ratio in the report — it is a real drag on a multi-year hold.

## [07:18 ET] DATA QUALITY — PPLT executed a 10-for-1 FORWARD SPLIT
- Aberdeen announced a **10-for-1 forward split of PPLT** (and 5-for-1 of PALL).
  source: https://www.prnewswire.com/news-releases/aberdeen-investments-announces-10-for-1-forward-share-split-of-abrdn-physical-platinum-shares-etf-pplt-and-5-for-1-forward-share-split-of-abrdn-physical-palladium-shares-etf-pall-302750450.html
- **This is why PPLT prints ~$16 rather than ~$160, and it must not be mistaken for a
  collapse in the metal.** Any downstream price check against pre-split quotes will be
  wrong by 10x. Calling it out explicitly for the validation phase.
- The nasdaq history I used **is** split-adjusted: the 120d range (14.06-21.54) and the
  last five closes (15.54/15.87/16.07/15.56/16.46) are all on the post-split scale and
  agree with the independently-sourced NAV of 15.82 on 2026-08-07. Levels are sound.
- Sanity check on the 20.50 target: it is **below** PPLT's own 120d high of 21.54, and
  PPLT traded at that high while platinum was near the ~$1,900 it "passed in December".
  Both published forecasts I found (Metals Focus $2,190, the competing case $1,750) sit
  at or above the implied level of the 20.50 target. **The target is conservative against
  every anchor I could source**, which is the right side to err on. I still could not
  fetch a live platinum spot price, so I am not asserting an exact oz-per-share mapping.

## [07:19 ET] REJECTED — DE (Deere) — reports today bmo, no differentiated view
- DE 580.63, **-9.8% off its 120d high**, and below BOTH SMA20 (610.69) and SMA50
  (602.64) — i.e. going into the print in a downtrend. eps est 4.835, rev est $11.05B.
- Insiders: **0 open-market buys, 0 distinct buyers.** No confirmation.
- It reports in roughly one hour and I have no edge on the number. Entering a print
  blind is gambling, not a trade. Rejected — but flagged as worth revisiting after the
  reaction, since an ag-equipment downcycle name at -10% is the right shape for this report.

## [06:43 ET] CORRECTION — timestamps above are WRONG; research is NOT complete
- I checked `date` and the real time is **06:43 ET**, not the 07:19 I had been labelling.
- Research started 06:32:47. **Only ~10 minutes of wall clock have actually elapsed.**
- I estimated elapsed time from my own sense of it instead of calling `date`, which is
  the exact failure config/strategy.md and the skill both warn against. Every heading
  from roughly "06:40" onward is stamped 20-35 minutes ahead of reality.
- **Treat the ordering of the blocks as correct and the clock values as unreliable.**
  All prices, levels and sources in them were fetched and are unaffected.
- Consequence: the "RESEARCH COMPLETE" block above was premature. Real budget runs to
  ~07:32, with new research allowed until ~07:14. **Research continues below.**
  A corrected RESEARCH COMPLETE block is appended at the end of this file.

## [06:46 ET] SCREEN — beaten-down names with dated earnings (Aug 26-27), 120d stats
symbol  last     off-high   vs SMA20  vs SMA50  ATR%    reports
MRVL    237.27   -28.07%    +15.1%    +1.2%     7.34    Aug 27
CRWD    201.63   -11.37%     -0.9%    +5.0%     4.61    Aug 26 amc
OKTA    141.21   -10.06%     -1.8%    +3.0%     4.79    Aug 26 amc
ADSK    251.29    -5.08%     +4.6%   +15.0%     3.76    Aug 27
WDAY    198.42   -12.78%    +15.4%   +34.0%     6.10    Aug 27 amc
ESTC     87.34    -0.70%    +20.7%   +34.8%     4.61    Aug 27
AFRM     77.33   -10.91%     +3.6%    +1.7%     4.90    Aug 27 amc
DG      122.31   -22.13%     -1.0%    +2.1%     2.80    Aug 27
ULTA    527.85   -24.86%     +1.7%    +8.0%     3.45    Aug 27

## [06:46 ET] REJECTED — the whole Aug 26-27 earnings cohort. Reasoning, once:
- **DG (-22.1% off high, flat base at the 20/50, low 2.80% ATR) and ULTA (-24.9%) are
  the two I most wanted** — de-rated consumer names coiled into a dated catalyst is
  exactly the right shape. Both killed on **correlation, not merit**: the open book
  already carries TJX x4 and HD x3, seven live lines on the US consumer. Adding a
  discount retailer and a beauty retailer would put one driver at nine lines against a
  stated cap of three. Revisit when the TJX/HD lines close.
- **CRWD / OKTA** — cyber is genuinely absent from the book and I looked hard. But both
  sit within 2% of their 20-day in the middle of a wide 120d range with a print in four
  sessions. Mid-range + no view + binary event = gambling on a number, which is the same
  reason I rejected DE. No differentiated thesis, so no trade.
- **ESTC (+20.7% over SMA20, -0.7% off its high), WDAY (+15.4% over SMA20, +34% over
  SMA50), MRVL (+15.1% over SMA20, 7.34% ATR)** — all extended into the print. Worst
  possible risk shape: priced for good news, and a 7% ATR on MRVL means a normal day
  is a stop-out.
- **ADSK** — only -5.1% off its high and +15% over the 50-day. Nothing on offer.

## [06:49 ET] REJECTED — ETON (Eton Pharmaceuticals) — insiders distributing into the spike
- The fundamental news is real and good: Q2 revenue **+99% YoY to $37.6M**, 2026 guidance
  raised from >$120M to **>$145M**, upgrades from B. Riley, Canaccord and H.C. Wainwright
  with a PT as high as $70. Exactly the small-cap shape this report is told to hunt.
  source: https://www.cabotwealth.com/daily/small-cap-stocks/small-cap-growth-stocks-up-100
- Liquidity is fine: **$33.7M average daily dollar volume** (30d), well clear of the floor.
- **Killed by the insider check.** ETON insiders: **0 open-market buys, 16 sells,
  $13.95M sold, net -$13.95M.** And a **Form 144 filed 2026-08-19 — yesterday** —
  i.e. notice of a further proposed sale of restricted stock, filed into the highs.
  source: https://www.sec.gov/Archives/edgar/data/1710340/000197407826000315/xsl144X01/primary_doc.xml
- Price context: gapped **40.80 -> 58.86 (+44%) on Aug 14** on the print, now 61.48.
  That is **+28% over its SMA20 (48.03) and +51% over its SMA50 (40.80)**, only -3.7%
  off the 120d high, on a 6.69% ATR. 10-Q and 8-K both filed 2026-08-13.
- Verdict: good company, wrong moment. Buying a +44% gap while management files to sell
  into it is paying insiders to exit. **This is precisely what the mandatory insider
  check on every equity finalist is for** — the thesis read well until that one query.

## [06:49 ET] DURABLE MISPRICING — gold equities are cheap on cash flow, not on price
- **Large-cap gold producers trade at 7.83x NTM cash flow vs a 5-year average of 8.86x**
  — an 11.6% discount to their own history *after* a huge move in the metal, because
  earnings re-rated faster than the multiple.
- Record H1/Q2 2026 free cash flow across the majors, with capital returns scaling:
  * Newmont Q2 FCF **$2.2B** (record)
  * Agnico Eagle Q2 FCF **$1.335B**, returned a record **$625M** to shareholders
  * Kinross FCF **>$725M**, ~40% of it returned
  * Endeavour Mining H1 FCF record **$761M**, $301M returned
- sources: https://discoveryalert.com.au/gold-miners-record-free-cash-flow-valuation-paradox-2026/
  https://nai500.com/blog/2026/07/gold-prices-stall-near-4000-but-miners-record-cash-flow-tells-a-different-story/
  https://www.vaneck.com/us/en/blogs/gold-investing/ima-casanova-sustaining-strength-in-a-higher-gold-price-environment/
- This **partially reverses my earlier blanket miner rejection**, and I want to be
  explicit about that rather than quietly contradict myself. The rejection stands for a
  *swing* entry — GDX at +17% over its SMA20 is a chase on any days-to-weeks horizon.
  It does not stand for a *long-term* position, where the anchor is a below-average
  cash-flow multiple against record FCF, not this week's candle.
- Instrument choice: **GDX (the basket), not a single miner.** The thesis is sector-level
  (multiple vs history, sector FCF), so single-mine, single-jurisdiction and operational
  risk are uncompensated here. A basket is the honest expression of a sector claim.

## [06:48 ET] VERIFIED — Treasury buyback, from the PRIMARY source
- **https://home.treasury.gov/news/press-releases/sb0607** (Treasury press release sb0607)
- Increases liquidity-support buybacks for the **10y-20y sector AND the 20y-30y sector**
  from a $2B per-operation maximum to **at least $4B per operation**.
- **Effective Sept 9, 2026, through Nov 4, 2026** (the remainder of the refunding quarter).
  Further sizing to be announced at the **Nov 4 Quarterly Refunding**.
- **The 20y-30y sector is exactly what TLT holds (20+ year maturities).** This is a more
  direct hit on TLT's own collateral than I had when I captured it. Upgrading the note.
- CNBC framed it as "Bessent moves to steady bond market", yields lower on the day.
  https://www.cnbc.com/2026/08/19/treasury-announces-upscaled-buyback-operation-for-longer-term-debt-sending-yields-lower.html
- **Cuts BOTH ways, and Treasury's own words are the bear case:** the release says the
  increase "reflects Treasury's desire to provide greater liquidity support in longer-dated
  nominal sectors where there is consistent strong sponsorship from market participants."
  That is Treasury explicitly calling this **liquidity plumbing, not stimulus** — and it
  is the strongest support for my own counter-argument that buybacks are debt management,
  not new money. Keeping TLT at conviction 3 for exactly this reason.

## [06:48 ET] VERIFIED — Warsh / Jackson Hole, and a direct quote that raises the risk
- Jackson Hole **Aug 27-29 2026**; theme "Financial Innovation: Implications for Payments
  and Policy". **Warsh's first keynote as Chair: Friday morning, Aug 28.**
  He **took office May 22, 2026.** Confirmed across multiple independent sources.
- **Warsh, at a press conference, said his Jackson Hole speech would step back from
  "near-sighted debates" to raise "big questions", and that the Fed is
  "not constrained by market prices."**
  source: https://finance.biggo.com/news/5199dcdf-716b-4f74-81f1-60f5a3b95518
  also: https://kalkine.com/news/premium/jackson-hole-2026-can-warshs-debut-signal-where-rates-go-next
- **This is the single most important sentence I found today.** A new Fed Chair saying he
  is "not constrained by market prices" days after the largest hard-asset repricing of the
  year is a direct signal that he may decline to validate the market's dovish read.
  Every hard-asset idea I captured must respect Aug 28. The "trim half before Aug 28"
  instruction on TLT is not boilerplate — it is the trade.
- Counterpoint, noted for balance: investinglive reports "Jackson Hole hype outruns Warsh
  playbook of saying as little as possible" — his style may be to under-deliver news.
  https://investinglive.com/central-banks/jackson-hole-hype-outruns-warsh-playbook-of-saying-as-little-as-possible/
- **NEXT FOMC: Sept 15-16, 2026, with updated projections (SEP).** Second dated catalyst,
  and the one that actually sets rates. Sits inside the buyback window.

## [06:48 ET] POSITION SWEEP — 12 of 22 open lines are through their stops
Fetched live prices for every open symbol and compared to the actual stop on each line.
prior_context.md carried stale marks (it showed TJX 148.05/148.21 and KRE 75.96/76.01);
the real 2026-08-19 closes are worse.

| Symbol | Last | Chg | vs entry | Stop(s) | Status |
| --- | --- | --- | --- | --- | --- |
| KRE | 75.00 | -2.41% | -2.3% | 74.2 / 75.4 / 75.2 | **BREACHED on 2 of 3 stops, 3rd at 1.1%** |
| TJX | 144.50 | -4.21% | -4.6% | 146.5 / 145.5 | **BREACHED on both** |
| /MBTU6 | BTC 71,905 | +11.8% | -11.7% | 66,600 x2 | **BREACHED, gapped through** |
| BTC spot | 71,905 | +11.8% | — | (sell thesis dead) | **THESIS DEAD** |
| XLE | 63.58 | -0.16% | +4.6% | 57.8/58.6/59.2 | ok, 7.4% above nearest stop |
| DHT | 19.99 | +3.52% | +6.3% | 17.6 | ok, 13.6% above stop |
| HD | 344.30 | +2.02% | +1.3% | 328.0 x2 | ok, 5.0% above stop |
| BCC | 83.13 | +3.68% | +2.6% | 76.0 | ok, 9.4% above stop |
| CCJ | 97.98 | +2.03% | +3.1% | none | ok, running |
| LCII | 107.70 | +4.29% | **+14.6%** | none | ok, best open line |
| NKE | 41.05 | +2.47% | +2.6% | none | hold (see 06:43 block) |
| PFE | 28.24 | +3.63% | +9.5% | none | hold, no add (see 06:43 block) |

- **ACTION REQUIRED THIS MORNING: close KRE (4 lines), TJX (4 lines), /MBTU6 short
  (2 lines) and BTC spot sell (2 lines). Twelve of twenty-two open lines.**
- This is the single most consequential output of today's research. It matters more than
  any new idea: the book was carrying 12 dead positions against stale marks.
- I am NOT capturing replacement ideas for KRE or TJX. Both were stopped for a reason and
  re-entering the same names the morning they stop out is how a stop becomes a suggestion.

## [06:49 ET] WHY TJX BROKE — Q2 beat, FY raised, but Q3 guided light on wage costs
- Q2 FY27: **EPS $1.22 vs $1.19 est (beat)**, sales $15.2B in line, **comps +4%**, faster
  than expected. **FY EPS raised to $5.31-5.36 from $5.08-5.15**; FY pretax margin guide
  raised to 12.3-12.4%.
- The problem was the near term: **Q3 adj EPS guided $1.30-1.32 vs ~$1.35 consensus**, and
  **adj SG&A rose to 19.7% of sales on incremental store-level wage growth.** CEO Ernie
  Herrman also announced accelerating **store openings to 4% growth next year** (global
  target lifted to 7,500) — more capex into a consumer whose buying power inflation has
  eroded. Stock -4.2%.
- sources: https://qz.com/tjx-raises-full-year-profit-forecast-stock-falls-081926
  https://www.bloomberg.com/news/articles/2026-08-19/tj-maxx-owner-s-plan-to-open-more-stores-hits-shares-after-beat
  https://www.cnbc.com/2026/08/19/why-were-giving-off-price-retailer-tjx-a-pass-for-softness-in-its-biggest-division
- **Honest nuance: there is a real argument this was an overreaction** — the full year was
  raised and comps accelerated. CNBC explicitly "gave TJX a pass". I am still closing it,
  because the stop was hit and a stop that gets re-argued after it triggers is not a stop.
  The catalyst has also now passed, so the original thesis has no remaining catalyst.
- **READ-THROUGH: wage-driven SG&A and a cautious near-term consumer is a cohort problem,
  not a TJX problem.** DKS Aug 24, ANF/KSS/FIVE/WSM Aug 25, BURL/BBWI Aug 26,
  ULTA/DG/BBY/GAP Aug 27 all report into it. This independently confirms the earlier
  decision to reject DG and ULTA rather than buy the de-rating ahead of their prints.

## [06:49 ET] WHY KRE BROKE — the curve flattened, which is the mechanism
- KRE -2.41% to 75.00 on a day when nearly every other asset rallied. Not noise.
- FRED: **10y-2y spread went 0.52 -> 0.46 (2026-08-19)** as Treasury announced it would
  buy the long end. A flatter curve compresses regional-bank net interest margin directly.
- So the same policy that supports TLT actively hurts KRE. The two open books were
  **structurally opposed** and nobody had noticed.
- NOTE, and then declining to act on it: the buyback runs Sept 9 - Nov 4, so the flattening
  pressure is scheduled to continue, which is a coherent *bearish* KRE thesis. I am **not**
  capturing a KRE short. Flipping from long to short in the same name on the morning the
  long stops out is whipsaw trading dressed up as conviction, and a short needs margin.
  Logged as an observation for a future session, not a trade for today.

## [06:52 ET] REJECTED — the entire crude-tanker complex, at the top of a war-driven cycle
- Rates are extraordinary: **VLCC earnings $170,000-200,000/day**, six-year highs; the
  Baltic **TD3C MEG-China index hit a record $423,736/day after the outbreak of war in
  March 2026**, +94% in a single session. Orderbook a historically tight 5-7%.
  sources: https://www.lloydslist.com/LL1156492/Crude-tanker-rates-in-unchartered-territory-VLCC-index-tops-420K
  https://www.mees.com/2026/2/27/refining-petrochemicals/middle-east-crude-shipping-costs-surge-to-six-year-highs/c0d9c9a0-13e8-11f1-917b-c9bc2043c45f
- **Calibration matters here.** Industry benchmarks: $30-40k/day covers opex, >$50k/day
  funds strong dividends, **>$80k/day is "exceptional cycle-peak territory."**
  Current $170-200k/day is **two to two-and-a-half times the definition of a cycle peak.**
- Price: every name is pinned to its 120d high — TNK -0.7%, INSW -0.8%, FRO -1.6%,
  DHT -2.7% off high. TNK +13.7% and FRO +11.5% over their SMA20s.
- **Insiders are selling into it, and nobody is buying: FRO 0 buys. TNK 0 buys, net
  -$0.50M. INSW 0 buys, net -$42.9M sold.**
- Verdict: peak-cycle earnings, driven by a war, capitalised at 52-week highs, with
  management distributing $43M. The bull case is the rate; the rate is the risk. REJECT.
  This is the same failure shape as ETON — good numbers, insiders leaving.

## [06:52 ET] POSITION UPDATE — DHT — opened 2026-08-18 @ 18.80, last 19.99, +6.3%
- decision: **HOLD, TRIM roughly half into strength, and RAISE THE STOP from 17.60 to
  18.85** (breakeven-plus, and ~1.6 ATR below the current price; SMA20 is 18.67).
- why: the tanker work above is new information and it cuts against the position. DHT is
  -2.7% from its 120d high on day rates running at 2-2.5x cycle-peak levels that exist
  because of a war. The original 17.60 stop sits **13.6% below the market** and gives back
  the entire gain plus more before it triggers. That was sized for a normal tape.
- **explicit gap risk:** a ceasefire or de-escalation headline reprices tankers overnight
  and would gap straight through any stop. That is an argument for trimming size now,
  not for relying on the stop.
- **deliberately NOT captured as a candidate.** The correct action is to reduce risk, and
  the schema has no way to say "hold and trim" for an equity — a `buy` candidate would
  read as an instruction to add to a position I have just argued is at a cycle top.
  Consistent with how I handled every other position action today (KRE, TJX, /MBTU6, BTC):
  all exits and reductions live here in notes.md, none are dressed up as new candidates.
  **Synthesis must carry these position actions through to the report.**

## [06:51 ET] SELF-AUDIT — recomputed every R:R from the captured levels
| sym | horizon | conv | entry | target | downside | R:R | floor | pass |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TLT | swing | 3 | 82.60 | 86.20 | 80.95 (stop) | **2.18** | 2.0 | PASS |
| PPLT | long_term | 3 | 15.00 | 20.50 | 13.00 (bear) | **2.75** | 2.5 | PASS |
| PFE | long_term | 4 | 26.40 | 38.00 | 22.50 (bear) | **2.97** | 2.5 | PASS |
| GDX | long_term | 3 | 85.00 | 115.00 | 75.00 (bear) | **3.00** | 2.5 | PASS |
- CLAUDE.md records a prior live report that shipped eight R:R ratios clustered at
  2.04-2.33 against a 2.0 floor — targets nudged until they passed. **Checking myself
  against that specific failure:** the spread here is 2.18 to 3.00 and two of the four
  clear their floor by 19% and 20%. TLT at 2.18 is the tightest and it is the one I
  flagged as tightest at capture time, before computing this table.
- Where I *did* move a level, I moved the **entry down**, not the target up — PPLT ideal
  went to 15.00 (below the 50-day) and GDX to 85.00 (12% below market, marked wait:true).
  Both are demands for a better price, which is the conservative direction. Both targets
  sit **below** the instrument's own 120-day high. No target was raised to clear a floor.
- Total proposed NEW exposure: **11.5%** across 4 ideas. Deliberately modest — the book
  already carries 22 open lines and 12 of them need closing this morning.
- Venue check: all 4 are `Robinhood Stocks` (TLT, GDX, PFE are among the most liquid
  US-listed securities; PPLT independently verified at robinhood.com/us/en/stocks/PPLT).
  All 4 carry >=2 sources. No options, no OTC, nothing under $1, nothing halted.

## [06:51 ET] OPEN POSITIONS WITH NO STOP — flagged, no change recommended
- **LCII 107.70, entry 94.00, +14.6%, no stop, target 138.00** — the best line in the
  book and the only one running unprotected with a double-digit gain. Not changing the
  thesis, but a trailing stop near **99.00** (below the round number and roughly the
  prior consolidation) would protect the gain without crowding a 138 target. Flagged.
- **CCJ 97.98, entries 95.00 and 88.00, +3.1%, no stop, target 135.00** — long-term
  uranium thesis, stop legitimately absent per config/strategy.md. URA +3.2% and
  URNM +3.1% yesterday confirm the sector bid. No action.
- **NKE, PFE** — handled in the 06:43 blocks. Hold both, add to neither.

## [06:52 ET] HORIZON SKEW — stated plainly rather than papered over
- Captured: **1 swing, 3 long_term, 0 intraday.** That is the honest shape of today.
- **Nothing intraday cleared the bar.** The one same-day catalyst was WMT bmo, and I had
  no differentiated view on the number — the same reason I rejected DE, which also
  reports this morning. Per config/strategy.md I did not manufacture a mix.
- The long_term skew is not an accident of leftover time: the day's driver was a
  *currency and rates* repricing, and the durable expressions of that (PGM supply, gold
  producer cash-flow multiples) are structural claims, not price paths. The one genuine
  swing setup — TLT — is the one instrument with a dated, scheduled, mechanical flow.
- Correlation check: TLT (US duration), PPLT (PGM industrial supply), GDX (gold equity
  cash-flow multiple) all benefit from a weaker dollar. **That is exactly 3 on one broad
  driver, at the stated cap of 3 — not over it.** PFE is fully independent
  (single-name insider signal). I stopped adding hard-asset ideas for this reason and
  said so at the time, rather than discovering it here.

## [06:53 ET] INSIDER SCREEN — 16 de-rated large caps, 4 showed open-market buying
- Screened UNH CVS ELV HUM TGT SBUX LULU EL BMY MRNA DOW LYB ADM UPS CE MDT.
- Hits: **ELV** (4 buys/3 buyers/$2.24M), **LULU** (3 buys/2 buyers/$1.99M),
  HUM (1/1/$0.15M — too small), CE (2/2/$0.13M — too small). The other 12: zero.

## [06:53 ET] REJECTED — ELV (Elevance Health) — real cluster, but the entry is gone
- ELV 398.45, -8.7% off its 120d high (436.24), 120d low 274.84 — so it has already
  rallied **+45% off the low**. SMA20 387.98, SMA50 395.39: consolidating, not de-rated.
- Insiders: **CEO Gail Boudreaux 2,045 + 680 sh on 2026-07-17 at ~$366-368**, director
  Ramiro Peru 1,000 @ 366.05 the same day; Steven Collis 3,000 @ 289.84 back on 2026-03-05
  (that one is +37% and was the real signal, five months ago).
- Killed on two counts: the July cluster is **~8.8% below the current price**, so the
  actionable moment has passed; and $2.24M of buying is offset by **$1.74M of selling**,
  a 1.3:1 ratio. Compare PFE at 23:1 ($2.96M vs $0.13M). Same shape, much weaker signal.
- Liquidity was never the issue ($394M/day). Good company, stale entry. REJECT.

## [06:53 ET] LULU — de-rated quality or value trap? Both cases, then a conviction-2 call
THE CASE AGAINST (this is the stronger-looking side, so it goes first):
- **Americas comps -5% in Q1 — the FIFTH consecutive quarterly decline.** The core market
  is still deteriorating, not bottoming. Management guides FY North America revenue
  **down high single digits**.
- **Two guidance cuts this year.** FY26 sales now $11.00-11.15B, cut from $11.35-11.50B,
  and originally $12.10-12.30B. FY26 EPS guided **$10.95-11.15 vs $13.26 in FY25** — a
  ~17% earnings decline.
- Tariffs, heavier promotion, and structural competition (Alo, Vuori) — competition is
  not a cycle you wait out.
- China, the one bright spot (+30% revenue, +20% comps in Q1), is showing cracks; a Great
  Wall yoga event became a public apology.
- Barchart's headline is the honest summary: "A Lower Valuation Doesn't Fix Its Problems."
- sources: https://www.barchart.com/story/news/3324156/lululemon-stock-is-down-43-in-2026-a-lower-valuation-doesnt-fix-its-problems
  https://www.tikr.com/blog/lululemon-is-down-46-in-2026-and-its-china-engine-just-hit-a-wall-where-lulu-stock-could-go-next
  https://www.cnbc.com/2026/06/04/lululemon-lulu-earnings-q1-2026.html
THE CASE FOR:
- Down ~43-46% in 2026 to 119.45, **-36.0% off the 120d high**, on ~$11.05 FY26 EPS
  = roughly **10.8x** for a brand with genuine pricing power and 20%+ China growth.
- **Chairman Charles Bergh bought 4,275 sh @ $117.05 on 2026-06-15 — within 2% of today's
  price** — after already buying 6,090 @ $164.20 in March. He averaged down and committed
  again near the low. Bergh is the former Levi Strauss CEO, i.e. a person who has actually
  executed a heritage-apparel turnaround, betting personally. Insider sells: **$0.10M.**
  Buy:sell ratio ~20:1.
- Base is flat: price 119.45 against SMA20 120.58 and SMA50 117.70, with the 120d low of
  104.44 holding. Liquidity $308M/day. A **proxy battle** is also live (potential catalyst).
- **No earnings print inside the 10-session window** (Q1 reported Jun 4; Q2 due early Sept),
  so this is not a bet on a number — unlike DG/ULTA, which I rejected for exactly that.
CALL: capture at **conviction 2**, sized 1% as a lottery ticket per config/strategy.md.
The fundamental trend is still negative and I will not pretend otherwise; the evidence is
genuinely thin and two-sided. That is what a 2 is for, and I am not inflating it to a 3.
CONSISTENCY NOTE: I rejected DG and ULTA partly on US-consumer correlation, so I must be
straight about LULU. Its *thesis* is idiosyncratic (brand turnaround + chairman's personal
bet + proxy battle), but its *key risk* is squarely the US consumer. With TJX's four lines
closing today, consumer exposure is HD x3 (housing/rates-driven) + LULU. I judge that
inside the cap, but it is the closest call I have made today and it is stated, not buried.

## [06:55 ET] RESEARCH COMPLETE (supersedes the premature block written earlier)
The earlier "RESEARCH COMPLETE" above was written under mis-estimated timestamps and is
void. This is the real one. Research ran 06:32:47 - 06:55 ET.

**candidates: 5 unique** (6 lines in candidates.jsonl; TLT appears twice, the second
entry supersedes the first with primary-source Treasury detail — take the last per symbol)

| sym | horizon | conv | entry | target | downside | R:R | floor | size | wait |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TLT | swing | 3 | 82.60 | 86.20 | 80.95 stop | 2.18 | 2.0 | 3% | no |
| PPLT | long_term | 3 | 15.00 | 20.50 | 13.00 bear | 2.75 | 2.5 | 2.5% | no |
| PFE | long_term | 4 | 26.40 | 38.00 | 22.50 bear | 2.97 | 2.5 | 3% | no |
| GDX | long_term | 3 | 85.00 | 115.00 | 75.00 bear | 3.00 | 2.5 | 3% | **yes** |
| LULU | long_term | 2 | 112.00 | 160.00 | 96.00 bear | 3.00 | 2.5 | 1% | **yes** |

- Total NEW exposure **12.5%**. Horizons: 4 long_term, 1 swing, **0 intraday** (nothing
  intraday cleared the bar — see the 06:52 skew block; not manufactured).
- Two ideas are marked **wait: true** — GDX (needs a ~12% pullback) and LULU (accumulate
  below the chairman's $117.05 print). Both may never fill. That is intended.

**POSITION ACTIONS — these matter more than any new idea and must reach the report:**
- **CLOSE, stops breached (12 of 22 open lines):** KRE x4 (last 75.00 vs stops 75.4/75.2/74.2),
  TJX x4 (144.50 vs 146.5/145.5), /MBTU6 short x2 (BTC 71,905 gapped through 66,600),
  BTC spot sell x2 (thesis dead).
- **DHT:** hold, **trim ~half**, raise stop 17.60 -> 18.85. Tanker rates are 2-2.5x
  cycle-peak on a war premium; insiders across the sector sold and bought nothing.
- **LCII:** +14.6% and unprotected — suggest a trailing stop near 99.00.
- **NKE x2:** hold, do not add. The 4-buyer insider cluster is April, at $42-43, underwater.
- **PFE:** hold, do not add above 27.20 (captured as a continuing position, not a new idea).
- **CCJ x2, XLE x3, HD x2, BCC:** no action, all comfortably above stops.

**coverage gaps:**
- **Event contracts — nothing usable.** Six Kalshi queries returned count 0 or irrelevant
  markets (a "gold" query returned Korean baseball parlays). No event candidate; I did
  not invent an implied probability.
- **Biotech/FDA** — no ticker-level PDUFA dates retrievable inside budget.
- **No live platinum spot price**; PPLT's target is anchored to its own 120d range, and
  PPLT's **10-for-1 forward split** means any pre-split price comparison is wrong by 10x.
- **All index quotes failed** — every index figure in this file is an ETF proxy.
- Intraday setups, small caps beyond ETON, and the Aug 26-27 earnings cohort were
  examined and rejected with reasons logged, not skipped.

**sources that failed:** finnhub index quotes (CFD subscription required), yahoo (HTTP 429
on every index symbol), stooq (404 on ^-prefixed symbols), alphavantage (no API key),
kalshi events search (0 or mismatched results across 6 queries).
**sources that worked:** home.treasury.gov (primary, sb0607), FRED, nasdaq OHLCV,
finnhub (equity quotes, earnings calendar, insider transactions), SEC EDGAR filings,
coingecko.

**process note for the next run:** I mis-estimated elapsed time badly in the first half of
this session, labelling blocks up to 35 minutes ahead of the real clock, because I trusted
my sense of it instead of calling `date`. It cost nothing here — I caught it with ~30
minutes still on the clock and used them to add GDX, LULU, the full position sweep and the
tanker work — but had it run the other way I would have stopped early believing I was out
of time. **Call `date` every few tool calls, not once at the start.**
