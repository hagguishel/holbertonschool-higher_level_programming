#!/usr/bin/python3
import sys

if __name__ == "__main__":
    addition = 0

    for i in range(1, len(sys.argv)):
        addition += int(sys.argv[i])

    print(addition)
