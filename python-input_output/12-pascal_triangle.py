#!/usr/bin/python3
"""
A a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    n (int): The number of rows to generate in Pascal's triangle.

    Returns:
    list of lists: A list of lists of integers representing Pascal's triangle.
                   Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                # Calculate the value based on the previous row
                prev_row = triangle[i - 1]
                value = prev_row[j - 1] + prev_row[j]
                row.append(value)
        triangle.append(row)

    return triangle