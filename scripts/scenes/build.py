import sys; sys.path.insert(0, sys.path[0])
from common import *
css = '''
    #b-flood { position: absolute; inset: 0; background: #399fef; }
    #b-title { position: absolute; left: 0; right: 0; top: 330px; text-align: center; }
    #b-l1 { font-size: 78px; font-weight: 500; }
    #b-l2 { position: relative; height: 150px; margin-top: 22px; overflow: hidden; }
    #b-l2 > div { position: absolute; left: 0; right: 0; top: 0; text-align: center; font-size: 100px; line-height: 150px; white-space: nowrap; }
    #b-l2 em { font-style: normal; color: #399fef; }
    #b-cam { position: absolute; inset: 0; transform-origin: 1334px 926px; }
    #b-wiz { position: absolute; left: 330px; top: 110px; width: 1260px; height: 900px; }
    #b-wiz > * { position: absolute; }
    .tile { width: 80px; height: 80px; border-radius: 18px; background: #132636; color: #399fef; display: flex; align-items: center; justify-content: center; }
    .tile svg { width: 42px; height: 42px; }
    .lbl { font-size: 28px; color: #94999e; }
    .bar { width: 66px; height: 10px; border-radius: 99px; background: #303c48; overflow: hidden; }
    .bar i { display: block; height: 100%; background: #399fef; transform-origin: left; }
    .tcard { top: 244px; width: 368px; height: 150px; padding: 26px 30px; display: flex; gap: 22px; align-items: center; }
    .tcard svg { width: 46px; height: 46px; color: #bfc3c7; }
    .tcard b { display: block; font-size: 36px; font-weight: 600; }
    .tcard span { font-size: 28px; color: #94999e; }
    #b-web-sel { position: absolute; inset: 0; border-radius: 18px; background: rgba(57,159,239,.18); box-shadow: inset 6px 0 0 #399fef; }
    #b-field { left: 56px; top: 472px; width: 1148px; height: 88px; padding: 0 34px; display: flex; align-items: center; font: 500 38px "JetBrains Mono Variable", monospace; }
    #b-typed { display: inline-block; overflow: hidden; white-space: nowrap; }
    #b-caret { width: 4px; height: 44px; background: #399fef; margin-left: 4px; }
    #b-avail { margin-left: auto; }
    .xrow { top: 640px; width: 566px; height: 92px; padding: 0 28px; display: flex; align-items: center; gap: 18px; font-size: 32px; }
    .xrow svg.icon { width: 34px; height: 34px; color: #94999e; }
    .sw { margin-left: auto; width: 76px; height: 42px; border-radius: 99px; background: #303c48; position: relative; }
    .sw b { position: absolute; left: 5px; top: 5px; width: 32px; height: 32px; border-radius: 50%; background: #f2f5f7; }
    #b-btn { left: 804px; top: 772px; width: 400px; height: 88px; font-size: 34px; }

    #b-prog { position: absolute; left: 360px; top: 170px; width: 1200px; height: 740px; }
    #b-prog > * { position: absolute; }
    #b-ptrack { left: 56px; top: 150px; width: 1088px; height: 12px; border-radius: 99px; background: rgba(7,12,16,.8); overflow: hidden; }
    #b-pfill { position: absolute; inset: 0; background: linear-gradient(90deg, #399fef, #5ed19d); transform-origin: left; }
    .prow { left: 56px; width: 1088px; height: 88px; padding: 0 30px; display: flex; align-items: center; gap: 22px; font-size: 34px; }
    .prow .slot { position: relative; width: 40px; height: 40px; }
    .prow .slot svg { position: absolute; inset: 0; width: 40px; height: 40px; }
    .prow .sp { color: #399fef; } .prow .ck { color: #5ed19d; }
    .prow .t { margin-left: auto; font: 500 28px "JetBrains Mono Variable", monospace; color: #94999e; }
    #b-logwin { left: 56px; top: 612px; width: 1088px; height: 92px; overflow: hidden; padding: 0 30px; }
    #b-loglines { font: 500 28px/46px "JetBrains Mono Variable", monospace; color: #bfc3c7; white-space: nowrap; }
    #b-loglines i { font-style: normal; color: #399fef; }

    #b-web { position: absolute; left: 330px; top: 130px; width: 1260px; height: 680px; overflow: hidden; }
    #b-web > * { position: absolute; }
    .dot { width: 18px; height: 18px; border-radius: 50%; top: 30px; }
    #b-url { left: 150px; top: 14px; width: 760px; height: 52px; padding: 0 26px; display: flex; align-items: center; gap: 12px; font: 500 28px "JetBrains Mono Variable", monospace; }
    #b-url svg { width: 26px; height: 26px; color: #5ed19d; }
    #b-url b { color: #399fef; font-weight: 500; }
    #b-live { left: 950px; top: 14px; }
    #b-ping { left: 958px; top: 18px; width: 44px; height: 44px; border-radius: 50%; border: 3px solid #5ed19d; }
    .sk { border-radius: 14px; background: rgba(22,27,32,.92); }
    #b-site-nav { left: 40px; top: 110px; width: 1180px; height: 64px; display: flex; align-items: center; padding: 0 28px; gap: 30px; font-size: 26px; color: #bfc3c7; }
    #b-site-nav b { color: #f2f5f7; font-size: 30px; margin-right: auto; }
    #b-site-hero { left: 40px; top: 204px; width: 700px; }
    #b-site-hero h2 { font-size: 64px; line-height: 1.05; font-weight: 600; }
    #b-site-hero p { font-size: 30px; color: #bfc3c7; margin-top: 18px; }
    #b-site-cta { left: 40px; top: 470px; width: 300px; height: 76px; font-size: 30px; }
    #b-order { left: 790px; top: 196px; width: 430px; height: 350px; padding: 28px 30px; }
    #b-order b { font-size: 32px; font-weight: 600; display: block; }
    #b-order .eta { font-size: 26px; color: #5ed19d; margin-top: 4px; }
    .ost { display: flex; align-items: center; gap: 14px; font-size: 27px; color: #bfc3c7; margin-top: 16px; }
    .ost i { width: 18px; height: 18px; border-radius: 50%; background: #303c48; }
    .ost.done i { background: #5ed19d; } .ost.now i { background: #399fef; box-shadow: 0 0 14px #399fef; } .ost.now { color: #f2f5f7; }
    #b-otrack { position: absolute; left: 30px; right: 30px; bottom: 30px; height: 10px; border-radius: 99px; background: #303c48; }
    #b-ofill { position: absolute; inset: 0; border-radius: 99px; background: linear-gradient(90deg, #5ed19d, #399fef); transform-origin: left; }
    #b-otruck { position: absolute; left: -9px; top: -7px; width: 24px; height: 24px; border-radius: 50%; background: #f2f5f7; box-shadow: 0 0 16px #399fef; }
    .stile { top: 578px; width: 380px; height: 72px; display: flex; align-items: center; gap: 14px; padding: 0 24px; font-size: 27px; color: #bfc3c7; }
    .stile svg { width: 28px; height: 28px; color: #5ed19d; }
    #b-cap { position: absolute; left: 0; right: 0; top: 860px; text-align: center; font-size: 56px; }
'''
types = [('Web','Sitio o app web','globe'),('API','Servicio HTTP','server'),('Worker','Tareas de fondo','cog')]
tcards = ''.join(f'<div class="tcard raised" id="b-t{i}" style="left:{56+i*390}px">{"<div id=\"b-web-sel\"></div>" if i==0 else ""}{ICON[ic]}<div style="position:relative"><b>{n}</b><span>{d}</span></div></div>' for i,(n,d,ic) in enumerate(types))
rows = [("Repositorio creado en GitHub","0:02"),("Compilando imagen","0:41"),("Desplegando en dev","0:58"),("Iniciando réplicas…","1:06")]
prows = ''.join(f'<div class="prow raised" id="b-r{i}" style="top:{196+i*100}px"><span class="slot"><span class="sp" id="b-sp{i}">{ICON["spin"]}</span><span class="ck" id="b-ck{i}">{ICON["ok"]}</span></span>{l}<span class="t">{t}</span></div>' for i,(l,t) in enumerate(rows))
logs = ['<i>build</i>  Step 4/9 : RUN npm ci','<i>build</i>  Step 7/9 : RUN npm run build','<i>push</i>   portal-clientes:a41f2c3 → registro','<i>deploy</i> dev · 1 réplica programada','<i>deploy</i> dev · réplica lista ✓']
body = f'''    <div id="b-title">
      <div id="b-l1" class="halo">Con Evolut,</div>
      <div id="b-l2" class="kin"><div id="b-r1x" data-layout-allow-overlap>tu tienda <em>en línea.</em></div><div id="b-r2x" data-layout-allow-overlap>tu portal <em>en línea.</em></div><div id="b-r3x" data-layout-allow-overlap>tu app <em>en línea.</em></div></div>
    </div>
    <div id="b-cam">
      <div id="b-wiz" class="glass">
        <div class="tile" style="left:56px;top:48px">{ICON["rocket"]}</div>
        <div style="left:160px;top:44px;font-size:50px;font-weight:600">Nueva aplicación</div>
        <div class="lbl" style="left:160px;top:110px">Despliega código propio desde un repo de GitHub.</div>
        <div style="left:900px;top:76px;display:flex;gap:13px">{"".join(f'<div class="bar"><i id="b-bar{i}"></i></div>' for i in range(4))}</div>
        <div class="lbl" style="left:56px;top:200px">Tipo de aplicación</div>
        {tcards}
        <div class="lbl" style="left:56px;top:430px">Nombre</div>
        <div id="b-field" class="frost"><span id="b-typed">portal-clientes</span><span id="b-caret"></span><span id="b-avail">{pill("ok","disponible")}</span></div>
        <div class="lbl" style="left:56px;top:598px">Extras</div>
        <div class="xrow raised" style="left:56px">{ICON["db"]}Base de datos<div class="sw" id="b-sw1"><b id="b-sk1"></b></div></div>
        <div class="xrow raised" style="left:638px">{ICON["globe"]}Dominio propio<div class="sw" id="b-sw2"><b id="b-sk2"></b></div></div>
        <div class="lbl" style="left:56px;top:798px">Repositorio, pipeline y URL se crean solos.</div>
        <div id="b-btn" class="btn">Crear aplicación<span class="shine" id="b-shine"></span></div>
      </div>
    </div>
    <div id="b-prog" class="glass">
      <div style="left:56px;top:48px;font-size:46px;font-weight:600">Iniciando despliegue de tu app</div>
      <div style="left:56px;top:104px;font-size:28px" class="mono muted">portal-clientes · dev</div>
      <div id="b-ptrack"><i id="b-pfill"></i></div>
      {prows}
      <div id="b-logwin" class="well"><div id="b-loglines">{"".join(f"<div>{l}</div>" for l in logs)}</div></div>
    </div>
    <div id="b-web" class="glass">
      <div class="dot" style="left:36px;background:#e47c76"></div><div class="dot" style="left:66px;background:#f4b85a"></div><div class="dot" style="left:96px;background:#5ed19d"></div>
      <div id="b-url" class="frost">{ICON["lock"]}<span>https://<b>portal-clientes</b>.evolut.cloud</span></div>
      <div id="b-ping"></div>
      <span id="b-live" style="position:absolute">{pill("ok","En vivo")}</span>
      <div id="b-site-nav" class="sk"><b>Portal Clientes</b><span>Pedidos</span><span>Catálogo</span><span>Cuenta</span></div>
      <div id="b-site-hero"><h2>Tus pedidos, en un solo lugar.</h2><p>Consulta, paga y sigue cada envío.</p></div>
      <div id="b-site-cta" class="btn">Entrar</div>
      <div id="b-order" class="sk"><b>Pedido #1042</b><div class="eta">Llega mañana</div>
        <div class="ost done"><i></i>Confirmado</div><div class="ost now"><i></i>En camino</div><div class="ost"><i></i>Entregado</div>
        <div id="b-otrack"><i id="b-ofill"></i><i id="b-otruck"></i></div></div>
      <div class="stile sk" style="left:40px">{ICON["ok"]}Pagos al día</div><div class="stile sk" style="left:440px">{ICON["ok"]}Envíos rastreados</div><div class="stile sk" style="left:840px">{ICON["ok"]}Soporte siempre</div>
    </div>
    <div id="b-cap" class="kin">Lista para <span style="color:#399fef">tus clientes.</span></div>
    <div class="cursor" id="b-cursor">{CURSOR}</div>
    <div id="b-flood"></div>'''
js = '''
    tl.fromTo("#b-flood", { opacity: 1 }, { opacity: 0, duration: 0.5, ease: "power2.out" }, 0.02);
    // kinetic line over the open hall, slot roll on the noun
    tl.fromTo("#b-l1", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.2, ease: "power4.out" }, 0.1);
    tl.fromTo("#b-l2", { opacity: 0 }, { opacity: 1, duration: 0.15 }, 0.35);
    // each option holds long enough to read, then hands over with a short blur
    const OUT = { yPercent: -55, opacity: 0, filter: "blur(6px)", duration: 0.22, ease: "power2.in" };
    const FROM = { yPercent: 55, opacity: 0, filter: "blur(6px)" };
    const IN = { yPercent: 0, opacity: 1, filter: "blur(0px)", duration: 0.28, ease: "power3.out" };
    tl.fromTo("#b-r1x", { yPercent: 0, opacity: 1 }, OUT, 1.0);
    tl.fromTo("#b-r2x", FROM, IN, 1.12);
    tl.to("#b-r2x", OUT, 1.66);
    tl.fromTo("#b-r3x", FROM, IN, 1.78);
    tl.to("#b-title", { opacity: 0, filter: "blur(8px)", y: -30, duration: 0.2, ease: "power2.in" }, 2.45);

    // wizard: panes rise out of a slight blur one after another, like the console's .reveal
    tl.fromTo("#b-wiz", DEPTH, LAND, 2.35);
    tl.fromTo("#b-wiz > *", { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.45, ease: "expo.out", stagger: 0.022 }, 2.45);
    ["#b-bar0", "#b-bar1", "#b-bar2", "#b-bar3"].forEach((b, i) => tl.fromTo(b, { scaleX: 0 }, { scaleX: 1, duration: 0.3, ease: "power3.out" }, [2.9, 3.6, 3.95, 4.2][i]));
    tl.fromTo("#b-cursor", { x: 1900, y: 1150 }, { x: 556, y: 432, duration: 0.5, ease: "power3.out" }, 2.4);
    tl.to("#b-cursor", { scale: 0.82, duration: 0.07 }, 2.85);
    tl.to("#b-cursor", { scale: 1, duration: 0.1 }, 2.93);
    tl.fromTo("#b-web-sel", { opacity: 0 }, { opacity: 1, duration: 0.12 }, 2.88);
    tl.fromTo("#b-t0", { scale: 1 }, { scale: 0.97, duration: 0.07, yoyo: true, repeat: 1 }, 2.85);
    tl.fromTo("#b-typed", { width: 0 }, { width: 380, duration: 0.6, ease: "steps(15)" }, 3.0);
    tl.fromTo("#b-avail", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(1.7)" }, 3.62);
    [3.0, 3.75, 4.25].forEach((t) => { tl.set("#b-caret", { opacity: 0 }, t + 0.22); tl.set("#b-caret", { opacity: 1 }, t + 0.44); });
    tl.fromTo("#b-sw1", { backgroundColor: "#303c48" }, { backgroundColor: "#399fef", duration: 0.15 }, 3.92);
    tl.fromTo("#b-sk1", { x: 0 }, { x: 34, duration: 0.25, ease: "back.out(2)" }, 3.92);
    tl.fromTo("#b-sw2", { backgroundColor: "#303c48" }, { backgroundColor: "#399fef", duration: 0.15 }, 4.15);
    tl.fromTo("#b-sk2", { x: 0 }, { x: 34, duration: 0.25, ease: "back.out(2)" }, 4.15);
    tl.to("#b-cursor", { x: 1330, y: 922, duration: 0.55, ease: "power3.inOut" }, 3.9);
    tl.fromTo("#b-shine", { x: 0 }, { x: 760, duration: 0.5, ease: "power2.inOut" }, 4.1);
    tl.to("#b-cursor", { scale: 0.82, duration: 0.07 }, 4.6);
    tl.to("#b-btn", { scale: 0.95, duration: 0.07 }, 4.6);
    tl.to("#b-cursor", { opacity: 0, duration: 0.1 }, 4.7);
    // zoom through the button: its blue becomes the next frame
    tl.to("#b-cam", { scale: 16, duration: 0.5, ease: "power3.in" }, 4.7);
    tl.to("#b-flood", { opacity: 1, duration: 0.2, ease: "power2.in" }, 5.0);
    tl.set("#b-cam", { opacity: 0 }, 5.22);

    // progress step: rows arrive, spinners turn, each lands on a check
    tl.to("#b-flood", { opacity: 0, duration: 0.35, ease: "power2.out" }, 5.22);
    tl.fromTo("#b-prog", DEPTH, LAND, 5.22);
    tl.fromTo("#b-pfill", { scaleX: 0 }, { scaleX: 1, duration: 2.3, ease: "power1.inOut" }, 5.4);
    const done = [5.75, 6.45, 7.0, 7.5];
    done.forEach((t, i) => {
      tl.fromTo(`#b-r${i}`, { opacity: 0, y: 14, filter: "blur(4px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.4, ease: "expo.out" }, 5.35 + i * 0.07);
      tl.fromTo(`#b-sp${i}`, { rotation: 0 }, { rotation: 360 * (t - 5.35) * 1.4, duration: t - 5.35, ease: "none" }, 5.35);
      tl.to(`#b-sp${i}`, { opacity: 0, scale: 0.4, duration: 0.12 }, t);
      tl.fromTo(`#b-ck${i}`, { opacity: 0, scale: 0.3 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2.2)" }, t);
      tl.fromTo(`#b-r${i}`, { backgroundColor: "rgba(22,27,32,.92)" }, { backgroundColor: "rgba(16,42,30,.85)", duration: 0.25, yoyo: true, repeat: 1 }, t);
    });
    tl.fromTo("#b-loglines", { y: 0 }, { y: -184, duration: 2.3, ease: "steps(4)" }, 5.6);
    tl.to("#b-prog", { opacity: 0, scale: 0.94, filter: "blur(12px)", duration: 0.25, ease: "power2.in" }, 7.8);

    // the live site loads in a browser window
    tl.fromTo("#b-web", DEPTH, LAND, 7.95);
    tl.fromTo("#b-web > *", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.45, ease: "expo.out", stagger: 0.05 }, 8.05);
    tl.fromTo("#b-ofill", { scaleX: 0 }, { scaleX: 0.62, duration: 1.2, ease: "power2.inOut" }, 8.5);
    tl.fromTo("#b-otruck", { x: 0 }, { x: 228, duration: 1.2, ease: "power2.inOut" }, 8.5);
    tl.fromTo("#b-ping", { scale: 0.6, opacity: 0.9 }, { scale: 2.4, opacity: 0, duration: 0.8, ease: "power2.out" }, 8.6);
    tl.fromTo("#b-cap", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.2 }, 8.2);
    // whip out to the left
    tl.to(["#b-web", "#b-cap"], { x: -1920, filter: "blur(10px)", duration: 0.6, ease: "power2.inOut" }, 9.7);'''
open(OUT + "build.html", "w").write(scene("build", css, body, js))
