#!/usr/bin/python3
"""
Module that defines the lookup function
"""


class MyList(list):
    """Classe qui hérite de la classe list.

    Cette classe ajoute une méthode pour afficher la liste triée
    sans modifier l'ordre original de la liste.
    """

    def print_sorted(self):
        """Affiche la liste triée en ordre croissant."""
        print(sorted(self))
