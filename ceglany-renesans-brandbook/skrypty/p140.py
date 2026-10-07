import sys;sys.path.insert(0,'build')
import ig
from ig import *
s=open(P+'str-140.dc.html').read()
k='<div style="position:absolute;left:52px;top:68px'
h=s[:s.index(k)].replace('Część V · 50','Część V · Dane formalne i załączniki')
def appr(n,t,who,note,fill=True):
    st=f'border-top:2px solid {T}' if fill else f'border-top:1px dashed #767676'
    return f'<div style="{st};padding:12px 0 14px;display:grid;grid-template-columns:70px 1fr;gap:14px"><span style="{MF};font-weight:300;font-size:44px;letter-spacing:-.05em;color:{T if fill else "#767676"};line-height:1">{n}</span><div><div style="{M};color:{G}">{t}</div><div style="font-size:16px;font-weight:500;letter-spacing:-.025em;color:{"#111" if fill else "#767676"};margin-top:4px">{who}</div><div style="font-size:13px;line-height:1.45;color:#333;margin-top:6px">{note}</div></div></div>'
p=lab('50 · Zatwierdzanie')+h1('Kto zatwierdza odstępstwa od zasad.',32)+para('Brand Book obowiązuje wszystkie materiały marki. Odstępstwo od zasad wymaga decyzji — zatwierdzają je osoby poniżej, w tej kolejności.',8)
p+=f'<div style="margin-top:18px">'+appr('1','Właściciel marki','Marek Pochcioł','CEGMAR Marek Pochcioł. Ostateczna decyzja w sprawie każdego odstępstwa od zasad.')+appr('2','Opiekun marki','Ewelina Bogacz','Project Manager, opiekun klienta<br>721 004 201 &nbsp;|&nbsp; ewelina@weboski.pl<br>weboski.pl · ul. Słowackiego 4b, Andrychów')+'</div>'
p+=f'<div style="margin-top:22px">{sub("Zasada",T)}'+steps([('1','Zgłoś odstępstwo'),('2','Opisz powód i materiał'),('3','Poczekaj na decyzję'),('4','Zapisz decyzję')],0)+'</div>'
p+=box('Dane rejestrowe właściciela','strona 138.',22)
open(P+'str-140.dc.html','w').write(h+f'<div style="position:absolute;left:52px;top:68px;width:437px;zoom:1.47;display:flex;flex-direction:column;gap:0">{p}</div>'+foot)
