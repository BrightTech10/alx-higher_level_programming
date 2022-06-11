#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """A function that deletes a key in a dictionary

    Args:
        a_dictionary: a dictionary
        key: dictionary key

    Return:
        returns updated dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
        return a_dictionary
    else:
        return a_dictionary
