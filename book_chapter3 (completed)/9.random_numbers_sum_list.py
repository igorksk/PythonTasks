import random

lst = []

for k in range(20):
    number = random.randint(0, 50)
    lst.append(number)

print("Initial list:", lst)

lst2 = []

for i in range(len(lst)):
    if i % 2 == 0:
        odd = lst[i]
        even = lst[i + 1]

        lst2.append(odd)
        lst2.append(even)
        lst2.append(odd + even)
        
print("New list:", lst2)