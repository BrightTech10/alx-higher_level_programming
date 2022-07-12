#!/usr/bin/python3
""" Module base
"""
import json


class Base:
    """ A parent class """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes instance attribute

        Args:
            id: identification number
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
            list_objs: a list of instances
        """
        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_objs_dict = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_objs_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of a JSON string representation

        Args:
            json_string: a string representing a list of dictionaries

        Return:
            if @json_string is None or empty, an empty list is returned
            otherwise a list represented by @json_string is returned
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set

        Args:
            dictionary: a dictionary representation of a class
        """
        if not dictionary and dictionary == {}:
            return
        if cls.__name__ == 'Rectangle':
            dum_obj = cls(2, 4)  # a dummy instance
        elif cls.__name__ == 'Square':
            dum_obj = cls(5)  # a dummy instance
        dum_obj.update(**dictionary)
        return dum_obj

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from ``<cls.__name__>.json``.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as json_file:
                file_objs = Base.from_json_string(json_file.read())
                return [cls.create(**obj) for obj in file_objs]
        except IOError:
            return []
