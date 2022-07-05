#!/usr/bin/python3
""" Defines the method read_file """


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout

    Args:
        filename: text file to be read
    """
    with open(file=filename, mode='r', encoding='utf-8') as file:
        read = file.read()
        print(read)
