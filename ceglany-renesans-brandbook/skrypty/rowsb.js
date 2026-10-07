const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';const dir='all/project';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
for(const f of process.argv.slice(2)){
const s=fs.readFileSync(S+dir+'/project/'+f,'utf8');
const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>([\s\S]*?)<\/helmet>/,(m,x)=>'<style>'+((x.match(/<style>([\s\S]*?)<\/style>/)||['',''])[1])+'</style>');
fs.writeFileSync(S+dir+'/_h.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${S}${dir}/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
await p.goto('file://'+S+dir+'/_h.html');await p.evaluate(()=>document.fonts.ready);
console.log(f,await p.evaluate(()=>{const r=[...document.querySelectorAll('.r,h3')];const l=r[r.length-1].getBoundingClientRect();const dx=document.querySelector('.dx');return [r.length,Math.round(l.bottom),dx&&Math.round(dx.scrollHeight),dx&&Math.round(dx.clientHeight)]}))}
await b.close()})()
