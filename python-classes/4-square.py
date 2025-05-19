#!/usr/bin/python3
"""Module square

Ce module contient la définition de la classe Square,
qui représente un carré géométrique avec une taille privée,
un accès contrôlé à cette taille, et une méthode pour calculer son aire.
"""


class Square:
    """Classe représentant un carré.

    Attributs privés :
        __size (int): La taille du carré, protégée par un getter et un setter.
    """

    def __init__(self, size=0):
        """Initialise un nouveau carré avec une taille donnée.

        Args:
            size (int, optionnel): La taille du carré (par défaut 0).

        Raises:
            TypeError: Si size n’est pas un entier.
            ValueError: Si size est négatif.
        """
        self.size = size

    def area(self):
        """Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré, calculée comme size * size.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Accède à la taille actuelle du carré.

        Returns:
            int: La taille du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Modifie la taille du carré avec validation.

        Args:
            value (int): La nouvelle taille du carré.

        Raises:
            TypeError: Si la valeur n’est pas un entier.
            ValueError: Si la valeur est négative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
