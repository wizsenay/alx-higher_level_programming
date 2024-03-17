#!/usr/bin/python3
import sys
i = 1
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        if len(sys.argv) == 2:
            print("{} argument:".format((len(sys.argv) - 1)))
        elif len(sys.argv) > 2:
            print("{} arguments:".format((len(sys.argv) - 1)))
        while i < len(sys.argv):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
