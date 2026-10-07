const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';const dir='all/project';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
const out={};
for(const f of fs.readdirSync(S+dir+'/project').filter(x=>/^str-\d+\.dc\.html$/.test(x)).sort()){
const s=fs.readFileSync(S+dir+'/project/'+f,'utf8');
const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>([\s\S]*?)<\/helmet>/,(m,x)=>'<style>'+((x.match(/<style>([\s\S]*?)<\/style>/)||['',''])[1])+'</style>');
fs.writeFileSync(S+dir+'/_h.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${S}${dir}/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
await p.goto('file://'+S+dir+'/_h.html');
out[f.slice(4,7)]=await p.evaluate(()=>{const pg=document.querySelector('.pg');const res=[];const w=document.createTreeWalker(pg,NodeFilter.SHOW_TEXT);let n;
while(n=w.nextNode()){const t=n.textContent.trim();if(!t)continue;const e=n.parentElement;if(e.closest('.rh,.ft,.tab'))continue;const r=e.getBoundingClientRect();if(r.top>330)break;const c=getComputedStyle(e);res.push([Math.round(r.left),Math.round(r.top),Math.round(parseFloat(c.fontSize)*(()=>{let z=1,q=e;while(q){const zz=parseFloat(getComputedStyle(q).zoom);if(zz&&zz!=1)z*=zz;q=q.parentElement}return z})()*10)/10,c.fontWeight,c.fontFamily.includes('Mono')?'M':'H',c.color.replace(/ /g,''),t.slice(0,28)]);if(res.length>=4)break}
return res});}
fs.writeFileSync(S+'heads.json',JSON.stringify(out));await b.close()})()
