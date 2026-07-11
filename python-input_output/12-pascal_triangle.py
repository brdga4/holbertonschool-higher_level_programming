#!/usr/bin/python3
"""Script"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(len(prev_row) - 1):
            sum_of_pair = prev_row[j] + prev_row[j + 1]
            new_row.append(sum_of_pair)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
