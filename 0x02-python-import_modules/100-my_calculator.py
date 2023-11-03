#!/usr/bin/python3


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = sys.argv[2]
    operators = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
        }
    

    if operator in operators:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        result = operators[operator](a, b)
        print(f"{a} {operator} {b} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
