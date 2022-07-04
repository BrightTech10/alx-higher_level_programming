#!/usr/bin/python3


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class

    Args:
        obj: object
        a_class: class

    Return:
        returns True if @obj is exactly an instance of @a_class else False
    """
    return True if type(obj) is a_class else False
