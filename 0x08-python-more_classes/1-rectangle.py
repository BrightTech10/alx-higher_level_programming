#!/usr/bin/python3
""" Defines a rectangle """


class Rectangle:
    """ Creates rectangle class """
    def __init__(self, width=0, height=0) -> None:
        """ Initializes instance attributes
        Args:
            width: width of rectangle object
            height: height of rectangle object
        """
        self.width = width
        self.height = height

    def __str__(self) -> str:
        """ Prints string representation of object """
        print("{'_Rectangle__height': " + self.__height +
              ", '_Rectangle_width': " + self.__width + "}")

    @property
    def width(self):
        """ Returns width of rectangle object """
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
