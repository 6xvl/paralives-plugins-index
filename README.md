# 6ix Plugin Hub — Paralives mods

Browse and install community mods for [Paralives](https://store.steampowered.com/app/1118520/Paralives/) from inside the game. No manual file copying after the first install.

---

## Quick install

**[⬇ Download the modpack zip — latest release](https://github.com/6xvl/paralives-plugins-index/releases/latest)** (1.1 MB)

1. **Find your Paralives folder.** Steam → right-click **Paralives** → **Manage** → **Browse local files**. You should see `Paralives.exe` inside.
2. **Extract the zip into that folder.** Right-click the downloaded `6ix-paralives-modpack.zip` → **Extract All…** → pick your Paralives folder. After it finishes, `winhttp.dll` should sit next to `Paralives.exe` and a `BepInEx` folder should appear beside it.
3. **Launch the game.** Click **Mods** on the main menu — you'll see a new **Plugin Hub** tab next to *Control Panel*. Click it to browse, install, and toggle mods.

That's it. Everything in the zip is set up to run on first launch.

### Linux / Steam Deck (Proton)

Paralives runs under Proton. One extra step is required because Proton's Wine ships its own `winhttp.dll` that shadows ours unless you tell Wine to use the native (game folder) copy.

After extracting the zip, run **one** of these:

**Option A — `protontricks` GUI (easiest):**
```bash
protontricks 1118520 winecfg
```
In the dialog: **Libraries** tab → type `winhttp` in the override field → **Add** → click it in the list → **Edit** → set to **native, builtin** → OK.

**Option B — fully non-interactive:**
```bash
protontricks 1118520 winetricks --force --no-isolate winhttp=n,b
```

`1118520` is Paralives' Steam App ID. After running once, launch the game through Steam normally.

Verified working: extraction with KDE Ark (right-click → Extract → Here), launching via Steam with default Proton.

### What's in the bundle

| File | Purpose |
|---|---|
| `winhttp.dll` + `doorstop_config.ini` | [BepInEx 5](https://github.com/BepInEx/BepInEx) (forked) — the mod loader Paralives uses (MIT). |
| `BepInEx/core/*` | BepInEx runtime + HarmonyX/MonoMod patching libraries. |
| `BepInEx/plugins/PluginHub.dll` | This project — the in-game browser. |
| `BepInEx/plugins/StatsOverlay.dll` | F3 stats panel — useful for spotting performance issues. |

Other mods (Menu FPS Limiter, Not Enough Workshop Mods, anything else listed below) install from inside the Plugin Hub UI in one click — they're not pre-bundled so first-launch is minimal.

### Updating

After the initial install, Plugin Hub auto-updates itself and all installed mods on each game launch (configurable per plugin). To update the bundled BepInEx runtime later, re-download this zip and overwrite.

### Uninstall

Delete `winhttp.dll`, `doorstop_config.ini`, `.doorstop_version`, and the `BepInEx` folder from your Paralives folder. The game returns to vanilla.

### Verify the download

```powershell
Get-FileHash -Algorithm SHA256 .\6ix-paralives-modpack.zip
```

Expected: `58d853b79a92a23ebbb598fcc8b2cd26318f2b09b4764fd275d2898172f018cb`

---

## Available mods

| Category | Mod | Bundled? | What it does |
|---|---|---|---|
| Tools | **Plugin Hub** | ✅ pre-installed | Browse, install, and toggle Paralives mods from inside the game. Auto-updates itself and your installed mods on each launch. |
| Tools | **Stats Overlay** | ✅ pre-installed | Unity-Editor-style stats panel — FPS, CPU/render times, draw calls, triangles, audio level, animation counts. Top-left overlay. Press F3 to toggle. |
| Performance | **Menu FPS Limiter** | install from Hub | Caps the frame rate at 60 in the main menu and 30 when the window isn't focused (alt-tab). Gameplay runs uncapped by default. Stops your fans screaming while the menu sits at 200+ fps doing nothing. |
| Fixes | **Not Enough Workshop Mods** | install from Hub | Fixes the Steam Workshop 50-mod cap. Without it, any subscribed mods past #50 get **deleted** from your computer on game launch. Install if you use Workshop. |

Hover any mod card in Plugin Hub for the same description in-game. More on the way — open a PR to add yours, see [Contributing](#contributing).

---

## How it works

- The **Plugin Hub** is a small loader you install once via the modpack zip.
- It reads `manifest.json` from this repo and lists every available mod with its description, version, and SHA256.
- When you click **Install** on a card, Plugin Hub downloads the mod's `.dll` straight from this repo, verifies the file against the manifest hash, and writes it into `BepInEx/plugins/`.
- Mods only load after a game restart — no risky mid-session injection.

---

## Safety

- **Hash verification on every download.** If a file doesn't match the manifest hash, it's rejected and nothing is written.
- **No telemetry, no analytics, no calling home.** Plugin Hub only connects to GitHub to fetch the manifest and the DLLs you explicitly click on.
- **Auditable.** Every mod's source, the loader, and the manifest are all in this repo.

---

## Contributing

To get your mod into Plugin Hub:

1. Build it as a normal BepInEx 5 plugin (`BaseUnityPlugin` + `[BepInPlugin]`), target `netstandard2.0`.
2. Pick a category from `manifest.json` → `categories` (`fixes`, `performance`, `ui`, `quality-of-life`, `gameplay`, `tools`).
3. Open a PR adding:
   - `plugins/<category>/<plugin-name>/YourPlugin.dll`
   - `plugins/<category>/<plugin-name>/README.md`
   - A new entry in `manifest.json` with `id` matching your `[BepInPlugin]` GUID, the raw-URL `download`, computed `sha256`, matching `size_bytes`, and a 1–2 sentence `description` (what the user sees on hover).

Get the SHA256 with PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 .\YourPlugin.dll
```

---

## Support

If Plugin Hub or any of these mods make your Paralives experience better, you can tip a coffee at **[ko-fi.com/6xvls](https://ko-fi.com/6xvls)**. No account needed, 0% fees, takes 30 seconds. Goes directly toward more mods + maintenance time.

The blue **Support this project** button in the Plugin Hub UI links to the same page.

---

## License

[MIT](LICENSE) — do what you want, just don't blame us if your save breaks. 6ix takes no responsibility for community-submitted mods; they're MIT-licensed by their authors. Bundled BepInEx is MIT — see the [BepInEx repo](https://github.com/BepInEx/BepInEx) for upstream copyright.

— [@6xvl](https://github.com/6xvl)
