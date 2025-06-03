#!/usr/bin/python3
"""4. Read file"""


def from_json_string(my_str):
    """Convert a JSON string to a Python object."""
    import json

    return json.loads(my_str)
