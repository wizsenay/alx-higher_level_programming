#!/usr/bin/python3
def uppercase(str):
    last_len = len(str) - 1
    uperr = ""
    for i in str:
        if (97 <= ord(i)) and (ord(i) < 123):
            j = chr(ord(i) - 32)
            uperr += "{}".format(j) 
        else:
            uperr += "{}".format(i)

    print(uperr)
