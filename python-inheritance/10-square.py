#!/usr/bin/python3
"""
Définition de la classe Square, héritée de Rectangle.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Classe représentant un carré, héritée de Rectangle."""

    def __init__(self, size):
        """Initialise un carré avec une taille unique."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
