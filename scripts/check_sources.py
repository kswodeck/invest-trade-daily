#!/usr/bin/env python3
"""Probe every data source and report which ones actually work.

    python scripts/check_sources.py

Prints a markdown table. Exits non-zero only if every source is dead, which
would mean a network or proxy problem rather than a missing key.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import market_data as md  # noqa: E402


def probe(name: str, fn, *, needs_key: str | None = None) -> tuple[str, bool, str]:
    try:
        result = fn()
    except Exception as exc:  # noqa: BLE001
        return name, False, f"{type(exc).__name__}: {exc}"
    if result.get("ok"):
        return name, True, result.get("note") or "working"
    err = result.get("error") or str(result.get("attempts", ""))[:160]
    if needs_key and "no api key" in err:
        return name, False, f"optional — set `{needs_key}` to enable"
    return name, False, err[:160]


def main() -> int:
    # (label, probe, optional key, critical) — critical sources are the ones the
    # report cannot produce entry/target/stop levels without.
    checks = [
        ("Yahoo (equity quotes)", lambda: md.quote_yahoo("SPY"), None, True),
        ("Yahoo (history/levels)", lambda: md.history("SPY", 90), None, True),
        ("Yahoo (futures)", lambda: md.quote_yahoo("/MESU6"), None, False),
        ("CoinGecko (crypto)", lambda: md.crypto(["bitcoin"]), None, True),
        ("Kalshi (event contracts)", lambda: md.events("", 3), None, False),
        ("SEC EDGAR (filings)", lambda: md.filings("AAPL", 3), "SEC_USER_AGENT", False),
        ("Stooq (quote fallback)", lambda: md.quote_stooq("SPY"), None, False),
        ("Finnhub (quotes)", lambda: md.quote_finnhub("SPY"), "FINNHUB_API_KEY", False),
        ("Finnhub (earnings)", lambda: md.earnings(7), "FINNHUB_API_KEY", False),
        ("Alpha Vantage (quotes)", lambda: md.quote_alphavantage("SPY"), "ALPHAVANTAGE_API_KEY", False),
        ("FRED (macro)", lambda: md.fred_series("DGS10"), "FRED_API_KEY", False),
    ]

    rows = [(probe(n, f, needs_key=k), crit) for n, f, k, crit in checks]

    print("## Data source check\n")
    print("| Source | Status | Detail |")
    print("| --- | --- | --- |")
    for (name, ok, detail), crit in rows:
        mark = "✅" if ok else ("🔴" if crit else "❌")
        print(f"| {name}{' **(critical)**' if crit else ''} | {mark} | {detail} |")

    working = sum(1 for (_, ok, _), _ in rows if ok)
    print(f"\n**{working} of {len(rows)} sources working.**")

    broken_critical = [name for (name, ok, _), crit in rows if crit and not ok]
    if broken_critical:
        print(
            f"\n🔴 **Critical source(s) down: {', '.join(broken_critical)}.** "
            "The report cannot set real entry, target, and stop levels without price "
            "history, and will fall back to publishing few or no ideas rather than "
            "inventing numbers. Fix before relying on a 6am run."
        )
        return 1

    print("\n✅ Every critical source is up. Optional keys above only improve depth.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
