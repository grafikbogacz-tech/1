import sys;sys.path.insert(0,'build')
from ig import *
s=open(P+'str-141.dc.html').read()
k='<div class="bd">' if '<div class="bd">' in s else '<div style="position:absolute;left:'
h=s[:s.index(k)].replace('Część V · 51','Część V · Dane formalne i załączniki')
def fold(n,t,files):
    return f'<div style="border-top:2px solid {T};padding:12px 0 14px;display:grid;grid-template-columns:44px 1fr;gap:12px"><span style="{MF};font-weight:300;font-size:34px;letter-spacing:-.05em;color:{T};line-height:1">{n}</span><div><div style="font-size:16px;font-weight:500;letter-spacing:-.02em;color:#111">{t}</div><div style="margin-top:8px">{chips(files,G)}</div></div></div>'
p=lab('51 · Załączniki do pobrania')+h1('Pliki źródłowe marki.',32)+para('Wszystkie pliki do pobrania znajdują się w jednym folderze na Dysku Google. Folder ma tę samą strukturę, co lista poniżej.',8)
p+=f'<div style="border:1px dashed #767676;padding:14px 16px;margin-top:16px"><div style="{M};color:#767676">Folder na Dysku Google</div><div style="font-size:15px;color:#767676;margin-top:6px">[link do uzupełnienia]</div></div>'
p+=f'<div style="margin-top:16px">'
p+=fold('01','Logo',['SVG','PNG','wersja terakota','wersja czarna','wersja biała'])
p+=fold('02','Fonty',['Hanken Grotesk','Overpass Mono'])
p+=fold('03','Paleta kolorów',['Figma','Adobe (ASE)','HEX / RGB / CMYK'])
p+=fold('04','Szablony',['social media','prezentacja','stopka email','materiały drukowane'])
p+=fold('05','Zdjęcia',['produkt','realizacje','proces'])

p+='</div>'
p+=box('Aktualizacja','Zawsze korzystamy z plików z folderu. Nie używamy kopii przesłanych e-mailem. Nowa wersja zastępuje starą.',6)
open(P+'str-141.dc.html','w').write(h+f'<div style="position:absolute;left:63px;top:83px;width:535px;zoom:1.2;display:flex;flex-direction:column;gap:0">{p}</div>'+foot)
