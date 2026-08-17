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
    python scripts/market_data.py insiders NVDA

Optional environment variables unlock better sources; all are safe to omit:
FINNHUB_API_KEY, TWELVEDATA_API_KEY, ALPHAVANTAGE_API_KEY, FRED_API_KEY, SEC_USER_AGENT.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import sys
from datetime import date, datetime, timedelta, timezone
from typing import Any, Iterable

import requests

TIMEOUT = 20
ET = timezone(timedelta(hours=-5))  # display only; exact offset resolved by caller

FINNHUB_KEY = os.environ.get("FINNHUB_API_KEY", "").strip()
ALPHAVANTAGE_KEY = os.environ.get("ALPHAVANTAGE_API_KEY", "").strip()
TWELVEDATA_KEY = os.environ.get("TWELVEDATA_API_KEY", "").strip()
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


# Robinhood futures codes look like /MESU6 (root + month letter + year digit).
# Yahoo wants the continuous contract, MES=F. Strip the month code, and if the
# micro root is not recognised fall back to the full-size root, which tracks the
# same underlying at the same quoted level.
_MONTH_CODE = re.compile(r"^([A-Z0-9]+?)([FGHJKMNQUVXZ]\d{1,2})$")

_YAHOO_ALIASES = {
    "SPX": "^GSPC", "NDX": "^NDX", "DJI": "^DJI", "RUT": "^RUT", "VIX": "^VIX",
    "DXY": "DX-Y.NYB", "WTI": "CL=F", "GOLD": "GC=F",
}


def _yahoo_symbol(symbol: str) -> str:
    s = symbol.strip().upper()
    if s in _YAHOO_ALIASES:
        return _YAHOO_ALIASES[s]
    if s.startswith("^") or s.endswith("=F") or "-" in s or "." in s:
        return s
    if s.startswith("/"):  # futures
        root = s[1:]
        m = _MONTH_CODE.match(root)
        if m:
            root = m.group(1)
        return f"{root}=F"
    return s


def _futures_fallback(symbol: str) -> str | None:
    """MES=F -> ES=F, for micro roots Yahoo does not carry."""
    s = _yahoo_symbol(symbol)
    if s.endswith("=F") and len(s) > 3 and s[0] == "M":
        return f"{s[1:]}"
    return None


# --------------------------------------------------------------------------
# quotes
# --------------------------------------------------------------------------

# Yahoo covers equities, ETFs, indices, futures, and crypto from one response
# shape, but rate limits GitHub Actions runners with 429 often enough that it
# sits behind Finnhub for quotes and Nasdaq for history. Kept because it is
# keyless and does sometimes succeed. These headers are reused for Nasdaq,
# which 403s without a browser-ish User-Agent.
YAHOO_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept": "application/json",
}


YAHOO_HOSTS = ("query1.finance.yahoo.com", "query2.finance.yahoo.com")


def _yahoo_chart(symbol: str, rng: str, interval: str) -> dict[str, Any]:
    """Fetch a chart, trying both Yahoo hosts.

    query1 and query2 sit behind different edge configurations and do not rate
    limit or block identically, so a 401/403/429 from one is often served fine
    by the other.
    """
    errors = []
    for host in YAHOO_HOSTS:
        try:
            payload = _get(
                f"https://{host}/v8/finance/chart/{_yahoo_symbol(symbol)}",
                params={"range": rng, "interval": interval, "includePrePost": "false"},
                headers=YAHOO_HEADERS,
            ).json()
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{host}: {type(exc).__name__}: {exc}")
            continue
        err = (payload.get("chart") or {}).get("error")
        if err:
            errors.append(f"{host}: {err}")
            continue
        results = (payload.get("chart") or {}).get("result") or []
        if not results:
            errors.append(f"{host}: empty result")
            continue
        return results[0]
    raise ValueError(f"yahoo failed for {symbol} — {' | '.join(errors)}")


def quote_yahoo(symbol: str) -> dict[str, Any]:
    for candidate in filter(None, [symbol, _futures_fallback(symbol)]):
        try:
            result = _yahoo_chart(candidate, "1d", "1d")
            meta = result.get("meta", {})
            price = _num(meta.get("regularMarketPrice"))
            if price is None:  # fall back to the last non-null close
                closes = [
                    c for c in
                    (result.get("indicators", {}).get("quote") or [{}])[0].get("close", [])
                    if c is not None
                ]
                price = _num(closes[-1]) if closes else None
            if price is None:
                raise ValueError(f"no price in yahoo meta for {candidate}")
            prev = _num(meta.get("previousClose")) or _num(meta.get("chartPreviousClose"))
            ts = meta.get("regularMarketTime")
            return {
                "ok": True,
                "source": "yahoo",
                "symbol": symbol.upper(),
                "resolved_symbol": _yahoo_symbol(candidate),
                "price": price,
                "high": _num(meta.get("regularMarketDayHigh")),
                "low": _num(meta.get("regularMarketDayLow")),
                "prev_close": prev,
                "volume": _num(meta.get("regularMarketVolume")),
                "change_pct": round((price - prev) / prev * 100, 2) if prev else None,
                "currency": meta.get("currency"),
                "instrument_type": meta.get("instrumentType"),
                "asof": datetime.fromtimestamp(ts, tz=timezone.utc).isoformat() if ts else None,
            }
        except Exception as exc:  # noqa: BLE001
            last = _fail("yahoo", exc)
    return last


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
    """Fallback only. Stooq 404s from datacenter IPs, so this rarely fires in CI."""
    try:
        # `h` is a bare flag requesting the header row; sending it as `h=` has
        # been observed to 404, so the query string is built by hand.
        text = _get(
            f"https://stooq.com/q/l/?s={_stooq_symbol(symbol)}&f=sd2t2ohlcv&h&e=csv"
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
    for fn in (quote_finnhub, quote_yahoo, quote_stooq, quote_alphavantage):
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

def _yahoo_range(days: int) -> str:
    for limit, label in ((5, "5d"), (30, "1mo"), (90, "3mo"), (180, "6mo"), (365, "1y")):
        if days <= limit:
            return label
    return "2y"


def _bars_yahoo(symbol: str, days: int) -> list[dict[str, Any]]:
    result = _yahoo_chart(symbol, _yahoo_range(days), "1d")
    stamps = result.get("timestamp") or []
    q = (result.get("indicators", {}).get("quote") or [{}])[0]
    rows = []
    for i, ts in enumerate(stamps):
        close = _num((q.get("close") or [None] * len(stamps))[i])
        if close is None:  # Yahoo pads holidays and halts with nulls
            continue
        rows.append({
            "Date": datetime.fromtimestamp(ts, tz=timezone.utc).date().isoformat(),
            "Open": _num((q.get("open") or [None] * len(stamps))[i]) or close,
            "High": _num((q.get("high") or [None] * len(stamps))[i]) or close,
            "Low": _num((q.get("low") or [None] * len(stamps))[i]) or close,
            "Close": close,
            "Volume": _num((q.get("volume") or [None] * len(stamps))[i]),
        })
    if not rows:
        raise ValueError(f"yahoo returned no usable bars for {symbol}")
    return rows


def _bars_stooq(symbol: str) -> list[dict[str, Any]]:
    text = _get("https://stooq.com/q/d/l/", params={"s": _stooq_symbol(symbol), "i": "d"}).text
    rows = [r for r in csv.DictReader(io.StringIO(text)) if r.get("Close")]
    if not rows:
        raise ValueError(f"stooq returned no history for {symbol}")
    return rows


def _clean_money(value: Any) -> float | None:
    """Nasdaq returns '$182.40' and '74,210,000'."""
    if value is None:
        return None
    return _num(str(value).replace("$", "").replace(",", "").strip() or None)


def _bars_nasdaq(symbol: str, days: int) -> list[dict[str, Any]]:
    """Keyless daily OHLCV from Nasdaq.

    Primary source: Yahoo rate limits datacenter IPs with 429 and Stooq blocks
    them outright, but Nasdaq serves runners fine.
    """
    today = date.today()
    params = {
        "assetclass": "stocks",
        "fromdate": (today - timedelta(days=max(days * 2, 30))).isoformat(),
        "todate": today.isoformat(),
        "limit": "9999",
    }
    errors = []
    for asset_class in ("stocks", "etf"):
        params["assetclass"] = asset_class
        try:
            payload = _get(
                f"https://api.nasdaq.com/api/quote/{symbol.strip().upper()}/historical",
                params=params,
                headers=YAHOO_HEADERS,  # a browser-ish UA; Nasdaq 403s without one
            ).json()
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{asset_class}: {type(exc).__name__}: {exc}")
            continue

        rows = (((payload or {}).get("data") or {}).get("tradesTable") or {}).get("rows") or []
        out = []
        for r in rows:
            close = _clean_money(r.get("close"))
            if close is None:
                continue
            try:
                month, day, year = r["date"].split("/")
            except (KeyError, ValueError):
                continue
            out.append({
                "Date": f"{year}-{month}-{day}",
                "Open": _clean_money(r.get("open")) or close,
                "High": _clean_money(r.get("high")) or close,
                "Low": _clean_money(r.get("low")) or close,
                "Close": close,
                "Volume": _clean_money(r.get("volume")),
            })
        if out:
            out.sort(key=lambda b: b["Date"])  # Nasdaq returns newest first
            return out
        errors.append(f"{asset_class}: no rows ({str(payload.get('message'))[:60]})")
    raise ValueError(f"nasdaq returned no history for {symbol} — {'; '.join(errors)}")


def _bars_twelvedata(symbol: str, days: int) -> list[dict[str, Any]]:
    """800 calls/day on the free tier — the roomiest keyed fallback."""
    if not TWELVEDATA_KEY:
        raise ValueError("no api key")
    payload = _get(
        "https://api.twelvedata.com/time_series",
        params={
            "symbol": symbol.strip().upper(),
            "interval": "1day",
            "outputsize": max(days, 30),
            "apikey": TWELVEDATA_KEY,
        },
    ).json()
    if str(payload.get("status")) == "error":
        raise ValueError(str(payload.get("message"))[:160])
    values = payload.get("values") or []
    if not values:
        raise ValueError(f"twelvedata returned no values for {symbol}")
    out = [
        {
            "Date": v["datetime"],
            "Open": _num(v.get("open")),
            "High": _num(v.get("high")),
            "Low": _num(v.get("low")),
            "Close": _num(v.get("close")),
            "Volume": _num(v.get("volume")),
        }
        for v in values
        if _num(v.get("close")) is not None
    ]
    out.sort(key=lambda b: b["Date"])  # returned newest first
    return out


def _bars_alphavantage(symbol: str) -> list[dict[str, Any]]:
    """Last-resort history. 25 calls/day, so only reached when everything else is down."""
    if not ALPHAVANTAGE_KEY:
        raise ValueError("no api key")
    payload = _get(
        "https://www.alphavantage.co/query",
        params={
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol.upper(),
            "outputsize": "compact",  # ~100 sessions
            "apikey": ALPHAVANTAGE_KEY,
        },
    ).json()
    series = payload.get("Time Series (Daily)")
    if not series:
        # Alpha Vantage reports quota exhaustion as a 200 with a Note/Information key.
        raise ValueError(str(payload.get("Note") or payload.get("Information") or payload)[:160])
    return [
        {
            "Date": day,
            "Open": float(v["1. open"]),
            "High": float(v["2. high"]),
            "Low": float(v["3. low"]),
            "Close": float(v["4. close"]),
            "Volume": _num(v.get("5. volume")),
        }
        for day, v in sorted(series.items())
    ]


def history(symbol: str, days: int = 120) -> dict[str, Any]:
    """Daily OHLCV plus the levels needed to set entries, targets, and stops."""
    errors = []
    rows: list[dict[str, Any]] = []
    source = ""
    # Ordered by what actually works from a GitHub Actions runner: Nasdaq is
    # keyless and unblocked, Yahoo 429s, Stooq 404s. The keyed sources sit
    # behind them as insurance.
    for name, loader in (("nasdaq", lambda: _bars_nasdaq(symbol, days)),
                         ("yahoo", lambda: _bars_yahoo(symbol, days)),
                         ("twelvedata", lambda: _bars_twelvedata(symbol, days)),
                         ("alphavantage", lambda: _bars_alphavantage(symbol)),
                         ("stooq", lambda: _bars_stooq(symbol))):
        try:
            rows, source = loader(), name
            break
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{name}: {type(exc).__name__}: {exc}")

    if not rows:
        return {"ok": False, "symbol": symbol.upper(), "attempts": errors}

    try:
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
            "source": source,
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
        return _fail(source or "history", exc)


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

# Yahoo symbols. Futures (=F) matter here: they are the only free source of a
# price for the Robinhood Derivatives ideas, and they trade overnight, so at
# 6am ET they are the honest read on where the session opens.
MACRO_TICKERS = {
    "spx": "^GSPC",
    "ndx": "^NDX",
    "dow": "^DJI",
    "russell2000": "^RUT",
    "vix": "^VIX",
    "es_futures": "ES=F",
    "nq_futures": "NQ=F",
    "dollar_index": "DX-Y.NYB",
    "us10y_yield": "^TNX",
    "gold": "GC=F",
    "wti_crude": "CL=F",
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

def profile(symbol: str) -> dict[str, Any]:
    """Sector, industry, and market cap — used for concentration and sizing rules."""
    if not FINNHUB_KEY:
        return {"ok": False, "source": "finnhub", "error": "no api key"}
    try:
        d = _get("https://finnhub.io/api/v1/stock/profile2",
                 params={"symbol": symbol.upper(), "token": FINNHUB_KEY}).json()
        if not d:
            raise ValueError(f"no profile for {symbol}")
        cap_m = _num(d.get("marketCapitalization"))  # Finnhub reports millions
        return {
            "ok": True, "source": "finnhub", "symbol": symbol.upper(),
            "name": d.get("name"),
            "sector": d.get("finnhubIndustry"),
            "exchange": d.get("exchange"),
            "market_cap_usd": cap_m * 1e6 if cap_m else None,
            "shares_outstanding": _num(d.get("shareOutstanding")),
        }
    except Exception as exc:  # noqa: BLE001
        return _fail("finnhub", exc)


def insiders(symbol: str, months: int = 6) -> dict[str, Any]:
    """Insider transactions, weighted toward open-market buys.

    Executives sell for a hundred reasons — diversification, taxes, a house.
    They buy for one. A cluster of open-market purchases (transaction code P) by
    several officers is among the few genuinely predictive public signals, so
    that is what this surfaces rather than raw transaction counts.
    """
    today = date.today()
    since = today - timedelta(days=months * 31)

    if FINNHUB_KEY:
        try:
            data = _get(
                "https://finnhub.io/api/v1/stock/insider-transactions",
                params={"symbol": symbol.upper(), "token": FINNHUB_KEY,
                        "from": since.isoformat(), "to": today.isoformat()},
            ).json()
            rows = data.get("data") or []
            buys = [r for r in rows if (r.get("transactionCode") or "").upper() == "P"]
            sells = [r for r in rows if (r.get("transactionCode") or "").upper() == "S"]
            buy_value = sum(abs(_num(r.get("change")) or 0) * (_num(r.get("transactionPrice")) or 0)
                            for r in buys)
            sell_value = sum(abs(_num(r.get("change")) or 0) * (_num(r.get("transactionPrice")) or 0)
                             for r in sells)
            buyers = {r.get("name") for r in buys if r.get("name")}
            return {
                "ok": True,
                "source": "finnhub",
                "symbol": symbol.upper(),
                "window_months": months,
                "open_market_buys": len(buys),
                "distinct_buyers": len(buyers),
                "buy_value_usd": round(buy_value, 2),
                "sells": len(sells),
                "sell_value_usd": round(sell_value, 2),
                "net_value_usd": round(buy_value - sell_value, 2),
                "recent_buys": [
                    {"name": r.get("name"), "date": r.get("transactionDate"),
                     "shares": _num(r.get("change")), "price": _num(r.get("transactionPrice"))}
                    for r in sorted(buys, key=lambda r: r.get("transactionDate") or "", reverse=True)[:8]
                ],
                "note": (
                    "Code P is an open-market purchase and is the signal worth weighting. "
                    "Sales are reported for completeness but are weak evidence on their own."
                ),
            }
        except Exception as exc:  # noqa: BLE001
            finnhub_error = f"{type(exc).__name__}: {exc}"
    else:
        finnhub_error = "no api key"

    # Fallback: SEC gives the filing stream but not parsed amounts. A burst of
    # Form 4s still tells you something; you just have to open them.
    sec = filings(symbol, limit=60)
    if sec.get("ok"):
        form4s = [f for f in sec.get("filings", []) if f.get("form") == "4"
                  and (f.get("filed") or "") >= since.isoformat()]
        return {
            "ok": True,
            "source": "sec",
            "symbol": symbol.upper(),
            "window_months": months,
            "form4_filings": len(form4s),
            "recent": form4s[:8],
            "note": (
                f"Finnhub unavailable ({finnhub_error}); this is the raw Form 4 stream with no "
                "buy/sell breakdown. Open the filings to see direction and size."
            ),
        }
    return {"ok": False, "source": "insiders", "error": f"finnhub: {finnhub_error}; sec: {sec.get('error')}"}


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

    p = sub.add_parser("insiders", help="insider transactions, weighted to open-market buys")
    p.add_argument("symbol")
    p.add_argument("--months", type=int, default=6)

    p = sub.add_parser("profile", help="sector, industry, and market cap")
    p.add_argument("symbol")

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
    elif args.cmd == "insiders":
        result = insiders(args.symbol, args.months)
    elif args.cmd == "profile":
        result = profile(args.symbol)
    else:  # pragma: no cover - argparse enforces the choices
        parser.error(f"unknown command {args.cmd}")

    json.dump(result, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
