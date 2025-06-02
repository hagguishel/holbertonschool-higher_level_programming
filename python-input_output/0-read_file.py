#!/usr/bin/python3
#!/usr/bin/python3
"""
Module 0-read_file

Ce module contient une fonction qui lit un fichier texte (UTF-8)
et affiche son contenu sur la sortie standard.
"""


def read_file(filename=""):
    """
    Lit un fichier texte (UTF-8) et affiche son contenu dans le terminal.

    Argument :
        filename : nom du fichier à lire.
    """
    with open(filename, encoding="utf-8") as f:
        text = f.read()

    print(text)
