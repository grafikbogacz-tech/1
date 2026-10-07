import json,re
d=json.load(open('build/fb.json'));E=d['entries']
P='all/project/project/'
tpl=open(P+'p126b.dc.html').read()
head=tpl[:tpl.index('<div style="position:absolute')]
M="font-family:'Overpass Mono',monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase"
groups=[E[i:i+2] for i in range(0,18,2)]
names=['p126b','p127','p128','p129','p130','p131','p131b','p131c','p131d']
for i,(g,n) in enumerate(zip(groups,names)):
    body=''
    y0=100
    if i==0:
        body+=f'<div style="position:absolute;left:76px;top:100px;width:642px"><div style="{M};letter-spacing:.14em;color:#ED6842">A · Biblioteka źródeł</div><div style="font-family:\'Hanken Grotesk\',sans-serif;font-size:36px;font-weight:300;letter-spacing:-.03em;line-height:1.1;margin-top:10px">Facebook.</div></div>'
        y0=190;slot=420
        body+=f'<div style="position:absolute;left:318px;top:102px;width:400px;text-align:right;font-family:\'Overpass Mono\',monospace;font-size:12px;line-height:1.5;color:#767676">Ocena redakcyjna na podstawie wniosku:<br/>Super 85–100% · Dobry 65–84% · Do poprawy &lt;65%</div>'
    else: slot=430
    for k,e in enumerate(g):
        top=y0+k*slot
        body+=f'<div style="position:absolute;left:76px;top:{top}px;width:642px;border-top:1px solid #E7DFC9"></div>'
        body+=f'<img src="/_blob/{e["img"]}" alt="{e["code"]}" style="position:absolute;left:76px;top:{top+16}px;width:250px;height:auto;border:1px solid #E7DFC9;display:block">'
        body+=f'<div style="position:absolute;left:346px;top:{top+16}px;width:372px">{e["html"]}</div>'
    t=head+body+'<div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n</x-dc><script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":794,"height":1123}}\'>class Component extends DCLogic{renderVals(){return {};}}</script></body></html>'
    t=re.sub(r'class="tab">\d+<',f'class="tab">{141+i}<',t,1)
    t=re.sub(r'<title>[^<]*</title>',f'<title>Strona {141+i}</title>',t)
    open(P+n+'.dc.html','w').write(t)
