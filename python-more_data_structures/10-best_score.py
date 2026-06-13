#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return ("None")
    sorted_list = sorted(list(a_dictionary.values()))
    highest_val = sorted_list[-1]
    for key, value in a_dictionary.items():
        if highest_val == value:
            return (key)
