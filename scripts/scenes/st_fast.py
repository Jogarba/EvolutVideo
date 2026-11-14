import sys, math, random; sys.path.insert(0, sys.path[0])
from st_common import *
rnd = random.Random(5)
# Station 01: you press "Publicar" in Evolut and the store's website is live on the monitor.
products = [("Café de origen", "$9.900", "#c98b5a", "#6b3f22"), ("Capuchino", "$7.500", "#e8c49a", "#a8724a"), ("Croissant", "$6.200", "#f0b965", "#b9762e"), ("Té chai", "$8.000", "#d99a6c", "#7d4a2a")]
prods = ''.join(f'<div class="wp"><div class="wpi" style="background:radial-gradient(circle at 35% 30%, {a}, {b})"><i></i></div><b>{n}</b><span>{p}</span><em>Añadir</em></div>' for n, p, a, b in products)
steps = [("Diseño listo", 1.75), ("Tienda creada", 2.1), ("Publicada en internet", 2.45)]
psteps = ''.join(f'<div class="ps" id="f-s{i}"><i id="f-si{i}">{ICON["ok"]}</i>{t}</div>' for i, (t, _) in enumerate(steps))
confetti = ''.join(f'<i class="cf" id="f-cf{i}" style="background:{rnd.choice(["#399fef","#5ed19d","#f0b965","#e48ab3","#a6d0f6"])}"></i>' for i in range(28))
cf_js = '\n    '.join(f'tl.fromTo("#f-cf{i}", {{ x: 0, y: 0, rotation: 0, opacity: 0 }}, {{ keyframes: [{{ opacity: 1, duration: 0.05 }}, {{ x: {math.cos(a)*r:.0f}, y: {math.sin(a)*r*0.7 - 40:.0f}, rotation: {rnd.randint(-300,300)}, duration: 0.9, ease: "power3.out" }}, {{ y: "+=90", opacity: 0, duration: 0.7, ease: "power1.in" }}] }}, 2.95);'
                     for i, (a, r) in enumerate((rnd.uniform(0, 2*math.pi), rnd.uniform(140, 300)) for _ in range(28)))
css = '''
    #sp-dim { }
    #sp-orb { left: 430px; top: 300px; }
    #sp-name { left: 135px; top: 230px; width: 590px; height: 140px; padding: 24px 34px; }
    #sp-name label { display: block; font-size: 24px; color: #94999e; }
    #sp-name .v { margin-top: 10px; font: 600 46px "JetBrains Mono Variable", monospace; display: flex; align-items: center; }
    #sp-typed { display: inline-block; overflow: hidden; white-space: nowrap; }
    #sp-caret { width: 4px; height: 50px; background: #66b8ff; margin-left: 6px; }
    #sp-btn { left: 230px; top: 410px; width: 400px; height: 116px; border-radius: 999px; background: linear-gradient(180deg, #5cb3f7, #2b8fe0); color: #000e1d; font-size: 44px; font-weight: 800; display: flex; align-items: center; justify-content: center; gap: 16px; overflow: hidden; box-shadow: 0 0 0 2px rgba(214,236,255,.9), 0 0 70px rgba(57,159,239,.8), 0 50px 110px rgba(0,0,0,.75); }
    #sp-btn svg { width: 44px; height: 44px; }
    #sp-ring { position: absolute; left: 330px; top: 368px; width: 200px; height: 200px; border-radius: 50%; border: 4px solid #a6d0f6; opacity: 0; }
    #sp-beam { position: absolute; left: 418px; top: -220px; width: 24px; height: 700px; border-radius: 12px; background: linear-gradient(180deg, rgba(166,208,246,0), #e6f3ff 60%, rgba(166,208,246,0)); filter: blur(4px); opacity: 0; }
    #sp-order { left: 155px; top: 230px; width: 550px; height: 150px; padding: 0 30px; display: flex; align-items: center; gap: 22px; }
    #sp-order i { width: 84px; height: 84px; border-radius: 24px; background: #5ed19d; display: flex; align-items: center; justify-content: center; color: #04120b; flex: none; }
    #sp-order svg { width: 50px; height: 50px; } #sp-order b { display: block; font-size: 38px; } #sp-order span { font-size: 28px; color: #bfc3c7; }
    #sp-pkt { position: absolute; left: 330px; top: 285px; width: 200px; height: 56px; border-radius: 99px; background: linear-gradient(90deg, rgba(94,209,157,0), #9be8c4 40%, #ffffff); box-shadow: 0 0 40px #5ed19d; opacity: 0; }

    #f-glow { left: 40px; top: 30px; width: 800px; height: 600px; background: radial-gradient(closest-side, rgba(57,159,239,.30), rgba(57,159,239,0)); }
    #f-mon { position: absolute; left: 40px; top: 30px; width: 780px; height: 470px; border-radius: 26px; padding: 16px; background: linear-gradient(160deg, #3f4b59, #141a21 35%, #0a0e13 70%, #2c3540); box-shadow: 0 50px 110px rgba(0,0,0,.6), inset 0 0 0 2px #5a6878; }
    #f-scr { position: relative; width: 100%; height: 100%; border-radius: 12px; overflow: hidden; background: #0b1016; }
    #f-cam { position: absolute; left: 50%; top: 5px; width: 6px; height: 6px; margin-left: -3px; border-radius: 50%; background: #1d2630; }
    #f-neck { position: absolute; left: 375px; top: 500px; width: 110px; height: 88px; background: linear-gradient(90deg, #1b232c, #46525f 50%, #1b232c); clip-path: polygon(18% 0, 82% 0, 100% 100%, 0 100%); }
    #f-base { position: absolute; left: 270px; top: 584px; width: 320px; height: 22px; border-radius: 50%; background: linear-gradient(180deg, #4b5866, #151b22); box-shadow: 0 16px 30px rgba(0,0,0,.5); }
    #f-wipe { position: absolute; left: 0; right: 0; top: 0; height: 40px; background: linear-gradient(180deg, rgba(166,208,246,0), rgba(214,236,255,.9), rgba(166,208,246,0)); z-index: 8; opacity: 0; }
    #f-sheen { position: absolute; inset: 0; background: linear-gradient(118deg, rgba(255,255,255,.12), rgba(255,255,255,0) 30%); pointer-events: none; z-index: 9; }
    /* phase 1: the Evolut panel */
    #f-app { position: absolute; inset: 0; display: flex; }
    #f-side { width: 64px; background: #0e1318; display: flex; flex-direction: column; align-items: center; gap: 18px; padding-top: 22px; }
    #f-side i { width: 30px; height: 30px; border-radius: 9px; background: #1e2833; display: block; } #f-side i:first-child { background: #399fef; }
    #f-form { margin: 34px auto 0; width: 470px; padding: 26px 30px; border-radius: 18px; background: #121a22; box-shadow: inset 0 0 0 1px rgba(242,245,247,.08); }
    #f-form h5 { font-size: 26px; font-weight: 600; } #f-form label { display: block; font-size: 16px; color: #94999e; margin: 16px 0 6px; }
    .fi { height: 44px; border-radius: 99px; padding: 0 18px; display: flex; align-items: center; font: 500 19px "JetBrains Mono Variable", monospace; background: #0b1016; box-shadow: inset 0 0 0 1px rgba(242,245,247,.14); }
    #f-typed { overflow: hidden; white-space: nowrap; display: inline-block; }
    .tpl { display: flex; gap: 10px; } .tpl span { flex: 1; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 17px; background: #0b1016; color: #bfc3c7; box-shadow: inset 0 0 0 1px rgba(242,245,247,.1); }
    #f-tpl0 { box-shadow: inset 0 0 0 2px #399fef !important; color: #f2f5f7 !important; }
    #f-pubbtn { margin-top: 20px; height: 50px; border-radius: 12px; background: #399fef; color: #000e1d; font-weight: 700; font-size: 20px; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; }
    /* phase 2: progress */
    #f-prog { position: absolute; inset: 0; background: #0b1016; display: flex; flex-direction: column; justify-content: center; padding: 0 140px; gap: 16px; }
    #f-prog h5 { font-size: 26px; font-weight: 600; margin-bottom: 6px; }
    #f-bar { height: 10px; border-radius: 99px; background: #1e2833; overflow: hidden; margin-bottom: 8px; } #f-barf { height: 100%; background: linear-gradient(90deg, #399fef, #5ed19d); transform-origin: left; }
    .ps { display: flex; align-items: center; gap: 12px; font-size: 21px; color: #bfc3c7; } .ps i { width: 26px; height: 26px; color: #5ed19d; }
    /* phase 3: the live website */
    #f-web { position: absolute; inset: 0; background: #f7f3ee; color: #2b1d14; }
    #f-chrome { height: 38px; background: #e9e2da; display: flex; align-items: center; gap: 8px; padding: 0 14px; }
    #f-chrome .d { width: 11px; height: 11px; border-radius: 50%; } #f-url { margin-left: 18px; flex: 1; height: 24px; border-radius: 99px; background: #fff; font: 500 14px "JetBrains Mono Variable", monospace; display: flex; align-items: center; padding: 0 12px; color: #5c4a3c; gap: 6px; }
    #f-url svg { width: 13px; height: 13px; color: #2a7a57; }
    #f-nav { display: flex; align-items: center; gap: 24px; padding: 12px 26px; font-size: 15px; color: #6e5545; } #f-nav b { font-size: 20px; color: #2b1d14; margin-right: auto; display: flex; align-items: center; gap: 10px; }
    #f-nav b i { width: 26px; height: 26px; border-radius: 8px; background: linear-gradient(135deg, #6b3f22, #c98b5a); display: block; }
    #f-cart { position: relative; padding: 6px 12px; border-radius: 99px; background: #2b1d14; color: #fff; } #f-badge { position: absolute; right: -6px; top: -6px; width: 20px; height: 20px; border-radius: 50%; background: #e4572e; color: #fff; font-size: 12px; display: flex; align-items: center; justify-content: center; }
    #f-heroweb { margin: 4px 22px; height: 150px; border-radius: 16px; background: linear-gradient(120deg, #3a2316, #8a5532); position: relative; padding: 22px 26px; color: #fff7ee; }
    #f-heroweb b { font-size: 30px; display: block; } #f-heroweb span { font-size: 15px; opacity: .85; } #f-heroweb em { display: inline-block; margin-top: 12px; font-style: normal; font-size: 15px; padding: 7px 16px; border-radius: 99px; background: #f0b965; color: #2b1d14; font-weight: 700; }
    .cup { position: absolute; right: 30px; top: 18px; width: 116px; height: 116px; border-radius: 50%; background: radial-gradient(circle at 40% 35%, #f3d7b4, #c98b5a 45%, #6b3f22 75%); box-shadow: 0 10px 30px rgba(0,0,0,.35); }
    #f-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; padding: 12px 22px; }
    .wp { background: #fff; border-radius: 14px; padding: 9px; box-shadow: 0 4px 12px rgba(60,30,10,.08); font-size: 13px; }
    .wpi { height: 66px; border-radius: 10px; position: relative; } .wpi i { position: absolute; left: 50%; top: 50%; width: 30px; height: 30px; margin: -15px; border-radius: 50%; background: rgba(255,255,255,.35); display: block; }
    .wp b { display: block; margin-top: 6px; font-size: 13px; } .wp span { color: #8a6a55; } .wp em { float: right; font-style: normal; font-size: 11px; padding: 2px 8px; border-radius: 99px; background: #2b1d14; color: #fff; }
    #f-order { position: absolute; right: 16px; top: 92px; padding: 10px 14px; border-radius: 14px; background: #2b1d14; color: #fff7ee; display: flex; align-items: center; gap: 10px; font-size: 14px; box-shadow: 0 10px 24px rgba(0,0,0,.3); z-index: 6; }
    #f-order i { width: 26px; height: 26px; border-radius: 8px; background: #5ed19d; display: flex; align-items: center; justify-content: center; color: #04120b; }
    #f-order svg { width: 18px; height: 18px; } #f-order b { font-size: 15px; }
    .cf { position: absolute; left: 430px; top: 250px; width: 12px; height: 18px; border-radius: 3px; opacity: 0; z-index: 10; }
    #f-live { position: absolute; left: 640px; top: 0; z-index: 11; }
    #f-steps { position: absolute; left: 60px; top: 650px; width: 740px; display: flex; justify-content: space-between; }
    .stp { display: flex; align-items: center; gap: 12px; font-size: 28px; color: #6c737a; }
    .stp b { width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font: 700 22px "JetBrains Mono Variable", monospace; background: #1e2833; color: #94999e; }
'''
hero = f'''<div class="glow" id="f-glow"></div>
        <div id="f-neck"></div><div id="f-base"></div>
        <div id="f-mon"><div id="f-scr"><div id="f-cam"></div>
          <div id="f-app"><div id="f-side"><i></i><i></i><i></i><i></i></div>
            <div id="f-form" data-layout-allow-overlap><h5>Nueva app</h5><label>Nombre</label><div class="fi"><span id="f-typed">Aroma Café</span></div>
              <label>Tipo</label><div class="tpl"><span id="f-tpl0">Tienda</span><span>Reservas</span><span>Portafolio</span></div>
              <div id="f-pubbtn">Publicar<span class="shine" id="f-shine"></span></div></div></div>
          <div id="f-prog" data-layout-allow-overlap><h5>Publicando Aroma Café…</h5><div id="f-bar"><div id="f-barf"></div></div>{psteps}</div>
          <div id="f-web" data-layout-allow-overlap><div id="f-chrome"><i class="d" style="background:#e47c76"></i><i class="d" style="background:#f4b85a"></i><i class="d" style="background:#5ed19d"></i><div id="f-url">{ICON["lock"]}aromacafe.evolut.cloud</div></div>
            <div id="f-nav"><b><i></i>Aroma Café</b><span>Menú</span><span>Pedidos</span><span>Nosotros</span><span id="f-cart">Carrito<i id="f-badge">1</i></span></div>
            <div id="f-heroweb"><b>Café recién tostado</b><span>Pide en línea y recoge en minutos</span><br><em>Pedir ahora</em><div class="cup"></div></div>
            <div id="f-grid">{prods}</div>
            <div id="f-order"><i>{ICON["ok"]}</i><span><b>Nuevo pedido</b><br>Café de origen ×2</span></div></div>
          <div id="f-wipe"></div><div id="f-sheen"></div></div></div>
        {confetti}
        <div id="f-live">{pill("ok", "¡En línea!")}</div>

        <div class="dim" id="sp-dim"></div>
        <div class="orb" id="sp-orb"></div>
        <div class="spot" id="sp-name"><label>Nombre de tu negocio</label><div class="v"><span id="sp-typed">Aroma Café</span><i id="sp-caret"></i></div></div>
        <div class="spot" id="sp-btn"><svg viewBox="0 0 24 24" class="icon" style="stroke-width:2.4"><path d="M4.5 16.5c-1.5 1.3-2 5-2 5s3.7-.5 5-2c.7-.8.7-2.1-.1-2.9a2.2 2.2 0 0 0-2.9-.1zM12 15l-3-3a22 22 0 0 1 2-3.9A12.9 12.9 0 0 1 22 2c0 2.7-.8 7.5-6 11a22.4 22.4 0 0 1-4 2z"/></svg>Publicar</div>
        <div id="sp-ring"></div><div id="sp-beam"></div>
        <div class="spot" id="sp-order"><i>{ICON["ok"]}</i><div><b>¡Nuevo pedido!</b><span>Café de origen ×2 · ahora</span></div></div>
        <div id="sp-pkt"></div>
        <div class="cursor" id="f-cursor">{CURSOR}</div>
        <div id="f-steps"><div class="stp" id="f-st0"><b>1</b>Crea</div><div class="stp" id="f-st1"><b>2</b>Publica</div><div class="stp" id="f-st2"><b>3</b>¡Vende!</div></div>'''
N, P, I, D = at("fast", "nombre"), at("fast", "publicar"), at("fast", "internet"), at("fast", "pedidos")
cf_js = cf_js.replace("}, 2.95);", f"}}, {I + 0.25});")
js = f'''
    // spotlight 1 — the orb from the reveal opens into one floating field: the business name
    ["#f-mon", "#f-neck", "#f-base", "#f-glow", "#f-web", "#f-live", "#f-order", "#sp-btn", "#sp-order", "#f-app"].forEach((s) => tl.fromTo(s, {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0));
    tl.fromTo("#sp-orb", {{ scale: 3, opacity: 1 }}, {{ scale: 0.2, opacity: 0, duration: 0.5, ease: "power3.in" }}, 0);
    tl.fromTo("#sp-dim", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.6 }}, 0.1);
    tl.fromTo("#sp-name", {{ opacity: 0, scale: 0.3, filter: "blur(10px)" }}, {{ opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.75, ease: "back.out(1.4)" }}, 0.25);
    tl.fromTo(".stp", {{ opacity: 0, y: 24 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "back.out(1.6)", stagger: 0.12 }}, 0.6);
    const lit = (i, t) => {{ tl.to(`#f-st${{i}}`, {{ color: "#f2f5f7", duration: 0.2 }}, t); tl.fromTo(`#f-st${{i}} b`, {{ scale: 1 }}, {{ backgroundColor: "#399fef", color: "#000e1d", scale: 1.2, duration: 0.2, yoyo: true, repeat: 1 }}, t); }};
    lit(0, {N});
    tl.fromTo("#sp-typed", {{ width: 0 }}, {{ width: 270, duration: 0.55, ease: "steps(10)" }}, {N});
    [{N} - 0.3, {N} + 0.7, {N} + 1.1].forEach((t) => {{ tl.set("#sp-caret", {{ opacity: 0 }}, t); tl.set("#sp-caret", {{ opacity: 1 }}, t + 0.2); }});
    // spotlight 2 — the field steps back, the Publicar button floats in alone
    tl.to("#sp-name", {{ y: -150, scale: 0.72, opacity: 0.45, duration: 0.6, ease: "back.out(1.3)" }}, {P - 0.95});
    tl.fromTo("#sp-btn", {{ opacity: 0, scale: 0.5, y: 40 }}, {{ opacity: 1, scale: 1, y: -60, duration: 0.7, ease: "back.out(1.5)" }}, {P - 0.85});
    tl.fromTo("#f-cursor", {{ x: 980, y: 760 }}, {{ x: 470, y: 400, duration: 0.55, ease: "back.out(1.2)" }}, {P - 0.6});
    tl.to("#f-cursor", {{ scale: 0.8, duration: 0.07 }}, {P}); tl.to("#sp-btn", {{ scale: 0.92, duration: 0.07 }}, {P});
    lit(1, {P});
    // the click becomes a beam of light that switches the monitor on (match cut inside the scene)
    tl.fromTo("#sp-ring", {{ scale: 0.4, opacity: 0.9 }}, {{ scale: 2.2, opacity: 0, duration: 0.5, ease: "power2.out", immediateRender: false }}, {P + 0.05});
    tl.to("#sp-btn", {{ scaleX: 0.15, scaleY: 0.15, opacity: 0, duration: 0.25, ease: "power3.in" }}, {P + 0.07});
    tl.fromTo("#sp-beam", {{ opacity: 0, scaleY: 0.1 }}, {{ keyframes: [{{ opacity: 1, scaleY: 1, duration: 0.18, ease: "power2.out" }}, {{ opacity: 0, duration: 0.25 }}] }}, {P + 0.15});
    tl.to(["#sp-name", "#f-cursor"], {{ opacity: 0, duration: 0.2 }}, {P + 0.15});
    tl.to("#sp-dim", {{ opacity: 0, duration: 0.4 }}, {P + 0.2});
    tl.to(["#f-mon", "#f-neck", "#f-base", "#f-glow"], {{ opacity: 1, duration: 0.01 }}, {P + 0.25});
    tl.fromTo("#f-mon", {{ scale: 0.25, filter: "blur(12px)" }}, {{ scale: 1, filter: "blur(0px)", duration: 0.75, ease: "back.out(1.35)" }}, {P + 0.25});
    tl.fromTo(["#f-neck", "#f-base"], {{ y: 60 }}, {{ y: 0, duration: 0.6, ease: "back.out(1.5)", stagger: 0.06 }}, {P + 0.4});
    tl.set("#f-prog", {{ opacity: 1 }}, {P + 0.25});
    tl.fromTo("#f-barf", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {I - P - 0.6:.2f}, ease: "power1.inOut" }}, {P + 0.5});
    tl.fromTo(".ps", {{ opacity: 0.35 }}, {{ opacity: 0.35, duration: 0.01 }}, 0);
    [0, 1, 2].forEach((i) => {{ const t = {P + 0.6} + i * {(I - P - 0.8) / 3:.3f}; tl.to(`#f-s${{i}}`, {{ opacity: 1, duration: 0.15 }}, t); tl.fromTo(`#f-si${{i}}`, {{ scale: 0.3 }}, {{ scale: 1, duration: 0.35, ease: "back.out(2.2)" }}, t); }});
    // "internet": the website arrives, live
    tl.fromTo("#f-web", {{ opacity: 0, y: -24 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "back.out(1.3)", immediateRender: false }}, {I - 0.05});
    tl.fromTo("#f-wipe", {{ y: -60, opacity: 0 }}, {{ keyframes: [{{ opacity: 1, duration: 0.05 }}, {{ y: 470, duration: 0.55, ease: "power2.inOut" }}, {{ opacity: 0, duration: 0.1 }}] }}, {I - 0.1});
    tl.fromTo(["#f-nav", "#f-heroweb", ".wp"], {{ opacity: 0, y: 16 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "back.out(1.6)", stagger: 0.07 }}, {I + 0.2});
    tl.fromTo("#f-live", {{ opacity: 0, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: 0.45, ease: "back.out(2)" }}, {I + 0.25});
    // spotlight 3 — "pedidos": the order leaps out of the cart and floats alone in front
    lit(2, {D});
    tl.fromTo("#f-badge", {{ scale: 0 }}, {{ scale: 1, duration: 0.4, ease: "back.out(3)" }}, {D});
    tl.to("#sp-dim", {{ opacity: 1, duration: 0.4 }}, {D + 0.1});
    tl.to(["#f-mon", "#f-neck", "#f-base"], {{ opacity: 0.35, filter: "blur(4px)", duration: 0.4 }}, {D + 0.1});
    tl.fromTo("#sp-order", {{ opacity: 0, x: 210, y: -150, scale: 0.25 }}, {{ opacity: 1, x: 0, y: 0, scale: 1, duration: 0.75, ease: "back.out(1.45)" }}, {D + 0.1});
    ''' + cf_js

exit_js = f'''
    tl.to("#sp-order", {{ scaleX: 0.36, scaleY: 0.37, opacity: 0, duration: 0.25, ease: "power3.in" }}, {OUTT});
    tl.fromTo("#sp-pkt", {{ opacity: 0, x: 0 }}, {{ keyframes: [{{ opacity: 1, duration: 0.1 }}, {{ x: 1700, duration: 0.45, ease: "power3.in" }}] }}, {OUTT + 0.15});
    tl.to(["#st-chip", "#st-h", "#f-mon", "#f-neck", "#f-base", "#f-steps", "#st-pool", "#sp-dim"], {{ opacity: 0, filter: "blur(8px)", duration: 0.35, ease: "power2.in" }}, {OUTT + 0.15});'''
js = js + f'''
    // plunge: the camera dives at the Publicar button and brakes on the word
    aim(960, 635, {P - 0.95});
    kick({{ scale: 0.96 }}, {P - 0.72});
    rig({{ scale: 1.42, y: -110, rotationX: 7, transformPerspective: 1600 }}, {P - 0.72}, 0.75);
    // the click's shockwave ejects the camera back to reveal the monitor
    kick({{ scale: 1.5 }}, {P + 0.34});
    rig({{ scale: 0.94, y: 0, rotationX: 0 }}, {P + 0.34}, 0.85);
    aim(960, 560, {P + 1.25});
    // a short push toward the floating order
    rig({{ scale: 1.15, y: -30 }}, {D + 0.05}, 0.7);'''
exit_js = exit_js + f'''
    // target-locked: the camera chases the packet to the right
    tl.to("#cam", {{ x: -760, duration: 0.45, ease: "power3.in" }}, {OUTT + 0.15});'''
write("fast", css, hero, js, 1, "RAPIDEZ", "Lista en", "minutos.", exit_js=exit_js)
print("fast")
