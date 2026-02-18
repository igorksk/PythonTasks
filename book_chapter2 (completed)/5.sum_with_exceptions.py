"""Task: Sum integers from 0 to limit excluding specified exceptions.

Prompts for an upper `limit` and a space-separated list of exception
integers; computes the sum of numbers in [0..limit] that are not in the
exceptions list and prints the result.
"""

limit = int(input("Enter limit: "))

exceptions_input = input("Enter numbers for the exceptions list (space-separated): ")

exceptions_list = [int(num) for num in exceptions_input.split()]

result = 0;

for n in range(limit + 1):
    if n not in exceptions_list:
        result += n

print("Sum with exceptions: ", result)