#!/usr/bin/python3
"""
This module provides a function that prints a square using the '#' character.
It strictly validates sizes against types, limits, and decimal boundaries.
"""


def print_square(size):
    """
    Prints a square with the character # based on the provided size length.

    Args:
        size (int): The height and width length of the square layout.

    Raises:
        TypeError: If size is not an explicit integer type.
        ValueError: If size is an integer less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
