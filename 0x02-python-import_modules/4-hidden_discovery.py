#!/usr/bin/python3
import hidden_4
copy_dir = None
if __name__ == "__main__":
    copy_dir = dir(hidden_4)
    for i in copy_dir:
        if i[0:2] != '__':
            print(i)
