#!/usr/bin/python3
"""7. Load, add, save

Script qui ajoute tous les arguments passés à la ligne de commande
à une liste JSON sauvegardée dans le fichier add_item.json.
Utilise les fonctions save_to_json_file et load_from_json_file.
"""

import sys  # Pour récupérer les arguments en ligne de commande
from json.decoder import JSONDecodeError  # Pour gérer le cas où le fichier est vide

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"

# Essaye de charger la liste depuis le fichier, ou initialise une liste vide
try:
    my_list = load_from_json_file(filename)
except (FileNotFoundError, JSONDecodeError):
    my_list = []

# Ajoute les nouveaux arguments passés au script
my_list.extend(sys.argv[1:])

# Sauvegarde la liste mise à jour dans le fichier JSON
save_to_json_file(my_list, filename)
