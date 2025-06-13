def fibonacci(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

number = int(input("Enter a non-negative number: "))

if number < 0:
    print("Fibonacci is not defined for negative numbers.")
else:
    nums = [fibonacci(k) for k in range(number)]
    print(nums)
