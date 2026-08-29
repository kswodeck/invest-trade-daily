#!/usr/bin/env python3
"""Classify a report as missing, stub, or published — one rule, one place.

Three things need to agree on what "today already has a report" means: the
schedule gate, the watchdog that dispatches a catch-up, and ensure_report.py,
which decides whether to overwrite what synthesis left behind. When they
disagree, a day goes missing quietly.

`reports/2026-08-28/report.json` is why this exists. Synthesis was killed
part-way through and left a skeleton:

    {"truncated": true, "data_quality_notes": "Synthesis in progress.",
     "market_context": {"summary": "Synthesis in progress."},
     "recommendations": []}

It is schema-valid, so ensure_report.py accepted it and the pipeline published
"Synthesis in progress." to the Sheet. Every downstream check that asked only
"does report.json exist?" then treated the day as done: both cron arms skipped,
and the watchdog went quiet on a day that produced nothing usable.

A report holding neither a recommendation nor a watchlist entry is not a result.
It is either a crash or a genuinely empty day, and the honest output is the same
either way — say the pipeline did not conclude anything, and let the catch-up
have another go while there is still time.

    python scripts/report_state.py reports/2026-08-28/report.json   # -> stub
    git show main:reports/2026-08-28/report.json | python scripts/report_state.py

Prints one word to stdout. Always exits 0 — an unreadable report is a `stub`,
not a crash, because the caller's next move is the same either way.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

MISSING = "missing"
STUB = "stub"
PUBLISHED = "published"


def classify(report: dict | None) -> str:
    """Whether a parsed report counts as today's published deliverable.

    `pipeline_failure` is ensure_report.py's own marker, so an honest stub is
    always recognised as one. The emptiness test catches everything else: a
    truncated skeleton, a synthesis that died mid-write, a report whose ideas
    were all demoted by the enforce pass.
    """
    if report is None:
        return MISSING
    if report.get("pipeline_failure"):
        return STUB
    has_ideas = bool(report.get("recommendations")) or bool(report.get("watchlist"))
    return PUBLISHED if has_ideas else STUB


def classify_text(raw: str | None) -> str:
    if raw is None:
        return MISSING
    if not raw.strip():
        return STUB
    try:
        report = json.loads(raw)
    except json.JSONDecodeError:
        # Unparseable is not "missing" — something wrote it, and it still needs
        # replacing before anything downstream reads it.
        return STUB
    if not isinstance(report, dict):
        return STUB
    return classify(report)


def classify_path(path: Path) -> str:
    if not path.exists():
        return MISSING
    try:
        return classify_text(path.read_text(encoding="utf-8"))
    except OSError:
        return STUB


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "report",
        nargs="?",
        help="path to report.json; omit to read the report from stdin",
    )
    args = ap.parse_args(argv)

    if args.report:
        print(classify_path(Path(args.report)))
    else:
        print(classify_text(sys.stdin.read()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
