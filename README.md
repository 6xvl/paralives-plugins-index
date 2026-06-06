# 6ix Plugin Hub — Paralives mods

<p align="center">
  <a href="https://www.patreon.com/6xvl"><img src="https://img.shields.io/badge/%E2%9D%A4%20Support%20this%20project-on%20Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white" alt="Support this project on Patreon — keep it from being discontinued"></a>
  <a href="https://ko-fi.com/6xvls"><img src="https://img.shields.io/badge/or%20buy%20me%20a-Ko--fi-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Support this project on Ko-fi"></a>
  <a href="https://github.com/6xvl/paralives-plugins-index/releases/latest"><img src="https://img.shields.io/github/v/release/6xvl/paralives-plugins-index?style=for-the-badge&label=Download&color=2ea44f&logo=github&logoColor=white" alt="Download the latest release"></a>
  <a href="https://discord.gg/XMXRPTDJv5"><img src="https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join the Discord"></a>
</p>
<p align="center">
  <a href="https://github.com/6xvl/paralives-plugins-index/releases"><img src="https://img.shields.io/github/downloads/6xvl/paralives-plugins-index/total?style=for-the-badge&label=Downloads&color=4c1&logo=github&logoColor=white" alt="Total downloads"></a>
  <a href="https://github.com/6xvl/paralives-plugins-index/stargazers"><img src="https://img.shields.io/github/stars/6xvl/paralives-plugins-index?style=for-the-badge&label=Stars&color=f9c513&logo=github&logoColor=white" alt="GitHub stars"></a>
  <a href="https://store.steampowered.com/app/1118520/Paralives/"><img src="https://img.shields.io/badge/Game-Paralives-1b2838?style=for-the-badge&logo=steam&logoColor=white" alt="For Paralives on Steam"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/6xvl/paralives-plugins-index?style=for-the-badge&label=License&color=lightgrey" alt="License: MIT"></a>
</p>

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

Everything's already in the zip — you just point Terminal at the folder, then paste three short commands.

1. **Open your Paralives folder.** In Steam, right-click **Paralives** → **Manage** → **Browse local files**. You'll see `Paralives.app`.
2. **Unzip the download into that folder**, so `run_bepinex.sh` lands next to `Paralives.app`.
3. **Point Terminal at that folder — this is the step everyone gets wrong.** If you just open Terminal and paste the commands, it says *"No such file or directory"* — because Terminal starts in your **home** folder, not the game folder, even though you can see the file sitting right there in Finder. Do this:
   - Open **Terminal** (press `Cmd + Space`, type `Terminal`, press Enter).
   - Type `cd` and then **one space** — *don't press Enter yet* — then **drag the Paralives folder from Finder into the Terminal window** and let go. It fills in the path for you. **Now** press Enter.
   - Type `ls` and press Enter. You should see `run_bepinex.sh` and `Paralives.app` in the list — that confirms you're in the right place.
4. **Now paste these three lines, pressing Enter after each:**

   ```bash
   chmod +x run_bepinex.sh
   xattr -dr com.apple.quarantine .
   codesign --remove-signature Paralives.app
   ```

   Line 1 makes the loader runnable, line 2 clears the "downloaded from the internet" block, and line 3 lets the loader attach to the game — macOS blocks this on signed apps by default (it's the same step the community [`gib`](https://github.com/toebeann/gib) installer does).
5. **Tell Steam to use it.** Right-click **Paralives** → **Properties** → **Launch Options**, and paste the full path to the script, a space, then `%command%`. To get the exact path, type `pwd` in the same Terminal and add `/run_bepinex.sh`:

   ```
   "/Users/YOU/Library/Application Support/Steam/steamapps/common/Paralives/run_bepinex.sh" %command%
   ```

6. **Start the game**, then open **Mods → Plugin Hub**.

> Mac support is experimental — if Plugin Hub doesn't show up, ask in the [Discord](https://discord.gg/XMXRPTDJv5) and we'll help.

### What's in the bundle

| File | Purpose |
|---|---|
| `winhttp.dll` + `doorstop_config.ini` | [BepInEx 5](https://github.com/BepInEx/BepInEx) (forked) — the mod loader Paralives uses on Windows / Proton (MIT). |
| `run_bepinex.sh` + `libdoorstop.dylib` | macOS BepInEx loader (Doorstop 4.5.0), preconfigured. Windows/Linux ignore these; macOS uses them instead of `winhttp.dll`. |
| `BepInEx/core/*` | BepInEx runtime + HarmonyX/MonoMod patching libraries. |
| `BepInEx/plugins/PluginHub.dll` | This project — the in-game browser. It also self-updates and updates your installed mods on each launch: reads `manifest.json`, downloads any newer DLLs, verifies them against the manifest hash, and applies them. |
| `BepInEx/plugins/WorkshopUnlock.dll` | "Not Enough Workshop Mods" — fixes the Steam Workshop 50-mod cap. |
| `BepInEx/plugins/StopReimporting.dll` | "FixMyReimport" — keeps one broken/outdated mod from freezing the loading screen or your save. (The file keeps its old name so it updates in place.) |
| `BepInEx/plugins/WhatIsMyLoadingDoing.dll` | Shows what the game is loading on the loading screen, and names the exact item if it gets stuck. |
| `BepInEx/plugins/StatsOverlay.dll` | F3 stats panel — useful for spotting performance issues. |

Only **Menu FPS Limiter** isn't pre-bundled — install it from inside the Plugin Hub UI in one click.

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
| Tools | **What Is My Loading Doing** | ✅ pre-installed | Shows what the game is doing on the loading screen ("Loading furniture 142/300", "Loading characters"…) instead of just a spinning icon, and names the exact item if a load gets stuck. |
| Fixes | **Not Enough Workshop Mods** | ✅ pre-installed | Fixes the Steam Workshop 50-mod cap. Without it, any subscribed mods past #50 get **deleted** from your computer on game launch. |
| Fixes | **FixMyReimport** | ✅ pre-installed | Keeps one broken or outdated mod from freezing the "Reimporting Assets" loading screen or your save. It skips just that mod for the session, tells you which one, and tries it again next launch. |
| Performance | **Menu FPS Limiter** | install from Hub | Caps the frame rate at 60 in the main menu and 30 when the window isn't focused (alt-tab). Gameplay runs uncapped by default. Stops your fans screaming while the menu sits at 200+ fps doing nothing. |

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

It should print `fe5c02a70d1e6c678e9166e5841f0fe0811ae6065a7a26ded967a185830b05e5`.
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

If Plugin Hub or any of these mods make your Paralives experience better, consider supporting on **[Patreon](https://www.patreon.com/6xvl)** or **[Ko-fi](https://ko-fi.com/6xvls)**. Goes directly toward more mods + maintenance time.

The blue **Support this project** button in the Plugin Hub UI links to the Patreon page.

---

## Star History

A ⭐ keeps the project visible — and keeps it going.

<a href="https://star-history.com/#6xvl/paralives-plugins-index&Date">
  <img src="https://api.star-history.com/svg?repos=6xvl/paralives-plugins-index&type=Date" alt="Star History Chart" width="600">
</a>

---

## License

[MIT](LICENSE) — do what you want, just don't blame us if your save breaks. 6ix takes no responsibility for community-submitted mods; they're MIT-licensed by their authors. Bundled BepInEx is MIT — see the [BepInEx repo](https://github.com/BepInEx/BepInEx) for upstream copyright.

— [@6xvl](https://github.com/6xvl)
