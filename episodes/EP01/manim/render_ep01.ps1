$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..\..")
$python = Join-Path $repoRoot ".venv\Scripts\python.exe"
$manim = Join-Path $repoRoot ".venv\Scripts\manim.exe"
$ffmpeg = "C:\Users\User\AppData\Local\Temp\mummur-voice-tools\node_modules\.pnpm\ffmpeg-static@5.3.0\node_modules\ffmpeg-static\ffmpeg.exe"
$build = Join-Path $PSScriptRoot "build"
$media = Join-Path $PSScriptRoot "media"
$exports = Join-Path $repoRoot "exports"
$narration = Join-Path $build "narration.mp3"
$music = Join-Path $build "technology-bed.wav"
$silentVideo = Join-Path $media "videos\ep01_silent_sparks\1920p30\SilentSparksEP01.mp4"
$output = Join-Path $exports "Silent_Sparks_EP01_Manim_Version_C.mp4"

if (!(Test-Path $python) -or !(Test-Path $manim)) {
    throw "Run: py -3.11 -m venv .venv; .\.venv\Scripts\python.exe -m pip install manim edge-tts"
}
if (!(Test-Path $ffmpeg)) {
    throw "FFmpeg was not found at the configured local path. Update `$ffmpeg in render_ep01.ps1."
}

New-Item -ItemType Directory -Force $build, $media, $exports | Out-Null
$env:PATH = "$(Split-Path $ffmpeg);$env:PATH"

& $python (Join-Path $PSScriptRoot "make_audio.py") `
    --text (Join-Path $PSScriptRoot "narration_en.txt") `
    --voice $narration `
    --music $music
if ($LASTEXITCODE -ne 0) { throw "Audio generation failed with exit code $LASTEXITCODE." }

& $manim -qh --fps 30 --media_dir $media (Join-Path $PSScriptRoot "ep01_silent_sparks.py") SilentSparksEP01
if ($LASTEXITCODE -ne 0) { throw "Manim render failed with exit code $LASTEXITCODE." }

& $ffmpeg -y `
    -i $silentVideo `
    -i $narration `
    -i $music `
    -filter_complex "[1:a]adelay=2000|2000,volume=1.0[voice];[2:a]volume=0.14[music];[voice][music]amix=inputs=2:duration=longest:dropout_transition=2[a]" `
    -map 0:v -map "[a]" `
    -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart `
    $output
if ($LASTEXITCODE -ne 0) { throw "FFmpeg composition failed with exit code $LASTEXITCODE." }

Write-Output "Rendered: $output"
