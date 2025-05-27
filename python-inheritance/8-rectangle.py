#!/usr/bin/python3
"""Définition d'un rectangle basé sur BaseGeometry."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Classe Rectangle qui hérite de BaseGeometry."""

    def __init__(self, width, height):
        """Initialise un rectangle avec une largeur et une hauteur.

        Les valeurs sont validées à l'aide de integer_validator
        hérité de BaseGeometry.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
