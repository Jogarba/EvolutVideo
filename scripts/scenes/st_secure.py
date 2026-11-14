import sys, math, random; sys.path.insert(0, sys.path[0])
from st_common import *
rnd = random.Random(9)
# Station 02: every change rides a line from you to your customers and passes through the shield.
TY = 330                      # the line's height in hero coordinates
SH = "M180 0 L330 50 C330 200 280 320 180 384 C80 320 30 200 30 50 Z"   # 360 wide shield, placed at x 250
shards = ''.join(f'<i class="shard" id="s-sh{i}"></i>' for i in range(12))
sh_js = '\n    '.join(f'tl.fromTo("#s-sh{i}", {{ x: 300, y: {TY}, opacity: 0, rotation: 0 }}, {{ keyframes: [{{ opacity: 1, duration: 0.02 }}, {{ x: {300 - abs(math.cos(a))*r:.0f}, y: {TY + math.sin(a)*r:.0f}, rotation: {rnd.randint(-200,200)}, opacity: 0, duration: 0.7, ease: "power3.out" }}] }}, 4.3);'
                     for i, (a, r) in enumerate((rnd.uniform(-1.3, 1.3), rnd.uniform(70, 200)) for _ in range(12)))
rivets = ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#d6ecff" fill-opacity=".8"/>' for x, y in [(60, 62), (300, 62), (180, 22), (88, 250), (272, 250), (180, 360)])
circuit = ''.join(f'<path d="M{x} 70 V{y} H{x + d}" fill="none" stroke="#399fef" stroke-opacity=".18" stroke-width="2"/><circle cx="{x + d}" cy="{y}" r="4" fill="#399fef" fill-opacity=".3"/>' for x, y, d in [(80, 160, 30), (110, 230, 40), (250, 150, -30), (280, 220, -40), (150, 300, 20), (210, 290, -20)])
css = f'''
    #s-glow {{ left: 130px; top: 60px; width: 600px; height: 560px; background: radial-gradient(closest-side, rgba(94,209,157,.25), rgba(94,209,157,0)); }}
    #s-line {{ position: absolute; left: 0; top: 0; overflow: visible; }}
    #s-svg {{ position: absolute; left: 250px; top: 130px; overflow: visible; }}
    .end {{ position: absolute; top: {TY - 52}px; width: 150px; display: flex; flex-direction: column; align-items: center; gap: 10px; font-size: 26px; color: #d6dde3; text-align: center; }}
    .end i {{ width: 74px; height: 74px; border-radius: 22px; display: flex; align-items: center; justify-content: center; background: rgba(14,19,24,.88); box-shadow: inset 0 0 0 1.5px rgba(242,245,247,.18); }}
    .end svg {{ width: 38px; height: 38px; }}
    .pkt {{ position: absolute; left: 0; top: 0; padding: 10px 18px; border-radius: 14px; display: flex; align-items: center; gap: 8px; font-size: 24px; font-weight: 600; white-space: nowrap; }}
    .pkt svg {{ width: 24px; height: 24px; }}
    .wait {{ background: rgba(22,30,38,.95); color: #d6dde3; box-shadow: inset 0 0 0 2px rgba(166,208,246,.5); }}
    .risk {{ background: rgba(53,28,26,.95); color: #e47c76; box-shadow: inset 0 0 0 2px rgba(228,124,118,.6); }}
    .shard {{ position: absolute; left: 0; top: 0; width: 12px; height: 12px; background: #e47c76; opacity: 0; }}
    #sp-in {{ position: absolute; left: 0; top: {TY - 28}px; width: 200px; height: 56px; border-radius: 99px; background: linear-gradient(90deg, rgba(94,209,157,0), #9be8c4 40%, #ffffff); box-shadow: 0 0 40px #5ed19d; }}
    #s-blocked {{ position: absolute; left: 330px; top: 70px; }}
    #s-badge {{ position: absolute; left: 330px; top: 560px; }}
'''
hero = f'''<div class="glow" id="s-glow"></div>
        <svg id="s-line" width="860" height="720"><path d="M110 {TY} H750" stroke="#203a52" stroke-width="8" stroke-linecap="round"/><path id="s-flow" d="M110 {TY} H750" stroke="#66b8ff" stroke-width="3" stroke-dasharray="10 16" stroke-linecap="round"/></svg>
        <div class="end" style="left:0"><i><svg viewBox="0 0 24 24" class="icon" style="color:#a6d0f6"><path d="M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg></i>Tus cambios</div>
        <div class="end" style="left:710px"><i><svg viewBox="0 0 24 24" class="icon" style="color:#5ed19d"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg></i>Tus clientes</div>
        <svg id="s-svg" width="360" height="400" viewBox="0 0 360 400">
          <defs>
            <linearGradient id="s-rim" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d6ecff"/><stop offset=".3" stop-color="#399fef"/><stop offset=".7" stop-color="#1e76b8"/><stop offset="1" stop-color="#9fd2ff"/></linearGradient>
            <linearGradient id="s-in" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#173852"/><stop offset="1" stop-color="#07111a"/></linearGradient>
            <clipPath id="s-clip"><path d="{SH}"/></clipPath>
            <linearGradient id="s-scan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5ed19d" stop-opacity="0"/><stop offset=".5" stop-color="#5ed19d" stop-opacity=".6"/><stop offset="1" stop-color="#5ed19d" stop-opacity="0"/></linearGradient>
          </defs>
          <g id="s-orbit" fill="none" stroke="#66b8ff" stroke-opacity=".5" stroke-width="2.5"><ellipse cx="180" cy="192" rx="178" ry="96" stroke-dasharray="8 14"/><ellipse cx="180" cy="192" rx="162" ry="82" stroke-opacity=".2"/><circle cx="180" cy="96" r="11" fill="#66b8ff" fill-opacity=".12" stroke="none"/><circle cx="180" cy="96" r="4" fill="#d6ecff" fill-opacity=".9" stroke="none"/></g>
          <path d="{SH}" fill="#06121d" stroke="#2a6d98" stroke-opacity=".72" stroke-width="10" transform="translate(4 18) scale(1.02)"/>
          <path d="{SH}" fill="url(#s-rim)" transform="translate(-12 -12) scale(1.066)"/>
          <path d="{SH}" fill="url(#s-in)"/>
          <g clip-path="url(#s-clip)">{circuit}<rect id="s-scanbar" x="0" y="-100" width="360" height="100" fill="url(#s-scan)"/>
            <path d="M0 40 L360 40" stroke="rgba(255,255,255,.07)" stroke-width="70" transform="rotate(-20 180 200)"/></g>
          <path d="M180 32 L304 72 C304 196 262 294 180 350 C98 294 56 196 56 72 Z" fill="none" stroke="#66b8ff" stroke-opacity=".4" stroke-width="2.5"/>
          {rivets}
          <path id="s-check" d="M112 196 L160 244 L250 154" fill="none" stroke="#5ed19d" stroke-width="26" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>
          <path id="s-ripple" d="{SH}" fill="none" stroke="#e47c76" stroke-width="6" opacity="0"/>
        </svg>
        <div class="pkt wait" id="s-k0">{ICON["info"]}<span id="s-k0t">Nueva función</span></div>
        <div class="pkt wait" id="s-k1">{ICON["info"]}<span>Mejora del menú</span></div>
        <div class="pkt risk" id="s-k2">{ICON["bad"]}Riesgo</div>
        {shards}
        <div id="sp-in"></div><div class="orb" id="sp-gorb" style="left:430px;top:330px;background:radial-gradient(circle,#fff,#9be8c4 35%,rgba(94,209,157,.5) 60%,rgba(94,209,157,0) 72%);box-shadow:0 0 60px #5ed19d"></div>
        <div id="s-blocked">{pill("bad", "Bloqueado", "lock")}</div>
        <div id="s-badge">{pill("ok", "Revisado por Evolut")}</div>'''
pk = lambda sel, t: f'''tl.fromTo("{sel}", {{ x: 150, y: {TY - 24}, opacity: 0 }}, {{ keyframes: [{{ opacity: 1, duration: 0.15 }}, {{ x: 330, duration: 0.7, ease: "back.out(1.3)" }}, {{ x: 330, duration: 0.35 }}, {{ x: 640, opacity: 0, duration: 0.7, ease: "power2.in" }}] }}, {t});
    tl.to("{sel}", {{ backgroundColor: "rgba(16,42,30,.95)", color: "#5ed19d", boxShadow: "inset 0 0 0 2px rgba(94,209,157,.6)", duration: 0.2 }}, {t + 0.95});'''
E, RV, SG, AF = at("secure", "escudo"), at("secure", "revisamos"), at("secure", "seguro"), at("secure", "afuera")
sh_js = sh_js.replace("}, 4.3);", f"}}, {SG});")
js = f'''
    tl.fromTo("#s-svg", {{ y: 100, opacity: 0, scale: 0.85, filter: "blur(10px)" }}, {{ y: 0, opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.9, ease: "expo.out" }}, 0.35);
    tl.fromTo("#s-orbit", {{ opacity: 0, rotation: -12, transformOrigin: "50% 50%", transformBox: "fill-box" }}, {{ opacity: 1, rotation: 12, duration: 4.8, ease: "sine.inOut" }}, 0.7);
    tl.fromTo("#s-svg", {{ y: 0 }}, {{ y: -7, duration: 1.25, ease: "sine.inOut", yoyo: true, repeat: 2 }}, 1.4);
    tl.fromTo(["#s-line", ".end"], {{ opacity: 0 }}, {{ opacity: 1, duration: 0.6, stagger: 0.1 }}, 0.5);
    tl.fromTo("#s-glow", {{ opacity: 0 }}, {{ opacity: 1, duration: 1.0 }}, 0.5);
    tl.fromTo("#s-flow", {{ strokeDashoffset: 0 }}, {{ strokeDashoffset: -260, duration: 6.4, ease: "none" }}, 0);
    tl.to("#s-check", {{ strokeDashoffset: 0, duration: 0.6, ease: "back.out(1.6)" }}, {RV});
    tl.to("#s-svg", {{ filter: "drop-shadow(0 0 26px rgba(94,209,157,.4))", duration: 0.45, ease: "power2.out" }}, {RV + 0.6});
    tl.fromTo("#s-scanbar", {{ y: 0 }}, {{ y: 500, duration: 1.0, ease: "power1.inOut", repeat: 3 }}, {RV - 0.2});
    ["#s-blocked", "#s-badge", "#s-ripple"].forEach((s) => tl.fromTo(s, {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0));
    // good changes stop inside the shield, get checked, turn green and reach your customers
    {pk("#s-k0", E - 0.85)}
    {pk("#s-k1", E + 0.2)}
    // a risk is stopped at the shield and breaks apart
    tl.fromTo("#s-k2", {{ x: 150, y: {TY - 24}, opacity: 0 }}, {{ keyframes: [{{ opacity: 1, duration: 0.15 }}, {{ x: 230, duration: 0.85, ease: "power2.in" }}, {{ x: 200, scale: 0.7, opacity: 0, duration: 0.15 }}] }}, {SG - 1.0});
    tl.fromTo("#s-ripple", {{ opacity: 0.9, scale: 1, transformOrigin: "50% 50%" }}, {{ opacity: 0, scale: 1.12, duration: 0.6, ease: "power2.out", immediateRender: false }}, {SG});
    {sh_js}
    tl.to("#s-blocked", {{ opacity: 1, duration: 0.01 }}, {AF});
    tl.fromTo("#s-blocked", {{ y: 16, scale: 0.7 }}, {{ y: 0, scale: 1, duration: 0.45, ease: "back.out(2)" }}, {AF});
    tl.to("#s-badge", {{ opacity: 1, duration: 0.01 }}, {AF + 0.45});
    tl.fromTo("#s-badge", {{ y: 16 }}, {{ y: 0, duration: 0.5, ease: "back.out(1.6)" }}, {AF + 0.45});'''
js = f'''
    tl.fromTo("#sp-in", {{ x: -1500, opacity: 1 }}, {{ keyframes: [{{ x: 120, duration: 0.5, ease: "power3.out" }}, {{ opacity: 0, scaleX: 0.3, duration: 0.25 }}] }}, 0);
    tl.fromTo("#sp-gorb", {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0);''' + js
exit_js = f'''
    tl.to(["#s-k0", "#s-k1", ".end", "#s-line", "#s-badge", "#s-blocked", "#st-chip", "#st-h", "#st-pool"], {{ opacity: 0, filter: "blur(8px)", duration: 0.3, ease: "power2.in" }}, {OUTT});
    tl.to("#s-svg", {{ scale: 0.06, opacity: 0, duration: 0.4, ease: "power3.in" }}, {OUTT + 0.05});
    tl.fromTo("#sp-gorb", {{ opacity: 0, scale: 0.3 }}, {{ opacity: 1, scale: 1.6, duration: 0.35, ease: "power2.out", immediateRender: false }}, {OUTT + 0.3});'''
js = js + f'''
    // still chasing the packet: the camera arrives from the left and brakes on the line
    tl.fromTo("#cam", {{ x: 760 }}, {{ x: 0, duration: 0.9, ease: SPRING }}, 0);
    // push in on the shield while it checks
    aim(960, 571, {RV - 0.6});
    rig({{ scale: 1.13 }}, {RV - 0.5}, 0.75);
    // the risk's impact shakes the lens
    tl.fromTo("#cam", {{ y: 0 }}, {{ y: 12, duration: 0.05, yoyo: true, repeat: 5, ease: "none" }}, {SG});
    rig({{ scale: 1.0 }}, {AF + 0.1}, 0.8);'''
exit_js = exit_js + f'''
    tl.to("#cam", {{ scale: 2.1, duration: 0.5, ease: "power3.in" }}, {OUTT});'''
write("secure", css, hero, js, 2, "SEGURIDAD", "Segura desde", "el primer día.", exit_js=exit_js)
print("secure")
