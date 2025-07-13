import random

lst = []

for k in range(20):
    number = random.randint(0, 50)
    lst.append(number)

print("Initial list:", lst)


def bubble_sort_even_asc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 2):
            if j % 2 == 0:
                if arr[j] > arr[j + 2]:
                    arr[j], arr[j + 2] = arr[j + 2], arr[j]


def bubble_sort_odd_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 2):
            if j % 2 == 1:
                if arr[j] < arr[j + 2]:
                    arr[j], arr[j + 2] = arr[j + 2], arr[j]


bubble_sort_even_asc(lst)
bubble_sort_odd_desc(lst)

print("Sorted list:", lst)

