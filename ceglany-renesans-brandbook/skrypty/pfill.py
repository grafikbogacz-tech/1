import sys,re,subprocess;sys.path.insert(0,'build')
from fotopages import *
import fotopages as FP
import ig
PR=f'<span style="{M};color:{T};border:1px solid {T};padding:2px 7px;margin-left:10px;vertical-align:middle">Propozycja</span>'
def title(lb,t):return f'<div style="{M};letter-spacing:.14em;color:{T}">{lb}</div>'+h1(t,30)
def bond(n=3,w=300,h=26,stroke='#111',offset=True,cut=False):
    rows=''
    bw=w/3
    for r in range(n):
        y=r*(h+6)
        xs=[0,bw,2*bw] if r%2==0 else [-bw/2,bw/2,1.5*bw,2.5*bw]
        for x in xs:
            x0=max(0,x);x1=min(w,x+bw)
            rows+=f'<rect x="{x0:.1f}" y="{y}" width="{x1-x0-4:.1f}" height="{h}" fill="none" stroke="{stroke}" stroke-width="1.5"/>'
    ht=n*(h+6)
    cl=f'<line x1="{bw*1.5}" y1="-4" x2="{bw*1.5}" y2="{ht}" stroke="{T}" stroke-width="2" stroke-dasharray="4 4"/>' if cut else ''
    return f'<svg viewBox="0 -4 {w} {ht+4}" width="100%" style="display:block">{rows}{cl}</svg>'
def p62():
    o=title('38 · Styl ilustracji / grafik','Mniej ilustracji. Więcej materiału.')+PR.replace('margin-left:10px;','margin-top:8px;align-self:flex-start;')
    o+=para('Marka nie opiera się na ilustracjach. Jej obrazem jest prawdziwa cegła, dlatego rysunek pojawia się tylko tam, gdzie fotografia nie pomoże: w schematach procesu i montażu.',10)
    o+=f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:18px"><div><div style="border:1px solid #DCDCDC;padding:18px 16px">{bond(4,300,34,"#111",cut=True)}</div><div style="margin-top:6px;{M};color:{G}">Tak · schemat liniowy</div></div><div><div style="border:1px solid #DCDCDC;padding:18px 16px;height:100%;display:flex;align-items:center;justify-content:center"><div style="font-size:48px;line-height:1;color:#CBCAC4;{MF}">✕</div></div><div style="margin-top:6px;{M};color:{T}">Nie · clipart i 3D</div></div></div>'
    o+=tn(['linia 1,5 px, czarna, bez wypełnień','jeden akcent: terakota','kąty proste, spójne z ikonami (str. 52)','podpis przy każdym schemacie'],['clipartów i ilustracji dekoracyjnych','efektów 3D i gradientów','postaci i maskotek','wielu kolorów w jednym rysunku'],'Schemat: tak','Nie',20)
    o+=box('Zasada','Zanim narysujesz, zapytaj, czy zdjęcie nie pokaże tego lepiej. Mniej grafiki interfejsu, więcej materiału (str. 136).',18)
    return o
def p63():
    o=title('39 · Elementy graficzne / motywy dodatkowe','Wzór z cegły.')+PR.replace('margin-left:10px;','margin-top:8px;align-self:flex-start;')
    o+=para('Jedyny motyw dodatkowy marki wynika z produktu: wiązanie cegieł, w którym kolejny rząd jest przesunięty o pół cegły (jak w siatce na stronie 51). Używamy go rzadko i cicho. Pozostałe detale opisuje strona 64.',10)
    pats=[('#111','#fff','Czarna linia na bieli'),(T,B,'Terakota na beżu'),('#fff',G,'Biała linia na granacie')]
    o+='<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:18px">'+''.join(f'<div><div style="background:{bg};padding:14px 12px">{bond(6,200,22,fg)}</div><div style="margin-top:6px;{M};color:#767676">{lb}</div></div>' for fg,bg,lb in pats)+'</div>'
    o+=f'<div style="margin-top:22px">{sub("Gdzie stosujemy",T)}{chips(["tło stron tytułowych","okładki serii","opakowania","karta próbki"],G)}</div>'
    o+=tn(['jeden kolor linii','linia 1 px','tylko pod pustą powierzchnią','niski kontrast względem tła'],['pod tekstem i zdjęciem','wypełnień kolorem','kilku wzorów naraz','cegły jako tekstury zdjęciowej'],'Tak','Nie',22)
    return o
def p71():
    o=title('43 · Stopka email i sygnatura','Jedna linia, jeden akcent.')+PR.replace('margin-left:10px;','margin-top:8px;align-self:flex-start;')
    sig=f'<div style="border:1px solid #DCDCDC;padding:34px 28px;margin-top:18px;display:flex;gap:26px;align-items:center"><img class="lg" src="logo-or.svg" alt="Ceglany Renesans" style="width:150px;flex:none"/><div style="border-left:2px solid {T};padding-left:18px"><div style="font-size:15px;font-weight:600">[Imię i nazwisko]</div><div style="{M};color:#767676;margin-top:2px">[stanowisko]</div><div style="font-size:13px;margin-top:8px;color:#111">[telefon] · [e-mail]</div><div style="font-size:13px;margin-top:2px"><span style="border-bottom:2px solid {T}">www.ceglanyrenesans.pl</span></div></div></div>'
    o+=sig
    o+=f'<div style="margin-top:20px">{sub("Budowa",T)}'+steps([('01','Imię i rola'),('02','Telefon i e-mail'),('03','Logo'),('04','Jeden link')],0)+'</div>'
    o+=tn(['tekst Hanken Grotesk 13 px, czarny','logo min. 55 px','kolor terakoty tylko na linku lub linii','jeden numer telefonu'],['grafik i banerów w stopce','cytatów i sloganów','kilku fontów','kilku numerów telefonu'],'Tak','Nie',22)
    o+=box('Zasada','Stopka jest podpisem, nie reklamą. Jeden przycisk lub link, bez promocji (str. 88).',18)
    return o
def p73():
    o=title('45 · Opakowania i merchandise','Logo na kraftcie i bieli.')+PR.replace('margin-left:10px;','margin-top:8px;align-self:flex-start;')
    items=[('Karton','#BFA27F','logo-k.svg',70),('Taśma','#fff','logo-or.svg',70),('Torba','#EDE9D0','logo-k.svg',70)]
    o+='<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:18px">'+''.join(f'<div><div style="height:240px;background:{bg};box-shadow:inset 0 0 0 1px #DCDCDC;display:flex;align-items:center;justify-content:center"><img class="lg" src="{lg}" alt="" style="width:{w}px"/></div><div style="margin-top:6px;{M};color:#767676">{n}</div></div>' for n,bg,lg,w in items)+'</div>'
    o+=tn(['jednolite tło: kraft lub biel','logo w jednej barwie','logo min. 15 mm','papier matowy, naturalny'],['zdjęć na opakowaniu','wielu kolorów','haseł reklamowych','folii i złoceń'],'Tak','Nie',22)
    o+=box('Zasada','Opakowanie ma być spokojne: materiał mówi sam za siebie. Logo na jednolitym tle, bez dodatków.',18)
    return o
def bottom(n):
    o=subprocess.run(['node','pag/fitabs.js','all/project',f'str-{n}.dc.html'],capture_output=True,text=True).stdout
    m=re.search(r'bottom: (\d+)',o);return int(m.group(1)) if m else 9999
for n,f,rh in (('062',p62,'Część III · 38 Styl ilustracji'),('063',p63,'Część III · 39 Motywy dodatkowe'),('071',p71,'Część IV A · 43 Stopka email'),('073',p73,'Część IV A · 45 Opakowania')):
    pp=f();FP.mywrite(n,pp,1.0);b=bottom(n)
    z=max(1.0,min(1.4,round(0.985*920/max(b-100,1),2)))
    while True:
        FP.mywrite(n,pp,z);b=bottom(n)
        if b<=1022 or z<=1.0:break
        z=round(z-0.02,2)
    s=open(ig.P+f'str-{n}.dc.html').read()
    s=re.sub(r'<div class="rh"><span>.*?</span>',f'<div class="rh"><span>{rh}</span>',s,count=1)
    open(ig.P+f'str-{n}.dc.html','w').write(s)
    print(n,z,b)
