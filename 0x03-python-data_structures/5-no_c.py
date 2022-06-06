#!/usr/bin/python3

if __name__ != "__main__":
    def no_c(my_string):

        for char in my_string:
            new_string = my_string.replace('c', "").replace('C', "")
        return new_string
