import json
SRC='../../live56/project/p024f.dc.html'
S=open(SRC).read()
HEAD0=S[:S.index('<div class="cr pg">')]
TAIL='\n</x-dc>'+S.split('</x-dc>')[1]
M="font-family:'Overpass Mono',monospace;font-size:12px;letter-spacing:.1em;text-transform:uppercase;"
H="font-family:'Hanken Grotesk',sans-serif;"
OR,BK,NV,BG,PK,LN='#ED6842','#000','#0D4C73','#EDE9D0','#EA4D70','#E7DFC9'
def A(x,y,w,h,inner,extra=''):
    hh=f'height:{h}px;' if h else ''
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;{hh}{extra}">{inner}</div>'
def ul(items,c='#333'): return f'<ul style="margin:6px 0 0;padding-left:16px">'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'
def title(lb,h1,su):
    return [A(76,100,300,16,lb,M+f'letter-spacing:.14em;color:{OR}'),
            A(76,118,642,44,h1,H+'font-size:36px;font-weight:300;letter-spacing:-.03em;line-height:1.08;white-space:nowrap'),
            A(76,172,642,44,su,H+'font-size:14px;line-height:1.5;color:#555')]
def page(num,rh,parts,ttl):
    return HEAD0.replace('25 Logo na tle',ttl)+f'<div class="cr pg"><div class="tab">{num}</div><div class="rh"><span>{rh}</span><span>Ceglany Renesans</span></div>'+''.join(parts)+'<div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n'+TAIL
# ---------- page A (35)
P=title('Kolory','Kolor wspiera produkt.','Cel: produkt — jego kolor, struktura i fotografia — ma pozostać głównym elementem wizualnym. Identyfikacja ma wspierać zdjęcie cegły, a nie z nim konkurować.')
def tag(x,y,t,main):
    st=f'background:{OR};border:1px solid {OR};' if main else f'border:1px solid {BK};'
    return A(x,y,0,0,f'<span style="{M}letter-spacing:.1em;color:#000;{st}padding:2px 8px;white-space:nowrap">{t}</span>')
def card(x,y,name,col,label,items,bd=False,w=313,hh=150):
    b=f'border:1px solid {LN};' if bd else ''
    r=[A(x,y,40,40,'',f'background:{col};{b}border-radius:2px'),
       A(x+56,y+4,200,24,name,H+'font-size:18px;font-weight:500;line-height:1.1'),
       A(x,y+56,w,hh-56,f'<div style="{M}color:{NV}">{label}</div>'+ul(items),H+'font-size:12.5px;line-height:1.45;color:#333')]
    return r
# terakota wide
P+=card(76,250,'Terakota',OR,'Stosować:',['CTA i elementy akcentowe,','aktywne stany,','krótkie wyróżnienia,','znaczniki,','linie i detale,','wybrane nagłówki,','elementy identyfikujące markę.'],w=240,hh=200)
P.append(tag(262,254,'Kolor główny',True))
P.append(A(400,306,300,150,f'<div style="{M}color:{OR}">Nie stosować:</div>'+ul(['jako dominujące tło większości strony,','do długich bloków tekstu,','jako filtr nakładany na zdjęcia produktu,','jednocześnie z wieloma innymi mocnymi kolorami.']),H+'font-size:12.5px;line-height:1.45;color:#333'))
P.append(A(76,468,642,1,'',f'background:{LN}'))
rows=[('Biel','#FFFFFF','Stosować jako:',['podstawowe tło,','przestrzeń oddechu,','tło dla zdjęć,','neutralne pole dla treści.']),
('Czerń',BK,'Stosować jako:',['podstawowy kolor tekstu,','nagłówki,','elementy nawigacji,','elementy o wysokim kontraście.']),
('Beż',BG,'Stosować jako:',['spokojne tło sekcji,','tło karuzel edukacyjnych,','pole dla informacji technicznych,','subtelne rozdzielenie treści.']),
('Granat',NV,'Stosować oszczędnie:',['jako ciemny kontrapunkt dla pomarańczu,','dla nagłówków lub sekcji wymagających wyraźnego kontrastu,','w materiałach informacyjnych i bardziej technicznych.']),
('Róż',PK,'Stosować wyjątkowo:',['jako akcent wtórny,','do pojedynczych elementów pomocniczych,','tylko wtedy, gdy nie konkuruje z #ED6842.'])]
for i,(n,c,l,it) in enumerate(rows):
    x=76+(i%2)*329; y=488+(i//2)*172
    P+=card(x,y,n,c,l,it,bd=(n=='Biel'))
pgA=page('35','Część III · Kolory w praktyce',P,'Propozycja 35 Kolor wspiera produkt')
open('p035v.dc.html','w').write(pgA)
# ---------- page B (36)
P=title('Kolory','CTA i kontrast.','Preferowany kierunek dla przycisków oraz minimalny kontrast zgodny ze standardem WCAG AA.')
P.append(A(76,244,400,16,'CTA · preferowany kierunek',M+'color:#000'))
btn=lambda x,t,bg,fg,bd: A(x,272,200,48,t,H+f'font-size:15px;font-weight:600;display:flex;align-items:center;justify-content:center;box-sizing:border-box;background:{bg};color:{fg};{bd}')
P+=[btn(76,'Zamów próbki',OR,'#000',''),btn(297,'Pobierz katalog PDF',NV,'#fff',''),btn(518,'Zobacz realizacje','#fff','#000',f'border:1.5px solid {OR};')]
for x,t in [(76,'pomarańczowe tło #ED6842 + czarny tekst'),(297,'granatowe tło #0D4C73 + biały tekst'),(518,'białe tło + czarny tekst + pomarańczowy akcent / obrys')]:
    P.append(A(x,330,196,40,t,H+'font-size:12px;line-height:1.35;color:#767676'))
P.append(A(76,384,642,36,f'<span style="{M}color:{OR};margin-right:8px">Unikaj</span>Białego tekstu na #ED6842 dla typowego małego tekstu przycisku. Kontrast jest zbyt niski dla standardu WCAG AA.',H+'font-size:12.5px;line-height:1.5;color:#333'))
P.append(A(76,438,642,1,'',f'background:{LN}'))
P.append(A(76,452,500,16,'Kontrast i dostępność · WCAG — minimalny kontrast',M+'color:#000'))
for k,(n,t) in enumerate([('4,5:1','zwykły tekst'),('3:1','duży tekst'),('3:1','elementy interfejsu i grafiki funkcjonalne')]):
    P.append(A(76+k*216,478,200,70,f'<div style="font-size:32px;font-weight:300;letter-spacing:-.02em;line-height:1">{n}</div><div style="font-size:12px;line-height:1.35;color:#767676;margin-top:6px">{t}</div>',H))
pairs=[(NV,'#FFF','9,14:1','AAA, bardzo dobry kontrast',0),(BK,BG,'17,17:1','AAA, bardzo dobry kontrast',0),(BK,OR,'6,66:1','AA dla zwykłego tekstu',0),(BK,PK,'5,79:1','AA dla zwykłego tekstu',0),
 (OR,'#FFF','3,15:1','nie spełnia AA; tylko duży tekst lub elementy dekoracyjne',1),(PK,'#FFF','3,62:1','nie spełnia AA; dopuszczalny dla dużego tekstu',1),(BG,'#FFF','1,22:1','nie używać jako zestawienia tekst–tło',1),(BK,NV,'2,30:1','nie używać dla tekstu',1)]
# table
th=lambda t,w='':f'<th style="{w}">{t}</th>'
trs=''
names={NV:'#0D4C73',BK:'#000000',BG:'#EDE9D0',OR:'#ED6842',PK:'#EA4D70','#FFF':'#FFFFFF'}
for fg,bg,r,t,bad in pairs:
    fgc=fg if fg!=BK or True else fg
    chip=f'<span style="display:inline-flex;align-items:center;justify-content:center;width:44px;height:24px;background:{bg};color:{fg};border:1px solid {LN};font-weight:600;font-size:12px">Aa</span>'
    # chip text color = foreground; for dark pair fg=black on navy
    trs+=f'<tr><td style="width:52px">{chip}</td><td style="white-space:nowrap">{names[fg]} na {names[bg]}</td><td style="width:70px;font-family:\'Overpass Mono\',monospace;font-size:12px">{r}</td><td style="color:{OR if bad else "#333"}">{t}</td></tr>'
tbl=(f'<table style="width:642px;border-collapse:collapse;border:1px solid {LN};font-size:12.5px;line-height:1.35;{H}">'
 f'<tr style="border-bottom:2px solid {OR}"><th style="text-align:left;font-weight:400;color:{NV};font-size:13px;padding:10px 12px;border-right:1px solid {LN}" colspan="2">Sprawdzone zestawienia</th><th style="text-align:left;font-weight:400;color:{NV};font-size:13px;padding:10px 12px;border-right:1px solid {LN}">Kontrast</th><th style="text-align:left;font-weight:400;color:{NV};font-size:13px;padding:10px 12px">Ocena</th></tr>'
 +trs+'</table>')
css=f'<style>.k2 td{{border-bottom:1px solid {LN};border-right:1px solid {LN};padding:6px 12px;vertical-align:middle}}.k2 tr:last-child td{{border-bottom:0}}.k2 td:last-child{{border-right:0}}</style>'
P.append(A(76,566,642,0,css+'<div class="k2">'+tbl+'</div>'))
pgB=page('36','Część III · CTA i kontrast',P,'Propozycja 36 CTA i kontrast')
open('p036v.dc.html','w').write(pgB)
# ---------- page C (37)
P=title('Kolory','Kolor nie zmienia cegły.','Kolorystyka marki nie może zmieniać realnego wyglądu cegły na zdjęciu.')
P.append(A(76,244,400,16,'Zasada dla zdjęć · nie stosować',M+'color:#000'))
BR='#B0603F'
def ph(inner,extra=''): return f'<div style="position:relative;width:150px;height:104px;background:{BR};overflow:hidden;{extra}">{inner}</div>'
bricks='<div style="position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent 0 24px,rgba(255,255,255,.18) 24px 26px)"></div>'
def mark(c): return f'<span style="position:absolute;top:6px;left:8px;font-size:13px;font-weight:700;color:#fff;z-index:2">✗</span>'
tiles=[('mocne filtry',ph(bricks+f'<div style="position:absolute;inset:0;filter:saturate(3)"></div>'+mark(''),'filter:saturate(2.6) contrast(1.2)')),
 ('tinty zmieniające kolor materiału',ph(bricks+f'<div style="position:absolute;inset:0;background:{NV};opacity:.45"></div>'+mark(''))),
 ('duże kolorowe nakładki na zdjęcia realizacji',ph(bricks+f'<div style="position:absolute;left:0;right:0;top:34px;height:44px;background:{PK};opacity:.9"></div>'+mark(''))),
 ('gradienty, które utrudniają ocenę produktu',ph(bricks+f'<div style="position:absolute;inset:0;background:linear-gradient(135deg,{NV},{PK})"></div><div style="position:absolute;inset:0;background:linear-gradient(135deg,rgba(13,76,115,.8),rgba(234,77,112,.8))"></div>'+mark('')))]
for k,(t,h) in enumerate(tiles):
    x=76+k*164
    P.append(A(x,272,150,150,h+f'<div style="font-size:12px;line-height:1.35;color:#333;margin-top:8px;{H}">{t}</div>'))
P.append(A(76,448,642,1,'',f'background:{LN}'))
P.append(A(76,462,642,16,'Jeżeli tekst musi pojawić się na zdjęciu',M+'color:#000'))
ok=[('odpowiedni dobór jasnej lub ciemnej wersji tekstu',f'<span style="position:absolute;left:10px;bottom:10px;color:#fff;font-weight:600;font-size:14px;{H}">Cegła z historią</span>'),
 ('neutralna apla',f'<div style="position:absolute;left:0;right:0;bottom:0;height:40px;background:#fff"></div><span style="position:absolute;left:10px;bottom:12px;color:#000;font-weight:600;font-size:14px;{H}">Cegła z historią</span>'),
 ('przyciemnienie fragmentu tła',f'<div style="position:absolute;left:0;right:0;bottom:0;height:56px;background:linear-gradient(to top,rgba(0,0,0,.55),rgba(0,0,0,0))"></div><span style="position:absolute;left:10px;bottom:12px;color:#fff;font-weight:600;font-size:14px;{H}">Cegła z historią</span>')]
for k,(t,inner) in enumerate(ok):
    x=76+k*214
    P.append(A(x,490,200,150,f'<div style="position:relative;width:200px;height:112px;background:{BR};overflow:hidden">{bricks}{inner}<span style="position:absolute;top:6px;left:8px;font-size:13px;font-weight:700;color:#fff;z-index:2">✓</span></div><div style="font-size:12px;line-height:1.35;color:#333;margin-top:8px;{H}">{t}</div>'))
P.append(A(76,654,642,36,'Zamiast dodawania przypadkowych cieni i obrysów.',H+'font-size:13px;color:#555'))
P.append(A(76,860,642,140,f'<div style="border-top:1px solid #000;padding-top:16px"><div style="{M}color:{OR}">Zasada nadrzędna</div><p style="font-size:20px;font-weight:300;line-height:1.4;margin:10px 0 0">Kolor firmowy ma identyfikować markę, nie dominować nad produktem. Najważniejszym „kolorem” komunikacji Ceglanego Renesansu pozostaje <span style="color:{OR}">rzeczywisty kolor i struktura starej cegły.</span></p></div>',H))
pgC=page('37','Część III · Zasady stosowania kolorów',P,'Propozycja 37 Kolor nie zmienia cegły')
open('p037v.dc.html','w').write(pgC)
# canvas
c=json.load(open('canvas.json'));o=c['order'];B=c['boards']
last=o.index('p037.dc.html')
for k,f in enumerate(['p037v.dc.html','p036v.dc.html','p035v.dc.html']):
    if f not in o: o.insert(last+1,f)
    B[f]={'h':1123,'w':794,'title':{'p035v.dc.html':'Propozycja 35 Kolor wspiera produkt','p036v.dc.html':'Propozycja 36 CTA i kontrast','p037v.dc.html':'Propozycja 37 Kolor nie zmienia cegły'}[f],'x':0,'y':0}
g=[f for f in o if f!='part-i-propozycja.dc.html']
for n,f in enumerate(g): B[f]['x']=(n%6)*874;B[f]['y']=(n//6)*1243
json.dump(c,open('canvas.json','w'),ensure_ascii=False)
