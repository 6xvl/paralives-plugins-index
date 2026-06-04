# Stop Reimporting My Mods

Stops a single broken or outdated mod from taking down your whole game — whether it freezes the **"Reimporting Assets"** loading screen, makes your other mods silently fail to show up, or softlocks a save.

## What it guards against

| Failure | Without this mod | With this mod |
|---|---|---|
| A corrupt asset throws/hangs during reimport | "Reimporting Assets" screen hangs until a 90s timeout (or forever) | The asset is skipped instantly; the owning mod is disabled for this session and named in the log |
| A mod's package fails to load (e.g. a missing `.setting` file) | The load loop aborts and **every mod after it silently fails to appear** | Only the broken mod is skipped; the rest load normally |
| A save references a broken/malformed Workshop item | The save load **softlocks** (loads fine on an empty lot, hangs on a furnished one) | The bad item is skipped and **its catalogue GUID + owning mod are logged**, so you can identify the exact CC that was softlocking your save |
| A dead entry in the mod list | A recurring `NullReferenceException` on boot | The dead entry is dropped before it can crash the load |

## Session-only, never permanent

When a mod fails, it's disabled **for that session only** — nothing is written to disk. The mod is tried again on the next launch, so a one-off failure (e.g. a mod still mid-download, or a transient Steam hiccup) never locks a working mod out. Mods that were skipped show a red **(Skipped)** / amber **(Partial)** tag in *My Mods*.

## Finding the mod that's breaking things

Open `BepInEx/LogOutput.log` and look for `[6ix/STOP-REIMPORTING]` lines. The relevant one names the asset or item and its owning mod, e.g.:

```
[6ix/STOP-REIMPORTING/ITEM] a placed item failed to load during save load and was SKIPPED — catalogueGUID=… ownerMod='…' … This is the Workshop item that was softlocking your save.
```

## Config (`BepInEx/config/6ix.StopReimporting.cfg`)

```ini
[StopReimporting]
## Seconds of continuous "Reimporting Assets" before the watchdog rescues the stuck state. 0 = disable.
WatchdogTimeout = 90

## On any mod failure, disable that whole mod for THIS session (not persisted; retried next launch). false = skip only the bad asset/package.
AutoDisableBrokenMods = true
```

Edit and restart the game to apply.

## Manual install

If you're not using the 6ix Plugin Hub:

1. Download [`StopReimporting.dll`](https://github.com/6xvl/paralives-plugins-index/raw/main/plugins/fixes/stop-reimporting/StopReimporting.dll)
2. Drop it into `Paralives/BepInEx/plugins/`
3. Restart Paralives. On boot you should see `[6ix/STOP-REIMPORTING/…] … active` lines in the BepInEx log.

## Verification

The current version and SHA256 are in [`manifest.json`](https://github.com/6xvl/paralives-plugins-index/blob/main/manifest.json) (entry `6ix.StopReimporting`) — the single source of truth. Plugin Hub verifies every download against that hash automatically. To check a manual download, run `Get-FileHash -Algorithm SHA256 .\StopReimporting.dll` and compare it to the manifest.

License: MIT.
