nums = [k for k in range(50)]

filtered_nums = []

for k in nums:
    if (k % 3==0 or k % 3==0) and k % 12!=0:
        filtered_nums.append(k)

print(filtered_nums)
