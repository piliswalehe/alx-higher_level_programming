#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for y in range(1, 4):
        try:
            if y > a:
                raise Exception('Too far')
            else:
                res += (a ** b) / y
        except Exception:
            res = a + b
            break
        return res
