#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attibutes and methods

    Args:
        obj: object
    """
    return dir(obj)
