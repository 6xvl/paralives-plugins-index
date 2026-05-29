# FPS Limiter

Context-aware FPS cap. By default:

- **Main menu / loading scenes:** 60 fps
- **Game window unfocused (alt-tab):** 30 fps
- **In a save (gameplay):** uncapped — runs at whatever the game/monitor can deliver

All three thresholds are configurable via `BepInEx/config/6ix.FpsLimiter.cfg` (created on first launch). Set any value to `-1` to disable that cap.

## How it works

Subscribes to `SceneManager.sceneLoaded` to know whether the menu shell or a gameplay scene is active. Polls `Application.isFocused` each frame for alt-tab. Disables VSync (`QualitySettings.vSyncCount = 0`) when a hard cap is active — Unity's `targetFrameRate` is ignored when VSync is on. Restores the original VSync setting when the cap is "uncapped" (i.e. entering gameplay).

## Why

Main menus that render at hundreds of fps for no reason (clouds and a single sprite at 240 fps) just heat the GPU. 60 is plenty for menus. 30 when unfocused saves a bunch of background power and stops your fans from screaming while you're in another window.

## Config

```ini
[Limits]
## Cap FPS in main menu / loading scenes. Set to -1 to leave uncapped.
# Setting type: Int32
# Default value: 60
MenuFps = 60

## Cap FPS when the game window does NOT have focus (alt-tabbed). Set to -1 to leave uncapped.
# Setting type: Int32
# Default value: 30
UnfocusedFps = 30

## Cap FPS in actual gameplay scenes. -1 = uncapped (the game's default).
# Setting type: Int32
# Default value: -1
GameplayFps = -1
```

Edit live and restart the game to apply.

## Compatibility

Works with Paralives early access (Unity 2020.3.49 Mono). Should work on any Paralives build going forward — no version-specific patches.
