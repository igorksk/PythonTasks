number = int(input("Enter number: "))

digits = [int(d) for d in str(number)]

count = []

for d in digits:
    count.append(9-d)

result = int(''.join(str(c) for c in count))

print(result)  