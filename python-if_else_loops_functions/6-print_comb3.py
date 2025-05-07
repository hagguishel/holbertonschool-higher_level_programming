#!/usr/bin/python3
for i in range(10):
    for y in range(i + 1, 10):
        if i == 8 and y == 9:
            print("{:d}{:d}".format(i, y))
        else:
            print("{:d}{:d}".format(i, y), end=", ")
