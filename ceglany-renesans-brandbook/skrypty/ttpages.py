import sys,json,subprocess,re;sys.path.insert(0,'build')
from ig import *
Z=json.load(open('build/ttz.json')) if len(sys.argv)>1 else {}
def W(n,inner,gap=16):write(n,inner,gap,Z.get(n,1))
L='44.3 · TikTok'
# p075
def stat():return f'<div style="display:flex;gap:18px;align-items:center;margin-top:14px;border-top:1px solid {H};padding-top:14px"><div style="{MF};font-weight:300;font-size:64px;letter-spacing:-.05em;color:{T};line-height:1">72%</div><div style="font-size:13px;line-height:1.45;color:#333">wszystkich wyświetleń z 20 ostatnich publikacji dały zaledwie trzy filmy. Konto publikuje bardzo regularnie, ale wynik opiera się na pojedynczych mocnych materiałach.</div></div>'
p=lab(L)+h1('Pokaż działanie, nie tylko efekt.')+para('TikTok nie jest kopią Facebooka ani galerią gotowych realizacji. Jego rola to pokazywanie tego, czego nie widać na zdjęciu.')
p+=f'<div style="margin-top:14px">{chips(["praca rąk","proces","montaż","cięcie","selekcja","różnice materiału","krótkie odpowiedzi"],G,True)}</div>'
p+=f'<div style="margin-top:26px">{sub("Obecny stan — wnioski",T)}<div style="font-size:12px;color:#767676;margin-top:-2px">Źródło: „Analiza TikTok @ceglanyrenesans”, dane publiczne z 4.10.2026.</div>{stat()}</div>'
p+=cols(sub('Najmocniejsze formaty')+li(['produkcja / proces,','krótkie poradniki montażowe,','ręce przy pracy.'],'+',G),sub('Słabsze formaty',T)+li(['samo „ładne wnętrze + muzyka”,','realizacje bez wyraźnego hooka,','ogólne hasła bez obietnicy konkretnej wiedzy.'],'×',T),22)
p+=box('Wniosek','nie zwiększamy liczby publikacji dla samej częstotliwości. Zmieniamy proporcje treści na korzyść procesu i poradników.',22)
W('p075',p,0)
# p076 mix + overview
pil=[('01','Produkcja — „od cegły do płytki”','pokazywać źródło wartości i przewagę autentycznej starej cegły.',['jak powstaje płytka','cięcie','selekcja','sortowanie','różnice między cegłami','co odrzucamy i dlaczego','materiał przed obróbką'],'Tematy',None),
('02','Montaż / poradniki','uczyć konkretnie: 1 film = 1 problem = 1 odpowiedź.',['klejenie','poziomowanie','fugowanie','dobór koloru fugi','impregnacja','docinki','narożniki','błędy przy montażu'],'Tematy',None),
('03','Pytanie od widza','odpowiadać na realne pytania klientów.',['komentarze','wiadomości','pytania klientów','rozmowy handlowe'],'Źródło','Schemat: pytanie → szybka odpowiedź → pokazanie na materiale → CTA do kolejnego filmu / komentarza.'),
('04','Błędy i mity','edukacja i zatrzymanie uwagi przez konkretny problem.',['„Czy zawsze potrzebujesz lasera?”','„Czy klej nakłada się grzebieniem?”','„Czy stara cegła musi wyglądać identycznie?”','„Czy cegłę trzeba impregnować?”','„Czy nadaje się na elewację?”'],'Przykłady',None),
('05','Realizacja z historią','pokazać zmianę, nie tylko gotowe wnętrze.',['przed','problem / decyzja','materiał','montaż','efekt'],'Schemat','Realizacja ma być historią zmiany, a nie samym estetycznym kadrem.'),
('06','Produkt w kontekście','pomóc wyobrazić sobie produkt we własnej przestrzeni.',['RETRO w klasycznym wnętrzu','cegła na tarasie','cegła w łazience','cegła przy kominku','elewacja','jodełka','różne kolory fug'],'Tematy',None),
('07','Kulisy / ludzie','pokazać realną kompetencję i charakter pracy.',['codzienna praca','magazyn','przygotowanie zamówień','montaż','sytuacje z hali'],'Pokazujemy','Nie przypadkowy „dzień z życia”.')]
tiles=''.join(f'<div style="border-top:1px solid {H};padding:8px 0 10px"><div style="{MF};font-weight:300;font-size:22px;letter-spacing:-.05em;color:{T};line-height:1">{c[0]}</div><div style="font-size:14px;font-weight:500;letter-spacing:-.02em;margin-top:5px;color:#111">{c[1]}</div></div>' for c in pil)
def bar(a,b,c):return f'<div style="margin-top:10px"><div style="display:flex;justify-content:space-between;{M};color:#111"><span>{b}</span><span>{a}</span></div><div style="height:14px;width:{a};background:{c};margin-top:4px"></div></div>'
p=lab(L+' · mix i filary')+h1('Docelowy mix: 70 / 30.')+para('Kierunek planowania, nie sztywna reguła.')
p+=cols(bar('70%','Proces i wiedza',G)+f'<div style="margin-top:8px">{li(["produkcja, cięcie, selekcja,","montaż, fugowanie, impregnacja,","odpowiedzi na pytania,","błędy i rozwiązania."],"+",G,12.5,3)}</div>',bar('30%','Realizacje i inspiracje',T)+f'<div style="margin-top:8px">{li(["realizacje, inspiracje,","przed / po,","zastosowania produktu,","historie klientów."],"+",T,12.5,3)}</div>',6)
p+=f'<div style="margin-top:26px">{sub("Siedem filarów",T)}</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:0 26px">{tiles}</div>'
W('p076',p,0)
def pc(c):
    n,t,cel,items,lt,rule=c
    b=row('Cel',cel)+f'<div style="margin-top:10px">{sub(lt)}{chips(items)}</div>'
    if rule:b+=box('Zasada',rule,10)
    return card(n,t,b,12)
def stack(l,gap=20):return f'<div style="display:flex;flex-direction:column;gap:{gap}px">'+''.join(l)+'</div>'
W('p077',lab(L+' · filary')+stack([pc(c) for c in pil[0:3]]),0)
W('p078',lab(L+' · filary')+stack([pc(c) for c in pil[3:7]],16),0)
# p079 hook + format
p=lab(L+' · hook i format')
p+=card('08','Hook — pierwsza sekunda',row('Pytanie','„Dlaczego mam oglądać dalej?”')+f'<div style="margin-top:12px">{sub("Dobre typy hooków")}{chips(["pytanie","błąd","zaskakujący fakt","obietnica efektu","czynność dziejąca się w kadrze"])}</div>'+cols(sub('Przykłady')+li(['„Klejenie bez grzebienia?”','„Nie potrzebujesz lasera?”','„Tak powstaje płytka ze 100-letniej cegły.”','„Ten błąd psuje fugę.”','„Dlaczego te płytki nie są identyczne?”','„Elewacja czy wnętrze — gdzie sprawdzi się ten model?”'],'→',T),sub('Unikamy',T)+li(['„Zobaczcie…” bez konkretu,','„Tak to wygląda…”,','„Ściany, które potrafią mówić”,','pustych haseł emocjonalnych,','długiego intro z logo.'],'×',T)))
p+=card('09','Format i długość',para('Najmocniejsze materiały w analizowanym profilu były krótkie i dynamiczne.',8)+steps([('5–20 s','Zwykle'),('1 temat','Na film'),('Od 1. kadru','Akcja'),('Seria','Dłuższy materiał dzielimy')],12)+para('Dłuższy film tylko wtedy, gdy temat wymaga narracji i utrzymuje uwagę.',10))
W('p079',p,24)
# p080 serie + okładki
p=lab(L+' · serie i okładki')
ser=['„Jak powstaje?”','„Błąd przy montażu”','„Pytanie od widza”','„1 minuta / 20 sekund o starej cegle”','„Przed i po”','„Czy wiesz, że…?”','„Produkt w realizacji”']
p+=card('10','System serii',f'<div style="margin-top:12px">{chips(ser,G,True)}</div>'+para('Numerowanie części tam, gdzie pomaga śledzić serię. Graficzne okładki serii: następna strona.',10))
p+=card('11','Okładki / siatka profilu',para('Obecnie siatka ma kilka różnych stylów tekstowych, a część okładek nie ma tekstu.',8)+cols(sub('Docelowy standard')+li(['jeden krój pisma i sposób zapisu,','stałe miejsce komunikatu,','wysoki kontrast,','2–5 słów.'],'+',G),sub('Nie stosować',T)+li(['dekoracyjnych fontów,','przypadkowej zmiany kolorów,','niezgodności z identyfikacją marki.'],'×',T))+box('Okładka odpowiada na pytanie','„O czym jest ten film?”',12)+f'<div style="margin-top:12px">{sub("Przykłady")}{chips(["KLEJENIE BEZ GRZEBIENIA?","JAK POWSTAJE PŁYTKA?","BŁĄD PRZY FUGOWANIU","RETRO NA ELEWACJI","JAK DOBRAĆ FUGĘ?"],G,True)}</div>')
W('p080',p,24)
# p081 bio + CTA
p=lab(L+' · bio i CTA')
p+=card('12','Bio profilu',para('Obecne bio nie tłumaczy jasno, czym zajmuje się firma i jaki jest kolejny krok użytkownika.',8)+steps([('01','Kim jesteśmy'),('02','Co produkujemy'),('03','Gdzie / jak kupić'),('04','Jedno CTA')],12)+box('Kierunek','„Płytki z autentycznej starej cegły. Produkcja • montaż • realizacje. Zamów próbkę / zobacz ofertę ↓”',12)+para('Nie umieszczamy kilku numerów telefonu. Priorytet: jedno główne CTA i klikalna ścieżka do strony.',8))
ct=[('Zaangażowanie',['„Gdzie położyłbyś taką cegłę?”','„Który wariant wybrałbyś?”','„Masz pytanie o montaż? Napisz w komentarzu.”']),('Edukacja',['„Zapisz, jeśli będziesz fugować.”','„Zobacz kolejną część.”']),('Decyzja',['„Próbki znajdziesz w linku w bio.”','„Zobacz dostępne warianty.”','„Sprawdź realizacje.”'])]
tt=''.join(f'<div style="border-top:2px solid {T};padding-top:8px"><div style="{M};color:{T}">{a}</div><div style="margin-top:6px">{li(c,"·",G,12,4)}</div></div>' for a,c in ct)
p+=card('13','CTA w filmach',para('Nie każdy film ma sprzedawać bezpośrednio.',8)+f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:12px">{tt}</div>'+box('Zasada','1 film = 1 główne CTA.',14))
W('p081',p,24)
# p081x1 komentarze, hashtagi, rytm
p=lab(L+' · komentarze, hashtagi, rytm')
p+=card('14','Komentarze jako źródło contentu',para('Komentarz z realnym pytaniem klienta jest gotowym briefem do kolejnego filmu.',8)+steps([('01','Zbieramy pytania'),('02','Grupujemy tematycznie'),('03','Odpowiadamy wideo'),('04','Zapisujemy do biblioteki FAQ')],12)+para('Najlepsze odpowiedzi wykorzystujemy też na WWW, YouTube, Facebooku i w Google Business Profile.',10))
p+=card('15','Hashtagi',cols(li(['3–5 stałych tagów niszowych,','1–2 dopasowane do tematu.'],'+',G)+f'<div style="margin-top:8px">{chips(["#płytkiceglane","#staracegła","#ścianazcegły"],G)}</div><div style="margin-top:6px">{chips(["#elewacja","#kominek","#fugowanie","#montaż","#remont"],T)}</div>',li(['literówek i spacji po #,','przypadkowej listy ogólnych tagów,','tagów tylko dlatego, że są popularne.'],'×',T)))
p+=card('16','Rytm publikacji',cols(f'<div style="{MF};font-weight:300;font-size:44px;letter-spacing:-.05em;color:{T};line-height:1">4–6</div><div style="font-size:13px;color:#333;margin-top:4px">mocnych materiałów tygodniowo — lepiej niż codzienna publikacja ze słabymi inspiracjami. Nie zwiększamy częstotliwości.</div>',sub('Priorytet')+li(['jakość hooka,','właściwy temat,','powtarzalne serie,','analiza retencji.'],'→',T))+para('Godziny i docelową częstotliwość ustalają dopiero dane z TikTok Studio.',10))
W('p081x1',p,22)
# p081x2 pomiar
p=lab(L+' · pomiar')
p+=card('17','Co mierzymy',para('Po uzyskaniu dostępu do TikTok Studio. Nie oceniamy treści tylko po wyświetleniach.',8)+f'<div style="margin-top:10px">{chips(["wyświetlenia","średni czas oglądania","obejrzenie do końca","retencja 1., 3. i kolejnych sekund","źródła ruchu","zapisania","udostępnienia","komentarze","wejścia na profil","kliknięcia linku","przyrost obserwujących"])}</div>'+f'<div style="margin-top:12px">{sub("Najważniejsze pytania")}{li(["które tematy zatrzymują uwagę,","które generują zapisania,","które prowadzą na profil,","które wywołują pytania zakupowe."],"?",T)}</div>')
p+=card('18','Miesięczny przegląd',cols(li(['Top 5 filmów według wyświetleń.','Top 5 według zapisów / udostępnień.','Najczęstsze pytania w komentarzach.','Najsłabsze filmy.'],'□',G),li(['Porównanie filarów.','3 tematy do powtórzenia / rozwinięcia.','Aktualizacja listy hooków.','Kontrola bio i CTA.'],'□',G),10))
p+=card('19','Wzmacnianie zwycięzców',para('Jeśli temat wyraźnie przewyższa medianę:',8)+cols(li(['nie kopiujemy filmu 1:1,','tworzymy rozwinięcie,','nagrywamy część 2,'],'+',G),li(['odpowiadamy na komentarze,','pokazujemy problem z innej perspektywy.'],'+',G),8)+para('Płatne wsparcie (Promote / Spark Ads) dopiero po sprawdzeniu, że materiał działa organicznie i służy celowi biznesowemu.',8))
W('p081x2',p,20)
# p081x3
rel=[('TikTok','krótkie odkrycie / hook'),('YouTube','pełniejsze wyjaśnienie'),('WWW','produkt / poradnik / próbka'),('Facebook / Instagram','realizacja / społeczność'),('Google Business Profile','dowód aktywności i decyzja lokalna')]
rl=''.join(f'<div style="border-top:1px solid {H};padding:7px 0"><div style="{M};color:{T if a=="TikTok" else G}">{a}</div><div style="font-size:12.5px;color:#333;margin-top:2px">{b}</div></div>' for a,b in rel)
p=lab(L+' · kanały i dane')
p+=card('20','Powiązanie z innymi kanałami',f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:0 18px;margin-top:10px">{rl}</div>'+para('Jeden temat może pracować w wielu kanałach, ale nie kopiujemy go 1:1 bez dostosowania formatu.',8))
p+=card('21','Brakujące dane',para('Do pełnego audytu potrzebujemy TikTok Studio.',8)+cols(sub('Dane')+li(['retencja, średni czas oglądania,','źródła ruchu, demografia,','aktywność obserwujących,','wejścia na profil, kliknięcia linku,','konwersje / ruch do strony.'],'·',G),sub('Pozwolą ustalić',T)+li(['najlepsze godziny publikacji,','realną optymalną długość,','które hooki zatrzymują użytkowników,','czy TikTok prowadzi do strony / próbki.'],'→',T),10))
p+=f'<div style="background:#000;color:#fff;padding:22px 24px;margin-top:6px"><div style="{M};color:{T}">Główna zasada TikToka</div><div style="font-size:24px;font-weight:300;letter-spacing:-.03em;line-height:1.2;margin-top:8px">Ruch, proces, ręce, materiał i wiedza — to, czego nie da się przekazać jednym zdjęciem.</div></div>'
W('p081x3',p,22)
