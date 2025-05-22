#!/usr/bin/python3
"""Classe Rectangle avec largeur et hauteur."""


class Rectangle:
    """Représente un rectangle."""

    def __init__(self, width=0, height=0):
        """Initialise un rectangle.
        Args:
           width (int): largeur du rectangle.
           height (int): hauteur du rectangle.
        """
        self.__width = width
        self.__height = height
