#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Creates square class """

    def __init__(self, size=0):
        """ Initializes object

        Args:
            size: size of object

        """
        self.__size = size

    @property
    def size(self):
        """ Returns object size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets object size

        Args:
            value: size to be set

        Raises:
            if size is not an integer, TypeError exception is raised
            if size is less than 0, ValuError exception is raised

        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Computes the square area

        Return:
            returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """ prints square with the character '#' in stdout """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
