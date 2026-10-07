import re
D='all/project/project/'
M="font-family:'Overpass Mono',monospace;font-size:11px;letter-spacing:.12em;text-transform:uppercase"
tpl=open(D+'str-062.dc.html').read()
head=tpl[:tpl.index('<div class="cr pg">')]
tail=tpl[tpl.index('<div class="ft">'):]
PH='<span style="color:#767676">[do uzupełnienia]</span>'
def li(items,c):
    return '<ul style="list-style:none;margin:0;padding:0;font-size:12.5px;line-height:1.4;color:#333">'+''.join(f'<li style="display:flex;gap:8px;margin:0 0 5px"><span style="color:{c};font-family:\'Overpass Mono\',monospace;flex:none">{"+" if c=="#0D4C73" else "×"}</span><span>{t}</span></li>' for t in items)+'</ul>'
def page(n,num,name,title,fmt,jak,unik,params,rel,vis):
    t=head.replace('<title>Strona 62</title>',f'<title>Strona {n}</title>')
    c=f'<div class="cr pg"><div class="tab">{n}</div><div class="rh"><span>Część IV A · Materiały promocyjne</span><span>Ceglany Renesans</span></div>'
    inner=(f'<div style="{M};letter-spacing:.14em;font-size:12px;color:#ED6842">Materiał {num} · {name}</div>'
     f'<div style="font-family:\'Hanken Grotesk\',sans-serif;font-size:36px;font-weight:300;letter-spacing:-.03em;line-height:1.1;margin-top:10px;color:#111">{title}</div>'
     f'<div style="margin-top:12px"><span style="{M};color:#767676;border:1px dashed #767676;padding:2px 7px">Szkielet · do uzupełnienia</span></div>'
     f'<div style="display:flex;gap:10px;margin-top:16px;font-size:13px;line-height:1.4;color:#333"><span style="{M};color:#767676;flex:none;padding-top:2px">Format</span><span>{fmt}</span></div>'
     f'<div style="display:flex;gap:10px;margin-top:8px;font-size:13px;line-height:1.4;color:#333"><span style="{M};color:#767676;flex:none;padding-top:2px">Cel</span>{PH}</div>'
     f'<div style="border:1px dashed #767676;height:300px;margin-top:16px;display:flex;align-items:center;justify-content:center"><span style="{M};color:#767676">Miejsce na wizualizację · {vis}</span></div>'
     f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:16px"><div><div style="{M};color:#0D4C73;margin-bottom:6px">Stosować</div>{li(jak+[PH],"#0D4C73")}</div><div><div style="{M};color:#ED6842;margin-bottom:6px">Nie stosować</div>{li(unik+[PH],"#ED6842")}</div></div>'
     f'<div style="margin-top:14px;border-top:1px solid #DCDCDC">'+''.join(f'<div style="display:flex;gap:14px;border-bottom:1px solid #DCDCDC;padding:7px 0;font-size:12.5px;color:#333"><span style="{M};color:#0D4C73;width:130px;flex:none;padding-top:1px">{k}</span><span style="color:#767676">[__]</span></div>' for k in params)+'</div>'
     f'<div style="background:#EDE9D0;padding:10px 14px;margin-top:16px"><div style="{M};color:#0D4C73">Przykład</div><div style="font-size:12.5px;line-height:1.45;color:#111;margin-top:3px">{PH}</div></div>'
     f'<div style="margin-top:14px;display:flex;align-items:center;flex-wrap:wrap;gap:4px"><span style="{M};color:#767676;margin-right:8px">Powiązane</span>'+''.join(f'<span style="{M};border:1px solid #0D4C73;color:#0D4C73;padding:2px 7px;margin-right:6px">{r}</span>' for r in rel)+'</div>')
    box=f'<div style="position:absolute;left:76px;top:100px;width:642px;display:flex;flex-direction:column;gap:0">{inner}</div>'
    open(D+f'str-{n:03d}.dc.html','w').write(t+c+box+tail)
page(74,'02','Papier firmowy','Papier firmowy i dokumenty.','A4 · [__ × __ mm]',['papier matowy, naturalny','czerń i jeden akcent #ED6842','logo min. 15 mm (str. 69)'],['folii, złoceń, lakierów wybiórczych','ciemnych teł, ozdobnych ramek'],['Papier','Marginesy','Logo i dane','Podpis i stopka'],['str. 67','str. 69','str. 35'],'A4 pionowo')
page(75,'04','Karty próbek i etykiety','Karty próbek i etykiety.','papier matowy · [__ × __ mm]',['papier naturalny','logo min. 15 mm, czerń i jeden akcent'],['błyszczącej folii, metalicznych farb','ozdobnych ramek'],['Papier','Wymiary','Kolor tła','Dane produktu'],['str. 67','str. 70','str. 37'],'karta próbki / etykieta')
page(76,'07','Materiały sprzedażowe','Oferta, wycena, próbki.','oferta, wycena, próbki · [__]',['karta próbki na beżu #EDE9D0','parametry w mono','kontakt na dole'],['przeładowanych tabel'],['Struktura oferty','Parametry','Kontakt','CTA'],['str. 68','str. 69','str. 153'],'oferta / wycena')
page(77,'08','Karty produktów','Karty produktów.','A4 pionowo i karta online',['zdjęcie produktu','tabela parametrów','uwaga o naturalnych różnicach partii'],['tekstu marketingowego zamiast danych'],['Zdjęcie','Parametry','Uwaga o partiach','CTA'],['str. 68','str. 65','str. 152'],'karta A4 / karta online')
# 067/068 chips
def chipfix(f,reps):
    s=open(D+f).read()
    for a,b in reps:
        assert a in s,(f,a);s=s.replace(a,b,1)
    open(D+f,'w').write(s)
CH=lambda t:f'<span style="{M};border:1px solid #0D4C73;color:#0D4C73;padding:2px 7px;white-space:nowrap;align-self:start">{t}</span>'
s67=open(D+'str-067.dc.html').read()
# second occurrences: item 02 'str. 69', item 04 'str. 70'
i=s67.index('str. 69');j=s67.index('str. 69',i+1);s67=s67[:j]+'str. 69 · 74'+s67[j+7:]
i=s67.index('str. 70');j=s67.index('str. 70',i+1);s67=s67[:j]+'str. 70 · 75'+s67[j+7:]
open(D+'str-067.dc.html','w').write(s67)
s68=open(D+'str-068.dc.html').read()
for k,txt in ((1,'str. 76'),(1,'str. 77')):
    s68=s68.replace('<span></span></div>',CH(txt)+'</div>',1)
open(D+'str-068.dc.html','w').write(s68)
print(s68.count('str. 76'),s68.count('str. 77'))
