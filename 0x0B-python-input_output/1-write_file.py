#!/usr/bin/python3
"""" Defines the method write_file """


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
        filename: file to be written to
        text: string to be written

    Return:
        returns number of characters written
    """
    with open(file=filename, mode='w', encoding='utf-8') as file:
        a_file = file.write(text)
        return a_file
