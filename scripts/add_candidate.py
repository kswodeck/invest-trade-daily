#!/usr/bin/env python3
"""Append one validated candidate to reports/<date>/candidates.jsonl.

    python scripts/add_candidate.py '{"symbol": "NVDA", "direction": "buy", ...}'

Research calls this the moment a candidate is fully specified. Structure is
enforced here, at capture time, so a malformed idea surfaces immediately while
there is still time to fix it — rather than at synthesis, when the research
phase is already dead and the material is unusable.

Prints the running candidate count so the research phase can see its own
progress. Exits non-zero on a malformed candidate, with the reason.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO / "scripts" / "report_schema.json"
ET = ZoneInfo("America/New_York")

# Fields a candidate must carry to be worth anything downstream. `rank` is
# assigned at synthesis, so it is not required here.
REQUIRED = ["symbol", "instrument", "asset_class", "venue", "direction",
            "horizon", "conviction", "entry", "exit", "catalyst", "thesis",
            "key_risk", "sources"]


def candidate_schema() -> dict[str, Any]:
    schema = json.loads(SCHEMA_PATH.read_text())
    idea = schema["definitions"]["idea"]
    idea = json.loads(json.dumps(idea))  # copy before mutating
    idea["required"] = REQUIRED
    idea["properties"].pop("rank", None)
    idea["$defs"] = schema.get("definitions", {})
    return idea


def validate(candidate: dict[str, Any]) -> None:
    try:
        import jsonschema
    except ImportError:
        missing = [f for f in REQUIRED if f not in candidate]
        if missing:
            raise SystemExit(f"missing required field(s): {', '.join(missing)}")
        return
    try:
        jsonschema.validate(candidate, candidate_schema())
    except jsonschema.ValidationError as exc:
        path = ".".join(str(p) for p in exc.absolute_path) or "(root)"
        raise SystemExit(f"invalid candidate at `{path}`: {exc.message}") from exc


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("candidate", help="the candidate as a JSON object")
    ap.add_argument("--date", default=None, help="report date; defaults to today in ET")
    args = ap.parse_args(argv)

    date_str = args.date or datetime.now(ET).date().isoformat()

    try:
        candidate = json.loads(args.candidate)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"not valid JSON: {exc}") from exc
    if not isinstance(candidate, dict):
        raise SystemExit("expected a JSON object, got a " + type(candidate).__name__)

    validate(candidate)

    out_dir = REPO / "reports" / date_str
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "candidates.jsonl"

    candidate.setdefault("captured_at_et", datetime.now(ET).isoformat(timespec="seconds"))
    with path.open("a") as fh:
        fh.write(json.dumps(candidate) + "\n")

    count = sum(1 for line in path.read_text().splitlines() if line.strip())
    print(f"saved {candidate['symbol']} ({candidate['direction']}, "
          f"conviction {candidate['conviction']}) — {count} candidate(s) captured")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
