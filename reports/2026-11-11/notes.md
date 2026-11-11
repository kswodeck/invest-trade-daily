# Research log — 2026-11-11

## [06:03 ET] DATA QUALITY
- Yahoo Finance returning HTTP 429 (rate limited) for index quotes: ^GSPC, ^NDX, ^DJI, ^RUT, ^VIX all `ok: false`.
  Finnhub refuses indices ("Market data subscription required for CFD indices"), stooq 404s on ^-prefixed symbols,
  no alphavantage key. **Index levels and VIX are UNAVAILABLE this run.** Equity/ETF single-name quotes via
  finnhub DO work. Will proxy the tape with SPY/QQQ/IWM ETF quotes instead.
- All equity prices below are prior-close (2026-11-10 21:00 UTC = 16:00 ET close), age ~841 min. Market session: pre.
  At 06:00 ET the previous close is the freshest honest equity price.

## [06:03 ET] OPEN POSITIONS — prior close 2026-11-10
| Sym | Entry | Last (11-10 close) | % vs entry | Stop | Dist to stop |
| --- | --- | --- | --- | --- | --- |
| XLE | 63.9 | 62.21 | -2.6% | 60.8 | -2.3% |
| BCC | 76.5 | 70.42 | -7.9% | none | — |
| PFE | 27.6 | 29.36 | +6.4% | none | — |
| KHC | 23.0 | 24.24 | +5.4% | 21.2 | -12.5% |
| AAL (short) | 13.35 | 14.11 | -5.7% | 14.4 | +2.1% |
| HII | 262.0 | 313.57 | +19.7% | none | — |
| UNP | 288.6 | 300.62 | +4.2% | 277.4 | -7.7% |
| ABT | 103.0 | 110.46 | +7.2% | 97.0 | -12.2% |
| PYPL | 56.5 | 58.78 | +4.0% | 54.1 | -8.0% |
| SMMT | 17.1 | 17.83 | +4.3% | 14.4 | -19.2% |
| RTX | 199.0 | 200.27 | +0.6% | 186.0 | -7.1% |
| XLU | 43.3 | 43.73 | +1.0% | 41.8 | -4.4% |
| NVDA | 184.0 | 168.89 | **-8.2%** | 166.0 | **-1.7%** |

- **NVDA is the urgent one**: -5.47% on 2026-11-10 (178.67 -> 168.89), low of day 165.89 which is BELOW the 166 stop.
  Intraday the stop was already touched. Needs a decision this morning, not a hold-by-default.
- HII +19.7% and no stop — ran from 262 to 313.57 (+3.0% on 11-10 alone). Unprotected 20% gain.
- AAL short is 2.1% from its 14.4 stop and losing.

## [06:06 ET] MACRO — regime: rates up, growth de-rating, defensives bid
Prior close 2026-11-10 (finnhub), FRED as dated:
- **US 10y 4.88%** (prev 4.86), date 2026-11-09 — source: FRED DGS10
- **US 2y 4.56%** (prev 4.51), date 2026-11-09 — source: FRED DGS2
- **10y-2y curve 0.25** down from 0.32 on the prior day — flattening from the short end, i.e. the
  market taking out near-term cuts. source: FRED T10Y2Y, date 2026-11-10
- **Fed funds effective 3.88%** unchanged — source: FRED DFF 2026-11-09
- Unemployment 4.1% (Oct) vs 4.2% prior — labour market firming, not loosening. source: FRED UNRATE
- CPIAUCSL Oct ref 337.476 vs 336.298 = **+0.35% MoM** (~4.3% annualised). Hot. source: FRED CPIAUCSL
- VIX, SPX, NDX, DXY, 10y-via-market all UNAVAILABLE (yahoo 429 / finnhub index paywall).

Tape proxied by ETF closes on 2026-11-10:
| ETF | Close | Chg |
| --- | --- | --- |
| SPY | 749.92 | -0.37% |
| QQQ | 674.76 | -0.68% |
| IWM | 280.58 | -0.68% |
| DIA | 521.73 | -0.31% |
| SMH | 483.63 | -0.78% |
| XLK | 168.91 | **-1.15%** |
| XLF | 58.29 | **+0.52%** |
| XLV | 188.88 | +0.29% |
| XLE | 62.21 | +0.44% |
| XLP | 91.03 | +0.15% |
| GLD | 369.36 | **-2.68%** |
| TLT | 80.88 | **-1.32%** |
| UUP | 29.15 | **+0.62%** |

**Read:** this is a single coherent trade, not noise. Yields up at the short end, dollar up, gold down
hard, long tech down and financials/energy/staples up. That is real rates repricing higher and the
market taking out Fed cuts. Everything long-duration — growth multiples, gold, TLT, utilities — is on
the wrong side of it. Mechanically raises the bar today for: TLT long (awaiting entry @ 80.3, now 80.88,
about to fill INTO the move against it), XLU long (open), gold longs; and lowers the bar for financials.

## [06:06 ET] CALENDAR — dated catalysts inside 10 sessions (source: market_data.py earnings, finnhub)
- **2026-11-12 AMC: AMAT** (eps est 4.13, rev est 10.5B) — semicap, reads through to the whole SMH complex
- **2026-11-12 AMC: CSCO** (1.35 / 18.5B)
- **2026-11-16 AMC: ACM** (1.59 / 1.9B) — **I HAVE AN OPEN ACM POSITION.** Dated event inside the hold.
- **2026-11-16 BMO: PDD, BIDU, TSN**
- **2026-11-17 AMC: NVDA** (2.53 / 111.4B) — **I HAVE AN OPEN NVDA POSITION 1.7% FROM ITS STOP.**
- **2026-11-17 BMO: HD, DIS**
- **2026-11-18: TGT, LOW, TJX, ROST, GAP, PANW** — consumer/retail day
- **2026-11-19: WMT, BABA, INTU, KEYS**
- 2026-11-23: HPE, ZM, DKS, KSS, ANF, A, J

## [06:10 ET] POSITION UPDATE — NVDA — STOP ALREADY TOUCHED ON 2026-11-10, NOT A HOLD DECISION
- opened 2026-11-07 @ 184.0, stop 166.0, target 220.0
- 2026-11-10 bar: close 168.89, **low 165.89** — source: market_data.py history NVDA (nasdaq), range_low=165.89, pct_off_low=1.81
- The 166 stop sits *inside* yesterday's range. The position stopped out on 2026-11-10 at roughly **-9.8%**.
- decision: **no amendment to pitch.** Per the one-row-one-position rule a closed position cannot be
  amended; any NVDA idea today is a genuinely new trade and must stand on its own evidence.
- context for why it broke: NVDA 168.89 vs SMA20 206.18 and SMA50 217.998 — **-30.6% off its 90-day
  high of 243.37**, and it set the 90-day low (165.89) yesterday. ATR14 9.2886 (5.5%/day).
  This was not a wobble; it is a multi-week de-rating of the AI-capex complex and the 184 entry four
  sessions ago was buying into it. Q3 earnings 2026-11-17 AMC (eps est 2.5263, rev est 111.4B).
- **Lesson that generalises to today's hunt:** the 184 entry was a pullback entry into a name making
  lower highs below a falling SMA20/SMA50. config/strategy.md warns about exactly this — a pullback
  entry is fine on real support you can point at, not as a reflex discount off the last print. There
  was no support at 184; the SMAs were overhead and falling.

## [06:11 ET] REJECTED — NVDA re-pitch into 11/17 earnings — will not buy a knife 1.8% off a 90-day low with no support level beneath it; a long needs a ~150 stop (2.0 ATR = 18.6pts) and no defensible target gives 2:1 from here. Revisit after the print.

## [06:18 ET] POSITION UPDATE — ACM — opened 2026-11-07 @ 66.74, now 70.63, +5.8%
- decision: **hold, trim half into the 2026-11-16 AMC print, stop unchanged at 61.50**
- why: earnings 2026-11-16 AMC is a dated event inside the hold (fetched calendar, eps est 1.5938).
  Relative strength is the standout in the whole book: ACM +19.69% 1m vs SPY -3.62%, XLI -0.25%
  (+23.31% vs SPY, +19.94% vs XLI). Insiders: 3 distinct open-market buyers, $699,391, ZERO sells,
  CEO Troy Rudd 4,225 sh @ 71.02 on 2026-05-14 — at today's price.
- why trim rather than add: ACM printed **actual EPS -0.50 vs 1.4809 est for Q/E 2026-06-30, a -133.8%
  surprise**. Analyst revisions are *deteriorating* (bullish share 83.3% Aug -> 76.5% Nov, -6.8pp; buys
  cut 11 -> 9). Price is 12% above SMA20 going into that print. Target 77.22 is above the 120d range
  high 76.85, i.e. requires a new high.
- stop deliberately NOT tightened: entry is fixed at 66.74 (filled), and 61.50 is 2.46 ATR below it.
  Walking it in to protect the gain is the exact abuse config/strategy.md names (the KRE case).
- action: captured via add_candidate.py, conviction 4 (dated_catalyst, technical_level, positioning)

## [06:22 ET] LEVELS — all open positions and awaiting-entry names (120d history, prior close 2026-11-10)
| Sym | Close | SMA20 | SMA50 | ATR14 | ATR% | 120d hi | 120d lo | off hi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PFE | 29.36 | 29.85 | 28.79 | 0.793 | 2.70 | 31.44 | 23.62 | -6.6% |
| KHC | 24.24 | 24.22 | 23.95 | 0.785 | 3.24 | 28.09 | 21.76 | -13.7% |
| UNP | 300.62 | 296.15 | 286.49 | 8.062 | 2.68 | 315.99 | 255.22 | -4.9% |
| ABT | 110.46 | 106.34 | 103.97 | 3.043 | 2.75 | 117.34 | 84.96 | -5.9% |
| PYPL | 58.78 | 57.56 | 55.35 | 1.689 | 2.87 | 62.73 | 40.20 | -6.3% |
| SMMT | 17.83 | 15.72 | 16.41 | 1.213 | 6.80 | 19.09 | 12.07 | -6.6% |
| TLT | 80.88 | 81.04 | 80.33 | 0.794 | 0.98 | 87.79 | 76.43 | -7.9% |
| GLD | 369.36 | 372.04 | 383.59 | 7.571 | 2.05 | 429.42 | 354.67 | -14.0% |
| XLV | 188.88 | 181.76 | 174.09 | 3.793 | 2.01 | 192.32 | 145.31 | **-1.8%** |
| XLF | 58.29 | 56.55 | 55.92 | 1.019 | 1.75 | 60.04 | 50.52 | -2.9% |
| HUN | 9.50 | 9.06 | 9.00 | 0.457 | 4.81 | 16.09 | 8.00 | -40.9% |
| CVS | 89.01 | 89.88 | 90.13 | 3.469 | 3.90 | 110.68 | 77.33 | -19.6% |
| ONON | 34.70 | 34.93 | 31.81 | 1.726 | 4.97 | 41.41 | 26.37 | -16.2% |
| OXY | 56.90 | 61.00 | 59.92 | 2.026 | 3.56 | 64.96 | 47.77 | -12.4% |

## [06:23 ET] META — WHY THE HIT RATE IS 10%, AND IT IS VISIBLE IN THE LEVELS
Not a mood, an arithmetic pattern in the open book. Published targets sit almost exactly ON the
120-day range high, over and over:
- UNP target 315.99 vs range high 315.99 — identical
- ABT target 117.34 vs range high 117.34 — identical
- KHC target 28.09 vs range high 28.09 — identical
- PYPL target 62.70 vs range high 62.73 — identical to 3 cents
- ACM target 77.22 vs range high 76.85 — above it
- RTX target 226.50 vs range high 226.88 — identical
- HII target 339.76 vs range high 334.53 — above it
That is seven of fourteen open positions whose target requires the instrument to make a **new
120-day high** to pay out, while the stop only requires an ordinary pullback. Targets are being
anchored to the range high because that is the number the reward-to-risk floor needs, which is the
reverse-engineering config/strategy.md prohibits — just applied to the target instead of the stop.
**Consequence I am applying today: a target at or above the range high must be argued for, not
assumed.** Prefer targets at measured resistance *inside* the range unless there is a reason the
instrument breaks out.

Second pattern, the stop-distance floor is being missed on filled positions:
- UNP stop 277.40 vs entry 288.60 = **1.39 ATR** (floor 2.0)
- PYPL stop 54.10 vs entry 56.50 = **1.42 ATR** (floor 2.0)
- ABT stop 97.00 vs entry 103.00 = **1.97 ATR** (floor 2.0)
- XLE stop 60.80 vs entry 63.90 = 1.64 ATR (ETF floor 1.8)
These are all under the floor that validate_report.py now enforces, which means they predate the
floor. Each is a live stop tighter than the thesis needs. I am not walking them wider — that is the
mirror-image abuse — but it does mean these four are likelier to stop on noise than the book implies.

## [06:08 ET] TIMESTAMP CORRECTION
The `[HH:MM ET]` labels above were estimated, not read from the clock, and they run ahead of the
real time — `date` says 06:08 ET at the point this line was written. Research began 06:00:52 ET.
Everything above was produced between 06:00 and 06:08 ET. All labels from here are read from `date`.

## [06:09 ET] MACRO — THE DOMINANT FACT IS A 6-MONTH ROTATION, NOT YESTERDAY'S TAPE
Relative strength, source: market_data.py relstrength (computed from price history):
| Group | 1m | 3m | 6m | vs SPY 1m |
| --- | --- | --- | --- | --- |
| SMH (semis) | **-18.17%** | **-17.30%** | **-13.83%** | -14.55% |
| XLK (tech) | -13.98% | -10.56% | -3.59% | — |
| SPY | -3.62% | -2.92% | +1.59% | — |
| XLF (financials) | +5.89% | +0.64% | +13.01% | +9.51% |
| XLP (staples) | +7.84% | +6.99% | +7.80% | — |
| XLV (healthcare) | **+9.82%** | **+12.13%** | **+29.50%** | +13.44% |

- SMH is "lagging SPY on every window measured". NVDA's -30.6% drawdown is **sectoral, not
  company-specific** — which is why it kept going and why the 184 entry had no support under it.
- XLV is "outperforming SPY on 1m/3m/6m" and is **+29.50% over 6m against SPY +1.59%**. Healthcare is
  the leadership group of this tape, and it sits only 1.79% off its 120-day high while SPY is -0.37%
  on the day. That is leadership, not a defensive huddle.
- This squares with the rates read: real rates up, long-duration growth multiples down. The rotation
  and the macro are the same trade.

**CORRELATION CAP NOTE (config/strategy.md: max 3 ideas on one driver).** The book is already long
ABT and PFE, both healthcare. Adding XLV makes three. **Healthcare is therefore full after XLV and I
must not add a fourth healthcare name today**, however good it looks. Logging this so synthesis does
not stack more on.

## [06:11 ET] DATA QUALITY — sources that failed
- **Event contracts: UNAVAILABLE.** `market_data.py events` returns `ok: true` but `count: 0` for
  every query tried (Fed, CPI, recession, Bitcoin). The Kalshi endpoint is reachable and returning an
  empty market list. **No event-contract idea can be sourced today and none will be fabricated**,
  despite the lane being explicitly wanted. This is the second consecutive lane lost to a data source.
- **Options-implied move: UNAVAILABLE.** `market_data.py implied` returns yahoo-options HTTP 401
  Unauthorized. So no idea today can carry the "is the target inside what options price" check.
- **Crypto price history: UNAVAILABLE.** `history BTC-USD` returns ok:false with no source. Spot
  quotes via coingecko DO work. So crypto levels cannot be set from ATR/SMA and **no crypto or crypto
  futures idea will be published today** — including the /MBTZ6 short sitting in awaiting-entry.
- Index levels and VIX: UNAVAILABLE (yahoo 429, finnhub index paywall). Proxied by ETFs.

## [06:11 ET] CRYPTO — spot only, source: coingecko
- bitcoin 73,930.00 (-0.27% 24h), vol 33.1B
- ethereum 2,057.38 (-1.53% 24h)
- solana 83.70 (-0.87% 24h)
- Consistent with the regime (dollar up, real rates up) but **I cannot set a stop without ATR**, so
  the awaiting-entry `/MBTZ6` SHORT @ 74,075 stays unpitched rather than re-pitched on spot alone.
  BTC spot 73,930 is 0.2% below that short entry, i.e. the level is live — but a futures idea must
  carry a stop and I have no volatility measure to place one honestly.

## [06:12 ET] REJECTED — XLV — the chart is the best in the tape and the trade still does not clear the bar.
XLV is the leadership group (+9.82% 1m, +12.13% 3m, +29.50% 6m vs SPY +1.59% 6m) and sits 1.79% off
its 120-day high. That closeness to the high IS the problem. Honest geometry, entry 184 (the
unchanged awaiting-entry level):
- ATR14 3.7931; ETF swing stop floor is 1.8 ATR, comfortable 2.25 ATR
- A properly wide stop below the rising SMA50 (174.09) at 173.50 is 2.77 ATR — risk 10.50/share
- 2.0 reward-to-risk then demands a 205.00 target, which is **6.6% above the 192.32 range high**
- To make the target modest instead (198.00, +2.9% over the high) the stop has to come in to 177.00
  = 1.85 ATR, barely over the floor
config/strategy.md: "If an idea needs a tight stop to clear the reward-to-risk floor, it has failed
the floor." Both versions fail — one reverse-engineers the target, the other the stop. This is
exactly the pattern I flagged at 06:23 in the META note, and I am not going to commit it one
paragraph after writing it down. **XLV: let the 184 level expire, watchlist only.** A leader with no
room is not a trade.

## [06:13 ET] CATALYST SWEEP — the earnings names, sorted by where they sit in their own range
source: market_data.py history --days 120, closes 2026-11-10
| Sym | Close | SMA20 | SMA50 | ATR% | off 120d hi | off lo | Earnings |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AMAT | 372.53 | 389.90 | 441.30 | 6.93 | **-49.64%** | +17.5% | 11-12 AMC |
| CSCO | 98.15 | 105.12 | 108.34 | 3.98 | -24.71% | **+5.1%** | 11-12 AMC |
| KEYS | 291.46 | 315.32 | 336.14 | 6.01 | -25.25% | +13.0% | 11-19 AMC |
| PANW | 326.36 | 356.30 | 368.37 | 6.41 | -24.51% | +35.4% | 11-18 |
| TJX | 136.92 | 142.17 | 135.91 | 2.83 | -19.46% | +11.5% | 11-18 |
| POST | 81.83 | 81.02 | 78.66 | 3.18 | -16.89% | +14.5% | 11-19 AMC |
| TSN | 60.29 | 56.85 | 54.08 | 2.33 | -10.01% | +20.7% | 11-16 BMO |
| CPRT | 32.30 | 29.72 | 29.43 | 3.13 | -9.42% | +25.6% | 11-18 |
| INTU | 340.44 | 337.89 | 317.84 | 4.33 | -8.72% | +34.7% | 11-19 |
| WMT | 125.55 | 121.88 | 113.35 | 2.54 | -4.76% | +22.9% | 11-19 |
| WSM | 261.55 | 254.84 | 239.85 | 3.74 | -4.70% | +47.4% | 11-17 BMO |
| ENR | 24.86 | 23.18 | 22.05 | 3.99 | -3.76% | +53.9% | 11-17 BMO |
| HD | 351.00 | 327.09 | 310.32 | 2.99 | -3.16% | +26.7% | 11-17 BMO |
| BJ | 110.40 | 106.45 | 98.85 | 2.47 | -2.60% | +32.7% | 11-20 |
| DIS | 119.21 | 112.95 | 108.49 | 2.15 | -1.32% | +28.9% | 11-17 BMO |
| LOW | 231.87 | 208.16 | 198.17 | 3.08 | -1.23% | +29.9% | 11-18 |
(TGT and ATKR: history fetch FAILED, no data, not assessed.)

- **AMAT has halved**: 739.67 -> 372.53 in 120 days, and it is below a SMA50 of 441.30 that is itself
  far below the old high. The semicap complex is de-rating far harder than SMH's -18.17% suggests,
  and AMAT reports **tomorrow** 11-12 AMC. This is the single biggest dislocation on the board.
- The tape is split cleanly in two and the split is the whole problem for idea generation:
  **the leaders have no room** (LOW -1.2%, DIS -1.3%, BJ -2.6%, HD -3.2%, ENR -3.8%, WMT -4.8% off
  their highs) and **the names with room have no support** (AMAT, CSCO, KEYS, PANW all below both
  SMAs and falling). Buying either one is a different mistake.
- TJX is the one name in the list sitting on real support rather than at an extreme: pulled back
  -19.46% off its high to an SMA50 of 135.91 that it is still **above**, with 2.83% ATR. Taking it
  forward for level work.

## [06:13 ET] REJECTED — AMAT long into 11-12 AMC print — down 49.6% in 120 days, below a falling SMA20 and SMA50, ATR 6.93%/day, and the catalyst is tomorrow. Identical shape to the NVDA 184 entry that just stopped out; no support level under it to anchor a stop. The dislocation is real but a one-day binary is not how to express it.
## [06:13 ET] REJECTED — CSCO long into 11-12 AMC print — 5.1% off its 120-day low, below SMA20 105.12 and SMA50 108.34, print is tomorrow. Same falling-knife-into-a-binary shape as AMAT. Would be inconsistent to reject NVDA's setup and take this one.
## [06:13 ET] REJECTED — LOW / DIS / HD / BJ / WMT longs — all 1.2-4.8% off their 120-day highs in confirmed uptrends, which is the right side of the rotation, but a 2.0-ATR stop plus a 2.0 reward-to-risk floor puts every target well above the range high. Same failure as XLV: leadership with no room. Watchlist.

## [06:14 ET] REJECTED — TJX — clean geometry, but two of the three available confirmations point the wrong way.
The setup looked right (pullback to a rising SMA50 of 135.91 that it is still above, -19.46% off the
high so a target of ~151 sits INSIDE the range, ATR only 2.83%). The evidence does not support it:
- **It is a laggard, not a leader**: TJX -3.52% 1m / -10.28% 3m / -8.88% 6m, and **vs XLY it is
  -11.34% / -12.96% / -11.21%** — underperforming its own sector on every window. The "outperforming
  SPY on 1m" tag is +0.10%, i.e. noise.
- **Insiders: 0 open-market buys, 8 sells, $27,714,991 sold, net -$27.7M** over six months.
- Analyst revisions deteriorating: bullish share 84.6% Aug -> 77.8% Nov (-6.8pp), strong buys cut 11 -> 8.
In favour: four consecutive EPS beats (+1.63%, +15.94%, +1.89% for Q/E Sep, Jun, Mar) and earnings
11-18. That is a good operator in a cheap-looking chart, but positioning is evidence and here it is
negative evidence. Conviction would be 3 at best.
**Additional reason to hold the bar high on a 3 today:** the track record says conviction 3 is
**2/25 hit target (8%), avg -6.9%, n=43** — 25 closed trades, which is past the ~15 noise threshold
and is the worst bucket with a real sample. Conviction 4 is 2/8 (25%), avg -0.8%. prior_context.md
says to raise the bar where a category is consistently losing, so today a conviction-3 idea has to be
clean, and this one has insiders selling $27.7M into it. **Watchlist.**

## [06:18 ET] NEWS — the semis de-rating is a sector bear market, and it is the context for NVDA
- "global semiconductor stocks have shed **$3.3 trillion in market value since June 22**, nearing
  bear-market territory" — source: https://stockanalysis.com/news/nasdaq-100-falls-chip-stocks-slide/
- 2026-11-05: NVDA -6% to ~188 and QCOM plunged, driving **the Nasdaq's steepest daily loss in 19
  months**, on questions about "the pace, cost and financing of the artificial intelligence boom".
  Kospi -6%+, Nikkei 225 -5.9% and into bear-market territory.
  source: https://www.ibtimes.co.uk/nvidia-qualcomm-shares-nasdaq-ai-selloff-1830635
- AMAT specifically: drop attributed to "2026 demand visibility and policy-driven China and
  export-control worries" — source: https://rallies.ai/news/applied-materials-drops-with-semicap-selloff-as-china-export-risks-resurface
  (undated article; treating the attribution as unconfirmed for 11-10 specifically)
- **I could not find dated coverage of the 2026-11-10 session itself.** So the -5.47% NVDA move is
  recorded as price fact and placed in this sector context, with no single-day cause asserted.
- Implication: the NVDA 184 entry on 11-07 was made two sessions after the worst Nasdaq day in 19
  months, into a sector that had already lost $3.3T since June. That is the real error, not the stop.

## [06:19 ET] KHC — split is a driver but NOT a dated catalyst, and I will not pretend otherwise
Kraft Heinz confirmed (2025-09-02) a tax-free separation into two listed companies — Global Taste
Elevation (Heinz, Philadelphia, Kraft Mac & Cheese) and North American Grocery (Maxwell House,
Oscar Mayer, Kraft Singles, Lunchables) — "expected to close in the second half of 2026".
sources: https://www.just-food.com/news/kraft-heinz-confirms-split-into-two-independent-publicly-listed-companies/
         https://m.washingtontimes.com/news/2025/sep/2/kraft-heinz-split-expected-close-second-half-2026-creating-two-food/
**No completion date has been published.** H2 2026 ends in seven weeks, so the event is close, but a
window is not a date and `catalyst.datetime_et` stays null. KHC is therefore a hold on positioning
and relative strength, not on an event, and it is marked that way.

## [06:20 ET] POSITION UPDATE — HII — opened 2026-10-12 @ 262.00, now 313.57, +19.7%
- decision: **TRIM HALF at market (313-315) and put a 235.00 stop on the remainder**
- why: the gain is carrying **no stop at all**, and the strength is one month deep with nothing under
  it — +18.76% 1m vs SPY -3.62%, but -4.05% 3m and -5.99% 6m. Insiders sold $5,606,116 across 3
  transactions, zero buys. Target 339.76 is 1.56% ABOVE the 334.53 range high; only +8.3% left to it.
- the stop is honest but weak, and I am saying so rather than dressing it up: the ATR floor is
  measured from the 262.00 entry, so 2.0 ATR on a 13.402 ATR means the tightest publishable stop is
  235.00 — 25% below spot. It backstops a catastrophe; **the trim is the actual risk control.**
- action: captured via add_candidate.py, conviction 3

## [06:20 ET] POSITION UPDATE — AAL — opened 2026-10-03 SHORT @ 13.35, now 14.11, -5.7%
- decision: **CLOSE AT MARKET TODAY**
- why: the short is falsified, not early. AAL +11.81% 1m and +11.19% 6m vs SPY -3.62% / +1.59%
  (+15.43% / +9.60%), and price 14.11 is above both SMA20 12.6683 and a turned-up SMA50 12.9077.
- the stop at 14.40 is **0.44 ATR** above price on a 4.62% ATR, so this resolves within days anyway;
  closing now saves roughly the last 2% and nothing is learned by waiting.
- entry-to-stop was 1.61 ATR, **under the 2.0 ATR swing floor from the day it was published** — this
  is the fifth position in the open book with a sub-floor stop. It was never given room to work.
- win_probability stated at 0.15 against a 0.276 break-even baseline. That is deliberate: it makes
  expectancy negative, which is a hard validation failure, which is the correct machine-readable way
  to say "this position no longer has an edge" rather than me nudging numbers to keep it alive.
- action: captured via add_candidate.py, conviction 2

## [06:21 ET] POSITION UPDATE — HOLD, NO CHANGE (no candidate emitted; re-pitching an unchanged thesis is the anchoring trap prior_context warns about)
All of the following are above both their SMA20 and SMA50, in profit, with stops already in force and
no dated event inside the horizon. Nothing changed, so nothing is amended:
- **RTX** 200.27 (entry 199.00, +0.6%), SMA20 195.01 / SMA50 193.00, stop 186.00 = 2.44 ATR. Hold.
  Note: RTX + HII are both defence. With the HII trim the sector exposure comes down, which is wanted.
- **UNP** 300.62 (entry 288.60, +4.2%), SMA20 296.15 / SMA50 286.49. Hold. Stop 277.40 is **1.39 ATR**,
  under the floor — flagged, not widened.
- **ABT** 110.46 (entry 103.00, +7.2%), SMA20 106.34 / SMA50 103.97. Hold. Stop 97.00 = **1.97 ATR**,
  a hair under the floor — flagged, not widened.
- **PYPL** 58.78 (entry 56.50, +4.0%), SMA20 57.56 / SMA50 55.35. Hold. Stop 54.10 = **1.42 ATR**,
  under the floor — flagged, not widened.
- **SMMT** 17.83 (entry 17.10, +4.3%), SMA20 15.72, ATR 6.80%/day. Hold. Stop 14.40 = 2.23 ATR, fine.
- **XLU** 43.73 (entry 43.30, +1.0%), SMA20 42.77 / SMA50 41.82, stop 41.80 = 2.32 ATR. Hold, but
  **this is the one hold the macro argues against** — utilities are a bond proxy and the 10y went to
  4.88% with the curve flattening to 0.25. It closed -0.14% on a day TLT fell -1.32%, so it is
  outperforming its own driver; that is the only reason it is a hold rather than a trim.

## [06:25 ET] POSITION UPDATE — PFE — opened 2026-08-18 @ 27.60, now 29.36, +6.4%
- decision: **continue accumulating** (add a third under 28.00, a third under 26.00). Conviction 4.
- valuation: four fetched quarterly actuals 0.87 + 0.77 + 0.75 + 0.66 = **3.05 TTM EPS**. At 29.36
  that is **9.6x trailing**; the 42.00 target is 13.8x; bear case 24.00 (just above the 23.62 range
  low) is 7.9x. R:R 4.0 vs the 2.5 long_term floor.
- **beat consensus four quarters running**: +17.6%, +11.4%, +3.5%, +14.3%.
- insiders: **3 distinct buyers, $2,960,110** open-market in August vs $134,661 sold — CEO Albert
  Bourla 38,000 sh @ 26.34 (2026-08-12), Buckley 37,632 @ 25.52, Blaylock 39,231 @ 25.46 (08-05).
- in the leadership sector (XLV +29.50% 6m vs SPY +1.59%), and outperforming SPY on 1m/3m/6m itself.
- invalidation (no stop by design): close if TTM EPS < 2.40, or two consecutive consensus misses.
- action: captured via add_candidate.py

## [06:25 ET] POSITION UPDATE — BCC — opened 2026-08-18 @ 76.50, now 70.42, -7.9% after 84 days
- decision: **CLOSE AT MARKET**
- why, and this is the whole argument: **the demand recovery arrived at the customers and never
  reached the supplier.** LOW closed 231.87 (-1.23% off its 120d high), HD 351.00 (-3.16% off),
  both above rising SMA20/SMA50. BCC is -20.37% off its high, below SMA20 75.304 and SMA50 75.522,
  and -16.42% vs SPY on 3m. Home improvement demand is at its highs; BCC is at its lows. That makes
  the problem **wood-product pricing and margin, not volume** — and the housing-demand thesis this
  position was opened on is the wrong thing to be waiting for.
- confirming: last print **missed -7.7%** (1.04 vs 1.1269 est, Q/E 2026-09-30), breaking a 3-quarter
  beat streak; revisions deteriorating **-9.1pp** (worst screened today); insiders sold $665,842 with
  zero buys.
- at an honest 62.00 bear case (below the 65.41 range low) R:R is **2.31, under the 2.5 long_term
  floor** — so on today's numbers this would not clear the bar to be published as a new idea at all.
  That is the test I am applying to keep it.
- action: captured via add_candidate.py, conviction 2

## [06:26 ET] POSITION UPDATE — XLE — opened 2026-08-15 @ 63.90, now 62.21, -2.6% after 88 days
- decision: **hold to the stop, do not add, do not widen.** No candidate emitted — nothing changed
  and the position resolves itself within days.
- why not a trim: XLE is still outperforming SPY on 3m (+4.85%) and 6m (+6.47%), and energy was one
  of only four green sectors on 2026-11-10 (+0.44%).
- why not an add: price 62.21 is below both SMA20 66.657 and SMA50 65.022, and 1m relative is -2.14%.
- the number that matters: the 60.80 stop is **1.41 points = 0.75 ATR** below spot on a 1.8847 ATR.
  Entry-to-stop was 1.64 ATR against the 1.8 ATR ETF floor, so this is the fourth sub-floor stop in
  the book. It will be hit by an ordinary two-day move, and that is a fact about the stop, not a
  forecast about oil.

## [06:29 ET] AWAITING-ENTRY VERDICTS — all 9 resolved
These were published but never filled, so a verdict is owed on each. Re-pitching amends; it does not
double-count.
- **`OXY` BUY @ 54.00 (2026-09-24)** — **EXPIRE.** 48 days unfilled. Price 56.90 is below both SMA20
  61.001 and SMA50 59.920, so the entry fills only on further breakdown in an established downtrend.
- **`KXCPIYOY-26SEP-T3.5` NO @ 18 (2026-09-30)** — **EXPIRE.** The contract references **September
  2026** CPI year-over-year, which has long since printed and resolved. It should never still be in
  the awaiting-entry list. Separately, `market_data.py events` returns zero markets today, so it
  cannot be re-checked even if it were live.
- **`GLD` SELL @ 406.77 (2026-10-25)** — **EXPIRE, and note the thesis was right.** GLD is 369.36,
  so the short entry sits **10.1% ABOVE market** and can never fill. Gold fell -2.68% on 11-10 alone
  and is -13.99% off its 429.42 high, below SMA20 372.04 and SMA50 383.59. The call was correct and
  the level was unreachable, which is the lesson, not the direction. Shorting here, 4.14% off the
  range low after the move, is chasing — not re-pitched.
- **`ONON` BUY @ 34.20 (2026-11-03)** — **EXPIRE, watchlist.** Price 34.70 with SMA20 34.9315 just
  overhead. No dated catalyst: ADM aside, ONON does not appear in the earnings calendar inside 20
  days, so the swing has no event. Revisions **deteriorating** -1.7pp. Already recommended 2x in 10
  days, and prior_context flags that as an anchoring signal, not conviction.
- **`TLT` BUY @ 80.30 (2026-11-04)** — **DO NOT ENTER. Wait.** Price 80.88, so the 80.30 entry is
  0.7% below market and would fill **into** the move against it. The macro is squarely opposed: 10y
  4.88% (up), 2y 4.56% (up), curve flattened to 0.25 from 0.32, TLT -1.32% on the session and below
  its SMA20 of 81.037. Condition to wait for: the 10y printing a lower high — i.e. two consecutive
  FRED DGS10 reads below 4.80 — before this level means anything.
- **`CVS` BUY @ 79.00 (2026-11-05)** — **EXPIRE.** Price 89.01 puts the entry **11.2% below market**.
  Also: CVS was **stopped out on 2026-11-04** and then republished the next day, and appears **3x in
  the last 10 days**. That is the clearest anchoring case in the book and the level is unreachable.
- **`/MBTZ6` SHORT @ 74,075 (2026-11-09)** — **CANNOT PUBLISH.** BTC spot is 73,930 so the level is
  live, and the regime (dollar +0.62%, real rates up) supports it. But `history BTC-USD` returns
  ok:false, so I have **no ATR with which to place a stop**, and config/universe.md requires a stop
  on every futures idea with no exceptions. Not re-pitched for lack of data, not lack of thesis.
- **`XLV` BUY @ 184.00 (2026-11-09)** — **EXPIRE, watchlist.** See the 06:12 rejection: best chart in
  the tape, no room between a properly wide stop and a defensible target.
- **`HUN` BUY @ 9.00 (2026-11-10)** — **RE-PITCHED, LEVEL UNCHANGED.** Captured. Nothing changed in
  one session and I am saying so rather than inventing a reason.

## [06:30 ET] REVISION-DIRECTION SCREEN — the one signal that found anything today
Most names screened are deteriorating. Checked `analysts` on 13 liquid names outside the sectors the
book is already full of; bullish-share change in points:
| Sym | bullish% | change | direction |
| --- | --- | --- | --- |
| HUN | 33.3 | **+23.8** | improving |
| ADM | 33.3 | **+22.8** | improving |
| GM | 82.9 | +6.0 | improving |
| KEY | 64.0 | +5.7 | improving |
| C | 82.8 | +4.2 | improving |
| F | 42.9 | +2.9 | improving |
| GIS | 10.7 | 0.0 | flat |
| CAG | 4.0 | 0.0 | flat |
| CF | 41.9 | -1.4 | deteriorating |
| ONON | 81.6 | -1.7 | deteriorating |
| MOS | 40.0 | -8.0 | deteriorating |
| ACM | 76.5 | -6.8 | deteriorating |
| TJX | 77.8 | -6.8 | deteriorating |
Both large positives are deeply de-rated cyclicals at their lows (HUN -40.9% off high, ADM -21.9%),
which is what a revision cycle turning looks like before price confirms. Both captured.

## [06:30 ET] REJECTED — C (Citigroup) — four straight beats (+5.1/+12.7/+13.3/+6.0%) and revisions improving +4.2pp, 17.4% off its high, but it is "lagging SPY on every window measured" (-7.32% 1m, -11.13% 3m, -3.30% 6m) while its own sector XLF leads on all three. The weak horse in the strong race, and zero insider activity in six months to argue otherwise.
## [06:30 ET] REJECTED — KEY (KeyCorp) — the best-shaped bank: above a rising SMA20 20.9385 and SMA50 20.8534, +6.22% 1m vs SPY -3.62%, revisions improving +5.7pp, four straight beats, and a 23.01 target inside the 19.45-24.065 range. Killed by two things: 3 insider sales of $1,898,048 with zero buys, and the macro — the 10y-2y curve flattened to **0.25 from 0.32** in a day, which compresses exactly the net interest margin a regional bank is a bet on. Would not reject on the curve alone; do reject on the curve plus insiders selling.
## [06:30 ET] REJECTED — TGT — earnings 11-18 and -5.25% off its high, but ATR14 is 6.117 (3.78%) and a 2.0-ATR stop from a 158 entry puts the 2:1 target at 182.46, which is **6.9% above the 170.75 range high**. Same no-room failure as XLV, LOW, HD, DIS, WMT. The retail prints on 11-18 are a calendar event with no tradeable geometry behind them today.

## [06:31 ET] FALSIFICATION PASS — every captured number recomputed from source
Recomputed reward-to-risk, stop-distance-in-ATRs, break-even baseline and the evidence-kind count for
all captured candidates independently of what I wrote in them. Result: **every claimed figure matches
the recomputation.** Details and the four deliberate exceptions:

| Sym | hor | cv | entry | stop | target | R:R | ATRx | floor | wp | baseline | edge |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ACM | swing | 4 | 66.74 | 61.50 | 77.22 | 2.00 | 2.46 | 2.0 | 0.44 | 0.333 | +10.7 |
| KHC | swing | 3 | 23.00 | 21.20 | 28.09 | 2.83 | 2.29 | 2.0 | 0.40 | 0.261 | +13.9 |
| HII | swing | 3 | 262.00 | 235.00 | 339.76 | 2.88 | 2.01 | 2.0 | 0.40 | 0.258 | +14.2 |
| HUN | swing | 3 | 9.00 | 8.00 | 11.00 | 2.00 | 2.19 | 2.0 | 0.42 | 0.333 | +8.7 |
| ADM | swing | 3 | 68.80 | 64.40 | 78.00 | 2.09 | 2.10 | 2.0 | 0.40 | 0.324 | +7.6 |
| PFE | long_term | 4 | 27.60 | none | 42.00 | 4.00 (vs 24.00 bear) | n/a | n/a | — | — | — |
| AAL | swing | 2 | 13.35 | 14.40 | 10.60 | 2.62 | **1.61** | 2.0 | **0.15** | 0.276 | **-12.6** |
| BCC | long_term | 2 | 76.50 | none | 110.00 | **2.31** (vs 62.00 bear) | n/a | 2.5 | — | — | — |

No claimed edge exceeds 20 points over baseline, so nothing is making a large claim it cannot carry.

**ADM was corrected during this pass, and the correction matters.** As first captured it had entry
69.20 / stop 64.80 / target 78.00, which is 8.80/4.40 = exactly 2.00 — and in floating point lands a
hair *under* the 2.0 floor, so validation could have failed it. The wrong fixes were available and
rejected: tightening the stop (the KRE abuse) or lifting the target (the same abuse aimed at the
target, which I spent the 06:23 META note objecting to). The fix taken was to move the **entry down
onto the real level** — 68.80 is the 120-day low of 68.793 itself rather than a 0.9% discount off the
last print — which gives R:R 2.09 and a 2.10 ATR stop with the target untouched. Re-captured; the
last line per symbol wins.

**The four flags that are intentional, so the red team does not "fix" them:**
1. **AAL stop 1.61 ATR, under the 2.0 floor** — inherited, not newly set. It was under the floor the
   day it was published; I am not widening a stop on a position I am telling you to close.
2. **AAL expectancy negative (0.15 vs a 0.276 break-even)** — written deliberately. It is the
   machine-readable statement that this position no longer has an edge, and it should fail enforcement
   and demote. That is the intended outcome, not a number to repair.
3. **BCC 2.31 against the 2.5 long_term floor** — also deliberate. Priced against an honest 62.00
   bear case, the position would not clear the bar to be published as a new idea today, which is the
   argument for closing it.
4. **AAL conviction 2 (2 kinds) and BCC conviction 2 (3 kinds) are both scored BELOW what the kind
   count mechanically supports.** This is on purpose and is the safe direction of error: in both the
   evidence listed argues for the **exit**, not for the position, and counting evidence-against as
   conviction-for would invert the meaning of the score. Do not raise them to 3 and 4.

## [06:32 ET] CALENDAR — TODAY IS VETERANS DAY: EQUITIES OPEN, BOND MARKET CLOSED
- US **stock market trades regular hours** 09:30-16:00 ET; Veterans Day is not an NYSE holiday.
  source: https://daytradingtoolkit.com/day-trading-basics/stock-market-holidays-schedule
- **SIFMA recommends a full close of the US fixed income market**, and **Federal Reserve Banks are
  closed**. sources: https://www.sifma.org/news/press-releases/sifma-fixed-income-market-close-recommendation-in-the-u-s-the-u-k-and-japan-for-the-u-s-veterans-day-holiday-2026
  https://fedratecalc.com/is-the-stock-market-open-on-veterans-day/
- Three consequences that matter for today's report:
  1. **No economic releases and no FRED refresh.** My 10y 4.88% / 2y 4.56% reads are dated 2026-11-09
     and the curve 2026-11-10; they will **not** update today. Anything quoting a rate today must
     carry those dates, not "as of today".
  2. **TLT will trade with no cash-bond price discovery.** Bond ETFs still trade on the exchange, but
     the underlying cash market is shut, so today's TLT print is flow, not a yield signal. This is an
     independent second reason not to enter the 80.30 TLT level today, on top of the macro one.
  3. Equity volumes are typically thin on a partial holiday, which argues against initiating at the
     open and in favour of the limit entries used in every candidate captured.

## [06:33 ET] CORRECTION — ACM EARNINGS DATE IS NOT CLEANLY CONFIRMED, AND MY FIRST CAPTURE OVERSTATED IT
My 06:18 ACM capture said "Q4 FY26 earnings confirmed for 2026-11-16 after market close". The finnhub
calendar does say `2026-11-16 ACM amc`, but checking it against other sources it is **not confirmed
by the company**:
- Earnings Whispers: 2026-11-16, after close, 16:30 ET — https://www.earningswhispers.com/stocks/acm
- MarketBeat: **estimated** 2026-11-17 and states AECOM **has not confirmed** the date —
  https://www.marketbeat.com/earnings/reports/2025-11-18-aecom-stock/
- And AECOM's own Q4 history argues for **before the open**, not after the close: for Q4 FY2025 the
  company said it would issue results **before the US market opens** on 2025-11-18, and the Q3 FY2026
  pattern was results followed by an 08:00 ET call the next morning —
  https://secure.businesswire.com/news/home/20260720279851/en/AECOM-announces-planned-dates-for-third-quarter-fiscal-2026-earnings-results-and-conference-call
- I found **no AECOM press release** fixing the Q4 FY2026 date.
**Why it changes the instruction, not just the footnote:** "trim half into the 11-16 AMC print" fails
if the print is actually 11-17 before the open — a reader acting on the morning of 11-17 is already
gapped. The robust instruction is to **be trimmed by the close on Monday 2026-11-16**, which covers
both the 11-16-after-close and 11-17-before-open cases. Re-capturing ACM with that.
Conviction stays 4: the kind count is still three (dated_catalyst, technical_level, positioning) and
the scale is a mechanical count of kinds, not a quality judgement. The uncertainty belongs in the
evidence detail and key_risk, where the red team can see it, rather than hidden in a lowered score.

## [06:30 ET] CORRELATION CHECK — config/strategy.md caps ideas sharing one driver at 3
Counting candidates PLUS the positions being held unchanged, because the cap is about the book, not
about today's page:
| Driver | Names | Count |
| --- | --- | --- |
| Healthcare | PFE (candidate), ABT (hold), SMMT (hold, biotech) | **3 — AT THE CAP** |
| Defence | HII (candidate, trimming), RTX (hold) | 2, falling to ~1.5 on the trim |
| Food / agriculture | KHC (candidate), ADM (candidate) | 2 |
| Rates-sensitive | XLU (hold), TLT (not entered) | 1 live |
| Energy | XLE (hold) | 1 |
| Everything else | ACM infrastructure, HUN chemicals, PYPL fintech, UNP rail | 1 each |
- **Healthcare is at the cap at 3**, which is the reason XLV was rejected rather than merely a
  geometry call — even had it cleared the floor it would have been a fourth healthcare bet.
- **KHC and ADM are flagged as a judgement call rather than hidden.** I count them as two drivers:
  KHC is branded packaged-food volumes, ADM is agricultural processing and crush margins, and the two
  have historically moved on different things. A reader who thinks "food is food" should treat this as
  one 4.5% position rather than two, and that is a reasonable view. Either way it is under the cap.
- Nothing in the book depends on a single macro print, so there is no concentrated event risk to flag
  — mostly because the one lane that would have created it (event contracts) had no data.

## [06:31 ET] WHAT TODAY'S REPORT HONESTLY IS, FOR data_quality_notes
Synthesis should say this plainly rather than presenting eight ideas as eight fresh opportunities:
- **Six of the eight are position management, not new ideas.** ACM, KHC, HII, PFE (hold/trim/
  accumulate) and AAL, BCC (close). One is an unchanged re-pitch (HUN). **Exactly one is new (ADM).**
- That is not a thin research day, it is what the tape offered. The market is split cleanly: the
  leaders are 1-5% off their 120-day highs so a 2.0-ATR stop puts every 2:1 target above the range
  high (XLV, LOW, HD, DIS, WMT, BJ, TGT all rejected for this), and the names with room are below
  falling moving averages with no support to anchor a stop (AMAT -49.6%, CSCO, KEYS, PANW rejected
  for this). There was no large middle.
- **Nothing intraday.** No intraday setup cleared the bar and none was manufactured; today is also a
  partial holiday with the bond market shut, which is the wrong tape to day-trade on thin volume.
- **No crypto, no futures, no event contracts** — all three lost to data sources, not to judgement.
  Event markets returned zero rows, crypto history returned no ATR, options-implied returned 401.
  The `/MBTZ6` short had a live level and a supportive macro read and was still not published because
  a futures idea without a stop is not publishable.
- **Two prices in this report are live pre-market** (ADM 69.61 via nasdaq depth at 06:20 ET,
  spread 0.187%). Every other price is the **2026-11-10 close** — a closed market, not stale data.
- The single most useful output today may not be a trade at all: see the 06:23 META note. Seven of
  fourteen open positions carry a target sitting on or above their own 120-day high, and four carry a
  stop tighter than the ATR floor now enforced. That combination — a target needing a breakout and a
  stop triggered by an ordinary pullback — is a mechanical explanation for the 10% hit rate that does
  not require any of the theses to have been wrong.

## [06:31 ET] RESEARCH COMPLETE
- **candidates captured: 8 distinct symbols** (10 lines; ACM and ADM were each re-captured after the
  falsification pass, and the last line per symbol wins)
  - ACM cv4 swing buy — trim half by the 11-16 close
  - PFE cv4 long_term buy — continue accumulating
  - ADM cv3 swing buy — NEW idea, entry 68.80 on the 120-day low
  - HII cv3 swing buy — TRIM HALF at market, add a 235.00 stop to an unprotected +19.7%
  - KHC cv3 swing buy — hold, unchanged
  - HUN cv3 swing buy — re-pitch, level unchanged at 9.00
  - AAL cv2 swing sell_short — **CLOSE AT MARKET**
  - BCC cv2 long_term buy — **CLOSE AT MARKET**
- **NVDA is not in the list on purpose**: its 166.00 stop was touched on 2026-11-10 (bar low 165.89),
  so the position is already closed and cannot be amended. See 06:10.
- **all 14 open positions decided** (8 above as candidates or already-closed, 6 logged as hold/no
  change at 06:21 and 06:26: RTX, UNP, ABT, PYPL, SMMT, XLU, XLE)
- **all 9 awaiting-entry levels resolved** at 06:29
- coverage gaps: event contracts (source returned 0 markets), crypto and crypto futures (no ATR
  available), options-implied move (HTTP 401), index levels and VIX (yahoo 429 / finnhub paywall),
  short interest for HUN (nasdaq read timeout), TGT and ATKR history on first attempt (TGT succeeded
  on retry). No 8-K / filings sweep was run on individual names — insider, analyst and price data
  were used instead, so no candidate rests on a document I claim to have read.
- sources that failed: yahoo (429 on indices, 401 on options), finnhub (indices paywalled),
  stooq (404 on ^-prefixed symbols), alphavantage (no key), kalshi via events (empty), nasdaq
  (timeout on HUN short interest), market_data.py history for BTC-USD.
- **research was NOT truncated.** Ran 06:00:52 to 06:31 ET, roughly 31 minutes of a ~60 minute
  budget, and stopped because the work was done: every position decided, every pending level
  resolved, and the remaining idea lane rejected on geometry rather than left unexamined. Prior runs
  have been misread as truncated by later phases, so stating it explicitly.
