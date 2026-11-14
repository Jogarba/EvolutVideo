import sys; sys.path.insert(0, sys.path[0])
from common import *
K = 0.577
units = [(160, 120), (410, 120), (660, 120)]
W, H = 90, 168
rack = ''.join(unit(f'lv-u{i}', cx, y0, W, H) for i, (cx, y0) in enumerate(units))
BY = units[0][1] + 2*W*K + H + 16
# the units share one network: a lit bus between their platforms with traffic running along it
bus = f'<path d="M{units[0][0]} {BY} L{units[-1][0]} {BY}" stroke="#203a52" stroke-width="6" stroke-linecap="round"/><path id="lv-bus" d="M{units[0][0]} {BY} L{units[-1][0]} {BY}" stroke="#66b8ff" stroke-width="3" stroke-dasharray="8 14" stroke-linecap="round"/>'
tokens = ''
tok_js = []
for i, (cx, y0) in enumerate(units):
    for k in range(9):
        tid = f'lv-tk{i}{k}'
        tokens += f'<polygon id="{tid}" class="tok" points="{cx},-32 {cx+12},-20 {cx},-8 {cx-12},-20"/>'
        t = 0.55 + k * 0.92 + i * 0.29
        tok_js.append(f'tl.fromTo("#{tid}", {{ y: 0, opacity: 0 }}, {{ y: {y0+W*K+12:.0f}, opacity: 1, duration: 0.42, ease: "power2.in" }}, {t:.2f}); tl.to("#{tid}", {{ opacity: 0, duration: 0.08 }}, {t+0.42:.2f});')
        tok_js.append(f'tl.to("#lv-u{i}-led{k%3}", {{ fill: "#d6ffe9", duration: 0.06, yoyo: true, repeat: 1 }}, {t+0.42:.2f});')
levels = [[.35, .62, .48, .7, .52, .6], [.42, .55, .72, .5, .64, .58], [.3, .5, .44, .66, .58, .47]]
for i, lv in enumerate(levels):
    tok_js.append(f'tl.fromTo("#lv-u{i}-g", {{ scaleY: 0.1, transformOrigin: "50% 100%" }}, {{ scaleY: {lv[0]}, duration: 0.6, ease: "power3.out" }}, 0.4);')
    for j, v in enumerate(lv[1:]):
        tok_js.append(f'tl.to("#lv-u{i}-g", {{ scaleY: {v}, duration: 0.9, ease: "power1.inOut" }}, {1.2 + j*1.5 + i*0.2:.2f});')
def spark(id, d, color):
    return f'<svg width="200" height="56" viewBox="0 0 200 56" style="position:absolute;left:26px;bottom:20px"><path id="{id}" d="{d}" fill="none" stroke="{color}" stroke-width="4" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>'
kpis = [("Tráfico", pill("info", "normal"), spark("lv-k0", "M0 40 C30 38 40 20 70 26 S120 10 140 18 S180 6 200 10", "#399fef")),
        ("Errores", pill("ok", "ninguno"), spark("lv-k1", "M0 46 H200", "#5ed19d")),
        ("Respuesta", pill("ok", "rápida"), spark("lv-k2", "M0 30 C40 34 60 22 90 28 S150 24 200 26", "#5ed19d"))]
kpi_html = ''.join(f'<div class="kpi glass" id="lv-kp{i}" style="left:{1000+i*275}px"><span class="muted" style="font-size:28px">{n}</span><div style="margin-top:12px">{p}</div>{s}</div>' for i, (n, p, s) in enumerate(kpis))
logs = [("200","GET /","2"),("200","POST /api/pedidos","1"),("200","GET /api/clientes","3"),("201","POST /api/pedidos","3"),("200","GET /api/catalogo","1"),("200","GET /","3"),("200","GET /api/clientes/42","2"),("200","POST /api/sesion","1"),("200","GET /api/catalogo","2"),("200","GET /api/pedidos/7","3"),("201","POST /api/pagos","1"),("200","GET /","2")]
log_html = ''.join(f'<div><i>{c}</i> {p:<24} <span class="muted">réplica {r}</span></div>' for c, p, r in logs)
css = '''
    #lv-flash { position: absolute; inset: 0; background: #0f3424; }
    #lv-world { position: absolute; inset: 0; }
    #lv-cam { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; transform-origin: 0 0; }
    .card { position: absolute; overflow: hidden; }
    .cap { position: absolute; left: 34px; top: 26px; font: 500 28px "JetBrains Mono Variable", monospace; color: #94999e; letter-spacing: 1px; }
    #lv-head { position: absolute; left: 120px; top: 168px; display: flex; gap: 18px; align-items: center; }
    #lv-head b { font: 600 44px "JetBrains Mono Variable", monospace; margin-right: 10px; }
    #lv-rack { left: 120px; top: 250px; width: 820px; height: 610px; }
    #lv-rack svg { position: absolute; left: 0; top: 70px; overflow: visible; }
    .led { fill: #5ed19d; }
    .tok { fill: #a6d0f6; }
    .rlabel { position: absolute; top: 548px; width: 200px; text-align: center; font: 500 28px "JetBrains Mono Variable", monospace; color: #5ed19d; }
    .kpi { position: absolute; top: 250px; width: 255px; height: 190px; padding: 22px 26px; }
    #lv-chart { left: 1000px; top: 470px; width: 800px; height: 240px; }
    #lv-logs { left: 1000px; top: 730px; width: 800px; height: 150px; }
    #lv-logwin { position: absolute; left: 34px; right: 34px; top: 70px; bottom: 14px; overflow: hidden; }
    #lv-loglines { font: 500 28px/1.6 "JetBrains Mono Variable", monospace; color: #bfc3c7; white-space: pre; }
    #lv-loglines i { color: #5ed19d; font-style: normal; }
    #lv-band { position: absolute; left: 0; right: 0; bottom: 0; height: 260px; background: linear-gradient(180deg, rgba(5,8,13,0), rgba(5,8,13,.9) 55%); }
    #lv-text { position: absolute; left: 120px; top: 900px; font-size: 70px; white-space: nowrap; }
    #lv-slot { display: inline-block; position: relative; width: 760px; height: 96px; overflow: hidden; vertical-align: bottom; }
    #lv-slot span { position: absolute; left: 0; top: 0; }
    #lv-slot span:not(:first-child) { color: #399fef; }
    #lv-slot span:first-child { color: #399fef; }
    #lv-rt { position: absolute; left: 0; right: 0; top: 900px; text-align: center; font-size: 76px; }
    #lv-rt b { color: #399fef; font-weight: 400; }
'''
body = f'''    <div id="lv-world">
      <div id="lv-cam" data-layout-allow-overflow>
        <div id="lv-head"><b>portal-clientes</b>{pill("info","PROD","globe")}{pill("info","v1.4.0","git")}{pill("ok","3 de 3 réplicas listas")}</div>
        <div id="lv-rack" class="card glass">
          <div class="cap">RÉPLICAS</div>
          <svg width="820" height="560" viewBox="0 0 820 560">{UNIT_DEFS}{bus}{tokens}{rack}</svg>
          <div class="rlabel" style="left:60px">réplica 1</div><div class="rlabel" style="left:310px">réplica 2</div><div class="rlabel" style="left:560px">réplica 3</div>
        </div>
        {kpi_html}
        <div id="lv-chart" class="card glass">
          <div class="cap">TRÁFICO · EN VIVO</div>
          <svg width="800" height="240" viewBox="0 0 800 260" style="position:absolute;left:0;top:0">
            <defs><linearGradient id="lv-area" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#399fef" stop-opacity=".35"/><stop offset="1" stop-color="#399fef" stop-opacity="0"/></linearGradient>
            <clipPath id="lv-clip"><rect id="lv-cliprect" x="0" y="0" width="800" height="260"/></clipPath></defs>
            <path d="M34 120 H766 M34 170 H766 M34 220 H766" stroke="rgba(242,245,247,.07)" stroke-width="2"/>
            <g clip-path="url(#lv-clip)">
              <path d="M34 210 C110 200 140 170 200 178 S300 130 360 146 S460 100 520 116 S620 80 680 90 S740 74 766 76 V240 H34Z" fill="url(#lv-area)"/>
              <path d="M34 210 C110 200 140 170 200 178 S300 130 360 146 S460 100 520 116 S620 80 680 90 S740 74 766 76" fill="none" stroke="#399fef" stroke-width="6"/>
              <path d="M34 232 C120 228 160 216 220 220 S330 200 380 208 S480 190 540 196 S640 178 700 182 S740 176 766 177" fill="none" stroke="#5ed19d" stroke-width="5"/>
            </g>
          </svg>
          <div id="lv-head-dot" style="position:absolute;left:0;top:0;width:22px;height:22px;border-radius:50%;background:#399fef;box-shadow:0 0 22px #399fef"></div>
        </div>
        <div id="lv-logs" class="card glass">
          <div class="cap">REGISTROS</div>
          <div id="lv-logwin"><div id="lv-loglines">{log_html}</div></div>
        </div>
      </div>
    </div>
    <div id="lv-band"></div>
    <div id="lv-text" class="kin">Mira <span id="lv-slot"><span id="lv-s1">tu app,</span><span id="lv-s2">tus visitas,</span><span id="lv-s3">cada detalle,</span></span></div>
    <div id="lv-rt" class="kin">Todo, <b>en vivo.</b></div>
    <div id="lv-flash"></div>'''
headpath = [(34,210),(200,178),(360,146),(520,116),(680,90),(766,76)]
js = '''
    tl.fromTo("#lv-flash", { opacity: 1 }, { opacity: 0, duration: 0.35, ease: "power2.out" }, 0);
    tl.fromTo("#lv-world", { clipPath: "circle(0% at 50% 50%)" }, { clipPath: "circle(80% at 50% 50%)", duration: 0.45, ease: "power3.out" }, 0);
    tl.fromTo("#lv-cam", cam(530, 560, 1.22), { ...cam(530, 560, 1.15), duration: 2.2, ease: "power2.out" }, 0);
    tl.to("#lv-cam", { ...cam(1400, 500, 1.4), duration: 0.55, ease: "power2.inOut" }, 2.35);
    tl.to("#lv-cam", { ...cam(1400, 760, 1.45), duration: 0.55, ease: "power2.inOut" }, 4.55);
    tl.to("#lv-cam", { ...cam(960, 540, 0.95), duration: 0.6, ease: "power2.inOut" }, 6.6);
    tl.fromTo(["#lv-head", "#lv-rack", "#lv-kp0", "#lv-kp1", "#lv-kp2", "#lv-chart", "#lv-logs"], DEPTH, { ...LAND, stagger: 0.07 }, 0.1);
    ["#lv-u0", "#lv-u1", "#lv-u2"].forEach((u, i) => tl.fromTo(u, { opacity: 0, y: -80 }, { opacity: 1, y: 0, duration: 0.55, ease: "back.out(1.4)" }, 0.25 + i * 0.12));
    ''' + '\n    '.join(tok_js) + '''
    ["#lv-k0", "#lv-k1", "#lv-k2"].forEach((k, i) => tl.to(k, { strokeDashoffset: 0, duration: 1.4, ease: "power2.out" }, 0.6 + i * 0.1));
    // the chart is drawn by a live head that keeps moving
    tl.fromTo("#lv-cliprect", { attr: { width: 34 } }, { attr: { width: 766 }, duration: 7.5, ease: "none" }, 0.5);
    tl.fromTo("#lv-head-dot", { x: 23, y: 199 }, { keyframes: ''' + str([{"x": x-11, "y": y-11, "duration": 1.5, "ease": "none"} for x, y in headpath[1:]]).replace("'", '"') + ''' }, 0.5);
    tl.fromTo("#lv-bus", { strokeDashoffset: 0 }, { strokeDashoffset: -440, duration: 9.5, ease: "none" }, 0.3);
    tl.fromTo(["#lv-u0-base", "#lv-u1-base", "#lv-u2-base"], { strokeDashoffset: 0 }, { strokeDashoffset: 180, duration: 9.5, ease: "none" }, 0.3);
    tl.fromTo("#lv-loglines", { y: 0 }, { y: -400, duration: 9, ease: "steps(9)" }, 0.8);
    tl.fromTo("#lv-text", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.18 }, 0.2);
    tl.fromTo("#lv-s2", { yPercent: 110 }, { yPercent: 110, duration: 0.01 }, 0);
    tl.fromTo("#lv-s3", { yPercent: 110 }, { yPercent: 110, duration: 0.01 }, 0);
    tl.to("#lv-s1", { yPercent: -110, duration: 0.14, ease: "power2.in" }, 2.45);
    tl.to("#lv-s2", { yPercent: 0, duration: 0.18, ease: "back.out(1.4)" }, 2.55);
    tl.to("#lv-s2", { yPercent: -110, duration: 0.14, ease: "power2.in" }, 4.65);
    tl.to("#lv-s3", { yPercent: 0, duration: 0.18, ease: "back.out(1.4)" }, 4.75);
    tl.to("#lv-text", { opacity: 0, filter: "blur(8px)", duration: 0.15 }, 6.5);
    tl.fromTo("#lv-rt", { opacity: 0, filter: "blur(10px)", scale: 1.08 }, { opacity: 1, filter: "blur(0px)", scale: 1, duration: 0.22, ease: "expo.out" }, 7.0);
    tl.to(["#lv-world", "#lv-rt", "#lv-band"], { y: -1080, filter: "blur(10px)", duration: 0.6, ease: "power2.inOut" }, 9.7);'''
open(OUT + "live.html", "w").write(scene("live", css, body, js))
