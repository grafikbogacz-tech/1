import sys,json,os;sys.path.insert(0,'build')
from ig import *
Z=json.load(open('build/adsz.json')) if os.path.exists('build/adsz.json') else {}
def W(n,inner,gap=16):write('str-'+n,inner,gap,Z.get(n,1))
L='C · Google Ads'
def table(rows,cols_w,head=None,fs=12.5):
    g=' '.join(cols_w);o=''
    if head:o+=f'<div style="display:grid;grid-template-columns:{g};gap:0 14px;border-bottom:2px solid {T};padding:0 0 6px">'+''.join(f'<div style="{M};color:{G}">{h}</div>' for h in head)+'</div>'
    for r in rows:
        o+=f'<div style="display:grid;grid-template-columns:{g};gap:0 14px;border-bottom:1px solid {H};padding:8px 0;align-items:start">'
        for i,c in enumerate(r):
            o+=f'<div style="font-size:{13.5 if i==0 else fs}px;{"font-weight:500;color:#111;" if i==0 else "line-height:1.4;color:#333;"}">{c}</div>'
        o+='</div>'
    return o
# 178
p=lab(L+' · standard')+h1('Najpierw produkt, potem cena.',32)+para('Reklama Google Ads nie deklaruje wartości marki, tylko pokazuje jej źródło. Każda reklama układa się w tej samej kolejności.',8)
p+=f'<div style="margin-top:14px">{sub("Hierarchia komunikatu",T)}'+steps([('01','Produkt'),('02','Autentyczność / cecha'),('03','Zastosowanie'),('04','Cena / warunek'),('05','CTA')],0)+'</div>'
p+=box('Odwrócona kolejność — nie stosujemy','CENA → RABAT → PRESJA → PRODUKT',12)
p+=cols(f'{sub("Mówimy",G)}'+li(['autentyczna stara cegła rozbiórkowa','naturalne zróżnicowanie koloru i struktury','realny materiał, nie imitacja','konkretne zastosowanie','możliwość zamówienia próbki','wybór wariantu: kolor, struktura, zastosowanie','producent i proces — jeśli zgodne z faktami'],'+',G),f'{sub("Unikamy",T)}'+li(['„najniższa cena na rynku” bez dowodu','„taniej już nie będzie”, „super promocja”','„wysoka jakość dla wymagających” bez konkretu','„modne rozwiązanie z duszą”','„pasuje do każdego wnętrza”, „wyjątkowy efekt”','presji sprzedażowej bez argumentu produktowego'],'−',T),18,26)
p+=box('Zasada Brand Booka','Nie deklarujemy wartości. Pokazujemy jej źródło.',16)
p+=libref('ADS-01 · ADS-02 · ADS-03 · ADS-04 · ADS-05')
W('178',p,0)
# 179
th=[('A. Produkt','Płytki ze starej cegły<br>Płytki z cegły rozbiórkowej<br>Płytki ceglane na ścianę<br>Płytki ceglane na elewację'),
('B. Wyróżnik','Autentyczna stara cegła<br>Naturalna struktura materiału<br>Każda partia jest inna<br>Prawdziwa cegła, nie imitacja'),
('C. Zastosowanie','Do wnętrz i elewacji<br>Zobacz realizacje<br>Porównaj warianty<br>Wybierz model do swojego wnętrza'),
('D. Decyzja / CTA','Zamów próbkę<br>Zobacz dostępne modele<br>Sprawdź ofertę<br>Porównaj kolory i struktury'),
('E. Cena / promocja','Wybrane modele w promocji<br>Sprawdź aktualną cenę<br>Zobacz warunki oferty<br>— tylko gdy aktualna')]
p=lab(L+' · Search')+h1('Reklama Search (RSA).',32)+para('Każda grupa reklam ma zestaw nagłówków z pięciu kategorii. Z każdej wybieramy 1–2 nagłówki, żeby reklama mówiła pełnym zdaniem.',8)
p+=f'<div style="margin-top:12px">'+table(th,['150px','1fr'],['Kategoria','Przykładowe nagłówki'],12.5)+'</div>'
p+=f'<div style="margin-top:18px">{sub("Opis reklamy — kolejność",T)}'+steps([('1','Fakt'),('2','Produkt'),('3','Zastosowanie'),('4','CTA')],0)+'</div>'
p+=box('Przykład opisu','„Płytki z autentycznej starej cegły rozbiórkowej. Zobacz dostępne warianty koloru i struktury, realizacje oraz zamów próbkę przed wyborem.”',14)
p+=libref('ADS-03 · ADS-04 · ADS-05')
W('179',p,0)
# 180
rows=[('„płytki ceglane na elewację”','reklama o elewacji','kategoria / podstrona elewacyjna'),('„płytki RETRO”','reklama RETRO','karta / kategoria RETRO'),('„próbki płytek ceglanych”','reklama próbki','strona zamówienia próbki')]
p=lab(L+' · Display i landing page')+h1('Kreacja i strona docelowa.',32)
p+=card('01','Standard kreacji Display',cols(li(['realny produkt lub realizacja jako główny obraz','jedna informacja główna','maksymalnie jedno CTA','produkt nazwany przed rabatem'],'+',G),li(['bez przeładowania cenami','zdjęcie nie zniekształca koloru cegły','logo identyfikuje, nie dominuje','spójność z Brand Bookiem i stroną www'],'+',G),10),10)
p+=f'<div style="margin-top:12px">{sub("Typy kreacji",G,6)}{chips(["produkt","realizacja","próbka","porównanie","proces / autentyczność","promocja"],G)}</div>'
p+=card('02','Landing page — jedna ścieżka',para('Fraza, reklama i landing page tworzą jedną ścieżkę. Nie kierujemy wszystkiego do strony głównej.',6)+f'<div style="margin-top:10px">'+table(rows,['1fr','1fr','1fr'],['Fraza','Reklama','Landing page'],12.5)+'</div>',10)
p+=f'<div style="margin-top:6px">{sub("Pierwszy ekran landing page potwierdza obietnicę",T)}'+steps([('1','Ten sam produkt'),('2','Ta sama intencja'),('3','Ta sama promocja'),('4','Jasne CTA')],0)+'</div>'
p+=libref('ADS-01 · ADS-02')
W('180',p,14)
# 181
p=lab(L+' · promocje i assety')+h1('Promocje, sitelinki, callouty.',32)
p+=card('01','Promocje — osobna logika',para('Promocja jest ofertą, nie osobowością marki. Każda ma pięć elementów:',6)+steps([('1','Produkt'),('2','Warunek'),('3','Czas obowiązywania'),('4','Osobny landing lub sekcja'),('5','Cena zgodna ze stroną')],10),10)
p+=card('02','Priorytetowe sitelinki',f'<div style="margin-top:10px">{chips(["Produkty","Zamów próbkę","Realizacje","Montaż / poradniki","Kontakt"],G)}</div><div style="margin-top:6px">{chips(["Promocje — tylko gdy aktywne"],T)}</div>',10)
p+=card('03','Objaśnienia (callouty)',para('Opieramy je na konkretach:',6)+f'<div style="margin-top:8px">{chips(["autentyczna stara cegła","próbki przed zakupem","realne realizacje","różne warianty koloru i struktury"],G,True)}</div>'+f'<div style="margin-top:12px">{sub("Nie używamy",T)}'+li(['„najniższa cena na rynku” jako stałego assetu marki','ogólników bez pokrycia'],'−',T)+'</div>',10)
p+=libref('ADS-04 · ADS-05')
W('181',p,16)
