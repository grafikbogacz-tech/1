import json
SRC='../../live56/project/p024f.dc.html'
S=open(SRC).read()
HEAD0=S[:S.index('<div class="cr pg">')]
TAIL='\n</x-dc>'+S.split('</x-dc>')[1]
M="font-family:'Overpass Mono',monospace;font-size:12px;letter-spacing:.1em;text-transform:uppercase;"
H="font-family:'Hanken Grotesk',sans-serif;"
OR,BK,NV,LN='#ED6842','#000','#0D4C73','#E7DFC9'
def A(x,y,w,h,inner,extra=''):
    hh=f'height:{h}px;' if h else ''
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;{hh}{extra}">{inner}</div>'
def title(lb,h1,su):
    return [A(76,100,300,16,lb,M+f'letter-spacing:.14em;color:{OR}'),
            A(76,118,642,44,h1,H+'font-size:36px;font-weight:300;letter-spacing:-.03em;line-height:1.08;white-space:nowrap'),
            A(76,172,642,44,su,H+'font-size:14px;line-height:1.5;color:#555')]
def page(num,rh,parts,ttl):
    return HEAD0.replace('25 Logo na tle',ttl)+f'<div class="cr pg"><div class="tab">{num}</div><div class="rh"><span>{rh}</span><span>Ceglany Renesans</span></div>'+''.join(parts)+'<div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n'+TAIL
def lab(x,y,t,c='#000'): return A(x,y,313,16,t,M+f'color:{c}')
def para(x,y,w,t,c='#333'): return A(x,y,w,0,t,H+f'font-size:13px;line-height:1.5;color:{c}')
def two(x,y,l,t): return A(x,y,313,60,f'<div style="{M}color:{NV};margin-bottom:6px">{l}</div>{t}',H+'font-size:13px;line-height:1.5;color:#333')
# ---- 1
P=title('Logo','Cztery zatwierdzone wersje.','Księga Znaku 2023. Używamy wyłącznie tych wersji. Nie przerysowujemy logo, nie upraszczamy go i nie odtwarzamy tekstem. Fonty logo są częścią znaku.')
tiles=[('Podstawowa kolor','logo-or.svg','#fff',f'border:1px solid {LN};'),('Negatyw kolor','logo-w.svg',OR,''),('Podstawowa mono','logo-k.svg','#fff',f'border:1px solid {LN};'),('Negatyw mono','logo-w.svg','#1E1E1C','')]
for k,(n,f,bg,b) in enumerate(tiles):
    x=76+(k%2)*329;y=250+(k//2)*270
    P.append(A(x,y,313,220,f'<img src="{f}" alt="{n}" style="width:190px;height:auto;display:block">',f'background:{bg};{b}box-sizing:border-box;display:flex;align-items:center;justify-content:center'))
    P.append(lab(x,y+232,n))
P.append(A(76,812,642,1,'',f'background:{LN}'))
P.append(two(76,836,'Co','Logo i jego cztery wersje zostają dokładnie takie, jak w Księdze Znaku.'))
P.append(two(405,836,'Dlaczego','Księga Znaku ma pierwszeństwo w sprawach logo. Ten Brand Book rozszerza system wokół znaku.'))
open('p030.dc.html','w').write(page('30','Część III · Logo w systemie · 1 / 3',P,'Logo: cztery wersje'))
# ---- 2
BR='#B0603F'
bricks='<div style="position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent 0 30px,rgba(255,255,255,.18) 30px 32px)"></div>'
def ph(w,h,inner): return f'<div style="position:relative;width:{w}px;height:{h}px;background:{BR};overflow:hidden">{bricks}{inner}</div>'
P=title('Logo','Użycie na zdjęciach i w szablonach.','Stałe miejsce logo w szablonach, wersja dobrana do kontrastu tła. Na zdjęciach dyskretnie lub na planszy końcowej.')
ex=[('Dyskretnie','Małe logo w rogu zdjęcia.',f'<img src="logo-w.svg" alt="" style="position:absolute;right:12px;top:12px;width:70px">'),
 ('Na apli','Logo na neutralnej planszy pod zdjęciem.',f'<div style="position:absolute;left:0;right:0;bottom:0;height:56px;background:#fff;display:flex;align-items:center;justify-content:flex-end;padding:0 14px;box-sizing:border-box"><img src="logo-or.svg" alt="" style="width:70px"></div>'),
 ('Bez logo','Zdjęcie jako samodzielny dowód marki.','')]
for k,(t,c,inner) in enumerate(ex):
    x=76+k*221
    P.append(A(x,250,200,0,ph(200,300,inner)+f'<div style="{M}color:#000;margin-top:12px">{t}</div><div style="{H}font-size:12.5px;line-height:1.45;color:#555;margin-top:4px">{c}</div>'))
P.append(A(76,660,642,1,'',f'background:{LN}'))
P.append(A(76,684,642,0,f'<div style="{M}color:{OR};margin-bottom:6px">Czego unikać</div>Dużego logo na produkcie, logo na każdym zdjęciu, nowego monogramu „CR” bez decyzji brandingowej.',H+'font-size:13px;line-height:1.5;color:#333'))
open('p030b.dc.html','w').write(page('30','Część III · Logo w systemie · 2 / 3',P,'Logo: użycie na zdjęciach i w szablonach'))
# ---- 3
P=title('Logo','Nieprawidłowe używanie znaku.','Logo zawsze zostaje takie, jak w Księdze Znaku.')
IM={'tl':'/_blob/15cee9b071ce1d40bd355d9699ab5bc6','tr':'/_blob/66f760d9749390ffebc00c7ae5eb321f','bl':'/_blob/7206acd3dd38e6314ee5874c4ccefd3b','br':'/_blob/cd520968d10f637a3f02b1ecf0bc22b5'}
import sys
if len(sys.argv)>1: IM={k:f'bl-{k}.png' for k in IM}
def img(x,y,k): return A(x,y,313,210,f'<img src="{IM[k]}" alt="" style="width:313px;height:210px;display:block;object-fit:cover">','')
P+=[img(76,250,'tl'),img(405,250,'tr')]
P.append(A(76,472,642,0,'Zbyt niski kontrast pomiędzy znakiem a tłem.',M+'color:#000'))
P+=[img(76,540,'bl'),img(405,540,'br')]
P.append(A(76,762,313,0,'Brak zachowania obszaru ochronnego.',M+'color:#000;line-height:1.5'))
P.append(A(405,762,313,0,'Zmiana w obrębie logo, w którymkolwiek elemencie, dodawanie cienia.',M+'color:#000;line-height:1.5'))
open('p030c.dc.html','w').write(page('30','Część III · Logo w systemie · 3 / 3',P,'Logo: błędne użycie'))
c=json.load(open('canvas.json'));o=c['order'];B=c['boards']
i=o.index('p030.dc.html')
for k,f in enumerate(['p030b.dc.html','p030c.dc.html']):
    if f not in o: o.insert(i+1+k,f)
    B[f]={'h':1123,'w':794,'title':{'p030b.dc.html':'Logo użycie na zdjęciach','p030c.dc.html':'Logo błędne użycie'}[f],'x':0,'y':0}
g=[f for f in o if f!='part-i-propozycja.dc.html']
for n,f in enumerate(g): B[f]['x']=(n%6)*874;B[f]['y']=(n//6)*1243
json.dump(c,open('canvas.json','w'),ensure_ascii=False)
