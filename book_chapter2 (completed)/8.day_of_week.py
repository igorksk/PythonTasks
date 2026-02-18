"""Task: Map a number (1-7) to the corresponding weekday name.

Prompts for an integer between 1 and 7 and prints the corresponding
day name; validates the input range.
"""

# Ask the user to enter a number
number = int(input("Enter a number from 1 to 7: "))

# List of day names
days = [
    "Monday",    # 1
    "Tuesday",   # 2
    "Wednesday", # 3
    "Thursday",  # 4
    "Friday",    # 5
    "Saturday",  # 6
    "Sunday"     # 7
]

# Check if the number is in the valid range
if 1 <= number <= 7:
    day_name = days[number - 1]
    print("Day of the week:", day_name)
else:
    print("Invalid number. Please enter a number from 1 to 7.")