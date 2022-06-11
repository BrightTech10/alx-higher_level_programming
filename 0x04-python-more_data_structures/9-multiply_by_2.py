#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """ A function that multuplies dictionary values by 2

    Args:
        a_dictionary: a dictionary

    Return:
        returns a new dictionary
    """
    new_dict = a_dictionary.copy()
    new_dict.update((key, value*2) for key, value in a_dictionary.items())
    return new_dict
