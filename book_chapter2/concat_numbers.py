numbers = [12, 3, 456, 789]

count = []

for n in numbers:
    digits = [int(d) for d in str(n)]
    for d in digits:
        count.append(d)

result = int(''.join(str(c) for c in count))

print(result)  