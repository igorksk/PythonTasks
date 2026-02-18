"""Task: Compare two integer lists for equality in order and length.

Defines `compare` that returns True when two lists have the same
length and identical elements at each position; otherwise False.
"""

def compare(list1, list2):

    if (len(list1) != len(list2)):
        return False;

    for i in range(len(list1)):
        for j in range(len(list2)):
            if i == j and list1[i] != list2[j]:
                return False

    return True;


print(compare([1, 2, 3], [1, 2, 3])) # True
print(compare([1, 2, 3], [3, 2, 1])) # False 
print(compare([1, 2, 3], [1, 2]))  # False

