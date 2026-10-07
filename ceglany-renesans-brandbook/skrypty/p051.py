import sys,re,subprocess;sys.path.insert(0,'build')
from fotopages import *
import fotopages as FP
COL='#FBE0D6'
def ph1(b,pos='50% 50%',size='cover'):return f'background:url(/_blob/{b}) {pos}/{size} no-repeat #CBCAC4'
def thumb(inner,h=96):
    cols=''.join(f'<i style="background:{"#F6D3C6" if (i//4)%2==0 else "#FBE6DE"};opacity:.8"></i>' for i in range(12))
    return f'<div style="position:relative;height:{h}px;background:#fff;box-shadow:inset 0 0 0 1px #DCDCDC"><div style="position:absolute;inset:8px;display:grid;grid-template-columns:repeat(12,1fr);gap:4px">{cols}</div><div style="position:absolute;inset:8px;display:grid;grid-template-columns:repeat(12,1fr);grid-template-rows:repeat(3,1fr);gap:4px">{inner}</div></div>'
def line(h,w='100%',c='#111'):return f'<i style="display:block;height:{h}px;width:{w};background:{c}"></i>'
R='grid-row:1/span 3;'
def A():return thumb(f'<div style="grid-column:1/span 8;{R}{ph1(BATH)}"></div><div style="grid-column:9/span 4;{R}display:flex;flex-direction:column;gap:5px;justify-content:flex-end">{line(3,"20px",T)}{line(8)}{line(4,"100%","#CBCAC4")}{line(4,"70%","#CBCAC4")}</div>')
def B():return thumb(f'<div style="grid-column:1/span 4;{R}display:flex;flex-direction:column;justify-content:space-between">{line(26,"34px",T)}<div style="display:flex;flex-direction:column;gap:5px">{line(9)}{line(4,"100%","#CBCAC4")}{line(4,"60%","#CBCAC4")}</div></div><div style="grid-column:7/span 6;{R}{ph1(STAIR)}"></div>')
def C():return thumb(f'<div style="grid-column:1/span 12;{R}margin:-8px;{ph1(HERR,"50% 60%","180%")}"></div><div style="grid-column:1/span 4;grid-row:3;z-index:1;background:#fff;display:flex;gap:6px;align-items:center;padding:0 8px"><span style="width:8px;height:8px;background:{T}"></span>{line(4,"34px")}</div>')
def D():return thumb(f'<div style="grid-column:1/span 4;{R}{ph1(BATH)}"></div><div style="grid-column:5/span 4;{R}{ph1(STAIR)}"></div><div style="grid-column:9/span 4;{R}{ph1(CHAIR)}"></div>')
def wall():
    c=['#B5654A','#A9553A','#C47C5C','#B06045']
    def br(a,b,k):return f'<div style="grid-column:{a}/span {b};background:{c[k%4]}"></div>'
    r1=''.join(br(1+4*i,4,i) for i in range(3))
    r2=br(1,2,3)+br(3,4,0)+br(7,4,1)+br(11,2,2)
    r3=''.join(br(1+4*i,4,i+2) for i in range(3))
    row=lambda x:f'<div style="display:grid;grid-template-columns:repeat(12,1fr);gap:6px;height:24px">{x}</div>'
    return f'<div style="display:flex;flex-direction:column;gap:6px">{row(r1)}{row(r2)}{row(r3)}</div>'
def p():
    o=lab('35 · Siatka i układ')+h1('Siatka z cegły.',30)
    o+=para('Siatka wynika z produktu: jedna cegła to cztery z dwunastu kolumn, a kolejny rząd przesuwamy o pół cegły, jak w murze. Dzięki temu asymetria jest uporządkowana, a nie przypadkowa.',8)
    o+=f'<div style="margin-top:14px">{wall()}<div style="display:flex;gap:14px;flex-wrap:nowrap;margin-top:8px;white-space:nowrap"><span style="{M};color:{T}">1 cegła = 4 kolumny</span><span style="{M};color:{T}">rząd 2: przesunięcie o 2 kolumny</span><span style="{M};color:{T}">fuga = rynna</span></div></div>'
    ex=[('A','zdjęcie 2 cegły + tekst 1 cegła',A()),('B','tekst 1 cegła, zdjęcie 1½ cegły z przesunięciem',B()),('C','pełny kadr + podpis na 1 cegłę',C()),('D','trzy karty produktu, każda 1 cegła',D())]
    o+='<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px 18px;margin-top:14px">'+''.join(f'<div>{t}<div style="display:flex;gap:8px;margin-top:6px;align-items:baseline"><span style="{M};color:{T}">{a}</span><span style="font-size:12.5px;color:#111">{b}</span></div></div>' for a,b,t in ex)+'</div>'
    sc=[8,16,24,40,64,96]
    o+=f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:20px"><div style="border-top:2px solid {T};padding-top:10px">{sub("Skala odstępów (px)",G)}<div style="display:flex;gap:8px;align-items:flex-end;height:80px">'+''.join(f'<div style="text-align:center"><i style="display:block;width:{s*0.65}px;height:{s*0.8}px;background:{T if s==96 else "#111"}"></i></div>' for s in sc)+f'</div><div style="{M};color:#767676;margin-top:6px">8 · 16 · 24 · 40 · 64 · 96</div></div><div style="border-top:2px solid {T};padding-top:10px">{sub("Linie i separatory",G)}<div style="display:flex;flex-direction:column;gap:14px;margin-top:14px"><i style="display:block;border-top:1px solid #111"></i><i style="display:block;border-top:1px solid {H}"></i><i style="display:block;border-top:2px solid {T};width:48px"></i></div><div style="{M};color:#767676;margin-top:14px">1 px czerń · 1 px beż · 2 px akcent</div></div></div>'
    o+=box('Zasada widoku','Maksymalnie: 1 zdjęcie główne, 1 nagłówek, 1 blok tekstu, 1 CTA i kilka podpisów. Reszta to biała przestrzeń. Marginesy druku: min. 15 mm; web: mobile-first, breakpointy 390 / 768 / 1280 px.',18)
    d=[('Co','Siatka 12 kolumn oparta na module cegły: 4 kolumny to jedna cegła. Moduł 8 px, rynna 24 px.'),('Dlaczego','Układ czyta się jak mur: rytmicznie, asymetrycznie i spokojnie. Siatka bierze proporcje z produktu.'),('Jak stosować','Bloki mają szerokość 4, 8 lub 12 kolumn, kolejny rząd przesuwamy o 2. Zdjęcie 6–8 kolumn, tekst 4. Tekst do lewej.'),('Czego unikać','Układów symetrycznych „na środek”, zaokrąglonych kart, ramek, cieni.')]
    o+=f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px 24px;margin-top:18px;border-top:1px solid {H};padding-top:12px">'+''.join(f'<div><div style="{M};color:{T if i==3 else G}">{a}</div><div style="font-size:12.5px;line-height:1.45;color:#333;margin-top:3px">{b}</div></div>' for i,(a,b) in enumerate(d))+'</div>'
    return o
def bottom(n):
    o=subprocess.run(['node','pag/fitabs.js','all/project',f'str-{n}.dc.html'],capture_output=True,text=True).stdout
    m=re.search(r'bottom: (\d+)',o);return int(m.group(1)) if m else 9999
n='051';pp=p();FP.mywrite(n,pp,1.0);b=bottom(n)
z=max(1.0,min(1.3,round(0.985*920/max(b-100,1),2)))
while True:
    FP.mywrite(n,pp,z);b=bottom(n)
    if b<=1022 or z<=1.0:break
    z=round(z-0.02,2)
print(z,b)
