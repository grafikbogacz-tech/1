import json,re
pages=json.load(open('build/pages116.json'))
tpl=open('build/tpl116.html').read()
names=['p116','p117','p118','p119','p120','p121','p122','p123','p123b','p123c','p123d']
files=[]
for i,pg in enumerate(pages):
    s=re.sub(r'<div class="dx">[\s\S]*?</div></div><div class="ft">','<div class="dx">'+'\n'.join(pg)+'\n</div></div><div class="ft">',tpl)
    s=re.sub(r'class="tab">\d+<',f'class="tab">{128+i}<',s)
    s=re.sub(r'<title>[^<]*</title>',f'<title>Strona {128+i}</title>',s)
    open(f'all/project/project/{names[i]}.dc.html','w').write(s)
    files.append(names[i])
print(files)
