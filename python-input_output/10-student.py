#!/usr/bin/python3
"""10. Student to JSON with filter"""


class Student:
    """Class that defines a student with public attributes."""

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

        If attrs is a list of strings, only those attributes will be included.
        Otherwise, all attributes will be returned.

        Args:
            attrs (list or None): List of attribute names to include.
        Returns:
            dict: Dictionary representation of the instance.
        """
        # Si attrs est une liste de chaînes
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            my_dict = {}
            # Pour chaque nom dans la liste
            for x in attrs:
                # On vérifie que l'attribut existe dans l'objet
                if hasattr(self, x):
                    # On récupère sa valeur et on l'ajoute au dictionnaire
                    my_dict[x] = getattr(self, x)
            return my_dict

        # Sinon, on retourne tous les attributs de l'objet
        return self.__dict__
