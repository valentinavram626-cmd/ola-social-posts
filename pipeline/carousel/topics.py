#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The five carousels for one publication day, and the primary source behind every figure.

One module, one day. Each topic carries:
  RO / EN   — the four content cards, rewritten per language, never translated
  CTA_RO/EN — the closing card
  GBP       — only on the single topic that goes to Google Business that day
  SOURCES   — the primary-source URL behind every figure on the cards
  SCOPE     — the four answers the README demands: nation, category, who is
              excluded, from when. A topic without all four does not ship.

Every figure here was read at primary source on 4 November 2026. Nothing on a
card comes from a news site, a blog or another firm's page.
"""

PHONE = "0330 133 1886"

BRAND_TAGS = ("#OlaAccountancy #ValentinTheAccountant "
              "#OlaAccountancyLuton #OlaAccountancyBirmingham")


def tags(topic, lang):
    return BRAND_TAGS + " " + (topic["tags_ro"] if lang == "ro" else topic["tags_en"])


# ===================================================================== 1
PAYMENTS_ON_ACCOUNT = dict(
  slug="plati-in-avans",
  title="Self Assessment — plățile în avans din 31 ianuarie",
  tags_ro="#selfassessment #hmrc #platiinavans #contabilitate #romaniinuk",
  tags_en="#selfassessment #hmrc #paymentsonaccount #ukaccountant #smallbusinessuk",

  RO=[
    dict(type="hook",
         kicker="Self Assessment · 31 ianuarie 2027",
         h1="Pe 31 ianuarie plătești de <em>două</em> ori.",
         say="Plătești taxele pe anul trecut. Și, în aceeași zi, încă o jumătate din ea în avans pentru anul care vine. Mulți află abia când văd suma."),
    dict(type="step", step="Cele două plăți", fig="50%",
         say="Prima jumătate pe 31 ianuarie, a doua pe 31 iulie. Fiecare e jumătate din taxele pe care le-ai avut de plătit anul trecut.",
         note="Dacă lucrezi pe cont propriu, în avans intră și Class 4 National Insurance."),
    dict(type="step", step="Cine NU plătește în avans", fig="<cur>£</cur>1.000",
         say="Dacă taxele de anul trecut au fost sub £1.000, nu plătești nimic în avans. Nici dacă peste <b>80%</b> din taxe ți s-au oprit deja din salariu sau din dobânzi.",
         note="Capital Gains Tax și rata la împrumutul studențesc nu intră niciodată în avans."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Self Assessment · 31 ianuarie 2027",
    h1="Nu ești sigur <em>cât ai de plătit</em>?",
    say="Scrie-ne un mesaj și ne uităm împreună la cifra din ianuarie. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Self Assessment · 31 January 2027",
         h1="On 31 January you pay <em>twice</em>.",
         say="You pay last year's tax. And on the same day, half of it again, in advance for the year ahead. Most people find out when they see the figure."),
    dict(type="step", step="The two payments", fig="50%",
         say="The first half on 31 January, the second on 31 July. Each one is half of the tax you owed last year.",
         note="If you work for yourself, Class 4 National Insurance goes into the advance payments too."),
    dict(type="step", step="Who does NOT pay in advance", fig="<cur>£</cur>1,000",
         say="If last year's tax was under £1,000, you pay nothing in advance. Nor do you if more than <b>80%</b> of your tax was already taken from your wages or your interest.",
         note="Capital Gains Tax and student loan repayments never go into the advance payments."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Self Assessment · 31 January 2027",
    h1="Not sure <em>what you owe</em>?",
    say="Send us a message and we will work through the January figure with you. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("Payments on account: both dates, the half-of-last-year rule, the under-£1,000 "
     "and 80%-at-source exclusions, Class 4 NIC inclusion, CGT and student loan in "
     "the balancing payment",
     "https://www.gov.uk/understand-self-assessment-bill/payments-on-account", "2026-11-04"),
    ("2025/26 online filing and payment deadline of 31 January 2027",
     "https://www.gov.uk/self-assessment-tax-returns/deadlines", "2026-11-04"),
  ],
  SCOPE=dict(
    nation="All of the UK — HMRC Self Assessment, no devolved variation.",
    category="Self Assessment taxpayers whose last-year tax bill was £1,000 or more "
             "and who had 80% or less deducted at source.",
    excluded="Anyone whose last-year tax owed was under £1,000, and anyone who paid "
             "more than 80% of last year's tax outside Self Assessment (PAYE code, "
             "bank-deducted interest). They make no payments on account at all. "
             "PAYE-only employees are not in Self Assessment and are outside this entirely.",
    from_when="31 January 2027 and 31 July 2027. Automatic — HMRC calculates it and "
              "shows it on the statement; nothing is claimed."),
)

# ===================================================================== 2
MTD_INCOME_TAX = dict(
  slug="mtd-income-tax",
  title="Making Tax Digital for Income Tax — pragurile și anii de referință",
  tags_ro="#makingtaxdigital #mtd #hmrc #contabilitate #romaniinuk",
  tags_en="#makingtaxdigital #mtd #hmrc #selfemployed #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Making Tax Digital · Income Tax",
         h1="Te prinde <em>Making Tax Digital</em>? Depinde de ce ai declarat acum doi ani.",
         say="Nu se uită la cât câștigi acum. Se uită la o declarație pe care ai depus-o deja."),
    dict(type="step", step="Pragurile, an cu an", fig="<cur>£</cur>50.000",
         say="Peste £50.000 în declarația 2024/25 → intri de la 6 aprilie 2026. Peste <b>£30.000</b> în 2025/26 → de la 6 aprilie 2027. Peste <b>£20.000</b> în 2026/27 → de la 6 aprilie 2028.",
         note="Se numără cât ai încasat din munca pe cont propriu și din chirii, înainte de cheltuieli."),
    dict(type="step", step="Cine NU intră", fig="PAYE",
         say="Dacă ai doar salariu, pensie, dobânzi sau dividende, nu intri — oricât ai câștiga. Se uită doar la munca pe cont propriu și la chirii.",
         note="Salariul și dividendele nu se adună la prag, nici măcar ca să te împingă peste el."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Making Tax Digital · Income Tax",
    h1="Nu știi <em>când intri</em>?",
    say="Trimite-ne cifra din ultima declarație și îți spunem din ce dată te privește. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Making Tax Digital · Income Tax",
         h1="Does <em>Making Tax Digital</em> catch you? It depends on a return you already filed.",
         say="It does not look at what you earn now. It looks at a tax return you have already sent in."),
    dict(type="step", step="The thresholds, year by year", fig="<cur>£</cur>50,000",
         say="Over £50,000 on the 2024/25 return → you are in from 6 April 2026. Over <b>£30,000</b> on 2025/26 → from 6 April 2027. Over <b>£20,000</b> on 2026/27 → from 6 April 2028.",
         note="It counts what you took in from self-employment and from rent, before expenses."),
    dict(type="step", step="Who is NOT in", fig="PAYE",
         say="If all you have is wages, a pension, interest or dividends, you are not in — however much you earn. It only looks at self-employment and rent.",
         note="Wages and dividends are not added to the threshold, not even to push you over it."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Making Tax Digital · Income Tax",
    h1="Not sure <em>when you start</em>?",
    say="Send us the figure from your last return and we will tell you which date applies. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("Exemptions exist and are not all automatic, which is why the card says "
     "\"unless an exemption applies\"",
     "https://www.gov.uk/guidance/find-out-if-you-can-get-an-exemption-from-making-tax-"
     "digital-for-income-tax", "2026-11-04"),
    ("Qualifying income excludes a partner's share of partnership profit, and excludes "
     "dividends including those from your own company",
     "https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-"
     "for-income-tax", "2026-11-04"),
    ("Who must use MTD for Income Tax; the £50,000 / £30,000 / £20,000 thresholds "
     "against the 2024-25 / 2025-26 / 2026-27 returns and the 6 April 2026 / 2027 / "
     "2028 start dates; qualifying income defined as total turnover from "
     "self-employment and property before expenses",
     "https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/introduction",
     "2026-11-04"),
  ],
  SCOPE=dict(
    nation="All of the UK — HMRC Income Tax, no devolved variation.",
    category="People already registered for Self Assessment who have filed a return "
             "and who have income from self-employment as a sole trader, from property "
             "as a landlord, or both, above the threshold for that stage.",
    excluded="Anyone with no sole-trade and no property income — an employee on PAYE "
             "only, or someone with only pension, savings or dividend income — is "
             "outside MTD for Income Tax however much they earn. So is anyone under "
             "the threshold for the stage, and anyone not registered for Self Assessment.",
    from_when="6 April 2026 (over £50,000), 6 April 2027 (over £30,000), 6 April 2028 "
              "(over £20,000). Mandatory by threshold, not claimed."),
)

# ===================================================================== 3
VAT_THRESHOLD = dict(
  slug="tva-prag-90000",
  title="TVA — pragul de £90.000 și cele două teste",
  tags_ro="#tva #vat #hmrc #afacerimici #romaniinuk",
  tags_en="#vat #vatregistration #hmrc #smallbusinessuk #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="TVA · £90.000",
         h1="Ai vândut de peste <em>£90.000</em>? Trebuie să te înregistrezi la TVA.",
         say="Se numără cât ai vândut, nu cât ți-a rămas. Și se numără ultimele 12 luni — nu anul trecut, nu anul fiscal."),
    dict(type="step", step="Când treci pragul", fig="30 de zile",
         say="La sfârșitul fiecărei luni, aduni vânzările din ultimele 12 luni. Dacă totalul trece de <b>£90.000</b>, ai 30 de zile să anunți HMRC.",
         note="Treci pragul în iulie → te înregistrezi până pe 30 august → pui TVA pe facturi de la 1 septembrie."),
    dict(type="step", step="Cine nu trebuie", fig="<cur>£</cur>88.000",
         say="Sub £90.000 nu ești obligat. Poți să te înregistrezi dacă vrei, dar nu trebuie. Iar dacă ești deja înregistrat și vânzările scad sub £88.000, poți cere să ieși.",
         note="Excepția: dacă firma ta e înregistrată în afara UK și vinzi aici, te înregistrezi de la prima liră."),
  ],
  CTA_RO=dict(type="cta",
    kicker="TVA · £90.000",
    h1="Nu știi dacă ai trecut <em>pragul</em>?",
    say="Scrie-ne și numărăm împreună ultimele 12 luni. Îți spunem clar dacă trebuie să te înregistrezi sau nu. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="VAT · £90,000",
         h1="Sold more than <em>£90,000</em>? You have to register for VAT.",
         say="It counts what you sold, not what you kept. And it counts the last 12 months — not last year, not the tax year."),
    dict(type="step", step="When you go over", fig="30 days",
         say="At the end of every month, add up your sales for the last 12 months. If the total passes <b>£90,000</b>, you have 30 days to tell HMRC.",
         note="Go over in July → register by 30 August → charge VAT from 1 September."),
    dict(type="step", step="Who does not have to", fig="<cur>£</cur>88,000",
         say="Under £90,000 you are not obliged. You may register by choice, but you do not have to. And if you are registered and sales drop below £88,000, you can ask to come out.",
         note="The exception: if your business is based outside the UK and you sell here, you register from the first pound."),
  ],
  CTA_EN=dict(type="cta",
    kicker="VAT · £90,000",
    h1="Not sure if you have gone <em>over</em>?",
    say="Message us and we will add up the last 12 months with you. We will tell you plainly whether you need to register. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("The £90,000 registration threshold and the £88,000 deregistration threshold",
     "https://www.gov.uk/how-vat-works/vat-thresholds", "2026-11-04"),
    ("The rolling 12-month backward look with its 30-day deadline and first-day-of-the-"
     "second-month effective date; the 30-day forward look with its end-of-period "
     "deadline and date-you-realised effective date; and that a business established "
     "outside the UK must register regardless of turnover",
     "https://www.gov.uk/register-for-vat", "2026-11-04"),
    ("Deregistration is a forward-looking test: HMRC must be satisfied that "
     "\"your taxable turnover in the next 12 months will not exceed the VAT "
     "registration cancellation limit\" (section 3.2)",
     "https://www.gov.uk/government/publications/vat-notice-70011-cancelling-your-"
     "registration/vat-notice-70011-cancelling-your-registration", "2026-11-04"),
    ("A business established outside the UK making taxable supplies here must register "
     "regardless of turnover: the threshold \"does not apply to you\" (paragraph 3.1)",
     "https://www.gov.uk/government/publications/vat-notice-7001-should-i-be-registered-"
     "for-vat/vat-notice-7001-should-i-be-registered-for-vat", "2026-11-04"),
  ],
  SCOPE=dict(
    nation="All of the UK — VAT is a UK-wide tax, no devolved variation.",
    category="Any business whose taxable turnover is at or near the threshold, "
             "whether sole trader, partnership or limited company.",
    excluded="A business whose rolling 12-month taxable turnover stays at or below "
             "£90,000 and which does not expect to pass it in the next 30 days has no "
             "obligation to register — voluntary registration stays available but is a "
             "choice, not a duty. The figures are turnover, not profit, so a business "
             "well under on profit can still be over on turnover.",
    from_when="Current thresholds, in force now. Registration is the business's own "
              "duty on a deadline; HMRC does not prompt it."),
)

# ===================================================================== 4
MARRIAGE_ALLOWANCE = dict(
  slug="marriage-allowance",
  title="Marriage Allowance — £252 pe an și patru ani retroactiv",
  tags_ro="#marriageallowance #hmrc #taxeuk #beneficiiuk #romaniinuk",
  tags_en="#marriageallowance #hmrc #taxrelief #personalfinanceuk #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Marriage Allowance",
         h1="Căsătoriți? Plătiți cu <em>£252</em> mai puțin impozit.",
         say="Fiecare poate câștiga £12.570 pe an fără să plătească impozit. Dacă unul dintre voi nu ajunge la suma asta, poate da o parte celuilalt."),
    dict(type="step", step="Cum funcționează", fig="<cur>£</cur>1.260",
         say="Cel care câștigă mai puțin îi trece celuilalt £1.260 din suma pe care o are scutită de impozit. Rezultatul: până la <b>£252</b> mai puțin impozit pe an.",
         note="Trebuie cerut — nu vine singur. Și poți cere și pentru anii trecuți, până la 6 aprilie 2022."),
    dict(type="step", step="Cine NU poate cere", fig="<cur>£</cur>50.270",
         say="Dacă locuiți împreună dar nu sunteți căsătoriți sau într-un parteneriat civil, nu puteți cere. E cea mai frecventă confuzie. Nici dacă cel care câștigă mai mult trece de £50.270.",
         note="În Scoția limita e £43.662. Și nu poți avea în același timp Married Couple's Allowance."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Marriage Allowance",
    h1="Credeți că vi se <em>aplică</em>?",
    say="Scrie-ne și verificăm dacă vă încadrați și pentru câți ani în urmă puteți cere. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Marriage Allowance",
         h1="Married and one of you earns little? Pay <em>£252</em> less tax.",
         say="Everyone can earn £12,570 a year before paying tax. If one of you does not reach that, they can pass part of it to the other."),
    dict(type="step", step="How it works", fig="<cur>£</cur>1,260",
         say="The lower earner moves £1,260 of their tax-free amount across. The result is up to <b>£252</b> less tax a year for the other.",
         note="You have to ask for it — it never arrives on its own. And you can claim for past years, back to 6 April 2022."),
    dict(type="step", step="Who CANNOT claim", fig="<cur>£</cur>50,270",
         say="If you live together but are not married and not in a civil partnership, you cannot claim. That is the one people get wrong. Nor can you if the higher earner is over £50,270.",
         note="In Scotland the limit is £43,662. And you cannot hold this and Married Couple's Allowance at the same time."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Marriage Allowance",
    h1="Think it <em>applies</em> to you?",
    say="Message us and we will check whether you qualify and how many past years are still open. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  GBP=[
    dict(type="solo",
         kicker="Marriage Allowance · gov.uk",
         h1="Up to £252 a year, and you can still backdate it.",
         rows=[["<cur>£</cur>252",   "maximum, a year off the higher earner's tax"],
               ["<cur>£</cur>1,260", "of Personal Allowance transferred"],
               ["4 years",           "backdating, to 6 April 2022"]],
         ask="Married or in a civil partnership, one of you under £12,570? Luton and Birmingham — message us.",
         phone=PHONE, disc="General information, not personal advice."),
  ],

  SOURCES=[
    ("The £252 a year value, the £1,260 Personal Allowance transfer, the £12,570 "
     "lower-earner condition, the basic-rate condition and the Scottish starter / "
     "basic / intermediate wording, backdating to 6 April 2022 (2022-23), and the "
     "rule that unmarried cohabiting couples cannot claim",
     "https://www.gov.uk/marriage-allowance", "2026-11-04"),
  ],
  SCOPE=dict(
    nation="All of the UK. The only national variation is which Scottish rate band "
           "the receiving partner must sit in (starter, basic or intermediate, "
           "£12,571–£43,662) instead of the rest-of-UK basic rate (£12,571–£50,270).",
    category="Married couples and civil partners where one partner's income is below "
             "the Personal Allowance (usually £12,570) and the other pays the basic "
             "rate (or the Scottish starter, basic or intermediate rate).",
    excluded="Couples living together who are not married and not in a civil "
             "partnership cannot claim at all — this is the single biggest exclusion "
             "and the one people get wrong. Also excluded: couples where both are "
             "above the Personal Allowance, couples where the higher earner is a "
             "higher-rate payer, and anyone already receiving Married Couple's "
             "Allowance, which cannot be held at the same time.",
    from_when="Available now. Must be CLAIMED — it is never automatic — and a claim "
              "can be backdated to 6 April 2022 while the 2022/23 year remains in date."),
)

# ===================================================================== 5
WINTER_FUEL = dict(
  slug="winter-fuel-35000",
  title="Winter Fuel Payment — £200-£300 și pragul de £35.000",
  tags_ro="#winterfuelpayment #pensii #hmrc #beneficiiuk #romaniinuk",
  tags_en="#winterfuelpayment #statepension #hmrc #pensionersuk #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Winter Fuel Payment · iarna 2026/27",
         h1="<em>£200-£300</em> pentru încălzire. Dar unii trebuie să-i dea înapoi.",
         say="Banii vin singuri, cu o scrisoare în octombrie sau noiembrie. Partea despre care se vorbește puțin e ce se întâmplă după."),
    dict(type="step", step="Cine primește", fig="<cur>£</cur>200",
         say="Dacă te-ai născut pe 27 iunie 1960 sau înainte. <b>£300</b> dacă te-ai născut înainte de 28 septembrie 1946.",
         note="Anglia, Țara Galilor și Irlanda de Nord. Scoția are plata ei, Pension Age Winter Heating Payment."),
    dict(type="step", step="Cine NU rămâne cu banii", fig="<cur>£</cur>35.000",
         say="Dacă venitul tău trece de £35.000, HMRC îți ia plata înapoi — din codul fiscal sau prin Self Assessment. Se uită la venitul tău, nu al gospodăriei.",
         note="Dacă nu a venit până în ianuarie, poate fi cerută până la 31 martie 2027."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Winter Fuel Payment · iarna 2026/27",
    h1="O vei <em>da înapoi</em>?",
    say="Scrie-ne un mesaj și ne uităm la venitul tău pe anul fiscal. Fără obligații.",
    phone=PHONE),

  EN=[
    dict(type="hook",
         kicker="Winter Fuel Payment · winter 2026/27",
         h1="<em>£200-£300</em> towards heating. Some have to give it back.",
         say="The money arrives on its own, with a letter in October or November. What is talked about less is what happens afterwards."),
    dict(type="step", step="Who gets it", fig="<cur>£</cur>200",
         say="If you were born on 27 June 1960 or earlier. <b>£300</b> if you were born before 28 September 1946.",
         note="England, Wales and Northern Ireland. Scotland has its own, the Pension Age Winter Heating Payment."),
    dict(type="step", step="Who does NOT keep it", fig="<cur>£</cur>35,000",
         say="If your own income goes over £35,000, HMRC takes the payment back — through your tax code or through Self Assessment. It looks at your income, not the household's.",
         note="If it has not arrived by January, it can be claimed up to 31 March 2027."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Winter Fuel Payment · winter 2026/27",
    h1="Will you <em>pay it back</em>?",
    say="Send us a message and we will look at your income for the tax year. No obligation.",
    phone=PHONE),

  SOURCES=[
    ("Born on or before 27 June 1960; usually live in England, Wales or Northern "
     "Ireland; qualifying week 21-27 September 2026; the exclusion list",
     "https://www.gov.uk/winter-fuel-payment/eligibility", "2026-11-04"),
    ("£200 and £300 for someone living alone, split at the 28 September 1946 birth "
     "date; letter in October or November",
     "https://www.gov.uk/winter-fuel-payment/how-much-youll-get", "2026-11-04"),
    ("The £35,000 threshold, assessed on each person's own income, and recovery "
     "through the PAYE tax code or Self Assessment",
     "https://www.gov.uk/guidance/paying-back-the-winter-fuel-payment", "2026-11-04"),
    ("Automatic for most; must be claimed if you have never had it or have deferred "
     "your State Pension; claim deadline 31 March 2027 for winter 2026 to 2027",
     "https://www.gov.uk/winter-fuel-payment/how-to-claim", "2026-11-04"),
    ("Scotland's replacement benefit, Pension Age Winter Heating Payment, and its own "
     "£35,000 recovery rule",
     "https://www.mygov.scot/pension-age-winter-heating-payment", "2026-11-04"),
  ],
  SCOPE=dict(
    nation="England, Wales and Northern Ireland ONLY. Scotland is NOT covered: people "
           "in Scotland get Pension Age Winter Heating Payment from Social Security "
           "Scotland instead. The card says this explicitly.",
    category="People born on or before 27 June 1960 who usually live in England, Wales "
             "or Northern Ireland. £200 or £300 living alone, split at the 28 September "
             "1946 birth date; lower amounts where an eligible partner or a care home "
             "is involved.",
    excluded="Anyone whose own income passes £35,000 keeps nothing — HMRC recovers the "
             "whole payment through the tax code or Self Assessment. Also excluded: "
             "people who usually live outside England, Wales and Northern Ireland "
             "(Scotland included, who get the Scottish payment instead); people in "
             "prison for the whole qualifying week; people in hospital on free "
             "treatment for the whole qualifying week and the year before; and some "
             "care-home residents on Pension Credit, Universal Credit or "
             "income-related ESA. Income is judged per person, so a couple on £30,000 "
             "each keep both payments while one person on £36,000 keeps none.",
    from_when="Winter 2026/27, based on the qualifying week of 21-27 September 2026. "
              "Automatic for most, with a letter in October or November. Those who have "
              "never had it, or who deferred their State Pension, must claim by "
              "31 March 2027."),
)

# ===================================================================== 6
CIS_20_30 = dict(
  slug="cis-20-30",
  title="CIS — de ce ți se opresc 20% sau 30% din plată",
  tags_ro="#cis #construcții #hmrc #subcontractor #romaniinuk",
  tags_en="#cis #construction #hmrc #subcontractor #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="CIS · construcții",
         h1="Ți se opresc <em>30%</em> din plată? De obicei, nu ești înregistrat.",
         say="În construcții, firma care te plătește oprește o parte din bani și o trimite la HMRC în numele tău. 30% înseamnă de obicei că nu ești înregistrat la CIS — sau că firma nu te-a putut verifica la HMRC."),
    dict(type="step", step="20% sau 30%", fig="20%",
         say="<b>20%</b> doar dacă ești înregistrat la CIS <b>și</b> firma te găsește la HMRC. Înregistrat, dar nu te găsește? Tot <b>30%</b>. Banii nu se pierd: sunt avans la taxele și National Insurance pe care le datorezi.",
         note="Pe cont propriu, se scad la declarația anuală. Cu firmă (Ltd), prin payroll — nu plătești taxele cu ele în declarația de Corporation Tax."),
    dict(type="step", step="Cine NU are opriri", fig="0%",
         say="Angajații nu intră deloc în CIS: cu contract de muncă, nu ți se oprește nimic pe CIS. Iar dacă obții „gross payment status” la HMRC, nu se oprește nimic nici ca subcontractor — primești tot și plătești taxele la final.",
         note="Nu se oprește nimic nici din TVA, nici din materialele plătite de tine."),
  ],
  CTA_RO=dict(type="cta",
    kicker="CIS · construcții",
    h1="Nu știi dacă ești <em>înregistrat</em>?",
    say="Scrie-ne și ne uităm împreună la ce ți s-a oprit și cum se scade din taxe. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="CIS · construction",
         h1="Having <em>30%</em> deducted? Usually you are not registered.",
         say="In construction, the firm paying you keeps part of the money and sends it to HMRC in your name. 30% usually means you never registered, or could not be verified."),
    dict(type="step", step="20% or 30%", fig="20%",
         say="<b>20%</b> only if you are registered for CIS <b>and</b> the contractor can find you at HMRC. Registered but not found? Still <b>30%</b>. The money is not lost: it is an advance on the tax you owe.",
         note="Sole trader: offset on your tax return. Limited company: through payroll — not by paying tax with them on the Corporation Tax return."),
    dict(type="step", step="Who has NO deduction", fig="0%",
         say="Employees are not in CIS at all: with a contract of employment, nothing is deducted under CIS. And a subcontractor granted gross payment status by HMRC has nothing deducted either — paid in full, tax settled at the end.",
         note="Nothing is deducted from VAT or from materials you paid for, either."),
  ],
  CTA_EN=dict(type="cta",
    kicker="CIS · construction",
    h1="Not sure whether you are <em>registered</em>?",
    say="Message us and we will check what has been deducted and how it comes off your tax. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  GBP=[
    dict(type="solo",
         kicker="CIS · gov.uk",
         h1="20% if you are registered. 30% if you are not.",
         rows=[["20%", "deducted from a registered subcontractor"],
               ["30%", "deducted if you are not registered"],
               ["0%",  "with gross payment status"]],
         ask="Working in construction around Luton or Birmingham? Message us and we will check your CIS deductions.",
         phone=PHONE, disc="General information, not personal advice."),
  ],

  SOURCES=[
    ("The 20% registered / 30% unregistered / 0% gross payment deduction rates, and the "
     "items taken off the invoice before the rate is applied: VAT, materials the "
     "subcontractor paid for, consumable stores, fuel other than travel fuel, plant hire "
     "and manufacturing or prefabricating costs; statement due within 14 days of the tax "
     "month end",
     "https://www.gov.uk/what-you-must-do-as-a-cis-contractor/make-deductions-and-pay-subcontractors", "2026-11-05"),
    ("A registered subcontractor has 20% deducted and an unregistered one 30%; an employee "
     "does not need to register",
     "https://www.gov.uk/what-you-must-do-as-a-cis-subcontractor", "2026-11-05"),
    ("Deductions are made only from the part of a payment that does not represent the cost "
     "of materials; contracts of employment are excluded from the scheme; running a canteen "
     "or hostel, medical, safety and security services and site facilities are not "
     "construction operations",
     "https://www.gov.uk/government/publications/construction-industry-scheme-cis-340/"
     "construction-industry-scheme-a-guide-for-contractors-and-subcontractors-cis-340", "2026-11-05"),
    ("20% for a matched subcontractor and 30% for an unmatched one, in force from "
     "6 April 2007",
     "https://www.gov.uk/hmrc-internal-manuals/construction-industry-scheme-reform/cisr71020", "2026-11-05"),
    ("The 20% standard rate applies only where BOTH apply — 'you\'re registered for CIS' "
     "and 'they can verify you' — and 'If either do not apply, contractors will take "
     "deductions at a higher rate of 30%', so a registered subcontractor who cannot be "
     "verified is still deducted at 30%",
     "https://www.gov.uk/what-you-must-do-as-a-cis-subcontractor/get-paid", "2026-11-06"),
    ("A limited company recovers deductions through its payroll scheme, and HMRC's only "
     "prohibition is 'Do not use your Corporation Tax return to pay tax with your "
     "deductions - you may get a penalty if you do'; leftover deductions carry forward "
     "within the tax year and a refund is claimed after it ends. This is why the cards no "
     "longer say CIS deductions are NEVER recovered through Corporation Tax",
     "https://www.gov.uk/what-you-must-do-as-a-cis-subcontractor/pay-tax-and-claim-back-deductions", "2026-11-06"),
    ("CIS340: 'At the end of the tax year, once we\'ve received the company\'s final Full "
     "Payment Submission (FPS) and final EPS, any excess CIS deductions that cannot be set "
     "off may be refunded or set against Corporation Tax due. No repayments or set-offs "
     "against other liabilities can be made in-year except where the company is in "
     "liquidation or administration.'",
     "https://www.gov.uk/government/publications/construction-industry-scheme-cis-340/"
     "construction-industry-scheme-a-guide-for-contractors-and-subcontractors-cis-340", "2026-11-06"),
  ],
  SCOPE=dict(
    nation="All of the UK — CIS is a UK-wide HMRC scheme, covering construction operations "
           "in the UK and within UK territorial waters. No devolved variation.",
    category="Subcontractors paid for construction work by a contractor — sole traders, "
             "partners, limited companies — and the contractors who pay them.",
    excluded="Employees are outside CIS entirely: a contract of employment is excluded from "
             "the scheme, so nothing is deducted under CIS from a wage. Subcontractors with "
             "gross payment status have 0% deducted. Within a payment, no deduction is taken "
             "from VAT, from materials the subcontractor paid for, from consumable stores, "
             "from fuel other than travel fuel, from plant hire paid to a third party, or "
             "from manufacturing and prefabrication costs. Running site facilities — canteens, "
             "hostels, offices, toilets, medical centres — and the supply of security guards "
             "are not construction operations; CONSTRUCTING those facilities is, as is most "
             "physical security work (erecting CCTV posts, fitting security shutters, site "
             "hoardings), so 'site security' must never be described as outside CIS.",
    from_when="Current rates, in force since 6 April 2007. Registration is the "
              "subcontractor's own step and is not automatic; without it the 30% rate "
              "applies to every payment."),
)

# ===================================================================== 7
TAX_CODE_30_DEC = dict(
  slug="taxa-prin-codul-fiscal",
  title="Self Assessment — plata prin codul fiscal, termen 30 decembrie 2026",
  tags_ro="#selfassessment #hmrc #codfiscal #paye #romaniinuk",
  tags_en="#selfassessment #hmrc #paye #taxcode #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Self Assessment · 30 decembrie 2026",
         h1="Ai taxă de plătit și salariu? HMRC o ia <em>din salariu</em>, singură.",
         say="Dacă datorezi sub £3.000 și ai deja salariu sau pensie, HMRC nu îți cere toată suma pe 31 ianuarie: o ia din salariu, puțin câte puțin, pe parcursul anului. Automat — nu ceri nimic."),
    dict(type="step", step="Cele trei condiții", fig="<cur>£</cur>3.000",
         say="Datorezi sub <b>£3.000</b>. Ai deja salariu sau pensie din care se oprește impozit. Și depui declarația online până pe <b>30 decembrie 2026</b>.",
         note="Pe hârtie termenul era 31 octombrie și a trecut. Online, mai sunt câteva săptămâni."),
    dict(type="step", step="Cine NU poate", fig="50%",
         say="Dacă datorezi £3.000 sau mai mult, nu poți — și nu poți plăti o parte ca să cobori sub prag. Nici dacă nu ai destul salariu din care HMRC să ia banii, sau dacă ai ajunge să plătești peste <b>50%</b> din salariu în impozit.",
         note="Se întâmplă automat dacă te încadrezi. Dacă NU vrei să ți se ia din salariu, bifezi pe declarație să nu se întâmple."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Self Assessment · 30 decembrie 2026",
    h1="Vrei să <em>împarți</em> suma?",
    say="Scrie-ne și ne uităm dacă te încadrezi și ce trebuie depus până pe 30 decembrie. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Self Assessment · 30 December 2026",
         h1="Owe tax and have a wage? HMRC takes it <em>out of your pay</em>.",
         say="Owe under £3,000 and already pay tax through PAYE, and HMRC does not ask for the whole sum on 31 January: it takes it from your wages a bit at a time across the year. Automatically. Nothing to apply for."),
    dict(type="step", step="The three conditions", fig="<cur>£</cur>3,000",
         say="You owe less than <b>£3,000</b>. You already pay tax through PAYE on a wage or a pension. And you file online by <b>30 December 2026</b>.",
         note="The paper deadline was 31 October and has gone. Online, there are still a few weeks."),
    dict(type="step", step="Who CANNOT", fig="50%",
         say="Owe £3,000 or more and you cannot — and you cannot part-pay to get under it. Nor if there is too little PAYE income to collect from, or if over <b>50%</b> of your pay would go in tax.",
         note="It happens automatically if you qualify. If you do NOT want it taken from your wages, tick the box on your return to stop it."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Self Assessment · 30 December 2026",
    h1="Want the bill <em>spread out</em>?",
    say="Message us and we will check whether you qualify and what has to be filed by 30 December. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("The three conditions — owe less than £3,000, already pay tax through PAYE, paper "
     "return by 31 October or online by 30 December — and who cannot use it: not enough "
     "PAYE income to collect from, more than 50% of PAYE income taken in tax, more than "
     "twice the usual amount of tax, anyone who part-paid to get under £3,000, and Class 2 "
     "National Insurance due since 6 April 2015",
     "https://www.gov.uk/pay-self-assessment-tax-bill/through-your-tax-code", "2026-11-05"),
    ("The 2025/26 dates: paper return 31 October 2026, tax-code option 30 December 2026, "
     "online filing and payment 31 January 2027",
     "https://www.gov.uk/self-assessment-tax-returns/deadlines", "2026-11-05"),
  ],
  SCOPE=dict(
    nation="All of the UK — HMRC Self Assessment and PAYE. No devolved variation.",
    category="Self Assessment taxpayers for 2025/26 who owe under £3,000 and already have "
             "tax deducted through PAYE from employment or from a company or personal pension.",
    excluded="Anyone who owes £3,000 or more cannot use it, and cannot part-pay to get below "
             "that figure. Anyone without enough PAYE income for HMRC to collect the tax "
             "from. Anyone for whom it would mean more than 50% of their PAYE income going "
             "in tax, or more than twice their usual tax. Self-employed people cannot pay "
             "Class 2 National Insurance this way unless it has been due since before "
             "6 April 2015. And anyone who files after 30 December 2026 loses the option for "
             "this year even if they would otherwise qualify.",
    from_when="For the 2025/26 return. The online deadline for this option is 30 December "
              "2026; the 31 October 2026 paper deadline has passed. AUTOMATIC, not claimed: "
              "HMRC 'will automatically collect what you owe through your tax code if you "
              "meet all 3 conditions', 'unless you've specifically asked them not to (on your "
              "tax return)'. So the person who must act is the one who does NOT want it."),
)

# ===================================================================== 8
TRADING_ALLOWANCE = dict(
  slug="scutire-1000-lire",
  title="Trading allowance — primele £1.000 pe an nu se declară",
  tags_ro="#tradingallowance #hmrc #selfassessment #venitsuplimentar #romaniinuk",
  tags_en="#tradingallowance #hmrc #sidehustle #selfassessment #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Trading allowance · £1.000",
         h1="Câștigi ceva pe lângă? Primii <em>£1.000</em> pe an sunt scutiți.",
         say="Dacă repari, livrezi, faci curățenie, dai cu împrumut uneltele tale sau cumperi ca să revinzi — pe lângă jobul tău — primii £1.000 pe an sunt scutiți de impozit și nu se anunță la HMRC, dacă nu ai alt motiv să depui declarație."),
    dict(type="step", step="Ce se numără", fig="<cur>£</cur>1.000",
         say="Se numără cât ai încasat, nu cât ți-a rămas. Dacă totalul pe anul fiscal trece de <b>£1.000</b>, te înregistrezi la Self Assessment până pe 5 octombrie din anul următor.",
         note="Salariul nu se adună aici. £1.000 e cifra pentru 2026/27 — din 6 aprilie 2027 crește la £3.000."),
    dict(type="step", step="Cine NU poate folosi scutirea", fig="0",
         say="Nu poți folosi scutirea pentru bani de la angajatorul tău, de la angajatorul soțului, soției sau al partenerului civil, ori de la o firmă pe care o controlezi.",
         note="Nici pentru profitul tău dintr-o firmă în parteneriat. Sub £1.000 declarația se poate depune voluntar — contează pentru Maternity Allowance și pentru pensie."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Trading allowance · £1.000",
    h1="Ai trecut de <em>£1.000</em>?",
    say="Scrie-ne și adunăm împreună ce ai încasat pe anul fiscal. Îți spunem clar dacă trebuie să declari. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Trading allowance · £1,000",
         h1="Earning a bit on the side? The first <em>£1,000</em> a year is tax free.",
         say="If you do repairs, deliveries, cleaning, hire out your own tools or buy things to resell — alongside a job — the first £1,000 a year is tax free and you do not have to tell HMRC, unless you have another reason to file."),
    dict(type="step", step="What counts", fig="<cur>£</cur>1,000",
         say="It counts what came in, not what you kept. If the tax-year total passes <b>£1,000</b>, you must register for Self Assessment by 5 October in the following tax year.",
         note="Wages do not count towards it. £1,000 is the 2026/27 figure — it rises to £3,000 from 6 April 2027."),
    dict(type="step", step="Who CANNOT use it", fig="0",
         say="You cannot use it on money from your own employer, from your spouse's or civil partner's employer, or from a company you or a connected person controls.",
         note="Nor on a partnership's profit. Below £1,000 a return can still be filed voluntarily — for Maternity Allowance or voluntary pension contributions."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Trading allowance · £1,000",
    h1="Gone past <em>£1,000</em>?",
    say="Message us and we will add up what came in across the tax year and tell you plainly whether you have to declare it. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("The £1,000 trading allowance; no need to tell HMRC where gross trading income is "
     "£1,000 or less; registration for Self Assessment required above £1,000, by 5 October "
     "in the following tax year; the exclusions for income from your own employer, your "
     "spouse's or civil partner's employer, or a company or partnership you or a connected "
     "person owns, controls or is a partner in, and that the allowance does not apply to "
     "partnership trading income; and the reasons to file anyway — loss relief, voluntary "
     "Class 2 National Insurance, Tax-Free Childcare, Maternity Allowance",
     "https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income", "2026-11-05"),
  ],
  SCOPE=dict(
    nation="All of the UK — a UK-wide Income Tax exemption, no devolved variation.",
    category="Individuals with gross trading or miscellaneous income of up to £1,000 in a "
             "tax year: selling, casual services, hiring out personal equipment, alongside "
             "or instead of other income.",
    excluded="The allowance cannot be used at all on trade or property income from your own "
             "employer, from your spouse's or civil partner's employer, or from a company or "
             "partnership that you or a connected person owns, controls or is a partner in; "
             "and it does not apply to trading income from a partnership. Separately, anyone "
             "whose gross trading income passes £1,000 is not exempt and must register for "
             "Self Assessment. And some people below £1,000 still need to file — to claim "
             "loss relief, to pay voluntary Class 2 National Insurance, or to base Tax-Free "
             "Childcare or Maternity Allowance on self-employment income.",
    from_when="£1,000 for 2026/27, in force now. RISES TO £3,000 FROM 6 APRIL 2027 "
              "(announced at the Budget on 28 October 2026), alongside the Self Assessment "
              "reporting threshold, so every asset carrying £1,000 must be reissued in "
              "April 2027. Automatic — nothing is claimed and, at or below the figure, "
              "nothing is reported. Above it, registration is the taxpayer's own duty, by "
              "5 October after the end of the tax year."),
)

# ===================================================================== 9
MIN_WAGE = dict(
  slug="salariu-minim-2027",
  title="Salariul minim — £12,71 acum, £13,21 din aprilie 2027",
  tags_ro="#salariulminim #drepturiangajati #payroll #muncainuk #romaniinuk",
  tags_en="#minimumwage #nationallivingwage #payroll #employeerights #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Salariul minim · acum și din aprilie 2027",
         h1="Salariul minim e <em>£12,71</em> pe oră. Din aprilie 2027, £13,21.",
         say="Dacă ai 21 de ani sau mai mult, salariul minim național e £12,71 pe oră. Cifra pentru anul viitor e deja decisă."),
    dict(type="step", step="Pe vârste", fig="<cur>£</cur>10,85",
         say="La 18-20 de ani, minimul e £10,85 pe oră. Sub 18 ani și pentru ucenici, £8,00. Din aprilie 2027: <b>£11,27</b> și <b>£8,31</b>.",
         note="Ucenicii de 19 ani sau peste care au terminat primul an primesc tariful vârstei lor. În agricultură, Scoția, Țara Galilor și Irlanda de Nord au tarife proprii, care pot fi mai mari."),
    dict(type="step", step="Cine NU are salariu minim", fig="0",
         say="Dacă lucrezi pe cont propriu, cu afacerea ta, salariul minim nu ți se aplică: tu îți stabilești prețul. Nici voluntarii nu intră.",
         note="Directorii de firmă nu intră — decât dacă au și contract de muncă cu firma, și atunci da. Nici rudele angajatorului care locuiesc în casa lui."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Salariul minim · acum și din aprilie 2027",
    h1="Ești plătit <em>corect</em> pe oră?",
    say="Scrie-ne cu fluturașul în față și verificăm tariful pe ore. Dacă ai angajați, ne uităm la statul de plată. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Minimum wage · now and from April 2027",
         h1="The minimum wage is <em>£12.71</em> an hour. From April 2027, £13.21.",
         say="If you are 21 or over, the National Minimum Wage is £12.71 an hour. Next year's figure is already set."),
    dict(type="step", step="By age", fig="<cur>£</cur>10.85",
         say="At 18 to 20 the minimum is £10.85 an hour. Under 18 and for apprentices, £8.00. From April 2027: <b>£11.27</b> and <b>£8.31</b>.",
         note="An apprentice aged 19 or over past the first year gets the rate for their age. In agriculture, Scotland, Wales and Northern Ireland set their own rates, which can be higher."),
    dict(type="step", step="Who does NOT get it", fig="0",
         say="If you work for yourself, running your own business, the minimum wage does not apply — you set your own price. Volunteers are not covered either.",
         note="Company directors are not covered — unless they also have an employment contract with the company, and then they are. Nor are family members living in the employer's home."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Minimum wage · now and from April 2027",
    h1="Is the hourly rate <em>right</em>?",
    say="Send us a payslip and we will check the rate against the hours. If you run a payroll, we will check that too. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("The rates from April 2026 — £12.71 for 21 and over, £10.85 for 18 to 20, £8.00 under "
     "18 and £8.00 apprentice — the April 2027 rates of £13.21, £11.27, £8.31 and £8.31, "
     "that rates change on 1 April, and the apprentice-rate rule for those 19 or over past "
     "their first year",
     "https://www.gov.uk/national-minimum-wage-rates", "2026-11-05"),
    ("Who is not entitled: self-employed people running their own business, company "
     "directors, volunteers and voluntary workers, members of the armed forces, family "
     "members of the employer living in the employer's home, workers younger than school "
     "leaving age, higher and further education students on work experience or a placement "
     "of up to one year, people shadowing others at work, share fishermen, prisoners, and "
     "people living and working in a religious community",
     "https://www.gov.uk/national-minimum-wage/who-gets-the-minimum-wage", "2026-11-05"),
  ],
  SCOPE=dict(
    nation="All of the UK for the headline rates — the same figures in England, Scotland, "
           "Wales and Northern Ireland. ONE DEVOLVED EXCEPTION: agriculture. Wales, "
           "Scotland and Northern Ireland each have their own agricultural wages body and "
           "an Agricultural Wages Order rate which 'will never be lower than their National "
           "Minimum Wage rate but may be higher'; England has none. So the hourly floor for "
           "an agricultural worker above entry grade in those three nations is ABOVE £12.71, "
           "and the cards must not say nobody may be paid less than £12.71. The voluntary "
           "'real Living Wage' and 'London Living Wage' set by a charity are different "
           "figures and are not these.",
    category="Workers at least of school leaving age. The National Living Wage applies from "
             "21; lower bands at 18 to 20, under 18, and for apprentices under 19 or in "
             "their first year.",
    excluded="Self-employed people running their own business are not entitled at all — the "
             "hourly minimum does not apply to them. Company directors are office holders "
             "and not entitled, BUT a director who is also employed by the company under a "
             "contract 'will be entitled to the minimum wage, like any other worker' for "
             "work done under that contract. Nor are volunteers "
             "and voluntary workers, members of the armed forces, family members of the "
             "employer who live in the employer's home, workers below school leaving age "
             "(usually 16), higher and further education students on work experience or a "
             "placement of up to one year, people shadowing others at work, share fishermen, "
             "prisoners, and people living and working in a religious community.",
    from_when="The April 2026 rates apply now. The April 2027 rates are already announced "
              "and take effect on 1 April 2027. Automatic — it is the employer's legal duty, "
              "not something a worker claims."),
)

# ==================================================================== 10
CHILD_BENEFIT = dict(
  slug="child-benefit-2026",
  title="Child Benefit — £27,05 pe săptămână și pragul de £60.000",
  tags_ro="#childbenefit #hmrc #alocatiecopii #beneficiiuk #romaniinuk",
  tags_en="#childbenefit #hmrc #hicbc #familyfinance #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Child Benefit · 2026/27",
         h1="<em>£27,05</em> pe săptămână pentru primul copil. Dar trebuie cerut.",
         say="Pentru un copil sub 16 ani — sau sub 20, dacă e încă într-o formă de școală aprobată — statul plătește o sumă fixă. Nu vine singură: se cere."),
    dict(type="step", step="Cât și cât de des", fig="<cur>£</cur>17,90",
         say="<b>£27,05</b> pe săptămână pentru primul copil și <b>£17,90</b> pentru fiecare copil următor, în anul fiscal 2026/27. Banii vin de obicei o dată la patru săptămâni.",
         note="Pentru un copil poate cere o singură persoană. Cu un copil sub 12 ani, cererea îți dă și credite pentru pensia de stat."),
    dict(type="step", step="Cine NU rămâne cu toți banii", fig="<cur>£</cur>60.000",
         say="Dacă tu sau partenerul tău câștigă peste <b>£60.000</b>, o parte se dă înapoi. Peste £80.000 se dă înapoi tot. Se uită la venitul unei persoane, nu la al gospodăriei.",
         note="Chiar și atunci merită cerut fără plată: păstrezi creditele pentru pensie și nu dai nimic înapoi."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Child Benefit · 2026/27",
    h1="Nu știi dacă <em>dai înapoi</em>?",
    say="Scrie-ne și ne uităm la venitul tău pe anul fiscal și la ce înseamnă pentru Child Benefit. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Child Benefit · 2026/27",
         h1="<em>£27.05</em> a week for the first child. But it has to be claimed.",
         say="For a child under 16 — or under 20 if they stay in approved education or training — there is a fixed weekly payment. It never starts on its own."),
    dict(type="step", step="How much, how often", fig="<cur>£</cur>17.90",
         say="<b>£27.05</b> a week for the eldest or only child and <b>£17.90</b> for each additional child, in the 2026 to 2027 tax year. Usually paid every four weeks.",
         note="Only one person can claim for a child. With a child under 12, claiming also gives you National Insurance credits towards the State Pension."),
    dict(type="step", step="Who does NOT keep all of it", fig="<cur>£</cur>60,000",
         say="If you or your partner earns over <b>£60,000</b>, part of it goes back. Over £80,000, all of it. It looks at one person's income, not the household's.",
         note="Even then it is worth claiming without the payments: you keep the pension credits and pay nothing back."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Child Benefit · 2026/27",
    h1="Not sure if you have to <em>pay it back</em>?",
    say="Message us and we will look at your income for the tax year and what it means for Child Benefit. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("Child Benefit weekly rates for the 2026 to 2027 tax year: £27.05 for the eldest or "
     "only child and £17.90 for other children",
     "https://www.gov.uk/government/publications/rates-and-allowances-tax-credits-child-"
     "benefit-and-guardians-allowance/tax-credits-child-benefit-and-guardians-allowance", "2026-11-05"),
    ("The child must be under 16, or under 20 in approved education or training; it is "
     "usually paid every 4 weeks; only one person can get Child Benefit for a child; "
     "National Insurance credits come automatically while the child is under 12; and anyone "
     "who does not want the payments should still make a claim for the other advantages",
     "https://www.gov.uk/child-benefit", "2026-11-05"),
    ("The High Income Child Benefit Charge: it applies to income over £60,000 for tax years "
     "from 2024 to 2025, 1% of the Child Benefit for every £200 over £60,000, the whole "
     "amount repaid over £80,000, assessed on the higher earner's own adjusted net income, "
     "and no charge for someone who opts out of receiving the payments",
     "https://www.gov.uk/child-benefit-tax-charge", "2026-11-05"),
  ],
  SCOPE=dict(
    nation="All of the UK — Child Benefit and the High Income Child Benefit Charge are "
           "UK-wide, no devolved variation.",
    category="Anyone responsible for a child under 16, or under 20 in approved education or "
             "training, who meets the residence conditions. One claimant per child.",
    excluded="Nobody receives it without claiming — it is never automatic, and a family that "
             "does not claim gets nothing at all. Only one person can claim for a given "
             "child, so a second parent or carer receives nothing for the same child. And it "
             "is not kept in full by everyone who receives it: where the claimant or their "
             "partner has adjusted net income over £60,000, the High Income Child Benefit "
             "Charge takes back 1% of the Child Benefit for every £200 above £60,000, and "
             "over £80,000 it takes back the whole amount. The test is on one person's "
             "income, not the household's, so two people on £50,000 each keep everything "
             "while one person on £80,000 keeps none of it. Someone over the threshold who "
             "opts out of the payments pays no charge and still keeps the National Insurance "
             "credits.",
    from_when="The 2026/27 rates apply now. Must be CLAIMED — never automatic. The £60,000 "
              "threshold has applied since the 2024/25 tax year."),
)

# ==================================================================== 11
MILEAGE_55P = dict(
  slug="kilometraj-55p",
  title="Mașina pentru muncă — 55p pe milă din 6 aprilie 2026",
  tags_ro="#cheltuieli #selfemployed #hmrc #contabilitate #romaniinuk",
  tags_en="#selfemployed #mileage #hmrc #smallbusinessuk #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Cheltuieli · Mașina pentru muncă",
         h1="O milă de muncă valorează până la <em>55p</em> din profit.",
         say="Lucrezi pe cont propriu și folosești mașina pentru muncă? Nu strângi bonuri de benzină. Scazi o sumă fixă pe milă — mai mică după primele 10.000."),
    dict(type="step", step="Cât scazi, milă cu milă", fig="55p",
         say="<b>55p</b> pentru primele 10.000 de mile într-un an fiscal, apoi <b>25p</b> pentru fiecare milă peste. Pe motocicletă, <b>24p</b> de la prima milă.",
         note="Drumul de la casă la muncă nu se numără — doar deplasările făcute pentru muncă. Până pe 5 aprilie 2026 primele 10.000 de mile se socoteau la 45p."),
    dict(type="step", step="Cine NU poate folosi suma pe milă", fig="Black cab",
         say="Contează cum e construită mașina, nu ce meserie faci. Nu intră mașinile construite pentru uz comercial — taxiurile negre, cele de școală cu dublă comandă.",
         note="Nici mașina cu costuri deja scăzute din profit. E una sau alta, iar odată aleasă, rămâi cu ea."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Cheltuieli · Mașina pentru muncă",
    h1="Nu știi <em>cum se numără</em> milele?",
    say="Scrie-ne și ne uităm împreună la ce poți scădea pe mașină. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Expenses · Using your car for work",
         h1="A business mile in your own car is worth up to <em>55p</em>.",
         say="If you are self-employed and use your own car for work, you do not have to keep every fuel receipt. You take a flat amount off your profit per mile — and the amount drops after the first 10,000."),
    dict(type="step", step="What you take off, mile by mile", fig="55p",
         say="<b>55p</b> a mile for your first 10,000 business miles in a tax year, then <b>25p</b> for every mile after that. On a motorcycle it is <b>24p</b> from the first mile.",
         note="Travel between home and work does not count — only travel for the work itself. The first 10,000 miles were 45p until 5 April 2026."),
    dict(type="step", step="Who cannot use the flat rate", fig="Black cab",
         say="Cars designed for commercial use — black cabs, hackney carriages, dual-control driving instructors' cars — are outside the flat rate altogether. So is any vehicle whose cost already came off your profits.",
         note="One method or the other, never both. And once you use the flat rate for a vehicle, you keep it for that vehicle."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Expenses · Using your car for work",
    h1="Not sure <em>how the miles count</em>?",
    say="Message us and we will go through what you can claim on the vehicle. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  GBP=[
    dict(type="solo",
         kicker="Simplified expenses · gov.uk",
         h1="Business miles are worth up to 55p now, not 45p.",
         rows=[["55p", "a business mile, first 10,000 in a tax year"],
               ["25p", "a mile after that; motorcycles 24p"],
               ["Home to work", "not a business mile — it does not count"]],
         ask="Self-employed and driving for work near Luton or Birmingham? Message us.",
         phone=PHONE, disc="General information, not personal advice."),
  ],

  SOURCES=[
    ("Simplified expenses flat rates for 2026 to 2027: 55p a mile for cars and goods "
     "vehicles for the first 10,000 miles, 25p thereafter, 24p for motorcycles; no "
     "simplified expenses for a vehicle already covered by capital allowances or whose "
     "costs are already in business profits; and once the flat rate is used for a "
     "vehicle it must be kept for that vehicle",
     "https://www.gov.uk/simpler-income-tax-simplified-expenses/vehicles", "2026-11-06"),
    ("The vehicle flat rate excludes \"cars (except those designed for commercial use, for example, black cabs, hackney carriages or dual control driving instructors' cars)\" — the test is the vehicle's DESIGN, not the driver's occupation, so an ordinary car used for private hire or ride-hailing is not excluded by this limb; and what is barred is the vehicle flat rate, not the simplified-expenses flat rates for working from home or for living at your business premises",
     "https://www.gov.uk/simpler-income-tax-simplified-expenses/vehicles", "2026-11-06"),
    ("HMRC Business Income Manual BIM75005: the fixed rate mileage deduction covers cars, motorcycles and goods vehicles used for the trade \"(except cars designed for commercial use, for example black cabs or dual control driving instructor cars)\" — it names only those two, and no occupation-based exclusion appears anywhere in it",
     "https://www.gov.uk/hmrc-internal-manuals/business-income-manual/bim75005", "2026-11-07"),
    ("Costs a self-employed person cannot claim, quoted verbatim: \"non-business driving or travel costs\", \"fines or penalty charges\" and \"travel between home and work\"",
     "https://www.gov.uk/expenses-if-youre-self-employed/travel", "2026-11-06"),
    ("The increase from 45 pence to 55 pence a mile for the first 10,000 miles, applying "
     "to the 2026 to 2027 tax year and subsequent tax years from 6 April 2026, for both "
     "Approved Mileage Allowance Payments and the self-employed simplified mileage rates; "
     "the rate above 10,000 miles is unchanged",
     "https://www.gov.uk/government/publications/increase-to-approved-mileage-allowance-"
     "payments-amaps-and-self-employed-simplified-mileage-rates/increasing-mileage-rates",
     "2026-11-06"),
  ],
  SCOPE=dict(
    nation="All of the UK — HMRC income tax rules for the self-employed, no devolved variation.",
    category="Self-employed people using simplified expenses for a car, goods vehicle or "
             "motorcycle used for business. The 55p/25p bands are per tax year, per vehicle.",
    excluded="A car designed for commercial use — a black cab, a hackney carriage, a dual-control driving instructor's car — cannot use the vehicle flat rate. The test is the vehicle's DESIGN, not the driver's occupation — which matters because private-hire and ride-hailing driving is common in this audience: a driver using an ordinary car is NOT excluded by this limb and CAN use the mileage flat rate, subject to the capital-allowances bar below. And only the vehicle flat rate is barred: the simplified-expenses flat rates for working from home and for living at your business premises are unaffected. Nor can a vehicle on which capital allowances have been claimed, or whose running costs are already in business profits: one method or the other, never both. The miles themselves are also narrower than the hook suggests — \"travel between home and work\" cannot be claimed at all, so a driver going to the same site each day cannot count that journey, and nor can non-business driving or fines. The choice is locked in: once the flat rate is used for a vehicle it must be kept for that vehicle. And the 25p band starts at mile 10,001, so a high-mileage driver does not get 55p on every mile.",
    from_when="55p applies from 6 April 2026, for the 2026/27 tax year and later years; it "
              "was 45p before that. Claimed on the tax return — nothing is paid out automatically."),
)

# ==================================================================== 12
LTD_DEADLINES = dict(
  slug="termene-firma-ltd",
  title="Firmă Ltd — cele patru termene și plata care vine înaintea declarației",
  tags_ro="#firmaltd #corporationtax #companieshouse #contabilitate #romaniinuk",
  tags_en="#limitedcompany #corporationtax #companieshouse #ukaccountant #smallbusinessuk",

  RO=[
    dict(type="hook",
         kicker="Firmă Ltd · Termene",
         h1="O firmă are <em>patru</em> termene, nu unul.",
         say="Mulți cred că o firmă depune o dată pe an. Sunt patru termene, în două locuri diferite — iar plata vine înaintea declarației."),
    dict(type="step", step="Cele trei date de la anul contabil", fig="9+1",
         say="Plătești Corporation Tax la <b>9 luni și o zi</b> după ce se încheie anul contabil. Depui bilanțul la Companies House în <b>9 luni</b>. Trimiți declarația firmei la HMRC în <b>12 luni</b>.",
         note="Exemplu: anul se încheie pe 31 decembrie 2026 → bilanțul până pe 30 septembrie 2027, plata până pe 1 octombrie 2027, declarația până pe 31 decembrie 2027."),
    dict(type="step", step="Cine NU are aceste termene", fig="0",
         say="Dacă lucrezi pe cont propriu, fără firmă, nu ai niciunul dintre ele — ai Self Assessment, cu 31 ianuarie, plus raportări trimestriale dacă intri în Making Tax Digital.",
         note="Declarația se depune și pe pierdere. Iar bilanțul și confirmation statement se depun chiar și la o firmă dormantă — iar un confirmation statement ratat poate duce la radierea firmei."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Firmă Ltd · Termene",
    h1="Nu știi <em>ce termen urmează</em>?",
    say="Trimite-ne data la care se încheie anul firmei tale și îți punem toate termenele pe hârtie. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Limited company · Deadlines",
         h1="A company has <em>four</em> deadlines, not one.",
         say="Most people expect one filing a year. A company has four deadlines, in two different places — and the payment falls due before the return."),
    dict(type="step", step="The three dates set by your year end", fig="9+1",
         say="Corporation Tax: <b>9 months and 1 day</b> after the accounting period ends. Accounts at Companies House: <b>9 months</b> after the year end. Company Tax Return: <b>12 months</b>.",
         note="Year ending 31 December 2026: accounts by 30 September 2027, payment by 1 October 2027, return by 31 December 2027."),
    dict(type="step", step="Who does NOT have these dates", fig="0",
         say="A sole trader has none of them — Self Assessment instead, due 31 January, plus quarterly updates if Making Tax Digital applies.",
         note="You file a return even after a loss. And accounts and a confirmation statement are due even for a dormant company — miss the confirmation statement and it can be struck off."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Limited company · Deadlines",
    h1="Not sure <em>which date is next</em>?",
    say="Send us your company's year end and we will set out all four deadlines. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("The Company Tax Return deadline is 12 months after the end of the accounting period "
     "it covers; Corporation Tax is usually due 9 months and one day after the end of the "
     "accounting period; and a return must still be sent after a loss or with no "
     "Corporation Tax to pay",
     "https://www.gov.uk/company-tax-returns", "2026-11-06"),
    ("Corporation Tax for taxable profits up to £1.5 million is paid 9 months and 1 day "
     "after the end of the accounting period; above £1.5 million it is paid in instalments",
     "https://www.gov.uk/pay-corporation-tax", "2026-11-06"),
    ("Deadline table: first accounts to Companies House 21 months after the date of "
     "registration; annual accounts 9 months after the financial year end; Company Tax "
     "Return 12 months after the accounting period for Corporation Tax ends; pay "
     "Corporation Tax, or tell HMRC none is owed, 9 months and 1 day after that period ends",
     "https://www.gov.uk/prepare-file-annual-accounts-for-limited-company", "2026-11-06"),
    ("The fourth deadline: at least one confirmation statement every 12 months; the review period ends 12 months after incorporation or the last confirmation statement date; it may be filed up to 14 days after the review period ends; \"You must file a confirmation statement even if there have not been any changes to your company during the review period\"; £50 online or £110 on paper; a financial penalty, a fine of up to £5,000 and strike-off from the register for not filing",
     "https://www.gov.uk/guidance/filing-your-companys-confirmation-statement", "2026-11-06"),
    ("Making Tax Digital for Income Tax applies to sole traders and landlords with qualifying income over £50,000 on the 2024-25 return from 6 April 2026, over £30,000 from 6 April 2027 and over £20,000 from 6 April 2028, and requires quarterly updates every 3 months IN ADDITION to the one annual tax return — so a sole trader no longer necessarily has a single filing date",
     "https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/introduction", "2026-11-06"),
    ("A company dormant for Corporation Tax does not have to pay Corporation Tax or file another Company Tax Return once HMRC has been told it is dormant, \"unless you receive a further notice to deliver a Company Tax Return\" — but it must still file annual accounts and a confirmation statement with Companies House",
     "https://www.gov.uk/dormant-company/dormant-for-corporation-tax", "2026-11-06"),
  ],
  SCOPE=dict(
    nation="All of the UK — Companies House covers England and Wales, Scotland and Northern "
           "Ireland, and Corporation Tax is an HMRC tax with no devolved variation.",
    category="Private limited companies registered at Companies House and within the charge "
             "to Corporation Tax, with taxable profits up to £1.5 million.",
    excluded="Sole traders and ordinary partnerships have none of these deadlines: no Corporation Tax, no accounts at Companies House, and Self Assessment on 31 January instead — though since 6 April 2026 a sole trader with over £50,000 of qualifying income on the 2024-25 return is inside Making Tax Digital for Income Tax and files quarterly updates as well, so \"one date a year\" is no longer true for them either. Companies with taxable profits above £1.5 million do not use the 9-months-and-1-day date — they pay in instalments. A brand new company's first accounts are not on the 9-month cycle: they are due 21 months after the date of registration. The confirmation statement runs on its own 12-month review period rather than the year end, with 14 days to file after it closes. A company dormant for Corporation Tax is excused the Company Tax Return once HMRC has been told, unless it receives a further notice to deliver one — so 'no company is excused' is wrong and no card says it. What a dormant company is NOT excused is Companies House: accounts and a confirmation statement are still due, and the confirmation statement is filed even when nothing has changed.",
    from_when="Three of the four run from each company's own accounting period and financial year end, so they differ per company; the confirmation statement runs on its own 12-month review period from incorporation or the last statement. All four are mandatory and none is claimed; HMRC and Companies House do not prompt them."),
)

# ==================================================================== 13
EMPLOYMENT_ALLOWANCE = dict(
  slug="employment-allowance-10500",
  title="Employment Allowance — până la £10.500 din National Insurance-ul Class 1 al firmei",
  tags_ro="#angajatori #payroll #nationalinsurance #contabilitate #romaniinuk",
  tags_en="#employmentallowance #payroll #nationalinsurance #ukaccountant #smallbusinessuk",

  RO=[
    dict(type="hook",
         kicker="Angajatori · Employment Allowance",
         h1="Până la <em>£10.500</em> din National Insurance-ul Class 1 al firmei.",
         say="Firma plătește National Insurance pentru fiecare angajat — o contribuție la stat, peste cât se oprește din salariul lui. Employment Allowance taie din partea firmei. Dar se cere."),
    dict(type="step", step="Cât și cum se cere", fig="<cur>£</cur>10.500",
         say="Se scad până la <b>£10.500</b> din National Insurance-ul Class 1 plătit de firmă într-un an fiscal. Se cere din programul de salarii, pentru un singur stat de plată — și se cere din nou la fiecare an fiscal.",
         note="Nu se reportează de la un an la altul. Dacă n-ai cerut-o deloc, se poate cere retroactiv până la 4 ani după anul fiscal respectiv."),
    dict(type="step", step="Cine NU poate cere", fig="1 director",
         say="Firma Ltd cu un singur director și niciun alt angajat cu Class 1 secundar — partea firmei. Instituțiile publice, dacă nu sunt caritate. Cine face peste jumătate din muncă pentru sectorul public.",
         note="Dar organizațiile de caritate pot cere oricum. Pentru o bonă sau un grădinar nu se scade nimic, doar dacă e îngrijitor — cine are doar personal casnic nu poate cere."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Angajatori · Employment Allowance",
    h1="Nu știi dacă <em>firma ta poate cere</em>?",
    say="Scrie-ne cum arată statul de plată și verificăm împreună. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Employers · Employment Allowance",
         h1="Up to <em>£10,500</em> off the company's National Insurance.",
         say="Once you have staff, the business pays National Insurance on top of what comes out of their wages. Employment Allowance cuts the employer's share. It is never applied on its own — it has to be claimed."),
    dict(type="step", step="How much, and how to claim", fig="<cur>£</cur>10,500",
         say="Up to <b>£10,500</b> off the employer's Class 1 National Insurance in a tax year. Claimed through your payroll software, against one payroll only — and claimed again every new tax year.",
         note="It does not carry forward. A claim never made can be backdated up to 4 years after the end of the tax year it covers."),
    dict(type="step", step="Who cannot claim", fig="1 director",
         say="A company with one director and no other employee liable for secondary Class 1. A public authority that is not a charity. An employer doing more than half its work in the public sector.",
         note="A registered charity can claim even so. Nothing comes off for a nanny or gardener, unless a care or support worker — an employer of domestic staff alone cannot claim."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Employers · Employment Allowance",
    h1="Not sure if <em>your payroll qualifies</em>?",
    say="Tell us how your payroll is set up and we will check it with you. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("The single-director bar is confined to BODIES CORPORATE and must never be written "
     "in a way that reaches a sole trader or a partnership. HMRC: \"Limited companies "
     "cannot claim Employment Allowance if they have just one director and that director "
     "is the only employee liable for secondary Class 1 National Insurance\" and, "
     "explicitly, \"This only applies to limited companies. If you're self-employed, this "
     "does not apply to you.\" NICA 2014 s.2(4A) opens \"A body corporate (\u2018C\u2019)\". The "
     "English \"a company with a single director\" maps correctly; Romanian \"firmă\" does "
     "NOT \u2014 it covers a sole trader and a partnership alike, so a bare \"firma cu un "
     "singur director\" told a self-employed reader that a bar applied to them which does "
     "not. That error was published on 7 November 2026 and corrected the same day. Every "
     "Romanian card, alt text and caption says \"firma Ltd\", never a bare \"firma\". HMRC's "
     "further guidance \u00a77 and \u00a78 are the other half of the same point: a self-employed "
     "person and a partnership CAN claim where they employ someone and pay employer "
     "Class 1",
     "https://www.gov.uk/government/publications/employment-allowance-more-detailed-guidance/single-director-companies-and-employment-allowance-further-employer-guidance", "2026-11-07"),
    ("Employment Allowance is worth up to £10,500 off the employer's Class 1 National "
     "Insurance; a single-director company cannot claim where that director is the only "
     "employee liable for secondary Class 1 National Insurance; an employer must do less "
     "than half its work in the public sector. NOTE: this short page's \"you're a business "
     "or public body\" wording is a simplification. The further employer guidance and NICA "
     "2014 s.2(1)-(2) are the rule: a public authority is barred unless it is a charity, "
     "and the share-of-work test is part of what MAKES a body a public authority, not a "
     "condition that lets one claim, so no card or caption lists a public body as able to "
     "claim. The single-director test is \"the only employee liable for SECONDARY Class 1\" "
     "— the employer's share, above the Secondary Threshold — and not \"the only employee "
     "with National Insurance\": an employee can generate primary (employee) National "
     "Insurance without the company incurring any secondary Class 1 liability at all, so "
     "the loose wording names the wrong test. That applies to the Romanian cards and "
     "captions word for word (\"Class 1 secundar — partea firmei, peste Secondary "
     "Threshold\"), not only the English; the fix is not done until it is in both "
     "languages. This page also keeps two headings apart and so does every card and "
     "caption here: \"Who cannot claim\" (the employer) is separate from \"Employees you "
     "cannot "
     "include in your claim\" — off-payroll (IR35) earnings, and personal, household or "
     "domestic work such as a nanny or gardener unless they are a care or support worker, "
     "which are excluded LIABILITIES under NICA 2014 s.2(3)-(4) while the employer stays "
     "eligible on its OTHER staff \u2014 and only then: NICA 2014 s.1(2)(b) caps the allowance "
     "at the total of the liabilities \"which are not excluded liabilities\", and the further "
     "employer guidance \u00a75 says flatly that \"Employers of domestic staff (for example, "
     "cleaners, gardeners or nannies) will be unable to claim the Employment Allowance, as "
     "the employees are all being employed in a personal capacity to support the running of "
     "a household\", so an employer whose only staff are domestic has no qualifying liability "
     "and cannot claim at all; a flat \"the employer stays eligible\" is never written. "
     "Only one company in a group and "
     "only one payroll may claim; and since April 2025 employers with Class 1 liabilities "
     "over £100,000 can apply",
     "https://www.gov.uk/claim-employment-allowance/eligibility", "2026-11-06"),
    ("\"You must claim the Employment Allowance for each new tax year by submitting an Employer Payment Summary\" — a claim is not carried forward from one tax year to the next; and a claim may be made \"up to 4 years after the end of the tax year in which the allowance applies\", so a 2022 to 2023 claim must be made by 5 April 2027",
     "https://www.gov.uk/government/publications/employment-allowance-more-detailed-guidance/claiming-employment-allowance-further-employer-guidance", "2026-11-06"),
    ("\"Functions are either wholly or mainly of a public nature, if you are carrying out "
     "more than 50% of your work in or for the public sector\" and \"if less than 50% of a "
     "business's work is of a public nature, it will be entitled to the Employment "
     "Allowance\" — so an employer at exactly 50% is entitled; and \"Registered charities "
     "can claim the Employment Allowance, even if they are wholly or mainly carrying out "
     "functions of a public nature\"",
     "https://www.gov.uk/government/publications/employment-allowance-more-detailed-guidance/eligibility-for-employment-allowance-further-employer-guidance", "2026-11-06"),
    ("Claiming for past years: \"To claim for the 2024 to 2025 tax year or earlier, your "
     "employers' Class 1 National Insurance liabilities must have been less than £100,000 "
     "the previous tax year. If you're claiming for the 2025 to 2026 tax year or later, "
     "there is no limit.\" Previous rates: £10,500 for 2025 to 2026, and £5,000 for each "
     "year between 6 April 2022 and 5 April 2025",
     "https://www.gov.uk/claim-employment-allowance/claim-for-past-years", "2026-11-06"),
    ("De minimis state aid was REPEALED for 2025 to 2026 onwards and is NEVER written as a "
     "live current-year bar. It was published as one on 7 November 2026 \u2014 on the LinkedIn "
     "caption and in the closing \"UK-wide, for the current tax year \u2014 subject to that "
     "Northern Ireland state-aid cap\" \u2014 because the previous instruction quoted the "
     "GOV.UK passage WITHOUT its scope. The scope is part of the rule. NICA 2014 "
     "s.2(4F)-(4G) are shown on legislation.gov.uk as \"omitted (6.4.2025)\", by the "
     "National Insurance Contributions (Secondary Class 1 Contributions) Act 2025 "
     "s.3(3)(a), which reads: \"In section 2 (exceptions), omit subsections (4B) to (4G) "
     "(secondary Class 1 liability limit of £100,000 or more and receipt of de minimis "
     "state aid)\", in force 6 April 2025. GOV.UK carries the state-aid test ONLY on "
     "\"Check if you can claim for previous years\" and not on the current-year eligibility "
     "page, which does not mention state aid at all; the how-to-claim page asks the "
     "state-aid question only \"If you're claiming for a previous year\". So there is no "
     "state-aid cap on a 2026/27 claim, \"UK-wide\" and the current tax year are never "
     "qualified by one, and the words \"outright bar\" are never attached to it in the "
     "present tense. It DOES still bite on claims for 2024 to 2025 and earlier \u2014 exactly "
     "the backdating this topic encourages \u2014 so the point is kept with that scope and only "
     "that scope: \"For some businesses, Employment Allowance counts as 'de minimis state "
     "aid'... There's a limit to how much de minimis state aid these businesses can get "
     "over a 3-year period. If they exceed the limit, they cannot claim Employment "
     "Allowance\", \"likely to apply to your business if both of the following are true: "
     "your business is located in Northern Ireland; your business makes or sells goods or "
     "wholesale electricity\", with 3-year limits from 20,000 euros for agricultural "
     "products to 200,000 euros for industrial and other businesses",
     "https://www.legislation.gov.uk/ukpga/2025/11/section/3", "2026-11-07"),
  ],
  SCOPE=dict(
    nation="All of the UK — employer Class 1 National Insurance is a UK-wide HMRC charge "
           "with no devolved variation, and nothing territorial qualifies a CURRENT-YEAR claim. "
           "\"UK-wide, for the current tax year\" therefore stands unqualified. The 7 November 2026 "
           "version of this field, which told captions to hang a Northern Ireland state-aid cap on "
           "it, was wrong: the de minimis state aid condition was repealed from 6 April 2025 — NICA "
           "2014 s.2(4B)-(4G) omitted by the National Insurance Contributions (Secondary Class 1 "
           "Contributions) Act 2025 s.3(3)(a) — GOV.UK carries it only on the claim-for-past-years "
           "page, and the current-year eligibility page does not mention state aid at all. The cap "
           "is a Northern Ireland carve-out on BACKDATED claims for 2024 to 2025 and earlier and on "
           "nothing else, so it is written only where the sentence is about those years. Read at "
           "primary source on 7 November 2026.",
    category="Employers paying employer Class 1 National Insurance who do less than half their work in the public sector — an employer at exactly 50% is entitled, because the test is MORE than 50% — and charities including community amateur sports clubs. A public authority is NOT in this category: NICA 2014 s.2(1) bars \"a public authority which is not a charity\", s.2(2) defines one as a person whose activities involve, wholly or mainly, the performance of functions of a public nature, and HMRC's further guidance names local authorities, town councils and parish councils as ineligible unless they have charitable status. The share-of-work test is part of what makes a body a public authority; it is not a condition on which a public body may claim, so a parish council is barred whatever proportion of its work is public-facing, and \"businesses and public bodies doing less than half their work in the public sector\" is never written as a who-CAN-claim line. The charity carve-out was read at primary source on 6 November 2026: a registered charity can claim even when it is wholly or mainly carrying out functions of a public nature, so the public-sector exclusion on every card and caption now carries it.",
    excluded="A company with one director and no other employee liable for secondary Class 1 "
             "National Insurance cannot claim at all — that is the single commonest exclusion "
             "for a small limited company. An employer carrying out MORE than half its work in "
             "or for the public sector cannot claim — but a registered charity can, even "
             "when its functions are wholly or mainly of a public nature, and an employer "
             "at exactly 50% is entitled rather than excluded, while a public authority is barred "
             "unless it is a charity however little of its work faces the public. Two different kinds "
             "of exclusion must stay apart, as GOV.UK and the statute keep them apart. The "
             "employer-level bar — NICA 2014 s.2(1) and s.2(4A) — is who \"cannot qualify\": the "
             "public authority and the single-director company; s.2(4A) opens \"A body corporate\", "
             "so it is never written in a way that reaches a sole trader or a partnership, and the "
             "Romanian says \"firma Ltd\", never a bare \"firma\". Separately, an EMPLOYEE can be "
             "outside the claim while the employer stays eligible and keeps claiming on everyone "
             "else — but ONLY where non-excluded liabilities are left, and that condition is never "
             "dropped: NICA 2014 s.1(2)(b) caps the allowance at the total of the liabilities "
             "\"which are not excluded liabilities\", and HMRC's eligibility guidance section 5 says "
             "flatly that \"Employers of domestic staff (for example, cleaners, gardeners or nannies) "
             "will be unable to claim the Employment Allowance, as the employees are all being "
             "employed in a personal capacity to support the running of a household\". An employer "
             "whose only employees are domestic staff has no eligibility left at all, so a flat "
             "\"the employer stays eligible\" — published on 7 November 2026 on LinkedIn, Pinterest "
             "and both Romanian long captions — is wrong without it. NICA 2014 s.2(3) and s.2(4) "
             "make these the \"excluded liabilities\": the "
             "earnings of an employee within off-payroll working rules, and someone employed for "
             "personal, household or domestic work such as a nanny or gardener, unless that person "
             "is a care or support worker. No card or caption puts those two under one \"who cannot "
             "claim\" heading, because that reads as though the nanny were the one barred from "
             "claiming. Within a group of connected companies or connected charities only "
             "one of them may claim, and an employer running several payrolls may claim against only one of "
             "them. A business with no employees at all is outside it entirely. And for a BACKDATED "
             "claim covering 2024 to 2025 or earlier — and only then — a business that has exceeded "
             "its de minimis state aid limit over a 3-year period cannot claim; GOV.UK puts that at "
             "its most likely where the business is both located in Northern Ireland and makes or "
             "sells goods or wholesale electricity. It was repealed from 6 April 2025, GOV.UK "
             "carries it only on the claim-for-past-years page, and it is therefore NOT a bar on a "
             "2026/27 claim and is never written as one.",
    from_when="Claimed through payroll software for EACH tax year separately — never automatic and never carried forward, so a fresh EPS claim is needed every year. NOTHING IS LOST by missing one, and no card or caption says it is: HMRC's claiming guidance section 8 allows a claim \"up to 4 years after the end of the tax year in which the allowance applies\", and section 7 says a late claim leaves a credit on the PAYE record which HMRC sets against PAYE debt or other liabilities, or repays. The 7 November 2026 LinkedIn caption said an employer who assumed it rolled over \"silently loses up to £10,500\" — unsourced, contradicted by the 4-year backdating two paragraphs later in the same post, and removed. A claim never made can be backdated up to 4 years after the end of the tax year concerned — but an earlier year is not claimed on today's terms: the allowance is £10,500 for 2025 to 2026 onwards and was £5,000 for each year between 6 April 2022 and 5 April 2025, and to claim for 2024 to 2025 or earlier the employers' Class 1 National Insurance liabilities must have been less than £100,000 in the previous tax year. The £100,000 bar was lifted from April 2025, so from 2025 to 2026 onwards there is no limit."),
)

# ==================================================================== 14
COLD_WEATHER = dict(
  slug="cold-weather-25",
  title="Cold Weather Payment — £25 pentru fiecare 7 zile de ger",
  tags_ro="#coldweatherpayment #iarna #ajutoare #beneficiiuk #romaniinuk",
  tags_en="#coldweatherpayment #costofliving #winterhelp #ukbenefits #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Iarna 2026/27 · Cold Weather Payment",
         h1="<em>£25</em> pentru 7 zile la rând de ger.",
         say="Dacă primești unul dintre câteva ajutoare, îndeplinești condițiile lui și în zona ta media e zero grade sau mai jos șapte zile la rând, de regulă banii vin automat în cont. Cerere nu se depune — dar un copil nou în casă se anunță."),
    dict(type="step", step="Pe ce ajutoare se dă", fig="4",
         say="Pension Credit, Universal Credit, Employment and Support Allowance legat de venit, sau Support for Mortgage Interest. Fiecare cu propriile condiții.",
         note="Banii vin în <b>14 zile lucrătoare</b>. Gerul se numără între 1 noiembrie 2026 și 31 martie 2027, după codul poștal. În Scoția nu există: cine ia un ajutor care dă dreptul primește Winter Heating Payment, o dată pe iarnă."),
    dict(type="step", step="Cine NU primește", fig="2 condiții",
         say="Pe Universal Credit, ambele: solicitantul și partenerul să nu fie angajați ori pe cont propriu ca ocupație principală, regulat, cu profit, ȘI unul din ei cu „capacitate limitată de muncă” ori copil sub 5 ani.",
         note="Cu suma pentru un copil cu dizabilitate se dă oricum. Un copil nou-născut sau un copil sub 5 ani mutat în casă se anunță — altfel nu mai vine automat."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Iarna 2026/27 · Cold Weather Payment",
    h1="Nu știi <em>unde se verifică</em>?",
    say="Scrie-ne și îți trimitem pagina oficială GOV.UK unde se verifică. Fără obligații.",
    phone=PHONE, disc="Informații generale, nu consultanță pe beneficii. Cere sfat de specialitate."),

  EN=[
    dict(type="hook",
         kicker="Winter 2026/27 · Cold Weather Payment",
         h1="<em>£25</em> for each 7 days running at zero or below.",
         say="If you get one of a short list of benefits, meet that benefit's own conditions, and the average temperature where you live sits at zero or below for seven days running, you'll usually get the money in your account. Nothing to claim — but a new child in the house has to be reported."),
    dict(type="step", step="Which benefits it runs on", fig="4",
         say="Pension Credit, Universal Credit, income-related Employment and Support Allowance, or Support for Mortgage Interest — each with its own conditions.",
         note="Paid within <b>14 working days</b>, for cold spells from 1 Nov 2026 to 31 Mar 2027, by postcode. Not in Scotland — a qualifying benefit brings Winter Heating Payment there, once a winter."),
    dict(type="step", step="Who does NOT get it", fig="2 tests",
         say="On Universal Credit both must hold: neither the claimant nor their partner is employed or \"gainfully self-employed\" — self-employment as their main job, worked regularly and expecting a profit — AND one of them has limited capability for work or a child under 5 at home.",
         note="A disabled child amount in the claim and it is paid either way. A new baby, or a child under 5 moving in, must be reported or it is not automatic."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Winter 2026/27 · Cold Weather Payment",
    h1="Not sure <em>where to check</em>?",
    say="Message us and we will send you the official GOV.UK page where you can check it. No obligation.",
    phone=PHONE, disc="General information, not benefits advice. Get specialist advice."),

  SOURCES=[
    ("£25 for each 7-day period where the average temperature is recorded as, or forecast "
     "to be, zero degrees celsius or below over 7 consecutive days; paid automatically with "
     "nothing to apply for; covers 1 November 2026 to 31 March 2027; England and Wales by "
     "postcode and Northern Ireland with its own checker; and \"If you live in Scotland, you "
     "cannot get Cold Weather Payments\" — the Winter Heating Payment is paid there instead",
     "https://www.gov.uk/cold-weather-payment", "2026-11-06"),
    ("Payment arrives within 14 working days of a cold period, into the same account as the "
     "benefit, for cold spells between 1 November 2026 and 31 March 2027",
     "https://www.gov.uk/cold-weather-payment/when-youll-get-paid", "2026-11-06"),
    ("Qualifying benefits and their conditions: Pension Credit; income-related ESA in a "
     "work-related activity or support group, or with a severe or enhanced disability "
     "premium, pensioner premium, disabled child or a child under 5; Universal Credit only "
     "where neither you nor your partner is employed or \"gainfully self-employed\" AND you "
     "have limited capability for work or a child under 5 — or, regardless of employment, a "
     "disabled child amount in the claim; and Support for Mortgage Interest where treated as "
     "receiving a qualifying benefit",
     "https://www.gov.uk/cold-weather-payment/eligibility", "2026-11-06"),
    ("The limited-capability-for-work limb is not the claimant's alone: \"you or your partner "
     "have a health condition or disability and have limited capability for work (with or "
     "without work-related activity)\". And the one action the claimant must take: \"If you're "
     "eligible, you'll get these payments automatically. You do not need to apply, but you may "
     "need to report a change in circumstances if you have a baby or if a child under 5 comes "
     "to live with you\" — on Universal Credit or income-related ESA, \"You will not "
     "automatically get Cold Weather Payments if you do not\"",
     "https://www.gov.uk/cold-weather-payment/eligibility", "2026-11-07"),
    ("Winter Heating Payment in Scotland is gated on a qualifying benefit exactly as the "
     "English payment is, so it is not paid to everyone in Scotland: \"Some people in Scotland "
     "get a single payment during winter called Winter Heating Payment... You will get Winter "
     "Heating Payment automatically if you get one of the benefits that make you eligible\"",
     "https://www.mygov.scot/winter-heating-payment", "2026-11-07"),
    ("Re-read on the Universal Credit work test and the Support for Mortgage Interest route. "
     "The test is NOT \"working\": \"you are not employed or 'gainfully self-employed'\" and "
     "\"your partner is not employed or 'gainfully self-employed' (if you have a partner)\", "
     "with the term defined narrowly — \"You're likely to be considered 'gainfully "
     "self-employed' if being self-employed is your main job, you work regularly and expect to "
     "make a profit.\" And SMI carries a second limb: \"You'll usually get Cold Weather "
     "Payments if you get Support for Mortgage Interest (SMI) and you're treated as getting a "
     "qualifying benefit where one of the following applies: a severe or enhanced disability "
     "premium; a pensioner premium; you have a child who is disabled; you have a child under 5 "
     "living with you. You're usually treated as getting a qualifying benefit if you apply for "
     "it but do not receive it because your income is too high.\"",
     "https://www.gov.uk/cold-weather-payment/eligibility", "2026-11-07"),
    ("The prescribed benefits behind the GOV.UK list, reg 1A(2): \"(a) state pension credit; "
     "(b) income support; (c) an income-based jobseeker's allowance; (d) an income-related "
     "employment and support allowance; (e) universal credit\" and (f)/(g) owner-occupier loan "
     "payments — six, not the four GOV.UK's page names, so Income Support and income-based JSA "
     "still qualify in law. Reg 1A(7)(b) defines the self-employment limb more tightly than "
     "the guidance: employment \"organised, developed, regular and carried on in expectation "
     "of profit\". This is why the posts keep GOV.UK's four and assert no negative about any "
     "other benefit. Read at primary source by the round-two fact-checker on 2026-11-07; "
     "legislation.gov.uk was not reachable from the repair session's proxy, so the quotations "
     "here are the fact-checker's, not re-read in that session",
     "https://www.legislation.gov.uk/uksi/1988/1724", "2026-11-07"),
    ("Re-read for round three, and legislation.gov.uk WAS reachable this time. Reg "
     "1A(3)(f)(ii): \"P has limited capability for work or limited capability for work and "
     "work-related activity as construed in accordance with regulations 39 and 40 of the "
     "Universal Credit Regulations 2013\" — so GOV.UK's \"limited capability for work (with or "
     "without work-related activity)\" is a formal determination under those regulations and "
     "not a description of being unwell. No card may render it as an illness that limits work. "
     "Reg 1A(4) also bars a person residing in a care home, an independent hospital, an "
     "Abbeyfield Society establishment or Polish Resettlement Act 1947 accommodation, except "
     "where the under-5 or disabled-child limb applies, and reg 2(6) bars payment more than 26 "
     "weeks after the winter period ends. None of that is under GOV.UK's Eligibility heading, "
     "which is why every GOV.UK benefit heading reads \"You'll usually get Cold Weather "
     "Payments if...\" — the hedge is what the cards carry, not the detail",
     "https://www.legislation.gov.uk/uksi/1988/1724/regulation/1A", "2026-11-07"),
  ],
  SCOPE=dict(
    nation="England, Wales and Northern Ireland only. NOT Scotland — GOV.UK states plainly "
           "that someone living in Scotland cannot get Cold Weather Payments. Winter Heating "
           "Payment is paid there instead, annually and regardless of the weather, but only to "
           "people who get one of the benefits that make them eligible: it is gated on a "
           "qualifying benefit in the same way, not paid to every Scottish household.",
    category="People receiving Pension Credit, income-related Employment and Support "
             "Allowance, Universal Credit or Support for Mortgage Interest, who meet that "
             "benefit's extra conditions, in a postcode area that records or is forecast a "
             "7-day cold spell. The Support for Mortgage Interest route has a second limb that "
             "is never dropped: being treated as getting a qualifying benefit is not enough on "
             "its own — one of a severe or enhanced disability premium, a pensioner premium, a "
             "disabled child or a child under 5 living with the claimant must also apply.",
    excluded="Anyone living in Scotland gets no Cold Weather Payment at all. What no card and "
             "no caption may say is that a reader on some other benefit gets nothing, and the "
             "silence is deliberate rather than an omission. GOV.UK lists four qualifying "
             "benefits and states the rule one way only — \"You may get Cold Weather Payments "
             "if you're getting\" one of them — and never the converse. The regulations behind "
             "it, SI 1988/1724 reg 1A(2), prescribe six: state pension credit, income support, "
             "an income-based jobseeker's allowance, an income-related employment and support "
             "allowance, universal credit and owner-occupier loan payments. Income Support and "
             "income-based Jobseeker's Allowance therefore still qualify in law while GOV.UK's "
             "page no longer names them. The posts cite GOV.UK, so the published list of four "
             "stays exactly as GOV.UK publishes it and is NEVER \"corrected\" by adding the "
             "other two — but the flat negative goes, because telling a reader on Income "
             "Support or income-based JSA that they get nothing would be wrong in law and would "
             "be a determination about that reader's own entitlement, which this firm is not "
             "authorised to make. State the rule, name the source, and leave the reader's own "
             "case to the source. On "
             "Universal Credit, a claimant or partner who is employed or \"gainfully "
             "self-employed\" is excluded, unless the claim includes a disabled child amount — "
             "and \"gainfully self-employed\" is narrow, not a synonym for working: GOV.UK, "
             "\"being self-employed is your main job, you work regularly and expect to make a "
             "profit\", and reg 1A(7)(b), self-employment that is \"organised, developed, "
             "regular and carried on in expectation of profit\". So small-scale or irregular "
             "self-employed work IS working and may still not be gainful self-employment, and "
             "that claimant can still qualify. No card or caption writes this limb as \"not "
             "working\" or \"să nu muncească\", which is stricter than the rule and turns that "
             "reader away wrongly. A "
             "Universal Credit claimant with no limited capability for work, no child under 5 "
             "and no disabled child amount is excluded too. On income-related ESA, someone in "
             "neither the work-related activity nor the support group is excluded unless they "
             "have one of the listed premiums or a child under 5. A postcode where no 7-day "
             "cold spell is recorded or forecast triggers no payment for anybody. And a "
             "claimant on Universal Credit or income-related ESA who qualifies only through a "
             "new baby or a child under 5 who has come to live with them, and who has not "
             "reported that change of circumstances, will not get the payment automatically.",
    from_when="Cold spells between 1 November 2026 and 31 March 2027. Automatic — no claim is "
              "made; payment follows each triggering cold period within 14 working days. The "
              "one thing that must be done: on Universal Credit or income-related ESA, a new "
              "baby or a child under 5 coming to live with the claimant has to be reported as "
              "a change of circumstances, or the payment does not arrive automatically."),
)

# ==================================================================== 15
RETURN_30_DAYS = dict(
  slug="retur-30-zile",
  title="Produs defect — dreptul de a cere banii înapoi în 30 de zile",
  tags_ro="#drepturi #consumator #baniiinapoi #romaniinuk #informatiiutile",
  tags_en="#consumerrights #refunds #knowyourrights #ukconsumer #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Drepturile cumpărătorului · 30 de zile",
         h1="Defect, de la un comerciant? <em>30 de zile</em> să ceri banii înapoi.",
         say="Nu e politica magazinului, e legea: Consumer Rights Act 2015. Dacă produsul e defect, nu e cum l-a descris vânzătorul sau nu face ce i-ai spus că ai nevoie, ceri banii — nu doar o reparație."),
    dict(type="step", step="Cele 30 de zile, exact", fig="30",
         say="Se numără de a doua zi după ce ai primit produsul și a devenit al tău. Dacă ceri reparație sau înlocuire, numărătoarea se oprește cât aștepți — iar dacă produsul primit e tot defect, ai cel puțin 7 zile de atunci.",
         note="Banii trebuie dați fără întârziere nejustificată și în cel mult <b>14 zile</b> de când vânzătorul e de acord că ți se cuvin."),
    dict(type="step", step="Cine NU are cele 30 de zile", fig="privat",
         say="Dacă ai cumpărat de la un particular, nu de la un comerciant, legea nu se aplică. Comerciant e oricine vinde în cadrul activității lui — firmă sau om pe cont propriu. Nici dacă ai cumpărat în totalitate sau în principal pentru firma ta.",
         note="La produsele perisabile termenul e mai scurt. După 30 de zile mai ai dreptul la reparație sau înlocuire."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Drepturile cumpărătorului · 30 de zile",
    h1="Vrei să <em>citești legea</em> în original?",
    say="Scrie-ne și îți trimitem textul oficial al legii. Fără obligații.",
    phone=PHONE, disc="Informații generale, nu consultanță juridică. Cere sfat de specialitate."),

  EN=[
    dict(type="hook",
         kicker="Your rights as a buyer · 30 days",
         h1="<em>30 days</em> to reject faulty goods and get a refund.",
         say="Not a shop's returns policy — the Consumer Rights Act 2015. Faulty, not as described or not fit for purpose: the first 30 days give you a refund, not a repair."),
    dict(type="step", step="The 30 days, precisely", fig="30",
         say="The clock starts the day after the goods are yours and delivered. Ask for a repair or replacement and the clock stops — if they come back still faulty you have at least 7 days from then.",
         note="A refund must be given without undue delay and in any event within <b>14 days</b> of the trader agreeing you are entitled to one."),
    dict(type="step", step="Who does NOT have the 30 days", fig="private",
         say="Buying from a private individual rather than a trader puts you outside this Act. So does buying wholly or mainly for your own business — but a buy that was mainly private keeps you a consumer.",
         note="Perishable goods have a shorter window. After 30 days you still have repair or replacement."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Your rights as a buyer · 30 days",
    h1="Want to <em>read the Act</em> yourself?",
    say="Message us and we will send you the wording of the Act itself. No obligation.",
    phone=PHONE, disc="General information, not legal advice. Get specialist advice."),

  SOURCES=[
    ("Section 22: the short-term right to reject runs to the end of 30 days, beginning the "
     "first day after ownership or possession has passed, the goods have been delivered and "
     "any required installation is done; a shorter period for goods that can reasonably be "
     "expected to perish; the clock stops for the waiting period while a requested "
     "repair or replacement is carried out; and section 22(7) — if the goods supplied in "
     "response to that request still do not conform, the time limit is then either 7 days "
     "after the waiting period ends or, if later, the original limit extended by the "
     "waiting period",
     "https://www.legislation.gov.uk/ukpga/2015/15/section/22", "2026-11-07"),
    ("Explanatory Notes to section 22, paragraph 130: \"On return of the goods to the "
     "consumer, the consumer has the remainder of the 30-day period, or 7 days (whichever "
     "is longer), within which they can still exercise the short-term right to reject if "
     "the goods still breach the standards set by the Act.\"",
     "https://www.legislation.gov.uk/ukpga/2015/15/section/22/notes", "2026-11-07"),
    ("Section 2(2): \"'Trader' means a person acting for purposes relating to that person's "
     "trade, business, craft or profession, whether acting personally or through another person "
     "acting in the trader's name or on the trader's behalf.\" The test is the seller's purpose, "
     "not whether the seller is a natural person or a company: a sole trader, a self-employed "
     "tradesman or a market trader is a person and is a trader. Section 2(7): \"'Business' "
     "includes the activities of any government department or local or public authority.\"",
     "https://www.legislation.gov.uk/ukpga/2015/15/section/2", "2026-11-07"),
    ("Section 23(6): \"A consumer who requires or agrees to the repair of goods cannot require "
     "the trader to replace them, or exercise the short-term right to reject, without giving the "
     "trader a reasonable time to repair them (unless giving the trader that time would cause "
     "significant inconvenience to the consumer).\"",
     "https://www.legislation.gov.uk/ukpga/2015/15/section/23", "2026-11-07"),
    ("Section 2(3): \"'Consumer' means an individual acting for purposes that are wholly "
     "or mainly outside that individual's trade, business, craft or profession.\" So a "
     "dual-purpose purchase that is mainly private keeps consumer status. Section 2(4): "
     "\"A trader claiming that an individual was not acting for purposes wholly or mainly "
     "outside the individual's trade, business, craft or profession must prove it.\"",
     "https://www.legislation.gov.uk/ukpga/2015/15/section/2", "2026-11-07"),
    ("Chapter 2 of Part 1: section 20(15) — a refund must be given without undue delay and "
     "in any event within 14 days of the trader agreeing the consumer is entitled to one; "
     "section 9(4) — the quality term does not cover a fault specifically drawn to the "
     "consumer's attention before the contract, or one an examination of the goods by the "
     "consumer ought to reveal; sections 23 and 24 — repair or replacement, then price "
     "reduction or the final right to reject",
     "https://www.legislation.gov.uk/ukpga/2015/15/part/1/chapter/2", "2026-11-06"),
    ("Part 1 applies to a contract between a trader and a consumer; section 2 defines a "
     "trader as a person acting for purposes relating to their trade, business, craft or "
     "profession, and a consumer as an individual acting for purposes wholly or mainly "
     "outside their trade, business, craft or profession",
     "https://www.legislation.gov.uk/ukpga/2015/15/part/1", "2026-11-06"),
    ("Section 99 (Extent): \"Section 27 extends only to Scotland\"; \"Chapter 3 of this Part [Part 3] extends only to England and Wales\"; \"Subject to that, this Act extends to England and Wales, Scotland and Northern Ireland\"",
     "https://www.legislation.gov.uk/ukpga/2015/15/section/99", "2026-11-06"),
    ("The section list of Part 1 Chapter 2 (Goods), read to place section 27: the chapter runs s3 to s32 and section 27 — \"Consignation, or payment into court, in Scotland\" — sits inside it, between s26 and s28. So the Scotland-only carve-out in s99(2) IS a Part 1 goods provision; what makes the 30-day right UK-wide is that s22, s20, s9 and s23-s24 are in neither carve-out",
     "https://www.legislation.gov.uk/ukpga/2015/15/part/1/chapter/2", "2026-11-06"),
  ],
  SCOPE=dict(
    nation="All of the UK for the 30-day right itself. Section 99 extends the Act to England and Wales, Scotland and Northern Ireland, carving out section 27 (Scotland only) and Chapter 3 of Part 3 (England and Wales only). Correction made on 6 Nov: section 27 — \"Consignation, or payment into court, in Scotland\" — DOES sit inside Part 1 Chapter 2, the goods chapter, so it is wrong to say the Part 1 goods provisions are in neither carve-out. What is UK-wide is the substance these cards rely on: s22 (the 30 days), s20 (the refund and its 14 days), s9(4) (the excluded faults) and the s23-s24 ladder. Court procedure is not uniform, and no card claims it is.",
    category="An individual buying goods from a trader for purposes wholly or mainly outside "
             "their own trade, business, craft or profession, where the goods are faulty, not "
             "as described, or not fit for a purpose made known to the trader.",
    excluded="Someone who bought from a private individual rather than a trader has no rights "
             "under this Act at all — the private-sale case is the one that catches people, "
             "and it is not a shop refusing to help, it is a different legal relationship. "
             "Someone buying for purposes wholly or mainly inside their own business is not a "
             "consumer and is outside Part 1 — but the test is \"wholly or mainly\", so a "
             "dual-purpose purchase that is mainly private keeps consumer status, and s.2(4) "
             "puts the burden on the trader to prove the buyer was not acting as a consumer. "
             "A fault the trader specifically drew to the "
             "buyer's attention before the contract, or one the buyer's own examination of "
             "the goods ought to have revealed, is not covered by the quality term. Goods "
             "that can reasonably be expected to perish sooner have a shorter window than 30 "
             "days. And after the 30 days the short-term right to reject is gone — repair or "
             "replacement comes first then, with a price reduction or a final right to reject "
             "only if that fails.",
    from_when="In force since 1 October 2015 for contracts made on or after that date. The 30 "
              "days run from the day after delivery and ownership; the right is exercised by "
              "the buyer, nothing is automatic. If a repair or replacement is requested the 30 "
              "days stop running for the waiting period, and under s.22(7), if the goods supplied "
              "in response still do not conform, the limit becomes 7 days after that period ends "
              "or the original limit extended by it, whichever is later. That turns on the goods "
              "supplied in response still not conforming: if the repair works, what is left is "
              "simply the days that were left, so no worked example can promise 7 days. And under "
              "s.23(6) a consumer who requires or agrees to a repair cannot require a replacement "
              "or exercise the short-term right to reject without giving the trader a reasonable "
              "time to repair, unless that time would cause the consumer significant inconvenience."),
)

# ==================================================================== 16
VOLUNTARY_NI = dict(
  slug="ni-voluntar-pensie",
  title="Pensia de stat — anii lipsă și cât costă să îi acoperi",
  tags_ro="#pensie #nationalinsurance #hmrc #contabilitate #romaniinuk",
  tags_en="#statepension #nationalinsurance #hmrc #ukaccountant #pensionplanning",

  RO=[
    dict(type="hook",
         kicker="Pensia de stat · Anii lipsă",
         h1="Ai lucrat în UK, dar nu în <em>fiecare</em> an?",
         say="Pensia de stat se socotește în ani care contează, nu în cât ai câștigat. Un an fără National Insurance și fără credite e o gaură în dosar. Multe găuri se pot plăti — nu toate: pentru timpul petrecut în afara UK, regulile s-au schimbat pe 6 aprilie 2026."),
    dict(type="step", step="Cât costă un an, la rata din 2026-2027", fig="<cur>£</cur>18,40",
         say="La clasa 3 e <b>£18,40</b> pe săptămână în 2026-2027 — adică <b>£956,80</b> pentru un an întreg. Cine a lucrat pe cont propriu cu profit mic plătește clasa 2, <b>£3,65</b> pe săptămână.",
         note="Plătești doar pentru ultimii <b>6</b> ani fiscali, până pe 5 aprilie. Anii mai vechi au rata de acum. Clasa 3 pe ultimii doi ani, și clasa 2 pe ultimul an, au rata din anul lor."),
    dict(type="step", step="Cine NU poate plăti", fig="0 găuri",
         say="Pentru un an fiscal care nu are gaură nu poți plăti — în afară de cine primește credite clasa <b>3</b> și are dreptul la clasa <b>2</b>. Nici după termen. Condiția e pe an fiscal, nu pe persoană.",
         note="De obicei ai nevoie de <b>10</b> ani ca să primești ceva, iar anii din SEE (România e în SEE) pot intra la acest minim, nu la sumă. GOV.UK: plata „nu crește întotdeauna pensia\"."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Pensia de stat · Anii lipsă",
    h1="Nu știi <em>câți ani</em> ai în dosar?",
    say="Scrie-ne și ne uităm împreună la dosarul tău de National Insurance. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="State Pension · The missing years",
         h1="Worked in the UK, but not in <em>every</em> year?",
         say="The State Pension is counted in qualifying years, not in how much you earned. A year with no National Insurance and no credits is a gap in the record. Many gaps can be paid for — not all: for time spent abroad, the rules changed on 6 April 2026."),
    dict(type="step", step="What a year costs at the 2026-27 rate", fig="<cur>£</cur>18.40",
         say="Class 3 is <b>£18.40</b> a week in 2026 to 2027 — <b>£956.80</b> for a whole year. If you were self-employed with small profits, Class 2 is <b>£3.65</b> a week.",
         note="You can only pay for the past <b>6</b> tax years, by 5 April. Older years are at today's rate. Class 3 for the last two years, and Class 2 for the last year, are at their own year's rate."),
    dict(type="step", step="Who cannot pay", fig="0 gaps",
         say="You cannot pay for a tax year with no gap — unless you get Class <b>3</b> credits and can pay Class <b>2</b>. Nor past the deadline. The test is on the tax year, not the person.",
         note="<b>Usually</b> 10 qualifying years are needed before any is paid. EEA contributions count towards that minimum, not the amount. GOV.UK: paying \"does not always increase your State Pension\"."),
  ],
  CTA_EN=dict(type="cta",
    kicker="State Pension · The missing years",
    h1="Not sure <em>how many years</em> you have paid?",
    say="Message us and we will go through your National Insurance record with you. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("Voluntary National Insurance rates for the 2026 to 2027 tax year, quoted verbatim: \"£3.65 a week for Class 2\" and \"£18.40 a week for Class 3\"; Class 2 for the previous tax year and Class 3 for the previous two tax years are paid at the original rate for those years, and \"If you're paying for any earlier years, you'll pay the rate for 2026 to 2027\"",
     "https://www.gov.uk/voluntary-national-insurance-contributions/rates", "2026-11-07"),
    ("The deadline, quoted verbatim: \"You can only pay voluntary contributions for the past 6 years\" and \"The deadline is 5 April each year\", with the worked example \"you have until 5 April 2032 to make up gaps for the tax year 2025 to 2026\"",
     "https://www.gov.uk/voluntary-national-insurance-contributions/deadlines", "2026-11-07"),
    ("Who cannot pay at all: someone who does \"not have gaps in your National Insurance record - unless you're getting Class 3 credits and are eligible to pay Class 2 contributions\", a \"married woman or widow paying reduced rate National Insurance\", or anyone who has \"passed the deadline for paying contributions for the period that has gaps\". The warning, verbatim: \"Voluntary contributions do not always increase your State Pension, for example if you were contracted out\", with the instruction to check a State Pension forecast first and to \"check if you're eligible for National Insurance credits before deciding to pay voluntary contributions\". Class 2 voluntarily is listed for someone \"self-employed and have annual profits of less than £7,105\"",
     "https://www.gov.uk/voluntary-national-insurance-contributions", "2026-11-07"),
    ("\"The full rate of new State Pension is £241.30 a week\"; a record that started after April 2016 needs \"35 qualifying years to get the full rate of new State Pension\", and someone contracted out before 2016 \"will usually need more than 35 qualifying years\"",
     "https://www.gov.uk/new-state-pension/what-youll-get", "2026-11-07"),
    ("\"You'll need 10 qualifying years on your National Insurance record to get any new State Pension\"",
     "https://www.gov.uk/new-state-pension/how-its-calculated", "2026-11-07"),
    ("Benefit and pension rates for 2026 to 2027: new State Pension full weekly rate £241.30, basic State Pension £184.90 — confirming the £241.30 figure belongs to the 2026/27 tax year and not to an earlier one",
     "https://www.gov.uk/government/publications/benefit-and-pension-rates-2026-to-2027/proposed-benefit-and-pension-rates-2026-to-2027", "2026-11-07"),
    ("Time spent abroad, read on the page itself: \"You cannot pay voluntary Class 2 National Insurance contributions for time abroad\"; Class 3 for time spent abroad after 5 April 2026 is applied for and carries its own conditions; \"You must apply to pay voluntary National Insurance contributions for time abroad\" and \"Do not make any payments until you get a letter from HMRC\" giving how much to pay and the payment reference number; and the transitional dates — contributions applied for under the previous rules paid on or before 5 April 2027, and an application to pay Class 3 for 2026 to 2027 on or before 5 April 2027. This is the page behind the sentence on card 1 that the rules for time abroad changed on 6 April 2026",
     "https://www.gov.uk/voluntary-national-insurance-contributions/if-you-live-or-work-abroad", "2026-11-07"),
    ("What a qualifying year is, quoted verbatim — a year in which you were \"working and made National Insurance contributions\", \"getting National Insurance credits\" or \"paying voluntary National Insurance contributions\" — which is why the cards and the Romanian caption say years that count rather than years paid; and \"You'll need 10 qualifying years on your National Insurance record to get any new State Pension\", with \"You might also qualify if you've lived or worked abroad\"",
     "https://www.gov.uk/new-state-pension", "2026-11-07"),
    ("The 10-year minimum is a usual minimum, not an absolute one: \"You usually need 10 qualifying years on your National Insurance record to be eligible. You could still be eligible if you made contributions to the state pensions in: the European Economic Area (EEA)\", with the page's worked example of 7 UK qualifying years plus 16 years in an EEA country meeting the minimum. Those contributions count towards the minimum qualifying period only, not towards the amount, which is worked out on UK qualifying years. NOTE: this page would not load on 7 November 2026 (the fetch was blocked before it returned); the quotation is the one carried verbatim in the Gatekeeper fault brief for this topic and the neighbouring /new-state-pension page corroborates it with \"You might also qualify if you've lived or worked abroad\". Re-read it at source before this topic is used again",
     "https://www.gov.uk/new-state-pension/living-and-working-overseas", "2026-11-07"),
    ("The Class 2 eligibility test behind the £7,105 figure, read on the page itself: someone self-employed with \"a gross income over £1,000, but with profits of less than £7,105\"",
     "https://www.gov.uk/voluntary-national-insurance-contributions/who-can-pay-voluntary-contributions", "2026-11-07"),
  ],
  SCOPE=dict(
    nation="All of the UK — National Insurance and the State Pension are reserved to HMRC and the "
           "DWP, with no devolved variation. The rates and the 6-year window are the same in "
           "England, Scotland, Wales and Northern Ireland.",
    category="People with gaps in a UK National Insurance record who want those years to count "
             "towards the new State Pension. Class 3 is the general voluntary class; Class 2 "
             "voluntarily is for the self-employed whose annual profits are under £7,105.",
    excluded="Four separate groups do NOT benefit, and the cards name the first three. (1) Anyone whose record has ALREADY earned the full rate: with a record that started after April 2016, 35 qualifying years give the full £241.30 and a further year adds nothing. A forecast on its own does not settle this, because it shows both what the record has earned to date and what it would reach if contributions continue to State Pension age — a forecast reaching £241.30 on that assumption falls short if the person stops. (2) Anyone with no gaps in the record at all — GOV.UK says you cannot pay, the single exception being someone getting Class 3 credits who is eligible to pay Class 2. (3) Anyone past the deadline: only the past 6 tax years can be paid, by 5 April. That is the general rule, not an absolute — under reg 50 SSCR 2001 (NIM25030) HMRC may allow a later payment where the failure to pay in time was due to the contributor's ignorance or error that was not caused by a failure to exercise due care and diligence, and NIM25028 extends the limit for a year containing six months or more of full-time education, apprenticeship or training, or imprisonment. Those are formal HMRC decisions with a right of appeal (DANSP23300), so no post may state a specific older gap as closed. (4) A married woman or widow, but only for a tax year throughout the whole of which a reduced rate election was in force — NIM25016 and NIM25107, reg 132 SSCR 2001. Where the election was not in force for the whole of a tax year she may pay from that tax year onwards if she meets the other conditions, so this is a bar on particular tax years and never a lifetime disqualification of a category of person. And a fifth case where paying may be wasted money rather than barred: someone who was contracted out, where GOV.UK warns outright that voluntary contributions \"do not always increase your State Pension\" and more than 35 years are usually needed — which is why no card promises that paying raises the pension. Nor is paying always necessary even where there is a gap: NI credits can cover some years for nothing, and GOV.UK says to check eligibility for them before deciding to pay. Note also that 10 qualifying years are USUALLY needed before any new State Pension is paid at all, so someone with very few UK years is not close to a part pension by filling one gap — usually, because contributions to the state pension of an EEA country, Romania included, can count towards that 10-year minimum qualifying period. They do not count towards the amount, which is worked out on UK qualifying years, and both halves of that have to survive any rewrite. A fifth bar sits outside the record itself: for time spent abroad, voluntary Class 2 cannot be paid at all from 6 April 2026, Class 3 for periods abroad has to be applied for and carries its own conditions, and nothing is paid until HMRC writes with the amount and the reference. Eligibility to pay for a period abroad is a residence test, so no post states who can or cannot pay for time abroad: it states what GOV.UK states and points at the page.",
    from_when="The £18.40 and £3.65 weekly rates are the 2026 to 2027 rates, from 6 April 2026. "
              "The rules for time spent abroad also changed on 6 April 2026. "
              "Nothing is automatic: voluntary contributions are a payment the person chooses to "
              "make, after checking a State Pension forecast, and the window is the past 6 tax "
              "years with 5 April as the annual cut-off."),
)

# ==================================================================== 17
DIVIDENDS_1075 = dict(
  slug="dividende-10-75",
  title="Dividende din firma ta — 10,75% din 6 aprilie 2026",
  tags_ro="#firmaltd #dividende #hmrc #contabilitate #romaniinuk",
  tags_en="#limitedcompany #dividends #hmrc #ukaccountant #smallbusinessuk",

  RO=[
    dict(type="hook",
         kicker="Firmă Ltd · Dividende",
         h1="Cota de bază pe dividende e acum <em>10,75%</em>, nu 8,75%.",
         say="Din 6 aprilie 2026 au urcat primele două cote. Se aplică la orice dividend, nu doar la cel scos din firma ta. Și 10,75% e doar taxa ta: firma a plătit deja impozit pe profit, iar dividendul iese numai din profitul disponibil."),
    dict(type="step", step="Cât plătești, pe fiecare bandă", fig="<cur>£</cur>500",
         say="Primii <b>£500</b> de dividende într-un an fiscal nu se impozitează. Peste: <b>10,75%</b> în banda de bază, <b>35,75%</b> în banda mare, <b>39,35%</b> în cea de sus.",
         note="Banda ta o stabilește venitul tău total, nu dividendul singur. Exemplu, cu Personal Allowance deja folosit de alte venituri: £2.000 de dividende în banda de bază → primii £500 fără taxă, restul £1.500 × 10,75% = £161,25."),
    dict(type="step", step="Ce NU se impozitează", fig="<cur>£</cur>12.570",
         say="Dividendele care încap în partea nefolosită din cei <b>£12.570</b> de Personal Allowance nu se impozitează. Ce trece peste se impozitează. Asta pe lângă primii £500.",
         note="£12.570 e alocația obișnuită: scade cu £1 la fiecare £2 de venit peste £100.000. Nici dividendele din acțiuni ținute într-un ISA nu se impozitează — dar acțiunile firmei tale nu pot sta în ISA."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Firmă Ltd · Dividende",
    h1="Nu știi <em>cât îți rămâne</em> din dividend?",
    say="Trimite-ne cifrele firmei și le punem pe hârtie înainte să scoți banii. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Limited company · Dividends",
         h1="The basic rate on dividends is <em>10.75%</em> now, not 8.75%.",
         say="The first two rates went up on 6 April 2026, on any dividend, not just your own company's. And 10.75% is only your tax: the company is taxed on the profit first, and pays a dividend only out of what is distributable."),
    dict(type="step", step="What you pay, band by band", fig="<cur>£</cur>500",
         say="Your first <b>£500</b> of dividends in a tax year is untaxed. Above that: <b>10.75%</b> at the basic rate, <b>35.75%</b> at the higher rate, <b>39.35%</b> at the additional rate.",
         note="Your band is set by your total income, not by the dividend alone. Example, with the Personal Allowance already used by other income: £2,000 of dividends at the basic rate — the first £500 free, the remaining £1,500 × 10.75% = £161.25."),
    dict(type="step", step="What is not taxed", fig="<cur>£</cur>12,570",
         say="Dividends that fit inside the unused part of your <b>£12,570</b> Personal Allowance are not taxed. Anything above it is. That is on top of the first £500.",
         note="£12,570 is the usual allowance: it goes down by £1 for every £2 of income over £100,000. Dividends from shares held in an ISA are not taxed either — but your own company's shares cannot go in an ISA."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Limited company · Dividends",
    h1="Not sure <em>what you keep</em> from a dividend?",
    say="Send us the company's figures and we will set them out before you take the money. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  GBP=[
    dict(type="solo",
         kicker="Dividend tax · 2026/27",
         h1="Basic rate on any dividend: 10.75%, not 8.75%.",
         rows=[["<cur>£</cur>500", "of dividends a year, still untaxed"],
               ["10.75%", "basic rate; then 35.75% and 39.35%"],
               ["6 Apr 2026", "when the first two rates went up"]],
         ask="Run a limited company near Luton or Birmingham? Message us.",
         phone=PHONE, disc="General information, not personal advice."),
  ],

  SOURCES=[
    ("Quoted verbatim: \"You also get a dividend allowance of £500 each year\"; \"You do not pay tax on any dividend income that falls within your Personal Allowance\"; \"You do not pay tax on dividends from shares in an ISA (Individual Savings Account)\". The rates shown for 6 April 2026 to 5 April 2027 on dividends above the allowance: basic rate 10.75%, higher rate 35.75%, additional rate 39.35%",
     "https://www.gov.uk/tax-on-dividends", "2026-11-07"),
    ("The measure that changed them: \"the dividend ordinary rate at 10.75%\", \"the dividend upper rate at 35.75%\" and \"the dividend additional rate will remain at 39.35%\", taking effect from 6 April 2026 — and the rates that applied before, 8.75% at the basic rate and 33.75% at the higher rate since April 2022. The additional rate is unchanged, so only the first two went up",
     "https://www.gov.uk/government/publications/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income", "2026-11-07"),
    ("Rates and allowances for 2026 to 2027, cross-checking the same three figures from a second GOV.UK page: Personal Allowance £12,570, dividend allowance £500, dividend rates 10.75%, 35.75% and 39.35%. The same page is why the Personal Allowance cannot be described as a slice nobody is taxed on, quoted verbatim: \"The Personal Allowance goes down by £1 for every £2 of income above the £100,000 limit. It can go down to zero.\"",
     "https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past", "2026-11-07"),
    ("How the duty to report actually works, and it is tiered, not absent and not universal. Headings quoted verbatim: \"Report tax on dividend income up to £10,000\" and \"Report tax on dividend income over £10,000\". Over £10,000, \"You'll need to fill in a Self Assessment tax return\". Up to £10,000, \"If you send a Self Assessment tax return, you must report any dividend income on your tax return\", and otherwise you \"must let HMRC (HM Revenue and Customs) know after the end of the tax year (5 April)\" and before 5 October, either by \"asking HMRC (HM Revenue and Customs) to update your tax code\" or by contacting the helpline. And the floor: \"You do not need to tell HMRC (HM Revenue and Customs) if your dividends are within the dividend allowance for the tax year.\" Nothing on the page asks for unused Personal Allowance to be reported",
     "https://www.gov.uk/tax-on-dividends/how-to-report-tax-on-dividends", "2026-11-07"),
    ("Why 10.75% is not the cost of taking profit out of a company: the company has already been taxed on that profit. Corporation Tax for the year starting 1 April 2026 — main rate \"25%\" on profits over \"£250,000\", small profits rate \"19%\" on profits under \"£50,000\", with marginal relief between the £50,000 lower limit and the £250,000 upper limit",
     "https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax", "2026-11-07"),
    ("And a dividend cannot be paid out of money that is not there. Companies Act 2006 s.830(1), quoted verbatim: \"A company may only make a distribution out of profits available for the purpose.\" And s.830(2) defines those profits as \"its accumulated, realised profits, so far as not previously utilised by distribution or capitalisation, less its accumulated, realised losses, so far as not previously written off in a reduction or reorganisation of capital duly made\"",
     "https://www.legislation.gov.uk/ukpga/2006/46/section/830", "2026-11-07"),
    ("Why the ISA line is about the investments and not about the person: The Individual Savings Account Regulations 1998 reg 7(2)(a) requires qualifying shares to be \"either officially listed on a recognised stock exchange\" or \"admitted to trading on a recognised stock exchange\", so shares in an ordinary private limited company do not qualify. The listing condition is subject to reg 7(3), for shares in a public offer due to be listed or admitted to trading within 30 days",
     "https://www.legislation.gov.uk/uksi/1998/1870/regulation/7", "2026-11-07"),
    ("The 2022 measure that set the previous rates, confirming where 8.75%, 33.75% and 39.35% came from: it \"increases the rates of Income Tax applicable to dividend income by 1.25%\", with \"The dividend ordinary rate will be set at 8.75%\", the upper rate at 33.75% and the additional rate at 39.35%, from 6 April 2022",
     "https://www.gov.uk/government/publications/increase-of-the-rates-of-income-tax-applicable-to-dividend-income", "2026-11-07"),
  ],
  SCOPE=dict(
    nation="All of the UK — GOV.UK publishes one set of dividend rates with no separate Scottish "
           "or Welsh dividend figures, and the measure that raised them says it applies UK-wide.",
    category="Anyone with dividend income above £500 in a tax year — in this audience, mainly "
             "directors and shareholders taking money out of their own limited company, but the "
             "rates reach an individual's dividend income generally, and the cards name only the "
             "UK cases that are certainly right: listed shares, investment funds, companies the "
             "person does not control. Foreign dividends are deliberately LEFT OUT of every "
             "published caption and card: whether they are caught turns on the reader's residence "
             "history (the four-year foreign income and gains regime), and Ola is not authorised "
             "to advise on a residency position. A reader with a share portfolio outside an ISA "
             "is affected too. The band "
             "that applies is set by the person's total income, not by the dividend on its own.",
    excluded="Three AMOUNTS escape the charge, and the cards name all three. None of them is a group of people, which is the mistake this topic kept making. (1) Dividends of £500 or less in the tax year: the dividend allowance covers them. (2) Dividends that fall inside the part of the £12,570 Personal Allowance left unused by other income: the relief attaches to that slice of income, so dividends above the unused part are taxed at the normal rates — a person with £12,570 of unused allowance and £60,000 of dividends pays dividend tax on roughly £46,930 of it — and the allowance itself goes down by £1 for every £2 of income over £100,000, so it is not a slice nobody is taxed on. (3) Dividends on shares held inside a valid ISA, at any amount — but shares in an ordinary private limited company are not qualifying ISA investments, so an owner-manager cannot hold their own company shares that way, and holdings outside the ISA are taxed normally. What is NOT an exclusion is an occupation. The charge attaches to the income (ITTOIA 2005 s.383(1)), so a sole trader or a partner who owns shares outside an ISA pays dividend tax at these rates like anyone else, and a partnership can hold shares with the dividend income taxed on the partners (SA804). What is genuinely outside is the SOURCE of the money: profit drawn from an unincorporated trade is trading profit, not a dividend, so these rates do not reach a sole trader's drawings. And the increase does reach high incomes: the additional rate stayed at 39.35%, but a shareholder taxed at the upper rate took the full two points, and part of a very large dividend can still fall in the upper band — so \"the highest earners were untouched\" is not a safe reading. Finally, 10.75% is not the cost of extracting profit: it is the shareholder's income tax, on top of the corporation tax the company has already paid, and a dividend can only be paid out of profits available for the purpose.",
    from_when="10.75% and 35.75% apply from 6 April 2026, for the 2026 to 2027 tax year onwards; "
              "8.75% and 33.75% applied before that, from 6 April 2022. The £500 allowance is per "
              "tax year. Dividend tax is not deducted at source, but the duty to report is TIERED "
              "and is not 'nothing is automatic': there is nothing to tell HMRC where the "
              "dividends are within the dividend allowance; up to £10,000 a Self Assessment filer "
              "reports it on the return and anyone else tells HMRC by 5 October, with the tax "
              "collectable through a change to the tax code; over £10,000 a Self Assessment "
              "return is needed. Unused Personal Allowance is NOT reported to HMRC — it is given "
              "automatically through PAYE or in the Self Assessment calculation."),
)

# ==================================================================== 18
HOME_WORKING = dict(
  slug="birou-acasa-26",
  title="Lucrezi de acasă pe cont propriu — £10, £18 sau £26 pe lună",
  tags_ro="#cheltuieli #selfemployed #hmrc #lucrezdeacasa #romaniinuk",
  tags_en="#selfemployed #workingfromhome #hmrc",

  RO=[
    dict(type="hook",
         kicker="Cheltuieli · Lucrezi de acasă",
         h1="Munca făcută de acasă scade din profit, de la <em>£10</em> pe lună.",
         say="Lucrezi pe cont propriu și faci munca de acasă? Suma fixă ia locul cheltuielilor curente ale casei — curățenie, căldură, lumină, apă la contor."),
    dict(type="step", step="Suma, după orele pe lună", fig="<cur>£</cur>26",
         say="<b>25-50</b> de ore într-o lună → <b>£10</b>. <b>51-100</b> de ore → <b>£18</b>. <b>101</b> de ore sau mai multe → <b>£26</b>.",
         note="Exemplu: 60 de ore pe lună, tot anul → 12 × £18 = £216 scăzuți din profit. Se numără și luna începută, nu doar lunile întregi. Ține evidența orelor."),
    dict(type="step", step="Cine NU poate folosi suma fixă", fig="25h",
         say="Nu o pot folosi firmele Ltd, nici o asociere în care intră o firmă. Sub <b>25</b> de ore într-o lună nu iei suma pe luna aceea, dar celelalte luni se iau normal.",
         note="Ia locul doar cheltuielilor curente ale casei. Chiria, council tax, asigurarea, reparațiile se cer pe lângă ea, dar numai dacă o parte din casă e folosită exclusiv pentru afacere. Telefonul și internetul: partea de muncă, sau tot, dacă folosirea personală e mică."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Cheltuieli · Lucrezi de acasă",
    h1="Nu știi <em>ce poți scădea</em> de acasă?",
    say="Scrie-ne și ne uităm împreună la cheltuielile tale înainte de declarație. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Expenses · Working from home",
         h1="Work done at home comes off your profit, from <em>£10</em> a month.",
         say="Self-employed and doing the work at home? The flat rate stands in for the home's running costs — cleaning, heat and light, metered water."),
    dict(type="step", step="The amount, by hours a month", fig="<cur>£</cur>26",
         say="<b>25 to 50</b> hours in a month → <b>£10</b>. <b>51 to 100</b> hours → <b>£18</b>. <b>101</b> hours or more → <b>£26</b>.",
         note="Example: 60 hours a month, all year — 12 × £18 = £216 off your profit. A month, or part of a month, carries the full band. Keep a record of the hours."),
    dict(type="step", step="Who cannot use the flat rate", fig="25h",
         say="Limited companies cannot use it, nor a partnership with a company as a partner. Under <b>25</b> hours in a month you take nothing that month; other months are fine.",
         note="It replaces only the home's running costs. Rent, council tax, insurance and repairs come on top, but only if part of the home is used solely for the trade. Phone and internet: business share, or in full if private use is small."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Expenses · Working from home",
    h1="Not sure <em>what you can claim</em> from home?",
    say="Message us and we will go through your expenses before the return goes in. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("The flat rates, by hours of business use a month: \"25 to 50\" is \"£10\", \"51 to 100\" is \"£18\", \"101 and more\" is \"£26\". Also verbatim: \"You can only use simplified expenses if you work for 25 hours or more a month from home\", \"This means you do not have to work out the proportion of personal and business use for your home\", and \"The flat rate does not include telephone or internet expenses\"",
     "https://www.gov.uk/simpler-income-tax-simplified-expenses/working-from-home", "2026-11-07"),
    ("Who may and may not use simplified expenses, verbatim: \"Simplified expenses cannot be used by limited companies or business partnerships involving a limited company\" — they are for sole traders and \"business partnerships that have no companies as partners\". The flat rates cover some vehicles, working from home and living in your business premises, and \"You must calculate all other expenses by working out the actual costs\". Records needed: the hours worked from home, with the amount included in total expenses on the Self Assessment return",
     "https://www.gov.uk/simpler-income-tax-simplified-expenses", "2026-11-07"),
    ("HMRC Business Income Manual BIM75010, which states the same three bands and amounts and adds what the guidance page does not: the deduction \"is only available if these hours exceed 25 per month\"; the deduction for a period is the total of the monthly rates \"for each month, or part of a month\"; \"Use of the flat rate deduction is optional\" and is available whether or not the cash basis is used; more than one home is \"treated as a single home for the purposes of calculating hours worked\"; and \"Only partnerships comprising solely individual partners can claim this simplified expenses\". It also records that the flat rate does not bar a separate claim for a business share of fixed costs such as council tax, insurance and mortgage interest, nor a separate claim for telephone and broadband",
     "https://www.gov.uk/hmrc-internal-manuals/business-income-manual/bim75010", "2026-11-07"),
  ],
  SCOPE=dict(
    nation="All of the UK — simplified expenses are an HMRC income tax rule for the self-employed, "
           "with no devolved variation.",
    category="Sole traders, and partnerships made up only of individual partners, who work 25 "
             "hours or more a month from home on business activities. The band is per month, so a "
             "quiet month and a busy month can take different amounts in the same year.",
    excluded="Three groups cannot use this at all, and a fourth condition bites on a month rather than on a claimant. (1) Limited companies cannot use simplified expenses: GOV.UK and BIM75001 bar the entity whose profits are being computed, not a human being by job title — s.94H applies to \"the profits of a trade of a person\", so a director who also carries on a trade in their own name can use the flat rate in that trade, and for use of home in the directorship HMRC routes to the employment rules (BIM47820 sends the reader to EIM32760 onwards). (2) A partnership with a company as a partner is also barred; only partnerships made up solely of individual partners qualify. (3) Anyone claiming the trading allowance: claiming it rules out deducting any other expenses or allowances, which includes this flat rate — and that is exactly the small home-based trader the £10 band speaks to. (4) Not an exclusion: a month with under 25 hours of qualifying work simply produces no applicable amount for that month, and the same trader claims normally in every other month of the period (s.94H(3), each month \"or part of a month\"). The floor is \"25 or more\" hours in the s.94H(4) table and on GOV.UK, so a month of exactly 25 hours qualifies; BIM75010's body text \"only if these hours exceed 25 per month\" contradicts its own table and is not the law. Employees and directors are outside simplified expenses because it is a trading-income rule — and since 6 April 2026 s.360B ITEPA blocks an employee's own deduction for additional household expenses, so what is left for them is an employer homeworking payment under the s.316A exemption, which continues to apply. Two further limits that are easy to misread: the flat rate stands in only for the household running costs listed at BIM47820 (cleaning, heat and light, metered water), and BIM75010 is explicit that using it \"does not prohibit a separate deduction\" for fixed costs such as council tax, insurance and mortgage interest, nor \"for telephone and broadband/internet connection costs\" — those are claimed alongside the flat rate, not instead of it, so the either/or is between the flat rate and the apportioned running costs alone. Two conditions on the separate claims: rent or mortgage interest, council tax, insurance, general repairs and water rates are allowable only where \"part of the home is set aside solely for trade use for a specific period\" (BIM47820, apportioned by area and time), so a trader at the kitchen table generally gets nothing for them; and telephone and broadband are apportioned by default but \"where private use is not significant the full cost\" can be claimed (BIM47820, BIM75010). Qualifying work is any work done in the home wholly and exclusively for the trade (s.94H(4A)), including work done there by the trader's own employees, with any hour counted only once (s.94H(4B)) — not only the three \"core business activities\" BIM75010 lists.",
    from_when="These are the current flat rates on GOV.UK, read on 7 November 2026; BIM75001 dates "
              "them \"from April 2013 onwards\" and s.94H(6) lets the Treasury alter them by "
              "regulations, so they are current rather than permanent. They are claimed on the "
              "Self Assessment return. Under Making Tax Digital for Income Tax (first year "
              "2026/27) the flat rate is not a quarterly-update item: HMRC's guidance says the "
              "quarterly updates \"are summaries, not tax returns\" and \"You do not need to make "
              "any accounting or tax adjustments before sending a quarterly update\", and that "
              "after the fourth quarterly update you \"may then need to adjust the data you have "
              "sent, before you complete and submit your tax return\", which \"could include: "
              "claiming reliefs or allowances\". The guide no longer uses \"final declaration\"; "
              "the step is headed \"Submit your tax return\". Nothing is paid out and nothing "
              "arrives automatically. "
              "A month, or part of a month, carries the full band. Using the flat rate is "
              "optional; actual costs remain an alternative."),
)

# ==================================================================== 19
WARM_HOME_150 = dict(
  slug="warm-home-150",
  title="Warm Home Discount — £150 scăzuți din factura de electricitate",
  tags_ro="#facturi #warmhomediscount #ajutoare #costuldevieta #romaniinuk",
  tags_en="#warmhomediscount #energybills #costofliving #ukrights #luton",

  RO=[
    dict(type="hook",
         kicker="Facturi · Warm Home Discount",
         h1="<em>£150</em> din factura de curent, în Anglia, Scoția și Țara Galilor.",
         say="Nu primești bani în mână — furnizorul taie £150 din factură în această iarnă. În Irlanda de Nord schema nu există."),
    dict(type="step", step="Ziua pe care o verifică: 23 august 2026", fig="<cur>£</cur>150",
         say="În Anglia și Țara Galilor: tu sau partenerul declarat la DWP primeați Universal Credit, Housing Benefit, ESA pe venit sau Pension Credit, iar contul era pe numele unuia din voi sau al reprezentantului legal.",
         note="De obicei vine automat, cu o scrisoare, pusă pe factură până pe 31 martie 2027. Scoția are altă listă de ajutoare: automat doar pentru „core group”, altfel ceri la furnizor."),
    dict(type="step", step="Cine NU îl primește", fig="N. Irlanda",
         say="Contul nu e pe numele tău, al partenerului sau al reprezentantului legal? Nu îl primești. Ca titular de cont te încadrezi, chiar fără factură pe hârtie.",
         note="Nu e toată lista: Irlanda de Nord, casa de bătrâni (permanent), caravanele — excluse după registre, cu o cale pe helpline. În Scoția unii cer la furnizor."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Facturi · Warm Home Discount",
    h1="£150 vin de la <em>furnizor</em>, nu de la contabil.",
    say="Condițiile și pașii sunt pe gov.uk/the-warm-home-discount-scheme. Pentru taxe și contabilitate, scrie-ne.",
    phone=PHONE, disc="Informații generale, nu consiliere pe ajutoare. Condițiile sunt pe GOV.UK."),

  EN=[
    dict(type="hook",
         kicker="Energy bills · Warm Home Discount",
         h1="<em>£150</em> off the electricity bill — England, Scotland and Wales.",
         say="No money reaches your hand — your supplier takes £150 off the bill this winter. In Northern Ireland there is no scheme."),
    dict(type="step", step="The day they look at: 23 August 2026", fig="<cur>£</cur>150",
         say="In England and Wales: Universal Credit, Housing Benefit, income-related ESA or Pension Credit was in payment, and you, your DWP-notified partner or your legal representative was on the account.",
         note="Usually automatic, by letter, and on the bill by 31 March 2027. Scotland has its own benefits list: automatic only for the core group, otherwise you apply to your supplier."),
    dict(type="step", step="Who does NOT get it", fig="N. Ireland",
         say="Is the account in neither your name, your partner's nor a legal representative's? You do not get it. Hold the account and you do qualify — even with no paper bill.",
         note="Not the whole list: Northern Ireland, permanent care home residents, caravans — excluded by property records, though a helpline route exists. In Scotland some apply to their supplier."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Energy bills · Warm Home Discount",
    h1="The <em>£150</em> comes from a supplier, not an accountant.",
    say="The conditions and the steps are on gov.uk/the-warm-home-discount-scheme. For tax and accounts, message us.",
    phone=PHONE, disc="General information, not benefits advice. The conditions are on GOV.UK."),

  SOURCES=[
    ("England and Wales eligibility, verbatim: \"You may be eligible if all of the following applied on 23 August 2026\" — \"your energy supplier is part of the scheme\", \"you (or your partner) get certain means-tested benefits\" and \"your name (or your partner's) is on the electricity bill\". The qualifying benefits named on the page are Universal Credit, Housing Benefit, income-related Employment and Support Allowance (ESA) and Pension Credit. Letters are sent from late October 2026 to early January 2027; for an eligible household \"your letter will confirm you do not need to do anything\"; if more information is needed the helpline must be called by 26 February 2027; the discount is applied to the bill by 31 March 2027",
     "https://www.gov.uk/the-warm-home-discount-scheme/if-you-live-in-england-and-wales", "2026-11-07"),
    ("The amount and the nations, verbatim: \"a one-off £150 discount off your electricity bill\", with the money paid to the supplier rather than to the household; \"The Warm Home Discount scheme is not available in Northern Ireland\", which has an Affordable Warmth scheme instead; Scotland has its own eligibility criteria and a household there may need to apply directly to its energy supplier; a pre-pay or pay-as-you-go meter can still qualify, with the supplier explaining how, for example \"a voucher you can use to top up your meter\"; park home residents apply through a different process; and the discount \"will not affect your Cold Weather Payment or Winter Fuel Payment\"",
     "https://www.gov.uk/the-warm-home-discount-scheme", "2026-11-07"),
    ("Scotland, which is where the automatic assumption breaks: the same three conditions on 23 August 2026, a core group that gets the discount automatically and a broader group that does not, and verbatim \"If you do not get the discount automatically, you'll need to apply directly to your energy supplier\" — suppliers may set extra criteria of their own, and a household should contact its supplier as early as possible even if it got the discount last year, because the number of discounts is limited. The discount is applied to the bill by 31 March 2027",
     "https://www.gov.uk/the-warm-home-discount-scheme/if-you-live-in-scotland", "2026-11-07"),
    ("Ofgem, the regulator that administers the scheme: it \"primarily provides support through the provision of £150 energy bill rebates\", and it runs in England, Scotland and Wales but not in Northern Ireland, which has an Affordable Warmth Scheme",
     "https://www.ofgem.gov.uk/environmental-and-social-schemes/warm-home-discount-whd", "2026-11-07"),
  ],
  SCOPE=dict(
    nation="England, Scotland and Wales — and NOT Northern Ireland, where GOV.UK says the scheme "
           "is not available at all and signposts the NI Affordable Warmth scheme, which is a "
           "capital grant for insulation and heating work rather than a bill discount, is not £150, "
           "and excludes Housing Executive and housing association tenants — so it is a signpost, "
           "not a replacement. England and Wales work one way (automatic, by letter) and Scotland "
           "another (automatic only for the core group, otherwise an application to the supplier), "
           "and the four qualifying benefits named on the GOV.UK page are the England and Wales "
           "list — Scotland runs on its own regulations, where Housing Benefit alone is a "
           "broader-group route and not automatic. So this is not one UK rule.",
    category="Households where, on 23 August 2026, the person or their partner as notified to DWP "
             "was getting one of the four benefits named on the GOV.UK England and Wales page — "
             "Universal Credit, Housing Benefit, income-related ESA or Pension Credit — that "
             "person, that partner, or their LEGAL REPRESENTATIVE was the electricity "
             "ACCOUNT HOLDER or named on the electricity bill (the account is the condition, and holding it is an alternative to being named "
             "on a bill, so a prepayment customer with no paper bill can qualify), and their "
             "energy supplier was part of the scheme. Scotland has its own list and its own "
             "route, so this category is the England and Wales one.",
    excluded="The exclusion list is NOT closed, and the cards now say so. (1) Anyone whose electricity account is in none of the three names the condition allows — their own, that of a partner notified to DWP, or that of their legal representative (an appointee, attorney or deputy): the household may be on Universal Credit and still get nothing. It runs the other way too — an owner-occupier misses out where the account sits with a spouse or adult child who is neither the claimant, nor a notified partner, nor a legal representative — but if that person IS the claimant's appointee, attorney or deputy, the condition is met — and holding the account is an alternative to being named on a bill, so a lodger or sharer who holds it in their own name DOES qualify. No frequency claim is made about rented rooms; the repo has no source for one. (2) Northern Ireland entirely: GOV.UK states the scheme is not available there and signposts Affordable Warmth, which is a grant for insulation and heating work, not a bill discount. (3) Anyone whose energy supplier is not in the scheme — real, but nearly always met, because every supplier with over 1,000 domestic customer accounts is required to take part, so it does not deserve equal billing with the rest. (4) NOT an exclusion: in Scotland, being outside the core group changes the route, it does not end the claim. The broader group (Universal Credit, Income Support, income-based JSA, income-related ESA, Housing Benefit, adult disability payment, pension age disability payment) applies directly to the supplier, suppliers may add criteria, the number of discounts is capped, and the applicant must stay with that supplier until the discount is paid. (5) Further exclusions from the DESNZ eligibility statement, which no earlier version of this topic mentioned: people living permanently in a care home; caravans, which are generally excluded by how the property is classed in property records and get no letter, with a small number of permanent residences still able to qualify by contacting the helpline and evidencing that the caravan is the household's sole legal residence and that they are named on the bill; properties not supplied with electricity wholly or mainly for domestic purposes, and park home residents supplied through the site owner, who fall outside the main scheme and use a separate route. One further point that stops the post overpromising: 23 August 2026 is the qualifying date in England, Wales AND Scotland (the Scotland page states the same date), and so are the letter window, the 26 February 2027 helpline deadline and the 31 March 2027 application date; the Park Homes route is assessed on benefit or income at the time of application — and the £150 is a discount applied by the supplier, not a payment, so nobody receives cash.",
    from_when="The qualifying date is 23 August 2026 in England, Wales and Scotland alike, and "
              "so are the three dates that follow. Letters go out from late October 2026 to "
              "early January 2027; the helpline deadline, where a letter asks for more "
              "information, is 26 February 2027; and the discount is applied to the bill by 31 "
              "March 2027. Automatic in England and Wales and for Scotland's core group; claimed "
              "from the supplier for Scotland's broader group and, by a separate process, for "
              "park home residents."),
)

# ==================================================================== 20
HOLIDAY_56 = dict(
  slug="concediu-56-saptamani",
  title="Concediul plătit — 5,6 săptămâni, până la 28 de zile",
  tags_ro="#drepturilaMunca #concediu #angajati #payroll #romaniinuk",
  tags_en="#employmentrights #holidaypay #payroll #ukemployers #hrcompliance",

  RO=[
    dict(type="hook",
         kicker="Drepturi la muncă · Concediu plătit",
         h1="Concediul plătit e <em>5,6 săptămâni</em> pe an, nu un bonus.",
         say="Aproape toți cei care muncesc pentru altcineva au dreptul la el. Pentru cine lucrează 5 zile pe săptămână, înseamnă 28 de zile plătite pe an."),
    dict(type="step", step="Cum se socotește pentru tine", fig="28",
         say="Legea dă <b>săptămâni</b>, nu zile. 5 zile pe săptămână → <b>28</b> de zile. 3 zile → cel puțin <b>16,8</b>. La ore neregulate se adună ore, nu zile: <b>12,07%</b> din cât lucrezi.",
         note="Peste 28 de zile nu se mai adaugă nimic: cine lucrează 6 zile pe săptămână are tot 28. Iar sărbătorile legale nu trebuie date ca zile libere plătite — angajatorul le poate socoti în cele 28."),
    dict(type="step", step="Cine NU are acest drept", fig="Personal",
         say="Dreptul îl are cine face munca <b>personal</b> pentru cineva care nu e clientul afacerii lui. Contează cum merge relația în practică, nu eticheta.",
         note="În afara dreptului rămân cei care își poartă chiar afacerea lor, cu clienții lor. „Freelance\" sau „zero hours\" pe hârtie poate însemna tot <b>worker</b>, cu concediu plătit. Statutul îl decid tribunalele, nu noi."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Drepturi la muncă · Concediu plătit",
    h1="Faci <em>payroll</em> pentru oamenii tăi?",
    say="Scrie-ne și ne uităm la concediu și la fluturași. Nu ți s-a dat? Acas ajută gratuit — în Irlanda de Nord, LRA.",
    phone=PHONE, disc="Informații generale, nu consiliere juridică. Noi facem payroll."),

  EN=[
    dict(type="hook",
         kicker="Employment rights · Paid holiday",
         h1="Paid holiday is <em>5.6 weeks</em> a year, not a favour.",
         say="Almost everyone who works for someone else is entitled to it. For someone on a 5-day week that is 28 paid days a year."),
    dict(type="step", step="How it works out for you", fig="28",
         say="The law gives <b>weeks</b>, not days. A 5-day week → <b>28</b> days. A 3-day week → at least <b>16.8</b>. On irregular hours it builds in hours, not days: <b>12.07%</b> of what you work.",
         note="Nothing is added above 28 days: a worker on a 6-day week still gets 28. And bank holidays do not have to be given as paid leave — an employer may count them inside the 28."),
    dict(type="step", step="Who does NOT have this right", fig="Personal",
         say="The right belongs to anyone who does the work <b>personally</b> for someone who is not, under the contract, a client of a business they run.",
         note="Outside it: people in business on their own account, with their own clients. \"Freelance\" or \"zero hours\" can still be a <b>worker</b>, with paid holiday. Courts and tribunals decide status, not the label."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Employment rights · Paid holiday",
    h1="Running <em>payroll</em> for your people?",
    say="Message us and we will go through the holiday and the payslips. Not given it? Acas helps free — the LRA in Northern Ireland.",
    phone=PHONE, disc="General information, not legal advice. We run payroll."),

  SOURCES=[
    ("Quoted verbatim: \"Almost all people classed as workers are legally entitled to 5.6 weeks' paid holiday a year\" and \"Statutory paid holiday entitlement is limited to 28 days\", with the page's own examples that a worker on a 6-day week still gets only 28 days and that someone working 3 days a week gets at least 16.8 days. Also verbatim: \"Bank or public holidays do not have to be given as paid leave\", and an employer may count them towards statutory leave",
     "https://www.gov.uk/holiday-entitlement-rights", "2026-11-07"),
    ("What makes someone a worker, and so entitled: the rights listed include \"the statutory minimum level of paid holiday\", and a person is generally a worker if they \"have a contract or other arrangement to do work or services personally for a reward\", written or unwritten — including casual or irregular work where the contract uses terms like \"casual\", \"freelance\", \"zero hours\" or \"as required\"",
     "https://www.gov.uk/employment-status/worker", "2026-11-07"),
    ("The exclusion, at source: \"Employment law does not cover self-employed people in most cases because they are their own boss\", and \"they do not get holiday or sick pay when they're not working\" is listed as a typical sign of self-employment. What they keep is \"protection of their health and safety\" and, in some cases, \"protection of their rights against discrimination\"",
     "https://www.gov.uk/employment-status/selfemployed-contractor", "2026-11-07"),
    ("The accrual method for irregular hours: \"For leave years beginning on or after 1 April 2024, there is a new accrual method for irregular hour workers and part-year workers\" and \"Holiday entitlement for these workers will be calculated as 12.07% of actual hours worked in a pay period\". A worker is an irregular hours worker where paid hours in each pay period are \"under the terms of their contract, wholly or mostly variable\"; rolled-up holiday pay at 12.07% of pay, shown separately on the payslip, is optional and only for these two groups",
     "https://www.gov.uk/government/publications/simplifying-holiday-entitlement-and-holiday-pay-calculations/holiday-pay-and-entitlement-reforms-from-1-january-2024", "2026-11-07"),
    ("The 2026 bank-holiday COUNT could not be confirmed, so no count is published on any card or caption. Read 7 November 2026: gov.uk/bank-holidays renders 8 for England and Wales, 9 for Scotland and 10 for Northern Ireland, but its own 2026 tables are internally wrong — Good Friday is given as 26 March 2026 and 1 January 2026 as a Friday, when Easter Sunday 2026 is 5 April (Good Friday 3 April) and 1 January 2026 is a Thursday. gov.scot/publications/bank-holidays, read the same day, lists 10 for Scotland in 2026, including a one-off World Cup bank holiday on 15 June 2026. Two official sources disagree, so the figure is dropped rather than softened. The legal point the sentence exists to make needs no count: GOV.UK states verbatim that \"Bank or public holidays do not have to be given as paid leave\" and that an employer may count them towards statutory leave",
     "https://www.gov.uk/bank-holidays", "2026-11-07"),
    ("The status test, verbatim: reg 2(1) defines \"worker\" as an individual who has entered into or works under \"(a) a contract of employment; or (b) any other contract, whether express or implied and (if it is express) whether oral or in writing, whereby the individual undertakes to do or perform personally any work or services for another party to the contract whose status is not by virtue of the contract that of a client or customer of any profession or business undertaking carried on by the individual\". The right therefore follows the contract and what the person actually does, not an occupation or a self-description",
     "https://www.legislation.gov.uk/uksi/1998/1833/regulation/2", "2026-11-07"),
    ("The genuine statutory exclusions, which are narrow: reg 18(1) puts outside the Regulations entirely workers covered by the Merchant Shipping (Maritime Labour Convention) (Hours of Work) Regulations 2018 (seafarers), the Fishing Vessels (Working Time: Sea-fishermen) Regulations 2004 and the Merchant Shipping (Working Time: Inland Waterways) Regulations 2003; reg 18(2) disapplies regs 13 and 13A where \"characteristics peculiar to certain specific services such as the armed forces or the police\" conflict with them, for certain civil protection activities, and for workers covered by the Civil Aviation (Working Time) Regulations 2004",
     "https://www.legislation.gov.uk/uksi/1998/1833/regulation/18", "2026-11-07"),
    ("Carry-over and no qualifying period. reg 13(9), as it has read since 1 January 2024, makes leave takeable \"only ... in the leave year in respect of which it is due\" and bars payment in lieu \"except where the worker's employment is terminated\" — but both limbs are expressly \"subject to the exceptions in paragraphs (14), (15) and (17)\": (14) carry-forward where statutory family leave prevented the leave being taken, (15) carry-forward where sick leave did, \"provided it is taken by the end of the period of 18 months from the end of the leave year in which the entitlement originally arose\", and (16)-(17) carry-forward of the WHOLE entitlement where the employer failed to recognise the right, failed to give the worker a reasonable opportunity to take the leave or encourage them to do so, or failed to inform the worker that leave not taken and not carryable would be lost. reg 13A(7) lets a relevant agreement carry the 1.6 weeks into the following leave year, which is the GOV.UK statement that a worker on 28 days \"can carry over a maximum of 8 days\". reg 13(5) pro-rates the first leave year and the regulation sets no minimum length of service anywhere. So statutory leave does not simply lapse, and an earlier version of this topic that said it did was wrong",
     "https://www.legislation.gov.uk/uksi/1998/1833/regulation/13", "2026-11-07"),
    ("The two groups the 12.07% rule is limited to, at source: reg 15F(1)(a) an irregular hours worker is one whose paid hours in each pay period are, under the terms of their contract, wholly or mostly variable; reg 15F(1)(b) a part-year worker is one required to work only part of the leave year, with periods of at least a week in which they are not required to work and are not paid. Fixed contractual hours plus variable overtime fall outside both",
     "https://www.legislation.gov.uk/uksi/1998/1833/regulation/15F", "2026-11-07"),
    ("Northern Ireland, where the HEADLINE figure is the same: reg 16(1) \"a worker is entitled to a period of 1.6 weeks additional leave in each leave year\" and reg 16(2) \"The aggregate entitlement provided for in paragraph (1) and regulation 15(1) is subject to a maximum of 28 days\". nidirect's holiday entitlements page states \"The statutory minimum is 5.6 weeks, which can include bank and public holidays\", and mentions neither 12.07% accrual nor rolled-up holiday pay",
     "https://www.legislation.gov.uk/nisr/2016/49/regulation/16", "2026-11-07"),
  ],
  SCOPE=dict(
    nation="England, Scotland and Wales — the GOV.UK holiday entitlement guidance covers Great "
           "Britain. Employment law is transferred in Northern Ireland, which has its own Working "
           "Time Regulations and its own guidance published by nidirect. The HEADLINE entitlement "
           "is identical there: reg 16 of the Working Time Regulations (Northern Ireland) 2016 "
           "gives additional leave subject to \"a maximum of 28 days\" and nidirect states \"The "
           "statutory minimum is 5.6 weeks\", so a card must not leave a Northern Ireland reader "
           "thinking 5.6 weeks and 28 days may not apply to them. What genuinely differs is the "
           "detail: the NI Regulations carry no irregular hours worker, part-year worker, 12.07% "
           "accrual or rolled-up holiday pay provisions at all, and holiday disputes there go to "
           "the Labour Relations Agency rather than Acas.",
    category="People classed as workers, which GOV.UK defines broadly: anyone with a contract or "
             "other arrangement, written or unwritten, to do work or services personally for a "
             "reward. That takes in employees, and also casual, freelance-labelled and zero-hours "
             "working. Part-time workers get the same 5.6 weeks, which is fewer days.",
    excluded="Three real exclusions, and the cards name them. (1) People genuinely in business on their own account, whose customer is a client or customer of that business. The right attaches to the CONTRACT and the status test, not to an occupation or a self-description: WTR 1998 reg 2(1) defines a worker as someone who undertakes to do or perform personally any work or services for another party whose status is not that of a client or customer of a business the individual carries on. Registering as self-employed, invoicing and paying your own tax do not remove the right, and gov.uk/employment-status says HMRC may regard someone as self-employed for tax while \"they have a different status in employment law\" and that \"Someone can be both employed and self-employed at the same time.\" The outright statutory exclusions are narrow: WTR reg 18 puts seafarers, sea-fishermen and inland waterways workers outside the Regulations entirely, and disapplies regs 13 and 13A for the armed forces and police, certain civil protection activities and civil aviation workers. Ola is an accountancy practice, not a law firm: no card or caption resolves a reader\'s own status — gov.uk/employment-status says \"Courts and tribunals can make final decisions on employment status\" and offers an online check that is expressly \"for tax purposes\" only, so the cards say tribunals decide, on how the relationship works in practice, and never point a reader at that check. Holiday disputes go to Acas in Great Britain and to the Labour Relations Agency in Northern Ireland. (2) Nobody gets more than 28 days of STATUTORY leave however many days a week they work — a 6-day week still gets 28, so the 5.6 weeks is capped and \"5.6 weeks of a 6-day week\" is wrong. (3) Bank holidays are not an extra entitlement: GOV.UK says they do not have to be given as paid leave and may be counted inside the 28 days, so a worker who assumes 28 days plus bank holidays can be wrong without the employer breaking anything. No COUNT of bank holidays is published: gov.uk/bank-holidays and gov.scot disagree for Scotland in 2026 and the gov.uk 2026 table is internally inconsistent, and the point needs no count. An employer may always contract for MORE than the statutory 28 days. One more thing that is NOT an exclusion and is the most useful line on the card: a \"freelance\" or \"zero hours\" label does not remove the right — if the person does the work personally for a reward they are a worker and the holiday is theirs, which is exactly where this audience is told otherwise. For the two groups in WTR reg 15F(1) the entitlement is 12.07% of hours actually worked, in leave years beginning on or after 1 April 2024, so it is a different sum rather than no right — an irregular hours worker is one whose paid hours are wholly or mostly variable UNDER THE TERMS OF THEIR CONTRACT, so fixed contractual hours plus variable overtime are NOT irregular hours and keep the ordinary 5.6 weeks / 28 days sum; a part-year worker is required to work only part of the year with unpaid gaps of at least a week, which is where term-time and seasonal staff sit. Two further things no figure shows: reg 13(9) requires statutory leave to be taken in its own leave year and bars payment in lieu \"except where the worker\'s employment is terminated\", but it says so \"subject to the exceptions in paragraphs (14), (15) and (17)\" — so leave does NOT simply lapse. A relevant agreement can carry up to 8 of the 28 days forward (reg 13A(7)); leave untaken because of sick leave carries forward and must be taken within 18 months of the end of that leave year (reg 13(15)); leave untaken because of statutory family leave carries into the following year (reg 13(14)); and the WHOLE entitlement carries forward where the employer failed to recognise the right, to give a reasonable opportunity to take the leave or encourage it, or to inform the worker that leave not taken would be lost (reg 13(16)-(17)). Rolled-up holiday pay under reg 16A — the 12.07% uplift paid with the wages, for irregular hours and part-year workers only — is a different thing from payment in lieu of untaken leave. And reg 13 imposes no qualifying period at all, with reg 13(5) pro-rating the first leave year, so only EXTRA contractual leave can carry a length-of-service condition.",
    from_when="5.6 weeks and the 28-day cap are the long-standing statutory minimum and apply now. "
              "The 12.07% accrual method and optional rolled-up holiday pay apply to leave years "
              "beginning on or after 1 April 2024. None of it is claimed from the state — it is "
              "taken from the employer, who has to give it."),
)


# ===================================================================== 2026-11-09
# Five carousels for 9 November 2026. Every figure below was read at primary
# source on 8 November 2026 — gov.uk, HMRC manuals and notices, and
# legislation.gov.uk. Nothing comes from a news site, a blog or another firm.

SA_PENALTIES = dict(
  slug="penalizari-31-ianuarie",
  title="Self Assessment — £100 chiar dacă nu ai nicio taxă de plătit",
  tags_ro="#selfassessment #hmrc #31ianuarie #penalizari #romaniinuk",
  tags_en="#selfassessment #hmrc #31january #latefiling #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Self Assessment · termen 31 ianuarie 2027",
         h1="O zi întârziere costă <em>£100</em>.",
         say="Și £100 se plătesc chiar dacă nu ai nicio taxă de dat. Chiar dacă declarația iese pe zero. Chiar dacă ai plătit deja tot."),
    dict(type="step", step="Cât crește dacă o lași", fig="<cur>£</cur>900",
         say="După 3 luni, HMRC poate adăuga £10 pe zi, până la £900. La 6 luni și iar la 12 luni se mai pune 5% din taxă sau £300 — cât e mai mult.",
         note="Plata întârziată se numără separat: 5% din cât ai rămas de plătit la 30 de zile, apoi iar la 6 și la 12 luni, plus dobândă în fiecare zi."),
    dict(type="step", step="Cine NU plătește £100", fig="0",
         say="Amenda e pentru o declarație pe care HMRC ți-a cerut-o. Dacă nu ți-a cerut niciuna, nu ai ce depune. Iar dacă nu mai trebuie să depui, HMRC poate anula amenda.",
         note="Anunță-i din timp, înainte de 31 ianuarie: dacă spui prea târziu, amenda rămâne. Se poate contesta și cu motiv întemeiat — online sau cu formularul SA370."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Self Assessment · termen 31 ianuarie 2027",
    h1="Nu ești sigur dacă <em>trebuie</em> să depui?",
    say="Scrie-ne un mesaj și verificăm împreună, din timp. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Self Assessment · deadline 31 January 2027",
         h1="One day late costs <em>£100</em>.",
         say="And the £100 is charged even if you owe no tax at all. Even if the return comes out at nil. Even if you have already paid in full."),
    dict(type="step", step="What it grows to", fig="<cur>£</cur>900",
         say="Three months late, HMRC can add £10 a day, up to £900. At six months and again at twelve, another 5% of the tax or £300 — whichever is greater.",
         note="Paying late is counted separately: 5% of what is still unpaid at 30 days, then again at 6 and 12 months, with interest running every day."),
    dict(type="step", step="Who does NOT pay the £100", fig="0",
         say="The penalty is for a return HMRC asked you for. If you were never sent one, there is nothing to file. And if you no longer need to file, HMRC can cancel the penalty.",
         note="Tell them in good time, before 31 January — leave it too late and the penalty stands. A reasonable excuse (hospital, a death in the family) can also be appealed, online or on form SA370."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Self Assessment · deadline 31 January 2027",
    h1="Not sure whether you <em>have</em> to file?",
    say="Message us and we will check it with you, in good time. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  # Google Business takes one frame and the whole message. This is the topic
  # chosen for it on 9 November: a January deadline is what brings telephone
  # enquiries into Luton and Birmingham.
  GBP=[dict(type="solo",
        kicker="Self Assessment · 31 January 2027",
        h1="£100 even if you owe no tax.",
        rows=[["<cur>£</cur>100", "the day after 31 January, nil return or not"],
              ["<cur>£</cur>10", "a day after 3 months, up to £900"],
              ["5%", "of the tax, for paying late at 30 days"]],
        ask="Not sure you even have to file? Luton and Birmingham — message us before 31 January.",
        phone=PHONE, disc="General information, not personal advice.")],

  SOURCES=[
    ("The late filing ladder, verbatim: \"You'll get the following late filing penalties: an initial £100 penalty / "
     "after 3 months, additional daily penalties of £10 per day, up to a maximum of £900 / after 6 months, a further "
     "penalty of 5% of the tax due or £300, whichever is greater / after 12 months, another 5% or £300 charge, "
     "whichever is greater\". The same page states the late payment penalties: \"You'll get penalties of 5% of the tax "
     "unpaid at: 30 days / 6 months / 12 months. You'll also be charged interest on the amount owed\", that \"All "
     "partners will be charged a penalty if a partnership tax return is late\", and that a penalty itself must be paid "
     "\"within 30 days of the date on the penalty notice\"",
     "https://www.gov.uk/self-assessment-tax-returns/penalties", "2026-11-08"),
    ("The deadlines, verbatim: \"You must submit your online tax return by 11:59pm on 31 January 2027 or you'll get a "
     "late filing penalty\"; \"HMRC must receive your paper tax return by 11:59pm on 31 October 2026\" (already passed, "
     "so online is the only route left for 2025/26); \"You need to pay your Self Assessment tax by 11:59pm on 31 "
     "January 2027\"; and \"The last tax year started on 6 April 2025 and ended on 5 April 2026\"",
     "https://www.gov.uk/self-assessment-tax-returns/deadlines", "2026-11-08"),
    ("That the £100 is charged with no tax to pay — HMRC's own words: \"an initial £100 fixed penalty, which applies "
     "even if there is no tax to pay, or if the tax due is paid on time\". The current /penalties guidance page does "
     "NOT carry this wording, which is why it is sourced here and to statute",
     "https://www.gov.uk/government/news/eight-days-left-to-file-your-self-assessment", "2026-11-08"),
    ("Statute for the flat £100 with no tax test, \"P is liable to a penalty under this paragraph of £100\" (Sch 55 "
     "para 3); the 90 days x £10 that make the £900 and the fact that daily penalties are NOT automatic — they bite "
     "\"if (and only if)\" HMRC \"decide that such a penalty should be payable\" and \"give notice to P\" (para 4); the "
     "6-month and 12-month penalties as \"the greater of (a) 5% of any liability to tax ... and (b) £300\" (paras 5 and "
     "6); cancellation of liability where the notice to file is withdrawn (para 17A); and reasonable excuse (para 23), "
     "which expressly excludes an insufficiency of funds unless outside P's control. Extent of the Schedule is U.K., "
     "which is the basis for the cards saying the penalties are the same in all four nations. The late payment "
     "percentages sit in Sch 56 paras 1 and 3",
     "https://www.legislation.gov.uk/ukpga/2009/10/schedule/55", "2026-11-08"),
    ("No notice to file, no obligation: \"Under the self assessment (SA) regime anyone sent a notice to file an SA tax "
     "return is required to complete and file an SA tax return\", and on cancellation: \"If we agree to withdraw the "
     "obligation to file an SA tax return then any penalties for failing to file the SA tax return on time will be "
     "cancelled\". No public gov.uk guidance page states the first point in terms, so the card is written from the "
     "manual and the statute rather than quoting a promise",
     "https://www.gov.uk/hmrc-internal-manuals/compliance-handbook/ch61700", "2026-11-08"),
    ("Telling HMRC in time, verbatim: \"You must tell HMRC as soon as possible if you believe you no longer need to "
     "send a tax return. HMRC needs time to review your request before the Self Assessment deadline of 31 January. You "
     "may have to pay a penalty if you do not tell them early enough\"",
     "https://www.gov.uk/self-assessment-tax-returns/no-longer-need-to-send-a-tax-return", "2026-11-08"),
    ("The appeal route as it stands now: \"You will be able to either: make your appeal online / download form SA370 or "
     "SA371 to appeal by post\" — the old SA370 publication page now redirects here, so \"fill in SA370\" as the only "
     "route is out of date. Also \"You can ask us to cancel a penalty if you do not need to send us a Self Assessment "
     "tax return\"",
     "https://www.gov.uk/guidance/check-when-to-appeal-a-self-assessment-penalty-for-late-filing-or-late-payment",
     "2026-11-08"),
    ("Reasonable excuses gov.uk accepts and rejects, verbatim, including \"your partner or another close relative died "
     "shortly before the tax return or payment deadline\", \"you had an unexpected stay in hospital that prevented you "
     "from dealing with your tax affairs\" and, among those NOT accepted, \"you did not get a reminder from HMRC\"",
     "https://www.gov.uk/tax-appeals/reasonable-excuses", "2026-11-08"),
    ("The interest rate actually in force on publication day. The table reads \"24 November 2026 | 8.00 | 3.00\" then "
     "\"9 January 2026 | 7.75 | 2.75\", and the formula is \"late payment interest set at base rate plus 4% from 6 "
     "April 2025 (was plus 2.5% on or before 5 April 2025)\". So 7.75% is the live rate on 9 November 2026 and 8.00% "
     "starts on 24 November 2026 — the page's own \"current\" bullet quotes the rate that is not yet in force, which is "
     "the trap. Interest runs from the day after the due date (FA 2009 s.101)",
     "https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates",
     "2026-11-08"),
    ("That the OLD penalties, not the new Making Tax Digital regime, apply to this deadline — decisive and verbatim: "
     "\"The current penalties will still apply to previous tax years. For example, if you use Making Tax Digital for "
     "Income Tax from 6 April 2026, current penalties will apply to your 2025 to 2026 tax return deadline of 31 "
     "January 2027\". The points-based regime and the 3%/3%/10% late payment charges are for 2026/27 onwards",
     "https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax", "2026-11-08"),
    ("Time to Pay, for the long captions: \"If you cannot pay your tax bill in full, you may be able to set up a "
     "payment plan to pay it in instalments\" and \"There's no time limit on how long a payment plan can last\". The "
     "current guidance page publishes NO threshold; the £30,000 self-serve figure is sourced to HMRC's own release of "
     "23 January 2026 (\"may be able to set up a Time to Pay arrangement online if they owe less than £30,000 and meet "
     "all relevant criteria\"), so the captions say \"under £30,000 and you meet HMRC's conditions\" and nothing more",
     "https://www.gov.uk/difficulties-paying-hmrc", "2026-11-08"),
  ],
  SCOPE=dict(
    nation="UK-wide — England, Scotland, Wales and Northern Ireland alike. FA 2009 Schedules 55 and 56 carry the "
           "U.K. extent marker and the gov.uk deadlines and penalties guides draw no territorial distinction. "
           "Devolution changes the amount of tax (Scottish and Welsh rates of Income Tax), never the filing date or "
           "the penalty. The one real difference on gov.uk is debt enforcement, not penalties: HMRC can \"take things "
           "you own and sell them\" and \"take money directly from your bank account\" only \"if you live in England, "
           "Wales or Northern Ireland\". No gov.uk sentence says the penalties are identical in all four nations, so "
           "the cards state it plainly rather than quoting it.",
    category="Anyone HMRC has sent a notice to file for 2025/26 — typically the self-employed, landlords, company "
             "directors with untaxed income, people with Capital Gains to report, and this year anyone whose Winter "
             "Fuel Payment from autumn 2025 is being recovered through the return. Partners in a partnership are a "
             "distinct category: every partner is penalised when the partnership return is late, not just the "
             "nominated partner.",
    excluded="Three real exclusions, and the cards name them. (1) Someone HMRC never sent a notice to file. The Sch 55 "
             "penalty attaches to a return under TMA 1970 s.8, which exists only where HMRC has given notice, and "
             "CH61700 says \"anyone sent a notice to file an SA tax return is required to complete and file\" one — so "
             "a person with no notice has nothing to file late and nothing to be penalised for. No public gov.uk page "
             "says this in terms, so it is written from the manual and the statute. (2) Someone who no longer needs to "
             "file and says so in time: HMRC can withdraw the notice under TMA 1970 s.8B and \"any penalties for "
             "failing to file the SA tax return on time will be cancelled\" (CH61700, FA 2009 Sch 55 para 17A). The "
             "trap, and the reason the card carries it as a note, is the timing — gov.uk: \"HMRC needs time to review "
             "your request before the Self Assessment deadline of 31 January. You may have to pay a penalty if you do "
             "not tell them early enough.\" (3) Reasonable excuse, which cancels liability rather than reducing it (Sch "
             "55 para 23); gov.uk lists what it accepts and what it does not, and \"you did not get a reminder from "
             "HMRC\" is on the rejected list. What is NOT an exclusion, and is the most expensive misunderstanding for "
             "this audience: owing no tax. The £100 is flat and statutory and HMRC says it \"applies even if there is "
             "no tax to pay, or if the tax due is paid on time\". Nor is the £100 ever reduced — it is cancelled or it "
             "stands; HMRC's \"special circumstances\" discretion in Sch 55 para 16 expressly excludes ability to pay. "
             "Two further precisions the cards respect: the £10-a-day penalties are not automatic (HMRC must decide and "
             "give written notice, Sch 55 para 4, CH62120), and gov.uk's \"another 5% or £300\" at twelve months is the "
             "ordinary case only — where information is deliberately withheld and concealed the statutory penalty is "
             "the greater of 100% of the tax and £300, so 5% is not a ceiling.",
    from_when="Now, for the 2025/26 return. The paper deadline of 31 October 2026 has already passed, so online "
              "filing by 31 January 2027 is the only route left, and the tax is due the same day. Penalties are "
              "automatic in the sense that nothing has to be claimed by HMRC to start the £100, but the daily "
              "penalties require a decision and a notice. Cancellation always has to be asked for. Note for next "
              "year: the Making Tax Digital points-based regime does NOT touch this deadline.",
  ),
)


# ===================================================================== 2
RENT_A_ROOM = dict(
  slug="camera-inchiriata-7500",
  title="Rent a Room — £7.500 pe an fără taxe, dar £3.750 dacă nu ești singur",
  tags_ro="#rentaroom #chirie #hmrc #scutire #romaniinuk",
  tags_en="#rentaroom #lodger #hmrc #taxfree #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Chirie · Rent a Room",
         h1="Închiriezi o cameră în casa ta? Primii <em>£7.500</em> pe an sunt fără taxe.",
         say="Scutirea se numește Rent a Room. Nu o ceri și nu completezi nimic: dacă încasezi £7.500 sau mai puțin într-un an, vine automat."),
    dict(type="step", step="Se numără cât încasezi", fig="<cur>£</cur>7.500",
         say="Nu cât îți rămâne. Tot ce îți intră: chiria, plus banii pe mese, curățenie sau spălat rufe, dacă îi iei.",
         note="Peste £7.500 depui declarație și alegi: plătești pe profitul real, cu cheltuieli scăzute, sau doar pe cât ai încasat peste £7.500, fără cheltuieli."),
    dict(type="step", step="Cine NU are £7.500", fig="<cur>£</cur>3.750",
         say="Dacă și altcineva încasează chirie din aceeași casă — de obicei partenerul, când casa e pe amândoi — fiecare are £3.750. Nu se adună la £15.000.",
         note="Nu se aplică la: camera nemobilată, casa împărțită în apartamente separate, camera dată ca birou sau depozit, și casa din UK închiriată cât timp tu stai în altă țară."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Chirie · Rent a Room",
    h1="Nu știi dacă <em>intri</em> în scutire?",
    say="Scrie-ne și ne uităm împreună la cât ai încasat și la ce trebuie depus. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Letting · Rent a Room",
         h1="A lodger in your own home? The first <em>£7,500</em> a year is tax free.",
         say="The relief is called Rent a Room. You do not claim it and you fill nothing in: take £7,500 or less in a year and it applies automatically."),
    dict(type="step", step="It counts what comes in", fig="<cur>£</cur>7,500",
         say="Not what you keep. Everything you receive: the rent, plus anything you charge for meals, cleaning or laundry.",
         note="Over £7,500 you file a return and choose: pay on your actual profit with expenses deducted, or on your receipts above £7,500 with no expenses at all."),
    dict(type="step", step="Who does NOT get £7,500", fig="<cur>£</cur>3,750",
         say="If anyone else also receives letting income from the same home — usually a partner, where the house is in both names — you get £3,750 each. It does not add up to £15,000.",
         note="It does not apply to: an unfurnished room, a house split into separate flats, a room let as an office or for storage, or a UK home let while you live abroad."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Letting · Rent a Room",
    h1="Not sure the relief <em>covers</em> you?",
    say="Message us and we will go through what you took and what has to be filed. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("The threshold and the halving, verbatim: \"The Rent a Room Scheme lets you earn up to a threshold of £7,500 per "
     "year tax-free from letting out furnished accommodation in your home. The threshold is halved to £3,750 if you "
     "share the income with someone else.\" The same page: \"The tax exemption is automatic if you earn less than your "
     "threshold. Which means you do not need to do anything\"; \"You must complete a tax return if you earn more than "
     "your threshold\"; \"You can let out as much of your home as you want\"; and \"You cannot use the scheme for "
     "homes converted into separate flats\"",
     "https://www.gov.uk/rent-room-in-your-home/the-rent-a-room-scheme", "2026-11-08"),
    ("Statute, which is why the £7,500 can be stated for 2026/27 even though HMRC's latest helpsheet is still headed "
     "2025 to 2026: ITTOIA 2005 s.789 fixes the amount permanently rather than annually — \"The basic amount for a tax "
     "year is £7500\" — and makes the halving turn on the exclusive receipts condition: \"If the individual does [meet "
     "it], the individual's limit for the tax year is the basic amount... If the individual does not, the individual's "
     "limit for the tax year is half that amount.\" s.790 defines that condition by reference to receipts accruing to "
     "any other person for the use of accommodation in the residence or for \"goods or services supplied in connection "
     "with that use (such as meals, cleaning or laundry)\", and s.786(1) requires \"furnished accommodation in a "
     "residence in the United Kingdom\" which \"is the individual's only or main residence\" for some or all of the "
     "period. Extent of each section is U.K.",
     "https://www.legislation.gov.uk/ukpga/2005/5/section/789", "2026-11-08"),
    ("Gross receipts, not profit, and the exclusions list, verbatim from HMRC's helpsheet: \"Your gross receipts "
     "include: rental income (before expenses); any amounts you receive for meals, goods and services, such as "
     "cleaning or laundry; any 'balancing charges'\"; \"If your gross receipts are less than £7,500 (or £3,750) you're "
     "automatically exempt from tax on that income\"; the two methods, \"Method A You pay tax on your actual profit\" "
     "and \"Method B You pay tax on your gross receipts over the Rent-a-Room limit... You cannot deduct any expenses "
     "or capital allowances if you choose this method\", with \"HMRC will automatically use your actual profit (Method "
     "A)\"; and \"You cannot use the scheme if the accommodation is: ... not furnished ... not part of your main home "
     "when you let it ... in your UK home and is let while you live abroad ... used as an office or for any business — "
     "you can use the scheme if your lodger works in your home in the evening or at weekends or is a student who is "
     "provided with study facilities\". Note the dating caveat: this is the 2025 to 2026 helpsheet, the latest "
     "published; no 2026 to 2027 version exists yet",
     "https://www.gov.uk/government/publications/rent-a-room-for-traders-hs223-self-assessment-helpsheet/hs223-rent-a-room-scheme-2026",
     "2026-11-08"),
    ("HMRC's Property Income Manual on the halving and on who qualifies: \"The exemption limit of £7,500 is reduced to "
     "£3,750 if during the tax year to 5 April, someone else received income from letting accommodation in the same "
     "property. This may happen where the taxpayer owns their home jointly with another person\" (PIM4010, which also "
     "states that a UK home let while the owner lives abroad \"will not normally be within rent-a-room\"); and from "
     "PIM4001, \"For the purposes of the rent-a-room scheme, gross receipts include not only rents but also payments "
     "made to the taxpayer for the provision of any other goods or services\", \"Rent-a-room applies to people who let "
     "a room in a home they rent as well as to people who own their homes\", and \"Only residential accommodation used "
     "as such qualifies. There is no relief if, for example, a room in the residence is let as an office or for "
     "storage\"",
     "https://www.gov.uk/hmrc-internal-manuals/property-income-manual/pim4010", "2026-11-08"),
    ("Furnished only, with the sting that one unfurnished letting in the same residence poisons the rest: \"Rent-a-room "
     "applies to furnished lettings only. If the taxpayer has any unfurnished letting in his only or main residence, "
     "then he or she is not a qualifying individual. Therefore any furnished letting the same taxpayer has in the same "
     "residence cannot attract rent-a-room relief\"",
     "https://www.gov.uk/hmrc-internal-manuals/property-income-manual/pim4012", "2026-11-08"),
    ("Why the £1,000 property allowance is not an alternative on the same money: \"You can get up to £1,000 each tax "
     "year in tax-free allowances for property or trading income\", \"You cannot use this allowance on income from "
     "letting a room in your own home under the Rent a Room Scheme\", and \"You cannot use the property allowance if "
     "you: ... deduct expenses from income from letting a room in your own home instead of using the Rent a Room "
     "Scheme\". The property allowance is a separate £1,000 from the trading allowance — \"If you have both types of "
     "income, you'll get a £1,000 allowance for each\"",
     "https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income", "2026-11-08"),
    ("Council tax and the bills, verbatim: \"You will be responsible for Council Tax and can include part of the cost "
     "in the rent you charge. You must tell your council if having a tenant means you're no longer entitled to a "
     "single person discount\". Also on the same guide: \"You may have to pay Capital Gains Tax when you sell your "
     "home if: you let out all or part of it; you've taken in more than one tenant or lodger at a time\"",
     "https://www.gov.uk/rent-room-in-your-home/rent-bills-and-tax", "2026-11-08"),
    ("The lodger's rent and Universal Credit, from DWP's own decision-making guidance (ADM Chapter H5, para H5112) "
     "rather than from any ordinary UC guidance page, which is silent: \"Because this weekly income from a sub-tenant "
     "or boarder is not defined as income for the purposes of UC, it is not taken into account as Teresa's unearned "
     "income. Note 1: It is not relevant whether the rental income is above or below the 'rent a room' tax relief "
     "limits. Note 2: if a self-employed claimant is renting out rooms in their house as part of conducting a trade, "
     "for example running a B&B, then that income would be taken into account in the same way as other earnings\"",
     "https://assets.publishing.service.gov.uk/media/691c864ad140bbbaa59a29a0/adm-ch-h5-unearned-income.pdf",
     "2026-11-08"),
  ],
  SCOPE=dict(
    nation="UK-wide as a matter of tax. ITTOIA 2005 ss.786, 789 and 790 each carry the U.K. extent marker and s.786(1) "
           "speaks of \"a residence in the United Kingdom\". What is NOT UK-wide, and must not be conflated with the "
           "tax relief, is landlord registration and licensing: Scotland requires landlord registration but exempts "
           "someone who lives \"in the property as a resident landlord\"; Wales requires Rent Smart Wales "
           "registration but the duty \"does not apply ... if an owner occupier has one or more lodgers in their home "
           "and the lodgers share amenities with the homeowner\"; Northern Ireland's Landlord Registration Scheme is "
           "stated in absolute terms on nidirect with no lodger exemption named either way, so no claim is made about "
           "it; and in England letting rooms to more than two people can make the property a House in Multiple "
           "Occupation needing a licence. One genuine future divergence on the tax side: the new separate property "
           "income rates from April 2027 apply \"to England, Wales and Northern Ireland\", with Scotland and Wales "
           "able to set their own.",
    category="An individual — not a company and not a partnership — who lets furnished living accommodation in the "
             "home that is their own only or main residence, whether they own it or rent it themselves. It reaches a "
             "resident landlord with a lodger, a family taking in a student, and someone running a bed and breakfast "
             "or guest house from their own home. Joint owners can each use it where they hold the income jointly "
             "without being a partnership.",
    excluded="The exclusions are the whole point of card 3, and there are two kinds. First, the halving, which is the "
             "one people lose money on: the £7,500 is an individual's limit, but it drops to £3,750 each where anyone "
             "else receives letting income from the same residence, which is the ordinary case for a couple who own "
             "the house together. Two people letting one room do not get £15,000 between them and do not get one "
             "£7,500 — they get £3,750 apiece. Second, the outright disqualifications in HS223 and the manual: "
             "accommodation that is not furnished (and HMRC goes further in PIM4012 — any unfurnished letting in the "
             "same residence makes the person a non-qualifying individual, so the furnished letting loses relief too); "
             "accommodation that is \"not part of your main home when you let it\"; a UK home let while the owner "
             "lives abroad; a room let as an office, for a business or for storage, with a narrow carve-out where a "
             "lodger works at home in the evenings or a student is given study facilities; and a home converted into "
             "separate flats. A self-contained flat inside the main residence is a question of fact under PIM4004 — it "
             "qualifies only where the division is temporary — so no flat rule is stated. Companies and partnerships "
             "are outside the scheme altogether. Three further things that are NOT exclusions and are worth knowing: "
             "renting rather than owning the home is fine; the limit is the same even if the letting ran for less than "
             "twelve months; and a lodger's rent is not counted as income for Universal Credit, whatever the tax "
             "limits say, unless the letting is part of a trade such as a B&B. And one real cost that is not a tax "
             "exclusion: taking in a lodger normally ends the 25% council tax single-person discount, which the "
             "council has to be told about, unless the lodger is in a disregarded category.",
    from_when="Now, and for 2026/27. The amount is fixed by statute rather than set each year, so it does not change "
              "with the tax year. Below the limit the relief is automatic with nothing to claim and no need to tell "
              "HMRC; above it a return is required and Method B has to be elected in writing within one year of the "
              "31 January following the tax year, with HMRC defaulting to actual profit if nothing is said. Two "
              "changes already legislated or announced are outside what the cards claim: separate property income "
              "rates of 24%, 44% and 49% from 6 April 2027, and the trading allowance — not the property allowance — "
              "rising to £3,000 from the same date.",
  ),
)


# ===================================================================== 3
CGT_60_DAYS = dict(
  slug="cgt-60-zile",
  title="Ai vândut o casă care nu era casa ta — 60 de zile ca să declari și să plătești",
  tags_ro="#capitalgainstax #proprietate #hmrc #60dezile #romaniinuk",
  tags_en="#capitalgainstax #ukproperty #hmrc #60days #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Capital Gains Tax · proprietăți din UK",
         h1="Ai vândut o casă care nu era casa ta? Ai <em>60 de zile</em>.",
         say="60 de zile de la ziua în care s-a încheiat vânzarea, nu de la semnarea contractului. În cele 60 de zile declari ȘI plătești."),
    dict(type="step", step="E o declarație separată", fig="60",
         say="Nu e Self Assessment. Se depune într-un cont separat la HMRC, pentru proprietăți. Dacă oricum depui Self Assessment, vânzarea se trece și acolo.",
         note="Se plătește 18% sau 24% din câștig, după banda în care intră. Primii £3.000 de câștig din tot anul nu se impozitează."),
    dict(type="step", step="Cine NU declară în 60 de zile", fig="0",
         say="Casa în care ai locuit tot timpul cât a fost a ta, dacă era singura ta casă: de regulă nu plătești și nu declari nimic. Și dacă nu iese taxă de plătit, declarația nu e cerută.",
         note="Asta e regula pentru rezidenții fiscali din UK. Dacă nu ești rezident fiscal aici, regulile sunt altele — vezi gov.uk/report-and-pay-your-capital-gains-tax. Acțiunile și spațiile comerciale merg în Self Assessment."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Capital Gains Tax · proprietăți din UK",
    h1="Vinzi și nu știi <em>dacă</em> ai de plătit?",
    say="Scrie-ne înainte să se încheie vânzarea — 60 de zile trec repede. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Capital Gains Tax · UK property",
         h1="Sold a property that was not your home? You have <em>60 days</em>.",
         say="60 days from the day the sale completed, not from exchange of contracts. Inside those 60 days you report AND pay."),
    dict(type="step", step="It is a separate return", fig="60",
         say="It is not the Self Assessment return. It goes through a separate HMRC account for property. If you file Self Assessment anyway, the sale goes on that as well.",
         note="The rate is 18% or 24% of the gain, depending on which band it falls in. The first £3,000 of gains in the whole year is not taxed."),
    dict(type="step", step="Who does NOT report in 60 days", fig="0",
         say="Your only home, lived in the whole time you owned it: usually nothing to pay and nothing to report. And where no tax is due, no return is needed.",
         note="That is the rule for UK tax residents. If you are not one, the rules are different — see gov.uk/report-and-pay-your-capital-gains-tax. Shares and commercial property go on the Self Assessment return."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Capital Gains Tax · UK property",
    h1="Selling, and unsure <em>whether</em> there is tax?",
    say="Message us before the sale completes — 60 days goes quickly. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("The 60 days, and that it runs from completion, verbatim: \"You must report and pay any Capital Gains Tax due on "
     "UK residential property within 60 days of completing the sale of the property\", with the table row \"If you sold "
     "a residential property in the UK with a completion date on or after 27 October 2021 | Within 60 days\". The same "
     "page: \"If you're already registered for Self Assessment, you'll also need to include details of the sale in "
     "your Self Assessment tax return\"; \"Use a Capital Gains Tax on UK property account to: report and pay any tax "
     "due on UK property\"; \"You need to sign in to report and pay online. If you do not already have sign in "
     "details, you'll be able to create them when you sign in for the first time\"; and the paper route, \"You'll need "
     "to complete an online form then print and send it to HMRC\"",
     "https://www.gov.uk/report-and-pay-your-capital-gains-tax/if-you-sold-a-property-in-the-uk-on-or-after-6-april-2020",
     "2026-11-08"),
    ("Statute for the deadline and the payment date: the return \"must [be delivered] to an officer of Revenue and "
     "Customs on or before the [60th] day following the day of the completion of the disposal\" (FA 2019 Sch 2 para "
     "3(1)(b), as substituted by FA 2022 s.23(2)) and \"The amount is payable on the filing date for the return\" "
     "(para 6(3)). Para 4(1) is the authority for no return where there is no liability, and para 1(2)(a) excludes "
     "no gain/no loss disposals, which is what takes a transfer to a spouse or civil partner outside the regime. "
     "Extent U.K.",
     "https://www.legislation.gov.uk/ukpga/2019/1/schedule/2", "2026-11-08"),
    ("No tax, no return — HMRC's own manual, verbatim: \"There is no need to report any disposal where there is no CGT "
     "liability (although users can report such disposals voluntarily). There may be no liability for example if: "
     "Private Residence Relief applies in full...; The gain is covered by the Annual Exemption...; The gain is covered "
     "by brought forward losses or current year losses realised prior to completion of the disposal...; A CGT Relief "
     "applies which reduces the full gain to nil\". The same page notes the opposite rule for non-UK residents: "
     "\"Non-UK residents must report all disposals of UK property to HMRC, even if there is no tax to pay or have made "
     "a loss\"",
     "https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg-app18-110", "2026-11-08"),
    ("The rates and the allowance for 2026/27, verbatim: \"6 April 2026 onwards — The following Capital Gains Tax rates "
     "apply: 18% and 24% for individuals; 24% for trustees; 24% for personal representatives of someone who has died; "
     "18% for gains qualifying for Business Asset Disposal Relief or Investors' Relief\", and \"2026 to 2027 | £3,000 "
     "| £1,500\" for the annual exempt amount. Important for anyone recycling older copy: since 30 October 2024 there "
     "is no separate residential property rate — 18%/28% and the old 10%/20% split for other assets are both gone",
     "https://www.gov.uk/guidance/capital-gains-tax-rates-and-allowances", "2026-11-08"),
    ("The band test and the allowance in plain words: \"If this amount is within the basic Income Tax band, you'll pay "
     "18% on your gains made from 6 April 2026... For any amount above the basic Income Tax band, you'll pay 24% on "
     "gains made from 6 April 2026\", and \"For the 2026 to 2027 tax year the allowance is £3,000\". Also \"You only "
     "pay Capital Gains Tax if your overall gains for the tax year (after deducting any losses and applying any "
     "reliefs) are above the annual exempt amount\"",
     "https://www.gov.uk/capital-gains-tax/rates", "2026-11-08"),
    ("Private Residence Relief, and why the card says \"usually\" and points at the full conditions rather than "
     "promising the relief. gov.uk: \"You do not pay Capital Gains Tax when you sell (or 'dispose of') your home if "
     "all of the following apply: you have one home and you've lived in it as your main home for all the time you've "
     "owned it; you have not let part of it out - this does not include having a lodger; you have not used a part of "
     "your home exclusively for business purposes...; the grounds, including all buildings, are less than 5,000 square "
     "metres...; you did not buy it just to make a gain.\" And: \"If all these apply you will automatically get a tax "
     "relief called Private Residence Relief and will have no tax to pay. If any of them apply, you may have some tax "
     "to pay\"",
     "https://www.gov.uk/tax-sell-home", "2026-11-08"),
    ("The final nine months, from HMRC's helpsheet HS283: \"The final 9 months of your period of ownership always "
     "qualify for relief, regardless of how you use the property in that time, as long as the dwelling house has been "
     "your only or main residence at some point\", with 36 months for a disabled person or a care home resident",
     "https://www.gov.uk/government/publications/private-residence-relief-hs283-self-assessment-helpsheet/hs283-private-residence-relief-2026",
     "2026-11-08"),
    ("What is outside the 60-day rule, verbatim: \"If your capital gain is not from a UK residential property, you can "
     "report your gain: in a Self Assessment tax return; using the 'real time' Capital Gains Tax service\" and \"You "
     "must report by 31 December in the tax year after you made your gain and pay by 31 January. For example, if you "
     "made a gain in the 2025 to 2026 tax year, you need to report it by 31 December 2026 and pay by 31 January 2027\"",
     "https://www.gov.uk/report-and-pay-your-capital-gains-tax/if-you-have-other-capital-gains-to-report", "2026-11-08"),
    ("Spouses and civil partners: \"You do not pay Capital Gains Tax on assets you give or sell to your husband, wife "
     "or civil partner, unless: you separated and did not live together at all in that tax year; you gave them goods "
     "for their business to sell on\", and \"Married couples and civil partners can only count one property as their "
     "main home at any one time\"",
     "https://www.gov.uk/capital-gains-tax/gifts", "2026-11-08"),
    ("Penalties and interest for a missed 60-day return. There is no CGT-property-specific penalty table on gov.uk, so "
     "the figures come from statute: FA 2009 Sch 55 applies paras 3 to 6 to \"a return under Schedule 2 to FA 2019\" "
     "(Table item 2A), giving £100 immediately, then the greater of 5% of the tax and £300 at six months and again at "
     "twelve. HMRC's factsheet CC/FS18a states the same amounts in plain words for Income Tax, CGT and ATED returns. "
     "Late-paid tax carries interest at base rate plus 4% — 7.75% on publication day, rising to 8.00% on 24 November "
     "2026. Announced at Budget 2026 and not yet an Act: where the disposal is reported on a Self Assessment return "
     "\"late filing penalties stop accruing from that point\", for returns delivered from 28 October 2026",
     "https://www.legislation.gov.uk/ukpga/2009/10/schedule/55", "2026-11-08"),
  ],
  SCOPE=dict(
    nation="UK-wide. Capital Gains Tax is not devolved: FA 2019 Sch 2 carries the U.K. extent marker, HMRC defines a "
           "UK tax resident as resident in \"England, Scotland, Wales and Northern Ireland\", and no gov.uk CGT page "
           "draws a territorial distinction. What IS devolved is a different tax, paid by the BUYER rather than the "
           "seller, and the cards never mention it: Stamp Duty Land Tax in England and Northern Ireland, Land and "
           "Buildings Transaction Tax in Scotland, Land Transaction Tax in Wales. The 18%/24% band test uses the UK "
           "basic rate band in gov.uk's own worked examples; no primary page spells out the position for a Scottish "
           "taxpayer, so nothing is claimed about it.",
    category="Someone who disposes of UK residential property at a gain that is not fully relieved — a second home, a "
             "buy-to-let, an inherited house, a property that was once a home but was let for part of the ownership. "
             "The obligation falls on the seller. Trustees and personal representatives are in scope at 24%. Non-UK "
             "residents are a separate and stricter category and are left to the long captions rather than the cards.",
    excluded="Four exclusions, and the cards carry three of them. (1) Your own home, where Private Residence Relief "
             "applies in full. The card says \"usually\" and points at gov.uk/tax-sell-home deliberately, because full "
             "relief needs every one of gov.uk's conditions: one home, lived in as the main home for all the time it "
             "was owned, no part let out beyond a lodger, no part used exclusively for business, grounds under 5,000 "
             "square metres, and not bought just to make a gain. A card promising \"no tax on your own home\" would be "
             "wrong for anyone who let a floor or ran a business from a dedicated room. Separately, the final nine "
             "months of ownership always qualify, whatever the property was used for then, provided it was the only or "
             "main residence at some point. (2) No tax to pay means no return is required for a UK resident — the gain "
             "falls inside the £3,000 annual exempt amount, or losses or a relief reduce it to nil (CG-APP18-110, FA "
             "2019 Sch 2 para 4(1)). This is the line that stops a reader filing in a panic over a £1,500 gain. (3) "
             "Assets that are not UK homes: shares, commercial premises and land go on the Self Assessment return at "
             "the ordinary deadline, or through the real time service, not in 60 days. (4) A transfer to a husband, "
             "wife or civil partner you live with: no CGT and outside the regime, because it is a no gain/no loss "
             "disposal. What is NOT an exclusion, and is the reverse trap: a non-UK resident must report every "
             "disposal of UK property or land, residential or not, \"even if there is no tax to pay or have made a "
             "loss\" — so the \"no tax, no return\" shortcut is exactly wrong for them. That sits in the long captions "
             "rather than on a card, because it needs the statutory residence test to be useful and the cards are not "
             "the place for it.",
    from_when="Now. The 60-day deadline applies to completions on or after 27 October 2021; the 30-day rule it "
              "replaced is long gone and is still the commonest error in recycled copy. The 18%/24% rates apply from "
              "6 April 2026 and Budget 2026 shows them unchanged for 2027/28, as is the £3,000 allowance. Nothing is "
              "automatic: the return has to be made and the tax paid by the taxpayer, through a separate HMRC "
              "property account, and HMRC's sign-in details have to exist first — which is why the advice is to "
              "start before completion rather than after it.",
  ),
)


# ===================================================================== 4
CHILDCARE_30H = dict(
  slug="cresa-30-ore",
  title="Creșă plătită de stat — 30 de ore pe săptămână în Anglia, de la 9 luni",
  tags_ro="#cresa #copii #anglia #parinticarelucreaza #romaniinuk",
  tags_en="#childcare #workingparents #england #freechildcare #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Creșă și grădiniță · numai Anglia",
         h1="<em>30 de ore</em> de creșă pe săptămână, plătite de stat.",
         say="În Anglia, pentru părinți care lucrează: 30 de ore pe săptămână, 38 de săptămâni pe an, din trimestrul de după ce copilul face 9 luni. Nu vine singur — trebuie cerut."),
    dict(type="step", step="Cât trebuie să câștigi", fig="£203",
         say="Tu și partenerul tău, dacă ai unul, trebuie să vă așteptați fiecare la cel puțin £203,36 pe săptămână, dacă aveți 21 de ani sau peste. Atât iese salariul minim pentru 16 ore.",
         note="Ceri un cod online, îl dai la creșă, și intri din 3 în 3 luni ca să confirmi că încă te încadrezi. Dacă nu te mai încadrezi, locul copilului continuă o perioadă limitată."),
    dict(type="step", step="Cine NU primește", fig="£100.000",
         say="Dacă tu sau partenerul tău vă așteptați la un venit net ajustat peste £100.000 în anul fiscal, nu primiți nici unul. Dacă nu ai partener, contează numai venitul tău.",
         note="Și e numai în Anglia — Scoția, Țara Galilor și Irlanda de Nord au alte scheme. Orele sunt gratuite, dar creșa poate cere bani pe mâncare, scutece sau excursii; nu are voie să le facă obligatorii."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Creșă și grădiniță · numai Anglia",
    h1="Codul se cere pe <em>gov.uk</em>, nu de la contabil.",
    say="Condițiile și cererea sunt pe gov.uk/free-childcare-if-working. Pentru taxe, salarii și dividende, scrie-ne.",
    phone=PHONE, disc="Informații generale, nu consultanță pe ajutoare de stat. Condițiile sunt pe gov.uk."),

  EN=[
    dict(type="hook",
         kicker="Childcare · England only",
         h1="<em>30 hours</em> of childcare a week, paid by the government.",
         say="In England, for working parents: 30 hours a week, 38 weeks a year, from the term after the child turns 9 months. It does not arrive on its own — you have to apply."),
    dict(type="step", step="What you have to earn", fig="£203",
         say="You and your partner, if you have one, must each expect to earn at least £203.36 a week if you are 21 or over. That is the minimum wage for 16 hours a week.",
         note="You apply online for a code, give it to the provider, then sign in every 3 months to reconfirm. If you stop qualifying, the place continues for a limited grace period."),
    dict(type="step", step="Who does NOT get it", fig="£100,000",
         say="If you or your partner expects an adjusted net income over £100,000 this tax year, neither of you gets it. If you have no partner, only your own income is tested.",
         note="And it is England only — Scotland, Wales and Northern Ireland run different schemes. The hours are free, but a provider may charge for meals, nappies or trips; they are not allowed to make those compulsory."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Childcare · England only",
    h1="The code comes from <em>gov.uk</em>, not from an accountant.",
    say="The conditions and the application are at gov.uk/free-childcare-if-working. For tax, payroll and dividends, message us.",
    phone=PHONE, disc="General information, not benefits advice. The conditions are on GOV.UK."),

  SOURCES=[
    ("The entitlement, the earnings test and the disqualifiers, verbatim: \"If your child is aged 9 months to 4 years "
     "old you can get 30 hours per week of free childcare for 38 weeks of the year\"; the minimum income table giving "
     "\"Over 21 years | £2,643.68 | £203.36\" with \"This is the National Minimum Wage or Living Wage for 16 hours a "
     "week on average\" and \"You (and your partner, if you have one) must each expect to earn a certain amount over "
     "the 3 months after you apply\"; \"You will not be eligible if either: your child does not usually live with you; "
     "you or your partner's expected adjusted net income (including any foreign income) is over £100,000 for the "
     "current tax year\"; what does not count towards the minimum — \"dividends; interest; income from investing in "
     "property; pension payments\"; and the non-working-partner exceptions, \"You may still be eligible if your "
     "partner is working, and you are on carer's leave or eligible for any of the following: Incapacity Benefit; "
     "Severe Disablement Allowance; Carer's Allowance; the limited capability for work element of Universal Credit; "
     "the carer's element of Universal Credit; contribution-based Employment and Support Allowance; National Insurance "
     "credits\"",
     "https://www.gov.uk/free-childcare-if-working/check-youre-eligible", "2026-11-08"),
    ("That it is England only and has to be claimed, verbatim: \"Your child must be aged 9 months to 4 years old and "
     "you must live in England. There are: different schemes in Scotland; different schemes in Wales; different "
     "schemes in Northern Ireland\"; \"To apply, you'll need to set up a childcare account. If your application is "
     "approved, you'll get an 11-digit code that proves you're eligible to get free childcare. You'll need to give "
     "this code to your childcare provider\"; \"You must sign in to your childcare account every 3 months to confirm "
     "your details are up to date\"; \"You can apply for 30 hours of free childcare from when your child is 23 weeks "
     "old\"; and on Tax-Free Childcare, \"You cannot get both Tax-Free Childcare and Universal Credit childcare at the "
     "same time\"",
     "https://www.gov.uk/free-childcare-if-working", "2026-11-08"),
    ("The 38 weeks, the stretching and — the line that matters most to a parent paying an invoice — what a provider may "
     "and may not charge, verbatim: \"You can get 30 hours of free childcare per week for 38 weeks of the year\"; \"You "
     "may be able to get free childcare for more than 38 weeks a year if you take fewer hours over more weeks\"; "
     "\"Although the childcare is free, you may be asked to pay for some extras, such as: meals; nappies; any "
     "additional hours on top of the 30 free hours you can get; additional activities, such as trips\"; \"If you do "
     "not want to pay for these extras, your provider should agree to an alternative arrangement\"; \"You can still "
     "get the free childcare if you do not pay for any extra costs\"; and \"If your provider says you must pay for "
     "extras and will not agree to an alternative arrangement, speak to your local council\"",
     "https://www.gov.uk/free-childcare-if-working/what-youll-get", "2026-11-08"),
    ("The statutory backing, which is stronger than the parent-facing wording and is what the \"not allowed to make "
     "them compulsory\" line rests on. DfE statutory guidance effective 1 April 2026: \"The 15 or 30 hours must be "
     "able to be accessed free of charge to parents. There must not be any mandatory charges for parents in relation "
     "to the free hours\" (A1.31); charges for consumables, meals and optional activities are allowed but \"these "
     "charges must be voluntary for the parent\" (A1.32); \"Parents must be able to opt out of paying for chargeable "
     "extras\" (A1.34); providers must offer \"reasonable alternatives that allow parents to access the entitlement "
     "for free\" (A1.35); \"these chargeable extras must not be a condition of accessing a free place\" (A1.36); and "
     "top-up fees, learning materials, business running costs, non-refundable registration fees and deposits, SEND "
     "support costs and \"non-itemised enrichment charges, sustainability charges\" are all prohibited (A1.38). The "
     "same guidance gives the entitlement as \"1,140 hours of free provision over at least 38 weeks\", confirms "
     "children become eligible \"on 1 April, 1 September or 1 January following them attaining the age of 9 months\", "
     "and sets out the grace-period dates in Table A. Read 8 Nov 2026 for three wordings the cards and captions now "
     "rest on: A1.42 says \"Invoices and receipts should be itemised\" — SHOULD, not must, unlike the three "
     "\"must\" rules in A1.31, A1.32, A1.34, A1.35 and A1.36; A1.22 says a local authority \"should continue to "
     "fund a place for the child for a limited grace period\" when a parent no longer meets the criteria on "
     "reconfirmation, with A1.23 running it to the end of the funding block or the following one; and C.6 tells "
     "providers to inform parents \"that a child may be able to continue to take-up their free place for a limited "
     "period known as the grace period\". No gov.uk or HMRC page states that a missed reconfirmation ends the code, "
     "so that claim was dropped rather than softened",
     "https://www.gov.uk/government/publications/early-education-and-childcare--2/early-education-and-childcare-valid-from-1-april-2026",
     "2026-11-08"),
    ("The termly application deadline, verbatim: \"When you would like to use your entitlements from / The deadline to "
     "apply for a code: 1 January → 31 December; 1 April → 31 March; 1 September → 31 August\" and \"If you do not "
     "apply on or before the deadline, you will not be able to take up your entitlements in that term\". GOV.UK and "
     "Best Start in Life both state the rule by date with no year, so the captions give the rule and name 31 December "
     "2026 only as the application of it for a January 2027 start",
     "https://www.gov.uk/free-childcare-if-working/when-to-apply", "2026-11-08"),
    ("Company directors, which is the part an accountancy practice is actually the right place to ask about: \"You'll "
     "need to show you meet the minimum income requirements if you're a company director. HM Revenue and Customs "
     "(HMRC) will try to check this using your PAYE records. If you do not submit regular PAYE information, you may "
     "have to provide evidence to show you are working and expect to meet the minimum income requirements for the next "
     "3 months. This could be: wage slips; bank statements; a statement from your accountant; copies of invoices\", "
     "and \"You'll need to do this the first time you apply and every time you reconfirm your eligibility\". Read "
     "together with the rule that dividends do not count towards the minimum, this is why a director on a small salary "
     "and large dividends can fail the test",
     "https://www.gov.uk/free-childcare-if-working/apply-for-free-childcare-if-youre-working", "2026-11-08"),
    ("The universal 15 hours that does not depend on working or earnings, for the long captions: \"All 3 to 4-year-olds "
     "in England can get 570 free hours per year. It's usually taken as 15 hours a week for 38 weeks of the year\" and "
     "\"You can get it from the term after your child's 3rd birthday, starting on 1 January, 1 April or 1 September\"",
     "https://www.gov.uk/help-with-childcare-costs/free-childcare-and-education-for-3-to-4-year-olds", "2026-11-08"),
    ("Tax-Free Childcare, the separate scheme that can run alongside: \"For every £8 you pay into the account, the "
     "government will top it up by £2\", \"The total top up you can get for each child is £500 every 3 months (up to "
     "£2,000 a year)\", \"your child must be 11 or younger (16 or younger if they're disabled)\", \"You must sign in "
     "to your childcare account every 3 months to confirm you're still eligible\", and the point that it can pay for "
     "exactly what the funded hours cannot — \"You can also use it to pay for extras such as nappies, meals and "
     "trips, where these are supplied by your childcare provider\"",
     "https://www.gov.uk/tax-free-childcare", "2026-11-08"),
    ("The minimum wage arithmetic behind £203.36: the April 2026 rates are £12.71 for 21 and over, £10.85 for 18 to 20 "
     "and £8.00 for under 18 and apprentices, and 16 x £12.71 = £203.36. April 2027 rates are already published at "
     "£13.21, £11.27 and £8.31, so the figure on this card has a shelf life and should be rebuilt in April",
     "https://www.gov.uk/national-minimum-wage-rates", "2026-11-08"),
    ("Scotland, for the nation comparison: \"Since August 2021, all local authorities have been offering 1,140 hours of "
     "funded ELC to all eligible children\" and \"Scotland is the only part of the UK to offer 1,140 hours a year of "
     "funded ELC to all 3 and 4 year olds and eligible 2 year olds, regardless of their parents' working status\" — "
     "same annual hours as England's working-parent offer, but from age 3 and with no earnings test",
     "https://www.gov.scot/policies/early-education-and-care/early-learning-and-childcare/", "2026-11-08"),
    ("Wales, for the nation comparison: \"Parents and guardians can apply for up to 30 hours of combined government "
     "funded nursery education and childcare a week... 30 hours a week is made up of: at least 10 hours of nursery "
     "education; up to 20 hours of childcare\" and \"You can choose how much of the 30 hours you use for up to 48 "
     "weeks of the year\" — 3 and 4 year olds only, and the Welsh income test is gross income of £100,000 or less, not "
     "adjusted net income",
     "https://www.gov.wales/childcare-3-and-4-year-olds", "2026-11-08"),
    ("Northern Ireland, for the nation comparison: \"The Pre-School Education Programme funds education for children "
     "in the year before they start primary school\" and \"All pre-school places available under the Pre-School "
     "Education Programme are funded by the government. Parents don't pay for these places.\" nidirect publishes no "
     "weekly hours figure, so none is claimed. Separately, \"The Northern Ireland Childcare Subsidy Scheme (NICSS) "
     "aims to reduce the childcare costs of eligible working parents by 15 per cent\", and \"Parents must be claiming "
     "Tax-Free Childcare to receive\" it",
     "https://www.nidirect.gov.uk/articles/pre-school-education-places", "2026-11-08"),
  ],
  SCOPE=dict(
    nation="ENGLAND ONLY, and the cards say so on the first frame and again on card 3. Scotland funds 1,140 hours a "
           "year for all 3 and 4 year olds and eligible 2 year olds \"regardless of their parents' working status\" — "
           "the same annual hours, from a later age, with no earnings test. Wales runs the Childcare Offer for Wales, "
           "up to 30 hours a week over up to 48 weeks for 3 and 4 year olds only, tested on gross income of £100,000 "
           "or less rather than adjusted net income. Northern Ireland has no 30-hours working-parent offer at all: "
           "funded pre-school in the year before primary school, plus a 15% subsidy on top of Tax-Free Childcare for "
           "which \"Universal Credit claimants are not eligible\". No weekly hours figure is published for Northern "
           "Ireland and none is claimed. Tax-Free Childcare, by contrast, is UK-wide.",
    category="A working parent in England of a child aged 9 months to 4 years, where each parent in the household "
             "expects to earn at least the equivalent of 16 hours a week at the minimum wage for their age over the "
             "next three months (£203.36 a week, £2,643.68 a quarter, at 21 and over) and neither expects an adjusted "
             "net income over £100,000. Employment is read broadly: in work or starting a job, on sick or annual "
             "leave, on parental, maternity, paternity or adoption leave. Company directors are in scope but have to "
             "evidence the minimum where PAYE records do not show it.",
    excluded="Four exclusions, three of them on card 3 and the fourth in its note. (1) Everyone outside England. (2) A "
             "household where the APPLICANT OR THEIR PARTNER expects adjusted net income over £100,000. gov.uk tests "
             "\"you (and your partner, if you have one)\" and not both biological parents, so both of those two must "
             "be above the minimum and both below the cap, and a partner at £101,000 ends the claim however little the "
             "applicant earns. A parent with no partner is tested on their own income alone and a former partner's "
             "income is irrelevant. (3) A family where one parent does not work, unless the "
             "working partner's claim is saved by one of gov.uk's listed grounds (carer's leave, Carer's Allowance, "
             "Incapacity Benefit, Severe Disablement Allowance, the limited capability for work or carer's element of "
             "Universal Credit, contribution-based ESA, National Insurance credits). (4) Anyone who has not applied, "
             "or who has stopped reconfirming: there is no automatic entitlement here at all — a code has to be "
             "applied for, handed to the provider and reconfirmed every three months, and gov.uk warns \"If you do not "
             "apply on or before the deadline, you will not be able to take up your entitlements in that term\". Two "
             "more that are not exclusions from the scheme but are the commonest disappointment, and the reason card "
             "3's note exists: the funded hours do not cover the whole bill — a provider may charge for meals, "
             "nappies, consumables, trips and extra hours, but DfE's statutory guidance says those charges \"must be "
             "voluntary\", \"must not be a condition of accessing a free place\", should be itemised (A1.42), and "
             "the provider must offer a free alternative such as letting the parent bring their own; and the hours "
             "cannot be used for a nanny, a home carer or a grandparent. Dividends, interest, property income and "
             "pension payments do not count towards the minimum earnings, which is what catches an owner-managed "
             "company director on a small salary. Finally, a family that fails the working-parent test still keeps the "
             "universal 15 hours for a 3 or 4 year old in England, from the term after the third birthday.",
    from_when="Now. The 30 hours from 9 months has been live since 1 September 2025 and the expansion is complete — "
              "there is no further step in 2026, and DfE's current guidance table has a single row. The earnings "
              "figures changed on 1 April 2026 with the minimum wage and change again on 1 April 2027, so this "
              "carousel is dated. It is claimed, never automatic, and the termly deadline is 31 December for a 1 "
              "January start, 31 March for 1 April and 31 August for 1 September. Nothing here touches residence or "
              "status, which is outside what this firm may advise on and is deliberately absent from every card and "
              "caption.",
  ),
)


# ===================================================================== 5
HELP_TO_SAVE = dict(
  slug="help-to-save-50",
  title="Help to Save — pui £50, statul adaugă £25",
  tags_ro="#helptosave #economii #universalcredit #bonus #romaniinuk",
  tags_en="#helptosave #savings #universalcredit #bonus #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Economii · Help to Save",
         h1="Pui £50 pe lună, statul adaugă <em>£25</em>.",
         say="Contul se numește Help to Save. Statul pune 50% peste cât ai strâns, în două plăți — nu lunar. În patru ani, maxim £2.400 puși de tine și până la £1.200 bonus."),
    dict(type="step", step="Bonusul nu vine lunar", fig="50%",
         say="Vine de două ori: o dată după 2 ani, o dată după 4. Primul bonus e 50% din cel mai mare sold pe care l-ai avut în primii doi ani.",
         note="Al doilea e 50% din cât ai urcat peste acel sold în anii 3 și 4. Banii intră în contul tău bancar, nu în contul de economii, și nu se impozitează."),
    dict(type="step", step="Cine NU poate deschide", fig="<cur>£</cur>0",
         say="Fără Universal Credit, nu se poate. Și nici cu Universal Credit, dar £0 câștigați în ultima lună de calcul — îți trebuie minim £1 în mână.",
         note="Nici dacă nu locuiești în Marea Britanie — excepție: funcționarii Crown și militarii britanici, cu soții sau partenerii lor civili. Și nici dacă ai avut deja un cont: unul pe persoană, o singură dată în viață."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Economii · Help to Save",
    h1="Contul se deschide pe <em>gov.uk</em>, în câteva minute.",
    say="Condițiile și cererea sunt pe gov.uk/get-help-savings-low-income. Pentru taxe și contabilitate, scrie-ne.",
    phone=PHONE, disc="Informații generale, nu consultanță pe ajutoare de stat. Condițiile sunt pe gov.uk."),

  EN=[
    dict(type="hook",
         kicker="Savings · Help to Save",
         h1="Put in £50 a month, the government adds <em>£25</em>.",
         say="The account is called Help to Save and the government adds 50% of what you build up, in two payments — not monthly. Over four years: £2,400 in at most, and up to £1,200 of bonus."),
    dict(type="step", step="The bonus is not monthly", fig="50%",
         say="It comes twice: once after 2 years, once after 4. The first bonus is 50% of the highest balance you reached in the first two years.",
         note="The second is 50% of however much you push that highest balance up in years 3 and 4. It is paid into your bank account rather than the savings account, and it is tax free."),
    dict(type="step", step="Who cannot open one", fig="<cur>£</cur>0",
         say="No Universal Credit, no account. Nor with Universal Credit but £0 of take-home pay in your last assessment period — £1 or more is the test.",
         note="Nor if you are not living in the UK — exception: Crown servants and members of the British armed forces, with their spouses or civil partners. Nor if you have already had an account: one per person, once ever."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Savings · Help to Save",
    h1="The account opens on <em>gov.uk</em>, in a few minutes.",
    say="The conditions and the application are at gov.uk/get-help-savings-low-income. For tax and accounts, message us.",
    phone=PHONE, disc="General information, not benefits advice. The conditions are on GOV.UK."),

  SOURCES=[
    ("The mechanics and the caps, verbatim: \"You can save between £1 and £50 each calendar month. You do not have to "
     "pay money in every month\"; \"For example, if you have saved £50 by 8 January you will not be able to pay in "
     "again until 1 February\"; \"You can only withdraw money from your Help to Save account to your bank account\"; "
     "\"Your Help to Save account will close 4 years after you open it. You will not be able to reopen it or open "
     "another Help to Save account\"; \"You can close your account at any time. If you close your account early you'll "
     "miss your next bonus and you will not be able to open another one\"; \"You can pay money into your Help to Save "
     "account by debit card, standing order or bank transfer\"; and on means-tested benefits, \"If you or your partner "
     "have £6,000 or less in personal savings this will not affect how much Universal Credit you get. This includes "
     "any savings in your Help to Save account\" and \"Your Help to Save bonuses will not affect your Universal Credit "
     "payments\", with the same two sentences repeated for Housing Benefit",
     "https://www.gov.uk/get-help-savings-low-income", "2026-11-08"),
    ("The two bonuses and the totals, verbatim: \"You can earn 2 tax-free bonuses over 4 years. You'll get any bonuses "
     "you've earned even if you withdraw money\"; \"After your first 2 years, you'll get a first bonus if you've been "
     "using your account to save. This bonus will be 50% of the highest balance you've saved\"; \"After 4 years, "
     "you'll get a final bonus if you continue to save. This bonus will be 50% of the difference between 2 amounts: "
     "the highest balance saved in the first 2 years (years 1 and 2); the highest balance saved in the last 2 years "
     "(years 3 and 4)\"; \"If your highest balance does not increase, you will not earn a final bonus\"; \"The most "
     "you can pay into your account each calendar month is £50, which is £2,400 over 4 years. The most you can earn "
     "from your savings in 4 years is £1,200 in bonus money\"; \"Your bonus is paid into your bank account, not your "
     "Help to Save account\"; and the warning the card's note is built on, \"If you withdraw money it will be harder "
     "for you to: grow your highest balance; earn the largest possible bonuses. Withdrawing money could mean you are "
     "not able to earn a final bonus - depending on how much you withdraw and when\". GOV.UK's own worked example: "
     "\"You pay in £25 every calendar month for 2 years... Your highest balance will be £600. Your first bonus is "
     "£300, which is 50% of £600. In years 3 and 4 you save an extra £200 to grow your highest balance from £600 to "
     "£800. Your final bonus is £100, which is 50% of £200\"",
     "https://www.gov.uk/get-help-savings-low-income/what-youll-get", "2026-11-08"),
    ("Eligibility as it stands now — and this is the figure an out-of-date writer gets wrong, because the old "
     "16-hours-at-minimum-wage threshold is gone. Verbatim and complete: \"You can open a Help to Save account if "
     "you're receiving Universal Credit and you (with your partner if it's a joint claim) had take-home pay of £1 or "
     "more in your last monthly assessment period\", with \"Your take-home pay is your pay after deductions (such as "
     "tax or National Insurance)\". The page no longer mentions Working Tax Credit or Child Tax Credit at all. Also "
     "\"If you get payments as a couple, you and your partner can apply for your own Help to Save accounts. You need "
     "to apply separately\" and, under \"If you stop claiming benefits\", \"You can keep using your Help to Save "
     "account\". The same page carries the residence condition that every card and both long captions were missing "
     "until 8 November 2026: \"You also need to be living in the UK\", with one published exception — \"If you "
     "live overseas, you can apply for an account if you're either a: Crown servant or their spouse or civil "
     "partner; member of the British armed forces or their spouse or civil partner.\" And it carries no closing "
     "date and no application deadline, which is how we know the scheme is open to new accounts today",
     "https://www.gov.uk/get-help-savings-low-income/eligibility", "2026-11-08"),
    ("The legislation behind the April 2025 widening, which is why the earnings threshold can be stated as £1: the "
     "Help-to-Save Accounts Regulations 2025 (S.I. 2025/327) reg 2(2) substituted reg 3(3)(b) of the 2018 Regulations "
     "to read \"has earned income in the assessment period immediately preceding the first eligibility reference date "
     "equal to or greater than £1\", reg 2(3) deleted the national living wage reference, and the explanatory note "
     "says it is \"amended to remove the reference to the national living wage rate\". The underlying award must not "
     "be a nil award — reg 3(3)(a), \"is in receipt of a current award validly obtained of universal credit (not being "
     "a nil award)\" — and reg 8(2)(b)(i) requires a declaration that \"the applicant has not previously opened a "
     "Help-to-Save account\", which is the one-per-person-for-life rule. The Regulations apply UK-wide, with express "
     "Northern Ireland equivalents built into reg 3(6)",
     "https://www.legislation.gov.uk/uksi/2025/327/made", "2026-11-08"),
    ("HMRC's impact note on the same change, verbatim: \"This measure will extend the eligibility criteria for the "
     "Help to Save scheme to all working individuals in receipt of UC, who earned £1 or more in their previous "
     "assessment period. It will remove the existing earnings threshold for UC claimants, currently set at the "
     "equivalent of 16 hours a week at the National Living Wage\" and \"This measure will have effect from 6 April "
     "2025\". It also names the provider: \"National Savings and Investments (NS&I) bank — the current scheme "
     "provider, which operates Help to Save accounts on behalf of the government\". And the sentence the captions' "
     "April 2027 line rests on, verbatim: \"Help to Save has been extended on its current terms until April "
     "2027\", alongside \"remains an effective savings product beyond the extension period\" and the costings "
     "\"for the extension to 2027 are set out jointly in Table 5.1 of Autumn Budget 2024\"",
     "https://www.gov.uk/government/publications/amendment-to-the-universal-credit-eligibility-criteria-for-help-to-save-accounts/help-to-save-accounts-amendment-to-the-universal-credit-eligibility-criteria",
     "2026-11-08"),
    ("The bonus formula in HMRC's technical manual, and the worked example the withdrawal warning is built on: the "
     "final bonus qualifying balance is \"the highest balance of a Help-to-Save account achieved after the first bonus "
     "period, less the highest balance of the account achieved in the first bonus period (if any)\", and HMRC's own "
     "case: \"Jack's highest account balance achieved at the end of the maturity period was £650. Jack's qualifying "
     "balance achieved at the first bonus period was £300. £650-£300= £350 ... you multiply his qualifying balance of "
     "£350 by 0.50 pence to get £175\"",
     "https://www.gov.uk/hmrc-internal-manuals/help-save-technical/hstm04400", "2026-11-08"),
    ("That the bonus is tax free and how savings are treated for Universal Credit, from HMRC's technical guidance: "
     "\"The Government bonus is tax-free and does not count as savings income for income tax purposes\" and \"The "
     "Help-to-Save bonus does not count as income for means testing purposes but the bonus and any savings "
     "accumulated in the Help-to-Save account will count as capital for the purpose of Universal Credit "
     "means-testing... their savings above £6,000 are considered in establishing their income\". Worth noting for "
     "reassurance: the most the account can hold, £2,400 plus bonuses, cannot by itself breach £6,000",
     "https://www.gov.uk/hmrc-internal-manuals/help-save-technical/hstm06000", "2026-11-08"),
    ("How it is opened, verbatim: \"You'll need to sign in to set up a Help to Save account. If you do not already "
     "have sign in details, you'll be able to create them when you sign in for the first time\"; \"You'll need your "
     "National Insurance number or postcode and 2 of the following: a valid UK passport; a UK photocard driving "
     "licence issued by the DVLA (or DVA in Northern Ireland); ... details from a Self Assessment tax return in the "
     "last 2 years, if you made one; information held on your credit record, if you have one\"; and \"You'll be asked "
     "to provide your UK bank details when you apply\". A Welsh-language version of the whole guide exists, which is "
     "the only national variation found",
     "https://www.gov.uk/get-help-savings-low-income/how-to-apply", "2026-11-08"),
    ("Budget 2026 on what replaces the current scheme, verbatim from item 2.2: \"As announced at Autumn Budget "
     "2026, the reformed Help to Save scheme will be introduced in Spring 2028\"; \"The scheme will be delivered "
     "through a multi-provider model, enabling banks, building societies and credit unions to offer accounts "
     "directly to eligible customers\"; \"Under this model, Help to Save accounts will be available from a wider "
     "range of savings providers, including some with an established high-street presence.\" Read with the April "
     "2027 extension date above, this is the whole published timeline, and the reason the captions name both dates "
     "and claim nothing at all about the months between them",
     "https://www.gov.uk/government/publications/budget-2026-overview-of-tax-legislation-and-rates-ootlar/budget-2026-overview-of-tax-legislation-and-rates-ootlar",
     "2026-11-08"),
  ],
  SCOPE=dict(
    nation="UK-wide. The guide's only residence condition is \"You also need to be living in the UK\", the 2018 "
           "Regulations apply across the UK with express Northern Ireland equivalents written into reg 3(6) and reg 9, "
           "and the identity list accepts a licence issued \"by the DVLA (or DVA in Northern Ireland)\". There is no "
           "separate Scottish, Welsh or Northern Irish scheme and no different figures; the only national variation "
           "found is a Welsh-language version of the same guide.",
    category="Someone receiving Universal Credit — not a nil award — who, with their partner on a joint claim, had "
             "take-home pay of £1 or more in their last monthly assessment period. That is the whole test now. In a "
             "couple each person applies separately for their own account.",
    excluded="Four exclusions, and the cards carry all of them. (1) Anyone not receiving Universal Credit, or "
             "receiving it with no earnings at all in the last assessment period. GOV.UK states eligibility "
             "positively and publishes no \"you cannot get it if\" list, so the exclusion is the inverse of the "
             "condition — which is exactly why it has to be spelled out on a card. Two traps sit here for an "
             "out-of-date reader: the old threshold of 16 hours a week at the National Living Wage was removed on 6 "
             "April 2025 and is now £1, so someone who was turned away before may qualify today; and Working Tax "
             "Credit is no longer a route, because tax credits ended in April 2025 and GOV.UK's eligibility page no "
             "longer mentions them, even though the conditions sit unrepealed in reg 3(2) of S.I. 2018/87. (2) Anyone "
             "who has already had an account: one per person for life, by declaration under reg 8(2)(b)(i), and "
             "closing early means missing the next bonus with no second chance. A couple is not excluded — each "
             "person can hold their own. (3) Anyone not living in the UK. GOV.UK states it plainly — \"You also "
             "need to be living in the UK\" — with one published exception: \"If you live overseas, you can apply "
             "for an account if you're either a: Crown servant or their spouse or civil partner; member of the "
             "British armed forces or their spouse or civil partner.\" That is a plain eligibility fact and is "
             "written as one. It is NOT, and must never be turned into, anything about immigration status, "
             "citizenship, settled or pre-settled status or recourse to public funds: that is regulated advice this "
             "firm is not authorised to give. (4) The withdrawal trap, which is not an exclusion from the scheme "
             "but is where the money is actually lost. GOV.UK's wording is \"You'll get any bonuses you've earned "
             "even if you withdraw money\", and that is as far as any card or caption now goes: HMRC's Help to Save "
             "Technical Manual HSTM04700 provides for recovery where an account is void or a bonus was paid in "
             "error, so \"never clawed back\" was stronger than the source supports and was removed on 8 November "
             "2026. The live trap is arithmetic: the second bonus is 50% of the INCREASE over the highest balance reached in years 1 "
             "and 2, so anyone who withdraws has to rebuild to the old high-water mark before a single penny of "
             "second bonus is earned — and at £50 a month a large withdrawal late in the term is arithmetically "
             "impossible to recover. Two things that are NOT exclusions and are worth saying: losing the Universal "
             "Credit award later does not close the account (\"You can keep using your Help to Save account\"), and "
             "the savings do not endanger Universal Credit or Housing Benefit below £6,000 of personal savings, which "
             "the account alone cannot reach.",
    from_when="Now, for anyone on Universal Credit with £1 of earnings in their last assessment period. The current "
              "eligibility test has applied since 6 April 2025. It is claimed, never automatic: the account is opened "
              "on GOV.UK or in the HMRC app, currently with NS&I as the single provider, and UK bank details are "
              "needed. The scheme IS open to new accounts today, 8 November 2026: the guide and its eligibility page "
              "are live and publish no closing date and no application deadline — checked, because if it were shut "
              "the carousel could not run at all. There is, however, a dated horizon, and the captions now carry it, "
              "because a reader invited to act is entitled to know the window. HMRC publishes it in terms: "
              "\"Help to Save has been extended on its current terms until April 2027\", with the costings "
              "\"for the extension to 2027\" in Table 5.1 of Autumn Budget 2024; and Budget 2026 OOTLAR item 2.2 "
              "says \"the reformed Help to Save scheme will be introduced in Spring 2028\" through \"a "
              "multi-provider model\". Those two sentences are the whole published timeline. Nothing published "
              "covers new-account opening between April 2027 and that launch, so the captions say exactly that — "
              "current terms to April 2027, reformed scheme from Spring 2028, the gap unpublished, so do not leave "
              "it — and they do not claim the scheme closes, because no source says so. The note here used to say a "
              "closing date was deliberately not claimed, on the ground that GOV.UK publishes none. That was true "
              "only of the guide pages: HMRC's own publication carries the April 2027 date, and a reader urged to "
              "open an account about five months before it was not told. Corrected 8 November 2026. "
              "From April 2028 eligibility widens again to Universal Credit claimants receiving the child or caring "
              "element; that is not in force and is not claimed.",
  ),
)


# ===================================================================== 2026-11-10
# Five topics for publication on 10 November 2026. Every figure below was read
# at primary source on 9 November 2026 — gov.uk, HMRC's own manuals, and the
# Civil Aviation Authority for the air passenger rules. Nothing comes from a
# news site, a blog or another firm's page.

CT_9_LUNI = dict(
  slug="corporation-tax-9-luni",
  title="Corporation Tax — firma plătește înainte să depună",
  tags_ro="#corporationtax #firmauk #limitedcompany #contabilitate #romaniinuk",
  tags_en="#corporationtax #limitedcompany #hmrc #ukaccountant #smallbusinessuk",

  RO=[
    dict(type="hook",
         kicker="Corporation Tax · firme limited",
         h1="Firma plătește taxa <em>înainte</em> să depună declarația.",
         say="Banii se dau la 9 luni și o zi după ce se încheie perioada contabilă a firmei. Declarația are termen 12 luni. Cine crede că plătește când depune, plătește cu trei luni întârziere."),
    dict(type="step", step="Plata, după încheierea perioadei", fig="9 <small>luni și o zi</small>",
         say="Plătești Corporation Tax la 9 luni și o zi după ziua în care se încheie perioada contabilă. Declarația o depui până la 12 luni după aceeași zi.",
         note="Dacă firma are profit impozabil peste £1,5 milioane, plata nu se face o dată, ci în rate."),
    dict(type="step", step="Cine NU depune la HMRC", fig="tot depui",
         say="Depui declarația și dacă firma a avut pierdere, și dacă nu are nicio taxă de plătit. Principala excepție e firma «dormant» pentru Corporation Tax: a oprit activitatea și nu are alt venit.",
         note="Dar și atunci depui bilanțul anual și confirmation statement la Companies House, registrul firmelor. «Dormant» la HMRC nu te scutește acolo."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Corporation Tax · firme limited",
    h1="Nu știi <em>când îți expiră termenul</em>?",
    say="Scrie-ne data la care se încheie perioada contabilă și îți spunem cele două termene. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Corporation Tax · limited companies",
         h1="The company pays <em>before</em> it files.",
         say="Corporation Tax is due 9 months and one day after the end of the accounting period. The return is due 12 months after it. Treat the two as one date and the payment is three months late."),
    dict(type="step", step="Payment, after the period ends", fig="9 <small>months and one day</small>",
         say="Pay Corporation Tax 9 months and one day after the day your accounting period ends. File the Company Tax Return within 12 months of that same day.",
         note="Where taxable profits top £1.5 million, the tax is paid in instalments rather than in one go."),
    dict(type="step", step="Who does NOT file with HMRC", fig="you still <small>file</small>",
         say="You still send a return after a loss, and when there is no Corporation Tax to pay. The main exception is a company dormant for Corporation Tax — it stopped trading and has no other income.",
         note="Even then, accounts and a confirmation statement still go to Companies House, the companies registry. Dormant for HMRC is not dormant there."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Corporation Tax · limited companies",
    h1="Not sure <em>when yours falls due</em>?",
    say="Send us your accounting period end date and we will give you both deadlines. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  GBP=[
    dict(type="solo",
         kicker="Corporation Tax · gov.uk",
         h1="The company pays before it files, not with it.",
         rows=[["9 months + 1 day", "to pay the Corporation Tax bill"],
               ["12 months",        "to file the Company Tax Return"],
               ["<cur>£</cur>200",  "penalty one day late, £200 more at 3 months"]],
         ask="Limited company in Luton or Birmingham? Message us and we will check both dates.",
         phone=PHONE, disc="General information, not personal advice."),
  ],

  SOURCES=[
    ("Corporation Tax due 9 months and 1 day after the end of the accounting period; "
     "taxable profits over £1.5 million paid in instalments",
     "https://www.gov.uk/pay-corporation-tax", "2026-11-09"),
    ("Company Tax Return due 12 months after the end of the accounting period; "
     "separate payment deadline of 9 months and one day; a return is still required "
     "where the company makes a loss or has no Corporation Tax to pay",
     "https://www.gov.uk/company-tax-returns", "2026-11-09"),
    ("Late filing penalties: £200 at one day, another £200 at 3 months, HMRC estimate "
     "plus 10% of unpaid tax at 6 months, a further 10% at 12 months",
     "https://www.gov.uk/company-tax-returns/penalties-for-late-filing", "2026-11-09"),
    ("Fixed late filing penalties raised, for returns with a filing date on or after "
     "1 April 2026, from £100 to £200 for a late return and from £200 to £400 for one "
     "more than 3 months late — the £400 being the cumulative total of the two £200 "
     "stages the penalties page lists",
     "https://www.gov.uk/government/publications/corporation-tax-increases-to-late-filing-penalties/increases-to-corporation-tax-late-filing-penalties",
     "2026-11-09"),
    ("Dormant for Corporation Tax: stopped trading and no other income; once told, "
     "no Corporation Tax to pay and no further return unless a further notice to "
     "deliver arrives; HMRC may write to say it is treating the company as dormant",
     "https://www.gov.uk/dormant-company/dormant-for-corporation-tax", "2026-11-09"),
    ("A dormant company must still file annual accounts and a confirmation statement "
     "(previously annual return); HMRC may write to say it is treating the company as "
     "dormant, and the company can also tell HMRC itself",
     "https://www.gov.uk/dormant-company/dormant-for-corporation-tax", "2026-11-09"),
    ("Large company instalments: profits at an annual rate of more than £1.5 million; for "
     "accounting periods beginning on or after 1 April 2023 the £1.5 million and £10 "
     "million thresholds are divided by the number of associated companies; no instalments "
     "where total liability for the period is less than £10,000",
     "https://www.gov.uk/guidance/corporation-tax-paying-in-instalments", "2026-11-09"),
  ],
  SCOPE=dict(
    nation="All of the UK. Corporation Tax is reserved and does not vary by nation.",
    category="Limited companies and other bodies within the charge to Corporation Tax, "
             "whatever their size. The instalment rule applies only above £1.5 million "
             "of taxable profit.",
    excluded="A company that is dormant for Corporation Tax — it has stopped trading "
             "and has no other income — does not pay and does not file, once HMRC has "
             "been told or has said so, and until a further notice to deliver a return "
             "arrives. That exclusion is narrower than it looks: gov.uk says such a "
             "company must still file annual accounts and a confirmation statement, so "
             "dormant for Corporation Tax is not dormant for Companies House. A loss, or "
             "a nil liability, excludes nobody: the return is still due. Companies with "
             "taxable profits at an annual rate over £1.5 million do not use the single "
             "9-months-and-one-day date at all; they pay in instalments — and for periods "
             "beginning on or after 1 April 2023 that £1.5 million is divided by the "
             "number of associated companies including the company itself, so a group of "
             "three is large at £500,000. A company whose total liability for the period "
             "is under £10,000 stays on the normal due date even above the threshold.",
    from_when="Current rules, now. The increased fixed late filing penalties apply to "
              "returns whose filing date is on or after 1 April 2026, so they are the "
              "figures in force for anything filed late today: £200 at one day and a "
              "further £200 at three months, which is the £400 cumulative total the "
              "policy paper quotes. The two are the same penalty described two ways, and "
              "the cards use gov.uk's own per-stage wording.",
  ),
)


# ===================================================================== 2
CINE_DEPUNE = dict(
  slug="cine-depune-declaratia",
  title="Self Assessment — cine trebuie să depună declarație",
  tags_ro="#selfassessment #hmrc #declaratie #contabilitate #romaniinuk",
  tags_en="#selfassessment #hmrc #taxreturn #ukaccountant #sidehustleuk",

  RO=[
    dict(type="hook",
         kicker="Self Assessment · anul fiscal 2025/26",
         h1="Nu toată lumea depune declarație la HMRC.",
         say="Dacă iei doar salariu sau pensie, taxa se oprește de obicei automat prin PAYE, adică direct din plată, și de regulă nu depui nimic. Întrebarea apare când ai luat bani din altă parte."),
    dict(type="step", step="Când TREBUIE să depui", fig="<cur>£</cur>1.000",
         say="Ai lucrat pe cont propriu și ai încasat peste £1.000 — cât ai încasat, nu cât ți-a rămas. Sau ai fost partener într-un business. Sau ai avut Capital Gains Tax de plătit.",
         note="Poate intra și venitul pe care nu ți l-a taxat nimeni: chirii, bacșișuri, dobânzi, dividende, bani din altă țară. GOV.UK spune «poate», nu «trebuie»."),
    dict(type="step", step="Cine NU depune", fig="PAYE",
         say="Dacă singurul venit e salariul sau pensia, taxa se ia direct din plată și nu ai ce depune. Dar e o excepție care prinde multă lume.",
         note="Excepția: taxa pe Child Benefit, dacă unul dintre voi trece de £60.000 venit net ajustat și nu se ia din salariu. Iar dacă HMRC ți-a cerut declarația în scris, o depui oricum."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Self Assessment · anul fiscal 2025/26",
    h1="Nu știi dacă <em>trebuie să depui</em>?",
    say="Scrie-ne ce venituri ai avut în anul fiscal 2025/26 și îți spunem ce ai de verificat. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Self Assessment · 2025/26 tax year",
         h1="Not everyone has to file a tax return.",
         say="If your only income is wages or a pension, the tax usually comes off through PAYE — straight out of your pay — and no return is normally due. The question starts the moment money arrives from somewhere else."),
    dict(type="step", step="When you MUST file", fig="<cur>£</cur>1,000",
         say="You were self-employed as a sole trader and took more than £1,000 — what came in, not what you kept. Or you were a partner in a business. Or you had Capital Gains Tax to pay.",
         note="Untaxed income may bring you in too: rent, tips, savings interest, dividends, money from abroad. GOV.UK says may, not must."),
    dict(type="step", step="Who does NOT file", fig="PAYE",
         say="If your only income is wages or a pension, the tax comes straight out of your pay and no return is normally due. But one exception catches people out.",
         note="The exception: the Child Benefit tax charge, where one of you has adjusted net income over £60,000 and it is not taken from wages. And a notice to file from HMRC is answered whatever you owe."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Self Assessment · 2025/26 tax year",
    h1="Not sure whether <em>you have to file</em>?",
    say="Tell us what came in during the 2025/26 tax year and we will say what to check. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("Who must send a return: sole trader earning more than £1,000 before relief; "
     "partner in a business partnership; Capital Gains Tax to pay; High Income Child "
     "Benefit Charge not paid through PAYE; and the untaxed income list — rent, tips "
     "and commission, savings interest, dividends, foreign income",
     "https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return", "2026-11-09"),
    ("Tax is usually deducted automatically from wages and pensions; people and "
     "businesses with other income must report it in a Self Assessment return; tell "
     "HMRC by 5 October if you need to complete a return for the previous year",
     "https://www.gov.uk/self-assessment-tax-returns", "2026-11-09"),
    ("Most people pay Income Tax through PAYE — the employer or pension provider takes "
     "Income Tax before paying wages or a pension",
     "https://www.gov.uk/income-tax/how-you-pay-income-tax", "2026-11-09"),
    ("High Income Child Benefit Charge: applies where adjusted net income is over "
     "£60,000 for tax years from 2024 to 2025; where both partners are over it, whoever "
     "has the higher income pays; it must go through Self Assessment where a return is "
     "needed for another reason or the payment falls after 31 January following the tax "
     "year, and can otherwise be paid through PAYE",
     "https://www.gov.uk/child-benefit-tax-charge", "2026-11-09"),
  ],
  SCOPE=dict(
    nation="All of the UK. Self Assessment is HMRC-wide with no devolved variation in "
           "who has to file.",
    category="Individuals with income that PAYE has not already taxed — sole traders "
             "over £1,000 of receipts, business partners, people with Capital Gains Tax "
             "to pay, and people with untaxed rent, tips, interest, dividends or foreign "
             "income.",
    excluded="Anyone whose only income is wages or a pension taxed through PAYE: gov.uk "
             "says tax is usually deducted automatically from wages and pensions, so no "
             "return is normally due. The exclusion is not absolute and the cards now say "
             "so: gov.uk's own must-file list includes the High Income Child Benefit "
             "Charge where it is not paid through PAYE, and an off-payroll worker "
             "repaying a student or postgraduate loan — both can apply to someone whose "
             "only income is wages. It also stops the moment HMRC issues a notice to "
             "file, which has to be answered even where nothing is owed, and it does not "
             "remove the separate duty to tell HMRC by 5 October when first registering.",
    from_when="The 2025/26 tax year, 6 April 2025 to 5 April 2026. First-time "
              "registration for that year had to be notified to HMRC by 5 October 2026.",
  ),
)


# ===================================================================== 3
BANI_INAPOI = dict(
  slug="bani-inapoi-p800",
  title="Taxa plătită în plus — scrisoarea P800 și termenul de 4 ani",
  tags_ro="#p800 #hmrc #taxainapoi #paye #romaniinuk",
  tags_en="#p800 #hmrc #taxrefund #paye #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Taxa pe salariu · scrisoarea P800",
         h1="HMRC îți poate datora bani, fără să-ți fi spus încă.",
         say="Când pe salariu s-a oprit prea multă taxă, HMRC trimite o scrisoare de calcul numită P800. Scrisorile pleacă între iunie și martie al anului următor — deci a ta poate să nu fi venit încă."),
    dict(type="step", step="Cum vin banii", fig="5 zile",
         say="Dacă P800 spune că HMRC trimite cecul, vine singur în 14 zile. Dacă poți cere banii online, vin în 5 zile lucrătoare. Dacă tu ceri cecul, până la 6 săptămâni.",
         note="Banii vin de la HMRC, nu prin link. HMRC nu oferă niciodată restituiri de taxă prin rețelele sociale."),
    dict(type="step", step="Cine NU primește P800", fig="4 ani",
         say="Dacă depui Self Assessment nu primești nicio scrisoare P800: banii ți se întorc prin declarație. P800 e pentru salariați și pensionari.",
         note="Ai 4 ani după încheierea anului fiscal ca să ceri taxa plătită în plus. Dacă treci termenul, de regulă nu se mai poate cere."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Taxa pe salariu · scrisoarea P800",
    h1="Crezi că ai plătit <em>prea multă taxă</em>?",
    say="Scrie-ne și îți spunem ce să verifici la HMRC. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="PAYE · the P800 letter",
         h1="HMRC may owe you money and not have told you yet.",
         say="When too much tax has come off your wages, HMRC sends a tax calculation letter — a P800. Those letters go out between June and the following March, so yours may simply not have arrived."),
    dict(type="step", step="How the money arrives", fig="5 days",
         say="If the P800 says HMRC will post a cheque, it comes on its own in 14 days. If you can claim online, 5 working days. If you ask for a cheque yourself, up to 6 weeks.",
         note="The money comes from HMRC, never through a link. HMRC never offers a tax rebate over social media."),
    dict(type="step", step="Who does NOT get a P800", fig="4 years",
         say="If you file Self Assessment you get no P800 at all — your refund is worked out in the return instead. The P800 is for employees and people drawing a pension.",
         note="You have 4 years after the end of the tax year to claim tax you overpaid. Miss that and normally it can no longer be claimed."),
  ],
  CTA_EN=dict(type="cta",
    kicker="PAYE · the P800 letter",
    h1="Think you have <em>overpaid tax</em>?",
    say="Message us and we will tell you what to check with HMRC. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("The P800 tax calculation letter: sent between June and March of the following tax "
     "year, only to people who are employed or getting a pension; Self Assessment "
     "taxpayers get neither a tax calculation letter nor a Simple Assessment letter "
     "because the bill is adjusted automatically",
     "https://www.gov.uk/tax-overpayments-and-underpayments", "2026-11-09"),
    ("Refund timings: online claim paid within 5 working days, a cheque requested online "
     "within 6 weeks, an automatic cheque within 14 days of the date on the letter",
     "https://www.gov.uk/tax-overpayments-and-underpayments/if-youre-due-a-refund", "2026-11-09"),
    ("Overpayment relief time limit: claims must be made within 4 years after the end of "
     "the relevant tax year or accounting period (HMRC Self Assessment Claims manual "
     "SACM12155)",
     "https://www.gov.uk/hmrc-internal-manuals/self-assessment-claims-manual/sacm12155", "2026-11-09"),
    ("Scam signs: an offer of a tax refund, rebate or grant, and HMRC never using social "
     "media to offer a tax rebate or request personal or financial information; suspect "
     "texts forwarded to 60599",
     "https://www.gov.uk/guidance/identify-hmrc-related-scam-phone-calls-emails-and-text-messages",
     "2026-11-09"),
  ],
  SCOPE=dict(
    nation="All of the UK. PAYE and the P800 are HMRC-wide.",
    category="People taxed through PAYE — employees and people drawing a pension — whose "
             "tax came out wrong, typically through a wrong tax code, two overlapping "
             "jobs, a new workplace pension, or Employment and Support Allowance or "
             "Jobseeker's Allowance.",
    excluded="Self Assessment taxpayers get neither a P800 nor a Simple Assessment "
             "letter: their bill is adjusted automatically in the return, so waiting for "
             "a letter that never comes is the mistake. And anyone more than 4 years past "
             "the end of the tax year concerned is normally out of time, however much was "
             "overpaid — SACM12155 keeps narrow consequential and special-relief routes "
             "open, which is why the cards say normally and not never. Separately, a "
             "P800 only arrives where HMRC's records already show the overpayment: "
             "employment expenses, tools and mileage, leaving the UK mid-year, and CIS "
             "deductions all have to be claimed and never come by letter.",
    from_when="P800 letters for a tax year are issued between June and the following "
              "March. The 4-year claim window runs from the end of the tax year, not "
              "from the date of the letter.",
  ),
)


# ===================================================================== 4
PENSIE_LA_JOB = dict(
  slug="pensie-la-job",
  title="Pensia de la job — 3% îi pune angajatorul, nu tu",
  tags_ro="#pensie #workplacepension #drepturiuk #angajat #romaniinuk",
  tags_en="#workplacepension #autoenrolment #employeerights #uk #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Pensia de la locul de muncă · UK",
         h1="În pensia ta pune bani și <em>angajatorul</em>.",
         say="La un job pe salariu intră în pensie 8% din câștigul care se ia în calcul: 3% pune angajatorul și 5% pui tu. Astea sunt minimele legale. Dacă ieși din schemă, partea angajatorului nu se înlocuiește cu nimic."),
    dict(type="step", step="Cine intră automat", fig="<cur>£</cur>10.000",
         say="Angajatorul te înscrie singur, fără să ceri, dacă ai între 22 de ani și vârsta de pensionare de stat, câștigi cel puțin £10.000 pe an și lucrezi de obicei în UK.",
         note="Câștigul care se ia în calcul: în majoritatea schemelor automate, partea de salariu dintre £6.240 și £50.270 pe an, nu tot salariul."),
    dict(type="step", step="Cine NU intră automat", fig="22",
         say="Sub 22 de ani, peste vârsta de pensionare sau sub £10.000 pe an — nu te înscrie nimeni automat. De regulă poți cere tu să intri, iar angajatorul nu te poate refuza.",
         note="Dar sub £6.240 pe an (£520 pe lună) angajatorul nu e obligat să pună bani. Iar un director unic, fără alt angajat, nu are obligația de înscriere."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Pensia de la locul de muncă · UK",
    h1="Nu știi dacă <em>ești înscris</em>?",
    say="Scrie-ne și îți trimitem pagina oficială GOV.UK unde verifici regulile. Fără obligații.",
    phone=PHONE, disc="Informații generale, nu consultanță pe pensii. Condițiile sunt pe gov.uk."),

  EN=[
    dict(type="hook",
         kicker="Workplace pensions · UK",
         h1="Your employer puts money in <em>too</em>.",
         say="In a job on payroll, 8% of your qualifying earnings goes into a pension: 3% from your employer and 5% from you. Those are the legal minimums. Leave the scheme and the employer's share is not replaced."),
    dict(type="step", step="Who is enrolled automatically", fig="<cur>£</cur>10,000",
         say="Your employer has to put you in without being asked if you are aged between 22 and State Pension age, earn at least £10,000 a year, and usually work in the UK.",
         note="Qualifying earnings: in most automatic enrolment schemes, the slice of pay between £6,240 and £50,270 a year — not your whole wage."),
    dict(type="step", step="Who is NOT enrolled automatically", fig="22",
         say="Under 22, over State Pension age, or earning under £10,000 a year, and nobody puts you in. You can usually still ask to join, and your employer cannot refuse.",
         note="But under £6,240 a year (£520 a month) your employer need not contribute. And a sole director with no other staff has no enrolment duty at all."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Workplace pensions · UK",
    h1="Not sure whether <em>you are enrolled</em>?",
    say="Message us and we will send you the official GOV.UK page with the rules. No obligation.",
    phone=PHONE, disc="General information, not pensions advice. The conditions are on gov.uk."),

  SOURCES=[
    ("Automatic enrolment conditions: aged between 22 and State Pension age, earn at "
     "least £10,000 a year, ordinarily work in the UK; the list of cases where an "
     "employer usually does not have to enrol you; you can usually still join and the "
     "employer cannot refuse; no employer contribution required at £520 a month, £120 a "
     "week or £480 over 4 weeks or less",
     "https://www.gov.uk/workplace-pensions/joining-a-workplace-pension", "2026-11-09"),
    ("Minimum total contribution 8% from April 2019, of which the employer pays at least "
     "3%; in most automatic enrolment schemes the percentages apply to earnings between "
     "£6,240 and £50,270 a year before tax",
     "https://www.gov.uk/workplace-pensions/what-you-your-employer-and-the-government-pay",
     "2026-11-09"),
    ("Opting out within a month of being added returns the money already paid in; later "
     "it usually stays in the pension until retirement; re-enrolment every 3 years",
     "https://www.gov.uk/workplace-pensions/if-you-want-to-leave-your-workplace-pension-scheme",
     "2026-11-09"),
    ("Automatic enrolment duties do not apply where the person is not an employer — "
     "including where you are a sole director of an organisation or business with no "
     "other staff. The Pensions Regulator is the regulator for automatic enrolment.",
     "https://www.thepensionsregulator.gov.uk/en/employers/what-if-i-dont-have-any-staff",
     "2026-11-09"),
  ],
  SCOPE=dict(
    nation="All of the UK. The duty applies to workers who ordinarily work in the UK.",
    category="Workers on an employer's payroll aged 22 to State Pension age earning at "
             "least £10,000 a year.",
    excluded="Nobody is automatically enrolled who is under 22, over State Pension age or "
             "earning under £10,000 a year — they can ask to join and the employer cannot "
             "refuse, but at £520 a month or less (£120 a week, £480 over 4 weeks) the "
             "employer need not contribute at all. The Pensions Regulator adds that a "
             "sole director of a business with no other staff has no automatic enrolment "
             "duty at all, which is the small-limited-company case in this audience. "
             "GOV.UK also lists cases where an employer usually does not have to "
             "enrol someone: notice already given or received either way, evidence of "
             "lifetime allowance protection, a pension already taken that the employer "
             "arranged, a one-off payment from a closed scheme, having opted out more than "
             "12 months before the staging date, membership of an EU cross-border scheme, "
             "being in a limited liability partnership, and a director without an "
             "employment contract who employs at least one other person.",
    from_when="Now. The 8% total and 3% employer minimum have applied since April 2019. "
              "Opting out within one month of being added gets back what you paid in; "
              "after that it normally stays in the pension until retirement, and the "
              "employer re-enrols you every 3 years.",
  ),
)


# ===================================================================== 5
COMPENSATIE_ZBOR = dict(
  slug="compensatie-zbor",
  title="Zbor întârziat — între £220 și £520, dar nu automat",
  tags_ro="#zbor #drepturipasageri #compensatie #caa #romaniinuk",
  tags_en="#flightdelay #passengerrights #uk261 #caa #consumerrights",

  RO=[
    dict(type="hook",
         kicker="Drepturile pasagerilor · zboruri UK",
         h1="Ai ajuns cu peste <em>3 ore</em> întârziere? Ți se pot datora bani.",
         say="Suma nu are nicio legătură cu cât ai dat pe bilet: e stabilită prin lege, între £220 și £520 de persoană. Nu se plătește singură — o ceri de la compania aeriană."),
    dict(type="step", step="Cât, după distanță", fig="<cur>£</cur>520",
         say="Sub 1.500 km — £220. Între 1.500 și 3.500 km — £350. Peste 3.500 km suma se împarte după cât de târziu ai ajuns: £260 la 3–4 ore, £520 la peste 4 ore.",
         note="Se numără ora la care ai ajuns la destinație, nu ora la care ar fi trebuit să pleci."),
    dict(type="step", step="Când NU primești bani", fig="3 h",
         say="La 3 ore întârziere sau mai puțin nu se dă compensație. Și nu se dă când compania arată că motivul a fost unul extraordinar: vreme extremă sau grevă la aeroport ori la controlul traficului aerian.",
         note="Orice zbor care pleacă dintr-un aeroport din UK intră, cu orice companie. Spre UK intră zborurile operate de companii din UK sau din UE."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Drepturile pasagerilor · zboruri UK",
    h1="Nu știi <em>dacă zborul tău intră</em>?",
    say="Scrie-ne și îți trimitem pagina oficială a autorității aviatice unde se verifică. Fără obligații.",
    phone=PHONE, disc="Informații generale, nu consultanță juridică. Regulile sunt pe caa.co.uk."),

  EN=[
    dict(type="hook",
         kicker="Air passenger rights · UK flights",
         h1="Landed more than <em>3 hours</em> late? You may be owed money.",
         say="The sum has nothing to do with what you paid for the ticket: it is set by law, between £220 and £520 a person. It is never paid automatically — you claim it from the airline."),
    dict(type="step", step="How much, by distance", fig="<cur>£</cur>520",
         say="Under 1,500km — £220. From 1,500km to 3,500km — £350. Over 3,500km the sum splits by how late you landed: £260 at three to four hours, £520 beyond four.",
         note="What counts is the time you reached your destination airport, not the time you were due to take off."),
    dict(type="step", step="When you get NOTHING", fig="3 h",
         say="Arrive three hours late or less and no compensation is due. Nor is it due where the airline shows the cause was extraordinary: extreme weather, or an airport or air traffic control strike.",
         note="Any flight leaving a UK airport is covered, on any airline. Into the UK, it is flights operated by a UK or EU airline."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Air passenger rights · UK flights",
    h1="Not sure <em>if your flight counts</em>?",
    say="Message us and we will send you the Civil Aviation Authority page where you can check it. No obligation.",
    phone=PHONE, disc="General information, not legal advice. The rules are on caa.co.uk."),

  SOURCES=[
    ("Delay compensation: £220 under 1,500km; £350 between 1,500km and 3,500km; £260 "
     "over 3,500km arriving three to four hours late and £520 arriving more than four "
     "hours late; you must arrive more than three hours late at the destination airport; "
     "amounts are fixed and not linked to the ticket price; compensation is not paid "
     "automatically and is claimed from the airline; no compensation where the airline "
     "considers the delay caused by extraordinary circumstances",
     "https://www.caa.co.uk/air-passengers/travel-problems-and-rights/flight-delays-and-cancellations/delays/",
     "2026-11-09"),
    ("Extraordinary circumstances examples: extreme weather, airport or air traffic "
     "control employee strikes",
     "https://www.caa.co.uk/air-passengers/travel-problems-and-rights/flight-delays-and-cancellations/cancellations/",
     "2026-11-09"),
    ("Which flights UK261 covers, by departure point, arrival point and airline: every "
     "flight departing the UK is inside it on any carrier; EU to UK is inside it on a UK "
     "or Community carrier; third country to UK on a third-country carrier is the row "
     "that is outside it",
     "https://www.caa.co.uk/media/jn3npj1h/uk-261-annex-1.pdf", "2026-11-09"),
    ("Time limit to issue a court claim: the legal limit to issue claims at Court is 6 "
     "years from the date of the incident in England and Wales and 5 years in Scotland; "
     "the CAA will not handle complaints where there is less than a year to take legal "
     "action",
     "https://www.caa.co.uk/air-passengers/travel-problems-and-rights/travel-complaints/how-the-caa-can-help/",
     "2026-11-09"),
  ],
  SCOPE=dict(
    nation="UK-wide. UK261 is the retained UK regulation, enforced by the Civil Aviation "
           "Authority.",
    category="Passengers on a flight UK261 covers: any flight departing a UK airport, and "
             "flights into the UK operated by a UK or EU airline, who reached the "
             "destination airport more than three hours late.",
    excluded="Nothing is due where the arrival was under three hours late, or where the "
             "airline considers the cause extraordinary — extreme weather, or an airport "
             "or air traffic control strike. A flight into the UK from a non-UK country "
             "flown by an airline that is neither UK nor EU is outside UK261 altogether, "
             "so the fixed sums do not exist for it. Two separate bookings self-connected "
             "by the passenger carry no statutory right to care, compensation or onward "
             "transport across the join.",
    from_when="In force now, for flights already taken as well as future ones. It is "
              "never automatic: the claim goes to the airline, and after eight weeks "
              "without a final answer it can be escalated to an ADR scheme or the CAA's "
              "passenger advice and complaints team. There is a deadline on the other "
              "end too: the CAA puts the limit for issuing a court claim at 6 years from "
              "the incident in England and Wales and 5 years in Scotland, and will not "
              "handle a complaint with less than a year of that left.",
  ),
)


DAY = [CT_9_LUNI, CINE_DEPUNE, BANI_INAPOI, PENSIE_LA_JOB, COMPENSATIE_ZBOR]

# CHILD_BENEFIT was drafted for the 6th and held by the scope checker: its card 3
# answers "who does not keep it" with the High Income Child Benefit Charge, while
# the exclusion that actually decides the claim for this audience is the residence
# condition — UK main home, right to reside, and no claim where leave carries a "no
# public funds" condition. Wording that on a card touches the regulated immigration
# boundary, so it is Valentin's call, not a studio improvisation at 20:00.
HELD = [WINTER_FUEL, CHILD_BENEFIT]

# Shipped on an earlier day. Kept so preflight's LOSS check can still see every
# topic that was in the last commit: a topic that leaves DAY has not been lost,
# it has been published.
ARCHIVE = [PAYMENTS_ON_ACCOUNT, MTD_INCOME_TAX, VAT_THRESHOLD, MARRIAGE_ALLOWANCE,
           CIS_20_30, TAX_CODE_30_DEC, TRADING_ALLOWANCE, MIN_WAGE,
           MILEAGE_55P, LTD_DEADLINES, EMPLOYMENT_ALLOWANCE, COLD_WEATHER, RETURN_30_DAYS,
           VOLUNTARY_NI, DIVIDENDS_1075, HOME_WORKING, WARM_HOME_150, HOLIDAY_56,
           SA_PENALTIES, RENT_A_ROOM, CGT_60_DAYS, CHILDCARE_30H, HELP_TO_SAVE]

BY_SLUG = {t["slug"]: t for t in DAY + HELD + ARCHIVE}
