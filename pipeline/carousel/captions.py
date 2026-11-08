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
 ro="""Pe 31 ianuarie 2027 nu plătești doar taxele pe 2025/26.

HMRC îți cere în aceeași zi și prima tranșă în avans pentru anul următor: jumătate din taxele datorate anul trecut. A doua tranșă vine pe 31 iulie 2027.

Asta înseamnă că factura din ianuarie poate fi de o dată și jumătate cât arată declarația. Pentru mulți, e o surpriză în primul an pe cont propriu — dar e previzibilă, dacă știi că vine.

Ce intră în avans: și Class 4 National Insurance, dacă lucrezi pe cont propriu.
Ce nu intră: Capital Gains Tax și împrumutul studențesc — acelea apar doar în plata de regularizare.

Cine nu plătește avans deloc: dacă taxele datorate anul trecut au fost sub £1.000, sau dacă peste 80% din ea s-a reținut deja la sursă (prin codul fiscal sau de către bancă).

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
 pin="""The UK VAT registration threshold is £90,000 of taxable turnover over a rolling 12 months, recalculated at every month end — not the tax year or the calendar year. Backward look: once the last 12 months pass £90,000, register within 30 days of that month's end, effective from the first day of the second month after. Forward look: if you expect to pass £90,000 in the next 30 days, register before that period ends, effective from the day you realised. Deregistration threshold £88,000, on expected turnover for the next 12 months. Turnover, not profit.""",
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
 pin="""Winter Fuel Payment for winter 2026/27: £200 for those born on or before 27 June 1960 and £300 if born before 28 September 1946, for someone living alone, based on the qualifying week of 21 to 27 September 2026. England, Wales and Northern Ireland only — Scotland has its own Pension Age Winter Heating Payment. If your own income passes £35,000, HMRC recovers the whole payment through your tax code or Self Assessment, assessed per person not per household. Most are paid automatically; anyone who has never had it must claim by 31 March 2027.""",
 source="gov.uk/winter-fuel-payment and gov.uk/guidance/paying-back-the-winter-fuel-payment",
)

# ------------------------------------------------------------------ 6
C["cis-20-30"] = dict(
 ro="""În construcții, firma care te plătește nu îți dă toți banii din factură. Oprește o parte și o trimite la HMRC în numele tău. Asta e CIS — Construction Industry Scheme.

Cât oprește nu depinde de un singur lucru, ci de două:
• Ești înregistrat la CIS ȘI firma te poate verifica la HMRC → 20%
• Lipsește oricare dintre cele două → 30%
• Cu „gross payment status" → 0%, primești tot și plătești taxele la final

Firma te verifică la HMRC înainte să te plătească. Dacă verificarea nu iese, se opresc 30% chiar dacă tu ești înregistrat.

Banii opriți nu sunt pierduți. Contează ca plată în avans pentru taxele și National Insurance pe care le datorezi. Dacă s-a oprit mai mult decât datorezi, diferența se returnează.

Cum se recuperează depinde de forma în care lucrezi: pe cont propriu, prin declarația anuală; cu firmă (Ltd), prin payroll, cu un Employer Payment Summary. HMRC spune explicit să NU folosești declarația de Corporation Tax — riști o penalizare.

Din ce NU se oprește nimic: din TVA, din materialele pe care le-ai plătit tu, din combustibilul folosit pe șantier (nu cel de drum), din utilajele închiriate pentru lucrare și din costul de fabricație al materialelor. Se oprește doar din munca ta.

Cine nu intră deloc: angajații. Un contract de muncă e exclus din CIS, deci din salariu nu se oprește nimic pe CIS.

Atenție la o confuzie des întâlnită: serviciile de pe șantier — paznicii angajați ca pază, bucătăria, cabinetul medical — sunt în afara CIS, dar nu sunt singurele. Lista HMRC e mai lungă. Iar construirea acelor facilități, montarea rulourilor de siguranță sau săpatul pentru stâlpii de camere SUNT în CIS.

Firma trebuie să îți dea o chitanță de plată și deducere în 14 zile de la sfârșitul lunii fiscale. Păstreaz-o: e dovada ta.

Se aplică în tot Regatul Unit. Înregistrarea e gratuită și e pasul tău.

Nu știi dacă ești înregistrat sau cât ți s-a oprit?""",
 th="""Ți se opresc 30% din plată în construcții? De obicei înseamnă că nu ești înregistrat la CIS — sau că firma nu te-a putut verifica la HMRC. Ca să fie 20%, îți trebuie amândouă: înregistrat și verificat.

Angajații nu intră deloc în CIS. Nici din TVA și nici din materialele plătite de tine nu se oprește nimic.""",
 li="""The Construction Industry Scheme decides how much of a subcontractor's invoice actually reaches them.

The rate turns on two facts, not one. The standard 20% applies only where both hold:
• Registered for CIS and the contractor can verify you — 20% deducted
• Either of those missing — 30% deducted
• Gross payment status — 0%, paid in full, tax settled later

A registered subcontractor who cannot be verified is still deducted at 30%, so registration alone does not settle it.

The deduction is not a cost. It is an advance payment against the subcontractor's Income Tax and National Insurance. Where the deductions exceed the tax and National Insurance due, the difference is repaid.

How it is recovered depends on the trading form, and this one is worth getting right: a sole trader or partner offsets it through Self Assessment, while a limited company recovers it through its payroll scheme on an Employer Payment Summary. HMRC's instruction is explicit — "Do not use your Corporation Tax return to pay tax with your deductions - you may get a penalty if you do."

The rate applies to labour only. Before it is calculated, a contractor takes out VAT, materials the subcontractor paid for, consumable stores, fuel other than travel fuel, plant hire paid to a third party, and the cost of manufacturing or prefabricating materials.

Outside the scheme altogether: employees. A contract of employment is excluded, so nothing is deducted under CIS from a wage.

One distinction that catches people: what is excluded is the RUNNING of site facilities — canteens, hostels, offices, toilets, medical centres — and the supply of security guards. Constructing those facilities is within the scheme, as is most physical security work: erecting CCTV posts, fitting security shutters, putting up site hoardings.

The contractor must issue a payment and deduction statement within 14 days of the end of the tax month. It is the subcontractor's evidence; without it the offset is an argument rather than a record.

UK-wide. Registration is free and is the subcontractor's own step — nobody does it for them, and the 30% rate is what happens when it is not done.

Want your CIS deductions checked against your return?""",
 bsky="""CIS: 20% off your pay needs both: registered, and the contractor can find you at HMRC. Miss either and it is 30%. Employees are outside it.""",
 pin_title="UK CIS: 20% or 30% off a subcontractor's pay",
 pin="""Why a UK construction subcontractor has 20% or 30% taken off their pay under the Construction Industry Scheme: 20% only if the subcontractor is registered for CIS and the contractor can find them at HMRC. Miss either and it is 30%. Gross payment status, 0%. Nothing comes off VAT, materials they paid for, plant hire or fuel other than travel fuel. Employees are outside CIS entirely, as is running a site canteen, guarding a site or installing alarms and CCTV — but site huts and hoardings, security shutters and CCTV posts are inside it. UK-wide.""",
 gbp="""Working in construction and wondering why 30% comes off your pay instead of 20%?

Under the Construction Industry Scheme the 20% rate needs two things to be true, not one: you are registered for CIS, and the contractor can check you against HMRC's records before they pay you. If either one is missing, 30% comes off instead — so registering does not on its own settle it, and a subcontractor who is registered but cannot be checked still has 30% taken. A subcontractor with gross payment status has nothing deducted at all.

The gap between 20% and 30% is 10 percentage points — an extra £10 off every £100 the deduction is worked out on — and registering is free. It is not taken off the whole invoice: it is worked out on the labour part of the payment.

The money is not lost either way: it is an advance payment against your Income Tax and National Insurance. Nothing is deducted from VAT, from materials you paid for, or from plant hire. Employees are outside the scheme completely.

Ola Accountancy works with construction subcontractors in Luton and Birmingham. Send us your payment and deduction statements and we will check what has been taken and how it comes off your tax.""",
 source="gov.uk/what-you-must-do-as-a-cis-subcontractor",
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
 li="""A Self Assessment bill for the 2025/26 tax year does not have to be paid in one go on 31 January 2027. Where the taxpayer is also on PAYE, HMRC collects that bill through the 2027/28 tax code instead — automatically, where the conditions are met.

When the money actually comes out of your pay: not this winter. The 2027/28 tax year starts on 6 April 2027, so nothing is deducted before that date. From then it is taken from the wage or the pension in equal instalments across the 12 months to 5 April 2028.

Three conditions, all required:
• The 2025/26 bill is under £3,000
• Tax is already deducted through PAYE — employment or a pension
• The return reached HMRC on paper by 31 October 2026, or online by 30 December 2026

That third condition is an either/or, and the paper half of it still counts: anyone who sent a paper return by 31 October 2026 has already met it. If the return has not gone in yet, online by 30 December 2026 is the route left — and for this option the date that matters is 30 December, not 31 January: a return filed on 15 January is on time for filing and too late for the tax code.

Who cannot use it:
• Anyone owing £3,000 or more — and a part payment to get under that figure is not accepted
• Anyone without enough PAYE income for HMRC to collect from
• Anyone for whom it would mean more than 50% of PAYE income going in tax
• Anyone who would end up paying more than twice their usual tax
• Class 2 National Insurance for the self-employed, unless it has been due since before 6 April 2015

UK-wide. And the direction of this one is the opposite of how it is usually described: HMRC "will automatically collect what you owe through your tax code if you meet all 3 conditions", "unless you've specifically asked them not to (on your tax return)". So the person who has to act is the one who does NOT want their 2027/28 code changed — cash flow, or a new employer's payroll seeing a large deduction.

What it covers and what it does not: coding out applies to the 2025/26 balancing payment. Payments on account due 31 January and 31 July still have to be found.

Worth checking before 30 December?""",
 bsky="""Owe under £3,000 and on PAYE? File by 30 December and HMRC collects it through your tax code automatically — or opt out on the return.""",
 pin_title="Pay a UK tax bill through your tax code: the 30 December deadline",
 pin="""How a UK Self Assessment bill is collected through your PAYE tax code instead of in one payment on 31 January. Three conditions must all apply: you owe less than £3,000, you already pay tax through PAYE on a wage or a pension, and you file online by 30 December. HMRC does it automatically where all three are met, unless you opt out on the return. You cannot use it if you owe £3,000 or more, if there is not enough PAYE income to collect from, or if it would mean more than half your PAYE income going in tax, or more than twice your usual tax. UK-wide.""",
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
 pin="""The UK trading allowance exempts the first £1,000 of trading or miscellaneous income in a tax year. £1,000 is the 2026/27 figure and it rises to £3,000 from 6 April 2027. It is measured on gross income, not profit. Above the threshold you must register for Self Assessment by 5 October in the following tax year, then choose either the allowance or your actual expenses, not both. It cannot be used at all on income from your own employer, your spouse's or civil partner's employer, or a company or partnership you or a connected person controls.""",
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
 pin="""UK National Minimum Wage and National Living Wage rates by age. From April 2026: £12.71 an hour for 21 and over, £10.85 for 18 to 20, £8.00 under 18 and £8.00 for apprentices. From 1 April 2027: £13.21, £11.27, £8.31 and £8.31. The apprentice rate applies only to apprentices under 19, or 19 and over in their first year. Not entitled at all: self-employed people running their own business, volunteers, armed forces, family members living in the employer's home, and under-school-leaving-age workers. Same rates across the UK, except agriculture.""",
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
 pin="""UK Child Benefit for 2026/27: £27.05 a week for the eldest or only child and £17.90 a week for each additional child, usually paid every four weeks. The child must be under 16, or under 20 in approved education or training, and only one person can claim per child. It is never automatic — it has to be claimed, and claiming for a child under 12 also gives National Insurance credits towards the State Pension. Over £60,000 the High Income Child Benefit Charge takes back 1% for every £200 above it, and all of it over £80,000, on one person's income not the household's.""",
 source="gov.uk/child-benefit-rates and gov.uk/child-benefit-tax-charge",
)

# ----------------------------------------------------------------- 11
C["kilometraj-55p"] = dict(
 ro="""Dacă lucrezi pe cont propriu și îți folosești mașina pentru muncă, suma pe care o poți scădea a crescut.

Din 6 aprilie 2026:
• 55p pentru fiecare milă, primele 10.000 de mile într-un an fiscal
• 25p pentru fiecare milă peste 10.000
• 24p pe motocicletă, de la prima milă

Până pe 5 aprilie 2026 primele 10.000 de mile se socoteau la 45p. Pe 10.000 de mile asta înseamnă £5.500 scăzuți din profit în loc de £4.500.

Cum funcționează: nu strângi bonuri de benzină, nu ții socoteala reparațiilor, nu împarți costurile între muncă și personal. Numeri milele făcute pentru muncă și înmulțești.

Dar nu orice milă se numără. GOV.UK trece „travel between home and work" direct pe lista cheltuielilor care NU se pot deduce, alături de deplasările personale și de amenzi. Drumul zilnic de acasă la locul de muncă nu intră, chiar dacă îl faci cu mașina ta și pentru munca ta.

Exemplu: 8.000 de mile pentru muncă într-un an → 8.000 × 55p = £4.400 scăzuți din profit. La 14.000 de mile: primele 10.000 la 55p (£5.500) plus 4.000 la 25p (£1.000) = £6.500.

Cine NU poate folosi suma pe milă deloc: mașinile construite pentru uz comercial. GOV.UK scrie „except those designed for commercial use" și dă ca exemple taxiurile negre, hackney carriages și mașinile de școală cu dublă comandă. Contează cum e construită mașina, nu ce meserie faci — cu o mașină normală, chiar și pe aplicație, suma pe milă ți se aplică.

Și nici pentru o mașină din al cărei preț, sau din a cărei benzină și reparații, ai scăzut deja din profit. E una sau alta, niciodată amândouă.

Și alegerea rămâne: dacă o dată ai folosit suma pe milă pentru o mașină, rămâi cu ea cât timp folosești mașina în afacere.

Se aplică în tot Regatul Unit. Se trece în declarație — nu vine nimic automat.

Nu știi cum se numără milele?""",
 th="""Lucrezi pe cont propriu și folosești mașina pentru muncă? Din 6 aprilie 2026 scazi 55p pe milă pentru primele 10.000 de mile, apoi 25p. Era 45p.

Dar drumul de acasă la muncă nu se numără. Și mașinile construite pentru uz comercial (taxiurile negre) nu intră în suma pe milă — o mașină normală intră.""",
 li="""The self-employed mileage rate went up, and it is worth more than it looks.

Simplified expenses, 2026/27:
• 55p a mile for the first 10,000 business miles in a tax year
• 25p a mile after that
• 24p for motorcycles, from the first mile

The first-10,000 rate rose from 45p to 55p on 6 April 2026. On 10,000 business miles that is £5,500 off profit instead of £4,500.

What the flat rate buys you is simplicity: no fuel receipts, no running-cost records, no apportioning between business and private use. Count the business miles, multiply.

But not every mile is a business mile. GOV.UK lists, verbatim, among the costs you cannot claim: "non-business driving or travel costs", "fines or penalty charges" and "travel between home and work". The daily run from home to the same site is not claimable, however much it feels like work.

Worked: 8,000 business miles in the year is 8,000 × 55p = £4,400. At 14,000 miles it is the first 10,000 at 55p (£5,500) plus 4,000 at 25p (£1,000) = £6,500.

Who cannot use it at all: cars designed for commercial use. GOV.UK says "except those designed for commercial use" and names black cabs, hackney carriages and dual-control driving instructors' cars. The test is the vehicle's design, not the driver's trade: a private-hire or ride-hailing driver in an ordinary car is not driving a car designed for commercial use, and can use the mileage flat rate. And it is the vehicle flat rate that is barred, not simplified expenses as a whole — the flat rates for working from home and for living at your business premises are unaffected.

Nor can anyone who has already claimed capital allowances on that vehicle, or already put its running costs through business profits. One method or the other, never both.

And the election sticks. Once the flat rate is used for a vehicle, it has to be kept for that vehicle for as long as it is used in the business — so a switch to actual costs in a better year is not available.

UK-wide, claimed on the return rather than paid out.

Want the vehicle position checked before January?""",
 bsky="""Self-employed? Business miles are 55p each for the first 10,000 in a tax year, then 25p. Home to work does not count.""",
 pin_title="UK self-employed mileage: 55p a mile from April 2026",
 pin="""HMRC simplified expenses mileage rates for 2026/27: 55p a mile for the first 10,000 business miles in a tax year, then 25p a mile, and 24p for motorcycles from the first mile. The first-10,000 rate rose from 45p on 6 April 2026. Travel between home and work does not count. Cars designed for commercial use — black cabs, dual-control instructors' cars — are outside the mileage flat rate, as is any vehicle you have already claimed capital allowances on. The test is the car's design, not the driver's trade. UK-wide, claimed on the tax return.""",
 gbp="""Business miles in your own car are worth up to 55p now, not 45p.

If you are self-employed and use simplified expenses, you can take 55p a mile off your profit for the first 10,000 business miles in a tax year, then 25p a mile after that. Motorcycles are 24p from the first mile. The first-10,000 rate rose from 45p to 55p on 6 April 2026.

On 10,000 business miles that is £5,500 off profit instead of £4,500 — and no fuel receipts to keep.

Travel between home and work does not count — only travel for the work itself.

Who cannot use it at all: cars designed for commercial use, which GOV.UK illustrates with black cabs, hackney carriages and dual-control driving instructors' cars. Nor any vehicle you have already claimed capital allowances on, or whose running costs are already in the accounts. One method or the other.

It applies across the UK, and it is claimed on the tax return — nothing arrives automatically.

Self-employed and driving for work around Luton or Birmingham? Call or message 0330 133 1886 and we will check what you can claim on the vehicle.

Ola Accountancy — Luton and Birmingham.

Source: gov.uk/simpler-income-tax-simplified-expenses/vehicles""",
 source="gov.uk/simpler-income-tax-simplified-expenses/vehicles and gov.uk/expenses-if-youre-self-employed/travel",
)

# ----------------------------------------------------------------- 12
C["termene-firma-ltd"] = dict(
 ro="""O firmă nu depune o dată pe an. Are patru termene, în două locuri diferite — și plata vine înaintea declarației.

Trei pornesc de la data la care se încheie anul contabil:
• Bilanțul la Companies House — în 9 luni
• Plata Corporation Tax — în 9 luni și o zi
• Declarația firmei la HMRC — în 12 luni

Pe un an care se încheie pe 31 decembrie 2026: bilanț până pe 30 septembrie 2027, plată până pe 1 octombrie 2027, declarație până pe 31 decembrie 2027. Da, plătești înainte să depui declarația: suma se calculează cu trei luni înainte de termen.

Al patrulea termen e pe alt ciclu și e cel mai periculos: confirmation statement la Companies House, o dată la 12 luni, în 14 zile de la încheierea perioadei. Se depune și dacă nu s-a schimbat nimic. Dacă nu, poți lua o amendă de până la £5.000 și firma poate fi radiată. Un bilanț întârziat costă bani; o declarație de confirmare ratată îți poate șterge firma.

Primul an e altfel: la o firmă nouă, primul bilanț se depune în 21 de luni de la înregistrare, nu în 9.

Cine NU are aceste termene: dacă lucrezi pe cont propriu, fără firmă, nu ai niciunul. Nu plătești Corporation Tax și nu depui nimic la Companies House — ai Self Assessment, cu declarația și plata pe 31 ianuarie — plus raportări trimestriale dacă ai avut peste £50.000 venit brut din activitate independentă sau chirii în declarația 2024/25 și ai intrat în Making Tax Digital din 6 aprilie 2026. Nici firmele cu profit peste £1,5 milioane nu au data de 9 luni și o zi: ele plătesc în tranșe.

Declarația se depune și pe pierdere. Singura excepție e firma dormantă: odată ce ai anunțat HMRC, nu mai depui declarație până nu primești o cerere. Dar la Companies House nu scapi — bilanțul și confirmation statement se depun și la o firmă dormantă.

Se aplică în tot Regatul Unit. Niciun termen nu se amintește singur.

Nu știi ce termen urmează?""",
 th="""O firmă are patru termene, nu unul. De la anul contabil: bilanțul la Companies House în 9 luni, plata Corporation Tax în 9 luni și o zi, declarația la HMRC în 12 luni. Plus confirmation statement, la fiecare 12 luni.

Dacă lucrezi pe cont propriu, fără firmă, nu ai niciunul — ai Self Assessment, cu 31 ianuarie.""",
 li="""A private limited company does not have one filing date a year. It has four, in two different places, and the payment falls due before the return.

Three of them run from the company's own year end:
• Accounts to Companies House — 9 months
• Corporation Tax paid to HMRC — 9 months and 1 day
• Company Tax Return to HMRC — 12 months

Year ending 31 December 2026:
• 30 September 2027 — accounts at Companies House
• 1 October 2027 — Corporation Tax paid
• 31 December 2027 — return filed

So the tax is paid three months before the return that reports it is due. That ordering catches new directors: the figure has to be worked out long before the filing deadline forces it.

The fourth deadline runs on its own cycle and it is the dangerous one: a confirmation statement at Companies House, at least once every 12 months. The review period ends 12 months after incorporation or after the last confirmation statement date, and you have 14 days after that to file. GOV.UK is explicit that "You must file a confirmation statement even if there have not been any changes to your company during the review period" — £50 online. Miss it and Companies House may issue a financial penalty, you can be fined up to £5,000, and the company "may be struck off the Companies House register". Late accounts cost money; a missed confirmation statement can cost you the company.

The first year is different. A newly registered company's first accounts are due 21 months after the date of registration, not 9 months after a year end.

Who does not have any of this: a sole trader. No Corporation Tax, nothing at Companies House, Self Assessment with the return and payment due 31 January instead — though "one date a year" stopped being true for them on 6 April 2026, when sole traders and landlords with over £50,000 of qualifying income on the 2024-25 return came inside Making Tax Digital for Income Tax and started filing quarterly updates as well. Companies with taxable profits above £1.5 million do not use the 9-months-and-1-day date either — they pay in instalments. The 9-month accounts date is a private company's; a public company files sooner.

A return is filed after a loss and when no Corporation Tax is owed, and HMRC still has to be told when nothing is due. A company dormant for Corporation Tax is the one exception — once HMRC has been told, no further return is due unless a notice to deliver one arrives. Companies House is less forgiving: accounts and a confirmation statement are still required of a dormant company.

UK-wide. Nothing here is claimed and nothing is prompted.

Want your company's four dates set out?""",
 bsky="""A UK private company: four deadlines. Accounts 9 months, tax 9 months and 1 day, return 12 months, confirmation statement every 12.""",
 pin_title="A UK private limited company's four filing deadlines",
 pin="""The four deadlines every UK private limited company has. Three run from its own year end: annual accounts to Companies House within 9 months, Corporation Tax paid 9 months and 1 day after the accounting period ends, and the Company Tax Return filed within 12 months. The fourth runs on its own cycle: a confirmation statement every 12 months, filed within 14 days of the review period ending, even if nothing has changed — miss it and the company can be struck off. A return is filed even after a loss. A public company files its accounts sooner.""",
 source="gov.uk/prepare-file-annual-accounts-for-limited-company",
)

# ----------------------------------------------------------------- 13
C["employment-allowance-10500"] = dict(
 ro="""Firma plătește National Insurance pentru angajați, peste cât se oprește din salariul lor. Employment Allowance taie până la £10.500 din National Insurance-ul Class 1 al firmei într-un an fiscal.

Nu vine singură. Se cere din programul de salarii, pentru un singur stat de plată — și se cere DIN NOU la fiecare an fiscal. Nu se reportează.

Dacă n-ai cerut-o deloc, se poate cere retroactiv până la 4 ani — pentru 2022/23, până pe 5 aprilie 2027. Dar un an vechi are alte condiții: £10.500 e suma din 2025/26 încoace, iar între 6 aprilie 2022 și 5 aprilie 2025 era £5.000 pe an. Pentru 2024/25 sau mai vechi poți cere doar dacă Class 1-ul firmei din anul anterior a fost sub £100.000 — barieră căzută în aprilie 2025, deci din 2025/26 nu mai există limită.

Cine NU poate cere deloc — firma:
• Firma Ltd cu un singur director, dacă el e singurul angajat cu National Insurance Class 1 secundar — partea firmei, peste Secondary Threshold.
• Instituțiile publice fără statut de caritate — primărie, consiliu local sau parohial — oricât de puțin lucrează pentru public.
• Orice alt angajator cu peste jumătate din muncă pentru sectorul public — dar organizațiile de caritate pot cere oricum.
• Într-un grup de firme sau de organizații de caritate legate între ele, cere una singură.

Angajați pe care NU îi poți include — firma rămâne eligibilă pentru ceilalți, dacă mai are alți angajați:
• Angajatul care intră sub regulile off-payroll (IR35).
• Cineva angajat pentru treburi casnice — o bonă, un grădinar — dacă nu e îngrijitor.

Pot cere: firmele cu sub jumătate din muncă pentru sectorul public, organizațiile de caritate, cluburile sportive de amatori și cine angajează un îngrijitor.

Se aplică în tot Regatul Unit. Se cere pentru anul fiscal în curs.

Nu știi dacă firma ta poate cere?""",
 th="""Employment Allowance taie până la £10.500 din National Insurance-ul Class 1 al firmei. Se cere din programul de salarii — și din nou la fiecare an fiscal. Nu se reportează.

Cine NU poate cere: firma Ltd cu un singur director, dacă el e singurul angajat cu National Insurance Class 1 secundar — partea firmei.""",
 li="""Employment Allowance takes up to £10,500 off an employer's Class 1 National Insurance in a tax year. It is never automatic — it is claimed through payroll software, against one payroll only.

And it is claimed again every single tax year, by Employer Payment Summary. It does not carry forward.

If you never claimed at all, you can go back up to 4 years after the end of the tax year concerned — a 2022 to 2023 claim has to be made by 5 April 2027. But an earlier year is not claimed on today's terms. The allowance is £10,500 for 2025 to 2026 onwards; for each year between 6 April 2022 and 5 April 2025 it was £5,000. And to claim for 2024 to 2025 or earlier, your employers' Class 1 National Insurance liabilities must have been less than £100,000 in the previous tax year. From 2025 to 2026 onwards there is no limit — that bar was lifted in April 2025.

One more bar sits on that past-years page, and nowhere else: for some businesses the allowance counted as de minimis state aid, capped over 3 years, and a business over the cap could not claim — most likely where the business is both located in Northern Ireland and makes or sells goods or wholesale electricity. HMRC asks the state-aid question only for a previous year.

Who cannot claim at all — the employer. The first is the trap for small companies:
• A company with a single director who is its only employee liable for secondary Class 1 National Insurance.
• A public authority that is not a charity — a local authority, a town or parish council — however little of its work is of a public nature.
• Any other employer doing more than half its work in or for the public sector — unless it is a charity, which can claim even when its functions are wholly or mainly of a public nature.
• Within a group of connected companies or connected charities only one may claim, and an employer running several payrolls claims against only one of them.

Employees you cannot include in the claim — a separate rule. The employer keeps claiming on everyone else, if there is anyone else — HMRC says an employer of domestic staff alone cannot claim at all:
• An employee whose earnings fall within the off-payroll working rules.
• Someone employed for personal, household or domestic work — a nanny, a gardener — unless they are a care or support worker.

Who can: businesses doing less than half their work in the public sector, charities including community amateur sports clubs, and employers of a care or support worker.

UK-wide, for the current tax year.

Want your payroll checked against the conditions?""",
 bsky="""Employment Allowance: up to £10,500 off employer Class 1 National Insurance, claimed again every tax year. It never carries forward.""",
 pin_title="Employment Allowance: £10,500 and who cannot claim",
 pin="""UK Employment Allowance takes up to £10,500 off an employer's Class 1 National Insurance in a tax year. It is never automatic and must be claimed again every tax year. Which employers cannot claim: a company whose single director is its only employee liable for secondary Class 1, and an employer doing over half its work in the public sector unless it is a charity. Separately, a nanny or gardener in personal, household or domestic work cannot be included unless they are a care or support worker; an employer of domestic staff alone cannot claim.""",
 source="gov.uk/claim-employment-allowance/eligibility, /claim-for-past-years, plus HMRC's further employer guidance",
)

C["cold-weather-25"] = dict(
 ro="""Cold Weather Payment e £25 pentru fiecare 7 zile la rând în care temperatura medie din zona ta e zero grade sau mai jos — măsurată sau prognozată. Nu se depune cerere: vine automat, în contul în care intră ajutorul, în 14 zile lucrătoare.

Se numără gerul între 1 noiembrie 2026 și 31 martie 2027, după codul poștal.

Un lucru TREBUIE făcut: pe Universal Credit sau pe ESA legat de venit, dacă s-a născut un copil sau un copil sub 5 ani s-a mutat în casă, schimbarea de situație se anunță. Fără anunț, plata nu vine automat — iar copilul sub 5 ani dă dreptul.

Ajutoarele listate de GOV.UK:
• Pension Credit
• ESA legat de venit (grupul de activitate sau de sprijin, un supliment de dizabilitate severă sau sporită ori de pensionar, un copil cu dizabilitate ori unul sub 5 ani)
• Universal Credit, în condițiile de mai jos
• Support for Mortgage Interest, dacă solicitantul e tratat ca primind un ajutor care califică — numai cu un supliment de dizabilitate severă sau sporită ori de pensionar, un copil cu dizabilitate ori unul sub 5 ani în casă

Pe Universal Credit, amândouă condițiile: nici solicitantul, nici partenerul să nu fie angajat ori pe cont propriu ca ocupație principală, regulat, cu profit („gainfully self-employed"), ȘI unul din ei să aibă o problemă de sănătate ori un handicap cu capacitate limitată de muncă, sau un copil sub 5 ani în casă. Excepție: cu suma pentru un copil cu dizabilitate în dosar, dreptul există chiar dacă cineva muncește.

Cine NU primește:
• Cine locuiește în Scoția — acolo nu există. Cine ia un ajutor care dă dreptul primește Winter Heating Payment, o dată pe iarnă, automat, indiferent de vreme.
• Pe Universal Credit, dosarul fără amândouă condițiile și fără suma pentru un copil cu dizabilitate.

Se aplică în Anglia, Țara Galilor și Irlanda de Nord.

Nu știi unde se verifică?""",
 th="""Cold Weather Payment: £25 pentru fiecare 7 zile la rând cu media la zero grade sau mai jos, 1 nov 2026 – 31 mar 2027. Cerere nu se depune.

Dar pe Universal Credit și ESA legat de venit, un copil nou sau un copil sub 5 ani mutat în casă se anunță ca schimbare. Fără anunț, plata nu vine automat.""",
 li="""Cold Weather Payment is £25 for each period of 7 consecutive days where the average temperature in your postcode area is recorded as, or forecast to be, zero degrees celsius or below. Nothing is applied for: it arrives automatically, into the account the benefit is paid into, within 14 working days of the cold period.

It covers cold spells between 1 November 2026 and 31 March 2027, and it works off postcode rather than town or county.

There is one thing that does have to be done, and it is the line most often left out. GOV.UK: "You'll need to report a change in circumstances if you get Universal Credit or income-related Employment and Support Allowance (ESA) and either: you've had a baby; a child under 5 has come to live with you... You will not automatically get Cold Weather Payments if you do not." The payment is automatic; the circumstances it is worked out from are not — and the child-under-5 route to eligibility is exactly the one that depends on the change being reported.

The four qualifying benefits GOV.UK lists:
• Pension Credit
• Income-related Employment and Support Allowance, in a work-related activity or support group — or with a severe or enhanced disability premium, a pensioner premium, a disabled child, or a child under 5 living with you
• Universal Credit, on the conditions below
• Support for Mortgage Interest, where the claimant is treated as receiving a qualifying benefit AND one of these applies: a severe or enhanced disability premium, a pensioner premium, a disabled child, or a child under 5 living with them

On Universal Credit there are two conditions and both must hold: neither the claimant nor their partner is employed or "gainfully self-employed", AND the claimant or their partner has a health condition or disability with limited capability for work (with or without work-related activity), or a child under 5 living with them. The exception: a claim that includes a disabled child amount qualifies regardless of whether either of them is working.

Who does not get it:
• Anyone living in Scotland. GOV.UK is explicit: Cold Weather Payments cannot be had there. Winter Heating Payment is paid instead — once a winter, automatically and regardless of the weather, to people who get one of the benefits that make them eligible. It is gated on a qualifying benefit in the same way, so it is not a payment every Scottish household receives.
• On Universal Credit, a claim where either of the two conditions is missing and there is no disabled child amount in it.

England, Wales and Northern Ireland.

Want the official page to check it on?""",
 bsky="""Cold Weather Payment: £25 per 7 days at 0°C or below, Nov–Mar, England/Wales/NI. On UC or ESA, report a new child or it is not automatic.""",
 pin_title="Cold Weather Payment: £25 per 7 days at 0°C or below and who misses out",
 pin="""Cold Weather Payment pays £25 for each period of 7 consecutive days where the average temperature in your postcode area is recorded as, or forecast to be, 0°C or below, between 1 Nov 2026 and 31 Mar 2027. Paid automatically within 14 working days, with no claim to make. But on Universal Credit or income-related ESA, a new baby or a child under 5 moving in must be reported as a change, or it does not arrive automatically. Qualifying benefits: Pension Credit, income-related ESA, Universal Credit and Support for Mortgage Interest. England, Wales and NI only.""",
 disc_ro="Informații generale, nu consultanță pe beneficii. Cere sfat de specialitate.",
 disc_en="General information, not benefits advice. Get specialist advice.",
 source="gov.uk/cold-weather-payment and mygov.scot/winter-heating-payment",
)

# ----------------------------------------------------------------- 15
C["retur-30-zile"] = dict(
 ro="""Dacă un produs cumpărat de la un comerciant e defect, nu e cum l-a descris vânzătorul sau nu face ce i-ai spus că ai nevoie, în primele 30 de zile poți cere banii înapoi — nu doar o reparație. E legea, Consumer Rights Act 2015, nu politica magazinului.

Cele 30 de zile încep a doua zi după ce produsul e al tău și ți-a fost livrat. Dacă trebuia montat, de a doua zi după ce vânzătorul îți spune că s-a terminat.

Puțini știu asta: dacă în acest timp ceri o reparație sau o înlocuire, numărătoarea se oprește cât aștepți și pornește de unde a rămas. Iar dacă produsul vine tot defect, ai cel puțin 7 zile de atunci.

Banii trebuie dați fără întârziere nejustificată și în cel mult 14 zile de când vânzătorul e de acord că ți se cuvin.

Cine NU are cele 30 de zile:
• Dacă ai cumpărat de la un particular, nu de la un comerciant — adică de la cineva care vinde în cadrul activității lui, firmă sau om pe cont propriu. Legea se aplică doar între un comerciant și un consumator.
• Dacă ai cumpărat în totalitate sau în principal pentru afacerea ta. Dacă a fost mai mult pentru tine, rămâi „consumator".

Două lucruri care NU îți iau cele 30 de zile:
• Un defect arătat de vânzător înainte de cumpărare, sau vizibil la verificarea ta, nu mai poate fi reclamat ca proastă calitate — dar ceri banii dacă produsul nu e cum l-a descris sau nu face ce i-ai spus că ai nevoie.
• Produsele perisabile, care se alterează repede, au același drept, doar cu termen mai scurt — cât se poate aștepta rezonabil să țină acel produs, nu o listă fixă.

După cele 30 de zile îți rămâne dreptul la reparație sau înlocuire, iar dacă nici asta nu merge, la o reducere de preț sau la returnarea produsului.

Se aplică în tot Regatul Unit: Anglia, Țara Galilor, Scoția și Irlanda de Nord.

Vrei să citești legea în original?""",
 th="""Produs defect cumpărat de la un comerciant? În primele 30 de zile poți cere banii înapoi, nu doar o reparație. Banii vin în cel mult 14 zile de când vânzătorul e de acord.

Comerciant e oricine vinde în cadrul activității lui, firmă sau om pe cont propriu. De la un particular, legea nu se aplică.""",
 li="""The short-term right to reject is 30 days, and most people spend it without knowing they had it.

If goods bought from a trader are faulty, not as described, or not fit for a purpose you made known, the Consumer Rights Act 2015 gives you 30 days to reject them and take a refund — not a repair, not a credit note.

How the 30 days are counted: they begin the day after ownership or possession has passed to you and the goods have been delivered. Where the contract required installation, they begin the day after the trader tells you it is done.

The part almost nobody knows: if you ask for or agree to a repair or a replacement inside that window, the clock stops for the waiting period and resumes where it left off. And if what the trader supplies in response still does not conform, section 22(7) makes the limit 7 days after the waiting period ends — or the original limit extended by that period, if that is later. That is the rule for a repair that fails: if it works, what is left is the days that were left. And section 23(6) runs the other way: once you have asked for a repair, you cannot reject until the trader has had a reasonable time to carry it out, unless that would significantly inconvenience you.

A refund must be given without undue delay and in any event within 14 days of the trader agreeing you are entitled to one.

Who does not have the 30 days:
• Anyone who bought from a private individual rather than a trader. Part 1 applies to a contract between a trader and a consumer, so a private sale sits outside it entirely.
• Anyone buying for purposes wholly or mainly inside their own business — not a consumer for these purposes.

Two things that do NOT take the 30 days away:
• A fault specifically drawn to the buyer's attention before the contract, or one an examination the buyer actually made ought to have revealed. Section 9(4) takes that fault outside the satisfactory quality term only. The other two grounds are untouched: if the goods are not as described, or not fit for a purpose made known to the trader, the 30-day right to reject is still there.
• Goods that can reasonably be expected to perish sooner. They carry the same right on a shorter period — the end of the period they can reasonably be expected to last. The Act names no categories: the test is applied to the goods actually bought.

After the 30 days the remedies change rather than disappear: repair or replacement first, then a price reduction or the final right to reject if that fails.

Section 99 extends the Act to England and Wales, Scotland and Northern Ireland.

Want to read the Act itself?""",
 bsky="""Faulty goods from a trader: 30 days to reject and get a refund, not just a repair. Private sales are outside the Act.""",
 pin_title="30 days to reject faulty goods in the UK",
 pin="""The Consumer Rights Act 2015 gives a 30-day right to reject goods bought from a trader that are faulty, not as described or not fit for purpose — a refund, not just a repair. The 30 days begin the day after ownership has passed and the goods have been delivered, and the clock stops while a requested repair or replacement is carried out. A refund is due within 14 days of the trader agreeing to it. Buying from a private individual falls outside the Act, as does buying for your own business. Goods expected to perish sooner keep the right, on a shorter period. UK-wide.""",
 disc_ro="Informații generale, nu consultanță juridică. Cere sfat de specialitate.",
 disc_en="General information, not legal advice. Get specialist advice.",
 source="legislation.gov.uk/ukpga/2015/15/section/22 and legislation.gov.uk/ukpga/2015/15/part/1/chapter/2",
)

# ------------------------------------------------------------------ 16
C["ni-voluntar-pensie"] = dict(
  ro="""Ai lucrat în UK, dar nu în fiecare an? Pensia de stat se socotește în ani care contează — iar un an acoperit cu credite NI contează fără plată. Un an care nu contează e o gaură.

În 2026-2027: clasa 3 e £18,40 pe săptămână; clasa 2, pentru cine e pe cont propriu cu profit sub £7.105, £3,65. Doar ultimii 6 ani fiscali, termen 5 aprilie.

Pentru timpul petrecut în afara UK, regulile depind de anul fiscal: clasa 2 voluntară nu se poate plăti pentru 2026-2027 și anii de după, dar interdicția nu atinge 2025-2026 și anii mai vechi din fereastra de 6 ani, unde rămân regulile de dinainte. Clasa 3 are condiții, se cere la HMRC și nu plătești până nu vine scrisoarea cu suma și referința.

Cu dosar început după aprilie 2016, pensia nouă plină — £241,30 pe săptămână în 2026-2027 — cere 35 de ani care contează. De obicei ai nevoie de 10 ani ca să primești ceva — de obicei, pentru că anii din SEE (România e în SEE) pot intra la acest minim, nu la sumă, care se face pe anii din UK.

Cine NU poate plăti: cine nu are găuri — în afară de cine primește credite clasa 3 și poate plăti clasa 2; cine a trecut termenul; femeia măritată sau văduva, pentru un an fiscal în care alegerea cotei reduse a fost în vigoare tot anul — dar poate plăti din primul an în care nu a fost. Condiția e pe an fiscal, nu pe persoană.

Când plata nu folosește: un an în plus nu crește neapărat pensia — nu mai adaugă nimic după ce ai atins suma plină. Anul fiscal în care ajungi la vârsta de pensionare și anii de după nu se pot plăti, dar găurile mai vechi se pot plăti și după vârsta de pensionare. GOV.UK avertizează că plata voluntară nu crește întotdeauna pensia, de exemplu dacă ai fost contracted out.

În tot Regatul Unit. Plata voluntară nu e automată — multe credite NI, da.

Nu știi câți ani ai în dosar?""",

  th="""Ai lucrat în UK, dar nu în fiecare an? Pensia de stat se socotește în ani care contează.

În 2026-2027 clasa 3 e £18,40 pe săptămână, doar ultimii 6 ani fiscali.

GOV.UK scrie că plata voluntară nu crește întotdeauna pensia, de exemplu dacă ai fost contracted out. Verifică întâi previziunea și creditele NI.""",

  li="""The UK State Pension is counted in qualifying years, not in earnings — and a year counts through National Insurance credits as well as contributions paid. A year that does not count is a gap, and many gaps can be paid for, not all.

Voluntary rates for 2026/27: Class 3, the general class, £18.40 a week; Class 2, for the self-employed with profits under £7,105, £3.65.

The window: GOV.UK says "You can only pay voluntary contributions for the past 6 years", with 5 April as the annual deadline. Six years is the general rule: HMRC can allow a later payment in limited circumstances, with a right of appeal.

Time spent abroad: GOV.UK says which contributions you can pay "depend on the tax year you were living or working abroad". From the 2026 to 2027 tax year on, "You cannot pay voluntary Class 2 National Insurance contributions for time abroad" — but that bar does not reach the 2025 to 2026 tax year or any earlier year, which keep the previous rules and conditions. Class 3 for periods abroad has its own conditions and must be applied for: "Do not make any payments until you get a letter from HMRC" giving the amount and reference.

Why the years matter: a record started after April 2016 needs 35 qualifying years for the full new State Pension, £241.30 a week in 2026/27. And 10 qualifying years is the usual minimum before any is paid — usual, because contributions to an EEA country's state pension can count towards it, though not towards the amount, which rests on UK years.

Who cannot pay:
• anyone with no gaps, "unless you're getting Class 3 credits and are eligible to pay Class 2 contributions"
• anyone past the deadline for the years with gaps
• a married woman or widow, for any tax year throughout which a reduced rate election was in force — reg 132 SSCR 2001; she can pay from a tax year in which it was not in force throughout, and for Class 2 the unit is the contribution week
The condition sits on the year, not the person.

GOV.UK describes its forecast as showing "how much State Pension you could get" and "how you could increase it" — read it before paying: a further year adds nothing once the full rate is reached, and the year State Pension age is reached, and later years, cannot be paid for at all — though earlier gaps can still be paid for after State Pension age. GOV.UK warns: "Voluntary contributions do not always increase your State Pension, for example if you were contracted out."

UK-wide. A voluntary contribution is never automatic; many National Insurance credits are.

Want your National Insurance record read before you pay?""",

  bsky="""Gaps in a UK National Insurance record can often be filled — but paying does not always raise your State Pension. Check your forecast first.""",

  pin_title="UK voluntary National Insurance: £18.40 a week, 6-year window",

  pin="""Voluntary National Insurance for 2026/27: Class 3 is £18.40 a week, and Class 2, for the self-employed with profits under £7,105, is £3.65. Contributions are allowed for the past 6 tax years only, by 5 April. A record starting after April 2016 needs 35 qualifying years for the full new State Pension of £241.30 a week, and usually 10 qualifying years before anything is paid: EEA contributions count towards that minimum, not towards the amount, which rests on UK years. Paying does not always increase a State Pension — check the forecast and NI credits first.""",

  source="gov.uk/voluntary-national-insurance-contributions, /rates, /deadlines, /if-you-live-or-work-abroad · gov.uk/new-state-pension",
)

# ------------------------------------------------------------------ 17
C["dividende-10-75"] = dict(
  ro="""Dacă îți scoți banii din firma ta ca dividend, cota de bază a crescut. Din 6 aprilie 2026 se plătește 10,75%, nu 8,75%.

Cotele pentru 2026-2027, pe dividendele de peste alocație:
• 10,75% în banda de bază
• 35,75% în banda mare
• 39,35% în banda de sus

Cotele ating orice dividend primit de o persoană, nu doar pe cel din firma ta: acțiuni la bursă, fonduri, firme în care nu decizi tu.

Și 10,75% nu e costul scoaterii banilor: e taxa ta pe dividend, peste impozitul pe profit plătit deja de firmă. Iar dividendul se plătește doar din profitul disponibil pentru distribuire.

Exemplu, cu Personal Allowance deja folosit de alte venituri: £2.000 de dividende, banda de bază. Primii £500 fără taxă; restul, £1.500 × 10,75% = £161,25.

Au urcat primele două cote, cu două puncte. Cota de sus, 39,35%, a rămas la fel — dar în banda mare creșterea s-a simțit întreagă, la 35,75%.

Ce NU se impozitează:
• primii £500 de dividende într-un an fiscal — „dividend allowance", per persoană, nu per firmă
• dividendele care încap în partea nefolosită din Personal Allowance; ce trece peste se impozitează normal
• dividendele din acțiuni ținute într-un ISA valid, oricât ar fi — dar acțiunile firmei tale nu pot sta în ISA, iar cele ținute în afara ISA se impozitează normal

Profitul scos din activitatea ta pe cont propriu nu e dividend, deci cotele nu-l ating. Dar dacă ai acțiuni, dividendele de pe ele se impozitează ca la oricine.

Se aplică în tot Regatul Unit. Dacă depui Self Assessment, treci în declarație orice dividend, inclusiv pe cel din alocația de £500. Dacă nu depui: sub alocație nu ai ce să anunți; peste, îi spui HMRC după 5 aprilie și până pe 5 octombrie, iar taxa poate veni prin codul fiscal; de la £10.000 HMRC cere Self Assessment — prag din practica HMRC, nu din lege.

Nu știi cât îți rămâne din dividend?""",

  th="""Îți iei un dividend? Din 6 aprilie 2026 cota de bază e 10,75%, nu 8,75%.

Ating orice dividend, nu doar pe cel din firma ta.

Nu se impozitează: primii £500 pe an, dividendele care încap în Personal Allowance nefolosit, și cele din acțiuni ținute în ISA — dar acțiunile firmei tale nu pot sta în ISA.""",

  li="""If you take profit out of your own limited company as a dividend, the basic rate changed on 6 April 2026: 10.75%, up from 8.75%.

Dividend rates for 2026/27, on dividends above the allowance:
• 10.75% at the basic rate
• 35.75% at the higher rate
• 39.35% at the additional rate

These are not company-specific rates. They reach every dividend an individual receives — listed shares, funds, a company you do not control. A shareholder with a portfolio outside an ISA is caught as much as an owner-manager.

And 10.75% is not the cost of getting money out of a company. It is the shareholder's income tax, on top of the corporation tax the company has already paid on that profit — and a dividend can only be paid out of profits available for the purpose.

Worked, with the Personal Allowance already used by other income: £2,000 of dividends for a basic-rate taxpayer. The first £500 is free; the remaining £1,500 × 10.75% = £161.25.

What actually changed: the ordinary and upper rates rose by two points each. The additional rate stayed at 39.35% — but a shareholder taxed at the upper rate took the full two points, and part of a very large dividend can still fall in that band, so the rise did not stop short of high earners.

What is not taxed:
• the first £500 of dividends in the year — the dividend allowance, per person per tax year, not per company
• dividends that fall inside the unused part of a Personal Allowance; anything above it is taxed at the normal rates
• dividends on shares held inside a valid ISA, at any amount — but shares in an ordinary private limited company are not qualifying ISA investments, so an owner-manager cannot hold their own company that way, and holdings outside the ISA are taxed normally

Profit drawn from an unincorporated trade is trading profit, not a dividend, so these rates do not reach it. Dividends on shares that sole trader holds are taxed like anyone else's.

UK-wide. Dividend tax is not deducted at source, and what has to be reported depends on whether you file. If you send a Self Assessment return, you must report any dividend income on it — including dividends inside the £500 allowance. If you do not: nothing to tell HMRC where the dividends are within the allowance; above it, tell HMRC after 5 April and by 5 October, with the tax collectable through your tax code; from £10,000 HMRC asks for a return. That £10,000 tier is HMRC's administrative practice, not a statutory threshold. Unused Personal Allowance is not reported — it is given automatically.

Planning the next dividend? Worth running the numbers before the money moves.""",

  bsky="""From 6 April 2026, dividends over the £500 allowance: 10.75% basic rate, up from 8.75%, then 35.75% and 39.35%. Not just your company's.""",

  pin_title="UK dividend tax 2026/27: basic rate 10.75%, up from 8.75%",

  pin="""UK dividend tax from 6 April 2026, above the £500 allowance: 10.75% basic, 35.75% higher, 39.35% additional. The first two rose two points; the additional did not. They reach any dividend, not just your own company's. £2,000 of dividends, allowance used elsewhere: £500 free + £1,500 at 10.75% = £161.25. Untaxed: the first £500, dividends inside unused Personal Allowance, and those on shares in a valid ISA — but your own company's shares cannot go in an ISA. Sole-trade profit is not a dividend; dividends on a sole trader's shares are taxed like anyone's.""",

  gbp="""The basic rate on dividends is 10.75% now, not 8.75%.

For 2026/27, on dividends above the allowance: 10.75% basic rate, 35.75% higher, 39.35% additional. The first two rose by two points on 6 April 2026; the additional rate is unchanged. They apply to listed shares and funds as much as to a company you own.

10.75% is your tax on the dividend, on top of the corporation tax the company already paid on that profit — and a dividend can only be paid out of profits available for the purpose.

Worked example, with the Personal Allowance already used by other income: £2,000 of dividends at the basic rate — the first £500 free, then £1,500 × 10.75% = £161.25.

Not taxed: the first £500 of dividends in the year; dividends falling inside an unused Personal Allowance, with anything above taxed normally; and dividends on shares held in a valid ISA — though your own company's shares cannot go in an ISA.

Profit you draw from your own sole trade is not a dividend, so these rates do not touch it — but dividends on shares you hold are taxed like anyone's.

Running a limited company around Luton or Birmingham? Message 0330 133 1886 and we will set out the position before you take the next payment.

Source: gov.uk/tax-on-dividends""",

  source="gov.uk/tax-on-dividends and gov.uk/tax-on-dividends/how-to-report-tax-on-dividends",
)

# ------------------------------------------------------------------ 18
C["birou-acasa-26"] = dict(
  ro="""Lucrezi pe cont propriu și faci munca de acasă? Scazi o sumă fixă pe lună din profit, în locul unor cheltuieli curente ale casei: curățenie, căldură, lumină, apă la contor.

Suma, după orele de acasă într-o lună:
• 25-50 de ore → £10
• 51-100 de ore → £18
• 101 de ore sau mai multe → £26

Exemplu: 60 de ore pe lună, tot anul. 12 × £18 = £216 scăzuți din profit. Se numără și luna începută, nu doar lunile întregi.

HMRC cere să ții evidența orelor lucrate acasă, pe tot anul.

Se numără orice oră lucrată în casa ta numai pentru afacere, nu doar producția sau actele. Și orele lucrate de angajații tăi în casa ta, dar o oră o singură dată.

Sub 25 de ore într-o lună nu iei nimic pe luna aceea; celelalte luni se iau normal. Se cer 25 de ore sau mai multe: o lună cu exact 25 intră.

Cine NU poate folosi suma fixă:
• firmele Ltd, și o asociere în care intră o firmă. Interdicția e pe firmă, nu pe om: dacă directorul are și activitate pe cont propriu, în aceea poate
• cine cere trading allowance — cu scutirea aceea nu mai deduci nicio altă cheltuială
• angajații și directorii, pentru munca de acasă din slujbă. Acolo e altă regulă: din 6 aprilie 2026 angajatul nu mai cere singur cheltuielile casei, dar plata de la angajator rămâne netaxată

Astea se cer pe lângă suma fixă, nu în locul ei, cu documente:
• chiria, council tax, asigurarea, reparațiile — numai dacă o parte din casă e folosită exclusiv pentru afacere, o perioadă anume
• telefonul și internetul — partea de muncă, sau tot, dacă folosirea personală e nesemnificativă

Alegi doar între suma fixă și cheltuielile curente socotite real. Cele de sus le ceri oricum.

Se trece în declarația de Self Assessment. În tot Regatul Unit, nimic nu vine automat, iar sumele se pot schimba.

Nu știi ce poți scădea de acasă?""",

  th="""Lucrezi pe cont propriu și faci munca de acasă? Scazi o sumă fixă pe lună, după ore: 25-50 de ore → £10, 51-100 → £18, 101 sau mai multe → £26.

HMRC cere să ții evidența orelor lucrate acasă.

Sub 25 de ore într-o lună nu primești nimic pe luna aceea. Și firmele Ltd nu pot folosi regula asta deloc.""",

  li="""Self-employed with the work happening at home: HMRC's simplified expenses take a flat amount off profit each month in place of apportioning the home's running costs — cleaning, heat and light and metered water among them.

The rates, by hours of qualifying work at home a month:
• 25 to 50 hours → £10
• 51 to 100 hours → £18
• 101 hours or more → £26

Worked: 60 hours a month at home for a full year is 12 × £18 = £216 off profit. A month, or part of a month, carries the full band, so a trade starting mid-month is not pro-rated.

Keep a record of the hours you work at home across the year.

Qualifying work is any work done in the home wholly and exclusively for the trade — not only producing, record-keeping and marketing. Work done there by the trader's own employees counts too, with any one hour taken into account once.

Assessed month by month, so a busy month can reach £26 and a quiet one £10 in the same year. A month under 25 hours produces no amount for that month, and every other month in the period is claimed as normal. The floor is 25 hours or more, so exactly 25 hours qualifies.

Who cannot use it:
• limited companies, and a partnership with a company as a partner. GOV.UK is explicit: "Simplified expenses cannot be used by limited companies or business partnerships involving a limited company". That bars the entity whose profits are computed, not a person by job title — a director who also carries on a trade in their own name can use the flat rate in that trade
• anyone claiming the trading allowance, which rules out deducting any other expenses or allowances
• employees and directors, for the use of home in the employment. That sits in the employment rules, not here — and since 6 April 2026 an employee can no longer deduct additional household expenses themselves, so what remains is a homeworking payment from the employer, which is still exempt

Claimed on top of the flat rate rather than instead of it, and on either method:
• rent or mortgage interest, council tax, insurance, general repairs and water rates — but only where part of the home is set aside solely for trade use for a specific period, apportioned by area and time
• telephone and broadband, at the business share, or the full cost where private use is not significant

So the either/or is narrower than it looks: the flat rate stands in only for those apportioned running costs. Using it is optional; the choice is made on the figures.

UK-wide, claimed on the Self Assessment return.

Worth checking which of the two gives the better result before January.""",

  bsky="""Self-employed and working from home? Simplified expenses give £10, £18 or £26 a month by hours. A month under 25 hours, nothing that month.""",

  pin_title="Working from home self-employed: £10, £18 or £26 a month",

  pin="""HMRC simplified expenses, self-employed working from home: £10 a month for 25-50 hours, £18 for 51-100, £26 for 101 or more. It replaces only the home's apportioned running costs: cleaning, heat and light, metered water. Rent, council tax, insurance and repairs are claimed on top, not instead, but only if part of the home is set aside solely for the trade. Telephone and broadband too: business share, or in full if private use is not significant. Keep a record of your hours at home. Under 25 hours in a month, nothing that month. Limited companies cannot use it. On the Self Assessment return.""",

  source="gov.uk/simpler-income-tax-simplified-expenses, /working-from-home and gov.uk/hmrc-internal-manuals/business-income-manual/bim75010",
)

# ------------------------------------------------------------------ 19
C["warm-home-150"] = dict(
  ro="""£150 se scad din factura de electricitate în această iarnă, în Anglia, Scoția și Țara Galilor. Nu primești bani în mână — furnizorul taie suma din factură.

Ce trebuia să fie adevărat pe 23 august 2026 — aceeași dată în toate trei:
• furnizorul e în schemă — aproape toți sunt
• tu, partenerul declarat la DWP sau reprezentantul tău legal erați pe contul de electricitate — titular de cont sau numele pe factură
• primeai un ajutor pe venit. În Anglia și Țara Galilor: Universal Credit, Housing Benefit, ESA pe venit sau Pension Credit

În Anglia și Țara Galilor vine de obicei automat, cu scrisoare, de la sfârșitul lui octombrie 2026 până la începutul lui ianuarie 2027. Dacă scrisoarea cere informații în plus, ea îți dă numărul de sunat până pe 26 februarie 2027. Pe factură până pe 31 martie 2027. Aceleași termene și în Scoția.

Scoția are altă listă de ajutoare și, pentru unii, alt drum: automat pentru „core group”. Altfel ceri direct furnizorului, care poate pune criterii în plus, iar numărul de reduceri e limitat — și rămâi la acel furnizor până se aplică reducerea.

N-a venit scrisoarea până la începutul lui ianuarie 2027? Contactează schema: gov.uk/the-warm-home-discount-scheme.

Cine NU îl primește — nu e lista completă:
• cine nu are contul pe numele lui, al partenerului sau al reprezentantului legal. Poți fi pe Universal Credit și să nu primești nimic
• Irlanda de Nord: schema nu există acolo. GOV.UK trimite la Affordable Warmth — bani pentru izolație și încălzire, nu o reducere la factură
• cine stă permanent în casă de bătrâni, locuințele fără curent pentru uz casnic
• caravanele, în general: excluderea ține de cum e clasată locuința în registre. Un număr mic de locuințe permanente pot intra, dacă suni la helpline și dovedești că e singura ta locuință legală și că ești pe factură

Pentru contabilitate, ne găsești aici:""",

  th="""£150 se scad din factura de curent. În Anglia și Țara Galilor vine de obicei automat. În Scoția, automat pentru „core group” — altfel ceri la furnizor.

Pe 23 august 2026 conta ajutorul pe venit și contul pe numele tău, al partenerului sau al reprezentantului legal.

Irlanda de Nord nu are schema.""",

  li="""The Warm Home Discount takes £150 off an electricity bill in England, Scotland and Wales. It is a discount applied by the supplier, not a payment — no money reaches the household.

Three things had to be true on 23 August 2026 — the qualifying date in all three nations:
• the energy supplier is part of the scheme — required of every supplier with over 1,000 domestic customers, so nearly always met
• a qualifying means-tested benefit was in payment. In England and Wales: Universal Credit, Housing Benefit, income-related ESA or Pension Credit
• the electricity account was in the name of the claimant, their partner as notified to DWP, or their legal representative — as account holder or named on the bill

In England and Wales it is usually automatic. Letters go out from late October 2026 to early January 2027. Where a letter asks for more information, that letter carries the helpline number to call by 26 February 2027. The discount is applied to the bill by 31 March 2027. The same three dates apply in Scotland.

Scotland runs on its own list, and being outside its core group is a different route, not an exclusion. The core group — Pension Credit, and some Universal Credit, Income Support, JSA and ESA awards — gets it automatically. The broader group, which includes Housing Benefit and the disability payments, applies to the supplier, which may set extra criteria, and discounts are capped. An applicant must stay with that supplier until the discount is paid, so switching can cost the £150.

No letter by early January 2027? GOV.UK says to contact the scheme in writing.

Who does NOT get it — not the complete list:
• anyone whose electricity account is in none of those three names: a household can be on Universal Credit and get nothing. Where a spouse or adult child who holds the account is also the claimant's appointee, attorney or deputy, that is a legal representative and the condition is met
• Northern Ireland: GOV.UK states the scheme is not available there and signposts Affordable Warmth — a grant for insulation and heating work, not a bill discount and not £150
• people permanently in a care home, and homes not supplied with electricity mainly for domestic use
• caravans are generally excluded, by how the property is classed in property records, and no letter goes to such an address. A small number of permanent residences can still qualify, by calling the helpline and evidencing that the caravan is the sole legal residence and that they are named on the bill
• park home residents supplied through the site owner, on a separate route

Prepayment meters still qualify: the account holder qualifies with no paper bill.""",

  bsky="""£150 off an electricity bill: England, Scotland, Wales. Three conditions, not one. Scotland: core group automatic, others apply.""",

  pin_title="Warm Home Discount: £150 off, and who misses out",

  pin="""£150 off an electricity bill in England, Scotland and Wales — from the supplier, not paid to you. Qualifying date in all three: 23 August 2026. You, your DWP-notified partner or your legal representative had to be on the account and getting a qualifying benefit (the list differs by nation). Usually automatic in England and Wales; on the bill by 31 March 2027. Scotland: core group automatic; others apply to their supplier and stay with it. Not the whole list. Missing: anyone off the account; Northern Ireland; care homes; homes classed as caravans in records.""",

  disc_ro="Nu evaluăm dreptul la ajutoare și nu depunem cereri. Condițiile sunt pe GOV.UK.",
  disc_en="We do not assess benefit entitlement or submit applications. Conditions on GOV.UK.",
  source="gov.uk/the-warm-home-discount-scheme",
)

# ------------------------------------------------------------------ 20
C["concediu-56-saptamani"] = dict(
  ro="""Concediul plătit nu e un bonus, e un drept. GOV.UK îl scrie în săptămâni: 5,6 săptămâni pe an pentru aproape toți cei din categoria „worker".

În zile: 5 zile pe săptămână → 28 de zile plătite pe an; 4 zile → cel puțin 22,4; 3 zile → cel puțin 16,8.

Plafonul: 28 de zile e maximul din lege. Cine lucrează 6 zile pe săptămână are tot 28, nu 33,6. Vechime nu se cere, iar primul an se dă proporțional.

Zilele se iau în anul lor de concediu, dar nu se pierd oricum: prin acord, până la 8 din cele 28 trec în anul următor; din concediu medical le poți lua în 18 luni de la finalul acelui an; din concediu de maternitate sau paternitate trec în anul următor; iar dacă angajatorul nu ți-a recunoscut dreptul, nu ți-a dat o ocazie rezonabilă să le iei sau nu ți-a spus că le pierzi, trec până la 20 de zile — la ore neregulate sau parte din an, tot concediul. În bani, în loc de concediu, se plătesc doar la încetarea contractului.

Sărbătorile legale nu se adaugă: nu trebuie date ca zile libere plătite și pot intra în cele 28.

Cine NU are acest drept: îl are cine lucrează personal pentru cineva care nu e clientul afacerii lui. „Freelance" sau „zero hours" pe hârtie poate însemna tot „worker": contează cum merge relația în practică, nu eticheta. Statutul îl decid tribunalele, nu noi.

La ore neregulate se socotește altfel, nu dispare: din anii de concediu de la 1 aprilie 2024, concediul se adună ca 12,07% din orele lucrate. Doar pentru cine are, prin contract, ore în mare parte variabile, sau lucrează doar o parte din an, cu pauze neplătite de cel puțin o săptămână. Acestora concediul poate fi plătit odată cu salariul, 12,07% peste plată — altceva decât plata zilelor nestate.

GOV.UK acoperă Anglia, Scoția și Țara Galilor; în Irlanda de Nord nu există 12,07% și nici plata concediului cu salariul.""",

  th="""Concediul plătit e un drept pentru aproape toți: 5,6 săptămâni pe an. 5 zile pe săptămână → 28 de zile; 3 zile → cel puțin 16,8.

Sărbătorile legale pot intra în cele 28.

Cine NU are dreptul: cine își poartă propria afacere, cu clienții lui. Statutul îl decid tribunalele.""",

  li="""Statutory paid holiday is written in weeks: almost all workers get 5.6 weeks a year.

In days: a 5-day week → 28 paid days; a 4-day week → at least 22.4; a 3-day week → at least 16.8.

There is a cap. "Statutory paid holiday entitlement is limited to 28 days", so a worker on a 6-day week still gets 28, not 33.6.

Bank holidays are not an addition: they "do not have to be given as paid leave" and may be counted towards statutory leave, so 28 days plus bank holidays is not safe to assume.

Who does NOT have the right: people genuinely in business on their own account. The test is reg 2(1)(b) of the Working Time Regulations 1998 — work done personally for a party who is not, under the contract, a client or customer of a business the individual carries on. Courts and tribunals decide status, on how the relationship works in practice — not the label.

The outright exclusions are narrow. Great Britain, reg 18: seafarers, sea-fishermen and inland waterways workers are outside the Regulations; the leave provisions are disapplied for civil aviation workers and, where characteristics peculiar to the service inevitably conflict, the armed forces, the police and certain civil protection activities.

Irregular hours mean a different calculation, not none: for leave years from 1 April 2024, irregular hours and part-year workers accrue 12.07% of hours worked. Rolled-up holiday pay is that 12.07% paid as an uplift with the wages, for those two groups only — a different thing from payment in lieu of untaken leave, which is confined to the end of the employment.

No qualifying period: the right runs from day one, with the first leave year pro-rated. Leave is normally taken in its own leave year, but does not simply lapse. An agreement can carry up to 8 of the 28 days into the next year. Leave untaken through sickness must be taken within 18 months of that leave year's end; leave untaken through statutory family leave carries into the next year; and up to 20 days carry over — the whole entitlement for irregular hours or part-year workers — where the employer failed to recognise the right, to give a reasonable opportunity to take the leave or encourage it, or to warn that untaken leave would be lost.

Northern Ireland's entitlement is identical — 5.6 weeks, capped at 28 days — under its own Working Time Regulations 2016, which contain no irregular hours, part-year, 12.07% or rolled-up holiday pay provision. Acas has no jurisdiction there: a claimant must notify the Labour Relations Agency and consider its Early Conciliation before a tribunal claim. Acas helps in England, Scotland and Wales only.""",

  bsky="""Great Britain: 5.6 weeks' paid holiday a year, capped at 28 days. It follows doing the work personally, not the label.""",

  pin_title="UK paid holiday: 5.6 weeks, capped at 28 days",

  pin="""Paid holiday in Great Britain is 5.6 weeks a year for almost anyone classed as a worker, capped at 28 days; a contract may give more. A 5-day week gives 28 paid days, a 3-day week at least 16.8. Bank holidays need not be paid leave and may count in the 28. A freelance, casual, zero hours or self-employed label does not decide it: what counts is doing the work personally for someone who is not your own client. From 1 April 2024 leave years, workers with wholly or mostly variable contractual hours and part-year workers accrue 12.07% of hours worked.""",

  disc_ro="Informații generale, nu consiliere juridică. Dispute: Acas; în Irlanda de Nord, LRA. Noi facem payroll.",
  disc_en="General information, not legal advice. For holiday disputes: Acas. We run payroll.",
  source="gov.uk/holiday-entitlement-rights and gov.uk/employment-status/worker",
)

# Threads caps a post at 500 characters through the API. Over that, Metricool
# returns "Media container not created by unknown cause" — a message that points
# at the images and has nothing to do with them. On 5 November 2026 a
# 638-character caption failed, a 755-character one failed, and a 488-character
# one published, on the same four images Facebook and Instagram accepted in the
# same second. So Threads gets its own post and its own caption: the hook, the
# single most useful fact, the who-does-NOT line, the number, the disclaimer and
# the four brand tags. No worked example, no topical tags — that is what fits.
# ---------------------------------------------------------------- 2026-11-09
# Every body below was measured against limits.py, not judged by eye. The
# first draft put 16 captions over their caps — twelve Pinterest and feed
# bodies, one LinkedIn and two Bluesky — and they were shortened until the
# gate passed. Shorter copy, never a smaller limit.
C["penalizari-31-ianuarie"] = dict(
 ro="""Depui declarația pe 1 februarie în loc de 31 ianuarie? £100.

Și £100 se plătesc chiar dacă nu ai nicio taxă de dat. Amenda se aplică chiar dacă nu e nicio taxă de plătit și chiar dacă ai plătit taxa la timp. Declarația pe zero nu te scapă.

Cum crește, dacă o lași:
• o zi întârziere — £100
• după 3 luni — £10 pe zi, până la £900 în total
• după 6 luni — încă 5% din taxă sau £300, cât e mai mult
• după 12 luni — iar 5% sau £300

Plata întârziată se numără separat de depunere: 5% din cât ai rămas de plătit la 30 de zile, apoi iar la 6 și la 12 luni. Plus dobândă în fiecare zi, de la 1 februarie — 7,75% până pe 23 noiembrie 2026, apoi 8%.

Cine NU plătește £100:
• cine nu a primit niciodată de la HMRC cererea de a depune. Amenda e pentru o declarație cerută; dacă nu ți-a cerut nimeni nimic, nu ai ce depune târziu.
• cine nu mai trebuie să depună și anunță HMRC din timp: obligația se retrage și amenda se anulează. Timpul contează — HMRC are nevoie de timp să analizeze cererea înainte de 31 ianuarie, iar dacă anunți prea târziu amenda rămâne.
• cine are motiv întemeiat (un deces în familie, o internare neașteptată). Se contestă online sau cu formularul SA370. „Nu am primit notificare de la HMRC" nu e motiv acceptat.

£100 nu scade în funcție de cât ai de plătit — nici dacă taxa iese zero. Se anulează, se plătește, sau HMRC o reduce doar în circumstanțe speciale, care nu includ lipsa banilor.

Nu ai banii acum? Dacă depui la timp, poți cere un plan de plată în rate — HMRC îl poate aproba online dacă datorezi sub £30.000 și te încadrezi în condițiile lor. Dobânda curge oricum, dar penalizările se opresc cât timp respecți planul.

E la fel în toată Marea Britanie. Pe hârtie nu se mai poate depune: termenul de 31 octombrie 2026 a trecut. Rămâne online, până pe 31 ianuarie 2027.

Nu ești sigur dacă trebuie să depui?""",
 th="""Depui declarația cu o zi întârziere? £100 — chiar dacă nu ai nicio taxă de plătit. După 3 luni se adaugă £10 pe zi, până la £900.

Cine NU plătește: cine nu a primit niciodată de la HMRC cererea de a depune. Iar dacă nu mai trebuie să depui, HMRC poate anula amenda — dar anunță-i înainte de 31 ianuarie.""",
 li="""File your Self Assessment return on 1 February instead of 31 January and it costs £100.

The £100 is charged even if you owe nothing. The penalty applies even if there is no tax to pay, and even if the tax due was paid on time. A nil return does not save you.

How it grows:
• one day late — £100
• after 3 months — £10 a day, up to £900
• after 6 months — a further 5% of the tax or £300, whichever is greater
• after 12 months — another 5% or £300

Paying late is a separate regime from filing late: 5% of the unpaid tax at 30 days, again at 6 months, again at 12. Interest runs daily from 1 February at base rate plus 4% — 7.75% to 23 November 2026, then 8%.

Who does not pay the £100:
• anyone HMRC never sent a notice to file. The penalty attaches to a return HMRC required; with no notice there is nothing to file late.
• anyone who no longer needs to file and says so in time. HMRC can withdraw the notice, and late filing penalties are then cancelled. Timing is the trap: HMRC needs time to review the request before 31 January, and leaving it too late means the penalty stands.
• anyone with a reasonable excuse — a bereavement, an unexpected hospital stay, a serious illness. Appeal online or on form SA370. "You did not get a reminder from HMRC" is on the rejected list.

The £100 is not scaled to the tax — a nil return does not shrink it. It is cancelled, paid, or reduced only where HMRC accepts special circumstances, which do not include inability to pay.

Cannot pay? File on time anyway and ask for a payment plan — HMRC can agree one online where you owe under £30,000 and meet its conditions. Interest still runs, but penalties stop while you keep to the plan. The filing deadline itself moves for nothing.

Two points of precision: the £10 daily penalties are not automatic — HMRC must decide to charge them and give written notice — and at twelve months, 5% is the ordinary case, not a ceiling. Where information is deliberately withheld and concealed, the statutory penalty is the greater of 100% of the tax and £300.

Also worth knowing: the Making Tax Digital points-based regime does not govern this deadline — current penalties apply to the 2025/26 return due 31 January 2027. Anyone who volunteered for MTD early should check which regime they are on.

Paper filing closed on 31 October 2026. Online, by 31 January 2027, is the only route left.""",
 bsky="""File one day late and it is £100 — even with no tax to pay. £10 a day after 3 months. No notice to file, no penalty.""",
 pin_title="Why a late UK tax return costs £100 even with no tax to pay",
 pin="""The UK Self Assessment return for 2025/26 is due online by 31 January 2027. One day late is a £100 penalty, charged even where no tax is owed. After three months HMRC can add £10 a day up to £900; at six and twelve months, a further 5% of the tax or £300, whichever is greater. Paying late is separate: 5% of the unpaid tax at 30 days, again at 6 and 12 months, plus daily interest. Who does not pay the £100: anyone HMRC never sent a notice to file, and anyone who no longer needs to file and tells HMRC in time. UK-wide. Ola Accountancy, Luton and Birmingham.""",
 gbp="""File the 2025/26 Self Assessment return one day after 31 January 2027 and the penalty is £100. HMRC charges it even if you owe no tax at all and even if the tax was paid on time, so a nil return is no protection.

After three months HMRC can add £10 a day, up to £900. At six months and again at twelve, a further 5% of the tax or £300, whichever is greater. Paying late is separate: 5% of the unpaid tax at 30 days, then again at 6 and 12 months, with interest running daily.

Who does not pay the £100: anyone HMRC never sent a notice to file, and anyone who no longer needs to file and tells HMRC in good time — HMRC can withdraw the obligation and cancel the penalty. Leave it too late and it stands.

Paper filing closed on 31 October 2026. Online by 31 January 2027 is the only route left, and the tax is due the same day.

Not sure you have to file at all? Ola Accountancy, Luton and Birmingham.""",
 source="gov.uk/self-assessment-tax-returns/penalties",
)

C["camera-inchiriata-7500"] = dict(
 ro="""Închiriezi o cameră în casa în care locuiești? Primii £7.500 pe an sunt fără taxe.

Scutirea se numește Rent a Room. Nu o ceri, nu completezi nimic, nu anunți pe nimeni: dacă încasezi £7.500 sau mai puțin într-un an fiscal, se aplică automat.

Se numără cât ÎNCASEZI, nu cât îți rămâne. Adică chiria, plus orice bani iei pentru mese, curățenie sau spălat rufe. Cheltuielile nu se scad din cifra asta.

Partea pe care o ratează lumea: £7.500 e limita unei persoane, dar scade la £3.750 dacă și altcineva încasează chirie din aceeași casă. Cazul obișnuit e un cuplu cu casa pe amândoi: fiecare are £3.750, nu £7.500, și nu se adună la £15.000.

Peste limită depui declarație și alegi una din două:
• plătești pe profitul real — ce ai încasat minus cheltuieli
• plătești doar pe cât ai încasat peste £7.500, fără să scazi nicio cheltuială
HMRC folosește automat prima variantă. A doua se cere în scris.

Nu se aplică la:
• camera nemobilată. Și atenție: dacă ai ORICE închiriere nemobilată în aceeași casă, HMRC spune că pierzi scutirea și pentru camera mobilată.
• casa împărțită în apartamente separate
• camera dată ca birou, pentru o afacere sau ca depozit
• o casă care nu e casa în care locuiești când o închiriezi
• casa din UK închiriată cât timp tu stai în altă țară

Merge și dacă stai în chirie și subînchiriezi o cameră — nu trebuie să fii proprietar. Nu merge pentru firme sau parteneriate.

Două lucruri de care nimeni nu te avertizează. Scutirea de £1.000 pentru venituri din chirii NU se poate folosi peste Rent a Room — sunt alternative, nu se adună. Și dacă primești un chiriaș, de regulă pierzi reducerea de 25% la council tax pentru persoana singură; trebuie să anunți primăria.

Se aplică la fel în toată Marea Britanie. Înregistrarea ca landlord e altă poveste și diferă pe națiuni.

Nu știi dacă intri în scutire?""",
 th="""Închiriezi o cameră în casa ta? Primii £7.500 pe an sunt fără taxe, automat — nu ceri nimic.

Se numără cât încasezi, nu cât îți rămâne: chiria plus banii pe mese sau curățenie.

Cine NU are £7.500: dacă și altcineva ia chirie din aceeași casă (de obicei partenerul), fiecare are £3.750. Nu se adună la £15.000.""",
 li="""Letting a room in the home you live in? The first £7,500 a year is tax free.

The relief is Rent a Room. You do not claim it, you fill nothing in and you tell nobody: take £7,500 or less in a tax year and it applies automatically.

It counts what comes IN, not what you keep — the rent, plus anything charged for meals, cleaning or laundry. Expenses are not deducted from that figure.

The part people miss: £7,500 is an individual's limit, and it halves to £3,750 where anyone else also receives letting income from the same home. The ordinary case is a couple who own the house together — £3,750 each, not £7,500, and nothing adds up to £15,000.

Over the limit you file a return and choose:
• tax on your actual profit — receipts less expenses
• tax on receipts above £7,500, with no expenses deductible at all
HMRC defaults to the first. The second has to be elected in writing.

It does not apply to:
• unfurnished accommodation. And note the sting: HMRC says any unfurnished letting in the same residence makes you a non-qualifying individual, so the furnished letting loses the relief too.
• a house converted into separate flats
• a room let as an office, for a business or for storage — with a narrow carve-out where a lodger works at home in the evenings or a student is given study facilities
• accommodation that is not part of your main home when you let it
• a UK home let while you live abroad

It works if you rent the property yourself and sublet a room — ownership is not required. It does not work for companies or partnerships.

Two things nobody warns you about. The £1,000 property allowance cannot be stacked on top of Rent a Room; they are alternatives for the same income. And taking in a lodger normally ends the 25% council tax single person discount, which the council has to be told about unless the lodger falls in a disregarded category.

UK-wide as a matter of tax. Landlord registration and licensing is a separate question and genuinely differs by nation.""",
 bsky="""A lodger in your own home: first £7,500 a year tax free, automatically. But if anyone else takes rent from the same house, it is £3,750 each.""",
 pin_title="Rent a Room: £7,500 tax free, or £3,750 if you are not the only one",
 pin="""The UK Rent a Room Scheme makes the first £7,500 a year from letting a furnished room in your own home tax free, automatically. It counts gross receipts — rent plus any charge for meals, cleaning or laundry — not profit. The limit is an individual's, and halves to £3,750 where anyone else also receives letting income from the same home: the ordinary case for a couple who own it together. It does not apply to unfurnished rooms, a house split into separate flats, a room let as an office, or a UK home let while you live abroad. UK-wide. Ola Accountancy, Luton and Birmingham.""",
 source="gov.uk/rent-room-in-your-home/the-rent-a-room-scheme",
)

C["cgt-60-zile"] = dict(
 ro="""Ai vândut o casă care nu era casa în care locuiai? Ai 60 de zile.

60 de zile de la ziua în care s-a încheiat vânzarea — completion — nu de la semnarea contractului. Și în cele 60 de zile faci două lucruri: declari ȘI plătești.

Nu e Self Assessment. Se depune separat, într-un cont la HMRC pentru proprietăți din UK. Dacă oricum depui Self Assessment, vânzarea se trece și acolo — e în plus, nu în loc.

Cât se plătește: 18% sau 24% din câștig, după banda de impozit în care intră câștigul. Primii £3.000 de câștig din tot anul nu se impozitează.

Cine NU declară în 60 de zile:
• casa ta, dacă ai avut o singură casă și ai locuit în ea tot timpul cât a fost a ta. Se numește Private Residence Relief. Condițiile sunt toate: o singură casă, locuită tot timpul, fără o parte închiriată (un chiriaș în casă nu strică), fără o cameră folosită exclusiv pentru o afacere, teren sub 5.000 m². Dacă una nu se potrivește, poate fi ceva de plătit.
• dacă nu iese taxă de plătit: câștigul intră în cei £3.000, sau e acoperit de pierderi. HMRC spune limpede că nu trebuie declarat nimic când nu e nimic de plătit.
• transferul către soț, soție sau partener civil cu care locuiești.
• acțiuni, spații comerciale, teren: merg în Self Assessment, la termenul obișnuit.

Un lucru pe dos, care prinde lumea: dacă NU ești rezident fiscal în UK, trebuie să declari fiecare vânzare de proprietate sau teren din UK — locuință sau nu — chiar dacă nu iese nicio taxă și chiar dacă ai pierdut bani.

Ce costă întârzierea: £100 imediat, apoi la 6 luni și la 12 luni câte 5% din taxă sau £300, cât e mai mult. Plus dobândă pe taxa neplătită — 7,75% până pe 23 noiembrie 2026, apoi 8%.

E la fel în toată Marea Britanie. Taxa pe care o plătește cumpărătorul la achiziție e altceva și diferă pe națiuni.

Vinzi și nu știi dacă ai de plătit?""",
 th="""Ai vândut o casă care nu era casa ta? 60 de zile ca să declari ȘI să plătești — de la încheierea vânzării, nu de la contract. E o declarație separată.

Cine NU declară: casa ta, locuită tot timpul cât a fost a ta. Și dacă nu iese taxă de plătit, nu se cere declarație — regula pentru rezidenții fiscali UK.""",
 li="""Sold a UK property that was not your home? You have 60 days.

Sixty days from completion, not from exchange of contracts. And inside them you do two things: report and pay.

It is not the Self Assessment return. It goes through a separate HMRC account for UK property disposals. If you file Self Assessment anyway, the disposal goes on that as well — in addition, not instead.

The rate is 18% or 24% of the gain, depending on which band the gain falls into. The first £3,000 of gains in the year is not taxed. Watch out for recycled copy: since 30 October 2024 there is no separate residential property rate, and the old 18%/28% split is gone.

Who does not report in 60 days:
• your own home, where Private Residence Relief applies in full. Every condition has to hold: one home, lived in as your main home for all the time you owned it, no part let out (a lodger does not count), no part used exclusively for business, grounds under 5,000 square metres, and not bought just to make a gain. If any one of them fails, there may be tax.
• where no tax is due — the gain sits inside the £3,000 annual exempt amount, or losses or a relief reduce it to nil. HMRC's manual is explicit that there is no need to report a disposal with no liability.
• a transfer to a spouse or civil partner you live with: no CGT, and outside the regime entirely as a no gain/no loss disposal.
• shares, commercial premises and land: these go on the Self Assessment return at the ordinary deadline, or through the real time service.

The reverse trap, and it catches people: a non-UK resident must report every disposal of UK property or land, residential or not, even with no tax to pay and even at a loss. The "no tax, no return" shortcut is exactly wrong there.

What lateness costs: £100 straight away, then at six months and twelve months the greater of 5% of the tax and £300. Interest runs on unpaid tax at base rate plus 4% — 7.75% to 23 November 2026, then 8%.

Worth knowing: the final nine months of ownership always qualify for relief, whatever the property was used for then, provided it was your only or main residence at some point.

UK-wide — Capital Gains Tax is not devolved. The purchase tax the buyer pays is a different tax and does differ by nation: SDLT in England and Northern Ireland, LBTT in Scotland, LTT in Wales.

The practical advice is to start before completion, not after. The HMRC property account has to exist and the figures have to be ready, and 60 days goes quickly.""",
 bsky="""Sold a UK property that was not your home? 60 days from completion to report AND pay, on a separate return. Your own home: usually neither.""",
 pin_title="UK property: 60 days to report and pay Capital Gains Tax",
 pin="""Sell a UK residential property that is not your home and you have 60 days from completion — not exchange — to report and pay any Capital Gains Tax. It is a separate return through an HMRC property account, not Self Assessment. The rate is 18% or 24% of the gain depending on your band, with the first £3,000 of gains in the year exempt. Who does not report in 60 days: your own home where Private Residence Relief applies in full, anyone with no tax to pay, a transfer to a spouse or civil partner, and shares or commercial property. UK-wide. Ola Accountancy, Luton and Birmingham.""",
 source="gov.uk/report-and-pay-your-capital-gains-tax",
)

C["cresa-30-ore"] = dict(
 ro="""30 de ore de creșă pe săptămână, plătite de stat. În Anglia, pentru părinți care lucrează, din trimestrul de după ce copilul face 9 luni și până la școală.

38 de săptămâni pe an, sau mai multe săptămâni cu mai puține ore.

Cât trebuie să câștigi: tu și partenerul tău, dacă ai unul, trebuie să vă așteptați fiecare, în următoarele 3 luni, la cel puțin £203,36 pe săptămână dacă aveți 21 de ani sau peste — adică £2.643,68 pe trimestru.

Important dacă ai firmă: dividendele, dobânzile, chiriile și pensia NU se numără la suma minimă. Un director cu salariu mic și dividende mari poate să nu se încadreze. HMRC verifică prin PAYE; dacă nu trimiți PAYE regulat, poate să îți ceară dovezi — fluturași, extrase sau o scrisoare de la contabil.

Nu vine singur: ceri un cod online, îl dai la creșă, și intri în cont din 3 în 3 luni ca să confirmi. Dacă nu te mai încadrezi, locul copilului continuă o perioadă limitată.

Termenul e pe trimestre: pentru orele din 1 ianuarie, ceri codul până pe 31 decembrie.

Cine NU primește:
• dacă tu sau partenerul tău vă așteptați la un venit net ajustat peste £100.000 în anul fiscal, nu primiți nici unul. Dacă nu ai partener, contează numai venitul tău.
• dacă partenerul tău nu lucrează, cu câteva excepții (concediu de îngrijitor, Carer's Allowance, elementele de îngrijitor sau de capacitate redusă de muncă din Universal Credit).
• oricine nu e în Anglia. Scoția, Țara Galilor și Irlanda de Nord au alte scheme.
Lista nu e completă — toate condițiile sunt pe gov.uk.

Orele gratuite nu acoperă toată factura. Creșa poate cere bani pe mâncare, scutece sau excursii — dar acele costuri trebuie să fie opționale, nu pot fi condiție pentru locul gratuit, și creșa trebuie să îți dea o alternativă.

Dacă nu te încadrezi, copilul de 3 sau 4 ani are oricum 15 ore pe săptămână, indiferent de venit.

Codul se cere pe gov.uk, nu de la contabil.""",
 th="""În Anglia: 30 de ore de creșă pe săptămână plătite de stat, 38 de săptămâni pe an, de la 9 luni. Ceri un cod online și confirmi din 3 în 3 luni.

Cine NU primește: dacă tu sau partenerul tău vă așteptați la un venit net ajustat peste £100.000, nu primiți nici unul. Și e numai în Anglia.""",
 li="""Thirty hours of government-funded childcare a week. England, working parents, from the term after the child turns 9 months until school.

Thirty hours a week, 38 weeks a year. What you have to earn: you and your partner, if you have one, must each expect to earn, over the three months after applying, at least £203.36 a week if you are 21 or over — £2,643.68 a quarter. That is the minimum wage for 16 hours a week.

The part that matters if you run a company: dividends, interest, property income and pension payments do not count towards the minimum. A director on a small salary and large dividends can fail the test, even when clearly working. HMRC checks through PAYE records, and where regular PAYE information is not submitted it can ask for evidence — wage slips, bank statements, invoices, or a statement from your accountant.

It does not arrive on its own. You apply online for an 11-digit code, give it to the provider, then sign in every three months to reconfirm. If you stop qualifying, statutory guidance gives the place a limited grace period.

The deadline is termly: 31 December for hours from 1 January, 31 March for 1 April, 31 August for 1 September. Apply later and you cannot take the entitlement up that term.

Who does not get it:
• a household where you or your partner expects adjusted net income over £100,000 this tax year. Neither of you gets it, however little the other earns. With no partner, only your income is tested.
• a household where your partner does not work, subject to listed exceptions — carer's leave, Carer's Allowance, the carer's or limited capability for work element of Universal Credit, contribution-based ESA, National Insurance credits.
• anyone who has not applied, or has stopped reconfirming.
• anyone outside England — and this is not the full list of conditions, which are all at gov.uk/free-childcare-if-working. Scotland funds 1,140 hours a year for 3 and 4 year olds and eligible 2 year olds with no earnings test; Wales offers up to 30 hours for 3 and 4 year olds only, tested on gross income; Northern Ireland funds pre-school in the year before primary school and a separate subsidy, but no 30-hours working-parent offer.

The hours are free but they are not the whole bill. A provider may charge for meals, nappies, trips and additional hours — but the statutory guidance is firm: those charges must be voluntary, must not be a condition of a free place, should be itemised, and the provider must offer a reasonable alternative.

A family that fails the working-parent test still keeps the universal 15 hours in England for a 3 or 4 year old, from the term after the third birthday.""",
 bsky="""England: 30 funded childcare hours a week from 9 months, for working parents. You or your partner over £100,000 and neither of you gets it.""",
 pin_title="30 funded childcare hours in England: who qualifies and who does not",
 pin="""In England, working parents can get 30 government-funded childcare hours a week, 38 weeks a year, from 9 months old until school. You and your partner must each expect to earn at least £203.36 a week if 21 or over, and dividends do not count towards it. It is never automatic: you apply online for a code and reconfirm every three months, by 31 December, 31 March or 31 August. Who does not get it: households where you or your partner expects over £100,000, households where your partner does not work, and everyone outside England. Ola Accountancy, Luton and Birmingham.""",
 source="gov.uk/free-childcare-if-working",
 wa_ro="Taxe și salarii: 0330 133 1886\nLuton · Birmingham",
 wa_th="Taxe și salarii: 0330 133 1886",
 wa_li="Tax and payroll: 0330 133 1886",
 disc_ro="Informații generale, nu consultanță pe ajutoare de stat. Condițiile sunt pe gov.uk.",
 disc_en="General information, not benefits advice. The conditions are on GOV.UK.",
)

C["help-to-save-50"] = dict(
 ro="""Pui £50 pe lună într-un cont, și statul adaugă £25. Contul se numește Help to Save.

Cum merge: pui între £1 și £50 pe lună, nu obligatoriu în fiecare lună, și statul adaugă 50%. În patru ani: maxim £2.400 puși de tine și până la £1.200 bonus.

Bonusul NU vine lunar. Vine de două ori:
• după 2 ani — 50% din cel mai mare sold pe care l-ai avut în primii doi ani
• după 4 ani — 50% din cât ai urcat peste acel sold în anii 3 și 4

Exemplul oficial de pe gov.uk: pui £25 pe lună doi ani, nu retragi nimic, soldul maxim e £600, primul bonus £300. În anii 3 și 4 mai strângi £200 peste acel maxim, deci al doilea bonus e £100.

Bonusul intră în contul tău bancar, nu în contul de economii. Și nu se impozitează.

Cine poate deschide: îți trebuie Universal Credit și cel puțin £1 câștigat — bani în mână, după taxe și National Insurance — de tine sau de partener, pe cerere comună. Pragul vechi de 16 ore pe săptămână a fost eliminat din 6 aprilie 2025: dacă ai fost refuzat înainte, s-ar putea să te încadrezi acum.

Cine NU poate deschide:
• cine nu are Universal Credit, sau îl are fără nicio sumă câștigată
• cine a avut deja un cont Help to Save. Un cont pe persoană, o singură dată în viață. Dacă îl închizi mai repede, pierzi bonusul următor și nu mai poți deschide altul.
Într-un cuplu, fiecare poate avea contul lui — se cere separat.

Capcana retragerilor. Bonusul deja câștigat nu se ia înapoi niciodată. Dar al doilea bonus se calculează din CREȘTEREA peste soldul maxim din primii doi ani. Deci dacă retragi, trebuie să pui înapoi tot ce ai scos ca să ajungi iar la vechiul maxim, și abia de acolo începi să câștigi bonus. Cu £50 pe lună, o retragere mare în anul 4 nu se mai recuperează matematic.

E la fel în toată Marea Britanie. Contul se deschide pe gov.uk/get-help-savings-low-income cu numărul de National Insurance și datele contului bancar.""",
 th="""Pui £50 pe lună, statul adaugă £25. Contul se numește Help to Save: până la £1.200 bonus în patru ani, neimpozabil.

Bonusul vine de două ori, la 2 și la 4 ani, nu lunar.

Cine NU poate deschide: cine nu are Universal Credit. Îți trebuie și minim £1 câștigat în ultima perioadă de calcul.""",
 li="""Pay in £50 a month and the government adds £25. The account is called Help to Save.

How it works: you pay in between £1 and £50 each calendar month, you are not obliged to pay in every month, and the government adds 50%. Over four years: £2,400 in at most, and up to £1,200 of bonus.

The bonus is not monthly. It comes twice:
• after 2 years — 50% of the highest balance you reached in years 1 and 2
• after 4 years — 50% of however much you push that highest balance up in years 3 and 4

GOV.UK's own example: pay in £25 a month for two years with no withdrawals, the highest balance is £600 and the first bonus is £300. In years 3 and 4 you grow that peak by £200, so the final bonus is £100.

The bonus is paid into your bank account rather than the savings account, and it is tax free.

Who can open one: you need Universal Credit and take-home pay of £1 or more — after tax and National Insurance — in your last monthly assessment period, from you or your partner on a joint claim. The old threshold of 16 hours a week at the National Living Wage was removed on 6 April 2025, so anyone turned away before that may qualify now. Working Tax Credit is no longer a route; tax credits ended in April 2025.

Who cannot:
• anyone not receiving Universal Credit, or receiving it with no earnings at all in the last assessment period
• anyone who has already had a Help to Save account. One per person, once ever. Close it early and you miss the next bonus with no second chance.
In a couple there is no problem: each person can hold their own, applied for separately.

The withdrawal trap, which is where the money is actually lost. A bonus already earned is never clawed back. But the final bonus is measured on the INCREASE over the highest balance reached in years 1 and 2. So if you withdraw, you have to put everything back just to return to the old high-water mark, and only above that does any further bonus start accruing. At £50 a month, a large withdrawal in year 4 is arithmetically impossible to recover.

If the Universal Credit award stops later, the account survives: GOV.UK says you can keep using it.

GOV.UK says Universal Credit and Housing Benefit are unaffected where you and your partner have £6,000 or less in personal savings in total — this account counts towards that alongside anything else you have saved.

UK-wide. The account opens on GOV.UK or in the HMRC app in a few minutes, with a National Insurance number and UK bank details.""",
 bsky="""Pay in £50 a month and the government adds 50% — up to £1,200 over four years, tax free, paid at years 2 and 4. You need Universal Credit.""",
 pin_title="Help to Save: a 50% government bonus on up to £50 a month",
 pin="""Help to Save is a UK government savings account that adds a 50% bonus to what you put away: £1 to £50 each calendar month, so £2,400 over four years at most, and up to £1,200 of tax-free bonus. The bonus is not monthly — one payment after two years worth 50% of your highest balance, and a final payment after four years worth 50% of however much you push that peak higher. To open one you need Universal Credit and take-home pay of £1 or more in your last assessment period. One account per person, once ever. UK-wide. Ola Accountancy, Luton and Birmingham.""",
 source="gov.uk/get-help-savings-low-income",
 wa_ro="Taxe și contabilitate: 0330 133 1886\nLuton · Birmingham",
 wa_th="Taxe și acte: 0330 133 1886",
 wa_li="Tax and accounts: 0330 133 1886",
 disc_ro="Informații generale, nu consultanță pe ajutoare de stat. Condițiile sunt pe gov.uk.",
 disc_en="General information, not benefits advice. The conditions are on GOV.UK.",
)


WA_TH = f"WhatsApp: {PHONE}"


def th_caption(slug):
    wa = C[slug].get("wa_th", WA_TH)
    return f"{C[slug]['th']}\n\n{wa}\n\n{C[slug].get('disc_ro', DISC_RO)}\n\n{BRAND_TAGS}"


def ro_caption(slug):
    t = topics.BY_SLUG[slug]
    disc = C[slug].get("disc_ro", DISC_RO)
    wa = C[slug].get("wa_ro", WA_RO)
    return (f"{C[slug]['ro']}\n\n{wa}\n\n{disc}\n\n"
            f"Sursă: {C[slug]['source']}\n\n{tags(t, 'ro')}")


def li_caption(slug):
    t = topics.BY_SLUG[slug]
    disc = C[slug].get("disc_en", DISC_EN)
    ph = C[slug].get("wa_li", PHONE)
    return (f"{C[slug]['li']}\n\n{ph}\n\nOla Accountancy — Luton and Birmingham\n\n"
            f"{disc}\n\nSource: {C[slug]['source']}\n\n{tags(t, 'en')}")


def bsky_caption(slug):
    # 300-character API cap. Brand tags are 85 of them, so no topical tags here.
    # The disclaimer is the brand-standard wording, not a shortened one: the cap is
    # answered by shorter copy, the way qa.py's overflow is answered by shorter copy.
    return f"{C[slug]['bsky']}\n\n{C[slug].get('disc_en', DISC_EN)}\n\n{BRAND_TAGS}"


def pin_caption(slug):
    t = topics.BY_SLUG[slug]
    return f"{C[slug]['pin']}\n\n{C[slug].get('disc_en', DISC_EN)}\n\n{tags(t, 'en')}"


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
        # 6 Nov 2026: four Pinterest descriptions (921, 929, 941 and 1046) were
        # rejected with "Code: 400 - Invalid request" and the first 75 characters
        # quoted back, which reads like a complaint about the words. It was the
        # count. limits.py held the 800 figure the whole time and this function
        # never asked it, so the check could not have failed — which is the one
        # thing a check has to be able to do.
        ro = ro_caption(slug)
        for net in ("instagram", "tiktok"):
            if len(ro) > 1 and len(ro) > {"instagram": 2200, "tiktok": 2200}[net]:
                bad.append(f"{net} {slug}: {len(ro)} chars (cap 2200)")
        if len(li_caption(slug)) > 3000:
            bad.append(f"linkedin {slug}: {len(li_caption(slug))} chars (cap 3000)")
        pin = pin_caption(slug)
        if len(pin) > 800:
            bad.append(f"pinterest {slug}: {len(pin)} chars (cap 800)")
        if len(C[slug]["pin_title"]) > 100:
            bad.append(f"pinterest title {slug}: {len(C[slug]['pin_title'])} chars (cap 100)")
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
