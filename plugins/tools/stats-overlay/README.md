# Stats Overlay

Unity-Editor-style statistics overlay for Paralives. Top-left, hidden by default, **F3 to toggle**.

```
Statistics · 6ix
Audio:
  Level:  -48.2 dB    DSP load: 0.0%
  Clipping: 0.0%   Stream load: 0.0%

Graphics:      60.0 FPS (16.7ms)
  CPU: main 16.7ms  render 11.2ms
  Batches: 142
  Draw calls: 198
  SetPass calls: 23
  Tris: 1.2M
  Verts: 1.8M
  Shadow casters: 14
  Screen: 1920x1080 - 16.6MB

Visible skinned meshes: 38 / 124
Animation components playing: 4
Animator components playing: 87
```

## What it shows

| Metric | Source |
|---|---|
| FPS / CPU main thread | `Time.unscaledDeltaTime`, EMA-smoothed |
| Render-thread time | `Camera.onPreRender` first / `onPostRender` last delta |
| Batches, SetPass, Draw calls, Tris, Verts, Shadow casters | `Unity.Profiling.ProfilerRecorder` (Render category) |
| Audio dB / clipping | `AudioListener.GetOutputData` → RMS |
| Animation / Animator / Skinned mesh counts | `FindObjectsOfType` every 60 frames (configurable) |
| Screen mem | `width × height × 4 × 2 / 1MB` |
| DSP / Stream load | always 0 — no public managed API in Unity 2020.3 |

## Why

When you're chasing a stutter or wondering whether a render-heavy scene is GPU- or CPU-bound, you want this info in front of you without alt-tabbing to a separate profiler. The classic Unity Editor stats panel is a sane format and reads fast.

## Config (`BepInEx/config/6ix.StatsOverlay.cfg`)

```ini
[Overlay]
StartVisible = false
ToggleKey = F3
Width = 320
MarginTop = 16
MarginLeft = 16
RefreshHeavyEveryNFrames = 60
FontSize = 12
```

Edit + restart the game.

## Manual install

If you're not using the 6ix Plugin Hub:

1. Download [`StatsOverlay.dll`](https://github.com/6xvl/paralives-plugins-index/raw/main/plugins/tools/stats-overlay/StatsOverlay.dll)
2. Drop into `Paralives/BepInEx/plugins/`
3. Restart Paralives, press F3 in-game

## Verification

SHA256 of the v1.0.4 DLL:
```
e7784f55a3758d1a863a8e80b2dc76e417f1eebc0743da93b0be8455f5ace89f
```
PowerShell: `Get-FileHash -Algorithm SHA256 .\StatsOverlay.dll`

## Heads up

Logs `Profiler is not supported in this build` to BepInEx output on init. That message is misleading — `ProfilerRecorder` actually works fine on Unity 2020.3 Mono shipping builds (the recorders return live values). Ignore the warning.
