#!/usr/bin/python3

"""
Script
"""


def write_file(filename="", text=""):
    """
    Function
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
