$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..\..")
$python = Join-Path $repoRoot ".venv\Scripts\python.exe"
$manim = Join-Path $repoRoot ".venv\Scripts\manim.exe"
$ffmpeg = "C:\Users\User\AppData\Local\Temp\mummur-voice-tools\node_modules\.pnpm\ffmpeg-static@5.3.0\node_modules\ffmpeg-static\ffmpeg.exe"
$build = Join-Path $PSScriptRoot "build"
$media = Join-Path $PSScriptRoot "media-duck"
$exports = Join-Path $repoRoot "exports"
$narration = Join-Path $build "narration-duck-standard.mp3"
$music = Join-Path $build "technology-bed-duck-standard.wav"
$silentVideo = Join-Path $media "videos\ep01_duck_host\1920p30\SilentSparksDuckHost.mp4"
$output = Join-Path $exports "Silent_Sparks_EP01_Duck_Host_Version_F_Standard_Speed.mp4"

New-Item -ItemType Directory -Force $build, $media, $exports | Out-Null
$env:PATH = "$(Split-Path $ffmpeg);$env:PATH"

if (!(Test-Path $narration) -or !(Test-Path $music)) {
    & $python (Join-Path $PSScriptRoot "make_audio.py") `
        --text (Join-Path $PSScriptRoot "narration_en.txt") `
        --voice $narration `
        --music $music `
        --rate=+0% `
        --duration 60.1
    if ($LASTEXITCODE -ne 0) { throw "Audio generation failed with exit code $LASTEXITCODE." }
}

& $manim -qh --fps 30 --media_dir $media (Join-Path $PSScriptRoot "ep01_duck_host.py") SilentSparksDuckHost
if ($LASTEXITCODE -ne 0) { throw "Manim render failed with exit code $LASTEXITCODE." }

& $ffmpeg -y `
    -i $silentVideo `
    -i $narration `
    -i $music `
    -filter_complex "[1:a]adelay=2000|2000,volume=1.0[voice];[2:a]volume=0.14[music];[voice][music]amix=inputs=2:duration=longest:dropout_transition=2,loudnorm=I=-16:LRA=11:TP=-1.5[a]" `
    -map 0:v -map "[a]" `
    -c:v libx264 -preset slow -crf 16 -maxrate 8M -bufsize 16M -pix_fmt yuv420p `
    -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart `
    $output
if ($LASTEXITCODE -ne 0) { throw "FFmpeg composition failed with exit code $LASTEXITCODE." }

Write-Output "Rendered: $output"
