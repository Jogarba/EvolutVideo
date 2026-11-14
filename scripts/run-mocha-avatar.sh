#!/usr/bin/env bash
# ==============================================================================
# Evolut Pitch Deck — MoCha (Orange-3DV-Team/MoCha) Character Replacement Runner
# Repository: https://github.com/Orange-3DV-Team/MoCha
# ==============================================================================
# Replaces a driving speaker video with a reference character portrait without masks
# using MoCha's Wan2.1 14B DiT backbone, and writes the resulting clip to:
#   assets/mocha-presenter.mp4
# Once present, the HyperFrames composition automatically displays the live video
# inside the [data-slot="mocha-presenter"] spokesperson stage in Scene 6.
#
# Hardware requirement: ~28 GB VRAM locally (Wan2.1-T2V-14B) or cloud GPU.
# ==============================================================================
set -euo pipefail

DRIVING_VIDEO="${1:-}"
CHARACTER_IMAGE="${2:-}"
MOCHA_DIR="${MOCHA_DIR:-/opt/MoCha}"
OUT_FILE="$(cd "$(dirname "$0")/.." && pwd)/assets/mocha-presenter.mp4"

if [[ -z "$DRIVING_VIDEO" || -z "$CHARACTER_IMAGE" ]]; then
  echo "Usage: $0 <driving_video.mp4> <character_portrait.png>"
  echo ""
  echo "Options:"
  echo "  1. Local GPU (>=28GB VRAM): Set MOCHA_DIR=/path/to/MoCha and run this script."
  echo "  2. Pre-rendered MoCha / HeyGen / Kling clip: Copy any 16:9 or 1:1 presenter"
  echo "     MP4 directly to: $OUT_FILE"
  echo "     and re-run: npx hyperframes render -o evolut-launch.mp4"
  exit 1
fi

if [[ ! -d "$MOCHA_DIR" ]]; then
  echo "[MoCha] Cloning Orange-3DV-Team/MoCha into $MOCHA_DIR..."
  git clone https://github.com/Orange-3DV-Team/MoCha.git "$MOCHA_DIR"
fi

echo "[MoCha] Running maskless Wan2.1 14B character replacement..."
python3 "$MOCHA_DIR/inference_mocha.py" \
  --video_path "$DRIVING_VIDEO" \
  --image_path "$CHARACTER_IMAGE" \
  --output_path "$OUT_FILE"

echo "[MoCha] Done -> $OUT_FILE"
