const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';
(async()=>{const f=process.argv[2];const s=fs.readFileSync(S+'all/project/project/'+f,'utf8');
const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>([\s\S]*?)<\/helmet>/,(m,x)=>'<style>'+((x.match(/<style>([\s\S]*?)<\/style>/)||['',''])[1])+'</style>');
fs.writeFileSync(S+'all/_d.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}all/project/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
await p.goto('file://'+S+'all/_d.html');
console.log(await p.evaluate(()=>{const e=document.elementFromPoint(400,1090);const ft=document.querySelector('.ft');const cs=getComputedStyle(ft);return [e.tagName,e.className,e.getAttribute('style')?.slice(0,80),cs.backgroundColor,cs.position,ft.getBoundingClientRect().top,ft.parentElement.className,document.querySelector('.pg').scrollHeight, getComputedStyle(document.querySelector('.pg')).zoom]}));
await p.screenshot({path:S+'all/_d.png'});await b.close()})()
