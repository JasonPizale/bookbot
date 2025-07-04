def get_book_text(books):
    with open(books) as f:
        content = f.read()
    return content
def main():
    print(get_book_text("books/frankenstein.txt"))
main()
