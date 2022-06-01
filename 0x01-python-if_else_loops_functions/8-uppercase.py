#!/usr/bin/python3
def uppercase(str):
    str_up = ''
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        else:
            i = chr(ord(i))
        str_up = str_up + i
    print(str_up)
