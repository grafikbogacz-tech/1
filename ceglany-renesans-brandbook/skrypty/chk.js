const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
const streams=JSON.parse(fs.readFileSync('/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/pag/streams.json','utf8'));const pages=JSON.parse(fs.readFileSync('/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/pag/pages.json','utf8'));
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:900,height:1200}});
await p.goto('file:///tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/pag/m.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
let bad=0,tot=0,fill=[];
for(const k of Object.keys(streams)){
 for(const [a,z] of pages[k]){
  const r=await p.evaluate((h)=>{const c=document.getElementById('c');c.innerHTML="";void c.offsetHeight;c.innerHTML=h;return [c.scrollWidth<=c.clientWidth+2, c.scrollWidth, c.clientWidth]},streams[k].slice(a,z+1).join('\n'));
  tot++; if(!r[0]){bad++;console.log('OVERFLOW',k,a,z,r)}
 }
}
console.log('pages',tot,'bad',bad);await b.close()})()
