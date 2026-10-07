import sys,json,os,subprocess,re;sys.path.insert(0,'build')
from vipages import *
import ig
def ph(blob,h,cap=None,pos='50% 50%',size='cover',mt=0):
    c=f'<div style="position:absolute;left:8px;right:8px;bottom:6px;{MF};font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:#fff;text-shadow:0 1px 3px rgba(0,0,0,.85)">{cap}</div>' if cap else ''
    return f'<div style="position:relative;height:{h}px;margin-top:{mt}px;background:url(/_blob/{blob}) {pos}/{size} no-repeat #d9d3bd">{c}</div>'
def tn(a,b,la='Tak',lb='Nie',mt=14,ca=G,cb=T):
    return cols(f'{sub(la,ca)}'+li(a,'+',ca),f'{sub(lb,cb)}'+li(b,'−',cb),mt,26)
BATH='1a1a6603944803de781a123be9b4f816';STAIR='f343626a0da1dd4c6f1d61158d82487b';HERR='b1a220213e227054557db356b1f27ebb';CHAIR='c1ba344c60538cebeac1c1b8984d2e6a';ART='5ee65d38d8e4a9de7497db222758e04f'
F={}
def fp(n):
    def d(f):F[n]=f;return f
    return d
@fp('056')
def _():
    p=lab('37.1–37.2 · Zasada i nastrój')+h1('Fotografia jest dowodem produktu.',30)
    p+=para('Zdjęcie ma pokazywać prawdziwy materiał: strukturę, różnice, ślady wieku i sposób, w jaki pracuje w realnej przestrzeni. Nie „upiększa” cegły w sposób, który zmienia jej charakter. Buduje zaufanie, pomaga wybrać produkt i pokazuje źródło wartości marki.',8)
    p+=f'<div style="margin-top:14px">{sub("Główna zasada",T)}'+steps([('01','Autentyczny materiał'),('02','Realny kontekst'),('03','Czytelny detal'),('04','Wiarygodny efekt')],0)+'</div>'
    p+=ph(BATH,200,'Prawdziwy materiał w realnej przestrzeni',mt=16)
    p+=f'<div style="margin-top:16px">{sub("Nastrój",T)}{chips(["naturalny","spokojny","materiałowy","ciepły, ale nie „rustykalny”","autentyczny","bez nadmiernej stylizacji","nacisk na fakturę i światło"],G)}</div>'
    p+=tn(['prawdziwego materiału','jakości wykonania','realnego zastosowania','historii i charakteru starej cegły'],['przesadnie „instagramowego” looku','ciężkich presetów','nadmiernej saturacji','stylizacji, która robi z każdej realizacji loft','zbyt ciemnych, dramatycznych kadrów, jeśli utrudniają ocenę produktu'],'Zdjęcie wzmacnia wrażenie','Unikamy',16)
    return p
@fp('057')
def _():
    p=lab('37.3–37.4 · Kolor i światło')+h1('Wierny kolor, światło wydobywające fakturę.',30)
    p+=box('Priorytet','wierne odwzorowanie koloru cegły. Zdjęcie produktu pomaga zrozumieć realny kolor i zróżnicowanie partii, a nie obiecuje idealnie powtarzalnej powierzchni.',12)
    p+=tn(['balans bieli możliwie neutralny','naturalne ciepło wnętrza może zostać'],['przesuwania cegły w pomarańcz lub czerwień','zwiększania nasycenia, żeby materiał był „bardziej efektowny”','filtrów ujednolicających różnice między płytkami','gaszenia struktury wygładzaniem lub HDR'],'Kolor — zasady','Kolor — nie',14)
    p+=ph(HERR,150,'Światło boczne wydobywa fakturę',mt=16,pos='50% 55%')
    p+=f'<div style="margin-top:14px">{sub("Dobre światło pokazuje",T)}{chips(["nierówności","strukturę","ślady zaprawy","różnice tonów","zachowanie materiału w przestrzeni"],G)}</div>'
    p+=tn(['naturalne światło dzienne','miękkie światło boczne','światło wydobywające fakturę','umiarkowany kontrast'],['płaskiego światła frontalnego','mocnego flesza i prześwietleń','bardzo żółtego lub bardzo zimnego światła LED','silnych refleksów zasłaniających fakturę'],'Preferujemy','Unikamy',14)
    return p
@fp('058')
def _():
    p=lab('37.5–37.6 · Kompozycja i kadr produktowy')+h1('Trzy poziomy kadru w każdej sesji.',30)
    cs=[(BATH,'1 Szeroki','całe wnętrze lub elewacja i relacja cegły z przestrzenią','50% 50%','cover'),(STAIR,'2 Średni','fragment zastosowania: ściana, kominek, schody, elewacja','50% 50%','cover'),(HERR,'3 Detal','struktura, krawędzie, fuga, zróżnicowanie i ślady materiału','50% 60%','220%')]
    p+='<div style="display:grid;grid-template-columns:1.5fr 1.2fr 1fr;gap:10px;margin-top:12px">'+''.join(f'<div>{ph(b,160,pos=pos,size=sz)}<div style="{M};color:{T};margin-top:8px">{t}</div><div style="font-size:12.5px;line-height:1.4;color:#333;margin-top:3px">{d}</div></div>' for b,t,d,pos,sz in cs)+'</div>'
    p+=box('Zasada','jedna realizacja nie składa się wyłącznie z szerokich zdjęć ani samych detali.',14)
    p+=f'<div style="margin-top:20px">{sub("Kadr produktowy — standard",T)}'+cols(li(['neutralne tło lub bardzo spokojne otoczenie','dobra ostrość i realna faktura','bez dekoracji konkurujących z produktem'],'+',G),li(['minimum jedno zdjęcie z bliska','minimum jedno zdjęcie większej powierzchni'],'+',G),0,26)+'</div>'
    p+=f'<div style="margin-top:16px">{sub("Próbki i zestawy próbek — to samo",T)}{chips(["światło","kąt","odległość","tło"],G,True)}</div>'
    p+=para('Dzięki temu klient może faktycznie porównać warianty. Zdjęcia produktowe potrzebne są osobno dla kart produktów i porównań.',8)
    return p
@fp('059')
def _():
    p=lab('37.7–37.8 · Realizacje, ludzie i proces')+h1('Realizacja jako dowód. Człowiek przy pracy.',30)
    p+=cols(f'{sub("Realizacja ma zawierać",T)}'+li(['szeroki plan','detal produktu','kontekst zastosowania','jeśli to możliwe: przed / w trakcie / po'],'+',G),ph(STAIR,128),14,24)
    p+=f'<div style="margin-top:14px">{sub("Przy publikacji znamy",T)}{chips(["nazwę produktu","rodzaj fugi","miejsce zastosowania","autora zdjęcia / wykonawcę","rok realizacji — jeśli jest"],G)}</div>'
    p+=para('Realizacja ma być dowodem, nie tylko inspiracją.',8)
    left=f'{sub("Ludzie i proces — preferowane",T)}{chips(["ręce przy sortowaniu","cięcie","pakowanie","montaż","wybór partii","rozmowa z klientem","praca na magazynie / produkcji"],G)}'+f'<div style="margin-top:14px">{sub("Unikamy",T)}'+li(['sztucznego pozowania bez kontekstu','„firmowych” zdjęć, które nic nie mówią o procesie','zdjęć zespołu tylko po to, żeby „byli ludzie”'],'−',T)+'</div>'
    p+=f'<div style="margin-top:22px;border-top:2px solid {T};padding-top:12px;display:grid;grid-template-columns:1fr 210px;gap:22px"><div>{left}</div><div>{ph("fe0ae6a7c8a98978702f3a6f318126fe",270,"Człowiek przy pracy","50% 35%")}</div></div>'
    p+=qt('Człowiek na zdjęciu powinien coś robić lub pomagać zrozumieć, jak działa marka.',14)
    return p
@fp('060')
def _():
    GOOD='fe1d49e4df6d7ab013fa9a883eda217b';WEAK='a24d4df4840b02dc495b57b905499314'
    def mk(ok):return f'<span style="position:absolute;top:8px;right:8px;padding:2px 8px;background:{G if ok else T};color:#fff;{M}">{"Dobre" if ok else "Słabe"}</span>'
    def sample(b,ok,pos,cap):return f'<div><div style="position:relative">{ph(b,100,None,pos)}{mk(ok)}</div><div style="font-size:12.5px;line-height:1.4;color:#333;margin-top:6px">{cap}</div></div>'
    p=lab('37.9–37.11 · Ocena zdjęcia i retusz')+h1('Dobre, słabe, dopuszczalne.',30)
    p+='<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:14px">'+sample(GOOD,True,'50% 40%','Realny kolor cegły, jasny temat, produkt w kontekście wnętrza, bez napisów.')+sample(WEAK,False,'50% 3%','Cegła to tylko fragment kadru. Odbicia w suficie, znak wodny i ciemne elementy odciągają uwagę od produktu.')+'</div>'
    WM=f'<div style="position:relative;width:84px;height:112px;flex:none;background:url(/_blob/{WEAK}) 50% 50%/cover no-repeat #CBCAC4"><div style="position:absolute;left:1px;top:1px;width:50px;height:16px;border:2px solid {T};border-radius:8px"></div><div style="position:absolute;right:1px;bottom:3px;width:56px;height:16px;border:2px solid {T};border-radius:8px"></div></div>'
    p+=f'<div style="margin-top:14px;border:2px solid {T};padding:12px 14px;display:flex;gap:14px;align-items:center">{WM}<div><div style="{M};color:{T}">Ważne · znak wodny</div><div style="font-size:14px;line-height:1.4;color:#111;margin-top:4px;font-weight:500">Nie nanosimy napisu „Ceglany Renesans” na zdjęcia. Jeśli już, to małe logo w rogu — nie napis.</div></div></div>'
    p+=tn(['pokazuje prawdziwy produkt','ma naturalny kolor','pozwala ocenić strukturę','pokazuje zastosowanie','ma jasny temat','nie jest przeładowane','może być użyte w kilku kanałach'],['ma ciężki filtr','nie pokazuje realnego koloru cegły','jest zbyt ciemne lub zbyt jasne','ma nieczytelny kadr','pokazuje za dużo przypadkowych elementów','produkt to mały fragment bez kontekstu','jest dekoracyjne, ale nie wyjaśnia produktu','tekst lub grafika przykrywa najważniejszy fragment'],'Dobre zdjęcie','Słabe zdjęcie',16)
    p+=f'<div style="margin-top:14px">{sub("Dobre kierunki z analizowanych materiałów",T)}{chips(["realizacja z produktem w kontekście wnętrza","przed / po","montaż i proces","detal cegły z widoczną fugą","elewacja w skali budynku","materiał klienta lub wykonawcy z oznaczonym źródłem"],G)}</div>'
    p+=f'<div style="margin-top:16px;border-top:2px solid {T};padding-top:10px">{sub("Retusz i postprodukcja",T)}'+tn(['korekta ekspozycji','korekta balansu bieli','lekkie wyrównanie perspektywy','korekta kontrastu','kadrowanie','usunięcie drobnych elementów technicznych, jeśli nie zmieniają produktu'],['zmiana koloru cegły','„upiększanie” struktury','wygładzanie powierzchni','kopiowanie fragmentów cegły','usuwanie naturalnych różnic','nadmierne HDR','filtry stylizujące materiał na inny produkt'],'Dopuszczalne','Niedopuszczalne',4)+'</div>'
    return p
@fp('061')
def _():
    p=lab('37.12–37.14 · Formaty i kontrola')+h1('Jedna sesja, wiele kanałów.',30)
    p+=para('Przy jednej dobrej sesji realizacji od razu przygotowujemy kadry do wszystkich kanałów.',8)
    p+=f'<div style="margin-top:6px">'+rows([('Poziome','WWW i YouTube'),('Pionowe','Reels, TikTok, Stories'),('Kwadratowe / elastyczne','social media'),('Detale','karty produktów'),('Hero / szeroki plan','strona główna i kategorie'),('Przed / po','jeśli jest dostępny')],6,False)+'</div>'
    p+=box('Zasada','fotografujemy z myślą o wielokanałowym wykorzystaniu, a nie tylko o jednym poście.',12)
    chk=['Czy kolor cegły jest wiarygodny?','Czy widać strukturę?','Czy wiadomo, gdzie produkt jest zastosowany?','Czy zdjęcie ma jeden główny temat?','Czy nic nie przykrywa produktu?','Czy kadr jest prosty i czytelny?','Czy zdjęcie nie jest nadmiernie przefiltrowane?','Czy mamy zgodę lub oznaczenie autora, jeśli materiał jest z zewnątrz?','Czy zdjęcie można połączyć z konkretnym produktem lub realizacją?','Czy obraz pokazuje coś, czego tekst nie musi już opisywać?']
    cl=''.join(f'<div style="display:flex;gap:10px;align-items:flex-start;border-bottom:1px solid {H};padding:5px 0;font-size:12.5px;line-height:1.35;color:#111"><span style="width:13px;height:13px;border:1.5px solid {G};flex:none;margin-top:2px"></span>{c}</div>' for c in chk)
    p+=f'<div style="margin-top:16px">{sub("Checklista przed publikacją zdjęcia",T,2)}{cl}</div>'
    p+=f'<div style="background:{B};padding:12px 16px;margin-top:16px"><div style="{M};color:{G}">Zasada końcowa</div><div style="font-size:14px;line-height:1.45;color:#111;margin-top:4px">Fotografia ma być wiarygodnym dowodem produktu. Nie fotografujemy cegły, żeby wyglądała „ładniej niż w rzeczywistości” — tylko tak, by klient zobaczył, że jest wartościowa właśnie dlatego, że jest prawdziwa, stara i niepowtarzalna.</div></div>'
    return p
def mywrite(n,inner,z):
    path=ig.P+'str-'+n+'.dc.html';s=open(path).read()
    k='<div class="bd tx">' if '<div class="bd tx">' in s else ('<div class="bd">' if '<div class="bd">' in s else '<div style="position:absolute;left:76px;top:100px')
    h=s[:s.index(k)].replace('<span>37 Standard sesji fotograficznej</span>','<span>Część III · 37 Styl fotografii</span>')
    zs=f'zoom:{z};' if z!=1 else ''
    open(path,'w').write(h+f'<div style="position:absolute;left:76px;top:100px;width:{round(642/z)}px;{zs}display:flex;flex-direction:column;gap:0">{inner}</div>'+ig.foot)
if __name__=='__main__':
    def bottom(n):
        o=subprocess.run(['node','pag/fitabs.js','all/project',f'str-{n}.dc.html'],capture_output=True,text=True).stdout
        m=re.search(r'bottom: (\d+)',o);return int(m.group(1)) if m else 9999
    for n in (sys.argv[1:] or sorted(F)):
        p=F[n]();mywrite(n,p,1.0);b=bottom(n)
        z=max(1.0,min(1.4,round(0.985*920/max(b-100,1),2)))
        while True:
            mywrite(n,p,z);b=bottom(n)
            if b<=1022 or z<=1.0:break
            z=round(z-0.02,2)
        print(n,z,b)
