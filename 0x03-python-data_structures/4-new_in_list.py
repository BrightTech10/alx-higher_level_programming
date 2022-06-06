#!/usr/bin/python3
if __name__ != "__main__":
    def new_in_list(my_list, idx, element):
        copy_list = list.copy(my_list)
        size = len(copy_list)

        if idx >= 0 and idx < size:
            copy_list[idx] = element
            return copy_list
        else:
            return my_list
