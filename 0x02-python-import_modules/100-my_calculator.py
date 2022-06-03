#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argc = len(sys.argv)
    arg = sys.argv
    if argc < 2:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(arg[1])
        b = int(arg[3])
        if arg[2] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
            sys.exit(0)
        if arg[2] == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
            sys.exit(0)
        if arg[2] == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
            sys.exit(0)
        if arg[2] == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)