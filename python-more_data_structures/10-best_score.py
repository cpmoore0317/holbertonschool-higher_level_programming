#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    best_score = float('-inf')
    if a_dictionary is None or not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value > best score:
            best_score = value
            best_key = key
    return best_key
