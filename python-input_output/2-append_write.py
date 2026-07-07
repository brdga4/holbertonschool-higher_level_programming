#!/usr/bin/python3

"""
Script
"""


def append_write(filename="", text=""):
    """
    Function
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
