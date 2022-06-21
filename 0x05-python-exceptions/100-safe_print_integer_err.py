#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    prints an integer.

    Args:
        value: integer to be printed

    Return:
        returns true if integer is printed, else false
    """
    try:
        print("{:d}".format(value))
    except Exception as error:
        print("Exception: " + str(error), file=sys.stderr)
    return isinstance(value, int)
