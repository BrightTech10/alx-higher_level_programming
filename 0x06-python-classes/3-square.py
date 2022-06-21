#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Creates square class """

    def __init__(self, size=0):
        """ Initializes object

        Args:
            size: size of object
            if size is not an integer, TypeError exception is raised
            if size is less than 0, ValuError exception is raised
        """
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Computes the square area

        Return:
            returns the current square area
        """
        return self.__size ** 2
