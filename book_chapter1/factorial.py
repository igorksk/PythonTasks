def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a non-negative number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    nums = [factorial(k) for k in range(number)]
    print(nums)

