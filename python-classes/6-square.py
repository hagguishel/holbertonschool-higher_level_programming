#!/usr/bin/python3
"""Module square

Classe Square qui permet de définir un carré
avec une taille et une position.
"""


class Square:
    """Représente un carré avec taille et position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise le carré avec size et position."""
        self.size = size
        self.position = position

    def area(self):
        """Retourne l’aire du carré."""
        return self.__size * self.__size

    def my_print(self):
        """Affiche le carré avec des # en tenant compte de la position."""
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    @property
    def size(self):
        """Retourne la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille du carré avec vérification."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retourne la position du carré."""
        return self.__position

    @position.setter
    def position(self, value):
        """Définit la position avec vérification."""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
