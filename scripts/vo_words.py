import asyncio, json, sys
import edge_tts
async def main(text, out_mp3, out_json):
    voice = sys.argv[4] if len(sys.argv) > 4 else "es-CO-GonzaloNeural"
    rate = sys.argv[5] if len(sys.argv) > 5 else "-4%"
    c = edge_tts.Communicate(text, voice, rate=rate, boundary="WordBoundary")
    words = []
    with open(out_mp3, "wb") as f:
        async for ch in c.stream():
            if ch["type"] == "audio": f.write(ch["data"])
            elif ch["type"] == "WordBoundary":
                words.append({"w": ch["text"], "t": ch["offset"] / 1e7, "d": ch["duration"] / 1e7})
    json.dump(words, open(out_json, "w"), ensure_ascii=False)
asyncio.run(main(sys.argv[1], sys.argv[2], sys.argv[3]))
