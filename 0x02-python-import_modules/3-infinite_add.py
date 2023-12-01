#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum_result = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            sum_result += int(arg)
    print(sum_result)
