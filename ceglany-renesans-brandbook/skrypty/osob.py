import os
SRC='../../live56/project/p024f.dc.html'
S=open(SRC).read()
HEAD0=S[:S.index('<div class="cr pg">')]
TAIL='\n</x-dc>'+S.split('</x-dc>')[1]
M="font-family:'Overpass Mono',monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase;"
H="font-family:'Hanken Grotesk',sans-serif;"
OR,NV,BG,LN='#ED6842','#0D4C73','#EDE9D0','#E7DFC9'
os.makedirs('flow',exist_ok=True)
def D(inner,st='',w=None): 
    ww=f'width:{w}px;' if w else ''
    return f'<div data-a style="{ww}{st}">{inner}</div>'
def title(lb,h1,su=None):
    s=f'<div style="{M}letter-spacing:.14em;color:{OR}">{lb}</div><div style="{H}font-size:36px;font-weight:300;letter-spacing:-.03em;line-height:1.1;margin-top:10px">{h1}</div>'
    r=[D(s,'',642)]
    if su: r.append(D(su,H+'font-size:14px;line-height:1.5;color:#555;',642))
    return r
def ul(items): return '<ul style="margin:6px 0 0;padding-left:16px">'+''.join(f'<li style="margin-bottom:2px">{i}</li>' for i in items)+'</ul>'
def lab(t,c): return f'<div style="{M}color:{c}">{t}</div>'
TXT=H+'font-size:13px;line-height:1.5;color:#333;'
def card(label,col,quote,w=None):
    return D(f'<div style="border-left:3px solid {col};padding:2px 0 2px 14px"><div style="{M}color:{col};margin-bottom:4px">{label}</div><div style="{H}font-size:13.5px;line-height:1.5;color:#000">{quote}</div></div>','',w)
def write(fn,parts,num,ttl,gap=22):
    html=HEAD0.replace('25 Logo na tle',ttl)+f'<div class="cr pg"><div class="tab">{num}</div><div class="rh"><span>Część I · 13 Osobowość marki</span><span>Ceglany Renesans</span></div><div class="fl" style="position:absolute;left:76px;top:100px;width:642px;display:flex;flex-direction:column;gap:{gap}px">'+''.join(parts)+'</div><div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n'+TAIL
    open('flow/'+fn,'w').write(html)
def grid2(left,right,lw=280,rw=346,gap=16):
    # left, right: list of data-a elements wrapped into column containers
    return f'<div style="display:grid;grid-template-columns:{lw}px {rw}px;gap:{gap}px;align-items:start"><div style="display:flex;flex-direction:column;gap:12px">{"".join(left)}</div><div style="display:flex;flex-direction:column;gap:12px">{"".join(right)}</div></div>'
def sec_wrap(inner): return inner
# ---------- page 1: osie
ax=[('Ekspercka — dostępna','Ekspercka','Dostępna',65,'65% ekspercka / 35% dostępna','Marka powinna znać materiał, montaż i zastosowanie, ale komunikować to prostym językiem.'),
('Formalna — swobodna','Formalna','Swobodna',35,'35% formalna / 65% swobodna','Komunikacja powinna być naturalna i bez dystansu, ale nie potoczna ani żartobliwa.'),
('Spokojna — dynamiczna','Spokojna','Dynamiczna',75,'75% spokojna / 25% dynamiczna','Historia materiału, trwałość i ponadczasowość lepiej współgrają ze spokojnym charakterem niż agresywną sprzedażą.'),
('Tradycyjna — progresywna','Tradycyjna','Progresywna',45,'45% tradycyjna / 55% progresywna','Marka pracuje z historycznym materiałem, ale pokazuje go w nowoczesnym zastosowaniu.'),
('Premium — masowa','Premium','Masowa',65,'65% premium / 35% masowa','Produkt powinien być postrzegany jako autentyczny i wartościowy, ale nie jako elitarny czy niedostępny.')]
P=title('13 · Osobowość marki','Pięć osi osobowości.','Pozycja marki na każdej z pięciu osi.')
for n,l,r,v,pos,why in ax:
    P.append(D(f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="{H}font-size:16px;font-weight:500">{n}</span><span style="{M}letter-spacing:.06em;color:{OR}">{pos}</span></div>'
      f'<div style="margin-top:10px;height:8px;background:{BG};position:relative"><div style="position:absolute;left:0;top:0;bottom:0;width:{v}%;background:{OR}"></div></div>'
      f'<div style="display:flex;justify-content:space-between;margin-top:6px;{M}letter-spacing:.06em;color:#767676"><span>{l}</span><span>{r}</span></div>'
      f'<div style="margin-top:8px;{TXT}">{why}</div>','',642))
write('p017.dc.html',P,17,'Osobowość marki: osie',gap=30)
# ---------- page 2: w praktyce
def section(title_,intro,left_extra,right):
    left=[D(f'<div style="{H}font-size:22px;font-weight:300;letter-spacing:-.02em;line-height:1.15">{title_}</div>')]+left_extra
    return grid2(left,right)
P=title('13 · Osobowość marki','Co to oznacza w praktyce.')
P.append(section('Ekspercka, ale dostępna','',[D(f'<div style="{TXT}">Marka:{ul(["zna właściwości starej cegły,","potrafi doradzić,","wyjaśnia różnice między materiałem autentycznym a imitacją,","edukuje w zakresie montażu i pielęgnacji."])}<div style="margin-top:8px;color:#767676">Ale nie mówimy językiem technicznym tam, gdzie nie jest to konieczne.</div></div>')],
 [card('Tak',NV,'Naturalne różnice kolorystyczne są cechą starej cegły i wynikają z jej pochodzenia.'),card('Nie',OR,'Ze względu na heterogeniczność strukturalną materiału możliwe są odchylenia chromatyczne.')]))
P.append(D('','height:1px;background:'+LN,642))
P.append(section('Swobodna, ale nie potoczna','',[D(f'<div style="{TXT}">Ceglany Renesans nie powinien brzmieć jak duża korporacja.</div>')],
 [card('Unikamy',OR,'Szanowni Państwo, pragniemy zaoferować…'),card('Ale również',OR,'Ta cegła robi robotę.'),card('Mówimy',NV,'Każda partia starej cegły jest trochę inna. I właśnie na tym polega jej charakter.')]))
P.append(D('','height:1px;background:'+LN,642))
P.append(section('Spokojna, nie agresywna','',[D(f'<div style="{TXT}">Marka powinna przede wszystkim <b>pokazywać materiał i pozwalać mu pracować wizualnie</b>.<div style="margin-top:8px;color:#767676">Promocje mogą istnieć, ale nie powinny definiować charakteru komunikacji marki.</div></div>')],
 [card('Mniej',OR,'KUP TERAZ! OSTATNIA SZANSA! −40%'),card('Więcej',NV,'Ponad 100 lat historii. Teraz może stać się częścią Twojego wnętrza.')]))
write('p017b.dc.html',P,17,'Osobowość marki: w praktyce',gap=20)
# ---------- page 3: tradycyjna / premium
P=title('13 · Osobowość marki','Tradycyjna i premium.')
P.append(D(f'<div style="{H}font-size:22px;font-weight:300;letter-spacing:-.02em;line-height:1.15">Tradycyjna w materiale, progresywna w zastosowaniu</div>','',642))
P.append(f'<div style="display:grid;grid-template-columns:313px 313px;gap:16px">'+card('Marka nie jest',OR,'„rustykalną firmą sprzedającą starą cegłę”.')+card('Bardziej',NV,'„współczesną marką pracującą z materiałem historycznym”.')+'</div>')
P.append(D(f'<div style="{TXT}">Dlatego fotografia, strona i komunikacja powinny pokazywać starą cegłę również w:<div style="display:grid;grid-template-columns:313px 313px;gap:16px">{ul(["nowoczesnych kuchniach,","minimalistycznych salonach,","restauracjach,"])}{ul(["nowoczesnych elewacjach,","przestrzeniach komercyjnych."])}</div><div style="margin-top:8px;font-weight:600;color:#000">Nie tylko w stylistyce „stodoła + drewno + retro”.</div></div>','',642))
P.append(D('','height:1px;background:'+LN,642))
P.append(D(f'<div style="{H}font-size:22px;font-weight:300;letter-spacing:-.02em;line-height:1.15">Premium, ale dostępna</div>','',642))
P.append(D(f'<div style="{TXT}">Nie pozycjonujemy <b>Ceglanego Renesansu</b> jako marki luksusowej. Produkt ma natomiast <b>wartość wynikającą z autentyczności materiału</b>.</div>','',642))
P.append(D(f'<div style="{H}font-size:20px;font-weight:300;line-height:1.4;color:#000">premium przez materiał, historię i jakość, <span style="color:{OR}">nie przez snobizm.</span></div>','',642))
P.append(f'<div style="display:grid;grid-template-columns:313px 313px;gap:16px">'+D(lab('Marka może komunikować',NV)+f'<div style="{TXT}">{ul(["unikalność,","jakość,","autentyczność,","ponadczasowość."])}</div>')+D(lab('Ale bez',OR)+f'<div style="{TXT}">{ul(["złota,","„ekskluzywności”,","przesadnego języka luksusu,","sztucznego elitaryzmu."])}</div>')+'</div>')
write('p018.dc.html',P,18,'Osobowość marki: tradycyjna i premium',gap=20)
# ---------- page 4: pięć cech
P=title('13 · Osobowość marki','Podsumowanie osobowości.','Ceglany Renesans w pięciu cechach.')
for i,w in enumerate(['autentyczna','kompetentna','spokojna','świadoma','charakterystyczna']):
    P.append(D(f'<div style="display:flex;align-items:baseline;gap:24px;border-top:1px solid {LN};padding-top:14px"><span style="{M}color:{OR};width:36px">{i+1:02d}</span><span style="{H}font-size:42px;font-weight:300;letter-spacing:-.03em;line-height:1.1">{w}</span></div>','',642))
write('p018b.dc.html',P,18,'Osobowość marki: pięć cech',gap=26)
# ---------- page 19: głos marki
def block2(l,col,t): return D(lab(l,col)+f'<div style="{TXT}margin-top:6px">{t}</div>')
P=[D(f'<div style="{M}letter-spacing:.14em;color:{OR}">13 · Osobowość marki · Głos marki</div><div style="{H}font-size:36px;font-weight:300;letter-spacing:-.03em;line-height:1.1;margin-top:10px">To nie jest imitacja.<br>To prawdziwa historia.</div>','',642),
 D('Klient dostaje fragment rzeczywistego, starego materiału, a nie produkt, który tylko próbuje go naśladować. W tekście to samo co na zdjęciu: konkret zamiast przymiotników.',H+'font-size:14px;line-height:1.5;color:#555;',642),
 D(lab('Tak i nie','#000'),'',642),
 '<div style="display:grid;grid-template-columns:313px 313px;gap:18px 16px;margin-top:-8px">'
  +card('Tak',NV,'Każda partia starej cegły jest trochę inna. I właśnie na tym polega jej charakter.')
  +card('Nie',OR,'Ze względu na heterogeniczność strukturalną materiału możliwe są odchylenia chromatyczne.')
  +card('Tak',NV,'Ponad 100 lat historii. Teraz może stać się częścią Twojego wnętrza.')
  +card('Nie',OR,'KUP TERAZ! OSTATNIA SZANSA! −40%')+'</div>',
 D('','height:1px;background:'+LN,642),
 D(lab('Pięć cech',OR)+f'<div style="{H}font-size:20px;font-weight:300;letter-spacing:-.01em;line-height:1.4;margin-top:6px">autentyczna · kompetentna · spokojna · świadoma · charakterystyczna</div>','',642),
 D('','height:1px;background:'+LN,642),
 '<div style="display:grid;grid-template-columns:313px 313px;gap:20px 16px">'
  +block2('Co',NV,'Głos: ekspercki, ale dostępny. Spokojny, premium przez materiał i historię, nie przez snobizm.')
  +block2('Dlaczego',NV,'Wizualny minimalizm i ton tekstu mają mówić jednym głosem.')
  +block2('Jak stosować',NV,'Nagłówek 3–8 słów, jedna myśl, jedno CTA. Fakty zamiast przymiotników. Domyślnie bez emoji.')
  +block2('Czego unikać',OR,'Języka korporacyjnego i potocznego, wykrzykników, CAPS LOCKA, „WOW”, złota i ekskluzywności.')+'</div>']
write('p019.dc.html',P,19,'Osobowość marki: głos marki',gap=22)
