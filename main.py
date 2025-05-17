def get_book_text(filename):
    with open(filename) as f:
        file_content = f.read()
        num_words = len(file_content.split())
    return num_words



def main():
    #filename = input('Enter filename: ',)
    return get_book_text('books/frankenstein.txt')



print(f'{main()} words found in the document')