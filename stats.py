def words_in_book(book):
    book_words = book.split()
    return len(book_words)

def count_letters_in_book(book):
    letters_in_book = {}
    for letter in book:
        letter = letter.lower()
        if letter not in letters_in_book:
            letters_in_book[letter] = 1
        else:
            letters_in_book[letter] += 1
    return letters_in_book

def sort_on(items):
    return items["num"]

def create_dicts_for_letters(letters_in_book):
    letter_dicts_list = []
    for letter in letters_in_book:
        letter_dict = {}
        letter_dict["char"] = letter
        letter_dict["num"] = letters_in_book[letter]
        letter_dicts_list.append(letter_dict)

    letter_dicts_list.sort(reverse=True, key=sort_on)
    return letter_dicts_list
