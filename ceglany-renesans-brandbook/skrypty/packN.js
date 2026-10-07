const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';const dir=S+process.argv[2]+'/work/';
const streams=JSON.parse(fs.readFileSync(dir+'streams.json','utf8'));
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
fs.writeFileSync(dir+'_m.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${dir}brand.css"><link rel="stylesheet" href="file://${dir}extra.css.css"><style>body{margin:0}</style></head><body><div class="cr pg"><div class="bd tx"><div class="dx" id="c" style="column-count:1;max-width:none"></div></div></div></body></html>`);
fs.copyFileSync(dir+'extra.css',dir+'extra.css.css');
await p.goto('file://'+dir+'_m.html');await p.evaluate(()=>document.fonts.ready);
const out={};
for(const [k,groups] of Object.entries(streams)){
 out[k]=await p.evaluate((groups)=>{const c=document.getElementById('c');const fits=h=>{c.innerHTML="";void c.offsetHeight;c.innerHTML=h;return c.scrollWidth<=c.clientWidth+2&&c.lastElementChild.getBoundingClientRect().bottom<=c.getBoundingClientRect().bottom};
 const pages=[];let cur=[];for(const g of groups){const t=cur.concat([g]);if(!fits(t.join('\n'))&&cur.length){pages.push(cur);cur=[g]}else cur=t}if(cur.length)pages.push(cur);return pages},groups);
 console.log(k,out[k].map(x=>x.length));
}
fs.writeFileSync(dir+'pages.json',JSON.stringify(out));await b.close()})()
