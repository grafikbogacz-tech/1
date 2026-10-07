import sys,json,os,subprocess,re;sys.path.insert(0,'build')
from ig import *
exec(open('build/adspages.py').read().split('# 178')[0].split("L='C · Google Ads'")[1])
def vs(bad,good,lb='Zamiast',lg='Lepiej',mt=12):
    return f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:{mt}px"><div style="border-left:3px solid {T};padding:2px 0 2px 12px"><div style="{M};color:{T}">{lb}</div><div style="font-size:13px;line-height:1.45;color:#333;margin-top:4px">{bad}</div></div><div style="border-left:3px solid {G};padding:2px 0 2px 12px"><div style="{M};color:{G}">{lg}</div><div style="font-size:13px;line-height:1.45;color:#111;margin-top:4px">{good}</div></div></div>'
def why(t,lb='Dlaczego?',mt=14):return box(lb,t,mt)
def rows(items,mt=12,nm=True):
    o=''
    for i,(a,b) in enumerate(items,1):
        o+=f'<div style="display:grid;grid-template-columns:{"34px " if nm else ""}170px 1fr;gap:10px;border-bottom:1px solid {H};padding:7px 0;align-items:start">'+(f'<span style="{M};color:{T};padding-top:2px">{i:02d}</span>' if nm else '')+f'<div style="font-size:13.5px;font-weight:500;color:#111">{a}</div><div style="font-size:12.5px;line-height:1.4;color:#333">{b}</div></div>'
    return f'<div style="margin-top:{mt}px;border-top:2px solid {T}">{o}</div>'
def src(code,t):return f'<div style="display:flex;gap:10px;align-items:baseline;margin-top:8px"><span style="{M};border:1px solid {G};color:{G};padding:2px 7px;flex:none">{code}</span><span style="font-size:12.5px;line-height:1.4;color:#333">{t}</span></div>'
def qt(t,mt=10):return f'<div style="border-left:3px solid {T};padding:4px 0 4px 14px;margin-top:{mt}px;font-size:16px;font-weight:300;letter-spacing:-.02em;line-height:1.3;color:#111">{t}</div>'
PG={}
def pg(n):
    def d(f):PG[n]=f;return f
    return d
S='Przykład źródłowy'
@pg('143')
def _():
    p=lab('52 · Zasada nadrzędna')+h1('Nie deklarujemy wartości. Pokazujemy jej źródło.',30)
    p+=para('Wartość Ceglanego Renesansu wynika z realnych cech materiału: wieku cegły, pochodzenia, śladów użytkowania, selekcji, procesu obróbki i efektu końcowego. Marka nie musi „upiększać” produktu reklamowym językiem — ma pomóc zobaczyć i zrozumieć, skąd bierze się jego charakter.',10)
    p+=f'<div style="margin-top:16px">{sub("Schemat komunikacji",T)}'+steps([('01','Fakt'),('02','Proces'),('03','Materiał'),('04','Efekt')],0)+'</div>'
    p+=vs('„Luksusowe płytki dla wymagających”.','„Tworzymy płytki z autentycznej, ponad 100-letniej cegły rozbiórkowej. Każda partia zachowuje własny kolor, strukturę i ślady historii.”',mt=18)
    p+=why('Deklaracje typu „luksusowy”, „wyjątkowy”, „najlepszy” łatwo skopiować. Fakty o materiale, procesie i doświadczeniu producenta są znacznie trudniejsze do podrobienia i budują wiarygodność bez nadmiernego marketingowego tonu.',mt=18)
    p+=para('To nie oznacza komunikacji chłodnej. Marka może być ciepła, obrazowa i emocjonalna, ale emocja ma wynikać z historii materiału i efektu jego ponownego wykorzystania, a nie z reklamowych ozdobników.',16)
    p+=libref('FB-10')
    return p
@pg('144')
def _():
    p=lab('53 · Autentyczność i premium')+h1('Wartość odczuwalna, nie deklarowana.',30)
    p+=para('Marka nie buduje całej tożsamości wokół słowa „premium”. Premium ma wynikać z produktu i standardu obsługi: autentycznego materiału, selekcji, kontroli procesu, doradztwa, próbek, zdjęć realnej partii i przewidywalności decyzji zakupowej.',10)
    p+=why('W komunikacji marki pojawiały się jednocześnie dwa sprzeczne sygnały: „luksusowy produkt” i bardzo agresywne komunikaty cenowe. To tworzy napięcie między marką wartościową a marką kupowaną ze względu na rabat.',mt=14)
    cs=[('Ceglany Renesans','szeroka oferta producenta'),('Outlet','partie ekonomiczne i komunikacja okazji'),('Premium','selekcjonowane partie oraz rozszerzony standard obsługi')]
    p+=f'<div style="margin-top:18px">{sub("Rekomendowana architektura",T)}<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">'+''.join(f'<div style="border-top:2px solid {T};padding-top:8px"><div style="font-size:15px;font-weight:500;color:#111">{a}</div><div style="font-size:12.5px;line-height:1.4;color:#333;margin-top:4px">{b}</div></div>' for a,b in cs)+'</div></div>'
    p+=f'<div style="margin-top:18px">{sub("Premium może być rozwijane jako",T)}'+rows([('Premium Selection','selekcja partii i większa przewidywalność efektu'),('Premium Concept','dodatkowe wsparcie w wyborze, próbka, dobór fugi i konsultacja'),('Premium Complete','pełniejsze prowadzenie klienta, kalkulacja, wsparcie wykonawcy i opieka po zakupie')],0)+'</div>'
    p+=box('Zasada','Nie mówimy klientowi, że produkt „jest premium”. Pokazujemy, co konkretnie otrzymuje i dlaczego ogranicza to ryzyko jego decyzji.',18)
    return p
@pg('145')
def _():
    p=lab('54 · Cena i promocje')+h1('Najpierw wartość, potem warunki zakupu.',30)
    p+=para('Cena i promocje mogą być obecne w komunikacji. Nie powinny jednak być pierwszą informacją, na podstawie której odbiorca rozumie markę.',10)
    p+=why('Jeśli najgłośniejszy komunikat brzmi „najniższe ceny w Polsce”, klient dostaje sygnał, że podstawowym kryterium porównania jest cena. Marka ma mocniejsze argumenty: autentyczne pochodzenie cegły, własny proces, selekcję, możliwość zamówienia próbki i szerokie zastosowanie produktu.',mt=14)
    p+=vs('„Najniższe ceny w Polsce.”<br>„Najlepsze okazje.”','„Kupujesz bezpośrednio od producenta.”<br>„Wybrane płytki teraz w niższych cenach.”<br>„Wybrane produkty w niższych cenach.”',lg='Preferujemy',mt=18)
    p+=why('Promocja pozostaje czytelna, ale nie przejmuje roli głównej obietnicy marki. Najpierw pokazujemy wartość, później warunki zakupu.','Dlaczego ta zmiana?',18)
    p+=f'<div style="margin-top:18px">{sub(S,T,2)}'+src('FB-02','post łączący realizację z mocnym komunikatem cenowym. W materiałach sprzedażowych najpierw eksponujemy wartość i cechy produktu, dopiero później cenę i dostępność.')+src('FB-18','promocja warunkowa powiązana z zakupem kompletu chemii montażowej. Warunek podajemy jednoznacznie i nie pozwalamy, aby cena zdominowała wartość produktu.')+'</div>'
    return p
@pg('146')
def _():
    p=lab('55 · Producent i proces')+h1('Jeden z najważniejszych dowodów marki.',30)
    p+=para('Komunikat „prosto od producenta” warto zachować, ale nie sprowadzać go wyłącznie do niskiej ceny. Jego największą siłą jest kontrola nad procesem.',10)
    p+=f'<div style="margin-top:14px">{sub("Rekomendowany kierunek",T,0)}'+qt('„Prosto od producenta. Od selekcji starej cegły po przygotowanie gotowej płytki — znamy i kontrolujemy cały proces.”',0)+'</div>'
    p+=f'<div style="margin-top:18px">{sub("Proces jako widoczny element komunikacji",T,0)}'+rows([('Odzyskujemy','cegła pochodzi z rozbiórek starych budynków'),('Selekcjonujemy','nie każda cegła nadaje się do ponownego wykorzystania'),('Tniemy','historyczny materiał przygotowujemy do współczesnego zastosowania'),('Zachowujemy charakter','nie usuwamy wszystkiego, co świadczy o historii materiału'),('Pokazujemy efekt','każda partia ma własny kolor, strukturę i charakter')],6)+'</div>'
    p+=why('Proces buduje wiarygodność, tłumaczy różnice między produktem autentycznym a imitacją i tworzy naturalny materiał dla strony, social mediów oraz wideo.',mt=18)
    p+=f'<div style="margin-top:16px">{sub(S,T,2)}'+src('FB-03','publikacja zewnętrzna o ponad 100-letniej cegle i nadawaniu jej drugiego życia. Dobry dowód wiarygodności i materiał wspierający komunikację procesu i autentyczności.')+'</div>'
    return p
@pg('147')
def _():
    p=lab('56 · Homepage')+h1('Najpierw zrozumienie wartości, potem sprzedaż.',30)
    p+=para('Obecna strona zbyt szybko przechodzi do sprzedaży i promocji, zanim użytkownik zrozumie, dlaczego produkt jest inny. Nowa hierarchia odwraca tę kolejność.',10)
    p+=vs('„Odkryj piękno starej cegły.” Komunikat poprawny, ale generyczny — mógłby należeć do wielu marek z tej kategorii.','„Ponad 100 lat historii w każdej płytce.”<br>„Prawdziwa stara cegła. Nie jej imitacja.”<br>spokojniej: „Autentyczna cegła rozbiórkowa przygotowana do współczesnych wnętrz.”',lb='Hero — obecnie',lg='Hero — kierunek',mt=14)
    p+=why('Pierwszy ekran ma w kilka sekund odpowiedzieć: „dlaczego właśnie ten produkt jest inny?”. Najmocniejszym wyróżnikiem nie jest ogólne „piękno”, ale autentyczność materiału.',mt=14)
    L=['Hero — czym naprawdę jest produkt','Produkty / zastosowania','Dlaczego prawdziwa stara cegła','Proces: od odzyskanej cegły do płytki','Realizacje','Jak dobrać odpowiednią cegłę','Próbki','Opinie klientów','Aktualna oferta / promocje','Wiedza / poradniki','FAQ']
    p+=f'<div style="margin-top:18px">{sub("Rekomendowana kolejność homepage",T)}<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 24px">'+''.join(f'<div style="display:flex;gap:10px;border-top:1px solid {H};padding:6px 0;font-size:13px;color:#111"><span style="{M};color:{T};flex:none">{i:02d}</span>{x}</div>' for i,x in enumerate(L,1))+'</div></div>'
    p+=box('Zasada','Najpierw budujemy zrozumienie wartości. Następnie ułatwiamy zakup.',14)
    return p
@pg('148')
def _():
    p=lab('57 · Kategorie i karty produktów')+h1('Pomagamy w decyzji, nie tylko opisujemy.',30)
    p+=para('Kategorie nie powstają według jednego szablonu SEO. Każda ma własną rolę w procesie wyboru i wyjaśnia, dla kogo oraz do jakiego zastosowania jest przeznaczona. Karta produktu to miejsce blisko decyzji — potrzebuje mniej reklamy, a więcej odpowiedzi.',10)
    p+=f'<div style="margin-top:12px">{sub("Wzorcowa konstrukcja karty produktu",T,0)}'+rows([('Nazwa','konkretna, bez reklamowego dopisku'),('Jednozdaniowe wyróżnienie','co realnie odróżnia tę partię lub produkt'),('Zdjęcia','detal, większa powierzchnia, realizacja'),('Cena i zakup','jasno, bez dominowania nad opisem wartości'),('Próbka','wyraźnie dostępna przed decyzją'),('Charakter materiału','kolor, struktura, naturalne różnice, ślady historii'),('Zastosowanie','gdzie produkt sprawdzi się najlepiej'),('Dane techniczne','opisane po ludzku'),('Montaż','konkretne wymagania i ograniczenia'),('Fuga, impregnacja','produkty uzupełniające'),('Realizacje','z tym produktem'),('Pytania','dotyczące produktu')],6)+'</div>'
    p+=why('Klient kupuje materiał odzyskany. Musi rozumieć, że nie zachowuje się on wizualnie jak seryjnie produkowana płytka ceramiczna. Dobra karta zmniejsza niepewność i pozwala podjąć świadomą decyzję.',mt=14)
    p+=f'<div style="margin-top:12px">{sub(S,T,2)}'+src('FB-06','realizacja produktu Rustykalne Loft na elewacji i ogrodzeniu; warto dopowiedzieć, jaka cecha produktu uzasadnia zastosowanie zewnętrzne.')+src('FB-14','zestawienie cegły z innymi materiałami: nie wyliczamy, tylko wyjaśniamy, jaką rolę cegła pełni w kompozycji i dlaczego połączenie działa.')+'</div>'
    return p
@pg('149')
def _():
    p=lab('58 · Próbka, parametry i montaż')+h1('Wiedza zamiast uspokajania.',30)
    p+=para('Próbka nie jest dodatkiem technicznym. Przy materiale o naturalnych różnicach może być jednym z najważniejszych elementów procesu sprzedaży.',10)
    p+=qt('„Zobacz materiał przed podjęciem decyzji.”',10)
    p+=para('Parametry techniczne opisujemy prostym językiem i zawsze tłumaczymy ich znaczenie dla użytkownika. Nie ograniczamy się do tabeli danych, jeśli klient może nie wiedzieć, co wartość oznacza w praktyce.',12)
    p+=vs('„To nic trudnego.”','„Samodzielny montaż jest możliwy, pod warunkiem odpowiedniego przygotowania podłoża i zastosowania właściwych materiałów.”',mt=14)
    p+=why('Marka ekspercka nie minimalizuje problemu. Sprawia, że proces staje się zrozumiały.',mt=12)
    p+=f'<div style="margin-top:16px">{sub("Cross-selling wynika z procesu",T)}'+steps([('01','Produkt'),('02','Instrukcja'),('03','Materiał montażowy'),('04','Fuga'),('05','Impregnacja')],0)+para('Produkty uzupełniające są rekomendacją funkcjonalną, a nie przypadkowym dodatkiem sprzedażowym.',8)+'</div>'
    p+=f'<div style="margin-top:12px">{sub(S,T,2)}'+src('FB-17','produkty uzupełniające jako element kolejnych etapów montażu; komunikację porządkujemy według procesu, nie jako listę asortymentu.')+src('FB-18','rola impregnacji; korzyści opisujemy konkretnie i wyłącznie w zakresie, który potwierdza dokumentacja produktu lub zalecenia producenta.')+'</div>'
    return p
@pg('150')
def _():
    p=lab('59 · Realizacje i opinie (1/2)')+h1('Dowód zamiast deklaracji.',30)
    p+=para('Realizacje to jeden z najbardziej niewykorzystanych aktywów marki. Pokazują nie tylko „ładny efekt”, ale relację między materiałem, przestrzenią i decyzją projektową.',10)
    p+=f'<div style="margin-top:14px">{sub("Przy realizacji podajemy",T)}'+li(['zastosowany produkt lub partię','rodzaj przestrzeni','zastosowanie: ściana, podłoga, elewacja, kominek','charakterystyczną cechę materiału','jeśli to możliwe: krótkie wyjaśnienie, dlaczego wybrano właśnie tę cegłę'],'+',G)+'</div>'
    p+=f'<div style="margin-top:14px">{sub("Jedna realizacja pracuje w wielu kanałach",T)}{chips(["WWW","karta produktu","social media","Google","Pinterest","wideo","poradnik","newsletter"],G)}</div>'
    p+=card('01','Standard social media',para('Jeśli dane są dostępne, publikacja wskazuje minimum: jaki produkt zastosowano, gdzie został użyty i jaka cecha materiału odpowiada za efekt. Nie poprzestajemy na „ściana z charakterem” — pokazujemy, skąd ten charakter wynika.',8)+libref('FB-02 · FB-04 · FB-05 · FB-06'),10)
    p+=card('02','Autor i źródło',para('Jeśli materiał pochodzi od fotografa, projektanta, wykonawcy lub klienta, oznaczamy autora zgodnie z ustaleniami i wykorzystujemy go dalej tylko w uzgodnionym zakresie.',8)+libref('FB-05'),10)
    return p
@pg('151')
def _():
    p=lab('59 · Realizacje i opinie (2/2)')+h1('Opinie, przed i po, czas, społeczność.',30)
    def rule(n,t,body,code):return f'<div style="border-top:1px solid {H};padding:10px 0 12px;display:grid;grid-template-columns:34px 1fr auto;gap:12px;align-items:start"><span style="{M};color:{T};padding-top:3px">{n}</span><div><div style="font-size:15px;font-weight:500;color:#111;letter-spacing:-.01em">{t}</div><div style="font-size:12.5px;line-height:1.45;color:#333;margin-top:4px">{body}</div></div><span style="{M};border:1px solid {G};color:{G};padding:2px 7px">{code}</span></div>'
    p+=para('Opinie klientów pozostawiamy naturalne. Nie przerabiamy ich na język Brand Booka — ich wartość wynika z tego, że brzmią inaczej niż komunikacja marki.',8)
    p+=f'<div style="margin-top:12px">'+rule('01','Publikacje klientów (UGC)','Osobna kategoria dowodu społecznego. Archiwizujemy, oznaczamy źródło i po uzgodnieniu praw wykorzystujemy w innych kanałach jako dowód realnego zastosowania. Nie przerabiamy na język reklamowy.','FB-07')+rule('02','Przed i po','Odbiorca widzi zmianę sam. Opis dopowiada, jaki produkt zastosowano, gdzie i jaka cecha materiału odpowiada za rezultat. Unikamy „ogromna różnica”, gdy można wskazać konkretną zmianę.','FB-08')+rule('03','Realizacje po latach','Pokazują materiał po czasie. Podajemy rok, produkt i warunki zastosowania. Nie używamy samego „wygląda świetnie po latach” — pokazujemy, co można zweryfikować na zdjęciach.','FB-09')+rule('04','Zewnętrzne grupy tematyczne','Nie publikujemy tak jak na profilu marki. Zaczynamy od wartości dla społeczności: inspiracji, rozwiązania, wskazówki. Dopiero później produkt i marka. CTA lekkie, zgodne z kontekstem grupy.','FB-11')+rule('05','Zbiorcze galerie','Jedno kryterium wyboru, które pomaga porównać zastosowania. Budujemy serię wokół pytania, pomieszczenia, stylu lub efektu — nie przypadkowy zestaw zdjęć.','FB-16')+'</div>'
    return p
@pg('152')
def _():
    p=lab('60 · Wideo')+h1('Obraz pokazuje, marka wyjaśnia.',30)
    p+=para('Wideo jest szczególnie wartościowe, bo produkt ma cechy trudne do przekazania tekstem: strukturę, różnice między partiami, selekcję, cięcie, pozostałości zaprawy, skalę realizacji i pracę ze światłem.',10)
    p+=box('Najważniejsza zasada','Nie tworzymy reklamy, a potem szukamy obrazów, które ją zilustrują. Zaczynamy od tego, co marka naprawdę może pokazać, i dopiero potem budujemy narrację. Kamera pokazuje fakt, detal, czynność lub efekt; narracja pomaga zrozumieć to, co widać.',12)
    p+=f'<div style="margin-top:14px">{sub("Podstawowe formaty",T)}'+rows([('Proces','od starej cegły do gotowej płytki'),('Wiedza o materiale','dlaczego cegły różnią się kolorem i strukturą'),('Produkt','konkretna partia, detal, zastosowanie, cechy'),('Realizacja','materiał w prawdziwej przestrzeni'),('Poradnik','wybór, montaż, fuga, impregnacja, pielęgnacja'),('Pytania klientów','odpowiedzi na realne wątpliwości')],0,False)+'</div>'
    p+=f'<div style="margin-top:14px">{sub("Przykładowa seria",T)}'+steps([('F1','Skąd pochodzi cegła?'),('F2','Dlaczego nie każda zostaje płytką?'),('F3','Jak powstaje płytka?'),('F4','Dlaczego zostawiamy ślady zaprawy?'),('F5','Od rozbiórki do wnętrza')],0)+'</div>'
    p+=f'<div style="margin-top:14px">{sub("Jeden temat — kilka formatów",T)}'+rows([('YouTube','pełne wyjaśnienie procesu'),('Short / Reels','30–45 sekund z najważniejszą odpowiedzią'),('Facebook / Instagram','fragment i krótki opis'),('Karta produktu','krótkie wideo o naturalnych cechach materiału'),('FAQ / poradnik','tekstowe rozwinięcie tego samego pytania')],0,False)+'</div>'
    p+=para('Narrator brzmi jak osoba, która zna materiał i spokojnie go tłumaczy, nie jak lektor reklamy. Bez superlatyw i bez zmiany charakteru marki tylko dlatego, że komunikacja trafia do social video.',12)+libref('FB-04')
    return p
@pg('153')
def _():
    p=lab('61 · System treści')+h1('Pytania klientów jako źródło tematów.',30)
    p+=para('FAQ to nie doczepiona lista na końcu strony, ale zapis realnych wątpliwości klientów i część ścieżki zakupowej. Pytań nie wymyślamy — zbieramy je z maili, telefonu, Facebooka, komentarzy, sklepu i obsługi klienta.',10)
    p+=f'<div style="margin-top:12px">{sub("Etapy decyzji",T)}'+steps([('01','Przed wyborem produktu'),('02','Przed zakupem'),('03','W trakcie montażu'),('04','Po montażu')],0)+'</div>'
    p+=f'<div style="margin-top:14px">{sub("Jedna odpowiedź pracuje jako",T)}{chips(["krótka odpowiedź w FAQ","rozwinięcie w poradniku","post w social media","krótki film","fragment filmu na YouTube","dopisek do karty produktu","temat newslettera"],G)}</div>'
    p+=para('Taki system ogranicza produkowanie treści „dla samej publikacji”: jeden dobrze opracowany temat pracuje wiele miesięcy w różnych kanałach.',8)
    p+=para('<b>Ludzie marki i kulisy</b> to stały filar treści, ale z kontekstem: kto pojawia się w materiale, dlaczego, co się wydarzyło i co ten moment mówi o marce. Nie zastępujemy historii samą obecnością osób na zdjęciu. Zob. FB-15.',10)
    chk=['Czy komunikat opiera się na fakcie, który marka może udowodnić?','Czy pokazujemy źródło wartości zamiast tylko ją deklarować?','Czy język jest spokojny, konkretny i zrozumiały?','Czy cena nie przykrywa wartości produktu?','Czy nie używamy superlatyw bez dowodu?','Czy materiał pomaga klientowi podjąć decyzję?','Czy obraz może coś pokazać lepiej niż tekst? Jeśli tak — pokazujemy zamiast opisywać.']
    cl=''.join(f'<div style="display:flex;gap:12px;align-items:center;border-bottom:1px solid {H};padding:5px 0;font-size:12.5px;color:#111"><span style="width:13px;height:13px;border:1.5px solid {G};flex:none"></span>{c}</div>' for c in chk)
    p+=f'<div style="margin-top:12px">{sub("Kontrola przed publikacją",T,2)}{cl}</div>'
    return p
if __name__=='__main__':
    only=sys.argv[1:] or sorted(PG)
    Z=json.load(open('build/viz.json')) if os.path.exists('build/viz.json') else {}
    def bottom(n):
        o=subprocess.run(['node','pag/fitabs.js','all/project',f'str-{n}.dc.html'],capture_output=True,text=True).stdout
        m=re.search(r'bottom: (\d+)',o);return int(m.group(1)) if m else 9999
    for n in only:
        p=PG[n]();z=1.0;write('str-'+n,p,0,z);b=bottom(n)
        z=max(1.0,min(1.45,round(0.985*920/max(b-100,1),2)))
        while True:
            write('str-'+n,p,0,z);b=bottom(n)
            if b<=1022 or z<=1.0:break
            z=round(z-0.02,2)
        Z[n]=z;print(n,z,b)
    json.dump(Z,open('build/viz.json','w'))
