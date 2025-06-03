#!/usr/bin/python3
"""7. Load, add, save"""


def class_to_json(obj):
    """
    Returns the dictionary description of a simple Python object
    for JSON serialization.

    Args:
        obj: An instance of a class with only serializable attributes.

    Returns:
        dict: A dictionary of all instance attributes.
    """
    return obj.__dict__
