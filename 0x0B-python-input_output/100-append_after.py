#!/usr/bin/python3
""" 100-append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename: path to file
        search_string: specific string to be searched
        new_string: new string to be inserted
    """
    a_file = open(filename, encoding='utf-8').readlines()

    with open(filename, 'w', encoding='utf-8') as write_file:
        for a_line in a_file:
            write_file.write(a_line)
            if search_string in a_line:
                write_file.write(new_string)
