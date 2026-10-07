const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';const dir=process.argv[2];const out=process.argv[3];
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});const res={};
for(const f of fs.readdirSync(S+dir+'/project').filter(x=>/^str-\d+\.dc\.html$/.test(x)).sort()){
const s=fs.readFileSync(S+dir+'/project/'+f,'utf8');
const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>([\s\S]*?)<\/helmet>/,(m,x)=>'<style>'+((x.match(/<style>([\s\S]*?)<\/style>/)||['',''])[1])+'</style>');
fs.writeFileSync(S+dir+'/_b.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${S}all/project/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
await p.goto('file://'+S+dir+'/_b.html');
res[f.slice(4,7)]=await p.evaluate(()=>{const pg=document.querySelector('.pg');let m=0;for(const e of pg.querySelectorAll('*')){if(e.closest('.ft,.tab,.rh'))continue;if(e.children.length&&e.tagName=='DIV'&&false)continue;const r=e.getBoundingClientRect();if(r.height>0&&r.bottom>m&&r.bottom<1300)m=r.bottom}return Math.round(m)})}
fs.writeFileSync(S+out,JSON.stringify(res));await b.close()})()
