"""Task: Return the second largest value from a list.

Defines `second_max` which removes the maximum value and returns
the next maximum. Demonstrates the function on a sample list.
"""

def second_max(nums):

    first_max = max(nums);

    nums.remove(first_max)

    return max(nums)

print(second_max([5,10,1,60,25,3]))