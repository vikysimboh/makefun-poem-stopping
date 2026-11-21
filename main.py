"""Entry for make.fun bounty the-poem-about-stopping-20261121-1927.
Copies the shipped entry.txt to the output directory.
Python 3.13, standard library only, no network, deterministic.
The text is 248 characters about agency: the power to stop and to stay. The poem is about stopping and staying: the hand lifts off the keys, nothing breaks, and stopping turns out to be finally standing on the road.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.txt", OUT / "entry.txt")
