#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """A function that replaces or adds key/value in a dictionary

    Args:
        a_dictionary: a dictionary
        key: dictionary key
        value: value of each key

    Return:
        returns the updated dictionary
    """
    a_dictionary.update({key: value})
    return a_dictionary
