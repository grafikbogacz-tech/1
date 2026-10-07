import re
P='all/project/project/'
M="font-family:'Overpass Mono',monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase"
def lb(t,c='#0D4C73',mt=12):return f'<div style="{M};color:{c};margin-top:{mt}px">{t}</div>'
def tx(t):return f'<div style="font-size:13px;line-height:1.45;color:#333;margin-top:3px">{t}</div>'
def badge(r,p):
    if r=='Do poprawy':st='color:#ED6842;border:1px solid #ED6842'
    elif r=='Super':st='background:#0D4C73;color:#fff;border:1px solid #0D4C73'
    else:st='color:#0D4C73;border:1px solid #0D4C73'
    return f'<div style="{M};letter-spacing:.08em;{st};padding:3px 9px;white-space:nowrap">{r} · {p}%</div>'
E=[
('IG-01','4a6d3f9106c3463f1d1b8193bd35c03d','Profil, bio i Highlights','Do poprawy',60,'profil @ceglanyrenesans',
 'profil z avatarem, bio, linkiem, liczbą obserwujących (ok. 12 tys.) i wyróżnionymi relacjami.',
 'nazwa marki jest spójna, profil ma dużą bazę odbiorców, a Highlights pokazują realizacje, montaż, próbki i opinie.',
 'pełne logo jest słabo czytelne w małym avatarze; bio informuje o produkcji, ale nie eksponuje autentycznej starej cegły i nie prowadzi do decyzji; Highlights mają niespójne nazwy i okładki.',
 '„Płytki z autentycznej starej cegły. / Produkcja • montaż • realizacje. / Zamów próbkę / zobacz ofertę ↓”',
 'uporządkować bio, avatar i nazwy Highlights.','Pierwszy ekran profilu ma odpowiedzieć: co to za marka, co sprzedaje i co użytkownik ma zrobić dalej.'),
('IG-02','6ffae2d009bef7561fe91b6fffce5ed4','Reel z montażu: „Kleimy nasze cudności”','Do poprawy',55,'rolka / post',
 'człowiek klejący płytki, bezpośredni kadr z pracy i napis na ekranie.',
 'prawdziwy montaż, ręce przy pracy, naturalny backstage i ruch; takiego materiału nie da się zastąpić stockiem.',
 'hook nie niesie wiedzy ani decyzji, a opis jest długi; pierwszy komunikat nie mówi, czego użytkownik się dowie.',
 '„Tak kleimy płytki ze starej cegły” albo „Montaż starej cegły — klejenie w praktyce”.',
 'hook ma nieść informację i prowadzić do konkretnej wiedzy.','Swobodnie, ale nie potocznie: hook niesie informację.'),
('IG-03','e718679039f8719c9cf23a59e923b6a6','Montaż na elewacji: „Tak wygląda dom przed montażem”','Dobry',70,'rolka / post',
 'etap przed montażem i komunikacja z realizacji elewacji.',
 'bardzo dobry format dowodowy: pokazuje punkt wyjścia i proces, który można zestawić z efektem.',
 'opis powinien uporządkować, co będzie montowane, jaki produkt wybrano i dlaczego.',
 'seria „PRZED → MONTAŻ → EFEKT” z oznaczeniem produktu w każdym etapie.',
 'budować serię i podawać produkt na każdym etapie.','Before/after jest jednym z podstawowych formatów realizacyjnych marki.'),
('IG-04','9752a704f2d7b5b279ac4649ebf11b0b','Gotowa realizacja przy schodach','Dobry',65,'rolka / post',
 'ceglana ściana przy schodach w gotowym wnętrzu.',
 'produkt w skali i w realnym kontekście; dowód, że cegła może być fragmentem wnętrza, a nie dominującą dekoracją.',
 'opis jest bardzo krótki; brakuje nazwy produktu i powodu, dla którego rozwiązanie działa.',
 'seria „Gdzie zastosować cegłę?” z jednym praktycznym wnioskiem: „Cegła przy schodach — kiedy działa najlepiej?”.',
 'dopisać produkt i jeden wniosek do każdej realizacji.','Realizacja ma wyjaśniać zastosowanie, nie tylko pokazywać efekt.'),
('IG-05','e721d1464a6e8b01a8d3080e7ea64a82','Ściana przed realizacją: „Tak było przed”','Do poprawy',50,'post / grafika',
 'surowa ściana przed montażem z prostym napisem.',
 'czytelny pierwszy etap historii i dobry materiał do sekwencji przed / po.',
 'samodzielnie ten kadr ma niską wartość; powinien być częścią karuzeli lub Reela z procesem i efektem.',
 'nie publikować „przed” bez dalszego ciągu; łączyć z etapem montażu i finałem w jednej karuzeli.',
 'łączyć „przed” z montażem i efektem.','Pojedynczy etap procesu ma sens wtedy, gdy prowadzi odbiorcę do kolejnego etapu.')]
foot='<div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n</x-dc><script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":794,"height":1123}}\'>class Component extends DCLogic{renderVals(){return {};}}</script></body></html>'
old=open(P+'p170h.dc.html').read();head=old[:old.index('<div class="cr pg">')]
src=open(P+'p170g.dc.html').read();intro=src[src.index('<div style="position:absolute;left:76px;top:100px;width:642px"><div style="font-family'):src.index('<div style="position:absolute;left:76px;top:215px')]
names=['p170g','p170h','p170i','p170j','p170k']
for i,(n,e) in enumerate(zip(names,E)):
    code,b,t,r,p,typ,desc,ok,bad,better,rec,rule=e
    tab=200+i
    body=f'<div class="cr pg"><div class="tab">{tab}</div><div class="rh"><span>Część VII · Biblioteka przykładów</span><span>Ceglany Renesans</span></div>'
    top=116
    if i==0:body+=intro.replace('Instagram — przykłady materiałów.','Instagram — przykłady materiałów.');top=231;body+='<div style="position:absolute;left:76px;top:215px;width:642px;border-top:1px solid #E7DFC9"></div>'
    else:body+='<div style="position:absolute;left:76px;top:100px;width:642px;border-top:1px solid #E7DFC9"></div>'
    head_row=f'<div style="display:flex;justify-content:space-between;align-items:center"><div style="{M};color:#ED6842">{code}</div>{badge(r,p)}</div><div style="font-size:18px;font-weight:500;letter-spacing:-.02em;line-height:1.2;margin-top:6px;color:#111">{t}</div>'
    if i<=3:
        W_=642 if i==0 else 560
        H_={0:319,1:419,2:418,3:421}[i]
        body+=f'<img src="/_blob/{b}" alt="{code}" style="position:absolute;left:76px;top:{top}px;width:{W_}px;height:auto;border:1px solid #E7DFC9;display:block">'
        y=top+H_+14
        body+=f'<div style="position:absolute;left:76px;top:{y}px;width:642px">{head_row}<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px"><div>{lb("Opis")}{tx(desc)}</div><div>{lb("Co działa")}{tx(ok)}</div><div>{lb("Co poprawić","#ED6842")}{tx(bad)}</div></div></div>'
        body+=f'<div style="position:absolute;left:76px;top:{y+200}px;width:642px"><div style="display:grid;grid-template-columns:1fr 1fr;gap:34px;border-top:1px solid #E7DFC9;padding-top:12px"><div>{lb("Przykład lepszej wersji",mt=0)}{tx(better)}</div><div>{lb("Rekomendacja",mt=0)}{tx(rec)}{lb("Reguła Brand Booka")}{tx(rule)}</div></div></div>'
    else:
        body+=f'<img src="/_blob/{b}" alt="{code}" style="position:absolute;left:76px;top:{top}px;width:250px;height:auto;border:1px solid #E7DFC9;display:block">'
        body+=f'<div style="position:absolute;left:346px;top:{top}px;width:372px">{head_row}{lb("Typ materiału")}{tx(typ)}{lb("Opis")}{tx(desc)}{lb("Co działa")}{tx(ok)}{lb("Co poprawić","#ED6842")}{tx(bad)}</div>'
        by=631 if i!=4 else 631
        body+=f'<div style="position:absolute;left:76px;top:{by}px;width:642px"><div style="display:grid;grid-template-columns:1fr 1fr;gap:34px;border-top:1px solid #E7DFC9;padding-top:12px"><div>{lb("Przykład lepszej wersji",mt=0)}{tx(better)}</div><div>{lb("Rekomendacja",mt=0)}{tx(rec)}{lb("Reguła Brand Booka")}{tx(rule)}</div></div></div>'
    open(P+n+'.dc.html','w').write(head.replace('Strona 200','Strona '+str(tab)).replace('Strona 201','Strona '+str(tab))+body+foot)
print(re.findall('<title>[^<]*',open(P+'p170k.dc.html').read()))
