# Week 23-29 Oct 2026 topics. Facts checked on GOV.UK on 22 Oct 2026 (see sources in approval page).
RT = "#hmrc #romaniinuk #contabilromania"
ET = "#UKTax #HMRC"
T = []
def t(k, ro, en):
    T.append(dict(k=k, ro=ro, en=en))

# ---------- Self Assessment ----------
t('sa-paper', ('Self Assessment','31 oct.','Depui declarația pe hârtie? Termenul e 31 octombrie',['Declarația pe hârtie pentru 2025–26: 31 octombrie 2026','Online ai timp până la 31 ianuarie 2027','Plata impozitului: tot 31 ianuarie 2027'],
  'Dacă depui declarația Self Assessment pe hârtie, termenul pentru anul 2025–26 este 31 octombrie 2026. Online ai timp până la 31 ianuarie 2027.', RT),
  ('Self Assessment','31 Oct','Filing on paper? Your deadline is 31 October',['Paper returns for 2025–26: 31 October 2026','Online returns: 31 January 2027','Tax payment: also 31 January 2027'],
  'Filing your 2025–26 Self Assessment return on paper? The deadline is 31 October 2026. Online, you have until 31 January 2027.', ET,
  'Paper Self Assessment returns for 2025–26 are due 31 October 2026. Online: 31 January 2027.'))
t('sa-register', ('Înregistrare','5 oct.','Ai devenit self-employed? Te înregistrezi până pe 5 octombrie',['Termenul: 5 octombrie după sfârșitul anului fiscal','Pentru anul 2026–27: până la 5 octombrie 2027','Primești UTR-ul prin poștă sau în cont online'],
  'Dacă ai început să lucrezi pe cont propriu, trebuie să te înregistrezi pentru Self Assessment până la 5 octombrie după sfârșitul anului fiscal în care ai început.', RT),
  ('Registration','5 Oct','Just gone self-employed? Register by 5 October',['Deadline: 5 October after the tax year ends','For 2026–27: by 5 October 2027','Your UTR arrives by post or in your online account'],
  'Started working for yourself? Register for Self Assessment by 5 October after the end of the tax year you started in.', ET,
  'Started self-employment? Register for Self Assessment by 5 October after the end of that tax year.'))
t('sa-late-file', ('Amenzi','£100','Ce se întâmplă dacă depui declarația târziu',['O zi întârziere: £100','După 3 luni: £10 pe zi, până la £900','După 6 luni: încă 5% din impozit sau £300'],
  'Amenzile pentru declarația Self Assessment depusă târziu cresc rapid: £100 din prima zi, apoi £10 pe zi după 3 luni și încă 5% sau £300 după 6 luni.', RT),
  ('Penalties','£100','What happens if you file your tax return late',['One day late: £100','After 3 months: £10 a day, up to £900','After 6 months: another 5% of the tax or £300'],
  'Late Self Assessment penalties add up fast: £100 from day one, £10 a day after 3 months, then another 5% or £300 after 6 months.', ET,
  'Late tax return? £100 from day one, £10 a day after 3 months (up to £900), then 5% or £300 after 6 months.'))
t('sa-late-pay', ('Plata târzie','5%','Ai depus, dar n-ai plătit? Se adaugă penalități',['5% din impozitul neplătit după 30 de zile','Încă 5% la 6 luni și la 12 luni','Plus dobândă pentru fiecare zi'],
  'Chiar dacă ai depus declarația la timp, plata întârziată aduce penalități de 5% la 30 de zile, la 6 luni și la 12 luni, plus dobândă.', RT),
  ('Late payment','5%','Filed on time but paid late? Penalties apply',['5% of unpaid tax after 30 days','Another 5% at 6 months and at 12 months','Plus daily interest'],
  'Filing on time is not enough. Paying late adds 5% penalties at 30 days, 6 months and 12 months, plus interest.', ET,
  'Paid your Self Assessment late? 5% penalties at 30 days, 6 months and 12 months, plus interest.'))
t('sa-utr', ('UTR','10 cifre','Ce este UTR-ul și de unde îl iei',['Unique Taxpayer Reference: 10 cifre','Îl primești după înregistrarea la HMRC','Îl găsești în contul online HMRC sau în aplicație'],
  'UTR-ul este numărul tău de contribuabil la HMRC, format din 10 cifre. Îți trebuie la fiecare declarație și când vorbești cu HMRC.', RT),
  ('UTR','10 digits','What is a UTR and where do you find it?',['Unique Taxpayer Reference: 10 digits','You get it after registering with HMRC','Find it in your HMRC online account or the HMRC app'],
  'Your UTR is your 10-digit taxpayer reference. You need it for every tax return and whenever you speak to HMRC.', ET,
  'Your UTR is a 10-digit number from HMRC. Find it in your online account or the HMRC app.'))
t('sa-docs', ('Self Assessment','Checklist','Ce acte pregătești pentru declarație',['P60 sau P45, dacă ai avut și job','Extrase de cont și facturi','Bonuri pentru cheltuieli și evidența milelor'],
  'Ca să-ți facem declarația repede și corect, pregătește P60 sau P45, extrasele de cont, facturile și bonurile pentru cheltuieli.', RT),
  ('Self Assessment','Checklist','What to gather for your tax return',['P60 or P45 if you also had a job','Bank statements and sales invoices','Expense receipts and your mileage log'],
  'To get your return done quickly and correctly, gather your P60 or P45, bank statements, invoices and expense receipts.', ET,
  'Tax return checklist: P60/P45, bank statements, invoices, expense receipts and your mileage log.'))
t('sa-amend', ('Corecturi','12 luni','Ai greșit ceva în declarație? Se poate corecta',['Poți modifica declarația online','Ai 12 luni de la termenul de 31 ianuarie','Corectează repede, înainte să te întrebe HMRC'],
  'Ai descoperit o greșeală în declarația depusă? O poți corecta online în 12 luni de la termenul de 31 ianuarie.', RT),
  ('Amendments','12 months','Made a mistake on your tax return? You can fix it',['You can amend your return online','You have 12 months from the 31 January deadline','Fix it before HMRC asks'],
  'Spotted a mistake on a return you already filed? You can amend it online within 12 months of the 31 January deadline.', ET,
  'Mistake on your tax return? Amend it online within 12 months of the 31 January deadline.'))
t('sa-who', ('Self Assessment','Cine?','Cine trebuie să depună declarație',['Self-employed cu venit peste £1.000','Cei cu venituri din chirii sau din străinătate','Cei care primesc Child Benefit și câștigă peste £60.000'],
  'Nu doar self-employed-ii depun Self Assessment. Și cei cu chirii, venituri din străinătate sau Child Benefit peste prag trebuie să o facă.', RT),
  ('Self Assessment','Who?','Who needs to file a tax return',['Self-employed with income over £1,000','People with rental or foreign income','Child Benefit claimants earning over £60,000'],
  "It's not just the self-employed. Landlords, people with foreign income and higher earners on Child Benefit may also need to file.", ET,
  'Who files Self Assessment? Self-employed over £1,000, landlords, foreign income, and Child Benefit over £60,000.'))
t('sa-plan', ('Plata impozitului','Plan','Nu poți plăti tot impozitul deodată?',['Poți cere un plan de plată la HMRC','HMRC verifică dacă planul e realist','Nu ignora datoria: penalitățile cresc'],
  'Dacă nu poți plăti tot impozitul pe 31 ianuarie, poți cere la HMRC un plan de plată în rate. Cel mai rău e să nu faci nimic.', RT),
  ('Paying your tax','Plan','Can\'t pay your tax bill in full?',['You can ask HMRC for a payment plan','HMRC checks the plan is affordable','Ignoring the debt only adds penalties'],
  "Can't pay your full tax bill by 31 January? You can ask HMRC for a payment plan. Doing nothing is the costly option.", ET,
  "Can't pay your tax bill in full? Ask HMRC for a payment plan before penalties build up."))
t('sa-dates', ('Calendar fiscal','4 date','Datele pe care un self-employed nu le uită',['31 ianuarie: declarația online și plata','31 iulie: a doua plată în avans','5 octombrie: înregistrarea; 31 octombrie: pe hârtie'],
  'Pune-ți în calendar datele importante: 31 ianuarie, 31 iulie, 5 octombrie și 31 octombrie. Așa scapi de amenzi.', RT),
  ('Tax calendar','4 dates','The dates every sole trader should know',['31 January: online return and payment','31 July: second payment on account','5 October: register; 31 October: paper return'],
  'Put these in your calendar: 31 January, 31 July, 5 October and 31 October. It is the simplest way to avoid penalties.', ET,
  'Key dates: 31 Jan (file and pay), 31 Jul (2nd payment on account), 5 Oct (register), 31 Oct (paper).'))
# ---------- Expenses ----------
t('exp-yes', ('Cheltuieli','Deductibil','Alte cheltuieli pe care le poți scădea',['Echipamente: laptop, scule, telefon','Publicitate și site','Onorariul contabilului'],
  'Pe lângă combustibil și telefon, poți deduce echipamentele de lucru, publicitatea și chiar onorariul contabilului.', RT),
  ('Expenses','Allowable','More expenses you can claim',['Equipment: laptop, tools, phone','Advertising and your website','Your accountant\'s fees'],
  'Beyond fuel and phone bills, you can claim work equipment, advertising and even your accountant\'s fees.', ET,
  'Sole trader? You can also claim equipment, advertising, your website and accountancy fees.'))
t('exp-no', ('Cheltuieli','Nedeductibil','Ce NU poți scădea din venit',['Drumul zilnic de acasă la locul de muncă','Hainele obișnuite și mesele zilnice','Amenzile de parcare sau de viteză'],
  'Atenție la cheltuielile care nu se deduc: naveta zilnică, hainele obișnuite, mesele de zi cu zi și amenzile.', RT),
  ('Expenses','Not allowable','What you CAN\'T claim as an expense',['Your daily commute to a regular workplace','Everyday clothes and daily meals','Parking and speeding fines'],
  'Watch out for costs HMRC won\'t accept: your normal commute, everyday clothes, daily meals and fines.', ET,
  "Not allowable: your daily commute, everyday clothes, daily meals and fines."))
t('exp-aia', ('Echipamente','£1.000.000','Cumperi echipamente pentru afacere?',['Annual Investment Allowance: până la £1 milion pe an','Scazi tot costul în anul în care cumperi','Mașinile au reguli separate'],
  'Prin Annual Investment Allowance poți scădea tot costul echipamentelor (până la £1 milion pe an) în anul cumpărării. Mașinile au reguli separate.', RT),
  ('Equipment','£1,000,000','Buying equipment for your business?',['Annual Investment Allowance: up to £1 million a year','Deduct the full cost in the year you buy','Cars follow different rules'],
  'The Annual Investment Allowance lets you deduct the full cost of business equipment, up to £1 million a year, in the year you buy it.', ET,
  'Annual Investment Allowance: deduct up to £1m of equipment in the year you buy it. Cars have separate rules.'))
t('exp-cash', ('Cash basis','Standard','Cash basis: evidența cea mai simplă',['Înregistrezi banii când intră și ies din cont','Este metoda standard pentru self-employed','Poți alege totuși contabilitatea tradițională'],
  'Pentru self-employed, cash basis este acum metoda standard: înregistrezi venitul și cheltuiala când banii intră sau ies efectiv.', RT),
  ('Cash basis','Standard','Cash basis: the simplest way to keep records',['Record money when it actually comes in or goes out','It is now the standard for sole traders','You can still opt for traditional accounting'],
  'For sole traders, cash basis is now the standard: you record income and expenses when the money actually moves.', ET,
  'Cash basis is now the standard for sole traders: record money when it actually comes in or goes out.'))
t('exp-training', ('Cursuri','Atenție','Cursurile se deduc? Depinde',['Da: cursuri care îți actualizează meseria actuală','Nu: cursuri pentru o meserie nouă','Păstrează factura și programul cursului'],
  'Un curs care îți îmbunătățește meseria actuală se poate deduce. Unul pentru o meserie nouă, de obicei nu.', RT),
  ('Training','Careful','Can you claim training costs? It depends',['Yes: courses that update your current skills','No: training for a brand-new trade','Keep the invoice and course outline'],
  'Training that updates the skills you already use can be claimed. Training for a completely new trade usually can\'t.', ET,
  'Training costs: claimable if they update skills for your current trade, not for a new one.'))
t('exp-mileage-log', ('Mile','Jurnal','Ține un jurnal al milelor de business',['Data, de unde, unde și de ce','Totalul milelor de afaceri','Fără jurnal, HMRC poate respinge deducerea'],
  'Ca să deduci milele (55p pe milă pentru primele 10.000), ai nevoie de un jurnal simplu: data, traseul, motivul și milele.', RT),
  ('Mileage','Log','Keep a business mileage log',['Date, start, destination and purpose','Total business miles','No log, and HMRC can refuse the claim'],
  'To claim mileage (55p a mile for the first 10,000), keep a simple log: date, route, purpose and miles.', ET,
  'Claiming mileage? Keep a log: date, route, purpose, miles. 55p/mile for the first 10,000.'))
t('exp-separate', ('Sfat','1 cont','Folosește un cont bancar separat pentru afacere',['Vezi clar ce e venit și ce e cheltuială','Declarația se face mai repede','Ești pregătit dacă HMRC cere dovezi'],
  'Un cont bancar separat pentru afacere te scapă de stres: totul e clar, iar declarația se face mai repede și mai ieftin.', RT),
  ('Tip','1 account','Use a separate bank account for your business',['See clearly what is income and what is expense','Your tax return gets quicker','You are ready if HMRC asks for evidence'],
  'A separate business bank account keeps everything clear and makes your tax return quicker and cheaper.', ET,
  'Tip: a separate business bank account makes your tax return quicker and HMRC checks easier.'))
t('exp-save', ('Sfat','Lunar','Pune deoparte bani pentru impozit în fiecare lună',['Impozitul vine o dată sau de două ori pe an','O sumă lunară te scapă de șocul din ianuarie','Ține-i într-un cont separat de economii'],
  'Cel mai mare șoc pentru self-employed e factura din ianuarie. Pune deoparte o sumă lunar, într-un cont separat.', RT),
  ('Tip','Monthly','Set money aside for tax every month',['Tax is paid once or twice a year','A monthly amount avoids the January shock','Keep it in a separate savings account'],
  'The biggest shock for sole traders is the January bill. Set money aside every month in a separate account.', ET,
  'Tip: set aside money for tax every month so January doesn\'t hurt.'))
t('exp-invoice', ('Facturi','5 detalii','Ce trebuie să conțină o factură',['Număr unic de factură și data','Numele și adresa ta și a clientului','Ce ai făcut și suma de plată'],
  'O factură corectă are: număr unic, dată, datele tale și ale clientului, descrierea serviciului și suma.', RT),
  ('Invoices','5 details','What every invoice needs',['A unique invoice number and date','Your name and address, and the customer\'s','What you did and the amount due'],
  'A proper invoice has a unique number, date, your details and the customer\'s, a description and the amount due.', ET,
  'Every invoice needs: unique number, date, your and your customer\'s details, description, amount.'))
# ---------- MTD ----------
t('mtd-7nov', ('Making Tax Digital','7 nov.','Ești în MTD? Următorul raport e pe 7 noiembrie',['7 noiembrie 2026: al doilea raport trimestrial','Apoi 7 februarie și 7 mai 2027','Totul se trimite din software compatibil'],
  'Dacă ești în Making Tax Digital, al doilea raport trimestrial pentru 2026–27 trebuie trimis până la 7 noiembrie 2026.', RT),
  ('Making Tax Digital','7 Nov','In MTD? Your next update is due 7 November',['7 November 2026: second quarterly update','Then 7 February and 7 May 2027','Everything goes through compatible software'],
  'If you are in Making Tax Digital, your second quarterly update for 2026–27 is due by 7 November 2026.', ET,
  'Making Tax Digital: second quarterly update due 7 November 2026, then 7 Feb and 7 May 2027.'))
t('mtd-software', ('Making Tax Digital','Software','De ce ai nevoie pentru MTD',['Software compatibil cu HMRC','Evidențe digitale pentru venituri și cheltuieli','Rapoarte de 4 ori pe an, plus declarația finală'],
  'Pentru MTD nu mai merge doar cu caietul: ai nevoie de software compatibil și de evidențe digitale ținute pe tot parcursul anului.', RT),
  ('Making Tax Digital','Software','What you need for Making Tax Digital',['HMRC-compatible software','Digital records of income and expenses','4 quarterly updates plus a final declaration'],
  'MTD means compatible software and digital records kept through the year, not a shoebox of receipts in January.', ET,
  'MTD needs HMRC-compatible software, digital records and 4 quarterly updates a year.'))
t('mtd-30k', ('Making Tax Digital','£30.000','Din aprilie 2027, MTD pentru încasări peste £30.000',['Acum: peste £50.000 încasări brute','Din aprilie 2027: peste £30.000','Din aprilie 2028: peste £20.000'],
  'Pragul pentru Making Tax Digital scade: din aprilie 2027 intră și cei cu încasări de peste £30.000. Pregătește-te din timp.', RT),
  ('Making Tax Digital','£30,000','From April 2027, MTD applies over £30,000',['Now: gross income over £50,000','From April 2027: over £30,000','From April 2028: over £20,000'],
  'The MTD threshold is falling: from April 2027 it covers gross income over £30,000. Get ready early.', ET,
  'Making Tax Digital threshold drops to £30,000 in April 2027 and £20,000 in April 2028.'))
t('mtd-final', ('Making Tax Digital','31 ian. 2028','Prima declarație finală MTD',['Pentru anul 2026–27','Se trimite din software-ul MTD','Termen: 31 ianuarie 2028'],
  'Pe lângă cele 4 rapoarte, cei din MTD trimit o declarație finală pentru 2026–27 până la 31 ianuarie 2028, direct din software.', RT),
  ('Making Tax Digital','31 Jan 2028','Your first MTD final declaration',['For the 2026–27 tax year','Submitted from your MTD software','Deadline: 31 January 2028'],
  'As well as the 4 updates, MTD users submit a final declaration for 2026–27 by 31 January 2028, straight from their software.', ET,
  'MTD final declaration for 2026–27 is due 31 January 2028, from your MTD software.'))
# ---------- Property ----------
t('prop-allow', ('Chirii','£1.000','Câștigi puțin din închiriere?',['Primii £1.000 pe an sunt acoperiți de property allowance','Peste, trebuie să declari','Nu poți folosi și allowance, și cheltuieli reale'],
  'Dacă venitul din proprietăți e mic, primii £1.000 pe an sunt acoperiți de property allowance.', RT),
  ('Property','£1,000','Earning a little from property?',['The first £1,000 a year is covered by the property allowance','Above that, you must declare it','You can\'t use the allowance and actual expenses together'],
  'If your property income is small, the first £1,000 a year is covered by the property allowance.', ET,
  'Property allowance: the first £1,000 a year of property income is tax-free.'))
t('prop-room', ('Rent a Room','£7.500','Închiriezi o cameră în casa ta?',['Până la £7.500 pe an fără impozit','£3.750 fiecare dacă împărțiți venitul','Camera trebuie să fie mobilată, în casa în care locuiești'],
  'Prin schema Rent a Room poți câștiga până la £7.500 pe an fără impozit din închirierea unei camere mobilate în casa ta.', RT),
  ('Rent a Room','£7,500','Renting out a room in your home?',['Up to £7,500 a year tax-free','£3,750 each if you share the income','A furnished room in the home you live in'],
  'Under Rent a Room you can earn up to £7,500 a year tax-free from a furnished room in your own home.', ET,
  'Rent a Room scheme: up to £7,500 a year tax-free (£3,750 if shared).'))
t('prop-interest', ('Proprietari','20%','Dobânda la ipotecă pentru casa închiriată',['Nu se mai scade direct din chirie','Primești o reducere de impozit de 20%','Contează mult dacă plătești rata superioară'],
  'Pentru proprietarii individuali, dobânda la ipotecă nu se mai scade din chirie: primești o reducere de impozit de 20%.', RT),
  ('Landlords','20%','Mortgage interest on a rental property',['It is no longer deducted from rent','You get a 20% tax reduction instead','This matters most for higher-rate taxpayers'],
  'For individual landlords, mortgage interest isn\'t deducted from rent any more. You get a 20% tax reduction instead.', ET,
  'Landlords: mortgage interest gives a 20% tax reduction, not a deduction from rent.'))
t('prop-exp', ('Proprietari','Cheltuieli','Ce poți scădea din chirii',['Reparații și întreținere (nu îmbunătățiri)','Comisionul agentului și asigurarea','Certificatele obligatorii: gaz, electric'],
  'Din chirii poți scădea reparațiile, comisionul agentului, asigurarea și certificatele obligatorii. Îmbunătățirile au alte reguli.', RT),
  ('Landlords','Expenses','What landlords can claim',['Repairs and maintenance (not improvements)','Letting agent fees and insurance','Required safety certificates'],
  'Landlords can claim repairs, agent fees, insurance and safety certificates. Improvements follow different rules.', ET,
  'Landlords can claim repairs, agent fees, insurance and safety certificates; improvements differ.'))
t('cgt-60', ('Capital Gains Tax','60 zile','Vinzi o proprietate care nu e casa ta?',['Raportezi la HMRC în 60 de zile','Și plătești impozitul tot în 60 de zile','Se aplică pentru proprietăți rezidențiale din UK'],
  'Dacă vinzi în UK o proprietate rezidențială care nu e casa ta principală, ai 60 de zile să raportezi și să plătești Capital Gains Tax.', RT),
  ('Capital Gains Tax','60 days','Selling a property that isn\'t your home?',['Report the sale to HMRC within 60 days','Pay the tax within the same 60 days','Applies to UK residential property'],
  'Selling UK residential property that isn\'t your main home? You have 60 days to report and pay Capital Gains Tax.', ET,
  'Sold a UK residential property that isn\'t your home? Report and pay CGT within 60 days.'))
t('cgt-rates', ('Capital Gains Tax','£3.000','Câștig din vânzare: cât impozit plătești',['Primii £3.000 de câștig pe an sunt scutiți','18% pentru rata de bază','24% pentru rata superioară'],
  'Pentru câștigurile din vânzarea de bunuri, primii £3.000 pe an sunt scutiți. Peste, plătești 18% sau 24%.', RT),
  ('Capital Gains Tax','£3,000','Capital Gains Tax: how much you pay',['First £3,000 of gains each year is tax-free','18% within the basic rate band','24% above it'],
  'The first £3,000 of gains each year is tax-free. Above that, Capital Gains Tax is 18% or 24%.', ET,
  'CGT 2026–27: £3,000 tax-free, then 18% (basic rate band) or 24%.'))
# ---------- Limited companies ----------
t('ltd-accounts', ('Firme LTD','9 luni','Termenul pentru conturile anuale',['Conturile la Companies House: 9 luni după an','Primele conturi: 21 de luni de la înființare','Întârzierea aduce amenzi automate'],
  'Conturile anuale ale firmei se depun la Companies House în 9 luni de la sfârșitul anului financiar. Primele: 21 de luni de la înființare.', RT),
  ('Limited companies','9 months','Your annual accounts deadline',['Companies House: 9 months after year end','First accounts: 21 months after incorporation','Late filing means automatic penalties'],
  'Annual accounts are due at Companies House 9 months after your financial year end. First accounts: 21 months after incorporation.', ET,
  'Company accounts are due at Companies House 9 months after year end (first accounts: 21 months).'))
t('ltd-ct-pay', ('Firme LTD','9 luni + 1 zi','Când plătește firma Corporation Tax',['Plata: 9 luni și o zi după anul fiscal','Declarația CT600: 12 luni după','Plata vine înaintea declarației'],
  'Corporation Tax se plătește în 9 luni și o zi după sfârșitul perioadei contabile, chiar dacă declarația are termen 12 luni.', RT),
  ('Limited companies','9 months + 1 day','When your company pays Corporation Tax',['Payment: 9 months and 1 day after year end','Company Tax Return: 12 months after','Payment comes before the return'],
  'Corporation Tax is due 9 months and 1 day after your accounting period ends, even though the return is due at 12 months.', ET,
  'Corporation Tax: pay 9 months + 1 day after year end; file the return within 12 months.'))
t('ltd-cs', ('Firme LTD','1 dată pe an','Confirmation statement: nu-l uita',['Se depune cel puțin o dată la 12 luni','Confirmi directorii, acționarii, adresa','Dacă nu-l depui, firma poate fi radiată'],
  'Confirmation statement-ul se depune la Companies House cel puțin o dată la 12 luni. Dacă îl ignori, firma poate fi radiată.', RT),
  ('Limited companies','Once a year','Don\'t forget your confirmation statement',['File at least once every 12 months','Confirm directors, shareholders and address','Ignore it and the company can be struck off'],
  'Your confirmation statement goes to Companies House at least every 12 months. Ignore it and the company can be struck off.', ET,
  'Limited company? File your confirmation statement at least every 12 months.'))
t('ltd-dla', ('Firme LTD','Atenție','Bani scoși din firmă fără salariu sau dividend',['Se trec ca împrumut de la firmă (director\'s loan)','Dacă nu-l returnezi la timp, firma plătește taxă','Ține evidența fiecărei sume'],
  'Banii pe care îi iei din firmă, dar care nu sunt salariu sau dividend, sunt un împrumut. Nereturnat la timp, aduce taxă suplimentară firmei.', RT),
  ('Limited companies','Careful','Taking money out of your company?',['If it isn\'t salary or dividend, it\'s a director\'s loan','Not repaid in time, and the company pays extra tax','Keep a record of every amount'],
  'Money you take that isn\'t salary or dividends is a director\'s loan. If it isn\'t repaid in time, the company pays extra tax.', ET,
  "Director's loan: money taken that isn't salary or dividends. Repay it in time to avoid extra tax."))
t('ltd-div-profit', ('Dividende','Profit','Dividende doar din profit',['Dividendele se plătesc doar din profit acumulat','Fără profit, nu sunt dividende legale','Păstrează procesul-verbal al deciziei'],
  'Dividendele se pot plăti doar din profitul firmei. Fără profit disponibil, banii scoși nu sunt dividende.', RT),
  ('Dividends','Profits','Dividends only come from profits',['Dividends can only be paid from available profits','No profits, no legal dividend','Keep minutes of each dividend decision'],
  'Dividends can only be paid from your company\'s available profits. No profits, no lawful dividend.', ET,
  'Dividends must come from available company profits. Keep minutes and vouchers.'))
t('ltd-trivial', ('Beneficii','£50','Cadouri mici pentru angajați, fără taxe',['Maximum £50 per cadou, nu în bani','Nu ca recompensă pentru muncă','Directorii: maximum £300 pe an'],
  'Trivial benefits: poți oferi cadouri de până la £50 fără taxe, dacă nu sunt bani sau recompensă. Directorii au limită de £300 pe an.', RT),
  ('Benefits','£50','Small tax-free gifts for staff',['Up to £50 per gift, not cash','Not a reward for work','Directors of small companies: £300 a year cap'],
  'Trivial benefits let you give gifts of up to £50 tax-free, as long as they aren\'t cash or a reward. Directors have a £300 yearly cap.', ET,
  'Trivial benefits: tax-free gifts up to £50 each (not cash). Directors capped at £300 a year.'))
t('ltd-party', ('Firme LTD','£150','Petrecerea de Crăciun a firmei',['Până la £150 de persoană pe an, fără taxe','Trebuie să fie deschisă tuturor angajaților','Peste limită, devine beneficiu impozabil'],
  'Petrecerea anuală a firmei poate fi fără taxe până la £150 de persoană pe an, dacă e deschisă tuturor angajaților.', RT),
  ('Limited companies','£150','Your company Christmas party',['Up to £150 per head a year, tax-free','It must be open to all staff','Go over and it becomes a taxable benefit'],
  'Your annual staff party can be tax-free up to £150 per head a year, as long as it is open to all employees.', ET,
  'Staff Christmas party: tax-free up to £150 per head a year if open to all employees.'))
t('ltd-or-se', ('LTD sau self-employed?','Depinde','LTD nu înseamnă automat impozit mai mic',['Contează profitul și cum scoți banii','LTD are mai multe obligații și costuri','Calculul se face pe situația ta'],
  'Firma LTD nu e întotdeauna mai avantajoasă. Depinde de profit, de cum îți iei banii și de costurile în plus. Hai să facem calculul.', RT),
  ('Ltd or sole trader?','It depends','A limited company doesn\'t always mean less tax',['Profit level and how you take money both matter','A company has more duties and costs','Work it out for your own situation'],
  'A limited company isn\'t always cheaper. It depends on your profit, how you take money out and the extra costs.', ET,
  'Ltd or sole trader? It depends on profit, how you take money out and the extra admin.'))
t('ltd-address', ('Firme LTD','Public','Adresa de pe Companies House e publică',['Registrul Companies House e public','Poți folosi o adresă de serviciu','Protejează-ți adresa de acasă'],
  'Datele firmei de pe Companies House sunt publice. Folosește o adresă de serviciu ca să-ți protejezi adresa de acasă.', RT),
  ('Limited companies','Public','Your Companies House address is public',['The Companies House register is public','You can use a service address','Keep your home address private'],
  'Companies House records are public. Use a service address to keep your home address private.', ET,
  'Companies House is public: use a service address to protect your home address.'))
t('badr', ('Vânzarea afacerii','18%','Vinzi afacerea? Business Asset Disposal Relief',['Impozit de 18% pe câștigurile eligibile','Pentru self-employed, parteneri și unii acționari','Condițiile trebuie verificate din timp'],
  'La vânzarea afacerii, Business Asset Disposal Relief poate reduce Capital Gains Tax la 18% pe câștigurile eligibile.', RT),
  ('Selling a business','18%','Selling your business? Business Asset Disposal Relief',['18% tax on qualifying gains','For sole traders, partners and some shareholders','Check the conditions early'],
  'When you sell your business, Business Asset Disposal Relief can bring Capital Gains Tax down to 18% on qualifying gains.', ET,
  'Selling a business? Business Asset Disposal Relief: 18% CGT on qualifying gains.'))
# ---------- VAT ----------
t('vat-deadline', ('TVA','1 lună + 7 zile','Termenul pentru declarația de TVA',['La 1 lună și 7 zile după trimestru','Plata are același termen','Nu se prelungește în weekend'],
  'Declarația de TVA și plata au același termen: o lună și 7 zile după sfârșitul perioadei. Banii trebuie să ajungă la HMRC până atunci.', RT),
  ('VAT','1 month + 7 days','Your VAT return deadline',['1 month and 7 days after the period ends','Payment is due the same day','No extension for weekends'],
  'Your VAT return and payment are both due 1 month and 7 days after the period ends. The money must reach HMRC by then.', ET,
  'VAT return and payment: due 1 month and 7 days after the period ends.'))
t('vat-mtd', ('TVA','MTD','Toate firmele cu TVA sunt în Making Tax Digital',['Evidențe digitale pentru TVA','Declarații trimise din software compatibil','Indiferent de cifra de afaceri'],
  'Orice afacere înregistrată pentru TVA trebuie să țină evidențe digitale și să trimită declarațiile din software compatibil.', RT),
  ('VAT','MTD','Every VAT-registered business is in Making Tax Digital',['Digital VAT records','Returns sent from compatible software','Whatever your turnover'],
  'Every VAT-registered business must keep digital records and file VAT returns through compatible software.', ET,
  'All VAT-registered businesses must use Making Tax Digital for VAT.'))
t('vat-voluntary', ('TVA','Voluntar','Merită să te înregistrezi pentru TVA voluntar?',['Poți recupera TVA-ul de la furnizori','Clienții firme pot recupera TVA-ul tău','Clienții persoane fizice plătesc mai mult'],
  'Înregistrarea voluntară pentru TVA poate avea sens dacă lucrezi cu firme. Dacă vinzi la persoane fizice, prețul pentru ele crește.', RT),
  ('VAT','Voluntary','Should you register for VAT voluntarily?',['You can reclaim VAT on your costs','Business customers can reclaim your VAT','Private customers end up paying more'],
  'Voluntary VAT registration can make sense if you sell to businesses. If you sell to the public, prices go up for them.', ET,
  'Voluntary VAT registration: good for B2B, can cost you with private customers.'))
t('vat-flat', ('TVA','Flat Rate','Flat Rate Scheme pe scurt',['Plătești un procent fix din încasări','Limited cost traders: 16,5%','Nu recuperezi TVA-ul pe majoritatea cheltuielilor'],
  'Flat Rate Scheme simplifică TVA-ul: plătești un procent fix din încasări. Dacă ai cheltuieli mici cu bunuri, procentul e 16,5%.', RT),
  ('VAT','Flat Rate','The VAT Flat Rate Scheme in brief',['You pay a fixed % of your gross turnover','Limited cost traders: 16.5%','You can\'t reclaim VAT on most costs'],
  'The Flat Rate Scheme simplifies VAT: you pay a fixed percentage of turnover. Limited cost traders pay 16.5%.', ET,
  'VAT Flat Rate Scheme: fixed % of turnover; limited cost traders pay 16.5%.'))
t('vat-invoice', ('TVA','Facturi','Factura cu TVA: ce trebuie să aibă',['Numărul tău de TVA','Suma fără TVA, cota și TVA-ul','Data și numărul unic al facturii'],
  'O factură cu TVA trebuie să conțină numărul tău de TVA, suma fără TVA, cota aplicată și valoarea TVA-ului.', RT),
  ('VAT','Invoices','What a VAT invoice must show',['Your VAT registration number','Net amount, VAT rate and VAT charged','Invoice date and unique number'],
  'A VAT invoice must show your VAT number, the net amount, the VAT rate and the VAT charged.', ET,
  'VAT invoice must show: VAT number, net amount, rate, VAT charged, date and invoice number.'))
# ---------- Employers ----------
t('nmw-21', ('Salariu minim','£12,71','Salariul minim din aprilie 2026',['21 de ani și peste: £12,71 pe oră','18–20 de ani: £10,85 pe oră','Sub 18 ani și ucenici: £8 pe oră'],
  'Din aprilie 2026, salariul minim pe oră este £12,71 pentru cei de 21 de ani și peste. Angajatorii trebuie să-l respecte.', RT),
  ('Minimum wage','£12.71','The minimum wage from April 2026',['21 and over: £12.71 an hour','18 to 20: £10.85 an hour','Under 18 and apprentices: £8 an hour'],
  'Since April 2026 the National Living Wage is £12.71 an hour for workers aged 21 and over.', ET,
  'Minimum wage from April 2026: £12.71 (21+), £10.85 (18–20), £8 (under 18 and apprentices).'))
t('ssp', ('Concediu medical','Din prima zi','Statutory Sick Pay din aprilie 2026',['Se plătește din prima zi de boală','£123,25 pe săptămână sau 80% din câștig','Se aplică suma mai mică'],
  'Din aprilie 2026, Statutory Sick Pay se plătește din prima zi de boală: £123,25 pe săptămână sau 80% din câștigul mediu, cât e mai puțin.', RT),
  ('Sick pay','Day one','Statutory Sick Pay from April 2026',['Paid from the first day of sickness','£123.25 a week or 80% of earnings','Whichever is lower'],
  'Since April 2026, SSP is paid from day one: £123.25 a week or 80% of average weekly earnings, whichever is lower.', ET,
  'SSP from April 2026: paid from day one, £123.25/week or 80% of earnings, whichever is lower.'))
t('pension-ae', ('Pensie','8%','Pensia automată a angajaților',['Minimum 8% din câștigul eligibil','Angajatorul: cel puțin 3%','Angajatul: restul, de obicei 5%'],
  'Prin auto-enrolment, contribuția minimă la pensie este 8%: cel puțin 3% de la angajator, restul de la angajat.', RT),
  ('Pensions','8%','Workplace pension minimums',['8% of qualifying earnings in total','Employer: at least 3%','Employee: the rest, usually 5%'],
  'Under auto-enrolment, the minimum total pension contribution is 8%, with at least 3% from the employer.', ET,
  'Auto-enrolment: 8% minimum total, at least 3% from the employer.'))
t('rti', ('Payroll','Ziua plății','Raportarea salariilor la HMRC',['Trimiți FPS la sau înainte de ziua plății','Pentru fiecare plată, nu doar lunar','Întârzierile aduc penalități'],
  'Ca angajator, trimiți la HMRC raportul FPS la sau înainte de fiecare zi de plată a salariilor.', RT),
  ('Payroll','Payday','Reporting payroll to HMRC',['Send an FPS on or before payday','For every payment, not just monthly','Late reports can bring penalties'],
  'As an employer, you send HMRC a Full Payment Submission on or before every payday.', ET,
  'Employers: send your FPS to HMRC on or before every payday.'))
t('p60', ('Payroll','31 mai','Angajatorii dau P60 până la 31 mai',['P60 arată salariul și impozitul pe an','Fiecare angajat activ pe 5 aprilie îl primește','Păstrează-l: îți trebuie la declarații și credite'],
  'Angajatorii trebuie să dea fiecărui angajat formularul P60 până la 31 mai. Păstrează-l, îți trebuie mai târziu.', RT),
  ('Payroll','31 May','Employers must give a P60 by 31 May',['P60 shows a year\'s pay and tax','Every employee on payroll at 5 April gets one','Keep it for tax returns and loans'],
  'Employers must give each employee a P60 by 31 May. Keep yours: you\'ll need it later.', ET,
  'P60s must be given to employees by 31 May.'))
t('p11d', ('Payroll','6 iulie','Beneficiile angajaților: P11D',['Mașina de serviciu, asigurarea medicală etc.','Se raportează pe P11D până la 6 iulie','Angajatorul plătește Class 1A NIC'],
  'Beneficiile în natură, ca mașina de serviciu, se raportează pe P11D până la 6 iulie după anul fiscal.', RT),
  ('Payroll','6 July','Reporting staff benefits: P11D',['Company cars, private medical cover and more','Report on P11D by 6 July','Employers pay Class 1A National Insurance'],
  'Benefits in kind, like company cars, are reported on a P11D by 6 July after the tax year.', ET,
  'Benefits in kind go on a P11D by 6 July.'))
t('er-nic', ('Angajatori','15%','Cât plătește angajatorul la National Insurance',['15% peste pragul de £5.000 pe an','Employment Allowance: până la £10.500','Reduce costul primilor angajați'],
  'Angajatorii plătesc 15% National Insurance peste £5.000 pe an pe angajat. Employment Allowance poate reduce factura cu până la £10.500.', RT),
  ('Employers','15%','What employers pay in National Insurance',['15% above £5,000 a year per employee','Employment Allowance: up to £10,500','Cuts the cost of your first hires'],
  'Employers pay 15% National Insurance above £5,000 a year per employee. Employment Allowance can cut the bill by up to £10,500.', ET,
  "Employer NI: 15% above £5,000 a year. Employment Allowance: up to £10,500."))
# ---------- Personal / family ----------
t('tfc', ('Familie','£2.000','Tax-Free Childcare: statul pune 20%',['La fiecare £8 plătiți, statul adaugă £2','Până la £2.000 pe an pentru fiecare copil','£4.000 pentru copii cu dizabilități'],
  'Prin Tax-Free Childcare, statul adaugă £2 la fiecare £8 plătiți pentru creșă sau after-school, până la £2.000 pe an pe copil.', RT),
  ('Family','£2,000','Tax-Free Childcare: the government adds 20%',['For every £8 you pay, it adds £2','Up to £2,000 a year per child','£4,000 for disabled children'],
  'Tax-Free Childcare adds £2 for every £8 you pay towards childcare, up to £2,000 a year per child.', ET,
  'Tax-Free Childcare: +£2 for every £8, up to £2,000 per child a year.'))
t('pa-trap', ('Venituri mari','60%','Capcana dintre £100.000 și £125.140',['Pierzi £1 din allowance la fiecare £2','Impozitul efectiv urcă la 60% în acest interval','O contribuție la pensie poate ajuta'],
  'Între £100.000 și £125.140, pierderea personal allowance face ca impozitul efectiv să ajungă la 60%. Planificarea contează.', RT),
  ('High earners','60%','The trap between £100,000 and £125,140',['You lose £1 of allowance for every £2','Your effective tax rate hits 60% in this band','Pension contributions can help'],
  'Between £100,000 and £125,140, losing your personal allowance pushes the effective tax rate to 60%. Planning matters.', ET,
  'Earning £100k–£125,140? Losing your personal allowance means an effective 60% rate.'))
t('taxcode', ('PAYE','1257L','Ce înseamnă codul tău fiscal 1257L',['1257L = £12.570 personal allowance','Un cod greșit înseamnă impozit greșit','Îl verifici în contul HMRC'],
  'Codul fiscal 1257L înseamnă că primești personal allowance-ul standard de £12.570. Un cod greșit te poate costa bani.', RT),
  ('PAYE','1257L','What your 1257L tax code means',['1257L = £12,570 personal allowance','A wrong code means wrong tax','Check it in your HMRC account'],
  'Tax code 1257L means you get the standard £12,570 personal allowance. A wrong code can cost you money.', ET,
  'Tax code 1257L = standard £12,570 allowance. Check yours in the HMRC app.'))
t('scam', ('Atenție','Fraudă','HMRC nu-ți cere datele bancare prin SMS',['Nu răspunde la SMS-uri cu „rambursare”','Nu da click pe linkuri suspecte','Verifică totul în contul tău de pe gov.uk'],
  'HMRC nu îți trimite SMS-uri sau e-mailuri cu linkuri ca să-ți ceară datele bancare pentru „rambursări”. Verifică totul pe gov.uk.', RT),
  ('Warning','Scam','HMRC won\'t ask for bank details by text',['Ignore texts offering a "tax refund"','Don\'t click suspicious links','Check everything in your gov.uk account'],
  'HMRC won\'t text or email you a link asking for bank details for a "refund". Check everything in your gov.uk account.', ET,
  'Scam alert: HMRC won\'t text you a refund link asking for bank details.'))
t('pension-years', ('Pensia de stat','35 de ani','Câți ani de contribuții îți trebuie',['35 de ani pentru pensia de stat completă','Minimum 10 ani pentru o pensie parțială','Verifică-ți istoricul în contul HMRC'],
  'Pentru pensia de stat completă în UK ai nevoie de 35 de ani de National Insurance. Minimum 10 ani pentru o pensie parțială.', RT),
  ('State Pension','35 years','How many qualifying years you need',['35 years for the full new State Pension','At least 10 years for any State Pension','Check your record in your HMRC account'],
  'You need 35 qualifying National Insurance years for the full new State Pension and at least 10 for any.', ET,
  'Full new State Pension needs 35 NI years; at least 10 for any pension.'))
t('pension-relief', ('Pensie','£60.000','Contribuțiile la pensie reduc impozitul',['Primești relief fiscal la contribuții','Limita anuală: de regulă £60.000','Self-employed: e o deducere utilă'],
  'Contribuțiile la pensie primesc relief fiscal. Limita anuală standard este £60.000. Pentru self-employed e una dintre cele mai bune economii.', RT),
  ('Pensions','£60,000','Pension contributions cut your tax',['You get tax relief on contributions','Annual allowance: usually £60,000','A smart move for the self-employed'],
  'Pension contributions get tax relief, with a standard annual allowance of £60,000. One of the best tax savers for the self-employed.', ET,
  'Pension contributions get tax relief; annual allowance is usually £60,000.'))
t('isa', ('Economii','£20.000','ISA: economii fără impozit',['Poți pune până la £20.000 pe an','Dobânda și câștigurile sunt fără impozit','Nu se declară în Self Assessment'],
  'Într-un ISA poți pune până la £20.000 pe an, iar dobânda sau câștigurile sunt fără impozit.', RT),
  ('Savings','£20,000','ISAs: tax-free saving',['Save up to £20,000 a year','Interest and gains are tax-free','Nothing to declare on your tax return'],
  'You can put up to £20,000 a year into ISAs, and the interest or gains are tax-free.', ET,
  'ISA allowance: £20,000 a year, interest and gains tax-free.'))
t('psa', ('Economii','£1.000','Dobânda la economii: cât e scutit',['Rata de bază: £1.000 dobândă scutită','Rata superioară: £500','Rata adițională: fără scutire'],
  'Personal Savings Allowance: dacă plătești rata de bază, primii £1.000 de dobândă pe an sunt scutiți. La rata superioară, £500.', RT),
  ('Savings','£1,000','How much savings interest is tax-free',['Basic rate: £1,000 of interest tax-free','Higher rate: £500','Additional rate: none'],
  'The Personal Savings Allowance lets basic-rate taxpayers earn £1,000 of interest tax-free; higher-rate, £500.', ET,
  'Personal Savings Allowance: £1,000 basic rate, £500 higher rate, none for additional rate.'))
t('class2-vol', ('National Insurance','£3,65','Profit mic? Poți plăti Class 2 voluntar',['Sub £7.105 profit nu ești obligat','Voluntar: £3,65 pe săptămână','Îți păstrează anii pentru pensia de stat'],
  'Dacă profitul tău e sub £7.105, poți plăti voluntar Class 2 cu £3,65 pe săptămână, ca să-ți păstrezi anii pentru pensie.', RT),
  ('National Insurance','£3.65','Low profits? Voluntary Class 2 NI',['Not required below £7,105 profit','Voluntary rate: £3.65 a week','Protects your State Pension years'],
  'With profits under £7,105 you can pay voluntary Class 2 at £3.65 a week to protect your State Pension record.', ET,
  'Profits under £7,105? Voluntary Class 2 is £3.65 a week and protects your pension years.'))
# ---------- Cross-border ----------
t('worldwide', ('Rezidenți UK','Global','Rezident în UK? Declari și veniturile din străinătate',['Rezidenții UK sunt impozitați pe venitul global','Chiria din România se declară în UK','Impozitul plătit acolo poate fi scăzut'],
  'Dacă ești rezident fiscal în UK, declari și veniturile din străinătate, de exemplu chiria din România. Impozitul plătit acolo se poate deduce.', RT),
  ('UK residents','Worldwide','UK resident? Declare your foreign income too',['UK residents are taxed on worldwide income','Rent from a property abroad goes on your UK return','Tax paid abroad can usually be credited'],
  'If you are UK tax resident, you declare foreign income too, such as rent from a property abroad. Foreign tax paid can usually be credited.', ET,
  'UK tax resident? Foreign income goes on your UK return; foreign tax can usually be credited.'))
t('dta', ('Dublă impunere','Tratat','UK și România au tratat împotriva dublei impuneri',['Același venit nu trebuie impozitat de două ori','Se aplică credit pentru impozitul plătit','Ai nevoie de acte din ambele țări'],
  'Între UK și România există un tratat împotriva dublei impuneri. Cu actele potrivite, nu plătești de două ori pe același venit.', RT),
  ('Double taxation','Treaty','The UK has double tax treaties',['The same income shouldn\'t be taxed twice','Foreign tax credit relief applies','You need paperwork from both countries'],
  'The UK has double taxation agreements with many countries. With the right paperwork, the same income isn\'t taxed twice.', ET,
  'Double tax treaties: claim foreign tax credit relief so the same income isn\'t taxed twice.'))
t('letters', ('HMRC','Scrisoare','Ai primit o scrisoare de la HMRC? Nu o ignora',['Citește termenul de răspuns','Verifică dacă e autentică în contul tău','Adu-ne scrisoarea, te ajutăm să răspunzi'],
  'O scrisoare de la HMRC ignorată devine o problemă mai mare. Citește termenul și adu-ne-o, te ajutăm să răspunzi corect.', RT),
  ('HMRC','Letter','Got a letter from HMRC? Don\'t ignore it',['Check the response deadline','Confirm it\'s genuine in your account','Bring it to us and we\'ll help you reply'],
  'An ignored HMRC letter becomes a bigger problem. Check the deadline and bring it to us; we\'ll help you respond.', ET,
  'Got a letter from HMRC? Check the deadline and get help replying. Ignoring it costs more.'))
# ---------- Ola ----------
t('ola-hours', ('Ola Accountancy','10–16','Când ne găsești la birou',['Luni–vineri, 10:00–16:00','Luton: 23A George Street, LU1 2AF','Birmingham: 22-42 Washwood Heath Rd, B8 1RB'],
  'Te așteptăm de luni până vineri, între 10:00 și 16:00, la birourile din Luton și Birmingham. Programează-te pe WhatsApp.', RT),
  ('Ola Accountancy','10–4','When you can visit us',['Monday to Friday, 10am to 4pm','Luton: 23A George Street, LU1 2AF','Birmingham: 22-42 Washwood Heath Rd, B8 1RB'],
  'Visit us Monday to Friday, 10am to 4pm, at our Luton and Birmingham offices. Book on WhatsApp.', ET,
  'Ola Accountancy: Mon–Fri 10am–4pm in Luton and Birmingham.'))
t('ola-services', ('Ola Accountancy','Servicii','Cu ce te ajutăm',['Self Assessment, MTD și TVA','Firme LTD: conturi, payroll, dividende','Certificate de rezidență fiscală'],
  'Ne ocupăm de Self Assessment, Making Tax Digital, TVA, firme LTD, payroll și certificate de rezidență fiscală. În română.', RT),
  ('Ola Accountancy','Services','How we can help',['Self Assessment, MTD and VAT','Limited companies: accounts, payroll, dividends','Certificates of tax residence'],
  'We handle Self Assessment, Making Tax Digital, VAT, limited companies, payroll and certificates of residence.', ET,
  'Ola Accountancy: Self Assessment, MTD, VAT, limited companies, payroll.'))
t('ola-fin', ('Consultanță financiară','£420','O oră de consultanță cu Valentin Avram',['Pentru antreprenori și afaceri mici','Structura afacerii, impozite, plan financiar','£420, TVA inclus'],
  'Pentru afaceri mici avem o consultanță financiară de o oră cu Valentin Avram: structura afacerii, impozite și plan. £420 cu TVA inclus.', RT),
  ('Financial consultation','£420','One hour with Valentin Avram',['For founders and small businesses','Structure, tax and financial planning','£420 including VAT'],
  'For small businesses: a one-hour financial consultation with Valentin Avram on structure, tax and planning. £420 including VAT.', ET,
  'One-hour financial consultation with Valentin Avram: £420 including VAT.'))
t('ola-bring', ('Ola Accountancy','Pregătire','Ce aduci la prima consultație',['Act de identitate și dovada adresei din UK','UTR-ul, dacă îl ai','Extrase de cont, facturi, bonuri'],
  'Ca prima consultație să fie utilă, adu actul de identitate, dovada adresei, UTR-ul și documentele pentru venituri și cheltuieli.', RT),
  ('Ola Accountancy','Prepare','What to bring to your first meeting',['ID and proof of UK address','Your UTR, if you have one','Bank statements, invoices and receipts'],
  'To get the most out of your first meeting, bring ID, proof of address, your UTR and your income and expense records.', ET,
  'First meeting checklist: ID, proof of address, UTR, bank statements, invoices, receipts.'))
t('ola-how', ('Ola Accountancy','3 pași','Cum lucrăm cu tine',['1. Ne scrii pe WhatsApp','2. Consultația: 30 de minute, £120 cu TVA','3. Îți spunem clar pașii și costul'],
  'Simplu: ne scrii pe WhatsApp, facem consultația de 30 de minute și îți spunem exact ce ai de făcut și cât costă.', RT),
  ('Ola Accountancy','3 steps','How working with us works',['1. Message us on WhatsApp','2. 30-minute consultation, £120 including VAT','3. Clear next steps and a clear price'],
  'Simple: message us on WhatsApp, have a 30-minute consultation, and get clear next steps and a clear price.', ET,
  'Working with Ola: WhatsApp us, 30-minute consultation (£120 inc VAT), clear next steps.'))
t('ola-why', ('Ola Accountancy','RO + EN','Contabilitate în limba ta',['Echipă care vorbește română și engleză','Birouri în Luton și Birmingham','Programări rapide pe WhatsApp'],
  'La Ola îți explicăm totul în română, iar cu HMRC vorbim noi. Birouri în Luton și Birmingham.', RT),
  ('Ola Accountancy','EN + RO','Accounting in your language',['A team that speaks English and Romanian','Offices in Luton and Birmingham','Quick bookings on WhatsApp'],
  'At Ola we explain everything clearly and deal with HMRC for you. Offices in Luton and Birmingham.', ET,
  'Ola Accountancy: English and Romanian-speaking accountants in Luton and Birmingham.'))
# ---------- Myths / tips ----------
t('myth-small', ('Mit','Fals','„Câștig puțin, nu trebuie să declar”',['Peste £1.000 venit independent te înregistrezi','Chiar dacă ai și job cu salariu','Amenzile vin și pentru sume mici'],
  'Mit: „dacă câștig puțin nu trebuie să declar”. Fals: peste £1.000 pe an din activități independente trebuie să te înregistrezi.', RT),
  ('Myth','False','"I earn too little to declare it"',['Over £1,000 of self-employed income, you register','Even if you also have a salaried job','Penalties apply to small amounts too'],
  'Myth: "I earn too little to declare it." Over £1,000 a year of self-employed income, you must register.', ET,
  'Myth: small side income doesn\'t count. Over £1,000 a year, you must register.'))
t('myth-paye', ('Mit','Fals','„Sunt pe PAYE, n-am nimic de făcut”',['Verifică-ți codul fiscal','Alte venituri trebuie declarate','Poți avea de primit bani înapoi'],
  'Chiar dacă ești angajat pe PAYE, verifică-ți codul fiscal și veniturile extra. Uneori ai de primit bani înapoi de la HMRC.', RT),
  ('Myth','False','"I\'m on PAYE, so there\'s nothing to do"',['Check your tax code','Other income may still need declaring','You might even be owed a refund'],
  'Even on PAYE, check your tax code and any extra income. Sometimes HMRC owes you money.', ET,
  'On PAYE? Still check your tax code and other income. You might be owed a refund.'))
t('tip-reminders', ('Sfat','Calendar','Setează remindere pentru termene',['31 ianuarie și 31 iulie: plăți','5 octombrie: înregistrare','7 noiembrie: raport MTD, dacă ești în MTD'],
  'Setează remindere în telefon pentru termenele fiscale. E cel mai ieftin mod de a evita amenzile.', RT),
  ('Tip','Calendar','Set reminders for your tax deadlines',['31 January and 31 July: payments','5 October: registration','7 November: MTD update, if you are in MTD'],
  'Set phone reminders for your tax deadlines. It\'s the cheapest way to avoid penalties.', ET,
  'Tip: set reminders for 31 Jan, 31 Jul, 5 Oct and 7 Nov.'))
t('tip-app', ('Sfat','HMRC app','Aplicația HMRC te ajută',['Vezi codul fiscal și istoricul NI','Vezi și plătești ce datorezi','Găsești UTR-ul și numărul NI'],
  'Aplicația oficială HMRC îți arată codul fiscal, istoricul National Insurance, UTR-ul și ce ai de plată.', RT),
  ('Tip','HMRC app','The HMRC app is worth having',['See your tax code and NI record','Check and pay what you owe','Find your UTR and NI number'],
  'The official HMRC app shows your tax code, National Insurance record, UTR and what you owe.', ET,
  'The HMRC app shows your tax code, NI record, UTR and what you owe.'))
# ---------- extra EN-only (replace Valentin slots) ----------
EN_EXTRA = [
 ('iht-nrb','Inheritance Tax','£325,000','The Inheritance Tax nil-rate band',['The first £325,000 of an estate is usually tax-free','Above that, the standard rate is 40%','Spouses can pass on unused allowance'],
  'Inheritance Tax is usually charged at 40% above the £325,000 nil-rate band. Married couples can pass unused allowance to each other.', 'Inheritance Tax: £325,000 nil-rate band, 40% above it.'),
 ('iht-rnrb','Inheritance Tax','£175,000','Leaving your home to your children?',['Residence nil-rate band: up to £175,000','On top of the £325,000 nil-rate band','It tapers away for larger estates'],
  'If you leave your home to children or grandchildren, the residence nil-rate band can add up to £175,000 to your tax-free amount.', 'Residence nil-rate band: up to £175,000 extra when your home goes to your children.'),
 ('iht-gifts','Gifts','£3,000','Gifts you can make each year',['£3,000 a year annual exemption','Small gifts of up to £250 per person','Unused annual exemption carries forward 1 year'],
  'You can give away £3,000 a year free of Inheritance Tax, plus small gifts of up to £250 per person.', 'Gift allowance: £3,000 a year, plus £250 small gifts per person.'),
 ('iht-7yr','Gifts','7 years','The 7-year rule for larger gifts',['Gifts above your allowances may be taxed','If you live 7 years, they usually fall outside your estate','Keep a record of what you gave and when'],
  'Larger gifts usually fall outside your estate if you live for 7 years after making them. Keep records.', 'Larger gifts usually escape Inheritance Tax if you live 7 years after giving them.'),
 ('iht-wedding','Gifts','£5,000','Wedding gifts and Inheritance Tax',['Parents can give £5,000','Grandparents can give £2,500','Anyone else: £1,000'],
  'Wedding gifts are exempt up to £5,000 from a parent, £2,500 from a grandparent and £1,000 from anyone else.', 'Wedding gift exemptions: £5,000 parent, £2,500 grandparent, £1,000 others.'),
 ('will','Planning','A will','Why every business owner needs a will',['Decide who inherits your business and assets','Make sure the right reliefs can be claimed','Review it after big life changes'],
  'A will decides who inherits your business and assets and helps your family claim the right reliefs. Review it after big changes.', 'Business owner? A will protects your family and your business.'),
 ('marg-relief','Limited companies','£50k–£250k','Corporation Tax marginal relief explained',['19% up to £50,000 profit','25% above £250,000','In between, marginal relief smooths the jump'],
  'Between £50,000 and £250,000 of profit, marginal relief smooths the step from 19% to 25% Corporation Tax.', 'Corporation Tax marginal relief applies between £50,000 and £250,000 of profit.'),
]

# ---------- batch 2 ----------
t('poa-reduce', ('Plăți în avans','Reducere','Venitul ți-a scăzut? Poți reduce plățile în avans',['Plățile se calculează din anul trecut','Dacă anul acesta câștigi mai puțin, ceri reducere','Atenție: dacă reduci prea mult, plătești dobândă'],
  'Dacă venitul tău a scăzut, poți cere la HMRC reducerea plăților în avans. Dar nu exagera: diferența se plătește cu dobândă.', RT),
  ('Payments on account','Reduce','Income down? You can reduce payments on account',['They\'re based on last year\'s bill','If this year will be lower, apply to reduce them','Reduce too much and you pay interest'],
  'If your income has dropped, you can ask HMRC to reduce your payments on account. Cut too far and interest applies.', ET,
  'Income down this year? You can apply to reduce your payments on account.'))
t('sa-refund', ('Rambursare','Bani înapoi','Ai plătit prea mult impozit? Îl primești înapoi',['Declarația poate arăta că HMRC îți datorează bani','Banii vin în cont după procesare','Verifică mereu calculul înainte de trimitere'],
  'Uneori declarația arată că ai plătit prea mult: de exemplu prin CIS sau un cod fiscal greșit. HMRC îți returnează diferența.', RT),
  ('Refunds','Money back','Paid too much tax? Get it back',['Your return can show HMRC owes you','The refund is paid after processing','Always check the calculation first'],
  'Sometimes your return shows you overpaid, through CIS or a wrong tax code. HMRC refunds the difference.', ET,
  'Overpaid through CIS or a wrong tax code? Your tax return can get it back.'))
t('cis-rates', ('Construcții (CIS)','20%','Lucrezi în construcții prin CIS?',['Înregistrat: se reține 20%','Neînregistrat: se reține 30%','Gross payment status: 0%'],
  'În construcții, prin CIS, contractorul reține 20% dacă ești înregistrat și 30% dacă nu ești. Înregistrează-te, e o diferență mare.', RT),
  ('Construction (CIS)','20%','Working in construction under CIS?',['Registered: 20% deducted','Not registered: 30% deducted','Gross payment status: 0%'],
  'Under CIS, contractors deduct 20% if you\'re registered and 30% if you\'re not. Registering makes a real difference.', ET,
  'CIS deductions: 20% registered, 30% unregistered, 0% with gross payment status.'))
t('cis-refund', ('Construcții (CIS)','Rambursare','Ți s-a reținut prea mult prin CIS?',['Reținerile sunt plăți în avans pentru impozit','Cheltuielile reduc impozitul real','Diferența ți-o dă HMRC prin declarație'],
  'Reținerile CIS sunt plăți în avans. După ce scazi cheltuielile, de multe ori ai de primit bani înapoi prin Self Assessment.', RT),
  ('Construction (CIS)','Refund','Had too much deducted under CIS?',['CIS deductions are advance tax payments','Your expenses reduce your real tax bill','HMRC refunds the difference via your return'],
  'CIS deductions are advance payments. Once expenses are taken off, many subcontractors are due a refund through Self Assessment.', ET,
  'CIS subcontractor? Deductions are advance tax payments, often refunded via your tax return.'))
t('cis-gross', ('Construcții (CIS)','0%','Gross payment status în CIS',['Primești plata fără rețineri','Trebuie să îndeplinești condiții de cifră de afaceri','Și să ai obligațiile fiscale la zi'],
  'Cu gross payment status primești plata integral, fără rețineri CIS. Trebuie îndeplinite condițiile HMRC și obligațiile la zi.', RT),
  ('Construction (CIS)','0%','CIS gross payment status',['You get paid with no deductions','You must meet turnover tests','And keep your tax affairs up to date'],
  'With gross payment status you\'re paid in full, with no CIS deductions, if you meet HMRC\'s tests and stay compliant.', ET,
  'CIS gross payment status: paid in full with no deductions, if you pass HMRC\'s tests.'))
t('drc', ('TVA în construcții','Reverse charge','Taxarea inversă în construcții',['Se aplică între firme cu TVA, prin CIS','Clientul plătește TVA-ul direct la HMRC','Pe factură scrii mențiunea de reverse charge'],
  'În construcții, între firme înregistrate pentru TVA și în CIS, se aplică domestic reverse charge: TVA-ul îl declară clientul.', RT),
  ('Construction VAT','Reverse charge','The construction VAT reverse charge',['Applies between VAT-registered CIS businesses','The customer accounts for VAT to HMRC','Your invoice must say reverse charge applies'],
  'Between VAT-registered businesses in CIS, the domestic reverse charge applies: the customer accounts for the VAT.', ET,
  'Construction VAT reverse charge: the customer accounts for VAT between CIS VAT-registered firms.'))
t('platforms', ('Vânzări online','HMRC vede','Vinzi online sau lucrezi prin aplicații?',['Platformele raportează la HMRC veniturile vânzătorilor','Livrări, ride-sharing, închirieri, vânzări','Declară corect ce câștigi'],
  'Platformele online raportează la HMRC veniturile celor care vând sau lucrează prin ele. Ce câștigi acolo trebuie declarat corect.', RT),
  ('Selling online','HMRC knows','Selling online or working through apps?',['Platforms report sellers\' income to HMRC','Delivery, ride-hailing, lettings, online sales','Declare what you earn correctly'],
  'Online platforms report sellers\' and workers\' income to HMRC. What you earn through them must be declared correctly.', ET,
  'Digital platforms report sellers\' income to HMRC. Declare your app and online earnings.'))
t('dir-pension', ('Firme LTD','Pensie','Contribuția la pensie plătită de firmă',['Este de regulă cheltuială deductibilă pentru firmă','Nu se plătește National Insurance pe ea','Atenție la limita anuală'],
  'Contribuțiile la pensie plătite de firmă pentru director sunt de regulă deductibile și fără National Insurance.', RT),
  ('Limited companies','Pension','Company pension contributions for directors',['Usually an allowable business expense','No National Insurance on them','Watch the annual allowance'],
  'Employer pension contributions for directors are usually tax-deductible for the company and free of National Insurance.', ET,
  'Directors: company pension contributions are usually deductible and NI-free.'))
t('ct-register', ('Firme LTD','3 luni','Ai înființat firma? Anunță HMRC',['Te înregistrezi pentru Corporation Tax','În 3 luni de la începerea activității','Altfel riști amenzi'],
  'După ce firma începe activitatea, ai 3 luni să o înregistrezi pentru Corporation Tax la HMRC.', RT),
  ('Limited companies','3 months','New company? Tell HMRC',['Register for Corporation Tax','Within 3 months of starting to trade','Or risk penalties'],
  'Once your company starts trading, you have 3 months to register it for Corporation Tax.', ET,
  'New company? Register for Corporation Tax within 3 months of starting to trade.'))
t('dormant', ('Firme LTD','Dormant','Firma nu are activitate? Tot depui acte',['Conturile anuale se depun și pentru firma dormantă','La fel confirmation statement-ul','Anunță HMRC că firma e dormantă'],
  'Chiar dacă firma nu are activitate, trebuie să depui conturile anuale și confirmation statement-ul la Companies House.', RT),
  ('Limited companies','Dormant','Company not trading? You still have to file',['Dormant companies still file annual accounts','And the confirmation statement','Tell HMRC the company is dormant'],
  'Even a dormant company must file annual accounts and a confirmation statement with Companies House.', ET,
  'Dormant company? You still file accounts and a confirmation statement.'))
t('idv', ('Companies House','Identitate','Directorii trebuie să-și verifice identitatea',['Obligatoriu din 18 noiembrie 2025','Perioadă de tranziție de 12 luni','Se aplică și persoanelor cu control (PSC)'],
  'Verificarea identității la Companies House este obligatorie din 18 noiembrie 2025 pentru directori și PSC, cu o tranziție de 12 luni. Nu lăsa pe ultima sută.', RT),
  ('Companies House','ID check','Directors must verify their identity',['Mandatory from 18 November 2025','12-month transition period','Applies to people with significant control too'],
  'Companies House identity verification became mandatory on 18 November 2025 for directors and PSCs, with a 12-month transition.', ET,
  'Directors and PSCs must verify identity with Companies House. The 12-month transition is ending.'))
t('vat-cash', ('TVA','£1,35 mil.','TVA pe bază de încasare (cash accounting)',['Plătești TVA când încasezi efectiv banii','Pentru cifră de afaceri până la £1,35 milioane','Ajută dacă clienții plătesc târziu'],
  'Cu VAT Cash Accounting plătești TVA-ul doar după ce clientul te plătește. Pentru afaceri cu cifra de afaceri de până la £1,35 milioane.', RT),
  ('VAT','£1.35m','VAT cash accounting',['Pay VAT when your customer actually pays','For taxable turnover up to £1.35 million','Helps if customers pay late'],
  'With VAT cash accounting you pay VAT only when customers pay you. Available up to £1.35 million taxable turnover.', ET,
  'VAT cash accounting: pay VAT when you get paid, for turnover up to £1.35m.'))
t('vat-rates', ('TVA','20%','Cotele de TVA din UK',['Standard: 20%','Redusă: 5% (de ex. energie casnică)','Zero: 0% (de ex. majoritatea alimentelor)'],
  'În UK, TVA are trei cote: 20% standard, 5% redusă și 0%. Contează ce vinzi.', RT),
  ('VAT','20%','UK VAT rates',['Standard rate: 20%','Reduced rate: 5% (e.g. domestic energy)','Zero rate: 0% (e.g. most food)'],
  'UK VAT has three rates: 20% standard, 5% reduced and 0% zero-rated. What you sell decides which applies.', ET,
  'UK VAT rates: 20% standard, 5% reduced, 0% zero.'))
t('holiday', ('Angajați','5,6 săptămâni','Concediul legal al angajaților',['5,6 săptămâni pe an pentru normă întreagă','Adică 28 de zile la 5 zile pe săptămână','Sărbătorile legale pot fi incluse'],
  'Angajații cu normă întreagă au dreptul la 5,6 săptămâni de concediu plătit pe an, adică 28 de zile la 5 zile pe săptămână.', RT),
  ('Employees','5.6 weeks','Statutory holiday entitlement',['5.6 weeks a year for full-time staff','That\'s 28 days on a 5-day week','Bank holidays can be included'],
  'Full-time employees are entitled to 5.6 weeks\' paid holiday a year: 28 days for a 5-day week.', ET,
  'Statutory holiday: 5.6 weeks a year (28 days on a 5-day week).'))
t('payslip', ('Angajați','Fluturaș','Fiecare angajat primește fluturaș de salariu',['Salariul brut și net','Toate reținerile: impozit, NI, pensie','Orele, dacă plata variază după ore'],
  'Toți angajații au dreptul la fluturaș de salariu care arată brutul, netul și toate reținerile.', RT),
  ('Employees','Payslip','Every employee gets a payslip',['Gross and net pay','Every deduction: tax, NI, pension','Hours, if pay varies by time worked'],
  'Every employee is entitled to a payslip showing gross pay, net pay and all deductions.', ET,
  'Every employee must get a payslip showing gross, net and all deductions.'))
t('reenrol', ('Pensie','3 ani','Re-înrolarea în pensie la fiecare 3 ani',['Angajații care au ieșit sunt reînscriși','Angajatorul face declarația de reînscriere','Termenul vine o dată la 3 ani'],
  'O dată la 3 ani, angajatorul trebuie să reînscrie la pensie angajații care au ieșit și să depună declarația de re-enrolment.', RT),
  ('Pensions','3 years','Pension re-enrolment every 3 years',['Staff who opted out are put back in','The employer files a re-declaration','It comes round every 3 years'],
  'Every 3 years, employers must re-enrol eligible staff who opted out and file a re-declaration.', ET,
  'Employers: pension re-enrolment and re-declaration every 3 years.'))
t('emergency', ('PAYE','Cod de urgență','Ai cod fiscal de urgență?',['Apare des când schimbi jobul','Poți plăti mai mult impozit temporar','Diferența se corectează prin HMRC'],
  'Codul fiscal de urgență apare des la schimbarea jobului și poate însemna impozit mai mare. Se corectează, iar banii se recuperează.', RT),
  ('PAYE','Emergency code','On an emergency tax code?',['Common when you change jobs','You may overpay tax for a while','It gets corrected and refunded'],
  'Emergency tax codes are common after a job change and can mean overpaying. It can be corrected and refunded.', ET,
  'Emergency tax code after a job change? You may be owed a refund once it\'s fixed.'))
t('wfh-employee', ('Angajați','Schimbare','Relief pentru lucrul de acasă: s-a schimbat',['Din 2026–27 angajații nu-l mai pot cere','Pentru anii anteriori se poate cere încă','Doar dacă erai obligat să lucrezi de acasă'],
  'Din anul fiscal 2026–27, angajații nu mai pot cere relief pentru lucrul de acasă. Pentru anii anteriori se poate încă cere, dacă erai obligat.', RT),
  ('Employees','Changed','Working from home relief has changed',['Employees can\'t claim it for 2026–27','Earlier years can still be claimed','Only if you had to work from home'],
  'Employees can no longer claim working-from-home tax relief for 2026–27, but earlier years can still be claimed if you had to work from home.', ET,
  'Employee WFH relief: not available for 2026–27; earlier years can still be claimed.'))
t('class3', ('Pensia de stat','Goluri','Ai ani lipsă în istoricul de National Insurance?',['Verifică-ți istoricul în contul HMRC','Unele goluri se pot acoperi voluntar','Merită verificat înainte de pensie'],
  'Dacă ai ani lipsă în istoricul de National Insurance, unii pot fi acoperiți prin contribuții voluntare. Verifică în contul HMRC.', RT),
  ('State Pension','Gaps','Gaps in your National Insurance record?',['Check your record in your HMRC account','Some gaps can be filled voluntarily','Worth checking well before retirement'],
  'Gaps in your NI record can reduce your State Pension. Some years can be filled with voluntary contributions.', ET,
  'Gaps in your NI record? Some can be filled with voluntary contributions.'))
t('lisa', ('Economii','25%','Lifetime ISA: statul adaugă 25%',['Pui până la £4.000 pe an','Primești bonus de până la £1.000 pe an','Pentru prima casă sau după 60 de ani'],
  'Lifetime ISA: pui până la £4.000 pe an și statul adaugă 25%, adică până la £1.000. Îl deschizi înainte de 40 de ani.', RT),
  ('Savings','25%','Lifetime ISA: a 25% government bonus',['Save up to £4,000 a year','Get up to £1,000 a year bonus','For a first home or from age 60'],
  'With a Lifetime ISA you save up to £4,000 a year and get a 25% bonus, up to £1,000. Open it before 40.', ET,
  'Lifetime ISA: save up to £4,000 a year, get a 25% bonus (max £1,000).'))
t('losses', ('Self-employed','Pierdere','Ai avut pierdere în afacere?',['Pierderea se declară, nu se ignoră','Poate reduce impozitul din alți ani','Sau din alte venituri, în anumite condiții'],
  'O pierdere în afacere trebuie declarată. În anumite condiții, poate reduce impozitul din alte venituri sau din alți ani.', RT),
  ('Self-employed','Loss','Made a loss in your business?',['Declare it; don\'t ignore it','It can reduce tax in other years','Or on other income, in some cases'],
  'A business loss should be declared. In some cases it can reduce tax on other income or in other years.', ET,
  'Made a trading loss? Declare it: it may reduce tax in other years or on other income.'))
t('ola-agent', ('Ola Accountancy','Agent HMRC','Vorbim noi cu HMRC pentru tine',['Ne autorizezi ca agent','Primim corespondența și răspundem noi','Tu te ocupi de afacerea ta'],
  'Când lucrezi cu Ola, ne autorizezi ca agent la HMRC. Noi răspundem la scrisori și ținem legătura cu HMRC.', RT),
  ('Ola Accountancy','HMRC agent','We deal with HMRC for you',['You authorise us as your agent','We handle HMRC letters and calls','You focus on your business'],
  'Once you authorise us as your agent, we deal with HMRC letters and calls for you.', ET,
  'Authorise Ola as your HMRC agent and we handle the letters and calls.'))
t('ola-residency', ('Rezidență fiscală','HMRC','Certificatul de rezidență fiscală din UK',['Îl emite HMRC rezidenților fiscali din UK','Confirmă situația reală: unde locuiești','Te ajutăm să aplici corect'],
  'Certificatul de rezidență fiscală îl emite HMRC pentru cei care sunt rezidenți fiscali în UK. Te ajutăm să aplici corect.', RT),
  ('Tax residence','HMRC','UK certificate of residence',['Issued by HMRC to UK tax residents','It confirms your real situation','We help you apply correctly'],
  'HMRC issues certificates of residence to people who are UK tax resident. We help you apply correctly.', ET,
  'Need proof of UK tax residence? HMRC issues certificates of residence; we can help you apply.'))
t('ola-bham', ('Ola Birmingham','B8 1RB','Ne găsești și în Birmingham',['22-42 Washwood Heath Rd, Saltley, B8 1RB','Luni–vineri, 10:00–16:00','Programare pe WhatsApp'],
  'Biroul Ola din Birmingham te așteaptă pe Washwood Heath Rd, Saltley, de luni până vineri, 10:00–16:00.', RT),
  ('Ola Birmingham','B8 1RB','Find us in Birmingham',['22-42 Washwood Heath Rd, Saltley, B8 1RB','Monday to Friday, 10am to 4pm','Book on WhatsApp'],
  'Our Birmingham office is on Washwood Heath Rd, Saltley. Monday to Friday, 10am to 4pm.', ET,
  'Ola Birmingham: 22-42 Washwood Heath Rd, B8 1RB. Mon–Fri 10–4.'))
t('ola-luton', ('Ola Luton','LU1 2AF','Biroul nostru central din Luton',['23A George Street, LU1 2AF','Luni–vineri, 10:00–16:00','Programare pe WhatsApp'],
  'Sediul central Ola e în Luton, pe 23A George Street. Te așteptăm de luni până vineri, 10:00–16:00.', RT),
  ('Ola Luton','LU1 2AF','Our Luton head office',['23A George Street, LU1 2AF','Monday to Friday, 10am to 4pm','Book on WhatsApp'],
  'Our head office is at 23A George Street, Luton. Monday to Friday, 10am to 4pm.', ET,
  'Ola Luton: 23A George Street, LU1 2AF. Mon–Fri 10–4.'))
t('rtw', ('Angajatori','Obligatoriu','Verifică dreptul de muncă înainte de angajare',['Verificarea se face înainte de prima zi','Păstrează o copie a dovezii','Amenzile pentru lipsă sunt mari'],
  'Ca angajator, verifici dreptul de a lucra în UK înainte de prima zi de muncă și păstrezi dovada.', RT),
  ('Employers','Required','Check right to work before someone starts',['Do the check before day one','Keep a copy of the evidence','Penalties for not checking are high'],
  'Employers must check a person\'s right to work in the UK before they start, and keep the evidence.', ET,
  'Employers: check right to work before day one and keep the evidence.'))
t('mtd-signup', ('Making Tax Digital','Înscriere','Trebuie să intri în MTD? Înscrie-te din timp',['Verifică dacă treci pragul','Alege software-ul înainte de termen','Te ajutăm cu înscrierea'],
  'Dacă treci pragul pentru Making Tax Digital, înscrie-te și alege software-ul din timp, nu în ultima săptămână.', RT),
  ('Making Tax Digital','Sign up','Need to join MTD? Sign up early',['Check whether you\'re over the threshold','Choose software before your deadline','We can help you sign up'],
  'If you are over the Making Tax Digital threshold, sign up and choose software early, not in the last week.', ET,
  'Over the MTD threshold? Sign up and choose software early.'))
t('cb-register', ('Child Benefit','NI','Câștigi peste prag? Tot merită să ceri Child Benefit',['Înregistrarea îți dă credite de National Insurance','Contează pentru pensia de stat','Poți opta să nu primești banii'],
  'Chiar dacă venitul e mare, înregistrarea pentru Child Benefit poate aduce credite de National Insurance pentru pensie.', RT),
  ('Child Benefit','NI credits','High earner? Still register for Child Benefit',['Registering can give National Insurance credits','They count towards your State Pension','You can opt out of the payments'],
  'Even if you earn a lot, registering for Child Benefit can give a non-working parent NI credits for their pension.', ET,
  'High earner? Still register for Child Benefit for the NI credits; you can opt out of payments.'))
t('uniform', ('Angajați','Uniformă','Speli singur uniforma de serviciu?',['Poți cere relief fiscal pentru spălare','Doar pentru uniforme specifice, nu haine obișnuite','Se poate cere și pentru anii anteriori'],
  'Dacă îți speli singur uniforma de serviciu, poți cere relief fiscal de la HMRC, inclusiv pentru anii anteriori.', RT),
  ('Employees','Uniform','Wash your own work uniform?',['You may claim tax relief for cleaning it','Only for uniforms, not everyday clothes','Earlier years can be claimed too'],
  'If you wash your own work uniform, you may be able to claim tax relief from HMRC, including for earlier years.', ET,
  'Wash your own work uniform? You may be able to claim tax relief.'))
t('student-loan', ('Student loan','Self Assessment','Ai student loan și ești self-employed?',['Rambursarea se calculează prin Self Assessment','Se adaugă la factura de impozit','Ține cont de ea când pui bani deoparte'],
  'Dacă ești self-employed și ai student loan, rambursarea se calculează prin Self Assessment și se adaugă la impozit.', RT),
  ('Student loan','Self Assessment','Self-employed with a student loan?',['Repayments are worked out through Self Assessment','They\'re added to your tax bill','Include them when you save for tax'],
  'If you\'re self-employed with a student loan, repayments are calculated through Self Assessment and added to your bill.', ET,
  'Self-employed with a student loan? Repayments are added to your Self Assessment bill.'))
t('mtd-exempt', ('Making Tax Digital','Scutire','Nu poți folosi software? Există scutire',['Pentru cei care nu pot folosi digital','Din motive de vârstă, dizabilitate sau locație','Se cere la HMRC, cu motive'],
  'Unii oameni pot cere scutire de la Making Tax Digital dacă nu pot folosi software, de exemplu din motive de vârstă sau dizabilitate.', RT),
  ('Making Tax Digital','Exemption','Can\'t use software? You may be exempt',['For people who are digitally excluded','Because of age, disability or location','Apply to HMRC with your reasons'],
  'People who are digitally excluded, for example because of age or disability, can apply to HMRC for an MTD exemption.', ET,
  'Digitally excluded? You can apply to HMRC for an MTD exemption.'))
t('vat-annual', ('TVA','O dată pe an','Annual Accounting Scheme pentru TVA',['O singură declarație de TVA pe an','Plăți în avans pe parcursul anului','Pentru cifră de afaceri până la £1,35 milioane'],
  'Prin Annual Accounting Scheme depui o singură declarație de TVA pe an și plătești în avans. Pentru afaceri până la £1,35 milioane.', RT),
  ('VAT','Once a year','The VAT Annual Accounting Scheme',['One VAT return a year','Advance payments through the year','For taxable turnover up to £1.35 million'],
  'The Annual Accounting Scheme means one VAT return a year with advance payments, for turnover up to £1.35 million.', ET,
  'VAT Annual Accounting: one return a year, for turnover up to £1.35m.'))
t('ltd-first-year', ('Firme LTD','Primul an','Firmă nouă: ce obligații ai în primul an',['Înregistrare pentru Corporation Tax în 3 luni','Primele conturi în 21 de luni','Confirmation statement în primele 12 luni'],
  'În primul an, o firmă nouă se înregistrează pentru Corporation Tax, depune confirmation statement-ul și pregătește primele conturi.', RT),
  ('Limited companies','Year one','New company: your first-year duties',['Register for Corporation Tax within 3 months','First accounts within 21 months','Confirmation statement within 12 months'],
  'In year one a new company registers for Corporation Tax, files its first confirmation statement and prepares first accounts.', ET,
  'New company? CT registration in 3 months, confirmation statement in 12, first accounts in 21.'))
