#!/usr/bin/env python3
"""Render the GitHub Actions run summary for a daily report.

    python scripts/step_summary.py 2026-08-12 >> "$GITHUB_STEP_SUMMARY"

Reads RESEARCH_OUTCOME and SYNTHESIS_OUTCOME from the environment when present.
Always exits 0 — a broken summary must not fail an otherwise good run.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

ARROW = {"buy": "▲", "long": "▲", "yes": "▲", "sell": "▼", "sell_short": "▼", "short": "▼", "no": "▼"}


def main() -> int:
    date_str = sys.argv[1] if len(sys.argv) > 1 else ""
    out: list[str] = [f"## Daily Trade Report — {date_str}", ""]

    research = os.environ.get("RESEARCH_OUTCOME", "unknown")
    synthesis = os.environ.get("SYNTHESIS_OUTCOME", "unknown")
    note = " (hit the time cap — expected)" if research == "failure" else ""
    out += [
        "| Phase | Outcome |",
        "| --- | --- |",
        f"| Research | `{research}`{note} |",
        f"| Synthesis | `{synthesis}` |",
        "",
    ]

    path = REPO / "reports" / date_str / "report.json"
    try:
        report = json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        out.append(f"⚠️ Could not read `{path.relative_to(REPO)}`: `{exc}`")
        print("\n".join(out))
        return 0

    ideas = sorted(report.get("recommendations", []), key=lambda i: i.get("rank", 99))
    ctx = report.get("market_context", {})
    out.append(
        f"**{len(ideas)} recommendations** · regime `{ctx.get('regime', 'unknown')}` · "
        f"truncated `{report.get('truncated')}`"
    )
    out.append("")

    if ideas:
        out += ["| # | Symbol | Side | Horizon | Conv | Entry | Target | Stop | Catalyst |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for i in ideas:
            entry, exit_, cat = i.get("entry", {}), i.get("exit", {}), i.get("catalyst", {})
            wait = "⏸ " if cat.get("wait") else ""
            out.append(
                f"| {i.get('rank', '')} | `{i.get('symbol', '')}` | "
                f"{ARROW.get(i.get('direction', ''), '')} {i.get('direction', '').upper()} | "
                f"{i.get('horizon', '')} | {i.get('conviction', '')} | "
                f"{entry.get('ideal', '—')} | {exit_.get('target', '—')} | {i.get('stop') or '—'} | "
                f"{wait}{cat.get('event', '')} |"
            )
        out.append("")
    else:
        out += ["_No recommendations published._", ""]

    if report.get("data_quality_notes"):
        out += ["> **Data quality:** " + report["data_quality_notes"], ""]

    print("\n".join(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
