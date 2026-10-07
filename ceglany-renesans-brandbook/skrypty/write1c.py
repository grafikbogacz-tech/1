import json,re
d=json.load(open('build/pages2c.json'));P='all/project/project/';names=d['names'];pages=d['pages']
css=open('build/dx1css.txt').read()
out=[]
for i,pg in enumerate(pages):
    n=names[i] if i<len(names) else names[-1]+'x'+str(i-len(names)+1)
    base=open(P+(names[i] if i<len(names) else names[-1])+'.dc.html').read()
    s=re.sub(r'/\*dx1\*/.*?/\*end\*/','',base,flags=re.S)
    s=s.replace('</style></helmet>','/*dx1*/'+css+'/*end*/</style></helmet>',1)
    s=re.sub(r'<div class="dx">[\s\S]*?</div></div><div class="ft">','<div class="dx">'+'\n'.join(pg)+'\n</div></div><div class="ft">',s)
    open(P+n+'.dc.html','w').write(s);out.append(n)
print(out,'unused:',names[len(pages):])
json.dump({'out':out,'unused':names[len(pages):]},open('build/out1c.json','w'))
