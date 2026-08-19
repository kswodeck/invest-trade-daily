#!/usr/bin/env python3
"""Weekly scorecard: what worked, what did not, and what to change.

    python scripts/weekly_digest.py 2026-08-23
    python scripts/weekly_digest.py 2026-08-23 --dry-run

Writes reports/weekly/<date>.md and a "Weekly Digest" tab in the Sheet.

The daily performance tab shows every position. This answers the question that
tab cannot: which *kinds* of idea are actually working. Conviction only means
something if high-conviction calls hit more often than low-conviction ones, and
that is checkable rather than assumed.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

STATE_PATH = REPO / "state" / "open_positions.json"
OUT_DIR = REPO / "reports" / "weekly"

# Terminal states that produced a P&L. `pending` and `not_filled` never became
# positions, so they are excluded from every rate and average below.
CLOSED = ("target_hit", "stopped", "expired")
UNFILLED = ("pending", "not_filled")
MIN_SAMPLE = 15  # below this, a bucket's hit rate is noise


def load_positions() -> list[dict]:
    if not STATE_PATH.exists():
        return []
    try:
        return json.loads(STATE_PATH.read_text() or "[]")
    except json.JSONDecodeError:
        return []


def stats(rows: list[dict]) -> dict[str, Any]:
    rows = [p for p in rows if p.get("status") not in UNFILLED]
    closed = [p for p in rows if p.get("status") in CLOSED]
    wins = [p for p in closed if p.get("status") == "target_hit"]
    pcts = [p["pct_vs_entry"] for p in closed if p.get("pct_vs_entry") is not None]
    return {
        "n": len(rows),
        "closed": len(closed),
        "wins": len(wins),
        "hit_rate": round(len(wins) / len(closed) * 100) if closed else None,
        "avg_move": round(sum(pcts) / len(pcts), 2) if pcts else None,
        "best": max(pcts) if pcts else None,
        "worst": min(pcts) if pcts else None,
    }


def table(rows: list[dict], key: str, label: str) -> list[str]:
    buckets: dict[Any, list[dict]] = defaultdict(list)
    for p in rows:
        buckets[p.get(key) if p.get(key) is not None else "unknown"].append(p)
    if not buckets:
        return []

    out = [f"### By {label}", "", "| " + label.title() + " | Closed | Hit rate | Avg move | Open |",
           "| --- | --- | --- | --- | --- |"]
    for name, group in sorted(buckets.items(), key=lambda kv: str(kv[0])):
        s = stats(group)
        open_n = len([p for p in group if p.get("status") == "open"])
        hit = f"{s['hit_rate']}%" if s["hit_rate"] is not None else "—"
        avg = f"{s['avg_move']:+.1f}%" if s["avg_move"] is not None else "—"
        out.append(f"| {name} | {s['closed']} | {hit} | {avg} | {open_n} |")
    out.append("")
    return out


def build(week_end: date, positions: list[dict]) -> str:
    week_start = week_end - timedelta(days=7)
    overall = stats(positions)

    def in_week(p: dict, field: str) -> bool:
        raw = p.get(field)
        return bool(raw) and week_start.isoformat() <= raw <= week_end.isoformat()

    closed_this_week = [p for p in positions if p.get("status") in CLOSED and in_week(p, "closed")]
    opened_this_week = [p for p in positions if in_week(p, "opened")]
    still_open = [p for p in positions if p.get("status") == "open"]

    lines = [
        f"# Weekly digest — week ending {week_end.isoformat()}",
        "",
        f"**All time:** {overall['closed']} closed of {overall['n']} tracked · "
        + (f"hit rate {overall['hit_rate']}% · " if overall["hit_rate"] is not None else "")
        + (f"avg move {overall['avg_move']:+.1f}%" if overall["avg_move"] is not None else "no closed trades yet"),
        "",
        f"**This week:** {len(opened_this_week)} opened · {len(closed_this_week)} closed · "
        f"{len(still_open)} still open",
        "",
    ]

    if closed_this_week:
        lines += ["## Closed this week", "",
                  "| Symbol | Side | Horizon | Conv | Opened | Outcome | Move |",
                  "| --- | --- | --- | --- | --- | --- | --- |"]
        for p in sorted(closed_this_week, key=lambda p: p.get("closed") or ""):
            outcome = {"target_hit": "✓ target", "stopped": "✗ stopped",
                       "expired": "– expired"}.get(p.get("status", ""), p.get("status", ""))
            pct = p.get("pct_vs_entry")
            lines.append(
                f"| `{p.get('symbol')}` | {(p.get('direction') or '').upper()} | "
                f"{p.get('horizon')} | {p.get('conviction')} | {p.get('opened')} | "
                f"{outcome} | {f'{pct:+.1f}%' if pct is not None else '—'} |")
        lines.append("")
    else:
        lines += ["## Closed this week", "", "_Nothing closed._", ""]

    lines += ["## What is working", ""]
    if overall["closed"] < MIN_SAMPLE:
        lines += [
            f"⚠️ Only {overall['closed']} closed trades so far. Below roughly {MIN_SAMPLE} "
            "the breakdowns below are noise — a single lucky or unlucky call moves every "
            "number. Read them, but do not change strategy on them yet.",
            "",
        ]
    lines += table(positions, "conviction", "conviction")
    lines += table(positions, "horizon", "horizon")
    lines += table(positions, "asset_class", "asset class")
    lines += table(positions, "venue", "venue")

    # The single most useful question this file can answer.
    conv_buckets = {c: stats([p for p in positions if p.get("conviction") == c])
                    for c in (2, 3, 4, 5)}
    rated = [(c, s) for c, s in conv_buckets.items() if s["closed"] >= 3 and s["hit_rate"] is not None]
    lines += ["## Is conviction calibrated?", ""]
    if len(rated) >= 2:
        ordered = sorted(rated, key=lambda cs: cs[0])
        trend = [f"{c}: {s['hit_rate']}%" for c, s in ordered]
        rising = all(a[1]["hit_rate"] <= b[1]["hit_rate"] for a, b in zip(ordered, ordered[1:]))
        lines += [
            "Hit rate by conviction score — " + " · ".join(trend),
            "",
            "Higher conviction is hitting more often, which is what a calibrated score "
            "looks like." if rising else
            "**Higher conviction is not hitting more often.** Either the score is not "
            "tracking evidence quality, or the sample is still too small to tell. If this "
            "persists past ~30 closed trades, the conviction rubric in `config/strategy.md` "
            "needs rewriting.",
            "",
        ]
    else:
        lines += ["_Not enough closed trades per conviction level to judge yet._", ""]

    if still_open:
        lines += ["## Still open", "",
                  "| Symbol | Side | Horizon | Opened | Days | Entry | Last | Move |",
                  "| --- | --- | --- | --- | --- | --- | --- | --- |"]
        for p in sorted(still_open, key=lambda p: p.get("opened") or ""):
            pct = p.get("pct_vs_entry")
            lines.append(
                f"| `{p.get('symbol')}` | {(p.get('direction') or '').upper()} | "
                f"{p.get('horizon')} | {p.get('opened')} | {p.get('days_open', '?')} | "
                f"{p.get('entry')} | {p.get('last_price') or '—'} | "
                f"{f'{pct:+.1f}%' if pct is not None else '—'} |")
        lines.append("")

    lines += [
        "---",
        "",
        "_Outcomes are graded from daily bars against the published entry, target and stop. "
        "They are what the report's calls did, not what any account did — no slippage, "
        "no fills, no position sizing._",
    ]
    return "\n".join(lines) + "\n"


def to_sheet_rows(markdown: str) -> list[list[str]]:
    """Flatten the digest into rows, splitting markdown tables into columns."""
    rows: list[list[str]] = []
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and set(stripped) <= set("|- :"):
            continue  # markdown table rule
        if stripped.startswith("|"):
            rows.append([c.strip().strip("`*") for c in stripped.strip("|").split("|")])
        else:
            rows.append([stripped.lstrip("#").strip().strip("*_")])
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("date", nargs="?", help="week-ending date, YYYY-MM-DD; defaults to today")
    ap.add_argument("--dry-run", action="store_true", help="write the file but not the Sheet")
    args = ap.parse_args(argv)

    week_end = date.fromisoformat(args.date) if args.date else date.today()
    positions = load_positions()
    markdown = build(week_end, positions)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"{week_end.isoformat()}.md"
    out_path.write_text(markdown)
    print(f"Wrote {out_path.relative_to(REPO)} ({len(positions)} positions tracked)")

    if args.dry_run:
        print("\n" + markdown)
        return 0

    try:
        import publish_sheets as ps
        spreadsheet, _ = ps.open_spreadsheet()
        ps.write_tab(spreadsheet, "Weekly Digest", to_sheet_rows(markdown), 1)
        print("Wrote the 'Weekly Digest' tab.")
    except SystemExit as exc:
        print(f"Sheet write skipped: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
