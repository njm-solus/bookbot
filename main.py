def get_book_text(filename):
    with open(filename) as f:
        file_content = f.read()
    return file_content



def main():
    #filename = input('Enter filename: ',)
    return get_book_text('books/frankenstein.txt')

print(main())
