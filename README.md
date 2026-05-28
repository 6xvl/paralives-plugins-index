# Paralives Plugins Index

Curated index of BepInEx plugins for [Paralives](https://store.steampowered.com/app/1118520/Paralives/), consumed by the **6ix Plugin Hub** mod for in-game one-click install.

## For users

Install the [6ix mod pack](#) which includes Plugin Hub. The hub fetches `manifest.json` from this repo and shows a download button per plugin. SHA256 verification is mandatory — corrupt or tampered downloads are rejected.

## For plugin authors — submitting a plugin

1. Build your `.dll` against BepInEx 5 + HarmonyX, targeting `netstandard2.0`.
2. Add a `[BepInPlugin("yourorg.PluginName", ...)]` attribute — the GUID is what Plugin Hub uses to detect "already installed".
3. Create a GitHub Release in your own repo, upload the DLL as a release asset.
4. Compute SHA256: `Get-FileHash -Algorithm SHA256 .\YourPlugin.dll`
5. Open a PR to this repo adding an entry to `manifest.json`:

```json
{
  "id": "yourorg.PluginName",
  "name": "Display Name",
  "author": "Your Handle",
  "description": "What it does in one sentence.",
  "version": "1.0.0",
  "download": "https://github.com/your/repo/releases/download/v1.0.0/YourPlugin.dll",
  "sha256": "abc123…",
  "size_bytes": 12345,
  "homepage": "https://github.com/your/repo"
}
```

## Listed plugins

| Plugin | Version | Author |
|---|---|---|
| [Workshop Unlock](https://github.com/6xvl/paralives-plugins-index/releases/tag/WorkshopUnlock-v1.0.0) | 1.0.0 | 6ix |

## Manifest URL

Plugin Hub reads from:
```
https://raw.githubusercontent.com/6xvl/paralives-plugins-index/main/manifest.json
```

— 6ix
