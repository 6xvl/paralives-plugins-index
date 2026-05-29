"""Rebuild the modpack zip with proper forward-slash entry separators.

PowerShell's Compress-Archive writes zip entries with backslash separators
(Windows-native), which violates the zip spec (POSIX-style forward slashes
required). Windows extractors and Python's zipfile are tolerant about this;
strict extractors like Linux unzip and KDE Ark take backslashes literally
and treat the entries as files with backslashes IN the filename.

Run this from the loader/ folder after rebuilding the staging tree.
"""
import os
import zipfile
import hashlib
import sys

STAGE = os.path.expandvars(r"%TEMP%\6ix-paralives-modpack-stage")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "6ix-paralives-modpack.zip")


def to_zip_path(rel: str) -> str:
    # Force POSIX-style separators regardless of host OS.
    return rel.replace(os.sep, "/").replace("\\", "/")


def main() -> int:
    if not os.path.isdir(STAGE):
        print(f"stage dir not found: {STAGE}", file=sys.stderr)
        return 1

    if os.path.exists(OUT):
        os.remove(OUT)

    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for root, dirs, files in os.walk(STAGE):
            for d in dirs:
                full = os.path.join(root, d)
                rel = os.path.relpath(full, STAGE)
                if not os.listdir(full):
                    z.writestr(to_zip_path(rel) + "/", "")
            for f in files:
                full = os.path.join(root, f)
                rel = os.path.relpath(full, STAGE)
                z.write(full, to_zip_path(rel))

    sha = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
    size = os.path.getsize(OUT)
    print(f"modpack sha={sha} size={size}")
    print()
    print("=== first 8 entries ===")
    with zipfile.ZipFile(OUT) as z:
        for n in z.namelist()[:8]:
            print(repr(n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
