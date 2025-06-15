limit = int(input("Enter limit: "))

exceptions_input = input("Enter numbers for the exceptions list (space-separated): ")

exceptions_list = [int(num) for num in exceptions_input.split()]

result = 0;

for n in range(limit + 1):
    if n not in exceptions_list:
        result += n

print("Sum with exceptions: ", result)