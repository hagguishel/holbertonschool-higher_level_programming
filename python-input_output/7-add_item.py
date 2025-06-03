#!/usr/bin/python3
"""7. Load, add, save"""

import sys  # Pour récupérer les arguments passés en ligne de commande
import os  # Pour vérifier si le fichier existe
from save_to_json_file import (
    save_to_json_file,
)  # Fonction pour sauvegarder une liste en JSON
from load_from_json_file import (
    load_from_json_file,
)  # Fonction pour charger une liste depuis un fichier JSON

filename = "add_item.json"  # Nom du fichier où la liste est stockée

# Vérifie si le fichier existe pour le charger, sinon initialise une liste vide
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Ajoute les arguments passés en ligne de commande à la liste
my_list.extend(sys.argv[1:])

# Sauvegarde la liste mise à jour dans le fichier JSON
save_to_json_file(my_list, filename)
2
