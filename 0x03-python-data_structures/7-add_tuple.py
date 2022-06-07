#!/usr/bin/python3
"""Function that adds 2 tuples

Args:
    tuple_a: first tuple
    tuple_b: second tuple

Returns:
    A tuple with two integers
    (the sum of the first and second tuples)
"""

if __name__ != "__main__":
    def add_tuple(tuple_a=(), tuple_b=()):
        new_tuple = ()
        value1 = (0, )
        value2 = (0, 0)
        if isinstance(tuple_a, tuple) and isinstance(tuple_b, tuple):
            if len(tuple_a) == 1 or len(tuple_b) == 1:
                tuple_a = tuple_a + value1
                tuple_b = tuple_b + value1

            elif len(tuple_a) == 0 or len(tuple_b) == 0:
                tuple_a = tuple_a + value2
                tuple_b = tuple_b + value2

            new_tuple = tuple(map(sum, zip(tuple_a, tuple_b)))
            return new_tuple
