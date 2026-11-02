#!/usr/bin/env python3
"""Look at the raw bytes of any file. Works on Windows, Mac and Linux.

    python3 tools/hexview.py FILE            # like:  hexdump -C FILE
    python3 tools/hexview.py --strings FILE  # like:  strings FILE

Hex view: each line shows 16 bytes.
  left   = offset (where the bytes start, in hex)
  middle = each byte as two hex digits
  right  = each byte as a character ('.' if it is not printable)
"""
import sys


def hexdump(data):
    for off in range(0, len(data), 16):
        chunk = data[off:off + 16]
        hexes = " ".join("%02x" % b for b in chunk[:8])
        hexes += "  " + " ".join("%02x" % b for b in chunk[8:])
        text = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        print("%08x  %-49s |%s|" % (off, hexes, text))


def strings(data, min_len=4):
    run = bytearray()
    for b in data + b"\0":
        if 32 <= b < 127:
            run.append(b)
        else:
            if len(run) >= min_len:
                print(run.decode("ascii"))
            run = bytearray()


def main():
    args = sys.argv[1:]
    mode = "hex"
    if args and args[0] == "--strings":
        mode = "strings"
        args = args[1:]
    if len(args) != 1:
        print(__doc__)
        sys.exit(1)
    with open(args[0], "rb") as f:
        data = f.read()
    if mode == "strings":
        strings(data)
    else:
        hexdump(data)


main()
