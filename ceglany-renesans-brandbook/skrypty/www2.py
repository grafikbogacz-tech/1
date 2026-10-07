import re,sys,json,shutil
sys.path.insert(0,'build')
from ig import *
P='all/project/project/'
def lb(t,c='#0D4C73',mt=12):return f'<div style="{M};color:{c};margin-top:{mt}px">{t}</div>'
def tx(t):return f'<div style="font-size:13px;line-height:1.45;color:#333;margin-top:3px">{t}</div>'
def badge(r,p):
    if r=='Do poprawy':st='color:#ED6842;border:1px solid #ED6842'
    elif r=='Super':st='background:#0D4C73;color:#fff;border:1px solid #0D4C73'
    else:st='color:#0D4C73;border:1px solid #0D4C73'
    return f'<div style="{M};letter-spacing:.08em;{st};padding:3px 9px;white-space:nowrap">{r} · {p}%</div>'
E=[
(12,'Kontakt: nagłówek podstrony','Do poprawy',50,'podstrona informacyjna',
 'header, menu i bardzo ciemny brązowy pas z nagłówkiem „Kontakt / Ceglany Renesans”.',
 'strona jest funkcjonalnie czytelna; użytkownik wie, gdzie się znajduje.',
 'ciemny brąz jest spoza systemu Brand Booka; nagłówek ma ciężki, mało premium charakter; szary tekst na brązowym tle ma słabszą czytelność.',
 'białe tło lub subtelny beż #EDE9D0, mały label w Overpass Mono, nagłówek w Hanken Grotesk, terakota #ED6842 tylko jako akcent.',
 'usunąć brąz z hero podstron.',
 'Podstrony informacyjne nie potrzebują ciężkiego, ciemnego hero.'),
(13,'Formularz wyceny','Do poprawy',55,'formularz',
 'tekst informacyjny po lewej, zdjęcie i rozbudowany formularz po prawej.',
 'formularz zbiera dane, które realnie pomagają przygotować wycenę; to funkcjonalnie dobry element.',
 'wizualnie jest ciężki; ciemny brąz jest poza Brand Bookiem; pola są duże, ale brakuje oddechu i hierarchii; długa lista checkboxów wygląda technicznie.',
 'formularz na białym lub beżowym tle, w etapach: 1. dane kontaktowe, 2. powierzchnia, 3. rodzaj płytek, 4. dodatki, 5. wiadomość. Granat #0D4C73 dla nagłówka formularza lub sekcji pomocniczej.',
 'podzielić formularz na etapy, zdjąć brąz.',
 'Formularz wyceny powinien wyglądać jak narzędzie doradcze, nie panel administracyjny.'),
(14,'Blog: hero','Do poprawy',50,'strona kategorii bloga',
 'ciemny hero z opisem bloga, niżej siatka artykułów (zrzut wspólny z WWW-15).',
 'blog ma duży potencjał edukacyjny; tematy są praktyczne i zakupowe: kolor ścian, kolor cegły, fuga.',
 'hero jest zdecydowanie za ciężkie; długi blok tekstu na ciemnym tle wygląda jak SEO-copy, nie zaproszenie do wiedzy.',
 'etykieta „BLOG / PORADNIK”, nagłówek „Wiedza o starej cegle w praktyce”, 1–2 zdania. Resztę treści przenieść do intro poniżej lub na stronę kategorii.',
 'skrócić hero do etykiety, nagłówka i 1–2 zdań.',
 'Blog ma wyglądać jak biblioteka wiedzy, nie blok SEO.'),
(15,'Blog: karty artykułów','Dobry',65,'siatka kart artykułów',
 'trzy kolumny kart artykułów (zrzut wspólny z WWW-14).',
 'dobre zdjęcia, trzy kolumny, jasna struktura.',
 'karty są ciężkie: zaokrąglenia i cienie mocniejsze niż przyjęty kierunek marki; opisy urywają się przypadkowo.',
 'układ editorial: duże zdjęcie, mały label w Overpass Mono, tytuł, 1–2 linie leadu, link tekstowy „Czytaj”.',
 'zdjąć cienie i zaokrąglenia, skrócić lead do 1–2 linii.',
 'Blog powinien wyglądać bardziej jak magazyn materiałowy niż sklep.'),
(16,'Promocje: hero','Do poprawy',45,'strona kategorii promocji',
 'nagłówek „Aktualne promocje na nasze płytki ceglane” (zrzut wspólny z WWW-17).',
 'użytkownik od razu wie, że jest na stronie promocyjnej.',
 'znowu brązowe hero i dużo tekstu; komunikacja jest mocno cenowa („atrakcyjne ceny”, „najlepsze ceny”, „okazja”), co osłabia pozycjonowanie marki.',
 'etykieta „PROMOCJE”, nagłówek „Aktualne zestawy i oferty specjalne”, lead: „Promocje dotyczą wybranych produktów i zestawów. Sprawdź aktualne warunki.”',
 'przepisać hero bez haseł cenowych.',
 'Promocja ma być dodatkiem do produktu, nie osią komunikacji marki.'),
(17,'Promocje: lista produktów','Do poprawy',50,'listing produktów',
 'karty produktów z rabatem, ceną, wysyłką, licznikiem, ulubionymi, ilością i przyciskiem (zrzut wspólny z WWW-16).',
 'rabat jest widoczny, cena czytelna, przycisk wyraźny.',
 'za dużo konkurujących elementów: rabat, przekreślona cena, wysyłka, licznik, serce, ilość i przycisk; do tego zielony status, bordowa plakietka i pomarańczowy przycisk, więc system kolorów się rozjeżdża.',
 'uprościć kartę do: zdjęcie, nazwa, cena, rabat, jedno CTA. Status wysyłki jako mały tekst, bez osobnego mocnego koloru.',
 'zostawić pięć elementów na karcie, ujednolicić kolory.',
 'Karta produktu nie może wyglądać jak dashboard.'),
(18,'Outlet','Do poprawy',55,'strona kategorii outlet',
 'strona kategorii outlet z listą produktów.',
 'kategoria outlet jest jasna i potrzebna.',
 'hero znów zbyt ciężkie i sprzedażowe; produkty outletowe wyglądają jak standardowe, więc użytkownik nie rozumie, dlaczego są w outlecie.',
 'wyjaśnienie: outlet to końcówki partii, nadwyżki, konkretne ilości, produkty dostępne do wyczerpania. Na kartach: ilość dostępna, powód outletu, informacja, czy produkt jest pełnowartościowy.',
 'dodać wyjaśnienie outletu i dane na kartach.',
 'Outlet ma być transparentny, nie wyglądać jak „tańszy produkt gorszej jakości”.'),
(19,'Próbki','Dobry',65,'strona kategorii próbek',
 'karty próbek płytek.',
 'próbki są bardzo ważnym elementem procesu zakupowego; cena jest niska i wejście w produkt łatwe.',
 'karty są wizualnie takie same jak duże produkty; brakuje wyjaśnienia, co klient dostaje i co próbka pozwala ocenić.',
 'komunikat: próbka pokazuje realny kolor i strukturę, materiał jest naturalnie zróżnicowany, próbka nie gwarantuje identyczności całej partii.',
 'dodać krótkie wyjaśnienie, co daje próbka.',
 'Próbka jest narzędziem decyzji, nie tylko produktem za 14 zł.'),
(20,'Sekcja liczb','Do poprawy',40,'sekcja statystyk',
 'cztery statystyki na tle cegły.',
 'liczby budują skalę i wiarygodność.',
 'ikony są niespójne z kierunkiem marki; tło jest ciężkie, a cztery duże ikony konkurują z liczbami. Liczby wymagają weryfikacji, szczególnie „1 316 549 wyciętych cegieł” i „1 000 000 realizacji Klientów”, ta druga brzmi bardzo mocno i trzeba ją potwierdzić.',
 'bez ikon: sama liczba i krótki podpis na jasnym tle.',
 'usunąć ikony, zweryfikować liczby przed publikacją.',
 'Dane liczbowe to dowód, więc muszą być weryfikowalne.'),
(21,'Kontakt do zespołu i godziny pracy','Dobry',65,'sekcja kontaktowa',
 'realne osoby z imionami, telefonami i godzinami pracy.',
 'pokazuje ludzi, imiona, telefony i godziny pracy; to bardzo dobry element zaufania.',
 'układ wygląda jak stopka z 2018 roku: zdjęcia w kółkach, duże imiona i ikony tworzą wiele konkurujących elementów.',
 'zdjęcie prostokątne lub mały portret, imię, rola, telefon, e-mail. Godziny pracy osobno.',
 'uprościć układ osób, godziny wydzielić.',
 'Ludzie marki powinni być pokazani spokojnie i rzeczowo.'),
(22,'Płytki na podłogę: hero','Do poprawy',35,'strona kategorii podłogowej',
 'hero kategorii z hasłem „Terakota, którą pokochają Twoje stopy ❤️” (zrzut wspólny z WWW-23).',
 'wiadomo, jaka to kategoria.',
 'ton odbiega od marki: emoji, „musisz to poczuć”, „odważni”, „odkryj podłogi, które pokochasz”; to styl lifestyle / social media, nie marki materiałowej.',
 'komunikacja oparta na faktach: „Płytki ceglane na podłogę. Polerowane płytki z autentycznej starej cegły do wnętrz i wybranych zastosowań zewnętrznych.”',
 'przepisać hero bez emoji i haseł emocjonalnych.',
 'Ton głosu WWW ma być spokojniejszy niż w social mediach.'),
(23,'Kategoria podłogowa: produkty','Do poprawy',55,'listing produktów',
 'karty produktów z kategorii podłogowej (zrzut wspólny z WWW-22).',
 'zdjęcia pokazują produkt w realnym zastosowaniu.',
 'wszystkie karty mają ten sam rabat, dużo elementów interfejsu i mało informacji o różnicach między wariantami.',
 'karta bardziej produktowa: typ, format, kolorystyka, przeznaczenie, cena.',
 'dodać parametry różnicujące warianty.',
 'Na kategorii klient ma porównać produkty, nie tylko ceny.'),
(24,'Logowanie i rejestracja','Do poprawy',55,'ekran systemowy',
 'dwie kolumny: logowanie i rejestracja (zrzut wspólny z WWW-25).',
 'funkcjonalnie prosta struktura dwóch kolumn.',
 'formularze są surowe, z dużą pustą przestrzenią i słabą hierarchią; bordowe przyciski wychodzą poza paletę.',
 'biały układ, cienkie obramowanie, Hanken Grotesk, przycisk w #ED6842, spokojny tekst pomocniczy, bez ciężkich ramek.',
 'wprowadzić białe tło i przyciski w #ED6842.',
 'Także ekrany systemowe muszą być częścią identyfikacji.'),
(25,'Stopka rozszerzona','Do poprawy',50,'stopka strony',
 'rozbudowana stopka z logo, kontaktami, godzinami, danymi formalnymi i ofertą (zrzut wspólny z WWW-24).',
 'kontakt do ludzi jest wartościowy.',
 'stopka jest przeładowana: logo, e-mail, dwoje pracowników, godziny, dane formalne, oferta, sklep; to za dużo w jednym ekranie.',
 'cztery kolumny: 1. marka, 2. oferta, 3. pomoc, 4. formalne. Kontakt do konkretnych osób przenieść na stronę kontaktową.',
 'zbudować stopkę w czterech kolumnach.',
 'Stopka ma porządkować, nie powtarzać całej strony.'),
(26,'Dostawa i montaż','Dobry',65,'strona informacyjna',
 'nagłówek na brązowym tle i trzy kolumny tekstu o różnej długości.',
 'treść jest bardzo konkretna, cennik dostawy jasny.',
 'strona wygląda jak dokument tekstowy: nagłówek na brązowym tle i trzy kolumny o różnej długości.',
 'rozbić na bloki: odbiór osobisty, kurier, transport CEGMAR. W każdym: co, dla kogo, koszt, ważna informacja.',
 'zamienić tekst na trzy bloki z jednakową strukturą.',
 'Informacje logistyczne muszą być łatwe do zeskanowania.')]
tail='<div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n</x-dc><script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":794,"height":1123}}\'>class Component extends DCLogic{renderVals(){return {};}}</script></body></html>'
src=open(P+'str-215.dc.html').read()
head=src[:src.index('<div class="cr pg">')]
def page(tab,inner_abs):
    h=re.sub(r'<title>[^<]*</title>',f'<title>Strona {tab}</title>',head,1)
    return h+f'<div class="cr pg"><div class="tab">{tab}</div><div class="rh"><span>Biblioteka przykładów / Strona internetowa</span><span>Ceglany Renesans</span></div>'+inner_abs+tail
# move colors & G first (must read before overwrite)
for old,new in [(216,231),(217,232),(218,233),(219,236)]:
    s=open(P+f'str-{old}.dc.html').read()
    s=re.sub(r'class="tab">\d+',f'class="tab">{new}',s,1);s=re.sub(r'<title>[^<]*</title>',f'<title>Strona {new}</title>',s,1)
    open(P+f'str-{new}.dc.html','w').write(s)
for i,(n,t,r,p,typ,desc,ok,bad,better,rec,rule) in enumerate(E):
    tab=216+i;code=f'WWW-{n:02d}'
    H_=170
    body='<div style="position:absolute;left:76px;top:100px;width:642px;border-top:1px solid #E7DFC9"></div>'
    body+=f'<div style="position:absolute;left:76px;top:116px;width:642px;height:{H_}px;box-sizing:border-box;border:1px dashed #BDB7A0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px"><div style="{M};color:#0D4C73">Miejsce na screen</div><div style="font-size:12px;color:#767676">{code}</div></div>'
    y=116+H_+16
    head_row=f'<div style="display:flex;justify-content:space-between;align-items:center"><div style="{M};color:#ED6842">{code}</div>{badge(r,p)}</div><div style="font-size:18px;font-weight:500;letter-spacing:-.02em;line-height:1.2;margin-top:6px;color:#111">{t}</div><div style="font-size:12px;color:#767676;margin-top:4px">{typ}</div>'
    body+=f'<div class="wmid" style="position:absolute;left:76px;top:{y}px;width:642px">{head_row}{lb("Opis",mt=10)}{tx(desc)}<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px"><div>{lb("Co działa")}{tx(ok)}</div><div>{lb("Co poprawić","#ED6842")}{tx(bad)}</div></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:34px;border-top:1px solid #E7DFC9;padding-top:12px;margin-top:22px"><div>{lb("Przykład lepszej wersji",mt=0)}{tx(better)}</div><div>{lb("Rekomendacja",mt=0)}{tx(rec)}{lb("Reguła Brand Booka")}{tx(rule)}</div></div></div>'
    open(P+f'str-{tab}.dc.html','w').write(page(tab,body))
# conclusions
def card(n,t,ls,b):return f'<div style="border-top:2px solid {T};padding-top:10px"><div style="display:flex;gap:12px;align-items:baseline"><span style="{MF};font-weight:300;font-size:28px;letter-spacing:-.05em;color:{T};line-height:1">{n}</span><span style="font-size:16px;font-weight:500;letter-spacing:-.02em;color:#111">{t}</span></div><div style="font-size:12.5px;line-height:1.4;color:#333;margin-top:6px">{b}</div></div>'
def wrap(inner,z=1):return f'<div style="position:absolute;left:76px;top:100px;width:{round(642/z)}px;{"zoom:"+str(z)+";" if z!=1 else ""}display:flex;flex-direction:column">{inner}</div>'
cards=[card('1','Największy problem: kolor','','ciemny brąz występuje na wielu podstronach. Zastąpić: biel, beż #EDE9D0, granat #0D4C73, terakota #ED6842.'),
card('2','Typografia','','strona używa różnych stylów. Docelowo: Hanken Grotesk dla całej typografii systemowej i contentowej, Overpass Mono dla etykiet, numerów i podpisów technicznych, logo bez zmian.'),
card('3','Za dużo ciężkich hero','','kontakt, blog, promocje, outlet i dostawa mają ten sam duży ciemny blok. Większość tych stron powinna mieć jasne, krótkie intro.'),
card('4','Za dużo ikon','','ikony częściej dekorują niż pomagają. Do usunięcia: statystyki, paski korzyści, część elementów stopki i dodatkowe ikonki pomocnicze.'),
card('5','Za dużo narracji cenowej','','„najniższe ceny”, outlet, promocje, rabaty i „wysyłka jutro” dominują. Kolejność komunikacji: autentyczność → materiał → realizacje → wiedza → próbka → zakup.'),
card('6','Mocna baza już istnieje','','prawdziwe realizacje, realne zdjęcia produktu, montaż, próbki, kalkulator, opinie, informacje techniczne i kontakt z konkretnymi ludźmi. Problemem jest hierarchia i system wizualny, nie zawartość.')]
inner=lab('F · Strona internetowa · wnioski')+h1('Wnioski po całej stronie.',32)+para('Po przeanalizowaniu wszystkich zrzutów obraz jest spójny: zawartość jest często wartościowa, ale rozjeżdża się system wizualny i hierarchia komunikatów.',8)
inner+=f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px 28px;margin-top:20px">{"".join(cards)}</div>'
open(P+'str-234.dc.html','w').write(page(234,wrap(inner,1.1)))
pairs=[('Mniej grafiki interfejsu.','Więcej materiału.'),('Mniej ikon.','Więcej fotografii.'),('Mniej kolorów.','Więcej hierarchii.'),('Mniej „okazji”.','Więcej dowodów.')]
pl=''.join(f'<div style="border-top:1px solid {H};padding:16px 0;display:flex;gap:18px;align-items:baseline"><span style="font-size:20px;font-weight:300;letter-spacing:-.025em;color:#767676;width:250px;flex:none">{a}</span><span style="font-size:20px;font-weight:500;letter-spacing:-.025em;color:#111">{b}</span></div>' for a,b in pairs)
inner=lab('F · Strona internetowa · zasada redesignu')+h1('Docelowa zasada dla WWW.',32)
inner+=f'<div style="background:#000;color:#fff;padding:22px 24px;margin-top:20px"><div style="{M};color:{T}">Zasada</div><div style="font-size:24px;font-weight:300;letter-spacing:-.03em;line-height:1.2;margin-top:8px">Mniej grafiki interfejsu. Więcej materiału.</div></div>'
inner+=f'<div style="margin-top:22px;border-bottom:1px solid {H}">{pl}</div>'
inner+=f'<div style="margin-top:26px">{sub("Kolejność komunikacji",T)}'+steps([('01','Autentyczność'),('02','Materiał'),('03','Realizacje'),('04','Wiedza'),('05','Próbka'),('06','Zakup')],0)+'</div>'
inner+=box('Kierunek','połączyć obecną stronę z Brand Bookiem bez budowania wszystkiego od nowa: najmocniejsze elementy to realizacje, zdjęcia produktu, montaż, próbki, kalkulator, opinie i informacje techniczne.',24)
open(P+'str-235.dc.html','w').write(page(235,wrap(inner,1.15)))
print('ok')
