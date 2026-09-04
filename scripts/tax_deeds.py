#!/usr/bin/env python3
"""Screening logic for Texas tax deed sales — Dallas, Tarrant, Johnson, Ellis.

    python scripts/tax_deeds.py thresholds          # what the gates are set to
    python scripts/tax_deeds.py statement           # 34.015 written statement status

Pure logic: gates, redemption law, economics, tiering, and the rendering of
both outputs. It fetches nothing, so it imports on a bare runner and every
rule below is testable without a network. `tax_deed_sources.py` does the
fetching; `tax_deed_screen.py` wires the two together.

THIS MODULE DOES NOT CERTIFY TITLE AND CANNOT. County clerk lien records are
not reliably machine-readable. Everything it emits is a CANDIDATE requiring a
professional title search before a bid. Nothing here may be written, commented,
or rendered in a way that suggests otherwise.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO / "config" / "tax_deeds.json"
SNAPSHOT_DIR = REPO / "data" / "tax_deeds"
PACKET_DIR = REPO / "reports" / "tax_deeds"

ET = ZoneInfo("America/New_York")

# Repeated verbatim in row 1 of the sheet, at the top of every packet, and in
# the run summary. It is the one claim this tool is actually making.
DISCLAIMER = (
    "NOT A TITLE SEARCH — EVERY ROW IS A CANDIDATE ONLY. This tool reads public county "
    "sale lists and appraisal district records. It cannot and does not certify title. "
    "County clerk lien records are not reliably machine-readable, so liens that survive a "
    "tax sale — federal tax liens (IRC §7425(d) gives the IRS 120 days to redeem after the "
    "sale), some HOA assessments, environmental liens, and super-priority PACE liens — may "
    "exist on any row here and go undetected. A blank in the Flags column means nothing was "
    "found by the checks that ran, never that the property is clear. Order a professional "
    "title search before you bid. Tex. Tax Code §34.015 separately requires an unexpired "
    "written statement from the county assessor-collector before a deed can be delivered."
)

# --------------------------------------------------------------------------
# Tex. Tax Code §34.21 — redemption
# --------------------------------------------------------------------------
#
# Two periods, and which one applies is a property-type question answered from
# the CAD record, not from the sale list. Homestead, agricultural and mineral
# property redeem for two years; the premium is 25% of the bid in year one and
# 50% in year two. Everything else redeems for 180 days at 25%.
#
# The two-year classes are rejected at Gate 1, so in practice every surviving
# row is the 180-day case. The long form stays here because the packet has to
# state the period it actually derived, and because a Gate 1 threshold change
# must not silently start mispricing redemptions.
LONG_REDEMPTION_DAYS = 730
SHORT_REDEMPTION_DAYS = 180
PENALTY_YEAR_ONE = 0.25
PENALTY_YEAR_TWO = 0.50

# Exemption codes and land-use markers that put a property in the two-year
# class. Matched case-insensitively as substrings of the CAD exemption strings.
HOMESTEAD_MARKERS = ("HOMESTEAD", "HS", "RESIDENCE HOMESTEAD", "OV65", "OVER 65", "DV", "DISABLED")
AGRICULTURAL_MARKERS = ("AG", "AGRICULTURAL", "1-D-1", "1D1", "OPEN SPACE", "TIMBER", "WILDLIFE")

# The IRS redemption right that survives the sale when a federal tax lien was
# of record. 120 days from the sale, or the state period, whichever is longer.
IRS_REDEMPTION_DAYS = 120

# --------------------------------------------------------------------------
# checks
# --------------------------------------------------------------------------

CLEAN, HIT, UNAVAILABLE = "clean", "hit", "unavailable"

MATERIAL, MINOR, UNIVERSAL = "material", "minor", "universal"

# What each Gate 2 check does on a hit, and how bad it is when the check could
# not run at all.
#
# "Unavailable" is never "clean". A check that did not run leaves the property
# unscreened for that lien, and the severity says how much that matters: the
# two checks that would have rejected the property outright are material when
# missing, because their absence is the absence of the screen this tool exists
# to run. The flag-only checks degrade to a minor flag.
#
# Consequence worth knowing before you go debugging: if the clerk adapters are
# unreachable — and they usually are, the portals are session-gated — then every
# property carries two material flags and the whole run grades Tier C. That is
# the tool reporting that it screened nothing, not a bug. Fix the adapter or
# accept that the shortlist is unranked.
LIEN_CHECKS: dict[str, dict[str, str]] = {
    "federal_tax_lien": {"on_hit": "reject", "on_unavailable": MATERIAL},
    "pace_lien":        {"on_hit": "reject", "on_unavailable": MATERIAL},
    "hoa_assessment":   {"on_hit": MINOR,    "on_unavailable": MINOR},
    "municipal_lien":   {"on_hit": MATERIAL, "on_unavailable": MINOR},
    "environmental":    {"on_hit": MATERIAL, "on_unavailable": MINOR},
}

CHECK_LABELS = {
    "federal_tax_lien": "federal tax lien",
    "pace_lien": "PACE lien",
    "hoa_assessment": "HOA / POA assessment",
    "municipal_lien": "municipal code / demolition lien",
    "environmental": "environmental use",
    "flood_zone": "FEMA flood zone",
    "road_frontage": "road frontage",
    "lot_size": "municipal minimum lot size",
}

DEFAULT_THRESHOLDS: dict[str, Any] = {
    "MAX_OPENING_BID": 20000,
    "MAX_BID_TO_VALUE": 0.75,
    "TIER_A_BID_TO_VALUE": 0.35,
    "QUIET_TITLE_BUDGET": 3500,
    "HOLDING_MONTHS": 7,
    "REJECT_FLOOD_ZONE": False,
    "EFFECTIVE_TAX_RATE": 0.023,
    "MONTHLY_CARRY": 75,
    "POST_JUDGMENT_YEARS": 1.0,
    "TEARDOWN_IMPROVEMENT_VALUE": 5000,
    "STATEMENT_WARN_DAYS": 30,
    "MAX_ENRICHMENTS": 250,
    "TIER_A_MAX_MINOR_FLAGS": 1,
    "TIER_B_MAX_MINOR_FLAGS": 2,
    "PACKET_TIERS": "A,B",
}

BOOL_THRESHOLDS = {"REJECT_FLOOD_ZONE"}
STRING_THRESHOLDS = {"PACKET_TIERS"}


# --------------------------------------------------------------------------
# config
# --------------------------------------------------------------------------

def load_config(path: Path | None = None) -> dict:
    """Read config/tax_deeds.json. Missing file is fatal, not a default."""
    path = path or CONFIG_PATH
    if not path.exists():
        raise SystemExit(
            f"{path} is missing. Every county URL and threshold lives there; "
            f"the screener has no hardcoded fallback on purpose."
        )
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{path} is not valid JSON: {exc}") from exc


def threshold(cfg: dict, name: str) -> Any:
    """Resolve a knob: environment beats the config file beats the default.

    The environment override exists so a workflow can widen or tighten a gate
    for one run without a commit, the same way REPORT_WINDOW_ET works for the
    daily report.
    """
    raw = os.environ.get(name)
    if raw is None:
        raw = (cfg.get("thresholds") or {}).get(name)
    if raw is None:
        raw = DEFAULT_THRESHOLDS[name]

    if name in BOOL_THRESHOLDS:
        if isinstance(raw, bool):
            return raw
        return str(raw).strip().lower() in {"1", "true", "yes", "on"}
    if name in STRING_THRESHOLDS:
        return str(raw).strip()
    if isinstance(raw, (int, float)):
        return raw
    try:
        return float(raw)
    except (TypeError, ValueError):
        raise SystemExit(f"{name}={raw!r} is not a number")


def counties(cfg: dict) -> list[dict]:
    """Configured counties in report order: Dallas, Tarrant, Johnson, Ellis."""
    return sorted(cfg.get("counties", []), key=lambda c: c.get("order", 99))


def county_order(cfg: dict) -> dict[str, int]:
    return {c["name"]: c.get("order", 99) for c in cfg.get("counties", [])}


# --------------------------------------------------------------------------
# parsing helpers, shared by the adapters and the tests
# --------------------------------------------------------------------------

def parse_money(value: Any) -> float | None:
    """`$12,345.67` -> 12345.67. None when there is no number in there.

    County lists write "TBD", "N/A", "-" and blank interchangeably for "no
    figure published", and every one of them must come back None rather than
    zero — a zero opening bid would sail through every economic gate.
    """
    if value is None:
        return None
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return float(value)
    text = str(value).strip()
    if not text:
        return None
    negative = text.startswith("(") and text.endswith(")")
    cleaned = re.sub(r"[^0-9.]", "", text)
    if not cleaned or cleaned.count(".") > 1:
        return None
    try:
        amount = float(cleaned)
    except ValueError:
        return None
    return -amount if negative else amount


_DATE_FORMATS = ("%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y", "%B %d, %Y", "%b %d, %Y", "%d-%b-%Y")


def parse_date(value: Any) -> str | None:
    """Any of the formats counties publish -> ISO. None when unparseable."""
    if value is None:
        return None
    if isinstance(value, date):
        return value.isoformat()
    text = re.sub(r"\s+", " ", str(value)).strip()
    if not text:
        return None
    for fmt in _DATE_FORMATS:
        try:
            return datetime.strptime(text, fmt).date().isoformat()
        except ValueError:
            continue
    match = re.search(r"(\d{4}-\d{2}-\d{2})", text)
    return match.group(1) if match else None


def normalize_account(value: Any) -> str:
    """CAD accounts are written with and without punctuation; match on both."""
    return re.sub(r"[^0-9A-Za-z]", "", str(value or "")).upper()


def first_tuesday(year: int, month: int) -> date:
    """Texas tax sales are the first Tuesday of the month, statewide."""
    day = date(year, month, 1)
    return day + timedelta(days=(1 - day.weekday()) % 7)


def next_sale_date(today: date) -> date:
    """The next first-Tuesday sale on or after `today`."""
    this_month = first_tuesday(today.year, today.month)
    if this_month >= today:
        return this_month
    year, month = (today.year + 1, 1) if today.month == 12 else (today.year, today.month + 1)
    return first_tuesday(year, month)


def now_iso() -> str:
    return datetime.now(ET).replace(microsecond=0).isoformat()


# --------------------------------------------------------------------------
# check + flag records
# --------------------------------------------------------------------------

def check_record(name: str, result: str, source: str, detail: str = "",
                 checked_at: str | None = None) -> dict:
    """One screening check, with the provenance the packet has to show.

    `result` is exactly one of clean / hit / unavailable. Anything else is a
    programming error and raises here rather than being rendered as a reassuring
    blank three layers down.
    """
    if result not in (CLEAN, HIT, UNAVAILABLE):
        raise ValueError(f"{name}: result must be clean, hit or unavailable, not {result!r}")
    return {
        "check": name,
        "result": result,
        "source": source,
        "detail": detail,
        "checked_at": checked_at or now_iso(),
    }


def flag(code: str, severity: str, detail: str) -> dict:
    if severity not in (MATERIAL, MINOR, UNIVERSAL):
        raise ValueError(f"{code}: unknown severity {severity!r}")
    return {"code": code, "severity": severity, "detail": detail}


def rejection(gate: int, code: str, detail: str) -> dict:
    return {"gate": gate, "code": code, "detail": detail}


def find_check(checks: Iterable[dict], name: str) -> dict | None:
    for check in checks:
        if check.get("check") == name:
            return check
    return None


# --------------------------------------------------------------------------
# property classification
# --------------------------------------------------------------------------

def _markers_in(exemptions: Iterable[str], markers: tuple[str, ...]) -> str | None:
    for raw in exemptions or []:
        text = str(raw).strip().upper()
        if not text:
            continue
        for marker in markers:
            if re.search(rf"(^|[^A-Z]){re.escape(marker)}([^A-Z]|$)", text):
                return text
    return None


def is_homestead(cad: dict | None) -> str | None:
    """The exemption string that makes this a homestead, or None."""
    if not cad:
        return None
    if cad.get("homestead") is True:
        return "homestead flag on the CAD record"
    return _markers_in(cad.get("exemptions") or [], HOMESTEAD_MARKERS)


def is_agricultural(cad: dict | None) -> str | None:
    if not cad:
        return None
    if cad.get("agricultural") is True:
        return "agricultural flag on the CAD record"
    return _markers_in(cad.get("exemptions") or [], AGRICULTURAL_MARKERS)


def is_mineral_only(listing: dict, cad: dict | None) -> str | None:
    """Mineral interests carry the 2-year period and no surface to sell."""
    haystack = " ".join(str(x or "") for x in (
        listing.get("property_type"), listing.get("legal_description"),
        (cad or {}).get("property_type"), (cad or {}).get("legal_description"),
        (cad or {}).get("land_use_code"), (cad or {}).get("land_use_description"),
    )).upper()
    if re.search(r"\bMINERAL\b|\bROYALT|\bWORKING INTEREST\b|\bOIL (?:AND|&) GAS\b", haystack):
        # A surface parcel that merely mentions a severed mineral estate is not
        # a mineral-only interest; a positive improvement or land value says
        # there is real estate attached.
        if (cad or {}).get("land_value") or (cad or {}).get("improvement_value"):
            return None
        return "mineral or royalty interest, no surface estate"
    return None


def is_mobile_home_without_land(listing: dict, cad: dict | None) -> str | None:
    haystack = " ".join(str(x or "") for x in (
        listing.get("property_type"), listing.get("legal_description"),
        (cad or {}).get("property_type"), (cad or {}).get("land_use_description"),
    )).upper()
    if not re.search(r"MOBILE HOME|MANUFACTURED HOM|\bMH\b|MOBILE HM", haystack):
        return None
    if re.search(r"ONLY|W/?O LAND|WITHOUT LAND|PERSONAL PROPERTY|NO LAND", haystack):
        return "mobile/manufactured home without the underlying land"
    land_value = (cad or {}).get("land_value")
    if land_value is not None and float(land_value) <= 0:
        return "mobile/manufactured home with no land value on the CAD record"
    return None


def redemption_terms(listing: dict, cad: dict | None) -> dict:
    """Which §34.21 period governs, and what the former owner would pay.

    Returns the label the sheet prints, the day count the annualized return is
    computed over, and the year-one premium.
    """
    reasons = []
    if is_homestead(cad):
        reasons.append("homestead")
    if is_agricultural(cad):
        reasons.append("agricultural")
    if is_mineral_only(listing, cad):
        reasons.append("mineral")

    if reasons:
        return {
            "label": "2yr",
            "days": LONG_REDEMPTION_DAYS,
            "penalty_year_one": PENALTY_YEAR_ONE,
            "penalty_year_two": PENALTY_YEAR_TWO,
            "basis": f"§34.21(a) — {', '.join(reasons)}",
        }
    return {
        "label": "180d",
        "days": SHORT_REDEMPTION_DAYS,
        "penalty_year_one": PENALTY_YEAR_ONE,
        "penalty_year_two": None,
        "basis": "§34.21(e) — non-homestead, non-agricultural, non-mineral",
    }


# --------------------------------------------------------------------------
# GATE 1 — hard disqualifiers
# --------------------------------------------------------------------------

def gate1_hard_disqualifiers(listing: dict, cad: dict | None, cfg: dict,
                             today: date) -> tuple[list[dict], list[dict]]:
    """Rejections and flags. The split is the whole point of this gate.

    A rejection is a *determination*: something was read and it disqualifies the
    property. Not being able to read something is not a determination, and the
    first live run made the difference concrete — 718 of 758 listings were
    rejected for having no sale date, and they are struck-off properties, which
    by definition have no sale date because there is no auction. Another 664
    went for having no CAD match, which is the appraisal district being
    unreachable rather than anything about the property.

    So: unknowns flag, findings reject.
    """
    out: list[dict] = []
    flags: list[dict] = []
    bid = listing.get("minimum_opening_bid")
    max_bid = threshold(cfg, "MAX_OPENING_BID")
    struck_off = listing.get("sale_type") == "struck_off"

    if bid is None:
        flags.append(flag("no_opening_bid", MATERIAL,
                          "the county list published no minimum bid, so nothing can be "
                          "priced — ask the tax office before bidding"))
    elif bid > max_bid:
        out.append(rejection(1, "opening_bid_over_cap",
                             f"opening bid ${bid:,.0f} is over the ${max_bid:,.0f} cap "
                             f"(MAX_OPENING_BID)"))

    sale_date = listing.get("sale_date")
    if sale_date:
        try:
            if date.fromisoformat(sale_date) < today:
                out.append(rejection(1, "sale_date_passed",
                                     f"sale date {sale_date} is in the past"))
        except ValueError:
            flags.append(flag("unparseable_sale_date", MINOR,
                              f"sale date {sale_date!r} could not be read"))
    elif not struck_off:
        # A struck-off property has no sale date because there is no sale — it
        # is bought over the counter, which is the point of the category.
        flags.append(flag("no_sale_date", MINOR,
                          "the county list published no sale date for an auction listing; "
                          "confirm the date with the county before you travel"))

    status = str(listing.get("status") or "").strip().lower()
    if status and re.search(r"withdraw|pulled|cancel|struck from|removed|paid|bankrupt", status):
        out.append(rejection(1, "withdrawn", f"county list status is {listing['status']!r}"))

    if not cad:
        value, source = valuation(listing, cad)
        if source == "adjudged":
            # Priced, but on the court's judgment-date figure rather than a
            # current roll. Still a material flag: it can be years stale, and
            # the exemption checks below never ran at all.
            flags.append(flag("no_cad_match", MATERIAL,
                              f"no appraisal district record matched this account. Priced on "
                              f"the ${value:,.0f} value published on the county sale list "
                              f"instead — usually the adjudged value from the tax suit, so "
                              f"confirm its basis and its age. The homestead, agricultural "
                              f"and mineral checks all read the CAD record and none ran."))
        else:
            flags.append(flag("no_cad_match", MATERIAL,
                              "no appraisal district record matched this account, so the "
                              "property cannot be valued and nothing below could be checked "
                              "against it — value it by hand before bidding"))
            return out, flags

        bid_now = listing.get("minimum_opening_bid")
        if bid_now is not None and value:
            cap = threshold(cfg, "MAX_BID_TO_VALUE")
            if bid_now / value > cap:
                out.append(rejection(1, "bid_to_value_over_cap",
                                     f"bid-to-value {bid_now / value:.2f} against the adjudged "
                                     f"value is over the {cap:.2f} cap (MAX_BID_TO_VALUE)"))
        return out, flags

    homestead = is_homestead(cad)
    if homestead:
        out.append(rejection(1, "homestead",
                             f"homestead exemption on the CAD record ({homestead}) — 2-year "
                             f"redemption under §34.21(a) makes it illiquid; you cannot sell, "
                             f"re-tenant or remodel without risk"))

    agricultural = is_agricultural(cad)
    if agricultural:
        out.append(rejection(1, "agricultural",
                             f"agricultural exemption on the CAD record ({agricultural}) — "
                             f"2-year redemption under §34.21(a)"))

    mineral = is_mineral_only(listing, cad)
    if mineral:
        out.append(rejection(1, "mineral_only",
                             f"{mineral} — 2-year redemption under §34.21(a)"))

    mobile = is_mobile_home_without_land(listing, cad)
    if mobile:
        out.append(rejection(1, "mobile_home_without_land", mobile))

    cad_value, _ = valuation(listing, cad)
    if cad_value in (None, 0):
        flags.append(flag("no_cad_value", MATERIAL,
                          "neither the CAD record nor the county list carries a value, so "
                          "bid-to-value cannot be computed"))
    elif bid is not None:
        ratio = bid / cad_value
        cap = threshold(cfg, "MAX_BID_TO_VALUE")
        if ratio > cap:
            out.append(rejection(1, "bid_to_value_over_cap",
                                 f"bid-to-value {ratio:.2f} is over the {cap:.2f} cap "
                                 f"(MAX_BID_TO_VALUE)"))
    return out, flags


# --------------------------------------------------------------------------
# GATE 2 — lien and encumbrance screening
# --------------------------------------------------------------------------

def gate2_liens(checks: list[dict], cfg: dict) -> tuple[list[dict], list[dict]]:
    """Rejections and flags from the lien checks.

    A property passes this gate only if every check came back clean, or came
    back unavailable *and* left a flag behind. A check that did not run is
    never silently a pass: a missing check is recorded as `unavailable`, and a
    check that is absent from the list entirely is treated the same way, because
    the two are indistinguishable from the property's point of view.
    """
    rejections: list[dict] = []
    flags: list[dict] = []

    for name, rule in LIEN_CHECKS.items():
        record = find_check(checks, name)
        label = CHECK_LABELS.get(name, name)
        result = record.get("result") if record else UNAVAILABLE
        detail = (record or {}).get("detail") or ""
        source = (record or {}).get("source") or "no adapter ran"

        if result == HIT:
            if rule["on_hit"] == "reject":
                why = f"{label} found: {detail}" if detail else f"{label} found"
                if name == "federal_tax_lien":
                    why += (f" — survives the sale, and IRC §7425(d) gives the IRS "
                            f"{IRS_REDEMPTION_DAYS} days from the sale to redeem")
                if name == "pace_lien":
                    why += " — PACE is super-priority and survives senior foreclosures"
                rejections.append(rejection(2, name, why))
            else:
                flags.append(flag(name, rule["on_hit"],
                                  f"{label} found: {detail}" if detail else f"{label} found"))
        elif result == UNAVAILABLE:
            flags.append(flag(
                f"{name}_unchecked", rule["on_unavailable"],
                f"{label} NOT screened — {detail or 'source unavailable'} ({source}). "
                f"Unknown, not clean."))
        # clean leaves nothing behind; the check itself is the record.

    return rejections, flags


# --------------------------------------------------------------------------
# GATE 3 — physical and marketability
# --------------------------------------------------------------------------

def gate3_physical(listing: dict, cad: dict | None, checks: list[dict],
                   cfg: dict) -> tuple[list[dict], list[dict]]:
    """Flood, access, lot size, teardown, occupancy."""
    rejections: list[dict] = []
    flags: list[dict] = []
    cad = cad or {}

    flood = find_check(checks, "flood_zone")
    # A flood zone is priceable — insurance, elevation certificates, a lower
    # bid — where a homestead's two-year redemption is not. So it flags rather
    # than rejects by default; REJECT_FLOOD_ZONE turns it back into a reject
    # for anyone who would never take one at any price.
    reject_flood = threshold(cfg, "REJECT_FLOOD_ZONE")
    if flood and flood.get("result") == HIT:
        zone = flood.get("detail") or "high-risk zone"
        if reject_flood:
            rejections.append(rejection(3, "flood_zone",
                                        f"FEMA {zone} (REJECT_FLOOD_ZONE is on)"))
        else:
            flags.append(flag("flood_zone", MATERIAL,
                              f"FEMA {zone} — price the flood insurance and the elevation "
                              f"certificate into your maximum bid"))
    elif not flood or flood.get("result") == UNAVAILABLE:
        detail = (flood or {}).get("detail") or "source unavailable"
        flags.append(flag("flood_zone_unchecked", MINOR,
                          f"FEMA flood zone NOT screened — {detail}. Unknown, not clean."))

    frontage = find_check(checks, "road_frontage")
    if frontage and frontage.get("result") == HIT:
        flags.append(flag("landlocked", MATERIAL,
                          f"no apparent road frontage in the CAD geometry — "
                          f"{frontage.get('detail') or 'possibly landlocked'}"))

    lot = find_check(checks, "lot_size")
    if lot and lot.get("result") == HIT:
        flags.append(flag("under_minimum_lot", MATERIAL,
                          f"likely unbuildable — {lot.get('detail')}"))

    improvement = cad.get("improvement_value")
    teardown_floor = threshold(cfg, "TEARDOWN_IMPROVEMENT_VALUE")
    has_structure = bool(cad.get("year_built") or cad.get("sqft") or
                         (improvement is not None and improvement > 0))
    if has_structure and improvement is not None and improvement < teardown_floor:
        flags.append(flag("likely_teardown", MINOR,
                          f"improvement value ${improvement:,.0f} on a parcel with a "
                          f"structure — likely a teardown; price the demolition"))

    # Occupancy cannot be determined remotely, ever. It is flagged on every row
    # rather than inferred, which also means it cannot discriminate between
    # rows — hence UNIVERSAL, which the tiering below deliberately ignores.
    # Removing this flag to tidy up a report would be removing the reason the
    # drive-by is on the checklist.
    flags.append(flag("occupancy_unknown", UNIVERSAL,
                      "occupancy cannot be determined remotely — drive by before you bid. "
                      "§34.21(h) bars the former owner from occupying or collecting rents "
                      "during redemption, and eviction is available, subject to "
                      "servicemember protections and bona fide leases."))
    return rejections, flags


# --------------------------------------------------------------------------
# GATE 4 — economics
# --------------------------------------------------------------------------

def valuation(listing: dict, cad: dict | None) -> tuple[float | None, str]:
    """What this property is worth, and where that number came from.

    The appraisal districts are the good source and are also the flakiest part
    of the pipeline — Tarrant rate-limited 365 straight lookups and Ellis reset
    the connection — and without a value nothing can be priced or ranked at all.

    But the county's own sale list often publishes the **adjudged value**: the
    figure the court set in the tax suit, and the one §34.01(p) measures a
    struck-off resale against. It is a real published number, not an estimate,
    so it is a legitimate second source — and every output says which one was
    used, because an adjudged value is a judgment-date figure and can be years
    stale where a CAD roll is current.
    """
    if cad and cad.get("appraised_value"):
        return float(cad["appraised_value"]), "cad"
    adjudged = listing.get("adjudged_value")
    if adjudged:
        return float(adjudged), "adjudged"
    return None, "none"


def gate4_economics(listing: dict, cad: dict | None, cfg: dict,
                    terms: dict | None = None) -> dict | None:
    """Both outcomes priced, because both are acceptable.

    Redemption and ownership are costed differently on purpose, and getting
    that wrong once made a perfectly good redemption read as a loss:

      * You do not buy a quiet title action on a property that is still
        redeemable, so the redemption case excludes that budget entirely.
      * §34.21(b) makes the former owner reimburse the deed recording fee and
        the taxes, penalties, interest and costs the purchaser paid. Those
        wash, so they are excluded from *both* sides of the redemption case —
        counting them as a cost with no matching reimbursement is what turned a
        17% return into a headline -8%.
      * What is left over the redemption period is the carry the statute does
        not reimburse: insurance and utilities on a vacant parcel.

    The result is still conservative, because §34.21(a) computes the 25%
    premium on the *aggregate total* — bid plus the recording fee plus the
    taxes reimbursed — while this takes it on the bid alone, as the spec does.
    """
    bid = listing.get("minimum_opening_bid")
    cad_value, value_source = valuation(listing, cad)
    if bid is None or not cad_value:
        return None

    terms = terms or redemption_terms(listing, cad)
    tax_rate = threshold(cfg, "EFFECTIVE_TAX_RATE")
    months = threshold(cfg, "HOLDING_MONTHS")
    quiet_title = threshold(cfg, "QUIET_TITLE_BUDGET")

    carry = threshold(cfg, "MONTHLY_CARRY")
    monthly_taxes = cad_value * tax_rate / 12
    holding_costs = months * (monthly_taxes + carry)
    post_judgment_taxes = cad_value * tax_rate * threshold(cfg, "POST_JUDGMENT_YEARS")

    est_total_cost = bid + quiet_title + holding_costs + post_judgment_taxes
    redemption_carry = months * carry           # the part §34.21(b) does not repay
    redemption_capital = bid + redemption_carry
    redemption_payout = bid * (1 + terms["penalty_year_one"])
    redemption_net = redemption_payout - redemption_capital
    redemption_days = terms["days"] if terms["label"] == "180d" else 365

    econ = {
        "opening_bid": round(bid, 2),
        "cad_value": round(float(cad_value), 2),
        "value_source": value_source,
        "bid_to_value": round(bid / cad_value, 4),
        "max_bid": round(cad_value * threshold(cfg, "MAX_BID_TO_VALUE"), 2),
        "quiet_title_budget": round(quiet_title, 2),
        "holding_months": months,
        "holding_costs": round(holding_costs, 2),
        "post_judgment_taxes_estimate": round(post_judgment_taxes, 2),
        "est_total_cost": round(est_total_cost, 2),

        "redemption_period": terms["label"],
        "redemption_basis": terms["basis"],
        "redemption_penalty_year_one": terms["penalty_year_one"],
        "redemption_penalty_year_two": terms["penalty_year_two"],
        "redemption_payout": round(redemption_payout, 2),
        "redemption_carry": round(redemption_carry, 2),
        "redemption_capital": round(redemption_capital, 2),
        "redemption_net_profit": round(redemption_net, 2),
        "redemption_return_pct": round(redemption_net / redemption_capital * 100, 2),
        "redemption_annualized_pct": round(
            redemption_net / redemption_capital * 100 * 365 / redemption_days, 2),

        "ownership_equity": round(cad_value - est_total_cost, 2),
        "ownership_equity_multiple": round(cad_value / est_total_cost, 3),
    }
    if terms["penalty_year_two"] is not None:
        econ["redemption_payout_year_two"] = round(bid * (1 + terms["penalty_year_two"]), 2)
    return econ


# --------------------------------------------------------------------------
# GATE 5 — tiering
# --------------------------------------------------------------------------

def count_flags(flags: list[dict]) -> tuple[int, int]:
    """(material, minor). Universal flags are on every row and rank nothing."""
    material = sum(1 for f in flags if f["severity"] == MATERIAL)
    minor = sum(1 for f in flags if f["severity"] == MINOR)
    return material, minor


def gate5_tier(flags: list[dict], econ: dict | None, cad: dict | None,
               cfg: dict) -> str:
    material, minor = count_flags(flags)
    ratio = (econ or {}).get("bid_to_value")

    if econ is None or ratio is None:
        return "C"
    if material:
        return "C"
    if minor > threshold(cfg, "TIER_B_MAX_MINOR_FLAGS"):
        return "C"
    # Tier A used to demand zero minor flags, which one unchecked flood zone —
    # and those are routine — was enough to deny forever. A tier nothing can
    # reach ranks nothing.
    if (minor <= threshold(cfg, "TIER_A_MAX_MINOR_FLAGS")
            and ratio < threshold(cfg, "TIER_A_BID_TO_VALUE") and not is_homestead(cad)):
        return "A"
    if ratio < threshold(cfg, "MAX_BID_TO_VALUE"):
        return "B"
    return "C"


# --------------------------------------------------------------------------
# the pipeline for one property
# --------------------------------------------------------------------------

def screen(listing: dict, cad: dict | None, checks: list[dict], cfg: dict,
           today: date) -> dict:
    """Run every gate over one listing and return the full, auditable result."""
    checks = list(checks or [])
    terms = redemption_terms(listing, cad)

    rejections, flags = gate1_hard_disqualifiers(listing, cad, cfg, today)
    lien_rejections, lien_flags = gate2_liens(checks, cfg)
    rejections += lien_rejections
    flags += lien_flags
    physical_rejections, physical_flags = gate3_physical(listing, cad, checks, cfg)
    rejections += physical_rejections
    flags += physical_flags

    econ = gate4_economics(listing, cad, cfg, terms)
    tier = None if rejections else gate5_tier(flags, econ, cad, cfg)
    material, minor = count_flags(flags)

    ran = [c["check"] for c in checks if c.get("result") in (CLEAN, HIT)]
    unavailable = [c["check"] for c in checks if c.get("result") == UNAVAILABLE]
    unavailable += [name for name in LIEN_CHECKS if not find_check(checks, name)]

    return {
        "listing": listing,
        "cad": cad,
        "checks": checks,
        "flags": flags,
        "rejections": rejections,
        "economics": econ,
        "redemption": terms,
        "tier": tier,
        "status": "rejected" if rejections else "candidate",
        "material_flags": material,
        "minor_flags": minor,
        "checks_run": sorted(set(ran)),
        "checks_unavailable": sorted(set(unavailable)),
        "screened_at": now_iso(),
    }


def sort_key(result: dict, order: dict[str, int]) -> tuple:
    """County block order, then tier, then bid-to-value ascending."""
    listing = result["listing"]
    ratio = (result.get("economics") or {}).get("bid_to_value")
    return (
        order.get(listing.get("county"), 99),
        {"A": 0, "B": 1, "C": 2}.get(result.get("tier"), 3),
        ratio if ratio is not None else 9.99,
        listing.get("account") or "",
    )


# --------------------------------------------------------------------------
# §34.015 written statement
# --------------------------------------------------------------------------

def statement_status(cfg: dict, county: str, today: date) -> dict:
    """Is the bidder's written statement good for this county on sale day?

    Without an unexpired statement the officer may not deliver a deed, so a
    winning bid buys nothing. This is the one blocker that is entirely the
    user's to fix and entirely invisible until the deed does not arrive.
    """
    block = cfg.get("bidder_statement") or {}
    entry = (block.get("counties") or {}).get(county) or {}
    expires = entry.get("expires")
    warn_days = int(threshold(cfg, "STATEMENT_WARN_DAYS"))

    if not expires:
        return {
            "county": county, "expires": None, "days_left": None, "state": "missing",
            "message": (f"No §34.015 written statement on file for {county}. Without an "
                        f"unexpired statement from the {county} County Assessor-Collector "
                        f"the officer may not deliver a deed — a winning bid produces "
                        f"nothing. Form 50-307, notarized: {block.get('form_url', '')}"),
        }
    try:
        expiry = date.fromisoformat(str(expires))
    except ValueError:
        return {
            "county": county, "expires": str(expires), "days_left": None, "state": "unreadable",
            "message": f"§34.015 statement expiry {expires!r} for {county} is not a date.",
        }

    days_left = (expiry - today).days
    if days_left < 0:
        state, message = "expired", (
            f"§34.015 statement for {county} EXPIRED {abs(days_left)} days ago ({expires}). "
            f"No deed can be delivered on it. Reapply now — some counties need a minimum of "
            f"21 working days.")
    elif days_left <= warn_days:
        state, message = "expiring", (
            f"§34.015 statement for {county} expires in {days_left} days ({expires}). "
            f"Renewal can take a minimum of 21 working days in some counties — start now.")
    else:
        state, message = "current", (
            f"§34.015 statement for {county} is current, expires {expires} "
            f"({days_left} days).")
    return {"county": county, "expires": expires, "days_left": days_left,
            "state": state, "message": message}


def statement_report(cfg: dict, county_names: Iterable[str], today: date) -> list[dict]:
    return [statement_status(cfg, name, today) for name in county_names]


# --------------------------------------------------------------------------
# Output 1 — the Google Sheet
# --------------------------------------------------------------------------

HEADERS = [
    "County", "Sale Date", "Sale Type", "Cause No", "Account No", "Address",
    "Legal Description", "Property Type", "Opening Bid", "Value", "Value Source", "Bid/Value",
    "Redemption Period", "Redemption Payout", "Recommended Max Bid", "Tier",
    "Flags", "Checks Run", "Checks Unavailable", "CAD Link", "County Listing Link",
    "Last Verified",
]

COL_TIER = HEADERS.index("Tier")
COL_FLAGS = HEADERS.index("Flags")
COL_LEGAL = HEADERS.index("Legal Description")

# Rows 1-3 are the disclaimer, the run banner, and the statement line; the
# header lands on row 4 and that is what gets frozen.
HEADER_ROW = 4

TIER_LABELS = {"A": "A", "B": "B", "C": "C"}


def _money(value: Any) -> str:
    return "" if value is None else f"${value:,.0f}"


def flag_summary(flags: list[dict]) -> str:
    """Every flag, worst first, so the column reads as a warning not a list."""
    rank = {MATERIAL: 0, MINOR: 1, UNIVERSAL: 2}
    marks = {MATERIAL: "‼", MINOR: "▲", UNIVERSAL: "•"}
    ordered = sorted(flags, key=lambda f: (rank[f["severity"]], f["code"]))
    return " · ".join(f"{marks[f['severity']]} {f['code']}" for f in ordered)


def sheet_rows(results: list[dict], cfg: dict, today: date,
               sale_date: str, statements: list[dict]) -> tuple[list[list[Any]], dict]:
    """The whole `Tax Deeds` tab, rewritten from scratch every run.

    Stale listings are dangerous — a property pulled from the sale on Friday is
    still a live-looking row on Monday if the tab is appended to rather than
    replaced — so this returns the complete grid and the caller overwrites.
    """
    order = county_order(cfg)
    candidates = [r for r in results if r["status"] == "candidate"]
    candidates.sort(key=lambda r: sort_key(r, order))

    tier_counts = {t: sum(1 for r in candidates if r["tier"] == t) for t in ("A", "B", "C")}
    blockers = [s for s in statements if s["state"] in ("missing", "expired", "expiring")]

    banner = (f"TEXAS TAX DEED CANDIDATES · sale {sale_date} · screened {today.isoformat()} · "
              f"{len(candidates)} candidates from {len(results)} listings "
              f"(A {tier_counts['A']} / B {tier_counts['B']} / C {tier_counts['C']})")
    statement_line = (
        "§34.015 BIDDER STATEMENT: " +
        (" | ".join(f"{s['county']}: {s['state'].upper()}" for s in statements) or "none configured") +
        ("  ← fix before bidding; without an unexpired statement no deed can be delivered"
         if blockers else "")
    )

    rows: list[list[Any]] = [[DISCLAIMER], [banner], [statement_line], list(HEADERS)]
    spec: dict[str, Any] = {"county_rows": [], "data_rows": [], "note_rows": []}

    for name in [c["name"] for c in counties(cfg)]:
        block = [r for r in candidates if r["listing"].get("county") == name]
        listed = sum(1 for r in results if r["listing"].get("county") == name)
        statement = next((s for s in statements if s["county"] == name), None)
        header = (f"{name.upper()} COUNTY — {len(block)} candidate(s) of {listed} listed"
                  + (f" · §34.015 {statement['state'].upper()}" if statement else ""))
        spec["county_rows"].append(len(rows))
        rows.append([header])

        if not block:
            spec["note_rows"].append(len(rows))
            rows.append(["  no listing survived the gates for this county this run"])
            continue

        for result in block:
            spec["data_rows"].append((len(rows), result))
            rows.append(_sheet_row(result))

    rows.append([])
    spec["note_rows"].append(len(rows))
    rows.append(["Rewritten in full every run. A row absent today was pulled, sold, or "
                 "failed a gate — it is not carried forward."])
    return rows, spec


def _sheet_row(result: dict) -> list[Any]:
    listing, cad = result["listing"], result.get("cad") or {}
    econ = result.get("economics") or {}
    ratio = econ.get("bid_to_value")
    return [
        listing.get("county", ""),
        listing.get("sale_date", ""),
        listing.get("sale_type", ""),
        listing.get("cause_number", ""),
        listing.get("account", ""),
        listing.get("address") or cad.get("situs") or "",
        (listing.get("legal_description") or cad.get("legal_description") or "")[:220],
        listing.get("property_type") or cad.get("land_use_description") or "",
        _money(econ.get("opening_bid") if econ else listing.get("minimum_opening_bid")),
        _money(econ.get("cad_value") if econ else cad.get("appraised_value")),
        {"cad": "CAD roll", "adjudged": "county list", "none": ""}.get(
            econ.get("value_source", ""), ""),
        f"{ratio:.2f}" if ratio is not None else "",
        result["redemption"]["label"],
        _money(econ.get("redemption_payout")),
        _money(econ.get("max_bid")),
        TIER_LABELS.get(result.get("tier"), ""),
        flag_summary(result["flags"]),
        ", ".join(result["checks_run"]) or "none",
        ", ".join(result["checks_unavailable"]) or "none",
        cad.get("cad_url", ""),
        listing.get("listing_url", ""),
        result.get("screened_at", ""),
    ]


# --------------------------------------------------------------------------
# Output 2 — the due diligence packet
# --------------------------------------------------------------------------

CHECKLIST = [
    "Title search ordered (~$500 — cheap insurance)",
    "Drive-by completed, photos taken, occupancy observed",
    "County clerk records pulled by hand for the legal description",
    "Post-judgment and omitted-year taxes confirmed with the tax office",
    "Municipal code liens confirmed with the city",
    "§34.015 Written Statement current and unexpired",
    "Maximum bid written down before the auction",
    "Certified funds / deposit staged (Dallas: 5% ACH ≥5 business days prior)",
    "Exit strategy chosen: redemption yield / wholesale / rehab / hold",
]

RESULT_MARKS = {CLEAN: "clean", HIT: "**HIT**", UNAVAILABLE: "**unavailable — not screened**"}


def packet_tiers(cfg: dict) -> set[str]:
    """Which tiers get a due-diligence packet. `A,B` per the spec.

    A knob rather than a constant because of the Tier C consequence documented
    above: while the clerk portals stay unscreenable, every property carries a
    material flag and nothing is ever Tier A or B — so the default would write
    no packets at all. Set `PACKET_TIERS=A,B,C` to get one for every candidate
    and read the flag list, rather than lowering a severity to manufacture a
    tier the evidence does not support.
    """
    raw = threshold(cfg, "PACKET_TIERS")
    return {part.strip().upper() for part in str(raw).split(",") if part.strip()}


def packet_path(result: dict) -> Path:
    listing = result["listing"]
    account = normalize_account(listing.get("account")) or "unknown"
    county = re.sub(r"[^A-Za-z]", "", listing.get("county") or "unknown").lower()
    return PACKET_DIR / (listing.get("sale_date") or "undated") / f"{county}_{account}.md"


def packet_markdown(result: dict, cfg: dict, statement: dict) -> str:
    listing, cad = result["listing"], result.get("cad") or {}
    econ = result.get("economics") or {}
    terms = result["redemption"]
    county = listing.get("county", "")
    county_cfg = next((c for c in cfg.get("counties", []) if c["name"] == county), {})

    def line(label: str, value: Any) -> str:
        return f"| {label} | {value if value not in (None, '') else '—'} |"

    out: list[str] = [
        f"# {county} County · account {listing.get('account', '—')} · Tier {result.get('tier', '—')}",
        "",
        f"> **{DISCLAIMER}**",
        "",
        f"Screened {result.get('screened_at')}. Sale {listing.get('sale_date')} "
        f"({listing.get('sale_type')}). Rewritten each run — check the timestamp before acting.",
        "",
        "## Property",
        "",
        "| Field | Value |",
        "| --- | --- |",
        line("County", county),
        line("Sale date", listing.get("sale_date")),
        line("Sale type", listing.get("sale_type")),
        line("Sale venue", county_cfg.get("sale_location")),
        line("Cause number", listing.get("cause_number")),
        line("Account number", listing.get("account")),
        line("Address", listing.get("address") or cad.get("situs")),
        line("Legal description", listing.get("legal_description") or cad.get("legal_description")),
        line("Property type", listing.get("property_type") or cad.get("land_use_description")),
        line("Land use code", cad.get("land_use_code")),
        line("Subdivision", cad.get("subdivision")),
        line("Year built", cad.get("year_built")),
        line("Square feet", cad.get("sqft")),
        line("Lot size (sqft)", cad.get("lot_sqft")),
        line("Exemptions", ", ".join(cad.get("exemptions") or []) or "none on the CAD record"),
        line("CAD appraised value", _money(cad.get("appraised_value"))),
        line("  land", _money(cad.get("land_value"))),
        line("  improvement", _money(cad.get("improvement_value"))),
        line("CAD record", cad.get("cad_url")),
        line("County listing", listing.get("listing_url")),
        "",
        "## Redemption — Tex. Tax Code §34.21",
        "",
        f"- **Period: {terms['label']}** ({terms['days']} days). Basis: {terms['basis']}.",
        f"- Former owner redeems by paying the bid plus "
        f"{terms['penalty_year_one']:.0%} in year one"
        + (f", {terms['penalty_year_two']:.0%} in year two." if terms["penalty_year_two"]
           else "."),
        "- §34.21(h): the former owner may not occupy, possess, or receive rents during "
        "redemption. The purchaser may evict, subject to servicemember protections and "
        "bona fide leases.",
        "- **Redemption reconstitutes junior liens that the sale had otherwise eliminated. "
        "A redeemed property does not come back clean.**",
        f"- If a federal tax lien was of record, IRC §7425(d) / 28 U.S.C. §2410 give the IRS "
        f"{IRS_REDEMPTION_DAYS} days from the sale to redeem, or the state period, whichever "
        f"is longer. That right survives this sale.",
        "",
        "## Economics",
        "",
    ]

    if econ:
        out += [
            "| Figure | Value |",
            "| --- | --- |",
            line("Opening bid", _money(econ["opening_bid"])),
            line("Value used", _money(econ["cad_value"])),
            line("Value source", {"cad": "appraisal district roll",
                                  "adjudged": "the **value published on the county sale "
                                              "list** — usually the adjudged value the court "
                                              "set in the tax suit. Confirm what basis it "
                                              "uses and how old it is before you rely on it"}
                 .get(econ.get("value_source"), econ.get("value_source"))),
            line("Bid / value", f"{econ['bid_to_value']:.2f}"),
            line("Recommended max bid", _money(econ["max_bid"])),
            line("Quiet title budget", _money(econ["quiet_title_budget"])),
            line(f"Holding costs ({econ['holding_months']:g} months)",
                 _money(econ["holding_costs"])),
            line("Post-judgment taxes (estimate)", _money(econ["post_judgment_taxes_estimate"])),
            line("**Estimated total cost**", f"**{_money(econ['est_total_cost'])}**"),
            "",
            "**Outcome 1 — redeemed.** Both outcomes are acceptable; this is the one that "
            "pays a coupon.",
            "",
            f"- Former owner pays **{_money(econ['redemption_payout'])}** "
            f"({terms['penalty_year_one']:.0%} over the bid), plus reimbursement of the deed "
            f"recording fee and the taxes, penalties, interest and costs you paid "
            f"(§34.21(b)).",
            f"- Capital at risk **{_money(econ['redemption_capital'])}** — the bid plus "
            f"{_money(econ['redemption_carry'])} of carry the statute does not repay "
            f"(insurance and utilities over {econ['holding_months']:g} months). No quiet "
            f"title: you do not quiet title a property that is still redeemable. Taxes are "
            f"excluded from both sides because they are reimbursed.",
            f"- Net **{_money(econ['redemption_net_profit'])}**, "
            f"**{econ['redemption_return_pct']:.1f}%** over ≤{terms['days']} days "
            f"(~{econ['redemption_annualized_pct']:.1f}% annualized).",
            "- Still conservative: §34.21(a) takes the premium on the *aggregate total* — the "
            "bid plus the recording fee plus the taxes reimbursed — where this takes it on "
            "the bid alone.",
            "",
            "**Outcome 2 — not redeemed. You own it.**",
            "",
            f"- Equity vs CAD value net of estimated costs: "
            f"**{_money(econ['ownership_equity'])}** "
            f"({econ['ownership_equity_multiple']:.2f}× cost).",
            "- CAD value is an appraisal district number, not a market appraisal or a broker "
            "opinion. Get a real one before you count this.",
        ]
    else:
        out.append("Not priceable — no opening bid or no CAD value. See rejections below.")

    out += ["", "## Checks that actually ran", "",
            "A blank finding means the check found nothing, never that the property is clear.",
            "",
            "| Check | Result | Source | Detail | Checked at |", "| --- | --- | --- | --- | --- |"]
    for check in sorted(result["checks"], key=lambda c: c["check"]):
        out.append(f"| {CHECK_LABELS.get(check['check'], check['check'])} "
                   f"| {RESULT_MARKS.get(check['result'], check['result'])} "
                   f"| {check.get('source') or '—'} "
                   f"| {(check.get('detail') or '—')[:160]} "
                   f"| {check.get('checked_at')} |")

    missing = [n for n in LIEN_CHECKS if not find_check(result["checks"], n)]
    if missing:
        out += ["", f"**No adapter ran at all for: {', '.join(missing)}.** "
                    f"Treated as unavailable, never as clean."]

    out += ["", "## Flags", ""]
    if result["flags"]:
        for f in sorted(result["flags"], key=lambda f: {MATERIAL: 0, MINOR: 1, UNIVERSAL: 2}[f["severity"]]):
            out.append(f"- **{f['severity']}** · `{f['code']}` — {f['detail']}")
    else:
        out.append("- none recorded by the checks that ran")

    if result["rejections"]:
        out += ["", "## Rejections", ""]
        for r in result["rejections"]:
            out.append(f"- **Gate {r['gate']}** · `{r['code']}` — {r['detail']}")

    out += ["", "## Bidder eligibility — Tex. Tax Code §34.011 and §34.015", "",
            f"- {statement['message']}",
            "- The officer may not deliver a deed unless you exhibit an unexpired written "
            "statement from the county assessor-collector showing no delinquent ad valorem "
            "taxes owed to that county or to any school district or municipality in it. "
            "Form 50-307, notarized: https://comptroller.texas.gov/forms/50-307.pdf",
            "- Processing can take a minimum of 21 working days in some counties.",
            "- **An individual may not bid or purchase in the name of another individual. "
            "Knowing violation is a Class B misdemeanor.**"]
    if county_cfg.get("registration_note"):
        out.append(f"- Registration: {county_cfg['registration_note']}")
    if county_cfg.get("written_statement_note"):
        out.append(f"- Written statement: {county_cfg['written_statement_note']}")

    out += ["", "## Manual checklist", "",
            "None of this is automatable, and the tool is not a substitute for any of it.", ""]
    out += [f"- [ ] {item}" for item in CHECKLIST]
    out += ["", "---", "", f"Generated by `scripts/tax_deed_screen.py` at {now_iso()}. "
            f"Candidate only — not a title search, not title certification, not legal advice."]
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# snapshot
# --------------------------------------------------------------------------

def snapshot(results: list[dict], cfg: dict, today: date, sale_date: str,
             statements: list[dict], source_report: list[dict]) -> dict:
    counted = {t: sum(1 for r in results if r.get("tier") == t) for t in ("A", "B", "C")}
    return {
        "disclaimer": DISCLAIMER,
        "screened_at": now_iso(),
        "screened_on": today.isoformat(),
        "sale_date": sale_date,
        "counties": [c["name"] for c in counties(cfg)],
        "thresholds": {k: threshold(cfg, k) for k in DEFAULT_THRESHOLDS},
        "bidder_statement": statements,
        "sources": source_report,
        "totals": {
            "listings": len(results),
            "candidates": sum(1 for r in results if r["status"] == "candidate"),
            "rejected": sum(1 for r in results if r["status"] == "rejected"),
            "tier_a": counted["A"], "tier_b": counted["B"], "tier_c": counted["C"],
        },
        "results": results,
    }


def snapshot_path(today: date) -> Path:
    return SNAPSHOT_DIR / f"{today.isoformat()}.json"


# --------------------------------------------------------------------------
# CLI — inspection only; the screening run is tax_deed_screen.py
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["thresholds", "statement", "disclaimer", "sale-date"])
    ap.add_argument("--date", help="as-of date, YYYY-MM-DD; defaults to today in ET")
    args = ap.parse_args(argv)

    cfg = load_config()
    today = date.fromisoformat(args.date) if args.date else datetime.now(ET).date()

    if args.command == "thresholds":
        for name in DEFAULT_THRESHOLDS:
            source = ("env" if name in os.environ else
                      "config" if name in (cfg.get("thresholds") or {}) else "default")
            print(f"{name:28} {threshold(cfg, name)!r:>10}  ({source})")
    elif args.command == "statement":
        for status in statement_report(cfg, [c["name"] for c in counties(cfg)], today):
            mark = {"current": "OK", "expiring": "WARN", "expired": "BLOCKED",
                    "missing": "BLOCKED", "unreadable": "BLOCKED"}[status["state"]]
            print(f"[{mark}] {status['message']}")
    elif args.command == "sale-date":
        print(next_sale_date(today).isoformat())
    else:
        print(DISCLAIMER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
