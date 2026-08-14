# Audio

18 MP3s, about **85 minutes** total, ~30 MB. Two neural voices (Riley / Sam) via `edge-tts`. Open `playlist.m3u` in any phone player.

This is not Google NotebookLM. The voices are clean but not “two hosts in a studio.” For that, paste each `podcasts/*.md` into NotebookLM after you land.

## If there are no MP3s, or you want better voices

**Best quality:** paste each `podcasts/*.md` file into [NotebookLM](https://notebooklm.google.com) as a source and generate an Audio Overview. The scripts are already a two-host conversation.

**Offline / scripted:** from this directory, with Python 3 and ffmpeg:

```bash
pip install edge-tts
python3 ../scripts/render_podcasts.py
```

That renders Riley and Sam as two different Edge voices and concatenates them into `NN-name.mp3`.

**Last resort on a laptop:** macOS `say`, or any TTS app that can read a markdown file aloud. Strip the header and the `**Sam:**` / `**Riley:**` labels first.

## Suggested flight playlist

00, 01, 02, 03, 08, 15, 16, 17 if you only have a short hop. Full series is 00–17 in order.
