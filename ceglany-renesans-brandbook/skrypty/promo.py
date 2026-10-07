import sys,re,subprocess;sys.path.insert(0,'build')
from fotopages import *
import fotopages as FP
def item(n,t,fmt,jak,unik,pg=None,last=False):
    ref=f'<span style="{M};border:1px solid {G};color:{G};padding:2px 7px;white-space:nowrap;align-self:start">str. {pg}</span>' if pg else f'<span></span>'
    return f'<div style="border-top:{"2px solid "+T};padding:12px 0 14px;display:grid;grid-template-columns:44px 1fr auto;gap:12px"><span style="{MF};font-weight:300;font-size:30px;letter-spacing:-.05em;color:{T};line-height:1">{n:02d}</span><div><div style="display:flex;gap:10px;align-items:baseline;flex-wrap:wrap"><span style="font-size:17px;font-weight:500;letter-spacing:-.02em;color:#111">{t}</span><span style="{M};color:#767676">{fmt}</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:8px"><div>{sub("Jak",G,3)}<div style="font-size:12.5px;line-height:1.45;color:#333">{jak}</div></div><div>{sub("Unikać",T,3)}<div style="font-size:12.5px;line-height:1.45;color:#333">{unik}</div></div></div></div>{ref}</div>'
A=[('Wizytówka','85 × 55 mm','logo po jednej stronie, dane kontaktowe w mono, czerń i jeden akcent terakoty.','gęstego tekstu, tła zdjęciowego, więcej niż jednego koloru akcentu.',69),
('Papier firmowy i prezentacja','A4 i 16:9','jedna myśl na slajd, duże zdjęcie, numer w mono, nagłówek w lewym górnym rogu.','ciemnych teł, punktorów, ozdobnych ramek.',69),
('Katalog PDF','A4 pionowo','kolekcja na stronie, zdjęcie + tabela parametrów, spis w mono.','gęstych stron i drobnego druku.',70),
('Druk: karty próbek i etykiety','papier matowy','papier naturalny, logo min. 15 mm, czerń i jeden akcent.','błyszczącej folii, metalicznych farb, ozdobnych ramek.',70),
('Stopka email i sygnatura','tekst + logo','imię, rola, telefon, logo w jednej linii, kolor terakoty tylko na linku.','grafik w stopce, cytatów, kilku fontów.',71)]
B=[('Banery reklamowe','Google Ads i display','biel, zdjęcie, jedna obietnica, przycisk główny.','kilku komunikatów, pomarańczowego tła, haseł cenowych jako głównej obietnicy.',72),
('Materiały sprzedażowe','oferta, wycena, próbki','karta próbki na beżu, parametry w mono, kontakt na dole.','przeładowanych tabel.',None),
('Karty produktów','A4 pionowo i karta online','zdjęcie, tabela parametrów, uwaga o naturalnych różnicach partii.','tekstu marketingowego zamiast danych.',None),
('Opakowania i merchandise','karton, taśma, torba','logo na jednolitym tle, jedna barwa, kraft lub biel.','zdjęć na opakowaniu, wielu kolorów, haseł reklamowych.',73)]
def p67():
    p=lab('Przegląd · materiały promocyjne (1/2)')+h1('Jeden system, dziewięć materiałów.',30)
    p+=para('Zmienia się format i skala, nie reguły. Szczegóły każdego materiału są na kolejnych stronach — przy numerze podajemy, gdzie.',8)
    p+='<div style="margin-top:14px">'+''.join(item(i+1,*a) for i,a in enumerate(A))+'</div>'
    return p
def p68():
    p=lab('Przegląd · materiały promocyjne (2/2)')+h1('Sprzedaż, karty i opakowania.',30)
    p+='<div style="margin-top:14px">'+''.join(item(i+6,*a) for i,a in enumerate(B))+'</div>'
    p+=f'<div style="margin-top:20px;border-top:2px solid {T};padding-top:12px">{sub("Wspólne elementy każdego materiału",T)}{chips(["logo","zdjęcie z podpisem źródła","linia","numer","znacznik","CTA"],G,True)}</div>'
    p+=box('Kanały cyfrowe','Facebook, Instagram, TikTok i www opisują części IV B i IV C.',16)
    return p
def bottom(n):
    o=subprocess.run(['node','pag/fitabs.js','all/project',f'str-{n}.dc.html'],capture_output=True,text=True).stdout
    m=re.search(r'bottom: (\d+)',o);return int(m.group(1)) if m else 9999
for n,f in (('067',p67),('068',p68)):
    p=f();FP.mywrite(n,p,1.0);b=bottom(n)
    z=max(1.0,min(1.45,round(0.985*920/max(b-100,1),2)))
    while True:
        FP.mywrite(n,p,z);b=bottom(n)
        if b<=1022 or z<=1.0:break
        z=round(z-0.02,2)
    print(n,z,b)
