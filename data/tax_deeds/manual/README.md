# Manual list drops

Several Texas constable offices publish their sale list only as a PDF, and this
repo carries no PDF dependency on purpose. Rather than pretend to parse one, such
a source fails with the path to put a hand-exported CSV here:

    data/tax_deeds/manual/<source_id>.csv

`<source_id>` is the `id` of the source in `config/tax_deeds.json` — e.g.
`ellis_auction.csv`. Column headers are matched by that source's `column_map`,
so they only have to *contain* the configured wording, not match it exactly.

A file here wins over the live fetch. Delete it once the county's own list is
parsing again, or the screener will keep reading a stale month.
