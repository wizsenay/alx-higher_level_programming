#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boo_list = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            boo_list[count] = True
        else:
            boo_list[count] = False
    return(boo_list)
