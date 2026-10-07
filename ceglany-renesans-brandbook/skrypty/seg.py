import json,subprocess,sys,os
SRC='../../live56/project/p024f.dc.html'
S=open(SRC).read()
HEAD0=S[:S.index('<div class="cr pg">')]
TAIL='\n</x-dc>'+S.split('</x-dc>')[1]
M="font-family:'Overpass Mono',monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase;"
H="font-family:'Hanken Grotesk',sans-serif;"
OR,NV,BG,LN='#ED6842','#0D4C73','#EDE9D0','#E7DFC9'
def ul(items): return '<ul style="margin:6px 0 0;padding-left:16px">'+''.join(f'<li style="margin-bottom:2px">{i}</li>' for i in items)+'</ul>'
def block(label,col,inner,w=None):
    st=f'width:{w}px;' if w else ''
    return f'<div data-a style="{st}{H}font-size:12.5px;line-height:1.45;color:#333"><div style="{M}color:{col};font-size:12px">{label}</div>{inner}</div>'
def steps(items):
    chips=''.join(f'<span style="display:inline-flex;align-items:center;gap:8px;border:1px solid {LN};padding:5px 10px;margin:0 8px 8px 0;font-size:12.5px;{H}color:#333"><span style="{M}font-size:12px;color:{OR};letter-spacing:.05em">{i+1:02d}</span>{t}</span>' for i,t in enumerate(items))
    return f'<div data-a style="width:642px;{H}"><div style="{M}color:{NV};margin-bottom:8px">Ścieżka decyzji</div><div style="display:flex;flex-wrap:wrap">{chips}</div></div>'
def seg(n,total,name,lead,need,problem,trigger,criteria,obj,barr,path,notes=(),trig_html=None,barr_html=None,crit_note='',extra=''):
    out=[]
    out.append(f'<div data-a style="width:642px"><div style="{M}letter-spacing:.14em;color:{OR}">12 · Grupy docelowe · Segment {n} z {total}</div><div style="{H}font-size:36px;font-weight:300;letter-spacing:-.03em;line-height:1.1;margin-top:10px">{name}</div></div>')
    if lead: out.append(f'<div data-a style="width:642px;{H}font-size:14px;line-height:1.5;color:#555">{lead}</div>')
    out.append(f'<div data-a style="width:642px;box-sizing:border-box;background:{BG};padding:14px 18px;{H}font-size:13.5px;line-height:1.5;color:#000"><div style="{M}color:#000;margin-bottom:4px">Potrzeba</div>{need}</div>')
    out.append(block('Problem',OR,ul(problem),313))
    out.append(block('Trigger zakupowy',NV,trig_html or ul(trigger),313))
    out.append(block('Kryteria wyboru',NV,ul(criteria)+(f'<div style="margin-top:8px;color:#767676">{crit_note}</div>' if crit_note else ''),313))
    out.append(block('Obiekcje',OR,ul(obj),313))
    out.append(block('Bariery',OR,barr_html or ul(barr),642))
    out.append(steps(path))
    for t in notes: out.append(f'<div data-a style="width:642px;{H}font-size:12.5px;line-height:1.5;color:#767676;border-top:1px solid {LN};padding-top:10px">{t}</div>')
    return out
def flowpage(blocks,num,ttl):
    # layout: blocks index mapping handled by caller via grid markers
    pass

def flow(parts_top,grid,parts_bottom):
    return ('<div class="fl" style="position:absolute;left:76px;top:100px;width:642px;display:flex;flex-direction:column;gap:22px">'
        +''.join(parts_top)+'<div style="display:grid;grid-template-columns:313px 313px;gap:22px 16px;align-items:start">'+''.join(grid)+'</div>'+''.join(parts_bottom)+'</div>')
def segpage(**k):
    p=seg(**k)
    # p order: title, lead?, need, problem, trigger, criteria, obj, barr, steps, notes...
    i=0
    top=[];
    top.append(p[0]); i=1
    if k.get('lead'): top.append(p[1]); i=2
    top.append(p[i]); i+=1
    grid=p[i:i+4]; i+=4
    bottom=p[i:]
    return flow(top,grid,bottom)
SEGS=[
dict(n=1,total=4,name='Klient indywidualny',lead='Osoba budująca, remontująca lub urządzająca dom / mieszkanie. Szuka charakterystycznego materiału na ścianę, podłogę, kominek lub elewację.',
 need='Stworzyć wnętrze, które nie wygląda masowo i ma naturalny, autentyczny charakter.',
 problem=['trudno ocenić efekt na podstawie zdjęcia,','obawa, że cegła będzie wyglądała zbyt rustykalnie,','niepewność dotycząca montażu,','trudność z obliczeniem ilości materiału,','obawa przed różnicami kolorystycznymi.'],
 trigger=['remont salonu lub kuchni,','budowa domu,','projekt kominka,','wykończenie elewacji,','inspiracja znaleziona na Pinterest / Instagramie,','zobaczenie podobnej realizacji u kogoś.'],
 criteria=['efekt wizualny,','autentyczność materiału,','cena za m²,','dostępność próbki,','zdjęcia realizacji,','łatwość montażu,','dostępność chemii,','koszt dostawy.'],
 obj=['Czy na żywo będzie wyglądało tak jak na zdjęciu?','Czy kolor będzie równy?','Czy poradzimy sobie z montażem?','Czy cegła nie będzie się kruszyć?','Czy nie będzie za ciężka?','Czy łatwo ją utrzymać w czystości?'],
 barr=['brak możliwości zobaczenia produktu na żywo,','naturalna zmienność starej cegły,','większy ciężar i trudniejszy montaż niż lekkiej imitacji,','niepewność, ile materiału zamówić.'],
 path=['Inspiracja','wyszukiwanie „stara cegła na ścianę”','oglądanie realizacji','porównanie modeli','próbka','kalkulacja m² i kosztów','konsultacja','zakup'],
 notes=['To szczególnie ważne przy starej cegle, bo każda partia może różnić się kolorem, strukturą czy wymiarem — marka sama komunikuje, że jest to naturalna cecha produktu.']),
dict(n=2,total=4,name='Architekt / projektant wnętrz',lead=None,
 need='Znaleźć charakterystyczny materiał, który wnosi do projektu autentyczność i pozwala stworzyć realizację inną niż typowe wnętrza katalogowe.',
 problem=['musi przewidzieć efekt końcowy,','potrzebuje wiarygodnych informacji technicznych,','materiał musi pasować do koncepcji,','klient musi zaakceptować naturalne różnice starej cegły.'],
 trigger=[],trig_html='<div style="margin-top:6px">Nowy projekt:</div>'+ul(['domu,','apartamentu,','restauracji,','hotelu,','biura,','przestrzeni komercyjnej.']),
 criteria=['estetyka,','autentyczność,','dostępne warianty,','przewidywalność efektu,','dane techniczne,','możliwość zamówienia próbek,','dostępność produktu,','pomoc producenta,','zdjęcia dobrze wykonanych realizacji.'],
 obj=['Czy kolejna partia będzie podobna?','Czy klient zaakceptuje różnice?','Czy producent dostarczy odpowiednią ilość?','Czy materiał sprawdzi się technicznie w tym miejscu?'],
 barr=['brak dokumentacji technicznej,','brak próbnika dla projektanta,','brak dobrej biblioteki zdjęć,','nieprzewidywalność naturalnego materiału.'],
 path=['Koncepcja projektu','research materiałów','próbki','prezentacja klientowi','uzgodnienie kolorystyki','specyfikacja produktu','wycena','zamówienie'],
 notes=['Marka już oferuje próbki oraz możliwość dobrania produktu o podobnej kolorystyce do przesłanego zdjęcia, co może być bardzo użyteczne dla projektanta.']),
dict(n=3,total=4,name='Wykonawca / firma remontowa',lead=None,
 need='Materiał, który da się poprawnie zamontować i do którego są odpowiednie produkty montażowe.',
 problem=['różna grubość płytek,','konieczność odpowiedniego przygotowania podłoża,','fugowanie,','impregnacja,','odpowiedzialność za efekt końcowy.'],
 trigger=[],trig_html='<div style="margin-top:6px">Klient pokazuje projekt lub konkretną płytkę i pyta wykonawcę:</div><div style="margin-top:6px;font-weight:600;color:#000">Czy możemy to położyć?</div>',
 criteria=['parametry produktu,','łatwość montażu,','dostępność kleju, fugi i impregnatu,','instrukcje,','możliwość konsultacji,','szybka dostępność materiału.'],
 obj=['Będzie dużo docinania.','Płytki są nierówne.','Montaż potrwa dłużej.','Klient będzie reklamował naturalne różnice.'],
 barr=[],barr_html='<div style="margin-top:6px">Największa: wykonawca może <b>odradzić produkt klientowi</b>, jeśli nie czuje się pewnie z montażem.</div><div style="margin-top:6px">Dlatego ta grupa powinna mieć własne materiały: instrukcję montażu, rekomendowaną chemię, FAQ techniczne, poradniki wideo.</div>',
 path=['Projekt klienta','weryfikacja techniczna','konsultacja produktu','dobór chemii','zamówienie','montaż'],
 notes=['Na stronie Ceglany Renesans sam wskazuje, że przy płytkach podłogowych różnice grubości są naturalne i powinny być wyrównane odpowiednim klejem przez doświadczonego wykonawcę.']),
dict(n=4,total=4,name='Inwestor komercyjny / HoReCa / właściciel lokalu',lead='Potencjał dla restauracji, hoteli, apartamentów, salonów i innych wnętrz, w których materiał ma budować charakter miejsca.',
 need='Stworzyć przestrzeń, która wyróżnia się wizualnie i wspiera wizerunek lokalu.',
 problem=['materiał musi dobrze wyglądać przy większej powierzchni,','inwestor musi pilnować budżetu,','potrzebuje przewidywalnego terminu dostawy,','zależy mu na trwałości.'],
 trigger=['otwarcie nowego lokalu,','generalny remont,','rebranding wnętrza,','projekt architektoniczny.'],
 criteria=['efekt końcowy,','koszt całej realizacji,','możliwość zamówienia większej partii,','termin dostawy,','dostępność produktu,','trwałość,','wsparcie techniczne.'],
 obj=['Czy dostaniemy 150–300 m² w odpowiednio spójnej tonacji?','Czy materiał dotrze na czas?','Jak wygląda cena dla dużej inwestycji?','Jak później uzupełnić materiał?'],
 barr=['większe ryzyko inwestycyjne,','naturalna zmienność materiału,','konieczność wcześniejszego planowania dostawy.'],
 path=['Projekt','specyfikacja materiału','próbki','wycena','ustalenie dostępności i terminu','akceptacja inwestora','zamówienie','dostawa'],
 notes=['Przy większych zamówieniach firma deklaruje osobne terminy realizacji, np. dla zamówień powyżej 100 m², co jest istotne dla tego segmentu.']),
]
FILES=['p012b','p013','p014','p015']
os.makedirs('flow',exist_ok=True)
def write(fn,body,num,ttl,rh='Część I · 12 Grupy docelowe'):
    html=HEAD0.replace('25 Logo na tle',ttl)+f'<div class="cr pg"><div class="tab">{num}</div><div class="rh"><span>{rh}</span><span>Ceglany Renesans</span></div>'+body+'<div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n'+TAIL
    open(fn,'w').write(html)
for f,sg,num in zip(FILES,SEGS,[12,13,14,15]):
    write(f'flow/{f}.dc.html',segpage(**sg),num,f'Grupy docelowe: {sg["name"]}')
# summary page
rows=[('Klient indywidualny','wnętrze z charakterem','wygląd, próbka, cena, realizacje'),('Architekt / projektant','autentyczny materiał do projektu','próbki, estetyka, dane techniczne'),('Wykonawca','bezproblemowy montaż','parametry, chemia, instrukcje'),('Inwestor komercyjny','wyróżniająca się przestrzeń','efekt, cena, dostępność, termin')]
tbl=(f'<table data-a style="width:642px;border-collapse:collapse;border:1px solid {LN};{H}font-size:13.5px;line-height:1.5"><tr>'+''.join(f'<th style="text-align:left;font-weight:400;color:{NV};font-size:13px;padding:14px 12px;border-bottom:2px solid {OR};{"border-right:1px solid "+LN+";" if i<2 else ""}">{h}</th>' for i,h in enumerate(['Segment','Główna potrzeba','Co decyduje o zakupie']))+'</tr>'
 +''.join('<tr>'+''.join(f'<td style="padding:14px 12px;vertical-align:top;color:#333;{"border-right:1px solid "+LN+";" if i<2 else ""}{"border-bottom:1px solid "+LN+";" if r<3 else ""}">{c}</td>' for i,c in enumerate(row))+'</tr>' for r,row in enumerate(rows))+'</table>')
sumbody=('<div class="fl" style="position:absolute;left:76px;top:100px;width:642px;display:flex;flex-direction:column;gap:22px">'
 f'<div data-a style="width:642px"><div style="{M}letter-spacing:.14em;color:{OR}">12 · Grupy docelowe</div><div style="{H}font-size:36px;font-weight:300;letter-spacing:-.03em;line-height:1.1;margin-top:10px">Segmenty w skrócie.</div></div>'
 +tbl+'</div>')
write('flow/p016.dc.html',sumbody,16,'Grupy docelowe: segmenty w skrócie')
