import re,json,glob
D='all/project/project/'
def f(n):
    if 36<=n<=72:return n+1
    if n==73:return 36
    return n
def gsec(n):return n-1 if 46<=n<=61 else n
tpat=re.compile(r'(?i)(?<![\w])(str\.|stron[aąęyie]*|strony)(\s*)(\d+)(?:(\s*[–\-]\s*)(\d+))?')
def fix_ref(m):
    out=f'{m.group(1)}{m.group(2)}{f(int(m.group(3)))}'
    if m.group(5):out+=f'{m.group(4)}{f(int(m.group(5)))}'
    return out
sec1=re.compile(r'^(\s*)(4[6-9]|5\d|6[01])((?:\.\d)?)(?= · | [A-ZŁŚŻĆŹ])')
sec2=re.compile(r'(?<=· )(4[6-9]|5\d|6[01])((?:\.\d)?)(?= [A-ZŁŚŻĆŹ])')
sec3=re.compile(r'(?i)(sekcj\w*\s+)(4[6-9]|5\d|6[01])((?:\.\d)?)')
log=set()
def gs(t):
    o=t
    t=sec1.sub(lambda m:f'{m.group(1)}{gsec(int(m.group(2)))}{m.group(3)}',t)
    t=sec2.sub(lambda m:f'{gsec(int(m.group(1)))}{m.group(2)}',t)
    t=sec3.sub(lambda m:f'{m.group(1)}{gsec(int(m.group(2)))}{m.group(3)}',t)
    if t!=o:log.add((o.strip()[:60],t.strip()[:60]))
    return t
def segs(s,fn):
    parts=re.split(r'(<[^>]*>)',s);out=[];skip=False
    for p in parts:
        if p.startswith('<'):
            ls=p.lower()
            if ls.startswith('<style') or ls.startswith('<script'):skip=True
            if ls.startswith('</style') or ls.startswith('</script'):skip=False
            out.append(p);continue
        out.append(p if skip or not p.strip() else fn(p))
    return ''.join(out)
def doref(t):
    return gs(tpat.sub(fix_ref,t))
rowpat=re.compile(r'(<div class="r">)((?:<span>.*?</span>){2,3}?)(<span>)(.*?)(</span></div>)',re.S)
def toc(s):
    # rows: first span = section no, last span = pages
    def row(m):
        cells=re.findall(r'<span>.*?</span>',m.group(0),re.S)
        a=re.sub(r'<[^>]+>','',cells[0]).strip();last=cells[-1]
        na=a
        mm=re.fullmatch(r'(\d+)(\.\d)?',a)
        if mm and 46<=int(mm.group(1))<=61:na=f'{gsec(int(mm.group(1)))}{mm.group(2) or ""}'
        cells[0]=cells[0].replace(a,na,1)
        txt=re.sub(r'<[^>]+>','',last)
        cells[-1]=last.replace(txt,re.sub(r'\d+',lambda x:str(f(int(x.group(0)))),txt),1)
        return '<div class="r">'+''.join(cells)+'</div>'
    return re.sub(r'<div class="r">(?:<span>.*?</span>)+</div>',row,s,flags=re.S)
def settab(s,n):return re.sub(r'<div class="tab">\d+</div>',f'<div class="tab">{n}</div>',s,1)
if __name__=='__main__':
    N=235;new={}
    for n in range(1,N+1):
        s=open(D+f'str-{n:03d}.dc.html').read()
        if n in (3,4,5):
            s=toc(s);s=segs(s,lambda t:gs(tpat.sub(fix_ref,t)) if not re.fullmatch(r'[\d\s,–\-]+',t) else t)
        else:s=segs(s,doref)
        m=f(n);s=settab(s,m);new[m]=s
    for m,s in new.items():open(D+f'str-{m:03d}.dc.html','w').write(s)
    for a,b in sorted(log):print(a,'=>',b)
