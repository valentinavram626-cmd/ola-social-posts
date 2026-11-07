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
  tags_en="#selfemployed #workingfromhome #hmrc #smallbusinessuk #ukaccountant",

  RO=[
    dict(type="hook",
         kicker="Cheltuieli · Lucrezi de acasă",
         h1="Munca făcută de acasă scade din profit, de la <em>£10</em> pe lună.",
         say="Lucrezi pe cont propriu și faci munca de acasă? Suma fixă ia locul cheltuielilor curente ale casei — curățenie, căldură, lumină, apă la contor."),
    dict(type="step", step="Suma, după orele pe lună", fig="<cur>£</cur>26",
         say="<b>25-50</b> de ore într-o lună → <b>£10</b>. <b>51-100</b> de ore → <b>£18</b>. <b>101</b> de ore sau mai multe → <b>£26</b>.",
         note="Exemplu: 60 de ore pe lună, tot anul → 12 × £18 = £216 scăzuți din profit. Se numără și luna începută, nu doar lunile întregi."),
    dict(type="step", step="Cine NU poate folosi suma fixă", fig="25h",
         say="Nu o pot folosi firmele Ltd, nici o asociere în care intră o firmă. Sub <b>25</b> de ore într-o lună nu iei suma pe luna aceea, dar celelalte luni se iau normal.",
         note="Acoperă doar cheltuielile curente ale casei. Chiria, council tax, asigurarea, reparațiile, telefonul și internetul le ceri separat, cu partea folosită pentru muncă."),
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
         note="Example: 60 hours a month, all year — 12 × £18 = £216 off your profit. A month, or part of a month, carries the full band."),
    dict(type="step", step="Who cannot use the flat rate", fig="25h",
         say="Limited companies cannot use it, nor a partnership with a company as a partner. Under <b>25</b> hours in a month you take nothing for that month, but every other month is unaffected.",
         note="It covers only the home's running costs. Rent, council tax, insurance, repairs, telephone and internet are claimed separately, at the business share."),
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
    excluded="Three groups cannot use this at all, and a fourth condition bites on a month rather than on a claimant. (1) Limited companies cannot use simplified expenses: GOV.UK and BIM75001 bar the entity whose profits are being computed, not a human being by job title — s.94H applies to \"the profits of a trade of a person\", so a director who also carries on a trade in their own name can use the flat rate in that trade, and for use of home in the directorship HMRC routes to the employment rules (BIM47820 sends the reader to EIM32760 onwards). (2) A partnership with a company as a partner is also barred; only partnerships made up solely of individual partners qualify. (3) Anyone claiming the trading allowance: claiming it rules out deducting any other expenses or allowances, which includes this flat rate — and that is exactly the small home-based trader the £10 band speaks to. (4) Not an exclusion: a month with under 25 hours of qualifying work simply produces no applicable amount for that month, and the same trader claims normally in every other month of the period (s.94H(3), each month \"or part of a month\"). The floor is \"25 or more\" hours in the s.94H(4) table and on GOV.UK, so a month of exactly 25 hours qualifies; BIM75010's body text \"only if these hours exceed 25 per month\" contradicts its own table and is not the law. Employees and directors are outside simplified expenses because it is a trading-income rule — and since 6 April 2026 s.360B ITEPA blocks an employee's own deduction for additional household expenses, so what is left for them is an employer homeworking payment under the s.316A exemption, which continues to apply. Two further limits that are easy to misread: the flat rate stands in only for the household running costs listed at BIM47820 (cleaning, heat and light, metered water); rent or mortgage interest, council tax, insurance, general repairs and water rates are still apportioned and still need the evidence, as are telephone and internet. Qualifying work is any work done in the home wholly and exclusively for the trade (s.94H(4A)), including work done there by the trader's own employees, with any hour counted only once (s.94H(4B)) — not only the three \"core business activities\" BIM75010 lists.",
    from_when="These are the current flat rates on GOV.UK, read on 7 November 2026; BIM75001 dates "
              "them \"from April 2013 onwards\" and s.94H(6) lets the Treasury alter them by "
              "regulations, so they are current rather than permanent. They are claimed on the "
              "Self Assessment return, or — for a trader mandated into Making Tax Digital for "
              "Income Tax, the first year of which is 2026/27 — through the quarterly updates "
              "and the final declaration. Nothing is paid out and nothing arrives automatically. "
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
    dict(type="step", step="Cine NU are acest drept", fig="Contract",
         say="Nu eticheta decide, ci contractul: dreptul îl are cine face munca <b>personal</b> pentru cineva care nu e clientul afacerii lui. Testul: gov.uk/employment-status.",
         note="În afara dreptului rămân cei care își poartă chiar afacerea lor, cu clienții lor. „Freelance\" sau „zero hours\" pe hârtie poate însemna tot <b>worker</b>, cu concediu plătit. Statutul nu îl stabilim noi."),
  ],
  CTA_RO=dict(type="cta",
    kicker="Drepturi la muncă · Concediu plătit",
    h1="Faci <em>payroll</em> pentru oamenii tăi?",
    say="Scrie-ne și ne uităm la concediu și la fluturași. Ești angajat și nu ți s-a dat? Acas ajută gratuit.",
    phone=PHONE, disc="Informații generale, nu consiliere juridică. Noi facem payroll."),

  EN=[
    dict(type="hook",
         kicker="Employment rights · Paid holiday",
         h1="Paid holiday is <em>5.6 weeks</em> a year, not a favour.",
         say="Almost everyone who works for someone else is entitled to it. For someone on a 5-day week that is 28 paid days a year."),
    dict(type="step", step="How it works out for you", fig="28",
         say="The law gives <b>weeks</b>, not days. A 5-day week → <b>28</b> days. A 3-day week → at least <b>16.8</b>. On irregular hours it builds in hours, not days: <b>12.07%</b> of what you work.",
         note="Nothing is added above 28 days: a worker on a 6-day week still gets 28. And bank holidays do not have to be given as paid leave — an employer may count them inside the 28."),
    dict(type="step", step="Who does NOT have this right", fig="Contract",
         say="The contract decides, not the label: the right belongs to anyone who works <b>personally</b> for someone who is not a client of their business.",
         note="Outside it: people in business on their own account, with their own clients. \"Freelance\" or \"zero hours\" can still be a <b>worker</b>, with paid holiday. Status test: gov.uk/employment-status"),
  ],
  CTA_EN=dict(type="cta",
    kicker="Employment rights · Paid holiday",
    h1="Running <em>payroll</em> for your people?",
    say="Message us and we will go through the holiday and the payslips. A worker who was not given it? Acas helps free.",
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
    ("The bank holiday count, which is NOT one number for Great Britain. Read off the page's own nation headings for 2026: \"Upcoming bank holidays in England and Wales 2026\" lists 8; \"Upcoming bank holidays in Scotland 2026\" lists 9, because Scotland adds the 2 January substitute (4 January 2026) and St Andrew's Day (30 November 2026) and has no Easter Monday; \"Upcoming bank holidays in Northern Ireland 2026\" lists 10, adding St Patrick's Day and the Battle of the Boyne. So \"8\" is correct for England and Wales only and must not be written as the figure for a post that covers Scotland too",
     "https://www.gov.uk/bank-holidays", "2026-11-07"),
    ("The status test, verbatim: reg 2(1) defines \"worker\" as an individual who has entered into or works under \"(a) a contract of employment; or (b) any other contract, whether express or implied and (if it is express) whether oral or in writing, whereby the individual undertakes to do or perform personally any work or services for another party to the contract whose status is not by virtue of the contract that of a client or customer of any profession or business undertaking carried on by the individual\". The right therefore follows the contract and what the person actually does, not an occupation or a self-description",
     "https://www.legislation.gov.uk/uksi/1998/1833/regulation/2", "2026-11-07"),
    ("The genuine statutory exclusions, which are narrow: reg 18(1) puts outside the Regulations entirely workers covered by the Merchant Shipping (Maritime Labour Convention) (Hours of Work) Regulations 2018 (seafarers), the Fishing Vessels (Working Time: Sea-fishermen) Regulations 2004 and the Merchant Shipping (Working Time: Inland Waterways) Regulations 2003; reg 18(2) disapplies regs 13 and 13A where \"characteristics peculiar to certain specific services such as the armed forces or the police\" conflict with them, for certain civil protection activities, and for workers covered by the Civil Aviation (Working Time) Regulations 2004",
     "https://www.legislation.gov.uk/uksi/1998/1833/regulation/18", "2026-11-07"),
    ("Use-it-or-lose-it and no qualifying period: reg 13(9) says leave \"may only be taken in the leave year in respect of which it is due\" and may not be replaced by a payment in lieu \"except where the worker's employment is terminated\"; reg 13(5) reduces the first leave year in proportion to the part of it remaining when employment begins, and the regulation sets no minimum length of service anywhere",
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
           "accrual or rolled-up holiday pay provisions, NI keeps its own first-year accrual rule, "
           "and NI has 10 bank holidays.",
    category="People classed as workers, which GOV.UK defines broadly: anyone with a contract or "
             "other arrangement, written or unwritten, to do work or services personally for a "
             "reward. That takes in employees, and also casual, freelance-labelled and zero-hours "
             "working. Part-time workers get the same 5.6 weeks, which is fewer days.",
    excluded="Three real exclusions, and the cards name them. (1) People genuinely in business on their own account, whose customer is a client or customer of that business. The right attaches to the CONTRACT and the status test, not to an occupation or a self-description: WTR 1998 reg 2(1) defines a worker as someone who undertakes to do or perform personally any work or services for another party whose status is not that of a client or customer of a business the individual carries on. Registering as self-employed, invoicing and paying your own tax do not remove the right, and gov.uk/employment-status says HMRC may regard someone as self-employed for tax while \"they have a different status in employment law\" and that \"Someone can be both employed and self-employed at the same time.\" The outright statutory exclusions are narrow: WTR reg 18 puts seafarers, sea-fishermen and inland waterways workers outside the Regulations entirely, and disapplies regs 13 and 13A for the armed forces and police, certain civil protection activities and civil aviation workers. Ola is an accountancy practice, not a law firm: no card or caption resolves a reader\'s own status — the test is on gov.uk/employment-status and holiday disputes go to Acas. (2) Nobody gets more than 28 days of STATUTORY leave however many days a week they work — a 6-day week still gets 28, so the 5.6 weeks is capped and \"5.6 weeks of a 6-day week\" is wrong. (3) Bank holidays are not an extra entitlement: GOV.UK says they do not have to be given as paid leave and may be counted inside the 28 days, so a worker who assumes 28 days plus bank holidays can be wrong without the employer breaking anything; 2026 has 8 bank holidays in England and Wales, 9 in Scotland and 10 in Northern Ireland, so \"the 8\" is England-and-Wales only. An employer may always contract for MORE than the statutory 28 days. One more thing that is NOT an exclusion and is the most useful line on the card: a \"freelance\" or \"zero hours\" label does not remove the right — if the person does the work personally for a reward they are a worker and the holiday is theirs, which is exactly where this audience is told otherwise. For the two groups in WTR reg 15F(1) the entitlement is 12.07% of hours actually worked, in leave years beginning on or after 1 April 2024, so it is a different sum rather than no right — an irregular hours worker is one whose paid hours are wholly or mostly variable UNDER THE TERMS OF THEIR CONTRACT, so fixed contractual hours plus variable overtime are NOT irregular hours and keep the ordinary 5.6 weeks / 28 days sum; a part-year worker is required to work only part of the year with unpaid gaps of at least a week, which is where term-time and seasonal staff sit. Two further things no figure shows: reg 13(9) makes statutory leave use-it-or-lose-it within its leave year and bars payment in lieu \"except where the worker\'s employment is terminated\"; and reg 13 imposes no qualifying period at all, with reg 13(5) pro-rating the first leave year, so only EXTRA contractual leave can carry a length-of-service condition.",
    from_when="5.6 weeks and the 28-day cap are the long-standing statutory minimum and apply now. "
              "The 12.07% accrual method and optional rolled-up holiday pay apply to leave years "
              "beginning on or after 1 April 2024. None of it is claimed from the state — it is "
              "taken from the employer, who has to give it."),
)

DAY = [VOLUNTARY_NI, DIVIDENDS_1075, HOME_WORKING, WARM_HOME_150, HOLIDAY_56]

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
           MILEAGE_55P, LTD_DEADLINES, EMPLOYMENT_ALLOWANCE, COLD_WEATHER, RETURN_30_DAYS]

BY_SLUG = {t["slug"]: t for t in DAY + HELD + ARCHIVE}
