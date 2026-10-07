import re,sys
sys.path.insert(0,'build')
from iglib import M,lb,tx,badge,foot
P='all/project/project/'
BL={1:('838e1fcb61e0fa01f26c0cbf396c23a6',2000,777),2:('5deccb532478102acc649c6019d18143',1249,552),3:('719ac727fe74e61ab4458a9d92e86a0b',1225,959),4:('a65bfb4e08c9b3a9cc1411e1ddc9bc2d',901,250),11:('41eb3968fcbc3577e473821998d8e7dc',1133,702)}
E=[
(1,'Strona główna: hero','Dobry',65,'strona główna sklepu',
 'główny header, menu, wyszukiwarka, hero z realizacją, hasło „Odkryj piękno starej cegły”, opis producenta i dwa przyciski.',
 'bardzo dobre zdjęcie realizacji, cegła jest głównym bohaterem; zdanie o „oryginalnej, ponad 100-letniej cegle” dobrze komunikuje przewagę marki; od razu widać, że to sklep i producent.',
 'hero jest bardziej estetyczne niż sprzedażowo-strategiczne; hasło „Odkryj piękno starej cegły” jest ogólne i pasowałoby do wielu marek; przyciski „PŁYTKI CEGLANE” i „STARA CEGŁA” nie tłumaczą różnicy między ścieżkami; czerwony pasek promocyjny zmienia odbiór marki w stronę dyskontu.',
 '„Płytki z autentycznej, ponad 100-letniej cegły”, a niżej krótszy kontekst emocjonalny. Przyciski decyzyjne: „Zobacz płytki” / „Zamów próbkę”.',
 'mocniej oprzeć hero na przewadze materiału, przyciski uczynić decyzyjnymi.',
 'Pierwsza sekcja ma komunikować materiał i jego autentyczność przed promocją i ceną.'),
(2,'Sekcja „Najniższe ceny w Polsce”','Do poprawy',40,'sekcja promocyjna strony głównej',
 'trzy produkty promocyjne z cenami, przekreślonymi cenami i komunikatem „przy zakupie chemii”.',
 'oferta jest konkretna, użytkownik szybko widzi cenę i produkt; zdjęcia realizacji pomagają zrozumieć zastosowanie.',
 'nagłówek „Najniższe ceny w Polsce” ustawia markę jako konkurującą ceną, nie autentycznością materiału, co jest sprzeczne z kierunkiem Brand Booka (premium przez materiał, historię i jakość); na kartach nakłada się wiele warstw cenowych: cena aktualna, stara cena, żółty pasek i data promocji.',
 'nagłówek „Aktualne zestawy promocyjne” albo „Płytki + chemia w zestawie”. Sama promocja może zostać.',
 'zmienić nagłówek, ograniczyć liczbę warstw cenowych na kartach.',
 'Cena może wspierać decyzję, ale nie może definiować marki.'),
(3,'Karta produktu: górna część','Dobry',70,'karta produktu',
 'galeria, cena, wariant promocji, ilość m², przycisk zakupu, dostawa, opis, parametry i warianty serii.',
 'bardzo dobra ilość informacji zakupowej, parametry są czytelne; zdanie „Płytki cięte ze starej, oryginalnej, ponad 100-letniej cegły.” to język marki oparty na fakcie.',
 'nazwa „Płytki RETRO (przy zakupie chemii)” jest bardziej nazwą warunku cenowego niż produktu; przycisk „DODAJ DO KOSZYKA Z CHEMIĄ” jest bardzo transakcyjny; brakuje krótkiego bloku „Dlaczego ten produkt jest inny?”.',
 'nazwa: „Płytki RETRO”; pod nią: „Cena promocyjna przy zakupie zestawu chemii.” Osobno: nazwa produktu, wariant zakupu, korzyść promocji.',
 'rozdzielić nazwę produktu, wariant zakupu i korzyść promocji; dodać blok „Dlaczego ten produkt jest inny?”.',
 'Nazwa produktu pozostaje stabilna; promocja jest informacją dodatkową.'),
(4,'Kalkulator chemii','Dobry',75,'blok narzędziowy na stronie',
 'ciemny blok „Oblicz potrzebną chemię” z przyciskiem.',
 'bardzo dobre narzędzie redukujące niepewność klienta; wspiera decyzję i pokazuje kompetencję producenta.',
 'tekst „Nie wiesz ile potrzebujesz chemii? Nasz kalkulator Ci w tym pomoże.” można skrócić.',
 '„Oblicz potrzebną ilość chemii. Podaj powierzchnię, a kalkulator dobierze potrzebne ilości.” To lepsze niż narracja problemowa.',
 'skrócić tekst i opisać działanie narzędzia.',
 'Narzędzia i kalkulatory są częścią doświadczenia eksperckiego marki.'),
(5,'Pasek korzyści','Do poprawy',50,'pasek korzyści',
 'etykiety: OPAKOWANIE, UBEZPIECZENIE, BEZPIECZNY DOWÓZ, ARANŻACJA, DOSTAWA.',
 'próbuje uspokoić klienta przed zakupem.',
 'część etykiet jest ogólna: nie wiadomo, co oznacza „ARANŻACJA”, czym „bezpieczny dowóz” różni się od „dostawy” i jaka korzyść kryje się pod „opakowaniem”; ikony są niespójne stylistycznie.',
 'zamiast samych rzeczowników: „Bezpieczne pakowanie”, „Ubezpieczona przesyłka”, „Dostawa paletowa”, „Pomoc w doborze”, „Odbiór osobisty”.',
 'zamienić rzeczowniki na konkretne korzyści i ujednolicić ikony.',
 'Benefit musi mówić, co klient realnie otrzymuje.'),
(6,'Produkty powiązane','Dobry',65,'sekcja produktów powiązanych',
 'produkty uzupełniające i podobne.',
 'bardzo dobry element cross-sellu; chemia obok płytek ma sens zakupowy.',
 'w jednej sekcji mieszają się inne modele płytek, impregnat i produkty z innym warunkiem cenowym; sekcja jest bardziej „sklepowa” niż doradcza.',
 'rozdzielić sekcje: „Do montażu tego produktu potrzebujesz” oraz „Podobne płytki”.',
 'rozdzielić sekcje, żeby zwiększyć czytelność i kompetencyjny charakter.',
 'Produkty powiązane porządkujemy według roli: do montażu, podobne, uzupełniające.'),
(7,'Realizacje klientów','Super',85,'sekcja realizacji',
 'trzy realizacje płytek RETRO.',
 'jedna z najmocniejszych sekcji strony: produkt w różnych zastosowaniach i dowód społeczny.',
 'podpisy są ogólne („elewacja zewnętrzna”, „aranżacja zewnętrzna”).',
 'do każdej realizacji dodać, jeśli dane są dostępne: model, zastosowanie, typ fugi, lokalizację lub typ obiektu i krótki kontekst.',
 'uzupełnić podpisy o model, zastosowanie i fugę.',
 'Realizacja to dowód, nie tylko galeria.'),
(8,'Blok producenta / zaufanie','Do poprawy',50,'sekcja formalna',
 'logo, dane producenta i dwa znaki jakości.',
 'zwiększa wiarygodność i pokazuje, że za marką stoi realny producent.',
 'blok wygląda jak osobna grafika z innej epoki i nie pasuje do reszty strony; logo jest czarne, a główny branding używa wersji pomarańczowej; znaki jakości wyglądają jak elementy z innego systemu.',
 'przebudować jako zwykłą sekcję HTML: producent CEGMAR Marek Pochcioł, dane, a osobno wiarygodne oznaczenia lub certyfikaty, jeśli są aktualne i udokumentowane.',
 'zbudować blok jako sekcję w systemie marki, z logo w wersji pomarańczowej.',
 'Dane formalne nie powinny wyglądać jak obca grafika wklejona do strony.'),
(9,'Opinie klientów','Dobry',65,'sekcja opinii Google',
 'opinie z Google.',
 'bardzo mocny dowód społeczny; opinie są konkretne i dotyczą produktu oraz obsługi.',
 'widoczne są błędy kodowania znaków i emoji jako „????”, co obniża jakość i zaufanie; opinie są bardzo długie, więc sekcja jest ciężka wizualnie.',
 'naprawić kodowanie, skrócić widoczny fragment i dodać „Czytaj pełną opinię w Google”.',
 'priorytet wysoki: naprawić kodowanie znaków i skrócić opinie.',
 'Social proof musi wyglądać równie wiarygodnie jak jego źródło.'),
(10,'Stopka','Do poprawy',55,'stopka strony',
 'dane CEGMAR, NIP, REGON, rachunek bankowy, oferta, linki sklepu i social media.',
 'dużo ważnych informacji formalnych, dane firmy są dostępne, jest polityka prywatności i regulamin.',
 'stopka jest bardzo techniczna i prawie traci markę Ceglany Renesans; hierarchia informacji jest płaska; numer konta bankowego nie musi być jednym z najważniejszych elementów wizualnych.',
 'zbudować stopkę w czterech kolumnach: Marka / Produkty / Pomoc / Formalne.',
 'uporządkować stopkę w cztery kolumny.',
 'Stopka ma zamknąć doświadczenie marki, a nie być tylko magazynem linków.'),
(11,'Formularz kontaktowy','Dobry',65,'formularz kontaktowy',
 'formularz na ciemnobrązowym tle.',
 'prosty formularz z małą liczbą pól i dobrym kontrastem.',
 'brak nagłówka wyjaśniającego, po co klient ma pisać; przycisk „WYŚLIJ” jest neutralny i nie wspiera intencji; zgoda jest opisana ciężkim, technicznym językiem, a jej treść warto sprawdzić z osobą odpowiedzialną za kwestie prawne.',
 'nagłówek: „Masz pytanie o produkt lub realizację?” Treść: „Napisz — pomożemy dobrać płytkę, ilość i rozwiązanie do Twojego projektu.” Przycisk: „Wyślij wiadomość”.',
 'dodać nagłówek i opis, zmienić przycisk; zgodę sprawdzić prawnie.',
 'Formularz tłumaczy, po co pisać i co klient dostanie.')]
src=open(P+'p170k.dc.html').read()
head=src[:src.index('<div class="cr pg">')]
intro=('<div style="position:absolute;left:76px;top:100px;width:642px"><div style="'+M+';letter-spacing:.14em;color:#ED6842">F · Biblioteka źródeł</div><div style="font-family:\'Hanken Grotesk\',sans-serif;font-size:36px;font-weight:300;letter-spacing:-.03em;line-height:1.1;margin-top:10px">Strona internetowa — przykłady.</div><div style="font-size:13px;line-height:1.45;color:#767676;margin-top:8px">Zasady strony opisuje część IV C, strony 130–134. Tu zbieramy przykłady strony głównej, karty produktu i elementów sklepu.</div></div>')
names=[f'pw{n:02d}' for n in range(1,12)]
for i,(n,t,r,p,typ,desc,ok,bad,better,rec,rule) in enumerate(E):
    tab=205+i;code=f'WWW-{n:02d}'
    h=head.replace('<title>Strona 204</title>',f'<title>Strona {tab}</title>')
    body=f'<div class="cr pg"><div class="tab">{tab}</div><div class="rh"><span>Biblioteka przykładów / Strona internetowa</span><span>Ceglany Renesans</span></div>'
    if i==0:
        body+=intro+'<div style="position:absolute;left:76px;top:215px;width:642px;border-top:1px solid #E7DFC9"></div>';top=231;cap=250
    else:
        body+='<div style="position:absolute;left:76px;top:100px;width:642px;border-top:1px solid #E7DFC9"></div>';top=116;cap=340
    if n in BL:
        b,w0,h0=BL[n];W_=min(642,round(cap*w0/h0));H_=round(W_*h0/w0)
        body+=f'<img src="/_blob/{b}" alt="{code}" style="position:absolute;left:76px;top:{top}px;width:{W_}px;height:auto;border:1px solid #E7DFC9;display:block">'
    else:
        H_=190
        body+=f'<div style="position:absolute;left:76px;top:{top}px;width:642px;height:{H_}px;box-sizing:border-box;border:1px dashed #BDB7A0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px"><div style="{M};color:#0D4C73">Miejsce na screen</div><div style="font-size:12px;color:#767676">{code}</div></div>'
    y=top+H_+16
    head_row=f'<div style="display:flex;justify-content:space-between;align-items:center"><div style="{M};color:#ED6842">{code}</div>{badge(r,p)}</div><div style="font-size:18px;font-weight:500;letter-spacing:-.02em;line-height:1.2;margin-top:6px;color:#111">{t}</div><div style="font-size:12px;color:#767676;margin-top:4px">{typ}</div>'
    body+=f'<div class="wmid" style="position:absolute;left:76px;top:{y}px;width:642px">{head_row}{lb("Opis",mt=10)}{tx(desc)}<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px"><div>{lb("Co działa")}{tx(ok)}</div><div>{lb("Co poprawić","#ED6842")}{tx(bad)}</div></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:34px;border-top:1px solid #E7DFC9;padding-top:12px;margin-top:22px"><div>{lb("Przykład lepszej wersji",mt=0)}{tx(better)}</div><div>{lb("Rekomendacja",mt=0)}{tx(rec)}{lb("Reguła Brand Booka")}{tx(rule)}</div></div></div>'
    open(P+names[i]+'.dc.html','w').write(head+body+foot)
# p177: keep only G
s=open(P+'p177.dc.html').read()
a=s.index('<h2>F. Strona internetowa / sklep</h2>');b=s.index('<h2>G. Inne materiały marki</h2>')
s=s[:a]+s[b:]
s=s.replace('Biblioteka przykładów / Strona internetowa / Inne materiały','Biblioteka przykładów / Inne materiały')
s=re.sub(r'class="tab">\d+','class="tab">219',s,1);s=re.sub(r'<title>[^<]*</title>','<title>Strona 219</title>',s,1)
open(P+'p177.dc.html','w').write(s)
print('ok')
