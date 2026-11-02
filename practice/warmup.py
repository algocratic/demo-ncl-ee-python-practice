#!/usr/bin/env python3
# Warm-up drill. Run it:  python3 warmup.py
# Read each line, guess the output, then check.

print("--- 1. Characters are numbers ---")
print(ord("A"), ord("a"), ord("0"))      # letter -> number
print(chr(83), chr(107))                 # number -> letter

print("--- 2. Add up a word ---")
word = "cyber"
total = 0
for c in word:
    total = total + ord(c)
    print(c, ord(c), "running total:", total)

print("--- 3. Shift a letter (wrap past z) ---")
n = ord("x") + 5
if n > ord("z"):
    n = n - 26
print("x shifted by 5 is", chr(n))

print("--- 4. Bit operations and how to undo them ---")
x = 100
a = x << 2          # shift left 2 = multiply by 4
b = a ^ 999         # XOR with a key
c = ~b              # NOT: ~v is the same as -(v + 1)
print("forward:", x, "->", a, "->", b, "->", c)
# Undo in REVERSE order. Each operation has an inverse:
#   NOT  is undone by NOT
#   XOR  is undone by XOR with the same key
#   << 2 is undone by >> 2 (or // 4)
back = ((~c) ^ 999) >> 2
print("backward:", back)
