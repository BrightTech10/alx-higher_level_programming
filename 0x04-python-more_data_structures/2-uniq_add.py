#!/usr/bin/python3


def uniq_add(my_list=[]):

    """function that adds all unique integers in a list
        (only once for each integer)

    Args:
        my_list: list containing integers

    Return:
        returns sum of unique integers
    """
    new_list = list(set(my_list))  # This retrieves all unique integers
    sum = 0
    for i in range(len(new_list)):
        sum += new_list[i]
    return sum
