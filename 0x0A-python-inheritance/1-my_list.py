#!/usr/bin/python3
""" Creates MyList class """


class MyList(list):
    """ Defines a print_sorted function"""
    def print_sorted(self):
        """
        Prints a list of integers in ascending order

        Raises:
            raises a TypeError if elements of list if not
            of type int
        """

        for item in self:
            if type(item) is not int:
                raise TypeError("Elements of list must be of type int")

        new_list = sorted(self)

        for item in new_list:
            if type(item) is not int:
                raise TypeError("Elements of list must be of type int")
        print(new_list)
