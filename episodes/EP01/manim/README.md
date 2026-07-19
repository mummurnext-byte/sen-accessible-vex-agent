# EP01 Manim Production

This folder contains the independent full stick-figure animation version of
Episode 01. It does not depend on the ChatCut timeline.

## Visual Specification

- 1080x1920, 30 fps, approximately 70 seconds
- dark charcoal `#1E1E1E` background
- white stick-figure teacher
- Input `#00D2FF`, Brain `#FFD700`, Output `#BD00FF`
- Thai is the primary, larger caption line
- English is the smaller reference caption line
- the robot section is explicitly presented as a simulation

## Local Setup

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install manim edge-tts
```

The render script uses the local FFmpeg binary configured near the top of
`render_ep01.ps1`. No API key or account credential is required.

## Render

From the repository root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\episodes\EP01\manim\render_ep01.ps1
```

The final review file is written to:

```text
exports/Silent_Sparks_EP01_Manim_Version_C.mp4
```

The English narration uses a gentle male neural voice. The background music is
generated locally from synthesized tones and does not contain third-party audio.
