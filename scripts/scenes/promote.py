import sys; sys.path.insert(0, sys.path[0])
from common import *
X = {'dev': 420, 'qa': 960, 'prod': 1500}; Y = 520
def hexpts(cx, cy, r=170):
    import math
    return ' '.join(f'{cx + r*math.cos(math.radians(a)):.0f},{cy + r*math.sin(math.radians(a)):.0f}' for a in range(-90, 270, 60))
css = '''
    #p-world { position: absolute; inset: 0; }
    #p-cam { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; transform-origin: 0 0; }
    #p-svg { position: absolute; left: 0; top: 0; overflow: visible; }
    .env { font-family: "Michroma", sans-serif; font-size: 46px; fill: #f2f5f7; text-anchor: middle; }
    .under { position: absolute; top: 720px; width: 420px; display: flex; flex-direction: column; align-items: center; gap: 12px; }
    .chip { position: absolute; left: 0; top: 0; height: 76px; padding: 0 28px; display: flex; align-items: center; gap: 14px; font: 600 34px "JetBrains Mono Variable", monospace; border-radius: 99px; }
    .chip svg { width: 32px; height: 32px; }
    .chip .lk { display: none; }
    #p-sweep { position: absolute; left: 790px; top: 350px; width: 340px; height: 340px; border-radius: 50%; background: conic-gradient(from 0deg, rgba(94,209,157,0) 0deg, rgba(94,209,157,.0) 290deg, rgba(94,209,157,.55) 360deg); }
    #p-sweep2 { position: absolute; left: 790px; top: 350px; width: 340px; height: 340px; border-radius: 50%; background: conic-gradient(from 0deg, rgba(228,124,118,0) 0deg, rgba(228,124,118,0) 290deg, rgba(228,124,118,.6) 360deg); }
    #p-checks { position: absolute; left: 1150px; top: 330px; width: 600px; padding: 34px; }
    #p-checks h4 { font-size: 30px; font-weight: 600; margin-bottom: 18px; }
    .crow { display: flex; align-items: center; gap: 16px; height: 72px; padding: 0 22px; margin-top: 12px; font-size: 30px; }
    .crow .s { margin-left: auto; }
    #p-banner { position: absolute; left: 0; right: 0; top: 880px; display: flex; justify-content: center; }
    #p-btn { position: absolute; left: 760px; top: 950px; width: 400px; height: 84px; font-size: 34px; }
    #p-text { position: absolute; left: 0; right: 0; top: 930px; text-align: center; font-size: 62px; white-space: nowrap; }
    #p-text span { display: inline-block; margin-right: 22px; }
    #p-text .g { color: #5ed19d; }
    #p-stop { position: absolute; left: 0; right: 0; top: 80px; text-align: center; font-size: 72px; }
    #p-stop b { color: #e47c76; font-weight: 400; }
    #p-flash { position: absolute; inset: 0; background: #0f3424; }
'''
hexes = ''
for k, x in X.items():
    stroke = '#5ed19d' if k == 'prod' else '#399fef'
    hexes += f'<polygon id="p-h-{k}" points="{hexpts(x, Y)}" fill="rgba(14,19,24,.86)" stroke="{stroke}" stroke-width="5"/>'
    hexes += f'<polygon points="{hexpts(x, Y, 140)}" fill="none" stroke="{stroke}" stroke-opacity=".25" stroke-width="2"/>'
    hexes += f'<text class="env" x="{x}" y="{Y+16}">{k.upper()}</text>'
body = f'''    <div id="p-world">
      <div id="p-cam" data-layout-allow-overflow>
        <svg id="p-svg" width="1920" height="1080" viewBox="0 0 1920 1080">
          <line x1="590" y1="{Y}" x2="790" y2="{Y}" stroke="#303c48" stroke-width="6" stroke-dasharray="12 12"/>
          <line x1="1130" y1="{Y}" x2="1330" y2="{Y}" stroke="#303c48" stroke-width="6" stroke-dasharray="12 12"/>
          <line id="p-w1" x1="590" y1="{Y}" x2="790" y2="{Y}" stroke="#399fef" stroke-width="6" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>
          <line id="p-w2" x1="1130" y1="{Y}" x2="1330" y2="{Y}" stroke="#5ed19d" stroke-width="6" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>
          <circle id="p-e1" cx="590" cy="{Y}" r="11" fill="#a6d0f6"/>
          <circle id="p-e2" cx="1130" cy="{Y}" r="11" fill="#5ed19d"/>
          <circle id="p-burst" cx="1500" cy="{Y}" r="175" fill="none" stroke="#5ed19d" stroke-width="4"/>
          {hexes}
        </svg>
        <div id="p-sweep" style="clip-path: polygon(50% 0, 93% 25%, 93% 75%, 50% 100%, 7% 75%, 7% 25%)"></div>
        <div id="p-sweep2" style="clip-path: polygon(50% 0, 93% 25%, 93% 75%, 50% 100%, 7% 75%, 7% 25%)"></div>
        <div class="under" style="left:210px">{pill("info", "v1.4.0", "git")}{pill("ok", "Sano")}</div>
        <div class="under" style="left:750px" id="p-qa-under">{pill("bad", "Bloqueada · vulnerabilidad crítica", "lock", "p-blocked")}</div>
        <div class="under" style="left:1290px" id="p-prod-under">{pill("info", "v1.4.0", "git", "p-prod-ver")}{pill("ok", "Sano", None, "p-prod-ok")}</div>
        <div class="chip glass" id="p-chip1" style="color:#f2f5f7;box-shadow: inset 0 0 0 2px #399fef, 0 0 40px rgba(57,159,239,.4)">{ICON["git"]}v1.4.0</div>
        <div class="chip glass" id="p-chip2" style="color:#f2f5f7;box-shadow: inset 0 0 0 2px #399fef">{ICON["git"]}v1.4.1</div>
        <div id="p-checks" class="glass"><h4>Control de calidad y seguridad</h4>
          <div class="crow raised" id="p-c0">Calidad de código<span class="s">{pill("ok","aprobado")}</span></div>
          <div class="crow raised" id="p-c1">Vulnerabilidades<span class="s">{pill("ok","ninguna")}</span></div>
          <div class="crow raised" id="p-c2">Imagen escaneada<span class="s">{pill("ok","limpia")}</span></div>
        </div>
      </div>
    </div>
    <div id="p-text" class="kin"><span id="p-w1x">Revisada</span><span id="p-w2x">por ti,</span><span id="p-w3x">antes</span><span id="p-w4x">de</span><span id="p-w5x" class="g">salir.</span></div>
    <div id="p-stop" class="kin">Si no es seguro, <b>no sale.</b></div>
    <div id="p-banner">{pill("info", "Dev ya corre v1.4.0: se puede promover", "info", "p-ban")}</div>
    <div id="p-btn" class="btn">{ICON["rocket"].replace('class="icon"','class="icon" style="width:36px;height:36px"')}Promover v1.4.0<span class="shine" id="p-shine"></span></div>
    <div class="cursor" id="p-cursor">{CURSOR}</div>
    <div id="p-flash"></div>'''
js = f'''
    const chipAt = (x) => x - 110;
    tl.fromTo("#p-world", {{ x: 1920, filter: "blur(10px)" }}, {{ x: 0, filter: "blur(0px)", duration: 0.6, ease: "power2.inOut" }}, 0);
    const tb = gsap.timeline(); tl.add(tb, 0.3);
    tb.fromTo("#p-cam", cam(560, 560, 1.3), cam(560, 560, 1.3), 0);
    tb.fromTo("#p-flash", {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0);
    tb.fromTo("#p-chip1", {{ x: chipAt(420), y: 236, opacity: 0 }}, {{ x: chipAt(420), y: 250, opacity: 1, duration: 0.4, ease: "expo.out" }}, 0.3);
    tb.fromTo("#p-chip2", {{ x: chipAt(420), y: 236, opacity: 0 }}, {{ x: chipAt(420), y: 236, opacity: 0, duration: 0.01 }}, 0);
    ["#p-sweep", "#p-sweep2", "#p-burst", "#p-checks", "#p-banner", "#p-btn", "#p-stop", "#p-qa-under", "#p-prod-ver", "#p-prod-ok"].forEach((s) => tb.fromTo(s, {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0));
    ["#p-w1x", "#p-w2x", "#p-w3x", "#p-w4x", "#p-w5x"].forEach((w, i) => {{
      tb.fromTo(w, {{ opacity: 0, filter: "blur(6px)" }}, {{ opacity: 1, filter: "blur(0px)", duration: 0.13 }}, 0.25 + i * 0.16 + (i > 1 ? 0.35 : 0));
    }});

    // DEV -> QA: the wire charges, an energy pulse runs it, the chip rides along
    tb.to("#p-cam", {{ ...cam(960, 600, 1.2), duration: 0.6, ease: "power2.inOut" }}, 1.4);
    tb.to("#p-w1", {{ strokeDashoffset: 0, duration: 0.5, ease: "power2.inOut" }}, 1.45);
    tb.fromTo("#p-e1", {{ attr: {{ cx: 590 }}, opacity: 1 }}, {{ attr: {{ cx: 790 }}, duration: 0.5, ease: "power2.inOut" }}, 1.45);
    tb.to("#p-e1", {{ opacity: 0, duration: 0.15 }}, 1.95);
    tb.to("#p-chip1", {{ x: chipAt(960), duration: 0.6, ease: "power2.inOut" }}, 1.4);
    // scan: a radar sweep inside the QA hexagon while the checks land
    tb.to("#p-sweep", {{ opacity: 1, duration: 0.15 }}, 2.0);
    tb.fromTo("#p-sweep", {{ rotation: 0 }}, {{ rotation: 720, duration: 1.3, ease: "none" }}, 2.0);
    tb.to("#p-sweep", {{ opacity: 0, duration: 0.2 }}, 3.2);
    tb.fromTo("#p-checks", {{ ...DEPTH, x: 80 }}, {{ ...LAND, x: 0 }}, 2.0);
    [0, 1, 2].forEach((i) => tb.fromTo(`#p-c${{i}} .pill`, {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)" }}, 2.4 + i * 0.3));
    tb.to("#p-h-qa", {{ attr: {{ stroke: "#5ed19d" }}, duration: 0.2 }}, 3.2);

    // promote: banner, button, click, the chip shoots to PROD
    tb.to("#p-checks", {{ opacity: 0, x: 40, filter: "blur(8px)", duration: 0.2 }}, 3.35);
    tb.to("#p-cam", {{ ...cam(960, 560, 1.0), duration: 0.55, ease: "power2.inOut" }}, 3.3);
    tb.to("#p-banner", {{ opacity: 1, duration: 0.01 }}, 3.4);
    tb.fromTo("#p-ban", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "expo.out" }}, 3.4);
    tb.fromTo("#p-btn", {{ opacity: 0, scale: 0.85 }}, {{ opacity: 1, scale: 1, duration: 0.35, ease: "back.out(1.6)" }}, 3.5);
    tb.fromTo("#p-shine", {{ x: 0 }}, {{ x: 760, duration: 0.5, ease: "power2.inOut" }}, 3.75);
    tb.fromTo("#p-cursor", {{ x: 1950, y: 1150 }}, {{ x: 1000, y: 985, duration: 0.5, ease: "power3.out" }}, 3.55);
    tb.to("#p-cursor", {{ scale: 0.82, duration: 0.07 }}, 4.15);
    tb.to("#p-btn", {{ scale: 0.94, duration: 0.07 }}, 4.15);
    tb.to(["#p-cursor", "#p-btn", "#p-banner"], {{ opacity: 0, duration: 0.18 }}, 4.3);
    tb.to("#p-w2", {{ strokeDashoffset: 0, duration: 0.35, ease: "power3.in" }}, 4.25);
    tb.fromTo("#p-e2", {{ attr: {{ cx: 1130 }}, opacity: 1 }}, {{ attr: {{ cx: 1330 }}, duration: 0.35, ease: "power3.in" }}, 4.25);
    tb.to("#p-e2", {{ opacity: 0, duration: 0.1 }}, 4.6);
    tb.to("#p-chip1", {{ x: chipAt(1500), boxShadow: "inset 0 0 0 2px #5ed19d, 0 0 50px rgba(94,209,157,.5)", duration: 0.35, ease: "power3.in" }}, 4.25);
    tb.to("#p-h-prod", {{ attr: {{ fill: "rgba(16,52,36,.9)" }}, duration: 0.25 }}, 4.6);
    tb.fromTo("#p-burst", {{ opacity: 0.8, scale: 1, transformOrigin: "50% 50%" }}, {{ opacity: 0, scale: 1.45, duration: 0.45, ease: "power2.out", immediateRender: false }}, 4.6);
    tb.to("#p-prod-ver", {{ opacity: 1, duration: 0.01 }}, 4.7);
    tb.fromTo("#p-prod-ver", {{ y: 16 }}, {{ y: 0, duration: 0.35, ease: "expo.out" }}, 4.7);
    tb.to("#p-prod-ok", {{ opacity: 1, duration: 0.01 }}, 4.82);
    tb.fromTo("#p-prod-ok", {{ scale: 0.6 }}, {{ scale: 1, duration: 0.35, ease: "back.out(2)" }}, 4.82);
    tb.to("#p-text", {{ opacity: 0, filter: "blur(8px)", duration: 0.2 }}, 3.15);

    // an unsafe version is caught at QA
    tb.to("#p-h-qa", {{ attr: {{ stroke: "#399fef" }}, duration: 0.2 }}, 5.3);
    tb.to("#p-chip2", {{ opacity: 1, y: 250, duration: 0.35, ease: "expo.out" }}, 5.4);
    tb.to("#p-chip2", {{ x: chipAt(960), duration: 0.5, ease: "power2.inOut" }}, 5.8);
    tb.to("#p-sweep2", {{ opacity: 1, duration: 0.12 }}, 6.3);
    tb.fromTo("#p-sweep2", {{ rotation: 0 }}, {{ rotation: 540, duration: 0.7, ease: "none" }}, 6.3);
    tb.to("#p-sweep2", {{ opacity: 0, duration: 0.15 }}, 7.0);
    tb.to("#p-h-qa", {{ attr: {{ stroke: "#e47c76", fill: "rgba(53,28,26,.9)" }}, duration: 0.15 }}, 6.95);
    tb.to("#p-chip2", {{ boxShadow: "inset 0 0 0 2px #e47c76, 0 0 50px rgba(228,124,118,.55)", color: "#e47c76", duration: 0.15 }}, 6.95);
    tb.fromTo("#p-chip2", {{ x: chipAt(960) }}, {{ x: chipAt(960) - 16, duration: 0.05, yoyo: true, repeat: 5, ease: "none" }}, 7.0);
    tb.to("#p-qa-under", {{ opacity: 1, duration: 0.01 }}, 7.05);
    tb.fromTo("#p-blocked", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "expo.out" }}, 7.05);
    tb.to("#p-stop", {{ opacity: 1, duration: 0.01 }}, 7.2);
    tb.fromTo("#p-stop", {{ filter: "blur(10px)", scale: 1.06 }}, {{ filter: "blur(0px)", scale: 1, duration: 0.22, ease: "expo.out" }}, 7.2);
    tb.to("#p-stop", {{ opacity: 0, filter: "blur(8px)", duration: 0.18 }}, 9.0);

    // zoom through the PROD hexagon
    tb.to("#p-cam", {{ ...cam(1500, 520, 12), duration: 0.75, ease: "power3.in" }}, 9.25);
    tb.to("#p-flash", {{ opacity: 1, duration: 0.25, ease: "power2.in" }}, 9.72);'''
open(OUT + "promote.html", "w").write(scene("promote", css, body, js))
