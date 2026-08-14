# Setup

Four required steps. Budget about 20 minutes. Nothing runs until steps 1–3 are
done; step 4 is optional polish.

---

## 1. Claude subscription token

This is what makes the workflow bill your Claude plan instead of an API key.

On your own machine, with Claude Code installed and logged in:

```bash
claude setup-token
```

Copy the token it prints. Then in this repo:

**Settings → Secrets and variables → Actions → New repository secret**

| Name | Value |
| ---- | ----- |
| `CLAUDE_CODE_OAUTH_TOKEN` | the token from `setup-token` |

Notes:
- The token is tied to *your* subscription. Long-lived, but not immortal — if
  the workflow starts failing with an auth error, regenerate and re-paste.
- A 60-minute Opus research run is a substantial chunk of usage. If you hit
  plan limits, drop `research_minutes` in the workflow.

---

## 2. Google Sheet + service account

### 2a. Create the Sheet

Make a new Google Sheet. Name it whatever you like — `Daily Trade Report` works.

From its URL, grab the ID:

```
https://docs.google.com/spreadsheets/d/1AbCdEf...XyZ/edit
                                       ^^^^^^^^^^^^^^ this part
```

Add it as a repository secret:

| Name | Value |
| ---- | ----- |
| `GOOGLE_SHEET_ID` | `1AbCdEf...XyZ` |

You do **not** need to create any tabs. The publisher creates `Today`,
`Performance`, and dated archive tabs on first run.

### 2b. Create the service account

1. Go to [console.cloud.google.com](https://console.cloud.google.com) and create
   a project (or reuse one). Name: `invest-trade-daily`.
2. **APIs & Services → Library** → enable **Google Sheets API**.
   (The Drive API is not needed — the publisher opens the Sheet by ID.)
3. **APIs & Services → Credentials → Create credentials → Service account**.
   - Name: `sheets-writer`
   - Grant it no project roles. It needs none; access is granted on the Sheet
     itself in the next step.
4. Open the new service account → **Keys → Add key → Create new key → JSON**.
   A `.json` file downloads.
5. Copy the **entire contents** of that JSON file into a repository secret:

   | Name | Value |
   | ---- | ----- |
   | `GCP_SERVICE_ACCOUNT_JSON` | the whole JSON, `{` to `}` |

   Paste it raw — do not base64-encode it, do not strip newlines.

### 2c. Share the Sheet with the service account

Open the JSON and find `"client_email"` — it looks like
`sheets-writer@invest-trade-daily.iam.gserviceaccount.com`.

In your Google Sheet: **Share** → paste that email → give it **Editor** →
uncheck "Notify people" → Share.

**This step is the one everyone forgets.** Without it the workflow fails with
`PermissionError: The caller does not have permission`.

Finally, delete the downloaded JSON key from your Downloads folder.

---

## 3. SEC user agent

The SEC requires a descriptive User-Agent on EDGAR requests and blocks traffic
without one.

| Name | Value |
| ---- | ----- |
| `SEC_USER_AGENT` | `Your Name your@email.com` |

Any real name and reachable email is fine.

---

## 4. Optional free API keys

All free, all optional. Each one measurably improves research quality. Without
them the pipeline falls back to keyless sources (Nasdaq, CoinGecko, Kalshi, SEC,
and Claude's web search).

| Secret | Where | Free tier | Buys you | Worth it? |
| ------ | ----- | --------- | -------- | --------- |
| `FINNHUB_API_KEY` | [finnhub.io/register](https://finnhub.io/register) | 60 calls/min | Earnings calendar, real quotes, company news | **Yes** |
| `FRED_API_KEY` | [fred.stlouisfed.org/docs/api/api_key.html](https://fred.stlouisfed.org/docs/api/api_key.html) | unlimited, instant | Rates, CPI, unemployment, yield curve | **Yes** |
| `TWELVEDATA_API_KEY` | [twelvedata.com/pricing](https://twelvedata.com/pricing) | 800 calls/day | Backup daily OHLCV if Nasdaq breaks | Insurance |
| `ALPHAVANTAGE_API_KEY` | [alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key) | 25 calls/**day** | Last-resort OHLCV | Marginal |

Add whichever you want as repository secrets. The scripts detect what is present
and skip what is not.

Two of these are worth the two minutes each:

- **Finnhub** gives a real earnings calendar. Catalyst hunting is 35% of the
  research budget and earnings are the single richest source of dated
  catalysts. Without it, Claude reconstructs the calendar from web search —
  workable, but slower and easier to get wrong.
- **FRED** gives authoritative rates and inflation series instead of whatever a
  news article claims the 10-year is.

Twelve Data and Alpha Vantage are pure insurance on daily price history. The
primary source is Nasdaq, which is keyless and works from Actions runners —
unlike Yahoo, which rate limits them with 429, and Stooq, which blocks them
outright. Add Twelve Data if you want a real backup; its 800 calls/day is
roomy. Alpha Vantage's 25 calls per *day* can be exhausted by a single research
run, so it is a last resort rather than a fallback.

---

## 5. Verify

First run **Actions → Data Sources Check → Run workflow**. It probes every
data source and does a real write-read-delete against your Sheet, then prints
a table of what works. This is the fastest way to catch a setup mistake, and it
takes about a minute.

Then run the real thing: Actions → **Daily Trade Report** → **Run workflow**,
and set:

```
research_minutes: 5
dry_run: false
```

A 5-minute run produces a thin but real report and — importantly — proves the
Google Sheets write works end to end. Check that `Today` and `Performance` tabs
appeared in your Sheet.

If it fails, the job log names the failing phase. Common causes:

| Symptom | Cause |
| ------- | ----- |
| `The caller does not have permission` | Skipped step 2c — share the Sheet with `client_email` |
| `invalid_grant` / auth error on the Claude step | Token expired; rerun `claude setup-token` |
| `Your Request Originates from an Undeclared Automated Tool` | `SEC_USER_AGENT` missing or not an email |
| Stooq or Yahoo rows show ❌ | Expected. Stooq 404s and Yahoo 429s from Actions runners. Finnhub covers quotes, Nasdaq covers history |
| A **critical** source is 🔴 | Do not trust a 6am run. Without price history the report cannot set real levels, and it will publish few or no ideas rather than invent them |
| Workflow never fires at 6am | See "Scheduling" below |
| Run is red but the Sheet updated | Intentional — see "Failure alerts" below |

---

## Failure alerts

There is no notification channel to configure. The run finishes, the Sheet is
current, and you open it when you want it.

The one deliberate exception: when the pipeline fails badly enough that the
report is a stub with no ideas, **the workflow marks itself red on purpose**.
GitHub emails repository owners about failed scheduled runs but says nothing
about successful ones — so without this, the single morning that produced
nothing would also be the single morning you heard nothing about. A red run
with a fresh Sheet is not a contradiction; it means "published, but the
contents are an apology."

The Sheet write and the git commit both happen *before* that failure, so a red
run still leaves you the full record.

To check what happened, open the run and read the summary — it names which
phase failed and includes the report's data-quality note.

---

## Scheduling

The workflow declares two cron entries — `10:00 UTC` and `11:00 UTC` — and a
gate step that exits immediately unless the current time in `America/New_York`
is the 6 o'clock hour. That is how it stays at 6:00 AM ET across daylight
saving transitions without you touching anything.

Two things worth knowing about GitHub's scheduler:

- **It is best-effort.** Scheduled runs queue behind Actions load and can start
  5–30 minutes late, occasionally later. If a run must be punctual, that is an
  argument for a different host, not a fixable setting.
- **Public repos get their schedules disabled after 60 days without repository
  activity.** `keepalive.yml` runs weekly and touches a timestamp file to
  prevent that. Leave it enabled.
