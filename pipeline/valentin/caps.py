import json
S={
'2026-08-06-163313834':[(0.18,3.78,'Fiecare afacere mare începe cu o decizie.'),(3.78,6.78,'Decizia de a face ceva mai bun.'),(6.78,13.28,'Noi am ales să schimbăm modul în care oamenii privesc contabilitatea.'),(13.28,19.78,'De asta sunt atât de transparent cu toată lumea și vă vorbesc din suflet.'),(19.78,25.78,'Sufletul unui om care înțelege alți oameni și nu vreau să vă las la greu.'),(25.78,29.78,'Asta e ideea: oricine are probleme'),(30.38,36.38,'trebuie să înțeleagă că problemele vin cu un scop: să fie rezolvate.'),(36.38,41.38,'Nu există nicio problemă fără rezolvare, există doar oameni neinformați.'),(41.38,44.0,'O zi frumoasă, dragilor!')],
'2026-09-29-120520962':[(0.02,8.02,'Am ajuns acasă. Cum vedeți și voi, sunt la sediul nostru din Luton, Ola Accountancy.'),(8.02,12.02,'Mă simt atât de bine aici, în biroul ăsta frumos, da?'),(12.02,21.02,'Și sunt fericit că am o echipă foarte tare. O organizație care a depășit zece oameni.'),(21.02,29.02,'Toți știu ce au de făcut, da? Am ajuns în etapa în care mă ocup doar de conducerea firmei.'),(29.02,32.02,'Fiecare om știe ce are de făcut.'),(33.02,42.02,'Dragilor, vă doresc și vouă succesul pe care mi-l doresc mie. Vă așteptăm cu drag la Ola Accountancy.'),(42.02,43.0,'Numai bine!')],
'2026-09-28-092335537':[(0.0,8.0,'După o săptămână de muncă asiduă, dragilor, Ola Accountancy Birmingham este deschis pentru public.'),(8.0,12.0,'Uitați-vă și voi cum a ieșit.'),(12.0,20.0,'Programul este de luni până vineri, de la ora 10 la ora 4.'),(22.0,25.0,'Și aici în spate, perfect.'),(25.0,35.54,'Mai avem de pus televizorul pe perete. Totul este cum trebuie.'),(35.54,44.54,'Vă așteptăm! Nu este cel mai mare birou, dar este foarte frumos.'),(46.54,49.54,'Vă așteptăm la consultații, dragilor! Ola Accountancy Birmingham.'),(49.54,50.9,'Numai bine!')],
'2026-04-22-182100633':[(0.0,10.0,'Unul dintre cele mai importante motive pentru care am succes, dragilor, este că sunt mai rapid decât ceilalți.'),(10.0,14.0,'Alții zic: căutăm un răspuns, vă dăm răspuns săptămâna viitoare.'),(14.0,19.0,'Eu am făcut deja trei greșeli și am găsit o cale mult mai rapidă.'),(19.0,25.0,'În loc de „îți scriu săptămâna viitoare”, de la mine o să auzi: „îți scriu mâine”.'),(25.0,35.0,'Așa câștigi oamenii, îți construiești o reputație și te dezvolți ca om.'),(35.0,39.0,'Astăzi oamenii caută rapiditatea asta.'),(39.0,43.0,'Dacă nu o ai în sânge, mai bine te angajezi.')]}
H="""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,DejaVu Sans,72,&H00FFFFFF,&H00FFFFFF,&H00241A0B,&H96241A0B,1,0,0,0,100,100,0,0,1,7,2,2,90,90,520,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
def ts(x): h=int(x//3600);m=int(x%3600//60);s=x%60;return f"{h}:{m:02d}:{s:05.2f}"
for k,segs in S.items():
    L=[]
    for a,b,txt in segs:
        w=txt.split(); n=max(1,round(len(w)/4)); chunks=[w[i*len(w)//n:(i+1)*len(w)//n] for i in range(n)]
        d=(b-a)/n
        for i,c in enumerate(chunks): L.append(f"Dialogue: 0,{ts(a+i*d)},{ts(a+(i+1)*d)},Cap,,0,0,0,,{' '.join(c)}")
    open(k+'.ass','w').write(H+'\n'.join(L)+'\n')
print('ok')
