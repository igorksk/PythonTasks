"""Task: Fill and print a matrix in spiral order.

Provides `fill_spiral(rows, cols)` which returns a rows x cols matrix
filled with increasing integers in spiral order. Prompts for sizes
and prints the resulting matrix.
"""

def fill_spiral(rows, cols):
    """
    Create a 2D matrix filled with numbers in a spiral order.
    """
    matrix = [[0] * cols for _ in range(rows)]
    num = 1
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    while top <= bottom and left <= right:
        # Left to right (top row)
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Top to bottom (right column)
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Right to left (bottom row)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # Bottom to top (left column)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix

# Example usage
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
spiral = fill_spiral(rows, cols)

# Print the result
for row in spiral:
    print("\t".join(map(str, row)))
