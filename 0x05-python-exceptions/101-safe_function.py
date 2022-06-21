#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    executes a function safely

    Args:
        fct: pointer to a function
        args: arguments
    """
    try:
        return fct(*args)
    except Exception as error:
        print("Exception: " + str(error), file=sys.stderr)
        return None
