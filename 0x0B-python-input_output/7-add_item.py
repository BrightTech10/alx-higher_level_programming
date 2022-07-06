#!/usr/bin/python3
""" Module 7-add_item.py """
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'
list_obj = []
try:
    my_list = load_from_json_file(filename)
except Exception:
    save_to_json_file(list_obj, filename)

arg_length = len(argv)

if arg_length > 1:
    for i in range(1, arg_length):
        list_obj.append(argv[i])

    save_to_json_file(list_obj, filename)
