#!/usr/bin/python3
"""
This module provides a function that adds two numbers together.
It handles integers and floats safely, ensuring strict type checks.
It blocks indeterminate forms (NaN) and float overflows (Infinity).
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.
    """
    # 1. Validate 'a' for basic types, NaN, and Infinity
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")

    # 2. Validate 'b' for basic types, NaN, and Infinity
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    # 3. Cast to integer and return the sum
    return int(a) + int(b)
