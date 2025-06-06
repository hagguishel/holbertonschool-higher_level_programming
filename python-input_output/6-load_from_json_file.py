#!/usr/bin/python3
"""5. Read file"""
import json


def load_from_json_file(filename):
    """Load a Python object from a JSON file."""

    with open(filename, "r") as f:
        return json.load(f)
