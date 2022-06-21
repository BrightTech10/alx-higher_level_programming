#!/usr/bin/python3
class Square:
    """ Defines a square

        Attribute:
            size: private instance attribute
            if size is not an integer, TypeError exception is raised
            if size is less than 0, ValuError exception is raised

    """
    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
