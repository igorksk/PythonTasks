"""Task: Create a sequence defined by 5*k + 3.

Generates the first 10 values of the sequence 5*k + 3, prints the list,
and prints the reversed iterator (note: `reversed` returns an iterator).
"""

nums = [5 * k + 3 for k in range(10)]

print(nums)

print(reversed(nums))