import sys,json;sys.path.insert(0,'build')
from ig import *
Z=json.load(open('build/mxz.json')) if len(sys.argv)>1 else {}
def W(n,inner,gap=16):write(n,inner,gap,Z.get(n,1))
L='44.4 · Matryca treści'
def table(rows,cols_w,head=None,fs=12.5):
    g=' '.join(cols_w)
    o=''
    if head:o+=f'<div style="display:grid;grid-template-columns:{g};gap:0 14px;border-bottom:2px solid {T};padding:0 0 6px">'+''.join(f'<div style="{M};color:{G}">{h}</div>' for h in head)+'</div>'
    for r in rows:
        o+=f'<div style="display:grid;grid-template-columns:{g};gap:0 14px;border-bottom:1px solid {H};padding:8px 0">'
        for i,c in enumerate(r):
            if i==0:o+=f'<div style="font-size:13.5px;font-weight:500;color:{T if False else "#111"};letter-spacing:-.01em">{c}</div>'
            else:
                if isinstance(c,list):o+=f'<div style="font-size:{fs}px;line-height:1.4;color:#333">'+''.join(f'<div style="display:flex;gap:6px;margin-bottom:2px"><span style="color:{G};{MF};flex:none">·</span><span>{x}</span></div>' for x in c)+'</div>'
                else:o+=f'<div style="font-size:{fs}px;line-height:1.4;color:#333">{c}</div>'
        o+='</div>'
    return o
# 114
p=lab(L)+h1('Jeden temat, wiele formatów.')+para('Jeden temat źródłowy pracuje w kilku kanałach, ale nie jest kopiowany 1:1.')
p+=f'<div style="background:#000;color:#fff;padding:20px 24px;margin-top:16px"><div style="{M};color:{T}">Główna zasada</div><div style="font-size:22px;font-weight:300;letter-spacing:-.03em;line-height:1.25;margin-top:8px">Jeden temat → wiele formatów → jeden spójny przekaz.</div></div>'
p+=f'<div style="margin-top:22px">{sub("Najpierw ustalamy",T)}'+steps([('01','Co chcemy powiedzieć'),('02','Jaki materiał mamy'),('03','Jaki jest cel'),('04','Dopiero potem adaptacja do kanału')],0)+'</div>'
p+=box('Zasada produkcji','Nie planujemy osobno „posta na Facebooka”, „posta na Instagram”, „TikToka”. Plan zaczyna się od TEMATU, a każdy kanał pełni własną rolę w tej samej ścieżce użytkownika. Nie tworzymy pięciu strategii treści, tylko jeden system tematów.',22)
W('p093',p,0)
# 115 role
role=[('Facebook',['szersza narracja','społeczność, wyjaśnienie','realizacje, opinie','informacje i aktualności'],['post + zdjęcie, album','karuzela','link do poradnika','dłuższy opis realizacji','UGC / opinia','wydarzenie / aktualność']),
('Instagram',['estetyka','produkt w kontekście','realizacja','zapis / udostępnienie','szybka edukacja'],['Reels, karuzela','mocne zdjęcie','Stories, Highlights','przed / po']),
('TikTok',['zasięg','szybki hook, proces','ręce przy pracy','konkretna odpowiedź'],['5–20 s','jeden problem, jedna odpowiedź','pytanie od widza','seria']),
('YouTube',['pogłębienie','pełny poradnik','proces, porównanie','case study'],['film 16:9','Shorts','playlisty tematyczne']),
('Google Business Profile',['wsparcie decyzji','aktualność','lokalna wiarygodność','przejście do produktu / kontaktu'],['realizacja, produkt','poradnik','promocja','aktualność'])]
p=lab(L+' · role kanałów')+h1('Rola kanałów.',32)+f'<div style="margin-top:16px">{table(role,["120px","1fr","1fr"],["Kanał","Rola","Najlepsze formaty"])}</div>'
W('p094',p,0)
# topics
T10=[('01','Realizacja','zdjęcia przed / po, gotowa przestrzeń, nazwa produktu, miejsce zastosowania, krótka historia realizacji.',[['3–5 zdań','kontekst realizacji, produkt','co warto zauważyć, jedno CTA'],['mocne zdjęcie / Reel','jeden temat przewodni, krótki opis','CTA „Zapisz jako inspirację”'],['nie samo „ładne wnętrze”','przed → proces → efekt','hook: „Cegła nie musi być na całej ścianie”'],['jeśli realizacja ma historię: case study','produkt + decyzje + efekt'],['zdjęcie, 2–4 zdania, produkt','link do realizacji / produktu']]),
('02','Montaż','nagrania z montażu, zdjęcia etapów, komentarz wykonawcy.',[['wyjaśnienie etapu','praktyczna wskazówka, link do poradnika'],['Reel z konkretnym hookiem','karuzela „krok po kroku”'],['1 film = 1 etap, 5–20 s','np. „Klejenie bez grzebienia?”'],['pełny poradnik','seria: podłoże → klejenie → fuga → impregnacja'],['krótki poradnik / link do strony montażowej']]),
('03','Produkt','packshot, detal, kolor, struktura, realizacja z danym modelem.',[['opis produktu, różnice','zastosowanie, link do produktu'],['produkt + realizacja','karuzela porównawcza, detal + jedno zastosowanie'],['szybkie porównanie','„RETRO czy CLASSIC?”','„Dlaczego te płytki nie są identyczne?”'],['pełne porównanie','„jak wygląda / czym się różni / gdzie się sprawdzi”'],['produkt, krótki argument','link bezpośredni do karty']]),
('04','Proces / autentyczność','odzysk, selekcja, cięcie, sortowanie, pakowanie.',[['historia materiału, wyjaśnienie procesu','dlaczego różnice są naturalne'],['Reel / karuzela','estetyczny detal procesu'],['najmocniejszy format zasięgowy, ręce przy pracy','hook: „Tak powstaje płytka ze starej cegły”'],['pełny film „Od cegły do płytki”'],['krótka aktualność / dowód producenta']]),
('05','Poradnik / FAQ','pytania klientów, komentarze, maile, telefon, FAQ ze strony.',[['pełna odpowiedź, spokojne wyjaśnienie','link do artykułu'],['karuzela, Reel 15–30 s','Stories z ankietą'],['pytanie od widza','odpowiedź w 5–20 s'],['pełny poradnik','FAQ w serii'],['krótka odpowiedź + link do poradnika']]),
('06','Próbki','zestaw próbek, pakowanie, odbiorca porównujący warianty.',[['dlaczego próbka pomaga podjąć decyzję','jak zamówić'],['Reel / karuzela „co dostajesz w próbce?”','CTA „Zamów próbkę”'],['szybkie pokazanie różnic','„Którą wybrałbyś?”'],['film „jak wybrać produkt na podstawie próbek”'],['post produktowy z linkiem do próbek']]),
('07','Opinia / UGC','zdjęcie klienta, opinia, oznaczenie, komentarz.',[['repost z kontekstem','podziękowanie, krótki komentarz marki'],['repost, Stories','realizacja klienta, Highlight „Opinie”'],['tylko jeśli mamy wideo / historię','nie przerabiamy suchej opinii na sztuczny film'],['tylko większe case study lub testimonial'],['odpowiedź na opinię','post tylko, gdy materiał wnosi wartość']]),
('08','Promocja','konkretny produkt, warunek, termin, landing page.',[['produkt → warunek → cena / rabat → CTA'],['produkt w pierwszej kolejności','promocja jako drugi komunikat, Stories do pilności'],['nie robimy z promocji głównego filaru','produkt + konkretny powód + warunek'],['tylko jako element opisu / CTA','nie budujemy kanału na rabatach'],['dobry kanał dla aktualnej oferty','jeden link i jasny termin']]),
('09','Ludzie / kulisy','zespół, magazyn, montaż, pakowanie, codzienna praca.',[['historia człowieka / roli','kontekst'],['Stories, Reel','zdjęcie zespołu'],['naturalne kulisy','sytuacja z pracy, realne zadanie'],['większy materiał o zespole / procesie'],['tylko jeśli wspiera wiarygodność lub aktualność']]),
('10','Porównanie','dwa produkty, dwa kolory, dwa style, dwie fugi.',[['spokojne wyjaśnienie różnic'],['karuzela „A czy B?”','zapis / udostępnienie'],['szybkie porównanie','jeden parametr na film'],['pełne porównanie z zastosowaniem'],['krótki post tylko wtedy, gdy prowadzi do właściwej kategorii']])]
chn=['Facebook','Instagram','TikTok','YouTube','GBP']
# 116 overview
rows=[(f'<span style="{MF};font-weight:300;font-size:20px;letter-spacing:-.05em;color:{T};margin-right:10px">{a}</span>{b}',c) for a,b,c,_ in T10]
p=lab(L+' · tematy')+h1('Dziesięć tematów źródłowych.',32)+para('Każdy temat zaczyna się od materiału źródłowego. Na kolejnych stronach: jak ten sam temat adaptujemy w pięciu kanałach.',8)+f'<div style="margin-top:14px">{table(rows,["210px","1fr"],["Temat","Materiał źródłowy"])}</div>'
W('p095',p,0)
def tcard(t):
    a,b,c,ch=t
    rows=[(chn[i],ch[i]) for i in range(5)]
    return card(a,b,row('Materiał',c)+f'<div style="margin-top:10px">{table(rows,["88px","1fr"])}</div>',10)
for n,i in zip(['p096','p097','p098','p099','p100'],range(0,10,2)):
    W(n,lab(L+' · tematy × kanały')+f'<div style="display:flex;flex-direction:column;gap:18px">{tcard(T10[i])}{tcard(T10[i+1])}</div>',0)
# p101 cele
goals=[('Zasięg','TikTok → Instagram Reels → YouTube Shorts',['proces','błędy, mity','montaż','zaskoczenie']),('Edukacja','YouTube → Facebook → Instagram karuzela → TikTok',['montaż, fuga','impregnacja','wybór produktu','różnice materiału']),('Inspiracja','Instagram → Facebook → GBP',['realizacje, przed / po','wnętrza, elewacje','zastosowania']),('Decyzja','GBP → Facebook → Instagram → WWW',['próbki, produkt','opinie','realizacje, porównania']),('Autentyczność','TikTok → YouTube → Instagram → Facebook',['proces','stare cegły przed obróbką','selekcja, ludzie, produkcja'])]
p=lab(L+' · cele')+h1('Matryca celów.',32)+para('Najpierw cel, potem kolejność kanałów.',8)+f'<div style="margin-top:14px">{table(goals,["110px","1fr","1fr"],["Cel","Priorytet kanałów","Najlepsze tematy"])}</div>'
W('p101',p,0)
# p101x1 example
slides=['Jak dobrać fugę?','Jasna','Ciemna','Efekt na całej ścianie','Na co uważać','Zapisz poradnik']
sl=''.join(f'<div style="border:1px solid {G};padding:8px 6px;font-size:12px;line-height:1.3;color:{G};min-height:46px"><span style="{MF};font-size:11px;color:{T}">{i+1}</span><br>{s}</div>' for i,s in enumerate(slides))
ex=[('TikTok','15 sekund. Hook: „Najczęstszy błąd? Fuga dobrana tylko do jednej płytki.”'),('Instagram',f'karuzela:<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:6px;margin-top:6px">{sl}</div>'),('Facebook','post z szerszym wyjaśnieniem i przykładami.'),('YouTube','pełny poradnik 4–6 minut.'),('GBP','„Kolor fugi potrafi zmienić odbiór całej ściany. Zobacz poradnik.”'),('WWW','pełny artykuł / poradnik.')]
p=lab(L+' · przykład')+h1('Jeden temat — „Jak dobrać kolor fugi?”',30)+f'<div style="margin-top:16px">{table(ex,["90px","1fr"])}</div>'
W('p101x1',p,0)
# p101x2 pakiety
p=lab(L+' · pakiety')
p+=card('A','Minimalny pakiet z jednej realizacji',para('Jeśli materiał na to pozwala. Nie publikujemy wszystkiego tego samego dnia.',8)+f'<div style="margin-top:12px">{chips(["1 Reel Instagram","1 TikTok","1 post Facebook","1 Stories","1 wpis GBP","1 Short YouTube","1 zdjęcie / case study na WWW"],G,True)}</div>')
p+=card('B','Minimalny pakiet z jednego poradnika',para('Przykład: „Fugowanie starej cegły”.',8)+table([('YouTube','pełny poradnik'),('TikTok','3–5 krótkich odpowiedzi'),('Instagram','1 Reel + 1 karuzela'),('Facebook','post edukacyjny'),('GBP','krótki wpis z linkiem'),('WWW','artykuł / instrukcja')],['110px','1fr']).replace('margin','margin'))
W('p101x2',p,26)
# p101x3 kalendarz
days=[('Pon','TikTok'),('Wt','Instagram Reel'),('Śr','Stories'),('Czw','Facebook'),('Pt','GBP'),('Kolejny tydzień','YouTube / WWW')]
cal=''.join(f'<div style="display:flex;gap:20px;align-items:baseline;border-top:1px solid {H};padding:18px 0"><div style="{M};color:{T};width:120px;flex:none">{a}</div><div style="font-size:20px;font-weight:300;letter-spacing:-.025em;color:#111">{b}</div></div>' for a,b in days)
p=lab(L+' · kalendarz')+h1('Kalendarz — jeden temat dłużej.',30)+para('Nie publikujemy wszystkich kanałów równocześnie. Dzięki temu jeden temat pracuje dłużej.',8)+f'<div style="margin-top:18px;border-bottom:1px solid {H}">{cal}</div>'+box('Zasada','jeden temat → kilka dni → kilka kanałów, każdy w swojej formie.',22)
W('p101x3',p,0)
# p101x4 karta tematu
fields=['Temat','Cel','Materiał źródłowy','Produkt','Główny argument','CTA','Kanały','Formaty','Termin publikacji']
fl=''.join(f'<div style="border-bottom:1px solid #000;padding:22px 0 6px;display:flex;gap:12px;align-items:baseline"><span style="{MF};font-size:11px;color:{T};width:22px">{i+1:02d}</span><span style="{M};color:{G};width:150px;flex:none">{f}</span><span style="flex:1"></span></div>' for i,f in enumerate(fields))
p=lab(L+' · karta tematu')+h1('Karta tematu.',32)+para('Dla każdego tematu tworzymy kartę, zanim powstanie jakikolwiek materiał.',8)+f'<div style="margin-top:20px">{fl}</div>'
W('p101x4',p,0)
# p101x5 checklist
ck=['Czy materiał ma jeden główny temat?','Czy wiemy, jaki produkt pokazujemy?','Czy mamy jeden główny argument?','Czy CTA jest właściwe dla kanału?','Czy tekst został dostosowany, a nie skopiowany 1:1?','Czy zdjęcie / wideo pasuje do formatu?','Czy link prowadzi do właściwej podstrony?','Czy komunikacja jest zgodna z Brand Bookiem?','Czy nie powtarzamy promocji częściej niż wartości produktu?','Czy mamy zgodę na UGC / zdjęcia klienta?']
cl=''.join(f'<div style="display:flex;gap:12px;align-items:center;border-bottom:1px solid {H};padding:9px 0;font-size:13.5px;color:#111"><span style="width:16px;height:16px;border:1.5px solid {G};flex:none"></span>{c}</div>' for c in ck)
p=lab(L+' · checklista')+h1('Przed publikacją w wielu kanałach.',30)+f'<div style="margin-top:14px">{cl}</div>'
p+=f'<div style="background:#000;color:#fff;padding:20px 24px;margin-top:22px"><div style="{M};color:{T}">Główna zasada matrycy</div><div style="font-size:19px;font-weight:300;letter-spacing:-.03em;line-height:1.3;margin-top:8px">Nie tworzymy pięciu różnych strategii treści. Tworzymy jeden system tematów, a każdy kanał pełni własną rolę w tej samej ścieżce użytkownika.</div></div>'
W('p101x5',p,0)
