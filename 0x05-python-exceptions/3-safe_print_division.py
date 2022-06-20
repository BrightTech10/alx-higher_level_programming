#!/usr/bin/python3


def safe_print_division(a, b):
    """divides 2 integers and prints the result.

    Args:
        a: first integer
        b: second integer

    Return:
        returns value of division, else None
    """
    div = 0
    if isinstance(a, int) and isinstance(b, int):
        try:
            if b != 0:
                div = a / b
                return div
            else:
                div = None
        except (TypeError, ZeroDivisionError) as error:
            pass
        finally:
            print("Inside result: {}".format(div))
    else:
        return None
