"""Task: Concatenate digits of several numbers into one integer.

Takes a list of integers, extracts their digits in order, concatenates
them and prints the resulting integer.
"""

numbers = [12, 3, 456, 789]

count = []

for n in numbers:
    digits = [int(d) for d in str(n)]
    for d in digits:
        count.append(d)

result = int(''.join(str(c) for c in count))

print(result)  