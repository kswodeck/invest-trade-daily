# Tax deed list fixtures

These reproduce the *shape* each county publishes — column wording, money and
date formatting, the layout tables the real list sits inside, the aggregator
rows for counties we do not want, and the withdrawn/cancelled rows that must be
rejected rather than parsed cheerfully.

**They are hand-built structural fixtures, not archived captures.** They were
written from the column vocabulary in `config/tax_deeds.json`, because this
repo's runner cannot reach county hosts. That makes them a regression test for
the parsers, not proof that today's live page still looks like this. The thing
that catches a live format change is `python scripts/tax_deed_sources.py verify`,
which fetches each source and fails with the URL when its declared
`required_markers` or `column_map` no longer match.

When a county does change format: capture the new page here, add the case, then
fix `column_map` in the config — not the parser.
