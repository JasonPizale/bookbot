from stats import number_of_words

with open("books/frankenstein.txt") as f:
    book_text = f.read()

num_words = number_of_words(book_text)
print(f"{num_words} words found in the document")

from stats import character_counts
char_counts = character_counts(book_text)
for character, count in char_counts.items():
    print(f"'{character}': {count}")