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

    def to_json(self):
        return self.__dict__
