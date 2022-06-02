#!/usr/bin/python3
for char in reversed(range(ord('a'), ord('z') + 1)):
    if (char % 2) != 0:
        char -= 32
    else:
        char
    print("{}".format(chr(char)), end="")
