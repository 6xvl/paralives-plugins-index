# Cross-Volume Write Fix (Paralives 0.1.2)

Fixes a save-and-Workshop-mod-loading regression introduced in Paralives 0.1.2 for players whose Steam library lives on a different drive than their Windows `%TEMP%` folder (e.g. Steam on D:/E:/F: + default TEMP on C:).

## Symptoms

You see one or both of these in `BepInEx/LogOutput.log` or in the BepInEx console window:

```
[Error : Unity Log] IOException: Win32 IO returned 1176. Path:
Stack trace:
  System.IO.File.Replace (...)
  AssetManager.WriteAllText (System.String path, System.String contents)
  AssetManager.LoadAssetPackageRecursiveWithCacheIfValid (...)
  AssetManager.LoadAssetPackage (System.UInt64 assetGUID)
  ModManager.RefreshCurrentlyLoadedMods ()
  ModManager.Update ()
```

In-game effects:
- **Workshop mods don't show up** in the in-game mods panel
- **Save files may fail to write** in some configurations
- Steady-state log spam every few seconds while the mod loader retries

## The bug

In 0.1.2 the devs added a new atomic-write helper:

```csharp
// AssetManager.cs:1465-1485
public static void WriteAllText(string path, string contents) {
    byte[] bytes = Encoding.UTF8.GetBytes(contents);
    if (File.Exists(path)) {
        string tempFileName = Path.GetTempFileName();   // <-- lives under %TEMP%
        try {
            using FileStream fs = File.Create(tempFileName, 4096, FileOptions.WriteThrough);
            fs.Write(bytes, 0, bytes.Length);
        } catch (Exception) { return; }
        File.Replace(tempFileName, path, null);          // <-- Win32 ReplaceFile
        return;
    }
    using FileStream fs2 = File.Create(path, 4096, FileOptions.WriteThrough);
    fs2.Write(bytes, 0, bytes.Length);
}
```

`Path.GetTempFileName()` creates the temp file under `%TEMP%`. `File.Replace` wraps Win32 `ReplaceFile`, which [requires source and destination on the same volume](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-replacefilea):

> *"The replaced file, the replacement file, and the backup file must all reside on the same volume; otherwise an error code is returned."*

When your Steam library is on D:/E:/F: and `%TEMP%` is on C:, every call to `AssetManager.WriteAllText` throws `IOException error 1176 = ERROR_UNABLE_TO_MOVE_REPLACEMENT`.

`ModManager.RefreshCurrentlyLoadedMods` regenerates the Workshop meta cache via this helper on every mod scan. Every cache write throws. Workshop mods fail to load silently.

## The fix

Harmony prefix on `AssetManager.WriteAllText` that routes the temp file to **the same directory as the destination** (`path + ".tmp"`). Same-volume by construction, so `File.Replace` works.

If `File.Replace` still fails for any other reason (file locked, antivirus interfering), the patch falls back to a direct overwrite so the caller doesn't lose the write — and logs the failure loudly. Never silent.

## Install

1. Make sure [BepInEx 5.x](https://github.com/BepInEx/BepInEx/releases) is installed in your Paralives folder.
2. Drop `CrossVolumeWriteFix.dll` into `Paralives/BepInEx/plugins/`.
3. Launch the game. You should see this in the BepInEx log:
   ```
   [Info :6ix • Cross-Volume Write Fix (Paralives 0.1.2)] [6ix/X-VOL-FIX] v1.0.0 starting
   [Info :6ix • Cross-Volume Write Fix (Paralives 0.1.2)] [6ix/X-VOL-FIX] hooked AssetManager.WriteAllText — same-volume .tmp atomic write active. (System %TEMP% root: C:\)
   ```

No configuration needed — the patch is on by default and self-disables if the target method can't be found (so it can't break a future game version that ships its own fix).

## Safe for all setups

- If your Steam library and `%TEMP%` are on the same drive: the patch still applies but does the same atomic-write the devs intended, with one extra layer of safety (loud failure logging instead of the dev's silent bare-return on failure).
- If a future Paralives version ships its own fix: the patch self-disables when the target method changes signature or disappears, falling back to whatever the devs ship.

## Compatibility

| | |
|---|---|
| **Game version** | Paralives 0.1.2 (and probably any later version that keeps the same `AssetManager.WriteAllText` signature) |
| **BepInEx** | 5.x |
| **Other 6ix mods** | Fully compatible. SaveGuardian's atomic save patch suppresses `AssetSavedGame.TriggerSave` before it ever calls `AssetManager.WriteAllText`, so this patch handles the other call sites (the Workshop mod loader). |
| **Conflicts** | Only conflicts with any other mod that also Harmony-patches `AssetManager.WriteAllText`. |

## Credits

Bug analysis: the Paralives 0.1.2 patch added the new atomic-write helper shown above; the cross-volume failure mode (Win32 1176) was predicted from the code before it was observed in the wild.

License: MIT.
