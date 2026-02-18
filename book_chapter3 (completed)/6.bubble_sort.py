"""Task: Sort a list using the bubble sort algorithm.

Defines `bubble_sort` which sorts the list in-place using bubble sort
and demonstrates the function on a sample list.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
numbers = [42, 17, 93, 8, 56, 21, 67, 3, 88, 34, 76, 5, 60, 29, 14, 97, 12, 70, 39, 50]

print("Unsorted list:", numbers)
bubble_sort(numbers)
print("Sorted list:", numbers)