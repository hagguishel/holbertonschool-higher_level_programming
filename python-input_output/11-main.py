#!/usr/bin/python3
"""11. Student to disk and reload"""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the student.

        If attrs is a list of strings, only the specified attributes are returned.
        Otherwise, all attributes are included.

        Args:
            attrs (list or None): List of attribute names to include.
        Returns:
            dict: Dictionary of selected or all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            my_dict = {}
            for x in attrs:
                if hasattr(self, x):
                    my_dict[x] = getattr(self, x)
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the student instance with those from a dictionary.

        Args:
            json (dict): Dictionary containing attribute names and their values.
        """
        for key, value in json.items():
            setattr(self, key, value)
