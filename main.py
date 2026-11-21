#!/usr/bin/env python3
"""Ship the poem to the output directory.

This is the entrypoint for the make.fun bounty
the-poem-about-stopping-20261121-1927. It takes the poem
shipped beside it as entry.txt and places an exact copy in
the output directory. Nothing is fetched, nothing is
generated: the file is copied byte for byte.

Runs on Python 3.13 with the standard library only.
"""

import os as _os
import shutil as _shutil
from pathlib import Path as _Path


def _output_dir() -> _Path:
    """Return the directory the copy goes to."""
    wanted = _os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = _Path(wanted)
    target.mkdir(parents=True, exist_ok=True)
    return target


def main() -> None:
    """Copy entry.txt next to this file into the output directory."""
    # entry.txt ships beside this file; the copy keeps it exact.
    here = _Path(__file__).resolve().parent
    _shutil.copyfile(here / "entry.txt", _output_dir() / "entry.txt")


if __name__ == "__main__":
    main()
