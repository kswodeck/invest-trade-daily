#!/usr/bin/env python3
"""Keyless-first market data CLI for the daily research phase.

Every subcommand prints a JSON object to stdout and exits 0 even when a source
fails, so a dead upstream never kills a research run. Check the ``ok`` field on
each result before trusting the payload.

    python scripts/market_data.py quote NVDA SPY
    python scripts/market_data.py crypto bitcoin ethereum
    python scripts/market_data.py history NVDA --days 120
    python scripts/market_data.py macro
    python scripts/market_data.py events "CPI"
    python scripts/market_data.py filings NVDA
    python scripts/market_data.py earnings --days 14

Optional environment variables unlock better sources; all are safe to omit:
FINNHUB_API_KEY, ALPHAVANTAGE_API_KEY, FRED_API_KEY, SEC_USER_AGENT.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import sys
from datetime import date, datetime, timedelta, timezone
from typing import Any, Iterable

import requests

TIMEOUT = 20
ET = timezone(timedelta(hours=-5))  # display only; exact offset resolved by caller

FINNHUB_KEY = os.environ.get("FINNHUB_API_KEY", "").strip()
ALPHAVANTAGE_KEY = os.environ.get("ALPHAVANTAGE_API_KEY", "").strip()
FRED_KEY = os.environ.get("FRED_API_KEY", "").strip()
SEC_UA = os.environ.get("SEC_USER_AGENT", "").strip()

_session = requests.Session()
_session.headers.update({"User-Agent": "invest-trade-daily/1.0 (+github actions)"})


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def _get(url: str, *, params: dict | None = None, headers: dict | None = None) -> requests.Response:
    resp = _session.get(url, params=params, headers=headers, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp


def _fail(source: str, exc: Exception) -> dict[str, Any]:
    return {"ok": False, "source": source, "error": f"{type(exc).__name__}: {exc}"}


def _stooq_symbol(symbol: str) -> str:
    s = symbol.strip().lower()
    if s.startswith("^") or "." in s:
        return s
    return f"{s}.us"


def _num(value: Any) -> float | None:
    try:
        f = float(value)
    except (TypeError, ValueError):
        return None
    return None if f != f else f  # drop NaN


# --------------------------------------------------------------------------
# quotes
# --------------------------------------------------------------------------

def quote_finnhub(symbol: str) -> dict[str, Any]:
    if not FINNHUB_KEY:
        return {"ok": False, "source": "finnhub", "error": "no api key"}
    try:
        data = _get(
            "https://finnhub.io/api/v1/quote",
            params={"symbol": symbol.upper(), "token": FINNHUB_KEY},
        ).json()
        price = _num(data.get("c"))
        if not price:
            raise ValueError(f"no price in response: {data}")
        return {
            "ok": True,
            "source": "finnhub",
            "symbol": symbol.upper(),
            "price": price,
            "open": _num(data.get("o")),
            "high": _num(data.get("h")),
            "low": _num(data.get("l")),
            "prev_close": _num(data.get("pc")),
            "change_pct": _num(data.get("dp")),
            "asof": datetime.fromtimestamp(data["t"], tz=timezone.utc).isoformat()
            if data.get("t")
            else None,
        }
    except Exception as exc:  # noqa: BLE001 - source failures are data, not crashes
        return _fail("finnhub", exc)


def quote_stooq(symbol: str) -> dict[str, Any]:
    try:
        text = _get(
            "https://stooq.com/q/l/",
            params={"s": _stooq_symbol(symbol), "f": "sd2t2ohlcv", "h": "", "e": "csv"},
        ).text
        row = next(csv.DictReader(io.StringIO(text)))
        close = _num(row.get("Close"))
        if close is None:
            raise ValueError(f"stooq returned no close for {symbol}: {row}")
        open_ = _num(row.get("Open"))
        return {
            "ok": True,
            "source": "stooq",
            "symbol": symbol.upper(),
            "price": close,
            "open": open_,
            "high": _num(row.get("High")),
            "low": _num(row.get("Low")),
            "volume": _num(row.get("Volume")),
            "change_pct": round((close - open_) / open_ * 100, 2) if open_ else None,
            "asof": f"{row.get('Date')} {row.get('Time')}".strip(),
            "note": "end-of-day or delayed; not a real-time quote",
        }
    except Exception as exc:  # noqa: BLE001
        return _fail("stooq", exc)


def quote_alphavantage(symbol: str) -> dict[str, Any]:
    if not ALPHAVANTAGE_KEY:
        return {"ok": False, "source": "alphavantage", "error": "no api key"}
    try:
        payload = _get(
            "https://www.alphavantage.co/query",
            params={"function": "GLOBAL_QUOTE", "symbol": symbol.upper(), "apikey": ALPHAVANTAGE_KEY},
        ).json()
        data = payload.get("Global Quote") or {}
        price = _num(data.get("05. price"))
        if not price:
            raise ValueError(f"no price (rate limited?): {payload}")
        return {
            "ok": True,
            "source": "alphavantage",
            "symbol": symbol.upper(),
            "price": price,
            "open": _num(data.get("02. open")),
            "high": _num(data.get("03. high")),
            "low": _num(data.get("04. low")),
            "prev_close": _num(data.get("08. previous close")),
            "change_pct": _num((data.get("10. change percent") or "").rstrip("%")),
            "asof": data.get("07. latest trading day"),
        }
    except Exception as exc:  # noqa: BLE001
        return _fail("alphavantage", exc)


def quote(symbol: str) -> dict[str, Any]:
    """First source that returns a usable price wins."""
    attempts = []
    for fn in (quote_finnhub, quote_stooq, quote_alphavantage):
        result = fn(symbol)
        if result.get("ok"):
            result["fallbacks_tried"] = [a["source"] for a in attempts]
            return result
        attempts.append(result)
    return {"ok": False, "symbol": symbol.upper(), "attempts": attempts}


def crypto(coin_ids: Iterable[str]) -> dict[str, Any]:
    ids = [c.strip().lower() for c in coin_ids if c.strip()]
    try:
        data = _get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={
                "ids": ",".join(ids),
                "vs_currencies": "usd",
                "include_24hr_change": "true",
                "include_24hr_vol": "true",
                "include_market_cap": "true",
            },
        ).json()
        return {
            "ok": True,
            "source": "coingecko",
            "prices": {
                coin: {
                    "price": _num(v.get("usd")),
                    "change_24h_pct": round(c, 2) if (c := _num(v.get("usd_24h_change"))) else None,
                    "volume_24h": _num(v.get("usd_24h_vol")),
                    "market_cap": _num(v.get("usd_market_cap")),
                }
                for coin, v in data.items()
            },
            "missing": [c for c in ids if c not in data],
            "note": "coin ids are CoinGecko slugs (bitcoin, ethereum, solana), not tickers",
        }
    except Exception as exc:  # noqa: BLE001
        return _fail("coingecko", exc)


# --------------------------------------------------------------------------
# history + derived levels
# --------------------------------------------------------------------------

def history(symbol: str, days: int = 120) -> dict[str, Any]:
    """Daily OHLCV plus the levels needed to set entries, targets, and stops."""
    try:
        text = _get(
            "https://stooq.com/q/d/l/", params={"s": _stooq_symbol(symbol), "i": "d"}
        ).text
        rows = [r for r in csv.DictReader(io.StringIO(text)) if r.get("Close")]
        if not rows:
            raise ValueError(f"stooq returned no history for {symbol}")
        rows = rows[-days:]
        closes = [float(r["Close"]) for r in rows]
        highs = [float(r["High"]) for r in rows]
        lows = [float(r["Low"]) for r in rows]

        trs = [
            max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1]))
            for i in range(1, len(rows))
        ]
        atr14 = round(sum(trs[-14:]) / len(trs[-14:]), 4) if trs else None
        last = closes[-1]

        def sma(n: int) -> float | None:
            return round(sum(closes[-n:]) / n, 4) if len(closes) >= n else None

        return {
            "ok": True,
            "source": "stooq",
            "symbol": symbol.upper(),
            "bars": len(rows),
            "start": rows[0]["Date"],
            "end": rows[-1]["Date"],
            "last_close": last,
            "atr14": atr14,
            "atr14_pct": round(atr14 / last * 100, 2) if atr14 and last else None,
            "sma20": sma(20),
            "sma50": sma(50),
            "sma200": sma(200),
            "range_high": round(max(highs), 4),
            "range_low": round(min(lows), 4),
            "pct_off_high": round((last - max(highs)) / max(highs) * 100, 2),
            "pct_off_low": round((last - min(lows)) / min(lows) * 100, 2),
            "recent": [
                {
                    "date": r["Date"],
                    "o": float(r["Open"]),
                    "h": float(r["High"]),
                    "l": float(r["Low"]),
                    "c": float(r["Close"]),
                    "v": _num(r.get("Volume")),
                }
                for r in rows[-20:]
            ],
        }
    except Exception as exc:  # noqa: BLE001
        return _fail("stooq", exc)


# --------------------------------------------------------------------------
# macro
# --------------------------------------------------------------------------

FRED_SERIES = {
    "us10y": "DGS10",
    "us2y": "DGS2",
    "fed_funds": "DFF",
    "yield_curve_10y2y": "T10Y2Y",
    "unemployment": "UNRATE",
    "cpi_yoy": "CPIAUCSL",
}

MACRO_TICKERS = {
    "spx": "^spx",
    "ndx": "^ndq",
    "dow": "^dji",
    "russell2000": "^rut",
    "vix": "^vix",
    "gold_etf": "GLD",
    "oil_etf": "USO",
    "dollar_etf": "UUP",
    "bonds_20y": "TLT",
}


def fred_series(series_id: str) -> dict[str, Any]:
    if not FRED_KEY:
        return {"ok": False, "source": "fred", "error": "no api key"}
    try:
        data = _get(
            "https://api.stlouisfed.org/fred/series/observations",
            params={
                "series_id": series_id,
                "api_key": FRED_KEY,
                "file_type": "json",
                "sort_order": "desc",
                "limit": 2,
            },
        ).json()
        obs = [o for o in data.get("observations", []) if o.get("value") not in (".", None)]
        if not obs:
            raise ValueError("no observations")
        return {
            "ok": True,
            "source": "fred",
            "series": series_id,
            "value": _num(obs[0]["value"]),
            "date": obs[0]["date"],
            "prev": _num(obs[1]["value"]) if len(obs) > 1 else None,
        }
    except Exception as exc:  # noqa: BLE001
        return _fail("fred", exc)


def macro() -> dict[str, Any]:
    return {
        "ok": True,
        "asof_utc": datetime.now(timezone.utc).isoformat(),
        "markets": {name: quote(sym) for name, sym in MACRO_TICKERS.items()},
        "crypto": crypto(["bitcoin", "ethereum", "solana"]),
        "fred": {name: fred_series(sid) for name, sid in FRED_SERIES.items()},
        "note": "index quotes via stooq are delayed; use for context, not entry levels",
    }


# --------------------------------------------------------------------------
# event contracts (Kalshi — backs Robinhood Prediction Markets)
# --------------------------------------------------------------------------

def events(search: str = "", limit: int = 40) -> dict[str, Any]:
    try:
        data = _get(
            "https://api.elections.kalshi.com/trade-api/v2/markets",
            params={"status": "open", "limit": min(limit * 5, 200)},
        ).json()
        markets = data.get("markets", [])
        needle = search.lower().strip()
        if needle:
            markets = [
                m
                for m in markets
                if needle in (m.get("title", "") + m.get("ticker", "") + m.get("subtitle", "")).lower()
            ]
        return {
            "ok": True,
            "source": "kalshi",
            "count": len(markets[:limit]),
            "markets": [
                {
                    "ticker": m.get("ticker"),
                    "title": m.get("title"),
                    "subtitle": m.get("subtitle"),
                    "yes_bid": m.get("yes_bid"),
                    "yes_ask": m.get("yes_ask"),
                    "no_bid": m.get("no_bid"),
                    "no_ask": m.get("no_ask"),
                    "last_price": m.get("last_price"),
                    "volume": m.get("volume"),
                    "open_interest": m.get("open_interest"),
                    "close_time": m.get("close_time"),
                }
                for m in markets[:limit]
            ],
            "note": (
                "prices are cents = implied probability. Kalshi lists markets Robinhood "
                "does not carry; verify availability in Robinhood before recommending."
            ),
        }
    except Exception as exc:  # noqa: BLE001
        return _fail("kalshi", exc)


# --------------------------------------------------------------------------
# SEC filings
# --------------------------------------------------------------------------

_cik_cache: dict[str, str] | None = None


def _cik_map() -> dict[str, str]:
    global _cik_cache
    if _cik_cache is None:
        data = _get(
            "https://www.sec.gov/files/company_tickers.json",
            headers={"User-Agent": SEC_UA or "invest-trade-daily research@example.com"},
        ).json()
        _cik_cache = {v["ticker"].upper(): str(v["cik_str"]).zfill(10) for v in data.values()}
    return _cik_cache


def filings(symbol: str, limit: int = 15) -> dict[str, Any]:
    if not SEC_UA:
        return {
            "ok": False,
            "source": "sec",
            "error": "SEC_USER_AGENT not set; SEC blocks requests without a contact UA",
        }
    try:
        cik = _cik_map().get(symbol.upper())
        if not cik:
            return {"ok": False, "source": "sec", "error": f"no CIK for {symbol}"}
        data = _get(
            f"https://data.sec.gov/submissions/CIK{cik}.json",
            headers={"User-Agent": SEC_UA},
        ).json()
        recent = data.get("filings", {}).get("recent", {})
        out = []
        for i in range(min(limit, len(recent.get("form", [])))):
            accession = recent["accessionNumber"][i].replace("-", "")
            out.append(
                {
                    "form": recent["form"][i],
                    "filed": recent["filingDate"][i],
                    "report_date": recent.get("reportDate", [None] * (i + 1))[i],
                    "description": recent.get("primaryDocDescription", [None] * (i + 1))[i],
                    "url": (
                        f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
                        f"{accession}/{recent['primaryDocument'][i]}"
                    ),
                }
            )
        return {
            "ok": True,
            "source": "sec",
            "symbol": symbol.upper(),
            "company": data.get("name"),
            "cik": cik,
            "filings": out,
        }
    except Exception as exc:  # noqa: BLE001
        return _fail("sec", exc)


# --------------------------------------------------------------------------
# earnings calendar
# --------------------------------------------------------------------------

def earnings(days: int = 14) -> dict[str, Any]:
    if not FINNHUB_KEY:
        return {
            "ok": False,
            "source": "finnhub",
            "error": "no api key; fall back to web search for the earnings calendar",
        }
    try:
        today = date.today()
        data = _get(
            "https://finnhub.io/api/v1/calendar/earnings",
            params={
                "from": today.isoformat(),
                "to": (today + timedelta(days=days)).isoformat(),
                "token": FINNHUB_KEY,
            },
        ).json()
        rows = data.get("earningsCalendar", [])
        return {
            "ok": True,
            "source": "finnhub",
            "count": len(rows),
            "earnings": [
                {
                    "symbol": r.get("symbol"),
                    "date": r.get("date"),
                    "hour": r.get("hour"),
                    "eps_estimate": r.get("epsEstimate"),
                    "revenue_estimate": r.get("revenueEstimate"),
                }
                for r in rows
            ],
        }
    except Exception as exc:  # noqa: BLE001
        return _fail("finnhub", exc)


# --------------------------------------------------------------------------
# cli
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("quote", help="equity/ETF quotes")
    p.add_argument("symbols", nargs="+")

    p = sub.add_parser("crypto", help="crypto prices by CoinGecko id")
    p.add_argument("coins", nargs="+")

    p = sub.add_parser("history", help="daily OHLCV plus ATR/SMA/range levels")
    p.add_argument("symbol")
    p.add_argument("--days", type=int, default=120)

    sub.add_parser("macro", help="indices, rates, VIX, dollar, FRED series")

    p = sub.add_parser("events", help="Kalshi event contracts")
    p.add_argument("search", nargs="?", default="")
    p.add_argument("--limit", type=int, default=40)

    p = sub.add_parser("filings", help="recent SEC filings")
    p.add_argument("symbol")
    p.add_argument("--limit", type=int, default=15)

    p = sub.add_parser("earnings", help="upcoming earnings calendar")
    p.add_argument("--days", type=int, default=14)

    args = parser.parse_args(argv)

    if args.cmd == "quote":
        result = {"quotes": {s.upper(): quote(s) for s in args.symbols}}
    elif args.cmd == "crypto":
        result = crypto(args.coins)
    elif args.cmd == "history":
        result = history(args.symbol, args.days)
    elif args.cmd == "macro":
        result = macro()
    elif args.cmd == "events":
        result = events(args.search, args.limit)
    elif args.cmd == "filings":
        result = filings(args.symbol, args.limit)
    elif args.cmd == "earnings":
        result = earnings(args.days)
    else:  # pragma: no cover - argparse enforces the choices
        parser.error(f"unknown command {args.cmd}")

    json.dump(result, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
