import { chromium } from '/mnt/datos/Jesus Garcia/infra/evolut-idp-ui-v2/node_modules/playwright/index.mjs';
const [out, total, speed, warm] = [process.argv[2], +process.argv[3], +process.argv[4], +process.argv[5]];
const browser = await chromium.launch({ headless: false, args: ['--ignore-gpu-blocklist', '--window-size=1920,1080'] });
const page = await (await browser.newContext({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 2, colorScheme: 'dark' })).newPage();
await page.addInitScript(() => {
  // virtual clock: the hall only advances when we step it
  let now = 0, id = 0; const cbs = new Map();
  const t0 = Date.now();
  performance.now = () => now; Date.now = () => t0 + now;
  window.requestAnimationFrame = (cb) => { cbs.set(++id, cb); return id; };
  window.cancelAnimationFrame = (i) => cbs.delete(i);
  window.__step = (dt) => { now += dt; const l = [...cbs.values()]; cbs.clear(); for (const cb of l) cb(now); };
  const s = document.createElement('style');
  s.textContent = 'main, .hall-scrim, button { opacity: 0 !important; } * { transition: none !important; }';
  document.addEventListener('DOMContentLoaded', () => document.head.appendChild(s));
});
// local capture only: lift the corridor's 30 fps render cap so every stepped frame is drawn
await page.route(/CorridorScene/, async (route) => {
  const res = await route.fetch();
  const src = await res.text(); const body = src.replace('<32.333333333333336||', '<0||').replace('this.last=t-n%Bn,', 'this.last=t,');
  console.log('patched', route.request().url(), src !== body);
  await route.fulfill({ response: res, body });
});
await page.goto('https://console.evolut.cloud/login', { waitUntil: 'networkidle' });
await page.waitForTimeout(6000);
const FPS = +(process.argv[6] || 30); const START = +(process.argv[7] || 0); const dt = 1000 / FPS * speed;
for (let i = 0; i < warm * 30; i++) await page.evaluate((d) => window.__step(d), 1000 / 30);
await page.waitForTimeout(1500);
for (let f = 0; f < total * FPS; f++) {
  await page.evaluate((d) => window.__step(d), dt);
  if (f < START) continue;
  await page.screenshot({ path: `${out}/f${String(f).padStart(5, '0')}.jpg`, type: 'jpeg', quality: 95 });
  if (f % 600 === 0) console.log('frame', f);
}
await browser.close();
