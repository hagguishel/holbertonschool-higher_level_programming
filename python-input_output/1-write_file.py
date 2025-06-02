#!/usr/bin/python3
"""
Écrit une chaîne de caractères dans un fichier texte (UTF-8).

Retourne :
    Le nombre de caractères écrits.
"""


def write_file(filename="", text=""):
    """
    Lit un fichier texte (UTF-8) et affiche son contenu dans le terminal.

    Argument :
        filename : nom du fichier à lire.
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
