import json
SRC='../../live56/project/p024f.dc.html'
S=open(SRC).read()
HEAD=S[:S.index('<div class="cr pg">')].replace('25 Logo na tle','Typografia: kroje')
TAIL='\n</x-dc>'+S.split('</x-dc>')[1]
M="font-family:'Overpass Mono',monospace;letter-spacing:.14em;text-transform:uppercase;font-size:12px;"
H="font-family:'Hanken Grotesk',sans-serif;"
OR,LN='#ED6842','#E7DFC9'
BLOB='/_blob/55fed68ad47a94d65019ee8aa4def2a9'
import sys
if len(sys.argv)>1: BLOB='spec-raw.png'
def A(x,y,w,h,inner,extra=''): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}">{inner}</div>'
P=[]
P.append(A(76,100,642,16,'Typografia',M+f'color:{OR}'))
P.append(A(76,122,642,92,'Litera buduje<br>charakter.',H+'font-size:42px;font-weight:300;letter-spacing:-.03em;line-height:1.08'))
P.append(A(76,228,540,66,'System typograficzny łączy charakter, czytelność i historyczny kontekst marki, a jednocześnie wspiera komunikację, pozostając subtelny, aby nie konkurować z materiałem.',H+'font-size:14px;font-weight:300;line-height:1.5;color:#555'))
def head(y,n,t):
    P.append(A(76,y,642,1,'',f'background:{LN}'))
    P.append(A(76,y+16,40,16,n,M+f'color:{OR};font-weight:700'))
    P.append(A(112,y+16,500,16,t,M+'color:#000;letter-spacing:.12em'))
# 01
head(334,'01','Krój podstawowy logo i kluczowej jego części.')
P.append(A(76,388,300,100,f'<img src="{BLOB}" alt="Boulevard Saint Denis" style="width:300px;height:auto;display:block;mix-blend-mode:multiply">',''))
P.append(A(404,380,1,120,'',f'background:{LN}'))
P.append(A(430,390,288,110,'<svg viewBox="262.04 191.62 358.18 141.4" width="288" height="113" xmlns="http://www.w3.org/2000/svg"><image href="logo-or.svg" x="262.04" y="191.62" width="358.18" height="173.21"/></svg>','overflow:hidden'))
# 02
head(584,'02','Krój indeksu logo')
P.append(A(76,640,300,110,f'<div style="font-family:Montserrat,sans-serif;font-weight:700;font-size:22px;color:#000;line-height:1.1;margin-bottom:12px">Montserrat Bold</div><div style="font-family:Montserrat,sans-serif;font-weight:700;font-size:13px;line-height:1.55;color:#000">abcdefghijklmnopqrstuwwxyz<br>ABCDEFGHIJKLMNOPQRSTUWVXXYZ</div>',''))
P.append(A(404,632,1,100,'',f'background:{LN}'))
P.append(A(430,668,288,40,'<svg viewBox="262.04 336 358.18 28.83" width="288" height="23.2" xmlns="http://www.w3.org/2000/svg"><image href="logo-or.svg" x="262.04" y="191.62" width="358.18" height="173.21"/></svg>','overflow:hidden'))
# 03
head(834,'03','Krój dopełniający')
for k,(name,w) in enumerate([('Overpass Mono Light',300),('Overpass Mono Medium',500),('Overpass Mono Bold',700)]):
    x=76+k*216
    P.append(A(x,888,200,100,f"<div style=\"font-family:'Overpass Mono',monospace;font-weight:{w};font-size:16px;color:#000;margin-bottom:14px\">{name}</div><div style=\"font-family:'Overpass Mono',monospace;font-weight:{w};font-size:12px;line-height:1.55;color:#222\">abcdefghijklmnopqrstuvwxyz<br>ABCDEFGHIJKLMNOPQRSTUVWXYZ</div>",''))
    if k: P.append(A(x-12,880,1,110,'',f'background:{LN}'))
body=('<div class="cr pg"><div class="tab">53</div><div class="rh"><span>Część III · 31 Typografia: kroje</span><span>Ceglany Renesans</span></div>'+''.join(P)+'<div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n')
open('p038b.dc.html','w').write(HEAD+body+TAIL)
c=json.load(open('canvas.json'));o=c['order'];B=c['boards']
if 'p038b.dc.html' not in o: o.insert(o.index('p039.dc.html'),'p038b.dc.html')
B['p038b.dc.html']={'h':1123,'w':794,'title':'Typografia: kroje','x':0,'y':0}
g=[f for f in o if f!='part-i-propozycja.dc.html']
for n,f in enumerate(g): B[f]['x']=(n%6)*874;B[f]['y']=(n//6)*1243
json.dump(c,open('canvas.json','w'),ensure_ascii=False)
