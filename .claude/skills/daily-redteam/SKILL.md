---
name: daily-redteam
description: Phase 2b of the daily trade report. Adversarially reviews the synthesized recommendations, kills the weak ones, and fixes what is fixable, using the mechanical validation flags as a starting point.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebSearch, WebFetch
---

# Red team

Your job is to **attack today's recommendations**, not to admire them. You did
not write this report and you owe it nothing.

The phase that produced it had to generate and critique at the same time, under
a clock. That never works well: the falsification step is the first thing to get
squeezed, and an author is the worst judge of their own idea. You are the
separate pair of eyes.

```bash
DATE=$(TZ=America/New_York date +%F)
cat "reports/$DATE/report.json"
```

Each recommendation carries a `validation` block written by
`scripts/validate_report.py` — recomputed reward-to-risk, live price, ATR, and
the results of mechanical checks. **Those are facts, not opinions.** Start
there, then go further than arithmetic can.

## What to attack

For each recommendation, in order:

1. **Is the thesis actually falsifiable?** "AI demand stays strong" is a mood.
   "Hyperscaler capex guides revised up three quarters running" is a claim that
   can be checked and can be wrong. Vague theses get cut, not softened.

2. **Does the evidence support the direction?** Read the sources. Not the
   headlines — the sources. If a cited article says something weaker than the
   thesis claims, or says the opposite, that is a kill.

3. **Is the edge already priced?** The most common failure in this kind of
   report is recommending a well-known story. If a stock has run 30% into an
   obvious catalyst that every desk has written up, the asymmetry is gone even
   though the thesis is correct. Being right and being early are different.

4. **Is the level real?** A `validation` warning that a target sits beyond the
   ATR guide usually means the number was chosen to clear the reward-to-risk
   floor. Check whether entry, target, and stop correspond to actual support,
   resistance, or a defensible valuation — or whether they are round numbers
   dressed up.

   **`stop_distance` is the one to read first.** The reward-to-risk floor can
   be cleared by finding a better target or by moving the stop closer, and only
   one of those is work. Every one of this report's first ten stop-outs had a
   stop tighter than 1.6 ATR, and ideas shipped at 29:1 and 26.7:1 on stops of
   0.19-0.38 ATR — ratios that measure nothing. A `stop_distance` warning on an
   otherwise healthy-looking ratio means the ratio is an artifact. Widen the
   stop and recheck the reward-to-risk; if it no longer clears the floor, the
   idea never did.

5. **Does it beat a coin flip?** Read `expectancy` against
   `breakeven_probability` in the validation block. The baseline is
   `1 / (1 + R:R)` — simultaneously the driftless random-walk probability of
   touching the target first and the break-even hit rate — so every idea is
   implicitly claiming to beat it. Ask what specifically justifies the claimed
   edge. "Good setup" does not. A `claimed_edge` above 20 points needs a
   mechanism named in the thesis, or the probability comes down.

6. **Is conviction paid for?** `conviction_evidence` names the score the listed
   evidence actually supports. When it disagrees with the score claimed, lower
   the score — that is the fix, not a kill. Watch for the same confirmation
   listed twice under different `kind` values; distinct kinds are the whole
   point.

7. **What breaks it that nobody mentioned?** Look for the risk absent from
   `key_risk`: a lockup expiry, a competitor's earnings two days earlier, an
   index rebalance, a correlated macro print, a pending legal decision.

8. **Does it survive the correlation test?** Several ideas that all need the
   same rate path or the same sector to work are one position wearing different
   tickers. Say so, and cut the weakest of the cluster.

## What to do about it

Edit `reports/<date>/report.json` directly.

- **Kill** an idea by moving it to `watchlist` with a `note` saying exactly why
  it failed. Do not silently delete anything — a killed idea with a reason is
  useful; a vanished one is not.
- **Downgrade** `conviction` when the thesis holds but the evidence is thinner
  than claimed. This is the most common correct outcome.
- **Fix** levels, `key_risk`, or `counter_argument` when the idea is sound and
  the specifics are sloppy. Never fix a level by moving the target further out
  to rescue a reward-to-risk ratio; that is the exact thing you are here to
  catch.
- **Re-rank** whatever survives, and renumber `rank` from 1 with no gaps.

Record what you did in `data_quality_notes`, appended to what is already there:

> Red team cut LOWRR (target beyond 4 ATR with no support behind it) and
> downgraded BABA to conviction 3 (the cited note is a preview, not a data
> point). Six ideas remain.

## Calibration

**Cutting nothing is a legitimate outcome** — say so explicitly rather than
inventing a criticism to look diligent. Manufactured objections are as harmful
as missed ones, because they train the reader to ignore you.

**Cutting everything is also legitimate** on a genuinely bad day. An empty
report that says "nothing cleared the bar this morning" is more valuable than
six weak ideas, and far more valuable than six weak ideas with a red-team stamp
of approval on them.

Be hardest on the highest-conviction ideas. A 5 that is wrong does more damage
than a 3 that is wrong, because it will be sized larger.

## Finishing

Validate before you stop — a malformed file loses the whole morning:

```bash
DATE=$(TZ=America/New_York date +%F)
python -c "
import json, jsonschema, pathlib
r = json.loads(pathlib.Path(f'reports/$DATE/report.json').read_text())
jsonschema.validate(r, json.loads(pathlib.Path('scripts/report_schema.json').read_text()))
print(f'valid — {len(r[\"recommendations\"])} recommendations survive')
"
```

You are on a short clock. If you can only get through some of the list,
prioritise the top-ranked ideas — they carry the most weight and the most size.
Leave the rest untouched rather than skimming everything shallowly.
