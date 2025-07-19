# List of English vowels
vowels = "aeiouyAEIOUY"

# Ask the user to enter some text
text = input("Enter some text: ")

# Set to store unique English vowels found in the text
found_vowels = set()

# Check each character in the text
for char in text:
    if char in vowels:
        found_vowels.add(char.lower())  # Store in lowercase for consistency

# Show the result
if found_vowels:
    print("English vowels found in the text:", ', '.join(sorted(found_vowels)))
else:
    print("No English vowels found in the text.")