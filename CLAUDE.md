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
5. **Never commit secrets.** Credentials arrive as environment variables only.

## Phase contract

| Phase | Skill | Writes | Reads |
| ----- | ----- | ------ | ----- |
| 1 Research | `/daily-research` | `reports/<date>/notes.md`, `candidates.jsonl` | web, `scripts/market_data.py` |
| 2 Synthesis | `/daily-synthesis` | `reports/<date>/report.json` | the above |
| 3 Publish | `scripts/publish_sheets.py` | Google Sheet, `state/open_positions.json` | `report.json` |

Phase 2 must produce a schema-valid `report.json` **even if `notes.md` is
short, truncated, or nearly empty**. A thin report that says so honestly is the
correct output; a fabricated full report is a failure.

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
