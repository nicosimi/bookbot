from stats import get_num_words
from stats import get_num_char
from stats import get_char_count
import sys


def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()   
    return file_contents


def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print(f"Analyzing book found at {filepath}")
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    num_char = get_num_char(text)
    print("---------- Character Count -------")
    get_char_count(num_char)
    print("============= END ===============")



main()