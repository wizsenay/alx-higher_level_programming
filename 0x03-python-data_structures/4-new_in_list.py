#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cop_list = my_list[:]
    if 0 <= idx < len(my_list):
        cop_list[idx] = element
        return cop_list
    return my_list
