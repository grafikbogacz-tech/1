import sys,json,re;sys.path.insert(0,'build')
from ig import *
Z=json.load(open('build/ytz.json')) if len(sys.argv)>1 else {}
def W(n,inner,gap=16):write('str-'+n,inner,gap,Z.get(n,1))
L='D · YouTube'
def table(rows,cols_w,head=None,fs=12.5):
    g=' '.join(cols_w);o=''
    if head:o+=f'<div style="display:grid;grid-template-columns:{g};gap:0 14px;border-bottom:2px solid {T};padding:0 0 6px">'+''.join(f'<div style="{M};color:{G}">{h}</div>' for h in head)+'</div>'
    for r in rows:
        o+=f'<div style="display:grid;grid-template-columns:{g};gap:0 14px;border-bottom:1px solid {H};padding:8px 0;align-items:start">'
        for i,c in enumerate(r):
            o+=f'<div style="font-size:{13.5 if i==0 else fs}px;{"font-weight:500;color:#111;" if i==0 else "line-height:1.4;color:#333;"}">{c}</div>'
        o+='</div>'
    return o
def rolecard(n,t,items):return f'<div style="border-top:2px solid {T};padding-top:10px"><div style="{MF};font-weight:300;font-size:26px;letter-spacing:-.05em;color:{T};line-height:1">{n}</div><div style="font-size:15px;font-weight:500;letter-spacing:-.02em;margin-top:6px;color:#111">{t}</div><div style="margin-top:8px">{li(items,"·",G,12.5,3)}</div></div>'
# 187
p=lab(L)+h1('Biblioteka wiedzy, realizacji i dowodów.',30)+para('YouTube nie jest archiwum przypadkowych filmów. Ma być uporządkowaną biblioteką wiedzy, realizacji i dowodów autentyczności produktu.',10)
p+=f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px 26px;margin-top:20px">'+rolecard('01','Edukacja',['montaż, fuga, impregnacja','wybór materiału','najczęstsze błędy'])+rolecard('02','Inspiracja',['realizacje i wnętrza','elewacje','zastosowania'])+rolecard('03','Dowód wartości',['autentyczna stara cegła','proces i selekcja','naturalne różnice materiału'])+rolecard('04','Wsparcie decyzji',['porównania produktów','zastosowania, próbka','właściwa karta produktu, kontakt'])+'</div>'
p+=f'<div style="margin-top:24px">{sub("Główna logika kanału",T)}'+steps([('01','Inspiracja'),('02','Wiedza'),('03','Produkt'),('04','Decyzja')],0)+'</div>'
p+=f'<div style="margin-top:24px">{sub("Kody materiałów w bibliotece",T)}'+chips(['YT-K kanał','YT-B banner','YT-M miniatura','YT-F film','YT-O opis / tytuł / CTA','YT-P playlista'])+'</div>'
p+=f'<div style="font-size:12.5px;line-height:1.45;color:#333;margin-top:16px">Przykłady z kanału: YT-01 – YT-05, strony 194–198.</div>'
W('187',p,0)
# 188
fm=[('A','Film pełny 16:9','3–8 minut','poradnik, porównanie, case study, proces, większy temat edukacyjny'),('B','Short','1 Short = 1 pytanie = 1 odpowiedź','jeden etap, jedna wskazówka, jeden błąd, jeden detal produktu'),('C','Krótka realizacja / inspiracja','produkt + miejsce + efekt','jedno zdanie wyjaśnienia')]
fl=''.join(card(a,b,row('Format',c)+row('Zastosowanie',d),10) for a,b,c,d in fm)
ser=[('Montaż starej cegły',['przygotowanie podłoża','klejenie','rozmieszczenie','fugowanie','wygładzanie','impregnacja','najczęstsze błędy']),('Poznaj produkt',['CLASSIC','RETRO','RUSTYKALNE','porównania modeli']),('Realizacje',['produkt w konkretnym wnętrzu','produkt na elewacji','produkt przy konkretnym materiale lub stylu']),('Od cegły do płytki',['odzysk','selekcja','cięcie','przygotowanie','pakowanie'])]
sl=''.join(f'<div style="margin-top:12px">{sub(a,G,4)}{chips(b)}</div>' for a,b in ser)
p=lab(L+' · formaty')+h1('Trzy formaty i cztery serie.',30)+f'<div style="display:flex;flex-direction:column;gap:12px;margin-top:6px">{fl}</div><div style="margin-top:22px">{sub("System serii",T)}{sl}</div>'
W('188',p,0)
# 189
con=['„Jak…?”','„Czy…?”','„X czy Y — czym się różnią?”','Produkt + zastosowanie','Produkt + kolor / struktura / efekt','Etap procesu: „…jak zrobić go poprawnie?”']
p=lab(L+' · tytuły i opisy')+h1('Tytuł, opis i jedno CTA.',30)
p+=card('01','System tytułów',cols(sub('Tytuł powinien')+li(['jasno mówić, czego dotyczy film,','zawierać produkt lub problem,','odpowiadać na pytanie lub zapowiadać wartość,','być poprawny językowo,','unikać pustych superlatywów.'],'+',G),sub('Unikamy',T)+li(['„wyjątkowy efekt”','„niesamowita realizacja”','„pasuje do każdego stylu”','„najpiękniejsza cegła”','„duży wybór modeli” bez dopowiedzenia'],'×',T),8)+f'<div style="margin-top:10px">{sub("Preferowane konstrukcje")}{chips(con,G)}</div>',10)
p+=card('02','System opisów',steps([('1','Pierwsze 1–2 zdania: czego dotyczy film'),('2','Nazwa produktu lub zastosowania'),('3','Link do właściwej podstrony'),('4','Jedno główne CTA')],10)+f'<div style="margin-top:12px">{sub("Zasada linkowania",T)}'+table([('Film produktowy','karta produktu lub kategoria'),('Film realizacyjny','realizacja lub produkt'),('Poradnik','poradnik, kategoria lub produkt'),('Film o próbce','strona zamówienia próbki')],['150px','1fr'],None,12)+'</div>',10)
p+=card('03','System CTA',f'<div style="margin-top:8px">{chips(["Zobacz produkt","Porównaj modele","Zamów próbkę","Zobacz realizację","Przeczytaj poradnik","Sprawdź dostępne warianty","Zobacz kolejną część serii"],G,True)}</div>'+para('Jedno główne CTA na film. Nie każdy film kończy się sprzedażą: CTA odpowiada etapowi decyzji użytkownika.',10),10)
W('189',p,18)
# 190 banner avatar nazwa
p=lab(L+' · kanał')+h1('Banner, avatar i nazwa kanału.',30)
p+=card('01','Banner',para('Ma w 2–3 sekundy odpowiedzieć: jaka to marka, co oferuje, czego można się spodziewać po kanale.',8)+cols(box('Kierunek komunikacyjny','Ceglany Renesans<br>Płytki z autentycznej starej cegły<br>realizacje • montaż • wiedza',0),box('Alternatywa produktowa','Ceglany Renesans<br>Płytki ze starej cegły rozbiórkowej<br>zobacz realizacje • poznaj montaż • wybierz produkt',0),10,16)+cols(li(['maks. 2–3 krótkie linie tekstu,','zdjęcie lub detal cegły wspiera komunikat,','logo czytelne, ale nie dominujące,','czytelny na telefonie.'],'+',G),li(['haseł „wyjątkowe wnętrza”, „najwyższa jakość”,','nadmiaru ikon i ozdobników,','nowej estetyki niezależnej od marki.'],'×',T),10),10)
p+=card('02','Avatar',cols(li(['najprostszy, najbardziej rozpoznawalny znak,','bez drobnego tekstu i sloganu,','sprawdzony w bardzo małym rozmiarze.'],'+',G),para('Avatar identyfikuje, nie informuje.',0),8),10)
p+=card('03','Nazwa kanału',row('Kierunek','„Ceglany Renesans”')+row('Ewentualnie','„Ceglany Renesans — płytki ze starej cegły”')+para('Nie rekomendujemy długiej nazwy przeładowanej słowami kluczowymi.',8),10)
W('190',p,18)
# 191 opis kanału
p=lab(L+' · kanał')+h1('Opis kanału.',32)
p+=card('04','Kolejność w opisie',steps([('1','Kim jesteśmy'),('2','Co produkujemy'),('3','Z czego powstaje produkt'),('4','Co znajdziesz na kanale'),('5','Dokąd przejść dalej')],10),10)
p+=box('Rekomendowana wersja','„Ceglany Renesans to producent płytek z autentycznej starej cegły rozbiórkowej. Materiał odzyskujemy, selekcjonujemy i przygotowujemy tak, aby zachować jego naturalne zróżnicowanie koloru, strukturę i ślady wieku.<br>Na kanale pokazujemy: montaż i fugowanie płytek ze starej cegły, gotowe realizacje we wnętrzach i na elewacjach, różnice między modelami, proces powstawania płytek, praktyczne wskazówki przed i po zakupie.<br>Jeśli chcesz zobaczyć produkty, realizacje lub zamówić próbkę, przejdź na stronę Ceglanego Renesansu.”',0)
p+=box('Wersja krótsza','„Produkujemy płytki z autentycznej starej cegły rozbiórkowej. Pokazujemy montaż, realizacje, produkty i proces powstawania materiału. Zobacz, jak stara cegła wygląda w gotowych wnętrzach i na elewacjach.”',12)
p+=para('Zasada: opis nie jest listą słów kluczowych SEO. Ma tłumaczyć, dlaczego warto zostać na kanale.',14)
W('191',p,16)
# 192 miniatury 1
th=[('1','Poradnik / montaż','człowiek przy pracy albo czytelny etap','„MONTAŻ KROK PO KROKU”, „JAK FUGOWAĆ?”, „IMPREGNACJA”, „NAJCZĘSTSZY BŁĄD”','pełnych zdań, wielu etapów, ozdobnych haseł'),
('2','DIY','realna osoba wykonująca czynność samodzielnie','„ZRÓB TO SAM”, „DASZ RADĘ?”, „KLEJENIE DIY”','— (cel: obniżyć barierę i pokazać prostotę zadania)'),
('3','Produkt / porównanie','detal produktu lub dwa warianty obok siebie','„CLASSIC”, „RETRO”, „RETRO VS CLASSIC”, „KTÓRY WYBRAĆ?”','— (cel: wspierać wybór)'),
('4','Realizacja','gotowy efekt: wnętrze, elewacja, ściana, podłoga','„RETRO NA ELEWACJI”, „CEGŁA W SALONIE”, „EFEKT KOŃCOWY”','— (fotografia najważniejsza, tekst pomocniczy)'),
('5','Proces / autentyczność','materiał, produkcja, cięcie, selekcja, dłonie, maszyna','„OD CEGŁY DO PŁYTKI”, „SELEKCJA”, „JAK POWSTAJE?”','— (cel: pokazać źródło wartości)'),
('6','Ludzie / kulisy','konkretna osoba podczas realnej pracy','„POZNAJ ZESPÓŁ”, „KULISY PRODUKCJI”','— (cel: zaufanie przez kompetencję)')]
p=lab(L+' · miniatury')+h1('System miniatur.',32)+para('Miniatury są spójne, czytelne na telefonie i od razu komunikują typ treści. Nie tworzymy osobnego języka wizualnego oderwanego od identyfikacji marki.',8)
p+=f'<div style="margin-top:12px">{sub("Wspólny szkielet miniatury",T)}{chips(["jedno mocne zdjęcie","2–4 słowa komunikatu","stałe miejsce na element marki","wysoki kontrast","bez drobnych opisów","bez powtarzania tytułu","maks. jeden komunikat"],G)}</div>'
p+=box('Zasada główna','miniatura zatrzymuje uwagę i nazywa temat; tytuł filmu dopowiada szczegóły.',14)
p+=f'<div style="margin-top:14px">{sub("Sześć typów",T)}'+table([(a+'. '+b,c,d) for a,b,c,d,e in th],['150px','1fr','1fr'],['Typ','Zdjęcie','Tekst (przykłady)'],12)+'</div>'
W('192',p,0)
# 193 miniatury 2
chk=['Czy bez czytania tytułu wiem, czego dotyczy film?','Czy tekst da się przeczytać na telefonie?','Czy jest maksymalnie jeden komunikat?','Czy miniatura wygląda jak materiał tej samej marki?','Czy zdjęcie pokazuje realny produkt, proces lub realizację?','Czy tekst nie powtarza pełnego tytułu?','Czy nie używamy generycznego hasła zamiast konkretu?','Czy miniatura nie jest przeładowana?']
cl=''.join(f'<div style="display:flex;gap:12px;align-items:center;border-bottom:1px solid {H};padding:7px 0;font-size:13px;color:#111"><span style="width:14px;height:14px;border:1.5px solid {G};flex:none"></span>{c}</div>' for c in chk)
p=lab(L+' · miniatury')+h1('Tekst, kolor, logo, kompozycja.',30)
p+=cols(card('01','Tekst na miniaturze',li(['2–4 słowa, maks. 2 linie,','duże litery, prosty krój,','bez kursywy i ozdobników,','bez całych zdań i emotikon.'],'+',G)+f'<div style="margin-top:8px"><span style="{M};color:{T}">Nie</span> „Płytki ceglane w studiu nagrań — montaż krok po kroku”<br><span style="{M};color:{G}">Tak</span> „MONTAŻ KROK PO KROKU”</div>',10),card('02','Kolory',li(['jeden kolor bazowy tekstu,','jeden opcjonalny akcent,','neutralne tło lub maska tylko, gdy trzeba,','bez osobnej palety dla YouTube.'],'+',G),10),0,22)
p+=cols(card('03','Logo / element marki',li(['mały, stały element w jednym miejscu,','nie konkuruje z tytułem,','bez dużego logo na środku,','położenie nie zmienia się w każdym filmie.'],'+',G),10),card('04','Kompozycja',li(['bohater po jednej stronie, tekst po drugiej,','ważny detal nie jest zasłonięty,','nic ważnego tam, gdzie YouTube nakłada interfejs,','sprawdzenie w małym podglądzie.'],'+',G),10),16,22)
p+=f'<div style="margin-top:18px">{sub("Checklista przed publikacją",T)}{cl}</div>'
W('193',p,0)
