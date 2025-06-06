#!/usr/bin/python3
"""7. Load, add, save

Script qui ajoute tous les arguments passés à la ligne de commande
à une liste JSON sauvegardée dans le fichier add_item.json.
Utilise les fonctions save_to_json_file et load_from_json_file.
"""

from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

conteneur = argv[1:]

try:
    pelo = load_from_json_file("add_item.json")
except FileNotFoundError:
    pelo = []

pelo.extend(conteneur)
save_to_json_file(pelo, "add_item.json")
