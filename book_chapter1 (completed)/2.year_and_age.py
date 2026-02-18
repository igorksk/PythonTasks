"""Task: Calculate a person's age from the current year and birth year.

Prompts for the current year and the user's birth year, computes
the age as the difference and prints the result.
"""

# Ask the user for the current year and birth year
current_year = int(input("Enter the current year (e.g., 2025): "))
birth_year = int(input("Enter your birth year (e.g., 1990): "))

# Calculate age
age = current_year - birth_year

# Print the result
print(f"You are {age} years old.")