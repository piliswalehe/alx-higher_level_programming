#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv) - 1
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        from calculator_1 import add, sub, mul, div
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])

        result = None
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operator == '*':
            result = mul(a, b)
        elif operator == '/':
           result = div(a, b) 
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

            print(f"{a} {operator} {b} = {result}")
