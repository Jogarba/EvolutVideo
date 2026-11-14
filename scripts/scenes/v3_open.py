import sys, math, random; sys.path.insert(0, sys.path[0])
from common import *
rnd = random.Random(21)
A = lambda w, line=None, nth=1: at("hook", w, line, nth)

# ── hook: an idea lights up and goes online ───────────────────────
BX, BY = 960, 470
nodes = []
while len(nodes) < 30:
    x, y = rnd.randint(80, 1840), rnd.randint(170, 900)
    if math.hypot(x - BX, y - BY) > 260: nodes.append((x, y))
links = ''.join(f'<path class="hl" d="M{BX} {BY} Q{(BX + x) / 2 + rnd.randint(-120, 120)} {(BY + y) / 2 + rnd.randint(-120, 120)} {x} {y}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>' for x, y in nodes)
mesh = ''.join(f'<line class="hm" x1="{nodes[i][0]}" y1="{nodes[i][1]}" x2="{nodes[j][0]}" y2="{nodes[j][1]}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>' for i in range(len(nodes)) for j in range(i + 1, len(nodes)) if math.hypot(nodes[i][0] - nodes[j][0], nodes[i][1] - nodes[j][1]) < 260)
dots = ''.join(f'<g class="hn"><circle cx="{x}" cy="{y}" r="16" fill="#399fef" fill-opacity=".18"/><circle cx="{x}" cy="{y}" r="6" fill="#a6d0f6"/></g>' for x, y in nodes)
hook_css = '''
    #h-cam { position: absolute; inset: 0; transform-origin: 960px 470px; }
    #h-svg { position: absolute; left: 0; top: 0; overflow: visible; }
    .hl { fill: none; stroke: #66b8ff; stroke-width: 2.5; }
    .hm { stroke: #66b8ff; stroke-opacity: .35; stroke-width: 1.5; }
    #h-warm { position: absolute; left: 660px; top: 170px; width: 600px; height: 600px; border-radius: 50%; background: radial-gradient(closest-side, rgba(255,196,110,.65), rgba(240,185,101,.18) 45%, rgba(240,185,101,0)); }
    #h-flash { position: absolute; inset: 0; background: radial-gradient(circle at 50% 44%, #ffffff, rgba(166,208,246,.8) 30%, rgba(57,159,239,0) 70%); }
    .ring { position: absolute; left: 760px; top: 270px; width: 400px; height: 400px; border-radius: 50%; border: 3px solid rgba(166,208,246,.8); opacity: 0; }
'''
hook_body = f'''    <div id="h-cam">
      <div id="h-warm"></div>
      <svg id="h-svg" width="1920" height="1080" viewBox="0 0 1920 1080">
        <defs><radialGradient id="h-glass" cx="50%" cy="40%"><stop offset="0" stop-color="#ffe2b0" stop-opacity=".55"/><stop offset=".6" stop-color="#f0b965" stop-opacity=".12"/><stop offset="1" stop-color="#f0b965" stop-opacity="0"/></radialGradient></defs>
        <g id="h-net">{mesh}{links}{dots}</g>
        <g id="h-bulb" transform="translate({BX - 110} {BY - 175})">
          <path id="h-glassfill" d="M110 0 C45 0 0 48 0 110 C0 158 30 186 52 210 C66 226 72 244 72 262 L148 262 C148 244 154 226 168 210 C190 186 220 158 220 110 C220 48 175 0 110 0 Z" fill="url(#h-glass)" opacity="0"/>
          <path id="h-glass1" d="M110 0 C45 0 0 48 0 110 C0 158 30 186 52 210 C66 226 72 244 72 262 L148 262 C148 244 154 226 168 210 C190 186 220 158 220 110 C220 48 175 0 110 0 Z" fill="none" stroke="#ffd79a" stroke-width="5" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>
          <path id="h-base" d="M74 278 H146 M78 296 H142 M86 314 H134 M98 332 H122" stroke="#d7dde3" stroke-width="7" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>
          <path id="h-fil" d="M84 262 L84 170 L98 138 L110 170 L122 138 L136 170 L136 262" fill="none" stroke="#ffcf85" stroke-width="5" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>
          <circle id="h-spark" cx="110" cy="150" r="9" fill="#fff4dc"/>
        </g>
      </svg>
      <div class="ring" id="h-r0"></div><div class="ring" id="h-r1"></div><div class="ring" id="h-r2"></div>
    </div>
    <div id="h-flash"></div>'''
hook_js = f'''
    // a warm spark in the dark; the camera creeps in
    tl.fromTo("#h-cam", {{ scale: 1.25 }}, {{ scale: 1.45, duration: {A("linea") + 0.4}, ease: "sine.inOut" }}, 0);
    tl.fromTo("#h-spark", {{ scale: 0, opacity: 0, transformOrigin: "50% 50%" }}, {{ scale: 1, opacity: 1, duration: 0.6, ease: "back.out(2)" }}, 0.2);
    tl.fromTo("#h-warm", {{ scale: 0.2, opacity: 0 }}, {{ scale: 0.6, opacity: 0.7, duration: 0.8, ease: "back.out(1.4)" }}, 0.3);
    tl.fromTo(["#h-flash", ".hn"], {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0);
    // "gran idea": the bulb draws itself around the spark
    tl.to("#h-glass1", {{ strokeDashoffset: 0, duration: 0.7, ease: "power2.inOut" }}, {A("proxima")});
    tl.to("#h-fil", {{ strokeDashoffset: 0, duration: 0.5, ease: "power2.out" }}, {A("gran")});
    tl.to("#h-base", {{ strokeDashoffset: 0, duration: 0.45, ease: "power2.out" }}, {A("gran") + 0.15});
    tl.to("#h-glassfill", {{ opacity: 1, duration: 0.4 }}, {A("idea")});
    tl.to("#h-warm", {{ scale: 1.15, opacity: 1, duration: 0.6, ease: "back.out(1.6)" }}, {A("idea")});
    // "en línea": the light leaves the bulb as a network that floods the frame
    tl.to(".hl", {{ strokeDashoffset: 0, duration: 0.55, ease: "power2.out", stagger: 0.015 }}, {A("en")});
    tl.fromTo(".hn", {{ opacity: 0, scale: 0.2, transformOrigin: "50% 50%" }}, {{ opacity: 1, scale: 1, duration: 0.45, ease: "back.out(2.4)", stagger: 0.015 }}, {A("linea")});
    tl.to(".hm", {{ strokeDashoffset: 0, duration: 0.5, ease: "power2.out", stagger: 0.004 }}, {A("linea") + 0.15});
    // "hoy mismo": a flash, rings, and the camera kicks back to show the whole web of light
    tl.fromTo("#h-flash", {{ opacity: 0 }}, {{ keyframes: [{{ opacity: 0.85, duration: 0.08 }}, {{ opacity: 0, duration: 0.5 }}] }}, {A("hoy")});
    [0, 1, 2].forEach((i) => tl.fromTo(`#h-r${{i}}`, {{ scale: 0.2, opacity: 0.9 }}, {{ scale: 3.2, opacity: 0, duration: 1.2, ease: "power2.out" }}, {A("hoy")} + i * 0.18));
    tl.to("#h-cam", {{ scale: 1.08, duration: 0.14, ease: "power2.in" }}, {A("hoy") - 0.14});
    tl.to("#h-cam", {{ scale: 0.82, rotation: -4, duration: 0.8, ease: SPRING }}, {A("hoy")});
    // ...then it all flickers out: that's the problem
    [4.75, 4.95, 5.1].forEach((t) => {{ tl.set("#h-net", {{ opacity: 0.25 }}, t); tl.set("#h-net", {{ opacity: 0.85 }}, t + 0.07); }});
    tl.to(".hl, .hm", {{ stroke: "#5c6670", duration: 0.3 }}, 4.7);
    tl.to("#h-warm", {{ scale: 0.3, opacity: 0.15, duration: 0.5, ease: "power3.in" }}, 4.9);
    tl.to("#h-cam", {{ y: 40, scale: 0.78, duration: 0.6, ease: "power2.in" }}, 5.0);'''
_ = (scene("hook", hook_css, hook_body, hook_js))

# ── problem: an obstacle race ─────────────────────────────────────
B = lambda w: at("problem", w)
RUN, H1, H2, H3, NOC = B("carrera"), B("servidores"), B("configurar"), B("cuentas"), B("noches")
RX = 640                                   # the runner holds this screen x; the world slides under it
walls = [("Servidores", 1300, "M3 4h18v6H3zM3 14h18v6H3z"), ("Configurar", 2000, "M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM19 12h2M3 12h2M12 3v2M12 19v2"), ("Cuentas por pagar", 2700, "M12 2v20M17 6H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6")]
WX = [w[1] for w in walls]
wall_html = ''.join(f'<div class="wall" id="pw{i}" style="left:{x}px"><div class="wi"><svg viewBox="0 0 24 24" class="icon"><path d="{d}"/></svg></div><b>{t}</b><span class="stripes"></span></div>' for i, (t, x, d) in enumerate(walls))
stamps = [("LENTO", H1), ("COMPLICADO", H2), ("CARO", H3)]
prob_css = '''
    #pb-sky { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 30%, #13202d, #05080d 70%); }
    #pb-red { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 40%, rgba(160,30,30,.55), rgba(40,6,6,.9) 75%); opacity: 0; }
    #pb-floor { position: absolute; left: -1200px; top: 600px; width: 4320px; height: 1400px; transform: rotateX(72deg); transform-origin: 50% 0; background-image: linear-gradient(rgba(102,184,255,.35) 2px, transparent 2px), linear-gradient(90deg, rgba(102,184,255,.25) 2px, transparent 2px); background-size: 140px 140px; }
    #pb-floorwrap { position: absolute; inset: 0; perspective: 900px; perspective-origin: 50% 40%; overflow: hidden; }
    #pb-shade { position: absolute; left: 0; right: 0; top: 560px; height: 140px; background: linear-gradient(180deg, #05080d, rgba(5,8,13,0)); }
    #pb-world { position: absolute; left: 0; top: 0; width: 6000px; height: 1080px; }
    #pb-track { position: absolute; left: 0; top: 742px; width: 6000px; height: 10px; border-radius: 99px; background: linear-gradient(90deg, rgba(102,184,255,.15), rgba(102,184,255,.7), rgba(102,184,255,.15)); box-shadow: 0 0 30px rgba(57,159,239,.5); }
    .wall { position: absolute; top: 470px; width: 230px; height: 272px; border-radius: 20px; background: linear-gradient(180deg, rgba(60,22,22,.95), rgba(26,10,10,.95)); box-shadow: inset 0 0 0 3px rgba(228,124,118,.75), 0 0 50px rgba(228,124,118,.35), 0 40px 80px rgba(0,0,0,.6); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 16px; text-align: center; overflow: hidden; }
    .wall b { font-size: 30px; color: #ffd9d6; padding: 0 12px; }
    .wi { width: 80px; height: 80px; border-radius: 22px; background: rgba(228,124,118,.2); display: flex; align-items: center; justify-content: center; color: #e47c76; }
    .wi svg { width: 46px; height: 46px; }
    .stripes { position: absolute; left: 0; right: 0; bottom: 0; height: 26px; background: repeating-linear-gradient(-45deg, #f0b965 0 16px, #1a0a0a 16px 32px); opacity: .85; }
    #pb-runner { position: absolute; left: 580px; top: 622px; width: 120px; height: 120px; border-radius: 32px; background: linear-gradient(160deg, #5cb3f7, #1e76b8); box-shadow: 0 0 0 3px rgba(214,236,255,.85), 0 0 50px rgba(57,159,239,.8), 0 30px 50px rgba(0,0,0,.6); display: flex; align-items: center; justify-content: center; color: #001428; }
    #pb-runner svg { width: 62px; height: 62px; stroke-width: 2.2; }
    #pb-trail { position: absolute; left: 380px; top: 662px; width: 220px; height: 40px; border-radius: 99px; background: linear-gradient(90deg, rgba(102,184,255,0), rgba(166,208,246,.6)); filter: blur(6px); }
    .stamp { position: absolute; left: 0; right: 0; top: 230px; text-align: center; font-family: "Michroma", sans-serif; font-size: 170px; color: transparent; -webkit-text-stroke: 4px #e47c76; text-shadow: 0 0 40px rgba(228,124,118,.55); opacity: 0; letter-spacing: 6px; }
    #pb-zz { position: absolute; left: 730px; top: 600px; font: 700 54px "Michroma", sans-serif; color: #a6d0f6; opacity: 0; }
    #pb-clock { position: absolute; left: 0; right: 0; top: 250px; text-align: center; opacity: 0; }
    #pb-clock .t { font: 700 200px "JetBrains Mono Variable", monospace; color: #fff1ef; text-shadow: 0 0 70px rgba(228,124,118,.75); }
    #pb-clock .s { font-size: 42px; color: #ffb3ad; margin-top: -14px; }
    #p-beam { position: absolute; top: 0; bottom: 0; left: 1920px; width: 420px; background: linear-gradient(90deg, rgba(57,159,239,0), rgba(166,208,246,.95) 50%, rgba(57,159,239,0)); filter: blur(12px); }
    #p-flood { position: absolute; inset: 0; background: #399fef; }
    #pb-shake { position: absolute; inset: 0; }
'''
prob_body = f'''    <div id="pb-shake">
      <div id="pb-sky"></div>
      <div id="pb-floorwrap"><div id="pb-floor"></div></div><div id="pb-shade"></div>
      <div id="pb-red"></div>
      {''.join(f'<div class="stamp" id="ps{i}">{t}</div>' for i, (t, _) in enumerate(stamps))}
      <div id="pb-world"><div id="pb-track"></div>{wall_html}</div>
      <div id="pb-trail"></div>
      <div id="pb-runner">{ICON["rocket"]}</div>
      <div id="pb-zz">z z</div>
      <div id="pb-clock"><div class="t"><span>03</span><span id="p-colon">:</span><span>12</span></div><div class="s">otra noche sin dormir</div></div>
    </div>
    <div id="p-beam"></div><div id="p-flood"></div>'''
# world x that puts a wall's front face right at the runner's nose
hitx = lambda wx: -(wx - (RX + 60) - 4)
seg = []
prev_x, prev_t = 0, RUN
for i, (wx, th) in enumerate(zip(WX, (H1, H2, H3))):
    seg.append(f'tl.to("#pb-world", {{ x: {hitx(wx)}, duration: {th - prev_t:.3f}, ease: "power2.in" }}, {prev_t:.3f});')
    seg.append(f'tl.to("#pb-world", {{ x: {hitx(wx) + 70}, duration: 0.18, ease: "power2.out" }}, {th:.3f});')
    prev_x, prev_t = hitx(wx) + 70, th + 0.2
prob_js = f'''
    ["#p-flood", "#pb-red", ".stamp", "#pb-zz", "#pb-clock"].forEach((s) => tl.fromTo(s, {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0));
    // the runner (an app) arrives and sets off; the floor streams under it
    tl.fromTo("#pb-runner", {{ x: -700, rotation: -20 }}, {{ x: 0, rotation: 0, duration: 0.9, ease: SPRING }}, 0.15);
    tl.fromTo("#pb-floor", {{ backgroundPositionY: "0px" }}, {{ backgroundPositionY: "-2100px", duration: 6.4, ease: "power1.in" }}, {RUN});
    tl.fromTo("#pb-floor", {{ backgroundPositionX: "0px" }}, {{ backgroundPositionX: "-1400px", duration: 6.4, ease: "power1.in" }}, {RUN});
    tl.fromTo("#pb-trail", {{ opacity: 0, scaleX: 0.3, transformOrigin: "100% 50%" }}, {{ opacity: 1, scaleX: 1, duration: 0.4 }}, {RUN});
    tl.fromTo("#pb-runner", {{ y: 0 }}, {{ y: -14, duration: 0.16, ease: "sine.inOut", yoyo: true, repeat: 23 }}, {RUN});
    {chr(10).join("    " + x for x in seg)}
    // each wall is hit on its word: squash, red flash, a giant stamp, a shake, then a leap over
    {chr(10).join(f"""    tl.to("#pb-runner", {{ scaleX: 0.78, scaleY: 1.15, duration: 0.07, yoyo: true, repeat: 1, ease: "power2.out" }}, {th:.3f});
    tl.fromTo("#pw{i}", {{ boxShadow: "inset 0 0 0 3px rgba(228,124,118,.75), 0 0 50px rgba(228,124,118,.35), 0 40px 80px rgba(0,0,0,.6)" }}, {{ boxShadow: "inset 0 0 0 5px #ff6b62, 0 0 120px rgba(255,90,80,.9), 0 40px 80px rgba(0,0,0,.6)", duration: 0.12, yoyo: true, repeat: 1 }}, {th:.3f});
    tl.fromTo("#pw{i}", {{ x: 0 }}, {{ x: 10, duration: 0.04, yoyo: true, repeat: 5, ease: "none" }}, {th:.3f});
    tl.fromTo("#pb-shake", {{ x: 0, y: 0 }}, {{ x: 12, y: -8, duration: 0.05, yoyo: true, repeat: 5, ease: "none" }}, {th:.3f});
    tl.fromTo("#ps{i}", {{ opacity: 0, scale: 1.5 }}, {{ keyframes: [{{ opacity: 1, scale: 1, duration: 0.18, ease: "power3.out" }}, {{ opacity: 1, duration: 0.25 }}, {{ opacity: 0, scale: 0.94, duration: 0.2 }}] }}, {th:.3f});
    tl.to("#pb-runner", {{ keyframes: [{{ y: -230, rotation: 25, duration: 0.2, ease: "power2.out" }}, {{ y: 0, rotation: 0, duration: 0.22, ease: "power2.in" }}] }}, {th + 0.18:.3f});""" for i, th in enumerate((H1, H2, H3)))}
    tl.to("#pb-world", {{ x: {hitx(WX[-1]) - 520}, duration: {NOC - H3 - 0.2:.3f}, ease: "power2.out" }}, {H3 + 0.2:.3f});
    // "noches sin dormir": the race stalls, the world goes red, the clock slams down
    tl.to("#pb-red", {{ opacity: 1, duration: 0.4 }}, {NOC - 0.1});
    tl.to("#pb-trail", {{ opacity: 0, duration: 0.3 }}, {NOC - 0.1});
    tl.to("#pb-runner", {{ rotation: 18, y: 18, duration: 0.6, ease: SPRING }}, {NOC});
    tl.fromTo("#pb-zz", {{ opacity: 0, y: 0 }}, {{ opacity: 1, y: -40, duration: 1.2, ease: "power1.out" }}, {NOC + 0.2});
    tl.fromTo("#pb-clock", {{ opacity: 0, y: -260, scale: 1.3 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.6, ease: SPRING }}, {NOC});
    tl.fromTo("#pb-shake", {{ y: 0 }}, {{ y: 16, duration: 0.05, yoyo: true, repeat: 5, ease: "none" }}, {NOC + 0.12});
    [{NOC + 0.5}, {NOC + 1.1}, {NOC + 1.7}].forEach((t) => {{ tl.set("#p-colon", {{ opacity: 0 }}, t); tl.set("#p-colon", {{ opacity: 1 }}, t + 0.3); }});
    // a beam of light sweeps it all away
    tl.to("#p-beam", {{ x: -2500, duration: 0.7, ease: "power2.in" }}, 8.1);
    tl.to(["#pb-clock", "#pb-runner", "#pb-zz"], {{ opacity: 0, filter: "blur(10px)", duration: 0.3 }}, 8.3);
    tl.to("#p-flood", {{ opacity: 1, duration: 0.3, ease: "power2.in" }}, 8.5);'''
_ = (scene("problem", prob_css, prob_body, prob_js))
print("hook/problem v3")
