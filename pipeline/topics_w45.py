# Week 30 Oct - 5 Nov 2026 topics. Facts checked on GOV.UK on 28 Oct 2026 (Budget day).
# Budget 2026 items: OOTLAR + Annex A, Budget 2026 document, LPC press release (all gov.uk, 28 Oct 2026).
# Usage: python3 topics_w45.py  -> writes week_plan.json, week_ro.json, week_en.json
import json
RT = ["#hmrc #romaniinuk #contabilromania", "#selfemployed #romaniinuk #luton #birmingham", "#hmrc #taxe #romaniinuk #contabil"]
BT = "#buget2026 #hmrc #romaniinuk #contabilromania"
ET = ["#UKTax #HMRC", "#UKTax #SmallBusiness"]
EBT = "#Budget2026 #UKTax"
DAYS = ["2026-10-30","2026-10-31","2026-11-01","2026-11-02","2026-11-03","2026-11-04","2026-11-05"]
PLAN = {d: [] for d in DAYS}; EXTRA = {}
T = {}
def t(day, k, ro, en, extra=False):
    assert k not in T, k
    T[k] = dict(ro=ro, en=en)
    if extra: EXTRA[day] = k
    else: PLAN[day].append(k)

D = DAYS[0]  # Fri 30 Oct
t(D,'b26-summary',('Bugetul 2026','28 oct.','Bugetul din 28 octombrie: 3 schimbări de reținut',['Trading allowance: £3.000 din aprilie 2027','Peste 10.000 de mile: 35p pe milă din aprilie 2027','Salariul minim: £13,21 pe oră din aprilie 2027'],
  'Dragilor, Bugetul a fost prezentat pe 28 octombrie. Pentru self-employed și angajați, astea sunt trei schimbări anunțate, toate din aprilie 2027.',BT),
  ('Budget 2026','28 Oct','Budget 2026: three changes to note',['Trading allowance: £3,000 from April 2027','Over 10,000 business miles: 35p a mile from April 2027','National Living Wage: £13.21 an hour from April 2027'],
  'The Budget was delivered on 28 October. For sole traders and employees, three announced changes stand out, all from April 2027.',EBT,
  'Budget 2026: trading allowance to £3,000, 35p a mile over 10,000 miles, and a £13.21 National Living Wage, all from April 2027.'))
t(D,'b26-trading-3000',('Bugetul 2026','£3.000','Trading allowance se triplează: de la £1.000 la £3.000',['Acum: £1.000 pe an pentru venituri mici din activități','Din 6 aprilie 2027: £3.000, anunțat în Buget','Crește și pragul de declarare în Self Assessment'],
  'În Bugetul din 28 octombrie s-a anunțat că trading allowance crește de la £1.000 la £3.000 din aprilie 2027. Pentru veniturile mici de pe lângă job, asta înseamnă mai puțină birocrație.',BT),
  ('Budget 2026','£3,000','Trading allowance triples: £1,000 to £3,000',['Now: £1,000 a year for small trading income','From 6 April 2027: £3,000, announced in the Budget','The Self Assessment reporting threshold rises too'],
  'The Budget announced that the trading allowance rises from £1,000 to £3,000 from April 2027, with the reporting threshold rising too. Less paperwork for small side income.',EBT,
  'Budget 2026: the trading allowance triples from £1,000 to £3,000 from 6 April 2027, and the Self Assessment reporting threshold rises with it.'))
t(D,'b26-mileage-35p',('Bugetul 2026','35p','Mergi mult cu mașina la lucru? Rata pe milă crește',['Primele 10.000 de mile: 55p, rata devine permanentă','Peste 10.000 de mile: de la 25p la 35p','Schimbarea vine din 6 aprilie 2027'],
  'Bugetul face permanentă rata de 55p pe milă pentru primele 10.000 de mile și crește rata de peste 10.000 de mile de la 25p la 35p, din aprilie 2027.',BT),
  ('Budget 2026','35p','High-mileage drivers get a better rate',['First 10,000 miles: 55p, now made permanent','Above 10,000 miles: up from 25p to 35p','The change starts on 6 April 2027'],
  'The Budget makes the 55p rate for the first 10,000 business miles permanent and raises the rate above 10,000 miles from 25p to 35p from April 2027.',EBT,
  'Budget 2026: 55p a mile for the first 10,000 business miles is now permanent, and miles above 10,000 rise from 25p to 35p from April 2027.'))
t(D,'b26-nlw-1321',('Bugetul 2026','£13,21','Salariul minim crește din aprilie 2027',['21 de ani și peste: £13,21 pe oră','18–20 de ani: £11,27 pe oră','16–17 ani și ucenici: £8,31 pe oră'],
  'Guvernul a acceptat noile rate de salariu minim de la 1 aprilie 2027: £13,21 pe oră pentru cei de 21 de ani și peste. Dacă ai angajați, planifică de acum costurile.',BT),
  ('Budget 2026','£13.21','Minimum wage rates from April 2027',['Age 21 and over: £13.21 an hour','Age 18 to 20: £11.27 an hour','Age 16 to 17 and apprentices: £8.31 an hour'],
  'The government accepted the new minimum wage rates from 1 April 2027: £13.21 an hour for workers aged 21 and over. Employers, budget for it now.',EBT,
  'From 1 April 2027: National Living Wage £13.21, 18-20 rate £11.27, 16-17 and apprentice rate £8.31.'))
t(D,'b26-prop-rates',('Bugetul 2026','24%','Ai chirii? Impozitul pe chirii crește din 2027',['Rata de bază: 24% în loc de 20%','Rata superioară 44%, rata adițională 49%','Din 6 aprilie 2027, în Anglia, Țara Galilor și NI'],
  'Bugetul introduce rate separate pentru veniturile din chirii: 24%, 44% și 49%, din aprilie 2027. Dacă ai o casă închiriată, merită să-ți refaci calculele.',BT),
  ('Budget 2026','24%','Landlords: higher tax on rental income from 2027',['Basic rate: 24% instead of 20%','Higher rate 44%, additional rate 49%','From 6 April 2027 in England, Wales and NI'],
  'The Budget sets separate property income rates of 24%, 44% and 49% from April 2027. If you let out a property, it is worth re-running your numbers.',EBT,
  'Budget 2026: property income tax rates rise to 24%, 44% and 49% from 6 April 2027 in England, Wales and Northern Ireland.'))
t(D,'b26-savings-rates',('Bugetul 2026','+2%','Dobânzile din economii, impozitate mai mult din 2027',['Din aprilie 2027: 24%, 44% și 49%','Personal Savings Allowance rămâne £1.000 / £500','Limita ISA rămâne £20.000 pe an'],
  'Din aprilie 2027, dobânzile peste allowance se impozitează cu 2 puncte mai mult. Allowance-ul și limita ISA de £20.000 rămân la fel.',BT),
  ('Budget 2026','+2%','Savings interest taxed more from 2027',['From April 2027: 24%, 44% and 49%','Personal Savings Allowance stays £1,000 / £500','ISA limit stays at £20,000 a year'],
  'From April 2027, savings interest above your allowance is taxed 2 points higher. The allowance and the £20,000 ISA limit stay the same.',EBT,
  'Budget 2026: savings income rates rise to 24%, 44% and 49% from April 2027. The £20,000 ISA limit stays.'))
t(D,'sa-paye-3000',('Self Assessment','30 dec.','Datorezi sub £3.000? Poți plăti prin tax code',['Trebuie să ai deja salariu sau pensie prin PAYE','Declarația online depusă până pe 30 decembrie','Impozitul se reține lunar, nu dintr-odată'],
  'Dacă ai job sau pensie prin PAYE și datorezi sub £3.000, poți plăti impozitul prin tax code. Condiția: declarația online depusă până pe 30 decembrie.',RT[0]),
  ('Self Assessment','30 Dec','Owe under £3,000? Pay through your tax code',['You must already pay tax through PAYE','File your online return by 30 December','The tax is collected monthly, not in one go'],
  'If you are employed or get a pension through PAYE and owe less than £3,000, HMRC can collect it through your tax code if you file online by 30 December.',ET[0],
  'Owe under £3,000 in Self Assessment and already pay PAYE? File online by 30 December and pay it through your tax code.'))
t(D,'winter-fuel',('Pensionari','£300','Winter Fuel Payment vine în noiembrie–decembrie',['Pentru născuții până la 27 iunie 1960','Între £100 și £300, după vârstă și situație','Venit peste £35.000: HMRC recuperează plata'],
  'Winter Fuel Payment pentru iarna 2026–27 se plătește de obicei în noiembrie sau decembrie. Dacă părinții tăi locuiesc aici, spune-le să urmărească scrisoarea.',RT[2]),
  ('Pensioners','£300','Winter Fuel Payment arrives Nov–Dec',['For people born on or before 27 June 1960','Between £100 and £300 depending on circumstances','Income over £35,000: HMRC takes it back'],
  'Winter Fuel Payment for winter 2026 to 2027 is usually paid in November or December. Over £35,000 income, HMRC takes it back.',ET[0],
  'Winter Fuel Payment 2026-27: £100 to £300, mostly paid Nov-Dec, for people born on or before 27 June 1960.'))
t(D,'cold-weather',('Ajutoare','£25','Cold Weather Payment: £25 pentru o săptămână geroasă',['Pentru cei care primesc anumite beneficii','7 zile la rând la 0°C sau mai puțin în zonă','Plata e automată, 1 nov. 2026 – 31 mar. 2027'],
  'Din 1 noiembrie, cine primește anumite beneficii poate primi £25 pentru fiecare 7 zile foarte reci. Nu trebuie să ceri, plata vine automat.',RT[2]),
  ('Benefits','£25','Cold Weather Payment: £25 per cold spell',['For people on certain benefits','7 days in a row at 0°C or below in your area','Paid automatically, 1 Nov 2026 to 31 Mar 2027'],
  'From 1 November, people on certain benefits can get £25 for each 7-day spell of very cold weather. It is paid automatically.',ET[0],
  'Cold Weather Payment: £25 for each 7 days at 0°C or below, 1 Nov 2026 to 31 Mar 2027, paid automatically.'))
t(D,'jan-first-year',('Primul an','150%','Primul an de self-employed? Ianuarie poate fi dublu',['Plătești tot impozitul pe anul trecut','Plus prima plată în avans: jumătate din el','Exemplul HMRC: £3.000 devine £4.500'],
  'În primul an de Self Assessment, pe 31 ianuarie plătești impozitul întreg plus prima plată în avans pentru anul următor. Mulți află abia atunci, da?',RT[1]),
  ('First year','150%','First year self-employed? January can hit twice',['You pay the full tax bill for last year','Plus your first payment on account: half of it','HMRC example: £3,000 becomes £4,500'],
  'In your first Self Assessment year, 31 January brings the full bill plus the first payment on account for the next year. Plan for it.',ET[0],
  'First Self Assessment? A £3,000 bill can mean £4,500 due on 31 January, because the first payment on account is added.'))
t(D,'vat-90k',('TVA','£90.000','Când trebuie să te înregistrezi pentru TVA',['Cifră de afaceri taxabilă peste £90.000','Sau când te aștepți să treci de prag','Verifică lunar ultimele 12 luni, nu anul fiscal'],
  'Pragul de înregistrare pentru TVA este £90.000 cifră de afaceri taxabilă. Verifică lunar ultimele 12 luni, ca să nu treci de prag fără să știi.',RT[1]),
  ('VAT','£90,000','When you must register for VAT',['Taxable turnover over £90,000','Or when you expect to go over','Check the last 12 months every month'],
  'The VAT registration threshold is £90,000 of taxable turnover. Check your last 12 months every month so you do not cross it unnoticed.',ET[1],
  'VAT registration threshold: £90,000 taxable turnover. Check your rolling 12 months every month.'))
t(D,'ola-first-call',('Ola Accountancy','£120','Prima consultație: 30 de minute, £120',['£120 cu TVA inclus','Vorbim românește, în Luton sau Birmingham','Pleci cu pașii clari pentru situația ta'],
  'Nu știi de unde să începi? Prima consultație la Ola durează 30 de minute și costă £120 cu TVA inclus. Pleci acasă cu pașii clari.',RT[0]),
  ('Ola Accountancy','£120','First consultation: 30 minutes, £120',['£120 including VAT','In Luton or Birmingham','You leave with clear next steps'],
  'Not sure where to start? A first consultation at Ola is 30 minutes and costs £120 including VAT. You leave with clear next steps.',ET[1],
  'Ola Accountancy first consultation: 30 minutes, £120 including VAT, in Luton or Birmingham.'))
t(D,'exp-clothes',('Cheltuieli','Haine?','Hainele de lucru se deduc? Doar unele',['Da: bocanci de protecție, cască, salopetă','Da: uniformă care nu e haină de zi cu zi','Nu: costum, cămașă sau pantofi obișnuiți'],
  'Ca self-employed poți deduce hainele de protecție și uniformele, dar nu hainele de zi cu zi, chiar dacă le porți doar la lucru.',RT[1]),
  ('Expenses','Clothing?','Can you claim work clothes? Only some',['Yes: safety boots, hard hats, overalls','Yes: uniforms that are not everyday wear','No: suits, shirts or ordinary shoes'],
  'Self-employed? You can claim protective clothing and uniforms, but not everyday clothing, even if you only wear it for work.',ET[1],
  'Self-employed clothing: protective gear and uniforms yes, everyday clothes no, even if worn only for work.'))
t(D,'marriage-252',('Familie','£252','Marriage Allowance: până la £252 pe an',['Unul câștigă sub £12.570, celălalt rata de bază','Se transferă £1.260 din allowance','Poți cere și pentru anii din urmă, din 2022–23'],
  'Dacă ești căsătorit și unul dintre voi câștigă sub £12.570, puteți reduce impozitul celuilalt cu până la £252 pe an. Se poate cere și retroactiv.',RT[2]),
  ('Family','£252','Marriage Allowance: up to £252 a year',['One earns under £12,570, the other is a basic-rate payer','£1,260 of allowance is transferred','You can backdate claims to 2022 to 2023'],
  'Married or in a civil partnership and one of you earns under £12,570? Marriage Allowance can save up to £252 a year, and you can backdate it.',ET[0],
  'Marriage Allowance: transfer £1,260 of Personal Allowance and save up to £252 a year. Backdate to 2022-23.'))
t(D,'b26-capital-allowances',None,('Budget 2026','50%','Budget 2026: capital allowances change',['First-year allowance rises from 40% to 50% from 1 Jan 2027','Main writing-down allowance falls to 12% from April 2027','Cars and second-hand assets are excluded from the 50%'],
  'Investing in plant or machinery? The Budget raises the main first-year allowance to 50% from January 2027 and cuts the main writing-down allowance to 12%.',EBT,
  'Budget 2026: main first-year allowance up to 50% from 1 Jan 2027; writing-down allowance down to 12% from April 2027.'),extra=True)

D = DAYS[1]  # Sat 31 Oct
t(D,'b26-mtd-points',('Making Tax Digital','0 puncte','MTD: fără puncte de penalizare nici în 2027–28',['Bugetul extinde perioada de toleranță','Pentru actualizările trimestriale din 2027–28','Declarația anuală întârziată rămâne penalizată'],
  'Vești bune pentru MTD: Bugetul anunță că nici în 2027–28 nu se dau puncte de penalizare pentru actualizările trimestriale întârziate. Declarația anuală rămâne cu termen strict.',BT),
  ('Making Tax Digital','0 points','MTD: no penalty points for 2027-28 updates',['The Budget extends the easement','Covers 2027 to 2028 quarterly updates','Late annual returns are still penalised'],
  'Good news on MTD: the Budget says no late submission penalty points for 2027 to 2028 quarterly updates. Annual return deadlines still apply.',EBT,
  'Budget 2026: no MTD late submission penalty points for 2027-28 quarterly updates. Late returns are still penalised.'))
t(D,'b26-energy-100',('Bugetul 2026','£100','£100 pentru facturile la energie din ianuarie 2027',['Anunțat în Bugetul din 28 octombrie','Gospodării din Anglia, council tax banda A–D','Bani plătiți direct în contul bancar'],
  'Bugetul anunță o plată de £100 din ianuarie 2027 pentru gospodăriile din Anglia aflate în benzile A–D de council tax. Banii vin direct în cont.',BT),
  ('Budget 2026','£100','£100 Household Energy Payment from Jan 2027',['Announced in the 28 October Budget','Households in England in council tax bands A to D','Paid straight into bank accounts'],
  'The Budget announced a £100 Household Energy Payment from January 2027 for households in England in council tax bands A to D.',EBT,
  'Budget 2026: £100 Household Energy Payment from January 2027 for council tax bands A-D in England, paid into bank accounts.'))
t(D,'b26-pension-allowance',('Bugetul 2026','0%','Pensionari cu venit mic: fără Income Tax din 2027',['Pentru cei peste vârsta de pensionare','Venit total până la nivelul pensiei de stat complete','Peste acest nivel, beneficiul scade treptat'],
  'Din aprilie 2027, pensionarii al căror venit total nu depășește pensia de stat completă nu vor plăti Income Tax. Peste acest nivel, beneficiul scade treptat.',BT),
  ('Budget 2026','0%','Pension Tax Allowance from April 2027',['For people over State Pension age','Total income up to the full new State Pension','Tapers away above that level'],
  'From April 2027, pensioners whose total income is no more than the full new State Pension will pay no Income Tax. It tapers above that.',EBT,
  'Budget 2026: from April 2027, pensioners with income up to the full new State Pension pay no Income Tax.'))
t(D,'mileage-55p',('Kilometraj','55p','Rata pe milă a crescut deja la 55p',['Din 6 aprilie 2026: 55p pentru primele 10.000 mile','Peste 10.000 de mile: 25p, deocamdată','Pentru self-employed și pentru angajați'],
  'Rata HMRC pentru mașină sau dubă a crescut de la 45p la 55p pe milă, retroactiv din 6 aprilie 2026. Ține evidența drumurilor de business, da?',RT[1]),
  ('Mileage','55p','The mileage rate is now 55p',['From 6 April 2026: 55p for the first 10,000 miles','Above 10,000 miles: 25p for now','Applies to employees and the self-employed'],
  'HMRC raised the car and van rate from 45p to 55p a mile, backdated to 6 April 2026. Keep a proper log of business journeys.',ET[1],
  'Mileage: 55p a mile for the first 10,000 business miles since 6 April 2026, then 25p (35p from April 2027).'))
t(D,'it-bands',('Impozit pe venit','20/40/45','Cât impozit plătești pe venit în 2026–27',['Până la £12.570: 0%','£12.571–£50.270: 20%; până la £125.140: 40%','Peste £125.140: 45% (Scoția are alte rate)'],
  'Ratele de impozit pe venit în 2026–27, pentru Anglia, Țara Galilor și Irlanda de Nord: 0%, 20%, 40% și 45%. Știind banda ta, știi cât să pui deoparte.',RT[0]),
  ('Income Tax','20/40/45','Income Tax bands for 2026-27',['Up to £12,570: 0%','£12,571 to £50,270: 20%; to £125,140: 40%','Over £125,140: 45% (Scotland differs)'],
  'Income Tax for 2026 to 2027 in England, Wales and NI: 0%, 20%, 40% and 45%. Know your band and you know what to set aside.',ET[0],
  'Income Tax 2026-27: 0% to £12,570, 20% to £50,270, 40% to £125,140, 45% above (not Scotland).'))
t(D,'class4-6',('National Insurance','6%','Self-employed: cât National Insurance plătești',['Class 4: 6% pe profitul dintre £12.570 și £50.270','2% pe profitul de peste £50.270','Se plătește odată cu impozitul, prin Self Assessment'],
  'Ca self-employed plătești Class 4 National Insurance: 6% pe profitul dintre £12.570 și £50.270 și 2% peste. Se adaugă la factura de Self Assessment.',RT[1]),
  ('National Insurance','6%','Self-employed National Insurance explained',['Class 4: 6% on profits £12,570 to £50,270','2% on profits above £50,270','Paid with your tax through Self Assessment'],
  'Self-employed? Class 4 NI is 6% on profits between £12,570 and £50,270 and 2% above, paid through Self Assessment.',ET[1],
  'Class 4 NI 2026-27: 6% on profits between £12,570 and £50,270, 2% above. Paid via Self Assessment.'))
t(D,'poa-1000',('Plăți în avans','31 ian.','Plățile în avans: cine le face și când',['Două plăți: 31 ianuarie și 31 iulie','Fiecare: de obicei jumătate din factura de anul trecut','Nu le faci dacă factura a fost sub £1.000'],
  'Plățile în avans sunt două: pe 31 ianuarie și pe 31 iulie, fiecare de obicei jumătate din impozitul de anul trecut. Dacă ai datorat sub £1.000, nu le faci.',RT[0]),
  ('Payments on account','31 Jan','Payments on account: who pays and when',['Two payments: 31 January and 31 July','Each is usually half of last year\'s bill','Not needed if last year\'s bill was under £1,000'],
  'Payments on account are due on 31 January and 31 July, each usually half of last year\'s tax. Owed under £1,000? You do not make them.',ET[0],
  'Payments on account: 31 Jan and 31 Jul, each usually half of last year\'s bill. Not due if it was under £1,000.'))
t(D,'b26-fuel',('Șoferi','5p','Reducerea de 5p la carburant se prelungește',['Reducerea de 5p pe litru rămâne','Până la 30 iunie 2027, anunțat în Buget','Bun de știut pentru cine lucrează pe drum'],
  'Bugetul prelungește reducerea de 5p pe litru la carburant până la 30 iunie 2027. Pentru cei care lucrează pe drum, contează la costuri.',BT),
  ('Drivers','5p','The 5p fuel duty cut is extended',['The 5p per litre cut stays','Until 30 June 2027, announced in the Budget','Useful for anyone who drives for work'],
  'The Budget extends the 5p per litre fuel duty cut until 30 June 2027. Worth knowing if you drive for a living.',EBT,
  'Budget 2026: the 5p fuel duty cut is extended to 30 June 2027.'))
t(D,'vat-points',('TVA','£200','Declarație de TVA întârziată: puncte de penalizare',['Un punct pentru fiecare declarație întârziată','Trimestrial: la 4 puncte vine amenda de £200','Lunar: prag de 5 puncte; anual: 2 puncte'],
  'La TVA, fiecare declarație întârziată aduce un punct. Când ajungi la prag, de exemplu 4 puncte la declarații trimestriale, primești £200 amendă.',RT[1]),
  ('VAT','£200','Late VAT returns earn penalty points',['One point for each late return','Quarterly filers: a £200 penalty at 4 points','Monthly: 5 points; annual: 2 points'],
  'Each late VAT return earns a point. Reach the threshold, 4 points for quarterly filers, and you get a £200 penalty.',ET[1],
  'VAT late submission: one point per late return; £200 penalty at the threshold (4 points quarterly, 5 monthly, 2 annual).'))
t(D,'ola-romana',('Ola Accountancy','RO','Contabil care îți explică totul în românește',['Îți explicăm ce scrisoare ai primit de la HMRC','Îți spunem clar ce ai de plătit și când','Birouri în Luton și Birmingham'],
  'Suntem români și vorbim românește. Îți explicăm pe înțelesul tău ce ai primit de la HMRC și ce ai de făcut, pas cu pas.',RT[0]),
  ('Ola Accountancy','Clear','An accountant who explains it plainly',['We explain what your HMRC letter means','We tell you clearly what to pay and when','Offices in Luton and Birmingham'],
  'We explain HMRC letters in plain language and tell you clearly what to pay and when.',ET[1],
  'Ola Accountancy: plain-language help with HMRC letters, tax bills and deadlines. Luton and Birmingham.'))
t(D,'hicbc-70k',('Child Benefit','£60.000','Câștigi peste £60.000 și iei Child Benefit?',['Returnezi 1% pentru fiecare £200 peste £60.000','La £70.000 returnezi jumătate','La £80.000 sau mai mult returnezi tot'],
  'High Income Child Benefit Charge începe de la £60.000 venit: returnezi 1% pentru fiecare £200 peste prag. La £80.000 returnezi tot.',RT[2]),
  ('Child Benefit','£60,000','Earning over £60,000 with Child Benefit?',['Repay 1% for every £200 over £60,000','At £70,000 you repay half','At £80,000 or more you repay it all'],
  'The High Income Child Benefit Charge starts at £60,000: 1% for every £200 over. At £80,000 you repay it all.',ET[0],
  'HICBC: 1% of Child Benefit per £200 over £60,000. Half at £70,000, all at £80,000.'))
t(D,'exp-phone',('Cheltuieli','%','Telefon și internet: deduci partea de business',['Calculezi procentul folosit pentru afacere','Nu intră în rata fixă pentru lucrul de acasă','Păstrează facturile lunare'],
  'Telefonul și internetul se deduc doar pentru partea folosită în afacere. Atenție: nu sunt incluse în rata fixă pentru lucrul de acasă.',RT[1]),
  ('Expenses','%','Phone and internet: claim the business share',['Work out the business-use percentage','Not covered by the working-from-home flat rate','Keep your monthly bills'],
  'You can claim the business share of phone and internet bills. They are not covered by the working-from-home flat rate.',ET[1],
  'Phone and internet: claim the business share. The home-working flat rate does not cover them.'))
t(D,'records-5y',('Evidențe','5 ani','Cât timp păstrezi actele pentru HMRC',['Minimum 5 ani după termenul de 31 ianuarie','Pentru 2025–26: cel puțin până în ianuarie 2032','Bonuri, facturi și extrase de cont'],
  'Ca self-employed păstrezi actele cel puțin 5 ani după termenul de 31 ianuarie. Pentru anul 2025–26, asta înseamnă cel puțin până la finalul lui ianuarie 2032.',RT[1]),
  ('Records','5 years','How long to keep your records',['At least 5 years after the 31 January deadline','For 2025-26: until at least end of January 2032','Receipts, invoices and bank statements'],
  'Self-employed? Keep records for at least 5 years after the 31 January deadline. For 2025 to 2026, that is until at least the end of January 2032.',ET[1],
  'Keep self-employed records at least 5 years after the 31 January deadline: 2025-26 records until at least end of January 2032.'))
t(D,'ola-docs-wa',('Ola Accountancy','Acte','Trimite-ne actele direct pe WhatsApp',['Fotografiază clar bonurile și facturile','Extrasele de cont le trimiți în PDF','Îți confirmăm ce mai lipsește'],
  'Nu trebuie să vii cu dosarul la birou. Trimite-ne actele pe WhatsApp, iar noi îți spunem ce mai lipsește.',RT[0]),
  ('Ola Accountancy','Docs','Send us your documents on WhatsApp',['Take clear photos of receipts and invoices','Send bank statements as PDFs','We confirm what is still missing'],
  'No need to bring a folder to the office. Send your documents on WhatsApp and we tell you what is still missing.',ET[1],
  'Send your tax documents to Ola Accountancy on WhatsApp and we confirm what is missing.'))
t(D,'b26-payroll-bik',None,('Budget 2026','Apr 2027','Payrolling benefits becomes mandatory',['Company cars, vans and fuel from 6 April 2027','Medical benefits from the same date','Most other benefits from April 2028'],
  'Employers: payrolling benefits in kind becomes mandatory from April 2027 for cars, vans, fuel and medical benefits, and for most others from April 2028.',EBT,
  'Budget 2026: mandatory payrolling of benefits for cars, vans, fuel and medical from 6 April 2027; most others from April 2028.'),extra=True)

D = DAYS[2]  # Sun 1 Nov
t(D,'b26-nic-freeze',('Bugetul 2026','2031','Pragurile de National Insurance rămân înghețate',['Majoritatea pragurilor, la nivelul 2026–27','Înghețate până în 2030–31','Class 3 voluntar: £19,05 pe săptămână din 2027'],
  'Bugetul confirmă că majoritatea pragurilor de National Insurance rămân înghețate până în 2030–31. Class 3 voluntar devine £19,05 pe săptămână din aprilie 2027.',BT),
  ('Budget 2026','2031','NI thresholds stay frozen',['Most limits stay at 2026-27 levels','Frozen until 2030 to 2031','Voluntary Class 3: £19.05 a week from April 2027'],
  'The Budget keeps most National Insurance thresholds frozen until 2030 to 2031. Voluntary Class 3 rises to £19.05 a week from April 2027.',EBT,
  'Budget 2026: most NI thresholds frozen to 2030-31; voluntary Class 3 £19.05/week from April 2027.'))
t(D,'b26-marketplace-vat',('Bugetul 2026','oct. 2027','Vinzi pe platforme online? Se schimbă TVA-ul',['Din octombrie 2027, anunțat în Buget','Platforma colectează TVA pe vânzări peste £90.000','Vânzările personale nu sunt afectate'],
  'Din octombrie 2027, platformele online vor colecta TVA pentru afacerile din UK care vând prin ele peste £90.000. Vânzările de lucruri personale nu sunt afectate.',BT),
  ('Budget 2026','Oct 2027','Selling on online marketplaces? VAT changes',['From October 2027, announced in the Budget','Platforms collect VAT on sales above £90,000','Personal sales are not affected'],
  'From October 2027, marketplaces must collect VAT on sales by UK businesses that exceed £90,000 through the platform. Personal sales are not affected.',EBT,
  'Budget 2026: from Oct 2027 online marketplaces collect VAT on UK business sales above £90,000 per platform.'))
t(D,'div-rates',('Dividende','10,75%','Cât impozit plătești pe dividende în 2026–27',['Rata de bază: 10,75%','Rata superioară: 35,75%','Rata adițională: 39,35%'],
  'Ai firmă LTD și îți iei dividende? Din aprilie 2026 ratele sunt 10,75%, 35,75% și 39,35%, în funcție de banda ta de impozit.',RT[0]),
  ('Dividends','10.75%','Dividend tax rates for 2026-27',['Ordinary rate: 10.75%','Upper rate: 35.75%','Additional rate: 39.35%'],
  'Taking dividends from your company? For 2026 to 2027 the rates are 10.75%, 35.75% and 39.35%, depending on your band.',ET[1],
  'Dividend tax 2026-27: 10.75% ordinary, 35.75% upper, 39.35% additional.'))
t(D,'div-500',('Dividende','£500','Primii £500 de dividende sunt fără impozit',['Dividend Allowance: £500 pe an','Peste £500 se aplică ratele de dividende','Contează în ce bandă de impozit te afli'],
  'Primii £500 de dividende pe an nu se impozitează. Peste această sumă plătești rata de dividende a benzii tale.',RT[0]),
  ('Dividends','£500','The first £500 of dividends is tax-free',['Dividend Allowance: £500 a year','Above that, dividend rates apply','Your Income Tax band decides the rate'],
  'The first £500 of dividends each year is tax-free. Above that, you pay the dividend rate for your band.',ET[1],
  'Dividend Allowance 2026-27: £500. Above it, 10.75%, 35.75% or 39.35% by band.'))
t(D,'cb-rates',('Child Benefit','£27,05','Cât e Child Benefit în 2026–27',['Primul copil: £27,05 pe săptămână','Fiecare alt copil: £17,90 pe săptămână','Din aprilie 2027: £28,00 și £18,55'],
  'Child Benefit în 2026–27: £27,05 pe săptămână pentru primul copil și £17,90 pentru fiecare alt copil. Din aprilie 2027 crește la £28,00 și £18,55.',RT[2]),
  ('Child Benefit','£27.05','Child Benefit rates for 2026-27',['Eldest or only child: £27.05 a week','Each other child: £17.90 a week','From April 2027: £28.00 and £18.55'],
  'Child Benefit for 2026 to 2027 is £27.05 a week for the eldest child and £17.90 for each other child, rising to £28.00 and £18.55 from April 2027.',ET[0],
  'Child Benefit 2026-27: £27.05 eldest, £17.90 others per week. From April 2027: £28.00 and £18.55.'))
t(D,'wfh-flat-se',('Lucru de acasă','£26','Lucrezi de acasă? Rata fixă pe lună',['25–50 de ore pe lună: £10','51–100 de ore: £18','101 ore sau mai mult: £26'],
  'Dacă lucrezi de acasă cel puțin 25 de ore pe lună, poți deduce o sumă fixă: £10, £18 sau £26 pe lună, în funcție de ore.',RT[1]),
  ('Working from home','£26','Work from home? Use the flat rate',['25 to 50 hours a month: £10','51 to 100 hours: £18','101 hours or more: £26'],
  'Self-employed and working from home at least 25 hours a month? You can claim a flat £10, £18 or £26 a month.',ET[1],
  'Home-working flat rate for the self-employed: £10, £18 or £26 a month depending on hours (min 25).'))
t(D,'exp-commute',('Cheltuieli','Nu','Drumul de acasă la lucru nu se deduce',['Naveta zilnică nu e cheltuială de business','Amenzile și penalitățile nu se deduc','Drumurile la clienți și furnizori, da'],
  'Naveta de acasă la locul obișnuit de muncă nu se deduce, nici amenzile. Drumurile de business, la clienți sau furnizori, da.',RT[1]),
  ('Expenses','No','Commuting is not a business expense',['Home-to-work travel cannot be claimed','Fines and penalties cannot be claimed','Trips to clients and suppliers can'],
  'You cannot claim for commuting or for fines. Business journeys, to clients or suppliers, you can.',ET[1],
  'Self-employed: no claims for commuting or fines; business journeys are allowable.'))
t(D,'exp-overnight',('Cheltuieli','Hotel','Deplasare cu înnoptare: ce poți deduce',['Hotelul pentru deplasarea de business','Mesele din deplasările cu înnoptare','Bilete de tren, autobuz, avion sau taxi'],
  'În deplasările de business cu înnoptare poți deduce cazarea, mesele și biletele. Păstrează bonurile pentru fiecare.',RT[1]),
  ('Expenses','Hotel','Overnight business trips: what to claim',['Hotel rooms for business trips','Meals on overnight business trips','Train, bus, air and taxi fares'],
  'On overnight business trips you can claim the hotel, meals and fares. Keep every receipt.',ET[1],
  'Overnight business trip? Hotel, meals and fares are allowable expenses.'))
t(D,'mtd-qualifying',('Making Tax Digital','£50.000','MTD: ce venit se socotește',['Self-employed plus chirii, adunate','Venitul brut, înainte de cheltuieli','Se ia din declarația depusă anul anterior'],
  'Pentru Making Tax Digital contează venitul brut din self-employed și chirii, adunate, luat din declarația depusă anul anterior.',RT[1]),
  ('Making Tax Digital','£50,000','MTD: what income counts',['Self-employment plus property income combined','Gross income, before expenses','Taken from the previous year\'s return'],
  'For MTD, qualifying income is your self-employment and property income combined, before expenses, based on the return you filed the year before.',ET[1],
  'MTD qualifying income = self-employment + property, combined, before expenses, from last year\'s return.'))
t(D,'ola-ltd',('Ola Accountancy','LTD','Vrei să-ți deschizi firmă LTD?',['Discutăm dacă LTD are sens pentru tine','Ne ocupăm de înregistrare și obligații','Contabilitate pe tot parcursul anului'],
  'Te gândești să treci de la self-employed la LTD? Discutăm cifrele tale, apoi ne ocupăm de înregistrare și de contabilitatea firmei.',RT[0]),
  ('Ola Accountancy','Ltd','Thinking of setting up a limited company?',['We look at whether a company suits you','We handle the set-up and the filings','Bookkeeping and accounts all year'],
  'Thinking about moving from sole trader to limited company? We go through your numbers first, then handle the set-up and the filings.',ET[1],
  'Thinking of a limited company? Ola Accountancy helps you decide, then handles set-up and filings.'))
t(D,'ctf-unclaimed',('Copii','£2.242','Ai copil de 18+ ani? Poate are un Child Trust Fund',['758.000 de conturi neridicate (HMRC, 2025)','Valoarea medie: aproximativ £2.242','Caută pe GOV.UK: Find my Child Trust Fund'],
  'HMRC a anunțat 758.000 de Child Trust Fund-uri neridicate, cu o valoare medie de aproximativ £2.242. Căutarea pe GOV.UK e gratuită.',RT[2]),
  ('Young people','£2,242','Aged 18+? You may have a Child Trust Fund',['758,000 unclaimed accounts (HMRC, 2025)','Average value about £2,242','Search GOV.UK: Find my Child Trust Fund'],
  'HMRC says 758,000 matured Child Trust Funds are unclaimed, worth about £2,242 on average. The GOV.UK search is free.',ET[0],
  '758,000 unclaimed Child Trust Funds, average about £2,242. Use the free Find my Child Trust Fund tool on GOV.UK.'))
t(D,'sure-start',('Ajutoare','£500','Sure Start Maternity Grant: £500 pentru bebeluș',['De obicei pentru primul copil','Dacă tu sau partenerul primiți anumite beneficii','Ceri cu 11 săptămâni înainte sau până la 6 luni după'],
  'Dacă aștepți primul copil și tu sau partenerul primiți anumite beneficii, poți primi £500, bani pe care nu-i dai înapoi.',RT[2]),
  ('Benefits','£500','Sure Start Maternity Grant: £500',['Usually for your first child','You or your partner must get certain benefits','Claim 11 weeks before or up to 6 months after'],
  'Expecting your first child and on certain benefits? The Sure Start Maternity Grant is £500 and you do not pay it back.',ET[0],
  'Sure Start Maternity Grant: £500, usually first child, claim from 11 weeks before to 6 months after the birth.'))
t(D,'tip-tax-pot',('Sfat','Lunar','Pune deoparte pentru impozit în fiecare lună',['Un cont separat doar pentru impozit','Muți un procent din fiecare încasare','În ianuarie nu mai ai surprize'],
  'Cel mai simplu obicei pentru self-employed: un cont separat doar pentru impozit, în care muți un procent din fiecare încasare.',RT[1]),
  ('Tip','Monthly','Set money aside for tax every month',['A separate account just for tax','Move a percentage of every payment in','No surprises in January'],
  'The simplest habit for the self-employed: a separate tax account and a percentage of every payment moved into it.',ET[1],
  'Self-employed tip: a separate tax account, topped up from every payment, means no January surprises.'))
t(D,'holiday',('Angajați','28 zile','Câte zile de concediu are un angajat',['Minimum 5,6 săptămâni plătite pe an','5 zile pe săptămână: 28 de zile','Sărbătorile legale pot intra în cele 28'],
  'Orice angajat are dreptul la cel puțin 5,6 săptămâni de concediu plătit pe an, adică 28 de zile la 5 zile pe săptămână.',RT[0]),
  ('Employees','28 days','Statutory holiday: how many days?',['At least 5.6 weeks paid a year','5 days a week: 28 days','Bank holidays can count towards the 28'],
  'Most workers are entitled to 5.6 weeks of paid holiday a year, which is 28 days for a 5-day week.',ET[1],
  'Statutory holiday: 5.6 weeks a year, 28 days for a 5-day week; bank holidays can count.'))
t(D,'b26-pension-iht',None,('Budget 2026','Apr 2027','Pensions come into inheritance tax',['Unused pension funds count from 6 April 2027','Executors can ask the scheme to pay the IHT','Review nominations and your estate plan'],
  'From 6 April 2027, most unused pension funds and death benefits count towards the estate for inheritance tax. Worth reviewing your plans now.',EBT,
  'From 6 April 2027 unused pension funds fall into the estate for IHT. Review nominations and plans now.'),extra=True)

D = DAYS[3]  # Mon 2 Nov
t(D,'mtd-quarters',('Making Tax Digital','7 nov.','MTD: următorul termen e 7 noiembrie',['Termene: 7 august, 7 noiembrie','Apoi 7 februarie și 7 mai','Următorul: 7 noiembrie 2026'],
  'Ești deja în Making Tax Digital? Următoarea actualizare trimestrială e pe 7 noiembrie 2026. Celelalte termene: 7 februarie, 7 mai și 7 august.',RT[1]),
  ('Making Tax Digital','7 Nov','MTD: next update due 7 November',['Deadlines: 7 August, 7 November','Then 7 February and 7 May','Next one: 7 November 2026'],
  'Already in Making Tax Digital? Your next quarterly update is due 7 November 2026. The others: 7 February, 7 May and 7 August.',ET[1],
  'MTD quarterly update deadlines: 7 Aug, 7 Nov, 7 Feb, 7 May. Next one: 7 November 2026.'))
t(D,'mtd-easement',('Making Tax Digital','2026–27','MTD: fără penalități pentru update-uri în 2026–27',['Pentru cei intrați în MTD din aprilie 2026','Dar trimiți update-urile înainte de declarație','Declarația anuală întârziată aduce punct de penalizare'],
  'În primul an de MTD, 2026–27, nu se dau penalități pentru actualizările trimestriale întârziate. Declarația anuală însă trebuie depusă la timp.',RT[1]),
  ('Making Tax Digital','2026-27','MTD: no penalties for late updates in 2026-27',['For people in MTD from April 2026','Updates must still be sent before your return','A late annual return still earns a point'],
  'In the first MTD year, 2026 to 2027, there are no penalties for missing a quarterly update deadline. The annual return deadline still counts.',ET[1],
  'MTD 2026-27: no penalties for late quarterly updates, but a late tax return still earns a penalty point.'))
t(D,'b26-poa-2029',('Bugetul 2026','2029','Plățile în avans se schimbă din 2029',['Plăți mai mici și mai dese în timpul anului','Automate, cu opțiune prin PAYE','Anunțat în Bugetul din 28 octombrie'],
  'Bugetul anunță că, din aprilie 2029, cei care fac plăți în avans vor plăti sume mai mici și mai dese în timpul anului. Până atunci, regulile rămân la fel.',BT),
  ('Budget 2026','2029','Payments on account to change from 2029',['Smaller, more regular payments in the year','Automated, with a PAYE option','Announced in the 28 October Budget'],
  'From April 2029, people who make payments on account will pay smaller, more regular amounts in the year. Until then, the rules stay the same.',EBT,
  'Budget 2026: from April 2029 payments on account become smaller and more regular, with a PAYE option.'))
t(D,'b26-se-paternity',('Bugetul 2026','2029','Tați self-employed: parental pay din 2029',['Pentru prima dată, și tații self-employed','Din aprilie 2029, în Anglia, Scoția și Țara Galilor','Plus partenerii și cei care adoptă'],
  'Bugetul anunță că, din aprilie 2029, tații, partenerii și cei care adoptă, self-employed, vor putea primi parental pay. Până acum erau excluși.',BT),
  ('Budget 2026','2029','Self-employed dads to get parental pay',['A first for self-employed fathers','From April 2029 in Great Britain','Partners and adopters included'],
  'From April 2029, eligible self-employed fathers, partners and adopters in Great Britain can get parental pay for the first time.',EBT,
  'Budget 2026: self-employed fathers, partners and adopters get access to parental pay from April 2029.'))
t(D,'vat-prereg',('TVA','4 ani','Te-ai înregistrat pentru TVA? Recuperezi și din urmă',['Bunuri cumpărate cu până la 4 ani înainte','Dacă încă le ai sau au intrat în produse','Servicii: cu până la 6 luni înainte'],
  'După înregistrarea pentru TVA poți recupera TVA-ul pe bunuri cumpărate cu până la 4 ani înainte, dacă încă le ai, și pe servicii din ultimele 6 luni.',RT[1]),
  ('VAT','4 years','Just registered for VAT? Reclaim the past',['Goods bought up to 4 years before','If you still have them or goods made from them','Services: up to 6 months before'],
  'After registering for VAT you can reclaim VAT on goods bought up to 4 years before, if you still have them, and on services from the last 6 months.',ET[1],
  'New VAT registration? Reclaim VAT on goods up to 4 years back (if still held) and services up to 6 months back.'))
t(D,'ct-rates',('Firme LTD','19%','Corporation Tax: 19% sau 25%',['Profit până la £50.000: 19%','Profit peste £250.000: 25%','Între ele: marginal relief'],
  'Firmele LTD plătesc 19% Corporation Tax pe profit de până la £50.000 și 25% peste £250.000. Între ele se aplică marginal relief.',RT[0]),
  ('Limited companies','19%','Corporation Tax: 19% or 25%',['Profits up to £50,000: 19%','Profits over £250,000: 25%','In between: marginal relief'],
  'Companies pay 19% Corporation Tax on profits up to £50,000 and 25% above £250,000, with marginal relief in between.',ET[1],
  'Corporation Tax: 19% up to £50,000 profit, 25% above £250,000, marginal relief between.'))
t(D,'ct600-12m',('Firme LTD','9 luni','Corporation Tax: plata vine înaintea declarației',['Plata: 9 luni și o zi după finalul anului','Declarația CT600: în 12 luni','Nu aștepta declarația ca să plătești'],
  'La firmele LTD, Corporation Tax se plătește de obicei la 9 luni și o zi după finalul anului contabil, iar declarația se depune în 12 luni.',RT[0]),
  ('Limited companies','9 months','Corporation Tax: pay before you file',['Payment: usually 9 months and 1 day after year end','Company Tax Return: within 12 months','Do not wait for the return to pay'],
  'Corporation Tax is usually due 9 months and 1 day after the year end, but the return is due 12 months after. Payment comes first.',ET[1],
  'Corporation Tax: usually pay 9 months + 1 day after year end; file the return within 12 months.'))
t(D,'ch-penalties',('Companies House','£1.500','Conturile firmei depuse târziu costă',['Până la o lună: £150; 1–3 luni: £375','3–6 luni: £750; peste 6 luni: £1.500','Doi ani la rând: amenda se dublează'],
  'Companies House amendează automat conturile depuse târziu, de la £150 la £1.500. Dacă întârzii doi ani la rând, amenda se dublează.',RT[0]),
  ('Companies House','£1,500','Late company accounts cost money',['Up to 1 month: £150; 1-3 months: £375','3-6 months: £750; over 6 months: £1,500','Late two years running: doubled'],
  'Companies House fines late accounts from £150 to £1,500, and doubles it if you are late two years in a row.',ET[1],
  'Late private company accounts: £150, £375, £750 or £1,500, doubled if late two years running.'))
t(D,'ea-10500',('Angajatori','£10.500','Employment Allowance: până la £10.500',['Reducere din National Insurance de angajator','Nu se poate dacă singurul angajat e directorul unic','Se cere prin payroll'],
  'Firmele cu angajați pot reduce National Insurance de angajator cu până la £10.500 pe an. Excepție: firma cu un singur director care e și singurul angajat.',RT[0]),
  ('Employers','£10,500','Employment Allowance: up to £10,500',['Cuts your employer National Insurance','Not if your sole director is the only employee','Claimed through payroll'],
  'Employment Allowance cuts employer NI by up to £10,500 a year, but not for a company whose only employee is its sole director.',ET[1],
  'Employment Allowance: up to £10,500 off employer NI. Not available to sole-director-only companies.'))
t(D,'ola-mtd',('Ola Accountancy','MTD','Te ajutăm cu Making Tax Digital',['Verificăm dacă intri în MTD și de când','Îți explicăm ce evidențe digitale îți trebuie','Scrie-ne și discutăm situația ta'],
  'Nu știi dacă intri în Making Tax Digital? Verificăm împreună de când, ce evidențe îți trebuie și cum le ții fără stres.',RT[1]),
  ('Ola Accountancy','MTD','Help with Making Tax Digital',['We check if and when MTD applies to you','We explain the digital records you need','Message us to talk it through'],
  'Not sure if Making Tax Digital applies to you? We check when it starts for you and what records you need.',ET[1],
  'Not sure if MTD applies to you? Ola Accountancy checks when and what records you need.'))
t(D,'smp-194',('Familie','£194,32','Maternity și paternity pay în 2026–27',['Maternity: 90% din salariu primele 6 săptămâni','Apoi £194,32 pe săptămână sau 90%, cât e mai puțin','Paternity: £194,32 sau 90%, cât e mai puțin'],
  'Statutory Maternity Pay în 2026–27: 90% din salariu în primele 6 săptămâni, apoi £194,32 pe săptămână sau 90%, cât e mai puțin.',RT[2]),
  ('Family','£194.32','Maternity and paternity pay 2026-27',['Maternity: 90% of pay for the first 6 weeks','Then £194.32 a week or 90%, whichever is lower','Paternity: £194.32 or 90%, whichever is lower'],
  'Statutory Maternity Pay for 2026 to 2027: 90% for 6 weeks, then £194.32 or 90% if lower. Paternity pay follows the same weekly rate.',ET[0],
  'SMP 2026-27: 90% for 6 weeks, then £194.32 or 90% if lower. SPP: £194.32 or 90% if lower.'))
t(D,'nmw-18-20',('Angajați','£10,85','Salariul minim pentru tineri, acum',['18–20 de ani: £10,85 pe oră','Sub 18 ani și ucenici: £8 pe oră','21 de ani și peste: £12,71 pe oră'],
  'Ratele de salariu minim valabile acum, din aprilie 2026: £12,71 pentru 21+, £10,85 pentru 18–20 de ani și £8 pentru sub 18 și ucenici.',RT[0]),
  ('Employees','£10.85','Minimum wage for younger workers now',['Age 18 to 20: £10.85 an hour','Under 18 and apprentices: £8 an hour','Age 21 and over: £12.71 an hour'],
  'Current minimum wage rates since April 2026: £12.71 for 21+, £10.85 for 18 to 20, and £8 for under-18s and apprentices.',ET[1],
  'Minimum wage now: £12.71 (21+), £10.85 (18-20), £8 (under 18 and apprentices).'))
t(D,'cash-basis',('Self-employed','Cash','Cash basis e acum metoda standard',['Înregistrezi banii când intră și când ies','Metoda tradițională doar dacă o alegi','Firmele LTD nu pot folosi cash basis'],
  'Pentru self-employed, cash basis e acum metoda standard: contează când intră și când ies banii. Metoda tradițională o folosești doar dacă o alegi.',RT[1]),
  ('Self-employed','Cash','Cash basis is now the standard method',['Record money when it comes in and goes out','Traditional accounting only if you choose it','Limited companies cannot use cash basis'],
  'For sole traders, cash basis is now the standard way to record income and expenses. Traditional accounting is an opt-in.',ET[1],
  'Sole traders: cash basis is now standard. Traditional accounting is opt-in. Companies cannot use it.'))
t(D,'sl-thresholds',('Student loan','£29.385','De la ce venit plătești student loan',['Plan 2: peste £29.385 pe an','Plan 1: £26.900; Plan 5: £25.000','Plătești 9% din ce depășește pragul'],
  'Student loan se plătește doar peste prag: £29.385 la Plan 2, £26.900 la Plan 1, £25.000 la Plan 5. Rata e 9% din ce depășește.',RT[2]),
  ('Student loan','£29,385','When student loan repayments start',['Plan 2: over £29,385 a year','Plan 1: £26,900; Plan 5: £25,000','You repay 9% of income above the threshold'],
  'Student loan thresholds for 2026 to 2027: Plan 2 £29,385, Plan 1 £26,900, Plan 5 £25,000. You repay 9% above the threshold.',ET[0],
  'Student loan 2026-27: Plan 2 £29,385, Plan 1 £26,900, Plan 5 £25,000; 9% above threshold.'))
t(D,'b26-ev-bik',None,('Budget 2026','4%','Electric company cars: BIK rises slowly',['2026-27: 4%; 2027-28: 5%','2028-29: 7%; 2029-30: 9%','Still well below most petrol and diesel cars'],
  'Company car tax on zero-emission cars stays low: 4% this year, 5% next, then 7% and 9%.',EBT,
  'Electric company car BIK: 4% (26-27), 5% (27-28), 7% (28-29), 9% (29-30).'),extra=True)

D = DAYS[4]  # Tue 3 Nov
t(D,'b26-eved',('Bugetul 2026','3p','Mașini electrice: taxă pe milă din 2028',['eVED de la 1 aprilie 2028','3p pe milă pentru mașini electrice','1,5p pe milă pentru plug-in hibride'],
  'Bugetul confirmă eVED din aprilie 2028: 3p pe milă pentru mașinile electrice și 1,5p pentru plug-in hibride.',BT),
  ('Budget 2026','3p','Electric cars: pay-per-mile from 2028',['eVED from 1 April 2028','3p a mile for battery electric cars','1.5p a mile for plug-in hybrids'],
  'The Budget confirms eVED from April 2028: 3p a mile for electric cars and 1.5p for plug-in hybrids.',EBT,
  'Budget 2026: eVED from 1 April 2028, 3p a mile for EVs and 1.5p for plug-in hybrids.'))
t(D,'b26-isa-20k',('Bugetul 2026','£20.000','Limita ISA rămâne £20.000',['Inclusiv pentru Cash ISA, peste 18 ani','Confirmat în Bugetul din 28 octombrie','Dobânda din ISA nu se impozitează'],
  'Bugetul păstrează limita de £20.000 pe an și pentru Cash ISA. Cu impozitul pe dobânzi în creștere din 2027, ISA contează mai mult.',BT),
  ('Budget 2026','£20,000','The £20,000 ISA limit stays',['Including cash ISAs for over-18s','Confirmed in the 28 October Budget','ISA interest is tax-free'],
  'The Budget keeps the £20,000 annual ISA limit, including for cash ISAs. With savings tax rising in 2027, ISAs matter more.',EBT,
  'Budget 2026: the £20,000 ISA limit stays, including cash ISAs for over-18s.'))
t(D,'sa-early',('Self Assessment','Acum','De ce să-ți faci declarația acum, nu în ianuarie',['Afli din timp cât ai de plătit','Ai timp să strângi banii până pe 31 ianuarie','Dacă ai refund, îl primești mai repede'],
  'Termenul e 31 ianuarie, dar dacă depui acum afli din timp suma și ai luni întregi să te pregătești.',RT[0]),
  ('Self Assessment','Now','Why file now, not in January',['You know your bill early','You have time to save before 31 January','Refunds arrive sooner'],
  'The deadline is 31 January, but filing now tells you your bill early and gives you months to prepare.',ET[0],
  'File your Self Assessment early: know your bill, plan your cash, get refunds sooner.'))
t(D,'myth-cash',('Mituri','Mit','„Banii cash nu se văd.” Greșit',['Tot venitul se declară, cash sau transfer','Platformele online raportează vânzările la HMRC','Corectează din timp, nu când te întreabă HMRC'],
  'Venitul încasat cash se declară exact ca cel din transfer. Dacă ai omis ceva, e mai bine să corectezi tu decât să te întrebe HMRC.',RT[2]),
  ('Myths','Myth','"Cash payments don\'t count." Wrong',['All income must be declared','Online platforms report sales to HMRC','Put it right before HMRC asks'],
  'Cash income is taxable like any other income. If something was missed, correcting it yourself beats waiting for HMRC.',ET[0],
  'Cash income must be declared like any other. If you missed some, correct it before HMRC asks.'))
t(D,'hicbc-paye',('Child Benefit','PAYE','HICBC se poate plăti prin tax code',['Dacă nu depui Self Assessment din alt motiv','Altfel, se plătește prin declarație','Sau renunți la plăți și păstrezi creditele NI'],
  'Dacă ești angajat și nu depui Self Assessment din alt motiv, poți plăti taxa pe Child Benefit prin tax code. Renunțarea la plăți îți păstrează creditele NI.',RT[2]),
  ('Child Benefit','PAYE','Pay the Child Benefit charge via PAYE',['If you do not file Self Assessment otherwise','Otherwise it goes on your tax return','Or opt out and keep NI credits'],
  'Employed and not filing Self Assessment for another reason? You can pay the Child Benefit charge through PAYE. Opting out keeps NI credits.',ET[0],
  'HICBC can be paid through PAYE if you do not need Self Assessment for anything else.'))
t(D,'state-pension-241',('Pensie','£241,30','Cât e pensia de stat completă acum',['£241,30 pe săptămână în 2026–27','Ai nevoie de 35 de ani de contribuții','Minimum 10 ani ca să primești ceva'],
  'Pensia de stat nouă completă este £241,30 pe săptămână în 2026–27. Pentru ea îți trebuie 35 de ani de contribuții, iar minimul e 10.',RT[2]),
  ('Pension','£241.30','Full new State Pension now',['£241.30 a week in 2026-27','35 qualifying years for the full amount','At least 10 years to get any'],
  'The full new State Pension is £241.30 a week in 2026 to 2027. You usually need 35 qualifying years, and at least 10 to get any.',ET[0],
  'Full new State Pension 2026-27: £241.30/week. 35 qualifying years for full, 10 minimum.'))
t(D,'spa-67',('Pensie','67','Vârsta de pensionare urcă la 67 de ani',['Crește treptat între 2026 și 2028','Născuți 6 apr. 1960 – 5 mar. 1961: între 66 și 67','Născuți din 6 martie 1961: 67 de ani'],
  'Vârsta de pensionare de stat crește treptat de la 66 la 67 de ani între 2026 și 2028. Verifică-ți data exactă pe GOV.UK.',RT[2]),
  ('Pension','67','State Pension age is rising to 67',['Rising in steps between 2026 and 2028','Born 6 Apr 1960 to 5 Mar 1961: between 66 and 67','Born from 6 March 1961: age 67'],
  'State Pension age is rising from 66 to 67 between 2026 and 2028. Check your exact date on GOV.UK.',ET[0],
  'State Pension age rises from 66 to 67 between 2026 and 2028. Born from 6 March 1961: 67.'))
t(D,'er-under21',('Angajatori','0%','Angajați sub 21 de ani: NI de angajator 0%',['0% până la £967 pe săptămână','15% doar peste acest prag','La fel pentru ucenicii sub 25 de ani'],
  'Pentru angajații sub 21 de ani și ucenicii sub 25, firma plătește 0% National Insurance de angajator până la £967 pe săptămână.',RT[0]),
  ('Employers','0%','Under-21 staff: 0% employer NI',['0% up to £967 a week','15% only above that','Same for apprentices under 25'],
  'For employees under 21 and apprentices under 25, employer NI is 0% up to £967 a week and 15% above.',ET[1],
  'Employer NI is 0% up to £967/week for under-21s and apprentices under 25.'))
t(D,'ola-sa-early',('Ola Accountancy','31 ian.','Fă declarația cu noi din noiembrie',['Trimite actele acum, nu în ultima săptămână','Îți spunem suma din timp','Plătești la termen, fără stres'],
  'Nu lăsa declarația pentru ultima săptămână din ianuarie. Trimite-ne actele acum și îți spunem din timp cât ai de plătit.',RT[0]),
  ('Ola Accountancy','31 Jan','Get your return done with us in November',['Send your documents now, not in late January','We tell you the figure early','Pay on time, without the stress'],
  'Do not leave your return for the last week of January. Send us your documents now and we tell you the figure early.',ET[1],
  'Beat the January rush: send your Self Assessment documents to Ola Accountancy now.'))
t(D,'gifts-50',('Cheltuieli','£50','Cadouri de Crăciun pentru clienți: când se deduc',['Maximum £50 pe client pe an','Cu reclama firmei vizibilă pe cadou','Nu mâncare, băutură sau vouchere'],
  'Cadourile pentru clienți se deduc doar dacă poartă reclama firmei, costă maximum £50 pe client pe an și nu sunt mâncare, băutură sau vouchere.',RT[1]),
  ('Expenses','£50','Client gifts: when you can claim them',['Up to £50 per recipient per year','Must carry a clear advert for your business','Not food, drink or vouchers'],
  'Client gifts are only deductible if they advertise your business, cost no more than £50 per recipient per year and are not food, drink or vouchers.',ET[1],
  'Client gifts: deductible if branded, up to £50 per recipient a year, and not food, drink or vouchers.'))
t(D,'vat-gifts-50',('TVA','£50','Cadouri de afaceri și TVA',['Cost de £50 sau mai puțin: fără TVA de plătit','Limita: £50 pentru aceeași persoană pe an','Doar cadouri făcute în scop de afaceri'],
  'Dacă ești înregistrat pentru TVA, cadourile de afaceri de cel mult £50 pentru aceeași persoană pe an nu generează TVA de plătit.',RT[1]),
  ('VAT','£50','Business gifts and VAT',['Cost £50 or less: no VAT due','Limit: £50 to the same person in a year','Business gifts only'],
  'VAT-registered? Business gifts costing £50 or less to the same person in a year are outside VAT.',ET[1],
  'VAT: business gifts costing £50 or less to the same person in a year are outside VAT.'))
t(D,'mar-relief',('Angajați','55p','Angajatorul îți plătește sub 55p pe milă?',['Poți cere diferența ca relief fiscal','Se numește Mileage Allowance Relief','Doar pentru drumuri de serviciu, nu navetă'],
  'Dacă folosești mașina ta pentru drumuri de serviciu și angajatorul îți dă mai puțin de 55p pe milă, poți cere diferența de la HMRC.',RT[0]),
  ('Employees','55p','Employer pays under 55p a mile?',['Claim the difference as tax relief','It is called Mileage Allowance Relief','Business journeys only, not commuting'],
  'Use your own car for work and your employer pays under 55p a mile? You can claim tax relief on the shortfall.',ET[0],
  'Employer pays less than 55p a mile? Claim Mileage Allowance Relief on the shortfall.'))
t(D,'uniform',('Angajați','Uniformă','Speli singur uniforma de serviciu?',['Poți cere relief fiscal pentru curățare','Doar uniforme sau haine de protecție','Poți cere și pentru ultimii 4 ani'],
  'Dacă îți speli singur uniforma de serviciu, poți cere relief fiscal de la HMRC, inclusiv pentru ultimii 4 ani fiscali.',RT[0]),
  ('Employees','Uniform','Wash your own work uniform?',['You may claim tax relief for cleaning it','Uniforms and protective clothing only','You can go back 4 tax years'],
  'Wash your own work uniform? You may be able to claim tax relief, for this year and the previous 4.',ET[0],
  'Wash your own work uniform? Claim tax relief, backdated up to 4 years.'))
t(D,'mtd-digital-records',('Making Tax Digital','Digital','MTD: evidențele se țin digital',['Venituri și cheltuieli în software compatibil','Update-uri la HMRC în fiecare trimestru','Declarația finală, tot din software'],
  'În Making Tax Digital nu mai merge cu caietul: veniturile și cheltuielile se țin în software compatibil, iar update-urile pleacă de acolo la HMRC.',RT[1]),
  ('Making Tax Digital','Digital','MTD means digital records',['Income and expenses in compatible software','Quarterly updates sent to HMRC','Your final return from the software too'],
  'Under Making Tax Digital you keep income and expense records in compatible software and send updates to HMRC from it.',ET[1],
  'MTD for Income Tax: digital records in compatible software, quarterly updates, final return from the software.'))
t(D,'b26-badr',None,('Budget 2026','£500k','Business Asset Disposal Relief limit halves',['Lifetime limit falls from £1m to £500,000','For disposals from 6 April 2027','The rate stays at 18%'],
  'Planning to sell your business? The Budget halves the BADR lifetime limit from £1 million to £500,000 from April 2027.',EBT,
  'Budget 2026: BADR lifetime limit falls from £1m to £500,000 from 6 April 2027. Rate stays 18%.'),extra=True)

D = DAYS[5]  # Wed 4 Nov
t(D,'b26-carers',('Bugetul 2026','2030','Carer\'s Allowance: nu mai pierzi tot pentru puțin',['Reducere treptată, nu tăiere completă','Din 2030–31, în Anglia și Țara Galilor','Anunțat în Bugetul din 28 octombrie'],
  'Bugetul anunță că, din 2030–31, cei care câștigă puțin peste limită nu mai pierd tot Carer\'s Allowance: se aplică o reducere treptată.',BT),
  ('Budget 2026','2030','Carer\'s Allowance: no more cliff edge',['A taper instead of losing it all','From 2030 to 2031 in England and Wales','Announced in the 28 October Budget'],
  'Carers who earn slightly over the limit will no longer lose all of Carer\'s Allowance: a taper applies from 2030 to 2031.',EBT,
  'Budget 2026: a Carer\'s Allowance earnings taper replaces the cliff edge from 2030-31.'))
t(D,'b26-ftb-isa',('Bugetul 2026','25%','Vine First Time Buyer ISA',['Din aprilie 2029, pentru economisitorii noi','Bonus de 25% de la stat','Pentru prima casă de până la £450.000'],
  'Bugetul anunță First Time Buyer ISA din aprilie 2029, cu bonus de 25% pentru prima casă de până la £450.000. Cine are deja LISA păstrează regulile actuale.',BT),
  ('Budget 2026','25%','A First Time Buyer ISA is coming',['From April 2029, for new savers','25% government bonus','For a first home up to £450,000'],
  'The Budget announced a First Time Buyer ISA from April 2029, with a 25% bonus for a first home up to £450,000. Existing LISAs keep their rules.',EBT,
  'Budget 2026: First Time Buyer ISA from April 2029, 25% bonus, first homes up to £450,000.'))
t(D,'pension-aa',('Pensie','£60.000','Cât poți pune în pensie cu relief fiscal',['Annual Allowance: £60.000 pe an','Ai accesat deja pensia flexibil? Limita e £10.000','Peste limită poate apărea o taxă'],
  'Annual Allowance pentru pensie este £60.000 pe an în 2026–27. Dacă ai scos deja bani flexibil din pensie, limita poate scădea la £10.000.',RT[2]),
  ('Pension','£60,000','Pension Annual Allowance 2026-27',['Annual Allowance: £60,000','Accessed a pension flexibly? £10,000 limit','Going over can trigger a tax charge'],
  'The pension Annual Allowance is £60,000 in 2026 to 2027, or £10,000 if the Money Purchase Annual Allowance applies.',ET[0],
  'Pension Annual Allowance 2026-27: £60,000; MPAA £10,000.'))
t(D,'savings-5000',('Economii','£5.000','Dobânzi: până la £5.000 la 0%',['Starting rate for savings: 0%','Doar dacă alte venituri sunt mici','Se reduce cu fiecare £1 peste £12.570'],
  'Dacă ai venituri mici, până la £5.000 din dobânzi pot fi impozitate cu 0%. Suma scade cu fiecare liră din alte venituri peste £12.570.',RT[2]),
  ('Savings','£5,000','Up to £5,000 of interest at 0%',['The starting rate for savings is 0%','Only if your other income is low','Reduced by £1 for each £1 over £12,570'],
  'If your other income is low, up to £5,000 of savings interest can be taxed at 0%. It shrinks as other income goes above £12,570.',ET[0],
  'Starting rate for savings: up to £5,000 of interest at 0% if your other income is low.'))
t(D,'jisa-9000',('Copii','£9.000','Junior ISA: până la £9.000 pe an',['Banii cresc fără impozit','Copilul îi poate folosi de la 18 ani','Pot contribui și bunicii'],
  'Într-un Junior ISA poți pune până la £9.000 pe an pentru copil, fără impozit pe câștiguri. Banii devin ai lui la 18 ani.',RT[2]),
  ('Children','£9,000','Junior ISA: up to £9,000 a year',['Grows free of tax','Your child can access it at 18','Grandparents can pay in too'],
  'You can put up to £9,000 a year into a Junior ISA, free of tax. Your child can access it at 18.',ET[0],
  'Junior ISA limit 2026-27: £9,000 a year, tax-free, accessible at 18.'))
t(D,'help-to-save',('Economii','50p','Help to Save: 50p bonus la fiecare £1',['Pentru anumiți beneficiari de Universal Credit','Economisești până la £50 pe lună','Bonusuri după 2 ani și după 4 ani'],
  'Dacă primești Universal Credit, poți avea dreptul la Help to Save: pui până la £50 pe lună și statul îți dă 50p pentru fiecare £1.',RT[2]),
  ('Savings','50p','Help to Save: 50p for every £1',['For some people on Universal Credit','Save up to £50 a month','Bonuses after 2 and 4 years'],
  'On Universal Credit? Help to Save pays a 50p bonus for every £1 you save, up to £50 a month.',ET[0],
  'Help to Save: save up to £50 a month, get 50p per £1, bonuses at 2 and 4 years.'))
t(D,'xmas-bonus',('Ajutoare','£10','Christmas Bonus: £10 fără impozit',['Pentru cei cu anumite beneficii','Se plătește automat, înainte de Crăciun','Nu trebuie să ceri nimic'],
  'Christmas Bonus este o plată de £10, fără impozit, pentru cei care primesc anumite beneficii. Vine automat, înainte de Crăciun.',RT[2]),
  ('Benefits','£10','The £10 Christmas Bonus',['For people on certain benefits','Paid automatically before Christmas','Tax-free, no need to claim'],
  'The Christmas Bonus is a tax-free £10 for people on certain benefits, paid automatically before Christmas.',ET[0],
  'Christmas Bonus: £10, tax-free, paid automatically before Christmas to people on certain benefits.'))
t(D,'xmas-staff-bonus',('Angajați','Bonus','Bonusul de Crăciun în bani se impozitează',['Cadoul în bani de la angajator e venit','Trece prin payroll, ca salariul','Cadourile mici, nu în bani, au alt regim'],
  'Banii dați angajaților de Crăciun se impozitează ca salariu și trec prin payroll. Cadourile mici, care nu sunt bani, au alte reguli.',RT[0]),
  ('Employees','Bonus','Cash Christmas bonuses are taxable',['Cash from your employer is earnings','It goes through payroll like pay','Small non-cash gifts follow other rules'],
  'Cash Christmas gifts and bonuses from an employer are taxable earnings and go through payroll.',ET[1],
  'Cash Christmas bonuses are taxable earnings and go through payroll.'))
t(D,'vat-annual',('TVA','O dată pe an','Annual Accounting Scheme pentru TVA',['O singură declarație de TVA pe an','Plăți în avans pe parcursul anului','Pentru cifră de afaceri până la £1,35 milioane'],
  'Prin Annual Accounting Scheme depui o singură declarație de TVA pe an și plătești în avans. Pentru afaceri de până la £1,35 milioane.',RT[1]),
  ('VAT','Once a year','The VAT Annual Accounting Scheme',['One VAT return a year','Advance payments through the year','For taxable turnover up to £1.35 million'],
  'The Annual Accounting Scheme means one VAT return a year with advance payments, for turnover up to £1.35 million.',ET[1],
  'VAT Annual Accounting: one return a year, for turnover up to £1.35m.'))
t(D,'ola-plan',('Ola Accountancy','£420','Planifică 2027 după Buget, împreună cu noi',['Consultație financiară de 60 de minute','£420 cu TVA inclus','Vedem ce schimbări te afectează pe tine'],
  'Bugetul aduce schimbări din aprilie 2027. În consultația financiară de 60 de minute, £420 cu TVA inclus, vedem împreună ce te afectează pe tine.',RT[0]),
  ('Ola Accountancy','£420','Plan 2027 after the Budget',['A 60-minute financial consultation','£420 including VAT','We look at what affects you'],
  'The Budget brings changes from April 2027. In a 60-minute financial consultation, £420 including VAT, we look at what affects you.',ET[1],
  'Ola Accountancy financial consultation: 60 minutes, £420 incl. VAT, to plan for the Budget changes.'))
t(D,'emp-exp-2500',('Angajați','£2.500','Cheltuieli de serviciu peste £2.500?',['Acum: peste £2.500 le ceri prin Self Assessment','Din aprilie 2028: pragul dispare','Mai multe cereri se vor face prin PAYE'],
  'Angajații cu cheltuieli de serviciu peste £2.500 le cer acum prin Self Assessment. Bugetul anunță că pragul dispare din aprilie 2028.',RT[0]),
  ('Employees','£2,500','Job expenses over £2,500?',['Now: over £2,500 means Self Assessment','From April 2028 the threshold goes','More claims will run through PAYE'],
  'Employees claiming over £2,500 of job expenses currently need Self Assessment. The Budget removes that threshold from April 2028.',EBT,
  'Budget 2026: the £2,500 Self Assessment threshold for employee expenses is removed from April 2028.'))
t(D,'sl-postgrad',('Student loan','£21.000','Postgraduate loan: de când plătești',['Prag: £21.000 pe an','Rată: 6% din ce depășești','Se plătește în plus față de alt plan'],
  'Pentru postgraduate loan plătești 6% din venitul de peste £21.000 pe an, în plus față de alt student loan, dacă ai.',RT[2]),
  ('Student loan','£21,000','Postgraduate loan repayments',['Threshold: £21,000 a year','Rate: 6% of income above it','Paid on top of any other plan'],
  'Postgraduate loan repayments are 6% of income above £21,000 a year, on top of any other student loan plan.',ET[0],
  'Postgraduate loan: 6% of income above £21,000 a year.'))
t(D,'holiday-part-time',('Angajați','16,8','Part-time 3 zile pe săptămână: câte zile de concediu?',['Tot 5,6 săptămâni pe an','3 zile × 5,6 = 16,8 zile','Plafonul legal: 28 de zile pe an'],
  'Și angajații part-time au 5,6 săptămâni de concediu. La 3 zile pe săptămână, asta înseamnă 16,8 zile pe an.',RT[0]),
  ('Employees','16.8','Part-time holiday: how many days?',['Still 5.6 weeks a year','3 days x 5.6 = 16.8 days','Statutory cap: 28 days'],
  'Part-time workers also get 5.6 weeks. On 3 days a week, that is 16.8 days a year.',ET[1],
  'Part-time holiday: 5.6 weeks pro rata. 3 days a week = 16.8 days.'))
t(D,'reenrol',('Angajatori','3 ani','Pensie angajați: re-enrolment la 3 ani',['La fiecare 3 ani, reînscrii angajații ieșiți','Apoi faci re-declaration la Pensions Regulator','Obligatorie chiar dacă nu reînscrii pe nimeni'],
  'Ai angajați? La fiecare 3 ani trebuie să reînscrii în pensie pe cei care au ieșit și să faci re-declaration, chiar dacă nu reînscrii pe nimeni.',RT[0]),
  ('Employers','3 years','Pension re-enrolment every 3 years',['Put eligible staff who left back in','Complete your re-declaration with TPR','Required even if nobody is re-enrolled'],
  'Every 3 years employers must re-enrol eligible staff who left the pension scheme and complete a re-declaration, even if nobody is re-enrolled.',ET[1],
  'Employers: re-enrol every 3 years and complete the re-declaration of compliance, even with no one to re-enrol.'))
t(D,'smp-recover',None,('Employers','92%','Recovering statutory parental pay',['Recover 92% of SMP, SPP and similar pay','Or 109% if your Class 1 NICs were £45,000 or less','Claimed through your payroll submissions'],
  'Employers can usually recover 92% of statutory parental payments, or 109% if total Class 1 NICs last year were £45,000 or less.',ET[1],
  'Employers recover 92% of SMP/SPP, or 109% if last year\'s Class 1 NICs were £45,000 or less.'),extra=True)

D = DAYS[6]  # Thu 5 Nov
t(D,'sa-87-days',('Self Assessment','87 zile','Mai sunt 87 de zile până pe 31 ianuarie',['Declarația online pentru 2025–26','Plata impozitului și prima plată în avans','Începe acum cu actele'],
  'Dragilor, din 5 noiembrie mai sunt 87 de zile până pe 31 ianuarie 2027: declarația online pentru 2025–26 și plata. Începe acum, da?',RT[0]),
  ('Self Assessment','87 days','87 days to the 31 January deadline',['Online return for 2025 to 2026','Tax payment and first payment on account','Start gathering documents now'],
  'From 5 November there are 87 days to 31 January 2027: the online return for 2025 to 2026 and the payment. Start now.',ET[0],
  '87 days to 31 January 2027: file your 2025-26 return online and pay. Start now.'))
t(D,'afr-ev',('Mașini de firmă','7p','Mașină electrică de firmă: cât rambursezi pe milă',['7p pe milă la încărcare acasă','15p pe milă la încărcător public','Rate HMRC din 1 septembrie 2026'],
  'Pentru mașinile electrice de firmă, HMRC recomandă 7p pe milă la încărcare acasă și 15p la încărcător public, din 1 septembrie 2026.',RT[0]),
  ('Company cars','7p','Electric company cars: mileage rates',['7p a mile when charged at home','15p a mile at public chargers','HMRC rates from 1 September 2026'],
  'Advisory electricity rates for company cars from 1 September 2026: 7p a mile at home, 15p at public chargers.',ET[1],
  'Advisory electricity rates from 1 Sep 2026: 7p/mile home charging, 15p/mile public.'))
t(D,'mileage-bike',('Kilometraj','20p','Bicicletă sau motocicletă la serviciu?',['Bicicletă: 20p pe milă','Motocicletă: 24p pe milă','Mașină sau dubă: 55p primele 10.000 mile'],
  'Și bicicleta are rată HMRC: 20p pe milă pentru drumurile de serviciu. Motocicleta are 24p, iar mașina 55p pentru primele 10.000 de mile.',RT[0]),
  ('Mileage','20p','Cycle or motorbike for work?',['Bicycle: 20p a mile','Motorcycle: 24p a mile','Car or van: 55p for the first 10,000 miles'],
  'HMRC mileage rates for business journeys: 20p a mile by bike, 24p by motorcycle, 55p by car for the first 10,000 miles.',ET[1],
  'Business mileage rates: bike 20p, motorcycle 24p, car/van 55p (first 10,000 miles).'))
t(D,'employee-nic-8',('Angajați','8%','Cât National Insurance plătește un angajat',['8% între £242 și £967 pe săptămână','2% pe ce depășește £967','Sub £242 pe săptămână: 0%'],
  'Ca angajat plătești 8% National Insurance pe câștigul dintre £242 și £967 pe săptămână și 2% peste. Sub £242, nimic.',RT[0]),
  ('Employees','8%','Employee National Insurance explained',['8% between £242 and £967 a week','2% on earnings above £967','Nothing below £242 a week'],
  'Employee NI for 2026 to 2027 is 8% on weekly earnings between £242 and £967, and 2% above.',ET[0],
  'Employee NI 2026-27: 8% on £242-£967 a week, 2% above.'))
t(D,'blind-allowance',('Allowance','£3.250','Blind Person\'s Allowance: £3.250 în plus',['Pentru persoane înregistrate ca nevăzătoare','Se adaugă la Personal Allowance','Partea nefolosită se poate transfera partenerului'],
  'Blind Person\'s Allowance adaugă £3.250 la Personal Allowance în 2026–27. Mulți nu știu de ea și nu o cer.',RT[2]),
  ('Allowances','£3,250','Blind Person\'s Allowance: £3,250 extra',['For people registered as blind or severely sight impaired','Added to your Personal Allowance','Unused amount can go to a spouse'],
  'Blind Person\'s Allowance adds £3,250 to your tax-free allowance in 2026 to 2027. Many people never claim it.',ET[0],
  'Blind Person\'s Allowance 2026-27: £3,250 on top of the Personal Allowance.'))
t(D,'winter-fuel-35k',('Pensionari','£35.000','Winter Fuel și venit peste £35.000',['Plata vine oricum, automat','HMRC o recuperează prin sistemul fiscal','Venitul partenerului nu se adună'],
  'Dacă venitul tău total depășește £35.000, Winter Fuel Payment vine oricum, dar HMRC o recuperează. Contează doar venitul tău, nu și al partenerului.',RT[2]),
  ('Pensioners','£35,000','Winter Fuel Payment and income over £35,000',['The payment still arrives automatically','HMRC takes it back through the tax system','Your partner\'s income does not count'],
  'If your total income is over £35,000, HMRC takes the Winter Fuel Payment back. Your partner\'s income does not count.',ET[0],
  'Winter Fuel Payment: income over £35,000 means HMRC takes it back. Partner\'s income does not count.'))
t(D,'hmrc-app-ni',('HMRC app','App','Numărul de National Insurance, din aplicația HMRC',['Îl descarci direct din HMRC app','Util la un job nou','Tot acolo îți vezi și tax code-ul'],
  'Ai nevoie de numărul de National Insurance pentru un job nou? Îl poți descărca direct din aplicația HMRC.',RT[2]),
  ('HMRC app','App','Get your NI number from the HMRC app',['Download it straight from the HMRC app','Handy when starting a new job','You can check your tax code there too'],
  'Need your National Insurance number for a new job? You can download it from the HMRC app.',ET[0],
  'Need your National Insurance number? Download it from the HMRC app.'))
t(D,'vat-88k',('TVA','£88.000','Sub £88.000? Poți ieși din TVA',['Când cifra de afaceri taxabilă scade sub £88.000','Ieșirea e opțională, nu obligatorie','Verifică ce TVA datorezi la ieșire'],
  'Dacă cifra de afaceri taxabilă scade sub £88.000, poți cere ieșirea din TVA. Nu e obligatoriu, iar la ieșire poate exista TVA de plătit pe stoc și echipamente.',RT[1]),
  ('VAT','£88,000','Below £88,000? You can deregister',['When taxable turnover falls below £88,000','Deregistering is optional','Check any VAT due when you leave'],
  'If taxable turnover drops below £88,000, you can cancel your VAT registration. It is optional, and VAT may be due on stock and assets.',ET[1],
  'VAT deregistration threshold: £88,000. Optional, and VAT may be due on stock and assets.'))
t(D,'ola-se-accounts',('Ola Accountancy','A–Z','Contabilitate pentru self-employed, de la A la Z',['Ținem evidența veniturilor și cheltuielilor','Facem declarația Self Assessment','Îți spunem din timp cât să pui deoparte'],
  'Ești self-employed și nu vrei să te mai gândești la acte? Ne ocupăm noi de evidențe și de declarație și îți spunem din timp cât să pui deoparte.',RT[1]),
  ('Ola Accountancy','Sole traders','Accounts for sole traders, start to finish',['We keep your income and expense records','We file your Self Assessment','We tell you early what to set aside'],
  'Self-employed and tired of paperwork? We handle your records and your return, and tell you early what to set aside.',ET[1],
  'Ola Accountancy: bookkeeping and Self Assessment for sole traders in Luton and Birmingham.'))
t(D,'trading-or-expenses',('Self-employed','£1.000','Trading allowance sau cheltuieli? Nu ambele',['Cu allowance nu mai scazi cheltuielile reale','Merită când ai cheltuieli mici','Cu cheltuieli mari, deduci cheltuielile'],
  'Trading allowance de £1.000 îl folosești în loc de cheltuieli, nu împreună cu ele. Dacă ai cheltuieli mari, de obicei e mai bine să le deduci pe ele.',RT[1]),
  ('Self-employed','£1,000','Trading allowance or expenses? Not both',['Using the allowance replaces actual expenses','Worth it when expenses are small','With bigger costs, claim the expenses'],
  'The £1,000 trading allowance replaces your actual expenses; you cannot use both. With bigger costs, claiming expenses usually works better.',ET[1],
  'The trading allowance replaces actual expenses. Small costs: allowance. Bigger costs: claim expenses.'))
t(D,'exp-fines-records',('Cheltuieli','Bonuri','Fără bon, fără cheltuială',['Păstrează bonul pentru fiecare cheltuială','Poza clară pe telefon e suficientă ca evidență','Notează pe scurt scopul de business'],
  'Orice cheltuială pe care vrei s-o deduci trebuie să aibă bon sau factură. Fă-i o poză clară și notează scopul, da?',RT[1]),
  ('Expenses','Receipts','No receipt, no expense',['Keep a receipt for every expense','A clear phone photo works as a record','Note the business purpose briefly'],
  'Every expense you claim needs a receipt or invoice. Take a clear photo and note what it was for.',ET[1],
  'Self-employed: keep a receipt for every expense, a clear photo is fine, and note the business purpose.'))
t(D,'afr-petrol',('Mașini de firmă','14p','Mașină de firmă pe benzină: cât rambursezi pe milă',['Benzină până la 1400cc: 14p pe milă','1401–2000cc: 17p; peste 2000cc: 27p','Diesel: 15p, 16p sau 22p, după motor'],
  'Dacă angajații folosesc mașina firmei și își plătesc singuri combustibilul, HMRC recomandă aceste rate pe milă, valabile din 1 septembrie 2026.',RT[0]),
  ('Company cars','14p','Advisory fuel rates for company cars',['Petrol up to 1400cc: 14p a mile','1401-2000cc: 17p; over 2000cc: 27p','Diesel: 15p, 16p or 22p by engine size'],
  'HMRC advisory fuel rates for company cars from 1 September 2026: petrol 14p, 17p or 27p; diesel 15p, 16p or 22p a mile.',ET[1],
  'Advisory fuel rates from 1 Sep 2026: petrol 14p/17p/27p, diesel 15p/16p/22p per mile.'))
t(D,'pa-12570',('Allowance','£12.570','Personal Allowance rămâne £12.570',['£12.570 în 2026–27 și în 2027–28','Se reduce cu £1 la fiecare £2 peste £100.000','Peste prag plătești impozit pe venit'],
  'Personal Allowance rămâne £12.570 și în 2027–28. Peste £100.000 venit, allowance-ul scade cu £1 pentru fiecare £2.',RT[0]),
  ('Allowances','£12,570','Personal Allowance stays at £12,570',['£12,570 in 2026-27 and 2027-28','Reduced by £1 for every £2 over £100,000','Income above it is taxed'],
  'The Personal Allowance stays at £12,570 in 2027 to 2028. Above £100,000 of income it falls by £1 for every £2.',ET[0],
  'Personal Allowance: £12,570 in 2026-27 and 2027-28; tapers above £100,000.'))
t(D,'lel-129',('National Insurance','£129','Câștigi puțin? Anul poate conta la pensie',['Între £129 și £242 pe săptămână nu plătești NI','Dar anul se socotește pentru pensia de stat','Sub £129 pe săptămână, nu se socotește'],
  'Ca angajat, dacă câștigi între £129 și £242 pe săptămână, nu plătești National Insurance, dar anul contează pentru pensia de stat.',RT[2]),
  ('National Insurance','£129','Low earnings can still build your pension',['Between £129 and £242 a week: no NI to pay','The year still counts for State Pension','Below £129 a week it does not'],
  'Employees earning between £129 and £242 a week pay no NI, yet the year still counts towards the State Pension.',ET[0],
  'Earning £129-£242 a week? No employee NI, but the year still counts for State Pension.'))
t(D,'lump-sum-268k',None,('Pensions','£268,275','Tax-free pension cash: the limit',['Lump Sum Allowance: £268,275','Unchanged for 2026-27 and 2027-28','Usually up to 25% of your pension'],
  'The Lump Sum Allowance, the usual cap on tax-free pension cash, stays at £268,275 in 2026 to 2027 and 2027 to 2028.',ET[0],
  'Lump Sum Allowance stays £268,275 in 2026-27 and 2027-28.'),extra=True)

if __name__ == "__main__":
    plan, ro, en = [], [], []
    for d in DAYS:
        assert len(PLAN[d]) == 14, (d, len(PLAN[d])); assert d in EXTRA, d
        plan.append({"day": d, "items": PLAN[d], "extra": EXTRA[d]})
        for k in PLAN[d] + [EXTRA[d]]:
            x = T[k]; mmdd = d[5:]
            if k != EXTRA[d]:
                tag, fig, head, lines, cap, tags = x['ro']
                ro.append({"id": f"ro-{mmdd}-{k}", "tag": tag, "figure": fig, "headline": head, "lines": lines,
                           "caption": f"{cap}\n\nScrie-ne pe WhatsApp la 0330 133 1886. Birouri în Luton și Birmingham.\n\n{tags}", "day": d, "k": k})
            tag, fig, head, lines, cap, tags, bs = x['en']
            en.append({"id": f"en-{mmdd}-{k}", "tag": tag, "figure": fig, "headline": head, "lines": lines,
                       "caption": f"{cap}\n\nMessage us on WhatsApp: 0330 133 1886. Offices in Luton and Birmingham.\n\n{tags}",
                       "bsky": bs, "day": d, "k": k, "wa": "Message us on WhatsApp", "disc": "General information only. Speak to an accountant about your situation."})
    json.dump(plan, open("week_plan.json", "w"), ensure_ascii=False, indent=1)
    json.dump(ro, open("week_ro.json", "w"), ensure_ascii=False, indent=0)
    json.dump(en, open("week_en.json", "w"), ensure_ascii=False, indent=0)
    print("plan days", len(plan), "ro", len(ro), "en", len(en), "keys", len(T))
