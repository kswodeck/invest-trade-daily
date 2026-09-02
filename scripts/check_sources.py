#!/usr/bin/env python3
"""Probe every data source and report which ones actually work.

    python scripts/check_sources.py

Prints a markdown report to stdout. Exits non-zero only when a *capability* is
unavailable — that is, when no provider can supply something the report needs.
An individual provider being down is information, not a failure, as long as
something else covers it.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))

import market_data as md  # noqa: E402


def _render_error(result: dict[str, Any]) -> str:
    """Turn a failed result into one readable line."""
    if result.get("error"):
        return str(result["error"])[:200]
    attempts = result.get("attempts") or []
    parts = []
    for a in attempts:
        if isinstance(a, dict):
            parts.append(f"{a.get('source', '?')}: {str(a.get('error', ''))[:90]}")
        else:
            parts.append(str(a)[:90])
    return " · ".join(parts)[:400] or "unknown failure"


def probe(name: str, fn: Callable[[], dict], needs_key: str | None = None) -> tuple[str, bool, str]:
    try:
        result = fn()
    except Exception as exc:  # noqa: BLE001
        return name, False, f"{type(exc).__name__}: {exc}"
    if result.get("ok"):
        detail = result.get("note") or result.get("source") or "working"
        if result.get("source") and result.get("note"):
            detail = f"via {result['source']} — {result['note']}"
        elif result.get("source"):
            detail = f"via {result['source']}"
        return name, True, str(detail)[:200]
    err = _render_error(result)
    if needs_key and "no api key" in err:
        return name, False, f"optional — set `{needs_key}` to enable"
    return name, False, err


def main() -> int:
    # Capabilities: what the report actually needs. Each exercises the full
    # provider fallback chain, so any one working source is enough.
    capabilities = [
        ("Equity/ETF quote", lambda: md.quote("SPY")),
        ("Equity/ETF history + levels", lambda: md.history("SPY", 90)),
        ("Crypto price", lambda: md.crypto(["bitcoin"])),
    ]

    # Providers: which individual source is up. Informational only.
    providers = [
        ("Nasdaq — history", lambda: {"ok": bool(md._bars_nasdaq("SPY", 90)), "source": "nasdaq"}, None),
        ("Finnhub — quote", lambda: md.quote_finnhub("SPY"), "FINNHUB_API_KEY"),
        ("Finnhub — earnings", lambda: md.earnings(7), "FINNHUB_API_KEY"),
        ("Yahoo — quote", lambda: md.quote_yahoo("SPY"), None),
        ("Yahoo — history", lambda: {"ok": bool(md._bars_yahoo("SPY", 90)), "source": "yahoo"}, None),
        ("Yahoo — futures (/MESU6)", lambda: md.quote_yahoo("/MESU6"), None),
        ("Twelve Data — history", lambda: {"ok": bool(md._bars_twelvedata("SPY", 90)), "source": "twelvedata"}, "TWELVEDATA_API_KEY"),
        ("Alpha Vantage — history", lambda: {"ok": bool(md._bars_alphavantage("SPY"))}, "ALPHAVANTAGE_API_KEY"),
        ("Stooq — quote", lambda: md.quote_stooq("SPY"), None),
        ("CoinGecko — crypto", lambda: md.crypto(["bitcoin"]), None),
        ("Kalshi — event contracts", lambda: md.events("", 3), None),
        ("SEC EDGAR — filings", lambda: md.filings("AAPL", 3), "SEC_USER_AGENT"),
        ("FRED — macro", lambda: md.fred_series("DGS10"), "FRED_API_KEY"),
        ("Yahoo — options chain (implied move)", lambda: md.implied_move("SPY"), None),
        ("Nasdaq — short interest", lambda: md.short_interest("AAPL"), None),
        ("Finnhub — analyst trend", lambda: md.analysts("AAPL"), "FINNHUB_API_KEY"),
        ("Computed — relative strength", lambda: md.relative_strength("AAPL"), None),
    ]

    cap_rows = [probe(n, f) for n, f in capabilities]
    prov_rows = [probe(n, f, k) for n, f, k in providers]

    print("## Capabilities\n")
    print("These are what the report needs. Each tries every provider in turn.\n")
    print("| Capability | Status | Detail |")
    print("| --- | --- | --- |")
    for name, ok, detail in cap_rows:
        print(f"| **{name}** | {'✅' if ok else '🔴'} | {detail} |")

    print("\n## Providers\n")
    print("Individual sources. A ❌ here is fine as long as the capability above is ✅.\n")
    print("| Provider | Status | Detail |")
    print("| --- | --- | --- |")
    for name, ok, detail in prov_rows:
        print(f"| {name} | {'✅' if ok else '❌'} | {detail} |")

    broken = [name for name, ok, _ in cap_rows if not ok]
    working = sum(1 for _, ok, _ in prov_rows if ok)
    print(f"\n**{working} of {len(prov_rows)} providers up.**")

    if broken:
        print(
            f"\n🔴 **Unavailable capability: {', '.join(broken)}.**\n\n"
            "Every provider for this failed. The report cannot set real entry, target, "
            "and stop levels without it, and will publish few or no ideas rather than "
            "invent numbers. Check the provider table above for the specific errors."
        )
        return 1

    print("\n✅ Every capability is covered. Provider ❌ rows above are redundancy, not problems.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
