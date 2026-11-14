import sys; sys.path.insert(0, sys.path[0])
from common import *
B = lambda w: at("problem", w)
T = dict(run=B("carrera"), h1=B("servidores"), h2=B("configurar"), h3=B("cuentas"), noc=B("noches"))
walls = [["Servidores", "M3 4h18v6H3zM3 14h18v6H3zM7 7h.01M7 17h.01"], ["Configurar", "M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"], ["Cuentas por pagar", "M12 2v20M17 6H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"]]
ROCKET = "M4.5 16.5c-1.5 1.3-2 5-2 5s3.7-.5 5-2c.7-.8.7-2.1-.1-2.9a2.2 2.2 0 0 0-2.9-.1zM12 15l-3-3a22 22 0 0 1 2-3.9A12.9 12.9 0 0 1 22 2c0 2.7-.8 7.5-6 11a22.4 22.4 0 0 1-4 2zM9 12H4s.6-3 2-4c1.6-1.1 5 0 5 0M12 15v5s3-.6 4-2c1.1-1.6 0-5 0-5"
import json
html = f'''<template>
  <style>{FONTS}
    #root {{ position: absolute; inset: 0; overflow: hidden; background: #03060c; font-family: "Hanken Grotesk Variable", sans-serif; }}
    #p3 {{ position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; }}
    .stamp {{ position: absolute; left: 0; right: 0; top: 165px; text-align: center; font-family: "Michroma", sans-serif; font-size: 170px; color: transparent; -webkit-text-stroke: 4px #ff7a70; text-shadow: 0 0 50px rgba(255,90,80,.6); opacity: 0; letter-spacing: 6px; }}
    #pb-clock {{ position: absolute; left: 0; right: 0; top: 230px; text-align: center; opacity: 0; }}
    #pb-clock .t {{ font: 700 200px "JetBrains Mono Variable", monospace; color: #fff1ef; text-shadow: 0 0 70px rgba(255,90,80,.85); }}
    #pb-clock .s {{ font-size: 42px; color: #ffb3ad; margin-top: -14px; }}
    #pb-zz {{ position: absolute; left: 900px; top: 560px; font: 700 54px "Michroma", sans-serif; color: #a6d0f6; opacity: 0; text-shadow: 0 0 20px #05080d; }}
    #p-open {{ position: absolute; inset: 0; background: radial-gradient(circle at 50% 50%, #fffaf0 0%, #ffd9a3 18%, #ff9a40 45%, #3a1a06 100%); }}
    #p-bloom {{ position: absolute; inset: 0; opacity: 0; background: radial-gradient(circle at 50% 50%, #ffffff 0%, #a6d0f6 20%, #399fef 52%, #12406a 100%); }}
    #p-vig {{ position: absolute; inset: 0; background: radial-gradient(ellipse at center, rgba(0,0,0,0) 50%, rgba(0,0,0,.6) 100%); }}
  </style>
  <div id="root" data-composition-id="problem" data-width="1920" data-height="1080">
    <canvas id="p3" width="1920" height="1080"></canvas>
    <div id="p-vig"></div>
    <div class="stamp" id="ps0">LENTO</div><div class="stamp" id="ps1">COMPLICADO</div><div class="stamp" id="ps2">CARO</div>
    <div id="pb-zz">z z</div>
    <div id="pb-clock"><div class="t"><span>03</span><span id="p-colon">:</span><span>12</span></div><div class="s">otra noche sin dormir</div></div>
    <div id="p-bloom"></div><div id="p-open"></div>
  </div>
  <script>
    const T = {json.dumps(T)};
    const WALLS = {json.dumps(walls)};
    const D = 8.8, WX = [14, 23, 32];
    const smooth = (a, b, t) => {{ const x = Math.min(1, Math.max(0, (t - a) / (b - a))); return x * x * (3 - 2 * x); }};
    const clamp01 = (x) => Math.min(1, Math.max(0, x));
    const spring = (t) => {{ if (t <= 0) return 0; if (t >= 1) return 1; const z = 0.72, w = 11, wd = w * Math.sqrt(1 - z * z); return 1 - Math.exp(-z * w * t) * (Math.cos(wd * t) + (z * w / wd) * Math.sin(wd * t)); }};
    let seed = 11; const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);

    const renderer = new THREE.WebGLRenderer({{ canvas: document.getElementById("p3"), antialias: true }});
    renderer.setPixelRatio(window.devicePixelRatio || 1); renderer.setSize(1920, 1080, false);
    renderer.outputEncoding = THREE.sRGBEncoding; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05;
    const scene = new THREE.Scene();
    const fogBlue = new THREE.Color(0x07101c), fogRed = new THREE.Color(0x2a0606);
    scene.background = fogBlue.clone(); scene.fog = new THREE.FogExp2(fogBlue.clone(), 0.038);
    const camera = new THREE.PerspectiveCamera(38, 1920 / 1080, 0.1, 300);
    const amb = new THREE.AmbientLight(0x30455c, 0.9); scene.add(amb);
    const key = new THREE.DirectionalLight(0xbfdcff, 1.1); key.position.set(-6, 10, 8); scene.add(key);
    const redL = new THREE.PointLight(0xff3020, 0, 40, 2); redL.position.set(30, 6, 4); scene.add(redL);

    const canvasTex = (w, h, draw) => {{ const c = document.createElement("canvas"); c.width = w; c.height = h; draw(c.getContext("2d"), w, h); const t = new THREE.CanvasTexture(c); t.encoding = THREE.sRGBEncoding; t.anisotropy = 8; return t; }};
    const glowTex = canvasTex(128, 128, (g) => {{ const gr = g.createRadialGradient(64, 64, 0, 64, 64, 64); gr.addColorStop(0, "rgba(255,255,255,1)"); gr.addColorStop(.3, "rgba(255,255,255,.5)"); gr.addColorStop(1, "rgba(255,255,255,0)"); g.fillStyle = gr; g.fillRect(0, 0, 128, 128); }});
    const sprite = (c, s, o) => {{ const m = new THREE.Sprite(new THREE.SpriteMaterial({{ map: glowTex, color: c, transparent: true, opacity: o, blending: THREE.AdditiveBlending, depthWrite: false }})); m.scale.set(s, s, 1); return m; }};

    // floor: a metallic grid that the fog swallows
    const grid = canvasTex(512, 512, (g, w, h) => {{ g.fillStyle = "#0a1220"; g.fillRect(0, 0, w, h); g.strokeStyle = "rgba(102,184,255,.55)"; g.lineWidth = 3; g.strokeRect(0, 0, w, h); g.strokeStyle = "rgba(102,184,255,.18)"; g.lineWidth = 1.5; g.beginPath(); g.moveTo(w / 2, 0); g.lineTo(w / 2, h); g.moveTo(0, h / 2); g.lineTo(w, h / 2); g.stroke(); }});
    grid.wrapS = grid.wrapT = THREE.RepeatWrapping; grid.repeat.set(120, 100);
    const floorMat = new THREE.MeshStandardMaterial({{ map: grid, metalness: 0.55, roughness: 0.35, emissive: new THREE.Color(0x000000) }});
    const floor = new THREE.Mesh(new THREE.PlaneGeometry(480, 400), floorMat); floor.rotation.x = -Math.PI / 2; floor.position.x = 200; scene.add(floor);
    // the lit track
    const track = new THREE.Mesh(new THREE.BoxGeometry(480, 0.04, 0.5), new THREE.MeshBasicMaterial({{ color: 0x5fb4ff }})); track.position.set(200, 0.02, 0); scene.add(track);
    [-1.2, 1.2].forEach((z) => {{ const e = new THREE.Mesh(new THREE.BoxGeometry(480, 0.02, 0.06), new THREE.MeshBasicMaterial({{ color: 0x2a6fb0 }})); e.position.set(200, 0.02, z); scene.add(e); }});
    // light posts along both sides: depth markers that stream past
    const posts = [];
    for (let i = -4; i < 30; i++) for (const z of [-5.5, -10]) {{
      const p = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.08, 3.2, 10), new THREE.MeshStandardMaterial({{ color: 0x1b2a3a, metalness: 0.8, roughness: 0.3 }}));
      p.position.set(i * 4, 1.6, z); scene.add(p);
      const lamp = sprite(0x66b8ff, 1.3, 0.85); lamp.position.set(i * 4, 3.25, z); scene.add(lamp); posts.push(lamp);
    }}
    // distant skyline blocks for parallax
    for (let i = 0; i < 70; i++) {{ const h = 4 + rnd() * 16; const b = new THREE.Mesh(new THREE.BoxGeometry(2 + rnd() * 4, h, 2 + rnd() * 4), new THREE.MeshStandardMaterial({{ color: 0x0c1624, metalness: 0.3, roughness: 0.7, emissive: 0x0a1a2c, emissiveIntensity: 0.6 }})); b.position.set(-20 + i * 4 + rnd() * 3, h / 2, -26 - rnd() * 20); scene.add(b); }}

    // walls: red glass panels with icon, label and hazard stripes
    const wallMeshes = WALLS.map(([label, path], i) => {{
      const tex = canvasTex(600, 512, (g, w, h) => {{
        const gr = g.createLinearGradient(0, 0, 0, h); gr.addColorStop(0, "#4a1414"); gr.addColorStop(1, "#1a0707"); g.fillStyle = gr; g.fillRect(0, 0, w, h);
        g.strokeStyle = "#ff6b62"; g.lineWidth = 14; g.strokeRect(7, 7, w - 14, h - 14);
        g.save(); g.translate(w / 2 - 96, 70); g.scale(8, 8); g.strokeStyle = "#ff8a80"; g.lineWidth = 2; g.lineCap = "round"; g.lineJoin = "round"; g.stroke(new Path2D(path)); g.restore();
        g.fillStyle = "#ffe0dd"; g.font = "700 50px Hanken Grotesk Variable, sans-serif"; g.textAlign = "center";
        const words = label.split(" "); words.length > 2 ? (g.fillText(words.slice(0, 2).join(" "), w / 2, 320), g.fillText(words.slice(2).join(" "), w / 2, 376)) : g.fillText(label, w / 2, 340);
        for (let x = -60; x < w + 60; x += 56) {{ g.fillStyle = "#f0b965"; g.beginPath(); g.moveTo(x, h - 70); g.lineTo(x + 28, h - 70); g.lineTo(x - 2, h - 14); g.lineTo(x - 30, h - 14); g.fill(); }}
      }});
      const mat = new THREE.MeshStandardMaterial({{ map: tex, emissiveMap: tex, emissive: new THREE.Color(0xffffff), emissiveIntensity: 0.55, metalness: 0.2, roughness: 0.4 }});
      const side = new THREE.MeshStandardMaterial({{ color: 0x2a0b0b, metalness: 0.6, roughness: 0.3 }});
      const m = new THREE.Mesh(new THREE.BoxGeometry(0.5, 2.2, 2.6), [mat, side, side, side, side, side]);
      m.position.set(WX[i], 1.1, 0);
      // the textured face points back toward the runner and the camera
      m.material = [side, mat, side, side, side, side];
      const glow = sprite(0xff4a40, 6, 0.25); glow.position.set(WX[i] - 0.5, 1.2, 0); scene.add(glow);
      scene.add(m); return {{ m, mat, glow }};
    }});

    // the runner: a rounded glass-blue block with the rocket on its face
    const rs = new THREE.Shape(); const r = 0.22, s = 0.5;
    rs.moveTo(-s + r, -s); rs.lineTo(s - r, -s); rs.quadraticCurveTo(s, -s, s, -s + r); rs.lineTo(s, s - r); rs.quadraticCurveTo(s, s, s - r, s); rs.lineTo(-s + r, s); rs.quadraticCurveTo(-s, s, -s, s - r); rs.lineTo(-s, -s + r); rs.quadraticCurveTo(-s, -s, -s + r, -s);
    const rgeo = new THREE.ExtrudeGeometry(rs, {{ depth: 0.8, bevelEnabled: true, bevelThickness: 0.12, bevelSize: 0.1, bevelSegments: 6, curveSegments: 12 }}); rgeo.center();
    const runner = new THREE.Group(); scene.add(runner);
    const body = new THREE.Mesh(rgeo, new THREE.MeshPhysicalMaterial({{ color: 0x2f8fe0, metalness: 0.25, roughness: 0.18, clearcoat: 1, clearcoatRoughness: 0.08, emissive: 0x0d3a66, emissiveIntensity: 0.6 }}));
    body.rotation.y = Math.PI / 2; runner.add(body);
    const iconTex = canvasTex(256, 256, (g) => {{ g.translate(128 - 84, 128 - 84); g.scale(7, 7); g.strokeStyle = "#e9f5ff"; g.lineWidth = 2.2; g.lineCap = "round"; g.lineJoin = "round"; g.stroke(new Path2D("{ROCKET}")); }});
    const icon = new THREE.Mesh(new THREE.PlaneGeometry(0.85, 0.85), new THREE.MeshBasicMaterial({{ map: iconTex, transparent: true }}));
    icon.position.set(0, 0, 0.56); runner.add(icon);
    const rglow = sprite(0x66b8ff, 3.2, 0.5); runner.add(rglow);
    const trail = sprite(0x66b8ff, 1, 0); scene.add(trail);
    const warmC = new THREE.Color(0xffa860), blueC = new THREE.Color(0x66b8ff), blueE = new THREE.Color(0x0d3a66);
    const dawn = sprite(0xbfe0ff, 6, 0); dawn.material.fog = false; dawn.material.depthTest = false; dawn.renderOrder = 10; scene.add(dawn);
    const dawnL = new THREE.PointLight(0x66b8ff, 0, 60, 2); scene.add(dawnL);
    // the same night sky as the hook, above the fog
    const skyGeo = new THREE.BufferGeometry(), skyP = new Float32Array(1600 * 3);
    for (let i = 0; i < 1600; i++) {{ const th = rnd() * Math.PI * 2, ph = 0.08 + rnd() * 1.2, r = 140; skyP[i * 3] = 60 + Math.cos(th) * Math.cos(ph) * r; skyP[i * 3 + 1] = Math.sin(ph) * r; skyP[i * 3 + 2] = Math.sin(th) * Math.cos(ph) * r; }}
    skyGeo.setAttribute("position", new THREE.BufferAttribute(skyP, 3));
    scene.add(new THREE.Points(skyGeo, new THREE.PointsMaterial({{ color: 0xa6d0f6, size: 0.35, fog: false, transparent: true, opacity: 0.8, depthWrite: false }})));

    // impact sparks, simulated once
    const SP = 70, sparks = [];
    [T.h1, T.h2, T.h3].forEach((th, k) => {{ const g = new THREE.BufferGeometry(), pos = new Float32Array(SP * 3); g.setAttribute("position", new THREE.BufferAttribute(pos, 3));
      const pts = new THREE.Points(g, new THREE.PointsMaterial({{ color: 0xffb070, size: 0.09, transparent: true, opacity: 0, blending: THREE.AdditiveBlending, depthWrite: false }})); scene.add(pts);
      const v = []; for (let i = 0; i < SP; i++) v.push([-(1 + rnd() * 5), 1 + rnd() * 5, (rnd() - 0.5) * 6]); sparks.push({{ th, pts, v, x: WX[k] - 0.3 }}); }});

    // the runner's path: sprint into each wall on its word, bounce back, flip over it
    const HITS = [T.h1, T.h2, T.h3];
    function runnerAt(t) {{
      let x = 0, y = 0, rot = 0, sq = 0;
      if (t >= T.run) {{
        let from = 0, ft = T.run;
        for (let k = 0; k < 3; k++) {{
          const hx = WX[k] - 0.95, th = HITS[k];
          if (t < th) {{ const u = clamp01((t - ft) / (th - ft)); x = from + (hx - from) * u * u; return [x, 0, 0, 0]; }}
          if (t < th + 0.16) {{ const u = (t - th) / 0.16; x = hx - 0.7 * Math.sin(u * Math.PI / 2); sq = Math.sin(u * Math.PI); return [x, 0, 0, sq]; }}
          if (t < th + 0.62) {{ const u = (t - th - 0.16) / 0.46; x = hx - 0.7 + (2.9) * u; y = Math.sin(u * Math.PI) * 2.5; rot = -u * Math.PI * 2; return [x, y, rot, 0]; }}
          from = hx + 2.2; ft = th + 0.62; x = from;
        }}
        // after the last wall the race drags to a stall on "noches"
        const u = clamp01((t - ft) / Math.max(0.3, T.noc - ft)); x = from + 5 * (1 - (1 - u) * (1 - u));
        const tired = smooth(T.noc, T.noc + 0.6, t) * (1 - smooth(7.3, 7.6, t));
        const dash = smooth(7.4, 8.8, t);
        return [x + 34 * dash * dash, -0.12 * tired, 0.32 * tired, 0];
      }}
      return [x, y, rot, sq];
    }}
    const shakeAt = (t) => {{ let s = 0; [...HITS, T.noc + 0.1].forEach((th) => {{ const d = t - th; if (d > 0 && d < 0.5) s += Math.exp(-d * 9) * Math.sin(d * 70) * 0.28; }}); return s; }};

    function render(t) {{
      const [x, y, rot, sq] = runnerAt(t);
      runner.position.set(x, 0.62 + y + (t > T.run && t < T.noc ? Math.abs(Math.sin(t * 19)) * 0.07 : 0), 0);
      runner.rotation.z = rot; runner.scale.set(1 - sq * 0.25, 1 + sq * 0.18, 1);
      const [px] = runnerAt(t - 0.05); const speed = Math.max(0, x - px) / 0.05;
      trail.position.set(x - 1.2, 0.62 + y, 0); trail.scale.set(Math.min(6, speed * 0.5), 0.7, 1); trail.material.opacity = Math.min(0.6, speed * 0.05);
      const w = 1 - smooth(0.2, 1.3, t);
      rglow.material.color.copy(blueC).lerp(warmC, w); rglow.scale.setScalar(3.2 + 2.5 * w); rglow.material.opacity = 0.5 + 0.25 * w;
      body.material.emissive.copy(blueE).lerp(warmC, w * 0.3);
      dawn.position.set(x + 80, 5, -2); dawn.material.opacity = smooth(7.2, 8.2, t); dawn.scale.setScalar(14 + 50 * smooth(7.6, 8.8, t));
      dawnL.position.set(x + 45, 12, 0); dawnL.intensity = 4 * smooth(7.2, 8.2, t);
      // walls flash red on their hit
      wallMeshes.forEach((w, k) => {{ const d = t - HITS[k]; const f = d > 0 ? Math.exp(-d * 5) : 0; w.mat.emissiveIntensity = 0.55 + f * 2.5; w.glow.material.opacity = 0.25 + f * 0.9; w.m.position.z = d > 0 && d < 0.3 ? Math.sin(d * 80) * 0.08 * (1 - d / 0.3) : 0; }});
      sparks.forEach((sp) => {{ const d = t - sp.th; const a = sp.pts.geometry.attributes.position; if (d < 0 || d > 1) {{ sp.pts.material.opacity = 0; return; }}
        for (let i = 0; i < SP; i++) {{ const v = sp.v[i]; a.array[i * 3] = sp.x + v[0] * d; a.array[i * 3 + 1] = 1.2 + v[1] * d - 4.9 * d * d; a.array[i * 3 + 2] = v[2] * d; }} a.needsUpdate = true; sp.pts.material.opacity = 1 - d; }});
      // "noches sin dormir": the world bleeds red
      const red = smooth(T.noc - 0.1, T.noc + 0.5, t) * (1 - smooth(7.2, 8.0, t));
      scene.fog.color.copy(fogBlue).lerp(fogRed, red); scene.background.copy(scene.fog.color);
      redL.intensity = red * 5; amb.color.setHex(red > 0.5 ? 0x5a2020 : 0x30455c);
      floorMat.emissive.setRGB(red * 0.12, 0, 0);
      // chase camera: three-quarter from behind, lagging the runner, shaken by each hit
      const [cx] = runnerAt(t - 0.18), sh = shakeAt(t);
      const open = 1 - smooth(0, 1.5, t), end = smooth(7.6, 8.8, t);
      const back = (6.8 - 1.2 * smooth(T.noc, T.noc + 1, t)) * (1 - open) + 3.2 * open, height = (2.6 + 0.5 * smooth(T.noc, T.noc + 1, t)) * (1 - open) + 1.15 * open - 1.6 * end;
      camera.position.set(cx - back, height + sh * 0.6, (6.4 + sh) * (1 - open) + 0.2 * open - 5.6 * end);
      camera.lookAt(cx + 3.2 * (1 - open) + 0.4 * open + 6 * end, 1.1 - 0.3 * open + 0.5 * end, 0);
      camera.rotation.z += -0.04 + sh * 0.05;
      renderer.render(scene, camera);
    }}
    render(0);
    const tl = gsap.timeline({{ paused: true }});
    const clock = {{ t: 0 }};
    tl.fromTo(clock, {{ t: 0 }}, {{ t: D, duration: D, ease: "none", onUpdate: () => render(clock.t) }}, 0);
    [[T.h1, 0], [T.h2, 1], [T.h3, 2]].forEach(([th, i]) => tl.fromTo(`#ps${{i}}`, {{ opacity: 0, scale: 1.5 }}, {{ keyframes: [{{ opacity: 1, scale: 1, duration: 0.18, ease: "power3.out" }}, {{ opacity: 1, duration: 0.25 }}, {{ opacity: 0, scale: 0.94, duration: 0.2 }}] }}, th));
    tl.fromTo("#pb-clock", {{ opacity: 0, y: -260, scale: 1.3 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.4)" }}, T.noc);
    tl.fromTo("#pb-zz", {{ opacity: 0, y: 0 }}, {{ opacity: 1, y: -40, duration: 1.2, ease: "power1.out" }}, T.noc + 0.3);
    [T.noc + 0.5, T.noc + 1.1, T.noc + 1.7].forEach((t) => {{ tl.set("#p-colon", {{ opacity: 0 }}, t); tl.set("#p-colon", {{ opacity: 1 }}, t + 0.3); }});
    tl.to(["#pb-clock", "#pb-zz"], {{ opacity: 0, filter: "blur(10px)", duration: 0.4 }}, 7.5);
    tl.fromTo("#p-open", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.6, ease: "power2.out" }}, 0);
    tl.fromTo("#p-bloom", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4, ease: "power2.in" }}, 8.4);
    window.__timelines["problem"] = tl;
  </script>
</template>
'''
open(OUT + "problem.html", "w").write(html)
print("problem 3d")
