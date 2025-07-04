from stats import number_of_words, character_counts, sorted_character_counts

book_path = "books/frankenstein.txt"
with open(book_path) as f:
    book_text = f.read()

num_words = number_of_words(book_text)
char_counts = character_counts(book_text)
sorted_char_counts = sorted_character_counts(char_counts)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for entry in sorted_char_counts:
    print(f"{entry['char']}: {entry['num']}")
print("============= END ==============")