#!/usr/bin/python3
"""Create a class Student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Public instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Representation json of student class"""
        if type(attrs) is list:
            new_dict = {}
            for key in self.__dict__:
                for key2 in attrs:
                    if key == key2:
                        new_dict[key] = self.__dict__[key]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """function that replace all attr"""
        self.__dict__.update(json)
