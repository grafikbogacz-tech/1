const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';const dir='all/project';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
for(const f of fs.readdirSync(S+dir+'/project').filter(x=>/^str-\d+\.dc\.html$/.test(x)).sort()){
const s=fs.readFileSync(S+dir+'/project/'+f,'utf8');
const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>([\s\S]*?)<\/helmet>/,(m,x)=>'<style>'+((x.match(/<style>([\s\S]*?)<\/style>/)||['',''])[1])+'</style>');
fs.writeFileSync(S+dir+'/_h.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${S}${dir}/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
await p.goto('file://'+S+dir+'/_h.html');await p.evaluate(()=>document.fonts.ready);
const r=await p.evaluate(()=>{const rh=document.querySelector('.rh');if(!rh)return null;const sp=rh.querySelectorAll('span');if(sp.length<2)return null;const a=sp[0].getBoundingClientRect(),c=sp[1].getBoundingClientRect();return (a.height>16||c.height>16||a.right>c.left-10)?[Math.round(a.right),Math.round(c.left),Math.round(a.height)]:null});
if(r)console.log(f.slice(4,7),r)}
await b.close()})()
