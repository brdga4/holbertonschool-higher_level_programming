#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
It validates matrix structures, dimensions, data types,
and division constraints.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor number.

    Args:
        matrix (list of lists): Matrix containing integers or floats.
        div (int/float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix representing the division
        results rounded to 2 decimals.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div != div:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix[0], list):
        raise TypeError(error_msg)
    row_size = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(error_msg)
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)
            if element != element or element in (float('inf'), float('-inf')):
                raise TypeError(error_msg)

    return [
        [round(element / div, 2) + 0.0 for element in row]
        for row in matrix
    ]
