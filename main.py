from stats import count_words, counting_each_letter, sorting_letters_and_num
import sys

# Main Function
def main():
    if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    bookpath = sys.argv[1]
    content = get_book_text(bookpath)
    num_words = count_words(content)
    letter_count = counting_each_letter(content)
    sorted_letters = sorting_letters_and_num(content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_letters:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

# Open the book and read its content
def get_book_text(book_path):
    with open(book_path, "r", encoding="utf-8") as book:
        book_contents = book.read()
        return book_contents


main()
