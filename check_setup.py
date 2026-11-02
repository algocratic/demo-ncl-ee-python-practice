#!/usr/bin/env python3
"""Run this first:  python3 check_setup.py

It checks that your computer is ready for the E&E Python practice.
Each line prints OK or FIX. Do the FIX steps, then run it again.
"""
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ok = True


def report(passed, what, fix=""):
    global ok
    if passed:
        print("OK   " + what)
    else:
        ok = False
        print("FIX  " + what)
        if fix:
            print("     -> " + fix)


# 1. Python version
v = sys.version_info
report(v >= (3, 8), "Python %d.%d.%d" % (v[0], v[1], v[2]),
       "Install Python 3.8 or later from python.org.")

# 2. Decompiler installed
tool = shutil.which("uncompyle6")
report(tool is not None, "uncompyle6 is installed",
       "Type:  pip install -r requirements.txt   (Windows: py -m pip install -r requirements.txt)")

# 3. Decompiler works on a practice file
if tool:
    target = os.path.join(HERE, "practice", "practice2.pyc")
    try:
        out = subprocess.run([tool, target], capture_output=True, text=True, timeout=60).stdout
        works = "def main" in out
    except Exception:
        works = False
    report(works, "uncompyle6 can decompile practice/practice2.pyc",
           "Close the terminal, open a new one, and run this check again. If it still fails, ask a coach.")

print()
print("READY. Open README.md and start with practice/warmup.py." if ok else "NOT READY. Do the FIX steps above.")
sys.exit(0 if ok else 1)
