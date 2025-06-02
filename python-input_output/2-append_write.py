#!/usr/bin/python3
"""
Module 2-append_write

Ce module contient une fonction qui ajoute une chaîne à la fin
d’un fichier texte (UTF-8) et retourne le nombre de caractères ajoutés.
"""


def append_write(filename="", text=""):
    """
    Ajoute une chaîne à la fin d’un fichier texte (UTF-8).

    Retourne :
        Le nombre de caractères ajoutés.
    """
    with open(filename, "a") as f:
        return f.write(text)
