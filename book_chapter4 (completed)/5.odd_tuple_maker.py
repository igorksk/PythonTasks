nums = [k for k in range(50)]

tuples_list = []

for k in nums:
    if k % 2 == 1:
        tuples_list.append([k, k+2])

print(tuples_list)