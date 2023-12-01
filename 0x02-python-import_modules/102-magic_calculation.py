#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a > b:
        result = a + b
    else:
        result = (a - b) * 2
    return result
dis.dis(magic_calculation)
