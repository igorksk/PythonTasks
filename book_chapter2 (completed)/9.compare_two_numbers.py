"""Task: Compare two real numbers and state their relation.

Prompts for two real numbers and prints whether they are equal,
or which one is greater. Handles invalid numeric input.
"""

try:
    # Ask the user to enter the first real number
    a = float(input("Enter the first number: "))
    
    # Ask the user to enter the second real number
    b = float(input("Enter the second number: "))
    
    # Use ternary operator to determine which is greater
    result = (
        "Both numbers are equal"
        if a == b
        else ("First number is greater" if a > b else "Second number is greater")
    )
    
    # Print the result
    print(result)

except ValueError:
    # Handle the case when the input is not a valid number
    print("Invalid input. Please enter valid real numbers.")