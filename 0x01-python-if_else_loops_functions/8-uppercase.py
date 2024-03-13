#!/usr/bin/python3
def uppercase(str):
    upper_case = ''
    charch = None
    for i in str:
        if ord(i) >= 65 and ord(i) <= 90:
            upper_case += "{}".format(i)
        elif ord(i) >= 97 and ord(i) <= 122:
            charch = ord(i) - 32
            upper_case += "{:c}".format(charch)
        else:
            upper_case += "{}".format(i)
    print(upper_case)

