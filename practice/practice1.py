#!/usr/bin/env python3
# Practice 1 - "Locker"
# Find a password that makes this program print "correct".
# Rule: letters and digits only. More than one answer can work.
#
# Run it like this:   python3 practice1.py YOURGUESS

import sys


def main():
    if len(sys.argv) != 2:
        print("usage: python3 practice1.py PASSWORD")
        return

    password = sys.argv[1]
    total = 0
    for c in password:
        total = total + ord(c)

    if total == 800 and len(password) == 8 and ord(password[3]) == 75:
        print("correct")
    else:
        print("incorrect")


main()
