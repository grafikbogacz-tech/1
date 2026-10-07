import sys;sys.path.insert(0,'build')
from ig import *
# p084 intro
fn=[('TikTok','ruch, proces, szybki hook, ręce przy pracy, krótka odpowiedź'),('Facebook','szersza narracja, kontekst, społeczność, dłuższy opis'),('Instagram','mocny obraz, jeden temat, konkretny produkt i zastosowanie, estetyczna prezentacja'),('YouTube','pogłębienie tematu, pełny poradnik, dłuższa historia')]
cm=''.join(f'<div style="border-top:{"2px solid "+T if a=="Instagram" else "1px solid "+H};padding:10px 0 4px"><div style="font-size:15px;font-weight:500;letter-spacing:-.02em;color:{T if a=="Instagram" else "#111"}">{a}</div><div style="font-size:12px;line-height:1.4;color:#555;margin-top:4px">{b}</div></div>' for a,b in fn)
p=lab('44.2 · Instagram')+h1('Estetyka + konkret + kontekst.')
p+=para('Instagram ma pokazać produkt w kontekście, uporządkować wizerunek marki i poprowadzić użytkownika od inspiracji do decyzji. Nie jest wyłącznie galerią ładnych zdjęć ani kopią TikToka.')
p+=steps([('01','Inspiracja'),('02','Dowód produktu'),('03','Edukacja')],14)
p+=f'<div style="margin-top:22px">{sub("Różnica między kanałami",T)}<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px">{cm}</div></div>'
p+=box('Główna zasada','Instagram Ceglanego Renesansu ma być estetyczną biblioteką produktu, realizacji i wiedzy. Nie tylko: „zobacz ładną cegłę”. Ale: „zobacz produkt, zrozum go i wyobraź go sobie u siebie”.',22)
p+=f'<div style="font-size:12.5px;line-height:1.45;color:#333;margin-top:12px">Zrzuty ekranu profilu i postów: część VII, sekcja E „Instagram”, strony 200–201.</div>'+libref()
write('p084',p,0)
# pillars
pil=[
('01','Realizacje','pokazywać produkt w realnych przestrzeniach.',[('Minimum informacji',['jaki produkt,','gdzie zastosowany,','co warto zauważyć,','jaki efekt daje materiał.'])],'Każda realizacja ma własny temat przewodni:',['kolor','struktura','fuga','światło','zestawienie z drewnem','strefa schodów','kominek','elewacja','łazienka','taras'],'Nie publikujemy realizacji wyłącznie jako „ładne wnętrze”.'),
('02','Reels — proces / montaż','pokazywać kompetencję przez realne działanie.',[],'Treści:',['klejenie','poziomowanie','fugowanie','impregnacja','cięcie','docinki','przygotowanie ściany','montaż na elewacji'],'Reel nie powinien być tylko „kulisy z muzyką”. Musi mieć konkretną wartość użytkową.'),
('03','Poradniki / karuzele','uczyć w 3–6 slajdach.',[],'Tematy:',['jak dobrać fugę','jak wybrać model','cegła do wnętrza vs elewacja','impregnacja','błędy montażowe','naturalne różnice materiału','jak zamawiać próbki'],'Struktura: slajd 1 — problem / pytanie, 2–4 — konkretna odpowiedź, 5 — przykład, 6 — CTA.'),
('04','Produkty / porównania','pomagać wybrać.',[],'Treści:',['RETRO','CLASSIC','RUSTYKALNE','porównania wariantów','kolor','struktura','zastosowanie'],'Standard: produkt → różnica → zastosowanie → CTA.'),
('05','Przed / po','pokazywać zmianę przestrzeni.',[],'Schemat:',['przed','proces / decyzja','produkt','efekt końcowy'],'To jeden z najlepszych formatów do zapisów i udostępnień.'),
('06','Zastosowania','odpowiadać na pytanie „dlaczego tutaj działa?” w serii „Gdzie zastosować cegłę?”.',[],'Tematy:',['przy schodach','na elewacji','przy kominku','w kuchni','w łazience','w przedpokoju','na tarasie'],'Każdy materiał powinien odpowiadać na pytanie: „dlaczego tutaj działa?”.'),
('07','Proces / autentyczność','udowadniać autentyczność materiału.',[],'Treści:',['odzysk','selekcja','cięcie','sortowanie','różnice między partiami','przygotowanie produktu'],None),
('08','Kulisy / ludzie','pokazywać kompetencję i charakter pracy.',[],'Treści:',['zakład','magazyn','zespół','przygotowanie zamówień','montaże','praca przy produkcie'],'Kulisy mają pokazywać kompetencję i charakter pracy.'),
]
def pcard(c):
    n,t,cel,mins,lt,items,rule=c
    b=row('Cel',cel)
    for l,it in mins:
        b+=f'<div style="margin-top:12px">{sub(l)}{li(it,"+",G)}</div>'
    b+=f'<div style="margin-top:12px">{sub(lt)}{chips(items)}</div>'
    if rule:b+=box('Zasada',rule,12)
    return card(n,t,b)
# p085 overview
tiles=''.join(f'<div style="border-top:1px solid {H};padding:10px 0 12px"><div style="{MF};font-weight:300;font-size:26px;letter-spacing:-.05em;color:{T};line-height:1">{c[0]}</div><div style="font-size:15px;font-weight:500;letter-spacing:-.02em;margin-top:6px;color:#111">{c[1]}</div><div style="font-size:12px;line-height:1.4;color:#555;margin-top:4px">{c[2][0].upper()+c[2][1:]}</div></div>' for c in pil)
p=lab('44.2 · Instagram · filary')+h1('Osiem filarów treści.')+para('Każda publikacja należy do jednego z ośmiu filarów. Poniżej przegląd, na kolejnych stronach karty: cel, treści, zasada.')+f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 26px;margin-top:14px">{tiles}</div>'
write('p085',p,0)
for i,n in enumerate(['p086','p087','p088','p089']):
    write(n,lab('44.2 · Instagram · filary')+'<div style="display:flex;flex-direction:column;gap:22px">'+pcard(pil[2*i])+pcard(pil[2*i+1])+'</div>',14)
# p090 feed + okładki
p=lab('44.2 · Instagram · feed i okładki')
p+=card('09','System feedu',para('Feed nie musi być „idealną szachownicą”. Ma być spójny, ale naturalny.',8)+f'<div style="margin-top:12px">{sub("Stałe formaty")}{chips(["realizacja","Reel","karuzela edukacyjna","produkt","przed / po","kulisy"])}</div>'+cols(sub('Feed rozpoznawalny przez',G)+li(['jeden system typografii,','podobny sposób kadrowania,','stałe zasady okładek,','ograniczoną paletę,','dużo realnych zdjęć produktu.'],'+',G),sub('Unikać',T)+li(['przypadkowych plansz,','różnych fontów,','zmieniającej się stylistyki przy każdym poście.'],'×',T)))
p+=card('10','System okładek Reels',row('Pytanie','okładka ma odpowiadać: „o czym jest film?”')+cols(sub('Standard')+li(['2–5 słów,','wysoki kontrast,','jeden krój pisma,','stałe miejsce tekstu.'],'+',G),sub('Nie stosować',T)+li(['przypadkowych kolorów,','pełnych zdań,','ozdobnych fontów.'],'×',T))+f'<div style="margin-top:12px">{sub("Przykłady")}{chips(["MONTAŻ NA ELEWACJI","JAK DOBRAĆ FUGĘ?","RETRO PRZY SCHODACH","PRZED I PO","JAK POWSTAJE PŁYTKA?"],G,True)}</div>'+box('Nie','„Kleimy nasze cudności ❤️”.',12))
write('p090',p,24)
# p091 reels + karuzele
p=lab('44.2 · Instagram · Reels i karuzele')
p+=card('11','Reels — struktura',steps([('0–2 s','Hook'),('Środek','Proces / odpowiedź / produkt'),('Koniec','Efekt lub jedno CTA')])+box('Przykład','hook: „Cegła nie musi być na całej elewacji.” → pokazanie fragmentu → wyjaśnienie, gdzie działa → efekt końcowy → „Zapisz jako inspirację.”',14))
p+=card('12','Karuzele — standard',steps([('Slajd 1','Mocne pytanie lub problem'),('Slajdy 2–5','Konkretna wiedza'),('Ostatni slajd','Jedno CTA')])+f'<div style="margin-top:12px">{sub("Przykłady tytułów")}{chips(["5 błędów przy fugowaniu","RETRO czy CLASSIC?","Czy trzeba impregnować starą cegłę?","Jak wybrać kolor fugi?"],G,True)}</div>')
write('p091',p,24)
# p091x1 stories highlights bio
p=lab('44.2 · Instagram · Stories, Highlights, bio')
p+=card('13','Stories — rola',cols(sub('Stories służą do')+li(['codziennego kontaktu,','kulis, pytań, ankiet,','pokazania pracy,','aktualnych realizacji,','promocji z ograniczonym czasem,','prowadzenia do linku.'],'+',G),sub('Powtarzalne formaty')+li(['„Dziś na montażu”','„Pytanie dnia”','„Który wariant?”','„Przed / po”','„Nowa realizacja”','„Próbki”','„Z zakładu”'],'→',T),10)+box('Zasada','Stories nie są śmietnikiem na wszystko, czego nie chcemy dać do feedu.',4))
p+=card('14','Highlights — docelowa struktura',f'<div style="margin-top:10px">{chips(["Produkty","Realizacje","Montaż","Próbki","Opinie","Proces","Elewacje","FAQ"],G,True)}</div>'+row('Nazwy','krótkie i czytelne.')+row('Okładki','jeden system, bez drobnego tekstu, bez przypadkowych zdjęć, zgodne z identyfikacją marki.'))
p+=card('15','Bio profilu',row('Komunikat','co sprzedajemy, czym produkt jest, co użytkownik może zrobić dalej.')+box('Kierunek','„Płytki z autentycznej starej cegły. Produkcja • montaż • realizacje. Zamów próbkę / zobacz ofertę ↓”',10)+para('Nie rozpraszamy użytkownika wieloma CTA.',8))
write('p091x1',p,20)
# p091x2 CTA caption hashtags
ct=[('Typ 1','Zapis',['„Zapisz na później.”','„Zapisz jako inspirację.”']),('Typ 2','Komentarz',['„Który wariant wybrałbyś?”','„Gdzie zastosowałbyś taką cegłę?”']),('Typ 3','Decyzja',['„Zamów próbkę.”','„Zobacz dostępne modele.”','„Sprawdź realizacje.”']),('Typ 4','Przejście dalej',['„Pełny poradnik znajdziesz na stronie.”','„Więcej realizacji w wyróżnionych relacjach.”'])]
tt=''.join(f'<div style="border-top:2px solid {T};padding-top:8px"><div style="{M};color:{T}">{a}</div><div style="font-size:15px;font-weight:500;letter-spacing:-.02em;margin-top:2px">{b}</div><div style="margin-top:6px">{li(c,"·",G,12,4)}</div></div>' for a,b,c in ct)
p=lab('44.2 · Instagram · CTA i opisy')
p+=card('16','CTA — system',f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px 22px;margin-top:12px">{tt}</div>'+box('Zasada','1 post = 1 główne CTA.',14))
p+=card('17','Caption — standard',row('Zasada','opis krótszy niż na Facebooku.')+steps([('01','Jedno mocne zdanie'),('02','1–3 konkrety'),('03','Jedno CTA')])+box('Przykład','„Stara cegła nie musi pokrywać całej elewacji. W tej realizacji pracuje tylko jako akcent przy wejściu i dobrze łączy się z jasnym tynkiem. Zapisz jako inspirację.”',12))
p+=card('18','Hashtagi',row('Zasada','nie budujemy strategii na hashtagach.')+cols(li(['kilka niszowych,','kilka tematycznych.'],'+',G),li(['przypadkowych popularnych tagów,','błędów i nadmiaru.'],'×',T),8))
write('p091x2',p,18)
# p091x3 UGC, rytm, mix, powiązania
mix=[('30','Realizacje / przed-po'),('25','Reels proces / montaż'),('15','Poradniki / karuzele'),('15','Produkt / porównania'),('10','Kulisy / ludzie'),('5','Promocje')]
bars=''.join(f'<div style="display:flex;align-items:center;gap:10px;margin-top:5px"><div style="width:150px;font-size:12px;color:#333;flex:none">{b}</div><div style="flex:1"><div style="height:12px;width:{int(a)*3.2}%;background:{T if a=="5" else G}"></div></div><div style="{MF};font-size:12px;width:34px;text-align:right;color:#111">{a}%</div></div>' for a,b in mix)
rel=[('TikTok','szybki hook / proces'),('Instagram','estetyka + wiedza + kontekst'),('Facebook','szersza narracja'),('YouTube','pogłębiony poradnik'),('WWW','produkt / realizacja / próbka'),('Google Business','aktualność / decyzja')]
rl=''.join(f'<div style="border-top:1px solid {H};padding:7px 0"><div style="{M};color:{T if a=="Instagram" else G}">{a}</div><div style="font-size:12.5px;color:#333;margin-top:2px">{b}</div></div>' for a,b in rel)
p=lab('44.2 · Instagram · rytm i mix')
p+=card('19','UGC / treści klientów',row('Zasada','materiały klientów są bardzo wartościowe.')+f'<div style="margin-top:10px">{steps([("01","Archiwizować oznaczenia"),("02","Prosić o zgodę"),("03","Repostować"),("04","Zapisywać do Highlights"),("05","Używać w realizacjach"),("06","Linkować do produktu")],0)}</div>'+para('Nie przerabiamy UGC na sztuczny język reklamowy.',8))
p+=card('20','Rytm publikacji i mix',cols(sub('Rekomendowany start')+li(['3–4 publikacje feed / Reels tygodniowo,','Stories kilka razy w tygodniu,','1 karuzela edukacyjna tygodniowo lub co 2 tygodnie,','realizacje w miarę pojawiania się materiału.'],'+',G)+para('Nie publikujemy codziennie tylko dla częstotliwości.',6),sub('Docelowy mix (orientacyjnie)')+bars+para('Promocja nie może dominować feedu.',8)))
p+=card('21','Powiązanie z innymi kanałami',f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:0 18px;margin-top:10px">{rl}</div>'+para('Ten sam temat może pojawić się w kilku kanałach, ale forma musi być dostosowana.',8))
write('p091x3',p,18)
# p091x4 measure
p=lab('44.2 · Instagram · pomiar')
p+=card('22','Co mierzymy',para('Po uzyskaniu Insightów. Nie oceniamy tylko lajków.',8)+f'<div style="margin-top:10px">{chips(["zasięg","wyświetlenia","zapisania","udostępnienia","komentarze","wejścia na profil","kliknięcia linku","obserwacje po publikacji","retencja Reels","odtworzenia do końca","odpowiedzi na Stories","kliknięcia naklejek / linków"])}</div>'+f'<div style="margin-top:12px">{sub("Najważniejsze pytania")}{li(["co jest zapisywane,","co jest udostępniane,","co prowadzi na profil,","co prowadzi do próbki / produktu."],"?",T)}</div>')
p+=card('23','Miesięczny przegląd',cols(li(['Top 5 postów według zapisów.','Top 5 Reels według retencji / zasięgu.','Top Stories według odpowiedzi / kliknięć.','Najczęstsze pytania.','Najlepszy format.'],'□',G),li(['Najsłabszy format.','Co powtórzyć.','Co usunąć z planu.','Jakie serie rozwijać.','Czy profil prowadzi do właściwego CTA.'],'□',G),10))
p+=card('24','Brakujące dane',para('Do pełnej oceny potrzebujemy Instagram Insights.',8)+cols(sub('Dane')+li(['zasięg, retencja Reels,','zapisania, udostępnienia,','profile visits, website taps,','follows from content,','wyniki Stories, demografia.'],'·',G),sub('Pozwolą ustalić',T)+li(['najlepszą częstotliwość,','godziny publikacji,','najlepsze formaty,','realny udział Instagrama w ścieżce zakupowej.'],'→',T),10))
write('p091x4',p,18)
print('ok')
