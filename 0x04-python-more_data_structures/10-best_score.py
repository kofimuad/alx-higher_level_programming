#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns the best score"""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)

    max_key = list(a_dictionary.keys())[0]
    maxi = a_dictionary[ret]
    for key, value in a_dictionary.items():
        if value > maxi:
            maxi = value
            max_key = key
    return (max_key)
