from curses.ascii import isalpha

# Count the number of words in the book
def count_words(content_of_book):
    words = content_of_book.split()
    return len(words)

def counting_each_letter(content_of_book):
    letters = {}

    for letter in content_of_book.lower():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_on(item):
    return item["num"]

def sorting_letters_and_num(content_of_book):
    letters_and_nums = counting_each_letter(content_of_book)
    list_of_dic = []

    for char,num in letters_and_nums.items():
        if char.isalpha():
            list_of_dic.append({"char": char, "num": num})
    list_of_dic.sort(key=sort_on, reverse = True)
    return list_of_dic
