# Safer Saves

Protects your saved games from being lost or corrupted.

## What it does

Saving a game means writing a lot of files to your disk. If the game crashes, your PC loses power, or something else goes wrong halfway through, a normal save can end up half-written — and a half-written save can fail to load. Safer Saves makes that much harder to happen:

- **Every save is written safely.** Files are written off to the side first and only swapped in once they're fully on disk, so a crash mid-save never leaves you with a broken file — your previous save stays intact.
- **It keeps backups.** Each time you save, Safer Saves quietly keeps a few of your most recent saves as backups (the last 5). If your current save ever looks damaged when you load it, it offers to restore the most recent good backup for you — and keeps your damaged files in a `.corrupt` folder just in case.
- **It checks your save before loading.** If a save looks damaged, you get a simple Yes/No prompt instead of a failed load.
- **Manual backup any time.** Press **F8** while playing to make an instant backup of your current game.

## Do I need to do anything?

No — it works on its own in the background. Just play normally. If anything ever goes wrong, it'll prompt you or note it in your `BepInEx/LogOutput.log` file.

## Settings (optional)

In `BepInEx/config/6ix.SaferSaves.cfg`:
- **EnableCompression** (default **off**) — shrinks your save files to use less disk space. It's off by default so the mod stays completely safe to remove at any time. If you turn it on, your saves are stored in a format only Safer Saves can read — so if you ever want to uninstall, turn this back on first, load and re-save your towns, *then* remove the mod.

## Verifying the download

The current version and file hash live in [`manifest.json`](https://github.com/6xvl/paralives-plugins-index/blob/main/manifest.json) (entry `6ix.SaferSaves`). The Plugin Hub checks this automatically on every download.

License: MIT.
