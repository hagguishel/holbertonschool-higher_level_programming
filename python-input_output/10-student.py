#!/usr/bin/python3
"""My class module"""


class Student:
    """Defines a Student class with public attributes:
    - first_name
    - last_name
    - age

    Includes a method to_json() that returns a dictionary
    representation of the instance.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs):
        """
        Returns a dictionary representation of the instance.

        If attrs is a list of strings,
        returns only the attributes named in the list.
        Otherwise, returns all attributes.
        """
        if type(attrs) is list and all(type(elem) == str for elem in attrs):
            pass
        else:
            return self.__dict__

        filtered = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered[attr] = getattr(self, attr)
        return filtered
