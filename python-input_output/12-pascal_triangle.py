#!/usr/bin/python3
"""
Function that returns Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        List of lists of integers representing Pascal’s triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_value = prev_row[j - 1] + prev_row[j]
            new_row.append(new_value)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
