# Plugin Hub — loose binaries

This folder holds the two files that make the Plugin Hub work. They look similar but **go in different folders and serve different purposes**:

| File | Goes in | What it does |
|---|---|---|
| `PluginHub.dll` | `BepInEx/plugins/` | The in-game UI — adds the Plugin Hub tab to Paralives' Mods editor. Needs Unity to run. |
| `Updater.dll` | `BepInEx/patchers/` | Boot-time updater. Runs BEFORE BepInEx loads plugins, fetches the manifest, replaces any out-of-date DLLs on disk, and auto-installs any plugin marked `default_install: true` in the manifest. Pure file I/O — no UI. |

**Why two files:** the chainloader loads ALL plugin DLLs at once, then calls `Awake()` on each. By the time PluginHub's `Awake()` runs, its own bytes are already in memory — too late to update itself. The only window to overwrite plugin DLLs is the BepInEx **Preloader** phase, which runs **patchers** before the chainloader scans `BepInEx/plugins/`. Hence the split.

If you just want the bundle installed for you, grab [`6ix-paralives-modpack.zip`](6ix-paralives-modpack.zip) — extract it into your Paralives folder and both files land in the right places automatically.

---

## Direct downloads

| File | Raw URL |
|---|---|
| `PluginHub.dll` | https://github.com/6xvl/paralives-plugins-index/raw/main/loader/PluginHub.dll |
| `Updater.dll` | https://github.com/6xvl/paralives-plugins-index/raw/main/loader/Updater.dll |
| `6ix-paralives-modpack.zip` (BepInEx + both files + bundled plugins) | https://github.com/6xvl/paralives-plugins-index/raw/main/loader/6ix-paralives-modpack.zip |

**Verify the file you downloaded** before installing:

PowerShell:
```powershell
Get-FileHash -Algorithm SHA256 .\PluginHub.dll
Get-FileHash -Algorithm SHA256 .\Updater.dll
```

Linux/macOS:
```bash
sha256sum PluginHub.dll Updater.dll
```

Compare against the latest commit on this folder — every push updates the binaries.

## Why these live in the repo (not a GitHub release)

So I don't have to publish a new GitHub Release every time I push a small fix. The README install steps link to these files' raw URLs, which always serve the latest commit. Update = `git commit + push`.

## Install (manual, if not using the modpack zip)

1. Install [BepInEx 5 x64 (Mono build)](https://github.com/BepInEx/BepInEx/releases) into your Paralives folder. You should see `winhttp.dll` next to `Paralives.exe`.
2. Launch Paralives once so BepInEx creates the `BepInEx/plugins/` and `BepInEx/patchers/` folders.
3. Drop `PluginHub.dll` into `BepInEx/plugins/`.
4. Drop `Updater.dll` into `BepInEx/patchers/`.
5. Launch the game. The Plugin Hub tab appears inside the Mods menu. The updater runs silently at every boot — check `BepInEx/LogOutput.log` for `[6ix/UPDATER]` lines.
