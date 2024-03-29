#!/usr/bin/python3
import calculator_1
import sys
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opretor = sys.argv[2]
    if opretor not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif opretor == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif opretor == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif opretor == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif opretor == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
