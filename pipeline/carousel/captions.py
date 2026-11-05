#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Caption text per topic, per network. Language follows the network rule.

Romanian — Instagram, Facebook, Threads, TikTok
English  — LinkedIn, Bluesky, Pinterest, Google Business

The four brand tags go on every post in both languages. Bluesky is the one
place they crowd the message: the API caps a post at 300 characters and the
brand tags alone are 85 of them, so Bluesky carries the brand tags and no
topical tags. assert_lengths() proves every Bluesky caption fits before
anything is scheduled.
"""
import topics
from topics import BRAND_TAGS, PHONE, tags

WA_RO = f"Scrie-ne pe WhatsApp: {PHONE}\nLuton · Birmingham"

# ola-compliance-review check 9: the disclaimer goes on educational posts. The
# Romanian wording is fixed by the skill. Bluesky caps a post at 300 characters
# and the brand tags take 85 of them, so English Bluesky uses the short form.
DISC_RO = "Informații generale. Pentru situația ta, vorbește cu un contabil."
DISC_EN = "General information. For your own situation, speak to an accountant."
DISC_SHORT = "General information, not personal advice. Speak to an accountant."
WA_EN = f"Ola Accountancy — Luton and Birmingham\n{PHONE}"

C = {}

# ------------------------------------------------------------------ 1
C["plati-in-avans"] = dict(
 ro="""Pe 31 ianuarie 2027 nu plătești doar taxa pe 2025/26.

HMRC îți cere în aceeași zi și prima tranșă în avans pentru anul următor: jumătate din taxa datorată anul trecut. A doua tranșă vine pe 31 iulie 2027.

Asta înseamnă că factura din ianuarie poate fi de o dată și jumătate cât arată declarația. Pentru mulți, e o surpriză în primul an pe cont propriu — dar e previzibilă, dacă știi că vine.

Ce intră în avans: și Class 4 National Insurance, dacă lucrezi pe cont propriu.
Ce nu intră: Capital Gains Tax și împrumutul studențesc — acelea apar doar în plata de regularizare.

Cine nu plătește avans deloc: dacă taxa datorată anul trecut a fost sub £1.000, sau dacă peste 80% din ea s-a reținut deja la sursă (prin codul fiscal sau de către bancă).

Se aplică în tot Regatul Unit. HMRC calculează avansul automat, din cifra de anul trecut — nu ceri nimic ca să apară. Dacă te aștepți la un an mai slab, poți cere reducerea avansului (formular SA303); dar dacă reduci prea mult, HMRC percepe dobândă pe diferență.

Nu ești sigur cât ai de plătit în ianuarie?""",
 li="""31 January 2027 is not only the 2025/26 liability.

On the same day HMRC also wants the first payment on account for the year ahead — half of last year's tax. The second instalment follows on 31 July 2027.

So the January figure can be one and a half times what the return itself shows. It catches a lot of people in their first year of self-employment, and it is entirely predictable once you know it is coming.

Inside the instalments: Class 4 National Insurance, for the self-employed.
Outside them: Capital Gains Tax and student loan repayments, which sit in the balancing payment instead.

Outside the regime altogether: anyone whose tax owed last year was under £1,000, and anyone who had more than 80% of it deducted at source. Those taxpayers make no payments on account at all.

UK-wide. HMRC calculates the instalments automatically from last year's figures — nothing is claimed to create them. If you expect a lower year you can claim to reduce them (form SA303), but reduce them too far and HMRC charges interest on the difference.

Want the January figure checked before it lands?""",
 bsky="""31 January 2027 is not just last year's tax — it carries the first payment on account too, half of last year's bill. Second: 31 July.""",
 pin_title="Why a UK January tax bill is bigger than the return",
 pin="""Why a UK Self Assessment bill due 31 January is often more than the return shows: the first payment on account adds half of last year's tax, and a second instalment follows on 31 July. The instalments include Class 4 National Insurance but not Capital Gains Tax or student loan, which sit in the balancing payment. No payments on account at all if last year's tax was under £1,000 or more than 80% was deducted at source. UK-wide, calculated by HMRC rather than claimed. Ola Accountancy, Luton and Birmingham.""",
 source="gov.uk/understand-self-assessment-bill/payments-on-account",
)

# ------------------------------------------------------------------ 2
C["mtd-income-tax"] = dict(
 ro="""Making Tax Digital pentru Income Tax nu vine pentru toți în același an. Vine în trepte — și pragul se judecă după o declarație pe care ai depus-o deja.

Din 6 aprilie 2026: venit peste £50.000 în declarația 2024/25.
Din 6 aprilie 2027: venit peste £30.000 în declarația 2025/26 — exact cea cu termen 31 ianuarie 2027.
Din 6 aprilie 2028: pragul coboară la £20.000, după declarația 2026/27.

Ce se numără: venitul brut, înainte de cheltuieli, din activitate independentă și din chirii, adunate. Nu profitul.

Cine nu intră: dacă nu ai venit nici din activitate independentă, nici din chirii — doar salariu, pensie, dividende sau economii — MTD pentru Income Tax nu te privește, oricât ai câștiga. Dividendele din propria firmă nu se numără, nici salariul, nici pensia. Nici partea ta de profit din parteneriat nu se numără la venitul de referință. Și nici cei sub pragul treptei, sau cei care nu sunt înregistrați pentru Self Assessment.

Se aplică în tot Regatul Unit și devine obligatoriu la depășirea pragului, dacă nu ai o scutire. Unele scutiri se aplică automat, altele se cer.

Vrei să știi în care treaptă intri și din ce dată?""",
 li="""Making Tax Digital for Income Tax does not arrive for everyone at once. It arrives in stages, and each stage is decided by a return you have already filed.

From 6 April 2026: qualifying income over £50,000 on the 2024/25 return.
From 6 April 2027: over £30,000 on the 2025/26 return — the one due 31 January 2027.
From 6 April 2028: over £20,000 on the 2026/27 return.

What counts is qualifying income: total turnover from self-employment and property, added together, before expenses. Not profit — a business can be comfortably under on profit and well over on turnover.

Who it does not reach: anyone with no sole-trade and no property income. Employment, pension, dividend or savings income alone keeps you outside MTD for Income Tax however large it is — dividends from your own company included. A partner's share of partnership profit does not count towards qualifying income either. Nor does being under the threshold for that stage, or not being in Self Assessment at all.

UK-wide, and mandatory by threshold rather than on request — unless an exemption applies. Some exemptions are automatic, others have to be applied for.

Not sure which stage you fall into?""",
 bsky="""MTD for Income Tax:
Apr 2026 — over £50,000 (2024/25 return)
Apr 2027 — over £30,000 (2025/26)
Apr 2028 — over £20,000 (2026/27)""",
 pin_title="Making Tax Digital for Income Tax: thresholds and dates",
 pin="""When Making Tax Digital for Income Tax applies to you, and which return decides it. From 6 April 2026 for qualifying income over £50,000 on the 2024/25 return; from 6 April 2027 for over £30,000 on the 2025/26 return; from 6 April 2028 for over £20,000 on the 2026/27 return. Qualifying income is total turnover from self-employment and property before expenses, not profit. Anyone with no sole-trade and no rental income stays outside it entirely. UK-wide. Ola Accountancy, Luton and Birmingham.""",
 source="gov.uk/guidance/use-making-tax-digital-for-income-tax/introduction and gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax",
)

# ------------------------------------------------------------------ 3
C["tva-prag-90000"] = dict(
 ro="""Pragul de TVA e £90.000. Partea care încurcă nu e cifra — e perioada.

Nu e anul fiscal. Nu e anul calendaristic. Sunt ultimele 12 luni, recalculate la sfârșitul fiecărei luni. Un trimestru bun în vară te poate duce peste prag în octombrie, pe o perioadă care nu seamănă cu niciun an de pe hârtie.

Două teste, nu unul:

Privirea în urmă — dacă totalul pe ultimele 12 luni trece peste £90.000, ai 30 de zile de la sfârșitul lunii respective să te înregistrezi. Înregistrarea intră în vigoare din prima zi a celei de-a doua luni după depășire.

Privirea în față — dacă te aștepți să depășești £90.000 în următoarele 30 de zile, te înregistrezi până la sfârșitul acelei perioade. Aici data de start e ziua în care ți-ai dat seama, nu ziua depășirii.

Ieșirea: poți cere anularea înregistrării dacă poți arăta HMRC că te aștepți să stai sub £88.000 în următoarele 12 luni. Nu se judecă după cele 12 luni trecute, ci după următoarele. Pragul de ieșire e mai mic decât cel de intrare.

Cine nu are obligația: dacă cifra taxabilă pe ultimele 12 luni rămâne la sau sub £90.000 și nu te aștepți să depășești în 30 de zile, nu ești obligat — înregistrarea voluntară rămâne o opțiune. Atenție: cifrele sunt pe vânzări taxabile, nu pe profit.

O excepție care prinde mulți: dacă afacerea ta e stabilită în afara Regatului Unit și face vânzări taxabile în UK, pragul de £90.000 nu ți se aplică deloc — te înregistrezi de la prima liră. Există și excepții, de exemplu când tot ce vinzi e cu cotă zero, așa că merită verificat pe cazul tău.

Se aplică în tot Regatul Unit. Înregistrarea e obligația ta, pe termen — HMRC nu te anunță.

Te apropii de prag?""",
 li="""The VAT registration threshold is £90,000. The number is not what catches people out — the period is.

It is not the tax year and not the calendar year. It is the last 12 months, recalculated at the end of every month. A strong summer quarter can push a business over the threshold in October, across a twelve-month window that matches no set of accounts anyone has ever looked at.

There are two tests, not one.

The backward look: once taxable turnover for the last 12 months passes £90,000, you have 30 days from the end of that month to register. Registration takes effect from the first day of the second month after you went over.

The forward look: if you expect to pass £90,000 in the next 30 days, you register before that period ends. Here the effective date is the day you realised, not the day turnover crossed — which is the part that surprises people, because it can sit earlier than the crossing itself.

Coming back out: you can apply to deregister if you can satisfy HMRC that your taxable turnover in the next 12 months will not exceed £88,000. It is a forward-looking test, not a look at the twelve months just gone. The exit threshold sits lower than the entry one.

Who has no obligation: a business whose rolling 12 months of taxable turnover stays at or below £90,000 and which does not expect to cross in the next 30 days. Voluntary registration remains available, but it is a choice. These are taxable turnover figures, not profit.

One exception that catches people: if your business is established outside the UK and makes taxable supplies here, the £90,000 threshold does not apply to you at all — you register from the first pound. There are exceptions, zero-rated supplies among them, so it is worth checking against your own supplies rather than assuming either way.

UK-wide, and registering is the business's own duty on a deadline — HMRC does not prompt it.

Heading for the threshold?""",
 bsky="""UK VAT threshold: £90,000 of taxable turnover over a rolling 12 months, recalculated every month end. Two tests — backward and forward look.""",
 pin_title="UK VAT threshold £90,000: the two tests explained",
 pin="""The UK VAT registration threshold is £90,000, measured over a rolling 12 months recalculated at every month end — not the tax year or the calendar year. Backward look: once the last 12 months pass £90,000, register within 30 days of that month's end, effective from the first day of the second month after. Forward look: if you expect to pass £90,000 within the next 30 days, register before that period ends, effective from the day you realised. Deregistration threshold £88,000, judged on expected turnover for the next 12 months. Turnover, not profit. Ola Accountancy, Luton and Birmingham.""",
 source="gov.uk/register-for-vat, gov.uk/how-vat-works/vat-thresholds, VAT Notice 700/1 and VAT Notice 700/11",
)

# ------------------------------------------------------------------ 4
C["marriage-allowance"] = dict(
 ro="""Marriage Allowance valorează până la £252 pe an și se poate cere retroactiv pe patru ani.

Cum funcționează: cel care câștigă mai puțin transferă £1.260 din alocația personală către celălalt. Rezultatul e o reducere de impozit de până la £252 pe an fiscal — maximul, nu o sumă garantată.

Condițiile: unul dintre voi trebuie să aibă venitul sub alocația personală, de regulă £12.570. Celălalt trebuie să fie plătitor de rată de bază — de obicei între £12.571 și £50.270. În Scoția, partenerul care primește transferul trebuie să fie pe rata starter, de bază sau intermediară, între £12.571 și £43.662.

Retroactiv: cererea se poate întinde până la 6 aprilie 2022, adică anul fiscal 2022/23 — dar numai pentru anii în care amândoi ați îndeplinit condițiile.

Cine NU se califică: cuplurile care locuiesc împreună fără să fie căsătorite sau în parteneriat civil nu pot cere deloc. E o excludere care surprinde multe cupluri. Nici cuplurile în care amândoi sunt peste alocația personală, nici cele în care cel care câștigă mai mult plătește rata superioară. Și nu se poate avea în același timp cu Married Couple's Allowance.

Se aplică în tot Regatul Unit. Nu vine automat — trebuie cerută.

Credeți că vi se aplică?""",
 li="""Marriage Allowance is worth up to £252 a year and can be backdated four years.

How it works: the lower earner transfers £1,260 of their Personal Allowance to their partner. The result is up to £252 off the higher earner's tax in a tax year — the maximum, not a fixed amount.

The conditions: one of you has income below the Personal Allowance, usually £12,570. The other pays the basic rate, usually between £12,571 and £50,270. In Scotland the receiving partner must be on the starter, basic or intermediate rate, between £12,571 and £43,662.

Backdating: a claim can reach back to 6 April 2022 — the 2022/23 tax year — but only for the years both conditions were met.

Who does not qualify: couples living together who are not married and not in a civil partnership cannot claim at all. It is an exclusion that surprises a lot of couples. Nor can couples where both are above the Personal Allowance, or where the higher earner is a higher-rate taxpayer. And it cannot be held at the same time as Married Couple's Allowance.

UK-wide, and it never arrives automatically — it has to be claimed.

Think it applies to you?""",
 bsky="""Marriage Allowance: up to £252 a year, backdatable to 2022/23. One under £12,570, the other basic-rate. Cohabiting couples cannot claim.""",
 pin_title="Marriage Allowance: £252 a year and four years back",
 pin="""UK Marriage Allowance explained: the lower earner transfers £1,260 of Personal Allowance to their partner, cutting the higher earner's tax by up to £252 a tax year. One partner must be below the Personal Allowance (usually £12,570) and the other a basic-rate payer; in Scotland the starter, basic or intermediate rate. A claim can be backdated to 6 April 2022. Couples living together who are not married or in a civil partnership cannot claim at all. UK-wide, and it must be claimed. Ola Accountancy, Luton and Birmingham.""",
 gbp="""Marriage Allowance is worth up to £252 a year, and you can still backdate a claim four years.

The lower earner transfers £1,260 of their Personal Allowance to their partner. One of you needs income below the Personal Allowance, usually £12,570; the other needs to be a basic-rate taxpayer. In Scotland the receiving partner must be on the starter, basic or intermediate rate.

A claim can reach back to 6 April 2022, for any year you both met the conditions.

Who cannot claim: couples living together who are not married or in a civil partnership. It is an exclusion that surprises a lot of couples. It also cannot be held alongside Married Couple's Allowance.

It applies across the UK, and it is never paid automatically — it has to be claimed.

Married or in a civil partnership with one of you under £12,570? Call or message 0330 133 1886 and we will check whether it applies and which years are still open.

Ola Accountancy — Luton and Birmingham.

Source: gov.uk/marriage-allowance""",
 source="gov.uk/marriage-allowance",
)

# ------------------------------------------------------------------ 5
C["winter-fuel-35000"] = dict(
 ro="""Winter Fuel Payment pentru iarna 2026/27 e între £200 și £300 pentru cei care locuiesc singuri. Vine automat, cu o scrisoare în octombrie sau noiembrie. Partea despre care se vorbește puțin e că nu rămâne la toți.

Cât și pentru cine: £200 pentru cei născuți la 27 iunie 1960 sau înainte; £300 dacă sunt născuți înainte de 28 septembrie 1946. Sumele sunt mai mici când locuiești cu un alt beneficiar sau într-un azil. Totul se judecă după săptămâna de referință, 21-27 septembrie 2026.

Unde: Anglia, Țara Galilor și Irlanda de Nord. Scoția NU e inclusă — acolo există o plată proprie, Pension Age Winter Heating Payment, de la Social Security Scotland.

Peste £35.000: dacă venitul tău personal depășește £35.000, HMRC îți ia plata înapoi, integral — prin codul fiscal sau prin declarația de Self Assessment. Se judecă venitul fiecăruia separat, nu al gospodăriei. Doi pensionari cu £30.000 fiecare păstrează ambele plăți; un singur pensionar cu £36.000 nu păstrează nimic.

Cine nu o primește deloc: cei care locuiesc de obicei în afara Angliei, Țării Galilor și Irlandei de Nord; cei care au fost în închisoare toată săptămâna de referință; cei internați pe tratament gratuit toată săptămâna de referință și anul dinainte; și unii rezidenți de azil care primesc Pension Credit, Universal Credit sau ESA pe bază de venit.

Dacă nu a venit: majoritatea o primesc automat. Dacă nu ai primit-o niciodată, sau ți-ai amânat pensia de stat de la ultima plată, trebuie să o ceri — termenul pentru iarna 2026/27 este 31 martie 2027.

Nu știi dacă va trebui să o dai înapoi?""",
 li="""The Winter Fuel Payment for winter 2026/27 is £200 to £300 for someone living alone. It arrives automatically, with a letter in October or November. What gets far less attention is that not everyone keeps it.

How much, and who: £200 for those born on or before 27 June 1960; £300 if born before 28 September 1946. Lower amounts apply where you live with another eligible person or in a care home. Everything is judged on the qualifying week, 21 to 27 September 2026.

Where: England, Wales and Northern Ireland. Scotland is NOT covered — there is a separate Scottish benefit, Pension Age Winter Heating Payment, from Social Security Scotland.

Over £35,000: if your own income passes £35,000, HMRC recovers the whole payment, through your PAYE tax code or your Self Assessment return. It is assessed on each person's income individually, not on the household's. Two pensioners on £30,000 each keep both payments; one pensioner on £36,000 keeps nothing.

Who does not get it at all: people who usually live outside England, Wales and Northern Ireland; people in prison for the whole qualifying week; people in hospital on free treatment for the whole qualifying week and the year before it; and some care-home residents receiving Pension Credit, Universal Credit or income-related ESA.

If it never arrived: most people are paid automatically. If you have never had it, or have deferred your State Pension since your last payment, you have to claim — and the deadline for winter 2026/27 is 31 March 2027.

Unsure whether you will have to pay it back?""",
 bsky="""Winter Fuel Payment 2026/27: England, Wales and NI only — Scotland has its own. Own income over £35,000? HMRC takes it back, judged per person.""",
 pin_title="Winter Fuel Payment 2026/27: who keeps it, who repays it",
 pin="""Winter Fuel Payment for winter 2026/27: £200 for those born on or before 27 June 1960 and £300 if born before 28 September 1946, for someone living alone, based on the qualifying week of 21 to 27 September 2026. It covers England, Wales and Northern Ireland only — Scotland has its own Pension Age Winter Heating Payment. If your own income passes £35,000, HMRC recovers the whole payment through your tax code or Self Assessment, assessed per person rather than per household. Most are paid automatically; anyone who has never had it must claim by 31 March 2027. Ola Accountancy, Luton and Birmingham.""",
 source="gov.uk/winter-fuel-payment and gov.uk/guidance/paying-back-the-winter-fuel-payment",
)

# ------------------------------------------------------------------ 6
C["cis-20-30"] = dict(
 ro="""În construcții, firma care te plătește nu îți dă toți banii din factură. Oprește o parte și o trimite la HMRC în numele tău. Asta e CIS — Construction Industry Scheme.

Cât oprește depinde de un singur lucru:
• Înregistrat la CIS → 20%
• Neînregistrat → 30%
• Cu „gross payment status" → 0%, primești tot și plătești taxa la final

Banii opriți nu sunt pierduți. Contează ca plată în avans pentru taxa și National Insurance pe care le datorezi. Dacă s-a oprit mai mult decât datorezi, diferența se returnează.

Cum se recuperează depinde de forma în care lucrezi: pe cont propriu, prin declarația anuală; cu firmă (Ltd), prin payroll, cu un Employer Payment Summary. HMRC spune explicit să NU folosești declarația de Corporation Tax — riști o penalizare.

Din ce NU se oprește nimic: din TVA, din materialele pe care le-ai plătit tu, din combustibilul folosit pe șantier (nu cel de drum), din utilajele închiriate pentru lucrare și din costul de fabricație al materialelor. Se oprește doar din munca ta.

Cine nu intră deloc: angajații. Un contract de muncă e exclus din CIS, deci din salariu nu se oprește nimic pe CIS.

Atenție la o confuzie des întâlnită: în afara CIS sunt doar serviciile de pe șantier — paznicii angajați ca pază, bucătăria, cabinetul medical. Construirea acelor facilități, montarea rulourilor de siguranță sau săpatul pentru stâlpii de camere SUNT în CIS.

Firma trebuie să îți dea o chitanță de plată și deducere în 14 zile de la sfârșitul lunii fiscale. Păstreaz-o: e dovada ta.

Se aplică în tot Regatul Unit. Înregistrarea e gratuită și e pasul tău — nimeni nu o face în locul tău.

Nu știi dacă ești înregistrat sau cât ți s-a oprit?""",
 th="""Ți se opresc 30% din plată în construcții? De obicei înseamnă că nu ești înregistrat la CIS — sau că firma nu te-a putut verifica la HMRC. Înregistrat, se opresc 20%.

Angajații nu intră deloc în CIS. Nici din TVA și nici din materialele plătite de tine nu se oprește nimic.""",
 li="""The Construction Industry Scheme decides how much of a subcontractor's invoice actually reaches them.

The rate turns on one fact:
• Registered for CIS — 20% deducted
• Not registered — 30% deducted
• Gross payment status — 0%, paid in full, tax settled later

The deduction is not a cost. It is an advance payment against the subcontractor's Income Tax and National Insurance. Where the deductions exceed the tax and National Insurance due, the difference is repaid.

How it is recovered depends on the trading form, and this one is worth getting right: a sole trader or partner offsets it through Self Assessment, while a limited company recovers it through its payroll scheme on an Employer Payment Summary. HMRC's instruction is explicit — "Do not use your Corporation Tax return to pay tax with your deductions - you may get a penalty if you do."

The rate applies to labour only. Before it is calculated, a contractor takes out VAT, materials the subcontractor paid for, consumable stores, fuel other than travel fuel, plant hire paid to a third party, and the cost of manufacturing or prefabricating materials.

Outside the scheme altogether: employees. A contract of employment is excluded, so nothing is deducted under CIS from a wage.

One distinction that catches people: what is excluded is the RUNNING of site facilities — canteens, hostels, offices, toilets, medical centres — and the supply of security guards. Constructing those facilities is within the scheme, as is most physical security work: erecting CCTV posts, fitting security shutters, putting up site hoardings.

The contractor must issue a payment and deduction statement within 14 days of the end of the tax month. It is the subcontractor's evidence; without it the offset is an argument rather than a record.

UK-wide. Registration is free and is the subcontractor's own step — nobody does it for them, and the 30% rate is what happens when it is not done.

Want your CIS deductions checked against your return?""",
 bsky="""CIS: 20% deducted if you are registered, 30% if not. Employees are outside it entirely.""",
 pin_title="UK CIS: 20% or 30% off a subcontractor's pay",
 pin="""Why a UK construction subcontractor gets 20% or 30% deducted from their pay under the Construction Industry Scheme: 20% if registered with HMRC, 30% if not, and 0% with gross payment status. The deduction is an advance payment against Income Tax and National Insurance. Nothing is deducted from VAT, from materials the subcontractor paid for, from plant hire or from fuel other than travel fuel. Employees are outside CIS entirely, as is running a site canteen and the supply of security guards — but constructing site facilities and most physical security work are inside it. UK-wide; registration is free. Ola Accountancy, Luton and Birmingham.""",
 gbp="""Working in construction and wondering why 30% comes off your pay instead of 20%?

Under the Construction Industry Scheme a contractor deducts 20% from a subcontractor who has registered with HMRC, 30% from one who has not, and nothing at all from a subcontractor with gross payment status. The difference between the first two is 10% of every single payment, and registering is free.

The money is not lost either way: it is an advance payment against your Income Tax and National Insurance. Nothing is deducted from VAT, from materials you paid for, or from plant hire. Employees are outside the scheme completely.

Ola Accountancy works with construction subcontractors in Luton and Birmingham. Send us your payment and deduction statements and we will check what has been taken and how it comes off your tax.""",
 source="gov.uk/what-you-must-do-as-a-cis-subcontractor · CIS340 Appendix C",
)

# ------------------------------------------------------------------ 7
C["taxa-prin-codul-fiscal"] = dict(
 ro="""Dacă ai taxă de plătit la Self Assessment și în același timp ai salariu sau pensie, nu ești obligat să scoți toată suma pe 31 ianuarie. HMRC o ia din salariu, puțin câte puțin, prin codul fiscal — automat, dacă te încadrezi. Nu ceri nimic.

Trei condiții, toate trei obligatorii:
• Datorezi sub £3.000
• Plătești deja impozit prin PAYE — salariu sau pensie
• Depui declarația online până pe 30 decembrie 2026

Termenul pe hârtie a fost 31 octombrie și a trecut. Online mai sunt câteva săptămâni, și 30 decembrie e singura dată care contează aici — nu 31 ianuarie.

Cine nu poate:
• Cine datorează £3.000 sau mai mult. Și nu poți plăti o parte ca să cobori sub £3.000 — nu se acceptă
• Cine nu are destul venit prin PAYE ca HMRC să aibă de unde lua
• Cine ar ajunge să plătească peste jumătate din venitul PAYE în impozit
• Cine ar ajunge să plătească peste dublul impozitului obișnuit
• Contribuțiile Class 2 National Insurance ale celor pe cont propriu nu se pot plăti așa, decât dacă sunt datorate dinainte de 6 aprilie 2015

Se aplică în tot Regatul Unit. Și aici e partea despre care nu se vorbește: HMRC o face automat dacă te încadrezi. Dacă NU vrei să ți se schimbe codul fiscal — pentru cash-flow, sau pentru că nu vrei o deducere mare pe fluturaș la un angajator nou — trebuie să bifezi pe declarație să nu se întâmple.

Un lucru pe care îl acoperă și unul pe care nu îl acoperă: se ia în codul fiscal doar diferența de plată finală. Plățile în avans din 31 ianuarie și 31 iulie rămân de plătit separat.

Vrei să vezi dacă te încadrezi până pe 30 decembrie?""",
 th="""Ai taxă de plătit și ai salariu? HMRC ia suma din salariu, puțin câte puțin, în loc de tot pe 31 ianuarie — automat, dacă depui online până pe 30 decembrie 2026.

Nu poți dacă datorezi £3.000 sau mai mult. Și dacă NU vrei, bifezi pe declarație să nu se întâmple.""",
 li="""A Self Assessment bill does not have to be paid in one go on 31 January. Where the taxpayer is also on PAYE, HMRC collects it through the tax code across the following year instead — automatically, where the conditions are met.

Three conditions, all required:
• The bill is under £3,000
• Tax is already deducted through PAYE — employment or a pension
• The return is filed online by 30 December 2026

The paper deadline of 31 October has gone. For this option the date that matters is 30 December, not 31 January: a return filed on 15 January is on time for filing and too late for the tax code.

Who cannot use it:
• Anyone owing £3,000 or more — and a part payment to get under that figure is not accepted
• Anyone without enough PAYE income for HMRC to collect from
• Anyone for whom it would mean more than 50% of PAYE income going in tax
• Anyone who would end up paying more than twice their usual tax
• Class 2 National Insurance for the self-employed, unless it has been due since before 6 April 2015

UK-wide. And the direction of this one is the opposite of how it is usually described: HMRC "will automatically collect what you owe through your tax code if you meet all 3 conditions", "unless you've specifically asked them not to (on your tax return)". So the person who has to act is the one who does NOT want their 2026/27 code changed — cash flow, or a new employer's payroll seeing a large deduction.

What it covers and what it does not: coding out applies to the balancing payment. Payments on account due 31 January and 31 July still have to be found.

Worth checking before 30 December?""",
 bsky="""Owe under £3,000 and on PAYE? File by 30 December and HMRC collects it through your tax code automatically — or opt out on the return.""",
 pin_title="Pay a UK tax bill through your tax code: the 30 December deadline",
 pin="""How a UK Self Assessment bill is collected through your PAYE tax code instead of in one payment on 31 January. Three conditions must all apply: you owe less than £3,000, you already pay tax through PAYE on a wage or a pension, and you file your return online by 30 December. HMRC does it automatically where all three are met, unless you opt out on the return. The paper deadline of 31 October has already passed. You cannot use it if you owe £3,000 or more, and you cannot part-pay to get below that figure; nor if there is not enough PAYE income to collect from, or if it would mean more than half your PAYE income going in tax, or more than twice your usual tax. UK-wide. Ola Accountancy, Luton and Birmingham.""",
 source="gov.uk/pay-self-assessment-tax-bill/through-your-tax-code",
)

# ------------------------------------------------------------------ 8
C["scutire-1000-lire"] = dict(
 ro="""Dacă repari, livrezi, faci curățenie, dai cu împrumut uneltele tale sau cumperi ca să revinzi — pe lângă jobul principal — primii £1.000 pe an din banii aceia sunt scutiți de impozit. Nu plătești nimic pe ei și nu trebuie să anunți HMRC.

Se numește trading allowance și se aplică pe an fiscal. £1.000 e cifra pentru 2026/27: din 6 aprilie 2027 crește la £3.000, anunțat la Budget pe 28 octombrie 2026.

Atenție la o confuzie: dacă vinzi lucruri de-ale tale de care nu mai ai nevoie, asta nu e comerț și nu consumă cei £1.000. Comerț înseamnă că ai cumpărat ca să revinzi, sau ai făcut tu lucrul vândut.

Ce se numără: cât ai încasat, nu cât ți-a rămas. Dacă ai vândut de £1.400 și ai cheltuit £600, se numără £1.400 — ai trecut pragul, chiar dacă în mână ți-au rămas £800.

Ce nu se numără: salariul. £1.000 se referă doar la banii din ce faci pe cont propriu.

Dacă treci de £1.000, te înregistrezi la Self Assessment până pe 5 octombrie din anul fiscal următor. Poți alege apoi: fie scazi scutirea de £1.000 din încasări, fie scazi cheltuielile reale. Nu pe amândouă.

Cine nu poate folosi scutirea deloc:
• Dacă banii vin de la angajatorul tău
• Dacă vin de la angajatorul soțului, al soției sau al partenerului civil
• Dacă vin de la o firmă sau un parteneriat pe care îl controlezi tu sau cineva apropiat
• Pentru partea ta din profitul unui parteneriat

Și invers: sub £1.000 declarația se poate depune voluntar — ca să înregistrezi o pierdere, ca să plătești voluntar Class 2 National Insurance pentru pensie, sau ca să ai bază pentru Maternity Allowance și Tax-Free Childcare.

Se aplică în tot Regatul Unit și nu se cere: e automată.

Ai trecut de £1.000 anul acesta?""",
 th="""Câștigi ceva pe lângă job? Primii £1.000 pe an sunt scutiți de impozit. Se numără cât ai încasat, nu cât ți-a rămas. Din 6 aprilie 2027 pragul crește la £3.000.

Scutirea NU se aplică la bani de la angajatorul tău, al soțului, al soției sau al partenerului civil, ori de la o firmă pe care o controlezi.""",
 li="""The trading allowance exempts the first £1,000 of trading or miscellaneous income in a tax year. Below that, nothing is taxed and nothing is reported to HMRC.

Date it before you use it: £1,000 is the 2026/27 figure. It rises to £3,000 from 6 April 2027, alongside the Self Assessment reporting threshold, announced at the Budget on 28 October 2026.

It is measured on income, not profit. £1,400 of sales against £600 of costs is £1,400 for this test — over the threshold, even though £800 reached the bank.

Wages do not count towards it. The £1,000 covers only money from working for yourself: selling, casual services, hiring out personal equipment.

Above £1,000, registration for Self Assessment is required by 5 October in the following tax year. From there it is a choice: deduct the £1,000 allowance, or deduct actual expenses. Not both.

The allowance cannot be used at all where the income comes from:
• Your own employer
• Your spouse's or civil partner's employer — note the wording: a spouse or civil partner, not an unmarried partner
• A company or partnership you or a connected person owns, controls or is a partner in

It also does not apply to trading income from a partnership.

And the reverse case is worth knowing: a return can still be filed below £1,000 — to record a loss, to pay voluntary Class 2 National Insurance towards the State Pension, or to base Maternity Allowance or Tax-Free Childcare on self-employment income.

Worth separating too: the property allowance is a different £1,000, against income from land or property. Side-trade and rent are not added together against one allowance.

UK-wide, automatic, nothing to claim.

Past £1,000 this year and unsure what to do about it?""",
 bsky="""First £1,000 of trading income a year is tax free. It counts what came in, not what you kept — and never money from your own employer.""",
 pin_title="The UK £1,000 trading allowance: who can and cannot use it",
 pin="""The UK trading allowance exempts the first £1,000 of trading or miscellaneous income in a tax year, with nothing to report to HMRC below that. £1,000 is the 2026/27 figure and rises to £3,000 from 6 April 2027. It is measured on gross income, not profit: £1,400 of sales against £600 of costs is £1,400 for the test. Wages do not count towards it. Above the threshold you must register for Self Assessment by 5 October in the following tax year, then choose either the allowance or your actual expenses, not both. It cannot be used at all on income from your own employer, your spouse's or civil partner's employer, or a company or partnership you or a connected person controls. Ola Accountancy, Luton and Birmingham.""",
 source="gov.uk/guidance/tax-free-allowances-on-property-and-trading-income",
)

# ------------------------------------------------------------------ 9
C["salariu-minim-2027"] = dict(
 ro="""Salariul minim nu e o recomandare. E o cifră pe oră sub care nu se poate plăti legal, și se schimbă pe 1 aprilie în fiecare an.

Acum, din aprilie 2026:
• 21 de ani și peste — £12,71 pe oră
• 18-20 de ani — £10,85
• Sub 18 ani — £8,00
• Ucenici — £8,00

Din 1 aprilie 2027, deja decis:
• 21 de ani și peste — £13,21
• 18-20 de ani — £11,27
• Sub 18 ani — £8,31
• Ucenici — £8,31

Tariful de ucenic se aplică doar dacă ucenicul are sub 19 ani, sau are 19 ani și peste dar e în primul an de ucenicie. După primul an, un ucenic de 19 ani sau peste primește tariful vârstei lui.

Cine nu are salariu minim:
• Cei care lucrează pe cont propriu, cu afacerea lor — tariful e al lor, nu al legii
• Directorii de firmă — dar atenție: un director care are ȘI contract de muncă cu firma are dreptul la salariul minim pentru munca făcută pe acel contract
• Voluntarii
• Militarii
• Rudele angajatorului care locuiesc în casa lui
• Cei sub vârsta la care se termină școala obligatorie, de obicei 16 ani
• Studenții în stagiu de practică de până la un an

Se aplică în tot Regatul Unit — Anglia, Scoția, Țara Galilor și Irlanda de Nord, aceleași cifre. O singură excepție: agricultura. Scoția, Țara Galilor și Irlanda de Nord au fiecare organismul lor care stabilește tarife agricole, iar acele tarife nu pot fi mai mici decât salariul minim, dar pot fi mai mari. Anglia nu are.

„Real Living Wage” și „London Living Wage” sunt altceva: tarife voluntare stabilite de o organizație, nu minimul legal.

E obligația angajatorului, nu ceva ce ceri.

Vrei verificat tariful pe fluturaș sau pe statul de plată?""",
 th="""Salariul minim național e £12,71 pe oră la 21 de ani și peste. Din aprilie 2027 urcă la £13,21. La 18-20 de ani: £10,85 acum, £11,27 din aprilie.

Dacă lucrezi pe cont propriu, cu afacerea ta, salariul minim nu ți se aplică — tu îți stabilești prețul. Nici voluntarii nu intră.""",
 li="""The minimum wage is not guidance. It is an hourly floor below which pay is unlawful, and it moves on 1 April each year.

Current, from April 2026:
• 21 and over — £12.71
• 18 to 20 — £10.85
• Under 18 — £8.00
• Apprentice — £8.00

From 1 April 2027, already announced:
• 21 and over — £13.21
• 18 to 20 — £11.27
• Under 18 — £8.31
• Apprentice — £8.31

The apprentice rate applies only where the apprentice is under 19, or is 19 or over and in the first year of the apprenticeship. Past that first year, an apprentice of 19 or over moves to the rate for their age — a common and expensive payroll error.

Not entitled to the minimum wage at all:
• Self-employed people running their own business
• Company directors — with the caveat that matters: a director who is ALSO employed by the company under a contract "will be entitled to the minimum wage, like any other worker" for work done under it
• Volunteers and voluntary workers
• Members of the armed forces
• Family members of the employer living in the employer's home
• Workers below school leaving age, usually 16
• Higher and further education students on a work placement of up to one year

UK-wide for the headline rates: the same figures in England, Scotland, Wales and Northern Ireland. One devolved exception — agriculture. Wales, Scotland and Northern Ireland each have an agricultural wages body whose Agricultural Wages Order rate "will never be lower than their National Minimum Wage rate but may be higher". England has none. The "real Living Wage" and "London Living Wage" are separate voluntary rates set by a charity, not the legal minimum.

It is the employer's duty, not a worker's claim.

Want a payroll checked against the April rates?""",
 bsky="""UK minimum wage: £12.71 an hour at 21 and over, £13.21 from April 2027. Self-employed people are not covered at all.""",
 pin_title="UK minimum wage 2026 and 2027: rates by age",
 pin="""UK National Minimum Wage and National Living Wage rates by age. From April 2026: £12.71 an hour for 21 and over, £10.85 for 18 to 20, £8.00 under 18 and £8.00 for apprentices. From 1 April 2027: £13.21, £11.27, £8.31 and £8.31. The apprentice rate applies only to apprentices under 19, or 19 and over in their first year — after that they move to the rate for their age. Not entitled at all: self-employed people running their own business, volunteers, armed forces, family members living in the employer's home, and under-school-leaving-age workers. Company directors are not entitled either, unless they also hold an employment contract with the company. Same rates across the UK, except agriculture, where Wales, Scotland and Northern Ireland set their own and can go higher. Ola Accountancy, Luton and Birmingham.""",
 source="gov.uk/national-minimum-wage-rates · gov.uk/national-minimum-wage/who-gets-the-minimum-wage",
)

# ----------------------------------------------------------------- 10
C["child-benefit-2026"] = dict(
 ro="""Child Benefit e o sumă fixă pe săptămână pentru fiecare copil. Nu vine singură: cineva trebuie să o ceară.

Anul fiscal 2026/27:
• £27,05 pe săptămână pentru primul copil sau singurul copil
• £17,90 pe săptămână pentru fiecare copil următor

Se plătește de obicei o dată la patru săptămâni. Copilul trebuie să aibă sub 16 ani, sau sub 20 dacă e încă într-o formă de școală sau formare aprobată.

Pentru un copil poate cere o singură persoană. Și dacă ai un copil sub 12 ani, cererea îți dă automat credite de National Insurance — adică ani care contează la pensia de stat, chiar dacă nu lucrezi sau nu câștigi destul ca să plătești contribuții.

Partea despre care se vorbește puțin: dacă tu sau partenerul tău are venit peste £60.000, o parte din bani se dă înapoi. Pentru fiecare £200 peste £60.000 se dă înapoi 1% din Child Benefit. Peste £80.000 se dă înapoi tot.

Se uită la venitul unei persoane, nu al gospodăriei. Doi părinți cu £50.000 fiecare păstrează totul. Un singur părinte cu £80.000 nu păstrează nimic.

Și aici e lucrul care merită știut: chiar dacă ești peste prag, merită să ceri Child Benefit fără să primești banii. Nu plătești nimic înapoi și păstrezi creditele pentru pensie.

Se aplică în tot Regatul Unit.

Nu știi dacă ar trebui să dai ceva înapoi?""",
 th="""Child Benefit 2026/27: £27,05 pe săptămână pentru primul copil, £17,90 pentru fiecare următor. Nu vine singur — se cere.

Dacă tu sau partenerul câștigă peste £60.000, o parte se dă înapoi; peste £80.000, tot. Se uită la venitul unei persoane, nu al gospodăriei.""",
 li="""Child Benefit is a fixed weekly amount per child, and it never starts on its own. Someone has to claim it.

Tax year 2026 to 2027:
• £27.05 a week for the eldest or only child
• £17.90 a week for each additional child

Usually paid every four weeks. The child must be under 16, or under 20 if they stay in approved education or training. Only one person can claim for a given child.

With a child under 12, claiming also gives the claimant National Insurance credits — qualifying years towards the State Pension, earned without working or without earning enough to pay contributions. That is the part most often left on the table.

The other half of the picture: where the claimant or their partner has adjusted net income over £60,000, the High Income Child Benefit Charge claws it back at 1% of the Child Benefit for every £200 above £60,000. Over £80,000 the whole amount goes back.

The test is on one person's income, not the household's. Two parents on £50,000 each keep everything. One parent on £80,000 keeps none of it.

Which makes the planning point simple: someone over the threshold can still register the claim and decline the payments. No charge to pay, and the National Insurance credits are kept.

UK-wide.

Want the charge worked out before January?""",
 bsky="""Child Benefit 2026/27: £27.05 a week for the first child, £17.90 for each other. Over £60,000 part of it goes back; over £80,000, all of it.""",
 pin_title="Child Benefit 2026/27 rates and the £60,000 charge",
 pin="""UK Child Benefit for the 2026 to 2027 tax year: £27.05 a week for the eldest or only child and £17.90 a week for each additional child, usually paid every four weeks. The child must be under 16, or under 20 in approved education or training, and only one person can claim per child. It is never automatic — it has to be claimed, and claiming for a child under 12 also gives National Insurance credits towards the State Pension. Where the claimant or their partner has income over £60,000 the High Income Child Benefit Charge takes back 1% for every £200 above it, and all of it over £80,000, judged on one person's income rather than the household's. Ola Accountancy, Luton and Birmingham.""",
 source="gov.uk/child-benefit-rates and gov.uk/child-benefit-tax-charge",
)

# Threads caps a post at 500 characters through the API. Over that, Metricool
# returns "Media container not created by unknown cause" — a message that points
# at the images and has nothing to do with them. On 5 November 2026 a
# 638-character caption failed, a 755-character one failed, and a 488-character
# one published, on the same four images Facebook and Instagram accepted in the
# same second. So Threads gets its own post and its own caption: the hook, the
# single most useful fact, the who-does-NOT line, the number, the disclaimer and
# the four brand tags. No worked example, no topical tags — that is what fits.
WA_TH = f"WhatsApp: {PHONE}"


def th_caption(slug):
    return f"{C[slug]['th']}\n\n{WA_TH}\n\n{DISC_RO}\n\n{BRAND_TAGS}"


def ro_caption(slug):
    t = topics.BY_SLUG[slug]
    return (f"{C[slug]['ro']}\n\n{WA_RO}\n\n{DISC_RO}\n\n"
            f"Sursă: {C[slug]['source']}\n\n{tags(t, 'ro')}")


def li_caption(slug):
    t = topics.BY_SLUG[slug]
    return (f"{C[slug]['li']}\n\n{PHONE}\n\nOla Accountancy — Luton and Birmingham\n\n"
            f"{DISC_EN}\n\nSource: {C[slug]['source']}\n\n{tags(t, 'en')}")


def bsky_caption(slug):
    # 300-character API cap. Brand tags are 85 of them, so no topical tags here.
    # The disclaimer is the brand-standard wording, not a shortened one: the cap is
    # answered by shorter copy, the way qa.py's overflow is answered by shorter copy.
    return f"{C[slug]['bsky']}\n\n{DISC_EN}\n\n{BRAND_TAGS}"


def pin_caption(slug):
    t = topics.BY_SLUG[slug]
    return f"{C[slug]['pin']}\n\n{DISC_EN}\n\n{tags(t, 'en')}"


def gbp_caption(slug):
    t = topics.BY_SLUG[slug]
    return f"{C[slug]['gbp']}\n\n{DISC_EN}\n\n{tags(t, 'en')}"


def assert_lengths():
    bad = []
    for slug in C:
        b = bsky_caption(slug)
        if len(b) > 300:
            bad.append(f"bluesky {slug}: {len(b)} chars (cap 300)")
        if "th" in C[slug]:
            th = th_caption(slug)
            if len(th) > 500:
                bad.append(f"threads {slug}: {len(th)} chars (cap 500)")
        if "gbp" in C[slug] and len(gbp_caption(slug)) > 1500:
            bad.append(f"gmb {slug}: {len(gbp_caption(slug))} chars (cap 1500)")
    return bad


if __name__ == "__main__":
    print(f"{'topic':22s} {'bsky':>5s} {'thr':>5s} {'gmb':>5s}   ro / li / pin")
    for slug in C:
        g = len(gbp_caption(slug)) if "gbp" in C[slug] else 0
        th = len(th_caption(slug)) if "th" in C[slug] else 0
        print(f"  {slug:20s} {len(bsky_caption(slug)):5d} {th:5d} {g:5d}   "
              f"{len(ro_caption(slug))} / {len(li_caption(slug))} / {len(pin_caption(slug))}")
    bad = assert_lengths()
    print("\nLENGTH FAILURES:", len(bad))
    for x in bad: print("  -", x)
    raise SystemExit(1 if bad else 0)
