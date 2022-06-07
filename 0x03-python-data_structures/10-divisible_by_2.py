#!/usr/bin/python3
if __name__ != "__main__":
    def divisible_by_2(my_list=[]):
        new_list = []

        if isinstance(my_list, list):
            new_list[:] = my_list
            for i in range(len(new_list)):
                if new_list[i] % 2 == 0:
                    new_list[i] = True
                else:
                    new_list[i] = False
            return new_list
