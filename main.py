#!/usr/bin/env python3
"""make.fun entry: "Sum up 25 November's world news in one image".

The graded program.  It writes exactly one image, ``entry.png``, into
the output directory named by the MAKEFUN_OUTPUT_DIR environment
variable (falling back to ./output when run locally).

The image itself - a 1024x1024 newspaper-style infographic of the
verified world news of Wednesday, 25 November 2026 - is rendered at
build time by generate_image.py and committed in this repository as
assets/entry.png.  This program only copies those bytes, using nothing
but the Python standard library, so the graded run:

* needs no network, no fonts and no third-party packages,
* finishes in well under a second, and
* writes byte-identical output on every run (the run_deterministic
  check runs it twice and compares).

See README.md and sources.md for what the image shows and where every
headline was verified.
"""

import os
import shutil
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    asset = here / "assets" / "entry.png"
    if not asset.is_file():
        raise SystemExit("assets/entry.png is missing from the repository")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(asset, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
