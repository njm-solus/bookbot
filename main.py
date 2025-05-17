from stats import get_num_words


def get_book_text(filename):
    with open(filename) as f:
        file_content = f.read()
    return file_content



def main():
    #filename = input('Enter filename: ',)
    content = (get_book_text('books/frankenstein.txt'))
    words = get_num_words(content)
    return words 



print(f'{main()} words found in the document')