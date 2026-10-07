const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
for(const n of process.argv.slice(2)){const s=fs.readFileSync(S+`build/project/p${n}.dc.html`,'utf8');
const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>[\s\S]*?<\/helmet>/,'');
fs.writeFileSync(S+'build/_s.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${S}build/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
await p.goto('file://'+S+'build/_s.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:S+`build/s${n}.png`});}
await b.close()})()
