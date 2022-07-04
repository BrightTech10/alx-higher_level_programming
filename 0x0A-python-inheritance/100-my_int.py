#!/usr/bin/python3
""" Defines a class Myint that inherits from class int """


class MyInt(int):
    """ Inverts the == and != operators """
    def __eq__(self, other) -> bool:
        """ Returns False for all == """
        return False

    def __ne__(self, other) -> bool:
        """ Returns True for all != """
        return True
