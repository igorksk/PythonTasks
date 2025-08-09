# Ask the user to enter some text
text = input("Enter some text: ")

char_dict = {}

for i in range(len(text)):
    char = text[i]
    if char not in char_dict:  # only first occurrence
        modified_text = text[:i] + text[i+1:]
        char_dict[char] = modified_text

print("Character dictionary:", char_dict)