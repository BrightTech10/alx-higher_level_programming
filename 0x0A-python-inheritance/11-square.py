#!/usr/bin/python3
""" A Rectangle class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from a base class

    Args:
        Rectangle: base class from which Square class inherits
    """
    def __init__(self, size):
        """
        Initializes an instance attribute.
        Method also validates @size
        using the integer_validator method
        """
        self.__size = size
        super().integer_validator("size", size)

    def __str__(self) -> str:
        """ Returns a Rectangle description """
        return "[" + str(self.__class__.__name__) + "] "\
               + str(self.__size) + "/" + str(self.__size)

    def area(self):
        """ Implements the area method and returns result """
        return (self.__size * self.__size)
