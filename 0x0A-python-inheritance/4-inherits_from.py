#!/usr/bin/python3


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
    return True if issubclass(type(obj), a_class) and type(obj) is not a_class else False
