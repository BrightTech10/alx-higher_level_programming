#!/usr/bin/python3
""" Defines the to_json_string method """
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj: object to be represented
    """
    return (json.dumps(my_obj))
