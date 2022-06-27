#!/usr/bin/python3
""" Defines a rectangle """


class Rectangle:
    """ Creates rectangle class """
    def __init__(self, width=0, height=0):
        """ Initializes instance attributes
        Args:
            width: width of rectangle object
            height: height of rectangle object
        """
        self.width = width
        self.height = height

    def __str__(self) -> str:
        """ Returns printable string representation of rectangle object.
            Rectangle is represented with the # character
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            list_item = []
            for i in range(self.__height):
                [list_item.append("#") for j in range(self.__width)]
                if i == self.__height - 1:
                    break
                list_item.append("\n")
            return "".join(list_item)

    @property
    def width(self):
        """ Retrieves width of rectangle object """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width of rectangle object

        Args:
            value: width value of rectangle (int)

        Raises:
            raises TypeError if value is not an integer
            raises ValueError if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns height of rectangle object """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height of rectangle object

        Args:
            value: height value of rectangle (int)

        Raises:
            raises TypeError if value is not an integer
            raises ValueError if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Computes and returns the area of a rectangle object """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Computes the perimeter of a rectangle object

        Return:
            returns perimeter as 0 if either width or height is 0
            else returns calculated perimeter
        """
        perim = 0
        if self.__width == 0 or self.__height == 0:
            return perim
        else:
            perim = 2 * (self.__width + self.__height)
            return perim
