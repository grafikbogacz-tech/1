const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';const dir='all/project';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
const out={};
for(const f of fs.readdirSync(S+dir+'/project').filter(x=>/^str-\d+\.dc\.html$/.test(x)).sort()){
const s=fs.readFileSync(S+dir+'/project/'+f,'utf8');
const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>([\s\S]*?)<\/helmet>/,(m,x)=>'<style>'+((x.match(/<style>([\s\S]*?)<\/style>/)||['',''])[1])+'</style>');
fs.writeFileSync(S+dir+'/_h.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${S}${dir}/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
await p.goto('file://'+S+dir+'/_h.html');
const r=await p.evaluate(()=>{const pg=document.querySelector('.pg');const all=[...pg.querySelectorAll('*')];
const zf=e=>{let z=1,q=e;while(q&&q!==pg.parentElement){const zz=parseFloat(getComputedStyle(q).zoom);if(zz&&zz!=1)z*=zz;q=q.parentElement}return z};
const res=[];
for(const e of all){if(e.closest('.rh,.ft,.tab'))continue;if(e.children.length)continue;const t=e.textContent.trim();if(!/^(\d{1,2}|[A-Z])$/.test(t))continue;const c=getComputedStyle(e);
if(!c.fontFamily.includes('Mono')||+c.fontWeight!=300||c.color.replace(/ /g,'')!='rgb(237,104,66)')continue;const z=zf(e);const eff=parseFloat(c.fontSize)*z;if(eff<34||eff>60)continue;
res.push({idx:all.indexOf(e),role:'num',eff,z,t});
const nx=e.nextElementSibling;if(nx){const cn=getComputedStyle(nx);if(!cn.fontFamily.includes('Mono')&&+cn.fontWeight==500)res.push({idx:all.indexOf(nx),role:'name',eff:parseFloat(cn.fontSize)*zf(nx),z:zf(nx),t:nx.textContent.trim().slice(0,30)})}}
return res});
if(r.length)out[f.slice(4,7)]=r}
fs.writeFileSync(S+'norm2.json',JSON.stringify(out));await b.close()})()
