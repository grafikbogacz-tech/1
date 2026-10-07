import sys,re,subprocess;sys.path.insert(0,'build')
from fotopages import *
import fotopages as FP
SG='a6773e57bb936bfccb33b9cca1bbd0be'
def im(px):return f'<img src="/_blob/{SG}" style="width:{px}px;height:{px}px;display:block"/>'
def p():
    o=lab('27 · Sygnet')+h1('Favicon, avatar i skrócony znak „C”.',30)
    o+=para('Tam, gdzie pełne logo jest zbyt małe, używamy sygnetu: kremowa, odręczna litera „C” z fakturą starej cegły, w terakotowym kole.',8)
    o+=f'<div style="display:grid;grid-template-columns:230px 1fr;gap:26px;margin-top:18px;align-items:center"><div>{im(230)}</div><div>{sub("Gdzie stosujemy",T)}'+li(['favicon strony www','avatar: Facebook, Instagram, TikTok, YouTube','logo w wizytówce Google','mały znak w miejscach bez miejsca na pełne logo'],'+',G)+'</div></div>'
    o+=f'<div style="margin-top:22px">{sub("Rozmiary — czytelność",T)}<div style="display:flex;gap:26px;align-items:flex-end;border-top:1px solid {H};padding-top:14px">'+''.join(f'<div style="text-align:center">{im(s)}<div style="{M};color:#767676;margin-top:6px">{s} px</div></div>' for s in (128,64,32,16))+'</div></div>'
    o+=f'<div style="margin-top:22px">{sub("Na tle",T)}<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0">'+''.join(f'<div style="background:{c};padding:16px;display:flex;align-items:center;justify-content:center">{im(72)}</div>' for c in ('#fff',B,'#111'))+'</div></div>'
    o+=tn(['pełne koło, bez ramki i cienia','kolory sygnetu bez zmian','dużo wolnej przestrzeni wokół'],['dopisywania napisu lub sloganu','rozciągania i zmiany proporcji','sygnetu zamiast pełnego logo w materiałach drukowanych i na stronie głównej'],'Zasada','Nie',20)
    return o
def bottom(n):
    o=subprocess.run(['node','pag/fitabs.js','all/project',f'str-{n}.dc.html'],capture_output=True,text=True).stdout
    m=re.search(r'bottom: (\d+)',o);return int(m.group(1)) if m else 9999
n='039';pp=p();FP.mywrite(n,pp,1.0);b=bottom(n)
z=max(1.0,min(1.3,round(0.985*920/max(b-100,1),2)))
while True:
    FP.mywrite(n,pp,z);b=bottom(n)
    if b<=1022 or z<=1.0:break
    z=round(z-0.02,2)
print(z,b)
