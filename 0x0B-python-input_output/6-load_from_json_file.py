#!/usr/bin/python3
""" Defines load_from_json_file method """
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file

    Args:
        filename: path to JSON file

    Return:
        returns created object
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
