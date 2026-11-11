# Compliance log — week 2026-W46

Required by the `ola-compliance-review` skill: every verdict logged in the
week's folder. Content only — no client, enquiry or personal data belongs in
this repository.

## 10 November 2026 — the five carousels drafted for publication on 11 November

Reviewed against the skill's nine checks by a compliance agent that did not
draft the items. Every figure re-traced to primary source on the day of review
(gov.uk/statutory-sick-pay, gov.uk rates and thresholds 2026 to 2027,
gov.uk/tax-codes/emergency-tax-codes, gov.uk digital-platform guidance,
IEIM901630, CCA 1974 s.75, FSMA 2000 (Claims Management Activity) Order 2018).

| Item | Verdict |
|---|---|
| `cod-urgenta-taxa` — emergency tax codes | FIX |
| `vanzari-online-platforme` — platform reporting | FIX |
| `cheltuieli-deductibile` — self-employed expenses | FIX |
| `concediu-medical-ssp` — Statutory Sick Pay from 6 April 2026 | FIX |
| `plata-cu-cardul-75` — Consumer Credit Act section 75 | **BLOCK** |

### `plata-cu-cardul-75` — blocked, and why

The closing card and both caption sign-offs invite readers who may have a
section 75 claim to bring it to Ola:

* RO card 04 — "Nu știi unde se reclamă? / Scrie-ne și îți spunem ce pagini
  oficiale explică pasul următor."
* EN card 04 — "Not sure where to complain? / Message us and we will point you
  at the official pages that set out the next step."
* RO caption — "Nu știi unde se reclamă? / Ola Accountancy · 0330 133 1886"
* EN LinkedIn — "Not sure where to start? / 0330 133 1886"

Article 89F(2)(d) of the FSMA 2000 (Claims Management Activity) Order 2018
states that a financial services or financial product claim "includes a claim
made under section 75 of the Consumer Credit Act 1974". Article 89G makes
seeking out "persons who may have a claim" and identifying claims or claimants
a regulated claims management activity; article 89I covers advising a claimant
or potential claimant. Ola holds no FCA authorisation for claims management.
The item is built to draw WhatsApp enquiries into exactly that activity, and
no written inbox rule exists to stop a reply crossing into it — structurally
the same stop as `winter-fuel-35000` in W45.

Cards 01 to 03 are accurate and fully sourced. The subject can be published
with a closing card that signposts the Financial Ombudsman Service and
Citizens Advice and carries no invitation to contact Ola about the claim.

### What the review asks changed on the other four

* **Check 6, implied endorsement — a regression.** `vanzari-online` carries
  "Vânzări online · HMRC" and "Selling online · HMRC" as the kicker on cards
  01 and 04. This is the defect fixed on `marriage-allowance` in W45. Use
  "· gov.uk".
* **Check 1, unsourced authority.** Both `vanzari-online` captions rely on
  HMRC manual IEIM901630 for the "both tests" point, and the Romanian caption
  on it for the euro threshold, but the manual is in neither the source list
  nor the published "Sursă:" line. IEIM901630 reads "the total Consideration
  paid or credited did not exceed 2000 euros" and "Both tests must be met",
  which is what supports the cards' "cel mult 2.000 de euro" against the
  looser "less than 2,000 euros" on the gov.uk consumer page. Cite it.
* **Check 1, standing item 2 from W45 (a maximum must read as a maximum).**
  The `cod-urgenta` Google Business frame prints "35 days — how long HMRC can
  take to update it". The source says "up to 35 days".
* **Check 1, overstatement.** `concediu-medical` card 01 and caption say the
  first three days of sickness "nu se plăteau deloc" / "were unpaid". They
  carried no SSP; an employer's own scheme could pay them, as the same
  carousel's card 02 says.
* **Check 1, employment status.** The `cheltuieli` Romanian caption states
  flatly that an agency or umbrella worker "ești angajat". Agency workers are
  not necessarily employees — the firm's own SSP caption is careful here
  ("lucrătorii prin agenție pot avea dreptul"). The point that matters for
  expenses is PAYE, so say PAYE.
* **Check 2 and 3, the free-step claim.** Every one of the ten closing cards
  ends "Fără obligații." / "No obligation." No price appears anywhere in the
  batch, so this line is the only thing standing in for price information next
  to the phone number, while the first consultation is £120 incl. VAT. What
  each CTA actually offers is a genuinely light free step, so say so or delete
  the line; "no obligation" is about commitment and is being read as price.
* **Check 9, the disclaimer.** The `cod-urgenta` Google Business frame carries
  "General information, not personal advice." On a tax subject the standard
  line applies. The two non-accountancy subjects correctly depart from it:
  `concediu-medical` carries "Informații generale, nu consultanță juridică de
  muncă." / "General information, not employment law advice." and
  `plata-cu-cardul` "Informații generale, nu consultanță juridică." / "General
  information, not legal advice." Both match their subject rather than
  defaulting to "vorbește cu un contabil". Neither yet says where the reader
  should go instead.
* **Check 3, prices.** None of the five quotes a price, so the VAT-inclusive
  rule is not engaged and there is nothing to reconcile against the published
  fees of £120 incl. VAT for 30 minutes and £420 incl. VAT for 60 minutes.
* **Check 5, confidentiality.** Clean across all five. No names, handles,
  enquiry details or identifiable circumstances.
* **Immigration boundary.** Tested card by card and caption by caption across
  all five: clear. Nothing states or implies that a reader's entitlement turns
  on residence or immigration status. The S and C prefixes in `cod-urgenta`
  concern which UK rate table applies, not status. `concediu-medical` is
  correct not to attach any status condition to SSP, because there is none.

### Standing items raised for the principal

1. "Fără obligații." is template-level, not a drafting slip — it is on all ten
   closing cards. Fix it at the template as the disclaimer was fixed in W45.
2. W45's proposed editorial rule 5 — Ola publishes on tax and on the tax
   consequences of a benefit, but not benefit eligibility criteria — would
   catch `concediu-medical` cards 02 and 03 if it has been adopted. SSP has no
   public-funds or immigration gate, so it does not reproduce the Winter Fuel
   problem, but the principal should say whether rule 5 is in force.
3. W45 standing item 3 recurs: the Romanian copy is weaker than the English on
   three separate points again this week — "te-a mințit" for misrepresentation
   where the English says "misled you", the flat "ești angajat", and the word
   order of "scriu în loc «NONCUM»".
4. Two of these five subjects sit outside accountancy. `concediu-medical`
   handles it (payroll-facing CTA, subject-matched disclaimer).
   `plata-cu-cardul` does not, and consumer-credit claims need an authorisation
   decision before the subject is attempted again.
