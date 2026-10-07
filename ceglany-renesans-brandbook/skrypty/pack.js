const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';
const groups=JSON.parse(fs.readFileSync(S+'live24/groups.json','utf8'));
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
fs.writeFileSync(S+'live24/_m.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${S}live24/project/brand.css"><style>body{margin:0}</style></head><body><div class="cr pg"><div class="bd tx"><div class="dx" id="c" style="column-count:1;max-width:none"></div></div></div></body></html>`);
await p.goto('file://'+S+'live24/_m.html');await p.evaluate(()=>document.fonts.ready);
const pages=await p.evaluate((groups)=>{const c=document.getElementById('c');const fits=h=>{c.innerHTML="";void c.offsetHeight;c.innerHTML=h;return c.scrollWidth<=c.clientWidth+2};
 const pages=[];let cur=[];for(const g of groups){const t=cur.concat([g]);if(!fits(t.join('\n'))&&cur.length){pages.push(cur);cur=[g]}else cur=t}if(cur.length)pages.push(cur);return pages},groups);
fs.writeFileSync(S+'live24/pages.json',JSON.stringify(pages));console.log(pages.map(x=>x.length));await b.close()})()
