#!/usr/bin/python3
def print_last_digit(number):
    last_digit = None
    for i in str(number):
        last_digit = i
    print(int(last_digit), end="")
    return int(last_digit)
