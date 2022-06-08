#!/usr/bin/python3


def search_replace(my_list, search, replace):

    """replaces all occurrences of an element by another in a new list

    Args:
        my_list: the initial list
        search: the element to replace in the list
        replace: the new element

    Return: returns updated list
    """
    return [item if (item != search) else replace for item in my_list]
