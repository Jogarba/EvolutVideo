import sys, math; sys.path.insert(0, sys.path[0])
from common import *
labels = [("Agentes de IA","#67b1f2"),("Documentos","#75dcab"),("Decisiones","#f0b965"),("Servicios","#e48ab3"),("Equipos","#aab4c2"),("Aplicaciones","#67b1f2"),("Bases de datos","#75dcab"),("Alertas","#d2736e")]
cx, cy, rx, ry = 960, 540, 640, 300
pts = []; edges = []; nodes = []; cross = []; pulses = []; pjs = []
for i, (l, c) in enumerate(labels):
    a = -math.pi/2 + i*2*math.pi/len(labels)
    x, y = cx + rx*math.cos(a), cy + ry*math.sin(a); pts.append((x, y))
    edges.append(f'<line class="gr-e" x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{c}" stroke-opacity=".55" stroke-width="3" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>')
    nodes.append(f'<g class="gr-n" id="gr-n{i}"><circle class="gr-halo" cx="{x:.0f}" cy="{y:.0f}" r="56" fill="{c}" fill-opacity=".14"/><circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#0e1318" stroke="{c}" stroke-width="5"/><circle cx="{x:.0f}" cy="{y:.0f}" r="12" fill="{c}"/><text x="{x:.0f}" y="{y+82:.0f}" text-anchor="middle" font-size="32" font-weight="500" fill="#f2f5f7" font-family="Hanken Grotesk Variable" stroke="#070c10" stroke-width="6" paint-order="stroke">{l}</text></g>')
    for k in range(3):
        pid = f'gr-p{i}{k}'
        pulses.append(f'<circle id="{pid}" r="8" fill="{c}" cx="{cx}" cy="{cy}"/>')
        t = 1.1 + k*1.45 + i*0.17
        out = k % 2 == 0
        a0, a1 = ((cx, cy), (x, y)) if out else ((x, y), (cx, cy))
        pjs.append(f'tl.fromTo("#{pid}", {{ attr: {{ cx: {a0[0]:.0f}, cy: {a0[1]:.0f} }}, opacity: 1 }}, {{ attr: {{ cx: {a1[0]:.0f}, cy: {a1[1]:.0f} }}, duration: 0.7, ease: "power1.inOut" }}, {t:.2f}); tl.to("#{pid}", {{ opacity: 0, duration: 0.08 }}, {t+0.7:.2f});')
for i in range(len(pts)):
    (x1, y1), (x2, y2) = pts[i], pts[(i+3) % len(pts)]
    cross.append(f'<line class="gr-e" x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#399fef" stroke-opacity=".22" stroke-width="2" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>')
svg = '\n          '.join(cross + edges + pulses + nodes)
css = '''
    #gr-cam { position: absolute; inset: 0; }
    #gr-svg { position: absolute; left: 0; top: 0; overflow: visible; }
    #gr-core { position: absolute; left: 810px; top: 390px; width: 300px; height: 300px; }
    #gr-coreglow { position: absolute; left: 760px; top: 340px; width: 400px; height: 400px; border-radius: 50%; background: radial-gradient(closest-side, rgba(57,159,239,.45), rgba(57,159,239,0)); }
    #gr-text { position: absolute; left: 0; right: 0; top: 60px; text-align: center; font-size: 60px; }
    #gr-text2 { position: absolute; left: 0; right: 0; top: 968px; text-align: center; font-size: 60px; color: #399fef; }
'''
body = f'''    <div id="gr-cam" data-layout-allow-overflow>
      <div id="gr-coreglow"></div>
      <svg id="gr-svg" width="1920" height="1080" viewBox="0 0 1920 1080">
        <g id="gr-orbit">
          {svg}
        </g>
      </svg>
      <img id="gr-core" src="assets/evolut-isotipo-on-dark.svg" alt="" />
    </div>
    <div id="gr-text" class="kin">Y todo lo que sabe tu empresa,</div>
    <div id="gr-text2" class="kin">en un solo lugar.</div>'''
js = '''
    tl.fromTo("#gr-cam", { scale: 1.3, opacity: 0, filter: "blur(14px)" }, { scale: 1, opacity: 1, filter: "blur(0px)", duration: 0.8, ease: "power3.out" }, 0.25);
    tl.fromTo("#gr-core", { scale: 0.5 }, { scale: 0.5, duration: 0.01 }, 0);
    tl.fromTo("#gr-coreglow", { scale: 0.4, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.8, ease: "expo.out" }, 0.3);
    tl.fromTo(".gr-n", { opacity: 0, scale: 0.3, transformOrigin: "50% 50%" }, { opacity: 1, scale: 1, duration: 0.45, ease: "back.out(1.6)", stagger: 0.12 }, 0.35);
    tl.to(".gr-e", { strokeDashoffset: 0, duration: 0.6, ease: "power2.out", stagger: 0.06 }, 0.5);
    tl.fromTo(".gr-halo", { scale: 1, transformOrigin: "50% 50%" }, { scale: 1.35, duration: 0.5, ease: "power2.out", yoyo: true, repeat: 1, stagger: 0.12 }, 1.6);
    tl.fromTo("#gr-orbit", { rotation: 0, svgOrigin: "960 540" }, { rotation: 24, svgOrigin: "960 540", duration: 6.0, ease: "none" }, 0);
    tl.fromTo(".gr-n", { rotation: 0 }, { rotation: -24, transformOrigin: "50% 50%", duration: 6.0, ease: "none" }, 0);
    ''' + '\n    '.join(pjs) + '''
    tl.fromTo("#gr-text", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.2 }, 0.25);
    tl.fromTo("#gr-text2", { opacity: 0, filter: "blur(10px)", scale: 1.08 }, { opacity: 1, filter: "blur(0px)", scale: 1, duration: 0.22, ease: "expo.out" }, 2.9);
    // everything collapses into the core, which becomes the end mark
    tl.to(["#gr-text", "#gr-text2"], { opacity: 0, filter: "blur(8px)", duration: 0.18 }, 5.9);
    tl.to("#gr-orbit", { scale: 0, opacity: 0, svgOrigin: "960 540", duration: 0.55, ease: "power3.in" }, 6.05);
    tl.to("#gr-core", { scale: 1, duration: 0.6, ease: "expo.out" }, 6.35);
    tl.to("#gr-coreglow", { opacity: 0, scale: 0.6, duration: 0.45, ease: "power2.in" }, 6.3);'''
open(OUT + "graph.html", "w").write(scene("graph", css, body, js))
