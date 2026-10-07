import json
SRC='../../live56/project/p024f.dc.html'
HEAD=open(SRC).read()
HEAD=HEAD[:HEAD.index('<div class="cr pg">')].replace('25 Logo na tle','Elementy graficzne: detale')
TAIL='\n</x-dc>'+open(SRC).read().split('</x-dc>')[1]
M="font-family:'Overpass Mono',monospace;font-size:12px;letter-spacing:.2em;text-transform:uppercase;"
H="font-family:'Hanken Grotesk',sans-serif;"
OR,BK,NV,BG,LN='#ED6842','#000','#0D4C73','#EDE9D0','#E7DFC9'
def A(x,y,w,h,inner,extra=''): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}">{inner}</div>'
def lab(x,y,t): return A(x,y,300,16,t,M+'color:#000')
def cap(t,b): return f'<div style="{H}font-size:12px;line-height:1.35;color:#767676;margin-top:8px">{t}<br>{b}</div>'
def hr(y): return A(76,y,642,1,'', f'background:{LN}')
P=[]
P.append(A(76,100,642,16,'Elementy graficzne',M+f'color:{OR};letter-spacing:.14em'))
P.append(A(76,122,642,90,'Detal, który<br>porządkuje całość.',H+'font-size:40px;font-weight:300;letter-spacing:-.03em;line-height:1.08'))
P.append(A(76,224,520,48,'System drobnych form wspiera komunikację, buduje rytm i porządkuje treść. Pozostaje subtelny, aby nie konkurować z materiałem.',H+'font-size:14px;line-height:1.5;color:#555'))
P.append(hr(292))
P.append(lab(76,308,'Linie i separatory'))
def line(y,svg): return f'<svg style="position:absolute;left:0;top:{y}px" width="300" height="12" viewBox="0 0 300 12">{svg}</svg>'
ls=(line(0,f'<path d="M0 6H300" stroke="{BK}"/>')+line(18,f'<path d="M0 6H300" stroke="{OR}"/>')+line(36,f'<path d="M0 6H300" stroke="{LN}" stroke-width="2"/>')
 +line(54,f'<path d="M0 6H300" stroke="{NV}"/>')+line(72,f'<path d="M0 6H300" stroke="{BK}" stroke-dasharray="5 4"/>')
 +line(90,f'<path d="M0 6H298M292 1l6 5-6 5" stroke="{BK}" fill="none"/>')+line(108,f'<path d="M0 6H290" stroke="{LN}"/><rect x="292" y="2" width="8" height="8" fill="{OR}"/>'))
P.append(A(76,336,300,124,ls,''))
P.append(A(404,300,1,170,'',f'background:{LN}'))
P.append(lab(430,308,'Etykiety'))
def tag(x,y,t,st): return A(x,y,138,38,t,M+f'letter-spacing:.18em;display:flex;align-items:center;justify-content:center;box-sizing:border-box;{st}')
P+= [tag(430,336,'Kolekcja',f'background:{OR};color:#000'),tag(580,336,'Realizacje',f'border:1px solid {BK};color:#000'),
     tag(430,392,'Technika',f'background:{NV};color:#fff'),tag(580,392,'Poradnik',f'border:1px solid {LN};color:#000')]
P.append(hr(484))
P.append(lab(76,500,'Numeracja'))
for k,(n,col) in enumerate([('01',OR),('02',BK),('03','#D3CFB8'),('04',NV)]):
    P.append(A(76+k*66,524,64,70,f'{n}<div style="width:28px;height:2px;background:{col};margin-top:8px"></div>',f"font-family:'Overpass Mono',monospace;font-weight:300;font-size:40px;line-height:1;color:{col}"))
P.append(A(344,492,1,128,'',f'background:{LN}'))
P.append(lab(366,500,'Ramki i pola'))
P.append(A(366,524,78,52,'',f'border:1px solid {BK};box-sizing:border-box'))
P.append(A(452,524,78,52,'',f'background:{BG}'))
P.append(A(538,524,78,52,f'<svg width="78" height="52" viewBox="0 0 78 52" fill="none" stroke="{OR}" stroke-width="1.5"><path d="M10 1H1V51H10M68 1H77V51H68"/></svg>',''))
P.append(A(624,524,78,52,'Produkt<br>w centrum',M+f'letter-spacing:.04em;line-height:1.3;background:{OR};color:#000;display:flex;align-items:center;justify-content:center;text-align:center;box-sizing:border-box'))
for x,(a,b) in zip([366,452,538,624],[('Cienka ramka','informacyjna'),('Pole','wyróżniające'),('Ramka otwarta','na zdjęcie'),('Pole akcentu','z tekstem')]):
    P.append(A(x,582,84,40,cap(a,b).replace('margin-top:8px','margin-top:0'),''))
P.append(hr(638))
P.append(lab(76,654,'Kąty i detal'))
items=[('Narożnik','liniowy',f'<svg width="70" height="58" viewBox="0 0 70 58" fill="none" stroke="{OR}" stroke-width="1.5"><path d="M2 56V2H68"/></svg>'),
 ('Ćwiartka koła','miękki detal',f'<svg width="70" height="58" viewBox="0 0 70 58"><path d="M2 56V2A54 54 0 0 1 56 56Z" fill="{BG}"/></svg>'),
 ('Prostokąt','akcentowy',f'<svg width="70" height="58" viewBox="0 0 70 58"><rect x="0" y="6" width="70" height="46" fill="{NV}"/></svg>'),
 ('Siatka punktów','rytm i porządek',f'<svg width="70" height="58" viewBox="0 0 70 58" fill="{OR}">'+''.join(f'<circle cx="{10+22*i}" cy="{8+20*j}" r="2.5"/>' for i in range(3) for j in range(3))+'</svg>'),
 ('Znak plus','dodatkowy akcent',f'<svg width="70" height="58" viewBox="0 0 70 58" fill="none" stroke="{BK}" stroke-width="1.5"><path d="M35 2V56M8 29H62"/></svg>')]
for k,(a,b,svg) in enumerate(items):
    P.append(A(76+k*130,682,120,100,svg+cap(a,b),''))
P.append(hr(802))
P.append(lab(76,818,'Wzory pomocnicze'))
cols=''.join(f'<path d="M{i*24+1} 0V86" stroke="{LN}"/>' for i in range(9))+f'<path d="M73 0V86" stroke="{OR}"/>'
P.append(A(76,846,190,130,f'<svg width="190" height="86" viewBox="0 0 190 86">{cols}</svg>'+cap('Moduł kolumnowy','elastyczny układ treści'),''))
grid=''.join(f'<path d="M0 {i*18+1}H190" stroke="{LN}"/>' for i in range(5))+''.join(f'<path d="M{i*38+1} 0V86" stroke="{LN}"/>' for i in range(5))+f'<path d="M77 0V86" stroke="{OR}"/>'
P.append(A(300,846,190,130,f'<svg width="190" height="86" viewBox="0 0 190 86">{grid}</svg>'+cap('Siatka konstrukcyjna','porządek i rytm'),''))
rows=''.join(f'<path d="M0 {i*11+2}H190" stroke="{LN}" stroke-width="2"/>' for i in range(8))+f'<path d="M0 35H190" stroke="{OR}" stroke-width="1.5"/>'
P.append(A(528,846,190,130,f'<svg width="190" height="86" viewBox="0 0 190 86">{rows}</svg>'+cap('Rytm liniowy','subtelne tło dla układów'),''))
body=('<div class="cr pg"><div class="tab">53</div><div class="rh"><span>Część III · 39 Elementy graficzne: detale</span><span>Ceglany Renesans</span></div>'+''.join(P)+'<div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n')
open('p052b.dc.html','w').write(HEAD+body+TAIL)
c=json.load(open('canvas.json'));o=c['order'];B=c['boards']
if 'p052b.dc.html' not in o: o.insert(o.index('p052.dc.html')+1,'p052b.dc.html')
B['p052b.dc.html']={'h':1123,'w':794,'title':'Elementy graficzne: detale','x':0,'y':0}
g=[f for f in o if f!='part-i-propozycja.dc.html']
for n,f in enumerate(g): B[f]['x']=(n%6)*874;B[f]['y']=(n//6)*1243
json.dump(c,open('canvas.json','w'),ensure_ascii=False)
