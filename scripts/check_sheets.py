#!/usr/bin/env python3
"""Verify Google Sheets credentials and write access, without touching data.

    python scripts/check_sheets.py

Writes a timestamp to a scratch tab named `_healthcheck`, reads it back, then
deletes the tab. Prints a markdown block. Exits non-zero on failure so the
workflow step goes red when the Sheet is misconfigured.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone


def main() -> int:
    print("\n## Google Sheets check\n")

    raw = os.environ.get("GCP_SERVICE_ACCOUNT_JSON", "").strip()
    sheet_id = os.environ.get("GOOGLE_SHEET_ID", "").strip()

    if not raw or not sheet_id:
        missing = [n for n, v in
                   [("GCP_SERVICE_ACCOUNT_JSON", raw), ("GOOGLE_SHEET_ID", sheet_id)] if not v]
        print(f"❌ Missing secret(s): `{'`, `'.join(missing)}`")
        return 1

    try:
        info = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"❌ `GCP_SERVICE_ACCOUNT_JSON` is not valid JSON: `{exc}`")
        print("\nPaste the key file's full contents, raw — not base64-encoded.")
        return 1

    email = info.get("client_email", "<no client_email in key>")
    print(f"Service account: `{email}`\n")

    try:
        import gspread
        from google.oauth2.service_account import Credentials

        creds = Credentials.from_service_account_info(
            info, scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        sh = gspread.authorize(creds).open_by_key(sheet_id)
    except Exception as exc:  # noqa: BLE001
        print(f"❌ Could not open the spreadsheet: `{exc}`\n")
        print(f"Most likely cause: the Sheet is not shared with `{email}`.")
        print("Open the Sheet → Share → paste that address → Editor → Share.")
        return 1

    print(f"✅ Opened **{sh.title}**")
    print(f"   Existing tabs: {', '.join(ws.title for ws in sh.worksheets())}\n")

    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    try:
        ws = sh.add_worksheet(title="_healthcheck", rows=2, cols=2)
        ws.update([["healthcheck", stamp]], "A1")
        got = ws.get("B1")[0][0]
        sh.del_worksheet(ws)
    except Exception as exc:  # noqa: BLE001
        print(f"❌ Write test failed: `{exc}`\n")
        print(f"The service account can read the Sheet but may not have Editor access.")
        return 1

    if got != stamp:
        print(f"❌ Read-back mismatch: wrote `{stamp}`, read `{got}`")
        return 1

    print("✅ Write, read-back, and cleanup all succeeded. Sheets is ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
