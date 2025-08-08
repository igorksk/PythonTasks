# Dictionary: key — author's last name, value — book title
books = {
    "Orwell": "1984",
    "Twain": "The Adventures of Tom Sawyer",
    "Austen": "Pride and Prejudice",
    "Hemingway": "The Old Man and the Sea",
    "Fitzgerald": "The Great Gatsby",
    "Dickens": "A Tale of Two Cities",
    "Rowling": "Harry Potter and the Philosopher's Stone",
    "Steinbeck": "Of Mice and Men",
    "Conrad": "Heart of Darkness",
    "Woolf": "Mrs Dalloway"
}

correct_answers = 0  # Counter for correct answers

print("Guess the author by the title of the book.\n")

# Iterate through the dictionary
for author, book in books.items():
    answer = input(f"Who is the author of '{book}'? ").strip()

    if answer.lower() == author.lower():
        print("Correct!\n")
        correct_answers += 1
    else:
        print(f"Incorrect. The correct answer is: {author}\n")

print(f"You got {correct_answers} out of {len(books)} correct.")