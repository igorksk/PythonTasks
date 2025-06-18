import random

def create_random_number_grid(rows, cols):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            letter = random.randint(0, 9)
            row.append(letter)
        grid.append(row)
    return grid

rows = int(input("Enter rows length: "))
cols = int(input("Enter columns length: "))

grid = create_random_number_grid(rows, cols)

#Initial grid
for row in grid:
    print(row)

try:
    row_to_delete = int(input("Enter row to delete (starting from 0): "))
    if 0 <= row_to_delete < len(grid):
        del grid[row_to_delete]
    else:
        print("Wrong number.")
except ValueError:
    print("Enter correct number.")

try:
    col_to_delete = int(input("Enter column to delete (starting from 0): "))
    if 0 <= col_to_delete < cols:
        for row in grid:
            del row[col_to_delete]
    else:
        print("Wrong number.")
except ValueError:
    print("Enter correct number.")

#Grid after deletion
for row in grid:
    print(row)