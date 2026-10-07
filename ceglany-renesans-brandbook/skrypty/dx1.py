import re,sys
CSS=""".tx .dx{column-count:1;column-gap:0;font-size:13px;line-height:1.45;color:#333}
.tx .dx h2{display:block;border-top:0;padding-top:0;font-size:24px;font-weight:300;letter-spacing:-.03em;line-height:1.1;margin:20px 0 8px;color:#111}
.tx .dx h2:first-child{margin-top:0}
.tx .dx h2 i{display:block;font-size:12px;letter-spacing:.14em;color:#ED6842;margin-bottom:4px;font-weight:400}
.tx .dx h3{font-size:16px;font-weight:500;letter-spacing:-.02em;margin:14px 0 6px;border-top:1px solid #E7DFC9;padding-top:10px}
.tx .dx h4{color:#0D4C73;margin:12px 0 4px}
.tx .dx b{font-weight:500;color:#111}
.tx .dx p{margin:0 0 6px}
.tx .dx li{margin:0 0 2px;padding-left:18px}
.tx .dx a{color:#0D4C73;word-break:break-all}
.tx .dx th{color:#0D4C73;border-top:1px solid #E7DFC9;border-bottom:2px solid #ED6842;font-weight:400}
.tx .dx td{border-bottom:1px solid #E7DFC9}
.tx .dx .rule{border-top:1px solid #E7DFC9}"""
for n in sys.argv[1:]:
    f=f'all/project/project/p{n}.dc.html'
    s=open(f).read()
    s=re.sub(r'/\*dx1\*/.*?/\*end\*/','',s,flags=re.S)
    s=s.replace('</style></helmet>','/*dx1*/'+CSS.replace('\n','')+'/*end*/</style></helmet>',1)
    open(f,'w').write(s)
