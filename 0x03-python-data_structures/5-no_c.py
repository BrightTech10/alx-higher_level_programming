#!/usr/bin/python3

if __name__ != "__main__":
    def no_c(my_string):
        list_copy = []
        list_copy[:] = my_string
        string_copy = ""

        for i in range(len(list_copy)):
            if list_copy[i] == 'c' or list_copy[i] == 'C':
                list_copy[i] = ''
            new_string = "".join(map(str, list_copy))

        return new_string
