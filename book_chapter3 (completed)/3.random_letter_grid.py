"""Task: Create and print a random grid of lowercase letters.

Generates a rows x cols grid filled with random lowercase letters
and prints it to the console.
"""

import random
import string

def create_random_letter_grid(rows, cols):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            letter = random.choice(string.ascii_lowercase)
            row.append(letter)
        grid.append(row)
    return grid

rows = int(input("Enter rows length: "))
cols = int(input("Enter columns length: "))

grid = create_random_letter_grid(rows, cols)

# Print result
for row in grid:
    print(' '.join(row))