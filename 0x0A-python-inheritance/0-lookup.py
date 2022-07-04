#!/usr/bin/python3
""" Defines a lookup function """


def lookup(obj):
    """
    Returns a list of available attibutes and methods

    Args:
        obj: object
    """
    return dir(obj)
