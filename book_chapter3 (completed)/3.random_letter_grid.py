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

# Печать результата
for row in grid:
    print(' '.join(row))