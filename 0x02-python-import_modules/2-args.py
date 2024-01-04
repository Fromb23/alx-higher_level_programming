#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) - 1 == 0:
        print("0 arguments.")
    else:
        count = len(sys.argv) - 1
        print(count, "argument:") if count == 1 else print(count, "arguments:")
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
