#!/usr/bin/python3
""" 8-class_to_json module
"""


def class_to_json(obj):
    """
    Retrieves the dictionary description of
    an instance of a class

    Args:
        obj: instance of a class

    Return:
        returns the dictionary description
    """
    return obj.__dict__
