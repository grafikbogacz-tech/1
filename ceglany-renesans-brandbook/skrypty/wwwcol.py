import sys,json;sys.path.insert(0,'build')
from ig import *
P='all/project/project/'
RL='#CC0000'
def sw(c,name,sub_,border=False,w=None):
    b='border:1px solid #DCDCDC;' if border else ''
    return f'<div><div style="height:46px;background:{c};{b}"></div><div style="font-size:13px;font-weight:500;color:#111;margin-top:6px;line-height:1.25">{name}</div><div style="font-size:12px;color:#555;line-height:1.35;margin-top:2px">{sub_}</div></div>'
def table(rows,cols_w,head=None,fs=12.5):
    g=' '.join(cols_w);o=''
    if head:o+=f'<div style="display:grid;grid-template-columns:{g};gap:0 14px;border-bottom:2px solid {T};padding:0 0 6px">'+''.join(f'<div style="{M};color:{G}">{h}</div>' for h in head)+'</div>'
    for r in rows:
        o+=f'<div style="display:grid;grid-template-columns:{g};gap:0 14px;border-bottom:1px solid {H};padding:9px 0;align-items:start">'
        for i,c in enumerate(r):
            o+=f'<div style="font-size:{13.5 if i==0 else fs}px;{"font-weight:500;color:#111;" if i==0 else "line-height:1.4;color:#333;"}">{c}</div>'
        o+='</div>'
    return o
def chip(c,txt,fg='#fff',b=''):return f'<span style="display:inline-block;background:{c};color:{fg};{b}font-size:12px;padding:2px 8px;margin:0 4px 4px 0;font-family:\'Overpass Mono\',monospace;letter-spacing:.04em">{txt}</span>'
L='F · Strona internetowa · kolory'
# pw12
obs=[('#FFFFFF','Biel i jasna szarość','tła, nawigacja, karty',True),('#250500','Bardzo ciemny brąz / bordo','kalkulator, formularz, pasek ikon',False),('#ED6842','Koral / pomarańcz','CTA, etykiety produktowe',False),(RL,'Intensywna czerwień','górny pasek promocyjny, „NOWOŚĆ”',False),('#FFD400','Żółty','komunikaty „przy zakupie chemii”',False),('#3DAA3D','Zielony','komunikaty o wysyłce',False),('#000000','Czerń','tekst, logo w części materiałów',False),('#E4E4E4','Szarości interfejsu','pola, tła pomocnicze',True)]
p=lab(L)+h1('Analiza kolorów strony.',32)+para('Kolory widoczne na zrzutach strony. Odcienie na próbkach są przybliżone, odczytane z ekranu.',8)
p+='<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:16px">'+''.join(sw(c,n,s,b) for c,n,s,b in obs)+'</div>'
p+=box('Problem','żaden z tych kolorów nie jest zły sam w sobie. Problemem jest to, że jednocześnie działają jak osobne systemy.',20)
p+=cols(sub('Co działa')+li(['biel jako baza: daje produktowi oddech i pozwala cegle być głównym elementem,','pomarańczowo-koralowe CTA są blisko koloru identyfikacji #ED6842,','ciemny kolor dobrze sprawdza się w sekcjach wymagających kontrastu: formularzach i narzędziach.'],'+',G),sub('Co osłabia spójność',T)+li(['jednocześnie czerwień, pomarańcz, bordo, żółć i zieleń,','użytkownik nie wie, który kolor jest kolorem marki,','efekt jest „sklepowy”, ale nie buduje rozpoznawalności Ceglanego Renesansu.'],'×',T),20)
p+=f'<div style="margin-top:20px">{sub("Obecny kod kolorów",T)}'+table([('Czerwień','promocja'),('Żółty','promocja chemii'),('Pomarańcz','CTA'),('Bordo','ważne sekcje'),('Zielony','wysyłka')],['120px','1fr'])+'</div>'
write('pw12',p,0)
# pw13
p=lab(L)+h1('Cztery elementy, które osłabiają markę.',30)
rows=[('1. Czerwony pasek na górze','intensywna czysta czerwień wygląda jak kolor alarmowy i wyprzedażowy; przy ciągłej ekspozycji przejmuje stronę i osłabia kolor marki.',chip('#ED6842','#ED6842','#000')+'z czarnym tekstem<br>'+chip('#0D4C73','#0D4C73')+'z białym tekstem'),
('2. Żółte etykiety „PRZY ZAKUPIE CHEMII”','bardzo widoczne, ale wyglądają jak element obcej identyfikacji; żółty nie należy do palety marki.',chip('#ED6842','#ED6842','#000')+chip('#EDE9D0','#EDE9D0','#000')+chip('#0D4C73','#0D4C73')),
('3. Zielone komunikaty wysyłkowe','zrozumiałe jako „pozytywna informacja”, ale w obecnym systemie to kolejny mocny kolor.','zielony tylko jako kolor statusu („wysyłka dziś”, „dostępne”); nie w przyciskach, nagłówkach i banerach'),
('4. Bardzo ciemny brąz / bordo','kalkulator, formularz i pasek ikon; dobrze współgra z cegłą, ale nie wynika z palety; mamy już oficjalny ciemny kolor.',chip('#0D4C73','#0D4C73')+chip('#000000','#000000')+'<br>bez dodawania nowego brązu do palety')]
p+=f'<div style="margin-top:16px">{table(rows,["150px","1fr","170px"],["Element","Problem","Zamiast"])}</div>'
p+=box('Decyzja do podjęcia','albo świadomie wprowadzamy ciemny brąz jako nowy kolor funkcjonalny, albo (bezpieczniej dla Brand Booka) zastępujemy go granatem #0D4C73 lub czernią. Na dziś paleta nie jest rozszerzana o kolejny brąz.',22)
write('pw13',p,0)
# pw14
sysr=[('#FFFFFF','Biel','główne tło',True),('#000000','Czarny','tekst',False),('#ED6842','#ED6842','główny akcent i CTA',False),('#0D4C73','#0D4C73','ciemny kontrast, sekcje techniczne',False),('#EDE9D0','#EDE9D0','spokojne tło',True),('#EA4D70','#EA4D70','bardzo sporadyczny akcent',False),('#3DAA3D','Zielony','tylko status funkcjonalny',False)]
p=lab(L)+h1('Docelowo: jeden prosty system kolorów.',30)
p+='<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:16px">'+''.join(sw(c,n,s,b) for c,n,s,b in sysr)+'</div>'
p+=f'<div style="margin-top:24px">{sub("Proponowany system dla WWW",T)}'+table([('CTA główne','#ED6842 + czarny tekst'),('CTA drugorzędne','białe tło + czarny tekst + obrys'),('Sekcje techniczne, kalkulatory, formularze','#0D4C73 + biały tekst albo białe tło + czarny tekst'),('Tła pomocnicze','#EDE9D0'),('Promocje','bez osobnego czerwonego i żółtego systemu; promocję pokazujemy przez #ED6842, typografię i etykietę'),('Statusy systemowe','zielony: tylko wysyłka i dostępność; czerwony: tylko błąd lub ostrzeżenie; nigdy jako branding')],['190px','1fr'])+'</div>'
p+=f'<div style="background:#000;color:#fff;padding:20px 24px;margin-top:22px"><div style="{M};color:{T}">Zasada dla Brand Booka</div><div style="font-size:19px;font-weight:300;letter-spacing:-.03em;line-height:1.3;margin-top:8px">Produkt ma być najbardziej kolorowym elementem strony. Interfejs powinien być spokojniejszy niż cegła.</div></div>'
p+=para('Kolor nie koduje każdej funkcji osobnym odcieniem. Największy problem obecnej strony to nie „złe kolory”, ale brak hierarchii kolorów.',14)
write('pw14',p,0)
print('ok')
