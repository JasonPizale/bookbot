def number_of_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

with open("books/frankenstein.txt") as f:
    book_text = f.read()

num_words = number_of_words(book_text)
print(f"{num_words} words found in the document")

