# `used` is stale — evidence for the 09:41 research run

Written by the evening Content Studio run of 21 November 2026, which scheduled
nothing because of what is recorded here.

## What happened

STEP 0 of the evening run claims subjects by the availability test the pipeline
defines: brand tag present, `recheck_after` not passed, and no date in `used`
within the last 12 weeks. On 21 November that test returned 122 available
entries for ola, 118 for bham and 136 for en.

The test was wrong. All nine carousels written that evening turned out to
duplicate posts already in `topics.py` — five of them the subjects sitting in
`DAY` right then (Small Business Rate Relief, Employment Allowance, Self
Assessment 31 January, the VAT registration thresholds, CIS monthly returns),
the rest with twins in `ARCHIVE` (trading allowance, the High Income Child
Benefit Charge, Tax-Free Childcare). The carousel pipeline began on 3 November
2026, so nothing in `ARCHIVE` is 12 weeks old: every one of those is a real
repeat, and the no-repeat rule is the rule that matters most.

## The measurement

`used-repair-2026-11-21.json` lists, for every bank entry, the published topic
it most likely corresponds to, by word overlap between the bank title/id and
the topic title/slug. Only matches at 0.5 overlap or better are listed, and the
list is ordered strongest first. Each row carries the entry's current `used`
value so the gap is visible.

- 112 of 192 bank entries match a topic already in `DAY`, `HELD`, `ARCHIVE` or
  `SOLOS`.
- **82 of those 112 have an empty `used` field.** The write-back after
  scheduling did not happen for them.
- The mechanism is not wholly broken: `marriage-allowance` (2026-11-20),
  `statutory-sick-pay` (2026-11-16) and `vat-annual-accounting-scheme`
  (2026-11-19) do carry dates. It has been missed far more often than it has
  been done.

The overlap figure is a heuristic, not a verdict. A high-overlap row is strong
evidence of a repeat; a row at 0.5-0.7 needs a human or the research run to
look at both before `used` is written.

## What this implies for volume

Once `used` is repaired, roughly 80 of 192 entries are genuinely unpublished,
and that is before the per-brand `brands` filter narrows it further. A night of
15 carousels and 9 single-image posts cannot be drawn from what is left. Either
the bank needs new subjects verified into it, or the nightly volume needs to
come down — that is a decision for Valentin, not for the evening run.

## What was deliberately NOT done here

No figure, source or scope block was touched. No `used` field was written: the
evening run did not use these entries, and writing `used` for a post that never
shipped would make this worse rather than better. `SOLOS` in `topics.py` was
left holding the previous night's nine entries, because nothing was rendered or
scheduled from it and the evening run could not read `SAFETY.md` (the private
ops repo is outside this session's GitHub scope) to check the rules for
changing a tracked file. Both are flagged for Valentin.
