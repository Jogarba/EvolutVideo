import sys, math, random; sys.path.insert(0, sys.path[0])
from common import *
rnd = random.Random(5)
L = 6.4          # each station's slot; hosts run 0.6 s longer so pushes overlap
OUTT = L - 0.3

def write(cid, css, hero, js, n, label, h1, h2, sub):
    body = f'''    <div class="world" id="world">
{station(n, label, h1, h2, sub)}
      <div class="hero" id="hero">{hero}</div>
    </div>'''
    open(OUT + cid + ".html", "w").write(scene(cid, STATION_CSS + css, body, STATION_IN + js + station_out(OUTT)))

# ── outcome: you sell, we handle the rest ─────────────────────────
orders = [("LM", "Laura M.", "Café de origen ×2", "#e48ab3"), ("AR", "Andrés R.", "Capuchino + croissant", "#67b1f2"), ("SP", "Sofía P.", "Té chai ×3", "#f0b965"), ("JC", "Julián C.", "Café de origen", "#75dcab")]
toasts = ''.join(f'<div class="ord glass" id="o-t{i}"><i style="background:{c}">{ini}</i><div><b>Nuevo pedido</b><span>{n} · {item}</span></div><em>ahora</em></div>' for i, (ini, n, item, c) in enumerate(orders))
out_css = '''
    #o-h { position: absolute; left: 0; right: 0; top: 190px; text-align: center; white-space: nowrap; font-family: "Michroma", sans-serif; font-size: 70px; text-shadow: 0 0 30px #070c10, 0 0 12px #070c10; }
    #o-h b { color: #399fef; font-weight: 400; }
    #o-h span, #o-h b { display: inline-block; }
    #o-sub { position: absolute; left: 150px; top: 560px; font-size: 38px; color: #d6dde3; text-shadow: 0 0 18px #070c10; }
    #o-stack { position: absolute; left: 610px; top: 320px; width: 700px; height: 600px; }
    .ord { position: absolute; left: 0; width: 700px; height: 118px; padding: 0 28px; display: flex; align-items: center; gap: 20px; border-radius: 26px !important; }
    .ord i { width: 66px; height: 66px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-style: normal; font-weight: 700; font-size: 26px; color: #05080d; }
    .ord b { display: block; font-size: 32px; } .ord span { font-size: 26px; color: #bfc3c7; }
    .ord em { margin-left: auto; font-style: normal; font-size: 24px; color: #5ed19d; }
    #ocam { position: absolute; inset: 0; transform-origin: 50% 55%; }
    #o-streak { position: absolute; left: 946px; top: -700px; width: 28px; height: 900px; border-radius: 14px; background: linear-gradient(180deg, #ffffff, #c9ffe6 30%, rgba(126,240,184,0)); filter: blur(3px); opacity: 0; }
    #o-orb { position: absolute; left: 930px; top: 540px; width: 60px; height: 60px; border-radius: 50%; background: radial-gradient(circle, #ffffff, #a6d0f6 35%, rgba(57,159,239,.5) 60%, rgba(57,159,239,0) 72%); box-shadow: 0 0 60px #66b8ff; opacity: 0; }
    #o-glow { position: absolute; left: 510px; top: 220px; width: 900px; height: 760px; border-radius: 50%; background: radial-gradient(closest-side, rgba(57,159,239,.25), rgba(57,159,239,0)); }
'''
out_body = f'''    <div class="world" id="world"><div id="ocam"><div id="o-glow"></div>
      <div id="o-h"><span id="o-h1">Tú dedícate</span> <b id="o-h2">a vender.</b></div>
      <div id="o-stack">{toasts}</div><div id="o-streak"></div></div><div id="o-orb"></div></div>'''
OT = [at('outcome', 'enfocas'), at('outcome', 'importa'), at('outcome', 'clientes'), at('outcome', 'ventas')]
out_js = '''
    tl.fromTo("#world", { opacity: 0 }, { opacity: 1, duration: 0.25 }, 0);
    tl.fromTo("#ocam", { y: -900 }, { y: 0, duration: 0.9, ease: SPRING }, 0);
    tl.fromTo("#ocam", { scale: 1 }, { scale: 1.05, duration: 4.3, ease: "sine.inOut" }, 0.9);
    tl.fromTo("#o-streak", { opacity: 0, y: -200 }, { keyframes: [{ opacity: 1, duration: 0.05 }, { y: 760, duration: 0.45, ease: "power3.in" }, { opacity: 0, duration: 0.15 }] }, 0);
    tl.fromTo("#o-h1", { opacity: 0, filter: "blur(10px)", y: 20 }, { opacity: 1, filter: "blur(0px)", y: 0, duration: 0.5, ease: "expo.out" }, 0.5);
    tl.fromTo("#o-h2", { opacity: 0, filter: "blur(10px)", y: 20 }, { opacity: 1, filter: "blur(0px)", y: 0, duration: 0.5, ease: "expo.out" }, 0.8);
    tl.fromTo("#o-glow", { opacity: 0 }, { opacity: 1, duration: 1.0 }, 0.4);
    // orders keep arriving: each new one lands on top and pushes the rest down
    [0, 1, 2, 3].forEach((i) => {
      const t = [@@OT@@][i];
      tl.fromTo(`#o-t${i}`, { y: -40, opacity: 0, scale: 0.94 }, { y: 0, opacity: 1, scale: 1, duration: 0.55, ease: "back.out(1.7)" }, t);
      for (let j = 0; j < i; j++) tl.to(`#o-t${j}`, { y: (i - j) * 136, opacity: 1 - (i - j) * 0.18, duration: 0.5, ease: "expo.out" }, t);
    });
    tl.fromTo("#o-stack", { y: 0 }, { y: -9, duration: 1.2, ease: "sine.inOut", yoyo: true, repeat: 3 }, 0.8);
    tl.fromTo("#o-h", { x: 0 }, { x: 12, duration: 5, ease: "sine.inOut" }, 0.3);
    tl.to("#ocam", { rotation: 360, scale: 0.1, duration: 0.6, ease: "power3.in" }, 5.2);
    tl.to("#o-stack", { scale: 0.05, y: 160, opacity: 0, duration: 0.45, ease: "power3.in" }, 5.25);
    tl.to(["#o-h", "#o-glow"], { opacity: 0, filter: "blur(8px)", duration: 0.3, ease: "power2.in" }, 5.25);
    tl.fromTo("#o-orb", { opacity: 0, scale: 0.2 }, { opacity: 1, scale: 1.5, duration: 0.3, ease: "power2.out" }, 5.55);'''
out_js = out_js.replace('@@OT@@', ', '.join(str(x) for x in OT))
open(OUT + "outcome.html", "w").write(scene("outcome", STATION_CSS + out_css, out_body, out_js))
print("stations written")
