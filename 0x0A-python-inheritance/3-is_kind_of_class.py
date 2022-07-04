#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class or if an
    object is an instance of a class inherited from a specified class

    Args:
        obj: object
        a_class: class

    Return:
        returns True if @obj is exactly an instance of @a_class else False
    """
    return True if isinstance(obj, a_class) else False
