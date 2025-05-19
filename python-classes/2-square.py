#!/usr/bin/python3
"""Module square

Ce module définit une classe Square représentant un carré avec une taille,
et qui assure que cette taille est un entier positif ou nul.
"""


class Square:
    """Classe représentant un carré géométrique.

    Attributs privés :
        __size (int) : La taille du carré (doit être un entier >= 0).
    """

    def __init__(self, size=0):
        """Initialise un nouveau carré avec une taille donnée.

        Args:
            size (int, optionnel) : La taille du carré (par défaut 0).

        Raises:
            TypeError: Si size n’est pas un entier.
            ValueError: Si size est négatif.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
