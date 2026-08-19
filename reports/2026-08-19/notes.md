# Research log — 2026-08-19

## [10:52 ET] MACRO — session open, big risk-parity move
- FRED: US10Y 4.72 (8/17), US2Y 4.19 (8/17), fed funds 3.63, 10y-2y +0.52 (8/18), unemployment 4.1% (Jul)
- Live quotes 10:49 ET (finnhub, regular session):
  - SPY 770.98 +0.46%; QQQ 716.54 -0.14%; IWM 302.70 +0.82%
  - GLD 411.03 **+3.13%** — outsized one-day move
  - TLT 83.02 **+1.67%** — large bond rally
  - USO 131.94 +0.98%
- Read: gold + long bonds ripping together while QQQ is flat = dovish/real-rate shock or
  a safety bid, not a growth impulse. Small caps (IWM) outperforming Nasdaq fits rate relief.
- DATA GAP: yahoo returned HTTP 429 for all index/VIX/DXY/futures symbols; finnhub refuses
  CFD indices. No VIX, no DXY, no ^TNX live print this run. Using ETF proxies instead.

## [10:54 ET] CALENDAR — dated catalysts inside 10 sessions (finnhub earnings)
- 8/19 bmo (today, already printed): TGT, LOW, TJX, ADI, EL
- 8/20 bmo: **WMT** (rev est $188.8B), **BABA** ($274B RMB rev est), **DE** ($11.05B), NTES, FUTU, SPR
- 8/21 bmo: BJ, UI
- 8/24: **PDD** bmo, DKS, PVH, XPEV
- 8/25: INTU amc, ZM amc, ANF, KSS, WSM, FIVE
- 8/26 amc: **NVDA** (rev est $93.6B), CRM, HPQ, VEEV, NTNX; CRWD, SNPS, BURL, URBN
- 8/27: **MRVL**, ADSK, WDAY amc, AFRM amc, BBY, DG, ULTA, GAP
- 8/31: FRO bmo (tanker read-through to DHT open position), AEO, ASO

## [11:02 ET] CONTEXT — this is a SECOND run today
- reports/2026-08-19/candidates.jsonl already held 16 candidates from an earlier (~06:30 ET) run,
  and report.json already exists. Prior context confirms TJX/HD//MBTU6 were opened today at
  premarket-ish prices (TJX 150.85, HD 337.49, /MBTU6 64340).
- Consequence: today's real value-add is RE-LEVELING against live regular-session prices, because
  several of those names have moved 3%+ since the morning marks. Synthesis takes the LAST entry
  per symbol, so re-captures supersede.

## [11:03 ET] MOVE OF THE DAY — precious metals break out, cross-confirmed
Live 10:59 ET (finnhub, regular session):
- GLD 410.97 (+3.12%), prev close 398.55, intraday high 412.63
- IAU 84.25 (+3.11%) — independent confirmation, same underlying
- SLV 59.18 (+3.03%) — silver moving with it
- GDX 96.53 (**+8.52%**) — miners at ~2.7x beta, the classic confirmation of a real bullion move
- TLT 83.02 (+1.67%) off a 90-day low of 81.17 set yesterday
- GLD 20-day range high before today was 407.36 — today is a clean breakout to new highs
- Driver per reporting: a Treasury buyback announcement pulled long yields sharply lower, with the
  July FOMC minutes today and Chair Kevin Warsh at Jackson Hole later this week.
  source: https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-19-2026
  source: https://www.voiceofemirates.com/en/business/2026/08/19/gold-prices-rebound-globally-amid-falling-us-treasury-yields/
- NOTE ON A CONFLICT: wire copy fetched at 11:00 described spot gold up only ~0.5-0.6%. Four
  independent US-listed instruments (GLD, IAU, SLV, GDX) disagree and show a 3%+ move. The wire
  copy is stamped to an earlier point in the session; the live quotes are what I am trading off.
