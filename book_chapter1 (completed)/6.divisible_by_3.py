# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check divisibility by 3
if number % 3 == 0:
    print(f"{number} is divisible by 3.")
else:
    print(f"{number} is NOT divisible by 3.")