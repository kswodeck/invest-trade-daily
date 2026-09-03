# Why the report is late, and what actually fixes it

## The finding

GitHub Actions `schedule` is best-effort. It is not a cron daemon and makes no
delivery-time promise. For this repo it was reliably ~30 minutes late for two
weeks and then degraded sharply, and has not recovered:

| ET date | `7 10 * * *` arm delivered | Late by | Report published |
| --- | --- | --- | --- |
| 2026-08-19 → 08-26 | 10:24Z – 10:38Z | 24–38 min | ~07:15 ET |
| 2026-08-27 | 20:10Z | **10h 10m** | none — window closed |
| 2026-08-28 | 21:07Z | **11h 07m** | none from cron |
| 2026-08-29 | 14:56Z | **4h 56m** | 11:53 ET |
| 2026-08-30 | 14:42Z | **4h 42m** | 11:30 ET |
| 2026-08-31 | not delivered by 12:29Z | **> 2h 29m** | dispatched by hand |

The same delay hits every workflow in the repo, so it is the scheduler, not
this configuration.

## What the repo does about it

Everything here is damage control. None of it makes the trigger arrive at 6am.

- **A 6–11 ET window** (`scripts/schedule_gate.py`). A delivery hours late still
  produces a report. Bounded, because a report researched in the afternoon is
  not the pre-open view and must not pretend to be.
- **Crons off `:00`.** The top of the hour is the busiest minute on GitHub's
  scheduler and the first it sheds. A hedge, worth the one-line change, not a
  fix.
- **A catch-up any workflow can call** (`.github/actions/report-catch-up`).
  Different workflows are delayed differently, so whichever one GitHub does
  deliver inside the window can dispatch the report. Bounded to three attempts
  a day by `scripts/report_runs.py`.
- **An honest stamp** (`scripts/note_late_run.py`). A report researched at 10:42
  says so in `data_quality_notes` rather than reading like the 6am view.
- **An alarm** (`Report Watchdog`). A lost morning is a red run, never silence.

Together these turn "no report" into "a late report that admits it is late".
That is the ceiling for anything living inside GitHub Actions.

## What actually fixes it

A trigger from outside GitHub. Use **cron-job.org**: it is free with no card, it
understands `America/New_York` so daylight saving is its problem rather than
yours, and the token it holds can do nothing but start a workflow run.

### The token: Actions, not Contents

This matters more than it looks. This repository's Actions hold
`GCP_SERVICE_ACCOUNT_JSON`, `CLAUDE_CODE_OAUTH_TOKEN` and every market-data key.
**Anyone who can push to the repo can add a workflow step that prints them.** So
the trigger must not use a token that can push:

| Endpoint | Token permission | What a leak costs you |
| --- | --- | --- |
| `POST /repos/…/dispatches` (`repository_dispatch`) | Contents: **write** | Push access → every Actions secret is readable |
| `POST /repos/…/actions/workflows/…/dispatches` (`workflow_dispatch`) | Actions: **write** | Someone can start and cancel workflow runs. That is all. |

Use the second one. `repository_dispatch` stays wired up in the workflow for a
caller that already has a Contents-scoped token for other reasons, but it is not
what you should hand to a third-party scheduler.

Create the token at **Settings → Developer settings → Personal access tokens →
Fine-grained tokens**:

- **Repository access:** Only select repositories → `invest-trade-daily`
- **Permissions → Repository permissions → Actions:** Read and write
- Leave everything else at "No access". (Metadata: Read is added automatically
  and cannot be removed; it is harmless.)
- **Expiration:** pick one, and put the rotation date in your calendar. A
  dispatch that silently stops because a token expired is the same outage in a
  new costume.

### The call

```
POST https://api.github.com/repos/kswodeck/invest-trade-daily/actions/workflows/daily-report.yml/dispatches
Accept: application/vnd.github+json
Authorization: Bearer <TOKEN>
Content-Type: application/json

{"ref": "main", "inputs": {"respect_window": "true"}}
```

A **204 No Content** means accepted; the run starts within seconds. Any other
status is a failure — 401 is a bad or expired token, 403 is a token without
Actions: write, 422 is a malformed body.

`respect_window: "true"` is what makes the call safe to repeat. It tells the
gate to apply the 6-11 ET window and the duplicate check to this dispatch, so a
retry, an overlap with a GitHub cron that finally arrived, or a second scheduler
firing all resolve to a ten-second skip instead of a duplicate report.

### cron-job.org, exactly

1. Sign up at <https://cron-job.org> and confirm the email.
2. **Create cronjob.**
3. **Title:** `invest-trade-daily 6am ET`
4. **URL:**
   `https://api.github.com/repos/kswodeck/invest-trade-daily/actions/workflows/daily-report.yml/dispatches`
5. **Schedule:** every day, hour `6`, minute `0`. Set **Timezone** to
   `America/New_York` — this is the whole reason to prefer this service, and it
   is why you need only one schedule rather than two UTC arms.
6. Open the **Advanced** section:
   - **Request method:** `POST`
   - **Headers:**
     - `Authorization: Bearer <TOKEN>`
     - `Accept: application/vnd.github+json`
     - `Content-Type: application/json`
   - **Request body:** `{"ref": "main", "inputs": {"respect_window": "true"}}`
   - **Treat redirects as success / expected status:** GitHub answers `204`.
     If the service lets you name the success status, say `204`; otherwise its
     default 2xx handling is correct.
7. Enable **notifications on failure**, so a 401 after a token expiry reaches
   you rather than becoming a quiet outage.
8. Save, then use **Test run** and confirm you get `204` and that a
   `Daily Trade Report` run appears in the repo's Actions tab within a few
   seconds.

### If you would rather not give a third party the token

A Cloudflare Worker keeps the token as an encrypted secret in your own account.
Free plan covers this comfortably. Cloudflare cron triggers are **UTC only**, so
declare both DST arms and let the repo's gate drop the wrong one.

`wrangler.toml`:

```toml
name = "invest-trade-daily-trigger"
main = "src/index.js"
compatibility_date = "2026-08-31"

[triggers]
crons = ["0 10 * * *", "0 11 * * *"]   # 06:00 ET in EDT and in EST
```

`src/index.js`:

```js
export default {
  async scheduled(event, env, ctx) {
    const res = await fetch(
      "https://api.github.com/repos/kswodeck/invest-trade-daily/actions/workflows/daily-report.yml/dispatches",
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${env.GH_DISPATCH_TOKEN}`,
          Accept: "application/vnd.github+json",
          "Content-Type": "application/json",
          "User-Agent": "invest-trade-daily-trigger",
        },
        body: JSON.stringify({ ref: "main", inputs: { respect_window: "true" } }),
      },
    );
    // 204 is success. Anything else should be loud in the Worker's logs.
    if (res.status !== 204) {
      throw new Error(`dispatch failed: ${res.status} ${await res.text()}`);
    }
  },
};
```

Then `wrangler secret put GH_DISPATCH_TOKEN` and `wrangler deploy`. Both arms
fire every day; in EDT the 11:00Z one finds the report already published and
skips, in EST the 10:00Z one is dropped as too early.

### Keeping the GitHub crons

Leave them. They cost nothing when the external trigger wins the race — the
gate sees a published report on the branch tip and skips in about ten seconds —
and they are the fallback if the external scheduler is the thing that breaks.

## The odd-lot screener, on the same footing

`Odd-Lot Tender Screener` runs twice a day and has exactly the same problem, so
it gets exactly the same treatment: two UTC arms per slot, a window, and a
duplicate guard. The differences are worth knowing.

| | Daily Trade Report | Odd-Lot Tender Screener |
| --- | --- | --- |
| Slots | 06:07 ET | 05:37 ET and 18:30 ET |
| Crons | `7 10`, `7 11` | `37 9`, `37 10`, `30 22 * * 1-5`, `30 23 * * 1-5` |
| Windows | 6–11 ET | 5–11 ET and 18–23 ET |
| What drops the second DST arm | today's report already on the branch tip | the universe was re-scored under two hours ago |
| Decided by | `scripts/schedule_gate.py` | `scripts/odd_lot.py slot` |

The morning slot is **30 minutes ahead of the report** so the Sheet's odd-lot
tab is already current when the research phase starts. The evening slot is after
EDGAR's **17:30 ET filing cutoff**, which is why its window opens at 18:00 and
not 17:00 — a run at 17:30 would find nothing that a run at 17:00 had not.

The duplicate guard is a recency check rather than an output check, because the
screener has no equivalent of "today's report is published": it produces a fresh
answer every time it runs, and running twice would be wasteful rather than
wrong. `scripts/odd_lot.py slot` reads `last_run_at` out of
`state/odd_lot_universe.json`, which the previous run committed.

Both slots use the same 30-minute-early logic in **EST and EDT** — every arm is
covered by `tests/test_odd_lot_screener.py::Slots::test_each_cron_arm_lands_where_it_is_meant_to`,
which resolves all four crons to New York time in both regimes.

### Triggering it externally, alongside the report

Everything in [What actually fixes it](#what-actually-fixes-it) applies
unchanged — the same fine-grained token with **Actions: Read and write** works
for both workflows, because it is scoped to the repository rather than to a
workflow. Add three more cron-job.org entries next to the existing one:

| Title | Time (`America/New_York`) | Days |
| --- | --- | --- |
| `invest-trade-daily 6am ET` | 06:00 | every day |
| `odd-lot screener premarket` | 05:30 | every day |
| `odd-lot screener evening` | 18:30 | Mon–Fri |

The external times are the round ones, `05:30` and `18:30`; the GitHub crons sit
seven minutes later at `05:37` because `:00` and `:30` are the busiest minutes on
GitHub's scheduler. Either way the morning screen lands exactly thirty minutes
ahead of the report.

Each one is the same POST as before, with the workflow file name changed:

```
POST https://api.github.com/repos/kswodeck/invest-trade-daily/actions/workflows/odd-lot-screener.yml/dispatches
Accept: application/vnd.github+json
Authorization: Bearer <TOKEN>
Content-Type: application/json

{"ref": "main", "inputs": {}}
```

`204 No Content` means accepted. There is no `respect_window` input here: a
`workflow_dispatch` is treated as deliberate and runs whatever the hour, and the
two-hour recency guard is what makes it safe to repeat. If you want a dispatch
that *does* defer to the window, use `repository_dispatch` with type
`run-odd-lot-screener` instead — but that needs a Contents-scoped token, which is
the thing [the table above](#the-token-actions-not-contents) says not to hand to
a third party.

For the Cloudflare Worker route, add the arms to the same `wrangler.toml` and
switch on `event.cron`:

```toml
[triggers]
crons = [
  "0 10 * * *", "0 11 * * *",       # daily report, 06:00 ET
  "30 9 * * *", "30 10 * * *",      # odd-lot premarket, 05:30 ET
  "30 22 * * 1-5", "30 23 * * 1-5", # odd-lot evening, 18:30 ET
]
```

```js
const WORKFLOW = (cron) =>
  cron.startsWith("0 1") ? "daily-report.yml" : "odd-lot-screener.yml";
```

Both odd-lot arms fire every day; the gate drops whichever one is not the
intended hour in the current DST regime, in about fifteen seconds.

### If you only set up one external trigger

Set up the report's. The odd-lot screener degrades far more gracefully than the
report does: its output is a list of offers that are open for days or weeks, so
a screen delivered four hours late is four hours stale rather than wrong, and
the next slot picks it up. A trade report framed as the 6am pre-open view is a
lie if it is researched at noon, which is why that one has a hard cutoff and
this one does not.
