#!/usr/bin/python3
"""
This module adds two numbers and returns result
"""


def add_integer(a, b=98):
    """
    Computes the sum of two numbers and returns the result.
    Argument is casted into an integer if any is a float

    Args:
        a: first number (int or float)
        b: second number (int or float)

    Raises:
        raises TypeError if a is not an integer or float
        raises TypeError if b is not an integer or float

    Return:
        returns sum of integers

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
