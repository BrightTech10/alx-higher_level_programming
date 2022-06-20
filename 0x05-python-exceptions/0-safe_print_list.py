#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list

    Args:
        my_list: list
        x: number of element to print. x can be bigger than length of my_list

    Return: number of elements printed
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count = count + 1
        except IndexError:
            pass
    print()
    return count
