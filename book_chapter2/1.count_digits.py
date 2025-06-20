number = int(input("Enter number: "))

digits = [int(d) for d in str(number)]

count = {} #Dictionary

for d in digits:
    if d in count:
        count[d] += 1
    else:
        count[d] = 1

for digit in sorted(count):
    print(f"{digit} appears {count[digit]} times")        