#!/usr/bin/python3
import sys
i = 1
j = 0
if __name__ == '__main__':
    while i < len(sys.argv):
        j += int(sys.argv[i])
        i += 1
    print(j)
