#!/usr/bin/python3
""" Defines save_to_json_file method """
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to be written
        filename: path to file
    """

    json_obj = json.dumps(my_obj)  # serializing json

    # writing to @filename
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json_obj)
