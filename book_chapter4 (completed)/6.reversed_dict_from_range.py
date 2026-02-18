"""Task: Build a dictionary mapping numbers 1..n to their reversed counterparts.

Prompts for a non-negative integer n, constructs `numbers = [1..n]` and
`reversed_numbers = numbers[::-1]`, then prints the mapping from each
original number to the corresponding reversed number.
"""

# Ask the user to enter a non-negative integer
n = input("Enter a non-negative integer: ")

# Check if the input is a valid non-negative integer
if not n.isdigit():
    print("Error: You must enter a non-negative integer.")
else:
    n = int(n)
    if n == 0:
        print("The list will be empty because you entered 0.")
    else:
        # Create a list of numbers from 1 to n
        numbers = list(range(1, n + 1))
        
        # Create a reversed version of the list
        reversed_numbers = numbers[::-1]
        
        # Create a dictionary where keys come from the original list
        # and values come from the reversed list
        result_dict = dict(zip(numbers, reversed_numbers))
        
        # Print the results
        print("List of numbers:", numbers)
        print("Resulting dictionary:", result_dict)