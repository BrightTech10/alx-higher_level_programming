#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers

    Args:
        my_list: list
        x: number of element to print. x can be bigger than length of my_list

    Return:
        returns number of elements printed
    """
    count = 0
    for i in range(x):
        if isinstance(my_list[i], int):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (IndexError, ValueError) as error:
                print(error)
    print()
    return count
