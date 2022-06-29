#!/usr/bin/python3
""" This module prints a square """


def print_square(size):
    """
    Prints a square with character #

    Args:
        size: size of square

    Raises:
        raises TypeError if size is not an int
        raises ValueError if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
