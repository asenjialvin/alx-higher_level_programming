#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    argc = len(sys.argv[1:])
    operators_arr = ['+', '-', '*', '/']
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operators_arr:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        operator = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if operator == "+":
            ans = add(a, b)
        elif operator == "-":
            ans = sub(a, b)
        elif operator == "*":
            ans = mul(a, b)
        elif operator == "/":
            ans = div(a, b)
        else:
            print("Operator is invalid")
        print("{} {} {} = {}".format(a, operator, b, ans))
