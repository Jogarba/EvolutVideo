"""Regenerate the per-scene Spanish voice tracks and their word timings.
Requires edge-tts in the selected Python environment.
"""
import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "narration.json").read_text(encoding="utf-8"))
for line in data["lines"]:
    subprocess.run([sys.executable, str(ROOT / "scripts/vo_words.py"), line["text"], str(ROOT / "assets/vo" / f"{line['id']}.mp3"), str(ROOT / "assets/vo" / f"{line['id']}.words.json"), data["voice"], data.get("rate", "+0%")], cwd=ROOT, check=True)
    print("Generated", line["id"])
subprocess.run([sys.executable, str(ROOT / "scripts/scenes/captions.py")], cwd=ROOT, check=True)
