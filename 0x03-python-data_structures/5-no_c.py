#!/usr/bin/python3

if __name__ != "__main__":
    def no_c(my_string):
        list_copy = []
        new_string = ""

        if isinstance(my_string, str):
            list_copy[:] = my_string
            for i in range(len(list_copy)):
                if list_copy[i] == 'c' or list_copy[i] == 'C':
                    list_copy[i] = ''
                new_string = "".join(list_copy)

        return new_string
