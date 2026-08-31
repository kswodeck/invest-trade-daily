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
