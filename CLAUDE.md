# invest-trade-daily — working notes for Claude

This repo generates a daily, actionable trade-idea report and publishes it to a
Google Sheet. Two Claude phases run in sequence inside one GitHub Actions job.

## Non-negotiables

1. **Robinhood-tradeable only.** If it can't be traded in a Robinhood account,
   it does not go in the report. See `config/universe.md`. When unsure whether
   an instrument is offered, verify at runtime — do not guess from memory.
2. **Never fabricate a number.** Every price, date, and figure must trace to a
   fetched source. If you could not get a live price, write `null` and say so
   in `data_quality_notes` rather than estimating.
3. **Every claim carries a source URL.** No source, no recommendation.
4. **Checkpoint constantly during research.** The research phase is killed at a
   hard wall clock limit with no warning. Append to `reports/<date>/notes.md`
   after *every* finding, not at the end. Unwritten research is lost research.
5. **Capture candidates as you find them**, via
   `python scripts/add_candidate.py '<json>'`. `candidates.jsonl` is what
   synthesis builds the report from; `notes.md` is context. A run that gathers
   brilliantly and captures nothing produces nothing — this has already
   happened once.
6. **Never commit secrets.** Credentials arrive as environment variables only.

## Phase contract

| Phase | Runs | Writes | Reads |
| ----- | ---- | ------ | ----- |
| 0 Context | `scripts/build_context.py` | `reports/<date>/prior_context.md` | `state/`, past reports |
| 1 Research | `/daily-research` | `candidates.jsonl` (the deliverable), `notes.md` (context) | web, `market_data.py`, prior context |
| 2 Synthesis | `/daily-synthesis` | `reports/<date>/report.json` | the above |
| 2a Guarantee | `scripts/ensure_report.py` | a stub `report.json` if it is missing, invalid, or empty | `report.json`, `notes.md` |
| 2b Validate | `scripts/validate_report.py` | a `validation` block per idea | live prices, ATR, earnings calendar |
| 2c Red team | `/daily-redteam` | edits `report.json` | validation flags, sources |
| 2d Enforce | `scripts/validate_report.py --enforce` | demotes failures to the watchlist | `report.json` |
| 3 Publish | `scripts/publish_sheets.py` | Google Sheet, `state/open_positions.json` | `report.json` |
| 4 Refresh | `scripts/refresh_prices.py` | fresh `last_price`, `distance_to_entry_pct` | live quotes |

Prices carry `as of` and the market session they were taken in. At 6am ET the
freshest honest equity price is the previous close — that is a closed market,
not stale data, and the two must never be conflated. `market_data.market_session()`
and `age_minutes()` are how you tell them apart.

Phases 2b–2d exist because the model is strong at research and undisciplined
about its own arithmetic. A live report once shipped eight reward-to-risk ratios
clustered at 2.04–2.33 against a 2.0 floor: targets nudged until they passed.
**Every number in `validation` is recomputed from source — never trust a figure
the model wrote about its own idea.**

Phase 2 must produce a schema-valid `report.json` **even if `notes.md` is
short, truncated, or nearly empty**. A thin report that says so honestly is the
correct output; a fabricated full report is a failure.

## Scheduling

GitHub cron is UTC-only, so 6am ET is declared as two arms (`0 10` and `0 11`
UTC) and both fire every day of the year. `scripts/schedule_gate.py` decides
which one works, on two separate questions:

- **Is it still early enough?** From the wall clock in New York, never from
  which cron fired — in EDT the "EST arm" lands at a perfectly reasonable 7am,
  so the hour alone cannot tell the arms apart. The window is `6-11` ET.
- **Is today's report already published?** From the branch tip, never from the
  checked-out tree. A scheduled run is pinned to the SHA it was created at, so
  its checkout cannot contain a commit the earlier arm pushed minutes ago.

"Published" is a three-way answer from `scripts/report_state.py`, not a file
existence test. A report holding neither a recommendation nor a watchlist entry
is a **stub**: it concluded nothing, so it is retried while the window is open
and alarmed on once the window shuts. `2026-08-28` is why — synthesis was killed
mid-write, left a schema-valid `{"data_quality_notes": "Synthesis in progress.",
"recommendations": []}`, and every later check saw a file and called the day
done. `ensure_report.py` uses the same rule, so a skeleton like that is replaced
by the honest no-signal stub instead of reaching the Sheet.

Recovery is `.github/actions/report-catch-up`, which any workflow can call: it
dispatches the report when the branch has nothing usable and the window is still
open. `Report Watchdog` and `Refresh Prices` both call it, on the theory that
whichever workflow GitHub does manage to deliver can rescue the morning.
`scripts/report_runs.py` bounds it — three attempts a day, and never while one
is already running.

Consequences worth knowing before you go debugging:

- A second run per day that finishes in ~10 seconds is the gate working.
- GitHub's scheduler is best-effort and has delivered this repo's crons ten
  hours late, watchdog slots included. A day with no `reports/<date>/` is a real
  outcome, not necessarily a bug — but it should always be a red `Report
  Watchdog` run, never silence.
- Never widen the window so far that an afternoon run publishes a report framed
  as the 6am pre-open view.
- Nothing here can fix delivery itself. If a morning must be guaranteed, the
  trigger has to come from outside GitHub Actions.

Logic changes here need a test in `tests/` — run with
`python -m unittest discover -s tests`.

## Data access

Use `scripts/market_data.py` before reaching for raw web scraping — it is
faster, more reliable, and already handles fallbacks:

```bash
python scripts/market_data.py quote NVDA SPY          # equities/ETFs
python scripts/market_data.py crypto bitcoin ethereum # crypto
python scripts/market_data.py history NVDA --days 90  # OHLCV
python scripts/market_data.py macro                   # rates, VIX, DXY, FRED
python scripts/market_data.py events "CPI"            # Kalshi event contracts
python scripts/market_data.py filings NVDA            # recent SEC filings
python scripts/market_data.py earnings --days 14      # upcoming earnings
```

Every subcommand prints JSON to stdout and never raises on a failed source — it
returns `{"ok": false, "error": ...}` for that source and moves on. Check `ok`.

## Style

- Python: standard library first, `requests` for HTTP, no heavy frameworks.
  Type-hint public functions. Keep scripts runnable standalone.
- Markdown research notes: terse, factual, timestamped. Bullets over prose.
- Never rewrite history in `reports/` — past reports are the performance record.
