# NCL Enumeration & Exploitation: Python Practice

This repo gets you ready for the NCL Gymnasium challenges **Python 1, 2 and 3**. The practice files are not the gym challenges. They use the same skills.

## 1. Get your copy

Pick ONE way.

**A. Codespaces (no installs; use this on lab computers).**
On this repo's GitHub page, click **Use this template → Open in a codespace**. Wait until the terminal shows `READY`. Then go to step 3.

**B. Your own computer.**
1. Click **Use this template → Create a new repository**. Make your copy **private**.
2. Clone your copy, then open a terminal in its folder.
3. Type `pip install -r requirements.txt` (on Windows, `py -m pip install -r requirements.txt`).

## 2. Check your setup

```
python3 check_setup.py
```

Every line must say `OK`. If a line says `FIX`, do what it says, then run the check again. On Windows, type `py` where this page says `python3`.

## 3. The method (use it on every challenge)

1. **READ.** Get code that you can read. A `.py` file is already readable. For a `.pyc` file, decompile it:
   `uncompyle6 practice2.pyc > practice2_src.py`
2. **LIST THE RULES.** Write each check that the input must pass, one per line. Use `notes/RULES.md`.
3. **REVERSE.** Start at the target value. Undo each step in the opposite order.
4. **RUN.** Test your answer. Mark each rule **C** (read in the code) or **R** (seen when you ran it). Do not guess. The code decides.

## 4. Do the practice, in order

```
cd practice
python3 warmup.py
python3 practice1.py YOURGUESS
uncompyle6 practice2.pyc > practice2_src.py
uncompyle6 practice3.pyc > practice3_src.py
```

| File | Skill | Gym match |
|---|---|---|
| `practice/warmup.py` | `ord()`, `chr()`, letter shifts, bit operations | All |
| `practice/practice1.py` | Read source, add a debug `print`, do the arithmetic | Python 1 |
| `practice/practice2.pyc` | Decompile, find a letter shift, shift back | Python 2 |
| `practice/practice3.pyc` | Decompile, undo `<<`, `^` and `~` in reverse order | Python 3 |

To test a practice 2 or 3 answer, run your decompiled file: `python3 practice2_src.py YOURANSWER`. If it stops responding, press `Ctrl+C` and read the second note below. Finding that problem is part of practice 2.

## 5. Do the gym challenges

Download the gym files into the `gym/` folder. **Do not commit them.** NCL rules do not allow anyone to post gym challenges online. Git ignores that folder for you.

## Notes

- **You cannot run a `.pyc` file on a different Python version.** The error is `Bad magic number`. Decompile the file and read it instead.
- **Decompiled code is close, not exact.** If a recovered loop says `while True:` with no `break`, it runs forever. Change it to the real condition, for example `while i < len(key):`.
- **The gym files use Python 2.7.** In Python 2, `print "x"` has no parentheses. Read the logic. Do not change it.
- **Python counts from 0.** `password[3]` is the 4th character.
- **More than one answer can work.** If a check uses only a sum, many inputs pass.
- **Use letters and digits.** The shell changes characters such as `!`, `$` and `&`.
