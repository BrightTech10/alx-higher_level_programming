#!/usr/bin/python3
if __name__ != "__main__":
    def replace_in_list(my_list, idx, element):
        size = len(my_list)
        if idx < 0 or idx > size:
            return my_list
        else:
            my_list[idx] = element
            return my_list
