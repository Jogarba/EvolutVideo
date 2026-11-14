import sys, json, os; sys.path.insert(0, sys.path[0])
from common import VO, FONTS, OUT
# Subtle subtitles in the bottom letterbox bar, one phrase at a time, each word lighting up as it is spoken.
order = ["hook", "problem", "reveal", "fast", "secure", "always", "grows", "outcome", "cta"]
groups = []
for line in order:
    words = json.load(open(os.path.join(os.path.dirname(OUT.rstrip("/")), "assets", "vo", f"{line}.words.json")))
    cur = []
    for k, w in enumerate(words):
        cur.append(w)
        nxt = words[k + 1] if k + 1 < len(words) else None
        gap = (nxt["t"] - (w["t"] + w["d"])) if nxt else 9
        if not nxt or len(cur) >= 6 or gap > 0.15 or (len(cur) >= 3 and w["w"][-1] in ",.:;…?"):
            groups.append([(x["w"], VO[line] + x["t"], VO[line] + x["t"] + x["d"]) for x in cur]); cur = []
html, js = [], []
for g, words in enumerate(groups):
    start = words[0][1] - 0.08
    end = words[-1][2] + 0.3
    if g + 1 < len(groups): end = min(end, groups[g + 1][0][1] - 0.1)
    html.append(f'<div class="cg" id="cg{g}">' + ' '.join(f'<span id="cw{g}_{i}">{w}</span>' for i, (w, _, _) in enumerate(words)) + '</div>')
    js.append(f'tl.fromTo("#cg{g}", {{ opacity: 0, y: 8 }}, {{ opacity: 1, y: 0, duration: 0.18, ease: "power2.out" }}, {start:.3f});')
    for i, (_, t, _) in enumerate(words):
        js.append(f'tl.to("#cw{g}_{i}", {{ color: "#ffffff", duration: 0.12 }}, {t:.3f});')
    js.append(f'tl.to("#cg{g}", {{ opacity: 0, duration: 0.12, ease: "power2.in" }}, {end - 0.12:.3f});')
    js.append(f'tl.set("#cg{g}", {{ opacity: 0, visibility: "hidden" }}, {end:.3f});')
page = f'''<template>
  <style>{FONTS}
    #root {{ position: absolute; inset: 0; pointer-events: none; }}
    .cg {{ position: absolute; left: 0; right: 0; top: 958px; text-align: center; font: 500 30px "Hanken Grotesk Variable", sans-serif; letter-spacing: .3px; color: rgba(191,195,199,.55); opacity: 0; overflow: visible; }}
    .cg span {{ display: inline-block; }}
  </style>
  <div id="root" data-composition-id="captions" data-width="1920" data-height="1080">
    {''.join(html)}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join("    " + x for x in js)}
    window.__timelines["captions"] = tl;
  </script>
</template>
'''
open(OUT + "captions.html", "w").write(page)
print(len(groups), "caption groups")
