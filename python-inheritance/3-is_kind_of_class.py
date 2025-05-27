#!/usr/bin/python3
"""
Module that defines the lookup function
"""


def is_kind_of_class(obj, a_class):
    """Vérifie si obj est une instance ou une instance héritée de a_class."""
    return isinstance(obj, a_class)
