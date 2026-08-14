#!/usr/bin/env python3
"""Guarantee that a schema-valid report.json exists for a given date.

The publish step must never be the thing that fails a morning. If the synthesis
phase crashed, timed out, or wrote invalid JSON, this writes a minimal honest
report in its place so the Sheet still updates and says what went wrong.

    python scripts/ensure_report.py 2026-08-12 --research-truncated

Exits 0 whether it wrote a stub or found a valid report already in place.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO / "scripts" / "report_schema.json"
ET = ZoneInfo("America/New_York")


def is_valid(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, "report.json was never written"
    try:
        report = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        return False, f"report.json is not valid JSON: {exc}"
    try:
        import jsonschema

        jsonschema.validate(report, json.loads(SCHEMA_PATH.read_text()))
    except ImportError:
        return True, "jsonschema unavailable; accepted without validation"
    except Exception as exc:  # noqa: BLE001 - jsonschema.ValidationError and friends
        return False, f"report.json failed schema validation: {str(exc).splitlines()[0]}"
    return True, f"valid, {len(report.get('recommendations', []))} recommendations"


def notes_excerpt(notes_path: Path, limit: int = 600) -> str:
    if not notes_path.exists():
        return "No research notes were produced."
    text = notes_path.read_text().strip()
    if not text:
        return "Research notes file was created but left empty."
    candidates = text.count("CANDIDATE")
    head = text[-limit:] if len(text) > limit else text
    return (
        f"Research notes contain {candidates} candidate block(s) and "
        f"{len(text)} characters, but were not converted into a report. "
        f"Tail of the log: ...{head}"
    )


def stub(date_str: str, reason: str, notes_path: Path, truncated: bool) -> dict:
    return {
        "date": date_str,
        "generated_at_et": datetime.now(ET).isoformat(timespec="seconds"),
        "research_minutes": None,
        "truncated": truncated,
        "pipeline_failure": True,
        "data_quality_notes": (
            f"NO RECOMMENDATIONS PUBLISHED. The synthesis phase did not produce a usable "
            f"report ({reason}). {notes_excerpt(notes_path)} "
            f"Treat today as a no-signal day rather than a neutral one — the pipeline "
            f"failed, it did not conclude that there was nothing to trade."
        ),
        "market_context": {
            "summary": "Unavailable — the report pipeline did not complete.",
            "regime": "unknown",
        },
        "recommendations": [],
        "watchlist": [],
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("date", help="report date, YYYY-MM-DD")
    ap.add_argument("--research-truncated", action="store_true",
                    help="set when the research step hit its hard timeout")
    args = ap.parse_args(argv)

    report_dir = REPO / "reports" / args.date
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / "report.json"

    ok, detail = is_valid(report_path)
    if ok:
        print(f"report.json OK ({detail})")
        return 0

    print(f"report.json unusable: {detail}", file=sys.stderr)
    print("Writing a stub report so the Sheet still updates.", file=sys.stderr)

    if report_path.exists():
        broken = report_dir / "report.invalid.json"
        broken.write_text(report_path.read_text())
        print(f"Preserved the unusable file at {broken.relative_to(REPO)}", file=sys.stderr)

    report_path.write_text(
        json.dumps(stub(args.date, detail, report_dir / "notes.md", args.research_truncated), indent=2) + "\n"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
