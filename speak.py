#!/usr/bin/env python3
"""
speak.py — speak German text using Microsoft Edge TTS
Usage: python3 speak.py "Guten Morgen!"
       python3 speak.py "Hello" --lang en   # English voice
"""
import asyncio
import sys
import tempfile
import os
import subprocess
import argparse

GERMAN_VOICE = "de-DE-ConradNeural"   # male, natural
ENGLISH_VOICE = "en-US-GuyNeural"

async def speak(text: str, voice: str):
    import edge_tts
    tts = edge_tts.Communicate(text, voice)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        tmp = f.name
    await tts.save(tmp)
    subprocess.run(["afplay", tmp], check=True)
    os.unlink(tmp)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    parser.add_argument("--lang", choices=["de", "en"], default="de")
    args = parser.parse_args()
    voice = GERMAN_VOICE if args.lang == "de" else ENGLISH_VOICE
    asyncio.run(speak(args.text, voice))

if __name__ == "__main__":
    main()
