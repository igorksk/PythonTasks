"""Task: Count digit frequencies in an integer.

Reads an integer from input, counts how many times each digit
appears and prints the counts in ascending digit order.
"""

number = int(input("Enter number: "))

digits = [int(d) for d in str(number)]

count = {} #Dictionary

for d in digits:
    if d in count:
        count[d] += 1
    else:
        count[d] = 1

for digit in sorted(count):
    print(f"{digit} appears {count[digit]} times")        