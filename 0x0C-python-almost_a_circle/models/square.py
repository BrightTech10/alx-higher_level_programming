#!/usr/bin/python3
""" Module rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes instance variables

        Args:
            size: size of Square object
            with dimensions width == height
            x:
            y:
            id: identification number
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size <= 0:
            raise ValueError("size must be > 0")

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

        if type(y) is not int:
            raise TypeError("x must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """ Return string representation of class
        name and instance attributes
        """
        return f"[{self.__class__.__name__}] ({self.id})"\
               f" {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Get Square object """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set Square object size

        Args:
            value: value of object size
        """
        self.width = value

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
                if key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
        else:
            value = []
            for item in args:
                value.append(item)
            if value is not None:
                self.id = value[0]
                if len(value) == 2:
                    self.width = value[1]
                if len(value) == 3:
                    self.width = value[1]
                    self.x = value[2]
                if len(value) == 4:
                    self.width = value[1]
                    self.x = value[2]
                    self.y = value[3]
                if len(value) >= 5:
                    self.width = value[1]
                    self.x = value[2]
                    self.y = value[3]

        if type(self.id) is not int:
            raise TypeError("id must be an integer")
        if self.id < 0:
            raise TypeError("id must be > 0")

        if type(self.width) is not int:
            raise TypeError("size must be an integer")
        elif self.width <= 0:
            raise ValueError("size must be > 0")

        if type(self.x) is not int:
            raise TypeError("x must be an integer")
        elif self.x < 0:
            raise ValueError("x must be >= 0")

        if type(self.y) is not int:
            raise TypeError("y must be an integer")
        elif self.y < 0:
            raise ValueError("y must be >= 0")

        return f"[{self.__class__.__name__}] ({self.id})"\
               f" {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y,
        }
