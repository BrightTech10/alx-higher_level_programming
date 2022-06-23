#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides two lists, element by element

    Args:
        my_list_1: first list
        my_list_2: second list

    Raises:
        TypeError: If an element is not an integer or float
        ZeroDivisionError: If the division (/0) can’t be done
        IndexError: If my_list_1 or my_list_2 is too short

    Return:
        returns new list with all divisions

    """
    result = list()
    for item in range(list_length):
        try:
            result.append(my_list_1[item] / my_list_2[item])
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            print(end="")

    return result
