#!/usr/bin/python3
"""
Définition d'une classe de base pour la géométrie.

Contient :
- une méthode area non implémentée,
- une méthode integer_validator pour valider les entiers strictement positifs.
"""


class BaseGeometry:
    """Classe de base pour la géométrie."""

    def area(self):
        """Lève une exception car la méthode n'est pas implémentée."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide que value est un entier strictement positif.

        Args:
            name (str): Le nom de la valeur.
            value (int): La valeur à valider.

        Raises:
            TypeError: si value n'est pas un entier.
            ValueError: si value est <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
