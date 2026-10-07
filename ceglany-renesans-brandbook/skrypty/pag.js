const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
const streams=JSON.parse(fs.readFileSync('/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/pag/streams.json','utf8'));
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:900,height:1200}});
await p.goto('file:///tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/pag/m.html');
await p.evaluate(()=>document.fonts.ready);
await p.waitForTimeout(500);
const res={};
for(const [k,els] of Object.entries(streams)){
 res[k]=await p.evaluate((els)=>{
  const c=document.getElementById('c');
  const isH=s=>/^<h[234]/.test(s);
  const fits=()=>c.scrollWidth<=c.clientWidth+2;
  const pages=[];let start=0;let i=0;const cur=[];
  const fitsAll=(arr)=>{c.innerHTML="";void c.offsetHeight;c.innerHTML=arr.join("\n");return fits();};
  while(i<els.length){
    let j=i;const group=[els[j]];
    while(isH(els[j])&&j+1<els.length){j++;group.push(els[j]);}
    const trial=cur.concat(group);
    if(!fitsAll(trial)){
      if(cur.length===0){pages.push([start,j]);start=j+1;i=j+1;continue;}
      pages.push([start,i-1]);start=i;cur.length=0;
      cur.push(...group);
    } else {cur.length=0;cur.push(...trial);}
    i=j+1;
  }
  if(start<els.length) pages.push([start,els.length-1]);
  return pages;
 },els);
 console.log(k,els.length,res[k].length,'pages');
}
fs.writeFileSync('/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/pag/pages.json',JSON.stringify(res));
await b.close();})()
