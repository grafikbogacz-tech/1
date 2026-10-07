const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';const dir='all/project';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
for(const f of fs.readdirSync(S+dir+'/project').filter(x=>/^str-\d+\.dc\.html$/.test(x)).sort()){
const s=fs.readFileSync(S+dir+'/project/'+f,'utf8');
const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>([\s\S]*?)<\/helmet>/,(m,x)=>'<style>'+((x.match(/<style>([\s\S]*?)<\/style>/)||['',''])[1])+'</style>');
fs.writeFileSync(S+dir+'/_h.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}${dir}/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
await p.goto('file://'+S+dir+'/_h.html');
const r=await p.evaluate(()=>{const pg=document.querySelector('.pg');const ft=pg.querySelector('.ft');if(!ft)return pg.parentElement.querySelector('.ft')||document.querySelector('.ft')?'OUTSIDE':'none';const r=ft.getBoundingClientRect();return [ft.parentElement===pg,Math.round(r.left),Math.round(r.top),Math.round(r.width),Math.round(r.height)].join(',')});
if(r!='none'&&r!='true,0,1075,794,48')console.log(f.slice(4,7),r)}
await b.close()})()
