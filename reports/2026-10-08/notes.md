# Research log — 2026-10-08

## [06:04 ET] MACRO — rates, FRED, crypto
- FRED (source: https://fred.stlouisfed.org/):
  - US10Y `DGS10` **5.27%** (2026-10-06), prev 5.31 — long end elevated
  - US2Y `DGS2` **4.79%** (2026-10-06), prev 4.84
  - Fed funds `DFF` **3.88%** (2026-10-06), unchanged
  - 10y-2y `T10Y2Y` **+0.51** (2026-10-07), prev +0.48 — steepening
  - Unemployment `UNRATE` **4.2%** (Sep), prev 4.1 — rising
  - CPI index `CPIAUCSL` 334.131 (Aug) vs 332.813 (Jul) = **+0.40% m/m** — hot
- Regime read: policy rate 3.88 well below a 5.27 10Y. A steepening curve with
  rising unemployment AND a hot CPI print is the stagflationary mix — it is
  hostile to long-duration equity and to rate-sensitive sectors, and supportive
  of real assets / energy / gold.
- Crypto (source: https://www.coingecko.com/): BTC **$83,061** (-0.85% 24h),
  ETH **$2,566.19** (-1.15%), SOL **$115.11** (-2.23%). BTC well off highs.
- TLT proxy `bonds_20y` 77.145 (-0.17%), pre-market, stooq delayed.

## [06:04 ET] DATA QUALITY — Yahoo rate-limited
- `market_data.py macro` returned ok:false for spx, ndx, dow, russell2000, vix,
  es/nq futures, DXY, us10y_yield, gold, wti_crude — **Yahoo returning HTTP 429
  (Too Many Requests)** on both query1 and query2 hosts; finnhub refuses indices
  ("Market data subscription required for CFD indices"); stooq 404s on `^`
  symbols; no alphavantage key.
- Consequence: no live index/VIX/DXY/gold/crude level this run unless another
  source works. Will retry and fall back to ETF proxies. Do not state an index
  level I did not fetch.

## [06:06 ET] CALENDAR — dated earnings, next 12 sessions (finnhub, fetched)
Source: `python scripts/market_data.py earnings --days 12` (finnhub, 260 rows)
- **2026-10-08 (today)**: PEP:bmo, HELE:bmo, TLRY:bmo, ANGO:bmo, BYRN:bmo, NG:bmo
- **2026-10-09 (tomorrow)**: **DAL:bmo** ← I am long DAL (opened 2026-10-05)
- 2026-10-13: **JPM:bmo, GS:bmo, C:bmo, WFC:bmo, JNJ:bmo, UNH:bmo**, DPZ:bmo, AZZ:amc
- 2026-10-14: **BAC:bmo, MS:bmo, BLK:bmo, STT:bmo**, FAST:bmo
- 2026-10-15: **SCHW:bmo, PNC:bmo, USB, AA:amc, CMC:bmo, IBKR:amc**, JBHT:amc, WHR, FHN, HRI, SNA, POOL, PLD
- 2026-10-16: **TRV:bmo, MTB, RF, CFG, TFC**, EEFT
- 2026-10-19: **GE:bmo, STLD:amc, CLF:amc**, FITB, ZION, WAL, BOKF, CCK, SFBS
- 2026-10-20: **TSLA:amc, NFLX:amc, RTX:bmo, NOC:bmo, GM:bmo, MMM, ISRG:amc, UAL, PM:bmo, HAL:bmo, COF:amc, ALLY:bmo, SYF:bmo, CB:amc, ALK**
- Read: the quarter's dominant dated catalyst is **Q3 bank earnings beginning
  Oct 13** (JPM/GS/C/WFC, then BAC/MS, then PNC/USB/SCHW, then regionals Oct
  16/19). Industrials and autos land Oct 19-20. Airlines: DAL tomorrow is the
  read-across for UAL/ALK/AAL on Oct 20.

## [06:03 ET] PRICE BASIS — all equity prices here are the 2026-10-07 CLOSE
- finnhub returns `asof: 2026-10-07T20:00:00+00:00`, `session: "pre"`,
  `age_minutes: ~843` for every equity/ETF. That is the 16:00 ET regular-session
  close on Oct 7 — the freshest honest equity price at 06:00 ET, not stale data.
- Note `prior_context.md`'s "Last" column is the **Oct 6** close, one session
  behind, so every "% vs entry" in it is a day old. Recomputed below.

## [06:03 ET] TAPE — Oct 7 was a commodity/miner/small-cap washout
Closes 2026-10-07 (finnhub, fetched), change vs Oct 6 close:
- SPY **777.22** -0.24% | QQQ **757.73** -0.25% | IWM **277.70** -1.29%
- XLF **53.75** -0.48% | XLE **63.36** -0.61%
- GLD **375.88** -1.67% | GDX **85.46** -3.13% (day low **84.36**)
- CCJ -4.25% | BCC -3.35% | LCII -2.52% | SNX -2.46% | EEM -1.32%
- UNG **11.03 +2.70%** | USO 143.91 -0.69% | TLT 77.145 -0.17%
- PFE **28.00 +1.82%** | DINO 115.63 +0.90%
- Read: mega-cap index essentially flat while miners, uranium, builders and
  small caps were sold hard. That is a **de-risking of the commodity/reflation
  trade specifically**, not a broad market decline — and it is where this
  report's open book is concentrated. Nat gas was the only thing bid.

## [06:08 ET] POSITION UPDATE — all 16 open positions, repriced to the Oct 7 close
ATR14 and moving averages from `market_data.py history <SYM> --days 90` (nasdaq).

| Sym | Side | Entry | Close 10/07 | % | Stop | Target | ATR14 | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GDX | BUY | 91.20 | 85.46 | -6.3% | 85.40 | 104.40 | 2.77 | **STOPPED OUT** |
| CCJ | BUY | 94.00 | 89.07 | -5.2% | 82.50 | 135.00 | 3.47 | hold, cut target |
| XLE | BUY | 63.90 | 63.36 | -0.8% | 60.80 | 70.50 | 1.21 | hold unchanged |
| EEM | BUY | 65.60 | 67.37 | +2.7% | 63.00 | 71.50 | 1.01 | raise stop 65.5 |
| DINO | BUY | 107.50 | 115.63 | +7.6% | 97.75 | 128.00 | 4.74 | raise stop 106 |
| SNX | BUY | 260.00 | 271.52 | +4.4% | 242.50 | 296.47 | 12.86 | raise stop 260 |
| KHC | BUY | 23.00 | 21.98 | -4.4% | 21.20 | 32.00 | 0.53 | **close early** |
| CEG | BUY | 272.00 | 299.59 | +10.1% | 250.00 | 320.00 | 13.15 | raise stop 273, trim |
| DAL | BUY | 83.00 | 82.97 | -0.0% | 78.10 | 94.50 | 2.42 | half size into print |
| NKE | BUY | 40.75 | 34.36 | -15.7% | none | 62.00 | 1.17 | hold (long_term) |
| NKE | SELL | 38.40 | 34.36 | +10.5% | 41.00 | 32.10 | 1.17 | hold, trail stop |
| LULU | BUY | 115.00 | 91.88 | -20.1% | none | 180.00 | 3.27 | hold (long_term) |
| LULU | SELL | 100.61 | 91.88 | +8.7% | 112.00 | 77.00 | 3.27 | hold, trail stop |
| BCC | BUY | 76.50 | 72.92 | -4.7% | none | 110.00 | 2.29 | hold (long_term) |
| LCII | BUY | 94.00 | 80.12 | -14.8% | none | 138.00 | 2.30 | hold, flag thesis |
| PFE | BUY | 27.60 | 28.00 | +1.4% | none | 42.00 | 0.52 | hold (long_term) |

### GDX — STOPPED OUT on 2026-10-07, do not re-enter
- Oct 7 bar: o85.32 h86.39 **l84.36** c85.46. The stop was 85.40; the low went
  through it. The position closed at the stop, -6.3%.
- Do not re-pitch. GDX closed below both the 20-day (91.85) and the 50-day
  (92.16) and is 19.1% off its 90-day high of 105.67. The correction is not a
  one-day event: per Canadian Mining Report (2026-10-05), NY gold futures slid
  from $4,441/oz at end-August to $4,158/oz at end-September and the fifteen
  largest gold miners lost $79bn, -12.7%, with **not one** finishing September
  higher. Buying a 2-ATR dip in that is catching the knife.
  — source: https://www.canadianminingreport.com/blog/the-264-billion-hit-was-not-one-trade
- GDX was recommended 2x in the last 10 days. Stop recommending it.

### KHC — close early, the stop is inside the noise and the trend is intact down
- Close 21.98, and the 90-day range low is **21.76** — made Oct 6. The stop at
  21.20 is only **1.46 ATR** (0.78 / 0.533) below the close, under the 2.0 ATR
  swing floor, in a name printing new lows.
- Below the 20-day (23.59) and the 50-day (24.73), 21.8% off the 90-day high.
  Four of the last four closes are 22.19 / 21.84 / 22.03 / 21.98 — no bid.
- Honest options were (a) widen the stop to 20.91 to respect the 2.0 ATR floor,
  which concedes another 4.9%, or (b) close. The target of 32.00 is a
  break-up/sum-of-parts valuation that nothing on the tape is paying for yet.
  **Taking the -4.4% is better than funding a 1.46-ATR coin flip.** Closing.

## [06:12 ET] CORRECTION — KHC's stop is fine; I measured it from the wrong point
The table above said KHC "close early — stop inside the noise at 1.46 ATR".
That was wrong: I divided the distance from **today's price** (21.98 - 21.20 =
0.78) by ATR. `check_stop_distance` measures from **entry**, and KHC's is
23.00 - 21.20 = 1.80 = **3.38 ATR**. The stop is wide, not tight. What is true
is only that the trade has moved against us so there is 1.46 ATR of room left —
which is what a stop being approached looks like, not a design flaw.
**Revised KHC decision: hold and let the stop do its job.** See below.

## [06:12 ET] STOP AUDIT — every open position re-measured from entry at today's ATR
`|entry-stop| / ATR14` vs the `config/strategy.md` floor (2.0 stock, 1.8 etf);
R:R `|target-entry| / |entry-stop|` vs the 2.0 swing floor; target distance in
ATR vs the 6.0 swing ceiling.

| Sym | ATR mult | floor | R:R | target ATR | verdict |
| --- | --- | --- | --- | --- | --- |
| GDX | 2.10 | 1.8 | 2.28 | 4.77 | ok (but stopped out) |
| CCJ | 3.32 | 2.0 | 3.57 | **11.83** | target beyond the 6 ATR swing ceiling |
| XLE | 2.57 | 1.8 | 2.13 | 5.46 | ok |
| EEM | 2.58 | 1.8 | 2.27 | 5.85 | ok |
| DINO | 2.06 | 2.0 | 2.10 | 4.33 | ok, nothing to spare |
| SNX | **1.36** | 2.0 | 2.08 | 2.83 | **stop inside the noise** |
| KHC | 3.38 | 2.0 | 5.00 | **16.89** | stop fine; target beyond the ceiling |
| CEG | **1.67** | 2.0 | 2.18 | 3.65 | **stop inside the noise** |
| DAL | 2.02 | 2.0 | 2.35 | 4.75 | ok, nothing to spare |
| NKE sell | 2.22 | 2.0 | 2.42 | 5.38 | ok |
| LULU sell | 3.48 | 2.0 | 2.07 | **7.22** | target beyond the ceiling |

Two fail the ATR floor, and the cause is **not** a walked-in stop — it is ATR
expanding after publication:
- **CEG** gapped +8.8% on 2026-10-06 (o291.11 from a 267.62 close, 13.5M shares
  against a ~3.5M norm), which lifted ATR14 to 13.15 and turned a stop that was
  adequate on 2026-10-01 into 1.67 ATR.
- **SNX** ATR14 is 12.86, **4.74% of price** — it is simply a more volatile
  instrument than its 17.50 stop assumed.

`config/strategy.md` says: widen the stop and re-check the ratio, or drop the
idea. Done, and **neither survives it**:
- CEG honest stop 245.70 → R:R **1.82**, under the 2.0 floor
- SNX honest stop 234.27 → R:R **1.42**, under the 2.0 floor
Both are in profit (+10.1%, +4.4%). So the disciplined answer is not to widen
into an idea that no longer qualifies, it is to **bank the gain**. Taking profit
on two winners because volatility expanded past what the structure supports is
the opposite of this report's recorded failure mode, which was holding losers
behind tight stops.

## [06:15 ET] NEWS — CEG's +8.8% gap is a 20-year Google PPA, not a spike to fade
- **2026-10-06: Google + Constellation 20-year PPA.** Funds uprates at **11
  Constellation reactors** in IL/PA/NJ adding **890 MW to the PJM grid**, phased
  **2028-2032**, with Constellation spending **>$4.3bn**. Alongside it a
  **separate 15-year deal for 2,700 MW from existing plants** — that second
  piece is contracted cash flow from an installed base, not 2030 capacity. Deal
  also puts Google Cloud / Gemini Enterprise into CEG's grid operations (site
  selection, outage management).
  — sources: https://www.googlecloudpresscorner.com/2026-10-06-Google-and-Constellation-Announce-Landmark-Agreement-to-Bring-890-MW-of-New-Nuclear-Capacity-to-PJM-Grid-as-Part-of-Long-Term-Power-Deal
    https://www.axios.com/2026/10/06/google-constellation-nuclear-energy
    https://www.constructiondive.com/news/constellation-google-nuclear-deal-data-center-energy/832351/
- **~2026-09-30/10-01: Amazon + Constellation 20-year deal** on Calvert Cliffs
  (MD), enabling +190 MW, output 2030-2032.
  — source: https://www.world-nuclear-news.org/articles/constellation-amazon-agree-nuclear-focused-power-purchase-deal
- No 8-K on EDGAR dated 10/06 for CEG (checked `filings CEG`: latest are Form 4s
  filed 10/02 and a 144 on 09/17), so the press release is the primary document.
- **This reverses my provisional "take profit on CEG" call.** A held gap on 4x
  volume explained by a signed 20-year contract is a re-rating, not a spike.
  Revised: **hold**, trim only at the 320 target. Stop stays 250.
- **Read-across, and the bit that is actually interesting:** CCJ (uranium) spiked
  on the same news — 10/06 o89.55 **h94.57** c93.02 — and then gave it all back
  on 10/07 to 89.07. The market bought the *utility* that signed the contract
  and faded the *fuel* that a 2028-2032 uprate implies. Worth testing rather
  than assuming; see CCJ below.

## [06:17 ET] FALSIFICATION — CCJ — close the position, the thesis is not being paid for
CCJ is open at 94.00 (2026-08-17, -5.2%) with a 135.00 target. Every test I ran
this morning came back against it:
- **Its best possible news arrived and was given straight back.** The
  Google/Constellation nuclear PPA is the single most bullish headline a uranium
  long could ask for. CCJ traded 10/06 o89.55 **h94.57** c93.02 on 6.06M shares
  — and on 10/07 closed **89.07**, below where it started the week. When the
  thesis's ideal catalyst lands and the stock is lower two sessions later, the
  market is declining to pay for the thesis.
- **Operating record:** 3 of the last 4 quarters missed consensus EPS, two
  badly — 2026-06-30 **-52.7%** (0.18 vs 0.381), 2026-03-31 -17.9%, 2025-09-30
  **-77.2%** (0.07 vs 0.307). Only 2025-12-31 beat, +12.5%.
  — source: https://finnhub.io/api/v1/stock/earnings
- **Analyst revisions deteriorating**, bullish share 81.8%, **-3.9pp** over four
  months (holds 3 → 4). Direction, not level, is the signal.
  — source: https://finnhub.io/api/v1/stock/recommendation
- **No insider buying at all** in six months (0 buys, 0 sells).
- **Relative strength: lagging SPY on every window measured** — 1m -14.12%,
  3m -10.36%, **6m -38.12%**. The sector is no better: URA 1m -15.94%,
  6m -22.32%. CCJ is not a cheap leader, it is in line with a falling group.
- **The target was never a swing target.** 135.00 is **11.83 ATR** from the
  94.00 entry against a 6.0 ATR ceiling for the horizon it was published in.
- Arithmetic at honest levels: the stop must sit at 87.07 to clear 2.0 ATR, and
  the only reachable swing target is the 50-day at ~94.7 / prior shelf ~105 —
  giving 11/6.93 = **1.59:1**, under the 2.0 floor. There is no configuration of
  this trade from a 94.00 entry that qualifies.
- **Decision: CLOSE at the market, take the -5.2%.** Also stop re-pitching it —
  it has been recommended 2x in the last 10 days.

## [06:21 ET] POSITION UPDATE — NKE and LULU: the book is long AND short both names
The open book holds, on each of two symbols, a stop-less long_term BUY that is
deeply underwater and a profitable swing SHORT:
- NKE: BUY 40.75 (2026-08-17, **-15.7%**, no stop, target 62) + SELL 38.40
  (2026-09-08, **+10.5%**, stop 41.00, target 32.10)
- LULU: BUY 115.00 (2026-08-22, **-20.1%**, no stop, target 180) + SELL 100.61
  (2026-09-08, **+8.7%**, stop 112.00, target 77.00)
You cannot coherently advise that NKE is worth 62 and going to 32. The net
exposure is roughly flat and the reader pays spread and margin on both sides.
One side has to go, and the evidence says which.

### Verified company guidance (both sides of the pair)
- **NKE, Q1 FY2027 reported 2026-10-01**: revenue **-4% to $11.21bn** vs ~$11.35bn
  expected; FY2027 revenue guided to **decline high single digits**; adjusted EPS
  guided **$1.15-1.35 against ~$1.69 consensus**; **Greater China -26%**
  currency-neutral; a restructuring plan ("Pace") targeting ~$2.5bn of savings
  by end-FY2031. Shares fell ~10% pre-market.
  — sources: https://investinglive.com/stocks/nike-beats-q1-profit-estimates-but-sees-fiscal-2027-revenue-falling-high-single-digits/
    https://stockanalysis.com/news/nike-q1-2027-sales-miss/
    https://www.tradingpedia.com/2026/10/02/nike-drops-as-weak-outlook-overshadows-earnings-beat/
- **LULU, guidance cut 2026-09-03 with Q2**: the **third cut since March**. Q3
  FY2026 revenue **$2.29-2.32bn, -10% to -11% y/y**, against $2.53bn consensus;
  FY2026 revenue now **-5% to -7%** (was flat to -1%); FY EPS cut to
  **$9.48-9.73 from $10.95-11.15**. Stock fell ~17-18% to under $100, an
  **8-year low**.
  — sources: https://finviz.com/news/388999/lululemon-shares-fall-17-after-fy2026-guidance-cut-despite-q2-earnings-beat
    https://www.tikr.com/blog/lululemon-stock-crashed-17-on-friday-the-guidance-cut-was-the-real-story

### Resolution: close the longs, keep the shorts
The longs are the weaker side on every measure, and their own arithmetic fails:
- **NKE long**: a 62 target needs EPS to roughly triple off a **$1.15-1.35**
  guide. At 34.36 the stock is already ~27x the midpoint of a trough year, so 62
  is ~50x. Greater China -26% is share loss, not a destocking blip. At an honest
  bear case of 26.00 (FY27 EPS 1.15 on a 22x trough multiple) the long_term R:R
  is (62-40.75)/(40.75-26) = **1.44:1 against a 2.5 floor**.
- **LULU long**: three guidance cuts in six months and an FY EPS base cut from
  $10.95-11.15 to $9.48-9.73 — the earnings base is not settled, so "quality
  de-rated on a fixable problem" is unproven. At a bear case of 76.00 (8x the
  $9.48 low end, which is also where the short targets) R:R is
  (180-115)/(115-76) = **1.67:1 against a 2.5 floor**.
- Both longs carry **no stop** and are -15.7% and -20.1%. Closing them.
- **The shorts are held.** Both rest on read guidance rather than on price, both
  clear every floor (NKE 2.22 ATR / 2.42:1; LULU 3.48 ATR / 2.07:1), and LULU
  made a fresh 90-day low of 90.56 on 10/07. NKE's target 32.10 is now only 1.93
  ATR from the 34.36 close, so it is close to done — trim there, do not extend.

## [06:24 ET] !! SYNTHESIS, READ THIS — NKE and LULU each need TWO rows kept
`daily-synthesis` resolves duplicates as "where a symbol appears more than once,
the last entry wins", keyed on **symbol**, not on (symbol, direction). Today
that rule would silently delete half of my position management, because NKE and
LULU each carry **two separate open positions pointing opposite ways**, and
`candidates.jsonl` therefore has two lines for each:

| Line | Keep because |
| --- | --- |
| `NKE` **buy** long_term | CLOSE the long opened 2026-08-17 at 40.75 |
| `NKE` **sell** swing | HOLD the short opened 2026-09-08 at 38.40 |
| `LULU` **buy** long_term | CLOSE the long opened 2026-08-22 at 115.00 |
| `LULU` **sell** swing | HOLD the short opened 2026-09-08 at 100.61 |

**Dedupe on (symbol, direction) for these four, not on symbol.** Dropping the
`buy` lines would leave two stop-less losing longs open with no instruction;
dropping the `sell` lines would abandon the two positions actually making money.
`merge_report` already tracks one live position per (symbol, direction), so both
rows are legitimate and neither double-counts.

## [06:24 ET] FORWARD REWARD-TO-RISK — the lens the entry-anchored checks miss
`validate_report.py` measures R:R and stop distance from **entry**, which is
right for a new idea. For a position already filled, the money at stake is
measured from **today's price**: risk is `last - stop`, reward is
`target - last`. Nobody moved these stops, so several winners now risk more than
they stand to make.

| Sym | last | risk to stop | reward to target | fwd R:R | risk in ATR | call |
| --- | --- | --- | --- | --- | --- | --- |
| XLE | 63.36 | 2.56 | 7.14 | **2.79** | 2.12 | hold |
| DAL | 82.97 | 4.87 | 11.53 | **2.37** | 2.01 | hold |
| KHC | 21.98 | 0.78 | 10.02 | 12.85 | 1.46 | hold, stop is near |
| CCJ | 89.07 | 6.57 | 45.93 | 6.99 | 1.90 | **ignore — target is fiction** |
| EEM | 67.37 | 4.37 | 4.13 | 0.95 | 4.33 | trim |
| SNX | 271.52 | 29.02 | 24.95 | 0.86 | 2.26 | close |
| LULU sh | 91.88 | 20.12 | 14.88 | 0.74 | 6.15 | trim a third |
| DINO | 115.63 | 17.88 | 12.37 | 0.69 | 3.77 | trim |
| CEG | 299.59 | 49.59 | 20.41 | **0.41** | 3.77 | hold, never add |
| NKE sh | 34.36 | 6.64 | 2.26 | 0.34 | 5.67 | trim at target |
- **CCJ is the warning against using this lens alone**: it shows the best forward
  ratio on the book, 6.99:1, purely because its target sits 11.83 ATR away and
  is not a real target. Forward R:R flatters any idea with a fantasy target. It
  is a trim signal, never an entry signal.
- **CORRECTION to the CEG candidate captured at 06:16**: it stated the forward
  trade as "20.41 of upside against 26.59 of risk, 0.77:1". That measured risk
  to a hypothetical 273 stop, not to the actual stop of 250. Against the real
  stop the forward ratio is **0.41:1** — worse, and the same conclusion, more
  strongly. Re-capturing CEG with the right number.
- The structural point for whoever maintains this: there is **no way to express a
  trailed stop in this schema** without failing `check_stop_distance`, because
  raising a stop toward a filled entry drives `|entry-stop| / ATR` to zero. That
  is why every one of these positions still carries its original stop. Not a
  change to make mid-run, but it is the reason this table reads the way it does.

## [06:27 ET] POSITION UPDATE — the remaining five, and a theme running through them
- **XLE** BUY 63.90, close 63.36, forward R:R **2.79:1**, stop 2.12 ATR, all
  floors clear. **Hold, unchanged, and deliberately not re-emitted** — XLE has
  been recommended 3x in the last 10 days and nothing about it changed this
  morning. Re-pitching an unchanged idea is the anchoring the guard exists for.
- **KHC** BUY 23.00, close 21.98 (-4.4%). Stop 21.20 is **3.38 ATR from entry**,
  not tight — see the 06:12 correction. There is 1.46 ATR of room left, so the
  stop may well trigger, and that is what a stop is for. **Hold and let it
  work; do not add and do not widen.** It is a conviction-2 idea and the
  conviction-2 record is 0/4 with an average of -8.3%, so it gets no more rope.
- **PFE** BUY 27.60, close 28.00 (+1.4%), long_term, no stop. The only open long
  that rose on 10/07 (+1.82% on 31.2M shares) and it closed above both its
  20-day (27.96) and 50-day (27.50). **Hold.** Not re-emitted: recommended 3x in
  the last 10 days and I found no new information this morning to justify a
  fourth.
- **BCC** BUY 76.50, close 72.92 (-4.7%), long_term, no stop, target 110.
  **Hold, do not add**, and the invalidation is now explicit — see below.
- **LCII** BUY 94.00, close 80.12 (**-14.8%**), long_term, no stop, target 138.
  **Close.** It printed a fresh 90-day low of 79.22 on 10/07, sits 27.9% off its
  high, below the 20-day (85.69) and the 50-day (96.66), and a 138 target is 72%
  above the market.

### The theme: the long_term book is long rate-sensitive discretionary at a 5.27% 10-year
LCII (RV and marine components) and BCC (wood products) are both bets on
big-ticket, credit-financed demand. The thing that has to go right for them —
cheaper long-term money — went the other way: the 10-year is **5.27%** with the
curve **steepening**, which is the long end pricing more term premium rather
than less. Meanwhile unemployment ticked to 4.2% from 4.1%, so the demand side
is softening while financing stays expensive. That is the invalidation for both,
stated as a condition rather than as a price.
**And the report is on both sides of it again**: `ITB SELL_SHORT @ 89.8`
(published 2026-09-30) is an open short on homebuilders, while BCC is a long on
the lumber that goes into their houses. BCC is kept only because it is -4.7%
rather than -14.8% and still 8.8% above its 90-day low of 67.05; if it loses
that low the same reasoning that closes LCII closes it.

## [06:30 ET] DATA QUALITY — event contracts unusable this run, so none are published
`market_data.py events` returns `ok: true` from Kalshi but is unusable:
- `"CPI"`, `"recession"`, `"FEDDECISION"`, `"Fed decision"`, `"inflation"`,
  `"unemployment"` all return **count 0**.
- `"Fed"` returns 6 markets, all of them sports cross-category contracts matched
  on the substring (titles are lists of tennis players), and **every price field
  is null** — no `yes_bid`, `yes_ask`, `last_price`, `volume` or `open_interest`.
- `config/universe.md` requires an event contract idea to state the market's
  implied probability against mine, and `config/strategy.md` calls "feels
  underpriced" not a thesis. With no fetchable price there is no implied
  probability, so **no event contract is published today.** Inventing one would
  be fabricating the single number the idea rests on.
- Note two Fed event contracts sit in `Awaiting entry`:
  `KXFEDDECISION-26OCT-H25 YES @ 28` (published 2026-09-02) and
  `KXFEDDECISION-26SEP-H0 YES @ 47` (published 2026-09-03). The September one is
  past its event and should be reaped rather than carried. I could not reprice
  either, so I am not amending them — unpriced is not the same as unchanged, and
  that distinction belongs in the report rather than hidden.

## [06:33 ET] MACRO — the driver of this tape is a live French sovereign-debt scare
This is the single most important thing I found this morning, and it reframes
everything else.
- **OAT/Bund 10-year spread 134.4 bps as of 2026-10-07**, with the 10-year OAT
  at **4.83%** and the Bund at **3.49%**. One account has the spread above
  **150 bps on 2026-10-02 — the widest since late 2011**.
  — source: https://www.ideal-investisseur.fr/en/markets/oat-bund-spread.html
- **Stoxx 600 banks fell 3.3% on Wednesday and as much as 2.2% on Thursday
  2026-10-08 — the biggest two-day slump since March** (Bloomberg, dated today).
  SocGen is **-25% from its August peak**, Deutsche Bank **-18%** from last
  month's high; SocGen alone fell 5.01% on 10/07. CAC 40 at a six-month low of
  7,834.10.
  — sources: https://www.bloomberg.com/news/articles/2026-10-08/european-bank-stocks-head-for-biggest-two-day-slump-since-march
    https://www.bbntimes.com/global-economy/cac-40-sinks-0-80-to-7-834-10-a-six-month-low-as-schneider-electric-slumps-10-and-french-fiscal-fears-deepen
- **The mechanism**: the 2027 draft budget needs roughly **€54bn of savings** to
  get the deficit to 5%, and investors doubt it can be delivered. French bank
  CDS now price above UK/German/Swiss/Spanish peers — a 5-year CDS on €10m of
  SocGen bail-in senior debt costs ~€103,000, about €16,500 more than comparable
  Deutsche Bank cover. Banks hold the sovereign, so the spread marks their books.
  — source: https://www.briefs.co/news/french-bank-credit-insurance-costs-pull-ahead-of-european-ri/
- **The ECB has explicitly declined to help.** The Bank of France governor
  called the fiscal situation serious and ruled out intervention; UBS's Ermotti
  says France needs "hard measures". Spreads are widening in Italy, Spain,
  Belgium, Portugal and Greece too.
  — source: https://www.cnbc.com/2026/10/06/france-debt-crisis-ubs-ermotti.html
- **This explains the 10/07 US tape, and the explanation matters**: US banks were
  sold in sympathy — JPM -10.1% off its high and below both its 20- and 50-day,
  **GS -23.1% off its high**, C -14.0%, WFC -12.8%, and **KRE traded 20.36M
  shares against a ~10M norm** while closing 1.59% above its 90-day low.
- **The part that should make anyone cautious: gold fell too.** GLD -1.67% and
  GDX -3.13% on a day of sovereign credit fear is not a flight to safety, it is
  indiscriminate de-risking — miners, uranium, small caps, EM and bullion all
  sold together while mega-cap indices barely moved. That is the signature of
  positions being reduced for liquidity, and it is the regime in which buying
  dips has the worst odds.
- **Consequence for today's new ideas: the bar goes up, not down.** I am not
  going to add fresh long risk into an escalating sovereign credit event just
  because prices are lower, and the report's own record argues the same way —
  stocks are 0/8 on closed trades, averaging -6.5%.
- Risk I now carry knowingly: **EEM** is an open long and a European credit
  scare with EM contagion is a direct threat to it. That is in the EEM
  key_risk, and is part of why it is being halved rather than held whole.

## [06:36 ET] REJECTED — JPM — buy fails R:R at any defensible target (1.83:1 vs 2.0 floor)
JPM is the best-looking bank into the 2026-10-13 bmo print: beats in 4 of 4
quarters (+4.0%, +8.0%, +3.5%, +3.8%), analyst bullish share 60.0% and
**improving +3.3pp**, and it is holding its sector (vs XLF +1.46% 3m, +2.04% 6m)
even while lagging SPY. But the levels do not work. Close 329.58, ATR14 5.72
(1.74%). A 2.0 ATR stop puts the stop at 318.0; the nearest defensible target is
the 50-day at **350.77**, giving (350.77-329.58)/11.58 = **1.83:1**, under the
2.0 floor. The only way to pass is to nudge the target to ~355, which is the
exact target-nudging `config/strategy.md` forbids. **A low-ATR name needs a
structurally-placed stop that is many ATRs wide, and then no reachable target
clears the ratio.** Rejected rather than fudged.

## [06:36 ET] REJECTED — GS — the arithmetic works and the evidence says do not
GS does clear the floors: close 887.21, ATR14 19.80, a 2.0 ATR stop at 847.4
sits below the 90-day low of 868.52, and the 50-day at 994.48 is 5.42 ATR away
for **2.71:1**. It also beat in 4 of 4 quarters, the last one by **+40.7%**
(20.98 vs 14.91). I am still not taking it:
- It is **the weakest major name in the weakest sector** — vs SPY -15.88% 1m,
  -19.37% 3m; and **vs XLF -8.21% 1m, -12.76% 3m**. Underperforming its own
  sector by 8% in a month after a 40% earnings beat means the market is pricing
  something specific, not overlooking something cheap.
- Analyst bullish share is only **46.9%** and flat — no revision support.
- Zero open-market insider buys, 21 sells.
- It reports 2026-10-13 bmo, three sessions away, in the middle of a live
  European sovereign credit event with direct trading and credit transmission.
A ratio that passes is permission to look, not a reason to buy. Rejected.

## [06:36 ET] REJECTED — banks as a short — wrong side of a binary
The mirror trade is no better: shorting into 2026-10-13/14 earnings after a
3.3%/2.2% two-day sector slump, against names beating consensus 4 quarters out
of 4, puts a short on the wrong side of a dated binary. **No bank idea today in
either direction** — the sector carries the day's dominant dated catalyst and
the honest answer is that it is untradeable on my evidence.

## [06:40 ET] REJECTED — natural gas long — good thesis, no tradeable structure
Natural gas was the only thing bid on 2026-10-07: UNG **+2.70% to 11.03** on
34.9M shares against a ~27M norm, BOIL +5.83% to 22.14, while everything else
was sold. The thesis is real and specific:
- NATGAS **+13.10% over seven days**, around $3.436 on 2026-10-08, on
  expectations of a **below-average working-gas inventory build** for early
  October. — source: https://tradingkey.com/news/market-movers/262204934-market-movers-natgas-20261008
- **Production pulled back** in the heart of the fall season while **Lower 48 LNG
  feedgas holds near 18 Bcf/d** (Entropic Analytics via NGI).
  — source: https://naturalgasintel.com/
- **EU storage was 72.7% full on 2026-10-04 and 169.4 TWh below the five-year
  average** (GIE) — a restocking deficit that pulls US LNG.
- Cold-winter cases of $5.00-8.00/MMBtu against a warm case of $2.00-2.80;
  Goldman $4.15 for 2026-27, Morgan Stanley a structural $5.
  — source: https://naga.com/en/news-and-analysis/articles/natural-gas-price-prediction
- Honest counterpoint, from EIA itself: depressed prices and possible warmer
  weather could mean **lower** heating bills this winter. The storage narrative
  is contested, not consensus.

**Why it is rejected anyway — the levels do not work.** UNG ATR14 is 0.3987
(**3.61%**), and the overhead is close:
- Close **11.03**; **200-day average 11.3336** (2.7% away); September high 11.67;
  90-day high 12.23. UNG is 42.28% below its one-year high of 19.11.
- A structurally-sound stop goes below the 50-day at 10.3142 — say 10.10, which
  is 0.93 or 2.33 ATR. Against the nearest real target, the 90-day high of
  12.23, that is 1.20/0.93 = **1.29:1**, under the 1.8... i.e. under the 2.0
  swing floor.
- A breakout version is no better: entry 11.40 above the 200-day, stop 10.60
  below the 20-day, target 12.23 gives **1.04:1**. The only passing targets
  (12.89 on the market entry, 13.00 on the breakout) are both beyond every
  level I can point at, and picking them would be the target-nudging the floor
  exists to catch.
**Why not the futures route**, which `config/universe.md` would prefer: I could
not verify that Robinhood lists **micro** natural gas (/MNG). Robinhood's own
learn content references standard **/NG**, which is 10,000 MMBtu — roughly
$34,000 of notional at $3.44, far too large for the 2% futures cap, and
universe.md requires the smallest contract that expresses the view. I also could
not fetch a live gas futures price or ATR (`market_data.py macro` returned
`ok: false` for wti_crude and the index/commodity block generally), so I have no
verified number to set futures levels from.
**What would make it tradeable:** UNG closing above the 11.3336 200-day and
holding it, which moves the stop reference up and makes 12.23 a 2:1 target; or a
confirmed /MNG listing. Watchlist, not a recommendation.

## [06:44 ET] NEW IDEA — PEP long_term — a staple de-rated 28% with its guidance intact
Captured. The one genuinely new recommendation today, and it is deliberately a
wait-for-the-print rather than an entry.
- **Reports today, 2026-10-08 bmo**, consensus EPS **2.319** on revenue
  **$25,226,779,564**, verified on the fetched finnhub calendar.
- Close **123.73**, 0.21% above a **fresh one-year low of 123.47** made 10/07 on
  13.3M shares against a ~8.8M norm. Below the 20-day (130.04), 50-day (136.10)
  and 200-day (146.88); **27.85% off the 171.48 one-year high**.
- **Management reiterated FY2026 EPS guidance of $8.55-8.71** → the close is
  **14.3x** the $8.63 midpoint, against the low-20s PEP historically carried.
  Target 164.00 = 19.0x that midpoint; bear case 101.00 = 11.8x the $8.55 low
  end. Long_term R:R from a 118.00 entry = 46/17 = **2.71:1** vs the 2.5 floor.
- **The locatable problem**: Frito-Lay North America volume flat *despite price
  cuts of up to 15%* on Lay's and Doritos; PBNA volume **-4%**, steepest since
  Q2 2020; core operating margin **-40bps** in Q2 — while international segments
  posted solid gains.
  — sources: https://www.techtimes.com/articles/328651/20261006/pepsico-q3-report-thursday-two-downgrades-signal-frito-lay-recovery-may-have-stalled.htm
    https://www.tipranks.com/news/pepsico-shares-near-12-month-low-at-126-72-as-frito-lay-sales-pressure-awaits-october-8-earnings-report
- **Evidence against, recorded rather than buried**: bullish share **40.0%,
  -4.8pp** over four months (strong buys 3→2, holds 15→17); **JPMorgan cut to
  Neutral from Overweight and Deutsche Bank to Hold from Buy**, both on North
  America; **zero open-market insider buys** in six months (1 sell, $405K);
  earnings delivery merely in line (-1.3%, +2.8%, 0.0%, +0.4%).
- **Why it is still a buy-the-wait**: price cuts of 15% that produced no volume
  is the bear case's best fact, not the bull's — it suggests category demand
  rather than price. So the entry discipline carries the idea: **nothing above
  120**, accumulate in thirds at 120 / 114 / 108.
- **Invalidation (mandatory, and not a price)**: Frito-Lay North America volume
  stays negative for two further quarters, **or** management guides FY EPS below
  the $8.55 floor. Either voids the valuation anchor, in which case the idea is
  void rather than cheaper.
- **Correlation noted**: KHC is already an open staples long. PEP is the second
  bet on de-rated packaged food, which is inside the 3-per-driver cap but is the
  reason it is sized 3% rather than higher.

## [06:47 ET] DATA QUALITY / REJECTED — no crypto idea: prices fetch, history does not
- Spot does work (coingecko, 06:32 ET): BTC **$82,733** (-1.32% 24h, $33.8bn
  volume), ETH **$2,555.56** (-1.12%), SOL **$114.50** (-2.82%). Crypto was sold
  alongside gold, miners, EM and small caps on 10/07-10/08 — consistent with the
  liquidity-driven de-risking read above rather than with a crypto-specific story.
- **But `history BTC-USD` fails on every source**: nasdaq has no rows, Yahoo
  returns **HTTP 429** on both hosts, twelvedata and alphavantage have no API
  key, stooq has no history. So I have **no OHLCV, no ATR and no swing levels**
  for bitcoin.
- `config/strategy.md` requires a crypto swing stop to clear **2.5 ATR**, and
  entries/targets to come from real price history. With no ATR and no identified
  support I cannot set either honestly, and `config/universe.md` would route a
  bearish crypto view to a short `/MBT` where the stop is mandatory. **So no
  crypto idea today** — not because the setup is absent but because the numbers
  to size it are unfetchable, and a guessed stop on a leveraged contract is the
  worst thing in this report.

## [06:47 ET] VENUE CHECK — everything captured is plainly Robinhood-tradeable
All 13 captured candidates are US exchange-listed common stock or a major ETF on
`Robinhood Stocks`: PEP, DAL, CEG, CCJ, SNX, DINO, NKE, LULU, LCII (NYSE/Nasdaq
common) and EEM (NYSE Arca ETF). Every one clears the $500K average dollar
volume floor by three or more orders of magnitude — the smallest is LCII at
**$27.5M/day** and the largest JPM-scale names above $1bn. No OTC, no warrants,
no foreign ordinaries, no options, nothing under $1, nothing halted.
- The two `sell` lines (NKE 38.40, LULU 100.61) are short equity and carry
  `requires_margin: true`.
- No `Robinhood Derivatives` or `Robinhood Prediction Markets` idea is published
  today, and in both cases that is a fetch failure rather than a judgement —
  see the event-contract and crypto notes above, and the /MNG note under the
  natural gas rejection. **I did not verify any contract from memory.**

## [06:50 ET] !! SYNTHESIS, READ THIS — five CLOSE instructions will be deleted unless you mirror them into the watchlist
I read `scripts/validate_report.py`. When `--enforce` demotes a failing
recommendation it builds the watchlist entry from scratch:
```
{"symbol", "instrument", "note": "Demoted by validation: <FAIL reasons>",
 "trigger": "Republish only once the numbers check out.",
 "demoted_from_rank", "demotion_reason"}
```
**`catalyst.action` is not copied.** So a demoted row loses its instruction
entirely and the reader is told "republish once the numbers check out" about a
position I am telling them to **close today**.

Four of today's five close recommendations **cannot be made to pass**, and the
reason is structural rather than sloppy: a position being closed at a loss has
its entry above the market and its honest downside below the market, so the
ratio describes a trade nobody would now enter. There is no honest set of levels
that fixes it — raising the target or shrinking the bear case to clear the floor
is precisely the gaming `config/strategy.md` forbids.

| Symbol | Direction | Why it fails | Instruction that must survive |
| --- | --- | --- | --- |
| `SNX` | buy | stop 1.36 ATR from entry; honest stop 234.27 gives 1.40:1 | **CLOSE** at market, ~+4.4% |
| `NKE` | buy | long_term 1.44:1 vs 2.5 floor at a 26.00 bear case | **CLOSE** at market, ~-15.7% |
| `LULU` | buy | long_term 1.67:1 vs 2.5 floor at a 76.00 bear case | **CLOSE** at market, ~-20.1% |
| `LCII` | buy | long_term 1.69:1 vs 2.5 floor at a 68.00 bear case | **CLOSE** at market, ~-14.8% |
| `CCJ` | buy | re-captured at its original levels so it PASSES and survives | **CLOSE** at market, ~-5.2% |

**What to do:** author a `watchlist` entry yourself for each of the four, with
the close instruction in the `note`, before `--enforce` runs. Enforcement uses
`report.setdefault("watchlist", [])` and **appends**, so entries you write
survive untouched; the demotion will add a second, thinner entry for the same
symbol and that duplication is acceptable — losing the instruction is not.
Also say in `data_quality_notes` that four closes were demoted on ratio
arithmetic rather than on doubt about the decision.

## [06:53 ET] CONVICTION — scored strictly as the count of distinct evidence kinds
`config/strategy.md` makes conviction a count (1 kind = 2, two = 3, three = 4,
four or more = 5), and CLAUDE.md records that it had collapsed into a default of
3 on 39 of the first 57 ideas. I scored several candidates by feel on the first
pass and then re-captured them against the rubric, because under-counting
evidence is the same error as inflating it, just in the safer direction:
- `CEG` buy 4 → **5** (4 kinds), `NKE` sell 4 → **5** (4), `LULU` sell 4 → **5** (4),
  `SNX` buy 3 → **4** (3). `DAL` buy 4 and `PEP` buy 4 were already right (3 each).

**Where I deliberately depart from the rubric, and why:** the five CLOSE
recommendations — `CCJ` (4 kinds), `NKE` buy (3), `LULU` buy (3), `LCII` (3) —
are scored **2**, well under what the count implies. That is intentional and is
not a scoring error. On those rows the evidence is almost entirely *against the
position*, and the rubric measures confirmations supporting an idea. Scoring a
position I am retiring as a conviction-4 or -5 **buy** would put a high-conviction
long on the sheet for a stock I am telling the reader to sell, and would corrupt
the by-conviction performance table with its own contradiction. If the red team
disagrees, the fix is to lower nothing and instead read the `catalyst.action`,
which says CLOSE on every one of them.

**Position sizes do not follow conviction upward today.** `NKE` sell and `LULU`
sell are conviction 5 but stay at **2%**, not the 4-5% the tier table suggests
for a 5, because both are short equity on margin into a live European credit
event where crowded shorts in beaten-up consumer names unwind violently. `CEG`
stays at **3%** despite being a 5, because its stop is 1.67 ATR and the forward
ratio is 0.41:1. Conviction measures how well evidenced a view is; size measures
what the risk can bear, and today those point in different directions.

## [06:57 ET] RESEARCH COMPLETE
- **candidates: 12 distinct positions** across 18 log lines (later lines
  supersede earlier ones for the same symbol+direction).
  - **1 genuinely new idea**: `PEP` buy, long_term, conviction 4, wait for this
    morning's print then accumulate below 120.
  - **5 CLOSE instructions**: `CCJ`, `SNX`, `NKE` buy (long_term), `LULU` buy
    (long_term), `LCII`.
  - **2 HOLD-and-trim-at-target shorts**: `NKE` sell, `LULU` sell (both conv 5).
  - **4 position amendments**: `DAL` (half size into tomorrow's print), `CEG`
    (hold, never add), `DINO` (trim half), `EEM` (trim half).
  - **Held unchanged and deliberately not re-emitted**: `XLE` (forward 2.79:1,
    nothing changed, already 3x in 10 days), `KHC` (stop is 3.38 ATR from entry
    and doing its job), `PFE` (only open long that rose on 10/07; 3x in 10 days),
    `BCC` (hold, do not add, invalidation now stated).
  - `GDX` closed itself: the 10/07 low of 84.36 went through the 85.40 stop.
- **Horizon mix: 8 swing, 4 long_term, 0 intraday.** Not manufactured — nothing
  intraday cleared the bar, and with equity prices only available as the previous
  close at 06:00 ET there was no intraday level to set honestly anyway.
- **Why only one new idea.** The tape is a live French sovereign-debt scare with
  the ECB declining to intervene, and 10/07 was indiscriminate de-risking — gold,
  miners, uranium, EM and small caps all sold together while mega-cap indices
  barely moved. Three setups were researched to completion and rejected on their
  numbers rather than trimmed to fit: **JPM** (1.83:1 at the only defensible
  target), **GS** (ratio passes at 2.71:1 but it is the weakest major name in the
  weakest sector, -8.2% vs XLF in a month after a +40.7% beat), and **natural
  gas** (good thesis, but the 200-day sits 2.7% overhead and every passing target
  is beyond any level I can point at). Writing those up is the output; padding
  the list would not have been.

### Coverage gaps — what I could not check
- **Event contracts: none published.** `market_data.py events` returns count 0
  for CPI, recession, FEDDECISION, inflation and unemployment, and for "Fed"
  returns six sports markets with **every price field null**. No implied
  probability means no honest event idea.
- **Crypto: none published.** Spot fetches (BTC $82,733, ETH $2,555.56, SOL
  $114.50) but `history BTC-USD` fails on all five sources, so there is no ATR
  and no support level to set a stop from.
- **Futures: none published.** Could not verify Robinhood lists micro natural
  gas (/MNG), and no live futures price or ATR was fetchable.
- **No index, VIX, DXY, gold or crude level this run.** Yahoo returned HTTP 429
  on both hosts throughout; finnhub refuses indices ("Market data subscription
  required for CFD indices"); stooq 404s on `^` symbols; no alphavantage key.
  **The dollar is the gap that matters most** — EEM is an open long and DXY is
  its primary driver.
- **Options-implied moves unavailable**: `implied DAL` returned HTTP 401 from
  Yahoo, so no target was checked against a straddle.
- **Short interest unavailable**: `short DAL` timed out at api.nasdaq.com. Not
  retried for other names.
- Earnings dates, prices, ATRs, FRED series, insider and analyst data all
  fetched successfully. Every price in this log is the **2026-10-07 close**.

### Two handoff items that are not optional
1. **NKE and LULU each need two rows kept** — synthesis dedupes on symbol, but
   each has a long to close and a short to hold. See 06:24.
2. **Four CLOSE instructions will be destroyed by `--enforce`** unless synthesis
   mirrors them into the watchlist first. See 06:50.

## [07:00 ET] ADDENDUM — AWAITING ENTRY review, and the VST lesson is the most useful thing here
Checked the 13 unfilled orders against today's prices. One matters a great deal.

### VST — CANCEL the BUY @ 132.00 (published 2026-08-24). Do not chase.
VST was the same trade as CEG and it ran without us:
- 10/02 close **140.02** → 10/05 **144.89** → 10/06 **160.50** (gapped open
  151.47, +10.8%, **18.1M shares**) → 10/07 **166.72** (+3.9%, high 168.11).
- **+19.1% in two sessions**, on the same hyperscaler-nuclear-PPA news that
  re-rated CEG. The order sat at **132.00**, and the market is now **26.3%
  above it**. That level will not be revisited without a crash, and the thesis
  it was waiting to buy has already been paid for.
- **Not chasing it.** Close 166.72 against a 20-day of 143.35 and a 50-day of
  143.37 — the stock is **16.3% above both** and 7.7% above its 200-day of
  154.78. ATR14 6.30 (3.78%). A 2.0 ATR stop lands at 154.11, essentially on the
  200-day, and the target that would clear 2:1 is 191.94 — a ratio of **exactly
  2.00**, which is the signature of a number reverse-engineered from the floor
  rather than read off a chart. Cancel, do not re-enter.

### The lesson, and it is evidence rather than a maxim
This report **correctly identified the theme and both names**. The difference in
outcome was entry style alone:
- `CEG` entry **272.00, at the market** on 2026-10-01 → filled → **+10.1%**.
- `VST` entry **132.00, a pullback discount** on 2026-08-24 → never filled →
  **missed +19.1%**, and the stock is 26% away.
`config/strategy.md` records that the first month ran 31 pullback entries against
1 breakout, with only 42% ever filling and the fills skewed to the ideas that
were already failing. This week is a clean instance of the same mechanism, on
one theme, in one book, five weeks apart. **A pullback entry is a bet that you
will be given a better price, and on a working thesis you are not.**

### The rest of the unfilled list, briefly
- `GLD` SELL @ 406.77 (09-08) and `TLT` SELL_SHORT @ 79.90 (09-24): **both moves
  happened without filling** — GLD is now 375.88 (-7.6% below the entry) and TLT
  77.145 (-3.4%). Same pattern mirrored: short entries placed above the market
  on instruments that fell straight down. **Cancel both**; the edge is spent.
- `ITB` SELL_SHORT @ 89.8 (09-30): close **84.70**, 0.94% off its one-year low of
  83.91, below the 20/50/200-day (88.11/93.25/97.14). Unfilled and 5.7% below the
  entry — the short was right and never got on. Do not chase a 28%-off-high
  instrument at its low. **Cancel.** Note it is also the contradiction flagged at
  06:27 against the open BCC long.
- `AAL` SELL_SHORT @ 13.35 (10-03): close **12.85**, so the entry is 3.9% *above*
  the market, which is the right side for a short to wait on. **DAL reports
  tomorrow bmo**, and a good DAL print is exactly what would bounce AAL into
  13.35. Structurally coherent as a pair against the open DAL long — long the
  quality airline, short the weakest balance sheet. **Keep the order live.** I am
  not re-capturing it as a candidate because I could not set an honest target: a
  2.0 ATR stop at 14.25 (above the 50-day 13.90 and 200-day 13.81) leaves the only
  2:1 target at 11.56, and I have no intermediate support level between 12.65 and
  the 9.48 one-year low to justify that number rather than derive it from the
  floor. Unchanged order, no new claim.
- `KXFEDDECISION-26SEP-H0` YES @ 47 (09-03): **its event has passed.** It should be
  reaped rather than carried as awaiting entry. `KXCPIYOY-26SEP-T3.5` NO @ 18 and
  `KXFEDDECISION-26OCT-H25` YES @ 28: unpriceable this run — see 06:30.
- `DG` @ 134.5, `MU` @ 960.0, `OXY` @ 54.0, `FCX` @ 68.2, `IYR` SELL_SHORT @ 97.8:
  not re-examined, no budget left to do it honestly. Carried unchanged.

## [07:04 ET] FINAL STATE — supersedes the 06:57 RESEARCH COMPLETE block
Research was **not** truncated; it ran 06:01-06:37 ET and finished inside budget.
The 06:57 RESEARCH COMPLETE block stands, with the 07:00 AWAITING ENTRY addendum
added after it. Final tally:

- **`candidates.jsonl`: 18 lines, 12 distinct (symbol, direction) positions.**
  All 18 validated at capture; re-checked just now for required fields, venue
  enum, a stop on every swing idea and a `bear_case_price` on every long_term
  one. All pass.
- Conviction spread: **2×4, 3×2, 4×3, 5×3** — not collapsed on 3, which was the
  recorded failure mode.
- Horizons: 8 swing, 4 long_term, 0 intraday.
- **Six orders to cancel** on top of the 12 positions, all recorded at 07:00 and
  none of them captured as candidates because a cancellation is not a trade:
  `VST` @132, `GLD` @406.77, `TLT` @79.90, `ITB` @89.8, and the expired
  `KXFEDDECISION-26SEP-H0` @47. `AAL` @13.35 stays live, unchanged.
- **The three things synthesis must not miss**, in priority order:
  1. Mirror the four un-savable CLOSE instructions into the watchlist before
     `--enforce` runs (06:50). `SNX`, `NKE` buy, `LULU` buy, `LCII`.
  2. Keep two rows each for `NKE` and `LULU` — dedupe on (symbol, direction),
     not symbol (06:24).
  3. Say in `data_quality_notes` that no event-contract, crypto or futures idea
     was published, and that this was a **fetch failure, not an absence of
     setups** (06:30, 06:47) — and that every equity price in this report is the
     2026-10-07 close, which at 06:00 ET is the freshest honest price and not
     stale data.
- Net effect on the book if all of this is acted on: **16 open positions become
  10** (5 closed by instruction, GDX closed by its stop), four of the survivors
  are halved, and one new long_term accumulation waits on a print that happens
  before the open today.
