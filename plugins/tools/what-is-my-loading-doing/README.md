# What Is My Loading Doing

Ever stared at the Paralives loading screen wondering if it froze or if it's still working? This shows you.

## What it does

It adds a small line under the loading bar that tells you what the game is actually doing right now, in plain words:

- Reading your save…
- Loading furniture (142 / 300)
- Loading characters…
- Building terrain…

If the loading ever gets stuck, it tells you exactly which Workshop item caused it — so instead of removing mods one by one to find the bad one, you know exactly what to take out.

The text uses the game's own font, so it fits right in.

## Do I need to do anything?

No — it shows up on its own while the game is loading and disappears once you're in.

## Settings (optional)

In `BepInEx/config/6ix.WhatIsMyLoadingDoing.cfg`:
- **Enabled** (default on) — show the line or not.
- **StuckSeconds** (default 10) — how long with no progress before it points out what it's stuck on.

## Verifying the download

The current version and file hash live in [`manifest.json`](https://github.com/6xvl/paralives-plugins-index/blob/main/manifest.json) (entry `6ix.WhatIsMyLoadingDoing`). The Plugin Hub checks this automatically.

License: MIT.
