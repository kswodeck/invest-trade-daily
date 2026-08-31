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

A trigger from outside GitHub. The workflow accepts one:

```yaml
on:
  repository_dispatch:
    types: [run-daily-report]
```

Any scheduler that can make one HTTPS call at 06:00 America/New_York will do.
The call:

```
POST https://api.github.com/repos/kswodeck/invest-trade-daily/dispatches
Accept: application/vnd.github+json
Authorization: Bearer <TOKEN>
Content-Type: application/json

{"event_type": "run-daily-report"}
```

A `204` means accepted. The run starts within seconds, arrives at the gate as a
non-`schedule` event, and therefore proceeds regardless of the window — the
duplicate guard exists to stop the scheduler, not the operator.

### The token

A fine-grained personal access token, scoped to this repository only, with a
single permission: **Contents: read and write** — the `dispatches` endpoint is
gated on write access to the repo, not on an Actions permission. Give it an
expiry and a calendar reminder to rotate it; a dispatch that silently stops
working because a token expired is the same outage in a new costume.

Store it in whichever service makes the call. It never goes in this repo.

### Picking a scheduler

Anything that runs a daily HTTPS request and is itself punctual:

- A hosted cron service (cron-job.org, EasyCron and similar) — free tiers cover
  one daily call, and most let you set the timezone to America/New_York so DST
  is handled for you.
- A Cloudflare Worker on a cron trigger, or AWS EventBridge → Lambda. More
  moving parts, no per-service account to trust with a token.
- Any always-on machine you already run, via its own crontab. `TZ` in the
  crontab handles DST.

If the scheduler is UTC-only, it has the same DST problem GitHub does — declare
both arms (`0 10` and `0 11` UTC) and let the repo's gate drop the wrong one,
exactly as the in-repo crons do.

### Keeping the GitHub crons

Leave them. They cost nothing when the external trigger wins the race — the
gate sees a published report on the branch tip and skips in about ten seconds —
and they are the fallback if the external scheduler is the thing that breaks.
