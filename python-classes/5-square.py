#!/usr/bin/python3
"""Module square

Ce module contient la classe Square qui permet de représenter un carré.
Il inclut des fonctionnalités de calcul d'aire, de validation de taille
et d'affichage textuel du carré avec des caractères `#`.
"""


class Square:
    """Classe représentant un carré géométrique.

    Attributs privés :
        __size (int) : La taille du carré (doit être un entier ≥ 0).
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
            int: L’aire du carré (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """Affiche une représentation du carré avec le caractère `#`.

        Affiche dans la sortie standard un carré de `size` lignes sur `size` colonnes.
        Si la taille du carré est 0, affiche simplement une ligne vide.

        Exemple:
            >>> s = Square(3)
            >>> s.my_print()
            ###
            ###
            ###
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)

    @property
    def size(self):
        """Récupère la taille actuelle du carré.

        Returns:
            int: La taille actuelle du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Modifie la taille du carré avec vérification de validité.

        Args:
            value (int): Nouvelle taille à assigner au carré.

        Raises:
            TypeError: Si value n’est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
