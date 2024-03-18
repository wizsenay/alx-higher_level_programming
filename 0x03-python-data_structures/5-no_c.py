#!/usr/bin/python3
def no_c(my_string):
    new_ste = ""
    for i in my_string:
        if (i != 'c') and (i != 'C'):
            new_ste += i
    return (new_ste)
