#!/usr/bin/python3
"""
Script
"""

import json


def load_from_json_file(filename):
    """
    Function
    """
    with open(filename, encoding="utf-8"):
        json.load(filename)
