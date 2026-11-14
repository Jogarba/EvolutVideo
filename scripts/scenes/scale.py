import sys; sys.path.insert(0, sys.path[0])
from common import *
K = 0.577
import math
# visits enter at one node and are routed along visible links to each replica
ENTRY = (70, 200)
CX = [330, 545, 760]; Y0 = 60; UW, UH = 80, 128
cubes = ''.join(unit(f's-c{i}', cx, Y0, UW, UH, '#399fef' if i == 0 else '#f4b85a', '#66b8ff' if i == 0 else '#ffd28a') for i, cx in enumerate(CX))
def port(cx):  # centre of the replica's lid
    return (cx, Y0 + UW * K)
def bez(a, b):
    (x0, y0), (x3, y3) = a, b
    return (x0, y0, x0 + 70, y0 - 150, x3, y3 - 170, x3, y3)
def pt(c, u):
    x0, y0, x1, y1, x2, y2, x3, y3 = c
    m = 1 - u
    return (m**3*x0 + 3*m*m*u*x1 + 3*m*u*u*x2 + u**3*x3, m**3*y0 + 3*m*m*u*y1 + 3*m*u*u*y2 + u**3*y3)
curves = [bez((ENTRY[0] + 36, ENTRY[1]), port(cx)) for cx in CX]
D = lambda c: f'M{c[0]:.0f} {c[1]:.0f} C{c[2]:.0f} {c[3]:.0f} {c[4]:.0f} {c[5]:.0f} {c[6]:.0f} {c[7]:.0f}'
links = ''.join(f'<path id="s-lt{i}" d="{D(c)}" fill="none" stroke="#203a52" stroke-width="7" stroke-linecap="round" opacity="0"/><path id="s-l{i}" d="{D(c)}" fill="none" stroke="{"#399fef" if i == 0 else "#f4b85a"}" stroke-width="3" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>' for i, c in enumerate(curves))
ex, ey = ENTRY
entry = (f'<g id="s-entry"><circle cx="{ex}" cy="{ey}" r="46" fill="#399fef" fill-opacity=".12"/><circle cx="{ex}" cy="{ey}" r="34" fill="#0e1318" stroke="#66b8ff" stroke-width="3"/>'
         f'<g transform="translate({ex-16} {ey-16}) scale(1.35)" fill="none" stroke="#a6d0f6" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></g>'
         f'<text x="{ex}" y="{ey+76}" text-anchor="middle" font-size="27" fill="#bfc3c7" font-family="Hanken Grotesk Variable">Visitas</text></g>')
times = []
t = 4.9
while t < 9.0:
    load = math.exp(-((t - 6.6) / 0.9) ** 2)
    times.append(round(t, 2)); t += 0.36 - 0.24 * load
dots = ''.join(f'<circle id="s-d{i}" class="dot" cx="{ex}" cy="{ey}" r="9"/>' for i in range(len(times)))
dot_js = []
for i, t in enumerate(times):
    k = i % (3 if 6.05 < t < 7.55 else 1)
    pts = [pt(curves[k], u / 8) for u in range(1, 9)]
    frames = ', '.join(f'{{ attr: {{ cx: {x:.0f}, cy: {y:.0f} }}, duration: 0.07, ease: "none" }}' for x, y in pts)
    dot_js.append(f'tb.fromTo("#s-d{i}", {{ attr: {{ cx: {ex+36}, cy: {ey} }}, opacity: 1 }}, {{ keyframes: [{frames}] }}, {t});')
    dot_js.append(f'tb.to("#s-d{i}", {{ opacity: 0, duration: 0.06 }}, {t+0.56:.2f});')
    dot_js.append(f'tb.to("#s-c{k}-led{i % 3}", {{ fill: "#d6ffe9", duration: 0.06, yoyo: true, repeat: 1 }}, {t+0.56:.2f});')
gauge_js = [f'tb.fromTo("#s-c{i}-g", {{ scaleY: 0.15, transformOrigin: "50% 100%" }}, {{ scaleY: {v}, duration: 0.6, ease: "power2.out" }}, {t0});' for i, v, t0 in ((0, .55, 4.7), (1, .5, 5.85), (2, .45, 6.05))]
gauge_js += ['tb.to("#s-c0-g", { scaleY: 0.9, duration: 0.8, ease: "power2.inOut" }, 5.2);', 'tb.to("#s-c0-g", { scaleY: 0.5, duration: 0.6, ease: "power2.inOut" }, 6.1);', 'tb.to("#s-c0-g", { scaleY: 0.3, duration: 0.8, ease: "power2.inOut" }, 7.7);']
link_js = ['tb.to("#s-l0", { strokeDashoffset: 0, duration: 0.5, ease: "power2.out" }, 4.7);',
           'tb.to("#s-lt0", { opacity: 1, duration: 0.3 }, 4.7);',
           'tb.to("#s-lt1", { opacity: 1, duration: 0.3 }, 5.85);',
           'tb.to("#s-lt2", { opacity: 1, duration: 0.3 }, 6.05);',
           'tb.to(["#s-lt2", "#s-lt1"], { opacity: 0, duration: 0.3, ease: "power2.in", stagger: 0.12 }, 7.65);',
           'tb.fromTo("#s-entry", { opacity: 0, scale: 0.6, transformOrigin: "50% 50%" }, { opacity: 1, scale: 1, duration: 0.45, ease: "back.out(1.6)" }, 4.55);',
           'tb.to("#s-l1", { strokeDashoffset: 0, duration: 0.4, ease: "power2.out" }, 5.85);',
           'tb.to("#s-l2", { strokeDashoffset: 0, duration: 0.4, ease: "power2.out" }, 6.05);',
           'tb.to(["#s-l2", "#s-l1"], { strokeDashoffset: 1, duration: 0.3, ease: "power2.in", stagger: 0.12 }, 7.6);']
dot_js = dot_js + gauge_js + link_js

rings = [("CPU", "#399fef", 38), ("Memoria", "#399fef", 55), ("Disco", "#399fef", 30)]
ring_html = ''.join(f'''<div class="ring"><svg viewBox="0 0 220 220"><circle cx="110" cy="110" r="92" fill="none" stroke="rgba(242,245,247,.12)" stroke-width="15"/><circle cx="110" cy="110" r="76" fill="rgba(7,12,16,.55)"/><circle id="s-g{i}" cx="110" cy="110" r="92" fill="none" stroke="{c}" stroke-width="15" stroke-linecap="round" stroke-dasharray="0 578" transform="rotate(-90 110 110)"/></svg><b class="mono" id="s-v{i}">0%</b><span>{n}</span></div>''' for i, (n, c, v) in enumerate(rings))
css = '''
    #s-world { position: absolute; inset: 0; }
    #s-btn { position: absolute; left: 640px; top: 480px; width: 640px; height: 120px; display: flex; align-items: center; justify-content: center; gap: 18px; font-size: 44px; font-weight: 600; }
    #s-btn svg { width: 44px; height: 44px; color: #399fef; }
    #s-db { position: absolute; left: 400px; top: 250px; width: 1120px; padding: 46px 54px; }
    .hd { display: flex; align-items: center; gap: 24px; }
    .tile { width: 88px; height: 88px; border-radius: 20px; background: #132636; color: #399fef; display: flex; align-items: center; justify-content: center; }
    .tile svg { width: 46px; height: 46px; }
    .hd .t { font-size: 48px; font-weight: 600; } .hd .s { font: 500 28px "JetBrains Mono Variable", monospace; color: #94999e; margin-top: 4px; }
    .hd .pill { margin-left: auto; }
    .rings { display: flex; justify-content: space-around; margin-top: 36px; }
    .ring { position: relative; text-align: center; font-size: 30px; color: #bfc3c7; width: 220px; }
    .ring svg { width: 220px; height: 220px; display: block; margin-bottom: 10px; }
    .ring b { position: absolute; left: 0; right: 0; top: 0; height: 220px; display: flex; align-items: center; justify-content: center; font-size: 46px; font-weight: 600; color: #f2f5f7; }
    #s-link { margin-top: 30px; height: 80px; padding: 0 26px; display: flex; align-items: center; gap: 16px; font-size: 30px; }
    #s-link .pill { margin-left: auto; }
    #s-auto { position: absolute; left: 860px; top: 230px; width: 960px; height: 650px; padding: 40px 48px; overflow: hidden; }
    #s-auto h4 { font-size: 40px; font-weight: 600; }
    #s-auto p { font-size: 30px; color: #bfc3c7; line-height: 1.45; margin-top: 12px; width: 840px; }
    #s-stage { position: absolute; left: 48px; top: 220px; width: 864px; height: 360px; }
    #s-stage svg { overflow: visible; }
    .dot { fill: #a6d0f6; filter: drop-shadow(0 0 6px #399fef); }
    #s-evt { position: absolute; left: 48px; width: 864px; top: 556px; display: grid; justify-items: center; }
    #s-evt > span { grid-area: 1 / 1; }
    #s-text, #s-text2 { position: absolute; left: 0; right: 0; top: 80px; text-align: center; font-size: 70px; }
    #s-text b, #s-text2 b { color: #399fef; font-weight: 400; }
'''
body = f'''    <div id="s-world">
      <div id="s-btn" class="frost">{ICON["db"]}+ Base de datos</div>
      <div id="s-db" class="glass">
        <div class="hd"><div class="tile">{ICON["db"]}</div><div><div class="t">Postgres</div><div class="s">portal-clientes-db</div></div>{pill("ok","Lista",None,"s-ready")}</div>
        <div class="rings">{ring_html}</div>
        <div id="s-link" class="raised">{ICON["git"].replace('class="icon"','class="icon" style="width:34px;height:34px;color:#94999e"')}Conectada a portal-clientes{pill("ok","dev · qa · prod")}</div>
      </div>
      <div id="s-auto" class="glass">
        <h4>Cómo escala</h4>
        <p>Cuando llega más trabajo suma réplicas iguales, de 1 a 3: como abrir más cajas en un supermercado.</p>
        <div id="s-stage"><svg width="864" height="330" viewBox="0 0 864 330">
          {UNIT_DEFS}{cubes}{links}{entry}{dots}
        </svg></div>
        <div id="s-evt">{pill("warn","Escalado: 1 → 3 réplicas",None,"s-e1")}{pill("info","Escalado: 3 → 1 réplicas","info","s-e2")}</div>
      </div>
    </div>
    <div id="s-text" class="kin">Tus datos, <b>en un clic.</b></div>
    <div id="s-text2" class="kin">Crece sola, <b>cuando más la necesitas.</b></div>
    <div class="cursor" id="s-cursor">{CURSOR}</div>'''
js = '''
    tl.fromTo("#s-world", { y: 1080, filter: "blur(10px)" }, { y: 0, filter: "blur(0px)", duration: 0.6, ease: "power2.inOut" }, 0);
    const tb = gsap.timeline(); tl.add(tb, 0.3);
    tb.fromTo("#s-text", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.18 }, 0.3);
    tb.fromTo("#s-cursor", { x: 1950, y: 1150 }, { x: 1100, y: 535, duration: 0.5, ease: "power3.out" }, 0.35);
    tb.to("#s-cursor", { scale: 0.82, duration: 0.07 }, 0.95);
    tb.to("#s-btn", { scale: 0.95, duration: 0.07 }, 0.95);
    tb.to("#s-cursor", { opacity: 0, duration: 0.12 }, 1.08);
    // the pill opens into the database card
    tb.to("#s-btn", { scaleX: 1.75, scaleY: 5.3, opacity: 0, duration: 0.35, ease: "power3.inOut" }, 1.05);
    tb.fromTo("#s-db", DEPTH, LAND, 1.15);
    tb.fromTo("#s-db .hd, #s-db .ring, #s-link", { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.4, ease: "expo.out", stagger: 0.06 }, 1.3);
    tb.fromTo("#s-ready", { scale: 0.5 }, { scale: 1, duration: 0.35, ease: "back.out(2)" }, 2.2);
    [[0, 38], [1, 55], [2, 30]].forEach(([i, v]) => {
      tb.to(`#s-g${i}`, { strokeDasharray: `${5.78 * v} 578`, duration: 1.1, ease: "power3.out" }, 1.6 + i * 0.12);
      const o = { v: 0 };
      tb.to(o, { v, duration: 1.1, ease: "power3.out", onUpdate: () => { document.querySelector("#s-v" + i).textContent = Math.round(o.v) + "%"; } }, 1.6 + i * 0.12);
    });

    // carry the database aside; scaling builds beside it
    tb.to("#s-text", { opacity: 0, filter: "blur(8px)", duration: 0.18 }, 4.05);
    tb.to("#s-db", { x: -520, y: 60, scale: 0.62, duration: 0.6, ease: "power2.inOut" }, 4.15);
    tb.fromTo("#s-auto", { ...DEPTH, x: 160 }, { ...LAND, x: 0 }, 4.4);
    tb.fromTo("#s-text2", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.18 }, 4.55);
    tb.fromTo("#s-c0", { opacity: 0, y: -60 }, { opacity: 1, y: 0, duration: 0.45, ease: "back.out(1.5)" }, 4.6);
    tb.fromTo("#s-c1", { opacity: 0, y: -90 }, { opacity: 1, y: 0, duration: 0.45, ease: "back.out(1.6)" }, 5.75);
    tb.fromTo("#s-c2", { opacity: 0, y: -90 }, { opacity: 1, y: 0, duration: 0.45, ease: "back.out(1.6)" }, 5.95);
    tb.to(["#s-c2", "#s-c1"], { opacity: 0, y: -40, duration: 0.3, ease: "power3.in", stagger: 0.12 }, 7.7);
    tb.fromTo("#s-e1", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.35, ease: "expo.out" }, 5.8);
    tb.to("#s-e1", { opacity: 0, y: -16, duration: 0.2 }, 7.65);
    tb.fromTo("#s-e2", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.35, ease: "expo.out" }, 7.85);
    
    tl.to(["#s-world", "#s-text2"], { opacity: 0, filter: "blur(14px)", scale: 0.94, duration: 0.4, ease: "power2.in" }, 10.1);''' + '\n    '.join(dot_js) + '''
    tl.to(["#s-world", "#s-text2"], { opacity: 0, filter: "blur(14px)", scale: 0.94, duration: 0.4, ease: "power2.in" }, 10.1);'''
open(OUT + "scale.html", "w").write(scene("scale", css, body, js))
