from stats import get_num_words
from stats import get_char_apps
from stats import sort
import sys


def get_book_text(filename):
    with open(filename) as f:
        file_content = f.read().lower()
    return file_content



def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    content = (get_book_text(filepath))
    words = get_num_words(content)
    appearances = get_char_apps(content)
    sorted = sort(appearances)
    return filepath, words, appearances, sorted

filepath, num_words, num_appearances, sorted = main()

#print(f'{num_words} words found in the document and {sorted}') #'''for key,value in num_appearances:'''}')
print('============ BOOKBOT ============')
print(f'Analyzing book found at {filepath}...')
print('----------- Word Count ----------')
print(f'Found {num_words} total words')
print('--------- Character Count -------')
for key, value in sorted.items():
    if key.isalpha():
        print(f'{key}: {value}')
print('============= END ===============')
