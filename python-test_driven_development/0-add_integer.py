#!/usr/bin/python3
"""
This module provides a function that adds two numbers together.
It handles integers and floats safely, ensuring strict type checks.
It is part of the Holberton/ALX Python TDD curriculum.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
