#!/usr/bin/python3
"""
Task 2: returns True if the object is exactly an
instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Task 2: returns True if the object is exactly an
    instance of the specified class ; otherwise False.
    """

    return type(obj) is a_class
