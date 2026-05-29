# Offline Workshop Enabler

By **lptb9**. Bundled into the 6ix Plugin Hub manifest with permission/credit; not authored by 6ix.

Lets Paralives finish loading when Steam is in **offline mode** or has no internet. Without this, the game hangs waiting for Steam Workshop's "initial launch downloads" check to complete, which never resolves offline.

## The fix (in one sentence)

Harmony Postfix on `SteamworksService.Update` that sets `CompletedInitialLaunchDownloads = true` so Paralives' boot pipeline proceeds past the Workshop-download gate when there's no Steam connection.

## Use case

- You play Paralives without internet (laptop on a plane, Steam Deck in offline mode, etc.)
- Steam Workshop downloads can't run without a connection
- Vanilla Paralives waits forever for the download check
- With this plugin: Paralives boots, your already-downloaded Workshop mods load normally, you play

## Manual install

If you're not using the 6ix Plugin Hub:

1. Download [`Paralives_OfflineWorkshopEnabler.dll`](https://github.com/6xvl/paralives-plugins-index/raw/main/plugins/fixes/offline-workshop-enabler/Paralives_OfflineWorkshopEnabler.dll)
2. Drop into `Paralives/BepInEx/plugins/`
3. Restart Paralives — even with Steam offline, the game now reaches the main menu

## Verification

SHA256 of the v1.0.0 DLL:
```
f9d75f61757f3035991fb43d53295ced4e10a425625742673da39f1705f56530
```
PowerShell: `Get-FileHash -Algorithm SHA256 .\Paralives_OfflineWorkshopEnabler.dll`

## Compatibility

Works alongside **Not Enough Workshop Mods** — they patch different methods on `SteamworksService` and don't conflict. If you use Steam Workshop and also play offline, you probably want both.
