import sys,re,subprocess;sys.path.insert(0,'build')
from fotopages import *
import fotopages as FP
def cell(st,cap,dashed=False,span=''):
    b=f'border:1px dashed #767676;background:#F4F2EA;' if dashed else st
    col='#555' if dashed else '#fff'
    sh='' if dashed else 'text-shadow:0 1px 3px rgba(0,0,0,.85);'
    ov='' if dashed else '<div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.62) 0%,rgba(0,0,0,.28) 32%,rgba(0,0,0,0) 62%)"></div>'
    return f'<div style="position:relative;{span}{b}">{ov}<div style="position:absolute;left:8px;right:8px;bottom:6px;{MF};font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:{col};{sh}">{cap}</div></div>'
def bg(b,pos='50% 50%',size='cover'):return f'background:url(/_blob/{b}) {pos}/{size} no-repeat #CBCAC4;'
def p():
    o=lab('21 · Moodboard')+h1('Jak marka wygląda w kadrze.',30)
    o+=para('Moodboard pokazuje klimat zdjęć i grafik, zanim powstanie pierwszy kadr. Opiera się wyłącznie na realnych ujęciach materiału i jego kontekstu.',8)
    o+=f'<div style="display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:140px 100px 90px;gap:8px;margin-top:14px">'+cell(bg('fe1d49e4df6d7ab013fa9a883eda217b','50% 50%'),'Szeroki kadr: ściana z płytek','','grid-row:1/span 3;')+cell(bg('ec275b1cbdbf1ee2fb9df0a37830e99e','50% 38%'),'Zbliżenie faktury','','grid-column:2/span 2;')+cell(bg('590524d23dce1948f1eb03419131b26d','35% 45%'),'Produkt','','grid-column:2;grid-row:2/span 2;')+cell(bg('321084940182209a83e0601d4938622f','50% 50%'),'Proces i magazyn','','grid-column:3;grid-row:2/span 2;')+'</div>'
    o+=f'<div style="margin-top:16px;border-top:2px solid {T};padding-top:10px">{sub("Słowa kluczowe",G)}{chips(["autentyczność","materiałowość","historia","rzemiosło","jakość","naturalność","współczesność","spokój"],G,True)}</div>'
    sw=[('#A9553A','cegła'),('#fff','biel'),('#CBCAC4','beton'),(T,'pomarańcz — tylko detal')]
    o+=f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:16px"><div>{sub("Estetyka",T)}<div style="font-size:13px;line-height:1.5;color:#222">Współczesna architektura, katalogi materiałów, magazyny wnętrzarskie, editorial, minimalizm szwajcarski.</div></div><div>{sub("Nastrój",T)}<div style="font-size:13px;line-height:1.5;color:#222">Spokojny, rzeczowy, premium bez przepychu. Światło dzienne, bez dramatyzowania.</div></div></div>'
    o+=f'<div style="margin-top:16px">{sub("Paleta w kadrze",T)}<div style="display:flex;gap:6px">'+''.join(f'<div style="flex:{3 if n.startswith("pomar") else 2}"><div style="height:34px;background:{c};box-shadow:inset 0 0 0 1px #DCDCDC"></div><div style="font-size:12px;color:#333;margin-top:4px">{n}</div></div>' for c,n in sw)+'</div></div>'
    d=[('Co','Moodboard oparty wyłącznie na realnych kadrach materiału i jego kontekstu. Bez ornamentów.'),('Dlaczego','Marka ma wyglądać jak katalog materiałów, nie jak dekoracja wnętrz.'),('Jak stosować','Układ asymetryczny, ale na siatce. Kadry w różnej skali: szeroki, średni, detal.'),('Czego unikać','Kadrów bez produktu, mocno przesyconych kolorów, filtrów vintage, stylu „industrial loft” jako jedynego kierunku.')]
    o+=f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px 24px;margin-top:18px;border-top:1px solid {H};padding-top:12px">'+''.join(f'<div><div style="{M};color:{T if i==3 else G}">{a}</div><div style="font-size:12.5px;line-height:1.45;color:#333;margin-top:3px">{b}</div></div>' for i,(a,b) in enumerate(d))+'</div>'
    return o
def bottom(n):
    o=subprocess.run(['node','pag/fitabs.js','all/project',f'str-{n}.dc.html'],capture_output=True,text=True).stdout
    m=re.search(r'bottom: (\d+)',o);return int(m.group(1)) if m else 9999
n='054';pp=p();FP.mywrite(n,pp,1.0);b=bottom(n)
z=max(1.0,min(1.3,round(0.985*920/max(b-100,1),2)))
while True:
    FP.mywrite(n,pp,z);b=bottom(n)
    if b<=1022 or z<=1.0:break
    z=round(z-0.02,2)
print(z,b)
