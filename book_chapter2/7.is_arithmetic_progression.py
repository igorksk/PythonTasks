user_input = input("Enter exactly three numbers (arithmetic progression), separated by spaces: ")

parts = user_input.split()

if len(parts) != 3:
    print("You must enter exactly 3 numbers.")
else:
    numbers = [int(num) for num in parts]

    if (numbers[0] + numbers[1] == numbers[2] or 
        numbers[0] + numbers[2] == numbers[1] or 
        numbers[1] + numbers[2] == numbers[0]
        ):
        print("This is arithmetic progression")
    else: 
        print("This is NOT arithmetic progression")
    