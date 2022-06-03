#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1  # Number of arguments
    value = sys.argv[argc]    # Value at argument position

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, value))
    else:
        print("{} arguments:".format(argc))
        # to get the argument value at its index position
        for i, arg in enumerate(sys.argv):
            if i == 0:
                continue
            print("{}: {}".format(i, arg))
