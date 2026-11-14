import sys; sys.path.insert(0, sys.path[0])
from common import *
L = 6.4          # each station's slot; hosts run 0.6 s longer so pushes overlap
OUTT = L - 0.3
def write(cid, css, hero, js, n, label, h1, h2, sub=None, exit_js=None):
    body = f'''    <div class="world" id="world"><div id="cam"><div id="drift">
{station(n, label, h1, h2)}
      <div class="hero" id="hero"><div id="hero-in">{hero}</div></div>
    </div></div></div>
    <div id="st-streak"></div><div id="st-flash"></div>'''
    open(OUT + cid + ".html", "w").write(scene(cid, STATION_CSS + SPOT_CSS + css, body, STATION_IN + RIG_JS + station_fx(n) + js + (exit_js if exit_js is not None else station_out(OUTT))))
