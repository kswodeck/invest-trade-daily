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
    python scripts/market_data.py depth NVDA          # bid/ask spread
    python scripts/market_data.py implied NVDA        # options-implied move
    python scripts/market_data.py implied NVDA --entry 180 --target 210
    python scripts/market_data.py relstrength NVDA --peer XLK
    python scripts/market_data.py short NVDA
    python scripts/market_data.py analysts NVDA

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
from datetime import date, datetime, time as dtime, timedelta, timezone
from typing import Any, Iterable
from zoneinfo import ZoneInfo

import requests

TIMEOUT = 20
ET = ZoneInfo("America/New_York")

# US equity session boundaries, ET. Outside regular hours the freshest honest
# equity price is the last close, and that is not a data-quality problem — it is
# what the market is doing. Callers use this to tell "stale" from "closed".
PRE_OPEN, REGULAR_OPEN = dtime(4, 0), dtime(9, 30)
REGULAR_CLOSE, POST_CLOSE = dtime(16, 0), dtime(20, 0)

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


def market_session(now: datetime | None = None) -> str:
    """Which US equity session we are in: pre, regular, post, or closed."""
    now = (now or datetime.now(ET)).astimezone(ET)
    if now.weekday() >= 5:
        return "closed"
    t = now.time()
    if REGULAR_OPEN <= t < REGULAR_CLOSE:
        return "regular"
    if PRE_OPEN <= t < REGULAR_OPEN:
        return "pre"
    if REGULAR_CLOSE <= t < POST_CLOSE:
        return "post"
    return "closed"


def age_minutes(asof: str | None, now: datetime | None = None) -> float | None:
    """Minutes since a quote timestamp. None when it cannot be parsed."""
    if not asof:
        return None
    try:
        stamp = datetime.fromisoformat(str(asof).replace("Z", "+00:00"))
    except ValueError:
        return None
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=ET)
    return round(((now or datetime.now(ET)) - stamp).total_seconds() / 60, 1)


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
                params={"range": rng, "interval": interval, "includePrePost": "true"},
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


def quote_depth(symbol: str) -> dict[str, Any]:
    """Bid, ask, and spread from Nasdaq.

    The spread matters more than the last price on thin names: a 3% spread eats
    the edge before the thesis has a chance to play out. Nasdaq is used because
    it already serves GitHub runners reliably; the free quote APIs that give a
    last price mostly do not publish depth.

    Returns bid/ask as None outside regular hours, which is normal, not a fault.
    """
    try:
        payload = _get(
            f"https://api.nasdaq.com/api/quote/{symbol.strip().upper()}/info",
            params={"assetclass": "stocks"},
            headers=YAHOO_HEADERS,
        ).json()
        data = (payload or {}).get("data") or {}
        primary = data.get("primaryData") or {}

        def money(key: str) -> float | None:
            raw = primary.get(key)
            if not raw or str(raw).strip().upper() in ("N/A", "", "--"):
                return None
            return _num(str(raw).replace("$", "").replace(",", "").strip())

        last = money("lastSalePrice")
        bid, ask = money("bidPrice"), money("askPrice")
        spread_pct = None
        if bid and ask and ask > bid:
            mid = (bid + ask) / 2
            spread_pct = round((ask - bid) / mid * 100, 3) if mid else None
        return {
            "ok": last is not None or bid is not None,
            "source": "nasdaq",
            "symbol": symbol.upper(),
            "price": last,
            "bid": bid,
            "ask": ask,
            "spread_pct": spread_pct,
            "is_real_time": bool(primary.get("isRealTime")),
            "asof": primary.get("lastTradeTimestamp"),
            "session": market_session(),
        }
    except Exception as exc:  # noqa: BLE001
        return _fail("nasdaq", exc)


def quote(symbol: str) -> dict[str, Any]:
    """First source that returns a usable price wins.

    Every result carries `session` and `age_minutes` so callers can tell a stale
    quote from a market that is simply shut. At 6am ET on a weekday the freshest
    honest equity price is yesterday's close, and that is not a failure.
    """
    attempts = []
    for fn in (quote_finnhub, quote_yahoo, quote_stooq, quote_alphavantage):
        result = fn(symbol)
        if result.get("ok"):
            result["fallbacks_tried"] = [a["source"] for a in attempts]
            result["session"] = market_session()
            result["age_minutes"] = age_minutes(result.get("asof"))
            return result
        attempts.append(result)
    return {"ok": False, "symbol": symbol.upper(), "attempts": attempts,
            "session": market_session()}


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


def _load_bars(symbol: str, days: int) -> tuple[list[dict[str, Any]], str, list[str]]:
    """Daily bars from the first source that answers. Never raises.

    Ordered by what actually works from a GitHub Actions runner: Nasdaq is
    keyless and unblocked, Yahoo 429s, Stooq 404s. The keyed sources sit behind
    them as insurance. Returns (rows, source, errors) with rows empty when
    every source failed.
    """
    errors: list[str] = []
    for name, loader in (("nasdaq", lambda: _bars_nasdaq(symbol, days)),
                         ("yahoo", lambda: _bars_yahoo(symbol, days)),
                         ("twelvedata", lambda: _bars_twelvedata(symbol, days)),
                         ("alphavantage", lambda: _bars_alphavantage(symbol)),
                         ("stooq", lambda: _bars_stooq(symbol))):
        try:
            return loader(), name, errors
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{name}: {type(exc).__name__}: {exc}")
    return [], "", errors


def history(symbol: str, days: int = 120) -> dict[str, Any]:
    """Daily OHLCV plus the levels needed to set entries, targets, and stops."""
    rows, source, errors = _load_bars(symbol, days)

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

# --------------------------------------------------------------------------
# what the market already thinks
# --------------------------------------------------------------------------

def implied_move(symbol: str, days: int = 30) -> dict[str, Any]:
    """What the options market prices as the move to the nearest useful expiry.

    A target set from ATR is a claim about how far price can travel. The options
    market is already quoting that claim in dollars, and it is the only estimate
    here that other people are betting real money on. Comparing the two is the
    cheapest reality check available: a swing target three times the 30-day
    implied move is not an edge, it is a forecast the market disagrees with.

    Priced off the at-the-money straddle rather than parsed implied vols — the
    straddle is what you would actually pay to own the move, needs no model, and
    survives a missing greeks field.
    """
    ticker = _yahoo_symbol(symbol)
    try:
        base = f"https://query1.finance.yahoo.com/v7/finance/options/{ticker}"
        chain = _get(base).json()
        result = ((chain.get("optionChain") or {}).get("result") or [None])[0]
        if not result:
            raise ValueError(f"no option chain for {symbol}")

        spot = _num((result.get("quote") or {}).get("regularMarketPrice"))
        expiries = [int(e) for e in (result.get("expirationDates") or [])]
        if not spot or not expiries:
            raise ValueError(f"no spot or expiries for {symbol}")

        wanted = datetime.now(timezone.utc) + timedelta(days=days)
        target_epoch = int(wanted.timestamp())
        expiry = min(expiries, key=lambda e: abs(e - target_epoch))
        expiry_date = datetime.fromtimestamp(expiry, tz=timezone.utc).date()
        to_expiry = (expiry_date - date.today()).days

        detail = _get(base, params={"date": expiry}).json()
        options = (((detail.get("optionChain") or {}).get("result") or [{}])[0]
                   .get("options") or [{}])[0]
        calls, puts = options.get("calls") or [], options.get("puts") or []
        if not calls or not puts:
            raise ValueError(f"empty chain for {symbol} at {expiry_date}")

        def at_the_money(rows: list[dict]) -> dict:
            def distance(row: dict) -> float:
                strike = _num(row.get("strike"))
                return abs(strike - spot) if strike is not None else float("inf")
            return min(rows, key=distance)

        def price(row: dict) -> float | None:
            """Mid where there is a two-sided market, last trade otherwise."""
            bid, ask = _num(row.get("bid")), _num(row.get("ask"))
            if bid and ask and ask >= bid:
                return (bid + ask) / 2
            return _num(row.get("lastPrice"))

        call, put = at_the_money(calls), at_the_money(puts)
        call_price, put_price = price(call), price(put)
        if call_price is None or put_price is None:
            raise ValueError(f"no usable option prices for {symbol}")

        straddle = call_price + put_price
        move_pct = round(straddle / spot * 100, 2)
        return {
            "ok": True, "source": "yahoo-options", "symbol": symbol.upper(),
            "spot": round(spot, 4),
            "expiry": expiry_date.isoformat(),
            "days_to_expiry": to_expiry,
            "atm_strike": _num(call.get("strike")),
            "straddle": round(straddle, 4),
            # One standard deviation, near enough: the straddle is roughly
            # 0.8 sigma, so this is the move the market gives about a 1-in-3
            # chance of being exceeded in either direction.
            "implied_move_pct": move_pct,
            "implied_move_usd": round(straddle, 4),
            "implied_iv": _num(call.get("impliedVolatility")),
            "note": (f"options price a ±{move_pct}% move by {expiry_date.isoformat()} "
                     f"({to_expiry}d). A target further than this is a bet against "
                     f"the options market, not a read of it."),
        }
    except Exception as exc:  # noqa: BLE001
        return _fail("yahoo-options", exc)


def target_vs_implied(symbol: str, entry: float, target: float, days: int = 30) -> dict[str, Any]:
    """Convenience wrapper: how many implied moves away is this target?

    Under 1.0 the options market already considers the move ordinary. Above
    about 2.0 the report is claiming something the people pricing the risk do
    not believe.
    """
    implied = implied_move(symbol, days)
    if not implied.get("ok"):
        return implied
    move_pct = abs(target - entry) / entry * 100
    multiple = round(move_pct / implied["implied_move_pct"], 2) if implied["implied_move_pct"] else None
    return {**implied, "target_move_pct": round(move_pct, 2), "implied_multiples": multiple}


def relative_strength(symbol: str, benchmark: str = "SPY", peer: str | None = None) -> dict[str, Any]:
    """Trailing returns against a benchmark, and optionally a sector proxy.

    A process that sets every entry below the current price buys whatever has
    been falling, which is how a report ends up long the weakest names in the
    weakest sectors and calls it value. This puts the relative move on the page
    so that choice has to be made deliberately.
    """
    windows = {"1m": 21, "3m": 63, "6m": 126}
    needed = max(windows.values()) + 5

    def closes(sym: str) -> list[float]:
        rows, _, errors = _load_bars(sym, needed)
        if not rows:
            raise ValueError(f"no history for {sym}: {'; '.join(errors[:2])}")
        return [float(r["Close"]) for r in rows]

    try:
        series = {symbol.upper(): closes(symbol), benchmark.upper(): closes(benchmark)}
        if peer:
            series[peer.upper()] = closes(peer)

        def trailing(values: list[float], back: int) -> float | None:
            if len(values) <= back:
                return None
            return round((values[-1] - values[-1 - back]) / values[-1 - back] * 100, 2)

        returns = {sym: {w: trailing(vals, n) for w, n in windows.items()}
                   for sym, vals in series.items()}
        me = returns[symbol.upper()]

        def spread(other: str) -> dict[str, float | None]:
            them = returns[other]
            return {w: (round(me[w] - them[w], 2) if me[w] is not None and them[w] is not None else None)
                    for w in windows}

        out = {
            "ok": True, "source": "computed", "symbol": symbol.upper(),
            "returns_pct": returns,
            "vs_benchmark_pct": spread(benchmark.upper()),
            "benchmark": benchmark.upper(),
        }
        if peer:
            out["vs_peer_pct"] = spread(peer.upper())
            out["peer"] = peer.upper()
        beats = [w for w, v in out["vs_benchmark_pct"].items() if v is not None and v > 0]
        out["leadership"] = (
            f"outperforming {benchmark.upper()} on {'/'.join(beats)}" if beats
            else f"lagging {benchmark.upper()} on every window measured")
        return out
    except Exception as exc:  # noqa: BLE001
        return _fail("relative_strength", exc)


def short_interest(symbol: str) -> dict[str, Any]:
    """Reported short interest and days to cover.

    Matters in both directions and the report has been flying blind on it: a
    crowded short is fuel under a long, and it is also the reason a short idea
    can be right about the business and still lose. Days to cover is the number
    to read — shares short divided by average daily volume, i.e. how long the
    exit takes.
    """
    ticker = symbol.strip().upper()
    last_error: Exception = ValueError(f"no short interest reported for {ticker}")
    for asset_class in ("stocks", "etf"):
        try:
            data = _get(f"https://api.nasdaq.com/api/quote/{ticker}/short-interest",
                        params={"assetClass": asset_class}).json()
            rows = (((data.get("data") or {}).get("shortInterestTable") or {}).get("rows")) or []
            if not rows:
                continue
            latest = rows[0]
            shares = _clean_money(latest.get("interest"))
            volume = _clean_money(latest.get("avgDailyShareVolume"))
            return {
                "ok": True, "source": "nasdaq", "symbol": ticker,
                "settlement_date": latest.get("settlementDate"),
                "shares_short": shares,
                "avg_daily_volume": volume,
                "days_to_cover": _num(latest.get("daysToCover")),
                # Two prints, so the direction is visible rather than just the level.
                "prior_shares_short": _clean_money(rows[1].get("interest")) if len(rows) > 1 else None,
                "history": [
                    {"date": r.get("settlementDate"),
                     "shares_short": _clean_money(r.get("interest")),
                     "days_to_cover": _num(r.get("daysToCover"))}
                    for r in rows[:6]
                ],
            }
        except Exception as exc:  # noqa: BLE001
            last_error = exc
    return _fail("nasdaq", last_error)


def analysts(symbol: str) -> dict[str, Any]:
    """Analyst recommendation trend and the recent earnings surprise record.

    Estimate revisions proper are paywalled everywhere useful, so this is the
    free proxy: the month-by-month buy/hold/sell mix, which moves when analysts
    change their minds, and whether the company has been beating or missing.
    Read the *change* across months, not the level — a stock nobody upgrades is
    not the same as one being upgraded from a low base.
    """
    if not FINNHUB_KEY:
        return {"ok": False, "source": "finnhub", "error": "no api key"}
    out: dict[str, Any] = {"ok": True, "source": "finnhub", "symbol": symbol.upper()}
    try:
        trend = _get("https://finnhub.io/api/v1/stock/recommendation",
                     params={"symbol": symbol.upper(), "token": FINNHUB_KEY}).json() or []
        rows = sorted(trend, key=lambda r: r.get("period", ""), reverse=True)[:4]
        out["recommendation_trend"] = [
            {"period": r.get("period"), "strong_buy": r.get("strongBuy"), "buy": r.get("buy"),
             "hold": r.get("hold"), "sell": r.get("sell"), "strong_sell": r.get("strongSell")}
            for r in rows
        ]

        def bullish_share(row: dict) -> float | None:
            total = sum(row.get(k) or 0 for k in
                        ("strong_buy", "buy", "hold", "sell", "strong_sell"))
            if not total:
                return None
            return round(((row.get("strong_buy") or 0) + (row.get("buy") or 0)) / total * 100, 1)

        shares = [bullish_share(r) for r in out["recommendation_trend"]]
        if len(shares) >= 2 and shares[0] is not None and shares[-1] is not None:
            out["bullish_share_pct"] = shares[0]
            out["bullish_share_change_pct"] = round(shares[0] - shares[-1], 1)
            out["revision_direction"] = (
                "improving" if shares[0] > shares[-1] else
                "deteriorating" if shares[0] < shares[-1] else "flat")
    except Exception as exc:  # noqa: BLE001
        out["recommendation_error"] = f"{type(exc).__name__}: {exc}"

    try:
        surprises = _get("https://finnhub.io/api/v1/stock/earnings",
                         params={"symbol": symbol.upper(), "token": FINNHUB_KEY}).json() or []
        out["earnings_surprises"] = [
            {"period": r.get("period"), "actual": r.get("actual"),
             "estimate": r.get("estimate"), "surprise_pct": r.get("surprisePercent")}
            for r in surprises[:4]
        ]
        beats = [r for r in out["earnings_surprises"] if (r.get("surprise_pct") or 0) > 0]
        out["beats_last_4"] = len(beats)
    except Exception as exc:  # noqa: BLE001
        out["surprise_error"] = f"{type(exc).__name__}: {exc}"

    if "recommendation_trend" not in out and "earnings_surprises" not in out:
        return {"ok": False, "source": "finnhub", "symbol": symbol.upper(),
                "error": out.get("recommendation_error") or out.get("surprise_error")}
    return out


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

    p = sub.add_parser("depth", help="bid, ask, and spread for an equity")
    p.add_argument("symbol")

    p = sub.add_parser("implied", help="options-implied move; --entry/--target to compare a target against it")
    p.add_argument("symbol")
    p.add_argument("--days", type=int, default=30, help="aim for the expiry nearest this many days out")
    p.add_argument("--entry", type=float)
    p.add_argument("--target", type=float)

    p = sub.add_parser("relstrength", help="trailing returns vs a benchmark and an optional sector proxy")
    p.add_argument("symbol")
    p.add_argument("--benchmark", default="SPY")
    p.add_argument("--peer", help="sector ETF, e.g. XLE for an energy name")

    p = sub.add_parser("short", help="reported short interest and days to cover")
    p.add_argument("symbol")

    p = sub.add_parser("analysts", help="recommendation trend and earnings surprise record")
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
    elif args.cmd == "depth":
        result = quote_depth(args.symbol)
    elif args.cmd == "implied":
        result = (target_vs_implied(args.symbol, args.entry, args.target, args.days)
                  if args.entry is not None and args.target is not None
                  else implied_move(args.symbol, args.days))
    elif args.cmd == "relstrength":
        result = relative_strength(args.symbol, args.benchmark, args.peer)
    elif args.cmd == "short":
        result = short_interest(args.symbol)
    elif args.cmd == "analysts":
        result = analysts(args.symbol)
    else:  # pragma: no cover - argparse enforces the choices
        parser.error(f"unknown command {args.cmd}")

    json.dump(result, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
