"""Task: Interleave two randomly generated lists.

Generates two random lists of equal length and produces a new list
by alternating elements from each input list (a1, b1, a2, b2, ...).
"""

import random

def create_random_list():
    lst = []

    for k in range(20):
        number = random.randint(0, 50)
        lst.append(number)

    return lst

lst1 = create_random_list()

print("Initial list 1:", lst1)

lst2 = create_random_list()

print("Initial list 2:", lst2)

lst3 = []

for a, b in zip(lst1, lst2):
    lst3.append(a)
    lst3.append(b)
        
print("New list:", lst3)