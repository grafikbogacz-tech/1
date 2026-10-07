import sys,json;sys.path.insert(0,'build')
from ig import *
Z=json.load(open('build/gbpz.json')) if len(sys.argv)>1 else {}
def W(n,inner,gap=16):write(n,inner,gap,Z.get(n,1))
L='B · Google Business Profile'
def table(rows,cols_w,head=None,fs=12.5,bold0=True):
    g=' '.join(cols_w);o=''
    if head:o+=f'<div style="display:grid;grid-template-columns:{g};gap:0 14px;border-bottom:2px solid {T};padding:0 0 6px">'+''.join(f'<div style="{M};color:{G}">{h}</div>' for h in head)+'</div>'
    for r in rows:
        o+=f'<div style="display:grid;grid-template-columns:{g};gap:0 14px;border-bottom:1px solid {H};padding:8px 0">'
        for i,c in enumerate(r):
            if i==0 and bold0:o+=f'<div style="font-size:13.5px;font-weight:500;color:#111;letter-spacing:-.01em">{c}</div>'
            elif isinstance(c,list):o+=f'<div style="font-size:{fs}px;line-height:1.4;color:#333">'+''.join(f'<div style="display:flex;gap:6px;margin-bottom:2px"><span style="color:{G};{MF};flex:none">·</span><span>{x}</span></div>' for x in c)+'</div>'
            else:o+=f'<div style="font-size:{fs}px;line-height:1.4;color:#333">{c}</div>'
        o+='</div>'
    return o
def stat(n,t,mt=0):return f'<div style="border-top:2px solid {T};padding-top:8px"><div style="{MF};font-weight:300;font-size:34px;letter-spacing:-.05em;color:{T};line-height:1">{n}</div><div style="font-size:12.5px;line-height:1.4;color:#333;margin-top:4px">{t}</div></div>'
def grid(items,n,gap=14,mt=12):return f'<div style="display:grid;grid-template-columns:repeat({n},1fr);gap:{gap}px;margin-top:{mt}px">'+''.join(items)+'</div>'
def src(t):return f'<div style="font-size:11.5px;line-height:1.4;color:#767676;margin-top:8px">{t}</div>'
# ---------- 163
p=lab(L)+h1('Pierwszy kontakt z marką, zanim klient wejdzie na stronę.',30)
p+=para('Wizytówka wyświetla się w wynikach lokalnych i w Mapach Google. Odbiorca ocenia w kilka sekund, czy firma jest aktywna, wiarygodna i prawdziwa, i dopiero potem przechodzi do strony.',10)
p+=f'<div style="margin-top:20px">{sub("Co klient widzi w wizytówce",T)}'+grid([stat(a,b) for a,b in [('01','nazwa i kategoria firmy'),('02','adres, godziny, telefon, link do strony'),('03','zdjęcia i filmy (realizacje, produkt, proces)'),('04','opinie i odpowiedzi marki'),('05','wpisy: aktualności, oferty, wydarzenia'),('06','linki do kanałów społecznościowych')]],3,14,0)+'</div>'
p+=f'<div style="margin-top:26px">{sub("Sześć celów wizytówki Ceglanego Renesansu",T)}'+table([('1','Widoczność w wynikach lokalnych i w Mapach Google.'),('2','Dowód, że firma jest aktywna i dostępna (aktualne dane, regularne wpisy).'),('3','Łatwy kontakt i dotarcie: telefon, adres, godziny.'),('4','Realne realizacje i produkty: zdjęcia, nie grafiki.'),('5','Wiarygodność: opinie i odpowiedzi marki.'),('6','Przejście dalej: strona, kontakt, sklep lub odwiedziny w firmie.')],['26px','1fr'])+'</div>'
p+=box('Punkt wyjścia','wizytówka wymaga uporządkowania, nie budowy od nowa. Zachowujemy to, co działa, uzupełniamy braki i ustawiamy proste zasady prowadzenia (kolejne strony). Przykłady z wizytówki i oceny: GBP-01 – GBP-08, strony 168–175.',22)
W('p132',p,0)
# ---------- 164
types=[('Aktualność','informacja o firmie, produkcie, realizacji, nowym artykule lub zmianie','codzienna praca z profilem: realizacje, porady, proces, nowe materiały','tekst, zdjęcie lub film, przycisk'),
('Oferta','promocja z terminem i warunkami','tylko konkretny produkt z warunkiem i datą końca','tytuł do 58 znaków, daty, warunki'),
('Wydarzenie','komunikat z datą rozpoczęcia i zakończenia','pokazy, dni otwarte, targi, szkolenia dla wykonawców','tytuł do 58 znaków, data i godzina')]
p=lab(L+' · wpisy')+h1('Trzy typy wpisów i konkretne limity.',30)
p+=f'<div style="margin-top:16px">{table(types,["96px","1fr","1fr","1fr"],["Typ","Do czego","Kiedy używamy","Wymaga"],12)}</div>'
p+=f'<div style="margin-top:22px">{sub("Limity techniczne",T)}'+grid([stat('1500','znaków w treści wpisu; zalecana długość 150–300'),stat('58','znaków w tytule oferty lub wydarzenia'),stat('4:3','proporcja zdjęcia we wpisie, min. 400 × 300 px'),stat('7 dni','tyle wpis jest widoczny na wierzchu profilu, potem trafia do archiwum wpisów')],4,14,0)+'</div>'
p+=src('Limity wg dokumentacji Google Business Profile; przed publikacją sprawdź je w panelu, bo Google je zmienia.')
p+=f'<div style="margin-top:22px">{sub("Przycisk we wpisie → podstrona",T)}'+table([('Dowiedz się więcej','karta produktu, realizacja lub artykuł (nigdy strona główna)'),('Kup / Zamów online','kategoria sklepu lub konkretny produkt'),('Zadzwoń','tylko gdy wpis dotyczy kontaktu lub wyceny'),('Zarejestruj się','wydarzenie z zapisami')],['150px','1fr'],None,12)+'</div>'
W('p133',p,0)
# ---------- 165
ex='Płytki RETRO w kuchni — jak wyglądają na większej powierzchni? W nowej realizacji pokazujemy je z fugą piaskową i naturalnym drewnem. Zobacz całą realizację i parametry produktu na stronie.'
p=lab(L+' · budowa wpisu')+h1('Anatomia wpisu: sześć elementów.',30)
p+=steps([('01','Konkret lub problem klienta (pierwsze zdanie)'),('02','Produkt, realizacja lub odpowiedź'),('03','Krótki kontekst: dlaczego to ważne')],14)
p+=steps([('04','Jeden kierunek działania'),('05','Jedno CTA'),('06','Link do najlepiej dopasowanej podstrony')],10)
p+=box(f'Przykład · {len(ex)} znaków',f'„{ex}”<br>CTA: „Dowiedz się więcej” → podstrona konkretnego produktu lub realizacji.',20)
p+=f'<div style="margin-top:22px">{sub("Wpis → dokąd prowadzi link",T)}'+table([('Produkt','karta produktu'),('Realizacja','realizacja lub powiązany produkt'),('Poradnik','właściwy artykuł'),('Oferta','strona z warunkami promocji'),('Informacja lokalna','kontakt lub odpowiednia podstrona')],['130px','1fr'])+'</div>'
p+=f'<div style="margin-top:22px">{sub("Media: wymagania Google",T)}'+table([('Zdjęcia profilu','JPG lub PNG, 10 KB – 5 MB, zalecane 720 × 720 px, min. 250 × 250 px'),('Zdjęcie we wpisie','proporcja 4:3, min. 400 × 300 px'),('Wideo','do 30 s, do 75 MB, min. 720p')],['130px','1fr'])+'</div>'
p+=src('Specyfikacje wg pomocy Google Business Profile. Zdjęcie ma odpowiadać rzeczywistości: bez mocnych filtrów i bez zmiany koloru cegły.')
W('p134',p,0)
# ---------- 166
pri=['nowe realizacje','konkretne produkty i ich zastosowanie','porady: wybór, montaż, fugowanie, impregnacja, pielęgnacja','nowe artykuły i poradniki ze strony','proces produkcji i pochodzenie cegły','nowe zdjęcia partii materiału','pytania klientów','opinie i dowody zewnętrzne','aktualne oferty i promocje','ważne informacje organizacyjne']
dont=['kopiowania posta z Facebooka 1:1','wpisów bez celu','samego hasła promocyjnego bez produktu','wielu CTA w jednym wpisie','kilku numerów telefonu w treści','niezweryfikowanych danych kontaktowych','mocno przefiltrowanych zdjęć','nieaktualnych informacji','linków wszystkich wpisów na stronę główną']
p=lab(L+' · treści i rytm')+h1('Co publikować, czego unikać, jak często.',30)
p+=grid([stat('1','wartościowy wpis tygodniowo, minimum'),stat('2','wpisy tygodniowo, gdy jest więcej nowości'),stat('+1','wpis przy każdej ważnej nowości na stronie')],3,14,16)
p+=para('Nie publikujemy dla samej regularności. Jeśli nie ma wartościowego tematu, lepiej mniej, ale konkretnie.',10)
p+=cols(sub('Priorytetowe treści')+li(pri,'+',G,12.5,3),sub('Nie stosować',T)+li(dont,'×',T,12.5,3),14,22)
p+=box('CTA i kontakt','jeden wpis = jedno główne działanie. Numer telefonu bierzemy z danych i przycisku profilu, nie wpisujemy go kilka razy w treści.',18)
W('p135',p,0)
# ---------- 167
resp='Dziękujemy za opinię i zdjęcia! Cieszymy się, że płytki Rustykalne Loft sprawdziły się w Państwa kuchni. Gdyby przy fugowaniu pojawiły się pytania, służymy pomocą.'
chk=['godziny otwarcia','numer telefonu','adres','strona internetowa','kategorie','zdjęcia','aktualne wpisy','opinie i zgłoszone zmiany']
wk=[('Tydz. 1','realizacja lub produkt'),('Tydz. 2','porada / odpowiedź na pytanie klienta'),('Tydz. 3','proces, autentyczność, producent'),('Tydz. 4','realizacja, opinia, artykuł lub oferta')]
wkh=''.join(f'<div style="border-top:2px solid {T};padding-top:8px"><div style="{M};color:{T}">{a}</div><div style="font-size:13px;line-height:1.35;color:#111;margin-top:4px">{b}</div></div>' for a,b in wk)
p=lab(L+' · opinie i aktualność')+h1('Opinie, kontrola profilu, rytm miesięczny.',28)
p+=card('09','Opinie',cols(li(['odpowiadamy na każdą opinię,','odpowiedź krótka, konkretna, naturalna,','nie kopiujemy jednej odpowiedzi do wszystkich,'],'+',G),li(['przy pytaniu odpowiadamy merytorycznie,','negatywnej opinii nie ignorujemy, gdy można odpowiedzieć rzeczowo.'],'+',G),8)+box('Przykład odpowiedzi',f'„{resp}”',8),12)
p+=card('10','Kontrola profilu — raz w miesiącu',f'<div style="margin-top:10px">{chips(chk)}</div>'+para('Wizytówka nie jest dokumentem „ustaw i zapomnij”.',8),12)
p+=card('11','Rytm miesięczny — wersja minimum',grid([wkh],1,0,0).replace('repeat(1,1fr)','1fr').replace('<div style="border-top:2px','<div style="display:contents"><div style="border-top:2px',0) if False else f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:12px">{wkh}</div>'+para('Dodatkowy wpis zawsze, gdy na stronie pojawia się ważna aktualność.',10),12)
p+=card('12','Powiązanie z innymi kanałami',para('Dodajemy linki do aktywnych kanałów: Facebook, Instagram, YouTube. Wizytówka nie jest kopią social mediów — wspiera decyzję klienta, który już szuka firmy, produktu lub rozwiązania.',8),12)
p+=f'<div style="font-size:12px;line-height:1.5;color:#767676;margin-top:12px;border-top:1px solid {H};padding-top:8px">Przykłady wpisów z wizytówki: GBP-01 – GBP-08 (strony 168–175). Schemat wpisu w bibliotece: kod, nazwa pliku, typ materiału, krótki opis, powiązane zasady, wniosek.</div>'
W('p136',p,0)
