#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Creates square class """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes object

        Args:
            size: size of object

        """
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Returns position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets object's position

        Args:
            value: position to be set

        Raises:
            if value is not a tuple of two integers,
            TypeError exception is raised

        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            return
        else:
            if self.__position[1] > 0:
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
