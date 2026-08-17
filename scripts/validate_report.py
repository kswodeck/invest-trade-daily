#!/usr/bin/env python3
"""Check every recommendation's numbers against reality before it is published.

    python scripts/validate_report.py reports/2026-08-16/report.json            # annotate
    python scripts/validate_report.py reports/2026-08-16/report.json --enforce  # demote failures

The model is good at research and undisciplined about arithmetic. A live report
showed eight reward-to-risk ratios clustered at 2.04-2.33 against a 2.0 floor —
targets nudged until they passed, not eight independent analyses. Prompting asks
for care; this makes a broken number unpublishable.

Every check is deterministic and recomputed from source. Nothing here trusts a
figure the model wrote.

Two modes:
  annotate  attach a `validation` block to each idea and print a report
  --enforce additionally move hard failures to the watchlist, with the reason

Exits 0 unless --enforce leaves zero recommendations standing.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

ET = ZoneInfo("America/New_York")

BULLISH = {"buy", "long", "yes"}
BEARISH = {"sell", "sell_short", "short", "no"}

RR_FLOOR = {"intraday": 1.5, "swing": 2.0, "long_term": 2.5}

# How far a target may sit from entry, in ATRs, before it stops being a
# forecast and starts being a wish. Long-term targets are valuation-anchored
# and legitimately far away, so they are exempt.
ATR_LIMIT = {"intraday": 2.0, "swing": 6.0}

# Sessions per horizon, for the "is this move reachable in time" estimate.
HORIZON_SESSIONS = {"intraday": 1, "swing": 15}

PASS, WARN, FAIL = "pass", "warn", "fail"


def _check(name: str, status: str, detail: str) -> dict[str, str]:
    return {"check": name, "status": status, "detail": detail}


# --------------------------------------------------------------------------
# individual checks
# --------------------------------------------------------------------------

def check_direction(idea: dict) -> list[dict]:
    """Longs must have target above entry and downside below it. And vice versa."""
    entry = (idea.get("entry") or {}).get("ideal")
    target = (idea.get("exit") or {}).get("target")
    down = idea.get("stop") if idea.get("stop") is not None else idea.get("bear_case_price")
    direction = idea.get("direction", "")
    bullish = direction in BULLISH

    if entry is None or target is None:
        return [_check("direction_consistency", FAIL, "entry or target is missing")]

    problems = []
    if bullish and target <= entry:
        problems.append(f"target {target} is not above entry {entry} for a {direction}")
    if not bullish and target >= entry:
        problems.append(f"target {target} is not below entry {entry} for a {direction}")
    if down is not None:
        if bullish and down >= entry:
            problems.append(f"downside {down} is not below entry {entry} for a {direction}")
        if not bullish and down <= entry:
            problems.append(f"downside {down} is not above entry {entry} for a {direction}")

    if problems:
        return [_check("direction_consistency", FAIL, "; ".join(problems))]
    return [_check("direction_consistency", PASS, "entry, target and downside are ordered correctly")]


def check_risk_reward(idea: dict) -> tuple[list[dict], float | None]:
    """Recompute R:R from the actual numbers rather than trusting the claim."""
    entry = (idea.get("entry") or {}).get("ideal")
    target = (idea.get("exit") or {}).get("target")
    down = idea.get("stop") if idea.get("stop") is not None else idea.get("bear_case_price")
    horizon = idea.get("horizon", "swing")
    floor = RR_FLOOR.get(horizon, 2.0)

    if entry is None or target is None:
        return [_check("risk_reward", FAIL, "cannot compute without entry and target")], None
    if down is None:
        label = "bear_case_price" if horizon == "long_term" else "stop"
        return [_check("risk_reward", FAIL, f"no {label}, so risk is undefined")], None

    reward, risk = abs(target - entry), abs(entry - down)
    if risk == 0:
        return [_check("risk_reward", FAIL, "downside equals entry — risk is zero")], None

    computed = round(reward / risk, 2)
    out = []
    if computed < floor:
        out.append(_check("risk_reward", FAIL,
                          f"computed {computed}:1 is below the {floor}:1 floor for {horizon}"))
    else:
        out.append(_check("risk_reward", PASS, f"computed {computed}:1 clears the {floor}:1 floor"))

    claimed = idea.get("risk_reward")
    if claimed is not None and abs(claimed - computed) > 0.15:
        out.append(_check("risk_reward_claim", WARN,
                          f"report claims {claimed}:1 but the numbers give {computed}:1"))
    return out, computed


def check_entry_vs_live(idea: dict, live: float | None) -> list[dict]:
    """An entry far from the live price is stale, fat-fingered, or invented."""
    entry = (idea.get("entry") or {}).get("ideal")
    if live is None:
        return [_check("entry_vs_live", WARN, "no live price available to compare against")]
    if entry is None:
        return [_check("entry_vs_live", FAIL, "no entry price")]

    drift = (entry - live) / live * 100
    detail = f"entry {entry} is {drift:+.1f}% from live {round(live, 4)}"
    if abs(drift) > 40:
        return [_check("entry_vs_live", FAIL, detail + " — implausible, likely a bad number")]
    if abs(drift) > 15:
        return [_check("entry_vs_live", WARN, detail + " — far from the market")]
    return [_check("entry_vs_live", PASS, detail)]


def check_catalyst_date(idea: dict, today: date) -> list[dict]:
    """A catalyst in the past is not a catalyst."""
    cat = idea.get("catalyst") or {}
    raw = cat.get("datetime_et")
    if not raw:
        if idea.get("horizon") == "long_term":
            return [_check("catalyst_date", PASS, "long-term idea, no dated event expected")]
        return [_check("catalyst_date", WARN, "no date given for a timed idea")]
    try:
        when = datetime.fromisoformat(raw.replace("Z", "+00:00")).date()
    except ValueError:
        return [_check("catalyst_date", WARN, f"unparseable date {raw!r}")]

    if when < today:
        return [_check("catalyst_date", FAIL,
                       f"catalyst dated {when} already passed — positioning around it is wrong")]
    if when > today + timedelta(days=120):
        return [_check("catalyst_date", WARN, f"catalyst {when} is more than four months out")]
    return [_check("catalyst_date", PASS, f"catalyst {when} is ahead of us")]


def check_earnings_date(idea: dict, calendar: dict[str, str]) -> list[dict]:
    """Cross-check a claimed earnings date against the real calendar.

    A wrong earnings date is worse than a missing one: you position for Tuesday
    and the company reports Thursday.
    """
    cat = idea.get("catalyst") or {}
    event = (cat.get("event") or "").lower()
    if "earnings" not in event and "results" not in event:
        return []
    symbol = (idea.get("symbol") or "").upper()
    actual = calendar.get(symbol)
    if not actual:
        return [_check("earnings_date", WARN,
                       f"claims an earnings catalyst but {symbol} is not on the fetched calendar")]
    raw = cat.get("datetime_et")
    if not raw:
        return [_check("earnings_date", WARN, f"no date given; calendar says {actual}")]
    claimed = raw[:10]
    if claimed != actual:
        return [_check("earnings_date", FAIL,
                       f"report says {claimed} but the calendar says {actual}")]
    return [_check("earnings_date", PASS, f"earnings date {actual} confirmed against the calendar")]


def check_target_feasibility(idea: dict, atr: float | None) -> list[dict]:
    """Is the move actually reachable in the stated horizon?"""
    horizon = idea.get("horizon", "swing")
    if horizon == "long_term":
        return [_check("target_feasibility", PASS, "long-term target is valuation-anchored, not ATR-bound")]
    limit = ATR_LIMIT.get(horizon)
    entry = (idea.get("entry") or {}).get("ideal")
    target = (idea.get("exit") or {}).get("target")
    if atr is None or entry is None or target is None or limit is None:
        return [_check("target_feasibility", WARN, "no ATR available to size the move against")]
    if atr == 0:
        return [_check("target_feasibility", WARN, "ATR is zero")]

    multiple = round(abs(target - entry) / atr, 2)
    sessions = HORIZON_SESSIONS.get(horizon, 15)
    detail = f"target is {multiple} ATR away, {sessions} session(s) to get there"
    if multiple > limit:
        return [_check("target_feasibility", WARN,
                       detail + f" — beyond the {limit} ATR guide for {horizon}, likely optimistic")]
    return [_check("target_feasibility", PASS, detail)]


def check_sources(idea: dict, session: Any) -> list[dict]:
    """Catch hallucinated URLs.

    Deliberately lenient: many publishers block automated requests, so a 403 or
    405 says nothing about whether the page exists. Only a clear 404 or a DNS
    failure is treated as evidence the source was invented.
    """
    urls = idea.get("sources") or []
    if not urls:
        return [_check("sources", FAIL, "no sources")]
    dead, unverifiable = [], 0
    for url in urls[:4]:
        try:
            resp = session.head(url, timeout=10, allow_redirects=True)
            if resp.status_code == 404:
                dead.append(url)
            elif resp.status_code >= 400:
                unverifiable += 1
        except Exception:  # noqa: BLE001 - network failure is not proof of a bad URL
            unverifiable += 1
    if dead:
        return [_check("sources", FAIL, f"{len(dead)} source(s) return 404: {', '.join(dead[:2])}")]
    if unverifiable:
        return [_check("sources", WARN,
                       f"{unverifiable} of {len(urls[:4])} source(s) could not be verified "
                       "(bot-blocked or unreachable), which is not proof they are wrong")]
    return [_check("sources", PASS, f"all {len(urls[:4])} checked source(s) resolve")]


# --------------------------------------------------------------------------
# orchestration
# --------------------------------------------------------------------------

def fetch_context(ideas: list[dict]) -> tuple[dict[str, float], dict[str, float], dict[str, str]]:
    """Live prices, ATRs, and the earnings calendar — fetched once, shared."""
    import market_data as md

    prices: dict[str, float] = {}
    atrs: dict[str, float] = {}
    for idea in ideas:
        symbol = idea.get("symbol", "")
        cls = idea.get("asset_class")
        if not symbol or cls == "event":
            continue
        try:
            if cls == "crypto":
                res = md.crypto([symbol.lower()])
                vals = list(res.get("prices", {}).values()) if res.get("ok") else []
                if vals and vals[0].get("price"):
                    prices[symbol] = vals[0]["price"]
                continue
            q = md.quote(symbol)
            if q.get("ok") and q.get("price"):
                prices[symbol] = q["price"]
            h = md.history(symbol, 90)
            if h.get("ok") and h.get("atr14"):
                atrs[symbol] = h["atr14"]
        except Exception as exc:  # noqa: BLE001 - validation must not crash the run
            print(f"  note: could not fetch context for {symbol}: {exc}", file=sys.stderr)

    calendar: dict[str, str] = {}
    try:
        cal = md.earnings(45)
        if cal.get("ok"):
            for row in cal.get("earnings", []):
                sym, when = row.get("symbol"), row.get("date")
                if sym and when and sym not in calendar:
                    calendar[sym] = when
    except Exception as exc:  # noqa: BLE001
        print(f"  note: earnings calendar unavailable: {exc}", file=sys.stderr)

    return prices, atrs, calendar


def validate_idea(idea: dict, prices: dict, atrs: dict, calendar: dict,
                  today: date, session: Any) -> dict:
    symbol = idea.get("symbol", "")
    live, atr = prices.get(symbol), atrs.get(symbol)

    checks: list[dict] = []
    checks += check_direction(idea)
    rr_checks, computed_rr = check_risk_reward(idea)
    checks += rr_checks
    checks += check_entry_vs_live(idea, live)
    checks += check_catalyst_date(idea, today)
    checks += check_earnings_date(idea, calendar)
    checks += check_target_feasibility(idea, atr)
    checks += check_sources(idea, session)

    verdict = FAIL if any(c["status"] == FAIL for c in checks) else (
        WARN if any(c["status"] == WARN for c in checks) else PASS)

    return {
        "verdict": verdict,
        "computed_risk_reward": computed_rr,
        "claimed_risk_reward": idea.get("risk_reward"),
        "live_price": live,
        "atr14": atr,
        "checked_at_et": datetime.now(ET).isoformat(timespec="seconds"),
        "checks": checks,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("report", type=Path)
    ap.add_argument("--enforce", action="store_true",
                    help="move hard failures to the watchlist instead of only flagging them")
    args = ap.parse_args(argv)

    report = json.loads(args.report.read_text())
    ideas = sorted(report.get("recommendations", []), key=lambda i: i.get("rank", 99))
    if not ideas:
        print("No recommendations to validate.")
        return 0

    import requests
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (compatible; invest-trade-daily/1.0)"})

    today = date.fromisoformat(report["date"])
    print(f"Validating {len(ideas)} recommendations for {report['date']}...")
    prices, atrs, calendar = fetch_context(ideas)
    print(f"  live prices: {len(prices)}  ATRs: {len(atrs)}  earnings calendar: {len(calendar)} symbols")

    for idea in ideas:
        idea["validation"] = validate_idea(idea, prices, atrs, calendar, today, session)

    failed = [i for i in ideas if i["validation"]["verdict"] == FAIL]
    warned = [i for i in ideas if i["validation"]["verdict"] == WARN]

    print(f"\n{'Symbol':<10} {'Verdict':<8} {'RR (claimed→computed)':<24} Issues")
    for idea in ideas:
        v = idea["validation"]
        rr = f"{v['claimed_risk_reward']} → {v['computed_risk_reward']}"
        issues = "; ".join(c["detail"] for c in v["checks"] if c["status"] != PASS) or "—"
        print(f"{idea.get('symbol', ''):<10} {v['verdict']:<8} {rr:<24} {issues[:110]}")

    report["validation_summary"] = {
        "checked": len(ideas),
        "passed": len(ideas) - len(failed) - len(warned),
        "warned": len(warned),
        "failed": len(failed),
        "enforced": bool(args.enforce),
    }

    if args.enforce and failed:
        watchlist = report.setdefault("watchlist", [])
        for idea in failed:
            reasons = "; ".join(c["detail"] for c in idea["validation"]["checks"]
                                if c["status"] == FAIL)
            watchlist.append({
                "symbol": idea.get("symbol", ""),
                "instrument": idea.get("instrument", ""),
                "note": f"Demoted by validation: {reasons}",
                "trigger": "Republish only once the numbers check out.",
                "demoted_from_rank": idea.get("rank"),
                "demotion_reason": reasons,
            })
        kept = [i for i in ideas if i["validation"]["verdict"] != FAIL]
        for rank, idea in enumerate(kept, start=1):
            idea["rank"] = rank
        report["recommendations"] = kept
        report["validation_summary"]["demoted"] = len(failed)
        print(f"\nDemoted {len(failed)} recommendation(s) to the watchlist; {len(kept)} remain.")

        note = (f"Validation demoted {len(failed)} idea(s) whose numbers did not check out. "
                f"{len(warned)} more carry warnings — see the validation block on each.")
        report["data_quality_notes"] = (report.get("data_quality_notes", "") + " " + note).strip()
    else:
        report["recommendations"] = ideas

    args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(f"\nWrote {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
