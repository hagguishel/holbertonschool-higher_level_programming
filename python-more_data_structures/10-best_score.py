#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_score = None
    best_name = None
    for key, valeur in a_dictionary.items():
        if best_score is None or valeur > best_score:
            best_score = valeur
            best_name = key
    return best_name
