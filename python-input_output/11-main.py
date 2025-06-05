#!/usr/bin/python3
"""Module defining the Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation, filtered by attrs if provided."""
        if type(attrs) is not list:
            return self.__dict__

        dic_vide = {}
        for attr in attrs:
            if hasattr(self, attr):
                dic_vide[attr] = getattr(self, attr)
        return dic_vide

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
