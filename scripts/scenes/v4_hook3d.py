import sys; sys.path.insert(0, sys.path[0])
from common import *
A = lambda w: at("hook", w)
T = dict(proxima=A("proxima"), gran=A("gran"), idea=A("idea"), en=A("en"), linea=A("linea"), hoy=A("hoy"))
html = f'''<template>
  <style>{FONTS}
    #root {{ position: absolute; inset: 0; overflow: hidden; background: #02040a; }}
    #h3 {{ position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; }}
    #h-flash {{ position: absolute; inset: 0; background: radial-gradient(circle at 50% 46%, #ffffff, rgba(255,214,150,.75) 25%, rgba(57,159,239,0) 65%); opacity: 0; }}
    .ring {{ position: absolute; left: 760px; top: 300px; width: 400px; height: 400px; border-radius: 50%; border: 3px solid rgba(255,220,170,.85); opacity: 0; }}
    #h-bloom {{ position: absolute; inset: 0; opacity: 0; background: radial-gradient(circle at 50% 50%, #fffaf0 0%, #ffd9a3 18%, #ff9a40 45%, #3a1a06 100%); }}
    #h-vig {{ position: absolute; inset: 0; background: radial-gradient(ellipse at center, rgba(0,0,0,0) 45%, rgba(0,0,0,.65) 100%); }}
  </style>
  <div id="root" data-composition-id="hook" data-width="1920" data-height="1080">
    <canvas id="h3" width="1920" height="1080"></canvas>
    <div class="ring" id="h-r0"></div><div class="ring" id="h-r1"></div><div class="ring" id="h-r2"></div>
    <div id="h-vig"></div>
    <div id="h-flash"></div>
    <div id="h-bloom"></div>
  </div>
  <script>
    const T = {T};
    const D = 5.6;
    const smooth = (a, b, t) => {{ const x = Math.min(1, Math.max(0, (t - a) / (b - a))); return x * x * (3 - 2 * x); }};
    const spring = (t) => {{ if (t <= 0) return 0; if (t >= 1) return 1; const z = 0.72, w = 11, wd = w * Math.sqrt(1 - z * z); return 1 - Math.exp(-z * w * t) * (Math.cos(wd * t) + (z * w / wd) * Math.sin(wd * t)); }};
    // seeded randomness: every frame is a pure function of t
    let seed = 7; const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);

    const canvas = document.getElementById("h3");
    const renderer = new THREE.WebGLRenderer({{ canvas, antialias: true, alpha: false }});
    renderer.setPixelRatio(window.devicePixelRatio || 1);
    renderer.setSize(1920, 1080, false);
    renderer.outputEncoding = THREE.sRGBEncoding;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 0.95;
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x02040a);
    const camera = new THREE.PerspectiveCamera(34, 1920 / 1080, 0.05, 200);

    // a soft studio environment for the glass to reflect: dark room, a few light strips
    const envScene = new THREE.Scene();
    envScene.background = new THREE.Color(0x05080d);
    const strip = (w, h, x, y, z, c, ry) => {{ const m = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({{ color: c, side: THREE.DoubleSide }})); m.position.set(x, y, z); m.rotation.y = ry; envScene.add(m); }};
    strip(6, 1.2, 0, 4, -6, 0x9fd2ff, 0); strip(1.2, 6, -6, 1, 0, 0xffd7a0, Math.PI / 2); strip(1.2, 6, 6, 1, 0, 0x6aa8ff, -Math.PI / 2); strip(8, 0.6, 0, -3, 5, 0x334455, 0);
    const pmrem = new THREE.PMREMGenerator(renderer);
    const env = pmrem.fromScene(envScene, 0.04).texture;
    scene.environment = env;

    // glow sprite texture (radial)
    const glowTex = (() => {{ const c = document.createElement("canvas"); c.width = c.height = 256; const g = c.getContext("2d"); const gr = g.createRadialGradient(128, 128, 0, 128, 128, 128); gr.addColorStop(0, "rgba(255,255,255,1)"); gr.addColorStop(0.25, "rgba(255,255,255,.55)"); gr.addColorStop(1, "rgba(255,255,255,0)"); g.fillStyle = gr; g.fillRect(0, 0, 256, 256); return new THREE.CanvasTexture(c); }})();
    const sprite = (color, size, op = 1) => {{ const s = new THREE.Sprite(new THREE.SpriteMaterial({{ map: glowTex, color, transparent: true, opacity: op, blending: THREE.AdditiveBlending, depthWrite: false }})); s.scale.set(size, size, 1); return s; }};

    // ── background: a slow nebula and a deep star field ──
    const nebula = new THREE.Group(); scene.add(nebula);
    [[0x1d4f8a, -9, 3, -30, 30, .22], [0x5a2d8a, 11, -4, -36, 34, .16], [0x8a5a1d, -3, -7, -26, 18, .12], [0x0f6a8a, 14, 7, -40, 40, .18]].forEach(([c, x, y, z, s, o]) => {{ const sp = sprite(c, s, o); sp.position.set(x, y, z); nebula.add(sp); }});
    const starGeo = new THREE.BufferGeometry(); const N = 2200; const sp = new Float32Array(N * 3);
    for (let i = 0; i < N; i++) {{ sp[i * 3] = (rnd() - 0.5) * 80; sp[i * 3 + 1] = (rnd() - 0.5) * 50; sp[i * 3 + 2] = -rnd() * 70 - 2; }}
    starGeo.setAttribute("position", new THREE.BufferAttribute(sp, 3));
    const stars = new THREE.Points(starGeo, new THREE.PointsMaterial({{ color: 0xa6d0f6, size: 0.06, sizeAttenuation: true, transparent: true, opacity: 0.85, depthWrite: false }}));
    scene.add(stars);

    // ── the bulb: A19 glass, threaded base, glass mount, tungsten coil ──
    const bulb = new THREE.Group(); scene.add(bulb);
    const prof = [new THREE.Vector2(0.5, -0.06)];
    const neck = new THREE.QuadraticBezierCurve(new THREE.Vector2(0.5, -0.02), new THREE.Vector2(0.5, 0.36), new THREE.Vector2(0.73, 0.67));
    neck.getPoints(16).forEach((v) => prof.push(v));
    for (let i = 1; i <= 48; i++) {{ const a = -0.75 + (i / 48) * (Math.PI / 2 + 0.75); prof.push(new THREE.Vector2(Math.max(0.0005, Math.cos(a)), 1.35 + Math.sin(a))); }}
    const glassGeo = new THREE.LatheGeometry(prof, 128);
    const glassMat = new THREE.MeshPhysicalMaterial({{ color: 0xffffff, metalness: 0, roughness: 0.04, clearcoat: 1, clearcoatRoughness: 0.03, envMapIntensity: 2.4, transparent: true, opacity: 0.1, depthWrite: false, emissive: 0xffa450, emissiveIntensity: 0 }});
    const glass = new THREE.Mesh(glassGeo, glassMat); glass.renderOrder = 2; bulb.add(glass);
    // fresnel rim: what makes clear glass read as glass
    const rimMat = new THREE.ShaderMaterial({{ transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide,
      uniforms: {{ c: {{ value: new THREE.Color(0xcfe6ff) }}, k: {{ value: 1 }} }},
      vertexShader: "varying vec3 vN; varying vec3 vV; void main(){{ vec4 mv = modelViewMatrix * vec4(position, 1.0); vN = normalize(normalMatrix * normal); vV = normalize(-mv.xyz); gl_Position = projectionMatrix * mv; }}",
      fragmentShader: "uniform vec3 c; uniform float k; varying vec3 vN; varying vec3 vV; void main(){{ float f = pow(1.0 - abs(dot(normalize(vN), normalize(vV))), 3.0); gl_FragColor = vec4(c * f * k, f * k); }}" }});
    const rim = new THREE.Mesh(glassGeo, rimMat); rim.renderOrder = 3; bulb.add(rim);
    // base: smooth collar, helical thread, black insulator, solder contact
    const alu = new THREE.MeshStandardMaterial({{ color: 0xd4d8de, metalness: 1, roughness: 0.28, envMapIntensity: 1.4 }});
    bulb.add(new THREE.Mesh(new THREE.LatheGeometry([new THREE.Vector2(0.505, -0.06), new THREE.Vector2(0.505, -0.2), new THREE.Vector2(0.45, -0.22), new THREE.Vector2(0.45, -0.84), new THREE.Vector2(0.4, -0.9), new THREE.Vector2(0.3, -0.93)], 96), alu));
    const helix = []; for (let i = 0; i <= 400; i++) {{ const u = i / 400, a = u * Math.PI * 2 * 4.5; helix.push(new THREE.Vector3(Math.cos(a) * 0.455, -0.26 - u * 0.54, Math.sin(a) * 0.455)); }}
    bulb.add(new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(helix), 600, 0.038, 12), alu));
    bulb.add(new THREE.Mesh(new THREE.LatheGeometry([new THREE.Vector2(0.3, -0.93), new THREE.Vector2(0.22, -1.0), new THREE.Vector2(0.13, -1.05), new THREE.Vector2(0.0005, -1.06)], 64), new THREE.MeshPhysicalMaterial({{ color: 0x0b0c0e, roughness: 0.15, clearcoat: 1, envMapIntensity: 1.5 }})));
    const tip = new THREE.Mesh(new THREE.SphereGeometry(0.1, 32, 16, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2), new THREE.MeshStandardMaterial({{ color: 0xc9a46a, metalness: 1, roughness: 0.3 }})); tip.position.y = -1.04; bulb.add(tip);
    // mount: flared glass stem, lead-in wires, support hooks
    const stemMat = new THREE.MeshPhysicalMaterial({{ color: 0xeaf4ff, roughness: 0.05, clearcoat: 1, transparent: true, opacity: 0.35, envMapIntensity: 2, depthWrite: false }});
    bulb.add(new THREE.Mesh(new THREE.LatheGeometry([new THREE.Vector2(0.4, -0.04), new THREE.Vector2(0.16, 0.12), new THREE.Vector2(0.075, 0.32), new THREE.Vector2(0.07, 0.68), new THREE.Vector2(0.11, 0.74), new THREE.Vector2(0.0005, 0.77)], 48), stemMat));
    const wireMat = new THREE.MeshStandardMaterial({{ color: 0xb8c0c8, metalness: 1, roughness: 0.2 }});
    const tube = (pts, r, mat) => new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts), 48, r, 8), mat);
    [-1, 1].forEach((sd) => bulb.add(tube([new THREE.Vector3(sd * 0.04, 0.1, 0), new THREE.Vector3(sd * 0.05, 0.7, 0), new THREE.Vector3(sd * 0.2, 1.0, 0), new THREE.Vector3(sd * 0.36, 1.24, 0)], 0.011, wireMat)));
    bulb.add(tube([new THREE.Vector3(0, 0.76, 0), new THREE.Vector3(0, 1.02, 0)], 0.02, stemMat));
    const bead = new THREE.Mesh(new THREE.SphereGeometry(0.05, 20, 12), stemMat); bead.position.y = 1.03; bulb.add(bead);
    [-1, 1].forEach((sd) => bulb.add(tube([new THREE.Vector3(0, 1.03, 0), new THREE.Vector3(sd * 0.1, 1.2, 0), new THREE.Vector3(sd * 0.14, 1.31, 0)], 0.006, wireMat)));
    const coil = []; for (let i = 0; i <= 420; i++) {{ const u = i / 420, x = -0.36 + u * 0.72, a = u * Math.PI * 2 * 22; coil.push(new THREE.Vector3(x, 1.24 + Math.sin(u * Math.PI) * 0.07 + Math.sin(a) * 0.028, Math.cos(a) * 0.028)); }}
    const filMat = new THREE.MeshBasicMaterial({{ color: 0x2a1a10, toneMapped: false }});
    const filament = new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(coil), 1400, 0.007, 6), filMat); bulb.add(filament);
    const fglow = sprite(0xff9a40, 1, 0); fglow.position.set(0, 1.28, 0); bulb.add(fglow);
    const fcore = sprite(0xfff4dc, 0.5, 0); fcore.position.set(0, 1.28, 0.02); bulb.add(fcore);
    const halo = sprite(0xffa65a, 6, 0); halo.position.set(0, 1.2, -0.3); bulb.add(halo);
    const light = new THREE.PointLight(0xffb066, 0, 14, 2); light.position.set(0, 1.28, 0); bulb.add(light);
    scene.add(new THREE.AmbientLight(0x223344, 0.6));
    const rimL = new THREE.DirectionalLight(0x6aa8ff, 1.4); rimL.position.set(-4, 3, -3); scene.add(rimL);
    const key = new THREE.DirectionalLight(0xffe2b8, 0.9); key.position.set(3, 2, 4); scene.add(key);
    const pool = sprite(0x3a7fc0, 5, 0.22); pool.position.set(0, -1.7, -0.5); scene.add(pool);
    const cold = new THREE.Color(0xcfe6ff), warm = new THREE.Color(0xffc488), hot = new THREE.Color(1.0, 0.72, 0.38);

    // ── the network that the light becomes ──
    const net = new THREE.Group(); scene.add(net);
    const NN = 46, nodes = [];
    for (let i = 0; i < NN; i++) {{ const y = 1 - (i / (NN - 1)) * 2, r = Math.sqrt(1 - y * y), th = i * 2.399963; nodes.push(new THREE.Vector3(Math.cos(th) * r * 5.2, 1.0 + y * 3.4, Math.sin(th) * r * 5.2)); }}
    const nodeSprites = nodes.map((p) => {{ const s = sprite(0x66b8ff, 0.55, 0); s.position.copy(p); net.add(s); return s; }});
    const lines = [];
    const lineMat = () => new THREE.LineBasicMaterial({{ color: 0x66b8ff, transparent: true, opacity: 0.0, blending: THREE.AdditiveBlending, depthWrite: false }});
    nodes.forEach((p, i) => {{
      const c = new THREE.QuadraticBezierCurve3(new THREE.Vector3(0, 1.25, 0), new THREE.Vector3(p.x * 0.4, p.y + 1.2, p.z * 0.4), p);
      const g = new THREE.BufferGeometry().setFromPoints(c.getPoints(40)); g.setDrawRange(0, 0);
      const l = new THREE.Line(g, lineMat()); net.add(l); lines.push({{ l, delay: (i % 12) * 0.03 }});
    }});
    const mesh = [];
    for (let i = 0; i < NN; i++) for (let j = i + 1; j < NN; j++) if (nodes[i].distanceTo(nodes[j]) < 2.4) {{ const g = new THREE.BufferGeometry().setFromPoints([nodes[i], nodes[j]]); const l = new THREE.Line(g, lineMat()); net.add(l); mesh.push(l); }}

    function render(t) {{
      // filament heats on "gran idea", blazes on "en línea", then the camera dives into it
      const dive = smooth(4.6, 5.6, t), dv = dive * dive;
      const heat = 0.16 * smooth(0.2, 0.8, t) + 0.45 * smooth(T.gran, T.idea + 0.3, t) + 0.5 * smooth(T.en, T.linea + 0.2, t) + 0.6 * dv;
      const h = heat + 0.03 * Math.sin(t * 23) * heat;
      filMat.color.copy(hot).multiplyScalar(0.12 + h * 2.4);
      fglow.material.opacity = Math.min(0.6, h * 0.55); fglow.scale.setScalar(0.7 + h * 1.0);
      fcore.material.opacity = Math.min(0.95, h * 0.9); fcore.scale.setScalar(0.3 + h * 0.3);
      halo.material.opacity = Math.min(0.22, h * 0.2);
      light.intensity = h * 3;
      glassMat.emissiveIntensity = h * 0.12;
      rimMat.uniforms.c.value.copy(cold).lerp(warm, Math.min(1, h)); rimMat.uniforms.k.value = 0.8 + h * 0.5;
      const form = spring((t - T.proxima + 0.2) / 1.1);
      bulb.scale.setScalar(0.7 + 0.3 * form);
      bulb.rotation.y = 0.5 + t * 0.35;
      bulb.position.y = Math.sin(t * 1.6) * 0.05;
      // the web draws outward on "en línea" and stays lit
      const grow = (t - T.en);
      lines.forEach(({{ l, delay }}) => {{ const u = Math.min(1, Math.max(0, (grow - delay) / 0.5)); l.geometry.setDrawRange(0, Math.floor(u * 41)); l.material.opacity = 0.75; }});
      nodeSprites.forEach((s, i) => {{ const u = spring((t - T.linea - (i % 12) * 0.02) / 0.6); s.material.opacity = 0.95 * u; s.scale.setScalar(0.25 + u * 0.4); }});
      mesh.forEach((l) => {{ l.material.opacity = 0.32 * smooth(T.linea + 0.1, T.linea + 0.7, t); }});
      net.rotation.y = t * 0.25;
      // camera: creeps in, kicks back on "hoy" to show the web, then plunges into the filament
      const pull = spring((t - T.hoy) / 1.0);
      const kick = smooth(T.hoy - 0.15, T.hoy, t) * (1 - smooth(T.hoy, T.hoy + 0.1, t));
      const base = 9.6 - 1.4 * smooth(0, T.linea, t) + 8 * pull - 0.4 * kick;
      const dist = base * (1 - dv) + 0.45 * dv;
      const ang = -0.35 + t * 0.18 + 0.5 * pull * (1 - dv);
      const ty = 0.7 + 0.58 * dv;
      camera.position.set(Math.sin(ang) * dist, ty + 0.6 * pull * (1 - dv), Math.cos(ang) * dist);
      camera.lookAt(0, ty, 0);
      camera.rotation.z += -0.06 * pull * (1 - dv) + 0.25 * dv;
      nebula.rotation.z = t * 0.02; nebula.position.x = -t * 0.3;
      stars.rotation.y = t * 0.01;
      renderer.render(scene, camera);
    }}
    render(0);
    const tl = gsap.timeline({{ paused: true }});
    const clock = {{ t: 0 }};
    tl.fromTo(clock, {{ t: 0 }}, {{ t: D, duration: D, ease: "none", onUpdate: () => render(clock.t) }}, 0);
    tl.fromTo("#h-flash", {{ opacity: 0 }}, {{ keyframes: [{{ opacity: 0.85, duration: 0.08 }}, {{ opacity: 0, duration: 0.55 }}] }}, T.hoy);
    [0, 1, 2].forEach((i) => tl.fromTo(`#h-r${{i}}`, {{ scale: 0.2, opacity: 0.9 }}, {{ scale: 3.4, opacity: 0, duration: 1.2, ease: "power2.out" }}, T.hoy + i * 0.18));
    tl.fromTo("#h-bloom", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.45, ease: "power2.in" }}, 5.15);
    window.__timelines["hook"] = tl;
  </script>
</template>
'''
open(OUT + "hook.html", "w").write(html)
print("hook 3d")
