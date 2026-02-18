"""Task: Check whether three lengths can form a triangle.

Prompts the user for three integers (triangle sides) and verifies the
triangle inequality (sum of any two sides greater than the third).
"""

user_input = input("Enter exactly three numbers (triangle sides), separated by spaces: ")

parts = user_input.split()

if len(parts) != 3:
    print("You must enter exactly 3 numbers.")
else:
    numbers = [int(num) for num in parts]

    if (numbers[0] + numbers[1] > numbers[2] and 
        numbers[0] + numbers[2] > numbers[1] and 
        numbers[1] + numbers[2] > numbers[0]
        ):
        print("Triangle exists")
    else: 
        print("Triangle not exists")
    