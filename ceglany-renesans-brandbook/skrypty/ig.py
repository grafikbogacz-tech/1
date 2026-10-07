import re
P='all/project/project/'
MF="font-family:'Overpass Mono',monospace"
M=MF+";font-size:11px;letter-spacing:.12em;text-transform:uppercase"
T='#ED6842';G='#0D4C73';B='#EDE9D0';H='#E7DFC9'
foot='<div class="ft"><span>Ceglany Renesans · Brand Book</span><span>Wersja 1.0</span></div></div>\n</x-dc><script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":794,"height":1123}}\'>class Component extends DCLogic{renderVals(){return {};}}</script></body></html>'
def head(n):
    s=open(P+n+'.dc.html').read()
    k='<div class="bd tx">' if '<div class="bd tx">' in s else '<div style="position:absolute;left:76px;top:100px'
    return s[:s.index(k)]
def lab(t,c=T):return f'<div style="{M};letter-spacing:.14em;color:{c}">{t}</div>'
def h1(t,s=36):return f'<div style="font-size:{s}px;font-weight:300;letter-spacing:-.03em;line-height:1.1;margin-top:10px;color:#111">{t}</div>'
def para(t,mt=10,c='#333'):return f'<div style="font-size:13px;line-height:1.5;color:{c};margin-top:{mt}px">{t}</div>'
def li(items,sym,col,fs=12.5,gap=5):
    return f'<ul style="list-style:none;margin:0;padding:0;font-size:{fs}px;line-height:1.4;color:#333">'+''.join(f'<li style="display:flex;gap:8px;margin:0 0 {gap}px"><span style="color:{col};{MF};flex:none">{sym}</span><span>{x}</span></li>' for x in items)+'</ul>'
def sub(t,c=G,mb=6):return f'<div style="{M};color:{c};margin-bottom:{mb}px">{t}</div>'
def chips(items,c=G,fill=False):
    st=f'background:{c};color:#fff;border:1px solid {c}' if fill else f'border:1px solid {c};color:{c}'
    return '<div style="display:flex;flex-wrap:wrap;gap:6px">'+''.join(f'<span style="font-size:12.5px;{st};padding:3px 9px">{x}</span>' for x in items)+'</div>'
def box(label,txt,mt=8):
    return f'<div style="background:{B};padding:10px 14px;margin-top:{mt}px"><div style="{M};color:{G}">{label}</div><div style="font-size:12.5px;line-height:1.45;color:#111;margin-top:3px">{txt}</div></div>'
def num(n,t,ns=38,ts=21):
    return f'<div style="display:flex;gap:14px;align-items:baseline"><span style="{MF};font-weight:300;font-size:{ns}px;letter-spacing:-.05em;color:{T};line-height:1">{n}</span><span style="font-size:{ts}px;font-weight:500;letter-spacing:-.025em;line-height:1.15;color:#111">{t}</span></div>'
def card(n,t,body,pad=14):return f'<div style="border-top:1px solid {H};padding-top:{pad}px">{num(n,t)}{body}</div>'
def row(l,t):return f'<div style="display:flex;gap:10px;margin-top:8px;font-size:13px;line-height:1.4;color:#333"><span style="{M};color:#767676;flex:none;padding-top:2px;min-width:56px">{l}</span><span>{t}</span></div>'
def cols(a,b,mt=12,gap=22):return f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:{gap}px;margin-top:{mt}px"><div>{a}</div><div>{b}</div></div>'
def steps(items,mt=10):
    n=len(items)
    return f'<div style="display:grid;grid-template-columns:repeat({n},1fr);gap:10px;margin-top:{mt}px">'+''.join(f'<div style="border-top:2px solid {T};padding-top:8px"><div style="{M};color:{T}">{a}</div><div style="font-size:13px;line-height:1.35;color:#111;margin-top:4px">{b}</div></div>' for a,b in items)+'</div>'
def libref(codes='IG-01 · IG-02'):
    return f'<div style="margin-top:12px;display:flex;align-items:center;flex-wrap:wrap;gap:4px"><span style="{M};color:#767676;margin-right:8px">Przykłady z biblioteki</span>'+''.join(f'<span style="{M};border:1px solid {G};color:{G};padding:2px 7px;margin-right:6px">{c}</span>' for c in codes.split(' · '))+'</div>'
def write(n,inner,gap=16,z=1):
    h=head(n);zs=f'zoom:{z};' if z!=1 else ''
    open(P+n+'.dc.html','w').write(h+f'<div style="position:absolute;left:76px;top:100px;width:{round(642/z)}px;{zs}display:flex;flex-direction:column;gap:{gap}px">{inner}</div>'+foot)
