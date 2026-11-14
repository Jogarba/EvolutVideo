# SPEC.md — Evolut Commercial Brand Film & Product Spot (48.0s)

## 1. GOAL
Deliver a 48.0-second cinematic commercial brand spot for **Evolut** (`evolut.cloud`) that sells Evolut as a product and platform partner (*"Tú construyes. Evolut lo lleva a producción"*, *"El equipo de plataforma que no tienes"*), structured around Evolut's official 6-stage hexagonal brand narrative (`brand-strategy.md` §3 & `brand-messaging.md` §1–§4). Powered by **HyperFrames**, **OpenMontage** (`hyperframes-creative`, `hyperframes-animation`, `hyperframes-media`), **MoCha** (`Orange-3DV-Team/MoCha` spokesperson slot), **Taste Skill (`design-taste-frontend`)**, and **Anti-Slop (`antislop`)**.

## 2. OUTPUT
- **Resolution:** `1920x1080` (16:9 Full HD)
- **Frame Rate:** `30 fps` (`1440` frames total)
- **Duration:** `48.0s`
- **Audio:**
  - 6 synchronized neural Spanish commercial voiceover tracks (`assets/vo-01.mp3` .. `assets/vo-06.mp3`, `es-CO-GonzaloNeural`)
  - Continuous beat-synced electronic commercial soundtrack + transition chimes (`assets/evolut-commercial-bed.mp3`)

## 3. LOOK (Official Evolut Brand Tokens — `evolut-tokens.css`)
- **Canvas Background (`--bg`):** `#070c10`
- **Surface (`--surface`):** `#0e1318`
- **Raised Card (`--surface-raised`):** `#161b20`
- **Primary Brand Blue (`--brand`):** `#399fef`
- **Text on Brand Fill (`--brand-text-on`):** `#000e1d` (WCAG AA `6.83:1` — never white on `#399fef`)
- **Primary Ink (`--text`):** `#f2f5f7`
- **Secondary Ink (`--text-secondary`):** `#939aa3`
- **Semantic Status:** `#3dd68c` (Active/Ready), `#f0b429` (Scaling/Demand), `#70b8ff` (Highlight)
- **Typography:**
  - Display / Headlines: `Michroma` (`assets/fonts/michroma-400.woff2`)
  - Body / Commercial Copy: `Hanken Grotesk Variable` (`assets/fonts/hanken-grotesk-latin.woff2`)
  - Labels / Badges: `JetBrains Mono Variable` (`assets/fonts/jetbrains-mono-latin.woff2`)

## 4. MOTION & OPENMONTAGE 6-LAYER COMPOSITION MODEL
- **Layer 1 (Background):** Deep `#070c10` canvas with subtle radial light source shifting per scene.
- **Layer 2 (Environment):** Isometric hexagonal blueprint grid + ambient depth lines.
- **Layer 3 (Visual Metaphor / Product Stage):** High-craft animated SVG/DOM visual metaphors for each of the 6 hexagonal stages + clean high-level `Evolut Console` overview in Stage 4.
- **Layer 4 (Kinetic Typography):** High-impact commercial headlines (`Michroma`) and concise benefit copy (`Hanken Grotesk`).
- **Layer 5 (Voiceover Captions & Progress HUD):** Synchronized commercial subtitle bar + 6-stage hexagonal progress indicator.
- **Layer 6 (Vignette & Polish):** Subtle edge vignette framing the 1920x1080 stage.

## 5. SHOTS (6-Stage Hexagonal Commercial Narrative)
1. **Shot 1 (`0.0s – 6.3s`, `6.3s`):** *01 · Impulso — Todo empieza con una idea*
   - Visual Metaphor: Glowing electric spark igniting a precision hexagonal blueprint core with expanding light rings.
   - Voiceover & Copy: *"Todo empieza con una idea. Tú la creas. Nosotros la impulsamos."*
2. **Shot 2 (`6.3s – 14.5s`, `8.2s`):** *02 · Construcción con Criterio — Materializamos tu idea*
   - Visual Metaphor: Precision automated golden-path assembly line transforming raw blocks (`Piensa -> Crea -> Codea -> Despliega`) into a live application without manual infrastructure plumbing.
   - Voiceover & Copy: *"Materializamos tu idea. Piensa, crea, codea y despliega tu primera versión, sin armar la infraestructura."*
3. **Shot 3 (`14.5s – 24.1s`, `9.6s`):** *03 · Entrega con Red — Tu fábrica de aplicaciones*
   - Visual Metaphor: Isolated on-demand hexagonal workspace capsules (`Producción`, `Workspace Pruebas`, `Workspace Demo Cliente`) spinning up independently with protective isolation shields.
   - Voiceover & Copy: *"Tu fábrica de aplicaciones. Crea tu workspace bajo demanda, aislando tus aplicaciones para pruebas o demostraciones, sin afectar tu operación."*
4. **Shot 4 (`24.1s – 32.1s`, `8.0s`):** *04 · Operación a la Vista — Gestionamos tu infraestructura*
   - Visual Metaphor: Clean, high-level overview of `Evolut Console` (applications catalog, version selector from GitHub releases, 3D hexagonal connection line, real-time indicator, and 1-click rollback button — zero technical lecture jargon).
   - Voiceover & Copy: *"Gestionamos tu infraestructura. Ve tus aplicaciones en tiempo real en un solo lugar, y vuelve a cualquier versión en un clic."*
5. **Shot 5 (`32.1s – 38.4s`, `6.3s`):** *05 · Recursos Bien Usados — Optimizamos tus recursos*
   - Visual Metaphor: Smooth, luminous harmonic wave that rises organically when real user activity arrives and rests peacefully when demand subsides.
   - Voiceover & Copy: *"Optimizamos tus recursos. Tu aplicación escala cuando hace falta, no antes."*
6. **Shot 6 (`38.4s – 48.0s`, `9.6s`):** *06 · Cuidamos tu Bolsillo & Cierre de Marca*
   - Visual Metaphor: Smooth cost curve descending and stabilizing into a calm horizontal line + MoCha spokesperson stage (`data-slot="mocha-presenter"`) + official `evolut-isologo-on-dark.svg` lockup + commercial CTA (`Agendar demostración · evolut.cloud`).
   - Voiceover & Copy: *"Cuidamos tu bolsillo. Tú construyes. Evolut lo lleva a producción. El equipo de plataforma que no tienes."*

## 6. BANNED (Anti-Slop R-01..R-40 & Brand Voice §4 "Fuente o fuera")
- Zero unverified or invented numbers, dollar figures, percentages, latencies, or SLA promises (`+$18,500`, `-68%`, `99.99%`, `100% SLA`, `12ms`, `40%` strictly forbidden).
- Zero technical university-lecture jargon (`CPU`, `RAM`, `p95`, `Pods`, `K8s`, `YAML`, `POST /checkout`, `Tempo`, `Mimir`, `Pyroscope`).
- Zero em-dashes (`—`) in user-facing copy (R-02).
- Zero white text on `#399fef` fill (always `#000e1d`).
