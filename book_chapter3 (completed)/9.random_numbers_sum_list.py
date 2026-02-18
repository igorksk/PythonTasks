"""Task: Generate a random list and build a combined list with sums.

Creates a random list and for each pair of elements at indices (i, i+1)
appends the first, the second and their sum to a new list, then prints it.
"""

import random

lst = []

for k in range(20):
    number = random.randint(0, 50)
    lst.append(number)

print("Initial list:", lst)

lst2 = []

for i in range(len(lst)):
    if i % 2 == 0:
        odd = lst[i]
        even = lst[i + 1]

        lst2.append(odd)
        lst2.append(even)
        lst2.append(odd + even)
        
print("New list:", lst2)