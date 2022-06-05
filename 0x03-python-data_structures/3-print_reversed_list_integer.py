#!/usr/bin/python3
if __name__ != "__main__":
    def print_reversed_list_integer(my_list=[]):
        # to access individual elements in reversed order
        for i in list(reversed(my_list)):
            print("{:d}".format(i))
