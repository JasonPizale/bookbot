def number_of_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def character_counts(book_text):
    char_dict = {}
    for character in book_text:
        character = character.lower()
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict
        

