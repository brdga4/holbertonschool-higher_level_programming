#!/usr/bin/python3
"""
This module provides a function that prints a formatted full name greeting.
It strictly validates that inputs are primitive string types.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'.

    Args:
        first_name (str): The first name string to print.
        last_name (str): The last name string to print (defaults to "").

    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
