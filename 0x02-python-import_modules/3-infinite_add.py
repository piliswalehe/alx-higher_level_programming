#!/usr/bin/python3
if __ name__ == "__main":
    import sys
    args = sys.argv[1:]
    sum_result = sum(int(arg) for arg in args)
    print(sum_result)
