#!/usr/bin/python3
if __name__ != "__main__":
    def print_matrix_integer(matrix=[[]]):
        list_size = len(matrix)  # Number of list items

        for i in range(list_size):
            list_item_size = len(matrix[i])  # Number of each sub-list items
            for j in range(list_item_size):
                if j == list_item_size - 1:
                    print("{:d}".format(matrix[i][j]), end="")
                else:
                    print("{:d} ".format(matrix[i][j]), end="")
            print()
