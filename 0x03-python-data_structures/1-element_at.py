#!/usr/bin/python3
if __name__ != "__main__":
    def element_at(my_list, idx):
        size = len(my_list)
        if idx < 0 or idx > size:
            return None
        else:
            for i in range(size):
                if i == idx:
                    break
            return my_list[i]
