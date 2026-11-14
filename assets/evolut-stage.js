/* One set and one app connect the shots. Every pose is derived from playhead time. */
window.createEvolutStage = function (canvas) {
  const T = window.THREE;
  const renderer = new T.WebGLRenderer({ canvas, antialias: true, alpha: false });
  renderer.setSize(1920, 1080, false);
  renderer.setClearColor(0x080e18);
  renderer.outputEncoding = T.sRGBEncoding;
  const scene = new T.Scene();
  scene.fog = new T.FogExp2(0x080e18, .04);
  const camera = new T.PerspectiveCamera(35, 1920 / 1080, .1, 100);
  scene.add(new T.HemisphereLight(0xc7e7ff, 0x1b2d47, .83));
  const key = new T.DirectionalLight(0xffe0bb, 1.27);
  key.position.set(-5, 8, 5);
  scene.add(key);
  const rim = new T.DirectionalLight(0x489dff, 2.35);
  rim.position.set(5, 4, -7);
  scene.add(rim);

  const fill = new T.DirectionalLight(0xb4dcff, .68);
  fill.position.set(5, 2, 5);
  scene.add(fill);

  const material = (color, metalness = .18, roughness = .46) => new T.MeshStandardMaterial({ color, metalness, roughness });
  const light = color => new T.MeshBasicMaterial({ color });
  const navy = material(0x25486c, .40, .31);
  const dark = material(0x101e30, .24, .40);
  const steel = material(0x6c8fae, .42, .29);
  const blue = light(0x61bdff);
  const mint = light(0x74edc0);
  const amber = light(0xffb571);
  const shadowImage = document.createElement('canvas');
  shadowImage.width = shadowImage.height = 128;
  const shadowCtx = shadowImage.getContext('2d');
  const gradient = shadowCtx.createRadialGradient(64, 64, 0, 64, 64, 64);
  gradient.addColorStop(0, 'rgba(1,3,8,.9)');
  gradient.addColorStop(.5, 'rgba(1,3,8,.45)');
  gradient.addColorStop(1, 'rgba(1,3,8,0)');
  shadowCtx.fillStyle = gradient;
  shadowCtx.fillRect(0, 0, 128, 128);
  const shadowMaterial = new T.MeshBasicMaterial({
    map: new T.CanvasTexture(shadowImage), transparent: true, depthWrite: false
  });
  function mesh(parent, geometry, surface, x = 0, y = 0, z = 0) {
    const object = new T.Mesh(geometry, surface);
    object.position.set(x, y, z);
    parent.add(object);
    return object;
  }
  const solidGeometries = new Map();
  function solid(size, requestedRadius) {
    const radius = Math.min(requestedRadius, Math.min(...size) * .47);
    const key = size.join(",") + ":" + radius;
    if (solidGeometries.has(key)) return solidGeometries.get(key);
    if (radius < .016) {
      const geometry = new T.BoxGeometry(...size);
      solidGeometries.set(key, geometry);
      return geometry;
    }
    // Concentrate vertices at the edges, then round them with analytic normals.
    const geometry = new T.BoxGeometry(2, 2, 2, 8, 8, 8);
    const positions = geometry.attributes.position;
    const normals = geometry.attributes.normal;
    const half = size.map(value => value / 2);
    const inner = half.map(value => value - radius);
    const roundedGrid = [0, .18, .52, .80, 1];
    for (let i = 0; i < positions.count; i++) {
      const unit = [positions.getX(i),positions.getY(i),positions.getZ(i)];
      const corner = unit.map((value, axis) => Math.sign(value) * inner[axis]);
      const direction = unit.map(value => Math.sign(value) * roundedGrid[Math.round(Math.abs(value) * 4)]);
      const length = Math.hypot(...direction);
      const normal = direction.map(value => value / length);
      positions.setXYZ(i, ...corner.map((value, axis) => value + radius * normal[axis]));
      normals.setXYZ(i, ...normal);
    }
    geometry.computeBoundingSphere();
    solidGeometries.set(key, geometry);
    return geometry;
  }
  function box(parent, size, surface, position = [0, 0, 0], radius = .10) {
    return mesh(parent, solid(size, radius), surface, ...position);
  }
  function group(parent, x = 0, y = 0, z = 0) {
    const object = new T.Group();
    object.position.set(x, y, z);
    parent.add(object);
    return object;
  }
  function shadow(parent, width, length, x, z) {
    const object = mesh(parent, new T.PlaneGeometry(width, length), shadowMaterial, x, .014, z);
    object.rotation.x = -Math.PI / 2;
  }
  function texture(width, height, draw) {
    const image = document.createElement('canvas');
    image.width = width;
    image.height = height;
    draw(image.getContext('2d'));
    const map = new T.CanvasTexture(image);
    map.encoding = T.sRGBEncoding;
    map.anisotropy = Math.min(8, renderer.capabilities.getMaxAnisotropy());
    return new T.MeshBasicMaterial({ map });
  }
  const appFace = texture(540, 360, c => {
    c.fillStyle = '#132c46';
    c.fillRect(0, 0, 540, 360);
    c.fillStyle = '#1b4468';
    c.fillRect(24, 24, 492, 312);
    c.fillStyle = '#75c8ff';
    c.fillRect(52, 57, 436, 9);
    c.strokeStyle = '#8ed6ff';
    c.lineWidth = 12;
    c.strokeRect(52, 96, 436, 202);
    for (let i = 0; i < 3; i++) c.fillRect(104 + i * 128, 143, 78, 104);
  });
  const appointment = (preview, booked = false) => texture(1100, 640, c => {
    c.fillStyle = '#eaf3fb';
    c.fillRect(0, 0, 1100, 640);
    c.fillStyle = '#112b46';
    c.fillRect(0, 0, 1100, 90);
    c.fillStyle = '#e7f6ff';
    c.font = '600 44px sans-serif';
    c.fillText('Agenda de citas', 48, 59);
    c.fillStyle = '#1b4673';
    c.font = '600 46px sans-serif';
    c.fillText(booked ? 'Cita reservada' : 'Reserva tu cita', 56, 178);
    c.fillStyle = '#45617d';
    c.font = '32px sans-serif';
    c.fillText(booked ? 'Confirmada para las 10:30' : 'Selecciona un horario disponible', 56, 236);
    for (let i = 0; i < 3; i++) {
      c.fillStyle = i === 1 ? '#c4e6ff' : '#f9fcff';
      c.fillRect(56 + i * 333, 286, 294, 126);
      c.fillStyle = '#234e79';
      c.font = '600 44px sans-serif';
      c.fillText(['09:00', '10:30', '12:00'][i], 110 + i * 333, 363);
    }
    c.fillStyle = booked ? '#217456' : '#2374bf';
    c.fillRect(56, 469, 345, 96);
    c.fillStyle = '#fff';
    c.font = '600 36px sans-serif';
    c.fillText(booked ? 'Confirmada' : 'Reservar cita', 107, 530);
    c.fillStyle = '#476481';
    c.font = '29px sans-serif';
    if (preview) c.fillText('Entorno de pruebas', 751, 527);
  });
  function placard(parent, words, color, x, y, z, width = 1.75) {
    const face = texture(768, 192, c => {
      c.fillStyle = '#0b1b2e';
      c.fillRect(0, 0, 768, 192);
      c.fillStyle = color;
      c.fillRect(0, 185, 768, 7);
      c.font = '700 68px sans-serif';
      c.textAlign = 'center';
      c.fillText(words, 384, 122, 714);
    });
    const sign = group(parent, x, y, z);
    box(sign, [width + .05, width / 4 + .05, .08], steel, [0, 0, -.043]);
    mesh(sign, new T.PlaneGeometry(width, width / 4), face);
    return sign;
  }
  const testScreen = appointment(true);
  const testBooked = appointment(true, true);
  const liveScreen = appointment(false);
  const liveBooked = appointment(false, true);
  function appObject(parent, x, y, z) {
    const app = group(parent, x, y, z);
    box(app, [1.45, .97, .26], steel, [0, 0, 0], .12);
    box(app, [1.35, .87, .05], dark, [0, 0, .14]);
    mesh(app, new T.PlaneGeometry(1.23, .82), appFace, 0, 0, .171);
    return app;
  }
  const floor = mesh(scene, new T.PlaneGeometry(200, 200), material(0x0c172b, .34, .84));
  floor.rotation.x = -Math.PI / 2;
  const grid = new T.GridHelper(140, 140, 0x203a58, 0x182940);
  grid.position.y = .011;
  scene.add(grid);
  const sets = Array.from({ length: 9 }, () => group(scene));
  function platform(parent, x, z, width = 2.5, depth = 2, surface = blue) {
    shadow(parent, width + 1.5, depth + 1.5, x, z);
    box(parent, [width, .25, depth], dark, [x, .14, z], .115);
    box(parent, [width - .025, .043, depth - .025], steel, [x, .245, z]);
    box(parent, [width - .09, .1, depth - .09], navy, [x, .31, z]);
    box(parent, [width - .2, .025, .025], surface, [x, .365, z + depth / 2 - .06]);
  }
  function line(parent, x1, z1, x2, z2, y, surface = blue) {
    const dx = x2 - x1, dz = z2 - z1;
    const beam = box(parent, [Math.hypot(dx, dz), .028, .035], surface, [(x1 + x2) / 2, y, (z1 + z2) / 2]);
    beam.rotation.y = -Math.atan2(dz, dx);
    return beam;
  }
  function rack(parent, x, z, surface = blue) {
    platform(parent, x, z, 1.62, 1.52, surface);
    const rack = group(parent, x, .35, z);
    box(rack, [1.34, 2.74, .98], navy, [0, 1.37, 0], .17);
    box(rack, [1.12, .085, .79], steel, [0, 2.66, .03]);
    for (const side of [-1, 1]) {
      box(rack, [.072, 2.43, .15], steel, [side * .59, 1.35, .51]);
    }
    for (let i = 0; i < 5; i++) {
      box(rack, [.025, .052, .55], dark, [.671, .42 + i * .13, -.015]);
    }
    box(rack, [1.23, 2.59, .05], dark, [0, 1.37, .505]);
    const lights = [];
    for (let i = 0; i < 6; i++) {
      const y = .31 + i * .41;
      box(rack, [1.06, .3, .062], steel, [0, y, .54]);
      for (let vent = 0; vent < 3; vent++) {
        box(rack, [.49, .022, .018], dark, [-.15, y + (vent - 1) * .045, .578]);
      }
      lights.push(box(rack, [.065, .058, .023], surface, [.39, y, .585]));
    }
    return { rack, lights };
  }
  function gate(parent, x, surface = blue) {
    const object = group(parent, x, .36, 0);
    const arch = new T.CurvePath();
    arch.add(new T.LineCurve3(new T.Vector3(0,.12,-.9), new T.Vector3(0,2.16,-.9)));
    arch.add(new T.QuadraticBezierCurve3(new T.Vector3(0,2.16,-.9), new T.Vector3(0,2.45,-.9), new T.Vector3(0,2.45,-.61)));
    arch.add(new T.LineCurve3(new T.Vector3(0,2.45,-.61), new T.Vector3(0,2.45,.61)));
    arch.add(new T.QuadraticBezierCurve3(new T.Vector3(0,2.45,.61), new T.Vector3(0,2.45,.9), new T.Vector3(0,2.16,.9)));
    arch.add(new T.LineCurve3(new T.Vector3(0,2.16,.9), new T.Vector3(0,.12,.9)));
    mesh(object, new T.TubeGeometry(arch, 72, .135, 12, false), steel);
    for (const z of [-.9, .9]) {
      box(object, [.45,.19,.44], navy, [0,.105,z], .08);
      box(object, [.03,1.54,.038], surface, [.134,1.13,z]);
    }
    box(object, [.07,.06,1.2], surface, [.127,2.45,0]);
    return object;
  }
  function tablet(parent, x, z, scale = 1, screen = liveScreen) {
    const device = group(parent, x, .44, z);
    device.scale.setScalar(scale);
    box(device, [2.78, 1.72, .17], steel, [0, .93, -.025], .080);
    box(device, [2.68, 1.62, .03], dark, [0, .93, .065]);
    mesh(device, new T.PlaneGeometry(2.48, 1.44), screen, 0, .93, .084);
    return device;
  }
  function phone(parent, x, z) {
    platform(parent, x, z, 1.29, 1.24, mint);
    const device = group(parent, x, .36, z);
    box(device, [.89, 1.62, .17], steel, [0, .85, -.015], .080);
    box(device, [.79, 1.48, .03], dark, [0, .85, .08]);
    const screen = mesh(device, new T.PlaneGeometry(.71, .416), liveScreen, 0, .99, .1);
    box(device, [.64, .09, .01], blue, [0, .57, .1]);
    box(device, [.23, .025, .016], steel, [0, 1.51, .103]);
    box(device, [.038, .22, .08], steel, [.447, 1.04, -.015]);
    return screen;
  }

  const [hook, problem, reveal, deploy, security, operation, growth, payoff, closing] = sets;
  platform(hook, 0, 0, 4.9, 2.6);
  const demo = tablet(hook, 0, 0, 1.72, testScreen);
  const demoScreen = demo.children[2];
  const tap = mesh(demo, new T.RingGeometry(.033, .047, 40), blue, -.72, .48, .094);
  const publishGate = gate(hook, 3.45, amber);
  box(publishGate, [.12, 1.91, 1.66], dark, [0, 1.27, 0]);
  const pending = placard(hook, 'SIN PUBLICAR', '#ffd09d', 3.45, 2.28, 1.06, 1.52);
  const releasedApp = appObject(hook, 0, 1.48, 1);
  line(hook, .6, 0, 3.24, 0, .32);

  const workload = appObject(problem, .8, 1.37, 0);
  const workloadRack = rack(problem, -1.75, 0);
  const costBlocks = group(problem, -1.2, .27, 0);
  for (let i = 0; i < 7; i++) box(costBlocks, [1.7, .16, 1.5], i % 2 ? navy : steel, [0, i * .2, 0]);
  const costsFace = texture(512, 240, c => {
    c.fillStyle = '#152a41';
    c.fillRect(0, 0, 512, 240);
    c.fillStyle = '#ffd19d';
    c.font = '600 152px sans-serif';
    c.textAlign = 'center';
    c.fillText('$', 256, 169);
  });
  mesh(costBlocks, new T.PlaneGeometry(1.3, .62), costsFace, 0, .75, .761);
  const obstacle = gate(problem, -1.2, amber);
  const barrier = box(obstacle, [.12, 1.9, 1.64], dark, [0, 1.29, 0]);
  platform(problem, .7, 0);
  const problemStrip = box(problem, [4.6, .035, .045], amber, [-1.4, .39, .95]);

  platform(reveal, 0, 0, 8.7, 2.6);
  const checkpoints = [-2.3, 0, 2.3].map((x, i) => {
    gate(reveal, x);
    return placard(reveal, ['Código', 'Controles', 'Despliegue'][i], '#a8daff', x, 2.84, .25);
  });
  const laneLights = Array.from({ length:15 }, (_, i) => {
    const x = -4.05 + i * .57;
    return box(reveal, [.37, .025, .07], mint, [x, .39, .98]);
  });
  const guide = mesh(reveal, new T.SphereGeometry(.08, 18, 12), mint);
  guide.position.set(-4.25, .4, .8);
  line(reveal, -4.25, 0, 4.25, 0, .38);
  const pipelineApp = appObject(reveal, -4, 1.43, 0);

  platform(deploy, 0, 0, 1.9, 1.55);
  platform(deploy, 2.1, -1.5, 1.8, 1.35);
  platform(deploy, 2.1, 1.5, 1.8, 1.35, amber);
  const packageApp = appObject(deploy, -2.35, 1.17, 0);
  const testApp = appObject(deploy, 2.1, 1.1, -1.5);
  gate(deploy, 2.1, amber).position.z = 1.5;
  placard(deploy, 'PRUEBAS', '#97daff', 2.1, .56, -.82, 1.48);
  placard(deploy, 'PRODUCCIÓN', '#ffd09d', 2.1, .56, 2.19, 1.64);
  placard(deploy, 'VERSIÓN', '#97daff', 0, .56, .8, 1.26);
  line(deploy, -2.35, 0, 1, 0, .19);
  line(deploy, 1, -1.5, 1, 1.5, .19);
  line(deploy, 1, -1.5, 2.1, -1.5, .19);
  line(deploy, 1, 1.5, 2.1, 1.5, .19, amber);

  platform(security, 0, 0, 5, 2.35);
  gate(security, -.75);
  gate(security, .75);
  const scanDoor = box(security, [.09, 1.92, 1.64], dark, [.94, 1.4, 0]);
  const correction = placard(security, 'REVISAR', '#ffd09d', 0, 2.76, 1.17, 1.56);
  const passed = placard(security, 'CONTROLES OK', '#99eac7', 0, 2.76, 1.17, 1.7);
  const scannedApp = appObject(security, 0, 1.43, 0);
  const scanMaterial = new T.MeshBasicMaterial({ color: 0x5fbfff, transparent: true, opacity: .28, depthWrite: false });
  const scan = box(security, [.045, 2.05, 1.58], scanMaterial, [-1, 1.38, 0]);
  const scanGlow = new T.MeshBasicMaterial({ color:0x63d9ff, transparent:true, opacity:0, depthWrite:false });
  const scanStrip = box(security, [.065, .025, 2.04], scanGlow, [-1, .38, 0]);
  const risk = mesh(security, new T.OctahedronGeometry(.31), amber, .61, 2.27, .12);

  platform(operation, -1.55, 0, 2.4, 2.45);
  const live = tablet(operation, -1.55, 0, .82);
  const monitors = group(operation, 1.25, 0, -.5);
  const metric = [];
  for (let i = 0; i < 12; i++) metric.push(box(monitors, [.13, 1, .11], i === 7 ? amber : blue, [-.8 + i * .19, .8, .8]));
  box(monitors, [2.62, 1.69, .15], navy, [.21, 1.14, .56]);
  const alert = mesh(monitors, new T.OctahedronGeometry(.2), amber, 1.42, 2.04, .86);
  const signal = mesh(operation, new T.SphereGeometry(.09, 14, 10), mint, 0, .47, 0);
  const userScreen = phone(operation, 2.8, 1.6);
  const customer = userScreen.parent;
  placard(monitors, 'LATENCIA', '#a8daff', .22, 2.29, .77);
  const booking = placard(operation, 'CITA CONFIRMADA', '#9deac9', 2.8, 2.57, 1.7, 1.8);
  line(operation, -1.55, .8, 2.8, 1.6, .39, mint);

  const racks = [rack(growth, 0, 0), rack(growth, -1.86, .3, mint), rack(growth, 1.86, .3, mint)];
  for (let i = 0; i < 8; i++) line(growth, -3.1 + .86 * i, 2.1, 0, .68, .06, blue);
  const traffic = Array.from({ length: 10 }, () => mesh(growth, new T.SphereGeometry(.066, 10, 8), blue));

  platform(payoff, 0, 0, 2.9, 2.25);
  tablet(payoff, 0, 0, 1.05);
  phone(payoff, 2.31, .6).material = liveBooked;
  phone(payoff, 3.75, -.6);
  line(payoff, .9, .24, 2.31, .6, .38, mint);
  line(payoff, 2.31, .6, 3.75, -.6, .38, mint);
  const stack = rack(payoff, -2.9, -2.6).rack;

  for (let i = 0; i < 5; i++) {
    rack(closing, -3.2, -2.1 * i);
    rack(closing, 3.2, -2.1 * i);
  }
  line(closing, -1.8, 3.6, -1.8, -12, .03);
  line(closing, 1.8, 3.6, 1.8, -12, .03);
  const finalApp = appObject(closing, 0, 1.73, -3.7);

  const smooth = (value, start, end) => {
    const t = Math.max(0, Math.min(1, (value - start) / (end - start)));
    return t * t * (3 - 2 * t);
  };
  const mix = (a, b, t) => a + (b - a) * t;
  function aim(from, to, target, t) {
    camera.position.set(...from.map((value, i) => mix(value, to[i], t)));
    camera.lookAt(...target);
  }
  // A single, smooth push accents a few actions inside shots.
  const focusBeats = [[.76, .76, .6], [2.08, .82, 1.25], [32.88, 1.28, 1.05], [45.02, 1.7, .85]];
  function focusPush(seconds) {
    return focusBeats.reduce((zoom, [at, duration, amount]) => {
      const t = (seconds - at) / duration;
      return t > 0 && t < 1 ? zoom + amount * Math.sin(Math.PI * t) ** 2 : zoom;
    }, 0);
  }
  const starts = [0, 4.05, 12.65, 20.75, 29.25, 36.02, 42.28, 48.73, 53.08];
  const shots = [
    t => {
      const cut = t >= 1.72;
      demo.visible = !cut;
      demoScreen.material = t < .88 ? testScreen : testBooked;
      tap.visible = t >= .74 && t < .95;
      tap.scale.setScalar(1 + 2.4 * smooth(t, .74, .95));
      releasedApp.visible = cut;
      publishGate.visible = cut;
      pending.visible = cut;
      releasedApp.position.x = mix(-.7, 2.48, smooth(t, 1.72, 2.14));
      releasedApp.rotation.y = .18 + .18 * smooth(t, 1.72, 2.18);
      if (cut) aim([6.5, 4.2, 9.5], [5.6, 3.8, 8.9], [1.4, 1.78, 0], smooth(t, 1.72, 3.95));
      else aim([1.6, 3.15, 8.5], [.68, 2.9, 8.05], [0, 2.2, 0], smooth(t, 0, 1.72));
    },
    t => {
      const phase = t < 2.04 ? 0 : t < 3.33 ? 1 : 2;
      workloadRack.rack.parent.visible = true;
      workloadRack.rack.visible = phase === 0;
      costBlocks.visible = phase === 1;
      obstacle.visible = phase === 2;
      costBlocks.children.slice(0, 7).forEach((block, i) => {
        block.position.y = i * .2 + 3.5 * (1 - smooth(t, 2.04 + i * .083, 2.24 + i * .083));
      });
      barrier.position.y = mix(3.7, 1.29, smooth(t, 3.33, 3.65));
      workload.position.x = mix(1.4, -.05, smooth(t, 3.27, 3.69)) + .4 * smooth(t, 3.69, 4.05);
      problemStrip.scale.x = mix(.65, 1.2, smooth(t, 4.5, 7.8));
      if (phase === 0) aim([-3.5, 3.15, 7.4], [-2.9, 3.05, 7.05], [-.45, 1.8, 0], smooth(t, 0, 2.04));
      if (phase === 1) aim([1.7, 4.7, 6.5], [2.6, 3.55, 6.1], [-.4, 1.66, 0], smooth(t, 2.04, 3.33));
      if (phase === 2) aim([3.3, 3.75, 7.1], [5.1, 4.45, 8.45], [-.45, 1.8, 0], smooth(t, 3.33, 8.6));
    },
    t => {
      pipelineApp.position.x = mix(-4.05, 3.95, smooth(t, .8, 7.35));
      guide.position.x = pipelineApp.position.x;
      laneLights.forEach(lamp => { lamp.visible = lamp.position.x <= pipelineApp.position.x; });
      checkpoints.forEach((label, i) => {
        label.position.y = 2.84 + .12 * smooth(pipelineApp.position.x, -2.8 + i * 2.3, -2.3 + i * 2.3);
      });
      pipelineApp.rotation.y = mix(.4, .04, smooth(t, 1, 7.5));
      aim([6.4, 4.9, 10.6], [-3.55, 4.1, 11.6], [0, 1.8, 0], smooth(t, 0, 8.1));
    },
    t => {
      packageApp.position.x = mix(-2.35, 0, smooth(t, .42, 2.1));
      testApp.position.x = mix(0, 2.1, smooth(t, 2.1, 3.55));
      testApp.position.z = -1.5 * smooth(t, 2.1, 3.55);
      testApp.scale.setScalar(smooth(t, 2.1, 2.6));
      aim([-4.2, 4.15, 8.9], [4.55, 6.95, 8.8], [.45, 1.28, 0], smooth(t, .3, 7.95));
    },
    t => {
      scannedApp.position.x = mix(-1.95, 0, smooth(t, .12, 1.32)) + 2.65 * smooth(t, 5.57, 6.57);
      scan.position.x = mix(-1.18, 1.18, smooth(t, 1.34, 3.8));
      scanMaterial.opacity = .28 * (smooth(t, .75, 1.25) - smooth(t, 3.75, 4.14));
      scanStrip.position.x = scan.position.x;
      scanGlow.opacity = Math.min(1, scanMaterial.opacity * 3.4);
      risk.scale.setScalar(smooth(t, 3.64, 4.05) - smooth(t, 5.12, 5.6));
      risk.rotation.y = t * 1.7;
      scanDoor.position.y = mix(1.4, 3.45, smooth(t, 5.18, 5.61));
      scanDoor.visible = t < 5.62;
      correction.visible = t >= 3.55 && t < 5.41;
      passed.visible = t >= 5.41;
      aim([-3.4, 3.7, 8.1], [3.65, 3.3, 7.1], [0, 1.84, 0], smooth(t, 0, 6.77));
    },
    t => {
      live.rotation.y = -.13;
      metric.forEach((bar, i) => {
        const height = (.36 + .12 * Math.sin(i * 2.8 + t * 2) + (i === 7 ? .7 : 0)) * smooth(t, .85 + i * .082, 1.2 + i * .082);
        bar.scale.y = Math.max(.01, height);
        bar.position.y = .53 + height / 2;
      });
      alert.scale.setScalar(smooth(t, 2.04, 2.37));
      alert.rotation.y = t * 1.2;
      const progress = smooth(t, 3.76, 5.4);
      signal.visible = t > 3.76;
      userScreen.material = t < 5.37 ? liveScreen : liveBooked;
      signal.position.set(mix(-1.55, 2.8, progress), .46, mix(.8, 1.6, progress));
      booking.visible = t >= 5.37;
      const close = smooth(t, 4.02, 4.84);
      customer.scale.setScalar(1 + .16 * close);
      monitors.visible = t < 4.02;
      live.visible = t < 4.02;
      if (t < 4.02) {
        aim([-3.2, 4.4, 8.8], [-1, 4.05, 8.5], [.55, 1.67, .2], smooth(t, .25, 3.85));
      } else {
        aim([2.8, 3.25, 7.75], [3.5, 3.15, 6.8], [2.66, 1.67, 1.6], close);
      }
    },
    t => {
      racks.forEach(({ rack, lights }, i) => {
        const progress = i === 0 ? 1 : smooth(t, 2.1 + i * .61, 2.76 + i * .61);
        rack.position.y = mix(-2.65, .35, progress);
        lights.forEach((lamp, j) => { lamp.visible = (t * 3 + j * 1.37) % 5 < 4.2; });
      });
      traffic.forEach((particle, i) => {
        const progress = (t * (.64 + .055 * i) + i * .17) % 1;
        particle.visible = i < 3 + t * 1.7;
        particle.position.set(mix(-3.1 + .69 * i, 0, progress), .075, mix(2.1, .68, progress));
      });
      aim([1.2, 2.65, 5.95], [-2.6, 4.65, 10.1], [0, 1.78, 0], smooth(t, 1.7, 5.73));
    },
    t => {
      stack.position.x = mix(-2.9, -5.3, smooth(t, .08, 1.47));
      aim([-2.4, 3.4, 8], [4.15, 4.05, 8.65], [.75, 1.62, 0], smooth(t, .08, 4.35));
    },
    t => {
      finalApp.position.z = mix(-3.7, -6.1, smooth(t, 0, 2.7));
      finalApp.rotation.y = .5 * smooth(t, 0, 2.7);
      const travel = smooth(t, 0, 9.92);
      aim([.85, 2.52, 6.6], [.1, 2.3, .1], [0, 1.72, -6.8], travel);
    }
  ];
  return function render(seconds) {
    let shot = starts.length - 1;
    while (shot > 0 && seconds < starts[shot]) shot--;
    sets.forEach((set, i) => { set.visible = i === shot; });
    const local = seconds - starts[shot];
    shots[shot](local);
    const opening = shot === 0 && local < 1.72;
    camera.fov = opening ? 37 : [2, 3, 7].includes(shot) ? 45 : shot === 8 ? 35 : 42;
    camera.clearViewOffset();
    camera.fov -= focusPush(seconds);
    const drift = Math.sin(seconds * .83);
    key.position.x = -5 + 2.2 * drift;
    rim.intensity = 2.35 + .38 * Math.cos(seconds * 1.17);
    camera.updateProjectionMatrix();
    renderer.render(scene, camera);
  };
};
