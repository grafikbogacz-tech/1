const {chromium}=require('playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-1/34ecf889-7155-59ef-bb10-7c921c558f87/scratchpad/';
(async()=>{const dir=process.argv[2],f=process.argv[3];
const s=fs.readFileSync(S+dir+'/project/'+f,'utf8');
const body=s.slice(s.indexOf('<x-dc>')+6,s.indexOf('</x-dc>')).replace(/<helmet>([\s\S]*?)<\/helmet>/,(m,x)=>'<style>'+((x.match(/<style>([\s\S]*?)<\/style>/)||['',''])[1])+'</style>');
fs.writeFileSync(S+dir+'/_f.html',`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://${S}fonts/local.css"><link rel="stylesheet" href="file://${S}${dir}/project/brand.css"><style>body{margin:0}</style></head><body>${body}</body></html>`);
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:794,height:1123}});
const M={'fe1d49e4df6d7ab013fa9a883eda217b':'110','b85503954390fe9c4f771d65ec2caf28':'112','54d48e1fcbc72e206ff9e7ec7793006e':'108','321084940182209a83e0601d4938622f':'111','bdb104ac9d28404749c50aa387e7cf31':'109','ec275b1cbdbf1ee2fb9df0a37830e99e':'113','f13bfb534ccf00e0996ec45a24a078f5':'p119','2220e7748909b98f052e7428974c361e':'p120','fdff6103d545d3549127f38239dd873c':'p121','d2bad5bf973de202541937b566f129bc':'p119','389ae5ceae94f6c0a728920f3f8a20cc':'p120','f343626a0da1dd4c6f1d61158d82487b':'78','fe0ae6a7c8a98978702f3a6f318126fe':'116','a24d4df4840b02dc495b57b905499314':'115','590524d23dce1948f1eb03419131b26d':'114'};
await p.route(/_blob\//,r=>{const id=r.request().url().split('/_blob/')[1];const k=M[id];if(k)r.fulfill({path:S+'up/foto-'+k+'.jpg'});else r.abort()});
await p.goto('file://'+S+dir+'/_f.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
console.log(await p.evaluate(()=>{const bd=document.querySelector(".bd")||{getBoundingClientRect:()=>({bottom:0})};const bdr=bd.getBoundingClientRect?bd.getBoundingClientRect():bd;let m=0;document.querySelectorAll('.dx > *').forEach(e=>{m=Math.max(m,e.getBoundingClientRect().bottom)});return {contentBottom:Math.round(m),bdBottom:Math.round(bdr.bottom)}}));
await p.screenshot({path:S+dir+'/'+f+'.png'});await b.close()})()
