#!/usr/bin/env python3
"""Portfolio-level view of a day's recommendations.

    python scripts/exposure.py reports/2026-08-16/report.json

Individual ideas can each look sensible while the report as a whole is one
concentrated bet. A live report was seven longs out of eight in a tape it
described as "mixed" — visible only by reading every row. This surfaces it.

Used by publish_sheets.py to head the Today tab and by step_summary.py for the
run summary. Importable: `summarize(report)` and `render_rows(summary)`.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

BULLISH = {"buy", "long", "yes"}
BEARISH = {"sell", "sell_short", "short", "no"}

# Above this share of gross exposure in one bucket, the report is really one
# position wearing several tickers.
CONCENTRATION_PCT = 40.0


def _size(idea: dict) -> float:
    """Position size, defaulting to something sane when unstated."""
    size = idea.get("position_size_pct")
    return float(size) if isinstance(size, (int, float)) else 2.0


def _bucket_exposure(ideas: list[dict], key) -> dict[str, float]:
    out: dict[str, float] = defaultdict(float)
    for idea in ideas:
        out[str(key(idea) or "unknown")] += _size(idea)
    return {k: round(v, 2) for k, v in sorted(out.items(), key=lambda kv: -kv[1])}


def fetch_sectors(ideas: list[dict]) -> dict[str, str]:
    """Sector per equity symbol. Best effort — needs a Finnhub key."""
    import market_data as md

    sectors: dict[str, str] = {}
    for idea in ideas:
        if idea.get("asset_class") not in ("stock", "etf"):
            continue
        symbol = idea.get("symbol", "")
        if not symbol or symbol in sectors:
            continue
        try:
            prof = md.profile(symbol)
            if prof.get("ok") and prof.get("sector"):
                sectors[symbol] = prof["sector"]
        except Exception:  # noqa: BLE001 - exposure is a nicety, never a blocker
            continue
    return sectors


def summarize(report: dict, sectors: dict[str, str] | None = None) -> dict[str, Any]:
    ideas = report.get("recommendations", []) or []
    if not ideas:
        return {"count": 0}

    sectors = sectors or {}
    longs = [i for i in ideas if i.get("direction") in BULLISH]
    shorts = [i for i in ideas if i.get("direction") in BEARISH]

    long_pct = round(sum(_size(i) for i in longs), 2)
    short_pct = round(sum(_size(i) for i in shorts), 2)
    gross = round(long_pct + short_pct, 2)

    by_sector: dict[str, float] = defaultdict(float)
    for idea in ideas:
        if idea.get("asset_class") in ("stock", "etf"):
            by_sector[sectors.get(idea.get("symbol", ""), "unclassified")] += _size(idea)

    summary: dict[str, Any] = {
        "count": len(ideas),
        "long_count": len(longs),
        "short_count": len(shorts),
        "long_pct": long_pct,
        "short_pct": short_pct,
        "gross_exposure_pct": gross,
        "net_exposure_pct": round(long_pct - short_pct, 2),
        "by_asset_class": _bucket_exposure(ideas, lambda i: i.get("asset_class")),
        "by_horizon": _bucket_exposure(ideas, lambda i: i.get("horizon")),
        "by_venue": _bucket_exposure(ideas, lambda i: (i.get("venue") or "").replace("Robinhood ", "")),
        "by_sector": {k: round(v, 2) for k, v in sorted(by_sector.items(), key=lambda kv: -kv[1])},
        "conviction_spread": dict(sorted(Counter(i.get("conviction") for i in ideas).items())),
        "regime": (report.get("market_context") or {}).get("regime", "unknown"),
    }

    # Warnings are the point of the whole exercise.
    warnings: list[str] = []
    if gross > 0:
        net_share = abs(summary["net_exposure_pct"]) / gross * 100
        side = "long" if summary["net_exposure_pct"] > 0 else "short"
        if net_share > 70 and len(ideas) >= 4:
            warnings.append(
                f"{net_share:.0f}% of gross exposure is net {side} "
                f"({len(longs)} long / {len(shorts)} short) — the report is a directional bet, "
                f"not a set of independent ideas"
            )
        if summary["regime"] in ("mixed", "risk-off") and side == "long" and net_share > 60:
            warnings.append(
                f"heavily net long into a '{summary['regime']}' regime — the positioning and the "
                f"stated view disagree"
            )
        # Stocks and ETFs are the same bet for concentration purposes, so they
        # are merged here — otherwise an all-equity report reports itself twice
        # at half the true share and the warning reads as less serious.
        merged: dict[str, float] = defaultdict(float)
        for name, pct in summary["by_asset_class"].items():
            merged["equity" if name in ("stock", "etf") else name] += pct

        for label, buckets in (("sector", summary["by_sector"]),
                               ("asset class", dict(merged))):
            for name, pct in buckets.items():
                if name in ("unclassified", "unknown"):
                    continue
                share = pct / gross * 100
                if share > CONCENTRATION_PCT and len(ideas) >= 4:
                    warnings.append(
                        f"{share:.0f}% of exposure sits in one {label}: {name}"
                    )
    if gross > 60:
        warnings.append(f"gross exposure is {gross:.0f}% of capital across {len(ideas)} ideas — "
                        "sizing every idea as suggested would leave little dry powder")
    summary["warnings"] = warnings
    return summary


def render_rows(summary: dict[str, Any]) -> list[list[Any]]:
    """Compact rows for the top of the Today tab."""
    if not summary.get("count"):
        return []

    def fmt(buckets: dict[str, float]) -> str:
        return "  ·  ".join(f"{k} {v:g}%" for k, v in list(buckets.items())[:6]) or "—"

    rows = [
        [f"EXPOSURE — {summary['count']} ideas  ·  "
         f"{summary['long_count']} long / {summary['short_count']} short  ·  "
         f"gross {summary['gross_exposure_pct']:g}%  ·  "
         f"net {summary['net_exposure_pct']:+g}%"],
        [f"By class: {fmt(summary['by_asset_class'])}"],
        [f"By horizon: {fmt(summary['by_horizon'])}"],
    ]
    if summary.get("by_sector"):
        rows.append([f"By sector: {fmt(summary['by_sector'])}"])
    for warning in summary.get("warnings", []):
        rows.append([f"⚠ {warning}"])
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("report", type=Path)
    ap.add_argument("--no-sectors", action="store_true", help="skip the Finnhub sector lookup")
    args = ap.parse_args(argv)

    report = json.loads(args.report.read_text())
    ideas = report.get("recommendations", [])
    sectors = {} if args.no_sectors else fetch_sectors(ideas)
    summary = summarize(report, sectors)

    if not summary.get("count"):
        print("No recommendations to summarize.")
        return 0
    for row in render_rows(summary):
        print(row[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
