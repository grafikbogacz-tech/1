import sys,json,os,subprocess,re;sys.path.insert(0,'build')
from fotopages import *
import fotopages as FP
def blk(t,body,mt=0,c=T):return f'<div style="border-top:2px solid {c};padding-top:10px;margin-top:{mt}px"><div style="{M};color:{G}">{t}</div><div style="font-size:13px;line-height:1.5;color:#222;margin-top:6px">{body}</div></div>'
I={}
def ip(n):
    def d(f):I[n]=f;return f
    return d
@ip('008')
def _():
    p=lab('04 · Marka w skrócie')+f'<div style="font-size:30px;font-weight:300;letter-spacing:-.03em;line-height:1.12;margin-top:10px;color:#111">Polska marka i producent płytek z autentycznej, ponad 100-letniej cegły rozbiórkowej.</div>'
    p+=para('Marka nie stylizuje nowego materiału na stary — pracuje z oryginalną cegłą, starannie ją selekcjonując i przygotowując do współczesnych zastosowań na ścianach, podłogach i elewacjach.',12)
    p+=box('Strategiczny wyróżnik','autentyczne pochodzenie materiału i jego historia — nie samo hasło „płytki ceglane”, którym posługuje się również konkurencja oferująca imitacje.',14)
    p+=f'<div style="margin-top:26px">{lab("05 · O marce")}</div>'
    cs=[('Kim jesteśmy','Polska marka i producent płytek z autentycznej, ponad 100-letniej cegły rozbiórkowej. Łączy historyczny charakter materiału ze współczesnymi możliwościami wykorzystania go w architekturze i aranżacji wnętrz.'),('Czym się zajmujemy','Stara cegła jest selekcjonowana i przygotowywana do ponownego zastosowania w formie płytek na ściany, podłogi i elewacje. Oferta obejmuje też narożniki oraz materiały potrzebne do montażu i wykończenia realizacji.'),('Co definiuje markę','Podstawą jest autentyczność materiału. Naturalne różnice kolorystyczne, nierówności, ślady zaprawy czy oznaki wieku nie są wadą produktu, lecz konsekwencją jego pochodzenia i częścią charakteru każdej płytki.'),('Kontekst rynkowy','Marka działa na styku rynku materiałów wykończeniowych, wyposażenia wnętrz i architektury. Konkuruje nie tylko z innymi producentami płytek ze starej cegły, ale także z klinkierem oraz produktami imitującymi starą cegłę.')]
    p+='<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px 26px;margin-top:12px">'+''.join(blk(t,b) for t,b in cs)+'</div>'
    return p
@ip('009')
def _():
    p=lab('06 · Brand Essence / DNA marki')+f'<div style="font-size:28px;font-weight:300;letter-spacing:-.03em;line-height:1.15;margin-top:12px;color:{T}">Autentyczna historia materiału, która wraca do życia we współczesnych wnętrzach i architekturze.</div>'
    cs=[('Istota marki','Ceglany Renesans przywraca wartość autentycznej starej cegle, przekształcając materiał z historią w element współczesnych wnętrz i elewacji.'),('Co marka wnosi do życia klienta','Możliwość stworzenia przestrzeni z charakterem, której nie da się uzyskać za pomocą masowej imitacji.'),('Co odróżnia markę','Nie stylizuje nowego materiału na stary. Pracuje z oryginalną cegłą rozbiórkową i zachowuje jej naturalne cechy.')]
    p+=f'<div style="margin-top:18px">'+''.join(f'<div style="border-top:1px solid {H};padding:10px 0 12px;display:grid;grid-template-columns:44px 170px 1fr;gap:10px"><span style="{M};color:{T};padding-top:2px">{i:02d}</span><div style="font-size:14px;font-weight:500;color:#111">{t}</div><div style="font-size:13px;line-height:1.45;color:#333">{b}</div></div>' for i,(t,b) in enumerate(cs,1))+'</div>'
    p+=f'<div style="margin-top:18px">{sub("Jakie emocje powinna budzić",T)}{chips(["autentyczność","trwałość","szacunek do materiału","indywidualność","ponadczasowość"],G,True)}</div>'
    p+=f'<div style="margin-top:20px">{sub("Czego tutaj nie mieszamy",T)}{chips(["cena","szybka wysyłka","rabaty","szerokość oferty","obsługa klienta","informacje o transporcie"],"#767676")}'+para('Do Brand Essence nie wprowadzamy tych elementów.',8)+'</div>'
    return p
@ip('010')
def _():
    p=lab('07 · Misja')+f'<div style="font-size:26px;font-weight:300;letter-spacing:-.03em;line-height:1.2;margin-top:12px;color:#111">Naszą misją jest przywracanie wartości autentycznej starej cegle poprzez staranną selekcję i obróbkę materiału, tak aby mógł ponownie stać się trwałym i charakterystycznym elementem współczesnych wnętrz, elewacji i przestrzeni użytkowych.</div>'
    p+=f'<div style="margin-top:34px">{lab("08 · Wizja")}</div>'
    def v(l,t):return f'<div style="background:{B};padding:16px 18px;margin-top:12px"><div style="{M};color:{G}">{l}</div><div style="font-size:17px;line-height:1.4;color:#111;margin-top:6px;letter-spacing:-.01em">{t}</div></div>'
    p+=v('Wersja A','Chcemy, aby autentyczna stara cegła była naturalnym wyborem dla osób, które szukają trwałych, ponadczasowych i niepowtarzalnych materiałów do współczesnych wnętrz i architektury.')
    p+=f'<div style="text-align:center;{M};color:#767676;margin-top:12px">lub</div>'
    p+=v('Wersja B','Chcemy rozwijać markę, która pokazuje, że materiały z historią mogą mieć trwałe miejsce we współczesnym projektowaniu — nie jako stylizacja, lecz jako autentyczny element architektury.')
    return p
@ip('011')
def _():
    p=lab('09 · Wartości marki')+h1('Pięć wartości, które widać w pracy.',30)
    vals=[('01','Autentyczność','prawdziwy materiał zamiast imitacji','Pracujemy z prawdziwą starą cegłą, a nie z materiałem stylizowanym na historyczny.',['pokazujemy naturalne różnice materiału','nie ukrywamy śladów czasu','nie próbujemy tworzyć sztucznej perfekcji','komunikujemy prawdziwe pochodzenie produktu']),('02','Szacunek do materiału','zachowanie jego historii i naturalnych cech','Stara cegła nie jest dla marki odpadem, lecz materiałem z historią i wartością.',['staranna selekcja','odpowiednie przygotowanie materiału','zachowanie charakterystycznych cech','ponowne wykorzystanie zamiast zastępowania imitacją']),('03','Rzemiosło','staranne przygotowanie do współczesnego zastosowania','Autentyczny materiał wymaga odpowiedniego przygotowania, aby mógł funkcjonować we współczesnej architekturze.',['kontrola jakości','powtarzalny proces obróbki','dbałość o detal','przygotowanie produktu do realnego zastosowania'])]
    for n,t,tag,d,l in vals:
        p+=f'<div style="border-top:2px solid {T};margin-top:18px;padding-top:12px;display:grid;grid-template-columns:1fr 1fr;gap:22px"><div>{num(n,t,36,20)}<div style="{M};color:{G};margin-top:8px">{tag}</div><div style="font-size:13px;line-height:1.5;color:#333;margin-top:8px">{d}</div></div><div>{sub("W praktyce oznacza to",T)}{li(l,"+",G)}</div></div>'
    return p
@ip('012')
def _():
    p=lab('09 · Wartości marki (cd.)')+h1('Dwie wartości długiego trwania.',30)
    vals=[('04','Ponadczasowość','estetyka oparta na trwałości, nie na trendach','Marka nie opiera się na chwilowych trendach. Stara cegła ma funkcjonować zarówno w przestrzeniach klasycznych, jak i nowoczesnych.',['spokojna komunikacja wizualna','brak przesadnego podążania za modą','nacisk na trwałość i charakter materiału','projektowanie marki z myślą o długim okresie użytkowania']),('05','Odpowiedzialność','ponowne wykorzystanie wartościowego materiału','Marka przywraca materiał do obiegu zamiast zastępować go nową imitacją.',['ponowne wykorzystanie starej cegły','ograniczenie marnowania wartościowego materiału','komunikacja oparta na faktach','bez przesadnych deklaracji ekologicznych'])]
    for n,t,tag,d,l in vals:
        p+=f'<div style="border-top:2px solid {T};margin-top:18px;padding-top:12px;display:grid;grid-template-columns:1fr 1fr;gap:22px"><div>{num(n,t,36,20)}<div style="{M};color:{G};margin-top:8px">{tag}</div><div style="font-size:13px;line-height:1.5;color:#333;margin-top:8px">{d}</div></div><div>{sub("W praktyce oznacza to",T)}{li(l,"+",G)}</div></div>'
    p+=f'<div style="margin-top:26px">{sub("Wszystkie wartości marki",T)}{chips(["Autentyczność","Szacunek do materiału","Rzemiosło","Ponadczasowość","Odpowiedzialność"],G,True)}</div>'
    return p
if __name__=='__main__':
    def bottom(n):
        o=subprocess.run(['node','pag/fitabs.js','all/project',f'str-{n}.dc.html'],capture_output=True,text=True).stdout
        m=re.search(r'bottom: (\d+)',o);return int(m.group(1)) if m else 9999
    for n in (sys.argv[1:] or sorted(I)):
        p=I[n]();FP.mywrite(n,p,1.0);b=bottom(n)
        z=max(1.0,min(1.45,round(0.985*920/max(b-100,1),2)))
        while True:
            FP.mywrite(n,p,z);b=bottom(n)
            if b<=1022 or z<=1.0:break
            z=round(z-0.02,2)
        print(n,z,b)
