# 6ix Plugin Hub — Paralives mods

Browse and install community mods for [Paralives](https://store.steampowered.com/app/1118520/Paralives/) from inside the game. No manual file copying.

---

## 🟢 How to install (10 minutes, no tech knowledge needed)

You need **two downloads**: BepInEx 5 (the mod loader Paralives uses) and the Plugin Hub `.dll` (the in-game browser). Both are free and open source.

### 1. Download BepInEx 5 (x64, Mono)

**[⬇ BepInEx 5 latest release](https://github.com/BepInEx/BepInEx/releases/latest)** → from the **Assets** list at the bottom, grab the file named like **`BepInEx_win_x64_5.4.X.X.zip`** (NOT `BepInEx_unix_…` and NOT the `6_X` previews).

### 2. Find your Paralives folder
- Open **Steam**
- Right-click **Paralives** in your library → **Manage** → **Browse local files**
- A folder opens. You should see `Paralives.exe` inside. This is the folder you need.

Typical path: `C:\Program Files (x86)\Steam\steamapps\common\Paralives\`

### 3. Extract BepInEx into the Paralives folder
- Right-click `BepInEx_win_x64_5.4.X.X.zip` → **Extract all…**
- Pick the Paralives folder from step 2
- After extracting you should see new files next to `Paralives.exe`: `winhttp.dll`, `doorstop_config.ini`, and a `BepInEx` folder

### 4. Run Paralives once, then close it
This lets BepInEx create the folders it needs (`BepInEx/plugins/`, `BepInEx/config/`, etc.). Just launch, wait until the main menu shows, then quit.

### 5. Download Plugin Hub

**[⬇ PluginHub.dll](https://github.com/6xvl/paralives-plugins-index/raw/main/loader/PluginHub.dll)** — direct download, always the latest.

(Optional, for the paranoid: verify the SHA256 hash matches the one in [`loader/README.md`](loader/README.md). PowerShell: `Get-FileHash -Algorithm SHA256 .\PluginHub.dll`)

### 6. Drop the .dll into the plugins folder
Move `PluginHub.dll` into `Paralives\BepInEx\plugins\` (this folder was created in step 4).

### 7. Launch the game
- Start Paralives through Steam
- Click **Mods** on the main menu
- You'll see a new blue **Plugin Hub** tab next to *Control Panel* — click it
- Browse, install, restart. Done.

### Updating
- **Update BepInEx:** re-extract a newer `BepInEx_win_x64_*.zip` into Paralives, overwrite when prompted
- **Update Plugin Hub:** re-download `PluginHub.dll` from the link in step 5, overwrite the one in `BepInEx/plugins/`

### Uninstall
Delete `winhttp.dll`, `doorstop_config.ini`, and the `BepInEx` folder from your Paralives folder. The game returns to vanilla.

---

## 🧩 Available mods

| Category | Mod | What it does |
|---|---|---|
| Fixes | **Not Enough Workshop Mods** | Fixes the Steam Workshop 50-mod cap. Without it, mods past #50 get **deleted** from your computer on game launch. |

*(More on the way. Open a PR to add yours — see Contributing below.)*

---

## ⚙️ How it works (short)

- The **Plugin Hub** is a small loader you install once.
- It reads `manifest.json` from this repo and shows a list of mods.
- When you click Download, it grabs the mod's `.dll` from this repo, verifies the file with a SHA256 hash, and drops it into your game's plugin folder.
- Mods only load after a game restart — no risky mid-session injection.

---

## 🛡️ Safety

- **Hash verification on every download.** If the file doesn't match the hash in the manifest, it's rejected and nothing is written.
- **Open source.** Every mod's source code, the loader, and this index are all on GitHub. You can read or audit any of it.
- **No telemetry, no analytics, no calling home.** Plugin Hub only ever connects to GitHub to fetch the manifest and DLLs you click on.

---

## 🛠️ For mod authors — contributing

1. Build your `.dll` against BepInEx 5 + HarmonyX, target `netstandard2.0`
2. Open a PR adding:
   - `plugins/<category>/<your-id>/YourPlugin.dll`
   - `plugins/<category>/<your-id>/plugin.json` (no `category` field — folder is the source of truth)
   - `plugins/<category>/<your-id>/README.md`
3. Run `python tools/build-manifest.py` to regenerate the root `manifest.json` (or let CI do it)

**Categories:** `fixes`, `performance`, `ui`, `quality-of-life`, `gameplay`, `tools`

### plugin.json schema
```json
{
  "id": "yourorg.PluginName",
  "name": "Display Name",
  "author": "Your Handle",
  "description": "One sentence.",
  "version": "1.0.0",
  "download": "https://github.com/6xvl/paralives-plugins-index/raw/main/plugins/<cat>/<id>/YourPlugin.dll",
  "sha256": "abc123…",
  "size_bytes": 12345,
  "homepage": "https://github.com/6xvl/paralives-plugins-index/tree/main/plugins/<cat>/<id>"
}
```

Get the SHA256 with PowerShell:
```powershell
Get-FileHash -Algorithm SHA256 .\YourPlugin.dll
```

---

## ☕ Support

If Plugin Hub or any of these mods make your Paralives experience better, you can tip a coffee at **[ko-fi.com/6xvls](https://ko-fi.com/6xvls)**. No account needed, 0% fees, takes 30 seconds. Goes directly toward more mods + maintenance time.

The blue **Support Me** button in the Plugin Hub UI links to the same page.

---

## 📜 License

[MIT](LICENSE) — do what you want, just don't blame us if your save breaks. 6ix takes no responsibility for community-submitted mods; they're MIT-licensed by their authors.

— [@6xvl](https://github.com/6xvl)
