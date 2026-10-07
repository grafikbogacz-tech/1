import json,re,html
b=json.load(open('/tmp/fb_blocks.json'))
M="font-family:'Overpass Mono',monospace;font-size:11px;letter-spacing:.12em;text-transform:uppercase"
def txt(h):
    h=re.sub(r'<br/?>','\n',h);h=re.sub(r'<[^>]*>','',h);return html.unescape(h).strip()
def lis(h):return [txt(x) for x in re.findall(r'<li>([\s\S]*?)</li>',h)]
def esc(t):return html.escape(t).replace('\n','<br/>')
# --- types
types=[];cur=None
for i in range(5,85):
    x=b[i]
    if x.startswith('<h3'):
        m=re.match(r'(\d+)\.\s*(.*)',txt(x));cur=dict(n=int(m.group(1)),title=m.group(2),cel='',st=[],nie=[],ex='',src=[],srcnote='');types.append(cur);mode=None;continue
    t=txt(x)
    if x.startswith('<p'):
        if t.startswith('Cel:'):cur['cel']=t[4:].strip()
        elif t.startswith('Stosować'):mode='st'
        elif t.startswith('Nie stosować'):mode='nie'
        elif t.startswith('Przykład źródłowy') or t.startswith('Przykłady źródłowe'):
            codes=re.findall(r'FB-\d+',t)
            cur['src']=codes
            if not codes:cur['srcnote']='brak mocnego wzorca — typ do rozwinięcia'
        elif t.startswith('Przykład'):cur['ex']=t.split('\n',1)[1].strip() if '\n' in t else t[9:].strip()
    elif x.startswith('<ul'):
        cur[mode]=lis(x)
short={1:'Realizacje',2:'Poradniki i wiedza',3:'Pytania klientów / FAQ',4:'Wybór produktu i próbka',5:'Historia materiału',6:'Proces produkcji',7:'Dowód zewnętrzny',8:'Inspiracje i przed / po',9:'Ludzie i kulisy',10:'Sprzedaż, promocje, CTA'}
# renumber FB codes: already FB-xx current numbering from text
def card(t):
    L=''.join(f'<li style="display:flex;gap:8px;margin:0 0 5px"><span style="color:#0D4C73;font-family:\'Overpass Mono\',monospace;flex:none">+</span><span>{esc(x)}</span></li>' for x in t['st'])
    R=''.join(f'<li style="display:flex;gap:8px;margin:0 0 5px"><span style="color:#ED6842;font-family:\'Overpass Mono\',monospace;flex:none">×</span><span>{esc(x)}</span></li>' for x in t['nie'])
    chips=''.join(f'<span style="{M};font-size:11px;border:1px solid #0D4C73;color:#0D4C73;padding:2px 7px;margin-right:6px">{c}</span>' for c in t['src']) or f'<span style="{M};font-size:11px;border:1px dashed #BDB7A0;color:#767676;padding:2px 7px">{esc(t["srcnote"])}</span>'
    return f'''<div style="border-top:1px solid #E7DFC9;padding-top:14px">
<div style="display:flex;gap:14px;align-items:baseline"><span style="font-family:'Overpass Mono',monospace;font-weight:300;font-size:38px;letter-spacing:-.05em;color:#ED6842;line-height:1">{t['n']:02d}</span><span style="font-size:21px;font-weight:500;letter-spacing:-.025em;line-height:1.15;color:#111">{esc(t['title'])}</span></div>
<div style="display:flex;gap:10px;margin-top:8px;font-size:13px;line-height:1.4;color:#333"><span style="{M};color:#767676;flex:none;padding-top:2px">Cel</span><span>{esc(t['cel'])}</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:12px"><div><div style="{M};color:#0D4C73;margin-bottom:6px">Stosować</div><ul style="list-style:none;margin:0;padding:0;font-size:12.5px;line-height:1.4;color:#333">{L}</ul></div><div><div style="{M};color:#ED6842;margin-bottom:6px">Nie stosować</div><ul style="list-style:none;margin:0;padding:0;font-size:12.5px;line-height:1.4;color:#333">{R}</ul></div></div>
<div style="background:#EDE9D0;padding:10px 14px;margin-top:8px"><div style="{M};color:#0D4C73">Przykład</div><div style="font-size:12.5px;line-height:1.45;color:#111;margin-top:3px">{esc(t['ex'])}</div></div>
<div style="margin-top:10px;display:flex;align-items:center;flex-wrap:wrap;gap:4px"><span style="{M};color:#767676;margin-right:8px">Przykłady z biblioteki</span>{chips}</div></div>'''
cards=[card(t) for t in types]
# overview
def tile(t):
    return f'<div style="border-top:1px solid #E7DFC9;padding:10px 0 12px"><div style="font-family:\'Overpass Mono\',monospace;font-weight:300;font-size:26px;letter-spacing:-.05em;color:#ED6842;line-height:1">{t["n"]:02d}</div><div style="font-size:15px;font-weight:500;letter-spacing:-.02em;margin-top:6px;color:#111">{short[t["n"]]}</div><div style="font-size:12px;line-height:1.4;color:#555;margin-top:4px">{esc(t["cel"])}</div></div>'
over=f'''<div style="{M};letter-spacing:.14em;color:#ED6842">44.1 · Facebook</div><div style="font-family:'Hanken Grotesk',sans-serif;font-size:36px;font-weight:300;letter-spacing:-.03em;line-height:1.1;margin-top:10px">Dziesięć typów postów.</div>
<div style="font-size:13px;line-height:1.5;color:#333;margin-top:10px">Każdy post należy do jednego głównego typu komunikacji. Dodatkowy cel może być wtórny, ale nie mieszamy kilku równorzędnych komunikatów w jednym materiale. Karta typu: cel → stosować → nie stosować → przykład → przykłady z biblioteki.</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 26px;margin-top:14px">{''.join(tile(t) for t in types)}</div>
<div style="border-left:3px solid #ED6842;background:#EDE9D0;padding:10px 14px;margin-top:16px"><div style="{M};color:#0D4C73">Luki do uzupełnienia</div><div style="font-size:12.5px;line-height:1.45;color:#111;margin-top:3px">Najmniej reprezentowane są proces produkcji, wybór i porównanie produktu oraz próbka jako narzędzie decyzji. To braki w materiale źródłowym i planie treści, nie w Brand Booku. Te trzy obszary powinny dostać własne serie.</div></div>
<div style="font-size:12.5px;color:#767676;margin-top:12px">Zrzuty ekranu i oceny postów: biblioteka źródeł, część VII, sekcja A „Facebook” (FB-01 – FB-18), strony @@FB@@.</div>'''
# --- standard rules
rules=[];cur=None
for i in range(89,140):
    x=b[i]
    if x.startswith('<h3'):
        t=txt(x);m=re.match(r'(\d+)\.\s*(.*)',t)
        cur=dict(n=int(m.group(1)),title=m.group(2),secs=[],text=[]);rules.append(cur);label=None;continue
    if cur is None:continue
    t=txt(x)
    if x.startswith('<p'):
        if t.endswith(':') and len(t)<40:label=t[:-1]
        elif t.startswith('Zasada'):cur['text'].append(('zasada',t.split(':',1)[1].strip()))
        else:cur['text'].append(('p',t))
    elif x.startswith('<ul'):cur['secs'].append((label or '',lis(x)))
rules=[r for r in rules if r['n']<=8]
for r in rules:print(r['n'],r['title'],[(l,len(v)) for l,v in r['secs']],[k for k,_ in r['text']])
def rcard(r):
    st=next((v for l,v in r['secs'] if l.startswith(('Stosować','Rekomendowany układ'))),[]);nie=next((v for l,v in r['secs'] if l.startswith('Nie stosować')),[])
    oth=[(l,v) for l,v in r['secs'] if not l.startswith(('Stosować','Nie stosować','Rekomendowany układ'))]
    L=''.join(f'<li style="display:flex;gap:7px;margin:0 0 4px"><span style="color:#0D4C73;font-family:\'Overpass Mono\',monospace;flex:none">+</span><span>{esc(x)}</span></li>' for x in st)
    R=''.join(f'<li style="display:flex;gap:7px;margin:0 0 4px"><span style="color:#ED6842;font-family:\'Overpass Mono\',monospace;flex:none">×</span><span>{esc(x)}</span></li>' for x in nie)
    O=''.join(f'<div style="margin-top:8px"><span style="{M};color:#0D4C73">{esc(l)}</span><div style="font-size:12.5px;line-height:1.4;color:#333;margin-top:2px">'+' · '.join(esc(x.rstrip(',;.')) for x in v)+'</div></div>' for l,v in oth)
    T=''.join(f'<div style="background:#EDE9D0;padding:8px 12px;margin-top:8px;font-size:12.5px;line-height:1.4;color:#111"><span style="{M};color:#0D4C73">{"Zasada" if k=="zasada" else "Uwaga"}</span> {esc(x)}</div>' if k=='zasada' else f'<div style="font-size:12.5px;line-height:1.4;color:#333;margin-top:6px">{esc(x)}</div>' for k,x in r['text'])
    cols=''
    if L or R: cols=f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:8px"><div><ul style="list-style:none;margin:0;padding:0;font-size:12.5px;line-height:1.4;color:#333">{L}</ul></div><div><ul style="list-style:none;margin:0;padding:0;font-size:12.5px;line-height:1.4;color:#333">{R}</ul></div></div>'
    return f'''<div style="border-top:1px solid #E7DFC9;padding-top:12px"><div style="display:flex;gap:12px;align-items:baseline"><span style="font-family:'Overpass Mono',monospace;font-weight:300;font-size:28px;letter-spacing:-.05em;color:#ED6842;line-height:1">{r['n']:02d}</span><span style="font-size:18px;font-weight:500;letter-spacing:-.02em;color:#111">{esc(r['title'])}</span></div>{cols}{O}{T}</div>'''
rcards=[rcard(r) for r in rules]
chk=lis(b[142])
checklist=f'''<div style="{M};letter-spacing:.14em;color:#ED6842">44.1 · Facebook</div><div style="font-family:'Hanken Grotesk',sans-serif;font-size:36px;font-weight:300;letter-spacing:-.03em;line-height:1.1;margin-top:10px">Zasada i checklista.</div>
<div style="border-top:1px solid #E7DFC9;margin-top:18px;padding-top:14px"><div style="{M};color:#0D4C73">Zasada nadrzędna dla zdjęć</div><div style="font-size:24px;font-weight:300;letter-spacing:-.03em;line-height:1.2;color:#111;margin-top:8px">Zdjęcie produktu lub realizacji pokazuje prawdziwy kolor, strukturę i kontekst materiału. Nie projektujemy grafiki tak, żeby przykryć najważniejszy dowód marki: samą cegłę.</div></div>
<div style="border-top:1px solid #E7DFC9;margin-top:24px;padding-top:14px"><div style="{M};color:#0D4C73">Checklista przed publikacją</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px 24px;margin-top:12px">{''.join(f'<div style="display:flex;gap:10px;align-items:flex-start;font-size:13px;line-height:1.4;color:#333"><span style="width:16px;height:16px;border:1.5px solid #0D4C73;flex:none;margin-top:1px"></span><span>{esc(x)}</span></div>' for x in chk)}</div></div>'''
json.dump(dict(over=over,cards=cards,rcards=rcards,checklist=checklist),open('build/fbcards.json','w'),ensure_ascii=False)
