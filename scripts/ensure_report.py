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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from report_state import PUBLISHED, classify  # noqa: E402

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
        pass  # fall through to the emptiness check, which needs no schema
    except Exception as exc:  # noqa: BLE001 - jsonschema.ValidationError and friends
        return False, f"report.json failed schema validation: {str(exc).splitlines()[0]}"

    # Schema-valid is not the same as finished. A synthesis phase killed
    # mid-write leaves behind a well-formed skeleton — on 2026-08-28 it was
    # {"data_quality_notes": "Synthesis in progress.", "recommendations": []} —
    # which passes validation and then goes to the Sheet as if it were the
    # morning's work. A report carrying neither a recommendation nor a
    # watchlist entry has concluded nothing, so say that in the stub's words
    # rather than publishing a placeholder.
    if classify(report) != PUBLISHED:
        return False, "report.json holds no recommendations and no watchlist"

    return True, f"valid, {len(report.get('recommendations', []))} recommendations"


def notes_excerpt(report_dir: Path, limit: int = 600) -> str:
    """Describe what research left behind, and where the pipeline broke."""
    notes_path = report_dir / "notes.md"
    candidates_path = report_dir / "candidates.jsonl"

    captured = 0
    if candidates_path.exists():
        captured = sum(1 for line in candidates_path.read_text().splitlines() if line.strip())

    if not notes_path.exists():
        return (
            f"No research notes were produced and {captured} candidate(s) were captured. "
            "The research phase likely failed at startup rather than running out of time."
        )
    text = notes_path.read_text().strip()
    if not text:
        return "Research notes file was created but left empty."

    head = text[-limit:] if len(text) > limit else text

    if captured:
        diagnosis = (
            f"{captured} candidate(s) were captured but synthesis did not convert them, "
            "so this is a synthesis failure, not a research failure — the material exists "
            f"in reports/{report_dir.name}/candidates.jsonl and is worth reading directly."
        )
    else:
        diagnosis = (
            "No candidates were captured despite the research above, so the research phase "
            "spent its budget gathering without converting anything into a tradeable idea "
            "before the cap killed it."
        )

    return (
        f"Research produced {len(text)} characters of notes and {captured} captured "
        f"candidate(s). {diagnosis} Tail of the log: ...{head}"
    )


def stub(date_str: str, reason: str, report_dir: Path, truncated: bool) -> dict:
    return {
        "date": date_str,
        "generated_at_et": datetime.now(ET).isoformat(timespec="seconds"),
        "research_minutes": None,
        "truncated": truncated,
        "pipeline_failure": True,
        "data_quality_notes": (
            f"NO RECOMMENDATIONS PUBLISHED. The synthesis phase did not produce a usable "
            f"report ({reason}). {notes_excerpt(report_dir)} "
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
        json.dumps(stub(args.date, detail, report_dir, args.research_truncated), indent=2) + "\n"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
