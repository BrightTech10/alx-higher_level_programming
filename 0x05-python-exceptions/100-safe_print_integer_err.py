#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    check = isinstance(value, int)
    try:
        print("{:d}".format(value))
        return check
    except Exception as error:
        print("Exception: " + str(error), file=sys.stderr)
