#!/usr/bin/python3
from sys import exit, argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argc = len(argv)
    if argc < 2:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    operators = ['+', '-', '*', '/']
    functions = [add(a, b), sub(a, b), mul(a, b), div(a, b)]

    # when user's input(intended operator) does
    # not match any item in operators tuple
    if not (argv[2] in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    # when user's input matches item in operator tuple
    # the corresponding function is executed
    for op, func in zip(operators, functions):
        if op == argv[2]:
            break
    print(f"{a} {argv[2]} {b} = {func}")
    exit(0)
