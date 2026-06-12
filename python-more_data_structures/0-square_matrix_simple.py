#!/usr/bin/python3

def square_matrix_simple(matrix=[[]]):
    result = []
    for row in matrix:
        result += [list(map(lambda item: item ** 2, row))]
    return (result)
