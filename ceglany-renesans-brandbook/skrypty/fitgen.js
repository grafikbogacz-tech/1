const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';
(async()=>{const dir=process.argv[2],f=process.argv[3];
const s=fs.readFileSync(S+dir+'/project/'+f,'utf8');
const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>([\s\S]*?)<\/helmet>/,(m,x)=>'<style>'+((x.match(/<style>([\s\S]*?)<\/style>/)||['',''])[1])+'</style>');
fs.writeFileSync(S+dir+'/_f.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${S}${dir}/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
await p.goto('file://'+S+dir+'/_f.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
console.log(await p.evaluate(()=>{const bd=document.querySelector(".bd")||{getBoundingClientRect:()=>({bottom:0})};const bdr=bd.getBoundingClientRect?bd.getBoundingClientRect():bd;let m=0;document.querySelectorAll('.dx > *').forEach(e=>{m=Math.max(m,e.getBoundingClientRect().bottom)});return {contentBottom:Math.round(m),bdBottom:Math.round(bdr.bottom)}}));
await p.screenshot({path:S+dir+'/'+f+'.png'});await b.close()})()
