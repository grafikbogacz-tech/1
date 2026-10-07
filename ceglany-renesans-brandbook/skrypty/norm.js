// emits for each page the list of {idx, role, eff, zoom} to normalise
const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';const dir='all/project';
const only=process.argv.slice(2);
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
const out={};
for(const f of fs.readdirSync(S+dir+'/project').filter(x=>/^str-\d+\.dc\.html$/.test(x)).sort()){
if(only.length&&!only.includes(f.slice(4,7)))continue;
const s=fs.readFileSync(S+dir+'/project/'+f,'utf8');
const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>([\s\S]*?)<\/helmet>/,(m,x)=>'<style>'+((x.match(/<style>([\s\S]*?)<\/style>/)||['',''])[1])+'</style>');
fs.writeFileSync(S+dir+'/_h.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${S}${dir}/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
await p.goto('file://'+S+dir+'/_h.html');
out[f.slice(4,7)]=await p.evaluate(()=>{const pg=document.querySelector('.pg');const all=[...pg.querySelectorAll('*')];
const zf=e=>{let z=1,q=e;while(q&&q!==pg.parentElement){const zz=parseFloat(getComputedStyle(q).zoom);if(zz&&zz!=1)z*=zz;q=q.parentElement}return z};
const res=[];const w=document.createTreeWalker(pg,NodeFilter.SHOW_TEXT);let n;let seenEye=false,seenTitle=false,seenNum=false;let titleTop=null;
while(n=w.nextNode()){const t=n.textContent.trim();if(!t)continue;const e=n.parentElement;if(e.closest('.rh,.ft,.tab'))continue;const r=e.getBoundingClientRect();if(r.top>300)break;
const c=getComputedStyle(e);const z=zf(e);const eff=parseFloat(c.fontSize)*z;const mono=c.fontFamily.includes('Mono');const or=c.color.replace(/ /g,'')=='rgb(237,104,66)';const wt=+c.fontWeight;
const idx=all.indexOf(e);
if(!seenEye&&mono&&or&&eff<=20&&wt<=500){seenEye=true;res.push({idx,role:'eye',eff,z,t:t.slice(0,30)});continue}
if(mono&&or&&wt==300&&eff>=24){seenNum=true;res.push({idx,role:'num',eff,z,t:t.slice(0,12),top:r.top});continue}
if(seenNum&&!res.some(x=>x.role=='name')&&!mono&&wt==500&&eff>=18){res.push({idx,role:'name',eff,z,t:t.slice(0,40)});continue}
if(!mono&&wt==300&&eff>=28&&!seenNum&&(!seenTitle||(titleTop!=null&&r.top-titleTop<eff*1.5))){seenTitle=true;titleTop=r.top;res.push({idx,role:'title',eff,z,t:t.slice(0,40),or});continue}
if(res.length>=5)break}
return res});}
fs.writeFileSync(S+'norm.json',JSON.stringify(out));await b.close()})()
