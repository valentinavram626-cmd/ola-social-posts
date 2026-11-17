# Scope check — 24 posts for 18 November 2026

Checked against `/home/claude/ola-social-posts/briefs/check/bank.json` (`scope.nation`, `scope.who`,
`scope.excluded`, `scope.from_when`, `scope.automatic` / `how_to_claim`). No web, no gov.uk.

**Headline rule: PASS on all 24.** No `h1` on any brand names a nation.
"Birmingham" appears in two bham headlines (CTA cards) — a city, not a nation, so not a breach.

**bham loudly-wrong-brand check: PASS.** All eight bham schemes cover England
(DFG England/Wales/NI; surcharge England; SDLT England and NI; PSR Great Britain; VAT margin UK;
HEP England; single person discount England and Wales; Sure Start England and Wales).
Nothing on bham is a scheme England is outside of.

**en / ola nation check:** only one en/ola post has a `scope.nation` narrower than the whole UK —
`ola-attendance-allowance` (England and Wales). It names Scotland in a card body, but not Northern
Ireland. See fault 4.

**30 faults.** Numbered below, worst first within each post.

---

## bham-household-energy-payment (SOLO, brand=bham)

Nation verdict: scheme is England only, brand audience is England — **nation did not need naming,
and was not named. Correct.**

**Fault 1 — FROM WHEN DROPPED ENTIRELY.** No row, no h1, no ask carries a date.
Bank `from_when`: "Payments from January 2027. One-off, for the 2026-27 financial year only."
The card says "You can get £100 towards your energy bills" with rows for the amount, the bands, the
Direct Debit split and the exclusions — and nothing about when.
Reader consequence: a Birmingham household reads this on 18 November 2026 and believes the £100 is
available now. They ring the council, or walk into the Saltley office, to chase a payment that cannot
arrive for another two months; non-Direct-Debit households may also conclude the application window
is open when it is not. This is fact 5 of the five from the 3 November near-miss, lost again on the
same post.

**Fault 2 — ROW 3, exclusion list truncated.** Bank excludes "second homes, empty properties, and
households where the householder is not responsible for paying council tax (so many people in houses
in multiple occupation, and tenants whose landlord pays…)". The row gives "second homes, and where
the landlord pays". Empty properties are gone, and HMO residents are only reachable by inference
from "where the landlord pays".
Reader consequence: an owner of an empty property, and an HMO resident who pays rent inclusive of
council tax, both read themselves as eligible and expect £100 that will not come.

**Fault 3 — bands E to H route dropped.** Bank excluded: bands E to H are outside the core scheme,
"reachable only through the separate £100 million discretionary fund each council runs on its own
criteria." Nothing in the card says a band E to H household has any route at all.
Reader consequence: a band E household reads "bands A to D", concludes there is nothing for them, and
never asks their council about the discretionary fund — a £100 loss caused by an omission.

---

## en-lifetime-isa (SOLO, brand=en)

Nation verdict: bank nation is United Kingdom, ISAs not devolved — **nation did not need naming in a
row, and was not named. Correct.**

**Fault 4 — THE WITHDRAWAL CHARGE IS ABSENT FROM THE WHOLE POST.** The bank entry is titled
"Lifetime ISA: the 25% bonus **and the withdrawal charge**". Bank excluded: the charge-free route is
"not available to anyone who owns or has ever owned a home, nor to a cash purchase without a
mortgage, nor within 12 months of the first payment"; the 25% charge is on the whole amount
withdrawn, bonus and growth included. The card has three rows — 25% of £4,000, provider claims it,
anyone 40 or over excluded — and the words "charge", "25% charge", "£450,000" and "mortgage" appear
nowhere.
Reader consequence: the worst outcome in this set. A reader opens a Lifetime ISA on the strength of
"£1,000 a year added to your savings", later needs the money for anything other than a qualifying
first home, withdraws, and loses 25% of everything — ending with less than they paid in. The post
sells the bonus and hides the penalty attached to it.

**Fault 5 — every first-home condition dropped.** £450,000 price cap, mortgage required, conveyancer
or solicitor, 12 months since the first payment, never having owned a home, buy-to-let and second
properties excluded. None appear.
Reader consequence: a reader saving for a £500,000 London flat, a cash buyer, or someone who already
owns a home believes they are inside the charge-free route and is not.

**Fault 6 — "no paying in or bonus after age 50" dropped.** Bank: "Nobody can pay in or earn the
bonus after age 50." The row says the bonus is automatic; the ask only tells readers to open one
before 40.
Reader consequence: a reader at 39 plans "£1,000 a year" for 21 years to age 60. Eleven of those
years earn nothing.

---

## ola-alocatie-nevazatori (SOLO, brand=ola, lang=ro)

Nation verdict: bank nation is "United Kingdom" (same £3,250 everywhere) — **no nation needed in a
row, and none given. Correct on the nation rule.** The per-nation *test*, however, is the fault
below: the bank's own note says "Do not state a single test UK-wide."

**Fault 7 — ROW 3: the eligibility test is dropped in both its forms.** Bank `who` / `excluded`: in
England and Wales you must be registered with your local council as blind or severely sight impaired
and hold the certifying document — "being sight impaired / partially sighted but not registered as
severely sight impaired does not qualify"; in Scotland and Northern Ireland the test is that you
cannot do work for which eyesight is essential. The excluded row says only "alte dizabilități; nu
este ajutor social".
Reader consequence: a partially sighted reader in England who is not on their council's register
reads the row, sees nothing that excludes them, and claims an allowance they are not entitled to —
or, worse, a reader who *is* eligible in Scotland on the work test assumes they need a council
registration that Scotland does not use, and does not claim. The one fact that decides the claim is
the one fact missing.

**Fault 8 — "no tax, no gain" dropped.** Bank excluded: "Anyone who neither pays Income Tax nor has
an eligible spouse or civil partner to transfer it to gets no cash benefit from it."
Reader consequence: a registered reader living on benefits below the Personal Allowance expects
£3,250 of extra money, or at least a repayment, and gets nothing — and nobody has told them the
transfer to a spouse is where the value would have been.

---

## ola-cresa-fara-taxa (CAROUSEL, brand=ola, lang=ro and lang=en)

Nation verdict: bank nation is United Kingdom (HMRC scheme, NI parents apply on GOV.UK) — **no nation
needed in a card body, and none given. Correct.**
All four faults below are present in both the ro and the en variant.

**Fault 9 — CARD 1 and CARD 2: the disabled-child age limit dropped.** Bank `who`: a child aged 11 or
younger, "or 16 or younger if the child is disabled". Card 1 says 11 or under in both languages;
card 2 gives the £1,000 / £4,000 disabled figures without ever saying the age runs to 16.
Reader consequence: a parent of a disabled 14-year-old reads "11 or under" on the hook card, decides
the scheme is closed to them, and loses up to £4,000 a year.

**Fault 10 — CARD 3: fostered children and children who do not usually live with you dropped.** Bank
excluded, first clause: "You cannot claim where the child does not usually live with you, or for a
child you foster."
Reader consequence: a foster carer, or a separated parent whose child lives mainly with the other
parent, opens an account and pays in. The top-up is recoverable and the account has to be unwound.

**Fault 11 — CARD 3: the childcare bursary or grant exclusion dropped.** Bank excluded: "if you or
your partner get a childcare bursary or grant".
Reader consequence: a student-nurse or trainee household on a childcare bursary applies and is
refused, or claims and has to repay.

**Fault 12 — CARD 3: the National Insurance number and immigration-permission conditions dropped.**
Bank excluded: "People without a National Insurance number or the required immigration permission are
excluded", and `who` sets out the British/Irish citizenship, settled or pre-settled status, or
eVisa / residence card permission needed, for both partners.
Reader consequence: this is the ola brand, a Romanian-speaking audience. A reader whose partner has
no NI number, or whose status is not settled, pre-settled or otherwise shows access to public funds,
is the single most likely reader of this post to be refused — and the card says nothing to them.

---

## ola-attendance-allowance (CAROUSEL, brand=ola, lang=ro and lang=en)

Nation verdict: bank nation is "England and Wales" — narrower than the UK, on a brand that reaches
the whole UK, so **the limit had to appear in a card body. Partly met:** Scotland and Pension Age
Disability Payment are named in card 3 in both languages. **Northern Ireland is not.**
All three faults are present in both variants.

**Fault 13 — CARD 3: Northern Ireland dropped.** Bank nation: "Northern Ireland runs its own
Attendance Allowance through nidirect."
Reader consequence: a reader in Belfast sees Scotland carved out, takes that as the only exception,
and follows the GOV.UK route the post points at. Same benefit name, wrong administration — a wasted
application and a delayed claim.

**Fault 14 — the "must be claimed" fact is in no card body.** Bank `automatic: false`; `how_to_claim`:
apply online, or by posted form, or by ringing 0800 731 0122 — and the claim date depends on which
route, with a phone claim backdated to the call if the form is returned within 6 weeks. Card 1 says
only "poți primi" / "goes to people who"; the claim surfaces only obliquely in the card 4 CTA.
Reader consequence: the bank calls this "the single most under-claimed pensioner benefit". A reader
who does not understand that nothing arrives unless they apply, and that the route chosen decides the
start date, loses weeks of entitlement that a phone call would have secured.

**Fault 15 — CARD 3: immigration control and habitual residence dropped.** Bank excluded: "Anyone
subject to immigration control, unless a sponsored immigrant. Anyone not habitually resident in the
UK, Ireland, the Isle of Man or the Channel Islands."
Reader consequence: again the ola audience. A reader helping a parent who has recently joined them in
the UK, or who is subject to immigration control, is told to go and claim. The claim fails on a
condition the post never mentions.

---

## ola-petrecere-craciun-150 (CAROUSEL, brand=ola)

Nation verdict: bank nation UK-wide (s264 is a UK exemption) — **no nation needed, none given.
Correct**, both languages.

**Fault 16 — lang=ro, CARD 3: salary sacrifice dropped.** Bank excluded: "anything provided under a
salary sacrifice arrangement, which must be reported regardless". The en variant carries this in the
card 3 note; the ro variant does not.
Reader consequence: a Romanian-reading employer running the party through salary sacrifice treats it
as exempt and reports nothing. The benefit was reportable whatever it cost — a P11D failure and a
Class 1A liability.

**Fault 17 — lang=ro, CARD 3: entertaining customers and suppliers dropped.** Bank excluded: "it
gives no relief for entertaining customers or suppliers". The en variant states it plainly; the ro
variant does not mention customers or suppliers anywhere.
Reader consequence: a reader puts clients on the guest list and assumes £150 a head covers them too.
It does not, and mixing them in also muddies the per-head calculation the CTA offers to do.

**Fault 18 — lang=en, CARD 3: the self-employed carve-out dropped.** Bank excluded: "It does not
apply to self-employed sole traders or partners entertaining themselves — they have no employment to
exempt." The ro variant has this in the card 3 note; the en variant does not.
Reader consequence: a sole trader with no employees puts their own Christmas dinner through the books
as an exempt annual function. There is no employment to exempt, so the deduction is disallowed.

---

## bham-sdlt-second-property (CAROUSEL, brand=bham)

Nation verdict: England and Northern Ireland, brand audience England — **no nation needed anywhere,
and none named. Correct.** (Scotland's LBTT/ADS and Wales's LTT are rightly absent from a bham post.)

**Fault 19 — CARD 3: the recently-inherited small-share let-out dropped.** Bank excluded: "buyers who
hold only a small share in a recently inherited property".
Reader consequence: this one costs the reader money rather than HMRC. A Birmingham buyer who holds a
minor inherited share in a late parent's house believes they are caught, pays five extra points on a
£250,000 purchase — around £12,500 — and never asks whether the share was small enough to be ignored.

**Fault 20 — CARD 3: caravans, mobile homes and houseboats dropped.** Bank excluded, named
explicitly.
Reader consequence: a buyer of a park home or houseboat as a second property budgets for a surcharge
that does not apply, or pays it on a return nobody queries.

---

## ola-uniforma-deducere (SOLO, brand=ola, lang=ro)

Nation verdict: bank nation UK-wide (cash value differs by Scottish and Welsh rates) — **no nation
needed in a row, none given. Correct.** Minor, not counted: the £12 in the h1 is the 20% basic-rate
saving and is a few pence out for a Scottish starter-rate taxpayer; the bank treats the rate
difference as a value point, not a nation limit.

**Fault 21 — ROW 3: "ordinary everyday clothing is never allowable" dropped.** Bank excluded, final
clause. The excluded row covers only employer-paid costs and the self-employed.
Reader consequence: the commonest wrong claim on this exact relief. A reader who buys black trousers
and a plain shirt for work, with no logo and no protective function, claims a relief that does not
exist — on a post whose headline is about uniforms.

**Fault 22 — ROW: "no Income Tax paid, nothing back" dropped.** Bank excluded: "Anyone who paid no
Income Tax in the year claimed for gets nothing, because relief cannot exceed the tax paid." The row
offers four years of backdating with no such condition.
Reader consequence: a part-time reader earning below the Personal Allowance, or one with a gap year
of no earnings, claims four years back expecting four payments and gets nothing for the untaxed
years — after being told the office would "calculate the years behind".

---

## bham-sure-start-grant (SOLO, brand=bham)

Nation verdict: England and Wales, brand audience England — **no nation needed, none named. Correct.**
(Scotland's Pregnancy and Baby Payment is rightly absent from a bham post.)

**Fault 23 — h1 and rows narrow the qualifying benefits to Universal Credit alone.** Bank `who`:
"income-related Employment and Support Allowance, Pension Credit or Universal Credit (a Support for
Mortgage Interest loan may also qualify you)". The h1 says "on Universal Credit"; no row widens it.
Reader consequence: an expectant household on income-related ESA or Pension Credit — or a grandparent
claiming for a family member under 16 — reads the headline as a test they fail and never claims £500
they are entitled to.

**Fault 24 — the claim window's opening date dropped.** Bank `from_when`: "Claim window opens 11
weeks before the due date and closes 6 months after the birth." Only the closing half is given, in
the ask.
Reader consequence: a reader at four months pregnant brings the SF100 to the Birmingham office,
sends it, and it is refused as early. The six-month closing date they were given tells them nothing
about when to start.

---

## en-inheritance-nil-rate-band (SOLO, brand=en)

Nation verdict: United Kingdom, IHT not devolved — **no nation needed in a row, none given. Correct.**

**Fault 25 — the taper is dropped.** Bank excluded: the residence nil-rate band "is withdrawn
entirely once the net estate is large enough for the £1-for-£2 taper to exhaust it" (the £2,000,000
threshold is in the entry's figures and sources).
Reader consequence: precisely the reader this post attracts. An owner of a £2.4m estate counts on
£325,000 plus £175,000, and plans a will around an extra allowance that tapers away to nothing. The
estate value for the taper is also measured before spouse exemption and business or agricultural
relief, so estates that pay no tax can still lose it.

**Fault 26 — trust-held homes and lifetime gifts dropped.** Bank excluded: no residence nil-rate band
"where the home is left in a trust under which descendants do not become entitled at death (for
example they must first reach a stated age); or on lifetime gifts and transfers into trust, which
never attract it."
Reader consequence: a parent leaving the house in trust until children turn 25 believes the row
"[Excluded] homes left to siblings, nieces or nephews" does not touch them. It is the trust that
costs them the £175,000.

---

## ola-child-trust-fund (SOLO, brand=ola, lang=ro)

Nation verdict: UK-wide, HMRC administers across the UK — **no nation needed in a row, none given.
Correct.**

**Fault 27 — "HMRC does not pay out the money" dropped.** Bank excluded: "HMRC does not pay out the
money — it only names the provider, and you must then claim from that provider." The rows say
"[Prin HMRC] căutare gratuită, de la 16 ani" and nothing more.
Reader consequence: a reader runs the free search expecting £2,200 to arrive from HMRC, receives a
letter naming a provider instead, assumes something went wrong or that the money is gone, and stops
one step short — with the provider's own identity checks still to pass.

---

## bham-vat-margin-second-hand (CAROUSEL, brand=bham)

Nation verdict: UK-wide — **no nation needed, none named. Correct.** The Northern Ireland–EU margin
guidance in the bank's nation line has no bearing on a Birmingham audience.

**Fault 28 — CARD 3 note: the separate-rules list is cut back too far.** The note gives "Gold,
precious stones, cars, caravans and houseboats". Bank excluded also names unredeemed pawns,
auctioneers, agents, **hire purchase and part-exchange goods**, horses and ponies, joint purchases
and shares, and imports and exports, plus the Global Accounting Scheme for high-volume low-value
stock.
Reader consequence: part-exchange and hire purchase are everyday trade for the second-hand dealer
this post is aimed at, and an auctioneer or a selling agent reads nothing that excludes them. They
set up the stock book the card describes, run part-exchanges through the general scheme, and
under-declare VAT.

---

## en-pre-trading-expenses (CAROUSEL, brand=en)

Nation verdict: UK-wide — **no nation needed, none named. Correct.**

**Fault 29 — CARD 3: "already deductible in a later period" dropped.** Bank excluded: "anything that
will already be deductible in a post-commencement period, such as rent paid in advance".
Reader consequence: a reader who paid six months' rent or insurance up front before opening claims it
in full on day one and again as it is incurred — a double deduction in the first year's accounts.

---

## bham-disabled-facilities-grant (CAROUSEL, brand=bham)

Nation verdict: England, Wales and Northern Ireland with a different maximum in each, and no scheme
at all in Scotland. Brand audience is England, and the card quotes the England figure of £30,000 —
**no nation needed anywhere, and none named. Correct.** The Welsh £36,000, the Northern Irish £25,000
and the Scottish absence are rightly off a bham post.

**Fault 30 — CARD 3: the means-test outcome softened.** Bank excluded: a means-tested household "may
get only a contribution, or nothing, and has to pay towards the cost". The card says "A household
with means of its own may be asked to pay a share."
Reader consequence: "a share" reads as a part-payment on a grant that is otherwise coming. A
household that will in fact receive nothing commissions an occupational therapy assessment and
plans the work on that footing. Card 2's note does carry the £6,000 savings line, so the means test
itself is present — it is the "or nothing" that has gone.

---

## Posts with no faults

Each checked on all five points and on the nation rule.

| Post | Nation verdict |
|---|---|
| **ola-cadouri-mici-50** (ro and en) | UK-wide; not needed, not named. Correct. All four statutory conditions, the £300 close-company director cap, the rank-and-file carve-out, the whole-benefit-taxed trap and the 6 April 2016 start date are all present in both languages. |
| **ola-plata-hmrc-timp** (ro and en) | UK-wide, channels identical in all four nations; not needed, not named. Correct. Post Office, the 5-working-day new Direct Debit and the paying-in-slip condition are all on card 3. |
| **bham-council-tax-surcharge-2028** | England only, brand audience England; not needed, not named. Correct. £2m threshold, 2026 valuation date, April 2028 start, surcharge-on-top not a reband, non-residential excluded, nothing to claim — all present. |
| **bham-priority-services-register** | Great Britain, which covers England; not needed, not named. Correct. Every limb of the bank's "it does not cross over" exclusion is on the cards, including the network-operator register, the switch, dual-fuel, no money off the bill and water. |
| **en-gift-aid-carry-back** | UK-wide; not needed, not named. Correct. The amended-return bar, the enough-tax-paid condition, the no-return case and the 31 January 2027 date are all present. |
| **en-partnership-return** | UK-wide; not needed, not named. Correct. Sole traders, companies, company-partner and late-notice date changes, and the non-partner carve-out all present. |
| **en-vat-penalty-points** | UK; not needed, not named. Correct. First return, final return, one-off period and the pre-2023 surcharge regime all present. |
| **en-company-active-hmrc** | UK-wide, Corporation Tax not devolved; not needed, not named. Correct. HMRC must confirm dormancy, going quiet is not dormancy, setup steps are not trading, Companies House obligations survive — all present. |
| **bham-single-person-discount** | England and Wales, brand audience England; not needed, not named. Correct. Two countable adults, the student disregard, not means-tested and "you apply, it is not automatic" all present. |
| **en-starting-rate-savings** | UK; not needed, not named. Correct. The £17,570 cut-off, the partial band below it and the automatic application all present. |

Not counted as a fault, recorded for completeness: `ola-plata-hmrc-timp` drops the bank's note that
the weekend and bank-holiday "pay by the last working day before" rule does **not** apply to Faster
Payments or card payments. 31 January 2027 is a Sunday, so the rule is live — but the omission makes
the reader pay earlier, not later, so no reader is misled into a loss.

---

**Fault count: 30.**
Nation-rule faults: 1 (fault 13, Northern Ireland missing from `ola-attendance-allowance`).
Headline-nation breaches: 0.
Posts clean on all five points: 10 of 24.
