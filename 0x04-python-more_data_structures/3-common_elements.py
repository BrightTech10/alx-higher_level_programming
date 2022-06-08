#!/usr/bin/python3


from multiprocessing import reduction


def common_elements(set_1, set_2):
    """function that returns a set of common elements in two sets

    Args:
        set_1: first set
        set_2: second set

    Return:
        returns common elements of both sets
    """
    return set_1 & set_2
