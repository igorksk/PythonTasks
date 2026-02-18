"""Task: Create pairs of odd numbers with their successor offset by 2.

Generates a list of [k, k+2] pairs for odd k in the range 0..49 and prints it.
"""

nums = [k for k in range(50)]

tuples_list = []

for k in nums:
    if k % 2 == 1:
        tuples_list.append([k, k+2])

print(tuples_list)