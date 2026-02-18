"""Task: Collect unique digits from two integers.

Reads two integers, extracts their digits and prints the set of
unique digits present in either number.
"""

number1 = int(input("Enter number 1: "))

number2 = int(input("Enter number 2: "))

digits1 = [int(d) for d in str(number1)]

digits2 = [int(d) for d in str(number2)]

all_digits = set()

for d in digits1:
    all_digits.add(d)

for d in digits2:
    all_digits.add(d)

print("All digits: ", all_digits)