#!/usr/bin/python3
""" This modules prints a user's name """


def say_my_name(first_name, last_name=""):
    """
    Print first and last names of a user

    Args:
        first_name: user's first name
        last_name: user's last name

    Raises:
        raises TypeError if first or last name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
