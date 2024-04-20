#!/usr/bin/python3
def uppercase(str):
    last_len = len(str) - 1
    for i in str:
        if (97 <= ord(i)) and (ord(i) < 123):
            j = chr(ord(i) - 32)
            print(f"{j}", end="")
        else:
            print(i, end="")

    print()
