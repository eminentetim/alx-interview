#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's Triangle with `n` rows.
    :param n: Number of rows
    :return: A list of lists representing Pascal's Triangle
    """
    if n <= 0:
        return []

    # Start with the first row containing only one element: 1
    triangle = [[1]]

    # Generate rows from 1 to `n-1` (total `n` rows)
    for row_index in range(1, n):
        # Start the new row with the first element as 1
        new_row = [1]

        # Fill in the intermediate elements
        for col_index in range(1, row_index):
            # Each element is the sum of the two elements directly above it
            new_value = triangle[row_index - 1][col_index - 1] + triangle[row_index - 1][col_index]
            new_row.append(new_value)

        # Add the last element to complete the row
        new_row.append(1)

        # Add the new row to the triangle
        triangle.append(new_row)

    return triangle
