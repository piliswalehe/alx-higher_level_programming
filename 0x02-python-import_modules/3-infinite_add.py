#!/usr/bin/python3
if __ name__ == "__main":
    import sys
    sum_result = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            sum_ result += int(arg)
            print(sum_result)
