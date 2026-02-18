"""Task: Convert miles to kilometers.

Prompts the user for a distance in miles, converts it to kilometers
using the factor 1 mile = 1.60934 kilometers, and prints the result.
"""

# Ask the user to enter miles
miles = float(input("Enter distance in miles: "))

# Convert miles to kilometers
kilometers = miles * 1.60934

# Print the result
print(f"{miles} miles is equal to {kilometers} kilometers.")