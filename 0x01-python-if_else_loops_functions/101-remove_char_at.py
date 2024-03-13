#!/usr/bin/python3
def remove_char_at(str, n):
    copy_str = ""
    if len(str) <= n or n < 0:
        return str
    for i in str:
        if str[n] != i:
            copy_str += i
    return copy_str

