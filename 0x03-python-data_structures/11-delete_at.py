#!/usr/bin/python3
if __name__ != "__main__":
    def delete_at(my_list=[], idx=0):
        size = len(my_list)

        if idx >= 0 and idx < size:
            del my_list[idx]
            return my_list
        else:
            return my_list
