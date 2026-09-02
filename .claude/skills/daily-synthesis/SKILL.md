---
name: daily-synthesis
description: Phase 2 of the daily trade report. Converts the research phase's notes.md into a schema-valid report.json, honestly reflecting whatever research actually completed.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

# Daily synthesis phase

Convert the research log into `reports/<date>/report.json`, valid against
`scripts/report_schema.json`.

```bash
DATE=$(TZ=America/New_York date +%F)
cat "reports/$DATE/candidates.jsonl"   # the real input
wc -c "reports/$DATE/notes.md"         # context and rejections
```

## Step zero: write a valid report before anything else

**Your first action is to write a schema-valid `report.json` with an empty
`recommendations` array.** Then improve it in place as you work.

You are on a timer too. A previous run read 38,000 characters of good research,
started reasoning about it, and was cut off having written nothing — turning a
strong research day into a total loss. A valid file on disk from minute one
means the worst case is a thin report instead of no report.

```bash
DATE=$(TZ=America/New_York date +%F)
python - <<PY
import json, pathlib
from datetime import datetime
from zoneinfo import ZoneInfo
p = pathlib.Path("reports/$DATE/report.json")
p.write_text(json.dumps({
    "date": "$DATE",
    "generated_at_et": datetime.now(ZoneInfo("America/New_York")).isoformat(timespec="seconds"),
    "truncated": True,
    "data_quality_notes": "Synthesis in progress.",
    "market_context": {"summary": "Synthesis in progress.", "regime": "unknown"},
    "recommendations": [],
}, indent=2))
print("skeleton written")
PY
```

Rewrite it with real content as soon as you have your first finished
recommendation, and again as you add each one. Do not hold the finished report
in your head until the end.

## Your job is to be a faithful editor, not a second researcher

The research phase may have been killed mid-sentence. Whatever is in `notes.md`
is what you have. You may re-read files and run `scripts/market_data.py` to fill
a missing current price or recompute a risk/reward ratio — that is it.

**Do not invent candidates, prices, catalysts, or sources that are not in the
notes.** If the notes contain three usable candidates, publish three. If they
contain zero, publish zero and explain why in `data_quality_notes`. An honest
thin report is a correct output. A padded report is a failure that will be
traded on.

## Steps

1. **Read `candidates.jsonl` first.** Each line is a validated candidate,
   already in report shape. Where a symbol appears more than once, the last
   entry wins — research captures improved versions as it goes.

   Then read `notes.md` and `prior_context.md` for context, rejections, and
   position updates. **`notes.md` uses whatever headings the research phase
   chose** — do not expect a fixed format, and do not skip material because it
   is not laid out the way you expected.

   If `candidates.jsonl` is missing or thin but `notes.md` is substantial, the
   research phase was cut off before consolidating. Reconstruct what you can
   from the notes: any finding with a symbol, a direction, a level, and a source
   is a usable recommendation. Say in `data_quality_notes` that you
   reconstructed it, and be honest that levels not set during research are
   weaker. Reconstructing beats publishing nothing — a full page of researched
   findings and an empty report is the one outcome to avoid.

   A `POSITION UPDATE` becomes a normal recommendation for that symbol, with the
   revised levels and a `thesis` that opens by naming it as an update to an open
   position — for example, *"Update to the 2026-08-05 long: thesis intact,
   raising the stop to 176."* Position updates do not count against the idea
   count; they are position management, not new risk.
2. **Filter.** Drop anything below conviction 2, anything missing the downside
   `config/strategy.md` requires for its horizon, and anything under its
   reward-to-risk floor — **1.5 intraday, 2.0 swing, 2.5 long_term**, where
   long-term risk is measured against a stated bear-case price rather than a
   stop. Enforce the correlation cap: at most 3 ideas depending on the same
   driver.

   **Do not filter or pad for horizon balance, and do not trim to a tidy
   count.** There are no per-horizon quotas and no target number — publish
   everything that clears the bar, up to the schema's 50. Whatever mix survives
   is the correct mix. Never drop a qualifying idea to make room for variety,
   and never promote a weak one to supply it.

   Conviction 2 ideas are published, marked as speculative and sized as lottery
   tickets. Check that each one's `key_risk` is honest about its thinness, and
   that `position_size_pct` respects the caps in `config/strategy.md` — 1% for
   conviction 2 or sub-$300M market caps, 2% for futures, 5% otherwise.

3. **Rank** by conviction, then reward-to-risk, using catalyst proximity only to
   break ties between ideas of the same horizon — a long-term thesis has no near
   catalyst by construction and must not be ranked down for it. If the best idea
   today is a multi-year hold, it ranks first.
4. **Refresh prices** for the finalists with
   `python scripts/market_data.py quote <symbols>` so `last_price` is as current
   as the run allows. Set `last_price: null` if it cannot be fetched.
5. **Recompute `risk_reward`** from the final entry, target, and downside rather
   than trusting the number in the notes — the stop for intraday and swing, the
   bear-case price for long-term. Drop any idea whose recomputed ratio falls
   below its floor.

   If several ratios land just above their floor, be suspicious: that is the
   signature of targets fitted to clear the bar rather than levels derived from
   the chart or a valuation. Say so in `data_quality_notes` if you see it.

   **Then check the stop the other way.** Pull `atr14` from
   `market_data.py history <symbol>` and confirm the stop clears the floor for
   this idea's horizon and asset class — 2.0 ATR for a swing stock, 1.8 for an
   ETF, 2.5 for crypto or futures, 1.0 for anything intraday. A ratio cleared
   by a tight
   stop is not cleared: the trade gets taken out by ordinary daily range before
   the thesis resolves, which is what happened to every one of the first ten
   closed positions. Do not fix this by moving the target — widen the stop and
   drop the idea if the ratio no longer holds.
6. **Carry `win_probability` and `evidence` through.** Both come from the
   candidate; neither is yours to invent, but both are yours to sanity-check.

   `win_probability` is the estimated chance the target is hit before the stop.
   Its baseline is `1 / (1 + risk_reward)` — the driftless random-walk
   probability, which is also the break-even hit rate. If a candidate arrives
   without one, set it from the notes' own reasoning if the notes support a
   number, and leave it out otherwise; validation warns rather than failing, and
   an invented probability is worse than a missing one.

   `evidence` is what conviction now rests on: the score must equal the number
   of *distinct* `kind` values listed, 1 kind for a 2 up to 4+ for a 5. If a
   candidate claims conviction 4 on two kinds of confirmation, publish it at 3.
   Lowering the score is the fix; dropping the idea is not.
7. **Write `report.json`** and validate it.
8. **Verify** before finishing:

```bash
python -c "
import json, jsonschema, pathlib, os
d = os.popen('TZ=America/New_York date +%F').read().strip()
r = json.loads(pathlib.Path(f'reports/{d}/report.json').read_text())
jsonschema.validate(r, json.loads(pathlib.Path('scripts/report_schema.json').read_text()))
print(f'valid — {len(r[\"recommendations\"])} recommendations')
"
```

Fix and re-validate until it passes. A schema-invalid file fails the publish
step and the morning produces nothing.

## Fields that carry the weight

**`catalyst.action`** is the field the reader acts on. It must say what to do
relative to the event: *enter before, wait for, trim into, avoid until*. When
the right move today is to not enter yet, set `catalyst.wait: true` — the
publisher marks it `⏸ WAIT` and holds it out of performance tracking.

**`entry.condition`** carries any precondition: `only if CPI prints above
consensus`, `only on a retest of 178 with volume`. Do not bury a condition in
the thesis where it will be missed.

**`thesis`** is two to three sentences, specific and falsifiable. Name the
mechanism. "AI tailwinds" is not a thesis; "three consecutive hyperscaler capex
raises with supply commentary pointing above consensus" is.

**`key_risk`** is the one thing most likely to break it, not a generic warning.
"Market could go down" is filler.

**`sources`** must be URLs actually visited during research. Never synthesize a
plausible-looking URL.

## Truncation and honesty

Set `truncated: true` if the notes lack a `RESEARCH COMPLETE` block — that means
the research phase was cut off. Then use `data_quality_notes` to say plainly
what that cost:

> Research phase hit its 60-minute cap during the falsification pass. Four
> candidates are fully specified; two others in the notes lacked stops and were
> dropped. Crypto and event markets were not reached this run.

Also record in `data_quality_notes`: sources that failed, prices that could not
be fetched, and why the idea count is what it is if it is below target.

This field is what makes the report trustworthy over time. Write it as though
the reader is deciding how much size to put on.
