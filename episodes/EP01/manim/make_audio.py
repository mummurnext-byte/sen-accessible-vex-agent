from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

import edge_tts
import numpy as np
from scipy.io import wavfile


VOICE = "en-US-BrianMultilingualNeural"


async def make_voice(text_path: Path, output_path: Path, rate: str) -> None:
    text = text_path.read_text(encoding="utf-8").strip()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate=rate,
        pitch="+2Hz",
        volume="+0%",
    )
    await communicate.save(str(output_path))


def make_music(output_path: Path, duration: float = 70.0, sample_rate: int = 44_100) -> None:
    """Create an original restrained technology bed without third-party audio."""
    t = np.arange(int(duration * sample_rate), dtype=np.float64) / sample_rate
    music = np.zeros_like(t)

    # Slow minor pad with a subtle stereo-safe pulse.
    for frequency, weight, phase in ((130.81, 0.30, 0.0), (155.56, 0.22, 0.7), (196.0, 0.18, 1.4)):
        lfo = 0.62 + 0.18 * np.sin(2 * np.pi * 0.08 * t + phase)
        music += weight * lfo * np.sin(2 * np.pi * frequency * t + phase)

    # Half-second arpeggio notes provide movement while leaving space for speech.
    notes = (261.63, 311.13, 392.0, 466.16, 392.0, 311.13)
    step = 0.5
    for index in range(int(duration / step)):
        start = int(index * step * sample_rate)
        length = min(int(0.42 * sample_rate), len(t) - start)
        if length <= 0:
            continue
        local = np.arange(length, dtype=np.float64) / sample_rate
        envelope = (1 - np.exp(-local * 24)) * np.exp(-local * 5.5)
        tone = 0.12 * envelope * np.sin(2 * np.pi * notes[index % len(notes)] * local)
        music[start : start + length] += tone

    # A soft low pulse marks each two-second visual beat.
    for start_seconds in np.arange(0, duration, 2.0):
        start = int(start_seconds * sample_rate)
        length = min(int(0.32 * sample_rate), len(t) - start)
        local = np.arange(length, dtype=np.float64) / sample_rate
        pulse = 0.18 * np.exp(-local * 11) * np.sin(2 * np.pi * 62 * local)
        music[start : start + length] += pulse

    fade = int(1.8 * sample_rate)
    music[:fade] *= np.linspace(0, 1, fade)
    music[-fade:] *= np.linspace(1, 0, fade)
    peak = max(float(np.max(np.abs(music))), 1e-6)
    music = np.clip(music / peak * 0.62, -1, 1)
    stereo = np.column_stack((music, music * 0.97))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    wavfile.write(output_path, sample_rate, (stereo * 32767).astype(np.int16))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=Path, required=True)
    parser.add_argument("--voice", type=Path, required=True)
    parser.add_argument("--music", type=Path, required=True)
    parser.add_argument("--rate", default="-25%")
    parser.add_argument("--duration", type=float, default=70.0)
    args = parser.parse_args()
    asyncio.run(make_voice(args.text, args.voice, args.rate))
    make_music(args.music, duration=args.duration)


if __name__ == "__main__":
    main()
