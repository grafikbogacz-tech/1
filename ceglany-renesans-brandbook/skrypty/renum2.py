import re
D='all/project/project/'
def h(n):
    if n in (43,44):return n+2
    if 45<=n<=60:return n+4
    return n
sec1=re.compile(r'^(\s*)(4[3-9]|5\d|60)((?:\.\d)?)(?= · | [A-ZŁŚŻĆŹ])')
sec2=re.compile(r'(?<=· )(4[3-9]|5\d|60)((?:\.\d)?)(?= [A-ZŁŚŻĆŹ])')
sec3=re.compile(r'(?i)(sekcj\w*\s+)(4[3-9]|5\d|60)((?:\.\d)?)')
log=set()
def gs(t):
    o=t
    t=sec1.sub(lambda m:f'{m.group(1)}{h(int(m.group(2)))}{m.group(3)}',t)
    t=sec2.sub(lambda m:f'{h(int(m.group(1)))}{m.group(2)}',t)
    t=sec3.sub(lambda m:f'{m.group(1)}{h(int(m.group(2)))}{m.group(3)}',t)
    if t!=o:log.add((o.strip()[:55],t.strip()[:55]))
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
def toc(s):
    def row(m):
        cells=re.findall(r'<span>.*?</span>',m.group(0),re.S)
        a=re.sub(r'<[^>]+>','',cells[0]).strip()
        mm=re.fullmatch(r'(\d+)(\.\d)?',a)
        if mm and (int(mm.group(1)) in (43,44) or 45<=int(mm.group(1))<=60):
            na=f'{h(int(mm.group(1)))}{mm.group(2) or ""}';cells[0]=cells[0].replace(a,na,1)
        return '<div class="r">'+''.join(cells)+'</div>'
    return re.sub(r'<div class="r">(?:<span>.*?</span>)+</div>',row,s,flags=re.S)
if __name__=='__main__':
    for n in range(1,236):
        f=D+f'str-{n:03d}.dc.html';s=open(f).read()
        if n in (4,5):s=toc(s)
        s=segs(s,gs);open(f,'w').write(s)
    for a,b in sorted(log):print(a,'=>',b)
