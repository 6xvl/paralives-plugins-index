# Privacy Policy

**Last updated: 2026-06-29**

ParaLine Launcher ("the launcher") is a free, open-source tool for managing Paralives mods. This document explains what information the launcher handles and how.

---

## What the launcher collects

### Online presence count
The launcher sends a periodic heartbeat to `api.6xvl.com` to power the "X Playing" counter shown on the home screen. This heartbeat contains a single identifier derived from your Steam ID. It is used only to count unique active sessions and is discarded after 5 minutes of inactivity. No name, email address, or account details are transmitted.

### Steam information
The launcher calls the local Steam client to read your Steam display name and Steam ID. This information stays on your machine. The Steam ID is used only as described above for the presence counter.

### Mod downloads
When you install a mod, the launcher fetches the mod file from the URL listed in the public mod index. The index is hosted on GitHub. No personal information is sent as part of this request beyond what a normal web request includes (your IP address, visible to GitHub's servers).

---

## What the launcher does not collect

- No account registration or login
- No analytics, telemetry, or crash reporting
- No persistent tracking across sessions
- No advertising identifiers
- No microphone, camera, or location access

---

## Third-party services

| Service | Purpose | Their privacy policy |
|---|---|---|
| Steam (Valve) | Local mod management, player count | https://store.steampowered.com/privacy_agreement |
| GitHub | Mod index hosting, mod file downloads | https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement |
| Cloudflare Workers | Presence API (`api.6xvl.com`) | https://www.cloudflare.com/privacypolicy |

---

## Contact

Questions or concerns: open an issue at https://github.com/6xvl/paralives-plugins-index/issues
