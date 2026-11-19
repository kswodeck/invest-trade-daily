# Research log — 2026-11-19

## [06:02 ET] SETUP
- Research start 06:01 ET, ~60 min budget. Minute-20 hard deadline 06:21; 70% cutoff 06:43.
- Prior context read: 13 open positions, 9 awaiting entry, 44 closed of 73 tracked.
- **Track record is poor and the sample is no longer noise**: 5/44 hit target (11%), avg -5.5%.
  stock 2/30 (7%), avg -7.1%. etf 3/14 (21%), avg -1.9%. long_term 0/4, avg -15.2%.
  By conviction: 2s are 0/6 avg -8.4%; 3s are 3/29 avg -6.4%; 4s are 2/9 avg -0.4%.
- Implication for today's bar: conviction-3 single-stock swing longs are the losing
  core of this book. 44 closed is past the ~15 noise threshold. I will bias toward
  (a) fewer ideas, (b) evidence-backed 4s, (c) ETFs/futures/event contracts over
  single-name swing longs, and will not pad the count.

## [06:06 ET] PRICE BASIS
All equity prices below are the **2026-11-18 regular-session close**, fetched
from finnhub/nasdaq at 06:0x ET on 2026-11-19. Market session is `pre`; the
previous close is the freshest honest equity price at this hour, not stale data.
`market_data.py macro` has not returned (slow source) — see DATA GAPS.

## [06:06 ET] OPEN POSITION DATA (close 2026-11-18, ATR14 from 150d history)
| Sym | Close | ATR14 | %ATR | SMA20 | SMA50 | Entry | Stop | ATRs to stop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BCC | 65.71 | 3.41 | 5.19 | 72.78 | 74.34 | 76.50 | 64.50 | 0.35 |
| OXY | 53.76 | 2.00 | 3.71 | 59.46 | 59.47 | 54.00 | 50.15 | 1.81 |
| HII | 287.89 | 11.67 | 4.05 | 298.72 | 281.18 | 262.00 | none | n/a |
| ONON | 32.43 | 1.77 | 5.46 | 34.33 | 32.46 | 34.20 | 30.69 | 0.98 |
| DKS | 144.69 | 6.26 | 4.33 | 144.28 | 138.18 | 144.50 | 129.00 | 2.50 |
Other closes: PFE 28.06, KHC 25.44, UNP 300.90, ABT 104.48, PYPL 57.89,
RTX 197.45, XLU 43.55, TLT 80.22. Index closes: SPY 730.20, QQQ 659.51,
IWM 270.12.

## [06:07 ET] CALENDAR — earnings in the next 10 sessions (finnhub, fetched)
- 2026-11-19 (today): WMT (bmo), BABA (bmo), INTU (amc), KEYS (amc), ESTC (amc),
  POST (amc), NTES (bmo), FUTU (bmo), VVV (bmo), GLOB (amc), HP (amc)
- 2026-11-20: BJ (bmo), FRO (bmo), IESC (bmo), MOG.A (bmo), RLX (bmo)
- 2026-11-23: **DKS (open position)**, A (amc), HPE (amc), ZM (amc), ANF, BURL,
  KSS, URBN, SYM (amc), WOOF, GES, CENT, FLNC, SMTC
- 2026-11-24: ADI (bmo), DELL (amc), HPQ (amc), MDT (bmo), WDAY (amc), BBY (bmo),
  ADSK (amc), NTNX (amc), AMBA (amc), SJM (bmo), DY (bmo), BILI (bmo)
- 2026-11-25: DE (bmo), BZ (bmo), FINV (amc), NNOX (bmo)
- 2026-11-26: MRVL, PD, NAT (bmo), REX (bmo)
- 2026-11-30: AEO, RBRK, NNE, SLP (amc)
**The retail cluster on 11/23-11/24 is the dominant dated catalyst of the week**
(DKS, ANF, BURL, KSS, URBN, BBY, plus WMT this morning setting the tone).

## [06:10 ET] POSITION UPDATE — DKS — opened 2026-11-13 @ 144.50, flat (close 144.69)
- decision: **hold, but halve into the print**. Entry unchanged (filled, cannot be amended).
- why: Q3 earnings 2026-11-23 confirmed on the fetched calendar. 7 distinct insiders,
  9 open-market buys, $5.59M, 2026-08-26 to 2026-09-30 at 128.70-136.39 — i.e. after
  the Q2 miss and below today's price. Against that: bullish analyst share 61.3% -> 53.1%
  over four months, and DKS missed Q3 2026 EPS by 7.1%.
- levels: stop 129.00 (2.48 ATR, below the 138.50/139.75 shelf of 11/05-11/06),
  target 175.50, R:R exactly 2.00 — at the floor, not above it. Size cut to 1.5%.
- action: captured via add_candidate.py, conviction 4 (dated_catalyst + positioning +
  technical_level = 3 distinct kinds).
- data gaps on this name: `short DKS` timed out (nasdaq), `implied DKS` returned
  yahoo-options 401 — so no short-interest or options-implied-move confirmation.

## [06:12 ET] MACRO — the 2026-11-18 tape was a commodity/reflation unwind, not broad risk-off
Closes 2026-11-18 (all fetched via market_data.py quote/history at 06:1x ET 11-19):
- GLD 341.19 **-3.20%** on 13.5M sh (vs ~8M typical) — 0.13% off its 150-day low
  of 340.76, -23.96% from the 448.70 high, SMA20 364.30 / SMA50 377.64 both above.
- XLE 61.29 **-3.27%** on 54.6M sh (~2x normal) — broke the 61.21-62.43 shelf of
  11/05-11/10. SMA20 65.39 / SMA50 64.87 above. 150d low 52.62.
- XOP 171.57 -3.40%, USO 136.11 -2.94% — confirms it is crude, not a single name.
- XLV 181.17 -2.20%.
- Against that: TLT 80.22 **+0.84%** (bonds bid), XLU 43.55 **+0.30%**, QQQ 659.51
  +0.39%, IWM 270.12 +0.40%, SPY 730.20 -0.31%.
**Read: gold, crude and energy equity were liquidated together while bonds and
utilities caught a bid and the Nasdaq rose.** That is an unwind of the reflation
trade / a disinflation-or-growth-scare rotation — not a general de-risking. It is
the single most important fact for today's book, because the open positions sit
on both sides of it.
- Crypto (coingecko, 24h): BTC $63,676 -0.73%, ETH $1,801.53 +0.13%, SOL $74.39 +0.03%.
  BTC is quiet while gold collapses — the "debasement trade" is not moving together.

## [06:13 ET] STALE AWAITING-ENTRY ORDERS — both now meaningless, say so rather than re-pitch
- `GLD SELL @ 406.77` (published 2026-10-25): GLD closed 341.19. The level is
  **16.1% above the market** and gold has already fallen 24% from its high. This
  order can never fill on the thesis that motivated it. Do not re-pitch at 406.77.
- `/MBTZ6 SHORT @ 74,075` (published 2026-11-09, 2x): BTC spot $63,676, i.e. the
  short entry is **~16% above spot**. Directionally the call was right and it
  never filled. Re-pitching the same 74,075 level is anchoring, not conviction.

## [06:15 ET] DATA GAPS — sources that failed or returned garbage
- `market_data.py macro` — started 06:05 ET, still had produced **zero bytes** many
  minutes later. No fetched read on rates, VIX, DXY or FRED series today. The macro
  regime read above is built from ETF/commodity-proxy closes instead, which is
  weaker but is actually fetched.
- `market_data.py events` — **unusable today.** "Fed" returns Kalshi
  `KXMVECROSSCATEGORY` multi-leg sports parlays matching the substring "Federico";
  "CPI" returns a football parlay. "Federal Reserve", "interest rate", "recession"
  and "Bitcoin" all return count 0. Every market returned has `yes_ask`,
  `last_price` and `volume` = null. **No event-contract idea today**, and the reason
  is a broken source, not an absence of opinion.
- `market_data.py short DKS` — nasdaq ReadTimeout. No short-interest reads today.
- `market_data.py implied <sym>` — yahoo-options HTTP 401 Unauthorized. **No
  options-implied-move check is available on any idea today**, so the
  "is the target inside what the market prices" test could not be run at all.

## [06:18 ET] NEWS — the 2026-11-18 healthcare break has a named, dated cause
- CMS proposed a rule on **2026-11-16** broadening oversight/audits of Medicare
  Advantage and Medicare Part D plans. Managed care sold off hard on 11/18:
  UNH -10.21%, HUM -12.98%, CVS -5.20% (85.81 -> 81.35 on 17.6M sh, ~1.5x normal).
  XLV -2.20% to 181.17. Also cited for CVS specifically: a Glenview Capital
  position reduction and doubts about the planned breakup.
  — source: https://www.tradingkey.com/news/market-movers/262311782-market-movers-cvs-20261118
  — source: https://beinsure.com/news/healthcare-stocks-fall-as-medicare-rules-trigger-a-selloff/
- **This is the dominant single-sector event of the session** and it reframes two
  of the book's awaiting-entry orders (CVS @ 77.50, XLV @ 184.00). It is a
  *proposed* rule, which means a comment period and a final rule — but it is also
  the kind of overhang that does not clear in a week.
- Correlation discipline: CVS + XLV are already two live orders on this one
  driver. The cap is 3. I will not stack more managed-care names on top of it.

## [06:18 ET] AWAITING-ENTRY REVIEW (closes 2026-11-18)
| Order | Entry | Close 11/18 | Read |
| --- | --- | --- | --- |
| GLD SELL @ 406.77 | 406.77 | 341.19 | **dead** — 16% above market, gold already -24% |
| /MBTZ6 SHORT @ 74,075 | 74,075 | BTC $63,676 | **dead** — 16% above spot, never fills |
| CVS BUY @ 77.50 | 77.50 | 81.35 | live; 150d low 76.10; now a CMS-rule knife |
| XLV BUY @ 184.00 | 184.00 | 181.17 | traded 180.74-185.29 on 11/18 — level reached |
| HUN BUY @ 9.00 | 9.00 | 9.03 | at the level; 150d low 7.995, -43.9% off high |
| ADM BUY @ 68.80 | 68.80 | 67.78 | traded 67.52-68.77 on 11/18 — level reached |
| LEN BUY @ 79.50 | 79.50 | 82.91 | not reached; 150d low 71.78 |
| IWM SELL_SHORT @ 270.50 | 270.50 | 270.12 | at the level; see IWM note below |

## [06:22 ET] SCREEN — insider buying across the 11/23-11/24 retail earnings cluster
`market_data.py insiders`, 6-month window, open-market (Form 4 code P) only:
| Sym | Buys | Distinct buyers | Buy $ | Sells | Net $ |
| --- | --- | --- | --- | --- | --- |
| **DKS** | **9** | **7** | **5,588,664** | 2 | **+1,007,325** |
| ANF | 0 | 0 | 0 | 9 | -10,595,392 |
| BURL | 0 | 0 | 0 | 39 | -14,359,239 |
| KSS | 0 | 0 | 0 | 6 | -1,814,990 |
| URBN | 0 | 0 | 0 | 8 | -3,369,147 |
| BBY | 0 | 0 | 0 | 20 | -189,725,901 |
| AEO | 0 | 0 | 0 | 5 | -326,373 |
| FIVE | 1 | 1 | 93,309 | 19 | -5,552,710 |
| DLTR | 0 | 0 | 0 | 14 | -248,742,763 |
**DKS is the only name in the whole cluster with real open-market insider buying,
and it is the only one with net-positive insider dollars.** Eight peers reporting
in the same week show zero buys between them. That is what makes DKS the retail
idea rather than one of nine, and it is the reason there is no second retail
candidate today — adding one would be filling a slot, not finding an edge.

## [06:23 ET] REJECTED — UNH / HUM / ELV — the knife is real but the swing arithmetic fails
CMS-6098-P (proposed 2026-11-16) applies extrapolation to Medicare Advantage RADV
audits from payment year 2018 forward and requires insurers to remit improper
payments; CMS estimates $90.2B of recoveries 2027-2036. **Comment period closes
2027-01-19** — source: https://mlq.ai/news/unitedhealth-and-humana-fall-after-cms-proposes-a-90-billion-anti-fraud-rule/
Closes 11/18: UNH 349.91 (-10.21%, 17.4M sh ~4x normal, low 342.455),
HUM 385.78 (-12.98%, low 384.61), ELV 400.84 (-7.63%), HCA 476.35 (-4.96%).
Why I am not buying it as a swing, with the arithmetic shown for UNH:
- ATR14 14.59. A stock swing stop must clear 2.0 ATR = 29.17 from entry. From a
  350.00 entry that caps the stop at 320.83; the honest level is 316.00, below the
  150d base low of 317.135, = 2.33 ATR. Risk 34.00.
- R:R 2.0 then demands a target of **418.00** — above the 412.02 close of 11/16 and
  a full round-trip of the selloff. The realistic bounce objective is the 387.14
  gap and the 390.64 SMA50, which gives **R:R 1.15**. It fails.
- The only way to publish it is to tighten the stop, which is the exact move
  `check_stop_distance` exists to refuse. So: **rejected, not re-levelled.**
- Supporting: UNH shows **0 open-market insider buys in 6 months** (2 sells,
  -$660,910 net), so there is no positioning confirmation either.
- And the dated catalyst is 2027-01-19 — two months out, outside a swing horizon.

## [06:23 ET] REJECTED — XLV as a swing (the awaiting order at 184.00)
XLV 181.17, ATR14 3.73, SMA50 176.03, 150d high 192.32. An ETF swing stop must
clear 1.8 ATR = 6.72; from 181.00 the honest stop is 173.50 (below the SMA50,
2.01 ATR), risk 7.50. R:R 2.0 then requires a **196.00** target — above the
150-day high. A target that has to exceed the range high to clear the floor is a
reverse-engineered target. Rejected as a swing. The level being "reached" on
11/18 (traded 180.74-185.29) does not rescue the arithmetic.

## [06:15 ET] NOTE ON TIMESTAMPS
Entries above carry headings a few minutes ahead of the wall clock; the real
elapsed time at this point is 06:15 ET. Times from here are read from `date`.

## [06:16 ET] RELATIVE STRENGTH — the decisive read on four open positions
`market_data.py relstrength`, 1m / 3m / 6m, each against its own peer ETF:
| Sym | 1m | peer | peer 1m | vs peer 1m | vs peer 6m | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| BCC | -13.86% | XHB | **+4.71%** | **-18.57%** | -4.18% | peer group rising while it falls |
| OXY | -14.56% | XLE | -9.83% | -4.73% | -11.17% | lagging a sector that is itself breaking |
| HII | **+5.75%** | ITA | +0.98% | +4.77% | -3.80% | leader; +10.8% vs SPY on 1m |
| ONON | -8.44% | XRT | +2.96% | -11.40% | -25.86% | lagging badly |
| DKS | +1.13% | XRT | +2.96% | -1.83% | -45.51% | de-rated, but no longer underperforming |

## [06:17 ET] POSITION UPDATE — BCC — opened 2026-08-18 @ 76.50, close 65.71, -14.1%
- decision: **close the position at the open. Do not wait for the 64.50 stop.**
- why: BCC is -13.86% over one month while **XHB, its own sector ETF, is +4.71%** —
  18.6 points of underperformance against the exact peer group the thesis was
  about. A housing/building-products thesis cannot be right while homebuilders
  rally and this name alone makes new lows. The 11/18 close of 65.71 sits 1.55%
  above the 150-day low of 64.71 printed that same session, and the 64.50 stop is
  **0.35 ATR away (ATR14 3.41)** — it is not a risk control any more, it is a
  near-certainty that will fill on the next ordinary down day, at the low, with
  slippage. SMA20 72.78 and SMA50 74.34 are both far overhead.
- not captured as a candidate, deliberately: the only amendment that expresses
  "get out" is a stop walked up to ~65.50, which is 0.06 ATR and would fail
  `check_stop_distance` and be demoted — i.e. publishing it would be the exact
  stop-tightening the repo refuses. **Synthesis must carry this as a close
  instruction in the report text, not as a tradeable idea.**
- BCC was recommended 2x in the last 10 days. That repetition was the anchoring
  signal the prior-context file warns about. It stops here.

## [06:18 ET] POSITION UPDATE — OXY — opened 2026-09-24 @ 54.00, close 53.76, -0.4%
- decision: **close the position at the open rather than ride to the 50.15 stop.**
- why: two independent things broke at once on 11/18. (1) The sector: XLE -3.27%
  to 61.29 on 54.6M shares, ~2x normal, snapping the 61.21-62.43 shelf that held
  from 11/05 to 11/10; XOP -3.40%, USO -2.94%, so it is crude and not one name.
  (2) The name: OXY -4.88% to 53.76, below the 59.46 SMA20 and 59.47 SMA50 which
  are sitting on top of each other — and OXY is **-14.56% over one month against
  XLE's -9.83%**, lagging its own sector by 4.73% on 1m and 11.17% on 6m.
- The position is only flat after 8 weeks because it was 4.7% up two days ago.
  Getting out at roughly the entry price, with the sector shelf broken and the
  name a laggard inside it, is a better outcome than the 50.15 stop (-7.1%).
- Not captured as a candidate for the same reason as BCC.

## [06:19 ET] POSITION UPDATE — HII — opened 2026-10-12 @ 262.00, close 287.89, +9.9%
- decision: **hold. No stop added, and that is a stated choice, not an oversight.**
- why: HII is **+5.75% on 1m against ITA's +0.98% and SPY's -5.05%** — it is
  leading, not breaking. The 4-session slide from 313.96 (11/11) to 287.89 is a
  pullback inside that leadership, and ITA itself was only -0.30% on 11/18, so
  nothing sector-wide happened. 287.89 is below the 298.72 SMA20 and above the
  281.18 SMA50.
- why no stop: the honest invalidation here is 281.18 (the SMA50), which sits
  **above** the 262.00 entry. `check_stop_distance` measures `abs(entry - stop)`
  against a 2.0 ATR floor (ATR14 11.67 -> 23.34 required), so a profit-protecting
  trailing stop at ~281 measures 1.37 ATR and would fail validation and demote the
  idea. A stop placed low enough to pass (<= 238.66) would be below the 255.36
  150-day low and would give back the entire gain — it would be a worse risk
  control than none. So: **invalidation is a weekly close below 281.18**, carried
  as text, and the position is not re-published as a candidate.

## [06:20 ET] POSITION UPDATE — ONON — opened 2026-11-03 @ 34.20, close 32.43, -5.2%
- decision: **hold to the existing 30.69 stop, do not add, do not amend.**
- why: ONON is -8.44% on 1m while XRT is +2.96% — 11.4 points of underperformance
  against its own peer group, and -25.86% over 6m. Close 32.43 is below the 34.33
  SMA20 and sitting exactly on the 32.46 SMA50; the 30.69 stop is **0.98 ATR away
  (ATR14 1.77)**, which is inside a single ordinary day's range. There is no
  amendment that improves this: widening the stop after the fact adds risk to a
  losing position, and tightening it is the forbidden move. Let the stop work.

## [06:21 ET] CORRECTION to the UNH rejection above
The 06:23-headed note said a 418.00 swing target would be "a full round-trip of
the selloff". That is true, but I should have added that 418.00 is still **inside**
the 150-day range (high 461.62) — unlike the XLV case, where the required target
sat above the range high. So the swing rejection rests on catalyst timing (the
resolving event, the comment-period close, is 2027-01-19 — two months beyond a
swing horizon) and on the absence of any positioning confirmation (0 open-market
insider buys in 6 months), **not** on the target being unreachable in principle.

## [06:21 ET] CAPTURED — UNH — long_term accumulation, conviction 4, WAIT below 325
Not a swing and not a bounce trade. Numbers, all fetched:
- TTM reported EPS **$20.41** = 4.69 + 6.38 + 7.23 + 2.11, four actuals from the
  finnhub surprise history. Close 349.91 = **17.14x**. Entry 317.50 = 15.56x.
- Shares outstanding **897.59M** (finnhub profile). Close 11/16 412.02 -> close
  11/18 349.91 = **$55.75B of market value gone in two sessions**; 11/18 alone was
  $35.70B. Market cap at the close $314.08B.
- CMS's own impact estimate for CMS-6098-P is **$90.2B across the whole MA
  industry over 2027-2036** — ten years, undiscounted, every plan. That is 1.6x
  what this one company lost in two days.
- target 408.20 = 20.0x the EPS already reported (the multiple it held on 11/16);
  bear 285.74 = 14.0x, below the 317.135 150-day low. **R:R 2.86** vs the 2.5
  long-term floor; baseline win prob 1/(1+2.86) = 25.9%, claimed 45%.
- conviction 4 = valuation_anchor + technical_level + counter_argument_answered.
  I deliberately did **not** count analyst revisions as a positioning
  confirmation: the 84.4% bullish share is measured as of 2026-11-01, two weeks
  before the proposal, so it says nothing about the thing that moved the stock.
- **The recommendation is to wait.** 317.50, not 349.91. That is a real level
  (the 150-day low), not a reflex discount, and the comment period gives two
  months in which it can be reached.

## [06:22 ET] WHY TODAY YIELDS FEW SWING LONGS — the arithmetic, not a mood
A stock swing must clear a 2.0 ATR stop floor *and* a 2.0 reward-to-risk floor.
Together those force a target **4.0 ATR above entry**. For a 3.75%-ATR name that
is roughly +15%; for a 4.3%-ATR name, +17%. So a swing long only qualifies if it
sits at least that far below its own range high — otherwise the required target
has to be printed above the high, which is the reverse-engineered target the
repo refuses. This is exactly why DKS qualifies (-40.8% off its 150-day high,
target 175.5 against a 244.38 high) and why **XLV (-5.8% off high) and ADSK
(-9.4% off high) cannot**, however good the story is. Today's tape is full of
names 5-12% off their highs. That is a thin day for this lane, and the honest
response is to publish fewer rather than to shave stops.

## [06:22 ET] REJECTED — ADSK — right signal, wrong distance
ADSK was the only name besides DKS in 20 screened with net-positive insider
dollars: 4 open-market buys, 3 distinct buyers, $1.67M, and **zero sells** —
earnings 2026-11-24 amc on the fetched calendar. But the buys were 2026-05-29 to
2026-06-23 at 189.20-231.34, five to six months ago and 8-25% below the 253.00
close, so the signal has already paid. And the levels fail: ATR14 9.49, so a 2.0
ATR stop from 253.00 caps at 234.02 (honest level 233.00, below the 236.95 SMA50,
2.11 ATR, risk 20.00), which demands a **293.00** target against a 150-day high of
279.24. Above the range high. Rejected rather than re-levelled.

## [06:26 ET] WATCHLIST — LEN — Berkshire Hathaway bought $329M of it, and the levels still do not qualify today
The find of the morning, and it does not become a recommendation. Facts:
- **BERKSHIRE HATHAWAY INC filed 24 open-market purchases (Form 4 code P) dated
  2026-10-02, 1,259,982 shares across the prints shown, $329,017,222, at
  77.12-81.90. Zero sells in the six-month window.** LEN closed 82.91 on 11/18 —
  just above the top of Berkshire's own accumulation band.
- The sell side hates it: bullish share **7.1%** (2 strong_buy, 0 buy, 11 hold,
  13 sell, 2 strong_sell at 2026-11-01), revision direction deteriorating.
- The company has **missed all four of its last four quarters**: -13.7%, -3.9%,
  -1.1%, -9.2%. TTM reported EPS 1.93+0.93+1.24+1.19 = **$5.29**, so 82.91 is 15.7x
  on a declining earnings series.
- Relative strength is *fine*, unlike BCC: LEN +5.42% on 1m against XHB +4.71% and
  SPY -5.05%. The slide from 93.53 (11/05) to 82.91 gives back a spike; it is not
  the name decoupling from its sector.
Why it is not a recommendation today, with the arithmetic:
- **As a swing it has no catalyst.** LEN is not on the fetched earnings calendar
  through 2026-12-01 (fiscal Q4 reports mid-December). A swing catalyst has to be
  a specific thing at a specific time, and there isn't one inside ten sessions.
  The levels would otherwise work: entry 79.50, stop 71.00 (below the 71.78
  150-day low, 2.20 ATR on ATR14 3.87), target 96.50 (inside the 97.94 150-day
  high) = R:R exactly 2.00.
- **As a long_term it fails the 2.5 floor.** Mid-cycle anchor: the best quarter
  actually reported (2025-12-31, $1.93) annualised is $7.72; at 13x that is
  $100.36. Bear: the latest quarter ($1.19) annualised is $4.76; at 13.6x that is
  $64.74. From a 79.50 entry that is R:R **1.41** against a 2.5 floor. Clearing
  2.5 would need a $116.40 target — above the 150-day high and 22x mid-cycle.
  That is not a valuation, it is a number chosen to pass.
- **Watchlist condition that makes it actionable**: a print back inside Berkshire's
  own band, i.e. below 79.50, *or* the fiscal-Q4 report in December arriving as a
  dated catalyst. Either one, and the arithmetic above is already done.

## [06:27 ET] WATCHLIST — HUN — CEO bought, no catalyst inside the horizon
Peter R. Huntsman (CEO) bought 100,000 shares at $9.81 on 2026-08-03 = $981,000,
one buyer, zero sells in six months. HUN closed 9.03 — **below the CEO's own
purchase price**. -43.9% off the 16.085 150-day high; 150-day low 7.995; ATR14
0.428 (4.74%); 30-day average dollar volume $25.6M, which clears the $500K floor
comfortably. Levels would work (entry 9.00, stop 7.90 below the 150-day low =
2.57 ATR, target 11.20 inside the range, R:R 2.00) — but HUN is not on the fetched
earnings calendar through 2026-12-01 and there is no other dated event. Watchlist,
not a recommendation. The awaiting-entry order at 9.00 is 0.3% below the close and
the level is unchanged.

## [06:25 ET] SCREEN — insider buying across the de-rated names that report in 10 sessions
Screened for "far enough below its own range high that a 2.0 ATR stop and a 2.0
R:R can both be met", then checked insiders. Off-150-day-high and ATR% first:
FLNC -86.6% (atr 13.1%), CRDO -60.2% (12.4%), SYM -49.6% (6.4%), SMTC -48.4%
(12.8%), HPE -37.8% (8.2%), MDB -35.2% (6.8%), GTLB -23.3% (5.8%), ZM -19.2%,
CRWD -17.4%, OKTA -16.8%, ANF -14.5%, NCNO -9.9%, URBN -7.5%, KSS -6.1%,
DLTR -4.1%, PVH -2.9%. (GES failed to fetch.)
Insider dollars over six months on the eight most de-rated:
HPE 0 buys / -$40.4M · MDB 0 / -$71.1M · SMTC 0 / -$10.9M · CRDO 0 / **-$211.6M**
· SYM 0 / **-$571.4M** · OKTA 0 / -$49.2M · GTLB 2 buys by 1 / -$115.9M ·
FLNC 2 buys by 2 ($125K) / -$1.5M.
**Not one name in the de-rated-with-a-catalyst group has insider support; every
one of them has insiders selling into the fall, several enormously.** So the two
halves of the screen do not overlap today: the names with room have insiders
leaving, and the names insiders are buying (DKS, LEN, HUN, ADSK) either already
qualified or lack the catalyst. That is the finding, and it is why the candidate
list is short rather than padded.

## [06:26 ET] CAPTURED — CVS — long_term, conviction 4, level UNCHANGED at 77.50
Re-horizoned, not re-levelled. TTM EPS **$8.33** (2.09 + 2.58 + 2.57 + 1.09, four
fetched actuals, **beats in all four**). 81.35 = 9.77x, entry 77.50 = 9.30x.
Target 108.29 = 13.0x against the 13.29x the stock carried at its own 110.68
150-day high; bear 66.64 = 8.0x, below the 9.14x the 76.10 150-day low implies.
**R:R 2.835** vs the 2.5 floor; baseline win prob 26.1%, claimed 44%.
- The comparison that carries it: same rule, same session, CVS at 9.77x with 4 of
  4 beats against **UNH at 17.14x with 3 of 4**. The MA audit risk is discounted
  about twice as hard in CVS.
- Disclosed weakness, deliberately: at a 12.5x target the R:R is **2.45** and this
  idea fails outright. It survives on half a turn of multiple.
- Against it, and in `key_risk`: insiders are net **-$350.7M** (8 sells vs one
  $2.0M buy), Glenview was reported cutting into the selloff, and **this report
  was already stopped out of CVS on 2026-11-04**.
- Correlation: CVS + UNH are 2 ideas on the CMS-6098-P driver. The cap is 3 and I
  am stopping at 2 — XLV was rejected above, so nothing else goes on this driver.

## [06:27 ET] POSITION UPDATE — PFE — opened 2026-08-18 @ 27.60, close 28.06, +1.7%
- decision: **hold, and cut the target from 42.00 to 36.60.** Entry unchanged (filled).
- why: the position carried a 42.00 target and **no downside price at all**. TTM
  reported EPS is $3.05 (0.66, 0.75, 0.77, 0.87 — four fetched actuals, beats in
  4 of 4, up 31.8% across the series), so 42.00 is **13.77x** when the 150-day high
  of 31.44 is only **10.31x**. A target a third above any multiple the stock has
  carried in the window is not an anchor. 36.60 is 12.0x; the new bear price 24.40
  is 8.0x, just above the 7.74x the 23.62 150-day low implies. R:R 2.81.
- conviction set at **3, not 4**: the real bear case is the loss-of-exclusivity
  cliff and I could not fetch pipeline or LOE data this morning, so the strongest
  argument against is unanswered rather than answered. Said so in key_risk.
- captured via add_candidate.py, re-horizoned to long_term, which is what it is.

## [06:28 ET] POSITION UPDATES — the seven that need nothing, and why
All closes 2026-11-18. No amendment captured for any of these; stating that is
the decision, not an omission.
- **KHC** @ 23.00, close **25.44, +10.6%** — the best position in the book. Rose
  1.31% on a session when gold, crude and energy equity were all down 3%+, which
  is the defensive rotation working exactly as a staples holding should. Above
  both the 24.69 SMA20 and the 23.91 SMA50. Target 28.09 is the 150-day high, so
  it needs a breakout, not a re-rate. Hold, unchanged. (Insiders: 0 buys, 1 sell,
  -$426,532 — not a reason to act, noted for completeness.)
- **UNP** @ 288.60, close **300.90, +4.3%** — rose 1.30% on the same weak tape,
  sitting on the 300.33 SMA20 with the 288.05 SMA50 below. Target 315.99 is the
  150-day high (close is -4.78% from it). Stop 277.40. Hold, unchanged.
- **XLU** @ 43.30, close **43.55, +0.6%** — up 0.30% on 11/18 and the only sector
  I checked that rose. Above the 43.37 SMA20 and well above the 41.93 SMA50.
  This is the right side of the regime described above. Hold, unchanged.
- **TLT** @ 80.30, close **80.22, -0.1%** — up 0.84% on 11/18 as the reflation
  trade was sold. Back above the 80.07 SMA50, below the 81.06 SMA20. Target 84.30,
  stop 78.80 (ATR14 0.73, so the stop is 1.95 ATR away — adequate). Hold.
- **RTX** @ 199.00, close **197.45, -0.8%** — on the 197.22 SMA20, above the
  192.66 SMA50, target 226.50 against a 226.88 150-day high. ITA was only -0.30%
  on 11/18 so nothing happened to defense. Hold, unchanged.
- **ABT** @ 103.00, close **104.48, +1.4%** — fell only 0.22% on a day XLV fell
  2.20%, i.e. it did **not** trade with the CMS-rule selloff, which is correct
  since a device maker has no Medicare Advantage risk-adjustment exposure. Below
  the 107.44 SMA20, just above the 103.86 SMA50. Stop 97.00, target 117.34 (the
  150-day high). Hold, unchanged.
- **PYPL** @ 56.50, close **57.89, +2.5%** — just under the 58.11 SMA20, above the
  55.90 SMA50, target 62.70 against a 62.73 150-day high. Stop 54.10 is 2.41 ATR
  away (ATR14 1.57). Hold, unchanged.

## [06:29 ET] AWAITING-ENTRY — IWM SELL_SHORT @ 270.50 (published 2026-11-18)
- decision: **leave the order, do not re-pitch, and do not raise the entry.**
- IWM closed 270.12, i.e. the market is already 0.14% through the short entry and
  it has still not filled. The reason to be careful rather than press: IWM printed
  its 150-day low at **267.865 on 11/17** and then closed *higher* on both 11/17
  and 11/18 (269.05, then 270.12). Starting a short at a 150-day low that has just
  held twice is the worst location on the chart for it, and the regime read above
  cuts against it too — bonds were bid on 11/18, and small caps are the main
  beneficiary of falling yields.
- I am not flipping the position; I have no evidence for a long. I am declining to
  add to it. SMA20 277.80 and SMA50 279.38 are both above, so the trend still
  supports the short — that is why the order stays rather than being withdrawn.

## [06:29 ET] AWAITING-ENTRY — ADM @ 68.80 — level unchanged, and a tracking note
ADM closed **67.78** on 11/18 after trading 67.52-68.77 — i.e. the whole session
was **below** the 68.80 buy entry, and 11/17 (69.22-71.01) was above it, so the
68.80 level was crossed on 11/18. Prior context still lists it as awaiting entry;
that may simply be the refresh not having run, and it is flagged here rather than
assumed. On the merits: -23.6% off the 88.75 150-day high, 150-day low 66.06,
below both the 73.35 SMA20 and the 78.87 SMA50, in a steady downtrend. Insiders:
1 buy, $196,756, 0 sells — real but small. **No earnings on the fetched calendar
through 2026-12-01, so no dated catalyst.** Level unchanged at 68.80, no re-pitch.

## [06:33 ET] CAPTURED — DY (Dycom) — swing, conviction 5, the best idea of the morning
Found by screening small/mid caps with earnings inside ten sessions for how far
they sit below their own 150-day high, then checking insiders — the same two-step
that produced DKS, and the only name where both halves hit.
- **-60.14% off a 150-day high of 566.47** while beating the estimate in **4 of 4**
  reported quarters: 3.63 (+9.8%), 2.03 (+13.8%), 4.42 (**+57.4%**), 5.29 (+8.9%).
  TTM reported EPS **$15.37**, so 225.78 = **14.69x**; the 566.47 high was 36.86x.
- **Why it fell**, which I would not recommend it without knowing: the August
  fiscal-Q2 release guided Q3 EPS to 4.33-4.79 against a 4.68 consensus midpoint
  and disclosed ~$150M of wireless program revenue shifting into **fiscal 2028**;
  a major wireless customer paused spending. Stock -13% that session, 52-week low
  2026-10-20. In the *same* release full-year revenue guidance was **raised** to a
  $7.57B midpoint and total backlog grew **53% YoY to $12.24B**.
  — sources: https://www.quiverquant.com/news/Dycom+Industries+Slides+as+Earlier+Guidance+Overhang+and+New+Lows+Weigh+on+Shares
  and https://markets.financialcontent.com/stocks/article/stockstory-2026-8-26-why-dycom-dy-shares-are-sliding-today
- **Insiders**: 3 open-market buys by **3 distinct** buyers, $551,307, zero
  completed sells in six months. Honest qualifier, recorded in key_risk: Form 144
  notices of *intended* sale were filed 2026-10-05 and 2026-11-05.
- **Base and turn**: low 186.25 on 11/05, then rising session lows 199.08, 210.50,
  213.73, 213.52, 213.99, 220.01 into a 225.78 close back above the 222.35 SMA20.
- levels: entry 225.78 (at the market, zone 219-232 — deliberately **not** a
  pullback discount), stop **198.00** below the 199.08 low of 11/06 = **2.09 ATR**
  (ATR14 13.28), target **292.00 = 19.0x** the TTM EPS already reported.
  **R:R 2.38**; baseline win prob 29.6%, claimed 40%.
- catalyst: fiscal Q3 **2026-11-24 bmo** on the fetched calendar — three sessions.
- conviction 5 = dated_catalyst + positioning + valuation_anchor + technical_level
  + counter_argument_answered, five distinct kinds. Sized at **2.5%, not the 4-5%**
  the count would allow: a 5.88% ATR name into a binary print three sessions out.
  The size cut is the risk control, and it is stated as such.
- ADV $130.6M, NYSE common — comfortably inside the Robinhood universe.

## [06:34 ET] REJECTED — WMT / INTU / BABA / ROAD / CTRN / NNE / AEO
- **WMT** reports today bmo, the week's tone-setter, and is **-5.77% off its high**
  with a 2.42% ATR. A 2.0 ATR stop plus a 2.0 R:R needs a target 4 ATR up, ~140,
  against a 135.16 150-day high. Fails the same arithmetic as XLV and ADSK.
  Insiders: 0 buys, 40 sells, **-$1.09B**.
- **INTU** (today, amc): 2 buys by 1 insider, $541,665, but 8 sells, net -$309,462.
  Roughly neutral, and no dislocation to buy.
- **BABA** (today, bmo): 3 buys by 2 ($25.7M) against 6 sells, net **-$56.2M**.
  Mixed rather than supportive.
- **ROAD** -48.3% off high — but it reports **this morning** (11/19 bmo), so there
  is no position to take before the event, and insider buying is $30,052.
- **CTRN** -42.1% off high, earnings 11/30: insiders 0 buys, **-$77.4M** net sold.
- **NNE** -67.2% off high, earnings 11/30: insiders 0 buys, 48 sells, -$52.3M.
- **AEO** only -3.5% off its high — no room for the required target.

## [06:34 ET] REJECTED — second de-rated batch, same result
IESC -59.3% off high with earnings **tomorrow** 11/20 bmo, ATR 9.62%, ADV $82.5M —
shaped almost exactly like DY, and insiders are 0 buys against 18 sells,
**-$62.0M**. NTAP -28.5% (12/01): 0 buys, -$45.8M. AMBA -43.3% (11/24): 0 buys,
-$8.6M. ASAN -24.8%: 0 buys, -$6.0M. OOMA -32.4%: 0 buys, -$5.1M. AMTM -26.7%:
no insider activity in either direction. BOX, A, J, BJ, HQY all under 12% off
their highs, so the required target would have to print above the range high.
**Across roughly 35 names screened this morning, open-market insider buying
appeared in six — DKS, DY, ADSK, LEN, HUN, ADM — and only DKS and DY also had a
dated catalyst and levels that clear both floors.** That is the whole reason the
list is five symbols.

## [06:35 ET] NO CRYPTO, NO FUTURES, NO EVENT CONTRACT TODAY — and why, per lane
- **Event contracts**: the source is broken, not quiet. See DATA GAPS above —
  "Fed" returns sports parlays, four other macro queries return zero markets, and
  every market returned has null prices. I will not state an implied probability
  I could not fetch, and an event-contract thesis without one is a hunch.
- **Crypto**: BTC $63,676 (-0.73% 24h), ETH $1,801.53, SOL $74.39 — all three
  essentially unchanged on the day. The trend is severe: IBIT, the cleanest
  fetchable proxy with daily bars, closed 35.36, **-28.41%** from its 49.39
  150-day high, falling from 44.94 on 11/05 in a near-straight line, below both
  its 42.53 SMA20 and 44.96 SMA50. Buying that is a knife; shorting a 28%
  drawdown eleven days into the move is late and badly located. No edge either
  way, so no trade. The existing /MBTZ6 short at 74,075 stays unfilled and
  unamended.
- **Futures**: I could not fetch a single futures price this morning —
  `market_data.py macro` produced nothing and there is no futures quote path in
  the CLI. Setting an entry, stop and target on /MES, /MGC or /MCL would mean
  deriving them from an ETF proxy and calling the result a contract price. That
  is exactly the fabricated number the rules forbid, so there is no futures idea
  today. **This is a tooling gap, not a judgement**: the macro picture above
  (gold at a 150-day low, crude broken, bonds bid) is the clearest futures setup
  the tape has offered in weeks and it went untraded for want of a price feed.

## [06:36 ET] CORRELATION AUDIT — read this before publishing
Five symbols captured, and they are **not** five independent bets:
- **UNH + CVS are the same bet**: both long, both de-rated by CMS-6098-P on the
  same session. Two on one driver, cap is 3. XLV was rejected so nothing else
  joins them.
- **PFE makes it three healthcare names of five.** PFE is *not* on the CMS driver
  (a vaccine and drug maker has no Medicare Advantage risk-adjustment exposure,
  and it proved it by falling 1.44% on a day UNH fell 10.21%) — but it is the
  same sector, and a sector-wide de-rating would hit all three. Mitigating: the
  PFE entry is an **amendment that cuts a target from 42.00 to 36.60**, i.e. it
  reduces the claim on an existing position rather than adding a new one.
- **Combined healthcare exposure if all three fill: 8.0% of capital** (UNH 3.0 +
  CVS 2.5 + PFE 2.5). That is the number to look at, and it is a deliberate
  concentration in a sector that was sold on one regulatory proposal two days ago.
- DKS (1.5%, consumer discretionary) and DY (2.5%, fiber/telecom capex) are
  genuinely independent of those and of each other.
- Nothing in the list depends on a single macro print, which is the failure mode
  the cap exists for.
- **Horizon skew is real and not manufactured**: 2 swing, 3 long_term, 0 intraday.
  Nothing intraday cleared the bar because the only same-session catalysts were
  this morning's prints (WMT, BABA, ROAD) and I have no pre-market data at 6am —
  every price in this file is the 2026-11-18 close.

## [06:37 ET] RESEARCH COMPLETE
- candidates: **6 lines, 5 distinct symbols** — DY (swing, conv 5), DKS (swing,
  conv 4, position update), UNH (long_term, conv 4), CVS (long_term, conv 4),
  PFE (long_term, conv 3, position amendment). UNH appears twice; the second line
  is the same idea with the explicit invalidation condition added, and synthesis
  takes the last entry per symbol.
- All 13 open positions were reviewed and decided. **Two are closes that could
  not be expressed as candidates and must be carried as text**: BCC (close at the
  open — -18.57% vs XHB over one month, 0.35 ATR from its stop, at its 150-day
  low) and OXY (close at the open — sector shelf broken, lagging XLE by 4.73% on
  1m). Both are explained in full above; neither was captured, because the only
  amendment that expresses "get out" is a stop inside the noise, which validation
  would correctly refuse. HII is a hold with a stated invalidation (weekly close
  below the 281.18 SMA50) and no stop, for the same structural reason.
- All 9 awaiting-entry orders were reviewed. **GLD SELL @ 406.77 and /MBTZ6 SHORT
  @ 74,075 are both ~16% away from the market and should be retired rather than
  re-published.** CVS was re-horizoned to long_term at an unchanged 77.50. The
  rest are unchanged, with reasons given.
- watchlist worth carrying: **LEN** (Berkshire Hathaway bought $329,017,222 of it
  on 2026-10-02 at 77.12-81.90; actionable below 79.50 or on the December print)
  and **HUN** (CEO bought $981,000 at 9.81; the stock is below his price).
- coverage gaps: no macro data at all (rates, VIX, DXY, FRED); no event-contract
  prices; no options-implied move on any idea; no short interest on any idea; no
  futures prices; no pre-market quotes. No primary filings were read this morning
  — the DY counter-argument rests on secondary sources and says so.
- sources that failed: `market_data.py macro` (zero bytes, killed after running
  for most of the session); `market_data.py events` (returns sports parlays with
  null prices for every macro query); `market_data.py implied` (yahoo-options
  HTTP 401 on every symbol); `market_data.py short` (nasdaq ReadTimeout);
  `history` failed for GES, SLP, LESL.
- honest note on the bar: the prior-context record is 5/44 to target (11%),
  avg -5.5%, with single-name swing stock longs at 2/30 (7%). 44 closed is past
  the noise threshold, so I raised the bar rather than matching a count — five
  symbols, every one carrying either a fetched insider-buying record or a
  valuation built from four quarters of fetched actual EPS, and the arithmetic
  for every rejection written down rather than left implicit.

## [06:38 ET] ADDENDUM — one last pass at the long_term lane outside healthcare
Three of five captured ideas are healthcare, so I spent the remaining budget
trying to find a durable mispricing somewhere else. Both candidates failed, and
the arithmetic is here so synthesis does not re-litigate them.
- **ADM** — genuinely interesting and still does not qualify. TTM reported EPS
  **$5.19** (0.87, 0.71, 1.84, 1.77), **beats in 4 of 4** (+8.2%, +6.6%, +26.8%,
  +9.3%), and the analyst bullish share has swung **+22.8 points to 33.3%** over
  four months — the largest improving revision I saw today. Close 67.78 = 13.06x;
  the 88.75 150-day high was 17.1x and the 66.06 low is 12.73x.
  The failure: an honest bear case for a cyclical ag processor with an EPS series
  that ran 0.87 → 0.71 → 1.84 → 1.77 is about **10.5x = 54.50**, below the 150-day
  low. From a 67.78 entry that is 13.28 of risk, so the 2.5 floor demands a
  **100.98** target = 19.5x — above any multiple in the window.
  **I could have passed it by setting the bear at 12.0x (62.28), which gives R:R
  2.77. I am not doing that.** A bear case 8% below the market on a stock already
  down 23.6% is not a bear case; it is the long-term analogue of walking the stop
  in, and it is the exact move `check_stop_distance` exists to refuse on swings.
  The awaiting order stays at 68.80, unchanged, and ADM goes to the watchlist.
- **HUN** — the CEO's $981,000 purchase is real but there is nothing to value.
  TTM reported EPS is **-$0.53** (-0.37, -0.20, 0.00, 0.04) and the company has
  beaten in 1 of 4. A P/E anchor does not exist, and I have no fetched book value
  or replacement-cost figure to put in its place. Peter Huntsman is buying a
  chemical cycle, not an earnings stream — which may well be right, and is not
  something this report can price today. Watchlist, as recorded above.
**Net: the healthcare concentration flagged in the correlation audit stands, and
it stands because the alternatives failed their floors, not because I stopped
looking.** Research ran 06:01-06:38 ET of a ~60 minute budget and closed here
with candidates captured; nothing was abandoned for want of clock.
