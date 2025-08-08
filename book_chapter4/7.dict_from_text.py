# Ask the user to enter some text
text = input("Enter some text: ")

dict = {}

for char in text:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

print("Character frequency dictionary:", dict) 
        
