from stats import get_num_words
from stats import get_char_apps

def get_book_text(filename):
    with open(filename) as f:
        file_content = f.read().lower()
    return file_content



def main():
    #filename = input('Enter filename: ',)
    content = (get_book_text('books/frankenstein.txt'))
    words = get_num_words(content)
    appearances = get_char_apps(content)
    return words, appearances

num_words, num_appearances = main()

print(f'{num_words} words found in the document and {num_appearances}')
