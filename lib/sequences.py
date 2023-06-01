#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    if int(length) < 1:
        print(fib_list)
    elif int(length) < 2:
        fib_list = [0]
        print(fib_list)
    else:
        fib_list = [0, 1]
        for i in range(length - 2):
            fib_list.append(fib_list[-1] + fib_list[-2])
        print(fib_list)