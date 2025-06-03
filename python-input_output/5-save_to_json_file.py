#!/usr/bin/python3
"""5. Read file"""
import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a file using JSON format."""

    with open(filename, "w") as f:
        json_str = json.dumps(my_obj)

        return f.write(json_str)
