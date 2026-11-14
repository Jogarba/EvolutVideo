import sys; sys.path.insert(0, sys.path[0])
from st_common import *
# Station 04: as sales cross a marked level, Evolut turns on more servers by itself.
bars = [.22, .3, .28, .42, .58, .74, .94]
days = "LMMJVSD"
BW, GAP, X0, BASE, H = 56, 34, 70, 330, 250
bx = [X0 + i * (BW + GAP) for i in range(7)]
bar_html = ''.join(f'<rect id="g-b{i}" x="{x}" y="{BASE - H}" width="{BW}" height="{H}" rx="9" fill="url(#g-bar)"/><text x="{x + BW/2}" y="{BASE + 30}" text-anchor="middle" font-size="20" fill="#94999e" font-family="JetBrains Mono Variable">{d}</text>' for i, (x, d) in enumerate(zip(bx, days)))
grid = ''.join(f'<path d="M{X0 - 20} {BASE - H*f:.0f} H{bx[-1] + BW + 20}" stroke="rgba(242,245,247,.07)" stroke-width="2"/>' for f in (.25, .5, .75, 1))
TH = BASE - H * 0.5
line = "M" + " L".join(f"{x + BW/2} {BASE - v*H:.0f}" for x, v in zip(bx, bars))
units = ''.join(unit(f'g-u{i}', 190 + i * 240, 0, 72, 118, '#399fef' if i == 0 else '#5ed19d', '#66b8ff' if i == 0 else '#9be8c4') for i in range(3))
tags = ''.join(f'<div class="utag" id="g-t{i}" style="left:{190 + i*240 - 90}px">{pill("ok" if i else "info", "Servidor 1" if i == 0 else "+1 automático", "server")}</div>' for i in range(3))
css = f'''
    #g-glow {{ left: 60px; top: 40px; width: 760px; height: 640px; background: radial-gradient(closest-side, rgba(94,209,157,.22), rgba(94,209,157,0)); }}
    #g-card {{ position: absolute; left: 50px; top: 20px; width: 760px; height: 400px; }}
    #g-card h4 {{ position: absolute; left: 32px; top: 24px; font-size: 30px; font-weight: 600; }}
    #g-trend {{ position: absolute; right: 30px; top: 22px; }}
    #g-chart {{ position: absolute; left: 0; top: 40px; overflow: visible; }}
    #g-units {{ position: absolute; left: 0; top: 440px; overflow: visible; }}
    .utag {{ position: absolute; top: 650px; width: 180px; display: flex; justify-content: center; }}
    .utag .pill {{ font-size: 22px; padding: 6px 14px; }}
    #sp-srv {{ left: 155px; top: 250px; width: 550px; height: 140px; padding: 0 30px; display: flex; align-items: center; gap: 22px; }}
    #sp-srv i {{ width: 80px; height: 80px; border-radius: 22px; background: #5ed19d; display: flex; align-items: center; justify-content: center; color: #04120b; flex: none; }}
    #sp-srv svg {{ width: 46px; height: 46px; }} #sp-srv b {{ display: block; font-size: 36px; }} #sp-srv span {{ font-size: 28px; color: #bfc3c7; }}
    #sp-up {{ position: absolute; left: {bx[-1] + BW/2 + 50 - 14:.0f}px; top: -700px; width: 28px; height: 1000px; border-radius: 14px; background: linear-gradient(0deg, rgba(126,240,184,0), #c9ffe6 70%, #ffffff); filter: blur(3px); opacity: 0; }}
    #g-thl {{ font: 600 18px "JetBrains Mono Variable", monospace; letter-spacing: 1px; }}
'''
hero = f'''<div class="glow" id="g-glow"></div>
        <div id="g-card" class="glass"><h4>Tus ventas</h4><div id="g-trend">{pill("ok", "▲ creciendo")}</div>
          <svg id="g-chart" width="760" height="360" viewBox="0 0 760 360">
            <defs><linearGradient id="g-bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7ef0b8"/><stop offset="1" stop-color="#1e76b8" stop-opacity=".45"/></linearGradient></defs>
            {grid}<path d="M{X0 - 20} {BASE} H{bx[-1] + BW + 20}" stroke="rgba(242,245,247,.18)" stroke-width="2"/>
            {bar_html}
            <path id="g-th" d="M{X0 - 20} {TH:.0f} H{bx[-1] + BW + 20}" stroke="#f0b965" stroke-width="3" stroke-dasharray="10 10"/>
            <text id="g-thl" x="{X0 - 14}" y="{TH - 12:.0f}" fill="#f0b965">MÁS VISITAS: +SERVIDORES</text>
            <path id="g-line" d="{line}" fill="none" stroke="#c9ffe6" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>
            {''.join(f'<circle id="g-p{i}" cx="{x + BW/2}" cy="{BASE - v*H:.0f}" r="7" fill="#c9ffe6"/>' for i, (x, v) in enumerate(zip(bx, bars)))}
          </svg></div>
        <svg id="g-units" width="860" height="220" viewBox="0 0 860 220">{UNIT_DEFS}{units}</svg>
        {tags}
        <div class="dim" id="sp-dim"></div>
        <div class="spot" id="sp-srv"><i>{ICON['server']}</i><div><b>+1 servidor activado</b><span>Automático · ahora</span></div></div>
        <div class="orb" id="sp-orb" style="left:430px;top:220px"></div>
        <div id="sp-up"></div>'''
CL, NT, SM, CP, ND = at("grows", "clientes"), at("grows", "nota"), at("grows", "suma"), at("grows", "capacidad"), at("grows", "nada")
js = '\n    '.join(f'tl.fromTo("#g-b{i}", {{ scaleY: 0, transformOrigin: "50% 100%" }}, {{ scaleY: {v}, duration: 0.7, ease: "back.out(1.4)" }}, {CL + i*0.27:.2f}); tl.fromTo("#g-p{i}", {{ scale: 0, transformOrigin: "50% 50%" }}, {{ scale: 1, duration: 0.35, ease: "back.out(2.4)" }}, {CL + 0.4 + i*0.27:.2f});' for i, v in enumerate(bars)) + '''
    tl.fromTo("#g-card", { y: 100, opacity: 0, rotationX: 14, transformPerspective: 1800, filter: "blur(10px)" }, { y: 0, opacity: 1, rotationX: 0, filter: "blur(0px)", duration: 0.8, ease: "expo.out" }, 0.35);
    tl.fromTo("#g-glow", { opacity: 0 }, { opacity: 1, duration: 1.0 }, 0.5);
    tl.to("#g-line", { strokeDashoffset: 0, duration: 2.0, ease: "none" }, @@CL + 0.1@@);
    tl.fromTo(["#g-th", "#g-thl"], { opacity: 0 }, { opacity: 1, duration: 0.4 }, 1.0);
    tl.fromTo("#g-u0", { opacity: 0, y: -60 }, { opacity: 1, y: 0, duration: 0.5, ease: "back.out(1.5)" }, 0.8);
    tl.fromTo("#g-t0", { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.4 }, 1.0);
    // the moment a bar crosses the line, a new server switches on
    [[1, @@SM@@], [2, @@CP@@]].forEach(([i, t]) => {
      tl.fromTo(`#g-u${i}`, { opacity: 0, y: -90 }, { opacity: 1, y: 0, duration: 0.5, ease: "back.out(1.6)" }, t);
      tl.fromTo(`#g-t${i}`, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2)" }, t + 0.2);
    });
    tl.fromTo("#g-th", { strokeWidth: 3 }, { stroke: "#7ef0b8", strokeWidth: 6, duration: 0.3, yoyo: true, repeat: 1 }, @@NT@@);
    tl.fromTo(["#g-u0-g", "#g-u1-g", "#g-u2-g"], { scaleY: 0.2, transformOrigin: "50% 100%" }, { scaleY: 0.6, duration: 1.2, ease: "power2.inOut", stagger: 0.35 }, 2.0);
    tl.fromTo("#g-trend", { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.45, ease: "back.out(2)" }, @@ND - 0.6@@);'''
import re as _re
js = _re.sub(r"@@(.+?)@@", lambda m: str(round(eval(m.group(1)), 3)), js)
js = js + f'''
    tl.fromTo("#sp-orb", {{ scale: 1.4, opacity: 1 }}, {{ scale: 0.1, opacity: 0, duration: 0.45, ease: "power3.in" }}, 0);
    tl.fromTo("#g-card", {{ scale: 0.1 }}, {{ scale: 1, duration: 0.85, ease: "back.out(1.35)", immediateRender: false }}, 0.2);
    ["#sp-srv", "#sp-dim", "#sp-up"].forEach((s) => tl.fromTo(s, {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0));
    tl.to("#sp-dim", {{ opacity: 1, duration: 0.3 }}, {SM + 0.6});
    tl.fromTo("#sp-srv", {{ opacity: 0, scale: 0.3, y: 260 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.7, ease: "back.out(1.5)", immediateRender: false }}, {SM + 0.6});
    tl.to("#sp-srv", {{ opacity: 0, scale: 0.85, y: 120, duration: 0.3, ease: "power2.in" }}, {SM + 1.75});
    tl.to("#sp-dim", {{ opacity: 0, duration: 0.3 }}, {SM + 1.8});'''
exit_js = f'''
    tl.to("#g-b6", {{ scaleY: 3.2, duration: 0.4, ease: "power3.in" }}, {OUTT});
    tl.fromTo("#sp-up", {{ opacity: 0, y: 300 }}, {{ keyframes: [{{ opacity: 1, duration: 0.1 }}, {{ y: -500, duration: 0.4, ease: "power3.in" }}] }}, {OUTT + 0.1});
    tl.to(["#g-card", "#g-units", ".utag", "#st-chip", "#st-h", "#st-pool", "#g-glow"], {{ opacity: 0, filter: "blur(8px)", duration: 0.35, ease: "power2.in" }}, {OUTT + 0.15});'''
js = js + f'''
    // satellite pull-back: from a close-up of the point of light out to the whole chart
    tl.fromTo("#cam", {{ scale: 1.75, y: -140 }}, {{ scale: 1, y: 0, duration: 1.1, ease: SPRING }}, 0.15);
    aim(960, 560, 1.4);
    rig({{ scale: 1.12 }}, {SM + 0.45}, 0.7);
    rig({{ scale: 1.0 }}, {SM + 1.8}, 0.8);'''
exit_js = exit_js + f'''
    // whip-tilt up with the light of the last bar
    kick({{ y: -30 }}, {OUTT + 0.1});
    tl.to("#cam", {{ y: 980, duration: 0.38, ease: "power3.in" }}, {OUTT + 0.1});'''
write("grows", css, hero, js, 4, "CRECIMIENTO", "Crece", "contigo.", exit_js=exit_js)
print("grows")
