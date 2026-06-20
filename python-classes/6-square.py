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

    def __init__(self, size=0, position=(0, 0)):
        """Default value if no size passed"""
        self.size = size
        self.position = position

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

    def my_print(self):
        """Prints the square with character #"""
        if self.__size == 0:
            print()
            return
        x, y = self.__position[0], self.__position[1]
        i = 0
        for _ in range(y):
            print()
        while i < self.__size:
            print(x * " ", end="")
            print("#" * self.__size)
            i += 1

    @property
    def position(self):
        """getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
