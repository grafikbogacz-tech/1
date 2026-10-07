const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';const dir=process.argv[2];
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
let bad=0,n=0;
for(const f of fs.readdirSync(S+dir+'/project').filter(f=>/^p011c\.dc\.html$/.test(f)).sort()){
 const s=fs.readFileSync(S+dir+'/project/'+f,'utf8');if(!s.includes('class="dx"'))continue;n++;
 const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>[\s\S]*?<\/helmet>/,'');
 fs.writeFileSync(S+dir+'/_d.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${S}${dir}/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
 await p.goto('file://'+S+dir+'/_d.html');await p.evaluate(()=>document.fonts.ready);
 const r=await p.evaluate(()=>{const d=document.querySelector('.dx');return [d.scrollWidth,d.clientWidth]});
 if(r[0]>r[1]+2){bad++;console.log('OVERFLOW',f,r)}
}
console.log('text pages',n,'bad',bad);await b.close()})()
