#!/usr/bin/env python3
"""The place table every MAX_MILES_FROM_BASE distance is measured against.

    python scripts/tax_deed_places.py distance Rowlett --county Dallas
    python scripts/tax_deed_places.py distance "North Richland H" --county Tarrant
    python scripts/tax_deed_places.py build path/to/rg_cities1000.csv

`config/tax_deed_places.json` is every Texas row of GeoNames cities1000 — each
populated place of 1,000 people or more — as bundled in the reverse_geocoder
package on PyPI. It is vendored rather than fetched per run so that a distance
is the same number every run and the radius can be tested offline; a
gazetteer that moves under the screener moves the line with it.

Rebuild it here rather than by hand, from the same file:

    pip download reverse_geocoder==1.5.1 --no-deps -d /tmp/rg
    tar -xzf /tmp/rg/reverse_geocoder-1.5.1.tar.gz -C /tmp/rg
    python scripts/tax_deed_places.py build \\
        /tmp/rg/reverse_geocoder-1.5.1/reverse_geocoder/rg_cities1000.csv

GeoNames data is CC BY 4.0 (https://www.geonames.org/); the attribution travels
in the file. A town under 1,000 people is not in it — Westworth Village, Rio
Vista, Cross Timber, Maypearl and a dozen more around the four counties — and
for those the screener asks the Census geocoder for the parcel instead. A row
neither can place is flagged `distance_unknown`, never rejected.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import tax_deeds as td  # noqa: E402

SOURCE = "GeoNames cities1000 via reverse_geocoder 1.5.1 (PyPI), rg_cities1000.csv"
LICENSE = "CC BY 4.0 — GeoNames, https://www.geonames.org/"
NOTE = ("Texas places and the point each one is measured from. Used to measure how far a "
        "listing's city is from the home base (MAX_MILES_FROM_BASE). Every Texas row of "
        "GeoNames cities1000 — every populated place of 1,000 or more — as bundled in the "
        "reverse_geocoder 1.5.1 package on PyPI (its data file rg_cities1000.csv). GeoNames "
        "data is CC BY 4.0: https://www.geonames.org/. A place under 1,000 people is not "
        "here; the screener asks the Census geocoder for that parcel instead, and a row "
        "neither can place is flagged distance_unknown, never rejected. Rebuild with "
        "scripts/tax_deed_places.py rather than by hand.")


def read_rows(path: Path) -> list[list]:
    """Texas rows of a reverse_geocoder-format CSV: lat,lon,name,admin1,admin2,cc."""
    with path.open(newline="", encoding="utf-8") as handle:
        rows = [r for r in csv.DictReader(handle)
                if r.get("cc") == "US" and r.get("admin1") == "Texas"]
    if not rows:
        raise SystemExit(f"{path} has no Texas rows — is it the reverse_geocoder "
                         f"rg_cities1000.csv (columns lat,lon,name,admin1,admin2,cc)?")
    return sorted(([r["name"], round(float(r["lat"]), 5), round(float(r["lon"]), 5),
                    r["admin2"]] for r in rows), key=lambda p: (p[0].casefold(), p[3]))


def write_table(places: list[list], path: Path, retrieved: date) -> None:
    """One place per line, so a rebuild diffs as the places that changed."""
    head = {"_": NOTE, "source": SOURCE, "license": LICENSE,
            "retrieved": retrieved.isoformat(), "fields": ["name", "lat", "lon", "county"]}
    lines = ["{"] + [f"  {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)},"
                     for k, v in head.items()]
    lines.append('  "places": [')
    lines.append(",\n".join("    " + json.dumps(p, ensure_ascii=False) for p in places))
    lines += ["  ]", "}"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)
    build = sub.add_parser("build", help="regenerate config/tax_deed_places.json")
    build.add_argument("csv", type=Path)
    dist = sub.add_parser("distance", help="miles from the home base to a city")
    dist.add_argument("city")
    dist.add_argument("--county", help="the listing's county, for the seat sanity check")
    args = ap.parse_args(argv)

    if args.command == "build":
        places = read_rows(args.csv)
        write_table(places, td.PLACES_PATH, date.today())
        td.place_table.cache_clear()
        print(f"{len(places)} Texas places -> {td.PLACES_PATH.relative_to(REPO)}")
        return 0

    cfg = td.load_config()
    base = td.home_base(cfg)
    if base is None:
        print("MAX_MILES_FROM_BASE is 0 — no radius configured.")
        return 0
    where = td.locate({"city": args.city, "county": args.county or ""}, cfg)
    radius = float(td.threshold(cfg, "MAX_MILES_FROM_BASE"))
    if where["miles"] is None:
        print(f"{args.city}: not measured — {where['detail']}")
        return 1
    verdict = "outside" if where["miles"] > radius else "inside"
    print(f"{where['place']}: {where['miles']:.1f} mi from {base[0]} "
          f"({where['basis']}) — {verdict} the {radius:g}-mile radius")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
