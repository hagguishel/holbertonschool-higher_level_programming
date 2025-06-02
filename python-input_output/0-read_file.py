#!/usr/bin/python3
"""0. Read file"""


def read_file(filename=""):
    """
    Lit un fichier texte (UTF-8) et affiche son contenu dans le terminal.

    Argument :
        filename : nom du fichier à lire.
    """
    with open(filename, encoding="utf-8") as f:
        text = f.read()

    print(text)
