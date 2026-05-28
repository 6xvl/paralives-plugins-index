# Paralives Plugins Index

Curated index of BepInEx plugins for [Paralives](https://store.steampowered.com/app/1118520/Paralives/), consumed by the **6ix Plugin Hub** mod for in-game one-click install.

## Structure

```
manifest.json               ← single index consumed by Plugin Hub
plugins/
├── fixes/                  ← bug fixes
│   └── workshop-unlock/
│       ├── plugin.json
│       └── README.md
├── performance/            ← perf optimizations
├── ui/                     ← overlays, panels
├── quality-of-life/        ← small QoL tweaks
├── gameplay/               ← gameplay changes
└── tools/                  ← dev/debug tooling
```

Each plugin folder is **human-browsable** — README explains the plugin, `plugin.json` is the per-plugin canonical metadata. The root `manifest.json` is the **machine-readable aggregate** that Plugin Hub fetches.

## For users

Install the [6ix mod pack](#) which includes Plugin Hub. The hub fetches `manifest.json`, groups plugins by category, and shows a Download button per row. SHA256 verification is mandatory — corrupt or tampered downloads are rejected.

Manifest URL Plugin Hub reads:
```
https://raw.githubusercontent.com/6xvl/paralives-plugins-index/main/manifest.json
```

## Listed plugins

### 🔧 Fixes
| Plugin | Version | Author |
|---|---|---|
| [Workshop Unlock](plugins/fixes/workshop-unlock/) | 1.0.0 | 6ix |

### ⚡ Performance
*(none yet)*

### 🖥️ UI
*(none yet)*

### ✨ Quality of Life
*(none yet)*

### 🎮 Gameplay
*(none yet)*

### 🛠️ Tools
*(none yet)*

## For plugin authors

1. Build your `.dll` against BepInEx 5 + HarmonyX, target `netstandard2.0`
2. Use `[BepInPlugin("yourorg.PluginName", ...)]` — the GUID is what Plugin Hub uses to detect "already installed"
3. Upload the DLL as a GitHub Release asset (your own repo)
4. Compute SHA256: `Get-FileHash -Algorithm SHA256 .\YourPlugin.dll`
5. Open a PR to this repo:
   - Add `plugins/<category>/<plugin-id>/plugin.json` + `README.md`
   - Add an entry to root `manifest.json` (must include `category`)

### plugin.json schema

```json
{
  "id": "yourorg.PluginName",
  "name": "Display Name",
  "author": "Your Handle",
  "category": "fixes",
  "description": "One sentence.",
  "version": "1.0.0",
  "download": "https://github.com/your/repo/releases/download/v1.0.0/YourPlugin.dll",
  "sha256": "abc123…",
  "size_bytes": 12345,
  "homepage": "https://github.com/your/repo"
}
```

Valid categories: `fixes`, `performance`, `ui`, `quality-of-life`, `gameplay`, `tools`.

— 6ix
