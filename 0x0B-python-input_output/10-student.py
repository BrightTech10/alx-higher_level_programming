#!/usr/bin/python3
""" 10-student module
"""


class Student:
    """ Defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiates instance attributes

        Args:
            first_name: first name of student
            last_name: last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs: a list of strings
        """

        if attrs is None or not all(type(item) is str for item in attrs):
            return self.__dict__
        dic = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                dic[key] = value
                return dic
