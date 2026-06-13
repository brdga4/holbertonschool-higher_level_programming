#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        new_dic = list(a_dictionary)
        a_dictionary.append((key, value))
        dict(a_dictionary)
