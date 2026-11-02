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

1. **LOOK.** Before you decompile, look at the raw bytes. Text and numbers in the program are often visible. See "Look before you decompile" below.
2. **READ.** Get code that you can read. A `.py` file is already readable. For a `.pyc` file, decompile it:
   `uncompyle6 practice2.pyc > practice2_src.py`
3. **LIST THE RULES.** Write each check that the input must pass, one per line. Use `notes/RULES.md`.
4. **REVERSE.** Start at the target value. Undo each step in the opposite order.
5. **RUN.** Test your answer. Mark each rule **C** (read in the code) or **R** (seen when you ran it). Do not guess. The code decides.

## 4. Do the practice, in order

```
cd practice
python3 warmup.py
python3 practice1.py YOURGUESS

python3 ../tools/hexview.py --strings practice2.pyc
python3 ../tools/hexview.py practice2.pyc
uncompyle6 practice2.pyc > practice2_src.py

python3 ../tools/hexview.py practice3.pyc
uncompyle6 practice3.pyc > practice3_src.py
```

| File | Skill | Gym match |
|---|---|---|
| `practice/warmup.py` | `ord()`, `chr()`, letter shifts, bit operations | All |
| `practice/practice1.py` | Read source, add a debug `print`, do the arithmetic | Python 1 |
| `practice/practice2.pyc` | Decompile, find a letter shift, shift back | Python 2 |
| `practice/practice3.pyc` | Decompile, undo `<<`, `^` and `~` in reverse order | Python 3 |

To test a practice 2 or 3 answer, run your decompiled file: `python3 practice2_src.py YOURANSWER`. If it stops responding, press `Ctrl+C` and read the second note below. Finding that problem is part of practice 2.

## 5. Look before you decompile

A `.pyc` file is not secret. It is compiled, not encrypted. The text and the numbers in the program are stored in the file as they are.

| Tool | Command | What it shows |
|---|---|---|
| Strings | `python3 ../tools/hexview.py --strings FILE` | Runs of readable text: messages, stored values, names of functions and variables. |
| Hex view | `python3 ../tools/hexview.py FILE` | Every byte, in hex (middle) and as text (right). Numbers show here, not in strings. |
| Native (Mac, Linux, Codespaces) | `strings FILE`, `od -A x -c FILE`, `hexdump -C FILE` | The same views. Some systems do not have all three. `hexview.py` works everywhere. |

Do these tasks. Write what you find in `notes/RULES.md`.

1. **Practice 2, strings.** Find the messages the program prints. Find one long string of letters that is not a message. What could it be?
2. **Practice 2, hex.** Find that string in the hex view. Note its offset (left column).
3. **Practice 3, strings.** Find the one-letter string. What could it be?
4. **Practice 3, hex.** Python stores a small whole number as the byte `69` or `e9`, then the number in 4 bytes, **lowest byte first**. Example: 10 is `e9 0a 00 00 00`. Find the stored numbers near the word `incorrect`. Convert one to decimal:
   `python3 -c "print(int.from_bytes(bytes.fromhex('0a000000'), 'little', signed=True))"`
5. **Then decompile.** Do the values you found match the code? Mark them **C** in your rules sheet.

**What the bytes cannot tell you:** the order of the steps, and what the program does with each value. The decompiler shows that.

## 6. Do the gym challenges

Download the gym files into the `gym/` folder. **Do not commit them.** NCL rules do not allow anyone to post gym challenges online. Git ignores that folder for you.

## Notes

- **You cannot run a `.pyc` file on a different Python version.** The error is `Bad magic number`. Decompile the file and read it instead.
- **Decompiled code is close, not exact.** If a recovered loop says `while True:` with no `break`, it runs forever. Change it to the real condition, for example `while i < len(key):`.
- **The gym files use Python 2.7.** In Python 2, `print "x"` has no parentheses. Read the logic. Do not change it.
- **Python counts from 0.** `password[3]` is the 4th character.
- **More than one answer can work.** If a check uses only a sum, many inputs pass.
- **Use letters and digits.** The shell changes characters such as `!`, `$` and `&`.
