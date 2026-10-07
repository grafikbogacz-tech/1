import sys;sys.path.insert(0,'build')
from ig import *
exec(open('build/adspages.py').read().split('# 178')[0].split("L='C · Google Ads'")[1])
Zf=1.3
p=lab('49 · Dane formalne')+h1('Standard dokumentów formalnych.',32)+para('Tam, gdzie trzeba jednoznacznie wskazać przedsiębiorcę, używamy pełnej nazwy rejestrowej. Marka może jej towarzyszyć, ale jej nie zastępuje.',8)
p+=f'<div style="background:{B};padding:14px 18px;margin-top:16px"><div style="{M};color:{G}">Pełna nazwa przedsiębiorcy</div><div style="font-size:26px;font-weight:300;letter-spacing:-.03em;color:#111;margin-top:4px">CEGMAR Marek Pochcioł</div></div>'
p+=f'<div style="margin-top:22px">{sub("Pełna nazwa obowiązuje w",T)}'+chips(['regulaminach','politykach','umowach','fakturach','ofertach formalnych','danych sprzedawcy'],G,True)+'</div>'
p+=f'<div style="margin-top:22px">{sub("Marka",G)}'+para('„Ceglany Renesans” może występować w tych dokumentach dodatkowo, jako oznaczenie marki, np. w nagłówku.',0)+'</div>'
p+=cols(f'{sub("Tak",G)}'+li(['pełna nazwa w danych sprzedawcy','marka jako dodatkowe oznaczenie','te same dane we wszystkich dokumentach'],'+',G),f'{sub("Nie",T)}'+li(['samo „Ceglany Renesans” w miejsce danych rejestrowych','różne warianty nazwy w różnych dokumentach'],'−',T),22,26)
p+=box('Zasada','Nazwa „Ceglany Renesans” nie zastępuje danych rejestrowych przedsiębiorcy. Dane rejestrowe: strona 138.',20)
write('str-139',p,0,Zf)
