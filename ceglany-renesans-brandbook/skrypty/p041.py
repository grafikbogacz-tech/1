src=open('../../build/osob.py').read().split('# ---------- page 1')[0]
exec(src)
LNN=LN
def write2(fn,parts,num,ttl,rh,gap=22):
    html=HEAD0.replace('25 Logo na tle',ttl)+f'<div class="cr pg"><div class="tab">{num}</div><div class="rh"><span>{rh}</span><span>Ceglany Renesans</span></div><div class="fl" style="position:absolute;left:76px;top:100px;width:642px;display:flex;flex-direction:column;gap:{gap}px">'+''.join(parts)+'</div><div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n'+TAIL
    open('flow/'+fn,'w').write(html)
P=title('32 · Typografia','Font uzupełniający / systemowy.','Rozwiązania zastępcze (fallback web-safe) na sytuacje, w których kroje marki nie są dostępne: e-mail, dokumenty Office, prezentacje, strony bez osadzonych fontów.')
th=lambda t,r=True:f'<th style="text-align:left;font-weight:400;color:{NV};font-size:13px;padding:12px 12px;border-bottom:2px solid {OR};{"border-right:1px solid "+LN+";" if r else ""}">{t}</th>'
def td(t,r=True,last=False,mono=False):
    f="font-family:'Overpass Mono',monospace;font-size:12px;" if mono else ''
    return f'<td style="padding:12px 12px;vertical-align:top;color:#333;{f}{"border-right:1px solid "+LN+";" if r else ""}{"" if last else "border-bottom:1px solid "+LN+";"}">{t}</td>'
rows=[('Nagłówki i tekst','Hanken Grotesk','Arial, Helvetica, sans-serif'),('Etykiety, numery, parametry','Overpass Mono','&quot;Courier New&quot;, Consolas, monospace'),('Logo','Boulevard Saint Denis i Montserrat Bold','nie zastępujemy: używamy tylko plików logo')]
tb=(f'<table data-a style="width:642px;border-collapse:collapse;border:1px solid {LN};{H}font-size:13px;line-height:1.5"><tr>{th("Zastosowanie")}{th("Krój marki")}{th("Zapas (fallback)",False)}</tr>'
 +''.join('<tr>'+td(a)+td(b)+td(c,False,i==len(rows)-1,mono=(i<2))+'</tr>' for i,(a,b,c) in enumerate(rows)).replace('border-bottom:1px solid '+LN+';','border-bottom:1px solid '+LN+';')+'</table>')
P.append(tb)
P.append('<div style="display:grid;grid-template-columns:313px 313px;gap:16px">'+D(lab('Stosować',NV)+f'<div style="{TXT}">{ul(["zapas tylko wtedy, gdy kroju marki nie da się osadzić,","Arial lub Helvetica zamiast Hanken Grotesk,","Courier New lub Consolas zamiast Overpass Mono, tylko dla etykiet i numerów,","tę samą hierarchię rozmiarów i odstępów co w kroju marki."])}</div>')+D(lab('Nie stosować',OR)+f'<div style="{TXT}">{ul(["Times New Roman, Comic Sans i innych przypadkowych krojów,","krojów ozdobnych lub pisanych,","kroju zapasowego do odtwarzania logo,","Montserrata poza logo."])}</div>')+'</div>')
P.append(D(f'<div style="border-top:1px solid {LN};padding-top:12px;{TXT}color:#767676">To rekomendacja wdrożeniowa. Źródłowa Księga Znaku nie definiuje fontów zapasowych.</div>','',642))
write2('p041.dc.html',P,50,'Typografia: font uzupełniający / systemowy','Część III · 32 Typografia: font systemowy')
