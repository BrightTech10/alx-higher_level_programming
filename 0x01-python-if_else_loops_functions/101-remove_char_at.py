#!/usr/bin/python3
if __name__ != "__main__":
    def remove_char_at(str, n):
        list_copy = []
        list_copy[:] = str
        new_string = ""

        for i in range(len(list_copy)):
            if i == n:
                list_copy[i] = ""
            new_string = "".join(list_copy)

        return new_string
