# fault-fact — figure check: 24 posts vs bank.json

Comparison only. Every card figure, date, duration, rate, form number and age limit was
matched against the mapped bank entry's `figures`, `scope` and `notes`.

## Faults

- **ola-cadouri-mici-50 (lang=ro), card 2 [step] "Dacă ești director"** — "cadourile scutite
  se opresc la £300 pe an fiscal, fiecare rămânând **sub £50**". Bank entry
  `trivial-benefits-exemption-employees-and-directors`: the £50 is the "maximum cost of
  providing a single benefit", and the exemption fails only for "any benefit costing **more
  than £50** to provide" — i.e. £50 exactly still qualifies. "sub £50" moves the boundary and
  also contradicts card 1 of the same post ("costă cel mult £50").

- **ola-cadouri-mici-50 (lang=ro), card 2 [step] "Dacă ești director"** — "Într-o **firmă
  mică** în care ești director, cadourile scutite se opresc la £300". Bank entry attaches the
  £300 cap to a **close company** ("where the employer is a close company and the recipient is
  a director or other office holder"), not to a small company. The EN variant of the same post
  says "In a close company"; the RO variant changes the condition on the figure.

- **ola-plata-hmrc-timp (lang=ro), card 2 [step] "Metodele rapide"** — "Faster Payments,
  aprobarea plății din aplicația băncii, CHAPS și cardul de debit online ajung în aceeași zi
  sau a doua zi, **inclusiv în weekend**". Bank entry
  `hmrc-payment-clearing-times-31-january` attaches "including weekends and bank holidays"
  only to Faster Payments; CHAPS is "**same working day** if you pay within your bank's
  processing times". The weekend condition is carried onto CHAPS, where the entry does not
  support it. The EN variant of the same post carries no weekend claim.

- **ola-uniforma-deducere, h1** — "Pentru uniforma de serviciu plătești cu **£12** mai puțin
  impozit." Bank entry `flat-rate-job-expenses-uniforms-tools` gives £12 as "actual tax saved
  on a £60 flat rate claim **at the 20% basic rate** — HMRC's own worked example" (notes: a
  higher-rate taxpayer saves £24). The card states £12 with no rate condition attached.

- **bham-sure-start-grant, ROW 2** — "[You apply] on form SF100, **signed by a midwife**".
  Bank entry `sure-start-maternity-grant-2026-27`, how_to_claim: form SF100 "signed by a
  **health professional** (for example using your MATB1)". The card narrows the condition on
  the form.

- **en-starting-rate-savings, ROW 1** — "[£5,000] in full **below £12,570** of other income".
  Bank entry `starting-rate-for-savings`: the full £5,000 is available where other income
  "**does not exceed**" the £12,570 Personal Allowance, and the band is reduced by £1 for every
  £1 of other income **above** it — so other income of exactly £12,570 still gets the full
  band. "below" moves the boundary.

- **ola-cresa-fara-taxa (lang=ro card 3 note; lang=en card 3 note)** — "trebuie să câștige
  £2.643,68 în 3 luni" / "must expect to earn £2,643.68 over three months". Bank entry
  `tax-free-childcare`: "£2,643.68 **before tax** over the next 3 months (£203.36 a week)".
  The gross-pay condition on the figure is dropped on both language variants.

## Clean (no figure fault found)

- ola-petrecere-craciun-150 (ro and en) — clean.
- ola-plata-hmrc-timp (en) — clean (£31 Jan, 11-character reference/10-digit UTR + K, Bacs 3
  working days, new Direct Debit 5 working days all match).
- ola-attendance-allowance (ro and en) — clean (£76.70 / £114.60 weekly, 6 months).
- ola-cresa-fara-taxa — clean apart from the fault above (£2/£8, £500 per 3 months, £2,000/yr,
  £1,000 and £4,000 disabled, £100,000, age 11, age 21 all match).
- bham-disabled-facilities-grant — clean (£30,000 England, under 18 carve-out, landlords,
  savings over £6,000, pre-approval work, OT assessment).
- bham-council-tax-surcharge-2028 — clean (£2m, 2026 assessment, April 2028, 28 October 2026
  Budget, 100% empty-homes premium at 12 months, business rates carve-out).
- bham-sdlt-second-property — clean (5 percentage points; 5/7/10/15/17% at £125,000,
  £250,000, £925,000, £1.5m; 17% company rate over £500,000; £40,000; 36 months).
- bham-priority-services-register — clean (free; two separate registers; no bill discount;
  switching drops you off; water separate).
- bham-vat-margin-second-hand — clean (one-sixth of the margin, £200/£500/£300 worked example,
  6 years and longer while unsold, VAT-registered, VAT-charged purchases barred).
- en-gift-aid-carry-back — clean (box 8 page TR 4, 31 January 2027, original return only).
- en-partnership-return — clean (£100 per relevant partner, second £100 after six months,
  31 January 2027, year to 5 April 2026, notice after 31 July 2026).
- en-vat-penalty-points — clean (2 annual / 4 quarterly / 5 monthly, £200 then £200, first and
  final return and one-off periods exempt, periods to 31 December 2022 on the old surcharge).
- en-company-active-hmrc — clean (3 months from the start of the accounting period).
- en-pre-trading-expenses — clean (7 years, run from commencement not incorporation, capital
  and stock carve-outs).
- ola-child-trust-fund — clean on figures (£2.200 average, over 750.000 accounts, age 16).
- ola-alocatie-nevazatori — clean (£3.250 for 2026-27, claimed from HMRC, not automatic).
- bham-household-energy-payment — clean (£100, bands A to D, automatic for Direct Debit payers
  only, second homes and landlord-paid excluded, £100m discretionary fund in SCOPE).
- bham-single-person-discount — clean (25%, must apply, two countable adults, students
  disregarded).
- en-inheritance-nil-rate-band — clean (£325,000, £175,000, IHT435, non-descendant exclusion,
  freeze to end of 2029-30).
- en-lifetime-isa — clean (£1,000 bonus, 25% of £4,000, provider claims it, under 40 only,
  £450,000 cap and 20%/29 October 2026 in SCOPE).

## Not counted as faults (flagged for the editor, outside the bank)

- "First consultation free, 30 minutes" appears on every card. It is a studio offer, not a
  figure in any bank entry, so it was not checked.
- ola-child-trust-fund, `ask`: "La biroul din Luton". A location claim, not a figure, and the
  bank holds nothing on it; every other `ola` post names no office and the `bham` posts name
  Birmingham. Verify against the brand's own office list.

**Faults found: 7**
