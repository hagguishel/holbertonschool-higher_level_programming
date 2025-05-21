#!/usr/bin/python3
"""Module square

Ce module définit une classe Square qui
représente un carré avec une taille donnée.
"""


class Square:
    """Classe représentant un carré géométrique.

    Attributs :
        __size (int) : La taille privée du carré.
        Accessible uniquement depuis la classe.
    """

    def __init__(self, size):
        """Initialise un nouvel objet Square avec une taille donnée.

        Args:
            size (int): La taille du carré
            (aucune vérification de type ou de valeur ici).
        """
        self.__size = size
