# Not Enough Workshop Mods

Fixes Paralives' Steam Workshop 50-mod cap. (Previously named "Workshop Unlock".)

## The bug

Paralives queries Steam UGC with `Query.Items.WhereUserSubscribed().GetPageAsync(1)` — a single page from Steam's API, hard-capped at 50 entries. The caller then `Directory.Delete`s any local mod folder NOT present in that page result.

**Consequence:** If you're subscribed to mod #51 (or beyond), it isn't in page 1, so the game treats it as "unsubscribed" and **deletes its local folder on next launch**.

Community confirmation: [Steam forum thread](https://steamcommunity.com/app/1118520/discussions/1/663863113757516191/)

## The fix

Harmony Prefix on `SteamworksService.DownloadDeleteOrLoadAllSubscribed()` that:
1. Loops `Query.Items.WhereUserSubscribed().GetPageAsync(page)` for `page = 1, 2, 3, ...`
2. Stops when `ResultCount < 50` or `MaxPagesToFetch` reached (default 200 → 10,000 mod ceiling)
3. Aggregates all entries before running the original per-item dispatch + deletion logic
4. Original code reused — only the source list is now complete

## Safety

- **If any `GetPageAsync` throws mid-fetch, the entire deletion pass is skipped for that launch.** Local mods are never deleted on partial Steam data. This is explicit — silent deletion is the bug we're fixing.
- **If `MaxPagesToFetch` is reached**, plugin logs a warning and skips deletion. Raise `MaxPagesToFetch` in config if you somehow have 10,000+ subscriptions.
- **If the patched method is renamed in a game update**, the plugin self-disables with an error log. Original (broken) method runs — mods past #50 still at risk but plugin won't cause new harm.

## Config (`BepInEx/config/6ix.WorkshopUnlock.cfg`)

```ini
[Workshop]
MaxPagesToFetch = 200
```

## Manual install

If you're not using the 6ix Plugin Hub:

1. Download [`WorkshopUnlock.dll`](https://github.com/6xvl/paralives-plugins-index/raw/main/plugins/fixes/workshop-unlock/WorkshopUnlock.dll) (lives in this repo, not a release)
2. Drop into `Paralives/BepInEx/plugins/`
3. Restart Paralives
4. Verify in BepInEx console: `[6ix/WORKSHOP-UNLOCK] fetched N subscribed mods across P page(s) ...`

## Verification

SHA256 of the v1.0.0 DLL:
```
4e1c7dfe042c7f4f69da5dea521441cfc3bb695a758aacddfc0d2d3ca2135c33
```
PowerShell: `Get-FileHash -Algorithm SHA256 .\WorkshopUnlock.dll`
