#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """ Defines the function area() """
    def area(self):
        """ Raises an exception with a message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ The function validates @value
        
        Raise:
            raises TypeError if value is not an integer
            raises ValueError if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError (name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
