#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    if a > b:
        result = a + b
    else:
        result = (a - b) * 2
    return result
