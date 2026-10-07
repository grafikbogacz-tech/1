const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';
(async()=>{const s=fs.readFileSync(S+'live19/project/p007.dc.html','utf8');
const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>[\s\S]*?<\/helmet>/,'');
fs.writeFileSync(S+'live19/_f.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${S}live19/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
await p.goto('file://'+S+'live19/_f.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
console.log(await p.evaluate(()=>{const d=document.querySelector('.dx'),bd=document.querySelector('.bd');return {dx:d.scrollHeight,bd:bd.clientHeight}}));
await p.screenshot({path:S+'live19/f7.png'});await b.close()})()
