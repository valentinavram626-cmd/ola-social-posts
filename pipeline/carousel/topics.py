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
         h1="De ce plătești <em>mai mult</em> decât ai calculat?",
         say="Pe 31 ianuarie nu plătești doar taxa pe 2025/26. Plătești și prima tranșă în avans pentru anul următor."),
    dict(type="step", step="31 ianuarie 2027", fig="50%",
         say="Prima plată în avans: jumătate din taxa datorată anul trecut, pe lângă regularizarea pentru 2025/26.",
         note="Avansul include și Class 4 National Insurance, dacă lucrezi pe cont propriu."),
    dict(type="step", step="31 iulie 2027", fig="50%",
         say="A doua tranșă în avans. Aceeași sumă, șase luni mai târziu.",
         note="Capital Gains Tax și împrumutul studențesc nu intră în avans — doar în regularizare."),
    dict(type="ask", step="Cine NU plătește avans", fig="<cur>£</cur>1.000",
         say="Taxa de anul trecut sub £1.000, sau peste <b>80%</b> reținut la sursă: fără avans.",
         ask="Nu știi dacă ai avans de plătit în ianuarie? Scrie-ne și verificăm cifra.",
         phone=PHONE),
  ],
  CTA_RO=dict(type="cta",
    kicker="Self Assessment · 31 ianuarie 2027",
    h1="Nu ești sigur <em>cât ai de plătit</em>?",
    say="Scrie-ne un mesaj și ne uităm împreună la cifra din ianuarie. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Self Assessment · 31 January 2027",
         h1="Why January costs <em>more</em> than the return says",
         say="31 January is not only the 2025/26 liability. It also carries the first payment on account for the year ahead."),
    dict(type="step", step="31 January 2027", fig="50%",
         say="First payment on account: half of last year's tax, on top of the 2025/26 balancing payment.",
         note="Payments on account include Class 4 National Insurance for the self-employed."),
    dict(type="step", step="31 July 2027", fig="50%",
         say="The second instalment. Same amount, six months later.",
         note="Capital Gains Tax and student loan sit in the balancing payment, not the instalments."),
    dict(type="ask", step="Who is outside it", fig="<cur>£</cur>1,000",
         say="Last year's tax under £1,000, or over <b>80%</b> deducted at source: no instalments.",
         ask="Want the January figure checked before it lands? Send us a message.",
         phone=PHONE),
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
         h1="Din <em>aprilie 2027</em> intri și tu?",
         say="MTD pentru Income Tax se extinde în trepte. Pragul scade an după an, iar anul de referință e mereu în urmă."),
    dict(type="step", step="Deja obligatoriu", fig="<cur>£</cur>50.000",
         say="Dacă venitul din declarația <b>2024/25</b> a depășit £50.000, intri din 6 aprilie 2026 — dacă nu ai o scutire."),
    dict(type="step", step="Din 6 aprilie 2027", fig="<cur>£</cur>30.000",
         say="Se judecă după declarația <b>2025/26</b> — exact cea cu termen 31 ianuarie 2027.",
         note="Din 6 aprilie 2028 pragul coboară la £20.000, după declarația 2026/27."),
    dict(type="ask", step="Ce se numără", fig="Brut",
         say="Independent plus chirii, <b>înainte</b> de cheltuieli. Nu salariul, nu dividendele.",
         ask="Vrei să știi în care treaptă intri? Trimite-ne cifra din ultima declarație.",
         phone=PHONE),
  ],
  CTA_RO=dict(type="cta",
    kicker="Making Tax Digital · Income Tax",
    h1="Nu știi <em>când intri</em>?",
    say="Trimite-ne cifra din ultima declarație și îți spunem din ce dată te privește. Fără obligații.",
    phone=PHONE, disc="Informații generale. Pentru situația ta, vorbește cu un contabil."),

  EN=[
    dict(type="hook",
         kicker="Making Tax Digital · Income Tax",
         h1="Does <em>April 2027</em> pull you in?",
         say="MTD for Income Tax arrives in stages. The threshold falls each year, and the year it is measured against is always behind you."),
    dict(type="step", step="Already mandatory", fig="<cur>£</cur>50,000",
         say="Qualifying income over £50,000 on the <b>2024/25</b> return puts you in from 6 April 2026, unless an exemption applies."),
    dict(type="step", step="From 6 April 2027", fig="<cur>£</cur>30,000",
         say="Tested against the <b>2025/26</b> return — the one due 31 January 2027.",
         note="From 6 April 2028 the threshold drops to £20,000, tested on the 2026/27 return."),
    dict(type="ask", step="What counts", fig="Gross",
         say="Sole trade plus property, <b>before</b> expenses. Not salary, not dividends.",
         ask="Not sure which stage you fall into? Send us the figure from your last return.",
         phone=PHONE),
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
         h1="<em>£200–£300</em> pentru pensionari. Dar nu rămân la toți.",
         say="Plata vine automat, cu o scrisoare în octombrie sau noiembrie. Partea despre care se vorbește puțin e ce se întâmplă după."),
    dict(type="step", step="Cât și pentru cine", fig="<cur>£</cur>200",
         say="Pentru cei născuți la 27 iunie 1960 sau înainte, care locuiesc singuri. <b>£300</b> dacă sunt născuți înainte de 28 septembrie 1946.",
         note="Anglia, Țara Galilor și Irlanda de Nord. Scoția are propria plată: Pension Age Winter Heating Payment."),
    dict(type="step", step="Peste £35.000", fig="<cur>£</cur>35.000",
         say="Dacă venitul tău personal depășește £35.000, HMRC îți ia plata înapoi — prin codul fiscal sau prin Self Assessment.",
         note="Se judecă venitul fiecăruia separat, nu al gospodăriei."),
    dict(type="ask", step="Dacă nu a venit", fig="31.03",
         say="Automat pentru majoritatea. Altfel, trebuie cerută până la 31 martie 2027.",
         ask="Nu știi dacă va trebui dată înapoi? Ne uităm la venitul tău pe anul fiscal.",
         phone=PHONE),
  ],
  CTA_RO=dict(type="cta",
    kicker="Winter Fuel Payment · iarna 2026/27",
    h1="O vei <em>da înapoi</em>?",
    say="Scrie-ne un mesaj și ne uităm la venitul tău pe anul fiscal. Fără obligații.",
    phone=PHONE),

  EN=[
    dict(type="hook",
         kicker="Winter Fuel Payment · winter 2026/27",
         h1="<em>£200–£300</em> for pensioners — but not everyone keeps it",
         say="It arrives automatically, with a letter in October or November. What gets far less attention is what happens afterwards."),
    dict(type="step", step="How much, and who", fig="<cur>£</cur>200",
         say="For those born on or before 27 June 1960 who live alone. <b>£300</b> if born before 28 September 1946.",
         note="England, Wales and Northern Ireland. Scotland has its own: Pension Age Winter Heating Payment."),
    dict(type="step", step="Over £35,000", fig="<cur>£</cur>35,000",
         say="If your own income passes £35,000, HMRC takes the payment back — through your tax code or your Self Assessment return.",
         note="Assessed on each person's income individually, not on the household's."),
    dict(type="ask", step="If it never arrived", fig="31 Mar",
         say="Automatic for most. Otherwise you must claim, by 31 March 2027.",
         ask="Unsure whether you will have to repay it? We will look at your income for the year.",
         phone=PHONE),
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

DAY = [PAYMENTS_ON_ACCOUNT, MTD_INCOME_TAX, VAT_THRESHOLD, MARRIAGE_ALLOWANCE]
HELD = [WINTER_FUEL]   # see reports/2026-11-04-studio.md, "Oprite de verificare"
BY_SLUG = {t["slug"]: t for t in DAY + HELD}
