import json,re
d=json.load(open('build/fb.json'));E=d['entries']
P='all/project/project/'
tpl=open(P+'p126b.dc.html').read()
head=tpl[:tpl.index('<div style="position:absolute')]
M="font-family:'Overpass Mono',monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase"
groups=[E[0:2],E[2:4],E[4:6],E[6:8],E[8:10],E[10:12],E[12:14],E[14:16],E[16:18],E[18:19]]
names=['p126b','p127','p128','p129','p130','p131','p131b','p131c','p131d','p131e']
for i,(g,n) in enumerate(zip(groups,names)):
    if i<7: continue
    body=''
    y0=100
    if i==0:
        body+=f'<div style="position:absolute;left:76px;top:100px;width:642px"><div style="{M};letter-spacing:.14em;color:#ED6842">A · Biblioteka źródeł</div><div style="font-family:\'Hanken Grotesk\',sans-serif;font-size:36px;font-weight:300;letter-spacing:-.03em;line-height:1.1;margin-top:10px">Facebook.</div></div>'
        y0=190;slot=420
    else: slot=430
    for k,e in enumerate(g):
        top=y0+k*slot
        body+=f'<div style="position:absolute;left:76px;top:{top}px;width:642px;border-top:1px solid #E7DFC9"></div>'
        body+=f'<div style="position:absolute;left:76px;top:{top+16}px;width:250px;height:{slot-52}px;box-sizing:border-box;border:1px dashed #BDB7A0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;text-align:center;padding:12px"><div style="{M};color:#0D4C73">Miejsce na screen</div><div style="font-size:12px;line-height:1.4;color:#767676;word-break:break-word">{e["code"]}<br/>{e["fn"]}</div></div>'
        body+=f'<div style="position:absolute;left:346px;top:{top+16}px;width:372px">{e["html"]}</div>'
    t=head+body+'<div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n</x-dc><script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":794,"height":1123}}\'>class Component extends DCLogic{renderVals(){return {};}}</script></body></html>'
    t=re.sub(r'class="tab">\d+<',f'class="tab">{141+i}<',t,1)
    t=re.sub(r'<title>[^<]*</title>',f'<title>Strona {141+i}</title>',t)
    open(P+n+'.dc.html','w').write(t)
