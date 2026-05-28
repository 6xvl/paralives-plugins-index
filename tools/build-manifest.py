#!/usr/bin/env python3
"""
Build root manifest.json by walking plugins/<category>/<plugin-id>/plugin.json.

Category is derived from the folder name — plugin authors never write it in their plugin.json.
To move a plugin to a different category: `git mv plugins/old-cat/<id> plugins/new-cat/<id>` and re-run.

Categories themselves come from plugins/categories.json (id, label, order).

Usage: python tools/build-manifest.py
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PLUGINS_ROOT = REPO / "plugins"
CATEGORIES_FILE = PLUGINS_ROOT / "categories.json"
OUTPUT = REPO / "manifest.json"

# Fields that MAY appear in plugin.json. Authors fill these; never write "category".
ALLOWED_FIELDS = {
    "id", "name", "author", "description", "version",
    "download", "sha256", "size_bytes", "homepage",
}
REQUIRED_FIELDS = {"id", "name", "version", "download", "sha256"}


def main() -> int:
    if not CATEGORIES_FILE.exists():
        die(f"missing {CATEGORIES_FILE.relative_to(REPO)}")

    cats_doc = load_json(CATEGORIES_FILE)
    cats = cats_doc.get("categories") or []
    valid_cat_ids = {c["id"] for c in cats}

    plugins_out = []
    errors = []

    # Walk plugins/<category>/<plugin-id>/plugin.json
    for cat_dir in sorted(p for p in PLUGINS_ROOT.iterdir() if p.is_dir()):
        cat_id = cat_dir.name
        if cat_id not in valid_cat_ids:
            # Unknown category folder — warn but include as-is so it surfaces in PluginHub's "Other"
            print(f"  warn: folder '{cat_id}/' has no entry in categories.json", file=sys.stderr)
        for plugin_dir in sorted(p for p in cat_dir.iterdir() if p.is_dir()):
            manifest_path = plugin_dir / "plugin.json"
            if not manifest_path.exists():
                continue
            try:
                entry = load_json(manifest_path)
            except Exception as e:
                errors.append(f"{manifest_path.relative_to(REPO)}: {e}")
                continue

            # Refuse author-written category — folder is source of truth
            if "category" in entry:
                errors.append(
                    f"{manifest_path.relative_to(REPO)}: do not put 'category' in plugin.json — "
                    f"it is derived from folder name '{cat_id}'. Remove the field."
                )
                continue

            missing = REQUIRED_FIELDS - entry.keys()
            if missing:
                errors.append(f"{manifest_path.relative_to(REPO)}: missing required fields {sorted(missing)}")
                continue

            unknown = entry.keys() - ALLOWED_FIELDS
            if unknown:
                errors.append(f"{manifest_path.relative_to(REPO)}: unknown fields {sorted(unknown)}")
                continue

            # Inject category from folder name
            entry["category"] = cat_id
            plugins_out.append(entry)

    if errors:
        for e in errors:
            print(f"  error: {e}", file=sys.stderr)
        die(f"{len(errors)} validation error(s) — manifest not written")

    plugins_out.sort(key=lambda p: (p["category"], p["name"].lower()))

    manifest = {
        "schema": 2,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "categories": cats,
        "plugins": plugins_out,
    }

    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"  ok: wrote {OUTPUT.relative_to(REPO)} ({len(plugins_out)} plugin(s), {len(cats)} categor(ies))")
    return 0


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def die(msg: str):
    print(f"build-manifest: {msg}", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    sys.exit(main())
