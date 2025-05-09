#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argument_count = len(sys.argv) - 1

    if argument_count == 0:
        print("0 arguments.")
    elif argument_count == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argument_count))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
