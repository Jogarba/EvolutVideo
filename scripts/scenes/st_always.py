import sys, math; sys.path.insert(0, sys.path[0])
from st_common import *
# Station 03: a globe with real continents turns from the Americas to Europe while day turns to night.
# Coarse land mask: latitude band -> longitude ranges (degrees).
LAND = {  # 5° bands, longitude ranges; Antarctica left out on purpose
 70: [(-165, -70), (-55, -20), (15, 32), (40, 180)],
 65: [(-165, -65), (-52, -22), (12, 32), (35, 180)],
 60: [(-165, -65), (-48, -42), (5, 30), (30, 170)],
 55: [(-133, -60), (-6, 1), (8, 165)],
 50: [(-127, -56), (-5, 2), (0, 140)],
 45: [(-124, -64), (-2, 40), (40, 135)],
 40: [(-124, -74), (-9, 3), (12, 28), (26, 45), (50, 122), (135, 141)],
 35: [(-121, -76), (-7, 11), (23, 36), (35, 60), (67, 120), (130, 140)],
 30: [(-116, -81), (-10, 32), (35, 60), (68, 122)],
 25: [(-112, -97), (-84, -75), (-16, 35), (37, 57), (68, 92), (98, 120)],
 20: [(-105, -87), (-17, 38), (40, 58), (72, 88), (95, 110)],
 15: [(-97, -84), (-17, 40), (42, 52), (74, 80), (97, 108)],
 10: [(-86, -62), (-15, 45), (76, 80), (98, 106), (122, 126)],
 5: [(-79, -52), (-10, 48), (100, 104), (115, 119)],
 0: [(-80, -50), (9, 42), (98, 106), (110, 118), (120, 125)],
 -5: [(-81, -35), (11, 40), (105, 115), (120, 140)],
 -10: [(-78, -36), (13, 40), (120, 150)],
 -15: [(-76, -39), (12, 41), (44, 50), (125, 145)],
 -20: [(-70, -40), (13, 36), (44, 48), (115, 150)],
 -25: [(-70, -47), (14, 33), (44, 47), (114, 153)],
 -30: [(-71, -51), (16, 31), (115, 153)],
 -35: [(-72, -56), (18, 25), (116, 150)],
 -40: [(-73, -62), (145, 148), (172, 176)],
 -45: [(-74, -65), (167, 172)],
 -50: [(-75, -68)],
 -55: [(-72, -66)],
}
def land(lat, lon):
    band = min(LAND, key=lambda b: abs(b - lat))
    return abs(band - lat) <= 3 and any(a <= lon <= b for a, b in LAND[band])
pts = [(lat, lon) for lat in range(-57, 76, 3) for lon in range(-180, 180, 3) if land(lat, lon)]
cities = [("Ciudad de México", 19.4, -99.1), ("Bogotá", 4.7, -74.1), ("Madrid", 40.4, -3.7), ("São Paulo", -23.5, -46.6)]
CX, CY, R = 430, 320, 228
css = '''
    #a-glow { left: 110px; top: 0; width: 640px; height: 640px; background: radial-gradient(closest-side, rgba(57,159,239,.34), rgba(57,159,239,0)); }
    #a-svg { position: absolute; left: 0; top: 0; overflow: visible; }
    .ld { fill: #66b8ff; }
    .vis { position: absolute; left: 0; top: 0; padding: 10px 16px; border-radius: 14px; background: rgba(14,19,24,.92); box-shadow: inset 0 0 0 1.5px rgba(94,209,157,.45); font-size: 23px; white-space: nowrap; display: flex; align-items: center; gap: 8px; opacity: 0; }
    .vis i { width: 10px; height: 10px; border-radius: 50%; background: #5ed19d; box-shadow: 0 0 10px #5ed19d; }
    .vis b { color: #5ed19d; font-weight: 600; }
    #sp-buy { left: 175px; top: 250px; width: 510px; height: 140px; padding: 0 30px; display: flex; align-items: center; gap: 22px; }
    #sp-buy i { width: 80px; height: 80px; border-radius: 22px; background: #f0b965; display: flex; align-items: center; justify-content: center; color: #2b1d14; flex: none; }
    #sp-buy svg { width: 46px; height: 46px; } #sp-buy b { display: block; font-size: 38px; } #sp-buy span { font-size: 28px; color: #bfc3c7; }
    #a-pill { position: absolute; left: 300px; top: 640px; }
    .lab { font: 600 18px "JetBrains Mono Variable", monospace; letter-spacing: 2px; }
'''
dots = ''.join('<circle class="ld" r="3"/>' for _ in pts)
mer = ''.join(f'<path class="mer" fill="none" stroke="#a6d0f6" stroke-opacity=".12" stroke-width="1.5"/>' for _ in range(12))
cmark = ''.join(f'<g class="cm" id="a-c{i}"><circle r="22" fill="none" stroke="#5ed19d" stroke-width="3" class="cring" id="a-cr{i}" opacity="0"/><circle r="7" fill="#5ed19d"/><circle r="12" fill="#5ed19d" fill-opacity=".25"/></g>' for i in range(len(cities)))
arcs = ''.join(f'<path id="a-arc{i}" fill="none" stroke="#5ed19d" stroke-width="3" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>' for i in range(2))
labels = [("Nueva visita", 0), ("Compra", 1), ("Compra", 2)]
vis = ''.join(f'<div class="vis" id="a-v{i}"><i></i><b>{w}</b>· {cities[c][0]}</div>' for i, (w, c) in enumerate(labels))
ticks = ''.join(f'<line x1="{CX + math.cos(a)*(R+44):.1f}" y1="{CY + math.sin(a)*(R+44):.1f}" x2="{CX + math.cos(a)*(R+(52 if k % 6 == 0 else 48)):.1f}" y2="{CY + math.sin(a)*(R+(52 if k % 6 == 0 else 48)):.1f}" stroke="#a6d0f6" stroke-opacity="{.6 if k % 6 == 0 else .25}" stroke-width="2"/>' for k, a in enumerate(i * 2 * math.pi / 24 for i in range(24)))
hero = f'''<div class="glow" id="a-glow"></div>
        <svg id="a-svg" width="860" height="720" viewBox="0 0 860 720">
          <defs><radialGradient id="a-ocean" cx="38%" cy="32%"><stop offset="0" stop-color="#1f4a70"/><stop offset=".65" stop-color="#0b1b2a"/><stop offset="1" stop-color="#050c13"/></radialGradient>
            <radialGradient id="a-atmo"><stop offset=".86" stop-color="#66b8ff" stop-opacity="0"/><stop offset=".93" stop-color="#66b8ff" stop-opacity=".45"/><stop offset="1" stop-color="#66b8ff" stop-opacity="0"/></radialGradient>
            <radialGradient id="a-spec" cx="32%" cy="26%" r="40%"><stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
            <clipPath id="a-clip"><circle cx="{CX}" cy="{CY}" r="{R}"/></clipPath></defs>
          <circle cx="{CX}" cy="{CY}" r="{R+44}" fill="none" stroke="#a6d0f6" stroke-opacity=".18" stroke-width="2"/>{ticks}
          <text class="lab" x="{CX}" y="{CY - R - 62}" text-anchor="middle" fill="#f0b965">DÍA</text><text class="lab" x="{CX}" y="{CY + R + 80}" text-anchor="middle" fill="#a6d0f6">NOCHE</text>
          <circle cx="{CX}" cy="{CY}" r="{R+26}" fill="url(#a-atmo)"/>
          <circle cx="{CX}" cy="{CY}" r="{R}" fill="url(#a-ocean)"/>
          <g clip-path="url(#a-clip)">{mer}<g id="a-dots">{dots}</g><path id="a-night" fill="#02060b" fill-opacity=".55"/></g>
          <circle cx="{CX}" cy="{CY}" r="{R}" fill="url(#a-spec)"/>
          <circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="#a6d0f6" stroke-opacity=".55" stroke-width="2"/>
          {arcs}{cmark}
          <g id="a-sun"><circle r="24" fill="#f0b965"/><circle r="38" fill="#f0b965" fill-opacity=".25"/></g>
          <g id="a-moon"><circle r="17" fill="#dfe6ee"/><circle r="17" cx="8" cy="-5" fill="#0b1b2a"/></g>
        </svg>
        {vis}
        <div class="dim" id="sp-dim"></div>
        <div class="spot" id="sp-buy"><i><svg viewBox="0 0 24 24" class="icon"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4zM3 6h18M16 10a4 4 0 0 1-8 0"/></svg></i><div><b>Nueva compra</b><span>Bogotá · 3:12 a.m.</span></div></div>
        <div class="orb" id="sp-gorb" style="left:{CX}px;top:{CY}px;background:radial-gradient(circle,#fff,#9be8c4 35%,rgba(94,209,157,.5) 60%,rgba(94,209,157,0) 72%);box-shadow:0 0 60px #5ed19d"></div>
        <div class="orb" id="sp-orb" style="left:{CX}px;top:{CY}px"></div>
        <div id="a-pill">{pill("ok", "Abierta día y noche")}</div>'''
C1, C2, C3, NV = at("always", "ciudad"), at("always", "hora"), at("always", "cierra"), at("always", "nunca")
js = f'''
    const PTS = {[[la, lo] for la, lo in pts]};
    const CITIES = {[[la, lo] for _, la, lo in cities]};
    const CX = {CX}, CY = {CY}, R = {R}, TILT = 0.32, D = Math.PI / 180;
    const dots = document.querySelectorAll("#a-dots circle"), mers = document.querySelectorAll(".mer");
    const st = {{ lon0: -96, sun: 0.0 }};
    const vis = [["#a-v0", 0, {C1}], ["#a-v1", 1, {C2}], ["#a-v2", 2, {C3}]];
    // project a point on the turning, tilted globe
    const proj = (la, lo) => {{
      const c = Math.cos(la * D), x = c * Math.sin((lo - st.lon0) * D), y = -Math.sin(la * D), z = c * Math.cos((lo - st.lon0) * D);
      return [x, y * Math.cos(TILT) - z * Math.sin(TILT), y * Math.sin(TILT) + z * Math.cos(TILT)];
    }};
    const draw = () => {{
      const sx = Math.cos(st.sun), sy = -0.35, sz = Math.sin(st.sun) * 0.9 + 0.2;
      PTS.forEach(([la, lo], i) => {{
        const [x, y, z] = proj(la, lo), d = dots[i];
        if (z <= 0) {{ d.setAttribute("opacity", "0"); return; }}
        const lit = x * sx + y * sy + z * sz;
        d.setAttribute("cx", (CX + x * R).toFixed(1)); d.setAttribute("cy", (CY + y * R).toFixed(1));
        d.setAttribute("r", (1.6 + z * 2.2).toFixed(1));
        d.setAttribute("fill", lit > 0 ? "#66b8ff" : "#f0b965");
        d.setAttribute("opacity", (lit > 0 ? 0.35 + z * 0.65 : 0.55 + z * 0.4).toFixed(2));
      }});
      mers.forEach((m, k) => {{
        const lo = -180 + k * 30; let p = "";
        for (let la = -90; la <= 90; la += 10) {{ const [x, y, z] = proj(la, lo); if (z > 0) p += (p ? " L" : "M") + (CX + x * R).toFixed(1) + " " + (CY + y * R).toFixed(1); else if (p && !p.endsWith("|")) p += "|"; }}
        m.setAttribute("d", p.split("|")[0]);
      }});
      // night side: a half-disc opposite the sun
      const ang = Math.atan2(sy, sx), k = Math.max(-1, Math.min(1, sz));
      const nx = -Math.cos(ang), ny = -Math.sin(ang), rx = R * Math.abs(k);
      const p1 = [CX + ny * R, CY - nx * R], p2 = [CX - ny * R, CY + nx * R];
      document.querySelector("#a-night").setAttribute("d", `M${{p1[0]}} ${{p1[1]}} A${{R}} ${{R}} 0 0 ${{1}} ${{p2[0]}} ${{p2[1]}} A${{rx}} ${{R}} ${{(ang / D).toFixed(1)}} 0 ${{k > 0 ? 1 : 0}} ${{p1[0]}} ${{p1[1]}}Z`);
      const ring = R + 44, sa = Math.atan2(sy, sx);
      gsap.set("#a-sun", {{ x: CX + Math.cos(sa) * ring, y: CY + Math.sin(sa) * ring }});
      gsap.set("#a-moon", {{ x: CX - Math.cos(sa) * ring, y: CY - Math.sin(sa) * ring }});
      const C = CITIES.map(([la, lo]) => proj(la, lo));
      C.forEach(([x, y, z], i) => gsap.set(`#a-c${{i}}`, {{ x: CX + x * R, y: CY + y * R, opacity: z > 0.05 ? 1 : 0 }}));
      [[0, 1], [1, 2]].forEach(([a, b], i) => {{
        const [ax, ay] = [CX + C[a][0] * R, CY + C[a][1] * R], [bx, by] = [CX + C[b][0] * R, CY + C[b][1] * R];
        const mx = (ax + bx) / 2, my = (ay + by) / 2, dx = mx - CX, dy = my - CY, l = Math.hypot(dx, dy) || 1;
        document.querySelector("#a-arc" + i).setAttribute("d", `M${{ax.toFixed(1)}} ${{ay.toFixed(1)}} Q${{(mx + dx / l * 120).toFixed(1)}} ${{(my + dy / l * 120).toFixed(1)}} ${{bx.toFixed(1)}} ${{by.toFixed(1)}}`);
      }});
      // each visit label sits beside its city, kept inside the frame
      vis.forEach(([sel, c]) => {{
        const [x, y] = [CX + C[c][0] * R, CY + C[c][1] * R];
        const left = x > CX ? Math.min(x + 28, 860 - 330) : Math.max(x - 330, 0);
        gsap.set(sel, {{ x: left, y: Math.max(0, Math.min(y - 24, 560)) }});
      }});
    }};
    draw();
    tl.fromTo(st, {{ lon0: -96, sun: -0.6 }}, {{ lon0: -20, sun: 2.2, duration: 6.4, ease: "none", onUpdate: draw }}, 0);
    tl.fromTo("#a-svg", {{ y: 100, opacity: 0, scale: 0.88, filter: "blur(10px)" }}, {{ y: 0, opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.9, ease: "expo.out" }}, 0.35);
    tl.fromTo("#a-glow", {{ opacity: 0 }}, {{ opacity: 1, duration: 1.0 }}, 0.5);
    vis.forEach(([sel, c, t]) => {{
      tl.fromTo(sel, {{ opacity: 0 }}, {{ keyframes: [{{ opacity: 1, duration: 0.3 }}, {{ opacity: 1, duration: 0.55 }}, {{ opacity: 0, duration: 0.2 }}] }}, t);
      tl.fromTo(`#a-cr${{c}}`, {{ attr: {{ r: 10 }}, opacity: 0.9 }}, {{ attr: {{ r: 40 }}, opacity: 0, duration: 0.8, ease: "power2.out", immediateRender: false }}, t);
    }});
    tl.to("#a-arc0", {{ strokeDashoffset: 0, duration: 0.7, ease: "power2.inOut" }}, {C2 - 0.2});
    tl.to("#a-arc1", {{ strokeDashoffset: 0, duration: 0.8, ease: "power2.inOut" }}, {C3 - 0.25});
    tl.fromTo("#a-pill", {{ opacity: 0, y: 20, scale: 0.85 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.5, ease: "back.out(1.8)" }}, {NV});'''
js = js + f'''
    tl.fromTo("#sp-gorb", {{ scale: 1.6, opacity: 1 }}, {{ scale: 0.1, opacity: 0, duration: 0.45, ease: "power3.in" }}, 0);
    tl.fromTo("#a-svg", {{ scale: 0.12 }}, {{ scale: 1, duration: 0.9, ease: "back.out(1.4)", immediateRender: false }}, 0.2);
    ["#sp-buy", "#sp-dim", "#sp-orb"].forEach((s) => tl.fromTo(s, {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0));
    tl.to("#sp-dim", {{ opacity: 1, duration: 0.35 }}, {C2 + 0.1});
    tl.fromTo("#sp-buy", {{ opacity: 0, scale: 0.3, y: 60 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.7, ease: "back.out(1.5)", immediateRender: false }}, {C2 + 0.15});
    tl.to("#sp-buy", {{ opacity: 0, scale: 0.85, y: -30, duration: 0.3, ease: "power2.in" }}, {C2 + 1.3});
    tl.to("#sp-dim", {{ opacity: 0, duration: 0.35 }}, {C2 + 1.35});'''
exit_js = f'''
    tl.to(st, {{ lon0: "+=220", duration: 0.55, ease: "power3.in", onUpdate: draw }}, {OUTT});
    tl.to("#a-svg", {{ scale: 0.03, rotation: 90, opacity: 0, duration: 0.55, ease: "power3.in" }}, {OUTT});
    tl.to(["#a-pill", ".vis", "#st-chip", "#st-h", "#st-pool", "#a-glow"], {{ opacity: 0, filter: "blur(8px)", duration: 0.3, ease: "power2.in" }}, {OUTT});
    tl.fromTo("#sp-orb", {{ opacity: 0, scale: 0.2 }}, {{ opacity: 1, scale: 1.4, duration: 0.3, ease: "power2.out", immediateRender: false }}, {OUTT + 0.3});'''
js = js + f'''
    // orbital pitch and roll: the camera glides in on a banked curve and levels out
    tl.fromTo("#cam", {{ rotationX: 26, rotation: -7, scale: 1.25, y: 70, transformPerspective: 1800 }}, {{ rotationX: 0, rotation: 0, scale: 1, y: 0, duration: 1.15, ease: SPRING }}, 0.05);
    aim(960, 560, 1.3);
    rig({{ scale: 1.1, rotation: 1.5 }}, {C2 - 0.1}, 0.7);
    rig({{ scale: 1.0, rotation: 0 }}, {C2 + 1.4}, 0.8);'''
exit_js = exit_js + f'''
    kick({{ rotation: 4 }}, {OUTT});
    tl.to("#cam", {{ rotation: -28, scale: 0.85, duration: 0.55, ease: "power3.in" }}, {OUTT});'''
write("always", css, hero, js, 3, "SIEMPRE ACTIVA", "Siempre", "en línea.", exit_js=exit_js)
print("always", len(pts), "land dots")
