import math,re
S='fill="#F1F1F1" stroke="#8A8A8A" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'
N='fill="none" stroke="#8A8A8A" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'
def saw():
    pts=[];n=14
    for i in range(n):
        a0=2*math.pi*i/n; a1=a0+2*math.pi/n*0.15; a2=a0+2*math.pi/n
        pts.append((48+30*math.cos(a0),48+30*math.sin(a0)))
        pts.append((48+42*math.cos(a0+0.02),48+42*math.sin(a0+0.02)))
        pts.append((48+36*math.cos(a2-0.12),48+36*math.sin(a2-0.12)))
    d='M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in pts)+'Z'
    return f'<path d="{d}" {S}/><circle cx="48" cy="48" r="7" fill="#fff" stroke="#8A8A8A" stroke-width="4"/>'
I=[
('Cegła',f'<path d="M8 38 L26 24 H88 L64 38Z" {S}/><path d="M64 38 L88 24 V58 L64 72Z" {S}/><rect x="8" y="38" width="56" height="34" {S}/>'),
('Cięcie',saw()),
('Płytka',f'<rect x="12" y="10" width="46" height="46" {S}/><rect x="36" y="34" width="46" height="46" {S}/>'),
('Wymiar',f'<rect x="8" y="30" width="80" height="36" {S}/><path d="M22 30v10M36 30v14M50 30v10M64 30v14M78 30v10" {N}/>'),
('Montaż',f'<path d="M14 40 L80 14 L56 78Z" {S}/><path d="M42 56 L22 76" {N}/><rect x="10" y="68" width="22" height="9" rx="4" transform="rotate(-45 21 72.5)" {S}/>'),
('Wiek',f'<circle cx="48" cy="48" r="38" {S}/><path d="M48 22V50L64 66" {N}/>'),
('Dostawa',f'<rect x="6" y="26" width="52" height="40" {S}/><path d="M58 38H74L88 50V66H58Z" {S}/><path d="M66 44H74L80 50H66Z" fill="#DADADA" stroke="#8A8A8A" stroke-width="3" stroke-linejoin="round"/><circle cx="24" cy="68" r="8" fill="#fff" stroke="#8A8A8A" stroke-width="4"/><circle cx="70" cy="68" r="8" fill="#fff" stroke="#8A8A8A" stroke-width="4"/>'),
('Próbka',f'<rect x="10" y="12" width="44" height="44" {S}/><rect x="34" y="34" width="46" height="46" {S}/>'+''.join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#8A8A8A"/>' for x in (46,57,68) for y in (46,57,68))),
('Kontakt',f'<rect x="8" y="22" width="80" height="54" {S}/><path d="M8 24 L48 54 L88 24" {N}/>'),
('Realizacja',f'<path d="M12 34 L48 14 L84 34Z" {S}/><rect x="16" y="34" width="64" height="48" {S}/>'+''.join(f'<rect x="{x}" y="46" width="8" height="8" fill="#8A8A8A"/><rect x="{x}" y="62" width="8" height="8" fill="#8A8A8A"/>' for x in (26,62))+f'<path d="M41 82V68a7 7 0 0 1 14 0V82" {S}/>'),
('Ponowne użycie',f'<path d="M20 52a28 28 0 0 1 48-18" {N}/><path d="M72 18V36H54" {N}/><path d="M76 44a28 28 0 0 1-48 18" {N}/><path d="M24 78V60H42" {N}/>'),
('Strzałka CTA','<path d="M8 48H86M62 24L86 48 62 72" fill="none" stroke="#C85F3E" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>'),
]
cells=''
for i,(n,s) in enumerate(I,1):
    cells+=f'<div class="ib"><svg viewBox="0 0 96 96" width="88" height="88">{s}</svg><div class="mono"><span style="color:#ED6842;margin-right:10px">{i:02d}</span>{n.upper()}</div></div>\n'
src=open('all/project/project/p043.dc.html').read()
src=re.sub(r'<div style="display:grid;grid-template-columns:repeat\(4,1fr\).*?</div>\n</div>\n<div class="sb">',
 '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:22px 18px">\n'+cells+'</div>\n<div class="sb">',src,flags=re.S)
src=src.replace('.ib{display:flex;flex-direction:column;gap:8px;padding:12px 0 0;border-top:1px solid var(--hl)}','.ib{display:flex;flex-direction:column;gap:14px;padding:0 0 16px;border-bottom:1px solid var(--hl)}.ib:nth-last-child(-n+4){border-bottom:0}')
src=src.replace('Styl outline, linia 1,5 px, siatka 32 px, proste końce i ostre narożniki, bez wypełnień. Ikona jest czarna; opcjonalnie jeden pomarańczowy detal.','Styl liniowy: szara obwódka, bardzo jasne wypełnienie, zaokrąglone końce i narożniki. Jedyny kolorowy znak to terakotowa strzałka CTA, a numery ikon są w kolorze terakoty.')
src=src.replace('Siatka 32 × 32 i zasady','Siatka 96 × 96 i zasady').replace('Ikona jest czarna','')
open('all/project/project/p043.dc.html','w').write(src)
