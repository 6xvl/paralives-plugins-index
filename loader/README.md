# Plugin Hub loader

This folder holds the live `PluginHub.dll` — the BepInEx plugin that adds the in-game Plugin Hub tab to Paralives' Mods editor.

**Direct download:** [PluginHub.dll](https://github.com/6xvl/paralives-plugins-index/raw/main/loader/PluginHub.dll)

**SHA256 (verify after download):**
```
5236daf37122abd0b332b9c8c6afaca104e0d50f05486c50caaa978390fa749e
```

PowerShell:
```powershell
Get-FileHash -Algorithm SHA256 .\PluginHub.dll
```

## Why it's in the repo (not a GitHub release)

So I don't have to publish a new GitHub Release every time I push a small fix. The README install steps link to this file's raw URL, which always serves the latest commit. Update = `git commit + push`.

## Install

See the [main README](../README.md) — short version: install BepInEx 5 x64 (Mono) → drop this file into `BepInEx/plugins/` → launch.
