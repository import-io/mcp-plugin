#!/usr/bin/env python3
"""Build a standalone Antigravity bundle without changing Claude's files."""

import argparse
import json
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    ".antigravity-plugin/plugin.json": "plugin.json",
    ".antigravity-plugin/README.md": "README.md",
    "mcp_config.json": "mcp_config.json",
    "skills/import-io-web-scraper/SKILL.md": "skills/import-io-web-scraper/SKILL.md",
    "assets/importio-icon.svg": "assets/importio-icon.svg",
    "assets/NOTICE.md": "assets/NOTICE.md",
    "LICENSE": "LICENSE",
    "docs/ANTIGRAVITY-VALIDATION.md": "docs/ANTIGRAVITY-VALIDATION.md",
}


def build(output: Path, source: Path = ROOT) -> Path:
    """Create a new package and deterministic zip. Never overwrite an old build."""
    output = output.absolute()
    archive = output.with_suffix(".zip") if not output.suffix else Path(str(output) + ".zip")
    if output.exists() or output.is_symlink() or archive.exists() or archive.is_symlink():
        raise FileExistsError("Output already exists; choose a new build directory.")
    sources = {}
    for relative, destination in FILES.items():
        path = source / relative
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(source.resolve()):
            raise ValueError(f"Missing or unsafe package input: {relative}")
        sources[destination] = path
    output.mkdir(parents=True)
    for destination, path in sources.items():
        target = output / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
        target.chmod(0o644)
    with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_DEFLATED) as bundle:
        for destination in sorted(sources):
            info = zipfile.ZipInfo(f"{output.name}/{destination}", (2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            bundle.writestr(info, (output / destination).read_bytes())
    return archive


def main() -> None:
    manifest = json.loads((ROOT / ".antigravity-plugin/plugin.json").read_text())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "dist" / f"{manifest['name']}-{manifest['version']}")
    args = parser.parse_args()
    try:
        archive = build(args.output)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Build failed: {exc}\n")
    print(f"Plugin directory: {args.output.absolute()}")
    print(f"Plugin archive: {archive}")


if __name__ == "__main__":
    main()
