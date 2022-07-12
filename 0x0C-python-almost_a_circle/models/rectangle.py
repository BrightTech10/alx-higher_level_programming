#!/usr/bin/python3
""" Module rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes instance variables

        Args:
            width: width of Rectangle object
            height: height of Rectangle object
            x:
            y:
            id: identification number
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def __str__(self) -> str:
        """ Return string representation of class
        name and instance attributes
        """
        return f"[{self.__class__.__name__}] ({self.id})"\
               f" {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    @property
    def width(self):
        """ Gets width of Rectangle object """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets width of Rectangle object

        Args:
            width: width of rectangle object
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Gets height of Rectangle object """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets height of Rectangle object

        Args:
            height: height of rectangle object
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Gets x co-ordinate of Rectangle object """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets x co-ordinate of Rectangle object

        Args:
            value: int value used to set x co-ordinate
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets y co-ordinate of Rectangle object """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets y co-ordinate of Rectangle object

        Args:
            value: int value used to set y co-ordinate
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Computes and returns the area value
            of Rectangle instances
        """
        return (self.__width * self.__height)

    def display(self):
        """ Prints a Rectangle instance with character # """
        space = " " * self.__x
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(f"{space}", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        Updates the value of attributes

        Args:
            args: non-keyworded variable-length arguments
            kwargs: keyworded variable-length argument
        """
        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
        else:
            value = []
            for item in args:
                value.append(item)
            if value is not None:
                self.id = value[0]
                if len(value) == 2:
                    self.__width = value[1]
                if len(value) == 3:
                    self.__width = value[1]
                    self.__height = value[2]
                if len(value) == 4:
                    self.__width = value[1]
                    self.__height = value[2]
                    self.__x = value[3]
                if len(value) >= 5:
                    self.__width = value[1]
                    self.__height = value[2]
                    self.__x = value[3]
                    self.__y = value[4]
        if type(self.id) is not int:
            raise TypeError("id must be an integer")
        if self.id < 0:
            raise TypeError("id must be > 0")
        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        elif self.__width <= 0:
            raise ValueError("width must be > 0")

        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        elif self.__height <= 0:
            raise ValueError("height must be > 0")

        if type(self.__x) is not int:
            raise TypeError("x must be an integer")
        elif self.__x < 0:
            raise ValueError("x must be > 0")

        if type(self.__y) is not int:
            raise TypeError("y must be an integer")
        elif self.__y < 0:
            raise ValueError("y must be > 0")

        return f"[{self.__class__.__name__}] ({self.id})"\
               f" {self.x}/{self.y} - {self.__width}/{self.__height}"

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
