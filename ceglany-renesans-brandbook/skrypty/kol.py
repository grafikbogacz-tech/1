import os
D='live36/project/'
HEAD='<!doctype html><html lang="pl"><head><meta charset="utf-8"><title>%s</title><script src="./support.js"></script><link rel="stylesheet" href="brand.css"></head><body><x-dc><helmet><link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300;400;500;600;700&family=Montserrat:wght@700&family=Overpass+Mono:wght@300;500;700&display=swap" rel="stylesheet"><style>body{margin:0}%s</style></helmet>\n'
TAIL='\n</x-dc><script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":794,"height":1123}}\'>class Component extends DCLogic{renderVals(){return {};}}</script></body></html>\n'
CSS='''.k .lb{font-family:"Overpass Mono",monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#ED6842;font-weight:500}
.k h1{font-size:42px;font-weight:300;letter-spacing:-.03em;line-height:1.08;margin:12px 0 10px}
.k h3{font-size:24px;font-weight:300;letter-spacing:-.02em;margin:0 0 6px}
.k .su{font-size:14px;line-height:1.5;color:#555;margin:0}
.k .mono{font-size:12px}'''
def page(n,title,rh,body,css=CSS):
    return HEAD%(title,css)+'<div class="cr pg"><div class="tab">%s</div><div class="rh"><span>%s</span><span>Ceglany Renesans</span></div><div class="bd tx"><div class="k" style="height:100%%;display:flex;flex-direction:column">%s</div></div><div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>'%(n,rh,body)+TAIL
C=[('Terakota','#ED6842','237 · 105 · 66'),('Czerń','#000000','0 · 0 · 0'),('Biel','#FFFFFF','255 · 255 · 255'),('Beż','#EDE9D0','237 · 233 · 209'),('Granat','#0D4C73','13 · 76 · 115'),('Róż','#EA4D70','234 · 77 · 112')]
def sw(h,b): return 'background:%s;%s'%(h,'border:1px solid #E7DFC9;' if h=='#FFFFFF' else '')
# page 1
sws=''.join('<div><div style="height:96px;%s"></div><div style="font-size:14px;font-weight:500;margin-top:8px">%s</div></div>'%(sw(h,0),n) for n,h,r in C)
P=[('Biel','#FFFFFF','40%','#000'),('Beż','#EDE9D0','25%','#000'),('Czerń','#000000','15%','#fff'),('Granat','#0D4C73','10%','#fff'),('Terakota','#ED6842','7%','#000'),('Róż','#EA4D70','3%','#000')]
pr=''.join('<div style="%spadding:14px 12px;height:175px;display:flex;flex-direction:column;justify-content:space-between;color:%s"><div style="font-size:13px;font-weight:500">%s</div><div><div style="font-size:30px;font-weight:300;letter-spacing:-.02em">%s</div><div class="mono">%s</div></div></div>'%(sw(h,0),c,n,p,h) for n,h,p,c in P)
b1='''<div class="lb">Kolory</div><h1>Sześć kolorów.<br/>Jedna cegła.</h1><p class="su">Paleta ma rozpoznawać markę – i zostawić scenę prawdziwej, starej cegle.</p>
<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin:44px 0 64px">%s</div>
<h3>Proporcje to hierarchia.</h3><p class="su">Wielkość pola odpowiada ilości koloru w materiale.</p>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:28px">%s</div>'''%(sws,pr)
# page 2
R=[('Kolor główny – tylko jako akcent.','Numer sekcji, linia, znacznik, CTA, podpis.','Pełnych teł i małego białego tekstu (3,15:1).','Aa','Tekst czarny · 6,7:1','#000'),
('Typografia i cienkie linie. Porządek bez ciężaru.','Nagłówki, tekst, linie 1 px, nawigacja.','Czarnych teł całych materiałów i grubych ramek.','Aa','Tekst biały · 21:1','#fff'),
('Główne tło i przestrzeń. Oddech dla faktury cegły.','60–70% powierzchni razem z beżem.','Wypełniania pustki ozdobnikami.','Aa','Tekst czarny · 21:1','#000'),
('Neutralne, naturalne tło. Ciepło zgodne z materiałem.','Pasy sekcji, karuzele edukacyjne, informacje techniczne.','Beżu jako koloru tekstu (1,22:1 na bieli).','Aa','Tekst czarny · 17,2:1','#000'),
('Kontrastowy akcent. Chłodny kontrapunkt dla cegły.','Nagłówki, dane, tło sekcji, przycisk z białym tekstem.','Granatu na czerni (2,30:1), dużych ciemnych teł.','Aa','Tekst biały · 9,1:1','#fff'),
('Akcent wtórny. Ożywia – w małej dawce.','Pojedynczy detal: plakietka, oznaczenie serii.','Jednego widoku z terakotą i granatem.','Aa','Tekst czarny · 5,8:1','#000')]
cards=''
for i,((n,h,r),(lead,jak,un,aa,ct,tc)) in enumerate(zip(C,R)):
    cards+='''<div style="border:1px solid #E7DFC9;padding:14px 16px;display:flex;flex-direction:column"><div style="display:flex;gap:12px;align-items:center"><div style="width:44px;height:44px;flex:none;%s"></div><div><div style="font-size:17px;font-weight:500;line-height:1.1"><span class="mono" style="color:#ED6842;margin-right:6px">0%d</span>%s</div><div class="mono" style="color:#555;margin-top:3px">%s · %s</div></div></div>
<div style="font-size:13px;font-weight:500;line-height:1.4;margin:10px 0 8px">%s</div>
<div style="font-size:12.5px;line-height:1.4;color:#333"><div><span class="mono" style="color:#0D4C73;margin-right:6px">Jak</span>%s</div><div style="margin-top:5px"><span class="mono" style="color:#ED6842;margin-right:6px">Unikaj</span>%s</div></div>
<div style="margin-top:auto;padding-top:10px"><span style="display:inline-flex;align-items:center;gap:8px;font-size:12px;border:1px solid #E7DFC9;padding:3px 8px 3px 3px"><span style="%scolor:%s;width:30px;height:22px;display:inline-flex;align-items:center;justify-content:center;font-weight:500">%s</span>%s</span></div></div>'''%(sw(h,0),i+1,n,h,r,lead,jak,un,sw(h,0),tc,aa,ct)
b2='''<div class="lb">Kolory</div><h1 style="font-size:36px">Każdy kolor ma swoją rolę.</h1><p class="su">Co oznacza, jak go używać i czego unikać.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:12px;margin-top:22px;flex:1">%s</div>'''%cards
# page 3
def tile(bg,inner,border=False):
    return '<div style="height:235px;background:%s;%sdisplay:flex;align-items:center;justify-content:center;position:relative">%s</div>'%(bg,'border:1px solid #E7DFC9;' if border else '',inner)
def mk(t,sym,col): return '<div style="position:relative">%s<span style="position:absolute;top:8px;left:10px;font-size:13px;font-weight:700;color:%s">%s</span></div>'%(t,col,sym)
caps=['Terakota to akcent z czarnym tekstem – nie tło.','Biel na granacie: 9,1:1. Granat na czerni: 2,3:1.','Róż pojedynczo. Nigdy obok terakoty i granatu.']
oks=[(tile('#fff','<span style="background:#ED6842;color:#000;font-size:13px;font-weight:500;padding:9px 16px">Zobacz kolekcję</span>',True),'#0D4C73'),
(tile('#0D4C73','<span style="color:#fff;font-size:15px;font-weight:500">Dane techniczne</span>'),'#fff'),
(tile('#EDE9D0','<span style="background:#EA4D70;color:#000;font-family:\'Overpass Mono\',monospace;font-size:12px;letter-spacing:.1em;padding:5px 10px">SERIA</span>'),'#0D4C73')]
nos=[(tile('#ED6842','<span style="color:#fff;font-size:12px">drobny biały tekst na pełnym tle</span>'),'#fff'),
(tile('#000','<span style="color:#0D4C73;font-size:15px;font-weight:500">Dane techniczne</span>'),'#EA4D70'),
(tile('#fff','<div style="display:flex;gap:8px"><div style="width:34px;height:34px;background:#ED6842"></div><div style="width:34px;height:34px;background:#0D4C73"></div><div style="width:34px;height:34px;background:#EA4D70"></div></div>',True),'#ED6842')]
cols=''.join('<div style="display:flex;flex-direction:column;gap:12px">%s%s<div style="font-size:12.5px;line-height:1.4">%s</div></div>'%(mk(o[0],'✓ Tak',o[1]),mk(n[0],'✗ Nie',n[1]),c) for o,n,c in zip(oks,nos,caps))
b3='''<div class="lb">Kolory</div><h1>Tak. I nie.</h1><p class="su">Trzy sytuacje, które zdarzają się najczęściej.</p>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:36px">%s</div>
<div style="margin-top:auto;border-top:1px solid #000;padding-top:16px"><div class="mono" style="color:#ED6842">Zasada nadrzędna</div><p style="font-size:18px;font-weight:300;line-height:1.4;margin:8px 0 0">Kolor identyfikuje markę, nie dominuje nad produktem. Najważniejszym kolorem pozostaje <span style="color:#ED6842">prawdziwa stara cegła.</span></p></div>'''%cols
open(D+'p032.dc.html','w').write(page('32','Strona 32 Kolory','Kolory · 1 / 3',b1))
open(D+'p033.dc.html','w').write(page('33','Strona 33 Kolory role','Kolory · 2 / 3',b2))
open(D+'p033b.dc.html','w').write(page('33','Strona 33b Kolory tak i nie','Kolory · 3 / 3',b3))
