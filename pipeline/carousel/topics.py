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
    dict(type="step", step="Cine NU poate folosi suma pe milă", fig="Taxi",
         say="Taxiurile și mașinile de școală cu dublă comandă nu intră deloc în suma pe milă. Nici o mașină din al cărei preț, benzină sau reparații ai scăzut deja din profit.",
         note="E una sau alta, niciodată amândouă. Iar odată folosită pentru o mașină, rămâi cu ea cât timp folosești mașina în afacere."),
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
    dict(type="step", step="Who cannot use the flat rate", fig="Taxi",
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
    ("Cars designed for commercial use are outside simplified expenses altogether — the page says \"except those designed for commercial use\" and gives black cabs, hackney carriages and dual-control driving instructors' cars as its examples",
     "https://www.gov.uk/simpler-income-tax-simplified-expenses/vehicles", "2026-11-06"),
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
    excluded="A car designed for commercial use — a black cab, a hackney carriage, a dual-control driving instructor's car — cannot use simplified expenses at all, which matters because taxi and private-hire driving is common in this audience. Nor can a vehicle on which capital allowances have been claimed, or whose running costs are already in business profits: one method or the other, never both. The miles themselves are also narrower than the hook suggests — \"travel between home and work\" cannot be claimed at all, so a driver going to the same site each day cannot count that journey, and nor can non-business driving or fines. The choice is locked in: once the flat rate is used for a vehicle it must be kept for that vehicle. And the 25p band starts at mile 10,001, so a high-mileage driver does not get 55p on every mile.",
    from_when="55p applies from 6 April 2026, for the 2026/27 tax year and later years; it "
              "was 45p before that. Claimed on the tax return — nothing is paid out automatically."),
)

# ==================================================================== 12
LTD_DEADLINES = dict(
  slug="termene-firma-ltd",
  title="Firmă Ltd — cele trei termene și plata care vine înaintea declarației",
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
  title="Employment Allowance — până la £10.500 din National Insurance-ul firmei",
  tags_ro="#angajatori #payroll #nationalinsurance #contabilitate #romaniinuk",
  tags_en="#employmentallowance #payroll #nationalinsurance #ukaccountant #smallbusinessuk",

  RO=[
    dict(type="hook",
         kicker="Angajatori · Employment Allowance",
         h1="Până la <em>£10.500</em> din National Insurance-ul firmei.",
         say="Firma plătește National Insurance pentru fiecare angajat — o contribuție la stat, peste cât se oprește din salariul lui. Employment Allowance taie din partea firmei. Dar se cere."),
    dict(type="step", step="Cât și cum se cere", fig="<cur>£</cur>10.500",
         say="Se scad până la <b>£10.500</b> din National Insurance-ul plătit de firmă într-un an fiscal. Se cere din programul de salarii, pentru un singur stat de plată — și se cere din nou la fiecare an fiscal.",
         note="Nu se reportează de la un an la altul. Dacă n-ai cerut-o deloc, se poate cere retroactiv până la 4 ani după anul fiscal respectiv."),
    dict(type="step", step="Cine NU poate cere", fig="1 director",
         say="Dacă firma are un singur director și niciun alt angajat pentru care firma plătește National Insurance, nu poate cere. Nici angajatorii care fac jumătate sau mai mult din muncă pentru sectorul public.",
         note="Nici pentru o bonă sau un grădinar angajat în casă — doar dacă persoana e îngrijitor. Iar într-un grup de firme, cere o singură firmă."),
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
         say="A company with a single director and no other employee liable for secondary Class 1 National Insurance cannot claim. Nor can an employer doing half or more of its work in the public sector.",
         note="Nor for personal or household work — a nanny, a gardener — unless they are a care or support worker. In a group, only one company claims."),
  ],
  CTA_EN=dict(type="cta",
    kicker="Employers · Employment Allowance",
    h1="Not sure if <em>your payroll qualifies</em>?",
    say="Tell us how your payroll is set up and we will check it with you. No obligation.",
    phone=PHONE, disc="General information. For your own situation, speak to an accountant."),

  SOURCES=[
    ("Employment Allowance is worth up to £10,500 off the employer's Class 1 National "
     "Insurance; a single-director company cannot claim where that director is the only "
     "employee liable for secondary Class 1 National Insurance; an employer must do less "
     "than half its work in the public sector; no claim for employees under off-payroll "
     "working rules or for personal, household or domestic work such as a nanny or "
     "gardener unless they are a care or support worker; only one company in a group and "
     "only one payroll may claim; and since April 2025 employers with Class 1 liabilities "
     "over £100,000 can apply",
     "https://www.gov.uk/claim-employment-allowance/eligibility", "2026-11-06"),
    ("\"You must claim the Employment Allowance for each new tax year by submitting an Employer Payment Summary\" — a claim is not carried forward from one tax year to the next; and a claim may be made \"up to 4 years after the end of the tax year in which the allowance applies\", so a 2022 to 2023 claim must be made by 5 April 2027",
     "https://www.gov.uk/government/publications/employment-allowance-more-detailed-guidance/claiming-employment-allowance-further-employer-guidance", "2026-11-06"),
  ],
  SCOPE=dict(
    nation="All of the UK — employer Class 1 National Insurance is a UK-wide HMRC charge "
           "with no devolved variation.",
    category="Employers paying employer Class 1 National Insurance who do less than half their work in the public sector, and charities including community amateur sports clubs. The charity position on the public-sector test was not read at primary source for this run, so no card claims anything about charities.",
    excluded="A company with one director and no other employee liable for secondary Class 1 "
             "National Insurance cannot claim at all — that is the single commonest exclusion "
             "for a small limited company. Employers doing half or more of their work in the "
             "public sector cannot claim. No claim can be made for an employee within "
             "off-payroll working rules, or for someone employed for personal, household or "
             "domestic work such as a nanny or gardener, unless that person is a care or "
             "support worker. Within a group of connected companies only one company may "
             "claim, and an employer running several payrolls may claim against only one of "
             "them. A business with no employees at all is outside it entirely.",
    from_when="Claimed through payroll software for EACH tax year separately — never automatic and never carried forward, so an employer who claimed last year and assumed it rolled over loses up to £10,500. A claim never made can be backdated up to 4 years after the end of the tax year concerned. The £100,000 Class 1 liability bar was lifted from April 2025."),
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
         h1="<em>£25</em> pentru fiecare săptămână de ger. Și vin singuri.",
         say="Dacă primești unul dintre câteva ajutoare, îndeplinești condițiile lui și în zona ta e zero grade sau mai jos șapte zile la rând, statul îți pune bani în cont."),
    dict(type="step", step="Pe ce ajutoare se dă", fig="4",
         say="Pension Credit, Universal Credit, Employment and Support Allowance legat de venit, sau Support for Mortgage Interest. Fiecare cu propriile condiții.",
         note="<b>£25</b> pentru fiecare 7 zile la rând cu media la zero grade sau mai jos. Banii vin în 14 zile lucrătoare. Se numără gerul dintre 1 noiembrie 2026 și 31 martie 2027, după codul poștal."),
    dict(type="step", step="Cine NU primește", fig="2 condiții",
         say="Pe Universal Credit nu primești dacă tu sau partenerul tău munciți. Dar nici dacă nu munciți nu e de ajuns: mai trebuie fie o boală care îți limitează capacitatea de muncă, fie un copil sub 5 ani în casă.",
         note="Cu suma pentru un copil cu dizabilitate primești oricum. Iar în Scoția nu există — acolo vine Winter Heating Payment, o dată pe iarnă."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Iarna 2026/27 · Cold Weather Payment",
    h1="Nu știi <em>unde se verifică</em>?",
    say="Scrie-ne și îți trimitem pagina oficială GOV.UK unde se verifică. Fără obligații.",
    phone=PHONE, disc="Informații generale, nu consultanță pe beneficii. Cere sfat de specialitate."),

  EN=[
    dict(type="hook",
         kicker="Winter 2026/27 · Cold Weather Payment",
         h1="<em>£25</em> for every week of freezing weather, paid automatically.",
         say="If you get one of a short list of benefits, meet that benefit's own conditions, and the temperature where you live sits at zero or below for seven days running, money goes into your account."),
    dict(type="step", step="Which benefits it runs on", fig="4",
         say="Pension Credit, Universal Credit, income-related Employment and Support Allowance, or Support for Mortgage Interest. Each with its own further conditions.",
         note="<b>£25</b> per 7 consecutive days at zero or below, recorded or forecast. Paid within 14 working days. Cold spells from 1 November 2026 to 31 March 2027, by postcode."),
    dict(type="step", step="Who does NOT get it", fig="2 tests",
         say="On Universal Credit you do not get it if you or your partner are employed or gainfully self-employed. And not working alone is not enough — you also need limited capability for work, or a child under 5.",
         note="A disabled child amount in the claim and you get it either way. Scotland has none of this — Winter Heating Payment instead."),
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
  ],
  SCOPE=dict(
    nation="England, Wales and Northern Ireland only. NOT Scotland — GOV.UK states plainly "
           "that someone living in Scotland cannot get Cold Weather Payments; the Winter "
           "Heating Payment is paid there instead, annually and regardless of the weather.",
    category="People receiving Pension Credit, income-related Employment and Support "
             "Allowance, Universal Credit or Support for Mortgage Interest, who meet that "
             "benefit's extra conditions, in a postcode area that records or is forecast a "
             "7-day cold spell.",
    excluded="Anyone living in Scotland gets no Cold Weather Payment at all. Anyone who "
             "receives none of the four qualifying benefits gets nothing, however cold it is "
             "and however low their income — it is tied to the benefit, not to the weather "
             "alone. On Universal Credit, a claimant or partner who is employed or gainfully "
             "self-employed is excluded, unless the claim includes a disabled child amount. A "
             "Universal Credit claimant with no limited capability for work, no child under 5 "
             "and no disabled child amount is excluded too. On income-related ESA, someone in "
             "neither the work-related activity nor the support group is excluded unless they "
             "have one of the listed premiums or a child under 5. And a postcode where no "
             "7-day cold spell is recorded or forecast triggers no payment for anybody.",
    from_when="Cold spells between 1 November 2026 and 31 March 2027. Automatic — no claim is "
              "made; payment follows each triggering cold period within 14 working days."),
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
         h1="Ai <em>30 de zile</em> să ceri banii înapoi pe un produs defect.",
         say="Nu e politica magazinului, e legea: Consumer Rights Act 2015. Dacă produsul e defect, nu e cum l-a descris vânzătorul sau nu face ce ar trebui, ceri banii — nu doar o reparație."),
    dict(type="step", step="Cele 30 de zile, exact", fig="30",
         say="Se numără de a doua zi după ce ai primit produsul și a devenit al tău. Dacă ceri reparație sau înlocuire, numărătoarea se oprește cât aștepți și pornește de unde a rămas.",
         note="Banii trebuie dați fără întârziere și în cel mult <b>14 zile</b> de când vânzătorul e de acord că ți se cuvin."),
    dict(type="step", step="Cine NU are cele 30 de zile", fig="privat",
         say="Dacă ai cumpărat de la o persoană fizică, nu de la un magazin sau o firmă, legea asta nu se aplică. Nici dacă vânzătorul ți-a spus de defect înainte să cumperi, sau se vedea când ai verificat produsul.",
         note="La produsele care se strică repede termenul e mai scurt. După 30 de zile mai ai dreptul la reparație sau înlocuire."),
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
         say="The clock starts the day after the goods are yours and delivered. If you ask for a repair or a replacement, the clock stops while you wait and picks up where it left off.",
         note="A refund must be given without undue delay and in any event within <b>14 days</b> of the trader agreeing you are entitled to one."),
    dict(type="step", step="Who does NOT have the 30 days", fig="private",
         say="Buying from a private individual rather than a trader puts you outside this Act. So does a fault the seller pointed out before you bought, or one your own examination ought to have revealed.",
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
     "expected to perish; and the clock stops for the waiting period while a requested "
     "repair or replacement is carried out",
     "https://www.legislation.gov.uk/ukpga/2015/15/section/22", "2026-11-06"),
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
             "consumer and is outside Part 1. A fault the trader specifically drew to the "
             "buyer's attention before the contract, or one the buyer's own examination of "
             "the goods ought to have revealed, is not covered by the quality term. Goods "
             "that can reasonably be expected to perish sooner have a shorter window than 30 "
             "days. And after the 30 days the short-term right to reject is gone — repair or "
             "replacement comes first then, with a price reduction or a final right to reject "
             "only if that fails.",
    from_when="In force since 1 October 2015 for contracts made on or after that date. The 30 "
              "days run from the day after delivery and ownership; the right is exercised by "
              "the buyer, nothing is automatic."),
)

DAY = [MILEAGE_55P, LTD_DEADLINES, EMPLOYMENT_ALLOWANCE, COLD_WEATHER, RETURN_30_DAYS]

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
           CIS_20_30, TAX_CODE_30_DEC, TRADING_ALLOWANCE, MIN_WAGE]

BY_SLUG = {t["slug"]: t for t in DAY + HELD + ARCHIVE}
