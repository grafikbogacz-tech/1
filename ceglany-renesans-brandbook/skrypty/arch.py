import sys,re,subprocess;sys.path.insert(0,'build')
from fotopages import *
import fotopages as FP
def bignum(n,t):return num(n,t,34,20)
def p27():
    o=lab('Część II · jak czytać ten rozdział')+h1('Od obietnicy do gotowych komunikatów.',30)
    o+=para('Rozdział układa komunikację marki od ogółu do szczegółu. Każdy kolejny poziom wynika z poprzedniego: najpierw to, co obiecujemy, na końcu gotowe zdania do użycia.',8)
    L=[('14','Obietnica marki','co obiecujemy klientowi'),('15','Value Proposition','dlaczego kupić u nas, a nie gdzie indziej'),('16','Główne przesłanie','jedno zdanie, które marka powtarza wszędzie'),('17','Filary komunikacji','tematy, wokół których budujemy treści'),('18','Argumenty i dowody','co mówimy i czym to udowadniamy'),('19','Key Messages','gotowe komunikaty dla marketingu i sprzedaży'),('20','Elevator Pitch','marka w kilku zdaniach, zależnie od tematu')]
    o+='<div style="margin-top:12px;border-top:2px solid '+T+'">'+''.join(f'<div style="display:grid;grid-template-columns:34px 190px 1fr;gap:10px;border-bottom:1px solid {H};padding:6px 0;align-items:baseline"><span style="{M};color:{T}">{a}</span><span style="font-size:13.5px;font-weight:500;color:#111">{b}</span><span style="font-size:12.5px;color:#333">{c}</span></div>' for a,b,c in L)+'</div>'
    o+=f'<div style="margin-top:22px">{bignum("14","Obietnica marki")}<div style="font-size:19px;font-weight:300;letter-spacing:-.02em;line-height:1.3;color:{T};margin-top:8px">Autentyczny charakter starej cegły w formie materiału gotowego do współczesnych realizacji.</div></div>'
    o+=f'<div style="margin-top:22px;border-top:1px solid {H};padding-top:12px">{bignum("15","Value Proposition")}'+para('Dlaczego mam kupić płytki właśnie od Ceglanego Renesansu zamiast imitacji cegły albo produktów konkurencji?',8)
    o+=f'<div style="margin-top:8px">{chips(["stara, ponad 100-letnia cegła — nie imitacja gipsowa ani betonowa","selekcjonowany materiał","kontrola pochodzenia i przechowywania","płytki obrabiane i myte","zachowane pozostałości zaprawy","dostępne materiały montażowe","dostawa w Polsce i za granicę","większość zamówień magazynowych wysyłana w 24 h"],G)}</div>'
    o+=box('W jednym zdaniu','Ceglany Renesans tworzy płytki z autentycznej, ponad 100-letniej cegły rozbiórkowej, starannie selekcjonowanej i obrabianej tak, aby zachować jej naturalny charakter, a jednocześnie przygotować ją do współczesnych wnętrz, podłóg i elewacji.',12)+'</div>'
    return o
def p28():
    o=lab('Część II · przesłanie, filary, dowody')+f'<div style="margin-top:6px">{bignum("16","Główne przesłanie marki")}</div>'
    o+=f'<div style="font-size:26px;font-weight:300;letter-spacing:-.03em;line-height:1.15;color:{T};margin-top:8px">To nie jest imitacja. To prawdziwa historia.</div>'+para('U nas dostajesz fragment rzeczywistego, starego materiału, a nie produkt, który tylko próbuje go naśladować.',6)
    o+=f'<div style="margin-top:20px;border-top:1px solid {H};padding-top:12px">{bignum("17","Filary komunikacji")}'
    P=[('1','Prawdziwa stara cegła, nie imitacja.',['ponad 100-letnia cegła','cegła rozbiórkowa','naturalne różnice','ślady czasu','pozostałości zaprawy','niepowtarzalność każdej partii']),('2','Materiał, który kiedyś był częścią budynku, wraca do architektury w nowej formie.',[]),('3','Jeden autentyczny materiał — wiele możliwości aranżacyjnych.',[])]
    o+='<div style="display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:14px;margin-top:10px">'+''.join(f'<div style="border-top:2px solid {T};padding-top:8px"><div style="{M};color:{T}">Filar {a}</div><div style="font-size:14px;font-weight:500;line-height:1.3;color:#111;margin-top:4px">{t}</div>'+(f'<div style="margin-top:8px">{sub("Komunikujemy",G,4)}{li(l,"+",G,12)}</div>' if l else '')+'</div>' for a,t,l in P)+'</div></div>'
    T9=[('Autentyczna stara cegła','oryginalna cegła rozbiórkowa, ponad 100-letnia'),('Nie imitacja','produkt nie jest wykonany z gipsu ani betonu'),('Staranna jakość','selekcja materiału przed dalszą obróbką'),('Zachowany naturalny charakter','naturalna struktura i pozostałości wapiennej zaprawy'),('Nowoczesna produkcja','obróbka na nowoczesnych maszynach'),('Kompletne rozwiązanie','płytki + narożniki + fuga + kleje + impregnaty'),('Szerokie zastosowanie','ściana, podłoga, elewacja, kominek'),('Sprawna realizacja','większość produktów magazynowych wysyłana w ciągu 24 h'),('Możliwość sprawdzenia przed zakupem','dostępne próbki')]
    o+=f'<div style="margin-top:22px;border-top:1px solid {H};padding-top:12px">{bignum("18","Argumenty i dowody")}'+table(T9,['1fr','1.3fr'],['Komunikujemy','Dowodzimy'],12.5)+'</div>'
    return o
def p29():
    o=lab('Część II · gotowe komunikaty')+f'<div style="margin-top:6px">{bignum("19","Key Messages")}</div>'+para('Najważniejsze komunikaty do wykorzystania przez marketing i sprzedaż.',8)
    o+=f'<div style="font-size:24px;font-weight:300;letter-spacing:-.03em;line-height:1.2;color:{T};margin-top:14px">Tworzymy płytki z autentycznej, ponad 100-letniej cegły rozbiórkowej.</div>'
    o+=f'<div style="margin-top:28px;border-top:1px solid {H};padding-top:12px">{bignum("20","Elevator Pitch")}'+para('Jedno zdanie na każdy temat rozmowy.',6)
    R=[('Marka / komunikacja główna','Tworzymy płytki z autentycznej, ponad 100-letniej cegły rozbiórkowej.'),('O produkcie','Każda płytka zachowuje naturalną strukturę, kolor i ślady historii starej cegły.'),('O autentyczności','To nie imitacja cegły. To prawdziwa stara cegła przygotowana do ponownego wykorzystania.'),('O designie','Historia materiału spotyka się ze współczesnym wnętrzem.'),('O produkcji','Starannie selekcjonujemy i przygotowujemy starą cegłę, aby zachować jej naturalny charakter.'),('O zastosowaniu','Ściany, podłogi i elewacje — jeden materiał, wiele możliwości.'),('O zakupie','Możesz zamówić próbkę i zobaczyć prawdziwą cegłę przed podjęciem decyzji.')]
    o+=table(R,['190px','1fr'],['Temat','Komunikat'],13)+'</div>'
    return o
def bottom(n):
    o=subprocess.run(['node','pag/fitabs.js','all/project',f'str-{n}.dc.html'],capture_output=True,text=True).stdout
    m=re.search(r'bottom: (\d+)',o);return int(m.group(1)) if m else 9999
for n,f in (('027',p27),('028',p28),('029',p29)):
    pp=f();FP.mywrite(n,pp,1.0);b=bottom(n)
    z=max(1.0,min(1.4,round(0.985*920/max(b-100,1),2)))
    while True:
        FP.mywrite(n,pp,z);b=bottom(n)
        if b<=1022 or z<=1.0:break
        z=round(z-0.02,2)
    print(n,z,b)
