#!/usr/bin/python3


def safe_print_integer(value):
    """Prints an integer

    Args:
        value: integer to be printed

    Return:
        returns True if value is an integer, else false
    """
    check = isinstance(value, int)
    if check:
        try:
            print("{:d}".format(value))
            return check
        except ValueError:
            pass
    else:
        return check
