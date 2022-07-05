#!/usr/bin/python3
""" Defines save_to_json_file method """
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object using a JSON representation

    Args:
        my_obj: object to be represented in JSON
        filename: path to file
    """
    # writing to @filename
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json.JSONEncoder().encode(my_obj))
