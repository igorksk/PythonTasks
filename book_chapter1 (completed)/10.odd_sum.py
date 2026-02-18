"""Task: Sum the odd numbers from a list.

Defines `odd_sum` which filters odd integers from the provided list
and returns their sum. Demonstrated with a sample list.
"""

def odd_sum(nums):

    odds = [k for k in nums if k%2==1]

    return sum(odds)

print(odd_sum([5,10,1,60,25,3]))