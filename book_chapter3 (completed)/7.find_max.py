"""Task: Find the maximum value and its index in a list.

Implements a simple scan to determine the maximum element and its
position, demonstrated on a sample list.
"""

def max(arr):
    n = len(arr)
    max = arr[0]
    index = 0
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
            index = i

    return [max, index]

numbers = [42, 17, 93, 8, 56, 21, 67, 3, 88, 34, 76, 5, 60, 29, 14, 97, 12, 70, 39, 50]

print("List:", numbers)
print("Max number and index: ", max(numbers))