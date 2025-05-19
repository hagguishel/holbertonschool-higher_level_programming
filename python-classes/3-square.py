#!/usr/bin/python3
"""Module square

Ce module définit une classe Square représentant un carré géométrique
avec une taille privée et une méthode pour calculer son aire.
"""


class Square:
    """Classe représentant un carré.

    Attributs :
        __size (int) : La taille du carré, privée et validée à l'initialisation.
    """

    def __init__(self, size=0):
        """Initialise un carré avec une taille donnée.

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

    def area(self):
        """Calcule et retourne l’aire du carré.

        Returns:
            int: L’aire du carré (size * size).
        """
        return self.__size * self.__size
