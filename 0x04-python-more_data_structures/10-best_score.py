#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    inKey = None
    inVal = 0
    for key, val in a_dictionary.items():
        if val > inVal:
            inVal = val
            inKey = key
    return inKey
