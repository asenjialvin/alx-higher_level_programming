#!/usr/bin/python3
def fizzbuzz():
    for str in range(1, 101):
        if ((str % 3) == 0) and ((str % 5) == 0):
            print("FizzBuzz ", end="")
        elif (str % 3) == 0:
            print("Fizz ", end="")
        elif (str % 5) == 0:
            print("Buzz ", end="")
        else:
            print(f"{str} ", end="")
