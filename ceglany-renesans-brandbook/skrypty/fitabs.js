const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';
(async()=>{const dir=process.argv[2],f=process.argv[3];
const s=fs.readFileSync(S+dir+'/project/'+f,'utf8');
const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>([\s\S]*?)<\/helmet>/,(m,x)=>'<style>'+((x.match(/<style>([\s\S]*?)<\/style>/)||['',''])[1])+'</style>');
fs.writeFileSync(S+dir+'/_f.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${S}${dir}/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
await p.goto('file://'+S+dir+'/_f.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
console.log(await p.evaluate(()=>{const c=[...document.querySelectorAll("div")].find(e=>e.style.position=="absolute"&&e.style.left=="76px"&&e.style.top=="100px");const ft=document.querySelector(".ft").getBoundingClientRect().top;return {bottom:Math.round(c.getBoundingClientRect().bottom),footTop:Math.round(ft)}}));
await p.screenshot({path:S+dir+'/'+f+'.png'});await b.close()})()
