import json,re,os,sys
d=json.load(open('build/pages2c.json'));P='all/project/project/';names=d['names'];pages=d['pages']
for i,pg in enumerate(pages):
    n=names[i] if i<len(names) else None
    assert n,'more pages than files'
    s=open(P+n+'.dc.html').read()
    s=re.sub(r'<div class="dx">[\s\S]*?</div></div><div class="ft">','<div class="dx">'+'\n'.join(pg)+'\n</div></div><div class="ft">',s)
    open(P+n+'.dc.html','w').write(s)
print(len(pages),len(names),names[len(pages):])
