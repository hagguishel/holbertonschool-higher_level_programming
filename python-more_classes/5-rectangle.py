#!/usr/bin/python3
"""Module rectangle : définit une classe Rectangle avec aire et périmètre."""


class Rectangle:
    """Classe représentant un rectangle géométrique."""

    def __init__(self, width=0, height=0):
        """Initialise un rectangle avec une largeur et une hauteur."""

        self.width = width
        self.height = height

    def area(self):
        """Retourne l'aire du rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * self.height

    def perimeter(self):
        """Retourne le périmètre du rectangle,
        ou 0 si width ou height vaut 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Retourne une représentation en chaîne du rectangle avec des #."""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            lines = []
            for i in range(self.height):
                lines.append("#" * self.width)
            return "\n".join(lines)

    def __repr__(self):
        """Retourne une représentation officielle
        du rectangle, recréable avec eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Affiche un message lors de la suppression de l'instance."""
        print("Bye rectangle...")

    @property
    def width(self):
        """Retourne la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle avec vérifications."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
