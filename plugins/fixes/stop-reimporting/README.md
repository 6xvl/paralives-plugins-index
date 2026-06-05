# FixMyReimport

Keeps one broken or out-of-date mod from breaking your whole game.

## What it does

Sometimes a single bad mod or piece of custom content can:
- get the game stuck on the "Reimporting Assets" loading screen,
- freeze your save when you try to load it,
- or stop your *other* mods from showing up.

FixMyReimport steps in and skips just that one bad mod (or that one bad item) so the game keeps loading normally — and it notes which one caused it, so you know what to update or remove.

It only skips the bad mod for that one play session. Next time you start the game it tries it again, so a mod that was just having a bad moment (like one that was still downloading) never gets turned off for good.

## Do I need to do anything?

No — it works on its own in the background. If a mod was causing trouble, it's written in your `BepInEx/LogOutput.log` file so you can see exactly which one.

## Settings (optional)

In `BepInEx/config/6ix.StopReimporting.cfg` (that file keeps the old internal name — it's the same mod):
- **AutoDisableBrokenMods** (default on) — skip the whole broken mod for the session instead of just the bad part.
- **WatchdogTimeout** (default 25) — seconds to wait on a stuck loading screen before stepping in.

## Verifying the download

The current version and file hash live in [`manifest.json`](https://github.com/6xvl/paralives-plugins-index/blob/main/manifest.json) (entry `6ix.StopReimporting`). The Plugin Hub checks this automatically on every download.

License: MIT.
