import json,re,sys
from html.parser import HTMLParser
D='all/project/project/'
B={'007','013','014','028','029','031','032','033','034','131','053'}
class P(HTMLParser):
    def __init__(s):super().__init__(convert_charrefs=False);s.t=[]
    def handle_starttag(s,tag,attrs):s.t.append((tag,s.getpos(),s.get_starttag_text()))
def run(only=None):
    d=json.load(open('norm.json'));rep={}
    for n,v in d.items():
        if only and n not in only:continue
        if n in B or not v:continue
        if re.match(r'(FB|GBP|ADS|YT|IG|WWW)-\d+',v[0]['t']):continue
        has_title=any(x['role']=='title' for x in v)
        tg=[]
        for x in v:
            if x['role']=='eye':tg.append((x,12))
            elif x['role']=='title':tg.append((x,36))
            elif x['role']=='num' and not has_title:tg.append((x,36))
            elif x['role']=='name' and not has_title:tg.append((x,21))
        if not tg:continue
        f=D+f'str-{n}.dc.html';s=open(f).read()
        a=s.index('class="cr pg"');a=s.index('>',a)+1;e=s.index('</x-dc>')
        seg=s[a:e];p=P();p.feed(seg)
        lines=seg.split('\n');off=[0]
        for l in lines:off.append(off[-1]+len(l)+1)
        edits=[]
        seen=set();tg=[(x,t) for x,t in tg if not (x['idx'] in seen or seen.add(x['idx']))]
        for x,tgt in tg:
            tag,(ln,col),txt=p.t[x['idx']]
            pos=off[ln-1]+col
            assert seg[pos:pos+len(txt)]==txt,(n,x)
            new=round(tgt/x['z'],2)
            nt=txt
            m=re.search(r'font-size:[\d.]+px',nt)
            if m:nt=nt[:m.start()]+f'font-size:{new:g}px'+nt[m.end():]
            else:nt=re.sub(r'style="',f'style="font-size:{new:g}px;',nt,1)
            if x['role']=='title':nt=re.sub(r'color:\s*(#000000|#000|rgb\(0,\s*0,\s*0\))',"color:#111",nt)
            edits.append((pos,len(txt),nt))
        for pos,l,nt in sorted(edits,reverse=True):seg=seg[:pos]+nt+seg[pos+l:]
        open(f,'w').write(s[:a]+seg+s[e:]);rep[n]=len(edits)
    return rep
if __name__=='__main__':print(run(sys.argv[1:] or None))
