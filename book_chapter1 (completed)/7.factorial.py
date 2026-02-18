"""Task: Compute factorials (recursive implementation).

Defines a recursive `factorial` function and prints the list of factorials
for numbers from 0 up to (n-1) where n is the user-provided non-negative
integer.
"""

def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a non-negative number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    nums = [factorial(k) for k in range(number)]
    print(nums)

