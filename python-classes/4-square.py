#!/usr/bin/python3
"""This module defines a simple, empty Square class.

It serves as the foundational step for learning Object-Oriented Programming
and class definitions in Python.
"""


class Square:
    """Represents a square shape.

    This class is currently empty and will be expanded in future tasks to
    include size attributes and area methods.
    """

    """Initializes the instance
    of an object"""

    def __init__(self, size=0):
        """Default value if no size passed"""
        self.size = size

    def area(self):
        """
        Calculates the area of the square
        and returns it
        """
        return self.__size**2

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
