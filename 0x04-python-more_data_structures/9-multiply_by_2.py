#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    # new_dictionary = {}
    # for key, val in a_dictionary.items():
    #    if val % 2 == 0:
    #        new_dictionary[key] = val * 2
    new_dictionary = {
        key: value * 2
        for key, value in a_dictionary.items()
    }

    return new_dictionary
