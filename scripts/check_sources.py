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
    checks = [
        ("Stooq (equity quotes)", lambda: md.quote_stooq("SPY"), None),
        ("Stooq (history/levels)", lambda: md.history("SPY", 30), None),
        ("CoinGecko (crypto)", lambda: md.crypto(["bitcoin"]), None),
        ("Kalshi (event contracts)", lambda: md.events("", 3), None),
        ("SEC EDGAR (filings)", lambda: md.filings("AAPL", 3), "SEC_USER_AGENT"),
        ("Finnhub (quotes)", lambda: md.quote_finnhub("SPY"), "FINNHUB_API_KEY"),
        ("Finnhub (earnings)", lambda: md.earnings(7), "FINNHUB_API_KEY"),
        ("Alpha Vantage (quotes)", lambda: md.quote_alphavantage("SPY"), "ALPHAVANTAGE_API_KEY"),
        ("FRED (macro)", lambda: md.fred_series("DGS10"), "FRED_API_KEY"),
    ]

    rows = [probe(n, f, needs_key=k) for n, f, k in checks]

    print("## Data source check\n")
    print("| Source | Status | Detail |")
    print("| --- | --- | --- |")
    for name, ok, detail in rows:
        print(f"| {name} | {'✅' if ok else '❌'} | {detail} |")

    working = sum(1 for _, ok, _ in rows if ok)
    print(f"\n**{working} of {len(rows)} sources working.**")

    keyless = [r for r in rows[:5]]
    if not any(ok for _, ok, _ in keyless):
        print("\n⚠️ No keyless source is reachable — this looks like a network problem, "
              "not a configuration one.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
