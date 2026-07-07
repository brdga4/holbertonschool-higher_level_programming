#!/usr/bin/python3

"""
Script
"""


def read_file(filename=""):
    """
    Function
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file, end="")
