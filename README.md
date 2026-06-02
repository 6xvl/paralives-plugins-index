# 6ix Plugin Hub — Paralives mods

Browse and install community mods for [Paralives](https://store.steampowered.com/app/1118520/Paralives/) from inside the game. No manual file copying after the first install.

> **Need help?** Join the **[Discord](https://discord.gg/XMXRPTDJv5)** → find the **mods** channel → open the **`[Plugin Hub] Help`** thread inside it.

---

## Install

**[⬇ Download the modpack zip](https://github.com/6xvl/paralives-plugins-index/releases/latest)** (1.2 MB)

Same three steps on every system: **unzip it into your game folder → start the game → open Mods → Plugin Hub.** Pick yours below.

### Windows

1. **Open your Paralives folder.** In Steam, right-click **Paralives** → **Manage** → **Browse local files**. A window opens with `Paralives.exe` in it.
2. **Unzip the download into that folder.** Right-click `6ix-paralives-modpack.zip` → **Extract All…** → choose that folder. You're done when `winhttp.dll` is sitting right next to `Paralives.exe`.
3. **Start the game.** On the main menu click **Mods** — there's a new **Plugin Hub** tab. Open it to browse and install mods.

That's it. ✅

### Steam Deck / Linux

Same as Windows, plus **one line to paste**:

1. Open your Paralives folder and unzip the download into it (Windows steps 1–2 above).
2. In Steam, right-click **Paralives** → **Properties** → **Launch Options**, and paste this into the box:

   ```
   WINEDLLOVERRIDES="winhttp=n,b" %command%
   ```

3. Start the game, then open **Mods → Plugin Hub**.

That line just tells Steam to load the mods from the zip. To undo it later, empty the box. ✅

<details>
<summary>Prefer protontricks?</summary>

```bash
protontricks 1118520 winetricks --force --no-isolate winhttp=n,b
```

`1118520` is Paralives' Steam ID. The launch-option method above is simpler and easier to undo. Tested with default Proton — thanks @maxtron95 + @seajr.
</details>

### Mac

Everything's already in the zip — you just paste **two short commands**.

1. **Open your Paralives folder.** In Steam, right-click **Paralives** → **Manage** → **Browse local files**. You'll see `Paralives.app`.
2. **Unzip the download into that folder**, so `run_bepinex.sh` lands next to `Paralives.app`.
3. **Open Terminal in that folder**, then copy-paste these two lines, pressing Enter after each:

   ```bash
   chmod +x run_bepinex.sh
   xattr -dr com.apple.quarantine .
   ```

   These just let Mac run the loader — it's blocked by default because you downloaded it.
4. **Tell Steam to use it.** Right-click **Paralives** → **Properties** → **Launch Options**, and paste the full path to the script, a space, then `%command%`. To get the exact path, type `pwd` in the Terminal from step 3 and add `/run_bepinex.sh`:

   ```
   "/Users/YOU/Library/Application Support/Steam/steamapps/common/Paralives/run_bepinex.sh" %command%
   ```

5. **Start the game**, then open **Mods → Plugin Hub**.

> Mac support is new — if Plugin Hub doesn't show up, ask in the [Discord](https://discord.gg/XMXRPTDJv5) and we'll help.

### What's in the bundle

| File | Purpose |
|---|---|
| `winhttp.dll` + `doorstop_config.ini` | [BepInEx 5](https://github.com/BepInEx/BepInEx) (forked) — the mod loader Paralives uses on Windows / Proton (MIT). |
| `run_bepinex.sh` + `libdoorstop.dylib` | macOS BepInEx loader (Doorstop 4.5.0), preconfigured. Windows/Linux ignore these; macOS uses them instead of `winhttp.dll`. |
| `BepInEx/core/*` | BepInEx runtime + HarmonyX/MonoMod patching libraries. |
| `BepInEx/patchers/PluginHubUpdater.dll` | Tiny pre-load updater — fetches the manifest at boot, replaces any installed plugin whose on-disk hash differs from the latest, then hands off to the chainloader. Updates apply on the same launch, no second restart. |
| `BepInEx/plugins/PluginHub.dll` | This project — the in-game browser. |
| `BepInEx/plugins/StatsOverlay.dll` | F3 stats panel — useful for spotting performance issues. |

Other mods (Menu FPS Limiter, Not Enough Workshop Mods, anything else listed below) install from inside the Plugin Hub UI in one click — they're not pre-bundled so first-launch is minimal.

### Updating

After the initial install, Plugin Hub auto-updates itself and all installed mods on each game launch (configurable per plugin). To update the bundled BepInEx runtime later, re-download this zip and overwrite.

### Uninstall

Delete `winhttp.dll`, `doorstop_config.ini`, `.doorstop_version`, and the `BepInEx` folder from your Paralives folder. The game returns to vanilla. On macOS, delete `run_bepinex.sh`, `libdoorstop.dylib`, and the `BepInEx` folder, and clear the Steam Launch Options.

---

## Available mods

| Category | Mod | Bundled? | What it does |
|---|---|---|---|
| Tools | **Plugin Hub** | ✅ pre-installed | Browse, install, and toggle Paralives mods from inside the game. Auto-updates itself and your installed mods on each launch. Also fixes the Steam-offline boot hang so the game launches without internet. |
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

<details>
<summary>Want to double-check the download yourself? (optional — for the technical)</summary>

You don't have to — Plugin Hub already checks everything automatically. But if you'd like to confirm the zip is exactly what we published, paste this into PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 .\6ix-paralives-modpack.zip
```

It should print `549f269d0f6df79d21b7aed88873ed9f5f23c6304d5a8232080050ba312f9761`.
</details>

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

If Plugin Hub or any of these mods make your Paralives experience better, consider supporting on **[Patreon](https://www.patreon.com/6xvl)**. Goes directly toward more mods + maintenance time.

The blue **Support this project** button in the Plugin Hub UI links to the same page.

---

## License

[MIT](LICENSE) — do what you want, just don't blame us if your save breaks. 6ix takes no responsibility for community-submitted mods; they're MIT-licensed by their authors. Bundled BepInEx is MIT — see the [BepInEx repo](https://github.com/BepInEx/BepInEx) for upstream copyright.

— [@6xvl](https://github.com/6xvl)
