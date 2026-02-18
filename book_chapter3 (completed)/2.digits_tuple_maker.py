"""Task: Create a tuple of digits from a numeric string.

Reads a number as text, converts each digit to int and returns a tuple
containing those digits.
"""

# Ask the user to enter a number
number = input("Enter a number: ")

# Create a tuple from the digits of the number
result = tuple(int(digit) for digit in number)

print("Resulting tuple:", result)