#!/usr/bin/python3
"""
This module provides a function that adds two integers.

It handles both integers and floats (by casting floats to ints).
If inputs are not int or float, it raises a TypeError.

You are not allowed to import any module.
"""


def add_integer(a, b=98):
    """
    Adds two numbers a and b

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
