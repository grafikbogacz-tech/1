import json,re,os,shutil,glob
S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad'
OLD=S+'/cr/project'; NEW=S+'/build/project'
shutil.rmtree(NEW,ignore_errors=True); os.makedirs(NEW)
streams=json.load(open(S+'/pag/streams.json')); pages=json.load(open(S+'/pag/pages.json'))
order=['I','II','III_audyt','III_kolory','III_foto','IV_fb','IV_tt','IV_ig','IV_mx','V','VI','VII']
# old pages
oldtype={};oldlab={};oldel={}
runs=[];prev=False;lastlab=None;si=-1;cnt={k:0 for k in order}
for i in range(1,136):
    s=open(f'{OLD}/p{i:03d}.dc.html').read()
    istext='class="dx"' in s
    oldtype[i]='T' if istext else 'V'
    m=re.search(r'class="rh"><span>(.*?)</span>',s); oldlab[i]=m.group(1) if m else ''
    if istext:
        if not prev or lastlab!=oldlab[i]: si+=1
        lastlab=oldlab[i]
        k=order[si]
        body=s.split('<div class="dx">\n',1)[1].split('\n</div></div><div class="ft">')[0]
        n=0;rest=body
        while rest:
            el=streams[k][cnt[k]+n]
            assert rest.startswith(el),(i,k,cnt[k]+n,rest[:80],el[:80])
            rest=rest[len(el):]
            if rest.startswith('\n'): rest=rest[1:]
            n+=1
        oldel[i]=(k,cnt[k],cnt[k]+n-1); cnt[k]+=n
        oldlab[i]=(k,oldlab[i])
    prev=istext
for k in order: assert cnt[k]==len(streams[k]),(k,cnt[k],len(streams[k]))
# new sequence
seq=[];emitted=set()
for i in range(1,136):
    if oldtype[i]=='V': seq.append(('V',i))
    else:
        k=oldel[i][0]
        if k in emitted: continue
        emitted.add(k)
        lab=oldlab[i][1]
        for j,(a,z) in enumerate(pages[k]): seq.append(('T',k,a,z,lab))
vmap={};newpg={k:[] for k in order}
for n,e in enumerate(seq,1):
    if e[0]=='V': vmap[e[1]]=n
    else: newpg[e[1]].append((e[2],e[3],n))
print('total',len(seq))
def el2page(k,el):
    for a,z,n in newpg[k]:
        if a<=el<=z: return n
    raise Exception((k,el))
# row headings: key -> (stream,start,next boundary)
def h2idx(k,prefix):
    for i,e in enumerate(streams[k]):
        if e.startswith('<h2') and re.sub('<[^>]+>','',e).startswith(prefix): return i
    raise Exception(prefix)
H={}
for nn in ['03','04','05','06','07','08','09','10','11','12','13']: H[nn]=('I',h2idx('I',nn))
for nn in ['14','15','16','17','18','19','20']: H[nn]=('II',h2idx('II',nn))
H['audyt']=('III_audyt',0)
H['29']=('III_kolory',0);H['30']=('III_kolory',h2idx('III_kolory','30.1'))
H['44.1']=('IV_fb',0);H['44.2']=('IV_tt',5);H['44.3']=('IV_ig',0);H['44.4']=('IV_mx',0)
H['49']=('V',0)
for nn in ['52','53','54','55','56','57','58','59','60','61']: H[nn]=('VI',h2idx('VI',nn))
H['kontrola']=('VI',h2idx('VI','Kontrola'))
for key,pre in [('cel',None),('A','A.'),('B','B.'),('C','C.'),('D','D.'),('E','E.'),('F','F.')]:
    H[key]=('VII',0 if pre is None else h2idx('VII',pre))
def bound(k,e):
    hs=sorted(v[1] for kk,v in H.items() if v[0]==k)
    nx=[x for x in hs if x>e]
    return nx[0] if nx else len(streams[k])
def rowkey(nn,title):
    t=re.sub('<[^>]+>','',title)
    if nn=='—':
        if t.startswith('Audyt'): return 'audyt'
        if t.startswith('Kontrola'): return 'kontrola'
        if t.startswith('Cel'): return 'cel'
        return None
    if nn in H: return nn
    if nn in 'ABCDEF' and len(nn)==1: return nn
    if nn=='02' or nn=='01' : return None
    return None
def oldfirst(p): return oldel[p][1] if oldtype[p]=='T' else None
def newtok(p,start,key):
    if oldtype[p]=='V': return vmap[p]
    k,a,z=oldel[p]
    if key and key in H and H[key][0]==k:
        e=H[key][1]
        if start: return el2page(k,max(e,a) if a<=e<=z else a)
        b=min(z,bound(k,e)-1)
        return el2page(k,b)
    return el2page(k,a if start else z)
def maprange(txt,key):
    m=re.fullmatch(r'(\d+)(?:–(\d+))?',txt)
    if not m: return txt
    a=int(m.group(1)); b=int(m.group(2) or a)
    if a>135 or b>135: return txt
    x=newtok(a,True,key); y=newtok(b,False,key)
    return str(x) if x==y else f'{x}–{y}'
def fv(old): return str(vmap[int(old)])
def fix_toc(s):
    def row(m):
        nn,title,pg=m.group(1),m.group(2),m.group(3)
        key=rowkey(nn,title)
        title2=re.sub(r'strona (\d+)',lambda q:'strona '+fv(q.group(1)),title)
        return f'<div class="r"><span>{nn}</span><span>{title2}</span><span>{maprange(pg,key)}</span></div>'
    s=re.sub(r'<div class="r"><span>(.*?)</span><span>(.*?)</span><span>(.*?)</span></div>',row,s)
    s=re.sub(r'str\. (\d+)</span>',lambda q:'str. '+fv(q.group(1))+'</span>',s)
    return s
def retab(s,n):
    s=re.sub(r'<div class="tab">\d+</div>',f'<div class="tab">{n}</div>',s)
    s=re.sub(r'<title>Strona \d+',f'<title>Strona {n}',s,1)
    return s
TPL=open(f'{OLD}/p008.dc.html').read()
head=TPL.split('<div class="cr pg">')[0]; tail='</x-dc>'+TPL.split('</x-dc>')[1]
partpages={5,16,19,46,90,94,101}
foto_rng=lambda: f"{newpg['III_foto'][0][2]}–{newpg['III_foto'][-1][2]}"
for n,e in enumerate(seq,1):
    if e[0]=='V':
        o=e[1]; s=open(f'{OLD}/p{o:03d}.dc.html').read()
        if o in (2,3,4) or o in partpages: s=fix_toc(s)
        s=retab(s,n)
        if o==27: s=s.replace('strona 31','strona '+fv(31))
        if o==37: s=s.replace('stronach 38–41','stronach '+foto_rng())
        if o==82: s=s.replace('str. 52–53',f'str. {fv(52)}–{fv(53)}').replace('str. 69','str. '+fv(69))
    else:
        k,a,z,lab=e[1],e[2],e[3],e[4]
        s=head.replace('<title>Strona 7</title>',f'<title>Strona {n}</title>')+f'<div class="cr pg"><div class="tab">{n}</div><div class="rh"><span>{lab}</span><span>Ceglany Renesans</span></div><div class="bd tx"><div class="dx">\n'+'\n'.join(streams[k][a:z+1])+'\n</div></div><div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n'+tail
    open(f'{NEW}/p{n:03d}.dc.html','w').write(s)
# canvas
board={}
for n in range(1,len(seq)+1):
    c,r=(n-1)%6,(n-1)//6
    board[f'p{n:03d}.dc.html']={'x':c*874,'y':r*1243,'w':794,'h':1123,'title':f'Strona {n}'}
old=json.load(open(OLD+'/canvas.json'))
old['boards']=board
json.dump(old,open(NEW+'/canvas.json','w'),ensure_ascii=False,indent=1)
shutil.copy(OLD+'/brand.css',NEW+'/brand.css')
for f in glob.glob(OLD+'/logo-*.svg'): shutil.copy(f,NEW)
json.dump({'vmap':vmap,'newpg':newpg},open(S+'/build/maps.json','w'))
