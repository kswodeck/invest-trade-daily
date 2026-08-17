# Tradeable universe — Robinhood only

**Hard constraint: every recommendation must be executable in a Robinhood
account.** If you cannot place the order in the Robinhood app, it does not go in
the report. An idea that is brilliant and untradeable is worth zero.

When a recommendation's tradeability is uncertain, verify it during research
rather than assuming. Robinhood's product list changes often enough that
anything remembered rather than checked is a liability.

## Express the view in the best available instrument

The same view can often be taken several ways. **When a futures contract exists
for the same underlying, prefer it.** In order:

1. **Futures** — `Robinhood Derivatives`
2. **Event contract** — `Robinhood Prediction Markets`, when the view is really
   about a probability rather than a price path
3. **Spot** — `Robinhood Stocks` / `Robinhood Crypto`

Why futures win when available:

- **Bearish views work properly.** Robinhood Crypto has no shorting at all, so a
  bearish crypto view expressed as `sell` is really just "exit or avoid" — it
  makes no money if you are right. Short equity needs margin. A short futures
  contract expresses the view directly.
- Nearly 24-hour trading, so an overnight macro move is tradeable rather than
  something you watch gap against you.
- Defined contract sizing, and micro/nano contracts keep the notional sane.

**A bearish crypto view must be a short futures contract, not a spot `sell`** —
unless you actually hold the asset and the recommendation is to exit, in which
case say that plainly.

Common substitutions to reach for:

| View | Prefer | Rather than |
| --- | --- | --- |
| Bitcoin direction | `/MBT` (micro) or `/BTC` | BTC spot, especially to short |
| Ether direction | `/MET` (micro) or `/ETH` | ETH spot |
| S&P 500 direction | `/MES` | SPY, especially to short |
| Nasdaq 100 direction | `/MNQ` | QQQ, especially to short |
| Russell 2000 direction | `/M2K` | IWM |
| Gold | `/MGC` | GLD |
| Crude oil | `/MCL` | USO |

This is a preference, not an absolute. Spot is right when the horizon is
long-term (futures roll costs make multi-year holds awkward), when the position
is too small for even a micro contract, or when the specific thesis is about a
single equity rather than the index it sits in. Say which and why.

## Venues and their vocabulary

| Venue string (use verbatim in `report.json`) | Instruments | `direction` values |
| --- | --- | --- |
| `Robinhood Stocks` | US-listed common stock, ADRs, ETFs | `buy`, `sell_short` |
| `Robinhood Crypto` | Coins on Robinhood's supported list | `buy`, `sell` |
| `Robinhood Derivatives` | CME futures offered by RH | `long`, `short` |
| `Robinhood Prediction Markets` | RH's Kalshi-backed event contracts | `yes`, `no` |

## Per-class rules

### Stocks & ETFs — `Robinhood Stocks`

**Small and micro caps are in scope and wanted.** The asymmetric ideas live
below the mega-cap tier, and a report that only surfaces names everyone already
owns is not worth much. Hunt them deliberately.

They come with obligations rather than a lower bar:

- **Check liquidity before anything else.** Average daily dollar volume must
  clear $500K, and your position must be a small fraction of it. State the
  figure in the thesis for anything under $2B market cap.
- **Size it as a lottery ticket**, per `config/strategy.md` — max 1% under $300M
  market cap. Small size is what makes these safe to publish.
- **Widen the stop to the instrument's actual volatility.** A micro cap with a
  9% ATR stopped at 4% is a coin flip on noise, not a risk control.
- **Name the liquidity and dilution risk explicitly** in `key_risk`. Small caps
  raise capital, and a secondary offering is the most common way these theses
  die well before the fundamental case is settled.
- Halts are a real risk at this size. Say so when it applies.

Otherwise:

- US exchange-listed only (NYSE, Nasdaq, NYSE American, Cboe BZX).
- **Excluded:** OTC / pink sheets, most foreign ordinaries, and warrants —
  Robinhood does not support them.
- Leveraged and inverse ETFs are supported, but flag the decay risk in
  `key_risk` whenever the horizon is longer than a few days.
- `sell_short` requires margin. Mark `requires_margin: true` so it is obvious
  before the trade is placed.

### Crypto — `Robinhood Crypto`
- Robinhood lists a curated set of coins, not the whole market. Verify the coin
  is listed before recommending it:
  <https://robinhood.com/us/en/support/articles/cryptocurrencies-available-on-robinhood/>
- 24/7 market. On weekend runs this class carries more of the report.
- No shorting in a Robinhood Crypto spot account. A bearish crypto view must be
  expressed as `sell` (exit/avoid), or routed to crypto futures under
  `Robinhood Derivatives`, or to an event contract.

### Futures — `Robinhood Derivatives`
- Robinhood offers 40+ CME products: equity index (including micro and nano
  contracts), energy, metals, FX, rates, and crypto futures.
- Verify the specific contract at:
  <https://robinhood.com/us/en/support/articles/futures-contracts-available-on-robinhood/>
- **Always prefer the smallest contract size that expresses the view** — micro
  or nano over full-size. Notional leverage on a full-size contract is large
  enough to be a different product in practice.
- State the contract month explicitly (e.g. `/MESU6`, not `/MES`), and never
  recommend a contract inside its final trading week without saying so.
- Every futures idea must carry a `stop`. No exceptions — these are leveraged
  and can lose more than the deposit.

### Event contracts — `Robinhood Prediction Markets`
**These are wanted, not tolerated.** Hunt them actively — a mispriced
probability is often cleaner than an equivalent equity trade, because the payoff
is defined and the thesis is a single falsifiable claim rather than a price path
that can be right and still stop you out.

- Robinhood's event contracts are Kalshi-backed. Only recommend an event that
  is actually listed in Robinhood's prediction markets tab; Kalshi lists many
  markets Robinhood does not carry.
- Prices are in **cents, 1–99**, representing implied probability. Set
  `unit: "cents"` and put entry/exit on that scale.
- The edge must be an explicit probability disagreement: state the market's
  implied probability, state your estimate, and state why the gap exists.
  "Feels underpriced" is not a thesis.
- Note the resolution date and source in `catalyst`. An event contract you
  cannot exit early is a hold-to-resolution commitment.

## Universally excluded

Not tradeable on Robinhood, or out of scope by choice:

- Options of any kind — excluded by scope decision, not by availability.
- Mutual funds, bonds and fixed income, forex spot pairs.
- OTC equities and anything trading under $1 — Robinhood restricts these and
  they are not reliably exitable.
- Anything with a market cap under **$50M** or average daily dollar volume under
  **$500K**. This floor is about exit, not size: a position you cannot get out
  of is worth nothing regardless of how good the thesis was.
- Instruments halted, in bankruptcy proceedings, or pending delisting.
- Any ticker that has moved more than 40% in the prior session, unless the move
  itself is the thesis and the risk is spelled out.
