# Plugin Hub — loose binary

This folder holds `PluginHub.dll`, the in-game UI for the 6ix Plugin Hub.

| File | Goes in | What it does |
|---|---|---|
| `PluginHub.dll` | `BepInEx/plugins/` | Adds the **Plugin Hub** tab to Paralives' Mods editor — browse, install, and toggle mods from inside the game. It also self-updates and updates your installed mods on each launch: reads `manifest.json`, downloads any newer DLLs, verifies each against the manifest SHA256, and writes them into `BepInEx/plugins/`. |

> Earlier versions shipped a second `Updater.dll` (a BepInEx patcher) to apply updates at boot, before the chainloader. That job is now built into `PluginHub.dll` itself, so the separate updater has been removed. If you still have an old `BepInEx/patchers/PluginHubUpdater.dll` from a previous install, you can safely delete it — it does nothing now.

If you just want everything installed for you, grab the modpack from the [**latest release**](https://github.com/6xvl/paralives-plugins-index/releases/latest) — extract it into your Paralives folder and every file lands in the right place. See the [main README](../README.md) for per-OS steps.

---

## Direct download

| File | URL |
|---|---|
| `PluginHub.dll` | https://github.com/6xvl/paralives-plugins-index/raw/main/loader/PluginHub.dll |
| `6ix-paralives-modpack.zip` (BepInEx + PluginHub + bundled plugins) | https://github.com/6xvl/paralives-plugins-index/releases/latest |

**Verify a download** before installing:

PowerShell:
```powershell
Get-FileHash -Algorithm SHA256 .\PluginHub.dll
```

Linux/macOS:
```bash
sha256sum PluginHub.dll
```

Compare the result against the `6ix.PluginHub` entry in [`manifest.json`](../manifest.json) — the single source of truth for every plugin's version and hash.

## Why `PluginHub.dll` lives in the repo (not a GitHub release)

So I don't have to publish a new release for every small fix. The install steps link to this file's raw URL, which always serves the latest commit on `main` — update = `git commit + push`. (The bundled modpack **zip** is the exception: it's attached to a GitHub release so its download link stays stable across versions.)

## Install (manual, if not using the modpack zip)

1. Install [BepInEx 5 x64 (Mono build)](https://github.com/BepInEx/BepInEx/releases) into your Paralives folder. You should see `winhttp.dll` next to `Paralives.exe`.
2. Launch Paralives once so BepInEx creates the `BepInEx/plugins/` folder.
3. Drop `PluginHub.dll` into `BepInEx/plugins/`.
4. Launch the game. The **Plugin Hub** tab appears inside the Mods menu; from there install any other mod in one click. Plugin Hub keeps itself and your installed mods up to date on each launch.
