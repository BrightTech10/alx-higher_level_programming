#!/usr/bin/python3


import re


def best_score(a_dictionary):
    if a_dictionary:
        biggest = max(a_dictionary, key=lambda key: a_dictionary[key])
        return biggest
    else:
        return None
