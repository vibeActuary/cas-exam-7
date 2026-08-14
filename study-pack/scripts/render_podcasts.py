#!/usr/bin/env python3
"""Render two-host podcast markdown to MP3 via edge-tts + ffmpeg."""

from __future__ import annotations

import asyncio
import re
import sys
import tempfile
from pathlib import Path

try:
    import edge_tts
except ImportError:
    sys.stderr.write("pip install edge-tts\n")
    raise

ROOT = Path(__file__).resolve().parents[1]
PODCASTS = ROOT / "podcasts"
AUDIO = ROOT / "audio"

# Two distinct English voices. Swap if you prefer.
VOICES = {
    "Riley": "en-US-JennyNeural",
    "Sam": "en-US-GuyNeural",
}

LINE = re.compile(r"^\*\*(Riley|Sam):\*\*\s*(.*)$")


def parse_script(path: Path) -> list[tuple[str, str]]:
    turns: list[tuple[str, str]] = []
    speaker: str | None = None
    buf: list[str] = []

    def flush() -> None:
        nonlocal speaker, buf
        if speaker and buf:
            text = " ".join(buf).strip()
            if text:
                turns.append((speaker, text))
        speaker, buf = None, []

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("#") or line.startswith("---") or line.startswith("**Hosts:**"):
            continue
        if line.startswith("**Length:**") or line.startswith("**Tasks:**") or line.startswith("**Paper"):
            continue
        m = LINE.match(line)
        if m:
            flush()
            speaker, rest = m.group(1), m.group(2)
            buf = [rest] if rest else []
            continue
        if speaker and line:
            buf.append(line)
    flush()
    return turns


async def synth_turn(text: str, voice: str, dest: Path) -> None:
    comm = edge_tts.Communicate(text, voice)
    await comm.save(str(dest))


async def render_one(md: Path) -> Path | None:
    turns = parse_script(md)
    if not turns:
        print(f"skip (no dialogue): {md.name}")
        return None
    out = AUDIO / (md.stem + ".mp3")
    AUDIO.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        parts: list[Path] = []
        for i, (who, text) in enumerate(turns):
            part = tmp / f"{i:03d}.mp3"
            await synth_turn(text, VOICES[who], part)
            parts.append(part)
        concat = tmp / "list.txt"
        concat.write_text("".join(f"file '{p}'\n" for p in parts), encoding="utf-8")
        import subprocess

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                str(concat),
                "-c",
                "copy",
                str(out),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    print(f"wrote {out.name} ({len(turns)} turns)")
    return out


async def main() -> None:
    names = sys.argv[1:]
    files = (
        [PODCASTS / n if n.endswith(".md") else PODCASTS / f"{n}.md" for n in names]
        if names
        else sorted(PODCASTS.glob("*.md"))
    )
    for md in files:
        if not md.exists():
            print(f"missing {md}")
            continue
        await render_one(md)


if __name__ == "__main__":
    asyncio.run(main())
