#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        sum = sum + int(arg)
    print(sum)
