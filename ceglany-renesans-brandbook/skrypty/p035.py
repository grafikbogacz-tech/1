import sys,re,subprocess;sys.path.insert(0,'build')
from fotopages import *
import fotopages as FP
BG='1a1a6603944803de781a123be9b4f816'
def tile(bg,inner,label,ok=True,h=104,photo=False):
    st=f'background:url(/_blob/{BG}) 50% 40%/cover no-repeat' if photo else f'background:{bg}'
    mk=f'<span style="position:absolute;top:6px;right:6px;width:20px;height:20px;border-radius:50%;background:{G if ok else T};color:#fff;font-size:13px;line-height:20px;text-align:center;box-shadow:0 0 0 2px #fff;{MF}">{"✓" if ok else "×"}</span>'
    return f'<div><div style="position:relative;height:{h}px;{st};display:flex;align-items:center;justify-content:center;overflow:hidden">{inner}{mk}</div><div style="font-size:12.5px;line-height:1.35;color:#111;margin-top:6px">{label}</div></div>'
def lg(f,w=96,extra=''):return f'<img src="{f}" style="width:{w}px;height:auto;display:block;{extra}"/>'
def grid(items):return '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px 14px;margin-top:10px">'+''.join(items)+'</div>'
def p():
    o=lab('25 · Logo na tle')+h1('Logo na tle: co działa, a co nie.',30)
    o+=para('Wybieramy wersję logo do tła, nigdy odwrotnie. Przy złożonym tle używamy apli.',8)
    o+=f'<div style="margin-top:16px">{sub("Poprawne",G,0)}</div>'
    o+=grid([
     tile('#fff',lg('logo-or.svg')+'','Podstawowa kolor na bieli',True,).replace('background:#fff','background:#fff;box-shadow:inset 0 0 0 1px #DCDCDC'),
     tile(B,lg('logo-k.svg'),'Mono na beżu'),
     tile('#ED6842',lg('logo-w.svg'),'Negatyw kolor na terakocie'),
     tile('#0D4C73',lg('logo-w.svg'),'Negatyw na granacie'),
     tile('#1E1E1C',lg('logo-w.svg'),'Negatyw mono na czerni'),
     tile('',f'<div style="background:#fff;padding:12px 16px">{lg("logo-or.svg",84)}</div>','Apla na zdjęciu',True,photo=True)])
    o+=f'<div style="margin-top:20px">{sub("Niepoprawne",T,0)}</div>'
    o+=grid([
     tile('#ED6842',lg('logo-or.svg'),'Niski kontrast: kolor na terakocie',False),
     tile(B,lg('logo-w.svg'),'Niski kontrast: negatyw na beżu',False),
     tile('',lg('logo-or.svg'),'Złożone tło bez apli',False,photo=True),
     tile('#fff',lg('logo-or.svg',96,'filter:drop-shadow(3px 4px 3px rgba(0,0,0,.55))'),'Dodawanie cienia',False).replace('background:#fff','background:#fff;box-shadow:inset 0 0 0 1px #DCDCDC'),
     tile('#fff',lg('logo-or.svg',96,'transform:scale(1.5,.7)'),'Deformowanie, zmiana proporcji',False).replace('background:#fff','background:#fff;box-shadow:inset 0 0 0 1px #DCDCDC'),
     tile('#fff',lg('logo-or.svg',96,'filter:hue-rotate(150deg) saturate(1.3)'),'Recolor poza zatwierdzone warianty',False).replace('background:#fff','background:#fff;box-shadow:inset 0 0 0 1px #DCDCDC')])
    o+=f'<div style="margin-top:18px">{sub("Także niepoprawne",T,4)}{chips(["brak pola ochronnego","modyfikowanie elementów znaku"],"#767676")}</div>'
    o+=box('Doprecyzowanie dla obecnej komunikacji','Na zdjęciach realizacji logo nie powinno zasłaniać produktu. Jeśli fotografia sama jest silnym dowodem marki, logo może być dyskretne albo pojawić się na planszy otwierającej / końcowej.',16)
    return o
def bottom(n):
    o=subprocess.run(['node','pag/fitabs.js','all/project',f'str-{n}.dc.html'],capture_output=True,text=True).stdout
    m=re.search(r'bottom: (\d+)',o);return int(m.group(1)) if m else 9999
n='035';pp=p();FP.mywrite(n,pp,1.0);b=bottom(n)
z=max(1.0,min(1.3,round(0.985*920/max(b-100,1),2)))
while True:
    FP.mywrite(n,pp,z);b=bottom(n)
    if b<=1022 or z<=1.0:break
    z=round(z-0.02,2)
print(z,b)
