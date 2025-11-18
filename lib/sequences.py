#!/usr/bin/env python3

def print_fibonacci(length):
    # generate the first `length` Fibonacci numbers and print as a list
    if length <= 0:
        print([])
        return

    fib = [0]
    if length == 1:
        print(fib)
        return

    fib.append(1)
    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])

    print(fib)