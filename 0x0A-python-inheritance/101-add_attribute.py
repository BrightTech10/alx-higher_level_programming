#!/usr/bin/python3
""" Defines add_attribute method """


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it’s possible

    Args:
        obj: object whose which attribute is to be assigned.
        name: object attribute which has to be assigned
        value: value with which variable is to be assigned.

    Raises:
        raises TypeError if new attribute can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
