def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    filepath = "/home/kio/Boot.dev/bookbot/books/frankenstein.txt"
    book_text = get_book_text(filepath)
    output = create_dicts_for_letters(count_letters_in_book(book_text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_in_book(book_text)} total words")
    print("--------- Character Count -------")
    for item in output:
        if item["char"].isalpha() == True:
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

from stats import words_in_book, count_letters_in_book, create_dicts_for_letters

main()