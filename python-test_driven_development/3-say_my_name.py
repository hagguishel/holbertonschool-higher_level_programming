#!/usr/bin/python3
"""
Prints 'My name is <first name> <last name>'.
Validates that both arguments are strings.
"""


def say_my_name(first_name, last_name=""):
    """
    Print 'My name is <first_name> <last_name>'.

    Args:
        first_name: The first name (string).
        last_name: The last name (string, optional).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
