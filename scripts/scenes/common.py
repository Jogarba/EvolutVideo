# Shared console look for every scene, mirrored from evolut-idp-ui-v2 (index.css, surfaces.ts, StatusPill).
FONTS = '''
    @font-face { font-family: "Michroma"; src: url("assets/fonts/Michroma-Regular.ttf") format("truetype"); font-weight: 400; font-display: block; }
    @font-face { font-family: "Hanken Grotesk Variable"; src: url("assets/fonts/HankenGrotesk-Variable.ttf") format("truetype"); font-weight: 300 700; font-display: block; }
    @font-face { font-family: "JetBrains Mono Variable"; src: url("assets/fonts/JetBrainsMono-Variable.ttf") format("truetype"); font-weight: 400 600; font-display: block; }'''
CSS = FONTS + '''
    #root { position: absolute; inset: 0; overflow: hidden; color: #f2f5f7; font-family: "Hanken Grotesk Variable", sans-serif; }
    .glass { background: linear-gradient(180deg, rgba(25,34,44,.84), rgba(10,15,20,.86)); backdrop-filter: blur(18px) saturate(1.3); box-shadow: inset 0 1.5px 0 rgba(255,255,255,.16), inset 0 0 0 1.5px rgba(242,245,247,.12), 0 50px 120px rgba(0,0,0,.6), 0 0 90px rgba(57,159,239,.12); border-radius: 32px; }
    /* light falling on the glass from the hall's ceiling lamps */
    .glass::after { content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none; background: linear-gradient(118deg, rgba(255,255,255,.08), rgba(255,255,255,0) 38%), radial-gradient(120% 60% at 50% 0%, rgba(57,159,239,.10), rgba(57,159,239,0) 60%); }
    .raised { background: linear-gradient(180deg, rgba(30,38,46,.92), rgba(20,25,30,.92)); border-radius: 18px; box-shadow: inset 0 1px 0 rgba(255,255,255,.07), 0 8px 24px rgba(0,0,0,.25); }
    .well { background: rgba(7,12,16,.72); border-radius: 16px; }
    .frost { background: rgba(14,19,24,.80); box-shadow: inset 0 0 0 1.5px rgba(242,245,247,.2); border-radius: 999px; }
    .pill { display: inline-flex; align-items: center; gap: 10px; border-radius: 999px; padding: 8px 20px; font-size: 28px; font-weight: 500; white-space: nowrap; }
    .pill svg { width: 26px; height: 26px; flex: none; }
    .ok { color: #5ed19d; background: #102a1e; } .warn { color: #f4b85a; background: #2f210c; }
    .bad { color: #e47c76; background: #351c1a; } .info { color: #399fef; background: #132636; }
    .neu { color: #94999e; background: rgba(22,27,32,.92); }
    .mono { font-family: "JetBrains Mono Variable", monospace; }
    .muted { color: #94999e; } .body { color: #bfc3c7; }
    .kin { font-family: "Michroma", sans-serif; text-shadow: 0 0 28px #070c10, 0 0 14px #070c10, 0 0 4px #070c10; }
    .halo { text-shadow: 0 0 22px #070c10, 0 0 10px #070c10, 0 0 3px #070c10; }
    .btn { display: inline-flex; align-items: center; justify-content: center; gap: 14px; border-radius: 16px; background: #399fef; color: #000e1d; font-weight: 700; overflow: hidden; position: relative; }
    .shine { position: absolute; top: 0; bottom: 0; width: 140px; left: -200px; background: linear-gradient(100deg, rgba(255,255,255,0), rgba(255,255,255,.55), rgba(255,255,255,0)); }
    .cursor { position: absolute; left: 0; top: 0; width: 84px; height: 84px; z-index: 20; filter: drop-shadow(0 8px 16px rgba(0,0,0,.55)); }
    .led { fill: #5ed19d; filter: drop-shadow(0 0 4px rgba(94,209,157,.8)); }
    .icon { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }'''
ICON = {
  'ok': '<svg viewBox="0 0 24 24" class="icon"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>',
  'bad': '<svg viewBox="0 0 24 24" class="icon"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6M9 9l6 6"/></svg>',
  'info': '<svg viewBox="0 0 24 24" class="icon"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>',
  'spin': '<svg viewBox="0 0 24 24" class="icon"><path d="M21 12a9 9 0 1 1-6.219-8.56"/></svg>',
  'lock': '<svg viewBox="0 0 24 24" class="icon"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
  'git': '<svg viewBox="0 0 24 24" class="icon"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="9" r="3"/><path d="M6 9v6M18 12c0 4-6 3-9 6"/></svg>',
  'globe': '<svg viewBox="0 0 24 24" class="icon"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>',
  'server': '<svg viewBox="0 0 24 24" class="icon"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><path d="M6 6h.01M6 18h.01"/></svg>',
  'cog': '<svg viewBox="0 0 24 24" class="icon"><path d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg>',
  'db': '<svg viewBox="0 0 24 24" class="icon"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.7 4 3 9 3s9-1.3 9-3V5M3 12c0 1.7 4 3 9 3s9-1.3 9-3"/></svg>',
  'rocket': '<svg viewBox="0 0 24 24" class="icon"><path d="M4.5 16.5c-1.5 1.3-2 5-2 5s3.7-.5 5-2c.7-.8.7-2.1-.1-2.9a2.2 2.2 0 0 0-2.9-.1zM12 15l-3-3a22 22 0 0 1 2-3.9A12.9 12.9 0 0 1 22 2c0 2.7-.8 7.5-6 11a22.4 22.4 0 0 1-4 2z"/></svg>',
}
CURSOR = '<svg viewBox="0 0 24 24"><path d="M4 2l15 11-6.5 1.2L16 21l-3 1.4-3.6-6.8L4 20z" fill="#f2f5f7" stroke="#05080d" stroke-width="1.2"/></svg>'
def pill(tone, label, icon=None, id=None, extra=''):
    i = f' id="{id}"' if id else ''
    return f'<span class="pill {tone} {extra}"{i}>{ICON[icon or tone] if (icon or tone in ICON) else ""}<span>{label}</span></span>'
# How much slower than authored each scene plays, so its beats span its narration line.
STRETCH = {"build": 1.2, "promote": 1.1, "live": 0.9, "scale": 1.05, "graph": 1.05}
def scene(cid, css, body, js):
    return f'''<template>
  <style>{CSS}
{css}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="1920" data-height="1080">
{body}
  </div>
  <script>
    gsap.config({{ force3D: false }});
    const root = gsap.timeline({{ paused: true }});
    const tl = gsap.timeline();
    const cam = (px, py, s) => ({{ x: 960 - px * s, y: 560 - py * s, scale: s }});
    // a pane rises out of depth: tilted back, lower and blurred, landing flat
    const DEPTH = {{ opacity: 0, y: 90, rotationX: 18, scale: 0.94, transformPerspective: 1800, filter: "blur(10px)" }};
    const LAND = {{ opacity: 1, y: 0, rotationX: 0, scale: 1, filter: "blur(0px)", duration: 0.75, ease: "expo.out" }};
{js}
    root.add(tl.timeScale({1 / STRETCH.get(cid, 1):.6f}), 0);
    window.__timelines["{cid}"] = root;
  </script>
</template>
'''
from pathlib import Path
OUT = str(Path(__file__).resolve().parents[2] / "compositions") + "/"

K = 0.577
def unit(uid, cx, y0, w, h, tone="#399fef", lit="#66b8ff"):
    """One isometric replica server, shared by the live rack and the scaling stage.
    Ids: {uid} group, {uid}-led0..2, {uid}-g (load gauge), {uid}-base (platform ring)."""
    P = lambda ps: ' '.join(f'{x:.1f},{y:.1f}' for x, y in ps)
    t = [(cx, y0), (cx+w, y0+w*K), (cx, y0+2*w*K), (cx-w, y0+w*K)]
    l = [(cx-w, y0+w*K), (cx, y0+2*w*K), (cx, y0+2*w*K+h), (cx-w, y0+w*K+h)]
    r = [(cx, y0+2*w*K), (cx+w, y0+w*K), (cx+w, y0+w*K+h), (cx, y0+2*w*K+h)]
    ry = lambda x: y0 + 2*w*K - (x - cx)*K
    ly = lambda x: y0 + w*K + (x - (cx - w))*K
    lid = [(cx, y0+w*K*0.35), (cx+w*0.65, y0+w*K), (cx, y0+w*K*1.65), (cx-w*0.65, y0+w*K)]
    hx = [(cx + w*0.2*dx, y0 + w*K + w*0.2*dy*K) for dx, dy in ((0, -1.6), (1, -0.8), (1, 0.8), (0, 1.6), (-1, 0.8), (-1, -0.8))]
    x1, x2 = cx + w*0.56, cx + w - 12
    gauge = [(x1, ry(x1)+26), (x2, ry(x2)+26), (x2, ry(x2)+h-16), (x1, ry(x1)+h-16)]
    ticks = ''.join(f'<line x1="{x1-6:.1f}" y1="{ry(x1)+26+(h-42)*q/4:.1f}" x2="{x1-1:.1f}" y2="{ry(x1)+26+(h-42)*q/4:.1f}" stroke="{tone}" stroke-opacity=".6" stroke-width="2"/>' for q in range(5))
    bays = ''.join(f'<path d="M{cx+10:.1f} {ry(cx+10)+28+k*24:.1f} L{cx+w*0.44:.1f} {ry(cx+w*0.44)+28+k*24:.1f} L{cx+w*0.44:.1f} {ry(cx+w*0.44)+40+k*24:.1f} L{cx+10:.1f} {ry(cx+10)+40+k*24:.1f}Z" fill="#0b1520" stroke="#2a4a66" stroke-width="1.5"/><circle cx="{cx+w*0.38:.1f}" cy="{ry(cx+w*0.38)+34+k*24:.1f}" r="2.2" fill="{tone}" fill-opacity=".8"/>' for k in range(5))
    vents = ''.join(f'<line x1="{cx-w+14}" y1="{ly(cx-w+14)+80+k*13:.1f}" x2="{cx-14}" y2="{ly(cx-14)+80+k*13:.1f}" stroke="#203a52" stroke-width="3" stroke-linecap="round"/>' for k in range(7))
    screws = ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.5" fill="#355a7a"/>' for x, y in [(cx-w+8, ly(cx-w+8)+10), (cx-8, ly(cx-8)+10), (cx-w+8, ly(cx-w+8)+h-10), (cx-8, ly(cx-8)+h-10)])
    leds = ''.join(f'<circle id="{uid}-led{j}" class="led" cx="{cx-w+22+j*20:.1f}" cy="{ly(cx-w+22+j*20)+34:.1f}" r="6"/>' for j in range(3))
    by = y0 + 2*w*K + h + 16
    cable = f'<path d="M{cx-w*0.55:.1f} {ly(cx-w*0.55)+h-6:.1f} C{cx-w*0.7:.1f} {by+6:.1f} {cx-w*1.2:.1f} {by+4:.1f} {cx-w*1.35:.1f} {by+14:.1f}" fill="none" stroke="#0b1520" stroke-width="7" stroke-linecap="round"/><path d="M{cx-w*0.55:.1f} {ly(cx-w*0.55)+h-6:.1f} C{cx-w*0.7:.1f} {by+6:.1f} {cx-w*1.2:.1f} {by+4:.1f} {cx-w*1.35:.1f} {by+14:.1f}" fill="none" stroke="{tone}" stroke-opacity=".35" stroke-width="2"/>'
    edge = f'<polyline points="{P([(cx-w, y0+w*K), (cx, y0+2*w*K), (cx+w, y0+w*K)])}" fill="none" stroke="#d6ecff" stroke-opacity=".75" stroke-width="2.5"/><line x1="{cx}" y1="{y0+2*w*K}" x2="{cx}" y2="{y0+2*w*K+h}" stroke="#d6ecff" stroke-opacity=".35" stroke-width="2"/>'
    return f'''<g id="{uid}">
      <ellipse cx="{cx}" cy="{by}" rx="{w*1.18:.1f}" ry="{w*0.36:.1f}" fill="{tone}" fill-opacity=".10"/>
      <ellipse id="{uid}-base" cx="{cx}" cy="{by}" rx="{w*1.0:.1f}" ry="{w*0.3:.1f}" fill="none" stroke="{tone}" stroke-opacity=".55" stroke-width="2.5" stroke-dasharray="10 8"/>
      {cable}
      <polygon points="{P(l)}" fill="url(#u-gl)" stroke="{tone}" stroke-opacity=".55" stroke-width="2"/>
      <polygon points="{P(r)}" fill="url(#u-gr)" stroke="{tone}" stroke-opacity=".55" stroke-width="2"/>
      {vents}{screws}{bays}{ticks}
      <polygon points="{P(gauge)}" fill="#05090d" stroke="#2a4a66" stroke-width="2"/>
      <polygon id="{uid}-g" points="{P(gauge)}" fill="{tone}"/>
      <polygon points="{P(t)}" fill="url(#u-gt)" stroke="{lit}" stroke-width="2.5"/>
      <polygon points="{P(lid)}" fill="none" stroke="{lit}" stroke-opacity=".35" stroke-width="1.5"/>
      <polygon points="{P(hx)}" fill="{tone}" fill-opacity=".25" stroke="{lit}" stroke-width="2"/>
      {edge}{leds}
    </g>'''
UNIT_DEFS = '''<defs>
      <linearGradient id="u-gt" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#335f86"/><stop offset="1" stop-color="#17304a"/></linearGradient>
      <linearGradient id="u-gl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#16283a"/><stop offset="1" stop-color="#091019"/></linearGradient>
      <linearGradient id="u-gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b3045"/><stop offset="1" stop-color="#0c1620"/></linearGradient>
    </defs>'''

# ── v2: cinematic stations ─────────────────────────────────────────────
# The frame is letterboxed to 2.39:1 by the root; everything sits inside y 150..930.
STATION_CSS = '''
    #root .world { position: absolute; inset: 0; }
    .st-chip { position: absolute; left: 150px; top: 250px; font: 600 26px "JetBrains Mono Variable", monospace; letter-spacing: 4px; color: #66b8ff; display: flex; align-items: center; gap: 14px; }
    .st-chip i { width: 46px; height: 2px; background: #66b8ff; display: block; }
    .st-h { position: absolute; left: 150px; top: 310px; width: 760px; font-family: "Michroma", sans-serif; font-size: 78px; line-height: 1.12; text-shadow: 0 0 30px #070c10, 0 0 12px #070c10; }
    .st-h b { color: #399fef; font-weight: 400; }
    .st-sub { position: absolute; left: 150px; top: 560px; width: 700px; font-size: 38px; line-height: 1.35; color: #d6dde3; text-shadow: 0 0 18px #070c10, 0 0 6px #070c10; }
    .hero { position: absolute; left: 940px; top: 160px; width: 860px; height: 760px; }
    .glow { position: absolute; border-radius: 50%; pointer-events: none; }
'''
def station(n, label, h1, h2, sub):
    return f'''      <div class="st-chip" id="st-chip"><i></i>ESTACIÓN {n:02d} · {label}</div>
      <div class="st-h" id="st-h"><span id="st-h1">{h1}</span><br><b id="st-h2">{h2}</b></div>
      <div class="st-sub" id="st-sub">{sub}</div>'''
STATION_IN = '''
    // the factory camera arrives from the previous station
    tl.fromTo("#world", { x: 1920, filter: "blur(10px)" }, { x: 0, filter: "blur(0px)", duration: 0.6, ease: "power2.inOut" }, 0);
    tl.fromTo("#st-chip", { opacity: 0, x: -30 }, { opacity: 1, x: 0, duration: 0.5, ease: "expo.out" }, 0.45);
    tl.fromTo("#st-h1", { opacity: 0, filter: "blur(10px)", y: 20 }, { opacity: 1, filter: "blur(0px)", y: 0, duration: 0.5, ease: "expo.out" }, 0.55);
    tl.fromTo("#st-h2", { opacity: 0, filter: "blur(10px)", y: 20 }, { opacity: 1, filter: "blur(0px)", y: 0, duration: 0.5, ease: "expo.out" }, 0.75);
    tl.fromTo("#st-sub", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.5, ease: "expo.out" }, 1.1);'''
def station_out(t):
    return f'''
    // and leaves for the next one
    tl.to("#world", {{ x: -1920, filter: "blur(10px)", duration: 0.6, ease: "power2.inOut" }}, {t});'''

# ── v3: symmetric stations with cinematic effects (overrides the v2 helpers above) ──
STRETCH.update({"reveal": 1.05, "fast": 1.3125, "secure": 1.15625, "always": 1.09375, "grows": 1.1875})
STATION_CSS = '''
    #root .world { position: absolute; inset: 0; }
    .st-chip { position: absolute; left: 0; right: 0; top: 168px; display: flex; justify-content: center; align-items: center; gap: 16px; font: 600 24px "JetBrains Mono Variable", monospace; letter-spacing: 5px; color: #66b8ff; }
    .st-chip i { width: 60px; height: 2px; background: linear-gradient(90deg, rgba(102,184,255,0), #66b8ff); display: block; }
    .st-chip i + span + i { background: linear-gradient(90deg, #66b8ff, rgba(102,184,255,0)); }
    .st-h { position: absolute; left: 0; right: 0; top: 206px; text-align: center; font-family: "Michroma", sans-serif; font-size: 66px; white-space: nowrap; filter: drop-shadow(0 0 18px #070c10) drop-shadow(0 0 6px #070c10); }
    .st-h span, .st-h b { display: inline-block; font-weight: 400; background-size: 300% 100%; background-position: 100% 0; -webkit-background-clip: text; background-clip: text; color: transparent; }
    .st-h span { background-image: linear-gradient(100deg, #f2f5f7 40%, #ffffff 47%, #a6d0f6 50%, #ffffff 53%, #f2f5f7 60%); }
    .st-h b { background-image: linear-gradient(100deg, #399fef 40%, #a6d0f6 47%, #ffffff 50%, #a6d0f6 53%, #399fef 60%); }
    .hero { position: absolute; left: 530px; top: 300px; width: 860px; height: 760px; transform: scale(.82); transform-origin: 50% 0; }
    #hero-in { position: absolute; inset: 0; }
    .glow { position: absolute; border-radius: 50%; pointer-events: none; }
    #st-pool { position: absolute; left: 560px; top: 760px; width: 800px; height: 150px; border-radius: 50%; background: radial-gradient(closest-side, rgba(102,184,255,.45), rgba(102,184,255,0)); }
    #st-streak { position: absolute; left: -200px; top: 538px; width: 2320px; height: 6px; background: linear-gradient(90deg, rgba(102,184,255,0), rgba(230,243,255,.95) 50%, rgba(102,184,255,0)); filter: blur(2px); }
    #st-flash { position: absolute; inset: 0; background: radial-gradient(ellipse at center, rgba(166,208,246,.55), rgba(57,159,239,0) 70%); }
    .spk { position: absolute; width: 6px; height: 6px; border-radius: 50%; background: #d6ecff; box-shadow: 0 0 10px #66b8ff; opacity: 0; }
'''
def station(n, label, h1, h2, sub=None):
    import random
    r = random.Random(n * 31)
    sparks = ''.join(f'<i class="spk" id="spk{i}" style="left:{r.randint(620, 1300)}px;top:{r.randint(700, 880)}px"></i>' for i in range(16))
    return f'''      <div id="st-pool"></div>{sparks}
      <div class="st-chip" id="st-chip"><i></i><span>ESTACIÓN {n:02d} · {label}</span><i></i></div>
      <div class="st-h" id="st-h"><span id="st-h1">{h1}</span> <b id="st-h2">{h2}</b></div>'''
def station_fx(n):
    import random
    r = random.Random(n * 31)
    return '\n    '.join(f'tl.fromTo("#spk{i}", {{ y: 0, opacity: 0 }}, {{ keyframes: [{{ opacity: 0.9, duration: 0.3 }}, {{ y: -{r.randint(260, 520)}, x: {r.randint(-60, 60)}, opacity: 0, duration: {r.uniform(1.8, 3.2):.2f}, ease: "power1.out" }}] }}, {r.uniform(0.9, 4.2):.2f});' for i in range(16))
STATION_IN = '''
    // the factory camera arrives: a light streak and flash mark the cut
    tl.fromTo("#world", { x: 1920, filter: "blur(10px)" }, { x: 0, filter: "blur(0px)", duration: 0.6, ease: "power2.inOut" }, 0);
    tl.fromTo("#st-flash", { opacity: 0.6 }, { opacity: 0, duration: 0.7, ease: "power2.out" }, 0.15);
    tl.fromTo("#st-streak", { scaleX: 0.05, opacity: 0 }, { keyframes: [{ scaleX: 1, opacity: 1, duration: 0.35, ease: "expo.out" }, { opacity: 0, duration: 0.6 }] }, 0.25);
    tl.fromTo("#st-chip", { opacity: 0, letterSpacing: "18px" }, { opacity: 1, letterSpacing: "5px", duration: 0.8, ease: "expo.out" }, 0.4);
    tl.fromTo("#st-h1", { opacity: 0, y: 40, filter: "blur(12px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.6, ease: "expo.out" }, 0.55);
    tl.fromTo("#st-h2", { opacity: 0, y: 40, filter: "blur(12px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.6, ease: "expo.out" }, 0.7);
    tl.fromTo(["#st-h1", "#st-h2"], { backgroundPosition: "100% 0" }, { backgroundPosition: "0% 0", duration: 1.2, ease: "power2.inOut" }, 1.1);
    // the hero swings in from depth, lands, then the camera orbits it slowly
    tl.fromTo("#hero-in", { opacity: 0, rotationY: -28, rotationX: 10, scale: 0.8, transformPerspective: 2200, filter: "blur(12px)" }, { opacity: 1, rotationY: 0, rotationX: 0, scale: 1, filter: "blur(0px)", duration: 1.0, ease: "expo.out" }, 0.3);
    tl.to("#hero-in", { rotationY: -6, x: -18, duration: 4.6, ease: "sine.inOut" }, 1.3);
    tl.fromTo("#st-pool", { opacity: 0, scaleX: 0.3 }, { keyframes: [{ opacity: 1, scaleX: 1.15, duration: 0.6, ease: "expo.out" }, { scaleX: 1, opacity: 0.75, duration: 0.8 }] }, 0.8);'''
def station_out(t):
    return f'''
    tl.to("#world", {{ x: -1920, filter: "blur(10px)", duration: 0.6, ease: "power2.inOut" }}, {t});'''

# ── narration sync: place an event on the word that names it ─────────────
import json as _json, os as _os, unicodedata as _ud
HOST = {"hook": 0, "problem": 5.6, "reveal": 14.4, "fast": 24.9, "secure": 32.906, "always": 39.959, "grows": 46.631, "outcome": 53.875, "endcard": 59.6}
VO = {'hook': 0.08, 'problem': 4.1, 'reveal': 12.78, 'fast': 20.81, 'secure': 29.3, 'always': 36.08, 'grows': 42.34, 'outcome': 48.79, 'cta': 53.22}
_VODIR = _os.path.join(_os.path.dirname(OUT.rstrip("/")), "assets", "vo")
def _norm(w): return ''.join(c for c in _ud.normalize("NFD", w.lower()) if c.isalnum() and _ud.category(c) != "Mn")
def at(scene_id, word, line=None, nth=1, lead=0.0):
    """Authored time (scene-local, before the scene's stretch) at which `word` starts in narration `line`."""
    line = line or scene_id
    words = _json.load(open(_os.path.join(_VODIR, f"{line}.words.json")))
    hits = [w for w in words if _norm(w["w"]) == _norm(word)]
    assert len(hits) >= nth, f"{word!r} not in {line}"
    real = VO[line] + hits[nth - 1]["t"] - HOST[scene_id] - lead
    return round(real / STRETCH.get(scene_id, 1), 3)

# ── v4: overshoot, cascades, three-layer parallax and constant micro-motion (overrides v3) ──
STATION_CSS = STATION_CSS + '''
    #st-fg { position: absolute; inset: 0; pointer-events: none; }
    .bk { position: absolute; border-radius: 50%; background: radial-gradient(circle, rgba(166,208,246,.55), rgba(57,159,239,0) 70%); filter: blur(6px); }
    .st-h .w { display: inline-block; }
'''
_station_v3 = station
def station(n, label, h1, h2, sub=None):
    import random
    r = random.Random(n * 53)
    bokeh = ''.join(f'<i class="bk" style="left:{r.choice([r.randint(-60, 380), r.randint(1540, 1980)])}px;top:{r.randint(120, 980)}px;width:{(s := r.randint(70, 190))}px;height:{s}px;opacity:{r.uniform(.12, .3):.2f}"></i>' for _ in range(9))
    return _station_v3(n, label, h1, h2) + f'\n      <div id="st-fg">{bokeh}</div>'
STATION_IN = '''
    // the factory camera arrives: a light streak and flash mark the cut
    tl.fromTo("#world", { x: 1920, filter: "blur(10px)" }, { x: 0, filter: "blur(0px)", duration: 0.6, ease: "power2.inOut" }, 0);
    tl.fromTo("#st-flash", { opacity: 0.6 }, { opacity: 0, duration: 0.7, ease: "power2.out" }, 0.15);
    tl.fromTo("#st-streak", { scaleX: 0.05, opacity: 0 }, { keyframes: [{ scaleX: 1, opacity: 1, duration: 0.35, ease: "expo.out" }, { opacity: 0, duration: 0.6 }] }, 0.25);
    // one after another: chip, first words, accent words, then the hero — each lands with a small overshoot
    tl.fromTo("#st-chip", { opacity: 0, letterSpacing: "18px" }, { opacity: 1, letterSpacing: "5px", duration: 0.8, ease: "back.out(1.4)" }, 0.4);
    [["#st-h1", 0.55], ["#st-h2", 0.75]].forEach(([s, t]) => {
      tl.fromTo(s, { opacity: 0, filter: "blur(12px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.45, ease: "power2.out" }, t);
      tl.fromTo(s, { y: 46, scale: 0.92 }, { y: 0, scale: 1, duration: 0.7, ease: "back.out(1.7)" }, t);
    });
    tl.fromTo(["#st-h1", "#st-h2"], { backgroundPosition: "100% 0" }, { backgroundPosition: "0% 0", duration: 1.2, ease: "power2.inOut" }, 1.15);
    tl.fromTo("#hero-in", { opacity: 0, filter: "blur(12px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.6, ease: "power2.out" }, 0.3);
    tl.fromTo("#hero-in", { rotationY: -28, rotationX: 10, scale: 0.8, transformPerspective: 2200 }, { rotationY: 0, rotationX: 0, scale: 1, duration: 1.1, ease: "back.out(1.35)" }, 0.3);
    tl.fromTo("#st-pool", { opacity: 0, scaleX: 0.3 }, { keyframes: [{ opacity: 1, scaleX: 1.15, duration: 0.6, ease: "back.out(1.6)" }, { scaleX: 1, opacity: 0.75, duration: 0.8 }] }, 0.8);
    // parallax: text drifts slowest, the hero at mid speed, the front motes fastest (the hall behind moves least, from the root)
    tl.fromTo(["#st-chip", "#st-h"], { x: 0 }, { x: 14, duration: 6.2, ease: "sine.inOut" }, 0.2);
    tl.to("#hero-in", { rotationY: -6, x: -42, duration: 5.4, ease: "sine.inOut" }, 1.3);
    tl.fromTo("#st-fg", { x: 120 }, { x: -170, duration: 6.4, ease: "none" }, 0);
    // micro-motion so nothing ever sits frozen
    tl.fromTo("#hero-in", { y: 0 }, { y: -7, duration: 1.3, ease: "sine.inOut", yoyo: true, repeat: 3 }, 1.4);
    tl.fromTo("#st-pool", { scaleY: 1 }, { scaleY: 1.12, duration: 1.3, ease: "sine.inOut", yoyo: true, repeat: 3 }, 1.4);
    tl.fromTo(".bk", { y: 0 }, { y: -26, duration: 2.6, ease: "sine.inOut", yoyo: true, repeat: 1, stagger: 0.2 }, 0.3);'''

# ── v5: spring physics for every arrival ──────────────────────────────
# A damped spring (ζ 0.72, ω 11): fast start, soft brake, a ~3.5 % elastic overshoot, settled by t = 1.
SPRING_JS = "    const SPRING = (t) => { const z = 0.72, w = 11, wd = w * Math.sqrt(1 - z * z); return t >= 1 ? 1 : 1 - Math.exp(-z * w * t) * (Math.cos(wd * t) + (z * w / wd) * Math.sin(wd * t)); };\n"
import re as _re
_scene_v4 = scene
def scene(cid, css, body, js):
    # arrivals spring into place; continuous drifts (sine), exits (.in) and constant loops keep their own curve
    js = _re.sub(r'ease: "(?:expo|power[234])\.out"|ease: "back\.out\([\d.]+\)"', 'ease: SPRING', js)
    return _scene_v4(cid, css, body, SPRING_JS + js)

# ── v5: match-cut stations (overrides v4 entrance) ────────────────────
STATION_IN = STATION_IN.replace('''tl.fromTo("#world", { x: 1920, filter: "blur(10px)" }, { x: 0, filter: "blur(0px)", duration: 0.6, ease: "power2.inOut" }, 0);''',
                                '''tl.fromTo("#world", { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "power1.out" }, 0);''')
SPOT_CSS = '''
    .spot { position: absolute; border-radius: 26px; background: linear-gradient(180deg, rgba(28,38,49,.96), rgba(12,17,23,.96)); box-shadow: 0 0 0 2px rgba(102,184,255,.85), 0 0 50px rgba(57,159,239,.55), 0 50px 110px rgba(0,0,0,.75); }
    .dim { position: absolute; left: -540px; top: -400px; width: 1940px; height: 1500px; background: radial-gradient(ellipse 40% 34% at 50% 45%, rgba(3,6,10,0), rgba(3,6,10,.62) 100%); pointer-events: none; opacity: 0; }
    .orb { position: absolute; width: 60px; height: 60px; margin: -30px 0 0 -30px; border-radius: 50%; background: radial-gradient(circle, #ffffff, #a6d0f6 35%, rgba(57,159,239,.5) 60%, rgba(57,159,239,0) 72%); box-shadow: 0 0 60px #66b8ff; }
'''

# ── v6: live camera rig ───────────────────────────────────────────────
# world > #cam (big moves: plunges, orbits, whips) > #drift (constant slow dolly + float) > content
STATION_CSS = STATION_CSS + '''
    #cam, #drift { position: absolute; inset: 0; transform-origin: 50% 52%; }
'''
RIG_JS = '''
    // camera moves: a short kick the other way, then a spring that covers 80 % in the first 0.2 s and lands with a small overshoot
    const rig = (props, t, dur = 0.75) => tl.to("#cam", { ...props, duration: dur, ease: SPRING }, t);
    const kick = (props, t) => tl.to("#cam", { ...props, duration: 0.14, ease: "power2.inOut" }, t - 0.14);
    const aim = (x, y, t) => tl.set("#cam", { transformOrigin: `${x}px ${y}px` }, t);
    tl.fromTo("#drift", { scale: 1, rotation: -0.4, x: 0 }, { scale: 1.055, rotation: 0.5, x: -16, duration: 7, ease: "sine.inOut" }, 0);
'''
