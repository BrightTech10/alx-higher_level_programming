#!/usr/bin/python3
""" defines a inherits_from function """


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of an inherited class

    Args:
        obj: object to check
        a_class: class to match object type

    Return:
        returns True if object is an instance of an inherited class
        else False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
