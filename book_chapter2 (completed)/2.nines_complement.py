"""Task: Compute the nine's complement of a number.

Reads an integer, computes the nine's complement of each digit,
recombines the digits and prints the resulting integer.
"""

number = int(input("Enter number: "))

digits = [int(d) for d in str(number)]

count = []

for d in digits:
    count.append(9-d)

result = int(''.join(str(c) for c in count))

print(result)  