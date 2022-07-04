#!/usr/bin/python3
""" A Rectangle class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from a base class

    Args:
        BaseGeometry: base class from which Rectangle class inherits
    """
    def __init__(self, width, height):
        """
        Initializes instance attributes.
        Method also validates @width and @height
        using the integer_validator method

        Args:
            width: width of Rectangle object
            height: height of Rectangle object
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def __str__(self) -> str:
        """ Returns a Rectangle description """
        return "[" + str(self.__class__.__name__) + "] "\
               + str(self.__width) + "/" + str(self.__height)

    def area(self):
        """ Implements the area method and returns result """
        return (self.__width * self.__height)
