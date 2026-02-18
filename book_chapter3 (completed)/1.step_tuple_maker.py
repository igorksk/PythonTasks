"""Task: Create a tuple from characters at regular steps in a string.

Prompts for text and a positive step index, then constructs a tuple
containing characters taken every `step` positions and prints it.
"""

# Ask the user to enter text
text = input("Enter text: ")

# Ask the user to enter the step index
step = int(input("Enter the step index (number): "))

# Check that the step is positive
if step <= 0:
    print("The index must be a positive number greater than 0.")
else:
    # Create a tuple with elements at every step
    result = tuple(text[i] for i in range(0, len(text), step))

    print("Resulting tuple:", result)