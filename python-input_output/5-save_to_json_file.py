#!/usr/bin/python3

"""
Script
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
