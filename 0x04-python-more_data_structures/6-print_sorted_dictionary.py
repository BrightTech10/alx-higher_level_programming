#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """ Function that prints a dictionary by ordered keys

        Args:
            a_dictionary: a dictionary
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
