#!/usr/bin/env python3
"""Announce qualifying odd-lot tenders as GitHub issues.

    python scripts/notify_odd_lot.py --dry-run
    python scripts/notify_odd_lot.py

Most days the screener finds nothing, so nobody opens the tab. A Tier A or B
offer has a deadline on it, and it has to come and find you rather than wait to
be looked at.

**An issue, not a red build.** Failing the workflow is how this repo alarms —
GitHub emails the owner on a failed scheduled run, and `Report Watchdog` and
the stub check both rely on it. But those are failures, and a tender offer is
good news. Overloading red to mean "something good happened" would make the
colour meaningless in the one repo where it is load-bearing, and you would no
longer be able to tell a broken screener from a productive one at a glance.

An issue is the right shape for other reasons too. It notifies by email and
mobile push through machinery already configured. It carries the quoted
paragraph, the numbers and the deadline, so the decision can be made from the
notification. It has a lifecycle: it closes when the offer expires. And it is
addressed to a person, which is what an offer with a withdrawal deadline needs.

Needs `GITHUB_TOKEN` (with `issues: write`) and `GITHUB_REPOSITORY`. Without
them it explains itself and exits 0 — a missing notification channel must never
be what breaks a screening run.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import odd_lot  # noqa: E402

ET = ZoneInfo("America/New_York")
API = "https://api.github.com"

DISCLAIMER = (
    "Automated research, not investment advice. Verify the quoted paragraph in the "
    "linked filing before tendering. You must tender **all** shares you own, and "
    "ownership aggregates across every account under your SSN."
)


def _pct(value: float | None) -> str:
    return "—" if value is None else f"{value * 100:+.2f}%"


def _usd(value: float | None) -> str:
    return "—" if value is None else f"${value:,.2f}"


def issue_title(entry: dict[str, Any]) -> str:
    """Front-loaded with the decision: tier, ticker, spread, deadline."""
    return (f"[Tier {entry.get('tier')}] {entry.get('ticker') or '?'} odd-lot tender — "
            f"{_pct(entry.get('spread_pct'))} spread, expires "
            f"{entry.get('expiration_date') or 'unknown'}")


def issue_body(entry: dict[str, Any], config: dict[str, Any]) -> str:
    """Everything needed to accept or reject it without opening anything else."""
    econ = config["economics"]
    shares = econ["shares_tendered"]

    if entry.get("dutch_range"):
        low, high = entry["dutch_range"]
        offer = f"{_usd(low)}  (Dutch range {_usd(low)}–{_usd(high)}, low end used)"
    else:
        offer = _usd(entry.get("offer_price"))

    withdrawal = entry.get("withdrawal_deadline") or "—"
    if withdrawal != "—" and entry.get("withdrawal_basis") == "expiration_date":
        withdrawal += " _(no separate date stated; runs to expiration)_"

    flags = entry.get("risk_flags") or []
    rows = [
        ("Company", f"{entry.get('company') or '—'} (CIK {entry.get('cik')})"),
        ("Form", f"{entry.get('form') or '—'} filed {entry.get('filed') or '—'}"),
        ("Offer price", offer),
        ("Current price", f"{_usd(entry.get('market_price'))} "
                          f"({entry.get('price_source') or 'no source'}, "
                          f"as of {entry.get('price_asof') or '—'})"),
        ("Spread", f"**{_pct(entry.get('spread_pct'))}**"),
        ("Annualized", _pct(entry.get("annualized"))),
        (f"Capital for {shares} shares", f"**{_usd(entry.get('capital'))}**"),
        (f"Gross profit on {shares} shares", _usd(entry.get("gross_profit"))),
        ("Expires", f"**{entry.get('expiration_date') or '—'}** "
                    f"({entry.get('days_to_expiry', '—')} days)"),
        ("Withdrawal deadline", withdrawal),
        ("30-day avg volume", f"{entry['avg_volume_30d']:,}"
                              if entry.get("avg_volume_30d") else "—"),
        ("Risk flags", ", ".join(f.replace("_", " ") for f in flags) if flags else "none"),
    ]

    out = [
        f"### Tier {entry.get('tier')} — {entry.get('ticker') or '?'}",
        "",
    ]
    # Above the table, because gate_document phrases these as "terms below".
    for warning in entry.get("warnings") or []:
        out += ["> [!WARNING]", f"> {warning}", ""]

    out += [
        "| | |", "| --- | --- |",
        *(f"| {label} | {value} |" for label, value in rows),
        "",
        f"**[Read the offer document]({entry.get('url', '')})** · "
        f"[filing index]({entry.get('index_url', '')})",
        "",
    ]

    if entry.get("odd_lot_paragraph"):
        out += ["**The odd-lot language, quoted from the filing:**", "",
                "> " + " ".join(entry["odd_lot_paragraph"].split()), ""]

    out += [
        "**Before you tender**",
        "",
        f"- Buy **{shares}** shares — fewer than 100. 100 forfeits the preference.",
        "- Tender **every** share you own. A partial tender forfeits it entirely.",
        "- Ownership aggregates across all accounts by SSN; it cannot be split.",
        "- Your broker's tender deadline runs **ahead** of the offer's, often by a "
        "full business day.",
        "- The issuer can amend or remove the preference before expiration.",
        "",
        "---",
        "",
        f"_{DISCLAIMER}_",
        "",
        f"_Opened automatically by `scripts/notify_odd_lot.py`. It closes when the "
        f"offer expires or stops clearing the gates. Screened "
        f"{entry.get('last_scored') or 'today'}._",
    ]
    return "\n".join(out)


# --------------------------------------------------------------------------
# GitHub
# --------------------------------------------------------------------------

class Github:
    """The two calls this needs. Imported lazily; see test_no_hard_dependencies."""

    def __init__(self, token: str, repository: str) -> None:
        self.repository = repository
        self._token = token
        self._session = None

    def _http(self):
        if self._session is None:
            import requests

            self._session = requests.Session()
            self._session.headers.update({
                "Authorization": f"Bearer {self._token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "invest-trade-daily-odd-lot",
            })
        return self._session

    def create_issue(self, title: str, body: str, labels: list[str]) -> int:
        resp = self._http().post(
            f"{API}/repos/{self.repository}/issues",
            json={"title": title, "body": body, "labels": labels}, timeout=30)
        resp.raise_for_status()
        return int(resp.json()["number"])

    def close_issue(self, number: int, comment: str) -> None:
        http = self._http()
        http.post(f"{API}/repos/{self.repository}/issues/{number}/comments",
                  json={"body": comment}, timeout=30).raise_for_status()
        http.patch(f"{API}/repos/{self.repository}/issues/{number}",
                   json={"state": "closed", "state_reason": "completed"},
                   timeout=30).raise_for_status()


def closing_comment(entry: dict[str, Any]) -> str:
    if entry.get("status") == "expired":
        return f"Closing: the offer expired {entry.get('expiration_date')}."
    reasons = "; ".join(entry.get("rejections") or [])
    if reasons:
        return f"Closing: no longer clears the gates — {reasons}."
    return (f"Closing: no longer a Tier {(entry.get('notified') or {}).get('tier')} "
            f"opportunity (now tier {entry.get('tier') or 'none'}).")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true",
                    help="print the issues that would be opened and closed")
    args = ap.parse_args(argv)

    config = odd_lot.load_config()
    universe = odd_lot.load_universe()
    due = odd_lot.notifications_due(universe, config)
    stale = odd_lot.notifications_to_close(universe, config)

    print(f"{len(due)} offer(s) to announce, {len(stale)} issue(s) to close "
          f"(floor: Tier {config['notify']['min_tier']}).")
    if not due and not stale:
        return 0

    token = os.environ.get("GITHUB_TOKEN", "").strip()
    repository = os.environ.get("GITHUB_REPOSITORY", "").strip()

    if args.dry_run or not (token and repository):
        if not args.dry_run:
            # Never the thing that breaks a screening run: the universe, the
            # report and the tab have all already been written by this point.
            print("GITHUB_TOKEN or GITHUB_REPOSITORY is not set — printing instead. "
                  "Grant the workflow `issues: write` to have these opened.",
                  file=sys.stderr)
        for entry in due:
            print(f"\n{'=' * 78}\n{issue_title(entry)}\n{'=' * 78}")
            print(issue_body(entry, config))
        for entry in stale:
            told = entry.get("notified") or {}
            print(f"\nwould close #{told.get('issue')}: {closing_comment(entry)}")
        return 0

    gh = Github(token, repository)
    now = datetime.now(ET)
    opened = 0
    for entry in due:
        try:
            number = gh.create_issue(issue_title(entry), issue_body(entry, config),
                                     config["notify"]["labels"])
        except Exception as exc:  # noqa: BLE001 - an alert is not worth the run
            print(f"::warning title=Odd-lot alert failed::could not open an issue for "
                  f"{entry.get('ticker')}: {type(exc).__name__}: {exc}")
            continue
        odd_lot.record_notified(entry, issue=number, now=now)
        opened += 1
        print(f"Opened #{number}: {issue_title(entry)}")

    closed = 0
    for entry in stale:
        told = entry.get("notified") or {}
        try:
            gh.close_issue(int(told["issue"]), closing_comment(entry))
        except Exception as exc:  # noqa: BLE001
            print(f"::warning::could not close issue #{told.get('issue')}: {exc}")
            continue
        told["closed"] = now.isoformat(timespec="seconds")
        closed += 1
        print(f"Closed #{told['issue']}.")

    if opened or closed:
        odd_lot.save_universe(universe)
    print(f"\nOpened {opened}, closed {closed}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
