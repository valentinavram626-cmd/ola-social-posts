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
 bsky="""31 January 2027 is not just last year's tax — it also carries the first payment on account, half of last year's bill. The second follows 31 July.""",
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
    return f"{C[slug]['bsky']}\n\n{DISC_SHORT}\n\n{BRAND_TAGS}"


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
        if "gbp" in C[slug] and len(gbp_caption(slug)) > 1500:
            bad.append(f"gmb {slug}: {len(gbp_caption(slug))} chars (cap 1500)")
    return bad


if __name__ == "__main__":
    print(f"{'topic':22s} {'bsky':>5s} {'gmb':>5s}   ro / li / pin")
    for slug in C:
        g = len(gbp_caption(slug)) if "gbp" in C[slug] else 0
        print(f"  {slug:20s} {len(bsky_caption(slug)):5d} {g:5d}   "
              f"{len(ro_caption(slug))} / {len(li_caption(slug))} / {len(pin_caption(slug))}")
    bad = assert_lengths()
    print("\nLENGTH FAILURES:", len(bad))
    for x in bad: print("  -", x)
    raise SystemExit(1 if bad else 0)
