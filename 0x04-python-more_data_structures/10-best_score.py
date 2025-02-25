#!/usr/bin/python3


def best_score(a_dictionary):
    num = 0
    name = ''
    if a_dictionary is None:
        return None
    for key, val in a_dictionary.items():
        if val > num:
            num = val
            name = key

    return name
