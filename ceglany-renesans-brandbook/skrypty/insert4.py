import re,json,os,glob
D='all/project/project/';SH=4;FIRST=74
tpat=re.compile(r'(?i)(?<![\w])(str\.|stron[aąęyie]*|strony)(\s*)(\d+)(?:(\s*[–\-]\s*)(\d+))?')
def sh(n):return n+SH if n>=FIRST else n
def fix_ref(m):
    a=sh(int(m.group(3)));out=f'{m.group(1)}{m.group(2)}{a}'
    if m.group(5):out+=f'{m.group(4)}{sh(int(m.group(5)))}'
    return out
def fix_text(t):return tpat.sub(fix_ref,t)
numcell=re.compile(r'^(\s*\d+(\s*[–\-]\s*\d+)?\s*)(,\s*\d+(\s*[–\-]\s*\d+)?\s*)*$')
def fix_numcell(t):
    return re.sub(r'\d+',lambda m:str(sh(int(m.group(0)))),t)
def transform(s,toc):
    parts=re.split(r'(<[^>]*>)',s);out=[];intag_style=False
    for p in parts:
        if p.startswith('<'):
            out.append(p);ls=p.lower()
            if ls.startswith('<style') or ls.startswith('<script'):intag_style=True
            if ls.startswith('</style') or ls.startswith('</script'):intag_style=False
            continue
        if intag_style or not p.strip():out.append(p);continue
        q=fix_text(p)
        if toc and numcell.match(p):q=fix_numcell(p)
        out.append(q)
    return ''.join(out)
def set_tab(s,n):return re.sub(r'<div class="tab">\d+</div>',f'<div class="tab">{n}</div>',s,1)
if __name__=='__main__':
    files=sorted(glob.glob(D+'str-*.dc.html'));N=len(files);assert N==231
    # 1) rewrite refs in pages < FIRST (in place)
    for n in range(1,FIRST):
        f=D+f'str-{n:03d}.dc.html';s=open(f).read();open(f,'w').write(transform(s,n in (3,4,5)))
    # 2) shift pages >= FIRST, descending
    for n in range(N,FIRST-1,-1):
        s=open(D+f'str-{n:03d}.dc.html').read();m=n+SH
        s=transform(s,False);s=set_tab(s,m)
        open(D+f'str-{m:03d}.dc.html','w').write(s)
    # 3) canvas
    c=json.load(open(D+'canvas.json'));tot=N+SH
    names=[f'str-{i:03d}.dc.html' for i in range(1,tot+1)]
    c['boards']={nm:{'h':1123,'title':f'Strona {i+1}','w':794,'x':(i%6)*874,'y':(i//6)*1243} for i,nm in enumerate(names)}
    c['order']=names;json.dump(c,open(D+'canvas.json','w'),ensure_ascii=False,separators=(', ',': '))
    print('done',tot)
