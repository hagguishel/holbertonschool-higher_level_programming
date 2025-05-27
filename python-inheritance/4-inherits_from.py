#!/usr/bin/python3
"""
This module defines a function that checks if an object
is an instance of a subclass of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a subclass of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare inheritance with.

    Returns:
        True if obj is an instance of a subclass of a_class
        (excluding a_class itself), False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
