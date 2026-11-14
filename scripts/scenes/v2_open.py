import sys, math, random; sys.path.insert(0, sys.path[0])
from common import *
rnd = random.Random(11)
import re as _re
def R(js): return _re.sub(r"@@(.+?)@@", lambda m: str(round(eval(m.group(1)), 3)), js)

# ── hook: an idea sparks in the dark ──────────────────────────────
motes = ''.join(f'<i class="mote" id="h-m{i}"></i>' for i in range(22))
mote_js = []
for i in range(22):
    a = rnd.uniform(0, 2*math.pi); r = rnd.uniform(380, 900)
    mote_js.append(f'tl.fromTo("#h-m{i}", {{ x: {math.cos(a)*r:.0f}, y: {math.sin(a)*r*0.6:.0f}, opacity: 0 }}, {{ keyframes: [{{ opacity: 0.9, duration: 0.4 }}, {{ x: 0, y: 0, opacity: 0, duration: {rnd.uniform(1.4, 2.6):.2f}, ease: "power2.in" }}] }}, {rnd.uniform(0, 1.6):.2f});')
hook_css = '''
    #h-spark { position: absolute; left: 960px; top: 540px; }
    #h-core { position: absolute; left: -10px; top: -10px; width: 20px; height: 20px; border-radius: 50%; background: #fff; box-shadow: 0 0 20px #fff, 0 0 60px #a6d0f6, 0 0 120px #399fef; }
    #h-halo { position: absolute; left: -220px; top: -220px; width: 440px; height: 440px; border-radius: 50%; background: radial-gradient(closest-side, rgba(102,184,255,.55), rgba(57,159,239,.12) 45%, rgba(57,159,239,0)); }
    #h-fx { position: absolute; left: -420px; top: -2px; width: 840px; height: 4px; background: linear-gradient(90deg, rgba(166,208,246,0), #e6f3ff 50%, rgba(166,208,246,0)); }
    #h-fy { position: absolute; left: -2px; top: -160px; width: 4px; height: 320px; background: linear-gradient(180deg, rgba(166,208,246,0), #e6f3ff 50%, rgba(166,208,246,0)); }
    .mote { position: absolute; left: 957px; top: 537px; width: 6px; height: 6px; border-radius: 50%; background: #a6d0f6; box-shadow: 0 0 10px #66b8ff; }
    .ring { position: absolute; left: 760px; top: 340px; width: 400px; height: 400px; border-radius: 50%; border: 2px solid rgba(166,208,246,.7); opacity: 0; }
    #h-l1 { position: absolute; left: 0; right: 0; top: 600px; text-align: center; font-size: 58px; font-weight: 500; }
    #h-l1 span { display: inline-block; margin: 0 9px; }
    #h-l2 { position: absolute; left: 0; right: 0; top: 690px; text-align: center; font-family: "Michroma", sans-serif; font-size: 70px; white-space: nowrap; }
    #h-l2 b { color: #399fef; font-weight: 400; }
'''
hook_words = "¿Y si tu próxima gran idea".split()
hook_body = f'''    {motes}
    <div id="h-spark"><div id="h-halo"></div><div id="h-fx"></div><div id="h-fy"></div><div id="h-core"></div></div>
    <div class="ring" id="h-r0"></div><div class="ring" id="h-r1"></div><div class="ring" id="h-r2"></div>
'''
hook_js = '\n    '.join(mote_js) + '''
    tl.fromTo("#h-spark", { scale: 0.9 }, { scale: 1.3, duration: 5.4, ease: "sine.inOut" }, 0);
    tl.fromTo("#h-core", { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.6, ease: "expo.out" }, 0.2);
    tl.fromTo("#h-halo", { scale: 0.2, opacity: 0 }, { scale: 1, opacity: 1, duration: 1.4, ease: "power2.out" }, 0.3);
    tl.fromTo(["#h-fx", "#h-fy"], { scaleX: 0, scaleY: 0, opacity: 0 }, { scaleX: 1, scaleY: 1, opacity: 1, duration: 0.9, ease: "expo.out" }, 0.4);
    tl.to("#h-halo", { scale: 1.35, duration: 1.2, ease: "power2.inOut" }, 1.8);
    [0, 1, 2].forEach((i) => tl.fromTo(`#h-r${i}`, { scale: 0.1, opacity: 0.9 }, { scale: 2.6, opacity: 0, duration: 1.6, ease: "power2.out" }, @@at("hook", "hoy") - 0.1@@ + i * 0.3));
    tl.to("#h-core", { scale: 1.8, duration: 0.25, yoyo: true, repeat: 1, ease: "back.out(2)" }, @@at("hook", "hoy")@@);
    // ...but the spark sputters: that is the problem
    tl.to(["#h-fx", "#h-fy"], { scaleX: 0.05, scaleY: 0.05, opacity: 0, duration: 0.4, ease: "power3.in" }, 4.8);
    tl.to("#h-halo", { scale: 0.3, opacity: 0.2, duration: 0.6, ease: "power3.in" }, 4.8);
    tl.to("#h-core", { backgroundColor: "#6c737a", boxShadow: "0 0 6px #6c737a", scale: 0.6, duration: 0.5, ease: "power2.in" }, 4.9);'''
_ = (scene("hook", hook_css, hook_body, R(hook_js)))

# ── problem: the usual way is slow, costly, complicated ──────────
chaos = [("Servidores", 260, 250, .9), ("Configuraciones", 1340, 230, .8), ("Facturas", 1500, 640, .95), ("Actualizaciones", 180, 640, .85),
         ("Copias de seguridad", 640, 820, .7), ("Certificados", 1150, 820, .75), ("Caídas", 820, 180, .7), ("Permisos", 1620, 440, .7), ("Redes", 90, 450, .7)]
cards = ''.join(f'<div class="cx glass" id="p-c{i}" style="left:{x}px;top:{y}px"><svg viewBox="0 0 24 24" class="icon"><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h16.9a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0zM12 9v4M12 17h.01"/></svg>{w}</div>' for i, (w, x, y, s) in enumerate(chaos))
cables = ''.join(f'<path d="M{rnd.randint(-100,2000)} {rnd.randint(100,1000)} C{rnd.randint(0,1920)} {rnd.randint(0,1080)} {rnd.randint(0,1920)} {rnd.randint(0,1080)} {rnd.randint(-100,2000)} {rnd.randint(100,1000)}" fill="none" stroke="#2a3a4a" stroke-width="{rnd.choice([2,3,4])}"/>' for _ in range(16))
prob_css = '''
    #p-field { position: absolute; inset: 0; }
    .cx { position: absolute; padding: 18px 26px; display: flex; align-items: center; gap: 14px; font-size: 32px; color: #94999e; border-radius: 18px !important; }
    .cx svg { width: 30px; height: 30px; color: #f4b85a; }
    #p-word { position: absolute; left: 0; right: 0; top: 430px; height: 140px; }
    #p-word div { position: absolute; left: 0; right: 0; text-align: center; font-family: "Michroma", sans-serif; font-size: 120px; text-shadow: 0 0 40px #05080d, 0 0 14px #05080d; }
    #p-clock { position: absolute; left: 0; right: 0; top: 380px; text-align: center; }
    #p-clock .t { font: 600 190px "JetBrains Mono Variable", monospace; color: #e8edf1; text-shadow: 0 0 60px rgba(228,124,118,.35); }
    #p-clock .s { font-size: 40px; color: #94999e; margin-top: -10px; }
    #p-err { position: absolute; left: 1220px; top: 330px; }
    #p-err2 { position: absolute; left: 230px; top: 560px; }
    #p-beam { position: absolute; top: 0; bottom: 0; left: 1920px; width: 420px; background: linear-gradient(90deg, rgba(57,159,239,0), rgba(166,208,246,.95) 50%, rgba(57,159,239,0)); filter: blur(12px); }
    #p-flood { position: absolute; inset: 0; background: #399fef; }
'''
prob_body = f'''    <div id="p-field"><svg width="1920" height="1080" style="position:absolute;left:0;top:0">{cables}</svg>{cards}
      <div id="p-err">{pill("bad", "Algo salió mal")}</div><div id="p-err2">{pill("bad", "Servidor caído")}</div></div>
    <div id="p-word"><div id="p-w0" class="kin">Lento.</div><div id="p-w1" class="kin">Caro.</div><div id="p-w2" class="kin" style="color:#e47c76">Complicado.</div></div>
    <div id="p-clock"><div class="t"><span>03</span><span id="p-colon">:</span><span>12</span></div><div class="s">otra noche sin dormir</div></div>
    <div id="p-beam"></div><div id="p-flood"></div>'''
prob_js = '''
    tl.fromTo("#p-field", { scale: 0.86, opacity: 0 }, { scale: 1.12, opacity: 1, duration: 8.8, ease: "none" }, 0);
    tl.fromTo("#p-field", { rotation: -3.5 }, { rotation: 2.5, duration: 8.8, ease: "sine.inOut" }, 0);
    tl.fromTo("#p-field", { filter: "blur(6px)" }, { filter: "blur(0px)", duration: 1.0 }, 0);
    tl.fromTo(".cx", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.6, ease: "expo.out", stagger: 0.08 }, 0.2);
    tl.fromTo("#p-flood", { opacity: 0 }, { opacity: 0, duration: 0.01 }, 0);
    [["#p-w0", @@at("problem", "lanzar")@@], ["#p-w1", @@at("problem", "carrera")@@], ["#p-w2", @@at("problem", "obstaculos")@@]].forEach(([w, t], i) => {
      tl.fromTo(w, { opacity: 0, scale: 1.35, filter: "blur(14px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.25, ease: "expo.out" }, t);
      if (i < 2) tl.to(w, { opacity: 0, filter: "blur(10px)", duration: 0.15 }, t + 0.5);
    });
    tl.to("#p-w2", { opacity: 0, filter: "blur(10px)", duration: 0.25 }, @@at("problem", "servidores") - 0.2@@);
    // jargon piles up and fails
    tl.to(".cx", { color: "#d6dde3", duration: 0.3, stagger: 0.1 }, @@at("problem", "servidores")@@);
    tl.fromTo("#p-err", { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2.2)" }, @@at("problem", "configurar")@@);
    tl.fromTo("#p-err2", { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2.2)" }, @@at("problem", "cuentas")@@);
    tl.to("#p-field", { opacity: 0.25, duration: 0.5 }, @@at("problem", "noches") - 0.15@@);
    tl.fromTo("#p-clock", { opacity: 0, filter: "blur(14px)", scale: 1.08 }, { opacity: 1, filter: "blur(0px)", scale: 1, duration: 0.5, ease: "back.out(1.5)" }, @@at("problem", "noches")@@);
    [6.9, 7.5, 8.1].forEach((t) => { tl.set("#p-colon", { opacity: 0 }, t); tl.set("#p-colon", { opacity: 1 }, t + 0.3); });
    // a beam of light sweeps it all away
    tl.to("#p-beam", { x: -2500, duration: 0.7, ease: "power2.in" }, 8.1);
    tl.to("#p-clock", { opacity: 0, filter: "blur(10px)", duration: 0.3 }, 8.3);
    tl.to("#p-flood", { opacity: 1, duration: 0.3, ease: "power2.in" }, 8.5);'''
_ = (scene("problem", prob_css, prob_body, R(prob_js)))

# ── reveal: Evolut, your idea factory ────────────────────────────
pillars = [("Tú la imaginas", "M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7V17h8v-2.3A7 7 0 0 0 12 2z", "#f0b965"),
           ("La construimos", "M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z", "#66b8ff"),
           ("La cuidamos", "M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10zM9 12l2 2 4-4", "#5ed19d"),
           ("La hacemos crecer", "M22 7l-8.5 8.5-5-5L2 17M16 7h6v6", "#e48ab3")]
pcards = ''.join(f'''<div class="pc glass" id="r-p{i}" style="left:{150 + i*415}px;--accent:{c}"><div class="pc-depth" aria-hidden="true"></div><i class="pc-sheen" id="r-sheen{i}" aria-hidden="true"></i><div class="pi" style="color:{c};box-shadow:0 0 40px {c}55, inset 0 0 0 2px {c}66"><svg viewBox="0 0 24 24" class="icon"><path d="{d}"/></svg></div><div class="pt">{t}</div></div>''' for i, (t, d, c) in enumerate(pillars))
rev_css = '''
    #r-flood { position: absolute; inset: 0; background: radial-gradient(circle at 50% 50%, #ffffff 0%, #a6d0f6 20%, #399fef 52%, #12406a 100%); }
    #r-flare { position: absolute; left: -400px; top: 418px; width: 2720px; height: 8px; background: linear-gradient(90deg, rgba(102,184,255,0), rgba(214,236,255,.95) 50%, rgba(102,184,255,0)); filter: blur(3px); }
    #r-flare2 { position: absolute; left: 160px; top: 380px; width: 1600px; height: 90px; background: radial-gradient(closest-side, rgba(102,184,255,.35), rgba(102,184,255,0)); }
    #r-brand { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; }
    #r-scrim { position: absolute; left: 260px; top: 200px; width: 1400px; height: 520px; border-radius: 50%; background: radial-gradient(closest-side, rgba(7,12,16,.8), rgba(7,12,16,0)); }
    #r-logo { position: absolute; left: 510px; top: 340px; width: 900px; height: 129px; filter: drop-shadow(0 0 30px rgba(57,159,239,.55)); }
    #r-tag { position: absolute; left: 0; right: 0; top: 520px; text-align: center; font-size: 60px; }
    #r-tag b { color: #399fef; font-weight: 400; }
    .pc { position: absolute; top: 560px; width: 380px; height: 300px; padding: 40px 34px; display: flex; flex-direction: column; gap: 28px; isolation: isolate; transform-style: preserve-3d; border: 1px solid rgba(255,255,255,.12); }
    .pc-depth { position: absolute; z-index: 0; inset: 8px -5px -18px 5px; border-radius: inherit; background: linear-gradient(145deg, color-mix(in srgb, var(--accent) 24%, #112131), #05090e 60%); box-shadow: 0 34px 76px rgba(0,0,0,.62), inset 0 1px 0 rgba(255,255,255,.12); transform: translateZ(-26px); pointer-events: none; }
    .pc-sheen { position: absolute; z-index: 2; inset: 1px; overflow: hidden; border-radius: inherit; opacity: 0; pointer-events: none; background: linear-gradient(112deg, transparent 18%, rgba(255,255,255,.2) 48%, rgba(166,208,246,.12) 54%, transparent 72%); transform: translateX(-140%) skewX(-16deg); }
    .pc > .pi, .pc > .pt { position: relative; z-index: 3; }
    .pi { width: 112px; height: 112px; border-radius: 28px; background: linear-gradient(145deg, rgba(24,37,49,.96), rgba(5,9,14,.96)); display: flex; align-items: center; justify-content: center; transform: translateZ(34px); box-shadow: inset 0 2px 0 rgba(255,255,255,.16), inset 0 0 0 1px rgba(255,255,255,.08), 0 14px 26px rgba(0,0,0,.46); }
    .rorb { position: absolute; left: 930px; top: 516px; width: 60px; height: 60px; border-radius: 50%; background: radial-gradient(circle, #ffffff, #a6d0f6 35%, rgba(57,159,239,.5) 60%, rgba(57,159,239,0) 72%); box-shadow: 0 0 60px #66b8ff; opacity: 0; }
    .pi svg { width: 58px; height: 58px; stroke-width: 1.8; filter: drop-shadow(0 0 7px currentColor); }
    .pt { font-size: 40px; font-weight: 600; text-shadow: 0 2px 12px rgba(0,0,0,.58); transform: translateZ(18px); }
'''
rev_body = f'''    <div id="r-brand"><div id="r-scrim"></div><div id="r-flare2"></div>
      <img id="r-logo" src="assets/evolut-isologo-on-dark.svg" alt="Evolut" />
      <div id="r-tag" class="kin">Tu <b>fábrica de ideas.</b></div></div>
    {pcards}
    <div id="r-flare"></div>
    <div id="r-orb" class="rorb"></div>
    <div id="r-flood"></div>'''
rev_js = '''
    tl.fromTo("#r-flood", { opacity: 1, scale: 1 }, { opacity: 0, scale: 1.6, duration: 1.1, ease: "power2.out" }, 0);
    tl.fromTo("#r-flare", { scaleX: 0.1, opacity: 0 }, { keyframes: [{ scaleX: 1, opacity: 1, duration: 0.5, ease: "expo.out" }, { opacity: 0, duration: 1.0, ease: "power2.in" }] }, 0.5);
    tl.fromTo("#r-flare2", { opacity: 0 }, { keyframes: [{ opacity: 1, duration: 0.6 }, { opacity: 0.4, duration: 1.4 }] }, 0.5);
    tl.fromTo("#r-scrim", { opacity: 0 }, { opacity: 1, duration: 0.8 }, 0.4);
    tl.fromTo("#r-brand", { scale: 1.6 }, { scale: 1, duration: 1.2, ease: SPRING }, @@at("reveal", "evolut") - 0.2@@);
    tl.fromTo("#r-logo", { clipPath: "inset(0 100% 0 0)", opacity: 1 }, { clipPath: "inset(0 0% 0 0)", duration: 0.9, ease: "expo.out" }, @@at("reveal", "evolut") - 0.1@@);
    tl.fromTo("#r-tag", { opacity: 0, filter: "blur(10px)", y: 14 }, { opacity: 1, filter: "blur(0px)", y: 0, duration: 0.5, ease: "back.out(1.6)" }, @@at("reveal", "idea") - 0.9@@);
    // a restrained camera dolly follows the promise cards, then releases into the next scene
    tl.fromTo("#root", { scale: 1, x: 0, y: 0 }, { scale: 1.055, x: -20, y: 8, duration: 8.8, ease: "power2.inOut" }, 0);
    tl.to("#root", { scale: 1, x: 0, y: 0, duration: 0.35, ease: "power3.in" }, 9.3);
    // the brand rises; the four promises arrive with the voice
    tl.to("#r-brand", { y: -150, scale: 0.72, transformOrigin: "50% 30%", duration: 0.8, ease: "power3.inOut" }, @@at("reveal", "idea") - 0.5@@);
    [@@at("reveal", "idea")@@, @@at("reveal", "construirla")@@, @@at("reveal", "protegerla")@@, @@at("reveal", "crecer")@@].forEach((t, i) => {
      const tilt = [-7, -3, 3, 7][i];
      tl.fromTo(`#r-p${i}`, { opacity: 0, y: 100, z: -36, rotationX: 20, rotationY: tilt, transformPerspective: 1500, filter: "blur(10px)" }, { opacity: 1, y: 0, z: 0, rotationX: 0, rotationY: 0, filter: "blur(0px)", duration: 0.82, ease: "back.out(1.5)" }, t);
      tl.fromTo(`#r-p${i} .pi`, { scale: 0.58, rotationY: -28, rotationZ: -12 }, { scale: 1, rotationY: 0, rotationZ: 0, duration: 0.58, ease: "back.out(1.8)" }, t + 0.28);
      tl.fromTo(`#r-sheen${i}`, { xPercent: -145, opacity: 0 }, { keyframes: [{ opacity: 0.72, duration: 0.12 }, { xPercent: 145, opacity: 0, duration: 0.92, ease: "power1.inOut" }] }, t + 0.72);
      tl.fromTo(`#r-p${i}`, { y: 0, rotationZ: 0 }, { y: -12, rotationZ: i % 2 ? -0.7 : 0.7, duration: 1.25, ease: "sine.inOut", yoyo: true, repeat: 2 }, t + 0.9);
    });
    tl.fromTo("#r-logo", { x: 0 }, { x: -10, duration: 6, ease: "sine.inOut" }, 1.5);
    // dive into the factory
    tl.to("#r-brand", { opacity: 0, filter: "blur(10px)", duration: 0.35, ease: "power2.in" }, 9.3);
    [0, 1, 2, 3].forEach((i) => tl.to(`#r-p${i}`, { x: 960 - (150 + i * 415 + 190), y: -170, scale: 0.12, opacity: 0, duration: 0.5, ease: "power3.in" }, 9.3 + i * 0.03));
    tl.fromTo("#r-orb", { opacity: 0, scale: 0.2 }, { keyframes: [{ opacity: 1, scale: 1, duration: 0.25, ease: "power2.out" }, { scale: 3, duration: 0.3, ease: "power2.in" }] }, 9.65);'''
open(OUT + "reveal.html", "w").write(scene("reveal", rev_css, rev_body, R(rev_js)))
print("open scenes written")
