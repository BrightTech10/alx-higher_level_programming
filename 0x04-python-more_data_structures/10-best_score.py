#!/usr/bin/python3

def best_score(a_dictionary):
    """ A function that computes the maximum value in a dictionary

    Args:
        a_dictionary: a dictionary

    Return:
        returns the key with the biggest integer value
    """
    if a_dictionary:
        biggest = max(a_dictionary, key=lambda key: a_dictionary[key])
        return biggest
    else:
        return None
