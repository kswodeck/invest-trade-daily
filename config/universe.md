# Tradeable universe — Robinhood only

**Hard constraint: every recommendation must be executable in a Robinhood
account.** If you cannot place the order in the Robinhood app, it does not go in
the report. An idea that is brilliant and untradeable is worth zero.

When a recommendation's tradeability is uncertain, verify it during research
rather than assuming. Robinhood's product list changes often enough that
anything remembered rather than checked is a liability.

## Venues and their vocabulary

| Venue string (use verbatim in `report.json`) | Instruments | `direction` values |
| --- | --- | --- |
| `Robinhood Stocks` | US-listed common stock, ADRs, ETFs | `buy`, `sell_short` |
| `Robinhood Crypto` | Coins on Robinhood's supported list | `buy`, `sell` |
| `Robinhood Derivatives` | CME futures offered by RH | `long`, `short` |
| `Robinhood Prediction Markets` | RH's Kalshi-backed event contracts | `yes`, `no` |

## Per-class rules

### Stocks & ETFs — `Robinhood Stocks`
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
- OTC equities, penny stocks under $1, and anything with a market cap under
  $300M or average daily dollar volume under $5M — the report should not
  recommend positions that cannot be exited.
- Instruments halted, in bankruptcy proceedings, or pending delisting.
- Any ticker that has moved more than 40% in the prior session, unless the move
  itself is the thesis and the risk is spelled out.
