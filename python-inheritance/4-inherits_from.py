#!/usr/bin/python3
"""
Fonction qui vérifie si un objet hérite d'une
classe donnée (sans être exactement cette classe).
"""


def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and type(obj) is not a_class
