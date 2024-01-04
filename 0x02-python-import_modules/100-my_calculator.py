#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if len(sys.argv) < 3:
        print(sys.argv[0], sys.argv[1], "operator", sys.argv[2])
        exit(1)

    if not sys.argv[1].isdigit() or not sys.argv[3].isdigit():
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))

    elif sys.argv[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))

    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))

    elif sys.argv[2] == "/":
        if b == 0:
            sys.exit(1)
        print("{} / {} = {}".format(a, b, div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
