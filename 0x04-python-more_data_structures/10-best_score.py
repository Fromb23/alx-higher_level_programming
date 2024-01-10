#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        try:
            max_key = max(a_dictionary, key=a_dictionary.get)
        except ValueError:
            max_key = None
        return max_key
    else:
        return None
