"""Task: List numbers divisible by 3 or 4 but not by 12.

Builds and prints a list of integers in the range 0..49 that are
divisible by 3 or 4, excluding those divisible by 12.
"""

nums = [k for k in range(50)]

filtered_nums = []

for k in nums:
    if (k % 3==0 or k % 3==0) and k % 12!=0:
        filtered_nums.append(k)

print(filtered_nums)
