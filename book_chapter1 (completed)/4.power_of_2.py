"""Task: Generate powers of two.

Prompts for an integer n and constructs a list of 2**k for k in range(n),
then prints the list.
"""

number = int(input("Enter number: "))

nums = [2**k for k in range(number)]

print(nums)