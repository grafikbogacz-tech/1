const {chromium}=require('playwright');const fs=require('fs');
const dir='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/build/project/';const only=process.argv.slice(2);
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:900,height:1200}});
let files=fs.readdirSync(dir).filter(f=>f.endsWith('.dc.html')).sort();
if(only.length) files=files.filter(f=>only.some(o=>f.includes(o)));
for(const f of files){
 const s=fs.readFileSync(dir+f,'utf8');
 const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>[\s\S]*?<\/helmet>/,m=>'<style>'+(m.match(/<style>([\s\S]*?)<\/style>/)||['',''])[1]+'</style>');
 const html='<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file:///tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/fonts/local.css"><link rel="stylesheet" href="file:///tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/build/project/brand.css"></head><body style="margin:0">'+body+'</body></html>';
 fs.writeFileSync('/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/pag/_v.html',html);
 await p.goto('file:///tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/pag/_v.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
 const r=await p.evaluate(()=>{
  const pg=document.querySelector('.pg');const bd=pg.querySelector('.bd');const out=[];
  const pr=pg.getBoundingClientRect();
  if(bd){const br=bd.getBoundingClientRect();
   bd.querySelectorAll('*').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&r.height&&(r.bottom>br.bottom+1||r.right>br.right+1)&&!e.closest('.dx')) out.push(['out',e.tagName,e.className,Math.round(r.bottom-br.bottom),Math.round(r.right-br.right)])});
   const dx=bd.querySelector('.dx'); if(dx&&dx.scrollWidth>dx.clientWidth+2) out.push(['dxoverflow']);
  }
  const small=new Set();
  pg.querySelectorAll('*').forEach(e=>{if([...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim())){const fs=parseFloat(getComputedStyle(e).fontSize);if(fs<12&&!e.closest('.ph')&&!e.closest('.art')) small.add(e.tagName+'.'+e.className+':'+fs)}});
  return {out:out.slice(0,6),small:[...small].slice(0,6)};
 });
 if(r.out.length||r.small.length) console.log(f,JSON.stringify(r));
}
console.log('checked',files.length);await b.close()})()
