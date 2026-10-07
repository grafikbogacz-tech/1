import json,re
d=json.load(open('build/fbcards.json'));P='all/project/project/'
M="font-family:'Overpass Mono',monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase"
base=open(P+'p066.dc.html').read()
head=base[:base.index('<div class="bd tx">')] if '<div class="bd tx">' in base else base[:base.index('<div style="position:absolute;left:76px;top:100px')]
foot='<div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n</x-dc><script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":794,"height":1123}}\'>class Component extends DCLogic{renderVals(){return {};}}</script></body></html>'
def lab(t):return f'<div style="{M};color:#ED6842">{t}</div>'
def page(inner):return head+f'<div style="position:absolute;left:76px;top:100px;width:642px;display:flex;flex-direction:column;gap:22px">{inner}</div>'+foot
pages=[]
pages.append('<div>'+d['over'].replace('@@FB@@','156–164')+'</div>')
cs=d['cards']
for i in range(0,10,2):
    pages.append(lab('44.1 · Facebook · typy postów')+'<div style="display:flex;flex-direction:column;gap:22px">'+cs[i]+cs[i+1]+'</div>')
rc=d['rcards']
pages.append(lab('44.1 · Facebook · standard wizualny i redakcyjny')+'<div style="display:flex;flex-direction:column;gap:16px">'+''.join(rc[0:3])+'</div>')
pages.append(lab('44.1 · Facebook · standard wizualny i redakcyjny')+'<div style="display:flex;flex-direction:column;gap:12px">'+''.join(rc[3:7])+'</div>')
ch=d['checklist'];i=ch.index('<div style="border-top');
pages.append('<div>'+ch[:i]+'<div style="margin-top:18px">'+rc[7]+'</div>'+ch[i:]+'</div>')
names=['p066','p067','p068','p069','p070','p071','p072','p073','p074']
assert len(pages)==9
for n,pg in zip(names,pages):
    s=open(P+n+'.dc.html').read();h=s[:s.index('<div class="bd tx">')] if '<div class="bd tx">' in s else s[:s.index('<div style="position:absolute;left:76px;top:100px')]
    html=h+f'<div style="position:absolute;left:76px;top:100px;width:642px;display:flex;flex-direction:column;gap:14px">{pg}</div>'+foot
    open(P+n+'.dc.html','w').write(html)
print('ok')
