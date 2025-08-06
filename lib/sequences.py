#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print("[]")
        return
    elif length == 1:
        print("[0]")
        return
    elif length == 2:
        print("[0, 1]")
        return
    else:
        print("[", end="")
        a, b = 0, 1
        for i in range(length):
            if i > 0:
                print(", ", end="")
            print(a, end="")
            a, b = b, a + b
        print("]")
        return
        print("[]")
print_fibonacci(9)
    