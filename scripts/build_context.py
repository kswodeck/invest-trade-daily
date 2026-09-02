#!/usr/bin/env python3
"""Summarize recent picks and their outcomes for the research phase to read.

    python scripts/build_context.py 2026-08-12 --days 10

Writes reports/<date>/prior_context.md. Without this the model starts every
morning with amnesia: it re-pitches the same idea for a week, never manages a
position it opened, and cannot notice that a kind of setup keeps failing.

Always exits 0 — missing history is a normal first-run state, not an error.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import date, timedelta
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
STATE_PATH = REPO / "state" / "open_positions.json"

CLOSED = ("target_hit", "stopped", "expired")
UNFILLED = ("pending", "not_filled")


def load_positions() -> list[dict]:
    if not STATE_PATH.exists():
        return []
    try:
        return json.loads(STATE_PATH.read_text() or "[]")
    except json.JSONDecodeError:
        return []


def load_recent_reports(today: date, days: int) -> list[dict]:
    out = []
    for offset in range(1, days + 1):
        path = REPO / "reports" / (today - timedelta(days=offset)).isoformat() / "report.json"
        if path.exists():
            try:
                out.append(json.loads(path.read_text()))
            except json.JSONDecodeError:
                continue
    return out


def rate(subset: list[dict]) -> str:
    subset = [p for p in subset if p.get("status") not in UNFILLED]
    closed = [p for p in subset if p.get("status") in CLOSED]
    if not closed:
        return "no closed trades yet"
    wins = sum(1 for p in closed if p["status"] == "target_hit")
    pcts = [p["pct_vs_entry"] for p in closed if p.get("pct_vs_entry") is not None]
    avg = f", avg {sum(pcts) / len(pcts):+.1f}%" if pcts else ""
    return f"{wins}/{len(closed)} hit target ({wins / len(closed) * 100:.0f}%){avg}"


def group_rates(positions: list[dict], key: str) -> list[str]:
    buckets: dict[Any, list[dict]] = defaultdict(list)
    for p in positions:
        buckets[p.get(key) or "unknown"].append(p)
    return [f"- **{k}**: {rate(v)} (n={len(v)})" for k, v in sorted(buckets.items(), key=str)]


def build(today: date, days: int) -> str:
    positions = load_positions()
    reports = load_recent_reports(today, days)
    open_pos = [p for p in positions if p.get("status") == "open"]
    pending = [p for p in positions if p.get("status") == "pending"]
    closed = [p for p in positions if p.get("status") in CLOSED]

    lines = [
        f"# Prior context — as of {today.isoformat()}",
        "",
        "Read this before researching. It is the record of what this report has",
        "already said and how those calls turned out.",
        "",
    ]

    if not positions and not reports:
        lines += ["_No history yet — this is a first run. Research from scratch._", ""]
        return "\n".join(lines)

    # ---- open positions -------------------------------------------------
    lines += [f"## Open positions ({len(open_pos)})", ""]
    if open_pos:
        lines += [
            "These are live. Do not re-pitch them as new ideas. Instead decide, for each:",
            "hold as-is, adjust the target or stop given new information, or close early.",
            "Put any change in the recommendation for that symbol and say it is an update.",
            "",
            "| Symbol | Side | Opened | Days | Entry | Target | Stop | Last | % vs entry |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for p in sorted(open_pos, key=lambda x: x.get("opened", "")):
            pct = p.get("pct_vs_entry")
            lines.append(
                f"| `{p.get('symbol')}` | {(p.get('direction') or '').upper()} | "
                f"{p.get('opened')} | {p.get('days_open', '?')} | {p.get('entry')} | "
                f"{p.get('target')} | {p.get('stop')} | {p.get('last_price') or '—'} | "
                f"{f'{pct:+.1f}%' if pct is not None else '—'} |"
            )
        lines.append("")
    else:
        lines += ["_None open._", ""]

    if pending:
        lines += [
            f"## Awaiting entry ({len(pending)})", "",
            "These were published but the market never reached the entry, so they are "
            "not positions. Re-pitching one is fine and does not double-count: it "
            "amends the position already tracked rather than opening a second one. "
            "Say what changed, or say the level is unchanged.", "",
        ]
        lines += [f"- `{p.get('symbol')}` {(p.get('direction') or '').upper()} "
                  f"@ {p.get('entry')} (published {p.get('opened')})" for p in pending]
        lines.append("")

    # ---- track record ---------------------------------------------------
    lines += [f"## Track record ({len(closed)} closed of {len(positions)} tracked)", ""]
    if closed:
        lines += [f"**Overall: {rate(positions)}**", ""]
        lines += ["By horizon:", *group_rates(positions, "horizon"), ""]
        lines += ["By asset class:", *group_rates(positions, "asset_class"), ""]
        lines += ["By conviction score:", *group_rates(positions, "conviction"), ""]
        lines += [
            "Use this honestly. If a category is consistently losing, either raise the bar",
            "for it or stop recommending it. If the sample is under ~15 closed trades, it is",
            "noise — note it and do not over-fit.",
            "",
        ]
        worst = [p for p in closed if p.get("status") == "stopped"][-5:]
        if worst:
            lines += ["Most recent stop-outs, worth a moment's reflection:", ""]
            for p in worst:
                lines.append(
                    f"- `{p.get('symbol')}` {(p.get('direction') or '').upper()} "
                    f"opened {p.get('opened')}, stopped {p.get('closed')} "
                    f"(conviction was {p.get('conviction')})"
                )
            lines.append("")
    else:
        lines += ["_Nothing has closed yet._", ""]

    # ---- repetition guard -----------------------------------------------
    counts = Counter(
        i.get("symbol")
        for r in reports
        for i in r.get("recommendations", [])
        if i.get("symbol")
    )
    repeats = [(s, c) for s, c in counts.most_common(12) if c > 1]
    if repeats:
        lines += [
            f"## Recently recommended (last {days} days)",
            "",
            "A symbol appearing here repeatedly is a warning sign, not a conviction signal.",
            "Re-recommend it only if something genuinely changed — a new catalyst, a new",
            "level, a new piece of information. Say what changed.",
            "",
        ]
        lines += [f"- `{s}` — {c}×" for s, c in repeats]
        lines.append("")

    # ---- what got skipped ------------------------------------------------
    gaps = [
        f"- {r['date']}: {r['data_quality_notes'][:200]}"
        for r in reports[:3]
        if r.get("data_quality_notes")
    ]
    if gaps:
        lines += ["## Recent coverage gaps", "",
                  "Areas prior runs could not reach. Consider prioritizing them today.", "", *gaps, ""]

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("date", help="report date, YYYY-MM-DD")
    ap.add_argument("--days", type=int, default=10, help="how far back to scan reports")
    args = ap.parse_args(argv)

    today = date.fromisoformat(args.date)
    out_dir = REPO / "reports" / args.date
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "prior_context.md"
    out_path.write_text(build(today, args.days) + "\n")
    print(f"Wrote {out_path.relative_to(REPO)} ({out_path.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
